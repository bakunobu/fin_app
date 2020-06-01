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


# creating a DF using iterative for loop

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
#print(df[['month', 'payment', 'interest', 'principal', 'balance']])

# creating a DF using prebuild mode
balance = loan
index = list(range(term + 1))
columns = ['month', 'payment', 'interest', 'principal', 'balance']
df2 = pd.DataFrame(index=index, columns=columns)

df2.iloc[0]['month'] = 0
df2.iloc[0]['balance'] = balance


for i in range(1, term + 1):
    interest = round(rate / 12 * balance, 2)
    principal = payment - interest
    balance -= principal
    
    df2.iloc[i]['month'] = i
    df2.iloc[i]['payment'] = payment
    df2.iloc[i]['interest'] = interest
    df2.iloc[i]['principal'] = principal
    df2.iloc[i]['balance'] = balance


#print(df2[['month', 'payment', 'interest', 'principal', 'balance']])


# amort func
def amort(loan, rate, term):
    payment = np.round(-nf.pmt(rate / 12, term, loan), 2)
    balance = loan
    index = list(range(term + 1))
    columns = ['month', 'payment', 'interest', 'principal', 'balance']
    df = pd.DataFrame(index=index, columns=columns)
    
    df.iloc[0]['month'] = 0
    df.iloc[0]['balance'] = balance
    
    for i in range(1, term + 1):
        interest = round(rate / 12 * balance, 2)
        principal = payment - interest
        balance -= principal
    
        df.iloc[i]['month'] = i
        df.iloc[i]['payment'] = payment
        df.iloc[i]['interest'] = interest
        df.iloc[i]['principal'] = principal
        df.iloc[i]['balance'] = balance
    
    return(df)




# testing
bank_a = amort(loan, 0.0399, 20)
print(bank_a)


#  amort func 2
def amort_cicle(loan, rate, term):
    payment = np.round(-nf.pmt(rate / 12, term, loan), 2)
    balance = loan
    df = pd.DataFrame({'month': [0],
                       'payment': [np.NaN],
                       'interest': [np.NaN],
                       'principal': [np.NaN],
                       'balance': [balance]})
    
    
    for i in range(1, term + 1):
        interest = round(rate / 12 * balance, 2)
        principal = payment - interest
        balance -= principal
    
        df = df.append(pd.DataFrame({'month': [i],
                                 'payment': [payment],
                                 'interest': [interest],
                                 'principal': [principal],
                                 'balance': [balance]}))
        
    return(df)
    

#  testing
bank_b= amort_cicle(loan, 0.0399, 20)
print(bank_b)