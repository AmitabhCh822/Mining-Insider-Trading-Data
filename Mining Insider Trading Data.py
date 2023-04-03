# Necessary Libraries.
import requests
import json
import pandas as pd
import numpy as np

# The stock symbol of Goldman Sachs is GS
stock = 'GS'

# Request for data from Finhub.io (30 calls per second limit: https://finnhub.io/docs/api/rate-limit).
r = requests.get('https://finnhub.io/api/v1/stock/insider-transactions?symbol='
                 +stock+'&token= Your API key')

# Load the JSON file as a string.
test = json.loads(r.text)

# Convert the data into a dataframe.
df = pd.DataFrame(data=test['data'])

# Derived attributes from the data.
df['dollarAmount'] = df['change']*df['transactionPrice']
df['insiderPortfolioChange'] = df['change']/(df['share'] - df['change'])

# print(type(df['transactionPrice'][0]))
conditions = [
    (df['change'] >= 0) & (df['transactionPrice'] > 0),
    (df['change'] <= 0) & (df['transactionPrice'] > 0),
    (df['transactionPrice'] == 0)
]
values = ['Buy', 'Sale', 'Gift']
df['buyOrSale'] = np.select(conditions, values)

print(df)

df.to_csv('Your Path\\'+stock+'.csv', index=False) 
