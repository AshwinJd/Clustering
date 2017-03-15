"""
CountVectorizer module in the package: sklearn.feature_extraction.text is used for tfidf vectorization.
In both datasets this module would be used for vectorization of non-numeric data
"""
import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
v=CountVectorizer()

"""
Each movie will be a document in this model: The non-numeric data columns will be converted to paragraphs of terms and 
each such document will be stored in a list
"""

class MovieLensClustering:
    
    def __init__(self):
        # the keys will be the ids of the movies
        self.documents={}

    def openFile(self, fileName):
        
        csvFile=open(fileName, newline="")
        reader=csv.reader(csvFile)
        return reader
    
    def makeDocuments(self, fileReader):
        
        reader=iter(fileReader)
        next(reader)
        for row in reader:
            
            """
            here remember that we need to separate 3 rows: id, imdbId and tagId, these rows are tfidf vectorizable as their
            numeric values are not sensible for comparison.
            So in the list these are indices:  0, 2, 31 
            """

            countCol=0
            id=row[0]
            self.documents[id]=''
            # returns one row from table at a time
            for value in row:
                
                # refers to each value from the row which is a list
                if type(value) == str:
                    # the value is not a list
                    if not value.isdigit():
                        # the value is non-numeric
                        self.documents[id]+=' '+value
                    elif  countCol==0 or countCol==2 or countCol==31:
                        self.documents[id]+=' '+value
                else:
                    # the value is a list
                    for element in value:
                        if not value.isdigit():
                            self.documents[id]+=' '+element
                        elif countCol==0 or countCol==2 or countCol==31:
                            self.documents[id]+=' '+element
                countCol+=1

        
    # def verifyTrainData(self):
    #     """
    #     trainData is the dictionary of all documents
    #     """
    #     for key in self.documents:
    #         for value in self.documents[key]:
    #             # value should be a string containing all the terms for one document

    #             #TODO

    def vectorize(self):

        """
        term frequency vectorization is done by method 
        """

        trainSet=[]
        for key in self.documents:
            
            trainSet.append(self.documents[key])

        # trainSet prepared
        
        # converting to term document matrix

        termDocMatrix=v.fit_transform(trainSet)

        tfidf=TfidfTransformer(norm='l2') 

        # Euclidean normalization: very simply converts to unit vectors

        tfidf.fit(termDocMatrix)

        tfidfMatrix=tfidf.transform(termDocMatrix)

        return tfidfMatrix


def prepareVectors():

    obj=MovieLensClustering()
    fileReader=obj.openFile('../MovieLens/ResultMovieDataSet.csv')
    obj.makeDocuments(fileReader)
    return obj.vectorize()
