import csv
from itertools import count
import numpy as np
import re
from nltk.stem.porter import PorterStemmer
import nltk

def remove_html_tags(text):
    clean_text = re.sub(r'<.*?>', '', text)
    return clean_text

def remove_special_characters(text):
    clean_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return clean_text

def read_index(filename, encoding):
    dict = {}
    index = count()
    with open( filename, 'r', encoding=encoding) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            dict[next(index)] = row
    return(dict)

def read_text(filename, encoding):
    with open( filename, 'r', encoding=encoding) as text_file:
        text_string = ''
        for line in text_file:
            line_string = line.strip()
            if line_string != '':
                html_free_text = remove_html_tags(line_string)
                clean_text = remove_special_characters(html_free_text)
                text_string = text_string + ' ' + clean_text
    return(text_string)

def read_text_files(index, encoding, path):
    corpus = []
    for key1, item1 in index.items():
        filename = path + item1['File']
        text_string = read_text(filename, encoding)
        corpus.append(text_string)
    return(corpus)

def tokenize(text):
        stemmer = PorterStemmer()
        tokens = [word for word in nltk.word_tokenize(text) if len(word) > 1] 
        #if len(word) > 1 because only want to retain words that are at least two characters before stemming
        stems = [stemmer.stem(item) for item in tokens]
        return stems