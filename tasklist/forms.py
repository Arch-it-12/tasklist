from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired


class AddUser(FlaskForm):
    user = StringField("User\'s Name", validators=[InputRequired()])


class AddTask(FlaskForm):
    task = StringField("Task Name", validators=[InputRequired()])

