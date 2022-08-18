from flask import Flask, request, render_template
from data import productos

app = Flask(__name__)

@app.route("/")
def index():
    return "Mi servidor flask funciona correctamente 😀🔥"

@app.route("/producto/<int:producto_id>")
def buscarProductoId(producto_id):
    data = None
    for producto in productos:
        if producto['id'] == producto_id:
            data = producto
        
    if data:
        return {
            "success": True,
            "message": "Producto encontrado",
            "content": data
        }, 200
    else:
        return {
            "success": False,
            "message": "Producto no encontrado",
            "content": None 
        }, 404

@app.route("/productos/<string:producto_nombre>")
def buscarProductosNombre(producto_nombre):
    resultado = []
    for producto in productos:
        if producto_nombre in producto['nombre']:
            resultado.append(producto)
    
    if resultado:
        return {
            "success": True,
            "message": "Producto encontrado",
            "content": resultado
        }, 200
    else:
        return {
            "success": False,
            "message": "Producto no encontrado",
            "content": None 
        }, 400

@app.route("/producto/actualizar", methods=['POST', 'GET'])
def actualizarProducto():
    if request.method == 'POST':
        body = request.json
        try:
            productos.append(body)
            return {
                "success": True,
                "message": "El producto se creo correctamente",
                "content": productos
            }
        except Exception as e:
            return {
                "success": False,
                "message": e,
                "content": None
            }
    else:
        return "El verbo es {}".format(request.method)

@app.route("/headers")
def datosPorHeaders():
    print(request.headers['Authorization'])
    return "success"

@app.route("/html")
def html():
    nombre = "Paolo"
    return render_template('index.html', nombre=nombre)

@app.route("/subir-archivo", methods=['POST'])
def subirArchivo():
    if request.method == 'POST':
        archivo = request.files['foto']
        # archivo.save('/var/www/uploads/')
        print(archivo)
        return "success"
    else:
        return "Metodo inexistente"