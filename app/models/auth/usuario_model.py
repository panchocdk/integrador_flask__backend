from ...database import DatabaseConnection
from models import rol_model, UsuarioRolModel
from models import status_model, UsuarioStatusModel
class Usuario:
    """Usuario model class"""

    def __init__(self, **kwargs):
        self.usuario_id = kwargs.get('usuario_id')
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
        self.nombre_completo = kwargs.get('nombre_completo')
        self.email = kwargs.get('email')
        self.imagen_de_perfil = kwargs.get('imagen_de_perfil')
        self.rol_id = kwargs.get('rol_id')
        self.status_id = kwargs.get('status_id')
  
    @classmethod
    def is_registered(cls, usuario):
        query = "SELECT usuario_id FROM chatnet.usuarios WHERE email = %s AND password = %s;"
        params = (usuario.email, usuario.password)
        result = DatabaseConnection.fetch_one(query, params=params)
        if result is not None:
            return True
        return False
    def serialize(self):
        """Serialize object representation """
        
        return {
            "usuario_id": self.usuario_id,
            "nombre_usuario": self.username,
            "clave": self.password,
            "nombre_completo": self.nombre_completo,
            "email": self.email,
            "imagen_de_perfil": self.imagen_de_perfil,
            "rol": UsuarioRolModel.get(UsuarioRolModel(rol_id =self.rol_id)).serialize(),
            "status": UsuarioStatusModel.get(UsuarioStatusModel(status_id= self.status_id)).serialize()

        }