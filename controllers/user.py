import uuid
import hashlib
import database as db
from mongoengine import ValidationError


def create_user(name, password):
    if get_user(name=name):
        return False

    try:
        new_user = db.models.User(name=name, password=hashlib.sha256(password.encode()).digest())
        new_user.save()
    except ValidationError:
        return False

    return new_user.id


def get_user(**kwargs):
    if kwargs.get("id"):
        if not isinstance(kwargs["id"], uuid.UUID) and isinstance(kwargs["id"], str):
            kwargs["id"] = uuid.UUID(f"{kwargs['id']}")

    users = db.models.User.objects(**kwargs)

    if not users.count():
        return False

    return users[0]


def delete_user(id):
    users = db.models.User.objects(id=id)

    if not users.count():
        return False

    users[0].delete()
    return True


def update_user_password(id, new_password):
    users = db.models.User.objects(id=id)

    if not users.count():
        return False

    users[0].update(password=hashlib.sha256(new_password.encode()).digest())
    return True
