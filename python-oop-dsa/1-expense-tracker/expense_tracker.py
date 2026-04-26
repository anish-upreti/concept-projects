import csv

class Category:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return f"Category('{self.name}')"    # the convention for __repr__ is that it should look like valid Python code you could copy-paste to recreate the objec


class Expense:
    def __init__(self, item, amount, category, date):
        self.item = item
        self.amount = amount
        self.category = category
        self.date = date

        if amount < 0:
            raise ValueError("amount should not be negative")
        
        if not isinstance(category, Category):
            raise TypeError("category should be a Category object")

    def __str__(self):
        return f"{self.item} - {self.amount} - {self.category} - {self.date}"
    
    def __repr__(self):
        return f"Expense('{self.item}', {self.amount}, {self.category!r}, '{self.date}')"
    
    @property
    def month(self):
        date = self.date.split("-")
        month = date[1]
        return month
    
    @property
    def year(self):
        date = self.date.split("-")
        year = date[0]
        return year
    
    # A class method lets us create an Expense object in a different way. For example, what if the data comes as a single string like:
    # "Coffee,250,Food & Drinks,2026-04-15"

    @classmethod
    def from_string(cls, expense_string):
        item, amount, category, date = expense_string.split(",")
        category_obj = Category(category)
        return cls(item, int(amount), category_obj, date)
    
class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def remove_expense(self, expense):
        self.expenses.remove(expense)

    def filter_by_category(self, category_name):
        result = []
        for expense in self.expenses:
            if expense.category.name == category_name:
                result.append(expense)
        return result

    def monthly_summary(self, month, year):
        total = 0
        for expense in self.expenses:
            if expense.month  == month and expense.year == year:
                total += expense.amount
        return total
    
    def export_to_csv(self, filename):
        with open(filename, "w") as f:
            writer = csv.writer(f)
            writer.writerow(["item", "amount", "category", "date"])     # header
            for expense in self.expenses:
                writer.writerow([expense.item, expense.amount, expense.category.name, expense.date])       # each expense

    

c = Category("Food & Drinks")
e = Expense("Coffee", 250, c, "2026-04-15")
print(e)
print(repr(e))
print(e.month)
print(e.year)
# print(c)    # uses __str__
# print(repr(c))    # uses __repr__



# test 1 - basic add and print
tracker = ExpenseTracker()
tracker.add_expense(e)
print(tracker.expenses)

# test 2 - filter by category
food = Category("Food & Drinks")
travel = Category("Travel")
e1 = Expense("Coffee", 250, food, "2026-04-15")
e2 = Expense("Bus", 50, travel, "2026-04-15")
tracker.add_expense(e1)
tracker.add_expense(e2)
print(tracker.filter_by_category("Food & Drinks"))

# test 3 - monthly summary
print(tracker.monthly_summary("04", "2026"))

# test 4 - from_string
e3 = Expense.from_string("Lunch,300,Food & Drinks,2026-04-20")
print(e3)

# test 5 - validation
try:
    Expense("Tea", -50, food, "2026-04-15")   # should raise ValueError
except ValueError as e:
    print(f"ValueError caught : {e}")

try:
    Expense("Tea", 50, "Food & Drinks", "2026-04-15")   # should raise TypeError
except TypeError as e:
    print(f"TypeError caught: {e}")

# test 6 - export to csv 
tracker.export_to_csv("expenses.csv")