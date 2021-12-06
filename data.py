from dotenv import load_dotenv
import mysql.connector

load_dotenv('./.env')
import os
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
config = {
    'user': DB_USER,
    'password' : DB_PASSWORD,
    'host' : DB_HOST
    }


db = mysql.connector.connect(**config)

cursor = db.cursor()