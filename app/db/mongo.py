import os
import pymongo
from datetime import datetime

class Mongo:
    def __init__(self, MONGO_URL, DATABASE, COLLECTION):
        self.client = pymongo.MongoClient(MONGO_URL)
        self.db = self.client[DATABASE]
        self.collection = self.db[COLLECTION]

    def index(self):
        try:
            return [doc for doc in self.collection.find( {}, {'_id': 0} )]
        except:
            return 'failed'

    def show(self, job_id):
        try:
            return self.collection.find_one(
                { 'job_id': job_id },
                {'_id': 0}
            )
        except:
            return 'failed'

    def upsert(self, documents):
        try:
            for doc in documents:
                doc['updated_at'] = datetime.now()
                self.collection.update_one(
                    { 'job_id': doc['job_id'] },
                    { '$set': doc },
                    upsert=True
                )
            return 'success'
        except:
            return 'failed'

    
