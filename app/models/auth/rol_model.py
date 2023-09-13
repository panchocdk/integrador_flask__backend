from ...database import DatabaseConnection

class UsuarioRolModel:
    """UsuarioRolModel model class"""

    def __init__(self, rol_id=None, nombre_rol=None):
        self.rol_id = rol_id
        self.nombre_rol = nombre_rol

    def serialize(self):
        """Serialize object representation """
        
        return {
            "rol": self.rol_id,
            "nombre_rol": self.nombre_rol
        }
      