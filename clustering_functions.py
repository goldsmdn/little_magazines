from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import cosine_similarity

def calculate_simularity_matrix(X):
    """Calculates simularity matrix"""
    simularity_matrix = cosine_similarity(X)
    return(simularity_matrix)

def pca_reduction(similarity_matrix, n_components):
    """Calculates pca from simularity matrix and number of components"""
    distance_matrix = 1 - similarity_matrix
    model = PCA(n_components)
    pos = model.fit_transform(distance_matrix)
    x_pos, y_pos = pos[:, 0], pos[:, 1]
    return (x_pos, y_pos)