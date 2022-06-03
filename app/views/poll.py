import sse
import uuid
import controllers.user as user
import controllers.poll as controller
from secure.auth import auth
from .message import Message
from mongoengine import ValidationError
from flask import Blueprint, render_template, request, session, Response, abort, redirect, url_for, make_response

poll = Blueprint('poll', __name__, template_folder='templates')


@poll.route("/view/<id>/")
@poll.route("/view/<id>")
def view(id):
    if not (pl := controller.get_poll(id=id)):
        abort(404)  # not found

    if (chart := request.args.get("chart", "")) not in ["bar", "doughnut", "pie"]:
        chart = "bar"

    return render_template(
        "poll.html",
        logged_in=auth.is_authenticated(session),
        poll=pl,
        chart=chart)


@poll.route("/")
@poll.route("/view/")
@poll.route("/view")
def view_all():
    polls = controller.get_polls(author=auth.get_user(session).id)
    return render_template("overview.html", polls=polls, poll_count=len(polls))


@poll.route("/vote/<id>/")
@poll.route("/vote/<id>", methods=["GET", "POST"])
def vote(id):
    if not (pl := controller.get_poll(id=id)):
        abort(404)  # not found

    if request.cookies.get(pl.id.hex):
        return redirect(url_for("poll.view", id=id))

    author = user.get_user(id=pl.author)

    if request.method == "POST":
        if auth.is_authenticated(session) and author:
            if author.id == auth.get_user(session).id:
                return render_template(
                    "vote.html",
                    logged_in=auth.is_authenticated(session),
                    poll=pl,
                    author=author.name if author else "Deleted User",
                    message=Message("error", "You must not vote on your own poll."))

        if len(request.form) != 1:
            return render_template(
                "vote.html",
                logged_in=auth.is_authenticated(session),
                poll=pl,
                author=author.name if author else "Deleted User",
                message=Message("warning", "No option was selected."))

        choice = list(request.form)[0]

        for option in pl.options:
            if uuid.UUID(choice) == option.id:
                option.votes += 1
                pl.save()
                sse.announcer.announce(msg=sse.format(data=pl.id.hex))
                response = make_response(redirect(url_for("poll.view", id=id)))
                response.set_cookie(pl.id.hex, "true")
                return response

        return render_template(
            "vote.html",
            logged_in=auth.is_authenticated(session),
            poll=pl,
            author=author.name if author else "Deleted User",
            message=Message("error", "Something went wrong selecting your option."))
    else:
        return render_template(
            "vote.html",
            logged_in=auth.is_authenticated(session),
            poll=pl,
            author=author.name if author else "Deleted User")


@poll.route("/create/")
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
                request.form.get("title"),
                request.form.get("desc"))

            if poll:
                return redirect(url_for("poll.view_all"))
            else:
                return render_template(
                    "signup.html",
                    message=Message("error", "Unknown error occurred while creating poll."))

        except ValidationError as e:
            return render_template("create.html", message=Message("warning", e))
    else:
        return render_template("create.html")


@poll.route("/delete/<id>/")
@poll.route("/delete/<id>")
def delete(id):
    if not (pl := controller.get_poll(id=id)):
        abort(404)  # not found

    if pl.author != auth.get_user(session).id:
        abort(401)  # unauthorised

    controller.delete_poll(pl.id)
    return redirect(url_for("poll.view_all"))


@poll.route("/listen/<id>", methods=["GET"])
def listen(id):

    def stream():
        messages = sse.announcer.listen()
        while True:
            msg = messages.get()
            if id in msg:
                yield sse.format("update")

    return Response(stream(), mimetype="text/event-stream")
