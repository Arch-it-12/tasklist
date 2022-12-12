from flask import Flask

from .routes import mainBP, adminBP


def create_app():
    app = Flask(__name__, instance_relative_config=True, template_folder="ui/templates", static_folder="ui/static")
    app.config.from_object("config.Config")

    app.register_blueprint(mainBP)
    app.register_blueprint(adminBP)

    return app
