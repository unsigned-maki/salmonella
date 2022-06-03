import uuid
from .user import User
from mongoengine import *
from .option import Option
from mongoengine import ValidationError


def valid_author(author):
    if not User.objects(id=author).count():
        raise ValidationError("Author is not a valid user.")


def valid_options(options):
    if len(options) < 2:
        raise ValidationError("Minimum of 2 options required.")


class Poll(Document):
    id = UUIDField(required=True, primary_key=True)
    title = StringField(required=True)
    description = StringField(required=True)
    author = UUIDField(required=True, validation=valid_author)
    options = EmbeddedDocumentListField(Option, required=True, validation=valid_options)
