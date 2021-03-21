import nltk
nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy
import tensorflow as tf
import tflearn
import random
import json
import pickle

from time import sleep
import a 
from a import process
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_reponse():
    userText = request.args.get('msg')
    return str(process(userText))

if __name__ == "__main__":
    app.run(debug=True)