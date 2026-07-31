from ui import menu 
from stocks_handler import buy, sell
from initialize import read_portfolio, read_stocks_from_file, read_history
from storage import view_transaction_history, view_portfolio, save_portfolio
from account import open_account,save_cash,check_cash,portfolio_value

stocks = read_stocks_from_file('prices.csv')
history = read_history()
portfolio = read_portfolio()
cash = open_account()

print("Welcome to the Portfolio Tracker!")
date = input("Enter the date (YYYY-MM-DD): ")
print("transactions are recorded only after you save the portfolio, so make sure to save your portfolio after every transaction.")

while True:
    menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        x = buy(stocks,date,portfolio,history,cash)
        if x != 'invalid':
            cash = x        
    elif choice == '2':
        if len(portfolio) == 0:
            print("You have no stocks to sell.")
        else:
            x = sell(stocks,date,portfolio,history,cash)
            if x != 'invalid':
                cash = x
    elif choice == '3':
        view_portfolio(portfolio)
    elif choice == '4':
        view_transaction_history(history)
    elif choice == '5':
        save_portfolio(portfolio, history)
        save_cash(cash)
    elif choice == '6':
        check_cash(cash)
        portfolio_value(portfolio,stocks,cash)
    elif choice == '7':
        break
    else:
        print("Invalid choice. Please try again.")
    