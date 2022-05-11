import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, ingredients, content, linkimg) VALUES (?, ?, ?,?)",
            ('Berghrir', 
            'test','test','C:/Users/Naila/Desktop/CFA INSTA/Projet Docker FlaskApp/static/Baghrir.jpg')
            )

# cur.execute("INSERT INTO posts (title, ingredients, content, linkimg) VALUES (?, ?)",
#             ('Second Post', 'Content for the second post')
#             )

connection.commit()
connection.close()