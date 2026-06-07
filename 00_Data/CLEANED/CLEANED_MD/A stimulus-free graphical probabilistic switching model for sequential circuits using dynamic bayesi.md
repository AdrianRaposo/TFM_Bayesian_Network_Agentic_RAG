# A Stimulus-free Graphical Probabilistic Switching Model for Sequential Circuits using Dynamic Bayesian Networks 

SANJUKTA BHANJA*, KARTHIKEYAN LINGASUBRAMANIAN* and N. RANGANATHAN*<br>* Department of Electrical Engineering<br>${ }^{+}$Department of Computer Science and Engineering<br>University of South Florida, Tampa, FL

We propose a novel, non-simulative, probabilistic model for switching activity in sequential circuits, capturing both spatio-temporal correlations at internal nodes and higher order temporal correlations due to feedback. This model, which we refer to as the temporal dependency model (TDM), can be constructed from the logic structure and is shown to be a dynamic Bayesian Network. Dynamic Bayesian Networks are extremely powerful in modeling high order temporal as well as spatial correlations; it is an exact model for the underlying conditional independencies. The attractive feature of this graphical representation of the joint probability function is that not only does it make the dependency relationships amongst the nodes explicit but it also serves as a computational mechanism for probabilistic inference. We report average errors in switching probability of 0.006 , with errors tightly distributed around the mean error values, on ISCAS'89 benchmark circuits involving up to 10000 signals.

Categories and Subject Descriptors: B.8.2 [Performance Analysis and Design Aids]: Power estimation


# 1. INTRODUCTION 

The ability to form accurate estimates of power usage, both dynamic and static, of VLSI circuits is an important issue for rapid design-space exploration. In circuits that are in active mode most of the time or those that switch between the active and standby modes, the total power (both static and active) becomes strongly input dependent [Nguyen et al. 2003; Srivastava et al. 2004]. In this work, we capture this input dependence by constructing a switching model.

Note that the switching model is extremely relevant of both static and dynamic component of power as shown in Eqn. 1 [Nguyen et al. 2003]. In this equation, $P_{d g}$ represents the dynamic component of power at the output of a gate g. The impact of data on dynamic component of power is encapsulated in $\alpha$, the individual switching activity. The static component of power $P_{s g}$ is dominated by $P_{l e a k, i}$, leakage loss in a leakage mode i. It has to be noted that each leakage mode is determined by the steady state signals that each transistor in the gate would be in. For example, in a two input (say A and B) NAND gate, the gate would have four dominant leakage mode ( $\mathrm{i}=4: A_{\oplus 0} B_{\oplus 0}, A_{\oplus 0} B_{\oplus 1}, A_{\oplus 1} B_{\oplus 0}$ and $A_{\oplus 1} B_{\oplus 1}$ ). $\beta$ is the probability of each mode i and for example $\beta_{1}=p\left(A_{\oplus 0}, B_{\oplus 1}\right)$ and is the joint probability of multiple signals in a gate and are dependent on the input data profile.

$$
\begin{aligned}
P_{t} & =\sum_{g} P_{t g}=P_{d g}+P_{s g} \\
& =0.5 \alpha f V_{d d}^{2} C_{\text {load }+ \text { wire }}+\sum_{i} P_{l e a k, i} \beta_{i}
\end{aligned}
$$

Switching activity $\alpha$ in Eq. 1 is one of the important component that is a direct yield from the switching model and contributes to the dynamic power dissipation that is independent ACM Transactions on Design Automation of Electronic Systems, Vol. , No. , 20.

of the technology of the implementation of the VLSI circuit. Contribution to total power due to switching is dependent on the logic of the circuit and the inputs and will be present even if sizes of circuits reduce to nano domain. Apart from contributing to power, switching in circuits is also important from reliability point of view and hence can be considered to be fundamental in capturing the dynamic aspects of VLSI circuits.

Among different types of VLSI circuits, switching in sequential circuits, which also happens to be the most common type of logic, is the hardest to estimate. Even though a large set of research work is performed in this area, almost all of it are input stimuli based and focus of the research is centered around obtaining a correct set of prior probabilities for the state nodes. This is particularly due to the complex higher order dependencies in the switching profile, induced by the spatio-temporal components of the main circuit but mainly caused by the state line feedbacks that are present. These state line feedbacks are not present in pure combinational circuits. One important aspect of switching dependencies in sequential circuits that one can exploit is the first order Markov property, i.e. the system state is independent of all past states given just the previous state. This is true because the dependencies are ultimately created due to logic and re-convergence, using just the current and last values.

The complexity of switching in sequential circuits arises due to the presence of feedback in basic components such as flip-flops and latches. The inputs to a sequential circuit are not only the primary inputs but also these feedback signals. The feedback lines can be looked upon as determining the state of the circuits at each time instant. The state probabilities affect the state feedback line probabilities that, in turn, affect the switching probabilities in the entire circuit. Thus, formally, given a set of inputs $i_{t}$ at a clock pulse and present states $s_{t}$, the next state signal $s_{t+1}$ is uniquely determined as a function of $i_{t}$ and $s_{t}$. At the next clock pulse, we have a new set of inputs $i_{t+1}$ along with state $s_{t+1}$ as an input to the circuit to obtain the next state signal $s_{t+2}$, and so on. Hence, the statistics of both spatial

![img-0.jpeg](img-0.jpeg)

Fig. 1. A model for sequential circuit.
and temporal correlations at the state lines are of great interest. It is important to be able to model both kinds of dependencies in these lines.

Previous work in [Bhanja and Ranganathan 2001] has shown that a combinational circuit can be exactly modeled in a probabilistic Bayesian Network(BN). Such models capture both the temporal and spatial dependencies in a compact manner using conditional probability specifications. For combinational circuits, first order temporal models are sufficient to completely capture dependencies under zero-delay. The attractive feature of the graphical representation of the joint probability distribution is that not only does it make the conditional dependencies among the nodes explicit, but it also serves as a computational mechanism for efficient probabilistic updating. This BN structure, however, cannot model cyclical logical structure, like those induced by the feedback lines. This cyclic dependence affects the state line probabilities that, in turn, affects the switching probabilities in the entire circuit.

# 1.1 Overview 

In this work, we propose a probabilistic, non-simulative, predictive model of the switching in sequential circuits using temporal dependency model (TDM) structure that explicitly models the higher order temporal and spatial dependencies among the feedback lines. The nodes in TDM represent switching activities at the primary inputs, state line feedbacks, and internal lines, in the form of random variables. These random variables are defined over four states, representing four possible signal transitions at each line which are $\left(x_{00}, x_{01}, x_{10}, x_{11}\right)$. Edges of TDM denote direct dependency. Some of the edges represent dependencies within one time slice and with each node (line) we associate conditional probability of switching at the output line of a gate given the switching at the input lines of that gate. Rest of the edges are temporal, i.e. the edges are between nodes from different time slices, capturing the state dependencies between two consecutive time slices. We add another set of temporal edges between the same input line at two consecutive slices, capturing the implicit spatio-temporal dependencies in the input switchings. Temporal edges between just consecutive slices are sufficient because of the first order Markov property of the underlying logic. We prove that the TDM structure is a Dynamic Bayesian Network (DBN) capturing all spatial and higher order temporal dependencies among the switchings in a sequential circuit. It is a minimal representation in terms of size, exploiting all the independencies. The model, in essence, builds a minimally factored representation of the joint probability distribution of the switchings at all the lines in the circuit.

We consider two inference algorithms to form the estimates from the built TDM representations: one is an exact scheme and the other is a hybrid scheme. The exact inferences scheme, which is based on local message passing, is presently practical for small circuits due to computational demands on memory. For large circuits, we resort to a hybrid inference method based on a combination of local message passing and importance sampling. Note that this sampling based probabilistic inference is non-simulative and is different from

samplings that are commonly used in circuit simulations. In the latter, the input space is sampled, whereas in our case both the input and the line state spaces are sampled simultaneously, using a strong correlative model, as captured by the Bayesian network. Due to this, convergence is faster and the inference strategy is stimulus-free.

The key features of this work are:
(1) This is a completely probabilistic model. This means that we do not perform inputpattern driven simulation rather focus on a random walk in the probabilistic dependency model. Hence we target the "circuit problem" rather than the "input problem" [Marculescu et al. 1999].
(2) In this work we introduce a method for handling higher order temporal dependencies in sequential circuits using dynamic bayesian networks.
(3) This work use a stochastic and accurate inference schemes for propagating probabilities in the dynamic Bayesian Networks.
(4) Since we represent the joint probability distribution of the entire variables including switching of state and signals, our model is capable of accurately predicting the coupling behavior of not only the individual switching activities, but also the probability of joint occurrence of events namely probability of two neighboring signals in a transistor stack remaining at zero. We also get $P\left(X_{0 \rightarrow 1}, Y_{1 \rightarrow 0}\right)$ for two neighboring lines that measures how often these two signals would be in the worst case cross-talk situation.
(5) These probabilistic set up are extremely capable and are mostly used for non-causal backward inferencing along with the forward propagation. For example, we would be able to see what type of input profile provides a low switching for a node that has high load capacitance and these could be used to characterize the input space. With probabilistic forward propagation, we need to an evolutionary search to find such characterization.

# 2. PRIOR WORK 

Since our work falls in the broad category of probabilistic methods of estimation, we start with a few break-throughs in probabilistic estimation for combinational circuit. In [Najm 1993], the concept of transition density is introduced and is propagated throughout the circuit by Boolean difference algorithm. However, these methods have problems in handling correlation between nodes and hence, the estimates are inaccurate when the nodes are highly correlated. An accurate way of switching activity estimation is proposed in [Bryant 1992] which has a high space requirement. Tagged probability simulation is proposed in [Ding et al. 1998], which is based on the local OBDD(ordered binary decision diagram) propagation. The signal correlations are captured by using local OBDDs. However, spatiotemporal correlation between the signals is not discussed. Pair-wise correlation between circuit lines were first proposed by Ercolani et al. in [Ercolani et al. 1992]. Marculescu et al. in [Marculescu et al. 1998], studied temporal, spatial and spatio-temporal dependencies as a composition of pair-wise correlations. However, none of these methods could be extended for modeling the dynamics of feedback system.

In one of a pioneering work, Marculescu et al. [Marculescu et al. 2000] proposed a method to find upper and lower bounds for the switching activity in finite state machines (FSMs), using a Markov chain model. This method even though probabilistic is more appropriate when circuit implementation of FSM is not known. In another approach Marculescu et al. used dynamic Markov model to capture the probabilistic temporal structure of the input space in sequential circuits. [Marculescu et al. 1999]. Once a reduced length input data-set is obtained, this method relies on simulation of the circuit for computing the power. In their own words, this work is focused to solve the "input problem" [Marculescu et al. 1999] rather than modeling the circuit probabilistically.

Bhanja et al. [Bhanja and Ranganathan 2001], handle the underlying joint probability distribution for the combinational circuit. In [Bhanja and Ranganathan 2004], we have

also modeled the probabilistic framework for input space by learning a best-fit tree structured Bayesian Networks in inputs which was also used in the partitions of intermediate Bayesian Networks. Hence both of these models were not capable of handling dynamic temporal aspects of a sequential circuits. In [Bhanja and Ranganathan 2004] we focused on mainly three aspects (1)issue of complexity and partitioning heuristics (2) Capturing correlation at the boundaries of adjacent loosely coupled Bayesian Networks and (3) a tree structure learning algorithm for spatio-temporally coupled (correlated) inputs. Sequential circuits have a different problem. Even with the random (spatio-temporally independent) inputs, the spatio-temporal correlation is generated in the circuit due to the feedback mechanism and this increases an induced dependency in the inputs which needs to be modeled separately along with the state feedback.

Most existing techniques for switching estimation in sequential circuits use statistical simulation. Almost all the statistical techniques in one way or the other employ sequential sampling of inputs, along with stopping criteria determined by the assumed statistical model. Stamoulis et al. [Stamoulis 1996] considered a path oriented transition probability computation to sample the input signal space, but the model did not account for correlations between latch and the combinational part. Najm et al. [Najm et al. 1995] proposed logic simulation to obtain the state line probability and then used statistical simulation for estimation.

Tsui et al. [Tsui et al. 1995] used a two-step approach. First, the stationary state line probabilities were estimated instead of state probabilities, thereby reducing the problem complexity but sacrificing the ability to model the spatial dependencies among the state lines. A set of non-linear equations described the relations of the next state to the primary inputs and the current state lines. These equations are solved using the Picard-Peano and Newton-Raphson methods to arrive at locally optimal solution for the individual state line probabilities. Next, given these state probability estimates, statistical simulations (or, ACM Transactions on Design Automation of Electronic Systems, Vol. , No. , 20.

for very small circuits, binary decision diagrams (BDD)) were used to obtain switching estimates. Yuan et al. [Yuan et al. 1997] exploited the observation that beyond a length of samples the inputs can be considered independent. Saxena et al. [Saxena et al. 2002] simulated multiple copies of a circuit, with mutually independent input vectors, thereby generating mutually independent samples. The entire sequential circuit estimates were formed by Monte-Carlo simulation with these inputs. Chen et al. [Chen and Roy 1997] presented a technique to estimate upper and lower bounds of power by considering the signal probability and signal activity at the inputs. Kozhaya et al. [Kozhaya and Najm 2001] enhanced this method in their work to estimate power in sequential circuits.

Even the best simulation based methods suffer from weak input pattern dependencies. Besides, for any change in primary input statistics, simulations need to be rerun. For these reasons, we prefer probabilistic strategies, particularly those that model the underlying joint probability distribution of the node switching. Such probabilistic models, not only allows one to estimate the switching probabilities, but also readily facilitates conditional estimation, i.e. estimation conditioned on the knowledge of the switching statistics at some nodes, not necessarily the input lines. In this work, we propose a graphical probabilistic model over all the state nodes, inputs, and internal lines to accurately model the joint switching probabilities of the whole circuit. The model accounts for high order temporal and spatial dependencies. The exact spatio-temporal correlation is modeled over $n$ time slices to capture higher $(>1)$ order temporal effects that are present in sequential circuits. Circuits modeled using $n$ slices captures $n$-th order temporal dependencies. Similar strategy was used by Tsui et al. [Tsui et al. 1995], who "unrolled" the circuits $n$ times to arrive at the statistics of the individual state lines, which were then used in simulations. We do not restrict ourselves to just state lines. Our comprehensive probability model, spanning multiple time slices, is over all the lines and simultaneously estimates the switching probabilities at all the lines (primary input, internal, and state lines).

# 3. BACKGROUND ON DYNAMIC BAYESIAN NETWORKS 

In this section, we discuss the structure and fundamentals of dynamic Bayesian Networks, which underlies our modeling of sequential circuits as TDMs. Since Dynamic Bayesian Networks are structurally Bayesian Networks themselves, we will highlight important features of Bayesian Networks as well. The following discussion is fashioned after [Pearl 1988; Kjaerulff 1995]. As a peek ahead, the reader can look at Fig. 2 for an example of the representation for a small circuit.

A Bayesian network is a directed acyclic graph (DAG) representation of the conditional factoring of a joint probability distribution. Any probability function $P\left(x_{1}, \cdots, x_{n}\right)$ can be written in the form of conditional probabilities as ${ }^{1}$

$$
P\left(x_{1}, \cdots, x_{N}\right)=P\left(x_{n} \mid x_{n-1}, x_{n-2}, \cdots, x_{1}\right) P\left(x_{n-1} \mid x_{n-2}, x_{n-3}, \cdots, x_{1}\right) \cdots P\left(x_{1}\right)
$$

This expression holds for any ordering of the random variables. In most applications, a variable is usually not dependent on all other variables. There are lots of conditional independencies embedded among the random variables, which can be used to reorder the random variables and to simplify the conditional probabilities.

$$
P\left(x_{1}, \cdots, x_{N}\right)=\Pi_{v} P\left(x_{v} \mid P a\left(X_{v}\right)\right)
$$

where $P a\left(X_{v}\right)$ are the parents of the variable $x_{v}$, representing its direct causes. For example in Fig. 2a $X_{1}, X_{2}$ are the parents of $X_{3}, X_{2}$ is the parent of $X_{4}$. This factoring of the joint probability function can be represented as a directed acyclic graph (DAG), with nodes $(V)$ representing the random variables and directed links $(E)$ from the parents to the children, denoting direct dependencies. The size of the representation, and hence the computational complexity would be dependent on the number of parents per node.

This section discusses some fundamental concepts behind the Bayesian Network based modeling. This is fashioned after [Bhanja and Ranganathan 2003] and is re-iterated here

[^0]
[^0]:    ${ }^{1}$ Probability of the event $X_{i}=x_{i}$ will be denoted simply by $P\left(x_{i}\right)$ or by $P\left(X_{i}=x_{i}\right)$.
    ACM Transactions on Design Automation of Electronic Systems, Vol. , No. , 20.

for the clarity of the readers. The important aspects that signifies a directed acyclic graph as a Bayesian Network are conditional independence and $d$-separation. The DAG structure preserves all the independencies among sets of random variables and is referred to as a Bayesian network. The concept of Bayesian network can be precisely stated by defining the notion of conditional independence among a set of random variables.

Definition 1: Let $\mathrm{U}=\{\alpha, \beta, \cdots\}$ be a finite set of
variables taking on discrete values. Let $P($.$) be the joint probability function over the$ variables in $U$, and let $X, Y$ and $Z$ be any three subsets (maybe overlapping) of $U . X$ and $Y$ is said to be conditionally independent given $Z$ if

$$
P(x \mid y, z)=P(x \mid z) \text { whenever } P(y, z)>0
$$

Following Pearl [Pearl 1988], we denote this conditional independency amongst $X, Y$, and $Z$ by $I(X, Z, Y) ; X$ and $Y$ are said to be conditionally independent given $Z$. For example in Fig. 2a(without the feedback line), we have $I\left(X_{6}, X_{3}, X_{1}\right)$ which denotes $X_{6}$ and $X_{1}$ are conditionally independent given $X_{3}$.

Next, we introduce the concept of $d$-separation of variables in a directed acyclic graph structure (DAG), which is the underlying structure of a Bayesian network. This notion of $d$-separation is then related to the notion of independence amongst triple subsets of a domain.

Definition 2: If $X, Y$ and $Z$ are three distinct node subsets in a DAG $D$, then $X$ is said to be $d$-separated from $Y$ by $Z,<X|Z| Y>$, if there is no path between any node in $X$ and any node in $Y$ along which the following two conditions hold: (1) every node on the path with converging arrows is in $Z$ or has a descendent in $Z$ and (2) every other node is outside $Z$.

Along with the above definitions the following definitions for conditional independence map or I-map and minimal I-map justifies the acceptance of a DAG as a BN.

Definition 3: A DAG $D$ is said to be an I-map of a dependency model $M$ if every $d$-separation condition displayed in $D$ corresponds to a valid conditional independence

relationship in $M$, i.e., if for every three disjoint set of nodes $X, Y$ and $Z$ we have, $<$ $X|Z| Y>\Rightarrow I(X, Z, Y)$.

Definition 4: A DAG $D$ is a minimal I-map of a dependency model $M$ if none of its edges can be deleted without destroying the underlying dependency model.

Definition 5: Given a probability distribution $P$ on a set of variable $U$, a DAG $D$ is called a Bayesian Network of $P$ if $D$ is a minimum I-map of $P$.

There is an elegant method of inferring the minimal I-map of $P$ that is based on the notion of a Markov blanket and a boundary DAG, which are defined below.

Definition 6: A Markov blanket of element $X_{i} \in U$ is an subset $S$ of $U$ for which $I\left(X_{i}, S, U-S-X_{i}\right)$ and $X_{i} \notin S$. A set is called a Markov boundary, $B_{i}$ of $X_{i}$ if it is a minimal Markov blanket of $X_{i}$, i.e. none of its proper subsets satisfy the triplet independence relation.

Definition 7: Let $M$ be a dependency model defined on a set $U=\left\{X_{1}, \cdots, X_{n}\right\}$ of elements, and let $d$ be an ordering $\left\{X_{d 1}, X_{d 2}, \cdots\right\}$ of the elements of $U$. The boundary strata of $M$ relative to $d$ is an ordered set of subsets of $U,\left\{B_{d 1}, B_{d 2}, \cdots\right\}$ such that each $B_{i}$ is a Markov boundary (defined above) of $X_{d i}$ with respect to the set $U_{i}(\subset U)=$ $\left\{X_{d 1}, X_{d 2}, \cdots, X_{d(i-1)}\right\}$, i.e. $B_{i}$ is the minimal set satisfying $B_{i} \subset U$ and $I\left(X_{d i}, B_{i}, U_{i}-B_{i}\right)$. The DAG created by designating each $B_{i}$ as the parents of the corresponding vertex $X_{i}$ is called a boundary DAG of $M$ relative to $d$.

This leads us to the final theorem that relates the Bayesian network to I-maps, which has been proven in [Pearl 1988]. This theorem is the key to constructing a Bayesian network over multiple time slices (Dynamic Bayesian Networks).

Theorem 1: If a graph structure $D$ is a boundary DAG of a dependency model $M$ relative to ordering $d$, then $D$ is a minimal I-map of $M$.

Proof: Please refer to [Pearl 1988].
ACM Transactions on Design Automation of Electronic Systems, Vol. , No. , 20.

# 3.1 DBN Structure 

A Dynamic Bayesian Network (DBN) is a generalization of Bayesian networks to handle temporal effects of an evolving set of random variables. While BN handles dependencies at one time slice DBN handles dependencies between various time slices while preserving the internal dependencies at each time slice. Other formalisms such as hidden Markov models and linear dynamic systems are special cases. The nodes and the links of the DBN are defined as follows. For any time period or slice, $t_{i}$, let a directed acyclic graph (DAG), $G_{t_{i}}=\left(V_{t_{i}}, E_{t_{i}}\right)$, represent the underlying dependency graphical model for the combinational part. Then the nodes of the DBN, $V$, is the union of all the nodes for each time slice.

$$
V=\bigcup_{i=1}^{n} V_{t_{i}}
$$

However, the links, $E$, of the DBN are not just the union of the links in the time-slice DAGs, but also include links between time-slices, i.e. temporal edges, $E_{t_{i}, t_{i+1}}$, defined as

$$
E_{t_{i}, t_{i+1}}=\left\{\left(X_{i, t_{i}}, X_{j, t_{i+1}}\right) \mid X_{i, t_{i}} \in V_{t_{i}}, X_{j, t_{i+1}} \in V_{t_{i+1}}\right\}
$$

where $X_{j, t_{k}}$ is the $j$-th node of the DAG for time slice $t_{k}$. Note that in a generalized structure (Fig. 2b), temporal edges can be drawn from any node of the time slice $t_{k}$ to any node of the time slice $t_{k+1}$. However, the overall representation has be the minimal I-map of the underlying probabilistic model (Fig. 2c).

Thus the complete set of edges $E$ is

$$
E=E_{t_{1}} \cup \bigcup_{i=2}^{n}\left(E\left(t_{i}\right)+E_{t_{i-1}, t_{i}}\right)
$$

Apart from the independencies among the variables from one time slice, we also have the following independence map over variables across time slices if we assume that the random variables representing the nodes follow Markov property [Hachtel et al. 1994], which is true for switching.

$$
I\left(\left\{X_{j, t_{1}}, \cdots, X_{j, t_{i-1}}\right\}, X_{j, t_{i}},\left\{X_{j, t_{i+1}}, \cdots, X_{i, t_{i+k}}\right\}\right) \text { is true } \forall i>1, k>1
$$

where $\mathrm{I}(\mathrm{X}, \mathrm{Z}, \mathrm{Y})$ implies conditional independence.

# 4. TDM MODELING 

The core idea is to express the switching activity of a circuit as a joint probability function, which can be mapped one-to-one onto a Bayesian Network, while preserving the dependencies. To model switching at a line, we use a random variable, $X$, with four possible states indicating the transitions from $\left\{x_{00}, x_{01}, x_{10}, x_{11}\right\}$. For combinational circuits, directed edges are drawn from the random variables representing switching of each gate input to the random variable for switching at the outputs of that gate. At each node, we also have conditional probabilities, given the states of parent nodes. If the DAG structure follows the logic structure then it is guaranteed to map all the dependencies inherent in the combinational circuit. However, sequential circuits cannot be handled in this manner. We have proposed a switching activity estimation model for combinational circuits. A straightforward extension of this model would result in a graph structure shown in Figure 2(a), which is not a DAG and hence is not a Bayesian network.

### 4.1 Structure

Let us consider graph structure of a small sequential circuit shown in Fig. 2(a). Following logic structure will not result in a DAG; there will be directed cycles due to feedback lines. To handle this, we do not represent the switching at a line as a single random variable, $X_{k}$, but rather as a set of random variables, representing the switching at consecutive time instants, $\left\{X_{k, t_{1}}, \cdots, X_{k, t_{n}}\right\}$, and then model the logical dependencies between them by two types of directed links.
(1) For any time instant, edges are constructed between nodes that are logically connected in the combinational part of the circuit, i.e. without the feedback component. Edges are drawn from each random variable representing switching activity at each input of a gate to the random variable representing output switching of the gate.

![img-1.jpeg](img-1.jpeg)

Fig. 2. Comparison of possible graphical models of a sequential circuit (left of part (a)). The representations shown in right side of (a) and in (b) are not used. (a) If one were to treat the circuit as a combinational circuit one gets a logically induced graph structure [Bhanja and Ranganathan 2001]. (b) Time unrolled representation. (c) TDM representation that we propose. Nodes in the graphs represent line switchings.
(2) We connect random variables representing the same state line from two consecutive time instants, $X_{k, t_{i}}^{s} \rightarrow X_{k, t_{i+1}}^{s}$, to capture the temporal dependencies between the switchings at state lines. Moreover, we also connect the random variables representing the switching at primary input lines at consecutive times, $X_{k, t_{i}}^{p} \rightarrow X_{k, t_{i+1}}^{p}$. This is done to capture the constraint in the primary line switching between two consecutive time instants. For instance, if an input has switched from $0 \rightarrow 1$ at time $t_{i}$, then switching at the next time instant cannot

be $0 \rightarrow 0$.

Let us consider Figure 2(b), note that we have all random variables connected to the previous time slice for every slice. This is required as our random variables are switching activities and not logic. Hence, every random variable $X_{i J_{i-1}}$ in this experiment has an edge connecting the variable $X_{i J_{i}}$. However, this representation is not a DBN as it is not minimal. Markov blanket of the switching variables at a time instant $t_{i}$ are still its parents and hence for individual node $X_{i J_{i}}, I\left(X_{i J_{i}}, P a\left(X_{i J_{i}}\right), X_{i J_{i-1}}\right)$ is true, and this implies that given the set of parents $P a\left(X_{i J_{i}}\right), X_{i J_{i}}$ is independent of $X_{i J_{i-1}}$. Hence we could remove edges from $X_{i J_{i-1}}$ to $X_{i J_{i}}$ without hampering the dependency model. However, for primary inputs, we have to make sure that $P\left(X_{k J_{i+1}}^{P} \mid X_{k J_{i}}^{P}\right)$ handles the switching constraints properly. In sequential circuit, each input signal values are considered random, however, for modeling the switching variables the temporal edges in inputs are essential and eliminates the need for explicit temporal dependencies of the intermediate random variables.

We call this graph structure as the temporal dependency model or TDM. Fig. 2(c) shows the TDM for the example sequential circuit in Fig. 2 (a); we just show three time slices here. The dash-dot edges shows the second type of edges mentioned above, which couples adjacent DAGs. We have $X_{2}$ as input and $X_{1}$ as the present state node. Random variable $X_{6}$ represents the next state signal. Note that this graph is a DAG. We next prove that this TDM structure is a minimal representation, hence is a dynamic Bayesian network.

Theorem 2: The TDM structure, corresponding to the sequential circuit is a minimal I-map of the underlying switching dependency model and hence is a dynamic Bayesian network.

Proof: Let us order the random variables $\left\{X_{i J_{i}}\right\}$, such that (i) for two random variables from one time $t_{i}, X_{p J_{i}}$ and $X_{c J_{i}}$, where $p$ is an input line to a gate and $c$ is an output line to the same gate, $X_{p J_{i}}$, appears before $X_{c J_{i}}$ in this ordering and (ii) the random variables for the next time slice $t(i+1),\left\{X_{1 J_{i+1}}, \cdots, X_{n J_{i+1}}\right\}$ appear after the random variables at time ACM Transactions on Design Automation of Electronic Systems, Vol. , No. , 20.

slice $t_{i}$.
With respect to this ordering, the Markov boundary of a node, $X_{i, j_{i}}$, is given as follows. If $X_{i, j_{i}}^{p}$ represents switching of an input signal line, then its Markov boundary is the variable representing the same input in time slice $X_{i, j_{i-1}}^{p}$. If $X_{i, j_{i}}^{s}$ represents switching of a state signal, then its Markov boundary is the variable representing the switching at the previous time slice $X_{i, j_{i-1}}^{s}$. And, since the switching of any gate output line is just dependent on the inputs of that gate, the Markov boundary of a variable representing any gate output line consists of just those that represent the inputs to that gate. In the TDM structure the parents of each node are its Markov boundary elements hence the TDM is a boundary DAG. And, by Theorem 2 the TDM is a minimal I-map and thus a Bayesian network. Since nodes and the edges in the TDM defined over $n$ time slices can be described by Eqn. 5, and Eqn. 7, the TDM is a dynamic Bayesian Network (DBN).

# 4.2 Conditional Probability Specifications 

The joint probability function is modeled by a Bayesian network as the product of the conditional probabilities defined between a node and its parents in the TDM structure: $P\left(x_{v} \mid P a\left(X_{v}\right)\right)$. These conditional probabilities can be easily specified using the circuit logic. There are three basic types of conditional probability specifications: (i) internal lines, (ii) primary input lines, and (iii) state lines. For the internal lines, the specification follows the gate logic. For state lines, the conditional probability models the logic of a buffer, as shown in Table I(b). For primary input lines, the conditional probabilities models the switching constraints between two time instants, as listed in Table I(a). For instance, if the primary line switched from 0 to 1 , then at the next time slice the line can either switch from 1 to 0 or remain at 1 . Since, we are considering random inputs, we distribute the probabilities equally between these two options. For correlated inputs, these conditional probabilities can be adjusted.

Table I. Conditional probability specification between (a) primary input line switchings at consecutive time instants: $P\left(x_{k, t_{i+1}}^{p} \mid x_{k, t_{i}}^{p}\right)$, and (b) state line switchings at consecutive time instants: $P\left(x_{k, t_{i+1}}^{s} \mid x_{k, t_{i}}^{s}\right)$




# 5. INFERENCE IN TDM 

In this section we present three inference schemes for Bayesian Networks. The first one is an exact inference scheme which we used to validate our model. This method is based on local message passing and is computationally expensive. This method is currently practical only for smaller circuits. For larger circuits we used the next two schemes which are hybrid schemes. Both of the schemes are based on stochastic inference. In particular, we use importance sampling based method. The first one: Evidence Pre-propagated Importance Sampling (EPIS) [Yuan and Druzdzel 2003] works efficiently for prediction and also for probabilistic backtracking with evidence. The second algorithm is excellent for estimation/prediction however, degenerates for backtracking.

### 5.1 Exact Inference

This inference method was used to validate our model. We inferenced the smallest circuit, s27, using this method. In the following discussion, the reader is requested to refer to Fig. 3 and Fig. 4 as examples, since they are drawn based on s27. The exact inference scheme is based on local message passing on a tree structure, whose nodes are subsets (cliques) of random variables in the original DAG [Cowell et al. 1999], [Hugin ]. (Fig. 3(a) represents the original DAG structure of s27.) This tree of cliques is obtained from the initial ACM Transactions on Design Automation of Electronic Systems, Vol. , No. , 20.

![img-2.jpeg](img-2.jpeg)

Fig. 3. (a)BN model of s27 for one time slice, (b)Triangulated undirected graph of s27 for one time slice
![img-3.jpeg](img-3.jpeg)

Fig. 4. Junction tree of cliques of s27 for (a)one time slice, (b)two time slices

DAG structure via a series of transformations that preserve the represented dependencies. The original DAG is first converted into an undirected Markov graph structure, which is referred to as the moral graph(Fig. 3(b) without the thick line), modeling the underlying joint probability distribution. This moral graph is obtained from the DAG structure, by adding undirected links between the parents of a common child node. These additional links directly capture the dependencies that were only implicitly represented in the DAG.

In a moral graph, every parent-child set form a complete subgraph. Due to the undirected nature of the moral graph, some of the independencies represented in the DAG would be lost, resulting in a non-minimal representation. The dependency structure is, however, preserved. This loss of minimal representation will eventually result in increased computational demands, but does not sacrifice accuracy. Next, a chordal graph is obtained from the moral graph by triangulating it(Fig. 3(b)). Triangulation is the process of breaking all cycles in the graph to be a composition of cycles over just 3 nodes by adding additional links. To control the computational demands, the goal is to form a triangulated moral graph with minimum number of additional links. Various heuristics exist for this. For instance, the Bayesian network inference software HUGIN (www.hugin.com), which we use in this work, uses efficient and accurate minimum fill-in heuristics to calculate these additional links.

Fig. 4(a) represent the junction tree of cliques for the TDM structure of $s 27$ for one time slice. Cliques of the chordal graph represented in Fig. 3(b) form the nodes of the junction tree. The tree structure is useful for local message passing. Given any evidence, messages consist of the updated probabilities of the common variables between two neighboring cliques. Global consistency is automatically maintained by constructing the tree in such a way that any two cliques, sharing a set of common variables, should have these common variables present in all the cliques that lie in the connecting path between the two cliques. A junction tree with this property can be easily obtained from the same minimum fill-in heuristic algorithm that is used to triangularize the graph [Bhanja and Ranganathan 2003].

Let us consider two neighboring cliques to understand the key feature of the Bayesian updating scheme. Let two cliques $A$ and $B$ have probability potentials $\phi_{A}$ and $\phi_{B}$, respectively, obtained by multiplying the conditional probabilities, in the DAG based Bayesian network, involving the nodes in each clique. Let $S$ be the set of common nodes between cliques $A$ and $B$. The two neighboring cliques have to agree on probabilities on the node ACM Transactions on Design Automation of Electronic Systems, Vol. , No. , 20.

set $S$, which is termed their separator. To achieve this, we first compute the marginal probability of $S$ from probability potential of clique $A$ and then use that to scale the probability potential of $B$. The transmission of this scaling factor, which is needed in updating, is referred to as message passing. New evidence is absorbed into the network by passing such local messages. The pattern of the message is such that the process is multi-threadable and partially parallelizable. Because the junction tree has no cycles, messages along each branch can be treated independent of the others.

The final junction tree of cliques for the TDM structure of $s 27$ for two time slices is more complicated, as shown in Fig. 4(b). Notice the increased number of cliques. In general, the size of the maximal clique will increase. This results in increased memory requirement to store the probability potential over the nodes in the cliques; the increase is exponential in the maximal clique size. Thus, it is obvious that the exact model cannot be used for large circuits. Available memory would determine the maximum circuit size that can be modeled exactly. In this work, we use this inference only for model validation with small circuits.

# 5.2 Hybrid Scheme 

For large circuits, a hybrid scheme, specifically the Evidence Pre-propagated Importance Sampling (EPIS) [Yuan and Druzdzel 2003], which uses local message passing and stochastic sampling, is appropriate. This method scales well with circuit size and is proven to converge to correct estimates. These classes of algorithms are also anytime-algorithms since they can be stopped at any point of time to produce estimates [Ramani and Bhanja 2004; Rejimon and Bhanja 2006]. Of course, the accuracy of estimates increases with time.

The EPIS algorithm is based on Importance Sampling that generates sample instantiations of the whole DAG network, i.e. all for line switching in our case. These samples are then used to form the final estimates. This sampling is done according to an importance function. In a Bayesian Network, the product of the conditional probability functions at

all nodes form the optimal importance function. Let $X=\left\{X_{1}, X_{2}, \cdots, X_{m}\right\}$ be the set of variables in a Bayesian Network, $\operatorname{Pa}\left(X_{k}\right)$ be the parents of $x_{k}$, and $E^{2}$ be the evidence set. Then, the optimal importance function is given by

$$
P(X \mid E)=\prod_{k=1}^{m} P\left(x_{k} \mid P a\left(X_{k}\right), E\right)
$$

This importance function can be approximated as

$$
P(X \mid E)=\prod_{k=1}^{m} \alpha\left(P a\left(X_{k}\right)\right) P\left(x_{k} \mid P a\left(X_{k}\right)\right) \lambda\left(X_{k}\right)
$$

where $\alpha\left(P a\left(X_{k}\right)\right)=P\left(x_{k} \mid E^{+}\right)$and $\lambda\left(X_{k}\right)=P\left(E^{-} \mid x_{k}\right)$, with $E^{+}$and $E^{-}$being the evidence from above and below, respectively, as defined by the directed link structure. For the proof of Eqn. 10 please refer [Yuan and Druzdzel 2003]. Calculation of $\lambda$ is computationally expensive and for this, Loopy Belief Propagation (LBP) [Murphy et al. 1999] over the Markov blanket of the node is used. Yuan et al. [Yuan and Druzdzel 2003] proved that for a poly-tree, the local loopy belief propagation is optimal. The importance function can be further approximated by replacing small probabilities with a specific cutoff value.
5.2.1 Loopy Belief Propagation. Loopy Belief Propagation (LBP) is an approximate inference mechanism. It uses the Pearl's belief propagation algorithm [Pearl 1988] to calculate the posterior belief of each node. Here, we briefly summarize Pearl's belief propagation algorithm. Each node $X$ computes its posterior probability based on the information obtained from its neighbors. i.e., $\operatorname{Bel}(x)=P(X=x \mid E)$, where $E$ represents the evidence set. In a polytree, any node $X$ d-separates $E$ into 2 subsets, $E_{x}^{+}$which is the evidence connected to node $X$ through its parent set $Z$ and $E_{x}^{-}$is the evidence connected to node $X$ through its child set $Y$. Now, the node $X$ can compute its belief by separately combining the messages obtained from its parents and children.

$$
\operatorname{Bel}(x)=\alpha \lambda(x) \pi(x)
$$

[^0]
[^0]:    ${ }^{2}$ Set of nodes that have already observed states.
    ACM Transactions on Design Automation of Electronic Systems, Vol. , No. , 20.

where $\lambda(x)$ and $\pi(x)$ are given by

$$
\lambda(x)=\prod_{U \in C H_{X}} \lambda_{U}(x)
$$

$C H_{X}$ is set of all children of $X$.

$$
\pi(x)=\sum_{z_{1}, z_{2}, \cdots, z_{j}}\left(P\left(x \mid z_{1}, z_{2}, \cdots, z_{j}\right) \prod_{i=1}^{j} \pi_{X}\left(z_{i}\right)\right)
$$

where $z_{1}, z_{2}, \cdots, z_{j}$ are parents of node X .
Once the node computes its belief it sends the updated messages to its neighbors. The message to the parents of node $X$ is given by:

$$
\lambda_{X}(w)=\sum_{x}\left(\sum_{z_{1}, z_{2}, \cdots, z_{k}}\left(P\left(x \mid w, z_{1}, z_{2}, \cdots, z_{k}\right) \prod_{i=1}^{k} \pi_{X}\left(z_{i}\right)\right)\right) \lambda(x)
$$

The message from node $X$ to its child is given by:

$$
\pi_{Y}(x)=\pi(x) \prod_{C \in C H_{X}-Y} \lambda_{C}(x)
$$

For network with loops, during each iteration all nodes calculate their outgoing messages based on the incoming messages from their neighbors during previous iteration. The iteration stops once the belief converges.

# 5.3 Probabilistic Logic Sampling 

Probabilistic Logic Sampling(PLS) developed by Henrion in 1988 is credited to be the first stochastic sampling method for inferencing Bayesian Networks [Henrion 1988]. In this method sampling is performed in the forward direction (from parents to children). The algorithm works as follows,

- In the circuit, which is represented as a Bayesian network, each node is selected and they are sampled.
- While inferencing, the Bayesian network the samples are grouped into sets and the observed values in each sample in a set are compared with the corresponding evidence values.

- If they are inconsistent with each other the whole sample set is discarded.
- The same method is repeated with each sample set.
- Using the selected sample set, the belief distributions are calculated by averaging the frequencies with which the relevant events occur.

With regards to the computational merits, this method has some disadvantages. Since it is based on forward sampling, the evidence that have already occurred cannot be accounted for until the corresponding variables are sampled. The occurrence of unlikely evidence can result in rejection of large number of samples thereby hindering the performance of this method. Due to this PLS is always considered to be better for Bayesian Network inference without evidence.

The above set of stochastic sampling strategies discussed in subsection 5.2 and 5.3 work because in a Bayesian Network the product of the conditional probability functions for all nodes is the optimal importance function. Because of this optimality, the demand on samples is low. We have found that just thousand samples are sufficient to arrive at good estimates for the ISCAS89 benchmark circuits. Note that this sampling based probabilistic inference is non-simulative and is different from samplings that are used in circuit simulations. In the latter, the input space is sampled, whereas in our case both the input and the line state spaces are sampled simultaneously, using a strong correlative model, as captured by the Bayesian Network. Due to this, convergence is faster and the inference strategy is stimulus-free.

# 5.4 Time and Space Complexity 

Exact Inference: Space complexity of the exact inference of Bayesian Network is $O\left(n .4^{\left|C_{\max }\right|}\right)$ [Bhanja and Ranganathan 2004] where $\left|C_{\max }\right|$ is the number of random variables in largest clique in the junction tree, n is the total number of random variables and usually $\left|C_{\max }\right|$ is much less than n . The time complexity of the exact inference is $O\left(p .4^{\left|C_{\max }\right|}\right)$ where p is the number of ACM Transactions on Design Automation of Electronic Systems, Vol. , No. , 20.

cliques in the junction tree which is also much less than n. Even though $\left|C_{\max }\right|$ is less than n , for larger circuits, the exponential nature makes the inference computationaly expensive.

Hybrid Inference: The space requirement of the Bayesian network representation is determined by the space required to store the conditional probability tables at each node. For a node with $n_{p}$ parents, the size of the table is $4^{n_{p}+1}$. The number of parents of a node is equal to the fan-in at the node. In the DBN model we break all fan-ins greater than 2 into a logically equivalent, hierarchical structure of 2 fan-in gates. For nodes with fan-in $f$, we would need $\lceil f / 2\rceil$ extra Bayesian network nodes, each requiring only $4^{3}$ sized conditional probability table. For the worst case, let all nodes in the original circuit have the maximum fan-in, $f_{\max }$. Then the total number of nodes in the BN structure is $n+f_{\max } n / 2$. Thus, the worst case space requirement is linear, i.e. $O 4^{3}\left(n f_{\max }\right)$ where $n$ is the number of nodes, $f_{\max }$ is the maximum fan-in.

The time complexity, based on the stochastic inference scheme, is also linear in $n$, specifically, it is $O(n N)$, where $N$ is the number of samples, which, from our experience with tested circuits, is in the order of 1000's for circuits with 32,424 nodes in the DBN model with three time slices.

# 6. EXPERIMENTAL RESULTS 

We have used the sequential circuits from the ISCAS89 benchmark suite to verify our method. To generate the simulation results the circuits were simulated for 1000000 test vectors. The sequential circuits are modeled as a DBN with 3 time-slices. A startup simulation with 50 random test vectors was performed and these startup estimates of the present state lines are given to the first time-slice of the DBN, i.e. these are the prior probabilities of the state lines. The priors for the primary input lines in the first time-slice of DBN was chosen to be unique, i.e. equally probable switching states. The approximate computation of the DBN was done by a tool named "GeNIe" [Genie ]. The exact computation was done

by a tool named "Hugin" [Hugin ].
The tests were performed on a Pentium IV, 2.00 GHz , Windows XP computer.
First, we show some results that validates the TDM model. For this, we use the $s 27$ benchmark circuit. Table II lists the switching estimates at each line in the circuit as computed by (i) simulation, (ii) the exact inference scheme based on tree of cliques, and (iii) the hybrid EPIS scheme. We used 10 time slices for the TDM representation. Note the excellent agreement of the exact inference scheme with simulation, thus validating that the TDM model is capturing the high order temporal and spatial correlations. The hybrid inference scheme also results in excellent estimates, close to the exact ones.

Table III lists the error statistics of the circuits by TDM-EPIS and TDM-PLS inference schemes. A sample size of 1000 samples was considered for both the schemes. Switching error is the error between the in-house logic simulation and the switching estimates obtained from Bayesian inference. We tabulate both the average error, $\mu_{E}$, and maximum error, $\max _{E}$, over all the nodes in column 2 and column 3 in both Table III(a) \& (b). We also list the percentage of nodes with switching error above 2 standard deviations from the mean error. The fourth column in both Table III(a) \& (b) indicate the run-time of the circuit with the specific inference scheme. The listed elapsed times are obtained by the ftime command in the WINDOWS environment, and is the sum of CPU, memory access and I/O time.

We see that the mean error is extremely small for both TDM-EPIS in Table III(a) and for TDM-PLS in Table III(b) for most benchmark circuits even for larger benchmarks like $s 5378, s 15850$. Even the maximum errors for most circuits are low. However, for some circuits, i.e. $s 208, s 953$ and $s 5378$, the maximum seem to be high, but these errors seem to be isolated to a few nodes as is seen from the low fraction of nodes with error above $2 \sigma$. In most cases, only $5 \%$ of the nodes exceed this error bound. In $s 208$, we see that $\%$ of nodes in $\mu+2 \sigma$ range is around $9 \%$. We also found the accuracy of our model is excellent even ACM Transactions on Design Automation of Electronic Systems, Vol. , No. , 20.

Table II. Switching probability estimates at each line of the $s 27$ benchmark circuit as computed by simulation, by the exact scheme, and by the hybrid EPIS method.


for larger benchmark like $s 15850\left(\mu_{E}=0.004\right)$
Note that the computation time reported for Probabilistic Logic Sampling based inference is almost ten times faster than that by TDM-EPIS based method. However, the importance of TDM-EPIS based inference scheme guarantees convergence to the exact value and also is more efficient than Logic Sampling where observation is made at any nodes other than inputs and plausible input probabilities for such an observation is estimated. This has important application in input space characterization for a desired outcome. TDM-PLS

Table III. Experimental results on switching activity estimation by Dynamic Bayesian network modeling using (a)TDM-EPIS [Yuan and Druzdzel 2003] and (b)TDM-PLS [Henrion 1988] for ISCAS'89 benchmark sequential circuits ( 3 time slices).
(a)


(b)


method is more efficient for relatively larger circuits due to its rapidity. TDM-PLS works better for circuit evaluation than for circuit characterization.

We also present estimation results with non-random inputs, in Table IV. Here two categories of biased inputs were chosen, (1) low switching inputs, where probability for switching is 0.2 (2) high switching inputs with probability of switching 0.6 . The simulation results and the TDM-EPIS results were compared and errors were found to be similar to those with random inputs.

In Table V, we show the modeling for three time slices versus ten time slices for random inputs. We observe that ten time slices do not enhance the quality of estimates. This shows ACM Transactions on Design Automation of Electronic Systems, Vol., No., 20.

Table IV. ESTIMATION WITH NON-RANDOM BIASED INPUTS using TDM-EPIS [Yuan and Druzdzel 2003] (a) Low switching (b) High switching


(b)


that third order temporal models are good enough for our benchmarks, which matches with the observations made in [Tsui et al. 1995; Yuan et al. 1997]. For some specific circuits 50 random input vectors will lead to wrong starting probability values. So in such circuits maximum error will keep on increasing for more time slices. We need more than 50 random vectors to get a proper starting probability values. s 27 and s 526 are perfect example for such circuits. In Table V, notice that $M a x_{E}$ is increasing for 10 time slices of s 27 and s 526 .

Note that the switching model is extremely relevant of both static and dynamic component of power as shown in Eq. 1. In this equation, $P_{d g}$ represents the dynamic component of power at the output of a gate g. The impact of data on dynamic component of power is encapsulated in $\alpha$, the individual switching activity. The static component of power $P_{s g}$ is

Table V. Experimental results on switching activity estimation by Dynamic Bayesian network modeling for ISCAS'89 benchmark sequential circuits for two different time slices.


Table VI. Joint probabilities between specific nodes.


$1_{t-1} 1_{t}$
dominated by $P_{\text {leak }, i}$, leakage loss in a leakage mode i. It has to be noted that each leakage mode is determined by the steady state signals that each transistor in the gate would be in. For example, in a two input (say A and B) NAND gate, the gate would have four dominant leakage mode ( $\mathrm{i}=4: A_{\oplus 0} B_{\oplus 0}, A_{\oplus 0} B_{\oplus 1}, A_{\oplus 1} B_{\oplus 0}$ and $A_{\oplus 1} B_{\oplus 1}$ ). $\beta$ is the probability of each mode i and for example $\beta_{1}=p\left(A_{\oplus 0}, B_{\oplus 1}\right)$ and is the joint probability of multiple signals in a gate and are dependent on the input data profile. These joint probabilities can be captured through our model as shown in Table. VI.

Hence run-time leakage power is dependent on the joint probabilities of the signals that ACM Transactions on Design Automation of Electronic Systems, Vol. , No. , 20.

are present in a transister stack. A combination of steady state 00 at all the signals the transistor stack produces less leakage than a steady state 11 in all of them. Also due to gate leakage the combinations 00 and 11 in two of the stacked signals also can produce considerable amount of total leakage current at sub-100 nm level technologies [Srivastava et al. 2004]. Table VI shows joint probability of a few nodes that are fan-ins to a single gate. Note that in s1238, signal 201 and 202 are fed to a transistor stack. The probability that both the signals remain at logic 0 is $0.01 \%$, while the probability that both the signals remain at logic 1 is $26 \%$. This result signifies that the worst case subthreshold leakage condition is highly probable. The other prominent condition for leakage (gate leakage during subthreshold) occurs when one signal (top of the stack) remains at logic 1 and the other one is at 0 . In Table VI we see that the probability of signal 201 remaining at logic 0 while signal 202 remaining at logic 1 is $15.5 \%$ (considerably high). Likewise we can estimate probabilities of all the dominant leakage mode through the joint probabilities extracted through our model.

Joint probabilities are of importance in determining the upper bound of capacitive coupling noise or crosstalk. The worst case capacitive coupling noise occurs when the neighboring signals switch the opposite way. It means from $0 \rightarrow 1$ on one signal and $1 \rightarrow 0$ on the other. For example in Table VI, consider the neighboring signals 639 and 640. The probability that signal 639 switches from $0 \rightarrow 1$ while signal 640 switches from $1 \rightarrow 0$ is $0.72 \%$, and the probability that signal 639 switches from $1 \rightarrow 0$ while signal 640 switches from $0 \rightarrow 1$ is $0.91 \%$. Both of these conditions are favorable for placing them tightly close to each other. But the same analysis show different results in the neighboring signals 201 and 202. The probability that signal 201 switches from $0 \rightarrow 1$ while signal 202 switches from $1 \rightarrow 0$ is $4.26 \%$, and the probability that signal 201 switches from $1 \rightarrow 0$ while signal 202 switches from $0 \rightarrow 1$ is $4.49 \%$. Both of these conditions are considerably probable and more attention needs to be taken for placing these two neighbors. Likewise we can also

estimate the relative probabilities of logic and delay faults through the joint probabilities extracted through our model.

# 7. CONCLUSIONS 

This paper introduces a switching activity estimation tool that encapsulates all the dependencies, in sequential circuits in reasonable time and with high accuracies. We use graphical probabilistic model (compact, minimal and dependency preserving) of the whole circuit as a single joint distribution function by a Bayesian Network. This is to be noted that the Bayesian Network based approach unifies the estimation of switching probabilities of state nodes and also the circuit nodes. We have shown results of the estimated switching activity for pseudo-random inputs as well as for biased inputs. The model handles higher order spatio-temporal dependencies between the nodes under zero-delay scenario. Our future effort will focus on studying the trade-off between various time slices, convergence issues and also the role and length of initial state probabilities on convergence and accuracy under realistic delay models. One approach that is outlined in [Manich and Figueras 1997] can be used to model switching under realistic delay.
