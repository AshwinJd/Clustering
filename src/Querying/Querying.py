import numpy as np
import csv

# This is the querying part of the system after pre-processing
NUM_RATINGS_TO_QUERY=3

class Querying:

    def __init__(self, userFileName):
        
        self.userFileName=userFileName
        self.users=[]
        self.ratings=[]
        self.movieID=[]
        self.index=-1

    def openFile(self):

        csvFile=open(self.userFileName, newline="")
        reader=csv.reader(csvFile)
        return reader

    # getLargestRatings gets the largest num ratings from the list ratings 
    def getLargestRatings(self, ratings, num):

        large=0
        position=0
        highestRatedIndices=[]
        iterations=0
        while iterations < num:
            large=0    
            for i in range(len(ratings)):
                
                if (ratings[i] > large) and (i not in highestRatedIndices):
                    # print(ratings[i])
                    large=ratings[i]
                    position=i
            
            highestRatedIndices.append(position)
            # del ratings[position]
            iterations+=1

        return highestRatedIndices

    def getUsersAndRatings(self):

        csvReader=self.openFile()
        rowIter=iter(csvReader)
        next(rowIter) # to get rid of the first row
        # users=[]
        while True:
            try:
                
                row=next(rowIter)
                self.users.append(row[0])
                self.movieID.append(row[1])
                self.ratings.append(row[2])

            except StopIteration:   
                # StopIteration exception is reached when the iterator has iterated thorugh all the rows
                # of the csvFile
                break
        

    def getUserApproxIndex(self, userID):
        
        low=0
        high=len(self.users)-1
        # index=-1
        while low <= high:
            mid=(low+high)/2
            if self.users[mid]==userID:
                self.index=mid
            else if self.users[mid]>userID:
                high=mid-1
            else if self.users[mid]<userID:
                low=mid+1

    def getUserStartIndex(self, userID):

        if self.index==-1:
            return -1
        else:
            # startIndex of the userID to be found
            i=self.index
            while i>=0:
                if userID!=self.users[i]:
                    return i+1
                i-=1

    def getUserEndIndex(self, userID):
        
        if self.index==-1:
            return -1
        else:
            # startIndex of the userID to be found
            i=self.index
            while i<=len(self.users):
                if userID!=self.users[i]:
                    return i-1
                i+=1

    def getUserRatings(self, userID):
        
        startIndex=self.getUserStartIndex(userID)
        endIndex=self.getUserEndIndex(userID)
        userRatings=[]
        for i in range(startIndex, endIndex):
            userRatings.append(self.ratings[i])

        indices=self.getLargestRatings(userRatings, NUM_RATINGS_TO_QUERY)
        # now indices has the positions where the highest ratings are stored



def check():
    a=[1,8,5,5,6,7,6]
    obj=Querying("dummy")
    print(obj.getLargestRatings(a, NUM_RATINGS_TO_QUERY))

def main():
    check()

if __name__=="__main__":
    main()
