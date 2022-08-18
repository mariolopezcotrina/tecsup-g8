from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Mi servidor flask funciona correctamente 😀🔥"

@app.route("/productos")
def productos():
    return {
        "id": 1,
        "nombre": "Sandwich de Chocolate", 
        "precio": 10
    }