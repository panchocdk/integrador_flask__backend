from flask import Blueprint
from ..controllers.user_controller import UserController

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/create', methods=['POST'])(UserController.create)
user_bp.route('/login', methods=['POST'])(UserController.login)
user_bp.route('/profile', methods=['GET'])(UserController.show_profile)
user_bp.route('/', methods=['GET'])(UserController.get_all)
user_bp.route('/<int:user_id>', methods=['PUT'])(UserController.update)
user_bp.route('/<int:user_id>', methods=['DELETE'])(UserController.delete)
user_bp.route('/logout', methods=['GET'])(UserController.logout)