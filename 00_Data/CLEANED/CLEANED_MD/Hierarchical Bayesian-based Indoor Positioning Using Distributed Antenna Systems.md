# Hierarchical Bayesian-based Indoor Positioning Using Distributed Antenna Systems 

Leonardo Terças*, Carlos Morais de Lima*, Jani Saloranta* and Matti Latva-aho*<br>*Centre for Wireless Communications (CWC), University of Oulu, Finland<br>E-mail: [leonardo.tercas, carlos.lima, jani.saloranta, matti.latva-aho] @oulu.fi


#### Abstract

This work proposes and evaluates hierarchical Bayesian-based localization methods to estimate the position of a target node in indoor deployment scenarios. The measurements are acquired through a distributed antenna system which is connected to a common master anchor node. Each antenna head is affected by different channels parameters, what makes the estimation more difficult. The proposed method combines received signal strength and time of flight measurements to estimate the target location. In our investigations, we also consider a one-level hierarchical Bayesian network model, which introduces conditional interdependencies to the model parameters, resulting in less susceptibility to local variations. The Markov Chain Monte Carlo sampling method is used to approximate the posterior distribution of the two-dimensional target's location coordinates. The root mean square error is used to evaluate the performance of the proposed solution in indoor scenarios. Our results show that by combining hybrid measurements or increasing conditions between the parameters by a hierarchical approach, the proposed mechanisms outperform the classic Bayesian model when estimating the target node using even fewer measurements.


Index Terms-Bayesian inference, Hierarchical graphical models, Indoor Localization, MCMC, DAG.

## I. INTRODUCTION

Among the 5G New Radio (NR) study cases, the massive Machine Type Communications (mMTC) imposes stringent requirements in terms of accuracy and reliability of the positioning information [1], [2]. For instance, health care technologies, transportation systems and object tracking are important applications that benefit from location information across industry verticals in Internet of Things (IoT) systems [3]. Recently, the research on new techniques and algorithms suitable for Indoor Positioning Systems (IPS) has increased [4], for the reason that traditional satellite Global Positioning System (GPS) localization methods and standard cell multilateration are limited or sometimes impractical in indoor deployment scenarios.

In an IPS, the position of a target node can be estimated by using distinct measurement types, for example, the Received Signal Strength (RSS) [5]. Furthermore, development and performance evaluation are easy due to the fact that these measurements can be simulated quickly and using a basic computational algorithm. However, RSS-based measurements are affected by radio channel degrading effects - such as fading, shadowing and signal reflections - that decreases the target position accuracy. Considering distributed deployment

Academy of Finland through the grants No. 318927 (project 6Genesis Flagship) and No. 24303208.
scenarios, each anchor node may be subject to different channels conditions (parameters), which makes the estimation more difficult.

When estimating the position of the target node, it is possible to minimize these degrading effects and increase the accuracy of the estimate by acquiring more measurements, although the stringent requirements of the mMTC scenarios regarding low latency and high reliability may not be attained if the processing time linger too long. Alternatively, the accuracy of the target position estimate can also be improved by combining distinct measurements types. In this approach, e.g., RSS samples are acquired and processed together with the following metrics: Time of Arrival (TOA), Time Difference of Arrive (TDOA) and Direction of Arrival (DOA).

Typically, optimization-based algorithms implementing Nonlinear Least Squares (NLS) and Maximum Likelihood (ML) estimators [6] are used to estimate the target position. In their recent work, authors studied Bayesian inference using probabilistic graphical models as a promising alternative to estimate the location of a target node [7], [8] - this approach estimates the position coordinates by sampling its joint posterior distribution. In indoor deployment scenarios, Bayesian graphical models can use distinct metrics, such as RSS, TDOA, TOA, and DOA; or combinations, thereof through the so-called hybrid solutions to find the position of a target [9].

In this context, a hierarchical approach allows to represent complex models, e.g., incorporating many constituent parameters that are allowed to be associated together by probability rules. Basically, modeling specifications - considering uncertainties and prior knowledge - are implemented and coherently linked by a series of conditions, i.e., the hierarchical Bayesian method organizes the parameters into groups of different levels of observation that are assumed to be a sample of the underlying population distribution. The variance of this population determines the range of the sampling distribution around a common mean, that results in a posterior distribution less sensitive [10].

By applying the aforementioned Bayesian models in indoor deployment scenarios, our work proposes and evaluates Bayesian-based localization methods using RSS and TOA measurements. We also consider distributed antennas systems (DAS) where each anchor (antenna head) may experience different channel conditions.

The remainder of this paper is organized as follows. Section II introduces the Bayesian networks through the probabilis-

tic graphical models and the Markov Chain Monte Carlo (MCMC) sampling algorithms. Section III presents the localization’s models and the evaluation scenarios. The numerical results, in terms of the root mean square error (RMSE), are presented in Section IV. Finally, Section V concludes this work and discusses final remarks.

## II. Graphical Models and Bayesian Inference

A probabilistic graphical model is a multivariate statistical model that allows representing a joint distribution by relating a set of random variables through conditional interdependencies between their descriptive parameters. Using the probabilistic graphical model, Bayesian networks can infer the likelihood of the related events based on the available prior knowledge. We model the source localization problem by using Directed Acyclic Graphs (DAGs) that are a probabilistic graphical model that have no cycles. DAG can be represented by $\mathcal{G}=(V ; E)$, where $V$ are the vertices and $E$ the edges. In this model, the vertices correspond to Random Variables (RVs) while the edges represent the underlying relationships between them [11].

The RVs in a Bayesian network are assumed to be conditionally independent. In other words, a vertex is only affected by its own parents (distribution to which it belongs), while being independent of its non-descendants given its parents [12]. This property implies a factorization of the joint probability density function $p(V)$ of the RVs $X_{v}$, $v \in V$. From [13], a Bayesian network model with respect to $\mathcal{G}$ is given as

$$
p(V)=\prod_{v \in V} p(v \mid \mathrm{pa}(v))
$$

where $\mathrm{pa}(v)$ represents the parents of $v$. The conditional distribution of a RV $v$ in the graph is given by

$$
\begin{aligned}
p(v \mid V / v) & \propto p(v, V / v) \\
& \propto \text { terms in } p(V) \text { containing } v \\
& =p(v \mid \mathrm{pa}(v)) \prod_{w \in \operatorname{child}(v)} p(w \mid \mathrm{pa}(w))
\end{aligned}
$$

where child $(v)$ yields all the children of $v$.
To carry out approximate inference of a Bayesian statistical model, it is necessary to use a sampling method as the Markov Chain Monte Carlo (MCMC) approach. The MCMC uses the Bayes' Theorem and the prior knowledge about the network to estimate the posterior distribution. From [14], the posterior distribution in a Bayesian statistical model can be estimated as follows,

$$
p(H \mid D)=\frac{p(D \mid H) p(H)}{p(D)}
$$

where $H$ is the hypothesis and $D$ is the observed data, $p(H)$ is the prior distribution and represents the initial hypothesis, $p(D \mid H)$ is the likelihood function and $p(D)$ represents the probability of all possible values that the parameters can assume.

## A. Hierarchical Bayesian model

When information is available on different observational units, the data parameters can be organized into groups to obtain a hierarchical structure [10]. For instance, each measurement corresponds to an observational unit that travels by a different path and is affected by a distinct coefficient value, we can organize these parameters to be samples of the same distribution, i.e., with the same mean and variance. This Bayesian model is called hierarchical and is more accurate than the non-hierarchical models, because the posterior distribution became less sensitive to local variations, resulting in less model variance than the classic method. A one-level hierarchy Bayesian network model can be represented as follows [15],

$$
p(\theta, \phi \mid D) \propto \prod_{i=1}^{n} p\left(D_{i} \mid \theta_{i}\right) p\left(\theta_{i} \mid \phi\right) p(\phi)
$$

where $H=(\theta, \phi)$ is the hypothesis of the system and $D$ the data. Considering an observation $y_{i}$ and a parameter $\theta_{i}$ governing the data generation process for $y_{i}$. The distribution of the observations is given by,

$$
\begin{aligned}
& y_{i} \sim \mathcal{N}\left(\theta_{i}, \sigma_{i}^{2}\right) \\
& \theta_{i} \sim \mathcal{N}\left(\mu, \tau^{2}\right), \quad i=1, \ldots, I
\end{aligned}
$$

relating to (4), $D=\left(y_{i}, \theta_{i}\right)$ and $\phi=(\mu, \tau)$. In this case, the parameters $\theta_{1}, \theta_{2}, \ldots, \theta_{i}$ are generated from a common population, with distribution given by a hyperparameter $\phi$. Therefore, the posterior distribution of this hierarchical Bayesian model is given by,

$$
p(\theta, \phi \mid D)=\frac{p(D \mid \theta, \phi) p(\theta \mid \phi) p(\phi)}{p(D)}
$$

## B. Markov Chain Monte Carlo sampling method

To estimate the posterior distribution of the target position, we build (non) hierarchical models and use the Bayes' Theorem through the MCMC sampling approach. The latter generates a sequence of random samples from a probability distribution by first making a random proposal for new parameter values and then accepting or rejecting the proposal [16].

The No-U-Turn Sampler (NUTS) algorithm is based on the Metropolis-Hastings method and finds good estimates adaptively, i.e., without a random walk (stochastic process). This NUTS avoids re-exploring local spaces and ensures a much shorter simulation time [17]. To initialize the NUTS sampler and find the posterior distribution of the position of interest, we first make suitable assumptions for the prior distribution of $p(H)$ in (3) and $p\left(\theta_{i} \mid \phi\right) p(\phi)$ in (4); then the NUTS algorithm explores the sample space and generates the posterior distribution based on the acquired data and the prior distributions. It is worth mentioning that the proper choice of the prior distribution and the input data affects the time of convergence of the posterior distributions.

## III. SYSTEM MODEL AND HIERARCHICAL LOCALIZATION MECHANISM

## A. Evaluation scenario

An indoor deployment scenario that represents, e.g. a warehouse and has a square shape with side length of 100 meters (Fig.1) is used to assess the proposed mechanism. Distributed antenna heads are positioned in each corner of the deployment area and are connected to a central processing unit (CPU) that is responsible to estimates the position of a target node after acquiring a minimum amount of measurements from the antennas heads with known positions. The target dwells in a random (unknown) position within the deployment area.

Each receiver (anchor) collects the corresponding Received Signal Strength (RSS) measurements independently and are affected by a log-distance shadowed path loss model with respect to the distance between the target and the receiver. Fig. 2(a) shows the distance $d$ that represents a circle centered at the receiver, where the border of the circle represents all possible target locations. The multilateration concept consists in estimates the target position considering more than one receiver, the intersection area generated by the distance of each antenna heads corresponds to the possible target location. In Fig. 2(b), the red area represents the density estimation of the localization. In scenarios with degrading effects, it is possible to determine the unknown position of the target node by using the measurements gathered by at least 3 anchor receivers [5].

The radio link RSS function is given by

$$
p_{r_{i}}=p_{t}-\alpha_{i} \ln \left(d_{i}\right)+\varphi \text { in } \mathrm{dBm}
$$

where $p_{r_{i}}$ is the target signal strength received by the $i$ th receiver, $p_{t}$ is the transmitted power, $\alpha_{i}$ is the path loss exponent with respect to the $i$ th receiver, $d_{i}$ is the Euclidean distance between the target and the $i$ th receiver, and $\varphi$ is the shadowing value with zero-mean normal distribution in the logarithmic scale.
![img-0.jpeg](img-0.jpeg)

Fig. 1. Indoor deployment scenario - squares represent the antenna heads, while a red cross identifies the target node.
![img-1.jpeg](img-1.jpeg)

Fig. 2. (a) Distance representation considering one antenna head, where the target node is represented by the red cross and $d$ is the distance between the target node and the antenna head. (b) Distance representation considering three antenna heads, where the red area represents the density estimation of the localization.

We also study hybrid scenarios where two arbitrary anchors are assumed to collect RSS and TOA measurements. In these scenarios, assuming DAS, the central unit is responsible for making the necessary synchronization between the anchors and information fusion. The TOA function is given by

$$
t_{i}=d_{i} / c
$$

where $c$ is the speed of light and $t_{i}$ is the time of flight assuming that the source emits a signal at time 0 and the sensor receives it at time $t_{i}$.

## B. Probabilistic graphical models for source localization

Herein, we consider three Bayesian networks to carry out our investigations, in each DAG model the parameters inside the lozenge $-x_{i}$ and $y_{i}$ - are assumed to be known a priori by the central unit, and represent the receivers' coordinates, further the parameters inside the circles correspond to random variables whose distribution is based on our prior knowledge. Below we present the DAG model and respective metrics for each case.

1) Non-hierarchical RSS-based Bayesian network: In this model the interdependence between the random variables is represented by the DAG model shown in Fig.3.
![img-2.jpeg](img-2.jpeg)

Fig. 3. Graphical model of the non-hierarchical RSS-based source localization.

The RSS-based Bayesian network is described by

$$
\begin{array}{rll}
p_{t} & \sim & \operatorname{Normal}(0,100) \\
\alpha_{i} & \sim & \operatorname{Normal}(0,100) \\
\sigma_{r s s_{i}}^{2} & \sim & \operatorname{InverseGamma}(1,0.1) \\
\mu_{r s s_{i}} & \sim & p_{t}-\alpha_{i} \log \left(d_{i}\right) \\
X & \sim & \operatorname{Uniform}(0, L) \\
Y & \sim & \operatorname{Uniform}(0, B) \\
d_{i} & \sim & \sqrt{\left(X-x_{i}\right)^{2}+\left(Y-y_{i}\right)^{2}}
\end{array}
$$

where $\sim$ indicates that a RV follows a specific distribution, $p_{t}$ is the transmit power at the transmitter, $\alpha_{i}$ is the path loss exponent, $\sigma_{r s s_{i}}$ is the standard deviation of the measurements collected by the $i$ th receiver point, $d_{i}$ is the distance between the target and the $i$ th receiver and $(X, Y)$ is a two-dimensional RV representing the target location coordinates.
2) Hybrid Bayesian network: The hybrid model combines RSS- and TOA-based Bayesian networks, the interdependence between the random variables using time of flight measurements, is represented by the DAG in Fig. 4.

Similar to the RSS-based model, the assumptions of the respective TOA-based Bayesian network is given as

$$
\begin{array}{rll}
\mu_{t o a_{i}} & \sim & d_{i} / c \\
\sigma_{t o a_{i}}^{2} & \sim & \operatorname{InverseGamma}(1,0.1) / c \\
X & \sim & \operatorname{Uniform}(0, L) \\
Y & \sim & \operatorname{Uniform}(0, B) \\
d_{i} & \sim & \sqrt{\left(X-x_{i}\right)^{2}+\left(Y-y_{i}\right)^{2}}
\end{array}
$$

The hybrid model combines the DAGs presented in Figs. 3 and 4.
3) Hierarchical RSS-based Bayesian network: We create a one-level hierarchy to the transmit power and the path loss exponents, so that each of these two data parameters has a distribution with mean and variance given by $\left(a_{i}, \sigma_{a_{i}}^{2}\right)$ and $\left(b_{i}, \sigma_{b_{i}}^{2}\right)$, respectively. It is worth mentioning that the hierarchical structure includes conditional interdependencies in the chosen parameters resulting in less model variance. Fig. 5 shows the DAG of this network, representing the interdependence between the random variables.
![img-3.jpeg](img-3.jpeg)

Fig. 4. Graphical model of the non-hierarchical TOA-based source localization.
![img-4.jpeg](img-4.jpeg)

Fig. 5. Graphical model of the hierarchical RSS-based source localization.

The hierarchical Bayesian network is described as

$$
\begin{array}{rll}
p_{t} & \sim & \operatorname{Normal}\left(a, \sigma_{a}^{2}\right) \\
a & \sim & \operatorname{Normal}(0,10) \\
\sigma_{a}^{2} & \sim & \operatorname{InverseGamma}(1,0.1) \\
\alpha_{i} & \sim & \operatorname{Normal}\left(b, \sigma_{b_{i}}^{2}\right) \\
b_{i} & \sim & \operatorname{Normal}(0,10) \\
\sigma_{b_{i}}^{2} & \sim & \operatorname{InverseGamma}(1,0.1) \\
\sigma_{h_{i}}^{2} & \sim & \operatorname{InverseGamma}(1,0.1) \\
\mu_{h_{i}} & \sim & p_{t}-\alpha_{i} \log \left(d_{i}\right) \\
X & \sim & \operatorname{Uniform}(0, L) \\
Y & \sim & \operatorname{Uniform}(0, B) \\
d_{i} & \sim & \sqrt{\left(X-x_{i}\right)^{2}+\left(Y-y_{i}\right)^{2}}
\end{array}
$$

where $a$ and $b_{i}$ are assumed to follow a normal distribution with mean 0 and with variance 10 and represent the mean of $p_{t}$ and $\alpha_{i}$ respectively, $\sigma_{a}^{2}$ and $\sigma_{b_{i}}^{2}$ represent the variance of $p_{t}$ and $\alpha_{i}$ and are assumed to have an inverse gamma distribution with shape parameter 1 and a scale parameter 0.1 .

## IV. PERFORMANCE EVALUATION

The indoor deployment scenarios introduced in § III were implement in Python, more specifically, our estimator was built using the PyMC3 package [18] and we carry out an extensive simulation campaign to evaluate the proposed Bayesianbased source localization mechanisms. In our simulations, the measurements are generated following the radio propagation channel described in (6) and (7), while the path loss coefficient is different for each anchor varying from 2 to 3.5. This assumption makes the estimation of the posterior distribution using the NUTS algorithm more difficult, because there are more parameters that need to be sampled and less relation between the anchors. The anchors collect the measurements and send them to the central unit which employs the NUTS algorithm to sample the posterior distribution of the parameters, and determine the Probability Density Function (PDF) of the twodimensional coordinate of the target position $(X, Y)$. In every

simulation, the target node is arbitrarily located at $(70,30)$ and is unknown by the algorithm.

To evaluate the performance of the proposed algorithms, we employ the error distance metric which is given by

$e=\frac{1}{N}\sum_{k=0}^{N}\sqrt{\left(X_{k}-X_{r}\right)^{2}+\left(Y_{k}-Y_{r}\right)^{2}},$ (8)

where $N$ is the number of simulation runs, $\left(X_{k},Y_{k}\right)$ is a two-dimensional RV representing the estimated target coordinates in the $k$th simulation run and $\left(X_{r},Y_{r}\right)$ is a two-dimensional RV representing the real target coordinates.

### V-A Non-hierarchical analysis of RSS and hybrid models

In Fig. 6, each curve point is averaged over 100 simulation runs and in each such iteration the localization algorithm is fed with 50 new measurements. In this simulation set, we compare the distance error between distinct models by varying the standard deviation of the error associated to the RSS measurements, the anchors independently acquire RSS or TOA measurements and the NUTS algorithm is used to estimate the position. It is worth mentioning that in this scenario the error associated to the TOA measurements are constant. The hybrid approach outperforms the RSS-based one though the wide gap narrows between the curves in Fig. 6. This occurs because the hybrid approach has more information acquired by TOA measurements and this compensates for the values of the standard deviation of the RSS measurements error when estimating the location of the target node. In RSS-based scenarios, we can observe that the error distance between the points are almost constant, the kernel density estimate (KDE) of the source location estimate is sparse, as show Fig.7(a)

![img-5.jpeg](img-5.jpeg)

Fig. 6. Error distance between the estimated and real target point for increasing error standard deviation of measurements when using RSS and hybrid (RSS plus TOA) models.

![img-6.jpeg](img-6.jpeg)

Fig. 7. The kernel density estimates of the source location estimate using (a) RSS-based method and (b) hybrid-based method. In each figure, the real location of the target is denoted by red circle and the maximum of the probability density by the black circle.

and represents that the estimated position can be located at any place of the scenario. Considering the maximum of the KDE in each iteration, the estimated target position is located always in the center of the square. In the case of hybrid-based scenarios, the acquired TOA measurements compensate for the values of standard deviation of the RSS measurements error, what generates a less disperse probability density of the source location and high precision in the estimation target position is obtained, as shows Fig.7(b).

### V-B RSS-based method with non- and hierarchical models

Similarly, Fig.8 compares the hierarchical approach fed with different numbers of RSS measurements, against the RSS-based models in terms of the distance error as function of standard deviation of the error associated to the measurements. In this figure, each curve point is averaged over 100

![img-7.jpeg](img-7.jpeg)

Fig. 8. Error distance comparison between the non- and hierarchical models for increasing standard deviation.

![img-8.jpeg](img-8.jpeg)

Fig. 9. Error distance comparison between hierarchical models for increasing standard deviation fed with different numbers of measurements.

Simulation runs and in each such iteration the localization algorithm is fed with new RSS measurements, the anchors independently acquire RSS measurements and the NUTS algorithm is used to estimate the target position. We observe that the hierarchical models achieve better performance than non-hierarchical models; this occurs because the hierarchical model has more information about the network than the non-hierarchical model, i.e., adding one-level hierarchy the knowledge about the prior distribution increase and the range of the sampling distribution has a common mean and variance, thus, the posterior distribution varies in a smaller local space, resulting in less variation of the model to estimate the target position.

We observe the number of measurement samples acquired by the receivers affects the accuracy of the algorithm, because comparing the hierarchical-based approach with 25 and 50 samples in Fig. 9, the latter shows a more accurate estimate of the target position, i.e., lower values of error distance around 1 meter when the error standard deviation of RSS measurements is about 4 meters. This occurs because NUTS algorithm has more data to sample the posterior distribution, concluding that hierarchical-based approach performs better by acquiring more measurements. Furthermore, the gap in performance becomes higher when the error associated with the measurements increases.

## V. CONCLUSION

In this work, three Bayesian-based localization methods were evaluated. The simulated scenario acquires distinct metrics by a distributed antenna system that is connected to a central unit responsible for fusing and use the data. Each anchor in the system experiences distinct radio channel impairments (fading coefficient) that make the estimation more difficult. The target position is estimated by sampling the corresponding posterior distribution using the MCMC NUTS algorithm. Results show that by combining RSS and TOA measurements in a hybrid Bayesian-based method, the target node position can be estimated with small error distance, different to non-hybrid Bayesian-based method where the estimation is inaccurate. In addition, our results show that RSS-hierarchical models can estimate the target node with fewer measurements and performance better – about 2 meters of accuracy – if the number of acquired samples is increased.

## VI. ACKNOWLEDGMENT

The research leading to these results has received funding from the Academy of Finland through the grants No. 318927 (project 6Genesis Flagship) and No. 24303208.
