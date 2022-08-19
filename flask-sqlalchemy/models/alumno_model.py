from app import db
from sqlalchemy import func

class AlumnoModel(db.Model):
    alumnoId = db.Column(db.Integer, primary_key=True)
    alumnoNombre = db.Column(db.String(100), nullable=False)
    alumnoDni = db.Column(db.String(8), nullable=False)
    alumnosEdad = db.Column(db.Integer, nullable=False)
    createdAt = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __init__(self, nombre, dni, edad) -> None:
        self.alumnoNombre = nombre
        self.alumnoDni = dni
        self.alumnosEdad = edad

    def json(self):
        return {
            "alumnoId": self.alumnoId,
            "alumnoNombre": self.alumnoNombre,
            "alumnoDni": self.alumnoDni,
            "alumnoEdad": self.alumnosEdad,
            "createdAt": self.createdAt
        }

    def guardar_db(self):
        db.session.add(self)
        db.session.commit()
        return {
            "alumnoId": self.alumnoId,
            "alumnoNombre": self.alumnoNombre,
            "alumnoDni": self.alumnoDni,
            "alumnoEdad": self.alumnosEdad,
            "createdAt": self.createdAt
        }