# Fully non-homogeneous hidden Markov model double net: A generative model for haplotype reconstruction and block discovery 

Alessandro Perina ${ }^{\text {a,* }}$, Marco Cristani ${ }^{\text {a }}$, Luciano Xumerle ${ }^{\text {b }}$, Vittorio Murino ${ }^{\text {a }}$, Pier Franco Pignatti ${ }^{\text {b }}$, Giovanni Malerba ${ }^{\text {b }}$<br>${ }^{a}$ Department of Computer Science, University of Verona, Strada le Grazie 15, 37134 Verona, Italy<br>${ }^{\text {b }}$ Department of Mother and Child, Biology and Genetics, Section Biology and Genetics, University of Verona, Strada le Grazie 8, 37134 Verona, Italy

Received 31 October 2007; received in revised form 21 August 2008; accepted 22 August 2008

## KEYWORDS

Haplotype reconstruction; Bayesian network; Variational learning; Block structure

## Summary

Objective: In the last decade, haplotype reconstruction in unrelated individuals and haplotype block discovery have riveted the attention of computer scientists due to the involved strong computational aspects. Such tasks are usually addressed separately, but recently, statistical techniques have permitted them to be solved jointly. Following this trend we propose a generative model that permits researchers to solve the two problems jointly.
Method: The model inference is based on variational learning, which permits one to estimate quickly the model parameters while remaining robust even to local minima. The model parameters are then used to segment genotypes into blocks by thresholding a quantitative measure of boundary presence.
Results: Experiments on real data are presented, and state-of-the-art systems for haplotype reconstruction and strategies for block estimation are considered as comparison.
Conclusions: The proposed method can be used for a fast and reliable estimation of haplotype frequencies and the relative block structure. Moreover, the method can be easily used as part of a more complex system. The threshold used for block discovery can be related to the quality-of-fit reached in the model learning, resulting in an unsupervised strategy for block estimation.
(C) 2008 Elsevier B.V. All rights reserved.

[^0]
[^0]:    * Corresponding author. Tel.: +39 0458027803 ; fax: +39 0458027068.

    E-mail addresses: alessandro.perina@univr.it (A. Perina), marco.cristani@univr.it (M. Cristani), luciano.xumerle@medgen.univr.it (L. Xumerle), vittorio.murino@univr.it (V. Murino), pignatti@medgen.univr.it (P. Pignatti), giovanni.malerba@medgen.univr.it (G. Malerba).

## 1. Introduction

Estimating haplotype ${ }^{1}$ frequencies has become increasingly important in the mapping of complex disease genes, since large numbers of closely linked single nucleotide polymorphisms (SNPs) can be genotyped. SNPs are single base pair differences among individuals in a population. Association studies work on the premise that some SNP genotypes are correlated with a disease phenotype. Numerous studies have shown that the human genome contains regions of high linkage disequilibrium (LD) with low haplotype diversity [1]: these regions are called haplotype blocks or LD blocks, where LD is a nonrandom association of alleles between adjacent SNPs. It is worth noting that SNPs or haplotypes within LD blocks may serve as proxies for causative and still unknown alleles; therefore, an accurate study on the blocks diversity results in a key factor in genome-wide association studies [2] to identify LD blocks containing a susceptible genetic factor that was not yet genotyped. Unfortunately, the allele phase of multilocus genotypes in unrelated individuals is unknown and haplotypes need to be reconstructed [3] before the discovery of LD blocks [4].

Statistical strategies for haplotype reconstruction have been recently introduced [3,5-10]. However, all these strategies, except [6], either do not perform block discovery or do it after the haplotype reconstruction, so that block discovery might be affected by potential reconstruction errors.

In this paper, we propose a statistical generative model for haplotype reconstruction and block estimation, called fully non-homogenous hidden Markov model double net (FNH-HMM double net). The idea of a generative model is to describe the process that generated the observations, employing random variables connected by a conditional probability distribution. Dynamic Bayesian networks (DBNs), and in particular, hidden Markov models (HMMs) [11], are the most known examples of generative models employed for haplotype reconstruction. In [5-7], the idea is to estimate relevant hidden "ancestral" patterns from genotype data, i.e. biologically meaningful allele patterns that represent high frequency haplotype fragments, mimicking biological theories [3]. HMMs are employed to model the fact that alleles at nearby markers are likely to arise from the same ancestral pattern, thus resulting in a block-like structure, where each block begins and terminates in correspondence with recombination hot spots. Our approach closely mirrors the process of genotype generation, considering

[^0]that different portions of the genotype have different probabilities of recombination and also that the LD is higher in some regions than in others (as in $[5,6])$. In our model, the phase information that determines haplotype reconstruction is explicitly modeled, which differs from all the other HMMbased approaches [5-7]. To this end, we employ binary variables with their own distribution estimated by the learning strategy. In this way, the haplotype reconstruction can be performed very easily once the model has completed the learning phase. The uncertainty at each site is therefore evaluated during the phasing process and cannot be computed in the other approaches where the haplotype inference is based on sampling strategies [7], or on a set of maximization procedures [5,6]. In our case, the explicit managements of the genotype generation process is done in terms of a complex (i.e. with several variables) model that has a modular structure; each module is a simple generative model (a FNH-HMM, here formally introduced). This, together with a novel inference strategy for learning based on variational learning [12], permits one to learn the model with a time complexity less than in [6] and comparable to that in [5,7]. More importantly, our strategy is not dependent on the parameter initialization, and less prone to local minima solutions.

The variational learning technique was introduced in this field by [13]. Here the authors introduced a similar generative model based on hybrid HMM for classification purposes: their goal was to distinguish genotypes that belong to patients affected by Crohn's disease from those belonging to healthy patients, starting with the exact knowledge of the block boundaries.

Together with the learning strategy, we equipped our model with an inference procedure strategy that permits it to estimate blocks. In practice, using the FNH-HMM double net, each reconstructed haplotype can be considered as the most probable path among estimated ancestral patterns (due to the recombination). Our inference identifies frequent splits and joins among the paths, which can be considered as block boundaries. Segmentation of block boundaries are determined by thresholding an econometricbased statistical measure, the Gini index [14], which represents the strength of a block. The threshold is easy to find, but, more importantly, it can be related to the degree of fit with which the learning step described the data (i.e. the data loglikelihood w.r.t. the model parameters). This means that (1) the uncertainty collected during the learning can explicitly flow down in the block estimation step and (2) the block estimation becomes an unsupervised operation.


[^0]:    ${ }^{1}$ Haplotypes are combinations of DNA marker alleles in a single chromosome.

Notions of block boundary strength have appeared earlier in this field [15,16]. For example in [16] the authors described a dynamic programming algorithm for finding the optimal segmentation with respect to the minimum description length (MDL) principle [17]. However, the strength measure proposed in [16] is very different from the one proposed here, the time complexity is much higher, and the blocks are calculated using haplotypes.

The rest of the paper is organized as follows: Section 2 gives some background mathematical notions, fix the notation and introduces the FNHHMM; Sections 3-6 explain our framework and Section 7 shows comparative experimental results on haplotype reconstruction and block estimation. Finally, Section 8 draws some conclusions and envisages future perspectives.

## 2. Preliminaries

### 2.1. Generative models and Bayesian networks

The goal of the generative modeling is to develop statistical models that can explain the input data (samples or visible variables, $v$ ), as tangible effects being generated by a combination of hidden variables $(h)$, representing the causes, eventually interconnected with conditional interdependencies. A generative model jointly models the input and the causes via a joint probability distribution $P(v, h)$ or $P$ (effects, causes).

Graphical models are well-known instruments that represent effectively generative models; they use graphs to represent and manipulate joint probability distributions. The states of the graphs represent random (visible or hidden) variables and the edges codify conditional dependence relations among them. Several types of graphical models are present in the literature [18], and, among these, the most used is the Bayesian network.

A Bayesian network for random variables (RVs) $x_{1}, \ldots, x_{R}$ is a directed acyclic graph (see an example in Fig. 1 a).

The nodes of the graph represent the variables, while the directed arcs represent probabilistic dependencies among them. There are two kinds of nodes, the hidden nodes $h$ modeling the hidden variables, and the observable nodes $v$ representing the visible variables. In a Bayesian network a conditional probability function is specified for each RV given its parents, $P\left(x_{i} \mid x_{A_{i}}\right)$, where $A_{i}$ is the set of indices of $x_{i}$ 's parents and $x_{i}$ represents either a hidden or visible variable.

Usually, each $P\left(x_{i} \mid x_{A_{i}}\right)$ is governed by a set of (hidden) parameters $\theta_{i}$ specifying the particular (parametric) form assumed by the conditional probability function (e.g. Gaussian). The parameters $\theta=$ $\bigcup_{i=1}^{R} \theta_{i}$ are treated like hidden variables and are thus included in $h$.

The joint distribution $P(x), x=\{v, h\}$, is given by the product of all the conditional probability functions:
$P(x)=\prod_{i=1}^{R} P\left(x_{i} \mid x_{A_{i}}\right)$
For example, in the Bayesian network of Fig. 1 a we have:
$P(a, b, c, y)=P(b) \cdot P(c) \cdot P(a \mid c) \cdot P(y \mid a, b, c)$
After having fixed the topology of a Bayesian network (i.e. the nodes and their interdependencies, their conditional parametric functional form), it is necessary to learn the model. Learning consists in inferring the hidden quantities (hidden variables and parameters) using the observations, i.e. choosing a possible instance of values for $h$ maximizing the a posteriori distribution $P(h \mid v)$ (Maximum A Posteriori learning), or alternatively, the likelihood $P(v \mid h)$ (Maximum Likelihood learning) [19].

In both cases, this choice cannot often be performed in closed form, and often is not even possible by exploring the space of the possible values assumed by $h$, since such space is exponential in the number of variables. Therefore, instead of considering the exact posterior distribution $P(h \mid v)$, it becomes advantageous to operate on approximations of $P(h \mid v)$, simpler than $P(h \mid v)$. Variational approximate learning [12] consists in inferring the
![img-0.jpeg](img-0.jpeg)

Figure 1 (a) An example of Bayesian network. $a, b$ and $c$ are the hidden variables, while $y$ is the only observed variable; (b) HMM with the respective parameters; (c) FNH-HMM; note that transition and emission matrices are now timedependent.

hidden quantities of a distribution $\mathcal{Q}(h)$ related to $P(h \mid v)$ while minimizing a quantity called free energy, which is defined as follows:

$$
\begin{aligned}
\mathcal{F} & (P, \mathcal{Q})=\int_{h} \mathcal{Q}(h) \log \mathcal{Q}(h) \\
& -\int_{h} \mathcal{Q}(h) \log P(h, v)
\end{aligned}
$$

The free energy is a measure of the approximation accuracy of $P(h \mid v)$ by $\mathcal{Q}(h)$, since
$\mathcal{F}(P, \mathcal{Q})=\mathbb{KL}(P, \mathcal{Q})-\log P(v)$
where $\mathbb{K L}(P, \mathcal{Q})$ is the Kullback-Leibler divergence [14] between $P$ and $\mathcal{Q}$.

### 2.2. Graphical models for sequential data: hidden Markov models

A special type of a Bayesian network is the dynamic Bayesian network (DBN) [20], aimed at modeling sequential data, which in turn are intended as realizations of a stochastic process. Roughly speaking, a DBN is a Bayesian network whose structure is replicated $N$ times (for $N$ slices), where $N$ is the length of the sequence. Each slice can be connected with the other ones via additional conditional dependencies.

The best-known DBN is the discrete-time hidden Markov model $\lambda$, which can be viewed as a Markov model whose states are not directly observable (Fig. 1b); instead, each state is characterized by a probability distribution function, modeling the observations corresponding to that state. More formally, a HMM is defined by the following entities [11]:
(1) $Q,|Q|=L$, the finite set of (hidden) states;
(2) a transition matrix $\mathbf{A}=\left\{a^{m n}\right\}, \quad 1 \leq m, n \leq L$ representing the probability of moving from state $m$ to state $n$ :
$a^{m n}=P\left(S_{k+1}=n \mid S_{k}=m\right), \quad 1 \leq n, m \leq L$,
with $a^{m n} \geq 0, \quad \sum_{n=1}^{L} a^{m n}=1$, and where $S_{k}$ denotes the state occupied by the model at index $k$. Depending on the context, the index $k$ indicates a time index if the considered sequence is thought of as generated by a temporal stochastic process, or it is considered a site index if the sequence is atemporal, with its spatial structure regulated by a Markovian process;
(3) an emission matrix $\mathbf{B}=\left\{b^{m}(v)\right\}$, indicating the probability of emission of symbol $v \in V$ when the system state is $m$. In this problem context, $V=$ \{A, C, G, T\} indicating Adenine (A), Cytosine (C), Guanine (G) and Thymine (T);
(4) the initial state probability distribution $\pi=\left\{\pi^{m}\right\}$ $\pi^{m}=P\left(S_{1}=m\right), \quad 1 \leq m \leq L$
with $\pi^{m} \geq 0$ and $\sum_{m=1}^{L} \pi^{m}=1$.

For convenience, we represent an HMM by a triplet $\lambda=(\mathbf{A}, \mathbf{B}, \pi)$.

### 2.3. Fully non-homogeneous hidden Markov model

Suppose we have a set of $J$ one-dimensional observation sequences each of length $N$, formed by symbols from the set $V$, i.e. $O^{(j)}$ with $j=1 \ldots J$.

A fully non-homogeneous hidden Markov model (FNH-HMM) (shown in Fig. 1c) is a set $\lambda_{\text {FNH }}=$ $\left\{\mathbf{A}_{k}, \mathbf{B}_{k}, \pi\right\}_{k=1}^{N}$ composed by the following parameters:
(1) A site-dependent transition matrix $\mathbf{A}_{k}=\left\{a_{k}^{m n}\right\}$ where

$$
\begin{aligned}
& a_{k}^{m n}=P\left(S_{k+1}=n \mid S_{k}=m\right), \quad 1 \leq m, n \leq L \\
& \quad \text { and } k=1, \ldots, N
\end{aligned}
$$

(2) A site-dependent emission matrix $\mathbf{B}_{k}=\left\{b_{k}^{m}(v)\right\}$ where

$$
\begin{aligned}
& b_{k}^{m}(v)=P\left(v \mid S_{k}=m\right), v \in V, \quad 1 \leq m \leq L \\
& \quad \text { and } k=1, \ldots, N
\end{aligned}
$$

(3) An initial state distribution $\pi=\left\{\pi^{m}\right\}, \quad 1 \leq m \leq L$.

The learning of a FNH-HMM is devised as a modified version of the Baum-Welch (BW) algorithm.

In this phase, the E-step consists in first calculating the standard forward and backward variables $\alpha$ and $\beta$, paying attention that all the transition and emission probabilities involved are site dependent (i.e. dependent on $k$ ). From these variables, key quantities can be obtained, such as the conditional probability of two consecutive hidden states in an observation sequence at site $k$, i.e. $P\left(S_{k}=\right.$ $\left.m, S_{k+1}=n \mid O^{(j)}\right)=\xi_{k}^{(j)}(m, n)$ and the conditional $P\left(S_{k}=m \mid O^{(j)}\right)=\sum_{n=1}^{L} \xi_{k}^{(j)}(m, n)=\gamma_{k}^{(j)}(m)$, where $\xi$ is defined as
$\xi_{k}^{(j)}(m, n)=\frac{\alpha_{k}^{(j)}(m) a_{k}^{m n} b_{k+1}^{n}\left(O_{k+1}^{(j)}\right) \beta_{k+1}^{(j)}(n)}{P\left(O^{(j)} \mid \lambda\right)}$
In the $M$-step the parameters are updated using these quantities. The transition $\mathbf{A}_{k}$ and the emission $\mathbf{B}_{k}$ matrices are updated as follows:
$a_{k}^{m n}=\frac{\sum_{j=1}^{J} \xi_{k}^{(j)}(m, n)}{\sum_{j=1}^{J} \sum_{n=1}^{L} \xi_{k}^{(j)}(m, n)}$
s.t. $O_{k}=v$
$b_{k}^{m}(v)=\frac{\sum_{j=1}^{J} \gamma_{k}^{(j)}(m)}{\sum_{j=1}^{J} \sum_{n=1}^{L} \xi_{k}^{(j)}(m, n)}$.

![img-1.jpeg](img-1.jpeg)

Figure 2 (a) FNH-HMM; (b) FNH-HMM double net: nodes in a solid box indicate that they are replicated the number of times indicated in the bottom left corner; point-dashed arrows mean 1st order Markov dependency. Filled (unfilled) circles mean observed (unobserved) random variables; dotted circles indicate the parameter set of the variables linked by the arrow; (c) SNPs' generative process: the picture is divided in two steps. Each step shows a portion of the process, drawn in an intuitive fashion (left) and in a formal graphical way (right).

The parameter vector $\pi$ is calculated as was done for the HMM.

## 3. The proposed model: FNH-HMM double net

In our framework, $O$ is formed by $J$ observation sequences or samples. Each sample represents the genotype of the $j$ th human subject, i.e. a sequence of $N$ allele pairs; each $k$ th SNP, $k=1, \ldots, N$, is formed by unordered variable pairs $\left\{x_{k}, y_{k}\right\}$ taking values from $\{A, C, G, T\}$.

In each sample, the values of every $k$ th SNP are considered to be generated by two different hidden random variables, called also hidden states, here indicated with $s_{k}$ and $t_{k}$. These variables can take index values $1, \ldots, L$. An ordered sequence of $N$ hidden states $\left\langle s_{1}, \ldots, s_{k}, \ldots, s_{N}\right\rangle\left(<t_{1}, \ldots, t_{N}>\right)$, with the same index value builds an ancestral pattern. The hidden states $s_{k}$ and $t_{k}$ take the pattern index values by considering a first-order Markov property, i.e. considering the previous states, $s_{k-1}$ and $t_{k-1}$, respectively (Fig. 2 c, step 1, Pattern choice). ${ }^{2}$ The generation of a particular nucleotide symbol $x_{k}$ and $y_{k}$ by a given hidden state occurs by means of an emission distribution related to the state $s_{k}$ and $t_{k}$, respectively (Fig. 2 c, step 1, Symbols emission).

Now, in order to simulate the allele phasing that produces the final SNP pair, we add a switch variable $m_{k}$ that decides the order (the phase) of the

[^0]alleles (Fig. 2 c, step 2, Symbols switch). This is a key aspect that distinguishes our approach from the others based on HMM for haplotype reconstruction [5-7]. The addition of the switch variable makes the generative process underlying our model easy and intuitive to understand. On the other hand, the addition of the switch variable makes the application of the classical EM algorithm for model learning very expensive. In our case, the problem is formally solved through the variational learning approach, that additionally overcomes the classical problem of the EM of being highly susceptible to the parameter initialization. Such problems afflict other HMM-based approaches, thus forcing repeated applications of the training algorithm. We call our model FNH-HMM double net, hereafter simply double net, which is depicted in a formal way in Fig. 2 b.

Another way to understand the generative behavior of our model can be observed in Fig. 3, where the generative process is shown for a portion of a genotype. In practice, the proposed model connects two different FNH-HMMs, where the connection holds at the observation level.

Formally, the double net has a joint distribution formed by the two sets of variables, $h=\left\{m_{k}, s_{k}, t_{k}\right\}$ and $v=\left\{x_{k}, y_{k}\right\}$, for each SNP $k$ and for each sample $J$. The model parameters are the transition and emission matrices of the two chains and the initial state distribution $\theta=\left\{\mathbf{A}_{c, k}, \mathbf{B}_{c, k}, \pi_{c}\right\}$, for each $k=1 \ldots N$. The pedix $c$ discriminates between the parameters of the two chains, i.e. if $c=L$ it addresses the lower-chain parameters, if $c=U$ it addresses the upper-chain parameters (see Fig. 2c).

First of all, it is reasonable to consider the samples as i.i.d., so we consider only the joint distribu-


[^0]:    ${ }^{2}$ Choosing the "right" $L$ is an issue not faced here. Driven by biological considerations, we try $7 \leq L \leq 10$ obtaining results very similar in quality. Anyway, we set $L=7$, with which we gather the best haplotype reconstruction quality measures.

![img-2.jpeg](img-2.jpeg)

Figure 3 Alternative FNH-HMM double net representation: the two non-homogeneous hidden Markov chains are coupled at emission level. The dotted box refers to part of the model shown in Fig. 2 b.
tion over a single sample, thus dropping the apex $(j)$. Therefore, we obtain

$$
\begin{aligned}
P(x, y, s, t, m)= & P\left(x_{1}, y_{1} \mid m_{1}, s_{1}, t_{1}\right) P\left(m_{1}\right) P \\
& \times\left(s_{1}\right) P\left(t_{1}\right) \prod_{k=2}^{N}\left[P\left(m_{k}\right) P\right. \\
& \left.\times\left(x_{k}, y_{k} \mid m_{k}, s_{k}, t_{k}\right) P\right. \\
& \left.\times\left(s_{k} \mid s_{k-1}\right) P\left(t_{k} \mid t_{k-1}\right)\right]
\end{aligned}
$$

In the equation above, the connection at the observation level between the FNH-HMMs is easily recognizable due to the term $P\left(x_{k}, y_{k} \mid m_{k}, s_{k}, t_{k}\right)$. The other terms indicate the switching variable probability, $P\left(m_{k}\right)$; the intra-chain transition probabilities, $P\left(s_{k} \mid s_{k-1}\right)$ and $P\left(t_{k} \mid t_{k-1}\right)$; and the initial state probabilities, $P\left(s_{1}\right)$ and $P\left(t_{1}\right)$.

The emission distribution can be further factorized, clarifying the meaning of the switching variable $m_{k} \in\{0,1\}$, which determines the phase of the chromosome pair $\left\{x_{k}, y_{k}\right\}$. If $m_{k}=1$, the state $s_{k}\left(t_{k}\right)$ generates the symbol $x_{k}\left(y_{k}\right)$, otherwise, $m_{k}=0$. This brings us to:

$$
\begin{aligned}
& P\left(x_{k}, y_{k} \mid m_{k}, s_{k}, t_{k}\right) \\
& =\left(P\left(x_{k} \mid s_{k}\right) P\left(y_{k} \mid t_{k}\right)\right)^{m_{k}}\left(P\left(y_{k} \mid s_{k}\right) P\left(x_{k} \mid t_{k}\right)\right)^{1-m_{k}}
\end{aligned}
$$

yielding to the following joint distribution

$$
\begin{aligned}
& P(x, y, s, t, m) \\
& \quad=\left(P\left(x_{1} \mid s_{1}\right) P\left(y_{1} \mid t_{1}\right)\right)^{m_{1}}\left(P\left(y_{1} \mid s_{1}\right) P\left(x_{1} \mid t_{1}\right)\right)^{1-m_{1}} \\
& \quad \times P\left(s_{1}\right) P\left(t_{1}\right) P\left(m_{1}\right) \prod_{k=2}^{N}\left[P\left(m_{k}\right)\left(P\left(x_{k} \mid s_{k}\right) P\left(y_{k} \mid t_{k}\right)\right)^{m_{k}}\right. \\
& \left.\quad \times\left(P\left(y_{k} \mid s_{k}\right) P\left(x_{k} \mid t_{k}\right)\right)^{1-m_{k}} P\left(s_{k} \mid s_{k-1}\right) P\left(t_{k} \mid t_{k-1}\right)\right]
\end{aligned}
$$

## 4. Variational inference and learning

The free energy (see Section 2.1) of our model can be written by taking into account a generic form of $\mathcal{Q}(h)$

$$
\mathcal{Q}(h)=\delta(\theta-\hat{\theta}) \prod_{j=1}^{J} q\left(\left\{m_{k}^{(j)}, s_{k}^{(j)}, t_{k}^{(j)}\right\}_{k=1}^{N}|\theta\rangle\right.
$$

where $\delta$ is the Dirac function. The equation above means that each sample is considered independent. Therefore, the free energy is

$$
\begin{aligned}
\mathcal{F}=\sum_{\text {samples }} \ & \left\{\sum_{m_{k}, s_{k}, t_{k}} q\left(\left\{m_{k}, s_{k}, t_{k}\right\} \mid \theta\right)\right. \\
& \left.\log \frac{q\left(\left\{m_{k}, s_{k}, t_{k}\right\} \mid \theta\right)}{P\left(\left\{x_{k}, y_{k}, m_{k}, s_{k}, t_{k}\right\} \mid \theta\right)}\right\}
\end{aligned}
$$

To make the inference easier to handle and to make it tractable, we use the following constrained form of the function $\mathcal{Q}(h)$, where we employ a factorization of several multinomial distributions:

$$
\begin{aligned}
& q\left(\left\{s_{k}\right\}_{k=1}^{N},\left\{t_{k}\right\}_{k=1}^{N},\left\{m_{k}\right\}_{k=1}^{N}\right) \\
& \quad=q\left(\left\{s_{k}\right\}_{k=1}^{N}\right) q\left(\left\{t_{k}\right\}_{k=1}^{N}\right) \prod_{k=1}^{N} q\left(m_{k}\right)
\end{aligned}
$$

Using this form, known as mean-field [21], we can write down the free energy and easily solve the optimization problem (minimizing $\mathcal{F}$ ). The meanfield approximation is widely used because of its simplicity: it consists in assuming all the component hidden RVs are independent, given the data. This permits the estimation to be insensible to parameter initialization and less prone to local minima [22], unlike the Expectation-Maximization (EM) algorithm [23]. The first advantage holds because,

in the classical EM, variables are connected through conditional distributions. Setting initial values for the parameters of such distributions assumes $a$ priori knowledge about how strongly the causes that generated the data are interconnected among themselves (in our case, it would assume knowledge about the identity of the ancestral pattern at each state). In such cases, the learning operates by revising such guesses when faced with the data. In the mean field approximation, such strong a priori knowledge does not exist. A random initialization of each (decoupled) parameter allows the data to build (and not to revise) the value of the conditional distribution in a more effective way. This, in turn, also helps to avoid local minima. For further details, see [22].

In order to minimize $\mathcal{F}$, we use the variational Expectation-Maximization algorithm [12] which alternates in minimizing the free energy w.r.t. the $\mathcal{Q}(h)$ distribution while keeping fixed the parameters (E-Step), and using the statistics over $\mathcal{Q}(h)$ just collected (M-Step) w.r.t. the parameters $\theta$. When updating $\mathcal{Q}$, the only constraint is that $\int_{h_{i}} q\left(h_{i}^{(j)}\right)=1$ for each hidden variable $h_{i}$ and for each sample $j$. This constraint can be easily accounted for by using Lagrange multipliers. The updating rules are simply obtained by setting the derivatives of $\mathcal{F}$ equal to zero.

In detail, the pseudo-code for the learning of our double net via the EM algorithm is shown below.

Initialization: Randomly choose values for the parameters $\theta$, i.e. the emission and transition matrices of the two chains, and set $q\left(m_{k}^{(j)}\right)=$ 0.5 for each sample $j$ and for each position $k$. E-Step: Minimize $\mathcal{F}$ with respect to $q\left(h_{i}^{(j)}\right)$, forbi each sample $j$ and for each hidden variable $h_{i}$, keeping fixed the values $\theta$. This is done using the following updating rules:

$$
\begin{aligned}
& \frac{\partial \mathcal{F}}{\partial q\left(s_{k}=i\right)}=0 \rightarrow \\
& q\left(s_{k}=i\right)=p\left(s_{k}=i \mid\left\{x_{k}, y_{k}\right\}_{k=1}^{N}\right)=\gamma_{U, k}(i) \\
& \frac{\partial \mathcal{F}}{\partial q\left(t_{k}=i\right)}=0 \rightarrow \\
& q\left(t_{k}=i\right)=p\left(t_{k}=i \mid\left\{x_{k}, y_{k}\right\}_{k=1}^{N}\right)=\gamma_{L, k}(i)
\end{aligned}
$$

where $\gamma_{U, k}(i)$ and $\gamma_{L, k}(i)$ are the probability of being in state $i$ at time $k$ given the observation $O$ and the model $\lambda(P\left(s_{k}=i \mid O, \lambda\right))$ in the respective chain, see Section 2.3. The updating rules can be derived from the forward and backward variables $\alpha$ and $\beta$ noting
that, in the FNH-HMM, we have
$\gamma_{k}(i)=\frac{\alpha_{k}(i)}{P(O \mid \lambda)} \frac{\beta_{k}(i)}{P(O \mid \lambda)}$
where the forward and backward variables are calculated using the following weighted log-likelihood
$\log p\left(x_{k}, y_{k} \mid s_{k}=i\right)=q\left(m_{k}\right.$

$$
\begin{aligned}
& =1) \cdot b_{U, k}^{i}\left(x_{k}\right)+q\left(m_{k}\right. \\
& =0) \cdot b_{U, k}^{i}\left(y_{k}\right)
\end{aligned}
$$

$\log p\left(x_{k}, y_{k} \mid t_{k}=l\right)=q\left(m_{k}\right.$

$$
\begin{aligned}
& =1) \cdot b_{L, k}^{i}\left(y_{k}\right)+q\left(m_{k}\right. \\
& =0) \cdot b_{L, k}^{i}\left(x_{k}\right)
\end{aligned}
$$

Update the distributions over a mask variable as follows:

$$
\begin{aligned}
& \frac{\partial \mathcal{F}}{\partial q\left(m_{k}=1\right)}=0 \rightarrow q\left(m_{k}=1\right) \\
& \quad \propto \exp \left(\sum_{s_{k}} q\left(s_{k}\right) \log b_{U, k}^{s_{k}}\left(x_{k}\right)+\sum_{t_{k}} q\left(t_{k}\right) \log b_{L, k}^{t_{k}}\left(y_{k}\right)\right) \\
& \frac{\partial \mathcal{F}}{\partial q\left(m_{k}=0\right)}=0 \rightarrow q\left(m_{k}=0\right) \\
& \quad \propto \exp \left(\sum_{s_{k}} q\left(s_{k}\right) \log b_{U, k}^{s_{k}}\left(y_{k}\right)+\sum_{t_{k}} q\left(t_{k}\right) \log b_{L, k}^{t_{k}}\left(x_{k}\right)\right)
\end{aligned}
$$

$q\left(m_{k}=1\right)$ and $q\left(m_{k}=0\right)$ are then normalized at every site $k$.

M-Step: Minimize $\mathcal{F}$ with respect to the model parameters $\theta$ setting the derivative $(\partial \mathcal{F} / \partial \theta)=0$. Using the convex combination of the observation likelihoods (Eq. (19)), we can decouple the two FNH-HMMs and update independently the parameters of the two chains $\lambda_{L}$ and $\lambda_{U}$ using the standard Baum-Welch algorithm for FNH-HMMs.

At this point, it is worthy to note other differences of our approach w.r.t the most similar approaches in the literature: [5-7]. In [6], the haplotypes and the blocks are estimated simultaneously and the approach computes the maximum likelihood directly (i.e. it is not based on a Bayesian network), making the system really prone to local minima. In [7], the first-order Markov property that regulates the presence of a particular ancestral pattern is relaxed, bringing to a less accurate haplotype estimation as noted by the authors. In [5], within the context

of a similar generative framework, haplotypes are estimated after the Viterbi calculation of the ancestral pattern identities and, due to the absence of the variational trick, the computational load for the learning step is $O\left(\mathrm{JNL}^{3}\right)$. In our case, it is $O\left(\mathrm{JNL}^{2}\right)$, basing on FNH-HMM inference strategies.

## 5. Haplotype reconstruction

Once the model is learned, it is easy to reconstruct the haplotypes from the genotypes. For each genotype $O^{(j)}=\left\langle\left(x_{1}, y_{1}\right), \ldots\left(x_{k}, y_{k}\right), \ldots\left(x_{N}, y_{N}\right)\right\rangle$, the phase of each $k$ th pair is given by the value of $q\left(m_{k}^{(j)}=1\right)$ : if it is larger than 0.5 , then $x_{k}$ belongs to the upper haplotype and $y_{k}$ belongs to the lower, and vice versa if $q\left(m_{k}^{(j)}=1\right)<0.5$. Note that at each position we can easily understand the uncertainty with which the model estimated the haplotype. This could in principle lead to the creation of measures of confidence for our haplotype reconstruction. Basically, whereas the $q\left(m_{k}^{(j)}=1\right)$ are pooled on 0 s or 1 s , strong certainty is associated to the related alleles phase.

## 6. Linkage disequilibrium block discovery

As mentioned in Section 3, the hidden patterns $1, \ldots, L$ model ancestral haplotype sequences which
have been fragmented and recombined throughout human history, producing all the observed haplotypes. As a first step toward the block discovery, we estimate the most probable pathway through these hidden patterns for each reconstructed haplotype sequence. This is done with a straightforward non-homogeneous version of the Viterbi algorithm [11], paying attention to use the log-likelihood previously introduced in Eq. (19). In this way, we account for all the uncertainty of the haplotype reconstruction in the block discovery task.

All the Viterbi paths (Fig. 4 a) are then placed on a lattice $L \times N$ (Fig. 4b). In this way, at each allele site $k$ we can distinguish $W_{k}$ distinct paths, each one indicated with $w_{k}(I), I=1, \ldots, W_{k} \leq L ; \quad\left\|w_{k}(I)\right\|$ indicates the number of haplotypes traversing $w_{k}(I)$ (see Fig. 4b).

We are now able to perform block discovery. The idea is that if two paths $w_{k}(I)$ and $w_{k}(I)$ do join at site $k+1$, they represent two sets of haplotypes with highly different haplotype fragments up to $k$, becoming similar after $k$. Therefore, a block boundary exists between $k$ and $k+1$. Similar reasoning holds for a split site (see Fig. 4b). We translate this intuition with the boundary presence strength measure $\Omega(k, k+1) \in[0,1)$, which models the existence of a block boundary between sites $k$ and $k+1$, i.e.
$\Omega(k, k+1)=1_{\text {Join }}(k) G(k)+1_{\text {Split }}(k+1) G(k+1)$
![img-3.jpeg](img-3.jpeg)

Figure 4 Toy example (J=4 haplotypes): (a) Viterbi paths; (b) paths over the lattice structure and the relative $\Omega$ plot; note that (b) is projection of (a) over the SNPs-"Ancestral Pattern" plane.

where $1_{\text {Join }}(k)\left(1_{\text {Split }}(k+1)\right)$ is equal to 1 when at least one join (split) is present at time $k(k+1)$, and $G(\cdot)$ is the Gini index [14]:
$G(k)=1-\sum_{i=1 \ldots W_{k}}\left(\frac{\left\|w_{k}(i)\right\|}{W_{k}}\right)^{2}$
The Gini index can be used to describe whether a graph join or split is well balanced or not. For example, a split at site $k$ is well balanced if the cardinalities $\left\{\left\|w_{k}\right\|\right\}$ of the child paths $\left\{w_{k}\right\}$ are similar. The idea is that the higher the $\Omega(k)$, the more likely the presence of a block boundary between site $k$ and $k+1$. On the other hand, a low $\Omega(k)$ means that in the join (split) site $k$, a dominant path (i.e. with a high number of haplotypes associated) merges (splits) with one or more irrelevant paths (see Fig. 4b). Given a threshold $\tau_{\Omega}$, we can assign a block boundary to the site $k$ when $\Omega(k)>\tau_{\Omega}$.

It is valuable to note that all the block boundary measures in the literature [24] are strongly dependent on the accuracy with which the haplotypes are estimated, but there is no way to codify formally this dependency. In our approach, instead, we calculate for a given set of simulated genotypes (with the positions of blocks boundaries a priori estimated) of length $N$, the mean log-likelihood $L L_{m}$ that results from the learning step. This represents a likelihood-based quality of fit criterion for the data, given the model. Then, we evaluate using the ground truth information about the "optimal" value of $\tau_{\Omega}$ in order to minimize the error of block discovery for each genotype produced. We average the values obtaining $\Omega_{m}$. By varying the length of the data we can build a look-up table of $\Omega_{m}, L L_{m}$, and $N$. Therefore, when a novel dataset is available (length $N$ ), if the log-likelihood obtained during the training is higher than the one precalculated for that data length, we can inherit the correspondent $\tau_{\Omega}$. Otherwise, we have to be more conservative and must choose an higher value for $\tau_{\Omega}$. Note that all the data have been processed by fixing the number of ancestral haplotypes to $\hat{L}=7$. The value of $\hat{L}$ has been chosen by maximizing on the haplotype reconstruction quality measures (see next section).

## 7. Experimental results

### 7.1. Haplotype reconstruction

To evaluate the proposed approach, our framework has been extensively tested on different data sets and compared to five other state-of-the-art systems.

Concerning the initialization issue, we again remark that no a priori knowledge has been used (random parameter initialization), and that all the results reported here derive from standard executions of the two inference strategies proposed here.

In the first two experiments, we compared the FNH-HMM double net to various haplotype reconstruction systems in terms of various quality measures. These tests show how our method successfully identifies the largest number of correct haplotypes, while keeping the number of incorrect haplotypes inferred and the correct haplotype frequencies in line with the other state-of-the-art systems. This observation may have practical value if our problem regards the functional genetics, where the issue is identifying the largest number of correct haplotypes, instead of minimizing the number of incorrect haplotypes inferred.

The first data set is taken from the hapmap project [25] from chromosome $7^{3}$ from SNP marker rs323917 to SNP rs324375. The reconstructed haplotype frequencies are summarized in Table 1, where Emp stands for the empirical frequencies, PhLD stands for Phase with linkage disequilibrium [3], fPh stands for fastPhase [7], SPHP stands for SNPHAP [10], Ger stands for Gerbil [6], Hit stands for Hit [5] and Double net stands for our method. Table 3 summarizes the statistics in terms of various measures of quality. In particular, haplotype frequency estimation ( $I_{F}$ ) and haplotype identification index $\left(I_{H}\right)$, proposed in [26], are two appropriate quality measures for the haplotype reconstruction task.

The haplotype frequency estimation $\left(I_{F}\right)$ is a measure defined as the proportion of haplotype frequencies in common between the estimated and the true haplotypes
$I_{F}=1-\frac{1}{2} \sum_{\text {haplotypes }}\left|p_{e, k}-p_{t, k}\right|$
where $p_{e, k}$ and $p_{t, k}$ are the estimated and the true haplotype frequency of the $k$ th haplotype, respectively.

The index $I_{F}$ varies between zero, when true haplotypes have estimated frequencies approaching zero, and one, when observed and estimated frequencies are identical. The index weights more heavily the high-frequency haplotypes.

A second commonly used index is the haplotype identification index $I_{H}$, defined as
$I_{H}=\frac{2\left(m_{\text {true }}-m_{\text {missed }}\right)}{m_{\text {true }}+m_{\text {estimated }}}$

[^0]
[^0]:    ${ }^{3}$ Caucasoid $r 21$ phasell.

Table 1 Haplotype frequencies obtained with a training set composed by 60 genotypes of 25 SNPs. Bold numbers indicate the best reconstruction
![img-4.jpeg](img-4.jpeg)
where $m_{\text {true }}$ is the number of true haplotypes in the sample, $m_{\text {estimated }}$ is the number of estimated haplotypes, and $m_{\text {missed }}$ is the number of true haplotypes not identified in the sample. The value of $I_{H}$ can vary between one, when the identified haplotypes are exactly those present in the true sample, and zero, when none of the true haplotypes has been identified.

As a second test, we choose a dataset available on demand, taken from the pituitary growth hormone (GH1) [27]. The five genes of the human growth hormone locus reside within about 45 kilobases ( kb ) on chromosome 17, and the GH1 is by far the most thoroughly studied gene. It is unusually polymorphic, with 16 SNPs having been identified in a span of 535 base-pairs. The data is taken from the sequencing of 154 recruits of the British army. Using this data, Horan et al. [28], empirically determined 36 haplotypes. In our experiment, we consider this data as ground-truth. The empirical haplotype frequencies exhibit considerable dispersion (see Table 2, column Emp): two haplotypes are relatively common with frequencies of $33 \%$ and $16 \%, 31$ have frequencies below $5 \%$ and 19 haplotypes have frequencies less than $1 \%$. Subsequently, Adkins [27] compared five haplotype reconstruction algorithms on the same dataset.

The reconstructed haplotype frequencies are summarized in Table 2, where we reported the results obtained by Adkins [27]. We added four comparisons to the systems analyzed in the first experiment (see Table 1). Concerning the haplotype reconstruction systems in [27] in Table 2, PhNLD stands for Phase with no linkage disequilibrium taken into account [3], PhLD for Phase with linkage disequilibrium [3], HPLT stands for $H$ aplotyper [8], PLEM stands for the partition-ligation expecta-tion-maximization algorithm [9], and SPHP stands for SNPHAP [10].

The statistics in terms of $I_{F}$ and $I_{H}$ are summarized in Table 3, showing that all the methods have good performances in terms of frequencies in both tests. However our method always identifies the greatest number of haplotypes. This results brings about the best $I_{H}$ index.

### 7.2. Haplotype block partitioning

Concerning the block discovery, no "formal" ground-truth data is present in literature for the block estimation. Nevertheless, universally accepted measures and algorithms exist that have produced results that are considered as groundtruth $[29,30]$. Here, for comparison, we use one of the most well known methods to individuate blocks: the Gabriel method [1]. It is worth noting

that, as a drawback, the Gabriel method is scarcely robust to reconstruction errors.

The first dataset used is taken from chromosome 11 on the fads 1, 2, 3, genes (chr11q12.13) [31]. It is valuable to note that for this test we could not use the pituitary growth hormone (GH1) dataset because no relevant block structure is present (see [27]).

Pairwise LD table (LD plot) is a widely used data structure for block discovery. The pairwise measures $D^{\prime}$ [32](Fig. 5 a - left diagonal elements) and $r^{2}$ [33](Fig. 5 a - right diagonal elements) build the LD table. A high $D^{\prime}\left(r^{2}\right)$ value in position $m, n$ (or $n, m$ ) indicates a block relation between the site $m$ and $n$.

The pairwise LD plot for the dataset considered is shown in Fig. 5 a. Using the Gabriel method, we obtain three major blocks highlighted in the figure with yellow squares. The first block ranges from the first SNP to the fourth, the second consists of SNPs from six to eight, and the last consists of the last four SNPs. Since a LD block is a group of consecutive highly correlated SNPs, one can intuitively be convinced of the presence of the first block looking only at the $D^{\prime}$ measure and noticing that the first four SNPs present a high value $(\approx 1)$ among one another.

With our approach, we first calculate the Viterbi path for each haplotype, that is the most likely sequence of hidden state values that led to that
particular observation [11]. Subsequently, we project all the paths over the lattice structure determined by the SNPs-Ancestral pattern plane (Fig. 5b), calculating the number of paths that share the same path segment as described in Section 6.

At this point, we focus our attention on the split and join points, highlighted in Fig. 5 b with a square.

Using Eq. (23), we can easily calculate the block boundary strength $\Omega(k, k+1)$ for each couple of consecutive SNPs, which is higher when more balanced intersections are present. Fig. 5 c shows the resulting $\Omega$-value: as expected, a high $\Omega$ value is present in correspondence with SNPs $(5,6)$ due to the presence of many splits at SNP 5, and many joins at SNP 6. The same holds for SNPs number (8,9).

Considering our look-up table of $\tau_{\Omega}$ values, we threshold the value of $\Omega$ with $\tau_{\Omega}=0.3$, obtaining the block structure reported in Fig. 5 d. Other block discovery results are shown in Fig. 6. Here, the data is randomly taken from the Hapmap project. In Fig. 6 b, the Pairwise LD table is reported. The table, built using empirical haplotypes, confirms the block division presented in Fig. 6 a, obtained after solving the reconstruction task with FNH-HMM double net and calculating the block boundary strength $\Omega$.

The fourth data set used consists of 11 SNPs taken from the interlukin-1 cluster on human chromosome
![img-5.jpeg](img-5.jpeg)

Figure 5 (a) Pairwise LD plot. The blocks are highlighted with a yellow square; (b) Viterbi paths over the ancestral pattern. Splits/joins are indicated with a square. The arrows indicate where the contributions of the split/joins point votes for a block boundary. In fact, as shown in Eq. (23), a join at position $k$ increases the block presence strength between the $k-1$ th SNP and the $k$ th SNP, while a split at $k$ increases the block presence strength between $k$ and $k+1$; (c) the $\Omega$ plot; (d) resulting blocks for the chr11q12.13 dataset with a threshold $\tau=0.3$. The thickness of the boundaries is proportional to the value of the block presence strength $\Omega$.

Table 2 Haplotype frequencies. Bold numbers indicate the best reconstruction


Table 2 (Continued)
SNP


![img-6.jpeg](img-6.jpeg)

Figure 6 (a) and (c) Viterbi paths over the lattice structure (top) and correspondent $\Omega$ plot (bottom). Splits/joins are indicated with yellow rectangles; block boundaries are shown with a bar whose thickness is proportional to the $\Omega$ value; (b) and (d) pairwise LD table: $D^{\prime}$ (left diagonal elements) and $r^{2}$ (right diagonal elements) values confirm the block boundaries found with our method.

Table 3 Accuracy of inference of haplotype structure on the GHI gene promoter


\# correct and \# wrong stand for respectively the number of corrected and wrong haplotypes inferred.

2q12-2q14 presented in [34]. In Fig. 6 c, the paths over the ancestral patterns inferred after the model training are depicted. No splits or joins are present, and thus only a haplotype block is present here, as confirmed by [34] and by the LD plot shown in Fig. 6 d.

## 8. Conclusions

Haplotype analysis is actually used in medical genetics to localize the genetic region containing susceptibility genes for genetic diseases. Therefore, haplotype frequency estimation and dissection in the LD structure of chromosomal regions are important tasks, since LD structures vary across the genome and among populations. For that reason, it is
important that available computational tools are able to resolve the haplotype phase from unrelated individual genotypes and are able to identify suitable patterns of LD structures in the regions to be studied. In this paper, we proposed a generative framework based on hidden first-order Markov processes able to perform haplotype reconstruction and block discovery at the same time, using two model inferences. The model is based on a connection between two FNH-HMM. The model learning has been carried out under a variational context, and it relies essentially on two independent computations of the Baum-Welch algorithm. In this way, a fast inference procedure is obtained that is linear in the length of genotypes, insensible to model initialization, and less prone to local minima w.r.t those

approaches employing exact versions of the EM algorithm for model learning. The time complexities of the other efficient approaches given here for comparison are $O\left(J N L^{3}\right)$ for HIT, $O\left(J N L^{2}\right)$ for fastPHASE and for Gerbil complexity was not expressed analytically by the authors. The complexity of the other methods ranges between $O\left(N^{2}\right)$ and $O\left(N^{3}\right)$ making it prohibitively expensive to apply them on long haplotypes [6].

To validate the approach (1) we exhaustively compared our method with five other state-of-the-art systems for haplotype reconstruction in terms of various accuracy measures and (2) we tested the block discovery capability with a wellknown block discovery method. The proposed method showed performances that are similar to, and for some measures even better than, the best known reconstruction methods. It is worth noting that our block discovery inference takes into account uncertainty in the haplotype reconstruction and imputation of haplotypes is based on a small number of core haplotypes. These features will be further investigated to develop a unified approach for fine linkage disequilibrium mapping of genes involved in complex diseases.

Future efforts will also be devoted to investigating an extension of our model that considers hidden Markov processes of order higher than one, evaluating the trade-off between the quality of the obtained results and the involved computational complexity.
