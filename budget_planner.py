def show_menu():
    print("\nStudent Budget Planner")
    print("1. Add income")
    print("2. Add expense")
    print("3. View transactions")
    print("4. View summary")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            print("Add income feature coming soon")

        elif choice == "2":
            print("Add expense feature coming soon")

        elif choice == "3":
            print("View transactions feature coming soon")

        elif choice == "4":
            print("Summary feature coming soon")

        elif choice == "5":
            print("Goodbye")
            break

        else:
            print("Invalid option. Try again.")


main()