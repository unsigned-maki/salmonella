import uuid
from .user import User
from mongoengine import *

def valid_author(author):
    if not User.objects(id=author).count():
        raise ValidationError("Author is not a valid user")

class Poll(Document):
    id = UUIDField(default=uuid.uuid4(), primary_key=True)
    title = StringField(required=True)
    author = UUIDField(required=True, validation=valid_author)
    