import os
import jwt
from .hash import hash_str
from database.models.user import User
from controllers import user

JWT_SECRET = os.getenv("JWT_SECRET")

class Auth:

    def authenticate_user(self, name, password, tmp):
        if usr := user.get_user(name=name):
            if hash_str(password) == usr.password:
                return jwt.encode({"user": str(usr.id)}, JWT_SECRET, algorithm="HS256")
            else:
                return False
        else:
            return False

    def is_authenticated(self, session):
        try:
            decoded = jwt.decode(session.get("token", ""), JWT_SECRET, algorithms="HS256")
            return isinstance(user.get_user(id=decoded["user"]), User)
        except:
            False

    def get_user(self, session):
        return user.get_user(id=jwt.decode(session.get("token", ""), JWT_SECRET, algorithms="HS256")["user"])


auth = Auth()
