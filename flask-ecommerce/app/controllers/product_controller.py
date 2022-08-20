from app.models.producto_model import ProductoModel
from app.schemas.producto_schema import product_schema, products_schema
from marshmallow import ValidationError
from app import db

class ProductoController():
    def getAll(self):
        products = ProductoModel.query.all()
        result = products_schema.dump(products)
        return result, 200

    def post(self, json_input):
        if not json_input:
            return {"message": "Datos de entrada no proporcionados"}, 400
        try:
            data = product_schema.load(json_input)
        except ValidationError as err:
            return err.messages, 422
        
        product = ProductoModel(**data)
        db.session.add(product)
        db.session.commit()
        result = product_schema.dump(product)
        return result, 201