# -*- coding: utf-8 -*-
"""
Created on Thursday March 9 18:22:27 2023

@author: Amitabh Chakravorty
"""

import finnhub
import pandas as pd
import numpy as np

#Accessing the trading database
finnhub_client = finnhub.Client(api_key="USER'S KEY") #The user’s unique API key has to be entered

#The stock symbol of Tesla is TSLA
stock = 'TSLA'

#Insider Trading Data of April 1 2020 to March 31 2021
df1 = finnhub_client.stock_insider_transactions(stock, '2020-04-01', '2021-03-31')
#Insider Trading Data of April 1 2021 to March 31 2022
df2 = finnhub_client.stock_insider_transactions(stock, '2021-04-01', '2022-03-31')
#Insider Trading Data of April 1 2022 to March 31 2023
df3 = finnhub_client.stock_insider_transactions(stock, '2022-04-01', '2023-03-31')

#Converting the data into a dataframe
df11 = pd.DataFrame(data=df1['data'])
df22 = pd.DataFrame(data=df2['data'])
df33 = pd.DataFrame(data=df3['data'])

#Insider Trading Data of April 1 2020 to March 31 2023
df = pd.concat([df33,df22,df11])

#First derived attribute from the data
df['DollarVolume'] = df['change']*df['transactionPrice']

#Checking if the transaction is a buy, sale or a gift
conditions = [
    (df['change'] >= 0) & (df['transactionPrice'] > 0),
    (df['change'] <= 0) & (df['transactionPrice'] > 0),
    (df['transactionPrice'] == 0)
]
values = ['Buy', 'Sale', 'Gift']

#Second derived attribute from the data
df['Transaction Type'] = np.select(conditions, values)

#Removing the rows of Gift transactions 
df.drop(df[(df['Transaction Type'] == 'Gift')].index, inplace=True)

print(df)

#Saving the data in a CSV file
df.to_csv("User's Folder Path"+stock+".csv", index=False)
