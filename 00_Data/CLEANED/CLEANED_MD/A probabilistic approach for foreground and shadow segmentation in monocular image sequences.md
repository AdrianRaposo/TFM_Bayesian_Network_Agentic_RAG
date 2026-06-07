# A Probabilistic Approach for Foreground and Shadow Segmentation in Monocular Image Sequences 

Yang Wang ${ }^{1,2 *}$, Tele Tan ${ }^{3}$, Kia-Fock Loe ${ }^{2}$, and Jian-Kang Wu ${ }^{1}$<br>${ }^{1}$ Institute for Infocomm Research, yang.wang@ieee.org, jiankang@i2r.a-star.edu.sg<br>${ }^{2}$ Department of Computer Science, National University of Singapore, loekf@comp.nus.edu.sg<br>${ }^{3}$ Department of Computing, Curtin University of Technology, teletan@cs.curtin.edu.au

## Summary

This paper presents a probabilistic approach for robust foreground segmentation that distinguishes moving objects from their moving cast shadows in indoor image sequences. Both foreground and shadow can be detected even in monocular grayscale sequences. To handle nonstationariness, the background, shadow, and edge models are set up and adaptively updated. A Bayesian framework is proposed to unify the various information including the segmentation label, background, intensity, and edge. The notion of Markov random field is used to encourage the spatial connectivity of the segmented regions. The solution is obtained by maximizing the posterior probability density of the segmentation field. Experiments on the test data show that our technique greatly improves the accuracy of segmentation.

[^0]
[^0]:    *Corresponding author

# A Probabilistic Approach for Foreground and Shadow Segmentation in Monocular Image Sequences 

Yang Wang ${ }^{1,2}$, Tele Tan ${ }^{3}$, Kia-Fock Loe ${ }^{2}$, and Jian-Kang Wu ${ }^{1}$<br>${ }^{1}$ Institute for Infocomm Research, yang.wang@ieee.org, jiankang@i2r.a-star.edu.sg<br>${ }^{2}$ Department of Computer Science, National University of Singapore, loekf@comp.nus.edu.sg<br>${ }^{3}$ Department of Computing, Curtin University of Technology, teletan@cs.curtin.edu.au


#### Abstract

This paper presents a novel method of foreground and shadow segmentation in monocular indoor image sequences. The models of background, edge information, and shadow are set up and adaptively updated. A Bayesian network is proposed to describe the relationships among the segmentation label, background, intensity, and edge information. A MAP-MRF (maximum a posteriori - Markov random field) estimation is used to boost the spatial connectivity of segmented regions.


Keywords: Bayesian network, foreground segmentation, graphical model, Markov random field, shadow detection.

## 1. Introduction

Detecting dynamic objects in image sequences is very important in application areas such as surveillance and objectbased coding. Effective and efficient background removal is critical in these systems. Background subtraction based on intensity or color is a commonly used technique to detect foreground objects. The background model is built from observed images and foreground elements are identified if they show significant difference from the background.

To deal with illumination or object changes in the background, many researchers [1] [2] have abandoned nonadaptive methods of backgrounding. The accumulation of errors in the background over time makes the method useful only in stationary environments. Friedman and Russell [3] classify each pixel by a probabilistic model of how that pixel looks when it is part of different classes and use an incremental EM algorithm to learn the pixel model. Stauffer and Grimson [4] model each pixel as a mixture of Gaussians and update the model in an adaptive way. The Gaussian distributions are then evaluated to determine which are possibly from a background process. Elgammal et al. [5] employ kernel density estimation for nonparametric background modeling. Recently, hidden Markov models [6] [7] have been used to model the dynamical dependencies in the background process.

Besides the nonstationariness of the background, camouflage and shadow are two classic problems of subtraction. If foreground objects have similar colors as the background, they may be erroneously removed from the scene. In addition, moving shadows cast on the background may be erroneously detected as foreground [8]. Depth computation from stereo cameras can be used to handle these two problems [9]. For monocular color video sequences, false segmentation caused by shadows can be reduced by computing differences in a normalized color space that is insensitive to illumination change [10] [11]. Moreover, edge information can be employed to improve the reliability of the results [12]. Stauder et al. [13] assume that static edges in the background remain under shadow and penumbras exist at the boundary of shadows. However, this is sometimes not true due to the properties of the imaging process. Mikic et al. [14] instead approximate the change of the camera response for the shadowed region by a diagonal matrix.

On the other hand, graphical probabilistic models provide a natural tool for handling uncertainty and complexity through the combination of probability theory and graph theory. In particular, Bayesian belief networks and Markov random fields are playing increasingly important roles in the design and analysis of machine intelligent systems [15]. Graphical models have attracted more and more attention in vision applications such as traffic scene analysis [16] [17], layer extraction from image sequences [18], and human motion tracking [19].

To solve the above mentioned problems in monocular indoor grayscale sequences, a unified framework of foreground segmentation is proposed in this paper. We introduce a Bayesian network to combine the background, intensity, and

edge information. A generalized model is built for the appearance change under shadow. Camouflage is decreased by encouraging the formation of continuous segmentation regions. Parameters in the model can be updated adaptively. The solution is obtained by maximizing the posterior probability density of the segmentation field using a noniterative algorithm. Experiments show that our method greatly improves the accuracy of segmentation. The rest part of the paper is arranged as follows: Section 2 presents the formulation of the models. Section 3 and 4 describes the segmentation method. Section 5 proposes the implementation details. Section 6 discusses the experimental results. At the end, our technique is concluded in Section 7.

# 2. Model Representation 

Given the image sequence $\left\{g_{k}\right\}$, we would like to classify each pixel of each image as foreground (moving object), shadow, or background. The segmentation label for a point is defined as

$$
s_{k}(\mathbf{x})=\left\{\begin{array}{l}
1, \text { if site } \mathbf{x} \text { is in the background } \\
2, \text { if site } \mathbf{x} \text { is shadowed by the foreground, } \forall \mathbf{x} \in \mathbf{X}, k=1,2, \ldots, \\
3, \text { if site } \mathbf{x} \text { is in the foreground }
\end{array}\right.
$$

where $s_{k}(\mathbf{x})$ is the label of a single pixel $\mathbf{x}$ within the image at time $k$, and $\mathbf{X}$ is the spatial domain of the video scene. Static shadows are considered to be part of the background. The entire segmentation field is expressed compactly as $s_{k}$.

### 2.1. Background Model

In order to segment the foreground in a video sequence, the system must first model the background of the video scene. Each image acquired by the camera contains noise components. Assume that independent Gaussian noise corrupts each pixel in the scene, so that the observation model for the background becomes

$$
b_{k}(\mathbf{x})=\mu_{b, k}(\mathbf{x})+n_{k}(\mathbf{x})
$$

where random variable $b_{k}(\mathbf{x})$ is the intensity of a single pixel $\mathbf{x}$ within the background at time $k$, and $\mu_{b, k}(\mathbf{x})$ is the intensity mean. $n_{k}(\mathbf{x})$ is the independent zero-mean additive noise with variance $\sigma_{b, k}^{2}(\mathbf{x})$ at time $k$. The parameter vector $\left(\mu_{b, k}(\mathbf{x}), \sigma_{b, k}^{2}(\mathbf{x})\right)^{T}$ is denoted as $\boldsymbol{\theta}_{b, k}(\mathbf{x})$, and the entire background is expressed as $\boldsymbol{\theta}_{b, k}$. For each site $\mathbf{x}$ in the background,

the mean intensity and variance at time $k$ could be estimated from its history. In this work, the intensity of each point is represented by its grayscale value, which ranges from 0 to $y_{\max }=255$.

# 2.2. Edge Model 

The edge model is built by applying the edge operator to the scene, which produces a horizontal difference image and a vertical difference image. For the $k$ th frame $g_{k}, \mathbf{e}_{g, k}(\mathbf{x})$ is the edge vector at site $\mathbf{x}=\left(x_{1}, x_{2}\right)$,

$$
\begin{aligned}
& \mathbf{e}_{g, k}(\mathbf{x})=\left(e_{g, k}^{h}(\mathbf{x}), e_{g, k}^{v}(\mathbf{x})\right)^{T} \\
& e_{g, k}^{h}(\mathbf{x})=g_{k}\left(x_{1}+1, x_{2}\right)-g_{k}\left(x_{1}-1, x_{2}\right) \\
& e_{g, k}^{v}(\mathbf{x})=g_{k}\left(x_{1}, x_{2}+1\right)-g_{k}\left(x_{1}, x_{2}-1\right)
\end{aligned}
$$

where $g_{k}(\mathbf{x})$ is the intensity of a single point $\mathbf{x}$ within the $k$ th video frame, $e_{g, k}^{h}(\mathbf{x})$ and $e_{g, k}^{v}(\mathbf{x})$ are the horizontal difference and vertical difference, respectively. The entire difference image is expressed as $\mathbf{e}_{g, k}$.

Similarly, we can define the edge information for the background,

$$
\begin{aligned}
& \mathbf{e}_{b, k}(\mathbf{x})=\left(e_{b, k}^{h}(\mathbf{x}), e_{b, k}^{v}(\mathbf{x})\right)^{T} \\
& e_{b, k}^{h}(\mathbf{x})=b_{k}\left(x_{1}+1, x_{2}\right)-b_{k}\left(x_{1}-1, x_{2}\right) \\
& e_{b, k}^{v}(\mathbf{x})=b_{k}\left(x_{1}, x_{2}+1\right)-b_{k}\left(x_{1}, x_{2}-1\right)
\end{aligned}
$$

From the background model we know that $\mathbf{e}_{b, k}(\mathbf{x})$ is of bivariate normal distribution with mean difference $\mu_{\mathbf{e}, k}(\mathbf{x})$ and covariance matrix $\boldsymbol{\Sigma}_{\mathbf{e}, k}(\mathbf{x})$ for each site $\mathbf{x} . \mu_{\mathbf{e}, k}(\mathbf{x})$ is determined by the intensity means of the four neighboring points,

$$
\begin{aligned}
& E\left[e_{b, k}^{h}(\mathbf{x})\right]=\mu_{b, k}\left(x_{1}+1, x_{2}\right)-\mu_{b, k}\left(x_{1}-1, x_{2}\right) \\
& E\left[e_{b, k}^{v}(\mathbf{x})\right]=\mu_{b, k}\left(x_{1}, x_{2}+1\right)-\mu_{b, k}\left(x_{1}, x_{2}-1\right)
\end{aligned}
$$

By the independent noise assumption in the background model, $\boldsymbol{\Sigma}_{\mathbf{e}, k}(\mathbf{x})$ can be calculated from the variances of the neighboring points,

$$
\begin{aligned}
& \operatorname{Var}\left[e_{b, k}^{h}(\mathbf{x})\right]=\sigma_{b, k}^{2}\left(x_{1}+1, x_{2}\right)+\sigma_{b, k}^{2}\left(x_{1}-1, x_{2}\right) \\
& \operatorname{Var}\left[e_{b, k}^{v}(\mathbf{x})\right]=\sigma_{b, k}^{2}\left(x_{1}, x_{2}+1\right)+\sigma_{b, k}^{2}\left(x_{1}, x_{2}-1\right)
\end{aligned}
$$

$$
\operatorname{Cov}\left[e_{b, k}^{b}(\mathbf{x}), e_{b, k}^{r}(\mathbf{x})\right]=0
$$

The parameter vector $\left(\boldsymbol{\mu}_{\mathbf{c}, k}(\mathbf{x}), \boldsymbol{\Sigma}_{\mathbf{c}, k}(\mathbf{x})\right)^{T}$ is denoted as $\boldsymbol{\theta}_{\mathbf{c}, k}(\mathbf{x})$, and the entire field at time $k$ is expressed as $\boldsymbol{\theta}_{\mathbf{c}, k}$. The edge model can be used to locate changes in the structure of the scenes as edges appear, vanish, or rotate.

# 2.3. Shadow Model 

Given the background intensity of a point $\mathbf{x}$ when illuminated, we use a linear transformation to approximate the change of intensity for the same point when shadowed in the video frame at time $k$,

$$
g_{k}(\mathbf{x})=a_{k} b_{k}(\mathbf{x})+c_{k}, \text { if } s_{k}(\mathbf{x})=2
$$

When $a_{k}$ equals 1 , the edge information will not change if the area is shadowed by the foreground. Moreover, if we extend the image input from one-channel (grayscale) to multi-channel (R, G, B), the chromaticity [10] [17] will remain unchanged under such a linear transformation when $c_{k}$ is zero. So the shadow model can be viewed as the generalization of the previous assumptions. With this model for the appearance change, we can easily estimate means and variances for the points under shadow. For a point $\mathbf{x}$ under shadow, its intensity mean is $a_{k} \mu_{b, k}(\mathbf{x})+c_{k}$, and its variance is $a_{k}^{2} \sigma_{b, k}^{2}(\mathbf{x})$ at time $k$. Thus the mean of pixel intensity under shadow is controlled by $a_{k}$ and $c_{k}$, and the variance is controlled by $a_{k}$. At the beginning $a_{0}$ and $c_{0}$ are manually initialized according to the visual environment, then parameters $a_{k}$ and $c_{k}$ are adaptively updated over time (see Section 5.1).

## 3. Adaptive Backgrounding

For static background, a sequence of background images may be recorded at the beginning and the intensity mean and variance of each pixel can be calculated.

For nonstationary background, the update method is based on the ideas from Stauffer et al. [4] and Harville et al. [20]. The recent history of each pixel, $\left\{g_{i}(\mathbf{x})\right\}_{1 \leq i \leq k}$, is modeled by a mixture of Gaussian distributions. The probability of the current observation is

$$
\begin{aligned}
& p\left(g_{k}(\mathbf{x})\right)=\sum_{i=1}^{K} w_{i, k}(\mathbf{x}) p\left(g_{k}(\mathbf{x}) \mid \mu_{i, k}(\mathbf{x}), \sigma_{i, k}^{2}(\mathbf{x})\right) \\
& p\left(g_{k}(\mathbf{x}) \mid \mu_{i, k}(\mathbf{x}), \sigma_{i, k}^{2}(\mathbf{x})\right)=\frac{1}{\sqrt{2 \pi} \sigma_{i, k}(\mathbf{x})} \exp \left\{-\frac{1}{2 \sigma_{i, k}^{2}(\mathbf{x})}\left[g_{k}(\mathbf{x})-\mu_{i, k}(\mathbf{x})\right]^{2}\right\}
\end{aligned}
$$

where $K$ is the number of distributions (Usually from three to five are used.), $w_{i, k}(\mathbf{x})$ is the normalized weight of the $i$ th Gaussian in the mixture at time $k, \mu_{i, k}(\mathbf{x})$ and $\sigma_{i, k}^{2}(\mathbf{x})$ are the mean and variance of the $i$ th Gaussian at time $k$.

At current time $k$, each new value $g_{k}(\mathbf{x})$ is checked to match the existing Gaussian distributions (The value is matched if it is within 3 standard deviations of a distribution.). If the $i$ th Gaussian is found to match the new value, its distribution parameters are updated as follows,

$$
\begin{aligned}
w_{i, k}(\mathbf{x}) & =(1-\alpha) w_{i, k-1}(\mathbf{x})+\alpha \\
\mu_{i, k}(\mathbf{x}) & =(1-\alpha) \mu_{i, k-1}(\mathbf{x})+\alpha g_{k}(\mathbf{x}) \\
\sigma_{i, k}^{2}(\mathbf{x}) & =(1-\alpha) \sigma_{i, k-1}^{2}(\mathbf{x})+\alpha\left(g_{k}(\mathbf{x})-\mu_{i, k-1}(\mathbf{x})\right)^{2}
\end{aligned}
$$

where $\alpha$ is the learning rate. (8) is equivalent to the expectation with an exponential factor for the past values. For unmatched distributions, the means and variances remain the same, while the weights should be renormalized. If none of the distributions are matched, the distribution of the lowest weight is replaced with a Gaussian with the new value as its mean, initially low weight and high variance.

As the parameters of the mixture model change, the Gaussian distribution that has the highest ratio of weight over variance is chosen as the background model for each site.

$$
\boldsymbol{\theta}_{b, k}(\mathbf{x})=\left(\mu_{m_{\mathbf{x}}, k}(\mathbf{x}), \sigma_{m_{\mathbf{x}}, k}^{2}(\mathbf{x})\right)^{T}
$$

where $m_{\mathbf{x}}=\arg \max _{i} \frac{w_{i, k}(\mathbf{x})}{\sigma_{i, k}(\mathbf{x})}$. Each time after background updating, the background edge information $\boldsymbol{\theta}_{\mathbf{x}, k}$ at time $k$ can be calculated by (4) and (5).

# 4. Bayesian Foreground Detection 

To extract the foreground given the current frame $g_{k}$, difference image $\mathbf{e}_{g, k}$, background $\boldsymbol{\theta}_{b, k}$, and background edge information $\boldsymbol{\theta}_{\mathbf{e}, k}$, we wish to compute the maximum a posteriori (MAP) estimation of the segmentation field $s_{k}$. Using the Bayes' rule and ignoring the constants with respect to the unknowns,

$$
\begin{aligned}
& \hat{s}_{k}=\arg \max _{s_{k}} p\left(s_{k} \mid \boldsymbol{\theta}_{b, k}, \boldsymbol{\theta}_{\mathbf{e}, k}, g_{k}, \mathbf{e}_{g, k}\right) \\
& =\arg \max _{s_{k}} p\left(s_{k}, \boldsymbol{\theta}_{b, k}, \boldsymbol{\theta}_{\mathbf{e}, k}, g_{k}, \mathbf{e}_{g, k}\right) \\
& =\arg \max _{s_{k}} p\left(\boldsymbol{\theta}_{b, k}, \boldsymbol{\theta}_{\mathbf{e}, k}, g_{k}, \mathbf{e}_{g, k} \mid s_{k}\right) p\left(s_{k}\right)
\end{aligned}
$$

where $\boldsymbol{\theta}_{b, k}$ is defined in Section 2.1, $\mathbf{e}_{g, k}$ and $\boldsymbol{\theta}_{\mathbf{e}, k}$ are described in Section 2.2. The likelihood model $p\left(\boldsymbol{\theta}_{b, k}, \boldsymbol{\theta}_{\mathbf{e}, k}, g_{k}, \mathbf{e}_{g, k} \mid s_{k}\right)$ and the prior model $p\left(s_{k}\right)$ must be defined for the video sequence.

### 4.1. Likelihood Model

Assuming conditional independence among spatially distinct observations, we factorize the likelihood model as

$$
\begin{aligned}
& p\left(\boldsymbol{\theta}_{b, k}, \boldsymbol{\theta}_{\mathbf{e}, k}, g_{k}, \mathbf{e}_{g, k} \mid s_{k}\right) \\
& =\prod_{\mathbf{x} \in \mathbf{X}} p\left(\boldsymbol{\theta}_{b, k}(\mathbf{x}), \boldsymbol{\theta}_{\mathbf{e}, k}(\mathbf{x}), g_{k}(\mathbf{x}), \mathbf{e}_{g, k}(\mathbf{x}) \mid s_{k}(\mathbf{x})\right)
\end{aligned}
$$

Figure 1. A Bayesian network for foreground segmentation.

The relationships among $s_{k}(\mathbf{x}), \boldsymbol{\theta}_{b, k}(\mathbf{x}), \boldsymbol{\theta}_{\mathbf{e}, k}(\mathbf{x}), g_{k}(\mathbf{x})$, and $\mathbf{e}_{g, k}(\mathbf{x})$ can be modeled by a Bayesian network in Figure 1. Given the segmentation label, background, and background edge information at the site, we assume that the image intensity is independent on the image edge. The conditional independence relationships implied by the belief network allow us to represent the joint more compactly [21]. Using the chain rule, the likelihood can be factorized as the product of the intensity likelihood $p\left(g_{k}(\mathbf{x}) \mid \boldsymbol{\theta}_{b, k}(\mathbf{x}), s_{k}(\mathbf{x})\right)$ and edge likelihood $p\left(\mathbf{e}_{g, k}(\mathbf{x}) \mid \boldsymbol{\theta}_{\mathbf{e}, k}(\mathbf{x}), s_{k}(\mathbf{x})\right)$ at site $\mathbf{x}$.

$$
\begin{aligned}
& p\left(\boldsymbol{\theta}_{b, k}(\mathbf{x}), \boldsymbol{\theta}_{\mathbf{e}, k}(\mathbf{x}), g_{k}(\mathbf{x}), \mathbf{e}_{g, k}(\mathbf{x}) \mid s_{k}(\mathbf{x})\right) \\
& =p\left(\boldsymbol{\theta}_{b, k}(\mathbf{x})\right) p\left(\boldsymbol{\theta}_{\mathbf{e}, k}(\mathbf{x})\right) p\left(g_{k}(\mathbf{x}) \mid \boldsymbol{\theta}_{b, k}(\mathbf{x}), s_{k}(\mathbf{x})\right) p\left(\mathbf{e}_{g, k}(\mathbf{x}) \mid \boldsymbol{\theta}_{\mathbf{e}, k}(\mathbf{x}), s_{k}(\mathbf{x})\right) \\
& \propto p\left(g_{k}(\mathbf{x}) \mid \boldsymbol{\theta}_{b, k}(\mathbf{x}), s_{k}(\mathbf{x})\right) p\left(\mathbf{e}_{g, k}(\mathbf{x}) \mid \boldsymbol{\theta}_{\mathbf{e}, k}(\mathbf{x}), s_{k}(\mathbf{x})\right)
\end{aligned}
$$

When site $\mathbf{x}$ is labeled as the background, we can calculate the intensity likelihood model $p\left(g_{k}(\mathbf{x}) \mid \boldsymbol{\theta}_{b, k}(\mathbf{x}), s_{k}(\mathbf{x})\right)$ using the background model,

$$
\begin{aligned}
& p\left(g_{k}(\mathbf{x}) \mid \boldsymbol{\theta}_{b, k}(\mathbf{x}), s_{k}(\mathbf{x})=1\right) \\
& =\frac{1}{\sqrt{2 \pi} \sigma_{b, k}(\mathbf{x})} \exp \left\{-\frac{1}{2 \sigma_{b, k}^{2}(\mathbf{x})}\left[g_{k}(\mathbf{x})-\mu_{b, k}(\mathbf{x})\right]^{2}\right\}
\end{aligned}
$$

When site $\mathbf{x}$ is shadowed, the density can be calculated by the shadow model,

$$
\begin{aligned}
& p\left(g_{k}(\mathbf{x}) \mid \boldsymbol{\theta}_{b, k}(\mathbf{x}), s_{k}(\mathbf{x})=2\right) \\
& =\frac{1}{\sqrt{2 \pi} a_{k} \sigma_{b, k}(\mathbf{x})} \exp \left\{-\frac{1}{2 a_{k}^{2} \sigma_{b, k}^{2}(\mathbf{x})}\left[g_{k}(\mathbf{x})-a_{k} \mu_{b, k}(\mathbf{x})-c_{k}\right]^{2}\right\}
\end{aligned}
$$

When site $\mathbf{x}$ is labeled as the foreground, the background has no contribution to the image intensity information. Uniform distribution is assumed for the pixel. The conditional probability density becomes

$$
\begin{aligned}
& p\left(g_{k}(\mathbf{x}) \mid \boldsymbol{\theta}_{b, k}(\mathbf{x}), s_{k}(\mathbf{x})=3\right) \\
& =p\left(g_{k}(\mathbf{x}) \mid s_{k}(\mathbf{x})=3\right) \\
& =\frac{1}{y_{\max }}
\end{aligned}
$$

Here $\left[0, y_{\max }\right]\left(y_{\max }=255\right)$ is the range of grayscale value for pixel intensity.

Figure 2. The first-order neighborhood system.

For each point $\mathbf{x}$, denote the set of its four nearest neighboring points by $M_{\mathbf{x}}$ (the first-order neighborhood, see Figure 2). Consider the spatial connectivity of the image, we assume the neighboring points have the same segmentation labels. Thus the edge likelihood $p\left(\mathbf{e}_{g, k}(\mathbf{x}) \mid \mathbf{e}_{b, k}(\mathbf{x}), s_{k}(\mathbf{x})\right)$ can be approximated by

$$
\begin{aligned}
& p\left(\mathbf{e}_{g, k}(\mathbf{x}) \mid \boldsymbol{\theta}_{\mathbf{e}, k}(\mathbf{x}), s_{k}(\mathbf{x})\right) \\
& \approx p\left(\mathbf{e}_{g, k}(\mathbf{x}) \mid \boldsymbol{\theta}_{\mathbf{e}, k}(\mathbf{x}), s_{k}(\mathbf{y})=s_{k}(\mathbf{x}), \forall \mathbf{y} \in M_{\mathbf{x}}\right) \\
& =p\left(\mathbf{e}_{g, k}(\mathbf{x}) \mid \boldsymbol{\theta}_{\mathbf{e}, k}(\mathbf{x}), \prod_{\mathbf{y} \in M_{\mathbf{x}}} s_{k}(\mathbf{y})=s_{k}(\mathbf{x})^{M_{\mathbf{x}} \mid}\right)
\end{aligned}
$$

where $\left|M_{\mathbf{x}}\right|$ is the number of elements in the set.

Similarly, when the neighborhood area $M_{\mathbf{x}}$ belongs to the background, the density can be computed by the edge model,

$$
\begin{aligned}
& p\left(\mathbf{e}_{g, k}(\mathbf{x}) \mid \boldsymbol{\theta}_{\mathbf{e}, k}(\mathbf{x}), \prod_{\mathbf{y} \in M_{\mathbf{x}}} s_{k}(\mathbf{y})=1\right) \\
& =\frac{1}{2 \pi \sqrt{\left|\Sigma_{\mathbf{e}, k}(\mathbf{x})\right|}} \exp \left\{-\frac{1}{2}\left[\mathbf{e}_{g, k}(\mathbf{x})-\boldsymbol{\mu}_{\mathbf{e}, k}(\mathbf{x})\right]^{T} \Sigma_{\mathbf{e}, k}^{-1}(\mathbf{x})\left[\mathbf{e}_{g, k}(\mathbf{x})-\boldsymbol{\mu}_{\mathbf{e}, k}(\mathbf{x})\right]\right\}
\end{aligned}
$$

When the neighborhood area $M_{\mathbf{x}}$ is shadowed, the density can be computed from the shadow model,

$$
\begin{aligned}
& p\left(\mathbf{e}_{g, k}(\mathbf{x}) \mid \boldsymbol{\theta}_{\mathbf{e}, k}(\mathbf{x}), \prod_{\mathbf{y} \in M_{\mathbf{x}}} s_{k}(\mathbf{y})=2^{\left|M_{\mathbf{x}}\right|}\right) \\
& =\frac{1}{2 \pi \sqrt{\left|a_{k}^{2} \Sigma_{\mathbf{e}, k}(\mathbf{x})\right|}} \exp \left\{-\frac{1}{2 a_{k}^{2}}\left[\mathbf{e}_{g, k}(\mathbf{x})-a_{k} \boldsymbol{\mu}_{\mathbf{e}, k}(\mathbf{x})\right]^{T} \Sigma_{\mathbf{e}, k}^{-1}(\mathbf{x})\left[\mathbf{e}_{g, k}(\mathbf{x})-a_{k} \boldsymbol{\mu}_{\mathbf{e}, k}(\mathbf{x})\right]\right\}
\end{aligned}
$$

When neighborhood area $M_{\mathbf{x}}$ belongs to the foreground, we assume that the points within $M_{\mathbf{x}}$ are independent and identically distributed (i. i. d.). From (15), we know

$$
\begin{aligned}
& p\left(\mathbf{e}_{g, k}(\mathbf{x}) \mid \boldsymbol{\theta}_{\mathbf{e}, k}(\mathbf{x}), \prod_{\mathbf{y} \in M_{\mathbf{x}}} s_{k}(\mathbf{y})=3^{\left|M_{\mathbf{x}}\right|}\right) \\
& =p\left(\mathbf{e}_{g, k}(\mathbf{x}) \mid \prod_{\mathbf{y} \in M_{\mathbf{x}}} s_{k}(\mathbf{y})=3^{\left|M_{\mathbf{x}}\right|}\right) \\
& =p\left(e_{g, k}^{h}(\mathbf{x}) \mid \prod_{\mathbf{y} \in M_{\mathbf{x}}} s_{k}(\mathbf{y})=3^{\left|M_{\mathbf{x}}\right|}\right) p\left(e_{g, k}^{v}(\mathbf{x}) \mid \prod_{\mathbf{y} \in M_{\mathbf{x}}} s_{k}(\mathbf{y})=3^{\left|M_{\mathbf{x}}\right|}\right) \\
& =\left(\frac{1}{y_{\max }}-\frac{\left|e_{g, k}^{h}(\mathbf{x})\right|}{y_{\max }^{2}}\right)\left(\frac{1}{y_{\max }}-\frac{\left|e_{g, k}^{v}(\mathbf{x})\right|}{y_{\max }^{2}}\right)
\end{aligned}
$$

# 4.2. Prior Model 

The prior model $p\left(s_{k}\right)$ represents the prior probability of the segmentation field. We model the density by a Markov random field [22]. That is, if $N_{\mathbf{x}}$ is the neighborhood of a pixel $\mathbf{x}$, then the conditional distribution of a single label at $\mathbf{x}$ completely depends on the labels within its neighborhood $N_{\mathbf{x}}$. According to the Hammersley-Clifford theorem, the density is given by a Gibbs distribution with the following form [23]:

$$
p\left(s_{k}\right) \propto \exp \left\{-\sum_{c \in C} V_{k}\left(s_{k}(\mathbf{x}) \mid \mathbf{x} \in c\right)\right\}
$$

where $C$ is the set of all cliques $c$, and $V_{k}$ is the clique potential function at time $k$. A clique is a set of pixels that are neighbors of each other. The clique potential depends only on the pixels within clique $c$. Only one-pixel and two-pixel cliques are used in our work.

The single-pixel clique potentials can be defined as

$$
V_{1, k}\left(s_{k}(\mathbf{x})\right)=\eta_{s_{k}(\mathbf{x}), k}
$$

They reflect our prior knowledge of the probabilities of different region types. The lower the value of $\eta_{s_{k}(\mathbf{x}), k}$, the more likely that a point $\mathbf{x}$ is labeled as $s_{k}(\mathbf{x})$ at time $k$.

Spatial connectivity can be imposed by the following two-pixel clique potential,

$$
V_{2}\left(s_{k}(\mathbf{x}), s_{k}(\mathbf{y})\right)=\frac{1}{\|\mathbf{x}-\mathbf{y}\|^{2}}\left(1-\delta\left(s_{k}(\mathbf{x})-s_{k}(\mathbf{y})\right)\right)
$$

where $\delta(\cdot)$ is the Kronecker delta function, and $\|\cdot\|$ denotes the Euclidian distance. Thus two neighboring pixels are more likely to belong to the same class than to different classes. The constraint becomes stronger with decrease of the distance between the neighboring sites.

Combining the above models, the Bayesian MAP estimate is obtained by minimizing the objective function

$$
F_{k}\left(s_{k}\right)=\sum_{\mathbf{x} \in \mathbf{X}} U_{1, k}\left(\mathbf{x}, s_{k}(\mathbf{x})\right)+\sum_{\mathbf{x} \in \mathbf{X}} U_{2, k}\left(\mathbf{x}, s_{k}(\mathbf{x})\right)+\lambda_{1} \sum_{\mathbf{x} \in \mathbf{X}} V_{1, k}\left(s_{k}(\mathbf{x})\right)+\lambda_{2} \sum_{[\mathbf{x}, \mathbf{y}] \in C} V_{2}\left(s_{k}(\mathbf{x}), s_{k}(\mathbf{y})\right)
$$

where $U_{1, k}\left(\mathbf{x}, s_{k}(\mathbf{x})\right)=-\ln p\left(g_{k}(\mathbf{x}) \mid \boldsymbol{\theta}_{b, k}(\mathbf{x}), s_{k}(\mathbf{x})\right)$, and $U_{2, k}\left(\mathbf{x}, s_{k}(\mathbf{x})\right)=-\ln p\left(\mathbf{e}_{g, k}(\mathbf{x}) \mid \boldsymbol{\theta}_{\mathbf{x}, k}(\mathbf{x}), s_{k}(\mathbf{x})\right) \cdot p\left(g_{k}(\mathbf{x}) \mid \boldsymbol{\theta}_{b, k}(\mathbf{x}), s_{k}(\mathbf{x})\right)$ and $p\left(\mathbf{e}_{g, k}(\mathbf{x}) \mid \boldsymbol{\theta}_{\mathbf{x}, k}(\mathbf{x}), s_{k}(\mathbf{x})\right)$ are the likelihood models for intensity and edge respectively. The parameters $\eta_{1, k}, \eta_{2, k}, \eta_{3, k}, \lambda_{1}$ and $\lambda_{2}$ should be determined carefully to control the influence of each term in (23).

# 5. Implementation 

### 5.1. Parameter Determination

After the segmentation of the $k$ th frame, denote the set of points labeled as $s(s=1,2,3)$ by $\mathbf{X}_{s, k}$. The single-pixel clique potential can be reestimated as

$$
\eta_{i, k}^{*}=-\frac{\left|\mathbf{X}_{i, k}\right|}{\sum_{s}\left|\mathbf{X}_{s, k}\right|}, i=1,2,3
$$

With the learning rate $\alpha, \eta_{i, k+1}$ can be updated in an adaptive way.

$$
\eta_{i, k+1}=(1-\alpha) \eta_{i, k}+\alpha \eta_{i, k}^{*}
$$

The parameters of the linear transformation in the shadow model can be reestimated from the set $\mathbf{X}_{2, k}$ by the least squares method,

$$
\begin{aligned}
& a_{k}^{*}=\frac{\sum_{\mathbf{x} \in \mathbf{X}_{2, k}} g_{k}(\mathbf{x}) \sum_{\mathbf{x} \in \mathbf{X}_{2, k}} \mu_{b, k}(\mathbf{x})-\left|\mathbf{X}_{2, k}\right| \sum_{\mathbf{x} \in \mathbf{X}_{2, k}} g_{k}(\mathbf{x}) \mu_{b, k}(\mathbf{x})}{\left(\sum_{\mathbf{x} \in \mathbf{X}_{2, k}} \mu_{b, k}(\mathbf{x})\right)^{2}-\left|\mathbf{X}_{2, k}\right| \sum_{\mathbf{x} \in \mathbf{X}_{2, k}} \mu_{b, k}^{2}(\mathbf{x})} \\
& c_{k}^{*}=\frac{\sum_{\mathbf{x} \in \mathbf{X}_{2, k}} g_{k}(\mathbf{x})-a_{k}^{*} \sum_{\mathbf{x} \in \mathbf{X}_{2, k}} \mu_{b, k}(\mathbf{x})}{\left|\mathbf{X}_{2, k}\right|}
\end{aligned}
$$

The shadow model is then updated adaptively.

$$
\begin{aligned}
& a_{k+1}=\left(1+\eta_{2, k}^{*} \alpha\right) a_{k}-\eta_{2, k}^{*} \alpha a_{k}^{*} \\
& c_{k+1}=\left(1+\eta_{2, k}^{*} \alpha\right) c_{k}-\eta_{2, k}^{*} \alpha c_{k}^{*}
\end{aligned}
$$

In (27) the effective learning rate $-\eta_{2, k}^{*} \alpha$ changes with the ratio of shadowed points in the scene. This helps to make a robust updating process, especially for the frames where there are only few shadowed points.

Parameters $\alpha, \lambda_{1}$, and $\lambda_{2}$ are manually determined to reflect the importance of previous knowledge, one-pixel clique potential, and two-pixel clique potential respectively.

# 5.2. Optimization 

Obviously, there is no simple method of performing the optimization in (23), furthermore, the objective function does not have a unique minimum since it is nonconvex in terms of $s_{k}(\mathbf{x})$. To arrive at a sub-optimal estimate, we use a local technique known as highest confidence first (HCF). HCF is a noniterative and deterministic algorithm that guarantees to reach a local optimum after a finite number of steps [24]. Its feature is the introduction of a special uncommitted label 0 in the labeling strategy, so that the original label set is augmented by this label into $\{0,1,2,3\}$.

Given the labels of the points within the neighborhood $N_{\mathbf{x}}$, the conditional posterior potential for a point $\mathbf{x}$ at time $k$ is defined as

$$
\begin{aligned}
& f_{k}\left(\mathbf{x}, s_{k}(\mathbf{x})\right)=U_{1, k}\left(\mathbf{x}, s_{k}(\mathbf{x})\right)+U_{2, k}\left(\mathbf{x}, s_{k}(\mathbf{x})\right)+\lambda_{1} V_{1, k}\left(s_{k}(\mathbf{x})\right)+\lambda_{2} \sum_{\mathbf{y} \in N_{\mathbf{x}}} V_{2}^{*}\left(s_{k}(\mathbf{x}), s_{k}(\mathbf{y})\right) \\
& V_{2}^{*}\left(s_{k}(\mathbf{x}), s_{k}(\mathbf{y})\right)=\left\{\begin{array}{l}
0, \text { if } s_{k}(\mathbf{y})=0 \\
V_{2}\left(s_{k}(\mathbf{x}), s_{k}(\mathbf{y})\right), \text { otherwize. }
\end{array}\right.
\end{aligned}
$$

Figure 3. The fifth-order neighborhood system.

In our work, the fifth-order neighborhood system is used (see Figure 3). Based on the conditional posterior potential, we can define the stability measure of site $\mathbf{x}$.

$$
S_{k}\left(\mathbf{x}, s_{k}(\mathbf{x})\right)=\left\{\begin{array}{l}
-\min _{s \neq 0, s_{\min , k}(\mathbf{x})}\left[f_{k}(\mathbf{x}, s)-f_{k}\left(\mathbf{x}, s_{\min , k}(\mathbf{x})\right)\right], \text { if } s_{k}(\mathbf{x})=0 \\
\min _{s \neq 0, s_{k}(\mathbf{x})}\left[f_{k}(\mathbf{x}, s)-f_{k}\left(\mathbf{x}, s_{k}(\mathbf{x})\right)\right], \text { otherwise. }
\end{array}\right.
$$

where $s_{\min , k}(\mathbf{x})=\arg \min _{s \neq 0} f_{k}(\mathbf{x}, s)$.

The stability measure [25], i.e. $S_{k}\left(\mathbf{x}, s_{k}(\mathbf{x})\right)$, determines the order in which the points are to be labeled. All points are initially labeled as uncommitted (or zero), and a committed (or non-zero) label can only be changed to another non-zero value. The label assignment procedure terminates when the objective function (23) can no longer be decreased.

# 6. Results and Discussion 

The algorithm has been tested on monocular indoor sequences. To reduce the computation afford, we assume $\sigma_{b, k}^{2}(\mathbf{x})=\sigma_{b, k}^{2}$ for every point at the step of Bayesian foreground detection in Section 4. Figure 4 shows the segmentation results for the "aerobic" sequence. Figure 4a shows four frames of the sequence. Using the same estimated background, the segmentation results of both simple background subtraction and our method are shown in Figure 4b-4d. Comparing with the results of simple background subtraction, the accuracy of object detection is greatly improved by the proposed approach. The moving cast shadows (the gray regions in Figure 4c) are exactly removed from the foreground. The flickering background pixels that will be detected as foreground by simple background subtraction method are correctly classified by our algorithm. The camouflage at the neck makes the head almost separated from the body in figure 4 b , while this effect is successfully overcome in figure 4 d .

Figure 4. (a) Frames of the "aerobic" sequence. (b) The segmentation results of simple background subtraction. (c) The segmentation results of the proposed algorithm. (d) The foreground detected by the proposed algorithm.

The comparison of the proposed method with two recent adaptive background subtraction techniques, background variation [1] and mixture of Gaussians [4], has also been investigated. The performance of the proposed technique, background variation (BV), and mixture of Gaussians (MG) is tested on a "laboratory" sequence. All the three methods are initialized using the first 50 frames of the sequence. A smoothing operation is applied on the detection results of BV and MG before comparison. The segmentation results are shown in Figure 5. Figure 5a shows four frames of the sequence. The manually segmented "ground truth" foreground images are shown in Figure 5b. The segmentation results

of BV, MG, and our technique are shown in Figure 5c-5e, respectively. Besides visual comparison, the results are also evaluated quantitatively in terms of the false negative number and rate (the number and portion of foreground pixels that are missed) and the false positive number and rate (the number and portion of non-foreground pixels that are marked as foreground) by comparing to the "ground truth" images. The errors for the four scenes in Figure 5a are summarized in Table 1. It can be seen that moving shadows cast on the floor, wall, and table result in an increase of falsely detected foreground pixels in Figure 5c and 5d. Large shadow attachments may cause failures in further analysis such as object recognition and tracking. Here cast shadows follow the movement of the person, so that they could not be learned by the background model as background changes. Moreover, there are a number of lights from the ceiling in the scene. Without an explicit shadow model, it is difficult to know which Gaussians in the mixture are produced by shadows.

Figure 5. (a) Frames of the "laboratory" sequence. (b) The "ground truth" foreground. (c) The segmentation results of BV. (d) The segmentation results of MG. (e) The segmentation results of the proposed algorithm.

Table 1. Quantitative evaluation of different methods.

Figure 6 shows the segmentation results by the proposed method for another "laboratory" sequence. The open cabinet in the third and fourth images is classified as background after a period of background updating. However, it can be seen from Figure 5e and 6b that erroneous segmentation sometimes takes place at boundary areas. The spatial constraint from the MRF formulation is relatively weak at object boundaries, so that errors are more likely to happen at these areas when the foreground has similar color as the background or the pixel intensity under shadow is far from its mean.

Figure 6. (a) Frames of another "laboratory" sequence. (b) The segmentation results of the proposed algorithm.

During the segmentation process given in Section 4, the density of the image intensity at site $\mathbf{x}$ is modeled as

$$
p\left(g_{k}(\mathbf{x}) \mid \boldsymbol{\theta}_{b, k}(\mathbf{x})\right)=\sum_{s_{k}(\mathbf{x})=1}^{3} p\left(s_{k}(\mathbf{x})\right) p\left(g_{k}(\mathbf{x}) \mid \boldsymbol{\theta}_{b, k}(\mathbf{x}), s_{k}(\mathbf{x})\right)
$$

Comparing this to the right side of (7a) in the case of $K=3$, it can be found that uniform distribution is assumed for the foreground in (30), while Gaussian distribution is assumed in (7a). Since in the foreground there is no particular reason

to prefer one value over any other, (30) could be thought as the improvement of (7a). However, the mixture of different kinds of distributions is much harder to estimate than the mixture of only Gaussians. Since foreground regions usually have large variances, from (9) we can see that such a difference will not make the backgrounding process in Section 3 to produce biased results.

# 7. Conclusion 

In this paper we have presented an adaptive approach for foreground segmentation and shadow detection in monocular indoor image sequences. Graphical probabilistic models are employed in our approach. In our work, three sources of information are employed in object and shadow detection. The first is edge information, the difference images help locate changes in the scene. The second is spatial information, objects and shadows usually form continuous regions, and the third is temporal information, the models are updated from previous segmentation results.

Experimental results show that our method successfully deals with nonstationary background, camouflage and shadows in grayscale video sequences. Moreover, the algorithm can be easily implemented for color image sequences. How to further decrease the computation load of the optimization process and automatically determine all the parameters in our model is the topic of our future study.

# Acknowledgements 

The authors acknowledge Dr. Andrea Prati, Dr. James Davis, and Dr. Li-Yuan Li et al. for providing the test data on the website.

## Biographies

Yang Wang was born in China, 1976. He received his B.Eng. degree in Electronic Engineering and M.Sc. degree in Biomedical Engineering from Shanghai Jiao Tong University in 1998 and 2001 respectively. He obtained his Ph.D. degree in Computer Science from National University of Singapore in 2004. He was awarded the National Excellence Scholarship of China and the President's Graduate Fellowship of Singapore. Dr. Wang has published about ten international journal and conference papers. His current research interests are in the area of Machine Intelligence and Computer Vision.

Tele Tan is Senior Lecturer in the Division of Engineering, Science and Computing at the Curtin University of Technology, Western Australia, where he is affiliated to the Department of Computing, Department of Electrical and Computer Engineering and the Applied Physics Department. His research interests are in human motion analysis, security and surveillance, multi-modal system considerations and technology commercialization. Dr Tan helped contribute to the original commercialization plan of a biometrics start-up company, XiD Technologies (http://www.xidtech.com) in late 2002. The biometrics software developed by the company was nominated for the 2004 World Technology Awards (software category) that was held in conjunction with the World Technology Summit 2004. He was made Technical Advisor to Miltrade Technologies in 2003 and was appointed International Reader with the Australian Research Council (ARC) in mid 2004.

Kia-Fock Loe is an Associate Professor in the Department of Computer Science at the National University of Singapore. He obtained his Ph.D degree from the University of Tokyo. His current research interests are pattern recognition, computer vision, neural network, machine learning, and uncertainty reasoning.

Jian-Kang Wu currently is principal Scientist, department manager of new initiatives, Institute for Infocomm Research (I2R), Singapore, which formally known as Kent Ridge Digital Labs (KRDL), and Institute of Systems Science (ISS), National University of Singapore. Dr. Wu received Bsc from the University of Science and Technology of China, and PhD from Tokyo University. Prior to join ISS in 1992, he was a full professor in the University of Science and Technology of China, received 9 distinguished awards from the Ministry of Education and Ministry of Science of China and the Chinese Academy of Science. He also worked in universities in US, UK, Germany, France and Japan. Dr. Wu pioneered several researches in the area of visual information processing. This includes adaptive image coding in later 70s, object-oriented GIS in early 80s, face recognition system in 1992, content-based multimedia indexing and retrieval in early 90s, NeuroInformatics and PhysioInformatics recently. He initiated and led 3 large intentional collaboration projects in 90s. He is an author of 18 patents, 60+ journal publications and 5 books.