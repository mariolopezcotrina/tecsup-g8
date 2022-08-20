from marshmallow import Schema, fields
from app.helpers.error_helpers import campo_necesario


class PreferenciaSchema(Schema):
    preferenciaId = fields.Integer(dump_only=True)
    preferenciaNombre = fields.String(required=True, validate=campo_necesario)
    estado = fields.Boolean(dump_only=True)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

preference_schema = PreferenciaSchema()
preferences_schema = PreferenciaSchema(many=True)