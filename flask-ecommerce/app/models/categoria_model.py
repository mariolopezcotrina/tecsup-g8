from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    func
)
from app import db

class CategoriaModel(db.Model):
    __tablename__ = 'categorias'
    categoriaId = Column(Integer, primary_key=True)
    categoriaNombre = Column(String(255), nullable=False)
    categoriaDescripcion = Column(String(255), nullable=False)
    estado = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())