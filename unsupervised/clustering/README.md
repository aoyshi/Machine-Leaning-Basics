# Clustering Algorithms

Clustering is an unsupervised learning method for learning the underlying structure of unlabeled data. \
It is the task of dividing the population or data points into a number of groups such that data points in the same groups are more similar to other data points in the same group and dissimilar to the data points in other groups.

### Broad Sub-groups of Clustering:

1. Hard Clustering:
Each data point either belongs to a cluster completely or not. 
2. Soft Clustering:
Instead of putting each data point into a separate cluster, a probability or likelihood of that data point to be in those clusters is assigned.

## Types of Clustering Algorithms:
#### Connectivity Models 
These models are based on the notion that the data points closer in data space exhibit more similarity to each other than the data points lying farther away. 
  * Hierarchical Clustering: \
    There are different levels of clustering, where each level is obtained by merging, or splitting, clusters from the previous level.
      * a) Agglomerative Clustering: \
           Bottom-Up approach - we merge clusters from the previous level. \
           All data points are classified into separate clusters & then aggregated as the distance decreases.
      * b) Divisive Clustering: \
           Top-Down approach - we split clusters from the previous level. \
           All data points are classified as a single cluster and then partitioned as the distance increases. \
Verdict: Connective models are very easy to interpret but lack scalability for handling big datasets.
<hr />
#### Connectivity Models 
These models are based on the notion that the data points closer in data space exhibit more similarity to each other than the data points lying farther away. 
  * Hierarchical Clustering: \
    There are different levels of clustering, where each level is obtained by merging, or splitting, clusters from the previous level.
      * a) Agglomerative Clustering: \
           Bottom-Up approach: we merge clusters from the previous level. \
           All data points are classified into separate clusters & then aggregated as the distance decreases.
      * b) Divisive Clustering:
           Top-Down approach: we split clusters from the previous level. \
           All data points are classified as a single cluster and then partitioned as the distance increases. \
Verdict: Connective models are very easy to interpret but lack scalability for handling big datasets.
<hr>
#### II. Centroid Models \
These are iterative clustering algorithms in which the notion of similarity is derived by the closeness of a data point to the centroid (center, mean) of the clusters. \
  * Partitioning Clustering: \
    * a) K-Means Clustering: \
         Partition the data into k clusters and each partition forms one cluster, with the centroid being the mean of all the points assigned to that cluster. Points belong to the cluster with the closest centroid.
    * b) K-Medoid Clustering:
         Variation of kmeans using medoids instead of means.
    * c) Mini-Batch K-Means:
         Main idea is to use small random batches of data of a fixed size, so they can be stored in memory. Each iteration a new random sample from the dataset is obtained and used to update the clusters and this is repeated until convergence.
    * d) CLARANS (Clustering Large Applications based upon randomized Search) 
Verdict: The number of clusters required at the end have to be mentioned beforehand, so need to have prior knowledge of the dataset.
<hr>
#### III. Distribution Models
These clustering models are based on the notion of how probable is it that all data points in the cluster belong to the same distribution (For example: Normal, Gaussian). 
  * Expectation-Maximization (EM) Clustering:
    The goal of EM clustering is to estimate the means and standard deviations for each cluster so as to maximize the likelihood of the observed data (distribution). It is a soft-clustering method - it does not compute actual assignments of observations to clusters, but classification probabilities.... i.e. each observation belongs to each cluster with a certain probability.
Verdict: Suffers from overfitting. 
<hr>
#### IV. Density Models: 
These models search the data space for areas of varied density of data points: it considers the clusters as the 'dense' region having some similarity and being different from the lower dense regions.
  * a) DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
  * b) OPTICS (Ordering Points to Identify Clustering Structure)
<hr>
#### V. Grid-based Models:
The data space is formulated into a finite number of cells that form a grid-like structure. All the clustering operation done on these grids are fast and independent of the number of data objects.
  * a) STING (Statistical Information Grid)
  * b) Wave Cluster
  * c) CLIQUE (CLustering In Quest)
 
