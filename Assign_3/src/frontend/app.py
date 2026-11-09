
import os
from flask import Flask, render_template, request
import requests


BACKEND_URL = os.getenv("BACKEND_URL")
app = Flask(__name__)

#Task - 2 signup route to render the index.html page
@app.route('/')
def signup(): 
    #Redirect the user to a signup page where they can enter their name, email, and password for sign up.
    return render_template('index.html')

@app.route('/', methods=['POST'])
def signup_post():
    # Get the form data
    #Create a form on the frontend that, when submitted, inserts data into MongoDB Atlas.
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
        postUrl = f"{BACKEND_URL}/signup"

        response = requests.post(postUrl, user_data)
        print(postUrl) 
        print(response.json()) 

        #On success: The user should be redirected to another page displaying the message “Data submitted successfully”
        if(response.json().get("message") == "Success"):
            return render_template('success.html', name=name)
        else:
            return render_template('index.html', error="An error occurred while submitting the data. Please try again."+str(response))


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)