from flask import render_template, redirect, url_for


def admin_home():
    return render_template("admin/admin_home.html")
