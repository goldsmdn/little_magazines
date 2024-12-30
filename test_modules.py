from text_functions import read_text, read_index
from text_functions import read_text_files

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

from pathlib import Path
import numpy as np

ENCODING = 'utf-8-sig'
DATA_PATH = 'data'
TEST_DATA_PATH1 = 'test_data1'
TEST_DATA_PATH2 = 'test_data2'

def test_read_text():
    """Unit test - reading text functionality"""
    data_file = 'test_data1.txt'
    file_path = Path(DATA_PATH).joinpath(TEST_DATA_PATH1).joinpath(data_file)
    text = read_text(file_path, ENCODING)
    expected_text = ' test data more data'
    assert expected_text == text

def test_full_process():
    """Test end process from index read to corpus production"""
    data_file = 'test_index.csv'
    data_path = Path(DATA_PATH).joinpath(TEST_DATA_PATH1)
    file_path = Path(data_path).joinpath(data_file)
    index = read_index(file_path, ENCODING)
    corpus = read_text_files(index, ENCODING, data_path)
    expected_corpus = [' test data more data', ' test data more data words']
    assert expected_corpus == corpus

def test_count_vectoriser():
    """check vectoriser against unit test in sklearn documentation"""
    data_file = 'test_index.csv'
    data_path = Path(DATA_PATH).joinpath(TEST_DATA_PATH2)
    file_path = Path(data_path).joinpath(data_file)
    index = read_index(file_path, ENCODING)
    corpus = read_text_files(index, ENCODING, data_path)
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

def test_similarity_matrix_calculation():
    """check the calculation of the similarity matrix"""
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

    similarity_matrix = cosine_similarity(X)

    assert expected_array.all() == similarity_matrix.all()