from flask import Flask, render_template
from pymongo.mongo_client import MongoClient
from flask import Flask, render_template_string
from dotenv import load_dotenv
from pymongo.server_api import ServerApi
import os


load_dotenv()
app = Flask(__name__)

class MongoDB:
    def __init__(self):
        user = os.getenv("MONGODB_USER")
        password = os.getenv("MONGODB_PASS")
        uri = f"mongodb+srv://{user}:{password}@datapruebafinal.cbsjndj.mongodb.net/?retryWrites=true&w=majority"
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        self.db = self.client['datapruebafinal']
        self.collection = self.db['moto_list']


@app.route('/')
def index():
    # Obtiene los datos de la base de datos
    mongo = MongoDB()
    moto_data = mongo.collection.find()

    return render_template('index.html', moto_data=moto_data)

if __name__ == "__main__":
    app.run(debug=True)