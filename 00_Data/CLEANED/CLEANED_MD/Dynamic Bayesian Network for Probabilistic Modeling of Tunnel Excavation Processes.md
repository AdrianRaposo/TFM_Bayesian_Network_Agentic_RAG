# Dynamic Bayesian network for probabilistic modeling of tunnel excavation processes 

Olga Špačková ${ }^{1} \&$ Daniel Straub ${ }^{2}$<br>${ }^{1}$ Czech Technical University in Prague, Fac. of Civil Engineering (olga.spackova@fsv.cvut.cz)<br>${ }^{2}$ Engineering Risk Analysis Group, Technical University Munich (straub@tum.de)


#### Abstract

A Dynamic Bayesian Network (DBN) model for probabilistic assessment of tunnel construction performance is introduced. It facilitates the quantification of uncertainties in the construction process and of the risk from extraordinary events that cause severe delays and damages. Stochastic dependencies resulting from the influence of human factors and other external factors are addressed in the model. An efficient algorithm for evaluating the DBN model is presented, which is a modification of the so-called Frontier algorithm. The proposed model and algorithm are applied to an illustrative case study, the excavation of a road tunnel by means of the New Austrian Tunneling Method.


## Keywords

Tunnel excavation; construction time estimation; dynamic Bayesian networks; risk assessment; convolution; modified Frontier algorithm.

## 1 Introduction

Estimations of time and cost of tunnel construction projects are subject to major uncertainties, which are caused by uncertain geotechnical conditions, varying

performance of the utilized excavation technologies and human and organizational factors. In spite of these uncertainties, at present a majority of stakeholders (project owners, contractors, public, etc.) rely on deterministic estimates of project time and cost, which are based on expert judgment. Additionally to these deterministic estimates, the risk is often analyzed by means of semi-quantitative or qualitative methods, which are also based on expert judgements; applications of this approach are presented in Sturk et al. (1996), Shahriar et al. (2008) and Hong et al. (2009). The approach is also recommended in guidelines of International Tunneling Asociation (Eskesen et al. 2004).

Since time and cost estimates are fundamental parameters for decision making in all phases of tunnel construction projects, it should be evident that a more realistic assessment of the associated uncertainties is crucial. The need of probabilistic prediction of construction time and costs and their communication with the stakeholders has been discussed in the tunneling community in recent years (Lombardi 2001, Reilly 2005, Grasso et al. 2006). Several model for such predictions have been developed, as summarized in the following.

In Ruwanpura \& Ariaratnam (2007), tools for simulation of the tunnel drilling process are presented, which include Monte Carlo Simulation (MCS) for the evaluation of uncertainties in predicting construction time and costs. Isaksson \& Stille (2005) suggest an analytical solution for probabilistic estimation of tunnel construction time and cost considering both normal variations of the performance and extraordinary events. In Chung et al. (2006) and in Benardos \& Kaliampakos (2004) observed advance rates are used for updating the predictions of advance rates and resulting excavation time for the remaining part of the tunnel, by means of Bayesian analysis and artificial neural networks, respectively.

At present, the most advanced method for probabilistic modeling of uncertainties in the tunnel construction processes available in the literature is the Decision Aids for Tunneling (DAT), developed in the group of Prof. Einstein at MIT. It has been applied to several projects, an overview of which is given in Min (2008). DAT uses Monte Carlo simulation (MCS) for probabilistic prediction of construction time, costs and consumption of resources. It takes into account the geotechnical uncertainties, which are modeled by means of a Markov process (Chan 1981), as well as the uncertainties in the

construction process. In the applications, the coefficients of variation of the total construction time and cost estimated by DAT are typically less than 5\%. This computed uncertainty is too low when compared to the one observed in practice, e.g. in (Flyvbjerg et al. 2004).

The risk of extraordinary events, such as tunnel collapse, tunnel flooding or legislative and political obstruction, is not included in the original DAT model. A model to include the risk of a tunnel collapse has been presented in Sousa \& Einstein (2011). Therein, a dynamic Bayesian networks (DBN) model and decision graphs were used to identify the optimal construction method based on a comparison of expected utilities of different methods (whereby utilities correspond to costs). Uncertainty in the costs is not considered and no probabilistic estimate of the overall construction cost and time is presented.

None of the models known to the authors fulfills all requirements that are deemed important for a realistic estimation of construction time and costs. A tunnel construction model should ideally provide the following: (1) It should correctly model common factors that systematically influence the construction process, such as human and organizational factors. These factors lead to stochastic dependence among the random variables describing performance at different phases of the excavation. The significant influence of such dependencies on construction time estimates is shown for example in Yang (2007) and Moret \& Einstein (2011). (2) The model should consider the risk of extraordinary events (e.g tunnel collapse, tunnel flooding). These events, even if they have relatively small probabilities, cannot be neglected as they often lead to huge delays and damages (IMIA 2006, Špačková et al. 2010, Sousa \& Einstein 2011). (3) The model should allow for making full use of data available from previous projects, such as advance rates and costs recorded during excavation of tunnels under similar conditions. In this way, the know-how can be systematically managed. (4) The methodology should facilitate the easy updating of predictions when new information on the analyzed project (e.g. geotechnical investigations, performance rates and costs observed after commencement of excavation) is available. (5) The model assumptions and involved simplifications must be properly understood and described. This is important in probabilistic modeling, where results are difficult to validate by experiments and must therefore be well reasoned.

The requirements stated above motivate the development of a methodology based on Dynamic Bayesian Networks (DBN). While many of the requirements could be satisfied by means of the commonly used MCS approach, we propose DBNs, because they are more efficient in updating of the predictions based on additional observations (requirement 4) and because the graphical nature of DBN strongly facilitates the representation and communication of the model assumptions (requirement 5), in particular when dependencies among random variables are present (requirement 1). The DBN presented in this paper also includes extraordinary events and the influence of human and organizational factors (requirements 1 and 2). The learning of model parameters from data (requirement 3) is not addressed in detail in this paper. However, the DBN framework facilitates such learning.

The proposed DBN is applied to the case study utilizing the DAT model presented in Min (2003) and Min et al. (2003). The proposed DBN is here limited to estimating construction time, but adaptation of the model to predict construction cost is straightforward by simply replacing the variable time with variable cost.

The paper starts out with a general introduction to Bayesian networks and to the Frontier algorithm applied for evaluating DBNs (section 2). Thereafter, the structure of the proposed DBN model for tunnel excavation is presented in section 3. In section 4, the application of the frontier algorithm for evaluating the tunnel DBN is explained in details. A modification of the algorithm is presented, which significantly increases its efficiency for this application. Finally, the DBN model is applied to a case study, allowing investigation of the effect of extraordinary events and the influence of human and organizational factors on the excavation time estimates.

# 2 Bayesian networks - basic principles 

Bayesian networks (BN) are directed acyclic graphical models for representation of a set of random variables. Random variables are symbolized by the nodes of the BN, the dependencies between them are depicted by directed links. The set of random variables $X_{1}, X_{2}, \ldots, X_{N}$ is fully described by the graphical structure and the conditional probability distribution of each node $X_{i}$ given its parent nodes $p a\left(X_{i}\right)$. Parent nodes are all nodes

with links pointing towards $X_{i}$. The joint probability mass function of $X_{1}, X_{2}, \ldots, X_{N}$ is expressed using the chain rule as

$$
p\left(x_{1}, . x_{2}, \ldots, x_{N}\right)=\prod_{i=1}^{N} p\left(x_{i} \mid p a\left(x_{i}\right)\right)
$$

where $p\left(x_{i} \mid p a\left(x_{i}\right)\right)$ is the conditional probability mass function (PMF) of variable $X_{i}$ given its parent variables. The notation used here applies to discrete random variables, which is the case for the model proposed in this paper. Whenever no ambiguity arises we use $p\left(x_{1}, . x_{2}, \ldots, x_{N}\right)$ as the short notation for $p_{X_{1}, X_{2}, \ldots, X_{N}}\left(x_{1}, . x_{2}, \ldots, x_{N}\right)$ and similarly $p\left(x_{i} \mid p a\left(x_{i}\right)\right)$ for $p_{X_{i} \mid p a\left(x_{i}\right)}\left(x_{i} \mid p a\left(x_{i}\right)\right)$.

The efficiency of the BN stems from the decomposition of the joint probability distribution into local conditional probability distributions according to Eq. (1). This decomposition is made possible, because the graphical structure of the BN encodes information about dependence among random variables. From the BN graph, one can directly infer which random variables are statistically independent of each other (dseparated in BN terminology). The statistical dependencies change when states of one or more nodes in the network are fixed (e.g. when evidence is available). For a given set of nodes $A$ it is possible to identify another set of nodes, which, when fixed, d-separate $A$ from the rest of the network. This set is called the Markov blanket of $A$. For a more detailed introduction to BN we refer to Jensen \& Nielsen (2007).

An example of a simple BN is depicted in Fig. 1. This BN contains four random variables: geology $G$, construction method $M$, excavation time $T$ and construction costs $C$. The construction method $M$ is defined conditionally on geology $G$ (i.e. $G$ is a parent node of $M$ and, correspondingly, $M$ is a child node of $G$ ), the excavation time $T$ is defined conditionally on the construction method $M$ and costs $C$ are defined conditionally on both $M$ and $T$.

![img-0.jpeg](img-0.jpeg)

Figure 1. Example of a Bayesian network.

Following Eq. (1), the joint probability mass function (PMF) of this BN is

$$
p(g, m, t, c)=p(g) p(m \mid g) p(t \mid m) p(c \mid m, t)
$$

where $p(g)$ is the PMF of $G$ and $p(m \mid g), p(t \mid m)$ and $p(c \mid m, t)$ are conditional PMFs of $M, T$ and $C$. The values of the conditional PMFs are conveniently organized in conditional probability tables (CPT). An example CPT is provided in the application presented in Section 5.1.

Assumptions concerning dependencies among the random variables are made when constructing the BN in Fig. 1: According to this model, if the construction method is known (fixed), any information about geology does not alter the probability distribution of time and costs, i.e. $T$ and $C$ are statistically independent of $G$ if $M$ is fixed.

Dynamic Bayesian networks (DBN) are a special case of BN used for modeling of random processes. An example is depicted in Fig. 2. The $i$ th slice of the DBN represents the state of the system in time/position $i$. Because the state of the system in slice $i$ has only its state in slice $(i-1)$ as its parent, this DBN represents a Markov chain: In a Markov chain, the future states are independent of the past states when the present state is known.
![img-1.jpeg](img-1.jpeg)

Figure 2. Example of a dynamic Bayesian Network (DBN)

In the example of Fig. 2, each slice $i$ consists of two random variables geology $G_{i}$ and unit excavation time $T_{i}$. The joint probability of $G_{i}$ and $T_{i}$ is obtained as

$$
p\left(g_{i}, t_{i}\right)=\sum_{g_{i-1}} p\left(g_{i-1}\right) p\left(g_{i} \mid g_{i-1}\right) p\left(t_{i} \mid g_{i}\right)
$$

where $p\left(g_{i-1}\right)$ is the marginal probability distribution of random variable $G_{i-1}$ in slice $(i-1), p\left(g_{i} \mid g_{i-1}\right)$ is the conditional probability describing changes of geology between neighboring slices and $p\left(t_{i} \mid g_{i}\right)$ is the conditional probability of $T_{i}$ in slice $i$ defined conditionally on geology in the same slice.

The use of BN and DBN in engineering applications has grown significantly in recent years (Weber et al. 2010). One reason is their graphical nature that facilitates communication of the model assumptions. Secondly, the BNs allow to easily update the prediction when additional information becomes available. Finally, the BN allows decomposing large models into local probabilistic dependences. Therefore, they are especially suitable for engineering applications, where statistical data is often sparse, but where conditional probability distributions of variables can be modeled by means of engineering models, expert judgment or other known relations. Applications of BN and DBN in engineering problems can be found for example in Faber et al. (2002), GrêtRegamey \& Straub (2006), Neil et al. (2008), Droguett et al. (2008), Straub (2009) or Straub \& Der Kiureghian (2010b).

# 2.1 Evaluation of the DBN - basic principles of the Frontier algorithm 

For the evaluation of the DBN presented in this paper, a procedure based on the so-called Frontier algorithm (see Murphy 2002) is used. It enables one to compute the marginal probability distribution of all random variables. The algorithm belongs to the group of exact inference methods and is applicable to DBNs with discrete nodes.

The Frontier algorithm utilizes the fact that in the DBN one can identify sets of nodes, which, if fixed, d-separate the nodes on their left side from the nodes on their right side. (These sets of nodes are Markov blankets of the sets of nodes on either their left or their right side.) These sets are called frontiers (or frontier sets). To give an example, all

variables in slice $i$ of the DBN in Fig. 2 create a frontier. They d-separate variables in the slices $j>i$, representing future states of the process (right side of the DBN), from the variables in the slices $j<i$, representing past states of the process (left side of the DBN).

For the evaluation of the DBN, the frontier is moved slice by slice along the network. We can add a variable to the frontier, if all its parents are already included in the frontier. We can remove a variable from the frontier if all its children variables are included in the frontier.

In the following, the Frontier algorithm is illustrated on a DBN containing $N$ variables in each slice. One cycle of the algorithm moving frontier from slice $i-1$ to slice $i$ is shown in Fig. 3. The variables marked with grey are those included in the frontier at a particular step. At the beginning of the cycle (Fig. 3a), the frontier contains variables $X_{1, i-1}, X_{2, i-1} \ldots X_{N, i-1}$ and $p\left(x_{1, i-1}, \ldots, x_{N, i-1}\right)$ is the known joint PMF of these variables.
![img-2.jpeg](img-2.jpeg)

Figure 3. Graphical representation of one cycle of the Frontier algorithm for an example DBN. The grey nodes are those included in the frontier at a given step.

In step (b), a variable $X_{1, i}$ is added to the frontier and variable $X_{1, i-1}$ is removed from the frontier. Adding $X_{1, i}$ corresponds to calculating the joint probability mass function $p\left(x_{1, i-1}, \ldots, x_{N, i-1}, x_{1, i}\right)$ as:

$$
p\left(x_{1, i-1}, \ldots, x_{N, i-1}, x_{1, i}\right)=p\left(x_{1, i-1}, \ldots, x_{N, i-1}\right) p\left(x_{1, i} \mid p a\left(x_{1, i}\right)\right)
$$

Removing $X_{1, i-1}$ is performed by summing the joint PMF over all states of $X_{1, i-1}$. This operation is called marginalization in BN terminology.

$$
p\left(x_{2, i-1} \ldots x_{N, i-1}, x_{1, i}\right)=\sum_{X_{1, i-1}} p\left(x_{1, i-1}, x_{2, i-1} \ldots x_{N, i-1}, x_{1, i}\right)
$$

The above steps are repeated for other nodes until the frontier consists only of nodes of slice $i$ as shown in (Fig. 3d). The cycle is then repeated for the next slice $i+1$ and so on. The marginal distribution of any variable $X_{j, i}$ can be obtained from the joint distribution of any frontier that includes this variable, through elimination of all other variables in that frontier.

As seen from Eqs. 4 and 5 above, in each step the algorithm requires only the joint probability of the variables in the frontier, which reduces the computational demand significantly. In every step, the frontier should include as few variables as possible. We therefore add a new variable to the frontier as late as possible and we remove variables from the frontier as soon as possible.

Evidence (observations of random variables) can be efficiently included in the DBN. Consider observation of node $X_{j, i}=x$. The frontier algorithm proceeds until a frontier including $X_{j, i}$ is reached. The observation is then included by setting the probability of all outcome states with $X_{j, i} \neq x$ equal to zero and normalizing the probabilities of the remaining outcome states. With this procedure, the probability distribution of a variable in slice $i$ is updated with the evidence from all slices $k \leq i$. The evidence in slices $k>i$ is not included. To include such evidence, the above algorithm must be extended by a backward computation, in which the frontier moves from right to left. This case is not considered in this paper. Details on the algorithm can be found in Murphy (2002); Straub (2009) presents an application of the algorithm to modeling the effect of inspection and monitoring of deteriorating structures.

# 3 Modeling tunnel excavation process via DBN 

A DBN for modeling uncertainties connected with tunnel excavation processes is presented in this section. The DBN is shown in Fig. 4. The excavation process is described by random variables representing (1) geotechnical conditions, (2) the

construction process, (3) extraordinary events and (4) overall excavation time. Excavation cost is not included here for ease of presentation, but its modeling is analogous to excavation time. Each slice in the DBN represents a tunnel segment of length $\Delta l$, i.e. a segment from position $(i-1) \Delta l$ to position $i \Delta l$ along the tunnel axis. Within one slice, all variables are modeled as constant. Table 1 provides an overview of the definition of the variables as they are used in the case study presented in sec. 5. The variables are introduced in more detail in the following subsections.
![img-3.jpeg](img-3.jpeg)

Figure 4. DBN for tunnel excavation. (The variables are explained in Table 1.)

Table 1. Overview of the variables in the DBN.


${ }^{*} t_{\text {int }}$ is the discretization interval of time variables. In the application example it is $t_{\text {int }}=0.5$ day,
${ }^{* *}$ upper bound of cumulative time $=122 \times 15=$ (number of segments) x (upper bound of unite time)
${ }^{* * *} t_{\text {extra,99.9 }}$ is the 99.9 percentilse of $\mathrm{T}_{\text {extra }}$

# 3.1 Geotechnical conditions 

The variables to be utilized for describing the geotechnical conditions vary depending on the specifics of the tunneling project. The variables selected here follow the description in Min (2003). Within a segment $i$ of the tunnel, the geotechnical conditions are described by the random variables zone $Z_{i}$, rock class $R_{i}$, height of the overburden $O_{i}$ and ground class $G_{i}$.

Along the tunnel axis, quasi-homogenous geotechnical zones are identified. The positions of the boundaries of these quasi-homogenous geotechnical zones are not known with certainty; therefore, the zone $Z_{i}$ to which segment $i$ belongs is modelled as a random variable. The definition of this variable is in detail described in Annex 1. The rock class $R$ within a zone is modelled as a homogeneous Markov process. The suitability of Markov processes for modeling of geotechnical conditions (such as rock class, degree of jointing) along the tunnel axis was shown already in Chan (1981). The parameters of the Markov process can be estimated by experts. The description of the parameters of the Markov process and definition of the variable $R_{i}$ in the DBN are given in Annex 1.

The height of overburden $O_{i}$ is modelled deterministically. The ground class $G_{i}$ is defined deterministically for given $R_{i}$ and $O_{i}$. As evident from Table 1, each $G_{i}$ corresponds to a specific combination of $R_{i}$ and $O_{i}$, e.g. ground class L-I stands for rock class I with low overburden, M-II for rock class II with medium overburden.

# 3.2 Construction process 

The construction performance in segment $i$ of the tunnel is described by the variables cross section geometry $E_{i}$, construction method $M_{i}$, Human factor $H_{i}$ and unit excavation time $T_{i}$.

The deterministic variable geometry $E_{i}$ enables one to consider the different cross sections along the tunnel (typical cross section vs. extended cross section for emergency parking places EPP) and it is also used to consider the special conditions at the beginning and end of the tunnel and at the location where the tunnel passes an existing chemical plant.

The construction method $M_{i}$ describes the excavation type and the related support pattern applied in the $i$ th segment and is determined conditional on the ground class $G_{i}$ and tunnel geometry $E_{i}$. The modeling of $M_{i}$ follows Min (2003), where the details of the construction methods are described.

The variable Human factor $H_{i}$ represents the uncertain quality of design and construction works and other external factors (legislative, political etc.) affecting the construction process. The Human factor $H_{i}$ is in one of the three states "unfavourable", "neutral" or "favourable" throughout the entire tunnel construction, i.e. the $H_{i} \mathrm{~s}$ are fully dependent from one slice to the next and the conditional probability matrix $p\left(h_{i} \mid h_{i-1}\right)$ in each slice is the $3 \times 3$ identity matrix. This simple model reflects the fact that the influence of human factor cannot be directly measured and can only be deduced from the average performance over long sections of the tunnel project (Špačková et al. 2010). The uncertainty in the Human factor introduces dependence among the performance in each segment of the tunnel, and thus increases the variability of the estimated total construction time. $H_{i}$ can also be interpreted as a random variable describing a model class, which reflects uncertainty on the selection of the appropriate probabilistic model of variables that are defined conditionally on $H_{i}$, i.e. unit time and failure rate. Prior to

construction, the probability distribution of unit time and the failure rate are not known with certainty. Several probabilistic models are thus applied. During the construction, it becomes apparent which of the models is the most appropriate. This learning process is automated when applying Bayesian networks through the updating of the probability distribution of $H_{i}$. The concept of model classes is often applied in the context of structural identification (e.g. Cheung and Beck 2010).

For every construction method $M_{i}$ and human factor $H_{i}$, the unit time $T_{i}$ is defined by a conditional $\operatorname{CDF} F\left(t_{i} \mid m_{i}, h_{i}\right)$. To facilitate the application of the exact inference algorithm presented earlier, the variable $T_{i}$ is discretized, as described in sec. 4.1.

# 3.3 Extraordinary events 

Extraordinary events are defined as events that stop the advance of the excavation (progress of the tunnel heading) for longer than a threshold value (here chosen as 15 days); these events can be considered a failure of the construction process. They are e.g. tunnel collapses, tunnel flooding or major legislative or organizational problems. They are characterized by the variables failure mode $F_{i}$ and number of failures $N_{F, i}$.

The failure mode $F_{i}$ describes the occurrence of failure in segment $i$. Different failure modes can be taken into account (cave-in collapse, tunnel flooding, fire). In the presented application, only modes "failure" and "no failure" were considered. $F_{i}$ is defined conditionally on ground class $G_{i}$ and human factor $H_{i}$.

The random variable $N_{F, i}$ represents the total number of failures from the beginning of the tunnel to location $i \Delta l$. It is defined conditionally on the number of failures in the previous slice, $N_{F, i-1}$, and the failure mode $F_{i}$ in the $i$ th segment. Definition of the variables $F_{i}$ and $N_{F, i}$ is described in Annex 1.

### 3.4 Excavation time

The main output of the model is the total excavation time $T_{\text {tot }}$. In the DBN, it is computed as the sum of excavation time excluding extraordinary events, $T_{\text {cum }}$ and the time delay caused by extraordinary events, $T_{\text {extra }}$.

The cumulative time $T_{\text {cum, } i}$ is the time for the excavation of the tunnel up to location $i \Delta l$. It is defined as the sum of $T_{\text {cum, } i-1}$ and the unit time in segment $i, T_{i}: T_{\text {cum, } i}=$ $T_{\text {cum, } i-1}+T_{i}$.
$T_{\text {extra, } i}$ is the time delay due to occurrences of failures (extraordinary events) in the tunnel construction up to segment $i$. The distribution of $T_{\text {extra, } i}$ for given number of failures $N_{F, i}$ can be derived from the statistics of observed delays, which provide the probability density function (PDF) of the delay caused by one failure event, $f_{D}(d)$. With $D_{k}$ being the delay caused by the $k$ th failure, the total delay due to $N_{F, i}$ failures is computed as the sum of the individual delays:

$$
T_{\text {extra, }, i}=\sum_{k=1}^{N_{F, i}} D_{k}
$$

We compute the PDF of $T_{\text {extra, } i}$ for given $N_{F, i}$ by assuming that all delays $D_{k}$ are independent and have identical $\operatorname{PDF} f_{D}\left(d_{k}\right)$. This implies the assumption that the expected delay caused by a failure is independent on the position where it occurs.

Assessment of the total excavation time is in most cases of interest for the tunnel as a whole or for a section of the tunnel. Therefore, its distribution is computed only at selected positions, as illustrated in Fig. 4, where $T_{\text {tot }}$ is assessed for the whole tunnel.

# 3.5 Length of segment represented by a slice of DBN 

We expect that the changes of conditions can only occur at the boundaries of the tunnel segments represented by slices of the DBN. We thus assume that the random variables are fully dependent within each segment. The optimal segment length $\Delta l$ corresponds (in case of cyclic excavation methods) approximately to the length of the excavation cycle. This topic is discussed in more detail in Špačková \& Straub (2011).

The definition of random variables, i.e. the determination of their conditional probabilities, also depends on $\Delta l$. Calculation of conditional PMFs of zone $Z_{i}$, rock class $R_{i}$ and failure mode $F_{i}$ for given $\Delta l$ is described in Annex 1. The conditional PDFs of unit time $T_{i}$ should be ideally determined directly from data for a given $\Delta l$.

The human factor $H_{i}$ is supposed to be fully dependent throughout the entire excavation, therefore its CPT does not change if $\Delta l$ changes. Deterministic variables and variables defined by deterministic functions (ground class $G_{i}$, construction method $M_{i}$, number of failures $N_{F, i}$ and cumulative time $T_{\text {cum, } i}$ ) are not influenced by the segment length.

# 4 Evaluation of the DBN 

The evaluation of the DBN proceeds in three steps: First, all continuous variables are discretized. Second, some of the nodes are eliminated from the DBN in order to simplify the computations in the modified Frontier algorithm. Third, the modified Frontier algorithm, which is outlined in Section 4.3, is applied. The three steps are presented in the following. In Section 4.4, the procedure for updating of the prediction based on observed geotechnical conditions and performance is shown.

### 4.1 Discretization of random variables

Random variables defined in a continuous space (i.e. variables describing unit time $T_{i}$ and delay $T_{\text {extra, } i}$ ) are transformed into random variables defined in a discrete space. The discretization is described below for $T_{i}$; an analogous procedure is used for discretizing $T_{\text {extra, } i}$.

Let $\tilde{T}_{i}$ be the original continuous random variable with parent variables $p a\left(\tilde{T}_{i}\right)$, which is defined by a CDF $F\left(\tilde{t}_{i} \mid P a\left(\tilde{T}_{i}\right)\right)$. Let $T_{i}$ be the corresponding discrete random variable whose $m_{T}$ states are denoted by $t_{i}^{(k)}$, where $k=1, \ldots, m_{T}$. Let state $t_{i}^{(k)}$ represent an interval $\left(\tilde{t}_{i}^{(k-1)}, \tilde{t}_{i}^{(k)}\right)$ in the original continuous space, $\tilde{t}_{i}^{(k)}$ is the upper bound of the interval corresponding to state $t_{i}^{(k)}$. The conditional probability mass function of $T_{i}$ then equals

$$
p\left(t_{i}^{(k)} \mid P a\left(\tilde{T}_{i}\right)\right)=F\left(\tilde{t}_{i}^{(k)} \mid P a\left(\tilde{T}_{i}\right)\right)-F\left(\tilde{t}_{i}^{(k-1)} \mid P a\left(\tilde{T}_{i}\right)\right)
$$

The intervals are defined so that they have an equal length $t_{\text {int }}$. Each state $t_{i}^{(k)}$ is represented by the central value of corresponding interval, i.e. $t_{i}^{(k)}=\tilde{t}_{i}^{(k)}-\frac{t_{i n t}}{2}$.

For computational purposes, which will become clear later in the paper (sec. 4.3), it is beneficial to define the representative values as integer multiplications of $t_{\text {int }}$.

In addition to $T_{i}$ and $T_{\text {extra }, i}$, also $T_{\text {cum, }, i}$ must be discretized. Since $T_{\text {cum }, i}$ is defined as a sum of $T_{\text {cum, }, i-1}$ and $T_{i}$, it is convenient to use the same discretization interval length $t_{\text {int }}$ for all three variables and to define the representative values of their states as integer multiplications of $t_{\text {int }}$. This, however, implies that the number of states of $T_{\text {cum, } i}$ increases with every slice of the DBN as is illustrated in Fig. 5. If $m_{T}$ is the number of states of $T_{i}, i=1, \ldots, I$, then the number of states of $T_{\text {cum }, i}$ is $m_{T_{\text {Cum }, i}}=i\left(m_{T}-1\right)+1$. To deal with the resulting large number of states of $T_{\text {cum, }, i}$, a modification to the Frontier algorithm is proposed in section 4.3.
![img-4.jpeg](img-4.jpeg)

Figure 5. Illustration of the summation of two discretized random variables: PMF of cumulative time $T_{\text {cum, }, i-1}$, unit time $T_{i}$ and cumulative time $T_{\text {cum, }, i}$ for tunnel segment $i=3$,zone $Z_{i}=1$, human factor $H_{i}=$ 'neutral', and rock class $R_{i}=$ III. The PMF of $T_{\text {cum, }, i}$ is obtained through convolution of $T_{\text {cum, }, i-1}$ and $T_{i}$.

# 4.2 Elimination of nodes 

Prior to the application of the Frontier algorithm, it is computationally beneficial to eliminate some nodes from the DBN. Such an elimination of nodes can be considered a

pre-processing of the DBN. In the presented DBN, we eliminate ground class $G_{i}$, overburden $O_{i}$, cross section geometry $E_{i}$ and construction method $M_{i}$. This operation can be performed generically for all slices in the DBN. The resulting DBN is shown in Fig. 6, following the procedure for graphical elimination of nodes explained in Straub and Der Kiureghian (2010a). When eliminating nodes from the network, additional links must be added to the remaining nodes, to ensure that their joint probability distribution is not altered. New links are introduced from $R_{i}$ to $F_{i}$ and $T_{i}$, and from $F_{i}$ to $T_{i}$. This new definition includes all the information from the eliminated nodes, which ensures that the reduced DBN gives the same results as the original DBN.

In principle, one could directly define this reduced DBN instead of the original DBN. However, because the effect of variables such as overburden or ground class is only implicit in this reduced model, the direct determination of the conditional probabilities in the reduced DBN is not straightforward.
![img-5.jpeg](img-5.jpeg)

Figure 6. DBN after elimination of nodes.

For the resulting network, due to the new links introduced in the elimination process, it becomes necessary to compute the conditional PMFs $p\left(f_{i} \mid q_{i}, r_{i}\right)$ and $p\left(t_{i} \mid q_{i}, r_{i}, f_{i}\right)$. The conditional PMF of failure mode $F_{i}$ can be calculated as (compare with Figure 4):

$$
\begin{aligned}
p\left(f_{i} \mid r_{i}, h_{i}\right) & =\sum_{G_{i}} p\left(f_{i}, g_{i} \mid r_{i}, h_{i}\right) \\
& =\sum_{G_{i}} p\left(f_{i} \mid g_{i}, h_{i}\right) \sum_{o_{i}} p\left(g_{i} \mid o_{i}, r_{i}\right) p\left(o_{i}\right)
\end{aligned}
$$

The conditional PMF of unit time $T_{i}$ is obtained as:

$$
p\left(t_{i} \mid r_{i}, h_{i}, f_{i}\right)=\frac{1}{p\left(f_{i}\right)} \sum_{G_{i}} p\left(f_{i}, g_{i} \mid r_{i}, h_{i}\right) \sum_{M_{i}} p\left(t_{i} \mid m_{i}, h_{i}\right) \sum_{E_{i}} p\left(m_{i} \mid e_{i}, g_{i}\right) p\left(e_{i}\right)
$$

# 4.3 Modified Frontier algorithm 

A modified version of the frontier algorithm is used for evaluating the DBN. The new algorithm is investigated and validated on an academic example in Annex 2. Because some random variables in the DBN have large numbers of states, direct application of the Frontier algorithm is inefficient. We therefore propose two modifications to the algorithm, which avoid defining large conditional probability tables: (a) the frontier is optimized by excluding some of the variables; this modification was originally proposed by Murphy (2002) under the name "interface algorithm"; (b) some steps of the original algorithm are replaced by computations of convolutions of conditional PMFs; to our knowledge, this modification has not been previously published. The new algorithm is computationally efficient; computations shown here were performed in Matlab and take in the order of 80 CPU seconds on a MacBook Pro with a 2.53 GHz Intel Core 2 Duo Processor, 4 GB 1067 MHz DDR3 RAM and Mac OS X v. 10.6.8. The computational efficiency in comparison with the original Frontier algorithm is presented in Annex 2.

In the following, we present one cycle of the modified Frontier algorithm, which advances the frontier from slice $i-1$, with corresponding joint PMF $p\left(z_{i-1}, r_{i-1}, t_{c u m, i-1}, n_{F, i-1}, h_{i-1}\right)$, to slice $i$, with corresponding joint PMF $p\left(z_{i}, r_{i}, t_{c u m, i}, n_{F, i}, h_{i}\right)$. As outlined in Section 2.1, the frontier is moved from slice $i-1$ to slice $i$ by sequentially adding nodes from slice $i$ and removing nodes from slice $i-1$ in the frontier. The individual steps are graphically documented in Fig. 7 and are described in the following.

![img-6.jpeg](img-6.jpeg)

Figure 7. Graphical documentation of one cycle of the Frontier algorithm for evaluation of the DBN of tunnel excavation processes. The grey nodes are those included in the frontier at a given step. Grey nodes with dashed line indicate the nodes that are operated in a particular step (i.e. nodes which are added or removed from the frontier in this step).

At the beginning of the cycle, the joint PMF $p\left(z_{i-1}, r_{i-1}, t_{c u m, i-1}, n_{F, i-1}, h_{i-1}\right)$ is available from the previous cycle. In the first step (a) of the cycle, the node $Z_{i}$ (the geotechnical zone in segment $i$ ) is added and node $Z_{i-1}$ is removed, as indicated in Fig. 7a. The corresponding computation is:

$$
\begin{gathered}
p\left(z_{i}, r_{i-1}, t_{c u m, i-1}, n_{F, i-1}, h_{i-1}\right)= \\
\sum_{Z_{i-i}} p\left(z_{i-1}, r_{i-1}, t_{c u m, i-1}, n_{F, i-1}, h_{i-1}\right) p\left(z_{i} \mid z_{i-1}\right)
\end{gathered}
$$

where $p\left(z_{i} \mid z_{i-1}\right)$ is obtained as described in sec. 3.1.
In the second step (b) of the cycle, the random variable rock class $R_{i}$ is added to the frontier and $R_{i-1}$ is removed, as depicted in Fig. 7b. The corresponding computation is:

$$
p\left(z_{i}, r_{i}, t_{c u m, i-1}, n_{F, i-1}, h_{i-1}\right)=
$$

$\sum_{R_{i-1}} p\left(z_{i}, r_{i-1}, t_{c u m, i-1}, n_{F, i-1}, h_{i-1}\right) p\left(r_{i} \mid r_{i-1}, z_{i}\right)$,
where $p\left(r_{i} \mid r_{i-1}, z_{i}\right)$ is obtained as described in sec. 3.1.
In the third step (c) of the cycle, the random variable human factor $H_{i}$ is added to the frontier and $H_{i-1}$ is eliminated, as shown in Fig. 7c. The corresponding computation is:

$$
\begin{gathered}
p\left(z_{i}, r_{i}, t_{c u m, i-1}, n_{F, i-1}, h_{i}\right)= \\
\sum_{H_{i-1}} p\left(z_{i}, r_{i}, t_{c u m, i-1}, n_{F, i-1}, h_{i-1}\right) p\left(h_{i} \mid h_{i-1}\right)
\end{gathered}
$$

The conditional probability $p\left(h_{i} \mid h_{i-1}\right)$ is defined by an identity matrix (see sec. 3.2). Because of this definition, the calculation from Eq. (12) can be skipped and the joint PMF can be obtained simply by replacing $h_{i-1}$ with $h_{i}$ in the known joint PMF $p\left(z_{i}, r_{i}, t_{c u m, i-1}, n_{F, i-1}, h_{i-1}\right)$.

In the fourth step (d) of the cycle, the random variable $N_{F, i}$, representing the number of failures, is added to the frontier and $N_{F, i-1}$ is removed. Since $N_{F, i}$ is defined conditional on the failure mode $F_{i}$, this random variable is also added to the frontier. The step is shown in Fig. 7d and the corresponding computation is:

$$
\begin{gathered}
p\left(z_{i}, r_{i}, t_{c u m, i-1}, n_{F, i}, h_{i}, f_{i}\right)= \\
\sum_{N_{F, i-1}} p\left(z_{i}, r_{i}, t_{c u m, i-1}, n_{F, i-1}, h_{i}\right) p\left(n_{F, i} \mid n_{F, i-1}, f_{i}\right) p\left(f_{i} \mid r_{i}, h_{i}\right)
\end{gathered}
$$

where $p\left(n_{F, i} \mid n_{F, i-1}, f_{i}\right)$ is computed as described in sec. 3.3 and $p\left(f_{i} \mid r_{i}, h_{i}\right)$ is obtained after the elimination of nodes according to sec. 4.2.

In order to complete the cycle, one could, in principle, perform the following two operations (corresponding to the fifth step shown in Fig. 7e). First, the random variable $T_{i}$, representing unit time, could be added and $F_{i}$ removed:

$$
\begin{gathered}
p\left(z_{i}, r_{i}, t_{c u m, i-1}, n_{F, i}, h_{i}, t_{i}\right)= \\
\sum_{F_{i}} p\left(z_{i}, r_{i}, t_{c u m, i-1}, n_{F, i}, h_{i}, f_{i}\right) p\left(t_{i} \mid q_{i}, r_{i}, f_{i}\right)
\end{gathered}
$$

Second, the cumulative costs $T_{\text {cum, } i}$ could be added, while $\mathrm{T}_{\text {cum, } i-1}$ and $T_{i}$ could be eliminated:

$$
\begin{aligned}
& p\left(z_{i}, r_{i}, t_{c u m, i}, n_{F, i}, h_{i}\right)= \\
& \sum_{T_{c u m, i-1}} \sum_{T_{i}} p\left(z_{i}, r_{i}, t_{c u m, i-1}, n_{F, i}, h_{i}, t_{i}\right) p\left(t_{c u m, i} \mid t_{c u m, i-1}, t_{i}\right)
\end{aligned}
$$

Because random variables $T_{\text {cum, } i-1}$ and $T_{\text {cum, } i}$ can have large numbers of states, computation of Eq. (15) puts high demands on computer memory, which can make exact computations infeasible. For this reason, an alternative solution that avoids this computation is developed in the following.

We exploit the fact that the cumulative time in segment $i$ is obtained as the sum $T_{\text {cum, } i}=$ $T_{\text {cum, } i-1}+T_{i}$, by using the convolution function to compute the distribution function of $T_{\text {cum, } i}$. If $T_{\text {cum, } i-1}$ and $T_{i}$ were independent random variables, the PMF of $T_{\text {cum, } i}$ could be computed as

$$
p_{T_{c u m, i}}(t)=\sum_{\tau} p_{T_{c u m, i-1}}(t-\tau) p_{T_{i}}(\tau)
$$

where the summation is over all states $\tau$ of $T_{i}$. This is the convolution function (illustrated in Fig. 5.), which is written in short notation as

$$
p_{T_{c u m, i}}(t)=p_{T_{c u m, i-1}} * p_{T_{i}}(t)
$$

$T_{\text {cum, } i-1}$ and $T_{i}$ are dependent and direct application of Eq. (17) is not possible. However, from the graphical structure of the DBN, it can be inferred that $T_{\text {cum, } i-1}$ and $T_{i}$ are independent for given values of $Z_{i}, R_{i}, Q_{i}$ and $F_{i}$. (This follows from the d-separation properties of the BN.) Making use of this conditional independence, we can write:

$$
p_{T_{c u m, i} \mid Z_{i}, R_{i}, H_{i}, F_{i}}(t)=p_{T_{c u m, i-1} \mid Z_{i}, R_{i}, H_{i}, F_{i}} * p_{T_{i} \mid R_{i}, H_{i}, F_{i}}(t)
$$

The conditional PMF of $T_{i}, p\left(t_{i} \mid r_{i}, q_{i}, f_{i}\right)$, is known from Eq. (9). Furthermore, from the joint PMF of step (d), Eq. (13), we obtain

$$
p\left(t_{c u m, i-1} \mid z_{i}, r_{i}, h_{i}, f_{i}\right)=\frac{\sum_{N_{F, i}} p\left(z_{i}, r_{i}, t_{c u m, i-1}, n_{F, i}, h_{i}, f_{i}\right)}{\sum_{T_{c u m, i-1}} \sum_{N_{F, i}} p\left(z_{i}, r_{i}, t_{c u m, i-1}, n_{F, i}, h_{i}, f_{i}\right)}
$$

The convolution operation in Eq. (18) is numerically efficient because it avoids the summation over the states of $T_{\text {cum, } i-1}$, which is necessary in the conventional approach (Eq. (15)). This reduces the number of necessary operations by a factor corresponding to the number of states of $T_{\text {cum, } i-1}$. Additionally, standard software like Matlab have optimized algorithms for computing the convolution function based on Fast Fourier Transform. The computation times of both algorithms are compared in Annex 2.

With $p\left(t_{c u m, i} \mid z_{i}, r_{i}, h_{i}, f_{i}\right)$ of Eq. (18), the final frontier shown in Fig. 7f is calculated from:

$$
p\left(z_{i}, r_{i}, t_{c u m, i}, n_{F, i}, h_{i}\right)=\sum_{F_{i}} p\left(t_{c u m, i} \mid z_{i}, r_{i}, h_{i}, f_{i}\right) p\left(z_{i}, r_{i}, n_{F, i}, h_{i}, f_{i}\right)
$$

with

$$
p\left(z_{i}, r_{i}, n_{F, i}, h_{i}, f_{i}\right)=\sum_{T_{c u m, i-1}} p\left(z_{i}, r_{i}, t_{c u m, i-1}, n_{F, i}, h_{i}, f_{i}\right)
$$

where $p\left(z_{i}, r_{i}, t_{c u m, i-1}, n_{F, i}, h_{i}, f_{i}\right)$ is the joint PMF of step d.
The full DBN is evaluated by repeatedly applying the cycle described above, starting at $i=2$ and ending at the last slice $i=1$. To initiate the calculation, the frontier in slice 1 must be known. It is:

$$
\begin{gathered}
p\left(z_{1}, r_{1}, t_{1}, n_{F, 1}, h_{1}\right)= \\
p\left(z_{1}\right) p\left(r_{1} \mid z_{1}\right) p\left(h_{1}\right) \sum_{F_{1}} p\left(f_{1} \mid r_{1}, h_{1}\right) p\left(n_{F, 1} \mid f_{1}\right) p\left(t_{1} \mid r_{1}, f_{1}, h_{1}\right)
\end{gathered}
$$

Because $T_{\text {cum, } 1}=T_{1}$, the joint PMF of the initial frontier is obtained simply by replacing $t_{1}$ with $t_{\text {cum, } 1}$ in the above expression.

# 4.4 Updating 

If observations of the tunnel construction performance are available, the predictions can be updated according to the description in sec. 2.1. Commonly, the rock class, cumulative time and number of failures for individual segments can be directly observed as the construction proceeds. The observations in segment $i$ are denoted as $R_{i}=r_{o b s, i}, T_{\text {cum }, i}=$

$t_{o b s, i}$ and $N_{F, i}=n_{o b s, i}$. To include the evidence in the Frontier algorithm, the joint PMF computed according to Eq. (20), $p\left(z_{i}, r_{i}, t_{c u m, i}, n_{F, i}, h_{i}\right)$, is replaced by the conditional PMF

$$
\begin{aligned}
& p\left(z_{i}, r_{i}, t_{c u m, i}, n_{F, i}, h_{i} \mid r_{o b s, i}, t_{o b s, i}, n_{o b s, i}\right) \\
& =\left\{\begin{array}{ll}
\alpha \cdot p\left(z_{i}, r_{i}, t_{c u m, i}, n_{F, i}, h_{i}\right), & \text { for } r_{i}=r_{o b s, i}, t_{c u m, i}=t_{o b s, i}, n_{F, i}=n_{o b s, i} \\
0, & \text { else }
\end{array},\right.
\end{aligned}
$$

where $\alpha$ is a normalization constant to ensure that the sum over all states of $p\left(z_{i}, r_{i}, t_{c u m, i}, n_{F, i}, h_{i} \mid r_{o b s, i}, t_{o b s, i}, n_{o b s, i}\right)$ is equal to one. This conditional PMF is then used as the input for the next cycle of the Frontier algorithm.

# 4.5 Calculation of total time 

The total time $T_{\text {tot, } i}$ is the sum of the cumulative time $T_{\text {cum, } i}$ and delays caused by extraordinary events $T_{\text {extra, } i}: T_{\text {tot, }, i}=T_{\text {cum, }, i}+T_{\text {extra, }, i}$. For given value of $N_{F, i}, T_{\text {cum, }, i}$ and $T_{\text {extra, }, i}$ are independent. Therefore, the distribution of $T_{\text {tot, }, i}$ can be computed via the convolution function as:

$$
p_{T_{t o t, i} \mid N_{F, i}}(t)=p_{T_{c u m, i} \mid N_{F, i}} * p_{T_{e x t r a, i} \mid N_{F, i}}(t)
$$

The conditional PMF $p_{T_{c u m, i} \mid N_{F, i}}$ is obtained from the joint PMF $p\left(z_{i}, r_{i}, t_{c u m, i}, n_{F, i}, q_{i}\right)$, which results from the Frontier algorithm, as follows:

$$
p\left(t_{c u m, i} \mid n_{F, i}\right)=\frac{p\left(t_{c u m, i, n_{F, i}}\right)}{p\left(n_{F, i}\right)}=\frac{\sum Q_{i} \sum z_{i} \sum R_{i} p\left(z_{i}, r_{i}, t_{c u m, i}, n_{F, i}, h_{i}\right)}{\sum_{T_{c u m, i}} \sum Q_{i} \sum z_{i} \sum R_{i} p\left(z_{i}, r_{i}, t_{c u m, i}, n_{F, i}, h_{i}\right)}
$$

$p_{T_{\text {extra, } i} \mid N_{F, i}}$ is evaluated following Eq. (6).

## 5 Numerical example

The DBN model is applied to the excavation of a section of the Suncheon-Dolsan road tunnel in South Korea. The case study was originally presented in Min (2003) and Min et

al. (2003), where the Decision Aids for Tunneling (DAT) model was applied for probabilistic prediction of construction time and costs.

The modeled tunnel section is a 610 m long tunnel tube with two lanes, which is excavated with a conventional tunneling method (ITA 2009). A scheme of the tunnel tube is depicted in Fig. 8.
![img-7.jpeg](img-7.jpeg)

Figure 8. Scheme of the modeled tunnel excavation.

A simplified version of the proposed DBN model, without consideration of extraordinary events, human factor $H_{i}$ and zone $Z_{i}$, was previously applied to this tunnel in Špačková \& Straub (2011), to validate the DBN model by comparing its results with those of the DAT model (Min 2003). In Špačková \& Straub (2011), the variable human factor $H_{i}$ is called quality $Q_{i}$, its meaning and modeling is however the same.

# 5.1 Parameters of the DBN model 

For the application of the DBN model, the tunnel is discretized in segments of length $\Delta l=5 \mathrm{~m}$.

The description of the geotechnical conditions (zone $Z_{i}$, rock class $R_{i}$, overburden $O_{i}$ and ground class $G_{i}$ ) as well as of some variables describing the construction process (geometry $E_{i}$ and construction method $M_{i}$ ) are taken from Min (2003). An example of a conditional probability table, describing the rock class in slice $i, R_{i}$, is show in Table 2.

The rock class definition is based on the classification utilized for the individual tunnel and it combines electrical resistivity, Rock Mass Rating (RMR) and Q-value. For further details on geotechnical classification we refer to (Singh \& Goel 1999).

Table 2. Conditional probability table of rock class in zone 2 for a DBN with slice length $\Delta l=5 m$. For example, the conditional probability of rock class in slice $i$ being $R_{i}=I I I$, given that the rock class in slice $i-1$ is $R_{i-1}=I$ and the zone in slice $i$ is $Z_{i}=2$, is $\operatorname{Pr}\left(R_{i}=\operatorname{III} \mid R_{i}=I, Z_{i}=2\right)=0.134$.


The conditional probability distributions $p\left(t_{i} \mid m_{i}, h_{i}\right)$ of unit time $T_{i}$ were determined based on data recorded during excavation of a Czech tunnel. An example of the utilized non-parametric distributions of $T_{i}$ for given construction methods $M_{i}$ and human factor $H_{i}=$ "neutral" is shown in Fig. 9. The means and standard deviations of $T_{i}$ conditional on human factor $H_{i}$ and construction method $M_{i}$, as applied in the numerical example, are summarized in Table 3.
![img-8.jpeg](img-8.jpeg)

Figure 9. PDF of unit time $T_{i}$ for excavation of a segment with length of $\Delta l=5 m$, on the condition of neutral human factor $H_{i}$ and for selected construction methods $M_{i}$

Table 3. Means and standard deviations of unit time $T_{i}$ [in days] for different human factors and construction methods, for slices of length $\Delta l=5 \mathrm{~m}$. The description of construction methods is taken from Min et al. (2008).


The discretization interval for $T_{i}$ and $T_{\text {cum, } i}$, as discussed in Section 4.1, is selected as $t_{\text {int }}=0.5$ days.

The conditional probability of an extraordinary event (a failure) in segment $i, p\left(f_{i} \mid g_{i}, h_{i}\right)$, is estimated based on experience from the Czech Republic, where the number of tunnel collapses is known (e.g. Aldorf, 2010) and can be related to the total length of constructed tunnels (Barták, 2007). The rate of failures is dependent on human factor $H_{i}$ and ground class $G_{i}$, and the estimated values [in number of failures per m] are assessed to range from $2.210^{-4}$ to $6.710^{-3}$ for unfavourable influence of human factor, from $1.110^{-4}$ to $3.310^{-3}$ for neutral influence of human factor and from $5.610^{-5}$ to $1.710^{-3}$ for favourable influence of human factor. The estimates were not validated with data from other countries, they should not be taken as generally applicable.

The determination of the probability distribution of $H_{i}$ will generally be based on a subjective assessment. For the purpose of this study, we apply two alternative prior distributions, to investigate the influence of this choice. The utilized probabilistic models are:

H(a): $\operatorname{Pr}\left(H_{i}={ }^{\prime}\right.$ unfavourite $\left.{ }^{\prime}\right)=0.3 \quad, \quad \operatorname{Pr}\left(H_{i}={ }^{\prime}\right.$ neutral $\left.{ }^{\prime}\right)=0.6 \quad, \quad \operatorname{Pr}\left(H_{i}=\right.$ 'favourite') $^{\prime}=0.1$.
$\mathrm{H}(\mathrm{b}): \operatorname{Pr}\left(H_{i}={ }^{\prime}\right.$ unfavourite $\left.{ }^{\prime}\right)=0.33, \operatorname{Pr}\left(H_{i}={ }^{\prime}\right.$ neutral $\left.{ }^{\prime}\right)=0.33, \operatorname{Pr}\left(H_{i}=\right.$ ${ }^{\prime}$ favourite $\left.{ }^{\prime}\right)=0.33$.

The probability distribution of delay caused by one extraordinary event $p\left(\mathrm{t}_{\text {extra, } \mathrm{i}} \mid N_{F, i}=1\right)$ was derived from (Sousa 2010). A shifted exponential distribution with minimum at 15 days, mean value 175 days and standard deviation 160 days was fitted to the data given in that reference and, in discretized form, applied in the example.

# 5.2 Bayesian updating of the probabilistic estimate with performance data 

To demonstrate the ability of the DBN for updating the prediction as the construction proceeds, we introduce hypothetical performance data. These are from the first 120 m of the tunnel and include observed rock class $R_{i}$, number of failures $F_{\text {cum, } i}$ and cumulative time $T_{\text {cum, } i}$ at each segment.

It is assumed that no failure occurs in this section and that the cumulative time is slightly higher (up to 10 per cent) than the mean prior prediction. The predicted and observed cumulative time $T_{\text {cum, } i}$ is shown in Fig. 10. Rock class II is found in the first 49 meters, rock class III in the next 41 meters and rock class IV in the last 30 meters of the section.
![img-9.jpeg](img-9.jpeg)

Figure 10. Performance data used for updating the predictions: Observed excavation time in the first 120 m of the tunnel, together with the predicted excavation time.

### 5.3 Results without observations

The resulting probabilistic estimates of construction time for the whole tunnel are presented in Fig. 11 and 12. Fig. 11 shows the prediction without consideration of

extraordinary events, Fig. 12 includes the extraordinary events. In both figures, results are shown separately for the two a-priori probabilistic models of human factor $H_{i}$. In addition, results for a fixed human factor $H_{i}=$ 'neutral' are shown, which correspond to a model that does not consider human factor as a random variable, i.e. which neglects the uncertainty in the model class. By comparing the results for fixed and uncertain human factor, the effect of introducing $H_{i}$ can be observed: The standard deviation of the construction time estimate increases due to the uncertainty in $H_{i}$. If the average performance (e.g. advance rate) is uncertain, the overall uncertainty of the total construction time is higher than in the case when this average value is known and only the variability of the performance is considered (which is the case of fixed human factor $H_{i}=$ 'neutral').

By comparing Fig. 11 and 12, the significant impact of extraordinary events on the expected construction time and, in particular, on the uncertainty in the construction time are evident. The resulting distributions of total excavation time are strongly skewed towards larger construction times.
![img-10.jpeg](img-10.jpeg)

Figure 11. Prediction of excavation time $T_{\text {cum }}$ without consideration of extraordinary events, for two a-priori models of human factor and for the case of fixed human factor.

![img-11.jpeg](img-11.jpeg)

Figure 12. Prediction of total excavation time $T_{\text {tot }}$ with consideration of extraordinary events, for two a-priori models of human factor and for the case of fixed human factor.

# 5.4 Results for the updating with performance data 

The updated estimates of cumulative time $T_{\text {cum }}$ (excluding extraordinary events) and total time $T_{\text {tot }}$ (including extraordinary events) for the whole tunnel, conditional on the observations described in Sec. 5.2, are shown in Fig. 13 and Fig. 14. They are obtained by updating the PMF at all slices with observations (segments $i=1,2, \ldots, 24$ ), according to Eq. (23). For comparison, the estimates computed without the observation data are also provided (corresponding to the results shown in Fig. 10 and Fig. 11). The updated estimates are identical for the two prior models of human factor $H_{i}$, because the observed performance strongly indicates that the human factor is $H_{i}=$ 'unf avourable'. This can be observed from Fig. 15, which shows the updated probability of $H_{i}$ as the construction proceeds. This probability is computed by marginalizing all other variables from the conditional joint PMF obtained according to Eq. (23).

The updated estimate of $T_{\text {cum }}$ (which excludes extraordinary events) shown in Fig. 13 exhibits a lower standard deviation, because there is no more uncertainty in $H_{i}$, i.e. in the appropriate probabilistic model of unit time $T_{i}$. However, the standard deviation of the updated total construction time $T_{\text {tot }}$ (including extraordinary events) is higher, because the resulting $H_{i}=$ "unf avourable" implies an increased probability of failure (extraordinary events).

![img-12.jpeg](img-12.jpeg)

Figure 13. Updated prediction of excavation time $T_{\text {cum }}$ (without consideration of extraordinary events) for Dolsan A tunnel based on observations made during excavation of 120 m of the tunnel.
![img-13.jpeg](img-13.jpeg)

Figure 14. Updated prediction of excavation time $T_{\text {tot }}$ (with consideration of extraordinary events) for Dolsan A tunnel based on observations made during excavation of 120 m of the tunnel.

![img-14.jpeg](img-14.jpeg)

Figure 15. Updated prediction of human factor $H_{i}$ for Dolsan A tunnel based on observations made during excavation of 120 m of the tunnel.

# 6 Discussion 

The proposed DBN model and computational algorithm for tunnel excavation processes is a step towards a quantitative assessment of uncertainties that is needed to support the optimization of decisions in infrastructure projects. The significant uncertainty in estimates of construction cost and time observed in practice is not fully reflected in most existing models. In our view, a main reason for this underestimation is the assumption of independence among the performances at different phases of the construction. This observation was also made recently by Yang (2007) and Moret \& Einstein (2011). In the proposed DBN model, we represent correlation among the performance at different phases of the construction through the random variable "Human factor", which is assumed to represent the overall quality of the planning and execution of the construction process and other external factors influencing the entire project. As observed in Figure 10, the inclusion of this variable leads to an increased variance of the estimate of construction time. As stated earlier, the variable "Human factor" can also be interpreted as a model uncertainty, which reflects the fact that the applied probabilistic models of tunnel excavation performance are based on a limited amount of data or expert estimates. This second interpretation has the advantage of not being judgmental and therefore more

easily acceptable in practice. As we show in the example application (Figure 15), the DBN model facilitates to update the estimate of the "Human factor", i.e. as the construction proceeds, the observed performance is used in an automated manner to learn the model and to improve the prediction for the remaining construction.

Another main reason for the underestimation of the uncertainty in construction time and cost is that most existing models do not account for possible extraordinary events, which can be considered as failures of the construction process. These events are included in the DBN model,. By providing the stakeholders with the full distribution of project time (and cost), as in Fig. 11, the risk associated with extraordinary events can be more effectively communicated and included in the decision making process than with the traditional approach of considering only expected values.

The presented Frontier algorithm for evaluating the DBN is computationally efficient and applicable in practice. It is flexible in including observations to update the model. Besides updating the model with performance data and the observed geology of the excavated tunnel sections, as shown in Sec. 5.2 and Sec. 5.4, other types of observations, e.g. borehole tests, can be used. For some of these observations, an extension of the presented algorithm is required, to include the so-called backward pass (e.g. Murphy 2002), which allows one to update the probabilistic model at segment $i$ with information from segments $j>i$.

The proposed DBN approach is flexible with regard to changes in the model. One aspect that should be revised in future work is the modeling of the variable $M_{i}$ to more realistically reflect changes of construction technology during the excavation process. The present model assumes full flexibility in changing the construction patterns based on changes in geology. In reality, the construction pattern is not modified so frequently, as this is connected with additional time and costs. This effect is even more pronounced when mechanized excavation is used. A second aspect that should be addressed is the modeling of costs. As stated earlier, the variable time can be replaced by the variable cost to obtain a cost estimate. However, for a combined modeling, an extension of the DBN model is needed to account for the dependence of construction costs on construction time.

In probabilistic assessment of construction time and costs, the model parameters (especially advance rates and unit costs) should ideally be based on analyses of data from

past projects. Expert estimates are reliable for the assessment of mean values, but not for determining the variances and the probabilistic models. Furthermore, determination of failure probabilities and associated delays should be based on an extensive analysis of information from past projects. The analysis of tunnel construction data is a complex task, because the local conditions and design and construction procedures differ in different countries and projects. Therefore, further research is needed to provide a more robust information basis for probabilistic modeling. The understanding of the benefits of probabilistic modeling among stakeholders should be raised, which should lead them to more systematically manage and statistically analyze data from available projects.

# 7 Conclusion 

A model for probabilistic prediction of tunnel construction performance using Dynamic Bayesian Networks (DBN) is introduced. It allows to realistically quantify the uncertainties connected with construction time, by including correlations in the construction process and the risk of extraordinary events (tunnel collapses and other major problems) in the model.

The DBN adopts the modeling of uncertain geotechnical conditions from previous models (DAT model) but modifies the representation of uncertainties inherent in the construction process itself. The dependencies that result from the influence of human, organizational and external factors are addressed by introducing a random variable "Human factor" into the model. The performance variables (unit time, probability of failures) are defined conditionally on the human factor.

An algorithm for the efficient evaluation of the DBN was described. We modified the existing Frontier algorithm to better address specific features of the proposed DBN. The modification enables one to deal with discrete random variables with large numbers of outcomes states that result from the discretization of continuous random variables such as time or cost. We exploited the fact that these variables are defined as cumulative sums of other random variables in the DBN and that the probability distribution of a sum of two random variables can be efficiently calculated by means of convolution functions.

The DBN model was applied to estimation of the excavation time of a 610 m long tunnel. Bayesian updating of the estimate with the observed construction performance was also shown. As demonstrated by this application, the DBN model is able to capture the overall uncertainty of estimates of tunnel construction time. Some data from real tunnel projects were used in the presented application, but more extensive analysis of data from past projects (combined with expert opinion) should be performed, using the DBN as a model framework.

# Acknowledgement 

The first author is funded by project No. TA01030245 of the Technology Agency of the Czech Republic, project No. 103/09/2016 of the Czech Science Foundation and project No. 1M0579 (CIDEAS research centre) of the Ministry of Education, Youth and Sports of the Czech Republic. Additional support by DAAD and Bayhost is gratefully acknowledged.

# Annex 1 - Probabilistic definition of selected nodes in the DBN 

## Zone $Z$

The variable represents the position of a tunnel segment in quasi-homogenous geotechnical zones along the tunnel axis. The uncertainty in the location of the boundary $B_{j}$ between zones $j$ and $j+1$ is described by the cumulative probability distribution function (CDF) of the location of the boundary, $F_{B j}(x)$,. To establish the conditional PMF of $Z_{i}$, let $\operatorname{Pr}\left(Z_{i}=j\right)$ denote the probability that segment $i$ is part of zone $j$ and $\operatorname{Pr}\left(Z_{i-1}=j\right)$ the probability that segment $i-1$ lies in zone $j$. Assuming that a segment $i$ can only be in either zone $j$ or zone $j+1$, the probability of the $i$ th segment being in zone $j$ is calculated as

$$
\operatorname{Pr}\left(Z_{i}=j\right) \approx 1-F_{B j}\left(i \Delta l-\frac{\Delta l}{2}\right)
$$

where $\Delta l$ is the length of the segment represented by one slice of the DBN.
The conditional probabilities defining the variable $Z_{i}$ (i.e. the values in the CPT) are:

$$
\begin{gathered}
\operatorname{Pr}\left(Z_{i}=j \mid Z_{i-1}=j\right)=\frac{\operatorname{Pr}\left(Z_{i}=j \cap Z_{i-1}=j\right)}{\operatorname{Pr}\left(Z_{i-1}=j\right)}=\frac{\operatorname{Pr}\left(Z_{i}=j\right)}{\operatorname{Pr}\left(Z_{i-1}=j\right)} \\
\operatorname{Pr}\left(Z_{i}=j+1 \mid Z_{i-1}=j\right)=1-\operatorname{Pr}\left(Z_{i}=j \mid Z_{i-1}=j\right)=1-\frac{\operatorname{Pr}\left(Z_{i}=j\right)}{\operatorname{Pr}\left(Z_{i-1}=j\right)} \\
\operatorname{Pr}\left(Z_{i}=j \mid Z_{i-1}=j+1\right)=0
\end{gathered}
$$

The second equality in Eq. (27) as well as Eq. (29) follow from the fact that segment $i$ can only be in zone $j$ if segment $i-1$ is also in zone $j$.

If the segment $i$ can be in more than two different zones (e.g. in zone $j-1, j$ and $j+1$ ), Eq. (26) - (29) must be extended accordingly.

# Rock class $R$ 

The rock class describes the geotechnical conditions along the tunnel axis. In a zone $Z_{i}=j$ it is modeled as a Markov process. Parameters of the Markov process are obtained from experts in form of the average length $l_{k}^{(j)}$ for which the rock class remains in state $k$ and transition probabilities $p_{k m}^{(j)}$, i.e. probability that, in case of a change, rock class $k$ is followed by rock class $m$ (Chan 1981).

In the DBN model, the Markov process is discretized into a Markov chain, i.e. it is transformed to a discrete space represented by slices of the DBN corresponding to segments of length $\Delta l$. Assuming that changes in rock class occur as a Poisson process, the conditional probabilities of rock class in segment $i, R_{i}$, are derived from the parameters of the continuous Markov process as follows:

$$
\begin{aligned}
& \operatorname{Pr}\left(R_{i}=k \mid R_{i-1}=k, Z_{i}=j\right)=\exp \left(-\frac{\Delta l}{l_{k}^{(j)}}\right) \\
& \operatorname{Pr}\left(R_{i}=m \mid R_{i-1}=k, Z_{i}=j\right)=p_{k m}^{(j)}\left[1-\exp \left(-\frac{\Delta l}{l_{k}^{(j)}}\right)\right], k \neq m
\end{aligned}
$$

Note that due to the dependence introduced through the parent variables $Z_{i}$, the rock class is not a Markov process. (It is a Markov process only conditional on zone $Z_{i}$.)

## Failure mode $F$

Variable failure mode $F_{i}$ represents the possible occurrence of an extraordinary event in segment $i$. In the presented application it can be in one of two states: "failure" or "no failure". It is defined conditionally on ground class $G_{i}$ and human factor $H_{i}$. The conditional failure rate $\lambda_{F_{i} \mid G_{i}, H_{i}}$ for given ground class and human factor can be determined from historic data. Assuming that failures occur as a Poisson process for given $H_{i}$ and $G_{i}$, the conditional probability of failure mode $F_{i}$ within a section of length $\Delta l$ can be approximated by:

$$
\operatorname{Pr}\left(F_{i}=\text { "no failure" } \mid G_{i}, H_{i}\right) \approx \exp \left(-\lambda_{F_{i} \mid G_{i}, H_{i}} \Delta l\right)
$$

$$
\operatorname{Pr}\left(F_{i}=\text { "failure" } \mid G_{i}, H_{i}\right) \approx 1-\exp \left(-\lambda_{F \mid G_{i}, H_{i}} \Delta i\right)
$$

# Number of failures $N_{F}$ 

Number of failures $N_{F, i}$ represents the total number of failures from the beginning of the up to the segment $i$. With $m_{F}$ being the maximal number of failures to be considered (where state $m_{F}$ represents $m_{F}$ or more failures), the conditional probabilities are:

$$
\begin{aligned}
& \operatorname{Pr}\left(N_{F, i}=j \mid N_{F, i-1}=j-1, F_{i}=\text { "failure" })=1, \text { for } j=\left\{1, \ldots, m_{F}\right\}\right. \\
& \operatorname{Pr}\left(N_{F, i}=j \mid N_{F, i-1}=j, F_{i}=\text { "no failure" })=1, \text { for } j=\left\{0, \ldots, m_{F}\right\}\right. \\
& \operatorname{Pr}\left(N_{F, i}=m_{F} \mid N_{F, i-1}=m_{F}, F_{i}=\text { "failure" })=1\right.
\end{aligned}
$$

For all other conditional probabilities it holds

$$
\operatorname{Pr}\left(N_{F, i} \mid N_{F,(i-1)}, f_{i}\right)=0
$$

# Annex 2 - Validation of modified Frontier algorithm 

In this annex, a simple DBN is evaluated using the original Frontier algorithm (FA) and the modified Frontier algorithm (MFA). The example is applied in order to validate the proposed MFA and to compare its computational performance with that of the original FA. The utilized sample DBN is depicted in Fig. 16. Each slice of the DBN consists of three random variables. Variable $V_{i}$ has two states, $m_{V}=2$, and is defined conditionally on $V_{i-1}$. The conditional probability table (CPT) of this random variable is shown in Table 4.
![img-15.jpeg](img-15.jpeg)

Figure 16. Sample DBN calculated with FA and MFA.

Table 4. Conditional probability table (CPT) of random variable $V_{i}$.


The variable $W_{i}$ is defined as a Normal distributed random variable conditional on $V_{i}$ with parameters as given in Table 5. For the application of the FA and MFA, the variable $W_{i}$ must be discretized according to the procedure described in sec. 4.1. Here, the variable is discretized into $m_{W}=13$ states: $0,1, \ldots 12$.

Table 5. Parameters of the Normal distributed variable $W_{i}$ for given $V_{i}$


The variable $X_{i}$ is defined as the sum of $X_{i-1}$ and $W_{i}$. The interest is in calculating the PDF of variable $X_{I}=\sum_{i=1}^{i=I} W_{i}$, where $I$ is the number of slices in the DBN.

# Frontier algorithm (FA) 

Prior to the application of the FA, we eliminate the variables $W_{i}$, since they do not have links to nodes in neighbouring slices. Elimination of these nodes can be understood as a pre-processing of the DBN, reducing the computational demand during application of the FA. The elimination of $W_{i}$ is performed for the whole DBN at once, variable $X_{i}$ is then defined directly on $V_{i}$ and on $X_{i-1}$ :

$$
p\left(x_{i} \mid v_{i}, x_{i-1}\right)=\sum_{W_{i}} p\left(w_{i} \mid v_{i}\right) p\left(x_{i} \mid w_{i}, x_{i-1}\right)
$$

where $p\left(w_{i} \mid v_{i}\right)$ is known from the discretization process of $W_{i}$ and $p\left(x_{i} \mid w_{i}, x_{i-1}\right)=$ $\operatorname{Pr}\left(X_{i}=x_{i} \mid W_{i}=w_{i}, X_{i-1}=x_{i-1}\right)$ takes value 1 for $x_{i}=x_{i-1}+w_{i}$ and value 0 otherwise. The number of states of $X_{i}$ is $m_{X}=I\left(m_{W}-1\right)+1$.

One cycle of the FA, i.e. moving the Frontier from slice $i-1$ to slice $i$, is shown in the following. First, the variable $V_{i}$ is added and $V_{i-1}$ removed from the Frontier:

$$
p\left(v_{i}, x_{i-1}\right)=\sum_{V_{i-1}} p\left(v_{i} \mid v_{i-1}\right) p\left(v_{i-1}, x_{i-1}\right)
$$

where $p\left(v_{i} \mid v_{i-1}\right)$ is defined in Table 4 and $p\left(v_{i-1}, x_{i-1}\right)$ is the joint PMF known from previous cycle of the FA.

Second, the variable $X_{i}$ is added and $X_{i-1}$ removed from the Frontier:

$$
p\left(v_{i}, x_{i}\right)=\sum_{X_{i-1}} p\left(x_{i} \mid v_{i}, x_{i-1}\right) p\left(v_{i}, x_{i-1}\right)
$$

where $p\left(x_{i} \mid v_{i}, x_{i-1}\right)$ and $p\left(v_{i}, x_{i-1}\right)$ are known from Eq. (38) and (39), respectively. Eq. (40) represents the most demanding computational step in the algorithm. The computation of this equation of the DBN requires $O\left(m_{X}{ }^{2} \times m_{V}\right)$ time in the $i$ th slice. The evaluation the whole DBN with $I$ slices therefore requires $O\left(I \times m_{X}{ }^{2} \times m_{V}\right)=$ $O\left(I \times\left[I\left(m_{W}-1\right)+1\right]^{2} \times m_{V}\right)$ time. It is evident that the computation time increases

exponentially with the number of states of the variable $W, m_{W}$, and with the number of slices of the DBN, $I$.

# Modified Frontier algorithm (MFA) 

One cycle of the MFA is presented in the following. First, variable $V_{i}$ is added and $V_{i-1}$ is removed from the Frontier according to Eq. (39). Second, the PMF of $X_{i}$ is calculated using convolution (analogously to Eq. (16) and (18)):

$$
p_{X_{i} \mid V_{i}}(x)=p_{X_{i-1} \mid V_{i}} * p_{W_{i} \mid V_{i}}(x)=\sum_{\tau} p_{X_{i-1} \mid V_{i}}(x-\tau) p_{W_{i} \mid V_{i}}(\tau)
$$

where $p_{X_{i-1} \mid V_{i}}=p\left(x_{i-1} \mid v_{i}\right)=p\left(v_{i}, x_{i-1}\right) / p\left(v_{i}\right), p\left(w_{i} \mid v_{i}\right)$ is known from the discretization of variable $W_{i}$ and the summation is over all states $\tau$ of $W_{i}$. Finally, the joint PMF describing the Frontier in slice $i$ is calculated as $p\left(v_{i}, x_{i-1}\right)=p\left(x_{i-1} \mid v_{i}\right) p\left(v_{i}\right)$. The number of states of $X_{i}$ is increasing in each slice of the DBN; it is $m_{X, i}=i\left(m_{W}-1\right)$ for $i=1,2, \ldots I$. The most demanding computational step of the MFA is the calculation of Eq. (41), which in the $i$ th slice of the DBN requires $O\left(m_{V} \times m_{X, i} \times m_{W}\right)$ time. For computation of the convolution, the Fast Fourier Transform (FFT) is commonly used (Walker 1996). With FFT, the calculation of the $i$ th slice of the DBN requires $O\left(m_{V} \times\right.$ $\left.m_{X, i} \log \left(m_{X, i}\right)\right.$ time and evaluation of the whole DBN with $I$ slices requires $O\left(m_{V} \sum_{i=1}^{I} m_{X, i} \log m_{X, i}\right)=O\left(m_{V} \sum_{i=1}^{I} i\left(m_{W}-1\right) \log \left[i\left(m_{W}-1\right)\right]\right) \quad$ time (Walker 1996).

## Results

Computations are performed for the DBN with varying number of slices $I$. The computation times depicted in Fig. 17 show the theoretical computation time estimated based on the number of performed operations as presented above and the observed time of computations performed in Matlab on the computer specified in sec. 4.3. The time needed for evaluation of the DBN with only $I=100$ slices is almost 1000 times higher with the original FA than with the MFA. The observed increase in computation time with the number of cycles is lower than the one estimated above. The likely reason for this is that the FFT algorithm implemented in Matlab is more efficient than the estimate given above (which represents a general upper bound).

![img-16.jpeg](img-16.jpeg)

Figure 17. Computation time for evaluation of the sample DBN with different number of slices, 1: comparison of FA and MFA.

A comparison of the mean and standard deviation of $X_{I}$ computed with FA and MFA with the exact analytical solution is given in Table 5. FA and MFA give exactly the same results, which differ slightly from the analytical results due to the small discretization errors.

Table 5. Comparison of $X_{I}$ for $I=10$ and $I=100$ computed with FA and MFA with exact analytical solution.
