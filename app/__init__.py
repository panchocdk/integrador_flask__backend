from flask import Flask
from flask_cors import CORS
from config import Config
from .database import DatabaseConnection
from .routes.status_bp import status_bp
from .routes.role_bp import role_bp
from .routes.user_bp import user_bp
from .routes.server_bp import server_bp
from .routes.channel_bp import channel_bp
from .routes.chat_bp import chat_bp
from .routes.error_handlers import errors

def init_app():
    """Crea y configura la aplicación Flask"""
    
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    
    CORS(app, supports_credentials=True)

    app.config.from_object(
        Config
    )

    DatabaseConnection.set_config(app.config)

    app.register_blueprint(status_bp, url_prefix = '/status')
    app.register_blueprint(role_bp, url_prefix = '/role')
    app.register_blueprint(user_bp, url_prefix = '/user')
    app.register_blueprint(server_bp, url_prefix = '/server')
    app.register_blueprint(channel_bp, url_prefix = '/channel')
    app.register_blueprint(chat_bp, url_prefix = '/chat')
    app.register_blueprint(errors)

    return app