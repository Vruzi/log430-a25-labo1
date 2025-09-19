import os
from dotenv import load_dotenv
import pymongo
from models.user import User

class UserDAOMongo:
    def __init__(self):
        try:
            env_path = ".env"
            print(os.path.abspath(env_path))
            load_dotenv(dotenv_path=env_path)

            db_host = os.getenv("MONGODB_HOST")
            db_name = os.getenv("MYSQL_DB_NAME")
            db_user = os.getenv("DB_USERNAME")
            db_pass = os.getenv("DB_PASSWORD")

            uri = f"mongodb://{db_user}:{db_pass}@{db_host}:27017/"

            self.conn = pymongo.MongoClient(uri)
            self.db = self.conn[db_name]
        except FileNotFoundError as e:
            print("Attention : Veuillez créer un fichier .env")
        except Exception as e:
            print("Erreur : " + str(e))

    def select_all(self):
        """ Select all users from MongoDB """
        col = self.db["users"]
        return [User(*col) for col in col.find()]

    def insert(self, user):
        """ Insert given user into MongoDB """
        col = self.db["users"]
        dict = { "name": user.name, "email": user.email }
        col.insert_one(dict)
        return str(dict["_id"])

    def update(self, user):
        """ Update given user in MongoDB """
        col = self.db["users"]
        query = { "_id": user.id }
        newValue = { "$set": { "name": user.name, "email": user.email } }
        col.update_one(query, newValue)
        return [print(x) for x in col.find()]

    def delete(self, user_id):
        """ Delete user from MongoDB with given user ID """
        col = self.db["users"]
        query = { "_id": user_id }
        col.delete_one(query)
        return [print(x) for x in col.find()]

    def delete_all(self): #optional
        """ Empty users table in MongoDB """
        col = self.db["users"]
        return col.delete_many({}).deleted_count
        
    def close(self):
        self.conn.close()