# Personalized Trip Planning Considering User Preferences and Environmental Variables with Uncertainty 

Mingu KIM ${ }^{\dagger+\mathrm{a}}$, Student Member, Seungwoo HONG ${ }^{\dagger \dagger+\mathrm{b}}$, and Il Hong SUH ${ }^{\dagger \mathrm{c}}$, Nonmembers


#### Abstract

SUMMARY Personalized trip planning is a challenging problem given that places of interest should be selected according to user preferences and sequentially arranged while satisfying various constraints. In this study, we aimed to model various uncertain aspects that should be considered during trip planning and efficiently generate personalized plans that maximize user satisfaction based on preferences and constraints. Specifically, we propose a probabilistic itinerary evaluation model based on a hybrid temporal Bayesian network that determines suitable itineraries considering preferences, constraints, and uncertain environmental variables. The model retrieves the sum of time-weighted user satisfaction, and ant colony optimization generates the trip plan that maximizes the objective function. First, the optimization algorithm generates candidate itineraries and evaluates them using the proposed model. Then, we improve candidate itineraries based on the evaluation results of previous itineraries. To validate the proposed trip planning approach, we conducted an extensive user study by asking participants to choose their preferred trip plans from options created by a human planner and our approach. The results show that our approach provides human-like trip plans, as participants selected our generated plans in $57 \%$ of the pairs. We also evaluated the efficiency of the employed ant colony optimization algorithm for trip planning by performance comparisons with other optimization methods.


key words: recommender system, personalization, trip planning, probabilistic modeling and ant colony optimization

## 1. Introduction

Traveling is among the most preferred leisure activities worldwide, and the number of travelers has been steadily increasing by the improving living standards [1], [2]. Besides its continued growth, tourism has experienced a notable change in recent years, as people want to customize their trips. However, this customization is challenging and timeconsuming, despite the easily available information about destinations provided by various dedicated web services. A survey determined that $57 \%$ of US travelers prefer travel information providers that adapt information to their personal preferences, and $36 \%$ is willing to pay more for such services [3].

Personal preferences can be classified into soft and hard. Soft preferences are appealing but not essential for

[^0]a trip plan to be valid, whereas hard preferences represent necessary conditions that must be met, such as travel budget and total travel time. In this paper, we use the term "preferences" for soft preferences and "constraints" for hard preferences, and our proposed approach can handle both.

A difficulty during trip planning is the selection of attractive places of interest (POIs) and their correct arrangement. If the created plan does not meet constraints such as schedule or budget, planning should be repeated considering the myriad of possible trip plans. Planning should also consider many other constraints, such as the opening and closing times of the POIs. Moreover, travelers should consider environmental variables from the destination. For example, weather conditions are crucial for trip planning, as expected rains usually lead to choose indoor POIs, such as museums and aquariums. Likewise, local traffic conditions should be considered during planning given its influence on the plan realization. Furthermore, the traveler should consider that these environmental factors can be highly uncertain and unpredictable during planning.

In this paper, we propose an effective approach for trip planning that maximizes user satisfaction based on personal preferences while considering various constraints and uncertainty in environmental variables. The proposed approach uses a probabilistic graphical model to represent the satisfaction and constraints as random variables comprising user preferences and environmental variables, such as weather and traffic conditions, and allows to evaluate an itinerary in terms of the sum of time-weighted satisfaction. Then, we adopt ant colony optimization (ACO) to efficiently find the itinerary that maximizes the objective function while satisfying the constraints.

The rest of this paper is organized as follows. In Sect. 2, we review previous approaches related to travel recommendation systems. Section 3 formalizes the probabilistic travel planning problem. Section 4 details the proposed probabilistic itinerary evaluation model and its inference. Section 5 shows the adoption of ACO to generate the trip plan that maximizes user satisfaction. Finally, we present comprehensive experimental results and draw conclusions in Sect. s 6 and 7 , respectively.

## 2. Related Work

The interest to investigate travel recommendation approaches has been increasing with the growth of tourism. In this section, we review previous studies related to trip


[^0]:    Manuscript received February 22, 2019.
    Manuscript revised June 14, 2019.
    Manuscript publicized July 24, 2019.
    ${ }^{\dagger}$ The authors are with Department of Electronics and Computer Engineering, Hanyang University, Seoul, Republic of Korea.
    ${ }^{\ddagger}$ The author is with Department of Intelligent Robot Engineering, Hanyang University, Seoul, Republic of Korea.
    ${ }^{\text {a }}$ M. Kim and S. Hong have equally contributed to this work.
    a) E-mail: mgkim1013@hanyang.ac.kr
    b) E-mail: swcoke@mobiletalk.co.kr
    c) E-mail: ihsuh@hanyang.ac.kr (Corresponding author)

    DOI: 10.1587/transinf.2019EDP7052

planning.

POI recommendation system is a branch of recommendation systems that suggests a new POI to be visited by a tourist. It is closely related to travel itinerary recommendation and provide great intuition for the trip planning problem in terms of POI evaluation. It has been addressed by Feng et al. [4], who proposed an approach to select POIs using personalized ranking metric embedding based on user preferences and geographical influences. In [5], Zhao et al. present spatiotemporal latent ranking for time-aware successive POI recommendation based on ranking-based pairwise tensor factorization. Yin et al. [6] used a spatiotemporal latent Dirichlet allocation model to learn region-dependent personal interests and proposed an attribute pruning algorithm for POI recommendation. Yao et al. [7] developed a POI recommendation system based on temporal matching between users and POIs to incorporate temporal popularity of POIs and user regularities. In [8], Han et al. focused on the geographical diversification of recommended POIs and proposed a method that recommends a variety of POIs located in a user's activity district. Yang et al. [9] proposed a framework incorporating semi-supervised learning and collaborative filtering for POI recommendation to overcome data scarcity. In [10], the authors proposed a spatialaware hierarchical collaborative deep learning model to learn spatial-aware personal preferences. They also developed methods for social regularization and spatial smoothing to overcome data sparsity, thus establishing an approach to provide POI recommendation. Zhao et al. [11] utilized hierarchical structures of both users and POIs using hierarchical geographical matrix factorization for POI recommendation. Wang et al. [12] proposed a framework for POI recommendation that incorporates users' historical check-ins and varied auxiliary information, such as geographical influences among POIs and social influences among users. Cai et al. [13] presented a feature-space separated factorization model to make POI recommendation, where the model represents multiple features of a POI in a separate latent space.

Although these works are closely related to trip planning problem, several differences exist between POI and itinerary recommendation. The most notable difference is the inability to evaluate trip plans from individual POI evaluation, because the plan can be affected by the order of the POIs in the itinerary. To address this issue, many researchers have proposed specific approaches for trip planning. In [14], De Choudhury et al. proposed an itinerary recommendation system based on photo streams from a media hosting service. They used the streams to construct a POI graph using visit counts, visit times, and travel time between POIs, and a recursive greedy algorithm was used to optimize the itinerary on the graph. Gionis et al. [15] developed tour recommendation with a specific sequence of POI categories with two different itinerary evaluation measures: additive- and coverage-based user satisfaction. Bolzoni et al. [16] proposed a cluster itinerary planning algorithm for tour recommendation with the constraint of POI category visit counts and presented two POI selection methods for
exact and greedy solutions. In [17], Cheng et al. investigated information from user profiles including gender, age, and race, and adopted a Bayesian framework to represent the sequential correlation between POIs and this information. Then, Chen and Cheng [18] extended this work by considering the size of groups of people traveling together retrieved from face detection. In [19]-[21], Brilhante et al. developed a personalized itinerary planning method and formulated the trip planning problem as an instance of the generalized maximum coverage problem. The method comprises two steps for selection of sub-itineraries and combination to maximize users' personal interests. Lim et al. [22], [23] proposed an algorithm called PersTour to personalize tour recommendations considering user preferences and POI popularity, which were determined using geotagged photos from the Flickr database.

These previous works on trip recommendation investigate various factors for itinerary evaluation such as user preferences, user attributes, size of traveling group, POI popularity, sequence of POI categories, and POI category visit counts. However, they did not consider environmental uncertainties, such as opening and closing times of POIs, weather, and traffic, which are crucial to realize the recommended trip plan. To the best of our knowledge, few studies have addressed trip recommendation considering environmental uncertainty. Chen et al. [24] considered traffic conditions along with personal preferences and time budget constraints for trip planning. They collected taxi GPS footprints to obtain data for time-varying transit time modeling and constructed a dynamic POI network model based on the collected GPS data, popularity and geographical location of the POIs. In terms of itinerary planning, they proposed a two-phase approach consisting of route search and route augmentation. Similarly, Gavalas et al. [25] considered time-dependent travel times among POIs as in [24].

The approaches in [24] and [25] consider time-varying travel times between two POIs but simplify modeling to travel times between POIs according to different departure times to build a POI network considering the time of user's request. In contrast, our approach directly models uncertainties using a probabilistic framework, thus enabling itinerary evaluation based on uncertainties in several aspects including travel time. Moreover, we consider variable travel times depending on the user. For example, an inexperienced driver may be delayed when arriving at a POI, and these delays will accumulate until the last POI, to which the traveler might arrive much later than scheduled. Therefore, trip planning should prepare an itinerary considering worst-case scenarios to satisfy constraints. In [26], Zhang et al. studied tour recommendation considering POI availability and uncertain traveling times represented as random variables following some probability distributions. This approach is similar to our proposed model, but our probabilistic itinerary evaluation model expands modeling capabilities by including various uncertain factors, such as weather conditions, visit duration, and costs.

## 3. Problem Formulation

Trip planning aims to generate an itinerary that maximizes the expected user satisfaction while satisfying various constraints. The satisfaction is affected by user preferences and various environmental variables such as weather conditions and visit duration to POIs. The environmental variables have probabilistic uncertainties, and hence it is convenient to represent both user satisfaction and constraints stochastically. More formally, we define the trip planning problem as a stochastic constrained optimization problem.

Definition 1 (POIs): Let $\mathbb{X}=\left\{x^{1}, x^{2}, \ldots, x^{[\mathbb{X}]}\right\}$ be a set of POIs, where $[\mathbb{X}]$ denotes the cardinality of set $\mathbb{X}$. A POI $x^{i}$ is defined by sextuple $\left(D_{x^{i}}, C_{x^{i}}, s c_{x^{i}}, p c_{x^{i}}, o t_{x^{i}}, c t_{x^{i}}\right)$, where $D_{x^{i}}$ is the visit duration, $C_{x^{i}}$ is the cost of the visits, $s c_{x^{i}} \in[0,5]$ is the POI rating provided by people who have visited it, $p c_{x^{i}} \in \mathbb{P C}$ is the POI category, $o t_{x^{i}}$ is the opening time, and $c t_{x^{i}}$ is the closing time. Visit duration $D_{x^{i}}$ is a continuous random variable dependent on the traveler. Likewise, cost of the visits $C_{x^{i}}$ is also a continuous random variable to represent the varying range of prices from POIs such as restaurants, hotels, and tourist attractions.

In this paper, we denote random variables with uppercase letters and their instantiations with lowercase letters.

Definition 2 (Trip Question): Trip question $q$ is defined by decuple $\left(x_{s}, x_{e}, t_{s}, t_{e}, b, \mathbb{X}_{+}, \mathbb{X}_{-}, \mathbb{P C}_{+}, \mathbb{P C}_{-}, \mathbb{U}\right)$, where $x_{s}$ and $x_{e}$ are the initial and final POIs on the itinerary, respectively, $t_{s}$ and $t_{e}$ are the initial and final times of the schedule, respectively, $b$ is the total budget for the trip, $\mathbb{X}_{+}$and $\mathbb{X}_{-}$ are the sets of POIs that the itinerary should include and exclude, respectively, $\mathbb{P C}_{+}$and $\mathbb{P C}_{-}$are sets of POI categories that the itinerary should include and exclude, respectively, and $\mathbb{U}$ is the set of user preferences about POI categories. User preference $u_{i} \in \mathbb{U}$ represents the predilection for POI category $p c_{i}$, whose default value is 0.5 and $u_{i} \in[0,1]$.

Definition 3 (Itinerary): Itinerary $\mathcal{I}=<x_{0}, x_{1}, \ldots, x_{[\mathcal{I}]}>$ is defined by an ordered set of POIs, whose elements belong to POI set $\mathbb{X}, x_{0}$ and $x_{[\mathcal{I}]}$ should be equal to $x_{s}$ and $x_{e}$, respectively, and the itinerary cannot contain repeated POIs. As the set is ordered, two itineraries with the same POI set but different orders are different.

Definition 4 (Probabilistic Trip Planning Problem): Let $S_{x_{i}} \in[0,5]$ be a continuous random variable representing the user satisfaction in POI $x_{i}$, where $S_{x_{i}}$ depends on the target POI and various other factors, such as visit duration, weather conditions, and user preferences. The probabilistic trip planning problem aims to find the best itinerary from all feasible itineraries based on trip question $q$ and is defined as the following stochastic constrained optimization problem:

$$
\mathcal{I}^{*}=\underset{\mathcal{I}}{\operatorname{argmax}} \sum_{i=1}^{[\mathcal{I}]} E\left[S_{x_{i}}[\mathcal{I}, q] E\left[D_{x_{i}}[\mathcal{I}, q\right]\right.
$$

subject to

$$
P\left(T_{i} \geq o t_{x_{i}}[\mathcal{I}, q)>1-\epsilon, \quad \text { for all } 1<i<[\mathcal{I}],\right.
$$

Table 1 List of variables for trip planning


$$
P\left(T_{i}^{d} \leq c t_{x_{i}}[\mathcal{I}, q)>1-\epsilon, \quad \text { for all } 1<i<[\mathcal{I}]\right.
$$

$$
P\left(T_{[\mathcal{I}]} \leq t_{e}[\mathcal{I}, q)>1-\epsilon\right.
$$

$P\left(\sum_{i=1}^{[\mathcal{I}]} C_{x_{i}} \leq b[\mathcal{I}, q\right)>1-\epsilon$,
$\mathbb{X}_{+} \subset \mathcal{I}$, and $x_{i} \notin \mathbb{X}_{-} \quad$ for all $x_{i} \in \mathcal{I}$,
$\mathbb{P C}_{+} \subset \mathbb{P C}_{\mathcal{I}}$, and $p c_{x_{i}} \notin \mathbb{P C}_{-} \quad$ for all $x_{i} \in \mathcal{I}$,
where $\epsilon$ is a small positive real number, $T_{i}$ is the random variable representing the time of user arrival to POI $x_{i}, T_{i}^{d}$ is the random variable representing the time of user departure from POI $x_{i}$, and $\mathbb{P C}_{\mathcal{I}}=\left\{p c_{x_{i}}: x_{i} \in \mathcal{I}\right\}$ is the set of POI categories in itinerary $\mathcal{I}$.

Objective function (1) maximizes the sum of expected user satisfaction $E\left[S_{x_{i}}[\mathcal{I}, q]\right.$ weighted by expected visit duration $E\left[D_{x_{i}}[\mathcal{I}, q]\right.$ given itinerary $\mathcal{I}$ and trip question $q$. Without the weighting term, the planner would be biased towards trip plans with POIs retrieving the shortest visit duration, because the sum of user satisfaction measures would be higher by visiting more POIs within the limited travel time. For example, a trip plan consisting of four 2-point POIs will be worth more than that consisting of one 5-point POI. Therefore, it is reasonable to weight user satisfaction by the visit

duration.
Constraints (2) and (3) imply that the arrival to and departure from a POI should be after its opening time and before its closing time, respectively. In addition, constraint (4) guarantees that the itinerary is completed before end time $t_{e}$, and constraint (5) guarantees that the total cost of the itinerary activities remains below budget limit $b$. Finally, (6) and (7) represent constraints on the itinerary and POI categories, respectively.

In (1-7), we use conditional expectations and probabilities to represent the objective function and constraints. Therefore, to solve this probabilistic trip planning problem, we need a model to infer probability distributions $P\left(S_{x_{i}} \mathcal{D}, q\right), P\left(D_{x_{i}} \mathcal{D}, q\right), P\left(T_{i} \geq o t_{x_{i}} \mathcal{D}, q\right), P\left(T_{i}^{d} \leq c t_{x_{i}} \mathcal{D}, q\right)$, $P\left(T_{\mathcal{D} \mid} \leq t_{e} \mathcal{D}, q\right)$, and $P\left(\sum_{i=1}^{\mathcal{D} \mid} C_{x_{i}} \leq b \mathcal{D}, q\right)$. We adopt a hybrid temporal Bayesian network (BN) [27] that can represent both causal and temporal stochastic relations for determining the solution.

## 4. Probabilistic Itinerary Evaluation Model

### 4.1 Hybrid Temporal BN

Theoretically, if we have a joint probability distribution of all relevant random variables, then any marginal, joint, or conditional probability from a subset of those random variables can be directly inferred. In practice, however, explicitly obtaining the joint distribution is difficult for a system containing several random variables for many reasons. First, the number of probabilities to be stored increases exponentially with the number of random variables, thus being memory expensive to store this information. Moreover, it is computationally expensive to manipulate the several random variables, and the data required to obtain the probabilities will be also prohibitive.

Alternatively, a BN provides a compact representation of the joint probability distribution based on a set of conditional independence assumptions of the underlying random variables. These assumptions are represented as a directed acyclic graph, whose nodes correspond to the random variables and the edges describe the influence from origin to destination node. Therefore, a BN encodes local independence as each variable is assumed to be conditionally independent of its non-descendant nodes given its parent nodes, and it factorizes the joint distribution from the network topology and conditional probability distributions as follows:

$$
\begin{aligned}
& V_{i} \perp \text { NonDescendants } V_{i} \mid P a_{V_{i}}^{G} \quad \text { for all } V_{i} \\
& P\left(V_{1}, \ldots, V_{n}\right)=\prod_{i}^{n} P\left(V_{i} \mid P a_{V_{i}}^{G}\right)
\end{aligned}
$$

where $G$ is a BN graph over nodes (variables) $V_{1}, \ldots, V_{n}$ and $P a_{V_{i}}^{G}$ denotes the parents of node $V_{i}$ in $G$.

We use a BN that admits discrete and continuous random variables, thus establishing a hybrid BN. In addition,
our BN can be considered as dynamic [28], [29] because it represents sequential events. The most notable difference between our hybrid dynamic BN and a conventional dynamic BN is the explicit representation of time as a random variable in the proposed BN, which simultaneously enables the inference of both events in the continuous time domain and their time of occurrence. Therefore, we call the proposed network a hybrid temporal BN.

Figure 1 illustrates the proposed probabilistic itinerary evaluation model based on the hybrid temporal BN. Figure 1a shows a part of the model comprising the relations of variables involved in inference of time, where arrival time $T_{i}$ is directly influenced by its preceding arrival time, $T_{i-1}$, the visit duration to the previous POI, $D_{i-1}$, and the travel time, $M_{i}$, between POIs $x_{i-1}$ and $x_{i}$. In addition, given that travel time $M_{i}$ usually depends on the departure time from previous POI $x_{i-1}$, it is affected by POIs $x_{i-1}$ and $x_{i}$, time of arrival $T_{i-1}$, and visit duration $D_{i-1}$ to the previous POI. Finally, visit duration $D_{i}$ is affected only by POI $x_{i}$. One might argue that the duration should be also influenced by the previous travel time, whose high length may induce the traveler to shorten the visit. However, considering every influence among variables would unnecessarily complicate the model, and consequently the inference and acquisition of model parameters may become intractable. Therefore, relations that we consider as negligible for model performance are assumed as conditional independence. Figure 1b describes influences among variables related to user satisfaction $S_{x_{i}}$. Satisfaction is directly affected by three variables, namely, weather suitability $W_{i}$, user preference $u_{x_{i}}$, and average score of POI $s c_{x_{i}}$. Weather suitability $W_{i}$ is a binary random variable that indicates whether a POI has favorable weather conditions at time $T_{i}$. In turn, weather conditions are represented by temperature $T E_{i}$ and probability of precipitation $R_{i}$.

### 4.2 Inference on Probabilistic Itinerary Evaluation Model

To represent the joint distribution and infer relevant probabilities for itinerary evaluation, each node must be associated with a corresponding conditional distribution, which can be of one from these 12 types: $x_{i}, D_{x_{i}}, C_{x_{i}}, M_{i}, T_{i}, T E_{i}$, $R_{i}, W_{i}, p c_{x_{i}}, s c_{x_{i}}, u_{x_{i}}$, and $S_{x_{i}}$. However, POI $x_{i}$ is given by itinerary $\mathcal{I}$, and $p c_{x_{i}}, s c_{x_{i}}$, and $u_{x_{i}}$ are deterministic functions of $x_{i}$ given $\mathcal{I}$ and $q$. Therefore, we only need the conditional probabilities of $D_{x_{i}}, C_{x_{i}}, M_{i}, T_{i}, T E_{i}, R_{i}, W_{i}$, and $S_{x_{i}}$ given their parent variables.

First, we gather candidate POIs and their associated data for $p c_{x_{i}}, c t_{x_{i}}, o t_{x_{i}}, s c_{x_{i}}, D_{x_{i}}$, and $C_{x_{i}}$ by web crawling various travel information services. We model the conditional distributions of visit duration $D_{x_{i}}$ and cost $C_{x_{i}}$ as Gaussian distributions using the estimated means ( $\mu_{x_{i}}^{d}$ and $\mu_{x_{i}}^{c}$, respectively) and variances $\left(\left(\sigma_{x_{i}}^{d}\right)^{2}\right.$ and $\left(\sigma_{x_{i}}^{c}\right)^{2}$, respectively) from the collected data. The values of other variables are deterministically obtained from POI $x_{i}$. For travel time $M_{i}$, we gather real-time navigation information for all combinations of POI pairs every hour from the Daum map ser-

![img-0.jpeg](img-0.jpeg)
(a) Part of probabilistic itinerary evaluation model including POIs, arrival times, travel times, and visit durations.
![img-1.jpeg](img-1.jpeg)
(b) Part of probabilistic itinerary evaluation model including arrival times, weather suitability, POIs, and user satisfaction.

Fig. 1 Example of probabilistic itinerary evaluation model divided into two parts. The nodes represent continuous (ellipses) and discrete (rectangles) random variables. The shaded nodes represent random variables given in advance. Edges represent direct probabilistic interactions among nodes.
vice [30]. Then, we model its conditional distribution as a Gaussian distribution using estimated mean $\mu_{\left(x_{i-1}, x_{i}, t_{i-1}+d_{x_{i-1}}\right)}$ and variance $\sigma_{\left(x_{i-1}, x_{i}, t_{i-1}+d_{x_{i-1}}\right)}^{2}$.

To infer arrival time $T_{i}$, we calculate the probability distribution of the first group of random variables, $M_{1}$ and $T_{1}$. Then, as $t_{x}, x_{x}$, and $x_{1}$ are given by trip question $q$ and itinerary $\mathcal{I}$, the distributions can be computed as

$$
\begin{aligned}
P\left(M_{1} \mathcal{I}, q\right) & =P\left(M_{1} \mid x_{x}, x_{1}, t_{x}\right) \\
& =N\left(M_{1} \mid \mu_{\left(x_{x}, x_{1}, t_{x}\right)}, \sigma_{\left(x_{x}, x_{1}, t_{x}\right)}^{2}\right) \\
P\left(T_{1} \mathcal{I}, q\right) & =\int P\left(T_{1} \mid m_{1}, t_{x}\right) P\left(m_{1} \mid x_{x}, x_{1}, t_{x}\right) d m_{1} \\
& =N\left(T_{1} \mid t_{x}+\mu_{\left(x_{x}, x_{1}, t_{x}\right)}, \sigma_{\left(x_{x}, x_{1}, t_{x}\right)}^{2}\right)
\end{aligned}
$$

where the conditional probability density function of $T_{i}$ is given by the Dirac delta function:

$$
P\left(T_{i} \mid m_{i}, d_{x_{i-1}}, t_{i-1}\right)=\delta\left(T_{i}-m_{i}-d_{x_{i-1}}-t_{i-1}\right)
$$

Then, the $i+1$-th conditional distributions, $P\left(M_{i+1} \mathcal{I}, q\right)$ and $P\left(T_{i+1} \mathcal{I}, q\right)$, can be computed by using the $i$-th distributions as

$$
\begin{gathered}
P\left(M_{i+1} \mathcal{I}, q\right)=\iint P\left(M_{i+1} \mid x_{i}, x_{i+1}, d_{x_{i}}, t_{i}\right) P\left(d_{x_{i}} \mathcal{I}, q\right) \\
P\left(t_{i} \mathcal{I}, q\right) d d_{x_{i}} d t_{i} \\
P\left(T_{i+1} \mathcal{I}, q\right)=\iint \int P\left(T_{i+1} \mid m_{i+1}, d_{x_{i}}, t_{i}\right) P\left(m_{i+1} \mathcal{I}, q\right) \\
P\left(d_{i} \mathcal{I}, q\right) P\left(t_{i} \mathcal{I}, q\right) d m_{i+1} d d_{x_{i}} d t_{i}
\end{gathered}
$$

where conditional density function $P\left(d_{x_{i}} \mathcal{I}, q\right)$ is simply $P\left(d_{x_{i}} \mid x_{i}\right)$ according to the BN local independence assumption. Departure time $T_{i}^{d}$ is given by the sum of two conditionally independent variables, $T_{i}$ and $D_{x_{i}}$, and its probability density function can be calculated as the convolution of two distributions [31], $P\left(T_{i} \mathcal{I}, q\right)$ and $P\left(D_{x_{i}} \mathcal{I}, q\right)$ :

$$
P\left(T_{i}^{d} \mathcal{I}, q\right)=\int P_{T_{i}}\left(T_{i}^{d}-z \mathcal{I}, q\right) P_{D_{x_{i}}}(z \mathcal{I}, q) d z
$$

where $P_{T_{i}}$ and $P_{D_{x_{i}}}$ denote conditional distributions $P\left(T_{i} \mathcal{I}, q\right)$ and $P\left(D_{i} \mathcal{I}, q\right)$, respectively.

For weather suitability, we obtained the temperatures and probabilities of precipitation over time using the open API of the Korea Meteorological Administration. Then, the conditional probability distribution of weather suitability is

a deterministic function of its parents, such that

$$
P\left(W_{i} \mid t e_{i}, r_{i}, p c_{x_{i}}\right)=\left\{\begin{array}{ll}
0 & t e_{i}>35^{\circ} \mathrm{C} \text { or } r_{i}=\text { true } \\
& p c_{x_{i}} \notin \mathbb{P C}_{\text {indoor }} \\
1 & \text { otherwise }
\end{array}\right.
$$

where $\mathbb{P C}_{\text {indoor }}$ is the set of indoor POI categories. Based on this local conditional distribution model, the marginal conditional distribution of weather suitability can be computed as

$$
\begin{gathered}
P\left(W_{i} \mid \mathcal{J}, q\right)=\sum_{r_{i}} \int \int P\left(W_{i} \mid r_{i}, t e_{i}, p c_{x_{i}}\right) P\left(r_{i} \mid t_{i}\right) \\
P\left(t e_{i} \mid t_{i}\right) P\left(t_{i} \mid \mathcal{J}, q\right) d t e_{i} d t_{i}
\end{gathered}
$$

Finally, the conditional density function of user satisfaction given its parents, $P\left(S_{x_{i}} \mid w_{i}, u_{x_{i}}, s c_{x_{i}}\right)$, is given by Dirac delta function $\delta\left(S_{x_{i}}-w_{i} u_{x_{i}} s c_{x_{i}}\right)$. Hence, user satisfaction is zero if POI $x_{i}$ is not suitable under weather $w_{i}$ at arrival time; otherwise, it is equal to overall score $s c_{x_{i}}$ of the POI weighted by user preference $u_{x_{i}}$.

Given these conditional distributions, we can estimate the conditional probabilities needed for itinerary evaluation:

$$
\begin{aligned}
& P\left(S_{x_{i}} \mid \mathcal{J}, q\right)=\sum_{w_{i}} P\left(S_{x_{i}} \mid w_{i}, u_{x_{i}}, s c_{x_{i}}\right) P\left(w_{i} \mid \mathcal{J}, q\right) \\
& P\left(D_{x_{i}} \mid \mathcal{J}, q\right)=P\left(D_{x_{i}} \mid x_{i}\right)=N\left(D_{x_{i}} \mid \mu_{x_{i}}^{d},\left(\sigma_{x_{i}}^{d}\right)^{2}\right) \\
& P\left(T_{i} \geq o t_{x_{i}} \mid \mathcal{J}, q\right)=\int_{o t_{x_{i}}}^{o o} P\left(t_{i} \mid \mathcal{J}, q\right) d t_{i} \\
& P\left(T_{i}^{d} \leq c t_{x_{i}} \mid \mathcal{J}, q\right)=\int_{-\infty}^{c t_{x_{i}}} P\left(t_{i}^{d} \mid \mathcal{J}, q\right) d t_{i}^{d} \\
& P\left(T_{[\mathcal{J}]} \leq t_{e} \mid \mathcal{J}, q\right)=\int_{-\infty}^{t_{e}} P\left(t_{[\mathcal{J}]} \mid \mathcal{J}, q\right) d t_{[\mathcal{J}]}, \\
& P\left(\sum_{i=1}^{[\mathcal{J}]} C_{x_{i}} \leq b \mid \mathcal{J}, q\right)=\int_{-\infty}^{b} N\left(c \mid \sum_{i=1}^{[\mathcal{J}]} \mu_{x_{i}}^{c}, \sum_{i=1}^{[\mathcal{J}]} \left(\sigma_{x_{i}}^{c}\right)^{2}\right) d c
\end{aligned}
$$

where $c$ is the sum of all costs.
Given an itinerary and a trip question, we can evaluate the itinerary and verify whether it satisfies the given constraints with the inferred probabilities in (18)-(23). A naive way to find the optimal itinerary would be to exhaustively evaluate all possible itineraries using the probabilistic itinerary evaluation model and retrieving the itinerary with the highest objective function value. However, the number of possible itineraries exponentially increases with the trip duration and other factors, making the evaluation computationally intractable. Moreover, the orienteering problem,
which resembles our trip planning problem, is a well-known NP-hard problem that has no polynomial-time algorithm retrieving its optimal solution. In fact, it took more than 3 days of computation when we evaluated all possible itineraries from 09:00 to 22:00 considering 153 POIs, although we did not use our model but only overall POI scores. Therefore, it is essential to have an efficient method to timely generate suitable candidate itineraries, as we detail in the sequel.

## 5. Ant Colony Optimization over Itineraries

In this section, we describe an itinerary optimization method that incorporates the probabilistic itinerary evaluation model and ACO [32]. ACO is a metaheuristic algorithm that provides near-optimal solutions using limited computation resources by iteratively simulating several artificial ants deployed on a graph representing the problem to be solved.

Figure 2 illustrates a trip planning problem, where the graph consists of nodes representing POIs and edges between all node pairs. Each artificial ant builds a candidate solution by traveling between nodes while satisfying the constraints in (2)-(7). At each ant motion between two POIs, the ant stochastically chooses the next node according to its attractiveness and the "pheromones" deposited by the other ants that previously selected that path. The amount of pheromone deposited by an ant depends on the quality of the itinerary determined from our itinerary evaluation model, and it guides subsequent ants to promising areas of the search space for improving the candidate itineraries. In this study, we used the MAX-MIN ant system [33], which is an ACO variant, as it is a relatively simple algorithm to implement.

To implement ACO, the attractiveness of the next POIs, $\eta_{x_{i+1} \mid \mathcal{J}, q}$, given itinerary $\mathcal{J}_{i}$ to the current POI should be modeled for providing a greedy local guidance for selecting next POI $x_{i+1}$. We incorporate the proposed probabilistic itinerary evaluation model to compute the attractiveness values as follows:

$$
\eta_{x_{i+1} \mid \mathcal{J}, q}=\frac{E\left[s_{x_{i+1}} \mathcal{J}_{i+1}, q\right] E\left[d_{x_{i+1}} \mathcal{J}_{i+1}, q\right]}{E\left[m_{i+1} \mathcal{J}_{i+1}, q\right]}
$$

where the attractiveness values are set to zero for POIs that do not satisfy the constraints in (2)-(7). In addition, we di-
![img-2.jpeg](img-2.jpeg)

Fig. 2 Example of the ACO graph for itinerary optimization over 6 POIs.

vide the time-weighted user satisfaction by the travel time to inform each ant that a long travel time may adversely influence the itinerary evaluation.

Using these attractiveness values and the initial value of pheromone, $\tau_{x_{i}, x_{i+1}}=\tau_{0}$, an artificial ant selects the next POI according to the selection probability:

$$
P\left(\operatorname{Sel}\left(x_{i+1}\right) \mid \mathcal{D}, q\right)=\frac{\tau_{x_{i}, x_{i+1}}^{\alpha} \eta_{x_{i+1} \mid \mathcal{D}, q}^{\beta}}{\sum_{x_{i+1} \in \mathbb{X}} \tau_{x_{i}, x_{i+1}}^{\alpha} \eta_{x_{i+1} \mid \mathcal{D}, q}^{\beta}}
$$

where parameters $\alpha$ and $\beta$ determine the influence of attractiveness $\eta$ and pheromone $\tau$. Equation (25) guarantees that no POI violating any constraint can be involved in the itinerary, because such POIs have zero attractiveness and therefore zero probability of being selected.

The ant repeatedly selects POIs until no more POIs satisfying the constraints remain. In most cases, the travel time budget constraint in (4) eliminates all POIs from the selectable set. When a set of ants has built candidate itineraries, pheromone trails $\tau_{x_{i}, x_{i+1}}$ are updated at each iteration as

$$
\tau_{x_{i}, x_{i+1}} \leftarrow\left[(1-\rho) \cdot \tau_{x_{i}, x_{i+1}}+\Delta \tau_{x_{i}, x_{i+1}}^{\text {best }}\right]_{\tau_{\min }}^{\tau_{\max }}
$$

where $\rho$ is the pheromone evaporation coefficient, $\tau_{\max }$ and $\tau_{\min }$ are the upper and lower bounds of the pheromone trails, respectively, and $\Delta \tau_{x_{i}, x_{i+1}}^{\text {best }}$ is the amount of pheromone deposited at the iteration. The amount of newly deposited pheromone, $\Delta \tau_{x_{i}, x_{i+1}}$, is determined from the best itinerary at that iteration retrieved using objective function (1). While the attractiveness provides a greedy local guidance for selection of the next POI, the pheromone offers a global guidance in terms of completed itineraries. Therefore, as ACO iteratively generates candidate itineraries and updates pheromone trails, more pheromones are deposited on promising edges between POIs. This way, the pheromone reflects the accumulated experience of the ant colony during the stochastic exploration of the itinerary search space.

During the early iterations of ACO, it generates relatively greedy solutions. However, as the algorithm gradually improves the itineraries based on the pheromone global guidance, it converges to an itinerary with sufficiently high objective function value. Another notable merit of ACO is its nature of anytime algorithm, which preserves the ability to retrieve a valid solution even if the algorithm stops before convergence. Thus, the tradeoff between computation time and itinerary quality can be easily adjusted.

## 6. Experiments and Results

We verified the ability of our approach to efficiently generate personalized trip plans considering user preferences and environmental uncertainties while satisfying the given constraints. Note that it is generally difficult to compare the performance of different trip planning methods for several reasons. For instance, different recommendation algorithms have been developed focused on different factors related to
the trip planning problem. In addition, there is no publicly available dataset for fair comparison among methods. Therefore, we conducted an extensive user study to validate our probabilistic itinerary evaluation model by comparing pairs of trip plans generated by our approach with those created by a human planner. Then, to demonstrate the effectiveness and efficiency of the proposed ACO-based itineraries, we compared them with those retrieved by four optimization methods: random selection (Rand), greedy nearest selection (GREEDYNeAREST), greedy highest satisfaction selection (GREEDYHIGHEST), and brute force selection with time limit (BRUTEFORCE).

### 6.1 Comparison with Human-Created Trip Plans

To validate our probabilistic itinerary evaluation model, we conducted a survey with 31 participants and asked them to choose their preferred trip plans from pairs of those generated by our approach and those created by a human planner. The participants were not aware of the source of the plans. For this experiment, we gathered 293 POIs from Jeju Island, one of the most famous tourist destinations in Korea, by web crawling travel information services. From the POIs, 153 were tourist attractions belonging to 36 categories, and the other POIs comprised 108 restaurants, 29 accommodations, 2 ferry terminals, and 1 airport. We also collected 30 human-created trip plans consisting of 72 daily plans and extracted trip questions from each plan. We used the same initial and final POIs, initial and final times of the schedule, and total cost if available. Then, the proposed approach generated trip plans based on the extracted questions.

Figure 3 illustrates the questionnaire adopted in this user study and shows side-by-side the trip plan created by the human planner (left panel) and that generated by our approach (right panel). For the example in the figure, our approach generated a trip plan following the trip question extracted from the human-created plan, where the initial and final POIs are the Jeju International Airport and the Sunbeach Hotel and Resort, respectively. The initial and final times are 09:30 and 20:00, respectively, and the total budget for the trip is KRW $\$ 35,000$. In this example, we included an additional constraint that allows only restaurant POIs to be visited at lunch and dinner times when optimizing the itinerary.

From the 72 pairs of trip plans and 31 survey participants considered in this study, we obtained 2,232 survey results. The participants chose our travel plans $57 \%$ of the time, showing that our approach can generate human-like trip plans. Besides the survey comparing pairs of plans, we asked the participants what criteria they used to choose their preferred travel plan. Twenty-three participants (approximately $74 \%$ ) stated that the most essential criterion for preferring a trip plan was the shortest travel time between POIs. Although it is difficult to conclude that this is the best criterion because there were not many participants in this study, these opinions are consistent with our consideration that the POI visitation order is crucial for trip planning.

![img-3.jpeg](img-3.jpeg)

Fig. 3 Example of questionnaire used for trip plan evaluation. The left and right trip plans were respectively created by a human planner and the proposed approach based on the trip question extracted from the human plan.

### 6.2 Comparison among Itinerary Optimization Methods

We also compared itineraries generated by the proposed ACO-based approach with those generated using the other optimization methods mentioned above to verify the efficiency and itinerary quality of our approach. To generate itineraries using these methods, we considered the same set of POIs and trip questions from the previous experiment. Rand is the naivest method, as it randomly selects an itinerary comprising POIs satisfying the constraints. GreedyNearest and GreedyHighest greedily select sequential POIs based on the shortest expected travel time and highest expected user satisfaction. BruteForce randomly selects an itinerary as Rand, but it repeatedly generates itineraries during a predefined period, evaluates the generated itineraries and finally selects the best itinerary among them. As mentioned above, we attempted to evaluate the method that retrieves the optimal itinerary by generating and evaluating every possible itinerary, but it was highly computationally expensive as it took more than 3 days to retrieve the best itinerary in the worst case. Hence, we used BruteForce
with time limit of 10 min as an alternative to the complete exhaustive search. We also limited the execution time for the proposed ACO algorithm to 2,3 , and 4 s to verify the computation time effect on the algorithm performance.

Figure 4 shows the results from these experiments. We performed the experiments 100 times for each trip question and optimization method, 50,400 times in total. Then, the results were compared in terms of average time-weighted user satisfaction normalized by the total time to complete the itinerary, because each trip question has different total travel times. The results show that the proposed ACO algorithm generates trip plans with high objective function values. Although the value was smaller than that of BruteForce, the proposed ACO algorithm took approximately one-hundredth of the computation time required by the BruteForce.

In terms of execution time and performance, the proposed ACO algorithm generated travel plans with higher objective function value and narrower standard deviation as the execution time increased. Thus, as we mentioned in Sect. 5, the tradeoff between computation time of the proposed ACO algorithm and itinerary quality can be adjusted for prioritiz-

![img-4.jpeg](img-4.jpeg)

Fig. 4 Comparison of the proposed ACO with various optimization methods regarding the normalized time-weighted user satisfaction. The numbers next to ACO and ExWe are the time limit in seconds for algorithm execution.
ing any of these aspects.
In addition, we also compared the proposed method with the method excluding weather suitability (ExWe) to show the effectiveness of considering environmental uncertainty. Figure 4 shows that the trip planner using the model excluding weather suitability has lower user satisfaction than the planner using the proposed model. Also, the method excluding the weather suitability has larger variances in user satisfaction according to the weather on the day of travel. On a good weather day, it has no significant difference from the proposed method, but the user satisfaction was greatly reduced when it rains or when the temperature is too high or too low.

## 7. Conclusions and Future Work

We propose an efficient approach to generate personalized trip plans considering user preferences and environmental factors with uncertainty while satisfying various constraints. Specifically, we propose the probabilistic itinerary evaluation model based on hybrid temporal BNs, which describe and allow to evaluate trip itineraries considering uncertainty from various relevant factors represented as random variables. Then, we propose an ACO algorithm for trip planning by incorporating the evaluation model. We have demonstrated the validity of our approach for trip recommendation through a comprehensive user study to compare our approach with trip plans created by a human planner. Furthermore, we compared the optimization of trip plans by using our approach and four methods aimed to retrieve the best itinerary and verified the effectiveness and efficiency of the proposed ACO algorithm. In future studies, we will incorporate more factors relevant to trip recommendation into our approach, such as time-varying user preferences and POI popularity. We will also explore real-time interactive trip planning based on user feedback to improve the recommended trip plans.
