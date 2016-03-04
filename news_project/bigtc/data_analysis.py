import json
import re
from nltk.corpus import stopwords
from stemming.porter2 import stem
from public_data import *

col = db['BigTC']
# from pprint import pprint
text = ''
words = []
refined_words = []
current_doc_words = []
bag_of_words = []

def remove_special_chars(s):
    return re.sub('[^a-zA-Z0-9-_*]', ' ', s)

def make_list_of_words(s):
    s.lower()
    return s.split()


def remove_stop_words_and_stem(s):
    stop_words = set(stopwords.words('english'))
    new_list = []
    current_doc_words = []
    for word in s:
        if word not in stop_words:
            new_list.append(stem(word))
    #         Here I want to create current_doc_words
            if word not in current_doc_words:
                current_doc_words.append(words)
    return {'refined_list': new_list, 'current_doc_words': current_doc_words}

with open('data.json') as data_file:
    data = json.load(data_file)

for item in data:
    col.insert({
        'class': item['class'],
        'title': item['title'],
        'text': item['text']
                })

# text = remove_special_chars(data[0]['text'])
# # print('Count: %s Data: %s' % (len(text), text))
# words = make_list_of_words(text)
# # print('Count: %s Data: %s' % (len(words), words))
# refined_words = remove_stop_words_and_stem(words)['refined_list']
# print('Count: %s Data: %s' % (len(refined_words), refined_words))
# current_doc_words = remove_stop_words_and_stem(words)['current_doc_words']
# print('Count: %s Data: %s' % (len(current_doc_words), current_doc_words))