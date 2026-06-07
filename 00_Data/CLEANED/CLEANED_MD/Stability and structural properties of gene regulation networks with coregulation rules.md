# Stability and Structural Properties of Gene Regulation Networks with Coregulation Rules (Preprint) 

Jonathan H. Warrell ${ }^{12 *}$, Musa M. Mhlanga ${ }^{123}$<br>${ }^{1}$ Gene Expression and Biophysics group, Council for Scientific and Industrial Research, Pretoria, South Africa<br>${ }^{2}$ Division of Chemical Systems and Synthetic Biology, Faculty of Health Sciences, University of Cape Town, South Africa<br>${ }^{3}$ Unidade de Biofisica e Expressão Genética, Instituto de Medicina Molecular, Universidade de Lisboa, Portugal<br>*jonathan.warrell@gmail.com


#### Abstract

Coregulation of the expression of groups of genes has been extensively demonstrated empirically in bacterial and eukaryotic systems. Such coregulation can arise through the use of shared regulatory motifs, which allow the coordinated expression of modules (and module groups) of functionally related genes across the genome. Coregulation can also arise through the physical association of multi-gene complexes through chromosomal looping, which are then transcribed together. We present a general formalism for modeling coregulation rules in the framework of Random Boolean Networks (RBN), and develop specific models for transcription factor networks with modular structure (including module groups, and multi-input modules (MIM) with autoregulation) and multi-gene complexes (including hierarchical differentiation between multi-gene complex members). We develop a mean-field approach to analyse the stability of large networks incorporating coregulation, and show that autoregulated MIM and hierarchical gene-complex models can achieve greater stability than networks without coregulation whose rules have matching activation frequency. We provide further analysis of the stability of small networks of both kinds through simulations. We also characterize several general properties of the transients and attractors in the hierarchical coregulation model, and show using simulations that the steady-state distribution factorizes hierarchically as a Bayesian network in a Markov Jump Process analogue of the RBN model.


## 1 Introduction

Empirical work has demonstrated that coregulation is a ubiquitous characteristic of transcription factor networks (which we shall refer to as gene regulation networks, or GRNs) in bacterial and eukaryotic systems. The operon model (Jacob and Monod (1961)) provides a simple example of the coregulation of a group of genes in bacteria. Extensive investigation of GRNs in the bacteria Escherichia coli and the yeast Saccharomyces cerevisiae has revealed a range of network motifs indicative of various types of coregulation between groups of operons or genes (Alon (2006), Alon (2007), Milo et al. (2002), Shenn-Orr et al. (2002)). Further investigation of Saccharomyces cerevisiae has revealed that a large component of its GRN can be modeled as a collection of modules each with characteristic functional roles and regulatory motifs, and that these can be further organized into a collection of module groups which share common regulators and regulatory motifs in a combinatorial fashion (Pe'er et al. (2002), Segal et al. (2002), Segal et al. (2003)).

Further work in eukaryotic cells has revealed that coregulation of gene transcription can also occur through the physical association of multi-gene complexes which are transcribed together (Fanucchi et al. (2013), Li et al. (2012), Papantonis et al. (2012)). Such coregulation is dependent on the 3D chromatin conformation of the nucleus in a given cell, which can be stochastic (Fanucchi et al. (2013)). Further, results have shown that the multi-gene complexes formed can have a hierarchical structure, where the transcription of certain members in the complex is dependent on other members in the multi-gene complex being cotranscribed (Fanucchi et al. (2013), Li et al. (2012)). The functional relevance of such hierarchical coregulation is yet to be characterized.

In the following, we are interested in characterizing the properties of networks involving coregulation rules in a general sense. For this purpose, we draw on the framework of Random Boolean Networks (RBNs), or $N K$-networks (Kauffman (1969), Kauffman (1993)). RBNs have provided a powerful framework in which the relationship between topological/rule-based constraints and dynamic (or emergent) properties of a network can be characterized through a combination of analytic and simulation-based methods. Examples of biologically inspired constraints include scale-free topology (Aldena (2003), Kauffman et al. (2004)) and

canalyzing regulation rules (Kauffman et al. (2004)); while emergent dynamical properties include network stability/criticality (Derrida and Pomeau (1986), Kauffman et al. (2004)), attractor and transient structure (Kauffman (1993), Kauffman et al. (2004)), and evolvability (Torres-Sosa et al. (2012)). The application of mean-field methods from statistical physics has permitted analytic results to be obtained in a number of these cases (Aldena (2003), Derrida and Pomeau (1986), Kauffman et al. (2004)). Further, empirical results have supported the general relevance of such models to the dynamics of actual biological systems, despite the simplification involved in the Boolean assumption (Huang et al. (2005), Chang (2008)).

We introduce a general formulation of coregulation rules in the RBN context, along with a characterization of the mean-field dynamics of models incorporating such rules, which can be used to analyse the dynamics in networks incorporating any of the types of coregulation described above. We focus particularly on (a) the multi-input module (MIM) network motif, which consists of a group of genes, all of which share the same regulators and regulatory logic, and occurs in bacterial and eukaryotic networks (Shenn-Orr et al. (2002)), and (b) hierarchical coregulation rules, which provide a model for the kind of hierarchical dependencies described above, observed to occur in multi-gene complexes in some eukaryotic systems (Fanucchi et al. (2013), Li et al. (2012)). By using the mean-field approach, we show that for certain forms of each type of rule we can demonstrate that networks incorporating coregulation achieve greater stability than can be achieved in networks without coregulation, whose rules have matching activation frequency, as defined below. We use simulations to verify the conclusions reached by mean-field analysis for small-scale networks. Further, we characterize general properties of the transients and attractors in the hierarchical coregulation model and the steady-state distribution of its associated annealed model. Particularly, the steady-state distribution necessarily factorizes hierarchically as a Bayesian network, and we demonstrate through simulations that this property also holds for the steady-state distributions of a Markov Jump Process analogue of the model with hierarchical coregulation rules (using the approach of Gillespie (2007)). We discuss the functional relevance of these properties below.

Section 2 offers a brief review of the RBN framework, followed by our general formulation of coregulation rules and their mean-field dynamics in Section 3. We then investigate the properties of the two particular coregulation models discussed above; the multi-input module in Section 4, and hierarchical coregulation model in Section 5. Section 6 concludes with a discussion.

# 2 Random Boolean Networks 

We begin by outlining the Random Boolean Network (or $N K$ network) model introduced in Kauffman (1969), and summarize the mean-field approach used to analyse the stability of this model in Derrida and Pomeau (1986). An RBN model has two parameters, $N$ the number of nodes in the network, which represent the genes, and $K$ the number of regulators for each gene. At a given time $t$ (where $t \in \mathbb{N} \cup\{0\}$, a gene may be either on or off (transcribed or not transcribed), represented by the Boolean values 1 and 0 respectively. The binary variable $\sigma_{i}(t)$ indicates the state of the $i$ 'th gene at time $t$. We will write $R_{i}(k)$ for the $k^{\prime}$ th regulator of gene $i$, where $R_{i}:\{1 \ldots K\} \rightarrow\{1 \ldots N\}$. The dynamics of the model are then fixed by specifying a separate Boolean update rule for each gene:

$$
\sigma_{i}(t+1)=f_{i}\left(\sigma_{R_{i}(1)}(t), \sigma_{R_{i}(2)}(t), \ldots, \sigma_{R_{i}(K)}(t)\right)
$$

where $f_{i}: \mathbb{B}^{K} \rightarrow \mathbb{B}$, with $\mathbb{B}=\{0,1\}$ (we note that the model incorporates only one layer of regulation, and hence cannot distinguish between pre- and post-transcriptional regulation; related models have attempted to incorporate further regulatory layers, see Markert et al. (2010)). Each $(N, K)$ thus fixes a class of networks, which may be sampled randomly by (a) selecting for each gene $i$ its $K$ regulators by sampling $K$ independently identically distributed values from $1 \ldots N$, hence setting $R_{i}$, and (b) for each gene sampling $2^{K}$ Boolean values to set the output of $f_{i}$ on each of the possible settings of its regulators. The outputs to $f_{i}$ may be sampled by giving even weight to the values $\{0,1\}$, hence performing $2^{K}$ Bernoulli trials with mean $1 / 2$; alternatively, a further parameter $p \in[01]$ is introduced (the activation frequency), and the outputs are sampled via $2^{K}$ Bernoulli trials with mean $p$.

To analyse the behaviour of the $N K$-model for the case of large networks (as $N \rightarrow \infty$ ), Derrida and Pomeau (1986) introduce an annealed stochastic approximation, which, instead of fixing the regulator indices $R_{i}$ and update function $f_{i}$ for a given gene at all time-steps, re-samples them at each time-step using one of the underlying generating distributions discussed above. To analyse the stability of a given network class, Derrida and Pomeau (1986) consider the change in Hamming distance over time between parallel runs of the same network with different initial conditions, under mean-field dynamics

in the annealed model. The mean-field dynamics can be characterized by introducing random variables $x_{i}(t) \in[01]$, representing the probability that $\sigma_{i}(1, t) \neq \sigma_{i}(2, t)$, where $\sigma_{i}(j, t)$ is the value of $\sigma_{i}(t)$ when the network is started from initial condition $j(j \in\{1,2\})$. This gives rise to the following mean-field updates (in a model with $p$ as above, and $\delta(i, t)=\left[\sigma_{i}(1, t) \neq \sigma_{i}(2, t)\right]$ where $[A]$ is the Iverson bracket which is 1 when $A$ is true and 0 otherwise, $R_{i t}$ and $f_{i t}$ are the regulator indexing and update functions respectively sampled for gene $i$ at time $t$, and $S_{i}(t)=\sum_{j=1 \ldots K} \delta\left(R_{i t}(j), t\right)$ ):

$$
\begin{aligned}
x_{i}(t+1)= & \sum_{R_{i t}, f_{i t}} P\left(R_{i t}\right) P\left(f_{i t}\right)\left(P\left(S_{i}(t)>0\right) P\left(\delta(i, t+1)=1 \mid S_{i}(t)>0\right)+\right. \\
& P\left(S_{i}(t)=0\right) P\left(\delta(i, t+1)=1 \mid S_{i}(t)=0\right)\right) \\
= & 2 p(1-p) \cdot\left(1-\sum_{R_{i t}} P\left(R_{i t}\right) \prod_{j=1 \ldots K}\left(1-x_{R_{i t}(j)}(t)\right)\right)+0
\end{aligned}
$$

We assume that the $x_{i}(0)$ 's are initialized identically to $p_{0}$, so that each gene takes a different value in the initial configurations with a probability $p_{0}$. Then, by symmetry $x_{i}(t=1)=x_{j}(t=1)$ for all $i, j$, and similarly for $t=2 \ldots \infty$. Hence, we can write the updates in Eq. 2 in terms of a single variable, $x(t)=x_{i}(t)$ for arbitrary $i$ :

$$
x(t+1)=2 p(1-p)\left(1-(1-x(t))^{K}\right)
$$

where we have used the fact as $N \rightarrow \infty$, the probability that each gene has $K$ distinct regulators tends to 1 . The fixed points of Eq. 3 can be characterized by considering the function $g(x)=2 p(1-p)\left(1-(1-x)^{K}\right)$. Clearly, for any fixed point, $x=g(x)$, and hence fixed points occur at intersections of the curves $y=x$ and $y=g(x) . y=x=0$ is always such a solution. Further, we observe that $y=g(x)$ is concave increasing (since $(1-x(t))^{K}$ is convex decreasing), and hence a second fixed-point will only occur when $g^{\prime}(0)>1$ (where $g^{\prime}=\mathrm{d} g / \mathrm{d} x$ ), which can be expressed as:

$$
2 K p(1-p)>1
$$

The fixed point 0 is attracting (and hence the network is stable) if and only if Eq. 4 does not hold, since when $2 K p(1-p)>1$ there is no neighbourhood of 0 such that $g(x)<x$ for all values. For $p=1 / 2$, this leads to the critical value $K=2$, as observed in Derrida and Pomeau (1986) and Kauffman (1993).

# 3 Coregulation Rules 

We first give a general formulation for modeling coregulation in the RBN framework, and provide general methods for studying the mean-field dynamics of such networks. As above, $N$ and $K$ denote the number of nodes (genes) and regulators respectively. We further partition the nodes into $G$ groups, which will represent groups of genes which are coregulated. We assume for convenience that $G$ divides $N$ exactly, so we have $M=N / G$ nodes per group. We let $C:\{1 \ldots N\} \rightarrow(\{1 \ldots G\} \times\{1 \ldots M\})$ be an arbitrary 1-1 mapping, which we shall consider fixed throughout (without loss of generality), such that $C(i)=(g, m)$ can be read as 'node $i$ is the $m$ 'th member of group $g$ '. A coregulated $N K$-network is then defined by: (1) for each group $g \in\{1 \ldots G\}$ picking a regulator indexing function $R_{g}:\{1 \ldots K\} \rightarrow\{1 \ldots N\}$ (hence all members of group $g$ share the same regulators); and (2) for each group $g$ picking a coregulation update rule, $f_{g}: \mathbb{B}^{K} \rightarrow \mathbb{B}^{M}$. The network dynamics can be expressed as:

$$
\sigma_{i}(t+1)=f_{C(i)}\left(\sigma_{R_{g(i)}(1)}(t), \sigma_{R_{g(i)}(2)}(t), \ldots, \sigma_{R_{g(i)}(K)}(t)\right)
$$

where we write $f_{(g, m)}$ for the projection of $f_{g}$ onto its $m$ 'th output, and $g(i)$ for the projection of $C(i)$ onto its first output. We will assume that $R_{g}$ and $f_{g}$ are sampled independently for each group. Hence, we will consider distributions over a class of coregulated networks which factor as $P(R, f)=\prod_{g}\left(P\left(R_{g}\right) P\left(f_{g}\right)\right)$.

As in Section 2, we introduce an annealed version of the coregulated model in order to study its meanfield dynamics. We therefore allow $R$ and $f$ to be resampled at each time step from $P(R, f)$ as above, and write $R_{g t}$ and $f_{g t}$ for the regulation index and update function respectively sampled for group $g$ at time $t$. As above, we consider the situation that the same network is started at two different initial states, and are interested in whether the Hamming distance converges to 0 as an indicator of network stability. We write

$\sigma_{i}(j, t)$ for the state of node $i$ at time $t$ started at the $j$ 'th initial condition $(j \in\{1,2\})$, and $\sigma_{g}(j, t)$ for the vector of states of the nodes in group $g$ at time $t$ starting at the $j$ 'th initialization. For the mean-field dynamic analysis, we introduce continuous variables $c_{g}(v, w, t)$, where $v, w \in \mathbb{B}^{M}$ are all possible settings of $\sigma_{g}(1, t)$ and $\sigma_{g}(2, t)$ respectively, and $c_{g}(v, w, t)=P\left(\left[\sigma_{g}(1, t)=v\right] \wedge\left[\sigma_{g}(2, t)=w\right]\right)$. The variable $x(t)$, representing the expected normalized Hamming distance at time $t$ as in Section 2, can be calculated as $x(t)=(1 /(G M)) \sum_{g \circ w} c_{g}(v, w, t) H(v, w)$, where $H(v, w)$ is the Hamming distance between $v$ and $w$. In the general formulation as given, the mean-field updates can be calculated as:

$$
\begin{aligned}
c_{g}(v, w, t+1)= & \sum_{R_{g}, f_{g}} P\left(R_{g}\right) P\left(f_{g}\right) \sum_{v^{\prime}, w^{\prime} \in \mathbb{B}^{K}} c_{R_{g}}\left(v^{\prime}, w^{\prime}, t\right) \\
& \left(\left[f_{g}\left(v^{\prime}\right)=v\right] \wedge\left[f_{g}\left(w^{\prime}\right)=w\right]\right)
\end{aligned}
$$

Here, we us the short-hands $\sigma_{R_{g}}(j, t)=\left[\sigma_{R_{g}(1)}(1, t), \ldots, \sigma_{R_{g}(K)}(1, t)\right]$, and $c_{R_{g}}\left(v^{\prime}, w^{\prime}, t\right)=$ $P\left(\left[\sigma_{R_{g}}(1, t)=v^{\prime}\right] \wedge\left[\sigma_{R_{g}}(2, t)=w^{\prime}\right]\right)$; writing $\sigma_{R_{g}}(j, t)$ for the vector of the states of the regulators of group $g$ at time $t$ for initialization $j$.

By introducing further assumptions about the forms of $P(R)$ and $P(f)$, we can derive special forms of the updates in Eq. 6 which can be applied to the models in Sections 4 and 5, allowing analytic results to be derived more directly. We first consider constraining $P(R)$. We will write $\mathbb{P}(G)$ for the set of permutations on the set $\{1 \ldots G\}$, and $\mathbb{P}(G, g, h)=\{\pi \in \mathbb{P}(G) \mid \pi(g)=h\}$ (the set of permutations mapping $g$ to $h$ ). Then, we will say that a distribution $P(R)$ has permutational invariance iff for any $\pi \in \mathbb{P}(G, g, h)$ and functions $R_{g}$ and $R_{h}$, whenever $\forall k\left[R_{g}(k)=\pi\left(R_{h}(k)\right)\right]$ (writing $\pi(n)$ for $(\pi(g(n)), m(n))$ ), we have $P\left(R_{g}\right)=P\left(R_{h}\right)$ (alternatively, the distribution remains invariant up to permutations of the group indices applied jointly to the $R$ subscripts and $R$ output regulator indices). Further, we call a distribution $P(R)$ simple when it places zero probability on any function $R_{g}$ for which $g\left(R_{g}(k)\right)=g\left(R_{g}(l)\right)$ and $k \neq l$ (all regulators have distinct groups). We then have:

Proposition 1. For a coregulated $N K$-network with a simple distribution $P(R)$ with permutational invariance as above, and assuming $P\left(f_{g}\right)=P\left(f_{h}\right)$ for all $g, h$, and at initialization that $c_{g}(v, w, 0)=c_{h}(v, w, 0)$ for all $g, h$, the mean-field dynamics are such that $c_{g}(v, w, t)=c_{h}(v, w, t)=c(v, w, t)$ for all $g, h, t$, where:

$$
\begin{aligned}
c(v, w, t+1)= & \sum_{R^{\prime}, f} P\left(R^{\prime}\right) P(f) \sum_{v^{\prime}, w^{\prime} \in \mathbb{B}^{K}}\left(\prod_{k} c_{R^{\prime}(k)}\left(v_{k}^{\prime}, w_{k}^{\prime}, t\right)\right) \\
& \left(\left[f\left(v^{\prime}\right)=v\right] \wedge\left[f\left(w^{\prime}\right)=w\right]\right)
\end{aligned}
$$

and $R^{\prime}:\{1 \ldots K\} \rightarrow\{1 \ldots M\}, P\left(R^{\prime}\right)=\sum_{R_{g}} P\left(R_{g}\right)\left[\forall k\left(m\left(R_{g}(k)\right)=R^{\prime}(k)\right)\right]$ (for arbitrary $g$ ), $c_{m}(a, b, t)=\sum_{v, w} c(v, w, t)\left[v_{m}=a \wedge w_{m}=b\right]$.

For a proof of Proposition 1, see Appendix A. We now consider a further restricted class of coregulation networks, in which $P(R)$ is uniform over the set of functions for which $g\left(R_{g}(k)\right) \neq g\left(R_{g}(l)\right)$ whenever $k \neq l$ (so $P(R)$ remains simple; we shall call a distribution $P(R)$ with this stronger property homogeneous). This implies that $P\left(R^{\prime}\right)$ (defined in terms of $P(R)$ as in Proposition 1) is uniform. Further, we assume that $P(f)$ factorizes across its input values: hence, $P(f)=\prod_{v \in \mathbb{B}^{K}} P^{\prime}(f(v))$, where $P^{\prime}($.$) is independent of v$. Then, we have:

Proposition 2. For a coregulated $N K$-network as in Proposition 1, where in addition $P(R)$ is homogeneous and $P(f)$ factorizes across its input values as $\prod_{v \in \mathbb{B}^{K}} P^{\prime}(f(v))$, under mean-field dynamics we have:

$$
x(t+1)=\mathcal{K}\left(1-(1-x(t))^{K}\right)
$$

where, writing $H(v, w)$ for the Hamming distance between $v$ and $w$,

$$
\mathcal{K}=\frac{1}{M} \sum_{v, w \in \mathbb{B}^{m}} P^{\prime}(v) P^{\prime}(w) H(v, w)
$$

Proof. We assume that we can calculate $x(t)$, and show that the update in Eq. 8 follows. Following the definition of $x(t)$ above, and using the fact (from Proposition 1) that $c_{g}(v, w, t+1)=c(v, w, t+1)$ for all

$g:$

$$
x(t+1)=\frac{1}{M} \sum_{v, w \in \mathbb{B}^{m}} c(v, w, t+1) H(v, w)
$$

Since $H(v, w)=0$ when $v=w$, these terms will not contribute to the summation in Eq. 10. Assuming then that $v \neq w$, following Eq. 7 we have:

$$
\begin{aligned}
c(v, w, t+1)= & \sum_{R^{\prime}, f} P\left(R^{\prime}\right) P(f) \sum_{v^{\prime}, w^{\prime} \in \mathbb{B}^{K}}\left(\prod_{k} c_{R^{\prime}(k)}\left(v_{k}^{\prime}, w_{k}^{\prime}, t\right)\right) \\
& \left(\left[f\left(v^{\prime}\right)=v\right] \wedge\left[f\left(w^{\prime}\right)=w\right]\right) \\
= & \sum_{f, v^{\prime} \neq w^{\prime}} x^{K-H\left(v^{\prime}, w^{\prime}\right)}(1-x)^{H\left(v^{\prime}, w^{\prime}\right)} \\
& P(f)\left(\left[f\left(v^{\prime}\right)=v\right] \wedge\left[f\left(w^{\prime}\right)=w\right]\right) \\
= & \sum_{v^{\prime} \neq w^{\prime}} x^{K-H\left(v^{\prime}, w^{\prime}\right)}(1-x)^{H\left(v^{\prime}, w^{\prime}\right)} P^{\prime}(v) P^{\prime}(w) \\
= & \left(1-(1-x(t))^{K}\right) P^{\prime}(v) P^{\prime}(w)
\end{aligned}
$$

using the fact that only non-matching $v^{\prime}, w^{\prime}$ values can lead to a non-matching $v, w$ and the homogeneity of $P(R)$ to make the first rearrangement, and the factorization property of $P(f)$ to make the second. The proposition follows by substituting Eq. 11 into Eq. 10.

# 4 Multi-Input Module Model 

We first outline two models based on the Multi-Input Module (MIM) network motif (Shenn-Orr et al. (2002)). The first is a generalization of the motif which allows module groups and combinatorial regulation as in Segal et al. (2003), and reduces to the basic motif when only one module per group is allowed. The second allows a Single-Input Module (SIM) with autoregulation (Shenn-Orr et al. (2002)) to be embedded in the MIM motif, as observed in Segal et al. (2003), which reduces to the SIM with autoregulation when $K=1$.

### 4.1 Model with Module Groups

A multiple-input module is defined as a group of genes whose regulators are identical, and which respond identically to those regulators. We generalize this motif to a multiple-input module group, which consists of a group of MIMs each with identical regulators, such that for a given setting of the regulators, either no module is activated, or with probability $p$, each module in the group is activated with a probability $q$. We note that this motif resembles the module group model of Segal et al. (2003), where (1) for simplicity we assume all modules in a module group share exactly the same regulators (rather than all sharing at least one regulator as in Segal et al. (2003)), (2) combinatorial use of a common set of regulatory motifs is modelled by activating subsets of the modules (or none) for a given setting of the regulators (the expected size of the subset being determined by $q$ ), (3) for convenience we assume there is no variation in response within a module, and (4) we allow arbitrary decision rules for the regulatory logic of a given module, in place of decision trees ((3) may be straightforwardly incorporated into our model, by introducing a further parameter representing the probability that a gene is activated given it is in an activated module).

The multiple-input module group as above may be modelled as a coregulated $N K$-network, as in Section 3. Here, we take the module-group as the coregulation unit, so that $G$ represents the number of module groups, $M$ the number of genes per module group, and in addition we introduce $L$, the number of modules per module group. Each module therefore has $N_{L}=M / L$ genes (which cannot be shared between modules, as in Segal et al. (2003)). We assume that $P(R)$ is simple homogeneous, as defined in Section 3. With

![img-0.jpeg](img-0.jpeg)

Fig. 1. Multi-input module coregulation models. (A) Model with module groups. Arrows denote regulatory relationships, and arrows between boxes are implicitly repeated for every pair of nodes in the source and target box. Illustration shows model with $K=4$ regulators, $L=3$ modules per group, and $N_{L}=2$ genes per module. Black/white nodes represent on/off gene states respectively, and a possible network configuration is shown. (B) Model with autoregulation. Notation as for (A). A model is shown with parameters $K=4, L=1, N_{L}=5, M=6$. (C) Graphs plot LHS and RHS quantities from Eq. 19. Parameter ranges where $Z^{\prime}(0)>\phi$ are those in which the autoregulated MIM model achieves potentially greater stability than an independently regulated model with matching activation frequency, and in ranges where $Z^{\prime}(0)<\phi$ the independent model achieves potentially greater stability. Parameters as shown, with $K=3, M=5$, and $p=0.7$ (left), and $p=0.85$ (right). (D) Graphs show parameter settings for which the autoregulated MIM model model achieves strictly greater stability than the independent model (left), and for which the independent model achieves strictly greater stability (right). Dotted line shows $y=x$, and an intersection of $g(x)$ with $y=x$ at a non-zero value indicates an attracting fixed point which prevents $x$ reaching 0 ( $g(x)$ is as in Eq. 42 for autoregulated model, and as defined following Eq. 3 for the independent model). Remaining parameters are as for (C).
$p$ and $q$ as above, we can define $P(f)$ as:

$$
\begin{aligned}
& P(f)=\prod_{v \in \mathbb{B}^{K}} P^{\prime}(f(v)) \\
& P^{\prime}(u)= \begin{cases}(1-p)\left[|u|_{1}=0\right]+ & p \mathrm{~B}\left(|u|_{1}(L / M) ; L, q\right) \\
0 & \text { if } \forall(a, b) s . t . l(a)=l(b), u_{a}=u_{b}
\end{cases}
\end{aligned}
$$

where $\mathrm{B}(.; N, p)$ denotes the Binomial distribution with $N$ trials and mean $N p,|u|_{1}=\sum_{i} u_{i}$ (the $L_{1}$ norm of $u$ ), and we have introduced a fixed function $l:\{1 \ldots M\} \rightarrow\{1 \ldots L\}$, which assigns module indices to genes within a module group $\left(\left(\sum_{m}[l(m)=a]\right)=M / L\right.$ for any $\left.a\right)$. The model is illustrated in schematic form in Figure 1A. We note that, when $q=1$ or $L=1$, the model reduces to an MIM, where all genes are coactivated with a probability $p$ for a given regulator setting.

Since $f$ factorizes over its input values in Eq. 12, Proposition 2 may be applied to analyse the stability of the model. Hence, following Eq. 9:

$$
\begin{aligned}
\mathcal{K} & =\frac{1}{M} \sum_{v, w \in \mathbb{B}^{m}} P^{\prime}(v) P^{\prime}(w) H(v, w) \\
& =\frac{1}{M}(2 p(1-p) M q+p^{2} M \cdot 2 q(1-q) \\
& =2 p q(1-p q)
\end{aligned}
$$

where line 2 follows by considering that when pairs $(v, w)$ are sampled from $P^{\prime}(v) P^{\prime}(w)$, with probability $2 p(1-p)$ one is active and the other not, so that the genes in each module take different values in $v$ and $w$ with probability $q$, while with probability $p^{2}$ both are active, and so each module takes a different

value with probability $2 q(1-q)$. We are interested in comparing the stability of this model with an $N K$ network without coregulation (which we will refer to as an independent or independently regulated model), whose outputs are active with the same probability (which we refer to by saying it has the same activation frequency). Considering Eq. 12, the expected proportion of active outputs across all inputs to $f$ is $p q$. Hence, following Eq. 3, the update for the normalized Hamming distance in an $N K$ net whose outputs are sampled independently with this probability is:

$$
x(t+1)=2 p q(1-p q)\left(1-(1-x(t))^{K}\right)
$$

which is identical to Eq. 8 with $\mathcal{K}$ as above. In the limit of large $N$ then, the stability of the multiple-input module group model is not different to a model without coregulation with matching activation frequency. While in this case coregulation does not affect stability therefore in the asymptotic limit, for small networks we can show that the stability of the coregulated model is greater than the corresponding model with independent regulation (see Appendix B).

# 4.2 Model with Autoregulation 

We now adapt the multi-input module group model above to include autoregulation. For this purpose, we add a further node to the coregulation unit, so that $M=L N_{L}+1$, and $l:\{1 \ldots M\} \rightarrow\{0 \ldots L\}$, with $\left(\sum_{m}(l(m)=a)\right)=L_{N}$ for $a=1 \ldots M$, and $l(1)=0$; hence $m=1$ picks out a distinguished member of each module group, which will be subject to autoregulation. Further, we expand the number of regulators to $2 K-1$, which will allow us to select different regulators for the distinguished member versus the other members of the module group. The distribution of the regulation function is:

$$
P\left(R_{g}\right) \propto \begin{cases}0 & \text { if } \exists(a, b), a \neq b, g\left(R_{g}(a)\right)=g\left(R_{g}(b)\right) \\ 0 & \text { if } R_{g}(1) \neq C(g, 1) \\ 1 & \text { otherwise }\end{cases}
$$

The first case of Eq. 15 ensures that $P\left(R_{g}\right)$ is simple, while the second ensures that the first regulator of group $g$ is the distinguished member of group $g$ itself (hence, it is not simple homogeneous). Clearly, Eq. 15 has the permutational invariance property discussed previously, since any permutation on $\{1 \ldots G\}$ which maps group $g$ to $h$ will map distinguished member $C(g, 1)$ to $C(h, 1)$ also. We complete the model definition by specifying $P(f)$. Here, we use four parameters: $p_{0}$ is the probability the distinguished member will be activated at $t+1$ given it was inactive at $t ; p_{1}$ is the probability it will be active at $t+1$ given it is active at $t ; p$ is the probability that the module group as a whole will be activated; and $q$ is as above the probability a module in the group is active if the group is activated. Further, we require that, writing $u_{a}$ for $u \in \mathbb{B}^{2 K-1}$ restricted to indices $[1 \ldots K]$ and $u_{b}$ for $u$ restricted to indices $[1, K+1 \ldots 2 K-1]$ : $u_{a}=v_{a}$ implies $f_{1}(u)=f_{1}(v)$, and $u_{b}=v_{b}$ implies $f_{2 \ldots M}(u)=f_{2 \ldots M}(v)$ (so that for all other functions, $P(f)=0$ ). The above leads us to define $P(f)$ as:

$$
P(f)=P_{a}\left(f^{\prime}\right) P_{b}\left(f^{\prime \prime}\right)
$$

where $f^{\prime}: \mathbb{B}^{K} \rightarrow \mathbb{B}, f^{\prime}\left(u_{a}\right)=f_{1}(u) ; f^{\prime \prime}: \mathbb{B}^{K} \rightarrow \mathbb{B}^{M-1}, f^{\prime \prime}\left(u_{b}\right)=f_{2 \ldots M}(u)$; and:

$$
\begin{aligned}
P_{a}\left(f^{\prime}\right) & =\prod_{u_{a} \in \mathbb{B}^{K}} P_{a}^{\prime}\left(u_{a}(1), f^{\prime}\left(u_{a}\right)\right) \\
P_{a}^{\prime}(\beta, v) & = \begin{cases}\left(1-p_{0}\right)^{[v=0]} p_{0}^{[v=1]} & \text { if } \beta=0 \\
\left(1-p_{1}\right)^{[v=0]} p_{1}^{[v=1]} & \text { otherwise }\end{cases} \\
P_{b}\left(f^{\prime \prime}\right) & =\prod_{u_{b} \in \mathbb{B}^{K}} P_{b}^{\prime}\left(f^{\prime}\left(u_{b}\right)\right) & \\
P_{b}^{\prime}(v) & = \begin{cases}(1-p)\left[|v|_{1}=0\right]+ & p \mathrm{~B}\left(|v|_{1}(L / M) ; L, q\right) \\
0 & \text { if } \forall(a, b) \text { s.t. } l(a)=l(b)>0, v_{a}=v_{b}\end{cases}
\end{aligned}
$$

A specific case of a module group with a regulator subject to autoregulation is observed in Segal et al. (2003) (the autoregulator being the transcription factor, Yap6; see their Figures 5 and 7f). Further, for $L=K=1$, the model reduces to an autoregulated single-input module, which is observed to be

a common network motif in bacteria and eukaryotes (Alon (2007)). The model is illustrated in Figure 1B. For convenience, in Figure 1B and the following, we will take $L=1$, so that each module group contains only one module, and each coregulation group contains a single module of $M-1$ nodes along with one distinguished autoregulatory node (hence forming a coregulation group of size $M$ ). We also set $q=1$, so that the module activation is determined entirely by $p$.

As remarked, the distribution $P\left(R_{g}\right)$ as defined in Eq. 15 is simple and has the permutational invariance property. Hence Proposition 1 can be used to analyse the stability of the model. Further, writing $p^{\prime}$ for the probability that an arbitrary output of $f$ is 1 under $P(f)$ (the activation frequency), we have:

$$
\begin{aligned}
p^{\prime} & =\sum_{f} P(f)(1 / M) \sum_{u, m}\left[f_{m}(u)=1\right] \\
& =\sum_{f} P_{a}\left(f^{\prime}\right) P_{b}\left(f^{\prime \prime}\right)(1 / M) \sum_{u, m}\left[f_{m}(u)=1\right] \\
& =\frac{0.5\left(p_{0}+p_{1}\right)+(M-1) p}{M}
\end{aligned}
$$

Hence, we are interested in the circumstances in which a coregulated model as above is able to achieve (or unable to achieve) greater stability than an independently regulated model with activation frequency $p^{\prime}$. Using Proposition 1, we can show that:

Proposition 3. For an autoregulated MIM model as above, with $L=q=1$ and identical initialization for all coregulated groups, the autoregulated MIM model has greater or equal stability to an independent $N K$-network with identical activation frequency (meaning that $x$ has a fixed point greater than 0 only when the independent model does) when the following condition holds:

$$
\begin{aligned}
Z^{\prime}(0) & \geq \phi\left(p_{0}, p_{1}, p\right) \\
& =\frac{M\left(2\left(\frac{M-1}{M}\right)(K-1) p(1-p)-2 K p^{\prime}\left(1-p^{\prime}\right)\right)}{1+2(M-1) p(1-p)}
\end{aligned}
$$

where

$$
\begin{aligned}
Z^{\prime}(0)= & \frac{\left(\left(1-p_{0}\right) p_{0}-\left(1-p_{1}\right) p_{1}\right)\left(p_{1} p_{0}-\left(1-p_{1}\right)\left(1-p_{0}\right)\right)}{\left(1-\left(1-p_{0}\right) p_{1}\right)^{2}-\left(\left(1-p_{1}\right) p_{0}\right)^{2}}+ \\
& \frac{\left(\left(1-p_{0}\right) p_{0}+\left(1-p_{1}\right) p_{1}\right)\left(\left(1-p_{0}\right) p_{0}-\left(1-p_{1}\right) p_{1}-1\right)}{\left(1-\left(1-p_{0}\right) p_{1}\right)^{2}-\left(\left(1-p_{1}\right) p_{0}\right)^{2}}
\end{aligned}
$$

subject to the condition that $Z(x)$, defined in Appendix C, is decreasing convex over the interval $[01]$. Similarly, the independent model has greater or equal stability when $Z^{\prime}(0) \leq \phi$.

For a proof of Proposition 3, see Appendix C. We can use the condition in Eq. 19 to investigate the stability of the autoregulated model under various parameter settings. Figure 1C for instance plots $Z^{\prime}(0)$ against $\phi\left(p_{0}, p_{1}, p\right)$ as a function of $p_{0}$, while fixing $p_{1}$ to a high ( 0.95 ) and low ( 0.05 ) value on the left and right graphs respectively ( $p$ fixed in both). In regions in which $\phi>Z^{\prime}(0)$, the coregulated model cannot be less stable than the independent model, while for $\phi<Z^{\prime}(0)$ it cannot be more stable. For $p_{1}=0.95$, corresponding to positive-feedback, the coregulated model can only achieve greater stability when $p_{0}$ is not too low: for low values of $p_{0}(<\sim 0.2)$, the 0 value of the autoregulator is a competing stable value, which disrupts the stability of the value 1 (left). For $p_{1}=0.05$, corresponding to negative feedback, the opposite is the case, and the model can achieve greater stability only when $p_{0}$ reinforces the stability of 0 (right). Interestingly, in the positive feedback case (left), the coregulation model can be stabilized also for very low values of $p_{0}(<\sim 0.01)$, corresponding to the 0 value of the autoregulator achieving greater stability than the value 1 . In all cases, the precise points at which the relative changes in stability and instability occur depend on the value of $p$, which determines the stochasticity of the module. Figure 1D picks parameter settings demonstrating a strict increase and decrease in stability of the coregulated model with respect to the independent model, using particular settings from the corresponding regions in Figure 1C. We further verify the stability/instability of these models in the small network setting by comparing simulations with the mean-field analysis given above (see Appendix B).

# 5 Hierarchical Coregulation Model 

The formation of multi-gene complexes via chromatin conformation, whose members are cotranscribed, has been ubiquitously observed in eukaryotic nuclei (Papantonis et al. (2012)). Two studies have observed that the members of such complexes may exhibit a hierarchical organization, such that members lower in the hierarchy are only transcribed if members at a higher level are transcribed. For instance, Li et al. (2012) observe a four member complex, in which one member (GREB1) must be transcribed for transcription of the remaining members to occur. Fanucchi et al. (2013) observe a gene-complex with three members, arranged into a three-tier hierarchy such that high-level transcription of the second (TNFAIP2) depends on transcription of the first (SAMD4A), and transcription of the third (SLC6AS) likewise depends on the second.

We present here a simple model of such hierarchical coregulation. Our model is a coregulated network as above, where we take the coregulation units to represent multi-gene complexes (hence $M$ denotes the number of genes per complex). For generality, we allow an arbitrary hierarchical structure to be placed over the members of a complex, which is represented by the function $\mathrm{Pa}:\{1 \ldots M\} \rightarrow\{0 \ldots M\}$. $\mathrm{Pa}\left(m_{1}\right)=m_{2}$ denotes that $m_{2}$ is the parent of $m_{1}$ in the hierarchical ordering, and we set $\mathrm{Pa}(m)=0$ for members which have no parent. We assume that for no element $m_{1}$ do we have $\mathrm{Pa}\left(m_{1}\right)=m_{2}, \mathrm{Pa}\left(m_{2}\right)=$ $m_{3}, \ldots, \mathrm{Pa}\left(m_{n}\right)=m_{1}$ (there are no loops), and hence Pa induces a partial ordering over $\{1 \ldots M\}$. For convenience, the function Pa is fixed for a given network, implying that all coregulation groups share the same hierarchical structure.

The model has one additional parameter $p$, which is the probability that a gene is active given its parent is active, or its probability of activation if it has no parent. For a gene whose parent is inactive, we take its probability of activation to be 0 . Hence, we specify $P(f)$ as follows:

$$
\begin{aligned}
P(f) & =\prod_{v \in \mathbb{B}^{K}} P^{\prime}(f(v)) \\
P^{\prime}(u) & =\prod_{m} p^{\prime}(u(m), u, \mathrm{~Pa}(m)) \\
p^{\prime}(b, u, m) & = \begin{cases}p^{b}(1-p)^{(1-b)} & \text { if }(m \neq 0, u(m)=1) \vee(u(m)=0) \\
{[b=0]} & \text { otherwise. }\end{cases}
\end{aligned}
$$

$P(f)$ therefore factorizes across its input values, according to our earlier definition (Section 3). The model is completed by specifying $P(R)$, which we take to be simple homogeneous. Examples of coregulation rules with various hierarchial structures across their outputs, and possible $f$ functions sampled from the corresponding $P(f)$ distributions are shown in Figure 2A.

### 5.1 Stability

Since $P(f)$ factorizes across its inputs and $P(R)$ is simple homogeneous, mean-field analysis of the stability of a given model with hierarchical coregulation can be made using Proposition 2. For simplicity, we give a detailed analysis here of the class of hierarchical models which place a total order across their members of the form $\mathrm{Pa}(m)=m-1$, so that the first member of each coregulation group has no parent, the second member is the child of the first, and so on. For the case of $M=3$, this corresponds directly to the observed hierarchy in Fanucchi et al. (2013). These rules can also be seen to impose an analogous structure over their outputs to the structure imposed by canalyzing rules over their inputs (see Kauffman et al. (2004)). The relationship between rules of this form and canalyzing rules is discussed further in Appendix D. For this class of models, we have:

Proposition 4. For a hierarchical coregulated $N K$-network with $\mathrm{Pa}(m)=m-1$ as above, under meanfield dynamics we have:

$$
x(t+1)=\mathcal{K}(M)\left(1-(1-x(t))^{K}\right)
$$

where,

$$
\mathcal{K}(M)=\frac{2}{M} \sum_{i=1 \ldots M} i\left(\sum_{j=0 \ldots(M-i-1)} p^{2 j+i}(1-p)^{2}+p^{2 M-i}(1-p)\right)
$$

![img-1.jpeg](img-1.jpeg)

Fig. 2. Hierarchical coregulation models. (A) Illustrates possible models. Notation is as in Fig 1, and additionally magenta arrows indicate Pa relationship over rule outputs (where the source node of a magenta arrow is the parent of the target node). For both (i) and (ii), $K=M=3$. (i) shows a model which places a total order over its outputs $(\operatorname{Pa}(m)=m-1)$, while (ii) shows a partial ordering. Tables show a valid coregulatory function $f$ which respects the hierarchical structure of each model. (B) Shows two parameter settings for which the hierarchical coregulation model achieves strictly greater stability than an independent model with matching activation frequency. A model is stable when $g(x)$ remains below the dotted line $y=x$, preventing a non-zero attracting fixed point from occurring (see Eq. 27). For both graphs, $p=0.5$ and $\operatorname{Pa}(m)=m-1$. (C) Compares the fit of a Bayesian network to the steady-state distributions of independent and hierarchically coregulated models, using a Markov Jump process analogue to the Boolean model. For both models, $N=20, K=2, p=0.5$, and for the coregulated model $M=4$. The median log-likelihood of the best fitting Bayesian Network is shown for 40 trials, and error bars indicate the upper quartiles (* $p<0.05$, one-tailed Mann-Whitney test).
Proof. From Eq. 21, we observe that the only valid output values for $f$ are $v_{0}=[0,0, \ldots, 0], v_{1}=$ $[1,0, \ldots, 0], v_{2}=[1,1,0, \ldots, 0], \ldots, v_{M}=[1,1, \ldots, 1]$. Further, we know that the Hamming distance between any two outputs is in the set $\{0 \ldots M\}$, and that for a given Hamming distance $i$, it can only occur between two outputs of the form $v_{j}$ and $v_{j+i}$. Assuming $j+i<M$, the probability of generating $v_{j}$ (from $P^{\prime}($.$) in Eq. 21$ ) is $p^{j}(1-p)$, and the probability of generating $v_{i}$ is $p^{j+i}(1-p)$. For the case that $j+i=M$ the probability of generating $v_{i}$ is $p^{j+i}$. Hence, for outputs $u, v$ sampled independently from $P^{\prime}($.$) , we have$ that:

$$
\begin{aligned}
P(H(u, v)=i) & =\sum_{j=0 \ldots M-i-1} 2 p^{j}(1-p) p^{j+1}(1-p)+2 p^{M-i}(1-p) p^{M} \\
& =2 \sum_{j=0 \ldots M-i-1} p^{2 j+1}(1-p)^{2}+p^{2 M-i}(1-p)
\end{aligned}
$$

where the factor of 2 arises from the fact that each pair $v_{j}$ and $v_{j+i}$ may be ordered arbitrarily for $H(u, v)>$ 0 . Since, following Eq. 9 of Proposition 2,

$$
\mathcal{K}(M)=\frac{1}{M} \mathbb{E}(H(u, v))=\frac{1}{M} \sum_{i=1 \ldots M} i P(H(u, v)=i)
$$

the proposition follows.

Following Section 3, we observe that $\left(1-(1-x(t))^{K}\right)$ is concave, and so a model with hierarchical coregulation where $\operatorname{Pa}(m)=m-1$ will have a fixed point only at zero when $g^{\prime}(0)<1$, where $g^{\prime}$ is the

differential with respect to $x$ of the function $g(x)=\mathcal{K}(M)\left(1-(1-x(t))^{K}\right)$; hence the model is stable when $\mathcal{K}(M) K<1$. We can calculate the activation frequency (the probability of an arbitrary output gene being on) of the hierarchical model as:

$$
\begin{aligned}
p^{\prime} & =\frac{1}{M} \sum_{i=1 \ldots M} P^{\prime}\left(u_{i}=1\right) \\
& =\frac{1}{M} \sum_{i=1 \ldots M} \prod_{j=1 \ldots i} p \\
& =\frac{1}{M} \sum_{i=1 \ldots M} p^{i}
\end{aligned}
$$

Hence, by Eq. 4, a independent model with the same activation frequency is stable when $2\left(K / M^{2}\right) p^{\prime}(1-$ $\left.p^{\prime}\right)=2\left(K / M^{2}\right)\left(\sum_{i} p^{i}\right)\left(1-\sum_{i} p^{i}\right)<1$. The hierarchical coregulation model therefore can achieve greater stability than an independent model with identical activation frequency when:

$$
\mathcal{K}(M)<2 \frac{1}{M^{2}}\left(\sum_{i=1 \ldots M} p^{i}\right)\left(M-\sum_{i=1 \ldots M} p^{i}\right)
$$

For simplicity, we now analyse the case in which $p=0.5$. Here:

$$
\begin{aligned}
\mathcal{K}(M) & =\frac{2}{M} \sum_{i=1 \ldots M} i\left(0.5^{2+i} \sum_{j=0 \ldots(M-i-1)} 0.5^{2 j}+0.5^{2 M-i+1}\right) \\
& =\frac{2}{M} \sum_{i=1 \ldots M} i\left(0.5^{2+i} \frac{1-0.5^{2(M-i)}}{1-0.5^{2}}+0.5^{2 M-i+1}\right) \\
& =\frac{2 \sum_{i=1 \ldots M} i 0.5^{i}}{3 M}+\frac{0.5^{2 M} \sum_{i=1 \ldots M} i 0.5^{-i}}{3 M} \\
& =\frac{2\left(2-0.5^{M}(2+M)\right.}{3 M}+\frac{0.5^{2 M}\left(2+2^{M}(2 M-2)\right)}{3 M}
\end{aligned}
$$

using the geometric series expansion $\sum_{j=0 \ldots N} p^{j}=\left(1-p^{N}\right) /\left(1-p^{2}\right)$ in line 2 , and the identities $\sum_{k=1 \ldots N} k 0.5^{k}=2-0.5^{N}(2+N)$ and $\sum_{k=1 \ldots N} k 2^{k}=2+2^{N}(2 N-2)$ in line 4. Further, since $\sum_{i=1 \ldots N} 0.5^{i}=1-0.5^{N}$, we have that $p^{\prime}=(1 / M)\left(1-0.5^{M}\right)$, and $\left(2 / M^{2}\right) p^{\prime}\left(M-p^{\prime}\right)=$ $\left(2 / M^{2}\right)\left(M-1+0.5^{M}-0.5^{2 M}\right)$. For the case of $p=0.5$ then, multiplying Eq. 27 through by $M>0$ and rearranging, the condition for coregulation to have a stabilizing effect becomes:

$$
\left(2-\frac{2}{M}-\frac{4}{3}\right)+\left(0.5^{M-1}-\frac{0.5^{2 M-1}}{M}-\frac{2(0.5)^{2 M}}{3 M}\right)+\frac{2(0.5)^{M}}{M}>0
$$

The left-hand side of Eq. 29 is 0 for $M=1$, and is satisfied for $M=2,3$. Clearly, when $M>3$ the first group of terms is positive. Further, for $M>1$, we have:

$$
\frac{0.5^{2 M-1}}{M}+\frac{2(0.5)^{2 M}}{3 M}<\frac{0.5^{2 M-1}}{M}+\frac{0.5^{2 M-1}}{M}=\frac{0.5^{2(M-1)}}{M}<0.5^{M-1}
$$

and hence the second group of terms in Eq. 29 is positive for $M>3$. It follows that the condition is satisfied for all $M>1$, and hence the hierarchical coregulation model with $p=0.5$ is always at least as stable as a model without coregulation and equal activation frequency. Examples are shown in Figure 2 for two settings of the parameters $K$ and $M$ (with $p=0.5$ ) under which the coregulation mean-field dynamics tend to 0 while the independent model with equal activation frequency tends to a non-zero fixed-point (implying strictly greater stability for the coregulation model). Although the above analysis applies only to models with $p=0.5$, we verified by calculation that Eq. 27 holds for all combinations of parameters $(p, M)$ where $p \in\{0.01,0.02, \ldots, 0.99\}$ and $2 \leq M \leq 10000$, suggesting that this is a general phenomenon. Further, we compare the mean-field analysis above with small network simulations of the model in Appendix A.

# 5.2 Other Structural Properties 

We briefly consider here some additional structural properties of hierarchically coregulated networks. In Section 5.2, we consider the case $p=0.5$ and $\operatorname{Pa}(m)=m-1$ for convenience.

Attractor and transient structure We note first that, because of the form of $P(f)$ the dynamics of the hierarchically coregulated model are highly constrained. To investigate these constraints, we introduce the notion of an output space, $O$, which is the set of network configurations that result by applying the network's update rules to all possible input configurations. For the hierarchical model, we have:

$$
O=\left\{\left[v_{\mathbf{m}(1)}, v_{\mathbf{m}(2)}, \ldots, v_{\mathbf{m}(G)}\right] \mid \mathbf{m} \in\{0 \ldots M\}^{G}\right\}
$$

where the $v_{m}$ are defined as in the proof of Proposition 4. Eq. 31 follows since each coregulation group must take a valid output value following an update, so the network state as a whole must be a combination of these. Hence, we have $|O|=(M+1)^{G}$. In contrast, for an $N K$ network without coregulation such that $p \notin\{0,1\}$, we have that $O=\mathbb{B}^{N},|O|=2^{N}=2^{M G}$.

An attractor is either a network state which updates to itself, or a closed cycle of network states under the update rules. Any attractor must therefore be a subset of the output space, since each state in the attractor must be mapped to either from itself, or another attractor state. By contrast, a transient, which is a sequence of network states respecting the update rules whose final member belongs to an attractor, may have an initial state which is not in the output space, but all subsequent states must belong to $O$.

The considerations above suggest that part of the increased stability in the hierarchical coregulated model may be a result of the much smaller output space (in contrast to an independent model with matching activation frequency). As a further consequence, we might expect that the attractors in the hierarchical coregulated model would be shorter in length, since they are constrained to lie in a smaller output space (alternatively, we might expect that the probability of a path in the output space intersecting itself and forming an attractor after a given number of steps is greater in the coregulated model, since the path is constrained to lie in a smaller subspace, although clearly this probability is not determined by $|O|$ alone). To test this prediction, we ran simulations of hierarchically coregulated networks while varying $M$, the size of the coregulation groups, from $2 \ldots 5$, and compared the length of the attractors encountered from a uniformly distributed initial state with those encountered in an $N K$ network without coregulation with update rules having matching activation frequency (fixing $N=40$ and $K=3$ in all simulations). The results are in Table 1, which shows a pronounced reduction in attractor lengths in the coregulated model for all parameter settings.

Table 1. Comparing attractor lengths in hierarchical coregulation and independent models. The median and median absolute deviation of the length of the first attractor encountered over 100 simulations is shown. $p$-values are shown for the one-tailed Mann-Whitney test. For all simulations, $N=40, K=3$.


Steady-state distributions The steady-state of the annealed model with hierarchical coregulation (which involves sampling a new update rule from $P(f)$ for each group at every time step) can be simply expressed:

$$
P(\mathbf{x})=\prod_{g=1 \ldots G} \prod_{m=1 \ldots M} P^{\prime \prime}\left(\mathbf{x}_{g}(m) \mid \mathbf{x}_{g}(\operatorname{Pa}(m))\right)
$$

where we write $\mathbf{x}_{g}(m)$ for the setting of the $m$ 'th gene in coregulation group $g$ (for convenience we fix $\mathbf{x}_{g}(0)=1$ ), and we have $P^{\prime \prime}(x \mid 1)=p^{x}(1-p)^{1-x}$ and $P^{\prime \prime}(x \mid 0)=[x=0]$. Given the partial order constraints on Pa, Eq. 32 expresses a factorization of the steady-state distribution in the form of a Bayesian network.

We were interested in whether such hierarchical steady-state distributions would similarly emerge in an analogue to the coregulation model above which drops the Boolean constraint on the gene expression levels. We therefore investigated a Markov Jump process (MJP) analogue of the hierarchical coregulation model above. Here, in place of the Boolean state vector, we let $\mathbf{x} \in(\mathbb{N} \cup\{0\})^{N}$, which can be taken to represent for instance the transcript count associated with each gene at a given point in time (see Wilkinson (2009), Wilkinson (2011)). The model is parameterized identically to the Boolean model, with

parameters $N, K, M, p$ and associated distributions $P(R), P(f)$. However, rather than using the function $f_{g}$ to directly update group $g$ at discrete time-steps, updates take place stochastically in continuous time according to rate equations derived from $f$ and $R$. An MJP analogue to the independent $N K$ network can be derived similarly, and full details of the derivation are given in Appendix E.

To test for hierarchical structure in the steady-state distributions of the MJP analogue model, we generated 40 hierarchically coregulated and independent networks fixing $N=20, K=2, p=0.5$ in both models and setting $M=4$ in the coregulated model, and simulated each model 20 times for a duration $t=[0100]$ (starting from a 0 initial state). We took the final states of each simulation to represent samples from the steady state distribution (we observed qualitatively that by $t=100$ the behaviour of each variable had typically stabilized), and fitted a Bayesian network to each steady state, using a Markov chain MonteCarlo approach to learn the structure of the network (Murphy (2001)). We compared the log-likelihoods of the best fitting Bayesian networks for the hierarchically coregulated and independent conditions. Figure 2C shows the fit to be significantly higher for the coregulated networks, suggesting that such 'structured stochasticity' in the steady-state distributions may be a general feature of this class of networks.

# 6 Discussion 

We have provided here a general analysis of coregulation in the context of Random Boolean Networks, particularly with respect to the emergent dynamical properties of networks which embody various kinds of coregulatory motifs. We have provided general tools for the mean-field analysis of stability in networks incorporating coregulatory rules, and applied these tools to two cases of biological interest. Significantly, we have shown that multi-input module motifs with positive or negative feedback (autoregulation) can enhance network stability within certain parameter ranges, but can have a destabilizing effect in other parameter ranges. By contrast, our analysis suggests that hierarchical coregulation is stabilizing in all cases. We also investigate further structural properties of networks with hierarchical coregulation, showing them to have smaller output spaces and shorter attractors than comparable networks without coregulation, and hierarchically structured steady-state distributions in both Boolean and analogous Markov Jump process models.

The findings we present suggest that part of the function of these motifs may consist in the effects they have on global network dynamics. For instance, while previous analysis of the SIM with autoregulation suggested that feedback can function as a stabilizing mechanism when viewed in isolation (for instance, allowing the system to respond only to signals which are temporally extended, see Alon (2006)), the analysis presented here allows us to investigate the effects on global stability of such feedback. Indeed, our analysis suggests that global context needs to be taken into account in assessing the effects of such motifs. Similarly, it has been suggested that hierarchical coregulation of multi-gene complexes could function in part to regulate the stoichiometry of the gene products associated with its members (Li et al. (2012)). This is concordant with our results which suggest that such motifs may robustly induce hierarchical structure in the network steady-state distributions, and results from other studies suggest that such structure could be important biologically (for instance, Bayesian networks have proved to be a useful model class in modeling both gene expression data, Friedman et al. (2000), and proteomic data, Sachs et al. (2005)). Our findings also suggest another role for hierarchical coregulation motifs, namely global network stability, and provide a means of interpreting observed parameters within this context (for instance, which models will result in subcritical dynamics, and which in chaotic dynamics).

One short-coming of our analysis is the fact that we have concentrated on small-scale network motifs, and have only considered large networks which are built by combining these stochastically without further structural constraints. Analyses of the global structure of transcription factor networks, for instance using ENCODE data to study the human TF network (Gerstein et al. (2012)), has suggested that it may be appropriate to view the global structure as layered (for instance, by categorizing TFs as high-level, mid-level or low-level regulators), and that the occurrence of network motifs is highly constrained by this global topological structure. Alternatively, scale-free global topological structure has been shown to be ubiquitous in biological networks (Aldena (2003)). It is likely that incorporating such interactions between global topological structure and motif occurrence will substantially modify the analysis given here. However, we believe that the simplified case presented here is important as a first step, and may also be of relevance from an evolutionary stand-point, since plausibly the evolution of isolated network motifs is expected to precede (and enable) the evolution of global structure (such predictions may be tested via simulations using an approach such as Torres-Sosa et al. (2012) for example). A further caveat to our analyses is that they have focussed mainly on the large-network case (as $N \rightarrow \infty$ ) necessary to apply mean-field techniques. As our

simulations show, the properties of such motifs in small networks need not match the large-scale behaviour (for instance, we show that the multiple input module group is stabilizing in the small network context, although in the large-scale limit its mean-field dynamics match those of a network without coregulation). Further, although we show that certain properties are robust across both Boolean and Markov Jump process model classes, further work is required to establish the generality of these results outside the Boolean context.

We hope then that this analysis provides a basis for understanding the properties of coregulation motifs in the context of global network dynamics. As discussed, we believe that such considerations may be important in interpreting and predicting the empirically observed parameter ranges of particular motifs, and suggestive of their functionality. Further, we hope that these results will provide a basis for future theoretical work, particularly concerning the relationship between coregulatory network motifs, global topological structure and network dynamics as discussed above, and also modeling the role of coregulatory motifs in the evolution of network structure.

# Appendix A. Proof of Proposition 1 

Proof. We first note that the distribution $P\left(R^{\prime}\right)$ in the proposition is well defined, since the set of functions $R_{g}$ and $R_{h}$ for which $\left[\forall k\left(m\left(R_{g}(k)\right)=R^{\prime}(k)\right)\right]$ is identical for any $g, h$ and fixed $R^{\prime}$ (which may be denoted $\left.\mathcal{R}_{R^{\prime}}=\left\{R \mid\left[\forall k(m(R(k))=R^{\prime}(k))\right]\right\}\right)$, and any member of $\mathbb{P}(G, g, h)$ is a 1-1 mapping on this set which preserves the probability assigned to each member (by the permutational invariance property), entailing that $\sum_{R_{g}} P\left(R_{g}\right)\left[\forall k\left(m\left(R_{g}(k)\right)=R^{\prime}(k)\right)\right]=\sum_{R_{h}} P\left(R_{h}\right)\left[\forall k\left(m\left(R_{g}(k)\right)=R^{\prime}(k)\right)\right]$.

The proposition may be proved by induction. The base-case at $t=0$ is given by the initial conditions. Assuming then for induction that $c_{g}(v, w, t)=c_{h}(v, w, t)=c(v, w, t)$ at time $t$, from Eq. 6 we have:

$$
\begin{aligned}
c_{g}(v, w, t+1)= & \sum_{R_{g}, f} P\left(R_{g}\right) P(f) \sum_{v^{\prime}, w^{\prime} \in \mathbb{B}^{K}} c_{R_{g}}\left(v^{\prime}, w^{\prime}, t\right) \\
& \left(\left[f\left(v^{\prime}\right)=v\right] \wedge\left[f\left(w^{\prime}\right)=w\right]\right) \\
= & \sum_{R_{g}, f} P\left(R_{g}\right) P(f) \sum_{v^{\prime}, w^{\prime} \in \mathbb{B}^{K}}\left(\prod_{k} c_{m\left(R_{g}(k)\right)}\left(v_{k}^{\prime}, w_{k}^{\prime}, t\right)\right) \\
& \left(\left[f\left(v^{\prime}\right)=v\right] \wedge\left[f\left(w^{\prime}\right)=w\right]\right)
\end{aligned}
$$

where we use the simplicity property and the induction hypothesis to factorize $c_{R_{g}}\left(v^{\prime}, w^{\prime}, t\right)$. By inspection, we have:

$$
c_{m\left(R_{g}(k)\right)}\left(v_{k}^{\prime}, w_{k}^{\prime}, t\right)=c_{R^{\prime}(k)}\left(v_{k}^{\prime}, w_{k}^{\prime}, t\right)
$$

for arbitrary $v^{\prime}, w^{\prime}, k$, where $R^{\prime}$ is chosen such that $R_{g} \in \mathcal{R}_{R^{\prime}}$. Hence $\sum_{v^{\prime}, w^{\prime} \in \mathbb{B}^{K}}\left(\prod_{k} c_{m\left(R_{g}(k)\right)}\right.$ $\left.\left(v_{k}^{\prime}, w_{k}^{\prime}, t\right)\right) \cdot\left(\left[f\left(v^{\prime}\right)=v\right] \wedge\left[f\left(w^{\prime}\right)=w\right]\right)$ is identical for all such $R_{g}$ and independent of $g$, as is the sum when weighted by $\sum_{R_{g} \in \mathcal{R}_{R^{\prime}}} P\left(R_{g}\right)=P\left(R^{\prime}\right)$. The sum across $R_{g}$ in Eq. 33 may thus be replaced by a sum across $R^{\prime}$, leading to the update in Eq. 7, which is independent of $g$.

## Appendix B. Small network simulations

The analysis of stability in the models above has used a mean-field approximation to network dynamics, which holds only in the case of large networks (as $N \rightarrow \infty$ ). Here, we analyse the stability of all models in the small network context through simulations.

As noted in Section 4.1, the MIM model without autoregulation has identical mean-field dynamics to an $N K$-network without coregulation with matching activation frequency (which we will call the independent model, and where activation frequency denotes the expected proportion of positive rule outputs). This does not necessarily imply the models have equal stability however for small network sizes. To investigate this, we ran simulations of the MIM model without autoregulation, setting $N=12, K=3, p=0.5$ and $M=2,3$. For convenience, we set $L=1$, so there is one module per module group, and $q=1$, so the activation of each group occurs with probability $p=0.5$. We compared this model to an independent

![img-2.jpeg](img-2.jpeg)

Fig. 3. Small network simulations. (A) Small network simulations comparing the MIM model without module groups with an independent model with matching activation frequency. Black solid lines show mean-field approximation (same for both models). Solid and dotted lines show expected value of $x$ (the normalized Hamming distance) calculated from the annealed approximation to each model, and the mean value of $x$ across 10 simulations respectively. Parameter settings as shown, with $p=0.5, K=3$. (B) As for (A), but compares MIM model with autoregulation to matching independent model. Solid lines show mean-field approximation. Parameter settings as shown with $p=0.7, p_{0}=$ $0.5, p_{1}=0.95, K=3$. (C) As for (B), but compares hierarchical coregulation model with matching independent model. Parameters as shown with $p=0.5, K=6$.
model with $N=12, K=3, p=0.5$, and do not assume the simplicity condition on $R$ for either model. We ran 10 pairs of simulations of each model, where in each case one member of the pair is initialized to a random network state uniformly over $\mathbb{B}^{N}$, and the other is initialized by flipping the state of $M$ genes of the first. We then track $x$, the Hamming distance normalized by $N$, for $T=50$ time-steps. Figure 3A compares the mean value of $x$ across all simulations for $M=2$ (upper), and $M=3$ (lower) (dotted lines show simulation results, and black line shows the mean-field estimate). As shown, the mean-field estimate severely over-estimates $x$ for $t>\sim 5$. Further, the simulations show that in this small network context, the MIM model does achieve greater stability (lower $x$, implying smaller Hamming distance) than the independent model.

The greater stability of the MIM model above in the small network context can be analysed by considering the full dynamics of the annealed model, as opposed to a mean-field approximation. Since for $L=1$, $q=1$, all genes in a coregulated group must be either 0 or 1 together, we can consider such a MIM model to be equivalent to an independent model with $N / M$ nodes. For an independent model with $N$ nodes, $x$ can take the values $0,1 / N, 2 / N, \ldots, 1$ at each time-step. In the annealed model (where $R$ and $f$ are resampled at each time-step), we can calculate exactly the distribution at each time step by setting:

$$
P\left(x_{t+1}\right)=\frac{1}{N} \sum_{x_{t}} P\left(x_{t}\right) \mathrm{B}\left(N x_{t+1} ; N, 2 p(1-p)\left(1-\left(1-x_{t}\right)^{K}\right)\right)
$$

where $\mathrm{B}(.; N, p)$ is the Binomial distribution with $N$ trials and mean $N p$. Using Eq. 35, we can derive an exact expression for the expected value of $x$ under the annealed model:

$$
\begin{aligned}
\mathbb{E}\left[x_{t+1}\right] & =\sum_{x_{t+1}} P\left(x_{t+1}\right) x_{t+1} \\
& =\frac{1}{N} \sum_{x_{t+1}} x_{t+1} \sum_{x_{t}} P\left(x_{t}\right) \mathrm{B}\left(N x_{t+1} ; N, 2 p(1-p)\left(1-\left(1-x_{t}\right)^{K}\right)\right) \\
& =\sum_{x_{t}} P\left(x_{t}\right) \mathbb{E}\left[x_{t+1} \mid x_{t}\right]
\end{aligned}
$$

where

$$
\mathbb{E}\left[x_{t+1} \mid x_{t}\right]=2 p(1-p)\left(1-\left(1-x_{t}\right)^{K}\right)
$$

In Figure 3A, the exact expectations for $x_{t}$ using Eq. 36 are plotted as solid blue/red lines for the independent/MIM model respectively, which are shown to provided better approximations to the simulations than the mean-field dynamics.

Since $\mathbb{E}\left[x_{t+1} \mid x_{t}\right]$ is concave in $x_{t}$ (as $\left(1-x_{t}\right)^{K}$ is convex), by Jensen's inequality we have:

$$
\mathbb{E}\left[x_{t+1}\right] \leq \mathbb{E}\left[x_{t+1} \mid \mathbb{E}\left[x_{t}\right]\right]
$$

In the following, we assume that $N>>(N / M)$, and that $P\left(x_{1}\right)$ is a delta distribution (we choose a fixed Hamming distance $N x_{0}$ at initialization). Then, at $t=2, P\left(x_{t}\right)=(1 / N) \mathrm{B}(.; N, c)$ for the independent model, and $P\left(x_{t}\right)=(M / N) \mathrm{B}(.; N / M, c)$ for the MIM model, where $c=2 p(1-p)\left(1-\left(1-x_{0}\right)^{K}\right)$, and for both models, $\mathbb{E}\left(x_{2}\right)=c$. Since $N>>(N / M), P\left(x_{2}\right)$ is highly peaked for the independent model, and hence the upper-bound in Eq. 38 is approximately satisfied, leading to $x_{3} \approx c^{\prime}$, where $c^{\prime}=$ $2 p(1-p)\left(1-(1-c)^{K}\right)$. For the MIM model, $P\left(x_{2}\right)$ is less highly peaked, and hence $\mathbb{E}\left[x_{3}\right]<c^{\prime}$. For $t>3$, we can show by induction that the expected value of the MIM model remains below that of the independent model, since:

$$
\begin{aligned}
\mathbb{E}_{\mathrm{MIM}}\left[x_{t+1}\right] & \leq \mathbb{E}_{\mathrm{MIM}}\left[x_{t+1} \mid \mathbb{E}_{\mathrm{MIM}}\left[x_{t}\right]\right] \\
& <\mathbb{E}_{\text {indep }}\left[x_{t+1} \mid \mathbb{E}_{\text {indep }}\left[x_{t}\right]\right] \\
& \approx \mathbb{E}_{\text {indep }}\left[x_{t+1}\right]
\end{aligned}
$$

where we write $\mathbb{E}_{\text {indep }}[$. $]$ and $\mathbb{E}_{\text {MIM }}[$. $]$ for the expected values under the independent and MIM models (with $N$ and $N / M$ nodes) respectively, and use Jensen's inequality in the first line, the inductive hypothesis in the second, and the fact that $N>>M$ in the third. Eq. 39 is confirmed in Fig. 3A, and provides a rationale for the greater stability of the MIM model in the small network simulations.

We further investigate the MIM model with autoregulation (see Section 4.2) in the small network setting in Fig. 3B. Here, we choose the parameters $p=0.7, p_{0}=0.5, p_{1}=0.95, K=3, M=5$, for which the mean-field analysis predicts greater stability for the coregulated model, which has only a zero fixedpoint, than the matching independent model, which has a non-zero fixed point. We compare networks with $N=30$ nodes (upper) and $N=120$ nodes lower (for smaller networks, the variation in network dynamics across simulations was significantly larger, and the models were not sharply distinguished). As expected, in the larger $N=120$ network, simulations of the independent and coregulated models are sharply separated, tending towards non-zero and zero fixed points respectively. Simulations for $N=30$ show that this behaviour also occurs in the smaller network, although the separation of the models is less pronounced. In Fig. 3C we simulate the hierarchical coregulation model (see Section 3), again choosing a parameter setting for which the mean-field analysis predicts a zero fixed-point only for the coregulated model, and a non-zero fixed point for the matching independent model ( $p=0.5, K=6, M=8$ ). We compare $N=24$ (upper) and $N=120$ (lower) network sizes. In both cases, the coregulated model tends quickly to the zero fixed-point in all simulations. The independent model simulations exhibit non-zero fixedpoints, with the larger network fixed-point being higher, providing a better fit to the predicted mean-field dynamics. As a whole, the simulations above suggest that the mean-field analysis remains informative for small networks, although the differences predicted between models may be less pronounced than for larger networks, and new phenomena may emerge, which the analysis of the exact dynamics in the annealed model sheds light on.

# Appendix C. Proof of Proposition 3 

Proof. For the autoregulated MIM model with $L=q=1$, the only valid settings of the coregulated groups are $S=\left\{\left[0 \mathbf{0}_{M-1}\right],\left[1 \mathbf{0}_{M-1}\right],\left[0 \mathbf{1}_{M-1}\right],\left[1 \mathbf{1}_{M-1}\right]\right\}$, where $\mathbf{0}_{A}$ is the vector of 0 's length $A$ (similarly for $\mathbf{1}_{A}$ ). Using Proposition 1 and the above, we therefore need only consider $c(v, w, t+1)$ for $(v, w) \in S^{2}$ to derive the mean-field dynamics for the autoregulated model. We will write $c_{1}\left(v_{1}, w_{1}, t\right)$ for $P\left(\left[\sigma_{C(g, 1)}(1, t)=\right.\right.$ $\left.v_{1}\right] \wedge\left[\sigma_{C(g, 1)}(2, t)=w_{1}\right]), c_{2}\left(v_{2}, w_{2}, t\right)$ for $P\left(\left[\sigma_{C(g, 2 \ldots M)}(1, t)=v_{2}\right] \wedge\left[\sigma_{C(g, 2 \ldots M)}(2, t)=w_{2}\right]\right)$, and

$u(t)=c_{1}(0,0, t), v(t)=c_{1}(1,1, t), y(t)=c_{2}(0,1, t)+c_{2}(1,0, t)$. Then, using Eq. 17 and writing $H(.,$.$) $ for the Hamming distance, we have:

$$
\begin{aligned}
x(t) & =\frac{1}{M} \sum_{v, w \in \Re^{m}} c(v, w, t) H(v, w) \\
& =\frac{1}{M}((1-u(t)-v(t))+(M-1) y(t))
\end{aligned}
$$

and the updates for $u, v, y$ take the form:

$$
\begin{aligned}
& u(t+1)=u(t)\left(\neg p_{0} \neg x^{K-1}+\neg p_{0}^{2}\left(1-\neg x^{K-1}\right)-\neg p_{1} \neg p_{0}\right)+ \\
& v(t)\left(\neg p_{1} \neg x^{K-1}+\neg p_{1}^{2}\left(1-\neg x^{K-1}\right)-\neg p_{1} \neg p_{0}\right)+\neg p_{1} \neg p_{0} \\
& v(t+1)=u(t)\left(p_{0} \neg x^{K-1}+p_{0}^{2}\left(1-\neg x^{K-1}\right)-p_{1} p_{0}\right)+ \\
& v(t)\left(p_{1} \neg x^{K-1}+p_{1}^{2}\left(1-\neg x^{K-1}\right)-p_{1} p_{0}\right)+p_{1} p_{0} \\
& y(t+1)=2 p(1-p)\left(1-(u(t)+v(t)) \neg x^{K-1}\right)
\end{aligned}
$$

where we write $\neg p, \neg p_{0}, \neg p_{1}, \neg x$, for $(1-p),\left(1-p_{0}\right),\left(1-p_{1}\right),(1-x(t))$ respectively. At a fixed-point, we must have $u(t+1)=u(t), v(t+1)=v(t), y(t+1)=y(t)$, which jointly imply $x(t+1)=x(t)$. Hence, by eliminating $y$, we can show by algebraic manipulation that at steady state the following relationship must hold:

$$
\begin{aligned}
x & =g(x) \\
g(x) & =\frac{1}{M}\left(1-Z+(M-1) 2 p(1-p)\left(1-Z \neg x^{K-1}\right)\right)
\end{aligned}
$$

where

$$
\begin{aligned}
Z & =u+v \\
u & =A u+B v+\neg p_{1} \neg p_{0} \\
v & =C u+D v+p_{1} p_{0} \\
A & =\neg x^{K-1} \neg p_{0} p_{0}+\neg p_{0}^{2}-\neg p_{1} \neg p_{0} \\
B & =\neg x^{K-1} \neg p_{1} p_{1}+\neg p_{1}^{2}-\neg p_{1} \neg p_{0} \\
C & =\neg x^{K-1} \neg p_{0} p_{0}+p_{0}^{2}-p_{1} p_{0} \\
D & =\neg x^{K-1} \neg p_{1} p_{1}+p_{1}^{2}-p_{1} p_{0}
\end{aligned}
$$

Writing $g^{\prime}(x)$ and $Z^{\prime}(x)$ for the differentials of $g(x)$ and $Z(x)$ with respect to $x$ respectively, we can show:

$$
\begin{aligned}
& g^{\prime}(x)=\frac{1}{M}\left(2 p \neg p(M-1)(K-1) Z \neg x^{K-2}-Z^{\prime}(x) \cdot\left(1+2 p \neg p(M-1) \neg x^{K-1}\right)\right) \\
& g^{\prime}(0)=\frac{1}{M}\left(2 p \neg p(M-1)(K-1)-Z^{\prime}(0)\left(1+2 p \neg p(M-1)\right)\right)
\end{aligned}
$$

where, noting that $Z, A, B, C, D$ are all implicitly functions of $x$,

$$
Z^{\prime}(x)=\frac{\left(p_{1} p_{0}-\neg p_{1} \neg p_{0}\right)\left(B^{\prime}-A^{\prime}\right)}{(1-D)(1-A)-B C}+Z \frac{A^{\prime}(1+B-D)+B^{\prime}(1+C-A)}{(1-D)(1-A)-B C}
$$

leading to $Z^{\prime}(0)$ as in Eq. 20, and in Eq. 44 we have used the fact that $Z(0)=1$ (for zero Hamming distance, $u+v=1$ ). Hence, the MIM model with autoregulation will be stable (will not have a fixed-point for $x>0$ ) iff $g^{\prime}(0)<1$, so long as $g(x)$ is concave increasing over the range $[01]$. By inspection of Eq. $42, g(x)$ is concave increasing whenever $Z$ is convex decreasing (since $(1-x)^{K-1}$ is convex decreasing and positive, and taking the product of two convex, decreasing (or increasing), positive functions preserves convexity). This can be ascertained by calculating $Z^{\prime}$ (using Eq. 44) and $Z^{\prime \prime}$ (by differentiating Eq. 45 again with respect to $x$ ) across this range for particular settings of $p, p_{0}, p_{1}, K$, to confirm that $Z^{\prime} \geq 0$ and $Z^{\prime \prime}$ is decreasing. We found this to be the case for all parameter settings used in this paper.

By substituting Eq. 18 into Eq. 4, we have that the independent model with matching activation frequency is stable iff $2 K p^{\prime}\left(1-p^{\prime}\right)<1$, where $p^{\prime}=(1 / M)\left(0.5\left(p_{0}+p_{1}\right)+(M-1) p\right)$. Hence, under the

condition that $Z(x)$ is convex decreasing over $[01]$ (as stated in the proposition), the MIM model with autoregulation is at least as stable as the matching independent model when:

$$
g^{\prime}(0) \leq 2 K p^{\prime}\left(1-p^{\prime}\right)
$$

and the independent model is at least as stable as the MIM model when $g^{\prime}(0) \geq 2 K p^{\prime}\left(1-p^{\prime}\right)$. Eq. 19 follows by substituting Eq. 44 into Eq. 46 and rearranging.

# Appendix D. Comparing Canalyzing and Hierarchical Coregulation rules 

In Kauffman et al. (2004), the notion of a nested canalysing rule is defined, and it is noted that regulatory interactions in many observed transcription networks can be cast in this form. A nested canalysing rule, $f: \mathbb{B}^{K} \rightarrow \mathbb{B}$ is such that, there exists a vector of input values, $\left[I_{1}, I_{2}, \ldots, I_{K}\right] \in \mathbb{B}^{K}$, and output values, $\left[O_{1}, O_{2}, \ldots, O_{K}, O_{K+1}\right]$, where:

$$
f(v)= \begin{cases}O_{1} & \text { if } v(1)=I_{1} \\ O_{2} & \text { if } v(1) \neq I_{1}, v(2)=I_{2} \\ & \ldots \\ O_{K} & \text { if } v(1) \neq I_{1}, v(2) \neq I_{2} \ldots v(K)=I_{K} \\ O_{K+1} & \text { otherwise }\end{cases}
$$

Hence, if the first input takes the canayzing value, $I_{1}$, the output $O_{1}$ is generated regardless of the other inputs; if the first input does not take $I_{1}$, but the second takes its canalyzing value, $I_{2}$, the output is $O_{2}$ regardless; and so on, with $O_{K+1}$ being generated if no input takes its canalyzing value.

Nested canalyzing rules are similar to hierarchical coregulation rules (see Section 5) in that they place a hierarchical structure over the genes involved in the rule. However, where canalyzing rules place a hierarchy over the rule inputs, hierarchical coregulation rules place it over the outputs. A tighter analogy can be drawn as follows: Consider the hierarchical coregulation model as in Section 5, with a total order over the outputs, $\mathrm{Pa}(m)=m-1$. Then, a way to approximate a valid coregulation rule for group $g$ is as follows: First, select $J$ regulators for $C(g, 1)$ (the first node in the group), and select a nested canalyzing rule $f_{1}: \mathbb{B}^{J} \rightarrow \mathbb{B}$ for this node. Second, for node $C(g, 2)$, select $C(g, 1)$ as the first regulator and $J$ further regulators, and select a nested canalysing rule of the form $f_{2}: \mathbb{B}^{J+1} \rightarrow \mathbb{B}$ with $I_{1}=O_{1}=0$, and the remaining parameters arbitrary. This has the effect that, when $C(g, 1)$ is $0, C(g, 2)$ is forced to be 0 also. For node $C(g, 3)$, select nodes $C(g, 1)$ and $C(g, 2)$ as the first two regulators and add $J$ further regulators, and select a nested canalyzing rule with $I_{1}=O_{1}=I_{2}=O_{2}=0$, and the remaining parameters arbitrary, and so on for the remaining nodes $C(g, 4) \ldots C(g, K)$.

The union of the final $J$ regulators for each node in group $g$ can be considered to be the 'proper regulators' of the group, which for convenience we assume do not belong to $g$, and may not all be distinct. If we fix these proper regulators to an arbitrary setting and apply updates to group $g$, after (at most) $M$ time-steps we will reach a valid setting of the nodes in group $g$ (in the sense of the hierarchical coregulation model), such that $\sigma_{C(g, m)}=1$ only if $m=1$, or $\sigma_{C(g, m-1)}=1$. However, if we do not fix the proper regulators as above, but allow all nodes in the network to update at each time-step, we cannot expect this property to hold at any particular time-step. The above suggests that the hierarchical coregulation model can alternatively be viewed in terms of a separation of time-scales: the coregulatory relationships between a rule's outputs can be considered to be regulatory relationships acting at a faster time-scale (instantaneously) compared to those between the rule's inputs and outputs. In this sense, the hierarchical coregulation model is implicitly a multi-scale model.

## Appendix E. Markov Jump Process Simulations for Hierarchical Coregulation Model

As mentioned in Section 5.2, in the Markov Jump process analogues of the independent and hierarchical coregulation models, we let $\mathbf{x} \in(\mathbb{N} \cup\{0\})^{N}$, which can be taken to represent for instance the transcript

count associated with each gene at a given point in time. We write $\mathbf{x}(t)$ for the joint setting of transcript counts at time $t$, where $t \in[0 T]$, and hence varies continuously. As noted, we retain all parameters from the Boolean models, including $N, K, M, p, P(R), P(f)$ for the hierarchical coregulation model. In addition, we introduce the parameters $a, b, d$, where $a$ and $b$ are low and high expected steady-state transcript counts which are used to represent a given gene being on or off respectively, and $d$ is a degradation rate common to all genes. We assume that $a \approx 0$, and that $b>>a$. For our simulations, we take $a=0.1, b=20, d=0.01$.

Each rule in the Boolean model becomes a set of rate equations in the MIP model. In all simulations, we use $K=2$, hence each rule has 2 inputs. Additionally, in the coregulation model, we split each group rule over $M$ outputs into $M$ rules with a single output each (hence, while the group responses are tied by $P(f)$, we do not model joint stochasticity across the group). For a given gene $Y$ then, with regulators $X_{1}$ and $X_{2}$ and update rule $f_{Y}: \mathbb{B}^{2} \rightarrow \mathbb{B}$ derived from the Boolean model, we introduce the following rate equations:

$$
\begin{aligned}
& \emptyset \xrightarrow{k_{00}} Y \quad X_{1} \xrightarrow{k_{10}} X_{1}+Y \quad X_{1}+Y \xrightarrow{k_{10}^{\prime}} X_{1} \\
& Y \xrightarrow{k_{00}^{\prime}} \emptyset \quad X_{2} \xrightarrow{k_{01}} X_{2}+Y \quad X_{2}+Y \xrightarrow{k_{01}^{\prime}} X_{2} \\
& X_{1}+X_{2} \xrightarrow{k_{11}} X_{1}+X_{2}+Y \quad X_{1}+X_{2}+Y \xrightarrow{k_{11}^{\prime}} X_{1}+X_{2}
\end{aligned}
$$

where

$$
\begin{aligned}
& k_{00}=a d\left[f_{00}=0\right]+b d\left[f_{00}=1\right] \\
& k_{10}=(1 / b)(b-a) d\left[f_{10}=1 \wedge f_{00}=0\right] \\
& k_{10}^{\prime}=d((1 / a)-(1 / b))\left[f_{10}=0 \wedge f_{00}=1\right] \\
& k_{01}=(1 / b)(b-a) d\left[f_{01}=1 \wedge f_{00}=0\right] \\
& k_{01}^{\prime}=d((1 / a)-(1 / b))\left[f_{01}=0 \wedge f_{00}=1\right] \\
& k_{11}=\left(1 / b^{2}\right)\left(b r^{\prime}-r\right)\left[f_{11}=1 \wedge\left(r^{\prime} / r\right)<b\right] \\
& k_{11}^{\prime}=\left(1 / b^{2}\right)\left(\left((r / b)-r^{\prime}\right)\left[f_{11}=1 \wedge\left(r^{\prime} / r\right)>b\right]+\left((r / a)-r^{\prime}\right)\left[f_{11}=0\right]\right),
\end{aligned}
$$

and $f_{x y}=f([x y]), r=k_{00}+b k_{10}+b k_{01}$ and $r^{\prime}=d+b k_{10}^{\prime}+b k_{01}^{\prime}$.
Following Wilkinson (2011) and Gillespie (2007), each reaction in Eq. 48 can be associated with a propensity function $\alpha$ whose value is the product of the reactant counts at a given time and the reaction rate constant; hence, numbering the reactions across and then down, $\alpha_{1}(t)=k_{00}, \alpha_{2}(t)=X_{1}(t) k_{10}$, $\alpha_{3}(t)=X_{1}(t) Y(t) k_{10}^{\prime}$, and so on. The probability that reaction $j$ occurs within a small time interval $[t, t+\mathrm{d} t)$ is $\alpha_{j}(t) \mathrm{d} t$, and the model is efficiently simulated using the Gillespie algorithm (Gillespie (2007)).

The parameter settings above are chosen such that if the counts of the regulators $X_{1}, X_{2}$ are fixed at the levels $(0,0),(b, 0),(0, b),(b, b)$, the expected count of $Y$ at steady-state will be $f^{*}(0,0), f^{*}(1,0), f^{*}(0,1), f^{*}(1,1)$ respectively, where $f^{*}(x, y)=a$ if $f(x, y)=0$, and $f^{*}(x, y)=b$ if $f(x, y)=1$. We illustrate by evaluating the expression levels of $Y$ for the XOR function, $f(x, y)=$ $(x \vee y)-(x \wedge y)$. For $X_{1}(t)=0, X_{2}(t)=0$, only reactions 1 and 4 occur, hence $Y$ is produced at rate $a d$ and degraded at rate $Y(t) d$, leading to an expected count at steady-state of $a d / d=a$. For $X_{1}(t)=b, X_{2}(t)=0$, reactions 1,2 and 4 occur ( 3 does not, since the condition $\left[f_{10}=0 \wedge f_{00}=1\right]$ is not satisfied in Eq. 49, and so $k_{10}^{\prime}=0$ ). Reaction 2 occurs at rate $X_{1}(t)(1 / b)(b-a) d=b(1 / b)(b-a) d=b d-a d$, and so the combined rate at which $Y$ is produced from reactions 1 and 2 is $b d-a d+a d=b d$, and the steadystate expected count is $b d / d=b$. For $X_{1}(t)=0, X_{2}(t)=b$, reactions 1,4 and 5 occur, and a similar analysis to $X_{1}(t)=b, X_{2}(t)=0$ leads to an expected count of $b$ for $Y$. For $X_{1}(t)=b, X_{2}(t)=b$, reactions $1,2,4,5$ and 8 occur, with the rates of $1,2,4$ and 5 as above, and reaction 8 occurs at a rate $X_{1}(t) X_{2}(t) Y(t)\left(1 / b^{2}\right)\left((r / a)-r^{\prime}\right)$. The rate of production of $Y$ is therefore $2 b d-2 a d+a d=2 b d-a d$, and writing $\delta(t)$ for the rate of degradation of $Y$ at time $t$, we have:

$$
\begin{aligned}
\delta(t) & =Y(t)\left(d+X_{1}(t) X_{2}(t)\left(1 / b^{2}\right)\left((r / a)-r^{\prime}\right)\right) \\
& =Y(t)\left(d+\left(b^{2}\right)\left(1 / b^{2}\right)\left(((a d+2 b d(b-a) / b) / a)-d\right)\right. \\
& =Y(t)(a d+2 d(b-a)) / a
\end{aligned}
$$

so that the steady-state expectation is $(2 b d-a d) a /(a d+2 d(b-a))=a=f^{*}(1,1)$. The chosen rate constants can similarly be shown to mimic all possible Boolean function settings of $f$ by calculations

similar to those above. For $a \approx 0$, the calculations above will hold approximately when the regulators are expressed at levels $(a, a),(b, a),(a, b),(b, b)$, allowing a network which combines such rules to approximate the dynamics of the associated Boolean model.
