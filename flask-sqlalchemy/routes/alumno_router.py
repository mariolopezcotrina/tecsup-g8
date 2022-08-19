from app import app
from controllers.alumno_controller import AlumnoController
from flask import request

@app.route("/alumnos", methods=['GET', 'POST'])
def alumnosAll():
    if request.method == 'GET':
        response = AlumnoController().get()
        return response
    else:
        json_input = request.get_json()
        response = AlumnoController().post(json_input)
        return response

@app.route("/alumno/<int:alumno_id>", methods=['PUT', 'DELETE'])
def alumnoUpdate(alumno_id):
    if request.method == 'PUT':
        json_input = request.get_json()
        response = AlumnoController().update(alumno_id, json_input)
        return response
    else:
        response = AlumnoController().delete(alumno_id)
        return response