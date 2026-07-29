def get_total(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    print("Total amount spent:", total)

def get_expenses(expenses):
    if not expenses:
                print("No expenses recorded.")
    else:
        print("Viewing expenses...")
        for expense in expenses:
            print(expense["description"], "-", expense["amount"])

def add_expense(expenses):
    description = input("Enter expense description: ")
    amount = int(input("Enter expense amount: "))
    expense = {"description": description, "amount": amount}
    expenses.append(expense)
    print("Expense added successfully!")

