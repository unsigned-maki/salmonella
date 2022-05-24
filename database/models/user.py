import uuid
from mongoengine import *


class User(Document):
    id = UUIDField(default=uuid.uuid4(), primary_key=True)
    name = StringField(unique=True, required=True)
    password = BinaryField(required=True)
