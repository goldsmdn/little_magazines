from text_functions import read_text, read_index
from text_functions import read_text_files, tokenize

ENCODING = 'utf-8-sig'
PATH = 'test_data/'

def test_read_text():
    """Unit test - reading text functionality"""
    filename = PATH + 'test_data1.txt'
    text = read_text(filename, ENCODING)
    expected_text = ' test data more data'
    assert expected_text == text

def test_full_process():
    """Test end process from index read to corpus production"""
    filename = PATH + 'test_index.csv'
    index = read_index(filename, ENCODING)
    corpus = read_text_files(index, ENCODING, PATH)
    expected_corpus = [' test data more data', ' test data more data words']
    assert expected_corpus == corpus

def test_stemming():
    """Test stemming on Wikipedia example"""
    #test data from https://raw.githubusercontent.com/snowballstem/snowball-data/master/porter/voc.txt
    text = 'argue, fished, fisher, fisherman, argue, argued, argues, arguing, argus, abandon, abandoned, abandoning'
    stemmed_text = tokenize(text)
    expected_text = ['argu', 'fish', 'fisher', 'fisherman', 'argu', 'argu', 'argu', 'argu', 'argu', 'abandon', 'abandon', 'abandon']
    assert expected_text == stemmed_text
