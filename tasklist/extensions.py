from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
import sqlite3

db = SQLAlchemy()
csrf = CSRFProtect()
