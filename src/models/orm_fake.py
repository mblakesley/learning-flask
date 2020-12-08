import sqlite3

from src.user import User


class DB:
    def __init__(self):
        self.connection = sqlite3.connect('users.db')
        self.cursor = self.connection.cursor()

    def save(self):
        self.connection.commit()

    def disconnect(self):
        self.connection.close()

    def get_user_by_x(self, field, value):
        result = self.cursor.execute(f'select * from users where {field}=?', [value])
        row = result.fetchone()
        if not row:
            raise ValueError
        return User(*row)
