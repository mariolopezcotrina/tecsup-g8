from app.models.producto_model import ProductoModel
from app.schemas.producto_schema import product_schema, products_schema
from marshmallow import ValidationError
from app import db
from flask_jwt_extended import jwt_required, get_jwt_identity


class ProductoController:
    def getAll(self):
        products = ProductoModel.query.all()
        result = products_schema.dump(products)
        return result, 200

    @jwt_required()
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

    @jwt_required()
    def getById(self, product_id):
        product = ProductoModel.query.filter_by(productoId=product_id).first()
        result = product_schema.dump(product)
        return result, 200

    @jwt_required()
    def getByCategoria(self, categoria_id):
        user_id = get_jwt_identity()
        if user_id == 2:
            products = ProductoModel.query.filter_by(categoriaId=categoria_id).all()
            result = products_schema.dump(products)
            return result, 200
        return {"message": "El usuario no tiene persmisos"}, 403