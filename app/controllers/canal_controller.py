from ..models.canales.canal_model import Canal
from flask import request

class CanalController:
    @classmethod
    def create_canal(cls):
        data = request.json
        canal = Canal(
            nombre_canal=data.get('nombre_canal'),
            servidor_id=data.get('servidor_id')
        )
        Canal.create(canal)
        return {'message': 'Canal creado con éxito'}, 201

    @classmethod
    def get_canal(cls, canal_id):
        canal = Canal(canal_id=canal_id)
        result = Canal.get(canal)
        if result is not None:
            return result.serialize(), 200
        else:
            return ({"message": "Canal no encontrado"}), 404

    @classmethod
    def get_all_canales(cls, servidor_id):
        canales = Canal.get_all_canales(servidor_id)
        if canales:
            return [canal.serialize() for canal in canales], 200
        else:
            return ({"message": "No se encontraron canales en este servidor"}), 404

    @classmethod
    def update_canal(cls, canal_id):
        data = request.json
        canal = Canal.get(canal_id)
        if canal is not None:
            canal.nombre_canal = data.get('nombre_canal', canal.nombre_canal)
            canal.servidor_id = data.get('servidor_id', canal.servidor_id)

            Canal.update(canal)
            return {"message": "Canal actualizado exitosamente"}, 200
        else: 
            return {"message": "Canal no encontrado"}, 404

    @classmethod
    def delete_canal(cls, canal_id):
        canal = Canal.get(canal_id)
        if canal is not None:
            Canal.delete(canal)
            return {"message": "Canal eliminado exitosamente"}, 200
        else:
            return {"message": "Canal no encontrado"}, 404
