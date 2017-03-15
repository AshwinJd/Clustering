"""
JoinData will simply do an inner join between different tables 
"""
import csv
class JoinData:
    def __init__(self):
        self.data={}

    """
    opens the source file: in this case all other files to be joined
    """
    def openSource(self, fileName):
        
        csvFile=open(fileName, newline="")
        reader=csv.reader(csvFile)
        return reader

    """
    opens the destination file: in this case Movies.csv
    """
    def openDestination(self, fileName):
        
        csvFile=open(fileName, newline="")
        # opening file in append mode
        reader=csv.reader(csvFile)
        return reader
    
    def write(self, destinationFileName):

        csvFile=open(destinationFileName, 'w', newline="")
        writer=csv.writer(csvFile)
        writer.writerow(self.data['parameters'])
        
        for key in self.data:
            writeList=[]
            num=0
            # # DEBUG:
            # print("printing self.data[id]: "+str(self.data[key]))

            if key != 'parameters':
                for i in self.data[key]:
                    if num==0:
                        # this is the rowDest list
                        for j in i:
                            writeList.append(j)
                        num=1
                        continue
                    else:
                        writeList.append(i)
                        
                writer.writerow(writeList)
    """
    structure of hashTable:key: [[rowDest],[values corresponding to parameters],...]
    """        

    def innerJoin(self, sourceReader, destinationReader):

        readParamSource=iter(sourceReader)
        readParamDest=iter(destinationReader)
        # skipping the first row
        # the first column is the movieId no matter what file it is
        self.data['parameters']=next(readParamDest)
        r=next(readParamSource)
        id=1
        countParams=-1
        for i in r:
            countParams+=1
            if id==1:
                id=0
                continue
            else:
                self.data['parameters'].append(i)
        skipRow=1
        stopIteration=0
        for rowDest in readParamDest:
        
            # # DEBUG :
            # print("printing rowDest: "+str(rowDest))
            id=rowDest[0]
            self.data[id]=[]
            self.data[id].append(rowDest)
            for j in range(countParams):
                self.data[id].append([])
            while True:
                if skipRow==1:
                    try:
                        rowSource=next(readParamSource)
                    except Exception:
                        stopIteration=1
                        break
                if rowSource[0]==id:
                    skipRow=1
                    lenRowSource=len(rowSource)
                    for i in range(lenRowSource):
                        if i != 0:
                            # DEBUG:
                            # print('rowSource[i]: '+str(rowSource[i]))
                            if rowSource[i] != '':
                                self.data[id][i].append(rowSource[i])      
                else:
                    skipRow=0
                    break

            if stopIteration==1:
                break
def main():
    obj=JoinData()
    source=obj.openSource('movie_actors.csv')
    dest=obj.openDestination('movies.csv')
    obj.innerJoin(source, dest)
    obj.write('moviesNew.csv')

    source=obj.openSource('movie_countries.csv')
    dest=obj.openDestination('moviesNew.csv')
    obj.innerJoin(source, dest)
    obj.write('moviesNew.csv')

    source=obj.openSource('movie_genres.csv')
    dest=obj.openDestination('moviesNew.csv')
    obj.innerJoin(source, dest)
    obj.write('moviesNew.csv')

    source=obj.openSource('movie_locations.csv')
    dest=obj.openDestination('moviesNew.csv')
    obj.innerJoin(source, dest)
    obj.write('moviesNew.csv')

    source=obj.openSource('movie_tags.csv')
    dest=obj.openDestination('moviesNew.csv')
    obj.innerJoin(source, dest)
    obj.write('moviesNew.csv')

    source=obj.openSource('movie_directors.csv')
    dest=obj.openDestination('moviesNew.csv')
    obj.innerJoin(source, dest)
    obj.write('moviesNew.csv')
    

if __name__=="__main__":
    main()



