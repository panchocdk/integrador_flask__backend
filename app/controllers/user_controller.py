from ..models.user_model import User
from flask import request, session
from datetime import date
from ..models.exceptions import SourceNotFound, InvalidDataError

class UserController:

    @classmethod
    def login(cls):
        data = request.json
        user = User(
            email = data.get('email'),
            password = data.get('password')
        )
        if User.is_registered(user):
            session['email'] = data.get('email')
            user_l = User.get(User(email = session.get('email')))
            session['user_id'] = user_l.user_id
            return {"message": "Sesion iniciada"}, 200
        else:
            return {"message": "Usuario o contraseña incorrectos"}, 401
    
    @classmethod
    def show_profile(cls):
        username = session.get('email')
        user = User.get(User(email = username))
        if user is not None:
            return user.serialize(), 200
        else:
            raise SourceNotFound('Usuario no encontrado')
        
    @classmethod
    def logout(cls):
        session.pop('email', None)
        return {"message": "Sesion cerrada"}, 200
    
    @classmethod
    def create(cls):
        data = request.json
        if data.get('user_name') is not None:
            if isinstance(data.get('user_name'), str):
                data['user_name'] = data.get('user_name').strip()
            else:
                raise InvalidDataError('Debe ingresar una cadena de caracteres para el nombre de usuario')
        else:
            raise InvalidDataError('El nombre de usuario es obligatorio')
        if data.get('email') is not None:
            if isinstance(data.get('email'), str):
                data['email'] = data.get('email').strip()
            else:
                raise InvalidDataError('Ingrese una direccion de mail valida')
        else:
            raise InvalidDataError('El email es obligatorio')
        if data.get('first_name') is not None:
            if isinstance(data.get('first_name'), str):
                data['first_name'] = data.get('first_name').strip()
            else:
                raise InvalidDataError('Ingrese una cadena valida para el nombre')
        else:
            raise InvalidDataError('El nombre es obligatorio')
        if data.get('last_name') is not None:
            if isinstance(data.get('last_name'), str):
                data['last_name'] = data.get('last_name').strip()
            else:
                raise InvalidDataError('Ingrese una cadena valida para el apellido')
        else:
            raise InvalidDataError('El apellido es obligatorio')
        if data.get('password') is not None:
            if len(data.get('password'))>=8:
                data['password'] = data.get('password')
            else:
                raise InvalidDataError('La contraseña debe tener al menos 8 caracteres')
        else:
            raise InvalidDataError('La contraseña es obligatoria')
        if data.get('date_of_birth') is not None:
            if isinstance(data.get('date_of_birth'), str):
                data['date_of_birth'] = data.get('date_of_birth')
            else:
                raise InvalidDataError('Ingrese un formato de fecha valido')
        else:
            raise InvalidDataError('La fecha de nacimiento es obligatoria')
        data['status_id'] = 1
        data['role_id'] = 1
        data['profile_image'] = 'users\profile.png'
        user = User(**data)
        if not User.is_registered(user):
            User.create(user)
            return {'message': 'User created successfully'}, 201
        else:
            return {'message': 'Ya existe un usuario con esos datos'}, 400
    
    @classmethod
    def update(cls, user_id):
        data = request.json
        if data.get('user_name') is not None:
            if isinstance(data.get('user_name'), str):
                data['user_name'] = data.get('user_name').strip()
            else:
                raise InvalidDataError('Debe ingresar una cadena de caracteres para el nombre de usuario')
        if data.get('email') is not None:
            if isinstance(data.get('email'), str):
                data['email'] = data.get('email').strip()
            else:
                raise InvalidDataError('Ingrese una direccion de mail valida')
        if data.get('first_name') is not None:
            if isinstance(data.get('first_name'), str):
                data['first_name'] = data.get('first_name').strip()
            else:
                raise InvalidDataError('Ingrese una cadena valida para el nombre')
        if data.get('last_name') is not None:
            if isinstance(data.get('last_name'), str):
                data['last_name'] = data.get('last_name').strip()
            else:
                raise InvalidDataError('Ingrese una cadena valida para el apellido')
        if data.get('password') is not None:
            if len(data.get('password'))>=8:
                data['password'] = data.get('password').strip()
            else:
                raise InvalidDataError('La contraseña debe tener al menos 8 caracteres')
        if data.get('date_of_birth') is not None:
            if isinstance(data.get('date_of_birth'), date):
                data['date_of_birth'] = data.get('date_of_birth')
            else:
                raise InvalidDataError('Ingrese un formato de fecha valido')
        data['user_id'] = user_id
        user = User(**data)
        if User.is_registered(user):
            User.update(user)
            if data.get('email') is not None:
                session['email'] = data.get('email')
            return {'message': 'User updated successfully'}, 201
        else:
            raise SourceNotFound('No existe un usuario con esos datos')
        
    @classmethod
    def get_all(cls):
        user_objects = User.get_all()
        users = []
        for user in user_objects:
            users.append(user.serialize())
        return users, 200
    
    @classmethod
    def delete(cls, user_id):
        user = User(user_id=user_id)
        if User.is_registered(user):
            User.delete(user)
            return {'message': 'Usuario eliminado correctamente'}, 204
        raise SourceNotFound('Usuario no encontrado')

    @classmethod
    def get(cls, user_id):
        user = User.get(User(user_id = user_id))
        if user is not None:
            return user.serialize(), 200
        else:
            raise SourceNotFound('Usuario no encontrado')