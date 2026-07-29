import json
from storage import load_expenses, save_expenses, remove_expense
from expense import get_total, get_expenses, add_expense
from ui import menu

expenses = load_expenses()
while True:  
    menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        add_expense(expenses)
    elif choice == "2":
        get_expenses(expenses)
        save_expenses(expenses)
    elif choice == "3":
        get_total(expenses)
    elif choice == "4":
        remove_expense(expenses)
        save_expenses(expenses)
    elif choice == "5":
        print("Goodbye!")
        break
    else :
        print("Invalid choice.")