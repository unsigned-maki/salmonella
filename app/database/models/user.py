import uuid
from mongoengine import *


class User(Document):
    id = UUIDField(required=True, primary_key=True)
    name = StringField(unique=True, required=True)
    password = BinaryField(required=True)
