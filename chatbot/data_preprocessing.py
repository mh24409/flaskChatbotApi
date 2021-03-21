import nltk 
import json
import pickle
import numpy
#list of libraries used by the code
import gensim
from gensim import models
from gensim.models import Word2Vec, KeyedVectors
import string
from gensim.models import Word2Vec
import logging
from nltk.corpus import stopwords
from textblob import Word
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
def data_preprocessing(stemmer):
    
    
    with open("intents.json") as file:
        data = json.load(file)
    
    try:
        with open("data.pickle", "rb") as f:
            words, labels, training, output = pickle.load(f)
            return (training, output,labels,words,data)
    except:
        words = []
        labels = []
        docs_x = []
        docs_y = [] 
        for intent in data ["intents"]:
            for pattern in intent["patterns"]:
                wrds = nltk.word_tokenize(pattern)
                words.extend(wrds)
                docs_x.append(wrds)
                docs_y.append(intent["tag"])
    
            if intent["tag"] not in labels:
                labels.append(intent["tag"])
    
        words = [stemmer.stem(w.lower()) for w in words if w != "?"]
        words = sorted(list(set(words)))
    
        labels = sorted(labels)
    
        training = []
        output = []
    
        out_empty = [0 for _ in range(len(labels))]
    
        for x, doc in enumerate(docs_x):
            bag = []
    
            wrds = [stemmer.stem(w) for w in doc]
    
            for w in words:
                if w in wrds:
                    bag.append(1)
                else:
                    bag.append(0)
    
    
            output_row = out_empty[:]
            output_row[labels.index(docs_y[x])] = 1
    
            training.append(bag)
            output.append(output_row)
    
    
        training = numpy.array(training)
        output = numpy.array(output)
    
        with open("data.pickle", "wb") as f:
            pickle.dump((words, labels, training, output), f)
        
        return training, output,labels,words,data
   
    # vectorizer=CountVectorizer()
    # vocabulary=vectorizer.fit(data)
    # X= vectorizer.transform(data)
    # print(X.toarray())
    # print(vocabulary.get_feature_names())
        stop = stopwords.words('english')
        df = pd.DataFrame(data)
        df['patterns'] = df['patterns'].apply(', '.join)
        print(df)
        df['patterns'] = df['patterns'].apply(lambda x:' '.join(x.lower() for x in x.split()))
        df['patterns']= df['patterns'].apply(lambda x: ' '.join(x for x in x.split() if x not in string.punctuation))
        df['patterns']= df['patterns'].str.replace('[^\w\s]','')
        df['patterns']= df['patterns'].apply(lambda x: ' '.join(x for x in x.split() if  not x.isdigit()))
        df['patterns'] = df['patterns'].apply(lambda x:' '.join(x for x in x.split() if not x in stop))
        df['patterns'] = df['patterns'].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))
        bigger_list=[]
        for i in df['patterns']:
            li = list(i.split(" "))
            bigger_list.append(li)
    #structure of data to be taken by the model.word2vec
        print("Data format for the overall list:",bigger_list)
    #custom data is fed to machine for further processing
        model = Word2Vec(bigger_list, min_count=1,size=300,workers=4)
        #print(model)
        model.save("word2vec.model")
        model.save("model.bin")


        