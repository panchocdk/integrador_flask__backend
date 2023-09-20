from ..models.servidores.servidor_model import Servidor
from flask import request

class ServidorController:
    @classmethod
    def create_servidor(cls):
        data = request.json
        servidor = Servidor(
            nombre_servidor=data.get('nombre_servidor'),
            descripcion=data.get('descripcion'),
            imagen_servidor=data.get('imagen_servidor'),
            creador_id=data.get('creador_id')
        )
        
        Servidor.create(servidor)
        return {'message': 'Servidor creado con exito'}, 201

    @classmethod
    def get_servidor(cls, servidor_id):
        servidor = Servidor(servidor_id=servidor_id)
        result = Servidor.get(servidor)
        if result is not None:
            return result.serialize(), 200
        else:
            return ({"message": "Servidor no encontrado"}), 404
    @classmethod
    def get_all(cls):
        servidor_objects = Servidor.get_all()
        servidores = []
        for servidor in servidor_objects:
            servidores.append(servidor.serialize())
        return servidores, 200
    def exists(self, servidor_id):
        servidor = Servidor(servidor_id=servidor_id)
        result = Servidor.get(servidor)
        if result is not None:
            return True
        else:
            return False
    @classmethod
    def update_servidor(cls, servidor_id):
        data = request.json
        servidor = Servidor.get(servidor_id)
        if cls.exists(cls, servidor_id):
            servidor.nombre_servidor = data.get('nombre_servidor', servidor.nombre_servidor)
            servidor.descripcion = data.get('descripcion', servidor.descripcion)
            servidor.imagen_servidor = data.get('imagen_servidor', servidor.imagen_servidor)
            servidor.creador_id = data.get('creador_id', servidor.creador_id)
            
            Servidor.update(servidor)
            return {"message": "Servidor actualizado exitosamente"}, 200
        else: 
            return {"message": "Servidor no encontrado"}, 404

    @classmethod
    def delete_servidor(cls, servidor_id):
        servidor = Servidor.get(servidor_id)
        if cls.exists(cls, servidor_id):
            Servidor.delete(servidor)
            return {"message": "Servidor eliminado exitosamente"}, 200
        return {"message": "Servidor no encontrado"}, 404
