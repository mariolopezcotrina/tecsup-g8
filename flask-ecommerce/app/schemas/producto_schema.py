from marshmallow import Schema, fields
from app.helpers.error_helpers import campo_necesario

class ProductoSchema(Schema):
    productoId = fields.Integer(dump_only=True)
    productoNombre = fields.String(required=True, validate=campo_necesario)
    productoDescripcion = fields.String(required=True, validate=campo_necesario)
    productoPrecio = fields.Float(required=True, validate=campo_necesario)
    productoImagen = fields.String(required=True, validate=campo_necesario)
    estado = fields.Boolean(dump_only=True)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    categoriaId = fields.Integer(required=True, validate=campo_necesario)
    preferenciaId = fields.Integer(required=True, validate=campo_necesario)

product_schema = ProductoSchema()
products_schema = ProductoSchema(many=True)
    