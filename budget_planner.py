transactions = []


def show_menu():
    print("\nStudent Budget Planner")
    print("1. Add income")
    print("2. Add expense")
    print("3. View transactions")
    print("4. View summary")
    print("5. Exit")


def add_income():
    source = input("Enter income source: ")
    amount = float(input("Enter amount: "))
    date = input("Enter date: ")

    income = {
        "type": "income",
        "source": source,
        "amount": amount,
        "date": date
    }

    transactions.append(income)

    print("Income added successfully")

def add_expense():
    category = input("Enter expense category: ").lower()
    amount = float(input("Enter amount: "))
    date = input("Enter date: ")

    expense = {
        "type": "expense",
        "category": category,
        "amount": amount,
        "date": date
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

        if transaction["type"] == "income":
            print(f"   Source: {transaction['source']}")

        elif transaction["type"] == "expense":
            print(f"   Category: {transaction['category']}")

        print(f"   Amount: ${transaction['amount']:.2f}")


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
            print("Summary feature coming soon")

        elif choice == "5":
            print("Goodbye")
            break

        else:
            print("Invalid option")


main()