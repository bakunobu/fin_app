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
my_client = MongoClient(MY_URI)

my_db = my_client['b52fldsjjhnxmaj']
my_col = my_db['test_app']

for record in my_col.find():
    print(record)