import sqlite3

def create_tables():
    connection = sqlite3.connect("data/budget.db")
    cursor = connection.cursor()    

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT NOT NULL,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        amount REAL NOT NULL,
        date TEXT NOT NULL
    )
    """)

    print("Database and tables created")

    connection.commit()
    connection.close()

def add_transaction(type, name, category, amount, date):
    connection = sqlite3.connect("data/budget.db")
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO transactions (type, name, category, amount, date)
        VALUES (?, ?, ?, ?, ?)
    """, (type, name, category, amount, date))

    connection.commit()
    connection.close()


create_tables()

