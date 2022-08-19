from models.alumno_model import AlumnoModel

class AlumnoController():

    def get(self):
        alumnos = AlumnoModel.query.all()
        resultado = []
        for alumnos in alumnos:
            resultado.append(alumnos.json())
        return {
            "succes": True,
            "message": "Lista de alumnos",
            "content": resultado
        }
    
    def post(self, data):
        resultado = AlumnoModel(data['alumnoNombre'], data['alumnoDni'], data['alumnoEdad']).guardar_db()
        return {
            "success": True,
            "message": "Alumno creado",
            "content": resultado
        }