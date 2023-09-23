from flask import Blueprint
from ..controllers.chat_controller import ChatController

chat_bp = Blueprint('chat_bp', __name__)

chat_bp.route('/<int:chat_id>', methods=['GET'])(ChatController.get)
chat_bp.route('/all/<int:channel_id>', methods=['GET'])(ChatController.get_all)
chat_bp.route('/create', methods=['POST'])(ChatController.create)
chat_bp.route('/<int:chat_id>', methods=['PUT'])(ChatController.update)
chat_bp.route('/<int:chat_id>', methods=['DELETE'])(ChatController.delete)