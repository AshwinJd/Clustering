# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 14:12:25 2017

@author: riflerRick
"""
class Test1:
    
    def __init__(self):
        self.dummy=0
        
    def vectorize(self):
            
        from sklearn.feature_extraction.text import CountVectorizer

        v=CountVectorizer()

        trainSet=["The sun in the sky is bright","We can see the shining sun, the bright sun"]

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


class Test2:
    
    def __init__(self):
        self.dummy=0
        
    def vectorize(self):
    
        from sklearn.feature_extraction.text import CountVectorizer

        v=CountVectorizer()

        from sklearn.feature_extraction.text import TfidfTransformer

        tfidf=TfidfTransformer(norm='l2')

        trainSet=["The sky is blue","The sun is bright"]

        freq_term_matrix=v.fit_transform(trainSet)

        # testSet=["The sun in the sky is bright","We can see the shining sun, the bright sun"]

        # freq_term_matrix=v.transform(testSet)

        print("frequency term matrix(also: term document matrix):")
        print(freq_term_matrix.todense())

        # now we need to prepare the idf matrix, the fit method learns the freq_term_matrix

        tfidf.fit(freq_term_matrix)

        tfidf_matrix=tfidf.transform(freq_term_matrix)

        print("Final tfidf matrix- These are the normalized vector components: ")
        print(tfidf_matrix.todense())


class KMeansTest:
    
    def cluster(self):
        from sklearn.cluster import KMeans
        from scipy import sparse
        import numpy as np

        data=np.array([[1,2],[2,2.5],[2,3],[2.5,1],[3,2],[3.5,1],[3.5,2.5],[4,3]])
        dataSparse=sparse.csr_matrix(data)

        print("printing sparse matrix:")
        print(dataSparse.todense())

        kmeans=KMeans(n_clusters=3, random_state=0).fit(dataSparse)

        testPoints=np.array([[1,2],[2,3],[3.5,2.5],[4,3.5]])

        print(kmeans.predict(testPoints))

def main():
    # obj=Test2()
    # obj.vectorize()
    obj=KMeansTest()
    obj.cluster()

if __name__=="__main__":
    main()



