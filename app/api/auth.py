from werkzeug.security import check_password_hash

from app.models.user import where_one


class UserPayload:
    def __init__(self, user):
        self.id = user['id']


def verify(username, password):
    if not (username and password):
        return None
    user = where_one(username=username)
    if check_password_hash(user['password'], password):
        return UserPayload(user)


def identity(payload):
    user_id = payload['identity']
    return {'user_id': user_id}
