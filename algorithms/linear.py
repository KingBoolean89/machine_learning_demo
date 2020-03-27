from sklearn.linear_model import LinearRegression
from sklearn import preprocessing, svm, model_selection
import numpy as np
import pandas as pd
import quandl
import math
import datetime
import matplotlib.pyplot as plt
import pickle
from matplotlib import style
import pandas_datareader.data as pdr
import yfinance as yf


ticker = "AMZN"
start_date = datetime.date.today() - datetime.timedelta(365)
end_date = datetime.date.today()
print(end_date)
print(start_date)

data = pdr.get_data_yahoo(ticker, start_date, end_date, interval='m')
print(data)
style.use('ggplot')

# API Key
quandl.ApiConfig.api_key = "SvQ-nHVssvdwaPU5sqtU"
# Get Specific Stock with Quandl
df = quandl.get('WIKI/GOOGL')
# Get Data Features
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
# Get High and Low Percentage
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100
# Get Percentage change
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / \
    df['Adj. Open'] * 100
# Get Updated Features
df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

forecast_col = 'Adj. Close'
# Handle NAN(not a number)
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.01*len(df)))

# Create Labels and Shifting Column
df['label'] = df[forecast_col].shift(-forecast_out)

x = np.array(df.drop(['label'], 1))
x = preprocessing.scale(x)
x = x[:-forecast_out]
x_lately = x[-forecast_out:]

df.dropna(inplace=True)
y = np.array(df['label'])
y = np.array(df['label'])

x_train, x_test, y_train, y_test = model_selection.train_test_split(
    x, y, test_size=0.2)
# Create classifier
# clf = LinearRegression(n_jobs=-1)
# Train classifier
# clf.fit(x_train, y_train)
# Save Classifier
# with open('linearregression.pickle', 'wb') as f:
#     pickle.dump(clf, f)
# Use Classifier
pickle_in = open('linearregression.pickle', 'rb')
clf = pickle.load(pickle_in)
# Test Classifier
accuracy = clf.score(x_test, y_test)

forecast_set = clf.predict(x_lately)
print(forecast_set, accuracy, forecast_out)

df['Forecast'] = np.nan

last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]

df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
# plt.show()
