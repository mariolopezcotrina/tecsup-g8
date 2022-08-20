from app.models.preferencia_model import PreferenciaModel
from app.schemas.preferencia_schema import preference_schema, preferences_schema


class PreferenciaController():
    def getAll(self):
        preferences = PreferenciaModel.query.all()
        result = preferences_schema.dump(preferences)
        return result

    def post(self, json_input):
        pass