
import nltk
nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy


from data_preprocessing import data_preprocessing
training, output,labels, words, data = data_preprocessing(stemmer)


    
###### architecture file       

from sklearn.model_selection import train_test_split

X_train, X_test, y_train,y_test = train_test_split(training,output,test_size=0.25)

print(X_train.shape,y_train.shape)
print(X_test.shape,y_test.shape)
print(X_train,y_train)
print(X_test,y_test)


from init_model import init_model
model = init_model(X_train,y_train,X_test,y_test)



#####
######### data pre processing module
def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
            
    return numpy.array(bag)

            
#### main file   
from chat import  chat 
chat(model,bag_of_words,labels,words,data)

model = Word2Vec.load('model.bin')

