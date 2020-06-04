from pymongo import MongoClient
from bson import ObjectId
import pandas as pd
import datetime


def add_revenue(source='salary', amt=0, date=datetime.datetime.now(), comment=''):
    '''
    Writes down revenue. Packs all the values into a dict of a given structure
    (converts a date into pd.Timestamp() object)
    pandas and datetime modules are required
    
    Args:
    =====
    sourse: str
    a sourse of revenue ('salary' is a default option)
    
    amt: int or float
    an ammount of money (0 is a default value)
    
    date: str or datetime.datetime object
    a date (and time) a revenue was received (datetime.daetime.now() is a default value)
    
    comment: str
    any comment (a blank field is a default)
    
    Returns:
    my_dict: dict
    the structure of the tictionary is:
    {
    'source': 'source',
    'ammount': ammount,
    'date': Timestamp(data),
    'comment': 'comment}
    }
    
    
    '''
    
    return{'source': source,
           'ammount': amt,
           'date': pd.Timestamp(date),
           'comment': comment}


# testing
print(add_revenue(source='bonus', amt=100, date='21.12.2019', comment='yearly bonus'))