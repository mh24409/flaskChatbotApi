#!/usr/bin/python3
from flask import Flask, request, jsonify ,render_template
from flask_restful import Resource, Api
from json import dumps
from main import main 
import numpy
import random
from time import sleep
import response
from response import process
app = Flask(__name__)
api = Api(app)


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
@app.route("/g", methods=['GET', 'POST'])
def notes_list():

       return pets[0]
#-----------------------------------------------------------------

if __name__ == '__main__':
     app.run(debug=True)