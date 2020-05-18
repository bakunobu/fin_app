from pymongo import MongoClient
from bson import ObjectId


def connect_to_db(conf):
    """
    Connects to a given DB and returns a DB object
    pymongo is required
    Args:
    =====
    conf: dictionary
    default values:
            - login: ''
            - password: ''
            - host: 'localhost'
            - port: 27017
            - database = ''
    

    Returns:
    ========
    db: pymongo.database.Database class object
    a database client to work with
    
    or prints 'Connection failed!' if it can't reach the server
    
    """
    
    login = conf.get('login', '')
    paswd = conf.get('paswd', '')
    host = conf.get('host', 'localhost')
    database = conf.get('database', '')
    port = conf.get('port', '27017')
    
    
    try:
        mongoURI = f'mongodb://{login}:{paswd}@{host}:{port}/{database}'
        client = MongoClient(mongoURI, connect=True)
        return(client[database])
    
    except:
        print('Connection failed!')

# an example

my_client = connect_to_db(my_config)


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


def update_record(collection, filt, new_data):
    '''
    Updates a document using .find_one_and_update()
    !!!needs import from bson library!!!
    
    Args:
    =====
    collection: pymongo.collection.Collection class
    a collection to work with
    filter: dict
    a parameter or a set of parameters to find a required document
    new_data: dict
    a new data to update a document with
    
    Returns:
    ========
    None: None type
    Doesn't return anything
    prints 'Document Updated!'
    '''
        collection.find_one_and_update(filt,
                                       {'$set': new_data})
        print('Document Updated!')
        

#an example

params =  {'_id': ObjectId("5ebbd583b40171c316ee330c")}
new_data = {'income': 9999}
update_record(collect, params, new_data)