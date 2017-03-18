from sklearn.cluster import KMeans
import tfidfVectorizer as tfidfVec

# NUM_OF_CLUSTERS=50
NUM_OF_CLUSTERS=100

class KMeansClustering:


    def __init__(self):
        # labels store the final predicted cluster values
        self.labels={}
        print("preparing vectors...Hang Tight...")
        self.tfidfMatrix=tfidfVec.prepareVectors()
        print("Vectors prepared.")

        for i in range(NUM_OF_CLUSTERS):
            self.labels[i]=[]

    def classify(self):

        print("Applying KMeans Clustering to vectors...Hang Tight...")
        kmeans=KMeans(n_clusters=NUM_OF_CLUSTERS, random_state=0).fit(self.tfidfMatrix)
        print("KMeans applied, clusters formed")
        print("Predicting labels...Hang Tight...")
        predictedLabels=kmeans.predict(self.tfidfMatrix)
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
        csvFile=open('LabelsClusters100.csv','w',newline="")
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