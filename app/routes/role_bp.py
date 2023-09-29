from flask import Blueprint
from ..controllers.role_controller import RoleController

role_bp = Blueprint('role_bp', __name__)

role_bp.route('/<int:role_id>', methods=['GET'])(RoleController.get)
role_bp.route('/', methods=['GET'])(RoleController.get_all)
role_bp.route('/create', methods=['POST'])(RoleController.create)
role_bp.route('/<int:role_id>', methods=['PUT'])(RoleController.update)
role_bp.route('/<int:role_id>', methods=['DELETE'])(RoleController.delete)