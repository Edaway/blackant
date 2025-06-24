from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_socketio import SocketIO

db = SQLAlchemy()
login_manager = LoginManager()
socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config.from_object('server.config.Config')

    db.init_app(app)
    login_manager.init_app(app)
    socketio.init_app(app)

    # Здесь импорт и регистрация блюпринтов
    from .auth.routes import auth_bp
    from .vacancies.routes import vacancies_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(vacancies_bp)

    return app
