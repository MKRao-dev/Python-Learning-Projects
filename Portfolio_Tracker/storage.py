import json

def view_transaction_history(history):
    if history:
        print("Transaction History:")
        for row in history:
            print(f"{row['date']}: {row['action']} {row['quantity']} shares of {row['stock']} at ${row['price']} each")
    else:
        print("No transactions to display.")

def view_portfolio(portfolio):
    if portfolio:
        print("Current Portfolio:")
        for index, row in enumerate(portfolio, start=1):
            print(f"{index}. {row['stock']}: {row['quantity']} shares at average price of ${row['avg_price']} each")
    else:
        print("Portfolio is empty.")

def save_portfolio(portfolio, history):
    with open("portfolio.json", "w") as file:
        json.dump(portfolio, file, indent=4)
    with open("transaction_history.json", "w") as file:
        json.dump(history, file, indent=4)
    print("Portfolio saved successfully.")