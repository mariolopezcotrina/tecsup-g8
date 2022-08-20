from unittest import result
from app import app
from flask import request
from app.controllers.preferencias_controller import PreferenciaController


@app.route("/preferencias/", methods=['GET', 'POST'])
def preferencias():
    if request.method == 'GET':
        preferences = PreferenciaController().getAll()
        return preferences
    else:
        json_input = request.get_json()
        result = PreferenciaController().post(json_input)
        return result