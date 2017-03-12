# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 14:12:25 2017

@author: riflerRick
"""
from sklearn.feature_extraction.text import CountVectorizer

v=CountVectorizer()

trainSet=["The sky is blue","The sun is bright","The sky soares high up in the sky"]

termDocumentMatrix=v.fit_transform(trainSet)

"""
The fit_transform function first learns a vocabulary dictionary of all tokens in
the raw documents and then transforms the documents to a term document matrix

So here the trainSet is
["The sky is blue","The sun is bright","The sky soares high up in the sky"]

The fit_transform finally reuturns a term document matrix in the format of 
Coordinate List(COO) i.e.  (row,column)   value(i.e. is the frequency)
                term1  term2 term3 ...
doc1=index[0]:  <freq> <freq> <freq> ...
doc2=index[1]:  <freq> <freq> <freq> ...
.
.
"""

print(t)

from sklearn.feature_extraction.text import TfidfTransformer

tfidf=TfidfTransformer(norm='l2')

"""
norm for normalization. l2 normalization simply denotes euclidean 
normalization.
"""

idf=tfidf.fit(termDocumentMatrix)

print("printing idf values:\n")

print(tfidf.idf_)

tf_idf_matrix=tfidf.transform(t)

print("printing the final tfidf matrix: \n")

print (tf_idf_matrix.todense())






