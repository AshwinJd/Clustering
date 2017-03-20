import profile

# This is a profiling module that gives a profile of all function calls and all the time taken for the program to execute
import KMeans 

statement='print(KMeans.apply())'

profile.run(statement)