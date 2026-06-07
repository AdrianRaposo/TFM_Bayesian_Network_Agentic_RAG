# WEATHER THREAT ASSESSMENT BASED ON DYNAMIC BAYESIAN NETWORK 

Miao, Y. F. ${ }^{1}$ - WANG, L. ${ }^{1}$ - ZHANG, G. A. ${ }^{1}$ - SU, Q. H ${ }^{2 *}$ - Li, X. L. ${ }^{1}$<br>${ }^{1}$ Department of Radio Navigation, Air Force Communication NCO Academy Dalian 116600, China<br>${ }^{2}$ School of Information and Mathematics, Yangtze University<br>Jingzhou 434023, China<br>*Corresponding author<br>e-mail: suqhdd@126.com

(Received $3^{\text {rd }}$ Apr 2019; accepted $17^{\text {th }}$ May 2019)


#### Abstract

This paper aims to ascertain the variation in weather threat over time. To this end, the author established an assessment model of weather threat based on the Dynamic Bayesian Networks (DBN). Then, the Hidden Markov Model (HMM) was introduced to assess the level of weather threat. To validate the proposed method, a simulation was carried out on an Unmanned Aerial Vehicle (UAV), considering all five key weather factors affecting UAV safety. The results show that the DBN-based model is much more effective than the ordinary Bayesian Network (BN) in handling fuzzy information and complex weather conditions. The research findings shed new light on the accurate rout planning of an UAV.


Keywords: UAV, DBN, HMM inference, forward-backward algorithm, conditional probability

## Introduction

Weather is a non-negligible factor in the rout planning of an UAV. Changeable weather poses a major threat to UAVs safety during reconnaissance missions. To minimize weather-induced loss and identify a safe route for UAVs, it is an urgent task to accurately quantify weather threat. Weather threat is too ambiguous, uncertain and time-dependent to be quantified by classical methods like function method (Paris and Erdogan, 1963). For instance, Tan and Du (2009) and Kilby and Hosseini (2004) reported that neither manned aircraft weather assessment nor engineering mathematic model can yield desirable results on weather threat on UAVs. Zhang et al. (2014) suggested that Gaussian approximation may lead to adverse weather.

Many researches have been done on weather threat quantification. Ramli et al. (2014) solved the weather threat on airport security by fuzzy logic. Adiwijaya (2013) created a prediction model based on weather data, and enhanced its forecast accuracy by the hybrid fuzzy-genetic algorithm. Zhu et al. (2011) identified eight weather factors that affect flight safety, and assessed the level of weather threat by the backpropagation (BP) neural network. Based on neural network and fuzzy logic, Al-Matarneh et al. (2014) developed different weather prediction models for different regions. Sannakki et al. (2013) adopted feed forward neural network to predict disease outbreaks in grapes induced by weather. The static BN (Zhu et al., 2015; Luo and Chen, 2008) was also applied to the quantitative assessment of weather threat.

In general, the above studies overlooked the time-dependence, failing to ascertain the variation in weather threat over time. The problem can be solved by DBN, a modelling and inference tool of dynamic and uncertain events. The DBN has been extensively applied in such fields as speech recognition (Zweig and Russell, 1998), threat

assessment (Tang et al., 2007; Zhang et al., 2005), and bio-sequence analysis (Tian and Lu, 2004; Hou et al., 2010).

In view of the above, this paper sets up an assessment model of weather threat, and proposes the DBN-based synthetic fuzzy assessment method for the level of weather threat. The goal is to obtain a logical level of weather threat in consideration of various factors. Specifically, the simple weight mathematical assessment was improved to evaluate the threat index under the combined effect of various weather factors. The proposed method can significantly enhance the validity, feasibility and accuracy of weather threat assessment.

The remainder of this paper is organized as follows: Section 2 introduces the Static Bayesian Network (SBN), the DBN, and Forward-Backward (FB) algorithm; Section 3 establishes a weather threat model; Section 4 assesses weather threat through simulations and experiments; Section 5 wraps up this paper with some meaningful conclusions.

# Materials and methods 

## Bayesian networks

Bayesian networks are invented to handle vague and uncertain issues in the field of artificial intelligence. As an important tool of uncertainty inference, the networks apply probability and statistics in complex domains. The SNB is a Directed Acyclic Graph (DAG), a finite directed graph with no directed cycles. In the DAG, each node represents a variable, and the edge between two nodes reflects the direct dependence between the two corresponding variables.

In general, the SBN consists of a structure diagram and a Conditional Probability Table (CPT). The CPT is a set of random variables to demonstrate marginal probability of a single variable with respect to the others. If a SBN provides sufficient conditional probabilities to derive any joint probability with given variables, then the network is considered calculable or inferential.

If $X=X_{1}, X_{2}, \ldots, X_{n}$ is the set of variables, then the joint probability distribution can be expressed as Equation 1:

$$
P\left(\mathrm{X}_{1}, \ldots, \mathrm{X}_{\mathrm{N}}\right)=\mathrm{P}\left(\mathrm{X}_{1}\right) \mathrm{P}\left(\mathrm{X}_{2} \mid \mathrm{X}_{1}\right) \ldots \mathrm{P}\left(\mathrm{X}_{\mathrm{N}} \mid \mathrm{X}_{1}, \ldots, \mathrm{X}_{\mathrm{N}-1}\right)=\prod_{i=1}^{n} P\left(\mathrm{X}_{i} \mid \mathrm{X}_{1 \ldots i-1}\right)=\prod_{i=1}^{n} P\left(\mathrm{X}_{i} \mid \mathrm{P}_{\text {arent }}\left(\mathrm{X}_{i}\right)\right)
$$

where $P_{\text {arent }}\left(X_{i}\right)$ are the parent nodes of $X_{i}$.
The SBN takes no account of the time elements of variables. Considering these elements, the network will change along the timeline, forming a DBN (Murphy, 2002). The DBN estimates the model state at each moment or a given moment based on multiple time observations, and deduces the final result through comprehensive consideration of the observations. The same features observed at different periods can supplement each other. Thus, the DBN overcomes the limit of single evidence inference, and acquires a strong inference power.

Figure 1 depicts the extension of the DBN along the timeline. It is clear that the DBN contains an initial network $B_{0}$ and a transfer network $\mathcal{B}_{\rightarrow}$. The initial network represents the initial state of the network. The probability distribution of variables in the initial state is denoted as $p(\mathrm{~b}[0])$. The transfer network $\mathcal{B}_{\rightarrow}$ describes the dependencies

between adjacent time slices in the network. The state transition probability between time $t$ and time $t+1$ is denoted as as $p(\mathrm{x}[\mathrm{t}+1] \mid \mathrm{x}[\mathrm{t}])$. To sum up, the DBN can disclose the causal relationships between variables, and identify the evolutionary state of variables on time series, making it an ideal tool for simulating and inferring dynamic events.
![img-0.jpeg](img-0.jpeg)

Figure 1. Initial network and transfer network structure of DBN

# FB algorithm 

Aiming to derive the probable values of hidden variables from numerous observed variables, the DBN is inextricably linked with the standard HMM. The network topologies of the two are interconvertible. The HMM inference is highly timedependent if there are only a few DBN nodes (Xiao, 2006).

There are two main algorithms for HMM inference: the FB algorithm and Viterbi decoding algorithm. Considering the research content, the author adopted the FB algorithm to assess the level of weather threat. For the given model $\mu=(A, B, \pi)$ and observation sequence $Y$, the FB algorithm was introduced to infer occurrence probability of the sequence $P(Y \mid \lambda)$. The FB algorithm relies on recursion operation to reduce the computing complexity in probability-solving problem.

## (1) Forward algorithm

The forward variable is defined as: $\alpha_{i}(i)=P\left(y_{1}, y_{2}, \ldots, y_{t}, x_{t}=i \mid \lambda\right)$.
Initialization (Eq. 2):

$$
\alpha_{1}(i)=\pi_{i} b_{i}\left(y_{1}\right), 1 \leq i \leq n
$$

Recursion (Eq. 3):

$$
\alpha_{t+1}(j)=\left[\sum_{i=1}^{n} \alpha_{i}(i) a_{i j}\right] b_{j}\left(y_{t+1}\right) \quad t=1,2, \ldots, T-1
$$

Result (Eq. 4):

$$
P\left(Y_{T} \mid \lambda\right)=\sum_{i=1}^{n} \alpha_{T}(i)
$$

# (2) Backward algorithm 

The backward variable is defined as: $\beta_{t}(i)=P\left(y_{(t+1)}, y_{(t+2)}, \ldots, y_{T}, x_{t}=i \mid \lambda\right)$.
Initialization (Eq. 5):

$$
\beta_{T}(i)=1,1 \leq i \leq n
$$

Recursion (Eq. 6):

$$
\beta_{t}(i)=\left[\sum_{j=1}^{n} a_{i j} b_{j}\left(y_{t+1}\right)\right] \beta_{t+1}(j) t=1,2, \ldots, T-1
$$

Result (Eq. 7):

$$
P\left(Y_{T} \mid \lambda\right)=\sum_{i=1}^{n} \pi_{i} \beta_{i}(i)
$$

The forward and backward algorithms are combined as the FB algorithm which is shown in Equation 8:

$$
P\left(Y_{T} \mid \lambda\right)=\sum_{i=1}^{n} \alpha_{i}(i) \beta_{i}(i) 1 \leq t \leq T
$$

The DBN-based weather threat assessment model for UAVs was set up in the following steps: First, determine the weather factors that affect the UAVs safety; second, carry out quantitative analysis on each factor; third, determine the CPT and Transition Probability Table (TPT).

## Weather factors affecting UAVs safety

The accuracy inference of weather threat level relies on the determination of typical weather factors. In light of the features of DBN, four factors were selected out of the various weather factors that affect the UAVs safety.

Threat Level (TL): As the parent node, the TL assesses the threat condition probability of UAVs flight at a certain point under various weather factors. In the US, EU and China, the weather TLs are depicted by four colours: blue (common), yellow (serious), orange (severe) and red (dangerous).

Weather Type (WT): Each type of weather has its unique impact on UAVs flight. For simplicity, the weather conditions were divided into 3 levels: mild (breeze, drizzle, sunny, etc.), common (moderate rain, fresh breeze, etc.) and dangerous (thunderstorm, tornado, etc.). The division clarifies the threat levels and reflects the features of DBN.

Intensity of effect (IOE): The intensity of effect varies with weather types. It is quantitatively classified in this paper.

Relative Location (RL): Both the effect range of weather and UAVs location are constantly changing. Therefore, the distance from the UAVs to the effect centre of the weather changes all the time. The variation in the relative location has a significant impact on the level of weather threat.

Flight Type (FT): The UAVs flies at different altitudes depending on the specific conditions. The maneuver operations include steep climb, dive, quick turn, and gentle turn. Under the same condition, the damage probability of the UAVs changes with time. It is assumed that the sudden flight operations (e.g. steep climb, dive, quick turn) are much more likely to be threatened than smooth flight operations (e.g. gentle turn).

The above factors were taken as the key to the flight analysis of the UAVs. Considering the factor of time, the authors created a weather threat assessment model as shown in Figure 2.
![img-1.jpeg](img-1.jpeg)

Figure 2. DBN model of weather threat

# Quantification of each factor 

Let S be the set of states of each node in the model. The factors were distinguished by the following subscripts:
$S_{\mathrm{WT}}=\{$ dangerous, common, gentle $\} ;$
$S_{\mathrm{IOE}}=\{$ powerful, strong, middle, weak $\} ;$
$S_{\mathrm{RL}}=\{$ far, medium, near $\} ;$
$S_{\mathrm{FT}}=\{$ sudden flight, smooth flight $\}$.
As mentioned before, the weather conditions were divided into 3 levels. The levels were ranked as dangerous weather, common weather and mild weather in descending order of the threat level to the UAVs.

Four-level quantification was employed to identify the exact IOE of each weather type. The distance from the UAVs to the energy centre was also taken into account in the quantification process. Its effect on threat level was ascertained by three-level quantification.

Furthermore, the flight attitudes of UAVs were classified into two categories. The sudden flight operations pose a great threat to UAVs, while the smooth flight operations have a limited threat. For convenience, the flight attitudes were partitioned according to the possible directions.

## Determination of the CPT

The CPT was adopted to depict the casual relationship between the threat level in the DBN and the relevant factors. The table reflects the expert knowledge, including the experience and priori knowledge. Owing to subjectivity, there is a certain deviation between the expert knowledge and the actual results. If conditions permit, the CPT

should be modified to a certain extent. Table 1 shows the CPT of the factors in the weather threat assessment model.

Table 1. Conditional probability table of weather factors


In Table 1, the first column lists the conditional probabilities of the three weather types $(P(W T \mid T L))$, which are respectively $15 \%, 25 \%$ and $60 \%$ at low TL, $20 \%, 45 \%$ and 3 at medium TL, and $80 \%, 15 \%$ and $5 \%$ at high TL. The conditional probabilities of the other factors can be understood in a similar way.

# Determination of the TPT 

As shown in Table 2, the random probability refers to the state transition probability between two time slices when the network changes along the timeline.

Table 2. Transition probability table of DBN


## Results and discussion

The proposed DBN-based weather threat assessment model was applied to a simulation, aiming to infer the probabilities of different weather threat levels. Then, the weather threat levels were derived accurately, laying the basis for scientific route planning of UAVs.

Without any observational evidence, the high threat level $\left(P_{T L}^{H}\right)$, the medium threat level $\left(P_{T L}^{M}\right)$ ) and the low threat level $\left(P_{T L}^{L}\right)$ ) were assumed as $0.3,0.4$ and 0.3 , respectively. Suppose the nodes are mutually independent. Then, the author began to collect the data on each node. Assuming that a UAVs was on a mission, the weather conditions were monitoring at ten different moments of the flight, and the factors related to the threat of the target UAVs were described in real time.

Based on the observational evidence, ten observed values of the target were recorded (Table 3). The weather threat levels were figured out by comparing the data on the target UAVs at different moments. Next, the weather threat was assessed by the DBN and the ordinary Bayesian network (BN), respectively. The assessment results are presented in Table 4 and Figure 3. When the data were normal, both the DBN and the BN inferred the right results, despite a slight difference.

Table 3. Observation evidence table of UAVs at different time


Table 4. Simulation results of weather threat when data is normal


![img-2.jpeg](img-2.jpeg)

Figure 3. Assessment results of weather threat using DBN and BN

Sometimes, the data became abnormal due to measuring error or other reasons. Here, $P_{I o E}^{9}=(0.7,0.1,0.1,0.1)$ was changed to $P_{I o E}^{9}=(0.1,0.1,0.7,0.1)$, where $P_{I o E}^{9}$ is the observation probability of the IoE at time $t$. In this case, the assessment results are given in Table 5 and Figure 4.

Table 5. Simulation results of weather threat using DBN and BN when abnormal data occurred


![img-3.jpeg](img-3.jpeg)

Figure 4. Assessment results of weather threat when abnormal data occurred

As shown in Figure 4, the DBN managed to infer the weather threat correctly before and after the abnormal data occurred at time 9 , although the states of weather factors changed over time and the threat levels were unclear according to the reference tables. By contrast, the BN only derived the right results based on the current data. Therefore, the DBN is much more accurate than the BN in the inference of weather threat level, in spite of the alteration or missing of the feature values.

# Conclusions 

This paper puts forward a weather treat assessment model based on the DBN, and determines the probability distribution of weather threat level by the HMM inference

method. The model considers all the key factors affecting the weather threat level, including some continuous observed data. Through the numerical simulation of UAVs flight, it is concluded that the DBN-based model is effective and feasible. The model has a great potential of application in fields like battlefield situation assessment, target recognition, etc. In the next step, it is proposed to automatically construct a meteorological threat assessment model through Bayesian learning method, which makes the constructed model more reasonable and accurate, and applies the weather threat assessment results to multi-UAV multi-target mission planning.
