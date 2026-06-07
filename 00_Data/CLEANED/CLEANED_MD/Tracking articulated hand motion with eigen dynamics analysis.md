# Tracking Articulated Hand Motion with Eigen Dynamics Analysis 

Hanning Zhou and Thomas S. Huang<br>ECE Department, University of Illinois at Urbana-Champaign<br>Urbana, IL 61801<br>email: \{hzhou,huang\}@ifp.uiuc.edu


#### Abstract

This paper introduces the concept of eigen-dynamics and proposes an eigen dynamics analysis (EDA) method to learn the dynamics of natural hand motion from labelled sets of motion captured with a data glove. The result is parameterized with a high-order stochastic linear dynamic system (LDS) consisting of five lower-order LDS. Each corresponding to one eigen-dynamics. Based on the EDA model, we construct a dynamic Bayesian network (DBN) to analyze the generative process of a image sequence of natural hand motion. Using the DBN, a hand tracking system is implemented. Experiments on both synthesized and real-world data demonstrate the robustness and effectiveness of these techniques.


## 1 Introduction

The methods that have been proposed for tracking hand motion could be divided into two categories. One is appearance-based. Some tried to establish a mapping between the image feature space and the hand configuration space [4, 33, 25]. The other is model-based. Deformable hand shape models are fitted with statistical methods such as local principal component analysis (PCA) [11, 12] and sequential Monte Carlo [13]. 3D kinematic models are used in [16, 24, 23, 6, 34]. Recently, the idea of tracking-bydetection merge these two categories by doing exhaustive search in large databases of 2D templates [27, 1]. Stenger et al. proposed a tree-based filtering to discretize the finger configuration space for faster searching [28, 29].

The aim of this paper is to study the dynamics of natural hand motion, which can be used both in the context of tracking and in building structurally optimized template database for fast detection. Dynamic models have been widely used in tracking [22], classification [19, 21] and synthesis [35] of human body motion. Ghahramani [9] proposed a DBN framework for learning and inference in one class of switching linear dynamic system (SLDS) models. North et al. [19]
proposed a framework of switching particle filters to learn multi-class dynamics. Although these methods could be applied to hand motion, they are not specifically tailored for the dynamics of human hand.

We define the concept of eigen-dynamics and propose an eigen dynamics analysis (EDA) method to learn the dynamics of natural hand motion as a high order stochastic LDS consisting of five decoupled lower order subsystems. Each corresponds to one eigen-dynamics. Based on the dynamic model, we introduce a DBN framework for tracking articulated hand motion, which incorporates a kinematic hand model, finger dynamics, color models and image observations. Using this DBN, we implemented a robust and effective system for tracking natural hand motion from a monocular view. In the observation phase, a new feature called likelihood edge is extracted. In the inference phase, we decompose hand motion into global motion and finger articulation and solve them iteratively in a divide-and-conquer fashion [32]. For global motion, we apply iterative closest point (ICP) algorithm[36]. For tracking finger articulation, we apply sequential Monte Carlo [18] to sample in the manifold spanned by the learned dynamic model.

Section 2 proposes the EDA method. Section 3 describes the DBN for tracking global and local hand motion. Section 4 introduces the new feature called likelihood edge. Section 5 describes the ICP based global hand tracking algorithm. Section 6 describes the inference of the finger articulation based on factored sampling. Section 7 provides experimental results in both quantitative and visual forms. Section 8 summaries our contributions and limitations of the system.

## 2 Modelling Hand Dynamics with EDA

The finger configuration $\mathbf{Z}[k]$ is represented by 20 joint angles based the kinematic model we use, where each finger is a kinematic chain with four degrees of freedom. Due to geometry and biomechanics constraints, the feasible finger configurations lie in a manifold $\mathrm{C} \subset \Re^{20}$, which we propose to model with EDA.

### 2.1 The $10^{t h}$ Order Stochastic LDS

Denoting the 6 dimensional PCA space by $\Upsilon$, we project $\mathbf{Z}[k] \in \mathrm{C}$ to $\mathbf{Y}[k] \in \Upsilon$ by

$$
\mathbf{Y}[k]=U_{6 \times 20}(\mathbf{Z}[k]-\mathbf{E}\{\mathbf{Z}\})
$$

where the rows of matrix $U_{6 \times 20}$ are the eigen vectors corresponding to the six largest eigen values of the covariance matrix of $\mathbf{Z}$, and $\mathbf{E}\{\mathbf{Z}\}$ is the mean over $\mathbf{C}$.

After PCA dimension reduction, around $99.79 \%$ of the variance is preserved. Because of the intrinsic nonlinearity, we need a high dimensional linear system to parameterize the dynamics of finger articulation. Therefore we assume $\mathbf{Y}[k]_{6 \times 1}$ as the output of a $10^{t h}$ order stochastic LDS:

$$
\begin{aligned}
\mathbf{X}[k+1] & =A_{10 \times 10} \mathbf{X}[k]+w[k] \\
\mathbf{Y}[k] & =C_{6 \times 10} \mathbf{X}[k]+v[k]
\end{aligned}
$$

where $w[k]$ and $v[k]$ are both zero mean Gaussian. Using the data collected with CyberGlove, we could directly train a $10^{t h}$ order stochastic LDS with subspace identification algorithm [31], and obtain a LDS $\hat{\mathbf{S}}=$ $\left\{\hat{A}_{10 \times 10}, \hat{C}_{6 \times 10}, \Sigma_{\hat{w} 10 \times 10}, \Sigma_{\hat{v} 6 \times 6}\right\}$. However, the variance in $w[k]$ and $v[k]$ are very large. In the next subsection, we will show how EDA will improve the training results by imposing structural information specific to the finger dynamics.

### 2.2 The Eigen Dynamics Analysis Method

We define an eigen-dynamics as the dynamics of intensional flexing/extending ${ }^{1}$ one finger while the other four fingers moving autonomically. Please note that we are not considering each finger as independent to the others, because each eigen-dynamics models all the 20 joint angles in the five fingers. In each training set, all five fingers are moving in a naturally constrained way, although the major motion is performed by one of them. The conjecture is that the five eigen-dynamics span the whole manifold of C. To verify it, we separately trained the five LDS with the corresponding CyberGlove data. Denoting the parameters for the $i^{t h}$ eigen-dynamics with $\hat{\mathbf{S}}^{(i)}=\left\{A_{2 \times 2}^{(i)}, C_{6 \times 2}^{(i)}\right.$, $\left.\Sigma_{w^{(i)} 2 \times 2}, \Sigma_{v^{(i)} 6 \times 6}\right\}$, we obtain the $10^{t h}$ order stochastic LDS $\hat{\mathbf{S}}$ as

$$
\begin{array}{ll}
\hat{A}_{10 \times 10}=\operatorname{diag}_{i=1}^{5}\left\{A_{2 \times 2}^{(i)}\right\} & \Sigma_{\hat{w} 10 \times 10}=\operatorname{diag}_{i=1}^{5}\left\{\Sigma_{w^{\prime} 2 \times 2}^{(i)}\right\} \\
\hat{C}_{6 \times 10}=\left[C_{6 \times 2}^{(1)} \cdots C_{6 \times 2}^{(5)}\right] & \Sigma_{\hat{v} 6 \times 6}=\sum_{i=1}^{5} \frac{1}{5} \Sigma_{v}^{(i)} 6 \times 6
\end{array}
$$

[^0]The fact that $\operatorname{rank}\left(\hat{C}_{6 \times 10}\right)=6$ proves that the five eigendynamics do span the whole manifold of $\mathbf{C}$. The quantitative results in Section 7.1 show that $\hat{\mathbf{S}}^{(i)}$ is sufficient to capture the nonlinearity in each eigen-dynamics. EDA significantly reduce the variance in the LDS $\hat{\mathbf{S}}$, by imposing a specific structure tailored for finger dynamics, that is, $\hat{\mathbf{S}}$ consists of five decoupled subsystems and each corresponding to one eigen-dynamics. $\hat{\mathbf{S}}$ is not similar ${ }^{2}$ to $\hat{\mathbf{S}}$. Therefore decoupling $\hat{\mathbf{S}}$ with standard SVD-based linear algebraic techniques will not give the same result as EDA. In fact, such decoupling would have the same noise variance as that of $\hat{\mathbf{S}}$, which is much larger than that of $\hat{\mathbf{S}}$.

A more careful study on $\hat{\mathbf{S}}^{(i)}$ shows that the five $A_{2 \times 2}^{(i)}$ matrices are very similar. Each subsystem has two modes: one is slightly unstable ${ }^{3}$, the other is stable. For example, $A^{(4)}=\left[\begin{array}{cc}1.0176 & -0.0014 \\ 0.0069 & 0.9910\end{array}\right]$. Physically, we could interpret the unstable component of $\mathbf{X}^{(i)}[k]$ as the joint angle, and the stable one as the angular velocity. The velocity will be driven away from zero by an impulse, and then converge back to zero as the motion stops, while the joint angles will end at a value than the starting value. This sigmoid shape captures the similar dynamics of the inner states $\mathbf{X}^{(i)}$. Nevertheless, the five $C_{6 \times 2}^{(i)}$ matrices are distinct, which characterize the five distinct output spaces. These results are consistent with the biomechanics structure of the hand, that each finger moves in a similar constrained fashion, while their major motions involve different sets of joint angles.

This method of training the subsystems of a high order LDS independently with labelled motion trajectories, is defined as eigen dynamics analysis. The word "eigen" comes from the analogues between PCA and EDA summarized in Table 1.

Table 1. Analogues between PCA and EDA


Figure 1 illustrates how EDA method models the dynamics of $\mathbf{Y}[k]$ in $\Upsilon$. The five ${ }^{4}$ colored cubes span the whole space $\Upsilon$. The dynamic constraints are modelled by the fact that $\mathbf{X}^{(i)}[k]_{2 \times 1}$ can only move along (or near) the colored dashed curve in the 2D state space spanned by $A^{(i)}$. However, since the five $\mathbf{X}^{(i)}[k]$ are moving independently, the

[^1]
[^0]:    ${ }^{1}$ We also study the difference between the dynamics of extending and flexing the same finger. The identification results show that after reversing the time index, they are almost identical, that is, $A_{\text {flexing }}^{(i)}$ $\times$ $A_{\text {extending }}^{(i) \approx I_{2 \times 2}}$, while $C_{\text {flexing }}^{(i)}$ and $C_{\text {extending }}^{(i)}$ are almost the same.

[^1]:    ${ }^{2}$ Two LDS's are similar if there exists a similarity transformation [5] between them.
    ${ }^{3} \mathrm{~A}$ mode is unstable if the eigen value of $A$ corresponding to that mode is larger than $1[5]$.
    ${ }^{4}$ For clarity, we only draw three of them.

![img-0.jpeg](img-0.jpeg)

Figure 1. A conceptual illustration of the manifold spanned by EDA. For clarity, only three of the five eigen-dynamics are drawn in red, green and blue respectively.

Table 2. Notations in Figure 1


combined output $\mathbf{Y}[k]$ can be very nonlinear, just as the actual motion of the hand is.

EDA method stratifies the intrinsic biomechanical nonlinearity from the apparent nonlinearity due to unsynchronized motion among different fingers. The former is modelled by the similar sigmoid-shape nonlinear dynamics of the inner states (the colored dashed curve), while the latter is modelled as the three hidden states $\mathbf{X}^{(i)}[k]$ sliding along the colored dashed curve independently. This stratification enables factored sampling to reduce the sampling space from the whole $\Re^{20}$ to a manifold in $\Re^{10}$ (corresponding to the five random walks along the nonlinear dashed curve induced by $A^{(i)}$ ). In this sense, we claim that EDA can compress the actual dimensionality of the manifold of feasible finger configurations.

To compare EDA method with other LDS-based models, we could introduce an ancillary state as the set of the labels of the active subsystems: $S[k]=\{i \mid i=$ $\{1 \ldots 5\}$ s.t. $\left\|\mathbf{X}^{(i)}[k]-\mathbf{X}^{(i)}[k-1]\right\| \geq \varepsilon>0\}$, where $\varepsilon$ would be a threshold to specify how large motion an ac- tive subsystem should have between consecutive frames. If we further restrict $S[k]$ to have only one element, i.e. only one active subsystem at each time, EDA model becomes similar to switching linear dynamic systems (SLDS) [20] [22], which switches between different LDS. At each time, SLDS only cover one of the subspaces induced by the $\dot{\mathbf{S}}^{(i)}$ subsystems (the colored rectangular cubes), while EDA can cover the whole manifold spanned by all five $\dot{\mathbf{S}}^{(i)}$. To learn $\dot{\mathbf{S}}^{(i)}$, we use the stochastic subspace identification algorithm [31] and do not assume a specific form, unlike, e.g., autoregressive moving average (ARMA) model used in [26] or the AR model used in [8] [35].

## 3 The Dynamic Bayesian Network Based on EDA

Based on EDA, we construct a DBN for tracking global and local hand motion. The tracking problem is formulated as inference both between consecutive frames and within each time frame given the observations.

Table 3. A list of the notations used in the DBN model


![img-1.jpeg](img-1.jpeg)

Figure 2. The dependency graph of the DBN for tracking articulated hand motion.

Figure 2 shows the dependency graph of the DBN depicting dependencies among the state variables and the ob-

servations at each frame. Table 3 lists the notations in the DBN.

Assuming the DBN is first-order Markovian, we can write the posterior of $\mathbf{M}[k]$ and $\mathbf{Z}[k]$ as
$p(\mathbf{M}[k], \mathbf{Z}[k]|V[k], \lambda)=\frac{p(V[k] \mid \mathbf{M}[k], \mathbf{Z}[k], \lambda) \times p(\mathbf{M}[k], \mathbf{Z}[k] \mid \lambda)}{p(V[k] \mid \lambda)}$
where the a priori knowledge $\lambda$ includes: $S H[k-1], \mathbf{M}[k-$ $1]$ and $\mathbf{Z}[k-1] . p(V[k] \mid \lambda)$ is invariant with respect to $\mathbf{M}[k]$ and $\mathbf{Z}[k]$.

With this DBN, tracking hand motion can be cast as the maximum a posteriori (MAP) estimate of $\mathbf{M}[k]$ and $\mathbf{Z}[k]$ given the a priori and the observation $V[k]$. Since $\mathbf{M}[k]$ and $\mathbf{Z}[k]$ are conditionally independent given $\lambda$, we can use divide-and-conquer iteration to find the MAP estimate. Figure 3 shows the flow chart that implements the observation and inference within one frame of the DBN.

## 4 Observation: Likelihood Edge

Given an RGB image $F[k]$, we convert it to a gray-scale image $G[k]$ and an HSI(hue, saturation and intensity) image $H[k]$, which is further converted to a likelihood ratio image $L[k]$ based on $S H[k-1]$ and $B H[k-1]$ as:

$$
L[k](u, v)=\frac{p(H[k](u, v) \mid \text { skin })}{p(H[k](u, v) \mid \text { nonskin })}
$$

for each pixel $(u, v)$. Most color segmentation algorithms [14] threshold the likelihood ratio to get a binary map of labels for different regions. In contrast, we propose not to threshold but to keep the quantitative information of the likelihood ratio and use it as sufficient statistics to generate a new feature called likelihood edge, that is, edge gradients on the likelihood ratio image $L[k]$, denoted by $L E[k]^{8}$. In $G[k]$, we extract grayscale edge $G E[k]$. The edge points are candidates for matching with the sample points on the 2D shape model shown in Figure 5.

## 5 Inference: Divide and Conquer

As Figure 3 shows, the inference flow within one frame consists of two embedded loops: the outer (blue) loop is the divide-and-conquer iteration that solves $\mathbf{M}[k]$ and $\mathbf{Z}[k]$ by maximizing Equation (4) and the inner (green) loop is the ICP iteration for solving $\mathbf{M}[k]$. When divide-and-conquer iteration converges, we update $S H[k]$ and $B H[k]$ according to the current hand region.

[^0]![img-2.jpeg](img-2.jpeg)

Figure 3. The flow chart for Bayesian hand tracking as inference within one frame of the DBN.

The bridge between step (2) and (3) is a 2D shape model shown in Figure 5. It is generated by rendering a 3D geometric hand model from current global pose and taking sample points along its silhouette. The points are given as $\left\{s_{i}=\left(m_{i}, d m_{i}\right), i=1 \ldots M\right\}$, where $m_{i}=\left(u_{i}, v_{i}, 1\right)^{T}$ is the 2D homogeneous coordinate, $d m_{i}=\left(d u_{i}, d v_{i}\right)^{T}$ is the normal direction (pointing from inner region to outer region) of the silhouette at $m_{i}$. Given the 2D shape model, there are many methods to solve for both correspondence and transformation [10]. Among them, the iterative closest point (ICP) algorithm[3] [36] is widely used because of its efficiency and guaranteed convergence to a local maximum. ICP iterates between assigning a binary correspondence based on nearest-neighbor relationship and estimating a transformation based on the correspondence. In our case, we search for the binary matching between the warped sample points and edge points as $F_{E}(i)=\arg \max _{(u, v) \in \wp}\left\{\psi\left(s_{i}, G E(u, v), L E(u, v)\right)\right\}$, where $\wp$ denotes the neighborhood region. The similarity measure $\psi\left(s_{i}, G E(u, v), L E(u, v)\right)=d m_{i}^{T} G E(u, v)+$ $d m_{i}^{T} L E(u, v)$ is the inner product between the normal di-


[^0]:    ${ }^{3}$ Since likelihood is sufficient statistics for classification [15]. The likelihood ratio edge gradient represents the normal direction of the boundary between skin and nonskin regions.

rection of the hand silhouette $s_{i}$ and the edge gradient. When the ICP iteration converges, we use the four-point algorithm [7] to solve for the 3D homography $H$ from $m_{i}[k]=H m_{i}[1], i=1 \ldots M$ where $m_{i}[1]$ is all the sample points in the very first frame and $m_{i}[k]$ is those in the current frame. From $H$, we can uniquely decide [17] 3D rotation $R[k]$ and translation $T[k]$ in $\mathbf{M}[k]=[R[k][T[k]]$.

## 6 Inference: Estimating Finger Configuration

Solving for MAP estimate $\mathbf{E}_{M A P}\{\mathbf{Z}[k] \mid V[k]\}$ (Step(3) in Figure 4) is accomplished by factored sampling in EDA space.

### 6.1 Sampling in EDA space

Since the mapping between $\mathbf{Z}[k]$ and the image feature $V[k]$ is nonlinear, the posterior probability density $p(\mathbf{Z}[k] \mid V[k], \mathbf{Z}[k-1])$ is multi-modal and cannot be approximated as normal. We therefore adopt a stochastic estimation technique based on factored sampling [30] to find the MAP estimate of $\mathbf{Z}[k]$.

When likelihood $p(V[k] \mid \mathbf{Z}[k])$ can be evaluated pointwise but it is infeasible to generate sample from, factored sampling can be used to approximate the MAP estimation. It draws $N$ random samples $Z[k]_{n}(n=1 \ldots N)$ from the prior $p(\mathbf{Z}[k] \mid \mathbf{Z}[k-1])$ and assigns to each sample a weight

$$
\pi[k]_{n}=\frac{p(V[k] \mid \mathbf{Z}[k]=Z[k]_{n})}{\sum_{m=1}^{N} p(V[k] \mid \mathbf{Z}[k]=Z[k]_{m})}
$$

It has been shown that $\lim _{N \rightarrow \infty} \sum_{n=1}^{N} Z[k]_{n} \pi[k]_{n}=$ $\mathbf{E}_{M A P}\{\mathbf{Z}[k] \mid V[k]\}$ [30]. The speed of convergence dependents on how well the samples $Z[k]_{n}$ are generated with respect to the unknown posterior $p(\mathbf{Z}[k] \mid V[k])$. Since

Step(1): Initialization
Use the EDA motion model to predict $\mathbf{M}[k]$ and $\mathbf{Z}[k]$ based on $\mathbf{M}[k-1]$ and $\mathbf{Z}[k-1]$.
Step(2): Solving for global motion
Recover $\mathbf{M}[k]$ with ICP, assuming the finger configuration $\mathbf{Z}[k]$ is fixed.
Step(3): Solving for finger configuration
Find MAP estimate of $\mathbf{Z}[k]$ with factored sampling, assuming $\mathbf{M}[k]$ is fixed.
Step(4): Testing convergence
If the likelihood is lower than a threshold, go back to Step (2); otherwise $\mathrm{k}:=\mathrm{k}+1$, process the next frame.

Figure 4. The divide-and-conquer iteration
![img-3.jpeg](img-3.jpeg)

Figure 5. An example of the rigid planar model for global tracking. Each number stands for a sample point, while the blue line is its normal direction.
evaluating the likelihood is computationally expensive, it is preferable to draw samples from areas where the likelihood $p(V[k] \mid Z[k]_{n})$ is very large, instead of adding up samples with negligible $\pi[k]_{n}$, which leads to importance sampling [2]. Given the true prior $f\left(Z[k]_{n}\right)=p(\mathbf{Z}[k]=$ $Z[k]_{n} \mid \mathbf{Z}[k-1])$ and a function $g_{k}(\mathbf{Z}[k])$ which resembles the unknown posterior, we can draw samples $Z[k]_{n}$ from $g_{k}(\mathbf{Z}[k])$. In order to reflect the use of a different sampling distribution, we need to add a correction term in Equation (6) and get:
$\pi[k]_{n}=\frac{p(V[k] \mid \mathbf{Z}[k]=Z[k]_{n}) f\left(Z[k]_{n}\right) / g\left(Z[k]_{n}\right)}{\sum_{m=1}^{N} p(V[k] \mid \mathbf{Z}[k]=Z[k]_{m}) f\left(Z[k]_{m}\right) / g\left(Z[k]_{m}\right))}$
To draw a new sample at time $k$, we generate a random walk along the trajectory induced by the state transition equation of $\dot{\mathbf{S}}^{(i)}$ :

$$
X^{(i)}[k]_{n}=\left(A^{(i)}\right)^{\left\lfloor w_{n}\right\rfloor} \mathbf{E}\left\{\mathbf{X}^{(i)}[k-1]\right\}
$$

where $\mathbf{E}\left\{\mathbf{X}^{(i)}[k-1]\right\}=\sum_{m=1}^{N} \pi[k-1]_{m} X^{(i)}[k-1]_{m}$ and $w_{n} \sim \mathbf{N}\left(0, \sigma^{(i)}\right)$. Since the observation noise $u_{n}$ is Gaussian, we generate $Z[k]_{n}$ from $X^{(i)}[k]_{n}$ by

$$
\begin{aligned}
& \widetilde{Z}[k]_{n}=\left(U^{T} \sum_{i \in I} C^{(i)} X^{(i)}[k]_{n}\right)+\mathbf{E}\{\mathbf{Z}\} \\
& Z[k]_{n}=\widetilde{Z}[k]_{n}+u_{n} \text { where } u_{n} \sim \mathbf{N}(0, \Sigma)
\end{aligned}
$$

Since the mapping $X^{(i)}[k]_{n} \rightarrow Y^{(i)}[k]_{n} \rightarrow Y[k]_{n} \rightarrow$ $Z[k]_{n}$ is linear, the additive Gaussian noise in each stage can be transformed to equivalent Gaussian noise in $\Re^{20}$.Therefore, the importance function is:

$$
\begin{gathered}
g\left(Z[k]_{n}\right)=\prod_{i=1}^{5} p\left(X^{(i)}[k]_{n} \mid \mathbf{X}^{(i)}[k-1]\right) p\left(Z[k]_{n} \mid \widetilde{Z}[k]_{n}\right) \\
=\prod_{i=1}^{5} \frac{1}{\sigma^{(i)}} \exp \left\{-\frac{\left(w^{(i)}[k]_{n}\right)^{2}}{2 \sigma^{(i)^{2}}}\right\} \frac{1}{|\Sigma|^{1 / 2}} \exp \left\{\frac{1}{2} u^{T}[k]_{n} \Sigma^{-1} u[k]_{n}\right\}
\end{gathered}
$$

This sampling scheme based on EDA stratifies the sampling space into: 1) a manifold due to the uncertainty in the position of each of the five inner states along its own trajectories, which is parameterized as the random walk $w_{n}^{(i)}$ in

the $i^{t h}$ subsystem; 2) the surrounding area due to observation noise in $\Re^{20}$, parameterized as a unimodal Gaussian $u_{n} \sim \mathbf{N}(0, \Sigma)$, with much smaller variance than that of directly sampling in $\Re^{20}$.

### 6.2 Evaluating the Likelihood Function

Given a sample $Z[k]_{n}$, we use a 3D geometric hand model to generate the silhouette from the current global view point. Taking sample points $m_{i}$ along the silhouette, we find their corresponding edge point $F_{E}(i)$ at image position $e_{F_{E}(i)}$, by nearest neighbor search. Assuming the sum of its gray-scale edge strength and its likelihood edge strength is $\zeta\left(F_{E}(i)\right)$, we define the likelihood function as

$$
p\left(V[k] \mid \mathbf{Z}[k]=Z[k]_{n}\right)=\sum_{i=1}^{M} \exp \left\{-\frac{\left\|m_{i}-e_{F_{E}(i)}\right\|^{2}}{\zeta\left(F_{E}(i)\right)}\right\}
$$

which assumes the pixel coordinates of the edge points around sample point $m_{i}$ have independent Gaussian distribution, with mean at $m_{i}$ and the variance being the strength of the edge.
![img-4.jpeg](img-4.jpeg)

Figure 6. Trajectory of the 6 PCA components in flexing the ring finger. The dotted red lines show the collected data, and the green lines show the recovered motion.

## 7 Experimental Results

### 7.1 Quantitative Results for Finger Articulation

In the simulation experiments, we use a 3D geometric hand model to render an image sequence from with the data collected by CyberGlove. To measure the performance of finger tracking without introducing the noise due to global tracker, we assume the ground truth global motion is known. We collect quantitative results of tracking five sequences of different types of motion (labelled as $D_{i}, i=1 \ldots 5$, corresponding to flexing each of the five fingers). Figure 6 shows
the results for the motion $D_{4}$ (flexing the ring finger). Table 4 shows relative mean square error (MSE) in the six dimensional PCA space $\Upsilon$. Relative MSE is defined as the ratio between the absolute MSE and the range of motion (ROM). We choose not to enumerate the MSE in the configuration space $\mathcal{C}$, because it is very lengthy and filled with a lot of insignificant entries corresponding to very small ROM. Since the mapping between $\Upsilon$ and $\mathcal{C}$ is linear, the relative MSE in $\Upsilon$ is sufficient for evaluating the performance of the finger tracking algorithm.

Table 4. The relative MSE in percentage for simulation using 2nd order LDS as the eigen-dynamics model


Table 5. The ROM in each PCA component


In Table 4, some entries are very large, e.g. the relative MSE reaches $21.2 \%$ in the $6^{\text {th }}$ PCA component of motion $D_{3}$ (extending/flexing middle finger). However, considering the ROM for the $6^{\text {th }}$ component is also quite small ${ }^{6}$, only 0.0879 as shown in Table 5, the absolute MSE for that entry is reasonably small.

Table 5 shows the ROM in $\Upsilon$. Table 6 shows the error while tracking finger motion with 1st order LDS as the model of the six eigen-dynamics, which is much larger than that of the 2nd order LDS'es. Using 1st order LDS is similar to the straight-line-fitting method used in [34]), except they assume finger motion is constrained along one of the lines between 28 predefined basis configurations at each time.

Table 6. The relative MSE (in percentage) for simulation using 1st order LDS as the eigen-dynamics model


[^0]
[^0]:    ${ }^{6}$ The $6^{\text {th }}$ component corresponds to the smallest eigen value among those of the six components.

7.2 Quantitative Results for Global Motion

To analyze the performance of global tracking alone, we assume the ground truth finger configuration is known. The trajectory of translation and rotation parameters are shown in Figure 7. The mean square error (MSE) in each dimension is shown in Table 7, where $R(X), R(Y), R(Z)$ denotes rotation along $X, Y, Z$ axis respectively and $T(X), T(Y), T(Z)$ denotes translation along $X, Y, Z$ axis.
![img-5.jpeg](img-5.jpeg)

Figure 7. Trajectory of translation and rotation parameters. The green lines show the original transformation used to synthesis image sequence, the red dots show the global tracking results.

Table 7. MSE, ROM and relative MSE in percentage.


The jittering effects occur when the nearest neighborhood search region covers the edges belonging to two adjacent fingers with very similar gradients. They can be alleviated by applying a smoothing filter when necessary.

### 7.3 Demonstration Using Real-world Data

The global tracker executes at 30 frames per second on an entry level processor (Pentium3 1.0GHz). Combining the local tracker, it slows down to 8 frames per second, partly because we have not optimize the implementation. Figure 8 and Figure 9 show some snapshots from various video clips. These and other video sequences are available at http://www.ifp.uiuc.edu/ hzhou/EDA.

## 8 Conclusions

The main contributions of our work are:

1) We proposed an EDA method to learn a high order LDS depicting the dynamics of natural finger articulation. By imposing a structure tailored for hand motion, EDA separates the intrinsic biomechanical nonlinearity from the nonlinearity due to the asynchrony between different fingers, thus reduces the search space for tracking. 2) We proposed a new feature called likelihood edge, which combines color histogram and edge feature in the observation level. 3) Based on EDA, we implemented a system for tracking both articulation and 3D global hand motion. As the experiments on the synthesized and real-world data show, the system is accurate and robust against cluttered variant background and can handle partial occlusion.

Enumerated below are the limitations of the system:

1) Under certain finger articulations, self-occlusion will affect the evaluation of the likelihood function, such that the MAP estimation given by factored sampling may be far from the actual configuration. In that case, the divide-andconquer iteration will take a long time to converge. 2) Under extreme out-plane rotation, the palm can not be approximated as a planar object. In such cases, the noise in point matching will introduce considerable error into the pose recovering results.
![img-6.jpeg](img-6.jpeg)

Figure 8. Demonstrations of the performance of the global hand tracker. The first two rows show the tracking results under inplane/outplane rotation and 3D translation. The third row shows that the tracker is robust against complex variant background. The fourth row demonstrates that starting from a rough initialization, the system can automatically converge to the actual hand pose. The fifth row shows the robustness against partial occlusion.

![img-7.jpeg](img-7.jpeg)

Figure 9. Demonstrations of the performance of the finger motion tracker.

Acknowledgements This research was supported in part by National Science Foundation, under Grant IIS 01-38965 and Alliance Program. The authors thank Ying Wu, John Lin, Dennis Lin and Bjorn Stenger for the inspiring discussions and selfless help. Special thanks for Ziyou Xiong's proofreading.
