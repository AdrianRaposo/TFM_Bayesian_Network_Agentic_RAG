# On the optimality of solutions of the max-product belief propagation algorithm in arbitrary graphs. 

Yair Weiss and William T. Freeman


#### Abstract

Graphical models, such as Bayesian networks and Markov random fields, represent statistical dependencies of variables by a graph. The max-product "belief propagation" algorithm is a local-message passing algorithm on this graph that is known to converge to a unique fixed point when the graph is a tree. Furthermore, when the graph is a tree, the assignment based on the fixed-point yields the most probable a posteriori (MAP) values of the unobserved variables given the observed ones.

Recently, good empirical performance has been obtained by running the max-product algorithm (or the equivalent min-sum algorithm) on graphs with loops, for applications including the decoding of "turbo" codes. Except for two simple graphs (cycle codes and single loop graphs) there has been little theoretical understanding of the max-product algorithm on graphs with loops.

Here we prove a result on the fixed points of max-product on a graph with arbitrary topology and with arbitrary probability distributions (discrete or continuous valued nodes). We show that the assignment based on a fixed-point is a "neighborhood maximum" of the posterior probability: the posterior probability of the max-product assignment is guaranteed to be greater than all other assignments in a particular large region around that assignment. The region includes all assignments that differ from the max-product assignment in any subset of nodes that form no more than a single loop in the graph. In some graphs this neighborhood is exponentially large. We illustrate the analysis with examples.


keywords: Belief propagation, max-product, min-sum, Bayesian networks, Markov random fields, MAP estimate.

Problems involving probabilistic belief propagation arise in a wide variety of applications, including error correcting codes, speech recognition and image understanding. Typically, a probability distribution is assumed over a set of variables and the task is to infer the values of the unobserved variables given the observed ones. The assumed probability distribution is described using a graphical model [14] - the qualitative aspects of the distribution are specified by a graph structure. The graph may either be directed as in a Bayesian network [18], [12] or undirected as in a Markov Random Field [18], [10].

Here we focus on the problem of finding an assignment for the unobserved variables that is most probable given the observed ones. In general, this problem is NP hard [19] but if the graph is singly connected (i.e. there is only one path between any two given nodes) then there exist efficient local message-passing schemes to perform this task. Pearl [18] derived such a scheme for singly connected Bayesian networks. The algorithm, which he called "belief revision", is identical to his algorithm for finding posterior marginals over nodes except that the summation operator is replaced with a maximization. Aji et al. [2] have shown that both of Pearl's algorithms can be seen as special cases of generalized distributive laws over particular semirings. In particular, Pearl's algorithm for finding maximum a posteriori (MAP) assignments can be seen as a generalized distributive law over the max-product semiring. We will henceforth refer to it as the "max-product" algorithm.

Pearl showed that for singly connected networks, the max-product algorithm is guaranteed to converge and that the assignment based on the messages at convergence is guaranteed to give the optimal assignment-values corresponding to the MAP solution.

Several groups have recently reported excellent experimental results by running the max-product algorithm on graphs with loops [23], [6], [3], [20], [6], [11]. Benedetto et al. used the max-product algorithm to decode "turbo" codes and obtained excellent results that were slightly inferior to the original turbo decoding algorithm (which is equivalent to the sum-product algorithm). Weiss [20] compared the performance of sum-product and max-product on a "toy" turbo code problem while distinguishing between converged and unconverged cases. He found that if one considers only the convergent cases, the performance of max-product decoding is significantly better than sum-product decoding. However, the max-product algorithm converges less often so its overall performance (including both convergent and nonconvergent cases) is inferior.

Progress in the analysis of the max-product algorithm has been made for two special topologies: single loop graphs, and "cycle codes". For graphs with a single loop [23], [20], [21], [5], [2], it can be shown that the algorithm converges to a stable fixed point or a periodic oscillation. If it converges to a stable fixed-point, then the assignment based on the fixed-point messages is the optimal assignment. For graphs that correspond to cycle codes (low density parity check codes in which each bit is checked by exactly two check nodes), Wiberg [23] gave sufficient conditions for max-product to converge to the transmitted codeword and Horn [11] gave sufficient conditions for convergence to the MAP assignment.

In this paper we analyze the max-product algorithm in graphs of arbitrary topology. We show that at a fixed-point of the algorithm, the assignment is a "neighborhood maximum" of the posterior probability: the posterior probability of the max-product assignment is guaranteed to be greater than all other assignments in a particular large region around that assignment. These results motivate using this powerful algorithm in a broader class of networks.

[^0]
[^0]:    Y. Weiss is with Computer Science Division, 485 Soda Hall, UC Berkeley, Berkeley, CA 94720-1776. E-mail: yweiss@cs.berkeley.edu. Support by MURI-ARO-DAAH04-96-1-0341, MURI N00014-00-1-0637 and NSF IIS-9988642 is gratefully acknowledged.
    W. T. Freeman is with MERL, Mitsubishi Electric Research Labs., 201 Broadway, Cambridge, MA 02139. E-mail: freeman@merl.com.

![img-0.jpeg](img-0.jpeg)

Fig. 1. Any Bayesian network can be converted into an undirected graph with pairwise cliques by adding cluster nodes for all parents that share a common child. a. A Bayesian network. b. The corresponding undirected graph with pairwise cliques. A cluster node for (x2,x3) has been added. The potentials can be set so that the joint probability in the undirected graph is identical to that in the Bayesian network. In this case the update rules presented in this paper reduce to Pearl's propagation rules in the original Bayesian network [21].

# I. The max-product algorithm in pairwise Markov Random Fields 

Pearl's original algorithm was described for directed graphs, but in this paper we focus on undirected graphs. Every directed graphical model can be transformed into an undirected graphical model before doing inference (see figure 1). An undirected graphical model (or a Markov Random Field) is a graph in which the nodes represent variables and arcs represents compatibility relations between them. Assuming all probabilities are nonzero, the Hammersley-Clifford theorem (e.g. [18]) guarantees that the probability distribution will factorize into a product of functions of the maximal cliques of the graph.

Denoting by $x$ the values of all unobserved variables in the graph, the factorization has the form:

$$
P(x)=\prod_{c} \Psi_{c}\left(x_{c}\right)
$$

where $x_{c}$ is a subset of $x$ that form a clique in the graph and $\Psi_{c}$ is the potential function for the clique.
We will assume, without loss of generality, that each $x_{i}$ node has a corresponding $y_{i}$ node that is connected only to $x_{i}$.

Thus:

$$
P(x, y)=\prod_{c} \Psi_{c}\left(x_{c}\right) \prod_{i} \Psi_{i i}\left(x_{i}, y_{i}\right)
$$

The restriction that all the $y_{i}$ variables are observed and none of the $x_{i}$ variables are is just to make the notation simple - $\Psi_{i i}\left(x_{i}, y_{i}\right)$ may be independent of $y_{i}$ (equivalent to $y_{i}$ being unobserved) or $\Psi_{i i}\left(x_{i}, y_{i}\right)$ may be $\delta\left(x_{i}-x_{o}\right)$ (equivalent to $x_{i}$ being observed, with value $x_{o}$ ).

In describing and analyzing belief propagation, we assume the graphical model has been preprocessed so that all the cliques consist of pairs of units. Any graphical model can be converted into this form before doing inference through a suitable clustering of nodes into large nodes [21]. Figure 1 shows an example - a Bayesian network is converted into an MRF in which all the cliques are pairs of units.

Equation 2 becomes

$$
P(x, y)=\prod_{i, j} \Psi_{i j}\left(x_{i}, x_{j}\right) \prod_{i} \Psi_{i i}\left(x_{i}, y_{i}\right)
$$

where the first product is over connected pairs of nodes.
The important property of MRFs that we will use throughout this paper is the Markov blanket property. The probability of a subset of nodes $S$ given all other nodes in the graph $S^{C}$ depends only on the values of the nodes that

immediately neighbor $S$. Furthermore, the probability of $S$ given all other nodes is proportional to the product of all clique potentials within $S$ and all clique potentials between $S$ and its immediate neighbors.

$$
\begin{aligned}
P\left(x_{S} \mid x_{S^{C}}\right) & =P\left(x_{S} \mid N\left(x_{S}\right)\right) \\
& =\prod_{x_{i}, x_{j} \in S} \Psi_{i j}\left(x_{i}, x_{j}\right) \prod_{x_{i} \in S, x_{j} \in N(S)} \Psi_{i j}\left(x_{i}, x_{j}\right)
\end{aligned}
$$

The advantage of preprocessing the graph into one with pairwise cliques is that the description and the analysis of belief propagation becomes simpler. For completeness, we review the belief propagation scheme used in [21]. As we discuss in the appendix, this belief propagation scheme is equivalent to Pearl's belief propagation algorithm in directed graphs, the Generalized Distributive Law algorithm of [1] and the factor graph propagation algorithm of [13]. These three algorithms correspond to the algorithm presented here with a particular way of preprocessing the graph in order to obtain pairwise potentials.

At every iteration, each node sends a (different) message to each of its neighbors and receives a message from each neighbor. Let $x_{i}$ and $x_{j}$ be two neighboring nodes in the graph. We denote by $m_{i j}\left(x_{j}\right)$ the message that node $x_{i}$ sends to node $x_{j}$, by $m_{i i}\left(x_{i}\right)$ the message that $y_{i}$ sends to $x_{i}$, and by $b_{i}\left(x_{i}\right)$ the belief at node $x_{i}$.

The max-product update rules are:

$$
\begin{aligned}
m_{i j}\left(x_{j}\right) & \leftarrow \alpha \max _{x_{i}} \Psi_{i j}\left(x_{i}, x_{j}\right) m_{i i}\left(x_{i}\right) \prod_{x_{k} \in N\left(x_{i}\right) \backslash x_{j}} m_{k i}\left(x_{i}\right) \\
b_{i}\left(x_{i}\right) & \leftarrow \alpha m_{i i}\left(x_{i}\right) \prod_{x_{k} \in N\left(x_{i}\right)} m_{k i}\left(x_{i}\right)
\end{aligned}
$$

where $\alpha$ denotes a normalization constant and $N\left(x_{i}\right) \backslash x_{j}$ means all nodes neighboring $x_{i}$, except $x_{j}$.
The procedure is initialized with all message vectors set to constant functions. Observed nodes do not receive messages and they always transmit the same vector- if $y_{i}$ is observed to have value $y^{*}$ then $m_{i i}\left(x_{i}\right)=\Psi_{i i}\left(x_{i}, y^{*}\right)$. The normalization of $m_{i j}$ in equation 6 is not necessary-whether or not the message are normalized, the belief $b_{i}$ will be identical. However, normalizing the messages avoids numerical underflow and adds to the stability of the algorithm. We assume throughout this paper that all nodes simultaneously update their messages in parallel.

For singly connected graphs it is easy to show that:

- The algorithm converges to a unique fixed point regardless of initial conditions in a finite number of iterations.
- At convergence, the belief for any value $x_{i}$ of a node $i$ is the maximum of the posterior, conditioned on that node having the value $x_{i}: b_{i}\left(x_{i}\right)=\alpha \max _{x} P\left(x \mid y, x_{i}\right)$.
- Define the max-product assignment, $x^{*}$ by $x_{i}^{*}=\arg \max _{x_{i}} b_{i}\left(x_{i}\right)$ (assuming a unique maximizing value exists). Then $x^{*}$ is the MAP assignment.
The max product assignment assumes there are no "ties" - that a unique maximizing $x_{i}$ exists for all $b\left(x_{i}\right)$. Ties can arise when the MAP assignment is not unique, e.g. when there are two assignments that have identical posterior and both maximize the posterior. For singly connected graphs, the converse is also true: if there are no ties in $b\left(x_{i}\right)$ then the MAP assignment is unique. In what follows, we assume a unique MAP assignment.

In particular applications, it might be easier to work in the log domain so that the product operation in equations 7 is replaced by a sum operations. Thus the max-product algorithm is sometimes referred to as the max-sum algorithm or the min-sum algorithm [23], [5]. If the graph is a chain, the max-product is a two-way version of the Viterbi algorithm in Hidden Markov Models and is closely related to concurrent dynamic programming [4]. Despite this connection to well studied algorithms, there has been very little analytical success in characterizing the solutions of the max-product algorithm on arbitrary graphs with loops.

# II. What are the fixed points of the max-product algorithm? 

Each iteration of the max-product algorithm can be thought of as an operator $F$ that inputs a list of messages $m^{(t)}$ and outputs a list of messages $m^{(t+1)}=F m^{(t)}$. Thus running belief propagation can be thought of as an iterative way of finding a solution to the fixed point equations $F m=m$ with an initial guess $m^{(0)}$ in which all messages are constant functions.

Note that this is not the only way of finding fixed-points. Murphy et al. [17] describe an alternative method for finding fixed-points of $F$. They suggested iterating:

$$
m^{(t+1)}=F\left(\alpha m^{(t)}+(1-\alpha) m^{(t-1)}\right)
$$

![img-1.jpeg](img-1.jpeg)

Fig. 2. a. A 25x25 grid of points. b.-c. Examples of subsets of nodes that form no more than a single loop. In this paper we prove that changing such a subset of nodes from the max-product assignment will always decrease the posterior probability

Here again, if iterations of equation 8 converge to $m^{*}$ then $m^{*}$ satisfies $m^{*}=F m^{*}$.

The equation $m^{*}=F m^{*}$ is a highly nonlinear equation and it is not obvious how many solutions exist or how to characterize them. Horn [11] showed that in single-loop graphs, $F$ can be considered as matrix multiplication over the max-product semiring and fixed points correspond to eigenvectors of that matrix. Thus even in single loop graphs, one can construct examples with any number of fixed points.

The main result of this paper is a characterization of how well the max-product assignment approximates the MAP assignment. We show that the assignment $x^{*}$ must be a neighborhood maximum of $P(x|y)$ : that is $P(x^{*}|y)>P(x|y)$ for all $x$ in a particular large region around $x^{*}$. This condition is weaker than a global maximum but stronger than a local maximum.

To be more precise we define the Single Loops and Trees (SLT) neighborhood of an assignment $x^{*}$ in a graphical model $G$ to include all assignments $x$ that can be obtained from $x^{*}$ by:

- Choosing an arbitrary subset $S$ of nodes in $G$ that consists of disconnected combinations of trees and single loops.
- Assigning arbitrary values to $x_{S}$ — the chosen subset of nodes. The other nodes have the same assignment as in $x^{*}$.

**Claim 1:** For an arbitrary graphical model with arbitrary potentials, if $m^{*}$ is a fixed-point of the max-product algorithm and $x^{*}$ is the assignment based on $m^{*}$ then $P(x^{*}|y)>P(x|y)$ for all $x \neq x^{*}$ in the SLT neighborhood of $x^{*}$.

Figure 2 illustrates example configurations within the SLT neighborhood of the max-product assignment. It shows examples of subsets of nodes that could be changed to arbitrary values and the posterior probability of the assignment is guaranteed to be worse than that of the max-product assignment.

To build intuition, we first describe the proof for a specific case, the diamond graph of figure 3. The general proof is given in section II-B.

### A. Specific Example

We start by giving an overview of the proof for the diamond graph shown in figure 3a. The proof is based on the unwrapped tree — the graphical model that the loopy belief propagation is solving exactly when applying the belief propagation rules in a loopy network [9], [23], [21], [22]. In error-correcting codes, the unwrapped tree is referred to as the "computation tree" — it is based on the idea that the computation of a message sent by a node at time $t$ depends on messages it received from its neighbors at time $t-1$ and those messages depend on the messages the neighbors received at time $t-2$ etc.

Figure 3 shows an unwrapped tree around node $x_1$ for the diamond shaped graph on the left. Each node has a shaded observed node attached to it that is not shown for simplicity.

To simplify notation, we assume that $x^{*}$, the assignment based on a fixed-point of the max-product algorithm is equal to zero, $x^{*}=0$. The periodic assignment lemma from [22] guarantees that we can modify $\hat{\Psi}_{ii}(x_i, y_i)$ for the leaf nodes so that the optimal assignment in the unwrapped tree is all zeros

$$P(\hat{x} = 0|\hat{y}) = \max_{\hat{x}} P(\hat{x}|\hat{y}) \tag{9}$$

(The $\hat{\Psi}_{ii}(x_i, y_i)$ are modified to include the messages from the nodes to be added at the next stage of the unwrapping).

![img-2.jpeg](img-2.jpeg)

Fig. 3. a: A Markov Random Field with multiple loops. b: The unwrapped graph corresponding to this structure. The unwrapped graphs are constructed by replicating the potentials $\Psi\left(x_{i}, x_{j}\right)$ and observations $y_{i}$ while preserving the local connectivity of the loopy graph. They are constructed so that the messages received by node $x_{1}$ after $t$ iterations in the loopy graph are equivalent to those that would be received by $x_{1}$ in the unwrapped graph. An observed node, $y_{i}$, not shown, is connected to each depicted node.

We now show that the global optimality of $\tilde{x}=0$ and the method of construction of the unwrapped tree guarantee that $P(x=0 \mid y)>P(x \mid y)$ for all $x$ in the SLT neighborhood of 0 .

Referring to figure 3a, suppose that $P(x=10000 \mid y)>P(x=00000 \mid y)$. By the Markov property of the diamond figure, this means that:

$$
P\left(x_{1}=1 \mid x_{2-4}=0\right)>P\left(x_{1}=0 \mid x_{2-4}=0\right)
$$

Note that node $\tilde{x}_{1}$ has exactly the same neighbors in the unwrapped graph as $x_{1}$ has in the loopy graph. Furthermore, by the method of construction, the potentials between $x_{1}$ and each of its neighbors is the same as the potentials between $\tilde{x}_{1}$ and its neighbors. Thus equation 10 implies that:

$$
P\left(\tilde{x}_{1}=1 \mid \tilde{x}_{2-4}=0\right)>P\left(\tilde{x}_{1}=0 \mid \tilde{x}_{2-4}=0\right)
$$

in contradiction to equation 9 . Thus no change of a single $x_{i}$ can improve the posterior probability.
What about changing two $x_{i}$ at a time? If we change a pair that is not connected in the graph, say $x_{1}$ and $x_{5}$, then by the Markov property this is equivalent to changing one at a time. Thus suppose $P(10001)>P(0000)$ this again implies that $P\left(x_{1}=1 \mid x_{2-4}=0\right)>P\left(x_{1}=0 \mid x_{2-4}=0\right)$ and we have shown earlier that leads to a contradiction. Thus no change of assignment in two unconnected nodes can improve the posterior probability.

If the two are connected, say $x_{1}, x_{2}$ then the same argument holds with respect to the pair of nodes $x_{1}, x_{2}$. Note that the subgraph $\tilde{x}_{1-2}$ is isomorphic to the subgraph $x_{1-2}$ and the two subgraphs have the same neighbors. Hence:

$$
P\left(x_{1-2}=1 \mid x_{3-5}=0\right)>P\left(x_{1-2}=0 \mid x_{3-5}=0\right)
$$

implies that:

$$
P\left(\tilde{x}_{1-2}=1 \mid \tilde{x}_{3-5}=0\right)>P\left(\tilde{x}_{1-2}=0 \mid \tilde{x}_{3-5}=0\right)
$$

and this is again in contradiction to equation 9. Thus no change of assignment in two connected nodes can improve the posterior probability.

Similar arguments show that no change of assignment in any subtree of the graph can improve the posterior probability (e.g. changing the values of $x_{1-4}$ or changing the values of $x_{1-2}$ and $x_{4-5}$ ).

These arguments no longer hold, however, when we change a subset of nodes that form a loopy subgraph of $G$. For example, the subgraph $x_{1}, x_{2}, x_{3}, x_{5}$ is not isomorphic to the subgraph $\tilde{x}_{1}, \tilde{x}_{2}, \tilde{x}_{3}, \tilde{x}_{5}$. Indeed since the unwrapped tree is a tree, it cannot have a loopy subgraph. Hence we cannot equate the probabilities of the two subgraphs given their neighbors.

If the subset forms a single loop, however, then there exists an arbitrarily long chain in the unwrapped tree that corresponds to the unwrapping of that loop. For example, note the chain $\tilde{x}_{1}, \tilde{x}_{2}, \tilde{x}_{5}, \tilde{x^{\prime}}_{3}, \cdots$ in figure 3b. Using a similar argument to that used in proving optimality of max-product in a single loop graph [23], [20], [2], [5] we can show that if we can improve the posterior in the loopy graph by changing the value of $x_{1}, x_{2}, x_{3}, x_{5}$ then we can also improve the posterior in the unwrapped graph by changing the values of the arbitrarily long chain. This again leads to a contradiction.

# B. Proof of Claim 1: 

We denote by $G$ the original graph and by $\tilde{G}$ the unwrapped graph. We use $x_{i}$ for nodes in the original graph and $\tilde{x}_{i}$ for nodes in the unwrapped graph. We define a mapping $C$ from nodes in $\tilde{G}$ to nodes in $G$. This mapping will say for each node in $\tilde{G}$ what is the corresponding node in $G: C\left(\tilde{x}_{1}\right)=x_{1}$.

The unwrapped tree is therefore a graph $\tilde{G}$ and a correspondence map. We now give the method of constructing both.
Pick an arbitrary node in $G$, say $x_{1}$. Set $C\left(\tilde{x}_{1}\right)=x_{1}$. Iterate $t$ times.

- Find all leaves of $\tilde{G}$ (start with the root).
- For each leaf $\tilde{x}_{i}$ find all $k$ nodes in $G$ that neighbor $C\left(\tilde{x}_{i}\right)$.
- Add $k-1$ nodes as children to $x_{i}$, corresponding to all neighbors of $C\left(\tilde{x}_{i}\right)$ except $C\left(\tilde{x}_{j}\right)$, where $\tilde{x}_{j}$ is the parent of $\tilde{x}_{i}$.
The potential matrices and observations for each node in the unwrapped network are copied from the corresponding nodes in the loopy graph. That is, if $x_{j}=C\left(\tilde{x_{i}}\right)$ then $\tilde{y}_{i}=y_{j}$, and:

$$
\hat{\Psi}\left(\tilde{x}_{i}, \tilde{x}_{j}\right)=\Psi\left(C\left(\tilde{x_{i}}\right), C\left(\tilde{x_{j}}\right)\right)
$$

Note that the unwrapped tree around $x_{i}$ after $t_{1}$ iterations is a subtree of the unwrapped tree around $x_{j}$ after $t_{2}>t_{1}$ iterations. If we let the number of iterations $t \rightarrow \infty$ then the unwrapped tree $\tilde{G}$ becomes a well-studied object in topology: the universal covering of $G$ [16]. Roughly speaking, it is a topology that preserves the local topology of the graph $G$ but is singly connected. It is precisely this fact, that max-product gives the global optimum on a graph that has the same local topology as $G$, that makes sure that $x^{*}$ is a neighborhood maximum of $P(x \mid y)$.

We now state some properties of $\tilde{G}$.

1. Equal neighbors property: Every non-leaf node in $\tilde{G}$ has the same number of neighbors as the corresponding node in $G$ and the neighbors are in one-to-one correspondence. If $C\left(\tilde{x}_{i}\right)=x_{i}$ then for each $\tilde{x}_{j} \in N\left(\tilde{x}_{i}\right), C\left(\tilde{x}_{j}\right) \in N\left(x_{i}\right)$ and for each $x_{j} \in N\left(x_{i}\right)$ there exists $\tilde{x}_{k} \in N\left(\tilde{x}_{j}\right)$ such that $C\left(\tilde{x}_{k}\right)=x_{j}$. This follows directly from the method of constructing $\tilde{G}$.
2. Equal conditional probability property: The probability of a nonleaf node $\tilde{x}_{j}$ given its neighbors in $\tilde{G}$ is equal to the probability of $C\left(\tilde{x}_{j}\right)$ given its neighbors. Formally, if $C\left(\tilde{x}_{j}\right)=x_{i}$ then

$$
P\left(\tilde{x}_{j} \mid N\left(\tilde{x}_{j}\right)=z, y\right)=P\left(x_{i} \mid N\left(x_{i}\right)=z, y\right)
$$

This follows from the Markov blanket property of MRFs (eq. 5) and the equal neighborhood property.
3. Isomoprhic subtree property: For any subtree $T \subset G$ then for sufficiently large unwrapping count $t$ there exists an isomorphic subtree $\tilde{T} \subset \tilde{G}$. The nodes of the subtrees are in one-to-one correspondence: for each $x_{i} \in T$ there exists a $\tilde{x}_{i} \in \tilde{T}$ such that $C\left(\tilde{x}_{i}\right)=x_{i}$ and for each $\tilde{x}_{j} \in \tilde{T}, C\left(\tilde{x}_{j}\right) \in T$. To prove this we pick the root node of $T, x_{i}$ as the initial node around which to expand the unwrapped tree. By the method of construction, the unwrapped tree after a number of iterations equal to the depth of $T$ will be isomoprhic to $T$ and in one-to-one correspondence. This gives us $\tilde{T}$. For any other choice of initial node for $\tilde{G}$, the unwrapped tree starting with $x_{i}$ is a subtree of $\tilde{G}$.
4. Infinite chain property: For any loop $L \subset G$ there exists an arbitrarily long chain $\tilde{L} \subset \tilde{G}$ that is the unwrapping of $L$. Furthermore, if we denote by $n$ the length of the chain divided by the length of the loop and by $\tilde{x}_{1}$ and $\tilde{x}_{N}$ the two endpoints of the chain then:

$$
P\left(\tilde{x}_{\tilde{L}} \mid N\left(\tilde{x}_{\tilde{L}}\right)\right)=P\left(x_{L} \mid N\left(X_{L}\right)\right)^{n} \beta
$$

with $\beta$ the "boundary potentials"

$$
\beta=\prod_{\tilde{x}_{i} \in N\left(\tilde{x}_{1}\right) \backslash \tilde{x}_{2}} \hat{\Psi}\left(\tilde{x}_{i}, \tilde{x}_{1}\right) \prod_{\tilde{x}_{i} \in N\left(\tilde{x}_{N}\right) \backslash \tilde{x}_{N-1}} \hat{\Psi}\left(\tilde{x}_{i}, \tilde{x}_{N}\right)
$$

Note that $\beta$ is independent of $n . x_{L}$ and $\tilde{x}_{\tilde{L}}$ refer to all node variables in the sets $L$ and $\tilde{L}$, respectively.
The existence of the arbitrarily long chain follows from the equal neighbor property, while equation 16 follows from the Markov blanket property for MRFs (equation 5).

Another property of the unwrapped tree that we will need was proven in [22]:
5. Periodic assignment lemma: Let $m^{*}$ be a fixed-point of the max-product algorithm and $x^{*}$ the max-product assignment in $G$. Let $\tilde{G}$ be the unwrapped tree. Suppose we modify the observation potentials $\hat{\Psi}_{i i}$ at the leaf nodes to include the messages from the nodes to be added at the next stage of unwrapping. Then the MAP assignment $\tilde{x}^{*}$ in $\tilde{G}$ is a replication of $x^{*}$ : if $x_{i}=C\left(\tilde{x}_{j}\right)$ then $\tilde{x}_{j}^{*}=x_{i}^{*}$.

Using these properties, we can prove the main claim. To simplify notation, we again assume that $x^{*}$, the assignment based on a fixed-point of the max-product algorithm is equal to zero, $x^{*}=0$. The periodic assignment property guarantees that we can modify $\hat{\Psi}_{i i}\left(x_{i}, y_{i}\right)$ for the leaf nodes so that the optimal assignment in the unwrapped tree is all zeros

$$
P(\tilde{x}=0 \mid \tilde{y})=\max _{\tilde{x}} P(\tilde{x} \mid \tilde{y})
$$

Now, assume that we can choose a subtree of $T \subset G$ and change the assignment of these nodes $x_{T}$ to another value and increase the posterior. Again, to simplify notation assume that maximizing value is $x_{T}=1$. By the Markov property, this means that:

$$
P\left(x_{T}=1 \mid N\left(x_{T}\right)=0, y\right)>P\left(x_{T}=0 \mid N\left(x_{T}\right)=0, y\right)
$$

Now, by the isomorphic subtree property we know that there exists $\tilde{T} \subset \tilde{G}$ that is isomorphic to $T$. We also know that $\tilde{T}$ has the same conditional probability given its neighbors as $T$ does. Thus equation 19 implies that:

$$
P\left(\tilde{x}_{\tilde{T}}=1 \mid N\left(\tilde{x}_{\tilde{T}}\right)=0, \tilde{y}\right)>P\left(\tilde{x}_{\tilde{T}}=0 \mid N\left(\tilde{x}_{\tilde{T}}\right)=0, \tilde{y}\right)
$$

in contradiction to equation 18. Hence changing the value of a subtree from the converged values of the max-product algorithm cannot increase the posterior probability.

Now, assume we change the value of a single loop $L \subset G$ and increase the posterior probability. This means that:

$$
P\left(x_{L}=1 \mid N\left(x_{L}\right)=0, y\right)>P\left(x_{L}=0 \mid N\left(x_{L}\right)=0, y\right)
$$

By the infinite chain property, we know that for arbitrarily large $n$ :

$$
P\left(\tilde{x}_{\tilde{L}}=1 \mid N\left(\tilde{x}_{\tilde{L}}\right)=0\right)=P\left(x_{L}=1 \mid N\left(x_{L}\right)=0\right)^{n} \beta_{1}
$$

Therefore equation 21 implies that:

$$
P\left(\tilde{x}_{\tilde{L}}=1 \mid N\left(\tilde{x}_{\tilde{L}}\right)=0\right)>P\left(\tilde{x}_{\tilde{L}}=0 \mid N\left(\tilde{x}_{\tilde{L}}\right)=0\right)
$$

in contradiction to the optimality of $\tilde{x}^{*}=0$. Hence changing the value of a single loop cannot improve the posterior probability over $x^{*}$.

Now we take two disconnected components $C_{1}, C_{2} \in G$ and assume that changing the values of $x_{C_{1}}, x_{C_{2}}$ improves the posterior probability. Again, by the Markov property:

$$
\begin{gathered}
P\left(x_{C_{1}}=1, x_{C_{2}}=1 \mid N\left(x_{C_{1}}, x_{C_{2}}\right)=0, y\right)> \\
P\left(x_{C_{1}}=0, x_{C_{2}}=0 \mid N\left(x_{C_{1}}, x_{C_{2}}\right)=0, y\right)
\end{gathered}
$$

but since $C_{1}$ and $C_{2}$ are not connected this implies:

$$
\begin{gathered}
P\left(x_{C_{1}}=1 \mid N\left(x_{C_{1}}\right)=0, y\right) P\left(x_{C_{2}}=1 \mid N\left(x_{C_{2}}\right)=0, y\right)> \\
P\left(x_{C_{1}}=0 \mid N\left(x_{C_{1}}\right)=0, y\right) P\left(x_{C_{2}}=0 \mid N\left(x_{C_{2}}\right)=0, y\right)
\end{gathered}
$$

Which implies that either

$$
P\left(x_{C_{1}}=1 \mid N\left(x_{C_{1}}=0\right), y\right)>P\left(x_{C_{1}}=0 \mid N\left(x_{C_{1}}=0\right), y\right)
$$

or:

$$
P\left(x_{C_{2}}=1 \mid N\left(x_{C_{2}}=0\right), y\right)>P\left(x_{C_{2}}=0 \mid N\left(x_{C_{2}}=0\right), y\right)
$$

Thus if $C_{1}$ or $C_{2}$ are either a tree or a single loop this leads to a contradiction. Hence we cannot simultaneously change the values of two subtrees or of a subtree and a loop or of two disconnected loops and increase the posterior probability. Similarly, we can show that changing the value of any finite number of disconnected trees or single loops will not increase the posterior. This proves claim 1.

# III. Examples 

Claim 1 holds for arbitrary topologies and arbitrary potentials (both discrete and continuous nodes). We illustrate the implications of claim 1 for specific networks.

## A. Gaussian graphical models

A Gaussian graphical model is one in which the joint distribution over $x$ is Gaussian. Weiss and Freeman [22] have analyzed belief propagation on such graphs. One of the results given there can also be proved using our claim 1.

Corollary 1: For a Gaussian graphical model of arbitrary topology. If belief propagation converges, then the posterior marginal means calculated using belief-propagation are exact.

Proof: For Gaussians, max-product and sum-product are identical. The posterior means calculated by belief propagation are therefore identical to the max-product assignment. By claim 1, we know that this must be a neighborhood maximum of the posterior probability. But Gaussians are unimodal hence it must be a global maximum of the posterior probability. Thus the max-product assignment must equal the MAP assignment, and the posterior means calculated using belief propagation are exact.

![img-3.jpeg](img-3.jpeg)

Fig. 4. Turbo code structure

![img-4.jpeg](img-4.jpeg)

Fig. 5. Results of small turbo-code simulation. (a) Percent correct decodings for max-product algorithm, compared with greedy gradient ascent in the posterior probability. (b) Comparison of convergence results of the two algorithms.

### B. Turbo-codes

Figure 4 shows the pairwise Markov network corresponding to the decoding of a turbo code with 7 unknown bits. The top and bottom nodes represent the two transmitted messages (one for each constituent code). Thus in this example, the top and bottom nodes can take on 128 possible values. The potentials between the message nodes and their observations give the posterior probability of the transmitted word given one message, and the potentials between the message nodes and the bit nodes impose consistency. For example $\Psi(\text{bit}_1, \text{message}_1) = 1$ if the first bit of message_1 is equal to bit_1 and zero otherwise. It is easy to show [21] that sum-product belief propagation on this graph gives the turbo decoding algorithm and max-product belief propagation gives the modified turbo decoding algorithm of [3].

Corollary 2: For a turbo code with arbitrary constituent codes. Let $x^*$ be a fixed-point max-product decoding. Then $P(x^*)|y > P(x|y)$ for all $x$ within Hamming distance 2 of $x^*$.

Proof: This follows from the main claim. Note that whenever we change any bits in the graph we also have to change the two message nodes so changing more than two bits will give two loops.

An obvious consequence of corollary 2 is that for a turbo code with arbitrary constituent codes, the max-product decoding is either the MAP decoding or at least Hamming distance 3 from the MAP decoding. In other words, the max-product algorithm cannot converge to a decoding that is "almost" right: if it is wrong it must be wrong in at least three bits. In order for max-product to converge to a wrong decoding, there must exist a decoding that is at least distance 3 from the MAP decoding, and that decoding must have higher posterior probability than anything in its neighborhood. If no such wrong decoding exists, the max-product algorithm must either converge to the MAP decoding or fail to converge to a fixed-point.

This behavior can be contrasted with the behavior of "greedy" iterative decoding which increases the posterior probability of the decoding at every iteration. Greedy iterative decoding checks all bits and compares the posterior probability with the current value of that bit versus flipping that bit. If the posterior probability improved with flipping, the algorithm flips it (this is equivalent to free energy decoding [15] at zero temperature). This greedy decoding algorithm is guaranteed to converge to a local maximum of the posterior probability.

To illustrate these properties we ran the following simulations. We simulated transmitting turbo-encoded codewords of length 7 bits over a Gaussian channel. We compared the max-product decoding and the greedy decoding to the MAP decoding (since we were dealing with such short block lengths we could calculate the MAP decoding using exhaustive search). We varied the noise $\sigma$ of the Gaussian channel.

Figure 5 shows the results. Figure 5a shows the probability of convergence for both algorithms. Convergence was determined numerically for both algorithms: if the standard deviation of the messages over 10 successive iterations was less than 10^-5 we declared convergence. If this criterion was not achieved in 100 iterations, we called that run a failure to converge.

Figure 5 b shows the probability of a correct decoding (i.e. a decoding equal to the MAP decoding) for the two algorithms on the cases for which both converged. When max-product converges, it always finds the MAP decoding. In contrast, greedy decoding very frequently converges to a wrong decoding.

# C. $2 D$ grids 

Figure 2 (a) shows a two dimensional grid. For two dimensional grids, it is easy to show the following corollaries:
Corollary 3: For two dimensional grids of arbitrary size and arbitrary potentials. Any configuration is either (1) in the SLT region of the max-product assignment or (2) in the SLT region of an assignment that is in the SLT region of the max-product assignment.

Corollary 4: For two dimensional grids of size $n$. The size of the SLT neighborhood increases exponentially with $n$.
Both corollaries follow from the fact that we can change the value of all the even (or odd) rows to an arbitrary value.
We compared greedy decoding to max-product decoding on the $3 x 3$ grid. Max-product found the MAP decoding in $99 \%$ of the runs and when it was wrong, its assignment was always the second best. In comparison, greedy decoding found the MAP assignment only on $44 \%$ of the runs and the ranking was anywhere between 4 and 61.

## IV. Discussion

The idea of using the computation tree to prove properties of the max-product assignment was also used in [23], [20], [8], [11]. The main tool in those analyses was the fact that the max-product assignment was the global optimum in the unwrapped tree. There are two problems with generalizing this approach to arbitrary topologies.

First, the global optimum depends on the numerosity of node replicas in the unwrapped tree. That is, different nodes in $G$ may have different number of replicas in $\bar{G}$. This leads to a distinction between balanced (or nonskewed) graphs [20], [8] and unbalanced (or skewed) graphs. Balanced graphs are those for which all nodes in $G$ have asymptotically the same number of replicas in $\bar{G}$. For unbalanced graphs, it is much more difficult to relate global optimality in $\bar{G}$ to optimality in $G$.

Second, the global optimum in the unwrapped tree contains contributions from the interior nodes (that have exactly the same neighbors in $\bar{G}$ as do their corresponding nodes in $G$ ) and contributions from the leaf nodes (that are missing some of the neighbors in $\bar{G}$ ). Unfortunately, for most graphs $G$ the number of leaf nodes grows at the same rate as the non-leaf nodes and cannot be neglected from the analysis.

In this analysis, on the other hand, we used primarily the local properties of the computation tree. No matter what the topology of $G$ is, it is always the case that the local structure of $\bar{G}$ is the same as the local structure of $G$. Thus the numerosity of the nodes in $\bar{G}$ and the ratio of leaf nodes to non-leaf nodes is irrelevant. In this way, we can analyze the max-product assignment in arbitrary topologies.

Although we exploited the local properties, we would like to extend our analysis using the global properties as well. Our simulation results indicate that the max-product assignment is better than our analytical results guarantee. For example, in the turbo code simulations we found that the posterior probability often contained two SLT maxima but for all these cases, max-product found the global maximum (and not the second SLT maximum). In current work, we are looking into using the global properties of the computation tree to extend our analysis.

## APPENDIX

## RELATIONSHIP BETWEEN BELIEF PROPAGATION SCHEMES

## A. Converting a factor graph to a pairwise Markov graph

A factor graph [7] is a bipartite graph with function nodes $f_{i}$ denoted by filled squares and variable nodes $x_{i}$ denoted by unfilled circles. The function nodes denote a decomposition of a "global" function $g(x)$ into a product of "local" functions $f_{i}(x)$. We will assume that $g$ represents a joint distribution over the variable nodes. The method of converting a factor graph into a pairwise Markov graph is to remove the function nodes. Specifically:

- find all $f_{i}$ of degree 2 . For each such $f_{i}$ remove it from the graph and directly connect the two variables nodes that were connected to those function nodes. That is, if $f_{1}$ is a degree 2 node connected to $x_{1}, x_{2}$ we directly connect $x_{1}$ and $x_{2}$ and set $\Psi\left(x_{1}, x_{2}\right)=f\left(x_{1}, x_{2}\right)$.
- for all $f_{i}$ of degree $d>2$, replace the node $f_{i}$ with a new variable node $x_{N+i}$. The variable node $x_{N+i}$ represents the joint configuration of all the $x_{i}$ that were connected to $f_{i}$. That is if $f_{2}$ is connected to $x_{2}, x_{3}, x_{4}$ then the new variable $x_{6}$ is a vector with three components $x_{5}=\left(x_{2}^{\prime}, x_{3}^{\prime}, x_{4}^{\prime}\right)$. Set the potentials $\Psi\left(x_{N+i}, x_{j}\right)=\delta\left(x_{j}-x_{j}^{\prime}\right)$. Finally, add an observation node $y_{N+i}$ and set $\Psi\left(x_{N+i}, y_{N+i}\right)=f_{i}(x)$.
It is easy to show that (1) The joint distribution over the variables $x_{1} \cdots x_{N}$ in the pairwise Markov graph is exactly $f(x)$ and (2) the belief propagation algorithm in the pairwise Markov graph is equivalent to the belief propagation algorithm in [7].

![img-5.jpeg](img-5.jpeg)

Fig. 6. Any factor graph can be converted into a Markov random field with pairwise potentials that represents exactly the same probability distribution over variables. When this conversion is done, the belief propagation algorithm for the pairwise Markov graph is equivalent to the belief propagation algorithm on the factor graph.

# B. Converting a junction graph to a pairwise Markov graph 

A junction graph [1] is a graph in which vertices $s_{i}$ represent "local domains" of a global function. Thus if $g\left(x_{1}, x_{2}, x_{3}\right)$ factorizes so that:

$$
g\left(x_{1}, x_{2}, x_{3}\right)=f_{1}\left(x_{1}, x_{2}\right) f_{2}\left(x_{2}, x_{3}\right)
$$

then the two local domains are $s_{1}=\left(x_{1}, x_{2}\right)$ and $s_{2}=\left(x_{2}, x_{3}\right)$. Edges between these vertices correspond to "communication links" in a message passing scheme for calculating marginals of $g$.

Aji et al. showed that for such a message passing algorithm to exist, the junction graph must possess the "running intersection property" - the subset of nodes whose domains include $x_{i}$ together with the edges containing these nodes must form a connected graph. We now show that junction graphs are equivalent to pairwise Markov graphs.

To show this we leave the graph between $s_{i}$ unchanged and add "observation" nodes $y_{i}$ such that $\Psi\left(s_{i}, y_{i}\right)=f\left(s_{i}\right)$. We set $\Psi\left(s_{i}, s_{j}\right)=1$ if the two nodes agree on the value of any $x_{i}$ that exists in both domains and zero otherwise. Note that the running intersection property guarantees that any two nodes (not necessarily neighboring) must agree on the value of a common $x_{i}$ for the joint distribution to be nonzero. When the potentials are set in this way, it is easy to see that the joint distribution over $x$ in the pairwise Markov graph is exactly $g(x)$ and that the belief propagation algorithm in the Markov graph is equivalent to the GDL algorithm in [1].

# I. BIOGRAPHIES OF THE AUTHORS 

## A. Yair Weiss

Yair Weiss is a postdoctoral scientist at the UC Berkeley department of Electrical Engineering and Computer Science. He received his PhD from MIT in 1998 where he worked with Ted Adelson on Bayesian models for vision. His research interests include human and machine vision, probabilistic inference and learning, and neural computation.

## B. William T. Freeman

William T. Freeman is a Senior Research Scientist at MERL, Mitsubishi Electric Research Labs. He studied computer vision for his PhD in 1992 from the Massachussetts Institute of Technology, and received a BS in physics and MS in electrical engineering from Stanford in 1979, and an MS in applied physics from Cornell in 1981.

His current research interests include machine learning applied to computer vision, Bayesian models of visual perception, and interactive applications of computer vision. In 1997, he received the Outstanding Paper prize at the Conference on Computer Vision and Pattern Recognition for work on applying bilinear models to "separating style and content".

From 1981 - 1987, Dr. Freeman worked in electronic imaging at the the Polaroid Corporation, developing algorithms for color image reconstruction used in Polaroid's digital camera. In 1987-88, was a Foreign Expert at the Taiyuan University of Technology, P. R. China. Dr. Freeman is an Associate Editor of IEEE-PAMI.