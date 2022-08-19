from datetime import timedelta
from app import db
from sqlalchemy import func

class AlumnosModel(db.Model):
    alumnoId = db.Column(db.Integer, primery_key=True)
    alumnoNombre = db.Column(db.String(100), nullable=False)
    alumnoDni = db.Column(db.String(8), nullable=False)
    alumnosEdad = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime(timedelta=True), server_default=func.now())