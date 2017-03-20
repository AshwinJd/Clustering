import csv
class Verify:

    def openRecordsFile(self):
        file=open("../MovieLens/ResultMovieDataSet.csv", newline='')
        reader=csv.reader(file)
        return reader

    def openClusterFile(self, fileName):
        # fileName='../MovieLens/'+fileName
        file=open(fileName, newline="")
        reader=csv.reader(file)
        return reader

    def verifyCluster(self, fileReader, clusterReader, movieName):
        # fileReader is the reader instance of the main file where the entire dataset resides and the clusterReader 
        # is the instance where only the clusters reside(movie indices in each cluster)
        # -1 returned if something went wrong
        movieName=movieName.lower()
        indexList=[]
        index=0
        row=iter(fileReader)
        next(row)
        for row in fileReader:
            if movieName in row[1].lower():
                indexList.append(index)
            index+=1

        print ("indices are:")
        print(indexList)
        
        if indexList==[]:
            return -1
        
        for row in clusterReader:
            # checkList method checks whether all the elements in indexList are part of the row 
            # it returns 1 if all elements are found
            # 0 if no elements are found
            # -1 if few not all elements are found
            check=self.checkList(row, indexList)
            if check==1:
                return True
            elif check==-1:
                return False
        return -1
                
                

    def checkList(self, row, indexList):
        # returns 1  if all elements of indexList are found in row
        # 0 if none are found
        # -1 if only some are found
        if indexList[0] in row:
            for index in indexList:
                if index not in row:
                    return -1
            return 1    
        else:
            return 0
                        
                
def main():
    obj=Verify()
    recordReader=obj.openRecordsFile()
    clusterReader=obj.openClusterFile('LabelsClusters50.csv')
    if obj.verifyCluster(recordReader, clusterReader, 'spider-man'):
        print("All Okay")
    else:
        print("Something not quite right")

if __name__=="__main__":
    main()