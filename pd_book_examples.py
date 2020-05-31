import pandas as pd
import numpy as np
import numpy_financial as nf


loan = 3000
rate = 0.0575
term = 14

balance = loan

payment = np.round(-nf.pmt(rate / 12, term, loan), 2)


df = pd.DataFrame({
    'month': [0],
    'payment': [np.NaN],
    'interest': [np.NaN],
    'principal': [np.NaN],
    'balance': [balance] 
})

# print(df)


for i in range(1, term + 1):
    interest = round(rate / 12 * balance, 2)
    principal = payment - interest
    balance -= principal
    
    df = df.append(pd.DataFrame({'month': [i],
                                 'payment': [payment],
                                 'interest': [interest],
                                 'principal': [principal],
                                 'balance': [balance]}))


df = df.reset_index(drop=True)
print(df[['month', 'payment', 'interest', 'principal', 'balance']])