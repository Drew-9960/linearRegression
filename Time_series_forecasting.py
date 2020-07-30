# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 16:19:44 2020

@author: melen
"""
################## Time Series Forecasting ###################### 

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

pd.set_option('display.max_columns', 30)
data = pd.read_excel('elec_time.xlsx', parse_dates = [0])
data.set_index('Billing Start Date', inplace=True)
data = data[['Total usage']]
data.dtypes
data.dropna(how='all', inplace=True)
data = data[data['Total usage'] >= 1]
data.dtypes
data.dropna(how='all', inplace=True)
data.columns
data.shape
data.head()

type(data)
series_value = data.values
type(series_value)

data.size
data.tail()

data.describe(include = 'all')
data = data[:58031]

data.plot()

data_mean = data.rolling(window = 100).mean()


data.plot()
data_mean.plot()

#identifying outliars 
import seaborn as sns
sns.boxplot(x=data['Total usage'])


data = data[data['Total usage'] <= 40000]




#building the model (Naive Model)
val = pd.DataFrame(series_value)
df = pd.concat([val, val.shift(1)], axis = 1)
df = df[1:564468]
df.shape

df.head()
df.columns = ['Actual_output', 'Forecasted_output']
df1 = df[1:564468]
df1.head()
df1.tail()
df1.isna().sum()



from sklearn.metrics import mean_squared_error
df_error = mean_squared_error(df1.Actual_output, df1.Forecasted_output)
np.sqrt(df_error)

#ARIMA - Autoregressive (p) Integrated (d) Moving Average (q)
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

plot_acf(data)
plot_pacf(data)



# p = 2,3,  d=0,  q=2,3

data.size
df_train = data[0:50000]
df_test = data[50000:56468]

df_train.size
df_test.size

from statsmodels.tsa.arima_model import ARIMA
df_model = ARIMA(df_train, order=(2,1,2))
df_fit = df_model.fit()

df_fit.aic

df_forecast = df_fit.forecast(steps = 40)[0]
df_forecast

df_test.head()

np.sqrt(mean_squared_error(df_test, df_forecast))







