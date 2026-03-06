CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, password TEXT NOT NULL,
email TEXT UNIQUE NOT NULL);
CREATE TABLE students(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, age INTEGER, grade TEXT,email TEXT);
CREATE TABLE tasks(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, description TEXT, status TEXT DEFAULT 'Pending', user_id INTEGER, FOREIGN KEY(user_id) REFERENCES users (id));

INSERT INTO users(username,password,email) VALUES('admin', 'admin123', 'admin@gmail.com');
INSERT INTO students(name, age, grade,email) VALUES ('krish',25,'A','krish@gmail.com');
INSERT INTO tasks(title, description, user_id) VALUES ('Simple Task', 'This is a sample task', 1);