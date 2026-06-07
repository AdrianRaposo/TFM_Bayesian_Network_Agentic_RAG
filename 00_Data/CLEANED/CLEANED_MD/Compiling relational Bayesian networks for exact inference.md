# UCLA 

## UCLA Previously Published Works

## Title

Compiling relational Bayesian networks for exact inference

## Permalink

https://escholarship.org/uc/item/2ts2n8nt

## Journal

International Journal of Approximate Reasoning, 42(1-2)

## ISSN

0888-613X

## Authors

Chavira, M D
Darwiche, A
Jaeger, M

## Publication Date

2006-05-01
Peer reviewed

# Compiling Relational Bayesian Networks for Exact Inference 

Mark Chavira, Adnan Darwiche<br>Computer Science Department, UCLA, Los Angeles, CA 90095<br>Manfred Jaeger<br>Institut for Datalogi, Aalborg Universitet, Fredrik Bajers Vej 7 E, DK-9220 Aalborg $\varnothing$


#### Abstract

We describe in this paper a system for exact inference with relational Bayesian networks as defined in the publicly available Primula tool. The system is based on compiling propositional instances of relational Bayesian networks into arithmetic circuits and then performing online inference by evaluating and differentiating these circuits in time linear in their size. We report on experimental results showing successful compilation and efficient inference on relational Bayesian networks, whose Primula-generated propositional instances have thousands of variables, and whose jointrees have clusters with hundreds of variables.


Key words: Exact Inference, Relational Models, Bayesian Networks

## 1 Introduction

Relational probabilistic models extend Bayesian network models by representing objects, their attributes, and their relations with other objects. The standard approach for inference with a relational model is based on the generation of a propositional instance of the model in the form of a classical Bayesian network, and then applying classical algorithms, such as jointree [1], to compute answers to queries.

[^0]
[^0]:    Email addresses: chavira@cs.ucla.edu (Mark Chavira), darwiche@cs.ucla.edu (Adnan Darwiche), jaeger@cs.aau.dk (Manfred Jaeger).

The propositional instance of a relational model includes one Boolean random variable for each ground relational atom. For example, if we have $n$ domain objects $o_{1}, \ldots, o_{n}$, and a binary relation $R(.,$.$) , we generate a propositional variable for each instance of the relation: R\left(o_{1}, o_{1}\right), R\left(o_{1}, o_{2}\right), \ldots, R\left(o_{n}, o_{n}\right)$. The first task in making Bayesian networks over these random variables tractable for inference is to ensure that the size of the Bayesian network representation does not show exponential growth in the number $n$ of domain objects (as can easily happen due to nodes whose in-degree grows as a function of $n$ ). This can often be achieved by decomposing nodes with high in-degree into suitable, sparsely connected sub-networks using a number of new, auxiliary nodes. This approach is systematically employed in the Primula system. Even when a reasonably compact Bayesian network representation (i.e., polynomial in the number of objects) has been constructed for a propositional instance, this model will often be inaccessible to standard algorithms for exact inference, because its global structure does not lead to tractable jointrees.

Even though the constructed networks may lack the global structure that would make them accessible to standard inference techniques, they may very well exhibit abundant local structure in the form of determinism. The objective of this paper is to describe a system for inference with propositional instances of relational models which can exploit this local structure, allowing us to reason very efficiently with some relational models whose propositional instances may look quite formidable at first. Specifically, we employ the approach proposed by [2] to compile propositional instances of relational models into arithmetic circuits, and then perform online inference by evaluating and differentiating the compiled circuits in time linear in their size. As our experimental results illustrate, this approach can efficiently handle some relational models whose Primula-generated propositional instances are quite massive. ${ }^{1}$ We note here that the inference approach of [2] is applicable to any Bayesian network, but is especially effective on networks with local structure, including determinism. Hence, one of the main points of this paper is to illustrate the extent of local structure available in propositional instances of relational models, and the effectiveness in exploiting this local structure by the approach proposed in [2].

This paper is structured as follows. We start in Section 2 with a review of relational models in general and the specific formalization used in this paper. We then discuss in Section 3 the Primula system, which implements this formalization together with a method for generating propositional instances in the form of Bayesian networks. Section 4 is then dedicated to our proposed

[^0]
[^0]:    ${ }^{1}$ Some may recall the technique of zero-compression which can be used to exploit determinism in the jointree framework [3]. This technique, however, requires that one perform inference on the original jointree before it is zero-compressed, making almost all of our data sets inaccessible to this method. For a more detailed relationship to jointree inference, the reader is referred to [4].

![img-0.jpeg](img-0.jpeg)

Fig. 1. A Bayesian net with two of its CPTs.
approach for compiling relational models. We provide experimental results in Section 5, and finally close with some concluding remarks in Section 6.

# 2 Relational Models 

A Bayesian network is a compact representation of a probability distribution and has two parts: a directed acyclic graph and a set of conditional probability tables (CPTs). Each node in the graph represents a random variable, which we assume to be discrete in this paper. Each variable $X$ has associated with it a CPT, which specifies the conditional probabilities $\operatorname{Pr}(x \mid \mathbf{u})$, where $\mathbf{u}$ is a configuration of the parents $\mathbf{U}$ of $X$ in the network.

A Bayesian network over a set of variables specifies a unique probability distribution over these variables. Probabilistic queries with respect to a Bayesian network are to be interpreted as queries with respect to the probability table the network specifies. The main goal of algorithms for Bayesian networks is to answer such queries without having to construct the table explicitly, since the table's size is exponential in the number of network variables. Figure 1 depicts a simple Bayesian network with two of its CPTs.

Relational or first-order probabilistic models extend propositional modeling supported by Bayesian networks by allowing one to represent objects explicitly, and to define relations over these objects. Most of the early work on such generic models, which has been subsumed under the title knowledge-based model construction (see e.g. [5]), combines elements of logic-programming with Bayesian networks. Today one can distinguish several distinct representation paradigms for relational and first-order models: (inductive) logicprogramming based approaches [6-8], network fragments [9], frame-based representations $[10,11]$, and probabilistic predicate logic formulas [12]. We review relational models with an example.

![img-1.jpeg](img-1.jpeg)

Fig. 2. (a) A simple alarm scenario, (b) the corresponding Bayesian network, and (c) a graph depicting the particulars of the situation, as opposed to what is common to all alarm situations.

# 2.1 An Example 

Consider the well-known example depicted in Figure 2(a), in which Holmes becomes alarmed if he receives a call from his neighbor Watson. Watson will likely call if an alarm has sounded at Holmes' residence, which is more likely if a burglary occurs. However, Watson is a prankster, so Holmes may receive a call even if the alarm does not sound. We can model this example with a Bayesian network as shown in Figure 2(b). A query might be the probability that there is a burglary given that Holmes is alarmed. We could also consider similar scenarios. Holmes might have multiple neighbors (only some of whom are pranksters) and become alarmed if any of them calls. There might be multiple individuals who can receive calls, each with distinct neighbors. Or it might be that individuals share neighbors and individuals who receive calls can also make them. For each of these scenarios, we can construct a distinct Bayesian network. Moreover, we can imagine needing to deal with many of these situations, and hence needing to construct many different networks.

Each of the situations described represents a combination of various themes, such as the theme of an alarm compelling a neighbor to call or an individual becoming alarmed when some neighbor calls. Relational models address domains involving themes by separating the model construction process into two phases. We first describe a set of general rules that apply to all situations. For example, in the alarm domain described, we need four rules:
(1) At a given residence, the probability of burglary is 0.005 .
(2) A particular alarm sounds with probability 0.95 if a burglary occurs at the corresponding residence, and with probability 0.01 otherwise.
(3) If an alarm sounds at an individual's residence, then each of the individual's neighbors will call with probability 0.9 ; otherwise, if the neighbor is a prankster, then the neighbor will call with probability 0.05 ; otherwise,

the neighbor will not call.
(4) An individual is alarmed if one or more neighbors call.

We highlight here that whether an individual is alarmed depends on the number of the individual's neighbors, which makes this domain difficult represent with a template-based language.

Once we have specified what is common to all situations, in order to specify a particular situation, we only need specify a small amount of additional information. In the alarm example, that information consists of which individuals are involved (other than burglars), who are neighbors of whom, and who are pranksters. We specify a graph where nodes represent individuals, edges capture the neighbor relationship, and each node is marked if the corresponding individual is a pranktser. Figure 2(c) depicts the graph corresponding to the situation in Figure 2(a).

One of the main advantages of using a relational model is that a relational model describes a situation involving themes succinctly. This advantage often makes constructing a relational model much easier and less error-prone than constructing a Bayesian network. For example, it is not uncommon for a relational model with a dozen or so general rules to correspond to a Bayesian network that involves hundreds of thousands of CPT parameters. Another advantage is that much of the work performed in constructing a relational model can be directly re-used in describing variations of the model, whereas creating another Bayesian network can involve much more work.

# 2.2 Relational Bayesian Networks 

We use in this paper the language of relational Bayesian networks [12] to represent relational models, as implemented in the Primula system available at http://www.cs.aau.dk/ jaeger/Primula. The formal semantics of the language is based on Random Relational Structure Models (RRSMs), which we define next.

Definition 1 Given (1) a set of relational symbols $S$, called predefined relations; (2) a set of relational symbols $R$, called probabilistic relations; and (3) a finite set $D$, called the domain; we define an $\overline{S^{D}}$-structure to be an interpretation of relations $S$ over domain $D$, that is, a function which maps every ground atom $s(d)(s \in S, d \subseteq D)$ to either true or false. We also define a Random Relational Structure Model (RRSM) as a partial function which takes an $S^{D}$-structure as input, and returns a probability distribution over all $R^{D}$ structures as output.

Intuitively, members of domain $D$ represent objects, and members of $S$ and $R$ represent relations that can hold on these objects. These relations can be unary in which case they are called attributes. A user would typically define the relations in $S$ (by providing an $S^{D}$-structure), and then use an RRSM to induce a probability distribution over the possible definitions of relations in $R$ ( $R^{D}$-structures). We note here that $S^{D}$-structures correspond to skeleton structures in [11]. For the alarm example above, the set $D$ of objects is the set of individuals. The set of predefined relations $S$ contains a unary relation, prankster, in addition to a binary relation neighbor. There are four probabilistic relations in $R$ for this domain. The first is $\operatorname{calls}(v, w)$ : whether $v$ calls $w$ in order to warn $w$ that his alarm went off. We also have another probabilistic relation alarmed $(v)$ : whether $v$ has been alarmed (called by at least one neighbor). A third is the relation alarm $(v)$ : whether $v$ 's alarm went off. The last probabilistic relation is burglary $(v)$ : whether $v$ 's home has been burglarized. The RRSM is the set of four generic rules described previously.

We now describe four RRSMs used in our experiments. These models have been implemented in Primula, which provides a syntax for specifying RRSM.

Random Blocks. This model describes the random placement of blocks (obstacles) on the locations of a map. The input structures consist of a particular gridmap and a set of blocks. This is represented using a set of predefined relations $S=\{$ location,block,leftof, belowof $\}$ where location and block are attributes that partition the domain into the two types of objects, and leftof and belowof are binary relations that determine the spatial relationship among locations. Figure 3 shows an input $S^{D}$-structure. One of the probabilistic relations in $R$ for this model is the binary relation blocks $(b, l)$ which represents the random placement of a block $b$ on some location $l$. Another is connected $\left(l_{1}, l_{2}\right)$ between pairs of locations which describes whether, after placement of the blocks, there is an unblocked path between $l_{1}$ and $l_{2}$. A probabilistic query might be the probability that there is an unblocked path between two locations $l_{1}$ and $l_{2}$, given the observed locations of some blocks (but uncertainty about the placement of the remaining ones). We experiment with different versions of this relational model, blockmap- $l-b$, where $l$ is the number of locations and $b$ the number of blocks.
![img-2.jpeg](img-2.jpeg)

Fig. 3. Input $S^{D}$-structure.
Mastermind. In the game of Mastermind, Player 1 arranges a hidden sequence of colored pegs. Player 2 guesses the exact sequence of colors by ar-

ranging guessed sequences of colored pegs. To each guessed sequence, Player 1 responds by stating how many pegs in the guess match pegs in his hidden sequence both in color and position (white feedback), and how many pegs in the guess match pegs in the hidden sequence only in color (black feedback). Player 2 wins if he guesses the hidden sequence within a certain number of rounds. The game can be represented as an RRSM where the domain $D$ consists of objects of types peg, color, and round specified by corresponding unary relations in $S$, as well as binary relations peg-ord and round-ord in $S$ that impose orders on the peg and round objects, respectively. The probabilistic relations $R$ in the model represent the game configurations after a number of rounds: true-color $(p, c)$ represents that $c$ is the color of the hidden peg $p$; guessed-color $(p, c, r)$ represents that in round $r$ color $c$ was placed in position $p$ in the guess. Similarly, the arrangement of the feedback pegs can be encoded. A query might be the most probable color configuration of the hidden pegs, given the observed query and feedback pegs. We experiment with different versions of this model, mastermind- $c-g-p$, where $c$ is the number of colors, $g$ is the number of guesses, and $p$ is the number of pegs.

Students and Professors. This domain was used by [13] to investigate methods for approximate inference for relational models. We have two types of objects in this model: students and professors and two corresponding attributes in the set $S$. Professors have two probabilistic attributes in $R$ : fame (yes/no) and funding_level (high/low). Students have one probabilistic attribute in $R$ : success (yes/no). Students and professors are related via the binary probabilistic relation advisor $(s, p)$ in $R$. According to the model, students use the softmax rule, and choose advisor $i$ with funding level $y_{i}$ with probability $e^{y_{i}} / \sum_{k} e^{y_{k}}$. With the funding level discretized into two categories high and low, this reduces to choosing any given rich (poor) professor with probability $z_{h} /\left(K z_{h}+L z_{l}\right)\left(z_{l} /\left(K z_{h}+L z_{l}\right)\right)$, where $K$ is the number of rich professors, $L$ is the number of poor professors, and $z_{h}, z_{l}$ are the (exponentials of) the funding levels of rich, respectively poor, professors. The probability of success of a student is defined conditional on the funding level. A query for this model can be the probabilities for a professor's funding level, given the success of his students. Inference in this model becomes hard very quickly with increasing numbers of professors and students in the domain [13]. We will experiment with different versions of this relational model, students- $p-s$, where $p$ is the number of professors and $s$ is the number of students.

Friends and Smokers. This domain was introduced in [14]. It involves a number of individuals, with relations in $R$, such as smokes $(v)$, which indicates whether a person smokes, cancer $(v)$, which indicates whether a person has cancer, and friends $(u, v)$, which indicates who are friends of whom. There are no relations in $S$ for this model. The probabilistic model over $R$ is defined by assigning weights to logical constraints, such as friends $(u, v) \wedge$ smokes $(u) \rightarrow$ smokes $(v)$. A query for this model might be the probability that a person has

cancer given information about others who have cancer. The Primula encoding of this model utilizes auxiliary probabilistic relations corresponding to the logical constraints. In ground instances of the model these auxiliary variables manifest themselves as variables in the Bayesian network, on which evidence should be asserted to indicate that they are always true. We experiment with different versions of this relational model, fr\&sm- $n$, where $n$ is the number of people in the domain.

# 3 The Primula System 

The RRSM is an abstract semantics of probabilistic relational models. For a practical system, one needs a specific syntax for specifying an RRSM. PrimULA allows users to encode RRSMs using the language of relational Bayesian networks [12], and outputs the distribution on $R^{D}$-structures in the form of a standard Bayesian network.

### 3.1 Specifying RRSMs using Primula

We now provide an example of specifying an RRSM using Primula. Consider again the alarm example from Section 2.1 and recall that for this example, the domain is the set of individuals, the set of predefined relations is $S=\{\operatorname{prankster}(v), \operatorname{neighbor}(v, w)\}$, and the set of probabilistic relations is $R=\{\operatorname{calls}(v, w), \operatorname{alarm}(v), \operatorname{alarmed}(v), \operatorname{burglary}(v)\}$. The probability of $\operatorname{calls}(v, w)$ is defined conditional on the predefined neighbor and prankster relations (it is 0 if $v$ and $w$ are not neighbors), and on the probabilistic alarm $(v)$ relation: whether the alarm of $v$ went off.

This RRSm is specified in Primula as given in Figure 4, which provides the probability distribution on probabilistic relations using probability formulas. These formulas can be seen either as probabilistic analogues of predicate logic formulas, or as expressions in a functional programming language. A probability formula defines both the dependency structure between ground probabilistic atoms (which depends on the predefined relations in the input structure), and the exact conditional probabilities, given the truth values of parent atoms.

The specification of the RRSM provides some intuition for why a logic-based approach might work well when applied to Primula generated networks. In addition to certain numbers, we also see in this specification a number of logical constructs. For example, each of the occurrences of $(x: y, z)$ is essentially an application of an if-then-else, and the noisy-or construct is essentially an existential quantification, which can be converted into a disjunction over a

```
burglary(v) = 0.005;
alarm(v) = (burglary(v):0.95,0.01);
calls(v,w) = (neighbor(v,w):
    (prankster(v)):
                            (alarm(w):0.9,0.05),
                            (alarm(w):0.9,0)),0);
alarmed(v)=n-or{ calls(w,v)|w:neighbor(w,v)}
```

Fig. 4. Specifying an RRSM using Primula.

```
DOMAIN: Holmes, Watson, Gibbon;
RELATION: prankster/1 {2};
RELATION: neighbor/2 {(0,1) (0,2) (1,0) (2,0)};
```

Fig. 5. Specifying an $S^{D}$ structure using Primula.
set of auxiliary variables. The utilization of these logical constructs is quite common in relational models.

# 3.2 From relational to propositional networks 

To instantiate a generic relational model in Primula, one must provide a definition of an input $S^{D}$-structure. For the RRSM defined in Figure 4, one must define the set of individuals in domain $D$, and then one must define which of these individuals are pranksters (by defining the attribute prankster), and who are neighbors of whom (by defining the relation neighbor). PrimULA provides a GUI for this purpose, but one can also supply a file-based definition of the domain and corresponding $S$ relations. Figure 5 presents what one of these files might look like. This file defines the domain to be $D=\{$ Holmes, Watson, Gibbon $\}$ and specifies that Gibbon is a prankster, that Holmes is a neighbor of Watson and Gibbon and that Watson and Gibbon are neighbors of Holmes.

Given the above inputs, the distribution over probabilistic relations can be represented, as described in Section 1, using a standard Bayesian network with a node for each ground probabilistic atom. Our example also illustrates how the in-degree of a node can grow as a function of the number of domain objects: the node alarmed(Holmes), for instance, depends on calls( $w$, Holmes) for all of Holmes's neighbors $w$ (of which there might be arbitrarily many).

The Primula system employs the general method described in [15] to decompose the dependency of a node on multiple parents. This method consists of an iterative algorithm that takes the probability formula defining the distribution of a node, decomposes it into its top-level subformulas - by introducing one new auxiliary node for each of these subformulas - and defines the prob-

ability of the original node conditional only on the new auxiliary nodes. This method can be applied to any relational Bayesian network that only contains multi-linear combination functions (including noisy-or and mean), and yields a Bayesian network where the number of parents is bounded by three for all nodes.

Even when one succeeds in constructing a standard Bayesian network of a manageable representation size, inference in this network may be computationally very hard. It is a long-standing open problem in first-order and relational modeling whether one might not design inference techniques that avoid these complexities of inference in the ground propositional instances by performing inference directly on the level of the relational representation, perhaps employing techniques of first-order logical inference. Complexity results derived in [16] show that one cannot hope for a better worst-case performance with such inference techniques. This still leaves the possibility that they could often lead to substantial gains in practice.

Recent work has described high-level inference techniques that aim at achieving such gains in average-case performance [17,18]. The potential advantage of this and similar techniques seems to be restricted, however, to relational models where individual model instances are given by relatively unstructured input structures, i.e., input structures containing large numbers of indistinguishable objects. The potential of high-level inference techniques lies in their ability to deal with such sets of objects without explicitly naming each object individually. However, in the type of relational models we are considering here, the input structures consist of mostly unique objects (in Random Blocks, for instance, the block objects are indistinguishable, but all location objects have unique properties defined by the belowof and leftof relations). We can identify an input structure with the complete ground propositional theory that defines it (for the structure of Figure 3 this would be the theory block $(B 1) \wedge \neg$ location $(B 1) \wedge \ldots \wedge$ leftof $(2,3) \wedge \ldots \wedge \neg$ belowof $(5,5))$, and, informally, characterize highly structured input structures as those for which this propositional theory admits no simple first-order abstraction. When a relational model instance, now, is given by an input structure that cannot be succinctly encoded in an abstract, first-order style representation, chances are very small that probabilistic inference for this model instance can gain much efficiency by operating on a non-propositional level.

It thus appears that at least for a fairly large class of interesting models more advantages might be gained by optimizing inference techniques for ground propositional models, than by non-propositional inference techniques.

Table 1 depicts the relational models with which we experimented, together with the size of corresponding propositional Bayesian networks generated by Primula. The table also reports the size of the largest cluster for the jointree

we constructed for these networks. Obviously, most of these networks are inaccessible to mainstream, structure-based algorithms for exact inference. Yet, we will show later that all of these particular models can be handled efficiently using the compilation approach we propose in this paper.

# 4 Compiling Relational Models 

We describe in this section the approach we use to perform exact inference on propositional instances of relational models, which is based on compiling Bayesian networks into arithmetic circuits [2]. Inference can then be performed using a simple two-pass procedure in which the circuit is evaluated and differentiated given evidence.

### 4.1 Bayesian networks as polynomials

The compilation approach we adopt is based on viewing each Bayesian network as a very large polynomial (multi-linear function in particular), which may be compactly represented using an arithmetic circuit. The function itself contains two types of variables. For each value $x$ of each variable $X$ in the network, we have a variable $\lambda_{x}$ called an evidence indicator. For each instantiation $x, \mathbf{u}$ of each variable $X$ and its parents $\mathbf{U}$ in the network, we have a variable $\theta_{x \mid \mathbf{u}}$ called a network parameter. The multi-linear function has a term for each instantiation of the network variables, which is constructed by multiplying all evidence indicators and network parameters that are consistent with that instantiation. For example, the multi-linear function of the network in Figure 1 has 8 terms corresponding to the 8 instantiations of variables $A, B, C: f=\lambda_{a} \lambda_{b} \lambda_{c} \theta_{a} \theta_{b \mid a} \theta_{c \mid a}+\lambda_{a} \lambda_{b} \lambda_{c} \theta_{a} \theta_{b \mid a} \theta_{c \mid a}+\ldots+\lambda_{\bar{a}} \lambda_{\bar{b}} \lambda_{\bar{c}} \theta_{\bar{a}} \theta_{\bar{b} \bar{a}} \theta_{\bar{c} \mid \bar{a}}$. Given this multi-linear function $f$, we can answer standard queries with respect to its corresponding Bayesian network by simply evaluating and differentiating this function; see [2] for details.

The ability to compute answers to probabilistic queries directly from the derivatives of $f$ is interesting semantically, but one must realize that the size of function $f$ is exponential in the number of network variables. Yet, one may be able to factor this function and represent it more compactly using an arithmetic circuit. An arithmetic circuit is a rooted DAG, in which each leaf represents a variable or constant and each internal node represents the product or sum of its children; see Figure 6. If we can represent the network polynomial efficiently using an arithmetic circuit, then inference can be done in time linear in the size of such circuits, since the (first) partial derivatives of an arithmetic circuit can all be computed simultaneously in time linear in

![img-3.jpeg](img-3.jpeg)

Fig. 6. Factoring multi-linear functions into arithmetic circuits. the circuit size $[2]$.

# 4.2 Compiling the network polynomial into an arithmetic circuit 

We now turn to the approach for compiling/factoring network polynomials into arithmetic circuits, which is based on reducing the factoring problem to one of logical reasoning [19]. This approach is based on three conceptual steps, as shown in Figure 6. First, the network polynomial is encoded using a propositional theory. Next, the propositional theory is factored by converting it to a special logical form. Finally, an arithmetic circuit is extracted from the factored propositional theory. ${ }^{2}$

Step 1: Encoding a multi-linear function using a propositional theory. The purpose of this step is to specify the network polynomial using a propositional theory. To illustrate how a multi-linear function can be specified using a propositional theory, consider the following function $f=a c+a b c+c$ over real-valued variables $a, b, c$. The basic idea is to specify this multi-linear function using a propositional theory that has exactly three models, where each model encodes one of the terms in the function. Specifically, suppose

[^0]
[^0]:    ${ }^{2}$ A similar approach has been recently proposed in [20], which calls for encoding Bayesian networks into CNFs, and reducing probabilistic inference to weighted model counting on the generated CNFs. The approach is similar in two senses. First, the weighted model counting algorithm applied in [20] is powerful enough to factor the CNF as suggested by Step 2 below-see [21]. Second, the factored logical form we generate from the CNF in Step 2 is tractable enough to allow weighted model counting in time linear in the form size $[22,23]$.

we have the Boolean variables $V_{a}, V_{b}, V_{c}$. Then the propositional theory $\Delta_{f}=$ $\left(V_{a} \vee \neg V_{b}\right) \wedge V_{c}$ encodes the multi-linear function $f$ as follows:


That is, model $\sigma$ encodes term $t$ since $\sigma\left(V_{j}\right)=$ true precisely when term $t$ contains the real-valued variable $j$. This method of specifying network polynomials allows one to easily capture local structure; that is, to declare certain information about values of polynomial variables. For example, if we know that parameter $a=0$, then we can exclude all terms that contain $a$ by conjoining $\neg V_{a}$ with our encoding.

Step 2: Factoring the propositional encoding. If we view the conversion of a network polynomial into an arithmetic circuit as a factoring process, then the purpose of this second step is to accomplish a similar task but at the logical level. Instead of starting with a polynomial (set of terms), we start with a propositional theory (set of models). And instead of building an arithmetic circuit, we build a Boolean circuit that satisfies certain properties. Specifically, the circuit must be in Negation Normal Form (NNF): a rooted DAG where leaves are labeled with literals, and where internal nodes are labeled with conjunctions or disjunctions; see Figure 6. The NNF must satisfy three properties: (1) conjuncts cannot share variables (decomposability), (2) disjuncts must be logically exclusive (determinism), and (3) disjuncts must be over the same variables (smoothness). The NNF in Figure 6 satisfies the above properties, and encodes the multi-linear function shown in the same figure. In our experimental results, we use a second generation compiler for converting CNFs to NNFs that are decomposable, deterministic and smooth (smooth d-DNNF) [24].

Step 3: Extracting an arithmetic circuit. The purpose of this last step is to extract an arithmetic circuit for the polynomial encoded by an NNF. If $\Delta_{f}$ is an NNF that encodes a network polynomial $f$, and if $\Delta_{f}$ is a smooth d-DNNF, then an arithmetic circuit for the polynomial $f$ can be obtained easily. First, replace and-nodes in $\Delta_{f}$ by multiplications; then replace ornodes by additions; and finally, replace each leaf node labeled with $V_{x}$ by $x$ and each node labeled with $\neg V_{x}$ by 1 . The resulting arithmetic circuit is then guaranteed to correspond to polynomial $f$ [19]. Figure 6 depicts an NNF and its corresponding arithmetic circuit. Note that the generated arithmetic circuit is no larger than the NNF. Hence, if we attempt to minimize the size of NNF, we are also attempting to minimize the size of generated arithmetic circuit.

# 4.3 Encoding Primula's networks 

The encoding step described above is semantic; that is, it describes the theory $\Delta_{f}$ which encodes a multi-linear function by describing its models. As mentioned earlier, the Primula system generates propositional instances of relational models in the form of classical Bayesian networks. We now turn to the question of how to syntactically represent in CNF the multi-linear function of a network so generated. We start with the baseline encoding defined in [19], which applies to any Bayesian network. The CNF has one Boolean variable $I_{\lambda}$ for each indicator variable $\lambda$, and one Boolean variable $P_{\theta}$ for each parameter variable $\theta$. CNF clauses fall into three sets. First, for each network variable $X$ with domain $x_{1}, x_{2}, \ldots, x_{n}$, we have:

$$
\begin{aligned}
& \text { Indicator clauses : } I_{\lambda_{x_{1}}} \vee I_{\lambda_{x_{2}}} \vee \ldots \vee I_{\lambda_{x_{n}}} \\
& \neg I_{\lambda_{x_{i}}} \vee \neg I_{\lambda_{x_{j}}}, \text { for } i<j
\end{aligned}
$$

For example, variable $B$ from Figure 1 generates the following clauses:

$$
I_{\lambda_{b}} \vee I_{\lambda_{\bar{b}}}, \quad \neg I_{\lambda_{b}} \vee \neg I_{\lambda_{\bar{b}}}
$$

These clauses ensure that exactly one indicator variable for $B$ appears in every term of the multi-linear function. The second two sets of clauses correspond to network parameters. In particular, for each parameter $\theta_{x_{n} \mid x_{1}, x_{2}, \ldots, x_{n-1}}$, we have:

$$
\begin{aligned}
& \text { IP clause : } I_{\lambda_{x_{1}}} \wedge I_{\lambda_{x_{2}}} \wedge \ldots \wedge I_{\lambda_{x_{n}}} \Rightarrow P_{\theta_{x_{n} \mid x_{1}, x_{2}, \ldots, x_{n-1}}} \\
& \text { PI clauses : } P_{\theta_{x_{n} \mid x_{1}, x_{2}, \ldots, x_{n-1}}} \Rightarrow I_{\lambda_{x_{i}}}, \text { for each } i
\end{aligned}
$$

For example, parameter $\theta_{b \mid a}$ in Figure 1 generates the following clauses:

$$
I_{\lambda_{a}} \wedge I_{\lambda_{b}} \Rightarrow P_{\theta_{b \mid a}}, \quad P_{\theta_{b \mid a}} \Rightarrow I_{\lambda_{a}}, \quad P_{\theta_{b \mid a}} \Rightarrow I_{\lambda_{b}}
$$

These clauses ensure that $\theta_{b \mid a}$ appears in a term iff the $\lambda_{a}$ and $\lambda_{b}$ appear. The encoding as discussed does not capture information about parameter values (local structure). However, it is quite easy to encode information about determinism within this encoding. Consider again Figure 1 and the parameter $\theta_{b \mid a}=0$, which generates the clauses in Equation 2. Given that this parameter is known to be 0 , all multi-linear terms that contain this parameter must vanish. Therefore, we can suppress the generation of a Boolean variable for this parameter, and then replace the above clauses by the single clause: $\neg I_{\lambda_{a}} \vee \neg I_{\lambda_{b}}$.

This clause has the effect of eliminating all CNF models which correspond to vanishing terms, those containing the parameter $\theta_{b \mid a}$.

To this basic encoding we apply some optimizations:

- Primula generated networks contain only binary variables. Therefore, instead of using one propositional variable for each evidence indicator $\lambda_{x}$, which would be needed in general, we use one propositional variable $I_{X}$ for each Bayesian network variable $X$, where the positive literal $I_{X}$ represents indicator $\lambda_{x}$, and the negative literal $\neg I_{X}$ represents indicator $\lambda_{\bar{x}}$. Not only does this cut the number of indicator variables by half, but it also relieves the need for indicator clauses. For example, without the enhancement, variable $B$ in Figure 1 generates Boolean variables $I_{\lambda_{b}}$ and $I_{\lambda_{\bar{b}}}$ and the two clauses in Equation 1. With the optimization, $B$ generates only a single Boolean variable $I_{B}$ and no clauses. This optimization requires a corresponding modification to the decoding step as indicated below.
- Another enhancement results from the observation that the Boolean indicators and parameters corresponding to the same state of a network root variable are logically equivalent, making it possible to delete the parameter variables and the corresponding IP and PI clauses, which establish the equivalence. The Boolean indicator thus represents both an indicator and a parameter. For example, without the enhancement, parameter $\theta_{a}$ in Figure 1 generates one Boolean variable $P_{\theta_{a}}$ and two clauses, $I_{A} \Rightarrow P_{\theta_{a}}$ and $P_{\theta_{a}} \Rightarrow I_{A}$. With the enhancement, the variable and clauses are omitted. This optimization requires a corresponding modification to the decoding step as indicated below.
- Variables and clauses generated by parameters equal to 1 are redundant and therefore omitted.

Applying these enhancements allows us to create the CNF as follows. For each network variable $X$, we create propositional variable $I_{X}$. If $X$ is not a root, then we perform three more steps. (1) For each network parameter $\theta_{x \mid \mathbf{u}}$ not equal to 0 or 1 , create a propositional variable $P_{\theta_{x \mid \mathbf{u}}}$. (2) For each parameter $\theta_{x \mid u_{1}, u_{2} \ldots, u_{n}}$ equal to 0 , create clause $\neg L_{U_{1}} \vee \neg L_{U_{2}} \vee \ldots \vee \neg L_{U_{n}} \vee \neg L_{X}$, where $L_{U_{i}}$ is a literal over variable $I_{U_{i}}$ whose sign is the the same as $u_{i}$, and similarly for $L_{X}$ with respect to $x$. (3) For each parameter $\theta_{x \mid u_{1}, u_{2}, \ldots, u_{n}}$ not equal to 0 and not equal to 1 , create clauses, $L_{U_{1}} \wedge L_{U_{2}} \wedge \ldots \wedge L_{U_{n}} \wedge L_{x} \Rightarrow P_{\theta_{x \mid u_{1}, \ldots, u_{n}}}$, $P_{\theta_{x \mid u_{1}, \ldots, u_{n}}} \Rightarrow L_{U_{1}}, P_{\theta_{x \mid u_{1}, \ldots, u_{n}}} \Rightarrow L_{U_{2}}, \ldots, P_{\theta_{x \mid u_{1}, \ldots, u_{n}}} \Rightarrow L_{U_{n}}, P_{\theta_{x \mid u_{1}, \ldots, u_{n}}} \Rightarrow L_{X}$, where $L_{U_{i}}$ and $L_{X}$ are as defined earlier. As an example, the CPT for variable $B$ in Figure 1 generates the following clauses:

1st CPT row: $\neg I_{A} \vee \neg I_{B}$
3nd CPT row: $\neg I_{A} \wedge I_{B} \Rightarrow P_{\theta_{b \mid \bar{a}}}, P_{\theta_{b \mid \bar{a}}} \Rightarrow \neg I_{A}, P_{\theta_{b \mid \bar{a}}} \Rightarrow I_{B}$
4th CPT row: $\quad \neg I_{A} \wedge \neg I_{B} \Rightarrow P_{\theta_{\bar{b} \mid \bar{a}}}, P_{\theta_{\bar{b} \mid \bar{a}}} \Rightarrow \neg I_{A}, P_{\theta_{\bar{b} \mid \bar{a}}} \Rightarrow \neg I_{B}$.

Because Primula generates networks with binary variables and nodes with at most three parents, this encoding leads to a CNF whose size is linear in the number of network variables. Table 1 depicts the size of CNF encodings for the relational models with which we experimented.

The special encoding used above calls for a slightly different decoding scheme for transforming a smooth d-DNNF into an arithmetic circuit. Specifically, if $X$ is not a root, then literals $I_{X}$ and $\neg I_{X}$ are replaced with evidence indicators $\lambda_{x}$ and $\lambda_{\bar{x}}$, respectively. If $X$ is a root, then literals $I_{X}$ and $\neg I_{X}$ are replaced with $\lambda_{x} * \theta_{x}$ and $\lambda_{\bar{x}} * \theta_{\bar{x}}$, respectively. Moreover, literals $P_{\theta_{x \mid \mathbf{u}}}$ and $\neg P_{\theta_{x \mid \mathbf{u}}}$ are replaced by $\theta_{x \mid \mathbf{u}}$ and 1 , respectively. Finally, conjunctions and disjunctions are replaced by multiplications and additions.

We close this section by pointing the reader to [25], which discusses more recent and sophisticated encodings to handle Bayesian networks with context-specific-independence [26], multi-valued variables, large CPTs, and lesser amounts of determinism.

# 5 Experimental Results 

We ran our experiments on a 1.6 GHz Pentium M with 2 GB of RAM using a system available for download at http://reasoning.cs.ucla.edu/ace. Table 1 lists for each relational model a number of instances, and for each instance a number of measurements. First is the size and connectivity of the Bayesian network that Primula generated. Primula generates networks in formats acceptable by general purpose tools such as Hugin and Netica, but exact inference in these tools cannot handle most of these networks. Next is the number of variables and clauses in the CNF encodings. Clauses have at most five literals since the networks have at most three parents per node.

Table 1 shows additional findings. First, the table shows the size of the compiled arithmetic circuit in terms of both number of nodes and edges (count and $\log$ base 2). We also show the time it takes to evaluate and differentiate the circuit, averaged over 31 different randomly generated evidence sets. By evaluating and differentiating the circuit, one obtains marginals over all network families, in addition to other probabilities discussed in [2].

The main points to observe are the efficiency of online inference on compiled circuits and the size of these circuits compared to the size and connectivity of the Bayesian networks. Table 1 also shows the time for jointree propagation using the SamIam inference engine (http://reasoning.cs.ucla.edu/samiam) on instances whose cluster size was manageable. One can see the big difference between online inference using the compiled AC and corresponding jointrees.


Table 1
Relational Bayesian networks, their corresponding propositional instances, and the sizes of their CNF encodings.

Table 1 finally shows the compile time to generate the arithmetic circuits. The compile times range from less than a minute to about 60 minutes for the largest model. Yet the time for online inference ranges from milliseconds to about 13 seconds for these models. This clearly shows the benefit of offline compilation in this case, whose time can be amortized over online queries.

Friends and smokers produces networks with particularly high connectivity. We mentioned previously that logical constraints in this model give rise to grounded Bayesian networks with evidence that applies to all queries. One might hope that classical pruning techniques - such as deleting leaf nodes not part of the query or evidence [27] and deleting edges exiting evidence nodes [28]-might reduce the connectivity of these networks, making them accessible to classical inference algorithms. This possibility is not realized though since all of the evidence occur on leaf nodes. However, we can use the method of [29] to place this evidence into the CNF encoding and compile with the evidence. In particular, if we know that network variable $A$ corresponds to a logical constraint that must be true, then we simply add a unit clause $\lambda_{a}$ to the CNF encoding. In fact, injecting these unit clauses into the CNF encoding prior to compilation has a critical effect on both compilation time and AC size, as most of these networks could not be compiled otherwise.

# 6 Conclusion 

We described in this paper an inference system for relational Bayesian networks as defined by Primula. The proposed inference approach is based on compiling propositional instances of these models into arithmetic circuits. The approach exploits determinism in relational models, allowing us to reason efficiently with some relational models whose Primula-generated propositional instances contain thousands of variables, and whose jointrees contain hundreds of variables. The described system appears to significantly expand the scale of Primula-based relational models that can be handled efficiently by exact inference algorithms. It is also equally applicable and effective to any Bayesian network that exhibits similar properties (e.g., determinism), regardless of whether it is synthesized from a relational model.

## Acknowledgments

This work has been partially supported by NSF grant IIS-9988543 and MURI grant N00014-00-1-0617.
