import json
import csv

def read_history():
    try:
        with open('transaction_history.json', 'r') as file:
            history = json.load(file)
    except FileNotFoundError:
        history = []
    return history

def read_stocks_from_file(filename):
    stocks = []
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                stocks.append({'stock': row['Ticker'], 'price': float(row['Price'])})
    except FileNotFoundError:
        print(f"File {filename} not found.")
    return stocks

def read_portfolio():
    try:
        with open('portfolio.json', 'r') as file:
            portfolio = json.load(file)
    except FileNotFoundError:
        portfolio = []
    return portfolio
