from app import app
from app.controllers.usuario_controller import UsuarioController
from flask import request


@app.route("/registro/", methods=['POST'])
def registrarUsuario():
    json_input = request.get_json()
    usuario = UsuarioController().singUp(json_input)
    return usuario


@app.route("/login/", methods=['POST'])
def iniciarSesion():
    json_input = request.get_json()
    usuario = UsuarioController().singIn(json_input)
    return usuario