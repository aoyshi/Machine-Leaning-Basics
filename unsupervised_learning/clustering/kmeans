# K-MEANS CLUSTERING:
-- Partition N observations into k clusters such that each observation belongs to the cluster with the nearest mean. 
-- Works on labeled data (since unsupervised)
-- Finds inherent groupings in any given data (how is my data set organized?)

INPUT:
X = 2D data set (represented as nxp matrix : n rows, p columns, i.e. n data points, each with p attributes/features)
k = number of centroids (aka clusters. centroids are the centers, aka means, of clusters)

OUTPUT:
[c1...ck] = array of k centroids (each centroid is a point with p features)

# PSEUDOCODE:
1. Initialize/seed k centroids using kmeans++ (can also use Llyod's random initialization)
   (i) Randomly choose first centroid (c=0) from X (remove already selected centroid from X as you go)
  (ii) For each remaining centroid (c=1 -> k-1), do
       (i) Get min squared distance from each data point in X to nearest centroid (thats already been chosen) -> store in array DX2
      (ii) Get weighted probability distribution of each data point wrt DX2
     (iii) Pick data point from X randomly by weight of DX2/DX2.sum - this is next centroid
2. Initialize counter for number of iterations
3. while number of iterations < 1000, do
    (i) Increment number of iterations counter
    3a. For each data point in X
        (i) calculate it's Euclidean (squared, L2) distance from each of the k centroids 
       (ii) assign data point to the closest centroid (min dist)
    3b. For each centroid
       (i) find the mean of all the data points assigned to it
      (ii) assign new centroid value to corresponding old one
      (iii) calculate the L2-norm distance between new and old centroid
      (iv)  if this L2-norm distance is <= 0
      
 # On Jupyter Notebook:
 1. Simply call 
 `compare_kmeans( N=number of total data points
                  d=dimensionality/number of features in data
                  k=number of clusters
                  maxIter=maximum iterations to run
                )`
2. Program will print out detailed comparison between my kmeans function (from scratch) vs sci-kit learn's built-in kmeans function outputs.
