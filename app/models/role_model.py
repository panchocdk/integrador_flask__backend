from ..database import DatabaseConnection

class Role:

    def __init__(self, **kwargs):
        self.role_id = kwargs.get('role_id')
        self.role_name = kwargs.get('role_name')

    def serialize(self):
        return {
            'role_id': self.role_id,
            'role_name': self.role_name,
        }
    
    @classmethod
    def is_registered(cls, role):
        query = '''SELECT role_id FROM discord_chat.user_roles\
                    WHERE role_name=%(role_name)s OR role_id=%(role_id)s'''
        params = role.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)
        if result is not None:
            return True
        return False
    
    @classmethod
    def get(cls, role):
        query = '''SELECT * FROM discord_chat.user_roles\
                    WHERE role_id=%(role_id)s'''
        params = role.__dict__
        results = DatabaseConnection.fetch_one(query, params=params)
        if results is not None:
            return cls(
                role_id = results[0],
                role_name = results[1]
            )
        return None
    
    @classmethod
    def get_all(cls):
        query = '''SELECT * FROM discord_chat.user_roles'''
        results = DatabaseConnection.fetch_all(query)
        roles = []
        if results is not None:
            for result in results:
                roles.append(cls(
                        role_id = result[0],
                        role_name = result[1]
                    ))
        return roles
    
    @classmethod
    def create(cls, role):
        query = '''INSERT INTO discord_chat.user_roles (role_name)
                    VALUES (%(role_name)s)'''
        params = role.__dict__
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def update(cls, role):
        allowed_columns = {'role_name'}
        query_parts = []
        params = []
        for key, value in role.__dict__.items():
            if key in allowed_columns and value is not None:
                query_parts.append(f'{key} = %s')
                params.append(value)
        params.append(role.role_id)
        query = "UPDATE discord_chat.user_roles SET " + ", ".join(query_parts) + " WHERE role_id = %s"
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def delete(cls, role):
        query = '''DELETE FROM discord_chat.user_roles WHERE role_id=%s'''
        params = role.role_id,
        DatabaseConnection.execute_query(query, params=params)