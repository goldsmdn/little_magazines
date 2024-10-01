from sklearn.decomposition import PCA
import numpy as np

def calculate_simularity_matrix(normalised_matrix):
    """calculates simularity matrix from normalised matrix"""
    normalised_array = normalised_matrix.toarray()
    normalised_array_T = np.transpose(normalised_array)
    simularity_matrix = normalised_array @ normalised_array_T
    return(simularity_matrix)

def pca_reduction(similarity_matrix, n_components):
    """calculates pca from simularity matrix and number of components"""
    one_min_sim = 1 - similarity_matrix
    model = PCA(n_components)
    pos = model.fit_transform(one_min_sim)
    x_pos, y_pos = pos[:, 0], pos[:, 1]
    return (x_pos, y_pos)