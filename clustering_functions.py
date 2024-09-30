#from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import numpy as np

def calculate_simularity_matrix(normalised_matrix):
    normalised_array = normalised_matrix.toarray()
    normalised_array_T = np.transpose(normalised_array)
    simularity_matrix = normalised_array @ normalised_array_T
    return(simularity_matrix)

#def get_cluster_kmeans(X, num_clusters):
#    model = KMeans(n_clusters = num_clusters)
#    model.fit(X)
#    #cluster_list = km.labels_.tolist()
#    model_predict = model.predict(X)
#    return model_predict

def pca_reduction(similarity_matrix, n_components):
    one_min_sim = 1 - similarity_matrix
    model = PCA(n_components)
    pos = model.fit_transform(one_min_sim)
    x_pos, y_pos = pos[:, 0], pos[:, 1]
    return (x_pos, y_pos)