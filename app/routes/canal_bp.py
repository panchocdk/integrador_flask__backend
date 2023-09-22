from flask import Blueprint
from ..controllers.canal_controller import CanalController

canal_bp = Blueprint('canal_bp', __name__)

canal_bp.route('/canales', methods=['POST'])(CanalController.create_canal)
canal_bp.route('/canales/<int:canal_id>', methods=['GET'])(CanalController.get_canal)
canal_bp.route('/canales/servidor/<int:servidor_id>', methods=['GET'])(CanalController.get_canales_by_servidor)
canal_bp.route('/canales', methods=['GET'])(CanalController.get_all_canales)
canal_bp.route('/canales/<int:canal_id>', methods=['PUT'])(CanalController.update_canal)
canal_bp.route('/canales/<int:canal_id>', methods=['DELETE'])(CanalController.delete_canal)
