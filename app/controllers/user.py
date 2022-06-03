import uuid
import database as db
from secure.hash import hash_str
from mongoengine import ValidationError


def create_user(name, password, confirm):
    if get_user(name=name):
        raise ValidationError(f"User {name} already exists.")

    if len(name) < 3 or len(name) > 12:
        raise ValidationError("Name must be between 3 and 12 characters long.")

    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters long.")

    if " " in password:
        raise ValidationError("Password must not contain spaces.")

    if any(i in name for i in [" ", "'", "+", ",", "<", ">", ".", "/", "\\", "\""]):
        raise ValidationError("Name contains invalid symbols.")

    if password != confirm:
        raise ValidationError("Passwords do not match.")

    try:
        new_user = db.models.User(
            id=uuid.uuid4(),
            name=name,
            password=hash_str(password))
        new_user.save()
    except ValidationError as e:
        raise e

    if not new_user:
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


def update_user_password(id, new, confirm):
    if len(new) < 8:
        raise ValidationError("Password must be at least 8 characters long.")

    if " " in new:
        raise ValidationError("Invalid username or password.")

    if new != confirm:
        raise ValidationError("Passwords do not match.")

    users = db.models.User.objects(id=id)

    if not users.count():
        return False

    users[0].update(password=hash_str(new))
    return True
