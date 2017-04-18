# Querying

## Approach 1

After **Preprocessing** the next step would be querying. It is assumed at this stage that appropriate clusters have been made. 

During this process, classes will be assigned based on a **tf** scoring scheme within the requisite cluster. 

After the assignment of the scores all that we have to do is to get the best n results. This can simply be done by following a clustering algorithm within teh cluster itself

## Approach 2

Another approach would be the following. We can go to the cluster, consider the first movie in the cluster see if that movie exists in the user's list of watched movies, if so get the rating the user has given, try to bring the difference between that rating and rating of the original(query) movie as close to zero as possible 