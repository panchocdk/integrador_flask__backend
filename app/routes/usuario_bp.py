from flask import Blueprint
from ..controllers.usuario_controller import UserController
usuario_bp = Blueprint('usuario_bp', __name__)
usuario_bp.route('/login', methods=['POST'])(UserController.login)
usuario_bp.route('/profile', methods=['GET'])(UserController.show_profile)
usuario_bp.route('/logout', methods=['GET'])(UserController.logout)