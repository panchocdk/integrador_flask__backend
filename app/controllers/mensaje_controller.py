from ..models.mensajes.mensaje_model import Mensaje
from flask import request

class MensajeController:
    @classmethod
    def create_mensaje(cls):
        data = request.json
        mensaje = Mensaje(
            contenido_mensaje=data.get('contenido_mensaje'),
            fecha_hora=data.get('fecha_hora'),
            usuario_id=data.get('usuario_id'),
            canal_id=data.get('canal_id')
        )
        
        Mensaje.create(mensaje)
        return {'message': 'Mensaje creado con éxito'}, 201

    @classmethod
    def get_mensaje(cls, mensaje_id):
        mensaje = Mensaje(mensaje_id=mensaje_id)
        result = Mensaje.get(mensaje)
        if result is not None:
            return result.serialize(), 200
        else:
            return {"message": "Mensaje no encontrado"}, 404

    @classmethod
    def get_all(cls, canal_id):
        mensaje_objects = Mensaje.get_all(canal_id)
        mensajes = []
        for mensaje in mensaje_objects:
            mensajes.append(mensaje.serialize())
        return mensajes, 200

    @classmethod
    def update_mensaje(cls, mensaje_id):
        data = request.json
        mensaje = Mensaje.get(mensaje_id)
        if mensaje:
            mensaje.contenido_mensaje = data.get('contenido_mensaje', mensaje.contenido_mensaje)
            mensaje.fecha_hora = data.get('fecha_hora', mensaje.fecha_hora)
            mensaje.usuario_id = data.get('usuario_id', mensaje.usuario_id)
            mensaje.canal_id = data.get('canal_id', mensaje.canal_id)
            
            Mensaje.update(mensaje)
            return {"message": "Mensaje actualizado exitosamente"}, 200
        else: 
            return {"message": "Mensaje no encontrado"}, 404

    @classmethod
    def delete_mensaje(cls, mensaje_id):
        mensaje = Mensaje.get(mensaje_id)
        if mensaje:
            Mensaje.delete(mensaje)
            return {"message": "Mensaje eliminado exitosamente"}, 200
        return {"message": "Mensaje no encontrado"}, 404
