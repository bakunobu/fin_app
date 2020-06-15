import os
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

MY_URI = os.environ.get('MONGO_PATH')
# manual connection
my_client = MongoClient(MY_URI)

my_db = my_client['b52fldsjjhnxmaj']
my_col = my_db['test_app']

for record in my_col.find():
    print(record)