# REVERSIBLE MCMC ON MARKOV EQUIVALENCE CLASSES OF SPARSE DIRECTED ACYCLIC GRAPHS ${ }^{1}$ 

By Yangbo He, Jinzhu Jia and Bin Yu<br>Peking University, Peking University and University of California, Berkeley

Graphical models are popular statistical tools which are used to represent dependent or causal complex systems. Statistically equivalent causal or directed graphical models are said to belong to a Markov equivalent class. It is of great interest to describe and understand the space of such classes. However, with currently known algorithms, sampling over such classes is only feasible for graphs with fewer than approximately 20 vertices. In this paper, we design reversible irreducible Markov chains on the space of Markov equivalent classes by proposing a perfect set of operators that determine the transitions of the Markov chain. The stationary distribution of a proposed Markov chain has a closed form and can be computed easily. Specifically, we construct a concrete perfect set of operators on sparse Markov equivalence classes by introducing appropriate conditions on each possible operator. Algorithms and their accelerated versions are provided to efficiently generate Markov chains and to explore properties of Markov equivalence classes of sparse directed acyclic graphs (DAGs) with thousands of vertices. We find experimentally that in most Markov equivalence classes of sparse DAGs, (1) most edges are directed, (2) most undirected subgraphs are small and (3) the number of these undirected subgraphs grows approximately linearly with the number of vertices.

Received September 2012; revised April 2013.
${ }^{1}$ Supported in part by NSFC (11101008, 11101005, 71271211), 973 Program2007CB814905, DPHEC-20110001120113, US NSF Grants DMS-11-07000, DMS-09-07632, DMS-06-05165, DMS-12-28246 3424, SES-0835531 (CDI), US ARO grant W911NF-11-10114 and the Center for Science of Information (CSoI), a US NSF Science and Technology Center, under Grant agreement CCF-0939370. This research was also supported by School of Mathematical Science, the Center of Statistical Sciences, the Key Lab of Mathematical Economics and Quantitative Finance (Ministry of Education), the Key lab of Mathematics and Applied Mathematics (Ministry od Education), and the Microsoft Joint Lab on Statistics and information technology at Peking University.

AMS 2000 subject classifications. 62H05, 60J10, 05C81.
Key words and phrases. Sparse graphical model, reversible Markov chain, Markov equivalence class, Causal inference.

This is an electronic reprint of the original article published by the Institute of Mathematical Statistics in The Annals of Statistics, 2013, Vol. 41, No. 1, 1742-1779. This reprint differs from the original in pagination and typographic detail.

1. Introduction. Graphical models based on directed acyclic graphs (DAGs, denoted as $\mathcal{D}$ ) are widely used to represent causal or dependent relationships in various scientific investigations, such as bioinformatics, epidemiology, sociology and business [12, 13, 19, 20, 24, 32, 35]. A DAG encodes the independence and conditional independence restrictions of variables. However, because different DAGs can encode the same set of independencies or conditional independencies, most of the time we cannot distinguish DAGs via observational data [31]. A Markov equivalence class is used to represent all DAGs that encode the same dependencies and independencies [2, 6, 33]. A Markov equivalence class can be visualized (or modeled) and uniquely represented by a completed partial directed acyclic graph (completed PDAG for short) [6] which possibly contains both directed edges and undirected edges [22]. There exists a one-to-one correspondence between completed PDAGs and Markov equivalence classes [2]. The completed PDAGs are also called essential graphs by Andersson et al. [2] and maximally oriented graphs by Meek [26].

A set of completed PDAGs can be used as a model space. The modeling task is to discover a proper Markov equivalence class in the model space $[3,4,8,9,18,25]$. Understanding the set of Markov equivalence classes is important and useful for statistical causal modeling [14, 15, 21]. For example, if the number of DAGs is large for Markov equivalence classes in the model space, searching based on unique completed PDAGs could be substantially more efficient than searching based on DAGs [6, 25, 27]. Moreover, if most completed PDAGs in the model space have many undirected edges (with nonidentifiable directions), many interventions might be needed to identify the causal directions $[11,17]$.

Because the number of Markov equivalence classes increases superexponentially with the number of vertices (e.g., more than $10^{18}$ classes with 10 vertices) [15], it is hard to study sets of Markov equivalence classes. To our knowledge, only completed PDAGs with a small given number of vertices $(\leq 10)$ have been studied thoroughly in the literature [14, 15, 29]. Moreover, these studies focus on the size of Markov equivalence classes, which is defined as the number of DAGs in a Markov equivalence class. Gillispie and Perlman [15] obtain the true size distribution of all Markov equivalence classes with a given number ( 10 or fewer) of vertices by listing all classes. Peña [29] designs a Markov chain to estimate the proportion of the equivalence classes containing only one DAG for graphs with 20 or fewer vertices.

In recent years, sparse graphical models have become popular tools for fitting high-dimensional multivariate data. The sparsity assumption introduces restrictions on the model space; a standard restriction is that the number of edges in the graph be less than a small multiple of the number of vertices. It is thus both interesting and important to be able to explore the properties of subsets of graphical models, especially with sparsity constraints on the edges.

In this paper, we propose a reversible irreducible Markov chain on Markov equivalence classes. We first introduce a perfect set of operators that determine the transitions of the chain. Then we obtain the stationary distribution of the chain by counting (or estimating) all possible transitions for each state of the chain. Finally, based on the stationary distribution of the chain (or estimated stationary distribution), we re-weigh the samples from the chain. Hence these reweighed samples can be seen as uniformly (or approximately uniformly) generated from the Markov equivalence classes of interest. Our proposal allows the study of properties of the sets that contain sparse Markov equivalence classes in a computationally efficient manner for sparse graphs with thousands of vertices.
1.1. A Markov equivalence class and its representation. In this section, we give a short overview for the representations of a Markov equivalence class.

A graph $\mathcal{G}$ is defined as a pair $(V, E)$, where $V=\left\{x_{1}, \ldots, x_{p}\right\}$ denotes the vertex set with $p$ variables, and $E$ denotes the edge set. Let $n_{\mathcal{G}}=|E|$ be the number of edges in $\mathcal{G}$. A directed (undirected) edge is denoted as $\rightarrow$ or $\leftarrow(-)$. A graph is directed (undirected) if all of its edges are directed (undirected). A sequence $\left(x_{1}, x_{2}, \ldots, x_{k}\right)$ of distinct vertices is called a path from $x_{1}$ to $x_{k}$ if either $x_{i} \rightarrow x_{i+1}$ or $x_{i}-x_{i+1}$ is in $E$ for all $i=1, \ldots, k-1$. A path is partially directed if at least one edge in it is directed. A path is directed (undirected) if all edges are directed (undirected). A cycle is a path from a vertex to itself.

A directed acyclic graph (DAG), denoted by $\mathcal{D}$, is a directed graph which does not contain any directed cycle. Let $\tau$ be a subset of $V$. The subgraph $\mathcal{D}_{\tau}=\left(\tau, E_{\tau}\right)$ induced by the subset $\tau$ has vertex set $\tau$ and edge set $E_{\tau}$, the subset of $E$ which contains the edges with both vertices in $\tau$. A subgraph $x \rightarrow$ $z \leftarrow y$ is called a $v$-structure if there is no edge between $x$ and $y$. A partially directed acyclic graph (PDAG), denoted by $\mathcal{P}$, is a graph with no directed cycle.

A graphical model consists of a DAG and a joint probability distribution. With the graphical model, in general, the conditional independencies implied by the joint probability distribution can be read from the DAG. A Markov equivalence class (MEC) is a set of DAGs that encode the same set of independencies or conditional independencies. Let the skeleton of an arbitrary graph $\mathcal{G}$ be the undirected graph with the same vertices and edges as $\mathcal{G}$, regardless of their directions. Verma and Pearl [36] proved the following characterization of Markov equivalence classes:

Lemma 1 (Verma and Pearl [36]). Two DAGs are Markov equivalent if and only if they have the same skeleton and the same $v$-structures.

This lemma implies that, among DAGs in an equivalence class, some edge orientations may vary, while others will be preserved (e.g., those involved in

![img-0.jpeg](img-0.jpeg)

Fig. 1. Four configurations where $v \rightarrow u$ is strongly protected in $\mathcal{G}$.
a $v$-structure). Consequently, a Markov equivalence class can be represented uniquely by a completed $P D A G$, defined as follows:

Definition 1 (Completed PDAG [6]). The completed PDAG of a DAG $\mathcal{D}$, denoted as $\mathcal{C}$, is a PDAG that has the same skeleton as $\mathcal{D}$, and an edge is directed in $\mathcal{C}$ if and only if it has the same orientation in every equivalent DAG of $\mathcal{D}$.

According to Definition 1 and Lemma 1, a completed PDAG of a DAG $\mathcal{D}$ has the same skeleton as $\mathcal{D}$, and it keeps at least the directed edges that occur in the $v$-structures of $\mathcal{D}$. Another popular name of a completed PDAG is "essential graph" introduced by Andersson et al. [2], who introduce four necessary and sufficient conditions for a graph to be an essential graph; see them in Lemma 2, Appendix A.1. One of the conditions shows that all directed edges in a completed PDAG must be "strongly protected," defined as follows:

Definition 2. Let $\mathcal{G}=(V, E)$ be a graph. A directed edge $v \rightarrow u \in E$ is strongly protected in $\mathcal{G}$ if $v \rightarrow u \in E$ occurs in at least one of the four induced subgraphs of $\mathcal{G}$ in Figure 1.

If we delete all directed edges from a completed PDAG, we are left with several isolated undirected subgraphs. Each isolated undirected subgraph is a chain component of the completed PDAG. Observational data is not sufficient to learn the directions of undirected edges of a completed PDAG; one must perform additional intervention experiments. In general, the size of a chain component is a measure of "complexity" of causal learning; the larger the chain components are, the more interventions will be necessary to learn the underlying causal graph [17].

In learning graphical models [6] or studying Markov equivalence classes [29], Markov chains on completed PDAGs play an important role. We briefly introduce the existing methods to construct Markov chains on completed PDAGs in the next subsection.
1.2. Markov chains on completed PDAGs. To construct a Markov chain on completed PDAGs, we need to generate the transitions among them. In general, an operator that can modify the initial completed PDAG locally

can be used to carry out a transition [6, 27, 29, 34]. Let $\mathcal{C}$ be a completed PDAG. We consider six types of operators on $\mathcal{C}$ : inserting an undirected edge (denoted by InsertU ), deleting an undirected edge (DeleteU), inserting a directed edge (InsertD), deleting a directed edge (DeleteD), making a $v$ structure (MakeV) and removing a $v$-structure (RemoveV). We call InsertU, DeleteU, InsertD, DeleteD, MakeV and RemoveV the types of operators. An operator on a given completed PDAG is determined by two parts: its type and the modified edges. For example, the operator "InsertU $x-y$ " on $\mathcal{C}$ represents inserting an undirected edge $x-y$ to $\mathcal{C}$, and $x-y$ is the modified edge of the operator. A modified graph of an operator is the same as the initial completed PDAG, except for the modified edges of the operator. A modified graph might (not) be a completed PDAG; see Example 1 in Section 2.1, of the Supplementary Material [16].

Madigan et al. [25], Perlman [34] and Peña [29] introduce several Markov chains based on the modified graphs of operators. At each state of these Markov chains, say $\mathcal{C}$, they move to the modified graph of an operator on $\mathcal{C}$ only when the modified graph happens to be a completed PDAG, otherwise, stay at $\mathcal{C}$. In order to move to new completed PDAGs, Madigan et al. [25] search the operators whose modified graphs are completed PDAG by checking Andersson's conditions [2] one by one. Perlman [34] introduces an alternative search approach that is more efficient by "exploiting further" Andersson's conditions.

When the modified graph of an operator on $\mathcal{C}$ is not a completed PDAG, the operator might result in a transition from one completed PDAG $\mathcal{C}$ to another. This operator also results in a "valid" transition. To obtain valid transitions, Chickering [6, 7] introduces the concept of validity for an operator on $\mathcal{C}$. Before defining "valid operator," we need a concept consistent extension. A consistent extension of a PDAG $\mathcal{P}$ is a directed acyclic graph (DAG) on the same underlying set of edges, with the same orientations on the directed edges of $\mathcal{P}$ and the same set of $v$-structures [10, 37]. According to Lemma 1, all consistent extensions of a PDAG $\mathcal{P}$, if they exist, belong to a unique Markov equivalence class. Hence if the modified graph of an operator is a PDAG and has a consistent extension, it can result in a completed PDAG that corresponds to a unique Markov equivalence class. We call it the resulting completed PDAG of the operator. Now a valid operator is defined as below.

Definition 3 (Valid operator). An operator on $\mathcal{C}$ is valid if (1) the modified graph of the operator is a PDAG and has a consistent extension, and (2) all modified edges in the modified graph occur in the resulting completed PDAG of the operator.

The first condition in Definition 3 guarantees that a valid operator results in a completed PDAG. The second condition guarantees that the valid oper-

ator is "effective;" that is, the change brought about by the operator occurs in the resulting completed PDAG. Here we notice that the second condition is implied by the context in Chickering [6]. Below we briefly introduce how to obtain the resulting completed PDAG of a valid operator from the modified graph.

Verma and Pearl [37] and Meek [26] introduce an algorithm for finding the completed PDAG from a "pattern" (given skeleton and $v$-structures). This method can be used to create the completed PDAG from a DAG or a PDAG. They first undirect every edge, except for those edges that participate in a $v$-structure. Then they choose one of the undirected edges and direct it if the corresponding directed edge is strongly protected, as shown in Figure 1(a), (c) or (d). The algorithm terminates when there is no undirected edge that can be directed.

Chickering [6] proposes an alternative approach to obtain the completed PDAG of a valid operator from its modified graph; see Example 2, Section 2.1 of the Supplementary Material [16]. The method includes two steps. The first step generates a consistent extension (a DAG) of the modified graph (a PDAG) using the algorithm described in Dor and Tarsi [10]. The second step creates a completed PDAG corresponding to the consistent extension $[5,6]$. We describe Dor and Tarsi's algorithm and Chickering's algorithms in Section 1 of the Supplementary Material [16].

The approach proposed by Chickering [5, 6] is "more complicated but more efficient" [26] than Meek's method described above. Hence when constructing a Markov chain, we use Chickering's approach to obtain the resulting completed PDAG of a given valid operator from its modified graph.

With a set of valid operators, a Markov chain on completed PDAGs can be constructed. Let $\mathcal{S}_{p}$ be the set of all completed PDAGs with $p$ vertices, $\mathcal{S}$ be a given subset of $\mathcal{S}_{p}$. For any completed PDAG $\mathcal{C} \in \mathcal{S}$, let $\mathcal{O}_{\mathcal{C}}$ be a set of valid operators of interest to be defined later on $\mathcal{C}$ in equation (3.2). A set of valid operators on $\mathcal{S}$ is defined as

$$
\mathcal{O}=\bigcup_{\mathcal{C} \in \mathcal{S}} \mathcal{O}_{\mathcal{C}}
$$

Here we notice that each operator in $\mathcal{O}$ is specific to the completed PDAG that the operator applies to. A Markov chain $\left\{e_{t}\right\}$ on $\mathcal{S}$ based on the set $\mathcal{O}$ can be defined as follows.

Definition 4 (A Markov chain $\left\{e_{t}\right\}$ on $\mathcal{S}$ ). The Markov chain $\left\{e_{t}\right\}$ determined by a set of valid operators $\mathcal{O}$ is generated as follows: start at an arbitrary completed PDAG, denoted as $e_{0}=\mathcal{C}_{0} \in \mathcal{S}$, and repeat the following steps for $t=0,1, \ldots$ :
(1) At the $t$ th step we are at a completed PDAG $e_{t}$.

(2) We choose an operator $o_{e_{t}}$ uniformly from $\mathcal{O}_{e_{t}}$; if the resulting completed PDAG $\mathcal{C}_{t+1}$ of $o_{e_{t}}$ is in $\mathcal{S}$, move to $\mathcal{C}_{t+1}$ and set $e_{t+1}=\mathcal{C}_{t+1}$; otherwise we stay at $e_{t}$ and set $e_{t+1}=e_{t}$.

Given the same operator set, the Markov chain in Definition 4 has more new transition states for any completed PDAG than those based on the modified graphs of operators [25, 29, 34]. This is because some valid operators will result in new completed PDAGs even if their modified graphs are not completed PDAGs. Consequently, the transitions, which are generated by these operators, are not contained in Markov chains based on the modified graphs.

The set $\mathcal{S}$ is the finite state space of chain $\left\{e_{t}\right\}$. Clearly, the sequence of completed PDAGs $\left\{e_{t}: t=0,1, \ldots\right\}$ in Definition 4 is a discrete-time Markov chain $[23,28]$. Let $p_{\mathcal{C} \mathcal{C}^{\prime}}$ be the one-step transition probability of $\left\{e_{t}\right\}$ from $\mathcal{C}$ to $\mathcal{C}^{\prime}$ for any two completed PDAGs $\mathcal{C}$ and $\mathcal{C}^{\prime}$ in $\mathcal{S}$. A Markov chain $\left\{e_{t}\right\}$ is irreducible if it can reach any completed PDAG starting at any state in $\mathcal{S}$. If $\left\{e_{t}\right\}$ is irreducible, there exists a unique distribution $\pi=\left(\pi_{\mathcal{C}}, \mathcal{C} \in \mathcal{S}\right)$ satisfying balance equations (see Theorems 1.7.7 and 1.5.6 in [28])

$$
\pi_{\mathcal{C}}=\sum_{\mathcal{C}^{\prime} \in \mathcal{S}} \pi_{\mathcal{C}^{\prime}} p_{\mathcal{C}^{\prime} \mathcal{C}} \quad \text { for all } \mathcal{C} \in \mathcal{S}
$$

An irreducible chain $e_{t}$ is reversible if there exists a probability distribution $\pi$ such that

$$
\pi_{\mathcal{C}} p_{\mathcal{C} \mathcal{C}^{\prime}}=\pi_{\mathcal{C}^{\prime}} p_{\mathcal{C}^{\prime} \mathcal{C}} \quad \text { for all } \mathcal{C}, \mathcal{C}^{\prime} \in \mathcal{S}
$$

It is well known that $\pi$ is the unique stationary distribution of the discretetime Markov chain $\left\{e_{t}\right\}$ if it is finite, reversible, and irreducible; see Lemma 1.9.2 in [28]. Moreover, the stationary probabilities $\pi_{\mathcal{C}}$ can be calculated efficiently if the Markov chain satisfies equation (1.3).

The properties of the Markov chain $\left\{e_{t}\right\}$ given in Definition 4 depend on the operator set $\mathcal{O}$. To implement score-based searching in the whole set of Markov equivalence classes, Chickering [6] introduces a set of operators with types of InsertU, DeleteU, InsertD, DeleteD, MakeV or ReverseD (reversing the direction of a directed edge), subject to some validity conditions. Unfortunately, the Markov chain in Definition 4 is not reversible if the set of Chickering's operators is used. Our goal is to design a reversible Markov chain, as it makes it easier to compute the stationary distribution, and thereby to study the properties of a subset of Markov equivalence classes.

In Section 2, we first discuss the properties of an operator set $\mathcal{O}$ needed to guarantee that the Markov chain is reversible. Section 2 also explains how to use the samples from the Markov chain to study properties of any given subset of Markov equivalence classes. In Section 3 we focus on studying sets of sparse Markov equivalence classes. Finally, in Section 4, we report the properties of directed edges and chain components in sparse Markov equivalence classes with up to one thousand of vertices.

2. Reversible Markov chains on Markov equivalence classes. Let $\mathcal{S}$ be any subset of the set $\mathcal{S}_{p}$ that contains all completed PDAGs with $p$ vertices, and $\mathcal{O}$ be a set of operators on $\mathcal{S}$ defined in equation (1.1). As in Definition 4, we can obtain a Markov chain denoted by $\left\{e_{t}\right\}$. We first discuss four properties of $\mathcal{O}$ that guarantee that $\left\{e_{t}\right\}$ is reversible and irreducible. They are validity, distinguishability, irreducibility and reversibility. We call a set of operators perfect if it satisfies these four properties. Then we give the stationary distribution of $\left\{e_{t}\right\}$ when $\mathcal{O}$ is perfect and show how to use $\left\{e_{t}\right\}$ to study properties of $\mathcal{S}$.
2.1. A reversible Markov chain based on a perfect set of operators. Let $p_{\mathcal{C} \mathcal{C}^{\prime}}$ be a one-step transition probability of $\left\{e_{t}\right\}$ from $\mathcal{C}$ to $\mathcal{C}^{\prime}$ for any two completed PDAGs $\mathcal{C}$ and $\mathcal{C}^{\prime}$ in $\mathcal{S}$. In order to formulate $p_{\mathcal{C} \mathcal{C}^{\prime}}$ clearly, we introduce two properties of $\mathcal{O}$ : Validity and Distinguishability.

Definition 5 (Validity). Given $\mathcal{S}$ and any completed PDAG $\mathcal{C}$ in $\mathcal{S}$, a set of operators $\mathcal{O}$ on $\mathcal{S}$ is valid if for any operator $o_{\mathcal{C}}$ ( $o$ without confusion below) in $\mathcal{O}_{\mathcal{C}}, o$ is valid according to Definition 3 and the resulting completed PDAG obtained by applying $o$ to $\mathcal{C}$, which is different from $\mathcal{C}$, is also in $\mathcal{S}$.

According to Definition 5, if a set of operators $\mathcal{O}$ on $\mathcal{S}$ is valid, we can move to a new completed PDAG in each step of $\left\{e_{t}\right\}$ and the one-step transition probability of any completed PDAG to itself is zero:

$$
p_{\mathcal{C} \mathcal{C}}=0 \quad \text { for any completed PDAG } \mathcal{C} \in \mathcal{S}
$$

For a set of valid operators $\mathcal{O}$ and any completed PDAG $\mathcal{C}$ in $\mathcal{S}$, we define the resulting completed PDAGs of the operators in $\mathcal{O}_{\mathcal{C}}$ as the direct successors of $\mathcal{C}$. For any direct successor of $\mathcal{C}$, denoted by $\mathcal{C}^{\prime}$, we obtain $p_{\mathcal{C} \mathcal{C}^{\prime}}$ clearly as in equation (2.2) if $\mathcal{O}$ has the following property.

Definition 6 (Distinguishability). A set of valid operators $\mathcal{O}$ on $\mathcal{S}$ is distinguishable if for any completed PDAG $\mathcal{C}$ in $\mathcal{S}$, different operators in $\mathcal{O}_{\mathcal{C}}$ will result in different completed PDAGs.

If $\mathcal{O}$ is distinguishable, for any direct successor of $\mathcal{C}$, denoted by $\mathcal{C}^{\prime}$, there is a unique operator in $\mathcal{O}_{\mathcal{C}}$ that can transform $\mathcal{C}$ to $\mathcal{C}^{\prime}$. Thus, the number of operators in $\mathcal{O}_{\mathcal{C}}$ is the same as the number of direct successors of $\mathcal{C}$. Sampling operators from $\mathcal{O}_{\mathcal{C}}$ uniformly generates a uniformly random transition from $\mathcal{C}$ to its direct successors. By denoting $M\left(\mathcal{O}_{\mathcal{C}}\right)$ as the number of operators in $\mathcal{O}_{\mathcal{C}}$, we have

$$
p_{\mathcal{C} \mathcal{C}^{\prime}}=\left\{\begin{array}{lc}
1 / M\left(\mathcal{O}_{\mathcal{C}}\right), & \mathcal{C}^{\prime} \text { is a direct successor of } \mathcal{C} \in \mathcal{S} \\
0, & \text { otherwise }
\end{array}\right.
$$

We introduce this property because it makes computation of $p_{\mathcal{C} \mathcal{C}^{\prime}}$ efficient: if $\mathcal{O}$ is distinguishable, we know $p_{\mathcal{C} \mathcal{C}^{\prime}}$ right away from $M\left(\mathcal{O}_{\mathcal{C}}\right)$.

In order to make sure the Markov chain $\left\{e_{t}\right\}$ is irreducible and reversible, we introduce two more properties of $\mathcal{O}$ : irreducibility and reversibility.

Definition 7 (Irreducibility). A set of operators $\mathcal{O}$ on $\mathcal{S}$ is irreducible if for any two completed PDAGs $\mathcal{C}, \mathcal{C}^{\prime} \in \mathcal{S}$, there exists a sequence of operators in $\mathcal{O}$ such that we can obtain $\mathcal{C}^{\prime}$ from $\mathcal{C}$ by applying these operators sequentially.

If $\mathcal{O}$ is irreducible, starting at any completed PDAG in $\mathcal{S}$, we have positive probability to reach any other completed PDAG via a sequence of operators in $\mathcal{O}$. Thus, the Markov chain $\left\{e_{t}\right\}$ is irreducible.

Definition 8 (Reversibility). A set of operators $\mathcal{O}$ on $\mathcal{S}$ is reversible if for any completed PDAG $\mathcal{C} \in \mathcal{S}$ and any operator $o \in \mathcal{O}_{\mathcal{C}}$ with $\mathcal{C}^{\prime}$ being the resulting completed PDAG of $o$, there is an operator $o^{\prime} \in \mathcal{O}_{\mathcal{C}^{\prime}}$ such that $\mathcal{C}$ is the resulting completed PDAG of $o^{\prime}$.

If the set of operators $\mathcal{O}$ on $\mathcal{S}$ is valid, distinguishable and reversible, for any pair of completed PDAGs $\mathcal{C}, \mathcal{C}^{\prime} \in \mathcal{S}, \mathcal{C}$ is also a direct successor of $\mathcal{C}^{\prime}$ if $\mathcal{C}^{\prime}$ is a direct successor of $\mathcal{C}$. For any $\mathcal{C} \in \mathcal{S}$ and any of its direct successors $\mathcal{C}^{\prime}$, we have

$$
p_{\mathcal{C} \mathcal{C}^{\prime}}=1 / M\left(\mathcal{O}_{\mathcal{C}}\right) \quad \text { and } \quad p_{\mathcal{C}^{\prime} \mathcal{C}}=1 / M\left(\mathcal{O}_{\mathcal{C}^{\prime}}\right)
$$

Let $\mathcal{T}=\sum_{\mathcal{C} \in \mathcal{S}} M\left(\mathcal{O}_{\mathcal{C}}\right)$, and define a probability distribution as

$$
\pi_{\mathcal{C}}=M\left(\mathcal{O}_{\mathcal{C}}\right) / \mathcal{T}
$$

Clearly, equation (1.3) holds for $\pi_{\mathcal{C}}$ in equation (2.4) if $\mathcal{O}$ is valid, distinguishable and reversible. $\pi_{\mathcal{C}}$ is the unique stationary distribution of $\left\{e_{t}\right\}$ if it is also irreducible $[1,23,28]$.

In the following proposition, we summarize our results about the Markov chain $\left\{e_{t}\right\}$ on $\mathcal{S}$, and give its stationary distribution.

Proposition 1 (Stationary distribution of $\left\{e_{t}\right\}$ ). Let $\mathcal{S}$ be any given set of completed PDAGs. The set of operators is defined as $\mathcal{O}=\bigcup_{\mathcal{C} \in \mathcal{S}} \mathcal{O}_{\mathcal{C}}$ where $\mathcal{O}_{\mathcal{C}}$ is a set of operators on $\mathcal{C}$ for any $\mathcal{C}$ in $\mathcal{S}$. Let $M\left(\mathcal{O}_{\mathcal{C}}\right)$ be the number of operators in $\mathcal{O}_{\mathcal{C}}$. For the Markov chain $\left\{e_{t}\right\}$ on $\mathcal{S}$ generated according to Definition 4, if $\mathcal{O}$ is perfect, that is, the properties - validity, distinguishability, reversibility and irreducibility-hold for $\mathcal{O}$, then:
(1) the Markov chain $\left\{e_{t}\right\}$ is irreducible and reversible;
(2) the distribution $\pi_{\mathcal{C}}$ in equation (2.4) is the unique stationary distribution of $\left\{e_{t}\right\}$ and $\pi_{\mathcal{C}} \propto M\left(\mathcal{O}_{\mathcal{C}}\right)$.

The challenge is to construct a concrete perfect set of operators. In Section 3, we carry out such a construction for a set of Markov equivalence

classes with sparsity constraints and provide algorithms to obtain a reversible Markov chain. We now show that a reversible Markov chain can be used to compute interesting properties of a completed PDAG set $\mathcal{S}$.
2.2. Estimating the properties of $\mathcal{S}$ by a perfect Markov chain. For any $\mathcal{C} \in \mathcal{S}$, let $f(\mathcal{C})$ be a real function describing any property of interest of $\mathcal{C}$, and the random variable $u$ be uniformly distributed on $\mathcal{S}$. In order to understand the property of interest, we compute the distribution of $f(u)$.

Let's consider one example in the literature. The proportion of Markov equivalence classes of size one (equivalently, completed PDAGs that are directed) in $\mathcal{S}_{p}$ is studied in the literature [14, 15, 29]. For this purpose, we can define $f(u)$ as the size of Markov equivalence classes represented by $u$ and obtain the proportion by computing the probability of $\{f(u)=1\}$.

Let $A$ be any subset of $\mathbb{R}$, the probability of $\{f(u) \in A\}$ is

$$
\mathbb{P}(f(u) \in A)=\frac{|\{\mathcal{C}: f(\mathcal{C}) \in A, \mathcal{C} \in \mathcal{S}\}|}{|\mathcal{S}|}=\frac{\sum_{\mathcal{C} \in \mathcal{S}} I_{\{f(\mathcal{C}) \in A\}}}{|\mathcal{S}|}
$$

where $|\mathcal{S}|$ is the number of elements in the set $\mathcal{S}$ and $I$ is an indicator function.

Let $\left\{e_{t}\right\}_{t=1, \ldots, N}$ be a realization of Markov chain $\left\{e_{t}\right\}$ on $\mathcal{S}$ based on a perfect operator set $\mathcal{O}$ according to Definition 4 and $M_{t}=M\left(\mathcal{O}_{e_{t}}\right)$. Let $\pi\left(e_{t}\right)$ be the stationary probability of Markov chain $\left\{e_{t}\right\}$. From Proposition 1, we have $\pi\left(e_{t}\right) \propto M_{t}$ for $t=1, \ldots, N$. We can use $\left\{e_{t}, M_{t}\right\}_{t=1, \ldots, N}$ to estimate the probability of $\{f(u) \in A\}$ by

$$
\hat{\mathbb{P}}_{N}(f(u) \in A)=\frac{\sum_{t=1}^{N} I_{\left\{f\left(e_{t}\right) \in A\right\}} M_{t}^{-1}}{\sum_{t=1}^{N} M_{t}^{-1}}
$$

From the ergodic theory of Markov chains (see Theorem 1.10.2 in [28]), we can get Proposition 2 directly.

Proposition 2. Let $\mathcal{S}$ be a given set of completed PDAGs, and assume the set of operators $\mathcal{O}$ on $\mathcal{S}$ is perfect. The Markov chain $\left\{e_{t}\right\}_{t=1, \ldots, N}$ is obtained according to Definition 4. Then the estimator $\hat{\mathbb{P}}_{N}(\{f(u) \in A\})$ in equation (2.6) converges to $\mathbb{P}(\{f(u) \in A\})$ in equation (2.5) with probability one, that is,

$$
\mathbb{P}\left(\hat{\mathbb{P}}_{N}(f(u) \in A) \rightarrow \mathbb{P}(f(u) \in A) \text { as } N \rightarrow \infty\right)=1
$$

Proposition 2 shows that the estimator defined in equation (2.6) is a consistent estimator of $\mathbb{P}(f(u) \in A)$. We can study any given subset of Markov equivalence classes via equation (2.6) if we can obtain $\left\{e_{t}\right\}_{t=1, \ldots, N}$ and $\left\{M_{t}\right\}_{t=1, \ldots, N}$. We now turn to construct a concrete perfect set of operators for a set of completed PDAGs with sparsity constraints and then introduce algorithms to run a reversible Markov chain.

3. A Reversible Markov chain on completed PDAGs with sparsity constraints. We define a set of Markov equivalence classes $\mathcal{S}_{p}^{n}$ with $p$ vertices and at most $n$ edges as follows:
(3.1) $\mathcal{S}_{p}^{n}=\left\{\mathcal{C}: \mathcal{C}\right.$ is a completed PDAG with $p$ vertices and $\left.n_{\mathcal{C}} \leq n\right\}$,
where $n_{\mathcal{C}}$ is the number of edges in $\mathcal{C}$. Recall that $\mathcal{S}_{p}$ denotes the set of all completed PDAGs with $p$ vertices. Clearly, $\mathcal{S}_{p}^{n}=\mathcal{S}_{p}$ when $n \geq p(p-1) / 2$.

We now construct a perfect set of operators on $\mathcal{S}_{p}^{n}$. Notice that our constructions can be extended to adapt to some other sets of completed PDAGs, say, a set of completed PDAGS with a given maximum degree. In Section 3.1, we construct the perfect set of operators for any completed PDAG in $\mathcal{S}_{p}^{n}$. In Section 3.2, we propose algorithms and their accelerated version for efficiently obtaining a Markov chain based on the perfect set of operators.
3.1. Construction of a perfect set of operators on $\mathcal{S}_{p}^{n}$. In order to construct a perfect set of operators, we need to define the set of operators on each completed PDAG in $\mathcal{S}_{p}^{n}$. Let $\mathcal{C}$ be a completed PDAG in $\mathcal{S}_{p}^{n}$. We consider six types of operators on $\mathcal{C}$ that were introduced in Section 1.2: InsertU, DeleteU, InsertD, DeleteD, MakeV and RemoveV. The operators on $\mathcal{C}$ with the same type but different modified edges constitute a set of operators. We introduce six sets of operators on $\mathcal{C}$ denoted by Insert $U_{\mathcal{C}}$, Delete $U_{\mathcal{C}}$, Insert $D_{\mathcal{C}}$, Delete $D_{\mathcal{C}}$, Make $V_{\mathcal{C}}$ and Remove $V_{\mathcal{C}}$ in Definition 9. In addition to the conditions that guarantee validity, for each type of operators, we also introduce other constraints to make sure that all operators are reversible.

First we explain some notation used in Definition 9. Let $x$ and $y$ be any two distinct vertices in $\mathcal{C}$. The neighbor set of $x$ denoted by $N_{x}$ consists of every vertex $y$ with $x-y$ in $\mathcal{C}$. The common neighbor set of $x$ and $y$ is defined as $N_{x y}=N_{x} \cap N_{y} . x$ is a parent of $y$ and $y$ is a child of $x$ if $x \rightarrow y$ occurs in $\mathcal{C}$. A vertex $u$ is a common child of $x$ and $y$ if $u$ is a child of both $x$ and $y . \Pi_{x}$ represents the set of all parents of $x$.

Definition 9 (Six sets of operators on $\mathcal{C}$ ). Let $\mathcal{C}$ be a completed PDAG in $\mathcal{S}_{p}^{n}$ and $n_{\mathcal{C}}$ be the number of edges in $\mathcal{C}$. We introduce six sets of operators on $\mathcal{C}$ : Insert $U_{\mathcal{C}}$ Delete $U_{\mathcal{C}}$, Insert $D_{\mathcal{C}}$, Delete $D_{\mathcal{C}}$, Make $V_{\mathcal{C}}$ and Remove $\mathrm{V}_{\mathcal{C}}$ as follows.
(a) For any two vertices $x, y$ that are not adjacent in $\mathcal{C}$, the operator "InsertU $x-y$ " on $\mathcal{C}$ is in Insert $U_{\mathcal{C}}$ if and only if $\left(\mathbf{i u}_{1}\right) n_{\mathcal{C}}<n$; (iu $\left.\mathbf{i u}_{2}\right)$ "InsertU $x-y$ " is valid; (iu $\mathbf{i u}_{3}$ ) for any $u$ that is a common child of $x, y$ in $\mathcal{C}$, both $x \rightarrow u$ and $y \rightarrow u$ occur in the resulting completed PDAG of "InsertU $x-y$."
(b) For any undirected edge $x-y$ in $\mathcal{C}$, the operator "DeleteU $x-y$ " on $\mathcal{C}$ is in Delete $U_{\mathcal{C}}$ if and only if (du $\left.\mathbf{u}_{1}\right)$ "DeleteU $x-y$ " is valid.
(c) For any two vertices $x, y$ that are not adjacent in $\mathcal{C}$, the operator "InsertD $x \rightarrow y$ " on $\mathcal{C}$ is in Insert $D_{\mathcal{C}}$ if and only if (id $\left.\mathbf{i}_{1}\right) n_{\mathcal{C}}<n$; (id $\left.\mathbf{i}_{2}\right)$ "InsertD

$x \rightarrow y$ " is valid; $\left(\mathbf{i d}_{3}\right)$ for any $u$ that is a common child of $x, y$ in $\mathcal{C}, y \rightarrow u$ occurs in the resulting completed PDAG of "InsertD $x \rightarrow y$."
(d) For any directed edge $x \rightarrow y$ in $\mathcal{C}$, operator "DeleteD $x \rightarrow y$ " on $\mathcal{C}$ is in Delete $D_{\mathcal{C}}$ if and only if $\left(\mathbf{d d}_{1}\right)$ "DeleteD $x \rightarrow y$ " is valid; $\left(\mathbf{d d}_{2}\right)$ for any $v$ that is a parent of $y$ but not a parent of $x$, directed edge $v \rightarrow y$ in $\mathcal{C}$ occurs in the resulting completed PDAG of "DeleteD $x \rightarrow y$."
(e) For any subgraph $x-z-y$ in $\mathcal{C}$, the operator "MakeV $x \rightarrow z \leftarrow y$ " on $\mathcal{C}$ is in Make $V_{\mathcal{C}}$ if and only if $\left(\mathbf{m v}_{1}\right)$ "MakeV $x \rightarrow z \leftarrow y$ " is valid.
(f) For any $v$-structure $x \rightarrow z \leftarrow y$ of $\mathcal{C}$, the operator "RemoveV $x \rightarrow$ $z \leftarrow y "$ on $\mathcal{C}$ is in Remove $\mathrm{V}_{\mathcal{C}}$ if and only if $\left(\mathbf{r v}_{1}\right) \Pi_{x}=\Pi_{y} ;\left(\mathbf{r v}_{2}\right) \Pi_{x} \cup N_{x y}=$ $\Pi_{z} \backslash\{x, y\} ;\left(\mathbf{r v}_{3}\right)$ every undirected path between $x$ and $y$ contains a vertex in $N_{x y}$.

Munteanu and Bendou [27] discuss the constraints for the first five types of operators such that each one can transform one completed PDAG to another. Chickering [6] introduces the necessary and sufficient conditions such that these five types of operators are valid. We list the conditions introduced by Chickering [6] in Lemma 3, Appendix A.1, and employ them to guarantee that the conditions $\mathbf{i u}_{2}, \mathbf{d u}_{1}, \mathbf{i d}_{2}, \mathbf{d d}_{1}$ and $\mathbf{m v}_{1}$ in Definition 9 hold.

The set of operators on $\mathcal{C}$ denoted by $\mathcal{O}_{\mathcal{C}}$ is defined as follows:

$$
\begin{aligned}
\mathcal{O}_{\mathcal{C}}= & \operatorname{Insert} U_{\mathcal{C}} \cup \operatorname{Delete} U_{\mathcal{C}} \cup \operatorname{Insert} D_{\mathcal{C}} \\
& \cup \operatorname{Delete} D_{\mathcal{C}} \cup \operatorname{Make} V_{\mathcal{C}} \cup \operatorname{Remove} V_{\mathcal{C}}
\end{aligned}
$$

Taking the union over all completed PDAGs in $\mathcal{S}_{p}^{n}$, we define the set of operators on $\mathcal{S}_{p}^{n}$ as

$$
\mathcal{O}=\bigcup_{\mathcal{C} \in \mathcal{S}_{p}^{n}} \mathcal{O}_{\mathcal{C}}
$$

where $\mathcal{O}_{\mathcal{C}}$ is the set of operators in equation (3.2). In the main result of this paper, we show that $\mathcal{O}$ in equation (3.3) is a perfect set of operators on $\mathcal{S}_{p}^{n}$.

THEOREM 1 (A perfect set of operators on $\mathcal{S}_{p}^{n}$ ). $\mathcal{O}$ defined in equation (3.3) is a perfect set of operators on $\mathcal{S}_{p}^{n}$.

Here we notice that $\mathbf{i u}_{3}, \mathbf{i d}_{3}$ and $\mathbf{d d}_{2}$ are key conditions in Definition 9 to guarantee that $\mathcal{O}$ is reversible. Without these three conditions, there are operators that are not reversible; see Example 3, Section 2.1 in the Supplementary Material [16]. We provide a proof of Theorem 1 in Appendix A.2.

The preceding section showed how to construct a perfect set of operators. A toy example is provided as Example 4 in Section 2.1 of the Supplementary Material [16]. Based on the perfect set of operators we can obtain a finite irreducible reversible discrete-time chain. In the next subsection, we provide detailed algorithms for obtaining a Markov chain on $\mathcal{S}_{p}^{n}$ and their accelerated version.

```
Algorithm 1: Road map to construct a Markov chain on \(\mathcal{S}_{p}^{n}\)
    Input:
    \(p\), the number of vertices; \(n\), the maximum number of edges; \(N\), the length of
    Markov chain.
    Output:
    \(\left\{e_{t}, M_{t}\right\}_{t=1, \ldots, N}\), where \(\left\{e_{t}\right\}\) is Markov chain and \(M_{t}\) is the number of operators in
    \(\mathcal{O}_{e_{t}}\).
    Initialize \(e_{0}\) as any completed PDAG in \(\mathcal{S}_{p}^{n}\)
    for \(t \leftarrow 0\) to \(N\) do
        Step A Construct the set of operators \(\mathcal{O}_{e_{t}}\) in equation (3.2) via Algorithm 1.1;
        Step B Let \(M_{t}\) be the number of operators in \(\mathcal{O}_{e_{t}}\);
        Step C Randomly choose an operator \(o\) uniformly from \(\mathcal{O}_{e_{t}}\);
        Step D Apply operator \(o\) to \(e_{t}\). Set \(e_{t+1}\) as the resulting completed PDAG of \(o\).
    return \(\left\{e_{t}, M_{t}\right\}_{t=1, \ldots, N}\).
```

3.2. Algorithms. In this subsection, we provide the algorithms in detail to generate a Markov chain on $\mathcal{S}_{p}^{n}$, defined in Definition 4 based on the perfect set of operators defined in (3.3). A sketch of Algorithm 1 is shown below; some steps of this algorithm are further explained in the subsequent algorithms.

Step A of Algorithm 1 constructs the sets of operators on completed PDAGs in the chain $\left\{e_{t}\right\}$. It is the most difficult step and dominates the time complexity of Algorithm 1. Step B and Step C can be implemented easily after $\mathcal{O}_{e_{t}}$ is obtained. Step D can be implemented via Chickering's method [6] that was mentioned in Section 1.2. We will show that the time complexity of obtaining a Markov chain on $\mathcal{S}_{p}^{n}$ with length $N\left(\left\{e_{t}\right\}_{t=1, \ldots, N}\right)$ is approximate $O\left(N p^{3}\right)$ if $n$ is the same order of $p$. For large $p$, we also provide an accelerated version that, in some cases, can run hundreds of times faster.

The rest of this section is arranged as follows. In Section 3.2.1, we first introduce the algorithms to implement Step A. In Section 3.2.2 we discuss the time complexity of our algorithm, and provide an acceleration method to speed up Algorithm 1.
3.2.1. Implementation of Step A in Algorithm 1. A detailed implementation of Step A (to construct $\mathcal{O}_{e_{t}}$ ) is described in Algorithm 1.1. To construct $\mathcal{O}_{e_{t}}$ in Algorithm 1.1, we go through all possible operators on $e_{t}$ and choose those satisfying the corresponding conditions in Definition 9.

The conditions in Algorithm 1.1 include: $\mathbf{i u}_{1}, \mathbf{i u}_{2}, \mathbf{i u}_{3}, \mathbf{d u}_{1}, \mathbf{i d}_{1}, \mathbf{i d}_{2}, \mathbf{i d}_{3}$, $\mathbf{d d}_{1}, \mathbf{d d}_{2}, \mathbf{r m}_{1}, \mathbf{r v}_{1}, \mathbf{r v}_{2}$ and $\mathbf{m v}_{1}$. For each possible operator, we check the corresponding conditions shown in Algorithm 1.1 one-by-one until one of them fails. Below, we introduce how to check these conditions.

```
Algorithm 1.1: Construct \(\mathcal{O}_{e_{t}}\) for a completed PDAG \(e_{t}\).
    Input: A completed PDAG \(e_{t}\) with \(p\) vertices.
    Output: Operator set \(\mathcal{O}_{e_{t}}\).
    // All sets of possible modified edges of \(e_{t}\) used below,
        for example, Undirected-edges \(_{e_{t}}\), are generated according
        to Definition 9.
    1 Set \(\mathcal{O}_{e_{t}}\) as empty set
    2 for each undirected edge \(x-y\) in Undirected-edges \(_{e_{t}}\) do
        consider operator DeleteU \(x-x\), add it to \(\mathcal{O}_{e_{t}}\) if \(\mathbf{d u}_{1}\) holds,
    for each directed edge \(x \rightarrow y\) in Directed-edges \(_{e_{t}}\) do
        consider DeleteD \(x \rightarrow x\), add it to \(\mathcal{O}_{e_{t}}\) if both \(\mathbf{d d}_{1}\) and \(\mathbf{d d}_{2}\) hold;
    for each \(v\)-structure \(x \rightarrow z \leftarrow y\) in \(V\)-structures \(_{e_{t}}\) do
        consider RemoveV \(x_{k} \rightarrow x_{i} \leftarrow x_{l}\), add it to \(\mathcal{O}_{e_{t}}\) if \(\mathbf{r v}_{1}, \mathbf{r v}_{2}\) and \(\mathbf{r v}_{3}\) hold,
    for each undirected \(v\)-structure \(x-z-y\) in Undirected- \(v\)-structures \(_{e_{t}}\) do
        consider MakeV \(x_{k} \rightarrow x_{i} \leftarrow x_{l}\), add it to \(\mathcal{O}_{e_{t}}\) if \(\mathbf{m v}_{1}\) holds,
    if \(n_{e_{t}}<n\) (i.e., \(\mathbf{i u}_{1}\) or \(\mathbf{i d}_{1}\) holds) then
        for each pair \((x, y)\) in Pairs-nonadj \(_{e_{t}}\) do
            consider InsertU \(x-y\), add it to \(\mathcal{O}_{e_{t}}\) if \(\mathbf{i u}_{1}, \mathbf{i u}_{2}\), and \(\mathbf{i u}_{3}\) hold;
            consider InsertD \(x \rightarrow y\), add it to \(\mathcal{O}_{e_{t}}\), if \(\mathbf{i d}_{1}, \mathbf{i d}_{2}\) and \(\mathbf{i d}_{3}\) hold;
            consider InsertD \(x \leftarrow y\), add it to \(\mathcal{O}_{e_{t}}\) if \(\mathbf{i d}_{1}, \mathbf{i d}_{2}\) and \(\mathbf{i d}_{3}\) hold.
    return \(\mathcal{O}_{e_{t}}\)
```

The conditions $\mathbf{i u}_{3}, \mathbf{i d}_{3}$ and $\mathbf{d d}_{2}$ in Algorithm 1.1 depend on both $e_{t}$ and the resulting completed PDAGs of the operators. Intuitively, checking $\mathbf{i u}_{3}$, $\mathbf{i d}_{3}$ or $\mathbf{d d}_{2}$ requires that we obtain the corresponding resulting completed PDAGs. We know that the time complexity of getting a resulting completed PDAG of $e_{t}$ is $O\left(p n_{e_{t}}\right)[6,10]$, where $n_{e_{t}}$ is the number of edges in $e_{t}$. To avoid generating resulting completed PDAG, in the Supplementary Material [16], we provide three algorithms to check $\mathbf{i u}_{3}, \mathbf{i d}_{3}$ and $\mathbf{d d}_{2}$ only based on $e_{t}$ and in an efficient manner.

The other conditions can be tested via classical graph algorithms. These tests include: (1) whether two vertex sets are equal or not, (2) whether a subgraph is a clique or not and (3) whether all partially directed paths or all undirected paths between two vertices contain at least one vertex in a given set. Checking the first two types of conditions is trivial and very efficient because the sets involved are small for most completed PDAGs in $\mathcal{S}_{p}^{n}$ when $n$ is of the same order of $p$. To check the conditions with the third type, we just need to check whether there is a partially directed path or undirected path between two given vertices not through any vertices in the given set. We

check this using a depth-first search from the source vertex. When looking for an undirected path, we can search within the corresponding chain component that includes both the source and the destination vertices.
3.2.2. Time complexity of Algorithm 1 and an accelerated version. We now discuss the time complexity of Algorithm 1. For $e_{t} \in \mathcal{S}_{p}^{n}$, let $p$ and $n_{t}$ be the number of vertices and edges in $e_{t}$, respectively, $k_{t}$ be the number of $v$ structures in $e_{t}$, and $k_{t}^{\prime}$ be the number of undirected $v$-structures (subgraphs $x-y-z$ with $x$ and $z$ nonadjacent) in $e_{t}$. To construct $\mathcal{O}_{e_{t}}$, in Step A of Algorithm 1 (equivalently, Algorithm 1.1), all possible operators we need to go through: $n_{t}$ deleting operators (DeleteU and DeleteD), $3\left(p(p-1) / 2-n_{t}\right)$ inserting operators (InsertU and InsertD) when the number of edges in $e_{t}$ is less than $n, k_{t}$ RemoveV operators and $k_{t}^{\prime}$ MakeV operators. There are at most $Q_{t}=1.5 p(p-1)-2 n_{t}+k_{t}+k_{t}^{\prime}$ possible operators for $e_{t}$. Among all conditions in Algorithm 1.1, the most time-consuming one, which takes time $O\left(p+n_{t}\right)$ [6], is to look for a path via the depth-first search for an operator with type of InsertD. We have that the time complexity of constructing $\mathcal{O}_{e_{t}}$ in Algorithm 1.1 is $O\left(Q_{t}\left(p+n_{t}\right)\right)$ in the worst case and the time complexity of Algorithm 1 is $O\left(\sum_{t=1}^{N} Q_{t}\left(p+n_{t}\right)\right)$ in the worst case, where $N$ is the length of Markov chain in Algorithm 1. We know that $k_{t}$ and $k_{t}^{\prime}$ reach the maxima $(p-2) / 2 * \operatorname{floor}(p / 2) * \operatorname{ceil}(p / 2)$ when $e_{t}$ is a evenly divided complete bipartite graphs [15]. Consequently, the time complexity of Algorithm 1 are $O\left(N p^{4}\right)$ in the worst case. Fortunately, when $n$ is a few times of $p$, say $n=2 p$, all completed PDAGs in $\mathcal{S}_{p}^{n}$ are sparse and our experiments show $k_{t}$ and $k_{t}^{\prime}$ are much less than $O\left(p^{2}\right)$ for most completed PDAGs in Markov chain $\left\{e_{t}\right\}_{t=1, \ldots, N}$. Hence the time complexity of Algorithm 1 is approximate $O\left(N p^{3}\right)$ on average when $n$ is a few times of $p$.

We can implement Algorithm 1 efficiently when $p$ is not large (less or around 100 in our experiments). However, when $p$ is larger, we need large $N$ to guarantee the estimates reach convergence. Experiments in Section 4 show $N=10^{6}$ is suitable. In this case, cubic complexity $\left(O\left(N p^{3}\right)\right)$ of Algorithm 1 is unacceptable. We need to speed up the algorithms for a very large $p$.

Notice that in Algorithm 1, we obtain an irreducible and reversible Markov chain $\left\{e_{t}\right\}$ and a sequence of numbers $\left\{M_{t}\right\}$ by checking all possible operators on each $e_{t}$. The sequence $\left\{M_{t}\right\}$ are used to compute the stationary probabilities of $\left\{e_{t}\right\}$ according to Proposition 1. We now introduce an accelerated version of Algorithm 1 to generate irreducible and reversible Markov chains on $\mathcal{S}_{p}^{n}$. The basic idea is that we do not check all possible operators but check some random samples. These random samples are then used to estimate $\left\{M_{t}\right\}$.

We first explain some notation used in the accelerated version. For each completed PDAG $e_{t}$, if $n_{e_{t}}<n, \mathcal{O}_{e_{t}}^{(\text {all })}$ is the set of all possible operators on $e_{t}$ with types of InsertU, DeleteU, InsertD, DeleteD, MakeV and RemoveV. If

```
Algorithm 2: An accelerated version of Algorithm 1.
    Input:
    \(\alpha \in(0,1]:\) an acceleration parameter; \(p, n\) and \(N\), the same as input in
    Algorithm 1
    Output:
    \(\left\{e_{t}, \hat{M}_{t}\right\}_{t=1, \ldots, N}\), where \(\hat{M}_{t}\) is an estimation of \(M_{t}=\left|\mathcal{O}_{e_{t}}\right|\)
    Initialize \(e_{0}\) as any completed PDAG in \(\mathcal{S}_{p}^{n}\)
    for \(t \leftarrow 0\) to \(N\) do
        Step A':
        if \(n_{e_{t}}<n\) then
            \(\operatorname{Set} \mathcal{O}_{e_{t}}^{\prime}=\mathcal{O}_{e_{t}}^{(\text {all })}\)
            else
            \(\operatorname{Set} \mathcal{O}_{e_{t}}^{\prime}=\mathcal{O}_{e_{t}}^{(\text {-insert })}\)
            Set \(m_{t}=\left|\mathcal{O}_{e_{t}}^{\prime}\right|\)
            Randomly sample \(\left[\alpha m_{t}\right]\) operators without replacement from \(\mathcal{O}_{e_{t}}^{\prime}\) to
            generate a set \(\mathcal{O}_{e_{t}}^{(\text {check })}\), where \(\left[\alpha m_{t}\right]\) is the integer closest to \(\alpha m_{t}\).
            Check all operators in \(\mathcal{O}_{e_{t}}^{(\text {check })}\), and choose perfect operators from it
            to construct a set of operators \(\tilde{\mathcal{O}}_{e_{t}}\).
            Set \(m_{i}^{\left(\mathcal{O}\right)}=\left|\tilde{\mathcal{O}}_{e_{t}}\right|\). If \(m_{i}^{\left(\mathcal{O}\right)}=0\), go to line 9.
    end
    Step B':
        Let \(\hat{M}_{t}=m_{t} \frac{\alpha\left|\mathcal{O}\right|}{[\alpha m_{t}]}\)
    end
    Step \(\mathbf{C}^{\prime}\) :
        Randomly choose an operator \(o\) uniformly from \(\tilde{\mathcal{O}}_{e_{t}}\).
    end
    Step D:
        Apply operator \(o\) to \(e_{t}\). Set \(e_{t+1}\) as the resulting completed PDAG of
        \(o\).
    end
    return \(\left\{e_{t}, \hat{M}_{t}\right\}_{t=1, \ldots, N}\).
```

$n_{e_{t}}=n$, the number of edges in $e_{t}$ reaches the upper bound $n$, no more edges can be inserted into $e_{t}$. Let $\mathcal{O}_{e_{t}}^{(-i n s e r t)}$ be the set of operators obtained by removing operators with types of InsertU and InsertD from $\mathcal{O}_{e_{t}}^{(\text {all })} \cdot \mathcal{O}_{e_{t}}^{(-i n s e r t)}$ is the set of all possible operators on $e_{t}$ when $n_{e_{t}}=n$. We can obtain $\mathcal{O}_{e_{t}}^{(\text {all })}$ and $\mathcal{O}_{e_{t}}^{(-i n s e r t)}$ easily via all possible modified edges introduced in Algorithm 1.1. The accelerated version of Algorithm 1 is shown in Algorithm 2.

In Algorithm 2, $\mathcal{O}_{e_{t}}^{\prime}$ (either $\mathcal{O}_{e_{t}}^{(\text {all })}$ or $\mathcal{O}_{e_{t}}^{(\text {-insert })}$ ) is the set of all possible operators on $e_{t}, \alpha \in(0,1]$ is an acceleration parameter that determines how many operators in $\mathcal{O}_{e_{t}}^{\prime}$ are checked, $\mathcal{O}_{e_{t}}^{(\text {check })}$ is a set of checked operators that are randomly sampled without replacement from $\mathcal{O}_{e_{t}}^{\prime}$ and $\tilde{\mathcal{O}}_{e_{t}}$ is the set of all perfect operators in $\mathcal{O}_{e_{t}}^{(\text {check })}$. When $\alpha=1, \tilde{\mathcal{O}}_{e_{t}}=\mathcal{O}_{e_{t}}$ and Algorithm 2 becomes back to Algorithm 1.

In Algorithm 2, because the operators in $\tilde{\mathcal{O}}_{e_{t}}$ are i.i.d. sampled from $\mathcal{O}_{e_{t}}$ in Step $\mathrm{A}^{\prime}$ and operator $o$ is chosen uniformly from $\tilde{\mathcal{O}}_{e_{t}}$ in Step $\mathrm{C}^{\prime}$, clearly, $o$ is also chosen uniformly from $\mathcal{O}_{e_{t}}$. We have that the following Corollary 1 holds according to Proposition 1.

Corollary 1 (Stationary distribution of $\left\{e_{t}\right\}$ on $\mathcal{S}_{p}^{n}$ ). Let $\mathcal{S}_{p}^{n}$, defined in equation (3.1), be the set of completed PDAGs with $p$ vertices and maximum $n$ of edges, $\mathcal{O}_{e_{t}}$, defined in equation (3.2), be the set of operators on $e_{t}$, and $M_{t}$ be the number of operators in $\mathcal{O}_{e_{t}}$. For the Markov chain $\left\{e_{t}\right\}$ on $\mathcal{S}_{p}^{n}$ obtained via Algorithms 1 or 2, then:
(1) the Markov chain $\left\{e_{t}\right\}$ is irreducible and reversible;
(2) the Markov chain $\left\{e_{t}\right\}$ has a unique stationary distribution $\pi$ and $\pi\left(e_{t}\right) \propto M_{t}$.

In Algorithm 2, we provide an estimate of $M_{t}$ instead of calculating it exactly in Algorithm 1. Let $\left|\mathcal{O}_{e_{t}}^{\prime}\right|=m_{t},\left|\mathcal{O}_{e_{t}}^{(\text {check })}\right|=\left[\alpha m_{t}\right]$ and $\left|\tilde{\mathcal{O}}_{e_{t}}\right|=m_{i}^{(\mathcal{S})}$. Clearly, the ratio $m_{i}^{(\mathcal{S})} /\left[\alpha m_{t}\right]$ is an unbiased estimator of the population proportion $M_{t} / m_{t}$ via sampling without replacement. We can estimate $M_{t}=$ $\left|\mathcal{O}_{e_{t}}\right|$ in Step $\mathrm{B}^{\prime}$ as

$$
\hat{M}_{t}=m_{t} \frac{m_{i}^{(\mathcal{S})}}{\left[\alpha m_{t}\right]}
$$

We have that when $\left[\alpha m_{t}\right]$ is large, the estimator $\hat{M}_{t}$ has an approximate normal distribution with mean equal to $M_{t}=\left|\mathcal{O}_{e_{t}}\right|$.

Let the random variable $u$ be uniformly distributed on $\mathcal{S}_{p}^{n}, f(u)$ be a real function describing a property of interest of $u$ and $A$ be a subset of $\mathbb{R}$. By replacing $M_{t}$ with $\hat{M}_{t}$ in equation (2.6), we estimate $\mathbb{P}_{N}(\{f(u) \in A\})$ via $\left\{e_{t}, \hat{M}_{t}\right\}_{t=1, \ldots, N}$ as follows:

$$
\hat{\mathbb{P}}_{N}^{\prime}(f(u) \in A)=\frac{\sum_{t=1}^{N} I_{\left\{f\left(e_{t}\right) \in A\right\}} \hat{M}_{t}^{-1}}{\sum_{t=1}^{N} \hat{M}_{t}^{-1}}
$$

where $\mathbb{P}_{N}(f(u) \in A)$ is defined in equation (2.5).
In the accelerated version, only $100 \alpha \%$ of all possible operators on $e_{t}$ are checked. In Section 4, our experiments on $\mathcal{S}_{100}^{150}$ show that the accelerated

version can speed up the approach nearly $\frac{1}{\alpha}$ times, and that equation (3.5) provides almost the same results as equation (2.6) in which $\left\{e_{t}, M_{t}\right\}_{t=1, \ldots, N}$ from Algorithm 1 are used. Roughly speaking, if we set $\alpha=1 / p$, the time complexity of our accelerated version can reduce to $O\left(N p^{2}\right)$.
4. Experiments. In this section, we conduct experiments to illustrate the reversible Markov chains proposed in this paper and their applications for studying Markov equivalence classes. The main points obtained from these experiments are as follows:
(1) For $\mathcal{S}_{p}$ with small $p$, the estimations of our proposed are very close to true values. For $\mathcal{S}_{p}^{n}$ with large $p$ (up to 1000), the accelerated version of our proposed approach is also very efficient, and the estimations in equations (2.6) and (3.5) converge quickly as the length of Markov chain increases.
(2) For completed PDAGs in $\mathcal{S}_{p}^{n}$ with sparsity constraints ( $n$ is a small multiple of $p$ ), we see that (i) most edges are directed, (ii) the sizes of maximum chain components (measured by the number of vertices) are very small (around ten) even for large $p$ (around 1000) and (iii) the number of chain components grows approximately linearly with $p$.

As we know, under the assumption that there are no latent or selection variables present, causal inference based on observational data will give a completed PDAG. Interventions are needed to infer the directions of the undirected edges in the completed PDAG. Our results show that if the underlying completed PDAG is sparse, in the model space of Markov equivalence classes, most graphs have few undirected edges and small chain components. They give hope for learning causal relationships via observational data and for inferring the directions of the undirected edges via interventions.

In Section 4.1, we evaluate our methods by comparing the size distributions of Markov equivalence classes in $\mathcal{S}_{p}$ with small $p$ to true distributions $(p=3,4)$ or Gillispie's results $(p=6)$ [15]. In Section 4.2, we report the proportion of directed edges and the properties of chain components of Markov equivalence classes under sparsity constraints. In Section 4.3, we show experimentally that Algorithm 2 is much faster than Algorithm 1, and that the difference in the estimates obtained is small. Finally, we study the asymptotic properties of our proposed estimators in Section 4.4.
4.1. Size distributions of Markov equivalence classes in $\mathcal{S}_{p}$ for small $p$. We consider size distributions of completed PDAGs in $\mathcal{S}_{p}$ for $p=3,4$ and 6 , respectively. There are 11 Markov equivalence classes in $\mathcal{S}_{3}$, and 185 Markov equivalence classes in $\mathcal{S}_{4}$. Here we can get the true size distributions for $\mathcal{S}_{3}$ and $\mathcal{S}_{4}$ by listing all the Markov equivalence classes and calculating the size of each explicitly. Gillespie and Perlman calculate the true size probabilities for $\mathcal{S}_{6}$ by listing all classes; these are denoted as GP-values. We estimate the size probabilities via equation (2.6) with the Markov chains from Al-

Table 1
Size distributions for $\mathcal{S}_{p}$ with $p=3,4$ and 6 , respectively. $N$ is the sample size, $T$ is the time (seconds) used to estimate the size distributions with a Markov chain, GP-values are obtained by Gillispie and Perlman [15]


gorithm 1. We ran ten independent Markov chains using Algorithm 1 to calculate the mean and standard deviation of each estimate. The results are shown in Table 1, where $N$ is the sample size (length of Markov chain). We can see that the means are very close to true values or GP-values, and the standard deviations are also very small.

We implemented our proposed method (Algorithm 1, the version without acceleration) in Python, and ran it on a computer with a 2.6 GHZ processor. In Table 1, $T$ is the time used to estimate the size distribution for $\mathcal{S}_{3}$, $\mathcal{S}_{4}$ or $\mathcal{S}_{6}$. These results were obtained within at most tens of seconds. In comparison, a MCMC method in [30] took more than one hour (in C++ on a 2.6 GHZ computer) in order to get similar estimates of the proportions of Markov equivalence classes of size one. It is worth noting that our estimates are based on a single Markov chain, while the results in [30] are based on $10^{4}$ independent Markov chains with $10^{6}$ steps.

![img-1.jpeg](img-1.jpeg)

Fig. 2. Distribution of proportion of directed edges in completed PDAGs in $\mathcal{S}_{p}^{r p}$. The lines in the boxes and the solid circles under the boxes indicate the medians and the $5 \%$ quartiles, respectively.
4.2. Markov equivalence classes with sparsity constraints. We now study the sets $\mathcal{S}_{p}^{n}$ of Markov equivalence classes defined in equation (3.1). The number of vertices $p$ is set to $100,200,500$ or 1000 , and the maximum edge constraint $n$ is set to $r p$ where $r$ is the ratio of $n$ to $p$. For each $p$, we consider three ratios: $1.2,1.5$ and 3 . The completed PDAGs in $\mathcal{S}_{p}^{r p}$ are sparse since $r \leq 3$. Define the size of a chain component as the number of vertices it contains. In this section, we report four distributions for completed PDAGs in $\mathcal{S}_{p}^{r p}$ : the distribution of proportions of directed edges, the distribution of the numbers of chain components and the distribution of the maximum size of chain components. The results about the distribution of the numbers of $v$-structures are reported in the Supplementary Material [16]. In each simulation, given $p$ and $r$, a Markov chain with length of $10^{6}$ on $\mathcal{S}_{p}^{r p}$ is generated via Algorithm 2 to estimate the distributions via equation (3.5). The acceleration parameter $\alpha$ is set to $0.1,0.05,0.01$ and 0.001 for $p=100,200,500$ and 1000 , respectively.

In Figure 2, twelve distributions of proportions of directed edges are reported for $\mathcal{S}_{p}^{r p}$ with different $p$ and ratio $r$. We mark the minimums, $5 \%$ quartiles (solid circles below boxes), 1st quartiles, medians, 3rd quartiles and maximums of these distributions. We can see that for a fixed $p$, the proportion of directed edges increases with the number of edges in the completed PDAG. For example, when the ratio $r=1.2$, the medians (red lines in boxes) of proportions are near $92 \%$; when the ratio $r=1.5$, the medians are near $95 \%$; when ratio $r=3$, the medians are near $98 \%$.

![img-2.jpeg](img-2.jpeg)

Fig. 3. Distributions of numbers of chain components of completed PDAGs in $\mathcal{S}_{p}^{r p}$. The lines in the boxes and the solid circles above the boxes indicate the medians and the $95 \%$ quartiles, respectively.

The distributions of the numbers of chain components of completed PDAGs in $\mathcal{S}_{p}^{r p}$ are shown in Figure 3. We plot the distributions for $\mathcal{S}_{p}^{1.5 p}$ in the main window and the distributions for $r=1.2$ and $r=3$ in two sub-windows. We can see that the medians of the numbers of chain components are close to $5,10,20$, and 40 for completed PDAGs in $\mathcal{S}_{p}^{1.5 p}$ with $p=100,200,500$ and 1000 , respectively. It seems that there is a linear relationship between the number of chain components and the number of vertices $p$. In the insets, similar results are shown in the distributions for $r=1.2$ and $r=3$.

The distributions of the maximum sizes of chain components of completed PDAGs in $\mathcal{S}_{p}^{r p}$ are shown in Figure 4. For $\mathcal{S}_{p}^{1.5 p}$ in the main window, the medians of the four distributions are approximately $4,5,6$ and 7 for $p=$ $100,200,500$ and 1000, respectively. This shows that the maximum size of chain components in a competed PDAG increases very slowly with $p$. In particular, from the $95 \%$ quartiles (solid circles above boxes), we can see that the maximum chain components of more than $95 \%$ completed PDAGs in $\mathcal{S}_{p}^{1.5 p}$ have at most $8,9,10$ and 13 vertices for $p=100,200,500$ and 1000 , respectively. This result implies that sizes of chain components in most sparse completed PDAGs are small.
4.3. Comparisons between Algorithm 1 and its accelerated version. In this section, we show experimentally that the accelerated version Algorithm 2 is much faster than Algorithm 1, and the difference of estimates based on two algorithms is small. We have estimated four distributions on $\mathcal{S}_{100}^{150}$ in Section 4.2 via Algorithm 2. The four distributions are the distribu-

![img-3.jpeg](img-3.jpeg)

Fig. 4. The distributions of the maximum sizes of chain components of completed PDAGs in $\mathcal{S}_{p}^{r p}$. The lines in the boxes and the solid circles above the boxes indicate the medians and the $95 \%$ quartiles, respectively.
tion of proportions of directed edges, the distribution of the numbers of chain components, the distribution of maximum size of chain components and the distribution of the numbers of $v$-structures. To compare Algorithm 1 with Algorithm 2, we re-estimate these four distributions for completed PDAGs in $\mathcal{S}_{100}^{150}$ via Algorithm 1.

For each distribution, in Figure 5, we report the estimates obtained by Algorithm 1 with lines and the estimates obtained by Algorithm 2 with points in the main windows. The differences of two estimates are shown in the sub-windows. The top panel of Figure 5 displays the cumulative distributions of proportions of directed edges. The second panel of this figure displays the distributions of the numbers of chain components. The third panel displays the distributions of maximum size of chain components. The bottom panel displays the distribution of the numbers of $v$-structures. We can see that the differences of three pairs of estimates are small.

The average times used to generate a state of the Markov chain of completed PDAGs in $\mathcal{S}_{p}^{1.5 p}$ are shown in Table 2, in which $\alpha$ is the acceleration parameter used in Algorithm 2. If $\alpha=1$, the Markov chain is generated via Algorithm 1. The results suggest that the accelerated version can speed up the approach nearly $\frac{1}{\alpha}$ times when $p=100$.
4.4. Asymptotic properties of proposed estimators. We further illustrate the asymptotic properties of proposed estimators of sparse completed PDAGs via simulation studies. We consider $\mathcal{S}_{p}^{1.5 p}$ for $p=100,200,500$ and 1000, respectively. Let $f(u)$ be a discrete function of Markov equivalence class $u$,

![img-4.jpeg](img-4.jpeg)

Fig. 5. Distributions for completed PDAGs in $\mathcal{S}_{100}^{150}$ estimated via Algorithm 1 (plotted in lines) and the accelerated version-Algorithm 2 (plotted in points) are shown in the main windows. The differences are shown in sub-windows. Four panels (from top to bottom) display distributions of directed edges, number of chain components, maximum size of chain components and v-structures, respectively.
where $u$ is a random variable distributed uniformly in $\mathcal{S}_{p}^{1.5 p}$. Let $\mathbb{E}(f)$ be the expectation of $f(u)$, and we have

$$
\mathbb{E}(f)=\sum_{i} i \mathbb{P}(f=i)
$$

Proposition 2 shows that the estimator $\hat{\mathbb{P}}(f=i)$ in equation (2.6) converges to $\mathbb{P}(f=i)$ with probability one. We also have that the estimator defined as

$$
\hat{\mathbb{E}}(f)=\sum_{i} i \hat{\mathbb{P}}(f=i)=\frac{\sum_{i} \sum_{t=1}^{N} i I_{\left\{f\left(e_{t}\right)=i\right\}} M_{t}^{-1}}{\sum_{t=1}^{N} M_{t}^{-1}}=\frac{\sum_{t=1}^{N} f\left(e_{t}\right) M_{t}^{-1}}{\sum_{t=1}^{N} M_{t}^{-1}}
$$

converges to $\mathbb{E}(f)$ with probability one, where $\left\{e_{t}, M_{t}\right\}_{t=1, \ldots, N}$ is a Markov chain from Algorithm 1.

TABLE 2
The average time used to generate a completed $P D A G$ in $\mathcal{S}_{p}^{1.5 p}$, where $p$ is the number of vertices, $\alpha$ is the acceleration parameter, $\kappa$ is the average time (seconds)


![img-5.jpeg](img-5.jpeg)

Fig. 6. Four sequences of average proportions of directed edges in completed PDAGs in $\mathcal{S}_{p}^{1.5 p}$ with $p=100,200,500$ and 1000, estimated via Algorithm 2 and the first $5000 k$ steps of the Markov chains, where $k$ is shown in x-axis.

We generate some sequences of Markov equivalence classes $\left\{e_{t}, \hat{M}_{t}\right\}$ with length of $N=1.25 \times 10^{6}$ via Algorithm 2 and divide each sequence into 250 blocks. Set $f(u)$ to be the proportion of directed edges in $u$, we estimate $\mathbb{E}(f)$ using cumulative data in the first $k$ blocks as

$$
\hat{\mathbb{E}}(f)_{k}=\left(\sum_{t=1}^{k \times j} f\left(e_{t}\right) \hat{M}_{t}^{-1}\right) / \sum_{t=1}^{k \times j} \hat{M}_{t}^{-1}
$$

where $j=5 \times 10^{3}$. The simulation results are shown in Figure 6. We can see that the estimates of proportions of directed edges converge quickly as $k$ increases.
5. Conclusions and discussions. In this paper, we proposed a reversible irreducible Markov chain on Markov equivalence classes that can be used to study various properties of a given set of interesting Markov equivalence classes. Our experiments on Markov equivalence classes with sparse constraints reveal useful information. For example, we find that proportions of undirected edges and chain components in sparse completed PDAGs are small even for Markov equivalence classes with thousands of vertices.

When some "important" but very rare equivalence classes are of interest, it will be very hard to sample them in the proposed Markov chain. In this case, we can constrain the space appropriately so that these Markov equivalence classes are easy to be sampled. For example, it is nearly impossible

to sample equivalence classes with 300 vertices and 1 edge from $\mathcal{S}_{300}$. Fortunately, if we set the space to be $\mathcal{S}_{300}^{2}$, sampling graphs with 1 edge is not difficult.

The sizes of Markov equivalence classes are the property most widely discussed in the literature. Due to space constraints, we have omitted several details in this paper about determining the size of Markov equivalence classes and calculating further properties of edges and vertices. We will discuss these issues in a follow-up paper. The proposed methods can potentially be extended to study other sets of completed PDAGs besides $\mathcal{S}_{n}^{p}$. Some interesting sets include (1) the completed PDAGs in which each vertex has at most $d$ adjacent edges; (2) completed PDAGs in which each pair of vertices is connected by a path along edges in the graph.

# APPENDIX: PRELIMINARY RESULTS AND PROOF OF THEOREM 1 

In this Appendix, we provide two preliminary results introduced by Andersson [2] and Chickering [5, 6], respectively, in Appendix A.1. These results are necessary to implement our proposed approach technically and will be used in the proof of Theorem 1. Then we provide a proof of the main result of this paper (Theorem 1) in Appendix A.2.
A.1. Two preliminary results. Some definitions and notation are introduced first. A graph is called a chain graph if it contains no partially directed cycles [22]. A chord of a cycle is an edge that joins two nonadjacent vertices in the cycle. An undirected graph is chordal if every cycle of length greater than or equal to 4 possesses a chord. A directed edge of a DAG is compelled if it occurs in the corresponding completed PDAG, otherwise, the directed edge is reversible, and the corresponding parents are reversible parents. Recall $N_{x}$ be the set of all neighbors of $x, \Pi_{x}$ is the set of all parent of $x$, $N_{x y}=N_{x} \cap N_{y}$ and $\Omega_{x, y}=\Pi_{x} \cap N_{y}$ and the concept of "strongly protected" is presented in Definition 2.

Lemma 2 characterizes completed PDAGs that are used to represent Markov equivalence classes [2] and will be used in the proofs in Appendix A.2.

Lemma 2 (Andersson [2]). A graph $\mathcal{C}$ is a completed PDAG of a directed acyclic graph $\mathcal{D}$ if and only if $\mathcal{C}$ satisfies the following properties:
(i) $\mathcal{C}$ is a chain graph;
(ii) let $\mathcal{C}_{\tau}$ be the subgraph induced by $\tau . \mathcal{C}_{\tau}$ is chordal for every chain component $\tau$;
(iii) $w \rightarrow u-v$ does not occur as an induced subgraph of $\mathcal{C}$;
(iv) every arrow $v \rightarrow u$ in $\mathcal{C}$ is strongly protected.

Lemma 3 shows the equivalent validity conditions for $\mathbf{i u}_{2}, \mathbf{d u}_{1}, \mathbf{i d}_{2}, \mathbf{d d}_{1}$ and $\mathbf{m v}_{1}$ used in Definition 9.

Lemma 3 (Validity conditions of some operators [6]). The necessary and sufficient validity conditions of the operators with type of InsertU, DeleteU, InsertD, DeleteD or MakeV are as follows:

- (InsertU) Let $x$ and $y$ be two vertices that are not adjacent in $\mathcal{C}$. The operator Insert $U x-y$ is valid (equivalently, $\mathbf{i u}_{2}$ holds) if and only if $\left(\mathrm{iu}_{2.1}\right)$ $\Pi_{x}=\Pi_{y},\left(\mathrm{iu}_{2.2}\right)$ every undirected path from $x$ to $y$ contains a vertex in $N_{x y}$.
- (DeleteU) Let $x-y$ be an undirected edge in completed PDAG $\mathcal{C}$. The operator Delete $U x-y$ is valid (equivalently, $\mathbf{d u}_{1}$ holds) if and only if $\left(\mathrm{du}_{1.1}\right) N_{x y}$ is a clique in $\mathcal{C}$.
- (InsertD) Let $x$ and $y$ be two vertices that are not adjacent in $\mathcal{C}$. The operator InsertD $x \rightarrow y$ is valid (equivalently, $\mathbf{i d}_{2}$ holds) if and only if $\left(\mathrm{id}_{2.1}\right) \Pi_{x} \neq \Pi_{y},\left(\mathrm{id}_{2.2}\right) \Omega_{x, y}$ is a clique, $\left(\mathrm{id}_{2.3}\right)$ every partially directed path from $y$ to $x$ contains at least one vertex in $\Omega_{x, y}$.
- (DeleteD) Let $x \rightarrow y$ be a directed edge in completed PDAG $\mathcal{C}$. The operator DeleteD of $x \rightarrow y$ is valid (equivalently, $\mathbf{d d}_{1}$ holds) if and only if $\left(\mathrm{dd}_{1.1}\right) N_{y}$ is a clique.
- (MakeV) Let $x-z-y$ be any length-two undirected path in $\mathcal{C}$ such that $x$ and $y$ are not adjacent. The operator Make $V x \rightarrow z \leftarrow y$ is valid (equivalently, $\mathbf{m v}_{1}$ holds) if and only if $\left(\mathrm{mv}_{1.1}\right)$ every undirected path between $x$ and $y$ contains a vertex in $N_{x y}$.
A.2. Proof of Theorem 1. Let $\mathcal{O}$ be the operator set defined in equation (3.3); to prove Theorem 1, which shows $\mathcal{O}$ is a perfect operator set, we need to show $\mathcal{O}$ satisfies four properties: validity, distinguishability, irreducibility and reversibility. Equivalently, we just need to prove Theorem 2-5 as follows:

THEOREM 2. The operator set $\mathcal{O}$ is valid.
THEOREM 3. The operator set $\mathcal{O}$ is distinguishable.
THEOREM 4. The operator set $\mathcal{O}$ is reversible.
THEOREM 5. The operator set $\mathcal{O}$ is irreducible.
Of the above four theorems, the most important and difficult is to prove Theorem 4. We now show the proofs one by one.

Proof of Theorem 2. According to the definition of validity in Definition 5 and the definition of $\mathcal{O}_{\mathcal{C}}$ in equation (3.2), all operators in Insert $U_{\mathcal{C}}$, Delete $U_{\mathcal{C}}$, Insert $D_{\mathcal{C}}$, Delete $D_{\mathcal{C}}$ and Make $V_{\mathcal{C}}$ are valid. We just need to prove Lemma 4, which shows all operators in Remove $V_{\mathcal{C}}$ are valid.

Lemma 4. Let $x \rightarrow z \leftarrow y$ be a $v$-structure in completed PDAG $\mathcal{C}$. If $\left(\mathbf{r v}_{1}\right) \Pi_{x}=\Pi_{y},\left(\mathbf{r v}_{2}\right) \Pi_{x} \cup N_{x y}=\Pi_{z} \backslash\{x, y\}$, and $\left(\mathbf{r v}_{3}\right)$ every undirected path between $x$ and $y$ contains a vertex in $N_{x y}$ hold, then the operator $\mathrm{Re}-$ move $V x \rightarrow z \leftarrow y$ is valid and results in a completed $P D A G$ in $\mathcal{S}_{p}^{n}$ defined in equation (3.1).

To prove Lemma 4, we will use Lemma 5 given by Chickering (Lemma 32 in $[6]$ ).

Lemma 5. Let $\mathcal{C}$ be any completed $P D A G$, and let $x$ and $y$ be any pair of vertices that are not adjacent. Every undirected path between $x$ and $y$ passes through a vertex in $N_{x y}$ if and only if there exists a consistent extension in which (1) $x$ has no reversible parents, (2) all vertices in $N_{x y}$ are parents of $y$ and (3) $y$ has no other reversible parents.

We now give a proof of Lemma 4.
Proof of Lemma 4. From Lemma 5 and condition $\mathbf{r v}_{3}$ in Lemma 4, there exists a consistent extension of $\mathcal{C}$, denoted by $\mathcal{D}$, in which $x$ has no reversible parents, and the reversible parents of $y$ are the vertices in $N_{x y}$. Because $y \rightarrow z$ occurs in the completed PDAG, $\mathcal{C}, N_{z}$ and $N_{y}$ occur in different chain components. We can orient the undirected edges adjacent to $z$ out of $z$. Then all vertices in $N_{z}$ are children of $z$ in $\mathcal{D}$. Let $\mathcal{D}^{\prime}$ be the graph obtained by reversing $y \rightarrow z$ in $\mathcal{D}$ and $\mathcal{P}^{\prime}$ be the PDAG obtained by applying the RemoveV operator to $\mathcal{C}$. We will show that $\mathcal{D}^{\prime}$ is a consistent extension of $\mathcal{P}^{\prime}$.

Clearly, $\mathcal{D}^{\prime}$ and $\mathcal{P}^{\prime}$ have the same skeleton.
We have that any $v$-structure that occurs in $\mathcal{D}$ but not in $\mathcal{P}^{\prime}$ must include either the edge $x \rightarrow z$ or $y \rightarrow z$. Since $\mathcal{D}$ is a consistent extension of $\mathcal{C}$, we have that all $v$-structures in $\mathcal{D}$ are also in $\mathcal{C}$. From condition $\mathbf{r v}_{2}$, all parents of z other than $x$ and $y$ are adjacent to $x$ and $y$. Hence $x \rightarrow z \leftarrow y$ is the only $v$-structure that is directed into $z$ in $\mathcal{C}$. We have that all $v$-structures of $\mathcal{P}^{\prime}$ are also in $\mathcal{D}$, and there is only one $v$-structure $x \rightarrow z \leftarrow y$ that is in $\mathcal{D}$ but not $\mathcal{P}^{\prime}$.

Since $y \rightarrow z$ is the unique edge that differs between $\mathcal{D}$ and $\mathcal{D}^{\prime}$, we have that any $v$-structure that exists in $\mathcal{D}$ but not in $\mathcal{D}^{\prime}$ must include the edge $y \rightarrow z$, and any $v$-structure that exists in $\mathcal{D}^{\prime}$ but not in $\mathcal{D}$ must include the edge $z \rightarrow y$. We have shown that $x \rightarrow z \leftarrow y$ is the only $v$-structure in $\mathcal{D}$ that is directed into $z$. From the construction of $\mathcal{D}$, we have that all compelled parents of $y$ in $\mathcal{D}^{\prime}$ are also parents of $z$, and all other parents are in $N_{x y}$; from $\mathbf{r v}_{2}$, they also are parents of $z$. There is no $v$-structure that includes edge $z \rightarrow y$ in $\mathcal{D}^{\prime}$. Hence, all $v$-structures of $\mathcal{D}^{\prime}$ are also in $\mathcal{D}$, and there is only one $v$-structure $x \rightarrow z \leftarrow y$ that is in $\mathcal{D}$ but not $\mathcal{D}^{\prime}$.

Hence, $\mathcal{D}^{\prime}$ and $\mathcal{P}^{\prime}$ have the same $v$-structures. It remains to be shown that $\mathcal{D}^{\prime}$ is acyclic.

If $\mathcal{D}^{\prime}$ contains a cycle, the cycle must contain the edges $z \rightarrow y$ because $\mathcal{D}$ is acyclic. This implies there is a directed path from $y$ to $z$ in $\mathcal{D}$. By construction, all vertices in $N_{z}$ are children of $z$ in $\mathcal{D}^{\prime}$. So, this path must include a compelled parent of $z$; denote it by $u$. If $u \neq x$, from condition $\mathbf{r v}_{2}$, $u \in \Pi_{y} \cup N_{x y}$; by the construction of $\mathcal{D}$, we have $u \in \Pi_{y}$. Thus, there is no path from $y$ to $z$ that contains $u$. If $u=x$, by construction, the path must contain a compelled parent $v$ of $x$. From condition $\mathbf{r v}_{1}, v \in \Pi_{y}$. Thus, there is no path from $y$ to $z$ contains $v$. We get that $\mathcal{D}^{\prime}$ is acyclic. Thus $\mathcal{D}^{\prime}$ is a consistent extension of $\mathcal{P}^{\prime}$ and the operator RemoveV $x \rightarrow z \leftarrow y$ is valid.

Proof of Theorem 3. For any completed $\mathcal{C} \in \mathcal{S}_{p}^{n}$, we need to show that different operators in $O_{\mathcal{C}}$ result in different completed PDAGs. For any valid operator $o \in \operatorname{Insert} U_{\mathcal{C}}$, say InsertU $x-y$, denoted as $o$, the resulting completed PDAG of $o$ contains the undirected edge $x-y$. We have that all other operators in $O_{\mathcal{C}}$ except for InsertD $x \rightarrow y$ and Insert $x \leftarrow y$ (if they are also valid) will result in completed PDAGs with skeletons different than the resulting completed PDAG of $o$. Thus, these operators cannot result in the same completed PDAG as $o$. If InsertD $x \rightarrow y$ or Insert $x \leftarrow y$ is valid, the resulting completed PDAGs of them contain $x \rightarrow y$ or $x \leftarrow y$. These two resulting completed PDAGs have at least a compelled edge different than the resulting completed PDAG of $o$. Thus there is no operator in $O_{\mathcal{C}}$ that can result in the same completed PDAG as $o$.

Similarly, we can show for any operator in $\mathcal{O}_{\mathcal{C}}$, different operators will result in different completed PDAGs because they will have distinct skeletons, compelled edges or $v$-structures.

Proof of Theorem 4. Let $\mathcal{C}$ be any completed PDAG in $\mathcal{S}_{p}^{n}, o \in \mathcal{O}_{\mathcal{C}}$ be an operator on $\mathcal{C}$. The operator $o^{\prime} \in \mathcal{O}$ is the reversible operator of $o$ if $o^{\prime}$ can transfer the resulting completed PDAG of $o$ back to $\mathcal{C}$. To prove Theorem 4, we just need to show each operator in $\mathcal{O}_{\mathcal{C}}$ defined in equation (3.3) has a reversible operator in $\mathcal{O}$. Equivalently, we prove Lemmas $6,7,8,9,10$ and 11 to show the reversibility for six types of operators, respectively.

Lemma 6. For any operator $o \in \mathcal{O}_{\mathcal{C}}$ denoted by "InsertU $x-y$," the operator "DeleteU $x-y$ " is the reversible operator of $o$.

Lemma 7. For any operator $o \in \mathcal{O}_{\mathcal{C}}$ denoted by "DeleteU $x-y$," the operator "InsertU $x-y$ " is the reversible operator of o.

Lemma 8. For any operator $o \in \mathcal{O}_{\mathcal{C}}$ denoted by "InsertD $x \rightarrow y$," the operator "DeleteD $x \rightarrow y$ " is the reversible operator of o.

Lemma 9. For any operator $o \in \mathcal{O}_{\mathcal{C}}$ denoted by "DeleteD $x \rightarrow y$," the operator "InsertD $x \rightarrow y$ " is the reversible operator of o.

Lemma 10. For any operator $o \in \mathcal{O}_{\mathcal{C}}$ denoted by "Make $V x \rightarrow z \leftarrow y$," the operator "Remove $V x \rightarrow z \leftarrow y$ " is the reversible operator of o.

Lemma 11. For any operator $o \in \mathcal{O}_{\mathcal{C}}$ denoted by "Remove $V x \rightarrow z \leftarrow y$," the operator "Make $V x \rightarrow z \leftarrow y$ " is the reversible operator of o.

Before giving proofs of these six lemmas, We first provide several results shown in Lemmas 12, 13, 14 and 15.

Lemma 12. Let graph $\mathcal{C}$ be a completed $P D A G,\{w, v, u\}$ be three vertices that are adjacent each other in $\mathcal{C}$. If there are two undirected edges in $\{w, v, u\}$, then the third edge is also undirected.

Proof. If the third edge is directed, there is a directed cycle like $w-$ $v-u \rightarrow w$. From Lemma 2, we know that $\mathcal{C}$ is a chain graph, so there is no directed circle in $\mathcal{C}$.

Lemma 13. Let $\mathcal{C}_{1}$ be the resulting completed PDAG obtained by inserting a new edge between $x$ and $y$ in $\mathcal{C}$. If there is at least one edge $v \rightarrow u$ that is directed in $\mathcal{C}$ but not directed in $\mathcal{C}_{1}$, then there exists a vertex $h$ that is common child of $x$ and $y$ such that $x \rightarrow h$ and $y \rightarrow h$ in $\mathcal{C}$ become undirected in $\mathcal{C}_{1}$.

Proof. According to Lemma 2, an edge is directed in a completed PDAG if and only if it is strongly protected. Thus, we have that at least one case among (a), (b), (c), (d) in Figure 1 occurs in $\mathcal{C}$ but not in $\mathcal{C}_{1}$ for $v \rightarrow u$. We will show that either Lemma 13 holds, or there exists a parent of $u$, denoted as $u_{1}$, such that $u_{2} \rightarrow u_{1}$ occurs in $\mathcal{C}$ but not in $\mathcal{C}_{1}$, where $u_{2}$ is a parent of $u_{1}$. We denote the latter result as $\left({ }^{*}\right)$.

Suppose case (a) in Figure 1 occurs in $\mathcal{C}$ but not in $\mathcal{C}_{1}$. Because $v \rightarrow u$ becomes undirected in $\mathcal{C}_{1}$, we have that $w \rightarrow v$ must be undirected in $\mathcal{C}_{1}$ since $w$ and $u$ are not adjacent. Set $u_{1}=v$ and $u_{2}=u$, and we have that $\left(^{*}\right)$ holds.

Suppose case (b) in Figure 1 occurs in $\mathcal{C}$ but not in $\mathcal{C}_{1}$. If the pair $\{v, w\}$ is not $\{x, y\}, v \rightarrow u \leftarrow w$ is a $v$-structure in $\mathcal{C}$. We have that $v \rightarrow u$ occurs in $\mathcal{C}_{1}$. This is a contradiction. If $\{v, w\}$ is $\{x, y\}$, we have that Lemma 13 holds $(h=u)$.

Suppose case (c) in Figure 1 occurs in $\mathcal{C}$ but not in $\mathcal{C}_{1}$. Either $v \rightarrow w$ or $w \rightarrow u$ occurs in $\mathcal{C}$ but not in $\mathcal{C}_{1}$. If it is $v \rightarrow w$, by setting $u_{2}=v$ and $u_{1}=w$, we have $\left(^{*}\right)$ holds. If it is $w \rightarrow u$, both $v-u$ and $w-u$ in $\mathcal{C}_{1}$, so $x-u$ also must be in $\mathcal{C}_{1}$. We also have that $\left({ }^{*}\right)$ holds.

Suppose case (d) in Figure 1 occurs in $\mathcal{C}$ but not in $\mathcal{C}_{1}$. If the pair $\left\{w, w_{1}\right\}$ is $\{x, y\}$, Lemma 13 holds $(h=u)$. Otherwise, $w \rightarrow u \leftarrow w_{1}$ must occur in

both $\mathcal{C}_{1}$ and $\mathcal{C}$ and the edge $v \rightarrow u$ is still strongly protected in $\mathcal{C}_{1}$, yielding a contradiction.

If $\left({ }^{*}\right)$ holds, we have that there is a directed path $u_{2} \rightarrow u_{1} \rightarrow u$ such that $u_{2} \rightarrow u_{1}$ occurs in $\mathcal{C}$ but not $\mathcal{C}_{1}$. Iterating, we can get a directed path $u_{k} \rightarrow$ $u_{k-1} \cdots \rightarrow u$ of length $k-1$ without undirected edges such that $u_{k} \rightarrow u_{k-1}$ occurs in $\mathcal{C}$ but not in $\mathcal{C}_{1}$ if Lemma 13 does not hold in each step. Because $\mathcal{C}$ is a chain graph without directed circle, the procedure will stop in finite steps and Lemma 13 will hold eventually.

From the proof of Lemma 13, we have that $u$ should be a descendant of $x$ and $y$, so we can get the following Lemma 14.

Lemma 14. Let $\mathcal{C}$ be any completed $P D A G$, and let $\mathcal{P}$ denote the $P D A G$ that results from adding a new edge between $x$ and $y$. For any edge $v \rightarrow u$ in $\mathcal{C}$ that does not occur in the resulting completed $P D A G$ extended from $\mathcal{P}$, there is a directed path of length zero or more from both $x$ and $y$ to $u$ in $\mathcal{C}$.

Lemma 15. Let Insert $U_{\mathcal{C}}$ and Delete $U_{\mathcal{C}}$ be the operator sets defined in Definition 9, respectively. For any o in Insert $U_{\mathcal{C}}$ or in Delete $U_{\mathcal{C}}$, where $\mathcal{P}^{\prime}$ is the modified graph of o that is obtained by applying o to $\mathcal{C}$, we have that $\mathcal{P}^{\prime}$ is a completed $P D A G$.

Proof. We just need to check whether $\mathcal{P}^{\prime}$ satisfies the four conditions in Lemma 2.
(i): For any $o \in$ Delete $U_{\mathcal{C}}$, denoted as DeleteD $x-y$, let $\mathcal{P}^{\prime}$ be the modified graph obtained by deleting $x-y$ from $\mathcal{C}$.

If there is a directed cycle in $\mathcal{P}^{\prime}$, it must be a directed cycle in $\mathcal{C}$, which is a contradiction. Thus there is no directed cycle in $\mathcal{P}^{\prime}$, and $\mathcal{P}^{\prime}$ is a chain graph.

If there exists an undirected cycle of length greater than 3 without a chord in $\mathcal{P}^{\prime}$, the cycle must contain both $x$ and $y$; otherwise, this cycle occurs in $\mathcal{C}$. If the length of the cycle is 4 , the other two vertices are in $N_{x y}$; we have that the cycle has a chord since $N_{x y}$ is a clique in $\mathcal{C}$. If the cycle in $\mathcal{P}^{\prime}$ has length greater than 4 without a chord, we have that $x-y$ is the unique chord of this cycle in $\mathcal{C}$. However, this would imply that there is a cycle of length greater than 3 without a chord in $\mathcal{C}$, a contradiction. Thus, there is no undirected cycle with length greater than 3 in $\mathcal{P}^{\prime}$, so every chain component of $\mathcal{P}^{\prime}$ is chordal.

Suppose that $\cdot \rightarrow \cdot-$ - occurs as an induced subgraph of $\mathcal{P}^{\prime}$; it must be $x \rightarrow \cdot-y$ (or $y \rightarrow \cdot-x$ ). However, in this case, $x \rightarrow \cdot-y-x$ (or $y \rightarrow \cdot-x-y$ ) would be a directed cycle in $\mathcal{C}$. Thus the induced subgraph like $\cdot \rightarrow \cdot-$ - does not occur as an induced subgraph of $\mathcal{P}^{\prime}$.

Finally, all directed edges in $\mathcal{P}^{\prime}$ will be strongly protected; by the definition of strong protection, all directed edges in $\mathcal{C}$ will remain strongly protected when an undirected edge is removed.

(ii): For any $o \in \operatorname{Insert} U_{\mathcal{C}}$, denoted as InsertU $x-y, \mathcal{P}^{\prime}$ is the modified graph of $o$.

If there is a directed cycle in $\mathcal{P}^{\prime}$, it must contain $x-y$; otherwise this cycle is also in $\mathcal{C}$. We can suppose that there exists a partially directed path from $x$ to $y$ in $\mathcal{C}$. Denote the adjacent vertex of $y$ in the path as $u$. Let $u$ be the vertex adjacent to $y$ in the path. We have $u \notin \Pi_{y}$; otherwise, from the condition $\Pi_{x}=\Pi_{y}$ in Lemma $3, u$ would also be in $\Pi_{x}$, so there would be a partially directed cycle from $x$ to $x$ in $\mathcal{C}$. Hence the directed path must have the form $x \cdots \rightarrow \cdots u-y$. This would induce a subgraph like $a \rightarrow b-v$ in $\mathcal{C}$, a contradiction. Consequently, $\mathcal{P}^{\prime}$ is a chain graph.

If there exists an undirected cycle of length greater than 3 without a chord in $\mathcal{P}^{\prime}$, the cycle must contain $x$ and $y$, and there must be an undirected path from $x$ to $y$ in $\mathcal{C}$; otherwise, the cycle would also be in $\mathcal{C}$. From Lemma 3, every undirected path from $x$ to $y$ contains a vertex in $N_{x y}$, so every undirected path of length greater than two has a chord. Thus, every undirected path of length greater than 3 from $x$ to $y$ in $\mathcal{P}^{\prime}$ has a chord. This implies that every chain component of $\mathcal{P}^{\prime}$ is chordal.

Suppose that a subgraph like $\cdot \rightarrow \cdot-$ occurs as an induced subgraph of $\mathcal{P}^{\prime}$. Since $\Pi_{x}=\Pi_{y}$ in $\mathcal{C}$, the induced subgraph is not $\cdot \rightarrow x-y$ (or $\cdot \rightarrow$ $y-x)$. Thus, the induced subgraph like $\cdot \rightarrow \cdot-$ also occurs in $\mathcal{C}$. This is a contradiction since $\mathcal{C}$ is a completed PDAG, yielding a contradiction.

From Lemma 13 and the condition $\mathbf{i u}_{3}$ in Definition 9, all directed edges in $\mathcal{C}$ are also directed in $\mathcal{C}_{1}$. This implies that all directed edges in $\mathcal{P}$ are still compelled, and are thus strongly protected.

We now give proofs of Lemmas $6,7,8,9,10$ and 11, one by one.
Proof of Lemma 6. Because the operator "InsertU $x-y^{\prime \prime}=o \in \mathcal{O}_{\mathcal{C}}$ is valid and $\mathcal{C}_{1}$ is the resulting completed PDAG of $o$, we have that $x-y$ occurs in $\mathcal{C}_{1}$. We just need to show that the common neighbors of $x$ and $y$, denoted as $N_{x y}$, form a clique in $\mathcal{C}_{1}$.

If $N_{x y}$ is empty set or has only one vertex, the condition that $N_{x y}$ is a clique in $\mathcal{C}_{1}$ holds.

If there are two different vertices $z, u \in N_{x y}$ in $\mathcal{C}_{1}$, we have that $x-z-y$ and $x-u-y$ form a cycle of length of 4 in $\mathcal{C}_{1}$. The cycle is also in $\mathcal{C}$. Since the edge $x-y$ does not exist in $\mathcal{C}$ and $\mathcal{C}$ is a completed PDAG in which all undirected subgraphs are chordal graphs, we have that $z-u$ occurs in $\mathcal{C}$, so $z$ and $u$ are adjacent in $\mathcal{C}_{1}$. Hence the condition that $N_{x y}$ is a clique in $\mathcal{C}_{1}$ holds.

Proof of Lemma 7. We need to show the operator $o^{\prime}:=$ InsertU $x-y$ satisfies the conditions $\mathbf{i u}_{1}, \mathbf{i u}_{2}$ and $\mathbf{i u}_{3}$ in Definition 9 for completed PDAG $\mathcal{C}_{1}$ and that the resulting completed PDAG of $o^{\prime}$ is $\mathcal{C}$.

The condition $\mathbf{i u}_{1}$ clearly holds, since $x-y$ exists in $\mathcal{C}_{1}$ but not in $\mathcal{C}$. Lemma 15 implies that the graph obtained by deleting $x-y$ from $\mathcal{C}$ is the completed PDAG $\mathcal{C}_{1}$. Thus, the graph obtained by inserting $x-y$ into $\mathcal{C}_{1}$ is $\mathcal{C}$. This implies that InsertU $x-y$ is valid, and the condition $\mathbf{i u}_{2}$ holds.

Lemma 15 implies that the condition $\mathrm{iu}_{3}$ also holds.
Proof of Lemma 8. I will first show that there is no undirected edge $y-w$ that occurs in both $\mathcal{C}$ and $\mathcal{C}_{1}$. If $w-y$ occurs in $\mathcal{C}$, since $x$ and $y$ are not adjacent in $\mathcal{C}, x \rightarrow w-y$ does not occur in $\mathcal{C}$. There are three possible configurations between $x$ and $w$ in $\mathcal{C}$ : (1) $x$ is not adjacent to $w$, (2) $w \rightarrow x$ and (3) $x-w$. If $x$ is not adjacent to $w$ in $\mathcal{C}$, inserting $x \rightarrow y$ will result in $y \rightarrow w$ in $\mathcal{C}_{1}$. If $w \rightarrow x$ is in $\mathcal{C}$, inserting $x \rightarrow y$ will result in $w \rightarrow y$ in $\mathcal{C}_{1}$. If $x-w$ in $\mathcal{C}$, there is an undirected path from $y$ to $x$; that is, the first condition for InsertD to be valid, according to Lemma 3, does not hold. Thus we get that there is no undirected edge $y-w$ that occurs in both $\mathcal{C}$ and $\mathcal{C}_{1}$.

For any $w \in N_{y}$ in $\mathcal{C}_{1}$, the edge between $w$ and $y$ is directed in $\mathcal{C}$; that is, either $w \rightarrow y$ or $y \rightarrow w$ occurs in $\mathcal{C}$. If $y \rightarrow w$ is in $\mathcal{C}$, there are three possible configurations between $x$ and $w$ in $\mathcal{C}$ : (1) $x$ is not adjacent to $w$, (2) $w \rightarrow x$ and (3) $x \rightarrow w$. If $x$ and $w$ are not adjacent in $\mathcal{C}$, inserting $x \rightarrow y$ will result in $y \rightarrow w$ in $\mathcal{C}_{1}$. If $w \rightarrow x$ occurs in $\mathcal{C}$, inserting $x \rightarrow y$ is not valid for $\mathcal{C}$ since there would be a directed path from $y$ to $x$. If $x \rightarrow w$ occurs in $\mathcal{C}, w$ is common child of $x$ and $y$, so from condition $\operatorname{id}_{3}, y \rightarrow w$ occurs in $\mathcal{C}_{1}$ and $w \notin N_{y}$ in $\mathcal{C}_{1}$. Thus, we have that $w \rightarrow y$ must be in $\mathcal{C}$.

If there is another vertex $v \in N_{y}$ in $\mathcal{C}_{1}, v \rightarrow y$ must also be in $\mathcal{C}$. If $v$ and $w$ are not adjacent, $v \rightarrow y \leftarrow w$ forms a $v$-structure both in $\mathcal{C}$ and in $\mathcal{C}_{1} . w \rightarrow y$ must occur in $\mathcal{C}_{1}$ and, consequently, $w \notin N_{y}$ in $\mathcal{C}_{1}$ yielding a a contradiction. Thus, we know that any two vertices in $N_{y}$ are adjacent in $\mathcal{C} . N_{y}$ is therefore a clique in $\mathcal{C}_{1}$, and the operator DeleteD $x \rightarrow y$ is valid for $\mathcal{C}_{1}$; that is, the condition $\mathbf{i d}_{1}$ in Definition 9 holds.

Denote the modified PDAG of operator DeleteD $x \rightarrow y$ of $\mathcal{C}_{1}$ as $\mathcal{P}^{\prime}$. We need to show that the corresponding completed PDAG of $\mathcal{P}^{\prime}$ is $\mathcal{C}$. Equivalently, we just need to show $\mathcal{P}^{\prime}$ and $\mathcal{C}$ have the same skeleton and $v$ structures. Clearly, $\mathcal{P}^{\prime}$ and $\mathcal{C}$ have the same skeleton. If there is a $v$-structure in $\mathcal{C}$, but not in $\mathcal{C}_{1}$, it must be $x \rightarrow u \leftarrow y$, where $u$ is a common child of $x$ and $y$. From condition $\mathbf{i d}_{3}$ in Definition 9, $x \rightarrow u$ and $y \rightarrow u$ also occur in $\mathcal{C}_{1}$, so, these $v$-structures also exist in $\mathcal{P}^{\prime}$. This implies that all $v$-structures of $\mathcal{C}$ are also in $\mathcal{P}^{\prime}$. Moreover, the $v$-structures in $\mathcal{C}_{1}$ but not in $\mathcal{C}$ must be $x \rightarrow y \leftarrow v$, where $v$ is parent of $y$, and $x$ and $v$ are not adjacent in $\mathcal{C}_{1}$. Clearly, after we delete $x \rightarrow y$ from $\mathcal{C}_{1}$, these $v$-structures will not exist in $\mathcal{P}^{\prime}$. This implies that all $v$-structures of $\mathcal{P}^{\prime}$ are in $\mathcal{C}$. So, $\mathcal{P}^{\prime}$ and $\mathcal{C}$ have the same $v$-structures.

For any $v \rightarrow y$ in $\mathcal{C}_{1}$, if $v-y$ is in $\mathcal{C}, v$ must be parent of $x$. If $x$ and $v$ are not adjacent, inserting $x \rightarrow y$ to $\mathcal{C}$ will result in $y \rightarrow v$ in $\mathcal{C}_{1}$. Moreover,

$x-v-y$ does not exist in $\mathcal{C}$ since InsertD $x \rightarrow y$ is a valid operator, and $x \rightarrow v-y$ does not occur in $\mathcal{C}$. Thus, for any $v$ that is a parent of $y$ but not a parent of $x$, the directed edge $v \rightarrow y$ also occurs in the resulting completed PDAG $\mathcal{C}$. That is, the condition $\mathrm{id}_{2}$ in Definition 9 holds.

Proof of Lemma 9. To prove this lemma, we first introduce Lemmas 16 and 17. Let $L=\left(u_{1}, u_{2}, \ldots, u_{k}\right)$ be a partially directed path from $u_{1}$ to $u_{k}$ in a graph. A path $L_{2}=\left(u^{1}, \ldots, u^{k}\right)$ is a sub-path of $L_{1}$ if all vertices in $L_{1}$ are in $L$ and have the same order as in $L$. We say that a partially directed path is shortest if it has no smaller sub-path.

Lemma 16. Let $\mathcal{C}$ be a completed $P D A G$, and let $L_{1}$ be a partially directed path from $y$ to $x$ in $\mathcal{C}$. Then there exists a shortest sub-path of $L_{1}$, denoted as $L_{2}=y-u_{1}-\cdots-u_{k} \rightarrow \cdots \rightarrow x$, in which there exists a $k$ such that all edges occurring before $u_{k}$ in the path are undirected, and all edges occurring after $u_{k}$ are directed.

Proof. We just need to show that a directed edge must be followed by a directed edge in the shortest sub-path. If not, $u_{i} \rightarrow u_{i+1}-u_{i+2}$ occurs in $L_{2}$. Because $\mathcal{C}$ is a completed PDAG, $u_{i}$ and $u_{i+2}$ must be adjacent; otherwise $u_{i+1} \rightarrow u_{i+2}$ occurs in $\mathcal{C}$. If $u_{i} \rightarrow u_{i+2}$ occurs in $\mathcal{C}, L_{2}$ is not a shortest path. If $u_{i} \leftarrow u_{i+2}$ occurs in $\mathcal{C}, u_{i+1} \leftarrow u_{i+2}$ must be in $\mathcal{C}$.

Lemma 17. If the graph $\mathcal{P}_{1}$ obtained by deleting $a \rightarrow b$ from a completed $P D A G \mathcal{C}$ can be extended to a new completed $P D A G, \mathcal{C}_{1}$, then we have that for any directed edge $x \rightarrow y$ in $\mathcal{C}$, if $y$ is not $b$ or a descendent of $b$, then $x \rightarrow y$ occurs in $\mathcal{C}_{1}$.

Proof. Because $x \rightarrow y$ occurs in $\mathcal{C}$, so it is strongly protected in $\mathcal{C}$. If $x \rightarrow y$ does not occur in $\mathcal{C}_{1}$, it is not strongly protected in $\mathcal{C}_{1}$ from Lemma 2. From the definition of strongly protected, we know that the four cases in Figure 1 in which $v \rightarrow u$ is strongly protected do not involve any descendant of $u$. Thus, if $x \rightarrow y$ is not compelled in $\mathcal{C}_{1}$, there must exist a directed edge $w \rightarrow z$ between two nondescendants of $y$ such that the edges between nondescendants of $z$ are strongly protected, and $w-z$ is no longer strongly protected in $\mathcal{P}_{1}$. Because $\mathcal{P}_{1}$ is obtained by deleting $a \rightarrow b, z$ is nondescendant of $b$, we have that $w \rightarrow z$ is strongly protected in $\mathcal{P}_{1}$, yielding a contraction.

We now give a proof of Lemma 9:
Proof of Lemma 9. Since $\mathcal{C} \in \mathcal{S}_{p}^{n}$, we have $n_{\mathcal{C}_{1}}<n$. That is, the condition $\operatorname{id}_{1}$ in Definition 9 holds for InsertD $x \rightarrow y$ of $\mathcal{C}_{1}$.

For any undirected edge $w-y$ in $\mathcal{C}, x$ must be parent of $w$; otherwise the edge between $y$ and $w$ is directed. Then deleting $x \rightarrow y$ from $\mathcal{C}$ will result

in $w \rightarrow y$ in $\mathcal{C}_{1}$. Thus, we have that all $N_{y}$ in $\mathcal{C}$ become parents of $y$ in $\mathcal{C}_{1}$. From the condition $\mathbf{d d}_{2}$, the parents of $y$ but not $x$ in $\mathcal{C}$ are also parents of $y$ in $\mathcal{C}_{1}$. If there is a partially directed path from $y$ to $x$ in $\mathcal{C}_{1}$, then the vertex adjacent to $y$ in this path must be a child of $y$ or a vertex that is parent of $y$ and $x$ in $\mathcal{C}$. We will show that if the vertex is not a parent of $y$ and $x$ in $\mathcal{C}$, there exists a contradiction.

If there is a partially directed path from $y$ to $x$ in $\mathcal{C}_{1}$, we can find a shortest partially directed path like $y-u_{1}-\cdots-u_{k} \rightarrow \cdots \rightarrow x$ from Lemma 16, denoted as $L_{1}$. Any directed edge, say $u_{i} \rightarrow u_{i+1}$, in $L_{1}$ does not become $u_{i} \leftarrow u_{i+1}$ in $\mathcal{C}$. If $L_{1}$ does not include undirected edges in $\mathcal{C}_{1}$, we have that the vertices of $L_{1}$ form a partially directed cycle in $\mathcal{C}$. We just need to show that the vertices of the undirected path $L_{1}$ also form a partially directed path in $\mathcal{C}$.

Suppose $y \rightarrow u_{1}$ occurs in $\mathcal{C}$. If $u_{1}-u_{2}$ is undirected in $\mathcal{C}$, then $y \rightarrow u_{2}$ must occur in $\mathcal{C}$, and consequently, $L_{1}$ will not be shortest in $\mathcal{C}_{1}$. If $u_{2} \rightarrow u_{1}$ occurs in $\mathcal{C}$, there exists a $v$-structure $u_{2} \rightarrow u_{1} \leftarrow y$ in $\mathcal{C}_{1}$; otherwise $u_{2}$ and $y$ are adjacent, and $L_{1}$ is not the shortest path in $\mathcal{C}_{1}$. Thus, $u_{1} \rightarrow u_{2}$ must occur in $\mathcal{C}$. In this manner, we get that all edges in $y-u_{1}-\cdots-u_{k} \rightarrow \cdots \rightarrow x$ are directed in $\mathcal{C}$ and are directed from $u_{i} \rightarrow u_{i+1}$. This implies that there exists a partially directed cycle in $\mathcal{C}$. So, $u_{1}$ must be a parent of $y$ and $x$ in $\mathcal{C}$. We have $u_{1} \in \Omega_{x y}$ and every partially directed path of $\mathcal{C}_{1}$ from $y$ to $x$ contains at least one vertex in $\Omega_{x y}$.

Since all vertices in $\Omega_{x y}$ in $\mathcal{C}_{1}$ are parents of $x$ and $y$ in $\mathcal{C}$, if there are two vertices, say $w_{1}, w_{2} \in \Omega_{x y}$, that are not adjacent, the subgraph $w_{1} \rightarrow y \leftarrow w_{2}$ could be a $v$-structure in $\mathcal{C}_{1}$. So, all vertices in $\Omega_{x y}$ in $\mathcal{C}_{1}$ are adjacent and $\Omega_{x y}$ is a clique.

We have that the parents of $y$ in $\mathcal{C}_{1}\left(\left(\Pi_{y}\right)_{\mathcal{C}_{1}}\right)$ are in the union of the parents and neighbors of $y$ in $\mathcal{C}\left(\left(\Pi_{y} \cup N_{y}\right)_{\mathcal{C}_{1}}\right)$. If there is at least one neighbor $u$ of $y$ in $\mathcal{C}, u$ must be child of $x$ in $\mathcal{C}$ and parent of $y$ in $\mathcal{C}_{1}$, so parents of $x$ and $y$ are not the same. If there is no neighbor of $y$ in $\mathcal{C}$, the parents of $y$ in $\mathcal{C}_{1}$ are the same as in $\mathcal{C}$, except those vertices that are parents of $x$, that is, $\left(\Pi_{y}-\Pi_{x}\right)_{\mathcal{C}_{1}}=\left(\Pi_{y}-\Pi_{x}\right)_{\mathcal{C}}$. At the same time, from Lemma 17, the parents of $x$ in $\mathcal{C}_{1}$ are also the parents of $x$ in $\mathcal{C}$. Thus, the parents of $x$ and $y$ are not the same in $\mathcal{C}_{1}$. From Lemma 3, we have that InsertD $x \rightarrow y$ is valid for $\mathcal{C}_{1}$, and condition $\mathbf{i d}_{2}$ holds.

Denote the modified PDAG of operator InsertD $x \rightarrow y$ of $\mathcal{C}_{1}$ as $\mathcal{P}^{\prime}$. We need to show that the corresponding completed PDAG of $\mathcal{P}^{\prime}$ is $\mathcal{C}$. Equivalently, we just need to show that $\mathcal{P}^{\prime}$ and $\mathcal{C}$ have the same skeleton and $v$-structures. Clearly, $\mathcal{P}^{\prime}$ and $\mathcal{C}$ have the same skeleton. A $v$-structure that is in $\mathcal{C}$ but not in $\mathcal{C}_{1}$ must have the form $x \rightarrow y \leftarrow u$, where $u$ is parent of $y$ but not adjacent to $x$. From condition $\mathbf{d d}_{2}$ in Definition 9, $u \rightarrow y$ also occurs in $\mathcal{C}_{1}$, so such a $v$-structure must also exist in $\mathcal{P}^{\prime}$. This implies that all $v$-structures of $\mathcal{C}$ are also in $\mathcal{P}^{\prime}$. Moreover, the $v$-structures in $\mathcal{C}_{1}$ but not

in $\mathcal{C}$ must have the form $x \rightarrow v \leftarrow y$, where $v$ is a common child of $y$ and $x$ in $\mathcal{C}_{1}$. Clearly, after we insert $x \rightarrow y$ to $\mathcal{C}_{1}$, this is no longer a $v$-structure in $\mathcal{P}^{\prime}$ implying that all $v$-structures of $\mathcal{P}^{\prime}$ are in $\mathcal{C}$. Thus, $\mathcal{P}^{\prime}$ and $\mathcal{C}$ have the same $v$-structures.

Let the modified graph of DeleteD $x \rightarrow y$ from $\mathcal{C}$ be $\mathcal{P}$; we know that $\mathcal{P}$ and $\mathcal{C}_{1}$ have the same $v$-structures. Thus, for any $u$ that is a common child of $x$ and $y$ in $\mathcal{C}_{1}, x \rightarrow u \leftarrow y$ is a $v$-structure in $\mathcal{P}$. This implies that $y \rightarrow u$ occurs in $\mathcal{C}$ and the condition $\mathbf{i d}_{3}$ hold.

Proof of Lemma 10. Since $x, z$ and $y$ are in the same chain component of $\mathcal{C}$, they have the same parent set in $\mathcal{C}$. The modified graph of $o^{\prime}$ has the same skeleton and $v$-structures as $\mathcal{C}_{1}$ because all compelled edges in $\mathcal{C}$ remain compelled in $\mathcal{C}_{1}$. We just need to prove that the operator $o^{\prime}$ is valid and equivalently to prove that the conditions $\mathbf{r m}_{1}, \mathbf{r m}_{2}$ and $\mathbf{r m}_{3}$ hold for $\mathcal{C}_{1}$.

We now show that the condition $\mathbf{r m}_{1}, x$ and $y$ have the same parents in $\mathcal{C}_{1}$ holds. Because $x$ and $y$ have the same parents in $\mathcal{C}$, and all directed edges in $\mathcal{C}$ occur in $\mathcal{C}_{1}$, we just need to consider the neighbors of $x$ or $y$. Let $w-y$ be any undirected edge in $\mathcal{C}$, we consider the edges between $w$ and $x$ or $z$ :
(1) If both $w-z$ and $x-w$ occur in $\mathcal{C}, w-y$ and $w-x$ must be undirected in $\mathcal{C}_{1}$.
(2) If $w-z$ occurs but $x-w$ does not occur in $\mathcal{C}, z \rightarrow w$ and $y \rightarrow w$ must be in $\mathcal{C}_{1}$.
(3) If $x-w$ occurs but $w-z$ does not occur in $\mathcal{C}$, there is an undirected cycle of length 4 without a chord in $\mathcal{C}$. Thus, this case will not occur.
(4) If neither $w-z$ nor $x-w$ occur in $\mathcal{C}$, and there is no undirected path other than $w-y-z$ from $w$ to $z$ in $\mathcal{C}$, then $w-y$ occurs in $\mathcal{C}_{1}$. If there exists another undirected path from $w$ to $z$, there must exist an undirected path of length 2 like $w-u^{\prime}-z$ in $\mathcal{C}$, and $y$ is adjacent to $u^{\prime}$. In this case, $y-w$ occurs in $\mathcal{C}_{1}$ when $x-u^{\prime}$ occurs and $y \rightarrow w$ occurs when $x$, and $u^{\prime}$ are not adjacent.

Thus, there are no neighbors of $y$ in $\mathcal{C}$ that become parents of $y$ in $\mathcal{C}_{1}$; that is, $y$ has the same parents in both $\mathcal{C}_{1}$ and $\mathcal{C}$. Similarly, $x$ has the same parents in both $\mathcal{C}_{1}$ and $\mathcal{C}$. we get $x$ and $y$ have the same parents in $\mathcal{C}_{1}$, and the condition $\mathbf{r m}_{1}$ holds.

All parents of $x$ must also be parents of $z$ in $\mathcal{C}_{1}$ since they are in the same chain component. For any $w \in N_{x y}, w-z$ also occurs in $\mathcal{C}$; otherwise $x-z-y-w-x$ would form cycle of length 4 without a chord. We have $w \rightarrow z$ must be in $\mathcal{C}_{1}$, otherwise a new $v$-structure will occur in $\mathcal{C}_{1}$. Thus, we have $\Pi(x) \cup N_{x y} \subset \Pi(z)$ in $\mathcal{C}_{1}$.

For any $w \in \Pi(z)$ in $\mathcal{C}_{1}$, if $w \in \Pi(z)$ in $\mathcal{C}$, it must also be parent of $x, y$ and $z$ in $\mathcal{C}_{1}$, so $w \in \Pi(x)$ in $\mathcal{C}_{1}$. If $w-z$ is an undirected edge in $\mathcal{C}$, there exist undirected edges $w-x$ and $w-y$ in $\mathcal{C}$ such that $w \rightarrow z$ is in $\mathcal{C}_{1}$. Thus,

$w \in N_{x y}$ in $\mathcal{C}_{1}$. We have that $w \in \Pi(x) \cup N_{x y}$ and $\Pi(z) \subset \Pi(x) \cup N_{x y}$ in $\mathcal{C}_{1}$. Thus, $\Pi(z)=\Pi(x) \cup N_{x y}$ in $\mathcal{C}_{1}$, and the condition $\mathbf{r m}_{2}$ holds.

Any undirected path between $x$ and $y$ in $\mathcal{C}_{1}$ will also be an undirected path in $\mathcal{C}$, so these paths contain at least one vertex in $N_{x y}$ in $\mathcal{C}$. From the proof above, any vertex in $N_{x y}$ in $\mathcal{C}$ is also a vertex of $N_{x y}$ in $\mathcal{C}_{1}$. Thus any undirected path between $x$ and $y$ contains a vertex in $N_{x y}$ in $\mathcal{C}_{1}$, and the condition $\mathbf{r m}_{3}$ holds.

Proof of Lemma 11. From Lemma 5 and the condition $\mathbf{r m}_{3}$, there exists a consistent extension of $\mathcal{C}$, denoted by $\mathcal{D}$, such that all neighbors of $x$ in $\mathcal{C}$ are children of $x$ in $\mathcal{D}$, and all neighbors of $y$ in $\mathcal{C}$ are parents of $x$ in $\mathcal{D}$. Changing $y \rightarrow z$ to $z \rightarrow y$ in $\mathcal{D}$, we obtain a new graph $\mathcal{D}^{\prime}$. From the proof of Lemma 4, we can get that (1) $\mathcal{D}^{\prime}$ is a DAG, (2) $\mathcal{D}^{\prime}$ is a consistent extension of $\mathcal{C}_{1}$. Thus, $\mathcal{D}$ is a consistent extension of the PDAG that results from making the $v$-structure $x \rightarrow z \leftarrow y$ in $\mathcal{C}_{1}$. Thus, we can get $\mathcal{C}$ by applying MakeV $x \rightarrow z \leftarrow y$ to $\mathcal{C}_{1}$. This implies that MakeV $x \rightarrow z \leftarrow y$ is a valid operator of $\mathcal{O}_{1}$ and satisfies the condition $\mathrm{mv}_{1}$.

Proof of Theorem 5. In order to prove this theorem, we first introduce three results: Lemmas 18, 19 and 20.

Lemma 18. For any completed PDAG $\mathcal{C}$ containing at least one undirected edge, there exists an undirected edge $x-y$ for which $N_{x y}$ is a clique.

Lemma 19. For any completed PDAG $\mathcal{C}$, if $x \rightarrow y$ occurs in $\mathcal{C}$, then $\Pi_{x} \neq \Pi_{y} \backslash x$.

A proof of Lemmas 18 and 19 can be found in Chickering [6].
Lemma 20. For any completed PDAG $\mathcal{C}$ containing no undirected edges and at least one directed edge, there exists at least one vertex $x$ for which any parent of $x$ has no parent.

Proof. The following procedure will find the vertex whose parent has no parent. Let $a \rightarrow b$ be a directed edge in $\mathcal{C}$, set $y=a$ and $x=b$.
(1) If $\Pi_{y}$ is not empty, choose any vertex $u$ in $\Pi_{y}$, set $x=y$ and $y=u$. Repeat this step until we find a directed edge $y \rightarrow x$ for which $\Pi_{y}$ is empty.
(2) Since $\Pi_{y}$ is empty, from Lemma 19, there exists at least one vertex other than $y$ in $\Pi_{x}$. If there is a vertex $u \in \Pi_{x}$ and $u \neq y$ such that $\Pi_{u}$ is not empty, choose a vertex in $\Pi_{u}$, denoted as $v$ and set $y=v$ and $x=u$, and go to step 1 .

Since $\mathcal{C}$ is an acyclic graph with finite vertices, above procedure must end at the step in which the parents of $x$ have no parents.

We now show a proof of Theorem 5.
Proof of Theorem 5. We need to show that for any two completed PDAGs $\mathcal{C}_{1}, \mathcal{C}_{2} \in \mathcal{S}$, there exists a sequence of operators in $\mathcal{O}$ such that $\mathcal{C}_{2}$ can be obtained by applying a sequence of operators to PDAGs, starting from $\mathcal{C}_{1}$. Because $\mathcal{O}$ is reversible, any operator in $\mathcal{O}$ has a reversible operator, so we just need to show that any completed PDAG can be transferred to empty graph without edges. The procedure includes three basic steps.
(1) Deleting all undirected edges.

From Lemma 18, for any completed PDAG containing at least one undirected edge, we can find an operator with type of DeleteU that satisfies the condition $\mathbf{d u}_{1}$ in Definition 9. We can delete an undirected edge with this operator and get a new completed PDAG whose skeleton is a subgraph of the skeleton of the initial completed PDAG. Repeating this procedure, we can get a completed PDAG, denoted as $\mathcal{C}_{i}$, which contains no undirected edges.
(2) Deleting some directed edges.

From Lemma 20, we can find a vertex, denoted as $x$, whose parents have no parents in the completed PDAG $\mathcal{C}_{i}$. If $\Pi_{x}$ contains more than two vertices, we can choose a vertex $u \in \Pi_{x}$. Because (1) $N_{x}$ is empty in $\mathcal{C}_{i}$, and (2) any other directed edge $v \rightarrow x$ forms a $v$-structure in $\mathcal{C}_{i}$, we have that $v \rightarrow x$ is also compelled in the completed PDAG obtained by deleting directed edge $u \rightarrow x$ from $\mathcal{C}_{i}$. We can delete $v \rightarrow x$ from $\mathcal{C}_{i}$ and get a new completed PDAG whose skeleton is a subgraph of the skeleton of the initial one. Thus, the new completed PDAG is in $\mathcal{S}$. Repeat this procedure for all other directed edges $v^{\prime} \rightarrow x$ in which $v^{\prime} \in \Pi_{x}$ until there are only two vertices in $\Pi_{x}$ in the new completed PDAG, denoted as $\mathcal{C}_{j}$.
(3) Removing a $v$-structure.

The conditions $\mathrm{rm}_{1}, \mathrm{rm}_{2}$ and $\mathrm{rm}_{3}$ hold for the $v$-structure $y \rightarrow x \leftarrow u$ in $\mathcal{C}_{j}$, so, we can remove $y \rightarrow x \leftarrow u$ from $\mathcal{C}_{j}$ and get a new completed PDAG whose skeleton is a subgraph of the skeleton of the initial graph. Denote the resulting completed PDAG as $\mathcal{C}_{k}$; it may still contain some undirected edges.

By repeatedly applying the above the steps in sequence, we can finally obtain a graph without any edges.

Acknowledgments. This work was partly done when Yangbo He was visiting Department of Statistics in UC Berkeley. Yangbo He would like to thank Prof. Lan Wu for her support of this visit. Jinzhu Jia's work was done when he was a postdoc in UC Berkeley. We are very grateful to Adam Bloniarz for his comments that significantly improved the presentation of our manuscript. We also thank Jasjeet Sekhon, the co-Editor, the Associate Editor and the reviewer for their helpful comments and suggestions.

# SUPPLEMENTARY MATERIAL 

## Supplement to "Reversible MCMC on Markov equivalence classes of sparse directed acyclic graphs" (DOI: 10.1214/13-AOS1125SUPP; .pdf). In

this supplementary note, we give some algorithms, examples, an experiment and the proofs of the results in this paper.
