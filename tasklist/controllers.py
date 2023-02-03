from flask import render_template, redirect, url_for, flash, request

from .forms import AddUser, AddTask, LoginForm
from .models import User, Task, Link, Admin
from .extensions import db
from flask_login import login_user, login_required, LoginManager

from werkzeug.security import check_password_hash, generate_password_hash


def index():
    return redirect(url_for("main.home"))


def home():
    login_form = LoginForm(request.form)

    if request.method == 'POST' and login_form.validate_on_submit():
        password = request.form.get('password')
        admin = Admin.query.filter_by(username="admin").first()

        if admin and check_password_hash(admin.password, password):
            login_user(admin)
            flash("Login successful!", category="success")
            return redirect(url_for('main.admin'))
        else:
            flash("Incorrect password, try again.", category="danger")
    return render_template('home.html', msg='Wrong password.', form=login_form)


@login_required
def admin_panel():
    group = request.args.get("group")
    tab = request.args.get("tab")

    user_form = AddUser()
    task_form = AddTask()

    if user_form.validate_on_submit():
        user = User(user_form.user.data)
        db.session.add(user)

    if task_form.validate_on_submit():
        task = Task(task_form.task.data)
        db.session.add(task)

    db.session.commit()

    all_users = db.session.query(User).order_by(User.order).all()
    all_tasks = db.session.query(Task).order_by(Task.order).all()
    all_links = db.session.query(Link).order_by(Link.order).all()

    return render_template("admin_panel.html", userForm=user_form, taskForm=task_form, all_users=all_users,
                           all_tasks=all_tasks, all_links=all_links, group=group, tab=tab)


def user_list():
    all_users = db.session.query(User).order_by(User.order).all()
    return render_template("user_list.html", all_users=all_users)


def tasks(user_id):
    da_user = db.session.query(User).filter_by(id=user_id).first()
    da_users_tasks = db.session.query(Link).filter_by(user_id=user_id).order_by(Link.order).all()
    return render_template("tasks.html", user=da_user, user_id=user_id, tasks=da_users_tasks)
