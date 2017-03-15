import csv
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.preprocessing import normalize
from scipy import sparse
import numpy as np

"""
Each movie will be a document in this model: The numeric data columns will be used as each dimension of the vector space
"""
VALID_NUMERIC_LIST_INDICES=[]
VALID_NUMERIC_NONLIST_INDICES=[7,8,9,10,11,12,13,14,15,16,17,18,19,20]

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
            self.documents[id]=[]
            # returns one row from table at a time
            for value in row:
                if countCol in VALID_NUMERIC_NONLIST_INDICES:
                    if value.isdigit():
                        self.documents[id].append(float(value))
                    else:
                        try:
                            val=float(value)
                            self.documents[id].append(val)
                        except Exception:
                            self.documents[id].append(0.0)
                elif countCol in VALID_NUMERIC_LIST_INDICES:
                    # the value is a list
                    l=self.stringToList(value)
                    for element in l:
                        if element != '':
                            self.documents[id].append(float(element))
                        else:
                            self.documents[id].append(0.0)
                countCol+=1

    def getParamDocList(self):
        # returns a normalized document parameter matrix as np array
        paramDocList=[]
        # index=0
        check=0
        for key in self.documents:
            if check==0:
                check+=1
                print(self.documents[key])
            paramDocList.append(self.documents[key])
        paramDocArray=np.array(paramDocList)
        print ("type of array:"+str(type(paramDocArray)))
        return normalize(paramDocArray, norm='l2')

            
def prepare():
    obj=MovieLensClustering()
    obj.makeDocuments(obj.openFile('../MovieLens/ResultMovieDataSet.csv'))
    paramDocArray=obj.getParamDocList()
    return sparse.csr_matrix(paramDocArray)
