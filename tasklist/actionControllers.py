import json

import sqlalchemy.exc
from flask import render_template, redirect, url_for, request

from .forms import AddUser, AddTask
from .models import User, Task, Link
from .extensions import db


def remove_user(user_id):
    user = db.session.query(User).filter_by(id=user_id).first()
    users = db.session.query(Link).filter_by(user_id=user_id).all()
    db.session.delete(user)
    for i in users:
        db.session.delete(i)
    db.session.commit()

    return redirect(url_for("main.admin"))


def remove_task(task_id):
    task = db.session.query(Task).filter_by(id=task_id).first()
    tasks = db.session.query(Link).filter_by(task_id=task_id).all()
    db.session.delete(task)
    for i in tasks:
        db.session.delete(i)
    db.session.commit()

    return redirect(url_for("main.admin"))


def assign_task(user_id, task_id):
    link = Link(user_id, task_id)
    db.session.add(link)

    try:
        db.session.commit()
    except sqlalchemy.exc.IntegrityError:
        return redirect(url_for("main.admin"))

    return redirect(url_for("main.admin"))


def mark_task(user_id, task_id):
    link = db.session.query(Link).filter_by(user_id=user_id, task_id=task_id).first()
    link.complete = not link.complete
    db.session.commit()

    return redirect(url_for("main.tasks", user_id=user_id))


def unassign_task(user_id, task_id):
    link = db.session.query(Link).filter_by(user_id=user_id, task_id=task_id).first()
    db.session.delete(link)
    db.session.commit()

    return redirect(url_for("main.admin"))


def reorder():
    ids = json.loads(request.json['id_list'])
    ids = [int(i) for i in ids]
    ids = dict(zip(ids, range(1, len(ids) + 1)))

    group = json.loads(request.json['group'])

    if group == "user-table":
        all_users = db.session.query(User).order_by(User.id).all()
        for user in all_users:
            print(ids.get(user.id))
            user.order = ids.get(user.id)
    else:
        all_tasks = db.session.query(Task).order_by(Task.id).all()
        for task in all_tasks:
            task.order = ids.get(task.id)

    db.session.commit()

    return redirect(url_for("main.admin"))
