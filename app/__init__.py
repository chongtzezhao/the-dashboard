from flask import Flask, render_template

from .keep_alive.routes import keep_alive_bp
from .telebot.routes import telebot_bp
from .telebot.api import telebot_api_bp
from .telebot.events import socketio


def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'

    # from .main import main as main_blueprint
    # app.register_blueprint(main_blueprint)
    
    # Register blueprints
    # app.register_blueprint(keep_alive_bp)
    app.register_blueprint(telebot_bp)
    app.register_blueprint(telebot_api_bp)
        
    # index
    @app.route("/")
    def index():
        return render_template("index.html")

    socketio.init_app(app)
    return app

