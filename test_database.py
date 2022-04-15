import pytest
import uuid
import hashlib
import database as db
from faker import Faker

faker = Faker()

def test_m():
    new_user = db.models.User(name=faker.first_name(), password=hashlib.sha256(faker.password().encode()).digest())
    new_user.save()
    assert db.models.User.objects(id=new_user.id).count() == 1
