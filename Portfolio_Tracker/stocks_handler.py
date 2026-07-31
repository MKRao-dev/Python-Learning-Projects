from storage import view_portfolio
from ui import stock_options

def buy(stocks,date,portfolio,history,cash):
    print("select a stock to buy")
    stock_options(stocks)
    number = input("enter the stock number you want to buy: ")
    quantity = input("enter the quantity you want to buy: ")
    if not number.isdigit() or not 0 < int(number) <= len(stocks):
        print("Invalid Quantity,Please try again")
        return 'invalid'
    if not quantity.isdigit() or int(quantity) <= 0:
        print("Quantity must be greater than zero.")
        return 'invalid'
    row = stocks[int(number) - 1]
    stock_exists = False
    for line in portfolio:
        if line['stock'] == row['stock']:
            line['avg_price'] = (line['quantity'] * line['avg_price'] + float(quantity) * row['price'])/(line['quantity'] + float(quantity))
            line['quantity'] += int(quantity)
            stock_exists = True
            break
    if not stock_exists:
        portfolio.append({'stock': row['stock'], 'avg_price': row['price'], 'quantity': int(quantity)})
    print(f"Bought {quantity} shares of {row['stock']} at ${row['price']} each")
    history.append({'date': date, 'action': 'BUY', 'stock': row['stock'], 'price': row['price'], 'quantity': int(quantity)})
    cash -= int(quantity) * row['price']
    return cash

def sell(stocks,date,portfolio,history,cash):
    print("select a stock to sell")
    view_portfolio(portfolio)
    number = input("enter the stock number you want to sell: ")
    quantity = input("enter the quantity you want to sell: ")
    if not number.isdigit() or not 0 < int(number) <= len(portfolio):
        print("Invalid Quantity,Please try again")
        return 'invalid'
    if not quantity.isdigit() or int(quantity) <= 0 or int(quantity) > portfolio[int(number)-1]['quantity']:
        print("Invalid Quantity,Please try again")
        return 'invalid'

    row = portfolio[int(number) - 1]
    for stock in stocks:
        if row['stock'] == stock['stock']:
            current_price = stock['price']
    row['quantity'] -= int(quantity)
    if row['quantity'] == 0:
        portfolio.remove({'stock': row['stock'], 'avg_price': row['avg_price'],'quantity': 0})
    history.append({'date': date, 'action': 'SELL', 'stock': row['stock'], 'price': row['avg_price'], 'quantity': int(quantity)})
    print(f"Sold {quantity} shares of {row['stock']} at ${current_price} each")
    cash += int(quantity) * current_price
    return cash
