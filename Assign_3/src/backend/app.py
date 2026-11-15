import os
from flask import Flask, json, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

app = Flask(__name__)

#Task - 1 API endpoint to return a JSON with List in data attribute from a file
#1. Create a Flask application with an /api route.
@app.route('/api')  
def home():
    with open('../data/data_sample.json') as f:
        #The data should be stored in a backend file, read from it, and sent as a response.
        json_response = json.load(f) 	
        #When this route is accessed, it should return a JSON list. 
    return json_response 


#Task - 2 post route to handle the todoitem post request
@app.route('/submititem', methods=['POST'])
def submit_todo_item():
    # Get the form data
    #Create a form on the frontend that, when submitted, inserts data into MongoDB Atlas.
    db = client['user_data']
    
    collection = db['todo_items']
    try:
        form_data = request.form
        print(form_data)
        itemName = form_data.get('itemName')
        itemDescription = form_data.get('itemDescription')
        # print(name,email,password)
        # code to save the data to a database
        todo_data = {
            'name': itemName,
            'description': itemDescription
        }
        collection.insert_one(todo_data)


        #On success: The user should be redirected to another page displaying the message “Data submitted successfully”
        return {"message": "Success"}

    except Exception as e:
        #On error: display the error on the same page without redirection.
        return {"error": "Error: " + str(e)}


#Task - 2 post route to handle the form submission
@app.route('/signup', methods=['POST'])
def submit_user():
    # Get the form data
    #Create a form on the frontend that, when submitted, inserts data into MongoDB Atlas.
    db = client['user_data']

    collection = db['users']
    try:
        form_data = request.form
        print(form_data)
        name = form_data.get('name')
        email = form_data.get('email')
        password = form_data.get('password')
        # print(name,email,password)
        # code to save the data to a database
        user_data = {
            'name': name,
            'email': email,
            'password': password
        }
        collection.insert_one(user_data)


        #On success: The user should be redirected to another page displaying the message “Data submitted successfully”
        return {"message": "Success"}

    except Exception as e:
        #On error: display the error on the same page without redirection.
        return {"error": "Error: " + str(e)}

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4000,debug=True)