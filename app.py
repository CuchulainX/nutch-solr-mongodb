from urllib.request import urlopen
import urllib
import json
import datetime
import time
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

auth = json.loads(open('auth.json').read())

USERNAME = auth["user"]
PASSWORD = auth["password"]
URL = "http://solr:8983/solr/nutch/select?indent=true&q.op=OR&q=*%3A*&useParams="
DATABASE = "nutch"
COLLECTION = "nutch"

uri = "mongodb+srv://" + USERNAME + ":" + PASSWORD + "@sandbox.zepml.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


if DATABASE in client.list_database_names():
    db = client[DATABASE]
    collection = db[COLLECTION]
    print("Database already exists")
else:
    print("Creating database")
    db = client[DATABASE]
    db.create_collection(COLLECTION)
    collection = db[COLLECTION]
    print("Database created")

while True:
    time.sleep(30)
    try:
        print('Trying to connect to Solr')
        response = urlopen(URL)
        if response.getcode() == 200:
            print('Successfully connected to Solr')
            data_json = json.loads(response.read())
            
            for document in data_json['response']['docs']:
                document['tstamp'] = datetime.datetime.strptime(document['tstamp'][0], '%Y-%m-%dT%H:%M:%S.%fZ')
                for elem in document:
                    if (elem != 'tstamp') and isinstance(document[elem], list) and len(document[elem]) == 1:
                        document[elem] = document[elem][0]
        
                if collection.count_documents(document, limit=1) == 0:
                    collection.insert_one(document)
                    print('Successfully inserted data into MongoDB')

    except urllib.error.URLError as e:
        print(e.reason)
        continue