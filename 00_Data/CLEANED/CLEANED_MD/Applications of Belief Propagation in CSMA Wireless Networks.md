# Applications of Belief Propagation in CSMA Wireless Networks 

Cai Hong Kai, Soung Chang Liew<br>Department of Information Engineering, The Chinese University of Hong Kong<br>Email: \{chkai6, soung\}@ie.cuhk.edu.hk


#### Abstract

The belief propagation (BP) algorithm is an efficient way to solve "inference" problems in graphical models, such as Bayesian networks and Markov random fields. The sys-tem-state probability distribution of CSMA wireless networks is a Markov random field. An interesting question is how BP can help the analysis and design of CSMA wireless networks. This paper explores three such applications. First, we show how BP can be used to compute the throughputs of different links in the network given their access intensities, defined as the mean packet transmission time divided by the mean backoff countdown time. Second, we propose an inverse-BP algorithm to solve the reverse problem: how to set the access intensities of different links to meet their target throughputs? Third, we introduce a BP-adaptive CSMA algorithm to find the link access intensities that can achieve optimal system utility. BP solves the three problems with exact results in networks with tree contention graph. It may, however, lose accuracy in networks with a loopy contention graph. We then show how a generalized version of BP, GBP, can be designed to solve the three problems with high accuracy for networks with loopy contention graph. Importantly, we show how the BP and GBP algorithms in this paper can be implemented in a distributed manner, making them useful in practical CSMA network operation.


Index Terms -Belief propagation, CSMA, IEEE 802.11.

## I. INTRODUCTION

With the widespread deployment of IEEE 802.11 networks, it is common today to find multiple wireless LANs co-located in the neighborhood of each other. The multiple wireless LANs form an overall large network whose links interact and compete for airtime using the carrier-sense multiple access (CSMA) protocol. The carrier sensing relationships among these links are often "non-all-inclusive" in that each link may sense only a subset, but not all, of other links.

For analytical purposes, the carrier sensing relationships among the links are typically captured using a contention graph. The links are modeled by vertices of the graph, and an edge joins two vertices if the transmitters of the two associated links can sense each other. Since different links may sense different subsets of other links, the links may experience different throughputs in the network.

Ref. [1] presented an analytical model, Ideal CSMA Network (ICN), to study the behavior of CSMA networks given their contention graphs. It was shown that the throughputs of links can be computed from the stationary probability distribution of the states of a continuous-time Markov chain. Fur-
thermore, the contention graph associated with ICN is a Markov random field [2] with respect to the probability distribution of its system states. The belief propagation (BP) algorithm is an efficient way to solve "inference" problems in graphical models, such as Bayesian networks and Markov random fields [3]. An interesting question, therefore, is how BP can help the analysis and design of CSMA wireless networks.

This paper considers three applications of BP in CSMA networks. To the best of our knowledge, this is the first paper to use the BP framework to solve problems related to CSMA networks. Importantly, we show that all three problems are amenable to solutions by distributed algorithms under the BP framework.

The first and the most direct application is to use BP to compute (infer) the throughputs of different links in a CSMA network given their access intensities. The access intensity of a link is the ratio of its average packet transmission time to its average backoff countdown time. Higher access intensity corresponds to higher aggressiveness of the link when it competes for airtime under the CSMA protocol. BP gives exact solutions for tree contention graphs and acceptable approximate solutions for loopy contention graphs. We show that an improved algorithm, generalized belief algorithm (GBP), can reduce the errors induced by loops significantly.

The second application is the reverse problem of computing the link access intensities to meet the target link throughputs. We propose an Inverse Belief Propagation (IBP) algorithm for this purpose. IBP can quickly output the approximate link access intensities required. Analogous to GBP, we propose IGBP to reduce the errors in the access intensities found.

The third application is on network utility optimization. We propose a BP-adaptive CSMA algorithm (BP-ACSMA) to adaptively achieve the optimal system utility. Compared with prior work, an advantage of BP-ACSMA is that it is a proactive computational algorithm without the need for network probing and traffic measurement. As with GBP and IGBP, we propose GBP-ACSMA for higher accuracy in loopy graphs. Our simulation results indicate that the achieved aggregate throughputs and system utility are near optimal.

## Related Work

There have been numerous publications on non-all-inclusive carrier-sense networks and this is indeed a "hot topic" among researchers. Recent work includes [1], [4]-[6], from which earlier work can be traced. Among them, [1] proposed a quick "back-of-the-envelope" (BoE) algorithm

for link throughputs computation in CSMA wireless networks. BoE could handle networks of up to 50 links with high accuracy and speed. Networks of larger size were left as an open issue. The BP algorithm proposed in this paper fills this gap.

Besides throughput computation, this paper proposes and investigates two other applications of BP: (1) computation of link access intensities required to meet target link throughputs; (2) optimization of network utility. The existing algorithms proposed in [7] are based on "probe and measure". Specifically, before a link adjusts its access intensity, a period of "smoothing" time is needed to measure the difference in the link's input traffic and output traffic. As will be shown in this paper, the required smoothing time can be quite excessive in networks that exhibit temporal starvation, resulting in very slow convergence. By contrast, BP-based algorithms proposed here do not have this problem because they are computa-tion-based rather than measurement-based.

BP as an inference-making methodology has been studied extensively. A good reference for BP is [8]. We believe ours is the first paper to explore the applications of BP in CSMA networks. Ref. [8] also presents GBP, without focusing on specific application domains. An important contribution of our paper is to show that a "maximal clique" method of forming "regions" in GBP allows us to design adaptive distributed GBP algorithms for CSMA networks. Furthermore, this re-gion-forming method yields good performance.

## Paper Organization

The remainder of the paper is organized as follows. Section II introduces our system model and reviews the throughput computation of CSMA wireless networks. Section III shows how to use BP for throughput computation in large CSMA wireless networks. Section IV investigates the reverse problem: given the target link throughputs, how to find the link access intensities to meet them. Section V proposes the BP-ACSMA algorithm for network utility optimization. Section VI shows how GBP can be used to solve the same problems as in Sections III-V, but with higher accuracy. Section VII concludes this paper.

## II. SYSTEM MODEL

In this section, we first review an idealized version of the CSMA network (ICN) to capture the main features of the CSMA protocol responsible for the interaction and dependency among links. The ICN model was used in several prior investigations [1][4][5][7]. The correspondence between ICN and the IEEE 802.11 protocol [9] can be found in [1].

## A. The ICN model

In ICN, the carrier-sensing relationship among links is described by a contention graph $G=(V, E)^{1}$. Each link is modeled as a vertex $i \in V$. Edges, on the other hand, model the carrier-sensing relationships among links. There is an edge $e \in E$ between two vertices if the transmitters of the two as-

[^0]sociated links can sense each other. In this paper we will use the terms "links" and "vertices" interchangeably.

At any time, a link is in one of two possible states, active or idle. A link is active if there is a data transmission between its two end nodes. Thanks to carrier sensing, any two links that can hear each other will refrain from being active at the same time. A link sees the channel as idle if and only if none of its neighbors is active.

In ICN, each link maintains a backoff timer, $C$, the initial value of which is a random variable with an arbitrary distribution $f\left(t_{c d}\right)$ and mean $E\left[t_{c d}\right]$. The timer value of the link decreases in a continuous manner with $d C / d t=-1$ as long as the link senses the channel as idle. If the channel is sensed busy (due to a neighbor transmitting), the countdown process is frozen and $d C / d t=0$. When the channel becomes idle again, the countdown continues and $d C / d t=-1$ with $C$ initialized to the previous frozen value. When $C$ reaches 0 , the link transmits a packet. The transmission duration is a random variable with arbitrary distribution $g\left(t_{a}\right)$ and mean $E\left[t_{a}\right]$. After the transmission, the link resets $C$ to a new random value according to the distribution $f\left(t_{c d}\right)$, and the process repeats. We define the access intensity of a link as the ratio of its mean transmission duration to its mean backoff time: $\rho=E\left[t_{a}\right] / E\left[t_{c d}\right]$.

Let $s_{i} \in\{0,1\}$ denote the state of link $i$, where $s_{i}=1$ if link $i$ is active (transmitting) and $s_{i}=0$ if link $i$ is idle (actively counting down or frozen). The overall system state of ICN is $s=s_{1} s_{2} \ldots s_{N}$, where $N$ is the number of links in the network. Note that $s_{i}$ and $s_{j}$ cannot both be 1 at the same time if links $i$ and $j$ are neighbors because (i) they can sense each other; and (ii) the probability of them counting down to zero and transmitting together is 0 under ICN (because the backoff time is a continuous random variable).

The collection of feasible states corresponds to the collection of independent sets of the contention graph. An independent set (IS) of a graph is a subset of vertices such that no edge joins any two of them [8].
![img-0.jpeg](img-0.jpeg)

Fig. 1. (a) An example contention graph and (b) its state-transition diagram.
As an example, Fig. 1(b) shows the state-transition diagram of the contention graph in Fig. 1(a) under the ICN model. To avoid clutters, we have merged the two directional transitions between two states into one line in Fig. 1(b). Each transition from left to right corresponds to the beginning of the transmission of one particular link, while the reverse transition corresponds to the ending of the


[^0]:    ${ }^{1}$ The mapping from network topology to contention graph has been studied in several prior works (e.g., [10]).

transmission of that link. For example, the transition $1000 \rightarrow 1010$ is due to link 3 's beginning to transmit; the reverse transition $1010 \rightarrow 1000$ is due to link 3 's completing its transmission.

## B. Equilibrium analysis

If we further assume that the backoff time and transmission time are exponentially distributed, then $s(t)$ is a time-reversible Markov process. For any pair of neighbor states in the continuous-time Markov chain, the transition from the left state to the right state occurs at rate $1 / E\left[t_{o d}\right]$, and the transition from the right state to the left state occurs at rate $1 / E\left[t_{o r}\right]$.

Let $\mathcal{S}$ denote the set of all feasible states, and $n_{s}$ be the number of transmitting links when the system is in state $s=s_{1} s_{2} \ldots s_{N}$. The stationary distribution of state $s$ is given by $[1]^{2}$ :

$$
P_{s}=\frac{P_{s}^{n_{s}}}{Z} \quad \forall s \in \mathcal{S}, \quad \text { where } Z=\sum_{s \in \mathcal{S}} P_{s}^{n_{s}}
$$

The fraction of time during which link $i$ transmits is $t h_{i}=\sum_{s: s_{i}=i} P_{s}$, which corresponds to the normalized throughput of link $i$.

Ref. [1] showed that (1) is in fact quite general and does not require the system state $s(t)$ to be a Markov process. In particular, (1) is insensitive to the distribution of the transmission duration $g\left(t_{o r}\right)$, and the distribution of the backoff duration $f\left(t_{o d}\right)$, given the ratio of their mean $\rho$.

Applying (1) to the state-transition diagram of Fig. 1 gives

$$
\begin{aligned}
& P_{6000}=1 / Z=1 /\left(1+4 \rho+2 \rho^{2}\right) \\
& P_{6000}=P_{6000}=P_{6010}=P_{6001}=\rho /\left(1+4 \rho+2 \rho^{2}\right) \\
& P_{1010}=P_{1001}=\rho^{2} /\left(1+4 \rho+2 \rho^{2}\right)
\end{aligned}
$$

The normalized throughputs of the links are then given by

$$
\begin{aligned}
& t h_{1}=P_{1000}+P_{1010}+P_{1001}=\left(\rho+2 \rho^{2}\right) /\left(1+4 \rho+2 \rho^{2}\right) \\
& t h_{2}=P_{1010}=\rho /\left(1+4 \rho+2 \rho^{2}\right) \\
& t h_{3}=P_{1010}+P_{1010}=\left(\rho+\rho^{2}\right) /\left(1+4 \rho+2 \rho^{2}\right) \\
& t h_{4}=P_{6001}+P_{1001}=\left(\rho+\rho^{2}\right) /\left(1+4 \rho+2 \rho^{2}\right)
\end{aligned}
$$

Note that $Z$ is a weighted sum of independent sets of $G$. In statistical physics, $Z$ is referred to as the partition function and the computation of $Z$ is the crux of many problems. We could also define $Z_{i}$ to be the weighted sum of the subset of independent sets in which $s_{i}=1$. Then, $t h_{i}$ could be equivalently expressed as $t h_{i}=Z_{i} / Z$. This expression will be used later in the Appendix A.

[^0]
## III. THROUGHPUT COMPUTATION USING BP

This section describes a direct application of BP in CSMA wireless networks: quick computation of the throughputs of links.

## A. Motivation

Exact link-throughput computation requires the computation of $Z_{i}$ and $Z$, which is an NP-hard problem, since it involves finding all the independent sets of a contention graph. Thus, the problem can become intractable for large CSMA networks. As detailed in [1], for networks of more than 100 links, ICN computation can be rather time-consuming. An outstanding problem is to find quick and accurate approximate methods for large CSMA networks. This section is dedicated to this pursuit using BP.

## B. Graphical model in BP

Under the framework of BP, the dependency between the states $s_{i}$ and $s_{j}$ of two neighbor vertices, $i$ and $j$, is captured using a compatibility function $\psi_{i j}\left(s_{i}, s_{j}\right)$, defined as follows:

$$
\psi_{i j}\left(s_{i}, s_{j}\right)=\left\{\begin{array}{ll}
0 & \text { if } s_{i}=1, s_{j}=1 \\
1 & \text { otherwise }
\end{array}\right.
$$

In other words, the state $s_{i}=1$ and the state $s_{j}=1$ are not compatible because under CSMA, the two neighbor links cannot transmit together.

In addition, a weight is given to each possible state $s_{i}$ as follows:

$$
\emptyset_{i}\left(s_{i}=1\right)=\rho_{i} ; \quad \emptyset_{i}\left(s_{i}=0\right)=1
$$

Note that $\emptyset_{i}\left(s_{i}=1\right)$ and $\emptyset_{i}\left(s_{i}=0\right)$ capture the relative likelihoods of states $s_{i}=1$ and $s_{i}=0$ if link $i$ were an isolated link without neighbors.

It is not difficult to verify that the stationary probability of the system state $s=s_{1} s_{2}, \ldots, s_{N}$ in (1) can be rewritten as

$$
P_{s}=\prod_{s_{1}, s_{N} \in} \psi_{i j}\left(s_{i}, s_{j}\right) \prod_{s \in s_{i}} \phi_{i}\left(s_{i}\right)
$$

In ICN, the normalized throughput of link $i$ is the marginal probability $p_{i}\left(s_{i}=1\right)=\sum_{s: s_{i}=1} P_{s}$. In the context of BP, $p_{i}\left(s_{i}\right), s_{i} \in\{0,1\}$, corresponds to the belief at vertex $i$, denoted by $b_{i}\left(s_{i}\right)$.

## C. Message update rules in $B P$

With the stationary distribution expressed in the form of (5), we next show how to use the BP algorithm to solve for $p_{i}\left(s_{i}=1\right)$. The reader is referred to [8] for a general and detailed treatment of BP. Here, we focus on BP as applied to CSMA networks only.

When applying BP to CSMA networks, each vertex $i$ has an "intrinsic" belief of what the value of $p_{i}\left(s_{i}\right)$ should be. This intrinsic belief corresponds to the "on" probability when link $i$ is an isolated link. For an isolated link, $p_{i}\left(s_{i}=1\right)=\rho_{i} /\left(1+\rho_{i}\right) \propto \phi_{i}\left(s_{i}=1\right) \quad, \quad$ and $\quad p_{i}\left(s_{i}=0\right)=$


[^0]:    ${ }^{2}$ Here, we assume all links have the same access intensity $\rho=E\left[t_{o r}\right] / E\left[t_{o d}\right]$. For the case where different links have difference access intensities, (1) can be generalized by replacing $\rho^{n_{s}}$ with the $\prod_{s s_{i}=1 \text { in } s} \rho_{i}$.

$1 /\left(1+\rho_{i}\right) \propto \phi_{i}\left(s_{i}=0\right)$. That is, $p_{i}\left(s_{i}\right) \propto \phi_{i}\left(s_{i}\right)$ for an isolated link.

In addition, each vertex $i$ receives messages from its neighbors as to what they "think" $p_{i}\left(s_{i}\right)$ should be. Let $N_{i}$ denote the neighbors of vertex $i$ in $G$. Each neighbor $j \in N_{i}$ passes a message $m_{j i}\left(s_{i}\right)$ to $i$ as to its "belief" of $p_{i}\left(s_{i}\right)$. The beliefs of $i$ and all $j \in N_{i}$ are then aggregated into an overall belief in the form of a product:

$$
b_{i}\left(s_{i}\right)=k_{i} \phi_{i}\left(s_{i}\right) \prod_{j \in N_{i}} m_{j i}\left(s_{i}\right)
$$

where $k_{i}$ is a normalization constant so that $\sum_{s_{i} \in[0,1]} b_{i}\left(s_{i}\right)=1$.

The messages are determined by the message update rule:

$$
\begin{aligned}
m_{j i}\left(s_{i}\right) & \leftarrow \sum_{s_{j} \in[0,1]} \psi_{i j}\left(s_{i}, s_{j}\right) \phi_{i}\left(s_{j}\right) \prod_{k \in N_{j} \backslash i} m_{k j}\left(s_{j}\right) \\
& =\sum_{s_{j} \in[0,1]} \psi_{i j}\left(s_{i}, s_{j}\right) b_{j}\left(s_{j}\right) /\left(k_{j} m_{i j}\left(s_{j}\right)\right)
\end{aligned}
$$

Note that $\phi_{i}\left(s_{j}\right) \prod_{k \in N_{j} \backslash i} m_{k j}\left(s_{j}\right) \propto b_{j}\left(s_{j}\right) / m_{i j}\left(s_{j}\right)$. That is, it is proportional to the aggregated belief at vertex $j$ with the message from $i$ to $j$ factored out. In tree graphs, this message update rule can also be understood as the expression of the Bayes' formula [8].

The BP algorithm iterates (7) over all vertices $i$. In each iteration, we could normalize the messages according to $\sum_{s_{i} \in[0,1]} m_{j i}\left(s_{i}\right)=1$ for $\forall j^{3}$. The iteration stops when $m_{j i}\left(s_{i}\right)$ converges.

It can be shown that (6) and (7) give exact solutions in tree graphs. Appendix A shows that in networks with a tree contention graph, the BP messages can be interpreted as the partition functions of subgraphs. This interpretation gives an explanation on why BP can give exact solutions in networks with loop-free graphs. Furthermore, each message needs only be computed once before convergence in trees. In other words, if there are no loops in the contention graph, (6) and (7) can solve ICN exactly within a time proportional to the number of edges in the graph. For loopy graphs, BP can often give good approximate results as well [8].

## D. Distributed BP

BP can be easily implemented in a distributed manner. We focus on a particular vertex $j$. It stores a record of $N_{j}$ and the received messages from its neighbors, denoted by $M_{j}=\left\{m_{i j}\left(s_{j}\right), \forall i \in N_{j}\right\}$.

Each vertex $j$ operates as follows: Initially, vertex $j$ sets its outgoing messages $m_{j i}\left(s_{i}\right)$ to $\sum_{s_{j} \in[0,1]} \phi_{j}\left(s_{j}\right) \psi_{i j}\left(s_{i}, s_{j}\right), \forall i \in N_{j}$. In each iteration, it passes $m_{j i}\left(s_{i}\right)$ to vertex $i$ and waits for time $T$ to receive messages from its neighbors. The locally stored messages in $M_{j}$

[^0]are then updated. Using the updated messages, vertex $j$ computes its outgoing messages according to (7) and repeats the iteration. The throughput of link $j$ (i.e., $t h_{j}=b_{j}\left(s_{j}=1\right)$ ) can be computed based on the messages it stores according to (6). The pseudocode of distributed BP is given in Algorithm 1.

## Message Passing between Neighbors in $G$

Distributed BP requires two neighbors who can mutually carrier-sense each other to exchange messages. Since the car-rier-sensing range may be beyond the transmission range of regular data, the BP messages may need to be transmitted at a lower rate. The beacons in 802.11 typically use a lower data rate than the regular DATA packet, and BP messages can be carried on them. For further details, the reader is referred to [12], which proposed a scalable CSMA MAC protocol in which mutually interfering nodes also need to exchange information (note: look for the power-exchange algorithm in [12]).

## Periodical update to track dynamic network topology

In practice, the network contention graph may change dynamically with new nodes joining and existing nodes leaving the network. Even among existing nodes, they may become idle when their users are not actively using the network. To track the variations of the network topology, $N_{j}$ needs to be refreshed periodically.

## Applications of distributed BP

This distributed throughput computation algorithm provides an alternative way to estimate the throughputs of links in some network optimization problems. For example, in the adaptive CSMA algorithm in [7] and the "Wait-and-Hop" link frequency assignment algorithm in [13], decisions in each iteration are made based on the throughputs of links under the link access intensities and link frequency assignments of the last iteration, respectively. Both papers proposed to use real-time measurements to gather the throughputs of links. Accurate real-time throughput measurements, however, take time, especially in networks susceptible to temporal starvation [6]. In such a network, the throughput of a link can alternate between 0 and 1 in cycles of very long duration. To avoid triggering oscillations in the control mechanism, each measurement must be averaged over several such cycles. As a result, the optimization algorithms may converge slowly.

In contrast, the throughput computation using BP does not have such problems. The speed of convergence is determined by how frequently the links pass BP messages to each other. Our simulation in Section III-F shows that for a network of up to 200 links, BP converges within 100 iterations. In real networks (e.g., WLAN), we may use beacons to exchange BP messages. Each AP typically broadcasts a beacon every 0.1 second [9]; thus, distributed BP can give solutions within ten seconds. If BP messages are piggybacked onto the regular DATA packets, the speed of convergence can be even faster.

## Algorithm 1: Distributed BP

1. The following procedure runs on each individual vertex independently. We focus on a particular vertex $j$.


[^0]:    ${ }^{3}$ If we normalize the beliefs in (6) without normalizing the messages, the magnitudes of the messages may grow unbounded, but not the beliefs themselves. Thus, the algorithm may still be well-behaved if the beliefs converge quickly.

2. Vertex $j$ keeps track of its one-hop neighbors $N_{j}$ and the incoming messages $M_{j}=\left\{m_{n}\left(s_{j}\right), \forall i \in N_{j}\right\}$.
3. In distributed BP, $N_{j}$ are periodically refreshed.
4. procedure INITIALIZATION
5. $m_{p}\left(s_{i}\right), \quad \forall i \in N_{j} \leftarrow \sum_{s_{j} \in[0,1]} \phi_{j}\left(s_{j}\right) \psi_{p}\left(s_{i}, s_{j}\right)$
6. end procedure
7. procedure ITERATION
8. Pass $m_{p}\left(s_{i}\right)$ to vertex $i \forall i \in N_{j}$
9. Wait for time $T$ to receive messages from its neighbors, $m_{k}\left(s_{j}\right), \forall i \in N_{j}$ and update $M_{j}$ accordingly.
10. Compute $m_{p}\left(s_{i}\right), \forall i \in N_{j}$ according to (7)
11. Invoke procedure BELIEFCOMPUTATION and repeat procedure ITERATION
12. end procedure
13. procedure BELIEFCOMPUTATION
14. Compute its belief $b_{j}\left(s_{j}\right)$ according to (6) and in turn obtain throughput $t h_{j}$.
15. end procedure

## E. BP in loopy contention graphs

Although BP can often give good approximations, as pointed out in [14], if we apply BP in loopy contention graphs, the information may circulate indefinitely around the loops, and BP may give inaccurate solutions and even not converge.

Consider a triangular graph consisting of three vertices. In BP, messages are passed between each pair of neighboring vertices. Vertex 1 gives certain information to vertex 2 , some of which is included in the information from vertex 2 to vertex 3 and finally passed back to vertex 1 , where it is regarded as a "new" incoming message. This message contains information correlated with the original information at vertex 1 . The message update rule and the belief computation formula, however, do not take this correlation into account.

When the loop is large, the information a vertex $i$ gives out vanishes along the cycle back to $i$, resulting in a smaller computation error. It can be shown that BP converges to the fixed point $b_{i}\left(s_{i}=0\right)=\left(1+\sqrt{1+4 \rho}\right) / 2 \sqrt{1+4 \rho}$ for each vertex in any $N$-vertex ring graph regardless of $N$ (See Appendix $D$ ). Given a value of $\rho=\rho_{0}=83 / 15.5$ (typical in 802.11 networks), the errors of BP for different $N$ are

- $8 \%$ for the 3 -vertex ring;
- $0.1 \%$ for the 8 -vertex ring;
- Zero for the $N$-vertex ring as $N \rightarrow \infty$.

That is, the error of BP decreases as the length of the cycle increases.

From the ring example, we can see intuitively that for general graphs, small loops are the loops that cause the more significant errors. To contain the errors, we want to eliminate small loops in message propagation. This is the basic idea behind the generalized belief propagation (GBP). For easy comparison, in the next subsection we evaluate the performance of GBP together with BP first, leaving the theoretical details of GBP to Section VI.

## F. Experimental Evaluation

Ref. [1] proposed a quick "back-of-the-envelope" (BoE) algorithm for link throughputs computation in CSMA wireless networks. BoE could only handle networks of up to 50 links. Networks of larger size were left as an open issue. The focus of our experiment here is on the accuracy and speed of BP and GBP for networks of more than 50 links.

We implement both algorithms in a centralized manner using MATLAB programs. The simulations run on an IBM ThinkCentre M51 Desktop computer with 3.4 GHz Intel Pentium 4 processor. The throughputs computed by BP and GBP are compared with that obtained from an ICN-simulator to examine their accuracy. The CPU runtimes are presented to evaluate the speed of BP and GBP. Furthermore, we list the average number of iterations a link performs before convergence. This will be used to estimate the convergence time for distributed implementation in real networks. In our experiments, we define the minimum $n$ such that $\max _{j}\left|t h_{j}\left[n\right]-t h_{j}^{*}\right| / t h_{j}^{*}<1 \%$ is satisfied as the number of iterations for BP and GBP to achieve convergence, where $t h_{j}^{*}$ is the final converged value ${ }^{4}$.

In the first set of experiments, we randomly generate networks of different numbers of links. We vary the network area while maintaining the mean degree of links (number of neighbors per link) to around four. The access intensities of all links are set to $\rho=\rho_{0}=83 / 15.5$, which corresponds to that typically seen in 802.11 b networks. For each link, we calculate the error of the throughput obtained by BP and GBP relative to the simulated throughput obtained from the ICN simulator. The error is normalized by the maximum link throughput in the network. For each network setting, we randomly generate ten different topologies and the experimental data are averaged over the ten networks.

As shown in Table I, for networks of up to 200 links, the error of BP is kept to $7.0 \%$ or below, while the error of GBP is consistently lower than $1 \%$. The maximum error of GBP is about $0.6 \%$. As for computation complexity, BP is very fast while GBP can also output solutions within seconds.

Table I. Mean Link Throughput Errors, Runtimes and Numbers of Iterations of BP and GBP for Networks in which Each Vertex has on AVERAGE Four Neighbors.


Table II shows the scenario in which the number of links is fixed to 100 while the network area is varied. That is, the

[^0] [^0]: ${ }^{4}$ We use exponential averaging to smooth out the computed messages for GBP algorithms: i.e., $m_{a v s}[n]=(1-\alpha) m_{a v s}[n]+\alpha m[n], 0<\alpha<1$, where $m[n]$ is the newly computed message and $\alpha$ is the smoothing factor. $m[n]$ is recomputed in each iteration. For BP algorithms, we do not perform the procedure above because it converges smoothly even without the procedure.

mean degree of links is varied. Again, GBP gives more accurate results while costing more CPU time. The error of BP is still below $10 \%$.

Table II. Mean Link Throughput Errors, Runtimes and Numbers of ITERATIONS OF BP AND GBP FOR NETWORKS OF 100 LINKS.


In Table I and Table II, $\rho$ is set to $\rho_{0}=83 / 15.5$. A question is how well these algorithms work under different $\rho$. It is known that when $\rho$ is large, two neighbor vertices become more tightly coupled, and the message passing within a loop may incur more computational errors. Table III shows the accuracy of both algorithms for different $\rho$ in a 100 -link network with the mean degree of links equal to four. As can be seen, the mean error of BP increases with the value of $\rho$. More impressive is GBP, whose mean error is very small even for $\rho=4 \rho_{0}$. This shows that GBP performs well over a large range of $\rho$.

Table III. Mean Link Throughput Errors, Runtimes and Numbers of ITERATIONS OF BP AND GBP FOR NETWORKS OF DIFFERENT $\rho$.


For all the scenarios, both algorithms converge within dozens of iterations. That is, if implemented in a distributed manner in which each link passes a message every 0.1 second (e.g., we use beacons for message passing in a 802.11 network), both BP and GBP can obtain links throughputs within seconds in real networks.

## IV. COMPUTATION OF LINK ACCESS INTENSITIES GIVEN TARGET LINK THROUGHPUTS

This section proposes an inverse belief propagation (IBP) algorithm to compute the link access intensities required to meet target link throughputs. We show that IBP can be easily implemented in a distributed manner and only only-hop message passing is needed. We evaluate the speeds and accuracies of IBP and IGBP (to be presented in Section VI) by simulations.

## A. Motivation

In network design, an interesting problem is as follows. Given a network contention graph $G$ and a set of target link throughputs, how to set the link access intensities $\bar{\rho}$ to meet the target link throughputs.

For small networks, we can find $\bar{\rho}$ by solving (1) and $t h_{i}=\sum_{s, s_{i}=1} P_{i}$. However, similar to the throughput computation using (1), the computation becomes intractable when the network is large. IBP below gives appropriate approximate solutions within a short time.

## B. Definition of IBP

As described in Section III, the operation of BP is as follows. Given the contention graph of the network $G$ and the access intensities of links $\bar{\rho}$, BP computes the throughputs of links. That is, $\overline{i h}=B P(G, \bar{\rho})$.

Definition of IBP: We define $\bar{\rho}=B P^{-1}(G, \overline{i h})$ as the inverse operation of belief propagation for $\overline{i h}=B P(G, \bar{\rho})$, where $\overline{i h}$ is the vector of target link throughputs.

## C. Message update rules and its distributed implementation

1) Message update rules in IBP

As mentioned in Section III-B, the belief at vertex $j$ $b_{j}\left(s_{j}=1\right)$ corresponds to the link throughput. That is, the belief of each link $j, b_{j}\left(s_{j}\right)$ is given in IBP.

From (7) we obtain the message update rule

$$
m_{j i}\left(s_{i}\right) \leftarrow \sum_{s_{j} \in[0,1]} \psi_{i j}\left(s_{i}, s_{j}\right) b_{j}\left(s_{j}\right) /\left(k_{j} m_{i j}\left(s_{j}\right)\right)
$$

and from (6) we have

$$
\rho_{j}=\phi_{j}\left(s_{j}=1\right)=\frac{b_{j}\left(s_{j}=1\right) \prod_{i \in N_{j}} m_{i j}\left(s_{j}=0\right)}{b_{j}\left(s_{j}=0\right) \prod_{i \in N_{j}} m_{i j}\left(s_{j}=1\right)}
$$

The IBP algorithm iterates (8) over all vertices $j$. Similar to BP, in each iteration we could normalize the messages according to $\sum_{s_{i} \in[0,1]} m_{j i}\left(s_{i}\right)=1, \forall j$. The iteration stops when $m_{j i}\left(s_{i}\right)$ converges or a maximum number of iterations is reached.

Note that IBP, being an approximate algorithm, has computation errors which potentially can result in non-convergence of the algorithm. As will be demonstrated in Section VI-D, we can resort to IGBP for more accurate computation. Another reason for non-convergence is due to the problem formulation itself. We require the target $\overline{i h}$ to be feasible and then seek the $\bar{\rho}$ to achieve that. If the given $\overline{i h}$ is beyond the feasible region (as defined in Section II-C of [7]), then no matter what algorithm we use, there is no solution. Formulating the problem as a system utility optimization problem as in Section V removes this difficulty, as the algorithm would then iterate to zoom into a feasible $\overline{i h}$ that can achieve optimal system utility.

## 2) Distributed IBP

In real applications, it is desirable to make IBP work in a distributed manner. Again we focus on a particular vertex $j$

that knows its target throughput $t h_{t}$ (i.e., $b_{j}\left(s_{j}\right)$ ). Similar to distributed BP, vertex $j$ stores a record of $N_{j}$ and the messages from its neighbors, $M_{j}=\left(m_{0}\left(s_{j}\right), \forall i \in N_{j}\right)$.

The procedure that link $j$ operates is as follows: Initially, vertex $j$ sets its outgoing messages $m_{j i}\left(s_{i}\right)$ to $\sum_{s_{j} \in[0,1]} \psi_{i i}\left(s_{i}, s_{j}\right) b_{j}\left(s_{j}\right), \forall i \in N_{j}$. In each iteration, it passes $m_{j i}\left(s_{i}\right)$ to vertex $i$ and waits for time $T$ to receive messages from its neighbors. The locally stored messages in $M_{j}$ are updated accordingly. Using the updated messages, it computes its outgoing messages according to (8) and repeats the iteration. The access intensity $\rho_{j}$ is computed according to (9). The pseudocode of distributed IBP is largely similar to that of distributed BP. Here, we only show the parts that are different.

```
Algorithm 2: Distributed IBP
    \(m_{j i}\left(s_{i}\right), \forall i \in N_{j} \leftarrow \sum_{s_{j} \in[0,1]} \psi_{i i}\left(s_{i}, s_{j}\right)\)
    Compute \(m_{j i}\left(s_{i}\right), \forall i \in N_{j}\) according to (8)
    Invoke procedure ACCESSINTENSITYCOMPUTA-
    TION and repeat procedure ITERATION;
    end procedure
    procedure ACCESSINTENSITYCOMPUTATION
        Compute its access intensity \(\rho_{j}\) according to (9)
    end procedure
```


## 3) Convergence of IBP

With respect to the convergence of IBP, we have the following theorem:

Theorem 1: If the target throughput is feasible in the sense that $\overline{i h}=B P(G, \bar{\rho})$ for some $\bar{\rho}$, IBP defined by (8) and (9) is a contraction mapping and is guaranteed to converge to $\bar{\rho}$.

Proof: See Appendix B.
We have shown that IBP is guaranteed to converge. However, recall that $\overline{i h}=B P(G, \bar{\rho})$ is an approximation of the actual link throughputs in the CSMA network. Similarly, IBP may output a $\bar{\rho}$ that does not exactly yield the target $\overline{i h}$ in the actual network.

To reduce the errors in loopy graphs, we can also adapt GBP for the reverse operation. The details of IGBP will be presented in Section VI-D.

## D. Experimental Evaluation

We examine the performance of IBP and IGBP. First, consider Network 1 shown in Fig. 2. Define $0 \leq \gamma<1$ as the "load factor". The target throughput vector is set to $\overline{i h}=\gamma^{*}\left[0.2^{*}(1,0,1,0,0,0)+0.3^{*}(1,0,0,1,0,1)+0.2^{*}(0,1,0\right.$ $\left.0,1,0)+0.3^{*}(0,0,1,0,1,0)\right]=\gamma^{*}(0.5,0.2,0.5,0.3,0.5,0.3)$.

That is, we set $\overline{i h}$ to be a linear combination of some MaIS, multiplied by a factor $\gamma<1$ to make sure that the target throughput vector is within the capacity region as in [7].

We implement IBP and IGBP using MATLAB programs. For Network 1, we vary $\gamma$ and find the corresponding access intensities $\bar{\rho}$ to meet the link target throughputs using IBP (IGBP). We then use an ICN-simulator to get the throughputs of Network 1 with the access intensities $\bar{\rho}$ found. For each link, we calculate the error of the throughput obtained by the ICN-simulator relative to the target throughput. The error is normalized by the maximum link throughput in the network. In our experiments, we define the minimum $n$ such that $\max _{j}\left|\rho_{j}[n]-\rho_{j}^{\prime}\right| / \rho_{j}^{\prime}<1 \%$ is satisfied as the number of iterations for IBP and IGBP to achieve convergence, where $\rho_{j}^{\prime}$ is the final converged value.
![img-1.jpeg](img-1.jpeg)

Fig.2. Network 1.

Table IV shows the mean throughput errors of IBP and IGBP with respect to $\gamma$. As can be seen, when $\gamma$ is not large (e.g., below 0.6), both IBP and IGBP work quite well. As $\gamma$ approaches 1, IBP has a throughput error of $12.3 \%$ and IGBP has an error of $3.8 \%$. It is known that as $\gamma$ increases, we need larger access intensities to meet the target throughputs. As shown in Section III, the mean error of BP and GBP increases with the value of $\rho$. Based on the same framework, the errors of IBP and IGBP will also increase with the value of $\rho$. This explains why the errors of IBP and IGBP increase with $\gamma$. As for computation complexity, IBP is very fast and its runtime is very close to zero while IGBP can output solutions within one second.

Next we conduct a set of random graph experiments as follows. We randomly generate networks of different numbers of links. The mean vertex degree is four. The access intensity of link $i, \rho_{i}$, is randomly generated within the interval $\left[\rho_{0}, 4 \rho_{0}\right]$. Then we run the ICN simulator to get the link throughputs and set them to be the target throughputs of IBP and IGBP. Finally we run IBP and IGBP and examine the throughput errors of both algorithms. Table V shows the mean throughput errors, CPU runtimes and number of iterations of IBP and IGBP. For networks of up to 200 links, the error of IBP is kept to $6.2 \%$ or below, while the error of IGBP is within $1 \%$. As for computation complexity, IBP is very fast while IGBP can also give solutions within seconds.

Table VI shows the scenario in which the number of links is fixed to 100 while the mean degree of links is varied. Again, the throughput error of IBP is kept to below $4 \%$. IGBP's throughput error is below $1 \%$. As for computation complexity,

IBP is very fast, while IGBP is slower but still outputs solutions within a minute. Note that these CPU runtimes are from a centralized implementation in which there is only one processor computing the results. Distributed implementation will be much more scalable with the number of links. As can be seen, both IBP and IGBP converge within dozens of iterations. If beacons in real networks are used for message passing, IBP and IGBP can output solutions within seconds for network of up to 200 links.

Table IV. Mean Throughput Errors, Runtimes and Number of Iterations of IBP and IGBP for Network 1.


Table V. Mean Throughput Errors, Runtimes and Numbers of Iterations of IBP and IGBP for Networks with Contention Graphs in which Each Vertex has on average Four Neighbors.


Table VI. Mean Throughput Errors, Runtimes and Numbers of Iterations of IBP and IGBP for Networks of 100 Links.


## V. BP-AdPative CSMA (BP-ACSMA)

This section investigates solving the network utility optimization problem in CSMA networks using BP.

## A. Motivation and Problem Formulation

In the previous section, the target link throughputs are given, and the corresponding link access intensities are computed. A problem is that in general we do not know whether the target link throughputs are feasible or not - computation of the feasible region is itself a tough problem for large networks. A way to circumvent this problem is to focus on optimizing a system utility $\sum_{j} U_{j}\left(t h_{j}\right)$ instead, where $U_{j}\left(t h_{j}\right)$ is the utility of link $j$. That is, we aim to find $\bar{\rho}$ to optimize $\sum_{j} U_{j}\left(t h_{j}\right)$. In the following, we briefly review the background leading to the ACSMA. Then, in Part C, we introduce the alternative of using BP to solve the problem.

Recall that the feasible states of ICN are the independent sets of the contention graph. Define an indicator function $x_{j}^{s}$ such that $x_{j}^{s}=1$ if link $j$ is transmitting in state $s$ and $x_{j}^{s}=0$ otherwise. Let $u_{s}$ be the probability of state $s$ (i.e., fraction of airtime dedicated to state $s$ ). Furthermore, let $f_{j}$ denote the input rate of link $j$. Let $\bar{u}$ and $\bar{f}$ denote the vectors consisting of $u_{s}$ for all $s$, and $f_{j}$ for all $j$, respectively. Consider the following utility optimization problem:

$$
\begin{array}{ll}
\max _{x, y} & \sum_{j} U_{j}\left(f_{j}\right) \\
\text { s.t. } & \sum_{s} u_{s} x_{j}^{s} \geq f_{j} \quad \forall j \\
& u_{s} \geq 0 \forall s ; \sum_{s} u_{s}=1
\end{array}
$$

As explained in [7], when the system is in a state $s$ and $x_{j}^{s}=1$, but link $j$ has no packet in its queue, link $j$ will transmit a dummy packet. This accounts for the inequality $\sum_{j} u_{s} x_{j}^{s} \geq f_{j}$ in order to balance the input and output traffic.

The optimization problem as formulated in (10) has two problems. First, it is a difficult combinatorial optimization problem. Also, it is not clear how to implement a distributed algorithm to solve it. Second, even if a solution could be found, to realize it using CSMA, the $\bar{u}$ found would still have to be mapped to $\bar{\rho}$. That is, $u_{s}$ must be equal to the stationary probability $P_{s}=\prod_{j: s_{j}^{\prime} \times s} \rho_{j} / Z$ for CSMA networks.

To circumvent the above difficulties, [7] formulated an alternative optimization problem as follows:

$$
\begin{array}{ll}
\max _{x, y} & \beta \sum_{j} U_{j}\left(f_{j}\right)-\sum_{s} u_{s} \log u_{s} \\
\text { s.t. } & \sum_{s} u_{s} x_{j}^{s} \geq f_{j} \quad \forall j \\
& u_{s} \geq 0 \forall s ; \sum_{s} u_{s}=1
\end{array}
$$

Compared with (10), the objective function in (11) has an extra entropy term $-\sum_{s} u_{s} \log u_{s}$. When $\beta$ is large, (11) asymptotically approaches (10). As shown below, the $\bar{u}$ found by (11) turns out to be CSMA realizable. Indeed $r_{j}=\log \left(\rho_{j}\right)$ turns out to be the dual variable to the constraint $\sum_{s} u_{s} x_{j}^{s} \geq f_{j}$.

Associate dual variable $r_{j}$ with the constraint $\sum_{j} u_{s} x_{j}^{s} \geq f_{j} \quad \forall j$, without assuming $r_{j}=\log \left(\rho_{j}\right)$ for the time being. A partial Lagrangian of problem (11) is

$$
L(\bar{u}, \bar{r}, \bar{f})=\beta \sum_{j} U_{j}\left(f_{j}\right)-\sum_{s} u_{s} \log u_{s}+\sum_{j} r_{j}\left(\sum_{s} u_{s} x_{j}^{s}-f_{j}\right)
$$

Given $\bar{r}$ and $\bar{f}$, the optimal $\bar{u}$ to (12) can be shown to be

$$
u_{s}^{*}(\bar{r})=\exp \left(\sum_{j} r_{j} x_{j}^{s}\right) / \sum_{s} \exp \left(\sum_{j} r_{j} x_{j}^{s}\right), \forall s
$$

We see that (13) is just the stationary distribution of CSMA networks with $r_{j}=\log \left(\rho_{j}\right) \quad \forall j$.
The optimal $\bar{f}$ is given by

$$
\partial L(\bar{u}, \bar{r}, \bar{f}) / \partial f_{j}=\beta U_{j}^{*}\left(f_{j}\right)-r_{j}=0
$$

The optimal $\bar{r}$ is given by

$$
\partial L(\bar{u}, \bar{r}, \bar{f}) / \partial r_{j}=\sum_{s} u_{s} x_{s}^{s}-f_{j}=0
$$

Combining (13), (14) and (15), we find that the optimal solution to (11) is given by a set of $\bar{r}$ and $\bar{f}$ that satisfy

$$
\begin{aligned}
& \beta U_{i}^{\prime}\left(f_{j}\right)-\log \left(\rho_{j}\right)=0 \\
& t h_{i}=f_{i}=\sum_{s} u_{s} x_{s}^{s}
\end{aligned}
$$

In Section B below, we briefly review how [7] solves the optimization problem using a distributed adaptive CSMA algorithm. We present an alternative method using the BP framework in Section C.

## B. ACSMA proposed in [7]

The joint scheduling and congestion control algorithm (ACSMA) proposed in [7] looks for the optimal solution to (11) by steepest ascent of $L(\bar{u}, \bar{r}, \bar{f})$. According to (15), $\partial L(\bar{u}, \bar{r}, \bar{f}) / \partial r_{i}=$ output rate of link $j$-input rate of link $j . \mathrm{T}$ he queue size of link $j$ is a smoothed measure of the difference in the output rate and input rate. Thus, in each iteration, link $j$ adjusts its $\rho_{j}$ such that $r_{i}=\log \left(\rho_{i}\right)$ is proportional to its queue length. If the input rate of the queue is larger than the service rate, the queue builds up, leading to an increase in $\rho_{j}$, and vice versa. Note, that $\rho_{j}$ controls the output rate of link $j$. For the input rate $f_{j}$, link $j$ adjusts $f_{j}$ to satisfy $\beta U_{i}^{\prime}\left(f_{j}\right)-\log \left(\rho_{j}\right)=0$ in (14) based on the newly computed $\rho_{j}$. Before the next iterative update, link $j$ waits for some time to examine whether the load $f_{j}$ can be supported by the network under current $\widehat{\rho}$ through its queue size. The iterations continue until the overall network finds a set of access intensities $\widehat{\rho}$ that can support the loads $\bar{f}$. At that point, the throughput of link $j$ satisfies $t h_{j}=f_{j}$.

ACSMA does not explicitly "compute" the link throughputs using (13). Rather, it makes use of actual data packets to probe the network and "measure" the link throughputs. To smooth out the measurement due to temporal throughput fluctuations to which CSMA networks are susceptible, long smoothing interval between successive iterations may be required.

## C. BP-ACSMA

The optimal network utility in (11) is achieved when the link access intensities and throughputs are such that (16) holds. BP can be applied to make sure that (16) is satisfied.

## 1) Message update rules of BP-CSMA

In BP-ACSMA, the messages are determined by the message update rule:

$$
m_{p}\left(s_{i}\right) \leftarrow \sum_{s_{i} \in[0,1]} \psi_{0}^{\prime}\left(s_{i}, s_{j}\right) \phi_{j}\left(s_{j}\right) \prod_{k \in N_{j} \cup} m_{k j}\left(s_{j}\right)
$$

In each iteration, based on the received messages, vertex $j$ computes belief $b_{j}\left(s_{j}\right)$ according to

$$
b_{j}\left(s_{j}\right)=k_{j} \phi_{j}\left(s_{j}\right) \prod_{i \in N_{j}} m_{i j}\left(s_{j}\right)
$$

It then solves for $\rho_{j}$ from (16) by setting $t h_{j}=b_{j}\left(s_{j}=1\right)$. Based on the new $\rho_{j}$, vertex $j$ updates messages $m_{p}\left(s_{i}\right)$, $i \in N_{j}$ according to (17) and broadcasts the messages to its neighbors.

In essence, BP replaces the network probing and throughput measurement in ACSMA by computation.

## 2) Distributed implementation

Consider a particular vertex $j$. It locally stores a record of $N_{j}$, the messages from its neighbors $M_{j}=$ $\left\{m_{i j}\left(s_{j}\right), \forall i \in N_{j}\right\}$, and its utility function $U_{j}\left(t h_{i j}\right) . N_{j}$ is periodically refreshed to track the dynamics of the local network contention graph.

Initially, vertex $j$ sets its outgoing messages $m_{p}\left(s_{i}\right)$ to $\sum_{s_{i} \in[0,1]} \psi_{0}\left(s_{i}, s_{j}\right), \quad \forall i \in N_{j}$. In each iteration, it passes $m_{p}\left(s_{i}\right)$ to each neighbor vertex $i$. It then waits for time $T$ to receive messages from its neighbors. Based on the received messages, link $j$ then (i) computes its belief $b_{j}\left(s_{j}\right)$ using (18); (ii) solves for $\rho_{j}$ according to (16); and (iii) determines its outgoing messages according to (17) using the newly computed $\rho_{j}$ in (ii).

The pseudocode of BP-ACSMA is largely similar to that of distributed BP. Here, we only show the parts that are different.

```
Algorithm 3: BP-ACSMA
5. \(m_{p}\left(s_{i}\right), \forall i \in N_{j} \leftarrow \sum_{s_{i} \in[0,1]} \psi_{0}\left(s_{i}, s_{j}\right)\)
10. Invoke procedure ACCESSINTENSITYCOMPUTATION
    and repeat procedure ITERATION;
11.end procedure
12. procedure ACCESSINTENSITYCOMPUTATION
13. Compute its belief \(b_{j}\left(s_{j}\right)\) using (18);
14. Solve for \(\rho_{j}\) according to (16)
15. Compute \(m_{p}\left(s_{i}\right), \forall i \in N_{j}\) according to (17)
16. end procedure
```


## D. Experimental Evaluation

We evaluate the performance of both BP-ACSMA and GBP-ACSMA (details of GBP-ACSMA will be presented in Section VI-E). We consider the proportional fairness utility: $U_{j}\left(t h_{j}\right)=\log \left(t h_{j}\right)$, and set the weighting factor $\beta$ to 1 . We implement both algorithms using MATLAB programs. For both algorithms, the outputs are the converged link access intensities, $\widehat{\rho}$. To evaluate the performance of each algorithm, we use the ICN simulator to get the throughputs of networks under the $\widehat{\rho}$ found, and then obtain the network utility achieved from the throughputs. Recall that $\rho_{j}$ relates

to $r_{i}$ in ACSMA of [7] via $r_{i}=\log \left(\rho_{i}\right)$. For easy comparison between our BP-based algorithms and ACSMA, we use $r_{i}$ in our convergence test although the parameters being adjusted in our algorithms are $\rho_{i} \forall j$. Let $r_{i}[n]$ be the value of $r_{i}$ in iteration $n$. We define the number of iterations required for convergence in BP-ACSMA (GBP-ACSMA) as the minimum $n$ such that $\max _{i}\left|r_{i}[n]-r_{i}^{*}\right| / r_{i}^{*}<1 \%$, where $r_{i}^{*}=\log \left(\rho_{i}^{*}\right)$ is the final converged $r_{i}$ value.

We also implement ACSMA of [7]. In ACSMA, the parameters adjusted in iteration $n$ are $r_{i}[n]$ and $f_{i}[n] \forall j$. If ACSMA converges, then $r_{i}[n]$ and $f_{i}[n]$ will asymptotically approach the targeted $r_{i}^{*}$ and $f_{i}^{*}$ as $n$ increases. We define the minimum $n$ such that $\max _{i}\left|r_{i}[n]-r_{i}^{*}\right| / r_{i}^{*}<3 \%$ is satisfied as the number of iterations for ACSMA to achieve convergence. Note that here we use a looser convergence test for ACSMA; by nature, some fluctuations are unavoidable in ACSMA even after convergence because of its measurement approach. In our simulation, the update interval of ACSMA is set to 150 DATA packet times to guarantee that convergence can be achieved. We find that if the update interval is set to 125 DATA packet times, ACSMA cannot converge in some networks we test ${ }^{5}$.

In the first set of experiments, we randomly generate networks with different numbers of links. The mean degree of links is around four. In each simulation run, we gather the statistics of two metrics: i) normalized total system throughput $T h=\sum_{i} t h_{i}$; ii) system utility $U=\sum_{i} \log \left(t h_{i}\right)$. Table VII shows the achieved throughputs and network utilities of BP-ACSMA, GBP-ACSMA and ACSMA. As shown, BP-ACSMA has acceptable performance in terms of both throughputs and network utilities; and GBP-ACSMA has comparable performance to ACSMA. As for speed, BP-ACSMA and GBP-ACSMA output solutions after dozens of iterations while ACSMA often requires hundreds of iterations.

Table VII. Achieved Aggregate Throughputs, Utilities and Number of Iterations of BP-ACSMA, GBP-ACSMA and ACSMA for Networks with CONTENTION GRAPHS IN WHICH EACH VERTEX HAS ON AVERAGE FOUR Neighbors


[^0]In the second set of experiments, we randomly generate networks of 100 links with varying mean vertex degrees. Table VIII compares the three algorithms. As the network becomes denser, more loops appear in the contention graph, resulting in more computation error of BP-ACSMA. As shown in Table VIII, BP-ACSMA loses accuracy when the mean vertex degree is set to six. GBP-ACSMA continues to work well since it has removed loops in message passing (see Section VI-E). Table VIII also shows that BP-ACSMA and GBP-ACSMA achieve higher aggregate throughputs than ACSMA does with some utility loss. As for convergence speed, BP-ACSMA and GBP-ACSMA are much faster than ACSMA.

Table VIII. Achieved Aggregate Throughputs, Utilities and Number of Iterations of BP-ACSMA, GBP-ACSMA and ACSMA for Networks of 100 Links.


## E. Comparison of BP-ACSMA and GBP-ACSMA

Our simulations in Part D show that both BP-ACSMA and GBP-ACSMA converge within dozens of iterations for a network of 100 links. ACSMA converges only after hundreds of iterations. For comparison, let us map the number of iterations to time needed for convergence in real network operation.

For BP-ACSMA and GBP-ACSMA, beacons could be used for message passing. In 802.11 networks, typically a beacon is broadcasted every 0.1 s . For BP-ACSMA, from the results in Tables VII and VIII, convergence is achieved within 11 iterations for all the scenarios we tested. Using beacons for message passing (note that the transmission time of a beacon is about 0.1 ms . Thus, each time a link has sufficient time to broadcast its message between two successive iterations), it only needs $0.1 * 11=1.1 \mathrm{~s}$ to output solutions for networks of up to 100 links. For GBP-ASMA, convergence is achieved within 64 iterations for all the scenarios tested, corresponding to a convergence time of within 6.4 seconds. The convergence speed of both algorithms can be even faster if the messages are piggybacked on data packets rather than being carried on beacons. By contrast, ACSMA requires $413^{*} 150 \mathrm{~ms} \approx 62 \mathrm{~s}$ for convergence, assuming a DATA packet duration is 1 ms - recall that we experimentally found that we need 150 DATA packet times for convergence of ACSMA in the networks simulated.

For networks that exhibit temporal starvation, even more time is needed for ACSMA for each iteration to smooth out the measurement. An example of a network that exhibits temporal starvation is Cayley tree network [15]. To illustrate our point, we perform simulations on a 3-order 4-layer Cayley tree. As shown in Fig. 3, each link in the Cayley tree has three

[^0]: ${ }^{5}$ This brings up another issue with ACSMA. That is, we do not know how to set the update interval $T$ in an optimal manner beforehand, and we need to run the algorithm to determine the minimum $T$ required for each network. BP-ACSMA and GBP-CSMA, however, do not have this issue because the update interval is not related to measurement smoothing time needed.

neighbors. Emanating from link 1, all the links are arranged in shells around vertex 1. In our example there are four such shells. We run ACSMA using the same parameters as in [7] except for that the update interval T is set to 100ms (we assume that a DATA packet duration is 1ms) and β = 5. Fig. 4 plots r<sup>i</sup> = log(p<sup>i</sup>), i = 1, 2 versus the iteration index, where link 2 is a neighbor of link 1. As can be seen, ACSMA cannot converge. This means that the update interval T = 100 ms is not long enough to accurately measure the link throughputs. Then we increase the update interval T by 200 ms each time and repeat the simulation. Finally we obtain that when T is set to 5700ms, ACSMA converges according to our convergence test max<sub>1</sub> |r<sup>i</sup> [n] − r<sup>i</sup><sub>j</sub>| / r<sup>i</sup><sub>j</sub> < 3% and the number of iterations required is 249. That is, given the update interval T = 5700ms, ACSMA needs at least 5700*249 ms ≈ 23.66 minutes to converge.

Large update interval T is required to avoid triggering oscillations of f<sup>i</sup> and log(p<sup>i</sup>) in the Cayley network because the temporal throughputs of links exhibit drastic fluctuations over time. Take link 1 as an example. As plotted in Fig. 5, its normalized temporal throughput alternates between 0 and 1 over time. To exactly measure the throughputs, each link needs to average its measured throughput over several 0-1 cycles, say 8-10 seconds. Thousands of DATA packets are transmitted in each iteration to estimate link throughputs under current network settings. This further slows down the convergence of the algorithm. BP-ACSMA and GBP-ACSMA, however, do not require this real-time measurement and hence will not be affected by this temporal starvation phenomenon.<sup>6</sup>

### A philosophical interpretation of convergence rates

BP-ACSMA and GBP-ACSMA require one-hop message passing while ACSMA does not require message passing. One may ponder why BP-ACSMA and GBP-ACSMA can converge faster than ACSMA. A way to look at the problem is as follows. In order for a link j to adjust its access intensity to achieve its fair share of throughput under the utility optimization problem, it somehow has to acquire information about the network topology. To achieve that in a distributed algorithm, the links somehow have to communicate with each other. In BP-ACSMA and GBP-ACSMA, the communication is in the form of "explicit" message passing. The communication in ACSMA, however, is achieved via "implicit messages" in the following sense. In ACSMA, each time a link j transmits a regular data packet, it is actually conveying some information to the neighbor links. In particular, data packets transmitted by link j slow down the clearing of queues in neighbor links, and these links make use of the queue occupancies to adjust their access intensities. Because of the need for smoothing and

the fact that these data packets are "indirect" messages, many more data packets than explicit messages are needed in order to convey the same information in ACSMA. This slows down the convergence rate of ACSMA.

![img-2.jpeg](img-2.jpeg)

**Fig. 3.** A three-order Cayley tree network.

The main potential drawback of BP-based algorithms is accuracy, since they only characterize the throughput dependence on the access intensities approximately. More precisely, both BP-ACSMA and GBP-ACSMA are only exact in tree-like topologies (e.g., Cayley tree networks) and may have errors in loopy graphs. The computation error may become unacceptable when the access intensities are extremely large (e.g., 1 e+6) or the network is highly populated. We note, however, that in practice we are unlikely to adopt such large access intensities because of implementation concerns such as finite size of time-slot (see Section III-B of [13], where it was argued that access intensity cannot go beyond 530), higher degree of temporal starvation, etc. For a dense network, we note that GBP-ACSMA can still achieve reasonably accurate results. Section VI details the theory behind GBP and how our specific implementation of GBP for CSMA networks attempts to remove small loops in the message passing construction; small loops are particularly detrimental to accuracy, as we have seen from the example of N-vertex circular network discussed in Section III-E.

![img-3.jpeg](img-3.jpeg)

**Fig. 4.** Transmission aggressiveness r<sup>i</sup> and r<sup>j</sup> of link 1 and link 2 in a 3*4 Cayley tree network for ACSMA of [7] with T = 100ms. Access intensities of other links exhibit similar fluctuations.

![img-4.jpeg](img-4.jpeg)

**Fig. 5.** The transmission aggressiveness r<sup>i</sup> and r<sup>j</sup> of link 1 and 2 in a 3*4 Cayley tree network for ACSMA of [7] with T = 100ms. Access intensities of other links exhibit similar fluctuations.

Fig.5. Normalized throughputs of link 1 in a 3-order 4-layer Cayley tree measured over successive 0.1 s intervals when ACSMA is implemented. Throughputs of other links exhibit similar fluctuations.

## VI. Generalized Belief Propagation and its APPLICATIONS IN CSMA NETWORKS

In BP, all messages are from one vertex to another vertex. To reduce the error effects of loops, GBP allows messages to be passed from a group of vertices to another group. These groups of vertices are called regions. A region graph is constructed for message passing purposes. The belief of a region corresponds to the joint probability of the states of the vertices within the region. GBP attempts to capture more information than BP because the joint probability of states contains more information on the inter-relationship among the vertices in a region. With the region graph and a new message update rule, GBP can be more accurate than BP.

## A. Region graph

The first step of GBP is to generate a region graph $G$. In this paper, we use an algorithm similar to the cluster variation method introduced by Kikuchi in 1951 and further developed in the physics literature [16]. The general theory of GBP, however, leaves open the issue of how to define the subsets of vertices to form regions. An important contribution of this paper is to show that a "maximal clique" method of forming regions that are amenable to distributed implementation in CSMA networks yield good results.

A region $R=\left(V_{R}, E_{R}\right)$ is a subgraph of the original contention graph $G=(V, E)$ in which $V_{R} \subseteq V$, and $E_{R} \subseteq E$ are edges between the vertices in $V_{R}$. Regions are divided into different hierarchical levels. Each region belongs to one of the level. Fig. 6 gives an example demonstrating the construction of a region graph using the cluster variation method.

An important step is the forming of the set of regions at level 0 , denoted by $\mathbf{R}_{\mathbf{0}}$. The regions at other levels are constructed based on $\mathbf{R}_{\mathbf{0}}$. That is, the definitions of regions in other levels follow from the definition of $\mathbf{R}_{\mathbf{0}}$. Thus, the definition of $\mathbf{R}_{\mathbf{0}}$ is critical. Every vertex $i \in V$ and every edge $e \in E$ in the original graph must be included into at least one region $R \in \mathbf{R}_{\mathbf{0}}$. We allow for the possibility of a vertex to belong to more than one region in $\mathbf{R}_{\mathbf{0}}$. However, no region $R \in \mathbf{R}_{\mathbf{0}}$ could be a subregion of another region $R^{\prime} \in \mathbf{R}_{\mathbf{0}}$ : that is, $R \not \subset R^{\prime}$ for any two regions $R, R^{\prime} \in \mathbf{R}_{\mathbf{0}}$.

In general, there are many ways of forming $\mathbf{R}_{\mathbf{0}}$. Different choices of $\mathbf{R}_{\mathbf{0}}$ correspond to different implementations of GBP. There is a general tradeoff between complexity and accuracy in the choice of $\mathbf{R}_{\mathbf{0}}$. More accuracy can be obtained by GBP if the regions in $\mathbf{R}_{\mathbf{0}}$ are large, but the computation complexity will also be higher.

As discussed in Section III-E, when BP messages are passed around a small loop, computation errors will be incurred. In GBP, we try to include loops in the original graph
into a region in $\mathbf{R}_{\mathbf{0}}$ to negate their effects ${ }^{7}$. In our implementation, we generate $\mathbf{R}_{\mathbf{0}}$ by making each maximal clique in $G$ a region in $\mathbf{R}_{\mathbf{0}}{ }^{8}$. This ensures that each vertex and each edge in $G$ are included into at least one region. Note in particular that error-inducing small loops in BP consisting of only three vertices are guaranteed to be subsumed into a region in GBP. Although larger loops may not be subsumed into a region, the intuition is that they induce smaller errors anyway. Simulation results in the preceding sections have borne out our method of forming regions in $\mathbf{R}_{\mathbf{0}}$ under various network topologies and parameter settings.

For notational simplicity, in the following we sometimes write $R$ in terms of its vertices only, without listing its edges. In Fig. 6, the maximal cliques are $\{1,2\},\{1,3\},\{3,4\}$, $\{2,4,5\},\{4,5,6\},\{5,6,8\},\{5,9\}$ and $\{6,7\}$, all of which are included in $\mathbf{R}_{\mathbf{0}}$ on the top row of Fig. 6(b).

After the construction of $\mathbf{R}_{\mathbf{0}}$, we then construct the set of regions at level $1, \mathbf{R}_{1}$, from the intersections of the regions in $\mathbf{R}_{\mathbf{0}}$. We discard from $\mathbf{R}_{i}$, however, any intersection region that is a strict subregion of another intersection region. Specifically, to construct $\mathbf{R}_{i}$, we first form the set $\mathbf{S}_{i}=\left\{R \mid R=R_{i} \cap R_{j}, \forall R_{i} \in \mathbf{R}_{0}, R_{j} \in \mathbf{R}_{0}, i \neq j\right\}$. We then discard from $\mathbf{S}_{i}$ any region $R \in \mathbf{S}_{i}$ where $R \subset R^{\prime} \in \mathbf{S}_{i}$.

In Fig. 6, for example, $\mathbf{R}_{i}$ consists of $\{1\},\{2\},\{3\},\{4,5\}$ and $\{5,6\}$. Note that although $\{5\}$ is the intersection of $\{2,4$, $5\}$ and $\{5,6,8\}$, but $\{5\}$ is not included in $\mathbf{R}_{i}$ because it is a strict subregion of $\{4,5\}$ and $\{5,6\}$.
![img-5.jpeg](img-5.jpeg)

Fig. 6. An example of construction of a region graph.

[^0]
[^0]:    ${ }^{7}$ It could be shown that when the resulting region graph does not have a loop, GBP will give exact solutions [16].
    ${ }^{8}$ It is important to note that the identification of maximal cliques here is not NP-hard if the vertex degree is limited. In practical CSMA wireless networks the degree of a vertex does not grow with the network size, thanks to geographical constraints. Typically, a vertex has at most 5-6 neighbors regardless of the number of vertices in the graph. Let $K$ be the maximum degree of vertices in the contention graph and $N$ be the number of links in the network. For each vertex the complexity of finding maximal cliques containing it is of order $O\left(2^{K}\right)$. Hence, the complexity of finding all the maximal cliques is of order $O\left(N 2^{K}\right)$, which increases linearly with $N$. For distributed implementation, the computation-time complexity is of order $O\left(2^{K}\right)$.

Similarly, we construct the set of regions $\mathbf{R}_{2}$ from the intersections of the regions in $\mathbf{R}_{0} \cup \mathbf{R}_{1}$. In addition to discarding intersection regions that are subregions of other intersection regions in $\mathbf{R}_{2}$, we also discard intersection regions that have already appeared in $\mathbf{R}_{1}$.

## General Procedure for Constructing $\mathbf{R}_{3}$ and Edges to it

In general, to construct $\mathbf{R}_{3}$, we first form the set

$$
\begin{aligned}
\mathbf{S}_{k}= & \left\{R \mid R=R_{i} \cap R_{j}, \forall R_{i} \in \mathbf{R}_{k-1}, R_{j} \in \mathbf{R}_{k-1}, i \neq j\right\} \cup \\
& \bigcup_{n=0}^{k-2}\left\{R \mid R=R_{i} \cap R_{j}, \forall R_{i} \in \mathbf{R}_{k-1}, R_{j} \in \mathbf{R}_{n}\right\}
\end{aligned}
$$

We then discard from $\mathbf{S}_{k}$ any region $R \in \mathbf{S}_{k}$ where $R \subset R^{\prime} \in \mathbf{S}_{k}$; and any region $R \in \mathbf{S}_{k}$ where $R \in \mathbf{R}_{n}$ for some $n \leq k-1$ (i.e., also discard any region in $\mathbf{S}_{k}$ that already appears at an upper level). We stop forming new regions at the next level when no more new intersection regions can be identified.

For each region $R$, we draw a directed edge from each of its super-regions to it, except for those regions that are su-per-regions of other super-regions of region $R$. For example, in Fig. 6 there is no direct edge from $\{2,4,5\}$ to $\{4\}$, since region $\{2,4,5\}$ is the super-region of region $\{4,5\}$, which is also a super-region of $\{4\}$.

In the resulting region graph $G$, an edge connects a "parent region" $P$ and a "child region" $R$. If there is a directed path from region $R^{\prime}$ to region $R$, we say that $R^{\prime}$ is an ancestor of $R$, and $R$ is a descendant of $R^{\prime}$. We denote the region graph by $G=(\mathbf{V}, \mathbf{E})$ where $\mathbf{V}$ is the set of regions and $\mathbf{E}$ is the set of edges. Note that in this paper, to avoid confusion, the bold fonts $\mathbf{V}$ and $\mathbf{E}$ are used to refer to the regions and edges between them, and $V$ and $E$ refers to the vertices and edges between them in the contention graph.

## B. Message and Message-update rules of GBP

In this paper, we adopt the Parent-to-Child algorithm [17] for message updates. In this algorithm, messages are passed from parent regions to their child regions only. Let $s_{R}=s_{1} s_{2} \cdots s_{i} s_{i} \cdots s_{|V_{R}|}, i, j \in V_{R}$ be the state of a region $R$, and $b_{R}\left(s_{R}\right)$ be the belief of a particular region state $s_{R}$. In GBP, the "intrinsic" belief of $R$ is given by $\prod_{\left(s_{i}, j\right) \in E_{R}} \psi\left(s_{i}, s_{j}\right) \prod_{i \in V_{R}} \phi_{i}\left(s_{i}\right)$. This would be proportional to the probability distribution of the states of the vertices in $R$, if there were no other vertices in the overall network (i.e., if $R$ were the overall network itself). In general, $R$ receives messages from other regions, and these messages capture the correlation of the states of different regions.

Let $\mathbf{D}_{R} \subseteq G$ be the subgraph consisting of a region $R$ and all its descendants. In GBP, the update equation of $R$ has to incorporate all "external" messages passed to the regions in $\mathbf{D}_{R}$, not just those to $R$ only. In Fig. 6, for example,
$\mathbf{D}_{\{5,6\}}=\{\{5,6\},\{5\},\{6\}\}$. The following external messages are passed into $\mathbf{D}_{\{5,6\}}: m_{\{4,5,6\}-\alpha\{5,6\}}, m_{\{5,6,8\}-\alpha\{5,6\}}, m_{\{4,5\}-\alpha\{5\}}$, $m_{\{5,9\}-\alpha\{5\}}, m_{\{6,7\}-\alpha\{6\}}$.

Let $\operatorname{Parents}\left(R^{\prime}\right)$ denote the parents of a region $R^{\prime}$. The belief at $R$ is the product of its intrinsic belief and external messages:

$$
\begin{aligned}
b_{R}\left(s_{R}\right)= & \prod_{\{i, j, k, l, j\}} \psi\left(s_{i}, s_{j}\right) \prod_{i \in V_{R}} \phi_{i}\left(s_{i}\right) \\
& \prod_{R^{\prime} \in \mathbf{D}_{R}} \prod_{R^{\prime} \in \operatorname{Parents}\left(R^{\prime}\right) \backslash \mathbf{D}_{R}} m_{R^{\prime \prime}-s R^{\prime}}\left(s_{R^{\prime}}\right)
\end{aligned}
$$

Note that in the above, the state of $R$ is $s_{R}$, and the state of $R^{\prime} \subseteq R, s_{R^{\prime}}$, is induced from $s_{R}$.

In the parent-to-child algorithm, the message-update rules are obtained by requiring consistency of the beliefs between parent and child regions. In Fig. 6(b), let us focus on the region $\{4,5,6\}$ and its child $\{5,6\}$. The belief at region $\{4,5,6\}$ is given by

$$
\begin{aligned}
& b_{\{4,5,6\}}\left(s_{4} s_{5} s_{6}\right) \propto \prod_{i, j \in\{4,5,6\}, i \neq j} \psi\left(s_{i}, s_{j}\right) \prod_{i \in\{4,5,6\}} \phi_{i}\left(s_{i}\right) m_{\{2,4,5\}-\alpha\{4,5\}}\left(s_{4} s_{5}\right) \\
& m_{\{5,6,8\}-\alpha\{5,6\}}\left(s_{4} s_{6}\right) m_{\{5,6\}-\alpha\{5\}}\left(s_{4}\right) m_{\{5,9\}-\alpha\{5\}}\left(s_{5}\right) m_{\{6,7\}-\alpha\{6\}}\left(s_{6}\right)
\end{aligned}
$$

and the belief at region $\{5,6\}$ is given by

$$
\begin{aligned}
& b_{\{5,6\}}\left(s_{5} s_{6}\right) \propto \psi\left(s_{5}, s_{6}\right) \phi_{5}\left(s_{5}\right) \phi_{6}\left(s_{6}\right) m_{\{4,5,6\}-\alpha\{5,6\}}\left(s_{5} s_{6}\right) \\
& m_{\{5,6,8\}-\alpha\{5,6\}}\left(s_{5} s_{6}\right) m_{\{4,5\}-\alpha\{5\}}\left(s_{5}\right) m_{\{5,9\}-\alpha\{5\}}\left(s_{5}\right) m_{\{6,7\}-\alpha\{6\}}\left(s_{6}\right)
\end{aligned}
$$

Using the marginalization constraint $b_{\{5,6\}}\left(s_{5} s_{6}\right)=$ $\sum_{s_{k}} b_{\{4,5,6\}}\left(s_{4} s_{5} s_{6}\right)$, we obtain a relation between messages

$$
\begin{aligned}
& m_{\{4,5,6\}-\alpha\{5,6\}}\left(s_{5} s_{6}\right) \\
& =\frac{\sum_{s_{k}} \psi\left(s_{4}, s_{5}\right) \psi\left(s_{4}, s_{6}\right) \phi_{4}\left(s_{4}\right) m_{\{2,4,5\}-\alpha\{4,5\}}\left(s_{4} s_{5}\right) m_{\{3,6\}-\alpha\{6\}}\left(s_{4}\right)}{m_{\{4,5\}-\alpha\{5\}}\left(s_{5}\right)}
\end{aligned}
$$

which is the message-update rule required. Note that on the RHS, with reference to Fig. 6, only those external messages flowing into $\mathbf{D}_{\{4,5,6\}}$ that are not also external messages flowing into $\mathbf{D}_{\{5,6\}}$ are retained in the numerator and only the "internal" messages from $\mathbf{D}_{\{4,5,6\}} \backslash \mathbf{D}_{\{5,6\}}$ to $\mathbf{D}_{\{5,6\}}$ are retained in the denominator. Similar relations can be obtained between each pair of parent and child regions.

In general, the belief of a parent region $P$ can be written as

$$
\begin{aligned}
b_{P}\left(s_{P}\right)= & \prod_{\{i, j, k, l, j\}} \psi\left(s_{i}, s_{j}\right) \prod_{i \in V_{P}} \phi_{i}\left(s_{i}\right) \\
& \prod_{P^{\prime} \in \mathbf{D}_{P}} \prod_{P^{\prime} \in \operatorname{Parents}\left(P^{\prime}\right) \backslash \mathbf{D}_{P}} m_{P^{\prime \prime}-s P^{\prime}}\left(s_{P^{\prime}}\right)
\end{aligned}
$$

The marginalization constraint for a child region $R$ with respect to the specific parent $P$ is

$$
b_{R}\left(s_{R}\right)=\sum_{s_{P \in R}} b_{P}\left(s_{P}\right)
$$

Combining (19), (20) and (21), and cancelling common items on the LHS and RHS of (21), the message from a parent $P$ to a child $R$ can be written as

$$
\begin{aligned}
& m_{P \rightarrow R}\left(s_{R}\right) \propto \\
& \frac{\sum_{s_{i} s_{k} s_{l} s_{l} s_{l} \mid P_{R}} \psi\left(s_{i}, s_{i}\right) \prod_{m_{P \rightarrow R_{k}}} \phi_{i}\left(s_{i}\right) \prod_{R \in \mathbf{D}_{P} \backslash \mathbf{D}_{R}} \prod_{R^{\prime} \in P_{\text {external }} \mid R^{\prime} \mid \backslash \mathbf{D}_{R}} m_{R^{\prime} \rightarrow R^{\prime}}\left(s_{R^{\prime}}\right)}{\prod_{R \in \mathbf{D}_{R}} \prod_{R^{\prime} \in P_{\text {external }} \mid R^{\prime} \mid V \backslash \mathbf{D}_{R} \backslash \mathbf{D}_{R}} m_{R^{\prime} \rightarrow R^{\prime}}\left(s_{R^{\prime}}\right)}
\end{aligned}
$$

Note that the term $\prod_{R \in \mathbf{D}_{R} \backslash \mathbf{D}_{R}} \prod_{R^{\prime} \in P_{\text {external }} \mid R^{\prime} \mid \backslash \mathbf{D}_{R}} m_{R^{\prime} \rightarrow R^{\prime}}\left(s_{R^{\prime}}\right)$ in the numerator consists of the "external" messages into $\mathbf{D}_{P}$ but not $\mathbf{D}_{R}$; and the term $\prod_{R \in \mathbf{D}_{R}} \prod_{R^{\prime} \in P_{\text {external }} \mid R^{\prime} \mid V \backslash \mathbf{D}_{R} \backslash \mathbf{D}_{R}} m_{R^{\prime} \rightarrow R^{\prime}}\left(s_{R^{\prime}}\right)$ in the denominator consists of the "internal" messages from $\mathbf{D}_{P} \backslash \mathbf{D}_{R}$ to $\mathbf{D}_{R}$. Although not necessary mathematically, in each updating we also impose the normalization constraint $\sum_{s_{R}} m_{P \rightarrow R}\left(s_{R}\right)=1$ to contain the numerical errors.

## C. Distributed GBP

In GBP the messages $m_{P \rightarrow R}\left(s_{R}\right)$ are passed from a parent region $P$ to its child region $R$. To implement GBP in a distributed manner, for each message $m_{P \rightarrow R}\left(s_{R}\right)$, we need to identify a particular vertex to be responsible for its update and dissemination. We propose to let a vertex that is in both $P$ and $R, j \in V_{P \cap R}$, to be such a vertex. Note that $V_{P \cap R}$ could contain more than one vertex. In this case, we elect the vertex with the lowest ID to be the responsible vertex. We will refer to the vertex responsible for a particular message as the message agent. As to what to use for ID, we note that each node in the CSMA network usually has a unique ID (e.g., MAC address). Each vertex is a link consisting of a transmitter node and a receiver node. We can simply choose the transmitter node to represent the link, in which case its ID will be the link ID. If we have an infrastructure network, the AP can be chosen to represent the link.

## Features for Correct Operation of Distributed GBP

The following lists three important features of our distributed GBP that enables its correct operation. These features, which will be proved, mean that each vertex $j$ could deduce its belief $b_{j}\left(s_{j}\right)$. Details of our distributed GBP will be presented immediately after the description of the features:

Feature 1: Each vertex $j$ could collect enough information to construct a local region graph $G_{j}$ for the purpose of distributed computation of beliefs and messages. The local region graph $G_{j}$ is a subgraph of the complete region graph $G$. In particular, $G_{j}$ is consistent with $G$ in that each region appearing in $G_{j}$ also appears in $G$, and each edge appearing in $G_{j}$ also appears in $G$.

Feature 2: Each vertex $j$ could (i) identify all regions to which it belong from $G_{j}$ and randomly select one of them $R$ for its throughput computation; (ii) collect the information
needed to compute the region belief $b_{R}\left(s_{R}\right)$ according to (19). Then, by taking marginal probability, it can compute its throughput: $t h_{j}=b_{j}\left(s_{j}=1\right)=\sum_{s_{R} s_{j}=1} b_{R}\left(s_{R}\right)$.

Feature 3: Each vertex $j$ could (i) identify the messages for which it is the message agent from $G_{j}$; and (ii) for each such message $m_{P \rightarrow R}\left(s_{R}\right)$, collect the information needed to update $m_{P \rightarrow R}\left(s_{R}\right)$ according to (22).

Next, we describe the part of our distributed GBP that enables Feature 1. In our implementation, a vertex $j$ would first construct a local contention graph $G_{j}$, from which it would construct the local region graph $G_{j}$. It does so by listening to the broadcast information from other vertices. We assume that a vertex $j$ can hear the broadcast of all its neighbors $N_{j}$ in the contention graph $G$.

## Broadcast of All Vertices

Let $N_{j}^{(i)} \square N_{j} \cup\{j\}$. Each vertex $j$ in the network broadcasts three kinds of information in its neighborhood: (i) its link ID $I D_{j}$; (ii) its access intensity $\rho_{j}$; (iii) a local contention graph, denoted by $G_{j}^{(i)}$, consisting of all the vertices in $N_{j}^{(i)}$ and the edges between them (i.e., all edges $(i, k)$ such that $i, k \in N_{j}^{(i)}$ ). Conceptually, this information is embodied in a 3-tuple $\left(I D_{j}, \rho_{j}, G_{j}^{(i)}\right)$. For ease of exposition, in this paper, we assume $I D_{j}=j$ and the broadcast information is a 3-tuple $\left(j, \rho_{j}, G_{j}^{(i)}\right)$. The intensity $\rho_{j}$ is not needed for construction of local contention graphs, and will be used only for the computations of beliefs and messages (to be described in the proofs of Feature 2 and Feature 3). Thus, in the following, we focus on the 2-tuple $\left(j, G_{j}^{(i)}\right)$ that can be extracted from the 3-tuple.

## Construction of Local Contention Graph $G_{j}$

By assumption, each vertex $j$ could hear the broadcast of all its one-hop neighbors. For each neighbor $i \in N_{j}$, the broadcast 2-tuple is $\left(i, G_{i}^{(i)}\right)$. Vertex $j$ will construct a local contention graph $G_{j}$ based on $\left(i, G_{i}^{(i)}\right)$ from all $i \in N_{j}$.

Initially $G_{i}^{(i)}=(i, \varnothing)$ and is not accurate. However, at least all $i \in N_{j}$ could be identified by vertex $j$ after one round of broadcast by the neighbors. In the next round, each vertex $i \in N_{j}$, based on what it hears from its neighbors in the last round, can deduce the set of edges $\left\{(i, k) \mid k \in N_{i}^{(i)}\right\}$. Vertex $i$ will then broadcast $\left(i, G_{i}^{(i)}\right)$ with $G_{i}^{(i)}=\left(N_{i}^{(i)},\{(i, k) \mid k \in N_{i}^{(i)}\}\right)$. Specifically, $G_{i}^{(i)}$ will have the correct vertices, but only edges between $i$ and its neighbors appear; but not those between neighbors. After one more

round, however, this will be fixed, and $G_{i}^{(1)}=$ $\left(N_{i}^{(1)},\{(k, l) \mid k, l \in N_{i}^{(1)},(k, l) \in E\}\right)$ where $E$ are the edges in the complete contention graph $G=(V, E)$. Thus, three rounds of broadcast will make sure the broadcast 2-tuple is correct.

Then, vertex $j$ constructs a local contention graph consisting of the union of its own $G_{j}^{(1)}$ and the $G_{i}^{(1)}$ in its neighborhood: $G_{j}=\bigcup_{i \in N_{j}^{(1)}} G_{i}^{(1)}$.

Property of $G_{j}: G_{j}$ contains all vertices within two hops of vertex $j$. From $G_{j}$, vertex $j$ can identify all maximal cliques to which it belongs (within the overall contention graph $G$ ), as well as all maximal cliques to which each of its neighbor $i \in N_{j}$ belongs. That is, all maximal cliques containing at least one vertex in $N_{j}^{(1)}$ can be identified.

## Construction of Local Region Graph $G_{j}$

Based on $G_{j}$, vertex $j$ then constructs a local region graph $G_{j}$ using the cluster variation method described in Section VI-A, with a small modification, as described in the next paragraph. As in Section VI-A, the first step is to form the set of regions at level 0 , denoted by $\mathbf{R}_{0}^{(j)}$ from the maximal cliques in $G_{j}$ that contains at least one vertex in $N_{j}^{(1)}$. After the construction of $\mathbf{R}_{0}^{(j)}$, we then perform the same procedure as in Section VI-A to construct the regions in lower levels.

The modification is that we will discard all regions that do not contain any vertex in $N_{j}^{(1)}$ (i.e., $V_{R} \cap N_{j}^{(1)}=\varnothing$ ). The discarded regions will have no bearing on the local computation to be performed. In Fig. 6, for example, let us look at vertex 1. We draw the local contention graph $G_{1}$ in Fig. 7(a). By forming maximal cliques, $\mathbf{R}_{0}^{(j)}$ includes regions $\{1,2\},\{1$, $3\},\{3,4\}$ and $\{2,4,5\}$. At level 1 , the intersections of regions in $\mathbf{R}_{0}^{(j)}$ are generated: $\{1\},\{2\},\{3\}$ and $\{4\}$. We discard region $\{4\}$ from level 1 since the sole vertex it contains, vertex 4 , is two hops away from vertex 1 and not in $N_{j}^{(1)}$.
![img-6.jpeg](img-6.jpeg)
(a) Local Contention graph
![img-7.jpeg](img-7.jpeg)
(b) Local Region graph

Fig. 7 An example of construction of a local region graph
As in Section IV-A, for each remaining region $R$, we draw a directed edge from each of its super-regions to it, except for those regions that are super-regions of a super-region of region $R$. We denote the local region graph of vertex $j$ by $G_{j}=\left(\mathbf{V}^{(j)}, \mathbf{E}^{(j)}\right)$. Note that $\mathbf{V}^{(j)}$ here are regions and $\mathbf{E}^{(j)}$ are the directed edges between regions.

## Consistency of Local Region Graph

We next show that the local region graph constructed above is fully consistent with the complete region graph $G$. We re-state Feature 1 more rigorously here.

Feature 1: The local region graph $G_{j}$ constructed from $G_{j}$ is consistent with the complete region graph $G$ in that each region in $G_{j}$ is also a region in $G$, and each edge in $G_{j}$ is also an edge in $G$. That is, (i) $\forall R \in \mathbf{V}^{(j)}, R \in \mathbf{V}$; (ii) $\forall e \in \mathbf{E}^{(j)}, e \in \mathbf{E}$.

The proof of Feature 1 is given in Appendix C. Based on $G_{j}$, we proceed to implement the other procedures of our distributed GBP.

## Selection, Message Computation, and Message Broadcast of Message Agents

As related earlier, for a message $m_{P \rightarrow R}\left(s_{R}\right)$ from a region $P$ to a region $R$, we elect the lowest-ID vertex that is in both $P$ and $R$ to be the message agent responsible for the computation and broadcast of the message. That is, we choose vertex $\arg \min _{i \in V_{P \rightarrow R}}\left(I D_{i}\right)$ to be the message agent for $m_{P \rightarrow R}\left(s_{R}\right)$. Feature 2 (proved in Appendix C) implies that vertex $j$ can identify all messages $m_{P \rightarrow R}\left(s_{R}\right)$ satisfying $j \in V_{P \cap R}$ from its local region graph $G_{j}$. For each such message, vertex $j$ examines the vertices in $V_{P \cap R}$. If it is the vertex with the lowest ID in $V_{P \cap R}$, vertex $j$ will elect itself as the message agent for $m_{P \rightarrow R}\left(s_{R}\right)$. It will compute message $m_{P \rightarrow R}\left(s_{R}\right)$ according to (22), and then broadcast the message to its neighbors.

We prove Feature 3 in Appendix C that vertex $j$ will be able to collect all the information needed for the computation of $m_{P \rightarrow R}\left(s_{R}\right)$. According to (22), other messages may be required for the computation of $m_{P \rightarrow R}\left(s_{R}\right)$. We prove that vertex $j$ will be able to hear the broadcast of these messages by their respective message agents (if vertex $j$ is not itself the agent).

## Belief Computation by All Vertices

Feature 2 states that each vertex $j$ can choose a region $R$ to which it belongs from $G_{j}$ and computes the beliefs $b_{R}\left(s_{R}\right)$ according to (19). It then obtains its throughput by taking marginal probability $t h_{j}=\sum_{s_{R}, s_{j} \cap} b_{R}\left(s_{R}\right)$. Essentially, as with computation of messages, our proof of Feature 2 in Appendix C shows that vertex $j$ will be able to hear the broadcast of the messages required in (19) by their message agents (if vertex $j$ is not itself the agent).

The overall pseudocode of distributed GBP is given below.

## Algorithm 4: Distributed GBP

1. The following procedure runs on each individual vertex independently. We focus on a particular vertex $j$.
2. Let $N_{j}^{(1)}=N_{j} \cup\{j\}$ and $G_{j}^{(1)}$ be the local contention graph consisting of all the vertices in $N_{j}^{(1)}$ and the edges between them. Denote the set of the vertices that are within two-hops of vertex $j$ as well as vertex $j$ by $N_{j}^{(2)}$. Define $G_{j}=\bigcup_{m, N_{j}^{(1)}} G_{j}^{(1)}$.
3. Let $M S_{j}$ be the set of messages to which vertex $j$ is the message agent.
4. Vertex $j$ performs the two threads below in parallel.

Thread 1: Periodical Local Information Update
5. Broadcast $\left(j, \rho_{j}, G_{j}^{(1)}\right)$.
6. By listening to the above broadcast of neighbors $N_{j}$, vertex $j$ derives the local contention graph $G_{j}$. Using the cluster variation method with the small modification described in Section VI-C, vertex $j$ generates the local region graph $G_{j}$.
7. In $G_{j}$ for each message $m_{P \rightarrow R}\left(s_{R}\right)$ satisfying $j \in V_{P \rightarrow R}$, vertex $j$ examines the vertices in $V_{P \rightarrow R}$. If it is the vertex with the lowest ID in $V_{P \rightarrow R}$, vertex $j$ will elect itself as the message agent for the computation and broadcast of $m_{P \rightarrow R}\left(s_{R}\right)$ by adding this $m_{P \rightarrow R}\left(s_{R}\right)$ to $M S_{j}$.
8. Wait for an interval of $T_{1}$ and repeat the operations of lines 5 and 7 , where $T_{1}$ is an update interval determined by how fast the network contention graph varies (according to the network environment, links leaving and joining the system, etc.).

Thread 2: Message Iteration
9. procedure INITIALIZATION
10. $\forall m_{P \rightarrow R}\left(s_{R}\right) \in M S_{j}, \leftarrow \sum_{s_{P \rightarrow R}} \prod_{s_{i} \in S_{P}} \psi\left(s_{i}, s_{j}\right) \prod_{s \in V_{P} \backslash s_{R}} \phi_{i}\left(s_{i}\right)$.
11. end procedure
12. procedure ITERATION
13. broadcast $m_{P \rightarrow R}\left(s_{R}\right) \in M S_{j}$ to all its one-hop neighbors;
14. Wait for time $T_{2}$ to receive messages from its neighbors, $m_{P \rightarrow R}\left(s_{R}\right), \forall P, R \in G_{j}$;
15. Based on the received messages and local information maintained by Thread 1, compute each $m_{P \rightarrow R}\left(s_{R}\right)$ in $M S_{j}$ according to (22);
16. Invoke procedure BELIEFCOMPUTATION and repeat procedure ITERATION;
18. end procedure
19. procedure BELIEFCOMPUTATION
20. Choose any $R$ where $j \in V_{R}$, compute its belief $b_{R}\left(s_{R}\right)$ according to (19), and in turn obtain its throughput $t h_{j}$ from marginal probability.
21. end procedure

## D. Inverse GBP (IGBP)

Analogous to IBP, we can adapt GBP for the access intensities computation to meet the target throughput distribution.

## 1)Message update rules in IGBP

The first step of IGBP is to construct a region graph using the method introduced in Section VI-A. Second, given $\overline{t h}$ (i.e., $b_{i}\left(s_{i}=1\right)$ in the BP context), we can obtain $b_{R}\left(s_{R}\right)$ directly since no more than one link can be active simultaneously in $R$ ( $R$ is a clique). If there is any region in $\mathbf{R}_{0}$ such that the sum of throughputs exceeds 1 , we can immediately conclude that the target $\overline{t h}$ is not feasible.

Invoking (19) and recall that the links in each region form a clique, we can write

$$
\begin{aligned}
& \rho_{j}=\phi_{j}\left(s_{j}=1\right)= \\
& b_{R}\left(s_{R}: s_{j}=1\right) /\left(k_{R} \prod_{R^{\prime} \in \mathbf{R}_{0}} \prod_{R^{\prime} \in \operatorname{Perents}\left(R^{\prime}\right) \backslash \mathbf{R}_{0}} m_{R^{\prime} \rightarrow R^{\prime}}\left(s_{R^{\prime}}\right)\right)
\end{aligned}
$$

where $k_{R}$ is a normalization factor for $\sum b_{R}\left(s_{R}\right)=1$.
Combining (23) with (22), we have the message update rules for IGBP:
i). Based on the messages updated in last iteration and the target throughput, we can solve $\phi_{j}\left(s_{j}=1\right)$ for each $j \in V_{R}$ (i.e., $\rho_{j}$ ) from (23);
ii). using $\phi_{j}\left(s_{j}=1\right)$ computed in step i), we iterate (22) over each parent-child pair in $G$.

The iteration stops when $\phi_{j}\left(s_{j}=1\right) \forall j$ converges or a maximum number of iterations is reached. Similar to IBP, we cannot guarantee that IGBP converges in general. Recall that $\overline{t h}=G B P(G, \widetilde{\rho})$ is an approximation of the actual link throughputs in the CSMA networks. Similarly, IGBP may output a $\widetilde{\rho}$ that does not exactly yield the target $\overline{t h}$ in the actual network. However, because the computation error has been significantly reduced by forming regions, IGBP has a good chance to approach the target throughputs. Our simulations in Section IV-D validated that the computation error of IGBP is consistently lower than $5 \%$ in various networks even if the target throughputs are very close to the upper bound of the capacity region.

## 2)Distributed IGBP

Similar to Distributed GBP, we can also implement IGBP in the distributed manner. We focus on a particular vertex $j$. Besides the local contention graph $G_{j}$ in distributed GBP, vertex $j$ also has a priori belief at vertex $j$ (i.e., the target throughput $t h_{j}$ ).

The construction of $G_{j}$, and in turn $G_{j}$, is similar to that of GBP. All vertices, however, need to compute and broadcast access intensities in each iteration, as follows.

## Computation and Broadcast of All Vertices

Each vertex $j$ in the network computes the access intensity of vertex $j, \rho_{j}$, using (23) and the received messages. After that, it broadcasts the newly computed access intensity $\rho_{j}$ in its neighborhood.

The pseudocode of IGBP is similar to Algorithm 4. Here, we only show the parts that are different.

```
Algorithm 5: Distributed IGBP
In thread 1, remove the broadcast of its access intensity \(\rho_{j}\).
In thread 2, we change from line 10:
10. \(\forall m_{P \rightarrow R}\left(s_{R}\right) \in M S_{j}, \leftarrow \sum_{i_{P, R}} \prod_{s_{i}, p_{i} \in E_{P} ; E_{R}} \psi\left(s_{i}, s_{j}\right)\).
14. Wait for time \(T_{2}\) to receive \(\rho_{i}, \forall i \in N_{j}\) and messages
from its neighbors, \(m_{P \rightarrow R}\left(s_{R}\right), \forall P, R \in G_{j}\);
16. Invoke procedure ACCESSINTENSITYCOMPUTATION
and repeat procedure ITERATION;
17. Broadcast its access intensity \(\rho_{j}\) to all its one-hop neigh-
bors.
18. procedure ACCESSINTENSITYCOMPUTATION
19. Compute its access intensity \(\rho_{j}\) according to (23).
20. end procedure
```


## E. GBP-ACSMA

Analogous to BP-ACSMA, GBP can be adapted for the utility optimization problem as in (11).

## 1)Message update rules in GBP-ACSMA

The first step of GBP-ACSMA is to construct a region graph using the method introduced in Section VI-A.

Second, given the messages in (19), $b_{R}\left(s_{R}\right)$ can be computed. We can obtain the throughput of a vertex $j$ in region $R, t h_{j}$, easily by taking marginal probability from $b_{R}\left(s_{R}\right)$, exploiting the fact that region $R$ is a clique. Using $t h_{j}$ computed above, we can then solve for $\rho_{j}$ from (16).

Third, for each message agent $j$, using the newly updated $\rho_{j}$ in the second step and the received messages, it updates the messages in $M S_{j}$ according to (22).

## 2)Distributed implementation

Similar to Distributed GBP and IGBP, we can also implement GBP-ACSMA in the distributed manner. We focus on a particular vertex $j$. Besides the local contention graph $G_{j}$ in distributed GBP, vertex $j$ also has its utility function $U_{j}\left(t h_{j}\right)$.

The construction of $G_{j}$, and in turn $G_{j}$, is similar to that of GBP. All vertices, however, need to compute and broadcast access intensities in each iteration, as follows.

## Computation and Broadcast of All Vertices

Each vertex $j$ in the network computes the belief of a region to which it belongs according to (19). By taking marginal probability, vertex $j$ gets it throughput $t h_{j}$, using which it solve for $\rho_{j}$ from (16). In addition, each vertex $j$ broadcasts its newly computed access intensity $\rho_{j}$ in its neighborhood.

```
Algorithm 6: GBP-ACSMA
    In thread 1, remove the broadcast of its access intensity \(\rho_{j}\).
    In thread 2, we change from line 10:
10. \(\forall m_{P \rightarrow R}\left(s_{R}\right) \in M S_{j}, \leftarrow \sum_{i_{P, R}} \prod_{s_{i}, p_{i} \in E_{P} ; E_{R}} \psi\left(s_{i}, s_{j}\right)\).
14. Wait for time \(T_{2}\) to receive \(\rho_{i}, \forall i \in N_{j}\) and messages
from its neighbors, \(m_{P \rightarrow R}\left(s_{R}\right), \forall P, R \in G_{j}\);
16. Invoke procedure ACCESSINTENSITYCOMPUTATION
and repeat procedure ITERATION;
17. Broadcast its access intensity \(\rho_{j}\) to all its one-hop neigh-
bors.
18. procedure ACCESSINTENSITYCOMPUTATION
19. Randomly pick a region \(R\) it belongs to, calculate its
    belief \(b_{R}\left(s_{R}\right)\) using (19). By taking marginal probability,
    vertex \(j\) gets its throughput \(t h_{j}\).
20. Solve for its access intensity \(\rho_{j}\) from (16).
21. end procedure
```


## VII. CONCLUSION

This paper is a first attempt to apply belief propagation to the analysis and design of CSMA wireless networks. In particular, we investigate three applications of belief propagation (BP) and generalized belief propagation (GBP): (1) computation of link throughputs given link access intensities; (2) computation of required link access intensities to meet target link throughputs; and (3) optimization of network utility.

We show how the BP and GBP algorithms for all three applications can be implemented in a distributed manner, making them useful in practical network operation. BP works well in terms of speed, and it yields exact results in tree contention graphs. For loopy contention graphs, GBP can improve accuracy at the cost of longer but still manageable convergence time.

With regard to (1), the problem of computing link throughput given link access intensities in very large CSMA networks is intractable [1]. We show, however, that BP and GBP can obtain accurate approximate results within a short time. This application makes use of the direct correspondence between "beliefs" in the BP framework and "link throughputs" in CSMA networks. In loopy graphs, BP can predict link throughputs with a mean error of less than $10 \%$ under various contention-graph and access-intensity settings. GBP can cap the mean error to below $1 \%$ for networks of up to 200 links within seconds of computation time.

With regard to (2), we show that the BP framework can be turned around, so that we treat link throughputs as given and

compute the link access intensities needed to meet them. This gives rise to the inverse BP and inverse GBP algorithms, in which rather than "belief", it is a network parameter, link access intensity, that gets propagated. Our simulation results show that IBP can output access intensities that give link throughputs that are within $10 \%$ of their targets under various contention-graph settings. IGBP can further reduce the difference to below 5\%. As for convergence speed, both IBP and IGBP can yield solutions within seconds in real network operation.

Among the three applications, of particular interest are distributed and adaptive algorithms to (3). A solution was first proposed in [7], in which no message passing is needed. The algorithm of [7] is one that is based on "probe and measure". Specifically, before a link adjusts its access intensity in an iteration, a period of "smoothing" time is needed to measure the difference in its input traffic and output traffic of the last iteration. As shown in this paper, the required smoothing time can be quite excessive in networks that exhibit temporal starvation [6], resulting in very slow convergence. BP and GBP adaptive CSMA algorithms, however, do not have this problem because they are computation-based rather than mea-surement-based. One-hop message passing, however, is required.

Belief propagation has found empirical success in numerous applications (e.g., decoding of LDPC and turbo codes). Typically, the convergence of BP algorithms in these applications is non-trivial to prove (except for tree graphs). Such is the case with belief propagation in CSMA networks as well. For all the scenarios tested, our experiments indicate that both BP and GBP algorithms can converge quickly with accurate computed results. Convergence proofs, however, await future work.

## Reference:

[1] S. Liew, C. Kai, J. Leung and B. Wong, "Back-of-the-Envelope Computation of Throughput Distributions in CSMA Wireless Networks", IEEE Transactions on Mobile Computing, Sep. 2010. Technical report available at http://arxiv.org//pdf/0712.1854.
[2] "Markov random field," http://en.wikipedia.org/wiki/Markov _random_field.
[3] "Belief propagation," http://en.wikipedia.org/wiki/ Belief_propagation.
[4] X. Wang and K. Kar, "Throughput Modeling and Fairness Issues in CSMA/CA Based Ad hoc networks," IEEE INFOCOM, Miami, 2005.
[5] M. Dervy, O. Dousse, and P. Thiran, "Border Effects, Fairness, and Phase Transition in Large Wireless Networks", IEEE INFOCOM 2008, Phoenix, USA.
[6] C. Kai and S. Liew, "Temporal Starvation in CSMA Wireless Networks," Technical Report, The Chinese University of Hong Kong, 2010.
[7] L. Jiang and J. Walrand, "A Distributed CSMA Algorithm for Throughput and Utility Maximization in Wireless Networks," IEEE/ACM Transactions on Networking, Vol. 18, Issue 3, 2010, pp.960-972.
[8] J. Yedidia, W. T. Freeman, and Y. Weiss, "Understanding belief propagation and its generalizations", in IJCAI, 2001.
[9] IEEE Std 802.11-1997, IEEE 802.11 Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specifications.
[10] F. Zayuan, and B. Bensaou, "Fair bandwidth sharing algorithms based on game theory frameworks for wireless ad-hoc networks," IEEE INFOCOM 2004, vol. 2, pp. 1284-1295.
[11] Independent set, http://en.wikipedia.org/wiki/Independent_set_tgraph_ theory).
[12] J. Jiang and S. Liew, "Improving Throughput and Fairness by Reducing Exposed and Hidden Nodes in 802.11 Networks," IEEE Transactions on Mobile Computing, Vol.7, No.1, 2008.
[13] M. Chen, S. Liew, Z. Shao and C. Kai, "Markov Approximation for Combinatorial Network Optimization," in IEEE INFOCOM, 2010.
[14] J. Pearl, "Probabilistic Reasoning in Intelligent Systems: Networks of Plausible Inference," Morgan Kaufmann.
[15] Cayley tree, http://en.wikipedia.org/wiki/Bethe_lattice.
[16] T. Morita, M. Suzuki, K. Wada, and M. Kaburagi, Eds., "Foundations and applications of cluster variation method and path probability method," in Progr. Theor. Phys. Suppl., 1994, vol. 115.
[17] J. S. Yedidia, W. T. Freeman, and Y. Weiss, "Constructing free energy approximations and generalized belief propagation algorithms," MERL, IEEE Trans. on Information Theory, Vol.51, N0.7, July 2005.

## APPENDIX A: INTERPRETATION OF BP IN TREE CONTENTION GRAPH

We now argue that the BP messages propagated in a tree graph can be interpreted as the partition functions of subgraphs. This interpretation reveals why BP can give exact solutions in loop-free graphs.

Consider a vertex $i$ in a tree-like contention graph $G=\{V, E\}$. Graph $G$ is separated into two subtrees if we remove the edge between $i$ and a neighbor $j$. Let $L(j)$ denote the subtree containing $j$, and let $\mathcal{L}(j)$ denote the subgraph formed by removing $j$ from $L(j)$. As before, the edges are implied by the existence of vertices.

Theorem A1: When applying belief propagation to a tree graph, the message from vertex $j$ to vertex $i$ satisfies

$$
\begin{aligned}
& m_{j i}\left(s_{i}=0\right) \propto Z(L(j)) \\
& m_{j i}\left(s_{i}=1\right) \propto Z(\mathcal{L}(j))
\end{aligned}
$$

where $Z(L(j))$ and $Z\left(\mathcal{L}^{\prime}(j)\right)$ are the partition functions of $L(j)$ and $\mathcal{L}^{\prime}(j)$, respectively.
Proof: Let $d_{j}(v)$ denote the shortest distance (in terms of number of hops) from vertex $v$ to vertex $j$ in the subtree $L(j)$. We prove Theorem A1 by mathematical induction as follows:

1) First we consider the case where $d_{j}(v) \leq 1 \quad \forall v \in L(j)$. The vertices $v$, if any, are all leaf nodes. If $\mathcal{L}^{\prime}(j)=\varnothing$, we have

$$
\begin{gathered}
m_{j i}\left(s_{i}=0\right) \propto 1+\rho=Z(L(j)) \\
m_{j i}\left(s_{i}=1\right) \propto 1=Z\left(\mathcal{L}^{\prime}(j)\right)
\end{gathered}
$$

If $\mathcal{L}^{\prime}(j) \neq \varnothing$, suppose that $j$ has $n$ one-hop neighbors in $\mathcal{L}^{\prime}(j)$. We have

$$
\begin{gathered}
m_{j i}\left(s_{i}=0\right) \propto(1+\rho)^{n}+\rho=Z(L(j)) \\
m_{j i}\left(s_{i}=1\right) \propto(1+\rho)^{n}=Z\left(\mathcal{L}^{\prime}(j)\right)
\end{gathered}
$$

2) Suppose that (A1) holds when $\max _{s \in L(j)} d_{j}(v)=k$.

When $\max _{s \in L(j)} d_{j}(v)=k+1$, denote the $n$ neighbors of $j$ by $N_{j}=\left\{r_{1}, r_{2}, \cdots, r_{n}\right\} . L(r)$ and $\mathcal{L}^{\prime}(r)$ are similarly defined for each $r \in N_{j}$. Note that $\forall v \in L(r)$, we have $v \in L(j)$ and $v$ is connected to $j$ through $r$, so $d_{j}(v)=d_{j}(v)-1$.

Thus we have $\forall r \in N_{j}, \max _{v \in L(r)} d_{v}(v) \leq k$. Following the precondition above, $\forall r \in N_{j}$,

$$
\begin{aligned}
& m_{i j}\left(s_{j}=0\right) \propto Z(L(r)) \\
& m_{i j}\left(s_{j}=1\right) \propto Z\left(L^{\prime}(r)\right)
\end{aligned}
$$

By the message update rule defined in (7), the message from $j$ to $i$ is

$$
\begin{aligned}
m_{j i}\left(s_{i}=0\right) & \leftarrow \prod_{v \in N_{j}} m_{i j}\left(s_{j}=0\right)+\rho \prod_{v \in N_{j}} m_{i j}\left(s_{j}=1\right) \\
& \propto \prod_{v \in N_{i}} Z(L(r))+\rho \prod_{v \in N_{j}} Z\left(L^{\prime}(r)\right) \\
& =Z(L(j)) \\
m_{j i}\left(s_{i}=1\right) & \leftarrow \prod_{v \in N_{i}} m_{i j}\left(s_{j}=0\right) \propto \prod_{v \in N_{i}} Z(L(r))=Z\left(L^{\prime}(j)\right)
\end{aligned}
$$

Hence, (A1) holds for $\max _{v \in L(j)} d_{j}(v)=k+1$.
According to (6), the beliefs at $i$ should be

$$
\begin{aligned}
& b_{i}\left(s_{i}=1\right) \propto \rho \prod_{j \in N_{i}} m_{j i}\left(s_{i}=1\right) \\
& b_{i}\left(s_{i}=0\right) \propto \prod_{j \in N_{i}} m_{j i}\left(s_{i}=0\right)
\end{aligned}
$$

After normalization, we have $b_{i}\left(s_{i}=1\right)=$

$$
\begin{aligned}
& \rho \prod_{j \in N_{i}} m_{j i}\left(s_{i}=1\right) /\left(\rho \prod_{j \in N_{i}} m_{j i}\left(s_{i}=1\right)+\prod_{j \in N_{i}} m_{j i}\left(s_{i}=0\right)\right) \\
& =\rho \prod_{j \in N_{i}} Z\left(L^{\prime}(j)\right) /\left(\rho \prod_{j \in N_{i}} Z\left(L^{\prime}(j)\right)+\prod_{j \in N_{i}} Z(L(j))\right) \\
& =\rho Z\left(G-\{i\} \cup N_{i}\right) /\left(\rho Z\left(G-\{i\} \cup N_{i}\right)+Z(G-\{i\})\right)
\end{aligned}
$$

Equation (A2) means that in a tree graph, BP correctly computes $p_{i}\left(s_{i}=1\right)=t h_{i}$ of ICN in the form of $Z_{i} / Z$ expressed in Section II.

## APPENDIX B: PROOF OF THE THEOREM 1

To prove Theorem 1, we first present a simplified belief propagation (SBP) that is equivalent to the original BP in CSMA networks. Using SBP, we show the convergence of IBP.

## A. Simplified belief propagation (SBP)

In the body of the paper, we use two variables to express the messages and beliefs. As mentioned there, the beliefs need to be normalized so that $\sum_{s_{i} \in\{0,1\}} b_{i}\left(s_{i}\right)=1$ and $\sum_{s_{j} \in\{0,1\}} m_{j i}\left(s_{i}\right)=1$. That is, in message passing, only the "ratios" are useful. Noting that in a finite CSMA network, the belief of a link state cannot be either 1 or 0 according to the ICN model. We define

$$
n_{i j}=\frac{m_{i j}\left(s_{j}=1\right)}{m_{i j}\left(s_{j}=0\right)}
$$

and

$$
c_{i}=\frac{b_{i}\left(s_{i}=1\right)}{b_{i}\left(s_{i}=0\right)}
$$

Instead of dealing with $b_{i}\left(s_{i}=0\right), b_{i}\left(s_{i}=1\right)$, $m_{i j}\left(s_{j}=0\right)$, and $m_{i j}\left(s_{j}=1\right)$, we can deal with $c_{i}$ and $n_{i j}$. Accordingly, the update rules of BP are revised as follows:

$$
\left.\begin{array}{l}
b_{i}\left(s_{i}=0\right)=k_{i} \prod_{j \in N_{i}} m_{i j}\left(s_{i}=0\right) \\
b_{i}\left(s_{i}=1\right)=k_{i} \rho_{i} \prod_{j \in N_{i}} m_{i j}\left(s_{i}=1\right)
\end{array}\right\} \Rightarrow c_{i}=\rho_{i} \prod_{j \in N_{i}} n_{j i}
$$

From (7), we have

$$
\left.\begin{array}{l}
m_{j i}\left(s_{i}=0\right)=\frac{b_{j}\left(s_{j}=0\right)}{k_{j} m_{i j}\left(s_{j}=0\right)}+\frac{b_{j}\left(s_{j}=1\right)}{k_{j} m_{i j}\left(s_{j}=1\right)} \\
m_{j i}\left(s_{i}=1\right)=\frac{b_{j}\left(s_{j}=0\right)}{k_{j} m_{i j}\left(s_{j}=0\right)}
\end{array}\right\} \Rightarrow n_{j i}=\frac{n_{i j}}{n_{i j}+c_{j}}
$$

Equations (B3) and (B4) form a simpler update rule to perform belief propagation. The number of equations is reduced by half.

## B. Proof the Theorem 1

In IBP, the belief of each link $b_{j}\left(s_{j}\right)$ is given from the target throughput. That is, $c_{j}$ defined in (B2) is pre-fixed in IBP and there is no need to update it. In SBP, the message update rule is (B4). It iterates (B4) over all vertices $j$, and the desired link access intensity $\rho_{j}$ is obtained from

$$
\rho_{j}=\frac{c_{j}}{\prod_{i \in N_{j}} n_{i j}}
$$

Recall that only "ratios" are useful in belief propagation, the simplified IBP defined by (B4) and (B5) is similar to the IBP defined by (8) and (9) in nature. We next investigate the convergence of the simplified IBP.

If the target throughput of IBP is feasible in the sense that $\overrightarrow{i h}=B P(G, \bar{\rho})$ for some $\bar{\rho}$, then the desired output of IBP should be $\bar{\rho}$. In message update, we denote the corresponding messages by $n_{j i}^{*}$. That is, $n_{j i}^{*}$ is the converged message if the algorithm converges correctly.

Consider any pair of vertices which perform the IBP procedure. Let $n_{j i}^{(k)}$ be the message from vertex $j$ to vertex $i$ in the $k^{\text {th }}$ iteration. In the $(k+1)^{\text {th }}$ iteration, the messages computed are

$$
n_{i j}^{(k+1)}=\frac{n_{j i}^{(k)}}{n_{j i}^{(k)}+c_{i}}
$$

and

$$
n_{j i}^{(k+1)}=\frac{n_{i j}^{(k+1)}}{n_{i j}^{(k+1)}+c_{j}}=\frac{n_{j i}^{(k)}}{n_{j i}^{(k)}+c_{j} n_{j i}^{(k)}+c_{i} c_{j}}
$$

We look at the distance between $n_{j i}^{(k)}$ and $n_{j i}^{*}$. Write $\Delta n_{j i}^{(k)}=\left|n_{j i}^{(k)}-n_{j i}^{*}\right|$. To show that the message computed in IBP converges, it is sufficient to show that

$$
\Delta n_{j i}^{(k+1)} \leq \varepsilon \Delta n_{j i}^{(k)} \text { for some } \varepsilon<1
$$

That is, the messages iterated in IBP is a contraction mapping and guaranteed to converge to the fixed point $n_{j i}^{*}$.

The following shows (B7):
Because $n_{\beta}^{*}$ is the desired fixed point, we have

$$
\begin{aligned}
& n_{\beta}^{*}=\frac{n_{\beta}^{*}}{n_{\beta}^{*}+c_{j} n_{\beta}^{*}+c_{i} c_{j}} \\
& \Delta n_{\beta}^{(k+1)}=\left|n_{\beta}^{(k+1)}-n_{\beta}^{*}\right|=\left|\frac{n_{\beta}^{(k)}}{n_{\beta}^{(k)}+c_{j} n_{\beta}^{(k)}+c_{i} c_{j}}-\frac{n_{\beta}^{*}}{n_{\beta}^{*}+c_{j} n_{\beta}^{*}+c_{i} c_{j}}\right| \\
& =\frac{c_{i} c_{j}\left|n_{\beta}^{(k)}-n_{\beta}^{*}\right|}{\left(n_{\beta}^{(k)}+c_{j} n_{\beta}^{(k)}+c_{i} c_{j}\right)\left(n_{\beta}^{*}+c_{j} n_{\beta}^{*}+c_{i} c_{j}\right)} \\
& =\frac{c_{i} c_{j} \Delta n_{\beta}^{(k)}}{\left(n_{\beta}^{(k)}+c_{j} n_{\beta}^{(k)}+c_{i} c_{j}\right)\left(n_{\beta}^{*}+c_{j} n_{\beta}^{*}+c_{i} c_{j}\right)}
\end{aligned}
$$

From (B8), we know that $n_{\beta}^{*}+c_{j} n_{\beta}^{*}+c_{i} c_{j}=1$. Furthermore, $n_{\beta}^{(k)}+c_{j} n_{\beta}^{(k)}>0$. Thus,

$$
\frac{c_{i} c_{j}}{\left(n_{\beta}^{(k)}+c_{j} n_{\beta}^{(k)}+c_{i} c_{j}\right)\left(n_{\beta}^{*}+c_{j} n_{\beta}^{*}+c_{i} c_{j}\right)}<1
$$

## APPENDIX C: DISTRIBUTED IMPLEMENTATION OF GBP

This section proves the three features for correct operation of Distributed GBP. We first review and summarize some properties of the region graph $G$ constructed using the method in Section VI-A, as well as some properties of the local contention graph $G_{j}$ and local region graph $G_{j}$ constructed using the method in Section VI-C. These properties will be used in our proofs.

Property 1: All maximal cliques in $G$ that contain at least one vertex in $N_{j}^{(i)}$ can be identified from $G_{j}$. Each region in $\mathbf{R}_{0}^{(j)}$ of $G_{j}$ is one of these maximal cliques. In addition, $\mathbf{R}_{0}$ of $G$ contains all these regions.

Property 2: All regions in $G$ and $G_{j}$ are cliques.
Property 3: For two regions $R$ and $R^{\prime}$ in $G\left(G_{j}\right)$, if $R \cap R^{\prime} \neq \varnothing$, then $R \cap R^{\prime}$ is also a region in $G\left(G_{j}\right.$ if $R \cap R^{\prime}$ contains at least one vertex in $\left.N_{j}^{(i)}\right)$.

Property 4: Consider two regions $R$ and $R^{\prime}$ in $G\left(G_{j}\right)$ such that $R^{\prime} \subset R$. There is a direct edge from $R$ to $R^{\prime}$ if and only if there does not exist another region $R^{\prime \prime}$ in $G\left(G_{j}\right)$ such that $R^{\prime} \subset R^{\prime \prime} \subset R$.

Property 5: Any region in $G$ that contains at least one vertex in $N_{j}^{(i)}$ must also be a region in $G_{j}$.

Property 1 is a property of $G_{j}$, which has been elaborated in the construction of $G_{j}$ in Section VI-C. Properties 2 and 4 are directed consequences of our region graph construction method described in Section VI-A and Section VI-C.

We give an explanation to Property 3 with respect to $G$ as follows (similar explanation applies to $G_{j}$ because it uses the same construction method). In the construction of $G$, all regions except those in $\mathbf{R}_{0}$ are generated by the intersections of regions at the upper levels. Although we discard some regions during the construction (see Section VI-A, in which it was mentioned that "We then discard from $\mathbf{S}_{k}$ any region $R \in \mathbf{S}_{k}$ where $R \subset R^{\prime} \in \mathbf{S}_{k}$; and any region $R \in \mathbf{S}_{k}$ where $R \in \mathbf{R}_{n}$ for some $n \leq k-1 \ldots$ "), we note these discarded regions either already exist at a higher level, or will be added back at a lower level.

To see Property 5, consider a region $R$ in the complete region graph $G$ containing at least one vertex in $N_{j}^{(i)}$. If $R$ is a maximal clique (i.e., $R \in \mathbf{R}_{0}$ ), then by Property 1, $R \in \mathbf{R}_{0}^{(j)}$. If $R$ is not a maximal clique, then $R$ has at least two ancestors in $\mathbf{R}_{0}, R^{\prime}, R^{\prime \prime} \in \mathbf{R}_{0}$, containing a vertex in $N_{j}^{(i)}$. By Property 1, $R^{\prime}, R^{\prime \prime} \in \mathbf{R}_{0}^{(j)}$. Thus, by Property 3, $R \in \mathbf{V}^{(j)}$. In summary, $R \in G_{j}$.

Proof of Feature 1: We first prove (i). First, consider the regions at level 0 . By Property 1 , all $R \in \mathbf{R}_{0}^{(j)}$ must also be in $\mathbf{R}_{0}$. A region $R$ at a lower level of $G_{j}(G)$ is generated from the intersection of the regions at the upper layers. In particular, lower-level regions are induced by the regions at level 0 . By Property 3, each region $R$ in $\mathbf{V}^{(j)}$ at levels below level 0 must also be a region in $\mathbf{V}$. That is, $\forall R \in \mathbf{V}^{(j)}, R \in \mathbf{V}$. The local region graph $G_{j}$ does not include any extraneous regions not in $G$.

We prove (ii) by contradiction. Suppose that there is a pair of parent-child regions $R, R^{\prime}$ in $G_{j}$ with an edge between them in $G_{j}$ but no edge between them in $G$. Without loss of generality, let $R$ be the parent, (i.e, $R^{\prime} \subset R$ ). Invoking Property 4, there must exist a region $R^{\prime \prime} \in \mathbf{V}$ and $R^{\prime \prime} \notin \mathbf{V}^{(j)}$, such that $R^{\prime} \subset R^{\prime \prime} \subset R$. Note that by our construction method for $G_{j}, R^{\prime}$ must contain at least one vertex in $N_{j}^{(i)}$. Together with $R^{\prime} \subset R^{\prime \prime}$, this means $R^{\prime \prime}$, which is not in $G_{j}$, must have at least one vertex in $N_{j}^{(i)}$. This contradicts Property 5. $\square$

Before we proceed to prove Features 2 and 3, we put down an extra property of our region graph.

Property 6: Consider two regions $R$ and $R^{\prime}$ in $G$ between which there is an edge. If $R$ and $R^{\prime}$ are also regions in $G_{j}$, there must be an edge between them as well in $G_{j}$.
Proof of Property 6: Without loss of generality, we assume $R$ is the parent of $R^{\prime}$. Invoking Property 4, there does not exist another region $R^{\prime \prime}$ in $G$ such that $R^{\prime} \subset R^{\prime \prime} \subset R$. Suppose that $R$ and $R^{\prime}$ also exist in $G_{j}$ and there is no

edge between them in $G_{j}$. Invoking Property 4, there must be another region $R^{\prime \prime}$ in $G_{j}$ such that $R^{\prime} \subset R^{\prime \prime} \subset R$. However, according to Feature $1, G_{j}$ does not contain any extraneous regions not in $G$. Thus, the existence of the extraneous region $R^{\prime \prime}$ cannot be true.

Feature 1' below combines Properties 5 ad 6 to facilitate articulation of the proofs of Features 2 and 3 later:

Feature 1': Any region $R$ in $G$ that contains at least one vertex in $N_{j}^{(1)}$ must also be a region $R$ in $G_{j}$. Consider two regions $R$ and $R^{\prime}$, both having at least one vertex in $N_{j}^{(1)}$. If there is an edge between $R$ and $R^{\prime}$ in $G$, there is also an edge between $R$ and $R^{\prime}$ in $G_{j}$.
Comment: Recall that Feature 1 means there are no extraneous regions or extraneous edges between regions in $G_{j}$. Feature 1' is sort of a converse to Feature 1. As will be seen, it means that the portion of the region graph structure in $G$ needed for the computation of local beliefs and messages by vertex $j$ is exactly duplicated in $G_{j}$.

We next prove Features 2 and 3.
Proof of Feature 2: According to Feature 1, vertex $j$ has a local region graph $G_{j}$ with no extraneous vertices or edges absent in $G$. According to Feature 1', all regions in $G$ that contain vertex $j$ must also be in $G_{j}$. Thus, vertex $j$ could identify all the regions in $G$ to which it belongs. For belief computation, vertex $j$ could choose a small region $R$ among such regions (for computation simplicity). For vertex $j$ to compute $b_{R}\left(s_{R}\right)$ as per (19), it needs the following information: (a) $\psi\left(s_{i}, s_{k}\right), \forall(i, k) \in E_{R}$ (note: we change the index $j$ in (19) to $k$ here to avoid confusion with vertex $j$ here) and $\phi_{i}\left(s_{i}\right) \forall i \in V_{R}$, and (b) the messages from external regions into $\mathbf{D}_{R}$.
(a) is trivial because all $i \neq j$ that are in $R$ are one-hop neighbors of $j$. Thus, the broadcast of their access intensities $\phi_{i}(1)=\rho_{i}$, as described in Section VI-C, can be heard by vertex $j$; and $\phi_{i}(0)=1$ by definition. As to $\psi\left(s_{i}, s_{k}\right)$, it is already available by definition: $\psi\left(s_{i}, s_{k}\right)=0$ if $s_{i}=s_{k}=1$; $\psi\left(s_{i}, s_{k}\right)=1$ otherwise.
(b) needs to be further separated into two steps. Vertex $j$ needs to be able to (i) identify the external messages for $\mathbf{D}_{R}$, and (ii) hear them when their agents broadcast them. An external message passed into a region $R^{\prime} \in \mathbf{D}_{R}$ is of the form $m_{P^{\prime} \rightarrow R^{\prime}}\left(s_{R^{\prime}}\right)$, where $P^{\prime}$ is a parent region of $R^{\prime}$ not within $\mathbf{D}_{R}$.

For (i), we note that $R^{\prime} \subseteq R$ because $R^{\prime}$ is either $R$ or a descendant of $R$. Thus, all vertices in $R^{\prime}$ are one-hop neighbors of vertex $j$. Combining with $R^{\prime} \subset P^{\prime}$, we deduce that $P^{\prime}$ must have at least one vertex that is in $N_{j}^{(1)}$. Invoking Feature 1', we have that both $P^{\prime}$ and $R^{\prime}$ are regions in $G_{j}$, and there is an edge from $P^{\prime}$ to $R^{\prime}$ in $G_{j}$. Since there are no extraneous regions and edges in $G_{j}$ either (Feature 1), vertex $j$ will be able to correctly deduce the portion of the graph structure of $G$ relevant to the computation of $b_{R}\left(s_{R}\right)$ (i.e., this portion is exactly duplicated in $G_{j}$ ).

For (ii), according to our distributed implementation, a vertex $i \in R^{\prime}$ is chosen as the agent for the computation and broadcast of $m_{P^{\prime} \rightarrow R^{\prime}}\left(s_{R^{\prime}}\right)$. Since all vertices in $R^{\prime}$ are one-hop neighbor of vertex $j$, vertex $j$ can hear $m_{P^{\prime} \rightarrow R^{\prime}}\left(s_{R^{\prime}}\right)$.

Proof of Feature 3: As mentioned in the first paragraph of the proof of Feature 2, vertex $j$ could identify all regions in $G$ to which it belongs. Suppose that vertex $j$ belongs to two regions $P$ and $R$. According to Features 1 and 1', the presence or absence of an edge between $P$ and $R$ is exactly duplicated in $G_{j}$. If there is an edge, vertex $j$ will be able to decide whether it should be the message agent for the edge (according to our implementation, vertex $j$ will elect itself as the message agent if it is the vertex with the lowest ID in $V_{P \cap R}$ ). If there is no such edge $G_{j}$, then there is no such edge in $G$, and vertex $j$ will not miss out any message for which it is responsible.

Consider a message $m_{P \rightarrow R}\left(s_{R}\right)$ to which vertex $j$ is the agent. For vertex $j$ to compute each $m_{P \rightarrow R}\left(s_{R}\right)$ as per (22), it needs the following information: (a) $\psi\left(s_{i}, s_{k}\right)$, $\forall(i, k) \in E_{P} \backslash E_{R}$ and $\phi_{i}\left(s_{i}\right), \forall i \in V_{P} \backslash V_{R}$, (b) messages $m_{R^{\prime} \rightarrow R^{\prime}}\left(s_{R^{\prime}}\right), \quad R^{\prime} \in \mathbf{D}_{P} \backslash \mathbf{D}_{R}$ and $R^{\prime \prime} \in \operatorname{Parents}\left(R^{\prime}\right) \backslash \mathbf{D}_{P}$, and (c) messages $m_{R^{\prime} \rightarrow R^{\prime}}\left(s_{R^{\prime}}\right), \quad R^{\prime} \in \mathbf{D}_{R}$ and $R^{\prime \prime} \in \operatorname{Parents}\left(R^{\prime}\right) \cap \mathbf{D}_{P} \backslash \mathbf{D}_{R}$.
(a) is trivial. We note that $j \in P$ and $j \in R$. And the rest of the argument is the same as the proof for (a) related to Feature 2 .

The arguments for (b) and (c) are also similar to the argument for (b) in the proof of Feature 2. Essentially, the portion of the graph structure in $G$ relevant to the messages in (b) and (c) are exactly duplicated in $G_{j}$, so that vertex $j$ can identify these messages properly. Furthermore, the agents for these messages must be either vertex $j$ itself or one-hop neighbors of vertex $j$.

APPENDIX D: FIXED POINT OF BP IN THE RING GRAPH
We prove that BP converges to the fixed point $b_{1}\left(s_{i}=0\right)=(1+\sqrt{1+4 \rho}) / 2 \sqrt{1+4 \rho}$ for each vertex in any $N$-vertex ring graph regardless of $N$.

## Proof:

By symmetry, in each iteration, the messages being passed from $i$ to $j$ are the same for all pairs of neighbors $i, j$. Let the vector $\binom{m^{(n)}(0)}{m^{(n)}(1)}$ denote the message being passed in iteration $n$. We omit the subscripts $i, j$ in our notation because all messages are the same. Applying (7) on this ring contention graph, we get the following dynamic equation for messages:

$$
\binom{m^{(n)}(0)}{m^{(n)}(1)}=\left(\begin{array}{cc}
\phi(0) & \phi(1) \\
\phi(0) & 0
\end{array}\right)\binom{m^{(n-1)}(0)}{m^{(n-1)}(1)}=\left(\begin{array}{cc}
1 & \rho \\
1 & 0
\end{array}\right)\binom{m^{(n-1)}(0)}{m^{(n-1)}(1)}
$$

From (C1), we can get

$$
\begin{aligned}
& m^{(n)}(0)=m^{(n-1)}(0)+\rho m^{(n-2)}(0) \\
& m^{(n)}(1)=m^{(n-1)}(0)
\end{aligned}
$$

The solution to the difference equation (the first equation in (C2)) is

$$
m^{(n)}(0)=C z_{1}^{n}+D z_{2}^{n}
$$

where $z_{1}, z_{2}=\frac{1 \pm \sqrt{1+4 \rho}}{2}$, and $C$ and $D$ are constants to match the boundary condition.

For example, if $\binom{m^{(0)}(0)}{m^{(0)}(1)}$ has been initialized to $\binom{1}{1}$. Then

$$
\begin{aligned}
& C+D=1 \\
& C z_{1}+D z_{2}=1+\rho
\end{aligned}
$$

which gives

$$
\begin{aligned}
& C=\frac{1+\rho-z_{2}}{z_{1}-z_{2}}=\frac{\frac{1}{2}+\rho+\frac{1}{2} \sqrt{1+4 \rho}}{\sqrt{1+4 \rho}}=\frac{\frac{1}{2}+\rho}{\sqrt{1+4 \rho}}+\frac{1}{2} \\
& D=\frac{-\frac{1}{2}-\rho+\frac{1}{2} \sqrt{1+4 \rho}}{\sqrt{1+4 \rho}}=-\frac{\frac{1}{2}+\rho}{\sqrt{1+4 \rho}}+\frac{1}{2}
\end{aligned}
$$

The belief is given by

$$
\begin{aligned}
& b^{(n)}(0)=\frac{\phi(0) m^{(n)}(0)^{2}}{\phi(0) m^{(n)}(0)^{2}+\phi(1) m^{(n)}(1)^{2}} \\
& \rightarrow \frac{z_{1}^{2 n}}{z_{1}^{2 n}+\rho z_{1}^{2(n-1)}}=\frac{1}{1+\rho\left(\frac{1+\sqrt{1+4 \rho}}{2}\right)^{-2}} \\
& =\frac{1+2 \rho+\sqrt{1+4 \rho}}{1+4 \rho+\sqrt{1+4 \rho}}=\frac{(1+\sqrt{1+4 \rho})^{2}}{2 \sqrt{1+4 \rho}[1+\sqrt{1+4 \rho}]} \\
& =\frac{(1+\sqrt{1+4 \rho})}{2 \sqrt{1+4 \rho}}
\end{aligned}
$$