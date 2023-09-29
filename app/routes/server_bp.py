from flask import Blueprint
from ..controllers.server_controller import ServerController

server_bp = Blueprint('server_bp', __name__)

server_bp.route('/create', methods=['POST'])(ServerController.create)
server_bp.route('/', methods=['GET'])(ServerController.show_servers)
server_bp.route('/<int:server_id>', methods=['GET'])(ServerController.get)
server_bp.route('/<int:server_id>', methods=['PUT'])(ServerController.update)
server_bp.route('/<int:server_id>', methods=['DELETE'])(ServerController.delete)
server_bp.route('/uxs', methods=['POST'])(ServerController.add_user_server)
server_bp.route('/uxs', methods=['GET'])(ServerController.get_uxs)
server_bp.route('/<string:server_name>', methods=['GET'])(ServerController.get_all_by_name)