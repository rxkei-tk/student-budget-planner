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

    income = {
        "type": "income",
        "source": source,
        "amount": amount
    }

    transactions.append(income)

    print("Income added successfully")


def view_transactions():
    if not transactions:
        print("No transactions yet")
        return

    print("\nTransactions:")

    for transaction in transactions:
        print(
            f"{transaction['type']} | "
            f"{transaction['source']} | "
            f"${transaction['amount']}"
        )


def main():
    while True:
        show_menu()

        choice = input("Choose an option: ")

        if choice == "1":
            add_income()

        elif choice == "2":
            print("Add expense feature coming tomorrow")

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