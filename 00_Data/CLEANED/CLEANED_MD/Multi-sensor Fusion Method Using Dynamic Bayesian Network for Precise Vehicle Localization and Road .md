# Multi-Sensor Fusion Method using Dynamic Bayesian Network for Precise Vehicle Localization and Road Matching 

Cherif Smaili ${ }^{1}$, Maan E. El Najjar ${ }^{2}$, François Charpillet ${ }^{1}$<br>${ }^{1}$ LORIA-INRIA Lorraine - MAIA Team Campus Scientifique BP 23954506 Vandoeuvre-lèsNancy, France<br>${ }^{2}$ LAGIS-CNRS UMR 8146 Polytech'Lille, Avenue Paul Langevin 59655 Villeneuve d'Ascq Cedex France<br>smailic@loria.fr


#### Abstract

This paper presents a multi-sensor fusion strategy for a novel road-matching method designed to support real-time navigational features within advanced driving-assistance systems. Managing multihypotheses is a useful strategy for the road-matching problem. The multi-sensor fusion and multi-modal estimation are realized using Dynamical Bayesian Network. Experimental results, using data from Antilock Braking System (ABS) sensors, a differential Global Positioning System (GPS) receiver and an accurate digital roadmap, illustrate the performances of this approach, especially in ambiguous situations.


## 1. Introduction

Autonomous Vehicles currently hold the attention of many researchers because they can provide solutions in many applications related to Intelligent Transportation system. One example of such a system is the transport of passengers in urban environments using a CyCab [1]. For navigational needs the vehicle first needs to know its position on the road network, and then to retrieve attributes from the appropriate databases. Examples of attributes are maximum authorized speed, the width of the road, the presence of landmarks for precise localization, etc. Unfortunately, the precise localization on a digital map cannot be guaranteed because there will often be errors in the estimation of position arising from sensor imprecision and because the map represents a deformed view of the real world: roads are represented by points nodes and shaping points- that describe the geometry of the center line.

Vehicle localization on a map has two meanings in the literature in this domain. In many works, [2], [3], [4] and [5] it refers to the projection of the absolute position estimate onto a segment of the road network stored in the database. In this case, the vehicle is localized when the curvilinear abscissa along the segment are known from
the starting node. These "arc-matching" methods therefore introduce geometric distortions, since the model of the world is a set of segments, usually with a 10 meters absolute error and a 1 meter relative error. Alternatively, vehicle localization can refer to absolute localization in the map reference frame. In this case, the localization of the vehicle does not need a projection onto the segments representing the road in the database. Absolute localization can be very useful for the following reasons. In several kinds of databases, including those of the National French Institute of Geography (IGN), attributes, instead of being attached to the arcs representing the roads, can be stored in the database as point objects with an absolute position.

The approach presented in this paper is an absolute localization method. The global positions provided by a GPS receiver are projected onto the map frame. The goal is to select the most likely segment(s) from a set of segments close to the estimation of the vehicle position. Nowadays, since the geometry of roadmaps is more and more detailed, the number of segments representing roads is increasing. The road managing module is an important stage in the vehicle localization process because the robustness of the localization depends mainly on this stage. In order to focus in this point, an accurate map Géoroute V2 provided by the IGN was used in this work.

In order to develop our approach, it is important to estimate continuously the pose - position and heading of the vehicle in the frame of the map using GPS, because of its affordability and convenience. However, GPS suffers from satellite outages occurring in urban environments, under bridges, tunnels or in forests. GPS can thus be seen as an intermittently-available positioning system that needs to be backed up by a dead-reckoning system [7]. In this work, a low-cost odometric method based on the use of encoders attached to the rear wheels is proposed. A dead-reckoned estimated pose is obtained by integrating the elementary rotations of the wheels starting from a known pose. The multisensor fusion of GPS and odometry is performed by a Switching Kalman Filter (SKF). This kind of formalism is also useful in

quantifying the imprecision associated with each estimated pose.

The outline is as follows. In section 2, the architecture of the road-matching method is described. In section 3, we present a short introduction of Bayesian networks. Section 4 describes the network model for road-matching. Next section, we evaluate the potential of our approach by presenting a real data results. Finally, concluding remarks are given in section 6 .

## 2. Architecture of the road-matching strategy

The road-matching method described in this section relies on Bayesian networks. The proposed approach is described in Figure 1. Firstly, the algorithm combines the ABS measurements with a GPS position, if it is available. Then, using this estimate, segments around the estimation are selected in a radius of 30 meters by using a Geographical Information System (GIS)-2D. Using these segments, map observations are built and merged with other data sensors using a method based on Dynamic Bayesian Network.
![img-0.jpeg](img-0.jpeg)

Figure 1: Synoptic of the road-matching method

### 2.1 Localization and heading estimation by combining odometry and GPS

Consider a car-like vehicle with front-wheel drive. The mobile frame is chosen with its origin M attached to the center of the rear axle. The x -axis is aligned with the longitudinal axis of the car (see Figure 2).

The vehicle's position is represented by the $\left(x_{k}, y_{k}\right)$ Cartesian coordinates of M in a world frame. The heading angle is denoted $\theta_{h}$. If the road is perfectly planar and horizontal, and if the motion is locally circular, the motion model can be expressed as [8]:

$$
X_{s}=\left\{\begin{array}{l}
x_{k+1}=x_{k}+\delta_{s} \cdot \cos \left(\theta_{k}+\delta_{\theta} / 2\right) \\
y_{k+1}=y_{k}+\delta_{s} \cdot \sin \left(\theta_{k}+\delta_{\theta} / 2\right) \\
\theta_{k+1}=\theta_{k}+\delta_{\theta}
\end{array}\right.
$$

Where $\delta_{s}$ is the length of the circular arc followed by M and $\delta_{\theta}$ is the elementary rotation of the mobile frame. These values are computed using the ABS measurements of the rear wheels. Let denote $X_{k}$ the state vector containing the pose.
![img-1.jpeg](img-1.jpeg)

Figure 2: The mobile frame attached to the car

### 2.2 Cartographical and GPS observation equation

A correction of the odometric estimation is performed by the GPS information. When the GPS satellites signal is blocked by buildings or tunnels, the odometric estimation is used to select the segments all around the estimation from the cartographical database. The cartographical observations can be obtained by projections onto the segments. If the orthogonal projection onto line does not make part of the segment, the closer extremity is used (see Figure 3). When several segments are candidates, the cartographical observation function is a non-linear multimodal observation. Considering a Gaussian distribution of noise to represent the uncertainty zone all around a segment, so the multi-modal observation is a multiGaussian observation one.
![img-2.jpeg](img-2.jpeg)

Figure 3: Most likely segments extracted from the database

The observation equation of the segment seg $_{i}$ can be written:

$$
Y_{\text {carto }}^{\text {cap }}=\left[\begin{array}{l}
x_{\text {carto }} \\
y_{\text {carto }} \\
z a p_{\text {carto }}
\end{array}\right]=\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right]\left(\begin{array}{l}
x \\
y \\
\theta
\end{array}\right)+\beta_{\text {carto }}
$$

Where $\left(x_{\text {carto }}, y_{\text {carto }}\right)$ is the orthogonal projection onto each segments and $\operatorname{cap}_{\text {carto }}$ is the segment heading.

To represent the error of the cartographical observation in the SKF formalism, we choose a Gaussian distribution of the uncertainty zone all around the segment. So this error can be represented with an ellipsoid which encloses the road (we choose to use an ellipsoid because it is just the available model). This ellipsoid has its semi-major axis in the length of the segment and its semi-minor axis equals to the width of the road [8] (see Figure 4).
![img-3.jpeg](img-3.jpeg)

Figure 4: Ellipsoidal of probability construction representing zone around a segment for horizontal segment i.e. parallel with the east axes

The third axis of the ellipsoid represents the uncertainty of the estimation of the segment. This uncertainty is related to the relative error of the cartographical database. The covariance matrix of the cartographical observation error can be written:

$$
Q_{k}^{\text {carto }}=\left(\begin{array}{ccc}
\sigma_{x, k}^{2} & Q_{x y, k} & 0 \\
Q_{x y, k} & \sigma_{y, k}^{2} & 0 \\
0 & 0 & \sigma_{\theta, k}^{2}
\end{array}\right)
$$

The GPS position measurement provides the GPS observation $\left(x_{g p s}, y_{g p s}\right)$. The GPS measurement error can be provided also and in real time using the Standard National Marine Electronics Association (NMEA) sentence "GPGST" given by the Trimble AgGPS132 receiver which has been used in the experiments. Therefore, the GPS noise is not stationary. The non stationary of the GPS measurements noise affect the observation model. With each measurement provided, the

GPS provide it with his noise in the sequence GPGST in the standard NMEA.
$Q_{k}^{\text {gas }}$ : covariance matrix of the GPS error where

$$
Q_{k}^{\text {gas }}=\left(\begin{array}{cc}
\sigma_{x, g p s}^{2} & Q_{x y, g p s} \\
Q_{x y, g p s} & \sigma_{y, g p s}^{2}
\end{array}\right)_{k}
$$

The observation equation can be written:

$$
Y_{1}=\left[\begin{array}{l}
x_{g p s} \\
y_{g p s}
\end{array}\right]=\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0
\end{array}\right] \cdot\left(\begin{array}{l}
x \\
y \\
\theta
\end{array}\right)+\beta_{g p s}
$$

## 3. Bayesian Networks

A Bayesian Network (BN) is a graph with probabilities for representing random variables and their dependencies. It efficiently encodes the joint probability distribution (JPD) of a set of variables. Its nodes represent random variables and its arcs represent dependencies between the random variables encoded by conditional probabilities. Afterwards, a BN is written as a directed acyclic graph $\mathrm{G}=(\mathrm{E}, \mathrm{W})$ with $\mathrm{W}=\left\{X_{1}, \ldots, X_{N}\right\}$ as the set of nodes, and $\left(X_{i}, X_{j}\right) \in \mathrm{E}$, the set of edges, if $X_{i} \in \operatorname{Pa}\left(X_{i}\right)$. Normally an edge is drawn from $X_{i}$ to $X_{j}$ if $X_{i}$ has a direct influence on $X_{j}$. For more detailed in Bayesian Networks see [9] [10].

The joint probability distribution of random variables $\mathrm{S}=\left\{X_{1}, \ldots, X_{N}\right\}$ in a BN is calculated by the multiplication of the local conditional probabilities of all the nodes. The (JPD) of $S$ is given as follows:

$$
P\left(X_{1}, \ldots, X_{N}\right)=\prod_{i} p\left(X_{i} / P a\left(X_{i}\right)\right)
$$

A Dynamic Bayesian network (DBN) is a BN used to model a temporal stochastic process. It can be created by specifying network (structure and parameters) for two consecutive "time slices", and then "unrolling" it into a static network of the required size.

DBNs generalize two well-known signal modelling tools: Kalman filters for continuous state linear dynamic system (LDS) and Hidden Markov Models (HMMs) for classification of discrete state sequences. It has been shown that estimation in (LDSs) and inference in (HMMs) are special cases of inference in DBNs [11]. The focus of this paper is on a subclass of DBNs models called Switching Linear Systems or Switching Kalman Filter.

### 3.1 Switching Kalman Filter

Switching Kalman filter is a subclass of DBN and this type of network is useful for modeling piece-wise linear behavior (one way of approximating non-linear models), or multiple type or "mode" of behavior [11].

Consider a dynamical system whose parameters evolve in time according to some known model. This system can

be described using the following set of state-space equations:

$$
\begin{aligned}
X_{t} & =A_{t} X_{t-1}+v_{t} \\
Y_{t} & =C_{t} X_{t}+w_{t}
\end{aligned}
$$

This model is called Linear Dynamical System (LDS), where $\mathrm{X}_{\mathrm{t}} \in \Re^{\mathrm{N}}$ is the hidden state variable at time $\mathrm{t}, \mathrm{Y}_{\mathrm{t}} \in$ $\Re^{\mathrm{M}}$ is the observation at time $t$, and $v_{t} \sim N\left(0, Q_{t}\right)$ and $\mathrm{w}_{\mathrm{t}} \sim \mathrm{N}\left(0, \mathrm{R}_{\mathrm{t}}\right)$ are independent Gaussian noise. The parameters of model: $\mathrm{A}_{\mathrm{t}}, \mathrm{C}_{\mathrm{t}}, \mathrm{Q}_{\mathrm{t}}$ and $\mathrm{R}_{\mathrm{t}}$ are assumed to be time-invariant. Unfortunately, most systems are not linear and are subject to non-Gaussian noise. One approach to this problem and one we take in this paper, is to switch among $K$ different linear models or take some linear combination of them (see Figure 5)[12].
![img-4.jpeg](img-4.jpeg)

Figure 5: A switching Kalman filter
The variables $S_{t}$ are discrete and the variables $X_{t}$ and $Y_{t}$ are continuous. Other observations can be introduced in this model. The conditional probability distributions for this model are as follows:
$P\left(X_{t}=x_{t} / X_{t-1}=x_{t-1}, S_{t}=i\right)=N\left(A x_{t-1}+\mu_{i}, Q i\right)$
$P\left(Y_{t}=y / X_{t}=x_{t}\right)=N\left(C x_{t}+\mu^{\mathrm{T}}, R\right)$
$P\left(S_{t}=j / S_{t-1}=i\right)=B(i, j)$
An important issue in BN is the computation of posterior probabilities of variables given observations. Several researchers have been developed to compute the exact and/or the approximate inference algorithms for different distributions. The most commonly used to compute the exact inference algorithm for discrete Bayesian Networks is known as the JLO ${ }^{1}$ algorithm [11]. The JLO algorithm is a recursive message passing algorithm that works on the junction tree of the BN. Namely, we need to find the posterior: $P\left(X_{t}, S_{t} / Y_{t}\right)$ in the case of switching Kalman filter.

## 4. Switching Kalman filter for road-matching

Road-matching involves applying a first filter which selects all the segments close to the estimated position of the vehicle. The goal is then to select the most likely

[^0]segment(s) from this subset. Nowadays, since the geometry of roadmaps is more and more detailed, the number of segments representing roads is increasing. In the other hand, the map has an absolute error ( 10 meters) and relative error ( 1 meter). The road classification module is an important stage in the vehicle localization process because the robustness of the localization depends mainly on this stage. In order to take into account the error of several sensors or database used in this application, we introduce a concept which can manage multi-hypothesis in the formalism of BN.

### 4.1 BN model

For each selected segment Carto, we represent it by a Gaussian: $\operatorname{Carto}_{i} \sim N\left(\mu_{i}, \sum_{i}\right)$. Where $\mu_{i}$ is the pose vector: $\left(x_{i}, y_{i}\right)$ is the projection of the estimated position on this segment and $\theta_{i}$ is the heading of the segment.

The proposed BN model for road-matching is illustrated in Figure 6. In this model we used two hidden variables. The discrete variable $S_{k}$ represents the segments of which the vehicle can be. The second is continuous variable; $X_{k}\left(x_{i}, y_{i}, \theta_{i}\right)$ represents the estimation of a vehicle for each segment candidate.

The graph represented in Figure 6 allows us to represent causal links between the variables. The variable $X_{k}$ is updated by observations $\operatorname{Carto}_{k}$ and/or $G P S_{k}$ (if GPS is masked we use only the cartographical observations). This variable is multi-modal because it has been updated by the set of candidates segments $\left(\right.$ Carto $\left._{k}{ }^{\text {sog }}\right)$. The variable $S_{k}$ is update by cartographical observation $\left(\right.$ Carto $\left._{k}\right)$ and the estimation is given by the hidden variable $X_{k}$.
![img-5.jpeg](img-5.jpeg)

Figure 6: Switching Kalman filter for a mapmatching

For each candidate segment one can build a cartographical observation given by projection of odometric estimation onto the segments. The cartographical observations and/or GPS observation are used to update variables $X_{k}$ and $S_{k}$. A result of Bayesian inference is a probability of each candidate segment. The synoptic of this algorithm is given by Figure 7.

Let us use a specific case study to illustrate the method. In Figure 8, the vehicle is traveling on the road represented by the segments 1 and 2. Estimation errors and digital map errors oblige the selection of the segment


[^0]:    ${ }^{1}$ F.V. Jensen, S.L. Lauritzen et K.G. Olesen

3 in addition to the segment 2 to be treated also. So, two cartographical observations were generated in giving the same chance to each segment candidate. Consequently two estimations were generated also at the step $\mathrm{t}=\mathrm{k}-1$.
![img-6.jpeg](img-6.jpeg)

Figure 7: Synoptic of road-matching using a BN
At the instant k , three segments were selected all around the predicted pose. These segments were used to generate three observations. Then, using SKF, three estimations were provided. We plot only the most probable in green circle on the Figure 8.
![img-7.jpeg](img-7.jpeg)

Figure 8: Illustrative example of multihypotheses

## 5. Experimental results

A test trajectory has been carried out at Compiègne in France with an experimental vehicle. The used GPS is a differential Trimble AgGPS132 receiver. For odometry, the ABS sensors is of the rear wheels of the vehicle are used.

The test trajectory is presented in Figure 9. In this experience, the GPS measurement was available in the beginning of the test trajectory. Then, the GPS still not
used for 1.5 Km . One can remark that in spite of the long GPS mask, the vehicle location is matched correctly. As matter of fact, the final estimated positions stay close to the GPS points. In Figure 9, we only presented the most probable SKF estimation of the pose.
![img-8.jpeg](img-8.jpeg)

Figure 9: pose estimation with SKF using odometry and cartographical observation (GPS was masked)

In Figure 10, the estimation is plotted with a red $\times$. When the GPS measurement is not available, the method provides estimation for each segment candidate and the estimation of the most probable segment only is plotted. Then the GPS measurement it becomes available but the GPS position is then closer the segment which describe the other side of the road. In this case, the situation is an ambiguous parallel road situation. The method detects the ambiguity of this situation and selects all probable segments in this parallel road situation. The SKF manage all hypotheses until the elimination of the ambiguity. One can remark that, in spite the ambiguity, the road on which the vehicle is running in reality presents the highest probability. With these results, the proposed approach can manipulate and take into account the GPS error also.
![img-9.jpeg](img-9.jpeg)

Figure 10: Multi-hypothesis managed with SKF to treat parallel road situation

In Figure 11, GPS was not available after the intersection. One can see that the method manage two hypotheses for seven steps then wrong hypothesis was eliminated. We can remark that, the good segment always presents the most important probability computed by the SKF inference.
![img-10.jpeg](img-10.jpeg)

Figure 11: Multi-hypothesis managed with SKF to treat junction road situation

## 6. Conclusion

This article has presented a road-matching method based on a multi-sensor fusion approach. The main contributions of this work are the formalization of a roadmatching method in the Switching Kalman filtering context and an experimental validation with real data.

An interesting characteristic of this approach is that it is flexible and modular in the sense that it can easily integrate other sensors. This feature is interesting because adding other sensors is a way to increase the robustness of the road-matching.

In this approach, the use of the digital map as an observation of the state space representation has been introduced. This observation is used in the Switching Kalman filter in the same way that the GPS data. It turned out in the experiments that the GPS measurements are not necessary available all the time, since the merging of odometry and roadmap data can provide a good estimation of the position over a substantial period. The strategy presented in this paper doesn't keep only the most likely segment. When approaching an intersection, several roads can be good candidates for this reason we manage several hypotheses until the situation becomes unambiguous.

## Acknowledgments

The authors wish to acknowledge the HEUDIASYC laboratory in the person of Philippe Bonnifait for his contribution.
