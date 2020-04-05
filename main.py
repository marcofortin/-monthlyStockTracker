# Imports
import yfinance as yf
from datetime import date, timedelta

# Set the range of data needed
endDate = date.today()

# If weekend, set to last Friday
if endDate.weekday() == 5:
    endDate -= timedelta(days=1)
elif endDate.weekday() == 6:
    endDate -= timedelta(days=2)

# Go back a Month
startDate = endDate.replace(month=endDate.month - 1)

# Select stock
selectedStock = input("Enter the stock's ticket symbol in all caps: ")

# Get stock's data going back a Month
data = yf.download(selectedStock, start=startDate, end=endDate)

# Initialize list containing all the opening and closing prices
prices = []

# Add all the opening and closing prices
for index, row in data.iterrows():
    prices.append(row['Open'])
    prices.append(row['Close'])

# Initialize the profit
profit = 0

# For each price
for i in range(1, len(prices)):
    # If a profit coud have been done
    if prices[i] > prices[i - 1]:
        # Add it
        profit += prices[i] - prices[i - 1]

print("Possible monthly profit: $", profit)