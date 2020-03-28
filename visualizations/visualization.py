import pandas as pd
import datetime as dt
import pandas_datareader.data as pdr
import matplotlib.pyplot as plt

tickers = ["AAPL", "MSFT", "AMZN", "IBM", "FB"]

close_prices = pd.DataFrame()
attempt = 0
drop = []
while len(tickers) != 0 and attempt <= 5:
    tickers = [j for j in tickers if j not in drop]
    for i in range(len(tickers)):
        try:
            temp = pdr.get_data_yahoo(tickers[i], dt.date.today(
            )-dt.timedelta(3650), dt.date.today())
            temp.dropna(inplace=True)
            close_prices[tickers[i]] = temp["Adj Close"]
            drop.append(tickers[i])

        except:
            print(tickers[i], " :failed to fetch data...retrying")
            continue
    attempt += 1

# Handling NaN Values
# Replaces NaN values with the next valid value along the column
close_prices.fillna(method='bfill', axis=0, inplace=True)
# Deletes any row where NaN value exists
close_prices.dropna(how='any', axis=0, inplace=True)

# Mean, Median, Standard Deviation, daily return
close_prices.mean()  # prints mean stock price for each stock
close_prices.median()  # prints median stock price for each stock
close_prices.std()  # prints standard deviation of stock price for each stock

# Creates dataframe with daily return for each stock
daily_return = close_prices.pct_change()

daily_return.mean()  # prints mean daily return for each stock
daily_return.std()  # prints standard deviation of daily returns for each stock

# Rolling mean and standard deviation
daily_return.rolling(window=20).mean()  # simple moving average
daily_return.rolling(window=20).std()

daily_return.ewm(span=20, min_periods=20).mean()  # exponential moving average
daily_return.ewm(span=20, min_periods=20).std()

# Data vizualization
close_prices.plot()  # Plot of all the stocks superimposed on the same chart

cp_standardized = (close_prices - close_prices.mean()) / \
    close_prices.std()  # Standardization
# Plot of all the stocks standardized and superimposed on the same chart
cp_standardized.plot()

close_prices.plot(subplots=True, layout=(
    3, 2), title="Tech Stock Price Evolution", grid=True)  # Subplots of the stocks


# Pyplot demo
fig, ax = plt.subplots()
plt.style.available
plt.style.use('ggplot')
ax.set(title="Daily return on tech stocks",
       xlabel="Tech Stocks", ylabel="Daily Returns")
plt.bar(daily_return.columns, daily_return.mean())
plt.show()
