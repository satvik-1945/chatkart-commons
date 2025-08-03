import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_name = os.getenv("DB_NAME", "chatkart_db")

