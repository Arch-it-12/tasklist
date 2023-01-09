from flask import Flask

from .routes import mainBP, actionBP
from .extensions import db, csrf


def create_app():
    app = Flask(__name__, instance_relative_config=True, template_folder="ui/templates", static_folder="ui/static")
    app.config.from_object("config.Config")

    db.init_app(app)
    csrf.init_app(app)
    app.config["SESSION_SQLALCHEMY"] = db

    app.register_blueprint(mainBP)
    app.register_blueprint(actionBP)

    with app.app_context():
        db.create_all()

    return app
