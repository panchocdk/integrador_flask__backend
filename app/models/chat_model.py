from ..database import DatabaseConnection

class Chat:
    def __init__(self, **kwargs):
        self.chat_id = kwargs.get('chat_id')
        self.channel_id = kwargs.get('channel_id')
        self.user_id = kwargs.get('user_id')
        self.chat_date = kwargs.get('chat_date')
        self.message = kwargs.get('message')

    def serialize(self):
        return {
            'chat_id': self.chat_id,
            'channel_id': self.channel_id,
            'user_id': self.user_id,
            'chat_date': self.chat_date,
            'message': self.message
        }
    
    @classmethod
    def get(cls, chat):
        query = '''SELECT * FROM discord_chat.chats\
                    WHERE chat_id=%(chat_id)s'''
        params = chat.__dict__
        results = DatabaseConnection.fetch_one(query, params=params)
        if results is not None:
            return cls(
                chat_id = results[0],
                channel_id = results[1],
                user_id = results[2],
                chat_date = results[3],
                message = results[4]
            )
        return None
    
    @classmethod
    def get_all(cls, channel):
        query = '''SELECT c.* FROM discord_chat.chats c
                    INNER JOIN discord_chat.channels ch
                    ON c.channel_id = ch.channel_id
                    WHERE c.channel_id=%s'''
        params = channel,
        result = DatabaseConnection.fetch_all(query, params=params)
        chats = []
        if result is not None:
            for item in result:
                chats.append(cls(
                        chat_id = item[0],
                        channel_id = item[1],
                        user_id = item[2],
                        chat_date = item[3],
                        message = item[4]
                    ))
        return chats
    
    @classmethod
    def create(cls, chat):
        query = '''INSERT INTO discord_chat.chats (channel_id, user_id, message)
                    VALUES (%(channel_id)s, %(user_id)s, %(message)s)'''
        params = chat.__dict__
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def update(cls, chat):
        allowed_columns = {'channel_id', 'user_id', 'message'}
        query_parts = []
        params = []
        for key, value in chat.__dict__.items():
            if key in allowed_columns and value is not None:
                query_parts.append(f'{key} = %s')
                params.append(value)
        params.append(chat.chat_id)
        query = "UPDATE discord_chat.chats SET " + ", ".join(query_parts) + " WHERE chat_id = %s"
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def delete(cls, chat):
        query = '''DELETE FROM discord_chat.chats WHERE chat_id=%s'''
        params = chat.chat_id,
        DatabaseConnection.execute_query(query, params=params)