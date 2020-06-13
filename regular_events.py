import pandas as pd
import numpy as np
import pymongo
from pymongo import MongoClient
from bson import ObjectId


# connect to DB
def test_connection():
    """
    a simple func for testing
    
    will be etit with some connection options
    """
    my_client = MongoClient('mongodb://localhost:27017/')
    return(my_client)


# create the first test score to start a new collection
date = pd.Timestamp(2020, 1, 1).normalize()

record = {'Description': 'A New Years\'s test spending',
          'Amount': 100.0,
          'Date': date,
          'Tags': ['testing', 'gifts'],
          'Regular': 'NO',
          'Source': 'cash',
          'comments': 'just testing'}


# create a new DB with a new collection (with a single document)
def initiate_collection(record=record):
    '''
    testing inititating func (reating a DB and a collection)
    '''
    my_client = test_connection()
    my_db = my_client['spending_DB']
    my_col = my_db['single_purch']
    record_id = my_col.insert_one(record).inserted_id
    print(record_id)

# testing

initiate_collection()