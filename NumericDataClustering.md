# Numeric Data Clustering

Numeric Data Clustering will actually be far simpler as there is no need for any type of tfidf vectorization. In case of Numeric Data Clustering we can simply use K means clustering to cluster the movies based on their numeric parameters.

#### Clustering of Movies using Numeric Data

- **Step 1**: The numeric data can be under a VSM where the vectors are the movies and the dimensions of each vector are essentially the numeric data parameters(for each dataset)

- **Step 2**: Apply K-Means clustering for on the whole dataset on only the numeric parameters.

