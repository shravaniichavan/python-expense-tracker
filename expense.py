class Expense:
    def __init__(self, amount, category, date):
        self.amount = float(amount)
        self.category = category
        self.date = date

    def to_csv(self):
        return f"{self.amount},{self.category},{self.date}\n"
