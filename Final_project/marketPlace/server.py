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



mongoClient = pymongo.MongoClient(
    "mongodb+srv://mongodb:Xcz990208@cluster0.rfss2.mongodb.net/user_Database?retryWrites=true&w=majority")

result = mongoClient['user_Database']['items'].aggregate([])
result = list(result)
for item in result:
    del item["_id"]
items = result


# Server process route
@app.route('/')
def welcome():
   return render_template('home_page.html')  

@app.route('/shop_items')
def display():
   global items
   return render_template('shop_grid.html', items=items)

@app.route('/login', methods=['GET', 'POST'])
def login_check():
    user_info = request.get_json()
    if user_info['user_name'] in ['ChongzhiXu'] and user_info['password'] in ['12345678']:
        return render_template('shop_grid.html')
    else:
        return render_template('home_page.html')

if __name__ == '__main__':
   app.run(debug = True)

