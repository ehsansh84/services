import re
from nltk.corpus import stopwords
from stemming.porter2 import stem


class Text:
    @classmethod
    def remove_special_chars(cls, s):
        s = s.replace(r'\n', ' ')
        return re.sub('[^a-zA-Z0-9-_*]', ' ', s)

    @classmethod
    def make_list_of_words(cls, s):
        s.lower()
        return s.split()

    @classmethod
    def remove_stop_words_and_stem(cls, s):
        stop_words = set(stopwords.words('english'))
        new_list = []
        unique_words = []
        for word in s:
            if word not in stop_words:
                w = stem(word)
                new_list.append(w)
                # Here I want to create unique_words
                if w not in unique_words:
                    unique_words.append(w)
        return {'refined_list': new_list, 'unique_words': unique_words}

