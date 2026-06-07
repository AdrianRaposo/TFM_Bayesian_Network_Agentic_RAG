# The Scaled Unscented Transformation 

Simon J. Julier, IDAK Industries, 901 Missouri Blvd., \#179<br>Jefferson City, MO 65109<br>E-mail:sjulier@idak.com


#### Abstract

This paper describes a generalisation of the unscented transformation (UT) which allows sigma points to be scaled to an arbitrary dimension. The UT is a method for predicting means and covariances in nonlinear systems. A set of samples are deterministically chosen which match the mean and covariance of a (not necessarily Gaussian-distributed) probability distribution. These samples can be scaled by an arbitrary constant. The method guarantees that the mean and covariance second order accuracy in mean and covariance, giving the same performance as a second order truncated filter but without the need to calculate any Jacobians or Hessians. The impacts of scaling issues are illustrated by considering conversions from polar to Cartesian coordinates with large angular uncertainties.


Keywords: Kalman filter, non-linear estimation, unscented filtering.

## I. INTRODUCTION

One of the most fundamental tasks in filtering and estimation is to calculate the statistics of a random variable which has undergone a transformation. The Kalman filter, for example, uses two such transformations to predict the state future state of a system and the measurements which a suite of sensors will make of that system. When the transformation is nonlinear no general closed-form solutions exist [1] and many approximations have been proposed [2-6]. Probably the most widely used estimator for nonlinear systems is the extended Kalman filter (EKF) [7, 8]. The EKF applies the Kalman filter to nonlinear systems by simply linearising all the nonlinear models so that the traditional linear Kalman filter equations can be applied. However, in practice, the EKF has two well-known drawbacks. First, linearisation can produce highly unstable filters if the assumptions of local linearity is violated [9]. Second, the derivation of the Jacobian matrices are nontrivial in most applications and often lead to significant implementation difficulties.

In [10] and [11] we introduced a new approximate method for propagating means and covariances through nonlinear transformations called the unscented transformation. A set of weighted sigma points are deterministically chosen so that certain properties of these points (such as their first two moments) match those of the prior distribution. Each point undergoes the nonlinear transformation and the properties of the transformed set are calculated. Although this algorithm superficially resembles a Monte Carlo method, no random sampling is used and, in consequence, only a small number of points $(2 n+1$ for an $n$ dimensional space)are required. In subsequent work we have developed other sigma point selection schemes which exploit more information such as the first three moments of an arbitrary distribution [12] or the first four non-zero moments of a Gaussian distribution [13].

However, all of these sigma point solutions share the property that as the dimension of the state space increases, the radius of the sphere that bounds all the sigma points increases as well. Even though the specified information is still captured correctly (i.e., the mean and covariance of the sigma points matches the aprior distribution for all dimensions), it does so at the cost of sampling non-local effects. For many kinds of nonlinearities
(such as exponents or trigonometric functions) this can lead to significant difficulties. In [14] we proposed a method for overcoming these difficulties through the use of negative weights and a "modified" form of the algorithm to guarantee positive semidefiniteness. However, the approach was developed from studying the higher order properties of the system and no physical intuition was used. Second, it was only developed to study the problem of point scaling for the specific set introduced in [11] and its applicability to other sigma point sets was not examined.

This paper re-examines the problem of sigma point scaling and introduces a new, general framework. Called the scaled unscented transformation, the method allows any set of sigma points to be scaled by an arbitrary scaling factor in such a manner that the first two moments of the set are preserved. It is equivalent to applying the conventional unscented transformation followed by a simple post-processing step. The storage and computational costs are exactly the same as a non-scaled version of the same transformation. The method can also be used to partially incorporate contributions higher order information into the estimates.

The structure of this paper is as follows. The problem is stated in Section II and the unscented transformation is described. Methods for sigma point scaling are examined in Section III and two complementary forms are derived. The first form uses an auxillary random variable - the nonlinear transformation is modified but the sigma point set is not. In this form it is easy to prove a number of properties including second order accuracy in mean and covariance predictions and also clearly shows the condition underwhich the predicted covariance is guaranteed to be positive semidefinite. We then derive the scaled unscented transformation which has the same properties as the auxillary form but modifies the sigma points themselves rather than the nonlinear transformation. We also show how some higher order information can be incorporated into the scaled transformation [15]. Conclusions are drawn in Section V.

## II. BACKGROUND

## A. Problem Statement

Let $\mathbf{x}$ be an $n$-dimensional random variable with mean $\overline{\mathbf{x}}$ and covariance $\mathbf{P}_{x x}$. A second random variable, $\mathbf{y}$ is related to $\mathbf{x}$ through the nonlinear transformation

$$
\mathbf{y}=\mathbf{f}[\mathbf{x}]
$$

The objective is to calculate the mean $\overline{\mathbf{y}}$ and covariance $\mathbf{P}_{y y}$ of $\mathbf{y}$.

Throughout this paper, we utilise to the Taylor Series expansion of Equation 1. Let $\mathbf{x}=\boldsymbol{\delta} \mathbf{x}+\overline{\mathbf{x}}$ where $\boldsymbol{\delta} \mathbf{x}$ is a zero mean random variable with covariance $\mathbf{P}_{x x}$. Expanding $\mathbf{f}[\cdot]$ about $\overline{\mathbf{x}}$,

$$
\mathbf{f}[\mathbf{x}]=\mathbf{f}[\overline{\mathbf{x}}+\boldsymbol{\delta} \mathbf{x}]=\mathbf{f}[\overline{\mathbf{x}}]+\boldsymbol{\nabla} \mathbf{f} \boldsymbol{\delta} \mathbf{x}+\frac{1}{2} \boldsymbol{\nabla}^{2} \mathbf{f} \boldsymbol{\delta} \mathbf{x}^{2}+\frac{1}{3!} \boldsymbol{\nabla}^{3} \mathbf{f} \boldsymbol{\delta} \mathbf{x}^{3}+\cdots
$$

where, for the sake of simplicity, we use the informal notation that $\nabla^{i} \mathbf{f} \boldsymbol{\delta} \mathbf{x}^{i}$ is the $i$ th order term in the multidimensional Taylor

1. Choose $0 \leq W_{0} \leq 1$.
2. Choose weight sequence:

$$
W_{i}= \begin{cases}\frac{1-W_{0}}{2^{i}} & \text { for } i=1 \\ W_{1} & \text { for } i=2 \\ 2^{i-1} W_{1} & \text { for } i=3, \ldots, n+1\end{cases}
$$

3. Initialize vector sequence as:

$$
\boldsymbol{\mathcal { X }}_{0}^{i} 1=[0], \boldsymbol{\mathcal { X }}_{1}^{i} 1=\left[-\frac{1}{\sqrt{2 W_{1}}}\right] \text { and } \boldsymbol{\mathcal { X }}_{2}^{i} 1=\left[\frac{1}{\sqrt{2 W_{1}}}\right]
$$

4. Expand vector sequence for $j=2, \ldots, n$ according to

$$
\boldsymbol{\mathcal { X}}_{j}^{i} j+1= \begin{cases}\left[\begin{array}{c}
\boldsymbol{\mathcal { X}}_{0}^{i} j \\
0\end{array}\right] & \text { for } i=0 \\
{\left[\begin{array}{c}
\boldsymbol{\mathcal { X}}_{i}^{i} j \\
-\frac{1}{\sqrt{2 W_{i}}}
\end{array}\right]} & \text { for } i=1, \ldots, j \\
\mathbf{0}_{j} & \text { for } i=j+1
\end{cases}
\end{cases}
$$

Box II.1: The Point Selection Algorithm for the Simplex Unscented Transform.

Series. Taking expectations, it can be shown that

$$
\begin{aligned}
\overline{\mathbf{y}}= & \mathrm{E}[\mathbf{y}] \\
= & \mathbf{f}[\overline{\mathbf{x}}]+\frac{1}{2} \nabla^{2} \mathbf{f} \mathbf{P}_{x x}+\frac{1}{6} \nabla^{3} \mathbf{f} \mathrm{E}\left[\boldsymbol{\delta} \mathbf{x}^{2}\right]+\cdots \\
\mathbf{P}_{y y}= & \mathrm{E}\left[(\mathbf{y}-\overline{\mathbf{y}})(\mathbf{y}-\overline{\mathbf{y}})^{T}\right] \\
= & \nabla \mathbf{f} \mathbf{P}_{x x}(\boldsymbol{\nabla} \mathbf{f})^{T}+\frac{1}{4} \nabla^{2} \mathbf{f E}\left[\boldsymbol{\delta} \mathbf{x}^{2}\right](\boldsymbol{\nabla} \mathbf{f})^{T}+\frac{1}{2} \nabla \mathbf{f E}\left[\boldsymbol{\delta} \mathbf{x}^{2}\right]\left(\boldsymbol{\nabla}^{2} \mathbf{f}\right)^{T} \\
& +\frac{1}{2} \boldsymbol{\nabla}^{2} \mathbf{f}\left(\mathrm{E}\left[\boldsymbol{\delta} \mathbf{x}^{4}\right]-\mathrm{E}\left[\boldsymbol{\delta} \mathbf{x}^{2} \mathbf{P}_{x x}\right]-\mathrm{E}\left[\mathbf{P}_{x x} \boldsymbol{\delta} \mathbf{x}^{2}\right]+\mathbf{P}_{x x}^{2}\right)\left(\boldsymbol{\nabla}^{2} \mathbf{f}\right)^{T} \\
& +\frac{1}{3!} \boldsymbol{\nabla}^{3} \mathbf{f E}\left[\boldsymbol{\delta} \mathbf{x}^{4}\right](\boldsymbol{\nabla} \mathbf{f})^{T}+\cdots
\end{aligned}
$$

The Unscented Transform builds on the principle that it is easier to approximate a probability distribution than it is to approximate an arbitrary nonlinear function. A set of $p+1$ weighted points $\mathcal{S}=\left\{W_{i}, \boldsymbol{\mathcal { X }}_{i}\right\}$ (such that $\sum_{i=0}^{p} W_{i}=1$ ) are chosen to reflect certain properties of $\mathbf{x}$ [13]. Once the set has been derived, the prediction method is straightforward. First, each point is instantiated through the nonlinear function, $\boldsymbol{\mathcal { Y }}_{i}=$ $\mathbf{f}\left[\boldsymbol{\mathcal { X}}_{i}\right]$. The estimated mean and covariance of $\mathbf{y}$ are then

$$
\begin{aligned}
\overline{\mathbf{y}} & =\sum_{i=0}^{p} W_{i} \boldsymbol{\mathcal { Y }}_{i} \\
\mathbf{P}_{y y} & =\sum_{i=0}^{p} W_{i}\left\{\boldsymbol{\mathcal { Y}}_{i}-\overline{\mathbf{y}}\right\}\left\{\boldsymbol{\mathcal { Y}}_{i}-\overline{\mathbf{y}}\right\}^{T}
\end{aligned}
$$

The difficulties of higher dimensions are clearly illustrated in the simplex set of sigma points which were derived in [16] and are listed in Box II.1. This set utilises the minimum number of points $(n+1)$ required to match the mean and covariance of an $n$-dimensional random variable.

The simplex set of points have two related difficulties. The first difficulty is that the distance of the $i$ th point from the origin is a function of $2^{(n-1 / 2)}$. Therefore, as $n$ increases, the radius of the sphere which bounds the sigma points increases as well. Second, these points are asymmetrically distributed about the origin. Therefore, higher order effects such as the skew become more significant as the dimension increases.

## III. Sigma Point Scaling Methods

The sigma point scaling methods attempt to overcome dimensional scaling effects by calculating the transformation of a scaled set of sigma points of the form

$$
\boldsymbol{\mathcal { X}}_{i}^{i}=\boldsymbol{\mathcal { X}}_{0}+\alpha\left(\boldsymbol{\mathcal { X}}_{i}-\boldsymbol{\mathcal { X}}_{0}\right)
$$

where $\alpha$ is a positive scaling parameter which can be made arbitrarily small to minimise higher order effects. Any permissible formulation should have the following two properties. First, for all choices of $\alpha$ the predicted covariance should be guaranteed to be positive semidefinite. Second, the second order accuracy in both the mean and covariance are preserved. We now describe two formulations for achieving this objective.

## A. The Auxillary Random Variable

The auxillary random variable formulation considers a transformation which is related to the problem stated in Equation 1. Specifically, we consider the problem of estimating the mean $\overline{\mathbf{x}}$ and covariance $\mathbf{P}_{z z}$ of the auxillary random variable $\mathbf{z}$. It is related to $\mathbf{x}$ through the nonlinear equation $\mathbf{z}=\mathbf{g}[\mathbf{x}, \overline{\mathbf{x}}, \alpha, \mu]$ where

$$
\mathbf{g}[\mathbf{x}, \overline{\mathbf{x}}, \alpha, \mu]=\frac{\mathbf{f}[\overline{\mathbf{x}}+\alpha(\mathbf{x}-\overline{\mathbf{x}})]-\mathbf{f}[\overline{\mathbf{x}}]}{\mu}+\mathbf{f}[\overline{\mathbf{x}}]
$$

$\alpha$ is a positive point scaling parameter and $\mu$ is a normalisation term which scales the transformed point about $\mathbf{f}[\overline{\mathbf{x}}]$ to offset the effects of $\alpha$. Because all sigma points are propagated through the term $\mathbf{f}[\overline{\mathbf{x}}+\alpha(\mathbf{x}-\overline{\mathbf{x}})]$, the scaling effect of Equation 7 is implicitly achieved. To prove the second order accuracy of this form, we consider the role played by $\alpha$ and $\mu$. Taking a Taylor Series expansion of $\mathbf{g}[\cdot, \cdot, \cdot \cdot]$ about $\overline{\mathbf{x}}$,

$$
\mathbf{g}[\mathbf{x}, \overline{\mathbf{x}}, \alpha, \mu]=\mathbf{f}[\overline{\mathbf{x}}]+\boldsymbol{\nabla} \mathbf{f}_{\mu}^{\frac{\alpha}{2}} \boldsymbol{\delta} \mathbf{x}+\frac{1}{2} \boldsymbol{\nabla}^{2} \mathbf{f} \frac{\alpha^{2}}{\mu} \boldsymbol{\delta} \mathbf{x}^{2}+\frac{1}{3!} \boldsymbol{\nabla}^{3} \mathbf{f} \frac{\alpha^{3}}{\mu} \boldsymbol{\delta} \mathbf{x}^{3}+\cdots
$$

Taking expectations, the mean of $\mathbf{z}$ is

$$
\overline{\mathbf{x}}=\mathbf{f}[\overline{\mathbf{x}}]+\frac{1}{2} \boldsymbol{\nabla}^{2} \mathbf{f} \frac{\alpha^{2}}{\mu} \mathbf{P}_{x x}+\frac{1}{6} \boldsymbol{\nabla}^{3} \mathbf{f} \frac{\alpha^{3}}{\mu} \mathrm{E}\left[\boldsymbol{\delta} \mathbf{x}^{2}\right]+\cdots
$$

These terms can be related directly to those of the Taylor Series expansion of $\mathbf{y}$. If $\mu=\alpha^{2}$, the expressions for $\overline{\mathbf{y}}$ and $\overline{\mathbf{x}}$ agree up to the second order. The ratio of the third and higher order terms of $\overline{\mathbf{x}}$ against $\overline{\mathbf{y}}$ scale geometrically with a commmon ratio of $\alpha$. Since $\alpha$ only affects the third and higher orders, its value can be chosen so that the scaling effects in the higher order terms are minimised. With a sufficiently small value of $\alpha$, the same mean can be calculated as with the modified form of the unscented transformation.

A similar result holds for the covariance. Let $\mathbf{P}_{z z}^{*}=\mu \mathbf{P}_{z z}$. Taking expectations,

$$
\begin{aligned}
\mathbf{P}_{z z}^{*}=\frac{\alpha^{2}}{\mu} \nabla \mathbf{f} \mathbf{P}_{x x}(\boldsymbol{\nabla} \mathbf{f})^{T}+\frac{\alpha^{3}}{\mu^{2}} \frac{1}{2} \nabla \mathbf{f E}\left[\boldsymbol{\delta} \mathbf{x}^{2}\right]\left(\boldsymbol{\nabla}^{2} \mathbf{f}\right)^{T} \\
\quad+\frac{\alpha^{4}}{\mu^{2}} \frac{1}{2} \boldsymbol{\nabla}^{3} \mathbf{f}\left(\mathrm{E}\left[\boldsymbol{\delta} \mathbf{x}^{4}\right]-\mathrm{E}\left[\boldsymbol{\delta} \mathbf{x}^{2} \mathbf{P}_{y y}\right]-\mathrm{E}\left[\mathbf{P}_{y y} \boldsymbol{\delta} \mathbf{x}^{2}\right]+\mathbf{P}_{y y}^{2}\right)\left(\boldsymbol{\nabla}^{3} \mathbf{f}\right)^{T} \\
\quad+\frac{\alpha^{4}}{\mu^{2}} \frac{1}{3!} \boldsymbol{\nabla}^{3} \mathbf{f E}\left[\boldsymbol{\delta} \mathbf{x}^{4}\right](\boldsymbol{\nabla} \mathbf{f})^{T}+\cdots
\end{aligned}
$$

When $\mu=\alpha^{2}$, the expansion of $\mathbf{P}_{z z}^{*}$ agrees with $\mathbf{P}_{y y}$ up to the second order and the third and higher order terms scale with $\alpha$.

The auxillary form of the unscented transformation simply applies the unscented transformation to the problem of estimating the mean and covariance of the auxillary random variable. Given an $n$-dimensional random variable $\mathbf{x}$ with mean $\overline{\mathbf{x}}$ and covariance $\mathbf{P}_{x x}$, a set of $p+1$ sigma points are chosen such that the

mean and covariance of those points are $\overline{\mathbf{x}}$ and $\mathbf{P}_{x x}$ respectively. The unscented transformation is then

$$
\begin{aligned}
\boldsymbol{Z}_{i} & =\frac{\mathbf{f}\left[\overline{\mathbf{x}}+\alpha\left(\boldsymbol{\mathcal { X }}_{i}-\overline{\mathbf{x}}\right)\right]-\mathbf{f}[\overline{\mathbf{x}}]}{\alpha^{2}}+\mathbf{f}[\overline{\mathbf{x}}] \\
\overline{\mathbf{x}} & =\sum_{i=0}^{p} W_{i} \boldsymbol{Z}_{i} \\
\mathbf{P}_{x x}^{*} & =\alpha^{2} \sum_{i=0}^{p} W_{i}\left\{\boldsymbol{\mathcal { Y }}_{i}-\overline{\mathbf{x}}\right\}\left\{\boldsymbol{\mathcal { Y }}_{i}-\overline{\mathbf{x}}\right\}^{T}
\end{aligned}
$$

From Equations 10 and 11 and given the fact that the sigma points have mean $\overline{\mathbf{x}}$ and covariance $\mathbf{P}_{x x}, \overline{\mathbf{z}}$ and $\mathbf{P}_{x x}^{*}$ are correct to the second order for any value of $\alpha$. Furthermore, because $\mathbf{P}_{x x}^{*}$ is calculated from the weighted outer products of vectors, positive semidefiniteness is guaranteed if all of the weights $W_{i}$ are non-negative. Since the only motive for choosing negative values of $W_{i}$ is to scale the points, this incentive is removed.

The auxiliary form is able to meet the requirements set out at the beginning of this section. However, it requires a change in the fundamental transformation system itself. We now show that it is possible to leave the original problem in place but apply a transformation to the sigma points themselves.

## B. The Scaled Unscented Transform

The scaled unscented transform yields the same results as the auxiliary form, but without the need to modify the transformation (Equation 1). Rather, an initial set of points are chosen using a normal sigma point selection algorithm. A specific transformation is applied to these points. The mean and covariance are calculated using Equations 5 and 6. A final term is added to offset the initial transformation which was applied to the sigma points.

Suppose a set of sigma points $\mathcal{S}$ have been constructed with mean $\overline{\mathbf{x}}$ and covariance $\mathbf{P}_{x x}$ and a positive scaling parameter $\alpha$ has been chosen. These points are transformed to a new set $\mathcal{S}^{\prime}=\{ \rangle=\prime, \infty, \ldots, \mathcal{S}^{\prime}: \boldsymbol{\mathcal { X }}_{1}^{\prime}, \mathcal{W}_{1}^{\prime}\}$ which has the same mean and covariance as $\mathcal{S}$ but the points now obey the condition of Equation 7. As a result, the weights of this transformed sequence are

$$
W_{i}^{\prime}=\left\{\begin{array}{ll}
W_{0} / \alpha^{2}+\left(1-1 / \alpha^{2}\right) & i=0 \\
W_{i} / \alpha^{2} & i \neq 0
\end{array}\right.
$$

The proof can be found in the Appendix. Because $\mathcal{S}^{\prime}$ is, itself, a sigma point set, it is possible with some selection algorithms to implicitly combine the scaling directly with the original sigma point selection.

Given this set of points, the scaled unscented transform calculates its statistics as follows:

$$
\begin{aligned}
& \boldsymbol{\mathcal { Y }}_{i}^{\prime}=\mathbf{f}\left[\boldsymbol{\mathcal { X }}_{i}^{\prime}\right] \\
& \overline{\mathbf{y}}^{\prime}=\sum_{i=0}^{p} W_{i}^{\prime} \boldsymbol{\mathcal { Y }}_{i}^{\prime} \\
& \mathbf{P}_{y y}^{\prime}=\sum_{i=0}^{p} W_{i}^{\prime}\left\{\boldsymbol{\mathcal { Y }}_{i}^{\prime}-\overline{\mathbf{y}}\right\}\left\{\boldsymbol{\mathcal { Y }}_{i}^{\prime}-\overline{\mathbf{y}}\right\}^{T}+\left(1-\alpha^{2}\right)\left\{\boldsymbol{\mathcal { Y }}_{0}^{\prime}-\overline{\mathbf{y}}\right\}\left\{\boldsymbol{\mathcal { Y }}_{0}^{\prime}-\overline{\mathbf{y}}\right\}^{T}
\end{aligned}
$$

In the Appendix we prove that, for any sigma point distribution, $\overline{\mathbf{y}}^{\prime}=\overline{\mathbf{z}}$ and $\mathbf{P}_{y y}^{\prime}=\mathbf{P}_{x x}^{*}$ when $\mu=\alpha^{2}$. This has a number of important consequences. First, the scaled unscented transformation possesses all of the properties of the auxillary form. The predicted mean and covariance are accurate to the second order and $\mathbf{P}_{y y}^{\prime}$ is guaranteed to be positive semidefinite if all of the untransformed weights are non-negative. Second, the numerical costs of this form are the same as with the unscaled unscented transform. Comparing Equation 18 to Equation 6, the only difference is that a term $\left(1-\alpha^{2}\right)$ is added to the weight on the zeroth sigma point. Finally this form provides a very simple
interpretation for $\alpha$. When $\alpha=1$, this gives Equation 6. When $\alpha=0$, this form gives the modified form of the covariance equation which was used in [14].

## C. Incorporating Higher Order Information

Although the sigma points only capture the first two moments of the sigma points (and so the first two moments of the Taylor Series expansion), the scaled unscented can be extended to include partial higher order information of the fourth order term in the Taylor Series expansion of the covariance [15]. The fourth order term of Equation 4 is

$$
\begin{aligned}
\mathbf{A}= & \frac{1}{4} \boldsymbol{\nabla}^{2} \mathbf{f}\left(\mathrm{E}\left[\boldsymbol{\delta} \mathbf{x}^{\mathrm{x}}\right]-\mathrm{E}\left[\boldsymbol{\delta} \mathbf{x}^{2} \mathbf{P}_{y y}\right]-\mathrm{E}\left[\mathbf{P}_{y y} \boldsymbol{\delta} \mathbf{x}^{2}\right]+\mathbf{P}_{y y}^{2}\right)\left(\boldsymbol{\nabla}^{2} \mathbf{f}\right)^{T} \\
& +\frac{1}{3!} \boldsymbol{\nabla}^{3} \mathbf{f E}\left[\boldsymbol{\delta} \mathbf{x}^{\mathrm{x}}\right]\left(\boldsymbol{\nabla} \mathbf{f}\right)^{T}
\end{aligned}
$$

The term $\frac{1}{3} \boldsymbol{\nabla}^{2} \mathbf{f} \mathbf{P}_{y y}^{2}\left(\boldsymbol{\nabla}^{2} \mathbf{f}\right)^{T}$ can be calculated from the same set of sigma points which match the mean and covariance. From Equations 2 and 3,

$$
\boldsymbol{\mathcal { Y }}_{0}-\overline{\mathbf{y}}=\frac{1}{2} \boldsymbol{\nabla}^{2} \mathbf{f} \mathbf{P}_{x x}+\frac{1}{6} \boldsymbol{\nabla}^{3} \mathbf{f} \mathrm{E}\left[\boldsymbol{\delta} \mathbf{x}^{\mathrm{x}}\right]+\cdots
$$

Taking outer products,

$$
\left(\overline{\mathbf{y}}-\boldsymbol{\mathcal { Y }}_{0}\right)\left(\overline{\mathbf{y}}-\boldsymbol{\mathcal { Y }}_{0}\right)^{T}=\frac{1}{4} \boldsymbol{\nabla}^{2} \mathbf{f P}_{y y}^{2}\left(\boldsymbol{\nabla}^{2} \mathbf{f}\right)^{T}+\cdots
$$

Therefore, adding extra weighting to the contribution of the zeroth point, further higher order effects can be incorporated at no additional computational cost by rewriting Equation 18 as

$$
\mathbf{P}_{y y}^{\prime}=\sum_{i=0}^{p} W_{i}^{\prime}\left\{\boldsymbol{\mathcal { Y }}_{i}^{\prime}-\overline{\mathbf{y}}\right\}\left\{\boldsymbol{\mathcal { Y }}_{i}^{\prime}-\overline{\mathbf{y}}\right\}^{T}+\left(\beta+1-\alpha^{2}\right)\left\{\boldsymbol{\mathcal { Y }}_{0}^{\prime}-\overline{\mathbf{y}}\right\}\left\{\boldsymbol{\mathcal { Y }}_{0}^{\prime}-\overline{\mathbf{y}}\right\}^{T}
$$

In this form, the error in the fourth order term is

$$
\begin{aligned}
\Delta \mathbf{A}= & \frac{1}{4} \boldsymbol{\nabla}^{2} \mathbf{f}\left(\mathrm{E}\left[\boldsymbol{\delta} \mathbf{x}^{\mathrm{x}}\right]-\mathrm{E}\left[\boldsymbol{\delta} \mathbf{x}^{2} \mathbf{P}_{y y}\right]-\mathrm{E}\left[\mathbf{P}_{y y} \boldsymbol{\delta} \mathbf{x}^{2}\right]+(1-\beta) \mathbf{P}_{y y}^{2}\right)\left(\boldsymbol{\nabla}^{2} \mathbf{f}\right)^{T} \\
& +\frac{1}{3!} \boldsymbol{\nabla}^{3} \mathbf{f E}\left[\boldsymbol{\delta} \mathbf{x}^{\mathrm{x}}\right]\left(\boldsymbol{\nabla} \mathbf{f}\right)^{T}
\end{aligned}
$$

In the special case that $\mathbf{x}$ Gaussian-distributed, $\mathrm{E}\left[\boldsymbol{\delta} \mathbf{x}^{\mathrm{x}}\right]=$ $3 \mathbf{P}_{x x}^{2}$ and so the error is

$$
\Delta \mathbf{A}=(2-\beta) \boldsymbol{\nabla}^{2} \mathbf{f P}_{y y}^{2}\left(\boldsymbol{\nabla}^{2} \mathbf{f}\right)^{T}+\frac{1}{3!} \boldsymbol{\nabla}^{3} \mathbf{f E}\left[\boldsymbol{\delta} \mathbf{x}^{\mathrm{x}}\right]\left(\boldsymbol{\nabla} \mathbf{f}\right)^{T}
$$

Under the assumption that no information about $\mathbf{f}[\cdot]$ is used, this term is minimised when $\beta=2$.

## D. Summary

The scaled unscented transformation can be written as

$$
\begin{aligned}
\boldsymbol{\mathcal { X }}_{i}^{\prime} & =\boldsymbol{\mathcal { X }}_{0}+\alpha\left(\boldsymbol{\mathcal { X }}_{i}-\boldsymbol{\mathcal { X }}_{0}\right) \\
\boldsymbol{\mathcal { Y }}_{i}^{\prime} & =\mathbf{f}\left[\boldsymbol{\mathcal { X }}_{i}^{\prime}\right] \\
W_{i}^{\prime} & =\left\{\begin{array}{ll}
W_{0} / \alpha^{2}+\left(1 / \alpha^{2}-1\right) & i=0 \\
W_{i} / \alpha^{2} & i \neq 0
\end{array}\right. \\
\overline{\mathbf{y}} & =\sum_{i=1}^{p} W_{i}^{\prime} \boldsymbol{\mathcal { Y }}_{i}^{\prime} \\
\mathbf{P}_{y y} & =\sum_{i=0}^{p} W_{i}^{\prime}\left\{\boldsymbol{\mathcal { Y }}_{i}^{\prime} \prime-\overline{\mathbf{y}}\right\}\left\{\boldsymbol{\mathcal { Y }}_{i}^{\prime} \prime-\overline{\mathbf{y}}\right\}^{T} \\
& +\left(W_{0}+1+\beta-\alpha^{2}\right)\left\{\boldsymbol{\mathcal { Y }}_{0}^{\prime}-\overline{\mathbf{y}}\right\}\left\{\boldsymbol{\mathcal { Y }}_{0}^{\prime}-\overline{\mathbf{y}}\right\}^{T}
\end{aligned}
$$

## IV. EXAMPLE

Suppose a mobile robot detects a beacon in its environment using a range-optimised sonar sensor. The sensor returns polar information (range $r$ and bearing $\theta$ ) and this is to be converted to estimate to Cartesian coordinates. The transformation is:

$$
\binom{x}{y}=\binom{r \cos \theta}{r \sin \theta} \text { with } \boldsymbol{\nabla} \mathbf{f}=\left[\begin{array}{cc}
\cos \theta & -r \sin \theta \\
\sin \theta & r \cos \theta
\end{array}\right]
$$

![img-0.jpeg](img-0.jpeg)

Fig. 1. $\overline{\mathbf{y}}$ and $\mathbf{P}_{yy}$ calculated using the simplex unscented algorithm and 20 different orientations of the sigma points. In all of these plots, $\beta = 0$.

The simplex points for a two-dimensional space consists of an isoceles triangle and a further point at the origin. Rotating the points about the origin by an angle $\phi$ does not affect their first or second moments. However, the rotation affects the third and higher moments which, through the nonlinear transformation, affect the predicted mean and covariance. The effect is illustrated in Figure 1(a) which shows the mean and the 1σ contours for $\overline{\mathbf{y}}$ and $\mathbf{P}_{yy}$ calculated for 20 different orientations of the sigma points. For this plot, $\alpha$ (the scaled unscented scaling parameter defined in Equation 22) has the value $10^{-1}$. As can be seen, the value of $\overline{\mathbf{y}}$ is hardly affected by the point orientation. However, the covariance does show significant variation, confirming the statement in [17]. These higher order effects can be greatly reduced by decreasing the value of $\alpha$. Figures 1(b) and 1(c) show the results of the same trials when $\alpha = 10^{-2}$ and $\alpha = 10^{-3}$. In the last value, the effects of sigma point orientation are minimal (the maximum change in the covariance is less than 0.09%). Therefore, this study has shown that the scaled sigma points directly contribute to the use of the simplex by eliminating higher order orientation dependent effects.

To investigate the accuracy of the simplex method, its results were compared with the true results (calculated by a Monte Carlo of $3.5 \times 10^6$ randomly drawn samples) and the results calculated through linearisation. The means and covariance ellipses for these three approaches are shown in Figure 2. The linearised estimate contains significant errors. Its mean is biased in the $x$-direction and, furthermore, its covariance is "too small". Whenever the filter updates with this estimate, it introduces unmodelled biases and correlations that can undermine filter stability. The simplex transform yields better results. When $\beta = 0$, its mean is unbiased. However, its covariance is similar to that calculated by linearisation. This is a direct consequence of the fact that the simplex only captures the first two moments of the mean and covariance correctly. However, the performance of this algorithm can be significantly improved by exploiting the fact that additional higher order information can be readily incorporated into the estimate. Because the distributions are Gaussian, the analysis from [16] shows that the information gained by the scaled unscented weight parameter $\beta$ (defined in Equation 27) is optimised when $\beta = 2$. This is confirmed in Figure 2 where it can be seen that the resulting estimate is, in fact, slightly conservative.

## V. DISCUSSION AND CONCLUSIONS

This paper has presented and analysed the scaled unscented transform. This new parameterisation permits a set of sigma points to be scaled using an arbitrary scaling parameter $\alpha$. Second order accuracy is maintained and the algorithm is guaranteed to give a positive semi-definite covariance if all of the weights on the sigma points are non-negative. Furthermore, its

![img-1.jpeg](img-1.jpeg)

Fig. 2. The means and 1σ contours calculated by different prediction algorithms. The Monte Carlo "true" solution has a mean + at (0.965,0) and its covariance is the solid ellipse. Linearisation yields the estimate + at (1,0) with the dotted ellipse. The simplex transform with $\beta = 0$ gives the mean $\Delta$ with the dot-dashed ellipse. The simplex transform with $\beta = 2$ has mean $\times$ and covariance the dashed line.

computational costs are exactly the same as those of the original formulation of the uscented transform.

This parameterisation provides a framework which can be applied with any sigma point distribution.

## APPENDIX

This Appendix shows that the any scaling strategy of the form of Equation 8 can be written as an application of the straightforward method plus a post-processing term. This means that the equation has exactly the same number of calculations as conventional unscented. We proceed by showing the equivalence of the weights, means and covariances respectively.

**Theorem 1:** The weights of the $\mathcal{S}^i$ are related to those of $\mathcal{S}$ by Equation 15.

**Proof:** The normalisation and covariance conditions obeyed by $\mathcal{S}$ are

$$
\sum_{i=0}^{\kappa} W_i = 1 \tag{28}
$$

$$
\sum_{i=1}^{\kappa} W_i(\mathbf{X}_i - \overline{\mathbf{x}})(\mathbf{X}_i^i - \overline{\mathbf{x}})^T = \mathbf{P}_{xx} \tag{29}
$$

where the fact that $\mathbf{X}_0 = \overline{\mathbf{x}}$ has been used. The conditions obeyed by $\mathcal{S}^i$ are

$$
\sum_{i=0}^{\kappa} W_i^i = 1 \tag{30}
$$

$$
\sum_{i=1}^{\kappa} W_i^i(\mathbf{X}_i^i - \overline{\mathbf{x}})(\mathbf{X}_i^i - \overline{\mathbf{x}})^T = \mathbf{P}_{xx} \tag{31}
$$

Comparing Equations 29 with 31 and substituting from Equation 7, it can be seen that $W_i = W_i^i \alpha^2$ for $i > 0$. $W_0$ is found from Equations 28 and 30,

$$
\begin{aligned}
1 &= \sum_{i=0}^{\kappa} W_i = W_0 + \sum_{i=1}^{\kappa} W_i \\
&= W_0 + \alpha^2 \sum_{i=1}^{\kappa} W_i^i \\
&= W_0 + \alpha^2 (1 - W_0^i)
\end{aligned} \tag{32}
$$

Each scaled unscented sigma point is $\boldsymbol{\mathcal{Y}}_{i}^{\prime}=\mathbf{f}\left[\boldsymbol{\mathcal{X}}_{i}^{\prime}\right]$, whereas $\boldsymbol{\mathcal { Z }}_{i}$ is given by Equation 8,

$$
\begin{aligned}
\boldsymbol{\mathcal { Z }}_{i} & =\mathbf{g}\left[\boldsymbol{\mathcal { X }}_{i}, \overline{\mathbf{x}}, \alpha, \mu\right] \\
& =\left(1-\frac{1}{\mu}\right) \mathbf{f}\left[\boldsymbol{\mathcal { X}}_{0}^{\prime}\right]+\frac{1}{\mu} \mathbf{f}\left[\boldsymbol{\mathcal { X}}_{i}^{\prime}\right] \\
& =\left(1-\frac{1}{\mu}\right) \boldsymbol{\mathcal { Y }}_{0}+\frac{1}{\mu} \boldsymbol{\mathcal { Y}}_{i}^{\prime}
\end{aligned}
$$

Theorem 2: Let

$$
\overline{\mathbf{z}}=\sum_{i=0}^{p} W_{i} \boldsymbol{\mathcal { Z }}_{i}, \overline{\mathbf{y}}^{\prime}=\sum_{i=0}^{p} W_{i}^{\prime} \boldsymbol{\mathcal { Y }}_{i}
$$

Then

$$
\overline{\mathbf{z}}=\frac{\mu-\alpha^{2}}{\mu} \boldsymbol{\mathcal { Y }}_{0}+\frac{\alpha^{2}}{\mu} \overline{\mathbf{y}}^{\prime}
$$

Proof: Substituting from Equations 15 and 33 and using the fact that $\sum_{i=0}^{p} W_{i}=1$,

$$
\begin{aligned}
\overline{\mathbf{z}} & =\left(1-\frac{1}{\mu}\right) \boldsymbol{\mathcal { Y }}_{0}+\frac{1}{\mu} \sum_{i=0}^{p} W_{i} \boldsymbol{\mathcal { Y }}_{i} \\
& =\left(\frac{\mu-1}{\mu}\right) \boldsymbol{\mathcal { Y }}_{0}+\frac{1-\alpha^{2}}{\mu} \boldsymbol{\mathcal { Y }}_{0}+\frac{\alpha^{2}}{\mu} \sum_{i=0}^{p} W_{i}^{\prime} \boldsymbol{\mathcal { Y }}_{i} \\
& =\frac{\mu-\alpha^{2}}{\mu} \boldsymbol{\mathcal { Y }}_{0}+\frac{\alpha^{2}}{\mu} \overline{\mathbf{y}}^{\prime}
\end{aligned}
$$

Theorem 3: Let
$\mathbf{P}_{z z}^{*}=\mu \sum_{i=0}^{p} W_{i}\left(\boldsymbol{\mathcal { Z }}_{i}-\overline{\mathbf{z}}\right)\left(\boldsymbol{\mathcal { Z }}_{i}-\overline{\mathbf{z}}\right)^{T}, \mathbf{P}_{\mathrm{yy}}^{\prime}=\sum_{i=0}^{p} W_{i}^{\prime}\left(\boldsymbol{\mathcal { Y}}_{i}^{\prime}-\overline{\mathbf{y}}^{\prime}\right)\left(\boldsymbol{\mathcal { Y }}_{i}-\overline{\mathbf{y}}^{\prime}\right)^{T}$.
Then

$$
\mathbf{P}_{z z}^{*}=\frac{\alpha^{2}}{\mu}\left\{\mathbf{P}_{\mathrm{yy}}^{\prime}+\left(1-\alpha^{2}\right)\left(\boldsymbol{\mathcal { Y }}_{0}-\overline{\mathbf{y}}^{\prime}\right)\left(\boldsymbol{\mathcal { Y }}_{0}-\overline{\mathbf{y}}^{\prime}\right)^{T}\right\}
$$

Proof: Substituting from Equations 33 and 34,

$$
\boldsymbol{\mathcal { Z }}_{i}-\overline{\mathbf{z}}=\frac{1}{\mu}\left(\boldsymbol{\mathcal { Y }}_{i}-\overline{\mathbf{y}}^{\prime}\right)+\frac{\left(\alpha^{2}-1\right)}{\mu}\left(\boldsymbol{\mathcal { Y }}_{0}-\overline{\mathbf{y}}^{\prime}\right)
$$

Therefore,

$$
\begin{aligned}
\mathbf{P}_{z z}^{*}= & \mu \sum_{i=0}^{p} W_{i}\left\{\frac{1}{\mu}\left(\boldsymbol{\mathcal { Y }}_{i}-\overline{\mathbf{y}}^{\prime}\right)+\frac{\left(\alpha^{2}-1\right)}{\mu}\left(\boldsymbol{\mathcal { Y }}_{0}-\overline{\mathbf{y}}^{\prime}\right)\right\} \\
& \times\left\{\frac{1}{\mu}\left(\boldsymbol{\mathcal { Y }}_{i}-\overline{\mathbf{y}}^{\prime}\right)+\frac{\left(\alpha^{2}-1\right)}{\mu}\left(\boldsymbol{\mathcal { Y }}_{0}-\overline{\mathbf{y}}^{\prime}\right)\right\}^{T} \\
= & \frac{1}{\mu} \sum_{i=0}^{p} W_{i}\left\{\left(\boldsymbol{\mathcal { Y }}_{i}-\overline{\mathbf{y}}^{\prime}\right)\left(\boldsymbol{\mathcal { Y }}_{i}-\overline{\mathbf{y}}^{\prime}\right)^{T}+\left(\alpha^{2}-1\right)\left(\boldsymbol{\mathcal { Y }}_{i}-\overline{\mathbf{y}}^{\prime}\right)\left(\boldsymbol{\mathcal { Y }}_{0}-\overline{\mathbf{y}}^{\prime}\right)^{T}+\right. \\
& \left.\left(\alpha^{2}-1\right)\left(\boldsymbol{\mathcal { Y }}_{0}-\overline{\mathbf{y}}^{\prime}\right)\left(\boldsymbol{\mathcal { Y }}_{i}-\overline{\mathbf{y}}^{\prime}\right)^{T}+\left(\alpha^{2}-1\right)^{2}\left(\boldsymbol{\mathcal { Y }}_{0}-\overline{\mathbf{y}}^{\prime}\right)\left(\boldsymbol{\mathcal { Y }}_{0}-\overline{\mathbf{y}}^{\prime}\right)^{T}\right\}
\end{aligned}
$$

From Equation 15,

$$
\sum_{i=0}^{p} W_{i}\left(\boldsymbol{\mathcal { Y }}_{i}-\overline{\mathbf{y}}^{\prime}\right)\left(\boldsymbol{\mathcal { Y }}_{i}-\overline{\mathbf{y}}^{\prime}\right)^{T}=\alpha^{2} \mathbf{P}_{y y}+\left(1-\alpha^{2}\right)\left(\boldsymbol{\mathcal { Y }}_{0}-\overline{\mathbf{y}}^{\prime}\right)\left(\boldsymbol{\mathcal { Y }}_{0}-\overline{\mathbf{y}}^{\prime}\right)^{T}
$$

$\sum_{i=0}^{p} W_{i}\left(\boldsymbol{\mathcal { Y }}_{i}-\overline{\mathbf{y}}^{\prime}\right)\left(\boldsymbol{\mathcal { Y }}_{0}-\overline{\mathbf{y}}^{\prime}\right)^{T}=\left(1-\alpha^{2}\right)\left(\boldsymbol{\mathcal { Y }}_{0}-\overline{\mathbf{y}}^{\prime}\right)\left(\boldsymbol{\mathcal { Y }}_{0}-\overline{\mathbf{y}}^{\prime}\right)^{T}$
$\sum_{i=0}^{p} W_{i}\left(\boldsymbol{\mathcal { Y }}_{0}-\overline{\mathbf{y}}^{\prime}\right)\left(\boldsymbol{\mathcal { Y }}_{0}-\overline{\mathbf{y}}^{\prime}\right)^{T}=\left(\boldsymbol{\mathcal { Y }}_{0}-\overline{\mathbf{y}}^{\prime}\right)\left(\boldsymbol{\mathcal { Y }}_{0}-\overline{\mathbf{y}}^{\prime}\right)^{T}$
Substituting Equations 37 to 39 into Equation 36,

$$
\mathbf{P}_{z z}^{*}=\frac{\alpha^{2}}{\mu}\left(\mathbf{P}_{\mathrm{yy}}^{\prime}+\left(1-\alpha^{2}\right)\left(\boldsymbol{\mathcal { Y }}_{0}-\overline{\mathbf{y}}^{\prime}\right)\left(\boldsymbol{\mathcal { Y }}_{0}-\overline{\mathbf{y}}^{\prime}\right)^{T}\right)
$$

Remark 1: When $\mu=\alpha^{2}$,

$$
\begin{aligned}
& \overline{\mathbf{z}}=\overline{\mathbf{y}}^{\prime} \\
& \mathbf{P}_{z z}^{*}=\mathbf{P}_{\mathrm{yy}}^{\prime}+\left(1-\alpha^{2}\right)\left(\boldsymbol{\mathcal { Y }}_{0}-\overline{\mathbf{y}}^{\prime}\right)\left(\boldsymbol{\mathcal { Y }}_{0}-\overline{\mathbf{y}}^{\prime}\right)^{T}
\end{aligned}
$$
