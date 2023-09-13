from ..models.auth.usuario_model import Usuario
from flask import request, session
class UserController:
    @classmethod
    def login(cls):
        data = request.json
        usuario = Usuario(
            email = data.get('email'),
            password = data.get('password')
        )
        if Usuario.is_registered(usuario):
            session['email'] = data.get('email')
            return {"message": "Sesión iniciada"}, 200
        return {"message": "Usuario o contraseña incorrectos"}, 401
    @classmethod
    def logout(cls):
        session.pop('email', None)
        return {"message": "Sesión cerrada"}, 200

    @classmethod
    def show_profile(cls):
        email = session.get('email')
        usuario = Usuario.get(Usuario(email = email))
        if usuario is None:
            return {"message": "Usuario no encontrado"}, 404
        else:
            return usuario.serialize(), 200
