from flask import render_template, redirect, url_for

from .forms import AddUser, AddTask
from .models import User, Task, Link
from .extensions import db


def index():
    return redirect(url_for("main.home"))


def home():
    return render_template("home.html")


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
    return render_template("user_list.html", all_users = all_users)


def tasks(user):
    return render_template("tasks.html", user=user)
