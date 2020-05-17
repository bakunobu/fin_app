from pymongo import MongoClient


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
