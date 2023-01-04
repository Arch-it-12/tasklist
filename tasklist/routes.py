from flask import Blueprint

from . import controllers, admin_controllers

mainBP = Blueprint("main", __name__)
adminBP = Blueprint("admin", __name__, url_prefix="/admin")

mainBP.add_url_rule("/", "index", controllers.index)
mainBP.add_url_rule("/home", "home", controllers.home)
mainBP.add_url_rule("/admin", "admin", controllers.admin_panel)
