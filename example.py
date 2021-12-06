import mysql.connector
from data import cursor


DB_NAME = 'chicken'



def create_database():
    cursor.execute("CREATE DATABASE {}".format(DB_NAME))
    print("database {} ".format(DB_NAME))


create_database()