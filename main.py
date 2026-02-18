from expense import Expense
from file_handler import save_expense, read_expenses, calculate_total, category_summary


def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category: ")
    date = input("Enter date (YYYY-MM-DD): ")

    try:
        expense = Expense(amount, category, date)
        save_expense(expense)
        print("✅ Expense added successfully!\n")
    except ValueError:
        print("❌ Invalid amount. Please enter a number.\n")


def view_expenses():
    expenses = read_expenses()
    if not expenses:
        print("No expenses found.\n")
        return

    print("\n--- All Expenses ---")
    for exp in expenses:
        print(f"{exp.date} | {exp.category} | ₹{exp.amount}")
    print()


def show_summary():
    expenses = read_expenses()
    total = calculate_total(expenses)
    summary = category_summary(expenses)

    print("\n--- Monthly Summary ---")
    print(f"Total Spent: ₹{total}")
    print("Category Wise:")
    for category, amount in summary.items():
        print(f"{category}: ₹{amount}")
    print()


def main():
    while True:
        print("==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
