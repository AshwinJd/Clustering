# tf-idf Vectorization:

Before we go into depth of tf-idf vectorization, a little background on tf-idf weighting metric.

#### Term frequency(tf):

The term frequency is simply the number of times a term occurs in a particular document. It is measure of scoring a term in a document. The log based term frequency metric is the following:

![Log Based Term frequency](https://github.com/CrossDomainCollaborativeFiltering/Clustering/blob/master/tf.PNG) 

The term frequency matching scoring: 

![Term frequency matching score](https://github.com/CrossDomainCollaborativeFiltering/Clustering/blob/master/tfMatchingScore.PNG) 

The term frequency matching score tells us the rank of a query term in a document such that the query term actually exists in the document. i.e. q (intersection) d is not empty.

### Inverse Document Frequency(idf):

The document frequency is the number of documents in the collection where the term occurs. It is an important mertic as it gives priority to terms occur only sparsly in the document. The collection frequency or the number of times a term appears in the entire collection could been a good metric however as it turns out it is actually not. To accurately measure the sparsity of a term therefore it is important to mesaure the number of documents the term occurs in and inverting that can give us a good measure of the rare terms in our document and hence the terms that carry more relevance and hence more weight.

![The log based inverse document frequency](https://github.com/CrossDomainCollaborativeFiltering/Clustering/blob/master/idf.PNG)

### tf-idf weighing:

The tf-idf weighing takes care of both the more frequent terms and the rare terms in a collection considering rare terms or terms occuring in less number of documents but more often in a single document should have more weight and should rank higher than the ones which are either too less in a document or spread over large number of documents.

![tf-idf weighing scheme](https://github.com/CrossDomainCollaborativeFiltering/Clustering/blob/master/tf-idf.PNG)

Therefore in general for a query phrase or a set of query terms:

![tf-idf query scoring](https://github.com/CrossDomainCollaborativeFiltering/Clustering/blob/master/tfidfQueryScoring.PNG) 

## Vector Space Model(VSM):

In Information retrieval and Text mining vector space model is a widely used tool to cluster similar terms in a collection together and perform other operations on them.


