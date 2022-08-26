from app import app
from flask import request
from app.controllers.product_controller import ProductoController
from flask_jwt_extended import jwt_required


@app.route("/productos/", methods=['GET', 'POST'])
def productos():
    if request.method == 'GET':
        products = ProductoController().getAll()
        return products
    else:
        json_input = request.get_json()
        result = ProductoController().post(json_input)
        return result


@app.route("/productos/get_by_id/<int:producto_id>", methods=['GET'])
def productoPorId(producto_id):
    producto = ProductoController()
    return producto.getById(producto_id)


@app.route("/productos/get_by_categoria_id/<int:categoria_id>", methods=['GET'])
def productoPorCategoria(categoria_id):
    productos = ProductoController()
    return productos.getByCategoria(categoria_id)