from sklearn.decomposition import PCA
import numpy as np

def pca_reduction(similarity_matrix: np.array, n_components: int):
    """Calculates pca from simularity matrix and number of components
    
    Parameters
    ----------
    similarity_matrix : array
        A matrix containing the similarity between different data points
    n_components : int
        An integer showing the number of dimensions required

    Returns
    -------
    x_pos: array
        The x positions of the points in the reduced dimensionality space
    y_pos: array
        The y positions of the points in the reduced dimensionality space
    """
    distance_matrix = 1 - similarity_matrix
    model = PCA(n_components)
    pos = model.fit_transform(distance_matrix)
    x_pos, y_pos = pos[:, 0], pos[:, 1]
    return (x_pos, y_pos)