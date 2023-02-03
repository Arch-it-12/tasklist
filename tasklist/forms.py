from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import InputRequired
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    password = PasswordField('Password:', validators=[InputRequired()])


class AddUser(FlaskForm):
    user = StringField("User\'s Name", validators=[InputRequired()])


class AddTask(FlaskForm):
    task = StringField("Task Name", validators=[InputRequired()])
