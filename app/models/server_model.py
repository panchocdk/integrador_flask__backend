from ..database import DatabaseConnection

class Server:

    def __init__(self, **kwargs):
        self.server_id = kwargs.get('server_id')
        self.server_name = kwargs.get('server_name')
        self.description = kwargs.get('description')
        self.icon_image = kwargs.get('icon_image')

    def serialize(self):
        return {
            'server_id': self.server_id,
            'server_name': self.server_name,
            'description': self.description,
            'icon_image': self.icon_image
        }
    
    @classmethod
    def is_registered(cls, server):
        query = '''SELECT server_id FROM discord_chat.servers\
                    WHERE server_name=%(server_name)s OR server_id=%(server_id)s'''
        params = server.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)
        if result is not None:
            return True
        return False

    @classmethod
    def get(cls, server):
        query = '''SELECT * FROM discord_chat.servers\
                    WHERE server_id=%(server_id)s OR server_name=%(server_name)s'''
        params = server.__dict__
        results = DatabaseConnection.fetch_one(query, params=params)
        if results is not None:
            return cls(
                server_id = results[0],
                server_name = results[1],
                description = results[2],
                icon_image = results[3]
            )
        return None
    
    @classmethod
    def get_all(cls):
        query = '''SELECT * FROM discord_chat.servers'''
        results = DatabaseConnection.fetch_all(query)
        servers = []
        if results is not None:
            for result in results:
                servers.append(cls(
                        server_id = result[0],
                        server_name = result[1],
                        description = result[2],
                        icon_image = result[3]
                    ))
        return servers

    @classmethod
    def create(cls, server):
        query = '''INSERT INTO discord_chat.servers (server_name, description, icon_image)
                    VALUES (%(server_name)s, %(description)s, %(icon_image)s)'''
        params = server.__dict__
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def create_uxs(cls, user, server, creator):
        query = '''INSERT INTO discord_chat.user_servers (user_id, server_id, creator)
                    VALUES (%s, %s, %s)'''
        params = (user, server, creator)
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def get_uxs(cls, user):
        query = '''SELECT s.* FROM discord_chat.user_servers uxs
                    INNER JOIN discord_chat.servers s
                    ON uxs.server_id = s.server_id
                    WHERE uxs.user_id=%s'''
        params = user,
        result = DatabaseConnection.fetch_all(query, params=params)
        uxss = []
        if result is not None:
            for item in result:
                uxss.append(cls(
                        server_id = item[0],
                        server_name = item[1],
                        description = item[2],
                        icon_image = item[3]
                    ))
        return uxss
    
    @classmethod
    def exist_uxs(cls, user, server):
        query = '''SELECT * from discord_chat.user_servers 
                    WHERE user_id=%s AND server_id=%s'''
        params = user,server
        result = DatabaseConnection.fetch_one(query, params=params)
        if result is not None:
            return True
        return False
    
    @classmethod
    def update(cls, server):
        allowed_columns = {'server_name', 'description'}
        query_parts = []
        params = []
        for key, value in server.__dict__.items():
            if key in allowed_columns and value is not None:
                query_parts.append(f'{key} = %s')
                params.append(value)
        params.append(server.server_id)
        query = "UPDATE discord_chat.servers SET " + ", ".join(query_parts) + " WHERE server_id = %s"
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def delete(cls, server):
        query = '''DELETE FROM discord_chat.servers WHERE server_id=%s'''
        params = server.server_id,
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def get_all_by_name(cls, server):
        query = '''SELECT * FROM discord_chat.servers
                    WHERE LOWER(server_name)=%s'''
        params = server,
        results = DatabaseConnection.fetch_all(query, params=params)
        servers = []
        if results is not None:
            for result in results:
                servers.append(cls(
                        server_id = result[0],
                        server_name = result[1],
                        description = result[2],
                        icon_image = result[3]
                    ))
        return servers