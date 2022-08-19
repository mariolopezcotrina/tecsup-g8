from app import app
from models.alumno_model import AlumnoModel

@app.route("/alumnos")
def alumnosAll():
    alumnos = AlumnoModel.query.all()
    return "Algo"