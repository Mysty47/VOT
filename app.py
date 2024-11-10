from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Функция за свързване към базата данни
def get_db():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return "Welcome to the Web App!"

# API endpoint за получаване на всички записи от базата данни
@app.route('/items', methods=['GET'])
def get_items():
    conn = get_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM items')
    rows = cur.fetchall()
    items = [dict(row) for row in rows]
    conn.close()
    return jsonify(items)

# API endpoint за добавяне на нов запис
@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.json
    conn = get_db()
    cur = conn.cursor()
    cur.execute('INSERT INTO items (name, description) VALUES (?, ?)',
                (new_item['name'], new_item['description']))
    conn.commit()
    conn.close()
    return jsonify(new_item), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
