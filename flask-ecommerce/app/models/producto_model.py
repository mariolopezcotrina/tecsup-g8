from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Text,
    Boolean,
    DateTime,
    func
)
from app import db

class ProductoModel(db.Model):
    __tablename__ = 'productos'
    productoId = Column(Integer, primary_key=True)
    productoNombre = Column(String(255), nullable=False)
    productoDescripcion = Column(String(255), nullable=False)
    productoPrecio = Column(Float, nullable=False)
    productoImagen = Column(Text, nullable=False)
    estado = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    categoriaId = Column(Integer, db.ForeignKey('categorias.categoriaId'))
    categoria = db.relationship('CategoriaModel')
    preferenciaId = Column(Integer, db.ForeingKey('preferencias.preferenciaId'))
    preferencia = db.relationship('PreferenciaModel')
