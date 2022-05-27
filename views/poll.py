import controllers.poll as controller
from secure.auth import auth
from jinja2 import TemplateNotFound
from flask import Blueprint, render_template, abort

poll = Blueprint('poll', __name__, template_folder='templates')


@poll.route("/view")
def view_all():
    try:
        return render_template("poll.html")
    except TemplateNotFound:
        abort(404)


@poll.route("/view/<id>", methods=["GET"])
def view_one(id):
    controller.get_poll(id)
    try:
        return render_template("poll.html")
    except TemplateNotFound:
        abort(404)


@poll.route("/create", methods=["GET", "POST"])
def create():
    try:
        return render_template("create.html")
    except TemplateNotFound:
        abort(404)
