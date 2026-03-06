import sqlite3
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users(
                   id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, password TEXT NOT NULL, email TEXT UNIQUE NOT NULL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, age INTEGER, grade TEXT,email TEXT)''' )
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL,description TEXT,status TEXT DEFAULT 'Pending', user_id INTEGER, FOREIGN KEY(user_id) REFERENCES users(id))''' )
    conn.commit()
    conn.close()
    print("Database created successfully!")

if __name__=="__main__":
    init_db()
    

