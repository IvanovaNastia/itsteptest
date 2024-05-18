import sqlite3


'''
connection = sqlite3.connect("itstep_DB.sl3", 5)
cur = connection.cursor()

print(connection)
print(cur)
connection.close()

'''
connection = sqlite3.connect("itstep_DB.sl3", 5)
cur = connection.cursor()
cur.execute("CREATE TABLE first_table (name TEXT);")
connection.commit()
connection.close()


''' 
connection = sqlite3.connect("itstep_DB.sl3", 5)
cur = connection.cursor()
cur.execute("INSERT INTO first_table (name) VALUES ('Nick');")
connection.commit()
connection.close()



connection = sqlite3.connect("itstep_DB.sl3", 5)
cur = connection.cursor()
cur.execute("SELECT rowid, name FROM first_table;")
connection.commit()
res = cur.fetchall()
print(res)
connection.close()
'''






