from flask import Blueprint
from ..controllers.status_controller import StatusController

status_bp = Blueprint('status_bp', __name__)

status_bp.route('/<int:status_id>', methods=['GET'])(StatusController.get)
status_bp.route('/', methods=['GET'])(StatusController.get_all)
status_bp.route('/create', methods=['POST'])(StatusController.create)
status_bp.route('/<int:status_id>', methods=['PUT'])(StatusController.update)
status_bp.route('/<int:status_id>', methods=['DELETE'])(StatusController.delete)