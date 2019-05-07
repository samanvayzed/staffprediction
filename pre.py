#!/anaconda3/bin/python3

import datetime
import time
import pandas as pd
import os
import sys 
import numpy as np

pd.set_option('display.max_rows', 2000)
pd.set_option('display.float_format', lambda x: '%.3f' % x)


#my_date_str = "2016-05-01"
#dt = datetime.datetime.strptime(my_date_str, "%Y-%m-%d")
#print(dt)

#unix_time = time.mktime(dt.timetuple())

products = pd.read_csv('/Users/samanvay/zed/sales_pred/mysql_data/note_products.csv', names=['eid', 'date','sales'], na_values=" NaN")
products = products.iloc[1:]
#print(products)

tickets = pd.read_csv('/Users/samanvay/zed/sales_pred/mysql_data/note_tickets.csv', names=['eid', 'date','sales'],na_values=" NaN")
tickets = tickets.iloc[1:]
#print(tickets)

services = pd.read_csv('/Users/samanvay/zed/sales_pred/mysql_data/note_services.csv', names=['eid', 'date','sales'],na_values=" NaN")
services = services.iloc[1:]
#print(services)


df_temp = pd.concat([products,tickets],ignore_index=True)
df = pd.concat([df_temp,services],ignore_index=True)
#print(df)


df.sort_values(by=['eid','date'])

df = df.dropna()
#df = df[df.sales != 0]
#print(df)

############################################################
# CODE TO VERIFY THAT THE DATA PICKED UP BY MYSQL IS CORRECT
#############################################################

#print(df.dtypes)
#df['date'] = pd.to_datetime(df['date'])
#df['sales'] = pd.to_numeric(df['sales'],errors='coerce')
#print(df.dtypes)

#df['year'] = df['date'].dt.year
#df['month'] = df['date'].dt.month
#df = df[['eid', 'month', 'year', 'sales', 'date']]
#sum = df.groupby(['eid','month','year'])['sales'].sum().reset_index()
#print(sum)
#sys.exit()

#######################################################################

df['date'] = df['date'].astype(str)

epoch_time = []

for row in df['date']:
        dt = datetime.datetime.strptime(row, "%Y-%m-%d")
        #print(dt)
        unix_time = time.mktime(dt.timetuple())
        epoch_time.append(unix_time)



df['epochtime'] = epoch_time

print(df)



feature_cols = ['eid', 'epochtime', 'sales']

x = df.loc[:, feature_cols]

print(x)

x.to_csv('data.csv', encoding='utf-8', index=False)


