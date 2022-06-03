import uuid
import pytest
from faker import Faker
from controllers import user
from mongoengine import ValidationError

fake = Faker()


def test_create_user_a():
    assert user.create_user(fake.name(), pw := fake.password(), pw)


def test_create_user_b():
    name = fake.name()
    user.create_user(name, pw := fake.password(), pw)
    with pytest.raises(ValidationError, match=f"User {name} already exists."):
        user.create_user(name, pw := fake.password(), pw)


def test_get_user_a():
    new_user = user.create_user(fake.name(), pw := fake.password(), pw)
    assert user.get_user(id=new_user)


def test_get_user_b():
    assert not user.get_user(id=uuid.uuid4())


def test_get_user_c():
    name = fake.name()
    new_user = user.create_user(name, pw := fake.password(), pw)
    assert user.get_user(name=name)


def test_get_user_d():
    assert not user.get_user(name=fake.name())


def test_get_user_e():
    new_user = user.create_user(fake.name(), pw := fake.password(), pw)
    assert user.get_user(id=new_user)


def test_get_user_f():
    new_user = user.create_user(fake.name(), pw := fake.password(), pw)
    assert user.get_user(id=str(new_user))


def test_delete_user_a():
    new_user = user.create_user(fake.name(), pw := fake.password(), pw)
    assert user.delete_user(new_user)


def test_delete_user_b():
    assert not user.delete_user(uuid.uuid4())


def test_update_user_password_a():
    new_user = user.create_user(fake.name(), pw := fake.password(), pw)
    password = user.get_user(id=new_user).password
    user.update_user_password(new_user, fake.password())
    assert user.get_user(id=new_user).password != password
