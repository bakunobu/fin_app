from pymongo import MongoClient


# manual connection
my_client = MongoClient('mongodb://uy2f3ugdkqyndqenqfaz:cvId7Wt84S7XIScyGVkc@b52fldsjjhnxmaj-mongodb.services.clever-cloud.com:27017/b52fldsjjhnxmaj')

my_db = my_client['b52fldsjjhnxmaj']
my_col = my_db['test_app']

for record in my_col.find():
    print(record)