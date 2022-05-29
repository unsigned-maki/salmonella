import os
import config
from views.poll import poll
from views.user import user
from secure.auth import auth
from flask import Flask, request, session, render_template, redirect, url_for


app = Flask(__name__, static_url_path="/static")

app.secret_key = os.urandom(16)

auth.init_app(app)

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
            return render_template("index.html")


@app.route("/")
def index():
    return redirect(url_for("poll.view_all"))


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
