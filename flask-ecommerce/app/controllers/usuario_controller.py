from app.schemas.usuario_schema import user_schema
from marshmallow import ValidationError
from app.models.usuario_model import UsuarioModel
from app import db
import bcrypt

class UsuarioController():
    def singUp(self, json_input):
        if not json_input:
            return {"message": "Datos de usuario no encontrado"}, 400
        try:
            data = user_schema.load(json_input)
        except ValidationError as err:
            return err.messages, 422
        #encriptamos la contraseña
        hashe = bytes(data['usuarioPassword'], 'utf-8')
        salt = bcrypt.gensalt()
        passwordHashed = bcrypt.hashpw(hashe, salt)
        saltDecoded = salt.decode('utf-8')
        passwordHashedDecoded = passwordHashed.decode('utf-8')
        usuario = UsuarioModel(
            usuarioNombre=data['usuarioNombre'],
            usuarioEmail=data['usuarioEmail'],
            usuarioDni=data['usuarioDni'],
            usuarioFono=data['usuarioFono'],
            usuarioHash=passwordHashedDecoded,
            usuarioSalt=saltDecoded
        )
        db.session.add(usuario)
        db.session.commit()
        result = user_schema.dump(usuario)
        return result, 201

    def singIn():
        pass