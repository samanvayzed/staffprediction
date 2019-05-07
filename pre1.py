#!/anaconda3/bin/python3
import datetime
import time
import pandas as pd
import os
import sys 
import numpy as np

pd.set_option('display.max_rows', 2000)
pd.set_option('display.float_format', lambda x: '%.3f' % x)


services = pd.read_csv('/Users/samanvay/zed/sales_pred/mysql_data/note_services.csv', names=['eid', 'date','sales'])
services = services.iloc[1:]
#print(services)
services['sales'] = pd.to_numeric(services['sales'],errors='coerce')
Total = services['sales'].sum()
print(Total)
sys.exit()


df_temp = pd.concat([products,tickets],ignore_index=True)
df = pd.concat([df_temp,services],ignore_index=True)
df.sort_values(by=['eid','date'])

df = df.dropna()
df = df.reset_index()
print(df)

sys.exit()



print(df.dtypes)
df['date'] = pd.to_datetime(df['date'])
#df[["sales"]] = df[["sales"]].apply(pd.to_numeric)

df['sales'] = pd.to_numeric(df['sales'],errors='coerce')
#df = df.astype({"sales": int})

print(df.dtypes)

df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df = df[['eid', 'month', 'year', 'sales', 'date']]


#df.sales = df.sales.astype(int)
#df[['sales']] = df[['sales']].apply(pd.to_numeric)
sum = df.groupby(['eid','month','year'])['sales'].sum().reset_index()
print(sum)

sys.exit()

df['date'] = df['date'].astype(str)

epoch_time = []

for row in products['Date']:
        dt = datetime.datetime.strptime(row, "%Y-%m-%d")
        #print(dt)
        unix_time = time.mktime(dt.timetuple())
        epoch_time.append(unix_time)

products['Epoch Time'] = epoch_time

#print(products)

feature_cols = ['User ID', 'Epoch Time', 'Sales']

 

x = products.loc[:, feature_cols]

#print(x)

x.to_csv('data.csv', encoding='utf-8', index=False)


