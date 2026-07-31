def open_account():
    with open('cash.txt','r') as file:
        cash = float(file.readline()) 
    return cash

def check_cash(cash):
    print(f"Current Cash: {cash}")

def save_cash(cash):
    with open('cash.txt','w') as file:
        file.write(f"{cash}")

def portfolio_value(portfolio,stocks,cash):
    value = 0
    for my_stock in portfolio:
        for current_stock in stocks:
            if my_stock['stock'] == current_stock['stock']:
                value += my_stock['quantity'] * current_stock['price']
    print(f"Portfolio value: ${value}")
    print(f"Total Equity: {cash + value}")
