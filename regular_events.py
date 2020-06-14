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
def initiate_collection(DB_NAME, COL_NAME, record=record):
    '''
    testing inititating func (reating a DB and a collection)
    
    EDITED:
    
    Args:
    =====
    DB_NAME: str
    a database name
    
    COL_NAME: str
    a collection name
    
    record: dict
    a document to initialize DB/collection
    
    Returns:
    ========
    None: None type
    prints the document's ID
    '''
    my_client = test_connection()
    my_db = my_client[DB_NAME]
    my_col = my_db[COL_NAME]
    record_id = my_col.insert_one(record).inserted_id
    print(record_id)

# testing
'''
initiate_collection('my_db', 'my_col')
'''

# creating another DB for regular spendings

# an initiating record

reg_date = pd.Timestamp(2020, 1, 1).normalize()

reg_record = {'Description': 'charity',
          'Amount': 10.0,
          'Date': reg_date,
          'Tags': ['testing', 'charity'],
          'Regular': 'YES',
          'Starts': reg_date,
          'ENDS': pd.Timestamp(2020, 12, 31).normalize(),
          'Period': 'MS',
          'Source': 'card',
          'comments': 'just testing'}

initiate_collection('spending_DB', 'reg_spend', record=reg_record)


