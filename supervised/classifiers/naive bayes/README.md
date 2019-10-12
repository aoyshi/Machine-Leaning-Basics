# Naive Bayes Classifier

  * Naïve Bayes classifiers are a family of simple "probabilistic classifiers" based on applying Bayes' theorem with strong (naïve) independence assumptions between the features. 
  * "Probabilistic Classifiers" are models that assign class labels to problem instances, represented as vectors of feature values, where the discrete class labels are drawn from some finite set.
  * It is a type of supervised learning method, which "learns" this model from a training dataset of features and corresponding labels, and makes predictions on new, unlabeled test dataset: the labels are discrete classifications of the data given the features of each data point.

## "Naive" Assumption:
There is not a single algorithm for training such classifiers, but a family of algorithms based on a common principle: all naive Bayes classifiers assume that the value of a particular feature is independent of the value of any other feature, given the class variable.\
For example, a fruit may be considered to be an apple if it is red, round, and about 10 cm in diameter. A naive Bayes classifier considers each of these features to contribute independently to the probability that this fruit is an apple, regardless of any possible correlations between the color, roundness, and diameter features.

## Advantages:
  * For problems with a small amount of training data, it can achieve better results than other classifiers because it has a low propensity to overfit. That’s Occam’s Razor at work!
  * Training is quick, and consists of computing the priors and the likelihoods.
  * Prediction on a new data point is quick. First calculate the posterior for each class. Then apply the MAP decision rule: the label is the class with the maximum posterior.
  * The RAM memory footprint is modest, since these operations do not require the whole data set to be held in RAM at once.
CPU usage is modest: there are no gradients or iterative parameter updates to compute, since prediction and training employ only analytic formulae.
  * Scales linearly with number of features and number of data points, and is easy to update with new training data.
  * Easily handles missing feature values — by re-training and predicting without that feature!
  * When independence assumption holds, NB outperforms logistic regression and other classifiers
## Disadvantages:
  * Cannot incorporate feature interactions, since assumes total independence.
  * For regression problems, i.e. continuous real-valued data, there may not be a good way to calculate likelihoods. Binning the data and assigning discrete classes to the bins is sub-optimal since it throws away information. Assuming each feature is normally distributed is workable, but could impact performance if features are not normally distributed. On the other hand, with enough training data in each class, you could estimate the likelihood densities directly, permitting accurate likelihood calculations for new data.
  * Performance is sensitive to skewed data — that is, when the training data is not representative of the class distributions in the overall population. In this case, the prior estimates will be incorrect.
