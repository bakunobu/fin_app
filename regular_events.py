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




# create a new DB with a new collection (with a single document)