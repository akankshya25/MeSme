from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Initialize DB
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            product TEXT NOT NULL,
            quantity INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('Mesme.html')

@app.route('/order', methods=['POST'])
def order():
    name = request.form['name']
    email = request.form['email']
    product = request.form['product']
    quantity = request.form['quantity']

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO orders (name, email, product, quantity)
        VALUES (?, ?, ?, ?)
    ''', (name, email, product, quantity))
    conn.commit()
    conn.close()

    return redirect(url_for('home'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
