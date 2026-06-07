![img-0.jpeg](img-0.jpeg)

# End-to-End Probabilistic Ego-Vehicle Localization Framework 

Abderrahim Kasmi, Johann Laconte, Romuald Aufrère, Dieumet Denis, Roland Chapuis

## To cite this version:

Abderrahim Kasmi, Johann Laconte, Romuald Aufrère, Dieumet Denis, Roland Chapuis. End-to-End Probabilistic Ego-Vehicle Localization Framework. IEEE Transactions on Intelligent Vehicles, 2020, pp.1-1. 10.1109/TIV.2020.3017256 . hal-03049396

## HAL Id: hal-03049396 <br> https://uca.hal.science/hal-03049396v1

Submitted on 9 Dec 2020

HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers.

L'archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d'enseignement et de recherche français ou étrangers, des laboratoires publics ou privés.

# End-to-End Probabilistic Ego-Vehicle Localization Framework 

Abderrahim KASMI ${ }^{1,2}$, Johann LACONTE ${ }^{2}$, Romuald AUFRERE ${ }^{2}$, Dieumet DENIS ${ }^{1}$, Roland CHAPUIS ${ }^{2}$


#### Abstract

Locating the vehicle in its road is a critical part of any autonomous vehicle system and has been subject to different research topics. In most works presented in the literature, ego-localization is split into three parts: Road level-localization consisting in the road on which the vehicle travels, Lane level localization which is the lane on which the vehicle travels, and Ego lane level localization being the lateral position of the vehicle in the ego-lane. For each part, several researches have been conducted. However, the relationship between the different parts has not been taken into consideration. Through this work, an end-to-end ego-localization framework is introduced with two main novelties. The first one is the proposition of a complete solution that tackles every part of the ego-localization. The second one lies in the information-driven approach used. Indeed, we use prior about the road structure from a digital map in order to reduce the space complexity for the recognition process. Besides, several fusion framework techniques based on Bayesian Network and Hidden Markov Model are elaborated leading to an ego-localization method that is, to a large extent, robust to erroneous sensor data. The robustness of the proposed method is proven on different datasets in varying scenarios.


Index Terms-Autonomous vehicle, localization, lane marking, map matching, road prior, fusion framework.

## 1 INTRODUCTION

OVER the past decades, the automotive industry has been growing strongly. The demand for the driver and pedestrians security coupled with the technological advances are the main factors behind this exponential growth. In that regard, Advanced Driver Assistance Systems (ADAS) have spread out. The main mission of these systems is to ensure that driver safety is constantly guaranteed. For this purpose, multiple applications have been deployed, such as lane departure warning, lane keeping assist, pedestrian detection, collision avoidance, or lane change assist system. To achieve this mission, the faultless knowledge of the localization of the ego-vehicle with regards to the surrounding environment is necessary.
The ego-localization of a vehicle is a mandatory component for a safe autonomous driving. Direct applications range from the decision-making system [1] regarding the decisions to make in order to keep lane or to change lane, to navigation: including path planning and vehicle control [2]. Ultimately, the lane/road understanding demands in terms of precision and false alarm rate [3] vary from one application to another. Therefore, the ego-localization solution must suit perfectly the localization requirement for each application. The ego-localization task has been widely tackled over the years. The current literature is teeming with solutions that address this issue in a variety of manners. However, one interpretation of ego-localization consists of the knowledge of three key components:

[^0]I Road level localization: the road on which the vehicle travels.
II Lane level localization: the position of the host lane within the road (the lane on which the vehicle travels).
III Ego-lane level localization: the position of the vehicle in the lane in terms of lateral and longitudinal position.

For the road level localization, digital maps (Google, OpenStreetMap (OSM) or Waze) are used to perform this task, GPS receivers are used to retrieve the geographic (latitude, longitude) coordinates, and map-matching procedure is performed in order to match the position of the ego-vehicle with the correct road ('link'). However, the accuracy of the localization obtained is in the order of meters. Indeed, according to the Federal Aviation Administration (FAA) GPS Performance Analysis Report [4], the accuracy of a standard GPS device is within $3 m$ with a $95 \%$ confidence, which can not be sufficient for most ADAS that require a more precise localization.
For some applications like lane-keeping, knowing the road on which the vehicle is traveling is not sufficient. These systems must be informed about the position of the host lane in the road to provide the adequate maneuver instruction and maintain the vehicle safety.
Further, autonomous vehicle applications need a more accurate localization, which can be translated by the knowledge of the lateral and longitudinal position of the vehicle in the ego-lane. For instance, overtaking maneuvers need a faultless knowledge of the lateral position of the ego-vehicle with respect to the ego-lane marking in order to decide whether the vehicle should overtake the obstacle or not.
The task of vehicle localization is still challenging for an autonomous vehicle, a complete ego-vehicle localization must perform all the three key components described above. Thus, in this work, an end-to-end solution for egolocalization from Road level localization to Ego-lane level


[^0]:    *This work has been sponsored by Sherpa Engineering and ANRT (Conventions Industrielles de Formation par la Recherche).
    1 Sherpa Engineering, R\&D Department, 333 Avenue Georges Clemenceau, 92000 Nanterre, France. [a.kasmi, d.denis] @sherpa-eng.com
    2 Université Clermont Auvergne, CNRS, SIGMA Clermont, Institut Pascal, F-63000 Clermont-Ferrand, France. FirstName.Lastname@uca.fr

localization is presented.

## 2 Related Work

Due to the vastity of this topic, this section will discuss the main vehicle localization techniques relevant to our presented work. To do so, the current literature is divided into three distinct topics: Localization on a map, Localization on a road and Localization on a lane.

### 2.1 Localization on a Map

For Autonomous Vehicles, map-matching (MM) algorithms are a critical piece on any localization system. In essence, MM algorithms integrate the geographical position from a GPS receiver with the spatial road network to identify the correct road on which the vehicle is traveling. In [5] a comprehensive literature survey of common MM methods is presented. The basic method combines an inertial measurement unit (IMU) with a classic GNSS receiver (e.g., GPS, Galileo) into a Kalman Filter to choose the correct road [6] [7]. In the same manner, authors in [8] propose a probabilistic MM that takes into account both the spatial (geographical coordinates) and temporal information (speed and time) to determine the likelihood road on which the ego-vehicle is traveling. However, in more complicated cases, such as urban scenarios, multi-path GPS signals lead to a lack of accuracy. In this case, the use of topological and geographical information enhances the proposed algorithm. Towards this end, many studies proposed a Hidden Markov Model (HMM) to take into account the measurement noise [9]. The authors in [10] introduce a HMM to robustify the proposed MM algorithm. The HMM incorporates the topological and the geographical road network information in the transition state to ensure the temporal connectivity between links. A more recent approach presented in [11] utilizes the HMM for the MM task. In essence, the two approaches are similar, except for the HMM modeling. Indeed, in [11] the transition from one 'link' or segment to another must obey some rules, these rules include the dynamics of the vehicles and the legal and logical connectivity of the road map. In a more specific way, the latest developments use the OpenStreetMap (OSM) database to perform the MM. In our previous work [12], a multi-criteria map-matching algorithm based on multiple probabilistic criteria has been introduced. Nevertheless, the road map topology has not been properly operated in the MM process, which consists of one of the contributions of this paper.

### 2.2 Localization on a road

Knowing the position of the ego-lane is still a challenging task for any localization system and subject-matter of research. Indeed, lane-level localization has been widely discussed in recent literature. According to [13], ego-lane localization can be performed in two different manners: model-driven and deep leaning approaches.

### 2.2.1 Model-driven approaches

The current literature abounds with ego-lane recognition techniques based on model-driven approaches. In these approaches, road level features are extracted from images via feature extraction, mainly two features (edge and color) are used. For the first feature, filters are used to extract lanes edges, then the resulted outputs are fed into Hough Transforms [14] or Ransac methods [15] to detect lanes in the road. For the color features, it exploits the primary color or the direction of lane components (arrow, zebra marking). Once these features extracted, they are fed into a high-level fusion framework. As an example, in [16] ego-lane recognition is achieved from multiple-lanes detection. Adjacent lanes are first hypothesized assuming the same curvature and lane width in the road, then tested using a video-based system. This approach shows interesting results. However the occlusion of lanes marking by obstacle vehicles can not be explained and will jeopardize the output of the egolane. More high level features systems fuse visual features from the road scene: surrounding vehicles [17], lanes marking [18] [19], road clues such as arrows marking [20], lane marking colors [21], lane marking and adjacent vehicles [22]. These visual cues are fed into a fusion framework: Bayesian filter (BF) [17], Bayesian Network (BN) [20] [18] [21], Hidden Markov Model (HMM) [19] or combination of BN and HMM [22]. A worth mentioning work is the one presented in [23] in which a lane-level accurate map is used in order to match the correct localization of the ego-vehicle. The map contains center lines of every lane of the road in addition to the lanes marking. Therefore to know the lane on which the vehicle is travailing a map matching procedure is presented. The presented method deals with the ambiguities encountered in choosing the right 'link'. Nevertheless, this method is tributary to the accurate map. In contrast, we present a method for lane level localization that relies only on a camera and a coarse map (OSM).

### 2.2.2 Deep learning approaches

Convolutional Neural Networks (CNNs) have also been widely adopted for lane level localization. These techniques do not take any prior about the surrounding environment, which makes these unrelated to the type of road-scenario (e.g., highway, urban). However, a learning phase is needed to set the weights of the used network.
In [24] local context of the scene is used to consider occlusion to determine the end point of the local lane segment, egolane is deduced once lane segments are extracted. Another research [25] uses a combination of CNN and RNN to detect lane boundaries. Similar to this approach a CNN is trained in an end-to-end way to estimate the ego-lane [26]. In [13] an end-to-end ego lane estimation is presented using a deep learning network SegNet. For all the mentioned methods before, no road prior is exploited. However, a learning stage is needed in all cases, which may require a large database to perform it.

### 2.3 Localization within a lane

In order to guarantee the ego-lane level localization, several data fusion methods have been investigated. The first one

uses a GPS receiver with a digital map to locate the egovehicle in the lane. The lack of accuracy provided by a classic GPS that can be caused by poor satellite signals, high degree dilution of precision, or multi-path in urban scenes, is first compensated with proprioceptive sensors, such as Inertial Measurement Unit (IMU). These methods are well known as Dead Reckoning [27]. Nevertheless, the accuracy provided by this kind of method is not sufficient for autonomous navigation, where centimetric accuracy is needed. Furthermore, dead reckoning methods suffer from integration errors that tend unbounded in time.
Leafing through the literature, it appears that most researchers use lane marking detection from a camera to provide an accurate ego-lane level localization. There are two main advantages of using the camera: currently, this sensor is the cheapest and most versatile modality for automotive applications and it provides dense information of the environment. Common approaches are based on a twostep process [3]. First, a road marking feature detection [28], then a fitting procedure [29] is used. This fitting procedure can be done with a polynomial fitting model based on the road geometry design [30] or non-parametric model [31]. The above-mentioned approaches suffer from the camera's weaknesses: high luminosity variation and occlusion issues. In an attempt to provide a more robust and more accurate localization, the trend for manufacturers and researchers is to equip the ego-vehicle with multiple sensors such as Velodyne lidars, multiples cameras, IMUs and high defined digital map that contains the precise location of high features such as the lane marking or landmarks [32]. In that way, authors in [33] used two lateral cameras combined with an IMU and a GPS receiver to accurately determine the lateral distance of the ego-vehicle with respect to the lane marking. To do so, a vision-based ego-lane marking detector was used [34] and fused with the IMU sensors through an Extended Kalman Filter (EKF) to locate the ego-vehicle. Furthermore, a sub-decimeter accuracy was achieved by adding lanes marking from a created map. Yet again, an EKF was introduced for the fusion stage between the lane marking extracted from the map and the marking obtained through the vision process. In order to bound the integration errors coming from dead reckoning, authors in [35] present a localization system based on the fusion of multi-sensor and a high definition map. The integrity of the localization is insured by a Student's distribution that replaces the classical Gaussian distribution used in fusion filter like Kalman filters in an Informational Filter (IF). Close to our work, an atypical approach presented in [36] relies on the use of road priors and contextual information for road detection (roadway detection). OSM map is used to create the road backbone depending on the lanes number and the width of the lane. This road shape is then projected on the image taking into account the uncertainties related to the ego-vehicle pose. The result is used as prior to roadway detection. The road shape is then delimited by estimating the vanishing point and the lane marking. Naturally, the mentioned approaches are just a small part of the ego-lane localization techniques, an interesting survey is presented in [3] for more detailed approaches.
To the best of the authors' knowledge, there is no end-toend localization solution proposed that tackles every aspect
of the ego-localization task. Thus, in this paper, we present a complete solution for the overall localization problem.
Unlike existent work, this contribution distinguishes by the information-driven approach. Indeed, we exploit the available data from the OSM map in order to extract prior about the road geometry. This strategy allows us to focalize the region of interest in the recognition procedure and ultimately reduce the computation complexity. In addition, we propose a probabilistic model that will ensure the geometric coherency between lanes marking. Finally, the main contributions can be summarized as follows:

1) An enhanced map matching method based on OSM datasets and a Hidden Markov Model
2) An ego-lane detection based on a prior OSM map and a vision based recursive recognition ego-lane marking in an information-driven fashion.
3) Once the ego lane marking is detected and the lateral distance between the ego-vehicle and the lane marking estimated, we proceed to the ego-lane determination (the postion of the ego-lane in the road) using a combination of a Bayesian Network and a Hidden Markov Model.
We perform the complete localization steps in a sequential fashion. Thereby, the robustness of the proposed approach is highly improved. In addition to that, the split between the different parts of the localization allows the use of any part of the complete solution individually.

## 3 OVERALL LOCALIZATION ALGORITHM

In this work, we present an end-to-end algorithm for ego localization as highlighted on Figure 1. The algorithm is intentionally divided into three modules: Road-level localization (RLL), Ego-lane level localization (ELL) and Lane level localization (LLL). This split allows us to be in phase with the current literature. Moreover, the pipeline of the algorithm allows to have modular algorithms that can be changed in the future without changing the entire algorithm architecture. In the following, we will first introduce our map-matching module based on OSM datasets, then we will use this map as a prior for our ego-lane marking detection in order to locate the vehicle within its lane. Once the egolane level localization is performed, we will proceed to the identification of the ego-lane in the road.

### 3.1 Road-level localization (RLL)

In this section, we present our road-level localization algorithm using OSM datasets. As shown in Figure 2 the proposed module is an upgrade of our work presented in [12]. Indeed, an HMM is added to robustify the proposed Map-Matching. Therefore, the algorithm is divided into two different stages:

- Discrimination stage elimination of incongruent links based on distance, orientation difference between vehicle steering, and links heading. Additionally, a third factor was implemented, it is based on the maximum speed allowed on the road.
- Selection stage in the case where the remaining candidate links are greater than one, we proceed into a selection procedure based on multiple probabilistic criteria to eliminate the ambiguity.

![img-1.jpeg](img-1.jpeg)

Fig. 1: Overall algorithm for complete localization of the ego-vehicle starting from the Road-level localization (RLL): to locate the ego-vehicle on the map Using OSM and GPS datasets, to the Lane-level localization (LLL): to locate the ego-vehicle within its own lane using prior road model from OSM and camera images and the Ego-lane level localization (ELL): to determine the ego-lane position in the road.

![img-2.jpeg](img-2.jpeg)

Fig. 2: Overall algorithm for the RLL using GPS data and OSM in order to extract the correct road and the corresponding number of lanes.

### 3.1.1 Discrimination stage

Before starting with this stage, we must present the OSM data. OSM data are composed of three keys components: Nodes, Ways, and Relations [37]. Nodes are the geometrical elements that represent GPS points. Ways are an ordered list of nodes that represents roads network, every Way has a number of tags, the latter provide information about the characteristics of the Way (number of lanes, limitation speed...). In addition, each Way is composed of a set of segments. In other words, belonging to a segment is equivalent to belonging to an OSM Way. So the map matching task can be reformulated as matching a GPS point with a segment. In the remaining sections, the words segment and Way are switchable.

Thus, the discrimination stage consists of the exclusion of segments which are not compatible with the current vehicle and the road network topology configuration. To do so, we introduced three discrimination criteria [12]:

- The first one is based on the distance between the ego-vehicle position estimated with the GPS data and the segment.
- The second one is based on the angle difference between the ego-vehicle steering angle and the segment heading (which expresses the traffic flow).
- The third one is based on the speed limit. The assumption made is that the ego-vehicle is respecting the limitation of speed to some extent i.e. the ego speed can not be higher than the limitation plus 40 km h<sup>−1</sup>.

Once the discrimination stage completed, if the number of candidates segment is higher than one, we proceed to the selection of the correct Way.

### 3.1.2 Selection of the correct Way

We define the state of ego-vehicle at time step t as

$$
\mathbf{x_t} = (x_w, y_w, \theta_w)^T. \tag{1}
$$

The selection procedure can be formulated as finding the highest conditional probability of belonging to a Way \( W_i \) knowing the pose of the ego-vehicle \( \mathbf{x_t} \) at each time \( t \):

$$
\arg \max p(W_{i_t} \mid \mathbf{x_t})
$$

The main goal of this formulation is to select the correct Way on which the vehicle is traveling. Consequently, a selection criterion must be introduced to determine the correct Way. Based on equation (1) three probabilistic criteria [12] were developed:

- \( C_c \): Criterion based on Euclidean distance.
- \( C_m \): Criterion based on Mahalanobis distance.
- \( C_p \): Criterion based on the probability of belonging to a segment.

Depending on the data available, one of these criteria is calculated for each GPS data and for each candidate Way. Furthermore, to take into account the relation between two consecutive frames, a convenient and effective approach is to use a HMM. Indeed, the change in Ways over time is governed by topology constraints that can be embedded in the transition state of the HMM. Thus we enhance the proposed multi-criteria algorithm with an HMM. The HMM in this work is an upgrade of the proposed HMM by [38] [39]. We fitted the HMM to the way selection problem. However, the big difference lies in the probabilistic reasoning. Indeed, we use criteria that represent probability to model the observation probability, which is not the case in [38] [39], where arbitrary functions have been introduced leading to non-intuitive criteria.

By definition a HMM consists of two stochastic processes, the first one is a Markov Chain to model the change of a state vector over time. This change is governed by a probability that describes the transit probability over time, which is called the transition probability. In the HMM, the states of the chain are not visible but observable, for this reason they are called "hidden". The second process is called the observation space, it produces emission of the observation at each time. Although the elements of the state vector are hidden, there is a relation between the hidden elements of the state and the observations, this relation is referred as an emission probability. Figure 3 describes the proposed HMM for the map-matching task.
So, in order to model the HMM-MM, three components must be defined:
State space the state of the system describes the list of the Ways candidates for each observation $\mathbf{x}_{\mathbf{t}}$. We will use $S_{t}$ to denote the set of candidates Ways at time $t$ $S_{t}=\left\{W_{1}, W_{2}, \ldots, W_{n_{t}}\right\}$ with $n_{t}$ the number of candidates Ways at each time $t, S_{t}$ is a form of categorical distribution, $S_{t} \sim \operatorname{Cat}(\xi)$.
Observation space for each candidate Way composing the state space, an emission probability is made. This emission probability is directly calculated from the multi-criteria algorithm. For each Way candidate the emission probability $\mathbb{P}_{e}\left(W_{i}\right)$ is calculated as follows:

$$
\mathbb{P}_{e}\left(W_{i}\right)=\frac{C_{k}\left(W_{i}\right)}{\sum_{j \in S_{t}} C_{k}\left(W_{j}\right)}
$$

where $C_{k}$ is the probabilistic criterion used with $k \in$ $\{e, p, m\}$.
Transition probability The transition probability reflects the probability of the transition matrix that a state will move from one state to another. In the map matching procedure, the topology of the network is used in order to determine the transition matrix. Indeed, the vehicle can only move on Ways that are physically connected.
![img-3.jpeg](img-3.jpeg)

Fig. 3: Modeling of the Hidden Markov model MapMatching (HMM-MM) algorithm, with $S_{t}$ the state space at time $t, W_{t}$ the Way candidate at time $t$ and $O_{t}$ the observations at time $t$. Note that the number of Way candidates at each time may vary.

TABLE 1: Transition matrix for example shown on Figure 4


We will refer to $\mathbb{P}\left(W_{i}^{t}, W_{j}^{\tau}\right)$ as the transition probability from Way $W_{i}^{t}$ to Way $W_{j}^{\tau}$ given the state space $S_{t}$ and $S_{\tau}$ for time $t$ and $\tau$ :

$$
\mathbb{P}\left(W_{i}^{t}, W_{j}^{\tau}\right)=\frac{w_{i}}{\sum_{j \in S_{t}} w_{j}}
$$

Where $w_{i}$ is a criterion calculated for each Way, this criterion obeys some rules defined as follows:

1) $w_{i}=0$ if the way $W_{i}^{t}$ and $W_{j}^{\tau}$ are not connected;
2) $w_{i}=s_{i j}^{t \tau}$ if the Way $W_{i}^{t}$ and $W_{j}^{\tau}$ are the same;
3) $w_{i}=c_{i j}^{t \tau}$ if the Way $W_{i}^{t}$ and $W_{j}^{\tau}$ are connected.

Figure 4 shows a simplified road network to illustrate the transition matrix probability. These probabilities are shown on Table 1. It can be noticed that in this example the number of Ways is the same for two connected states, which is not always the case. Indeed, the number of Ways may vary from two consecutive frames.
The transition probability $s_{i j}^{t \tau}$ is used whenever the two Ways are the same. Let $P\left(x_{w}, y_{w}\right)$ be the vector describing the Cartesian coordinates of the ego-vehicle in the Universal Transverse Mercator coordinate system frame (UTM), we note $P^{\prime}$ the projection of the point $P$ on the Way and $\psi$ the Way's heading, the Way $W_{i}^{\tau}$ is composed of two nodes $n_{1}, n_{2}$ as represented on Figure 5. The criterion $s_{i j}$ is computed as a Gaussian distance to the middle of the segment $\left[n_{1}, n_{2}\right]$. Indeed, the probability to change the Way will be higher if $P^{\prime}$ is in the middle and will be lower in the limits, thus it is calculated as follows:

$$
s_{i j}=e^{-\frac{1}{2}\left(\frac{t-u_{0}}{\sigma_{0}}\right)^{2}}
$$

With $P^{\prime}=t . n_{1} n_{2}, u_{0}=0$ and we take $\sigma_{0}=0.25$.
If the Way $W_{i}$ and $W_{j}$ are connected then we introduce a criterion based on [39], this criterion depends on the
![img-4.jpeg](img-4.jpeg)

Fig. 4: Example of road network to illustrate the transition probability calculation. In this example the number of Way candidates is the same between two consecutive frames

![img-5.jpeg](img-5.jpeg)

Fig. 5: Example of calculation for transition probability $s_{i j}^{t r}$, the vehicle is illustrated by the box with black triangle, $\psi$ represents the Way heading and $\theta$ the vehicle's heading
difference between the vehicle's heading and the Way's heading :

$$
c_{i j}^{t r}=e^{-\beta|\Delta \theta-\Delta \psi|}
$$

with $\Delta \theta$ being the vehicle's heading change over time, $\Delta \psi$ the Way's heading change between the two Ways $W_{i}$ and $W_{j}$ and $\beta$ a chosen coefficient. Once the Way selected, the number of lanes is extracted from the OSM database.

### 3.2 Ego-lane level localization (ELL)

Once the RLL has been performed, the ELL is initiated. We choose to start the ELL before the LLL for several reasons: the first is that the ego-lane marking is, for the most part, the easiest one to detect. The second one is due to the use of the information driven approach. Indeed, when the ELL is completed we have an estimate of the ego-vehicle's lateral position in its own lane. So, knowing the lane's width and the lanes number allows us to interpolate research zones for other lane marking.
To perform the ELL, the road is modeled in a 2D vehicle's frame $\left(x_{v}, y_{v}\right)$ as a cubic polynomial [40] [41]:

$$
x_{v}=\frac{1}{6} c_{0} y_{v}^{3}+\frac{1}{2} c_{1} y_{v}^{2}+c_{2} y_{v}+c_{3}
$$

The parameters $c_{0}$ is the curvature's derivative of the road, $c_{1}$ the curvature of the road, $c_{2}$ the vehicle's heading with respect to the tangent of the road, $c_{3}$ the lateral shift of the ego-vehicle with regards to the road model. Once the road has been modeled in the vehicle's frame, the next step is to project this model on the image taking into account the intrinsic and extrinsic parameters of the camera. According to [42] the projection of the road model (left and right lines) in the image frame $\left(u_{i}, v_{i}\right)$ is defined as follows:

$$
\begin{gathered}
u_{i}=e_{u}\left(\left(\frac{e_{v} Z_{0}}{\left(v_{i}-e_{v} \alpha\right)}\right)^{2} \frac{c_{0}}{6}-\frac{e_{v} Z_{0}}{2\left(v_{i}-e_{v} \alpha\right)} c_{1}\right. \\
\left.+\frac{v_{i}-e_{v} \alpha}{e_{v} Z_{0}}\left(x_{0} \pm \frac{L_{w}}{2}\right)-x_{0}\right)
\end{gathered}
$$

where $e_{u}=f / d u, e_{v}=f / d v, f$ is the focal distance of the camera, $d u$ and $d v$ are the width and height of a pixel in the image, $Z_{0}$ is the height of the camera, $x_{0}$ the lateral distance
of the ego-vehicle with respect to the ego-lane marking, the $\pm$ sign indicates whether the ego-marking is right $(+)$ or left $(-), \alpha$ is the camera tilt angle and $L_{w}$ is the road width. $i=1, \ldots, n_{R o i}$ with $n_{R o i}$ the number of Region Of Interest (ROI) for each lane marking.
As mentioned in [12], the OSM map does not provide information about the accuracy of its data. However, it is well known that OSM is a collaborative project in which volunteers provide the geospatial data. If we consider that most of the volunteers have a classic GNSS receiver, the accuracy of the OSM is thus metric. That being said, the polynomial representation of the road will be affected by this unknown accuracy. For the parameters $c_{0}$ and $c_{1}$, they represent the shape of the road. Given that we are working mostly with highway roads, their values will not be affected by the inaccurate geospatial accuracy of the OSM. In contrast, the parameter $c_{2}$ is more sensitive to inaccurate accuracy of the OSM, and its value will be affected. Hence, to compensate for the inaccuracy of its value, we will define $X_{v}=\left[x_{0}, c_{2}\right]^{T}$ as the state vector of the road model in the ego-vehicle frame. We associate a covariance matrix to this vector $C_{X_{v}}$. This matrix expresses the allowed dispersion around the average parameters previously defined by the vector $X_{v}$. Concerning the parameters $c_{3}$, the value extracted from equation (6) is not used. Indeed, it express the lateral shift of the vehicle to the road. Hence it is not used in equation (7), as we use $x_{0}$, which is the lateral shift regarding the center of the ego-lane. It assumed that the ego-vehicle travel in the center of the ego-lane thus $x_{0}$ is around 0 .
Using equation ( 7 ), we can express the probabilistic model $\left(X_{v}, C_{X_{v}}\right)$ into the image space. We will note this probabilistic model as $u^{\prime}, C_{u}^{\prime}$, with $u^{\prime}$ being the average values for the pixel in the image and $C_{u}^{\prime}$ its corresponding covariance matrix:

$$
C_{u}=J_{u} C_{X_{v}} J_{u}^{T}
$$

with:

$$
J_{u}=\left[\begin{array}{cc}
\frac{\partial u_{1}}{\partial x_{0}} & \frac{\partial u_{1}}{\partial c_{2}} \\
\cdot & \cdot \\
\cdot & \cdot \\
\frac{\partial u_{n}}{\partial x_{0}} & \frac{\partial u_{n}}{\partial c_{2}}
\end{array}\right], C_{X_{v}}=\left[\begin{array}{cc}
\sigma_{x_{0}}^{2} & 0 \\
0 & \sigma_{c_{2}}^{2}
\end{array}\right]
$$

The resulting projection of the equation (7) is shown in Figure 6. Taking into account the prior about the road geometry allows focalizing the zones of research in a Top-Down process fashion. Indeed, not all the image is used in order to perform the processing task. Consequently, the recognition process is faster, and subject to less noise considering it takes into account only the regions in the image that most likely contains a lane marking.
Once the probabilistic model is defined, we proceed to the recognition phase. This stage is inspired by [42]. For clarity's sake, we will discuss each aspect of this stage as presented in Figure 7.
i Initialization in this stage we define the probabilistic model $\left(u^{\prime}, C_{u}^{\prime}\right)$ as already presented in Figure 6.
ii Selection of the best Region Of Interest (ROI) once the probabilistic model is defined, we proceed to the selection of the most informative ROI in the Image in

![img-6.jpeg](img-6.jpeg)

Fig. 6: Projection of the initial probabilistic model (u', $C_{u}^{\prime}$ ) on the image. The mean values of the lane marking $u^{\prime}$ are presented in Red, Blue illustrates the dispersion around these values. Finally, green boxes are the ROI for each lane marking, in this example the number of ROI is 9 for each lane marking.

![img-7.jpeg](img-7.jpeg)

Fig. 7: All different steps of the Recognition stage for ego-lane marking detection.

a **Top-Down fashion** To do so, we present an informational criterion based on the Shannon entropy [43]. For each ROI, we use an *a priori* selection based on a entropic criterion $H_{sel}$:

$$H_{sel} \triangleq H_0^- - H_0^+$$

$$= p(Dk = 1, Db = 1) \cdot \frac{1}{2} \left[ \log \left| 2\pi e \, C_{X_v}^- \right| - \log \left| 2\pi e \, C_{X_v}^+ \right| \right]$$

with:

$$\begin{cases}
X_0^- & \text{The state vector before simulation of the detection,} \\
C_{X_v}^- & \text{Covariance before simulation of the detection,} \\
X_{v}^+ & \text{The state vector after simulation of the detection,} \\
C_{X_v}^- & \text{Covariance after simulation of the detection.}
\end{cases}$$

For the probabilities, $p(D_b), p(D_k)$, a Bayesian Network (BN) is introduced. The presented nodes are an adaptation of the BN presented in [44]. The scheme of the network is illustrated in Figure 8. The BN is composed of the following nodes:

- $X_{k_+}$ the confidence before the detection is attempted.
- $Z_0$ is the chosen landmark (the white strip) is observable in the ROI.
- $D_k$ a landmark is detected in the focal zone.
- $D_b$ the correct landmark has been detected (which manages landmark ambiguity).

![img-8.jpeg](img-8.jpeg)

Fig. 8: Bayesian Network used for the confidence estimation. Yellow nodes are the input nodes, Purple node is the node we are seeking to estimate.

- $X_{k_+}$ the confidence after the detection is attempted.

This network has two uses, the first one is to calculate the *a priori* probabilities $p(D_k)$ and $p(D_b)$, the second one is to determine the confidence $p(X_{k_+})$ obtained after proceeding to a detection.

iii **Detection** Once the most informative ROI is chosen, we proceed to the detection. The implemented method is based on a row filter as presented in [42]. The idea is to compute the gradient of the image row by row with the aim to find pixels that correspond to the lane marking. Once the patterns have been selected for the complete ROI, a Ransac method is used in order to detect the segment in the ROI. Thus, for each ROI two points $p_1(u_u, v_u)$ and $p_2(u_d, v_d)$ are defined.

iv **Update** for the state vector $x_p = (u_u, u_d)$ we associate a covariance matrix $C_p$ :

$$C_p = \begin{pmatrix} \sigma_{u_u}^2 & 0 \\ 0 & \sigma^2 u_u \end{pmatrix} \tag{11}$$

With $\sigma_{u_u}^2$ being the accuracy of the segment detected. In order to update the probabilistic model, we use a Kalman filter:

$$\begin{cases}
u^+ = u^- + K_u \left[ \hat{x}_p - x_p \right] \\
C_u^+ = C_u^^- - K_u H_u C_p
\end{cases} \tag{12}$$

$K_u$ being the Kalman Gain, $(u^-, C_u^)$ is the model before detection and $(u^+, C_u^)$ is the model after detection.

v **End** after each detection, we compute the corresponding entropic gain $H_{gain}$ :

$$H_{gain} = p\left(X_{k_+}\right) \cdot \frac{1}{2} \left[ \log \left| 2\pi e C_u^+ \right| - \log \left| 2\pi e C_u^ \right| \right] \tag{13}$$

With $C_u^+$ the covariance from the initialization stage. The ego-lane marking has been detected if the following condition is satisfied :

$$H_{gain} \geq \lambda H_{max} \tag{14}$$

with

$$H_{max} = p\left(X_{k_+}\right) \cdot \frac{1}{2} \left[ \log \left| 2\pi e \, C_u^+ \right| - \log \left| 2\pi e \, C_u^ \right| \right]$$

With $\lambda$ a fixed coefficient $(< 1)$. If the condition is satisfied, it means that enough detections have been attempted successfully, and the obtained probabilistic model $(u^+, C_u^)$ is sufficiently precise to consider the ego-lane recognition finished. Otherwise, the ego-lane

recognition process carried out, and the second most informative ROI is selected.

The end of the marking detection involves the end of the ego-lane level localization. Indeed, the update of the model $u, C_{u}$ leads to the update of the model $X_{v}, C_{X_{v}}$. This means that an estimation of the road parameters $c_{2}, x_{0}$ is performed.

### 3.3 Lane level localization (LLL)

Once the ego-lane localization is estimated, we have to perform the lane-level localization to correctly choose the right lane on which the vehicle travels. To do so, we proposed in [22] a probabilistic framework that is split into three stages. Thus, the presented LLL algorithm is an extension of our work proposed in [22]. Indeed, the Hidden Markov Model's architecture is the same. The difference lies in the input of the algorithm, as we take the information about the road from OSM. In addition, the parameters of the road, such as the curvature, are also extracted from OSM, which will be useful for interpolating other lanes marking.

In the first stage, we extrapolate adjacent lanes by assuming that lanes in the same road have the same width $L_{w}$ and the variation in the curvature $c_{1}$ is very small. The second step consists of a Bayesian Network (BN), that takes as input the results of the hypothesized adjacent lane-marking detection, whether these detections succeed or fail. Furthermore, since the proposed BN is modular, we also use an adjacent vehicle detector based on deep learning. The third step includes a filtering process, using a Hidden Markov Model (HMM).

### 3.3.1 Adjacent lanes extrapolation

The adjacent lanes are extrapolated by taking advantage of the estimated ego-lane localization. Thus, each adjacent lane is described by a probabilistic model $\left\{X_{l}, C_{X_{l}}\right\}$, where $X_{l}$ contains the parameters $\left(x_{0}, c_{2}\right)^{T}$ described in Section 3.2 and $C_{X_{l}}$ refers to the corresponding covariance matrix. The assumption made is that the curvature and lane width stays constant for all the lanes in the same road. Thereby, the value of the vector $X_{l}$ remains the same as $x_{v}$ described in equation (6), only the value of $x_{0}$ will be shifted by a $\left( \pm i L_{w}\right)$, with $(-i)$ indicates that the edge is at the right of the ego-lane and $(+i)$ the left. The number of adjacent lanes extrapolated is equal to the lanes number from OSM. Thus, from a perspective view, the hypothesized lanes are shown in Figure 9.

As mentioned in the ELL section, the model $\left\{X_{l}, C_{X_{l}}\right\}$ can be transferred to the model image $\left\{u_{l}, C_{u_{l}}\right\}$. As a consequence, $u_{l}$ represents the horizontal pixel of the edges in the image and $C_{u_{l}}$ its interval confidence. In Figure 10, the adjacent lane regions of interest resulting from the extrapolation are shown.

For each adjacent lane marking extrapolated, the detection is performed and the results are fed into a Bayesian Network (BN).

### 3.3.2 Bayesian network for ego-lane determination

The proposed BN is designed to be flexible and modular for other detection results from any type of sensor, i.e. vehicle detector, guardrail detector. In order to show the flexibility
of the BN, we will first use only adjacent lanes detection to determine the ego-lane. Thereafter, an adjacent vehicle detector based on Deep Learning (YOLO [45]) is introduced. The general architecture of the BN used is illustrated in Figure 11. The described nodes are the following:

- $Z_{k_{i}}$ the element $i$ is observable, this element can represent any element of the road scene: (vehicles, lane-marking, traffic signs...),
- $D_{k_{i}}$ the detection of the element of type $k$ is successful. Later we will use $D_{l}$ for adjacent lanes and $D_{v}$ for vehicles,
- $L_{B N}$ the lane on which the ego-vehicle is traveling, $L_{B N}$ is a form of categorical distribution, $L_{B N} \sim$ $\operatorname{Cat}(\xi)$ with $L_{B N}=\left\{l_{1}, \ldots, l_{n}\right\}$, where $l_{1}$ indicates the leftmost lane and $n$ the lanes number.

Depending on the results of the detection, we infer the probability to belong to a lane $l_{i}$ as follows:

$$
P\left(L_{B N=l_{i}}\right)=P\left(L_{B N=l_{i}} \mid D_{k_{1}}, Z_{k_{1}}, \ldots, D_{k_{n}}, Z_{k_{n}}\right)
$$

The lane with the highest probability is chosen to be the lane on which the vehicle travels. As mentioned before, the proposed BN is aimed to be modular for other detectors. To start, we only use the Adjacent Lanes Detection (ALD) as input into our BN (BN + ALD), where $D_{l_{i}}$ indicates whether the detection of adjacent lane $i$ is successful. After, we add the information about the adjacent vehicles $D_{v_{i}}$ using the Yolo detector, where $D_{v_{i}}$ indicates whether the detection of the adjacent vehicle $i$ is successful. Knowing that, this detection is performed in the regions of the image bounded by the neighboring marking-lanes.

### 3.3.3 HMM for ego-lane determination

The proposed BN in the previous section is applied on a per-frame basis. However, the dynamic relationship between two consecutive frames is not taken into account. Indeed, the BN does not take into consideration the dynamic constraints of the ego-vehicle (i.e. the ego-vehicle can only change lane to an adjacent lane). In order to take into account these constraints, we filter the output of the BN by a Dynamic Bayesian Network which is the Hidden Markov Model (HMM).
We will use $L_{t}$ to denote the set of ego-lane state variables at time $t$, which depends on the lanes number $n_{\text {lanes }}$ and
![img-9.jpeg](img-9.jpeg)

Fig. 9: Detected ego-lane in solid red and the hypothesized lanes in dash

![img-10.jpeg](img-10.jpeg)

Fig. 10: Results of the adjacent lane regions of interest resulting from the extrapolation
![img-11.jpeg](img-11.jpeg)

Fig. 11: Final architecture Bayesian Network (BN) used for ego-lane determination.
which are assumed to be observable. $e_{t}$ denotes the observable evidence variable. The aim of the filter algorithm is to estimate the probability $P\left(L_{t+1} \mid e_{1: t+1}\right)$. According to [46], this probability can be formulated as follows:

$$
\begin{aligned}
P\left(L_{t+1} \mid e_{1: t+1}\right) & =P\left(L_{t+1} \mid e_{1: t}, e_{t+1}\right)_{\text {(Eviding up the evidence) }} \\
& =\eta P\left(e_{t+1} \mid L_{t+1}, e_{1: t}\right) P\left(L_{t+1} \mid e_{t+1}\right)_{\text {(Buyer rule) }} \\
& =\eta P\left(e_{t+1} \mid L_{t+1}\right) P\left(L_{t+1} \mid e_{t+1}\right)_{\text {(Markov assumption) }}
\end{aligned}
$$

Where $\eta$ denotes a normalizing constant to make probabilities sum equal to 1 . By arranging Equation (16):

$$
\begin{aligned}
P\left(L_{t+1} \mid e_{1: t+1}\right) & =\eta P\left(e_{t+1} \mid L_{t+1}\right) \sum_{l_{t}} P\left(L_{t+1} \mid L_{t}, e_{1: t}\right) P\left(L_{t}, e_{1: t}\right) \\
& =\eta P\left(e_{t+1} \mid L_{t+1}\right) \sum_{l_{t}} P\left(L_{t+1} \mid L_{t}\right) P\left(L_{t}, e_{1: t}\right)
\end{aligned}
$$

The probability $P\left(e_{t+1} \mid L_{t+1}\right)$ comes from the observation model. Hence, in this paper from the BN described previously, thus:

$$
P\left(e_{t+1} \mid L_{t+1}\right)=P\left(L_{B N}\right)
$$

With regard to the probability $P\left(L_{t+1} \mid l_{t}\right)$, it comes from the transition model. It expresses the probability of the egolane to change its current state, which is the lane change probability. Finally, the third term $P\left(L_{t}, e_{1: t}\right)$ expresses the current state distribution. Graphically, we can illustrate the corresponding HMM as in Figure 12.
With the recursive formulation obtained in Equation (17),
![img-12.jpeg](img-12.jpeg)

Fig. 12: Hidden Markov Model for $n$ lanes case, with $L=\left\{l_{1}, l_{2}, \ldots, l_{n}\right\}$ being the set of hidden states and $O=\left\{e_{1}, e_{2}, \ldots, e_{n}\right\}$ being the set of observations resulting from the BN.
we can estimate the current ego-lane state given the observation obtained from the BN, but before we have to compute the lane change probability.

### 3.3.4 Transition probability (Lane change probability)

To calculate the lane change probability, we model the lateral position $x_{0}$ estimated in the ego-lane level localization as a normal distribution with mean $\mu_{x_{0}}$ and variance $\sigma_{x_{0}}$ :

$$
x_{0} \sim \mathcal{N}\left(\mu_{x_{0}}, \sigma_{x_{0}}^{2}\right)
$$

The value $\mu_{x_{0}}$ and variance $\sigma_{x_{0}}$ are obtained from the estimated probabilistic model $\left(x_{v}, C_{x_{v}}\right)$. Therefore, we predict the lateral position $x_{0}$ at time $t_{k+1}$ as shown on Fig 13. Accordingly, the lane-change probability is calculated as
![img-13.jpeg](img-13.jpeg)

Fig. 13: Lane change probability, with the blue area representing the right change probability. The coordinate system for $x_{0}$ is centered on the vehicle

follows:

$$
\begin{aligned}
& P\left(C_{r}\right)=\int_{L_{w} / 2}^{+\infty} \frac{1}{\sigma_{x_{0}} \sqrt{2 \pi}} \mathrm{e}^{-\frac{\left(x-\mu_{x_{0}}\right)^{2}}{2 \sigma_{x_{0}}^{2}}} d x \\
& P\left(C_{l}\right)=\int_{-\infty}^{-L_{w} / 2} \frac{1}{\sigma_{x_{0}} \sqrt{2 \pi}} \mathrm{e}^{-\frac{\left(x-\mu_{x_{0}}\right)^{2}}{2 \sigma_{x_{0}}^{2}}} d x
\end{aligned}
$$

with $P\left(C_{r}\right)$ the probability to right change lane and $P\left(C_{l}\right)$ the probability to left change lane.
Now that we have designed the HMM, we will introduce the real-world experimental results in the following section.

## 4 REAL-WORLD EXPERIMENTAL RESULTS

The different parts of the localization algorithm have been introduced in the previous section. In order to prove the effectiveness of the presented algorithms, real-world experiments have been carried out.
To do so, we tested our algorithm on real driving datasets. The first one was collected in the region of ClermontFerrand in France, where we drove our acquisition vehicle on two lanes and three lanes road in a national highway. In order to collect these datasets, the acquisition vehicle was equipped with a front camera, with the addition of an IMU and a classic GPS receiver. The data have been stored on a bag using using ROS. In addition to that, the ego-vehicle provides information about its own odometery. Finally, these datasets will be made available for researchers ${ }^{1}$. In the following, they will be referred to as " 2 -lanes" for two lanes road and " 3 -lanes" for three lanes road ( 1000 images frames).
Furthermore, we wanted to compare the performances of our algorithm to the literature on more challenging scenarios. Naturally, we turned our attention to the KITTI datasets [47]. Although these dataset contain few lanechanging scenarios, we will however use some part of those in order to show the effectiveness of our RLL module. In addition, we tested our algorithm on some datasets referred to in [19]. Unfortunately, all the data were not ready yet. We were able to test on some of them, noted as the A4Highway Italy, for a total of 9528 frames. The collected datasets were manually annotated in a per-frame basis in order to determine the correct ego-lane classification. In the following, we will refer to these datasets as " 4 -lanes".
Each part of the ego-localization: RLL, ELL and LLL will be tested on the presented datasets, the results will be discussed in terms of accuracy. In the end, the overall algorithm will be discussed in terms of computation time.
In order to assess the presented RLL algorithm, the correct Way has been manually annotated for each GPS frame. The resulting ground truth was compared with HMM-MM. The results are summarized on Table 2. As highlighted, the Map-Matching with the addition of the HMM improves the overall accuracy precision. This can be explained by the inclusion of the topology of the road network in the HMM. Indeed, the transition states are governed by the connectivity between links. Furthermore, we test the reliability of our algorithm in more challenging scenarios. Thus, we used the well-known

1. shorturl.at/1AR28


TABLE 2: Map Matching results on the entire datasets without and with the HMM, KITTI-1 and KITTI-2 refer to KITTI sequences:'_2011_09_26_0001' and '_2011_09_26_0002'

KITTI [47] database in urban scenarios. The used sequences are the following: "sequence_2001_09_26_0001" and "sequence_2001_09_26_0001". Even if the two sequences were taking in urban areas, the correct map-matching obtained shows the effectiveness and the robustness of our proposed RLL algorithm in varying scenarios. Finally, it can be noticed that for the " 4 -lanes", the GPS datasets have not been mentioned. Indeed, practically the entirety of the datasets is on the same Highway. Thus, the results on MM would not be relevant.
As discussed in [48] [13], in most of the work presented in the literature, the aim is to find the white strips in the image without seeking for consecutive elements of lane marking. Cnversely, in our work, we are more interested in the curvature of the lane marking than the white strips. However, by doing so, the characterization of the algorithm is considerably more difficult. Some examples are presented in Figure 14 showing the robustness of the presented egolane marking detector on different lighting conditions. Once the ego-lane localization completed, the Lane level localization is performed. So as to point out the increment of each added part, we first, determined the ego-lane using solely the BN with adjacent lanes. Within the second instance, we introduced adjacent vehicle detection in the BN. In all instances, we filtered the outcome of the BN with the HMM. All the results obtained are summarized in Table 3.
Considering the results, the increment provided by each module is clearly illustrated. Indeed, altogether cases the
![img-14.jpeg](img-14.jpeg)

Fig. 14: Some examples of correct ego-lane marking recognition (in Blue). As highlighted, the ego-lane marking are correctly detected in varying imaging conditions: low light level for the top images and high brightness for the bottom images.


TABLE 3: Classification accuracy for ego-lane determination. BN+ALD refers to the BN feed with the adjacent lanes detection, BN+ALD+HMM indicates the HMM with the corresponding BN, BN+ALD+AVD refers to the BN feed with adjacent lanes and vehicles detection and BN+ALD+AVD+HMM refers to the HMM with the corresponding BN.

BN+ALD+AVD provides more accurate classification than the BN+ALD, which suggests that the addition of another information source also will improve the obtained accuracy. After investigation on the inaccurate results, it appears that the false classifications obtained using the BN+ALD are due to two main reasons: either the lanes marking are not detected or the lanes marking are wrongly detected. For the primary case, this can be explained if the lanes marking are missing or hidden by an object. For the second case, it shows the limitation of the used lane marking detector. Moreover, even if the introduction of the adjacent vehicle detection shows excellent results, there are some cases where the vehicles detection are not relevant, for instance, if the detected vehicle is on the nearby road. To overcome this issue, we would have to determine the localization of the detected vehicle relative to the ego-vehicle, which is not the case since we use solely images as input.
Finally, despite that the authors ${ }^{2}$ in [19] did not take into account the lane change scenarios and designed empirically the HMM. Nevertheless, we manage to outperform their results on the same datasets. Indeed, they achieved $77 \%$ correct classifications, where we were able to reach $85.35 \%$ on 9528 frames. Some ELL in different images are presented in Figure 15. The presented results have been carried using Python 3.7 under a Dell G3 3579 Core i7 8th generation equipped with an NVIDIA GeForce GTX 1050 Ti. The computation time results presented in Figure 16 shows that even if the entire algorithm was coded in Python, real-time implementation is possible. Indeed, the sum of all parts of the ego-localization algorithm is under 500 ms ( 446.95 ms on average). In addition, if we glance in-depth at the time consumed in the RLL, we found that on average, it takes 238.16 ms to query the local server containing the OSM data. Furthermore, from the 143.67 ms dedicated to the LLL, 65.60 ms are spent on the YOLO detector. These results lead us to assume that implementation on $\mathrm{C} / \mathrm{C}++$ will divide the calculation time by 10 .

## 5 CONCLUSION

In this paper, we presented an end-to-end ego-vehicle localization. Starting from Road-level localization (RLL) using OSM datasets and a classic GPS receiver, to the Ego-lane level localization (ELL) using a recognition lane marking in an information-driven fashion and finally, a Lane-level localization (LLL) using the well-known YOLO detector in a probabilistic framework composed of a Bayesian Network and Hidden Markov Model to correctly determine the egolane in the road. The distinction from other work lies in the overall aspect of the ego-localization that has been tackled
2. The authors would like to acknowledge the authors of [19] for their help with their datasets.
in stock in the paper. In addition, this work is distinguished by the information-driven approach.
For our future work, we are currently working on adding detectors from different sensors, i.e., lidar, radar to enhance the proposed framework. On the other hand, we are still working on the OSM datasets in order to update this database when it provides false information about the environment.

## 6 Acknowledgment

This work has been sponsored by Sherpa Engineering and ANRT (Conventions Industrielles de Formation par la Recherche). This work has also been sponsored by the French government research program Investissements d'avenir through the RobotEx Equipment of Excellence (ANR-10-EQPX-44) and the IMobS3 Laboratory of Excellence (ANR-10-LABX-16-01), by the European Union through the program Regional competitiveness and employment 2014- 2020 (FEDER - AURA region) and by the AURA region.
