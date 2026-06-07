# Constructing the Dependency Structure of a Multiagent Probabilistic Network 

S.K. Michael Wong, Member, IEEE, and Cory J. Butz


#### Abstract

A probabilistic network consists of a dependency structure and corresponding probability tables. The dependency structure is a graphical representation of the conditional independencies that are known to hold in the problem domain. In this paper, we propose an automated process for constructing the combined dependency structure of a multiagent probabilistic network. Each domain expert supplies any known conditional independency information and not necessarily an explicit dependency structure. Our method determines a succinct representation of all the supplied independency information called a minimal cover. This process involves detecting all inconsistent information and removing all redundant information. A unique dependency structure of the multiagent probabilistic network can be constructed directly from this minimal cover. The main result of this paper is that the constructed dependency structure is a perfect-map of the minimal cover. That is, every probabilistic conditional independency logically implied by the minimal cover can be inferred from the dependency structure and every probabilistic conditional independency inferred from the dependency structure is logically implied by the minimal cover.


Index Terms-Probabilistic networks, dependency structure, probabilistic reasoning, conditional independence, data dependencies, multiagent systems.

## 1 INTRODUCTION

Probabilistic networks [11], [14], [19], [20] have become an established framework for representing and reasoning with uncertain knowledge. A probabilistic network consists of a dependency structure coupled with a corresponding set of probability tables. The dependency structure is a graphical representation of the conditional independencies that are known to hold in the problem domain. These conditional independencies are needed to provide an economical representation of a joint probability distribution over the problem domain. Clearly, probabilistic reasoning would not be practical without this independency information. Traditionally, there are two main types of probabilistic networks, namely, Bayesian and Markov. A Bayesian network [14], [19], [20] consists of a directed acyclic graph (DAG) and corresponding conditional probability tables. The DAG can represent conditional independencies that hold over any subset of variables in the problem domain. The other kind of probabilistic network is called a Markov network. A Markov network [11] consists of an acyclic hypergraph and corresponding potentials [11]. Unlike a DAG, which is capable of representing independencies over any subset of variables in the problem domain, an acyclic hypergraph can only represent known conditional independencies that involve all the variables in the problem domain. We refer to these conditional independencies as nonembedded. In spite of not being capable of representing independencies involving proper subsets of variables, a Markov network can take advantage of the

- The authors are with the Department of Computer Science, University of Regina, Regina, Saskatchewan, Canada, S4S 0A2.
E-mail: [wong, butz]@cs.uregina.ca.
Manuscript received 26 Oct. 1996; revised 27 Oct. 1998; accepted 15 Dec. 1999.

For information on obtaining reprints of this article, please send e-mail to: tkde@computer.org, and reference IEEECS Log Number 108121.
many efficient propagation techniques [13], [15], [24] developed for computing marginal distributions.

Traditionally, probabilistic knowledge is represented and reasoned with by a single agent. Manually constructing a Bayesian network has been regarded as a difficult procedure, especially when the conditional independency information regarding the problem domain is not fully understood. Several learning methods have subsequently been developed for constructing the dependency structure of a probabilistic network using independency information mined from observed data [12], [20], [31].

Recently, there is emerging interest in extending the traditional single-agent probabilistic environment into a multiagent environment. In these situations, a number of individual agents are willing to cooperate and share their knowledge to reach a common goal. (It is also possible that the agents are physically separated.) An example of this situation can be found in medical applications. Each agent could represent a medical specialist. These specialists pool their knowledge together to make a diagnosis. Another example can be found in military applications. Each agent could represent a unit commander in a battle. Each commander makes decisions with the information he possesses together with the information supplied by the other unit commanders.

In a multiagent environment, we assume that the knowledge of each agent is represented by a marginal distribution of a common joint probability distribution. To define such a multiagent probabilistic network, we need to explicitly specify the dependency structure representing the conditional independency information known to hold in the multiagent problem domain. It is not realistic to expect the domain experts to manually construct the dependency structure since the problem domain may be much larger and perhaps distributed. One suggestion would be to learn

the dependency structure from observed data. It is not entirely clear, however, how those learning methods [12], [20], [31] developed for the single-agent environment can be applied. For example, it may not be possible to obtain a reliable sample. On the other hand, if the learning methods are applied to collected samples for each individual agent, then independence assumptions must be made rendering the samples independent. Thus, constructing the multiagent dependency structure amounts to finding a method to combine the known conditional independency information supplied by the individual domain experts. One previously proposed method [37] constructs the dependency structure of a multiagent Bayesian network. That method verifies whether the dependency structure formed by connecting the individual agent DAGs is acyclic. This method is straightforward, but may be too restrictive for constructing the multiagent dependency structure in some situations. (See the discussion on related work in Section 3.)

In this paper, we suggest a more robust algorithm for constructing the dependency structure of a multiagent probabilistic network. Each domain expert supplies any known conditional independency information and not necessarily an explicit dependency structure. Our automated process computes a succinct representation of all the supplied independency information, called a minimal cover. This process involves detecting all inconsistent information and removing all redundant information. A unique dependency structure of the multiagent probabilistic network can be constructed directly from this minimal cover. In fact, it is shown that the constructed dependency structure is a perfect-map [20] of the minimal cover. That is, every probabilistic conditional independency logically implied by the minimal cover can be inferred from the dependency structure, and every probabilistic conditional independency inferred from the dependency structure is logically implied by the minimal cover. Our method takes advantage of the fact that there exists a complete axiomatization for nonembedded conditional independencies [10], [20], [29].

Our formulism here is based on a generalized relational data model [28], [35] we developed for probabilistic reasoning. In fact, our data model can be applied to other applications involving local propagation on an acyclic hypergraph [35], including dynamic programming [5], solving sparse linear equations [21], and constraint propagation [7]. The process of constructing an acyclic hypergraph proposed in this paper can then be applied to these other applications by defining the supplied independency information accordingly.

This paper is organized as follows: The basic notions are defined in Section 2. As the reader may not be familiar with the generalized relational data model, we have included a review of this model. In Section 3, we discuss related research. The proposed method for constructing the dependency structure of a multiagent Markov network is described in Section 4. We show in Section 5 how the dependency structure of a Markov network may be further refined using the mixture of embedded and nonembedded conditional independencies. The conclusion is presented in Section 6.

## 2 Basic Notions

We begin by defining some pertinent notions: hypergraphs, relational databases, and our generalized relational data model [28], [29], [35]. A detailed description of this model is given here as it forms the basis of our subsequent discussion.

### 2.1 Hypergraphs

Let $\mathcal{N}$ be a finite set of variables $\left\{A_{1}, A_{2}, \ldots, A_{m}\right\}$. A hypergraph, denoted $\mathcal{H}$, is a family of subsets of variables in $\mathcal{N}$, i.e., $\mathcal{H} \subseteq 2^{\mathcal{N}}$. An element in $\mathcal{H}$ is called a hyperedge. We call an element $t \in \mathcal{H}$, a twig, if there exists another distinct element $b \in \mathcal{H}$, such that

$$
t \cap(\cup\{h \mid h \in \mathcal{H} \text { and } h \neq t\})=t \cap b
$$

(By this definition, the hyperedge in a hypergraph consisting of a single hyperedge is not a twig.) This means that the intersection of $t$ and the hypergraph $\cup(\mathcal{H}-\{t\})$ is contained in the hyperedge $b$. We call any such $b$ a branch for the twig $t$ and note that a twig $t$ may have many possible branches. A hypergraph $\mathcal{H}=\left\{h_{1}, h_{2}, \ldots, h_{n}\right\}$ is called an acyclic hypergraph (a hypertree) [4], [24] if its elements $h_{1}, h_{2}, \ldots, h_{i}$ can be ordered such that $h_{i}$ is a twig in the subhypergraph, $\left\{h_{1}, h_{2}, \ldots, h_{i}\right\}, i=2, \ldots, n$. We call any ordering satisfying this condition a hypertree construction ordering for $\mathcal{H}$. (A hypertree construction ordering can also be represented as a join tree [4].) Given a particular hypertree construction ordering, we can choose an integer $b(i)$, for $i=2, \ldots, n$, such that $1 \leq b(i) \leq i-1$ and $h_{b(i)}$ is a branch for $h_{i}$ in $\left\{h_{1}, h_{2}, \ldots, h_{i}\right\}$. We call $b(i)$ a branching function for this ordering. It is possible that a hypertree construction ordering may have more than one branching function. Given a hypertree construction ordering $h_{1}, h_{2}, \ldots, h_{n}$ for a hypertree $\mathcal{H}$, and a branching function $b(i)$ for this ordering, the set $\mathcal{J}$ of J-keys is defined as

$$
\mathcal{J}=\left\{h_{b(2)} \cap h_{2}, h_{b(3)} \cap h_{3}, \ldots, h_{b(n)} \cap h_{n}\right\}
$$

This set $\mathcal{J}$ is in fact independent of the hypertree construction ordering, i.e., $\mathcal{J}$ is the same for any hypertree construction ordering of a given acyclic hypergraph. In the probabilistic reasoning theory, the set $\mathcal{J}$ of the hypertree $\mathcal{H}$ is referred to as the separation set.
Example 1. Consider the case where $\mathcal{N}=\left\{A_{1}, A_{2}, \ldots, A_{6}\right\}$. Let

$$
\begin{aligned}
\mathcal{H}=\{ & h_{1}=\left\{A_{1}, A_{2}, A_{3}\right\}, h_{2}=\left\{A_{2}, A_{3}, A_{4}\right\} \\
& h_{3}=\left\{A_{2}, A_{3}, A_{5}\right\}, h_{4}=\left\{A_{5}, A_{6}\right\}\}
\end{aligned}
$$

denote the hypergraph shown in Fig. 1. Since we can define a hypertree construction ordering $h_{1}, h_{2}, h_{3}, h_{4}$, by definition this hypergraph is a hypertree. One possible branching function for this ordering $h_{1}, h_{2}, h_{3}, h_{4}$ is $b(2)=1, b(3)=1, b(4)=3$. The set $\mathcal{J}$ of J-keys for the acyclic hypergraph $\mathcal{H}$ is

$$
\mathcal{J}=\left\{h_{1} \cap h_{2}, h_{1} \cap h_{3}, h_{3} \cap h_{4}\right\}=\left\{\left\{A_{2}, A_{3}\right\},\left\{A_{5}\right\}\right\}
$$

![img-0.jpeg](img-0.jpeg)

Fig. 1. A graphical representation of the hypergraph $\mathcal{H}=\left\{h_{1}, h_{2}, h_{3}, h_{4}\right\}$.

### 2.2 Relational Databases

In this section, we review the basic concepts of the standard relational database model with emphasis on data dependencies [1], [18]. These relational concepts are extended in the next section to express similar probabilistic concepts and dependencies.

Let $\mathcal{N}=\left\{A_{1}, A_{2}, \ldots, A_{m}\right\}$ be a finite set of attributes (variables). Each attribute $A_{i}$ is associated with a finite set $D_{A_{i}}, 1 \leq i \leq m$, called the domain of $A_{i}$. We define an $\mathcal{N}$-tuple $t$ (or simply a tuple if $\mathcal{N}$ is understood) to be a function from $\mathcal{N}$ to $D_{A_{i}} \cup D_{A_{i}} \cup \ldots \cup D_{A_{m}}$ with the restriction that $t\left[A_{i}\right] \in D_{A_{i}}$ for all $A_{i} \in \mathcal{N}$, where $t\left[A_{i}\right]$ denotes the value obtained by restricting the mapping to $A_{i}$. Thus, a tuple is a mapping that associates a value with each attribute in $\mathcal{N}$, i.e., $t[\mathcal{N}]=\left\langle t\left[A_{1}\right], t\left[A_{2}\right], \ldots, t\left[A_{m}\right]\right\rangle$. If $X \subseteq \mathcal{N}$ and $t$ is a $\mathcal{N}$-tuple, then $t[X]$ denotes the $X$-tuple obtained by restricting the mapping to $X$. A relation over $X$ (or a relation if $X$ is understood) is a finite set of $X$-tuple. We will sometimes find it convenient to add subscripts in denoting a relation and write the relation $r$ over $X$ as $r[X]$.

The relational operators, select, project, and natural join are defined as follows: Let $r$ be a relation over $\mathcal{N}$ with $A \in \mathcal{N}$ and $a$ an element in the domain of $A$, i.e., $a \in D_{A}$. The select operator $\sigma$ is a unary operator on relations. That is, $\sigma_{A=a}(r)=\{t \in r \mid t[A]=a\}$ defines the set of tuples $t$ in $r$ such that $t[A]=a$. The projection of $r[\mathcal{N}]$ onto $X \subseteq \mathcal{N}$ is defined as $r[X]=\{t[X] \mid t \in r[\mathcal{N}]\}$. The natural join of two relations $r_{1}[X]$ and $r_{2}[Y]$ is defined as

$$
r_{1}[X] \bowtie r_{2}[Y]=\left\{t[X Y] \mid t[X] \in r_{1}[X], t[Y] \in r_{2}[Y]\right\}
$$

where we have written $X \cup Y$ as $X Y$.
Let $r[\mathcal{N}]$ be a relation over a set of attributes $\mathcal{N}$ and $X, Y \subseteq \mathcal{N}$. We say that the functional dependency (FD) $X \rightarrow Y$ is satisfied by $r[\mathcal{N}]$ if every two tuples of $r[\mathcal{N}]$ which have the same projection on $X$ also have the same projection on $Y$. That is, an FD $X \rightarrow Y$ is satisfied by $r[\mathcal{N}]$ if and only if each X -value in $r[\mathcal{N}]$ is associated with precisely one Y -value. The FD $X \rightarrow Y$ is a sufficient but not a necessary condition for $r[\mathcal{N}]$ to be written as $r[\mathcal{N}]=r[X Y] \bowtie r[X(\mathcal{N}-X Y)]$.

Let $X, Y, Z \subseteq \mathcal{N}$ such that $Y \cap Z \subseteq X$ and $r[\mathcal{N}]$ a relation over $\mathcal{N}$. We say that the multivalued dependency (MVD), written $X \rightarrow \rightarrow Y \mid Z$, is satisfied by $r[\mathcal{N}]$ if and only if $r[X Y Z]=r[X Y] \bowtie r[X Z]$. The MVD $X \rightarrow \rightarrow Y \mid Z$ is called nonembedded in the special case where $X Y Z=\mathcal{N}$. If $X Y Z \subset \mathcal{N}$, then the MVD $X \rightarrow \rightarrow Y \mid Z$ is called embedded. Suppose the MVD $X \rightarrow Y \mid Z W$ is satisfied by the relation $r[\mathcal{N}]$, where $X, Y, Z$, and $W$ are disjoint subsets of $\mathcal{N}$ (i.e., $r[X Y Z W]=r[X Y] \bowtie r[X Z W])$. Obviously, the

$$
r[\mathcal{N}]=\left|\begin{array}{cccc}
A_{1} & A_{2} & A_{3} & A_{4} \\
0 & 0 & 0 & 0 \\
0 & 0 & 1 & 1 \\
0 & 1 & 0 & 0 \\
0 & 1 & 1 & 0 \\
1 & 1 & 1 & 1
\end{array}\right|
$$

Fig. 2. A relation $r[\mathcal{N}]$ over $N=\left\{A_{1}, A_{2}, A_{3}, A_{4}\right\}$.
MVD $X \rightarrow \rightarrow Y \mid Z$ is satisfied by $r[\mathcal{N}]$, that is, the smaller projection $r[X Y Z]$ of $r[\mathcal{N}]$ onto $X Y Z$ can be written $r[X Y Z]=r[X Y] \bowtie r[X Z]$. However, the converse is not necessarily true. The fact that the MVD $X \rightarrow \rightarrow Y \mid Z$ is satisfied by $r[\mathcal{N}]$ (i.e., $r[X Y Z]=r[X Y] \bowtie r[X Z]$ ) does not necessarily imply that $X \rightarrow Y \mid Z W$ or $X \rightarrow Y W \mid Z$ would be satisfied by $r[\mathcal{N}]$ (i.e., the larger projection $r[X Y Z W]$ can be expressed as $r[X Y Z W]=r[X Y] \bowtie$ $r[X Z W]$ or $r[X Y Z W]=r[X Y W] \bowtie r[X Z])$. For example, it can be verified that the MVD $\left\{A_{1}\right\} \rightarrow \rightarrow\left\{A_{2}\right\} \mid\left\{A_{3}\right\}$ is satisfied by the relation $r[\mathcal{N}]$ over $\mathcal{N}=\left\{A_{1}, A_{2}, A_{3}, A_{4}\right\}$, as shown in Fig. 2, i.e.,

$$
r\left[\left\{A_{1}, A_{2}, A_{3}\right\}\right]=r\left[\left\{A_{1}, A_{2}\right\}\right] \bowtie r\left[\left\{A_{1}, A_{3}\right\}\right]
$$

However, this MVD does not imply that either the MVD $\left\{A_{1}\right\} \rightarrow \rightarrow\left\{A_{2}, A_{4}\right\} \mid\left\{A_{3}\right\}$ or $\left\{A_{1}\right\} \rightarrow \rightarrow\left\{A_{2}\right\} \mid\left\{A_{3}, A_{4}\right\}$ is also satisfied by the relation $r[\mathcal{N}]$, i.e.,

$$
r[\mathcal{N}] \neq r\left[\left\{A_{1}, A_{2}, A_{4}\right\}\right] \bowtie r\left[\left\{A_{1}, A_{3}\right\}\right]
$$

and

$$
r[\mathcal{N}] \neq r\left[\left\{A_{1}, A_{2}\right\}\right] \bowtie r\left[\left\{A_{1}, A_{3}, A_{4}\right\}\right]
$$

The MVD $X \rightarrow \rightarrow Y \mid(\mathcal{N}-X Y)$ is a necessary and sufficient condition for $r[\mathcal{N}]$ to be losslessly decomposed as $r[\mathcal{N}]=r[X Y] \bowtie r[X(\mathcal{N}-X Y)]$. Thereby, the FD $X \rightarrow Y$ logically implies the MVD $X \rightarrow \rightarrow Y \mid(\mathcal{N}-X Y)$, but the converse is not necessarily true.

Multivalued dependency is a special case of a more general kind of data dependency, called join dependency. We say that the join dependency (JD), written $\bowtie \mathcal{H}$, is satisfied by a relation $r[\mathcal{N}]$ if

$$
r[\mathcal{N}]=r\left[h_{1}\right] \bowtie r\left[h_{2}\right] \bowtie \ldots \bowtie r\left[h_{n}\right]
$$

where $h_{i} \subseteq \mathcal{N}$ and $\cup_{i=1}^{n} h_{i}=\mathcal{N}$. The database scheme $\mathcal{H}=$ $\left\{h_{1}, h_{2}, \ldots, h_{n}\right\}$ is in fact a hypergraph. We say that $\bowtie \mathcal{H}$ is an acyclic join dependency (AJD) if $\mathcal{H}$ is an acyclic hypergraph. It has been demonstrated that an AJD has many desirable properties and plays an important role in database design [4].

### 2.3 The Generalized Relational Data Model

We have shown that probabilistic networks can be viewed as a generalization of the standard relational database model [28], [29], [35]. This model is referred to as the generalized relational data model in which probabilistic concepts can be conveniently expressed in familiar relational terminologies. One of the advantages of this unified model is that techniques developed for one particular subdomain can be appropriately modified such that they will become applicable to other subdomains [27], [30], [33], [34], [36], [32].

![img-1.jpeg](img-1.jpeg)

Fig. 3. A joint distribution $\phi_{\mathcal{N}}$ expressed as a relation $\Phi_{\mathcal{N}}$, where $t_{i}\left[f_{\phi_{\mathcal{N}}}\right]=\phi_{\mathcal{N}}\left(t_{i}[\mathcal{N}]\right)$.

Let $\mathcal{N}=\left\{A_{1}, A_{2}, \ldots, A_{m}\right\}$ denote a finite set of variables. A joint probability distribution (jpd) over $\mathcal{N}$, written as $\phi_{\mathcal{N}}$ or $\phi\left(\left\{A_{1}, A_{2}, \ldots, A_{m}\right\}\right)$, is a normalized nonnegative realvalued function. We can express a jpd $\phi_{\mathcal{N}}$ as a generalized relation $\Phi_{\mathcal{N}}$ in our model. The relation $\Phi_{\mathcal{N}}$ is defined by the set of attributes $\left\{A_{1}, A_{2}, \ldots, A_{m}, f_{\phi_{\mathcal{N}}}\right\}$. For convenience, we will say $\Phi_{\mathcal{N}}$ is a relation over $\mathcal{N}=\left\{A_{1}, A_{2}, \ldots, A_{m}\right\}$. It is understood that the attribute $f_{\phi_{\mathcal{N}}}$ is implicitly used for defining the relation $\Phi_{\mathcal{N}}$. Each row in $\Phi_{\mathcal{N}}$ is defined by a tuple $t_{i}$ in a standard relation $r[\mathcal{N}]$, as shown in Fig. 3.

Having defined a joint probability distribution as a generalized relation, we can now define probabilistic operations on distributions as generalized relational operations. Computing the projection of a relation and the natural join of two relations in relational database theory corresponds to computing a marginal distribution and the product of two distributions in probabilistic reasoning theory, respectively.

If $\Phi_{\mathcal{N}}$ is a relation and $X \subseteq \mathcal{N}$, then the marginalization of $\Phi_{\mathcal{N}}$ onto $X$ is the marginal relation, denoted $\Phi_{\mathcal{N}}^{\perp X}$, with attributes $X \cup\left\{f_{\phi_{\mathcal{N}}^{\perp X}}\right\}$, defined by

$$
\begin{aligned}
& \Phi_{\mathcal{N}}^{\perp X}=\left\{t\left[X \cup\left\{f_{\phi_{\mathcal{N}}^{\perp X}}\right\}\right] \mid t[X] \in \Phi_{\mathcal{N}}[X], \text { and }\right. \\
& \left.t\left[f_{\phi_{\mathcal{N}}^{\perp X}}\right]=\phi_{\mathcal{N}}^{\perp X}(t[X])=\sum_{t^{\prime} \in \Phi_{\mathcal{N}}, t^{\prime}[X]=t[X]} \phi_{\mathcal{N}}\left(t^{\prime}[\mathcal{N}]\right)\right\}
\end{aligned}
$$

Note that if $\Phi_{\mathcal{N}}$ is a relation representing a distribution over $\mathcal{N}$ and $X \subseteq Y \subseteq \mathcal{N}$, then $\left(\left(\Phi_{\mathcal{N}}\right)^{\perp Y}\right)^{\perp X}=\Phi_{\mathcal{N}}^{\perp X}$.

Let $\phi_{X}$ and $\phi_{Y}$ be two distributions over $X$ and $Y$, respectively. We can express the product $\phi_{X} \cdot \phi_{Y}$ as the product join $\Phi_{X} \times \Phi_{Y}$ of the corresponding relations $\Phi_{X}$ and $\Phi_{Y}$. That is, $\Phi_{X} \times \Phi_{Y}$ is a relation on the set of attributes $X Y \cup\left\{f_{\phi_{X} \cdot \phi_{Y}}\right\}$ defined as follows:

$$
\begin{aligned}
& \Phi_{X} \times \Phi_{Y}= \\
& \quad\left\{t\left[X Y \cup\left\{f_{\phi_{X} \cdot \phi_{Y}}\right\}\right] \mid t[X Y] \in\left(\Phi_{X}[X] \bowtie \Phi_{Y}[Y]\right), \text { and }\right. \\
& \left.t\left[f_{\phi_{X} \cdot \phi_{Y}}\right]=\phi_{X}(t[X]) \cdot \phi_{Y}(t[Y])\right\}
\end{aligned}
$$

Let $\Phi_{\mathcal{N}}$ be a relation. The inverse of $\Phi_{\mathcal{N}}$ is the inverse relation, denoted $\left(\Phi_{\mathcal{N}}\right)^{-1}$, with attributes $\mathcal{N} \cup\left\{f_{\left(\phi_{\mathcal{N}}\right)^{-1}}\right\}$, defined by

$$
\begin{aligned}
\left(\Phi_{\mathcal{N}}\right)^{-1} & =\left\{t\left[\mathcal{N} \cup\left\{f_{\left(\phi_{\mathcal{N}}\right)^{-1}}\right\}\right] \mid t[\mathcal{N}] \in \Phi_{\mathcal{N}}[\mathcal{N}] \text { and } t\left[f_{\left(\phi_{\mathcal{N}}\right)^{-1}}\right]\right. \\
& =1 / t\left[f_{\phi_{\mathcal{N}}}\right] \text { if } t\left[f_{\phi_{\mathcal{N}}}\right]>0, \text { and } t\left[f_{\left(\phi_{\mathcal{N}}\right)^{-1}}\right] \\
& \left.=t\left[f_{\phi_{\mathcal{N}}}\right] \text { otherwise }\right\}
\end{aligned}
$$

Fig. 4. The relation $\Phi_{\mathcal{N}}$ over $N=\left\{A_{1}, A_{2}, A_{3}, A_{4}\right\}$.

Generalized relational data dependencies can now be introduced using the above generalized operators. The notion of probabilistic conditional independence is used to decompose a joint distribution into two marginal distributions, namely, conditional independence corresponds to MVD in relational database theory.

The fundamental notion of generalized multivalued dependency is introduced first. This generalized data dependency is equivalent to probabilistic conditional independence.

Let $X, Y, Z \subseteq \mathcal{N}$ such that $Y \cap Z \subseteq X$ and $\Phi_{\mathcal{N}}$ a relation over $\mathcal{N}$. We say that the generalized multivalued dependency (GMVD), written

$$
X \Rightarrow \Rightarrow Y \mid Z
$$

is satisfied by the relation $\Phi_{\mathcal{N}}$ if and only if the marginal relation $\Phi_{\mathcal{N}}^{\perp X Y Z}$ of $\Phi_{\mathcal{N}}$ can be factorized as follows:

$$
\Phi_{\mathcal{N}}^{\perp X Y Z}=\Phi_{\mathcal{N}}^{\perp X Y} \otimes \Phi_{\mathcal{N}}^{\perp X Z} \equiv \Phi_{\mathcal{N}}^{\perp X Y} \times \Phi_{\mathcal{N}}^{\perp X Z} \times\left(\Phi_{\mathcal{N}}^{\perp X}\right)^{-1}
$$

We refer to the binary operation $\otimes$ defined above as the generalized join.

Note that it can be shown that

$$
X \Rightarrow \Rightarrow Y \mid Z \text { if and only if } X \Rightarrow \Rightarrow(Y-X) \mid(Z-X)
$$

We distinguish the special case when $X Y Z=\mathcal{N}$ by calling the GMVD $X \Rightarrow \Rightarrow Y \mid Z$ nonembedded. If $X Y Z \subset \mathcal{N}$, then we call the GMVD $X \Rightarrow \Rightarrow Y \mid Z$ embedded. Suppose the GMVD $X \Rightarrow \Rightarrow Y \mid Z W$ is satisfied by the relation $\Phi_{\mathcal{N}}$, where $X, Y, Z$, and $W$ are disjoint subsets of $\mathcal{N}$ (i.e., $\Phi_{\mathcal{N}}^{\perp X Y Z W}=\Phi_{\mathcal{N}}^{\perp X Y} \otimes \Phi_{\mathcal{N}}^{\perp X Z W}$ ). Clearly, the GMVD $X \Rightarrow \Rightarrow Y \mid Z$ is satisfied by $\Phi_{\mathcal{N}}$, that is, the smaller marginal relation $\Phi_{\mathcal{N}}^{\perp X Y Z}$ of $\Phi_{\mathcal{N}}$ onto $X Y Z$ can be written $\Phi_{\mathcal{N}}^{\perp X Y Z}=\Phi_{\mathcal{N}}^{\perp X Y} \otimes \Phi_{\mathcal{N}}^{\perp X Z}$. Similar to MVDs in standard relational databases, however, the converse is not necessarily true. The fact that the GMVD $X \Rightarrow \Rightarrow Y \mid Z$ is satisfied by $\Phi_{\mathcal{N}}$ does not necessarily imply that $X \Rightarrow \Rightarrow Y \mid Z W$ or $X \Rightarrow \Rightarrow Y W \mid Z$ would be satisfied by $\Phi_{\mathcal{N}}$ (i.e., the larger marginal relation $\Phi_{\mathcal{N}}^{\perp X Y Z W}$ may not necessarily be expressed as $\Phi_{\mathcal{N}}^{\perp X Y Z W}=\Phi_{\mathcal{N}}^{\perp X Y} \otimes \Phi_{\mathcal{N}}^{\perp X Z W}$ or $\Phi_{\mathcal{N}}^{\perp X Y Z W}=\Phi_{\mathcal{N}}^{\perp X Y W} \otimes \Phi_{\mathcal{N}}^{\perp X Z}$ ). For example, consider the relation $\Phi_{\mathcal{N}}$ over $\mathcal{N}=\left\{A_{1}, A_{2}, A_{3}, A_{4}\right\}$, as shown in Fig. 4. It can be verified that the GMVD $\left\{A_{1}\right\} \Rightarrow \Rightarrow\left\{A_{2}\right\} \mid\left\{A_{3}\right\}$ is satisfied by $\Phi_{\mathcal{N}}$, i.e., $\Phi_{\mathcal{N}}^{\left|\left\{A_{1}, A_{2}, A_{3}\right\}\right.}=\Phi_{\mathcal{N}}^{\left|\left\{A_{1}, A_{2}\right\}\right|} \otimes \Phi_{\mathcal{N}}^{\left|\left\{A_{1}, A_{3}\right\}\right|}$. However, this GMVD does not imply that either of the GMVDs $\left\{A_{1}\right\} \Rightarrow \Rightarrow$ $\left\{A_{2}, A_{4}\right\} \mid\left\{A_{3}\right\}$ or $\left\{A_{1}\right\} \Rightarrow \Rightarrow\left\{A_{2}\right\} \mid\left\{A_{3}, A_{4}\right\}$ is satisfied by

$\Phi_{\mathcal{N}}$, as can also be verified, i.e., $\Phi_{\mathcal{N}} \neq \Phi_{\mathcal{N}}^{\left\{\left(A_{1}, A_{2}, A_{4}\right\}\right.} \otimes \Phi_{\mathcal{N}}^{\left\{A_{1}, A_{2}\right\}}$ or $\Phi_{\mathcal{N}} \neq \Phi_{\mathcal{N}}^{\left\{A_{1}, A_{2}\right\}} \otimes \Phi_{\mathcal{N}}^{\left\{A_{1}, A_{2}, A_{4}\right\}}$.

Let $\Phi_{\mathcal{N}}$ be a relation representing a joint probability distribution $\phi_{\mathcal{N}}$ over a set of variables $\mathcal{N}$, and $X, Y, Z \subseteq \mathcal{N}$ be disjoint subsets. We say $Y$ and $Z$ are probabilistically conditionally independent given $X$ with respect to $\Phi_{\mathcal{N}}$ if

$$
\left(\Phi_{\mathcal{N}}^{\lfloor Y X Z} \times\left(\Phi_{\mathcal{N}}^{\lfloor X Z}\right)^{-1}\right)^{\lfloor X Y}=\Phi_{\mathcal{N}}^{\lfloor X Y} \times\left(\Phi_{\mathcal{N}}^{\lfloor X}\right)^{-1}
$$

Equivalently, conditional independence can be defined as

$$
\Phi_{\mathcal{N}}^{\lfloor Y X Z}=\Phi_{\mathcal{N}}^{\lfloor X Y} \times \Phi_{\mathcal{N}}^{\lfloor X Z} \times\left(\Phi_{\mathcal{N}}^{\lfloor X}\right)^{-1}
$$

It should be obvious that the definition of probabilistic conditional independence given in (3) is equivalent to stating that the relation $\Phi_{\mathcal{N}}^{\lfloor Y X Z}$ satisfies the GMVD $X \Rightarrow \Rightarrow$ $Y \mid Z$ in (1), namely,

$$
\Phi_{\mathcal{N}}^{\lfloor Y X Z}=\Phi_{\mathcal{N}}^{\lfloor X Y} \otimes \Phi_{\mathcal{N}}^{\lfloor X Z}
$$

One can also verify that (2) and (3) written in our generalized relational data model notation are equivalent, respectively, to the following more familiar definitions of probabilistic conditional independence:

$$
\phi(Y \mid X Z)=\phi(Y \mid X)
$$

and

$$
\phi(Y X Z)=\frac{\phi(Y X) \cdot \phi(X Z)}{\phi(X)}
$$

(Pearl [20] writes the GMVD $X \Rightarrow \Rightarrow Y \mid Z$ as $I(Y, X, Z)$.)
Here, we should perhaps make one observation comparing GMVDs in probabilistic uncertainty management and MVDs in standard relational databases. Consider the relation $\Phi_{\mathcal{N}}$ representing a uniform joint distribution $\phi_{\mathcal{N}}$ (i.e., $t\left[f_{\phi_{\mathcal{N}}}\right]=c$ for all $t$ in $\Phi_{\mathcal{N}}$ ), as shown in Fig. 4. By projecting $\Phi_{\mathcal{N}}$ onto the set of attributes $\mathcal{N}$, we obtain the standard relation $\Phi_{\mathcal{N}}[\mathcal{N}]$ shown in Fig. 2. It has been shown [28] that the nonembedded GMVD $X \Rightarrow \Rightarrow Y \mid Z$ is satisfied by a uniform $\Phi_{\mathcal{N}}$ if and only if the nonembedded MVD $X \rightarrow \rightarrow Y \mid Z$ is satisfied by $\Phi_{\mathcal{N}}[\mathcal{N}]$. This result will be used in a subsequent proof.

We now define the notions of generalized join dependencies in order to express a joint distribution as the product of potentials [11], i.e., probability tables which are not necessarily pairwise consistent. Recall that, in relational database theory, the notion of decomposing a relation into two projections with an MVD was generalized into decomposing a relation into two or more projections with a JD. Probabilistic networks can be expressed as generalized join dependencies in our data model. In particular, it will be shown that a Markov network is equivalent to a generalized relation satisfying a generalized acyclic join dependency.

By the chain rule, a joint probability distribution (jpd) $\phi$ over $\mathcal{N}=\left\{A_{1}, A_{2}, \ldots, A_{m}\right\}$ can always be written as

$$
\begin{aligned}
\phi= & \phi\left(\left\{A_{1}\right\}\right) \cdot \phi\left(\left\{A_{2}\right\} \mid\left\{A_{1}\right\}\right) \\
& \cdot \phi\left(\left\{A_{3}\right\} \mid\left\{A_{1}, A_{2}\right\}\right) \cdot \ldots \cdot \phi\left(\left\{A_{m}\right\} \mid\left\{A_{1}, A_{2}, \ldots, A_{m-1}\right\}\right)
\end{aligned}
$$

The above equation is an identity. However, one can use conditional independencies that are known to hold in the problem domain to obtain a simpler representation of a jpd. For example, consider a jpd $\phi\left(\left\{A_{1}, A_{2}, A_{3}, A_{4}, A_{5}, A_{6}\right\}\right)$ and the following known conditional independencies:

$$
\begin{aligned}
\phi\left(\left\{A_{3}\right\} \mid\left\{A_{1}, A_{2}\right\}\right) & =\phi\left(\left\{A_{3}\right\} \mid\left\{A_{1}\right\}\right) \\
\phi\left(\left\{A_{4}\right\} \mid\left\{A_{1}, A_{2}, A_{3}\right\}\right) & =\phi\left(\left\{A_{4}\right\} \mid\left\{A_{2}, A_{3}\right\}\right) \\
\phi\left(\left\{A_{5}\right\} \mid\left\{A_{1}, A_{2}, A_{3}, A_{4}\right\}\right) & =\phi\left(\left\{A_{5}\right\} \mid\left\{A_{2}, A_{3}\right\}\right) \\
\phi\left(\left\{A_{6}\right\} \mid\left\{A_{1}, A_{2}, A_{3}, A_{4}, A_{5}\right\}\right) & =\phi\left(\left\{A_{6}\right\} \mid\left\{A_{5}\right\}\right)
\end{aligned}
$$

namely, the following GMVDs

$$
\begin{aligned}
& \left\{A_{1}\right\} \Rightarrow \Rightarrow\left\{A_{2}\right\} \mid\left\{A_{3}\right\} \\
& \left\{A_{2}, A_{3}\right\} \Rightarrow \Rightarrow\left\{A_{1}\right\} \mid\left\{A_{4}\right\} \\
& \left\{A_{2}, A_{3}\right\} \Rightarrow \Rightarrow\left\{A_{1}, A_{4}\right\} \mid\left\{A_{5}\right\} \\
& \left\{A_{5}\right\} \Rightarrow \Rightarrow\left\{A_{1}, A_{2}, A_{3}, A_{4}\right\} \mid\left\{A_{6}\right\}
\end{aligned}
$$

Utilizing these conditional independencies, a jpd written using the chain rule can be expressed in a simpler form, namely,

$$
\begin{aligned}
& \phi\left(\left\{A_{1}, A_{2}, A_{3}, A_{4}, A_{5}, A_{6}\right\}\right)= \\
& \phi\left(\left\{A_{1}\right\}\right) \cdot \phi\left(\left\{A_{2}\right\} \mid\left\{A_{1}\right\}\right) \cdot \phi\left(\left\{A_{3}\right\} \mid\left\{A_{1}\right\}\right) \\
& \quad \cdot \phi\left(\left\{A_{4}\right\} \mid\left\{A_{2}, A_{3}\right\}\right) \cdot \phi\left(\left\{A_{5}\right\} \mid\left\{A_{2}, A_{3}\right\}\right) \cdot \phi\left(\left\{A_{6}\right\} \mid\left\{A_{5}\right\}\right)
\end{aligned}
$$

We can represent the dependency structure of this jpd by a DAG, as shown in Fig. 5. This DAG, together with the conditional probability tables $\phi\left(\left\{A_{1}\right\}\right), \phi\left(\left\{A_{2}\right\} \mid\left\{A_{1}\right\}\right)$, $\phi\left(\left\{A_{3}\right\} \mid\left\{A_{1}\right\}\right), \phi\left(\left\{A_{4}\right\} \mid\left\{A_{2}, A_{3}\right\}\right), \phi\left(\left\{A_{5}\right\} \mid\left\{A_{2}, A_{3}\right\}\right)$, and $\phi\left(\left\{A_{6}\right\} \mid\left\{A_{5}\right\}\right)$, defines a Bayesian network. Such a network provides an economical representation of a jpd.

A salient feature of the generalized relational data model is that a jpd can be equivalently expressed as a relation. For example, the jpd $\phi\left(\left\{A_{1}, A_{2}, A_{3}, A_{4}, A_{5}, A_{6}\right\}\right)$ in (6), can be expressed as

$$
\begin{aligned}
\Phi_{\mathcal{N}}= & \Phi_{\left\{A_{1}\right\}} \times \Phi_{\left\{A_{1}, A_{2}\right\}} \times \Phi_{\left\{A_{1}, A_{2}\right\}} \\
& \times \Phi_{\left\{A_{2}, A_{3}, A_{4}\right\}} \times \Phi_{\left\{A_{2}, A_{3}, A_{5}\right\}} \times \Phi_{\left\{A_{5}, A_{6}\right\}}
\end{aligned}
$$

where $\mathcal{N}=\left\{A_{1}, A_{2}, A_{3}, A_{4}, A_{5}, A_{6}\right\}$. The relations $\Phi_{\left\{A_{1}\right\}}$, $\Phi_{\left\{A_{1}, A_{2}\right\}}, \Phi_{\left\{A_{1}, A_{3}\right\}}, \Phi_{\left\{A_{2}, A_{3}, A_{4}\right\}}, \Phi_{\left\{A_{2}, A_{3}, A_{5}\right\}}$, and $\Phi_{\left\{A_{5}, A_{6}\right\}}$ are respectively defined by the conditional probability tables, $\phi\left(\left\{A_{1}\right\}\right), \phi\left(\left\{A_{2}\right\} \mid\left\{A_{1}\right\}\right), \phi\left(\left\{A_{3}\right\} \mid\left\{A_{1}\right\}\right), \phi\left(\left\{A_{4}\right\} \mid\left\{A_{2}, A_{3}\right\}\right)$, $\phi\left(\left\{A_{5}\right\} \mid\left\{A_{2}, A_{3}\right\}\right)$, and $\phi\left(\left\{A_{6}\right\} \mid\left\{A_{5}\right\}\right)$.

To facilitate probabilistic inference, it is useful to transform a Bayesian network into a Markov network. The DAG representing the dependency structure of a Bayesian network can be converted by the moralization and triangulation procedures [11], [20] into an acyclic hypergraph. (An acyclic hypergraph, in fact, represents a chordal undirected graph. Each maximal clique in the graph corresponds to a hyperedge in the acyclic hypergraph.) For example, by applying these procedures to the DAG in Fig. 5, we obtain the acyclic hypergraph depicted in Fig. 1. Such an acyclic hypergraph represents the dependency structure of a Markov network. To define a Markov network, we need

![img-2.jpeg](img-2.jpeg)

Fig. 5. A DAG, the dependency structure of a Bayesian network, representing the conditional independencies in (6).
to specify its potentials. The jpd defined by (6) can be rewritten as:

$$
\Phi_{\mathcal{N}}=\Phi_{\left\{A_{1}, A_{2}, A_{3}\right\}} \times \Phi_{\left\{A_{2}, A_{3}, A_{4}\right\}} \times \Phi_{\left\{A_{2}, A_{3}, A_{5}\right\}} \times \Phi_{\left\{A_{5}, A_{6}\right\}}
$$

where

$$
\Phi_{\left\{A_{1}, A_{2}, A_{3}\right\}} \equiv \Phi_{\left\{A_{1}\right\}} \times \Phi_{\left\{A_{1}, A_{2}\right\}} \times \Phi_{\left\{A_{1}, A_{3}\right\}}
$$

The relations $\Phi_{\left\{A_{1}, A_{2}, A_{3}\right\}}, \Phi_{\left\{A_{2}, A_{3}, A_{4}\right\}}, \Phi_{\left\{A_{2}, A_{3}, A_{5}\right\}}$, and $\Phi_{\left\{A_{5}, A_{6}\right\}}$ are called potentials. These potentials can be transformed into marginal relations of $\Phi_{\mathcal{N}}$. In terms of marginals, we can express $\Phi_{\mathcal{N}}$ as

$$
\begin{aligned}
& \Phi_{\mathcal{N}}= \\
& \left(\left(\left(\Phi_{\mathcal{N}}^{\left\{\left\{A_{1}, A_{2}, A_{3}\right\}\right.\right.} \times \Phi_{\mathcal{N}}^{\left\{\left\{A_{2}, A_{3}, A_{4}\right\}\right.}\right.\right. \times\left(\Phi_{\mathcal{N}}^{\left\{\left\{A_{2}, A_{3}\right\}\right.}\right)^{-1}\right) \times \Phi_{\mathcal{N}}^{\left\{\left\{A_{2}, A_{3}, A_{5}\right\}\right.} \\
& \left.\left.\left.\left.\left.\left.\times \Phi_{\mathcal{N}}^{\left\{\left\{A_{2}, A_{3}\right\}\right.}\right)^{-1}\right)\right) \times \Phi_{\mathcal{N}}^{\left\{\left\{A_{1}, A_{6}\right\}\right.} \times\left(\Phi_{\mathcal{N}}^{\left\{\left\{A_{1}\right\}\right.}\right)^{-1}\right)\right)
\end{aligned}
$$

By the definition of the generalized join operator $\otimes$, (9) can be expressed as:

$$
\begin{aligned}
& \Phi_{\mathcal{N}}= \\
& \left(\left(\Phi_{\mathcal{N}}^{\left\{\left\{A_{1}, A_{2}, A_{3}\right\}\right.} \otimes \Phi_{\mathcal{N}}^{\left\{\left\{A_{2}, A_{3}, A_{4}\right\}\right.}\right) \otimes \Phi_{\mathcal{N}}^{\left\{\left\{A_{2}, A_{3}, A_{5}\right\}}\right) \otimes \Phi_{\mathcal{N}}^{\left\{A_{5}, A_{6}\right\}}\right.
\end{aligned}
$$

In our generalized relational data model, we say that the above $\Phi_{\mathcal{N}}$ satisfies the generalized acyclic join dependency (GAJD) [28], written $\otimes \mathcal{H}=\left\{h_{1}=\left\{A_{1}, A_{2}, A_{3}\right\}\right.$, $\left.h_{2}=\left\{A_{2}, A_{3}, A_{4}\right\}, h_{2}=\left\{A_{2}, A_{3}, A_{5}\right\}, h_{3}=\left\{A_{5}, A_{6}\right\}\right\}$. We call the pair $\left(\Phi_{\mathcal{N}}, \mathcal{H}\right)$ a Markov network, $\Phi_{\mathcal{N}}$ is the relation defined by (10), and $\mathcal{H}$ is the acyclic hypergraph depicted in Fig. 1 representing the dependency structure of the network. In general, we say a GAJD $\otimes \mathcal{H}=\left\{h_{1}, h_{2}, \ldots, h_{n}\right\}$ is satisfied by a relation $\Phi_{\mathcal{N}}$ if $\Phi_{\mathcal{N}}$ can be written as

$$
\Phi_{\mathcal{N}}=\left(\ldots\left(\left(\Phi_{\mathcal{N}}^{\left\{h_{1}\right.} \otimes \Phi_{\mathcal{N}}^{\left\{h_{2}\right.}\right) \otimes \Phi_{\mathcal{N}}^{\left\{h_{5}\right.}\right) \ldots \otimes \Phi_{\mathcal{N}}^{\left\{h_{n}\right.}\right)
$$

where the sequence $h_{1}, h_{2}, \ldots, h_{n}$ is a hypertree construction ordering for $\mathcal{H}$.

A Bayesian network is more expressive than a Markov network. The structure of a Markov network only reflects
![img-3.jpeg](img-3.jpeg)

Fig. 6. The respective DAGs of two agents who wish to form a multiagent system.
nonembedded GMVDs. For instance, in the above example, the embedded GMVD $\left\{A_{1}\right\} \Rightarrow \Rightarrow\left\{A_{2}\right\} \mid\left\{A_{3}\right\}$ is not satisfied by the Markov relation in (10). In contrast, this GMVD is satisfied by the Bayesian relation in (7).

## 3 Related Research

Here, we motivate the need for developing an automated process for constructing the dependency structure of a Markov network. The reason is the inherent difficulty of constructing the dependency structure of a Bayesian network for a multiagent problem domain. As already mentioned, it is not realistic to expect the domain experts to manually construct the dependency structure since the problem domain may be much larger than the single-agent case and, perhaps, distributed. One suggestion would be to learn the dependency structure from observed data. It is not entirely clear, however, how those learning methods [12], [20], [31] developed for the single-agent environment can be applied, let alone obtaining a reliable sample. Thus, constructing the multiagent dependency structure amounts to finding a method to combine the known conditional independency information supplied by the individual domain experts. One previously proposed method [37] constructs the dependency structure of a multiagent Bayesian network. That method verifies whether the dependency structure formed by connecting the individual agent DAGs is acyclic. However, we now demonstrate that the acyclicity condition is too restrictive.

Consider the situation where two agents wish to form a probabilistic multiagent reasoning system. According to [37], each agent supplies a respective DAG, as shown in Fig. 6. It can be easily verified that the combined dependency structure contains the cycle $A_{2} \rightarrow A_{5} \rightarrow A_{2}$. One might wonder, since the same conditional independency may be expressed in a variety of DAGs, if the agents can supply other equivalent DAGs such that the combined dependency structure is in fact a DAG. Our example explicitly demonstrates that this does not always work. DAGs which express precisely the same conditional independencies have the same links and uncoupled head-to-head nodes [26]. By construction, each DAG in Fig. 6 has no other equivalent DAG other than itself. Thus, Xiang's method would state that these two agents cannot form a multiagent system. However, consider the acyclic hypergraphs in Fig. 7, obtained by sacrificing the embedded

![img-4.jpeg](img-4.jpeg)

Fig. 7. The agent dependency structures, reflecting only nonembedded probabilistic conditional independencies, obtained from the respective DAGs in Fig. 6.
probabilistic conditional independencies represented in the respective DAGs in Fig. 6.

The first agent would supply the independency information

$$
\begin{aligned}
& \left\{\left\{A_{2}\right\} \Rightarrow \Rightarrow\left\{A_{1}\right\} \mid\left\{A_{3}, A_{4}, A_{5}, A_{6}\right\}\right. \\
& \left\{A_{2}\right\} \Rightarrow \Rightarrow\left\{A_{3}, A_{4}\right\} \mid\left\{A_{1}, A_{5}, A_{6}\right\} \\
& \left\{A_{2}\right\} \Rightarrow \Rightarrow\left\{A_{5}, A_{6}\right\} \mid\left\{A_{1}, A_{3}, A_{4}\right\}\right\}
\end{aligned}
$$

while the second agents supplies

$$
\begin{aligned}
& \left\{\left\{A_{2}\right\} \Rightarrow \Rightarrow\left\{A_{1}, A_{4}\right\} \mid\left\{A_{3}, A_{5}, A_{6}\right\}\right. \\
& \left\{A_{2}\right\} \Rightarrow \Rightarrow\left\{A_{3}, A_{5}\right\} \mid\left\{A_{1}, A_{4}, A_{6}\right\} \\
& \left\{A_{2}\right\} \Rightarrow \Rightarrow\left\{A_{6}\right\} \mid\left\{A_{1}, A_{3}, A_{4}, A_{5}\right\}\right\}
\end{aligned}
$$

Note that neither agent has knowledge of the GMVD $\left\{A_{2}\right\} \Rightarrow \Rightarrow\left\{A_{3}\right\} \mid\left\{A_{1}, A_{4}, A_{5}, A_{6}\right\}$. Given the combined set of GMVDs, our approach would produce the multiagent dependency structure $\mathcal{H}$ :

$$
\mathcal{H}=\left\{\left\{A_{1}, A_{2}\right\},\left\{A_{2}, A_{3}\right\},\left\{A_{2}, A_{4}\right\},\left\{A_{2}, A_{5}\right\},\left\{A_{2}, A_{6}\right\}\right\}
$$

Note that the GMVD $\left\{A_{2}\right\} \Rightarrow \Rightarrow\left\{A_{3}\right\} \mid\left\{A_{1}, A_{4}, A_{5}, A_{6}\right\}$, which was previously unknown to each agent, can be inferred from the combined multiagent dependency structure $\mathcal{H}$. The important point to realize is that the GMVD $\left\{A_{2}\right\} \Rightarrow \Rightarrow\left\{A_{3}\right\} \mid\left\{A_{1}, A_{4}, A_{5}, A_{6}\right\}$ was logically implied by the combination of the individual domain expert independency information. Thereby, not only would our method allow the agents to form a multiagent system, but our method may detect independencies that are logically implied by the combination of all independencies.

One may also suggest directly constructing a multiagent DAG from an arbitrary input set of probabilistic conditional independencies using Pearl's semigraphoid axioms [20]:


(We express the conditional independence of $Y$ and $Z$ given $X$ by the GMVD $X \Rightarrow \Rightarrow Y \mid Z$. Pearl denotes the same independency by $I(Y, X, Z)$.) Unfortunately, it has been shown [25], [32] that Pearl's semigraphoid axioms are not complete for probabilistic conditional independencies, as incorrectly conjectured by Pearl [20]. In fact, probabilistic conditional independencies have no finite complete axiomatization [25], [32]. That is, the semigraphoid axioms may not derive every conditional independency logically implied by an arbitrary set of probabilistic conditional independencies.

It is well-known [20], however, that the semigraphoid axioms are complete for nonembedded probabilistic conditional independencies. In fact, Geiger and Pearl [10] developed an alternative complete axiomatization for nonembedded probabilistic conditional independencies using only nonembedded inference axioms. In [29], yet another alternative complete axiomatization for nonembedded probabilistic conditional independencies was shown. This complete axiomatization (stated in Section 4.2) directly corresponds to a complete axiomatization for (nonembedded) multivalued dependency (MVD) in relational databases [2]. Therefore, we prefer to use the complete axiomatization in [29] to emphasize the intrinsic relationship between Bayesian networks and relational databases.

## 4 Constructing the Dependency Structure OF A MARKOV NETWORK

Representing probability distributions as relations in the generalized data model enables us to adopt various techniques developed in other areas such as relational databases for probabilistic reasoning systems. In particular, we have demonstrated how a Markov network can be represented as a generalized acyclic join dependency in our model. Furthermore, similar to standard relational databases, there exists a complete axiomatization for nonembedded generalized multivalued dependencies.

Our main goal here is to develop a process for the construction of the dependency structure (an acyclic hypergraph) of a multiagent Markov network. We assume that the input to such a construction process is a set of probabilistic conditional independencies supplied by the different domain experts. We will first outline two problems of such a process caused by redundant and conflicting independency information in the initial input set. A complete set of axioms for nonembedded GMVDs will be subsequently applied to remove redundant and detect inconsistent independency information. The remaining set of GMVDs is used to systematically construct the dependency structure of the desired Markov network. (Note that the resulting acyclic hypergraph is in fact a perfect-map.)

### 4.1 Scheme Design Problems

Given a set $G$ of probabilistic conditional independencies supplied by the individual domain experts over a set $\mathcal{N}$ of attributes, a construction algorithm factorizes $\mathcal{N}$ into two sets of attributes on the basis of a known conditional independency in $G$. That is, given $X Y Z=\mathcal{N}$, the set of attributes $\mathcal{N}$ is replaced by $\mathcal{N} \cap X Y$ and $\mathcal{N} \cap X Z$, where the GMVD $X \Rightarrow$ $\Rightarrow Y \mid Z$ is in $G$. Each of these new subsets may be further factorized on the basis of another known GMVD in $G$. Before formally defining the construction algorithm, let us first highlight two desirable properties such a construction process should satisfy:

1. Every conditional independency provided should contribute in the construction process.
2. A unique dependency structure is constructed.

Unfortunately, without refining the conditional independencies supplied by the individual domain experts, it is not always possible to meet these desirable properties. To illustrate a failure of 1 , consider the set $G$ of GMVDs on $\mathcal{N}=\left\{A_{1}, A_{2}, A_{3}, A_{4}\right\}$ :

$$
\begin{aligned}
G= & \left\{\left\{A_{1}, A_{2}\right\} \Rightarrow \Rightarrow\left\{A_{3}\right\} \mid\left\{A_{4}\right\}\right. \\
& \left.\left\{A_{3}, A_{4}\right\} \Rightarrow \Rightarrow\left\{A_{1}\right\} \mid\left\{A_{2}\right\}\right\}
\end{aligned}
$$

Factorizing $\mathcal{N}$ with the GMVD $\left\{A_{1}, A_{2}\right\} \Rightarrow \Rightarrow\left\{A_{3}\right\} \mid\left\{A_{4}\right\}$ produces the hypergraph $\mathcal{H}=\left\{\left\{A_{1}, A_{2}, A_{3}\right\},\left\{A_{1}, A_{2}, A_{4}\right\}\right\}$. The problem now is that the other GMVD $\left\{A_{3}, A_{4}\right\} \Rightarrow \Rightarrow$ $\left\{A_{1}\right\} \mid\left\{A_{2}\right\}$ in the input set $G$ cannot be applied to refine the dependency structure $\mathcal{H}$. A similar argument holds if the GMVD $\left\{A_{3}, A_{4}\right\} \Rightarrow \Rightarrow\left\{A_{1}\right\} \mid\left\{A_{2}\right\}$ is applied first. To illustrate a failure of Property 2, consider the set $G$ of GMVDs on $\mathcal{N}=\left\{A_{1},, A_{2}, \ldots, A_{7}\right\}$ :

$$
\begin{aligned}
G=\{ & \left\{A_{1}\right\} \Rightarrow \Rightarrow\left\{A_{7}\right\} \mid\left\{A_{2}, A_{3}, A_{4}, A_{5}, A_{6}\right\}, \\
& \left\{A_{1}, A_{2}\right\} \Rightarrow \Rightarrow\left\{A_{4}\right\} \mid\left\{A_{3}, A_{5}, A_{6}, A_{7}\right\}, \\
& \left\{A_{1}, A_{2}\right\} \Rightarrow \Rightarrow\left\{A_{5}\right\} \mid\left\{A_{3}, A_{4}, A_{6}, A_{7}\right\}, \\
& \left\{A_{1}, A_{2}\right\} \Rightarrow \Rightarrow\left\{A_{3}, A_{6}, A_{7}\right\} \mid\left\{A_{4}, A_{5}\right\}, \\
& \left\{A_{1}, A_{3}\right\} \Rightarrow \Rightarrow\left\{A_{4}\right\} \mid\left\{A_{2}, A_{5}, A_{6}, A_{7}\right\}, \\
& \left\{A_{1}, A_{3}\right\} \Rightarrow \Rightarrow\left\{A_{6}\right\} \mid\left\{A_{2}, A_{4}, A_{5}, A_{7}\right\}, \\
& \left\{A_{1}, A_{3}\right\} \Rightarrow \Rightarrow\left\{A_{2}, A_{5}, A_{7}\right\} \mid\left\{A_{4}, A_{6}\right\} \quad\}
\end{aligned}
$$

Factorizing $\mathcal{N}$ with the GMVD

$$
\left\{A_{1}\right\} \Rightarrow \Rightarrow\left\{A_{7}\right\} \mid\left\{A_{2}, A_{3}, A_{4}, A_{5}, A_{6}\right\}
$$

produces the hypergraph $\mathcal{H}_{1}$ :

$$
\mathcal{H}_{1}=\left\{h_{11}=\left\{A_{1}, A_{7}\right\}, h_{12}=\left\{A_{1}, A_{2}, A_{3}, A_{4}, A_{5}, A_{6}\right\}\right\}
$$

The set of attributes $h_{12}=\left\{A_{1}, A_{2}, A_{3}, A_{4}, A_{5}, A_{6}\right\}$ can be further refined with the GMVD

$$
\left\{A_{1}, A_{2}\right\} \Rightarrow \Rightarrow\left\{A_{4}\right\} \mid\left\{A_{3}, A_{5}, A_{6}\right\}
$$

(Sincethe GMVD $\left\{A_{1}, A_{2}\right\} \Rightarrow \Rightarrow\left\{A_{4}\right\} \mid\left\{A_{3}, A_{5}, A_{6}, A_{7}\right\}$ holds on $\mathcal{N}$, then the GMVD $\left\{A_{1}, A_{2}\right\} \Rightarrow \Rightarrow\left\{A_{4}\right\} \mid\left\{A_{3}, A_{5}, A_{6}\right\}$ holds on $\left\{A_{1}, A_{2}, A_{3}, A_{4}, A_{5}, A_{6}\right\}$ (see Section 2.3.)) Factorizing $h_{12}=\left\{A_{1}, A_{2}, A_{3}, A_{4}, A_{5}, A_{6}\right\}$ as such produces the sets $\left\{A_{1}, A_{2}, A_{4}\right\}$ and $\left\{A_{1}, A_{2}, A_{3}, A_{5}, A_{6}\right\}$. The latter can also be factorized using the GMVD $\left\{A_{1}, A_{2}\right\} \Rightarrow \Rightarrow\left\{A_{5}\right\} \mid\left\{A_{3}, A_{6}\right\}$ to produce the new dependency structure $\mathcal{H}_{2}$ :

$$
\begin{aligned}
\mathcal{H}_{2}=\{ & h_{11}=\left\{A_{1}, A_{7}\right\}, h_{21}=\left\{A_{1}, A_{2}, A_{4}\right\}, \\
& h_{22}=\left\{A_{1}, A_{2}, A_{5}\right\}, h_{23}=\left\{A_{1}, A_{2}, A_{3}, A_{6}\right\}\}
\end{aligned}
$$

The set of attributes $h_{23}=\left\{A_{1}, A_{2}, A_{3}, A_{6}\right\}$ can be factorized with the GMVD $\left\{A_{1}, A_{3}\right\} \Rightarrow \Rightarrow\left\{A_{6}\right\} \mid\left\{A_{2}\right\}$ constructing the output dependency structure $\mathcal{H}_{3}$ :

$$
\begin{aligned}
\mathcal{H}_{3}=\{ & h_{11}=\left\{A_{1}, A_{7}\right\}, h_{21}=\left\{A_{1}, A_{2}, A_{4}\right\}, \\
& h_{22}=\left\{A_{1}, A_{2}, A_{5}\right\}, h_{31}=\left\{A_{1}, A_{2}, A_{3}\right\}, \\
& h_{32}=\left\{A_{1}, A_{3}, A_{6}\right\}\}
\end{aligned}
$$

On the other hand, factorizing $h_{12} \in \mathcal{H}_{1}$ with the GMVD $\left\{A_{1}, A_{3}\right\} \Rightarrow \Rightarrow\left\{A_{4}\right\} \mid\left\{A_{2}, A_{5}, A_{6}\right\}$ produces the sets of attributes $\left\{A_{1}, A_{3}, A_{4}\right\}$ and $\left\{A_{1}, A_{2}, A_{3}, A_{5}, A_{6}\right\}$, the latter
of which can be be further factorized with the GMVD $\left\{A_{1}, A_{3}\right\} \Rightarrow \Rightarrow\left\{A_{6}\right\} \mid\left\{A_{2}, A_{5}\right\}$ to produce the dependency structure $\mathcal{H}_{3^{\prime}}$ :

$$
\begin{aligned}
\mathcal{H}_{3^{\prime}}=\{ & h_{11}=\left\{A_{1}, A_{7}\right\}, h_{21^{\prime}}=\left\{A_{1}, A_{3}, A_{4}\right\}, \\
& h_{22^{\prime}}=\left\{A_{1}, A_{3}, A_{6}\right\}, h_{31^{\prime}}=\left\{A_{1}, A_{2}, A_{3}\right\}, \\
& h_{32^{\prime}}=\left\{A_{1}, A_{3}, A_{6}\right\}\}
\end{aligned}
$$

On the other hand, factorizing $h_{12} \in \mathcal{H}_{1}$ with the GMVD $\left\{A_{1}, A_{3}\right\} \Rightarrow \Rightarrow\left\{A_{4}\right\} \mid\left\{A_{2}, A_{5}, A_{6}\right\}$ produces the sets of attributes $\left\{A_{1}, A_{3}, A_{4}\right\}$ and $\left\{A_{1}, A_{2}, A_{3}, A_{5}, A_{6}\right\}$, the latter
of which can be further factorized with the GMVD $\left\{A_{1}, A_{3}\right\} \Rightarrow \Rightarrow\left\{A_{6}\right\} \mid\left\{A_{2}, A_{5}\right\}$ to produce the dependency structure $\mathcal{H}_{3^{\prime}}$ :

$$
\begin{aligned}
\mathcal{H}_{3^{\prime}}=\{ & h_{11}=\left\{A_{1}, A_{7}\right\}, h_{21^{\prime}}=\left\{A_{1}, A_{3}, A_{4}\right\}, \\
& h_{22^{\prime}}=\left\{A_{1}, A_{3}, A_{6}\right\}, h_{31^{\prime}}=\left\{A_{1}, A_{2}, A_{3}\right\}, \\
& h_{32^{\prime}}=\left\{A_{1}, A_{2}, A_{5}\right\}\}
\end{aligned}
$$

Obviously, the output constructed dependency structures $\mathcal{H}_{3}$ and $\mathcal{H}_{3^{\prime}}$ are not the same. The problem, in this case, is that the order in which the GMVDs were applied to factorize $\mathcal{N}$ affected the output dependency structure of the multiagent Markov network.

Another undesirable characteristic can be illustrated by the following example: Let $\mathcal{N}=\left\{A_{1}, A_{2}, A_{3}, A_{4}, A_{5}, A_{6}\right\}$ and $G$ be the set of GMVDs

$$
\begin{aligned}
G= & \left\{\left\{A_{1}\right\} \Rightarrow \Rightarrow\left\{A_{5}\right\} \mid\left\{A_{2}, A_{3}, A_{4}, A_{6}\right\}\right. \\
& \left\{A_{2}\right\} \Rightarrow \Rightarrow\left\{A_{6}\right\} \mid\left\{A_{1}, A_{3}, A_{4}, A_{5}\right\} \\
& \left\{A_{5}, A_{6}\right\} \Rightarrow \Rightarrow\left\{A_{3}\right\} \mid\left\{A_{1}, A_{2}, A_{4}\right\} \\
& \left.\left\{A_{5}, A_{6}\right\} \Rightarrow \Rightarrow\left\{A_{4}\right\} \mid\left\{A_{1}, A_{2}, A_{3}\right\}\right\}
\end{aligned}
$$

Factorizing $\mathcal{N}$ first with the GMVD

$$
\left\{A_{1}\right\} \Rightarrow \Rightarrow\left\{A_{5}\right\} \mid\left\{A_{2}, A_{3}, A_{4}, A_{6}\right\}
$$

followed by the GMVD $\left\{A_{2}\right\} \Rightarrow \Rightarrow\left\{A_{6}\right\} \mid\left\{A_{1}, A_{3}, A_{4}, A_{5}\right\}$ produces the output dependency structure $\mathcal{H}$ :
$\mathcal{H}=$

$$
\left\{h_{11}=\left\{A_{1}, A_{5}\right\}, h_{21}=\left\{A_{1}, A_{2}, A_{3}, A_{4}\right\}, h_{22}=\left\{A_{2}, A_{6}\right\}\right\}
$$

The remaining GMVDs in the input set $G\left\{A_{1}, A_{6}\right\} \Rightarrow \Rightarrow$ $\left\{A_{3}\right\} \mid\left\{A_{1}, A_{2}, A_{4}\right\}$ and $\left\{A_{5}, A_{6}\right\} \Rightarrow \Rightarrow\left\{A_{4}\right\} \mid\left\{A_{1}, A_{2}, A_{3}\right\}$ cannot be applied to factorize any set of attributes in $\mathcal{H}$. The problem here is that $\mathcal{H}$ does not reflect all of the dependency information since $\mathcal{H}$ can be further factorized by the GMVD $\left\{A_{1}, A_{2}\right\} \Rightarrow \Rightarrow\left\{A_{3}\right\} \mid\left\{A_{4}, A_{5}, A_{6}\right\}$ as

$$
\begin{aligned}
\mathcal{H}=\{ & h_{11}=\left\{A_{1}, A_{5}\right\}, h_{22}=\left\{A_{2}, A_{6}\right\} \\
& h_{3}=\left\{A_{1}, A_{2}, A_{3}\right\}, h_{4}=\left\{A_{1}, A_{2}, A_{4}\right\}\}
\end{aligned}
$$

since $G$ logically implies the GMVD

$$
\left\{A_{1}, A_{2}\right\} \Rightarrow \Rightarrow\left\{A_{3}\right\} \mid\left\{A_{4}, A_{5}, A_{6}\right\}
$$

That is, it may be possible to factorize the output dependency structure of the multiagent Markov network with a GMVD $g$ not explicitly stated but logically implied by $G$.

The above problems are the result of redundant and conflicting (inconsistent) conditional independency information in the initial input set. These two problems can be resolved by removing all redundant independencies and, subsequently, identifying any conflicting conditional independencies.

### 4.2 Computing a Dependency Basis

We will consider primarily nonembedded GMVDs referring to a fixed (universal) relation $\Phi_{\mathcal{N}}$ defined on a particular set of attributes $\mathcal{N}$. Thus, to simplify the notation, we may subsequently write $X \Rightarrow \Rightarrow Y \mid \mathcal{N}-X Y$ as $X \Rightarrow \Rightarrow Y$ if no confusion arises.

A set $G$ of GMVDs logically implies the GMVD $X \Rightarrow \Rightarrow Y$, written $G \models X \Rightarrow \Rightarrow Y$, if $X \Rightarrow \Rightarrow Y$ is satisfied by every relation that satisfies all the GMVDs in $G$. That is, $X \Rightarrow \Rightarrow Y$ is logically implied by $G$ if there is no counterexample relation such that all the GMVDs in $G$ are satisfied but $X \Rightarrow$ $\Rightarrow Y$ is not. An inference axiom is a rule that states if a relation $\Phi$ satisfies certain GMVDs, then it must satisfy certain other GMVDs. Given a set $G$ of GMVDs and a set of inference axioms, the closure of $G$, written $G^{+}$, is the smallest set containing $G$ such that the axioms cannot be applied to the set to yield a GMVD not in the set. More specifically, the set $G$ derives a GMVD $X \Rightarrow \Rightarrow Y$, written $G \vdash X \Rightarrow \Rightarrow Y$, if $X \Rightarrow \Rightarrow Y$ is in $G^{+}$. A set of axioms is sound if, whenever $G \vdash X \Rightarrow \Rightarrow Y$, then $G \models X \Rightarrow \Rightarrow Y$. A set of axioms is complete if the converse holds, that is, if $G \models X \Rightarrow \Rightarrow Y$, then $G \vdash X \Rightarrow \Rightarrow Y$. In other words, if $G$ logically implies the GMVD $X \Rightarrow \Rightarrow Y$, then $G$ derives $X \Rightarrow \Rightarrow Y$. A complete set of axioms is minimal if no proper subset of axioms is also complete. A complete minimal set of inference axioms for nonembedded GMVDs is listed below [29] (assume symmetry):

GMVD1: If $Y \subseteq X$, then $X \Rightarrow \Rightarrow Y$; GMVD2: If $X \Rightarrow \Rightarrow Y$ and $Y \Rightarrow \Rightarrow Z$, then $X \Rightarrow \Rightarrow Z-Y$ [reflexivity]
(Strictly speaking, (GMVD1) is an identity and not an inference axiom.) From this minimal set, one can derive additional inference axioms that will be used in subsequent discussions. We obtain

GMVD3: If $Z \subseteq W$ and $X \Rightarrow \Rightarrow Y$, then $W X \Rightarrow \Rightarrow Z Y$; [augmentation]
GMVD4: If $X \Rightarrow \Rightarrow Y$ and $X \Rightarrow \Rightarrow Z$, then $X \Rightarrow \Rightarrow Y Z$; [union]
GMVD5: If $X \Rightarrow \Rightarrow Y$ and $X \Rightarrow \Rightarrow Z$, then $X \Rightarrow \Rightarrow Y \cap Z$, $X \Rightarrow \Rightarrow Y-Z$, and $X \Rightarrow \Rightarrow Z-Y \quad$ [decomposition].

It should be noted that the axioms (GMVD1) and (GMVD2) are different from the semigraphoid axioms. The GMVD axioms are defined only with respect to nonembedded probabilistic conditional independencies. We do not incorporate axioms which mix embedded and nonembedded independencies such as the semigraphoid contraction axiom. (In fact, it has been shown [25], [27] that no finite complete axiomatization exists for both embedded and nonembedded conditional independencies.)

Similarly to the relational database theory [2], [8], it is useful to introduce the notion of a dependency basis. A dependency basis is used to summarize a set of GMVDs
that all have the same lefthand side. Given $X \subseteq \mathcal{N}$, the dependency basis of $X$, written $\operatorname{Dep}(X)$, is defined as follows:

$$
\operatorname{Dep}(X)=\left\{W_{1}, W_{2}, \ldots, W_{m}\right\}
$$

where $X \cap W_{i}=\emptyset$ for $i=1,2, \ldots, m$ and $\left\{W_{1}, W_{2}, \ldots, W_{m}\right\}$ forms a partition of $\mathcal{N}-X$. With this notation, it is understood that the set $\left\{\left\{A_{i}\right\} \mid A_{i} \in X\right\}$ is implicitly included in $\operatorname{Dep}(X)$. The usefulness of introducing $\operatorname{Dep}(X)$ lies in the fact that, for any GMVD $X \Rightarrow \Rightarrow Y$ which is logically implied by an given set $G$ of GMVDs, the set $Y$ is a union of some elements in $\operatorname{Dep}(X)$. That is, if $G \models X \Rightarrow \Rightarrow Y$, then $Y$ is equal to the union of some sets in $\operatorname{Dep}(X)$; whereas, for each nonempty proper subset $W$ of $W_{i}(1 \leq i \leq m)$, the GMVD $X \Rightarrow \Rightarrow W$ is not in $G^{+}$(i.e., $G \not \models X \Rightarrow \Rightarrow W$ ). Sometimes, it is more convenient to express the dependency basis $\operatorname{Dep}(X)$ as in [8], namely,

$$
X \Rightarrow \Rightarrow W_{1}\left|W_{2}\right| \ldots \mid W_{m}
$$

These two notations will be used interchangeably in the following exposition.

We will first present an algorithm to construct the dependency basis for a given $X \subseteq \mathcal{N}$. Beeri [3] originally proposed a polynomial time algorithm to compute the dependency basis for MVDs in relational databases. (Faster algorithms have since been proposed [9], [22].) Here, we adopt Beeri's procedure to our problem by using GMVDs instead of MVDs. Our method is outlined in Algorithm 1 by replacing the complete axiomatization for multivalued dependencies with the complete axiomatization for GMVDs. Given a set $G$ of GMVDs on a set of attributes $\mathcal{N}$ and a set $X \subseteq \mathcal{N}$, Algorithm 1 constructs the dependency basis of $X$ as follows:

## Algorithm 1

procedure Dependency-Basis $(\mathrm{G}, \mathrm{X})$
$\operatorname{Dep}(X)=\{\{A\} \mid A \in\{X\}\} \cup\{\mathcal{N}-X\}$
repeat until $\operatorname{Dep}(X)$ is not changed
\{
for each GMVD $W \Rightarrow \Rightarrow Z$ in $G$
\{
$Y=\cup\{R \mid R \in \operatorname{Dep}(X)$, and $R \cap W \neq \emptyset\}$
$Z^{\prime}=Z-Y$
if $Z^{\prime} \neq \emptyset$ and $Z^{\prime} \neq \cup_{i} R_{i}$, (i.e., if $Z^{\prime}$ is not a union of some $R_{i}^{\prime} s$ in $\operatorname{Dep}(X)$ )
$\{$
$\operatorname{Dep}(X)=\left\{R \left\lvert\, R \in \operatorname{Dep}(X)\right.$ and $\left.R \cap Z^{\prime}=\emptyset\right\} \cup$
$\left\{R \cap Z^{\prime}, R-Z^{\prime}, Z^{\prime}-R \mid R \in \operatorname{Dep}(X)\right.$
and $\left.R \cap Z^{\prime} \neq \emptyset\right\}$
\}
\}
\}
return $(\operatorname{Dep}(X))$
end Dependency - Basis
Let us use an example to demonstrate how Algorithm 1 works.

Example 2. Let $\mathcal{N}=\left\{A_{1}, A_{2}, A_{3}, A_{4}, A_{5}, A_{6}, A_{7}, A_{8}, A_{9}, A_{10}\right\}$.
Let the input set of nonembedded GMVDs be

$$
\begin{aligned}
G= & \left\{\left\{A_{1}, A_{2}\right\} \Rightarrow \Rightarrow\left\{A_{4}, A_{5}, A_{6}, A_{7}\right\}\right. \\
& \left.\left\{A_{3}, A_{7}, A_{10}\right\} \Rightarrow \Rightarrow\left\{A_{1}, A_{4}, A_{8}, A_{9}\right\}\right\}
\end{aligned}
$$

on $\mathcal{N}$. Suppose we want to compute the dependency basis $\operatorname{Dep}(X)$ for the subset $X=\left\{A_{1}, A_{3}, A_{7}, A_{10}\right\} \subseteq \mathcal{N}$. According to the algorithm, we obtain the initial dependency basis:

$$
\begin{aligned}
& \operatorname{Dep}(X)= \\
& \left\{\left\{A_{1}\right\},\left\{A_{3}\right\},\left\{A_{7}\right\},\left\{A_{10}\right\},\left\{A_{2}, A_{4}, A_{5}, A_{6}, A_{8}, A_{9}\right\}\right\}
\end{aligned}
$$

First, we check if the GMVD

$$
\left\{A_{1}, A_{2}\right\}=W \Rightarrow \Rightarrow Z=\left\{A_{4}, A_{5}, A_{6}, A_{7}\right\}
$$

in $G$ can be used to refine $\operatorname{Dep}(X)$. The members $\left\{A_{1}\right\}$ and $\left\{A_{2}, A_{4}, A_{5}, A_{6}, A_{8}, A_{9}\right\}$ in $\operatorname{Dep}(X)$ intersect $W$. Thus,

$$
\begin{aligned}
Y & =\left\{A_{1}\right\} \cup\left\{A_{2}, A_{4}, A_{5}, A_{6}, A_{8}, A_{9}\right\} \\
& =\left\{A_{1}, A_{2}, A_{4}, A_{5}, A_{6}, A_{8}, A_{9}\right\}
\end{aligned}
$$

By (GMVD4), we can immediately conclude
$\left\{A_{1}, A_{3}, A_{7}, A_{10}\right\}=X \Rightarrow \Rightarrow Y=\left\{A_{1}, A_{2}, A_{4}, A_{5}, A_{6}, A_{8}, A_{9}\right\}$.
On the other hand, by (GMVD3), $W \Rightarrow \Rightarrow Z$ implies that:

$$
W \cup\left\{A_{4}, A_{5}, A_{6}, A_{8}, A_{9}\right\} \Rightarrow \Rightarrow Z
$$

namely,

$$
\left\{A_{1}, A_{2}, A_{4}, A_{5}, A_{6}, A_{8}, A_{9}\right\} \Rightarrow \Rightarrow\left\{A_{4}, A_{5}, A_{6}, A_{7}\right\}
$$

By applying (GMVD2) to (12) and (13), we obtain:

$$
\begin{aligned}
\left\{A_{1}, A_{3}, A_{7}, A_{10}\right\}= & X \Rightarrow \Rightarrow Z^{\prime}=Z-Y \\
= & \left\{A_{4}, A_{5}, A_{6}, A_{7}\right\} \\
& -\left\{A_{1}, A_{2}, A_{4}, A_{5}, A_{6}, A_{8}, A_{9}\right\}=\left\{A_{7}\right\}
\end{aligned}
$$

However, the current dependency basis $\operatorname{Dep}(X)$ cannot be refined since $Z^{\prime}=\left\{A_{7}\right\}$ is already an element in $\operatorname{Dep}(X)$.

Next, we consider the GMVD

$$
\left\{A_{3}, A_{7}, A_{10}\right\}=W \Rightarrow \Rightarrow Z=\left\{A_{1}, A_{4}, A_{8}, A_{9}\right\}
$$

in $G$. Then, $Y=\left\{A_{3}\right\} \cup\left\{A_{7}\right\} \cup\left\{A_{10}\right\}=\left\{A_{3}, A_{7}, A_{10}\right\}$, as only $\left\{A_{3}\right\},\left\{A_{7}\right\}$, and $\left\{A_{10}\right\}$ intersect $W$. Thus, by (GMVD4), we have:

$$
\left\{A_{1}, A_{3}, A_{7}, A_{10}\right\}=X \Rightarrow \Rightarrow Y=\left\{A_{3}, A_{7}, A_{10}\right\}
$$

By applying (GMVD2), this GMVD, together with $W \Rightarrow \Rightarrow Z$, implies that:

$$
\begin{aligned}
\left\{A_{1}, A_{3}, A_{7}, A_{10}\right\} & =X \Rightarrow \Rightarrow Z^{\prime}=Z-Y \\
& =\left\{A_{1}, A_{4}, A_{8}, A_{9}\right\}-\left\{A_{3}, A_{7}, A_{10}\right\} \\
& =\left\{A_{1}, A_{4}, A_{8}, A_{9}\right\}
\end{aligned}
$$

Now, (GMVD5) is used to refine the above $\operatorname{Dep}(X)$. From the GMVD
$\left\{A_{1}, A_{3}, A_{7}, A_{10}\right\}=X \Rightarrow \Rightarrow R=\left\{A_{2}, A_{4}, A_{5}, A_{6}, A_{8}, A_{9}\right\}$, already in $\operatorname{Dep}(X)$ and the above GMVD

$$
\left\{A_{1}, A_{3}, A_{7}, A_{10}\right\}=X \Rightarrow \Rightarrow Z^{\prime}=\left\{A_{1}, A_{4}, A_{8}, A_{9}\right\}
$$

it follows:

$$
\begin{aligned}
& \left\{A_{1}, A_{3}, A_{7}, A_{10}\right\}=X \Rightarrow \Rightarrow R \cap Z^{\prime}=\left\{A_{4}, A_{8}, A_{9}\right\} \\
& \left\{A_{1}, A_{3}, A_{7}, A_{10}\right\}=X \Rightarrow \Rightarrow R-Z^{\prime}=\left\{A_{2}, A_{5}, A_{6}\right\} \\
& \left\{A_{1}, A_{3}, A_{7}, A_{10}\right\}=X \Rightarrow \Rightarrow Z^{\prime}-R=\left\{A_{1}\right\}
\end{aligned}
$$

Thus, the new $\operatorname{Dep}(X)$ becomes:

$$
\begin{aligned}
\operatorname{Dep}(X)= & \left\{\left\{A_{3}\right\},\left\{A_{7}\right\},\left\{A_{10}\right\}\right\} \\
& \cup\left\{\left\{A_{1}\right\},\left\{A_{2}, A_{5}, A_{6}\right\},\left\{A_{4}, A_{8}, A_{9}\right\}\right\} \\
= & \left\{\left\{A_{1}\right\},\left\{A_{3}\right\},\left\{A_{7}\right\},\left\{A_{10}\right\},\left\{A_{4}, A_{8}, A_{9}\right\}\right. \\
& \left.\left\{A_{2}, A_{5}, A_{6}\right\}\right\}
\end{aligned}
$$

As the dependency basis has been changed, a second iteration of the repeat until construct is performed. The GMVD

$$
\left\{A_{1}, A_{2}\right\}=W \Rightarrow \Rightarrow Z=\left\{A_{4}, A_{5}, A_{6}, A_{7}\right\}
$$

and $\operatorname{Dep}(X)$ imply that:

$$
Y=\left\{A_{1}\right\} \cup\left\{A_{2}, A_{5}, A_{6}\right\}=\left\{A_{1}, A_{2}, A_{5}, A_{6}\right\}
$$

By (GMVD2) and (GMVD3),

$$
\left\{A_{1}, A_{3}, A_{7}, A_{10}\right\}=X \Rightarrow \Rightarrow Z^{\prime}=Z-Y=\left\{A_{4}, A_{7}\right\}
$$

Hence, $\operatorname{Dep}(X)$ is changed to:

$$
\begin{aligned}
& \operatorname{Dep}(X)= \\
& \left\{\left\{A_{1}\right\},\left\{A_{3}\right\},\left\{A_{7}\right\},\left\{A_{10}\right\},\left\{A_{4}\right\},\left\{A_{8}, A_{9}\right\},\left\{A_{2}, A_{5}, A_{6}\right\}\right\}
\end{aligned}
$$

One can verify that the above $\operatorname{Dep}(X)$ cannot be further refined. $\operatorname{Dep}(X)$ is, therefore, the desired dependency basis for $X=\left\{A_{1}, A_{3}, A_{7}, A_{10}\right\}$ which can be written as

$$
X \Rightarrow \Rightarrow\left\{A_{4}\right\} \mid\left\{A_{8}, A_{9}\right\} \mid\left\{A_{2}, A_{5}, A_{6}\right\}
$$

or

$$
\operatorname{Dep}(X)=\left\{\left\{A_{4}\right\},\left\{A_{8}, A_{9}\right\},\left\{A_{2}, A_{5}, A_{6}\right\}\right\}
$$

Theorem 1. Given a set $G$ of GMVDs on a set of attributes $\mathcal{N}$ and $X \subseteq \mathcal{N}$, Algorithm 1 always terminates and $\operatorname{Dep}(X)$ is the dependency basis of $X$.
Proof. This proof follows the corresponding proof [3] in relational database theory. We will first show that Algorithm 1 always terminates and then demonstrate that $\operatorname{Dep}(X)$ is, in fact, the dependency basis of $X$ given $G$. Notice that, at all times, the value of $\operatorname{Dep}(X)$ is a partition of all the attributes $\mathcal{N}$. Clearly, every iteration of the repeat until construct (except the last) refines the value of $\operatorname{Dep}(X)$. Each refinement increases the number of elements in $\operatorname{Dep}(X)$ by at least one. Therefore, the repeat until construct is executed at most $|\mathcal{N}|$ times.

We now demonstrate that the value of $\operatorname{Dep}(X)$ is independent of the order using the GMVDs of $G$ in

executing the for construct. Given a fixed order of the GMVDs in $G$, consider the constructed value $\operatorname{Dep}(X)$. Let

$$
\operatorname{Dep}(X)=\left\{Y_{1}, Y_{2}, \ldots, Y_{k}, Y_{k+1}, \ldots, Y_{k+|X|}\right\}
$$

where $Y_{1} \cup Y_{2} \cup \ldots \cup Y_{k}=\mathcal{N}-X$ and $Y_{k+1}, \ldots, Y_{k+|X|}$ are singleton sets whose union is $X$. We now demonstrate that if $Y_{i} \in \operatorname{Dep}(X)$, then $X \Rightarrow \Rightarrow Y_{i}$ is in $G^{+}$.

By the reflexivity axiom (GMVD1), $X \Rightarrow \Rightarrow A_{i}$ is in $G^{+}$ for each $A_{i} \in X$. Hence, $X \Rightarrow \Rightarrow X$ is in $G^{+}$and, by the definition of GMVD so is $X \Rightarrow \Rightarrow \mathcal{N}-X$. Thus, for every set $Y$ in the initial value of $\operatorname{Dep}(X), X \Rightarrow \Rightarrow Y$ is in $G^{+}$. We show this claim is true after each iteration by induction on the iterations of the while construct. Suppose the claim is true after $j(j \geq 0)$ iterations of the while construct. Let $W \Rightarrow \Rightarrow Z$ in $G$ be a GMVD used in the $j+1$ iteration and suppose the value of $\operatorname{Dep}(X)$ is changed. Let $Y$ be the union of the sets of $\operatorname{Dep}(X)$ after the $j$ th iteration that intersect $W$. Since $\operatorname{Dep}(X)$ is a partition of $\mathcal{N}$ and $W \subseteq Y$, by (GMVD3) the GMVD $W \Rightarrow \Rightarrow Z$ can be augmented to $Y \Rightarrow \Rightarrow Z$. Applying (GMVD2) to $X \Rightarrow \Rightarrow Y$ and $Y \Rightarrow \Rightarrow Z$, we derive that $X \Rightarrow \Rightarrow Z-Y$ is in $G^{+}$. It easily follows by (GMVD5) that $X \Rightarrow \Rightarrow Y$ is in $G^{+}$for every $Y$ in the value of $\operatorname{Dep}(X)$ after the $j+1$ iteration.

After Algorithm 1 has terminated, $X \Rightarrow \Rightarrow Y$ is in $G^{+}$ for every $Y$ in $\operatorname{Dep}(X)$. Thus, every element of $\operatorname{Dep}(X)$ is a union of the elements of the dependency basis of $X$. To complete the proof that $\operatorname{Dep}(X)$ is in fact equal to the dependency basis of $X$, we now show that each element in the dependency basis of $X$ is a union of the elements of $\operatorname{Dep}(X)$. Equality is then implied since both sets are partitions of $\mathcal{N}$. We shall construct a relation $\Phi_{\mathcal{N}}$ with the following two properties:

1. Every GMVD $W \Rightarrow \Rightarrow Z$ in $G$ is satisfied by $\Phi_{\mathcal{N}}$.
2. A GMVD $X \Rightarrow \Rightarrow Y$ is satisfied by $\Phi_{\mathcal{N}}$ if and only if $Y$ is a union of elements of $\operatorname{Dep}(X)$.
Since every GMVD of $G$ is satisfied by $\Phi_{\mathcal{N}}$, so is every GMVD in $G^{+}$. Hence, for every $Y$ in the dependency basis of $X$, the GMVD $X \Rightarrow \Rightarrow Y$ is satisfied by $\Phi_{\mathcal{N}}$. By Property 2, we can conclude that $\operatorname{Dep}(X)$ is in fact equal to the dependency basis of $X$.

We now construct the relation $\Phi_{\mathcal{N}}$ defined by a distribution $\phi_{\mathcal{N}}$. We assume that each attribute $A_{i} \in \mathcal{N}$ has the domain $\{0,1\}$. The relation $\Phi_{\mathcal{N}}$ has $2^{k}$ rows, one row for each sequence of zeros and ones of length $k$. (Recall that $k$ is the number of sets in $\operatorname{Dep}(X)$ such that $Y_{1} \cup Y_{2} \cup \ldots \cup Y_{k}=\mathcal{N}-X$.) In the row corresponding to a sequence $a_{1}, \ldots, a_{k}$, each of the attributes $Y_{i}$ is assigned the value $a_{i}$, where $a_{i} \in\{0,1\}$ and $i=1,2, \ldots, k$. Each attribute of $X$ is assigned the value 1 in all rows of $\Phi_{\mathcal{N}}$. The attribute $f_{\phi_{\mathcal{N}}}$ is assigned the value $1 /\left(2^{k}\right)$ in all rows of $\Phi_{\mathcal{N}}$.

We now make some observations regarding the constructed relation $\Phi_{\mathcal{N}}$. The GMVD $\emptyset \Rightarrow \Rightarrow Y_{i}$ is satisfied by $\Phi_{\mathcal{N}}(1 \leq i \leq k)$. By (GMVD3), the GMVD $\emptyset \Rightarrow \Rightarrow Y_{i}$ can be augmented to $W \Rightarrow \Rightarrow Y_{i}$ for each set $W \subseteq \mathcal{N}$ and $1 \leq i \leq k$.

Our second observation is that if a set $W$ intersects $Y_{i}$, then the GMVD $W \Rightarrow \Rightarrow V_{i}$ is satisfied by $\Phi_{\mathcal{N}}$ for each $V_{i} \subseteq Y_{i}$. Note that the attributes in $W \cap Y_{i}$ always have
the same value as the rest of the attributes in $Y_{i}$ for every tuple of $\Phi_{\mathcal{N}}$. It follows that the FD $W \rightarrow V_{i}$ is satisfied by the relation $\Phi_{\mathcal{N}}[\mathcal{N}]$, for every $V_{i} \subseteq Y_{i}$. The FD $W \rightarrow V_{i}$ implies the MVD $W \rightarrow \rightarrow V_{i}$ is satisfied by $\Phi_{\mathcal{N}}[\mathcal{N}]$ (see Section 2.2). The MVD $W \rightarrow \rightarrow V_{i}$ implies that the GMVD $W \Rightarrow \Rightarrow V_{i}$ is satisfied by $\Phi_{\mathcal{N}}$ since $\Phi_{\mathcal{N}}$ is a uniform distribution (see Section 2.3).

Our last observation is that if $W$ does not intersect $Y_{i}$, then, for each nonempty proper subset $\bar{Y}_{i}$ of $Y_{i}$, i.e., $\emptyset \subset \bar{Y}_{i} \subset Y_{i}$, the GMVD $W \Rightarrow \Rightarrow \bar{Y}_{i}$ is not satisfied by $\Phi_{\mathcal{N}}$.

We can now show that $\Phi_{\mathcal{N}}$ has Property 1 above. Let $W \Rightarrow \Rightarrow Z$ be in $G$ and let $Y$ be the union of the sets from $\operatorname{Dep}(X)$ that intersect $W$. Since Algorithm 1 has terminated, we know that $Z-Y$ is either empty or a union of some $Y_{i} \in \operatorname{Dep}(X)$. Therefore, $W \Rightarrow \Rightarrow Z-Y$ is satisfied by $\Phi_{\mathcal{N}}$. The fact that $W \Rightarrow \Rightarrow Z \cap Y$ is satisfied by $\Phi_{\mathcal{N}}$ follows easily from our observation that if $W$ intersects some $Y_{i}$, then, for each $\bar{Y}_{i} \subseteq Y_{i}, W \Rightarrow \Rightarrow \bar{Y}_{i}$ is satisfied by $\Phi_{\mathcal{N}}$. Since $W \Rightarrow \Rightarrow Z-Y$ and $W \Rightarrow \Rightarrow Z \cap Y$ are satisfied by $\Phi_{\mathcal{N}}$, by (GMVD4) the GMVD $W \Rightarrow \Rightarrow Z$ is satisfied by $\Phi_{\mathcal{N}}$.

To show Property 2, suppose that the GMVD $X \Rightarrow \Rightarrow Y$ is satisfied by $\Phi_{\mathcal{N}}$. By construction, the GMVD $X \Rightarrow \Rightarrow Y_{i}$ $(1 \leq i \leq k)$ is satisfied by $\Phi_{\mathcal{N}}$. By (GMVD5), the GMVD $X \Rightarrow \Rightarrow Y \cap Y_{i}$ is satisfied by $\Phi_{\mathcal{N}}(1 \leq i \leq k)$. However, since $X$ does not intersect any $Y_{i}$, by observation, the GMVD $X \Rightarrow \Rightarrow Y \cap Y_{i}$ is satisfied by $\Phi_{\mathcal{N}}$ if and only if $Y \cap$ $Y_{i}$ is either empty or equal to $Y_{i}$. Thus, $Y-X$ is a union of some of the $Y_{i} \pi(1 \leq i \leq k)$ and $Y$ is a union of elements of $\operatorname{Dep}(X)$.

The individual domain experts may initially supply redundant and conflicting conditional independency information. Our proposed algorithm for constructing the dependency structure of probabilistic networks requires the input independency information in a more refined format. In particular, all redundant independency information must be removed and the remaining information expressed in terms of its dependency basis. The last task is to identify any conflicting independency information.

The individual domain experts may initially supply a set $G$ of GMVDs containing redundant ones. That is, those GMVDs that can be derived from the rest of the GMVDs in $G$ using the inference axioms (GMVD1) and (GMVD2). We say that a set $G_{1}$ of GMVDs is a cover of $G$ if $G^{+}=G_{1}^{+}$. If a cover $G_{1}$ of $G$ contains no proper subset $G_{2}$ such that $G_{2}$ is also a cover of $G$, i.e., $G^{+}=G_{2}^{+}$, then $G_{1}$ is a minimal cover of $G$. A minimal cover contains no redundant independency information.

We now give a procedure to compute a minimal cover for a given set $G$ of GMVDs supplied by the individual agents. Take any GMVD $g$ in $G$, say, $X \Rightarrow \Rightarrow Y$, and compute $\operatorname{Dep}(X)$ from the set $G-\{g\}$ of GMVDs. If $Y$ is a union of some sets in $\operatorname{Dep}(X)$, i.e., $G-\{g\} \vdash X \Rightarrow \Rightarrow Y$, then remove $g$ from $G$; otherwise, $g$ remains in $G$. Repeat this step for every GMVD in $G$. If we adopt Sagiv's faster algorithm [22] for computing the dependency basis using multivalued dependencies instead of Beeri's [3], a minimum cover of a given set $G$ of GMVDs can be computed in

time $O\left(k^{2}\left|\mathcal{N}^{2}\right|\right)$, where $k$ is the number of GMVDs originally in $G[16]$.

Consider a computed minimum cover $G$ of the collective set of GMVDs supplied by the agents. The left sides of the GMVDs of $G$ are called the keys of $G$. The left set of $G$, written $\mathbf{X}$, is the set of all keys of $G$. A full minimum cover $G_{1}$ is a minimum cover which contains all GMVDs in the dependency basis of $\mathbf{X}$. That is, if the dependency basis of a key $X \in \mathbf{X}$ is $\operatorname{Dep}(X)=\left\{W_{1}, W_{2}, \ldots, W_{m}\right\}$, then $G_{1}$ contains the GMVDs $X \Rightarrow \Rightarrow W_{i}(1 \leq i \leq m)$. A full minimum cover contains no redundant information and is expressed in terms of its dependency basis. For example, given the minimum cover $G$ of a set of GMVDs over $\mathcal{N}=\left\{A_{1}, A_{2}, A_{3}, A_{4}\right\}$ :

$$
\begin{aligned}
G= & \\
& \left\{\left\{A_{1}\right\} \Rightarrow \Rightarrow\left\{A_{2}\right\} \mid\left\{A_{3}, A_{4}\right\},\left\{A_{1}, A_{2}\right\} \Rightarrow \Rightarrow\left\{A_{3}\right\} \mid\left\{A_{4}\right\}\right\}
\end{aligned}
$$

the full minimum cover $G_{1}$ of $G$ is computed by repeatedly applying Algorithm 1 with $G$ and each key in $X$ as input,

$$
\begin{aligned}
G_{1}= & \left\{\operatorname{Dep}\left(\left\{A_{1}\right\}\right)=\left\{\left\{A_{2}\right\},\left\{A_{3}\right\},\left\{A_{4}\right\}\right\}, \operatorname{Dep}\left(\left\{A_{1}, A_{2}\right\}\right)\right. \\
= & \left\{\left\{A_{3}\right\},\left\{A_{4}\right\}\right\}\right\}=\left\{\left\{A_{1}\right\} \Rightarrow \Rightarrow\left\{A_{2}\right\} \mid\left\{A_{3}\right\} \mid\left\{A_{4}\right\}\right. \\
& \left.\left\{A_{1}, A_{2}\right\} \Rightarrow \Rightarrow\left\{A_{3}\right\} \mid\left\{A_{4}\right\}\right\}
\end{aligned}
$$

### 4.3 Conflict-Free Dependencies

A full minimum cover may contain conflicting GMVDs. A conflict-free full minimum cover is derived by removing the conflicting GMVDs from the full minimum cover. This conflict-free full minimum cover is needed to construct the multiagent dependency structure.

The notion of conflict-free multivalued dependencies was originally introduced by Lien [17] in the study of the relationship between various database models. We extend this notion to GMVDs in our generalized relational data model. We say that a GMVD $X \Rightarrow \Rightarrow Y$ splits two attributes $A_{i}$ and $A_{j}$ if one of them is in $Y$ and the other is in $\mathcal{N}-X Y$, where $\mathcal{N}$ is the set of all attributes. A set $G$ of GMVDs splits two attributes $A_{i}$ and $A_{j}$ if some GMVD in $G$ splits them. We then say that a GMVD splits a set $W$ if it splits two attributes in $W$ and that a set $G$ of GMVDs splits a set $W$ if some GMVD in $G$ splits two attributes in $W$. A set $G$ of GMVDs is conflict-free if

1. $G$ does not split its keys and
2. $\operatorname{Dep}(X) \cap \operatorname{Dep}(Y) \subseteq \operatorname{Dep}(X \cap Y)$.

For example, the set of GMVDs in the first example of Section 4.1 violates Condition 1. It can be verified that the GMVDs in the second example of Section 4.1 violate Condition 2.

If conflicting GMVDs are detected, we have to rely on the domain experts to resolve these conflicts. Henceforth, we may assume that a conflict-free full minimum cover has been determined from the GMVDs supplied by the individual domain experts.

As in relational databases [4], conflict-free sets of generalized multivalued dependencies have several nice
properties: 1) They allow a unique Markov network dependency structure and 2) all generalized multivalued dependencies participate in the decomposition process, that is, the phenomenon where decomposing according to one generalized multivalued dependency prevents another generalized multivalued dependency from being applied does not occur. Furthermore, enforcing conflict-freedom should not necessarily be seen as a restriction. On the contrary, it has been argued [23] that if a set of dependencies is not conflict-free, then part of the semantics is not adequately captured.

### 4.4 A Construction Algorithm

Here, we suggest an algorithm (i.e., Algorithm 2) to generate a unique dependency structure (an acyclic hypergraph) from a conflict-free full minimum cover of GMVDs. This algorithm is a modified version of Lien's algorithm [17].

Let $\mathbf{X}$ denote the set of keys in the conflict-free full minimum cover. The keys in $\mathbf{X}$ can be arranged in a p-ordering sequence $\left(X_{1}, X_{2}, \ldots, X_{p}\right)$ such that $X_{i} \subset X_{j}$ implies $i<j$. Given a conflict-free full minimum cover $G$ and a p-ordering sequence $\left(X_{1}, X_{2}, \ldots, X_{p}\right)$ of the keys $\mathbf{X}$ of $G$, Algorithm 2 constructs an acyclic hypergraph representing the dependency structure of the input GMVDs as follows:

## Algorithm 2

procedure Construction $\left(G,\left(X_{1}, X_{2}, \ldots, X_{p}\right)\right)$
$\mathcal{H}^{0}:=\{\mathcal{N}\}$
for $i:=1$ to $p$
\{
$\mathcal{H}^{i-1}:=\mathcal{H}^{i-1}-\left\{h_{j}\right\}$, where $X_{i} \subseteq h_{j} ;$
$\mathcal{H}^{i}:=\mathcal{H}^{i-1} \cup\left\{X_{i} \cup\left(h_{j} \cap W\right) \mid W \in D E P\left(X_{i}\right)\right.$
and $\left.h_{j} \cap W \neq \emptyset\right\} ;$
\}
return $\left(\mathcal{H}^{p}\right)$
end Construction
Example 3. Let $\mathcal{N}=\left\{A_{1}, A_{2}, A_{3}, A_{4}, A_{5}, A_{6}, A_{7}, A_{8}, A_{9}\right\}$ and let $\left(\left\{A_{1}\right\},\left\{A_{2}\right\},\left\{A_{3}\right\},\left\{A_{1}, A_{2}\right\},\left\{A_{1}, A_{3}\right\},\left\{A_{2}, A_{3}\right\}\right)$ be a p-ordering sequence of the keys in the following conflictfree minimum cover $G$ :

$$
\begin{aligned}
G= & \left\{\left\{A_{1}\right\} \Rightarrow \Rightarrow\left\{A_{7}\right\} \mid\left\{A_{2}, A_{3}, A_{4}, A_{5}, A_{6}, A_{8}, A_{9}\right\}\right. \\
& \left\{A_{2}\right\} \Rightarrow \Rightarrow\left\{A_{8}\right\} \mid\left\{A_{1}, A_{3}, A_{4}, A_{5}, A_{6}, A_{7}, A_{9}\right\} \\
& \left\{A_{3}\right\} \Rightarrow \Rightarrow\left\{A_{9}\right\} \mid\left\{A_{1}, A_{2}, A_{4}, A_{5}, A_{6}, A_{7}, A_{8}\right\} \\
& \left\{A_{1}, A_{2}\right\} \Rightarrow \Rightarrow\left\{A_{4}\right\} \mid\left\{A_{7}\right\} \mid\left\{A_{8}\right\} \mid\left\{A_{3}, A_{5}, A_{6}, A_{8}\right\} \\
& \left\{A_{1}, A_{3}\right\} \Rightarrow \Rightarrow\left\{A_{5}\right\} \mid\left\{A_{7}\right\} \mid\left\{A_{9}\right\} \mid\left\{A_{2}, A_{4}, A_{6}, A_{8}\right\} \\
& \left.\left\{A_{2}, A_{3}\right\} \Rightarrow \Rightarrow\left\{A_{6}\right\} \mid\left\{A_{8}\right\} \mid\left\{A_{9}\right\} \mid\left\{A_{1}, A_{4}, A_{5}, A_{7}\right\}\right\}
\end{aligned}
$$

In the initialization step, the dependency structure is $\mathcal{H}^{0}=\left\{\left\{A_{1}, A_{2}, A_{3}, A_{4}, A_{5}, A_{6}, A_{7}, A_{8}, A_{9}\right\}\right\}$. For $i=1$, the hyperedge $h_{j} \in \mathcal{H}^{0}$ is

$$
h_{j}=\left\{A_{1}, A_{2}, A_{3}, A_{4}, A_{5}, A_{6}, A_{7}, A_{8}, A_{9}\right\}
$$

since $X_{1}=\left\{A_{1}\right\} \subseteq\left\{A_{1}, A_{2}, A_{3}, A_{4}, A_{5}, A_{6}, A_{7}, A_{8}, A_{9}\right\}$. The first step removes the hyperedge $h_{j}$ from $\mathcal{H}^{0}$ to obtain $\mathcal{H}^{0}=\{ \}$. The second step adds hyperedges

to construct $\mathcal{H}^{1}$. Since $W=\left\{A_{7}\right\} \in \operatorname{Dep}\left(\left\{A_{1}\right\}\right)$ and $h_{j} \cap\left\{A_{7}\right\} \neq \emptyset$, the hyperedge

$$
X_{1} \cup\left(h_{j} \cap\left\{A_{7}\right\}\right)=\left\{A_{1}, A_{7}\right\}
$$

is added to $\mathcal{H}^{1}$. Similarly, $W=\left\{A_{2}, \ldots, A_{9}\right\} \in \operatorname{Dep}\left(\left\{A_{1}\right\}\right)$ and $h_{j} \cap\left\{A_{2}, \ldots, A_{9}\right\} \neq \emptyset$. Thus,

$$
X_{1}\left(h_{j} \cap W\right)=\left\{A_{1}, \ldots, A_{6}, A_{8}, A_{9}\right\}
$$

is added to $\mathcal{H}^{1}$. Thus, the intermediate dependency structure $\mathcal{H}^{1}$ is

$$
\mathcal{H}^{1}=\left\{\left\{A_{1}, A_{7}\right\},\left\{A_{1}, A_{2}, A_{3}, A_{4}, A_{5}, A_{6}, A_{8}, A_{9}\right\}\right\}
$$

For $i=2$, the hyperedge $h_{j} \in \mathcal{H}^{1}$ is

$$
h_{j}=\left\{A_{1}, \ldots, A_{6}, A_{8}, A_{9}\right\}
$$

since $X_{2}=\left\{A_{2}\right\} \subseteq h_{j}$. The first step removes $h_{j}$ from $\mathcal{H}^{1}$ obtaining $\mathcal{H}^{1}=\left\{\left\{A_{1}, A_{7}\right\}\right\}$. The second step then adds the hyperedges $\left\{A_{2}, A_{8}\right\}$ and $\left\{A_{1}, \ldots, A_{6}, A_{9}\right\}$ to $\mathcal{H}^{1}$ to construct the intermediate dependency structure $\mathcal{H}^{2}$ as follows:

$$
\mathcal{H}^{2}=\left\{\left\{A_{1}, A_{7}\right\},\left\{A_{2}, A_{8}\right\},\left\{A_{1}, A_{2}, A_{3}, A_{4}, A_{5}, A_{6}, A_{9}\right\}\right\}
$$

The subsequent intermediate dependency structures generated by Algorithm 2 are:

$$
\begin{aligned}
\mathcal{H}^{3}= & \left\{\left\{A_{1}, A_{7}\right\},\left\{A_{2}, A_{8}\right\},\left\{A_{3}, A_{9}\right\},\left\{A_{1}, A_{2}, A_{3}, A_{4}, A_{5}, A_{6}\right\}\right\} \\
\mathcal{H}^{4}= & \left\{\left\{A_{1}, A_{7}\right\},\left\{A_{2}, A_{8}\right\},\left\{A_{3}, A_{9}\right\},\left\{A_{1}, A_{2}, A_{4}\right\}\right. \\
& \left.\left\{A_{1}, A_{2}, A_{3}, A_{5}, A_{6}\right\}\right\} \\
\mathcal{H}^{5}= & \left\{\left\{A_{1}, A_{7}\right\},\left\{A_{2}, A_{8}\right\},\left\{A_{3}, A_{9}\right\},\left\{A_{1}, A_{2}, A_{4}\right\}\right. \\
& \left.\left\{A_{1}, A_{3}, A_{5}\right\},\left\{A_{1}, A_{2}, A_{3}, A_{6}\right\}\right\} \\
\mathcal{H}^{6}= & \left\{\left\{A_{1}, A_{7}\right\},\left\{A_{2}, A_{8}\right\},\left\{A_{3}, A_{9}\right\},\left\{A_{1}, A_{2}, A_{4}\right\}\right. \\
& \left.\left\{A_{1}, A_{3}, A_{5}\right\},\left\{A_{2}, A_{3}, A_{6}\right\},\left\{A_{1}, A_{2}, A_{3}\right\}\right\}
\end{aligned}
$$

It can be easily verified that the output $\mathcal{H}=\mathcal{H}^{6}$ is an acyclic hypergraph. A hypertree construction ordering of this scheme is

$$
\begin{aligned}
& h_{1}=\left\{A_{1}, A_{2}, A_{3}\right\}, h_{2}=\left\{A_{1}, A_{2}, A_{4}\right\} \\
& h_{3}=\left\{A_{1}, A_{3}, A_{5}\right\}, h_{4}=\left\{A_{2}, A_{3}, A_{6}\right\} \\
& h_{5}=\left\{A_{1}, A_{7}\right\}, h_{6}=\left\{A_{2}, A_{8}\right\}, h_{7}=\left\{A_{3}, A_{9}\right\}
\end{aligned}
$$

Thus, the J-keys of $\mathcal{H}$ are

$$
\begin{array}{ll}
h_{2} \cap h_{5(2)}=\left\{A_{1}, A_{2}\right\}, & b(2)=1 \\
h_{3} \cap h_{5(3)}=\left\{A_{1}, A_{3}\right\}, & b(3)=1 \\
h_{4} \cap h_{5(4)}=\left\{A_{2}, A_{3}\right\}, & b(4)=1 \\
h_{5} \cap h_{5(5)}=\left\{A_{1}\right\}, & b(5)=2 \\
h_{6} \cap h_{5(6)}=\left\{A_{2}\right\}, & b(6)=4 \\
h_{7} \cap h_{5(7)}=\left\{A_{3}\right\}, & b(7)=3
\end{array}
$$

Algorithm 2 is executed $\mathbf{X}=p$ times. Each iteration $i$ has $W_{i, m_{i}}$ steps, where $\operatorname{Dep}\left(X_{i}\right)$ is

$$
X_{i} \Rightarrow \Rightarrow W_{i, 1}\left|W_{i, 2}\right| \ldots \mid W_{i, m_{i}}
$$

Thus, the computational complexity of Algorithm 2 is $O(|G|)$.

It is worth mentioning that we are not simply using Lien's algorithm [17] with a different kind of independency
as input. Lien's input type is called "MVDs with nulls" (NMVDs) with which some properties of GMVDs (probabilistic conditional independencies) do not hold. In particular, NMVDs have the following two characteristics:

1. For any key $X, \operatorname{Dep}(X)$ can be computed by those NMVDs with a key $Y \subseteq X$.
2. Two logically equivalent minimum covers have the same set of keys $\mathbf{X}$.
Characteristics 1 and 2 do not hold for GMVDs. A counterexample of 1 is given by $G$ in (14). The dependency basis of key $\left\{A_{1}\right\}$ is $\operatorname{Dep}\left(\left\{A_{1}\right\}\right)=\left\{\left\{A_{2}\right\},\left\{A_{3}\right\},\left\{A_{4}\right\}\right\}$, as shown in (15). However, the GMVD $\left\{A_{1}\right\} \Rightarrow \Rightarrow\left\{A_{3}\right\}$ cannot be derived without using the key $\left\{A_{1}, A_{2}\right\} \nsubseteq\left\{A_{1}\right\}$. A counterexample of characteristic 2 is given by consideration of the sets $G_{1}$ and $G_{2}$ of GMVDs over $\mathcal{N}=\left\{A_{1}, A_{2}, A_{3}, A_{4}, A_{5}\right\}$, where

$$
\begin{aligned}
& G_{1}=\left\{\left\{A_{5}\right\} \Rightarrow \Rightarrow\left\{A_{2}\right\},\left\{A_{1}, A_{5}\right\} \Rightarrow \Rightarrow\left\{A_{3}\right\}\right\} \\
& G_{2}=\left\{\left\{A_{5}\right\} \Rightarrow \Rightarrow\left\{A_{2}\right\},\left\{A_{1}, A_{2}, A_{5}\right\} \Rightarrow \Rightarrow\left\{A_{3}\right\}\right\}
\end{aligned}
$$

We have $G_{1}^{+}=G_{2}^{+}$and $G_{1}$ and $G_{2}$ are both minimal covers of $G_{1}^{+}$. However, the keys $\mathbf{X}_{1}$ of $G_{1}$ are not the same as the keys $\mathbf{X}_{2}$ of $G_{2}$, i.e.,

$$
\mathbf{X}_{1}=\left\{\left\{A_{5}\right\},\left\{A_{1}, A_{5}\right\}\right\} \neq \mathbf{X}_{2}=\left\{\left\{A_{5}\right\},\left\{A_{1}, A_{2}, A_{5}\right\}\right\}
$$

Because of the above differences between "MVDs with nulls" and probabilistic conditional independencies, the construction algorithm (Algorithm 2) requires the input set of dependencies in different forms. For applications involving NMVDs, the relational database scheme is constructed from a conflict-free minimum cover. On the other hand, for applications involving conditional independencies, the dependency structure of the probabilistic network is constructed from the more refined conflict-free full minimum cover.

### 4.5 The Relationship between the Constructed Dependency Structure and the Refined Input Set of Dependencies

Our goal now is to demonstrate that the acyclic hypergraph $\mathcal{H}$ constructed as output by Algorithm 2 is a perfect-map of the given input set $G$ of GMVDs. That is, every GMVD logically implied by $G$ can be inferred from $\mathcal{H}$ and every GMVD inferred from $\mathcal{H}$ is logically implied by $G$. If $\mathcal{H}$ is a hypergraph, then the set of GMVDs generated by $\mathcal{H}$ is the set of GMVDs $X \Rightarrow \Rightarrow Y$, where $Y$ is the union of some disconnected components of the hypergraph $\mathcal{H}-X$ obtained from $\mathcal{H}$ by deleting the set $X$ of nodes. That is, $\mathcal{H}-X=$ $\{h-X \mid h$ is a hyperedge of $\mathcal{H}\}-\{\emptyset\}$. We then say that $X$ separates off $Y$ from the rest of the nodes.
Example 4. Consider the acyclic hypergraph $\mathcal{H}$ in Fig. 1. Let $X=\left\{A_{2}, A_{3}\right\}$. The disconnected components of $\mathcal{H}$ obtained by deleting the set $X$ is the set

$$
\mathcal{H}-X=\left\{\left\{A_{1}\right\},\left\{A_{4}\right\},\left\{A_{5}, A_{6}\right\}\right\}
$$

Three GMVDs generated by $\mathcal{H}$ are $\left\{A_{2}, A_{3}\right\} \Rightarrow \Rightarrow\left\{A_{1}\right\}$, $\left\{A_{2}, A_{3}\right\} \Rightarrow \Rightarrow\left\{A_{4}\right\}$, and $\left\{A_{2}, A_{3}\right\} \Rightarrow \Rightarrow\left\{A_{5}, A_{6}\right\}$.

We first turn our attention to relationship between any two keys $X_{i}$ and $X_{k}$ in $\mathbf{X}$. Consider the dependency bases of $X_{i}$ and $X_{k}$
$X_{i} \Rightarrow \Rightarrow W_{i, 1}\left|W_{i, 2}\right| \ldots\left|W_{i, m_{i}-1}\right| W_{i, m_{i}}$,
$X_{k} \Rightarrow \Rightarrow W_{k, 1}\left|W_{k, 2}\right| \ldots\left|W_{k, l}\right| \ldots\left|W_{k, m_{k}-1}\right| W_{k, m_{k}}$.
Case 1. $X_{i}-X_{k} \neq \emptyset$ and $X_{k}-X_{i} \neq \emptyset$. Since keys are not split, we know precisely one $X_{i} W_{i, j}$ contains $X_{k}$. Without loss of generality, we may choose $j=1$, namely,

$$
X_{k} \subseteq X_{i} W_{i, 1}
$$

Applying augmentation on (17), we derive the GMVDs

$$
X_{i} W_{i, 1} \Rightarrow \Rightarrow W_{k, 1}\left|W_{k, 2}\right| \ldots\left|W_{k, m_{k}-1}\right| W_{k, m_{k}}
$$

By transitivity, we obtain:

$$
\begin{gathered}
X_{i} \Rightarrow \Rightarrow W_{k, 1}-X_{i} W_{i, 1} \\
X_{i} \Rightarrow \Rightarrow W_{k, 2}-X_{i} W_{i, 1} \\
\vdots \\
X_{i} \Rightarrow \Rightarrow W_{k, m_{k}-1}-X_{i} W_{i, 1} \\
X_{i} \Rightarrow \Rightarrow W_{k, m_{k}}-X_{i} W_{i, 1}
\end{gathered}
$$

Since $X \Rightarrow \Rightarrow Y$ if and only if $X \Rightarrow \Rightarrow(Y-X)$ (see Section 2.3), (18) can be rewritten as:

$$
\begin{gathered}
X_{i} \Rightarrow \Rightarrow W_{k, 1}-W_{i, 1} \\
X_{i} \Rightarrow \Rightarrow W_{k, 2}-W_{i, 1} \\
\vdots \\
X_{i} \Rightarrow \Rightarrow W_{k, m_{k}-1}-W_{i, 1} \\
X_{i} \Rightarrow \Rightarrow W_{k, m_{k}}-W_{i, 1}
\end{gathered}
$$

Similarly, we also know precisely one $X_{k} W_{k, j}$ contains $X_{i}$. Without loss of generality, we may assume $j=l$, namely,

$$
X_{i} \subseteq X_{k} W_{k, l}
$$

Note that $W_{k, l}$ must contain at least one attribute belonging to $X_{i}$; otherwise, $X_{i} \subseteq X_{k}$ contradicting our initial assumption.

Applying augmentation on (16), we derive the GMVDs

$$
X_{k} W_{k, l} \Rightarrow \Rightarrow W_{i, 1}\left|W_{i, 2}\right| \ldots\left|W_{i, m_{i}-1}\right| W_{i, m_{i}}
$$

Applying transitivity using these GMVDs and (17), we obtain

$$
\begin{gathered}
X_{k} \Rightarrow \Rightarrow W_{i, 1}-X_{k} W_{k, l}=W_{i, 1}-W_{k, l} \\
X_{k} \Rightarrow \Rightarrow W_{i, 2}-X_{k} W_{k, l}=W_{i, 2}-W_{k, l} \\
\vdots \\
X_{k} \Rightarrow \Rightarrow W_{i, m_{i}}-X_{k} W_{k, l}=W_{i, m_{i}}-W_{k, l}
\end{gathered}
$$

We now make some observations which will be used in showing the main result of our paper. (To improve readability, the proofs have been moved to the Appendix.)
Proposition 1. No $W_{k, j}$ in $\operatorname{Dep}\left(X_{k}\right), j \neq l$, partially intersects $W_{i, 1}$.

Proposition 2. If $W_{k, j} \cap W_{i, 1}=\emptyset, j \neq l$, then $W_{k, j}$ must also belong to $\operatorname{Dep}\left(X_{i} \cap X_{k}\right)$.

For notational convenience, let

$$
\operatorname{Dep}^{\prime}\left(X_{i}\right)=\operatorname{Dep}\left(X_{i}\right)-\left\{W_{i, 1}\right\}
$$

Proposition 3. If $W_{i, s}$ in $\operatorname{Dep}^{\prime}\left(X_{i}\right)$ belongs to $\operatorname{Dep}\left(X_{i} \cap X_{k}\right)$, then $W_{i, s}$ must also belong to $\operatorname{Dep}\left(X_{k}\right)$.

The only remaining element in $\operatorname{Dep}\left(X_{k}\right)$ which we have not considered in detail so far is $W_{k, l}$. The following observations are in order:
Proposition 4. $W_{k, l}-X_{i} W_{i, 1} \neq \emptyset$. More specifically,

$$
\begin{aligned}
& W_{k, l}-X_{i} W_{i, 1}= \\
& \quad \cup\left\{W \mid W \in \operatorname{Dep}^{\prime}\left(X_{i}\right) \text { and } W \notin \operatorname{Dep}\left(X_{i} \cap X_{k}\right)\right\}
\end{aligned}
$$

Proposition 5. $X_{i}-X_{k} \neq \emptyset$ and $X_{k}-X_{i} \neq \emptyset$. If $\operatorname{Dep}\left(X_{i}\right)$ and $\operatorname{Dep}\left(X_{k}\right)$ satisfy Propositions 1, 2, 3, and 4, then $\operatorname{Dep}\left(X_{i}\right)$ and $\operatorname{Dep}\left(X_{k}\right)$ cannot be refined.
Case 2. $X_{i} \subseteq X_{k}$. We have the following observations on the elements in $\operatorname{Dep}\left(X_{k}\right)$.
Proposition 6. No $W_{k, j}$ partially intersects $W_{i, 1}$.
Proposition 7. Every $W_{i, s}$ in $\operatorname{Dep}^{\prime}\left(X_{i}\right)$ also belongs to $\operatorname{Dep}\left(X_{k}\right)$.
Proposition 8. If $W_{k, j} \cap W_{i, 1}=\emptyset$, then $W_{k, j}$ is also an element in $\operatorname{Dep}^{\prime}\left(X_{i}\right)$.

Let us now explicitly demonstrate the implications of the above results. Let $X_{i}$ and $X_{k}$ be two keys that are not subsets of each other. Recall the dependency basis of $X_{i}$ and $X_{k}$ in (16) and (17), respectively, where $X_{k} \subseteq X_{i} W_{i, 1}$ and $X_{i} \subseteq X_{k} W_{k, l}$. Since Proposition 1 states that no $W_{k, j}$ in $\operatorname{Dep}\left(X_{k}\right), j \neq l$, partially intersects $W_{i, 1}$, we can rewrite $\operatorname{Dep}\left(X_{k}\right)$ in (17) as

$$
X_{k} \Rightarrow \Rightarrow W_{k, 1}\left|W_{k, 2}\right| \ldots\left|W_{k, l-1}\right| W_{k, l}\left|W_{1}\right| \ldots \mid W_{s}
$$

where $W_{k, j} \cap W_{i, 1}=W_{k, j}, j=1, \ldots, l-1$, and $W_{j} \cap W_{i, 1}=\emptyset$, $j=1, \ldots, s$. By Proposition 2, each element $W_{1}, \ldots, W_{s}$ also belongs to $\operatorname{Dep}\left(X_{i} \cap X_{k}\right)$, i.e., $\left\{W_{1}, \ldots, W_{s}\right\} \subseteq \operatorname{Dep}\left(X_{i} \cap X_{k}\right)$. By Proposition 4, we can write $\operatorname{Dep}\left(X_{i}\right)$ in (16) and $\operatorname{Dep}\left(X_{k}\right)$ in (21) as

$$
X_{i} \Rightarrow \Rightarrow W_{i, 1}\left|W_{i, 2}\right| \ldots\left|W_{i, r}\right| W_{i, r+1}|\ldots| W_{i, m_{i}}
$$

and

$$
\begin{aligned}
& X_{k} \Rightarrow \Rightarrow \\
& W_{k, 1}\left|W_{k, 2}\right| \ldots\left|W_{k, l-1}\right|\left((Z)\left(W_{i, 2} \cdots W_{i, r}\right)\right)\left|W_{1}\right| \ldots \mid W_{s}
\end{aligned}
$$

where $W_{i, j} \notin \operatorname{Dep}\left(X_{i} \cap X_{k}\right)$,

$$
j=2, \ldots, r
$$

and

$$
W_{k, l}=\left((Z)\left(W_{i, 2} \cdots W_{i, r}\right)\right)
$$

Since every element in $\operatorname{Dep}^{\prime}\left(X_{i}\right)$ is either an element in $\operatorname{Dep}\left(X_{i} \cap X_{k}\right)$ or not an element in $\operatorname{Dep}\left(X_{i} \cap X_{k}\right)$, by Proposition 3, the elements $W_{i, r+1}, \ldots, W_{i, m_{i}}$ also belong to $\operatorname{Dep}\left(X_{k}\right)$. This means the elements $W_{i, r+1}, \ldots, W_{i, m_{i}}$ are precisely the elements $W_{1}, \ldots, W_{s}$ in $\operatorname{Dep}\left(X_{k}\right)$. Thus, we rewrite $\operatorname{Dep}\left(X_{i}\right)$ in (24) as

$$
X_{i} \Rightarrow \Rightarrow W_{i, 1}\left|W_{i, 2}\right| \ldots\left|W_{i, r}\right| W_{1}|\ldots| W_{s}
$$

Since $W_{k, j} \cap W_{i, 1}=W_{k, j}, j=1, \ldots, l-1$, we further clarify $\operatorname{Dep}\left(X_{i}\right)$ in (24) as

$$
\begin{aligned}
& X_{i} \Rightarrow \Rightarrow \\
& \left((Y)\left(W_{k, 1} \cdots W_{k, l-1}\right)\right)\left|W_{i, 2}\right| \ldots\left|W_{i, r}\right| W_{1}|\ldots| W_{s}
\end{aligned}
$$

where $W_{i, 1}=\left((Y)\left(W_{k, 1} \cdots W_{k, l-1}\right)\right)$. By substituting for $Y$ in the above equation and $Z$ in (23), we obtain the most detailed description of $\operatorname{Dep}\left(X_{i}\right)$ and $\operatorname{Dep}\left(X_{k}\right)$ :

$$
\begin{aligned}
X_{i} \Rightarrow \Rightarrow & \left(\left(\left(X_{k}-X_{i}\right)(V)\right)\left(W_{k, 1} \cdots W_{k, l-1}\right)\right) \mid \\
& W_{i, 2}|\ldots| W_{i, r}\left|W_{1}\right| \ldots \mid W_{s}
\end{aligned}
$$

and

$$
\begin{aligned}
X_{k} \Rightarrow \Rightarrow & W_{k, 1}\left|W_{k, 2}\right| \ldots\left|W_{k, l-1}\right| \\
& \left(\left(\left(X_{i}-X_{k}\right)(V)\right)\left(W_{i, 2} \cdots W_{i, r}\right)\right)\left|W_{1}\right| \ldots \mid W_{s}
\end{aligned}
$$

where $\left\{W_{1}, \ldots, W_{s}\right\} \subseteq \operatorname{Dep}\left(X_{i} \cap X_{k}\right), Y=\left(\left(X_{k}-X_{i}\right)(V)\right)$, $Z=\left(\left(X_{i}-X_{k}\right)(V)\right)$, and $V$ may be the empty set.

Similarly, in the second case, where $X_{i} \subseteq X_{k}$, by Propositions 6,7 , and $8, \operatorname{Dep}\left(X_{i}\right)$ in (16) and $\operatorname{Dep}\left(X_{k}\right)$ in (17) take the detailed form:

$$
X_{i} \Rightarrow \Rightarrow\left(X_{k}-X_{i}\right)\left(W_{k, 1} \cdots W_{k, l-1}\right)\left|W_{1}\right| \ldots \mid W_{s}
$$

and

$$
X_{k} \Rightarrow \Rightarrow W_{k, 1}\left|W_{k, 2}\right| \ldots\left|W_{k, l-1}\right| W_{1}|\ldots| W_{s}
$$

This completes our analysis of the relationship between any two keys $X_{i}$ and $X_{k}$ in $\mathbf{X}$.

We now focus our attention on the graphical properties of the dependency structure constructed by Algorithm 2.

Recall that $\mathcal{H}^{k-1}$ denotes the intermediate dependency structure constructed after $k-1$ iterations of Algorithm 2. We want to show that $X_{k}$ is a subset of a hyperedge $h$ in $\mathcal{H}^{k-1}$, where

$$
h=X_{1} W_{1,1} \cap X_{2} W_{2,1} \cap \ldots \cap X_{k-1} W_{k-1, m_{k}-1}
$$

and we have assumed that $X_{k} \subseteq X_{j} W_{j, 1}, j=1, \ldots, k-1$.
We first make some observations in the case where the dependency structure $\mathcal{H}^{k-1}$ is a perfect-map of the following GMVDs:

$$
\begin{aligned}
X_{1} \Rightarrow & \Rightarrow W_{1,1}\left|W_{1,2}\right| \ldots \mid W_{1, m_{1}} \\
& \vdots \\
X_{i} \Rightarrow & \Rightarrow W_{i, 1}\left|W_{i, 2}\right| \ldots \mid W_{i, m_{i}} \\
& \vdots \\
X_{k-1} \Rightarrow & \Rightarrow W_{k-1,1}\left|W_{k-1,2}\right| \ldots \mid W_{k-1, m_{k-1}}
\end{aligned}
$$

From the assumption that $\mathcal{H}^{k-1}$ is a perfect-map of (30), $X_{i}$ is a J-key of $\mathcal{H}^{k-1}$ and $X_{i} W_{i, 1}$ is a disconnected component when $X_{i}$ is deleted from $\mathcal{H}^{k-1}$. (The same can be said about all the $X_{i} \mathrm{~s}$ in (30).) Clearly, each $X_{i} W_{i, 1}$ can be characterized by a unique set $\overline{X_{i} W_{i, 1}}$ of hyperedges in $\mathcal{H}^{k-1}$, namely,

$$
\overline{X_{i} W_{i, 1}}=\left\{h \mid h \in \mathcal{H}^{k-1} \text { and } h \cap W_{i, 1} \neq \emptyset\right\}
$$

Proposition 9. $X_{k}$ is a subset of exactly one hyperedge $h$ in $\mathcal{H}^{k-1}$.
Proposition 10. Let $h$ be the hyperedge in $\mathcal{H}^{k-1}$ containing $X_{k}$. Then,

$$
\{h\}=\overline{X_{1} W_{1,1}} \cap \ldots \cap \overline{X_{k-1} W_{k-1,1}}
$$

This concludes our analysis of the graphical properties of the dependency structure constructed by Algorithm 2. In Propositions 1-6, we proved a number of axiomatic properties for $\operatorname{Dep}\left(X_{k}\right)$ based on the fact that we are given a conflict-free full minimum cover. Before stating the main result of this paper, we need to derive one additional property about $\operatorname{Dep}\left(X_{k}\right)$ using the graphical properties in Propositions 9 and 10.

Recall that

$$
\overline{X_{i} W_{i, 1}}=\left\{h \mid h \in \mathcal{H}^{k-1} \text { and } h \cap W_{i, 1} \neq \emptyset\right\}
$$

and from Proposition 10,

$$
\{h\}=\overline{X_{1} W_{1,1}} \cap \ldots \cap \overline{X_{k-1} W_{k-1,1}}
$$

Since

$$
X_{i} W_{i, 1}=\cup_{h \in \overline{X_{i} W_{i, 1}}} h
$$

it follows that $X_{k} \subseteq h$, where

$$
h=X_{1} W_{1,1} \cap \ldots \cap X_{k-1} W_{k-1,1}
$$

We are now ready to state the main result of this paper.
Theorem 2. The dependency structure $\mathcal{H}^{k}$ constructed from Algorithm 2 is a perfect-map of the GMVDs

$$
\begin{aligned}
X_{1} \Rightarrow & \Rightarrow W_{1,1}\left|W_{1,2}\right| \ldots \mid W_{1, m_{1}} \\
& \vdots \\
X_{i} \Rightarrow & \Rightarrow W_{i, 1}\left|W_{i, 2}\right| \ldots \mid W_{i, m_{i}} \\
& \vdots \\
X_{k-1} \Rightarrow & \Rightarrow W_{k-1,1}\left|W_{k-1,2}\right| \ldots \mid W_{k-1, m_{k-1}} \\
X_{k} \Rightarrow & \Rightarrow W_{k, 1}\left|W_{k, 2}\right| \ldots \mid W_{k, m_{k}}
\end{aligned}
$$

Proof. We will prove this claim by induction.
Basic step. $h=\{\mathcal{N}\}$,

$$
X_{1} \Rightarrow \Rightarrow W_{1,1}\left|W_{1,2}\right| \ldots \mid W_{1, m_{1}}
$$

Obviously, $\mathcal{H}^{1}$ is a perfect-map for the above GMVDs and $X_{1}$ is the J-key of $\mathcal{H}^{1}$. Inductive hypothesis: $\mathcal{H}^{k-1}$ is a perfect-map for (30) and $X_{1}, X_{2}, \ldots, X_{k-1}$ are the J-keys of $\mathcal{H}^{k-1}$.

Based on previous discussions, we have the following observations: Proposition 9 states there exists one and only one hyperedge $h \in \mathcal{H}^{k-1}$ that contains $X_{k}$. Proposition 10 indicates that this hyperedge $h$ can be expressed as:

$$
h=X_{1} W_{1,1} \cap \ldots \cap X_{k-1} W_{k-1,1}=\cap_{i=1}^{k-1} X_{i} W_{i, 1}
$$

We have shown in Proposition 7 that

$$
\operatorname{Dep}^{\prime}\left(X_{i} \cap X_{k}\right) \subseteq \operatorname{Dep}\left(X_{k}\right)
$$

for $i=1, \ldots, k-1$. Since $W_{i, 1}$ and $\operatorname{Dep}^{\prime}\left(X_{i} \cap X_{k}\right)$ are disjoint,
$\left(\cap_{i=1}^{k-1} X_{i} W_{i, 1}\right) \cap\left(\cup_{i=1}^{k-1}\left(\cup\left\{W \mid W \in \operatorname{Dep}^{\prime}\left(X_{i} \cap X_{k}\right)\right\}\right)\right)=\emptyset$.
By definition, $h=\cap_{i=1}^{k-1} X_{i} W_{i, 1}$ and, thereby,

$$
h \cap\left(\cup_{i=1}^{k-1}\left(\cup\left\{W \mid W \in \operatorname{Dep}^{\prime}\left(X_{i} \cap X_{k}\right)\right\}\right)\right)=\emptyset
$$

On the other hand, we have shown in Proposition 2 that each $X_{i} W_{i, 1}$ has a nonempty intersection with every element in

$$
D \equiv \operatorname{Dep}\left(X_{k}\right)-\operatorname{Dep}^{\prime}\left(X_{i}\right), i=1, \ldots, k-1
$$

Thus, $h$ has a nonempty intersection with every $W_{k, j} \in D$.
As a result of applying the dependencies,

$$
X_{k} \Rightarrow \Rightarrow W_{k, 1}\left|W_{k, 2}\right| \ldots \mid W_{k, m_{k}}
$$

to the hypergraph $\mathcal{H}^{k-1}$, we obtain the hypergraph $\mathcal{H}^{k}$ which contains the following new hyperedges from $h$ :

$$
\left\{h_{k, j}=X_{k}\left(h \cap W_{k, j}\right) \mid W_{k, j} \in D\right\}
$$

Obviously, $\mathcal{H}^{k}$ is an acyclic hypergraph if $\mathcal{H}^{k-1}$ is acyclic. Moreover, $X_{1}, X_{2}, \ldots, X_{k-1}$ are J-keys of $\mathcal{H}^{k}$ and, when $X_{i}(1 \leq i \leq k-1)$ is deleted from $\mathcal{H}^{k}$, the disconnected components of $X_{i}$ are the same as those when $X_{i}$ is deleted from $\mathcal{H}^{k-1}$.

For every $W_{k, j} \in D$ such that $X_{k} W_{k, j}$ does not contain any key,

$$
h \cap W_{k, j}=W_{k, j}
$$

Whenever $X_{k} W_{k, j}$ contains some key(s), $W_{k, j} \in D$, then $W_{k, j}$ contains all the hyperedges in

$$
\cup_{i=1}^{k-1}\left(\operatorname{Dep}^{\prime}\left(X_{i}\right)-\operatorname{Dep}^{\prime}\left(X_{i} \cap X_{k}\right)\right)
$$

Obviously, every hyperedge in $\mathcal{H}^{k-1}$ must be connected to $h$ through some key(s) in $h$. In particular, every hyperedge in (33) is connected to $h$ by some key(s) in $h$. It immediately follows that all attributes in $h-W_{k, j}$ are
connected to all attributes in $h \cap W_{k, j}$ by some key(s) in $h$. In other words, all the attributes in $W_{k, j}$ will comprise one and only one disconnected component when $X_{k}$ is deleted from $\mathcal{H}^{k}$. We can immediately conclude that, when $X_{k}$ is deleted from $\mathcal{H}^{k}$, the resulting disconnected components are exactly equal to the elements in $\operatorname{Dep}\left(X_{k}\right)$. By the inductive hypothesis that $\mathcal{H}^{k-1}$ is a perfect-map for (30), it immediately follows that $\mathcal{H}^{k}$ is a perfect-map for (31).
We now show that a conflict-free full minimum cover $G$ has a unique dependency structure $\mathcal{H}$. Let $q=$ $\left(X_{1}, X_{2}, \ldots, X_{k}, X_{l}, \ldots, X_{p}\right)$ be a p-ordering sequence of the keys $\mathbf{X}$ of $G$. If two keys $X_{k}$ and $X_{l}$ are not subsets of each other, then $q=\left(X_{1}, X_{2}, \ldots, X_{l}, X_{k}, \ldots, X_{p}\right)$ is also a valid p-ordering sequence. We say that $q^{\prime}$ is obtained from $q$ by a 2-permutation [17], namely, by permuting a neighboring pair of keys which are not subsets of each other.

Let $\mathbf{X}$ be the keys of a conflict-free full minimum cover $G$. We write $\mathcal{H}_{q}$ to denote the dependency structure constructed as output by Algorithm 2 using $G$ with p-ordering sequence $q$.
Lemma 1. Let $G$ be a conflict-free full minimum cover and $q=$ $\left(X_{1}, X_{2}, \ldots, X_{k-1}, X_{k}, X_{l}, \ldots, X_{p}\right)$ be a p-ordering sequence of the keys $X$ of $G$. Let $q^{\prime}=\left(X_{1}, X_{2}, \ldots, X_{k-1}, X_{l}, X_{k}, \ldots, X_{p}\right)$ be another p-ordering sequence obtained from $q$ by a 2-permutation. Then, $\mathcal{H}_{q}=\mathcal{H}_{q^{\prime}}$.
Proof. Let $\mathcal{H}^{k-1}$ be the intermediate dependency structure constructed by Algorithm 2 after $k-1$ iterations. If $X_{k}$ and $X_{l}$ are contained in distinct hyperedges of $\mathcal{H}^{k-1}$, then the claim follows trivially. Suppose $X_{k}$ and $X_{l}$ are contained in the same hyperedge $h \in \mathcal{H}^{k-1}$. Recall that Propositions 1-5 explicitly state the form that $\operatorname{Dep}\left(X_{k}\right)$ and $\operatorname{Dep}\left(X_{l}\right)$ have in relationship to each other. That is,
$X_{k} \Rightarrow \Rightarrow$
$W_{1}|\ldots| W_{s}\left|W_{k, 1}\right| \ldots \mid W_{k, i} \mid\left(X_{l}-X_{k}\right)(Z)\left(W_{l, 1} \cdots W_{l, j}\right)$
and
$X_{l} \Rightarrow \Rightarrow$
$W_{1}|\ldots| W_{s}\left|W_{l, 1}\right| \ldots \mid W_{l, j} \mid\left(X_{k}-X_{l}\right)(Z)\left(W_{k, 1} \cdots W_{k, i}\right)$,
where each $W_{1}, \ldots, W_{s}$ is in $\operatorname{Dep}\left(X_{k} \cap X_{l}\right)$ and $Z$ may be empty.

Suppose $q$ is the p-ordering sequence used. Obviously, $W_{1} \cdots W_{s} \cap h=\emptyset$. By definition, $h \in \mathcal{H}^{k-1}$ is replaced with the hyperedges

$$
\begin{aligned}
h_{1} & =X_{k}\left(W_{k, 1} \cap h\right) \\
h_{2} & =X_{k}\left(W_{k, 2} \cap h\right) \\
& \vdots \\
h_{i} & =X_{k}\left(W_{k, i} \cap h\right) \\
h_{i+1} & =X_{k}\left(\left(\left(X_{l}-X_{k}\right)(Z)\left(W_{l, 1} \cdots W_{l, j}\right)\right) \cap h\right) \\
& =\left(X_{k} X_{l} Z\right)\left(W_{l, 1} \cdots W_{l, j}\right) \cap h
\end{aligned}
$$

Now, $X_{i} \subseteq h_{i+1} \in \mathcal{H}^{k}$. By definition, $h_{i+1}$ is replaced with the hyperedges

$$
\begin{aligned}
h_{1}^{\prime} & =X_{l}\left(W_{l, 1} \cap h_{i+1}\right) \\
h_{2}^{\prime} & =X_{l}\left(W_{l, 2} \cap h_{i+1}\right) \\
& \vdots \\
h_{j}^{\prime} & =X_{l}\left(W_{l, j} \cap h_{i+1}\right) \\
h_{j+1}^{\prime} & =X_{l}\left(\left(\left(X_{k}-X_{l}\right)(Z)\left(W_{k, 1} \cdots W_{k, i}\right)\right) \cap h_{i+1}\right) \\
& =\left(X_{l} X_{k} Z\right)\left(W_{k, 1} \cdots W_{k, i}\right) \cap h_{i+1}\right) \\
& =\left(X_{l} X_{k} Z\right)\left(W_{k, 1} \cdots W_{k, i}\right) \cap\left(X_{k} X_{l} Z\right)\left(W_{l, 1} \cdots W_{l, j}\right) \cap h \\
& =\left(X_{l} X_{k} Z\right) \cap h
\end{aligned}
$$

Thus, $h \in \mathcal{H}^{k-1}$ is replaced with the set of hyperedges

$$
h_{1}, h_{2}, \ldots, h_{i}, h_{1}^{\prime}, h_{2}^{\prime}, \ldots, h_{j}^{\prime},\left(X_{l} X_{k} Z\right) \cap h
$$

in $\mathcal{H}^{k+1}$.
Now suppose, on the other hand, that $q^{\prime}$ is the p-ordering used in Algorithm 2. We will show that the intermediate constructed dependency structure $\mathcal{H}^{k+1}$ is the same. By definition, $h \in \mathcal{H}^{k-1}$ is replaced with the hyperedges

$$
\begin{aligned}
h_{1}^{\prime} & =X_{l}\left(W_{l, 1} \cap h\right) \\
h_{2}^{\prime} & =X_{l}\left(W_{l, 2} \cap h\right) \\
& \vdots \\
h_{j}^{\prime} & =X_{l}\left(W_{l, j} \cap h\right) \\
h_{j+1}^{\prime} & =X_{l}\left(\left(\left(X_{k}-X_{l}\right)(Z)\left(W_{k, 1} \cdots W_{k, i}\right)\right) \cap h\right) \\
& =\left(X_{l} X_{k} Z\right)\left(W_{k, 1} \cdots W_{k, i}\right) \cap h
\end{aligned}
$$

Now, $X_{k} \subseteq h_{j+1}^{\prime} \in \mathcal{H}^{k}$. By definition, $h_{j+1}^{\prime}$ is replaced with the hyperedges

$$
\begin{aligned}
h_{1} & =X_{k}\left(W_{k, 1} \cap h_{j+1}^{\prime}\right) \\
h_{2} & =X_{k}\left(W_{k, 2} \cap h_{j+1}^{\prime}\right) \\
& \vdots \\
h_{i} & =X_{k}\left(W_{k, i} \cap h_{j+1}^{\prime}\right) \\
h_{i+1} & =X_{k}\left(\left(\left(X_{l}-X_{k}\right)(Z)\left(W_{l, 1} \cdots W_{l, j}\right)\right) \cap h_{j+1}^{\prime}\right) \\
& =\left(X_{k} X_{l} Z\right)\left(W_{l, 1} \cdots W_{l, j}\right) \cap h_{j+1}^{\prime} \\
& =\left(X_{k} X_{l} Z\right)\left(W_{l, 1} \cdots W_{l, j}\right) \cap\left(X_{l} X_{k} Z\right)\left(W_{k, 1} \cdots W_{k, i}\right) \cap h \\
& =\left(X_{k} X_{l} Z\right) \cap h
\end{aligned}
$$

Thus, $h \in \mathcal{H}^{k-1}$ is replaced with the set of hyperedges

$$
h_{1}^{\prime}, h_{2}^{\prime}, \ldots, h_{j}^{\prime}, h_{1}, h_{2}, \ldots, h_{i},\left(X_{k} X_{l} Z\right) \cap h
$$

in $\mathcal{H}^{k+1}$.
The desired result is obtained since (34) is identical to (35).
Theorem 3. A conflict-free full minimum cover $G$ has a unique dependency structure. That is, the particular p-ordering sequence used in Algorithm 2 is immaterial.
Proof. We show by induction that any valid p-ordering can be transformed into any other valid p-ordering
sequence through a series of 2-permutations. Let $q=$ $\left(X_{1}, X_{2}, \ldots, X_{p}\right)$ be any valid p-ordering sequence of the keys $\mathbf{X}$ of a conflict-free full minimum cover. Obviously, any valid p-ordering sequence with two keys in $q$ transputed can be obtained from $q$ by a 2-permutation. Suppose $q_{k}$ is any valid p-ordering sequence obtainable from $q$ by $k 2$-permutations. Let $q_{k+1}$ be any valid p-ordering sequence with two keys in $q_{k}$ transmuted. By definition, $q_{k+1}$ can be obtained from $q_{k}$ by a 2-permutation. It easily follows that $q_{k+1}$ is obtainable from $q$ by $k+12$-permutations. Lemma 1 demonstrates that if two neighboring keys $X_{k}$ and $X_{l}$ are not subsets of each other, then they can be interchanged in the p-ordering sequence without affecting the output dependency structure $\mathcal{H}$. Thus, the constructed dependency structure $\mathcal{H}_{q}$ is identical to $\mathcal{H}_{q_{k+1}}$.

## 5 Refining the Dependency Structure Using the Mixture of Nonembedded and Embedded INDEPENDENCIES

In this section, we outline how the constructed dependency structure can be refined using the embedded independency information supplied by the domain experts. This process will utilize the fact that the GMVD axioms are not only complete for nonembedded GMVDs, but are, in fact, complete for deriving all embedded GMVDs from other embedded GMVDs as long as the embedded GMVDs are defined over the same fixed set of attributes. The contraction axiom (SG4) can then be applied to derive GMVDs logically implied by other GMVDs defined over a mixed set of attributes.

Let $G$ be a set of all GMVDs (not necessarily nonembedded) over the set $\mathcal{N}$ of all attributes in the multiagent problem domain supplied by the individual domain experts. For every GMVD $X \Rightarrow \Rightarrow Y \mid Z$ in $G$, construct the set $G_{X Y Z}$ of nonembedded GMVDs over the fixed context $X Y Z$ as follows:

$$
\begin{aligned}
& G_{X Y Z}= \\
& \quad\{X \Rightarrow \Rightarrow Y \mid Z \mid X \Rightarrow \Rightarrow V \mid W \text { in } G, \text { and } Y \subseteq V, Z \subseteq W\}
\end{aligned}
$$

For example, consider the set $G$ of GMVDs over $\mathcal{N}=$ $\left\{A_{1}, A_{2}, A_{3}, A_{4}\right\}$

$$
G=\left\{\left\{A_{2}\right\} \Rightarrow \Rightarrow\left\{A_{1}\right\} \mid\left\{A_{3}\right\},\left\{A_{2}, A_{3}\right\} \Rightarrow \Rightarrow\left\{A_{1}\right\} \mid\left\{A_{4}\right\}\right\}
$$

We then construct the sets $G_{\left\{A_{1}, A_{2}, A_{3}\right\}}$ and $G_{\left\{A_{1}, A_{2}, A_{3}, A_{4}\right\}}$ of respective nonembedded GMVDs as follows:

$$
G_{\left\{A_{1}, A_{2}, A_{3}\right\}}=\left\{\left\{A_{2}\right\} \Rightarrow \Rightarrow\left\{A_{1}\right\} \mid\left\{A_{3}\right\},\left\{A_{2}, A_{3}\right\} \Rightarrow \Rightarrow\left\{A_{1}\right\}\right\}
$$

and

$$
G_{\left\{A_{1}, A_{2}, A_{3}, A_{4}\right\}}=\left\{\left\{A_{2}, A_{3}\right\} \Rightarrow \Rightarrow\left\{A_{1}\right\} \mid\left\{A_{4}\right\}\right\}
$$

We apply the process described in Section 4 to remove redundancy, detect inconsistency, and compute a conflictfree full minimum cover, written $G_{X Y Z}^{\prime}$, for each $G_{X Y Z}$ above. This set of conflict-free full minimum covers reflects

all logically implied conditional independency information for each fixed $X Y Z \subset \mathcal{N}$. For the sets $G_{\left\{A_{1}, A_{2}, A_{3}\right\}}$ and $G_{\left\{A_{1}, A_{2}, A_{3}, A_{4}\right\}}$ of nonembedded GMVDs in (36) and (37), the respective conflict-free full minimum covers are

$$
G_{\left\{A_{1}, A_{2}, A_{3}\right\}}^{c}=\left\{D e p\left(\left\{A_{2}\right\}\right)=\left\{\left\{A_{1}\right\},\left\{A_{3}\right\}\right\}\right\}
$$

and

$$
G_{\left\{A_{1}, A_{2}, A_{3}, A_{4}\right\}}^{c}=\left\{D e p\left(\left\{A_{2}, A_{3}\right\}\right)=\left\{\left\{A_{1}\right\},\left\{A_{4}\right\}\right\}\right\}
$$

The contraction axiom (SG4) is now applied to derive new conditional independencies from other conditional independencies defined on mixed sets of attributes. Applying (SG4) on the GMVD $\left\{A_{2}\right\} \Rightarrow \Rightarrow\left\{A_{1}\right\} \mid\left\{A_{3}\right\}$ over $\left\{A_{1}, A_{2}, A_{3}\right\}$ in (38) and the GMVD $\left\{A_{2}, A_{3}\right\} \Rightarrow \Rightarrow\left\{A_{1}\right\} \mid\left\{A_{4}\right\}$ over $\left\{A_{1}, A_{2}, A_{3}, A_{4}\right\}$ in (39), we derive the new nonembedded GMVD $\left\{A_{2}\right\} \Rightarrow \Rightarrow\left\{A_{1}\right\} \mid\left\{A_{3}, A_{4}\right\}$ over $\left\{A_{1}, A_{2}, A_{3}, A_{4}\right\}$. We add this GMVD to the set $G_{\left\{A_{1}, A_{2}, A_{3}, A_{4}\right\}}$ in (37), namely,

$$
\begin{aligned}
& G_{\left\{A_{1}, A_{2}, A_{3}, A_{4}\right\}} \cup\left\{\left\{A_{2}\right\} \Rightarrow \Rightarrow\left\{A_{1}\right\} \mid\left\{A_{3}, A_{4}\right\}\right\} \\
= & \left\{\left\{A_{2}, A_{3}\right\} \Rightarrow \Rightarrow\left\{A_{1}\right\} \mid\left\{A_{4}\right\}\right\} \cup \\
& \left\{\left\{A_{2}\right\} \Rightarrow \Rightarrow\left\{A_{1}\right\} \mid\left\{A_{3}, A_{4}\right\}\right\} \\
= & \left\{\left\{A_{2}, A_{3}\right\} \Rightarrow \Rightarrow\left\{A_{1}\right\} \mid\left\{A_{4}\right\},\left\{A_{2}\right\} \Rightarrow \Rightarrow\left\{A_{1}\right\} \mid\left\{A_{3}, A_{4}\right\}\right\}
\end{aligned}
$$

An updated conflict-free full minimum cover $G_{\left\{A_{1}, A_{2}, A_{3}, A_{4}\right\}}^{c}$ for the nonembedded GMVDs over $\left\{A_{1}, A_{2}, A_{3}, A_{4}\right\}$ is then,

$$
G_{\left\{A_{1}, A_{2}, A_{3}, A_{4}\right\}}^{c}=\left\{D e p\left(\left\{A_{2}\right\}\right)=\left\{\left\{A_{1}\right\},\left\{A_{3}, A_{4}\right\}\right\}\right\}
$$

Note that the GMVD $\left\{A_{2}, A_{3}\right\} \Rightarrow \Rightarrow\left\{A_{1}\right\} \mid\left\{A_{4}\right\}$ in (39) is now redundant in (40). This demonstrates that the contraction axiom can use the mixture of embedded and nonembedded dependencies to derive GMVDs not derivable using the GMVD axiomatization. The conflict-free full minimum cover $G_{\mathcal{N}}^{c}$ and a p-ordering sequence can be supplied as input to Algorithm 2. The output dependency structure of the multiagent Markov network $\mathcal{H}=\left\{h_{1}, h_{2}, \ldots, h_{n}\right\}$ is a per-fect-map of $G_{c}^{\mathcal{N}}$.

In order to completely define a probabilistic network, one must specify the dependency structure and the corresponding probability tables. However, the potentials corresponding to an acyclic hypergraph are not necessarily uniquely definable. On the other hand, the conditional probability tables corresponding to the dependency structure of a Bayesian network can be uniquely specified. It is thereby useful to transform the constructed acyclic hypergraph into a DAG in order to elicit the quantitative component of the probabilistic network. The potentials of the constructed acyclic hypergraph can then be defined in terms of the elicited conditional probability tables.

It is always possible to construct a DAG which reflects precisely the same probabilistic conditional independencies as and acyclic hypergraph $\mathcal{H}$. For example, consider the acyclic hypergraph $\mathcal{H}=\left\{h_{1}, h_{2}, h_{3}, h_{4}\right\}$ in Fig. 1. The dependency structure of the multiagent Bayesian network can be defined by adding the directed edge $\left(A_{2}, A_{3}\right)$ to the DAG in Fig. 5. (The directed edge $\left(A_{2}, A_{3}\right)$ could be equivalently replaced by $\left(A_{3}, A_{2}\right)$.) Notice that the only probabilistic conditional independencies inferred from the modified

DAG using d-separation [20] are exactly those nonembedded conditional independencies inferred from acyclic hypergraph $\mathcal{H}$. It is assumed that the domain experts are able to specify the conditional probability tables corresponding to the constructed DAG, namely, $\phi\left(\left\{A_{1}\right\}\right), \phi\left(\left\{A_{2}\right\} \mid\left\{A_{1}\right\}\right)$, $\phi\left(\left\{A_{3}\right\} \mid\left\{A_{1}, A_{2}\right\}\right), \phi\left(\left\{A_{4}\right\} \mid\left\{A_{2}, A_{3}\right\}\right), \phi\left(\left\{A_{5}\right\} \mid\left\{A_{2}, A_{3}\right\}\right)$, and $\phi\left(\left\{A_{6}\right\} \mid\left\{A_{5}\right\}\right)$. These elicited conditional probability tables are represented as the relations $\Phi_{\left\{A_{1}\right\}}, \Phi_{\left\{A_{1}, A_{2}\right\}}, \Phi_{\left\{A_{1}, A_{2}, A_{3}\right\}}$, $\Phi_{\left\{A_{2}, A_{3}, A_{4}\right\}}, \Phi_{\left\{A_{2}, A_{3}, A_{5}\right\}}, \Phi_{\left\{A_{5}, A_{6}\right\}}$, respectively. At this point, the multiagent Bayesian network is completely defined.

Since each agent reasons with a particular subset of variables in the entire network, it is necessary to section the constructed multiagent dependency structure. The multiply sectioned Bayesian network technique [38] can be applied for this purpose. Thus, each agent initially is given a portion of the constructed DAG representing the dependency structure of the multiagent Bayesian network. However, in practice, it is useful to transform the Bayesian network into a Markov network in order to take advantage of the techniques developed for computing marginal distributions. Even though the original DAG has been sectioned, this transformation can still be accomplished through cooperation of the agents [38]. The dependency structure of the multiagent system is thereby again a hypergraph, but the hyperedges are distributed among the agents. At this point, the multiagent system is ready for user input. Techniques have already been proposed for probabilistic reasoning in a distributed multiagent environment [6], [33].

## 6 CONCLUSION

The dependency structure of a probabilistic network is a graphical representation of the conditional independencies that are known to hold in the problem domain. It is not realistic to expect the domain experts to directly construct the dependency structure of a multiagent probabilistic network since the problem domain may be significantly larger and perhaps distributed. It is also not entirely clear how the single-agent techniques for learning the dependency structure can be applied, let alone obtaining a reliable sample. Thus, constructing the multiagent dependency structure amounts to finding a method to combine the known conditional independency information supplied by the individual domain experts. We have shown that the method of simply connecting the individual dependency structures in [37] may be too restrictive in some situations.

In this paper, an automated procedure was proposed for directly constructing the dependency structure (an acyclic hypergraph) of a multiagent Markov network. The individual domain experts can supply any known probabilistic conditional independency information and not necessarily an explicit dependency structure. Our method is capable of detecting all inconsistent and redundant independencies. The resulting minimum cover is used to systematically construct a unique dependency structure. The main result of this paper is that the constructed acyclic hypergraph is in fact a perfect-map of the probabilistic conditional independencies in the minimal cover. This method takes full advantage of the fact that nonembedded conditional independencies have a complete axiomatization [10], [20], [29].

## APPENDIX

## Proofs of Propositions

Here, we prove several results that are used in deriving the main result of our paper stated in Theorem 2.

Case 1. $X_{i} \nsubseteq X_{k}$.
Proposition 1. No $W_{k, j}$ in $\operatorname{Dep}\left(X_{k}\right), j \neq l$, partially intersects $W_{i, 1}$.
Proof. Suppose there exists a $W_{k, j}$ that intersects partially with $W_{i, 1}, j \neq l$. That is,

$$
W_{k, j} \cap W_{i, 1} \neq \emptyset \text { and } W_{k, j}-W_{i, 1} \subset W_{k, j}
$$

Since $X_{i} \subseteq X_{k} W_{k, l}$, we have

$$
X_{k} \Rightarrow \Rightarrow X_{k} W_{k, l}=X_{i} \bar{W}_{k, l}, \text { where } \bar{W}_{k, l}=X_{k} W_{k, l}-X_{i}
$$

By augmentation on the GMVD $X_{i} \Rightarrow \Rightarrow W_{k, j}-W_{i, 1}$ in (19), we obtain

$$
X_{i} \bar{W}_{k, l} \Rightarrow \Rightarrow W_{k, j}-W_{i, 1}
$$

By transitivity, it follows:

$$
X_{k} \Rightarrow \Rightarrow\left(W_{k, j}-W_{i, 1}\right)-X_{i} \bar{W}_{k, l}
$$

However, the right side can be simplified as

$$
\begin{aligned}
& \left(W_{k, j}-W_{i, 1}\right)-X_{i} \bar{W}_{k, l} \\
& \quad=\left(W_{k, j}-W_{i, 1}\right)-X_{k} W_{k, l} \\
& \quad=\left(W_{k, j}-W_{i, 1}\right)-W_{k, l}=\left(W_{k, j}-W_{i, 1}\right)
\end{aligned}
$$

Since $\left(W_{k, j}-W_{i, 1}\right) \subset W_{k, j}$, then $\operatorname{Dep}\left(X_{k}\right)$ can be refined. This is a contradiction.

Proposition 2. If $W_{k, j} \cap W_{i, 1}=\emptyset, j \neq l$, then $W_{k, j}$ must also belong to $\operatorname{Dep}\left(X_{i} \cap X_{k}\right)$.
Proof. We first show that $W_{k, j}$ must belong to $\operatorname{Dep}\left(X_{i}\right)$. From (19), we obtain

$$
X_{i} \Rightarrow \Rightarrow W_{k, j}-W_{i, 1}=W_{k, j}
$$

Suppose $W_{k, j} \neq W_{i, s}$, for any $s \geq 2$. We can show that either $\operatorname{Dep}\left(X_{i}\right)$ or $\operatorname{Dep}\left(X_{k}\right)$ can be refined. Obviously, if $W_{k, j}$ is not equal to a union of some $W_{i} \mathrm{~s}$, then $\operatorname{Dep}\left(X_{i}\right)$ can be refined, a contradiction. On the other hand, if $W_{k, j}$ is equal to a union of more than one $W_{i, s}$, then $W_{k, j}$ can be written as

$$
W_{k, j}=W_{i, s_{1}} W_{i, s_{2}} \ldots W_{i, s_{q}}
$$

By definition $W_{k, j} \cap W_{k, l}=\emptyset$, it then follows:

$$
W_{i, s_{1}}-W_{k, l}=W_{i, s_{1}} \text { and } W_{i, s_{2}}-W_{k, l}=W_{i, s_{2}}
$$

By (20), we therefore obtain

$$
X_{k} \Rightarrow \Rightarrow W_{i, s_{1}} \text { and } X_{k} \Rightarrow \Rightarrow W_{i, s_{2}}
$$

This means that $\operatorname{Dep}\left(X_{k}\right)$ can be refined, a contradiction. From the above analysis, we can therefore conclude that $W_{k, j}=W_{i, s}$, for some $s \geq 2$. That is, $W_{k, j}$ is an element in $\operatorname{Dep}\left(X_{i}\right)$. Hence,

$$
W_{k, j} \in \operatorname{Dep}\left(X_{i}\right) \cap \operatorname{Dep}\left(X_{k}\right)
$$

By the second condition of conflict-free, we have

$$
\operatorname{Dep}\left(X_{i}\right) \cap \operatorname{Dep}\left(X_{k}\right) \subseteq \operatorname{Dep}\left(X_{i} \cap X_{k}\right)
$$

It follows $W_{k, j} \in \operatorname{Dep}\left(X_{i} \cap X_{k}\right)$.

Proposition 3. If $W_{i, s}$ in $\operatorname{Dep}^{\prime}\left(X_{i}\right)$ belongs to $\operatorname{Dep}\left(X_{i} \cap X_{k}\right)$, then $W_{i, s}$ must also belong to $\operatorname{Dep}\left(X_{k}\right)$.
Proof. Since $W_{i, s} \in \operatorname{Dep}\left(X_{i} \cap X_{k}\right)$, by augmentation, we have $X_{i} \Rightarrow \Rightarrow W_{i, s}$ and $X_{k} \Rightarrow \Rightarrow W_{i, s}$. Suppose $W_{i, s}$ is not equal to some $W_{k, j}$ disjoint from $W_{i, 1}$. Then, there are two possibilities:

1. $W_{i, s}$ is a union of more than one $W_{k, j}$ disjoint from $W_{i, 1}$. That is,

$$
W_{i, s}=W_{k, j_{1}} W_{k, j_{2}} \ldots W_{k, j_{k}}
$$

From (19), we obtain

$$
X_{i} \Rightarrow \Rightarrow W_{k, j_{1}}, \text { and } X_{i} \Rightarrow \Rightarrow W_{k, j_{2}}
$$

This means that $W_{i, s}$ in $\operatorname{Dep}\left(X_{i}\right)$ can be made "smaller." This is a contradiction.
2. $W_{i, s}$ is not a union of some $W_{k, j} \mathrm{~s}$.

From the fact that $X_{k} \Rightarrow \Rightarrow W_{i, s}$, we can immediately conclude that some $W_{k, j} \mathrm{~s}$ in $\operatorname{Dep}\left(X_{k}\right)$ can be made "smaller." This is a contradiction.
Therefore, $W_{i, s}$ must be equal to some $W_{k, j}$ outside $W_{i, 1}$.
Proposition 4. $W_{k, l}-X_{i} W_{i, 1} \neq \emptyset$. More specifically,

$$
\begin{aligned}
W_{k, l}- & X_{i} W_{i, 1}= \\
& \cup\left\{W \mid W \in \operatorname{Dep}^{\prime}\left(X_{i}\right) \text { and } W \notin \operatorname{Dep}\left(X_{i} \cap X_{k}\right)\right\}
\end{aligned}
$$

Proof. $W_{k, l}-W_{i, 1} \neq \emptyset$ since, by assumption, $W_{k, l}$ contains at least one attribute in $X_{i}$ and, of course, $W_{i, 1}$ does not. Since $\mathcal{N}$ is a fixed set of attributes, the claim follows immediately.
Proposition 5. $X_{i}-X_{k} \neq \emptyset$ and $X_{k}-X_{i} \neq \emptyset$. If $\operatorname{Dep}\left(X_{i}\right)$ and $\operatorname{Dep}\left(X_{k}\right)$ satisfy Propositions 1, 2, 3, and 4, then $\operatorname{Dep}\left(X_{i}\right)$ and $\operatorname{Dep}\left(X_{k}\right)$ cannot be refined.
Proof. Obviously, $X_{i} \Rightarrow \Rightarrow W_{k, l}-W_{i, 1}$ in (19) leads to no refinement of $\operatorname{Dep}\left(X_{i}\right)$. Next, we want to show that $X_{i} \Rightarrow$ $\Rightarrow W_{k, l}-W_{i, 1}$ leads to no refinement of $\operatorname{Dep}\left(X_{k}\right)$ either. Since $X_{k} \Rightarrow \Rightarrow W_{k, l}$, we have

$$
X_{k} \Rightarrow \Rightarrow X_{k} W_{k, l}=X_{i} \bar{W}_{k, l}, \text { where } \bar{W}_{k, l}=X_{k} W_{k, l}-X_{i}
$$

By augmentation, $X_{i} \Rightarrow \Rightarrow W_{k, l}-W_{i, 1}$ becomes

$$
X_{i} \bar{W}_{k, l} \Rightarrow \Rightarrow W_{k, l}-W_{i, 1}
$$

By transitivity, we obtain

$$
X_{k} \Rightarrow \Rightarrow\left(W_{k, l}-W_{i, 1}\right)-X_{i} \bar{W}_{k, l}
$$

Since $X_{i} \bar{W}_{k, l}=X_{k} W_{k, l}$ and $\left(W_{k, l}-W_{i, 1}\right) \subseteq X_{k} W_{k, l}$, the GMVD in (41) is $X_{k} \Rightarrow \Rightarrow \emptyset$. Thus, $\operatorname{Dep}\left(X_{k}\right)$ cannot be refined with this GMVD.

We now show that the GMVD $X_{k} \Rightarrow \Rightarrow W_{i, 1}-W_{k, l}$ in (20) leads to no refinement of $\operatorname{Dep}\left(X_{k}\right)$. By Proposition 1, $W_{i, 1}-W_{k, l}$ is a union of elements in $\operatorname{Dep}\left(X_{k}\right)$. Thus,

$X_{k} \Rightarrow \Rightarrow W_{i, 1}-W_{k, l}$ cannot be used to refine $\operatorname{Dep}\left(X_{k}\right)$. We now show that the GMVD $X_{k} \Rightarrow \Rightarrow W_{i, 1}-W_{k, l}$ in (20) leads to no refinement of $\operatorname{Dep}\left(X_{i}\right)$. Since $X_{i} \Rightarrow \Rightarrow W_{i, 1}$, we have

$$
X_{i} \Rightarrow \Rightarrow X_{i} W_{i, 1}=X_{k} \bar{W}_{i, 1}, \text { where } \bar{W}_{i, 1}=X_{i} W_{i, 1}-X_{k}
$$

By augmentation, $X_{k} \Rightarrow \Rightarrow W_{i, 1}-W_{k, l}$ becomes

$$
X_{k} \bar{W}_{i, 1} \Rightarrow \Rightarrow W_{i, 1}-W_{k, l}
$$

By transitivity, we obtain

$$
X_{i} \Rightarrow \Rightarrow\left(W_{i, 1}-W_{k, l}\right)-X_{k} \bar{W}_{i, 1}
$$

Since $X_{k} \bar{W}_{i, 1}=X_{i} W_{i, 1}$ and $\left(W_{i, 1}-W_{k, l}\right) \subseteq X_{i} W_{i, 1}$, the GMVD in (42) is $X_{i} \Rightarrow \Rightarrow \emptyset$. Thus, $\operatorname{Dep}\left(X_{i}\right)$ cannot be refined with this GMVD.
Case 2. $X_{i} \subseteq X_{k}$.
Proposition 6. No $W_{k, j}$ partially intersects $W_{i, 1}$.
Proof. Suppose $W_{k, j}-W_{i, 1} \subset W_{k, j}$. From (19),

$$
X_{i} \Rightarrow \Rightarrow W_{k, j}-W_{i, 1} \equiv W_{k, j}^{\prime} \subset W_{k, j}
$$

Since $X_{i} \subseteq X_{k}$, by augmentation, we obtain the GMVD $X_{k} \Rightarrow \Rightarrow W_{k, j}^{\prime}$. This means that $\operatorname{Dep}\left(X_{k}\right)$ can be refined. This is a contradiction.

Proposition 7. Every $W_{i, s}$ in $\operatorname{Dep}^{\prime}\left(X_{i}\right)$ also belongs to $\operatorname{Dep}\left(X_{k}\right)$.
Proof. In this case, $\operatorname{Dep}\left(X_{i} \cap X_{k}\right)=\operatorname{Dep}\left(X_{i}\right)$. The claim follows from Proposition 3.
Proposition 8. If $W_{k, j} \cap W_{i, 1}=\emptyset$, then $W_{k, j}$ is also an element in $\operatorname{Dep}^{\prime}\left(X_{i}\right)$.
Proof. In this case, $\operatorname{Dep}\left(X_{i} \cap X_{k}\right)=\operatorname{Dep}\left(X_{i}\right)$. The claim follows from Proposition 2.
Proposition 9. $X_{k}$ is a subset of exactly one hyperedge $h$ in $\mathcal{H}^{k-1}$.
Proof. Let $h_{i}$ and $h_{j}$ be two distinct hyperedges in $\mathcal{H}^{k-1}$. Suppose $X_{k}$ is a subset of $h_{i} \cap h_{j}$. Since $X_{k}$ is not a J-key in $\mathcal{H}^{k-1}, X_{k}$ must be contained by some J-key of $\mathcal{H}^{k-1}$. This is a contradiction to the definition of a p-ordering sequence. On the other hand, suppose there are attributes $A$ and $B$ in $X_{k}$ such that $A \in h_{i}-h_{j}$ and $B \in h_{j}-h_{i}$. This means $X_{k}$ is split by some key. This contradicts the initial assumption that the keys are conflict-free.
Proposition 10. Let $h$ be the hyperedge in $\mathcal{H}^{k-1}$ containing $X_{k}$. Then,

$$
\{h\}=\overline{X_{1} W_{1,1}} \cap \ldots \cap \overline{X_{k-1} W_{k-1,1}}
$$

Proof. Obviously, by Proposition 9, we have

$$
\{h\} \subseteq \overline{X_{1} W_{1,1}} \cap \ldots \cap \overline{X_{k-1} W_{k-1,1}}
$$

It is also clear that any hyperedge $h^{\prime} \in \mathcal{H}^{k-1}, h^{\prime} \neq h, h^{\prime}$ is not an element of some $\overline{X_{i} W_{i, 1}}$. Thus,
$X_{k} \subseteq\{h\}=\overline{X_{1} W_{1,1}} \cap \ldots \cap \overline{X_{k-1} W_{k-1,1}}$.
