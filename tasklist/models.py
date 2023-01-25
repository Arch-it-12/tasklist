from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from .extensions import db

from flask_login import UserMixin


class Admin(db.Model, UserMixin):
    __tablename__ = 'Admin'
    admin = Column(String, unique=True, primary_key=True)
    password = Column(String)


class User(db.Model):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    order = Column(Integer)
    tasks = relationship("Link", back_populates="user")

    def __init__(self, name):
        self.name = name
        self.order = len(db.session.query(User).all()) + 1


class Task(db.Model):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    order = Column(Integer)
    users = relationship("Link", back_populates="task")

    def __init__(self, name):
        self.name = name
        self.order = len(db.session.query(Task).all()) + 1


class Link(db.Model):
    __tablename__ = "link"
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    task_id = Column(Integer, ForeignKey('task.id'), primary_key=True)

    user = relationship("User", back_populates="tasks")
    task = relationship("Task", back_populates="users")

    complete = Column(Boolean, default=False)

    def __init__(self, user_id, task_id, complete=False):
        self.user_id = user_id
        self.task_id = task_id
        self.complete = complete
