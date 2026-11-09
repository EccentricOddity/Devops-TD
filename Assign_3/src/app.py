from logging import exception
import os
from sys import exception
from flask import Flask, json, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)

db = client['user_data']

collection = db['users']


app = Flask(__name__)

#Task - 1 API endpoint to return a JSON with List in data attribute from a file
#1. Create a Flask application with an /api route.
@app.route('/api')  
def home():
    with open('data/data_sample.json') as f:
        #The data should be stored in a backend file, read from it, and sent as a response.
        json_response = json.load(f) 	
        #When this route is accessed, it should return a JSON list. 
    return json_response 

#Task - 2 signup route to render the index.html page
@app.route('/signup')
def signup(): 
    #Redirect the user to a signup page where they can enter their name, email, and password for sign up.
    return render_template('index.html')

#Task - 2 post route to handle the form submission
@app.route('/signup', methods=['POST'])
def signup_post():
    # Get the form data
    #Create a form on the frontend that, when submitted, inserts data into MongoDB Atlas.
    try:
        form_data = request.form
        name = form_data.get('name')
        email = form_data.get('email')
        password = form_data.get('password')
       
        # code to save the data to a database
        user_data = {
            'name': name,
            'email': email,
            'password': password
        }
        collection.insert_one(user_data)
        #On success: The user should be redirected to another page displaying the message “Data submitted successfully”
        return render_template('success.html', name=name)

    except Exception as e:
        #On error: display the error on the same page without redirection.
        return render_template('index.html', error="An error occurred while submitting the data. Please try again."+str(e))

if __name__ == '__main__':
    app.run(debug=True)