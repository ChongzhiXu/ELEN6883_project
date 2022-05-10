from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)
import time
import pymongo
from pymongo import MongoClient


# Music items database
items = {
    "1": { 
    "id": "1", 
    "item_title": "",
    "item_info": "",
    "item_media": "",
    "item_image": ""
    },
    "2": { 
    "id": "2", 
    "item_title": "",
    "item_info": "",
    "item_media": "",
    "item_image": ""
    },
    "3": { 
    "id": "3", 
    "item_title": "",
    "item_info": "",
    "item_media": "",
    "item_image": ""
    },
    "4": { 
    "id": "4", 
    "item_title": "",
    "item_info": "",
    "item_media": "",
    "item_image": ""
    },
    "5": { 
    "id": "5", 
    "item_title": "",
    "item_info": "",
    "item_media": "",
    "item_image": ""
    },
    "6": { 
    "id": "6", 
    "item_title": "",
    "item_info": "",
    "item_media": "",
    "item_image": ""
    },
    "7": { 
    "id": "7", 
    "item_title": "",
    "item_info": "",
    "item_media": "",
    "item_image": ""
    },
    "8": { 
    "id": "8", 
    "item_title": "",
    "item_info": "",
    "item_media": "",
    "item_image": ""
    },
    "9": { 
    "id": "9", 
    "item_title": "",
    "item_info": "",
    "item_media": "",
    "item_image": ""
    },
    "10": { 
    "id": "10", 
    "item_title": "",
    "item_info": "",
    "item_media": "",
    "item_image": ""
    },
    "11": { 
    "id": "11", 
    "item_title": "",
    "item_info": "",
    "item_media": "",
    "item_image": ""
    },
    "12": { 
    "id": "12", 
    "item_title": "",
    "item_info": "",
    "item_media": "",
    "item_image": ""
    }
}

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
   global activity
   time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
   activity[time_str] = 'home page'
   return render_template('home_page.html')  

@app.route('/learn/introduction')
def learn_intro():
    global learning_data
    page_info = learning_data["1"]
    next_category = learning_data["2"]["category"]
    next_subcategory = learning_data["2"]["subcategory"]
    print(page_info)
    if int(page_info["id"]) == len(learning_data):
        page_info["end"] = 1
    else:
        page_info["end"] = 0
    global activity
    time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    activity[time_str] = 'introduction'
    return render_template('learning.html', page_info = page_info, learning_data = learning_data, next_category=next_category,next_subcategory=next_subcategory)  

@app.route('/learn/<category>/<subcategory>')
def learn(category,subcategory):
    global activity
    global fire_simulation
    global learning_data

    time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    activity[time_str] = category+"/"+subcategory

    page_info = {}
    for item in learning_data:
        # print(learning_data[item])
        if category == learning_data[item]["category"] and subcategory == learning_data[item]["subcategory"]:
            page_info = learning_data[item]
    # print(page_info)
    next_id = str(int(page_info["id"]) + 1)
    # print(next_id)
    if int(page_info["id"])+1 == len(learning_data):
        page_info["end"] = 1
    else:
        page_info["end"] = 0
    next_category = learning_data[next_id]["category"]
    next_subcategory = learning_data[next_id]["subcategory"]
    if page_info["subcategory"] == "video":
        video_link = page_info["media"][0].replace("watch?v=", "embed/watch?v=")
        return render_template('learningvideo.html', page_info = page_info, learning_data = learning_data,next_category=next_category,next_subcategory=next_subcategory,video_link=video_link)
    elif page_info["subcategory"] == "quiz":
        return render_template('miniquiz.html',page_info=page_info, learning_data=learning_data, next_category=next_category, next_subcategory=next_subcategory)
    elif page_info["subcategory"] == "signal_fire_activity":
        return render_template('firesim.html', fire_material = fire_simulation,learning_data=learning_data, next_category=next_category, next_subcategory=next_subcategory) 
    else:  
        return render_template('learning.html', page_info = page_info, learning_data = learning_data,next_category=next_category,next_subcategory=next_subcategory)

# @app.route('/learn/signal_fire_activity')
# def build_a_fire():
#     global fire_simulation
#     global activity
#     time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#     activity[time_str] = 'signal fire activity'
#     return render_template('firesim.html', fire_material = fire_simulation)   

# @app.route('/view/<id>')
# def film_info(id = None):
#     global data
#     movie = data[int(id)]
#     return render_template('film_info.html', movie = movie)    

# @app.route('/sign_up')
# def sign_up():
#     return render_template('sign_up.html')

# @app.route('/log_in')
# def log_in():
#     return render_template('log_in.html')

@app.route('/test/homepage')
def th():
    global score
    score = 0
    
    return render_template('testhomepage.html')


@app.route('/test/<id>')
def test(id=None):
    
    one = test_data[id]
    next_id = str(int(id) + 1)
    
    if int(next_id) > len(test_data):
        next_page = "/test/result"
    else:
        next_page = "/test/" + next_id
    
    return render_template('test.html', one=one, next_page=next_page)

@app.route('/record/activity')
def get_record():
    return render_template('record.html', activity = activity)

@app.route('/record/test')
def get_test_record():
    return render_template('record_test.html', test_record = test_record)

# ajax for checking answer in test.js
@app.route('/check_ans', methods=['GET', 'POST'])
def check_ans():
    global score
    global user_ans
    json_data = request.get_json()  

    ans = json_data["ans"]
    num = json_data["num"]
    
    correct = "False"

    user_ans += str(num)+". "+str(ans)+" "

    if ans == test_answers[num]:
        correct = "True"
        score += 1
    
    fb = feedback[num]
    
    return jsonify(feedback=fb, correct=correct, real_ans=test_answers[num])

@app.route('/test/result')
def result():
    result = score
    global attempt_cnt
    global user_ans
    global test_record
    grade = score / len(test_data) * 100
    attempt_cnt += 1
    test_record[attempt_cnt] = "Answers: "+user_ans + " "+"Grades: "+str(grade)
    user_ans = ""
    return render_template('testresult.html', result=result)

@app.route('/certificate')
def certificate():
    grade = score / len(test_data) * 100
    return render_template('certificate.html', grade=grade)

if __name__ == '__main__':
   app.run(debug = True)

