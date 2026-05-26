from flask import Flask, jsonify
from database import get_transactions

app = Flask(__name__)

@app.route("/")
def home():
    return "Student Budget Planner API Running"


@app.route("/test")
def test():
    return "API test successful"


@app.route("/transactions")
def transactions():
    rows = get_transactions()
    return jsonify([dict(row) for row in rows])


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050, debug=True)

""" 

transactions = []


def show_menu():
    print("\nStudent Budget Planner")
    print("1. Add income")
    print("2. Add expense")
    print("3. View transactions")
    print("4. View summary")
    print("5. View category spending")
    print("6. Exit")


def add_income():
    source = input("Enter income source: ")
    
    try:
        amount = float(input("Enter amount: "))
    
    except ValueError:
        print("Invalid number")

    income = {
        "type": "income",
        "name": source,
        "category": "income",
        "amount": amount
    }

    transactions.append(income)

    print("Income added successfully")
    print("Income added successfully")


def add_expense():

    category = input("Enter expense category: ").lower()

    try:
        amount = float(input("Enter amount: "))
    
    except ValueError:
        print("Invalid number")

    expense = {
        "type": "expense",
        "name": category,
        "category": category,
        "amount": amount
    }

    transactions.append(expense)

    print("Expense added successfully")


def view_transactions():

    if not transactions:
        print("\nNo transactions yet")
        return

    print("\nTransactions")

    for index, transaction in enumerate(transactions, start=1):

        print(f"\n{index}. {transaction['type'].upper()}")
        print(f"   Name: {transaction['name']}")
        print(f"   Category: {transaction['category']}")
        print(f"   Amount: ${transaction['amount']:.2f}")


def view_summary():

    total_income = 0
    total_expenses = 0

    for transaction in transactions:

        if transaction["type"] == "income":
            total_income += transaction["amount"]

        elif transaction["type"] == "expense":
            total_expenses += transaction["amount"]

    remaining_balance = total_income - total_expenses
    savings_rate = (remaining_balance / total_income) * 100

    print("\nFinancial Summary")
    print(f"\nTotal Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Remaining Balance: ${remaining_balance:.2f}")
    print(f"Saving Rate: {savings_rate:.2f}%")

    if remaining_balance < 0:
        print("Warning: You are overspending")


def view_category_summary():

    category_totals = {}

    for transaction in transactions:

        if transaction["type"] == "expense":

            category = transaction["category"]
            amount = transaction["amount"]

            if category not in category_totals:
                category_totals[category] = 0

            category_totals[category] += amount

    if not category_totals:
        print("\nNo expense data available")
        return

    print("\nSpending By Category")

    for category, total in category_totals.items():
        print(f"{category}: ${total:.2f}")


def main():
    while True:
        show_menu()

        choice = input("Choose an option: ")

        if choice == "1":
            add_income()

        elif choice == "2":
            add_expense()

        elif choice == "3":
            view_transactions()

        elif choice == "4":
            view_summary()

        elif choice == "5":
            view_category_summary()

        elif choice == "6":
            print("Goodbye")
            break

        else:
            print("Invalid option")


main()
"""