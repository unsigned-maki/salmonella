import os
from flask import Flask
from views.poll import poll
from views.user import user
from secure.auth import auth


app = Flask(__name__)

app.secret_key = os.urandom(16)

auth.init_app(app)

app.register_blueprint(poll, url_prefix="/poll")
app.register_blueprint(user, url_prefix="/user")

if __name__ == "__main__":
    app.run()
