import csv
from itertools import count
import re
from nltk.stem.porter import PorterStemmer
import nltk

def remove_html_tags(text):
    """Removes html charactors from text"""
    clean_text = re.sub(r'<.*?>', '', text)
    return clean_text

def remove_special_characters(text):
    """Removes special charactors and numbers from text"""
    # Note ^ inverts the list. 
    clean_text = re.sub(r'[^a-zA-Z\s]', '', text)
    return clean_text

def read_index(filename, encoding):
    """Reads CSV file and returns and dictionary
     
    Parameters
    ----------
    filename : str
        The filename of the CSV file.  
    encoding : str
        The expected coding.  If this is missed 
        get odd charactors at start of the file

    Returns
    -------
    dict : dict
        A dictionary with the contents on the CSV file
    """
    dict = {}
    index = count()
    with open( filename, 'r', encoding=encoding) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            dict[next(index)] = row
    return(dict)

def read_text(filename, encoding):
    """Reads and cleans html tags and special charactors from a text file

    Parameters
    ----------
    filename : str
        The filename of the CSV file.  
    encoding : str
        The expected coding.  If this is missed 
        get odd charactors at start of the file

    Returns
    -------
    text_string : str
        One clean text string for the whole file
    """

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
    """Read read files and concatenate into the corpus

    Parameters
    ----------
    index : dict
        A dictionary read from the index.csv file.
    encoding: str
        The expected coding.  If this is missed 
        get odd charactors at start of the file.
    path : str
        The path to the data files
    """

    corpus = []
    for item in index.values():
        filename = path + item['File']
        text_string = read_text(filename, encoding)
        corpus.append(text_string)
    return(corpus)

def tokenize(text):
        """Returns the stemmed text"""
        stemmer = PorterStemmer()
        tokens = [word for word in nltk.word_tokenize(text) if len(word) > 1] 
        #if len(word) > 1 because only want to retain words that are at least two characters before stemming
        stems = [stemmer.stem(item) for item in tokens]
        return stems