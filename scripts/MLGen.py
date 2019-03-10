import keras 
import pandas as pd
import numpy as np
import random
import keras
import pickle
import re


maxlen = 10


with open('../ML model/text_data.txt', 'rb') as fn:
    text = fn.read()
    text = text.decode()

chars = sorted(list(set(text)))

with open('../ML model/char_indices.pickle', 'rb') as picklein:
    char_indices = pickle.load(picklein)
with open('../ML model/indices_char.pickle', 'rb') as picklein:
    indices_char = pickle.load(picklein)


def sample(preds, temperature=1.0):
    # helper function to sample an index from a probability array
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)
    
def generate_text(length, diversity):
    # Get random name
    start_index = random.randint(0, len(text) - maxlen - 1)
    generated = ''
    sentence = text[start_index: start_index + maxlen]
    generated += sentence
    for i in range(length):
            x_pred = np.zeros((1, maxlen, len(chars)))
            for t, char in enumerate(sentence):
                x_pred[0, t, char_indices[char]] = 1.

            preds = model.predict(x_pred, verbose=0)[0]
            next_index = sample(preds, diversity)
            next_char = indices_char[next_index]

            generated += next_char
            sentence = sentence[1:] + next_char
    return sentence


def generator(num):
    names = []
    for i in range(num):
        randnum = random.randint(0, 50)
        names.append(re.sub("[\n (){}?/,.<>:-]", "", generate_text(randnum, 0.5)))
    return names


model = keras.models.load_model('../ML model/modelForNames.h5')

if __name__ == "__main__":
    names = generator(20)
    for i in names:
        print(i)

