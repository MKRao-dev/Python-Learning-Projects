import csv

def read_stock_data(filename):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        data_list = []
        for row in reader:
            data_list.append(row)
    return data_list

def calculate_daily_returns(data_list):
    previous_price = float(data_list[0]['Close'].replace('$', '').replace(',', ''))
    returns = []
    for row in data_list[1:]:
        current_price = float(row['Close'].replace('$', '').replace(',', ''))
        daily_return = (current_price - previous_price) / previous_price
        returns.append({'date': row['Date'], 'return': daily_return})
        previous_price = current_price
    return returns

def calculate_cumulative_return(returns):
    cumulative_return = 1
    for row in returns:
        cumulative_return *= (1 + row['return'])
    return cumulative_return - 1

def print_stock_analysis(avg_return, max_return, worst_return, cumulative_return):
    print(f"Average Daily Return: {avg_return:.4%}")
    print(f"Maximum Daily Return: {max_return['return']:.4%} on {max_return['date']}")
    print(f"worst Daily Return: {worst_return['return']:.4%} on {worst_return['date']}") 
    print(f"Cumulative Return: {cumulative_return:.4%}")

data_list = read_stock_data("HistoricalQuotes.csv")
data_list.reverse()
returns = calculate_daily_returns(data_list)
max_return = returns[0]
worst_return = returns[0]
total_return = 0
for row in returns:
    total_return += row['return']
    if row['return'] > max_return['return']:
        max_return = row
    if row['return'] < worst_return['return']:
        worst_return = row
avg_return = total_return / len(returns)

cumulative_return = calculate_cumulative_return(returns)

print_stock_analysis(avg_return, max_return, worst_return, cumulative_return)