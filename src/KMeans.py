from sklearn.cluster import KMeans
from NonNumericClustering import tfidfVectorizer as tfidfVec
from NumericClustering import Vectorizer as vec

NUM_OF_CLUSTERS=50

class KMeansClustering:


    def __init__(self):
        # labels store the final predicted cluster values
        self.labels={}
        print("preparing vectors...Hang Tight...")
        temp=tfidfVec.prepareVectors()
        print(type(temp))
        tfidfArray=(temp).toarray()
        # tfidfVec.prepareVectors() actually returns a sparse matrix(scipy), so to numpy array
        numericArray=vec.prepare()
        # vec.prepare() actually returns a numpy array

        iteratorNumArr=iter(numericArray)

        # The following step adds the numeric parameter dimensions to non-numeric matrix

        for i in range(len(tfidfArray)):
            numDataList=next(iteratorNumArr)
            for value in numDataList:
                l=list(tfidfArray[i])
                l.append(value)
                tfidfArray[i]=l
        
        self.dimensions=sparse.csr_matrix(tfidfArray)
            
        print("Vectors prepared.")

        for i in range(NUM_OF_CLUSTERS):
            self.labels[i]=[]

    def classify(self):

        print("Applying KMeans Clustering to vectors...Hang Tight...")
        kmeans=KMeans(n_clusters=NUM_OF_CLUSTERS, random_state=0).fit(self.dimensions)
        print("KMeans applied, clusters formed")
        print("Predicting labels...Hang Tight...")
        predictedLabels=kmeans.predict(self.dimensions)
        count=0
        for i in predictedLabels:
            # count here are the ids of the corresponding movies
            self.labels[i].append(count)
            count+=1
    
    def getSimilar(self, id):
        
        # ids start from 0
        print("predicted movieID/s: ")
        for clusterNum in self.labels:
            if id in self.labels[clusterNum]:
                return self.labels[clusterNum]

    def writeLabelsToFile(self):
        
        import csv
        # Optimization 1, reduced number of parameters for tfidf vectorization
        csvFile=open('LabelsClusters50_Merged.csv','w',newline="")
        writer=csv.writer(csvFile)
        for key in self.labels:
            writer.writerow(self.labels[key])

def main():
    obj=KMeansClustering() 
    obj.classify()
    print("Writing to file...")
    obj.writeLabelsToFile()
    print("Done...File saved to current Directory")

if __name__=="__main__":
    main()