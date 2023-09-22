from flask import Blueprint
from ..controllers.mensaje_controller import MensajeController

mensaje_bp = Blueprint('mensaje_bp', __name__)


mensaje_bp.route('/mensajes', methods=['POST'])(MensajeController.create_mensaje)
mensaje_bp.route('/mensajes/<int:mensaje_id>', methods=['GET'])(MensajeController.get_mensaje)
mensaje_bp.route('/mensajes/canal/<int:canal_id>', methods=['GET'])(MensajeController.get_mensaje)
mensaje_bp.route('/mensajes', methods=['GET'])(MensajeController.get_all)
mensaje_bp.route('/mensajes/<int:mensaje_id>', methods=['PUT'])(MensajeController.update_mensaje)
mensaje_bp.route('/mensajes/<int:mensaje_id>', methods=['DELETE'])(MensajeController.delete_mensaje)