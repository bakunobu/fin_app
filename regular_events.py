import datetime
import numpy as np
import pandas as pd
import pprint
import pymongo
from bson import ObjectId
from pymongo import MongoClient


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

# testing
'''
initiate_collection('spending_DB', 'reg_spend', record=reg_record)
'''

reg_records = [{'Description': 'salary',
                'Amount': 15000.0,
                'Date': pd.Timestamp(2020, 1, 12).normalize(),
                'Tags': ['testing', 'salary'],
                'Regular': 'YES',
                'Starts': pd.Timestamp(2020, 1, 12).normalize(),
                'ENDS': pd.Timestamp(2020, 12, 31).normalize(),
                'Period': 'M',
                'Shift': 12,
                'Source': 'cash',
                'comments': 'just testing'},
               {'Description': 'mortgage',
                'Amount': -5000.0,
                'Date': pd.Timestamp(2020, 1, 12).normalize(),
                'Tags': ['testing', 'mortgage'],
                'Regular': 'YES',
                'Starts': pd.Timestamp(2020, 1, 12).normalize(),
                'ENDS': pd.Timestamp(2027, 8, 16).normalize(),
                'Period': 'M',
                'Shift': 10,
                'Source': 'bank acc.',
                'comments': 'just testing'},
               {'Description': 'gas',
                'Amount': -1000.0,
                'Date': pd.Timestamp(2020, 1, 12).normalize(),
                'Tags': ['testing', 'salary'],
                'Regular': 'YES',
                'Starts': pd.Timestamp(2020, 1, 12).normalize(),
                'ENDS': pd.Timestamp(2020, 12, 31).normalize(),
                'Period': 'Q',
                'Shift': 15,
                'Source': 'card',
                'comments': 'just testing'},
               {'Description': 'commodities',
                'Amount': -100.0,
                'Date': pd.Timestamp(2020, 1, 12).normalize(),
                'Tags': ['testing', 'commodities'],
                'Regular': 'YES',
                'Starts': pd.Timestamp(2020, 1, 12).normalize(),
                'ENDS': pd.Timestamp(2020, 12, 31).normalize(),
                'Period': 'M',
                'Shift': 16,
                'Source': 'card',
                'comments': 'just testing'},
               {'Description': 'internet+phone',
                'Amount': -25.0,
                'Date': pd.Timestamp(2020, 1, 12).normalize(),
                'Tags': ['testing', 'communication'],
                'Regular': 'YES',
                'Starts': pd.Timestamp(2020, 1, 12).normalize(),
                'ENDS': pd.Timestamp(2020, 12, 31).normalize(),
                'Period': 'M',
                'Shift': 6,
                'Source': 'card',
                'comments': 'just testing'},
               {'Description': 'Photoshop',
                'Amount': -6.0,
                'Date': pd.Timestamp(2020, 1, 12).normalize(),
                'Tags': ['testing', 'subscription'],
                'Regular': 'YES',
                'Starts': pd.Timestamp(2020, 1, 12).normalize(),
                'ENDS': pd.Timestamp(2020, 12, 31).normalize(),
                'Period': 'M',
                'Shift': 6,
                'Source': 'card',
                'comments': 'just testing'},
               {'Description': 'packt',
                'Amount': -7.0,
                'Date': pd.Timestamp(2020, 1, 12).normalize(),
                'Tags': ['testing', 'subscription'],
                'Regular': 'YES',
                'Starts': pd.Timestamp(2020, 1, 12).normalize(),
                'ENDS': pd.Timestamp(2020, 12, 31).normalize(),
                'Period': 'M',
                'Shift': 26,
                'Source': 'card',
                'comments': 'just testing'},
               {'Description': 'boiler service',
                'Amount': -100.0,
                'Date': pd.Timestamp(2020, 1, 12).normalize(),
                'Tags': ['testing', 'commodities'],
                'Regular': 'YES',
                'Starts': pd.Timestamp(2020, 1, 12).normalize(),
                'ENDS': pd.Timestamp(2020, 12, 31).normalize(),
                'Period': 'Y',
                'Shift': 200,
                'Source': 'card',
                'comments': 'just testing'},
               {'Description': 'kindergarden',
                'Amount': -200.0,
                'Date': pd.Timestamp(2020, 1, 12).normalize(),
                'Tags': ['testing', 'services'],
                'Regular': 'YES',
                'Starts': pd.Timestamp(2020, 1, 12).normalize(),
                'ENDS': pd.Timestamp(2020, 12, 31).normalize(),
                'Period': 'M',
                'Shift': 27,
                'Source': 'bank acc.',
                'comments': 'just testing'},
               {'Description': 'fees',
                'Amount': -40.0,
                'Date': pd.Timestamp(2020, 1, 12).normalize(),
                'Tags': ['testing', 'salary'],
                'Regular': 'YES',
                'Starts': pd.Timestamp(2020, 1, 12).normalize(),
                'ENDS': pd.Timestamp(2020, 12, 31).normalize(),
                'Period': 'Y',
                'Shift': 90,
                'Source': 'bank acc.',
                'comments': 'just testing'}]


# testing
'''
my_client = test_connection()
my_db = my_client['spending_DB']
my_col = my_db['reg_spend']
my_col.insert_many(reg_records)
'''

# adding spending manually

my_client = test_connection()
my_db = my_client['spending_DB']
my_col = my_db['reg_spend']

# search for outdated documents
TODAY = pd.Timestamp(2020, 1, 13).normalize()
'''
for record in my_col.find({'ENDS': {'$gte': TODAY}}):
    pprint.pprint(record)
'''

my_col.insert_one({'Description': 'test',
                'Amount': -4000.0,
                'Date': pd.Timestamp(2020, 1, 1).normalize(),
                'Tags': ['testing', 'test'],
                'Regular': 'YES',
                'Starts': pd.Timestamp(2020, 1, 1).normalize(),
                'ENDS': pd.Timestamp(2020, 1, 12).normalize(),
                'Period': 'M',
                'Shift': 12,
                'Source': 'cash',
                'comments': 'just testing'})


CHECK_DATE = pd.Timestamp(2020, 2, 12).normalize()

def del_outdated(my_col, CHECK_DATE):
    '''
    Deletes outdated records
    !!!pprint import required!!!
    
    
    Args:
    =====
    my_col: PyMongo collection obj.
    a collection to be modified
    
    CHECK_DATE: pd.Timestamp obj.
    All the documents that expire BEFORE ('<', '$lt') this date will be deleted.
    
    
    Returns:
    ========
    None: None type
    prints all the deleted docs
    '''
    
    for record in my_col.find({'ENDS': {'$lt': CHECK_DATE}}):
        pprint.pprint(record)
        my_col.delete_one(record)

spending_col = my_db['single_purch']

# generate data sequence
def update_reg_payments(my_col, spending_col, CHECK_DATE):
    '''
    add regular payments up to the given date to a single spending collection
    
    Args:
    my_col: pymongo collection obj.
    a collection with regular spendings
    
    spending_col: pymongo collection obj.
    a collection where all the spendings are being aggregated
    
    CHECK_DATE: pd.Timestamp() obj.
    a date that all the records must be up to
    
    Returns:
    None: None type
    Modifies the initial collection (spending_col)
    
    '''
    for record in my_col.find():
        paydays = pd.Series(
            pd.date_range(start= record.get('Starts', TODAY),
                        end=record.get('ENDS', TODAY),
                        freq=record.get('Period', 'M')) + datetime.timedelta(days=record.get('Shift', 0)))
        if paydays.isin([CHECK_DATE]).any():
            spending_col.insert_one({'Description': record.get('Description', np.NaN),
            'Amount': record.get('Amount', np.NaN),
            'Date': CHECK_DATE,
            'Tags': record.get('Tags', np.NaN),
            'Regular': 'YES',
            'Source': record.get('Source', np.NaN),
            'comments': record.get('comments', np.NaN)})