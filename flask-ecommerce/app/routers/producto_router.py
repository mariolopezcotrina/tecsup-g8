from app import app
from flask import request
from app.controllers.product_controller import ProductoController


@app.route("/productos/", methods=['GET', 'POST'])
def productos():
    if request.method == 'GET':
        products = ProductoController().getAll()
        return products
    else:
        json_input = request.get_json()
        result = ProductoController().post(json_input)
        return result