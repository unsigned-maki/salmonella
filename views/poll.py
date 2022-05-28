import controllers.poll as controller
from secure.auth import auth
from .message import Message
from jinja2 import TemplateNotFound
from mongoengine import ValidationError
from flask import Blueprint, render_template, abort, request, session

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
    if request.method == "POST":
        options = []

        for field in request.form:
            if "option" in field:
                options.append(request.form[field])

        try:
            poll = controller.create_poll(
                auth.get_user(session).id,
                options,
                title := request.form.get("title"),
                request.form.get("desc"))

            if poll:
                return render_template(
                    "create.html",
                    message=Message("success", f"Successfully created poll {title}."))
            else:
                return render_template(
                    "signup.html",
                    message=Message("error", "Unknown error occurred while creating poll."))

        except ValidationError as e:
            return render_template("create.html", message=Message("warning", e))
    else:
        return render_template("create.html")
