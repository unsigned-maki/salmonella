import os
import config
from views.poll import poll
from views.user import user
from secure.auth import auth
from flask import Flask, request, session, render_template, redirect, url_for


app = Flask(__name__, static_url_path="/static")

app.secret_key = JWT_SECRET = os.getenv("SESSION_SECRET")

app.register_blueprint(poll, url_prefix="/poll")
app.register_blueprint(user, url_prefix="/user")


@app.before_request
def require_auth():
    if request.endpoint in config.REQUIRE_AUTHENTICATION:
        if not auth.is_authenticated(session):
            return redirect(url_for("user.login"))


@app.before_request
def no_auth():
    if request.endpoint in config.NO_AUTHENTICATION:
        if auth.is_authenticated(session):
            return redirect(url_for("poll.view_all"))


@app.route("/")
def index():
    return redirect(url_for("poll.view_all"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
