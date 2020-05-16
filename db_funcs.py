from pymongo import MongoClient


def connect_to_db(log, passwd, host, d_base):
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


    Returns:
    ========
    client: pymongo.database.MongoClient class object
    a database client to work with
    """
    client = MongoClient(f"mongodb://{log}:{passwd}@{host}/{d_base}")
    
    return(client)

# an example

my_client = connect_to_db(log, passwd, host, d_base)

db = my_client.d_base


