from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from .extensions import db


class User(db.Model):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    tasks = relationship("Task", secondary="link", back_populates="users")

    def __init__(self, name):
        self.name = name


class Task(db.Model):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    users = relationship("User", secondary="link", back_populates="tasks")

    def __init__(self, name):
        self.name = name


class Link(db.Model):
    __tablename__ = "link"
    user_id = Column(
        Integer,
        ForeignKey("user.id"),
        primary_key=True
    )

    task_id = Column(
        Integer,
        ForeignKey('task.id'),
        primary_key=True
    )

    complete = Column(Boolean)

    def __init__(self, user_id, task_id, complete=False):
        self.user_id = user_id
        self.task_id = task_id
        self.complete = complete
