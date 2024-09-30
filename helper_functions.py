def make_category_list(index_dict):
    """Makes a list of categories from the index to plot graphs

    Parameters
    ----------
    index_dict : dict
        Index dictionary read from index.csv

    Returns
    -------
    category_list : list
        List of categories to use in plots
    """
    category_list = []
    for item in index_dict.values():
        category = item['Category']
        if category not in category_list:
            category_list.append(category)
    return(category_list)

def make_long_text(item, show_category=False):
    """Makes a long text to use in plots

    Parameters
    ----------
    item : dict
        an item from the index dictionary read from
        index.csv

    Returns
    -------
    text : string
        Concatentation of certain fields in the index dictorionary
    """

    title = item['Short_Title']
    author = item['Short_Author']
    year = item['Year']
    if show_category:
        #used for dendogram
        category = item['Category']
        text = f'{category}-{title}-{author}({year})'
    else:
        #shorter version intended for scatter plot
        text = f'{title}-{author}({year})'
    return(text)

def make_book_name_list(index_dict):
    """Makes a list of book names to use in plots
    by looping round the index dictionary read from index.csv

    Parameters
    ----------
    index_dict : dict
        Index dictionary read from index.csv

    Returns
    -------
    book_names_list : list
        List of book names to use in plots
    """
    
    book_names_list = []
    for item in index_dict.values():
        text = make_long_text(item, show_category=True)
        book_names_list.append(text)
    return(book_names_list)


