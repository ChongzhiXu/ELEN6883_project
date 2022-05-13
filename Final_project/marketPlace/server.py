from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)
import time
import pymongo
from pymongo import MongoClient


# MongoDB data service
def findItems(status):
    mongoClient = pymongo.MongoClient(
        "mongodb+srv://mongodb:Xcz990208@cluster0.rfss2.mongodb.net/user_Database?retryWrites=true&w=majority")
    q={}
    q['status'] = status
    q1={}
    q1['$match'] = q
    q2 = []
    q2.append(q1)
    result = mongoClient['user_Database']['items'].aggregate(q2)
    result = list(result)
    for item in result:
        del item["_id"]
    items = result
    return items


# Server process route
@app.route('/')
def welcome():
   return render_template('home_page.html')  

@app.route('/shop_items')
def display():
    items = findItems('sale')
    return render_template('shop_grid.html', items=items)

@app.route('/shop_items/<num>')
def display_category(num):
    mongoClient = pymongo.MongoClient(
        "mongodb+srv://mongodb:Xcz990208@cluster0.rfss2.mongodb.net/user_Database?retryWrites=true&w=majority")
    q={}
    q['status'] = 'sale'
    q['category'] = num
    q1={}
    q1['$match'] = q
    q2=[]
    q2.append(q1)
    result = mongoClient['user_Database']['items'].aggregate(q2)
    result = list(result)
    for item in result:
        del item["_id"]
    items = result
    return render_template('shop_grid.html', items=items)


@app.route('/profile')
def profile_info():
    items = findItems(token_address)
    return render_template('profile_display.html', items=items)

@app.route('/login', methods=['GET', 'POST'])
def login_check():

    user_info = request.get_json()
    print(user_info)
    print(type(user_info))

    # Check from mongoDB
    mongodb_url = "mongodb+srv://mongodb:Xcz990208@cluster0.rfss2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    mongo_client = MongoClient(mongodb_url)
    db = mongo_client["user_Database"]
    res = db.Users.find_one({'Name':user_info['user_name']})
    print(res)

    if user_info['user_name'] in res['Name'] and user_info['password'] in res['Account_pwd']:
        # Token address and full info of user
        global token_address, Login_user_info
        Login_user_info = res
        token_address = res['Ale_id']
        return jsonify(url='shop_items')
    else:
        return jsonify(url='')


@app.route('/register', methods=['GET', 'POST'])
def sign_up():
    user_register = request.get_json()
    print(user_register)
    print(type(user_register))

    # Load the info into mongoDB
    mongodb_url = "mongodb+srv://mongodb:Xcz990208@cluster0.rfss2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    mongo_client = MongoClient(mongodb_url)
    db = mongo_client["user_Database"]
    new_user_info ={
        'Name': user_register['user_name'],
        'Account_id': user_register['email'],
        'Account_pwd': user_register['password'],
        'Ale_id': user_register['ale_id'],
        'Transaction_records':[],
        'items_owned':[],
        'items_selling':[]
        }
    res = db.Users.insert_one(new_user_info)

    return jsonify(url='/')


if __name__ == '__main__':
   app.run(debug = True)

