from text_functions import read_text, read_index
from text_functions import read_text_files

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

from pathlib import Path
import numpy as np

ENCODING = 'utf-8-sig'
TEST_DATA_PATH = 'test_data1'

def test_read_text():
    """Unit test - reading text functionality"""
    data_file = 'test_data1.txt'
    file_path = Path(TEST_DATA_PATH).joinpath(data_file)
    text = read_text(file_path, ENCODING)
    expected_text = ' test data more data'
    assert expected_text == text

def test_full_process():
    """Test end process from index read to corpus production"""
    data_file = 'test_index.csv'
    file_path = Path(TEST_DATA_PATH).joinpath(data_file)
    index = read_index(file_path, ENCODING)
    corpus = read_text_files(index, ENCODING, TEST_DATA_PATH)
    expected_corpus = [' test data more data', ' test data more data words']
    assert expected_corpus == corpus

def test_count_vectoriser():
    """check vectoriser against unit test in sklearn documentation"""
    path = 'test_data2/'
    filename = path + 'test_index.csv'
    index = read_index(filename, ENCODING)
    corpus = read_text_files(index, ENCODING, path)
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(corpus)
    array = X.toarray()
    expected_array = np.array([
                     [0, 1, 1, 1, 0, 0, 1, 0, 1,],
                     [0, 2, 0, 1, 0, 1, 1, 0, 1,],
                     [1, 0, 0, 1, 1, 0, 1, 1, 1,],
                     [0, 1, 1, 1, 0, 0, 1, 0, 1,],
                    ])   
    assert expected_array.all() == array.all()

def test_simularity_matrix_calculation():
    """check the calculation of the simularity matrix"""
    X = np.array([
                [0, 1, 1, 1, 0, 0, 1, 0, 0],
                [1, 2, 3, 2, 1, 1, 2, 0, 1],
                [1, 0, 0, 0, 1, 0, 1, 1, 0],
                [0, 1, 0, 1, 0, 0, 1, 0, 1],
            ]) 

    expected_array = np.array([
        [1, 0.9, 0.25, 0.75],
        [0.9, 1, 0.4, 0.7],
        [0.25, 0.4, 1, 0.25],
        [0.75, 0.7, 0.25, 1]
    ])

    simularity_matrix = cosine_similarity(X)

    assert expected_array.all() == simularity_matrix.all()