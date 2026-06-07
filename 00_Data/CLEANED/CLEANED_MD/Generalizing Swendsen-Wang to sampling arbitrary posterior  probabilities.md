# Generalizing Swendsen-Wang to Sampling Arbitrary Posterior Probabilities 

Adrian Barbu and Song-Chun Zhu


#### Abstract

Many vision tasks can be formulated as graph partition problems that minimize energy functions. For such problems, the Gibbs sampler [9] provides a general solution but is very slow, while other methods, such as Ncut [24] and graph cuts [4], [22], are computationally effective but only work for specific energy forms [17] and are not generally applicable. In this paper, we present a new inference algorithm that generalizes the Swendsen-Wang method [25] to arbitrary probabilities defined on graph partitions. We begin by computing graph edge weights, based on local image features. Then, the algorithm iterates two steps. 1) Graph clustering: It forms connected components by cutting the edges probabilistically based on their weights. 2) Graph relabeling: It selects one connected component and flips probabilistically, the coloring of all vertices in the component simultaneously. Thus, it realizes the split, merge, and regrouping of a "chunk" of the graph, in contrast to Gibbs sampler that flips a single vertex. We prove that this algorithm simulates ergodic and reversible Markov chain jumps in the space of graph partitions and is applicable to arbitrary posterior probabilities or energy functions defined on graphs. We demonstrate the algorithm on two typical problems in computer vision-image segmentation and stereo vision. Experimentally, we show that it is 100-400 times faster in CPU time than the classical Gibbs sampler and 20-40 times faster then the DDMCMC segmentation algorithm [27]. For stereo, we compare performance with graph cuts and belief propagation. We also show that our algorithm can automatically infer generative models and obtain satisfactory results (better than the graphic cuts or belief propagation) in the same amount of time.


Index Terms-Swendsen-Wang, cluster sampling, Markov chain Monte Carlo, Bayesian inference, image segmentation, stereo matching.

## 1 INTRODUCTION

MANY computer vision tasks have a "what goes with what" component which can be formulated as a graph partition (or coloring) problem. For example, segmentation and grouping in perceptual organization and correspondence in stereo and motion. The common objective of these tasks is to partition various image elements, as vertices in an adjacency graph, into a number of coherent visual structures so that a Bayesian posterior probability or an energy function is optimized.

Under the formulation of graph partition, an increasing number of algorithms from computer science and modern statistical physics have been brought to computer vision and become very influential recently. The first prominent method is the graph spectral analysis [32], such as the normalized cuts [24] and its variants for segmentation and grouping that minimize discriminative energy functions. The second popular method is the minimum-cut [22] and the graph cut [4] which maps energy minimization problems to maximum flow problems and solve them in low order polynomial time. The third method is the generalized belief propagation on graphs [33], which is shown to minimize some approximate energy functions. All three methods are computationally efficient, but they are limited to specific forms of energy functions and, thus, not generally applicable in visual

- The authors are with the Departments of Computer Science and Statistics, University of California, Los Angeles, 8125 Math Science Bldg., Los Angeles, CA 90095. E-mail: abarbu@ucla.edu, sczhu@stat.ucla.edu.
Manuscript received 10 Mar. 2003; revised 1 June 2004; accepted 10 Dec. 2004; published online 13 June 2005.
Recommended for acceptance by A. Rangarajan.
For information on obtaining reprints of this article, please send e-mail to: tpami@computer.org, and reference IEEECS Log Number 118443.
inference. We shall address their limitations in comparison to our method later in this section.

For graph partition problems, classic Markov chain Monte Carlo methods, such as Gibbs sampler [9] or "heat bath" in physics, provide general solutions but experience very slow convergence, especially when adjacent vertices in the graph are strongly coupled, i.e., the coloring of the vertices are interlocked locally. Fig. 2 illustrates such an example where the Gibbs sampler, which flips the color of a single vertex at each step, has to wait exponentially before changing the color of a set of coupled vertices. The speed problem of Gibbs sampler was addressed by the well-celebrated SwendsenWang (SW) method [25], [30]. At each step, the SW algorithm clusters the coupled vertices into connected components, each having the same color, and then flips the color of each connected component jointly. For classic Ising/Potts models [19], a new bounding chain technique [14] has been developed recently, and can diagnose the convergence of SW to its invariant probability, i.e., exact sampling, and, furthermore, the convergence speed (Markov chain mixing time) is polynomial on the graph size $n$. But, the SW method is only valid for Ising/Potts models since the cancellation required in deriving the SW method is not observed in general probabilities or energies. Even worse, SW slows down in the presence of an "external field" (i.e., data or likelihood). More specifically, if one integrates the Potts model as a prior probability with likelihood in Bayesian inference, it could be very slow, as the graph clustering step does not make use of the data. We shall discuss the SW method and its properties in details in Section 3.2.

In this paper, we generalize SW to arbitrary posterior probabilities or energy functions and derive a generic

solution for graph partition. The basic ideas are summarized below.

1. Initialization. Given an adjacency graph, we compute local discriminative probabilities for each edge based on the external field and the prior. For computer vision, local image features or statistical tests are used to obtain these edge weights. Then, the algorithm iterates the following two steps.
2. Graph clustering. Given a current partition (coloring), it removes all edges between vertices of different colors. Then, each of the remaining edges connecting adjacent vertices of the same color is turned on/off according to its weight. If the discriminative probabilities are informative, then the edges at object boundaries have a high chance to be turned off. Thus, it obtains a number of connected components (subgraphs) each having the same color and, usually, these connected components correspond to strongly coupled vertices that stand for parts of objects in the image (see Fig. 4). We define a "Swendsen-Wang cut" for each connected component as the set of edges which connect this component with its neighboring vertices of the same color. In other words, the edges in a Swendsen-Wang cut are turned off probabilistically. These connected components can be regarded as samples from an approximation of the posterior with a Potts model, and they will be accepted by the posterior probability in the next step.
3. Graph flipping. It selects one (or multiple) connected component and flips, with a probability driven by the posterior, the coloring of all vertices in the selected component(s) simultaneously. Thus, it realizes the split, merge, and regrouping of a "chunk" of the graph, in contrast to the Gibbs sampler that flips a single vertex. The flipping procedure can automatically change the number of colors and, thus, is more general than the original SW method that works for a fixed number of colors in the Potts model.
We shall show that the new algorithm simulates ergodic and reversible Markov chain jumps in the finite space of all possible graph partitions. The algorithm is valid for sampling arbitrary posterior probability or energy functions.

Our new algorithm mainly makes three contributions. First, we generalize the SW method from the perspective of Metropolis-Hastings method and derive a simple and analytic formula for the acceptance probability in a reversible Metropolis-Hastings step. This formula (see Theorem 2) is expressed in terms of the product of the discriminative probabilities on the edges (often a very small number) in the Swendsen-Wang cuts. Second, we compute the discriminative probabilities on edges from the input image ("external field" in a physics term). We observe that empirically these discriminative probabilities make the connected components more effective in comparison to a uniform probability in the original SW method. This is in a similar spirit to data-driven Markov chain Monte Carlo [27]. Third, we present various versions of the algorithm. One of the variants is a direct generalization of the Gibbs sampler. It flips the coloring of a connected component according to a conditional probability with a rectifying factor and the flip is accepted with probability one.

We demonstrate the algorithm on two typical problems in computer vision-image segmentation and stereo vision.

In image segmentation, we choose a generative image representation with three classes of image models. It works 100-400 times faster in CPU time than the classic Gibbs sampler and obtains good results in 3-30 seconds on a PC. In the stereo matching problem, we adopt the energy function used in graph cut [4] and the benchmark in [23] for comparison. It obtains good results (better than belief propagation [26]) in 6-10 minutes on a $400 \times 290$ image and is slower than graph cuts. The computing speed certainly depends on the discriminative probabilities in the problem domain. For optimization problems, our method still uses simulated annealing, but at a much quicker schedule than the Gibbs sampler ( 15 sweeps as opposed to 5,000 sweeps) and we do not have to start with a high initial temperature. The algorithm can therefore start with good initial solutions to speed-up convergence.

We now compare our method with other graph partition algorithms in computer vision.

First, it is distinct from the graph spectral analysis [32], such as normalized cuts [24], [32]. We argue that the discriminative energies, used in Ncuts and many other discriminative grouping and clustering algorithms [15], [13], [21], [8], have difficulties in expressing global visual patterns, such as shading effects, perspective projection effects, contour closure, etc. Furthermore, natural images contain very diverse visual structures which are "coherent" in many different ways, there is no single discriminative criterion that is generally applicable to correctly partition all the visual structures in images [8]. For example, a criterion that prefers compact regions will break elongated curve patterns. Thus, we need a generative and Bayesian formulation incorporating a number of diverse and competing image models. Each family of models explains how a pattern is generated and stands for a coherence criterion. For example, seven families of models are used for texture, color, shading, and clutter regions in image segmentation [27]. Our algorithm uses the Ncut type discriminative probabilities on edges, but only for making proposals, which are accepted or rejected by the Bayesian posterior probability that incorporates many families of image models and global prior knowledge.

Second, although the graph cut and minimum-cut algorithms [22], [17] are effective in minimizing some energy functions, it is shown [17] that only very limited classes of energy functions can be mapped into the maximum flow problems. For example, so far these methods have not been applicable to generative models with multiple classes of image models.

Third, our method is an addition to the recent data-driven Markov chain Monte Carlo (DDMCMC) algorithm for segmentation [27] and parsing [28] which solves Bayesian inference by mixing a number of reversible jumps. The jumps are divided into two types. Type I solves the "what is what" subtasks, such as model selection, switching, and fitting. The DDMCMC algorithm computes discriminative models, such as color and texture clustering, and expresses them in the form of nonparametric probabilities to drive these jumps. Type II solves the "what goes with what" subtasks such as grouping, segmentation, and correspondence. Our Swend-sen-Wang cut algorithm in this paper improves the Type II jumps in both theoretical formulation and computational speed. It can speed up the DDMCMC algorithm [27] by 2040 times for segmentation.

In this paper, we shall focus on the Type II reversible jumps in the graph partition space. We omit discussion on the model spaces for Type I jumps, which are referred to [27].

![img-0.jpeg](img-0.jpeg)

Fig. 1. Image segmentation as graph partition. (a) Input image. (b) Atomic regions by Canny edge detection followed by edge tracing and contour closing, each being a vertex in the graph $G_{o}$. (c) Segmentation result.

The paper is organized as follows: We present the Bayesian formulation for graph partition in Section 2. Then, we discuss the difficulties in sampling the graph partitions and introduce the original SW algorithm in Section 3. Section 4 presents the new Swendsen-Wang cut algorithm and its variants. Then, we show two groups of experiments in Section 5-image segmentation and stereo matching. Finally, Section 6 concludes the paper with discussions on the advanced topics on extending and analyzing the Swendsen-Wang cuts.

## 2 BAYESIAN FORMULATION OF GRAPH PARTITION

### 2.1 Bayesian Formulation

We consider an adjacency graph $G_{o}=<V, E_{o}>$, where $V=\left\{v_{1}, v_{2}, \ldots, v_{N}\right\}$ is the set of nodes that need to be partitioned, such as atoms, pixels, edge elements, image primitives, or atomic regions with nearly constant intensities and $E_{o}$ is a set of edges connecting neighboring nodes. An $n$-partition of the graph is denoted by

$$
\pi_{n}=\left(V_{1}, V_{2}, \ldots V_{n}\right), \quad \cup_{i=1}^{n} V_{i}=V, V_{i} \cap V_{j}=\emptyset, \forall i \neq j
$$

Since visual structures are coherent in many different ways, each subset $V_{i}, i=1,2, \ldots, n$ is assigned a color $\mathbf{c}_{i}$ which represents the model, usually consisting of a type (constant, spline, etc.) and some parameters. Our objective is to compute the following world representation $W$ from the input $\mathbf{I}$,

$$
W=\left(n, \pi_{n}, \mathbf{c}_{1}, \ldots, \mathbf{c}_{n}\right)
$$

This becomes an optimization problem, either maximizing the Bayesian posterior probability or minimizing an energy in a solution space $\Omega$,

$$
W^{*}=\arg \max _{W \in \Omega} p(\mathbf{I} \mid W) p(W), \quad \text { or } \quad W^{*}=\arg \min _{W \in \Omega} \varepsilon(W \mid \mathbf{I})
$$

We choose two typical vision problems as examples in this paper. We denote by $\mathbf{I}_{v}$ the image attributes on vertex $v$, and $\mathbf{I}=\mathbf{I}_{V}$ the attributes for the set $V$.

The first example is image segmentation, as shown in Fig. 1. Each vertex $v$ is an atomic region with nearly constant intensity, and $\mathbf{I}_{v}$ is its intensity. A partitioned subset $V_{i}$ corresponds to a coherent region $R_{i}$ with model $\mathbf{c}_{i}=\left(\ell_{i}, \theta_{i}\right)$, where $\ell_{i}$ is the type of image model and $\theta_{i}$ the model parameters. We adopt three types of simple image models and a prior probability in Section 5.1. Usually, these models should be color, texture, and shading, as implemented in DDMCMC [27]. Thus, the likelihood for $\mathbf{I}_{V_{i}}$ is
$p\left(\mathbf{I}_{V_{i}} ; \ell_{i}, \theta_{i}\right)$, where $\theta_{i}$ may have different dimensions for different types of models.

The second example is stereo matching. The graph $G_{o}$ is the pixel lattice, $\mathbf{I}_{v}=\left(\mathbf{I}_{v}^{\prime}, \mathbf{I}_{v}^{\prime}\right)$ is the left and right image intensity and $\mathbf{c}_{i}$ is the disparity of $V_{i}$, discretized along the epipolar line as $\mathbf{c}_{i} \in\left\{0, \ldots, d_{\max }\right\}$. The energy function is formulated in Section 5.3.

In our recent work [2], we have applied the same SW-cuts algorithm to motion where $\mathbf{c}_{i}=\left(u_{i}, v_{i}\right)$ is the motion velocity, or even $\mathbf{c}_{i}$ can be a vector that includes both motion and image segmentation. Our algorithm has also been used for curve grouping.

### 2.2 Solution Space and Markov Chain Jumps

In this section, we consider the structure of the solution space and the necessary Markov chain steps for optimization in this space. Then, we present the place of graph partition in this optimization.

For $W$ in (2), we denote by $\Omega_{\pi_{n}} \ni \pi_{n}$ the space of all possible $n$-partitions $\pi_{n}$ of $V, \Omega_{\ell} \ni \ell_{i}$ the set of types of image models, and $\Omega_{\theta_{i}} \ni \theta_{i}$ the model parameter space (family) for type $\ell_{i}$. Thus, the solution space for $W$ is

$$
\Omega=\cup_{n=1}^{|V|}\left\{\Omega_{\pi_{n}} \times \Omega_{\ell}^{n} \times \Omega_{\theta_{i}} \times \cdots \times \Omega_{\theta_{n}}\right\}
$$

The factorization of the space corresponds to the two types of moves necessary for exploring the entire space. ${ }^{1}$

1. Type I is "what is what" moves for selecting the model $\ell_{i} \in \Omega_{\ell}$ and fitting the model parameters $\theta_{i} \in \Omega_{\theta_{i}}$ for $V_{i}, i=1,2, \ldots, n$. Model fitting is omitted in the stereo matching experiment. We usually can quantize the model spaces so that they become finite.
2. Type II is "what goes with what" moves for grouping, segmentation, and correspondence in the partition space $\Omega_{\pi}=\cup_{n=1}^{|V|} \Omega_{\pi_{n}}$, which is a finite space.
The two types of moves are tightly coupled and we implement them by a number of reversible jumps which simulate Markov chain searches in the space $\Omega$. The Markov chain starts with an initial solution $W_{o}$ and is designed to have a unique invariant (stationary) probability $p(W \mid \mathbf{I})$. Suppose we denote the state probability of the Markov chain at time $t$ by $p_{t}\left(W_{o}, W\right)$. A classic measure of convergence is the total variation,
3. It is interesting to note that the human brain mapping study [29] shows that the recognition task (Type I) is handled by a dorsal stream and the spatial vision (Type II) is processed by a ventral stream.

![img-1.jpeg](img-1.jpeg)

Fig. 2. Difficulty in sampling the Ising and Potts models.

$$
\left\|p_{t}\left(W_{o}, W\right)-p(W \mid \mathbf{I})\right\|_{\mathrm{TV}}=\frac{1}{2} \sum_{W \in \Omega}\left|p_{t}\left(W_{o}, W\right)-p(W \mid \mathbf{I})\right|
$$

A measure of the speed of an algorithm $\mathcal{A}$ is the mixing rate, that is the minimum time for the Markov chain to come close to the stationary probability for any $W_{o}$,

$$
\tau_{\mathcal{A}}=\max _{W_{o}} \min \left\{t:\left\|p_{t}\left(W_{o}, W\right)-p(W \mid \mathbf{I})\right\|_{\mathrm{TV}} \leq \epsilon\right\}
$$

Usually, $\tau_{\mathcal{A}}=\tau_{\mathcal{A}}\left(\epsilon,\left|G_{o}\right|\right)$ is a function of $\frac{1}{\epsilon}$ and the graph size $\left|G_{o}\right|$, i.e., number of vertices and edges. The algorithm $\mathcal{A}$ is said to be rapid mixing if $\tau_{\mathcal{A}}$ is polynomial or logarithmic.

In this paper, we shall only study the Type II moves and omit the Type I moves which have been discussed in the DDMCMC algorithm [27].

## 3 Gibbs Sampler, Swendsen-Wang Method, and Their Limitations

In this section, we discuss the Gibbs sampler and the original Swendsen-Wang algorithm for graph partition, to set the background.

### 3.1 The Difficulty of Graph Partition by the Gibbs Sampler

The difficulty of sampling in the partition space $\Omega_{s}$ is well reflected in a simple Ising and Potts model [19], which are sometimes used in vision as prior models. Fig. 2 shows a string of spins whose labels (color) $\mathbf{c}$ can be +1 (up) and -1 (down). A Potts model may have $Q \geq 3$ colors, $\mathbf{c} \in\{1,2, \ldots, Q\}$. The Ising/Potts model is

$$
p\left(\pi_{n}\right)=\frac{1}{Z} \exp \left\{\beta \sum_{<s, t>\in E_{o}} \mathbf{1}\left(\mathbf{c}_{s}=\mathbf{c}_{t}\right)\right\}, \quad \beta>0
$$

where $\mathbf{1}\left(\mathbf{c}_{s}=\mathbf{c}_{t}\right)=1$ if $\mathbf{c}_{s}=\mathbf{c}_{t}$ for two adjacent vertices $s, t$ otherwise it is zero. Obviously, the highest probability is achieved when all vertices have the same label. In a best visiting scheme, suppose a single site update algorithm, like the Gibbs sampler, flips the -1 spins at the two "cracks" in Fig. 2. The probability for flipping each spin from -1 to +1 is $p_{o}=1 / 2$. Thus, to flip a string of $k$ spins $(k=9$ in Fig. 2) from -1 to +1 successfully, the expected number of steps is $\frac{1}{\left(1 / p_{o}\right)^{2}-2^{k}}$. This is exponential waiting and is typical for general graph partition! Intuitively, it will be desirable to flip a big set of vertices that have the same color at each step. Of course, we need to ensure that such moves still keep $p\left(\pi_{n}\right)$ as its stationary probability. This is what the Swendsen-Wang method does.

### 3.2 Swendsen-Wang on Potts Models and Theoretical Results

There are many ways to interpret the SW algorithm, including random cluster model, auxiliary variables [6] and slice sampling and decoupling [12]. In this paper, we interpret the SW method as a Metropolis-Hastings step and
our interpretation leads to generalizing it to arbitrary probabilities in Section 4.

Consider a Potts model in (7) on a 2D lattice. Fig. 3 shows two partition states $\pi_{A}$ and $\pi_{B}$ with $\pi_{A}=\left(V_{o} \cup V_{1}, V_{2}, \cdots\right)$ and $\pi_{B}=\left(V_{1}, V_{o} \cup V_{2}, \cdots\right)$, which differ by the labels of the vertices $V_{o}$ inside the center window.

The SW algorithm realizes a reversible move between $\pi_{A}$ and $\pi_{B}$ in a single step. From state $\pi_{A}$, the SW algorithm proceeds in the following way:

1. Any edge $e=\langle s, t\rangle \in E_{o}$ is removed if $\mathbf{c}_{s} \neq \mathbf{c}_{t}$. If $\mathbf{c}_{s}=\mathbf{c}_{t}$, then $e=\langle s, t\rangle$ is turned "on" with a probability $q_{o}=1-e^{-\beta}$, otherwise, it is turned "off," i.e., removed. This yields a number of connected components, each being a subset of vertices of the same color.
2. It randomly selects a connected component $V_{o}$ of the resulting graph (see Fig. 3a). The dark edges in $V_{0}$ remain on, the other edges have been turned off.
3. It chooses a label $\mathbf{c} \in\{1, \ldots, Q\}$ for $V_{o}$ with uniform probability.
In the example of Fig. 3, $V_{o}$ change color from black to white and we obtain partition state $\pi_{B}$ in Fig. 3b. Reversely, at state $\pi_{B}$, we will have a chance to select $V_{o}$ and flip it to black color and this way return to $\pi_{A}$.

In this paper, the Swendsen-Wang cuts at $\pi_{A}$ and $\pi_{B}$ are the sets of edges connecting $V_{o}$ to $V_{1}$ and $V_{2}$, respectively, marked by the crosses in Fig. 3.

$$
\begin{aligned}
& \mathcal{C}_{A}=\mathcal{C}\left(V_{o}, V_{1}\right)=\left\{(s, t): s \in V_{o}, t \in V_{1}\right\} \\
& \mathcal{C}_{B}=\mathcal{C}\left(V_{o}, V_{2}\right)=\left\{(s, t): s \in V_{o}, t \in V_{2}\right\}
\end{aligned}
$$

In state $\pi_{A}$, there is a combinatorial number of ways to make $V_{0}$ a connected component, but, in all cases, the edges in $\mathcal{C}_{A}$ must have been cut probabilistically. Similarly, in state $\pi_{B}$, the edges in $\mathcal{C}_{B}$ must be turned off in order for $V_{o}$ to be a connected component.
![img-2.jpeg](img-2.jpeg)

Fig. 3. The SW algorithm flips the color of a set of vertices $V_{o}$ in one step for the Ising/Potts models. The set of edges marked with crosses is called the Swendsen-Wang cut.

We look at the moves between states $\pi_{A}$ and $\pi_{B}$ from the perspective of the Metropolis-Hastings method [18]. Though it is computationally difficult to compute the proposal probabilities $q\left(\pi_{A} \rightarrow \pi_{B}\right)$ and $q\left(\pi_{B} \rightarrow \pi_{A}\right)$, one can compute their ratio easily through cancellation.

$$
\frac{q\left(\pi_{A} \rightarrow \pi_{B}\right)}{q\left(\pi_{B} \rightarrow \pi_{A}\right)}=\frac{\left(1-q_{o}\right)^{\left|\mathcal{C}_{A}\right|}}{\left(1-q_{o}\right)^{\left|\mathcal{C}_{B}\right|}}=\left(1-q_{o}\right)^{\left|\mathcal{C}_{A}\right|-\left|\mathcal{C}_{B}\right|}
$$

$\mathcal{C}_{A}$ is the cardinality of set $\mathcal{C}_{A}$. Remarkably the probability ratio for $p\left(\pi_{A}\right) / p\left(\pi_{B}\right)$ for the Potts model is also decided by the Swendsen-Wang cuts

$$
\frac{p\left(\pi_{A}\right)}{p\left(\pi_{B}\right)}=\frac{e^{-\beta\left|\mathcal{C}_{B}\right|}}{e^{-\beta\left|\mathcal{C}_{A}\right|}}=e^{\beta\left(\left|C_{A}\right|-\left|C_{B}\right|\right)}
$$

The acceptance probability for the move from $\pi_{A}$ to $\pi_{B}$ is

$$
\begin{aligned}
\alpha\left(\pi_{A} \rightarrow \pi_{B}\right) & =\min \left(1, \frac{q\left(\pi_{B} \rightarrow \pi_{A}\right)}{q\left(\pi_{A} \rightarrow \pi_{B}\right)} \frac{p\left(\pi_{B}\right)}{p\left(\pi_{A}\right)}\right) \\
& =\left(\frac{e^{-\beta}}{1-q_{o}}\right)^{\left|\mathcal{C}_{A}\right|-\left|\mathcal{C}_{B}\right|}=1
\end{aligned}
$$

if we take $q_{o}=1-e^{-\beta}$, so the proposal from $\pi_{A}$ to $\pi_{B}$ is always accepted. So, once $V_{o}$ is selected, its new color is picked at random without having to go through the MetropolisHastings step due to the cancelation! As $\beta \propto \frac{1}{\beta}$ is the inverse of the "temperature" in the Potts models, at lower temperature, $q_{o} \rightarrow 1$ and SW flips a larger patch each time.

For Potts models in (7), Huber [14] developed a new bounding chain technique [14] which can diagnose the convergence of SW, i.e., exact sampling or perfect sampling [20]. The number of steps in reaching exact sampling is in the order of $O\left(\log \left|E_{o}\right|\right)$ for temperature far below and far above the critical temperature. Using a path coupling technique, Cooper and Frieze [5] have shown that the mixing time $\tau$ (see (6)) is polynomial [5] if each vertex in graph $G_{o}$ is connected to $O(1)$ number of neighbors, i.e., the connectivity of each vertex does not grow with the size of $V$. This is usually observed in vision problems, such as the lattice. The mixing time becomes exponential at a worst case when $G_{o}$ is fully connected [10]. Such a case may never occur in vision problems.

However, the excitement of the SW algorithm has been limited for the following reasons:

1. It is restricted to Ising and Potts models, while posterior probabilities in vision tasks are of much more complex forms.
2. It becomes very slow even for the Potts models in the presence of external fields (data). As $q_{o}$ is a constant, it does not utilize the input data in clustering the connected components.
3. It assumes the number of labels $n$ is fixed. The Markov chain does not create new labels in cases where $n$ is unknown (in vision, usually the number of models is unknown).
In the next section, we overcome these limitations and extend SW to arbitrary probabilities.

## 4 Graph Partition by Swendsen-Wang Cuts

### 4.1 Discriminative Probabilities on Edges

Before running the reversible jumps, we augment the adjacency graph $G_{o}=<V, E_{o}>$ with discriminative
probabilities in an initial stage. Partition samples obtained using these probabilities will be used in the next section as proposals for the full posterior probability. For any vertex $v \in V$, we extract a number of features $F(v)=\left(F_{1}(v), F_{2}(v), \ldots, F_{n}(v)\right)$ and for each edge $e=<s, t>\in E_{o}$, we assign a binary random variable $\mu_{e} \in\{$ on, off $\} . \mu_{e}$ indicates whether the edge is turned on or off. Then, we compute a discriminative probability $q_{e}=q\left(\mu_{e}=\operatorname{on}\left|F(s), F(t)\right)\right.$ based on local features $F(s)$ and $F(t)$.

Take the adjacency graph in Fig. 1 as an example. For each atomic region (vertex in $G_{o}$ ), we compute a 15 -bin intensity histogram $h$ normalized to 1 . For each edge $e=\left\langle v_{i}, v_{j}\right\rangle$, we define

$$
q_{e}=p\left(\mu_{e}=\operatorname{on}\left|h_{i}, h_{j}\right)=e^{-\left(K L\left(h_{i}\right) \mid h_{j}\right)+K L\left(h_{j} \mid h_{i}\right)\right) T / 2}\right.
$$

where $K L()$ is the Kullback-Leibler divergence between the two histograms and $T$ is a temperature factor. Usually, $q_{e}$ should be close to zero for $e$ on object boundary. Suppose we turn on the edges independently according to $q_{e}, e \in E_{o}$, we obtain a sparse graph $G=\langle V, E\rangle$ with probability

$$
q(E)=\prod_{e \in E} q_{e} \prod_{e \in E_{o} \backslash E}\left(1-q_{e}\right)
$$

Then, $G$ consists of a number connected components. Fig. 4 shows some examples of $G$ for $G_{o}$ in Fig. 1. Each region of uniform gray level is a connected component that consists of a number of atomic regions. We show three random partitions sampled according to $q(E)$ for four temperatures $T=1,2,4,8$. At a reasonable temperature, various parts of the cheetah are obtained, legs, body, and tail, as connected components, which are then proposed as candidates for partition in the reversible jumps.

This example shows that the discriminative models are good heuristics for partition. However, these partitions are limited by the local features. More complex posterior probabilities with global generative models are needed to accept these proposals and this is done next.

### 4.2 Swendsen-Wang Cuts and Its Variants

The Swendsen-Wang cut algorithm engages three types of graphs shown in Fig. 5. It starts with an adjacency graph $G_{o}=<V, E_{o}>$ (Fig. 5a). At each time step, we have a partition $\pi=\left(V_{1}, \ldots, V_{n}\right)$ which assigns a color to each vertex $\mathbf{c}_{v}=\ell$ for $v \in V_{\ell}, \ell=1,2, \ldots, n$ and we obtain a graph $G(\pi)=\langle V, E(\pi)\rangle$ (Fig. 5b) with $E(\pi)=\left\{e=<s, t>\left: \mathbf{c}_{s}=\mathbf{c}_{t}\right\}\right.$. Then, each edge $e \in E(\pi)$ is turned off with probability $1-q_{e}$ independently and we obtain a sparse graph $C P$ with a number of connected components.

Now, we present a first version of the Swendsen-Wang cut algorithm.

## Swendsen-Wang Cut: SWC-1

Input: $G_{o}=<V, E_{o}>, q_{e}, \forall e \in E_{o}$, and posterior $p(W \mid \mathbf{I})$. Output: Samples $W \sim p(W \mid \mathbf{I})$.

1. Initialize a partition $\pi$ by random clustering (see Fig. 4)
2. Repeat, for current state $\pi=\left(V_{1}, V_{2}, \ldots, V_{n}\right)$.
3. For $e \in E(\pi)$, turn $\mu_{e}=$ off with probability $1-q_{e}$.
4. $\quad V_{\ell}=\left(V_{\ell 1}, \ldots, V_{\ell n_{\ell}}\right)$ is divided into $n_{\ell}$ connected components for $\ell=1,2, \ldots, n$.
5. Collect all the connected components in set

$$
C P=\left\{V_{\ell i}: \ell=1, \ldots, n, i=1, \ldots, n_{\ell}\right\}
$$

![img-3.jpeg](img-3.jpeg)

Fig. 4. Random clustering of the adjacency graph using independent discriminative models on edges. Each uniform region is a connected component.
![img-4.jpeg](img-4.jpeg)

Fig. 5. Three stages of graphs in the algorithm. (a) Adjacency graph $G_{o}$, (b) graph $G$ for current partition (coloring) $\pi$, and (c) connected components $C P$ by turning off some edges in $G$.
6. Select a connected component $V_{o} \in C P$ with prob. $q\left(V_{o} \mid C P\right)$, say $V_{o} \subset V_{t}$.
(Usually $q\left(V_{o} \mid C P\right)=\frac{1}{\not C P}$ is uniform, Fig. 6a is an example of $V_{o}$ in partition $\pi=\pi_{A}$ ).
7. Propose to assign $V_{o}$ a new label $\mathbf{c}_{V_{o}}=\ell^{\prime}$ with a probability $q\left(\ell^{\prime} \mid V_{o}, \pi\right)$, thus obtain $\pi^{\prime}\left(\pi^{\prime}=\pi_{B}\right.$ is in Fig. 6b if $V_{0}$ is merged to an existing color $V_{2}$, or $\pi^{\prime}=\pi_{C}$ is in Fig. 6c if $V_{o}$ is assigned a new color).
8. Accept the proposal with probability $\alpha\left(\pi \rightarrow \pi^{\prime}\right)$ defined in Theorem 2.
The proposal probability $q\left(l^{\prime} \mid V_{o}, \pi\right)$ can be uniform, or better, dependent on the similarity of $V_{o}$ with $V_{l^{\prime}}$. At each step, model switching and fitting (Type I jumps) are performed deterministically or sampled from some proposal probabilities (see later in this section).

In the above algorithm, let $V_{o} \subseteq V_{t}$ in $\pi$ and $V_{o} \subseteq V_{l^{\prime}}$ in $\pi^{\prime}$. The move $\pi \rightarrow \pi^{\prime}$ can realize three types of moves depending on the choice of the new color of $V_{o}$. Thus, the number of colors $n$ will be decided automatically.

1. Regrouping: $V_{o} \subset V_{t}$ is split from $V_{t}$ and merged into an existing color $V_{l^{\prime}}$. The number of colors $n$ is unchanged. E.g. $\pi_{A} \leftrightarrow \pi_{B}$ in Fig. 6. When $V_{t}$ and $V_{l^{\prime}}$ are adjacent, this is, in fact, a discrete version of the boundary evolution, like region competition [34].
2. Splitting: $V_{o} \subset V_{t}$ is split into a new color $\ell^{\prime}=n+1$. For example, $\pi_{A} \rightarrow \pi_{C}$ in Fig. 6.
3. Merging: $V_{o}=V_{t}$ and is merged into an existing color. For example, $\pi_{C} \rightarrow \pi_{A}$ in Fig. 6.
The second version of the algorithm differs only in the way it selects the set $V_{o}$. Instead of sampling all the edges in a current partition, it starts from a single vertex (seed) $v$ and grows into a connected component $V_{o}$.

## Swendsen-Wang Cuts: SWC-2

1. Repeat, for current state $\pi=\left(V_{1}, V_{2}, \ldots, V_{n}\right)$,
2. Select a seed vertex $v$, say $v \in V_{t}$ in $\pi$. Set $V_{o} \leftarrow\{v\}$, $\mathcal{C} \leftarrow \emptyset$,
3. Repeat until $\mathcal{C} \cap \mathcal{C}\left(V_{o}, V_{t} \backslash V_{o}\right)=\mathcal{C}\left(V_{o}, V_{t} \backslash V_{o}\right)$,
4. For any $e=\langle s, t\rangle \in \mathcal{C}\left(V_{o}, V_{t} \backslash V_{o}\right)$,
$s \in V_{o}, t \in V_{t} \backslash V_{o}$.
5. Turn $\mu_{e}=$ on with probability $q_{e}$, else
$\mu_{e}=$ off,
6. If $\mu_{e}=$ on, set $V_{o} \leftarrow V_{o} \cup\{t\}$, else $\mathcal{C} \leftarrow \mathcal{C} \cup\{e\}$.
7. Propose to assign $V_{o}$ a new label $\ell^{\prime}$ with prob. $q\left(\mathbf{c}_{V_{o}}=\ell^{\prime} \mid V_{o}, \pi\right)$.
8. Accept the move with probability $\alpha\left(\pi \rightarrow \pi^{\prime}\right)$ defined in Theorem 2.
Now, we compute the acceptance probability $\alpha\left(\pi \rightarrow \pi^{\prime}\right)$ in SWC-1 and SWC-2.

![img-5.jpeg](img-5.jpeg)

Fig. 6. A reversible move between three partition states $\pi_{A}, \pi_{B}, \pi_{C}$ which differ only in the color of $V_{0}$. The vertices connected by thick edges form a connected component. The thin lines marked with crosses are edges in the SW-cuts. (a) A CP of state $\pi_{A}$, (b) A CP of state $\pi_{B}$. (c) A CP of state $\pi_{C}$.

We start with computing the probability ratio for selecting $V_{o}$ in $\pi \rightarrow \pi^{\prime}$ and $\pi^{\prime} \rightarrow \pi$.
Theorem 1. Let $\pi$ and $\pi^{\prime}$ be a pair of reversible partition states which differ in the coloring of $V_{o}$, with $V_{o} \subseteq V_{\ell}$ in $\pi$ and $V_{o} \subseteq V_{\ell^{\prime}}$ in $\pi^{\prime}$, then

$$
\frac{q\left(V_{o} \mid \pi\right)}{q\left(V_{o} \mid \pi^{\prime}\right)}=\frac{\prod_{\epsilon \in \mathcal{C}\left(V_{o}, V_{\ell} \backslash V_{o}\right)}\left(1-q_{\epsilon}\right)}{\prod_{\epsilon \in \mathcal{C}\left(V_{o}, V_{\ell^{\prime}} \backslash V_{o}\right)}\left(1-q_{\epsilon}\right)}
$$

$\prod_{\epsilon \in \mathcal{C}\left(V_{o}, V_{\ell} \backslash V_{o}\right)}\left(1-q_{\epsilon}\right)=1$ if $V_{\ell} \backslash V_{o}=\emptyset$.
Proof. See Appendix A. This is the most important step in obtaining the acceptance probability. It states the fact that although there are a combinatorial number of ways for selecting $V_{o}$ in $\pi$ and $\pi^{\prime}$, their probability ratio is simple due to cancellations.
Theorem 2. In the above notation, the acceptance probability for move $\pi \rightarrow \pi^{\prime}$

$$
\begin{aligned}
& \alpha\left(\pi \rightarrow \pi^{\prime}\right)= \\
& \min \left(1, \frac{\prod_{\epsilon \in \mathcal{C}\left(V_{o}, V_{\ell} \backslash V_{o}\right)}\left(1-q_{\epsilon}\right)}{\prod_{\epsilon \in \mathcal{C}\left(V_{o}, V_{\ell}-V_{o}\right)}\left(1-q_{\epsilon}\right)} \cdot \frac{q\left(\mathbf{c}_{V_{o}}=\ell \mid V_{o}, \pi^{\prime}\right)}{q\left(\mathbf{c}_{V_{o}}=\ell^{\prime} \mid V_{o}, \pi\right)} \cdot \frac{p\left(\pi^{\prime} \mid \mathbf{I}\right)}{p(\pi \mid \mathbf{I})}\right)
\end{aligned}
$$

Proof. By Metropolis-Hastings method [18], the acceptance probability is,

$$
\alpha\left(\pi \rightarrow \pi^{\prime}\right)=\min \left(1, \frac{q\left(\pi^{\prime} \rightarrow \pi\right)}{q\left(\pi \rightarrow \pi^{\prime}\right)} \frac{p\left(\pi^{\prime} \mid \mathbf{I}\right)}{p(\pi \mid \mathbf{I})}\right)
$$

For the regrouping case (see $\pi_{A} \leftrightarrow \pi_{B}$ in Fig. 6), there is only one path moving between the two states $\pi$ and $\pi^{\prime}$, i.e., selecting and flipping $V_{o}$. Therefore,

$$
\frac{q\left(\pi^{\prime} \rightarrow \pi\right)}{q\left(\pi \rightarrow \pi^{\prime}\right)}=\frac{q\left(V_{o} \mid \pi^{\prime}\right)}{q\left(V_{o} \mid \pi\right)} \cdot \frac{q\left(\mathbf{c}_{V_{o}}=\ell \mid V_{o}, \pi^{\prime}\right)}{q\left(\mathbf{c}_{V_{o}}=\ell^{\prime} \mid V_{o}, \pi\right)}
$$

The conclusion follows straight from Theorem 1. For the splitting and merging case (see $\pi_{A} \leftrightarrow \pi_{C}$ in Fig. 6), there are two paths. We put the proof in Appendix B for clarity.
As the partition space $\Omega_{\pi} \ni \pi$ is finite, the Markov chain in SWC-1, 2 is then ergodic following the observation that there is a nonzero probability for any node $v \in V$ to be chosen as $V_{o}$ and assigned a new color. Then, the Markov chain can move from a partition to any other partition with nonzero probability in $|V|$ steps.

To include the Type I moves for model selection and fitting, we augment the move from two partitions $\pi \leftrightarrow \pi^{\prime}$ to two states $W \leftrightarrow W^{\prime}$. In state $W$, the set $V_{\ell} \supseteq V_{o}$ has image
model $\theta_{\ell}$ while the set $V_{\ell^{\prime}}$ has image model $\theta_{\ell^{\prime}}$. In state $W^{\prime}$, $V_{o}$ is split from $V_{\ell}$ and merged into $V_{\ell^{\prime}}$. The set $V_{\ell} \backslash V_{o}$ has a new model $\theta_{\ell}^{\prime}$, and the set $V_{\ell^{\prime}} \cup V_{o}$ has model $\theta_{\ell^{\prime}}^{\prime}$, obtained by sampling from proposals $q\left(\theta_{\ell}^{\prime} \mid \mathbf{I}_{V_{\ell} \backslash V_{o}}\right), q\left(\theta_{\ell^{\prime}}^{\prime} \mid \mathbf{I}_{V_{\ell^{\prime}}, V_{o}}\right)$, respectively. Then, the acceptance probability is

$$
\begin{aligned}
& \alpha\left(W \rightarrow W^{\prime}\right)= \\
& \min \left(1, \frac{q\left(\theta_{\ell} \mid \mathbf{I}_{V_{o}}\right) q\left(\theta_{\ell^{\prime}} \mid \mathbf{I}_{V_{\ell^{\prime}}}\right)}{q\left(\theta_{\ell}^{\prime} \mid \mathbf{I}_{V_{\ell} \backslash V_{o}}\right) q\left(\theta_{\ell^{\prime}}^{\prime} \mid \mathbf{I}_{V_{\ell^{\prime}}, V_{o}}\right)} \cdot \frac{q\left(\pi^{\prime} \rightarrow \pi\right)}{q\left(\pi \rightarrow \pi^{\prime}\right)} \cdot \frac{p\left(W^{\prime} \mid \mathbf{I}\right)}{p(W \mid \mathbf{I})}\right)
\end{aligned}
$$

The dimensions of the model parameters are matched in the ratio. The proposal probabilities $q\left(\theta \mid \mathbf{I}_{V_{\ell}}\right)$ for any set $V_{\ell} \in V$ are again a product of discriminative probabilities on the vertices. They are computed in a bottom-up step through data clustering, see [27].

### 4.3 SWC-3: Generalized Gibbs Sampler

Now, we design the probability $q\left(\mathbf{c}_{V_{o}}=\ell^{\prime} \mid V_{o}, \pi\right)$ to achieve acceptance probability 1 . The third version of our algorithm, named SWC-3, becomes a generalized Gibbs sampler.

Let $\pi=\left(V_{1}, V_{2}, \ldots, V_{n}\right)$ be the current partition, and $V_{o} \subseteq V_{\ell}$ be a connected component whose color $\mathbf{c}_{V_{o}}$ has $n+1$ choices. That is, $V_{o}$ can be merged with one of the following sets,

$$
S_{1}=V_{1}, S_{2}=V_{2}, \ldots, S_{l}=V_{\ell} \backslash V_{0}, \ldots, S_{n}=V_{n}, S_{n+1}=\emptyset
$$

By assigning $\mathbf{c}_{V_{o}}=\ell^{\prime} \in\{1,2, \ldots, n+1\}$, we have $n+1$ possible partitions for $\pi^{\prime}$ ( $n$ if $V_{l} \backslash V_{o}=\emptyset$ ), and we denote them by $\pi_{1}, \pi_{2}, \ldots, \pi_{n+1}$, respectively. $V_{o}$ is merged with $S_{i}$ in $\pi_{i}$ for $i=1,2, \ldots, n$ and $\pi_{\ell}=\pi$. These partitions may have $m \in$ $\{n-1, n, n+1\}$ colors. We use $m$ for clarity of notation.

We denote the Swendsen-Wang cuts between $V_{o}$ and $S_{j}, j=1,2, \ldots, n+1$ by

$$
\begin{aligned}
\mathcal{C}_{i}= & \mathcal{C}\left(V_{o}, S_{i}\right), i=1,2, \ldots, n+1 \\
& \text { with } \mathcal{C}\left(V_{o}, \emptyset\right)=\emptyset, \quad \cup_{i=1}^{n} \mathcal{C}_{i}=\mathcal{C}\left(V_{o}, V \backslash V_{o}\right)
\end{aligned}
$$

The number of edges in these SW-cuts is fixed regardless the number of colors $m$. We denote the weight for the $n+1$ partitions by

$$
\omega_{i}=\prod_{i \in S_{j}}\left(1-q_{\epsilon}\right), \quad i=1,2, \ldots, m
$$

Theorem 3. Given the partition of $V \backslash V_{o}$, and let $p\left(\pi_{i} \mid \mathbf{I}\right)$ be the posterior probability of partition $\pi_{i}$ for $i=1,2, \ldots, m$, if we choose the new color of $V_{o}$ by

$$
q\left(\mathbf{c}_{V_{o}}=i \mid V_{p}, \pi\right)=\frac{\omega_{i} p\left(\pi_{i} \mid \mathbf{I}\right)}{\sum_{j=1}^{m} \omega_{j} p\left(\pi_{j} \mid \mathbf{I}\right)}
$$

then the proposed move is accepted with probability one.
Proof. For any two partitions $\pi_{\ell}$ and $\pi_{\ell^{\prime}}$, we have the following acceptance probability, from Theorem 2,

$$
\alpha\left(\pi_{\ell} \rightarrow \pi_{\ell^{\prime}}\right)=\min \left(1, \frac{\omega_{\ell^{\prime}}}{\omega_{\ell}} \frac{\omega_{\ell} p\left(\pi_{\ell} \mid \mathbf{I}\right)}{\omega_{\ell^{\prime}} p\left(\pi_{\ell^{\prime}} \mid \mathbf{I}\right)} \frac{p\left(\pi_{\ell^{\prime}} \mid \mathbf{I}\right)}{p\left(\pi_{\ell} \mid \mathbf{I}\right)}\right)=1
$$

because the denominator in (21) is the same for $\pi_{l}$ and $\pi_{l^{\prime}}$.
Intuitively, once we pick up $V_{o}$, we merge $V_{o}$ with $S_{i}$ according to the posterior probability $p\left(\pi_{i} \mid \mathbf{I}\right), i=1,2, \ldots, m$ modified by the SW-cut factor $\omega_{i}=\prod_{v \in \mathcal{C}_{i}}\left(1-q_{o}\right)$ to ensure the Markov chain follows the posterior. If $V_{o}$ is always a single site, then $\mathcal{C}_{i}=\emptyset$ and $\omega_{i}=1$ for $i=1,2, \ldots, m$, and this reduces to the Gibbs sampler. Now, we get the third version of the SWC algorithm.

## Swendsen-Wang Cuts: SWC-3

1. Repeat, for a current partition $\pi=\left(V_{1}, \ldots, V_{n}\right)$.
2. Select a candidate set $V_{o}$ as in SWC-1 or SWC-2
3. Draw a random sample $\ell^{\prime}$ with probability $q\left(\ell^{\prime}=i \mid V_{o}, \pi\right)$ from (21)
4. Merge $V_{0}$ to $S_{i}$

In comparison, SWC-3 is computationally more costly as it has to evaluate $m$ posteriors at each step. Sometimes we can limit the number of color $m$ to only the sets which are adjacent to $V_{o}$. SWC-2 has a smaller computational cost than SWC-1 as it only tests a small number of edges in the graph clustering step. In SWC-2, one can choose the initial seed vertex $v \in V$ according to the goodness of fit, to avoid picking large components every time.

## 5 EXPERIMENTS—SEGMENTATION AND STEREO

In this section, we apply the SW-cut algorithms to two classical vision problems-image segmentation and stereo matching.

For optimizing the posterior probability, one needs a simulated annealing procedure [16] that raises the posterior probability to a certain power called temperature. This temperature is slowly decreased according to a cooling schedule. The initial temperature $T_{\max }$ is big, in order to avoid being stuck in local minima and then it is reduced it to $T_{\min }$ in a given number of sweeps ( 1 sweep $=|V|$ steps). The initial temperature $T_{\max }$ depends on the efficiency of the algorithm. As Fig. 8 shows empirically, the Gibbs sampler needs very high initial temperature $T_{\max }=200$ and a slow temperature decrease (in 5, 000 sweeps) in order to reach good solutions. Any good initial solution $W_{o}$ will be destroyed (randomized) at the high temperature. In comparison, the Swendsen-Wang cuts can walk fast at low temperature and we start with $T_{\max }$ small, usually $T_{\max }<20$, and decrease fast (in 15 sweeps), and it can utilize good initial solutions. The ending temperature $T_{\min }$ is usually in the range of $[0.1,1]$.

### 5.1 Experiment I: Image Segmentation

To reduce the size of the adjacency graph, we use a Canny edge detector and edge tracing to divide the image into "atomic regions" with almost constant intensities. Depending on image size and texture, there are $N \in[500,1500]$ atomic regions, each being a vertex in $G_{o}$. The use of atomic regions
helps reduce the computational time, but we should be aware of the risk that we are not able to break them if they are wrong, sometimes some kind of "leakage" occurs. In more recent work [2], we overcome this problem by hierarchic SW-cut method which works on multiple levels of adjacency graphs where the vertices are of various granularities.

We adopt three simple image models and more sophisticated models can be easily added as in [27]. Let $x, y$ be the coordinates of a pixel.

The first model $C_{1}$ assumes constant intensity with additive noise modeled by a nonparametric histogram $\mathcal{H}$.

$$
\mathbf{J}_{1}(x, y ; \theta)=\mu+\eta, \quad \eta \sim \mathcal{H}, \quad \theta_{1}=(\mu, \mathcal{H})
$$

The second model $C_{2}$ assumes a linear function with additive noise $\mathcal{H}$. A linear model:

$$
\mathbf{J}_{2}(x, y ; \theta)=\mu+a x+b y+\eta, \quad \eta \sim \mathcal{H}, \quad \theta_{2}=(\mu, a, b, \mathcal{H})
$$

The third model $C_{3}$ assumes a quadratic function with additive noise $\mathcal{H}$,

$$
\begin{aligned}
\mathbf{J}_{3}(x, y ; \theta) & =\mu+a x+b y+c x^{2}+d x y+c y^{2}+\eta, \eta \sim \mathcal{H} \\
\theta_{3} & =(\mu, a, b, c, d, e, \mathcal{H})
\end{aligned}
$$

The selection of model was studied in previous DDMCMC work [27]. Such models are found to be useful for fitting smoothness regions with global shading effects. The texture is modeled by the nonparametric histogram $\mathcal{H}$ which, in practice, is represented by a vector of $B$-bins $\left(\mathcal{H}_{1}, \ldots, \mathcal{H}_{B}\right)$ normalized to sum to 1 . Let $R$ be a region which has a model $(\ell, \theta)$. Then, the likelihood is

$$
P\left(\mathbf{I}_{R} ; \ell, \theta\right) \propto \prod_{e \in R} \mathcal{H}\left(\mathbf{I}_{e}\right)=\prod_{j=1}^{B} \mathcal{H}_{j}^{n_{j}}=\exp (-|R| \operatorname{entropy}(\mathcal{H}))
$$

where $n_{j}$ is the number of pixels of $R$ that fall into the $j$ th bin of the histogram.

Like [27], we use the prior $p(W)$ to encourage large and connected regions. Let $n$ be the number of regions, each region may consist of one or many subregions. We denote these connected components by $r_{1}, r_{2}, \ldots, r_{m}, m \geq n$. The prior is

$$
p(W) \propto e^{-\gamma m} e^{-\gamma^{\prime} m} \prod_{i=1}^{n} e^{-\mu\left|\theta_{i}\right|} \prod_{i=1}^{m} e^{-\lambda \operatorname{Area}\left(r_{i}\right)^{0.5}}
$$

We fix $\gamma=35, \gamma^{\prime}=15, \mu=2$ in our experiments.
The model parameters for the regions are computed deterministically at each step as the best least-square fit. This could be replaced by separate steps of model fitting and switching, but this is beyond the purpose of our experiments. The segmentation results obtained from SWC-1 are shown in Figs. 1 and 7.

### 5.2 Computational Speed and Comparison

We compare the speed of our algorithm and Gibbs sampler in Figs. 8 and 9. We run the SWC-1 algorithm five times on the cheetah image in Fig. 1, with two types of initializations. One is random initialization which assigns a random color to each atomic region independently with $n=5$ colors in total. The other is a uniform initialization which sets all atomic regions to the same color $n=1$. It happens that the

![img-6.jpeg](img-6.jpeg)

Fig. 7. Image segmentation: input image, atomic regions, and segmentation result.
uniform initialization has lower energy $(-\log p(W \mid \mathbf{I}))$ than the random initializations.

To achieve the same low energy level, the Gibbs sampler (upper two curves) in Fig. 8 has to start with a high temperature $T=200$ and use a logarithmic annealing schedule to $T=0.1$ in 5,000 sweeps; otherwise, it remains stuck at a higher energy level. In contrast, the SWC-1 starts at temperature $T=20$ and decreases to $T=0.1$ in 15 sweeps. Fig. 8 plots the energy for each run as a function of the CPU time in seconds.

The two upper curves are the Gibbs sampler with random and uniform initialization, respectively. As SWC-1 converges much faster, we plot a zoom-in view of the first 20 seconds. We show five SWC-1 runs, for both the random and uniform
initializations. The uniform initialization has much lower energy to start with and the SWC-1 algorithm also converges faster (in 3 seconds). In contrast, the Gibbs sampler cannot utilize the good initialization because it has to raise the temperature high.

To study the effects of the discriminative probabilities $q_{c}$ on convergence speed, we compare the performance of our algorithm with and without discriminative probabilities in Fig. 9. We run the SWC-1 algorithm three times with all edges having the constant probability, $q_{e}=0.2,0.4,0.6$, respectively, (Note that the Gibbs sampler is equivalent to SWC with $q_{e}=0$ ). The annealing schedules for these runs have to be slower, starting at higher temperature, to obtain

![img-7.jpeg](img-7.jpeg)

Fig. 8. Convergence comparison between SWC-1 and Gibbs sampler (upper curves) in CPU time (seconds). (a) The first 1,200 seconds. (b) Zoomed-in view of the first 20 seconds. The SWC-1 runs five times for both the random and uniform initializations.
![img-8.jpeg](img-8.jpeg)

Fig. 9. (a) Convergence comparison between SWC-1 (solid) and SWC-1 using constant edge probabilities $q_{c}=0.2,0.4,0.6$ (dotted). (b) Comparison of SWC-1 and SWC-3 for the second image in Fig. 7. Both plots are in CPU time. SWC-3 has more overhead at each step and is slower in this example.
the same final energy. Sometimes the algorithm cannot reach the same low energy as with discriminative models.

Fig. 9 displays the energy versus CPU time (in seconds) of the three runs and the SWC-1 on the airplane image shown in Fig. 7. The energies of the three SWC runs with constant edge probability $q_{c}=0.2,0.4,0.6$ are shown in dotted lines, all three runs start from a uniform initialization. They are significantly slower than SWC-1. It is worth mentioning that these SWC runs without discriminative probabilities are not equivalent with the original SW algorithm because we work on a more general energy function, in which the original SW cannot be applied.

Fig. 9b compares SWC-1 and SWC-3. SWC-1 is more effective than SWC-3 because of the computational overhead of each SWC-3 move and that there is more datadriven information used in the SWC-1 than in SWC-3, existent in the design of the $q\left(l^{\prime} \mid V_{o}, \pi\right)$.

Compared with the DDMCMC algorithm from [27], our algorithm can speed it up by 20-40 times in CPU time. Our model fitting and switching steps are quite simple, but we
observed that the full-featured model fitting and switching steps take much less time than the split-merge steps which are the focus of our algorithm. By incorporating fullfeatured model fitting and switching steps in our algorithm, it will remain 20-40 times faster than the DDMCMC [27].

### 5.3 Experiment II: Comparison with Graph Cuts and Belief Propagation for Stereo

In this section, we compare the performance of the SW Cuts with Graph Cuts [4] and Loopy Belief Propagation [33] on stereo matching using the benchmark in [23], [26].

Given a pair of stereo images $\mathbf{I}=\left(\mathbf{I}_{l}, \mathbf{I}_{r}\right)$, we assign an integer disparity value (as color) $\mathbf{c}_{v}=d_{v}$ for every pixel $v$ in the left image. The adjacency graph $G_{o}$ is simply the lattice with 4-nearest neighbor connections. The energy used in the benchmark [23], [26] is a Potts model with external field,

$$
\varepsilon=\sum_{v} D\left(d_{v}, v\right)+\sum_{<s, t>} \beta_{s, t} \mathbf{1}\left(d_{s} \neq d_{t}\right)
$$

![img-9.jpeg](img-9.jpeg)

Fig. 10. Stereo matching for the Tsukuba sequence (first row) and the Sawtooth sequence (second row). (a) Image. (b) SWC-2 result. (c) Graph cuts result. (d) Manual (truth).

The external field (data) term measures the goodness of intensity match between the left and right images for a disparity $d_{v}$,

$$
D\left(d_{v}, v\right)=\min \left\{\min _{d_{i}-1 / 2 \leq x \leq d_{v}+1 / 2}\left|\mathbf{I}_{l}(v)-\mathbf{I}_{r}(v-x)\right|, 50\right\}
$$

The coefficient in the prior term is made to be dependent on $\langle s, t\rangle$ (inhomogeneous Potts model) $\beta_{s, t}=20$ if $\left|\mathbf{I}_{l}(s)-\mathbf{I}_{l}(t)\right|>8$, otherwise $\beta_{s, t}=40$. This energy has some shortcomings. 1). It is a low-level Markov random field without generative model fitting. For example, the slanted planes in Fig. 10 (second row) are broken into many pieces. 2) It does not treat half-occluded pixels explicitly and, because of this, the ground truth has much higher energy than what the algorithms output (see Fig. 11). We are forced to use this energy in order to compare with the graph cut (and BP) as this is the type of energy that they can minimize. We compare the SWC-2 with the Graph Cuts implementations provided in the Scharstein and Szelisky's package [23] and Tappen's extension to Belief Propagation [26] available online.

For the stereo problem, we define discriminative probabilities on both vertices and edges to get better empirical results.

On each vertex (pixel) $v \in V$ we compute the vertex probability $q\left(d_{v}, v\right) \propto e^{-D\left(d_{v}, v\right)}$ normalized to 1 for $d_{v} \in\left\{0, \ldots, d_{\max }\right\}$. It measures how likely pixel $v$ has disparity $d_{v}$ based on local information. We compute a marginal probability $q(d)=\frac{1}{|V|} \sum_{v} q(d, v)$ for each disparity level $d$.

For each edge $e=\langle s, t\rangle$, we define an edge probability for any $d \in\left\{0, \ldots, d_{\max }\right\}$,

$$
q_{e}^{d}=1-e^{-\frac{20 \beta_{s, t}}{0.75 \times d_{v}(1+20) \cdot d_{v}(1+5)}}
$$

Thus, we have $d_{\max }+1$ probabilities on each edge $e$, one for each disparity level. At each SWC-2 step, we first choose a
disparity level $d$ with probability $q(d)$ and then we use $q_{e}^{d}$ as the edge probability for clustering the connected component $V_{o}$.

We found that most of the energy costs are contributed by the boundary pixels (due to the lack of half-occlusion treatment). Therefore, in SWC-2, a seed vertex $v$ is chosen with equal probability either from the boundary pixels or by sampling from a goodness of fit probability $q\left(d_{v}, v\right) D\left(d_{v}, v\right)$ with $d_{v}$ being the current assigned disparity at $v$. That is, we wish to choose more often those pixels $v$ whose assigned disparity level $d_{v}$ have a lower probability. Then, we grow the component $V_{o}$ as in SWC-2 from the seed $v$ and propose to flip its label. The new disparity level $d$ (or color) for $V_{o}$ is chosen according to a probability

$$
q\left(d \mid V_{o}, \pi\right) \propto e^{-\sum_{v \in V_{o}} D(d, v)-0.7 K \sum_{e \in s, t>, v \in V_{o}} \beta_{s, t} \mathbf{1}\left(d \neq d_{v}\right)}
$$

![img-10.jpeg](img-10.jpeg)

Fig. 11. Performance comparison of SWC with Graph Cuts and Belief Propagation for the Tsukuba sequence. The curves plot the energy over CPU time in seconds.

![img-11.jpeg](img-11.jpeg)

Fig. 12. Using a Bayesian formulation with generative models fitting piecewise planar surfaces, our algorithm obtains much better results for the same set of stereo images. The running time is about 5 minutes on a PC. (a) Image. (b) SWC result. (c) Graph cuts. (d) Manual (truth).

Fig. 11 compares the energy curves against CPU time in seconds for the SWC (two runs with different annealing schedules), graph cuts [4], and belief propagation (two versions) [23], [26]. We initialized the system with an SWC-1 version working on atomic regions which decreased the energy from about $5,000,000$ to about 650,000 in less than 30 seconds. Then, the SWC-2 version working on the pixel lattice provided the final result. The final energy obtained with SWC-2 was within 1 percent of the final energy of the Graph Cuts algorithm for the Tsukuba sequence and within less then 2 percent for the other sequences. All parameters were kept the same in all experiments.

The energy level is not a good indicator of the quality of results as the ground truth results have higher energy than all algorithms. The experiments show that the SWC reaches lower energy than belief propagation but it is slower than Graph cuts.

If we release ourselves from the simple energy model in (28), and adopt generative models with piecewise planar surfaces, we obtain a Bayesian posterior probability similar to the segmentation problem using in Experiment I. Our algorithm runs in 5 minutes and obtains the much better results shown in Fig. 12 which are closer to the ground truth. We run the SWC-2 algorithm on the atomic regions and then run the boundary diffusion [34] for a few steps to smooth the object boundary.

## 6 Discussion

In this paper, we present a generic inference algorithm for sampling arbitrary probabilities or energy functions on general graphs by extending the SW method from physics and the Gibbs sampler (SWC-3). Our method extends the SW method from the Metropolis-Hastings perspective and it is thus different from other interpretations in the literature [6],
[12]. In fact, there were some early attempts for applying SW to image analysis [12], [3] using a partial decoupling concept.

The speed of the SW-cut method depends on the discriminative probabilities on the edges and vertices. Such probabilities also make a theoretical analysis of convergence difficult. In ongoing projects, we are studying ways for bounding the SW-cut convergence with "external field" (data) and for diagnosing exact sampling using recent advanced techniques. We are also incorporating the SW-Cuts into the DDMCMC framework for image parsing.

## APPENDIX A

Proof of Theorem 1. Although there is combinatorial number of ways for selecting $V_{o}$ in the two partitions $\pi$ and $\pi^{\prime}$, the proposal probabilities ratio $\frac{q\left(V_{o} \mid \pi\right)}{q\left(V_{o} \mid \pi^{\prime}\right)}$ is very simple due to cancellation. In what follows, we compute this ratio for SWC-1. The same ratio can be derived for SWC-2 and SWC-3 following the same steps.

First, we calculate the probability $q\left(V_{o} \mid \pi\right)$ for selecting $V_{o}$ in a partition $\pi=\left(V_{1}, V_{2}, \ldots, V_{n}\right)$. Without loss of generality, we assume $V_{o} \subseteq V_{\ell}$. At state $\pi$, the edges between different colors are removed and the set of remaining edges is denoted by

$$
E_{\mathrm{on}}(\pi)=E_{o} \backslash E_{\mathrm{off}}(\pi), \quad E_{\mathrm{off}}(\pi)=\cup_{i \neq j} \mathcal{C}\left(V_{i}, V_{j}\right)
$$

Each edge $e \in E_{\text {on }}(\pi)$ is turned off ( $\mu_{e}=$ off) with probability $1-q_{e}$ independently and we denote the edge variables by

$$
\begin{aligned}
U(\pi) & =U_{\mathrm{on}}(\pi) \cup U_{\mathrm{off}}(\pi), \quad \text { with } \\
U_{\mathrm{on}}(\pi) & =\left\{\mu_{e}=\text { on }, e \in E_{\mathrm{on}}(\pi)\right\} \\
U_{\mathrm{off}}(\pi) & =\left\{\mu_{e}=\text { off }, e \in E_{\mathrm{on}}(\pi)\right\}
\end{aligned}
$$

![img-12.jpeg](img-12.jpeg)

Fig. 13. State $\pi_{A}$ has two subgraphs $V_{1}$ and $V_{2}$ which are merged in state $\pi_{B}$. There are two paths between $\pi_{A}$ and $\pi_{B}$. One is to choose $V_{0}=V_{1}$ and the other is to choose $V_{0}=V_{2}$.

We denote the sets of edges that are turned on and off by $U$ given $\pi$ by, respectively,

$$
\begin{aligned}
& E_{\text {on }}(\pi, U)=\left\{e: e \in E_{\text {on }}(\pi), \mu_{e}=\text { on }\right\}, \text { and } \\
& E_{\text {off }}(\pi, U)=\left\{e: e \in E_{\text {on }}(\pi), \mu_{e}=\text { off }\right\}
\end{aligned}
$$

The probability of an event $U(\pi)$ is simply

$$
p(U(\pi))=\prod_{e \in E_{\text {on }}(\pi, U)} q_{e} \cdot \prod_{e \in E_{\text {off }}(\pi, U)}\left(1-q_{e}\right)
$$

In the clustering step, each color $V_{i}$ is broken into a number $n_{i}$ of connected components. Let $C P(\pi)$ be a set of connected components at state $\pi$. There are many ways to arrive at $C P(\pi)$ depending on the edge probability $U(\pi)$. For event $U=U(\pi)$, we denote the set of connected components by $C P(\pi, U)$. Each set of connected components can be obtained by a combinatorial number of edge probabilities $U$, so the probability of $C P(\pi)$ is,

$$
p(C P(\pi))=\sum_{U: C P(\pi, U)=C P(\pi)} p(U(\pi))
$$

We are interested in the set of $C P(\pi)$ s which includes $V_{o}$ as a connected component,

$$
\Omega\left(V_{o}, \pi\right)=\left\{C P(\pi): V_{o} \in C P(\pi)\right\}
$$

Therefore, the probability for choosing $V_{o}$ at $\pi$ is

$$
q\left(V_{o} \mid \pi\right)=\sum_{C P(\pi, U) \in \Omega\left(V_{o}, \pi\right)} p(U(\pi)) p\left(V_{o} \mid C P(\pi, U)\right)
$$

where $p\left(V_{o} \mid C P(\pi, U)\right)$ could be arbitrary, say $p\left(V_{o} \mid C P\right.$ $(\pi, U))=\frac{1}{\mid C P(\pi, U))}$.

To summarize, all $C P$ s in $\Omega\left(V_{o}, \pi\right)$ must observe one common property-the edges in the SW-cut $\mathcal{C}\left(V_{o}, V_{\ell} \backslash V_{o}\right)$ must be turned off; otherwise, $V_{o}$ is connected to other vertices in $V_{\ell}$ and, thus, violates the premise that $V_{o}$ is a connected component. So, we have
$\mathcal{C}\left(V_{o}, V_{\ell} \backslash V_{o}\right) \subset E_{\text {off }}(\pi, U), \quad \forall C P(\pi, U) \in \Omega\left(V_{o}, \pi\right)$.
Let

$$
\begin{aligned}
& E_{\text {off }}^{-}(\pi, U)= \\
& E_{\text {off }}(\pi, U) \backslash \mathcal{C}\left(V_{o}, V_{\ell} \backslash V_{o}\right), \quad \forall C P(\pi, U) \in \Omega\left(V_{o}, \pi\right)
\end{aligned}
$$

Therefore, we can take the common factor out the summation,

$$
\begin{aligned}
q\left(V_{o} \mid \pi\right)= & \prod_{e \in \mathcal{C}\left(V_{o}, V_{\ell} \backslash V_{o}\right)}\left(1-q_{e}\right) \cdot \sum_{C P(\pi, U) \in \Omega\left(V_{o}, \pi\right)} \frac{1}{|C P(\pi, U)|} \\
& {\left[\prod_{e \in E_{\text {on }}(\pi, U)} q_{e} \cdot \prod_{e \in E_{\text {off }}^{-}(\pi, U)}\left(1-q_{e}\right)\right] }
\end{aligned}
$$

Second, we calculate the probability $q\left(V_{o} \mid \pi^{\prime}\right)$ for selecting $V_{o}$ in a partition $\pi^{\prime}$. Without loss of generality, we assume $V_{o} \subseteq V_{\ell}$. Following the same steps above, we have,

$$
\begin{aligned}
q\left(V_{o} \mid \pi^{\prime}\right)= & \prod_{e \in \mathcal{C}\left(V_{o}, V_{\ell} \backslash V_{o}\right)}\left(1-q_{e}\right) \cdot \sum_{C P\left(\pi^{\prime}, U^{\prime}\right) \in \Omega\left(V_{o}, \pi^{\prime}\right)} \frac{1}{\mid C P\left(\pi^{\prime}, U^{\prime}\right) \mid} \\
& {\left[\prod_{e \in E_{\text {on }}\left(\pi^{\prime}, U^{\prime}\right)} q_{e} \cdot \prod_{e \in E_{\text {off }}^{\prime}\left(\pi^{\prime}, U^{\prime}\right)}\left(1-q_{e}\right)\right] }
\end{aligned}
$$

Since $\pi$ and $\pi^{\prime}$ are partitions at consecutive SWC-steps and they differ only in the coloring of $V_{o}$, we have the following observations.

For each $C P(\pi, U) \in \Omega\left(V_{o}, \pi\right)$, there is a corresponding $C P\left(\pi^{\prime}, U^{\prime}\right) \in \Omega\left(V_{o}, \pi^{\prime}\right)$, such that $C P\left(\pi^{\prime}, U^{\prime}\right)=C P(\pi, U)$. Furthermore, we have
$E_{\text {on }}(\pi, U)=E_{\text {on }}\left(\pi^{\prime}, U^{\prime}\right), \quad$ and $\quad E_{\text {off }}^{-}(\pi, U)=E_{\text {off }}^{-}\left(\pi^{\prime}, U^{\prime}\right)$.
That is, $U$ and $U^{\prime}$ differs only in the SW-cuts. As the correspondence is one-to-one, we have

$$
\Omega\left(V_{o}, \pi\right)=\Omega\left(V_{o}, \pi^{\prime}\right)
$$

Therefore, we obtain the ratio by canceling the common probability in (41) and (42).

$$
\frac{q\left(V_{o} \mid \pi\right)}{q\left(V_{o} \mid \pi^{\prime}\right)}=\frac{\prod_{e \in \mathcal{C}\left(V_{o}, V_{\ell} \backslash V_{o}\right)}\left(1-q_{e}\right)}{\prod_{e \in \mathcal{C}\left(V_{o}, V_{\ell} \backslash V_{o}\right)}\left(1-q_{e}\right)}
$$

In a special case, when $q_{e}=q_{e}, \forall e \in E_{s}$, we obtain the proposal ratio in (9) for the original SW method.

## APPENDIX B

Proof of Theorem 2: The Splitting and Merging Cases. For the regrouping case where $V_{o} \subset V_{\ell}$ in $\pi$ and $V_{o} \subset V_{\ell^{\prime}}$ in $\pi^{\prime}$, the only way for moving between $\pi$ and $\pi^{\prime}$ is to select $V_{o}$. But, for the merging and splitting cases there might be two paths illustrated in Fig. 13. Without loss of generality, we write $\pi=\left(V_{1}, V_{2}, V_{3}, \ldots, V_{n}\right)$ and $\pi^{\prime}=\left(V_{1+2}, V_{3}, V_{4}, \ldots, V_{n}\right)$ with $V_{1+2}=V_{1} \cup V_{2}$. The two paths for moving between $\pi$ and $\pi^{\prime}$ are, respectively.

Path 1. Choose $V_{o}=V_{1}$. In state $\pi=\pi_{A}$, choose $\ell^{\prime}=2$, i.e., merge $V_{o}$ to $V_{2}$ and, reversely, in state $\pi^{\prime}=\pi_{B}$, choose $\ell^{\prime}=1$, i.e., split $V_{o}$ from $V_{2}$.

Path 2. Choose $V_{o}=V_{2}$. In state $\pi=\pi_{A}$, choose $\ell^{\prime}=1$, i.e., merge $V_{o}$ to $V_{1}$ and, reversely, in state $\pi^{\prime}=\pi_{B}$, choose $\ell^{\prime}=2$, i.e., split $V_{o}$ from $V_{1}$.

The proposal probability ratio is,

$$
\begin{aligned}
& \frac{q\left(\pi^{\prime} \rightarrow \pi\right)}{q\left(\pi \rightarrow \pi^{\prime}\right)}= \\
& \frac{q\left(V_{o}=V_{1} \mid \pi^{\prime}\right) q\left(\mathbf{c}_{V_{o}}=2 \mid V_{o}, \pi^{\prime}\right)+q\left(V_{o}=V_{2} \mid \pi^{\prime}\right) q\left(\mathbf{c}_{V_{o}}=1 \mid V_{o}, \pi^{\prime}\right)}{q\left(V_{o}=V_{1} \mid \pi\right) q\left(\mathbf{c}_{V_{o}}=1 \mid V_{o}, \pi\right))+q\left(V_{o}=V_{2} \mid \pi\right) q\left(\mathbf{c}_{V_{o}}=2 \mid V_{o}, \pi\right)}
\end{aligned}
$$

In state $\pi=\pi_{A}$, the SW-cut $\mathcal{C}\left(V_{o}, V_{\ell} \backslash V_{o}\right)=\emptyset$ for both paths and, in state $\pi^{\prime}=\pi_{B}$, the cut is $\mathcal{C}\left(V_{\ell}, V_{\ell^{\prime}}\right)=\mathcal{C}\left(V_{1}, V_{2}\right)$ for both paths. Following Theorem 1, the probability ratios for choosing $V_{o}=V_{1}$ and $V_{o}=V_{2}$ are equal,

$$
\frac{q\left(V_{o}=V_{1} \mid \pi\right)}{q\left(V_{o}=V_{1} \mid \pi^{\prime}\right)}=\frac{1}{\prod_{e \in \mathcal{C}\left(V_{1}, V_{2}\right)}(1-q(e))}=\frac{q\left(V_{o}=V_{2} \mid \pi\right)}{q\left(V_{o}=V_{2} \mid \pi^{\prime}\right)}
$$

Once $V_{o}$ is selected, either $V_{o}=V_{1}$ or $V_{o}=V_{2}$, then the remaining partition for both $\pi$ and $\pi^{\prime}$ is the same, and is denoted by $\pi\left(V \backslash V_{o}\right)=\pi^{\prime}\left(V \backslash V_{o}\right)$. In proposing the new label of $V_{o}$, we easily observe that

$$
\frac{q\left(\mathbf{c}_{V_{o}}=2 \mid V_{o}=V_{1}, \pi^{\prime}\right)}{q\left(\mathbf{c}_{V_{o}}=1 \mid V_{o}=V_{2}, \pi\right)}=\frac{q\left(\mathbf{c}_{V_{o}}=1 \mid V_{o}=V_{2}, \pi^{\prime}\right)}{q\left(\mathbf{c}_{V_{o}}=2 \mid V_{o}=V_{1}, \pi\right)}
$$

Then, the acceptance rate in Theorem 2 follows from (47) and (48).

## AcKNOWLEDGMENTS

The work is supported by US National Science Foundation grant IIS-02-44763 and US Office of Naval Research grant N-00014-02-1-0952. The authors would like to thank Zhuowen Tu and Yingnian Wu for discussions and they thank Dr. Rangarajan and anonymous reviewers for helpful comments. An earlier version of this paper appeared in Proceedings of the Ninth International Conference on Computer Vision, Nice, France, 2003.
