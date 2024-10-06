# Mapping of texts

## Overview
It is useful to map out texts, for example, books and articles, so that text that are close in meaning are close in the map.  This might help identify hidden connections between the maps.  

## Notebooks
This reposititory currently contains a [Jupyter notebook](manifesto_map.ipynb) for mapping out texts based on simularities between the words that they contain.  The texts were featured in the 2015 film installation [Manifesto](https://en.wikipedia.org/wiki/Manifesto_\(2015_film\)) written, produced and directed by Julian Rosefeldt, in which Cate Blanchett reads out a series of manifestos.  The manifestos are grouped into a number of classifications, for example, Situationism, Futurism and Dadaism.  The aim of the work is to map out the different manifestos, and see how that mapping corresponds to the mappings given.  The [notebook](manifesto_map.ipynb) contains furthr documentation.  Futher notebooks are planned later.

## Unit testing
A GitHub action automatically executes a series of Unit Tests on each push.

## Further documentation
For documentation of the relevant Python modules please see [this link](https://goldsmdn.github.io/little_magazines/).  This documentation is automatically generated by [Sphinx](https://www.sphinx-doc.org/en/master/).  A GitHub action generates the Sphinx documentation and moves it to a branch 'gh-pages', from which it is automatically published by a standard GitHub actions.  Jekyll is not used, so to stop error being thrown the GitHub action makes a '.nojekyll' file in the root of 'gh-pages'.

## Pre-requisites
The Jupyter notebook with Python 3.12.  You will need to have the following Python modules and package installed:
 - [CSV](https://docs.python.org/3/library/csv.html) handles CSV file loads
 - [itertools](https://docs.python.org/3/library/itertools.html) provides iteration tools including a counter
 - [re](https://docs.python.org/3/library/re.html) handles regular expressions
 - [nltk](https://www.nltk.org/) Natural Language Toolkit provides stemming functionality
 - [sklearn](https://scikit-learn.org/stable/) provides "off-the shelf" Machine Learning functionality including Principal Component Analysis (PCA) and vectorisation techniques
 - [numpy](https://docs.python.org/3/library/numeric.html) provides fast array manipulation
 - [matplotlib](https://matplotlib.org/) used for plotting
 - [scipy](https://scipy.org/) used to make a dendogram

 I simply installed [Anaconda](https://www.anaconda.com/) v2.6.3 and used the base environment, which contain all of the dependencies.  

 ## Installation of the repository locally
Clone the repository to a suitable location on your computer using the following command:
```
git clone https://github.com/goldsmdn/little_magazines

``` 
## Running the notebooks
To run the 'Manifesto map' notebook, open a terminal window and navigate to the folder containing the repository.  Then run the following command:

```
jupyter notebook manifesto_map.ipynb

```
Alternatively you can run in the VS code development environment, setting the Python interpreter to Base.

## Contributing
Contributions to the repository are very welcome.  Please raise an issue if you have any problems, and feel free to contact me.

## Acknolwedgements
The 'Manifesto Map' notebook was based on a 2018 GitHub [repository](https://github.com/utkuozbulak/unsupervised-learning-document-clustering) by Utku Ozbulak.  This was recoded to use the up to date SciKit Learn functionality. 

Two blogs by Neri Van Otten were very helpful:
 - [How To Implement Bag-Of-Words In Python](https://spotintelligence.com/2022/12/20/bag-of-words-python/) 2018 
 - [Tutorial On How To Implement Document Clustering In Python With K-mean](https://spotintelligence.com/2023/01/16/document-clustering-in-python/) 2023