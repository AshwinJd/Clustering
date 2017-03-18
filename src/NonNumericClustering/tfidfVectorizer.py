"""
CountVectorizer module in the package: sklearn.feature_extraction.text is used for tfidf vectorization.
In both datasets this module would be used for vectorization of non-numeric data
"""
"""
here remember that we need to separate 3 rows: id, imdbId and tagId, these rows are tfidf vectorizable as their
numeric values are not sensible for comparison.
So in the list these are indices:  0, 2, 31 

Few values to be taken for tfield: year(5), actorID(22), actorName(23), country(25), genre(26), location1(27),
location2(28), location3(29), location4(30), directorName(34),   
"""

import csv
import math
from scipy import sparse
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
v=CountVectorizer()

"""
Each movie will be a document in this model: The non-numeric data columns will be converted to paragraphs of terms and 
each such document will be stored in a list
"""
VALID_NONLIST_INDICES=[]
VALID_LIST_INDICES=[23,25,26,27,28,29,30,34]
# VALID_LIST_INDICES=[26,34]
# VALID_LIST_INDICES=[1]
# VALID_INDICES=[26]

class MovieLensClustering:
    
    def __init__(self):
        # the keys will be the ids of the movies
        self.documents={}
        

    def openFile(self, fileName):
        
        csvFile=open(fileName, newline="")
        reader=csv.reader(csvFile)
        return reader
    
    def stringToList(self, s): # this is a hack: avoid as far as possible
         
        s=s.strip('[')
        s=s.strip(']')
        # print(s)
        s=s.strip("'")
        # print(s)
        return s.split("', '")

    # def vectorNormalizer(self, termDocArray):
    #     sum=0
    #     for i in range(len(termDocArray)):
    #         for j in termDocArray[i]:
    #             sum+=(j*j)
    #         length=math.sqrt(sum)
    #         sum=0
    #         try:
    #             termDocArray[i]=termDocArray[i]/length
    #         except Exception:
    #             print("length : "+str(length))

    #     return termDocArray

    def makeDocuments(self, fileReader):
        
        reader=iter(fileReader)
        next(reader)
        for row in reader:
            
            countCol=0
            id=row[0]
            self.documents[id]=''
            
            # returns one row from table at a time
            for value in row:
                
                # refers to each value from the row which is a list
                if countCol in VALID_NONLIST_INDICES:
                    # the value is not a list
                    self.documents[id]+=' '+value

                elif countCol in VALID_LIST_INDICES:
                    # the value is actaully a string that needs to be converted to a list
                    l=self.stringToList(value)
                    for element in l:
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

        check=0
        for key in self.documents:
            
            if check==0:
                check+=1
                print(self.documents[key])
            
            trainSet.append(self.documents[key])
            

        # trainSet prepared
        
        # converting to term document matrix

        termDocMatrix=v.fit_transform(trainSet)

        # DEBUG: 
        # print(v.get_feature_names())
        # print("termDocMatrix: row1: ")
        # print(termDocMatrix.todense()[0])

        # import sys
        # sys.exit()
        """
        # TFIDF Vectorization
        tfidf=TfidfTransformer(norm='l2') 

        # Euclidean normalization: very simply converts to unit vectors

        tfidf.fit(termDocMatrix)

        tfidfMatrix=tfidf.transform(termDocMatrix)
        """

        # termDocArray=termDocMatrix.toarray()
        # termDocArray=self.vectorNormalizer(termDocArray) 
        # termDocMatrix=sparse.csr_matrix(termDocArray)

        # DEBUG
        # tfidfMatrix=tfidfMatrix.toarray()
        # sum=0
        # count=0
        # for i in tfidfMatrix:
        #     # print(type(i))
        #     count+=1
        #     for j in i:
        #         # print(type(j))
        #         sum+=(j*j)
            
        #     print(math.sqrt(sum))
        #     sum=0
        #     if count==50:
        #         import sys
        #         sys.exit()

        return termDocMatrix


# use the following method when running from same directory as the file itself

def prepareVectors():

    obj=MovieLensClustering()
    fileReader=obj.openFile('../MovieLens/ResultMovieDataSet.csv')
    obj.makeDocuments(fileReader)
    return obj.vectorize()

# run this file when running from root directory src

# def prepareVectors():
    
#     obj=MovieLensClustering()
#     fileReader=obj.openFile('MovieLens/ResultMovieDataSet.csv')
#     obj.makeDocuments(fileReader)
#     return obj.vectorize()

# DEBUG
# def main():
#     obj=MovieLensClustering()
#     fileReader=obj.openFile('../MovieLens/ResultMovieDataSet.csv')
#     obj.makeDocuments(fileReader)
#     obj.vectorize()

# if __name__=="__main__":
#     main()