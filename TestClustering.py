"""
Both the data sets would be clustered based on their genre first and within each genre basd on a range of ratings.
Mind you that the same concept will be applied in both the data sets
"""
import csv
class TestClustering:
    def __init__(self):
        self.hashTable={}
        """
        This hashTable stores the record for all the genres and within each genre the ratings
        So the way this can be implemented is that for each genre and rating we can make an entry in the dictionary for the key and the value will be the index of all the movies that we falls in that category
        The implementation of this hashTable will be such that we do for each value in the dictionary we use a list of 3 lists , the first being for rating 0 to 1.5 next being for rating >1.5 to <3 and the third being for rating >=3 to <=5

        MovieLens:
        For the MovieLens database let us use the rating of rotten Tomatoes called rtAudienceRating. From the data it was clear that the maximum rating was 5 so the range of ratings for this database is [0,1.5),(1.5-3),(3-5]. From the data it is clear that it is the 17th row where we have the rtAudienceRating 
        Kaggle:

        """

    def openFile(self,fileName):
        """
        Opens the file and returns a reader object that is iterable
        """
        csvFile=open(fileName,newline="")
        reader=csv.reader(csvFile)
        return reader

    def makeClusters(self,genreFile, movieFile):
        """
        makes Clusters of the given file
        """
        readGenre=self.openFile(genreFile)
        readRatings=self.openFile(movieFile)

        """
        readRatings is an itearble object and hence we can call the next function that simply iterates thorugh the file once, this is done just for getting rid of the first row which is the paramter list.
        """
        readRatingsIter=iter(readRatings)
        next(readRatingsIter)
        # mind you we need to skip the very first row
        i=0
        count=0
        for row in readGenre:
            count+=1
            if i==0:
                i+=1
                continue
            # so the movie id is now available in row[0], for that movie id we can check what is the rating of that movie and place the movie in the appropriate cluster
            movieId=row[0]
            genre=row[1]
            try:
                rating=float(next(readRatingsIter)[17])
            except Exception:
                rating=0
            
            if genre not in self.hashTable:
                self.hashTable[genre]=[]
                for i in range(3):
                    self.hashTable[genre].append([])
                # the above code is for the creation of 3 lists
            
            if rating <= 1.5:
                if movieId not in self.hashTable[genre][0]:
                    self.hashTable[genre][0].append(movieId)
            elif rating<3:
                if movieId not in self.hashTable[genre][0]:
                    self.hashTable[genre][1].append(movieId)
            else:
                if movieId not in self.hashTable[genre][0]:
                    self.hashTable[genre][2].append(movieId)
        print("count:"+str(count))

    def displayHashTable(self):
        for key in self.hashTable:
            print(self.hashTable[key])

    def writeHashTableToFile(self):
        csvFile=open("hashTable.csv",'w',newline="")
        writer=csv.writer(csvFile)
        for key in self.hashTable:
            writer.writerow(self.hashTable[key])
def main():
    test=TestClustering()
    test.makeClusters("movie_genres.csv","movies.csv")
    print("clustering...done")
    test.writeHashTableToFile()

if __name__=="__main__":
    main()