from ...database import DatabaseConnection

class Servidor:
    """Servidor model class"""

    def __init__(self, **kwargs):
        self.servidor_id = kwargs.get('servidor_id')
        self.nombre_servidor = kwargs.get('nombre_servidor')
        self.descripcion = kwargs.get('descripcion')
        self.imagen_servidor = kwargs.get('imagen_servidor')
        self.creador_id = kwargs.get('creador_id')

    @classmethod
    def create(cls, servidor):
        query = """
            INSERT INTO chatnet.servidores (nombre_servidor, descripcion, imagen_servidor, creador_id)
            VALUES (%(nombre_servidor)s, %(descripcion)s, %(imagen_servidor)s, %(creador_id)s);
        """
        params = servidor.__dict__
        DatabaseConnection.execute(query, params=params)

    @classmethod
    def get(cls, servidor_id):
        query = "SELECT * FROM chatnet.servidores WHERE servidor_id = %(servidor_id)s;"
        params = {'servidor_id': servidor_id}
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(
                servidor_id=result[0],
                nombre_servidor=result[1],
                descripcion=result[2],
                imagen_servidor=result[3],
                creador_id=result[4]
            )
        return None
    @classmethod
    def get_all(cls):
        
        query = """SELECT * FROM chatnet.servidores"""
        results = DatabaseConnection.fetch_all(query)

        servidores = []
        if results is not None:
            for result in results:
                servidores.append(cls(*result))
        return servidores
    
    def serialize(self):
        """Serialize object representation"""
        return {
            "servidor_id": self.servidor_id,
            "nombre_servidor": self.nombre_servidor,
            "descripcion": self.descripcion,
            "imagen_servidor": self.imagen_servidor,
            "creador_id": self.creador_id
        }
    @classmethod
    def update(cls, servidor):
        allowed_columns = {'nombre_servidor', 'descripcion', 'imagen_servidor',
                           'creador_id'}
        query_parts = []
        params = []
        for key, value in servidor.__dict__.items():
            if key in allowed_columns and value is not None:
                query_parts.append(f"{key} = %s")
                params.append(value)
        params.append(servidor.servidor_id)

        query = "UPDATE chatnet.servidores SET " + ", ".join(query_parts) + " WHERE servidor_id = %s"
        DatabaseConnection.execute_query(query, params=params)
    
    @classmethod
    def delete(cls, servidor):
        query = "DELETE FROM chatnet.servidoes WHERE servidor_id = %s"
        params = servidor.servidor_id,
        DatabaseConnection.execute_query(query, params=params)