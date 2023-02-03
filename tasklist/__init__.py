from flask import Flask

from .models import Admin
from .routes import mainBP, actionBP
from .extensions import db, csrf
import secrets
from flask_login import LoginManager
from werkzeug.security import generate_password_hash


def create_app():
    app = Flask(__name__, instance_relative_config=True, template_folder="ui/templates", static_folder="ui/static")
    app.config.from_object("config.Config")

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'main.home'
    db.init_app(app)
    csrf.init_app(app)
    app.config["SESSION_SQLALCHEMY"] = db
    app.config['SECRET_KEY'] = secrets.token_hex(16)

    app.register_blueprint(mainBP)
    app.register_blueprint(actionBP)

    with app.app_context():
        db.create_all()

    @login_manager.user_loader
    def load_user(user_id):
        return Admin.query.get(int(user_id))

    return app
