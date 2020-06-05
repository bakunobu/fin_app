import os
from dotenv import load_dotenv, find_dotenv
from db_funcs import connect_to_db


load_dotenv(find_dotenv())


MY_LOG = os.environ.get('MONGO_LOG')
MY_PASS = os.environ.get('MONGO_PASS')
MY_SERVER = os.environ.get('MONGO_SERVER')
MY_DB = os.environ.get('MONGO_DB')


my_config = {'login': MY_LOG,
'paswd': MY_PASS,
'host': MY_SERVER,
'database': MY_DB}


my_client = connect_to_db(my_config)
print(type(my_client))