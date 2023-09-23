from ..database import DatabaseConnection

class User:

    def __init__(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.user_name = kwargs.get('user_name')
        self.email = kwargs.get('email')
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.password = kwargs.get('password')
        self.profile_image = kwargs.get('profile_image')
        self.date_of_birth = kwargs.get('date_of_birth')
        self.status_id = kwargs.get('status_id')
        self.role_id = kwargs.get('role_id')

    def serialize(self):
        return {
            'user_id': self.user_id,
            'user_name': self.user_name,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'password': self.password,
            'profile_image': self.profile_image,
            'date_of_birth': self.date_of_birth,
            'status_id': self.status_id,
            'role_id': self.role_id
        }
    
    @classmethod
    def is_registered(cls, user):
        query = '''SELECT user_id FROM discord_chat.users\
                    WHERE (email=%(email)s AND password=%(password)s)
                        OR (user_id=%(user_id)s)'''
        params = user.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)
        if result is not None:
            return True
        return False
    
    @classmethod
    def get(cls, user):
        query = '''SELECT * FROM discord_chat.users\
                    WHERE email=%(email)s'''
        params = user.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)
        if result is not None:
            return cls(
                user_id = result[0],
                user_name = result[1],
                email = result[2],
                first_name = result[3],
                last_name = result[4],
                password = result[5],
                profile_image = result[6],
                date_of_birth = result[7],
                status_id = result[8],
                role_id = result[9]
            )
        return None
    
    @classmethod
    def create(cls, user):
        query = '''INSERT INTO discord_chat.users (user_name, email, first_name, last_name,
                    password, date_of_birth, profile_image, status_id, role_id) VALUES (%(user_name)s,
                    %(email)s, %(first_name)s, %(last_name)s, %(password)s, %(date_of_birth)s,
                    %(profile_image)s, %(status_id)s, %(role_id)s)'''
        params = user.__dict__
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def update(cls, user):
        allowed_columns = {'user_name', 'email', 'first_name', 'last_name', 'password',
                           'profile_image', 'date_of_birth'}
        query_parts = []
        params = []
        for key, value in user.__dict__.items():
            if key in allowed_columns and value is not None:
                query_parts.append(f'{key} = %s')
                params.append(value)
        params.append(user.user_id)
        query = "UPDATE discord_chat.users SET " + ", ".join(query_parts) + " WHERE user_id = %s"
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def get_all(cls):
        query = '''SELECT * FROM discord_chat.users'''
        result = DatabaseConnection.fetch_all(query)
        users = []
        if result is not None:
            for res in result:
                users.append(cls(
                        user_id = res[0],
                        user_name = res[1],
                        email = res[2],
                        first_name = res[3],
                        last_name = res[4],
                        password = res[5],
                        profile_image = res[6],
                        date_of_birth = res[7],
                        status_id = res[8],
                        role_id = res[9]
                    ))
        return users
    
    @classmethod
    def delete(cls, user):
        query = '''DELETE FROM discord_chat.users WHERE user_id=%s'''
        params = user.user_id,
        DatabaseConnection.execute_query(query, params=params)