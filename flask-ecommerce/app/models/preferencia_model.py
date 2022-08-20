from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    func
)
from app import db


class PreferenciaModel(db.Model):
    __tablename__ = 'preferencias'
    preferenciaId = Column(Integer, primary_key=True)
    preferenciaNombre = Column(String(255), nullable=False)
    estado = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())