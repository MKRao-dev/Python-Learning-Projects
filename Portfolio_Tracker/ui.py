import csv

def menu():
    print("Portfolio Tracker")
    print("1. Buy Stock")
    print("2. Sell Stock")
    print("3. View Portfolio")
    print("4. View Transaction History")
    print("5. Save Portfolio")
    print("6. Check Cash, Portfolio Value, Total Equity")
    print("7. Exit")

def stock_options(stocks):
    print("Available Stocks:")
    for index, row in enumerate(stocks, start=1):
        print(f"{index}. {row['stock']}: ${row['price']}")
   