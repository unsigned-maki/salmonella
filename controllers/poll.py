import uuid
import database as db
from mongoengine import ValidationError


def create_poll(author, options, title, description):
    if not isinstance(author, uuid.UUID) and isinstance(author, str):
        author = uuid.UUID(f"{author}")

    insert_options = []

    for option in options:
        if not bool(option.strip()):
            raise ValidationError("Option must not be empty.")

        insert_options.append(db.models.Option(id=uuid.uuid4(), text=option))

    try:
        new_poll = db.models.Poll(
            id=uuid.uuid4(),
            author=author,
            options=insert_options,
            title=title,
            description=description)
        new_poll.save()
    except ValidationError as e:
        raise e

    if not new_poll:
        return False

    return new_poll.id


def get_poll(**kwargs):
    if kwargs.get("id"):
        if not isinstance(kwargs["id"], uuid.UUID) and isinstance(kwargs["id"], str):
            kwargs["id"] = uuid.UUID(f"{kwargs['id']}")

    polls = db.models.Poll.objects(**kwargs)

    if not polls.count():
        return False

    return polls[0]


def get_polls(**kwargs):
    if kwargs.get("id"):
        if not isinstance(kwargs["id"], uuid.UUID) and isinstance(kwargs["id"], str):
            kwargs["id"] = uuid.UUID(f"{kwargs['id']}")

    polls = db.models.Poll.objects(**kwargs)

    return polls


def delete_poll(id):
    polls = db.models.Poll.objects(id=id)

    if not polls.count():
        return False

    polls[0].delete()
    return True
