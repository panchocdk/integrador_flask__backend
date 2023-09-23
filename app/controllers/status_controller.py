from ..models.status_model import Status
from flask import request

class StatusController:

    @classmethod
    def get(cls, status_id):
        status = Status.get(Status(status_id=status_id))
        if status is not None:
            return status.serialize(), 200
        return {'message': 'Status no encontrado'}, 404
    
    @classmethod
    def get_all(cls):
        status_objects = Status.get_all()
        statuss = []
        for status in status_objects:
            statuss.append(status.serialize())
        return statuss, 200
    
    @classmethod
    def create(cls):
        data = request.json
        status = Status(**data)
        if not Status.is_registered(status):
            Status.create(status)
            return {'message': 'Status creado con exito'}, 201
        return {'message': 'Ya existe un status con ese nombre'}, 400
    
    @classmethod
    def update(cls, status_id):
        data = request.json
        data['status_id'] = status_id
        status = Status(**data)
        if Status.is_registered(status):
            Status.update(status)
            return {'message': 'Status modificado con exito'}, 201
        return {'message': 'Status no encontrado'}, 400
    
    @classmethod
    def delete(cls, status_id):
        status = Status(status_id=status_id)
        if Status.is_registered(status):
            Status.delete(status)
            return {'message': 'Canal eliminado correctamente'}, 204