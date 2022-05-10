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

items = {
    "1": {
        "id": "1",
        "name": "Animal 1",
        "img_url": "https://cdn-icons-png.flaticon.com/512/4193/4193243.png",
        "price": "$100",
        "summary": ""
    },
    "2": {
        "id": "2",
        "name": "Animal 2",
        "img_url": "https://cdn-icons-png.flaticon.com/512/4193/4193245.png",
        "price": "$100",
        "summary": ""
    },
    "3": {
        "id": "3",
        "name": "Animal 3",
        "img_url": "https://cdn-icons-png.flaticon.com/512/4193/4193247.png",
        "price": "$100",
        "summary": ""
    },
    "4": {
        "id": "4",
        "name": "Animal 4",
        "img_url": "https://cdn-icons-png.flaticon.com/512/4193/4193249.png",
        "price": "$100",
        "summary": ""
    },
    "5": {
        "id": "5",
        "name": "Animal 5",
        "img_url": "https://cdn-icons-png.flaticon.com/512/4193/4193251.png",
        "price": "$100",
        "summary": ""
    },
    "11": {
        "id": "11",
        "name": "Pet 1",
        "img_url": "https://cdn-icons-png.flaticon.com/512/4213/4213616.png",
        "price": "$50",
        "summary": ""
    },
    "12": {
        "id": "12",
        "name": "Pet 2",
        "img_url": "https://cdn-icons-png.flaticon.com/512/4213/4213623.png",
        "price": "$50",
        "summary": ""
    },
    "13": {
        "id": "13",
        "name": "Pet 3",
        "img_url": "https://cdn-icons-png.flaticon.com/512/4213/4213627.png",
        "price": "$50",
        "summary": ""
    },
    "14": {
        "id": "14",
        "name": "Pet 4",
        "img_url": "https://cdn-icons-png.flaticon.com/512/4213/4213630.png",
        "price": "$50",
        "summary": ""
    },
    "15": {
        "id": "15",
        "name": "Pet 5",
        "img_url": "https://cdn-icons-png.flaticon.com/512/4213/4213672.png",
        "price": "$50",
        "summary": ""
    },
    "21": {
        "id": "21",
        "name": "Home 1",
        "img_url": "https://cdn-icons-png.flaticon.com/512/4288/4288932.png",
        "price": "$75",
        "summary": ""
    },
    "22": {
        "id": "22",
        "name": "Home 2",
        "img_url": "https://cdn-icons-png.flaticon.com/512/4288/4288939.png",
        "price": "$75",
        "summary": ""
    },
    "23": {
        "id": "23",
        "name": "Home 3",
        "img_url": "https://cdn-icons-png.flaticon.com/512/4288/4288945.png",
        "price": "$75",
        "summary": ""
    },
    "24": {
        "id": "24",
        "name": "Home 4",
        "img_url": "https://cdn-icons-png.flaticon.com/512/4288/4288953.png",
        "price": "$75",
        "summary": ""
    },
    "25": {
        "id": "25",
        "name": "Home 5",
        "img_url": "https://cdn-icons-png.flaticon.com/512/4288/4288960.png",
        "price": "$75",
        "summary": ""
    }
}


# Server process route
@app.route('/')
def welcome():
   return render_template('home_page.html')  

@app.route('/shop_items')
def display():
   global items
   return render_template('shop_grid.html', items=items)


if __name__ == '__main__':
   app.run(debug = True)

