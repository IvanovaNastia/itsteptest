import sqlite3

# connection = sqlite3.connect("itstep_DB.db", 5)
# cur = connection.cursor()
#
# print(connection)
# print(cur)
# connection.close()


# connection = sqlite3.connect("itstep_DB.db", 5)
# cur = connection.cursor()
# cur.execute("CREATE TABLE first_table (name TEXT);")
# connection.commit()
# connection.close()

# connection = sqlite3.connect("itstep_DB.db", 5)
# cur = connection.cursor()
# cur.execute("INSERT INTO first_table (name) VALUES ('Nick');")
# connection.commit()
# connection.close()

# connection = sqlite3.connect("itstep_DB.db", 5)
# cur = connection.cursor()
# cur.execute("SELECT rowid, name FROM first_table;")
# connection.commit()
# res = cur.fetchall()
# print(res)
# connection.close()



# connection = sqlite3.connect("itstep_DB.db", 5)
# cur = connection.cursor()
# cur.execute("INSERT INTO first_table (name) VALUES ('Ann');")
# cur.execute("INSERT INTO first_table (name) VALUES ('Kats');")
# cur.execute("INSERT INTO first_table (name) VALUES ('John');")
# connection.commit()
# cur.execute("SELECT rowid, name FROM first_table;")
# connection.commit()
# res = cur.fetchall()
# print(res)
# connection.close()



# connection = sqlite3.connect("itstep_DB.db", 5)
# cur = connection.cursor()
# cur.execute("INSERT INTO first_table (name) VALUES ('Nick');")
# connection.commit()
# connection.close()


# connection = sqlite3.connect("itstep_DB.db", 5)
# cur = connection.cursor()
# cur.execute("SELECT rowid, name FROM first_table;")
# connection.commit()
# res = cur.fetchall()
# print(res)
# connection.close()

connection = sqlite3.connect("itstep_DB.db", 5)
cur = connection.cursor()
cur.execute("DELETE FROM first_table WHERE rowid=2;")
connection.commit()
connection.close()

# connection = sqlite3.connect("itstep_DB.db", 5)
# cur = connection.cursor()
# cur.execute("INSERT INTO first_table (name) VALUES ('Ann');")
# cur.execute("INSERT INTO first_table (name) VALUES ('Kats');")
# cur.execute("INSERT INTO first_table (name) VALUES ('John');")
# connection.commit()
# cur.execute("SELECT rowid, name FROM first_table;")
# connection.commit()
# res = cur.fetchall()
# print(res)
# connection.close()


# connection = sqlite3.connect("itstep_DB.db", 5)
# cur = connection.cursor()
# cur.execute("INSERT INTO first_table (name) VALUES ('Lion');")
# cur.execute("INSERT INTO first_table (name) VALUES ('Crocodile');")
# cur.execute("INSERT INTO first_table (name) VALUES ('Eagle');")
# cur.execute("INSERT INTO first_table (name) VALUES ('Sea turtle');")
# cur.execute("INSERT INTO first_table (name) VALUES ('Monkey');")
# connection.commit()
# connection.close()
