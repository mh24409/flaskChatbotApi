

import tflearn
from tensorflow.python.framework import ops
import gensim
from gensim import models
from gensim.models import Word2Vec, KeyedVectors
import string
from gensim.models import Word2Vec

def init_model(X_train,y_train,X_test,y_test):
    
    ops.reset_default_graph()
    
    net = tflearn.input_data(shape=[None, len(X_train[0])])
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, len(y_train[0]), activation = "softmax")
    net = tflearn.regression(net)
    
    model = tflearn.DNN(net)

    import os
    
    
    if os.path.exists("model.tflearn.meta"):
        model.load("model.tflearn")
    else:
        model.fit(X_train, y_train,validation_set=(X_test,y_test), n_epoch=400, batch_size=8, show_metric=True)
        model.save("model.tflearn")
        
    return model
