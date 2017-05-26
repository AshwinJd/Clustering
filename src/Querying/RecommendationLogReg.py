"""
The following program will be used to recommend based on a Machine Learning approach. The user enters a userid,
The userid is checked from the user-movies file and the corresponding movies are taken and the data is split into two sets:
1. The training data
2. The test data
Movies rated from 2.5 and below are taken as 'not liked' and movies rated >2.5 are rated as 'liked'. For logistic regression the features in this case would simply be the tf(term frequency) values. So for every training of the data a tfidf score would be calculated and accordingly will be used for recommendation. It is also more effective to keep the trained model for a particular user for future calculations.
Accordingly a 2 class classifier is built.
Purpose:
1. Evaluation
For evaluation of the recommender system a simple appraoch would be to simply use 2/3 of the data for training and 1/3rd of the data for testing purpose.
2. Recommending movies not watched by the current user
For movies not watched by the current user we can use the entire data of the user for purposes of training and then on separate movies not watched by the user we can say whether the user would like it or not.
"""
import csv
import math
from scipy import sparse
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import linear_model
v=CountVectorizer(stop_words=['The','a'])

USER_MOVIE_FILENAME="../../../dataSets/movieLens/user_ratedmovies.csv"
MOVIE_FILENAME="../MovieLens/ResultMovieDataSetClone.csv"
VALID_LIST_INDICES=[24,27,35]

def openFile(fileName):
    csvFile=open(fileName, newline="")
    reader=csv.reader(csvFile)
    return reader

def stringToList(s): # this is a hack: avoid as far as possible
         
        s=s.strip('[')
        s=s.strip(']')
        # print(s)
        s=s.strip("'")
        # print(s)
        return s.split("', '")

# columns to be used for tf vectorization: actorName(24), genre(27), directorName(35)

class AllUsers:
    
    def __init__(self):
        self.users=[]
        self.movieID=[]
        self.ratings=[]

    def getAllUserDetails(self):
        
        csvReader=openFile(USER_MOVIE_FILENAME)
        rowIter=iter(csvReader)
        next(rowIter) # to get rid of the first row
        # users=[]
        while True:
            try:
                
                row=next(rowIter)
                self.users.append(int(row[0]))
                self.movieID.append(int(row[1]))
                self.ratings.append(float(row[2]))

            except StopIteration:   
                # StopIteration exception is reached when the iterator has iterated thorugh all the rows
                # of the csvFile
                break
    

class User:
    # all user details from the user-movie file

    def __init__(self, users, movieID, ratings):
        self.index=-1

        self.userStartIndex=-1
        self.userEndIndex=-1

        self.users=users
        self.movieID=movieID
        self.ratings=ratings

        # the following are the 2 lists that will be used directly by the other modules
        self.userRatedMovies=[] # contains the allocated movie ids (not the true movie ids)
        self.userRatings=[]

    def getUserApproxIndex(self, userID):
        
        low=0
        high=len(self.users)-1
        self.index=-1
        # index=-1
        while low <= high:
            mid=int((low+high)/2)
            if self.users[mid]==userID:
                # print("found index:"+str(mid))
                self.index=mid
                break
            elif self.users[mid]>userID:
                high=mid-1
            elif self.users[mid]<userID:
                low=mid+1

    def getUserStartIndex(self, userID):

        if self.index==-1:
            return -1
        else:
            # startIndex of the userID to be found
            i=self.index
            while i>=0:
                if userID!=self.users[i]:
                    self.userStartIndex=i+1
                    return i+1
                i-=1
            return 0

    def getUserEndIndex(self, userID):
        
        if self.index==-1:
            return -1
        else:
            # startIndex of the userID to be found
            i=self.index
            while i<len(self.users):
                if userID!=self.users[i]:
                    self.userEndIndex=i
                    return i
                i+=1
            return len(self.users)-1

        
    def getUserDetails(self, userID): # from this class only this function is called
        self.getUserApproxIndex(userID)
        if self.index==-1:
            raise Exception('Unknown user')
        startIndex=self.getUserStartIndex(userID)
        endIndex=self.getUserEndIndex(userID)
        # print("start index is:"+str(startIndex)+"\n end index:"+str(endIndex))
        userRatings=[]
        for i in range(startIndex, endIndex):
            self.userRatedMovies.append(self.movieID[i])
            self.userRatings.append(self.ratings[i])


class Document:
    # this class returns the documents for the tf vectorizer
    def __init__(self, userRatedMovies):
        
        self.userRatedMovies=userRatedMovies
        # list of allocated ids of the movies that the user had rated.
        self.documents={}

    def makeDocuments(self):
        reader=openFile(MOVIE_FILENAME)
        next(reader)
        # to skip the very first line
        for row in reader:
            countCol=0
            allocatedID=int (row[1])
            if allocatedID not in self.userRatedMovies:
                continue
            id=row[0]
            self.documents[id]=''
            
            # returns one row from table at a time
            for value in row:

                if countCol in VALID_LIST_INDICES:
                    # the value is actaully a string that needs to be converted to a list
                    l=stringToList(value)
                    
                    if countCol==24:
                        for index in range(len(l)):
                            l[index]=l[index].replace(' ','')
                    for element in l:
                        self.documents[id]+=' '+element

                countCol+=1

class TfVectorizer:
    
    def __init__(self, documents, userRatings):
        
        self.documents=documents
        self.ratings=userRatings # a list that stores all the user ratings serially
        self.labels=None
        self.trainModel=None
        self.termDocMatrix=None

    def vectorize(self):
    
        """
        term frequency vectorization is done by method 
        """

        trainSet=[]

        check=0
        for key in self.documents:
            
            # if check==0:
            #     check+=1
            #     print(self.documents[key])
            
            trainSet.append(self.documents[key])
            

        # trainSet prepared
        
        # converting to term document matrix

        self.trainModel=v.fit(trainSet)

        termDocMatrix=v.transform(trainSet)

        self.termDocMatrix=termDocMatrix
        # termDocMatrix is a scipy sparse matrix
    
    """
    This function defines the labels for the data if the rating is >2.5 it is assigned 
    """
    def defineLabels(self):
        
        for rating in self.ratings:
            if rating>2.5:
                # user has liked the movie
                self.labels.append(1)
            else:
                # user has not liked the movie
                self.labels.append(0)
        # the following is an important step
        self.labels=np.array(self.labels)
        
class SampleTfVectorizer:
    
    def __init__(self, document, trainModel):
        self.document=document
        self.trainModel=trainModel
    
    def vectorizer(self):
        trainSet=[]

        check=0
        for key in self.documents:
            
            # if check==0:
            #     check+=1
            #     print(self.documents[key])
            
            trainSet.append(self.documents[key])
            

        # trainSet prepared
        
        # converting to term document matrix

        trainedModel=v.fit(trainSet)

        termDocMatrix=v.transform(trainSet)

        # here we need to make changes to the termDocMatrix

        sampleFeatureNames=trainedModel.get_feature_names()
        trainFeatureNames=self.trainModel.get_feature_names()
        modifiedTermDocMatrix=[]
        for feature in trainFeatureNames:
            if feature not in sampleFeatureNames:
                modifiedTermDocMatrix.append(0)
            else:
                featureIndex=sampleFeatureNames.index(feature)
                modifiedTermDocMatrix.append(termDocMatrix[featureIndex])
        termDocMatrix=np.array(modifiedTermDocMatrix)
        
        return termDocMatrix
        # termDocMatrix is a scipy sparse matrix

class Recommend:

    # here both featureMatrix is a scipy sparse matrix and the labels is simply a numpy lists
    def __init__(self, featureMatrix, labels):
        self.featureMatrix=featureMatrix
        self.labels=labels
        self.logr=None

    def trainModel(self):
        """
        computer the logistic regression model
        """
        lg=linear_model.LogisticRegression()

        """
        the fit function of sklearn.linear_model.LogisticRegression has 2 parameters. The first one is an array-like/sparse matrix of all the features of the training data. The second parameter is an array-like (basically a list) of all the labels
        """  
        # fitting a curve y=f(x) where Y is the set of labels and X is the set of features
        self.logr=lg.fit(self.featureMatrix,self.labels)
    
    def predict(self, sample):
        """
        predicts for a sample X
        """
        return self.logr.predict(sample)


def main():

    allUsers=AllUsers()
    allUsers.getAllUserDetails()
    print ("all user details cached...")
    while True:
        print ("Enter a user id to recommend to/ -1 to quit:")
        userid=int(input())
        if user==-1:
            return -1
        user=User(allUsers.users, allUsers.movieID, allUsers.ratings)
        print ("getting user details...")
        user.getUserDetails(userid)
        document=Document(user.userRatedMovies)
        print ("making documents...")
        document.makeDocuments()
        tfvectorizer=TfVectorizer(document.documents, user.userRatings)
        print ("vectorizing...")
        tfvectorizer.vectorize()
        print ("training model...")
        recommend=Recommend(tfvectorizer.termDocMatrix,tfvectorizer.labels)
        print ("model trained...")

if __name__=="__main__":
    main()