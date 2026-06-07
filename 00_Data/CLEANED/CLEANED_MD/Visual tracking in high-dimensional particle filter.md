# RESEARCH ARTICLE 

## Visual tracking in high-dimensional particle filter

Jingjing Liu*, Ying Chen, Lin Zhou, Li Zhao<br>Key Laboratory of Underwater Acoustic signal Processing of Ministry of Education, Southeast University, Nanjing, Jiangsu, China

* 230149052@seu.edu.cn


## Abstract

In this paper, we propose a novel object tracking algorithm by using high-dimensional particle filter and combined features. Firstly, the refined two-dimensional principal component analysis and the tendency are combined to represent an object. Secondly, we present a framework using high-order Monte Carlo Markov Chain which considers more information and performs more discriminative and efficient on moving objects than the traditional first-order particle filtering. Finally, an advanced sequential importance resampling is applied to estimate the posterior density and obtains the high-quality particles. To further gain the better samples, K-means clustering is used to select more typical particles, which reduces the computational cost. Both qualitative and quantitative evaluations on challenging image sequences demonstrate that the performance of our proposed algorithm is superior to the state-of-the-art methods.

## 1. Introduction

Visual object tracking is a fundamental research topic in computer vision, which plays a critical role in various applications, such as human computer interaction, driverless car, surveillance, and human motion analysis, to name a few. After several decades of visual tracking research, considerable progress has been made, it still remains very challenging for developing an all-situation-handled tracker that successfully handles all scenarios, such as partial occlusions, illumination changes, fast motions, camera motions, background clutter and viewpoint, etc.[1, 2]. Current visual tracking algorithms are classified as either generative or discriminative models. Both of them require filters to obtain the object's candidates. Particle filter [3] also known as Sequential Monte Carlo filter which has been studied actively on object tracking, because it can cope with difficult nonlinear/non-Gaussian dynamic problems. Particle selecting is a matter of prime importance in the particle filter, which impacts the results of tracking objects immediately. Theoretically speaking, large number and high quality of particles could achieve the optimal approximation of the probability distribution [4]. However, the large number of particles means high computation costs such that the way to get high quality of particles is always complicated. Thus the tradeoff between the speed and the discriminative ability becomes a challenge problem to be solved.

The calculation of the particle tracking depends on the complexity of feature extraction and the amount of the sampling particles. Two kinds of methods are very often used to reduce the

decision to publish, or preparation of the manuscript.

Competing interests: The authors have declared that no competing interests exist.
computation costs. One is to create the easier but more effective feature. For example, Perez introduced an ingredients incorporated multi-part color modeling and a background color model to handle color clutter in the background and complete occlusion of the tracked entities over a few frames[5]. Han presented an on-line appearance modeling technique based on sequential density approximation which adopted to variations of lighting condition, pose, scale and view-point over time [6]. Wang represented an object using 2DPCA which combined 2D basis matrices and an additional sparse error matrix [7]. Kong proposed a feature selection method which chose low dimension but more discriminative features [8]. Nevertheless, another alternative way is to reduce the quantity of samples. Ridge regression was employed [9] to decrease the computational costs for it could exclude the outlying particles. Their product sparse coding guaranteed their lower calculation simultaneously. Li reduced the number of particles considerably because of their effective sampling strategy [10]. Joint tracking algorithm adopted the mean shift and particle filter with model updating which could sample fewer particles and perform better performance for similar color appearance and cluttered backgrounds [11]. Shan improved the sampling efficiency using the mean shift optimization and their real-time hand tracking run fast as it used only color and motion cues [12].

Motivated by aforementioned discussions, this paper proposes a supplementary knowledge based high-order particle filtering tracking algorithm. The contributions of this work are threefold: (1) we represent the tracked object using the combined feature including an improved 2DPCA and the supplementary information. 2DPCA is a simple but effective feature which could achieve performance comparable to PCA with less computation costs. The supplementary information such as tendency could enrich the presentation of the object. (2) The high-order particle filter can be used to increase the algorithm's accuracy because more information could be considered as well as more accurate and reliable moving object model could be supported. The traditional first-order Markov model is sensitive to loss of particle information from the previous time instant. For this reason, second-order object motion is widely used in tracking using Bayesian networks. However, it still cannot characterize the dynamics of moving objects. (3) Moreover, k-means clustering, a simple but valid algorithm, is adopted to selecting the sample particles with high possible appearance and further reduces the amount of the samples as it could decrease the computation costs.

The rest of the paper is organized as follows. In Section 2, we introduce our high-order particle filtering with combined features. Then, we present the summary of our proposed tracking algorithm in Section 3. Section 4 explains experimental results and analysis on tracking. Finally, Section 5 gives the conclusions.

## 2. High-order particle filtering with combined features

We begin with a concise review of particle filtering and then introduce our high-order particle filter tracking framework.

### 2.1 Review of particle filtering

Particle filter is a filtering method which has been shown to offer improvements in performance over non-linear or non-Gaussian environment. The traditional particle filter is derived on the first-order Markov chain. Its basic network structure is shown in Fig 1.

Fig 1 represents the structure of the particle filters (PF). The state parameter vector of a target and its observation at time $t$ is denoted as $x_{t}$ and $z_{t}$, respectively. The history of observations from time 1 to $t$ is denoted as $Z_{t}=\left\{z_{1}, \cdots, z_{t}\right\}$. The state-space model is a first-order Markov chain and the current state $x_{t}$ only depends on the previous state $x_{t-1}$. However, particle filters using the first-order Markov model cannot perform on fast moving objects efficiently. The situation

![img-0.jpeg](img-0.jpeg)

Fig 1. Dynamic Bayesian network structure of particle filtering.
https://doi.org/10.1371/journal.pone.0201872.g001
would be worse if the object from the previous time instant is lost. Therefore, the high-order Markov Chain named as m-th-order Markov Chain is required to model the moving objects with high-order dynamics. Compared with the state-space model of the first-order particle filters, an m-th-order Markov chain's current state $x_{t}$ depends on the past $m$ states and we have

$$
p\left(\mathrm{x}_{t} \mid \mathrm{x}_{t-1}, \mathrm{x}_{t-2}, \ldots, \mathrm{x}_{\mathrm{tt}}\right)=p\left(\mathrm{x}_{t} \mid \mathrm{x}_{t-1}, \mathrm{x}_{t-2}, \ldots, \mathrm{x}_{t-m}\right)
$$

# 2.2 Probability propagation of high-order particle filtering 

In particle filtering, the tracking only uses sequential state probability propagation information. The information derived from the states and the objects' prior is also quite useful to influence the sampling strategies and the tracking. In this work, we assume that a target's appearance is modeled by a subspace model and the state space is augmented with the corresponding appearance's supplementary information such that the state $x_{t}=\left(c_{t}, s_{t}\right)$ consists of two parts: the state $c_{t}$, which models the estimated position, and the supplementary information $s_{t}$, containing the moving tendency and so on. The posterior distribution now is described as $P\left(c_{t}, s_{t} \mid Z_{t}\right)$. Unlike the probability $P\left(x_{t} \mid Z_{t}, A\right)$ in the Appearance-Guided Particle Filtering [13], in which the tracking employs further prior of object appearance, we show the solutions using the assist knowledge derived between the sequential states.

Fig 2 shows our first-order framework's Bayesian network structure and the network becomes:

$$
P\left(\mathrm{c}_{t}, \mathrm{~s}_{t} \mid \mathrm{Z}_{t}\right)=k P\left(Z_{t} \mid \mathrm{c}_{t}, \mathrm{~s}_{t}\right) \times \int_{s_{t-1}} \int_{s_{t-1}} P\left(c_{t}, \mathrm{~s}_{t} \mid \mathrm{c}_{t-1}, \mathrm{~s}_{t-1}\right) P\left(\mathrm{c}_{t-1}, \mathrm{~s}_{t-1} \mid Z_{t-1}\right)
$$

The posterior over the current state is influenced by integrating the target state and the assist knowledge at the previous time-step. Once we integrate out the assist part and approximate the filter using a hybrid Monte Carlo Method, the Bayes filter is reduced to Rao-Blackwellized particle filter (RBPF) [14] and the filter would be:

$$
P\left(\mathrm{c}_{t} \mid \mathrm{Z}_{t}\right)=\mathrm{k} \int_{\mathrm{s}_{t}} P\left(Z_{t} \mid c_{t}, \mathrm{~s}_{t}\right) \times \int_{s_{t-1}} \int_{s_{t-1}} P\left(c_{t}, \mathrm{~s}_{t} \mid \mathrm{c}_{t-1}, \mathrm{~s}_{t-1}\right) P\left(c_{t-1}, \mathrm{~s}_{t-1} \mid Z_{t-1}\right)
$$

In a Rao-Blackwellized particle filter, the assumption that the moving model for the state does not depend on the assist information is necessary and the marginal Bayes filter is obtained

![img-1.jpeg](img-1.jpeg)

Fig 2. Bayesian network structure of our first-order framework.
https://doi.org/10.1371/journal.pone.0201872.g002
as follows:

$$
P\left(\mathrm{c}_{t} \mid \mathrm{Z}_{t}\right) \approx \mathrm{k} \sum_{i} w_{t-1}^{(i)} P\left(\mathrm{c}_{t} \mid \mathrm{c}_{t-1}^{(i)}\right) \times \int_{\mathrm{s}_{t}} P\left(\mathrm{Z}_{t} \mid \mathrm{c}_{t}, \mathrm{~s}_{t}\right) \int_{\mathrm{s}_{t-1}} P\left(\mathrm{~s}_{t} \mid \mathrm{c}_{t}, \mathrm{c}_{t-1}^{(i)}, \mathrm{s}_{t-1}\right) \mathrm{s}_{t-1}^{(i)}\left(\mathrm{s}_{t-1}\right)
$$

The approximation to this Bayes network model need an assumption that the motion model for the location at time $t$ does not depend on the previous time-step's knowledge but uses the same importance sampling schemes as with the particle filter. However, if assuming the assist knowledge is independent of the state at the previous time-step and only influence the Bayesian bootstrap or the results of sampling importance resampling, the aforementioned model would degenerates to a BN structure for particle filtering. Hence, we investigate the probability $P\left(\mathrm{x}_{t} \mid \mathrm{Z}_{t}\right)$ as follows:

$$
P\left(x_{t} \mid \mathrm{Z}_{t}\right) \approx P\left(\mathrm{c}_{t} \mid \mathrm{Z}_{t}\right) \propto P\left(\mathrm{Z}_{t} \mid \mathrm{c}_{t}\right) \int P\left(\mathrm{c}_{t} \mid \mathrm{c}_{t-1}\right) \cdot P\left(\mathrm{c}_{t-1} \mid \mathrm{Z}_{t-1}\right) \mathrm{dc}_{t-1}
$$

where a first-order Markov chain of the states is considered. In order to better track the fast moving objects, high-order Markov Model is adopted and its posterior density function $P\left(C_{t} \mid Z_{t}\right)$ is shown in formula 6. Fig 3 provides an example of a second-order hidden Markov model which could give more intuitionistic descriptions. The circle nodes and the square
![img-2.jpeg](img-2.jpeg)

Fig 3. Second-order hidden Markov model.
https://doi.org/10.1371/journal.pone.0201872.g003

nodes denote the states of the object and the observations, respectively.

$$
\begin{aligned}
& P\left(\mathrm{C}_{\mathrm{t}} \mid \mathrm{Z}_{\mathrm{t}}\right)=\frac{p\left(\mathrm{z}_{\mathrm{t}}, \mathrm{C}_{\mathrm{t}}, \mathrm{Z}_{\mathrm{t}-1}\right)}{p\left(\mathrm{z}_{\mathrm{t}}, \mathrm{Z}_{\mathrm{t}-1}\right)} \\
& =\frac{P\left(\mathrm{z}_{\mathrm{t}} \mid \mathrm{C}_{\mathrm{t}}, \mathrm{Z}_{\mathrm{t}-1}\right) P\left(\mathrm{C}_{\mathrm{t}}, \mathrm{Z}_{\mathrm{t}-1}\right)}{P\left(\mathrm{z}_{\mathrm{t}}, \mathrm{Z}_{\mathrm{t}-1}\right)} \\
& =\frac{P\left(\mathrm{z}_{\mathrm{t}} \mid \mathrm{C}_{\mathrm{t}}, \mathrm{Z}_{\mathrm{t}-1}\right) P\left(\mathrm{C}_{\mathrm{t}} \mid \mathrm{Z}_{\mathrm{t}-1}\right)}{P\left(\mathrm{z}_{\mathrm{t}} \mid \mathrm{Z}_{\mathrm{t}-1}\right)} \\
& =\frac{P\left(\mathrm{z}_{\mathrm{t}} \mid \mathrm{C}_{\mathrm{t}}, \mathrm{Z}_{\mathrm{t}-1}\right) P\left(\mathrm{c}_{\mathrm{t}}, \mathrm{C}_{\mathrm{t}-1} \mid \mathrm{Z}_{\mathrm{t}-1}\right)}{P\left(\mathrm{z}_{\mathrm{t}} \mid \mathrm{Z}_{\mathrm{t}-1}\right)} \\
& =\frac{P\left(\mathrm{z}_{\mathrm{t}} \mid \mathrm{C}_{\mathrm{t}}, \mathrm{Z}_{\mathrm{t}-1}\right) P\left(\mathrm{c}_{\mathrm{t}} \mid \mathrm{C}_{\mathrm{t}-1}, \mathrm{Z}_{\mathrm{t}-1}\right) P\left(\mathrm{C}_{\mathrm{t}-1} \mid \mathrm{Z}_{\mathrm{t}-1}\right)}{P\left(\mathrm{z}_{\mathrm{t}} \mid \mathrm{Z}_{\mathrm{t}-1}\right)} \\
& \propto P\left(\mathrm{z}_{\mathrm{t}} \mid \mathrm{C}_{\mathrm{t}}, \mathrm{Z}_{\mathrm{t}-1}\right) P\left(\mathrm{c}_{\mathrm{t}} \mid \mathrm{C}_{\mathrm{t}-1}, \mathrm{Z}_{\mathrm{t}-1}\right) P\left(\mathrm{C}_{\mathrm{t}-1} \mid \mathrm{Z}_{\mathrm{t}-1}\right) \\
& =P\left(\mathrm{z}_{\mathrm{t}} \mid \mathrm{c}_{\mathrm{t}}\right) P\left(\mathrm{c}_{\mathrm{t}} \mid \mathrm{c}_{\mathrm{t}-m: t-1}\right) P\left(\mathrm{C}_{\mathrm{t}-1} \mid \mathrm{Z}_{\mathrm{t}-1}\right)
\end{aligned}
$$

# 2.3 Weight updating of the high-order particle filtering 

As aforementioned, the basic Sequential Importance Resampling (SIR) algorithm given starts from a random measure with equal weight on each of the $N$ sample values and samples $N$ times independently from the set with probabilities to obtain an equally weighted random measure. Exploiting the SIR method, the high-order particle filtering's posterior density can be estimated as

$$
P\left(\mathrm{C}_{\mathrm{t}} \mid \mathrm{Z}_{\mathrm{t}}\right) \approx \sum_{i=1}^{N} \omega_{t}^{i} \delta\left(\mathrm{C}_{\mathrm{t}}-\mathrm{C}_{\mathrm{t}}^{i}\right)
$$

The weight update equation is given by the equation

$$
\omega_{t}^{i} \propto \frac{P\left(\mathrm{z}_{\mathrm{t}} \mid \mathrm{c}_{\mathrm{t}}^{i}\right) \mathrm{P}\left(\mathrm{c}_{\mathrm{t}}^{i} \mid \mathrm{c}_{\mathrm{t}-m: t-1}^{i}\right) \mathrm{P}\left(\mathrm{c}_{\mathrm{t}: t-1}^{i} \mid \mathrm{Z}_{\mathrm{t}-1}\right)}{\mathrm{Q}\left(\mathrm{c}_{\mathrm{t}}^{i} \mid \mathrm{c}_{\mathrm{t}-m: t-1}^{i}, \mathrm{z}_{\mathrm{t}}\right) \mathrm{Q}\left(\mathrm{c}_{\mathrm{t}: t-1}^{i} \mid \mathrm{Z}_{\mathrm{t}-1}\right)}=\omega_{t-1}^{i} \frac{P\left(\mathrm{z}_{\mathrm{t}} \mid \mathrm{c}_{\mathrm{t}}^{i}\right) \mathrm{P}\left(\mathrm{c}_{\mathrm{t}}^{i} \mid \mathrm{c}_{\mathrm{t}-m: t-1}^{i}\right)}{\mathrm{Q}\left(\mathrm{c}_{\mathrm{t}}^{i} \mid \mathrm{c}_{\mathrm{t}-m: t-1}^{i}, \mathrm{z}_{\mathrm{t}}\right)}
$$

where $P\left(z_{t} \mid c_{t}^{i}\right), P\left(c_{t}^{i} \mid c_{t-m: t-1}^{i}\right)$ and $Q\left(c_{t}^{i} \mid c_{t-m: t-1}^{i}, z_{t}\right)$ are the likelihood, the transition probability and the importance density, respectively. Hence, the posterior filtered density $P\left(c_{t-m+1: t}^{i} \mid Z_{t}\right)$ can be shown as

$$
P\left(\mathrm{c}_{\mathrm{t}-m+1: t} \mid \mathrm{Z}_{\mathrm{t}}\right) \approx \sum_{i=1}^{N} \omega_{t}^{i} \delta\left(\mathrm{c}_{\mathrm{t}-m+1: t}-\mathrm{c}_{\mathrm{t}-m+1: t}^{i}\right)
$$

For more details of the derivation, we refer readers to [1]. However, this SIR filter is vulnerable to sample impoverishment, so that the particle distribution cannot give an accurate approximation of the required PDF. Usually, researchers explore large numbers of particles in realistic applications which require more computation. For the sake of reducing computational complexity of particle filters, unequal importance weights measure before resampling is employed to refine the SIR strategy. Then, the importance density $Q\left(c_{t}^{i} \mid c_{t-m: t-1}^{i}, z_{t}\right)$ would be changed to $\omega_{t-1}^{i} Q\left(c_{t}^{i} \mid c_{t-m: t-1}^{i}, z_{t}\right)$ as the new one. The obvious distinction between the refined density $\omega_{t-1}^{i} Q\left(c_{t}^{i} \mid c_{t-m: t-1}^{i}, z_{t}\right)$ and the original density $Q\left(c_{t}^{i} \mid c_{t-m: t-1}^{i}, z_{t}\right)$ is that the refined density adds $\omega_{t-1}^{i}$. The weighted sample points carry more information than an equal number of unweight points. We apply $\omega_{t-1}^{i}$ to our high-order particle filter because its superiority to the SIR filter both in terms of combating sample impoverishment and in computational cost. The

paper [15] is recommended to the readers for more comprehensive and profound understanding to the weighted sample points. Combing the preceding ideas, the proposed high-order particle filter algorithm is presented in Algorithm 1.
Algorithm 1. Proposed Advanced High-order Particle Filtering Algorithm Initialize: Start from a random measure with $M$ support points $\left\{c_{t}^{i}, \omega_{t}^{i}\right\}_{i=1}^{M}$, obtained by stratified sampling, which approximates to the PDF $P\left(c_{0}\right)$
For $t=1,2,3 \ldots$
For $i=1,2, \ldots, M$
Keep particles $c_{t-m t-1}^{i}$
Draw particles $c_{t}^{i} \sim \omega_{t-1}^{i} \mathrm{Q}\left(c_{t}^{i} \mid c_{t-m t-1}^{i}, z_{t}\right)$
Calculate the importance weight $\omega_{t}^{i}$ as in formula (8)
End for $i$
Normalize the importance weight $\omega_{t}^{i}$ according to $\omega_{t}^{i} / \sum_{t=1}^{M} \omega_{t}^{i}$
Estimate $c_{t}$ according to $\sum_{i=1}^{M} \omega_{t}^{i} c_{t}^{i}$
Resample $\left\{c_{t-m+1 t}^{i}, \omega_{t}^{i}\right\}_{i=1}^{M}$
End for $t$

# 2.4 Transition probability $\mathbf{P}\left(\mathbf{c}_{t}^{i} \mid \mathbf{c}_{t-m t-1}^{i}\right)$ and importance density $\mathbf{Q}\left(\mathbf{c}_{t}^{i} \mid \mathbf{c}_{t-m t-1}^{i}, \mathbf{z}_{t}\right)$ 

Compared with the dynamics of the objects from the traditional first-order particle filter, that is given as $x_{t}=a x_{t-1}+b v_{t}$, our dynamics of the tracking object is assumed as $c_{t}=A c_{t-m}+\cdots+$ $E c_{t-2}+F c_{t-1}+G v_{t}$, where $v_{k}$ is modeled as Gaussian distribution $\mu\left(0, \Sigma_{1}\right)$ and $\Sigma_{1}$ is diagonal covariance metrics. In order to calculate the coefficients, maximum-likelihood estimation method is used. The transition probability is given as follows:

$$
P\left(c_{t}^{i} \mid c_{t-m t-1}^{i}\right)=N_{c_{t}^{i}}\left(A c_{t-m}^{i}+\cdots+E c_{t-2}^{i}+F c_{t-1}^{i}, G^{2} \sum_{i}\right)
$$

where $N_{c}(\mu, \Sigma)=(1) /(2 \pi|\Sigma|) \exp (-(1) /(2)(\mathrm{c}-\mu)^{T} \Sigma^{-1}(\mathrm{c}-\mu))$. After obtaining the coefficients, the new samples based on the previous samples could be generated intuitively and the notation is as follows:

$$
c_{t}^{i}=A c_{t-m}^{i}+\cdots+E c_{t-2}^{i}+F c_{t-1}^{i}+H v_{t}
$$

Note that the value of $H$ is the variance of the importance density function. Similar to the transition probability, the importance density could be given as:

$$
\mathrm{Q}\left(\mathrm{c}_{t}^{i} \mid \mathrm{c}_{t-m t-1}^{i}, \mathrm{z}_{t}\right)=N_{c_{t}^{i}}\left(A c_{t-m}^{i}+\cdots+E c_{t-2}^{i}+F c_{t-1}^{i}, H^{2} \sum_{i}\right)
$$

## 2.5 "Extra Step": Analytical update

We have laid the theoretical foundation for the high-order particle filter and derived the probability propagation that is related to the BN as shown in Fig 3. However, our supplementary information is not covered and the valuable information can afford more prove to generate more precise particles. How to apply the supplementary information better is a confusing problem for us. It is widely accepted that large numbers of particles which distribute reasonably could improve the performance of the trackers. Chang explored a mixture distribution which generated two sets of samples from $P\left(x_{t} \mid x_{t-1}\right)$ and $P\left(x_{t} \mid A\right)$, respectively [14]. This method combines particles with both dynamic model-driven information and appearance information and it is effective for visual tracking problems such as articulated hand tracking and lip-contour tracking. The amount of its particles in combined methods is more than the one in

dynamic model which implies high computational cost. However, our original intention is to reduce the computation cost of implementing particle filters which means less particles. Huang used ridge regression to delete the outlying particles to obtain fewer particles [9]. Combining the two different methods above, here, we use $P\left(c_{t}, s_{t} \mid Z_{t}\right)$ to reselect more suitable particles. As shown aforementioned, in order to simplify the model, $M$ particles have been generated using the advanced SIR algorithm and only cover the information of the state $c_{k-m+1: k}^{i}$. Moreover, the supplementary information $s_{t}$ is an important resource to resample the particles. The mixture distribution of $P\left(c_{t}, s_{t} \mid Z_{t}\right)$ is set according to the following equation:

$$
P\left(\mathrm{c}_{\mathrm{t}}, \mathrm{~s}_{\mathrm{t}} \mid \mathrm{Z}_{\mathrm{t}}\right)=\alpha P\left(\mathrm{c}_{\mathrm{t}} \mid \mathrm{Z}_{\mathrm{t}}\right)+(1-\alpha) P\left(\mathrm{s}_{\mathrm{t}} \mid \mathrm{Z}_{\mathrm{t}}\right)
$$

Note that the probability $P\left(c_{t} \mid Z_{t}\right)$ and $P\left(s_{t} \mid Z_{t}\right)$ is caused by the state transition and the supplementary information transition, respectively. When $\alpha$ is set to one, it degenerates to the original particle filtering in which only the dynamical information is used. Form Algorithm 1, we have set $M$ particles using the state transition. Similar to generate $M$ particles, $M_{s}$ particles would be generated based on $P\left(s_{t} \mid Z_{t}\right)$. Here we use the direction of motion as the object's the supplementary information between the frames. Then, the two sets of particles are combined together as a complete sample set whose amount is more than each of them. Since the number of the particles is large, it must exists a method to reduce the computational cost for the sake of obtaining our expected idea. K-means clustering is applied in our method to reduce the amount of sample particles, which is simple but useful to decrease the computational cost. Kmeans clustering is popular for cluster analysis and aims to partition $N$ observations into $k$ clusters in which each observation belongs to the cluster with the nearest mean. Expressing with the mathematical language, the objective of K-means clustering is to find:

$$
\arg \min _{S} \sum_{i=1}^{k} \sum_{x \in S_{i}}\left\|x-\mu_{i}\right\|^{2}
$$

Note that each of observations in the observation sets $\left(x_{1}, x_{2}, \cdots x_{n}\right)$ is a $d$-dimensional real vector and would be partitioned into $k(\leq n)$ sets $S=\left(S_{1}, S_{2}, \cdots S_{n}\right)$, and $\mu_{i}$ is the mean of points in $S_{i}$. One of the most popular heuristics for solving the k -means problem is generalized Lloyd's algorithm. In order to implement Lloyd's algorithm simply and efficiently, the filtering algorithm which is based on storing the multidimensional data points in a kd-tree is applied. A kd-tree represents a hierarchical subdivision of the point set using axis aligned splitting hyperplanes. Given $n$ observations, this produces a tree with $O(n)$ nodes and $O(\log n)$ depth. After using filtering algorithm, the observation set is partitioned into k clusters with its corresponding cluster center. For each cluster, we select half of the observations which are near to the center of each set. Except the sample method using the special distance from the center, a randomly sample method is another useful and practicable way. Certainly, mixed selecting method combining the specific scheme with the random way is definitely doable. Here, the points near the center are selected for the following actions because we do not cut the number of the sample particles so aggressively. Therefore, the amount of the particles would be reduced to half of the original one.

# 3. Proposed tracking algorithm summary 

This tracking algorithm is under the frame of high order particle filter which can be viewed as a Bayesian inference task in a Markov model with hidden state variables. In this paper, the feature extraction is not the most important part in the whole tracking system. Principal component analysis (PCA) is a classical dimension reduction method, which has been used as a

method to extract feature in many areas. The advanced PCA which is called two-dimensional principal component analysis (2DPCA) attracts more attention because of its better performance and less computational cost. Motivated by the advantage of 2DPCA, we represent an object by using 2D matrices. For a series of image matrices $z=\left(z_{1}, z_{2}, \cdots z_{k}\right)$, an orthogonal left-projection matrix $U \in R^{d_{1} \times k_{1}}$, an orthogonal right-projection matrix $V \in R^{d_{1} \times k_{1}}$, and a projection coefficients $C o=\left(C o_{1}, C o_{2}, \cdots C o_{k}\right)$ is obtained by solving the objective function $\min _{U, V, C o_{i}} \frac{1}{k} \sum_{i=1}^{k}\left\|z_{i}-U C o_{i} V^{T}\right\|_{F}^{2}$. The optimizations of the orthogonal left-projection matrix $U$ and the orthogonal right-projections matrix $V$ are computed according to the algorithms in the paper [16] and [17] respectively. Then $C o_{i}$ could be approximated using $U^{T} z_{i} V$. After the projection coefficient is calculated, the likelihood can be obtained by the reconstruction error,

$$
P\left(\mathrm{z}^{i} \mid \mathrm{c}^{i}\right)=\exp \left(-\left\|\mathrm{z}^{i}-U C o^{i} V^{T}\right\|_{F}^{2}\right)
$$

We summarize the algorithm in Algorithm 2.
Algorithm 2. Proposed Tracking Algorithm
Initialize: an observation Matrix $Z$, left- and right- projection matri-
ces $U$ and $V$.
Given a random measure with $M$ support points $\left\{\mathrm{c}_{\mathrm{ij}}^{i}, \omega_{\mathrm{ij}}^{i}\right\}_{i=1}^{M}$, the following steps are performed to construct a new set of samples.
1. select $M$ particles using the proposed advanced high-order particle filtering algorithm
2. select $N$ particles using the supplementary information
3. the distribution of $M+N$ particles is according to $P\left(c_{i}, s_{i} \mid z_{i}\right)$
4. k-means cluster is used to select the more suitable particles
5. measure each particles using $P\left(\mathrm{z}^{i} \mid \mathrm{c}^{i}\right)=\exp \left(-\left\|z^{i}-U C o^{i} V^{T}\right\|_{F}^{2}\right)$
6. choose the best candidate as the current state

# 4. Experiments and analysis 

The proposed algorithm is implemented in Matlab (R2013a) on a personal computer Inter(R) Core(TM) i5-4300U 1.90GHz CPU with 4 GB RAM. The object is initialized manually and the proposed method can process at about 10 frame/s. In order to evaluate the performance of the proposed tracking framework, 13 image sequences are tested in the experiments. These sequences are public which can be obtained from the internet easily and the website address is http://www.visual-tracking.net. Such videos cover most challenging conditions in visual tracking, scale variation, occlusion, rotation, motion blur, background clutter, illumination variation and fast motion.

### 4.1 Ablation study

In order to demonstrate the feasibility of the proposed high-dimensional methods, we summarize the performance of our proposed tracker and the trackers without some variants in Table 1. 2DPCA tracking is a base tracker and its MATLAB source codes could be downloaded on http://ice.dlut.edu.cn/lu/publications.html. The tracker with combined features here is an alternation of the 2DPCA tracker which changes the 2DPCA feature of the original tracker into the combined features and the combined features comprise 2DPCA and tendency. The third tracker named 2DPCA_HDPF is built by changing the $l-1$ regulation of the 2DPCA tracker into high-order particle filter. The combined features_HDPF tracker is made by abandoning the k -means cluster from the proposed tracker and it is also can be written as ours_without cluster tracker. Throughout the comparisons between the 5 trackers, it is easily concluded that the proposed tracker performs the best and all the parts of the proposed

Table 1. Comparison in terms of success rate.


https://doi.org/10.1371/journal.pone.0201872.t001
tracker are useful to improve the performance. Noticed that ours performs better than ours_without cluster and it only rises about 0.4 because the difference between the two trackers is a k-means cluster method. The proposed algorithm runs faster than the combined features_HDPF tracker.

To further illustrate the efficiency of the proposed method, the experiments on tracking accuracy versus number of particles have been made subsequently. Three different trackers are selected to participate the experiments and those are the 2DPCA tracker, the Combined features_HDPF tracker and ours. Fig 4 shows the average center error mean with different number of particle sampling for each tracker and its general trend appears to be decrease with increasing number of sample particle. However, the average center error mean cannot drop steadily but remains almost constant when the number of sample particle is more than 800. The proposed method could achieve an acceptable performance when the number of sample particle is 400 . In the paper, we set 400 as the number of the particle sampling which reaches the balance between the computation and the performance.

# 4.2 Comparison with state-of-the-art trackers 

We evaluate our tracker against 13 state-of-the-art algorithms, including IVT tracking [18], MIL tracking [19], DFT tracking [20], L1APG tracking [21], ASLA tracking [22], DLT tracking [23], SCM tracking [24], 2DPCA tracking [15], SCT tracking [8], TLD tracking [25], VTD tracking [26], Struck tracking [27] and SPC tracking [28]. The source codes for all the evaluated trackers can be downloaded from the internet. For fair comparisons, all the evaluated trackers are initialized with the same parameters.
![img-3.jpeg](img-3.jpeg)

Fig 4. Center error mean with different sampling particles.
https://doi.org/10.1371/journal.pone.0201872.g004

Table 2. Comparison in terms of the center error mean and standard deviation (in pixel).


https://doi.org/10.1371/journal.pone.0201872.t002

For the purpose of assessing the performance of the proposed tracker, we conduct quantitative comparisons between the proposed method and other algorithms using the PASCAL VOC criterion score [29]. Table 2 shows that the proposed method can achieve an excellent tracking result in most sequences in terms of both the average and the standard of center error. Even so, the proposed algorithm improves the performance about 5.8 and 6.7 pixels compared with the tracker which is second best. In addition, Table 3 shows the success rate provided by our proposed tracker and other approaches on 13 sequences. The proposed tracker shows the optimal or suboptimal performance in almost all the sequences, which obtains a mean success rate of $90.19 \%$. However, our method runs slower than SCT. Although ours is either the most accurate or the fastest one, ours do the best within an acceptable scale.

# 5. Conclusions

In this paper we propose a high degree particle filter with the methods to reduce the particles for robust visual tracking. We represent the tracked object by 2DPCA and the tendency of the object and model tracking under the frame of high degree particle filter. In order to reduce the computational cost, K-means cluster is used to select the more suitable particles. Then,

Table 3. Comparison in terms of success rate.


https://doi.org/10.1371/journal.pone.0201872.t003 reconstruction error is adopted to judge the best candidate. Experiments on challenging video clips demonstrate the robustness of the proposed algorithm.

# Acknowledgments 

This research project was supported in part by National Natural Science Foundation of China (No. 61375028, No. 61571106, No. 61673108), Natural Science Foundation of Jiangsu Province, China (No. BK20161517). The authors would like to thank the anonymous reviewers and the associate editor for their valuable comments they provided.

## Author Contributions

Conceptualization: Jingjing Liu.
Funding acquisition: Li Zhao.
Methodology: Jingjing Liu, Ying Chen.
Resources: Ying Chen.
Supervision: Li Zhao.
Writing - original draft: Jingjing Liu.
Writing - review \& editing: Lin Zhou, Li Zhao.
