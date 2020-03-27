from sklearn.linear_model import LinearRegression
from sklearn import preprocessing, svm, model_selection
import numpy as np
import pandas as pd
import quandl
import math
import datetime
import matplotlib.pyplot as plt

from matplotlib import style

# API Key
quandl.ApiConfig.api_key = "SvQ-nHVssvdwaPU5sqtU"

# Get Specific Stock
quandl.get_table('FXCM/H1', date='2017-07-02', symbol='EUR/USD')

# Get Data Features
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
