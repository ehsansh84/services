# This file will analyze documents and generates the final results
import json
import re
from nltk.corpus import stopwords
from stemming.porter2 import stem
from public_data import *

col = db['bigtc']

# from pprint import pprint
text = ''
words = []
refined_words = []
current_doc_words = []
bag_of_words = []


def remove_special_chars(s):
    s = s.replace(r'\n', ' ')
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
                current_doc_words.append(word)
    return {'refined_list': new_list, 'current_doc_words': current_doc_words}

# with open('data.json') as data_file:
#     data = json.load(data_file)
#
# for item in data:
#     col.insert({
#         'class': item['class'],
#         'title': item['title'],
#         'text': item['text']
#                 })


db = con.bigtc
col_analyze = db['analyze']


def init_bigtc():
    f = open('news_sample.txt', 'r')
    news_sample = f.read()
    col_analyze.remove({})
    col_analyze.insert({'level': 'step1', 'desc': 'this is original text', 'text': news_sample})
    col_analyze.insert({'level': 'step2', 'desc': 'Remove special characters', 'text': ''})
    col_analyze.insert({'level': 'step3', 'desc': 'Make list of words', 'text': ''})
    col_analyze.insert({'level': 'step4', 'desc': 'Remove stop words and stem', 'text': ''})
    # col_analyze.insert({'level': 'step5', 'desc': '', 'text': ''})
    # col_analyze.insert({'level': 'step6', 'desc': '', 'text': ''})
    # col_analyze.insert({'level': 'step7', 'desc': '', 'text': ''})
    # col_analyze.insert({'level': 'step8', 'desc': '', 'text': ''})
    # col_analyze.insert({'level': 'step9', 'desc': '', 'text': ''})

init_bigtc()

data = col_analyze.find({'level': 'step1'})
news_doc = data[0]['text']
print(news_doc)

news_doc = remove_special_chars(news_doc)
col_analyze.update({'level': 'step2'}, {'$set': {'text': news_doc}})
print(news_doc)

news_doc = make_list_of_words(news_doc)
col_analyze.update({'level': 'step3'}, {'$set': {'text': news_doc}})
print(news_doc)

news_doc = remove_stop_words_and_stem(news_doc)
col_analyze.update({'level': 'step4'}, {'$set': {'text': news_doc}})
print(news_doc)

# print(news_sample)
# print(len(news_sample))

# news_sample = remove_special_chars(news_sample)
# print(news_sample)
# print(len(news_sample))


# text = remove_special_chars(data[0]['text'])
# # print('Count: %s Data: %s' % (len(text), text))
# words = make_list_of_words(text)
# # print('Count: %s Data: %s' % (len(words), words))
# refined_words = remove_stop_words_and_stem(words)['refined_list']
# print('Count: %s Data: %s' % (len(refined_words), refined_words))
# current_doc_words = remove_stop_words_and_stem(words)['current_doc_words']
# print('Count: %s Data: %s' % (len(current_doc_words), current_doc_words))