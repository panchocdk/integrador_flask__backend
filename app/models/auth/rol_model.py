from ...database import DatabaseConnection

class UsuarioRolModel:
    """UsuarioRolModel model class"""

    def __init__(self, **kwargs):
        self.rol_id = kwargs.get('rol_id')
        self.nombre_rol = kwargs.get('nombre_rol')

    def serialize(self):
        """Serialize object representation """
        
        return {
            "rol": self.rol_id,
            "nombre_rol": self.nombre_rol
        }
    @classmethod
    def get(cls, role):
        query = """SELECT rol_id, nombre_rol FROM chatnet.usuario_rol WHERE rol_id = %(rol_id)s"""
        params = role.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return UsuarioRolModel(
                rol_id = result[0],
                nombre_rol = result[1]
            )
        return None