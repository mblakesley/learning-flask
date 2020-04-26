from werkzeug.security import safe_str_cmp
from models.orm_fake import DB

db = DB()


def authenticate(username, password):
    user = db.get_user_by_x('username', username)
    if safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return db.get_user_by_x('id', user_id)
