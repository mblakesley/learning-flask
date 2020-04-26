import sqlite3

sql = sqlite3.connect('users.db')
curse = sql.cursor()
curse.execute('create table users (id integer primary key, username text, password text)')
datums = (
    ('bhorseman', 'brand new attitude'),
    ('dnguyen', 'am i doing drugs wrong?'),
    ('pcaroline', 'you gotta get your shit together'),
)
curse.executemany('insert into users (username, password) values (?, ?)', datums)
# print(list(curse.execute('select * from users where username="pcaroline"')))
sql.commit()
sql.close()
