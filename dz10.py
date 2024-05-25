import sqlite3


# connection = sqlite3.connect("AnimalKingdom.sl3", 5)
# cur = connection.cursor()
#
# print(connection)
# print(cur)
# connection.close()


# connection = sqlite3.connect("AnimalKingdom.sl3", 5)
# cur = connection.cursor()
# cur.execute("CREATE TABLE animals (id, animal_name, animal_type TEXT);")
# connection.commit()
# connection.close()


# connection = sqlite3.connect("AnimalKingdom.sl3", 5)
# cur = connection.cursor()
# cur.execute("DELETE FROM animals WHERE rowid=1;")
# cur.execute("DELETE FROM animals WHERE rowid=2;")
# cur.execute("DELETE FROM animals WHERE rowid=3;")
# cur.execute("DELETE FROM animals WHERE rowid=4;")
# cur.execute("DELETE FROM animals WHERE rowid=5;")
# connection.commit()
# connection.close()


# connection = sqlite3.connect("AnimalKingdom.sl3", 5)
# cur = connection.cursor()
# cur.execute("INSERT INTO animals VALUES ('1', 'Lion', 'Mammal');")
# cur.execute("INSERT INTO animals VALUES ('2', 'Crocodile', 'Reptile');")
# cur.execute("INSERT INTO animals VALUES ('3', 'Eagle', 'Bird');")
# cur.execute("INSERT INTO animals VALUES ('4', 'Sea turtle', 'Reptile');")
# cur.execute("INSERT INTO animals VALUES ('5', 'Monkey', 'Mammal');")
# connection.commit()
# connection.close()


# connection = sqlite3.connect("AnimalKingdom.sl3", 5)
# cur = connection.cursor()
# cur.execute("UPDATE animals SET animal_name='Falcon' WHERE rowid=3;")
# connection.commit()
# connection.commit()
# connection.close()


# connection = sqlite3.connect("AnimalKingdom.sl3")
# cur = connection.cursor()
#
# cur.execute("SELECT * FROM animals WHERE animal_type = 'Mammal'")
# connection.commit()
# res = cur.fetchall()
# print(res)
# connection.close()


# connection = sqlite3.connect("AnimalKingdom.sl3", 5)
# cur = connection.cursor()
# cur.execute("SELECT * FROM animals;")
# connection.commit()
# res = cur.fetchall()
# print(res)
# connection.close()

