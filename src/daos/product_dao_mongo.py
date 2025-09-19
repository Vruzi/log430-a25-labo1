import os
from dotenv import load_dotenv
import pymongo
from bson import ObjectId
from models.product import Product

class ProductDAOMongo:
    def __init__(self):
        try:
            env_path = ".env"
            load_dotenv(dotenv_path=env_path)

            db_host = os.getenv("MONGODB_HOST") or "localhost"
            db_name = os.getenv("MYSQL_DB_NAME") or "mydb"
            db_user = os.getenv("DB_USERNAME") or ""
            db_pass = os.getenv("DB_PASSWORD") or ""

            if db_user and db_pass:
                uri = f"mongodb://{db_user}:{db_pass}@{db_host}:27017/?authSource=admin"
            else:
                uri = f"mongodb://{db_host}:27017/"

            self.conn = pymongo.MongoClient(uri, serverSelectionTimeoutMS=2000)
            self.conn.admin.command("ping")

            self.db = self.conn[db_name]

        except FileNotFoundError:
            print("Attention : Veuillez créer un fichier .env")
            raise
        except Exception as e:
            print("Erreur : " + str(e))
            raise

    def select_all(self):
        """ Select all products from MongoDB """
        col = self.db["products"]
        return [
            Product(str(doc["_id"]), doc.get("name"), doc.get("brand"), doc.get("price"))
            for doc in col.find()
        ]

    def insert(self, product):
        """ Insert given product into MongoDB """
        col = self.db["products"]
        doc = {"name": product.name, "brand": product.brand, "price": product.price}
        res = col.insert_one(doc)
        return str(res.inserted_id)

    def update(self, product):
        """ Update given product in MongoDB """
        col = self.db["products"]
        query = {"_id": ObjectId(product.id) if isinstance(product.id, str) else product.id}
        newValue = {"$set": {"name": product.name, "brand": product.brand, "price": product.price}}
        res = col.update_one(query, newValue)
        return res.modified_count

    def delete(self, product_id):
        """ Delete product from MongoDB with given product ID """
        col = self.db["products"]
        query = {"_id": ObjectId(product_id) if isinstance(product_id, str) else product_id}
        res = col.delete_one(query)
        return res.deleted_count

    def delete_all(self):  # optional
        """ Empty products table in MongoDB """
        col = self.db["products"]
        return col.delete_many({}).deleted_count

    def close(self):
        self.conn.close()
