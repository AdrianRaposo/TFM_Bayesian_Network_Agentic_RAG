# Article 

## Information Value-Based Fault Diagnosis of Train Door System under Multiple Operating Conditions

Seokgoo Kim ${ }^{1}$ (D) Nam Ho Kim ${ }^{2}$ (D) and Joo-Ho Choi ${ }^{3, *}$<br>1 Department of Aerospace \& Mechanical Engineering, Korea Aerospace University, Goyang-City 10540, Korea; sgkim@kau.kr<br>2 Mechanical \& Aerospace Engineering, University of Florida, Gainesville, FL 32611, USA; nkim@ufl.edu<br>3 School of Aerospace \& Mechanical Engineering, Korea Aerospace University, Goyang-City 10540, Korea<br>* Correspondence: jhchoi@kau.ac.kr; Tel.: +82-2-300-0117

Received: 10 June 2020; Accepted: 14 July 2020; Published: 16 July 2020


#### Abstract

While there are many data-driven diagnosis algorithms for fault isolation of complex systems, a new challenge arises in the case of multiple operating regimes. In this case, the diagnosis is usually carried out for each regime for better accuracy. However, the problem is that different results can be derived from each regime and they can conflict with each other, which may invalidate the performance of fault diagnosis. To address this challenge, a methodology for selecting the most reliable one among the different diagnostic results is proposed, which combines the Bayesian network (BN) and the information value (IV). The BN is trained for each regime and a conditional probability table is obtained for probabilistic fault diagnosis. The IV is then employed to evaluate the value of several diagnostic results. The proposed approach is applied to the fault diagnosis of a train door system and its effectiveness is proven.


Keywords: multiple classifier; Bayesian network; multiple operating conditions; train door system; information value

## 1. Introduction

Health diagnostics of mechanical systems and remaining useful life (RUL) prediction brings numerous benefits such as safety system operation, zero downtime, cost-effective maintenance scheduling. To realize these aspects, many studies have been conducted under the name of prognostics and health management (PHM). There are several review papers that address the recent research trend of PHM [1-3]. Basically, PHM can be grouped into two main aspects: fault diagnosis and prognosis. Diagnosis is the prior stage of prognosis because accurate fault isolation and fault severity estimation are directly related to the accuracy of prognostics. Most of the fault diagnostics approaches can be categorized into the model-based and data-driven method [4]. In the case of model-based methods, users are required to establish mathematical models of the system based on the physics of failure, in which the physical parameters are estimated from the sensors data [5]. Data-driven approaches use large amounts of training datasets to train machine learning algorithms to diagnose the health state of the system [6]. Recently, deep learning algorithms are gaining popularity as an alternative option in the data-driven diagnostics approach due to less involvement of features processing [7-10]. Each approach has its own pros and cons. Model-based methods are superior in terms of accuracy. However, it is rarely possible to establish such a model. Data-driven approaches are more common in the field, but require a large amount of data that is not easily available in the industry [11,12]. Users should choose a proper one based on their environments for effective PHM implementation.

In the railway system, the passenger access system (PAS) is known to operate under highly stressed conditions over time and is regarded as one of the most critical parts in the view of safety.

PAS is responsible for $30-40 \%$ of the failures during operation [13]. In order to prevent such failures, model-based and data-driven approaches have been applied to the fault diagnostics of the PAS. In the model-based approach, Bond Graph modeling of a train door is employed to carry out a global FDI (Fault Diagnostics and Isolation) for the fault indicators and residual threshold in the presence of door failures [14]. Lin et al. established a mathematical model of an urban train door system to estimate physical parameters in the case of normal and faulty conditions [15]. Then, the principal component analysis (PCA) is applied to perform the fault diagnosis. Dassanayake et al. performed fault detection and diagnosis of an electric train door by parameter estimation of the system model [16]. In the knowledge-based and data-driven approach, a Petri net behavioral model, which includes normal and faulty condition operating, is established, which is used for fault diagnosis of PAS [17]. Similar to the train door system, Yan and Lee used information gathered from controllers or sensors in the elevator door system and performed on-line performance degradation assessment and root cause analysis using multiple logistic regression (LR) [18]. Apart from these approaches, there have been continued studies employing the Bayesian network (BN) for the fault diagnosis, which is a probabilistic causal network that represents a set of random variables and their conditional dependencies. For decades, it has been widely applied in numerous domains from reliability engineering, risk analysis, and medical diagnosis [19]. In the fault diagnosis, there have been several approaches using BN. For example, Yang and Lee applied BN to predict the wafer quality of a semiconductor manufacturing system and inferred which sensors are directly related to the wafer quality [20]. Xu et al. performed fault inference for rotating flexible rotors with an attempt to enhance the reasoning capacity under conditions of uncertainty with BN [21]. Cai et al. applied PCA and used the principal components as the input nodes of BN for the fault diagnostics of a three-phase inverter [22]. Zheng et al. combined fault tree (FT) and BN to diagnose the bridge crane spreader. This method proved that the proposed method could reduce the amount of required data for model training by using prior knowledge for the system [23]. More applications of the BN in the fault diagnosis can be found in [19].

In this study, the BN is applied to the train door system for the purpose of fault diagnosis using the motor current signals acquired during the door operation. Although there exists literature with the similar applications, a new challenge arises in this problem, which is the issue of multiple operation stages, namely, the train door moves under three different conditions: acceleration, constant motion, and deceleration. As will be discussed in the main text, the diagnosis performance is significantly affected by whether the velocity stages are considered separately or not. In order to achieve better results, it is more advantageous to divide the current signal into different stages, and training is performed respectively.

The problem is, however, that the algorithm can yield different diagnosis results in each stage, which can confuse the identification of the fault modes. Several methods have been proposed to deal with the issue of different or competing results from multiple classifications. Zhang et al. combined multiple neural networks to obtain a more reliable diagnosis than a single one by using the modified majority voting method [24]. The result was compared with original majority voting, averaging, and weighted averaging. Niu et al. proposed a decision fusion for fault diagnosis that integrates data from different types of sensors and decisions of multiple classifiers [25]. The multiple classifiers are fused by using a multi-agent combination algorithm. W. Yan and Xue introduced a dynamic fusion approach and applied it to an aircraft engine fault diagnosis [26]. Their performance was compared with other fusion approaches such as simple averaging and local accuracy-based selection. Existing pieces of literature, however, have focused only on the fusion of different algorithms trained by the data under the same operating condition. On the other hand, this study aims at the fusion of different diagnosis results by multiple operation data using a single BN algorithm.

To solve this problem, this paper proposes a new method that introduces information value (IV) based on the training data to suggest the most reliable classifier. The paper is organized as follows. Section 2 introduces the theoretical background of the Bayesian network. In Section 3, the basic concept

of IV is explained. Application to the train door system is introduced in Section 4 and finally, the paper is concluded in Section 5.

# 2. Bayesian Network 

Bayesian network (BN) is a probabilistic graphical model which represents conditional dependencies or causal connections between a set of random variables via a Directed Acyclic Graph (DAG). BN is capable of reasoning under uncertainty, where the nodes represent variables (discrete or continuous) and links represent direct connections between them. In addition, BN models the quantitative strength of the connections between variables, allowing probabilistic beliefs about them to be updated automatically as new information becomes available [27]. The BN-based fault diagnosis consists of three steps: (1) Determine the network structure, (2) establish the conditional probability table (CPT), and (3) carry out probabilistic fault diagnosis based on given evidence. In the BN, the DAG is called the structure and the values in the CPT are called the parameters.

### 2.1. Basis of Bayesian Network

Let us assume a network model which consists of four nodes named $X_{1}, X_{2}, X_{3}$, and $X_{4}$. The joint probability of the illustrated model can be written as

$$
P\left(X_{1}, X_{2}, X_{3}, X_{4}\right)=P\left(X_{1}\right) P\left(X_{2} \mid X_{1}\right) P\left(X_{3} \mid X_{1}, X_{2}\right) P\left(X_{4} \mid X_{1}, X_{2}, X_{3}\right)
$$

where $2^{4}-1=15$ conditional probability parameters are required to construct the full joint probability when each node has binary status. On the other hand, the BN assumes conditional independence which leads to the reduction of the required number of parameters to calculate joint probability. In the network model shown in Figure 1, $X_{2}$ is the parent node of $X_{3}$ and $X_{4}$, which are conditionally independent each other, and $X_{1}$ is non-immediate parent nodes of $X_{4}$, i.e., $P\left(X_{4} \mid X_{1}, X_{2}, X_{3}\right)=P\left(X_{4} \mid X_{2}\right)$. Applying these relations, the joint probability can be obtained as follows

$$
P\left(X_{1}, X_{2}, X_{3}, X_{4}\right)=P\left(X_{1}\right) P\left(X_{2}\right) P\left(X_{3} \mid X_{1}, X_{2}\right) P\left(X_{4} \mid X_{2}\right)
$$

where the number of parameters is now reduced to 8 . Based on this, any type of probability can be calculated with joint probability.
![img-0.jpeg](img-0.jpeg)

Figure 1. An example of a Bayesian network.

### 2.2. Structure Learning and Parameter Learning for Bayesian Network

The first step of BN-based fault diagnosis is to establish a network structure which reflects the interconnection between random variables. In simple words, the structure implies a set of conditional independence relations among the variables involved [28]. When a domain expert or system user already understands paths of possible influence between variables or the fault tree, the structure of BN can be established based on the domain expert. In some cases, however, it is not a simple matter to find the structure of a BN. In this case, the structure can be determined automatically by

applying BN learning algorithms. Among others, the score-based approach is one of the most popular methods, including the Akaike information criterion (AIC), the Bayesian information criterion (BIC), the minimum description length (MDL), and K2 [20]. This paper employs the K2-algorithm which was developed by Cooper [29] and is known as the simplest approach. The benefit of the K2 algorithm is that prior knowledge for the network structure can be embedded by defining node order in advance to reduce the unnecessary computation. Given database $D$ and a candidate network structure $B_{S}$, the K2 algorithm searches the BN structure, maximizing the probability $P\left(B_{s} \mid D\right)$. This algorithm requires node ordering and an upper limit of the number of parent nodes as the input to reduce the computational complexity. Then, the algorithm searches the most likely set of parent nodes which precedes the current node based on the node ordering by calculating the probability of each case. In other words, it searches the set of parent nodes maximizing the following probability function:

$$
g\left(i, \pi_{i}\right)=\prod_{j=1}^{q_{i}} \frac{\left(r_{i}-1\right)!}{\left(N_{i j}+r_{i}-1\right)!} \prod_{k=1}^{r_{i}} N_{i j k}!
$$

where $i$ is the index of the node variable $x_{i}, \pi_{i}$ is the set of its parent nodes, $q_{i}$ is the unique instantiations of the parents of $x_{i}$ in the database, $r_{i}$ is the number of all possible values of $x_{i}$, and $N_{i j k}$ is the number of cases in the database in which the variable $x_{i}$ has $k^{\text {th }}$ value, and the parents of $x_{i}$ are instantiated with the $j^{\text {th }}$ instances among all possible instantiations of the $\pi_{i}$. Note that $N_{i j}$ can be obtained by $\sum_{k=1}^{r_{i}} N_{i j k}$. Algorithm 1 illustrates the pseudo-code for the K2 algorithm and details can be found in references [29-31]. As a result, optimum BN structure is determined based on the K2 algorithm.

```
Algorithm 1: The K2 algorithm
    1: procedure K2;
    2: \{Input: A set of \(n\) nodes, an ordering on the nodes, an upper bound \(u\) on the
        number of parents a node may have, and a database \(D\) containing m cases.\}
    4: \{Output: For each node, a printout of the parents of the node.\}
    5: for \(i:=1\) to \(n\) do
    6: \(\pi_{i}:=\varnothing\);
    7: \(\quad P_{\text {old }}:=g\left(i, \pi_{i}\right)\);
    8: OKToProceed : true
    9: while OKToProceed and \(\left|\pi_{i}\right|<u\) do
    10: let \(z\) be the node in \(\operatorname{Pred}\left(x_{i}\right)-\pi_{i}\) that maximizes \(g\left(i, \pi_{i} \cup\{z\}\right)\);
    11: \(\quad P_{\text {new }}: g\left(i, \pi_{i} \cup\{z\}\right)\);
    12: if \(P_{\text {new }}>P_{\text {old }}\) then
    13: \(\quad P_{\text {old }}: \mathrm{P}_{\text {new }} ;\)
    14: \(\quad \pi_{i}:=\pi_{i} \cup\{z\}\)
15: else OKToProceed : false;
16: end \{while\};
17: write ('Node:', \(x_{i}\), 'Parents of this node:', \(\pi_{i}\) )
18: end \{for\};
19: end \(\{\mathrm{K} 2\}\);
```

Once the network structure is determined by the K2 algorithm, next is to establish the CPT. CPTs are usually obtained by two ways: domain expert's knowledge or learning from normal and fault data [22]. In this paper, CPTs are calculated from training data by implementing the maximum likelihood estimation (MLE) [32]. When database $D$ consists of $N$ samples and is expressed as

$D=\left\{D_{1}, D_{2}, \ldots, D_{N}\right\}$, MLE tries to find the best parameter $\theta$ by maximizing the likelihood function, $l(\theta \mid D)$. The log-likelihood of $\theta$ is represented as follows:

$$
l(\theta \mid D)=\log P(D \mid \theta)=\log \prod_{i=1}^{N} P\left(D_{i} \mid \theta\right)=\sum_{i=1}^{N} \log P\left(D_{i} \mid \theta\right)=\sum_{i j k} N_{i j k} \log \theta_{i j k}
$$

where $\theta_{i j k}$ is defined as $k$ th probability of a conditional probability of $P\left(X_{i}=k \mid \pi_{i}=j\right)$. In other words, the MLE estimate $\theta_{i j k}^{*}$ for $\theta_{i j k}$ can be calculated as follows:

$$
\theta_{i j k}^{*}=\frac{N_{i j k}}{N_{i j}}
$$

After the model structure and the CPT of all nodes are established, the BN can be used to propagate probabilities from the root to the following other nodes under given evidence [33].

# 3. Information Value 

Information value (IV) is known as a very useful concept for variable selection during the model construction in the industry. The IV helps to rank variables based on their significance for the predictive model and it can be stated as follows:

$$
I V=\sum\{P(E \mid H)-P(E \mid \bar{H})\} \log \frac{P(E \mid H)}{P(E \mid \bar{H})}
$$

where $H$ and $E$ represent the hypothesis or theory and some evidence, respectively. The negation of $H$ is denoted by $\bar{H}$. The first term on the right, $P(E \mid H)-P(E \mid \bar{H})$, measures the importance of deviation. The second term, $\log P(E \mid H) / P(E \mid \bar{H})$, known as the weight of evidence (WOE), represents the deviation between distributions, which is the ratio of likelihood and is mathematically equal to the logarithm of the Bayes factor. In general, the IV values are interpreted as shown in Table 1 [34]. In this study, the hypothesis and evidence correspond to the normal condition of the system and the feature vectors that are used to diagnosis the system health, respectively.

Table 1. Interpretation of information value.


## 4. Application: Train Door System Fault Diagnosis

### 4.1. Data Acquisition and Preprocessing

In this study, motor current and encoder signals acquired from the door control unit (DCU) with the sampling rates of 100 Hz and 10 Hz are utilized during the open and close operation of the train door. Figure 2a,b show the train door system test rig and the current signal obtained during the operation. In the figure, the spindle nut assembly moves along the spindle where the cam follower bearing slides within the track of the base frame is parallel to the spindle. Attached to this assembly is the hanger assembly, which hangs the door below and moves along the roller track by the rollers. Note that the eccentric roller exists inside the hanger assembly to prevent vibration during the door operation. Based on the experiences, it is known that the cam follower bearing and roller are prone to fail due to the wear. Therefore, signals are acquired for the conditions of normal and two seeded

faults to the bearing and roller. The faults are shown in Figure 2c, in which the outer diameter of the bearing is reduced from 22.3 mm (normal) to 21.8 mm (fault) to induce loosening of locking, and the shaft diameter of the roller is reduced from 10.0 mm (normal) to 9.0 mm (fault) to simulate the wear between the roller and shaft. The door is operated under three different velocity conditions when it opens and closes, which are the acceleration, constant speed, and deceleration.
![img-1.jpeg](img-1.jpeg)

Figure 2. Data acquisition: (a) Train door system test rig; (b) current signal during operation; (c) bearing and roller specimen for test.

The three regimes can be identified by the encoder, and the acquired signals are shown in Figure 3a,b for the open and close operation, respectively, distinguished by the symbols at each regime. For more accuracy, it is better to carry out fault diagnosis by dividing the signal into these regimes and extracting features, respectively. This is because the features can represent the condition in a certain regime more clearly, while it may not be so for the whole period. Similar attempts have been made in the literature $[35,36]$ to cluster the data by the velocity regimes.

![img-2.jpeg](img-2.jpeg)

Figure 3. Current signal behavior: (a) open operation; (b) current signal during close operation.
By considering the three regimes corresponding to different input conditions, it also makes sense to evaluate the features separately for different input conditions. Commonly used statistical features, root mean square (RMS), max, mean and variance, are extracted from each regime as illustrated in Table 2, which results in the total of 12 features. Since the BN usually deals with the discrete variables, all the extracted features are transformed into the binary states, assuming that all the features follow normal distribution, namely normal (1) and abnormal (0) where the anomaly is defined by the exceedance of $95 \%$ confidence limit. In the table, velocity regimes are labeled as follows: acceleration $=$ 1 , constant $=2$, and deceleration $=3$. Figure 4 illustrates the feature transformation process during the open operation. The output dataset in the database consists of six variables: one velocity state ( 1,2 , or 3), four feature states ( 1 or 0 ), and one door state (norm, bearing, roller). Since the number of datasets in each operation is 57 , the total number of datasets for all three operating conditions becomes 171. Among them, $70 \%$ are used for the training, which is to find parameters and structure of BN, while the remaining $30 \%$ are used to test the model performance.

Table 2. Feature extraction for velocity condition.


![img-3.jpeg](img-3.jpeg)

Figure 4. Feature transformation into the binary state during the open operation.

# 4.2. Bayesian Network Model Construction 

As mentioned in Section 2.2, the optimum BN structure is constructed by using the K2 algorithm. The algorithm requires node ordering and the number of maximum parent orders as an important input. In this study, the velocity regimes and the door state are chosen as the root node at the top and the final node at the bottom, respectively. Node ordering is then set as: Vel, RMS, max, mean, var, door state, with the number of nodes $n$ being six. The maximum number of parents $u$ for a node is constrained at three to reduce complexity of the model. Using the training data, the BN structures are constructed by applying the K2 algorithm for the open and close operation as shown in Figure 5a,b respectively. As shown in the figure, different BN structures are obtained for each operation. For the open operation, door state (S) is found to have conditional dependency on the Max, Mean and Var, whereas it has the Vel, Mean and Var in the close operation. These structures represent that the door health conditions can be estimated by monitoring the condition values of these nodes. Note that the structures in Figure 5a,b are those maximizing the probability function (3). In fact, the log of the function being -512.82 at the initial structure converged to -228.5 and -255.5 , respectively, at the two optimum structures. Using the constructed BN, CPTs for open and close operation are obtained next based on the MLE approach. As an illustration, CPTs of the last node, which is the door state (S), and three nodes connected with $S$ are given in Tables 3 and 4. Once the BN and CPTs are available, they can be applied to diagnose the door health condition, i.e., fault can be predicted through the belief propagation of the network. Given a velocity condition (acc' 1 , const' 2 , or dec' 3 ) and corresponding state (normal 1 or abnormal 0 ) of each feature, the door state is predicted by the posterior probabilities for the three failure modes: normal, bearing fault, and roller fault. For example, during the close operation, when Vel, RMS, and Max are at the state 1,0 , and 0 , respectively, the BN indicates that the door has the chance of roller fault with $97.78 \%$. This can be expressed in the form of conditional probability as $P(S=$ Roller $|\mathrm{Vel}=1, \mathrm{RMS}=0, \mathrm{Max}=0)=0.9778$. With this information, one can estimate the health condition of the train door system. For each of the training data, the door state is predicted in this way and validated by the true state. The accuracies of the open and close operation are validated by using the training datasets and their results are 82.53 and $78.83 \%$, respectively.

![img-4.jpeg](img-4.jpeg)

Figure 5. Bayesian network structure: (a) open operation; (b) close operation (Vel: velocity, Max: Maximum, Var: variance, S: door state).

Table 3. Conditional probability table during the open operation.


Table 4. Conditional probability table during the close operation.


# 4.3. Fault Diagnosis Based on Information Value

As mentioned, when the system operates under different conditions and multiple diagnosis models are established for each condition, the result can be different for each operating condition. To resolve the conflicting issues in terms of diagnosis performance, one should determine which result is the most reliable. In the train door system, three different fault prediction results were obtained for three velocity conditions. As an example, Table 5 shows this problem, which diagnoses three different door conditions for an open operation. That is, the door is considered to be bearing fault



Table 5. Estimation result during one open operation.


Table 6. Information value calculation during one open operation.


![img-5.jpeg](img-5.jpeg)

Figure 6. Information value-based fault diagnostics procedure
Table 7. Information value during open and close.


![img-6.jpeg](img-6.jpeg)
(a)

Figure 7. Cont.

![img-7.jpeg](img-7.jpeg)
(c)

Figure 7. Comparison of fault diagnostic results before and after applying information value: (a) open operation; (b) close operation; (c) open \& close operation.

# 5. Conclusions 

Fault prediction using a Bayesian network provides more information (i.e., probabilistic reasoning) for effective reasoning than a deterministic fault diagnosis algorithm. To realize effective fault diagnostics, operation conditions, such as rotating speed and loading condition, should be considered properly. For this purpose, this paper performed regime partitioning, which is widely used to deal with fault diagnosis problems under multiple operating conditions. In addition, information value was proposed to deal with the situation when multiple diagnostic results exist, which are derived from the results of each regime. Future work can be considered as two mainstreams: A continuous Bayesian network will be considered to alternate binary Bayesian networks. Even if the Bayesian network was originally developed for a binary condition, continuous versions are expected to show more accurate results. In addition, a dynamic Bayesian network will be developed to deal with real-time data.

Author Contributions: Conceptualization, S.K.; writing—original draft preparation, S.K.; writing—review and editing, N.H.K. and J.-H.C.; supervision, J.-H.C. All authors have read and agreed to the published version of the manuscript.

Funding: This research was supported by National Research Foundation of Korea (NRF) grant funded by the Korea government (MSIT) (No. 2019R1A2C2010028).
Conflicts of Interest: The authors declare no conflict of interest.
