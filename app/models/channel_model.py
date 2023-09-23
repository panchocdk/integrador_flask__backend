from ..database import DatabaseConnection

class Channel:

    def __init__(self, **kwargs):
        self.channel_id = kwargs.get('channel_id')
        self.channel_name = kwargs.get('channel_name')
        self.server_id = kwargs.get('server_id')
        self.description = kwargs.get('description')

    def serialize(self):
        return {
            'channel_id': self.channel_id,
            'channel_name': self.channel_name,
            'server_id': self.server_id,
            'description': self.description
        }
    
    @classmethod
    def is_registered(cls, channel):
        query = '''SELECT channel_id FROM discord_chat.channels\
                    WHERE channel_name=%(channel_name)s OR channel_id=%(channel_id)s'''
        params = channel.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)
        if result is not None:
            return True
        return False
    
    @classmethod
    def get(cls, channel):
        query = '''SELECT * FROM discord_chat.channels\
                    WHERE channel_id=%(channel_id)s'''
        params = channel.__dict__
        results = DatabaseConnection.fetch_one(query, params=params)
        if results is not None:
            return cls(
                chanel_id = results[0],
                channel_name = results[1],
                server_id = results[2],
                description = results[3]
            )
        return None
    
    @classmethod
    def get_all(cls, server):
        query = '''SELECT * FROM discord_chat.channels
                    WHERE server_id=%s'''
        paramas= server,
        results = DatabaseConnection.fetch_all(query, params=paramas)
        channels = []
        if results is not None:
            for result in results:
                channels.append(cls(
                        channel_id = result[0],
                        channel_name = result[1],
                        server_id = result[2],
                        description = result[3]
                    ))
        return channels
    
    @classmethod
    def create(cls, channel):
        query = '''INSERT INTO discord_chat.channels (channel_name, server_id, description)
                    VALUES (%(channel_name)s, %(server_id)s, %(description)s)'''
        params = channel.__dict__
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def update(cls, channel):
        allowed_columns = {'channel_name', 'server_id', 'description'}
        query_parts = []
        params = []
        for key, value in channel.__dict__.items():
            if key in allowed_columns and value is not None:
                query_parts.append(f'{key} = %s')
                params.append(value)
        params.append(channel.channel_id)
        query = "UPDATE discord_chat.channels SET " + ", ".join(query_parts) + " WHERE channel_id = %s"
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def delete(cls, channel):
        query = '''DELETE FROM discord_chat.channels WHERE channel_id=%s'''
        params = channel.channel_id,
        DatabaseConnection.execute_query(query, params=params)