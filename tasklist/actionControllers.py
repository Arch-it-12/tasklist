from flask import render_template, redirect, url_for

from .forms import AddUser, AddTask
from .models import User, Task, Link
from .extensions import db


def remove_user(user_id):
    user = db.session.query(User).filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()

    return redirect(url_for("main.admin"))


def remove_task(task_id):
    task = db.session.query(Task).filter_by(id=task_id).first()
    db.session.delete(task)
    db.session.commit()

    return redirect(url_for("main.admin"))


def assign_task(user_id, task_id):
    link = Link(user_id, task_id)
    db.session.add(link)
    db.session.commit()

    return redirect(url_for("main.admin"))
