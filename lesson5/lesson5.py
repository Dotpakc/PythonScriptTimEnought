# # Sqlite3
# import sqlite3

# # Connect to database
# conn = sqlite3.connect('lesson5/lesson5.sqlite3')

# #Курсор - это объект, который выполняет запросы и получает их результаты
# c = conn.cursor() 


# # Create table
# c.execute('''CREATE TABLE IF NOT EXISTS Monsters
#           (name text, health integer, level integer, team text)''')
# # .execute - метод курсора, который выполняет запросы

# c.execute('''CREATE TABLE IF NOT EXISTS Players
#             (name text, health integer, level integer, team text, experience integer, gold integer, attack integer, armor integer)''')

# # Insert a row of data
# c.execute("INSERT INTO Monsters VALUES ('Goblin44', 100, 1, 'Monster')")
# c.execute("INSERT INTO Monsters VALUES ('Orc666', 200, 2, 'Monster')")
# c.execute("INSERT INTO Monsters VALUES ('Troll777', 300, 3, 'Monster')")
# c.execute("INSERT INTO Monsters VALUES ('Dragon888', 400, 4, 'Monster')")

# c.execute("INSERT INTO Players VALUES ('Player3', 100, 1, 'Player', 0, 0, 10, 5)")
# c.execute("INSERT INTO Players VALUES ('Player4', 200, 4, 'Player', 0, 0, 20, 10)")

# conn.commit()# .commit - метод соединения, который сохраняет изменения
# conn.close() # .close - метод соединения, который закрывает соединение


#PostgreSQL
import psycopg2

conn = psycopg2.connect(
    user = "postgres",
    password = "Ваш пароль1234",
    host = "localhost",
    port = "5432",
    database = "Game")

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS Monsters
            (id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            health INTEGER NOT NULL,
            level INTEGER NOT NULL)''')

c.execute('''INSERT INTO Monsters (name, health, level) VALUES ('Goblin44', 100, 1)''')
c.execute('''INSERT INTO Monsters (name, health, level) VALUES ('Orc666', 200, 2)''')
c.execute('''INSERT INTO Monsters (name, health, level) VALUES ('Troll777', 300, 3)''')

conn.commit()
conn.close()