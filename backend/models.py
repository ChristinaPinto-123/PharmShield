from datetime import date, datetime
from sqlalchemy import Column, String, Float, Integer, ForeignKey, DateTime, Date
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Medicine(Base):
    __tablename__ = "medicines"

    sku = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    dosage_form = Column(String, nullable=False)
    pack_size = Column(String, nullable=False)
    storage = Column(String, nullable=False)
    criticality = Column(Float, nullable=False)
    lead_time_days = Column(Integer, nullable=False)
    therapeutic_class = Column(String, nullable=False)

    batches = relationship("Batch", back_populates="medicine", cascade="all, delete-orphan")

class Batch(Base):
    __tablename__ = "facility_batches"

    id = Column(Integer, primary_key=True, autoincrement=True)
    facility_id = Column(String, index=True, nullable=False)
    sku = Column(String, ForeignKey("medicines.sku", ondelete="CASCADE"), nullable=False)
    lot = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    expiry = Column(Date, nullable=False)
    temperature = Column(String, default="Controlled")
    status = Column(String, default="Usable")

    medicine = relationship("Medicine", back_populates="batches")

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    event = Column(String, nullable=False)
    actor = Column(String, nullable=False)
    details = Column(String, nullable=False)
    state_hash = Column(String, nullable=False)
    status = Column(String, nullable=False)