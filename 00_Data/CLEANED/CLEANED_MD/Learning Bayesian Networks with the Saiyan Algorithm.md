# Learning Bayesian Networks with the Saiyan algorithm 

ANTHONY C. CONSTANTINOU, Queen Mary University of London


#### Abstract

Some structure learning algorithms have proven to be effective in reconstructing hypothetical Bayesian Network (BN) graphs from synthetic data. However, in their mission to maximise a scoring function, many become conservative and minimise edges discovered. While simplicity is desired, the output is often a graph that consists of multiple independent subgraphs that do not enable full propagation of evidence. While this is not a problem in theory, it can be a problem in practice. This paper examines a novel unconventional associational heuristic called Saiyan, which returns a directed acyclic graph that enables full propagation of evidence. Associational heuristics are not expected to perform well relative to sophisticated constraint-based and score-based learning approaches. Moreover, forcing the algorithm to connect all data variables implies that the forced edges will not be correct at the rate of those identified unrestrictedly. Still, synthetic and realworld experiments suggest that such a heuristic can be competitive relative to some of the well-established constraint-based, score-based, and hybrid learning algorithms.


CCS Concepts: $\cdot$ Computing methodologies $\rightarrow$ Machine learning; Artificial Intelligence

## KEYWORDS

Bayesian networks, directed acyclic graphs, graphical models, structure learning

## ACM Reference format:

Anthony Constantinou. 2020. Learning Bayesian Networks with the Saiyan algorithm. ACM Transactions on Knowledge Discovery from Data, XXXX. 2 (XXXX 2020), XX pages.
https://doi.org/
This research was supported by the ERSRC Fellowship project EP/S001646/1 on Bayesian Artificial Intelligence for Decision Making under Uncertainty, and by The Alan Turing Institute in the UK. Author's addresses: A. C. Constantinou, Bayesian Artificial Intelligence research lab, Risk and Information Management (RIM) research group, School of Electronic Engineering and Computer Science, Queen Mary University of London, London, UK, E1 4NS; e-mail: a.constantinou@qmul.ac.uk; The Alan Turing Institute, British Library, 96 Euston Road, London, NW1 2DB, UK.

## 1 INTRODUCTION

A Bayesian Network (BN) is a type of a probabilistic graphical model introduced by Pearl [1], [2]. If we assume that the arcs between nodes in a BN model represent causation, then a BN is a unique Directed Acyclic Graph (DAG) that enables us to reason about intervention. However, if we assume that the arcs between nodes represent some dependency that is not necessarily a causal relationship, then a BN is a Partial Directed Acyclic Graph (PDAG) and hence, not a causal graph. A PDAG, also called patterns by Spirtes et al [3], essential graphs by Anderson et al [4], and maximally oriented graphs by Meek [5], incorporates both directed and undirected edges and represents an equivalence class of DAGs [6].

Constructing BNs typically involves two steps: a) determining the graphical structure of the model that captures the relationships between variables, and b) parameterising the Conditional Probability Tables (CPTs) to capture the relationship between variables. The graph of a BN can be determined by knowledge, learned from data, or a combination of both. In this paper we are interested in learning BN graphs from observational data, which is a particularly challenging and, depending on the number of variables, an NP-Hard problem [7], [8].

The algorithms that learn the graphical structure of a BN typically fall under two categories. First, the score-based methods represent a classic machine learning approach where algorithms search for different structures and score them, in terms of how well the fitting distributions agree with the empirical distributions, determined by a scoring function. The graph with the highest score is returned as the preferred graph. Popular score-based algorithms include the K2 [9], Sparse Candidate [10], Optimal Reinsertion [11], and the GES algorithm [12].

Second, the constraint-based methods use conditional independence tests to establish edges between variables, often under causal or influential assumptions. This learning process was inherited from the Inductive Causation (IC) algorithm [13]. The Peter Clark (PC) algorithm [3], some variants of the Greedy Equivalence Search (GES), and the Grow-Shrink (GS) algorithm have had major impact in this area of research. Hybrid algorithms that combine both approaches also exist and include the Max-Min Hill-Climbing (MMHC) algorithm [14] and the L1Regularisation paths [15].

Other score-based approaches that put greater emphasis on pruning the search space of possible graphs, and some guarantee to return the graph that maximises a scoring function, include the Integer Programming (IP) methods by Cussens [16] and Cussens et al [17] that are based on the IP formulation of Bartlett and Cussens [18] and which form part of the GOBNILP system. Other relevant approaches include the Integer Linear Programming (ILP) bounded treewidth approach by Parviainen et al [19], the linear program acyclic approach by Jaakkola et al [20] that reduces search space based on various constraints, the special vector characteristic imset by Hemmecke et al [21], and the branch-and-bound (BnB) linear programming method by Peharz and Pernkopf [22] that maximises a discriminative score to offer an exact solution. Moreover, various dynamic programming methods include those by Silander and Myllymaki [23] that return the global optimal BN structure more efficiently than earlier methods (albeit restricted to 30 variables), by Koivisto and Sood [24] on exact Bayesian structure discovery, by Ott et al [25] on optimal structures for small gene networks, and by Singh and Moore [26] on achieving global maxima with exponential (rather than super-exponential) search space.

Other notable approaches include the A* search-based algorithm by Yuan and Malone [27] that learns the structure based on the most promising part of the solution space, the frontier breadth-first BnB search method by Malone et al [28] that improves memory efficiency, the BnB algorithm by de Campos and Ji [29] that integrates structural constraints with data in a way to guarantee global optimality, the nonparametric regression approach by Imoto et al [30] to capture non-linear relationships between genes, and the constraint-based depth-first BnB search method by van Beek and Hoffmann [31] that reduces the search space using various constraints.

This paper presents the Saiyan algorithm that is based on an associational heuristic with the unconventional restriction to output a DAG that enables full propagation of evidence. The paper is structured as follows: Section 2 describes the algorithm, Section 3 presents the results, and Section 4 provides the concluding remarks and limitations along with directions for future work.

# 2 THE SAIYAN ALGORITHM 

The Saiyan algorithm is based on a novel associational score that measures the level of difference between prior and posterior distributions. The algorithm follows a six-phase process to construct a DAG, with optional temporal and directed constraints, as illustrated in Fig 1. The high-level reasoning for each of the phases is as follows:
i. Phase 1 generates a graph based on the combined causal effect each pair of variables has on each remaining third variable. While the above process leads to multiple arcs between

nodes, only the arc that maximises a score function (refer to Section 2.1) is preserved for phase 2 .
ii. Phase 2 ensures that model dimensionality is reasonably low relative to the input data. If a CPT has an expected parameter size greater than the sample size of the data, the weakest parent of that CPT is pruned until the dimensionality space is deemed acceptable.
iii. Phase 3 prunes the weakest arc in a cycle until the graph becomes acyclic.
iv. Phase 4 generates a new set of scores that are based on pairwise effect, rather than on the combined causal effect, and which are considered for further graphical modifications in subsequent phases.
v. Phase 5 uses the scores from phase 4 to simplify the graph via arc removals and arc reversals.
vi. Phase 6 connects any independent nodes, or graphical fragments, to enable full propagation of evidence.

Fig A1 illustrates some of the graphical structures generated at different learning phases of the Saiyan algorithm. The outputs are based on the results of the Football case study (refer to Section 3.1). The subsections that follow describe the scoring function as well as each of the six phases in turn.
![img-0.jpeg](img-0.jpeg)

Fig. 1. The overall process of the Saiyan algorithm.

# 2.1 The MMD scoring function 

The scoring function investigated in this paper is called the Mean/Max/MeanMax Marginal Discrepancy (MMD). This score can be used to return either the average Mean (MN), average Max (MX), or average MeanMax (MM) discrepancies between marginal probabilities in prior and posterior distributions. The preferred type of discrepancy is specified as a parameter input. A higher discrepancy score between prior and posterior distributions indicates a stronger dependency.

If we assume discrepancy type MN to compute the score of B being a parent of A , the output will be the average over $i$ distributional differences of mean marginal discrepancies between $P(A)$ and $P\left(A \mid b_{i}\right)$; i.e., $\mathrm{MMD}_{M N}(A \leftarrow B)$ is

$$
\left(\sum_{i}^{s_{B}}\left[\left(\sum_{j}^{s_{A}}\left|P\left(a_{j}\right)-P\left(a_{j} \mid b_{i}\right)\right|\right) / s_{A}\right]\right) / s_{B}
$$

for each state $a_{j}$ in $A$ and $b_{i}$ in $B$, and over $s_{A}$ states in $A$ and $s_{B}$ states in $B$. In the case of MX, the score is simply the average maximum, rather than the average mean, discrepancy between marginal probabilities. In the case of MM, the score is the average of MN and MX scores.

Consider the hypothetical prior and posterior distributions shown in Table 1. The mean marginal discrepancy, for example, between $P(A)$ and $P\left(A \mid b_{1}\right)$ is 0.025 , whereas the maximum marginal discrepancy is 0.05 . Based on these discrepancies, and over all three discrepancy assessments between $P(A)$ and $P\left(A \mid b_{i}\right)$, the three MMD scores are:

$$
\begin{gathered}
\mathrm{MMD}_{M N}(A \leftarrow B)=(0.025+0.05+0.15) / 3=0.075 \\
\mathrm{MMD}_{M X}(A \leftarrow B)=(0.05+0.1+0.25) / 3=0.1333 \\
\mathrm{MMD}_{M M}(A \leftarrow B)=(0.075+0.1333) / 2=0.1042
\end{gathered}
$$

Table 1. Hypothetical Prior and Posterior distributions used to illustrate the computation of the three different types of the MMD score.


# 2.2 Phase 1: Combined causal effect search 

At phase 1, the algorithm searches over all possible $C \rightarrow A \leftarrow B$ structures to measure the MMD score each pair of parents $\{B, C\}$ has on each residual data variable $A$. For example, the score $\mathrm{MMD}_{M N}(C \rightarrow A \leftarrow B)$ is

$$
\left(\sum_{k}^{s_{C}} \sum_{i}^{s_{B}}\left[\left(\sum_{j}^{s_{A}}\left|P\left(A_{j}\right)-P\left(A_{j} \mid B_{i}, C_{k}\right)\right|\right) / s_{A}\right]\right) /\left(s_{B}+s_{C}\right)
$$

The resulting score is assigned to both arcs entering $A$, from $B$ and $C$, as long as the discrepancy score is greater than the threshold $\theta$ specified by the user; otherwise, the arcs are not drawn.

When this process completes it produces graph $G_{1 A}$ as shown in Fig 2, which is based on four hypothetical variables, and shows all arcs (including duplicates) with scores greater than $\theta$. For example, and with reference to $G_{1 A}$ in Fig 2, setting $\theta$ to 0.15 would not have drawn the two arcs entering $A$, from $B$ and $C$, with score 0.121 .

Graph $G_{1 A}$ is then revised into $G_{1 B}$ by eliminating duplicate arcs and preserving the maximum score over all duplicates. A third revision follows, that produces graph $G_{1 C}$ from $G_{1 B}$, in which bi-directions are eliminated by preserving the direction that maximises MMD, as illustrated in Fig 2. Algorithm 1 describes this process, with optional code to account for temporal and directed knowledge-based constraints highlighted in grey.
![img-1.jpeg](img-1.jpeg)

Fig. 2. The three subphases of phase 1, based on hypothetical data. Red dashed arcs represent arcs eliminated.

ALGORITHM 1: Phase 1, with optional code for knowledge-based constraints in grey shading.
Input: variables $x$, discrepancy threshold $\theta$
Output: graph $G_{1 C}$
// Produce graph $G_{1 A}$ in phase 1.
List $L$
for each variable $x_{i} \in x$ do
for each remaining variable $x_{j} \in x$ do
for each remaining variable $x_{k} \in x$ do
if $x_{i} \leftarrow x_{j}$ and $x_{i} \leftarrow x_{k}$ satisfy constraints then
add MMD $\left(P\left(x_{i}\right), P\left(x_{i} \mid x_{j}, x_{k}\right)\right)$ score $s$ in $L$ if $s>\theta$
end if
end for
end for
end for
// Produce graph $G_{1 B}$ in phase 1, revised from $G_{1 A}$.
for each $s \in L$ do
if $s$ relates to an arc that is a directed constraint then

$$
s=1
$$

end if
Eliminate duplicate arcs and preserve $\max (s)$
end for
// Produce graph $G_{1 C}$ in phase 1, revised from $G_{1 B}$.
for each $s \in L$ do
Eliminate the bi-directed arc with the lowest $s_{2}$
end for

# 2.3 Phases 2 and 3: Dimensionality and Acyclic 

At phase 2, the algorithm determines the maximum number of parents a node can have, as described in Algorithm 2. The maximum number of parents is determined by CPT size relative to the sample size of the input data. This process ensures that the expected number of parameters of the average CPT with $a$ parents will not be greater than the sample size of the data. Setting parameter input $c=$ 1 represents a more conservative choice where the maximum number of parents further decreases by 1 .

Once the maximum number of parents is determined, the algorithm revises $G_{1 C}$ into $G_{2}$ by pruning the excess parents that violate this restriction, starting from the weakest parent in terms of MMD score. For a visual example, refer to the first three graphs in Fig A1 where the maximum number of parents is determined to be 3 .

At phase 3, the algorithm searches for cycles in $G_{2}$ and breaks them until the graph becomes acyclic. This is achieved by removing the weakest arc in a cycle, one at a time, as determined by MMD score. This process is repeated until no cycles exist. The result is graph $G_{3}$ (also as shown in Fig A1).

ALGORITHM 2: Determining max parents during phase 2.
Input: user input $c$, sample size $n$, average states $\bar{y}$
Output: $a$
$a=1$
threshold $=1$
convergence $=2$
while convergence $>$ threshold do
convergence $=n / \bar{y}^{(a+2)}$
if convergence $>$ threshold do
$a++$
end if
end while
$a=a-c$

### 2.4 Phases 4 and 5: Pairwise effect search, Reduction and Reversal

As initially shown in Fig 1, phase 4 generates a new set of scores that are based on pairwise rather than combined causal effect, and these scores are used in subsequent phases to perform further graphical modifications. In computing the pairwise scores, phase 4 also produces the supplementary fully connected undirected graph $G_{4}$, as shown in the example of Fig A1. If the MMD score is set to

type MN, then each undirected edge $A-B$ in $G_{4}$ is assigned the average MMD score of $A \rightarrow B$ and $A \leftarrow B$; i.e., $\mathrm{MMD}_{M N}(A-B)$ is

$$
\left[\mathrm{MMD}_{M N}(A \leftarrow B)+\mathrm{MMD}_{M N}(A \rightarrow B)\right] / 2
$$

Phase 5 begins by eliminating edges in the supplementary graph $G_{4}$, one by one, starting from the edge with the lowest score. As described in Algorithm 3, for each edge $A-B$ eliminated, if $A$ and $B$ share neighbour $C$ (implying that edges $A-C$ and $B-C$ have MMD scores greater than that of $A-B$ ), the 'reduction' step is activated. This step checks if the edge eliminated in $G_{4}$ exists in $G_{3}$ as an arc and if yes, and assuming the edge eliminated in $G_{4}$ is $A-B$ and the respective arc in $G_{3}$ is $A \rightarrow B$, then $A \rightarrow B$ is not preserved in $G_{5}$ as long as:
i. $\quad A-B$ has MMD $<\theta$. In this case, the arc is eliminated since the pairwise score between $A$ and $B$ is lower than threshold $\theta$.
ii. $\quad A$ and $B$ in $G_{3}$ share a neighbour $C$ that is not a child of $A$ and $B$. In this case, the arc is eliminated since the dependency is preserved through $C$.
iii. $\quad A$ and $B$ in $G_{3}$ share child $C$. In this case, $A \rightarrow B$ is not preserved from $G_{3}$ to $G_{5}$, and further activates the 'reversal' step. Specifically, for each $A \rightarrow B$ not preserved in $G_{5}$, if $A$ and $B$ share child $C$, then $A \rightarrow C \leftarrow B$ is reoriented into $A \rightarrow C \rightarrow B$ (or $A \leftarrow C \leftarrow B$ in the case of $A \leftarrow B$ ) as long as the graph remains acyclic and optional knowledge-based constraints are not violated.

ALGORITHM 3: Phases 4 and 5, with optional knowledge-based constraints in grey shading.
Input: variables $X$, discrepancy threshold $\theta$, graph $G_{3}$
Output: graphs $G_{4}$ and $G_{5}$
// Produce graph $G_{4}$ in phase 4, independent of $G_{3}$.
for each variable $x_{i} \in X$ do
for each remaining variable $x_{j} \in X$ do
if $x_{i}$ and $x_{j}$ are part of a directed constraint then add them in $G_{4}$ with MMD score 1
else add them in $G_{4}$ with MMD score $\left[\operatorname{MMD}\left(P\left(x_{i}\right), P\left(x_{i} \mid x_{j}\right)\right)+\operatorname{MMD}\left(P\left(x_{j}\right), P\left(x_{j} \mid x_{i}\right)\right)\right] / 2$
end if
end for
end for
// Produce graph $G_{5}$ in phase 5, dependent on $G_{3}$ and $G_{4}$.
while edge $e \in G_{4}$ do
delete $e_{i}$ in $G_{4}$ with $\min (\mathrm{MMD})$ and get nodes $A$ and $B$
if $A$ and $B$ share a neighbour $C$ in $G_{4}$ then
if there is an arc between $A$ and $B$ in $G_{3}$ then
if $e_{i}$ had MMD $<\theta$
delete arc between $A$ and $B$ in in $G_{5}$
else if $A$ and $B$ share a non-child $C$ in $G_{3}$ then
delete arc between $A$ and $B$ in in $G_{5}$
else if $A$ and $B$ share a child $C$ in $G_{3}$ then
delete arc between $A$ and $B$ in in $G_{5}$

```
    for each \(C\) do
        if the arc eliminated in \(G_{5}\) was \(A \rightarrow B\) then
            if \(A \rightarrow C \rightarrow B\) do not violate constraints then
                alter \(A \rightarrow C \leftarrow B\) to \(A \rightarrow C \rightarrow B\) if \(G_{5}\) remains acyclic
            end if
            else
                if \(A \leftarrow C \leftarrow B\) do not violate constraints then
                    alter \(A \rightarrow C \leftarrow B\) to \(A \leftarrow C \leftarrow B\) if \(G_{5}\) remains acyclic
            end if
            end if
            end for
            end if
        end if
    end if
end while
```


# 2.5 Phase 6: DAG 

The final phase ensures that the graph returned to the user is a DAG that enables full propagation of evidence. It starts by searching for the largest graphical fragment $g_{5 i}$ in $G_{5}$, and then for the variable $x_{i}$ that is not part of $g_{5 i}$ and which maximises MMD score on a variable $z_{i}$ in $g_{5 i}$. It then connects $x_{i}$ to $z_{i}$ with an arc. The direction of the arc is determined based on the number of parents in $x_{i}$ with respect to $z_{i}$; i.e., the node with the lowest number of parents is selected as the child (unless it violates any knowledge-based constraints). This process is repeated until all $x_{i}$ become part of $g_{5 i}$. Algorithm 4 describes this phase.

ALGORITHM 4: Phase 6, with optional knowledge-based constraints in grey shading.
Input: variables $X$, graph $G_{4}$, graph $G_{5}$
Output: graph $G_{6}$
// Produce graph $G_{6}$ in phase 6, dependent on $G_{4}$ and $G_{5}$.
Find the largest BN fragment $g_{5 i} \in G_{5}$ and get variables $Z$ of $g_{5 i}$.
while size of set $Z<$ size of set $X$ do
for each $x_{i} \notin Z$ do
Search for variable $z_{i}$ that maximises $s$ on a $x_{i}$
if $x_{i}$ has parents $\geq$ to the number of parents of $z_{i}$ then
if $x_{i} \rightarrow z_{i}$ does not violate constraints then
do $x_{i} \rightarrow z_{i}$
else
do $z_{i} \rightarrow x_{i}$
end if
else
if $z_{i} \rightarrow x_{i}$ does not violate constraints then
do $z_{i} \rightarrow x_{i}$
else
do $x_{i} \rightarrow z_{i}$
end if
end if
end for
end while

# 2.6 Computational and time complexity 

Previous relevant studies have based computational complexity on the number of associational tests between variables, and the number of conditional independence tests [3], [14], [32]. As described in the previous subsections, the only phases that involve associational tests are phases 1 and 4 which compute the combined causal and pairwise MMD scores respectively. The remaining phases simply make use of those MMD scores to modify the graph.

More specifically, the number of associational tests in phase 1 is $[x(x-1)(x-2)] / 2$, where $x$ is the number of variables in the data. In phase 4 , the number of associational tests is $x(x-1)$. Therefore, computational complexity is the sum of associational tests over these two phases; i.e.,

$$
o\left(\left(x(x-1)(x-2) / 2\right)+x(x-1)\right)
$$

Due to the exhaustive search performed in phase 1 , each increase in $x$ results in a non-linear cubic growth in the number of associational tests. This means that the Saiyan algorithm is not suitable for datasets that incorporate 1000s of variables, such as those in bioinformatics. Algorithms that scale linearly with the number of variables are typically more suitable for those problems.

## 3 EVALUATION AND RESULTS

The evaluation process is based on four case studies ( 10 datasets, including different sample sizes), four scoring metrics, and another ten state-of-the-art or well-established structure learning algorithms.

### 3.1 Data case studies

Two real-world and two synthetic case studies are considered. The real-world case studies represent a 'simple' and a 'complex' test, whereas the synthetic case studies represent a 'rule-based' and a 'knowledge-based' test. Specifically,
i. Football: A real-world dataset that consists of seven variables and has a sample size of 380. The data and knowledge-based BN graph are based on a simplified version of the model presented in [33]. This dataset represents the 'simple' real-world test.
ii. Forensic medicine: A real-world dataset that consists of 56 variables and has a sample size of 953. The data and knowledge-based graph are based on [34]. This dataset represents the 'complex' real-world test.
iii. Alarm network: The classic BN model that consists of 37 variables. Data are simulated based on the knowledge-based structure and parameters specified in the Bayesian Network Repository with reference to [35]. This dataset represents the 'knowledge-based' synthetic test.
iv. Property market: A rule-based BN model that consists of 27 variables and which had its structure and parameters determined by clearly defined rules and regulating protocols associated with the UK property market, as described in [36]. This dataset represents the 'rule-based' synthetic test.

It is important to note that for cases $i$ and $i i$, the algorithms are judged in terms of how well they predict the knowledge-based graph, which is not necessarily the ground truth graph. For cases iii

and $i v$, the algorithms are judged in terms of how accurately they reconstruct the hypothetical ground truth graph.

# 3.2 Evaluation metrics 

Four evaluation metrics are considered that are fully oriented towards graphical discovery. These are:
i. the classic F1 score which represents the harmonic mean of Precision and Recall; the most popular metrics used to evaluate BN structure learning algorithms in the literature [37],
ii. the Structural Hamming Distance (SHD) metric that penalises each change required to transform the discovered graph into the ground truth graph by 1 [14],
iii. the DAG Dissimilarity Metric (DDM) that penalises dissimilarities and rewards similarities between graphs, with a weighted reward for un/bi-directed edges [37],
iv. the Balanced Scoring Function (BSF) that balances the score proportional to the number of direct dependencies and independencies in the ground truth graph, by taking into consideration all of the confusion matrix parameters. A score of 0 represents performance equivalent to an empty or a fully connected graph, and scores of -1 and 1 represent the most inaccurate and accurate graphs respectively [37].

Note that, in thus study, all of the four metrics consider the discovery of a correct edge with an incorrect direction to be a partial match with a $50 \%$ reward. For example, if the true arc is $A \rightarrow B$ and an algorithm discovers $A \rightarrow B$, then the reward will be 1 ; but the reward will be 0.5 if the algorithm discovers $A \leftrightarrow B, A-B$, or $A \leftarrow B$ instead (and 0 for no edge). Finally, the evaluation process assumes that the ground truth graph is a DAG, rather than a PDAG.

### 3.3 Structure learning algorithms considered

The TETRAD freeware and the bnlearn R Statistical package [38] were used to test the other algorithms. The graphs generated by the Saiyan algorithm are compared to the graphs generated by each of the other 10 algorithms when applied to the same data. The other 10 algorithms are:
i. The PC (Peter-Clark) algorithm, which uses conditional independence tests to construct the network and is perhaps the most well-known constraint-based algorithm [39].
ii. The FCI (Fast Causal Inference) algorithm, that is similar to PC but which accounts for the possibility of latent confounders [40].
iii. The FGES (Fast Greedy Equivalence Search) algorithm which is a parallelised and an optimised version of the score-based GES algorithm that was initially developed by Meek [41] and later further developed by Chickering [12].
iv. The GS (Grow-Shrink Markov Blanket) algorithm which recovers the Markov blanket based on pairwise independence test [38].
v. The MMPC (Max-Min Parents and Children) constraint-based algorithm that uses forward selection to discover neighbours based on the maximum and minimum associations observed in subset nodes during previous iteration [42].
vi. The HC (Hill-Climbing) score-based algorithm that searches the space of directed graphs using greedy search [43].
vii. The TABU (Tabu Search) scored-based algorithm that is a modified HC version designed to escape local optima [43].

viii. The MMHC (Max-Min Hill-Climbing) hybrid algorithm, which is based on MMPC and HC algorithms, and is said to outperform several prototypical and state-of-the-art algorithms [14].
ix. The IAMB (Incremental Association) constraint-based algorithm which is a Markov blanket detection algorithm using forward selection search [44].
x. The RSMAX2 (Restricted Maximization) hybrid algorithm which is a modified version of MMHC that uses different combinations of constraint-based and score-based searches [45, 46].

The TETRAD freeware version 6.5.3 was used to run the PC, FCI, and FGES algorithms with their default parameter inputs, and the bnlearn R Statistical package v4.4 was used to run the GS, MMPC, HC, TABU, MMHC, IAMB, and RSMAX2 algorithms with their default parameter inputs [46].

# 3.4 Results and discussion 

The results are based on the four case studies discussed in Section 3.1, and on a total of 10 datasets. The 10 datasets are the result of dividing each of the two synthetic case studies into four datasets of different sample size; i.e., $0.1,1,10$, and 100 thousand samples per dataset per synthetic case.

The Saiyan algorithm is tested over different combinations of parameter input. Specifically, 42 graphs are generated for each dataset, where each of those 42 graphs represents a unique combination of the following parameters:
i. Three types of MMD score to measure the discrepancy between prior and posterior distributions; i.e. MN, MX, and MM as defined in Section 2.1.
ii. Seven different discrepancy thresholds $\theta$, which represent the threshold above which a relationship is established between variables given the MMD score, as defined in Section 2.2. The seven thresholds tested are $0.05,0.07,0.1,0.15,0.2,0.25$, and 0.3 .
iii. Two input values for constant $c(0$ or 1$)$, which modifies the maximum number of parents a node can have as defined in Section 2.3.

Since the evaluation is based on 10 datasets, a total of 100 graphs are generated by the other algorithms (one graph per dataset per algorithm), and 420 graphs are generated by the Saiyan algorithm ( 42 graphs per dataset). Therefore, the results from this evaluation illustrate how the Saiyan algorithm with unoptimised parameters (i.e., over 42 different parameter inputs) performs relative to the 10 algorithms with default parameters.

Figs 3 and 4 present the ranking of the algorithms, as determined by each of the four metrics, in terms of how well they predict the Football and Forensic medicine knowledge-based graphs. Two scores are reported for Saiyan; the best and worst scores over the 42 graphs generated per case study.

![img-2.jpeg](img-2.jpeg)

Fig. 3. Football case study: Performance of each algorithm as determined by each of the four metrics, in terms of how well they predict the knowledge-based graph. Algorithms Saiyan [b] and Saiyan [w] represent the best (highlighted in orange) and worst (highlighted in red) scores respectively, over the 42 parameter input combinations.
![img-3.jpeg](img-3.jpeg)

Fig. 4. Forensic medicine case study: Performance of each algorithm as determined by each of the four metrics, in terms of how well they predict the knowledge-based graph. Algorithms Saiyan [b] and Saiyan [w] represent the best (highlighted in orange) and worst (highlighted in red) scores respectively, over the 42 parameter input combinations.

Overall, the algorithms have done well in predicting the Football knowledge-based graph, but not well in predicting the more complex Forensic medicine graph. The same applies to the Saiyan algorithm. However, not being able to discover a graph that closely approximates the knowledgebased graph does not imply that the graph discovered is inaccurate. Still, these results suggest that the algorithms are rather consistent in the graphs they generate; at least in relation to the knowledgebased graphs.

Interestingly, while the four metrics are generally in agreement when it comes to ranking the algorithms in the Football case study, they generate conflicting rankings in the Forensic medicine ACM Transactions on Knowledge Discovery from Data, Vol. ?, No. ?, Article ?. Publication date: ? 2020.

case study. The most staggering example involves the GS algorithm; F1 and BSF metrics place GS at the bottom of the rankings whereas SHD and DDM metrics place GS at the top of the rankings. This inconsistency occurs because the GS generates a limited number of edges relative to the other algorithms (refer to Table 2). The limited number of edges is viewed positively by the SHD and DDM metrics which approximate classification accuracy and hence, tend to be biased in favour of empty graphs [37].

Similarly, Figs 5 and 6 rank the synthetic performance of the algorithms for the Property market and Alarm network case studies respectively. These graphs include the performance scores over all of the four different data sample sizes. Results of interest include:
i. The TABU algorithm has topped all of the rankings and is closely followed by the similar HC algorithm.
ii. While the Saiyan algorithm has not topped any of the rankings, its performance is competitive relative to most of the other algorithms.
iii. The F1 (Recall and Precision) and BSF metrics tend to rank the Saiyan algorithm higher than the SHD and DDM metrics.
iv. The worst performances of the Saiyan algorithm (i.e., Saiyan [b]) are often at the bottom of the rankings. This suggests that some of the parameter inputs tested, which are detailed in Appendix B, are far from being optimal and should be avoided. Tables B1, B2, and B3 suggest that the inputs 'Mean', ' 5 ', and ' 0 ' for respective parameters MMD, $\theta$, and $c$, produce scores that are considerably inferior relative to the scores generated when based on the remaining parameter inputs tested. According to Table B4, however, even when we restrict the results to the better performing parameter inputs, it is still unclear which combination of inputs maximises performance over all cases. It is possible that the optimal parameters depend on the dimensionality of the data relative to the sample size of the input data.
v. Increasing the sample size of the input data does not always improve accuracy. This observation applies to multiple algorithms, and applies to both synthetic case studies. However, in most cases the difference in scoring performance is rather marginal and may be due to random variability that arises once an algorithm is provided with enough data samples.
vi. The results are not entirely consistent with those reported in [14], in which the MMHC outperforms several prototypical algorithms according to the SHD score, including the PC, GES, and GS algorithms tested in this paper. The RSMAX2 algorithm, which is a modified version of MMHC, appears to be on par with MMHC, as expected.

Table 2 presents the number of arcs or edges discovered by each of the algorithms, as well as the number of independent graphical fragments (i.e., disjoint subgraphs) or variables generated by each of the algorithms, for each case study. Observations of interest include:
i. The other algorithms will rarely return a graph that enables full propagation of evidence, despite all of the input variables being dependent.
ii. The number of edges generated by the Saiyan algorithm appear to better approximate the knowledge-based or true number of edges. For example, in the Forensic medicine case none of the other algorithms came close to generating 103 edges. Remarkably, the GS algorithm only discovered 9 edges and yet, the SHD and DDM metrics considered GS to be the best performing algorithm (refer to Fig 4). This observation serves as further evidence that simple classification accuracy, which these metrics approximate, can be

misleading. Moreover, five of the other algorithms (GS, MMHC, IAMB, MMPC, and RSMAX2) also generated a low number of edges relative to the true number of edges, for both synthetic experiments and irrespective of sample size.
iii. In the Property market case study, the variability in the number of edges discovered is minor for the Saiyan algorithm (over its 168 graphs), whereas it is much higher for the other algorithms (over just four graphs; one per sample size). This difference is relaxed in the Alarm network case. Overall, these results suggest that Saiyan is more consistent in the number of edges discovered, which is a consequence of the assumption that all of the input variables are dependent.
iv. While the restriction to enable full propagation of evidence is expected to lead to more complex graphs, Table 2 suggests that this is often, but not always, the case. For example, in the Property market case the PC, FCI and FGES algorithms generated a much higher number of edges across all four sample size cases, compared to the Saiyan's maximum number of edges generated across all of the 168 different graphs. This observation, however, does not extend to the Alarm network case. Moreover, most of the other algorithms tend to generate simple models with limited edges when the sample size is low.

![img-4.jpeg](img-4.jpeg)

Fig. 5. Property market case study: Performance of each algorithm over different sample sizes, as determined by each of the four metrics, in terms of how well they predict the hypothetical ground truth rule-based graph. Algorithms Saiyan [b] and Saiyan [w] represent the best (highlighted in orange) and worst (highlighted in red) scores respectively, over the 42 parameter input combinations, per sample size.

![img-5.jpeg](img-5.jpeg)

Fig. 6. ALARM network case study: Performance of each algorithm over different sample sizes, as determined by each of the four metrics, in terms of how well they predict the hypothetical ground truth graph. Algorithms Saiyan [b] and Saiyan [w] represent the best (highlighted in orange) and worst (highlighted in red) scores respectively, over the 42 parameter input combinations, per sample size.

Table 2. The number of edges and independent graphical fragments (or disjoint subgraphs) discovered per algorithm per case study.


![img-6.jpeg](img-6.jpeg)

Fig. 7. Overall performance of the Saiyan algorithm (over all 42 input unoptimised combinations) relative to the overall performance of the other 10 algorithms. The bars illustrate the percentage of the Saiyan's scores being inferior, on par, and superior, relative to the respective scores generated by the other 10 algorithms.

# 4 CONCLUDING REMARKS AND FUTURE WORK 

This paper presented a BN structure learning algorithm, called Saiyan, which is based on a novel scoring function to determine relationships between variables, and follows an unconventional sixphase associational heuristic approach to generate a DAG that enables full propagation of evidence.

In guaranteeing full propagation of evidence, Saiyan 'forces' the discovery of edges that would otherwise remain undiscovered, and these additional edges are not expected to be correct at the rate of those identified unrestrictedly. The assumption that the input variables are dependent is a practical solution and not a theoretical advancement, which means that the restriction may negatively impact the evaluation scores. Moreover, Saiyan represents an associational heuristic that, in theory, is not expected to perform well relative to more sophisticated approaches, such as those based on constraint-based and score-based learning. Still, the empirical results suggest that this heuristic is as competitive as the average algorithm evaluated in this study.

The Saiyan algorithm represents an experimental implementation. Planned extensions of this research will investigate the impact of the assumption to enable full propagation of evidence on constraint-based and score-based learning. The latest version of the Saiyan algorithm, along with relevant datasets and Bayesian Network case studies, is available online [47] .

## ACKNOWLEDGMENTS

This research was supported by the ERSRC Fellowship project EP/S001646/1 on Bayesian Artificial Intelligence for Decision Making under Uncertainty, and by The Alan Turing Institute in the UK.

# APPENDIX A: SAMPLE GRAPHS GENERATED BY SAIYAN 

![img-7.jpeg](img-7.jpeg)

Fig. A.1. Sample graphs generated by the Saiyan algorithm over the different learning phases when applied to the football case study with parameters inputs MMD $=$ Mean, $\theta=0.05, c=0$. The maximum number of parents is determined to be 3 . The scores associated with each edge represent the MMD scores for the particular phase. The red dashed arcs represent arcs eliminated, and the blue dashed arcs represent arcs reversed.

# APPENDIX B: SYNTHETIC PERFORMANCE SAIYAN BASED ON DIFFERENT PARAMETER INPUTS 

Table B.1. Overall synthetic performance over parameters MMD. Worst performances are highlighted in red and best performances in yellow.


Table B.2. Overall synthetic performance over parameters $c$. Worst performances are highlighted in red and best performances in yellow.


Table B.3. Overall synthetic performance over parameters $\theta$. Worst performances are highlighted in red and best performances in yellow.


Table B.4. Detailed synthetic performance over each combination of parameters MMD, $c$, and $\theta$, excluding the combinations that led to the worst performances highlighted in Tables B1, B2, and B3. Worst performances are highlighted in red and best performances in yellow, per sample size.


ACM Transactions on Knowledge Discovery from Data, Vol. ?, No. ?, Article ?. Publication date: ? 2020.

