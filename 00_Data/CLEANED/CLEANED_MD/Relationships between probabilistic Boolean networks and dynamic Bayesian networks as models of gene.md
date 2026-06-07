# NIH Public Access 

## Author Manuscript

Publishing in final edited form as:
Signal Processing. 2006 April ; 86(4): 814-834.

## Relationships between probabilistic Boolean networks and dynamic Bayesian networks as models of gene regulatory networks

Harri Lähdesmäki ${ }^{\mathrm{a}, \mathrm{b}, *}$, Sampsa Hautaniemi ${ }^{\mathrm{a}}$, Ilya Shmulevich ${ }^{\mathrm{c}}$, and Olli Yli-Harja ${ }^{\mathrm{a}}$<br>a Institute of Signal Processing, Tampere University of Technology, P.O. Box 553, FIN-33101<br>Tampere, Finland<br>b Cancer Genomics Laboratory, The University of Texas M. D. Anderson Cancer Center, Houston, TX 77030, USA<br>c Institute for Systems Biology, Seattle, WA 98103, USA


#### Abstract

A significant amount of attention has recently been focused on modeling of gene regulatory networks. Two frequently used large-scale modeling frameworks are Bayesian networks (BNs) and Boolean networks, the latter one being a special case of its recent stochastic extension, probabilistic Boolean networks (PBNs). PBN is a promising model class that generalizes the standard rule-based interactions of Boolean networks into the stochastic setting. Dynamic Bayesian networks (DBNs) is a general and versatile model class that is able to represent complex temporal stochastic processes and has also been proposed as a model for gene regulatory systems. In this paper, we concentrate on these two model classes and demonstrate that PBNs and a certain subclass of DBNs can represent the same joint probability distribution over their common variables. The major benefit of introducing the relationships between the models is that it opens up the possibility of applying the standard tools of DBNs to PBNs and vice versa. Hence, the standard learning tools of DBNs can be applied in the context of PBNs, and the inference methods give a natural way of handling the missing values in PBNs which are often present in gene expression measurements. Conversely, the tools for controlling the stationary behavior of the networks, tools for projecting networks onto sub-networks, and efficient learning schemes can be used for DBNs. In other words, the introduced relationships between the models extend the collection of analysis tools for both model classes.


## Keywords

Gene regulatory networks; Probabilistic Boolean networks; Dynamic Bayesian networks

## 1. Introduction

During recent years, it has become evident that cellular processes are executed in a highly parallel and integrated fashion and that computational modeling approaches can provide powerful methodologies for gaining deeper insight into the operation of living cells. The modeling problem that has received a considerable amount of attention is the discovery of

[^0]
[^0]:    *Corresponding author. Institute of Signal Processing, Tampere University of Technology, P.O. Box 553, FIN-33101 Tampere, Finland. Tel.: +358 33115 3859; fax: +358 33115 3817. E-mail addresses: harri.lahdesmaki@tut.fi (H. Lähdesmäki), sampsa.hautaniemi@tut.fi (S. Hautaniemi), is@ieee.org (I. Shmulevich), yliharja@cs.tut.fi (O. Yli-Harja)..

    5 For example, in Fig. 3, the PBN counterparts of $\operatorname{Po}(\bar{X} \int t)$ ) are $\left\{X_{i}(t-1), X_{j 1}(t-1), X_{j 2}(t-1), X_{k 1}(t-1), X_{k 2}(t-1)\right\}$.

transcriptional level interactions. With the help of recent development in high-throughput genomic technologies, computational methods have enormous potential in the context of model inference from real measurement data and in practical use, such as drug discovery.

A number of different frameworks for gene regulatory network modeling have been proposed, ranging from differential equations too qualitative models (for an overview, see e.g. [1]). There is a clear conceptual difference between differential equation and coarse-scale models. The former can be used for a detailed representation of biochemical reactions, whereas the latter emphasize fundamental, generic principles between interacting components. In this context, models classes that are both discrete-time and discrete-state are called coarse-scale models.

Fine-scale modeling of biological interactions at the molecular level may require some type of differential equations. Although differential equations have successfully been used to simulate small (known) biochemical pathways (see e.g. [2,3]), their use in large-scale (genome-wide) modeling has considerable limitations. First of all, those models are computationally very demanding. Therefore, when modeling regulatory networks with differential equations, the model selection problem is usually ignored and the underlying biological system is assumed to be known. Because the model selection is the most important computational tool for discovering new, unknown regulatory relationships from the measured data, researchers have considered alternative modeling approaches. Also, the available analysis tools for differential equations are much more restricted than the ones for the alternative model classes (see below).

So-called graphical models can overcome the above-mentioned modeling problems, and advanced analysis tools have been developed for them. The use of holistic, coarse-scale models is also supported by the fact that the currently available data is limited both in quality and the number of samples. That is, there is no advantage using models that are much more accurate than the available data. Another constraint to be kept in mind is that the modeling framework should also be selected on the basis of the preferred goals, i.e., to what kinds of questions are we seeking answers. The two most often used large-scale modeling frameworks are Boolean and Bayesian networks (BNs). Since the Boolean network is a special case of another commonly used model class, probabilistic Boolean networks (PBNs), we will consider PBNs instead of Boolean networks.

PBNs is a model class that has been recently introduced in the context of genetic network modeling [4]. PBN is a stochastic extension of the standard Boolean network that incorporates rule-based dependencies between variables but is also stochastic in nature. The PBN model has a strong biological motivation through the standard, often used Boolean network model, originally proposed by Kauffman [5,6]. The theory of PBNs as models of genetic regulatory networks has been developed further in several papers. In particular, there has been interest in the control of stationary behavior of the network by means of gene interventions/perturbations [7], modifications of the network structure [8], and external control [9]. Another recent paper [10] introduces mappings between PBNs, including projections, node adjunctions and resolution reductions, which at the same time preserve consistency with the original probabilistic structure. Further, learning methods for PBNs have been introduced in [11,12]. More efficient learning schemes, in terms of computational complexity, but with cost of decreased accuracy, have been studied in [13]. General learning concepts have also been introduced in [14], although not in the context of PBNs, but a related setting. Kim and coauthors also show that the Markovian gene regulatory network model ${ }^{\mathbf{1}}$ is biologically plausible $[15]$.

[^0]
[^0]:    ${ }^{1}$ The dynamics of PBNs can be studied using Markov chains.

Dynamic Bayesian networks (DBNs), also called dynamic probabilistic networks, are a general model class that is capable of representing complex temporal stochastic processes [16-18]. DBNs are also known to be able to capture several other often used modeling frameworks, such as hidden Markov models (and its variants) and Kalman filter models, as its special cases (see e.g. [18]). DBNs and their non-temporal versions, BNs, have successfully been used in different engineering problems, such as in speech recognition [19] and target tracking and identification [20]. Recently, BNs have also been used in modeling genetic regulation [17, 21-30].

In this study we concentrate on PBNs and DBNs, and introduce certain equivalences between them. The first part of this paper is devoted to showing that PBNs and a certain subclass of DBNs can represent the same joint probability distribution over their common variables. For that purpose, we introduce a way of conceptually expressing a PBN as a DBN and vice versa. We would like to note that because there are many PBNs that can represent the same conditional probabilities, the one-to-one connection between the two models is true only in terms of probabilistic behavior. The main motivation for introducing the relationships between the models is that it opens up the possibility of applying the advanced tools of these network models to both of them. In other words, the introduced relationships between the models extend the collection of analysis tools for both model classes. The most important consequences of the results are briefly summarized below.

From the DBN point of view, the tools for controlling the stationary behavior of PBNs, by means of interventions, structural modifications of the network, and optimal external control, become available for DBNs. To our knowledge, no such methods have been introduced in the context of DBNs thus far. The same applies to efficient learning schemes, as well as mappings between different networks, in particular, projections onto subnetworks, which at the same time preserve consistency with the original probabilistic structure.

From the PBN point of view, one can use the standard learning tools of DBNs. This is particularly useful because the learning of gene regulatory networks has turned out to be a difficult problem and, therefore, efficient and flexible tools, with a possibility to be able to combine different data sources, are needed. Furthermore, both exact and approximate inference tools give a natural way of handling the missing values in PBNs which are often present in gene expression measurements. Further discussion on the impacts of the relationships can be found in Section 6. Note that the presented results are applicable to all similar modeling approaches, not only for gene regulatory network modeling. Also note that although the relationships are presented in the binary setting, they can be generalized to finer models (more discretization levels) as well.

The paper is organized as follows. Section 2 covers the basics of both model classes and develops PBNs to the extent necessary for this paper. Sections 3 and 4 introduce the relationships between the two models while the benefits of the relationships are explained in Section 6. Section 7 is devoted to general discussion and further topics in learning gene regulatory networks.

# 2. Network models 

In the following, we focus on distributions over a set of discrete-valued random variables. To make a distinction between random variables and their particular values we use the following notation. Upper-case letters, such as $X, X_{1}, Y$, are used to denote random variables (and corresponding nodes in the graphs). Lower-case letters, such as $x, x_{1}, y$, are used to denote the values of the corresponding random variables. Vector-valued quantities are in boldface.

# 2.1. Probabilistic Boolean networks 

For consistency of notation, we will be using the same notation as in [4]. A PBN $G(V, F)$ is defined by a set of binary-valued nodes (genes) $V=\left\{X_{1}, \ldots, X_{n}\right\}$ and a list of function sets $F$ $=\left(F_{1}, \ldots, F_{n}\right)$, where each function set $F_{i}$ consists of $l(i)$ Boolean functions, i.e., $F_{i}=\left\{f_{1}^{(i)}, \ldots, f_{l(i)}^{(i)}\right\}$. The value of each node $X_{i}$ is updated by a Boolean function taken from the corresponding set $F_{i}$. A realization of the PBN at a given time instant is defined by a vector of Boolean functions. Assuming that there are $N$ possible realizations for the PBN, then there are $N$ vector functions $\mathbf{f}_{1}, \ldots, \mathbf{f}_{N}$ where each $f_{j}=\left(f_{j_{1}}^{(1)}, \ldots, f_{j_{n}}^{(n)}\right), 1 \leq j \leq N, 1 \leq j_{i} \leq l(i)$, and each $f_{j_{i}}^{(i)} \in F_{i}$. Each realization of the PBN maps (updates) the values of the nodes into their new values, i.e., $\mathbf{f}_{i}: \mathbb{R}^{n} \rightarrow \mathbb{R}^{n}$, where $\mathbb{R}_{i}=\{0,1\}$. Network realizations $\mathbf{f}_{1}, \ldots, \mathbf{f}_{N}$ constitute the possible values of a random variable whose outcome is selected independently for each updating step.

In order to make the discussion more explicit, we use the notion of time with the updating step of the network. That is, $X_{i}(t)(1 \leq i \leq n)$ is the discrete-time random variable (stochastic process) that denotes the attribute $X_{i}$ at time $t$, and $\mathbf{X}(t)=\left(X_{1}(t), \ldots, X_{n}(t)\right)$ is a vector of all random variables $X_{i}, 1 \leq i \leq n$, at time $t$. So, the updating step from time $t-1$ to $t$, given the current state of the nodes $\mathbf{x}(t-1)$ and a realization $\mathbf{f}_{j}$, is expressed as $\left(x_{1}(t), \ldots, x_{n}(t)\right)=\mathbf{f}_{j}\left(x_{1}(t-1), \ldots, x_{n}(t\right.$ $-1))$.

Let $F^{(i)}$ and $\mathbf{F}=\left(F^{(1)}, \ldots, F^{(n)}\right)$ denote random variables taking values in $F_{i}=\left\{f_{1}^{(i)}, \ldots, f_{l(i)}^{(i)}\right\}$ and $F_{1} \times \ldots \times F_{n}$, respectively. The probability that a certain predictor function $f_{j}^{(i)}$ is used to update the value of the node $X_{i}$ is equal to

$$
c_{j}^{(i)}=\operatorname{Pr}\left\{F^{(i)}=f_{j}^{(i)}\right\}=\sum_{f: F^{(i)}=f_{j}^{(i)}} \operatorname{Pr}\left\{F=f\right\}
$$

A PBN is said to be independent if the elements $F^{(1)}, \ldots, F^{(n)}$ of the random variable $\mathbf{F}$ are independent, i.e., $\operatorname{Pr}\{F=f\}=\prod_{i=1}^{n} \operatorname{Pr}\left\{F^{(i)}=f^{(i)}\right\}$. If the PBN is independent, its predictor functions $f_{j}^{(i)}, 1 \leq j \leq l(i)$, for all the nodes $X_{i}(1 \leq i \leq n)$, are associated with an independent selection probability $c_{j}^{(i)}$. A PBN is said to be dependent if the joint probability distribution of random variables $F^{(1)}, \ldots, F^{(n)}$ cannot be factored as for the independent PBN.
Correspondingly, the node $X_{i}$ in the PBN is said to be independent (resp. dependent) if its predictor function is (resp. is not) independent of the other predictor functions. It is also worth noting that the model $G(V, F)$ is not changing with time, i.e., it defines a homogeneous process. A basic building block of a PBN, which describes the updating mechanisms for a single node $X_{i}$, is shown in Fig. 1.

### 2.2. Time-series in PBNs

In the following, we are interested in the joint probability distribution of the variables expanded over a finite number of updating steps, say $T$ steps, i.e., $\{\mathbf{X}(i): 0 \leq i \leq T\}$. Given the initial state $\mathbf{x}(t-1)$, the probability of moving to some state $\mathbf{x}(t)$ after one step of the network is (see e.g. $[4])$

$$
A(\mathbf{x}(t-1), \mathbf{x}(t))=\sum_{j: f_{j} \times(t-1))=\mathbf{x}(t)} \operatorname{Pr}\{F=f\}
$$

Because the network realizations are selected independently for each time instant, the joint probability distribution over all possible time-series of length $T+1$ can be expressed as

$$
\begin{aligned}
& \operatorname{Pr}\{\boldsymbol{X}(0)=\boldsymbol{x}(0), \ldots, \boldsymbol{X}(T)=\boldsymbol{x}(T)\} \\
& =\operatorname{Pr}\{\boldsymbol{X}(0)=\boldsymbol{x}(0)\} \prod_{t=1}^{T} A(\boldsymbol{x}(t-1), \boldsymbol{x}(t))
\end{aligned}
$$

where $\operatorname{Pr}\{\mathbf{X}(0)=\mathbf{x}(0)\}$ denotes the distribution of the first state. Eq. (3) shows that dynamics of PBNs can also be modeled by Markov chains [4].

Let us concentrate on independent PBNs for now and rewrite the state transition probabilities $A(\mathbf{x}(t-1), \mathbf{x}(t))$. Let $(\mathbf{x}(t))_{i}, 1 \leq i \leq n$, denote the $i$ th element of $\mathbf{x}(t)$, and $A(\mathbf{x}(t-1),(\mathbf{x}(t))_{i})$ denote the probability that the $i$ th element of $\mathbf{x}(t)$ will be $(\mathbf{x}(t))_{i}$ after one step of the network, given that the current state is $\mathbf{x}(t-1)$. (A more detailed computation of probability $A(\mathbf{x}(t-1),(\mathbf{x}$ $(t))_{i}$ ) is shown in Eq. (12), which will be discussed later on.) Since all nodes are assumed to be independent, each node is updated independently, and Eq. (2) can be written as [15]

$$
A(\boldsymbol{x}(t-1), \boldsymbol{x}(t))=\prod_{i=1}^{D} A(\boldsymbol{x}(t-1),(\boldsymbol{x}(t))_{i})
$$

So, given Eqs. (3) and (4), the joint probability distribution over all possible time-series of length $T+1$ can be expressed as

$$
\begin{aligned}
& \operatorname{Pr}\{\boldsymbol{X}(0)=\boldsymbol{x}(0), \ldots, \boldsymbol{X}(T)=\boldsymbol{x}(T)\} \\
& =\operatorname{Pr}\{\boldsymbol{X}(0)=\boldsymbol{x}(0)\} \prod_{i=1}^{T} \prod_{i=1}^{D} A(\boldsymbol{x}(t-1),(\boldsymbol{x}(t))_{i})
\end{aligned}
$$

Let us now concentrate on a dependent PBN. Let a dependent PBN have $I$ independent nodes, $X_{i}, i=1, \ldots, I$, and $D$ sets of dependent but mutually exclusive nodes, $\mathbf{X}_{j}=\left(X_{j 1}, \ldots, X_{I d(j)}\right), j=$ $1, \ldots, D$. That is, $\left\{X_{i}\right\} \cap \mathbf{X}_{j}=\varnothing$; for all $i=1, \ldots, I, j=1, \ldots, D$, and $\mathbf{X}_{j} \cap \mathbf{X}_{k}=\varnothing$, for all $1 \leq j \neq k \leq D .{ }^{2}$ Further, $\cup_{i=1}^{I}\left\{X_{i}\right\} \cup \cup_{j=1}^{D} X_{j}=\left\{X_{1}, \ldots, X_{m}\right\}$. Without loss of generality, we assume that the genes are sorted and re-labeled such that the first $I$ nodes are the independent ones and the rest are dependent. The probability distribution of the network realization can be written as

$$
\begin{aligned}
& \operatorname{Pr}\{\boldsymbol{F}=\boldsymbol{f}\} \\
& =\prod_{i=1}^{I} \operatorname{Pr}\left\{F^{(i)}=f^{(i)}\right\} \\
& \times \prod_{j=1}^{D} \operatorname{Pr}\left\{F^{\left(j_{1}\right)}=f^{\left(j_{1}\right)}, \ldots, F^{\left(j_{d(j)}\right)}=f^{\left(j_{d(j)}\right)}\right\}
\end{aligned}
$$

Define $D_{j}=\left\{j_{1}, \ldots, j_{d(j)}\right\}$, and let $(\mathbf{x}(t))_{D_{j}}$ denote the elements $j_{1}, \ldots, j_{d(j)}$ of the vector $\mathbf{x}(t)$. Let $A(\mathbf{x}(t-1),(\mathbf{x}(t))_{D_{j}})$ denote the probability that the elements $j_{1}, \ldots, j_{d(j)}$ of $\mathbf{x}(t)$ are $(\mathbf{x}(t))_{D_{j}}$ after one step of the network, given that the current state is $\mathbf{x}(t-1)$. Without going into details, it is quite straightforward to see that the joint probability of a dependent PBN over all $T+1$ length time-series can be decomposed the same way as in Eq. (5) except that terms $A(\mathbf{x}(t-1),(\mathbf{x}$ $(t))_{i}$ ), which correspond to the independent nodes, must be replaced by terms $A(\mathbf{x}(t-1),(\mathbf{x}$ $(t))_{D_{j}}$ ). That is,

[^0]
[^0]:    ${ }^{2}$ Throughout this paper, symbol $\mathbf{X}$ is used for both (random) vector variables and sets of (random) variables so that notations such as $\mathbf{X}_{j} \cap \mathbf{X}_{k}$ make sense.

$$
\begin{aligned}
& \operatorname{Pr}\left\{\boldsymbol{X}(0)=\boldsymbol{x}(0), \ldots, \boldsymbol{X}(T)=\boldsymbol{x}(T)\right\} \\
& =\operatorname{Pr}\left\{\boldsymbol{X}(0)=\boldsymbol{x}(0) \mid \prod_{i=1}^{T} \prod_{t=1}^{I} A(\boldsymbol{x}(t-1),(\boldsymbol{x}(t))_{t}\right\} \\
& \times \prod_{j=1}^{D} A(\boldsymbol{x}(t-1),(\boldsymbol{x}(t))_{D})_{j}^{J}
\end{aligned}
$$

# 2.3. Dynamic Bayesian networks 

Definitions in this section follow mainly the notation used in [17]. Let $\mathbf{X}=\left\{X_{1}, \ldots, X_{n}\right\}$ denote the (binary-valued) random variables in the network and $\operatorname{Pr}\{\cdot\}$ denote the joint probability distribution of $\mathbf{X} .{ }^{3}$ A BN, also called a probabilistic network, for $X$ is a pair $B=(G, \Theta)$ that encodes the joint probability distribution over X . The first component, $G$, is a directed acyclic graph whose vertices correspond to the variables in $X$. The network structure, especially the lack of possible arcs in $G$, encodes a set of conditional independence properties about the variables in $\mathbf{X}$. The second component, $\Theta$, defines a set of local conditional probability distributions (or conditional probability tables (CPT)), induced by the graph structure $G$, associated with each variable. Let $\mathbf{P a}\left(X_{i}\right)$ denote the parents of the variable $X_{i}$ in the graph $G$ and $\mathbf{p a}\left(X_{i}\right)$ denote the value of the corresponding variables. Then, a BN $B$ defines a unique joint probability distribution over $\mathbf{X}$ given by

$$
\operatorname{Pr}\left\{x_{1}, \ldots, x_{n}\right\}=\prod_{i=1}^{n} \operatorname{Pr}\left\{x_{i} \mid \boldsymbol{p a}\left(X_{i}\right)\right\}
$$

For a detailed introduction to BNs, see, e.g., [31,32].
Temporal extension of BNs, DBNs, extend these concepts to stochastic processes. In this paper, we restrict our attention to first-order Markov processes in $\mathbf{X}$, i.e., to processes whose transition probability obeys $\operatorname{Pr}\{\mathbf{X}(t) \mid \mathbf{X}(0), \mathbf{X}(1), \ldots, \mathbf{X}(t-1)\}=\operatorname{Pr}\{\mathbf{X}(t) \mid \mathbf{X}(t-1)\}$. The transition probabilities are also assumed to be independent of $t$, meaning that the process is homogeneous, as is the case for PBNs.

A DBN that represents the joint probability distribution over all possible time-series of variables in $\mathbf{X}$ consists of two parts: (i) an initial $\mathrm{BN} B_{0}=\left(G_{0}, \Theta_{0}\right)$ that defines the joint distribution of the variables in $\mathbf{X}(0)$, and (ii) a transition $\mathrm{BN} B_{1}=\left(G_{1}, \Theta_{1}\right)$ that specifies the transition probabilities $\operatorname{Pr}\{\mathbf{X}(t) \mid \mathbf{X}(t-1)\}$ for all $t$. So, a DBN is defined by a pair $\left(B_{0}, B_{1}\right)$. In this paper we restrict the structure of DBNs in two ways. First, the directed acyclic graph $G_{0}$ in the initial $\mathrm{BN} B_{0}$ is assumed to have only within-slice connections, i.e., $\mathbf{P a}\left(X_{i}(0)\right) \subseteq \mathbf{X}(0)$ for all $1 \leq i \leq n$. We also constrain the variables in time slice $\mathbf{X}(t), t>0$, to have all their parents in slice $t-1$, i.e., $\mathbf{P a}\left(X_{i}(t)\right) \subseteq \mathbf{X}(t-1)$ for all $1 \leq i \leq n$ and $t>0$. The fact that connections exist only between consecutive slices is related to our first-order Markovian assumption stated earlier. An example of the basic building blocks of DBNs, $B_{0}$ and $B_{1}$, is shown in Fig. 2.

Using Eq. (8) and the assumptions on the initial and transition BNs discussed above, the joint distribution over a finite set of random variables $\mathbf{X}(0) \cup \mathbf{X}(1) \cup \ldots \cup \mathbf{X}(T)$ can be expressed as $[17]$

[^0]
[^0]:    ${ }^{3}$ In order to follow the standard notation we write $\operatorname{Pr}\{\mathbf{x}\}$ instead of $\operatorname{Pr}\{\mathbf{X}=\mathbf{x}\}$.

$$
\begin{aligned}
& \operatorname{Pr}\{\boldsymbol{x}(0), \boldsymbol{x}(1), \ldots, \boldsymbol{x}(T)\} \\
& =\operatorname{Pr}\{\boldsymbol{x}(0) \mid \prod_{t=1}^{T} \operatorname{Pr}\{\boldsymbol{x}(t) \mid \boldsymbol{x}(t-1)\} \\
& =\prod_{i=1}^{n} \operatorname{Pr}\left\{x_{j}(0) \mid \boldsymbol{p o}\left(X_{j}(0)\right)\right\} \\
& \times \prod_{t=1}^{T} \prod_{j=1}^{n} \operatorname{Pr}\left\{x_{j}(t) \mid \boldsymbol{p o}\left(X_{j}(t)\right)\right\}
\end{aligned}
$$

It may also be worth mentioning that we assume fully observable DBNs. That is, when used in a real application, the values of all nodes are observed. Hidden nodes are considered when extensions to PBNs are discussed in Section 5.

# 3. Relationships between independent PBNs and DBNs 

In order to be able to establish the relationship between PBNs and DBNs, we will add an extra feature to the definition of a PBN. We will assume that the initial state $\mathbf{X}(0)$ of a PBN can have any joint probability distribution. Indeed, that definition was already used in Eqs. (3), (5) and (7). In particular, we assume $\mathbf{X}(0)$ to have the same distribution as defined by $B_{0}$ for the first slice of a DBN. For instance, in the context of genetic regulatory network modeling this initial distribution can be set equal to the stationary distribution of the corresponding Markov chain. Also note that we are not discussing the general class of DBNs in the following but only the subclass of binary-valued DBNs, as discussed in the previous section. We relax the requirement of binary-valued nodes in Sections 4.1 and 4.2.

### 3.1. An independent PBN as a binary-valued DBN

We first illustrate a way of expressing an independent $\operatorname{PBN} G(V, F)$ as a $\operatorname{DBN}\left(B_{0}, B_{1}\right)$. Let an independent $\operatorname{PBN} G(V, F)$ be fixed. The nodes in the graphs $G_{0}$ and $G_{1}$ must clearly correspond to the nodes in the PBN. In order to distinguish between the nodes from different models, nodes in the PBN are denoted by $X_{i}, 1 \leq i \leq n$, as above, and the corresponding nodes in the DBN are denoted by $\hat{X}_{i}$ (similarly for the vector-valued random variables $\mathbf{X}$ and $\hat{\boldsymbol{X}}$ ). We refer to nodes $X_{i}$ and $\mathbf{X}$ as the PBN counterparts of $\hat{X}_{i}$ and $\hat{\boldsymbol{X}}$, respectively, and the other way around.

Because an initial $\mathrm{BN} B_{0}$ is capable of representing any joint probability distribution over its nodes [31,32], the distribution of the initial state of the $\operatorname{PBN}, \operatorname{Pr}\{\mathbf{X}(0)\}$, can be represented by $B_{0}$. We omit the technical details since they are quite straightforward.

From Eqs. (3) and (9) it is easy to see that both PBNs and DBNs obey the first-order Markovian property. Thus, we only need to consider one-step transition probabilities, say between time instants $t-1$ and $t, \operatorname{Pr}\{\mathbf{X}(t) \mid \mathbf{X}(t-1)\}$, when expressing the PBN as a DBN. Further, from Eqs. (5) and (9) one can see that, for both models, the joint probability can also be decomposed over their nodes in the same way. Thus, when constructing a transition $\mathrm{BN} B_{1}$, we can further concentrate only on a single node, say $X_{i}$, with other nodes being handled similarly. Let $\boldsymbol{X}_{j}^{(i)}(t-1) \subseteq \boldsymbol{X}(t-1)$ denote the set of essential variables (nodes) used by predictor function $t^{e}(i)$ for gene $X_{i}$ at time $t$. The set

$$
\boldsymbol{P o}\left(X_{j}(t)\right)=\bigcup_{j=1}^{t(i)} \boldsymbol{X}_{j}^{(j)}(t-1)
$$

denotes the set of all variables used to predict the value of the gene $X_{i}$. Let us expand the domain of all the predictor functions in $F_{i}$ by adding fictitious variables so that they are functions of variables in $\operatorname{Pa}\left(X_{i}(t)\right)$. Thus, we can define $B_{1}=\left(G_{1}, \Theta_{1}\right)$ as follows. The graph $G_{1}$ has directed

edges from $\hat{\boldsymbol{X}}(t-1)$ to $\hat{\boldsymbol{X}}(t)$ such that the parents of $\hat{X}_{j}(t)$ are equal to the DBN counterparts of the nodes shown in Eq. (10). As was already shown in [4], given the distribution $\mathscr{G}_{i}$ over the predictor variables of node $X_{i}$ (denoted as $\mathbf{P a}\left(X_{i}\right) \sim \mathscr{G}_{i}$ ), the probability of $X_{i}$ being one is

$$
\operatorname{Pr}\left\{X_{i}=1\right\}=\sum_{j=1}^{l(i)} c_{j}^{(i)} \sum_{\mathbf{x} \in\{0,1\}^{|\mathbf{P a}\left(X_{i}\right)\}}} \mathscr{D}_{i}(\mathbf{x}) f_{j}^{(i)}
$$

where the domain of predictor functions $f_{j}^{(i)}$ is assumed to be expanded and $f_{j}^{(i)}$ is treated as a real-valued function. We can interpret Eq. (11) as $\operatorname{Pr}\left\{X_{i}(t)=1 \mid \mathbf{P a}\left(X_{i}(t)\right) \sim \mathscr{G}_{i}\right\}$. Thus, by specifying $\mathscr{G}_{i}$ to be "deterministic" such that it corresponds to a particular predictor node configuration $\operatorname{Pa}\left(X_{i}(t)\right)=\mathbf{z}$, i.e., $\mathscr{G}_{i}(\mathbf{x})=1$ if $\mathbf{x}=\mathbf{z}$ and $\mathscr{G}_{i}(\mathbf{x})=0$ otherwise, we have that

$$
\operatorname{Pr}\left\{X_{i}(t)=1 \mid P a\left(X_{i}(t)\right)=\mathbf{z}\right\}=\sum_{j=1}^{l(i)} f_{j}^{(i)}(\mathbf{z}) c_{j}^{(i)}
$$

Then, the set of local conditional probability distributions, or CPTs, $\Theta_{1}$, induced by the graph structure $G_{1}$, has exactly the same entries as shown in Eq. (12) for each node. So, all terms in Eq. (5) can be represented by corresponding terms in Eq. (9). Thus, any PBN can be expressed as a binary DBN.

# 3.2. A binary-valued DBN as an independent PBN 

To establish the converse of the above conclusion, let us see how a binary-valued DBN $\left(B_{0}, B_{1}\right)$ can be represented as an independent $\operatorname{PBN} G(V, F)$. Let a $\operatorname{DBN}\left(B_{0}, B_{1}\right)$ be given. The set of nodes $V$ must clearly correspond to the nodes in the graphs $G_{0}$ and $G_{1}$, and the distribution of the first state $\mathbf{X}(0)$ in the PBN must be the same as for the DBN.

Following the same reasoning as in Section 3.1, we can again conclude that when constructing a PBN, one only needs to consider the predictor functions for a single node $X_{i}$ between consecutive time instants $t-1$ and $t$. Let us assume that the local conditional probability distributions in $\Theta_{1}$ are given in the form of CPTs, and the number of parents of the $i$ th node is denoted as $q=\left|P a\left(\hat{X}_{i}(t)\right)\right|$. Let us enumerate the entries in the CPTs that are assigned to the $i$ th node as triplets $\left(z_{l}, \mathbf{y}_{l}, p_{l}\right)$, where $z_{l} \in \mathbb{R}_{p}, \mathbf{y}_{l} \in \mathbb{R}_{p q}, p_{l}=\operatorname{Pr}\left\{\hat{X}_{i}(t)=z_{l} \mid P a\left(\hat{X}_{i}(t)\right)=\mathbf{y}_{l}\right\}$, and $1 \leq l \leq 2^{q+1}$. Let us also suppose that the triplets are enumerated such that the first $r=2^{q}$ triplets have $z_{l}=1$ and they are sorted in increasing order, i.e., $1 \leq k<l \leq r \Rightarrow p_{k} \leq p_{l}$. Let $\mathbf{y}_{l}=$ $y_{l_{1}} y_{l_{2}} \ldots y_{l_{q}}$ and interpret a sequence of symbols $\boldsymbol{x}_{l}=x_{l_{1}}^{y_{l_{1}}} x_{l_{2}}^{y_{l_{2}}} \ldots x_{l_{q}}^{y_{l_{q}}}$ as a conjunction, where $x_{l_{i}}^{y_{l_{i}}}=x_{l_{i}}$ if $y_{l_{i}}=1$ and $x_{l_{i}}^{y_{l_{i}}}=\pi l_{i}$ if $y_{l_{i}}=0$. The variables in the conjunction correspond to a set of specific variables, $\left\{X_{l_{1}}, \ldots, X_{l_{q}}\right\}$, in the PBN, i.e., they are PBN counterparts of $P a\left(\hat{X}_{i}(t)\right)$.

Then, for the $i$ th node in the PBN, the set of functions $F_{i}$ can be generated as follows: $F_{i}=\left\{f_{1}^{(i)}, \ldots, f_{r}^{(i)}, f_{r+1}^{(i)}\right\}$ where

$$
f_{l}^{(j)}=x_{l} \vee x_{l+1} \vee \ldots \vee x_{r} \text { for } 1 \leq l \leq r
$$

is a disjunction of conjunctions, $f_{r+1}^{(j)}$ is a zero function, i.e., $f_{r+1}^{(j)}(\boldsymbol{x}) \equiv 0$ for all $\mathbf{x} \in \mathbb{R}^{q}$, and $r=2^{q} .{ }^{4}$ The corresponding selection probabilities are set to $c_{1}^{(j)}=p_{1}, c_{l}^{(j)}=p_{l}-p_{l-1}$ for $2 \leq l \leq r$, and $c_{r+1}^{(j)}=1-p_{r}$. If some of the $c_{j}^{(j)}$ s happen to be zero, the corresponding functions $f_{j}^{(j)}$ can be removed from $F_{l}$. By applying Eq. (12), we can verify that the above construction really gives an equivalent PBN to the given DBN. Let us first compute the one step prediction probabilities for the cases where $X_{l}(t)=1$ and the parent nodes have value $\mathbf{y}_{l}$. One gets

$$
\begin{aligned}
& \operatorname{Pr}\left\{X_{l}(t)=1 \mid \operatorname{Pa}\left(X_{l}(t)\right)=y_{l}\right\} \\
& =\sum_{j=1}^{r+1} f_{j}^{(j)}\left(y_{l}\right) c_{j}^{(j)} \\
& =\sum_{j=1}^{l} f_{j}^{(j)}\left(y_{l}\right) c_{j}^{(j)} \\
& =p_{1}+\sum_{j=2}^{l}\left(p_{j}-p_{j-1}\right)=p_{l}
\end{aligned}
$$

where the second equality follows from the fact that only the first $l$ functions $f_{1}^{(j)}, \ldots, f_{l}^{(j)}$ contain the conjunction $\mathbf{x}_{l}$ (see Eq. (13)), i.e., $f_{j}^{(j)}\left(\boldsymbol{y}_{l}\right)=1$ only for $1 \leq j \leq l$. The probability of the corresponding complement event $\operatorname{Pr}\left\{X_{l}(t)=0 \mid \operatorname{Pa}\left(X_{l}(t)\right)=\mathrm{y}_{l}\right\}$ is clearly $1-p_{l}$. So, a binaryvalued DBN can be represented as an independent PBN. Thus, we can state the following theorem.

Theorem 1-Independent PBNs $G(V, F)$ and binary-valued DBNs $\left(B_{0}, B_{1}\right)$ whose initial and transition BNs $B_{0}$ and $B_{1}$ are assumed to have only within and between consecutive slice connections, respectively, can represent the same joint distribution over their common variables.

The methods introduced in Sections 3.1 and 3.2 provide the actual conversions between the two modeling frameworks.

It is important to note that the mapping from a binary DBN to an independent PBN is not unique. Instead, there are many PBNs that have the same probabilistic structure. This is best illustrated by a toy example (see also the example below). Assume that node $X_{1}$ is regulated by node $X_{2}$ and all the values in the CPT of the node $X_{1}$ are equal to 0.5 . Then the following two function sets have the same conditional probabilities: $F_{1}=\left\{f_{1}^{(1)}, f_{2}^{(1)}\right\}$, with $c_{1}^{(1)}=c_{2}^{(1)}=0.5$ and where the functions $f_{1}^{(1)}=0$ and $f_{2}^{(1)}=1$ are constant zero and unity functions, respectively, or $F_{1}=\left\{f_{1}^{(1)}, f_{2}^{(1)}\right\}$, with $c_{1}^{(1)}=c_{2}^{(1)}=0.5$ and where the functions $f_{1}^{(1)}=x_{2}$ and $f_{2}^{(1)}=x_{2}$ are the identity and the negation functions, respectively. In other words, two fundamentally different function sets can have the same probabilistic structure. In the case of many parent variables, this issue becomes more complicated. In practice, one may want to construct the predictor functions for each node in the PBN such that the predictor

[^0]
[^0]:    ${ }^{4}$ Note that $f_{1}^{(j)}$ is essentially the unity function. Also, some of the Boolean expressions in Eq. (13) can possibly be expressed in more compact form.

functions have as few variables as possible, or such that the number of predictor functions is minimized.

Let us first consider minimizing the number of variables in the predictor functions. The above construction method produces predictor functions with the maximal number of variables. In some cases, when the CPTs are "separable," one can construct predictor functions having less variables, but at the same time being consistent with the original conditional probabilities. For example, consider a case where node $X_{1}$ is regulated by a set of nodes $X_{2}, \ldots, X_{n}$. Assume that the first parent node $X_{2}$ has a forcing (canalizing) effect on the target node $X_{1}$ such that all the values in the CPT for which $X_{1}=1$ and $X_{2}=1$ are equal to 0.9 . Assume further (for simplicity) that all other values in the CPT for which $X_{1}=1$ (i.e., $X_{1}=1$ and $X_{2}=0$ ) are smaller than 0.9 , the largest of those being, say, 0.8 . Instead of blindly using the aforementioned algorithm for generating the predictor functions for $X_{1}$, it can be useful to take the special form of the CPT into account. Following the above algorithm the first functions can be constructed as explained. However, the effect of the forcing variable $X_{2}$ can be accounted for using only a single onevariable predictor function $f^{(1)}=x_{2}$ with $c^{(1)}=0.9-0.8=0.1$. Alternatively, if no singlevariable predictor functions can be constructed as explained above, then combinations of variables, starting with two variables, three variables, etc., can be considered. For example, if all the values in the CPT for which $X_{1}=1, X_{2}=1$ and $X_{3}=1$ are equal, then a single twovariable function can be defined as $f^{(1)}=x_{2} x_{3}$.

The above search for predictor variables was explained in terms of the original conditional probabilities (i.e., CPTs). Alternatively, one can try to optimize the obtained predictor functions somehow. That is, each function in $F_{i}$ should be expressed in some optimal form. The first thing to be considered is the removal of fictitious variables from the functions. That can possibly result in functions which have far fewer input variables. Yet another issue is to further optimize the actual expressions of the Boolean functions using methods such as QuineMcCluskey algorithm (see e.g. [33]), which minimizes the number of terms in the disjunctive normal form. The above discussion, however, does not provide any optimal method for the predictor function construction (apart from the optimal representation of the functions). An optimal method can be described in terms of the number of predictor functions which is described next.

In the worst case, the minimum number of predictor functions is determined by the number of different values in the CPT. The above construction method automatically selects that number of predictors (plus a possible constant zero function). In some special cases, the number of predictor functions can be reduced. Consider again the same triplets as above $\left(z_{l}, \boldsymbol{y}_{l}, p_{l}\right)$ for a single node $X_{i}$ and again focus on only those triplets for which $z_{l}=1$. This leaves us with a set of probability values $p_{1}, \ldots, p_{r}, r=2^{q}$. The general optimality criterion can be stated as follows. Find the smallest set of selection probabilities $\left\{c_{1}^{(i)}, \ldots, c_{m}^{(i)}\right\}$, where each $c_{j}^{(i)} \in[0,1]$ and $\sum_{j=1}^{m} c_{j}^{(i)}>1$, such that each $p_{l}, 1 \leq l \leq r$, can be written as

$$
p_{l}=\sum_{i} c_{l j}^{(i)}
$$

where $I_{l} \subseteq\{1, \ldots, m\}$. Let $J_{j}=\left\{l \mid j \in I_{l}\right\} \subseteq\{1, \ldots, 2^{q}\}$ be the set of indices of those $P_{l}$ for which $c_{j}^{(i)}$ is used in the sum in Eq. (15). Then the function set $F_{i}=\left\{f_{1}^{(i)}, \ldots, f_{m}^{(i)}\right\}$ is defined as

$$
f_{j}^{(i)}=\underset{l \in J_{j}}{v} x_{l}
$$

where $\mathbf{x}_{l}$ is as above. In the same manner as in Eq. (14), we can verify the correctness of the predictor functions and the corresponding selection probabilities

$$
\begin{aligned}
& \operatorname{Pr}\left\{X_{j}(t)=1 \mid P a\left(X_{j}(t)\right)=X_{j}\right\} \\
& =\sum_{j=1}^{m} r_{j}^{(j)}\left(x_{l}\right) c_{j}^{(j)}=\sum_{j \in r_{j}^{(j)}\left(x_{l}\right)=1} c_{j}^{(j)} \\
& =\sum_{j \in I \in J_{j}} c_{j}^{(j)}=\sum_{l} c_{j}^{(j)}=p_{l}
\end{aligned}
$$

because (the third equality) $r_{j}^{(j)}\left(x_{l}\right)=1$ only if the function $r_{j}^{(j)}$ contains the conjunction $\mathbf{x}_{l}$, i.e., $l \in J_{j}$. The second to last equality follows from the fact that $l \in J_{j} \Leftrightarrow j \in I_{l}$, and the last equality from Eq. (15). Note that the optimal function set can still be non-unique.

The obtained functions in $F_{i}$ can be modified further as explained above e.g. by removing the possible fictitious variables and by applying the Quine-McCluskey optimization algorithm. A computationally efficient algorithm for the search of the optimal function sets remains to be developed. Fortunately, the search problem is usually limited in the sense that each gene contains only few parent variables.

Theorem 1 says that the two model classes can represent the same probabilistic behavior. However, there are many statistically equivalent PBNs that correspond to a DBN. This means the PBN formalism is redundant from the probabilistic point of view. On the other hand, PBN formalism is richer from the functional point of view because it can explain the regulatory roles of different gene sets in more detail than the conditional probabilities in DBNs can do.

Example 2-This example illustrates the above conversions between PBNs and DBNs. Let us assume that we have the following independent PBN: $G=(V, F), V=\left\{X_{1}, X_{2}\right\}, F=\left(F_{1}, F_{2}\right)$, $F_{1}=\left\{r_{1}^{(1)}, r_{2}^{(1)}\right\}, \quad r_{1}^{(1)}=x_{1} \vee x_{2}, \quad r_{2}^{(1)}=x_{2}, \quad c_{1}^{(1)}=0.2, \quad c_{2}^{(1)}=0.8, \quad F_{2}=\left\{r_{1}^{(2)}, r_{2}^{(2)}\right\}, \quad r_{1}^{(2)}$

$$
=x_{1} \wedge x_{2}, \quad r_{2}^{(2)}=x_{1}, \quad c_{1}^{(2)}=0.6, \quad c_{2}^{(2)}=0.4
$$

which we would like express as a DBN. (We omit the definition of the joint probability distribution of the first slice $\mathbf{X}(0)$.) The sets of essential variables used by predictor functions $r_{1}^{(1)}$ and $r_{2}^{(1)}$ are $\boldsymbol{X}_{1}^{(1)}(t-1)=\left\{X_{1}(t-1), \quad X_{2}(t-1)\right\}$ and $\boldsymbol{X}_{2}^{(1)}(t-1)=\left\{X_{2}(t-1)\right\}$, respectively. Then, following Eq. (10), the parents of the node $\hat{X}_{1}$ are the DBN counterparts of $P a\left(X_{1}(t)\right)=U_{j=1}^{2} \quad X_{j}^{(1)}(t-1)=\left\{X_{1}(t-1), \quad X_{2}(t-1)\right\}$. In a similar manner, we obtain that $P a\left(\hat{X}_{2}(t)\right)=\left\{\hat{X}_{1}(t-1), \quad \hat{X}_{2}(t-1)\right\}$. For purposes of illustration, the truth tables of the functions $r_{1}^{(1)}$ and $r_{2}^{(1)}$, as well as $r_{1}^{(2)}$ and $r_{2}^{(2)}$, are shown in Table 1. Note that the domains of the functions $r_{2}^{(1)}$ and $r_{2}^{(2)}$ are expanded.

The local conditional probability distributions in the DBN can be obtained by using Eq. (12). For instance, the probability of $X_{1}(t)$ being one, given that $P a\left(\hat{X}_{1}(t)\right)=00$, is $\sum_{j=1}^{2} r_{j}^{(1)}(00) c_{j}^{(1)}=1 \times c_{1}^{(1)}+0 \times c_{2}^{(1)}=c_{1}^{(1)}=0.2$. The probability of the corresponding complement event is $\operatorname{Pr}\left\{\hat{X}_{1}(t)=0 \mid P a\left(\hat{X}_{1}(t)\right)=00\right\}=1-0.2=0.8$. Similar calculations apply to other cases. The local conditional probability distributions are tabulated in Table 2 which concludes the conversion of the given PBN into a DBN.

Let us now assume that we are given a DBN as follows. (We again omit the definition of the initial $\mathrm{BN} B_{0}$.) The transition $\mathrm{BN} B_{1}=\left\{G_{1}, \Theta_{1}\right\}$ is: $G_{1}=\left\{V_{1}, E_{1}\right\}$, with $V_{1}=\left\{\dot{X}_{1}, \dot{X}_{2}\right\}$ and $E_{1}=\left\{\left[\dot{X}_{1}(t-1), \dot{X}_{1}(t)\right],\left[\dot{X}_{1}(t-1), \dot{X}_{2}(t)\right],\left[\dot{X}_{2}(t-1), \dot{X}_{1}(t)\right],\left[\dot{X}_{2}(t-1), \dot{X}_{2}(t)\right]\right\}$. The CPTs for both nodes $\left(\Theta_{1}\right)$ are given in Table 2. Let us concentrate on the node $\dot{X}_{1}$ and enumerate the triplets ${ }_{1}\left(y_{l}, z_{l}, p_{l}\right), 1 \leq l \leq 8$, in increasing order as introduced above (see Table 3).

The function set $F_{1}$ contains functions
$f_{1}^{(1)}=x_{1} x_{2} \vee x_{1} x_{2} \vee x_{1} x_{2} \vee x_{1} x_{2}, \quad f_{2}^{(1)}=x_{1} x_{2} \vee x_{1} x_{2} \vee x_{1} x_{2}, \quad f_{3}^{(1)}=x_{1} x_{2} \vee x_{1} x_{2}, \quad f_{4}^{(1)}=x_{1} x_{2}$ and $f_{5}^{(1)}=0$, where the last one denotes the zero function. The corresponding selection probabilities are $c_{1}^{(1)}=p_{1}=0, c_{2}^{(1)}=p_{2}-p_{1}=0.2, c_{3}^{(1)}=p_{3}-p_{2}=0.8, c_{4}^{(1)}=p_{4}-p_{3}=0$ and $c_{5}^{(1)}=1-p_{4}=0$. Because $c_{1}^{(1)}=c_{4}^{(1)}=c_{5}^{(1)}=0$, the corresponding functions can be removed from $F_{1}$. Further, the remaining functions can be manipulated as $f_{2}^{(1)}=x_{1} x_{2} \vee x_{1} x_{2} \vee x_{1} x_{2}=x_{1} \vee x_{1} x_{2}=x_{1} \vee x_{2}$ and $f_{3}^{(1)}=x_{1} x_{2} \vee x_{1} x_{2}=x_{2}$, which directly correspond to the predictor functions shown in the beginning of this Example. Note that the selection probabilities are also the same. After similar operations for the second node one gets the following list of functions:
$f_{2}^{(2)}=x_{1} x_{2} \vee x_{1} x_{2} \vee x_{1} x_{2}=x_{1} \vee x_{1} x_{2}, f_{4}^{(2)}=x_{1} x_{2}$ and $f_{5}^{(2)}=0$, with the corresponding selection probabilities being $c_{2}^{(2)}=0.4, c_{4}^{(2)}=0.2$ and $c_{5}^{(2)}=0.4$. These functions do not directly correspond to the ones shown in the beginning of this Example. However, in light of Eq. (12), they are effectively the same because they define the same one-step element-wise prediction probabilities (see also the last column of Table 2).

Note that the number of predictor functions can be reduced for the second node. Using the optimal procedure explained above it is easy to see that, e.g., the following two functions suffice $F_{2}=\left\{f_{1}^{(2)}, f_{2}^{(2)}\right\}$, with $c_{1}^{(2)}=0.4$ and $c_{2}^{(2)}=0.2$, where $f_{1}^{(2)}=x_{1} \vee x_{2}$ and $f_{2}^{(2)}=x_{1} x_{2}$.

# 4. Relationships between dependent PBNs and DBNs 

This section shows the relationships between dependent PBNs and DBNs. The methods of expressing a dependent PBN as a DBN, and vice versa, are conceptually similar to the ones for independent PBNs.

### 4.1. A dependent PBN as a discrete-valued DBN

Let us concentrate on a dependent PBN and illustrate a way of expressing it as a DBN. Using the same notation as in Section 2.2, let the given dependent PBN have $I$ independent nodes, $X_{i}, i=1, \ldots, I$, and $D$ sets of dependent and mutually exclusive nodes, $\mathbf{X}_{j}=\left\{X_{j 1}, \ldots, X_{j_{i}(j)}\right\}, j$ $=1, \ldots, D$. Assuming that the genes are sorted and re-labeled as in Section 2.2, the probability distribution of the network realization can be written as in Eq. (6).

From now on, we relax the requirement of pure binary-valued nodes by allowing discretevalued nodes in DBNs. In the following the discrete-valued nodes are also thought of as binary vector-valued nodes (i.e., binary vector presentation of a discrete variable). In order to define an equivalent DBN to the given PBN, we start by defining its nodes. First, a DBN is assumed to have only $I+D$ nodes. Let the first $I$ nodes be binary-valued nodes as above, $\dot{X}_{i}, 1 \leq i \leq I$, and the remaining $D$ nodes be binary vector-valued, denoted as $\dot{\boldsymbol{X}}_{j}=\left(\dot{X}_{j_{1}}, \ldots, \dot{X}_{j_{d(j)}}\right), 1 \leq$ $j \leq D$, and $\dot{\mathbf{X}}_{j} \in \mathbb{R}(d i j)$. The scalar- and vector-valued nodes, $\dot{X}_{j}$ and $\dot{\boldsymbol{X}}_{i}$, correspond to the nodes $X_{i}$ and $X_{j 1}, \ldots, X_{j_{i}(j)}$ in the PBN, respectively (see Fig. 3). As before, nodes $X_{i}$ and $X_{j 1}$,

$\ldots, X_{i k}$ are called the PBN counterparts of $\hat{X}_{i}$ and $\hat{\boldsymbol{X}}_{i}$, respectively. (Similarly, $\hat{X}_{i}$ and $\hat{\boldsymbol{X}}_{i}$ are the DBN counterparts of $X_{i}$ and $\mathbf{X}_{i}$.) In vector form, the nodes in a DBN, when incorporating the notion of time, are $\hat{\boldsymbol{X}}(t)=\left(\hat{X}_{1}(t), \ldots, \hat{X}_{l}(t), \hat{\boldsymbol{X}}_{1}(t), \ldots, \hat{\boldsymbol{X}}_{l}(t)\right)$.

An initial BN $B_{0}$ can be defined as in Section 3.1, such that the nodes $\hat{X}_{i}(1 \leq i \leq I)$ and the elements of the nodes $\hat{\boldsymbol{X}}_{i}(1 \leq j \leq D)$ in the DBN have the same initial joint distribution as the variable $\mathbf{X}(0)$ in the given PBN. Technical details are again omitted.

Let us then construct the transition $\mathrm{BN} B_{1}=\left(G_{1}, \Theta_{1}\right)$. Following the same reasoning as in Section 3.1, the dependent PBN defines a first-order Markovian process in $\mathbf{X}(t)$ (see also Eq. (7)). Even though the given PBN is dependent, nodes of a DBN are constructed in such a way that their PBN counterparts are mutually independent (see Eq. (6)). Based on Eq. (7) and the above node construction, we can again concentrate on a single node in the DBN, between consecutive time steps $t-1$ and $t$, when constructing the transition $\mathrm{BN} B_{1}$.

The set $\operatorname{Pa}\left(X_{i}(t)\right)$ denotes the set of all variables used to predict the value of the gene $X_{i}$ at time $t$ (see Eq. (10)). Similarly, let $\operatorname{Pa}(\hat{X}_{i}(t))$ contain the DBN counterparts of the nodes in Pa $\left(X_{i}(t)\right)$ except that variables belonging into sets of dependent nodes $\mathbf{X}_{i}=\left(X_{j_{1}}, \ldots, X_{j_{d(j)}}\right)$, $1 \leq j \leq D$, are replaced by their corresponding DBN analogs $\hat{\boldsymbol{X}}_{i}$. For example, let us assume that some of the nodes (one or more) in $\operatorname{Pa}\left(X_{i}(t)\right)$ belong to the set of dependent nodes, say to the $j$ th $(1 \leq j \leq D)$ dependent set. Then, those nodes are replaced by $\hat{\boldsymbol{X}}_{i}$ in $\operatorname{Pa}(\hat{X}_{i}(t))$. The above parent sets are illustrated in Fig. 3, where, e.g., $\operatorname{Pa}\left(X_{i}(t)\right)=\left\{X_{i}(t-1), X_{j_{1}}(t-1)\right\}$ but $\operatorname{Pa}(\hat{X}_{i}(t))=\left\{\hat{X}_{i}(t-1), \hat{\boldsymbol{X}}_{i}(t-1)\right\}$ because $X_{j_{1}}$ is not independent.

Construction of the graph $G_{1}$, then, goes as follows. For nodes $\hat{X}_{i}, 1 \leq i \leq I$, the graph has directed edges from time slice $t-1$ to $t$ such that the parents of $\hat{X}_{i}(t)$ are equal to $\operatorname{Pa}(\hat{X}_{i}(t))$. For the grouped nodes $\hat{\boldsymbol{X}}_{i}, 1 \leq j \leq D$, the graph has directed edges such that the parents of $\hat{\boldsymbol{X}}_{i}(t)$ are

$$
\operatorname{Pa}(\hat{\boldsymbol{X}}_{i}(t))=\underset{i=j_{1}}{J_{i j_{i}} \mid} \operatorname{Pa}(\hat{\boldsymbol{X}}_{i}(t))
$$

where $\hat{X}_{i}, j_{1} \leq i \leq j_{d(j)}$, is an element of $\hat{\boldsymbol{X}}_{i}$. This is illustrated in Fig. 3, where, e.g., $\operatorname{Pa}(\hat{\boldsymbol{X}}_{i}(t))=\left\{\hat{X}_{i}(t-1), \hat{\boldsymbol{X}}_{i}(t-1), \hat{\boldsymbol{X}}_{k}(t-1)\right\}$. Let us again expand the domain of predictor functions in $F_{i}$ by adding fictitious variables. However, the new domain of the functions is not assumed to be $\operatorname{Pa}\left(X_{i}(t)\right)$ but, instead, it consists of the PBN counterparts of the nodes in $\operatorname{Pa}(\hat{X}_{i}(t))$. An example is again shown in Fig. 3. For example, even though $\operatorname{Pa}\left(X_{i}(t)\right)=\left\{X_{i}(t\right.$ $-1), X_{j_{1}}(t-1)\}$, the PBN counterparts of $\operatorname{Pa}(\hat{X}_{i}(t))$ are $\left\{X_{i}(t-1), X_{j_{1}}(t-1), X_{j_{2}}(t-1)\right\}$. It is easy to see that the local CPTs for the first $I$ nodes can be formed as shown in Eq. (12). Let us then define $D$ random vectors $\mathbf{F}_{j}=\left(F^{(j 1)}, \ldots, F^{(j_{d(j j)})}\right), 1 \leq j \leq D$, taking values in $F_{j_{1}} \times \ldots \times$ $F_{j_{d(j)}}$ and whose domains are expanded as discussed above. Thus, $\mathbf{F}_{j} \mid \mathbb{\square}_{s} \rightarrow \mathbb{\square}_{d(j)}$, where $s$ equals the number of nodes in the PBN counterparts of $\operatorname{Pa}(\hat{\boldsymbol{X}}_{i}(t)) .{ }^{5}$ Then, the CPT of the grouped node $\hat{\boldsymbol{X}}_{i}, 1 \leq j \leq D$, can be computed as

$$
\begin{aligned}
& \operatorname{Pr}\left\{\hat{\boldsymbol{X}}_{i}(t)=x \mid \operatorname{Pa}(\hat{\boldsymbol{X}}_{i}(t))=y\right\} \\
& =\sum_{i} f(\boldsymbol{f} \mid \boldsymbol{y})=x) \operatorname{Pr}\left\{\boldsymbol{F}_{j}=\boldsymbol{f}\right\}
\end{aligned}
$$

where $I(\cdot)$ is the indicator function and the sum is expanded over all possible realizations of $\mathbf{F}_{j}$. The probability distribution of $\mathbf{F}_{j}$, in turn, can be computed by "integrating out" the other functions (see Eq. (1)).

# 4.2. A discrete-valued DBN as a dependent PBN 

The final step is to show a way of expressing a discrete-valued $\operatorname{DBN}\left(B_{0}, B_{1}\right)$ as a $\operatorname{PBN} G(V$, $F)$. We again start by defining the nodes of a PBN. Discrete-valued nodes in the DBN are considered to have a binary representation. That is, let $\tilde{\boldsymbol{x}}_{i}$ (a node in DBN) have $b(i)$ bits in its binary representation in which case we can also write $\tilde{\mathbf{x}}_{i}=\left(\tilde{x}_{i_{1}}, \ldots, \tilde{x}_{i_{b(i)}}\right), \tilde{x}_{i j} \in \mathbb{R}, j=1$, $\ldots, b(i)$. For notational simplicity, we will assume in the following that the number of different values for each node is a power of two. In general, that does not need to be the case. For each node $\tilde{\boldsymbol{x}}_{i}$ in the DBN, the corresponding PBN has a set of $b(i)$ mutually dependent nodes. So, in total, the constructed PBN has $\sum_{i=1}^{n} b(i)$ nodes, where $n$ equals the number of nodes in the given DBN.

The initial distribution of the PBN must be able to represent the same distribution as the first state of the given DBN. When the states of the DBN are considered via their binary representation it is clear, by the assumption stated in the beginning of Section 3, that the previous condition holds.

The joint probability distribution over the variables in the given discrete-valued DBN can be decomposed exactly the same way as shown in Eq. (9). Thus, the process is first order Markovian and we only need to consider the one step prediction probabilities, say from time $t-1$ to time $t$. We cannot, however, define the predictor functions for each node in PBN independently. Fortunately, it suffices to consider the set of $b(i)$ dependent nodes at a time.

Let us then construct the predictor functions for a PBN. Binary nodes in the DBN are not interesting since for those nodes we can use practically the same method as in Section 3.2. The only exception is that some parent nodes (in the DBN) may be non-binary. In that case, all the nodes in the PBN which correspond to a non-binary node in the DBN are used to predict the value of that gene. So, assume that we are considering a node $\tilde{\boldsymbol{x}}_{i}$ which has $b>1$ bits in its binary representation. (The index $i$ will be omitted from $b$ since we concentrate on a single node $\tilde{\boldsymbol{x}}_{i}$ at a time.) Let the corresponding nodes in the PBN be $\left\{X_{i_{1}}, \ldots, X_{i_{b}}\right\}$. The parents of the node $\tilde{\mathbf{x}}_{i}, \operatorname{Pa}\left(\tilde{\boldsymbol{x}}_{i}(t)\right)$, are assumed to have $q$ bits in total. Input variables of the predictor functions for the nodes $\left\{X_{i_{1}}, \ldots, X_{i_{b}}\right\}$ are required to be the PBN counterparts of $\operatorname{Pa}\left(\tilde{\boldsymbol{x}}_{i}(t)\right)$. Further, all those predictor functions are mutually dependent.

Let the CPTs in $\Theta_{1}$ for the node $\tilde{\mathbf{x}}_{i}$ be given: $\operatorname{Pr}\left\{\tilde{\boldsymbol{x}}_{i}(t)=\boldsymbol{z} \mid \operatorname{Pa}\left(\tilde{\boldsymbol{x}}_{i}(t)\right)=\boldsymbol{y}\right\}$ for all $\mathbf{z} \in \mathbb{R}^{b}$, $\mathbf{y} \in \mathbb{R}^{q}$. Assume that they are organized in $2^{q}$ lists, each containing $2^{b}$ entries (triplets): $L_{l}=$ $\left(\left(\mathbf{z}_{l, 1}, \mathbf{y}_{l}, p_{l, 1}\right), \ldots,\left(\mathbf{z}_{l, 2^{b}}, \mathbf{y}_{l}, p_{l, 2^{b}}\right)\right)$ where $\mathbf{z}_{l, r} \in \mathbb{R}^{b} \mathbf{y}_{l} \in \mathbb{R}^{q}$ and $p_{l, r}=\operatorname{Pr}\left\{\tilde{\boldsymbol{x}}_{i}(t)=\boldsymbol{z}_{l, r} \mid \operatorname{Pa}\left(\tilde{\boldsymbol{x}}_{i}(t)\right)=\boldsymbol{y}_{l}\right\}, r=1, \ldots, 2^{b}, l=1, \ldots, 2^{q}$. So, each list shows the elements of the CPT for a single parent (input) node configuration $\mathbf{y}_{l}$. Thus, the probabilities in each list must sum up to unity, i.e., $\sum_{i=1}^{2^{b}} p_{l, i}=1$, for all $l=1, \ldots, 2^{q}$. For simplicity, let us assume that entries $\left(\mathbf{z}_{l, r}, \mathbf{y}_{l}, p_{l, r}\right)$ for which $p_{l, r}=0$ are removed from all lists. We now show a constructive algorithm that generates vector-valued random predictor functions $\mathbf{F}_{i}: \mathbb{R}^{q} \rightarrow$ $\mathbb{R}^{b}$ for a set of dependent nodes in a PBN. Eventually, however, we will end up with a "normal" dependent PBN with standard Boolean functions for each node. In order to do so, we still

introduce an additional set of $2^{q}$ indices (pointers) $s_{i}^{(k)} \in\left\{1, \ldots, 2^{k}\right\}, i=1, \ldots, 2^{q}$. Index $s_{i}^{(k)}$ is used to index (point) an element in the $i$ th list, and $k$ is an iteration index. A constructive algorithm, for a single node in the DBN is shown in Fig. 4.

In step 2, Eq. (17), we essentially define a function $\mathbf{f}_{k}: \mathbb{R}_{2^{q}} \rightarrow \mathbb{R}_{2^{k}}$ because $\mathbf{y}_{l}$ s are different for all lists $l=1, \ldots, 2^{q}$. That is, the output value of $\mathbf{f}_{k}$ is defined for all possible inputs. It is also important to note that in step 3, Eq. (18), we could have used $\left.\begin{array}{l}p_{l, s_{l}^{(k)}:}=p_{l, s_{l}^{(k)}}-\operatorname{Pr}\left\{\boldsymbol{F}_{l}=\boldsymbol{f}_{k}\right\} \text { as well because if } p_{l, s_{l}^{(k)}}=\operatorname{Pr}\left\{\boldsymbol{F}_{l}=\boldsymbol{f}_{k}\right\}, \text { then } \\ p_{l, s_{l}^{(k)}}-\operatorname{Pr}\left\{\boldsymbol{F}_{l}=\boldsymbol{f}_{k}\right\}=\operatorname{Pr}\left\{\boldsymbol{F}_{l}=\boldsymbol{f}_{k}\right\}-\operatorname{Pr}\left\{\boldsymbol{F}_{l}=\boldsymbol{f}_{k}\right\}=0 .\end{array}\right.$ During each iteration we "subtract a probability mass" $\operatorname{Pr}\left\{\mathbf{F}_{i}=\mathbf{f}_{k}\right\}$ from all lists (distributions). So, after each iteration $0 \leq \sum_{i=1}^{2^{k}} p_{1, i}=\cdots=\sum_{i=1}^{2^{k}} p_{2^{q}, i} \leq 1$ holds. This ensures that the condition in step 4 is meaningful and becomes valid such that all the sums $\sum_{i=1}^{2^{k}} p_{l, i}, 1 \leq l \leq 2^{q}$, become equal to zero at the same time. Also, during each iteration, probability $p_{l, s_{l}^{(k)}}$ is set to zero and the index $s_{l}^{(k)}$ is incremented at least for one index $l=1, \ldots, 2^{q}$. So, the criterion in step 4 is reached in at most after $2^{q} \times 2^{b}$ iterations.

In order to see that the above procedure really constructs an equivalent PBN for the given DBN, consider one entry in the CPT of the given DBN, say $\operatorname{Pr}\left\{\hat{\boldsymbol{X}}_{l}(t)=\boldsymbol{z}_{l, r} \mid \boldsymbol{P a}\left(\hat{\boldsymbol{X}}_{l}(t)\right)=\boldsymbol{y}_{l}\right\}$. The above construction procedure generates a set of functions $\left\{\mathbf{f}_{1}, \ldots, \mathbf{f}_{j}\right\}$, with $2^{b} \leq j \leq 2^{q} \times 2^{b}$. It is easy to see that the sum of the selection probabilities of those functions for which $\mathbf{f}\left(\mathbf{y}_{l}\right)=\mathbf{z}_{l, r}$ is the probability $p_{l, r}=\operatorname{Pr}\left\{\hat{\boldsymbol{X}}_{l}(t)=\boldsymbol{z}_{l, r} \mid \boldsymbol{P a}\left(\hat{\boldsymbol{X}}_{l}(t)\right)=\boldsymbol{y}_{l}\right\}$. Thus, the same conditional probabilities are preserved. So, by applying the same construction method to all nodes in the DBN, one can see that all terms of Eq. (9) can be represented by the corresponding terms in Eq. (7).

To formalize the constructed PBN in the same manner as introduced in Section 2.1, one needs to define the predictor functions for each node separately. Given the vector-valued predictor functions $\left\{\mathbf{f}_{1}, \ldots, \mathbf{f}_{j}\right\}, 2^{b} \leq j \leq 2^{q} \times 2^{b}$, then, for each node $X_{i_{k}}, 1 \leq k \leq b$, one needs to "extract" all possible Boolean functions appearing as the $k$ th element in the vector-valued functions. The probabilities of occurrence remain the same as set by the constructive method.

Thus, since any discrete-valued DBN can be represented as a dependent PBN, we can state the following theorem.

Theorem 3-Dependent PBNs $G(V, F)$ and discrete-valued DBNs $\left(B_{0}, B_{1}\right)$ whose initial and transition BNs $B_{0}$ and $B_{1}$ are assumed to have only within and between consecutive slice connections, respectively, can represent the same joint distribution over their corresponding variables.

The methods introduced in Sections 4.1 and 4.2 provide the actual conversions between the two modeling frameworks.

Example 4-We illustrate the operation of the above constructive procedure with a simple example. We apply it only to a single node, $\hat{\boldsymbol{X}}_{i}=\left(\hat{X}_{i_{1}}, \hat{X}_{i_{2}}\right)$ whose parents are

$\hat{\chi}_{p}=\left\{\hat{x}_{p_{1}}, \hat{x}_{p_{2}}\right\}$. Thus, both nodes are quaternary, i.e., $b=q=2$. Further, let the CPT for that node be given as in Table 4.

So, now each column in the table corresponds to a list $L_{i}, 1 \leq i \leq 4$. In each list (column), the outputs, z , are in the same order for simplicity even though that does not need to be the case. So, when step 2 is applied for the first time, we define a function $\mathbf{f}_{1}: 00 \mapsto 00,01 \mapsto 00$, $10 \mapsto 00,11 \mapsto 00$ with the selection probability $\operatorname{Pr}\left\{\mathbf{F}_{i}=\mathbf{f}_{1}\right\}=0.1$. Note that, for each input (column), we pick the first non-zero element. Selected elements are shown in bold-face in Table 4 and the selection probability is the minimum of the selected elements. After step 3, the lists will be updated as shown in Table 5. During the second iteration one gets another vectorvalued function (see Table 5) $\mathbf{f}_{2}: 00 \mapsto 01,01 \mapsto 00,10 \mapsto 01,11 \mapsto 00$, and the corresponding selection probability is $\operatorname{Pr}\left\{\mathbf{F}_{i}=\mathbf{f}_{2}\right\}=0: 1$. The lists will again be updated as shown in Table 6. In a similar manner we obtain the third function $\mathbf{f}_{3}: 00 \mapsto 01,01 \mapsto 01,10 \mapsto 01,11 \mapsto 01$, with the selection probability $\operatorname{Pr}\left\{\mathbf{F}_{i}=\mathbf{f}_{1}\right\}=0: 2$. The lists are updated as shown in Table 7. The remaining iterations are similar (not shown). Note that the sums of probabilities in each list (column) are the same within each iteration.

The above procedure is not guaranteed to produce optimal sets of vector-valued functions. As in the case of independent networks, one can, e.g., minimize the number of functions. To set the stage, consider again the lists $L_{l}, 1 \leq l \leq 2^{q}$ for a single node $X_{i}$. The goal is to find the smallest set of vector-valued functions $\mathbf{F}_{i}=\left\{\mathbf{f}_{1}, \ldots, \mathbf{f}_{m}\right\}$ together with their selection probabilities $\operatorname{Pr}$ $\left\{\mathbf{F}_{i}=\mathbf{f}_{j}\right\} \in[0,1]$ whose sum is equal to one, such that each $p_{l, r}$ can be written as

$$
p_{l, r}=\sum_{i \in I_{l, r}} \operatorname{Pr}\left\{F_{i}=F_{i}\right\}
$$

where $\boldsymbol{I}_{l, r} \subseteq\{1, \ldots, m\}$, with the constraint that $j \in \boldsymbol{I}_{l, r} \Leftrightarrow j \notin \boldsymbol{I}_{l, s}, s \neq r(j=1, \ldots, m$ and $r=$ $1, \ldots, 2^{h}$ ), for all $l$. The extra constraint essentially says that each individual function $\mathbf{f}_{j}$ is deterministic, i.e, each input $\mathbf{y}_{l}$ is mapped to a single output $\mathbf{z}_{l, r}$. Let $\boldsymbol{J}_{j}=\left\{(l, r) \mid j \in \boldsymbol{I}_{l, r}\right\}$, then the actual vector functions are defined as

$$
\boldsymbol{f}_{j}: \boldsymbol{y}_{l} \mapsto \mathbf{z}_{l, r} \forall(l, r) \in \mathcal{J}_{j}
$$

and their validity can be checked as shown in Eq. (16). Efficient algorithms for the construction of the optimal vector-valued functions remain to developed.

# 5. Extensions of PBNs 

The PBN model was further developed in [7] by introducing node perturbations. In the context of gene regulatory network modeling, the perturbations can capture various random or unknown factors, such as environmental conditions, that can possibly affect the expression value of a gene.

From a mathematical point of view, node perturbation can be defined in a variety of ways, but let us use the definition from [7]. At every time step of the network, we have a so-called perturbation vector $\gamma \in \Pi$. The value of the $i$ th node in the network is flipped if the corresponding element of $\gamma$ is one. We will be assuming the perturbation vector to be independent and identically distributed (i.i.d.) for simplicity, even though this is not necessary in general. Let the probability of a single node perturbation be $\operatorname{Pr}\left\{\gamma_{i}=1\right\}=p$ for all $i$, where $\gamma_{i}$ denotes the $i$ th element of $\gamma$. Let the random perturbation process also be homogeneous. Then, given the current state $\mathbf{x}(t-1)$ of the network and a network realization $\mathbf{f}_{j}, 1 \leq j \leq N$, the updating step of the network is

where $\oplus$ denotes addition modulo 2 and $(1-p)^{n}$ is the probability of no perturbation occurring. That is, if no nodes are perturbed, the standard network transition function is used as explained in Section 2.1, while in the case of random node perturbations, the next state is determined by the previous state and the perturbation vector. An alternative definition would allow the unperturbed nodes to transition according to the (random) network function and only the perturbed nodes to be flipped.

Another extension to PBNs was introduced in [34] by defining an additional binary random variable $\delta$ which controls the random network changes. If $\delta=1$, then the network realization is randomly selected for the next time step as discussed in Section 2. Otherwise $(\delta=0)$ the previously used network function is used. The network change variable is assumed to homogeneous with $\operatorname{Pr}\{\delta=1\}=q$. With this extension the state of a PBN consists of the actual variables $\mathbf{X}$ as well as the network function $\mathbf{F}$.

Effectively the same model can also be defined in the DBN context. Let us concentrate on independent PBNs for simplicity. The basis of the model is the same as illustrated in Section 3.1. The effects of perturbations and random network changes can be captured by adding additional hidden nodes $\gamma(t), \mathbf{F}(t)$ and $\delta(t)$, see Fig. 5.

Concerning the node perturbations, the hidden variable $\gamma(t)$ is assumed to have $n$-dimensional independent Bernoulli distribution with common probability $p$. The perturbation node $\gamma(t)$ is also added into the set of parent nodes of $\dot{X}_{i}(t)$, i.e., $\gamma(t) \in \operatorname{Pa}\left(\dot{X}_{i}(t)\right)$ for all $i$ and $t \geq 0$. The local CPTs of the nodes $\dot{X}_{i}(t)$ are the same as in Section 3.1, except with the following adaptation: for the parent node configurations where $\gamma(t)=(00 \ldots 0)$ the CPTs remain unchanged and only depend on the value of $\operatorname{Pa}\left(\dot{X}_{i}(t)\right)$, and for the remaining parent node configurations (where $\gamma(t) \neq(00 \ldots 0)$, regardless of the value of $\operatorname{Pa}\left(\dot{X}_{i}(t)\right)$ ) the value of the node is $x_{i}(t)=x_{i}(t-1) \oplus \gamma_{i}(t)$ with probability one. Also note that $\dot{X}_{i}(t-1)$ must belong to $\operatorname{Pa}\left(\dot{X}_{i}(t)\right)$ for all $1 \leq i \leq n$.

The random network changes can be accounted for using the additional hidden variables $\mathbf{F}(t)$ and $\delta(t)$. The network change variable $\delta(t)$ is Bernoulli with parameter $q$. The value of the network function $\mathbf{F}(t)$ depends directly on the value of $\mathbf{F}(t-1)$ and $\delta(t)$, i.e., $\operatorname{Pa}(\mathbf{F}(t))=\{\mathbf{F}(t-$ 1), $\delta(t)\}$. If $\delta(t)=0$, then $\mathbf{f}(t)=\mathbf{f}(t-1)$. Otherwise a new network function is selected according to its selection probability. In the DBN formalism, the parents of the actual state variable, $\operatorname{Pa}\left(\dot{X}_{i}(t)\right)$, include not only its parent variables as defined in Section 3.1 but also the hidden network function variable, i.e., $\boldsymbol{F}(t-1) \in \operatorname{Pa}\left(\dot{X}_{i}(t)\right)$. Given the value of the parent variables, the CPTs of the actual state variables $\dot{X}_{i}(t)$ are degenerate since each network function operates deterministically. In the case of random network changes, the effects of node perturbations can be handled as explained above.

# 6. Benefits of relationships between PBNs and DBNs 

As already discussed in Section 1, having shown the connection between PBNs and DBNs (Theorems 1 and 3), it immediately opens up the possibility of applying the advanced tools of PBNs to DBNs and vice versa. Let us give a more detailed description of the tools that become available for DBNs and PBNs in Sections 6.1 and 6.2, respectively.

# 6.1. Benefits for DBNs 

Relationships between PBNs and DBNs make the following tools, among others, available in the context of DBNs as well. The tools originally developed for PBNs can be applied in the context DBNs, e.g., by using the detailed conversion of a DBN to a PBN. Alternatively, knowing the detailed mapping of a DBN to a PBN and that the two models can capture the same probabilistic behavior, it is possible to tailor each PBN method to be used directly in the DBN framework. The details of these tailored methods are not provided here.

In the context of genetic regulatory networks, one may want to elicit certain long-run behavior from the network. For example, a certain set of states can be deemed "undesirable" and one may wish for the network to transition into a "desirable" set of states. For example, in terms of cancer therapeutics, one may want to reach the set of states representing apoptosis in order to suppress the growth of cancer cells, which may keep proliferating.

The problem of controlling the stationary behavior of the dynamic network model has recently been addressed in several papers. Shmulevich et al. [7] considered the control by means of gene interventions. As the intervention is typically only transient, it does not affect the steadystate distribution. Thus, one may want to achieve the desired behavior as quickly as possible. For computational reasons, the control should also be achieved by intervening with as few genes as possible. A control method using the first-passage times of Markov chains was used in [7]. A related approach was taken in [8] where the control was formulated in terms of (permanently) modifying the network structure. That is, given the set of undesirable and desirable states and the original stationary distribution of the network, the goal is to find the best alteration of some preselected number of Boolean predictor functions such that a desired effect in the resulting stationary distribution is obtained. Yet another approach to control the stationary behavior, under the assumption of external variables, was introduced in [9]. Datta et al. based their approach on the theory of controlled Markov chains and used dynamic programming to find the optimal sequence of control actions that minimize a performance index over a finite time horizon. To our knowledge, no methods for controlling the stationary behavior of DBNs have been introduced so far. Therefore, the aforementioned methods can be of great value for the applications of DBNs.

Owing to the large number of variables in full genetic regulatory networks, it is often necessary to constrain one's approach to sufficiently small sub-networks. Therefore, network projections onto sub-networks are of particular interest. Dougherty and Shmulevich considered mappings between PBNs, such as projections, node adjunctions and resolution reductions, while at the same time preserving consistency with the original probabilistic structure [10].

Learning of PBN models has been considered e.g. in [11-13,15]. A promising approach to network learning was taken in [12]. In order to limit the search space, a novel clustering-based approach to finding sets of possible predictor genes for each gene was used. Further, a reversible jump Markov chain Monte Carlo method together with the coefficient of determination were used to compute the model order and parameters. Computationally more efficient learning schemes, although with the cost of decreased accuracy, were studied in [13]. From the DBN point of view, this can be viewed as an approximate learning method.

It is also worth noting that the constructed predictor functions can provide more compact presentation of the CPTs in DBNs. For example, instead of storing the whole CPT consisting of $2^{q+1}$ real numbers one can represent the conditional probabilities using PBNs. Assuming only $m$ predictor functions are required to represent a CPT, then only $m 2^{q}$-length binary vectors (assuming truth table format for the Boolean functions) together with $m$ real number (selection probabilities) are needed.

# 6.2. Benefits for PBNs 

Having shown the relationships between PBNs and DBNs (Theorems 1 and 3), the following tools from the context of DBNs can be used for PBNs as well. As introduced in the benefits for DBNs section, the DBN tools can be applied to PBNs by using the detailed mapping of a PBN to a DBN. Alternatively, the methods originally developed for DBNs can be tailored, with the help of the detailed conversions between the two model classes, to be used directly in the PBN context.

Gene expression measurements are often corrupted by missing data values. If it so happens that the missing components are of particular relevance, one may want to compute the posterior probability of the hidden nodes, given the incomplete measurements. In order to compute that, one can use exact inference methods [35] in the context of BNs, or approximate inference methods [36] if the exact solution is intractable.

Learning of gene regulatory networks from data has turned out to be a difficult problem and, therefore, efficient and flexible tools are needed. From a theoretical point of view, optimal learning of graphical models from data is a difficult problem-the optimal learning of BN structure using a Bayesian metric, BDe score, was shown to be an NP-complete problem [37], and the temporal dimension of DBNs does not make the problem any easier. In principle, learning of graphical models can be divided into two groups, model selection and parameter estimation, the former step generally being considerably harder than the latter. As is apparent based on the relationships between PBNs and DBNs, the same division can also be used when learning PBNs. Now, the model selection step corresponds to the selection of variables for each Boolean predictor function, whereas the parameter estimation step is related to the selection of the optimal Boolean predictor functions along with their selection probabilities.

Learning of DBNs has been a topic of several studies. A good introduction to learning of (nontemporal) BNs can be found in [38,39]. Learning of DBNs has been studied, e.g., in [17,40]. More efficient inference methods based on estimating local properties (Markov blanket) of the underlying graph have also been introduced [41,42].

In the fully observable case, learning the network structure should not be overly complicated at least for small indegree, which is the maximum number of parents of each node. However, computational and theoretical problems may arise in the case of incomplete data, which is quite common in the context of gene expression measurements. Also, unknown control/regulatory factors not taken into account in the network model can be considered as hidden variables. The expectation-maximization (EM) algorithm is a standard tool for tackling the problems caused by missing data [17,43]. A more efficient structural EM (SEM) algorithm has been introduced for learning BNs (see, for instance, [17]). However, as the EM is an optimization routine, computational costs increase and there is no guarantee for the global maxima.

Data used in the gene regulatory network learning are usually both expensive and difficult to collect. Therefore, one should carefully design the experiments in order to gain maximal advantage. The use of active learning can remarkably reduce the number of observations required to learn the model by choosing data instances whose expected decrease in the uncertainty in the model learned so far is the greatest. Greedy active learning methods for BNs have recently been introduced in [44-46].

As a summary, a number of advanced methods have been developed for learning DBNs. Since PBNs and DBNs can capture the same probabilistic behavior, a straightforward way of using the DBN learning methods in the context of PBNs is as follows: learn a DBN from a given data set, e.g. by maximizing the posterior probability, and then convert it to a PBN using the

methods introduced above. However, special care must be taken in the conversion of a DBN to a PBN due to the one-to-many nature (non-uniqueness) of this transformation.

# 7. Discussion 

The subclass of DBNs used in this study, even though not necessarily binary-valued, is by far the most commonly used DBN model class in the context of modeling dynamic gene regulatory networks. In particular, often only between-slice connections are used since that fits well in the modeling of cause-effect behavior. However, independent PBNs cannot cope with dependent effects (or nearly instantaneous interactions) between variables. The same applies to the binary-valued DBNs as well. This issue can be handled using dependent PBNs or discrete-valued (i.e., binary vector-valued) DBNs. Indeed, the discrete-valued DBNs can be viewed as binary DBNs where some individual binary variables (within slice) are clustered together, hence forming binary vector-valued variables. Since the binary vector-valued nodes can have any local conditional distributions, the individual elements of a binary vector variable can have any joint effects. The same applies to dependent PBNs due to the correspondence between the models.

In the context of learning genetic regulatory networks, the main focus so far has been on the use of gene expression data only. In the context of PBNs, several papers have been published on learning the network structure e.g. [12-15] most of which use the so-called coefficient of determination (CoD) principle [47]. Learning methods for DBNs, in the context of genetic networks, have been studied in [17,21,22,24,25,27,29]. Note, however, that some of the DBN studies have concentrated on non-temporal BNs. A problem of non-dynamic model inference is that one generally loses the causal direction of regulatory effects. This can be circumvented by using perturbations, such as gene over-expression and knock-outs [28,30].

As the DBN is a versatile model class, different information sources can be used, in a principled way, in the model inference. Recently, the use of so-called location data [48], measuring the protein-DNA interactions, was introduced in the framework of BNs [23], and with more abundant data in [49]. ${ }^{6}$ The optimal DBN model structures are the ones that maximize the a posteriori probability of the model $\mathbb{R}$ given the data $\mathscr{G}, \operatorname{Pr}\left\{\mathbb{R} \mid \mathcal{G}\right\} \propto \operatorname{Pr}\left\{\mathcal{G} \mid \mathbb{R}\right\} \operatorname{Pr}\{\mathbb{R}\}$. In [23], the location data was brought into the model inference via the model prior $\operatorname{Pr}\{\mathbb{R}\}$. Loosely speaking, genome-wide location data can be used to measure the degree to which a transcriptional factor, a product of a gene or several genes, binds to the promoter of a gene. So, that data provides a measure of plausibility of a certain gene being a direct parent of some other (or even the same) gene. In other words, by using location data we may be able to assess the likelihood of $X_{j}(t-1) \in \mathbf{P a}\left(X_{i}(t)\right)$.

In order to incorporate even more prior knowledge into the network learning process, we may also consider the use of sequence analysis results, possibly combined with clustering results. For instance, genes having highly homologous promoter sequences are likely to be regulated by the same transcriptional factors. An approach combining both expression data and sequence information for finding putative regulatory elements was introduced in [50] (for further reading see e.g. [51] and references therein). A purely combinatorial approach to the same problem, even though it was also validated by expression data, was introduced in [52]. Assume that two genes, say $X_{i}$ and $X_{j}$, are found to have highly homologous promoter sequences and are hypothesized to be regulated by the same transcriptional factor, say a product of gene $X_{k}$. Then, one can expect that $X_{k}(t-1) \in \mathbf{P a}\left(X_{i}(t)\right) \Leftrightarrow X_{k}(t-1) \in \mathbf{P a}\left(X_{j}(t)\right)$, where the "if and only if"

[^0]
[^0]:    ${ }^{6}$ Bayesian networks were not used in [49].

must be considered, of course, probabilistically, meaning that the probability of this condition can be expected to be high.

In other words, basically any additional information source can be utilized in the process of learning gene regulatory network structure (for a recent study, see [26]). For instance, recent preliminary results indicate that the genetic regulatory networks exhibit scale-free topology, as do many real-world networks [53,54]. All aforementioned information sources can be included in the model induction process through the model prior. Model inference, which utilizes several different information sources, is a topic for further studies.

Another interesting implication of the proposed relationships between the models can be seen after rewriting $\operatorname{Pr}\{\mathcal{M}\}(d)$ as $\operatorname{Pr}\{\mathcal{M}(d) \propto(\mid \operatorname{Pr}\{\mathcal{U} \mathcal{M}, \theta\} \operatorname{Pr}\{\theta \mid \mathcal{M}\}) \operatorname{Pr}\{\mathcal{M}\}$, where $\theta$ denotes the model parameters. Because the model parameters in DBNs correspond to the predictor functions and their selection probabilities in PBNs, one can also use the natural constraints of the predictor function classes in the learning phase in a Bayesian fashion. For instance, Harris et al. [55] recently studied more than 150 known regulatory transcriptional systems with varying number of regulating components and found that these controlling rules are strongly biased toward so-called canalizing functions. These and other natural constraints on the class of rules in genetic regulatory networks [56] can be incorporated in the learning phase.

In summary, we have shown relationships between dynamic Bayesian networks and probabilistic Boolean networks. These relationships between the models extend the collection of advanced analysis tools for both model classes. Further, as the theory of both DBNs and PBNs is under vigorous research, new advances are directly applicable to the gene regulatory networks under both models.

# Acknowledgements 

This study was supported by Tampere Graduate School in Information Science and Engineering (TISE) (H. L.), Academy of Finland (H. L. and O. Y.-H.) and NIH R01 GM072855-01 (I. S.).
