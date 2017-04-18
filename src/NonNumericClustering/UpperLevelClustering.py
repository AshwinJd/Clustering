from sklearn.cluster import KMeans
import numpy as np
import csv

NUM_OF_CLUSTERS=100

# important columns to consider: 7, 12, 17

# Numeric colums to take into consideration are the following: 7 to 20 (both inclusive)

START_NUMERIC_INDEX=7
END_NUMERIC_INDEX=20

columns=[7, 12, 17]

class UpperLevelClustering:

    def __init__(self):
        self.movies={}
        self.labels={}
        for i in range(NUM_OF_CLUSTERS):
            self.labels[i]=[]

    def openFile(self, fileName):
            
        csvFile=open(fileName, newline="")
        reader=csv.reader(csvFile)
        return reader

    def openWriterFile(self, fileName):
        
        csvFile=open(fileName,'w',newline="")
        writer=csv.writer(csvFile)
        return writer

    def initializeIterator(self, csvFileObject):
        return csv.reader(csvFileObject)

    def stringToList(self, s): # this is a hack: avoid as far as possible
        
        s=s.strip('[')
        s=s.strip(']')
        # print(s)
        s=s.strip("'")
        # print(s)
        return s.split("', '")

    def makeDocuments(self, mainFileMovieList, movieId):
        # count=0
        movie=mainFileMovieList[movieId+1]
        self.movies[movieId]=[]
        # for index in range(START_NUMERIC_INDEX,END_NUMERIC_INDEX+1):
        for index in columns:
            try:
                numericVal=float(movie[index])
            except Exception:
                numericVal=0.0
            self.movies[movieId].append(numericVal)
        # print (self.movies[movieId])
    
    def initializeLabels(self):
        self.labels.clear()
        for i in range(NUM_OF_CLUSTERS):
            self.labels[i]=[]

    def initializeMovies(self):
        self.movies.clear()

    def makeClustersAndWriteToFile(self, clusterCSVReader, mainFileCSVReader, finalClusterWriter):

        writer=finalClusterWriter
        clusterNum=0
        mainFileMovieList=list(mainFileCSVReader)
        for row in clusterCSVReader:
            print("reading cluster:"+str(clusterNum))
            clusterNum+=1
            # print(row)
            if len(row)>NUM_OF_CLUSTERS:
                for id in row:
                    self.makeDocuments(mainFileMovieList, int(id))
                # print(self.movies)
                movieList=[]
                for key in self.movies:
                    movieList.append(self.movies[key])
                movieList=np.array(movieList)
                kmeans=KMeans(n_clusters=NUM_OF_CLUSTERS).fit(movieList)
                predictedLabels=kmeans.predict(movieList)
                print("length of predicted Labels: "+str(len(predictedLabels)))
                print (predictedLabels)
                # count=0
                movieIterator=iter(self.movies)
                for i in predictedLabels:
                    # count here are the ids of the corresponding movies
                    movieId=next(movieIterator)
                    self.labels[i].append(movieId)
                    # count+=1
                nonNumericCluster=[]
                for key in self.labels:
                    nonNumericCluster.append(self.labels[key])
                writer.writerow(nonNumericCluster)
                # freeing memory
                del nonNumericCluster
                self.initializeLabels()
                self.initializeMovies()
                # self.labels.clear()
                # self.movies.clear()
                del movieList
            else:
                writer.writerow(row)
        del mainFileMovieList
                

def main():
    obj=UpperLevelClustering()
    clusterCSVReader=obj.openFile("LabelsClusters200NoIdfOp2ActorDirectorNoCountry.csv")
    mainFileCSVReader=obj.openFile("../MovieLens/ResultMovieDataSet.csv")
    finalClusterWriter=obj.openWriterFile("LabelsNumreicClusters100Op1.csv")
    print("making clusters and writing to file")
    obj.makeClustersAndWriteToFile(clusterCSVReader, mainFileCSVReader, finalClusterWriter)

if __name__=="__main__":
    main()