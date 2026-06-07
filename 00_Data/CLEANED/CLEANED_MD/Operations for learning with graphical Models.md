# Operations for Learning with Graphical Models 

Wray L. Buntine<br>WRAY@KRONOS.ARC.NASA.GOV<br>R1ACS \& NASA Ames Research Center, Mail Stop 269-2<br>Moffett Field, CA 94035-1000, USA


#### Abstract

This paper is a multidisciplinary review of empirical, statistical learning from a graphical model perspective. Well-known examples of graphical models include Bayesian networks, directed graphs representing a Markov chain, and undirected networks representing a Markov field. These graphical models are extended to model data analysis and empirical learning using the notation of plates. Graphical operations for simplifying and manipulating a problem are provided including decomposition, differentiation, and the manipulation of probability models from the exponential family. Two standard algorithm schemas for learning are reviewed in a graphical framework: Gibbs sampling and the expectation maximization algorithm. Using these operations and schemas, some popular algorithms can be synthesized from their graphical specification. This includes versions of linear regression, techniques for feed-forward networks, and learning Gaussian and discrete Bayesian networks from data. The paper concludes by sketching some implications for data analysis and summarizing how some popular algorithms fall within the framework presented.

The main original contributions here are the decomposition techniques and the demonstration that graphical models provide a framework for understanding and developing complex learning algorithms.


## 1. Introduction

A probabilistic graphical model is graph where the nodes represent variables and the arcs (directed or undirected) represent dependencies between variables. They are used to define a mathematical form for the joint or conditional probability distribution between variables. Graphical models come in various forms: Bayesian networks used to represent causal and probabilistic processes, data-flow diagrams used to represent deterministic computation, influence diagrams used to represent decision processes, and undirected Markov networks (random fields) used to represent correlation for images and hidden causes.

Graphical models are used in domains such as diagnosis, probabilistic expert systems, and, more recently, in planning and control (Dean \& Wellman, 1991; Chan \& Shachter, 1992), dynamic systems and time-series (Kjæruff, 1992; Dagum, Galper, Horvitz, \& Seiver, 1994), and general data analysis (Gilks et al., 1993a) and statistics (Whittaker, 1990). This paper shows the task of learning can also be modeled with graphical models. This metalevel use of graphical models was first suggested by Spiegelhalter and Lauritzen (1990) in the context of learning probabilities for Bayesian networks.

Graphical models provide a representation for the decomposition of complex problems. They also have an associated set of mathematics and algorithms for their manipulation. When graphical models are discussed, both the graphical formalism and the associated algorithms and mathematics are implicitly included. In fact, the graphical formalism is unnecessary for the technical development of the approach, but its use conveys the important

structural information of a problem in a natural visual manner. Graphical operations manipulate the underlying structure of a problem unhindered by the fine detail of the connecting functional and distributional equations. This structuring process is important in the same way that a high-level programming language leads to higher productivity over assembly language.

A graphical model can be developed to represent the basic prediction done by linear regression, a Bayesian network for an expert system, a hidden Markov model, or a connectionist feed-forward network (Buntine, 1994). A graphical model can also be used to represent and reason about the task of learning the parameters, weights, and structure of each of these representations. An extension of the standard graphical model that allows this kind of learning to be represented is used here. The extension is the notion of a plate introduced by Spiegelhalter ${ }^{1}$ (1993). Plates allow samples to be explicitly represented on the graphical model, and thus reasoned about and manipulated. This makes data analysis problems explicit in much the same way that utility and decision nodes are used for decision analysis problems (Shachter, 1986).

This paper develops a framework in which the basic computational techniques for learning can be directly applied to graphical models. This forms the basis of a computational theory of Bayesian learning using the language of graphical models. By a computational theory we mean that the approach shows how a wide variety of learning algorithms can be created from graphical specifications and a few simple algorithmic criteria. The basic computational techniques of probabilistic (Bayesian) inference used in this computational theory of learning are widely reviewed (Tanner, 1993; Press, 1989; Kass \& Raftery, 1993; Neal, 1993; Bretthorst, 1994). These include various exact methods, Markov chain Monte Carlo methods such as Gibbs sampling, the expectation maximization (EM) algorithm, and the Laplace approximation. More specialized computational techniques also exist for handling missing values (Little \& Rubin, 1987), making a batch algorithm incremental, and adapting an algorithm to handle large samples. With creative combination, these techniques are able to address a wide range of data analysis problems.

The paper provides the blueprint for a software toolkit that can be used to construct many data analysis and learning algorithms based on a graphical specification. The conceptual architecture for such a toolkit is given in Figure 1. Probability and decision theory are used to decompose a problem into a computational prescription, and then search and optimization techniques are used to fill the prescription. A version of this toolkit already exists using Gibbs sampling as the general computational scheme (Gilks et al., 1993b). The list of algorithms that can be constructed in one form or another by the scheme in Figure 1 is impressive. But the real gain from the scheme does not arise from the potential re-implementation of existing software, but from understanding gained by putting these in a common language, the ability to create novel hybrid algorithms, and the ability to tailor special purpose algorithms for specific problems.

This paper is tutorial in the sense that it collects material from different communities and presents it in the language of graphical models. This paper introduces graphical models, to represent first-order inference and learning. Second, this paper develops and reviews a number of operations on graphical models. Finally, this paper gives some examples

[^0]
[^0]:    1. The notion of a "replicated node" was my version of this developed independently. I have adopted the notation of Spiegelhalter and colleagues for uniformity.

![img-0.jpeg](img-0.jpeg)

Figure 1: A software generator
of developing learning algorithms using combinations of the basic operations. The main original contribution is the demonstration that graphical models provide a framework for understanding and developing complex learning algorithms.

In more detail, the paper covers the following topics.
Introduction to graphical models: Graphical models are used in two ways.
Graphical models for representing inference tasks: Section 2 reviews some basics of graphical models. Graphical models provide a means of representing patterns of inference.
Adapting graphical representations to represent learning: Section 3 discusses the representation of the problem of learning within graphical models using the notion of a plate.

Operations on graphical models: Operations take a graphical representation of a learning problem and simplify it or perform an important calculation required to solve the problem.

Operations using closed-form solutions: Section 4 covers those classes of learning problems where closed-form solutions to learning are known. This section adapts standard statistical methods to graphical models.
Other basic operations: Other operations on graphs are required to be able to handle more complex problems. These are covered in Section 6, including:
Decomposition: Breaking a learning problem into independent components and evaluating each component.
Differentiation: Computing the derivative of a probability or log probability with respect to variables on the graph. Differentiation can be decomposed into operations local to groups of nodes in the graph as is popular in neural networks.
Some approximate operations: Some approximate algorithms follow naturally from the above methods. Section 7 reviews Gibbs sampling and its deterministic cousin, the EM algorithm.

Some example algorithms: The closed-form solutions to learning can sometimes be used to form a fast inner loop of more complex algorithms. Section 8 illustrates how graphical models help here.

The conclusion lists some common algorithms and their derivation within the above framework. Proofs of lemmas and theorems are collected in Appendix A.

# 2. Introduction to graphical models 

This section introduces graphical models. The brief tour is necessary before introducing the operations for learning.

Graphical models offer a unified qualitative and quantitative framework for representing and reasoning with probabilities and independencies. They combine a representation for uncertain problems with techniques for performing inference. Flexible toolkits and systems exist for applying these techniques (Srinivas \& Breese, 1990; Andersen, Olesen, Jensen, \& Jensen, 1989; Cowell, 1992). Graphical models are based on the notion of independence, which is worth repeating here.

Definition 2.1 $A$ is independent of $B$ given $C$ if $p(A, B \mid C)=p(A \mid C) p(B \mid C)$ whenever $p(C) \neq 0$, for all $A, B, C$.

The theory of independence as a basic tool for knowledge structuring is developed by Dawid (1979) and Pearl (1988). A graphical model can be equated with the set of probability distributions that satisfy its implied constraints. Two graphical models are equivalent probability models if their corresponding sets of satisfying probability distributions are equivalent.

### 2.1 Directed graphical models

The basic kind of graphical model is the Bayesian network, also called belief net, which is most popular in artificial intelligence. See Charniak (1991), Shachter and Heckerman (1987), and Pearl (1988) for an introduction. This is also a graphical representation for a Markov chain. A Bayesian network is a graphical model that uses directed arcs exclusively to form a directed acyclic graph (DAG), (i.e., a directed graph without directed cycles). Figure 2, adapted from (Shachter \& Heckerman, 1987) shows a simple Bayesian network for
![img-1.jpeg](img-1.jpeg)

Figure 2: A simplified medical problem
a simplified medical problem. The graphical model represents a conditional decomposition of the joint probability (see (Lauritzen, Dawid, Larsen, \& Leimer, 1990) for more details and interpretations). This decomposition works as follows (full variable names have been

abbreviated).

$$
\begin{aligned}
& p(A g e, O c c, \text { Clim, Dis, Symp }[M)= \\
& \quad p(A g e \mid M) p(O c c \mid M) p(\text { Clim } \mid M) p(\text { Dis } \mid \text { Age }, \text { Occ, Clim, } M) p(\text { Symp } \mid \text { Dis }, M)
\end{aligned}
$$

where $M$ is the conditioning context, for instance the expert's prior knowledge and the choice of the graphical model in Figure 2. Each variable is written conditioned on its parents, where parents $(x)$ is the set of variables with a directed arc into $x$. The general form for this equation for a set of variables $X$ is:

$$
p(X \mid M)=\prod_{x \in X} p(x \mid \operatorname{parents}(x), M)
$$

This equation is the interpretation of a Bayesian network used in this paper.

# 2.2 Undirected graphical models 

Another popular form of graphical model is an undirected graph, sometimes called a Markov network (Pearl, 1988). This is a graphical model for a Markov random field. Markov random fields became used in statistics with the advent of the Hammersley-Clifford theorem (Besag, York, \& Mollie, 1991). A variant of the theorem is given later in Theorem 2.1. Markov random fields are used in imaging and spatial reasoning (Ripley, 1981; Geman \& Geman, 1984; Besag et al., 1991) and various stochastic models in neural networks (Hertz, Krogh, \& Palmer, 1991). Undirected graphs are also important because they simplify the theory of Bayesian networks (Lauritzen et al., 1990).

Figure 3 shows a simple $4 \times 4$ image and an undirected model for the image. This model
![img-2.jpeg](img-2.jpeg)

Figure 3: A simple $4 \times 4$ mage and its graphical model
is based on the first degree Markov assumption; that is, the current pixel is only directly influenced by pixels positioned next to it, as indicated by the undirected arcs between variables $p_{i, j}$ and $p_{i, j+1}, p_{i, j}$ and $p_{i+1, j}$, etc. Each node $x$ (corresponding to a pixel) has its set of neighbors-those nodes it is directly connected to by an undirected arc. For instance, the neighbors of $p_{1,1}$ are $p_{1,2}, p_{2,2}$ and $p_{2,1}$. For the variable/node $x$, denote these by neighbors $(x)$.

In general, there is no formula for undirected graphs in terms of conditional probabilities corresponding to Equation (1) for the Bayesian network of Figure 2. However, a functional decomposition does exist in another form based on the maximal cliques in Figure 3. Maximal

cliques are subgraphs that are fully connected but are not strictly contained in other fully connected subgraphs. These are the 9 sets of $2 \times 2$ cliques such as $\left\{p_{1,2}, p_{1,3}, p_{2,2}, p_{2,3}\right\}$. The interpretation of the graph is that the joint probability is a product over functions of the maximal cliques.

$$
\begin{aligned}
& p\left(p_{1,1}, \ldots, p_{4,4}\right)= \\
& \quad f_{1}\left(p_{1,1}, p_{1,2}, p_{2,1}, p_{2,2}\right) f_{2}\left(p_{1,2}, p_{1,3}, p_{2,2}, p_{2,3}\right) f_{3}\left(p_{1,3}, p_{1,4}, p_{2,3}, p_{2,4}\right) \\
& \quad f_{4}\left(p_{2,1}, p_{2,2}, p_{3,1}, p_{3,2}\right) f_{5}\left(p_{2,2}, p_{2,3}, p_{3,2}, p_{3,3}\right) f_{6}\left(p_{2,3}, p_{2,4}, p_{3,3}, p_{3,4}\right) \\
& \quad f_{7}\left(p_{3,1}, p_{3,2}, p_{4,1}, p_{4,2}\right) f_{8}\left(p_{3,2}, p_{3,3}, p_{4,2}, p_{4,3}\right) f_{9}\left(p_{3,3}, p_{3,4}, p_{4,3}, p_{4,4}\right)
\end{aligned}
$$

for some functions $f_{1}, \ldots, f_{9}$ defined up to a constant. From this formula it follows that $p_{1,3}$ is conditionally independent of its non-neighbors given its neighbors $p_{1,2}, p_{2,2}, p_{2,3}, p_{1,4}, p_{2,4}$.

The general form for Equation (3) for a set of variables $X$ is given in the next theorem. Compare this with Equation 2.

Theorem 2.1 An undirected graph $G$ is on variables in the set $X$. The set of maximal cliques on $G$ is $\operatorname{Cliques}(G) \subset 2^{X}$. The distribution $p(X)$ (probability or probability density) is strictly positive in the domain $\times_{x \in X} \operatorname{domain}(x)$. Then under the distribution $p(X), x$ is independent of $X-\{x\}-$ neighbors $(x)$ given neighbors $(x)$ for all $x \in X$ (Frydenberg (1990) refers to this condition as local G-Markovian) if, and only if, $p(X)$ has the functional representation

$$
p(X)=\prod_{C \in \operatorname{Cliques}(G)} f_{C}(C)
$$

for some functions $f_{C}>0$.
The general form of this theorem for finite discrete domains is called the HammersleyClifford Theorem (Geman, 1990; Besag et al., 1991). Again, this equation is used as the interpretation of a Markov network.

# 2.3 Conditional probability models 

Consider the conditional probability $p(\operatorname{Dis} \mid \text { Age }, \text { Occ }, \text { Clim })$ found in the simple medical problem from Figure 2 and Equation (1). This conditional probability models how the disease should vary for given values of age, occupation, and climate. Class probability trees (Breiman, Friedman, Olshen, \& Stone, 1984; Quinlan, 1992), graphs and rules (Rivest, 1987; Oliver, 1993; Kohavi, 1994), and feed-forward networks are representations devised to express conditional models in different ways. In statistics, the conditional distributions are also represented as regression models and generalized linear models (McCullagh \& Nelder, 1989).

The models of Figure 2 and Equation (1) and Figure 3 and Equation (3) show how the joint distribution is composed from simpler components. That is, they give a global model of variables in a problem. The conditional probability models, in contrast, give a model for a subset of variables conditioned on knowing the values of another subset. In diagnosis the concern may be a particular direction for reasoning, such as predicting the disease given patient details and symptoms, so the full joint model provides unnecessary detail. The full joint model may require extra parameters and thus more data to learn. In

supervised learning applications, the general view is that conditional models are superior unless prior knowledge dictates a full joint model is more appropriate. This distinction is sometimes referred to as the diagnostic versus the discriminant approach to classification (Dawid, 1976).

There are a number of ways for explicitly representing conditional probability models. Any joint distribution implicitly gives the conditional distribution for any subset of variables, by definition of conditional probability. For instance, if there is a model for $p(A g e, O c c, C l i m, D i s, S y m p)$, then by the definition of conditional probability a conditional model follows:

$$
\begin{aligned}
p(\text { Dis } \mid \text { Age }, \text { Occ }, \text { Clim, Symp }) & =\frac{p(\text { Age }, \text { Occ }, \text { Clim, Dis, Symp })}{\sum_{\text {Dis }} p(\text { Age }, \text { Occ }, \text { Clim, Dis, Symp })} \\
& \propto p(\text { Age }, \text { Occ }, \text { Clim, Dis, Symp })
\end{aligned}
$$

Conditional distributions can also be represented by a single node that is labeled to identify which functional form the node takes. For instance, in the graphs to follow, labeled Gaussian nodes, linear nodes, and other standard forms are all used. Conditional models such as rule sets and feed-forward networks can be constructed by the use of special deterministic nodes. For instance, Figure 4 shows four model constructs. In each case, the input variables to the
![img-3.jpeg](img-3.jpeg)

Figure 4: Graphical conditional models
conditional models represented have been shaded. This shading means the values of these variables are known or given. In Figure 4(b), the shading indicates that the value for $x$ is known, but the value for $c$ is unknown. Presumably $c$ will be predicted using $x$. Figure 4(a) represents a rule set. The nodes with double ovals are deterministic functions of their inputs in contrast to the usual nodes, which are probabilistic functions. This means that the value for $r u l e_{1}$ is a deterministic function of $x_{1}, \ldots, x_{n}$. Notice that this implies that the values for rule $_{1}$ and the others are known as well. The conditional probability for a deterministic node, as required for Equation (2), is treated as a delta function. Figure 4(c) corresponds to the statement:

$$
p\left(\text { unit } \mid x_{1}, \ldots, x_{n}\right)=\delta_{\text {unit }}=f\left(x_{1}, \ldots, x_{n}\right)= \begin{cases}1 & \text { if unit }=f\left(x_{1}, \ldots, x_{n}\right) \\ 0 & \text { otherwise }\end{cases}
$$

for some function $f$ not specified. A Bayesian network constructed entirely of double ovals is equivalent to a data flow graph where the inputs are shaded. The analysis of deterministic nodes in Bayesian networks and, more generally, in influence diagrams is considered by Shachter (1990). For some purposes, deterministic nodes are best treated as intermediate variables and removed from the problem. The method for doing this, variable elimination, is given later in Lemma 6.1.

The logical or conjunctive form of each rule in Figure 4(a) is not expressed in the graph, and presumably would be given in the formulas accompanying the graph, however the basic functional structure of the rule set exists. In Figure 4(b), a node has been labeled with its functional type. The functional type for this node with a Boolean variable $c$ is the function,

$$
p(c=1 \mid x)=\frac{1}{1+e^{x}}=\operatorname{Sigmoid}(x)=\text { Logistic }^{-1}(x)
$$

which maps a real value $x$ onto a probability in $(0,1)$ for the binary variable $c$. This function is the inverse of the logistic or logit function used in generalized linear models (McCullagh \& Nelder, 1989), and is also the sigmoid function used in feed-forward neural networks. Figure 4(c) uses a deterministic node to reproduce a single unit from a connectionist feedforward network, where the unit's activation is computed via a sigmoid function. Figure 4(d) is a simple univariate Gaussian, which makes $y$ normally distributed with mean $\mu$ and standard deviation $\sigma$. Here the node is labeled in italics to indicate its conditional type.

At a more general level, networks can be conditional. Figure 5 shows two conditional versions of the simple medical problem. If the shading of nodes is ignored, the joint proba-
![img-4.jpeg](img-4.jpeg)

Figure 5: Two equivalent conditional models of the medical problem
bility, $p(A g e, O c c, C l i m, D i s, S y m p)$ for the two graphs (a) and (b) is:

$$
\begin{aligned}
& p(A g e) p(O c c \mid A g e) p(C l i m \mid A g e, O c c) p(D i s \mid A g e, O c c, C l i m) p(S y m p \mid A g e, D i s) \\
& p(A g e) p(O c c) p(C l i m) p(D i s \mid A g e, O c c, C l i m) p(S y m p \mid A g e, D i s)
\end{aligned}
$$

However, because four of the five nodes are shaded, this means their values are known. The conditional distributions computed from the above are identical:

$$
\begin{aligned}
& p(D i s \mid A g e, O c c, C l i m, S y m p) \\
& \quad=\frac{p(D i s \mid A g e, O c c, C l i m) p(S y m p \mid A g e, D i s)}{\sum_{D i s} p(D i s \mid A g e, O c c, C l i m) p(S y m p \mid A g e, D i s)}
\end{aligned}
$$

Why do these distinct graphs become identical when viewed from the conditional perspective? Because conditional components of the model corresponding to age, occupation and climate cancel out when the conditional distribution is formed. However, the symptoms node has the unknown variable disease as a parent, so the arc from age to symptoms is kept.

More generally, the following simple lemma applies and is derived directly from Equation 2 .

Lemma 2.1 Given a Bayesian network $G$ with some nodes shaded representing a conditional probability distribution, if a node $X$ and all its parents have their values given, then the Bayesian network $G^{\prime}$ created by deleting all the arcs into $X$ represents an equivalent probability model to the Bayesian network $G$.

This does not mean, for instance in the graphs just discussed, that there is no causal or influential links between the variables age, occupation, and climate, rather that their effects become irrelevant in the conditional model considered because their values are already known. A corresponding result holds for undirected graphs, and follows directly from Theorem 2.1.

Lemma 2.2 Given an undirected graph $G$ with some nodes shaded representing a conditional probability distribution, delete an arc between nodes $A$ and $B$ if all their common neighbors are given. The resultant graph $G^{\prime}$ represents an equivalent probability model to the graph $G$.

# 2.4 Mixed graphical models 

Undirected and directed graphs can also be mixed in a sequence. These mixed graphs are called chain graphs (Wermuth \& Lauritzen, 1989; Frydenberg, 1990). These chain graphs are sometimes used here, However, a precise understanding of them is not required for this paper. A simple chain graph is given in Figure 6. In this case, the single disease node
![img-5.jpeg](img-5.jpeg)

Figure 6: An expanded medical problem
and single symptom node of Figure 2 are expanded to represent the case where there are two possibly co-occurring diseases and three possibly co-occurring symptoms. The medical specialist may have said something like: "Lung disease and heart disease can influence each other, or may have some hidden common cause; however, it is often difficult to tell which is the cause of which, if at all." In the causal model, join the two disease nodes by an undirected arc to represent direct influence. Likewise for the symptom nodes. The resultant joint distribution takes the form:

$$
\begin{gathered}
p(A g e, O c c, \text { Clim, Heart-Dis, Lung-Dis, Symp-A, Symp-B, Symp-C })= \\
p(\text { Age }) p(\text { Occ }) p(\text { Clim }) p(\text { Heart-Dis, Lung-Dis } \mid \text { Age, Occ, Clim }) \\
p(\text { Symp-A, Symp-B, Symp-C } \mid \text { Heart-Dis, Lung-Dis })
\end{gathered}
$$

where the last two conditional probabilities can take on an arbitrary form. Notice that the probabilities now have more than one variable on the left side.

In general, a chain graph consists of a chain of undirected graphs connected by directed arcs. Any cycle through the graph cannot have directed arcs going in opposite directions. Chain graphs can be interpreted as Bayesian networks defined over the components of the chain instead of the original variables. This goes as follows:

Definition 2.2 Given a subgraph $G$ over some variables $X$, the chain components are subsets of $X$ that are maximal undirected connected subgraphs in a chain graph $G$ (Frydenberg, 1990). Furthermore, let chain-components $(A)$ denote all nodes in the same chain component as at least one variable in $A$.

The chain components for the graph above, ordered consistently with the directed arcs, are $\{A g e\},\{O c c\},\{C l i m\},\{H e a r t-D i s, L u n g-D i s\}$, and $\{S y m p-A, S y m p-B, S y m p-C\}$. Informally, a chain graph over variables $X$ with chain components given by the set $T$ is interpreted first as the decomposition corresponding to the decomposition of Bayesian networks in Equation (2):

$$
p(X \mid M)=\prod_{\tau \in T} p(\tau \mid \text { parents }(\tau), M)
$$

where

$$
\operatorname{parents}(A)=\bigcup_{a \in A} \operatorname{parents}(a)-A
$$

Each component probability $p(\tau \mid$ parents $(\tau), M)$ has a form similar to Equation (4).
Sometimes, to process graphs of this form without having to consider the mathematics of chain graphs, the following device is used.

Comment 2.1 When a set of nodes $U$ in a chain graph form a clique (a fully connected subgraph), and all have identical children and parents otherwise, then the set of nodes can be replaced a single node representing the cross product of the variables.

This operation for Figure 6 is done to get Figure 7. Furthermore, chain graphs are sometimes
![img-6.jpeg](img-6.jpeg)

Figure 7: An expanded medical problem
used here where Bayesian networks can also be used. In this case:
Comment 2.2 The chain components of a Bayesian network are the singleton sets of individual variables in the graph. Furthermore, chain-components $(A)=A$.

Chain graphs can be decomposed into a chain of directed and undirected graphs. An example is given in Figure 8. Figure 8(a) shows the original chain graph. Figure 8(b) shows
![img-7.jpeg](img-7.jpeg)

Figure 8: Decomposing a chain graph
its directed and undirected components together with the Bayesian network on the right showing how they are pieced together. Having done this decomposition, the components are analyzed using all the machinery of directed and undirected graphs. The interpretation of these graphs in terms of independence statements and the implied functional form of the joint probability is a combination of the previous two forms given in Equation (2) and Theorem 2.1, based on (Frydenberg, 1990, Theorem 4.1), and on the interpretation of conditional graphical models in Section 2.3.

# 3. Introduction to learning with graphical models 

A simplified inference problem is represented in Figure 9. Here, the nodes $v a r_{1}, v a r_{2}$ and $v a r_{3}$ are shaded. This represents that the value of these nodes is given, so the inference task is to predict the value of the remaining variable class. This graph matches the so-called "idiot's" Bayes classifier (Duda \& Hart, 1973; Langley, Iba, \& Thompson, 1992) used in supervised learning for its speed and simplicity. The probabilities on this network are easily learned from data about the three input variables $v a r_{1}, v a r_{2}$ and $v a r_{3}$, and class. This graph also matches an unsupervised learning problem where the class class is not in the data but is hidden. An unsupervised learning algorithm learns hidden classes (Cheeseman, Self, Kelly, Taylor, Freeman, \& Stutz, 1988; McLachlan \& Basford, 1988).
![img-8.jpeg](img-8.jpeg)

Figure 9: A simple classification problem

The implied joint for these variables read from the graph is:

$$
p\left(\text { class }, v a r_{1}, v a r_{2}, v a r_{3}\right)=p(\text { class }) p\left(v a r_{1} \mid \text { class }\right) p\left(v a r_{2} \mid \text { class }\right) p\left(v a r_{3} \mid \text { class }\right)
$$

The Bayesian classifier gets its name because it is derived by applying Bayes theorem to this joint to get the conditional formula:

$$
p\left(\text { class } \mid v a r_{1}, v a r_{2}, v a r_{3}\right)=\frac{p\left(\text { class }\right) p\left(v a r_{1} \mid \text { class }\right) p\left(v a r_{2} \mid \text { class }\right) p\left(v a r_{3} \mid \text { class }\right)}{\sum_{\text {class }} p\left(\text { class }\right) p\left(v a r_{1} \mid \text { class }\right) p\left(v a r_{2} \mid \text { class }\right) p\left(v a r_{3} \mid \text { class }\right)}
$$

The same formula is used to predict the hidden class for objects in the simple unsupervised learning framework. Again, this formula, and corresponding formula for more general classifiers, can be found automatically by using exact methods for inference on Bayesian networks.

Consider the simple model given in Figure 9. If the matching unsupervised learning problem for this model was represented, a sample of $N$ cases of the variables would be observed, with the first case being $v a r_{1,1}, v a r_{2,1}, v a r_{3,1}$, and the $N$-th case being $v a r_{1, N}$, $v a r_{2, N}, v a r_{3, N}$. The corresponding hidden classes, class $_{1}$ to class $_{N}$, would not be observed, but interest would be in performing inference about the parameters needed to specify the hidden classes. The learning problem is represented in Figure 10. This includes two added features: an explicit representation of the model parameters $\phi$ and $\theta$, and a representation of the sample as $N$ repeated subgraphs. The parameter $\phi$ (a vector of class probabilities)
![img-9.jpeg](img-9.jpeg)

Figure 10: Learning the simple classification
gives the proportions for the hidden classes, and the three parameters $\theta_{1}, \theta_{2}$ and $\theta_{3}$ give how the variables are distributed within each hidden class. For instance, if there are 10 classes, then $\phi$ is a vector of 10 class probabilities such that the prior probability of a case being in class $c$ is $\phi_{c}$. If $v a r_{1}$ is a binary variable, then $\theta_{1}$ would be 10 probabilities, one for each class, such that if the case is known to be in class $c$, then the probability $v a r_{1}$ is true is given by $\theta_{1, c}$ and the probability $v a r_{1}$ is false is given by $1-\theta_{1, c}$. This yields the following equations:

$$
\begin{aligned}
p(\text { class }=c \mid \phi, M) & =\phi_{c} \\
p\left(v a r_{j}=\text { true } \mid \text { class }=c, \theta_{j}, M\right) & =\theta_{j, c}
\end{aligned}
$$

The unknown model parameters $\phi, \theta_{1}, \theta_{2}$ and $\theta_{3}$ are included in the graphical model to explicitly represent all unknown variables and parameters in the learning problem.

# 3.1 Introduction to Bayesian learning 

Now is a useful time to introduce the basic terminology of Bayesian learning theory. This is not an introduction to the field. Introductions are given in (Bretthorst, 1994; Press, 1989; Loredo, 1992; Bernardo \& Smith, 1994; Cheeseman, 1990). This section reviews notions such as the sample likelihood and Bayes factor, important for subsequent results.

For the above unsupervised learning problem there is the model, $M$, which is the use of the hidden class and the particular graphical structure of Figure 10. There are data assumed to be independently sampled, and there are the parameters of the model ( $\phi, \theta_{1}$, etc.). In order to use the theory, it must be assumed that the model is correct. That is, the "true" distribution for the data can be assumed to come from this model with some parameters. In practice, hopefully the model assumptions are sufficiently close to the truth. Different sets of model assumptions may be tried. Typically, the "true" model parameters are unknown, although there may be some rough idea about their values. Sometimes, several models are considered (for instance different kinds of Bayesian networks), but it is assumed that just one of them is correct. Model selection or model averaging methods are used to deal with them.

For the Bayesian classifier above, a subjective probability is placed over the model parameters, in the form $p\left(\phi, \theta_{1}, \theta_{2}, \theta_{3} \mid M\right)$. This is called the prior probability. Bayesian statistics and decision theory is distinguished from all other statistical approaches in that it places initial probability distributions, the prior probability, over unknown model parameters. If the model is a feed-forward neural network, then a prior probability needs to be placed over the network weights and the standard deviation of the error. If the model is linear regression with Gaussian error, then it is over the linear parameters $\theta$ and the standard deviation of the error. Prior probabilities are an active area of research and are discussed in most introductions to Bayesian methods.

The next important component is the sample likelihood, which, on the basis of the model assumptions $M$ and given a set of parameters $\phi, \theta_{1}, \theta_{2}$ and $\theta_{3}$, says how likely the sample of data was. This is $p\left(\right.$ sample $\left.\mid \phi, \theta_{1}, \theta_{2}, \theta_{3}, M\right)$. The model needs to completely determine the sample likelihood. The sample likelihood is the basis of the maximum likelihood principle and many hypothesis testing methods (Casella \& Berger, 1990). This combines with the prior to form the posterior probability:

$$
p\left(\phi, \theta_{1}, \theta_{2}, \theta_{3} \mid \text { sample }, M\right)=\frac{p\left(\text { sample } \mid \phi, \theta_{1}, \theta_{2}, \theta_{3}, M\right) p\left(\phi, \theta_{1}, \theta_{2}, \theta_{3} \mid M\right)}{p(\text { sample } \mid M)}
$$

This equation is Bayes theorem and the term $p($ sample $\mid M)$ is derived from the prior and sample likelihood using an integration or sum that is often difficult to do:

$$
p(\text { sample } \mid M)=\int_{\phi, \theta_{1}, \theta_{2}, \theta_{3}} p\left(\text { sample } \mid \phi, \theta_{1}, \theta_{2}, \theta_{3}, M\right) p\left(\phi, \theta_{1}, \theta_{2}, \theta_{3} \mid M\right) \mathrm{d}\left(\phi, \theta_{1}, \theta_{2}, \theta_{3}\right)
$$

This term is called the evidence for model $M$, or model likelihood, and is the basis for most Bayesian model selection, model averaging methods, and Bayesian hypothesis testing

methods using Bayes factors (Smith \& Spiegelhalter, 1980; Kass \& Raftery, 1993). The Bayes factor is a relative quantity used to compare one model $M_{1}$ with another $M_{2}$ :

$$
\text { Bayes-factor }\left(M_{2}, M_{1}\right)=\frac{p\left(\text { sample } \mid M_{2}\right)}{p\left(\text { sample } \mid M_{1}\right)}
$$

Kass and Raftery (1993) review the large variety of methods available for computing or estimating the evidence for a model including numerical integration, importance sampling, and the Laplace approximation. In implementation, the log of the Bayes factor is used to keep the arithmetic within reasonable bounds. The log of the evidence can still produce large numbers, and since rounding errors in floating point arithmetic scales with the order of magnitude, the log Bayes factor is the preferred quantity to consider in implementation. The evidence is often simpler in mathematical analysis. The Bayes factor is the Bayesian equivalent to the likelihood ratio test used in orthodox statistics and developed by Wilks. See Casella and Berger (1990) for an introduction and Vuong (1989) for a recent review.

The evidence and Bayes factors are fundamental to Bayesian methods. It is often the case that a complex "non-parametric" model (a statistical term that loosely translates as "many and varied parameter" model) be used for a problem, rather than a simple model with some fixed number of parameters. Examples of such models are decision trees, most neural networks, and Bayesian networks. For instance, suppose two models are proposed with $M_{1}$ and $M_{2}$ being two Bayesian networks suggested by the domain expert. These are given in Figure 11. They are over two multinomial variables $v a r_{1}$ and $v a r_{2}$ and two Gaussian variables $x_{1}$ and $x_{2}$. Model $M_{2}$ has an additional arc going from the discrete variable $v a r_{2}$ to the real valued variable $x_{1}$.
![img-10.jpeg](img-10.jpeg)

Figure 11: Two graphical models. Which should learning select?
The parameters $\theta_{1}, \theta_{2}, \mu_{1}, \sigma_{1}, \mu_{2}, \sigma_{2}$ for model $M_{1}$ parameterize probability distributions for the first Bayesian network, and the parameters $\theta_{1}, \theta_{2}, \mu_{1}^{\prime}, \sigma_{1}^{\prime}, \mu_{2}, \sigma_{2}$ for the second. The task is to learn not only a set of parameters, but also to select a Bayesian network from the two. The Bayes factor gives the comparative worth of the two models. This simple example extends in principle to selecting a single decision tree, rule set, or Bayesian network from

the huge number available from attributes in the domain. In this case compare the posterior probabilities of the two models $p\left(M_{1} \mid\right.$ sample $)$ and $p\left(M_{2} \mid\right.$ sample $)$. Assuming the truth falls in one or other model, the first is computed using Bayes theorem as:

$$
\begin{aligned}
p\left(M_{1} \mid \text { sample }\right) & =\frac{p(\text { sample } \mid M_{1}) p\left(M_{1}\right)}{p(\text { sample } \mid M_{1}) p\left(M_{1}\right)+p(\text { sample } \mid M_{2}) p\left(M_{2}\right)} \\
& =\frac{1}{1+\text { Bayes-factor }\left(M_{2}, M_{1}\right) \frac{p\left(M_{2}\right)}{p\left(M_{1}\right)}}
\end{aligned}
$$

More generally, when multiple models exist, it still holds that:

$$
\frac{p\left(M_{2} \mid \text { sample }\right)}{p\left(M_{1} \mid \text { sample }\right)}=\text { Bayes-factor }\left(M_{2}, M_{1}\right) \frac{p\left(M_{2}\right)}{p\left(M_{1}\right)}
$$

Notice that the computation requires of each model its prior and its evidence. The second form reduces the computation to the relative quantity being the Bayes factor, and a ratio of the priors. Bayesian hypothesis testing corresponds to checking if the Bayes factor of the null hypothesis compared to the alternative hypothesis is very small or very large. Bayesian model building corresponds to searching for a model with a high value of $p(M \mid$ sample $) \propto p($ sample $\mid M) p(M)$, which usually involves comparing Bayes factors of this model with alternative models during the search.

When making an estimate about a new case $x$, the estimate becomes:

$$
\begin{aligned}
& p\left(x \mid \text { sample, }\left\{M_{1}, M_{2}\right\}\right) \\
& \quad=p\left(M_{1} \mid \text { sample }\right) p\left(x \mid \text { sample }, M_{1}\right)+p\left(M_{2} \mid \text { sample }\right) p\left(x \mid \text { sample }, M_{2}\right) \\
& \quad=\frac{p(\text { sample } \mid M_{1}) p\left(M_{1}\right) p\left(x \mid \text { sample }, M_{1}\right)+p(\text { sample } \mid M_{2}) p\left(M_{2}\right) p\left(x \mid \text { sample }, M_{2}\right)}{p(\text { sample } \mid M_{1}) p\left(M_{1}\right)+p(\text { sample } \mid M_{2}) p\left(M_{2}\right)}
\end{aligned}
$$

The predictions of the individual models is averaged according to the model posteriors $p\left(M_{1} \mid\right.$ sample $)$ and $p\left(M_{2} \mid\right.$ sample $)=1-p\left(M_{1} \mid\right.$ sample $)$. The general components used in this calculation are the model priors, the evidence for each model or the Bayes factors, and the prediction for the new case made for each model.

This process of model averaging happens in general. A typical non-parametric problem would be to learn class probability trees from data. The number of class probability tree models is super-exponential in the number of features. Even when learning Bayesian networks from data the number of Bayesian networks is at best quadratic in the number of features. Doing an exhaustive search of these spaces and doing the full averaging implied by the equation above is computationally infeasible in general. It may be the case that 15 models have posterior probabilities $p(M \mid$ sample $)$ between 0.1 and 0.01 , and several thousand more models have posteriors from 0.001 to 0.0000001 . Rather than select a single model, a representative set of several models might be chosen and averaged using the identity:

$$
p(x \mid \text { sample })=\sum_{i} p\left(M_{i} \mid \text { sample }\right) p\left(x \mid \text { sample }, M_{i}\right)
$$

The general averaging process is depicted in Figure 12 where a Gibbs sampler is used to generate a representative subset of models with high posterior. This kind of computation is done for class probability trees where representative sets of trees are found using a heuristic branch and bound algorithm (Buntine, 1991b), and for learning Bayesian networks (Madigan \& Raftery, 1994). A sampling scheme for Bayesian networks is presented in Section 8.3.

![img-11.jpeg](img-11.jpeg)

Figure 12: Averaging over multiple Bayesian networks

# 3.2 Plates: representing learning with graphical models 

In their current form, graphical models do not allow the convenient representation of a learning problem. There are four important points to be observed regarding the use of graphical models to improve their suitability for learning. Consider again the unsupervised learning system described in the introduction of Section 3.

- The unknown model parameters $\phi, \theta_{1}, \theta_{2}$, and $\theta_{3}$ are included in the graphical model to explicitly represent all variables in the problem, even model parameters. By including these in the probabilistic model, an explicitly Bayesian model is constructed. Every variable in a graphical model, even unknown model parameters, has a defined prior probability.
- The learning sample is a repeated set of measured variables so the basic model of Figure 9 appears duplicated as many times as there are cases in the sample, as shown in Figure 10. Clearly, this awkward repetition will occur whenever homogeneous data is being modeled (typical in learning). Techniques for handling this repetition form a major part of this paper.
- Neither graph in Figures 9 and 10 represents the goal of learning. For learning to be goal directed, additional information needs to be included in the graph: how is learned knowledge evaluated or how can subsequent performance be measured? This is the role of decision theory and it is modeled in graphical form using influence diagrams (Shachter, 1986). This is not discussed here, but is covered in (Buntine, 1994).
- Finally, it must be possible to take a graphical representation of a learning problem and the goal of learning and construct an algorithm to solve the problem. Subsequent sections discuss techniques for this.

Consider a simplified version of the same unsupervised problem. In fact, the simplest possible learning problem containing uncertainty goes as follows: there is a biased coin with

![img-12.jpeg](img-12.jpeg)

Figure 13: Tossing a coin: model without and with a plate
an unknown bias for heads $\theta$. That is, the long-run frequency of getting heads for this coin on a fair toss is $\theta$. The coin is tossed $N$ times and each time the binary variable heads $_{i}$ is recorded. The graphical model for this is in Figure 13(a). The heads ${ }_{i}$ nodes are shaded because their values are given, but the $\theta$ node is not. The $\theta$ node has a $\operatorname{Beta}(1.5,1.5)$ prior. This assumes $\theta$ is distributed according to the Beta distribution with parameters $\alpha_{1}=1.5$ and $\alpha_{2}=1.5$

$$
p\left(\theta \mid \alpha_{1}, \alpha_{2}\right)=\frac{\theta^{\alpha_{1}-1}(1-\theta)^{\alpha_{2}-1}}{\operatorname{Beta}\left(\alpha_{1}, \alpha_{2}\right)}
$$

where $\operatorname{Beta(,)}$ is the standard beta function given in many mathematical tables. This prior is plotted in Figure 14. A $\operatorname{Beta}(1.0,1.0)$ prior, for instance, is uniform in $\theta$, whereas $\operatorname{Beta}(1.5,1.5)$ slightly favors values closer to 0.5 -a fairer coin. Figure 13(b) is an equivalent
![img-13.jpeg](img-13.jpeg)

Figure 14: The $\operatorname{Beta}(1.5,1.5)$ prior $(\alpha=1.5)$ and other priors on $\theta$
graphical model using the notation of plates. The repeated group, in this case the heads ${ }_{i}$ nodes, is replaced by a single node with a box around it. The box is referred to as a plate. and implies that

- the enclosed subgraph is duplicated $N$ times (into a "stack" of plates),
- the enclosed variables are indexed, and

- any exterior-interior links are duplicated.

In Section 2.1 it was shown that any Bayesian network has a corresponding form for the joint probability of variables in the Bayesian network. The same applies to plates. The plate indicates that a product ( $\Pi$ ) will appear in the corresponding form. The probability equation for Figure 10, read directly from the graph, is:

$$
\begin{aligned}
& p\left(\phi, \theta_{1}, \theta_{2}, \theta_{3}, \text { class }_{1}, \text { var }_{1,1}, \text { var }_{2,1}, \text { var }_{3,1}, \ldots, \text { class }_{N}, \text { var }_{1, N}, \text { var }_{2, N}, \text { var }_{3, N}\right)= \\
& \quad p(\phi) p\left(\theta_{1}\right) p\left(\theta_{2}\right) p\left(\theta_{3}\right) p\left(\operatorname{class}_{1}|\phi\right) p\left(\operatorname{var}_{1,1}\left|\operatorname{class}_{1}, \theta_{1}\right) p\left(\operatorname{var}_{2,1}\left|\operatorname{class}_{1}, \theta_{2}\right) p\left(\operatorname{var}_{3,1}\left|\operatorname{class}_{1}, \theta_{3}\right)\right.\right. \\
& \left.\quad \ldots p\left(\operatorname{class}_{N}\right| \phi\right) p\left(\operatorname{var}_{1, N}\left|\operatorname{class}_{N}, \theta_{1}\right) p\left(\operatorname{var}_{2, N}\left|\operatorname{class}_{N}, \theta_{2}\right) p\left(\operatorname{var}_{3, N}\left|\operatorname{class}_{N}, \theta_{3}\right)\right.\right.
\end{aligned}
$$

The corresponding equation using product notation is:

$$
\begin{gathered}
p\left(\phi, \theta_{1}, \theta_{2}, \theta_{3}, \text { class }_{i}, \text { var }_{1, i}, \text { var }_{2, i}, \text { var }_{3, i}: i=1, \ldots, N\right)=p(\phi) p\left(\theta_{1}\right) p\left(\theta_{2}\right) p\left(\theta_{3}\right) \\
\prod_{i=1}^{N} p\left(\operatorname{class}_{i}|\phi\right) p\left(\operatorname{var}_{1, i}\left|\operatorname{class}_{i}, \theta_{1}\right) p\left(\operatorname{var}_{2, i}\left|\operatorname{class}_{i}, \theta_{2}\right) p\left(\operatorname{var}_{3, i}\left|\operatorname{class}_{i}, \theta_{3}\right)\right.\right.
\end{gathered}
$$

These two equations are equivalent. However, the differences in their written form corresponds to the differences in their graphical form. Each plate is converted into a product: the joint probability ignoring the plates is written, a product ( $\Pi$ ) is added for each plate to index the variables inside it. If there are two disjoint plates then there are two disjoint products. Overlapping plates yield overlapping products. The corresponding transformation for the unsupervised learning problem of Figure 10 is given in Figure 15. Notice, the
![img-14.jpeg](img-14.jpeg)

Figure 15: Simple unsupervised learning, with a plate
hidden class variable is not shaded so it is not given. The corresponding transformation for the supervised learning problem of Figure 10, where the classes are given, and thus corresponds to the idiot's Bayes classifier, is identical to Figure 15 except that the class variable is shaded because the classes are now part of the training sample.

Many learning problems can be similarly modeled with plates. Write down the graphical model for the full learning problem with only a single case provided. Put a box around the data part of the model, pull out the model parameters (for instance, the weights of the network or the classification parameters), and ensure they are unshaded because they are unknown. Now add the data set size $(N)$ to the bottom left corner.

The notion of a plate is formalized below. This formalization is included for use in subsequent proofs.

Definition 3.1 A chain graph $G$ with plates on variable set $X$ consists of a chain graph $G^{\prime}$ on variables $X$ with additional boxes called plates placed around groups of variables. Only directed arcs can cross plate boundaries, and plates can be overlapping. Each plate $P$ has an integer $N_{P}$ in the bottom left corner indicating its cardinality. Each plate indexes the variables inside it with values $i=1, \ldots, N_{P}$. Each variable $V \in X$ occurs in some subset of the plates. Let indval $(V)$ denote the set of values for indices corresponding to these plates. That is, indval $(V)$ is the cross product of index sets $\left\{1, \ldots, N_{P}\right\}$ for plates $P$ containing $V$.

A graph with plates can be expanded to remove the plates. Figure 10 is the expanded form of Figure 15. Given a chain graph with plates $G$ on variables $X$, construct the expanded graph as follows:

- For each variable $V \in X$, add a node for $V_{i}$ for each $i \in \operatorname{indvar}(V)$.
- For each undirected arc between variables $U$ and $V$, add an undirected arc between $U_{i}$ and $V_{i}$ for $i \in \operatorname{indvar}(V)=\operatorname{indvar}(U)$.
- For each directed arc between variables $U$ and $V$, add a directed arc between $U_{i}$ and $V_{j}$ for $i \in \operatorname{indvar}(V)$ and $j \in \operatorname{indvar}(V)$ where $i$ and $j$ have identical values for index components from the same plate.

The parents for indexed variables in a graph with plates are the parents in the expanded graph.

$$
\operatorname{parents}(U)=\bigcup_{i \in \text { indval }(U)} \operatorname{parents}\left(U_{i}\right)
$$

A graph with plates is interpreted using the following product form. If the product form for the chain graph $G^{\prime}$ without plates with chain components $T$ is

$$
p\left(X \mid M\left(G^{\prime}\right)\right)=\prod_{\tau \in T} p(\tau \mid \operatorname{parents}(\tau), M)
$$

then the product form for the chain graph $G$ with plates has a product for each plate:

$$
p(X \mid M(G))=\prod_{\tau \in T} \prod_{i \in \text { indval }(\tau)} p\left(\tau_{i} \mid \text { parents }\left(\tau_{i}\right), M\right)
$$

This is given by the expanded version of the graph. Testing for independence on chain graphs with plates involves expanding the plates. In some cases, this can be simplified.

# 4. Exact operations on graphical models 

This section introduces basic inference methods on graphs without plates and exact inference methods on graphs with plates. While there are no common machine learning algorithms explained in this section, the operations explained are the mathematical basis of most fast learning algorithms. Therefore, the importance of these basic operations should not be underestimated. Their use within more well-known learning algorithms is explained in later sections.

Once a graphical model is developed to represent a problem, the graph can be manipulated using various exact or approximate transformations to simplify the problem. This section reviews basic exact transformations available: arc reversal, node removal, and exact removal of plates by recursive arc reversal. The summary of operations emphasizes the computational aspects. A graphical model has an associated set of definitions or tables for the basic functions and conditional probabilities implied by the graph, the operations given below effect both the graphical structure and these underlying mathematical specifications. In both cases, the process of making these transformations should be constructive so that a graphical specification for a learning problem can be converted into an algorithm.

There are several generic approaches for performing inference on directed and undirected networks without plates. These approaches are mentioned, but will not be covered in detail. The first approach is exact and corresponds to removing independent or irrelevant information from the graph, then attempting to optimize an exact probabilistic computation by finding a reordering of the variables. The second approach to performing inference is approximate and corresponds to approximate algorithms such as Gibbs sampling, and other Markov chain Monte Carlo methods (Hrycej, 1990; Hertz et al., 1991; Neal, 1993). In some cases, the complexity of the first approach is inherently exponential in the number of variables, so the second can be more efficient. The two approaches can be combined in some cases after appropriate reformulation of the problem (Dagum \& Horvitz, 1992).

# 4.1 Exact inference without plates 

The exact inference approach has been highly refined for the case where all variables are discrete. It is not surprising that available algorithms have strong similarities (Shachter, Andersen, \& Szolovits, 1994) since the major choice points involve the ordering of the summation and whether this ordering is selected dynamically or statically. Other special classes of inference algorithms include the cases where the model is a multivariate Gaussian (Shachter \& Kenley, 1989; Whittaker, 1990), or corresponds to some specific diagnostic structure, such as two-level believe networks with a level of symptoms connected to a level of diseases (Henrion, 1990). This subsection reviews some simple, exact transformations on graphical models without plates. Two representative methods are covered but are by no means optimal: arc reversal and arc removal. They are important, however, because they are the building blocks on which methods for graphs with plates are based. Many more sophisticated variations and combinations of these algorithms exist in the literature, including the handling of deterministic nodes (Shachter, 1990) and chain graphs and undirected graphs (Frydenberg, 1990).

### 4.1.1 Arc reversal

Two basic steps for inference are to marginalize nuisance parameters or to condition on new evidence. This may require evaluating probability variables in a different order. The arc reversal operator interchanges the order of two nodes connected by a directed arc (Shachter, 1986). This operator corresponds to Bayes theorem and is used, for instance, to automate the derivation of Equation (9) from Equation (8). The operator applies to directed acyclic graphs and to chain graphs where $a$ and $b$ are adjacent chain components.

![img-15.jpeg](img-15.jpeg)

Figure 16: Arc reversal: reversing nodes $a$ and $b$

Consider a fragment of a graphical model as given in the left of Figure 16. The equation for this fragment is:

$$
p(a, b \mid A)=p(b \mid \text { parents }(b)) p(a \mid b, \text { parents }(a))
$$

Suppose nodes $a$ and $b$ need to be reordered. Assume that between $a$ and $b$ there is no directed path of length greater than one. If there was, then reversing the arc between $a$ and $b$ would create a cycle, which is forbidden in a Bayesian network and chain graph. The formula for the variable reordering can be found by applying Bayes theorem to the above equation.

$$
\begin{aligned}
p(a \mid A) & =\sum_{b} p(b \mid \text { parents }(b)) p(a \mid \text { parents }(a)) \\
p(b \mid a, A) & =\frac{p(b \mid \text { parents }(b)) p(a \mid \text { parents }(a))}{\sum_{b} p(b \mid \text { parents }(b)) p(a \mid \text { parents }(a))}
\end{aligned}
$$

The corresponding graph is given in the right of Figure 16. Notice that the effect on the graph is that nodes for $a$ and $b$ now share their parents. This is an important point. If all of $a$ 's parents were also $b$ 's, and vice versa, excepting $b($ parents $(a)=$ parents $(b) \cup\{b\}$ ), then the graph would be unchanged except for the direction of the arc between $a$ and $b$. Regardless, the probability tables or formula associated with the graph also need to be updated. If the variables are discrete and full conditional probability tables are maintained, then this operation requires instantiating the set $\{a, b\} \cup$ parents $(a) \cup$ parents $(b)$ in all ways, which is exponential in the number of variables.

# 4.1.2 Arc and node removal 

Some variables in a graph are part of the model, but are not important for the goal of the data analysis. These are called nuisance parameters. An unshaded node $y$ without children (no outward going arcs) that is neither an action node nor a utility node can always be removed from a Bayesian network. This corresponds to leaving out the term $p(y \mid$ parents $(y))$ in the product of Equation 2. Given

$$
p(a, b, y)=p(a) p(b \mid a) p(y \mid a, b)
$$

then $y$ can be marginalized out trivially to yield:

$$
p(a, b)=p(a) p(b \mid a)
$$

More generally this applies to chain graphs-a chain component whose nodes are all unshaded and have no children can be removed. If $y$ is a node without children, then remove the node with $y$ from the graph and the arcs to it; ignore the factor $p(y \mid$ parents $(y))$ in the full joint form. Consider that the $i$-th case in Figure 10 (nodes class $_{i}$, var $_{1, i}$, var $_{2, i}$, var $_{3, i}$ ) can be removed from the model without affecting the rest of the graph.

# 4.2 Removal of plates by exact methods 

Consider the simple coins problem of Figure 13 again. The graph represents the joint probability for $p\left(\theta\right.$, heads $\left._{1}, \ldots\right.$, heads $\left._{N}\right)$. The main question of interest here is the conditional probability of $\theta$ given the data heads $_{1}, \ldots$, heads $_{N}$. This could be obtained through repeated arc reversals between $\theta$ and heads $_{1}$, then between $\theta$ and heads $_{2}$, and so on, until all the data appears before $\theta$ in the directed graph. Doing this repeated series of applications of Bayes theorem yields a fully connected graph with $(N+1) N / 2$ arcs. The corresponding formula for the posterior simplified with Lemma 2.1 is also simple:

$$
p\left(\theta \mid \text { heads }_{1}, \ldots, \text { heads }_{N}, \alpha_{1}=1.5, \alpha_{2}=1.5\right)=\frac{\theta^{\alpha_{1}-1+p}(1-\theta)^{\alpha_{2}-1+n}}{\operatorname{Beta}\left(\alpha_{1}+p, \alpha_{2}+n\right)}
$$

where $p$ is the number of heads in the sequence and $n=N-p$ is the number of tails. This is a worthwhile introductory exercise in Bayesian decision theory (Howard, 1970) that should be familiar to most students of statistics. Compare this with Equation (11). There are several important points to notice about this result:

- Effectively, this does a parameter update, $\alpha_{1}^{\prime}=\alpha_{1}+p$ and $\alpha_{2}^{\prime}=\alpha_{2}+n$, requiring no search or numerical optimization. The whole sequence of tosses, irrespective of its length and the ordering of the heads and tails, can be summed up with two numbers. These summary statistics are called sufficient statistics because, assuming the model used is correct, they are sufficient to explain all that is important about $\theta$ in the data,.
- The corresponding graph can be simplified as shown in Figure 17. The plate is efficiently removed and replaced by the sufficient statistics (two numbers) irrespective of the size of the sample.

Figure 17: Removing the plate in the coin problem

- The posterior distribution has a simple form. Furthermore, all the moments of $\theta$, $\log \theta$, and $\log (1-\theta)$ for the distribution can be computed as simple functions of the normalizing constant, $\operatorname{Beta}\left(\alpha_{1}^{\prime}, \alpha_{2}^{\prime}\right)$. For instance:

$$
\begin{aligned}
\mathcal{E}_{\theta \mid \text { heads }_{1}, \ldots, \text { heads }_{N}, \alpha_{1}, \alpha_{2}}(\log \theta) & =\frac{\partial \log \operatorname{Beta}\left(\alpha_{1}^{\prime}, \alpha_{2}^{\prime}\right)}{\partial \alpha_{1}} \\
\mathcal{E}_{\theta \mid \text { heads }_{1}, \ldots, \text { heads }_{N}, \alpha_{1}, \alpha_{2}}(\theta) & =\frac{\operatorname{Beta}\left(\alpha_{1}^{\prime}+1, \alpha_{2}^{\prime}\right)}{\operatorname{Beta}\left(\alpha_{1}^{\prime}, \alpha_{2}^{\prime}\right)}
\end{aligned}
$$

$$
\mathcal{E}_{\theta \mid h e a d s_{1}, \ldots, \text { heads }_{N}, \alpha_{1}, \alpha_{2}}\left((\theta-\bar{\theta})^{2}\right)=\frac{\operatorname{Beta}\left(\alpha_{1}^{\prime}+2, \alpha_{2}^{\prime}\right)}{\operatorname{Beta}\left(\alpha_{1}^{\prime}, \alpha_{2}^{\prime}\right)}-\frac{\operatorname{Beta}^{2}\left(\alpha_{1}^{\prime}+1, \alpha_{2}^{\prime}\right)}{\operatorname{Beta}^{2}\left(\alpha_{1}^{\prime}, \alpha_{2}^{\prime}\right)}
$$

This result might seem somewhat obscure, but it is a general property holding for a large class of distributions that allows some averages to be calculated by symbolic manipulation of the normalizing constant.

# 4.3 The exponential family 

This result generalizes to a much larger class of distributions referred to as the exponential family (Casella \& Berger, 1990; DeGroot, 1970). This includes standard undergraduate distributions such as Gaussians, Chi squared, and Gamma, and many more complex distributions constructed from simple components including class probability trees over discrete input domains (Buntine, 1991b), simple discrete and Gaussian versions of a Bayesian network (Whittaker, 1990), and linear regression with a Gaussian error. Thus, these are a broad and not insignificant class of distributions that are given in the definition below. Their general form has a linear combination of parameters and data in the exponential.

Definition 4.1 A space $X$ is independent of the parameter $\theta$ if the space remains the same when just $\theta$ is changed. If the domains of $x, y$ are independent of $\theta$, then the conditional distribution for $x$ given $y, p(x \mid y, \theta, M)$, is in the exponential family when

$$
p(x \mid y, \theta, M)=\frac{h(x, y)}{Z(\theta)} \exp \left(\sum_{i=1}^{k} w_{i}(\theta) t_{i}(x, y)\right)
$$

for some functions $w_{i}, t_{i}, h$ and $Z$ and some integer $k$, for $h(x, y)>0$. The normalization constant $Z(\theta)$ is known as the partition function.

Notice the functional form of Equation (14) is similar to the functional form for an undirected graph of Equation (4), as holds in many cases for a Markov random field. For the previous coin tossing example, both the coin tossing distribution (a binomial on heads ${ }_{i}$ ) and the posterior distribution on the model parameters $(\theta)$ are in the exponential family. To see this, notice the following rewrites of the original probabilities. These make the components $w_{i}, t_{i}$ and $Z$ explicit.

$$
\begin{aligned}
& p\left(\text { heads } \mid \theta\right)=\exp \left(1_{\text {heads=true }} \log \theta+1_{\text {heads=false }} \log (1-\theta)\right) \\
& p\left(\theta \mid \text { heads }_{1}, \ldots, \text { heads }_{N}, \alpha_{1}, \alpha_{2}\right)= \\
& \frac{1}{\operatorname{Beta}\left(\alpha_{1}+p, \alpha_{2}+n\right)} \exp \left(\left(\alpha_{1}+p-1\right) \log \theta+\left(\alpha_{2}+n-1\right) \log (1-\theta)\right)
\end{aligned}
$$

Table 2 in Appendix B gives a selection of distributions, and their functional form. Further details can be found in most textbooks on probability distributions (DeGroot, 1970; Bernardo \& Smith, 1994).

The following is a simple graphical reinterpretation of the Pitman-Koopman Theorem from statistics (Jeffreys, 1961; DeGroot, 1970). In Figure 18(a), $T\left(x_{*}, y_{*}\right)$ is a statistic of fixed dimension independent of the sample size $N$ (corresponding to $n, p$ in the coin tossing example). The theorem says that the sample in Figure 18(a) can be summarized in statistics, as shown in Figure 18(b), if and only if the probability distribution for $x \mid y, \theta$ is in the exponential family. In this case, $T\left(x_{*}, y_{*}\right)$ is a sufficient statistic.

![img-16.jpeg](img-16.jpeg)

Figure 18: The generalized graph for plate removal

Theorem 4.1 (Recursive arc-reversal). Consider the model $M$ represented by the graphical model for a sample of size $N$ given in Figure 18(a). Have $x$ in the domain $X$ and $y$ in the domain $Y$, both domains are independent of $\theta$, and both domains have components that are real valued or finite discrete. Let the conditional distribution for $x$ given $y, \theta$ be $f(x \mid y, \theta)$, which is positive for all $x \in X$. If first derivatives exist with respect to all real valued components of $x$ and $y$, the plate removal operation applies for all samples $x_{*}=x_{1}, \ldots, x_{N}$, $y_{*}=y_{1}, \ldots, y_{N}$, and $\theta$, as given in Figure 18(b), for some sufficient statistics $T\left(x_{*}, y_{*}\right)$ of dimension independent of $N$ if and only if the conditional distribution for $x$ given $y, \theta$ is in the exponential family, given by Equation (14). In this case, $T\left(x_{*}, y_{*}\right)$ is an invertible function of the $k$ averages:

$$
\frac{1}{N} \sum_{j=1}^{N} t_{i}\left(x_{j}\right): \quad i=1, \ldots, k
$$

In some cases, this extends to domains $X$ and $Y$ dependent on $\theta$ (Jeffreys, 1961).
Sufficient statistics for a distribution from the exponential family are easily read from the functional form by taking a logarithm. For instance, for the multivariate Gaussian, the sufficient statistics are $x_{i}$ for $i=1, \ldots, d$ and $x_{i} x_{j}$ for $0 \leq i \leq j \leq d$, and the normalizing constant $Z(\mu, \Sigma)$ is given by:

$$
Z(\mu, \Sigma)=\frac{(2 \pi)^{d / 2}}{\operatorname{det}^{1 / 2} \Sigma} \exp \left(\frac{1}{2} \mu^{\dagger} \Sigma \mu\right)
$$

As for coin tossing, it generally holds that if a sampling distribution (a binomial on heads ${ }_{i}$ ) is in the exponential family, then the posterior distribution for the model parameters $(\theta)$ can also be cast as exponential family. This is only useful when the normalizing constant (this is $\operatorname{Beta}\left(\alpha_{1}+p, \alpha_{2}+n\right)$ in the coin tossing example) and its derivatives are readily computed.

Lemma 4.1 (The conjugacy property). In the context in Theorem 4.1, assume the distribution for $x$ given $y, \theta$ can be represented by the exponential family. Factor the normalizing constant $Z(\theta)$ into two components, $Z(\theta)=Z_{1}(\theta) Z_{2}$, where the second is the constant part independent of $\theta$. Assume the prior on $\theta$ takes the form:

$$
p(\theta \mid \tau, M)=\frac{f(\theta)}{Z_{\theta}(\tau)} \exp \left(\tau_{k+1}\left(\log 1 / Z_{1}(\theta)\right)+\sum_{i=1}^{k} \tau_{i} w_{i}(\theta)\right)
$$

for some $k+1$ dimensional parameter $\tau$, where $Z_{\theta}(\tau)$ is the appropriate normalizing constant and $f(\theta)$ is any function. Then the posterior distribution for $\theta, p\left(\theta \mid \tau, x_{1}, \ldots, x_{N}, M\right)$, is also represented by Equation (15) with the parameters

$$
\begin{aligned}
\tau_{k+1}^{\prime} & =\tau_{k+1}+N \\
\tau_{i}^{\prime} & =\tau_{i}+\sum_{j=1}^{N} t_{i}\left(x_{j}, y_{j}\right) \quad i=1, \ldots, k
\end{aligned}
$$

When the function $f(\theta)$ is trivial, for instance uniformly equal to 1 , then the distribution in Equation (15) is referred to as the conjugate distribution, which means it has a mathematical form mirroring that of the sample likelihood. The prior parameters $\tau$, by looking at the update equations in the lemma, can be thought of as corresponding to the sufficient statistics from some "prior sample" and given by $\tau_{k+1}$.

This property is useful for analytic and computational purposes. Once the posterior distribution is found, and assuming it is one of the standard distributions, the property can easily be established. Table 3 in Appendix B gives some standard conjugate prior distributions for those in Table 2, and Table 4 gives their matching posteriors. More extensive summaries of this are given by DeGroot (1970) and Bernardo and Smith (1994). The parameters for these priors can be set using standard reference priors (Box \& Tiao, 1973; Bernardo \& Smith, 1994) or elicited from a domain expert.

There are several other important consequences of the Pitman-Koopman Theorem or recursive arc reversal that should not go unnoticed.

Comment 4.1 If $x, y$ are discrete and finite valued, then the distribution $p(x \mid y, \theta)$ can be represented as a member of the exponential family. This holds because a positive finite discrete distribution can always be represented as an extended case statement in the form

$$
p(x \mid y, \theta)=\exp \left(\sum_{i=1, k} 1_{t_{i}(x, y)} f_{i}(\theta)\right)
$$

where the boolean functions $t_{i}(x, y)$ are a set of mutually exclusive and exhaustive conditions. The indicator function $1_{A}$ has the value 1 if the boolean $A$ is true and 0 otherwise. The main importance of the exponential family is in continuous or integer domains. Of course, since a large class of functions $\log p(x \mid y, \theta)$ can always be approximated arbitrarily well by a polynomial in $x, y$ and $\theta$ with sufficiently many terms, the exponential family covers a broad class of distributions.

The application of the exponential family to learning is perhaps the earliest published result on computational learning theory. The following two interpretations of the recursive arc reversal theorem are relevant mainly for distributions involving continuous variables.

Comment 4.2 An incremental learning algorithm with finite memory must compress the information it has seen so far in the training sample into a smaller set of statistics. This can only be done without sacrificing information in the sample, in a context where all probabilities are positive, if the hypothesis or search space of learning is a distribution from the exponential family.

Comment 4.3 The computational requirements for learning an exponential family distribution are guaranteed to be linear in the sample size: first compute the sufficient statistics and then learning proceeds independently of the sample size. This could be exponential in the dimension of the feature space, however.

Furthermore, in the case where the functions $w_{i}$ are full rank in $\theta$ (dimension of $\theta$ is $k$, same as $w$, and the Jacobian of $w$ with respect to $\theta$ is invertible, $\operatorname{det}\left(\frac{\mathrm{d} \omega(\theta)}{\mathrm{d} \theta}\right) \neq 0$ ), various moments of the distribution can easily be found. For this situation, the function $w^{-1}$, when it exists, is called the link function (McCullagh \& Nelder, 1989).

Lemma 4.2 Consider the notation of Definition 4.1. If the link function $w^{-1}$ for an exponential family distribution exists, then moments of functions of $t_{i}(x, y)$ and $\exp \left(t_{i}(x, y)\right)$ can be expressed in terms of derivatives and direct applications of the functions $Z, t_{i}, w_{i}$, and $w^{-1}$. If the normalizing constant $Z$ and the link function are in closed form, then so will the moments.

Techniques for doing these symbolic calculations are given in Appendix B. Exponential family distributions then fall into two groups. There are those where the normalizing constant and link function are known, such as the Gaussian. One can efficiently compute their moments and determine the functional form of their conjugate distributions up to the normalizing constant. For others this is not the case. For others, such as a Markov random field used in image processing, moments can generally only be computed by an approximation process like Gibbs sampling given in Section 7.1.

# 4.4 Linear regression: an example 

As an example, consider the problem of linear regression with Gaussian error described in Figure 19. This is an instance of a generalized linear model and has a linear construction
![img-17.jpeg](img-17.jpeg)

Figure 19: Linear regression with Gaussian error

$$
m=\sum_{j=1}^{M} \theta_{j} \text { basis }_{j}\left(x_{1}, \ldots, x_{n}\right)
$$

at its core. The $M$ basis functions are known deterministic functions of the input variables $x_{1}, \ldots, x_{n}$. These would typically be nonlinear orthogonal functions such as Legendre polynomials. These combine linearly with the parameters $\theta$ to produce the mean $m$ for the Gaussian.

The corresponding learning problem represented as plates is expressed in Figure 20. The
![img-18.jpeg](img-18.jpeg)

Figure 20: The linear regression problem
joint probability for this model is as follows:

$$
p(\sigma) p(\theta \mid \sigma) \frac{1}{(\sqrt{2 \pi} \sigma)^{N}} e^{-\frac{1}{2 \sigma^{2}} \sum_{i=1}^{N}\left(y_{i}-\sum_{j=1}^{M} \theta_{j} \operatorname{basis}_{j}\left(x_{. . i}\right)\right)^{2}}
$$

where $x_{. . i}$ denotes the vector of values for the $i$-th datum, $x_{1, i}, \ldots, x_{n, i}$. Linear regression with Gaussian error falls in the exponential family because a Gaussian is in the exponential family and the mean of the simple Gaussian is a linear function of the regression parameters (see Lemma 5.1).

For this case, the correspondence to the exponential family is drawn as follows. The individual data likelihoods, $p\left(y \mid x_{1}, \ldots, x_{n}, \theta, \sigma\right)$, need only be considered. Expand the probability to show it is a linear sum of data terms and parameter terms.

$$
\begin{aligned}
p & \left(y \mid x_{1}, \ldots, x_{n}, \theta, \sigma\right) \\
& =\frac{1}{\sqrt{2 \pi} \sigma} \exp \left(-\frac{1}{2 \sigma^{2}}\left(y-\sum_{j=1}^{M} \text { basis }_{j}\left(x_{.}\right) \theta_{j}\right)^{2}\right) \\
& =\frac{1}{\sqrt{2 \pi} \sigma} \exp \left(-\frac{1}{2 \sigma^{2}} y^{2}-\sum_{j, k=1}^{M} \text { basis }_{j}\left(x_{.}\right) \text { basis }_{k}\left(x_{.}\right) \frac{\theta_{j} \theta_{k}}{2 \sigma^{2}}+\sum_{j=1}^{M} \text { basis }_{j}\left(x_{.}\right) y \frac{\theta_{j}}{2 \sigma^{2}}\right)
\end{aligned}
$$

The data likelihood in this last line can be seen to be in the same form as the general exponential family where the sufficient statistics are the various data terms in the exponential. Also, the link function does not exist because there are $M$ parameters and $M(M+1) / 2$ sufficient statistics.

![img-19.jpeg](img-19.jpeg)

Figure 21: The linear regression problem with the plate removed

The model of Figure 20 can therefore be simplified to the graph in Figure 21, where $q$ and $S$ are the usual sample means and covariances obtained from the so-called normal equations of linear regression. $S$ is a matrix of dimension $M$ (the number of basis functions) and $q$ is a vector of dimension $M$.

$$
\begin{aligned}
S_{j, k} & =\frac{1}{N} \sum_{i=1}^{N} \operatorname{basis}_{j}\left(x_{., i}\right) \text { basis }_{k}\left(x_{., i}\right) \\
q_{j} & =\frac{1}{N} \sum_{i=1}^{N} \text { basis }_{j}\left(x_{., i}\right) y_{i} \\
y s q & =\frac{1}{N} \sum_{i=1}^{N} y_{i}^{2}
\end{aligned}
$$

These three sufficient statistics can be read directly from the data likelihood above.
Consider the formula:

$$
\int_{y} p\left(y \mid x_{1}, \ldots, x_{n}, \theta, \sigma\right) \mathrm{d} y
$$

Differentiating with respect to $\theta_{i}$ shows that the expected value of $y$ given $x_{1}, \ldots, x_{n}$ and $\theta, \sigma$ is the mean (as expected):

$$
\mathcal{E}_{y \mid x_{1}, \ldots, x_{n}, \theta, \sigma}(y)=m=\sum_{j=1}^{M} \text { basis }_{j}\left(x_{.}\right) \theta_{j}
$$

Differentiating with respect to $\sigma$ shows that the expected error from the mean is $\sigma^{2}$ (again expected):

$$
\mathcal{E}_{y \mid x_{1}, \ldots, x_{n}, \theta, \sigma}\left((y-m)^{2}\right)=\sigma^{2}
$$

Higher-order derivatives give formula for higher-order moments such as skewness and kurtosis (Casella \& Berger, 1990), which are functions of the second, third and fourth central moments. While these are well known for the Gaussian, the interesting point is that these formula are constructed by differentiating the component functions in Equation (14) without recourse to integration. Finally, the conjugate distribution for the parameters $\theta$ in this linear regression problem is the multivariate Gaussian distribution when $\sigma$ is known, and for $\sigma^{2}$ is the inverted Gamma.

# 5. Recognizing and using the exponential family 

How can recursive arc reversal be applied automatically to a graphical model? First, when a graphical model or some subset of a graphical model falls in the exponential family needs to be identified. If each conditional distribution in a Bayesian network or chain component in a chain graph is exponential family, then the full joint is exponential family. The following lemma gives this with some additional conditions for deterministic nodes. This applies to Bayesian networks using Comment 2.2.

Lemma 5.1 A chain graph has a single plate. Let the non-deterministic variables inside the plate be $X$, and the deterministic variables be $Y$. Let the variables outside the plate be $\theta$. If:

1. All arcs crossing a plate boundary are directed into the plate.
2. For all chain components $\tau$, the conditional distribution $p(\tau \mid$ parents $(\tau))$ is from the exponential family with data variables from $(X, Y)$ and model parameters from $\theta$; furthermore $\log p(\tau \mid$ parents $(\tau), \theta)$ is a polynomial function of variables in $Y$.
3. Each variable $y \in Y$ can be expressed as a deterministic function of the form

$$
y=\sum_{i=1}^{l} u_{i}(X) v_{i}(\theta)
$$

for some functions $u_{i}, v_{i}$.
Then the conditional distribution $p(X, Y \mid \theta)$ is from the exponential family.
Second, how can these results be used when the model does not fall in the exponential family? There are two categories of techniques available in this context. In both cases, the algorithms concerned can be constructed from the graphical specifications. The two new classes together with the recursive arc reversal case are given in Figure 22. In each case, (I) denotes the graphical configuration and (II) denotes the operations and simplifications performed by the algorithm. When the various normalization constants are known in closed form and appropriate moments and Bayes factors can be computed quickly, all three algorithm schemas have reasonable computational properties.

The first category is where a useful subset of the model does fall into the exponential family. This is represented by the partial exponential family in Figure 22. The part of the problem that is exponential family is simplified using the recursive arc reversal of Theorem 4.1, and the remaining part of the problem is typically handled approximately. Decision trees and Bayesian networks over multinomial or Gaussian variables also fall into this category. This happens because when the structure of the tree or Bayesian network is given the remaining problem is composed of a product of multinomials or Gaussians. This is the basis of various Bayesian algorithms developed for these problems (Buntine, 1991b; Madigan \& Raftery, 1994; Buntine, 1991c; Spiegelhalter, Dawid, Lauritzen, \& Cowell, 1993; Heckerman, Geiger, \& Chickering, 1994). Strictly speaking, decision trees and Bayesian networks over multinomial or Gaussian variables are in the exponential family (see Comment 4.1). However, it is more computationally convenient to treat them this way. This category is discussed more in Section 8.

![img-20.jpeg](img-20.jpeg)

Figure 22: Three categories of algorithms using the exponential family

The second category is where, if some hidden variables are introduced into the data, the problem becomes exponential family if the hidden values are known. This is represented by the mixture model in Figure 22. Mixture models (Titterington, Smith, \& Makov, 1985; Poland, 1994) are used to model unsupervised learning, incomplete data in the classification problems, robust regression, and general density estimation. Mixture models extend the exponential family to a rich class of distributions, so this second category is an important one in practice. General methods for handling these problems correspond to Gibbs sampling (and other Markov chain Monte Carlo methods) discussed in Section 7.2 and its deterministic counterpart the expectation maximization algorithm, discussed in Section 7.4. As shown in Figure 22, these algorithms cycle back and forth between a process that reestimates $c$ given $\theta$ using first-order inference and a process that uses the fast exponential family algorithms to re-estimate $\theta$ given $c$.

# 6. Other operations on graphical models 

The recursive arc reversal theorem of Section 4.2 characterizes when plates can be readily removed and the sample summarized in some statistics. Outside of these cases, more general classes of approximate algorithms exist. Several of these are introduced in Section 7 and more detail is given, for instance, by Tanner (1993). These more general algorithms require a number of basic operations be performed on graphs:

Decomposition: A learning problem can sometimes be decomposed into simpler subproblems with each yielding to separate analysis. One form of decomposition of learning problems is considered in Section 6.2. Another related form that applies to undirected graphs is developed by Dawid and Lauritzen (1993). Other forms of decomposition can be done at the modeling level, where the initial model is constructed in a manner requiring fewer parameters, as is Heckerman's similarity networks (1991).

Exact Bayes factors: Model selection and averaging methods are used to deal with multiple models (Kass \& Raftery, 1993; Buntine, 1991b; Stewart, 1987; Madigan \& Raftery, 1994). These require the computation of Bayes factors for models constructed during search. Exact methods for computing Bayes factors are considered in Section 6.3.

Derivatives: Various approximation and search algorithms require derivatives be calculated, as discussed next.

# 6.1 Derivatives 

An important operation on graphs is the calculation of derivatives of parameters. This is useful after conditioning on the known data to do approximate inference. Numerical optimization using derivatives can be done to search for MAP values of parameters, or to apply the Laplace approximation to estimate moments. This section shows how to compute derivatives using operations local to each node. The computation is therefore easily parallelized, as is popular, for instance, in neural networks.

Suppose a graph is used to compile a function that searches for the MAP values of parameters in the graph conditioned on the known data. In general, this requires use of numerical optimization methods (Gill, Murray, \& Wright, 1981). To use a gradient descent, conjugate gradient or Levenberg-Marquardt approach requires calculation of first derivatives. To use a Newton-Raphson approach requires calculation of second derivatives, as well. While this could be done numerically by difference approximations, more accurate calculations exist. Methods for symbolically differentiating networks of functions, and piecing together the results to produce global derivatives are well understood (Griewank \& Corliss, 1991). For instance, software is available for taking a function defined in Fortran, $\mathrm{C}++$ code, or some other language, to produce a second function that computes the exact derivative. These problems are also well understood for feed-forward networks (Werbos, McAvoy, \& Su, 1992; Buntine \& Weigend, 1994), and graphical models with plates only add some additional complexity. The basic results are reproduced in this section and some simple examples given to highlight special characteristics arising from their use with chain graphs.

Consider the problem of learning a feed-forward network. A simple feed-forward network is given in Figure 23(a). The corresponding learning problem is given in Figure 23(b), representing the feed-forward network as a Bayesian network. Here the sigmoid units of the network are modeled with deterministic nodes, and the network output represents the mean of a bivariate Gaussian with inverse variance matrix $\Sigma$. Because of the nonlinear sigmoid function making the deterministic mapping from inputs $x_{1}, x_{2}, x_{3}$ to the means $m_{1}, m_{2}$, this learning problem has no reasonable component falling in the exponential family. A rough fallback method is to calculate a MAP value for the weight parameters. This would be the method used for the Laplace approximation (Buntine \& Weigend, 1991; MacKay, 1992) covered in (Tanner, 1993; Tierney \& Kadane, 1986). The setting of priors for feed-forward networks is difficult (MacKay, 1993; Nowlan \& Hinton, 1992; Wolpert, 1994), and it will not be considered here other than assuming a prior is used, $p(w)$. The graph implies the

![img-21.jpeg](img-21.jpeg)

Figure 23: Learning a feed-forward network
following posterior probability:

$$
\begin{aligned}
& p\left(\Sigma, w_{1}, \ldots, w_{5} \mid o_{1, i}, o_{2, i}, x_{1, i}, x_{2, i}, x_{3, i}: i=1, \ldots, N\right) \\
& \quad \propto p(\Sigma) p\left(w_{1}, \ldots, w_{5}\right) \prod_{i=1}^{N} \frac{\operatorname{det}^{1 / 2} \Sigma}{2 \pi} \exp \left(\frac{1}{2}\left(o_{i}-m_{i}\right)^{\dagger} \Sigma\left(o_{i}-m_{i}\right)\right) \\
& m_{i}=\operatorname{Sigmoid}\left(w_{i}^{\dagger} h\right) \\
& h_{i}=\operatorname{Sigmoid}\left(w_{i+2}^{\dagger} x\right)
\end{aligned}
$$

The undirected clique on the parameters $w$ indicates the prior has a term $p(w)$. Suppose the posterior is differentiated with respect to the parameters $w_{4}$. The result is well known to the neural network community since this kind of calculation yields the standard backpropagation equations.

Rather than work through this calculation, instead look at the general case. To develop the general formula for differentiating a graphical model, a few more concepts are needed. Deterministic nodes form islands of determinism within the uncertainty represented by the graph. Partial derivatives within each island can be calculated via recursive use of the chain rule, for instance, by forward or backward propagation of derivatives through the equations. For instance, forward propagation for the above network gives:

$$
\frac{\partial m_{1}}{\partial w_{4}}=\sum_{i=1}^{3} \frac{\partial m_{1}}{\partial h_{i}} \frac{\partial h_{i}}{\partial w_{4}}
$$

This is called forward propagation because the derivatives with respect to $w_{4}$ are propagated forward in the network. In contrast, backward propagation would propagate derivatives of $m_{1}$ with respect to different variables backwards. For each island of determinism, the important variables are the output variables, and their derivatives are required. So for the feed-forward network above, partial derivatives of $m_{1}, m_{2}$, and $m_{3}$ with respect to $w_{4}$ are required.

Definition 6.1 The non-deterministic children of a node $x$, denoted ndchildren $(x)$, are the set of non-deterministic variables $y$ such that there exists a directed path from $x$ to $y$ given by $x, y_{1}, \ldots, y_{n}, y$, with all intermediate variables $\left(y_{1}, \ldots, y_{n}\right)$ being deterministic. The nondeterministic parents of a node $x$, denoted ndparents $(x)$, are the set of non-deterministic variables $y$ such that there exists a directed path from $y$ to $x$ given by $y, y_{1}, \ldots, y_{n}, x$, with all intermediate variables $\left(y_{1}, \ldots, y_{n}\right)$ being deterministic. The deterministic children of a node $x$, denoted $\operatorname{detchildren}(x)$, are the set of deterministic variables $y$ that are children of $x$. The deterministic parents of a node $x$, denoted detparents $(x)$, are the set of deterministic variables $y$ that are parents of $x$.

For instance, in the model in Figure 23, the non-deterministic children of $w_{3}$ are $o_{1}$ and $o_{2}$. Deterministic nodes can be removed from a graph by rewriting the equations represented into the remaining variables of the graph. Because some graphical operations do not apply to deterministic nodes, this removal is often done implicitly within a theorem. This goes as follows:

Lemma 6.1 A chain graph $G$ with nodes $X$ has deterministic nodes $Y \subset X$. The chain graph $G^{\prime}$ is created by adding to $G$ a directed arc from every node to its non-deterministic children, and by deleting the deterministic nodes $Y$. The graphs $G$ and $G^{\prime}$ are equivalent probability models on the nodes $X-Y$.

The general formula for differentiating Bayesian networks with plates and deterministic nodes is given below in Lemma 6.2. This is nothing more than the chain rule for differentiation, but it is important to notice the network structure of the computation. When partial derivatives are computed over networks, there are local and global partial derivatives that can be different. Consider the feed-forward network of Figure 23 again. On this figure, place an extra arc from $w_{4}$ to $m_{2}$. Now consider the partial derivative of $m_{2}$ with respect to $w_{4}$. The value of $m_{2}$ is influenced by $w_{4}$ directly, as the new arc shows, and indirectly via $h_{2}$. When computing a partial derivative involving indirect influences, we need to differentiate between the direct and indirect effects. Various notations are used for this (Werbos et al., 1992; Buntine \& Weigend, 1994). Here the notation of a local versus global derivative is used. The local partial derivative is subscripted with an $l, \partial / \partial_{l}$ and represents the partial derivative computed at the node using only the direct influences-the parents. For the example of the partial derivative of $m_{2}$ with respect to $w_{4}$, the various local partial derivatives combine to produce the global partial derivative:

$$
\frac{\partial m_{2}}{\partial w_{4}}=\frac{\partial m_{2}}{\partial_{l} w_{4}}+\frac{\partial m_{2}}{\partial_{l} h_{2}} \frac{\partial h_{2}}{\partial_{l} w_{4}}
$$

This is equivalent to:

$$
\frac{\partial m_{2}}{\partial w_{4}}=\frac{\partial m_{2}}{\partial_{l} w_{4}}+\frac{\partial m_{2}}{\partial_{l} h_{2}} \frac{\partial h_{2}}{\partial_{l} w_{4}}+\frac{\partial m_{2}}{\partial_{l} h_{1}} \frac{\partial h_{1}}{\partial_{l} w_{4}}
$$

since $\frac{\partial h_{1}}{\partial_{l} w_{4}}=0$.
In general, the (global) partial derivative for an index variable $\theta_{i}$ is the sum of the

- local partial derivative at the node containing $\theta_{i}$,

- the partial derivatives for each child of $\theta_{i}$ that is also a non-deterministic child, and
- combinations of (global) partial derivatives for deterministic children found by backward or forward propagation of derivatives.

Lemma 6.2 (Differentiation). A model $M$ is represented by a Bayesian network $G$ with plates and deterministic nodes on variables $X$. Denote the known variables in $X$ by $K$ and the unknown variables by $U=X-K$. Let the conditional probability represented by the graph $G$ be $p(U \mid K, M)$. Let $\theta$ be some unknown variable in the graph, and let $1_{n d(\theta)}$ be 1 if $\theta$ is non-deterministic and 0 otherwise. If $\theta$ occurs inside a plate then let $i$ be some arbitrary valid index ( $i \in \operatorname{indval}(\theta)$ ), otherwise let $i$ be null. Then:

$$
\begin{aligned}
& \frac{\partial \log p(U \mid K, M)}{\partial \theta_{i}}=1_{n d\left(\theta_{i}\right)} \frac{\partial \log p\left(\theta_{i} \mid\right. \text { parents }\left(\theta_{i}\right))}{\partial_{l} \theta_{i}} \\
& +\sum_{x \in \text { ndchildren }\left(\theta_{i}\right) \text { children }\left(\theta_{i}\right)} \frac{\partial \log p(x \mid \text { parents }(x))}{\partial_{l} \theta_{i}} \\
& +\sum_{x \in \text { ndchildren }\left(\theta_{i}\right) y \in \text { detparents }(x), y \neq \theta_{i}} \frac{\partial \log p(x \mid \text { parents }(x))}{\partial_{l} y} \frac{\partial y}{\partial \theta_{i}}
\end{aligned}
$$

Furthermore, if $Y \subset U$ is some subset of the unknown variables, then the partial derivative of the probability of $Y$ given the known variables, $p(Y \mid K, M)$ is an expected value of the above probabilities:

$$
\frac{\partial \log p(Y \mid K, M)}{\partial \theta_{i}}=\mathcal{E}_{U-Y \mid Y, K, M}\left(\frac{\partial \log p(U \mid K, M)}{\partial \theta_{i}}\right)
$$

Equation (17) contains only one global partial derivative which is inside the double sum on the right side. This is the partial derivative $\partial y / \partial \theta_{i}$ and can be computed from its local island of determinism using the chain rule of differentiation, for instance, using forward propagation from $\theta_{i}$ 's deterministic children, or backward propagation from $\theta_{i}$ 's non-deterministic parents.

To apply the Differentiation Lemma on problems like feed-forward networks or unsupervised learning, the lemma needs to be extended to chain graphs. This means differentiating Markov networks as well as Bayesian networks, and handling the expected value in Equation (18). These extensions are explained below after first giving two examples.

As a first example, consider the feed-forward network problem of Figure 23. By treating the two output units in the feed-forward network as a single variable, a Cartesian product $\left(o_{1}, o_{2}\right)$, the above Differentiation Lemma can now be applied directly to the feed-forward network model of Figure 23. This uses the simplification given in Section 2.4 with Comment 2.1. Let $P$ be the joint probability for the feed-forward network model, given in Equation (16). The non-deterministic children of $w_{4}$ are the single chain component consisting of the two variables $o_{1}$ and $o_{2}$. Its parents are the set $\left\{m_{1}, m_{2}\right\}$. Consider the Differentiation Lemma. There are no children of $w_{4}$ that are also non-deterministic, so the middle sum in Equation (17) of the Differentiation Lemma is empty. Then the lemma yields, after expanding out the inner most sum:

$$
\frac{\partial \log P}{\partial w}=\frac{\partial \log p(w)}{\partial_{l} w_{4}}+
$$

$$
\sum_{i=1}^{N}\left(\frac{\partial \log p\left(o_{1, i}, o_{2, i} \mid \Sigma, m_{1}, m_{2}\right)}{\partial_{l} m_{1}} \frac{\partial m_{1}}{\partial_{l} w_{4}}+\frac{\partial \log p\left(o_{1, i}, o_{2, i} \mid \Sigma, m_{1}, m_{2}\right)}{\partial_{l} m_{2}} \frac{\partial m_{2}}{\partial_{l} w_{4}}\right)
$$

where $p\left(o_{1, i}, o_{2, i} \mid \Sigma, m_{1}, m_{2}\right)$ is the two-dimensional Gaussian, and $\frac{\partial m_{i}}{\partial w_{4}}$ is from the global derivative but evaluates to a local derivative.

As a second example, reconsider the simple unsupervised learning problem given in the introduction to Section 3. The likelihood for a single datum given the model parameters is a marginal of the form:

$$
p\left(\operatorname{var}_{1}=1, \operatorname{var}_{2}=0, \operatorname{var}_{3}=1 \mid \phi, \theta\right)=\sum_{c=1}^{10} \phi_{c} \theta_{1, c}\left(1-\theta_{2, c}\right) \theta_{3, c}
$$

Taking the logarithm of the full case probability $p\left(\right.$ class, $\left.v a r_{1}, v a r_{2}, v a r_{3} \mid \phi, \theta\right)$ reveals the vectors of components $w$ and $t$ of the exponential distribution:

$$
\begin{aligned}
& \log p\left(\text { class }, \operatorname{var}_{1}, \operatorname{var}_{2}, \operatorname{var}_{3} \mid \phi, \theta\right) \\
& \quad=\sum_{c=1}^{10} 1_{\text {class }=c} \log \phi_{c}+\sum_{j=1}^{3} \sum_{c=1}^{10}\left(1_{\text {class }=c, v a r_{j}= \text { true }} \log \theta_{j, c}+1_{\text {class }=c, v a r_{j}=f a l s e} \log \left(1-\theta_{j, c}\right)\right)
\end{aligned}
$$

Notice that the normalizing constant $Z(\phi, \theta)$ is 1 in this case. Consider finding the partial derivative $\partial \log p\left(\operatorname{var}_{1}, \operatorname{var}_{2}, \operatorname{var}_{3} \mid \phi, \theta\right) / \partial \theta_{2,5}$. This is done for each case when differentiating the posterior or the likelihood of the unsupervised learning model. Applying Equation (18) to this yields:

$$
\begin{aligned}
& \frac{\partial \log p\left(\operatorname{var}_{1}, \operatorname{var}_{2}, \operatorname{var}_{3} \mid \phi, \theta\right)}{\partial \theta_{2,5}} \\
& =\sum_{d=1}^{10} \frac{\partial \log \theta_{2, d}}{\partial \theta_{2,5}} \mathcal{L}_{\text {class }=\left(\mid v a r_{1}, v a r_{2}, v a r_{3}, \phi, \theta\right.}\left(1_{\text {class }=d, v a r_{2}=\text { true }}\right) \\
& +\frac{\partial \log \left(1-\theta_{2, d}\right)}{\partial \theta_{2,5}} \mathcal{L}_{\text {class }=\left(\mid v a r_{1}, v a r_{2}, v a r_{3}, \phi, \theta\right.}\left(1_{\text {class }=d, v a r_{2}=\text { true }}\right) \\
& =\frac{1}{\theta_{2,5}} 1_{\text {var }_{2}=\text { true }} p\left(\text { class }=5 \mid \text { var }_{1}, \text { var }_{2}, \text { var }_{3}, \phi, \theta\right) \\
& +\frac{1}{1-\theta_{2,5}} 1_{\text {var }_{2}=\text { false }} p\left(\text { class }=5 \mid \text { var }_{1}, \text { var }_{2}, \operatorname{var}_{3}, \phi, \theta\right) .
\end{aligned}
$$

Notice that the derivative is computed by doing first-order inference to find $p($ class $=$ $5 \mid$ var $_{1}$, var $_{2}$, var $_{3}, \phi, \theta)$, as noted by Russell, Binder, and Koller (1994). This property holds in general for exponential family models with missing or unknown variables. Derivatives are calculated by some first-order inference followed by a combination with derivatives of the $w$ functions. Consider the notation for the exponential family introduced previously in Definition 4.1, where the functional form is:

$$
p(x \mid y, \theta, M)=\frac{h(x, y)}{Z(\theta)} \exp \left(\sum_{i=1}^{k} w_{i}(\theta) t_{i}(x, y)\right)
$$

Consider the partial derivative of a marginal of this probability, $p(x-u \mid y, \theta, M)$, for $u \subset x$. Using Equation (18) in the Differentiation Lemma, the partial derivative becomes:

$$
\frac{\partial \log p(x-u \mid y, \theta, M)}{\partial \theta}=\sum_{i=1}^{k} \frac{\partial w_{i}(\theta)}{\partial \theta} \mathcal{E}_{u \mid x-u, y, \theta}\left(t_{i}(x, y)\right)-\frac{\partial Z(\theta)}{\partial \theta}
$$

If the partition function is not known in closed form (the case with the Boltzmann machine) then the final derivative $\partial Z(\theta) / \partial \theta$ is approximated (the key formula for doing this is Equation (28) in Appendix B).

To extend the Differentiation Lemma to chain graphs, use the trick illustrated with the feed-forward network. First, interpret the chain graph as a Bayesian network on chain components, as done in Equation (7), then apply the Differentiation Lemma. Finally, evaluate necessary local partial derivatives with respect to $\theta_{i}$ of each individual chain component. Since undirected graphs are not necessarily normalized, this may present a problem. In general, there is an undirected graph $G^{\prime}$ on variables $X \cup Y$. Following Theorem 2.1, the general form is:

$$
p(X \mid Y)=\frac{\prod_{C \in C l i q u e s\left(G^{\prime}\right)} f_{C}(C)}{\sum_{X} \prod_{C \in C l i q u e s\left(G^{\prime}\right)} f_{C}(C)}
$$

The local partial derivative with respect to $x$ becomes:

$$
\frac{\partial \log p(X \mid Y)}{\partial_{l} x}=\left(\sum_{C \in C l i q u e s\left(G^{\prime}\right), x \in C} \frac{\partial \log f_{C}(C)}{\partial_{l} x}\right)-\mathcal{E}_{X \mid Y}\left(\sum_{C \in C l i q u e s\left(G^{\prime}\right), x \in C} \frac{\partial \log f_{C}(C)}{\partial_{l} x}\right)
$$

The difficulty here is computing the expected value in the formula, which comes from the normalizing constant. Indeed, this computation forms the core of the early Boltzmann machine algorithm (Hertz et al., 1991). In general, this must be done using something like Gibbs sampling and the techniques of Section 7.1 can be applied directly.

# 6.2 Decomposing learning problems 

Learning problems can be decomposed into sub-problems in some cases. While the material in this section applies generally to these sorts of decompositions, this section considers one simple example and then proves some general results on problems decomposition. Problem decompositions can also be recomputed on the fly to create a search through a space of models that takes advantage of decompositions that exist. A general result is also presented on incremental decomposition. These results are simple applications of known methods for testing independence (Frydenberg, 1990; Lauritzen et al., 1990), with some added complication because of the use of plates.

Consider the simple learning problem given in Section 3, Figure 11 over two multinomial variables $v a r_{1}$ and $v a r_{2}$, and two Gaussian variables $x_{1}$ and $x_{2}$. For this problem we have specified two alternative models, model $M_{1}$ and model $M_{2}$. Model $M_{2}$ has an additional arc going from the discrete variable $v a r_{2}$ to the real valued variable $x_{1}$. We will use this subsequently to discuss local search of these models evaluated by their evidence.

A manipulation of the conditional distribution for this model, making use of Lemma 2.1, yields, for model $M_{1}$, the conditional distribution given in Figure 24. When parameters,

![img-22.jpeg](img-22.jpeg)

Figure 24: A simplification of model $M_{1}$
$\theta_{1}, \theta_{2}$ are a priori independent, and their data likelihoods do not introduce cross terms between them, the parameters become a posteriori independent as well. This occurs for $\theta_{1}$, $\theta_{2}$, and the set $\left\{\mu_{1}, \sigma_{1}\right\}$. This model simplification also implies the evidence for model $M_{1}$ decomposes similarly. Denote the sample of the variable $x_{1}$ as $x_{1, *}=x_{1,1}, \ldots, x_{1, N}$, and likewise for $v a r_{1}$ and $v a r_{2}$. In this case, the result is:
evidence $\left(M_{1}\right)=p\left(\right.$ var $\left._{1, *} \mid M_{1}\right) p\left(\right.$ var $\left._{2, *} \mid v a r_{1, *}, M_{1}\right) p\left(x_{1, *} \mid v a r_{1, *}, M_{1}\right) p\left(x_{2, *} \mid x_{1, *}, v a r_{1, *}, M_{1}\right)$.
The evidence for model $M_{2}$ is similar except that the posterior distribution of $\mu_{1}$ and $\sigma_{1}$ is replaced by the posterior distribution for $\mu_{1}^{\prime}$ and $\sigma_{1}^{\prime}$.

This result is general, and applies to Bayesian networks, undirected graphs, and more generally to chain graphs. Similar results are covered by Dawid and Lauritzen (1993) for a family of models they call hyper-Markov. The general result described above is an application of the rules of independence applied to plates. This uses the notion of nondeterministic children and parents introduced in Definition 6.1. It also requires a notion of local dependence, which is called the Markov blanket, following Pearl (1988), since it is a generalization of the equivalent set for Bayesian networks.

Definition 6.2 We have a chain graph $G$ without plates. The Markov blanket of a node $u$ is all neighbors, non-deterministic parents, non-deterministic children, and non-deterministic parents of the children and their chain components:

$$
\begin{aligned}
\text { Markov-blanket }(u)= & \text { neighbors }(u) \cup \text { ndparents }(u) \cup \text { ndchildren }(u) \\
& \cup \text { ndparents }(\text { chain-components }(\text { ndchildren }(u)))
\end{aligned}
$$

From Frydenberg (1990) it follows that $u$ is independent of the other non-deterministic variables in the graph $G$ given the Markov blanket.

To perform the simplification depicted in Figure 24, it is sufficient then to find the finest partitioning of the model parameters such that they are independent. The decomposition in Figure 24 represents the finest such partition of model $M_{1}$. The evidence for the model will then factor according to the partition, as given for model $M_{1}$ in Equation (21). For this task there is the following theorem, depicted graphically in Figure 25.

Theorem 6.1 (Decomposition). A model $M$ is represented by a chain graph $G$ with plates. Let the variables in the graph be $X$. There are $P$ possibly empty subsets of the variables $X$, $X_{i}$ for $i=1, \ldots, P$ such that unknown $\left(X_{i}\right)$ is a partition of unknown $(X)$. This induces a decomposition of the graph $G$ into $P$ subgraphs $G_{i}$ where:

- the graph $G_{i}$ contains the nodes $X_{i}$ and any arcs and plates occurring on these nodes, and
- the potential functions for cliques in $G_{i}$ are equivalent to those in $G$.

The induced decomposition represents the unique finest equivalent independence model to the original graph if and only if $X_{i}$ for $i=1, \ldots, P$ is the finest collection of sets such that, when ignoring plates, for every unknown node $u$ in $X_{i}$, its Markov blanket is also in $X_{i}$. This finest decomposition takes $O\left(|X|^{2}\right)$ to compute. Furthermore, the evidence for $M$ now becomes a product over each subgraph:

$$
\text { evidence }(M)=p\left(\operatorname{known}\left(X_{*}\right) \mid M\right)=f_{0} \prod_{i} f_{i}\left(\operatorname{known}\left(X_{i, *}\right)\right)
$$

for some functions $f_{i}$ (given in the proof).
Figure 25 shows how this decomposition works when there are unknown nodes. Figure 25(a) shows the basic problem and Figure 25(b) shows the finest decomposition. Notice the bottom component cannot be further decomposed because the variable $x_{1}$ is unknown.
![img-23.jpeg](img-23.jpeg)

Figure 25: The incremental decomposition of a model

In some cases, the functions $f_{i}$ given in the Decomposition Theorem in Equation (23) have a clean interpretation: they are equal to the evidence for the subgraphs. This result can be obtained from the following corollary.

Corollary 6.1.1 (Local Evidence). In the context of Theorem 6.1, suppose there exists a set of chain components $\tau_{j}$ from the graph ignoring plates such that $X_{j}=\tau_{j} \cup$ ndparents $\left(\tau_{j}\right)$, where unknown $\left(\right.$ ndparents $\left.\left(\tau_{j}\right)\right)=\emptyset$. Then

$$
f_{j}\left(\operatorname{known}\left(X_{j, *}\right)\right)=p\left(\operatorname{known}\left(\tau_{j}\right)_{*}\left|\operatorname{ndparents}\left(\tau_{j}\right)_{*}, M\right)\right.
$$

If we denote the $j$-th subgraph by model $M_{j}^{S}$, then this term is the conditional evidence for model $M_{j}^{S}$ given ndparents $\left(\tau_{j}\right)_{*}$. Denote by $M_{0}^{S}$ the maximal subgraph on known variables only (induced by cliques $_{0}$ as given in the proof of the Decomposition Theorem). If the condition of Corollary 6.1.1 holds for $M_{j}^{S}$ for $j=0,1, \ldots, P$, then it follows that the evidence for the model $M$ is equal to the product of the evidence for each subgraph:

$$
\operatorname{evidence}(M)=\prod_{i=0}^{P} \operatorname{evidence}\left(M_{i}^{S}\right)
$$

This holds in general if the original graph $G$ is a Bayesian network, as used in learning Bayesian networks (Buntine, 1991c; Cooper \& Herskovits, 1992).

Corollary 6.1.2 Equation (24) holds if the parent graph $G$ is a Bayesian network with plates.

In general, we might consider searching through a family of graphical models. To do this local search (Johnson, Papdimitriou, \& Yannakakis, 1985) or numerical optimization can be used to find high posterior models, or Markov chain Monte Carlo methods to select a sample of representative models, as discussed in Section 7.2. To do this, how to represent a family of models must be shown. Figure 26, for instance, is similar to the models of Figure 11 except that some arcs are hatched. This is used to indicate that these arcs are optional.
![img-24.jpeg](img-24.jpeg)

Figure 26: A family of models (optional arcs hatched)
To instantiate a hatched arc they can either be removed or replaced with a full arc. This graphical model then represents many different models, for all $2^{4}$ possible instantiations of the arcs. Prior probabilities for these models could be generated using a scheme such as in (Buntine, 1991c, p54) or (Heckerman et al., 1994), where a prior probability is assigned by

a domain expert for different parts of the model, arcs and parameters, and the prior for a full model found by multiplication. The family of models given by Figure 26 includes those of Figure 11 as instances. During search or sampling, an important property is the Bayes factor for the two models, Bayes-factor $\left(M_{2}, M_{1}\right)$, as described in Section 3.1. Because of the Decomposition Theorem and its corollary, the Bayes factor for $M_{2}$ versus $M_{1}$ can be found by looking at local Bayes factors. The difference between models $M_{1}$ and $M_{2}$ is the parent for the variable $x_{1}$,

$$
\text { Bayes-factor }\left(M_{2}, M_{1}\right)=\frac{p\left(x_{1, *} \mid \text { var }_{1, *}, \text { var }_{2, *}, M_{2}\right)}{p\left(x_{1, *} \mid \text { var }_{1, *}, M_{1}\right)}
$$

That is, the Bayes factor can be computed from only considering the models involving $\mu_{1}, \sigma_{1}$ and $\mu_{1}^{\prime}, \sigma_{1}^{\prime}$.

This incremental modification of evidence, Bayes factors, and finest decompositions is also general, and follows directly from the independence test. A similar property for undirected graphs is given in (Dawid \& Lauritzen, 1993). This is developed below for the case of directed arcs and non-deterministic variables. Handling deterministic variables will require repeated application of these results, because several non-deterministic variables may be effected when adding a single arc between deterministic variables.

Lemma 6.3 (Incremental decomposition). For a graph $G$ in the context of Theorem 6.1, we have two non-deterministic variables $U$ and $V$ such that $U$ is given. Consider adding or removing a directed arc from $U$ to $V$. To update the finest decomposition of $G$, there is a unique subgraph containing the unknown variables in ndparents(chain-component(V)). To this subgraph add or delete an arc from $U$ to $V$, and add or delete $U$ to the subgraph if required.

Shaded non-deterministic parents can be added at will to nodes in a graph, and the finest decomposition remains unchanged except for a few additional arcs. The use of hatched arcs in these contexts causes no additional trouble to the decomposition process. That is, the finest decomposition for a graph with plates and hatched directed arcs is formed as if the arcs where unhatched directed arcs. The evidence is adjusted during the search by adding the different parents as required.

# 6.3 Bayes factors for the exponential family 

To make use of the decomposition results in a learning system it is necessary to be able to generate Bayes factors or evidence for the component models. For models in the exponential family, whose normalization constant is known in closed form, this turns out to be easy. If these exact computations are not available, various approximation methods can be used to compute the evidence or Bayes factors (Kass \& Raftery, 1993); some are discussed in Section 7.3.

If the conjugate distribution for an exponential family model and its derivatives can be readily computed, then the Bayes factor for the model can be found in closed form. Along with the above decomposition methods, this result is an important basis of many fast Bayesian algorithms considering multiple models. It is used explicitly or implicitly in all Bayesian methods for learning decision trees, directed graphical models (with discrete or Gaussian variables), and linear regression (Buntine, 1991b; Spiegelhalter et al., 1993).

For instance, if the normalizing constant $Z_{\theta}(\tau)$ in Lemma 4.1 was known in closed form, then the Bayes factor can be readily computed.

Lemma 6.4 Consider the context of Lemma 4.1. Then the model likelihood or evidence, given by evidence $(M)=p\left(x_{1}, \ldots, x_{N} \mid y_{1}, \ldots, y_{N}, M\right)$, can be computed as:

$$
\begin{aligned}
\text { evidence }(M) & =\frac{p(\theta \mid \tau) \prod_{j=1}^{N} p\left(x_{j} \mid y_{j}, \theta\right)}{p\left(\theta \mid \tau^{\prime}\right)} \\
& =\frac{Z_{\theta}\left(\tau^{\prime}\right)}{Z_{\theta}(\tau) Z_{2}^{N}}
\end{aligned}
$$

For $y \mid x \sim$ Gaussian this involves multiplying out the two sets of normalizing constants for the Gaussian and Gamma distributions. The evidence for some common exponential family distributions is given in Appendix B in Table 5

For instance, consider the learning problem given in Figure 24. Assume that the variables $v a r_{1}$ and $v a r_{2}$ are both binary ( 0 or 1 ) and that the parameters $\theta_{1}$ and $\theta_{2}$ are interpreted as follows:

$$
\begin{aligned}
p\left(v a r_{1}=0 \mid \theta_{1}\right) & =\theta_{1} \\
p\left(v a r_{2}=0 \mid v a r_{1}=0, \theta_{2}\right) & =\theta_{2,0 \mid 0} \\
p\left(v a r_{2}=0 \mid v a r_{1}=1, \theta_{2}\right) & =\theta_{2,0 \mid 1}
\end{aligned}
$$

If we use Dirichlet priors for these parameters, as shown in Table 3, then the priors are:

$$
\begin{aligned}
\left(\theta_{1}, 1-\theta_{1}\right) & \sim \operatorname{Dirichlet}\left(\alpha_{1,0}, \alpha_{1,1}\right) \\
\left(\theta_{2,0 \mid j}, 1-\theta_{2,0 \mid j}\right) & \sim \operatorname{Dirichlet}\left(\alpha_{2,0 \mid j}, \alpha_{2,1 \mid j}\right) \quad \text { for } j=0,1
\end{aligned}
$$

where $\theta_{2,0 \mid 0}$ is a priori independent of $\theta_{2,0 \mid 1}$. The choice of priors for these distributions is discussed in (Box \& Tiao, 1973; Bernardo \& Smith, 1994). Denote the corresponding sufficient statistics as $n_{1, j}$ (equal to the number of data where $\operatorname{var}_{1}=j$ ) and $n_{2, j \mid i}$ (equal to the number of data where $v a r_{2}=j$ and $v a r_{1}=i$ ). Then the first two terms of the evidence for model $M_{1}$, read directly from Table 5, can be written as:

$$
\begin{aligned}
p\left(v a r_{1, *} \mid M_{1}\right) & =\frac{\operatorname{Beta}\left(n_{1,0}+\alpha_{1,0}, n_{1,1}+\alpha_{1,1}\right)}{\operatorname{Beta}\left(\alpha_{1,0}, \alpha_{1,1}\right)} \\
p\left(v a r_{2, *} \mid v a r_{1, *}, M_{1}\right) & =\frac{\operatorname{Beta}\left(n_{2,0 \mid 0}+\alpha_{2,0 \mid 0}, n_{2,1 \mid 0}+\alpha_{2,1 \mid 0}\right)}{\operatorname{Beta}\left(\alpha_{2,0 \mid 0}, \alpha_{2,1 \mid 0}\right)} \frac{\operatorname{Beta}\left(n_{2,0 \mid 1}+\alpha_{2,0 \mid 1}, n_{2,1 \mid 1}+\alpha_{2,1 \mid 1}\right)}{\operatorname{Beta}\left(\alpha_{2,0 \mid 1}, \alpha_{2,1 \mid 1}\right)}
\end{aligned}
$$

Assume the variables $x_{1}$ and $x_{2}$ are Gaussian with means given by

$$
\begin{array}{ll}
\mu_{1 \mid 0} & \text { when } v a r_{1}=0 \\
\mu_{1 \mid 1} & \text { when } v a r_{1}=1 \\
\mu_{2 \mid 0,1}+\mu_{2 \mid 0,2} x_{1} & \text { when } v a r_{1}=0 \\
\mu_{2 \mid 1,1}+\mu_{2 \mid 1,2} x_{1} & \text { when } v a r_{1}=1
\end{array}
$$

and variances $\sigma_{1 \mid j}$ and $\sigma_{2 \mid j}$ respectively. In this case, we split the data set into two parts, those when $v a r_{1}=0$, and those when $v a r_{1}=1$. Each get their own parameters, sufficient

statistics, and contribution to the evidence. Conjugate priors from Table 3 in Appendix B (using $y \mid x \sim$ Gaussian) are indexed accordingly as:

$$
\begin{aligned}
& \mu_{i \mid j} \mid \sigma_{i \mid j} \sim \operatorname{Gaussian}\left(\mu_{0, i \mid j}, \frac{\Sigma_{0, i \mid j}}{\sigma_{i \mid j}^{2}}\right) \quad \text { for } i=1,2 \text { and } j=0,1, \\
& \sigma_{i \mid j}^{-2} \sim \operatorname{Gamma}\left(\delta_{0, i \mid j} / 2, \beta_{0, i \mid j}\right) \quad \text { for } i=1,2 \text { and } j=0,1 .
\end{aligned}
$$

Notice that $\Sigma_{0, i \mid j}$ is one-dimensional when $i=0$ and two-dimensional when $i=2$. Suitable sufficient statistics for this situation are read from Table 4 by looking at the data summaries used there. This can be simplified for $x_{1}$ because $d=1$ and $y_{1}$ for the Gaussian is uniformly 1. Thus the sufficient statistics for $x_{1}$ become the means and variances for the different values of $v a r_{1}$. Denote $\overline{x_{1 \mid 0}}$ and $\overline{x_{1 \mid 1}}$ as the sample means of $x_{1}$ when $v a r_{1}=0,1$, respectively, and $s_{1 \mid 0}^{2}$ and $s_{1 \mid 1}^{2}$ their corresponding sample variances. This cannot be done for the second case, so we use the notation from Table 4, where $\Sigma, \bar{\mu}, \beta$ from Table 4 become, respectively, $\Sigma_{2 \mid j}, \overline{\mu_{2 \mid j}}, \beta_{2 \mid j}$. Change the vector $y$ to $\left(1, x_{1}\right)$ when making the calculations indicated here. The sufficient statistics are, for each case of $v a r_{1}=j$ :

$$
\begin{aligned}
S_{2 \mid j} & =\sum_{i=1}^{N} 1_{v a r_{1, i}=j} y_{i} y_{i}^{\dagger} \\
m_{2 \mid j} & =\sum_{i=1}^{N} 1_{v a r_{1, i}=j} x_{i} y_{i} \\
s_{2 \mid j}^{2} & =\sum_{i=1}^{N} 1_{v a r_{1, i}=j}\left(x_{i}-\overline{\mu_{2 \mid j}^{\dagger}} y_{i}\right)^{2}
\end{aligned}
$$

The evidence for the last two terms can now be read from Table 5. This becomes:

$$
\begin{aligned}
& p\left(x_{1, *} \mid v a r_{1, *}, M_{1}\right)=\prod_{j=0,1} \frac{\sqrt{\Sigma_{0,1 \mid j}}}{\pi^{n_{1, j} / 2} \sqrt{\Sigma_{0,1 \mid j}+n_{1, j}}} \frac{\Gamma\left(\left(\delta_{0,1 \mid j}+n_{1,0}\right) / 2\right)}{\Gamma\left(\delta_{0,1 \mid j} / 2\right) \beta_{0,1 \mid j}^{\delta_{0,1 \mid j} / 2}} \\
& \left(\beta_{0,1 \mid j}+s_{1 \mid j}^{2}+\frac{\Sigma_{0} N}{\Sigma_{0}+N}\left(\bar{x}-\mu_{0,1 \mid j}\right)^{2}\right)^{\left(\delta_{0,1 \mid j}+n_{1, j}\right) / 2} \\
& p\left(x_{2, *} \mid x_{1, *}, v a r_{1, *}, M_{1}\right)=\prod_{j=0,1} \frac{\operatorname{det}^{1 / 2} \Sigma_{0,2 \mid j}}{\pi^{n_{1, j} / 2} \operatorname{det}^{1 / 2} \Sigma_{2 \mid j}} \frac{\Gamma\left(\left(\delta_{0,2 \mid j}+n_{1,0}\right) / 2\right) \beta_{2 \mid j}^{\left(\delta_{0,2 \mid j}+n_{1, j}\right) / 2}}{\Gamma\left(\delta_{0,2 \mid j} / 2\right) \beta_{0,2 \mid j}^{\delta_{0,2 \mid j} / 2}}
\end{aligned}
$$

The final simplification of the model is given in Figure 27.

# 7. Approximate methods on graphical models 

Exact algorithms for learning of any reasonable size invariably involve the recursive arc reversal theorem of Section 4.2. Most learning methods, however, use approximate algorithms at some level. The most common uses of the exponential family within approximation algorithms were summed up in Figure 22. Various other methods for inference on plates can be

![img-25.jpeg](img-25.jpeg)

Figure 27: The full simplification of model $M_{1}$
applied either at the model level or the parameter level: Gibbs sampling, first described in Section 7.1, other more general Markov chain Monte Carlo algorithms, EM style algorithms (Dempster, Laird, \& Rubin, 1977), and various closed form approximations such as the mean field approximation, and the Laplace approximation (Berger, 1985; Azevedo-Filho \& Shachter, 1994). This section summarizes the main families of these approximate methods.

# 7.1 Gibbs sampling 

Gibbs sampling is the basic tool of simulation and can be applied to most probability distributions (Geman \& Geman, 1984; Gilks et al., 1993a; Ripley, 1987) as long as the full joint has no zeros (all variable instantiations are possible). It is a special case of the general Markov chain Monte Carlo methods for approximate inference (Ripley, 1987; Neal, 1993). Gibbs sampling can be applied to virtually any graphical model whether there are plates, undirected or directed arcs, and whether the variables are real or discrete. Gibbs sampling does not apply to graphs with deterministic nodes, however, since these put zeroes in the full joint. This section describes Gibbs sampling without plates, as a precursor to discussing Gibbs sampling with plates in Section 7.2. On challenging problems, other forms of Markov chain Monte Carlo sampling can and should be tried. The literature is extensive.

Gibbs sampling corresponds to a probabilistic version of gradient ascent, although their goals of averaging as opposed to maximizing are fundamentally different. Gradient ascent in real valued problems corresponds to simple methods from function optimization (Gill et al., 1981) and in discrete problems corresponds to local repair or local search (Johnson et al., 1985; Minton, Johnson, Philips, \& Laird, 1990; Selman, Levesque, \& Mitchell, 1992). Gibbs sampling varies gradient ascent by introducing a random component. The algorithm usually tries to ascend, but will sometimes descend, as a strategy for exploring further around the search space. So the algorithm tends to wander around local maxima with occasional excursions to other regions of the space. Gibbs sampling is also the core algorithm of simulated annealing if temperature is held equal to one (van Laarhoven \& Aarts, 1987).

To sample a set of variables $X$ according to some non-zero distribution $p(X)$, initialize $X$ to some value and then repeatedly resample each variable $x \in X$ according to its conditional

probability $p(x \mid X-\{x\})$. For the simple medical problem of Figure 2, suppose the value of symptoms is known, and the remaining variables are to be sampled, then do as follows:

1. Initialize the remaining variables somehow.
2. Repeat the following for $i=1,2,3, \ldots$, and record the sample of $A g e_{i}, O c c_{i}, \operatorname{Clim}_{i}, \operatorname{Dis}_{i}$ at the end of each cycle.
(a) Reassign $A g e$ by sampling it according to the conditional:

$$
p(A g e \mid O c c, \text { Clim, Dis, Symp })
$$

That is, take the values of $O c c, C l i m, D i s, S y m p$ as given and compute the resulting conditional distribution on $A g e$. Then sample $A g e$ according to that distribution.
(b) Reassign $O c c$ by sampling it according to the conditional:

$$
p(O c c \mid A g e, C l i m, D i s, S y m p)
$$

(c) Reassign Clim by sampling it according to the conditional:

$$
p(\text { Clim } \mid A g e, O c c, \text { Dis, Symp })
$$

(d) Reassign Dis by sampling it according to the conditional:

$$
p(\text { Dis } \mid A g e, \text { Clim, Occ, Symp })
$$

This sequence of steps is depicted in Figure 28. In this figure, the basic graph has been re-
![img-26.jpeg](img-26.jpeg)

Figure 28: Gibbs sampling on the medical example
arranged for each step to represent the dependencies that arise during the sampling process. This uses the arc reversal and conditioning operators introduced previously.

The effect of sampling is not immediate. $A g e_{2}, O c c_{2}, \operatorname{Clim}_{2}, \operatorname{Dis}_{2}$ is conditionally dependent on $A g e_{1}, O c c_{1}, \operatorname{Clim}_{1}, \operatorname{Dis}_{1}$, and in general so is $A g e_{i}, O c c_{i}, \operatorname{Clim}_{i}, \operatorname{Dis}_{i}$ for any $i$. However the effect of the sampling scheme is that in the long run, for large $i, A g e_{i}, O c c_{i}, \operatorname{Clim}_{i}, \operatorname{Dis}_{i}$

is approximately generated according to $p(A g e, O c c, C l i m, D i s \mid S y m p)$ independently of $A g e_{1}, O c c_{1}, \operatorname{Clim}_{1}, D i s_{1}$. In Gibbs sampling, all the conditional sampling is done in accordance with the original distribution, and since this is a stationary process, in the long run the samples converge to the stationary distribution or fixed-point of the process. Methods for making subsequent samples independent are known as regenerative simulation (Ripley, 1987) and correspond to sending the temperature back to zero occasionally.

With this sample different quantities such as the probability a patient will have $A g e>20$ and $\operatorname{Clim}=$ tropical given $S y m p$ can be estimated. This is done by looking at the frequency of this event in the generated sample. The justification for this is the subject of Markov process theory (Çinlar, 1975, Theorem 2.26). The following result, presented informally, applies:
Comment 7.1 Let $x_{1}, x_{2}, \ldots, x_{I}$ be a sequence of discrete variables from a Gibbs sampler for the distribution $p(x)>0$. Then the average of $g\left(x_{i}\right)$ approaches the expected value with probability 1 as I approaches infinity:

$$
\frac{1}{I} \sum_{i=1}^{I} g\left(x_{i}\right) \longrightarrow \overline{g(x)}=\mathcal{E}(g(x))
$$

Further, for a second function $h\left(x_{i}\right)$, the ratio of two sample averages for $g$ and $h$ approaches their "true" ratio:

$$
\frac{\sum_{i=1}^{I} g\left(x_{i}\right)}{\sum_{i=1}^{I} h\left(x_{i}\right)} \longrightarrow \frac{\overline{g(x)}}{\overline{h(x)}}
$$

This is used to approximate conditional expected values.
To complete this procedure it is necessary to know how many Gibbs samples to take, how large to make $I$, and how to estimate the error in the estimate. Both these questions have no easy answer but heuristic strategies exist (Ripley, 1987; Neal, 1993).

For Bayesian networks this scheme is easy in general since the only requirement when sampling from $p(x \mid X-\{x\})$ is the conditional distribution for nodes connected to $x$, and the global probabilities do not need to be calculated. Notice, for instance, that in Figure 28 some sampling operations do not require all five variables. The general form for Bayesian networks given in Equation (2) goes as follows:

$$
p(x \mid X-\{x\})=\frac{p(X)}{\sum_{x} p(X)}=\frac{p\left(x \mid \text { parents }(x)\right) \prod_{y: x \in \text { parents }(y)} p(y \mid \text { parents }(y))}{\sum_{x} p\left(x \mid \text { parents }(x)\right) \prod_{y: x \in \text { parents }(y)} p(y \mid \text { parents }(y))}
$$

Notice the product is over a subset of variables. Only include conditional distributions for variables that have $x$ as a parent. Thus, the formula only involves examining the parents, children and children's parents of $x$, the so-called Markov blanket (Pearl, 1988). Also, notice normalization is only required over the single dimension changed in the current cycle, done in the denominator. For $x$ discrete, these conditional probabilities can be enumerated and direct sampling done for $x$.

The kind of simplification above for Bayesian networks also applies to undirected graphs and chain graphs, with or without plates. Here, modify Equation (4):

$$
p(x \mid X-\{x\})=\frac{\exp \left(\sum_{C: x \in C \in \operatorname{cliques}(G)} f_{C}(C)\right)}{\sum_{x} \exp \left(\sum_{C: x \in C \in \operatorname{cliques}(G)} f_{C}(C)\right)}
$$

In this formula, ignore all cliques not containing $x$ so, again, Gibbs sampling only computes with information local to the node. Also, the troublesome normalization constant does not have to be computed because the probability is a ratio of functions and so cancels out. As before, normalization is only required over the single dimension $x$.

# 7.2 Gibbs sampling on plates 

Many learning problems can be represented as Bayesian networks. For instance, the simple unsupervised learning problem represented in Figure 10 is a Bayesian network once the plate is expanded out. It follows that Gibbs sampling is readily applied to learning as a general inference algorithm (Gilks et al., 1993a, 1993b).

Consider a simplified example of this unsupervised learning problem. In this model, assume that each variable $v a r_{1}$ and $v a r_{2}$ belongs to a mixture of Gaussians of known variance equal to 1.0. This simple model is given in Figure 29. For a given class, class $=c$,
![img-27.jpeg](img-27.jpeg)

Figure 29: Unsupervised learning in two dimensions
the variables $v a r_{1}$ and $v a r_{2}$ are distributed as Gaussian with means $\mu_{1, c}$ and $\mu_{2, c}$. In the uniform, unit-variance case the distribution for each sample is given by:

$$
p\left(\operatorname{var}_{1}, \operatorname{var}_{2} \mid, \phi, \mu, M\right)=\sum_{c} \phi_{c} N\left(\operatorname{var}_{1}-\mu_{1, c}\right) N\left(\operatorname{var}_{2}-\mu_{2, c}\right)
$$

where $N($,$) is the one-dimensional Gaussian probability density function with standard$ deviation of 1 . This model might seem trivial, but if the standard deviation were to vary as well, the model corresponds to a Kernel density estimate so can approximate any other distribution arbitrarily well using sufficient number of tiny Gaussians.

In this simplified Gaussian mixture model, the sequence of steps for Gibbs sampling goes as follows:

1. Initialize the variables $\phi_{c}, \mu_{1, c}, \mu_{2, c}$ for each class $c$.
2. Repeat the following and record the sample of $\phi_{c}, \mu_{1, c}, \mu_{2, c}$ for each class $c$ at the end of each cycle.
(a) For $i=1, \ldots, N$, reassign class $_{i}$ according to the conditional:

$$
p\left(\text { class }_{i} \mid \text { var }_{1, i}, \text { var }_{2, i}, \phi, \mu_{1}, \mu_{2}\right)
$$

(b) Reassign the vector $\phi$ by sampling according to the conditional:

$$
p\left(\phi \mid \text { class }_{i}: i=1, \ldots, N\right)
$$

(c) Reassign the vector $\mu_{1}$ (and $\mu_{2}$ ) by sampling according to the conditional:

$$
p\left(\mu_{1} \mid \text { var }_{1, i}, \text { class }_{i}: i=1, \ldots, N\right)
$$

Figure 30(a) illustrates Step 2(a) in the language of graphs. Figure 30(b) illustrates
![img-28.jpeg](img-28.jpeg)

Figure 30: Gibbs sampling in the unsupervised learning problem
Steps 2(b) and 2(c). Step 2(a) represents the standard sampling operation using inference on Bayesian networks without plates. Step 2(b) and 2(c) are also easy to perform because in this case the distributions are exponential family, and the graph matches the conditions for Lemma 6.1.2. Therefore, each of the model parameters $\phi, \mu_{1}, \mu_{2}$ are a posteriori independent and their distribution is known in closed form, with the sufficient statistics calculated in $O(N)$ time.

One important caveat in the use of Gibbs sampling for learning is the problem of symmetry. In the above description, there is nothing to distinguish class 1 from class 2 . Initially, the class centers $\mu$ for the above process will remain distinct. Asymptotically, since there is nothing in the problem definition to distinguish between class 1 and class 2 , they will appear indistinguishable. This problem is handled by symmetry breaking: force $\mu_{1, c}<\mu_{2, c}$.

Gibbs sampling applies whenever there are variables associated with the data that are not given. Hidden or latent variables are an example. Incomplete data (or missing values) (Quinlan, 1989), robust methods and modeling of outliers, and various density estimation and non-parametric methods all fall in this family of models (Titterington et al., 1985). Gibbs sampling generalizes to virtually any graphical model with plates and unshaded nodes inside the plate; the sequence of sampling operations will be much the same as in Figure 30. If the underlying distribution is exponential family, for instance, Lemma 5.1 applies after shading all nodes inside the plate; each full cycle is guaranteed to be linear time in the sample size. The algorithm in the exponential family case is summed up in Figure 31. Figure 31(I) shows the general learning problem, extending the mixture model of Figure 22. This same structure appears in Figure 29. However, in Figure 31(I) the sufficient statistics $T\left(x_{*}, u_{*}\right)$ are also shown. Figure 31(II) shows more of the algorithm, generalizing Figure 30(a) and (b). Again the role of sufficient statistics is shown. The sampling in Figure 30(b) first computes the sufficient statistics and then sampling applies from that.

Thomas, Spiegelhalter, and Gilks (1992)(Gilks et al., 1993b) have taken advantage of this general applicability of sampling to create a compiler that converts a graphical representation of a data analysis problem, with plates, into a matching Gibbs sampling algorithm. This scheme applies to a broad variety of data analysis problems.

![img-29.jpeg](img-29.jpeg)

Figure 31: Gibbs sampling with the exponential family

# 7.3 A closed form approximation 

What would happen to Gibbs sampling if the number of cases in the training sample, $N$, was large compared to the number of unknown parameters in the problem? A good way to think of this is: first, if $N$ is sufficiently large, then the samples of the model parameters $\phi$ and $\mu_{1}, \mu_{2}$ will tend to drift around their mean because their posterior variance would be $O(I / N)$. That is, after the $i$-th step, the sample is $\phi_{i}, \mu_{1, i}, \mu_{2, i}$. The $i+1$-th sample $\phi_{i+1}, \mu_{1, i+1}, \mu_{2, i+1}$ would be conditionally dependent on these, but because $N$ is large, the posterior variance of the $i+1$-th sample given the $i$-th sample would be small so that:

$$
\phi_{i+1} \approx \mathcal{E}_{\phi_{i}, \mu_{1, i}, \mu_{2, i}}\left(\phi_{i+1}\right)
$$

This approximation is used with Markov chain Monte Carlo methods by the mean field method from statistical physics, popular in neural networks (Hertz et al., 1991). Rather than sampling a sequence of parameters $\theta, \theta_{1}, \theta_{2}, \ldots, \theta_{i}$, according to some scheme, use the deterministic update:

$$
\overline{\theta_{i+1}}=\mathcal{E}_{\theta_{i}=\overline{\theta_{i}}}\left(\theta_{i+1}\right)
$$

where the expected value is according to the sampling distribution. This instead generates a deterministic sequence $\overline{\theta_{1}}, \overline{\theta_{2}}, \ldots, \overline{\theta_{i}}$ that under reasonable conditions converges to some maxima. This kind of approach leads naturally to the EM algorithm, which will be discussed in Section 7.4.

### 7.4 The expectation maximization (EM) algorithm

The expectation maximization algorithm, widely known as the EM algorithm, corresponds to a deterministic version of Gibbs sampling used to search for the MAP estimate for model parameters (Dempster et al., 1977). It is generally considered to be faster than gradient descent. Convergence is slow near a local maxima so some implementations switch to conjugate gradient or other methods (Meilijson, 1989) when near a solution. The computation used to find the derivative is similar to the computation used for the EM algorithm, so this does not require a great deal of additional code. Also, the determinism means the EM algorithm no longer generates unbiased posterior estimates of model parameters. The intended

gain is speed, not accuracy. The EM algorithm can generally be applied to exponential family models wherever Gibbs sampling can be applied. The correspondence between EM and Gibbs is shown below.

Consider again the simple unsupervised learning problem represented in Figure 29 (Section 7.2). In this case, the sequence of steps for the EM algorithm is similar to that for the Gibbs sampler. The EM algorithm works on the means or modes of unknown variables instead of sampling them. Rather than sampling the set of classes and thereby computing sufficient statistics so that a distribution for $\phi$ and $\mu_{1}, \mu_{2}$ can be found, a sequence of class means are generated and thereby used to compute expected sufficient statistics. Likewise, instead of sampling new parameters $\phi$ and $\mu_{1}, \mu_{2}$, modes are then computed from the expected sufficient statistics.

Consider again the unsupervised learning problem in Figure 9. Suppose there are 10 classes and that the three variables $v a r_{1}, v a r_{2}, v a r_{3}$ are finite valued and discrete and modeled with a multinomial with probabilities conditional on the class value class $_{i}$. The sufficient statistics in this case are all counts: $n_{j}$ is the number of cases where the class is $j$; $n_{v, k \mid j}$ is the number of cases where class $=j$ and $v a r_{v}=k$ :

$$
\begin{aligned}
n_{j} & =\sum_{i=1}^{N} 1_{\text {class }_{i}=j} \\
n_{v, k \mid j} & =\sum_{i=1}^{N} 1_{\text {class }_{i}=j} 1_{v a r_{v, i}=k}
\end{aligned}
$$

The expected sufficient statistics computed from the rules of probability for a given set of parameters $\phi$ and $\theta_{1}, \theta_{2}, \theta_{3}$ are given by:

$$
\begin{aligned}
\overline{n_{j}} & =\sum_{i=1}^{N} p\left(\text { class }_{i}=j \mid \text { var }_{1, i}, \text { var }_{2, i}, \text { var }_{3, i}, \phi, \theta_{1}, \theta_{2}, \theta_{3}\right) \\
\overline{n_{v, k \mid j}} & =\sum_{i=1}^{N} p\left(\text { class }_{i}=j \mid \text { var }_{1, i}, \text { var }_{2, i}, \text { var }_{3, i}, \phi, \theta_{1}, \theta_{2}, \theta_{3}\right) 1_{\text {var }_{v, i}=k}
\end{aligned}
$$

Thanks to Lemma 4.2, these kinds of expected sufficient statistics can be computed for most exponential family distributions. Once sufficient statistics are computed for any of the distributions posterior means or modes of the model parameters (in this case $\phi$ and $\theta_{1}, \theta_{2}, \theta_{3}$ ) can be found.

1. Initialize the parameters $\phi$ and $\theta_{1}, \theta_{2}, \theta_{3}$.
2. Repeat the following until some convergence criteria is met:
(a) Compute the expected sufficient statistics $\overline{n_{j}}$ and $\overline{n_{v, k \mid j}}$.
(b) Recompute $\phi$ and $\theta_{1}, \theta_{2}, \theta_{3}$ to be equal to their mode conditioned on the sufficient statistics. For many posterior distributions, these can be found in standard tables, and in most cases found via Lemma 4.2. For instance, using the mean for $\phi$ gives:

$$
\phi_{j}=\frac{\overline{n_{j}}+\alpha_{j}}{\sum_{j}\left(\overline{n_{j}}+\alpha_{j}\right)}
$$

All of the other Gibbs sampling algorithms discussed in Section 7.2 can be similarly placed in this EM framework. When the mode is used in Step 2(b), ignoring numerical problems, the EM algorithm converges on a local maxima of the posterior distribution for the parameters (Dempster et al., 1977). The general method is summarized in the following comment (Dempster et al., 1977).

Comment 7.2 The conditions of Lemma 5.1 apply with data variables $X$ inside the plate and model parameters $\theta$ outside. In addition, some of the variables $U \subset X$ are latent, so they are unknown and unshaded. Some of the remaining variables are sometimes missing, so, for the data $X_{i}$, variables $V_{i} \subset(X-U)$ are not given. This means the data given for the $i$-th datum is $X-U-V_{i}$ for $i=1, \ldots N$. The EM algorithm goes as follows:

E-step: The contribution to the expected sufficient statistics for each datum is:

$$
E T_{i}=\mathcal{E}_{U_{i}, V_{i} \mid X-U_{i}-V_{i}, \theta}\left(t\left(X_{i}\right)\right)
$$

The expected sufficient statistic is then $E T=\sum_{i=1}^{N} E T_{i}$.
M-step: Maximize the conjugate posterior using the expected sufficient statistics ET in place of the sufficient statistics using the MAP approach for this distribution.

The fixed point of this algorithm is a local maxima of the posterior for $\theta$.
Figure 31(II) for Gibbs sampling in Section 7.2 illustrates the steps in EM nicely. Figure 31 (II)(a) corresponds to the E-step. The expected sufficient statistics are found from the parameters $\theta$. Rather than sampling $u$, and therefore computing the sufficient statistics, the expected sufficient statistics are computed. Figure 31(II)(b) corresponds to the M-step. Here, given the sufficient statistics, the mean or mode of the parameters $\theta$ are computed instead of being sampled. EM is therefore Gibbs with a mean/mode approximation done at the two major sampling steps of the algorithm.

In some cases, the expected sufficient statistics can be computed in closed form. Assume the exponential family distribution for $p(X \mid \theta)$ has a known normalization constant $Z(\theta)$ and the link function $w^{-1}$ exists. For some $i$, the normalizing constant for the exponential family distribution $p\left(U_{i}, V_{i} \mid X-U_{i}-V_{i}, \theta\right)$ is known in closed form. Denote it by $Z_{i}(\theta)$. Then using the notation of Theorem 4.1:

$$
E T_{i}= \begin{cases}t\left(X_{i}\right) & \text { if } U=V_{i}=\emptyset \\ \frac{\mathrm{d} w(\theta)}{\mathrm{d} \theta}^{-1} \frac{\mathrm{~d} \log Z_{i}(\theta)}{\mathrm{d} \theta} & \text { otherwise }\end{cases}
$$

# 8. Partial exponential models 

In some cases, only an initial, inner part of a learning problem can be handled using the recursive arc reversal theorem of Section 4.3. In this case, simplify what can be simplified, and then solve the remainder of the problem using a generic method like the MAP approximation. This section presents several examples: linear regression with heterogeneous variance, feed-forward networks with a linear output layer, and Bayesian networks.

This general process was depicted in the graphical model for the partial exponential family of Figure 22. This is an abstraction used to represent the general process. Consider

the problem of learning a Bayesian network, both structure and parameters, where the distribution is exponential family given the network structure. The variable $T$ is a discrete variable indicating which graphical structure is chosen for the Bayesian network. The variable $X$ represents the full set of variables given for the problem. The variable $\Theta_{T}$ represents the distributional parameters for the Bayesian network, and is the part of the model that is conveniently exponential family. That is, $p\left(X \mid \Theta_{T}, T\right)$ will be treated as exponential for different $\Theta_{T}$ and hold $T$ fixed. The sufficient statistics in this case are given by $s s(X *, T)$. In this case, the subproblem that conveniently falls in the exponential family, $p\left(\Theta_{T} \mid X *, T\right)$ is simplified, but it is necessary to resort to the more general learning techniques of previous sections to solve the remaining part of the problem, $p(T \mid X *)$.

# 8.1 Linear regression with heterogeneous variance 

Consider the heterogeneous variance problem given in Figure 32. This shows a graphical model for the linear regression problem of Section 4.4 modified to the situation where the standard deviation is heterogeneous, so it is a function of the inputs $x$ as well. In this case,
![img-30.jpeg](img-30.jpeg)

Figure 32: Linear regression with heterogeneous variance
the standard deviation $s$ is not given but is computed via:

$$
s=\exp \left(\sum_{i=1}^{m} \text { weights- } \sigma_{i} \text { basis }_{i}(x)\right)
$$

The exponential transformation guarantees that the standard deviation $s$ will also be positive.

The corresponding learning model can be simplified to the graph in Figure 33. Compare this with the model given in Figure 21. What is the difference? In this case, the sufficient statistics exist, but they are shown to be deterministically dependent on the sample and ultimately on the unknown parameters for the standard deviation weights- $\sigma$. If the parameters for the standard deviation were known then the graph could be reduced to Figure 21. Computationally, this is an important gain. It says that for a given set of values for weights- $\sigma$, calculation can be done that is linear time in the sample size to arrive at a characterization

![img-31.jpeg](img-31.jpeg)

Figure 33: The heterogeneous variance problem with the plate simplified
of what the parameters from the mean, weights- $\mu$, should be. In short, one half of a problem, $p\left(\right.$ weights- $\mu \mid$ weights- $\sigma, y_{i}, x_{., i}: i=1, \ldots, N$ ), is well understood. To do a search for the MAP solution, search the space of parameters for the standard deviation, weights- $\sigma$, since the remaining (weights- $\mu$ ) is given.

Another variation of linear regression replaces the Gaussian error function with a more robust error function such as Student's $t$ distribution, or an $L_{q}$ norm for $1<q<2$. By introducing a convolution, these robust regression models can be handled by combining the EM algorithm with standard least squares (Lange \& Sinsheimer, 1993).

# 8.2 Feed-forward networks with a linear output layer 

A similar example is the standard feed-forward network where the final output layer is linear. This situation is given by Figure 23 if we change the deterministic functions for $m_{1}$ and $m_{2}$ to be linear instead of sigmoidal. In this case Lemma 5.1 identifies that when the weight vectors $w_{3}, w_{4}$, and $w_{5}$ are assumed given, the distribution is in the exponential family. Thus the simplification to Figure 34 is possible using the standard sufficient statistics for multivariate linear regression. Algorithmically, this implies that given values for the internal weight vectors $w_{3}, w_{4}$, and $w_{5}$, and assuming a conjugate prior holds for the output weight vectors $w_{1}$ and $w_{2}$, the posterior distribution for the output weight vectors $w_{1}$ and $w_{2}$, and their means and variances, can be found in closed form. The evidence for $w_{1}$ and $w_{2}$ given $w_{3}, w_{4}$ and $w_{5}, p\left(y_{*}\left|x_{1, *}, \ldots, x_{n, *}, w_{3}, w_{4}, w_{5}, M\right)\right.$, can also be computed using the exact method of Lemma 6.4, so therefore the posterior for $w_{3}, w_{4}$, and $w_{5}$,

$$
p\left(w_{3}, w_{4}, w_{5} \mid y_{*}, x_{1, *}, \ldots, x_{n, *}, M\right) \propto p\left(w_{3}, w_{4}, w_{5} \mid M\right) p\left(y_{*}\left|x_{1, *}, \ldots, x_{n, *}, w_{3}, w_{4}, w_{5}, M\right)\right.
$$

can be computed in closed form up to a constant. This effectively cuts the problem into two pieces- $w_{3}, w_{4}$ and $w_{5}$ followed by $w_{1}$ and $w_{2}$ given $w_{3}, w_{4}$, and $w_{5}$-and provides a clean solution to the second piece.

![img-32.jpeg](img-32.jpeg)

Figure 34: Simplified learning of a feed-forward network with linear output

# 8.3 Bayesian networks with missing variables 

Class probability trees and discrete Bayesian networks can be learned efficiently by noticing that their basic form is exponential family (Buntine, 1991b, 1991a, 1991c; Cooper \& Herskovits, 1992; Spiegelhalter et al., 1993). Take, for instance, the family of models specified by the Bayesian network given in Figure 26. In this case, the local evidence corollary, Corollary 6.1.1, applies. The evidence for Bayesian networks generated from this graph is therefore a product over the nodes in the Bayesian network. If we change a Bayesian network by adding or removing an arc, the Bayes factor is therefore simply the local Bayes factor for the node, as mentioned in the incremental decomposition lemma, Lemma 6.3. Local search is then quite fast, and Gibbs sampling over the space of Bayesian networks is possible. A similar situation exists with trees (Buntine, 1991b). The same results apply to any Bayesian network with exponential family distributions at each node, such as Gaussian or Poisson. Results for Gaussians are presented, for instance, in (Geiger \& Heckerman, 1994).

This local search approach is a MAP approach because it searches for the network structure maximizing posterior probability. More accurate approximation can be done by generating a Markov chain of Bayesian networks from the search space of Bayesian networks. Because the Bayes factors are readily computed in this case, Gibbs sampling or Markov chain Monte Carlo schemes can be used. The scheme given below is the Metropolis algorithm (Ripley, 1987). This only looks at single neighbors until a successor is found. This is done be repeating the following steps:

1. For the initial Bayesian network $G$, randomly select a neighboring Bayesian network $G^{\prime}$ differing only by an arc.

2. Compute Bayes-factor $\left(G^{\prime}, G\right)$ by making the decompositions described in Theorem 6.1, doing a local computation as described in Lemma 6.3, and using the Bayes factors computed with Lemma 6.4.
3. Accept the new Bayesian network $G^{\prime}$ with probability given by:

$$
\min \left(1, \text { Bayes-factor }\left(G^{\prime}, G\right) \frac{p\left(G^{\prime}\right)}{p(G)}\right)
$$

If accepted, assign $G^{\prime}$ to $G$, otherwise $G$ remains unchanged.
A local maxima Bayesian network could be found concurrently, however, this scheme generates a set of Bayesian networks appropriate for model averaging and expert evaluation of the space of potential Bayesian networks. Of course, initialization might search for local maxima to use as a reference. This sampling scheme was illustrated in the context of averaging in Figure 12.

This scheme is readily adapted to learn the structure and parameters of a Bayesian network with missing or latent variables. For the Metropolis algorithm, add Step 4, which resamples the missing data and latent variables.
4. For the current complete data and Bayesian network $G$, compute the predictive distribution for the missing data or latent variables. Use this to resample the missing data or latent variables to construct a new set of complete data (for subsequent use in computing Bayes factors).

# 9. Conclusion 

The marriage of learning and graphical models presented here provides a framework for understanding learning. It also provides a framework for developing a learning or data analysis toolkit, or more ambitiously, a software generator for learning algorithms. Such a toolkit combines two important components: a language for representing a learning problem together with techniques for generating a matching algorithm. While a working toolbox is not demonstrated, a blueprint is provided to show how it could be constructed, and the construction of some well-known learning algorithms has been demonstrated. Table 1 lists some standard problems, the derivation of algorithms using the operations from the previous chapters, and where in the text they are considered. The notion of a learning toolkit is not new, and can be seen in the BUGS system by Thomas, Spiegelhalter, and Gilks (1992)(Gilks et al., 1993b), in the work of Cohen (1992) for inductive logic programming, and emerging in software for handling generalized linear models (McCullagh \& Nelder, 1989; Becker, Chambers, \& Wilks, 1988).

There is an important role for a data analysis toolkit. Every problem has its own quirks and requirements. Knowledge discovery, for instance, can vary in many ways depending on the user-defined notion of interestingness. Learning is often an embedded task in a larger system. So while there are some easy applications of learning, generally learning applications require special purpose development of learning systems or related support software. Sometimes, this can be achieved by patching together some existing techniques or by decomposing a problem into subproblems. Nevertheless, the decomposition and patching


Table 1: Derivation of learning algorithms
of learning algorithms with inference and decision making can be formalized and understood within graphical models. In some ways the S system plays the role of a toolkit (Chambers \& Hastie, 1992). It provides a system for prototyping learning algorithms, includes the ability to handle generalized linear models, does automatic differentiation of expressions, and includes many statistical and mathematical functions useful as primitives. The language of graphical models is best viewed as an additional layer on top of this kind of system. Note, also, that it is impractical to assume that a software generator could create algorithms competitive with current finely tuned algorithms, for instance, for hidden Markov models. However, a software toolkit for learning could be used to prototype an algorithm that could later be refined by hand.

The combination of learning and graphical models shares some of the superior aspects of each of the different learning fields. Consider the philosophy of neural networks. These nonparametric systems are composed of simple computational components, usually readily parallelizable, and often nonlinear. The components can be pieced together to tailor systems for specific applications. Graphical models for learning have these same features. Graphical models also have the expressibility of probabilistic knowledge representations that were developed in artificial intelligence to be used in knowledge acquisition contexts. They therefore form an important basis of knowledge refinement. Finally, graphical models for learning allow the powerful tools of statistics to be applied to the problem.

Once learning problems are specified in the common language of graphical models, their associated learning algorithms, their derivation, and their interrelationships can be explored. This allows commonalities between seemingly diverse pairs of algorithms-such as k-means clustering versus approximate methods for learning hidden Markov models, learning decision trees versus learning Bayesian networks (Buntine, 1991a), and Gibbs sampling versus the expectation maximization algorithm in Section 7.4-to be understood as variations of one another. The framework is important as an educational tool.

# Appendix A. Proofs of Lemmas and Theorems 

## A. 1 Proof of Theorem 2.1

A useful property of independence is that $A$ is independent of $B$ given $C$ if and only if $p(A, B, C)=f(A, C) g(B, C)$ for some functions $f$ and $g$. The only if result follows directly from this property. The proof of the if result makes use of the following simple lemma. If $A$ is independent of $B$ given $X-A-B$, and $p(X)=\prod_{i} f_{i}\left(X_{i}\right)$ for some functions $f_{i}>0$ and variable sets $X_{i} \subseteq X$, then:

$$
p(X)=\prod_{i} g_{i}\left(X_{i}-B\right) h_{i}\left(X_{i}-A\right)
$$

for some functions $g_{i}, h_{i}>0$. Notice that it is known $p(X)=g(X-B) h(X-A)$ for some functions $g$ and $h$ by independence. Instantiate the variables in $B$ to some value $b$. Then:

$$
g(X-B) h(X-A, B=b)=\prod_{i} f_{i}\left(X_{i}, B=b\right)
$$

Similarly, instantiate $A$ to $a$, then:

$$
g(X-B, A=a) h(X-A)=\prod_{i} f_{i}\left(X_{i}, A=a\right)
$$

Multiplying both sides of the two equalities together, and substitute in

$$
g(X-B, A=a) h(X-A, B=b)=p(X, A=a, B=b)=\prod_{i} f_{i}\left(X_{i}, A=a, B=b\right)
$$

Get:

$$
p(X) \prod_{i} f_{i}\left(X_{i}, A=a, B=b\right)=\prod_{i} f_{i}\left(X_{i}, B=b\right) \prod_{i} f_{i}\left(X_{i}, A=a\right)
$$

This is defined for all $X$ since the domain is a cross product. The lemma holds because all functions are strictly positive if

$$
g_{i}\left(X_{i}-B\right)=\frac{f_{i}\left(X_{i}, B=b\right)}{f_{i}\left(X_{i}, B=b, A=a\right)}
$$

and

$$
h_{i}\left(X_{i}-A\right)=f_{i}\left(X_{i}, A=a\right)
$$

The final proof of the if result follows by applying Equation (27) repeatedly. Suppose the variables in $X$ are $x_{1}, \ldots, x_{v}$. Now $p(X)=f_{0}(X)$ for some strictly positive function $f_{0}$. Therefore:

$$
p(X)=g_{0}\left(X-\left\{x_{1}\right\}\right) h_{0}\left(\left\{x_{1}\right\} \cup \text { neighbors }(x)\right)
$$

Denote $A_{i, 0}=X-\left\{x_{i}\right\}$ and $A_{i, 1}=\left\{x_{i}\right\} \cup$ neighbors $\left(x_{i}\right)$. Repeating the application of Equation (27) for each variable yields:

$$
p(X)=\prod_{i_{1}=0,1} \ldots \prod_{i_{v}=0,1} g_{i_{1}, \ldots, i_{v}}\left(X-\bigcup_{j=1, \ldots, v} A_{j, i_{j}}\right)
$$

for strictly positive functions $g_{i_{1}, \ldots, i_{v}}$. Now, consider these functions. It is only necessary to keep the function $g_{i_{1}, \ldots, i_{v}}$ if the set $X-\bigcup_{j=1, \ldots, v} A_{j, i_{j}}$ is maximal: it is not contained in any such set. Equivalently, keep the function $g_{i_{1}, \ldots, i_{v}}$ if the set $\bigcup_{j=1, \ldots, v} A_{j, i_{j}}$ is minimal. The minimal such sets are the set of cliques on the undirected graph. The result follows.

# A. 2 Proof of Theorem 6.1 

It takes $O\left(|X|^{2}\right)$ operations to remove the deterministic nodes from a graph using Lemma 6.1. These nodes can be removed from the graph and then reinserted at the end. Hereafter, assume the graph contains no deterministic nodes. Also, denote the unknown variables in a set $Y$ by unknown $(Y)=Y-\operatorname{known}(Y)$. Then, without loss of generality, assume that $X_{i}$ contains all known variables in the Markov blanket of unknown $\left(X_{i}\right)$.

Showing the independence model is equivalent amounts to showing for $i=1, \ldots, P$ that unknown $\left(X_{i}\right)$ is independent of $\bigcup_{j \neq i}$ unknown $\left(X_{j}\right)$ given $\operatorname{known}(X)$. To test independence using the method of Frydenberg (1990), each plate must be expanded (that is, duplicate it the right number of times), moralize the graph, removing the given nodes, and then test for separability. The Markov blanket for each node in this expanded graph corresponds to those nodes directly connected in the moralized expanded graph. Suppose we have the finest unique partition unknown $\left(X_{i}\right)$ of the unknown nodes. $X_{i}$ 's are then reconstructed by adding known variables in the Markov blankets for variables in unknown $\left(X_{i}\right)$. Suppose $V$ is an unknown variable in a plate, and $V_{j}$ are its instances once the plate is expanded. Now, by symmetry, every $V_{j}$ is either in the same element of the finest partition, or they are all in separate elements. If $V_{j}$ has a certain unknown variable in its Markov boundary outside the plate, then so must $V_{k}$ for $k \neq j$ by symmetry. Therefore $V_{j}$ and $V_{k}$ are in the same element of the partition. Hence by contradiction, if $V_{j}$ is in a separate element, that element occurs wholly within the plate boundaries. Therefore, this finest partition can be represented using plates, and the finest partition identified from the graph ignoring plates. The operation of finding the finest separated sets in a graph is quadratic in the size of the graph, hence the $O\left(|X|^{2}\right)$ complexity.

Assume the condition holds and consider Equation (23). Let cliques $(\tau)$ denote the subsets of variables in $\tau \cup$ parents $(\tau)$ that form cliques in the graph formed by restricting $G$ to $\tau \cup$ parents $(\tau)$ and placing an undirected arc between all parents. Let $\tau(X)$ be the set of chain components in $X$. From Frydenberg (1990), we have:

$$
p(X \mid M)=\prod_{\tau \in \tau(X) \in \operatorname{ind}(\tau)} \prod_{C \in \operatorname{cliques}(\tau)} g_{C}\left(C_{i}\right)
$$

Furthermore, if $u \in X_{i}$ is not known, then the variables in $u$ 's Markov blanket will occur in $X_{i}$, and therefore, if $u \in C$ for some clique $C$, then $C \subseteq X_{i}$. Therefore cliques containing an unknown variable can be partitioned according to which subgraph they belong in. Let:

$$
\text { cliques }_{j}^{\prime}=\left\{C: C \in \operatorname{cliques}(\tau(X)), \operatorname{unknown}\left(X_{j}\right) \cap C \neq \emptyset\right\}
$$

and add to this any remaining cliques wholly contained in the set so far:

$$
\text { cliques }_{j}=\text { cliques }_{j}^{\prime} \cup\left\{C: C \in \operatorname{cliques}(\tau(X)), C \subseteq \bigcup_{C^{\prime} \in \text { cliques }_{j}^{\prime}} C^{\prime}\right\}
$$

Call any remaining cliques cliques $_{0}$. Therefore:

$$
p(X \mid M)=\prod_{j=0}^{P} \prod_{C \in \text { cliques }_{j}} \prod_{i \in \text { ind }(C)} g_{C}\left(C_{i}\right)
$$


Table 2: Distributions and their functional form

Results in:

$$
f_{j}\left(\operatorname{known}\left(X_{j, *}\right)\right)=\int_{\text {unknown }\left(X_{j}, *\right)} \prod_{C \in \text { cliques }_{j}} \prod_{i \in \operatorname{ind}(C)} g_{C}\left(C_{i}\right) \text { dunknown }\left(X_{j}, *\right)
$$

Furthermore, the potential functions on the cliques in $G_{i}$ are well defined as described.

# A. 3 Proof of Corollary 6.1.1 

If $X_{j}=\tau_{j} \cup$ ndparents $\left(\tau_{j}\right)$, then every clique in a chain component in $\tau_{j}$ will occur in cliques $_{j}$. Therefore:

$$
\begin{aligned}
\prod_{C \in \text { cliques }_{j}} \prod_{i \in \text { ind }(C)} g_{C}\left(C_{i}\right) & =\prod_{\tau \in \tau_{j}} p(\tau \mid \text { ndparents }(\tau)) \\
& =p\left(\tau_{j} \mid \text { ndparents }\left(\tau_{j}\right)\right)
\end{aligned}
$$

## A. 4 Proof of Lemma 6.3

Consider the definition of the Markov blanket. If a directed arc is added between the nodes, then the Markov blanket will only change for an unknown node $X$ if $U$ now enters the set of non-deterministic parents of the chain-components containing non-deterministic children of $X$. This will not effect the subsequent graph separability, however, because it will only subsequently add arcs between $U$, a given node, and other nodes.

## Appendix B. The exponential family

The exponential family of distributions was described in Definition 4.1. The common use of the exponential family exists because of Theorem 4.1. Table 2 gives a few exponential family distributions and their functional form. Further details and more extensive tables can be found in most Bayesian textbooks on probability distributions (DeGroot, 1970; Bernardo \& Smith, 1994). Table 3 gives some standard conjugate prior distributions for those in Table 2, and Table 4 gives their matching posteriors (DeGroot, 1970; Bernardo \& Smith,


Table 3: Distributions and their conjugate priors


Table 4: Distributions and matching conjugate posteriors


Table 5: Distributions and their evidence
1994). For the distributions in Table 2 with priors in Table 3, Table 5 gives their matching evidence derived using Lemma 6.4 and cancelling a few common terms.

In the case where the functions $w_{i}$ are full rank in $\theta$ (dimension of $\theta$ is $k$, same as $w$, and the Jacobian of $w$ with respect to $\theta$ is invertible, $\operatorname{det}\left(\frac{\mathrm{d} w(\theta)}{\mathrm{d} \theta}\right) \neq 0$ ), then various moments of the distribution can be easily found:

$$
\mathcal{E}_{x \mid y, \theta}(t(x, y))=\left(\frac{\mathrm{d} w(\theta)}{\mathrm{d} \theta}\right)^{-1} \frac{\mathrm{~d} Z(\theta)}{\mathrm{d} \theta}
$$

The vector function $w(\theta)$ now has an inverse and it is referred to as the link function (McCullagh \& Nelder, 1989). This yields:

$$
\mathcal{E}_{x \mid y, \theta}\left(\exp \left(\sum_{i=1}^{k} \phi_{i} t_{i}(x, y)\right)\right)=\frac{Z\left(w^{-1}(\phi+w(\theta))\right)}{Z(\theta)}
$$

These are important because if the normalization constant $Z$ can be found in closed form, then it can be differentiated and divided, for instance, symbolically, to construct formula for various moments of the distribution such as $\mathcal{E}_{x \mid \theta}\left(t_{i}(x)\right)$ and $\mathcal{E}_{x \mid \theta}\left(t_{i}(x) t_{j}(x)\right)$. Furthermore, Equation (28) implies that derivatives of the normalization constant, $\mathrm{d} Z(\theta) / \mathrm{d} \theta$, can be found by estimating moments of the sufficient statistics (for instance, by Markov chain Monte Carlo methods).

# Acknowledgements 

The general program presented here is shared by many, including Peter Cheeseman, who encouraged this development from its inception. These ideas were presented in formative stages at Snowbird 1993 (Neural Networks for Computing), April 1993, and to the Bayesian Analysis in Expert Systems (BAIES) group in Pavia, Italy, June 1993. Feedback from that group helped further develop these ideas. Graduate students at Stanford and Berkeley have also received various incarnations of this ideas. Thanks also to George John, Ronny Kohavi, Scott Schmidler, Scott Roy, Padhraic Smyth, and Peter Cheeseman for their feedback on drafts, and to the JAIR reviewers. Brian Williams pointed out the extension of the decomposition theorems to the deterministic case. Brian Ripley reminded me of the extensive features of S .
