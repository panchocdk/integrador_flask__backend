from ..database import DatabaseConnection

class Status:

    def __init__(self, **kwargs):
        self.status_id = kwargs.get('status_id')
        self.status_name = kwargs.get('status_name')

    def serialize(self):
        return {
            'status_id': self.status_id,
            'status_name': self.status_name,
        }
    
    @classmethod
    def is_registered(cls, status):
        query = '''SELECT status_id FROM discord_chat.user_status\
                    WHERE status_name=%(status_name)s OR status_id=%(status_id)s'''
        params = status.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)
        if result is not None:
            return True
        return False
    
    @classmethod
    def get(cls, status):
        query = '''SELECT * FROM discord_chat.user_status\
                    WHERE status_id=%(status_id)s'''
        params = status.__dict__
        results = DatabaseConnection.fetch_one(query, params=params)
        if results is not None:
            return cls(
                status_id = results[0],
                status_name = results[1]
            )
        return None
    
    @classmethod
    def get_all(cls):
        query = '''SELECT * FROM discord_chat.user_status'''
        results = DatabaseConnection.fetch_all(query)
        statuss = []
        if results is not None:
            for result in results:
                statuss.append(cls(
                        status_id = result[0],
                        status_name = result[1]
                    ))
        return statuss
    
    @classmethod
    def create(cls, status):
        query = '''INSERT INTO discord_chat.user_status (status_name)
                    VALUES (%(status_name)s)'''
        params = status.__dict__
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def update(cls, status):
        allowed_columns = {'status_name'}
        query_parts = []
        params = []
        for key, value in status.__dict__.items():
            if key in allowed_columns and value is not None:
                query_parts.append(f'{key} = %s')
                params.append(value)
        params.append(status.status_id)
        query = "UPDATE discord_chat.user_status SET " + ", ".join(query_parts) + " WHERE status_id = %s"
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def delete(cls, status):
        query = '''DELETE FROM discord_chat.user_status WHERE status_id=%s'''
        params = status.status_id,
        DatabaseConnection.execute_query(query, params=params)