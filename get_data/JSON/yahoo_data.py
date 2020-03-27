from sklearn.linear_model import LinearRegression
from sklearn import preprocessing, svm, model_selection
import numpy as np
import pandas as pd
import math
import datetime
import matplotlib.pyplot as plt
from matplotlib import style
import pandas_datareader.data as pdr



# ticker = "AMZN"
# start_date = datetime.date.today() - datetime.timedelta(365)
# end_date = datetime.date.today()
# print(end_date)
# print(start_date)

# data = pdr.get_data_yahoo(ticker, start_date, end_date, interval='m')
# print(data)

tickers = ["ASIANPAINT.NS", "ADANIPORTS.NS", "AXISBANK.NS", "BAJAJ-AUTO.NS",
           "BAJFINANCE.NS", "BAJAJFINSV.NS", "BPCL.NS", "BHARTIARTL.NS",
           "INFRATEL.NS", "CIPLA.NS", "COALINDIA.NS", "DRREDDY.NS", "EICHERMOT.NS",
           "GAIL.NS", "GRASIM.NS", "HCLTECH.NS", "HDFCBANK.NS", "HEROMOTOCO.NS",
           "HINDALCO.NS", "HINDPETRO.NS", "HINDUNILVR.NS", "HDFC.NS", "ITC.NS",
           "ICICIBANK.NS", "IBULHSGFIN.NS", "IOC.NS", "INDUSINDBK.NS", "INFY.NS",
           "KOTAKBANK.NS", "LT.NS", "LUPIN.NS", "M&M.NS", "MARUTI.NS", "NTPC.NS",
           "ONGC.NS", "POWERGRID.NS", "RELIANCE.NS", "SBIN.NS", "SUNPHARMA.NS",
           "TCS.NS", "TATAMOTORS.NS", "TATASTEEL.NS", "TECHM.NS", "TITAN.NS",
           "UPL.NS", "ULTRACEMCO.NS", "VEDL.NS", "WIPRO.NS", "YESBANK.NS", "ZEEL.NS"]

stock_cp = pd.DataFrame()  # dataframe to store close price of each ticker
attempt = 0  # initializing passthrough variable
drop = []  # initializing list to store tickers whose close price was successfully extracted
while len(tickers) != 0 and attempt <= 5:
    # removing stocks whose data has been extracted from the ticker list
    tickers = [j for j in tickers if j not in drop]
    for i in range(len(tickers)):
        try:
            temp = pdr.get_data_yahoo(tickers[i], datetime.date.today(
            )-datetime.timedelta(1095), datetime.date.today())
            temp.dropna(inplace=True)
            stock_cp[tickers[i]] = temp["Adj Close"]
            drop.append(tickers[i])
            print(f"${drop[i]} : ${stock_cp}")
        except:
            print(tickers[i], " :failed to fetch data...retrying")
            continue
    attempt += 1
