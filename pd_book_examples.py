import pandas as pd
import numpy as np


loan = 3000

balance = loan


df = pd.DataFrame({
    'month': [0],
    'payment': [np.NaN],
    'interest': [np.NaN],
    'principal': [np.NaN],
    'balance': [balance] 
})

print(df)