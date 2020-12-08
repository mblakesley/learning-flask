import sqlite3
from pprint import pprint

sql = sqlite3.connect('users.db')
curse = sql.cursor()
x = curse.execute('SELECT name FROM sqlite_master WHERE type="table" and name="users";').fetchall()
if len(x) < 1:
    curse.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
    datums = (
        ('bhorseman', 'brand new attitude'),
        ('dnguyen', 'am i doing drugs wrong?'),
        ('pcaroline', 'you gotta get your shit together'),
    )
    curse.executemany('INSERT INTO users (username, password) VALUES (?, ?)', datums)
    # print(list(curse.execute('select * from users where username="pcaroline"')))
    sql.commit()
# context manager?
sql.close()
