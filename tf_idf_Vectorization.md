# tf-idf Vectorization:

Before we go into depth of tf-idf vectorization, a little background on tf-idf weighting metric.

### Term frequency(tf):

The term frequency is simply the number of times a term occurs in a particular document. It is measure of scoring a term in a document. The log based term frequency metric is the following:

![Log Based Term frequency](https://github.com/CrossDomainCollaborativeFiltering/Clustering/blob/master/assets/tf.PNG) 

The term frequency matching scoring: 

![Term frequency matching score](https://github.com/CrossDomainCollaborativeFiltering/Clustering/blob/master/assets/tfMatchingScore.PNG) 

The term frequency matching score tells us the rank of a query term in a document such that the query term actually exists in the document. i.e. q (intersection) d is not empty.

### Inverse Document Frequency(idf):

The document frequency is the number of documents in the collection where the term occurs. It is an important mertic as it gives priority to terms occur only sparsly in the document. The collection frequency or the number of times a term appears in the entire collection could been a good metric however as it turns out it is actually not. To accurately measure the sparsity of a term therefore it is important to mesaure the number of documents the term occurs in and inverting that can give us a good measure of the rare terms in our document and hence the terms that carry more relevance and hence more weight.

![The log based inverse document frequency](https://github.com/CrossDomainCollaborativeFiltering/Clustering/blob/master/assets/idf.PNG)

### tf-idf weighting:

The tf-idf weighting takes care of both the more frequent terms and the rare terms in a collection considering rare terms or terms occuring in less number of documents but more often in a single document should have more weight and should rank higher than the ones which are either too less in a document or spread over large number of documents.

![tf-idf weighing scheme](https://github.com/CrossDomainCollaborativeFiltering/Clustering/blob/master/assets/tf-idf.PNG)

Therefore in general for a query phrase or a set of query terms:

![tf-idf query scoring](https://github.com/CrossDomainCollaborativeFiltering/Clustering/blob/master/assets/tfidfQueryScoring.PNG) 

## Vector Space Model(VSM):

In Information retrieval and Text mining vector space model is a widely used tool to cluster similar terms in a collection together and perform other operations on them.

The representation of a set of documents as a vector in a common vector space is known as the vector space model and is fundamental to a host of information retrival operations ranging from scoring documents from a query, document classification and document clustering.

We denote the vector V derived from a document d with one component in the vector for each dictionary term. Unless otherwise specified, the reader may simply assume that components are computed using the tf-idf weighting scheme. The set of documents in a collection then may be viewed as a set of vectors in a vector space where each dimension or each axis of each of the vectors represent one query term.

### Computing document similarities:

Once all documents are represented in the form of vectors, a similarity metric can be formulated in order to cluster documents of similar types.
 
The most naive approach would be to measure simlarity based on euclidean distance however that would not necessarily be a good measure. Here's how:

There can be 2 documents that are similar in a major way as they have equal proportions of terms in them however one has more **number** of terms in them than the other. Euclidean distance would classify them as distant documents however in reality they would be very similar.

The standard similarity is a **Cosine Similarity**:

Given by: ![Cosine Similarity](https://github.com/CrossDomainCollaborativeFiltering/Clustering/blob/master/assets/cosineSim.PNG)

This essentially computes a far in terms of angle is one document from another. The lower the angle the higher the consine and hence higher the similarity.

As we all know the dot product of 2 vectors is the scalar product of their magnitudes multiplied with the cosine of the angle between them. So if we wanna get the cosine all we need to do is the dot product divided by the scalar product of their magnitudes.

The following picture gives us an idea of how a query document can be used to figure our documents close to it.

![VSM Model](https://github.com/CrossDomainCollaborativeFiltering/Clustering/blob/master/assets/vsm.PNG)

Here gossip and jealous are the only terms and d1 and d2 are the 2 documents. q is the query.

The more general way to think about cosine similarity is that we are firt normalizing the vectors and then computing the dot product in which case the magnitudes of the vectors are 1.

## Application of VSM in Movies Datasets:
##### for vectorization of each movie in the dataset

In a movie based dataset the record of each movie can be considered as a  document and the dimensions of the vector becomes the tf-idf scores for the terms that occur in a document. 

As a reference to how this concept can be used check out: [this link](http://blog.christianperone.com/2011/09/machine-learning-text-feature-extraction-tf-idf-part-i/)

#### Python implementation:

Scikit learn library has modules to do tfidf vectorization for us and thats what we are gonna use.

Lets say that we have the following training set:

trainSet=["The sky is blue","The sun is bright"]

Based on the terms we can build a term document matrix in the following:

doc1: The sky is blue

doc2: The sun is bright

|  | Term1 | Term2 | Term3 | Term4 | 
|---| --- | --- | --- | --- |
| Doc 1 | freq | freq | freq | freq |
| Doc 2 | freq | freq | freq | freq |
| Doc 3 | freq | freq | freq | freq |

Each frequency actually represents the frequency of the terms in the corresponding document.

Here is a bit of code that can actually create a term document matrix for a particular dataset of documents

```
from sklearn.feature_extraction.text import CountVectorizer

v=CountVectorizer()

trainSet=["The sky is blue","The sun is bright","The sky soares high up in the sky"]

termDocumentMatrix=v.fit_transform(trainSet)
print(termDocumentMatrix)
```
The output of the following document is:

```
  (0, 0)        1
  (0, 4)        1
  (0, 5)        1
  (0, 8)        1
  (1, 1)        1
  (1, 7)        1
  (1, 4)        1
  (1, 8)        1
  (2, 3)        1
  (2, 9)        1
  (2, 2)        1
  (2, 6)        1
  (2, 5)        2
  (2, 8)        2
```

The above output actually represents the term document matrix in a form called the coordinate list notation. The representation is (row, column)  value.

In a similar fashion there are modules that help us convert whole collection of documents into tf-idf matrices.
The following code computes the idf for a term document matrix.

```
from sklearn.feature_extraction.text import TfidfTransformer

idf=TfidfTransformer(norm='l2')

idf.fit(termDocumentMatrix)

"""
here the parameter termDocumentMatrix is basically the term document matrix variable.
"""

```
Now the fit() method has calculated the idf for the matrix, lets transform this resulting matrix to the tfidf weighted matrix.

```

tf_idf_matrix=tfidf.transform(t)

print("printing the final tfidf matrix: \n")

print (tf_idf_matrix.todense())
```
The final matrix is the one printed in that last line. That final matrix is the tf idf matrix...Try these codes out in your system

### Clustering:

Now after the tfidf Vectorization