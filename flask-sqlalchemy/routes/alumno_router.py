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