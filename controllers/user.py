import hashlib
import database as db

def create_user(name, password):
    new_user = db.models.User(name=name, password=hashlib.sha256(password.encode()).digest())
    
    try:
        new_user.save()
    except ValidationError:
        return False

    return new_user.id
    
def get_user(**kwargs):
    user = db.models.User.objects(**kwargs)

    if not user.count():
        return False

    return user[0].to_json()
    