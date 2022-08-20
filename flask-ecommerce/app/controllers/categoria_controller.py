from app import db
from app.models.categoria_model import CategoriaModel
from app.schemas.categoria_schema import category_schema, categories_schema
from marshmallow import ValidationError

class CategoriaController():
    def getAll(self):
        categories = CategoriaModel.query.all()
        result = categories_schema.dump(categories)
        return result, 200

    def post(self, json_input):
        if not json_input:
            return {"message": "Datos de entrada no proporcionados"}, 400
        try:
            data = category_schema.load(json_input)
        except ValidationError as err:
            return err.messages, 422
        category = CategoriaModel(**data)
        db.session.add(category)
        db.session.commit()
        result = category_schema.dump(category)
        return result, 201