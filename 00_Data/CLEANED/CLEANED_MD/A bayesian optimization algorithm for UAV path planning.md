# A BAYESIAN OPTIMIZATION ALGORITHM FOR UAV PATH PLANNING 

X. Fu , X. Gao and D. Chen<br>Northwestern Polytechnical University, Xi'an 710072, China

London South Bank University, London SE1 0AA, UK


#### Abstract

A Bayesian optimization algorithm (BOA) for unmanned aerial vehicle (UAV) path planning is presented, which involves choosing path representation and designing appropriate metric to measure the quality of the constructed network. Unlike our previous work in which genetic algorithm (GA) was used to implement implicit learning, the learning in the proposed algorithm is explicit, and the BOA is applied to implement such explicit learning by building a Bayesian network of the joint distribution of solutions. Experimental results demonstrate that this approach can overcome some drawbacks of other path planning algorithms. It is also suggested that the learning mechanism in the proposed approach might be suitable for other multivariate encoding problems.


Key words: UAV, path planning, Bayesian network, genetic algorithm, Bayesian optimization algorithm

## 1. INTRODUCTION

Flight path planning is a part of unmanned aerial vehicle (UAV) mission planning, and has received a lot of research attention [1] [2]. In essence, flight path planning is ultimately responsible for the generation of a trajectory in space which, when followed, maximizes the likelihood of the UAV completing its assigned tasks. However, most previous approaches have their drawback. For example, the planning result needs to be optimized further to make it flyable to UAV [2], or the algorithm might get stuck in

local minima [1]. In this paper, we propose an algorithm that can overcome these drawbacks.

In the presented algorithm, an initial set of path genotype strings will be generated randomly. From the current population, the better promising set of strings will be used for building a Bayesian network of the joint distribution of solutions. Subsequently, another set of path genotype strings will be generated in terms of the joint distribution, some of which will replace previous strings based on fitness selection. If stopping conditions are not satisfied, the constructed Bayesian network will be updated again using the current set of promising path genotype strings.

# 2. BOA FOR PATH PLANNING 

This section discusses the proposed Bayesian optimization algorithm for path planning, including genetic representation, chromosome decoding, and multivariate $K 2$ metric for measuring the quality of the constructed Bayesian network. For a detailed description of the UAV path planning problem and the BOA see, for example, [1] [3] [4] [5].

### 2.1 Genetic Representation

In the presented algorithm, a chromosome consists of different sequences of positive integers that represent a sequence of speed and heading transitions at discrete times $\left\{t_{k}, k=0,1 \ldots n\right\}$, respectively. The possible transitions, assumed to be triggered at the start of each $t_{k}$ interval, are listed in Table 1, where $\Delta u$ and $\Delta \varphi$ denote increment in velocity and heading of the UAV, respectively. Note that the ordering of the transitions in Table 1 is arbitrary and the transitions mean that all turns are made at the maximum possible turn rate $\dot{\varphi}_{\text {max }}$ and all accelerations/decelerations are made at the maximum value $a_{\text {max }}$. This corresponds to aggressive maneuvering of the UAV.

Table 1. Genetic representation


Thus, the $j^{\text {th }}$ individual of a population can be expressed as a sequence of transitions that reflect the nature of changes in the motion state to be initiated at time instant $k^{\text {th }}$ :
$\vec{P}^{j}=\left[\begin{array}{lllll}I_{1} & I_{2} & \ldots & I_{\ell}\end{array}\right]$

where $I_{k}$ indicates the type of change to be initiated at sampling interval $k^{t h}$, and ranges from 1 to 9 in our case.

# 2.2 Chromosome Decoding 

Given a sequence of transitions in speed and heading as discussed above, it is then necessary to generate a corresponding expected trajectory for the flight. This trajectory is typically required for evaluating the performance of a trial solution. In a 2-dimensional case, given a constant acceleration and turn rate as defined by the transition rules in Table 1, the motion of the UAV over an interval is described by the equations:

$$
\begin{aligned}
& u[k+1]=u[k]+\Delta u \\
& \varphi[k+1]=\varphi[k]+\Delta \varphi \\
& x[k+1]=x[k]+u[k+1] \cos (\varphi[k+1]) \\
& y[k+1]=y[k]+u[k+1] \sin (\varphi[k+1])
\end{aligned}
$$

where $u$ is the UAV velocity with $u_{\min } \leq u \leq u_{\max }, \varphi$ is the UAV heading with $|\varphi| \leq \varphi_{\max }, \Delta u$ and $\Delta \varphi$ are the inputs, and $(x, y)$ are inertial UAV position coordinates.

The rationale for using the kinematics model is based on the assumption that there exist inner and outer loop navigation control laws, which enable the UAV to track a trajectory as long as changes in speed and heading are within the UAV's motion limits.

### 2.3 Multivariate K2 Metric

The traditional BOA uses bivariate chromosome to construct Bayesian network. In our algorithm multivariate chromosome is employed, and therefore the metric used is different to that in the traditional BOA. For each pair of positions $i$ and $j$, the count of each combination of values can be summarized as the following contingency table:

Table 2. Count of each combination


where $n_{i, j}\left(r_{i}, r_{j}\right)$ denotes the count of each combination of values $I_{i}$ and $I_{j}$ in positions $i$ and $j$ at the same time, $N$ denotes the size of a population, and $r_{j}=r_{i}=9$.

The multivariate marginal frequency $p_{i, j}\left(I_{i}, I_{j}\right)$ is defined as the frequency of individuals in parent population, which has $I_{i}$ and $I_{j}$ in positions $i$ and $j$ at the same time:

$$
p_{i, j}\left(I_{i}, I_{j}\right)=n_{i, j}\left(I_{i}, I_{j}\right) / N
$$

Conditional probability of occurrence of the value $I_{i}$ in the $i$ th position in the case of occurrence of $I_{j}$ in the $j$ th position is determined by

$$
p_{i, j}\left(I_{i} \mid I_{j}\right)=p_{i, j}\left(I_{i}, I_{j}\right) / p_{j}\left(I_{j}\right)
$$

The dependency information is used to build up a Bayesian network and the following metric is used to measure the quality of the constructed network [7]:

$$
K 2_{i, j}=\left(\prod_{l=1}^{r_{i}} \frac{\left(r_{j}\right)!}{\left(r_{j}+n_{i}(l)\right)!} \prod_{s=1}^{r_{j}}\left(1+n_{i, j}(l, s)\right)!\right) /\left(\frac{\left(r_{j}\right)!}{\left(r_{j}+N\right)!} \prod_{s=1}^{r_{j}}\left(1+n_{j}(z)\right)!\right)
$$

This equation is derived from $K 2$ metric used in BOA algorithm [4] [5], which is a special case of Bayesian Dirichlet (BD) metric for measuring the quality of the network. The $K 2$ metric is used when no prior information available about the problem under consideration. This is the case for path planning as usually there is no any prior information about the distribution of the population. Therefore, $K 2$ metric is employed in our algorithm.

# 3. EXPERIMENTAL RESULTS 

In this section, some results of path planning experiments using the proposed BOA are presented, which are further compared to the results given by the standard genetic algorithm based on the same dataset.
![img-0.jpeg](img-0.jpeg)

Figure 1. Planning result by GA
![img-1.jpeg](img-1.jpeg)

Figure 2. Planning result by BOA

The UAV is assumed to be initially at $\left(x_{0}, y_{0}\right)=(0,-1)$ with speed $u[0]=2$ and heading $\varphi[0]=0$. Speed changes are limited to 1 with the UAV speed constrained to be an integer in the range [1,3]. Changes in heading are limited to $\pm 30^{\circ}$. The environment through which the UAV must

navigate consists of three threats and six obstacles located at the positions as indicated in Figure 1. A target is located at $\left(x_{T}, y_{T}\right)=(8,1)$.

Figure 1 shows the planning result by genetic algorithm, which traps in a local minimum. We can use fitness sharing to counteract the attraction towards the local minimum. Figure 2 shows the result of path planning generated by the presented BOA, which overcomes the drawback of the standard genetic algorithm.

# 4. CONCLUSIONS 

In this paper a new path planning algorithm is presented based on Bayesian networks. The approach is novel because it is the first time that a Bayesian network model has been applied to the field of UAV path planning. Experimental results have demonstrated the strength of the proposed Bayesian optimization algorithm. The standard GA uses problemindependent recombination operators that may break good building blocks in order to converge to a local optimum. The proposed approach takes advantage of global information about the set of promising solutions to estimate their distribution and this estimate can be used to generate new candidate solutions. Although we have presented this work in terms of path planning problem, it is suggested that the main idea of the approach could be applied to many other multivariate encoding problems. In the future, we will attempt to use the BOA to resolve path planning for multiple UAVs.

## ACKNOWLEDGEMENTS

This research work was supported by the National Nature Science Foundation of China (grant No.90205019) and the Research Fund for the Doctoral Program of Higher Education (grant No.20020699001).
