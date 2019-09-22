import random
import numpy as np

## kmeans++ algorithm for seeding initial centroids before kmeans clustering
# parameters: X (data set), k (number of clusters)
# returns: centroids (array of initial cluster centers)
def kmeans_pp(X, k):
    # randomly choose first centroid from X
    rand_int = random.randint(0, np.size(X,0)-1)
    centroids = np.array([X[rand_int]])
    # remove already selected centroid from dataset X
    X = np.delete(X,rand_int,axis=0)
    # for each remaining centroid, do
    for c in range(1, k):
        # get min L2 distance (squared) from each data point in X to nearest centroid (thats already chosen)
        Dx = np.array([min([np.linalg.norm(x-c)**2 for c in centroids]) for x in X])
        # get weighted probability distribution of each data point wrt Dx^2
        probs = Dx / np.sum(Dx)
        # get cumulative probability of probs 
        cumprobs = np.cumsum(probs)
        # pick data point from X to be next center at random using weighted probs dist wrt Dx^2
        r = random.random()
        ind = np.where(cumprobs >= r)[0][0]
        centroids = np.append(centroids, [X[ind]], axis=0)
        X = np.delete(X,ind,axis=0)
    return centroids

## generate k centroids for all clusters in dataset
# parameters: Nxp dataset X and int k
# returns: kxp array of centroids (each row is a centroid with p features)
def k_means(X, k, maxIters):
    # initialize k centroids using kmeans++
    seeds = kmeans_pp(X, k)
    centroids = seeds
    iters=0
    stopLoop = False
    
    # keep iterating until max iterations reached or no change in centroid updates
    while (iters < maxIters) and (not stopLoop):
        iters = iters + 1
        # stores sum of all data points belonging to each cluster
        cluster_sum = np.zeros(centroids.shape, dtype='float64')
        # stores cluster assignments for each data point in X
        cluster_assgnmt = np.zeros(np.size(X,0), dtype='int64')
        
        # loop through entire dataset X
        for i,data_point in enumerate(X):
            # calculate Euclidean L2 distance of data point from each of the k centroids
            distances = np.linalg.norm(data_point - centroids, axis=1)
            # find index of closest centroid to current data point
            min_index = np.argmin(distances)
            # save min_index assignment for each data point
            cluster_assgnmt[i] = min_index
            # update sum of all data points belonging to this cluster
            cluster_sum[min_index] += data_point

        # get total number of data points for each cluster
        cluster_count = np.bincount(cluster_assgnmt, minlength=k)
        # new centroids are means of sum/count for each cluster (add new axis to count vector to allow broadcasting)
        new_centroids = cluster_sum / cluster_count[:,None]
        # calculate the L2 distance between new and old centroids
        L2_distances = np.linalg.norm(centroids - new_centroids, axis=1)
        # update centroids
        centroids = new_centroids
        # if all L2 distance is <= 0.001 (no centroids change), stop iterating
        if np.any(L2_distances <= 0.001):
            stopLoop = True
    
    return seeds, centroids, iters, cluster_assgnmt
