# cuPC: CUDA-based Parallel PC Algorithm for Causal Structure Learning on GPU 

Behrooz Zarebavani, Foad Jafarinejad, Matin Hashemi, and Saber Salehkaleybar<br>This article is published. Please cite as B. Zarebavani, F. Jafarinejad, M. Hashemi, S. Salehkaleybar, "cuPC: CUDA-based Parallel PC Algorithm for Causal Structure Learning on GPU," IEEE Transactions on Parallel and Distributed Systems (TPDS), 2019. doi: 10.1109/TPDS.2019.2939126


#### Abstract

The main goal in many fields in the empirical sciences is to discover causal relationships among a set of variables from observational data. PC algorithm is one of the promising solutions to learn underlying causal structure by performing a number of conditional independence tests. In this paper, we propose a novel GPU-based parallel algorithm, called cuPC, to execute an order-independent version of PC. The proposed solution has two variants, cuPC-E and cuPC-S, which parallelize PC in two different ways for multivariate normal distribution. Experimental results show the scalability of the proposed algorithms with respect to the number of variables, the number of samples, and different graph densities. For instance, in one of the most challenging datasets, the runtime is reduced from more than 11 hours to about 4 seconds. On average, cuPC-E and cuPC-S achieve 500 X and 1300 X speedup, respectively, compared to serial implementation on CPU. The source code of cuPC is available online [1].


Index Terms—Bayesian Networks, Causal Discovery, CUDA, GPU, Machine Learning, Parallel Processing, PC Algorithm.

## 1 INTRODUCTION

LEARNING causal structures is one of the main problems in empirical sciences. For instance, we need to understand the impact of a medical treatment on a disease or recover causal relations between genes in gene regulatory networks (GRN) [2]. By discovering such causal relations, one will be able to predict the impact of different actions. Causal relations can be inferred by controlled randomized experiments. However, in many cases, it is not possible to perform the required experiments due to technical or ethical reasons. In such cases, causal relations need to be learned merely from observational data [3], [4].

Causal Bayesian network is one of the models which has been widely considered to explain the data-generating mechanism. In this model, causal relations among variables are represented by a directed acyclic graph (DAG) where there is a direct edge from variable $V_{i}$ to variable $V_{j}$ if $V_{i}$ is a direct cause of $V_{j}$. The task of causal structure learning is to learn all DAGs that are compatible with the observed data. Under some assumptions [4], the underlying true causal structure is in the set of recovered DAGs if the number of observed data samples goes to infinity. Two common approaches for learning causal structures are scorebased and constraint-based approaches. In the score-based approach, in order to find a set of DAGs that best explains dependency relations among the variables, a score function is evaluated, which might become an NP-hard problem [5].

In the constraint-based approach, such DAGs are found by performing a number of conditional independence (CI)

[^0]tests. Sprites and Glymour [4] proposed a promising solution, called PC algorithm. For ground-truth graphs with bounded degrees, PC algorithm does not require to perform high-order conditional independence tests, and thus, runs in polynomial time. PC algorithm has become a common tool for causal explorations and is available in different graphical model learning packages such as pcalg [6], bnlearn [7], and TETRAD [8]. Moreover, it has been widely applied in different applications such as learning the causal structure of GRNs from gene expression data [9], [10]. Furthermore, a number of causal structure learning algorithms, for instance, FCI and its variants such as RFCI [4], [11], and CCD algorithm [12], use PC algorithm as a subroutine.

PC algorithm starts from a complete undirected graph and removes the edges in consecutive levels based on carefully selected conditional independence tests. However, performing these number of tests might take a few days on a single machine in some gene expression data such as DREAM5-Insilico dataset [13]. Furthermore, the order of performing conditional independence tests may affect the final result. Parallel implementations of PC algorithm on multi-core CPUs have been proposed in [14], [15]. In [16], Colombo and Maathuis proposed a variant of PC algorithm called PC-stable which is order-independent and produces less error compared with the original PC algorithm. The key property of PC-stable is that removing an edge in a level has no effect on performing conditional independence tests of other edges in that level. This order-independent property makes PC-stable suitable for executing on multi-core machines. In [17], Le et al. proposed a parallel implementation of PC-stable algorithm on multi-core CPUs, called ParallelPC, which reduces the runtime by an order of magnitude. For instance, it takes a couple of hours to process DREAM5Insilico dataset. In case of using GPU hardware, there was an attempt for parallelization of the PC-stable algorithm


[^0]:    The authors are with Learning and Intelligent Systems Laboratory, Department of Electrical Engineering, Sharif University of Technology, Tehran, Iran. Webpage: http://lis.ee.sharif.edu/ E-mails: behrooz.zare@ee.sharif.edu, fzj5053@psu.edu, matin@sharif.edu (corresponding author), saleh@sharif.edu. doi: 10.1109/TPDS.2019.2939126

in [18]. However, only a small part (only level zero and level one) of the PC-stable algorithm is parallelized in this method, and thus, it cannot be used as a complete solution in many datasets which require more than two levels. In fact, their approach cannot be generalized to level two and beyond.

In this paper, we propose a GPU-based parallel algorithm, called "cuPC", for learning causal structures based on PC-stable. We assume that there is no missing observations for any variable, and data has multivariate normal distribution. In order to execute PC-stable, one needs to perform conditional independence tests to evaluate whether two variables $V_{i}$ and $V_{j}$ are independent given another set of variables $S$. The proposed algorithm has two variants, called "cuPC-E" and "cuPC-S", which employ the following ideas.

If cuPC-E employs two degrees of parallelism at the same time. First is performing tests for multiple edges in parallel and second, is parallelizing the tests which are performed for a given edge. Although abundant parallelism is available, parallelizing all such tests does not yield the highest performance because it incurs different overheads and also results in many unnecessary tests. Instead, cuPCE judiciously strikes a balance between the two degrees of parallelism in order to efficiently utilize the parallel computing capabilities of GPU and avoid launching unnecessary tests at the same time. In addition, cuPC-E employs two configuration parameters which can be adjusted to tune the performance and achieve high speedup in both sparse and dense graphs.

II) A conditional set $S$ might be common in tests of many pairs of variables. cuPC-S takes advantage of this property and reuses the results of computations in one of such tests in the others. This sharing can be performed in different ways. For instance, sharing all redundant computations in processing the entire graph might first seem more beneficial, but it has non-justifiable overheads. Hence, cuPC-S employs a carefully-designed local sharing strategy in order to avoid different overheads and achieve significant speedup.

III) cuPC-E and cuPC-S parallel algorithms avoid storing the indices of variables in set $S$. Instead, a combination function is employed to compute the indices on-the-fly and also in parallel. IV) The causal structure is represented by an adjacency matrix which is compacted before starting the computations in every level. The compacted format is judiciously selected to assign and execute parallel threads more efficiently, and also, improves cache performance. V) GPU shared memory is used in order to improve performance. VI) Where applicable, threads are terminated early in order to avoid performing unnecessary computations. For instance, edge removals are monitored in parallel, and when an edge is removed in another thread or another block, the rest of the tests on that edge are skipped.

Experiments on multiple datasets show the scalability of the proposed parallel algorithms with respect to the number of variables, the number of samples, and different graph densities. For instance, in one of the most challenging datasets, cuPC-S can reduce the runtime of PC-stable from more than 11 hours to about 4 seconds. On average, cuPCE and cuPC-S achieve about 500 X and 1300 X speedup, respectively, compared to serial implementation on CPU.

The rest of this paper is organized as follows. In Section 2, we review some preliminaries on causal Bayesian networks and description of PC-stable. In Section 3, we present the two variants of cuPC algorithm, cuPC-E and cuPC-S. Furthermore, we elaborate details of our contributions in Section 4. We conduct experiments to evaluate the performance and scalability of the proposed solution in Section 5 and conclude our results in Section 6.

## 2 PRELIMINARIES

### 2.1 Bayesian Networks

Consider a set of random variables $\mathcal{V}=\left\{V_{1}, V_{2}, \ldots, V_{n}\right\}$. Given $X, Y, Z \subseteq \mathcal{V}$, a conditional independence (CI) assertion of the form $X \perp Y \mid Z$ means $X$ and $Y$ are independent given $Z$. A CI test of the form $I(X, Y \mid Z)$ is a test procedure based on observed data samples from $X$, $Y$ and $Z$ which determines whether the corresponding CI assertion $X \perp Y \mid Z$ holds or not. Section 4.3 describes how to perform CI tests from observed-data samples.

Graphical model $G$ is a graph which encodes a joint distribution $P$ over the random variables in $\mathcal{V}$. The reason behind the development of a graphical model is that the explicit representation of the joint distribution becomes infeasible as the number of variables grows. Furthermore, under some assumptions on the data generating model, one can interpret causal relations among the variables from these graphs [19].

Bayesian Networks (BN) are a class of graphical models that represent a factorization of $P$ over $\mathcal{V}$ by a directed acyclic graph (DAG) $G=(\mathcal{V}, \mathcal{E})$ as

$$
P\left(V_{1}, V_{2}, \ldots, V_{n}\right)=\prod_{i=1}^{n} P\left(V_{i} \mid \operatorname{par}\left(V_{i}\right)\right)
$$

where $\mathcal{E}$ is the set of edges, and $\operatorname{par}\left(V_{i}\right)$ denotes parents of $V_{i}$ in $G$. Moreover, the graph $G$ encodes conditional independence between the random variables in $\mathcal{V}$ by some notion of separation in graphs.

A Causal Bayesian Network (CBN) is a BN where each directed edge represents a cause-effect relationship from the parent to its child. For the exact definition of CBN, please refer to [20], Section 1.3. A CBN satisfies causal Markov condition, i.e., given $\operatorname{par}\left(V_{i}\right)$, variable $V_{i}$ is independent of any variable $V_{j}$ that there is no directed path from $V_{i}$ to $V_{j}$. Let $\mathcal{I}(P)$ be the set of all CI assertions that holds in $P$. Under causal Markov condition and faithful assumptions [4], all CI assertions in $\mathcal{I}(P)$ are encoded in the true causal graph $G$ [21].

### 2.2 CPDAG

In a directed graph $G$, we say that three variables $V_{i}, V_{k}, V_{j} \in \mathcal{V}$ form a $\mathbf{v}$-structure at $V_{k}$ if variables $V_{i}$ and $V_{j}$ have an outgoing edge to variable $V_{k}$ while they are not connected by any edge in $G$. This is denoted by $V_{i} \rightarrow V_{k} \leftarrow V_{j}$. The skeleton of a directed graph $G$ is an undirected graph that contains edges of $G$ without considering their orientations.

For a given joint distribution $P$, there might be different DAGs that can represent $\mathcal{I}(P)$. The set of all such DAGs is called Markov equivalence class [22]. It can be shown

that two DAGs are in the same Markov equivalence class if they have the same skeleton and the same set of $\mathbf{v}$ structures [23]. A Markov equivalence class can be represented uniquely by a mixed graph called completed partial DAG (CPDAG). In particular, there is a directed edge in CPDAG from $V_{i}$ to $V_{j}$ if this edge exists with the same direction in all DAGs in the Markov equivalent class. There is an undirected edge between $V_{i}$ and $V_{j}$ in CPDAG if there exist two DAGs in the Markov equivalence class which have an edge between $V_{i}$ and $V_{j}$ but with different orientations.

### 2.3 Causal Structure Learning

Causal structure learning, our focus in this paper, is the problem of finding a CPDAG which best describes dependency relations in a given data that is sampled from the random variables in $\mathcal{V}$. In the literature, two main approaches have been proposed for causal structure learning [24]: constraint-based approach and score-based approach.

In the constraint-based approach, CI tests are utilized to recover the CPDAG. Examples include PC [4], Rank PC [25], PC-stable [16], IC [26], and FCI [4]. In the scorebased approach, a score function indicates how well each DAG explains dependency relations in the data. Then, a CPDAG with the highest score is obtained by searching over Markov equivalence classes. Examples include ChowLiu [27] and GES [28] algorithms. There are other methods such as LiNGAM [29], [30], and BACKSHIFT [31] which do not belong to any of the above two categories because their underlying assumptions are more restricted or their settings are different.

Choosing between the types of algorithms depends on the characteristics of the data [32]. For instance, Scutari et al. [33] concluded that constraint-based algorithms are more accurate than score-based algorithms for small sample sizes and that they are as accurate as hybrid algorithms. PC algorithm, as one of the main constraint-based algorithms, has become a common tool for causal explorations and is available in different graphical model learning packages [6], [7], [8]. In addition, a number of causal structure learning algorithms utilize PC algorithm as a subroutine [4], [11], [12].

### 2.4 PC-stable Algorithm

In the constraint-based approach, a naive solution to check whether there is an edge between two variables $V_{i}$ and $V_{j}$ in the CPDAG is to perform all CI tests of the form $I\left(V_{i}, V_{j} \mid S\right)$ where $S \subseteq \mathcal{V} \backslash\left\{V_{i}, V_{j}\right\}$. This solution is computationally infeasible for large number of variables due to exponentially growing number of CI tests.

Unlike the naive solution, the PC algorithm is computationally efficient for sparse graphs with up to thousands number of variables and is commonly used in highdimensional settings [34]. Here we describe PC-stable algorithm which is a variation of PC with less estimation errors [16].

PC-stable algorithm consists of two main steps: In the first step, the skeleton is determined by performing a number of carefully selected CI tests. In the second step, the set of v-structures are extracted and as many of the undirected edges as possible are oriented by applying a set of rules

Algorithm 1 The first step in PC-stable algorithm.
Input: $\mathcal{V}$
Output: $G$, SepSet
$G=$ fully connected graph
$S e p S e t=\emptyset$
$\ell=0$
repeat
Copy $G$ into $G^{\prime}$
for any edge $\left(V_{i}, V_{j}\right)$ in $G$ do
repeat
Choose a new $S \subseteq \operatorname{adj}\left(V_{i}, G^{\prime}\right) \backslash\left\{V_{j}\right\}$ with $|S|=\ell$
Perform $I\left(V_{i}, V_{j} \mid S\right)$
if $V_{i} \perp V_{j} \mid S$ then
Remove $\left(V_{i}, V_{j}\right)$ from $G$
Store $S$ in SepSet
end if
until $\left(V_{i}, V_{j}\right)$ is removed or all sets $S$ are considered
end for
$\ell=\ell+1$
until ( max degree $-1 \geq \ell$ )
![img-0.jpeg](img-0.jpeg)

Fig. 1. An example of execution of PC-stable algorithm. For better readability, we use the term $i$ instead of $V_{i}$. For instance, $I(0,1)$ actually means $I\left(V_{0}, V_{1}\right)$. This is done in Fig. 3 and Fig. 4 as well.
called Meek rules [35]. The second step is fairly fast. The first step is computationally intensive [15] and forms our focus in this paper. For instance, in ground truth graphs with a bound $\Delta$ on the maximum degree, the time complexity of PC-stable algorithm is in the order of $O\left(n^{\Delta}\right)$. Sections 3 and 4 present our proposed solution for acceleration of this step on GPU. Details of the first step are described in the following.

See Algorithm 1. First, $G$ is initiated with a fully connected undirected graph over set $\mathcal{V}$ (line 1). Next, the extra edges are removed from $G$ by performing a number of CI tests. The tests are performed by levels. In each level $\ell$, first a copy of $G$ is stored in $G^{\prime}$ (line 5). Next, for every edge $\left(V_{i}, V_{j}\right)$ in graph $G$, a CI test $I\left(V_{i}, V_{j} \mid S\right)$ is performed for any $S \subseteq \operatorname{adj}\left(V_{i}, G^{\prime}\right) \backslash\left\{V_{j}\right\}$ such that $|S|=\ell$ (lines $6-9$ ), where $\operatorname{adj}\left(V_{i}, G^{\prime}\right)$ denotes the neighbors of $V_{i}$ in $G^{\prime}$ (see Section 4.3 for the details of performing a CI test). If there

exists a set $S$ where $V_{i}$ is independent of $V_{j}$ given $S$ (line 10), edge $\left(V_{i}, V_{j}\right)$ is removed from $G$, and $S$ is stored in SepSet (lines 11-12). Once all the edges are considered, $\ell$ is incremented (line 16) and the above procedure is repeated. The algorithm continues as long as the maximum degree of the graph is large enough (line 17). The second step in PCstable is to use SepSet to find v-structures and orient the edges of graph $G$.

Fig. 1 illustrates execution of the first step on a small graph. In level $\ell=0$, six CI tests are performed, one for every edge in the fully connected graph. Assuming that the result of the fourth CI test is true, we have $V_{1} \perp V_{2}$, and hence, edge $\left(V_{1}, V_{2}\right)$ is removed. In level $\ell=1,12$ CI tests are performed and edges $\left(V_{1}, V_{3}\right)$ and $\left(V_{2}, V_{3}\right)$ are removed.

Note that by selecting the conditional sets $S$ from $G^{\prime}$ but removing edges from $G$, the algorithm finally reaches the same graph regardless of the edge selection order. In other words, during the execution of the algorithm in a level, $S$ only depends on $G^{\prime}$. Since performing CI tests in each level is independent of the edge selection order, making an error in one of the CI tests does not have any impact on other CI tests in that level.

## 3 CUPC: CUDA-Accelerated PC Algorithm

This section presents our proposed solution for acceleration of the computationally-intensive portion of PC-stable (lines $5-15$ in Algorithm 1) on GPU using CUDA parallel programming API. We assume that there is no missing observations for any variable, and data has multivariate normal distribution. The overall view of the proposed method is shown in Algorithm 2. The main loop on $\ell$ which iterates through the levels still exists in the proposed solution, but the internal computations of every level are accelerated on GPU. In specific, since the computations of level zero can be simplified, a separate parallel algorithm is employed for this level (line 7 in Algorithm 2). For every level $\ell \geq 1$, first $G$ is copied into $G^{\prime}$ (line 9), and then, the required computations are performed (line 10). Note that we work on adjacency matrix of graph $G$ denoted as $A_{G}$. In order to increase the efficiency of the proposed parallel algorithms, $A_{G}^{\prime}$ is a compacted version of $A_{G}$. The details are discussed in the following.

A short background on CUDA is presented in Section 3.1. Acceleration of level $\ell=0$ is discussed in Section 3.2. For levels $\ell \geq 1$, two different parallel algorithms called cuPC-E and cuPC-S are proposed. cuPC-E and the compact procedure are discussed in Section 3.3. cuPC-S is discussed in Section 3.4. Further details on some parts of the proposed solution are discussed later in Section 4.

### 3.1 CUDA

CUDA is a parallel programming API for Nvidia GPUs. GPU is a massively parallel processor with hundreds to thousands of cores. CUDA follows a hierarchical programming model. At the top level, computationally intensive functions are specified by the programmer as CUDA kernels. A kernel is specified as a sequential function for a single thread. The kernel is then launched for parallel execution on the GPU by specifying the number of concurrent threads.

Algorithm 2 Overall view of the proposed solution. Lines 7, 9 , and 10 are executed in parallel on GPU.

```
Input: \(\mathcal{V}\)
Output: G, SepSet
    \(G=\) fully connected graph
    SepSet \(=\emptyset\)
    \(\ell=0\)
    \(A_{G}=\) adjacency matrix of graph \(G\)
    repeat
        if \((\ell==0)\) then
            GPU: execute level zero
        else
            GPU: compact \(A_{G}\) into \(A_{G}^{\prime}\)
            GPU: execute level \(\ell\)
        end if
        \(\ell=\ell+1\)
    until ( max degree \(-1 \geq \ell\) )
```

Threads are grouped into blocks. A kernel consists of a number of blocks, and every block consists of a number of threads. Every block has access to a small, on-chip and low-latency memory, called shared memory. The shared memory of a block is accessible to all threads within that block, but not to any thread from other blocks ${ }^{1}$.

In order to identify blocks within a kernel, and also, threads within a block, a set of indices are used in the CUDA API, for instance, blockIdx.y and blockIdx.x as the block index in dimension $y$ and dimension $x$ within a 2D kernel, and threadIdx.y and threadIdx.x as the thread index in dimensions $y$ and $x$ within a 2D block. For brevity, we denote these four indices as $b y, b x, t y$ and $t x$, respectively.

### 3.2 Level $\ell=0$

Size of conditional sets $S$ is equal to $\ell$ (Algorithm 1, line 8). As a result, in level zero, $S=\emptyset$, and therefore, the required computations can be simplified. In specific, for every edge $\left(V_{i}, V_{j}\right)$ in $G$, only one CI test is required, which is $I\left(V_{i}, V_{j} \mid \emptyset\right)$ or simply $I\left(V_{i}, V_{j}\right)$. In addition, copying $G$ into $G^{\prime}$ is not required.

All the required CI tests $I\left(V_{i}, V_{j}\right)$ are performed in parallel as shown in Algorithm 3. Since the input graph in level zero is a fully connected undirected graph, a total of $n(n-1) / 2$ tests are required, i.e., one for every edge. Every test $I\left(V_{i}, V_{j}\right)$ is assigned to a separate thread and $n^{2}$ threads are launched. Threads are grouped in a 2D kernel of $n / 32 \times n / 32$ blocks. Every block has $32 \times 32$ threads. Indices $i$ and $j$ are calculated in lines $1-2$. Here, $0 \leq b y, b x<n / 32$ and $0 \leq t y, t x<32$.

Lines $4-7$ are executed in only $n(n-1) / 2$ threads. In line 4 , the CI test $I\left(V_{i}, V_{j}\right)$ is performed. In lines $5-7$, the edge $\left(V_{i}, V_{j}\right)$ is removed from graph $G$ if $V_{i} \perp V_{j}$. The term $A_{G}$ denotes the adjacency matrix of graph $G$. Edge $\left(V_{i}, V_{j}\right)$ is removed from $G$ by setting $A_{G}[i, j]=A_{G}[j, i]=0$.

1. This article is presented based on CUDA programming framework. However, the presented ideas and parallel algorithms can readily be ported to OpenCL programming framework for other GPU vendors as well. In specific, block, thread and shared memory in CUDA programming framework correspond to work-group, work-item, and local memory in OpenCL programming framework.

Algorithm 3 Acceleration of level $\ell=0$. See Section 3.2.
Input: $A_{G}$
Output: $A_{G}$
\# of blocks: $n / 32 \times n / 32$
\# of threads / block: $32 \times 32$
$1: i=b y \times 32+t y$
$2: j=b x \times 32+t x$
3: if $(i<j)$ then
4: Perform $I\left(V_{i}, V_{j}\right)$
5: if $\left(V_{i} \perp V_{j}\right)$ then
6: $\quad A_{G}[i, j]=A_{G}[j, i]=0$
7: end if
8: end if
![img-1.jpeg](img-1.jpeg)

Fig. 2. $A_{G}^{\prime}$ is formed by compacting $A_{G}$.

### 3.3 Level $\ell \geq 1$ : Parallel Algorithm cuPC-E

Two different parallel algorithms (kernels) are proposed for acceleration of every level $\ell \geq 1$. This section describes the first algorithm, called cuPC-E. See Algorithm 4.

Compact: cuPC-E takes $\ell, A_{G}$ and $A_{G}^{\prime}$ as input. As shown in line 9 in Algorithm 2, $A_{G}^{\prime}$ is formed by compacting adjacency matrix $A_{G}$ into a sparse representation. Fig. 2 illustrates a small example. An element with value $j$ in $i$-th row in $A_{G}^{\prime}$ denotes existence of edge $\left(V_{i}, V_{j}\right)$ in $A_{G} . A_{G}^{\prime}$ has $n$ rows. Row $i$ has $n_{i}^{\prime}$ elements, i.e., edges. Let $n^{\prime}=\max _{0 \leq i<n} n_{i}^{\prime}$. Note that $A_{G}^{\prime}$ can be implemented in different formats such as linked lists as in adjacency list representations [36]. However, since linked lists are not efficient for parallel execution, $A_{G}^{\prime}$ is implemented as a matrix with $n$ rows and $n^{\prime}+1$ columns. The element at the last column of each row $i$ stores $n_{i}^{\prime}$. The Compact procedure is executed in parallel by employing another parallel algorithm called scan [37], [38]. Details are removed for brevity.

Blocks and Threads: cuPC-E kernel consists of $n \times n^{\prime} / \beta$ blocks. See Fig. 3(a). Every block performs the required CI tests for $\beta$ edges, i.e., $\beta$ consecutive elements from one row in $A_{G}^{\prime}$. In Fig. 3(a), there are $7 \times 2$ blocks. Block $(2,1)$, which is marked with green color, works on $\beta=3$ edges, namely, $\left(V_{2}, V_{4}\right),\left(V_{2}, V_{5}\right)$, and $\left(V_{2}, V_{6}\right)$. See Fig. 3(b). The CI tests for each one of the $\beta$ edges are split among $\gamma$ threads. Hence, every block consists of $\gamma \times \beta$ threads. In Fig. 3(d), there are $2 \times 3$ threads in block $(2,1)$. Thread $(1,1)$ in this block, which is marked with purple color, works on half of the CI tests for edge $\left(V_{2}, V_{5}\right)$. Thread $(0,1)$ works on the other half.

Shared Memory: The threads in block $(b y, b x)$ frequently access different elements in row $b y$ in $A_{G}^{\prime}$. Therefore, in order to speedup the memory accesses, the entire row is copied into the block's shared memory, i.e., into vector $A_{s h}^{\prime}$. See Fig. 3(c).

Index Calculations: Let $\left(V_{i}, V_{j}\right)$ denote the target edges in block $(b y, b x)$. For all threads within block $(b y, b x), i$ is equal

Algorithm 4 Acceleration of level $\ell \geq 1$ with parallel algorithm cuPC-E. See Section 3.3 and Fig. 3.
Input: $A_{G}, A_{G}^{\prime}, \ell$
Output: $A_{G}$, SepSet
\# of blocks: $n \times n^{\prime} / \beta$
\# of threads / block: $\gamma \times \beta$
$1: i=b y$
2: $n_{i}^{\prime}=$ size of row $i$ in $A_{G}^{\prime}$
3: Copy the entire row $i$ from matrix $A_{G}^{\prime}$ into vector $A_{s h}^{\prime}$ in shared memory
4: $p=b x \times \beta+t x$
5: $j=A_{s h}^{\prime}[p]$
6: for $\left(t=t y ; t<\binom{n_{i}^{\prime}-1}{\ell} ; t=t+\gamma\right)$ do
7: if $\left(A_{G}[i, j]==1\right)$ then
8: $\quad P_{1 \times \ell}=\operatorname{Comb}\left(n_{i}^{\prime}-1, \ell, t, p\right)$
9: $\quad S_{1 \times \ell}=A_{s h}^{\prime}[P]$
10: Perform $I\left(V_{i}, V_{j} \mid S\right)$
11: if $\left(V_{i} \perp V_{j} \mid S\right)$ then
12: $\quad A_{G}[i, j]=A_{G}[j, i]=0$
13: $\quad$ Store $S$ in SepSet
14: end if
15: end if
16: end for
![img-2.jpeg](img-2.jpeg)

Fig. 3. Blocks and threads in cuPC-E parallel algorithm. In this example, $n=7, n^{\prime}=6, \beta=3, \gamma=2$ and $\ell=2$. Block $(2,1)$ is marked with green color, and thread $(1,1)$ in this block is marked with purple color. For threads $(0,1)$ and $(1,1)$ in block $(2,1), S$ is selected from set $\{0,1,3,4,6\}$.
to by. See line 1 in Algorithm 4. For thread $(t y, t x)$ in this block, $j$ is equal to the $t x$-th element in the green portion of the corresponding row, i.e., element $b x \times \beta+t x$ in $A_{s h}^{\prime}$. See lines $4-5$ in Algorithm 4, and also, Fig. 3(c).

Combinations: Consider all CI tests $I\left(V_{i}, V_{j} \mid S\right)$ for edge $\left(V_{i}, V_{j}\right)$. Set $S$ is formed by selecting $\ell$ elements from row $i$ in $A_{G}^{\prime}$ or equivalently from $A_{s h}^{\prime}$. Since element $j$ in this row should not be selected, there will remain $n_{i}^{\prime}-1$ elements to choose from. Therefore, there are a total of $\binom{n_{i}^{\prime}-1}{\ell}$ possible combinations for set $S$. CI tests of an edge $\left(V_{i}, V_{j}\right)$ are split among $\gamma$ threads. In the example of Fig. 3(d), $i=2$ and $j=5$. Hence, $S$ is selected from $\{0,1,3,4,6\}$. There are

$\binom{5}{2}=10$ possible combinations for $S$. Each of the $\gamma=2$ threads sequentially perform $10 / 2=5$ of these tests. See lines $6-10$ in Algorithm 4, and also, Fig. 3(d). $P$ is an array of pointers that point to the selected elements. For instance, when $t=9$ (the last combination), we have $P=\{3,5\}$ and $S=\left\{V_{4}, V_{6}\right\}$. The Comb function returns $t$-th combination in parallel, while skipping the unwanted combinations that include $p$, i.e., the pointer to $j$. Different parallel threads call this function with different values of $t$. The internal details of the Comb function are discussed later in Section 4.2.

Edge Removal: In lines $10-14$, one CI test $I\left(V_{i}, V_{j} \mid S\right)$ is performed, and if $V_{i} \Perp V_{j} \mid S$, the edge $\left(V_{i}, V_{j}\right)$ is removed from $A_{G}$. As mentioned before in Algorithm 1, the conditional sets $S$ are selected from $G^{\prime}$ but the edges are removed from $G$.

Key Features: Important features of cuPC-E parallel algorithm are discussed in the following. I) cuPC-E offers two degrees of parallelism, in specific, processing all the edges in parallel, and for every edge, performing the CI tests in parallel. Although abundant parallelism is available, parallelizing all such tests does not yield the highest performance. cuPC-E does not fully parallelize all CI tests for an edge. The number of CI tests for edge $\left(V_{i}, V_{j}\right)$ is equal to $\binom{n_{i}^{\prime}-1}{\ell}$, while these CI tests are performed by only $\gamma$ parallel threads. In the example of Fig. 3(d), for edge $\left(V_{2}, V_{5}\right), 10$ tests are performed by 2 parallel threads. When one of these $\gamma$ threads removes the target edge, we no longer need to perform the rest of the CI tests for that edge. The if statement in line 7 in Algorithm 4 blocks these unnecessary tests. $\gamma=1$ avoids all the unnecessary tests but is sequential, and $\gamma=\binom{n_{i}^{\prime}-1}{\ell}$ is fully parallel but does not avoid any of the unnecessary tests. Parallel algorithm cuPC-E, therefore, strikes a balance by judiciously employing partial parallelism of the CI tests.
II) Edge removals are monitored in parallel in order to avoid unnecessary tests. In specific, when edge $\left(V_{i}, V_{j}\right)$ is removed by another block, i.e., by a block with $b y=j$, the same if statement in line 7 in Algorithm 4 blocks the unnecessary tests.
III) All indices required for fetching sets $S$ are calculated on-the-fly and also in parallel based on a combination function (Section 4.2), and hence, cuPC-E does not use extra memory for storing the indices.
IV) Processing the compacted version of the adjacency matrix removes unnecessary checks for zero elements of $A_{G}$, reduces total number of combinations for set $S$, and also leads to better cache performance. The compacted format is judiciously selected to match the proposed method.
V) Use of shared memory for the rows of $A_{G}^{\prime}$ increases the performance. Note that every block has only one copy of its corresponding row but processes $\beta$ edges. Storing the correlation matrix $C$ or the set of combinations in shared memory is not beneficial.

### 3.4 Level $\ell \geq 1$ : Parallel Algorithm cuPC-S

Every CI test $I\left(V_{i}, V_{j} \mid S\right)$ includes computing pseudoinverse of a matrix $M_{2}$. See Sections 4.3 and 4.4 for the details. Pseudo-inverse computations are time consuming. cuPC-S employs the following idea in order to accelerate the process. The matrix $M_{2}$, which requires inversion, depends

Algorithm 5 Acceleration of level $\ell \geq 1$ with parallel algorithm cuPC-S. See Section 3.4 and Fig. 4.
Input: $A_{G}, A_{G}^{\prime}, \ell$
Output: $A_{G}$, SepSet
\# of blocks: $n \times \delta$
\# of threads / block: $\theta \times 1$
$i=b y$
$n_{i}^{\prime}=$ size of row $i$ in $A_{G}^{\prime}$
Copy the entire row $i$ from matrix $A_{G}^{\prime}$ into vector $A_{s h}^{\prime}$ in shared memory
for $\left(t=b x \times \theta+t y ; t<\binom{n_{i}^{\prime}}{\ell} ; t=t+\theta \times \delta\right)$ do
$P_{1 \times \ell}=\operatorname{Comb}\left(n^{\prime}, \ell, t\right)$
$S_{1 \times \ell}=A_{s h}^{\prime}[P]$
Form matrix $M_{2}$ based on set $S$ (Section 4.3)
$M_{2}^{-1}=$ Pseudo-inverse of $M_{2}$ (Section 4.4)
for $p=0$ to $n_{i}^{\prime}$ do
$j=A_{s h}^{\prime}[p]$
if $(j \notin S)$ then
if $\left(A_{G}[i, j]==1\right)$ then
Perform $I\left(V_{i}, V_{j} \mid S\right)$
if $\left(V_{i} \Perp V_{j} \mid S\right)$ then
$A_{G}[i, j]=A_{G}[j, i]=0$
Store $S$ in SepSet
end if
end if
end for
end for
only on set $S$, and not $V_{i}$ or $V_{j}$. See Equation 4. Therefore, by assigning the CI tests that depend on the same set $S$ to a single thread, it is possible to avoid multiple calculations of the same pseudo-inverse by sharing it among the CI tests. See Algorithm 5.

Blocks and Threads: cuPC-S kernel consists of $n \times \delta$ blocks. For a given row $i$ in $A_{G}^{\prime}$, there exist $\binom{n_{i}^{\prime}}{\ell}$ possible sets $S$ of size $\ell$. Processing of these sets are split among $\delta$ blocks, each containing $\theta$ threads. Each one of these $\delta \times \theta$ threads, therefore, is responsible for processing $\binom{n_{i}^{\prime}}{\ell} /(\delta \times \theta)$ sets $S$.

Fig. 4 illustrates a small example. Row 2 contains $n_{2}^{\prime}=6$ elements. Therefore, there are $\binom{n_{2}^{\prime}}{\delta}=15$ possible sets $S$ for this row, which are split among $\delta=2$ blocks, each containing $\theta=4$ threads. See Fig. 4(b). Block $(2,1)$ is marked with green color, and thread 0 within this block is marked with purple color. This thread works on two sets $S$, in specific, $S=\left\{V_{0}, V_{6}\right\}$ and $S=\left\{V_{4}, V_{5}\right\}$.

Index Calculations: Lines $1-3$ in Algorithm 5 are similar to cuPC-E. Since every thread that is assigned to row $i=b y$ in cuPC-S is responsible for processing $\binom{n_{i}^{\prime}}{\ell} /(\delta \times \theta)$ sets $S$, the for loop in line 4 iterates $\binom{n_{i}^{\prime}}{\ell} /(\delta \times \theta)$ times. In Fig. 4(b), it iterates twice, for instance, we have $t=1 \times 4+0=4$ and $t=4+8=12$ in thread 0 in block $(2,1)$.

In every iteration, one set $S$ is selected based on the value of $t$. This is done using the Comb function. See lines $5-6$ in Algorithm 5. The selected set $S$ is used to perform a number of CI tests $I\left(V_{i}, V_{j} \mid S\right)$. Since matrix $M_{2}$ depends only on $S$, and not $V_{i}$ or $V_{j}$, we compute this matrix and its pseudoinverse once and use the results in all these CI tests. See lines $7-8$.

![img-3.jpeg](img-3.jpeg)

Fig. 4. Blocks and threads in cuPC-S parallel algorithm. In this example, $n=7, n^{\prime}=6, \delta=2, \theta=4$ and $\ell=2$. Block $(2,1)$ is marked with green color, and thread 0 in this block is marked with purple color. In the second loop iteration in this thread, we have $t=12$, and hence, $S=\{4,5\}$ (red color). Therefore, $j$ is equal to $0,1,3$, and finally 6 (orange color).

In the target CI tests $I\left(V_{i}, V_{j} \mid S\right), i=b y$ and different values of $j$ are determined in lines $9-11$ by iterating through all adjacent nodes of $V_{i}$ and selecting the ones which are not in $S$. As an example, consider thread 0 in block $(2,1)$ in Fig. 4. This thread has two loop iterations: $t=4$ and $t=12$. In the second iteration $(t=12)$, we have $S=\left{V_{4}, V_{5}\right}$ which is marked with red color in the figure. As a result, $V_{j}$ 's are the other adjacent nodes of $V_{i}$, namely, $V_{0}, V_{1}, V_{3}$ and finally $V_{6}$. They are marked with orange color. See Fig. 4(c). Hence, in the second iteration $(t=12)$ in thread 0 in block $(2,1)$, the following CI tests are performed: $I\left(V_{2}, V_{0} \mid\left{V_{4}, V_{5}\right}\right), I\left(V_{2}, V_{1} \mid\left{V_{4}, V_{5}\right}\right)$, $I\left(V_{2}, V_{3} \mid\left{V_{4}, V_{5}\right}\right)$, and $I\left(V_{2}, V_{6} \mid\left{V_{4}, V_{5}\right}\right)$.

Edge Removal: Lines $12-18$ in Algorithm 5 are similar to cuPC-E, except that line 13 executes faster because part of performing a CI test is to compute pseudo-inverse $M_{2}^{-1}$ which is already computed in line 8 .

Key Features: Similar to cuPC-E parallel algorithm, cuPCS $I$ ) works on $A_{G}^{\prime}$ which is the compacted version of the adjacency matrix, $I I$ ) employs shared memory, $I I I$ ) skips unnecessary CI tests via the if statement in line 12 in Algorithm 5, and IV) employs a parallel combination function to compute the indices of sets $S$. V) More importantly, sharing one pseudo-inverse among multiple CI tests brings a large saving.
VI) In the CUDA framework, every 32 threads within a block form a warp. Therefore, in order to maximize GPU utilization, the number of threads within a block, i.e., $\theta$, should be a multiple of 32 . However, $\binom{n_{i}^{\prime}}{\ell}$ might not be divisible by $\delta \times \theta$. cuPC-S employs the following idea in order to resolve this issue. Blocks do not process all their assigned sets $S$ in parallel. Instead, they iterate multiple times and in every iteration, process $\theta$ sets $S$, where $\theta$ is a multiple of 32 . As a result, only the last iteration may not contain a multiple of 32 active threads.
VII) There are many CI tests $I\left(V_{i}, V_{j} \mid S\right)$ that share the same set $S$. For instance, in Fig. 4, $S=\left{V_{4}, V_{5}\right}$ can be
shared among CI tests in not only row 2 but also row 0 because both of these rows have elements 4 and 5, i.e., because both $V_{0}$ and $V_{2}$ are connected to $V_{4}$ and $V_{5}$. See Fig. 4(a). cuPC-S only shares a set $S$ and its corresponding pseudo-inverse $M_{2}^{-1}$ locally. In other words, a set $S$ is shared only among the CI tests $I\left(V_{i}, V_{j} \mid S\right)$ with the same value $i$, i.e., among the CI tests of edges which are connected to the same $V_{i}$. This is in contrast to sharing a set $S$ globally, i.e., among all CI tests from the entire graph. While global sharing may yield more savings, it requires searching the entire graph. The amount of extra saving is not large enough to justify the additional cost of global search. Section 5.5 demonstrates this point through an experiment.

## 4 FURTHER DETAILS OF CUPC

### 4.1 Early Termination

So far we have discussed only one of the early termination strategies employed in cuPC, in specific, the if statements in line 7 in Algorithm 4, and line 12 in Algorithm 5. There are other cases where further processing is no longer required, and threads may terminate early in order to save time. Such cases are listed in the following. For brevity, their corresponding if statements are not shown in Algorithm 4 and Algorithm 5. I) If the number of adjacent nodes of $V_{i}$ is less than $\ell+1$, i.e., $n_{i}^{\prime}<\ell+1$, then all threads in the corresponding blocks are terminated because we need at least one adjacent node $V_{j}$ plus $\ell$ other adjacent nodes for set $S$. II) In block $(b y, b x)$ in cuPC-E, if $b x \times \beta \geq n_{i}^{\prime}$, all threads terminate. This is because $n_{i}^{\prime}$, i.e., the number of edges to be processed in row $i=b y$, is too small to require the processing power of this block. III) Similarly, in block $(b y, b x)$ in cuPC-S, if $b x \times \theta \geq\binom{n_{i}^{\prime}}{\ell}$, all threads terminate. This is because $\binom{n_{i}^{\prime}}{\ell}$, i.e., the number of sets $S$ in row $i=b y$, is too small.

### 4.2 Computing Sets of Combination in Parallel

The Comb function employed in Algorithm 4 and Algorithm 5 is discussed in this section. Let $O=$ $\left{O_{0}, O_{1}, O_{2}, \cdots, O_{\binom{n}{\ell}-1}\right}$ be the set of all possible combinations of choosing $\ell$ elements from set $\{1,2,3, \cdots, n\}$ in lexicographical order. For instance, when $n=3$ and $\ell=2$, we have $O_{0}=[1,2], O_{1}=[1,3]$, and $O_{2}=[2,3]$. Given $n, \ell$ and $t$, the algorithm in [39] directly computes vector $O_{t}$ without requiring to compute the entire set $O$. Thus, by utilizing this algorithm in every thread, every $O_{t}$ is derived separately.

There are $\ell$ elements in $O_{t}$. Let $O_{t}=\left[O_{t}[0], \ldots, O_{t}[\ell-1]\right]$ and $O_{t}[-1]=0$. According to [39], the following statement holds true:

$$
t=\sum_{c=0}^{\ell-1} \sum_{k=O_{t}[c-1]+1}^{O_{t}[c]-1}\binom{n-k}{\ell-(c+1)}
$$

Based on the above equation, Algorithm 6 iteratively computes $O_{t}$. The algorithm has $\ell$ iterations. In iteration $c$, $O_{t}[c]$ is computed. The value of $S u m$ must be less than or equal to, and also, as close as possible to the value of $t$.

Once all the $\ell$ elements in $O_{t}$ are computed in Algorithm 6 , the following minor modifications are performed

Algorithm 6 Combination function.
Input: $n, \ell, t, p$
Output: $O_{t}$
1: Sum $=0$
2: $O_{t}[-1]=0$
3: for $c=0$ to $\ell-1$ do
4: $\quad O_{t}[c]=O_{t}[c-1]$
5: while Sum $\leq t$ do
6: $\quad O_{t}[c]=O_{t}[c]+1$
7: $\quad$ Sum $=$ Sum $+\binom{n-O_{t}[c]}{\ell-(c+1)}$
8: end while
9: Sum $=$ Sum $-\binom{n-O_{t}[c]}{\ell-(c+1)}$
10: end for
in order to use the results in cuPC-E and cuPC-S parallel algorithms. In cuPC-S, since all indices start from zero (and not one), all elements in $O_{t}$, i.e., the output of Algorithm 6, are decremented by 1 . In cuPC-E, in addition to the above modification, we also need to skip all the combinations which include $p$, i.e., the index of $j$. Hence, we set the input of the Comb function to $n_{i}^{\prime}-1$ instead of $n_{i}^{\prime}$, and also, increment all the values which are larger than or equal to $p$ by 1 .

### 4.3 CI Tests

In practice, the CI tests need to be performed based on data samples observed from the random variables. In particular, for multivariate normal distribution, CI test $I\left(V_{i}, V_{j} \mid S\right)$ can be performed based on partial correlations. Let $\rho\left(V_{i}, V_{j} \mid S\right)$ be the partial correlation between $V_{i}$ and $V_{j}$ given $S$. Then, we have $V_{i} \perp V_{j} \mid S$ if and only if $\rho\left(V_{i}, V_{j} \mid S\right)$ is zero. The exact procedure is described below: Let $C_{n \times n}$ be the correlation matrix among the $n$ random variables in the set $\mathcal{V}$, and $C\left[V_{i}, V_{j}\right]$ be $(i, j)$-th entry in matrix $C$. We define a $1 \times \ell$ vector $C\left(V_{i}, S\right)$ as

$$
C\left(V_{i}, S\right):=\left[C\left[V_{i}, S[1]\right], C\left[V_{i}, S[2]\right], \ldots C\left[V_{i}, S[\ell]\right]\right]_{1 \times \ell}
$$

where $S[k]$ is the $k$-th element in the set $S$. In order to compute $\rho\left(V_{i}, V_{j} \mid S\right)$, we first extract $M_{0}, M_{1}$, and $M_{2}$ matrices from the correlation matrix as the following:

$$
\begin{aligned}
& M_{0}=\left[\begin{array}{cc}
C\left[V_{i}, V_{i}\right] & C\left[V_{i}, V_{j}\right] \\
C\left[V_{j}, V_{i}\right] & C\left[V_{j}, V_{j}\right]
\end{array}\right]_{2 \times 2}, \quad M_{1}=\left[\begin{array}{c}
C\left(V_{i}, S\right) \\
C\left(V_{j}, S\right)
\end{array}\right]_{2 \times \ell} \\
& M_{2}=\left[\begin{array}{c}
C(S[1], S) \\
C(S[2], S) \\
\vdots \\
C(S[\ell], S)
\end{array}\right]_{\ell \times \ell}
\end{aligned}
$$

Next, we obtain matrix $H=M_{0}-M_{1} \times M_{2}^{-1} \times M_{1}^{T}$. Note that $M_{2}$ might be ill-conditioned, and hence, $M_{2}^{-1}$ needs to be computed using a pseudo-inverse algorithm (Section 4.4). Once $H$ which is a $2 \times 2$ matrix is computed, an estimation of $\rho\left(V_{i}, V_{j} \mid S\right)$ is computed as the following:

$$
\hat{\rho}\left(V_{i}, V_{j} \mid S\right)=\frac{H[1,2]}{\sqrt{H[1,1] \times H[2,2]}}
$$

Algorithm 7 Pseudo-inverse method.
Input: $M_{2}$
Output: $M_{2}^{-1}$
1: $L=$ Cholesky Factorization $\left(M_{2}^{T} \times M_{2}\right)$
2: $R=\left(L^{T} \times L\right)^{-1}$
3: $M_{2}^{-1}=L \times R \times R \times L^{T} \times M_{2}^{T}$

In order to test whether the value of $\hat{\rho}\left(V_{i}, V_{j} \mid S\right)$ implies $V_{i} \perp V_{j} \mid S$, we compute Fisher's z-transform [34] as

$$
Z\left(\hat{\rho}\left(V_{i}, V_{j} \mid S\right)\right)=\left|\frac{1}{2} \times \ln \left(\frac{1+\hat{\rho}\left(V_{i}, V_{j} \mid S\right)}{1-\hat{\rho}\left(V_{i}, V_{j} \mid S\right)}\right)\right|
$$

and compare it with the following threshold:

$$
\tau=\frac{\Phi^{-1}\left(1-\frac{\alpha}{2}\right)}{\sqrt{m-|S|-3}}
$$

where $m, \alpha$ and $\Phi$ are the size of data samples for every random variable, the significance level for testing partial correlations, and CDF of standard normal distribution, respectively. If $Z\left(\hat{\rho}\left(V_{i}, V_{j} \mid S\right)\right) \leq \tau$, we imply that $V_{i} \perp V_{j} \mid S$. Note that in level zero, the above procedure is reduced to comparing $Z\left(C\left[V_{i}, V_{j}\right]\right)$ with the threshold $\tau$.

We can conclude that a CI test $I\left(V_{i}, V_{j} \mid S\right)$ can be performed based on observational data, in specific, based on the threshold $\tau$ and the correlation matrix $C_{n \times n}$ among the $n$ random variables.

### 4.4 Pseudo-Inverse

As mentioned above, a pseudo-inverse algorithm is needed in order to compute $M_{2}^{-1}$. We employ Moore-Penrose [40] method as shown in Algorithm 7. The pseudo-inverse is computed based on two matrices $L$ and $R$. Matrix $L$ is computed as the full rank Cholesky factorization of matrix $M_{2}^{T} \times M_{2}$. Matrix $R$ is computed as the inverse (the usual inverse) of $L^{T} \times L$.

## 5 EXPERIMENTAL EVALUATION

### 5.1 Source Code

cuPC is implemented in the C language in the CUDA framework. Our parallel implementation is wrapped in a function in the $R$ language with the exact same interface as the original PC-stable function in pcalg [6]. Thus, cuPC is consistent with standard casual learning $R$ packages and can be easily integrated in pcalg. The source code of cuPC is available online [1].

### 5.2 Experiment Setup

We experimentally evaluate cuPC along with the following related previous works. Two different serial implementations of PC-stable [16] algorithm are available as part of the pcalg [41] package. The original one (called "Stable" in pcalg) is implemented in $R$ language, and the recent one (called "Stable.fast") is in C language. A multi-threaded method, called "Parallel-PC" [17], is implemented in $R$ language and is available here [42]. In addition, Stable.fast (i.e., the C implementation in pcalg) supports multi-threaded execution mode as well.

We employ a machine with an Intel Xeon CPU with 8 cores running at 2.5 GHz . Serial methods (Stable and Stable.fast) are executed on a single core, and multi-threaded methods (Parallel-PC and Stable.fast) are executed on all the 8 cores. The CUDA kernels in cuPC are executed on Nvidia GTX 1080 GPU which is hosted on the same machine, and the other procedures in cuPC are executed sequentially on a single core. We employ Ubuntu OS 16.04, gcc version 5.4, and CUDA version 9.2.

Six gene expression datasets are employed as our benchmarks [10], [13], [43]. These are the same benchmarks used in [17]. Table 1 shows the number of random variables and the number of samples in every dataset.

The accuracy of the proposed method is exactly the same as the one of PC-stable which was evaluated extensively in [16] in terms of True Discovery Rate (TDR) and Structural Hamming Distance (SHD). This is because cuPC is GPU-accelerated implementation of the same PC-stable algorithm.

TABLE 1
Benchmark datasets.


### 5.3 Performance Comparison

## Comparing Serial, Multicore, and GPU:

The speedup gained by multicore and GPU implementations over serial implementations are compared in Table 2. In specific, the last column in Table 2 compares three average speedup ratios. The details are discussed below.

The first two rows in Table 2 report runtime of Stable and Parallel-PC. It is noteworthy to mention that ParallelPC has two modes. In every benchmark, both modes are executed and the smaller runtime is reported. Runtime of Stable ranges from 11 minutes in NCI-60 to about 3 days in DREAM5-Insilico. Parallel-PC takes about 11 hours in DREAM5-Insilico, which is 6.7 X faster than Stable. On average, Parallel-PC on eight cores is about 5.6 X faster than Stable.

The third row in Table 2 reports runtime of Stable.fast on a single core. The runtime ranges from 74 seconds in

NCI-60 to more than 11 hours in DREAM5-Insilico. The multi-threaded mode in Stable.fast is not yet optimized at the time of this writing. With full optimizations, the multithreaded mode may reach linear speedup gain on multicore systems. In other words, the speedup gain on eight cores compared to serial execution may reach up to 8 X .

The fourth and fifth rows in Table 2 report runtime of cuPC-E and cuPC-S, respectively. Note that the time it takes to transfer data to and from GPU is counted as well. Runtime of cuPC-E ranges from 440 milliseconds to about 48 seconds. On average, the speedup ratio of cuPC-E over the serial execution in C language, i.e., Stable.fast, is 525 X . Runtime of cuPC-S ranges from 390 milliseconds to 4.76 seconds. On average, the speedup ratio of cuPC-S over serial execution is 1296 X .

## Comparing cuPC with Baseline Methods:

Fig. 5 compares cuPC with the following two baseline GPU-parallel algorithms. The first algorithm is formed by basically porting parallel-PC [17] from its original multithreaded CPU implementation to GPU. In specific, in every level $\ell$, all rows $i$ of the adjacency matrix are processed in parallel in separate blocks. In block $i$, all edges $\left(V_{i}, V_{j}\right)$ are processed in parallel. All the CI tests for an edge $\left(V_{i}, V_{j}\right)$ are performed sequentially in the corresponding thread. We also apply the same ideas in cuPC, namely, using the same compacted form of the adjacency matrix, using the same shared memory allocations, and using the same early termination strategies.

The second baseline algorithm is formed as the following. In every level $\ell$, all elements $i j$ of the adjacency matrix, i.e., all edges $\left(V_{i}, V_{j}\right)$, are processed in parallel in separate blocks. In block $i j$, all CI tests of edge $\left(V_{i}, V_{j}\right)$ are processed in parallel. Again, the same compact, shared memory, and early termination strategies are also applied.

As illustrated in Fig. 5, cuPC-E is 1.3 X to 3.9 X faster than baseline algorithm 1, and 1.8 X to 3.2 X faster than baseline algorithm 2. This shows that cuPC-E judiciously strikes a balance between the available degrees of parallelism and thus achieves higher performance compared to both of the baseline methods. cuPC-S is faster than cuPCE. For instance in DREAM5-Insilico, which is the most challenging dataset, cuPC-S is 45.8 X and 20.6 X faster than the two baseline methods.

TABLE 2
Comparing serial, multicore, and GPU implementations. The first five rows show the runtime values, which are denoted as T1 to T5. The last three rows show speedup ratios, which are calculated as T1/T2, T3/T4 and T3/T5. The last column compares the geometric mean of speedup ratios.


![img-4.jpeg](img-4.jpeg)

Fig. 5. Comparing the performance of cuPC-E and cuPC-S with two baseline GPU-parallel algorithms. Every bar represents a ratio between two runtime values. For instance, the bottom-right bar means cuPC-S is 20.6 X faster than baseline algorithm 2 in DREAM5-Insilico dataset.
![img-5.jpeg](img-5.jpeg)

Fig. 6. Distribution of the runtime (in percent) for a) cuPC-E and b) cuPC-S, in different levels. The values are normalized to the total runtime in every benchmark.

## Comparing Different Levels:

Fig. 6 shows distribution of the runtime values in different levels in cuPC-E and cuPC-S. Note that the reported runtime of every level includes all the corresponding overheads such as forming $A_{G}^{\prime}$. In the first five benchmarks, level 1 takes between $49 \%$ to $83 \%$ of the total runtime. However, in the last benchmark, level 1 takes less than $10 \%$, but levels 2 to 5 take $90 \%$ and $70 \%$ of the total runtime in cuPC-E and cuPCS, respectively. This figure shows that the computations in all levels contribute to the total runtime.

### 5.4 Configuration Parameters

cuPC-E and cuPC-S have configuration parameters which can be adjusted to improve the performance. The above results are based on executing cuPC-E with $\beta=2$ and $\gamma=32$, and cuPC-S with $\theta=64$ and $\delta=2$. We denote these selected configurations as cuPC-E-2-32 and cuPC-S-642. The effect of different configurations on the performance of cuPC-E and cuPC-S is evaluated in this section.
cuPC-E: 30 different configurations are experimented for cuPC-E. In specific, $\gamma$ and $\beta$ are selected from the set $\{1,2,4, \ldots, 128,256\}$ such that $32 \leq \gamma \times \beta \leq 256$. This bounds the number of threads in every block from 32 to 256. Note that the number of blocks in cuPC-E is equal to $n \times n^{\prime} / \beta$ and the number of threads in every block is equal to $\gamma \times \beta$.

The heat maps in Fig. 7 show the performance improvement or degradation of cuPC-E with different configurations compared to the selected configuration. The heat maps show a variation between 0.3 X to 1.3 X . This is mainly due to the
underlying graph structure in the benchmark datasets. In particular, in denser graphs, the number of adjacent nodes is larger, and therefore, the number of CI tests required for every edge grows. As a result, in every row in the heat maps, configurations with larger $\gamma$ show higher performance because more CI tests are executed in parallel. Note that the number of threads for the CI tests of an edge in cuPC-E is equal to $\gamma$. For instance, in DREAM5-Insilico, cuPC-E-4-64 shows $10 \%$ higher performance compared to cuPC-E-4-8 because 64 threads are assigned to the CI tests of an edge instead of 8 . Note that there is a limit to this gain. In DREAM5-Insilico, the configuration 1-256 shows 10\% lower performance compared to 1-128 because large number of parallel threads result in too many unnecessary CI tests.

As opposed to dense graphs, in sparse graphs higher performance is achieved in configurations with smaller $\gamma$ in every row in the heat maps. For instance, in NCI-60, cuPC-E-2-128 shows $40 \%$ lower performance compared to cuPC-E-2-16.
cuPC-S: 16 different configurations are experimented for cuPC-S. In specific, $\theta \in\{32,64,128,256\}$ and $\delta \in$ $\{1,2,4,8\}$. Note that the number of blocks in cuPC-S is equal to $n \times \delta$ and the number of threads in every block is equal to $\theta$. Fig. 8 shows the performance improvement or degradation of cuPC-S with different configurations compared to the selected configuration.

The heat maps in Fig. 8 show a variation between 0.7 X to 1.2 X . Hence, compared to cuPC-E, cuPC-S shows less variation to the configuration parameters. This is mainly because in cuPC-S, threads are assigned to the conditional sets $S$ instead of the edges. In other words, the number

![img-6.jpeg](img-6.jpeg)

Fig. 7. Comparing different configurations of cuPC-E with the selected configuration $(\beta=2$ and $\gamma=32)$. The $Y$ axis is $\beta$ and the $X$ axis is $\gamma$. Green color means higher speed and red color means lower speed.
![img-7.jpeg](img-7.jpeg)
![img-8.jpeg](img-8.jpeg)
![img-9.jpeg](img-9.jpeg)

Fig. 8. Comparing different configurations of cuPC-S with the selected configuration $(\theta=64$ and $\delta=2)$. The $Y$ axis is $\theta$ and the $X$ axis is $\delta$. Green color means higher speed and red color means lower speed.
of adjacent nodes of $V_{i}$, i.e., $n_{i}^{\prime}$, and hence, $n^{\prime}$ varies in dense or sparse graphs. This causes imbalance workloads in different blocks in cuPC-E. However, in cuPC-S, since $\binom{n_{i}^{\prime}}{l}$ is normally much larger than $n_{i}^{\prime}$, blocks are fully loaded and their workloads are more balanced.

### 5.5 Global Sharing vs Local Sharing in cuPC-S

As mentioned at the end of Section 3, conditional sets $S$ can be shared either locally or globally in cuPC-S in order to save redundant computations and increase the overall speed. We employ a local sharing strategy in which only the CI tests from one row in $A_{G}^{\prime}$ share a set $S$. Global sharing among all CI tests from the entire graph is time consuming because it requires searching the entire graph to find all such CI tests. The amount of extra savings yielded by global sharing is not large enough to justify the additional cost of global search. In this section, we experimentally show the above point.

Fig. 9 shows a histogram. The value of each bin $\left[b_{i}, b_{i+1}\right)$ is equal to the number of conditional sets $S$ that appear in CI tests from at least $b_{i}$ to at most $b_{i+1}-1$ rows of $A_{G}^{\prime}$ in level 2 in DREAM5-Insilico dataset. The figure shows that about $95 \%$ of the redundant conditional sets $S$ appear in at most 40 rows of $A_{G}^{\prime}$. This is much smaller than the total number of rows in this dataset, i.e., $n=1643$. Hence, the cost of global search is not justified.

### 5.6 Scalability

Scalability of the proposed parallel algorithms are evaluated in this section. In specific, performance of cuPC-E and cuPC-S are experimented for different number of variables $(n)$, different number of samples $(m)$, and different graph densities $(d)$.
![img-10.jpeg](img-10.jpeg)

Fig. 9. The percentage of redundant conditional sets $S$ in the entire graph in level 2 of DREAM5-Insilico dataset. See Section 5.5 for further details.

To evaluate the impact of scaling the number of variables, we consider $n=1000,2000,3000$ and 4000 . In every case, ten graphs are generated by randomly drawing an edge between any pairs of variables with probability $d=0.1$. In particular, we first generate a random adjacency matrix $A_{G}$ with independent realizations of Bernoulli random variable with parameter $d$ in the lower triangle of the matrix and zeros in the remaining entries. Next, we replace the ones in $A_{G}$ by independent realizations of a uniform random variable in the range $[0.1,1]$. A non-zero entry $A_{G}[i, j]$ shows that there is a direct causal effect from $V_{j}$ to $V_{i}$. Next, from $i=0$ to $i=n-1$, i.e., from top to bottom, the samples are generated as $V_{i}=N_{i}+\sum_{j=0}^{n} A_{G}[i, j] V_{j}$, where the random variables $N_{i}$ 's have normal distribution and are mutually independent. The sample size for every random variable is set to $m=10000$.

Next, cuPC-E and cuPC-S are executed and the runtimes are measured in every case. The results are shown in Fig. 10(a). Runtime increases with $n$, but cuPC-S al-

![img-11.jpeg](img-11.jpeg)

Fig. 10. Runtime of cuPC-E and cuPC-S with a) different number of variables, b) different sample sizes, and c) different graph densities. Every box-and-whisker plot shows quartiles 1, 2 (median), and 3, plus the lowest point still within 1.5 IQR of the lower quartile, and the highest point still within 1.5 IQR of the upper quartile. The outliers are shown as small circles.

ways has higher performance compared to cuPC-E. We also executed the C implementation of PC-stable on the same datasets. However, even in the smaller graphs (n = 1000), PC-stable could not produce results after 48 hours, and thus, we aborted the job. Hence, cuPC-E is at least 48 × 3600 / 20.3 sec. ≈ 8500 X faster than PC-stable in this case.

Next, the impact of scaling the sample size is experimented. We consider m = 2000, 4000, 6000, 8000, and 10000. Here, n = 1000 and d = 0.1. In every case, ten random graphs are generated as discussed above and runtimes are measured. The results are shown in Fig. 10(b). The runtime increases linearly with the sample size. Increasing the sample size improves the accuracy of the CI tests. This decreases the number of edges that are removed in level ℓ, which in turn, increases the number of CI tests required to be performed in level ℓ + 1.

Finally, the impact of scaling the graph density is experimented. We consider d = 0.1, 0.2, 0.3, 0.4, and 0.5. Here, n = 1000 and m = 10000. The results are shown in Fig. 10(c). Increasing d means the graph is more dense, the number of remaining edges are increased, and hence, the runtime should increase. Runtime of cuPC-E and cuPC-S increases almost linearly from density 0.2 to 0.5. However, at density 0.1, the runtime is much smaller. This is because the runtime changes by optimizing the configuration parameters in every case, while we employ the same configuration across all values of d. Therefore, in some cases, e.g., in d = 0.1, the selected configuration is a better fit and the algorithm runs faster.

## 6 CONCLUSION

In empirical sciences, it is often vital to recover the underlying causal relationships among variables in real-world high-dimensional datasets. In this paper, we proposed a GPU-based parallel algorithm for PC-stable with two variants, i.e., cuPC-E and cuPC-S, to learn causal structures from observational data. Experiments showed the scalability of our prospered algorithms with respect to the number of variables, the number of samples, and different graph densities. Note that the proposed solution also helps to accelerate some other causal structure learning algorithms such as CCD, FCI, and RFCI, because they use PC algorithm as a subroutine.
