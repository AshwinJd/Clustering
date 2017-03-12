## tf-idf Vectorization:

Before we go into depth of tf-idf vectorization, a little background on tf-idf weighting metric.

#### Term frequency(tf):

The term frequency is simply the number of times a term occurs in a particular document. It is measure of scoring a term in a document. The log based term frequency metric is the following:

[Log Based Term frequency]() 

The term frequency matching scoring: 

[Term frequency matching score]() 

The term frequency matching score tells us the rank of a query term in a document such that the query term actually exists in the document. i.e. q (intersection) d is not empty.