import uuid
import config
from .hash import hash_str
from database.models.user import User
from controllers import user
from flask_caching import Cache


class Auth(Cache):

    def authenticate_user(self, name, password, tmp):
        if usr := user.get_user(name=name):
            if hash_str(password) == usr.password:
                self.add(token := str(uuid.uuid4().hex), str(usr.id), timeout=18000 if tmp else 0)
                return token
            else:
                return False
        else:
            return False

    def is_authenticated(self, session):
        return isinstance(user.get_user(id=self.get(session.get("token", ""))), User)

    def get_user(self, session):
        return user.get_user(id=self.get(session["token"]))


auth = Auth(config=config.CACHE_CONFIG)
