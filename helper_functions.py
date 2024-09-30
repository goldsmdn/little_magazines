def make_category_list(index_dict):
    category_list = []
    for item in index_dict.values():
        category = item['Category']
        if category not in category_list:
            category_list.append(category)
    return(category_list)

def make_long_text(item, show_category=False):
    if show_category:
        category = item['Category']
    title = item['Short_Title']
    author = item['Short_Author']
    year = item['Year']
    if show_category:
        text = f'{category}-{title}-{author}({year})'
    else:
        text = f'{title}-{author}({year})'
    return(text)

def make_book_name_list(index_dict):
    book_names_list = []
    for item in index_dict.values():
        text = make_long_text(item, show_category=True)
        book_names_list.append(text)
    return(book_names_list)


