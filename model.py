import sqlite3


def get_user_byid(user_id):
    connection = sqlite3.connect("db.db")
    cursor = connection.cursor()
    sql = "select * from users where user_id = ?"
    cursor.execute(sql, (user_id,))
    user = cursor.fetchone()
    connection.close()
    return user


def add_new_user(user):
    user_id = user['user_id']
    first_name = user['first_name']
    last_name = user['last_name']
    username = user['username']
    connection = sqlite3.connect("db.db")
    cursor = connection.cursor()
    sql = "insert into users  (user_id, first_name, last_name, username ) values (?, ?, ?, ?)"
    cursor.execute(sql, (user_id, first_name, last_name, username))
    connection.commit()
    connection.close()
    return user


def add_user_city(user_id, city):
    connection = sqlite3.connect("db.db")
    cursor = connection.cursor()
    sql = "update users set `city` = ? where user_id = ?"
    cursor.execute(sql, (city, user_id))
    connection.commit()
    connection.close()
