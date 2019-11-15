# K Nearest Neighbors
  * KNN is a supervised classification/regression algorithm that classifies a new unlabeled sample by looking at its nearest neighbors.
  * KNN starts with an initial set of already-labeled sample points, and adds new, unlabeled data points to that set. 
  * It calculates the distances of this data point from all other already-labeled samples, and finds the K nearest neighbors.
  * For classification problems, KNN chooses the class label of the majority of the K nearest neighbors as the label for the new data point.
  * For regression problems, KNN chooses the average value of the K nearest neighbors as the value of the new data point.
  
### Distance Metric to determine "near-ness":
  * Euclidean  (most popular)
  * Minkowski
  * Manhattan
  * Chebyshev
  * Hamming    (for categorical variables)
  
### Parameter Tnuning: Choosing the right K
‘k’ in KNN is a parameter that refers to the number of nearest neighbours to include in the majority of the voting process.\
  * Small values for K can be noisy and subject to the effects of outliers.
  * Larger values of K will have smoother decision boundaries which mean lower variance but increased bias.
  * Choosing odd values of k will help avoid confusion between two classes of data
(1) Quick-fix: K=sqrt(N) where N=total number of samples in training dataset.\
(2) More robust method: cross-validation. Select the cross-validation dataset from the training dataset. Take a small portion from the training dataset and call it a validation dataset, and then use the validation set to evaluate different possible values of K. This way we are going to predict the label for every instance in the validation set using with K equals to 1, K equals to 2, K equals to 3...and then we look at what value of K gives us the best performance on the validation set and then we can take that value and use that as the final setting of our algorithm so we are minimizing the validation error.
  
 <hr>
 
 ## PROS:
   * Simplicity: There's no need to tune parameters 
   * No formal training needed: We just need more training examples to improve the model
   * Naturally handles multi-class cases
   
 ## CONS:
   * It is computationally expensive - in a naive approach, all distances between points and every new sample have to be calculated, except when caching is implemented.
   * Need to choose the right value of parameter K (number of nearest neighbors)
   
<hr>

## Pseudocode:
(i) We place the previously known samples on the data structures.\
(ii) We then read the next sample to be classified and calculate the Euclidean distance from the new sample to every sample in the training set. \
(iii) We decide the class of the new element by selecting the class of the nearest sample, by Euclidean distance. The K-NN method requires the vote of the K closest samples – e.g. if K=11, the classes of the 11 nearest neighbors are considered. That class which has the most nearest neighbors of these 11, is the class label assigned to the new sample.\
(iv) We repeat the procedure until there are no more remaining samples.\

<hr>

