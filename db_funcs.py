from pymongo import MongoClient


def connect_to_db(log, passwd, host, d_base, port='27017'):
    """
    Connects to a given DB and returns a DB object
    pymongo is required
    Args:
    =====
    log: str
    a db login

    passwd: str
    a db pass

    server: str
    a server's name

    d_base: str
    a db name
    
    port:str
    by default - 27017, but can be adjusted
    

    Returns:
    ========
    client: pymongo.mongo_client.MongoClient class object
    a database client to work with
    """
    client = MongoClient(f"mongodb://{log}:{passwd}@{host}:{port}/{d_base}")
    
    return(client)

# an example

my_client = connect_to_db(log, passwd, host, d_base)

db = my_client.d_base


def add_doc(collection, doc):
    '''
    Adds a document to the collection
    
    Args:
    =====
    collection: pymongo.database.Database class object
    a coolection to work with
    doc: dict class object
    contains all the data to be added as a document
    
    Returns:
    ========
    None: None type
    prints 'Added!'
    '''
    collection.insert_one(doc)
    print('Added!')
    

# an example
test_doc = {
    'date':'2027-01-01',
    'income': 0,
    'expenses': -3000
    }

add_doc(test_db, test_doc)
