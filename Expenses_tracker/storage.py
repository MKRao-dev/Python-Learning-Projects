import json

def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

def remove_expense(expenses):
    if not expenses:
        print("No expenses recorded.")
        return

    print("Select an expense to remove:")
    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense['description']} - {expense['amount']}")

    choice = int(input("Enter the number of the expense to remove: "))
    if 1 <= choice <= len(expenses):
        removed_expense = expenses.pop(choice - 1)
        print(f"Removed expense: {removed_expense['description']} - {removed_expense['amount']}")
    else:
        print("Invalid choice.")
