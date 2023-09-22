from flask import Blueprint
from ..controllers.servidor_controller import ServidorController

servidor_bp = Blueprint('servidor_bp', __name__)

servidor_bp.route('/servidores', methods=['POST'])(ServidorController.create_servidor)
servidor_bp.route('/servidores/<int:servidor_id>', methods=['GET'])(ServidorController.get_servidor)
servidor_bp.route('/servidores', methods=['GET'])(ServidorController.get_all)
servidor_bp.route('/servidores/<int:servidor_id>', methods=['PUT'])(ServidorController.update_servidor)
servidor_bp.route('/servidores/<int:servidor_id>', methods=['DELETE'])(ServidorController.delete_servidor)