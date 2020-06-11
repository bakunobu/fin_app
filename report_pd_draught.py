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

print(mortgage.head())
