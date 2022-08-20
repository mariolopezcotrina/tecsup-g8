from app.models.preferencia_model import PreferenciaModel
from app.schemas.preferencia_schema import preference_schema, preferences_schema
from marshmallow import ValidationError
from app import db


class PreferenciaController():
    def getAll(self):
        preferences = PreferenciaModel.query.all()
        result = preferences_schema.dump(preferences)
        return result, 200

    def post(self, json_input):
        if not json_input:
            return {"message": "Datos de entrada no proporcionados"}, 400
        try:
            data = preference_schema.load(json_input)
        except ValidationError as err:
            return err.messages, 422
        preference = PreferenciaModel(**data)
        db.session.add(preference)
        db.session.commit()
        result = preference_schema.dump(preference)
        return result, 201