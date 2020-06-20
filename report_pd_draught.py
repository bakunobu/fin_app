from bson import ObjectId
import datetime
from dateutil import rrule
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pymongo
from pymongo import MongoClient
from recurrent import RecurringEvent



TODAY = pd.Timestamp(2020, 6, 11)
END = TODAY + datetime.timedelta(days=365)


calendar = pd.DataFrame(index=pd.date_range(start=TODAY, end=END))

income = pd.DataFrame(
    data={'income': 15000},
    index=pd.date_range(start=TODAY, end=END, freq='MS')
)

mortgage = pd.DataFrame(
    data={'rent': -5000},
    index=pd.date_range(start=TODAY, end=END, freq='M') + datetime.timedelta(days=15)
)

calendar = pd.concat([calendar, income], axis=1).fillna(0)
calendar = pd.concat([calendar, mortgage], axis=1).fillna(0)


calendar['total'] = calendar.sum(axis=1)
calendar['cum_total'] = calendar['total'].cumsum()


"""
plt.figure(figsize=(10, 5))
plt.plot(calendar.index, calendar.total, label='Daily Total')
plt.plot(calendar.index, calendar.cum_total, label = 'Cumulative Total')
plt.legend()
plt.show()
"""

def update_totals(df):
    
    if df.columns.isin(['total', 'cum_total']).any():
        df['total'] = 0
        df['cum_total'] = 0
    df['total'] = df.sum(axis=1)
    df['cum_total'] = df['total'].cumsum()
    
    return(df)


def plot_budget(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df.total, label='Daily Total')
    plt.plot(df.index, df.cum_total, label='Cumulative Total')
    plt.legend()
    plt.show()
    

def get_dates(frequency):
    try:
        return(pd.Timestamp(frequency).normalize())
    except ValueError:
        pass
    
    try:
        r = RecurringEvent()
        r.parse(frequency)
        rr = rrule.rrulestr(r.get_RFC_rrule())
        return([pd.to_datetime(date).normalize()
                for date in rr.between(TODAY, END)])
    except ValueError as e:
        raise ValueError('Invalid Frequency')
    

def add_saving(saving, date=pd.Timestamp().today().normalize(), df):
    '''
    '''
    spending = -saving
    DATE = date
    data = {'Saving': saving,
            'Spending': spending,
            'Balance': df['Saving'].sum(axis=0) + saving,
            'Date': date}
    df.append(data)
    return(df)