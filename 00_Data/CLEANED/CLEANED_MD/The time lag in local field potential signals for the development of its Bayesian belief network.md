# The time lag in local field potential signals for the development of its Bayesian belief network 

Victor H. B. Tsukahara ${ }^{1 *}$, Jordão N. O. Junior ${ }^{1 \dagger}$, Tamiris Prizon ${ }^{2 \dagger}$, Rafael N. Ruggiero ${ }^{2 \dagger}$ and Carlos D. Maciel ${ }^{1 \dagger}$<br>${ }^{1}$ These authors contributed equally to this work.<br>*Correspondence:<br>vhbtsukahara@alumni.usp.br<br>${ }^{1}$ Signal Processing Laboratory, Department of Electrical and Computing Engineering, School of engineering of São Carlos, University of São Paulo (USP), Trabalhador São Carlense Avenue, 400, São Carlos 13566-590, São Paulo, Brasil<br>${ }^{2}$ Department of Neuroscience and Behavioral Sciences, Ribeirão Preto School of Medicine, University of São Paulo (USP), Banderiantes Avenue, 3900, Ribeirão Preto 14049-900, São Paulo, Brasil


#### Abstract

Purpose: The objective is to suggest time as an important variable to consider in the network model, specifically when discussing causality. Methods: There is a consideration of the context of functional connectivity because of the time importance of observing the feature inside the neuroscience context. A network model was constructed using the Bayesian network method, utilizing a dataset consisting of three rats' local field potentials. The model took into consideration the time delay of communication among brain areas, as recorded in this study. In pursuit of this objective, the delayed mutual information method was employed to ascertain the temporal delay between local field potentials and K2 score for the purpose of model comparison. Results: Bayesian network depicted the probabilistic relationship among rat's brain areas. Delayed mutual information captured the lag among brain areas, and after its appliance on the Bayesian network model, posed better results. Conclusion: The primary novelty of this research lies in its integration of minor delays within the Bayesian network approach, accomplished through the utilization of the delayed mutual information technique prior to its implementation. The suggested methodology incorporates an essential feature that supports the analysis of functional connectivity among brain areas, thereby providing support for the dynamics of neurophysiology.


Keywords: Local field potential, Time lag, Time series analysis, Temporal synchronization, Bayesian network, Neuroinformatics, Computational modeling, Information flow, Information theory, Mutual information

## 1 Introduction

The brain is an intricate network of nonlinear interactions among neuron populations originating from different regions of this organ [1, 2]. It is a complex system with emergent properties [3, 4], such as dynamic memory [5-7], creative thinking [8-10], behavior [11], and brain disorders [12-14]. A comprehensive examination of the spatiotemporal attributes of brain disorders and their functional connectivity analysis is of utmost importance to facilitate more comprehensive investigations. This is because the

Springer Open

[^0]
[^0]:    (c) The Author(s) 2024. Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/.

observed patterns of brain communication during a neurological disturbance diverge from the connections of healthy brains [15].

Synchronization of the brain network, a modern concept used to illuminate the healthy and pathological functioning of the brain [13], what differs the condition is the proper coordination in time of the states of the brain network, as well as the dynamics of its elementary units, the neurons [16]. Synchronized neural oscillations enable efficient communication and integration of information across different brain regions through mechanisms like phase-locking and coherence. Studies have emphasized the importance of neural synchrony in various cognitive processes such as attention, memory, and sensory processing [17]. Abnormal synchronization patterns have been linked to neuropsychiatric conditions like schizophrenia and epilepsy, highlighting the importance of comprehending the principles that control brain network synchronization [18, 19]. Understanding the mechanisms that cause synchronization between different brain regions is essential for uncovering the intricacies of brain function and treating neurological and psychiatric disorders.

Additionally to this upward trend, it is imperative to acknowledge that the communication between different brain regions entails a certain degree of temporal delay [20]. This delay plays a crucial role in preserving the synchronization of the brain's healthy or pathological networks [21]. The time delay is a characteristic of realistic systems such as human or animal physiology that is inherent in them [22].

Comprehending the temporal dynamics and time delays among various brain regions is crucial for revealing the mechanisms implicated in the processing and integrating of information within the brain. Temporal delays in neural communication can offer knowledge of brain networks' hierarchical structure and functional interconnections. Advanced techniques such as magnetoencephalography (MEG), electroencephalography (EEG), and functional magnetic resonance imaging (fMRI) along with effective connectivity measures such as dynamic causal modeling (DCM) and Granger causality analysis have been crucial in studying how neural signals move and the time delays between different brain areas [23-26]. These methods allow researchers to deduce the direction of influences and measure the timing of neural interactions within widespread brain networks. Computational modeling methods such as neural mass models and neural network simulations offer theoretical structures to study how time delays affect network dynamics and cognitive function [27, 28]. Researchers can thoroughly comprehend the spatial and temporal arrangement of brain activity and its functional importance in cognition and behavior by combining multi-modal imaging and computational modeling.

Important studies in the literature make use of Bayesian networks (BNs). In their study, Tsukahara et al. [29] employed Bayesian networks to simulate local field potentials (LFPs) recordings of rats that were induced with epilepsy. The researchers also assessed the arcs of these recordings using an analytical threshold approach. In their recent study, Sip et al. [30] proposed a data-driven approach that utilizes Bayesian inference to deduce seizure propagation patterns in an epileptic brain using intracranial electroencephalography. In their study, Van Esch et al. [31] employed the Bayesian approach to assess the efficacy of brain network connectivity in detecting the Mozart effect. In a study conducted by Eldawlatly et al. [32], the objective was to investigate the dynamic connectivity among cortical neurons. Smith et al. [33] deduced nonlinear connections

in communication between different regions of the brain. In their study, De Blasi et al. [34] employed the glsBN method to forecast associations with organ failure in situations where predefined outcomes were unavailable. In their study, Ruiz et al. [35] employed the GLSL-BN model to examine the correlation between various neuromuscular performance parameters and dynamic postural control techniques. The models GLS-BN are probabilistic; the system consists of a directed acyclic graph (DAG) and conditional probability tables (CPTs) representing the probabilistic relationship between signals.

The paper proposes the utilization of delayed mutual information (DMI) within the glsBN method to account for the minor temporal delays between brain regions. This is because information theoretical approaches do not make any assumptions regarding the interdependence of time series [36]. This paper hypothesizes that by replicating the delays observed in the brain, we can develop a more accurate model for a Bayesian network. The method's strength lies in its utilization of a nonparametric approach, which enables the measurement of generalized interdependence between two variables, encompassing both linear and nonlinear relationships [37]. According to WAN [38], it is widely acknowledged that real-world time series typically exhibit nonlinearity and nonstationarity. The proposed methodology integrates the Bayesian network approach with the delayed mutual information technique to construct a network model using a dataset comprising the local field potentials of rats. The functional connectivity analysis examines the impact of slight delays on model results by considering six brain areas: dorsal hippocampus (glsdHp), ventral hippocampus (glsvHp), striate (glss), prefrontal cortex (glsPfc), thalamus (glsTh), and ventral tegmental area (glsVTA). This study's primary contribution is the integration of minor delays within the GLSS-BN model. The neurophysiology of brain dynamics is substantiated by including a crucial aspect of the proposed methodology for examining the temporal progression of brain communication.

# 2 Theory 

### 2.1 Delayed mutual information

The deterministic nature of a given variable can be assessed by its entropy $(H)$, which is defined as [39]:

$$
H(X)=-\sum_{x \in X} p(x) \log _{a} p(x)
$$

Let $X$ denote a discrete random variable. The function $p(x)=P(X=x)$ represents the probability of $X$ being equal to $x$, where $x$ is a probability mass function of $X$. The logarithm base $a$ is used to calculate the entropy measure in bits, assuming $a=2$. The mutual information can be used to quantify the amount of information shared between two signals modeled as random variables, namely signal $X$ and signal $Y$. It quantifies the extent to which the uncertainty of signal $X$ can be reduced based on the knowledge of signal $Y[39]$.

The concept of delayed mutual information (DMI), as defined by NICHOLS [40], refers to the measurement of the amount of information that is shared between two variables $X$ and $Y_{\tau}$, where $Y_{\tau}$ represents the signal that has been displaced by a lag $\tau$. According to Cover [39], it is defined as:

$$
I\left(X ; Y^{\tau}\right)=\sum_{x_{n} \in \mathcal{X}} \sum_{y^{\tau} \in \gamma^{\tau}} p\left(x_{n}, y_{y-\tau}\right) \log _{a} \frac{p\left(x_{n}, y_{n-\tau}\right)}{p\left(x_{n}\right) p\left(y_{n-\tau}\right)}
$$

According to [39], the maximum measure of mutual information is defined as the channel capacity $(\mathrm{C})$ :

$$
C=\max I(X, Y)
$$

The channel capacity is used to determine the delay between temporal signals, with the interval where the maximum channel capacity is observed being the value of the delay to be considered in the analysis.

# 2.2 Bayesian networks 

Let $G=(V, E)$ be a directed acyclic graph (DAG) with vertices $V$ and edges $E$. If each $X_{1}, X_{2}, \ldots, X_{n}$ represents a random variable, $X_{a} \rightarrow X_{b}$ (meaning that $X_{a}$ is a parent of $X_{b}$ or $X_{b}$ is a descendent from $X_{a}$ ) implies that there is statistical dependence between $X_{a}$ and $X_{b}$. A Bayesian network $B=(G, \Theta)$ is represented by a pair $G$ and the set of conditional dependence $\Theta=\left\{\theta_{1}, \theta_{2}, \ldots, \theta_{n}\right\}$ and $G$ obeys the Markov Condition $X \Perp N D_{X} \mid \mathrm{PA}_{X}$, for each $X \in V$ in which $N D_{X}$ represents the set of all vertices nondescendent from $X$ and $P A_{X}$ represents the parents of $X$. The joint probability function for any BN with joint distribution $P$ and vertices $V$ on the set of random variables $X_{1}, X_{2}, \ldots, X_{n}$ can be defined as

$$
P=\prod_{x \in\{X\}} p\left(x \mid \mathrm{PA}_{X}\right)
$$

Finding the BN that best fits the data is usually comprised of two parts: a scoring function to evaluate the likelihood of a certain DAG against the data and a search method to find possible DAGs. The maximum a posterior (MAP) probability of $B$ given the data $y_{\lambda}[T]$, where $T$ is the time window of the local field potential under analysis [41]:

$$
P\left(y_{\lambda}[T] \mid G\right)=\int_{\Theta} P\left(y_{\lambda}[T] \mid G, \Theta\right) P(\Theta \mid G) d \Theta
$$

Bayesian networks assume that the conditional distribution of Directed Acyclic Graphs (DAGs) follows a Dirichlet distribution, as it offers mathematical convenience and suitability. The Dirichlet distribution serves as the conjugate prior for categorical and multinomial distributions, thereby simplifying computations by guaranteeing that the posterior distribution remains Dirichlet. The flexibility of this model enables the representation of a diverse set of probability distributions that add up to one. The parameters of the model can be understood as prior counts, which enhances the intuitiveness of prior beliefs. Moreover, its uncomplicated structure and easily comprehensible characteristics facilitate the process of drawing conclusions and acquiring knowledge, fitting seamlessly within the Bayesian framework. Assuming $P(\Theta \mid G) \mathrm{P}(\Theta \mid G)$ is a Dirichlet distribution [41, 42] defines the Bayesian-Dirichlet score, Bayesian Dirichlet (BD):

$$
B D=\log \prod_{i=1}^{n} \prod_{j=1}^{q_{i}} \frac{\Gamma\left(N_{i j}^{\prime}\right)}{\Gamma\left(N_{i j}^{\prime}+N_{i j}\right)} \prod_{k=1}^{r_{i}} \frac{\Gamma\left(N_{i j k}^{\prime}+N_{i j k}\right)}{\Gamma\left(N_{i j k}^{\prime}\right)}
$$

Let $n$ represent the total number of nodes, $r_{i}$ represent the number of states of node $i$, and $q_{i}$ represent the number of possible instances of the parents of node $i$. The symbol $\Gamma(\cdot)$ denotes the Gamma function. The variable $N_{i j k}$ represents the frequency of $x_{i}$, taking the value $k$ given the parent configuration $j$. The equation $N_{i j}=\sum_{k=1}^{r_{i}} N_{i j k}$ and $N_{i j}^{\prime}=\sum_{k=1}^{r_{i}} N_{i j k}^{\prime}$ can express these values. Including the quantization level of the variables, denoted as $r$, within a product implies that a sufficiently high quantization level may significantly increase the cost of the learning method. Nevertheless, if the quantization is insufficient, the distinct dataset will forfeit its characteristics and modify its behavior, leading to an erroneous directed acyclic graph (DAG) being assumed to be the optimal Graph Linked Support Network (BN) for the original data. Multiple iterations of the BD score exist, including the BDe and BDeu scores [41]. However, for this study, the K2 score will be employed; this score is obtained by setting all Dirichlet hyperparameters to 1 , resulting in a Bayesian score [43]

$$
K 2\left(y_{i}[T] \mid G\right)=\log \prod_{i=1}^{n} \prod_{j=1}^{q_{i}} \frac{\left(r_{i}-1\right)!}{\left(N_{i j}+r_{i}-1\right)!} \prod_{k=1}^{r_{i}} N_{i j k}!
$$

It is important to notice that the directed edges from the BN represent statistical dependencies between the variables and are obtained from the data; they do not necessarily represent causality relationships [44]. In general, to obtain causality corrections from the BN structure, it is necessary to have a specialist's knowledge [45].

# 3 Methodology 

### 3.1 Experimental protocol

The current experimental protocols involving rats are expounded upon in greater depth in de Oliveira-Junior et al. [46], Ruggiero et al. [47]. The open field test assesses the rats' exploratory behavior and locomotion over 30 min . Each rat is individually placed in the center of an acrylic apparatus measuring $46 \times 46 \times 46 \mathrm{~cm}$ (height $\times$ width $\times$ length), and movements are recorded using a webcam connected to a computer. The animals scrutinize freely, with exploratory behavior evaluated through rearing and locomotion assessed by distance traveled and speed [46, 47].
Intracranial electroencephalography signals are collected at a frequency of 10 kHz , through electrodes implanted directly in the following areas of the rat brain, during the open field test: Dorsal Hippocampus (dHp), Prefrontal Cortex (Pfc), Striate (s), Thalamus (Th), Ventral Hippocampus (vHp) and Ventral Tegmental Area (VTA). For each acquisition, approximately 8 million samples are collected for each brain area mapped in the study (approximately 13 min of acquisition)

### 3.2 Algorithms

Figure 1 presents the flowchart illustrating the summarized methodology. Initially, the dataset is divided into 100 smaller datasets, each containing 100,000 samples

![img-0.jpeg](img-0.jpeg)

**Fig. 1** Methodological summary: first, the local field potentials are acquired from 3 rats, using 10 kHz frequency of sampling [frequency of sampling (fz)]. After each rat acquisition, a dataframe with 6 columns is created. The next step is the BN method appliance, and a consolidated BN is created based on the analytical threshold method, obtaining its K2 score. The DMI method is applied to discover the lag among brain areas. After the lag consolidation, the BN method is applied to obtain a consolidated BN using the analytical threshold method again. The K2 score was obtained to compare with the previous results.

and 6 columns (dHp, Pfc, s, Th, vHp, and VTA). An algorithm is utilized to collect the data points, randomly sampling the data at various points during the experiment recording—Fig. 3.

The relationships between the chosen variables were determined using a quantitative approach that relied on graphical and nonparametric methods. A BN structure represented the functional connectivity networks among brain areas learned from the discretized dataset. In the study by Gencaga et al. [48], a quantization technique was implemented, followed by the adaptive bins algorithm using a maximum of 32 bins (5 bits) to keep the best tradeoff between resolution and computational time, previously tested with similar time series and published by Signal Processing Laboratory of University of São Paulo [49]. The hill climbing search algorithm, implemented in the Python package *pgmpy*,[1] was utilized to acquire knowledge of the directed acyclic graph (DAG) from the dataset. The BDeu function was employed as a scoring method, as the task may be intricate or even unattainable for humans [50].

The experiment consists of a collection of *K* = 100 directed acyclic graphs (DAGs) constructed through the iterative execution of the hill climbing search algorithm. Each run utilizes distinct data from one of the rats in this preclinical study. The fundamental concept is a reduced ambiguity concerning the formed arcs, even when gathering data from a distinct animal. The wide range of structures observed can be attributed to using data from various rats within the same species, with typically assigned precise weights. Additionally, the hill climbing search process, when initialized randomly and subjected to local optimizations during a run, exhibits non-deterministic characteristics. By the stop criterion, the hill climbing search algorithm undergoes one million iterations for

<sup>1</sup> https://pgmpy.org/.

![img-1.jpeg](img-1.jpeg)

Fig. 2 The analysis of lag. The Thalamus, denoted as Th, serves as a reference point for determining the sample delay characteristic of LFP signals. According to the DMI analysis, the dHp, Pfc, s, vHp, and VTA LFP signals of $\boldsymbol{\tau}_{1}$ and $\boldsymbol{\tau}_{2}$ are being replaced in samples. This study employs a repetitive process for each time slice and rat data. Dataframe preparation is conducted before the application of the BN method

Each complete run. Subsequently, the collection of directed acyclic graphs (DAGs) was condensed into a solitary consensus DAG using a technique known as the model-averaging approach. This reduction involves calculating the frequency of each of the three potential connections (i.e., " $\leftarrow$ ", " $\rightarrow$ ", and "absent") by examining every pair of nodes in the 100 graphs obtained. Accepted were only directed arcs that met the minimum percentage (f) as defined by the equation $f=(1 / 3)+\sqrt{2 / K}$. The analytical threshold model, as proposed by Gross [51] and extensively described in Gross [52], was utilized to assess the arcs. Additionally, a specialist analysis was conducted during the final evaluation of the network, but only the edges derived from the analytical threshold analysis were considered.

The K2 score is calculated for the resulting BN to facilitate further comparison. The brain areas were represented using a BN structure learned from the discretized dataset. The hill climbing search algorithm in Python is employed to acquire knowledge of the directed acyclic graph (DAG) from the dataset. K2 is utilized as a scoring method due to its high efficacy as a Bayesian network learning algorithm [53]. Additionally, the K2 score can be generalized. The term "Bayesian Dirichlet equivalence with a uniform prior metric, BDeu" refers to the Bayesian Dirichlet function used as the scoring function to determine the optimal Bayesian network (BN). The BDeu algorithm assigns equal scores to directed acyclic graphs (DAGs), which possess identical conditional independencies, thereby establishing their Markov-equivalent nature [54]. BDeu's performance may encounter difficulties in scenarios with many dimensions, such as when dealing with multivariate nonstationary time series [55]. Two additional frequently employed scoring methods include the utilization of Akaike information criteria (AIC) and Bayesian information criteria (BIC) [56–58]. There are, however, apprehensions regarding the evaluation methodology, particularly the utilization of the asymptotic theory [59] for the calculation of both criteria.

Subsequently, the delayed mutual information technique was employed to examine the delay between different brain regions. The Thalamus brain region is a benchmark for determining the temporal delay between the LFP signals. In Fig. 2, the same 100 datasets used in developing the Bayesian networks without delay were employed to calculate the

# 1. LFP acquistion 

![img-2.jpeg](img-2.jpeg)

The LFP signals are recorded during the execution of an open-field test with rats. Brain areas: $\mathrm{dHp}, \mathrm{vHp}, \mathrm{Pfc}, \mathrm{s}, \mathrm{Th}, \mathrm{VTA}$.
![img-3.jpeg](img-3.jpeg)

Local Field Potential timeseries are discretized using 32 bins. Signal acquisition at a frequency of 10 kHz , utilizing 3 rats. For each acquisition, approximately 8 million samples are collected for each brain area mapped in the study. The dataset is divided into 100 smaller datasets, each containing 100,000 samples and 6 columns (dHp, vHp, Pfc, s, Th, and VTA).

Fig. 3 In the applied methodology, the initial two steps are as follows: The acquisition of local field potentials is initially conducted on three rats, encompassing five distinct brain regions-dHp, Pfc, s, Th, vHp, and VTA, using a sampling frequency of 10 kHz . After that, time series discretization using 32 bins is divided into 100 smaller datasets, each containing 100,000 samples

![img-4.jpeg](img-4.jpeg)

Fig. 4 (1) The method uses all the dataframes from the three rats to develop the resulting BN without considering lag among brain areas. (2) The analytical threshold method evaluates the edges and provides a final Bayesian network. K2 score is then calculated for that structure. (3) The lag study among rats' brain areas uses delayed mutual information. The consolidated lags were used in the Bayesian network (BN) structure for each dataset. The analytical threshold method is again employed to assess the edges and generate a conclusive Bayesian network. The K2 score is subsequently computed for the given structure. The objective is to examine the BN that exhibits the most optimal fit.

DMI between the brain areas involved in the experiment. The results obtained through the application of DMI were statistically tested to validate them before considering the delay between signals for developing Bayesian networks.

A collection of K = 100 directed acyclic graphs (DAGs) was constructed by iteratively executing the hill climbing search algorithm a hundred times. Subsequently, employing the described methodology, the collection of directed acyclic graphs (DAGs) was condensed into a solitary consensus DAG using a model-averaging technique as outlined by Gross et al. (2019)—Fig. 4. The K2 score is calculated for the resulting BN to compare with previous results. Compiling each rat database, which consisted of five local field potential time series and totaled around 100,000 samples, required approximately 12 min, including the generation of BNs and preprocessing.

![img-5.jpeg](img-5.jpeg)

Fig. 5 Pareto chart for each result, considering (b) or not (a) the lag among brain areas. It is important to observe the analytical threshold of 40%, indicating the probabilistic relationships considered in the final Bayesian network for each case.

![img-6.jpeg](img-6.jpeg)

Fig. 6 Example of autocorrelation calculated for DMI results. Observe that variance is not constant over the sample lag, and the mean of the DMI results is not zero. Both results conclude that results are not Gaussian or random walk noise
which was found using a 1 TB RAM and 32-core/128-thread @2.70GHz POWER9-2.2 computer with a NVidia Tesla V100 SXM2 16GB GPU. Therefore, the total time spent processing all databases comprising 3 rats $(\mathrm{K}=100$ for each rat) was about 360 min .

# 4 Results 

Based not on the number of datasets created $(K=100)$, the analytical threshold resulted in a value of $0.40(40 \%)$. The Pareto chart with the frequency of edges resulting from applying the BN method can be observed in Fig. 5a. Figure 7a depicts the consolidated BN without the lag consideration.
After the BN and analytical threshold method were applied, without lag consideration, the DMI method was utilized to examine the temporal delay among brain regions to be considered within the model. Table 1 represents the median of the observed lags.
A statistical analysis was used to verify the DMI and observe the normality of the lag results. The Durbin-Watson test for heteroscedasticity yielded a statistically significant result of 2.76, while the Anderson-Darling test for normality yielded a statistically significant result of 3.60 . The critical values for each significance level are as follows:
significance level: 0.55 for $15.00 \%, 0.63$ for $10.00 \%, 0.76$ for $5.00 \%, 0.89$ for $2.50 \%$ and 1.05 for $1.00 \%$. Figure 6 shows an example of the autocorrelation calculated for DMI results. The mean of the DMI results is not zero, and the variance is not constant and different from zero. It is possible to observe that there is an autocorrelation among the results.
After validating the DMI results, the BN method was applied again, considering the lag among brain areas-the median of the lag observed for each brain area, considering the Th as reference. Figure 5b depicts the Pareto chart of the observed edges. Figure 7b presents the consolidated BN using the analytical threshold.

Table 1 The median of the lag observed for each rat (ELS 11, ELS 12, and ELS13)


Each rat originated 100 dataframes comprising 6 columns. DMI was applied for each dataframe, and the lag was consolidated to consider it inside the BN method
![img-7.jpeg](img-7.jpeg)

Fig. 7 The directed acyclic graph obtained considering the lag among local field potential time series and using the raw signal, without any delay. There is biologically a substantial difference in the probabilistic relationship between rat brain areas

The K2 score observed for the consolidated BN without lag was - 98,222.96. Considering the lag, the K2 scores observed was - 100,376.71.

# 5 Discussion 

### 5.1 Biological analysis

The results from both directed acyclic graphs (DAGs), whether with or without delay, highlight the connectivity between cortical and subcortical regions with the ventral tegmental area (VTA) during exploratory behavior and locomotion. Indeed, the VTA exhibits heightened activation in goal-directed behaviors, contributing to motivation, learning and memory, behavioral activation, and salience detection [60, 61].
The striatum is crucial in the basal ganglia associated with motor functions and a broad spectrum of goal-directed behaviors [62]. It is anticipated to be a key region involved in the exploratory behavior examined in this study. Its primary outputs extend to the ventral pallidum, the medial dorsal nucleus of the thalamus, as well as the globus

pallidus and substantia nigra pars reticulata (SNr) [62]. The proximity of the substantia nigra to the ventral tegmental area (VTA) emphasizes its central role in the broader neural network regulating diverse behaviors. It justifies the DAG connectivity from the Striatum to the VTA.

Furthermore, the prefrontal cortex (PFC) and the hippocampus (HPC) play pivotal roles in modulating VTA function during motivated behavior, with the activity in the PFC and HPC predicting VTA responses (Murty et al., 2017). Polysynaptic pathways connecting the hippocampus and VTA have been delineated [63, 64]. Conversely, the PFC sends direct excitatory projections to the VTA, regulating the activity of VTA neurons and extracellular dopamine (DA) levels within forebrain regions [65, 66].

The literature data strongly support the proposed directed acyclic graph (DAG) for both networks, emphasizing the influential roles of the PFC, HPC, and striatum in shaping VTA activity. However, a notable feature in the delayed network is the emergence of unique connectivity between the PFC and the midline thalamic nucleus-a phenomenon absent in the DAG without delay.

Neurobiological data support the connectivity presented in the network with delay. The PFC exhibits bidirectional connections with thalamic afferents [67, 68], particularly demonstrating dense reciprocal connectivity with the mediodorsal (MD) region. These reciprocal interactions play a pivotal role in cognition, with the PFC strongly influencing neuronal activity in the thalamus [69]. Given the significance of these dynamic interactions in shaping cognitive processes, it becomes apparent that the delayed network offers a more comprehensive explanation of the neurobiological processes underlying the analyzed exploratory behavior.

Similarly, the CA1 and subiculum regions of the HPC project to the Reuniens nucleus of the thalamus, which, in turn, projects back to the HPC [70]. This emphasizes the crucial role of the ventral midline thalamus in establishing a bidirectional connection between the HPC and the PFC, governing cognitive processes and emotional regulation [47, 70]. These findings are further confirmed in the DAGs, demonstrating the influence of the ventral HPC on thalamic activity and affirming the validity of our network.

# 5.2 The delayed mutual information and Bayesian belief network 

According to Krubitzer [71], rats of the same species with similar weights may exhibit physiological differences when subjected to the same experimental protocol. The veracity of this statement can be verified by examining the outcomes of the BN methodology employed to construct the database of rats. Figure 5 presents a Pareto chart illustrating the range of edges generated by the BN methodology appliance. This chart utilizes dataframes from the same rat and different rat periods. The superexponential increase in the quantity of potential directed acyclic graphs (DAGs) relative to the number of vertices suggests that conducting a thorough search is unattainable. Multiple methodologies exist to achieve a satisfactory alignment with the data. The hill climbing algorithm's state-space exhibits diverse outcomes due to its probabilistic nature. Both issues guarantee the expected variability of the obtained results.

Utilizing delayed mutual information to examine the delay between recorded brain regions of rats appeared to be a viable alternative. The local field potentials of animals

exhibit characteristics such as kurtosis, nonlinearity, and heteroskedasticity, which aligns with the understanding that real-world problems are characterized by nonlinearity. The method can handle signals, allowing communication delays between different brain regions.

The findings of the DMI model exhibited a departure from a normal distribution, suggesting that the lag does not conform to Gaussian or random walk noise. The AndersonDarling normality test further supported the results, which yielded a $p$ value of $5 \%$.

The inclusion of communication delay between brain areas in the development of the BN method is documented in Table 1, which presents the lag observed in the time series obtained through this approach. The BN without any lag had a K2 score of - 98,222.96. The observed K2 scores were - 100,376.71, taking into account the lag. Upon comparing the results, it is evident that incorporating lag consideration within the BN model enhanced the fit with the dataframes, resulting in a notable difference of $5 \%$. As previously mentioned, Fig. 7b is more biologically logical than Fig. 7a.

It is important to indicate that, even when dealing with the same type of animal from the same species to perform the experiments, they are physiologically distinct [71]. Additionally, experiments to collect intracranial electroencephalography signals need substantial financial investments and, in addition to the required resources, demand refined techniques for animal preparation, electrode positioning, and inherent issues involving the animals themselves, such as movement artifacts. All these points are also challenges when conducting this type of study. Therefore, Table 1 presents distinct values for the delays among different brain areas. We must consider all the described factors for interpreting the encountered values, influencing the variability of the measurements obtained with the DMI method.

Once more, the incorporation of communication delay between different regions yielded a model that exhibited superior fit compared to the BN model lacking communication lag. The findings support previous research indicating that there is a delay in communication between different regions of the brain [20], and this delay affects the synchronization of brain networks [21].

The involvement of a neuroscience expert in interpreting the BN models was crucial in transferring the probabilistic relationships obtained from the method to causal analysis of brain dynamics. It is crucial to remember that the Bayesian network (BN) method offers probabilistic relationships between variables, necessitating the evaluation of the resulting associations. Overall, the findings are consistent with the existing body of neuroscience research. Nevertheless, it is imperative to take into account certain concerns.

# 6 Conclusion 

The Bayesian network method is a cost-effective approach that provides valuable insights into the dynamics of brain communication. Delayed mutual information refers to the temporal delay in communication between various brain regions in rats, including the prefrontal cortex, dorsal and ventral hippocampus, striate, thalamus, and ventral tegmental area. By integrating the delay component into the Bayesian network model, notable enhancements were observed in the outcomes. The verification of this assertion was derived from the computed K2 scores for the constructed Bayesian networks, both with and without the inclusion of lag outcomes. As outlined in the results section, the

optimal Bayesian network model aligns with the existing body of neuroscience literature and offers recommendations for future comprehensive investigations. Hence, integrating both approaches presented a viable alternative for conducting functional connectivity analysis within the research framework involving LFP recordings.

We would like to acknowledge the contributions of our laboratory colleagues, whose constructive discussions and suggestions enriched this work.

VHBT and JNOJ designed, drafted, and revised the manuscript. TP performed the data acquisition and experiments. RNR supervised data acquisition and experiments and designed, drafted, and revised the manuscript. CDM designed, drafted, and revised the manuscript. No undisclosed groups were involved in this study. All co-authors have seen and approved the submitted version of the paper and accepted responsibility for its content.

This work was partially supported by the following agencies: FAPESP 2014/50851-0 and BPE FAPESP 2018/19150-6.

The raw data supporting the conclusions of this article will be made available by the authors upon request, without undue reservation.

The authors declare that the research was conducted without any commercial or financial relationships that could potentially create a conflict of interest.

Received: 28 February 2024 Accepted: 11 June 2024
Published online: 27 September 2024

## Publisher's Note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.