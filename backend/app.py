from flask import Flask, render_template, request, redirect,session,url_for
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

def get_db():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        conn = get_db()
        try:
            conn.execute('INSERT INTO users (username,password,email) VALUES (?, ?, ?)',(username, password, email))
            conn.commit()
            return redirect(url_for('login'))
        except:
            return "Username or email already exists!"
        finally:
            conn.close()
    return render_template('register.html')
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db()
        user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?',(username,password)).fetchone()
        conn.close()

        if user:
            session['user_id'] = user['id']
            session['username'] = user['username']
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')
    
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html',username=session['username'])
    
@app.route('/students')
def students():
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    conn = get_db()
    students = conn.execute('SELECT * FROM students').fetchall()
    conn.close()
    return render_template('crud.html', students=students)
    
@app.route('/students/add',methods=['POST'])    
def add_student():
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    name = request.form['name']
    age = request.form['age']
    grade = request.form['grade']
    email = request.form['email']
    conn = get_db()
    conn.execute('INSERT INTO students(name, age, grade, email) VALUES (?,?,?,?)',(name, age, grade, email))
    conn.commit()
    conn.close()
    return redirect(url_for('students'))
    
@app.route('/students/edit/<int:id>', methods=['POST'])
def edit_student(id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    name = request.form['name']
    age = request.form['age']
    grade = request.form['grade']
    email = request.form['email']
    conn = get_db()
    conn.execute('UPDATE students SET name=?, age=?, grade=?, email=? WHERE id=?',(name, age, grade, email, id))
    conn.commit()
    conn.close()
    return redirect(url_for('students'))
    
@app.route('/students/delete/<int:id>')
def delete_student(id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    conn = get_db()
    conn.execute('DELETE FROM students WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('students'))
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
    
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
    
        
