from app.models.categoria_model import CategoriaModel
from app.schemas.categoria_schema import category_schema, categories_schema


class CategoriaController():
    def getAll():
        categories = CategoriaModel.query.all()
        result = categories_schema.dump(categories)
        return result, 200

    def post(self, data):
        pass
