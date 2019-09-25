# Kernel Density Estimation 
# (Parzen-Rosenblatt Window Estimation)

## What is it?
  * KDE is a technique that lets you create a smooth curve given a set of data from an unknown distribution, helping to visualize just the “shape” of some data, instead of just a discrete histogram. KDE creates an estimate of the underlying distribution.

### Kernel Function K(u)
  * The KDE is calculated by weighting the distances of all the data points we’ve seen for each location. If we’ve seen more points nearby, the estimate is higher, indicating the probability of seeing a point at that location. 
  * The Kernel function determines how the point distances are weighted, which determine how much the data points surrounding a location contribute to the estimation at that location. Kernel curves exist for each location on the kDE curve and are bell-shaped (like a minima)
  * The concept of weighting the distances of our observations from a particular point, x, can be expressed mathematically as follows:
    * P(x) = 1/N * SUM( 1/h^d * K((x-xi)/h) ) for all xi in X 
      * K = kernel function, in our case hypercube kernel\
      Hypercube Kernel:  K(u) = 1 if |u|<=0.5, 0 otherwise
      * X = data set
      * xi = each point (row) in data set
      * N = number of data points in X
      * h = bandwidth
      * d = dimension of data (number of features) 
    
  * Types of Kernel Functions:\
  Using different kernel functions will produce different estimates.\
  List of different kernels: http://homepages.inf.ed.ac.uk/rbf/CVonline/LOCAL_COPIES/AV0405/MISHRA/kde.html

### Bandwidth (h)
  * KDE algorithm takes one parameter, bandwidth h, that affects how “smooth” the resulting curve is.
  * Changing the bandwidth changes the shape of the kernel: a lower bandwidth means only points very close to the current position are given any weight, which leads to the estimate looking squiggly; a higher bandwidth means a shallow kernel where distant points can contribute.

Move your mouse over the graphic to see how the data points contribute to the estimation — the “brighter” a selection is, the more likely that location is. The red curve indicates how the point distances are weighted, and is called the kernel function. The points are colored according to this function.


### Helpful Links:
1. Interactive explanation of KDE: https://mathisonian.github.io/kde/
2. Most comprehensive guide on KDE: https://sebastianraschka.com/Articles/2014_kernel_density_est.html
3. PPT of 1D, 2D KDE, choosing h via cross-validation, & applied project ideas: https://web.as.uky.edu/statistics/users/pbreheny/621/F10/notes/10-28.pdf
4. Different kernel functions: http://homepages.inf.ed.ac.uk/rbf/CVonline/LOCAL_COPIES/AV0405/MISHRA/kde.html
5. PPT on limitations of KDE, alternatives: http://research.cs.tamu.edu/prism/lectures/pr/pr_l7.pdf
