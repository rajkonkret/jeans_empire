import sqlite3


def init_db():
    conn = sqlite3.connect('jeans_empire.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY,
            name TEXT,
            value REAL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS campaigns (
            id INTEGER PRIMARY KEY,
            name TEXT,
            budget REAL,
            start_date TEXT,
            end_date TEXT
        )
    ''')
    cursor.execute('''
           CREATE TABLE IF NOT EXISTS projects (
               id INTEGER PRIMARY KEY,
               name TEXT,
               budget REAL,
               start_date TEXT,
               end_date TEXT,
               description TEXT
           )
       ''')

    conn.commit()
    conn.close()


def save_value(name, value):
    conn = sqlite3.connect('jeans_empire.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO items (name, value) VALUES (?, ?)', (name, value))
    conn.commit()
    conn.close()


def get_all_values():
    conn = sqlite3.connect('jeans_empire.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM items')
    values = cursor.fetchall()
    conn.close()
    return values


def get_value_by_id(item_id):
    conn = sqlite3.connect('jeans_empire.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM items WHERE id=?', (item_id,))
    item = cursor.fetchone()
    conn.close()
    return item


def save_campaign(name, budget, start_date, end_date):
    conn = sqlite3.connect('jeans_empire.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO campaigns (name, budget, start_date, end_date) VALUES (?, ?, ?, ?)',
                   (name, budget, start_date, end_date))
    conn.commit()
    conn.close()


def get_all_campaigns():
    conn = sqlite3.connect('jeans_empire.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM campaigns')
    values = cursor.fetchall()
    conn.close()
    return values


def save_project(name, budget, start_date, end_date, description):
    conn = sqlite3.connect('jeans_empire.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO projects (name, budget, start_date, end_date, description) VALUES (?, ?, ?, ?, ?)',
                   (name, budget, start_date, end_date, description))
    conn.commit()
    conn.close()


def get_all_projects():
    conn = sqlite3.connect('jeans_empire.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM projects')
    values = cursor.fetchall()
    conn.close()
    return values
