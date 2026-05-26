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

def get_transactions():
    connection = sqlite3.connect("data/budget.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM transactions")

    transaction = cursor.fetchall()

    connection.commit()
    connection.close()

    return transaction


create_tables()


""" transactions = get_transactions()

for transaction in transactions:
    print(f"{transaction[1]} | {transaction[2]} | ${transaction[4]:.2f}")

""" 