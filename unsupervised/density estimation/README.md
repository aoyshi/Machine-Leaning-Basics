# Density Estimation
**Why do we need it:**\
We work only with samples (observable) taken from the real population (unobservable), so must approximate back from the sample to the population.\
**Formally:**\
Density estimation is the construction of an estimate, based on observed data, of an unobservable underlying probability density function (PDF*), according to which a large population is distributed.

## Types of Density Estimations
### Parametric Density Estimation:
Assumes that the sample data came from a population that can be modeled by a probability distribution with a fixed set of parameters. Parametric DE approaches attempt to estimate this fixed set of parameters of the model. E.G.  The normal family of distributions all have the same general shape and are parameterized by mean and standard deviation. So if the mean and standard deviation are estimated and if the distribution is normal, the probability of any future observation lying in a given range is known.\
A parametric approach to density estimation is sensible if one has some justification that the data at hand can be modeled by a known parametric family of distributions:
1. Parametric Continuous Distributions:
  * Gaussian (Normal) Distribution
  * Uniform Distribution
  * Exponential Distribution
2. Parametric Discrete Distributions:
  * Bernoulli Distribution
  * Binomial Distribution
  * Poisson Distribution
#### GREAT article detailing all 6 parametric distributions: https://www.analyticsvidhya.com/blog/2017/09/6-probability-distributions-data-science/


### Non-Parametric:
Assumes that the sample data came from a population that can be modeled by a probability distribution which has a NON-FIXED parameter set, i.e. the number of parameters can increase, or even decrease, if new relevant information is collected.\
Let X = X1, . . . , Xn be a sample from a distribution P with density p. The goal of nonparametric density estimation is to estimate p with as few assumptions about p as possible (assuming only that it is “smooth”). The estimator will depend on a smoothing parameter h  (called the bandwidth) and choosing h carefully is crucial.
1. Discrete Histograms
2. Kernel Density Estimation
3. Orthogonal Series Estimators
4. Penalized Maximum Likelihood Estimators
5. Density Estimation via Nonparametric Regression
#### Article detailing all 5 non-parametric distributions: http://anson.ucdavis.edu/~mueller/encycl5-1.pdf


## *PDF: Probability Density Function
PDF of a continuous random variable, is a function whose value at any given point provides a relative likelihood** that the value of a drawn random variable would equal that. PDF is non-negative, and its integral over the entire space = 1.\
The PDF is used to specify the probability of the random variable falling within a particular range of values, as opposed to taking on any one value. This probability is given by the integral of the PDF over that range (i.e. area under the density function graph).\
****Absolute Likelihood**: the absolute likelihood for a continuous random variable to take on any particular value is 0 (since there are an infinite set of possible values to begin with).
