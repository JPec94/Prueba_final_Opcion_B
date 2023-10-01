from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os


load_dotenv()

class m_connect:
    def __init__(self):
        user = os.getenv("MONGODB_USER")
        password = os.getenv("MONGODB_PASS")
        uri = f"mongodb+srv://{user}:{password}@datapruebafinal.cbsjndj.mongodb.net/?retryWrites=true&w=majority"

        self.client = MongoClient(uri, server_api=ServerApi('1'))

    def test_connection(self):
        # Send a ping to confirm a successful connection
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    m_connect().test_connection()