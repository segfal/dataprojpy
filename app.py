from flask import Flask
import mysql.connector
from mysql.connector import connection
from flask_cors import CORS
import mysql.connector
import numpy as np 
import pandas as pd



app = Flask(__name__)
CORS(app)

@app.route('/')
def greeting():
    return "<p> good morning </p>"

@app.route('/home')
def welcome():
    return "Welcome home"

