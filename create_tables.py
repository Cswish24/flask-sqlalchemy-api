# import sqlite3
#
# connection = sqlite3.connect('data.db')
# cursor = connection.cursor()
#
# create_table = "Create Table IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
# cursor.execute(create_table)
#
# create_table = "Create Table IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"
# cursor.execute(create_table)
#
#
# connection.commit()
#
# connection.close()        sqlalchemy can create tables