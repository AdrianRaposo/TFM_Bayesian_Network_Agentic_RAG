# A Hierarchical Bayesian Model for Crowd Emotions 

Oscar J. Urizar ${ }^{1 *}$, Mirza S. Baig ${ }^{2}$, Emilia I. Barakova ${ }^{1}$, Carlo S. Regazzoni ${ }^{2}$, Lucio Marcenaro ${ }^{2}$ and Matthias Rauterberg ${ }^{1}$<br>${ }^{1}$ Department of Industrial Design, Eindhoven University of Technology, Eindhoven, Netherlands, ${ }^{2}$ Department of Naval, Electric, Electronic, and Telecommunications Engineering, University of Genova, Genoa, Italy

Estimation of emotions is an essential aspect in developing intelligent systems intended for crowded environments. However, emotion estimation in crowds remains a challenging problem due to the complexity in which human emotions are manifested and the capability of a system to perceive them in such conditions. This paper proposes a hierarchical Bayesian model to learn in unsupervised manner the behavior of individuals and of the crowd as a single entity, and explore the relation between behavior and emotions to infer emotional states. Information about the motion patterns of individuals are described using a self-organizing map, and a hierarchical Bayesian network builds probabilistic models to identify behaviors and infer the emotional state of individuals and the crowd. This model is trained and tested using data produced from simulated scenarios that resemble real-life environments. The conducted experiments tested the efficiency of our method to learn, detect and associate behaviors with emotional states yielding accuracy levels of $74 \%$ for individuals and $81 \%$ for the crowd, similar in performance with existing methods for pedestrian behavior detection but with novel concepts regarding the analysis of crowds.

Keywords: crowd behavior, emotion estimation in crowds, estimation of individual and collective emotions

## 1. INTRODUCTION

The tendency of the urban development toward Smart cities (Chourabi et al., 2012) poses a number of research and engineering challenges among which crowd emotion management and prevention of escalations is of vital importance. Furthermore, with the fast growth of population in urban areas around the world, the phenomenon of crowds is set to become commonplace in the near future. The purpose of this work is to present an approach for estimating emotions of single individuals and of a crowd as a whole. In this work, we use the working definition of the crowd as a group of people in proximity, where a common motivation or set of emotions may exist as in the case of sports events and concerts, or merely individuals with different motivations and emotions walking around a busy area. In both instances, the term crowd behavior refers to the behavior adopted by individuals when becoming part of a crowd.

Research on crowd emotions differs significantly from the research on individual emotions in several ways. de Gelder (2006) and Huis in 't Veld and De Gelder (2015) propose that crowd emotions are a delicate balance between the emotions of the individuals and the emotions of the crowd. They found that the interactive or panicked crowds, as opposed to the individually fearful crowds, triggered more anticipatory and preparation action activity, whereas the brain was less sensitive to the dynamics of individuals in a happy or neutral crowd.

Despite the dissimilarities among the most prominent theories addressing crowds from psychologists and sociologist such as Le Bon (2001), Freud (1921), and Allett (1996) among others, there is a consensus on the important role of emotions in the phenomenon of crowd behavior (Challenger et al., 2009). Emotions can be thought as manifestations of our internal state of well-being utilizing psychophysiological and behavioral reactions. In more practical terms, emotions serve as a response to internal or external events experienced by a subject and are manifested over brief periods of time (Plutchik, 2011). Also, supported by the work done by Matsumoto (2004), Ekman et al. (1987) and Keltner and Ekman (2000) we have learn that emotions are discrete and measurable, also that certain emotions appear to be universally recognized despite cultural context or learned associations.

The use of facial and vocal expressions to infer emotions becomes unfeasible in crowded environments. Hence, in this work we propose the use of behaviors described as motion patterns to identify emotional states. This approach is supported by de Gelder et al. (2010), Van den Stock (2007) and Frijda (2010) where they suggest that the whole body expressions of emotion are primary carriers of emotion and action information and may thus play a more important role in a crowd situation than facial expressions. Emotions expressed by dancers and music instrument players have been simulated on robot agents by Barakova and Lourens (2010). The relationship between emotional states and behaviors is further supported by Damasio's Somatic Marker hypothesis (Bechara and Damasio, 2005) in which he explains that decision making involves both cognitive and emotional processes. However, it is important to point out that the relationship between emotions and behaviors is not straightforward as shown in appraisal theory (Moors et al., 2013) proposed by Arnold and developed Lazarus to explain how the same event can provoke different emotions in different individuals and occasions. Moreover, the contemporary appraisal theories define emotions as processes rather than states (Moors et al., 2013), which is in line with the modeling of the movement behavior of the individuals in the crowd.

The work presented in this paper proposes a hierarchical Bayesian model suited for crowded environments. Our model is capable to learn behaviors and associate them with emotions during the training phase, and to estimate emotional states based on partial observations of behaviors during the testing phase; we apply this for both the individuals in the crowd and the crowd as a whole. We consider two types of entities, namely the individual and the crowd. The entity individual describes the behavior and associated emotion of individual people walking across the observed environment. Hence, an instance of entity individual is implemented for each pedestrian detected. The entity crowd describes the whole congregation of people as a single being subjected to the laws of mental unity as explained in Le Bon (2001), hence having its own behavior and associated emotional state. In this work, we limit to describe emotional states in one dimension, ranging from positive to negative according to the principle of valence (Rosenhan and Messick, 1966).

In the proposed approach, the topology of an environment is learned from observed trajectories of individuals employing a
self-organizing map $\mathrm{SOM}_{I}$, where each node of $\mathrm{SOM}_{I}$ represents a mutually exclusive zone. The path of individuals is expressed as a sequence of transitions among these zones, and a hierarchical Bayesian network builds probabilistic models to describe and group similar behaviors. The learned behaviors are associated with certain emotional states in an empirical fashion. We describe the configuration of the crowd in a given instant with a state vector containing the estimated density level in each zone of the environment. Employing a second self-organizing map $\mathrm{SOM}_{C}$ we cluster similar configurations of the crowd into a node of $\mathrm{SOM}_{C}$, enabling us to describe the behavior of a crowd as a transition of nodes of $\mathrm{SOM}_{C}$ using a similar hierarchical Bayesian network. The proposed hierarchical Bayesian model is presented in Figure 1. Finally, the emotional states are associated to crowd behaviors in an empirical way. The association between behaviors and emotions is done empirically because the interpretation of a behavior greatly depends on the context of the environment, for example, a fast-paced walk with sudden turns during rush-hour in a train station could have a different emotion associated if the same behavior was displayed in a museum.

The remaining of this work is organized as follow: Section 2 presents a brief survey of previous approaches to estimate emotions. A comprehensive description of our proposed model is presented in Section 3. Experiments and results to validate our model are given in Section 4. Finally, in Section 5 we state our conclusions and intended future work.

## 2. RELATED WORK

Most of the existing literature in the subject of human emotion recognition has been focused on individuals rather than crowds (Horlings et al., 2008; Izar, 2013). Facial and vocal expressions are useful indicators to infer emotional states, Ekman proposed in Ekman and Friesen (2002) a system based on sets of action units (AU) to recognize emotions based on facial movements. Juslin and Scherer explore the use of pitch and context to infer emotions, as presented in Juslin and Scherer (2008). However, the use of facial and vocal expressions to identify emotions is not feasible in crowded environments. Observation of behaviors seems more appropriate for estimating emotions in crowded scenarios but the relationship between behaviors and emotions is not straightforward as shown in Moors et al. (2013) as it varies depending on the context of the situation and environment. However, promising research has emerged in recent years proposing solutions to this problem. An interesting experiment in Novelli et al. (2013) tested a self-categorization theory to estimate positive and negative emotional responses to crowded environments under different circumstances. Inspired from the highly crowded cities in China, Liu et al. (2013) analyze the contagion of emotions among individuals, particularly under abnormal (panic) scenarios. A more relevant research and the starting point for the work presented here was done by Baig et al. (2014) with a probabilistic model to estimate emotional state of individuals as positive or negative based on the time and trajectory taken to traverse a simple scenario. Our contribution differs from Novelli et al. (2013) and Liu et al. (2013) in that

![img-0.jpeg](img-0.jpeg)

FIGURE 1 | Hierarchical bayesian model for entities individual and crowd.

![img-1.jpeg](img-1.jpeg)

FIGURE 2 | (A) Simulation of a crowded environment. (B) Plot of individual's trajectories, colors are assigned randomly.

we provide a method for online estimation of emotions of both individuals and the crowd as a whole. Also, unlike the work in Baig et al. (2014) that models only individuals that have the same motivation, we provide a more robust and adaptable framework that treats individuals and the crowd as separate entities to estimate emotions under environments where multiple types of behaviors are observed.

## 3. METHODS

This section describes the proposed hierarchical Bayesian model to describe behaviors and associated emotional states of both entities *individual* and *crowd*. In this work, we define a behavior as the way in which an entity transits among different states to achieve its goal (destination). For *individual*, a state corresponds to a physical region of the environment whereas for the crowd a state corresponds to a given configuration of people's density distribution in the observed environment. Behaviors for both *individual* and *crowd* are labeled empirically by a human operator knowledgeable of the environment using the labels of positive, normal or negative to denote the emotional state.

In overall, our approach starts by learning the topology of the observed environment from the trajectory of individuals using a self-organizing map (SOM) (Kohonen, 1990) which

![img-2.jpeg](img-2.jpeg)

FIGURE 3 | (A) Training data (green) and the self-organizing map *SOM<sup>I</sup>* (red edges and blue nodes). (B) Environment partitioned into zones, colors are assigned to zones in a random fashion. (C) Clustering distribution of training data among zones.

divides the physical space into regions. Trajectories of individuals are represented as transition of regions, and all trajectories with similar destination are classified to a same behavior, to finally build a probabilistic model that describes this behavior. Likewise for the crowd, similar sequences of state transitions are grouped into a same behavior which is described by means of a probabilistic model. The bayesian network for both *individual* and *crowd* entities is presented in Figure 1.

Once the topology of the environment and behaviors of both the *individual* and the *crowd* are learned, we can test the ability of the model to produce estimation of emotions.

### 3.1. Environment Representation

We first address the problem of obtaining a topological representation of the environment of interest as this is necessary to describe behaviors of individuals. Let us consider an environment monitored by a surveillance camera that captures the motion of individuals as illustrated in Figure 2A. By applying state of the art techniques for multi-target tracking in camera networks (Antonini et al., 2006; Ali and Shah, 2008) it is possible to obtain the trajectory of each individual and collect this data into a training set **X**

$$
\mathbf{X} = \{\hat{x}_{1_i}, \dots, \hat{x}_{N_i}\}_{i=1}^{\tau_k} \tag{1}
$$

where $\hat{x}_{i_i} \in \mathbb{R}^2$ is a coordinate estimation of individual $\theta_i$ at time $t$, in a period of observation from 1 to $\tau_k$ for a total of $N$ individuals. Using **X** we train a self-organizing map *SOM<sup>I</sup>* containing a set of nodes $S = \{s_1, \dots, s_{m \times n}\}$ where $m$ is the number of rows and $n$ is the number of columns in an hexagonal topology. As a result of the training phase, *SOM<sup>I</sup>* provides a complete topological representation of the environment, where node $s_i \in S$ represents a mutually exclusive zone in the environment as shown in Figures 3A,B. Representing the environment utilizing a self-organizing map encompasses several advantages including (a) unsupervised learning of the environment's topological configuration, (b) clustering and reduction of data and (c) a simpler way to describe individual's trajectories.

### 3.2. Entity Individual

We describe each observed individual $\theta_i$ in the environment with an instance of the entity *Individual* hence in a crowd with $N$ people detected, a total of $N$ instances will be implemented. The hierarchical model of entity *Individual* is presented in Figure 1. We describe the trajectory of $\theta_i$ as a discrete-controlled process with a state vector $x_{i_i} \in \mathbb{R}^2$

$$
x_{i_i} = x_{i_{i-1}} + g_{i_i} \tag{2}
$$

and observation vector $z_{i_i} \in \mathbb{R}^2$

$$
z_{i_i} = x_{i_i} + h_{i_i} \tag{3}
$$

Where $g_{i_k}$ and $h_{i_k}$ represent the process and observation noise, both assumed to be independent, white, with Gaussian

distribution. Applying an Extended Kalman Filter (EKF) over the observation and state vectors we obtain an estimation $\hat{x}_{t_{i}}$. The trajectory $X_{i}$ of $\vartheta_{i}$ is described as a sequence of estimations

$$
X_{i}=\left\{\hat{x}_{t_{1}}, \ldots, \hat{x}_{t_{k}} ; t_{k} \geq 1\right\}
$$

and $\left\{X_{k}\right\}_{k=1}^{N}$ represents the trajectories of individuals $\left\{\vartheta_{k}\right\}_{k=1}^{N}$. Using the zones of $S$ and $S O M_{I}$ produced in Section 3.1, we can cluster every estimation $\hat{x}_{t_{i}} \in X_{i}$ into a zone $s_{k} \in S$ as $\operatorname{SOM}_{I}\left(\hat{x}_{t_{i}}\right)=s_{k}$. Furthermore, we can express the trajectory $X_{i}$ as a sequence of zones

$$
w_{i}=\left\{s_{1}, \ldots, s_{q} ; s_{j} \in S, q \geq 1\right\}
$$

where $w_{i}$ is called a word. Words are grouped into a vocabulary $V_{l}=\left\{w_{1}, \ldots, w_{q}\right\}$ given the condition that $\forall w_{a}, w_{b} \in V_{l}, s_{1} \in$ $w_{a}=s_{1} \in w_{b}$ and $s_{n} \in w_{a}=s_{m} \in w_{b}$ where $\left|w_{a}\right|=n$ and $\left|w_{b}\right|=m$, that is, words with similar origin and destination. The notion of words provides a simplified way to describe trajectories whereas the notion of vocabularies allows to group trajectories that correspond to the same behavior, aiming to reach the same destination. Hence, each vocabulary $V_{l}$ indicates a different behavior. Each learned behavior is modeled with two conditional probability distributions (CPDs)

$$
\Omega_{s_{\alpha}, s_{\beta}, s_{b+1}, w_{a: b}}^{I}=p\left(s_{\alpha}, s_{\beta}, s_{b+1} \mid w_{a: b}\right)
$$

and

$$
\Lambda_{\Delta t, s_{b+1}, s_{b}}^{I}=p\left(\Delta t \mid s_{b+1}, s_{b}\right)
$$

where $s_{\alpha}$ is the initial state, $s_{\beta}$ is the final state and $s_{b+1}$ is the predicted next state given the partial observed trajectory $w_{a: b}$ from time instant $a$ to $b$ in Equation (6). $\Delta t$ is the transition time given the current state $s_{b}$ and the predicted next state $s_{b+1}$ in Equation (7). The purpose of Equation (6) is to estimate the origin, destination and next state of $\vartheta_{i}$ by matching $w_{a: b}$ to the most similar existing word $w_{k}$ with the highest likelihood. On the other hand, Equation (7) estimates the time required for the next transition time. Notice that in both Equations (6) and (7), the superscript $I$ is used to indicate the behavior (vocabulary) to which the CPDs correspond to. Given the estimation of trajectory (Equation 6) and transition time (Equation 7) we can proceed to estimate the emotional state using Bayes rule (Equation 8)

$$
\begin{aligned}
p\left(E, w_{a: b+1}, \Delta t\right)= & p(E) p\left(s_{\alpha}, s_{\beta}, s_{b+1} \mid w_{a: b}\right) \\
& p\left(\Delta t \mid s_{b+1}, s_{b}\right)
\end{aligned}
$$

where $E$ is the emotional state labeled as positive, normal or negative, and $p(E)$ is the prior probability learned from the training data and assumed to be uniform. We evaluate Equation (8) for each possible value of $E$ in order to find the emotional state with the highest likelihood. Given that the association between behavior and emotion depends on the context of the situation, the rules for labeling are to be determined for each particular scenario. However, in Section 4 we explain the labeling criteria applied to the experiments presented here.

TABLE 1 | Parameters of training and testing datasets produced from simulations.


### 3.3. Entity Crowd

Supported by the work presented in Le Bon (2007) and Reicher (2012) we argue that a crowd behaves as a collective minded entity and therefore we can model behaviors and infer emotional states for the entity crowd in a similar way to that of the entity individual. One single instance of the entity crowd is employed in a given environment. We start our description of the entity crowd by defining a state vector $X_{C_{i}}$

$$
X_{C_{i}}=\left\{x_{1_{i}}, \ldots, x_{N_{i}} ; x_{i_{i}} \in \mathbb{R}^{2}\right\}
$$

and observation vector $Z_{C_{i}}$

$$
Z_{C_{i}}=\left\{z_{1_{i}}, \ldots, z_{N_{i}} ; z_{i_{i}} \in \mathbb{R}^{2}\right\}
$$

where $x_{i_{i}}$ and $z_{i_{i}}$ are the state and observation vectors of $\vartheta_{i}$ as defined in Equations (2) and (3), respectively, for a total of $N$ individuals. In a similar way we could define $\hat{X}_{C_{i}}=\left\{\hat{x}_{i_{i}}\right\}_{i=1}^{N}$ as an estimation of the state vector of entity Crowd, however the difficulty of using that definition is that $\hat{X}_{C_{i}}$ is prompt to irregular dimensionality between samples as individuals join or leave the crowd. Instead we define $\hat{X}_{C_{i}}$ as

$$
\hat{X}_{C_{i}}=\left\{\hat{y}_{1_{i}}, \ldots, \hat{y}_{m \times n_{i}}\right\}
$$

where $\hat{y}_{k_{i}}$ is an estimated amount of individuals in zone $s_{k} \in S$ at time $t_{i}$ for a total of $m \times n$ zones in $S$ as produced by $S O M_{I}$ in Section 3.1. In this sense, the crowd's state vector estimation is implicitly dependent on the estimation of the individuals' trajectories. This definition of $\hat{X}_{C_{i}}$ is more advantageous as it provides a vector with uniform dimensionality while maintaining meaningful information. Also, since the focus of $\hat{X}_{C_{i}}$ is density estimation rather than trajectory tracking, we could employ crowd density algorithms (Cho et al., 1999; Rahmalan et al., 2006) to achieve this task. We collect the estimations $\hat{X}_{C_{i}}$ into a training set

$$
X_{C}^{T}=\left\{\hat{X}_{C_{i_{1}}}, \ldots, \hat{X}_{C_{i_{k}}} ; t_{k} \geq 1\right\}
$$

and use this set to train a self-organizing map $\operatorname{SOM}_{C}$ that further reduces dimensionality and provides a representation of states transitions. It is important to mention that $\operatorname{SOM}_{C}$ does not provide topological information as $\operatorname{SOM}_{I}$ does. $\operatorname{SOM}_{C}$ is composed by $p$ rows, $q$ columns and a set of nodes $C=$ $\left\{c_{1}, \ldots, c_{p \times q}\right\}$ where the node $c_{k}$ represents a state of the crowd. This enables us to classify each estimation to a state.

![img-3.jpeg](img-3.jpeg)

FIGURE 4 | Examples of learned behaviors from the trajectories in the training phase, a total of 41 different behaviors where identified. Colors are assigned randomly.

For the entity crowd we do not define words to describe state transition sequences because unlike the entity individual where there is a finite trajectory, the sequence of state transitions in a crowd emerges as a cyclic process with people continuously joining and leaving the crowd. As explained in Section 5 we aim to explore the cyclic behaviors of a crowd in a more comprehensive way in future work, but for the work presented here we describe a crowd behavior as a first order Markov process with two CPDs to estimate the change of states and transition time

$$
\gamma_{c_{k}, c_{k+1}}=p\left(c_{k+1} \mid c_{k}\right)
$$

and

$$
\Psi_{\Delta_{t}, c_{k}}=p\left(\Delta_{t} \mid c_{k+1}, c_{k}\right)
$$

where $c_{k}$ and $c_{k+1}$ are the current and next state, respectively, and $\Delta t$ is the transition time. The emotional state of the crowd

is assigned to be the same as the experienced for the majority of individuals, hence no labeling is applied to specific state or transition time of the entity crowd.

## 4. EXPERIMENTS AND RESULTS

To validate our proposed model we employ data produced by a realistic crowd simulator first introduced in Chiappino et al. (2012, 2015), based on social forces (Helbing and Molnar, 1995) where each individual in the environment is treated as a particle subject to 2D forces, deriving its motion equations from Newtons law $F=m a$ and accounting for its motivation as an attraction force pulling the individual toward its destination and repulsive forces from physical objects and other individuals in the environment. We have recreated a scenario similar to that of a train station as shown in Figure 2A, the produced trajectories are plotted in Figure 2B. The information of individual's trajectories is provided directly from the crowd simulator, hence the steps for detection and tracking of people are omitted. Simulations were carried out under different levels of crowdedness, details for the training and testing datasets produced from simulations are presented in Table 1.

The self-organizing maps $S O M_{I}$ and $S O M_{C}$ are initialized with similar parameters. The set of neurons on each $S O M$ is initialized with random weights and in a hexagonal arrangement spread across the corresponding input space. Distance between neurons is calculated by the number of links among them. The initial neighborhood size is 3 with 100 steps for the ordering phase. The training phase is done over 500 epochs by competitive layer but without bias, updating the winning neuron and all other neurons within the given neighborhood using Kohonen rule.

The first task addressed is to use the trajectory of individuals to obtain a topological representation of the environment with the help of a self-organizing map $S O M_{I}$ as shown in Figures 3A,B. We can observe from Figure 3C the distribution of training data among zones after the clustering process, which is important when describing trajectories, larger zones indicate that more trajectories traverse this area whereas the opposite is also true for smaller zones. The decision of how many zones to employ to describe trajectories has a direct impact on the reliability of our model to estimate the emotion of individuals; this happens because we describe the behavior of individuals by transition of zones, and with fewer zones there is a higher uncertainty of the motion of individuals. In these experiments, $S O M_{I}$ is composed of 100 zones ( 10 rows and 10 columns) in a hexagonal topology. After testing our model with different dimensions, we found this size to be a suitable balance between predictability and topological representativeness.

Employing $S O M_{I}$, the trajectories of the training set were evaluated, and a total of 41 different behaviors were identified, a few examples of the learned behaviors are shown in Figure 4.

The scenario replicated in the experiments corresponds to that of a train station. Hence, the criteria for labeling behaviors follows from the assumption that people aim to reach their destination in the briefest possible time. The behaviors with the minimum number of state transitions and the shortest transition time are
![img-4.jpeg](img-4.jpeg)

FIGURE 5 | (A) Overall success rate in behavior prediction of individuals. (B) Online emotion estimation of individuals.
labeled with a positive emotion. The behaviors with the higher frequency of occurrence are associated with a normal emotion. Finally, the behaviors with the highest number of transitions and longer transition time are assigned a negative emotion. During the testing phase, for the purpose of estimating emotional state on individuals, our hierarchical model predicts the zones transitions and transition time for each individual in real time based on the learned behaviors. In our model, the accuracy level to estimate the emotion of individuals depends on the model's capability to predict the individual's behavior. In Figure 5A we show the behavior prediction success rate during a period of 100 s where the average rate was of $76 \%$. Throughout the entire length of the simulations, the prediction success rate oscillated between 74 and $82 \%$. A summary of the model's performance to estimate emotional states is presented in Table 2. In Figure 5B we present a snapshot of the online emotion estimation of individuals.

The behavior of the crowd is described with a second selforganizing map $S O M_{C}$, also composed of 100 zones ( 10 rows and 10 columns), which allow us to build a probabilistic model for its behavior. However, unlike $S O M_{I}$, a plot of $S O M_{C}$ does not provide a visual semantic due to the high dimensionality of

TABLE 2 | Confusion matrix of emotional state estimation based on individuals' behavior.


its state vector. Using the same simulations applied to test our model for individuals, we test the ability of the crowd model to predict its behavior, that is, the next state and transition time among states of $\mathrm{SOM}_{\mathrm{C}}$. In Figure 6A we can observe the behavior prediction success rate of the crowd oscillating more consistently between 50 and $94 \%$, with an average rate of $81 \%$. In the work proposed here, the emotional state of the crowd is not correlated to its behavior, instead is assigned to be the same as the experienced for the majority of individuals. In Figure 6B we display the summary of detected emotions in an observation period of 600 s , during which a positive emotion becomes predominant as the number of individuals joining the crowd increases.

## 5. CONCLUSIONS AND FUTURE WORK

In this work, we presented a robust model for the estimation of emotions on single individuals and the crowd as a whole, under complex crowded environments. In comparison with (Baig et al., 2014), our approach provides significant improvements: (1) accounts for scenarios with multiple origin and destination points, (2) introduces the idea of vocabularies to describe behaviors which help to reduce data sparsity, and (3) explores the idea of the crowd as a single entity with its own behavior and emotional state.

Our overall hypothesis is that crowd emotion is a combination of individual's emotion estimation, as suggested by neuroscience studies (de Gelder et al., 2010). In this particular study, we have a rather simple model that treats the crowd emotion as a sum of the emotions of the individuals in the crowd. The emotion of the crowd is estimated by a deviation of normal patterns and speed of movement identified in normal situations.

The approach presented here is applicable to real-life crowded environments for monitoring automation intended to identify and prevent dangerous situations as well as to improve crowd control. Furthermore, contributions of this nature are essential for the development of robust cognitive dynamic systems intended for smart cities.

Future development of this work will focus on extending the model to consider the interaction of individual and crowd emotions enabling us to explore causality and contagion of emotional states among individuals and its impact in the crowd as a whole. The result of the simulations performed show the behavior of the crowd to emerge in a cyclic manner; we are interested in further explore this phenomenon and to provide a more comprehensive model for describing such behavior of the

![img-5.jpeg](img-5.jpeg)

FIGURE 6 | (A) Success rate in behavior prediction of crowd entity. (B) Online emotion estimation of the crowd. crowd. Finally, we aim to extend this model to enable its use in first person perspective models and applications.

## AUTHOR CONTRIBUTIONS

The central idea of this work was developed jointly with CR throughout extensive discussions. MB implemented modifications to the employed software to suit the experiments needs. LM helped in several technical aspects to facilitate the execution of the simulations. EB provided essential insights in the fundamentals of emotion theory and contributed to writing the manuscript. MR assisted with valuable insights and revision of the manuscript. All authors contributed significantly to the work presented in this paper.

## FUNDING

This work was produced under the program of Erasmus Mundus Joint Doctorate in Interactive and Cognitive Environments (EMJD ICE), funded by the Education, Audiovisual and Culture Executive Agency (EACEA).

## ACKNOWLEDGMENTS

Sincere thanks to the members of the Information and Signal Processing for Telecommunications Laboratory from the University of Genoa for their valuable
