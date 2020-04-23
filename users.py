from werkzeug.security import safe_str_cmp


class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password


in_memory_users = [
    User(1, 'jseinfeld', 'eff you money'),
    User(2, 'jalexander', 'sine'),
]


def authenticate(username, password):
    for user in in_memory_users:
        if safe_str_cmp(user.username, username) and safe_str_cmp(user.password, password):
            return user


def identity(payload):
    user_id = payload['identity']
    for user in in_memory_users:
        if user.id == user_id:
            return user
