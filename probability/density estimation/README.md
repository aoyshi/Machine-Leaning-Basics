# Density Estimation
Why do we need it: We work only with samples (observable) taken from the real population (unobservable), so must approximate back from the sample to the population.\
Formally: Density estimation is the construction of an estimate, based on observed data, of an unobservable underlying probability density function (PDF*), according to which a large population is distributed.\

## Types of Density Estimations
### Parametric Density Estimation:
Assumes that the sample data came from a population that can be modeled by a probability distribution with a fixed set of parameters. Parametric DE approaches attempt to estimate this fixed set of parameters of the model. A parametric approach to density estimation is sensible if one has some justification that the data at hand can be modeled by a known parametric family of distributions:
1. Parametric Continuous Distributions:
  * Gaussian (Normal) Distribution:\
  The normal family of distributions all have the same general shape and are parameterized by mean and standard deviation. So if the mean and standard deviation are known and if the distribution is normal, the probability of any future observation lying in a given range is known.
  * Uniform Distribution
  * Exponential Distribution
2. Parametric Discrete Distributions:
  * Bernoulli Distribution:
  A Bernoulli distribution has only two possible outcomes, namely 1 (success) and 0 (failure), and a single trial. So the random variable X which has a Bernoulli distribution can take value 1 with the probability of success, say p, and the value 0 with the probability of failure, say q or 1-p.
  * Binomial Distribution
  * Poisson Distribution

### Non-Parametric:
Assumes that the sample data came from a population that can be modeled by a probability distribution which has a NON-FIXED parameter set, i.e. the number of parameters can increase, or even decrease, if new relevant information is collected./
Let X = X1, . . . , Xn be a sample from a distribution P with density p. The goal of nonparametric density estimation is to estimate p with as few assumptions about p as possible (assuming only that it is “smooth”). The estimator will depend on a smoothing parameter h and choosing h carefully is crucial.
1. Histograms:\
Here, space is divided into regular bins, and the estimated density within each bin is assigned a uniform value, proportional to the number of observations that fall within that bin. Divide X into bins, or sub-cubes, of size h. There are N ≈ (1/h)^d such bins and each has volume h^d (where d=dimensionality of data). Denote the bins by B1, . . . , BN .\Histogram estimates are not smooth and suffer greatly from the curse of dimensionality.
2. Kernel Density Estimation
3.

## *PDF: Probability Density Function
PDF of a continuous random variable, is a function whose value at any given point provides a relative likelihood** that the value of the random variable would equal that point. PDF is non-negative, and integral over entire graph = 1.\
The PDF is used to specify the probability of the random variable falling within a particular range of values, as opposed to taking on any one value. This probability is given by the integral of the PDF over that range (i.e. area under the density function).\
**Absolute Likelihood: the absolute likelihood for a continuous random variable to take on any particular value is 0 (since there are an infinite set of possible values to begin with).
