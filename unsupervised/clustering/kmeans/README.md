# K-MEANS CLUSTERING:
1. Partition N observations into k clusters such that each observation belongs to the cluster with the nearest mean. 
2. Works on labeled data (since unsupervised)
3. Finds inherent groupings in any given data (how is my data set organized?)

## INPUT:
X = 2D data set (represented as nxp matrix : n rows, p columns, i.e. n data points, each with p attributes/features)
k = number of centroids (aka clusters. centroids are the centers, aka means, of clusters)

## OUTPUT:
[c1...ck] = array of k centroids (each centroid is a point with p features)

# Objective:
Implement k-means (with k-means++ seeding) from scratch, and compare output and performance with sci-kit learn's built-in k-means module.

# PSEUDOCODE:

0. Initialize parameters:
  * N = total number of data points
  * d = dimensions of data
  * k = number of clusters
  * maxIter = maximum number of iterations to run inside kmeans
  * reps = minimum number of times to repeat kmeans over X

1. Initialize/seed k centroids using kmeans++ (can also use Llyod's random initialization)

   1a. Randomly choose first centroid (c=0) from X (remove already selected centroid from X as you go)
   
   1b. For each remaining centroid (c=1 -> k-1), do
  
        (i) Get min squared distance from each data point in X to nearest centroid (thats already been chosen) -> store in array DX2
       (ii) Get weighted probability distribution of each data point wrt DX2
       (iii) Pick data point from X randomly by weight of DX2/DX2.sum - this is next centroid
     
2. Initialize counter for number of iterations

3. While number of iterations < maxIter, do

    3a. Increment number of iterations counter
    
    3b. For each data point in X
    
        (i) calculate it's Euclidean (squared, L2) distance from each of the k centroids 
       (ii) assign data point to the closest centroid (min dist)
       
    3c. For each centroid
    
         (i) find the mean of all the data points assigned to it
        (ii) assign new centroid value to corresponding old one
       (iii) calculate the L2-norm distance between new and old centroid
        (iv)  if any of these L2-norm distances is <= 0, exit the loop
    
    3c. Calculate SSE for this set of centroids
      
        (i) Initialize SSE sum counter=0
        (ii) Loop through all xi in X
           * find its assigned centroid, c
           * calculate squared distance between xi and c
           * add to SSE sum counter

4. Repeat steps 1->3 as many times as specified by user, and return the batch with the lowest SSE


 # Run on Jupyter Notebook:
 1. Simply Run All Cells for the Jupyter Notebook file provided.

## Notes:
#### KMeans++ vs Lloyd's:
-- Lloyd's random initialization (seeding) of centroids can lead to iterations where a centroid has 0 assignments, which leads to NaN values for the new centroids (remember that each centroid is sum of assignees / count of assignees).\
-- KMeans++ does a smarter random seeding of centroids - data points that are farther away from the set of already chosen centroids are more likely to be picked as the next centroid.

## Limitations of my implementation:
1. Sometimes the initial seeding by kmeans++ will get stuck in a local minimum (two seeds in the same cluster, i.e. the algorithm mistakenly splits up one cluster as two or more): the occurence of this is more prevalent as the number of clusters increases. This problem never happens with sci-kit learn's built-in kmeans. \
** **Edit 9/26/2019: I have greatly reduced the occurence of this problem by running the kmeans algorithm multiple times over the data set. The number of times to repeat kmeans can be specified by the user via a "reps" integer parameter, similar to the n_init parameter for scikit learn's KMeans function. Of the resp times that kmeans is repeated, the centroids with the lowest SSE (squared sum of errors: i.e. squared distances between each data point from its closest centroid) over the data.**
2. The plotting functions only work for 2D and 3D data (but the actual kmeans centroid finding algorithm will work for all dimensions)
3. Only works for upto 12 clusters

# Helpful Links:
1. Explanation of k-means++ seeding: https://www.youtube.com/watch?v=h_cVHtV0XoA
2. Limitations of k-means: https://stats.stackexchange.com/questions/133656/how-to-understand-the-drawbacks-of-k-means
3. Comprehensive Guide for k-means: https://www.analyticsvidhya.com/blog/2019/08/comprehensive-guide-k-means-clustering/
4. Weighted probability random selection: https://stats.stackexchange.com/questions/272114/using-kmeans-computing-weighted-probability-for-kmeans-initialization
5. Comparison k-means++ vs Lloyd's seeding: http://www.cs.columbia.edu/~jebara/6772/proj/oldprojects/bal2123_BATS-Means.pdf
6. Super detailed k-means++ math on excel: http://www.real-statistics.com/multivariate-statistics/cluster-analysis/initializing-clusters-k-means/
7. Article on clever seeding: http://ilpubs.stanford.edu:8090/778/1/2006-13.pdf
8. Other people's kmeans++ implementations:
  * https://datasciencelab.wordpress.com/2014/01/15/improved-seeding-for-clustering-with-k-means/
  * https://medium.com/machine-learning-algorithms-from-scratch/k-means-clustering-from-scratch-in-python-1675d38eee42
9. K-Means real-world project ideas: https://dzone.com/articles/10-interesting-use-cases-for-the-k-means-algorithm
