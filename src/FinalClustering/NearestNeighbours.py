# from sklearn.cluster import KMeans
# from sklearn.neighbours import KNeighborClassifier
import numpy as np
import os
import sys
end=os.getcwd().rindex('\\')
path=''
for i in range(end):
    path+=os.getcwd()[i]
sys.path.append(path+'\\NonNumericClustering')
import tfidfVectorizer as tfidfVec

class CosineSimilarityNN:

    def getDotProduct(self, documentIndex):
        print("preparing vectors...Hang Tight...")
        tfidfMatrix=tfidfVec.prepareVectors()
        print("Vectors prepared...Analyzing Nearest Movies...")
        tfidfArray=tfidfMatrix.toarray()
        doc=tfidfArray[documentIndex]
        dotProducts=[]
        sum=0
        for i in tfidfArray:
            val=i*doc
            for i in val:
                sum+=i
            dotProducts.append(sum)
            del val
            sum=0
        # all dotProducts prepared
        return dotProducts
    
    # the following function returns the smallest indices excluding the values in the exclude list
    def getSmallest(self, dotProducts, exclude):
        large=0
        count=0
        pos=0
        for i in dotProducts:
            if i > large and count not in exclude:
                large=i
                pos=count
            count+=1

        return pos
    
def getNearestNeighbours():
    obj=CosineSimilarityNN() 
    # document Index for testing is 0
    # docIndex=0
    docIndex=5026 # checking for spider man
    dotProducts=obj.getDotProduct(docIndex)
    # getting 5 smallest
    exclusionList=[docIndex]
    print("5 Nearest Movie Indices for movie 0 are:")
    for i in range(5):
        val=obj.getSmallest(dotProducts, exclusionList)
        exclusionList.append(val)
        print(val)

def apply():
    getNearestNeighbours()

# if __name__=="__main__":
    # main()

    



        