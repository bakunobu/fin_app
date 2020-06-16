import os
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

def generate_path():
    prefix = 'mongodb://'
    LOG = os.environ.get('MY_LOG')
    PAS = os.environ.get('MY_PAS')
    HOST = os.environ.get('MY_HOST')
    PORT = os.environ.get('MY_PORT')
    DB = os.environ.get('MY_DB')
    return(f'{prefix}{LOG}:{PAS}@{HOST}:{PORT}/{DB}')


# MY_URI = os.environ.get('MONGO_PATH')
MY_URI = generate_path()
# manual connection
# my_client = MongoClient(MY_URI)


def connect_to_server():
    '''
    quick connect to the remote server using  generate_path() func
    '''
    PATH = generate_path()
    return(MongoClient(PATH))


def connect_to_db(DB):
    '''
    quick connect to the DB using  generate_path() and
    connect_to_server() func
    '''
    my_client = connect_to_server()
    return(my_client[DB])

my_db = connect_to_db('b52fldsjjhnxmaj')
my_col = my_db['test_app']

for record in my_col.find():
    print(record)
