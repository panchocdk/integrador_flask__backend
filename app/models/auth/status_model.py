from ...database import DatabaseConnection

class UsuarioStatusModel:
    """UsuarioStatusModel model class"""

    def __init__(self, status_id=None, nombre_status=None):
        self.status_id = status_id
        self.nombre_status = nombre_status

    def serialize(self):
        """Serialize object representation """
        
        return {
            "status": self.status_id,
            "nombre_status": self.nombre_status
        }