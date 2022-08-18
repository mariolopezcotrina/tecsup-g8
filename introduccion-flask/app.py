from flask import Flask
from data import productos

app = Flask(__name__)

@app.route("/")
def index():
    return "Mi servidor flask funciona correctamente 😀🔥"

@app.route("/producto/<int:producto_id>")
def listaProductos(producto_id):
    data = None
    for producto in productos:
        if producto['id'] == producto_id:
            data = producto
        
    if data:
        return {
            "success": True,
            "message": "Producto encontrado",
            "content": data
        }
    else:
        return {
            "success": False,
            "message": "Producto no encontrado",
            "content": None 
        }