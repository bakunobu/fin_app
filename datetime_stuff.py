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
    'comment': 'comment'
    }
    
    
    '''
    
    return{'source': source,
           'ammount': amt,
           'date': pd.Timestamp(date),
           'comment': comment}


# testing
# print(add_revenue(source='bonus', amt=100, date='21.12.2019', comment='yearly bonus'))

def add_spending(source='booze', amt=0, date=datetime.datetime.now(), comment=''):
    '''
    Writes down spending. Packs all the values into a dict of a given structure
    (converts a date into pd.Timestamp() object)
    pandas and datetime modules are required
    
    Args:
    =====
    sourse: str
    a sourse of revenue ('booze' is a default option)
    
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
    'comment': 'comment'
    }
    
    
    '''
    
    return{'source': source,
           'ammount': amt,
           'date': pd.Timestamp(date),
           'comment': comment}
    
    
# testing
#  print(add_spending(source='transport', amt=100, date='21.12.2019', comment='one-way ticket'))


def add_reg_revenue(source='salary', amt=0, date=datetime.datetime.now(), freq='M', comment=''):
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
    
    freq: str
    frequncy of revenue gaining(a month ('M') is for default)
    
    comment: str
    any comment (a blank field is a default)
    
    Returns:
    my_dict: dict
    the structure of the tictionary is:
    {
    'source': 'source',
    'ammount': ammount,
    'date': Timestamp(data),
    'frequency': 'frequency'
    'comment': 'comment'
    }
    
    
    '''
    
    return{'source': source,
           'ammount': amt,
           'date': pd.Timestamp(date),
           'frequency': freq,
           'comment': comment}


# testing
#  print(add_reg_revenue(source='salary', amt=100, date='21.12.2019', freq='M', comment='yearly bonus'))


def add_reg_spending(source='salary', amt=0, date=datetime.datetime.now(), freq='M', dur=365, comment=''):
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
    
    freq: str
    frequncy of revenue gaining(a month ('M') is for default)
    
    dur:int
    a duration of spending (a year (365 days) is a default value)
    
    comment: str
    any comment (a blank field is a default)
    
    Returns:
    my_dict: dict
    the structure of the tictionary is:
    {
    'source': 'source',
    'ammount': ammount,
    'date': Timestamp(data),
    'frequency': 'frequency'
    'duration': duration,
    'comment': 'comment'
    }
    
    
    '''
    
    return{'source': source,
           'ammount': amt,
           'date': pd.Timestamp(date),
           'frequency': freq,
           'duration': dur,
           'comment': comment}


# testing
print(add_reg_spending())