from sklearn.cluster import KMeans
import tfidfVectorizer as tfidfVec


NUM_OF_CLUSTERS=15
class KMeansClustering:


    def __init__(self):
        # labels store the final predicted cluster values
        self.labels={}
        self.tfidfMatrix=tfidfVec.prepareVectors()

        for i in range(NUM_OF_CLUSTERS):
            self.labels[i]=[]

    def classify(self):

        kmeans=KMeans(n_clusters=NUM_OF_CLUSTERS, random_state=0).fit(self.tfidfMatrix)
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
        csvFile=open('Labels.csv','w',newline="")
        writer=csv.writer(csvFile)
        for key in self.labels:
            writer.writerow(self.labels[key])

def main():
    obj=KMeansClustering() 
    obj.classify()
    obj.writeLabelsToFile()

if __name__=="__main__":
    main()