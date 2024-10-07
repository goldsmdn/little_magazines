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