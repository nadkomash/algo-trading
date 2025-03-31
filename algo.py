
import pandas_datareader as web
import matplotlib as plt
import statsmodels.api as sm
import pandas as pd
import numpy as np
import datetime as dt
import yfinance as yf
import warnings
warnings.filterwarnings('ignore')


sp500 = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
sp500['Symbol'] = sp500['Symbol'].str.replace('.', '-')


symbols_list = sp500['Symbol'].unique().tolist()
print (symbols_list)
print ('='*20)
end_date = '2025-03-30' 
start_date = pd.to_datetime(end_date)-pd.DateOffset(10)

df = yf.download( tickers = symbols_list , start = start_date , end = end_date ).stack()
df.index.names=['date','ticker']
df.columns = df.columns.str.lower()
print(df)
print ('='*20)
 

df['garman_klass_vol']= ((np.log(df['high'])-np.log(df['low']))**2)/2-(2*np.log(2)-1)*((np.log(df['adj close'])-np.log(df['open']))**2)
print(df)