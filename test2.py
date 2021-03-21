#!/usr/bin/python3
from flask import Flask, request, jsonify ,render_template
from flask_restful import Resource, Api
from json import dumps
from main import main 
import numpy
import random
from time import sleep
import main
from main import chat
app = Flask(__name__)
api = Api(app)

#--------------------------------------------------------------------
@app.route('/', methods = ['GET', 'POST', 'DELETE'])
def home():
   return render_template("index.html")

       
@app.route('/get', methods = ['GET', 'POST', 'DELETE'])
def get_bot_response():
    userMessage = request.args.get('msg')
    return str(chat(userMessage))
       

# ----------------------------------------------------------------
@app.route('/users/<user_id>', methods = ['GET', 'POST', 'DELETE'])
def user(user_id):
    if request.method == 'GET':
       return 'hello'
    if request.method == 'POST':
        user = user_id
        return user

#----------------------------------------------------------------

pets = ['cat', 'dog', 'fish']
marks = [ 5, 4, 3, 2, 1]
@app.route("/g", methods=['GET', 'POST'])
def notes_list():

       return pets[0]
#-----------------------------------------------------------------

if __name__ == '__main__':
     app.run(debug=True)