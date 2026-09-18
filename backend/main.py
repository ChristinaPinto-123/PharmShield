import hashlib
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from contextlib import asynccontextmanager

from .database import engine, get_db, Base
from .models import Medicine, Batch, AuditLog
from .schemas import MedicineCreate, InventoryAdjustment

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Auto-generate tables on startup (prefer Alembic in production)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(title="PharmShield Core API", lifespan=lifespan)

# Allow requests from the single-file UI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/v1/medicines")
async def list_medicines(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Medicine))
    return result.scalars().all()

@app.post("/api/v1/medicines", status_code=status.HTTP_201_CREATED)
async def create_medicine(payload: MedicineCreate, db: AsyncSession = Depends(get_db)):
    existing = await db.get(Medicine, payload.sku)
    if existing:
        raise HTTPException(status_code=400, detail="SKU already registered")
    
    med = Medicine(
        sku=payload.sku,
        name=payload.name,
        dosage_form=payload.dosageForm,
        pack_size=payload.packSize,
        storage=payload.storage,
        criticality=payload.criticality,
        lead_time_days=payload.leadTimeDays,
        therapeutic_class=payload.therapeuticClass
    )
    db.add(med)
    
    # Write cryptographic audit row
    digest = hashlib.sha256(f"{payload.sku}:{payload.name}".encode()).hexdigest()[:8]
    log = AuditLog(
        event="FORMULARY_MEDICINE_CREATED",
        actor="System Client",
        details=f"Created {payload.name} ({payload.sku})",
        state_hash=digest,
        status="COMMITTED"
    )
    db.add(log)
    await db.commit()
    return {"status": "success", "sku": payload.sku}

@app.post("/api/v1/inventory/adjust")
async def record_adjustment(adj: InventoryAdjustment, db: AsyncSession = Depends(get_db)):
    batch = Batch(
        facility_id=adj.facility_id,
        sku=adj.sku,
        lot=adj.lot,
        quantity=adj.quantity,
        expiry=adj.expiry,
        status="Usable"
    )
    db.add(batch)
    
    log = AuditLog(
        event="INVENTORY_STOCK_UPDATE",
        actor="Facility Pharmacist",
        details=f"{adj.transaction_type}: {adj.quantity} units to lot {adj.lot}",
        state_hash=hashlib.sha256(adj.lot.encode()).hexdigest()[:8],
        status="COMMITTED"
    )
    db.add(log)
    await db.commit()
    return {"status": "success"}