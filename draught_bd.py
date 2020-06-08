import pandas as pd
import numpy as np
from pymongo import MongoClient


my_client = MongoClient('mongodb://localhost:27017/')

my_db = my_client['app_db']
my_col = my_db['budget']
my_dict = {'Title': 'booze',
           'Ammount': 99,
           'Date': pd.Timestamp.now(),
           'Comment': 'testing purpose'}

my_col.insert_one(my_dict)
print(my_client.list_database_names())