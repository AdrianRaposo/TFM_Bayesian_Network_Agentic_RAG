# A UCB-BASED Tree Search Approach to Joint Verification-Correction Strategy for Large Scale SYSTEMS 

A Preprint

Peng Xu<br>Grado Department of Industrial and Systems Engineering Virginia Tech<br>Blacskburg, VA 24060<br>xupeng@vt.edu

Xinwei Deng<br>Department of Statistics<br>Virginia Tech<br>Blacskburg, VA 24060<br>xdeng@vt.edu

Alejandro Salado<br>Department of Systems and Industrial Engineering<br>The University of Arizona<br>Tucson, AZ 85721<br>alejandrosalado@arizona.edu

April 5, 2022


#### Abstract

Verification planning is a sequential decision-making problem that specifies a set of verification activities (VA) and correction activities (CA) at different phases of system development. While VAs are used to identify errors and defects, CAs also play important roles in system verification as they correct the identified errors and defects. However, current planning methods only consider VAs as decision choices. Because VAs and CAs have different activity spaces, planning a joint verificationcorrection strategy (JVCS) is still challenging, especially for large-size systems. Here we introduce a UCB-based tree search approach to search for near-optimal JVCSs. First, verification planning is simplified as repeatable bandit problems and an upper confidence bound rule for repeatable bandits (UCBRB) is presented with the optimal regret bound. Next, a tree search algorithm is proposed to search for feasible JVCSs. A tree-based ensemble learning model is also used to extend the tree search algorithm to handle local optimality issues. The proposed approach is evaluated on the notional case of a communication system.


Keywords verification planning $\cdot$ Bayesian network $\cdot$ multi-armed bandit problem $\cdot$ correction activity $\cdot$ tree search $\cdot$ random forest

This work has been submitted to the IEEE for possible publication. Copyright may be transferred without notice, after which this version may no longer be accessible.

# 1 Introduction 

System verification is defined as the process that evaluates whether a system or its components fulfill their requirements [Engel, 2010]. System verification is planned and implemented as a verification strategy (VS) that specifies how to implement activities at different developmental phases and on different system configurations [Salado and Kannan, 2018a]. A VS consists of verification activities (VA), each of which is used to identify errors and defects, and correction activities (CA) that correct the identified errors and defects. While VAs includes inspection, analysis, analogy, demonstration, test, and sampling, CAs usually take the form of rework, repair, or redesign, depending on whether the activity encompasses substitution of a faulty part, modification of the product, or modification of the product's design [Engel, 2010, for Standardization, 2015]. A VS is defined aiming at three objectives: "maximizing confidence on verification coverage, which facilitates convincing a customer that contractual obligations have been met; minimizing risk of undetected problems, which is important for a manufacturer's reputation and to ensure customer satisfaction once the system is operational; and minimizing invested effort, which is related to manufacturer's profit" [Salado, 2015].

Several strategy planning methods have been proposed to design VSs, including decomposition approach [Barad and Engel, 2006], set-based design [Xu and Salado, 2019], parallel tempering method [Xu et al., 2021], and reinforcement learning method [Xu et al., 2020]. All these methods treat only VAs as dedicated decisions that are planned for a system configuration at a development phase (i.e., system state), and CAs are simplified as default actions or even ignored reactively [Xu and Salado, Under Review]. This simplification may undermine the value of resulting VSs because of the potential suboptimality of CAs. Thus, an extended paradigm of verification planning is presented in our previous paper to include both VAs and CAs as the result of independent decisions. All dependency relationships of VAs and CAs are summarized in that extended paradigm. An order-based dynamic programming (ODP) method is also proposed to find the optimal joint verification-correction strategies (JVCS) that specifies VAs and CAs along a verification process [Xu and Salado, Under Review]. However, as there are more possible activities, the number of the resulting possible system states increases exponentially [Xu and Salado, Under Review]. So, it becomes computationally a very difficult task to update the values of all system states. Thus, the ODP method fails to obtain optimal strategies when the system size is large, and an alternative planning method is lacking.
As it is computationally difficult to find the optimal strategy for large systems, we proposed a UCB-based tree search approach for large scale systems in this paper. The proposed method can generate near-optimal JVCSs that fit well with the engineering requirements within certain computational resources. The contributions of this paper are as follows:
First, we presented a search rule based on the upper confidence bound for repeatable bandits (UCBRB). To simplify the verification planning problem, a repeatable bandit model is presented as an extension of the traditional multi-armed bandit problem. Then the UCBRB rule is proposed with the regret theory. The UCBRB rule can be used to find near-optimal strategies of those decision-making problems whose strategies are repeatable.
Second, we designed a UCBRB1 tree search method to apply the UCBRB rule to verification planning. This method originates from traditional AO* algorithms [Nilsson, 1982] that require accurate admissible heuristic functions, which is hard to define in verification planning. So, we approximate the heuristic functions with the proposed UCBRB rule. The characteristics of system verification, including confidence information, two types of activities, and a value-based model, are also considered to design this method for the search of JVCSs.
Third, we leveraged a tree-based ensemble learning model to handle local optimality issue of the UCBRB1 tree search method. As verification planning is a sequential decision-making problem with dependency, the distributions of state values are not stationary during tree search processes (i.e., concept drift). These concept drifts usually result in local optimality of JVCSs. We trained random forest regression (RFR) with collected samples of system states during the tree search process and used a lower confidence bound of RFR outputs to predict state values as prior information. These prediction values are used to narrow the gap of concept drifts between different system states and help jump out of the local optimum spaces.
The rest of this paper is organized as followed. Section 2 reviews the literature about bandit-based methods, tree search methods for sequential decision-making, and tree-based ensemble learning models. Section 3 introduces the basic underlying models to model verification planning problems to underpin the proposed work. Section 4 presents the proposed UCB-based tree search approach. Section 5 uses a demonstrative case to illustrate the performance of the approach. Our conclusions and future directions are summarized in Section 6.

# 2 Literature Review 

### 2.1 Bandit-based Methods

The multi-armed bandit problem is a sequential decision model in which an agent needs to decide which arm of $K$ different slot machines to maximize their reward while improving their information at the same time [Bergemann and Välimäki, 2006]. This problem provides a paradigm of the tradeoff between exploration (trying out each arm to find the best one) and exploitation (playing the arm believed to give the best payoff). The reward of each arm is a random variable $x_{k}$ with an unknown distribution and the distributions of all arms are independent from each other. This bandit problem aims at finding a policy that determines which bandit to play based on previous trials. The performance of a policy is commonly measured by the agent's regret [Bubeck and Cesa-Bianchi, 2012], which is the expected loss due to not playing the best bandit.
In a seminal paper, Lai and Robbins [Lai et al., 1985] made a regret analysis to find an asymptotic lower bound on the growth rate of total regret for a large class of reward distributions. The regret bound is $O(\ln n)$, where $n$ is the overall number of plays. Since then, various online policies have been proposed, among which the UCB1 policy developed by Auer et al. [Auer et al., 2002] is considered the optimal [Kuleshov and Precup, 2014, Huo and Fu, 2017]. The UCB1 policy is to play a machine $k$ that maximizes $\bar{x}_{k}+\sqrt{\frac{2 \ln n}{n_{k}}}$, where $\bar{x}$ is the average reward obtained from machine $k$, and $n_{k}$ is the number of times machine $k$ has been played so far. That is, this policy can balance the exploitation of the bandit currently believed to be optimal with the exploration of other bandits that currently appear suboptimal but may turn out to be superior in the long run [Browne et al., 2012]. This UCB1 policy achieves logarithmic regret uniformly over time (not asymptotically) without any prior knowledge regarding the reward distributions. However, the UCB1 is limited by its assumption that the optimal machine is determined by comparing the expected average rewards of all machines. That is, the UCB1 policy would lose its rationality if the expected average reward is not the measure of a machine's performance.
To solve the tree search problem, Kocsis and Szepesvári [Kocsis and Szepesvári, 2006, Kocsis et al., 2006] proposed the use of UCB1 as tree search policy, which is called the upper confidence bound for trees (UCT). Its formula is

$$
U C B=\bar{x}_{k}+D_{1} \sqrt{\frac{2 \ln n}{n_{k}}}
$$

where $D_{1}$ is constant. While the UCT follows the assumption of expected average rewards to determine upper confidence bounds, some variant policies have been proposed as extensions of the UCT to adapt to their domains where the assumption is invalid. We find two domains that are related to system verification in this paper. First, Schadd et al. [Schadd et al., 2008] extended bandit problems to single-player games with perfect information where the expected maximum value rather than the expected average value is used to choose moves. They proposed a single-player MCTS policy (SP-MCTS) that add a third term to the UCT rule:

$$
U C B=\bar{x}+D_{2} \sqrt{\frac{2 \ln n}{n_{k}}}+\sqrt{\frac{x^{2}-n_{k} \cdot \bar{x}^{2}+D_{3}}{n_{k}}}
$$

where $D_{3}$ is a constant that artificially inflates the standard deviation for infrequently visited nodes. However, as the averaged values are used as the first item to represent the performance, the phenomenon that a good move is hidden by previous records of bad moves may still occur [Bjornsson and Finnsson, 2009]. Second, Galichet et al [Galichet et al., 2013] studied a risk-aware bandit problem that measures machine's performance with the conditional value at risk $\alpha(\mathrm{CVaR})$, which is the average of the lowest quantiles of the reward distribution with level $\alpha$. As the goal is to find the machine with maximal CVaR, machines are selected with the best lower confidence bound on their CVaRs, which is called MARAB policy $\widehat{C V a R}_{k}-D_{4} \sqrt{\frac{\ln (|n \alpha|)}{|n_{k} \alpha|}}$, where $D_{4}>0$ is a constant that controls the exploration vs exploitation tradeoff. As $\alpha$ decreases, the risk-aware bandit problem boils down to a standard max-min optimization problem. However, the calculation of the lowest quantiles results in the storage issue when the bandit problem is of large size, because all previous trials must be recorded to determine the quantiles.

### 2.2 Tree Search Methods for Sequential Decision-making

Sequential decision-making is a procedural approach to decision-making that aims at finding a policy that maximizes the expected return for all possible initial system states, where earlier decisions influences the later available choices [Barto et al., 1989]. We refer by sequential decision-making under uncertainty to those problems where the results of a decision follow a random distribution, such as bandit problems, path planning under uncertainty, and system verification. We distinguish between two types of sequential decision-making problems under uncertainty according to

whether all following states of a decision should be further planned. If only one following state should be planned after a decision, finding the policy requires determining the set of optimal actions that are connected as a path. In contrast, if it is necessary to plan all following states, the optimal policy can be represented as an AND/OR tree where all actions of a decision have OR relationship and all results of an action have AND relationship. While the first type is widely studied in the fields related to reinforcement learning [Kaelbling et al., 1996], the second type has been explored in a variety of research domains, such as system verification [Salado and Kannan, 2018a], disease diagnosis [Mitra et al., 2005], and troubleshooting [Khanafer et al., 2008].
The key difference between the methods of these two types lies in the calculation of rewards. That is, the reward of a state depends on all following states in the second type of decision-making problems. Until now, two approaches have been proposed to find the policy of the second type. The first approach is heuristic search methods that originate from $\mathrm{AO}^{*}$ algorithms for AND/OR trees. Nilsson [Nilsson, 1968, 1982] first described a version of $\mathrm{AO}^{*}$ for searching AND/OR trees to find a solution in the form of a tree. Martelli and Montanari [Martelli and Montanari, 1978] generalized this algorithm for searching AND/OR graphs to find a solution in the form of an acyclic graph. The graph-search version is more efficient than the tree-search version when the same state can be reached along different paths because it avoids performing duplicate searches [Hansen and Zilberstein, 2001]. Hansen and Zilbersterin [Hansen and Zilberstein, 2001] proposed a generalization of $\mathrm{AO}^{*}$, called LAO*, to find solution graphs with loops. As the solution of verification planning can be presented as directed acyclic graphs, we only focus on the $\mathrm{AO}^{*}$ algorithm for system verification. All these $\mathrm{AO}^{*}$ algorithms use admissible heuristic functions to find exact solutions and have been applied to troubleshooting [Warnquist et al., 2009] and diagnosis of autonomous system [Chanthery et al., 2010]. However, when the admissible heuristic functions are not available, the $\mathrm{AO}^{*}$ algorithm cannot be applied.
The second approach is dynamic programming methods (DP) that solve the problem by breaking it down into simpler sub-problems in a recursive manner. DP methods can be classified into exact DP methods and approximate DP methods according to whether the type of solution policies are exact or approximate. Exact DP methods, such as backward induction method, value iteration, and policy iteration, are used to solve exact planning problems [Sniedovich, 2010]. They have been applied to solve various fields, such as verification planning [Kulkarni et al., 2020, 2021], circuit design [Shachter and Bhattacharjya, 2010], and fault location [Velimirovic et al., 2019]. However, when the state space is large, exact DP methods fail in finding exact solutions due to the curse of dimensions [Powell, 2007]. Instead, approximate DP methods can be used to approximate the decision-making process. These approximate methods can be broken down into four classes according to the types of approximate policies: myopic policies, lookahead policies, policy function approximations, and value function approximations [Powell, 2007]. While myopic and lookahead policies minimize costs for one or several finite time periods, ignoring the effect of a decision now on the later time periods, they are limited if the long-term effects are important. Policy function approximations are applied when the structure of a policy is fairly obvious [Powell, 2016]. Because verification strategies have VAs and CAs in this paper, the structure of a policy suffers the dependency relationship between VAs and CAs. So, the fourth type of value function approximations is mostly related to verification planning. Many different approximation models of value functions have been proposed, such as look-up tables of Q learning [Watkins and Dayan, 1992], support vector regression [Bethke et al., 2008], and neural network [Bertsekas and Tsitsiklis, 1995]. However, as far as we know, there are no value function approximation methods for the second type of sequential decision-making under uncertainty.

# 2.3 Tree-based Ensemble Learning Models 

Ensemble learning is an effective technique that has increasingly been adopted to combine multiple learning models to improve overall prediction accuracy [Dietterich, 2000a]. These ensemble techniques have the advantage to alleviate the small sample size problem by incorporating over multiple learning models to reduce the potential for overfitting the training data [Dietterich, 2000b, Yang et al., 2010]. Decision trees are commonly used in ensemble learning model because decision trees are sensitive to small changes on the training set [Dietterich, 2000a]. So, the scope of ensemble learning models is narrowed down to tree-based models. These ensemble learning models have been applied to many fields, such as bioinformatics [Yang et al., 2010], defect prediction [Matloob et al., 2021], and remote sensing [Saini and Ghosh, 2017]. However, as far as we know, tree-based ensemble learning models have not been used in verification planning.
Some common types of ensemble learning include bagging, boosting, and stocking, which are realized as some basic models, such as random forest (RF) [Ho, 1995], XGBoost [Chen and Guestrin, 2016], LightGBM [Ke et al., 2017], and CatBoost [Dorogush et al., 2018]. Many studies have been conducted to test the performance of these models and each of them has its own merits. For example, Bentéjac and Csörgő [Bentéjac et al., 2021] found that CatBoost obtained the best results in generalization accuracy and AUC while LightGBM had the fastest training speed in the studied datasets. Ibrahim et al. [Hancock and Khoshgoftaar, 2020] recommended CatBoost algorithm for better prediction of loan approvals and staff promotion. In another study about highly imbalanced Big Data [Jhaveri et al., 2019],

XGBoost was found to be better than CatBoost because of its shorter training time. In addition, the applications of tree-based ensemble learning models are not limited to these basic models. For example, Jhaveri et al. [Ibrahim et al., 2020] proposed a weighted random forest along with AdaBoost to predict the success rate of Kickstarter campaigns. Zhang et al. [Zhang et al., 2018] combined RFs with XGBoost to establish the data-driven wind turbine fault detection framework. Zeinulla et al. [Zeinulla et al., 2020] proposed a fuzzy random forest model to diagnose heart disease with incomplete and dirty datasets. So, the selection of ensemble learning models depends on the characteristics of the research task and datasets.

It is noticeable that ensemble learning has also been used in nonstationary environment, where the underlying data distribution changes over time (i.e., concept drift). Elwell and Polikar [Elwell and Polikar, 2011] proposed an ensemble of classifiers-based approach for incremental learning of concept drift. The proposed algorithm collects consecutive batches of data, trains one new classifier for each batch of data it receives, and combines these classifiers using a dynamically weighted majority voting. Later, Yin et al. [Yin et al., 2013, 2015] introduce a comprehensive hierarchical approach called dynamic ensemble of ensembles. It includes two stages. First, component classifiers and interim ensembles are dynamically trained. Second, the final ensemble is then learned by exponentially weighted averaging with available experts. However, all these methods use the weighted averaging method to fuse the information of all components. Thus, they cannot be directly applied in the verification planning that searches for optimal strategies.

# 3 Verification Planning Framework 

### 3.1 System Verification with Bayesian Networks

We consider that a given system can be decomposed into a set of system elements and assume that the objective of system verification is to verify relevant requirements for these elements. We conceive system verification as a set of tuples of system parameters $\theta_{1}, \cdots, \theta_{I}$ about these requirements and the VAs that provide information about such system parameters, denoting the resulting verification evidence of a VA by $\mu_{j}$ with $j=1, \cdots, J$. Using the modeling framework presented in [Salado and Kannan, 2019], we build a basic system verification model as a BN $\Omega=(\Theta \cup M, E)$, where $\Theta$ is a set of nodes, each of which represents one system parameter, $M$ is a set of nodes that represent VAs, and $E$ is a set of directed edges that connects the different nodes. There are three types of directed edges: $\Theta \Rightarrow \Theta, \Theta \Rightarrow M$, and $M \Rightarrow M$, which capture the information dependencies between system parameters, between system parameters and VAs, and between VAs, respectively. In the resulting BN, nodes representing VAs will be treated as observable nodes (those whose node states can be observed directly) and nodes representing system parameters will be treated as hidden nodes (those whose value states cannot be observed directly but are inferred from the values of the observable nodes). For example, consider a computer system that has two parameters, processor speed (denoted by $\theta_{1}$ ) and computer speed (denoted by $\theta_{2}$ ), and each parameter has its own VA (denoted by $\mu_{1}$ and $\mu_{2}$, respectively). The BN can be built accordingly, as shown in Fig. 1 (a).
Because the interpretation of the information provided by VAs is subjective [Salado and Kannan, 2018b], we capture the information about system parameters as beliefs. Without loss of generality, all nodes are assumed to be binary (i.e., two node states, such as pass/fail or compliant/non-compliant). The nature of Bayesian analysis, and of BNs by extension, allows for easy removal of this restriction and use of any number of discrete values and even continuous belief distributions [Berger, 2013]. The specific beliefs of a network node are presented as a conditional probability table (CPT) in this paper. Each CPT summarizes the dependency relationships between a node and all its parent nodes. After all CPTs are elicited as prior distributions of a BN, the impact of a VA on the beliefs is modeled as follows: (1) A verification result $A\left(\mu_{i}\right)$ is collected after executing $\mu_{i}$ (i.e., an observable node $\mu_{i}$ is observed); and (2) the posterior distributions of the network nodes are updated by the Bayesian rule.
CAs are defined as those that correct errors or defects that are found during system development [Xu and Salado, 2021]. CAs impact the confidence of system parameters because they affect the system configuration. In our previous study [Xu and Salado, 2021], uncertain evidence is leveraged to model the effects of CAs on the BN. Three basic types of CAs are modeled with their uncertain evidence: rework, repair, and redesign. For example, when a repair activity is executed to modify a faulty element with parts, processes, or materials that were initially unplanned for that element, it is assumed that repairing the element has impact on the beliefs of the corresponding parameter in the verified system. We can apply virtual evidence to represent the impact of repair on the beliefs. For example, a repair activity is conducted to improve the overall computer speed. As the repair is applied to the system. This piece of evidence is captured as virtual evidence applied on $\theta_{2}$ directly. The virtual evidence is shown as a virtual node $\varphi_{1}$ on $\theta_{2}$ in Fig. 1 (b). When the uncertain evidence of a CA is collected, the beliefs of a BN are updated in the same way as that of VAs [Xu and Salado, 2021]. That is, when the uncertain evidence of $\varphi_{k}$ is added to the BN, the confidence of other network nodes can be updated with the Bayesian rule.

![img-0.jpeg](img-0.jpeg)
(a) An Exemplar Network
![img-1.jpeg](img-1.jpeg)
(b) Repair on the BN

Figure 1: Illustration of the Bayesian Network Models.

# 3.2 Verification Planning Problems 

We consider a verification process with time events $t=1, \cdots, T$. For simplicity, we assume that only one VA and one CA is conducted at each time event and the VA is followed by the CA. This assumption can be relaxed when conducting more than one activity in parallel, which is reserved for future work. In this paper, the paradigm of verification planning is defined as a sequential process of repeating VAs and CAs at $T$ time events, as shown in Fig. 2. The solution of verification planning is the assignment of VAs and CAs along a verification process. Because each VA has multiple possible results (e.g., Pass/Fail), different combinations of activities exist along the same process and all of these possible combinations can be presented as an activity tree. One example of an activity tree is shown in Fig. 3. Each path from the root node to a terminal node is called a verification path in this study. In the example in Fig 3, there are 5 verification paths, and all verification paths share the same initial system state $S_{1}$. System states are generated along with the collection of activity results at each verification path. At the end of each verification path, the verification process terminates with a certain system state, which is called terminal state (denoted by 'Stop', as shown in Fig. 3).
![img-2.jpeg](img-2.jpeg)

Figure 2: Illustration of Two Time Events of a Verification Process
![img-3.jpeg](img-3.jpeg)

Figure 3: One JVCS example (P: pass; F: fail)
At each time event, verification planning consists of assigning a VA and a CA from their own activity spaces, each of which is a set of all eligible activity actions, including the action 'NA' (i.e., No Activity). It is notable that there are two constraints about the activity spaces of VAs and CAs. First, it is unnecessary to repeat any activity again if the previous result of such an activity remains valid. That is, if an activity has been executed and its result can still be used to update beliefs, such an activity is not included in the activity space. Second, implementing a CA can make the existing results of a VA invalid if the result of the VA depends on the corrected parameter. The reason for this is that once a CA changes a system parameter, all existing verification results that depend on such a parameter lose their credibility in deducing accurate posterior beliefs of the system. According to this constraint, it can be inferred that each VA may be executed multiple times if some CAs influence the relevant parameters of such a VA. Therefore, the activity spaces of VAs and CAs depend on the system state at the time the decision is made, and the specific set of activity actions always change along the entire verification process.
To measure the performance of a JVCS, three value factors are considered to calculate the value function. The first value factor is activity costs, which is a fixed amount of financial resources necessary to conduct either a VA or a CA. It is denoted as $C\left(\mu_{j}\right)$ for $\mu_{j}$ and $C\left(\varphi_{k}\right)$ for $\varphi_{k}$. For example, if a rework activity is executed to replace a faulty element, corresponding activity costs could include the purchasing cost of new elements and labor fees to replace the elements. The second value factor is failure costs, $C\left(A\left(\mu_{j}\right)=\right.$ Fail $)$, which is incurred when the result of a VA is found to be Fail. The third value factor is system revenue, $B\left(\theta_{i}\right)$, which is obtained only when a verification process terminates (i.e., reaches a terminal state) and the system is deployed. $B\left(\theta_{i}\right)$ depends on the evolution in confidence

Table 1: Summary of Notations


that the system is operating correctly as VAs are performed. We consider the system to be deployed only when the confidence level $P\left(\theta_{i}=\right.$ Pass $)$ of the target parameter $\theta_{i}$ at a system state $S_{m}$ reach or surpass certain thresholds, $H_{i}$.

For simplicity, all of these value factors are summarized at each terminal state. Each verification path could be stopped in two situations. First, the confidence levels of all target parameters reach their thresholds $\left\{H_{i}\right\}$. Second, the action 'NA' is selected when assigning a VA. Consider a JVCS $\Psi$ that starts from a system state $S_{1}$ and has $w$ verification paths $Z_{1}, \cdots, Z_{W}$ and each verification path has a set of system states $\left\{S_{m}\right\}_{w}$. For a given verification path $Z_{w}$, the overall value is calculated as:

$$
\begin{aligned}
U\left(Z_{w}\right) & =\sum_{i} B\left(\theta_{i}\right) P\left(\theta_{i}=\operatorname{Pass} \mid Z_{w}\right) \delta\left(P\left(\theta_{i}=\operatorname{Pass} \mid Z_{w}\right)>H_{i}\right) \\
& -\sum_{j} C\left(\mu_{j}\right)-\sum_{j} C\left(A\left(\mu_{j}\right)=\right. \text { Fail })-\sum_{k} C\left(\varphi_{k}\right)
\end{aligned}
$$

where $\delta(\cdot)$ is an indicator function whose value is 1 if the statement is true and 0 otherwise. Because a JVCS $\Psi$ consists of a set of verification paths, the performance of this JVCS $U\left(\Psi \mid S_{1}\right)$ is calculated as the expected value of a verification process $E\left(U\left(Z_{w}\right)\right)$, which is the weighted sum of the overall values of all verification paths:

$$
U\left(\Psi \mid S_{1}\right)=E\left(U\left(Z_{w}\right)\right)=\sum_{w} P\left(Z_{w}\right) U\left(Z_{w}\right)
$$

where $P\left(Z_{w}\right)$ is the probability of a verification path $Z_{w}$ that is calculated by multiplying state transition probabilities (i.e., the probabilities of an activity result) along a verification path:

$$
P\left(Z_{w}\right)=\prod_{m} P\left(A \mid S_{m}\right)
$$

The verification planning problem is to solve for the optimal JVCS for a given initial system state $S_{1}$ :

$$
\Psi_{o p t}=\arg \max _{\Psi} U\left(\Psi \mid S_{1}\right)
$$

A summary of the notations used in this paper is shown in Table 1.

# 4 Proposed UCB-based Tree Search Approach 

### 4.1 Upper Confidence Bound for Repeatable Bandits (UCBRB)

As each verification path has a set of its own system states, all system states of a JVCS can be represented as an AND/OR tree. At any system state whose following system states are not fully explored, verification planning shares

the uncertain characteristic with bandit problems. That is, when an activity is selected, the expected reward of this activity follows an unknown distribution. However, verification planning differs from a sequential play of bandit problems. As long as the prior knowledge about the target system is determined, implementing a given JVCS always generates the same expected reward by enumerating all possible verification paths, which means a JVCS is repeatable. So, a repeatable bandit problem (RBP) is investigated in this section first as a simplification of verification planning.
Consider a K-armed bandit problem where $K$ machines are played sequentially and only one machine is played each time. The reward of a level pull of each machine is represented by a random variable $X_{k, s}$ for $1 \leq k \leq K$, where $k$ is the index of a machine. Successive plays of machine $k$ yield rewards $X_{k, 1}, X_{k, 2}, \cdots$, which are independent and identically distributed (i.i.d.) according to an unknown distribution $F_{k}$. The support of $F_{k}$ is $\left[a_{k}, b_{k}\right]$. The distributions of all machines are independent from each other; i.e., $X_{k, s}$ and $X_{k^{\prime}, s^{\prime}}$ are independent (and usually not identically distributed) for each $1 \leq k<k^{\prime} \leq K$ and each $s, s^{\prime} \geq 1$. Assume that whenever a reward is collected from machine $k$, the player can remember the tricks about reproducing such a reward through controlling the pulling factors, such reaction time point, pull speed, and pull length. So, when the player has collected some pull results of all machines, they can select the machine of the optimal reward and repeat some previous level pull to obtain the same reward. This bandit problem is defined as RBP in this paper. The objective of a RBP is to maximize the sum of rewards earned through a sequence of pulls.
The main difference between traditional bandit problems and the RBP is the expected reward of each machine. In traditional bandit problems, the reward of a level pull is a random observation of machine $k$. So, the expected reward of machine $k$ is the expectation of $F_{k}$. However, in RBPs, only the maximum reward of machine $k$ will be considered for further repetition. So, the expected reward of machine $k$ can be represented by the maximum reward after $n_{k}$ plays of machine $k$, where $n_{1}+n_{2}+\cdots+n_{k}=n$ and $n$ is the total plays of all machines. Other results with lower rewards are not considered for future repetition any more. As each machine of a RBP has its own distribution with a supremum $u_{k} \leq b_{k}$, the maximum among the supremum rewards of all bandits is defined as the overall supremum $u_{*}=\max _{k}\left(u_{k}\right)$. We follow the previous study [Lai et al., 1985] to define the regret of a RBP as:

$$
u_{*} \cdot n-u_{k} \sum_{k=1}^{K} E\left(n_{k}\right)
$$

That is, the regret of a RBP is the expected loss due to the fact that the player does not always repeat the optimal play. For bandit problems, a policy is a strategy that chooses the next machine to play based on the sequence of past plays and obtained rewards [Auer et al., 2002]. Previous policies, such as the UCB1, work by providing an upper confidence bound for each machine to optimize the accumulated regret. However, as these policies use the expectation of a machine as the target, they are not appropriate choices for RBPs. Thus, we proposed a modified policy called upper confidence bound for repeatable bandits:

- Initialization: play each machine once;
- Loop: play machine k that maximizes $x_{k}^{\max }+\frac{4 l n(n)}{D_{0} \cdot n_{k}}$, where $x_{k}^{\max }=\max \left(x_{k, 1}, x_{k, 2}, \cdots, x_{k, n_{k}}\right)$ is the maximum reward obtained from machine $k, n_{k}$ is the number of times machine $k$ has been played so far, $D_{0}$ is a constant that is determined by the distributions of all machines, and $n$ is the overall number of plays.

It is noticeable that $D_{0}$ is the minimum of $D_{0, k}$ and each $D_{0, k}$ is the bound constant of the distribution of each machine, as shown in Lemma 1. As the distribution of each machine is unknown, the constant $D_{0, k}$ can be estimated according to presumptive distributions and collected samples. For example, assume the distribution of any machine $F_{k}$ is a uniform distribution $\left[a_{k}, b_{k}\right]$. The range $\left(b_{k}-a_{k}\right)$ can be estimated as $\frac{n+1}{n-1}\left(x_{k}^{\max }-x_{k}^{\min }\right)$. So, the estimate of $D_{0}$ is $\min _{k} \frac{n-1}{\left(n+1\right)\left(x_{k}^{\max }-x_{k}^{\min }\right)}$.
The regret bound of this policy is summarized as the theorem below. The proof of this theorem is provided in Appendix.
Theorem 1 For all $K>1$, if the UCBRB rule is run on $K$ machines having arbitrary reward distributions with support in $[0,1]$, then its expected regret after any number $n$ of plays is at most $O(\ln (n))$.

# 4.2 UCBRB1 Tree Search Method 

As verification planning can be viewed as a sequential play of RBPs, we use the proposed UCBRB rule to calculate the UCB of the expected reward of a nonterminal system state $S_{m}$ :

$$
U C B\left(S_{m}\right)=x_{k}^{\max }+D_{6} \frac{\ln (n)}{n_{k}}, D_{6} \geq 0
$$

where $x_{k}^{\max }$ is the maximum expected reward of $n_{k}$ JVCSs that starts from $S_{m}$ (i.e., $\max _{\Psi}\left(\left\{U\left(\Psi \mid S_{m}\right)\right)\right\}$ ), $n_{k}$ is the visit count of $S_{m}$, and $n$ is the overall visit count of its preceding state $S_{m-1} . D_{6}$ is a constant that depends on the unknown distribution of the state value, which may be obtained through sensitivity analysis in practice. If the range of $x_{k}^{\max }$ is larger than 1 , the first item may be replaced by $x_{k}^{\max } / D_{7}$, and $D_{7}$ is a discount constant to normalize the range. With this UCBRB rule, system states are evaluated with the balance between exploration and exploitation. In addition, if the confidence of target parameters reaches the threshold $H_{i}$ or a 'NA' is selected as a VA, the corresponding system state is a terminal state and the reward of this state is deterministic no matter how many more times it is visited. So, the UCBs of these terminal states are simply their maximum reward value and the second item in Eq. 8 is 0 .
As a verification process consists of multiple time events, the UCBRB rule is insufficient because it only solves the comparison between the activities at a given system state. Therefore, we proposed a UCBRB1 tree search method to make sequential decisions along a verification process. The method consists of a set of loops, with each loop having two stages. First, an AND/OR tree is generated in a forward way where each nonterminal state is expanded as a tip node and an activity is selected to generate its following states. Then, the set of nonterminal states are updated by removing the expanded state and adding nonterminal following states. This expansion step is repeated until the set of nonterminal states is empty. In particular, all feasible activities are determined first according to the activity constraints in Section 3.2. Then each activity is evaluated with the UCB values of all its following states. The activity with the largest value is chosen, as shown in Eq. 9:

$$
\begin{aligned}
& \mu_{*}=\arg \max _{\mu_{j}}\left(-C\left(\mu_{j}\right)-C\left(A\left(\mu_{j}\right)=\text { Fail }\right)+\sum_{a} P\left(A\left(\mu_{j}\right)=a\right) U C B\left(S_{m+1}\right) \mid a\right), \text { or } \\
& \varphi_{*}=\arg \max _{\varphi_{k}}\left(-C\left(\varphi_{k}\right)+U C B\left(S_{m+1} \mid \varphi_{k}\right)\right)
\end{aligned}
$$

where $S_{m+1}$ means the next system state after conducting the activity and $a$ represents Pass or Fail. Second, the node information of all tree nodes, including expected reward and visit counts are updated backwardly from terminal nodes to the root node. That is, the expected value of each node is updated according to expected values of their child nodes in this tree:

$$
\begin{aligned}
& U\left(S_{m}\right)=-C\left(\mu_{j}\right)-C\left(A\left(\mu_{j}\right)=\text { Fail }\right)+\sum_{a} P\left(A\left(\mu_{j}\right)=a\right) U\left(S_{m+1} \mid \mu_{*}\right)\right), \text { or } \\
& U\left(S_{m}\right)=-C\left(\varphi_{k}\right)+U\left(S_{m+1} \mid \varphi_{*}\right)\right)
\end{aligned}
$$

Then the expected rewards are compared with the previous record of this state and saved in the look-up table. If its value is larger than that in the look-up table, the record is updated with the larger one. The visit counts of all tree nodes are added by 1 in the look-up table.
The UCBRB1 tree search method is designed by extending the previous work [Vomlelová and Vomlel, 2003] from three aspects to improve the efficiency of tree search. First, as all following states of an AND branch must be considered in an AND/OR tree, all nonterminal states of an AND branch are expanded simultaneously in the method. Second, we update the information of all nodes only when the whole AND/OR tree is expanded completely rather than whenever a node is expanded. Third, we use the UCBs rather than an admissible function to represent the heuristic value of a system state.
In addition, two adjustments are made about Eq. 8 in practice. First, while Eq. 8 is meaningless if either $n$ or $n_{k}$ is 0 , the visit counts of all system states are 0 at the beginning. So, we assume that all system states have been visited once before the tree search and, for simplicity, the expected value is set as None. Then, Eq. 8 is equivalent to:

$$
U C B\left(S_{m}\right)=x_{k}^{\max }+D_{6} \frac{\ln (n+1)}{n_{k}+1}
$$

Second, because all following system states are expanded, the number of tree nodes increases exponentially along with the tree depth, which makes the strategy space very complex. To simplify the strategy space, we add a penalty item in Eq. 8 to prevent the over-expansion of trees:

$$
U C B\left(S_{m}\right)=x_{k}^{\max }+D_{6} \frac{\ln (n+1)}{n_{k}+1}-f(m \mid \Psi)
$$

For simplicity, the penalty item $f(m \mid \Psi)$ is assumed to be a function of system index $m$ when it is expanded. For example, $f(m \mid \Psi)=D_{8} *\left\lfloor m / D_{9}\right\rfloor, D_{8}=1$, and $D_{9}=50$. That is, the UCB of a nonterminal state is reduced by 1 every 50 system states. Finally, the UCBRB1 tree search method is summarized in Algorithm 1.

# Algorithm 1 UCBRB1 Tree Search Method 

1: Inputs:
$L=\{\}$ : lookup table; $\Psi$ : sample tree.
2: Initialize $\Psi=\left\{S_{1}\right\}$, where $S_{1}$ is the initial state.
3: while $\Psi$ has some tip nodes do
4: $\quad$ Expand all tip nodes of $\Psi$ according to the UCBs of all following states calculated by Eq. 12.
5: Add expanded states to $\Psi$.
6: $\quad$ Denote all nonterminal expanded states as tip nodes.
7: end while
8: Update state values and visit counts of all nodes in $\Psi$ according to Eq. 10.
9: Update L with the updated state values and visit counts.
10: if the expected value $U(\Psi)$ converges then
11: $\quad$ Output $\Psi_{o p t}$ as the solution.
12: else
13: $\quad$ Go to 2 .
14: end if

### 4.3 Function Approximation of State Values

Even though the proposed UCBRB1 tree search method can solve for a near-optimal JVCS, the tree search process has local optimality issues. That is, the activities of a strategy become fixed at a system state after certain rounds of tree search and it is impossible to explore other possible activities. To handle this issue, we use a function approximation model to approximate state values by generalizing the values of collected system states. Here this model serves two purposes. First, when a new nonterminal state is expanded, the selection of activities suffers from a lack of state information because all following states have not been visited before. However, if a prior state value is added to the calculation of UCBs, some promising action will be selected and the efficiency of tree search will be improved. Second, because the tree search process collect state information incrementally, concept drifts occurs in terms of the distribution of $U\left(S_{m}\right)$. This concept drift can result in the immovability of activity selection, as will be shown in the experiment section. So, the function approximation model is expected to provide some heuristic information to narrow the gap of distributions between different system states. Thus, the tree search process can jump out of local optimum spaces.
To approximate state values, it is necessary to identify all factors that contribute to the distribution of a state value. During a verification process, there are four types of independent information, including prior confidence of system parameters and activities, collected evidence of activities, value factors of a verification process, and policy rules (e.g., the UCBRB rule). We use three types of variables as the input of the function approximation model to predict state values, as shown in Fig. 4. First, the posterior confidence values of all system parameters are used because they directly determine whether one system can be deployed. Second, the statuses of all activities, including whether all parameters are corrected and whether valid verification results are collected, are denoted as a list of categorical variables. Third, the counts of all executed VAs and CAs are calculated as two count variables to distinguish node information. These count variables are redundant because they are the sum of all status values.
![img-4.jpeg](img-4.jpeg)

Figure 4: Dependency between Verification Information and State Values

With the analysis above, we propose to use random forest regression (RFR) to approximate the dependency relationship. The rationale of using RFR for such a function approximation is as follows. First, the input variables are a mixture of continuous, categorical, and count ones. RFR can accept such mixed variables as inputs. Second, all input variables are correlated because they depend on collected evidence. RFR are robust to such redundant inputs. Third, RFR can generate prediction intervals by using the outputs of all decision trees, which can provide a robust approximation of state values. This is important because if an improper activity is selected, all following activities may be vain attempts.

While sample trees are generated continuously along the tree search process, we train RFR models periodically along the tree search process. That is, we divide tree search processes into basic sampling periods and collect tree nodes of sample trees as training datasets at each sampling period. Then a RFR model is built for each sampling period and the output of the latest model are used as the predicted state values. This is explained from two aspects. First, there is a dependency among sample trees because the UCBs are calculated based on all previous state values and visit counts. That is, all training samples are not i.i.d. samples. When the number of sample trees increases, the relationship between training samples becomes increasingly complex. So, models are trained at each period to simplify the dependency between sample trees. Second, because of the concept drift of state value distributions, those built approximation models may lose their generalization accuracy gradually. So, we only use the latest RFR model to predict state values.

We add RFR approximation to extend the UCBRB1 tree search method in two places. First, whenever a sampling period is finished, we train a RFR model based on the lookup table and the sample trees in the sampling period. Because of the randomness of tree search process, the dependency relationship of collected sample trees is random and always change during the tree search process. So, we use RFR models to interpolate the datasets and each decision tree is built with a zero mean squared error. That is, the information of all visited system states are saved accurately in the RFR models. Second, when calculating the UCBs of state values, we use the latest RFR model to predict state values as prior values. In particular, the $k$-th percentile of the outputs of all decision trees is used as the prior state value $\hat{x}_{k}$. Each prior state value is compared with the state value record in the lookup table. Thus, the UCB formula in Eq. 12 is extended as:

$$
U C B\left(S_{m}\right)=\max \left(\hat{x}_{k}, x_{k}^{\max }\right)+D_{6} \frac{\ln (n+1)}{n_{k}+1}-f(m \mid \Psi)
$$

where the first item is the maximum between the prior value and the maximum record value.
We also make another two adjustments about data processing to improve the quality of training datasets. First, when each sample tree is generated, all terminal nodes of a sample tree are not included as training samples. The reason is that if ' $\mathrm{NA}^{\prime}$ ' is selected as a VA, this type of terminal nodes suffer larger variance of state values than nonterminal nodes because their following states have not been visited. If parameter confidence reaches the threshold, it is unnecessary to predict state values. Second, besides the tree nodes in the latest sampling period, another set of system states is uniformly sampled from the lookup table with replacement and added to the training datasets. This adjustment is made to reduce the bias caused by the dependency of sample trees. For simplicity, the number of sampled system states is the same as that of sample tree nodes. The extended algorithm is called UCBRB2 tree search method in this paper.

# 5 Experimental Design 

### 5.1 Problem Description

In this section, we implement the proposed framework to design a JVCS for an optical instrument in a satellite [Salado and Kannan, 2019]. The notional instrument has been used to support prior research in verification [Salado and Kannan, 2019]. The system parameters of this optical instrument and their possible VAs are modeled as the BN shown in Fig. 5. System parameters are represented as circle nodes and candidate VAs square nodes. The definitions of the nodes are given in [Salado and Kannan, 2019], hence not presented here. Each node is characterized with its own conditional probability tables (CPT). Their specific values are synthetic and have been generated using the generalized Noisy-OR and Noisy-AND model [Pearl, 2014], which takes into account the physical meaning of the different modes when estimating their mutual effects for reasonability of the data. While this instrument is verified through a set of these VAs, each parameter $\theta_{i}$ has CAs to correct potential errors and defects. Without loss of generality, this experiment takes only repair activities $\varphi_{k}$ as an example of CAs.
In this experiment, we assume that system revenue is driven by system parameter $\theta_{1}$. Hence, $\theta_{1}$ is set as the single target parameter. The threshold for the system deployment rule, $H_{1}$, is set as 0.90 . Cost data have also been synthetically generated in thousand dollar units $(dollars 1,000)$. The revenue $B\left(\theta_{1}\right)$ has been set to 20,000 so that it provides a balance when making a selection tradeoff between different VAs. In the BN, there is a dependency between $\theta_{1}$ and all other network nodes. That is, once an activity is executed on any node of these 32 nodes and an activity result is collected,

Table 2: Cost Table (Unit: dollars1,000)


the confidence $P\left(\theta_{1}=\right.$ Pass $)$ will change. The activity costs of the different activities, as well as the failure costs of VAs, are provided in Table 2. Specific values have been generated according to the type of activities defined in [Salado and Kannan, 2019].
![img-5.jpeg](img-5.jpeg)

Figure 5: BN of the Optical Instrument (The smaller network outlined by the dash line is used in Scenario 1 and the whole network is used in Scenario 2.)

# 5.2 Experimental Method 

With the provided problem and generated data, the whole experiment is realized with Python 3.6 and Bayes Net Toolbox for Matlab [Murphy et al., 2001]. Two scenarios are conducted to study the performance of the proposed approach. In Scenario 1, the target network is the smaller one outlined by the dash line in Fig. 5. With 5 system parameters and 9 VAs in this BN, there are $2 \cdot 2^{5} \cdot 2^{9}=1259712$ total system states. The costs items of all activities are shown in bold in Table 2. To get some intuition about this scenario, we apply the order-based backward induction method first to solve for the exact JVCS. When the backward induction is conducted to calculate the expected values of all states, the optimal activities of all system states are identified to constitute the exact JVCS, as shown in Fig. 6. With 24 verification paths (i.e., the number of terminal states 'Stop'), the exact JVCS has 93 tree nodes (excluding terminal states 'Stop'). The depth of this JVCS is 13 nodes (i.e., 7 time events). The expected value of this JVCS is 7,788 while the total running time is $97,925 \mathrm{sec}$.
In Scenario 2, the target network is the whole network in Fig. 5. With 10 system parameters and 22 VAs in this BN, there are $2 \cdot 2^{10} \cdot 2^{22}=6.43 * 10^{13}$ total system states. As the number of total system states is too large, the order-based backward induction method is infeasible for this whole network and the exact solution is unknown. However, because the small network is a subset of the whole one, the exact JVCS in Scenario 1 can be used as a reference. So, there is a question whether a better JVCS can be found in the large network, which is discussed later.
In each scenario, the proposed approach is compared with two types of benchmark methods. First, we compare the UCBRB rule with other UCB rules, including the UCT rule (i.e., Eq. 1) and the SP-MCTS rule (i.e., Eq. 2). As verification planning is such a special problem that we cannot find an accurate admissible heuristic function of all states, the $\mathrm{AO}^{*}$ algorithm cannot be applied to solve for AND/OR trees. Algorithm 1 in Section 4.2 is the only feasible

![img-6.jpeg](img-6.jpeg)

Figure 6: The exact JVCS solution of Scenario 1
Table 3: Expected value and runtime of all possible $D_{6}$ constants


method to find a JVCS as far as we known. So, we combine Algorithm 1 with all these UCB rules to compare their effects. For each rule, their constant values are selected through their own sensitivity analyses. We set $D_{7}=20000$, $D_{8}=1$, and $D_{9}=50$. The tree search process is conducted by generating 5000 sample trees. We record the optimal state value every 50 sample trees at the initial state to compare the performance of difference UCB rules.

Second, we compare the proposed methods with a Monte Carlo method. The UCBRB2 tree search method is also tested as an extension of the UCBRB1 one. A RFR model is trained every 3000 tree nodes and another 3000 system states are sampled from the lookup table. Each RFR model consists of 100 decision trees and the 5th percentile of the 100 outputs are used as predicted state values. The hyperparameter 'Bootstrap' is set as False and the hyperparameter 'minimum number of samples required to be at a leaf node' is set as 1 to interpolate state samples while other hyperparameters are set as their default values. Finally, a Monte Carlo method is designed to search for a JVCS in a random fashion. As the number of tree nodes can be large if all activities are chosen randomly. A constraint about the total number of tree nodes is added in this Monte Carlo method. That is, the total node number is less than $D_{10}=50$.

# 5.3 Experimental Results 

### 5.3.1 Scenario 1

In the UCBRB rule (given by Eq. 8), the constant $D_{6}$ depends on the unknown distributions of the specific problem. So, it is necessary to determine the constant $D_{6}$ first for the proposed approach. For simplicity, a set of six possible $D_{6}$ constants $[0.1,0.25,0.5,1,1.5,2]$ is used to find the optimal one. For each constant value, the tree search algorithm in Algorithm 1 is conducted to test the performance and their trends are shown in Fig. 7. It is found that when $D_{6}$ is 0.5 , the expected value reaches the maximum 7780.78 among the 5000 sample trees. The expected values and runtimes of all possible constants are listed in Table 3.

![img-7.jpeg](img-7.jpeg)

Figure 7: Constant selection for the UCBRB rule

From Fig. 7 and Table 3, it can be observed that when $D_{6}$ decreases, the expected value converges faster. This is because more weights are allocated to the exploitation of existing strategies (i.e., the first item in Eq. 8) when $D_{6}$ decreases. The runtime also decreases become similar trees are exploited. However, if $D_{6}$ is too small, the tree search process may get stuck in local optimal spaces. For example, when $D_{6}=0.1$, the expected value becomes stable after the 1950th sample tree. Thus, $D_{6}$ should be large enough given fixed computation resources. In this case, as the limit of tree number is set as 5000 , we set $D_{6}$ as 0.50 for the UCBRB rule in this experiment.
Next, three kinds of UCB rules are compared to solve this small network problem. With a similar approach for the $D_{6}$ value of the UCBRB, the optimal constants of UCT and SP-MCTS is found to be $D_{1}=0.50, D_{2}=0.50$, and $D_{3}=10000$. The performance of all UCB rules are shown in Fig. 8 (a). It is found that even though both UCT and SP-MCTS rules can find their near-optimal strategies, the UCBRB rule outperforms them slightly after the 4000th sample tree. This is explained by the usage of maximum value as the first item in Eq. 8, which make the UCBRB more sensitive to the optimal activities. It is also found that SPUCB converges faster than UCT. We attribute it to the third item in Eq. 2 as it adds more weights to those nodes that are visited less frequently. Because there is no significant difference between the optimal expected values of all UCB rules, all UCB rules can be considered for the activity selection in this scenario.
Finally, we also conduct the Monte Carlo method and the UCBRB2 tree search method to search this small strategy space. The Monte Carlo method is conducted to generate 5000 sample trees. Then the UCBRB2 tree search method shares the same $D_{6}$ value with the UCBRB1 tree search method. Their performances are shown in Fig. 8 (b) and summarized in Table 4. It is found that the Monte Carlo method cannot compete with the proposed two methods in terms of the expected values of JVCS, even though it costs the least runtime among all methods. The UCBRB1 tree search method can find the optimal strategy with the highest expected value and its runtime is close to that of the Monte Carlo method.
Even though the UCBRB2 tree search method costs the more runtime and its expected value is not the highest, it can solve the local optimality issue that exists in the UCBRB1 tree search method. For simplicity, we use the distribution of all activities at the initial state $S_{1}$ to study the local optimality issue. If the UCBRB1 tree search method is used, the first activity is always fixed as $\mu_{19}$ after the 500th sample tree, as shown in Fig. 9 (a) (i.e., activity immovability). This activity immovability problem is attributed to the concept drift that enlarges the value gap of the first item in Eq. 8. So, the UCB of other activities cannot surpass that of $\mu_{19}$, as shown in Fig. 10 (a). The UCBRB2 tree search method solved this local optimality issue by narrowing the value gap with the prior information, as shown in Fig 10 (b). So, more sample trees are allocated to other activities and it is possible to jump out of the local optimum strategy space (i.e., Fig. 9 (b)).

# 5.3.2 Scenario 2 

In Scenario 2, there are 10 CAs and 22 VAs. As only some extra network nodes are added to the BN, all methods in Scenario 1 can be applied directly. For simplicity, all constants are assigned with the same values as those in Scenario 1. We compare all UCB rules first in this scenario and show their results in Fig. 8 (c) and Table 4. It is found that the JVCS generated by the UCBRB rule has the maximum expected value 8478.43 , while the UCT and SP-MCTS only found their strategies with 7011.08 and 6114.59. In particular, the expected values of the UCT rule do not surpass 6000 until the 3350th sample tree. The reason provided by our analysis is that this large network has more large-cost

![img-8.jpeg](img-8.jpeg)

Figure 8: Plots of All UCB Rules and Benchmark Methods

Table 4: Performance comparison of all UCB rules and benchmark methods (including UCT, SP-MCTS, Monte Carlo, and ODP)


activities than the small network. So, the mean value is a biased estimate of a state value that makes the estimated UCB less accurate. However, the mean value still has some effect in the long term as it can be found that the expected value gradually reaches 7000 . The SP-MCTS rule can find a JVCS with the value 6114.59 at the 300th sample tree. However, once this rule finds the JVCS with the 6114.59, it fails to provide a better JVCS as the value gradually decreases after the 300th sample tree. This is explained by the third item in Eq. 2 as it is not sensitive to the maximum value when the number of samples is large. Therefore, the UCBRB rule can find a better strategy than other ones in Scenario 2 because it uses the maximum function as a more accurate estimate of state value.
The performances of all three benchmark methods are shown in Fig. 8 (d) and also summarized in Table 4. It is found that the proposed two methods have found near-optimal JVCSs while the Monte Carlo method fails in providing a JVCS with a positive expected value. The reason is attributed to the large network that has more high-cost activities. So, it is harder to search for a strategy with positive expected values randomly. Instead, estimating the expected value with UCBs can avoid repeating the over-exploration of high-cost activities and yield better strategies with limited tree samples. However, these two proposed methods also cost much more time than the Monte Carlo method. It is attributed to the UCB calculation and the network size. The UCBRB2 tree search method converges faster than the UCBRB1 one in the first 2000 sample trees, even though there is no significant difference between their optimal expected values.
The activity immovability problem still occurs when the UCBRB1 tree search method is used. The optimal activity at the initial state is fixed as $\mu_{19}$, as shown in Fig. 9 (c). It is caused by the same reason as in Scenario 1 that the value gap of the first item in Eq. 8 is too large. So, the UCBs of other activities can hardly surpass that of $\mu_{19}$. However, the UCBRB2 tree search method can improve the UCBs significantly so that other activities are allocated with more exploration times. Thus, the tree search process can jump out of local optimum spaces and find a better JVCS. This explains why the JVCS of the UCBRB2 method has the largest expected value 8487.27.

# 5.4 Discussion 

The two scenarios in this experiment are designed by expanding the activity set of the same system network. With the proposed UCBRB1 and UCBRB2 tree search methods, a better JVCS is found in Scenario 2, which is attributed to those extra 5 CAs and 13 VAs (i.e., $\varphi_{6}$ to $\varphi_{10}$, and $\mu_{20}$ to $\mu_{32}$ ) in Scenario 2. However, this phenomenon does not always occur. We have verified the expected value of the exact JVCS (ref. Fig. 6) in the context of the large network and found its expected value is 76 because the confidence of the target node drops below 0.9 at most terminal states of verification paths in the large network. Thus, if the costs of all extra activities are very large, it is highly likely that the expected values of near-optimal JVCSs in Scenario 2 are lower than 7,788. Due to some low-cost activities, such as $\varphi_{10}$ and $\mu_{23}$, there are still some opportunities to improve the strategy performance in Scenario 2. Therefore, while finding JVCSs is the task of this research, the effects of all activity costs on JVCSs are not fully explored, which is left as a future work.
During the tree search process, we also found that activity immovability always happens in this verification planning problem, no matter which UCB rule is used. This problem cannot be solved by adjusting the constant $D_{6}$, neither. It is attributed to the concept drift of value distributions. In addition, we assume there are two causes of concept drift. The first one is the lacking of the completeness in tree search processes. If it requires a large number of 'Pass' activity results to reach the deployment threshold of the target parameter, the tree of a near-optimal JVCS has a large depth and it cannot be found easily. Instead, only some partial information is collected, which results in concept drift. The second cause is the second item of UCB rules. When the parent visit count is 1 (i.e., $n=0$ in Eq. 8), the first item is None and the second item is 0 . Then, the optimal activity is 'NA' because it has the minimum activity cost 0 . So, the optimal activity of an unvisited state is always 'NA', which makes the expected values of its parent tree nodes inaccurate. However, it is noticeable that activity immovability also has a positive effect on the search of JVCS. After the tree search processes find a simple JVCS with a positive expected value, this set of activities is fixed as a core set of activities and its value can be improved by exploitation. Thus, it is unnecessary to eliminate this effect. Instead, it is suggested to improve the UCBs of other promising activities.
While the ensemble learning model is applied to extend the UCBRB1 tree search method, the optimal expected value is not improved significantly. It is mainly attributed to CAs in our view. Because CAs can eliminate errors and defects and reset the statuses of VAs, they can improve the confidence of system parameters fundamentally and reduce the impact of negative activity results. So, if a JVCS can eliminate system errors, the selection of activities at early time events does not matter too much on expected values in this experiment. From the aspect of practice, the UCBRB1 tree search method should be considered first as it can provide a feasible JVCS with less runtime and storage space. However, if it is important to explore other candidate activities, the UCBRB2 method is a better choice because it can handle local optimality issues and solve the exploration-exploitation dilemma much better than the UCBRB1 one.

![img-9.jpeg](img-9.jpeg)
(c) Scenario 2 - UCBRB1 tree search method
![img-10.jpeg](img-10.jpeg)
(d) Scenario 2 - UCBRB2 tree search methods

Figure 9: Distribution of All Activities at the Initial State $S_{1}$

![img-11.jpeg](img-11.jpeg)
(c) Scenario 2 - UCBRB1 tree search method
![img-12.jpeg](img-12.jpeg)
(d) Scenario 2 - UCBRB2 tree search methods

Figure 10: UCBs of All Activities at the Initial State $S_{1}$

# 6 Conclusion 

This paper has presented a UCB-based tree search approach to solve the verification planning problem. First, we simplify the verification planning problem as a repeatable bandit problem and propose a UCBRB rule. The upper regret bound of this UCBRB rule is also found and proved. Then we propose a UCBRB1 tree search method to apply the UCBRB rule to search for JVCSs. A tree-based ensemble learning model is also used to extend the UCBRB1 tree search method by using RFR models to predict state values. It is found that the proposed UCBRB rule can outperform other UCB rules in the experiment. This advantage is more obvious when the size of the system network increases. The UCBRB2 tree search method can also effectively solve the local optimality issue and handle the explorationexploitation dilemma better than the UCBRB1 one.
We would like to remark there are three limitations in the proposed methodology. First, the constants of all UCB rules are selected from several possible values in the experiment. The selected value is used as a deterministic value at all system states in the two scenarios. Second, some other parameters and constants of tree search algorithms are not optimized, including discount constant, penalty item, total sample tree number. Third, when training RFR models to predict state values, we set most hyper-parameters with their default values and make some ad hoc adjustments, such as removing terminal states as samples and adding the same number of system states from lookup tables, which are not fully optimized to improve the tree search performance.
In addition, we suggest that this work opens three main future research directions. First, the horizon of verification processes is not fully explored in this study as a penalty item is simply added to restrict the horizon. More mechanisms may be developed to explore the effect of horizon on JVCSs. Second, this work focuses on the tree search given a fixed system network. The selection of possible sub-networks could be explored to simplify tree search processes. The sub-networks may be generated by evaluating the impacts of activities on JVCSs. Third, only RFR models are studied in this work. They are also trained with some intuitive features to approximate system values. Other machine learning methods need to be explored as benchmarks in the future.

## Acknowledgments

This material is based upon work supported by the National Science Foundation under Grant No. CMMI-1762883.

## Appendix

Lemma 1 [Galichet et al., 2013, Lemma 4.1] Let $v$ be a bounded distribution with support in $[0,1]$, with $u$ its supremum and let us assume that $v$ is lower bounded in the neighborhood of a:

$$
\exists D>0, \forall \varepsilon>0, P(X \geq a-\varepsilon)>D \varepsilon, \text { with } X \sim v
$$

Let $x_{1}, \ldots x_{t}$ be $t$-sample independently drawn from $X$. The maximum value over $x_{i}, i=1, \cdots, t$ goes exponentially fast to $u$ :

$$
P\left(\max _{1 \leq i \leq t}\left(x_{i}\right) \leq u-\varepsilon\right)>\exp (-t D \varepsilon)
$$

Proof of Theorem 1:

Proof 1 For each machine $k$, the upper bound of $n_{k}$ is determined first as $T_{k}(n)$. Let $h$ be some positive integer, $I_{t}=k$ is an indicator function, and $X_{k}^{\max }$ be the maximum value over $x_{k, i}, i=1, \cdots, t$. The supremum of $X_{k}^{\max }$ is

$u_{k}$ and $u_{*}=\max _{k}\left(u_{k}\right)$.

$$
\begin{aligned}
T_{k}(n) & =1+\sum_{t=K+1}^{n}\left\{I_{t}=k\right\} \\
& \leq h+\sum_{t=K+1}^{n}\left\{I_{t}=k, T_{k}(t-1) \geq h\right\} \\
& \leq h+\sum_{t=K+1}^{n}\left\{X_{*}^{\max }+\frac{4 \ln (t-1)}{D \cdot T_{*}(t-1)} \leq X_{k}^{\max }+\frac{4 \ln (t-1)}{D \cdot T_{k}(t-1)}, T_{k}(t-1) \geq h\right\} \\
& \leq h+\sum_{t=K+1}^{n}\left\{\min _{0<s<t} X_{*, s}^{\max }+\frac{4 \ln (t-1)}{D \cdot s} \leq \max _{h<s_{k}<t} X_{k, s_{k}}^{\max }+\frac{4 \ln (t-1)}{D \cdot s_{k}}\right\} \\
& \leq h+\sum_{t=1}^{\infty} \sum_{s=1}^{t-1} \sum_{s_{k}=h}^{t-1}\left\{X_{*, s}^{\max }+\frac{4 \ln (t)}{D \cdot s} \leq X_{k, s_{k}}^{\max }+\frac{4 \ln (t)}{D \cdot s_{k}}\right\}
\end{aligned}
$$

The inequation $X_{*, s}^{\max }+\frac{4 \ln (t)}{D \cdot s} \leq X_{k, s_{k}}^{\max }+\frac{4 \ln (t)}{D \cdot s_{k}}$ implies at least one of the following inequations must hold:

$$
\begin{aligned}
X_{*, s}^{\max } & \leq u_{*}-\frac{4 \ln (t)}{D \cdot s} \\
X_{k, s_{k}}^{\max } & \geq u_{k}+\frac{4 \ln (t)}{D \cdot s_{k}} \\
u_{*} & <u_{k}+2 \frac{4 \ln (t)}{D \cdot s_{k}}
\end{aligned}
$$

Because $X_{k, s_{k}}^{\max }$ is always less than $u_{k}$, Inequation 15 cannot be true.
When $s_{k} \geq \frac{8 \ln (t)}{D \cdot\left(u_{*}-u_{k}\right)}$, Inequation 16 is false because

$$
u_{*}-u_{k}-2 \frac{4 \ln (t)}{D \cdot s_{k}} \geq u_{*}-u_{k}-\left(u_{*}-u_{k}\right)=0
$$

With Lemma 1, we have

$$
P\left(X_{*, s}^{\max } \leq u_{*}-\frac{4 \ln (t)}{D \cdot s}\right) \leq \exp \left(-s D \frac{4 \ln (t)}{D s}\right)=\exp (-4 \ln (t))=t^{-4}
$$

So, we have

$$
\begin{aligned}
E\left(T_{k}(n)\right) & \leq\left\lceil\frac{8 \ln (t)}{D\left(u_{*}-u_{k}\right)}\right\rceil+\sum_{t=1}^{\infty} \sum_{s=1}^{t-1} \sum_{s_{k}=\lceil 8 \ln (t) / D\left(u_{*}-u_{k}\right)\rceil}^{t-1} P\left(X_{*, s}^{\max } \leq u_{*}-\frac{4 \ln (t)}{D \cdot s}\right) \\
& \leq\left\lceil\frac{8 \ln (t)}{D\left(u_{*}-u_{k}\right)}\right\rceil+\sum_{t=1}^{\infty} \sum_{s=1}^{t} \sum_{s_{k}=1}^{t} t^{-4} \\
& \leq \frac{8 \ln (t)}{D\left(u_{*}-u_{k}\right)}+1+\frac{\pi^{2}}{6}
\end{aligned}
$$

Thus,

$$
u_{*} \cdot n-u_{k} \sum_{k=1}^{K} E\left(n_{k}\right)=\sum_{k=1}^{K}\left(u_{*}-u_{k}\right) E\left(n_{k}\right) \leq \sum_{k=1}^{K}\left(\left(u_{*}-u_{k}\right)\left(\frac{8 \ln (t)}{D\left(u_{*}-u_{k}\right)}+1+\frac{\pi^{2}}{6}\right)\right)=O(\ln (t))
$$
