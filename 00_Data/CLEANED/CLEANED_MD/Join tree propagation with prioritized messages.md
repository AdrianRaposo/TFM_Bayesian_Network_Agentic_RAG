# Join Tree Propagation with Prioritized Messages 

C. J. Butz, S. Hua, K. Konkel, and H. Yao<br>Department of Computer Science, University of Regina, Regina, Canada S4S 0A2


#### Abstract

Current join tree propagation algorithms treat all propagated messages as being of equal importance. On the contrary, it is often the case in real-world Bayesian networks that only some of the messages propagated from one join tree node to another are relevant to subsequent message construction at the receiving node. In this article, we propose the first join tree propagation algorithm that identifies and constructs the relevant messages first. Our approach assigns lower priority to the irrelevant messages as they only need to be constructed so that posterior probabilities can be computed when propagation terminates. Experimental results, involving the processing of evidence in four real-world Bayesian networks, empirically demonstrate an improvement over the state-of-the-art method for exact inference in discrete Bayesian networks. (C) 2009 Wiley Periodicals, Inc. NETWORKS, Vol. 55(4), 350-359 2010


Keywords: Bayesian networks; join tree propagation; exact probabilistic inference; conditional independence

## 1. INTRODUCTION

Bayesian networks [19] are a formal approach to uncertainty management based on the combination of probability theory and graph theory. A Bayesian network is a directed acyclic graph [26] coupled with a set of conditional probability tables [23]. The vertices of the graph represent random variables, while the arcs in the graph represent probabilistic dependencies amongst the variables. It can be shown [11] that the product of the conditional probability tables is a joint probability distribution by utilizing the probabilistic conditional independencies [25] encoded in the directed acyclic graph. By providing a sound and concise representation of probabilistic knowledge [7, 13], Bayesian networks have been successfully applied in practice to many problem domains, including medical diagnosis [12, 20].

Although Cooper [9] has shown that the complexity of inference in Bayesian networks is NP-hard, various approaches have been developed that seem to work quite well

[^0]in practice $[5,8,10,22,24]$. Generally speaking, there are two approaches to exact inference in discrete Bayesian networks. One approach, called direct computation, performs inference directly within a Bayesian network. Two classical direct computation algorithms are variable elimination (VE) [28] and arc reversal (AR) [18, 21]. Another approach, known as join tree propagation, first builds a secondary network called a join tree [4] by triangulating [27] the directed acyclic graph. Join tree propagation then performs inference by propagating probabilities in the join tree. Shafer [23] emphasizes that join tree probability propagation is central to the theory and practice of probabilistic expert systems.

The state-of-the-art algorithm for exact inference in discrete Bayesian networks is Madsen's Lazy AR [14, 15]. Lazy AR is a hybrid approach, because it falls into the join tree propagation framework while utilizing a direct computation inference algorithm. More specifically, AR is applied to physically construct the messages passed from a join tree node to a neighbor. Although traditional join tree propagation algorithms pass a single probability table between neighboring nodes in the join tree [23], Lazy AR can pass a set of probability tables between nodes. By maintaining a factorization of probability tables, Lazy AR can show favorable experimental results $[14,15]$ with its exploitation of barren [21] variables and independencies induced by evidence. Nevertheless, there is room for improvement, because Lazy AR views all propagated messages as being of equal importance. On the contrary, it is often the case in real-world Bayesian networks that only some of the messages propagated from one join tree node to a neighbor are relevant to subsequent message construction at the neighbor node.

In this article, we propose prioritized join tree propagation as a new approach to exact inference in Bayesian networks. The distinguishing feature of our method can be seen as a three-step process. First, AR is applied only to determine the distribution heading (the schema or label) of each message (distribution) that will be propagated in a join tree. In other words, we identify all of the message headings without physically building in computer memory the probability distributions complete with probability values. Second, the relevant and irrelevant messages are identified (with respect to the subsequent message construction at the receiving join tree nodes). Finally, the relevant messages are then physically constructed in memory using variable elimination. Thus, in


[^0]:    Received September 2006; accepted February 2009
    Correspondence to: C. J. Butz; e-mail: butz@cs.uregina.ca
    Contract grant sponsor: NSERC Discovery; Contract grant number: 238880 DOI 10.1002/net. 20328
    Published online 31 July 2009 in Wiley InterScience (www.interscience. wiley.com).
    (C) 2009 Wiley Periodicals, Inc.


FIG. 1. Tables $p(a), p(b \mid a), p(c), p(d \mid c), p(e \mid c), p(f \mid d, e), p(g \mid b, f), p(h \mid c), p(i \mid h), p(j \mid g, h, i)$, and $p(k \mid g)$.
our method, a join tree node is allowed to physically build an outgoing message as soon as it has received all incoming messages that are relevant to its construction. The main advantage of prioritized join tree propagation over Lazy AR is that our approach does not force a join tree node to wait for messages that are irrelevant to its subsequent message computation. The efficiency improvement offered by prioritized join tree propagation is shown through empirical evaluations on four real-world Bayesian networks and one benchmark Bayesian network. As is usually done, inference is performed in each network with varying amounts of evidence, namely, zero, nine, and eighteen percent. Our prioritized join tree propagation approach finished inference faster than Lazy AR in all fifteen cases, as reported in Tables 2, 3, and 4.

This article is organized as follows. Section 2 contains background information. We propose prioritized join tree propagation in Section 3. Experimental results are shown in Section 4. Section 5 presents the conclusion.

## 2. DEFINITIONS

Here we review results from discrete Bayesian networks, and three approaches for exact inference therein.

Consider a finite set of discrete random variables $U=$ $\left\{v_{1}, v_{2}, \ldots, v_{n}\right\}$. Let $\operatorname{dom}\left(v_{i}\right)$ denote the finite domain of values that each variable $v_{i} \in U$ can assume. For a subset $X \subseteq U$, the Cartesian product of the domains of the individual variables in $X$ is $\operatorname{dom}(X)$. An element $x \in \operatorname{dom}(X)$ is a configuration of $X$. A potential [12] on $\operatorname{dom}(X)$ is a function $\phi$ such that $\phi(x) \geq 0$, for each configuration $x \in \operatorname{dom}(X)$, and at least one $\phi(x)$ is positive. For simplicity, we speak of a potential as defined on $X$ instead of on $\operatorname{dom}(X)$, and we call $X$ its domain rather than $\operatorname{dom}(X)$ [23]. A joint probability distribution [23] on $U$, written $p(U)$, is a function $p$ on $U$ satisfying the following two conditions: (i) $0 \leq p(u) \leq 1$, for each configuration $u \in \operatorname{dom}(U)$; (ii) $\sum_{u \in \operatorname{dom}(U)} p(u)=1$. Let $X$ and $Y$ be two disjoint subsets of $U$. A conditional probability table (table for short) [23] for $Y$ given $X$, denoted $p(Y \mid X)$, is a nonnegative function on $X \cup Y$, satisfying the following condition: for each configuration $x \in \operatorname{dom}(X)$, $\sum_{y \in \operatorname{dom}(Y)} p(Y=y \mid X=x)=1$. For example, given binary variables $U=\{a, b, \ldots, k\}$, tables $p(a), p(b \mid a), p(c), p(d \mid c)$, $p(e \mid c), p(f \mid d, e), p(g \mid b, f), p(h \mid c), p(i \mid h), p(j \mid g, h, i)$, and $p(k \mid g)$ are shown in Figure 1. Note that missing probabil-
ties can be obtained by the definition of a table. For instance, $p(a=0)=0.504$ and $p(b=0 \mid a=0)=0.948$.

The heading of a table is the label shown above the probability column. For instance, the heading of table $p(a)$ in Figure 1 is the label " $p(a)$ " appearing above the probability column. It will always be made clear as to whether $p(Y \mid X)$ refers to the heading or the table itself.

A discrete Bayesian network [19] on $U=\left\{v_{1}, v_{2}, \ldots, v_{n}\right\}$ is a pair $(D, C) . D$ is a directed acyclic graph with vertex set $U . C$ is the set of tables $\left\{p\left(v_{i} \mid P_{i}\right) \mid i=1,2, \ldots, n\right\}$, where $P_{i}$ denotes the parents of variable $v_{i} \in D$. For example, the directed acyclic graph in Figure 2i together with the corresponding tables in Figure 1 is based on a real-world Bayesian network for coronary heart disease (CHD) [12]. Here, the parents $P_{i}$ of variable $v_{i}=g$ are $P_{i}=\{b, f\}$.

We use the terms Bayesian network and directed acyclic graph interchangeably. A topological ordering [7] of the variables in a Bayesian network is denoted by $<$. The family $F_{i}$ of a variable $v_{i}$ in a Bayesian network is the variable together with its parents, that is, $\left\{v_{i}\right\} \cup P_{i}$. A variable without parents is called a root variable.

A Bayesian network $D$ graphically encodes probabilistic conditional independencies [25], which can be inferred from $D$ using the $d$-separation algorithm [19]. Based on the independencies encoded in $D$, the product of the tables in $C$ is a joint distribution $p(U)$ [11], namely, $p(U)=\prod_{v_{i} \in U} p\left(v_{i} \mid P_{i}\right)$. For example, the independencies encoded in the Bayesian network of Figure 2i indicate that the product of the tables in Figure 1 is a joint distribution on $U=\{a, b, c, d, \ldots, k\}$, namely, $p(U)=p(a) \cdot p(b \mid a) \cdot p(c) \cdot p(d \mid c) \cdots p(k \mid g)$. Thereby, one favorable feature of Bayesian networks is that they provide a compact, graphical representation of a joint distribution modelling a real-world problem domain. For instance, only 30 probabilities are required for the CHD Bayesian network in Figure 2i versus $2^{11}-1$ probabilities required for specifying the joint distribution $p(U)$ directly.

Suppose that the values $e$ of a set $E$ of variables in a Bayesian network have been observed and that the posterior probabilities of set $X$ (disjoint with $E$ ) are sought. All variables outside of $E \cup X$ must necessarily be eliminated in answering this query, denoted $p(X \mid E=e)$. A bruteforce approach to eliminating these variables, however, can involve unnecessary manipulation of probability distributions in memory. Given a Bayesian network $D$ and a query

![img-0.jpeg](img-0.jpeg)

FIG. 2. (i) The coronary heart disease (CHD) Bayesian network [12]. Given the query $p(k \mid f=0)$ : (ii) barren variables $h, i$, and $j$ have been pruned; (iii) variables $c, d$, and $e$ are also removed as they are independent of $k$ given evidence $f=0$.
$p(X \mid E=e)$, a variable $v_{i}$ is barren [21] if $\left(\left\{v_{i}\right\} \cup Y\right) \cap(X \cup E)=$ $\emptyset$, where $Y$ is the set of descendants of $v_{i}$ in $D$. For example, given the query $p(k \mid f=0)$ posed to the Bayesian network in Figure 2i, variables $h, i$, and $j$ are barren. Thus, they can be removed, yielding the network in Figure 2ii.

Similarly, independencies induced by evidence can also be taken advantage of to save unnecessary physical computation. Baker and Boult [2] proposed an algorithm, which we will call Prune, that prunes all variables from a Bayesian network that are irrelevant to a given query $p(X \mid E=e)$. Their algorithm removes barren variables as well as those variables rendered immaterial to $X$ given the evidence $E=e$. Note that the time complexity of Prune is $O(|\lambda|)$, where $|\lambda|$ is the number of arcs in the Bayesian network [2]. For example, given evidence $f=0$ in query $p(k \mid f=0)$ posed to Figure 2ii, variable $k$ is conditionally independent of variables $c, d$, and $e$. Thus, $c$, $d$, and $e$ can be safely removed to yield the smaller Bayesian network in Figure 2iii.

A root variable $v_{i}$ that is also an evidence variable can have its table ignored and, for each child $v_{j}$ of $v_{i}$, the table $p\left(v_{j} \mid P_{j}\right)$ is modified to agree with the observed evidence. In our running example, because $f$ is both an evidence variable and a root variable in Figure 2iii, table $p(f \mid d, e)$ is ignored and table $p(g \mid b, f)$ for the child $g$ of $f$ is modified to only contain rows agreeing with the evidence $f=0$ [23]. That is, all rows in $p(g \mid b, f)$ with $f=1$ are deleted leaving $p(g \mid b, f=0)$ stored in computer memory. The query $p(k \mid f=0)$ can now be answered by eliminating variables $a, b$, and $g$ from the distributions stored in computer memory.

Given a set of variables to be eliminated from a set $S$ of potentials, variable elimination (VE) [28] recursively eliminates the variables $v_{i}$ one-by-one using the following four steps: (i) remove from $S$ the set of potentials containing $v_{i}$; (ii) multiply together the distributions removed from $S$; (iii) sum $v_{i}$ out of the potential obtained in (ii); and (iv) add the resulting potential to $S$. Unlike VE, arc reversal (AR) [18, 21] eliminates variables while maintaining a factorization of tables. The following outline draws from $[14,15,21]$. Suppose variable $v_{i}$ is to be eliminated. $\operatorname{Arc}\left(v_{i}, v_{j}\right)$ is reversed by setting the
new parents of $v_{j}$ as $P_{j} \cup P_{j}-\left\{v_{i}\right\}$, while making $P_{i} \cup F_{j}-\left\{v_{i}\right\}$ the new parents of $v_{i}$. Next, new tables for $v_{j}$ and $v_{i}$ in the modified directed acyclic graph are physically constructed as follows [21]:

$$
p\left(v_{j} \mid P_{i} \cup P_{j}-\left\{v_{i}\right\}\right)=\sum_{v_{i}} p\left(v_{i} \mid P_{i}\right) \cdot p\left(v_{j} \mid P_{j}\right)
$$

and

$$
p\left(v_{i} \mid P_{i} \cup F_{j}-\left\{v_{i}\right\}\right)=\frac{p\left(v_{i} \mid P_{i}\right) \cdot p\left(v_{j} \mid P_{j}\right)}{p\left(v_{j} \mid P_{i} \cup P_{j}-\left\{v_{i}\right\}\right)}
$$

Note that it is not necessary to evaluate Equation (2) when the final arc from $v_{i}$ is reversed, because $v_{i}$ will be eliminated. Also, a directed acyclic graph structure is maintained after eliminating a variable, because AR uses a fixed topological ordering of the original Bayesian network to avoid creating directed cycles.

Although VE and AR compute the posterior probabilities of a set $X$ of variables given the evidence $E=e$, join tree propagation seeks to update all variables in $U-E$. The notion of a join tree is first needed. A join tree [4] is a tree with sets of variables as nodes, and with the property that any variable in two nodes is also in any node on the path between the two. The directed acyclic graph $D$ of a Bayesian network is converted into a join tree via the moralization and triangulation procedures. The moralization [19] $D_{\mathrm{m}}$ of $D$ is the undirected graph obtained from $D$ by adding undirected edges between every pair of nonadjacent vertices that have a common child, and then dropping the directions of all arcs. If necessary, undirected edges are added to the moralization to create a triangulated graph. An undirected graph is triangulated (chordal) [27], if each cycle of length four or more possesses an edge $\left(v_{i}, v_{j}\right)$ between two nonadjacent variables $v_{i}$ and $v_{j}$ in the cycle. Finding a triangulation of a graph by adding the minimum number of edges is NP-complete [19]. Each maximal clique (complete subgraph) [6] of the triangulated graph is represented by a node in the join tree. Although the CHD Bayesian network is useful for illustrating some pertinent concepts, it is not interesting due to its small size. A

![img-1.jpeg](img-1.jpeg)

FIG. 3. The Hailfinder join tree, where only the pertinent nodes and messages are shown. Both messages $p(n \mid l)$ and $p(q \mid l, n)$ from lmnqr are irrelevant to the forwarding of message $p(i)$ at node ilnqr.
larger real-world Bayesian network, called Hailfinder [1], is instead used here. Figure 3 shows the partial depiction of one possible join tree for Hailfinder. Some join tree edges have been directed to depict the propagation of those messages pertinent to our forthcoming discussion. Each join tree node name corresponds to the variables in the node. For instance, in Figure 3, node $a b c f$ means that the join tree node consists of variables $\{a, b, c, f\}$. The table of each variable $v_{i}$ in the given Bayesian network is assigned to precisely one join tree node containing $v_{i}$ and its parents $P_{i}$. For instance, $p(f \mid a, b, c)$ is assigned to $a b c f$ in Figure 3.

Given collected evidence, messages are systematically passed in a join tree such that each join tree node can compute the posterior probabilities of its variables when propagation finishes. In particular, the message passing is controlled by the rule that each node waits to send its message to a particular neighbor until it has received all messages from all its other
neighbors. It is well known that join tree propagation can be performed serially or in parallel [16, 23]. Our discussion is based on parallel computation.

Madsen's Lazy AR [14, 15] implements AR as the engine for performing inference in join tree propagation. When a join tree node $N$ is ready to send its messages to a particular neighbor $N^{\prime}$, the Lazy AR approach computes the messages from node $N$ to $N^{\prime}$ using the following three steps: (i) collect all messages from $N$ 's other neighbors; (ii) identify the relevant and irrelevant variables; (iii) apply AR to physically eliminate variables in $N-N^{\prime}$ from the relevant distributions.

Example 1. Consider how Lazy AR physically constructs the messages passed from node lmnqr to node ilnqr in the Hailfinder join tree of Figure 3 given evidence $j=0$. In Step (i), lmnqr collects $p(n \mid m)$ and $p(q \mid m, n)$ from node kmnq, as well as $p(m \mid l)$ from node elm. For Step (ii), no variables are
![img-2.jpeg](img-2.jpeg)

FIG. 4. Lazy AR applies AR to eliminate variable $m$ in Example 1.

![img-3.jpeg](img-3.jpeg)

FIG. 5. For building messages $p(j=0)$ and $p(m \mid j=0)$ from node lmnqr, messages $p(j=0)$ and $p(l \mid j=0)$ from ilnqr are, respectively, relevant, whereas the message $p(r \mid j=0, l, n, q)$ is irrelevant in both cases.
irrelevant. In Step (iii), Lazy AR eliminates variable m from the Bayesian network in Figure 4i defined by these tables as follows. Observe that arcs $(m, n)$ and $(m, q)$ need to be reversed and $n \prec q$. For the first arc $(m, n), v_{i}=m, P_{i}=\{l\}$, $v_{j}=n, P_{j}=\{m\}$, and $F_{j}=\{m, n\}$. The reversed arc $(n, m)$ is created by setting $P_{i}=\{l, n\}$ and $P_{j}=\{l\}$, as shown in Figure 4ii. Next, the new table $p(n \mid l)$ for $n$ is physically constructed by Equation (1) as: $p(n \mid l)=\sum_{m} p(m \mid l) \cdot p(n \mid m)$. Using Equation (2), the new table for $m$ is constructed in computer memory as: $p(m \mid l, n)=(p(m \mid l) \cdot p(n \mid m)) / p(n \mid l)$. Similarly, $\operatorname{arc}(m, q)$ is reversed as $(q, m)$ and a new table for $q$ is physically computed: $p(q \mid l, n)=\sum_{m} p(m \mid l, n) \cdot p(q \mid m, n)$, as shown in Figure 4iii. Variable $m$ can now be removed from the network as illustrated in Figure 4iv. The constructed messages $p(n \mid l)$ and $p(q \mid l, n)$ are sent to ilnqr.

## 3. PRIORITIZED JOIN TREE PROPAGATION

In this section, we introduce prioritized join tree propagation as a new approach to Bayesian inference. Our method can be broken down into three tasks: (i) identify the headings of all messages to be propagated in the join tree. (ii) for each join tree node, identify the relevant and irrelevant incoming messages with respect to each outgoing message; (iii) apply VE to physically build the relevant messages, followed by the irrelevant messages.

For probabilistic inference in real-world Bayesian networks, it is often the case that only some of the messages propagated are relevant to subsequent message computation at the receiving node. Using the propagation of evidence in
the Hailfinder join tree, Example 2 will show that all messages from lmnqr are irrelevant to ilnqr, while Example 3 illustrates that some of the messages from ilnqr to lmnqr are irrelevant. For simplicity we ignore all distributions not essential to our main point.

Example 2. Consider the message $p(i)$ to be passed from node ilnqr to node gjjl in Figure 3. Clearly, ilnqr simply forwards to gjjl the incoming message $p(i)$ from node $f i$. Therefore, all of the physical computation done by Lazy AR at node lmnqr in Example 1 to construct messages $p(n \mid l)$ and $p(q \mid l, n)$ is irrelevant to the subsequent message construction at ilnqr.

Example 2 shows that Lazy AR will force node ilnqr to wait for node lmnqr to build messages $p(n \mid l)$ and $p(q \mid l, n)$, even though these messages are irrelevant to the forwarding of the subsequent message $p(i)$ from ilnqr.

Example 3. In Figure 5, consider Lazy AR's construction of the three messages $p(j=0), p(l \mid j=0)$, and $p(r \mid j=0, l, n, q)$ sent from node ilnqr to node lmnqr in the Hailfinder join tree given evidence $j=0$. By Step (i), node ilnqr has collected messages $p(i), p(j=0 \mid i)$, and $p(l \mid i, j=0)$ from its other neighbors. In Step (ii), all variables are relevant. For Step (iii), variable i needs to be eliminated from these three messages together with the table $p(r \mid i, l, n, q)$ assigned to ilnqr. Arcs $(i, j),(i, l)$, and $(i, r)$ need to be reversed. Because $j \prec l \prec r$, AR is applied as follows. Arc $(i, j)$ is reversed as $(j, i)$ using $p(j=0)=\sum_{i} p(i) \cdot p(j=0 \mid i)$ and $p(i \mid j=0)=(p(i) \cdot p(j=0 \mid i)) / p(j=0)$. To create $(l, i)$,

Lazy AR builds $p(l \mid j=0)=\sum_{i} p(i \mid j=0) \cdot p(l \mid i, j=0)$ and $p(i \mid j=0, l)=(p(i \mid j=0) \cdot p(l \mid i, j=0)) / p(l \mid j=0)$. Lastly, reversing $(i, r)$ is accomplished by physically building $p(r \mid j=0, l, n, q)=\sum_{i} p(i \mid j=0, l) \cdot p(r \mid i, l, n, q)$. Lazy AR then sends the constructed messages $p(j=0)$, $p(l \mid j=0)$, and $p(r \mid j=0, l, n, q)$ to lmnqr. Revisiting Figure 5, now consider how the subsequent messages $p(j=0)$ and $p(m \mid j=0)$ from lmnqr to node kmnq are constructed. Message $p(j=0)$ can be simply forwarded meaning that the incoming messages $p(l \mid j=0), p(r \mid j=0, l, n, q)$, and $p(m \mid l)$ are irrelevant. Lazy AR builds message $p(m \mid j=0)$ as: $p(m \mid j=0)=\sum_{l} p(l \mid j=0) \cdot p(m \mid l)$. This implies that only the incoming message $p(l \mid j=0)$ from ilnqr and message $p(m \mid l)$ from elm are relevant, while the incoming messages $p(j=0)$ and $p(r \mid j=0, l, n, q)$ are irrelevant.

Example 3 shows that Lazy AR forces lmnqr to wait for all messages to be received, even though only some of the messages are relevant to subsequent message computation at lmnqr. Examples 2 and 3 together motivate the development of a new approach to Bayesian inference-one that gives priority to relevant messages.

### 3.1. Identifying the Message Headings

Our prioritized join tree propagation approach can identify the headings of all messages propagated in a join tree with Algorithm 1, called MsgId, defined as follows.

```
Algorithm 1 [3] MsgId \((C, X)\)
Input: \(C\) - a set of distribution headings at a join tree node \(N\),
    \(X\) - the set of variables to be eliminated.
Output: the set \(C\) of message headings sent from a join tree
    node to a neighbor.
begin
```

Construct the unique directed acyclic graph $D_{N}$ defined by $C$.
for each variable $v_{i}$ in $X$
Let $Y=\left\{v_{1}, \ldots, v_{k}\right\}$ be the set of all children of $v_{i}$ in $D_{N}$, where $v_{1} \prec \cdots \prec v_{k}$.
for $j=1, \ldots, k$

$$
\begin{aligned}
P_{j} & =P_{i} \cup P_{j}-\left\{v_{i}\right\} \\
P_{i} & =P_{i} \cup F_{j}-\left\{v_{i}\right\}
\end{aligned}
$$

Remove $v_{i}$ from $D_{N}$ and its distribution heading from $C$.
return $(C)$
end

Example 4. In the Hailfinder join tree of Figure 3, let us show how node lmnqr identifies the headings of the messages to be sent to its neighbor ilnqr. Node lmnqr collects the headings $p(m \mid l), p(n \mid m)$, and $p(q \mid m, n)$ sent from its neighbors elm and kmnq. It then calls MsgId with $C=$ $\{p(m \mid l), p(n \mid m), p(q \mid m, n)\}$ and $X=\{m\}$. Here, $v_{i}=m$, $Y=\left\{v_{1}=n, v_{2}=q\right\}, P_{i}=\{l\}, P_{1}=\{m\}, F_{1}=\{m, n\}$, $P_{2}=\{m, n\}$, and $F_{2}=\{m, n, q\}$. Consider the first variable
![img-4.jpeg](img-4.jpeg)

FIG. 6. Given evidence $j=0$ in the join tree for the real-world Hailfinder Bayesian network (see Figs. 3 and 5), our system identifies the headings of the messages (distributions) to be propagated.
$v_{1}=n$ in $Y$. As $P_{i} \cup P_{1}-\left\{v_{i}\right\}=\{l\}, P_{1}$ is modified as $P_{1}=\{l\}$. Because $P_{i} \cup F_{1}-\left\{v_{i}\right\}=\{l, n\}, P_{i}$ is changed to $P_{i}=\{l, n\}$. The set $C$ is set to $C=\{p(m \mid l, n), p(n \mid l)$, $p(q \mid m, n)\}$. Now consider the second variable $v_{2}=q$ in $Y$. $P_{2}$ is changed to $\{l, n\}$, because $P_{i} \cup P_{2}-\left\{v_{i}\right\}=\{l, n\}$. As $P_{i} \cup F_{2}-\left\{v_{i}\right\}=\{l, n, q\}, P_{i}$ is modified as $P_{i}=\{l, n, q\}$. Variable $m$ is then removed. Thus, $C=\{p(n \mid l), p(q \mid l, n)\}$ denotes the headings of messages $p(n \mid l)$ and $p(q \mid l, n)$ sent from lmnqr to ilnqr.

Note that it is easy to use MsgId to identify message headings when evidence is propagated in a join tree. Given evidence $E=e$, set $N=N \cup E$ for each node $N$ in the join tree. On this augmented join tree, apply MsgId as usual. After message heading identification, for each evidence variable $v \in E$, change each occurrence of $v$ in the headings returned by MsgId from $v$ to $v=\varepsilon$, where $\varepsilon$ is the observed value of $v$. The screen-shot of our implemented system in Figure 6 shows some of the message headings identified given evidence $j=0$ in the Hailfinder join tree. Figure 6 emphasizes node lmnqr and its neighbors. The important point is that the MsgId algorithm identifies the headings of the messages that will be propagated in the join tree before the probability distributions of the messages are physically built in computer memory.

### 3.2. Identifying the Relevant Messages

Here, we determine the relevant messages with respect to subsequent message computation at the receiving node.

Consider three distinct join tree nodes $N_{1}, N_{2}$, and $N_{3}$ such that $p\left(X_{1} \mid Y_{1}\right)$ is a message to be passed from $N_{1}$ to $N_{2}$ and $p\left(X_{2} \mid Y_{2}\right)$ is a message to be passed from $N_{2}$ to $N_{3}$. We say $p\left(X_{1} \mid Y_{1}\right)$ is relevant to $p\left(X_{2} \mid Y_{2}\right)$, if $p\left(X_{1} \mid Y_{1}\right)$ is required in

![img-5.jpeg](img-5.jpeg)

FIG. 7. Given evidence $j=0$ in the Hailfinder join tree of Figure 5, our system identifies the relevant and irrelevant incoming messages for the construction of every outgoing message.
the physical construction or the forwarding of $p\left(X_{2} \mid Y_{2}\right)$; otherwise, $p\left(X_{1} \mid Y_{1}\right)$ is irrelevant to $p\left(X_{2} \mid Y_{2}\right)$. By viewing each outgoing message $p\left(X_{2} \mid Y_{2}\right)$ sent out from a join tree node $N_{2}$ as a query posed to $N_{2}$ 's local directed acyclic graph $D_{N_{2}}$, the RelMsgId algorithm can determine which, if any, of the incoming messages $p\left(X_{1} \mid Y_{1}\right)$ are relevant.

## Algorithm 2 RelMsgId $(A, p(v \mid Y), C)$

Input: $A$ - the set of distribution headings assigned to join tree node $N$,
$p(v \mid Y)$ - the heading of an outgoing message sent from $N$ to a neighbor $N^{\prime}$,
$C$ - the headings of the incoming messages sent to $N$ from all neighbors except $N^{\prime}$.
Output: classification of the headings in $C$ as relevant or irrelevant with respect to constructing or forwarding $p(v \mid Y)$. begin
Build the local directed acyclic graph $D_{N}$ uniquely defined by $A$ and $C$ at join tree node $N$.
Apply the Prune algorithm on $D_{N}$ using $p(v \mid Y)$.
for each variable $v_{i}$ that was pruned
if $p\left(v_{i} \mid P_{i}\right) \in C$
Mark heading $p\left(v_{i} \mid P_{i}\right)$ as irrelevant.
for each variable $v_{i}$ that was not pruned
if $v_{i} \neq v$ and $p\left(v_{i} \mid P_{i}\right) \in C$ and $v_{i}$ is a root evidence variable

Mark heading $p\left(v_{i} \mid P_{i}\right)$ as irrelevant.
Mark all remaining unmarked headings in $C$ as relevant. return $(C)$
end

Example 5. Consider the message $p(i)$ sent from node ilnqr to its neighbor gjjl in the Hailfinder join tree of Figure 3. RelMsgId builds the local directed acyclic graph defined by the incoming headings $p(i), p(n \mid l)$, and $p(q \mid l, n)$ along with the assigned heading $p(r \mid i, l, n, q)$. Given this graph and query $p(i)$, the Prune algorithm removes the irrelevant variables $l, n, q$, and $r$. Thus, RelMsgId marks the incoming messages $p(n \mid l)$ and $p(q \mid l, n)$ from node lmnqqr as irrelevant to the forwarding of $p(i)$. On the contrary, the incoming message $p(i)$ from node $f i$ is marked relevant. In the converse direction, consider message $p(m \mid j=0)$ sent from node lmnqr to its neighbor kmnq in Figure 5. RelMsgId builds the local directed acyclic graph defined by the incoming messages $p(j=0), p(l \mid j=0), p(r \mid j=0, l, n, q)$, and $p(m \mid l)$. The Prune algorithm removes irrelevant variables $n, q$, and $r$. Thus, RelMsgId marks $p(r \mid j=0, l, n, q)$ as irrelevant. Because $j$ is a root evidence variable, RelMsgId marks $p(j=0)$ as irrelevant. On the other hand, the incoming messages $p(l \mid j=0)$ and $p(m \mid l)$ are marked as relevant.

Given evidence $j=0$ in the Hailfinder join tree, the screen-shot of our system in Figure 7 indicates whether or not an incoming message from node 1 is relevant at node 2 for the subsequent construction of a particular message from node 2 to node 3.

### 3.3. Physical Construction of Messages

A join tree node is allowed to physically build an outgoing message as soon as it has received all incoming messages that are relevant to its construction. Our approach uses VE to build distributions in computer memory. AR is not well suited

for message construction in prioritized join tree propagation, because it constructs a new probability distribution for every child of the variable being eliminated [3]. As some of these new distributions can be deemed relevant and the rest irrelevant, we instead call VE to build the relevant distributions as needed. After all relevant messages have been constructed and sent, the irrelevant messages are built so that posterior probabilities can be computed when propagation finishes.

Example 6. Consider how VE builds message $p(m \mid j=0)$ from node lmnqr to node kmnq in the Hailfinder join tree of Figure 5 when evidence $j=0$ is observed. By Example 5, only $p(m \mid l)$ and $p(l \mid j=0)$ are relevant to this task. To eliminate variable $l$, VE computes $p(m, l \mid j=0)=p(m \mid l) \cdot p(l \mid j=0)$, followed by $p(m \mid j=0)=\sum_{l} p(m, l \mid j=0)$. The probability table $p(m \mid j=0)$ is returned to lmnqr.

Further to Example 6, while $p(r \mid j=0, l, n, q)$ is irrelevant with respect to subsequent message construction at node lmnqr, it is needed so that lmnqr can compute the posterior probability of its variables (given the evidence $j=0$ ) from the tables assigned to it together with those passed to it after propagation finishes. According to Figures 3 and 5 , when propagation of the evidence $j=0$ finishes, the probability information at node lmnqr is more formally expressed as: $p(l, m, n, q, r, j=0)=p(j=0) \cdot p(l \mid j=$ $0) \cdot p(m \mid l) \cdot p(n \mid m) \cdot p(q \mid m, n) \cdot p(r \mid j=0, l, n, q)$. The posterior probability $p(n \mid j=0)$, for instance, can be easily computed from this factorization.

The primary difference between our approach and Lazy AR is illustrated in Example 6, whereby our approach allows node lmnqr to physically build message $p(m \mid j=0)$ as soon as it has the received messages $p(l \mid j=0)$ and $p(m \mid l)$. On the contrary, the state-of-the-art method, Lazy AR, will force node lmnqr to wait for the reception of messages $p(j=0)$ and $p(r \mid j=0, l, n, q)$ as well, even though these two messages are not required in the physical construction of $p(m \mid j=0)$. This unnecessary delay in Example 6 is inherently built into the main philosophy of Lazy AR. Messages are classified as relevant or irrelevant in Step (ii) only after a join tree node collects all of its messages in Step (i). This immediately means that for any incoming message deemed irrelevant in Step (ii), Lazy AR has already forced the join tree node to wait for its physical construction prior to Step (i). On the contrary, in the three main steps of prioritized join tree propagation, the message headings identified in Step (i) are classified as relevant or irrelevant in Step (ii) before any physical computation takes place in computer memory by Step (iii). Therefore, by avoiding this type of unnecessary delay, our prioritized approach can perform Bayesian network inference faster than Lazy AR.

## 4. EXPERIMENTAL RESULTS

Here, we conduct an empirical comparison of Lazy AR and prioritized join tree propagation.

We first illustrate how prioritized messages can be exploited during parallel computation based on the
following three assumptions: (i) there are two processors, denoted $P_{1}$ and $P_{2}$, each with a queue of messages to be built or forwarded; (ii) in Lazy AR, if a join tree node applies AR to physically build $k$ messages $\left\{p\left(v_{1} \mid P_{1}\right), p\left(v_{2} \mid P_{2}\right), \ldots, p\left(v_{k} \mid P_{k}\right)\right\}$, then we place all $k$ messages on the queue of same processor, because $p\left(v_{1} \mid P_{1}\right)$ is needed to build $p\left(v_{2} \mid P_{2}\right)$, and so on; (iii) in Lazy AR, the processor that finishes building or forwarding the messages sent from node $N_{1}$ to node $N_{2}$ will be used to build or forward the subsequent messages sent from $N_{2}$ to node $N_{3}\left(N_{3} \neq N_{1}\right)$. The reason is that, in Lazy AR, if $N_{1}$ sends messages to $N_{2}$, then $N_{2}$ necessarily waits for all of $N_{1}$ 's messages before building or forwarding the subsequent messages to node $N_{3}$. In the next two examples, we often refer to messages with the sending and receiving nodes understood.

Example 7. The optimal schedule in Lazy AR for propagating the eleven distributions from nodes dkoq, elm, and abcf towards node gijl in the real-world Hailfinder join tree of Figure 3 is:

$$
\begin{aligned}
P_{1} & : p(q \mid k, o), p(k), p(q \mid k, m), p(n \mid m), p(q \mid m, n) \\
& \quad p(n \mid l), p(q \mid l, n), p(i) \\
P_{2} & : p(m \mid l), p(f), p(i)
\end{aligned}
$$

By (ii) and (iii), the eight messages $p(q \mid k, o), p(k), p(q \mid k, m)$, $p(n \mid m), p(q \mid m, n), p(n \mid l), p(q \mid l, n)$, and $p(i)$ from node dkoq towards node gijl must necessarily be built in a serial fashion, say on processor $P_{1}$. This means that processor $P_{2}$ builds three messages, namely, $p(m \mid l), p(f)$, and $p(i)$. Our optimal schedule is:

$$
\begin{aligned}
& P_{1}: p(q \mid k, o), p(q \mid k, m), p(n \mid m), p(q \mid m, n), p(n \mid l), p(q \mid l, n) \\
& P_{2}: p(k), p(m \mid l), p(f), p(i), p(i)
\end{aligned}
$$

Example 7 shows that, in our approach, when processor $P_{1}$ is building $p(q \mid k, o)$, processor $P_{2}$ is forwarding $p(k)$, because we mark $p(q \mid k, o)$ as irrelevant to the forwarding of $p(k)$. Moreover, $p(i)$ can be built and forwarded by $P_{2}$, because $p(f)$ is the only relevant message for building $p(i)$. Now, let us consider a more involved example.

Example 8. In the Hailfinder join tree of Figure 5, the Lazy AR optimal schedule for propagating the thirteen distributions from nodes hxy, gst, abcf, and elm towards node kmnq is:

$$
\begin{aligned}
& P_{1}: p(h), p(j=0 \mid i), p(j=0 \mid i), p(l \mid i, j=0), p(j=0) \\
& \quad p(l \mid j=0), p(r \mid j=0, l, n, q), p(j=0) \\
& P_{2}: p(g), p(f), p(i), p(m \mid l), p(m \mid j=0)
\end{aligned}
$$

By (ii) and (iii), the first eight distributions sent from hxy towards kmnq must necessarily be built in a serial fashion, say on $P_{1}$. Therefore, the remaining five messages are placed in $P_{2}$ 's queue. Observe that even though there are two messages $p(j=0)$ and $p(m \mid j=0)$ sent from node lmnqr to kmnq,

TABLE 1. Description of real-world or benchmark Bayesian networks and the constructed join trees.


$p(j=0)$ can be simply forwarded by $P_{1}$ in Equation (3), while $p(m \mid j=0)$ can be built by $P_{2}$, without the need of $p(j=0)$ as shown in Example 3. The prioritized propagation optimal schedule is:

$$
\begin{aligned}
P_{1}: & p(h), p(j=0 \mid i), p(j=0 \mid i), p(l \mid i, j=0) \\
& p(l \mid j=0), p(r \mid j=0, l, n, q) \\
P_{2}: & p(g), p(f), p(i), p(j=0), p(j=0), p(m \mid l), p(m \mid j=0)
\end{aligned}
$$

The two important points in Example 8 are that in Equation (3), Lazy AR insists that $p(l \mid i, j=0)$ be physically built before $p(j=0)$ is constructed, even though $p(l \mid i, j=0)$ is not needed in the construction of $p(j=0)$. Moreover, for the second $p(j=0)$ in Equation (3), Lazy AR requires $p(l \mid i, j=0)$, $p(l \mid j=0)$, and $p(r \mid j=0, l, n, q)$ to be physically built even though they are not needed to forward $p(j=0)$. These problems are avoided in our prioritized schedule. Examples 7 and 8 together illustrate that Lazy AR can impose unnecessary restrictions on when a distribution is built or forwarded. Therefore, Lazy AR often performs calculations in a serial manner when, in fact, they can be performed in a parallel fashion. By recognizing and removing these unnecessary restrictions, our prioritized approach necessarily runs faster.

It is also worth contrasting our work here with our previous work. In [3], we suggest applying the VE algorithm to build the messages in a Lazy AR schedule rather than applying the AR algorithm to construct the messages as Lazy AR does. We explicitly demonstrated that the AR algorithm can build probability distributions that will not be passed as messages, nor are they needed in the construction of the messages that will be passed. Thus, although our previous work focused on how the messages are built, the work here focuses on when the messages are built. We now empirically demonstrate the

TABLE 2. The performance of Lazy AR and our prioritized approach without evidence variables.


TABLE 3. The performance of Lazy AR and our prioritized approach with nine percent evidence variables.


time savings to be made by using a better schedule of when messages can be constructed.

In our empirical evaluation, both methods were implemented in the C++ programming language. The experiments were conducted on a 24 -processor SGI Onyx2 graphics supercomputer. Each inference algorithm has two processors allocated for its sole usage. The evaluation was carried out on four real-world Bayesian networks, called Alarm, Barley, CHD and Hailfinder, as well as one benchmark Bayesian network known as Insurance. The corresponding join trees were built using the Netica system [17]. Table 1 describes each Bayesian network and its corresponding join tree.

Table 2 reports on Bayesian inference with no evidence variables. The running times in seconds are listed in the second and third columns for Lazy AR and prioritized join tree propagation, respectively. The last column shows the speedup of our prioritized approach over Lazy AR, the average of which was $49.6 \%$.

Next, the running times of Bayesian network inference involving evidence were measured. As shown in Tables 3 and 4 , approximately nine percent and eighteen percent of the variables in each Bayesian network were randomly instantiated as evidence variables, respectively. Once again, prioritized join tree propagation was faster than Lazy AR in all Bayesian networks. In Table 3, the time saved ranged from 13.6 to $66.7 \%$ with an average of $36.1 \%$. Similarly, in Table 4 , the time saved ranged from 7.4 to $40.9 \%$ with an average of $21.7 \%$.

## 5. CONCLUSIONS

This article is the first work to suggest the concept of prioritized join tree propagation. As illustrated in Examples 2 and 3, the motivation for this study is based on the observation

TABLE 4. The performance of Lazy AR and our prioritized approach with eighteen percent evidence variables.


that, during inference in real-world Bayesian networks, it is often the case that only some of the messages passed to a join tree node are actually needed in the physical construction of the subsequent probability distributions (messages) sent out from the node. Consequently, our approach first identifies the headings of all distributions to be propagated in the join tree, as illustrated by the screen-shot of Figure 6. With respect to each join tree node $N$, our system then labels each incoming message to $N$ as either relevant or irrelevant to the physical construction of each message outgoing from $N$, as indicated by the screen-shot of Figure 7. Lastly, our system builds the relevant messages and then the irrelevant messages. As reported in Tables 2, 3, and 4, in all four real-world Bayesian networks and one benchmark Bayesian network and with varying amounts of evidence, prioritized join tree propagation finished faster than Lazy AR without exception. Future work includes the identification of those instances when the same distribution is to be constructed at multiple join tree nodes, as well as the development of a heuristic to estimate the node to best build the distribution.

## Acknowledgments

The authors would like to thank anonymous reviewers for their contribution in making a more clear and focused paper.
