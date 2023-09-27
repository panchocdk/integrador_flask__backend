from ..models.server_model import Server
from flask import request, session
from ..models.exceptions import SourceNotFound, InvalidDataError

class ServerController:

    @classmethod
    def show_servers(cls):
        server_objects = Server.get_all()
        servers = []
        for server in server_objects:
            servers.append(server.serialize())
        return servers, 200
    
    @classmethod
    def create(cls):
        data = request.json
        if data.get('server_name') is not None:
            if isinstance(data.get('server_name'), str):
                data['server_name'] = data.get('server_name').strip()
            else:
                raise InvalidDataError('Ingrese un nombre valido para el servidor')
        else:
            raise InvalidDataError('El nombre del servidor es obligatorio')
        if data.get('description') is not None:
            data['description'] = data.get('description').strip()
        session['server_name'] = data.get('server_name')
        data['icon_image'] = 'app\static\default\topic.png'
        server = Server(**data)
        if not Server.is_registered(server):
            Server.create(server)
            serv = Server.get(Server(server_name = session.get('server_name')))
            uid = session.get('user_id')
            Server.create_uxs(uid, serv.server_id, True)
            return {'message': 'Servidor creado con exito'}, 201
        else:
            raise InvalidDataError('Ya existe un servidor con ese nombre')

    @classmethod
    def add_user_server(cls):
        data = request.json
        serv = Server.get(Server(server_name = data.get('server_name')))
        uid = session.get('user_id')
        if not Server.exist_uxs(uid, serv.server_id):
            Server.create_uxs(uid, serv.server_id, False)
            return {'messge': 'Relacion creada con exito'}, 201
        else:
            raise InvalidDataError('El usuario ya pertenece al servidor')
        
    @classmethod
    def get_uxs(cls):
        user = session.get('user_id')
        uxs_objects = Server.get_uxs(user)
        uxs = []
        for item in uxs_objects:
            uxs.append(item.serialize())
        return uxs, 200
    
    @classmethod
    def update(cls, server_id):
        data = request.json
        data['server_id'] = server_id
        server = Server(**data)
        if Server.is_registered(server):
            Server.update(server)
            return {'message': 'Servidor modificado con exito'}, 201
        else:
            raise SourceNotFound('Servidor no enocontrado')
        
    @classmethod
    def delete(cls, server_id):
        server = Server(server_id=server_id)
        if Server.is_registered(server):
            Server.delete(server)
            return {'message': 'Servidor eliminado correctamente'}, 204
        else:
            raise SourceNotFound('Servidor no encontrado')
        
    @classmethod
    def get(cls, server_id):
        server = Server.get(Server(server_id=server_id))
        if server is not None:
            return server.serialize(), 200
        else:
            raise SourceNotFound('Servidor no encontrado')