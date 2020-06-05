import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

MY_LOG = os.environ.get('MONGO_LOG')
MY_PASS = os.environ.get('MONGO_PASS')

print(MY_LOG, MY_PASS)
