import controllers.user as controller
from .message import Message
from secure.auth import auth
from mongoengine import ValidationError
from flask import Blueprint, render_template, request, session, abort, url_for, redirect

user = Blueprint("user", __name__, template_folder='templates')


@user.route("/signup", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        try:
            new_user = controller.create_user(
                name := request.form.get("name", ""),
                password := request.form.get("password", ""),
                request.form.get("confirm", ""))

            if not new_user:
                return render_template(
                    "signup.html",
                    message=Message("error", "Unknown error occurred while creating user."))
            else:
                if token := auth.authenticate_user(name, password, True):
                    session["token"] = token
                    return render_template(
                        "index.html",
                        message=Message("success", "Your account has been created."))
                else:
                    abort(401)  # unauthorised
        except ValidationError as e:
            return render_template("signup.html", message=Message("warning", e))
    else:
        return render_template("signup.html")


@user.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        token = auth.authenticate_user(
            request.form.get("name", ""),
            request.form.get("password", ""),
            request.form.get("keep", False))

        if token:
            session["token"] = token
            return render_template("index.html")
        else:
            return render_template(
                "login.html",
                message=Message("error", "Invalid username or password."))
    else:
        return render_template("login.html")


@user.route("/logout")
def logout():
    auth.delete(session.get("token", ""))
    return redirect(url_for("user.login"))
