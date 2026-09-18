from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class MedicineCreate(BaseModel):
    sku: str
    name: str
    dosageForm: str
    packSize: str
    storage: str
    criticality: float = Field(ge=0.1, le=1.0)
    leadTimeDays: int
    therapeuticClass: str

class InventoryAdjustment(BaseModel):
    facility_id: str
    sku: str
    transaction_type: str
    quantity: int = Field(gt=0)
    lot: str
    expiry: date
    clinical_notes: Optional[str] = None