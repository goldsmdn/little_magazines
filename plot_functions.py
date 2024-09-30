from scipy.cluster.hierarchy import ward, dendrogram
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

from helper_functions import make_book_name_list, make_long_text
from helper_functions import make_category_list

def make_color_list():
    color_dict = mcolors.XKCD_COLORS
    color_list = []
    for item in color_dict.values():
        color_list.append(item)
    return(color_list)

def plot_matrix(matrix):
    plt.matshow(matrix)
    plt.title('Document Similarity Matrix')
    plt.xlabel('Document ID')
    plt.ylabel('Document ID')
    plt.savefig('Simularity_matrix.png', facecolor='white')

def plot_dendogram(similarity_matrix, index_dict):
    book_names_list = make_book_name_list(index_dict)
    linkage_matrix = ward(similarity_matrix) # Define the linkage_matrix using ward clustering pre-computed distances
    mpl.rcParams['lines.linewidth'] = 5

    fig, ax = plt.subplots(figsize=(15, 20)) # Set size
    ax = dendrogram(linkage_matrix, orientation="right", labels=book_names_list);

    plt.tick_params(\
        axis= 'x',
        which='both',
        bottom='off',
        top='off',
        labelbottom='off',
        length = 25)
    plt.tick_params(\
        axis= 'y',
        which='both',
        bottom='off',
        top='off',
        labelbottom='off',
        labelsize = 20)
    plt.tick_params(width=50, length = 10)
    plt.tight_layout() # Show plot with tight layout
    plt.savefig('Dendogram.png', facecolor='white')

def plot_scatter(index_dict, x, y, offset, annotate=True):
    marker_list = ['o', 'v', '^', '<', '>', '+', '*', 's','x']
    # rotate through this list
    category_list = make_category_list(index_dict)
    color_list = make_color_list()
    for i, category in enumerate(category_list):
        marker = marker_list[i % len(marker_list)]
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
        plt.scatter(x_list, y_list, color=color, label=category, marker=marker)
        if annotate == True:
            for i, txt in enumerate(text_list):
                plt.annotate(txt, 
                            (x_list[i],y_list[i]), 
                            xytext =(x_list[i]+offset,y_list[i]+offset), 
                            #arrowprops=dict(arrowstyle='->')
                            )  
    plt.title('Manifesto Map')
    plt.legend(loc = 'upper right', bbox_to_anchor=(1.35, 0.9), shadow=True, title="Category",)
    plt.savefig('Manifesto_map.png',facecolor='white' )