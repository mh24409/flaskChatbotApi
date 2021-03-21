import numpy
import random
from time import sleep


def chat(model, bag_of_words, labels, words, data,message):

    print("Hi, How can i help you ?")
        inp = message
        results = model.predict([bag_of_words(inp, words)])[0]

        results_index = numpy.argmax(results)
        tag = labels[results_index]

        if results[results_index] > 0.8:
            for tg in data["intents"]:
                if tg['tag'] == tag:
                    responses = tg['responses']
            sleep(3)
            Bot = random.choice(responses)
            return(Bot)
        else:
            return("I don't understand!")
