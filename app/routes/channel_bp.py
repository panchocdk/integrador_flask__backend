from flask import Blueprint
from ..controllers.channel_controller import ChannelController

channel_bp = Blueprint('channel_bp', __name__)

channel_bp.route('/<int:channel_id>', methods=['GET'])(ChannelController.get)
channel_bp.route('/all/<string:server_name>', methods=['GET'])(ChannelController.get_all)
channel_bp.route('/create', methods=['POST'])(ChannelController.create)
channel_bp.route('/<int:channel_id>', methods=['PUT'])(ChannelController.update)
channel_bp.route('/<int:channel_id>', methods=['DELETE'])(ChannelController.delete)