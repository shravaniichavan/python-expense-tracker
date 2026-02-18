from expense import Expense

FILE_NAME = "expenses.csv"


def save_expense(expense):
    with open(FILE_NAME, "a") as file:
        file.write(expense.to_csv())


def read_expenses():
    expenses = []
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                amount, category, date = line.strip().split(",")
                expenses.append(Expense(amount, category, date))
    except FileNotFoundError:
        pass
    return expenses


def calculate_total(expenses):
    return sum(exp.amount for exp in expenses)


def category_summary(expenses):
    summary = {}
    for exp in expenses:
        if exp.category in summary:
            summary[exp.category] += exp.amount
        else:
            summary[exp.category] = exp.amount
    return summary
