# Kernel Density Estimation 
# (Parzen-Rosenblatt Window Estimation)

## What is it?
  * KDE is a technique that lets you create a smooth curve given a set of data (creates an estimate of the underlying distribution., helping to visualize just the “shape” of some data, instead of just a discrete histogram  problems with histograms are that they are not smooth, and too dependent on the width of the bins and the end points of the bins). KDE 

### Kernel Function K(u)
  * The KDE is calculated by weighting the distances of all the data points we’ve seen for each location. If we’ve seen more points nearby, the estimate is higher, indicating the probability of seeing a point at that location. 
  * The Kernel function determines how the point distances are weighted, which determine how much the data points surrounding a location contribute to the estimation at that location. Kernel functions are centered at each data point (removing dependence on bin widths)
  * The concept of weighting the distances of our observations from a particular point, x, can be expressed mathematically as follows:
    * P(x) = 1/N * SUM( 1/h^d * K((x-xi)/h) ) for all xi in X 
      * K = kernel function, in our case hypercube kernel\
      Hypercube Kernel:  K(uj) = 1 if |uj|<=0.5 (for all j=1...d) ; 0 otherwise\
      This kernel, which corresponds to a unit hypercube centered at the origin,
is known as a Parzen window or the naïve estimator
      * X = data set
      * xi = each point (row) in data set
      * N = number of data points in X
      * h = bandwidth
      * d = dimension of data (number of features) \
      h^d for d=1 is just points along a line through x, for d=2, it is a cube in which if x falls within, it is considered in the estimation.
    
  * Types of Kernel Functions:\
    * Using the Parzen window hypercube kernel has a serious drawback: it weights equally all points 𝑥𝑖, regardless of their distance to the estimation point 𝑥. For these reasons, the Parzen window is commonly replaced with a smooth kernel function 𝐾(𝑢) like the Gaussian kernel
    * Just as the Parzen window estimate can be seen as a sum of boxes centered at the data, the smooth kernel estimate is a sum of “bumps”. The specific type of kernel function used determines the shape of these bumps. The parameter ℎ, also called the smoothing parameter or bandwidth, determines their width. Hence, using different kernel functions will produce different estimates.\
    List of different kernels: http://homepages.inf.ed.ac.uk/rbf/CVonline/LOCAL_COPIES/AV0405/MISHRA/kde.html

### Bandwidth (h)
  * KDE algorithm takes one parameter, bandwidth h, that affects how “smooth” the resulting curve is.
  * The contribution of data point x(i) to the estimate at some point x depends on how apart x(i) and x are.
  * Changing the bandwidth changes the shape of the kernel: a lower bandwidth means only points very close to the current position are given any weight, which leads to the estimate looking squiggly; a higher bandwidth means a shallow kernel where distant points can contribute.
  * Choosing the right bandwidth is critical:
    * Undersmoothing: When the bandwidth is 0.1 (very narrow) then the kernel density estimate is said to undersmoothed as the bandwidth is too small: spiky estimates with no smoothing. 
    * Oversmoothing: We have chosen a bandwidth that is too large and have obscured most of the structure of the data: flat estimate with few peaks/troughs
    * Optimal: use the bandwidth that minimises the AMISE (Asymptotic Mean Integrated Squared Error). 
      * AMISE still depends on the true underlying density and so we need to estimate the AMISE from our data: this particular choice of bandwidth recovers all the important features whilst maintaining smoothness.

### Helpful Links:
1. Interactive explanation of KDE: https://mathisonian.github.io/kde/
2. Most comprehensive guide on KDE: https://sebastianraschka.com/Articles/2014_kernel_density_est.html
3. PPT of 1D, 2D KDE, choosing h via cross-validation, & applied project ideas: https://web.as.uky.edu/statistics/users/pbreheny/621/F10/notes/10-28.pdf
4. Different kernel functions: http://homepages.inf.ed.ac.uk/rbf/CVonline/LOCAL_COPIES/AV0405/MISHRA/kde.html
5. PPT on limitations of KDE, alternatives: http://research.cs.tamu.edu/prism/lectures/pr/pr_l7.pdf
