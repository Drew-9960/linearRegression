# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 16:23:01 2020

@author: melen
"""


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

from sqlalchemy import delete 
import seaborn as sb
from collections import Counter

pd.set_option('display.max_columns', 30)


df_data = pd.read_excel('utilitydata13-14.xls')
df_data1 = pd.read_excel('utilitydata14-15.xls')
df_data2 = pd.read_excel('utilitydata15-16.xls')
df_udata = pd.read_excel('utilitydata16-17.xls')
df_udata1 = pd.read_excel('utilitydata17-18.xls')
df_udata2 = pd.read_excel('utilitydata18-19.xls')

data_all = pd.concat([df_data, df_data1, df_data2, df_udata, df_udata1, df_udata2])


#exploring dataframe 
data_all.columns
data_all.info()
data_all.head()
data_all.describe()
data_all.describe(include= 'all')

data_all.replace(np.nan, 0)

#setting parks to index to run an analysis
data_all.dropna(subset = ['Park'], inplace=True)
data_all.set_index('Park')
data_all.sort_values(['Utility Bill Amt'], ascending = True, axis=0, inplace=True)

#binning for frequency prices in a categorical format
data_all.columns
bins = np.linspace(min(data_all['Utility Bill Amt']), max(data_all['Utility Bill Amt']),4)
group_names = ['low', 'medium', 'high']
data_all['utility bill binned'] = pd.cut(data_all['Utility Bill Amt'], bins, labels=group_names, include_lowest=True)
data_all['utility bill binned'].dropna(inplace=True)

pd.value_counts(data_all['utility bill binned'])

data_all['utility bill binned'].hist(bins=20)
plt.show()

