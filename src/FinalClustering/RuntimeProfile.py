import profile

# This is a profiling module that gives a profile of all function calls and all the time taken for the program to execute
import NearestNeighbours 

statement='print(NearestNeighbours.apply())'

profile.run(statement)