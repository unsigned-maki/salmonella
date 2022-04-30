import database as db 

def create_poll(author, options, title, description):
    if get_poll(author=author):
        return False

    insert_options = []

    for option in options:
        insert_options.append(db.models.Option(text=option)) 

    try:
        new_poll = db.models.Poll(author=author, options=insert_options, title=title, description=description)
        new_poll.save() 
    except ValidationError:
        return False

    return new_poll.id

def get_poll(**kwargs):
    polls = db.models.Poll.objects(**kwargs)

    if not polls.count():
        return False

    return polls[0]

def delete_poll(id):
    polls = polls.models.Poll.objects(id=id)

    if not polls.count():
        return False

    polls[0].delete()
    return True
