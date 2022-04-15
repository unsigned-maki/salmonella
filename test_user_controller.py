import uuid
from faker import Faker
from controllers import user

fake = Faker()

def test_create_user_a():
    assert user.create_user(fake.name(), fake.password())

def test_create_user_b():
    name = fake.name()
    user.create_user(name, fake.password())
    assert not user.create_user(name, fake.password())

def test_get_user_a():
    new_user = user.create_user(fake.name(), fake.password())
    assert user.get_user(id=new_user)

def test_get_user_b():
    assert not user.get_user(id=uuid.uuid4())

def test_get_user_c():
    name = fake.name()
    new_user = user.create_user(name, fake.password())
    assert user.get_user(name=name)

def test_get_user_d():
    assert not user.get_user(name=fake.name())

def test_delete_user_a():
    new_user = user.create_user(fake.name(), fake.password())
    assert user.delete_user(new_user)

def test_delete_user_b():
    assert not user.delete_user(uuid.uuid4())
