from ..models.channel_model import Channel
from flask import request, session
from ..models.exceptions import SourceNotFound, InvalidDataError

class ChannelController:

    @classmethod
    def get(cls, channel_id):
        channel = Channel.get(Channel(channel_id=channel_id))
        if channel is not None:
            return channel.serialize(), 200
        else:
            raise SourceNotFound('Canal no encontrado')
    
    @classmethod
    def get_all(cls, server_name):
        channel_objects = Channel.get_all(server_name)
        channels = []
        for channel in channel_objects:
            channels.append(channel.serialize())
        return channels, 200
    
    @classmethod
    def create(cls):
        data = request.json
        if data.get('channel_name') is not None:
            if isinstance(data.get('channel_name'), str):
                data['channel_name'] = data.get('channel_name').strip()
            else:
                raise InvalidDataError('Ingrese un nombre valido para el canal')
        else:
            raise InvalidDataError('El nombre del canal es obligatorio')
        if data.get('server_name') is not None:
            if isinstance(data.get('server_name'), str):
                data['server_name'] = data.get('server_name').strip()
            else:
                raise InvalidDataError('Debe ingresar un numero entero')
        else:
            raise InvalidDataError('El id de servidor es obligatorio')
        if data.get('description') is not None:
            if isinstance(data.get('description'), str):
                data['description'] = data.get('description').strip()
            else:
                raise InvalidDataError('Ingrese una cadena valida para la descripcion')
        else:
            raise InvalidDataError('La descripcion es obligatoria')
        channel = Channel(**data)
        if not Channel.is_registered(channel):
            Channel.create(channel)
            return {'message': 'Canal creado con exito'}, 201
        else:
            raise InvalidDataError('Ya existe un canal con ese nombre')
    
    @classmethod
    def update(cls, channel_id):
        data = request.json
        if data.get('channel_name') is not None:
            if isinstance(data.get('channel_name'), str):
                data['channel_name'] = data.get('channel_name').strip()
            else:
                raise InvalidDataError('Ingrese un nombre valido para el canal')
        if data.get('description') is not None:
            if isinstance(data.get('description'), str):
                data['description'] = data.get('description').strip()
            else:
                raise InvalidDataError('Ingrese una cadena valida para la descripcion')
        data['channel_id'] = channel_id
        channel = Channel(**data)
        if Channel.is_registered(channel):
            Channel.update(channel)
            return {'message': 'Canal modificado con exito'}, 201
        else:
            raise SourceNotFound('Canal no encontrado')
    
    @classmethod
    def delete(cls, channel_id):
        channel = Channel(channel_id=channel_id)
        if Channel.is_registered(channel):
            Channel.delete(channel)
            return {'message': 'Canal eliminado correctamente'}, 204
        else:
            raise SourceNotFound('Canal no encontrado')