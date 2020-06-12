import datetime
import pandas as pd
import numpy as np
import pymongo
from pymongo import MongoClient
from bson import ObjectId


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

print(calendar.tail(10))