from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)
import time
import pymongo
from pymongo import MongoClient


# MongoDB data service
def mongoFind(acconut_id):
    mongodb_url = "mongodb+srv://mongodb:Xcz990208@cluster0.rfss2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    mongo_client = MongoClient(mongodb_url)
    db = mongo_client["user_Database"]
    Users = db["Users"]

def mongoPost(account_id):
    mongodb_url = "mongodb+srv://mongodb:Xcz990208@cluster0.rfss2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    mongo_client = MongoClient(mongodb_url)
    db = mongo_client["user_Database"]
    Users = db["Users"]

def mongoUpdate(account_id):
    mongodb_url = "mongodb+srv://mongodb:Xcz990208@cluster0.rfss2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    mongo_client = MongoClient(mongodb_url)
    db = mongo_client["user_Database"]
    Users = db["Users"]


# Server process route
@app.route('/')
def welcome():
   return render_template('home_page.html')  


if __name__ == '__main__':
   app.run(debug = True)

