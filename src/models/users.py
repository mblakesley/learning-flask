from hashlib import md5

from pydantic.main import BaseModel


class User(BaseModel):
    user: str
    password: str


fake_users_db: dict = {
    'bhorseman': {
        'user': 'bhorseman',
        'password': '54873eed8c5ce25c4441e7d726325184',
    },
    'tchavez': {
        'user': 'tchavez',
        'password': '9cc6a2962537f146b6ac07082be925bc',
    },
}


def shit_hash(s: str) -> str:
    return md5(s.encode()).hexdigest()
