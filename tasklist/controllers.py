from flask import render_template, redirect, url_for


def index():
    return redirect(url_for("main.home"))


def home():
    return render_template("home.html")