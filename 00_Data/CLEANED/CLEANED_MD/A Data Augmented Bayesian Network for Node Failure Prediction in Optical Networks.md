# A Data Augmented Bayesian Network for Node Failure Prediction in Optical Networks 

Dibakar Das<br>IIIT Bangalore<br>Bangalore, India<br>dibakard@ieee.org

Mohammad Fahad Imteyaz<br>Tejas Networks<br>Bangalore, India<br>imteyaz@tejasnetworks.com

Jyotsna Bapat<br>IIIT Bangalore<br>Bangalore, India<br>jbapat@iiitb.ac.in

Debabrata Das<br>IIIT Bangalore<br>Bangalore, India<br>ddas@iiitb.ac.in

Abstract-Failures in optical network backbone can cause significant interruption in internet data traffic. Hence, it is very important to reduce such network outages. Prediction of such failures would be a step forward to avoid such disruption of internet services for users as well as operators. Several research proposals are available in the literature which are applications of data science and machine learning techniques. Most of the techniques rely on significant amount of real time data collection. Network devices are assumed to be equipped to collect data and these are then analysed by different algorithms to predict failures. Every network element which is already deployed in the field may not have these data gathering or analysis techniques designed into them initially. However, such mechanisms become necessary later when they are already deployed in the field. This paper proposes a Bayesian network based failure prediction of network nodes, e.g., routers etc., using very basic information from the log files of the devices and applying power law based data augmentation to complement for scarce real time information. Numerical results show that network node failure prediction can be performed with high accuracy using the proposed mechanism.

Index Terms-Bayesian Networks, data augmentation, optical, failure prediction

## I. INTRODUCTION

Today's digital world depend primarily on internet. Internet backbone network carries bulk of the data traffic from different users, such as, individuals, Internet of Things (IoT) devices, edges devices, computers and cloud. Backbone networks primarily use optical communications due to their high bandwidth and low bit error rates. These networks comprise of huge number of nodes, e.g., routers, etc., which carry data from one part of the world to the other. A failure in any of these nodes can lead to major disruption in internet services leading to losses in business and other activities. Hence, for reliable internet services it is essential to prevent failures proactively in backbone networks using intelligent mechanisms.

There are several approaches for failure prediction in optical networks. A gaussian classifier based approach to detect single link failures has been proposed in [1]. Authors applied heuristics to shortlist the probable failed links and then the gaussian classifier is applied to identify the failed link. [2] proposes support vector machine along with double exponential smoothing approach to predict optical network equipment failure. [3]

This research is funded by Tejas Networks, Bangalore, India
describes a method for prediction of link quality estimate in wireless sensor networks using online and offline supervised learning. A comparison of three data mining approaches, KMeans, Fuzzy C-Means, and Expectation Maximization, to detect abnormal behaviour in networks is proposed in [4]. Using Bayesian networks, [5] derives a mechanism to predict failures in cellular networks.

Most of the proposals mentioned above are data intensive. They rely on collecting real time data from various monitors in the network and then analyze the data to predict failures. For deployed systems in the field, such prediction mechanism may not be built into the initial design. However, subsequently, a need for failure prediction arises. In such a scenario, nonavailability of relevant data is a major hindrance. Changes to the deployed system like introducing new probes to collect data are highly risky. Hence, applying convention data intensive techniques are not possible. Non-intrusive failure prediction techniques have to be developed with very little information available (quantitative or qualitative) without disturbing the deployed network. This paper proposes such a technique using Bayesian Networks (BN) as explained below. In [6], we described an architecture for non-intrusive fault prediction in network nodes. It applies an ad-hoc node failure prediction mechanism as an initial solution. This paper extends and generalizes the network node failure prediction mechanism in [6] applying formal approach of data augmented BN.

Network nodes are equipped with log files which are used by the developers to debug problems. Observing the logs of past failures, patterns emerge on the sequence of events leading to a failure. These events can be represented as nodes in a Directed Acyclic Graph (DAG). This DAG can used as BN based failure prediction mechanism. Bayesian networks need conditional probabilities of a node (event) given its parents in the DAG for prediction. As already mentioned above, statistics on events and failures are not readily available in deployed network nodes. However, qualitative information on how frequently or infrequently a failure occurs can be acquired from the developers. Using this information, data augmentation is applied to generate the conditional probabilities assuming power law distribution for failure occurrences. The BN uses these probabilities and predicts failures as events occur in real-

time. Numerical results show, even with scarce data available from logs retrieved from the deployed network nodes, fairly accurate failure prediction is possible.

Objectives behind this BN based approach are as follows.

- Construct a quick solution to meet time to market requirements
- Construct a non-intrusive prediction mechanism devoid of any changes in the deployed network
- Effectively use information from the logs and qualitative information on frequency of occurrence of failures from the developers
- Failure prediction mechanism should evolve over time

The remaining of this paper is organized as follows. Section II describes the proposed idea and the system model. The results obtained applying the proposed idea are presented in section III. Section IV concludes this work with some future directions.

## II. SYSTEM MODEL

As already mentioned, the statistical information about the occurrence of events and failures at network nodes is not readily known, since the deployed systems are not equipped with necessary mechanisms to collect such data by initial design. Mining all the historical logs to extract statistical information mentioned above can be a extremely time consuming approach and may not meet time to market requirements. The only information extracted from the logs is the sequence of events leading to failures with the help of the developers. Also, qualitative information on which errors occur more frequently than others can be known from the experience of the developers.

An example log file is shown in Fig. 1. The first column contains the time at the which the corresponding text (second column) is logged and associated values of system parameters, e.g., clock drift, Optical Signal To Noise Ratio (OSNR), etc. Based on analysis of the developers some of the texts can be designated as events shown in third column of Fig. 1. There can be several events, such as, clock drift exceeding certain threshold, temperature rising above a certain value, OSNR exceeding lower threshold, or a node not receiving signal from its peer. Once the failures and their corresponding events are designed from the logs, they are presented in form of a matrix as shown in (1) for 5 failures. Each row in the matrix represents a sequence of events leading to a failure. A value 1 means that the corresponding event has to happen for that particular failure. For example, event $E_{2}$ has to happen for failures $F_{1}$, $F_{2}$ and $F_{3}$, not for $F_{4}$ and $F_{5}$. Subsequently, a DAG comprising all the events can be constructed (Fig. 2) which forms the BN. For example, event $E_{1} \rightarrow E_{2} \rightarrow E_{3} \rightarrow$ $E_{5}$ have to occur in sequence for failure $F_{2}$. Note that $E_{1}$ and $E_{2}$ (marked in red) are the valid start states of event sequences leading to failures. By (1), $F_{1}, F_{2}, F_{4}$ and $F_{5}$ start with $E_{1}$, and $F_{3}$ starts with $E_{2}$.
![img-0.jpeg](img-0.jpeg)

Figure 1. Example log file with events
![img-1.jpeg](img-1.jpeg)

Figure 2. DAG constructed using (1)

$$
E_{5,5}=\begin{gathered}
F_{1} \\
F_{2} \\
F_{3} \\
F_{4} \\
F_{5}
\end{gathered}\left[\begin{array}{cccccc}
E_{1} & E_{2} & E_{3} & E_{4} & E_{5} \\
1 & 1 & 0 & 1 & 1 \\
1 & 1 & 1 & 0 & 1 \\
0 & 1 & 0 & 1 & 1 \\
1 & 0 & 1 & 1 & 0 \\
1 & 0 & 1 & 0 & 1
\end{array}\right]
$$

## A. Generation of statistics for events and failures

To apply BN for failure prediction, statistics of occurrence of events and their failures are necessary to calculate the conditional probabilities. However, as already mentioned such statistics are not readily available. For this purpose, two available information are used. Firstly, events are extracted from old logs as explained above. Secondly, developers can provide the information on which failures occur more frequently than others. Based on this information, a probability distribution can be assumed to artificially create statistics of the events and their corresponding failures. Since, there is non-zero chance of any failure a scale free probability distribution can be assumed. For this purpose, a power law probability distribution

is assumed in (2) for occurrence of $N$ failures, though other scale free functions can also be considered (in future).

$$
p(x)=a x^{-k}
$$

where $a$ is constant and failure $F_{x}$ occurs with probability $p(x), x=1,2, . ., N$ and $k \geq 2$. Also, it is assumed that $p(i)>p(j)$ for $i<j$ and $i, j \in\{1,2, . ., N\}$. Value of $a$ can be adjusted so that,

$$
\sum_{x=1}^{N} p(x) \approx 1
$$

Based on the probability distribution function, statistics of each of the failures can be calculated as follows using (4).

$$
C_{F_{x}}=\lfloor S \times p(x)\rfloor
$$

where $C_{F_{x}}$ is the number of occurrences of $F_{x}$ in the population of $S$ failures.

Once the number of occurrence of each failure is estimated with (4), the statistics of the events can also be found out using (1). Using all these augmented data and information, a BN can be constructed with all the conditional probabilities.

## B. Application of Bayesian Networks

Application of BN is explained with the following scenerio. Lets evaluate the probabilities of occurrences of $E_{4}$ and $E_{5}$ given $E_{1}=1$ (Fig. 2) as shown in (5). Note that there are 4 possible combinations for $E_{4}$ and $E_{5}$.

$$
\operatorname{Pr}\left(E_{5}, E_{4} \mid E_{1}=1\right)=\frac{\operatorname{Pr}\left(E_{5}, E_{4}\right)}{\operatorname{Pr}\left(E_{1}=1\right)}
$$

$E_{4}$ and $E_{5}$ depend on other predecessors (Fig. 2), so the above equation has to be expanded as follows.

$$
\begin{aligned}
& \Rightarrow \operatorname{Pr}\left(E_{5}, E_{4} \mid E_{1}=1\right)=\frac{1}{\operatorname{Pr}\left(E_{1}=1\right)} \\
& \times \sum_{E_{3}} \sum_{E_{2}} \operatorname{Pr}\left(E_{5}, E_{4}, E_{3}, E_{2}\right) \\
& \Rightarrow \operatorname{Pr}\left(E_{5}, E_{4} \mid E_{1}=1\right)=\frac{1}{\operatorname{Pr}\left(E_{1}=1\right)} \\
& \times \sum_{E_{3}} \sum_{E_{2}} \operatorname{Pr}\left(E_{5} \mid E 4, E 3\right) \\
& \times \operatorname{Pr}\left(E_{4} \mid E 3, E 2\right) \\
& \times \operatorname{Pr}\left(E_{3} \mid E 2, E 1\right) \\
& \times \operatorname{Pr}\left(E_{2} \mid E_{1}\right) \\
& \Rightarrow \operatorname{Pr}\left(E_{5}, E_{4} \mid E_{1}=1\right)=\frac{1}{\operatorname{Pr}\left(E_{1}=1\right)} \\
& \times\left\{\sum_{E_{3}} \operatorname{Pr}\left(E_{5} \mid E 4, E 3\right) \times\left(\sum_{E_{2}}\right.\right. \\
& \times \operatorname{Pr}\left(E_{4} \mid E 3, E 2\right) \\
& \left.\times \operatorname{Pr}\left(E_{3} \mid E 2, E 1\right)\right. \\
& \left.\left.\times \operatorname{Pr}\left(E_{2} \mid E_{1}\right)\right)\right\}
\end{aligned}
$$

Thus, $\operatorname{Pr}\left(E_{5}, E_{4} \mid E_{1}=1\right)$ is expressed as conditional probabilities of occurrences of its predecessors in Fig. 2. These derivations have to be repeated for each combination of events. It is evident, when the BN is large, these derivations can be extremely tedious and cumbersome.

## C. Failure Prediction

Once the BN is constructed as explained above, failure prediction is performed based on the events happening in real time, extracted from network node logs and traversing the BN. A remote machine, running the proposed BN failure prediction model, transfers the real time logs from the network nodes using remote copy, etc., parses the logs for events, using the architecture proposed in [6].

## III. ReSults and DisCussion

This section presents the results obtained using the system model in section II. The model is implemented in python using pgmpy library [7]. The first step is the generation of statistics of occurrence of failures. Using the generated statistics, the failures are predicted using BN. Calculating the conditional probabilities given all its predecessors of a event in the BN manually for equations such as (8) can be extremely cumbersome, tedious and error-prone when the network is large (which is expected to be in future). Hence, using a tool such as pgmpy can be extremely beneficial to reliably calculate the probabilities.

## A. Generation of failure statistics

For generation of population of failures the power law distribution in (2) is used with $k=2, N=5, a=0.7$ satisfying (3). Number of each failures $F_{i}, i=1,2,3,4,5$ is shown in Fig. 3 and the probability distribution of failures is shown in Fig. 4, under the assumption that occurrence frequency of $F_{1}>$ occurrence frequency of $F_{2}>$ occurrence frequency of $F_{3}>$ occurrence frequency of $F_{4}>$ occurrence frequency of $F_{5}$, available from the qualitative information provided by the developers. Ten thousand samples of failures are generated. The probabilities of the events are shown in Fig. 5.

## B. Application of BN

Using the augmented data described above in section III-A, the conditional probabilities necessary for prediction of failures applying BN are calculated. Probabilities of $E_{1}$ are shown in Table I. Similarly, the probabilities of $E_{2}$ given its parent $E_{1}$

Table I
Probabilities of $E_{1}$


(Fig. 2) occurred or not are provided in Table II. Likewise, the same for $E_{3}$ is provided in Table. III. Note that probabilities of $E_{3}$ given $E_{1}=0$ and $E_{2}=0$ are not valid failures in current set (1). However, pgmpy needs all the combinations of

![img-2.jpeg](img-2.jpeg)

Figure 3. Number of each failure $F_{i}$ in the power law distributed population

![img-3.jpeg](img-3.jpeg)

Figure 4. Probability of each failure $F_{i}$ in the power law distributed population

probabilities of nodes given their parents to be made available and each row in the tables should add up to 1. This does not adversely affect the performance of the prediction model as the results show subsequently. The probabilities of $E_{4}$ and $E_{5}$ given their respective parents are shown in Tables IV and V. These probabilities are then fed into the BN for failure prediction.

Table II PROBABILITIES OF $E_{2}$


Non-occurrence of an event, i.e., $E_1 = 0$, is hard to provide as evidence to the BN. Hence, occurrence of event is always set as evidence to predict the failures. The tool takes all the probabilities provided in that tables above and outputs the prediction after calculating the equations such as (8).

If function call to query the BN for prediction of the

![img-4.jpeg](img-4.jpeg)

Figure 5. Probability of each event $E_i$ in the power law distributed population

Table III PROBABILITIES OF $E_3$


subsequent events with the evidence that $E_1$ has already occurred, its output predicts $F_1$ defined in (1) as shown below. The PREDICTION is concatenation of evidence and OUTPUT.

```
FUNCTION CALL:
infer.map_query(['E2', 'E3',
    'E4', 'E5'],
    evidence={'E1': '1'})
OUTPUT:
    {'E2': '1', 'E3': '0',
    'E4': '1', 'E5': '1'}
PREDICTION:
    {'E1': '1', 'E2': '1', 'E3': '0',
    'E4': '1', 'E5': '1'} --> Failure F1
```

Afterwards, when events $E_1$ and $E_2$ occur which are presented as evidence to the BN, it continues to predict failure $F_1$.

```
FUNCTION CALL:
infer.map_query(['E3', 'E4', 'E5'],
    evidence={
    'E1': '1',
    'E2': '1'})
OUTPUT:
    {'E3': '0', 'E4': '1', 'E5': '1'}
PREDICTION:
    {'E1': '1', 'E2': '1', 'E3': '0',
    'E4': '1', 'E5': '1'} --> Failure F1
```

With evidence $E_1$, $E_2$ and $E_3$, the BN changes its prediction from $F_1$ to $F_2$ as defined in (1).

Table IV
Probabilities of $E_{4}$


Table V
Probabilities of $E_{5}$


FUNCTION CALL:
infer.map_query(['E4', 'E5'],
evidence $=\{$
'E1': '1',
'E2': '1',
'E3': '1'\})
OUTPUT:
\{'E4': '0', 'E5': '1'\}
PREDICTION:
\{'E1': '1', 'E2': '1', 'E3': '1',
'E4': '0', 'E5': '1'\} --> Failure F2
However, if occurrence of $E_{1}, E_{2}, E_{3}$ and $E_{4}$ are provided as evidence then it correctly detects an invalid event since the output does not match with any row in (1).
FUNCTION CALL:
infer.map_query(['E5'],
evidence $=\{$
'E1': '1',
'E2': '1',
'E3': '1',
'E4': '1'\})
OUTPUT:
\{'E5': '0'\}
PREDICTION:
\{'E1': '1', 'E2': '1',
'E3': '1', 'E4': '1',
'E5': '0'\} --> invalid event
If occurrence of events $E_{2}$ and $E_{4}$ are provided as evidence then the BN predicts $F_{3}$ as expected.
FUNCTION CALL:
infer.map_query(['E5'],
evidence $=\{$
'E2': '1',
'E4': '1'\})
OUTPUT:
\{'E5': '1'\}

PREDICTION:

$$
\begin{aligned}
& \text { \{'E1': '0', 'E2': '1', 'E3': '0', } \\
& \text { 'E4': '1', 'E5': '1'\} --> Failure F3 }
\end{aligned}
$$

If events $E_{1}$ and $E_{3}$ are evidences, then $F_{4}$ is predicted due to its higher probability (Fig. 4).
FUNCTION CALL:
infer.map_query(['E4', 'E5'],
evidence $=\{$
'E1': '1',
'E3': '1'\})
OUTPUT:
\{'E4': '1', 'E5': '0'\}
PREDICTION:
\{'E1': '1', 'E2': '0', 'E3': '1',
'E4': '1', 'E5': '0'\} --> Failure F4
To predict $F_{5}$, the query has to happen on the evidence that $E 4$ has occurred, since it is the only difference between $F_{4}$ and $F_{5}$, and $E_{1}, E_{3}$ and $E_{5}$ have to occur. Doing so, the BN predicts $F_{5}$ correctly.

```
FUNCTION CALL:
infer.map_query(['E4'],
    evidence={
    'E1': '1',
    'E3': '1',
    'E5': '1'})
OUTPUT:
    ('E4': '0')
PREDICTION:
    ('E1': '1', 'E2': '0', 'E3': '1',
    'E4': '0', 'E5': '1'\} --> Failure F5
```


## IV. CONCLUSION AND FUTURE WORK

Failures in backbone optical networks can lead to major disruption in internet traffic. Hence, prediction of such failures can avoid such problems. This paper proposed an data augmented BN to predict failures of networks node using some information from logs and (qualitative) inputs from developers on frequency of occurrence of failures. The conditional probabilities of the BN is calculated after generation of failure population applying a power law distribution of the failures based on their frequency of occurrences. Results show that the proposed node failure prediction mechanism is able to perform with high accuracy.

Future work will extend the model to more nodes in the BN and integrate this to the deployed network.

## ACKNOWLEDGMENT

This research project is funded by Tejas Networks, Bangalore, India.
