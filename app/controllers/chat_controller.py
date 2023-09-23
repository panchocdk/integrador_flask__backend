from ..models.chat_model import Chat
from flask import request, session
from ..models.exceptions import SourceNotFound, InvalidDataError

class ChatController:

    @classmethod
    def get(cls, chat_id):
        chat = Chat.get(Chat(chat_id=chat_id))
        if chat is not None:
            return chat.serialize(), 200
        else:
            raise SourceNotFound('Chat no encontrado')
    
    @classmethod
    def get_all(cls, channel_id):
        chat_objects = Chat.get_all(channel_id)
        chats = []
        for chat in chat_objects:
            chats.append(chat.serialize())
        return chats, 200
    
    @classmethod
    def create(cls):
        data = request.json
        data['user_id'] = session.get('user_id')
        chat = Chat(**data)
        Chat.create(chat)
        return {'message': 'Chat creado con exito'}, 201
        
    @classmethod
    def update(cls, chat_id):
        data = request.json
        data['chat_id'] = chat_id
        chat = Chat(**data)
        Chat.update(chat)
        return {'message': 'Chat modificado con exito'}, 201
    
    @classmethod
    def delete(cls, chat_id):
        chat = Chat(chat_id=chat_id)
        Chat.delete(chat)
        return {'message': 'Chat eliminado correctamente'}, 204