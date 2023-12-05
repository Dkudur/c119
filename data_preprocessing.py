#Text Data Preprocessing Lib
import nltk

# PorterStemmer() will find the stem/root words from the words
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()


import json
import pickle
import numpy as np

words=[]
classes = []
word_tags_list = []

ignore_words = ['?', '!',',','.', "'s", "'m"]
train_data_file = open('intents.json').read()
intents = json.loads(train_data_file)

def getStemWords(words, ignoreWords):
        stem_words = []
        for word in words:
                if word not in ignoreWords:
                        w = stemmer.stem(word.lower())
                        stem_words.append(w)
        
        return stem_words

            
getStemWords(words, ignore_words)


# hey how are you doing ? ---> hey how be you do 









