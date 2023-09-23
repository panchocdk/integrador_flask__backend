from ..models.role_model import Role
from flask import request

class RoleController:

    @classmethod
    def get(cls, role_id):
        role = Role.get(Role(role_id=role_id))
        if role is not None:
            return role.serialize(), 200
        return {'message': 'Rol no encontrado'}, 404
    
    @classmethod
    def get_all(cls):
        role_objects = Role.get_all()
        roles = []
        for role in role_objects:
            roles.append(role.serialize())
        return roles, 200
    
    @classmethod
    def create(cls):
        data = request.json
        role = Role(**data)
        if not Role.is_registered(role):
            Role.create(role)
            return {'message': 'Rol creado con exito'}, 201
        return {'message': 'Ya existe un rol con ese nombre'}, 400
    
    @classmethod
    def update(cls, role_id):
        data = request.json
        data['role_id'] = role_id
        role = Role(**data)
        if Role.is_registered(role):
            Role.update(role)
            return {'message': 'Rol modificado con exito'}, 201
        return {'message': 'Rol no encontrado'}, 400
    
    @classmethod
    def delete(cls, role_id):
        role = Role(role_id=role_id)
        if Role.is_registered(role):
            Role.delete(role)
            return {'message': 'Rol eliminado correctamente'}, 204