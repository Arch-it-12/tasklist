from flask import render_template, redirect, url_for, flash, request

from .forms import AddUser, AddTask, LoginForm
from .models import User, Task, Link, Admin
from .extensions import db
from flask_login import login_user

from werkzeug.security import check_password_hash, generate_password_hash

def index():
    return redirect(url_for("main.home"))

def home():
    login_form = LoginForm(request.form)

    if request.method == 'POST' and login_form.validate_on_submit():
        # read form data
        password = request.form.get('password')
        # project's password given its name.
        # Verify password.
        if check_password_hash(generate_password_hash(password), "password123"):
            # Success.
            return redirect(url_for('main.admin'))
        else:
            # Something (user or pass) is not ok
            flash("Incorrect password, try again.", category="danger")
    return render_template('home.html', msg='Wrong password.', form=login_form)

def admin_panel():
    user_form = AddUser()
    task_form = AddTask()

    if user_form.validate_on_submit():
        user = User(user_form.user.data)
        db.session.add(user)

    if task_form.validate_on_submit():
        print(task_form.task.data)
        task = Task(task_form.task.data)
        db.session.add(task)

    db.session.commit()

    all_users = db.session.query(User).all()
    all_tasks = db.session.query(Task).all()
    print(all_tasks)
    all_links = db.session.query(Link).all()

    return render_template("admin_panel.html", userForm=user_form, taskForm=task_form, all_users=all_users,
                           all_tasks=all_tasks, all_links=all_links)


def user_list():
    all_users = db.session.query(User).all()
    return render_template("user_list.html", all_users=all_users)


def tasks(user_id):
    da_user = db.session.query(User).filter_by(id=user_id).first()
    return render_template("tasks.html", user=da_user, user_id=user_id)
