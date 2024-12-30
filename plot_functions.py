from scipy.cluster.hierarchy import ward, dendrogram

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

from helper_functions import make_book_name_list, make_long_text
from helper_functions import make_category_list

import numpy as np

def make_color_list():
    """Returns a color list to use in the scatter plots"""
    color_dict = mcolors.XKCD_COLORS
    color_list = []
    for item in color_dict.values():
        color_list.append(item)
    return(color_list)

def vector_plot(X, feature_names):
    """returns vectors and a unit circle"""
    num_points = X.shape[0]
    if num_points > 4:
        raise Exception(f'Not enough colours for {num_points} points')
    if len(feature_names) != 2:
        raise Exception(f'{num_points} features names received, can only plot in two dimensions')
    color_list = ['red', 'blue', 'green','orange', 'brown']

    for i in range(0, num_points):
        x_v, y_v = X[i,0], X[i,1] 
        color=color_list[i]
        label = 'Corpus' + str(i+1)
        plt.scatter(x_v, y_v, color=color, label=label)
        plt.arrow(0, 0, x_v, y_v, head_width=0.05, color=color)
    plt.legend(loc = 'upper right', shadow=True, title="Corpus",)
    plt.xlabel(feature_names[0])
    plt.ylabel(feature_names[1])
    plt.title(f'Vectors found from the {num_points} example corpii')
    start, stop, step = 0, 1, 0.0001
    x_c = np.arange(start, stop, step)
    y_c = np.sqrt(1 - np.square(x_c))
    plt.plot(x_c, y_c, color = 'black')

def plot_matrix(matrix, path):
    """Plots the similarity matrix"""
    plt.matshow(matrix)
    plt.title('Document Similarity Matrix')
    plt.xlabel('Document ID')
    plt.ylabel('Document ID')
    filename = path + 'Similarity_matrix.png'
    plt.savefig(filename, facecolor='white')

def plot_dendogram(similarity_matrix, index_dict, path):
    """Plots a dendogram from the simularity matrix and a dictionary read from index.csv"""
    book_names_list = make_book_name_list(index_dict)
    linkage_matrix = ward(similarity_matrix) 
    # Define the linkage_matrix using ward clustering pre-computed distances

    mpl.rcParams['lines.linewidth'] = 5

    fig, ax = plt.subplots(figsize=(15, 20)) # Set size
    ax = dendrogram(linkage_matrix, orientation="right", labels=book_names_list)

    plt.tick_params(
        axis= 'x',
        which='both',
        bottom='off',
        top='off',
        labelbottom='off',
        length = 25)
    plt.tick_params(
        axis= 'y',
        which='both',
        bottom='off',
        top='off',
        labelbottom='off',
        labelsize = 20)
    plt.tick_params(width=50, length = 10)
    plt.tight_layout() # Show plot with tight layout
    filename = path + 'Dendogram.png'
    plt.tight_layout()
    plt.savefig(filename, facecolor='white')

def plot_scatter(index_dict, x, y, offset, path, annotate=True):
    """Plots scatter plot

    Parameters
    ----------

    index_dict : dict
        An index dictionary read from the index.csv file.
    x : list of floats
        x co-ordinate of each point
    y : list of floats
        y co-ordinate of each point
    offset : float
        distance of each annotation from the data point
    path : str
        filepath for plots
    annotate : bool
        True if data points are to be annotated
    """
    marker_list = ['o', 'v', '^', '<', '>', '+', '*', 's','x']
    # rotate through this list to select distinct markers
    category_list = make_category_list(index_dict)
    color_list = make_color_list()
    for i, category in enumerate(category_list):
        #loop by categories and make a separate plot for each category
        marker = marker_list[i % len(marker_list)]
        #choose a new marker
        x_list = []
        y_list = []
        text_list = []
        for key, item in index_dict.items():
            if item['Category'] == category:
                x_list.append(x[key])
                y_list.append(y[key])
                if annotate == True:
                    text = make_long_text(item)
                    text_list.append(text)
                color = color_list[i]
                #next color - there are many in the list so no risk of index error
        plt.scatter(x_list, y_list, color=color, label=category, marker=marker)
        #rotating through markers and colors for each category
        if annotate == True:
            #add annotations for each data point.  Becomes messy if more that about
            #ten data points
            for i, txt in enumerate(text_list):
                plt.annotate(txt, 
                            (x_list[i],y_list[i]), 
                            xytext =(x_list[i]+offset,y_list[i]+offset)
                            )  
    plt.title('Manifesto Map')
    plt.legend(loc = 'upper right', bbox_to_anchor=(1.35, 0.9), shadow=True, title="Category",)
    #need legend outside plot for clarity
    filename = path + 'Manifesto_map.png'
    plt.tight_layout()
    plt.savefig(filename,facecolor='white' )