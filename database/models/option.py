import uuid
from mongoengine import *
from mongoengine import ValidationError


def valid_votes(votes):
    if votes < 0:
        raise ValidationError("Votes cannot be less than 0")


class Option(EmbeddedDocument):
    id = UUIDField(default=uuid.uuid4(), primary_key=True)
    text = StringField(required=True)
    votes = IntField(default=0, validation=valid_votes)
