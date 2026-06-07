# Probabilistic Logic Methods and Some Applications to Biology and Medicine 

NIKITA A. SAKHANENKO ${ }^{1}$ and DAVID J. GALAS ${ }^{1,2}$


#### Abstract

For the computational analysis of biological problems-analyzing data, inferring networks and complex models, and estimating model parameters-it is common to use a range of methods based on probabilistic logic constructions, sometimes collectively called machine learning methods. Probabilistic modeling methods such as Bayesian Networks (BN) fall into this class, as do Hierarchical Bayesian Networks (HBN), Probabilistic Boolean Networks (PBN), Hidden Markov Models (HMM), and Markov Logic Networks (MLN). In this review, we describe the most general of these (MLN), and show how the above-mentioned methods are related to MLN and one another by the imposition of constraints and restrictions. This approach allows us to illustrate a broad landscape of constructions and methods, and describe some of the attendant strengths, weaknesses, and constraints of many of these methods. We then provide some examples of their applications to problems in biology and medicine, with an emphasis on genetics. The key concepts needed to picture this landscape of methods are the ideas of probabilistic graphical models, the structures of the graphs, and the scope of the logical language repertoire used (from First-Order Logic [FOL] to Boolean logic.) These concepts are interlinked and together define the nature of each of the probabilistic logic methods. Finally, we discuss the initial applications of MLN to genetics, show the relationship to less general methods like BN, and then mention several examples where such methods could be effective in new applications to specific biological and medical problems.


Key words: Bayesian networks, first-order logic, hierarchical Bayesian networks, machine learning, Markov logic networks, probabilistic Boolean networks, probabilistic graphical models, propositional logic.

## 1. INTRODUCTION

LOGIC AND PROBABILISTIC GRAPHICAL MODELS ARE NATURAL TOOLS OF COMPUTING and have been studied and used in computer science for many years. Some of these methods have emerged in recent years as promising approaches to a range of problems in artificial intelligence. In biology and medicine, where many of the computational problems involve data analysis and the inference of underlying complex models, simple forms of these methods, such as Hidden Markov Models (HMM), and simple forms of Bayesian Networks

[^0]
[^0]:    ${ }^{1}$ The Institute for Systems Biology, Seattle, Washington.
    ${ }^{2}$ Luxembourg Centre for Systems Biomedicine, University of Luxembourg, Esch-sur-Alzette, Luxembourg.

(BN), have become more commonly used in recent years (Baldi and Brunak, 2001). There is now a wide range of these methods that have been usefully applied to biological and medical problems, but it is often difficult to see in the reports of successful applications in the literature how they are related to one another. In this review, we attempt to address this difficulty and elucidate some of the key relationships, not specifically for the experts in the field, but more for the computational biologists that are grappling with the realities and complexities of current problems in systems biology, genetics and their applications to modern medicine. This review is not a comprehensive survey of methods, nor of the specific techniques and implementations in the literature, but rather is focused on providing a map of some of the key concepts that we hope will allow computational biologists to see the relationships, contrasts, and overlaps among widely used methods. Even more importantly, in our view, we hope to point out where new applications of probabilistic logic methods may provide powerful new approaches to the sometimes dauntingly complex problems of understanding biological systems. Our plan for this review is to begin with the most general combination of logic and probability, and illustrate how simplifying restrictions and constraints lead to more familiar methods, in order to elucidate the key relationships, and to indicate where some power is lost and where efficiency is gained. There are several relevant logical systems and several different forms, and representations, of probability distributions. These are briefly summarized below.

First-Order Logic (FOL) is a very general formal logic, and represents a more powerful tool for expression of logical relationship than propositional logic (Ershov and Palyutin, 1986). Using propositional logic, we are not able to express assertions about classes of objects or events. FOL is considerably richer than propositional logic and allows just these expressions. FOL allows the propositional symbols to have arguments that range over elements of sets, which allows us to make assertions about the sets or classes. FOL can also deal with recursive statements, while propositional logic cannot.

Probability distributions can involve a wide range of simple and complex dependencies and are often represented in graphical form in statistics, where the independencies of the variables represented as nodes are encoded in the edges. In this review, we illustrate the key relationships by beginning with the most general and proceeding to more restrictive, and constrained representations. While there are some significant differences in the graphical representations used in various methods the logical components of the probabilistic logic are where most of the restrictions occur.

Markov Logic Networks (MLN) represent a new and general approach to modeling based on full FOL and Markov Random Fields (MRF) (Richardson and Domingos, 2006). In addition to high representational power of FOL, MRFs provide a very compact way of representing probability distributions and are very useful for modeling and reasoning in noisy, uncertain environments. For physicists, MRFs are probably most familiar as the mathematical representation of Ising models, which are simplified, statistical models of the interaction of arrays of magnetic spins (Kindermann and Snell, 1980). MLNs thus combine (and generalize) FOL and MRFs to gain most of the advantages of both the logic and probabilistic modeling worlds. Among the advantages of MLN are the ability to handle arbitrary classes of variables, recursive statements, and the ability to construct multiple templates for MRFs.

Using MLN can allow us to perform sophisticated probabilistic modeling while directly incorporating biological knowledge, particularly including partial knowledge, into the models, which is one of our major motivations for developing this general approach. We think that this capability is fundamentally important for the development of system level analysis and modeling of biological systems, including metabolic, regulatory, and genetic aspects of these systems.

It is useful here to presage, or summarize, the conclusions of the later sections here by giving a compact overview of the key relationships that put the MLN and other methods into some context. We use the examples elaborated later in this article to illustrate this overview. Since the most widely used probabilistic graphical models in computational biology are various versions of BN, it is specifically useful to note the key differences between these and MLN. The major differences are these three:

1. The probability distributions that can be represented in MLN are those of MRF, which are more general than those of BN.
2. Relationships and probabilities can be assigned to classes of elements and/or events in MLN, whereas in BN probabilities are assigned to individual elements or events.
3. The representation of the logical relationships in MLN is much more compact than in BN (for those that can be expressed in BN), particularly for more complex models.

These differences will be illustrated and discussed in later sections. A fourth difference is that MLNs are much more computationally intensive to implement, which can be an important practical limitation.

Now we turn to a specific example of model selection in genetic analysis. We have applied MLN by using a search method that allows us to solve various model selection problems with different biological knowledge constraints naturally embedded in them. In a previous article, we used MLN to select models for the influence of the genotype (specific sets of markers, indicating gene variants) on the phenotype (e.g., properties of the organism as expressed in measurements: size, color, shape, gene expression levels). We first used a single-marker model iteratively that focused on relationships between genetic markers and a given phenotype (Sakhanenko and Galas, 2010). Every marker associated with a gene selected in the model had a specific influence on the phenotype, even when considered alone. The model is asked to predict the phenotype given the genotype of a single organism, and the markers were iteratively selected to improve the prediction. Later, in this review, we discuss a natural extension of this application that uses a pair-wise gene model that explicitly represents relationships between a phenotype and pair-wise interacting genes. The models discussed here to illustrate the approach, while complex in implementation, are still rather simple genetic models, and the full power of MLNs will come with the natural extension to much more complex models. This is one of the major points we would like to emphasize-that much more powerful applications are to come, but probabilistic logic represents a "language" for expression and calculation with such complex models.

To illustrate the method in a simple form, a single-marker model encodes an influence of a set of genetic markers on a phenotype as an aggregation of influences of individual markers. When conditioned on the alleles of the markers (predicting the phenotype values given the genotype data), modeling using a singlemarker model can be seen (as we specifically show in a later section) as performing a logistic regression of the marker alleles on the phenotype values. Note however that the single-marker model does not make the assumption that the data is identically, independently distributed (iid) as opposed to the case of a true logistic regression. At the first iteration of the search method (see Algorithm 1 of Section 4), when each model is based on only one marker, the corresponding logistic regression has two predictors (assuming a genetic marker can have two possible alleles). For the following iterations, as we add more markers to the predictive markers set, the corresponding logistic regression is expanded to include more predictors (four, six, and so on). It is important to note however that the MLN description of the models at different levels of iteration does not change; what changes is a set of possible values of the MLN variables that correspond to the predictors of the logistic regression. The method is then a systematic application of a template specified by MLN to different subsets of the data. This template is essentially a model. We can use this template then for adding biological domain knowledge into the probabilistic search-information about how the various parts of a biological system interact or influence one another. For example, by using pair-wise models, we expand the template to specifically allow for pair-wise gene interactions.

A pair-wise model encodes an aggregation of joint influences of pairs of markers together with their interactions on a phenotype. This model is an MLN template that explicitly takes into account possible gene interactions. As with the single-marker model, when predicting phenotype values from genotype values, the pair-wise model can also be seen as a logistic regression. The difference between the singlemarker and the pair-wise models becomes apparent when we look closely at their corresponding forms of regression. A logistic regression derived from the pair-wise model contains all the terms of the regression of the single-marker model given the same set of markers, plus the terms that correspond to possible interactions in each pair of the markers. If the markers have no gene interactions, then a corresponding pairwise model reduces to a single-marker model. On the other hand, if the markers do interact, then the pairwise model can encompass that effect when predicting the phenotype, even if the markers individually have little influence on the phenotype and cannot therefore be detected as contributing in the single gene model. This is why the pair-wise models have been successful at capturing synthetic gene interactions that confer a phenotype only when both specific alleles of a pair of genes are present. However, if two genes have an effect on phenotype individually, but also have a significant interaction, the interaction may be detected by the single gene template as a non-additive effect of the two genes on prediction accuracy (because of the induced correlation or dependence). The pair-wise model, on the other hand can detect significant interaction effects even if the single gene effects are in the noise and not detectable. The pair-wise model, while more complex than the single gene model, is clearly just the tip of the iceberg of the kinds of complex models that likely underlie real complex genetic traits.

MLNs are powerful tools for systems genetics since they allow us to incorporate explicit biological knowledge into genome-wide studies. For example, when using the pair-wise model, we can control the interaction terms of the corresponding logistic regression through specific constraints in the logical relationships based on our biological knowledge. We could also define specific constraints concerning the gene interactions in the model. Moreover, the logic component of MLNs makes it possible to represent large probabilistic models (a logistic regression with many interaction terms, for example) in a highly compact way. Using MLNs as model templates in genetic studies is a huge step beyond Genome-Wide Association Studies (GWAS) and moves us substantially toward true systems genetics.

It is important to compare MLNs to other established and related modeling methods in computational biology. Since MLNs are based on MRFs and FOL, it is natural that MLNs represent a generalization of both of these (Richardson and Domingos, 2006). In the most extreme case, we can reduce MLNs simply to FOL by setting all the weights in an MLN to an arbitrarily large number. Conversely, we can also reduce MLNs to MRFs by assigning an MLN formula for each clique of an MRF and then using the cliques potential as the weight of that formula. As with MRFs, we can also express any probability distribution represented by a BN using MLNs. Consequently, other kinds of BNs, such as Hierarchical BNs (HBN) and Dynamical BNs (DBN), can also be represented in the MLN framework. We note, for example, that an HMM is actually a particularly simple form of a DBN.

To briefly summarize the relationships between these methods, we present a simplified table of properties here (Table 1). These elements will be described and discussed in the body of the review, and though some of the entries in this table may be less than clear at this point, the table represents a rough map of the methods review and of our intent. We revisit the summary of relationships more explicitly in a later section (Fig. 3).

To further explore and analyze the relationship between MLNs and other methods, we will now consider in more detail the probabilistic, logic, and structural components of each method and indicate where the methods differ in how constrained their components are. The MLNs have the least constrained logic component, and so we will use them as the general, master method. Next, in Section 2, we set out the notation carefully, and we briefly introduce FOL, MRFs, and MLNs with a little more rigor. In Section 3, we show explicitly the relationship between MLNs and BNs, and then discuss how MLNs fit into a broader picture of probabilistic logic methods. To make it explicitly clear, we illustrate a specific MLN representation of a BN in an example in Section 3. In Section 4, we illustrate the use of MLN-based methods applied thus far to genetics. These examples show two types of models, single-marker and pair-wise models, which are analyzed in Sections 5 and 6, respectively. Finally, we conclude by describing some future, possible applications of MLNs to other biological problems in Section 7.

Table 1. Brief Summary of Some of the Key Elements of Probabilistic Logic Methods


# 2. PRELIMINARIES 

We describe here all the necessary preliminary information, definitions, and notation for logic, MRFs, and networks.

### 2.1. Logic

Among various systems of logic, the most general one we will use here is FOL. On the other hand, propositional logic has the simplest semantics, but many concepts of propositional logic generalize to FOL (Ershov and Palyutin, 1986).

In propositional logic, there are atomic (simple) assertions, consisting of propositional letters, and compound assertions, composed from the atomic assertions and the logical connectives, and $(\wedge)$, or $(\vee)$, not $(\neg)$, implication $(\Rightarrow)$, and equivalence $(\Leftrightarrow)$. An interpretation in propositional logic is a mapping that assigns a truth value (True or False) to every propositional letter. Once the atomic assertions in a proposition have received an interpretation, we can compute the truth value of the proposition. We can do this since all propositional formulas are inductively constructed from the atomic assertions, and the logical connectives are interpreted with the truth table given in Table 2.

In propositional logic, propositions that are equivalent irrespective of their interpretations form an equivalence class. A structure based on these equivalence classes is called Boolean algebra.

Using propositional logic, we are not able to express assertions about elements of structures. FOL is considerably richer than propositional logic and allows these expressions. FOL allows the propositional symbols to have arguments that range over elements of different structures, which allows us to make assertions about the sets of elements of structures.

In FOL, there are atomic formulas, consisting of predicates applied to logical terms. A term is an entity inductively constructed from variables and functions and has many levels of complexity. Note that the simplest term is a value of a variable, called a constant, that can be seen as a function that takes no arguments, or has the same value irrespective of its arguments. Note also that a simplest atomic formula is a predicate that takes no arguments, which is similar to a propositional letter in propositional logic. In FOL, there are formulas, composed inductively from the atomic formulas, the logical connectives, $\wedge, \vee, \neg, \Rightarrow$, $\Leftrightarrow$ (as in propositional logic), and the quantifiers, universal ( $\forall$, the usual mathematical symbol for "each and every") and existential ( $\exists$, the usual mathematical symbol for "there exists"). In order to assign meaning to the symbols in FOL, we first must define a domain (a universe), which is the domain of the logical variables. An instantiation of a first-order formula is, then, a replacement of variables of the formula with logical terms. Note that the most common instantiation replaces the variables with the values (constants) from their domain. An interpretation in FOL is a mapping that assigns a truth value to every atomic formula for every instantiation of variables. An interpretation is then recursively defined on complex formulas. Note that, given an instantiation, formulas composed from atomic formulas and logical connectives, are interpreted just as in propositional logic. The interpretation of quantified formulas is as follows:

$$
\begin{aligned}
& (\forall x A(x)) \text { is true iff } A(d) \text { is true for any } d \in \text { Domain } \\
& (\exists x A(x)) \text { is true iff } A(d) \text { is true for some } d \in \text { Domain }
\end{aligned}
$$

A possible world (a Herbrand interpretation) in FOL is an assignment of truth-values to all possible predicates whose variables are replaced with every possible combination of values. For example, one

Table 2. Truth Table Defining the Interpretation of Logical Connectives of Propositional Logic


Table 3. Possible World (in FOL) for the Program (13)


Here predicates Phenotype $\left(s_{i}, t_{j}\right)$ and Allele $\left(s_{i}, m_{k}, v_{l}\right)$ encode two facts (two data points) that $t_{j}$ is a phenotype value of strain $s_{i}$ and that $v_{l}$ is an allele of marker $m_{k}$ for strain $s_{i}$.
possible world for the program (13) can be given in Table 3. Note that various model restrictions can be applied by reducing the set of all possible predicates and a set of possible values for the variables.

# 2.2. Probabilistic graphical models 

A BN is a probabilistic graphical model that represents random variables and their probabilistic dependencies with a directed, acyclic graph (Pearl, 1988; Koller and Friedman, 2009). A BN is represented by a directed, acyclic graph where each vertex represents a random variable and each edge represents a conditional dependence between two vertices. Since the graph is directed, for every edge we distinguish a parent, a vertex from which the edge originates, and a child, a vertex to which the edge goes. Consequently, every vertex is assigned a conditional probability, in a table defining the probability of a variable given every possible set of values of the parents of the vertex (corresponding to all edges going in the vertex). We could say "conditioned on" those values. One powerful feature of BNs is their ability to graphically encode conditional dependence between random variables: a variable is conditionally independent from any of non-descendent variables, given the values of its parents. This feature allows BNs to specify probability distributions in a compact and efficient way, but only those distributions that fit these constraints.

Consider a set of random variables $\mathbf{V}=\left\{V_{1}, \ldots, V_{N}\right\}$ and consider a directed, acyclic graph $G=(\mathbf{V}, \mathbf{E})$ based on the set $\mathbf{V}$ (thus, every $V_{i}$ will be referred to as either a variable or a vertex). Given a parameter set $\Theta=\left\{\Theta_{1}, \ldots, \Theta_{N}\right\}$, where each $\Theta_{i}$ is a conditional probability distribution of $V_{i}$ given its parents, $\Theta_{i}=\operatorname{Pr}\left(V_{i} \mid\right.$ parents $\left.\left(V_{i}\right)\right)$, then $\langle\mathbf{V}, G, \Theta\rangle$ is a BN if a joint probability distribution on $\mathbf{V}$ can be factorized as

$$
\operatorname{Pr}(\mathbf{V})=\prod_{i=1}^{N} \Theta_{i}=\prod_{i=1}^{N} \operatorname{Pr}\left(V_{i} \mid \text { parents }\left(V_{i}\right)\right)
$$

Note that in many applications of BNs researchers give causal meaning to the edges of a network. In general, however, the directionality of edges does not imply causality. Note the significance of the factorization is related to the chain rule for conditional probabilities. The interpretation of this rule is the source of these incorrect causality arguments.

Consider here an example from a textbook (Luger, 2008). Suppose there is one event that can cause orange barrels to appear on the road, $B=$ true: a road construction, $C=$ true. There is also one event that can cause flashing lights to appear on the road, $L=$ true: an accident, $A=$ true. Suppose then that there are two events that can cause bad traffic, $T=$ true: either an accident or a road construction. This example can be modeled by a BN shown in Figure 1, whose parameters are given in the tables below. Note that all the variables are binary in this case.

The probabilistic independencies encoded by the BN in Figure 1 allows us to express a joint probability distribution in a compact way with a small number of parameters. Here, the rule is the probabilities of nodes not directly connected by edges are independent and can be multiplied:

$$
\operatorname{Pr}(C, A, B, T, L)=\operatorname{Pr}(C) \times \operatorname{Pr}(A) \times \operatorname{Pr}(B \mid C) \times \operatorname{Pr}(T \mid C, A) \times \operatorname{Pr}(L \mid A)
$$

MRFs are another kind of probabilistic graphical model, which is similar to BNs in how dependencies are represented (Kindermann and Snell, 1980; Pearl, 1988; Koller and Friedman, 2009). As opposed to BNs though, MRFs are defined on undirected graphs. Removing edge directionality eliminates the asymmetry between a parent vertex and a child vertex, which allows MRFs to represent cyclic dependencies that

FIG. 1. Structure of a road traffic Bayesian network. Here $B$ stands for orange barrels on the street, $C$ for a road construction, $T$-for traffic, $A$-for an accident, and $L$ for flashing lights.
![img-0.jpeg](img-0.jpeg)
cannot be represented by BNs. Note however that there are dependencies, such as induced dependencies, that can be represented by BNs, but not by MRFs. Thus, MRFs offer an alternative graphical semantics for probability distributions where graph separation of two vertices by a separating set implies conditional independence of the two vertices given the separating set, and we are able to make different conditional independence statements in MRFs than in BNs.

More formally, given three disjoint sets of vertices, $A, B, C$, in an undirected graph, the set $B$ separates $A$ from $C$ in the graph if every path from $A$ to $C$ contains at least one vertex from $B$. We now use the definition of graph separation to define an MRF. Consider a set of random variables $\mathbf{V}=\left\{V_{1}, \ldots, V_{N}\right\}$ and consider an undirected graph $G=(\mathbf{V}, \mathbf{E})$ based on the set $\mathbf{V}$. An MRF defined on $\mathbf{V}$ is a probability distribution such that there exists a $G$ with a condition that, for disjoint sets of vertices $A, B, C$, if $A$ and $C$ are separated by $B$, then vertices from $A$ are conditionally independent from vertices from $C$ given $B$. The conditional independence property of MRFs implies that if we have two vertices $V_{i}$ and $V_{j}$ that are not directly connected, then they are conditionally independent given all other vertices, i.e.,

$$
\begin{aligned}
& \operatorname{Pr}\left(V_{i}=v_{i}, V_{j}=v_{j} \mid \mathbf{V} \backslash\left\{V_{i}, V_{j}\right\}=\mathbf{v} \backslash\left\{v_{i}, v_{j}\right\}\right)= \\
& =\operatorname{Pr}\left(V_{i}=v_{i} \mid \mathbf{V} \backslash\left\{V_{i}, V_{j}\right\}=\mathbf{v} \backslash\left\{v_{i}, v_{j}\right\}\right) \operatorname{Pr}\left(V_{j}=v_{j} \mid \mathbf{V} \backslash\left\{V_{i}, V_{j}\right\}=\mathbf{v} \backslash\left\{v_{i}, v_{j}\right\}\right)
\end{aligned}
$$

Here, $V_{i}=v_{i}$ stands for an event that a variable $V_{i}$ takes on a value $v_{i}, \mathbf{V}=\mathbf{v}$ is shorthand for $V_{1}=v_{1}, \ldots, V_{N}=v_{N}$, and $\mathbf{V} \backslash\left\{V_{i}, V_{j}\right\}$ is a set $\mathbf{V}$ without vertices $V_{i}$ and $V_{j}$. Note also that two directly connected vertices are not conditionally independent given all other vertices. This can be used to factorize an MRF.

A clique $c$ of a graph $G$ is a subgraph such that all vertices of $c$ are fully connected. A Gibbs distribution defined on $G$ is

$$
\operatorname{Pr}(\mathbf{V}=\mathbf{v})=\frac{1}{Z} \prod_{c \in C l} \exp \left(-\phi_{c}\left(\mathbf{v}_{c}\right)\right)
$$

The so-called partition function $Z=\sum_{\mathbf{v}} \prod_{c \in C l} \exp \left(-\phi_{c}\left(\mathbf{v}_{c}\right)\right)$ normalizes the probability to ensure that $\sum_{\mathbf{v}} \operatorname{Pr}(\mathbf{V}=\mathbf{v})=1$. Here $C l$ is the set of all cliques of $G, \mathbf{v}_{c}$ is a restriction of a configuration of $\mathbf{v}$ to a clique $c$, and $\phi_{c}$ is a real-valued potential function assigned to a clique $c$. Given a Gibbs distribution on $G$,

$$
\begin{aligned}
& \operatorname{Pr}\left(V_{1}=v_{1} \mid \mathbf{V} \backslash\left\{V_{1}\right\}=\mathbf{v} \backslash\left\{v_{1}\right\}\right)=\frac{\operatorname{Pr}(\mathbf{V}=\mathbf{v})}{\operatorname{Pr}\left(\mathbf{V} \backslash\left\{V_{1}\right\}=\mathbf{v} \backslash\left\{v_{1}\right\}\right)} \\
& =\frac{\prod_{c \in C l} \exp \left(-\phi_{c}\left(v_{1}, v_{2}, \ldots, v_{N}\right)\right)}{\sum_{x} \prod_{c \in C l} \exp \left(-\phi_{c}\left(x, v_{2}, \ldots, v_{N}\right)\right)}=\frac{\prod_{\left\{c \in C l \mid V_{1} \in c\right\}} \exp \left(-\phi_{c}\left(v_{1}, v_{2}, \ldots, v_{N}\right)\right)}{\sum_{x} \prod_{\left\{c \in C l \mid V_{1} \in c\right\}} \exp \left(-\phi_{c}\left(x, v_{2}, \ldots, v_{N}\right)\right)}
\end{aligned}
$$

Note that although for convenience we write $\phi_{c}\left(V_{1}, \ldots, V_{N}\right)$, this potential function depends only on the vertices from the clique $c$, hence the right side of the derivation above depends only on the variables from the cliques containing $V_{1}$. Thus, the variable $V_{1}$ is conditionally dependent on only the variables form the same cliques it belongs to, which means that any Gibbs distribution is an MRF. On the other hand, the

Hammersley-Clifford theorem proves the converse, that every positive MRF corresponds to some Gibbs distribution.

Without loss of generality, we can represent an MRF conveniently as a log-linear model:

$$
\operatorname{Pr}(\mathbf{V}=\mathbf{v})=\frac{1}{Z} \exp \left(\sum_{i} w_{i} f_{i}(\mathbf{v})\right)
$$

where the $f_{i}$ are real-valued functions defining features of the MRF and $w_{i}$ are the real-valued weights of the MRF, that are the parameters of the model (Pietra et al., 1997). Features, that can be as simple as indicator functions representing the presence of some attributes, and can overlap in arbitrary ways providing representational flexibility.

# 2.3. Markov logic networks 

Because of their flexibility and the potential for representing complex relationships we have proposed using probabilistic logic methods for analyzing genetic data. From a set of related logic-based probabilistic methods, we chose the most general of these, MLNs, and have used the method to identify genetic loci that predict quantitative phenotypes (Sakhanenko and Galas, 2010).

MLNs merge MRFs with first-order logic (see Sections 2.1 and 2.2). Any strictly formal completely logic system (not including probabilities) is not suitable for applications where the data contain any uncertainty or noise. This is because a set of first-order formulas specifying a logical model is seen as a set of uncompromising requirements so that the model is either true or false by comparison with the data. In other words, models in FOL can only have probability values 1 or 0 , and since noise and uncertainty exist in all real data, no model is satisfied exactly and all must therefore be false. Since the data we wish to analyze are actually rich in information while not being exactly satisfied, this is not a useful point of view. MLNs relax this constraint by allowing a model with unsatisfied formulas with a lesser probability than 1 . The model with the smallest measure of unsatisfied formulas is the most probable, and will therefore represent the most successful extraction of knowledge of reality from the data.

An MLN is a set of first-order formulas, $F_{i}$, with assigned weights $w_{i}$. An MLN, together with the set of possible values of its variables, is then converted to an MRF as follows. For every predicate of the MLN whose variables are instantiated with every possible combination of values, we create one random variable in the MRF. The value of the random variable is either 1 or 0 corresponding to whether the instantiated predicate is true or false. Furthermore, for every possible instantiation of every formula, $F_{i}$, we construct one feature of the log-linear MRF (see Section 2.2) whose value is either 1 or 0 , depending on the truth value of the instantiated formula. The weight of the MRF feature is the weight $w_{i}$ assigned to the formula $F_{i}$ in the MLN. Taking the original definition (3) and replacing all the features corresponding to false formulas with 0 , we obtain the probability distribution represented by an instantiated MLN

$$
\operatorname{Pr}(\gamma)=\frac{1}{Z} \exp \left(\sum_{i} w_{i} n_{i}(\gamma)\right)
$$

where $n_{i}(\gamma)$ is a number of times the formula $F_{i}$ is instantiated to a true proposition in the state $\gamma$ (which corresponds to our data). Note that this probability distribution depends on the set of possible values of MLN variables. Therefore, MLNs can be seen as templates specifying classes of MRFs, similar to FOL specifying propositional formulas (see Section 2.1).

## 3. MARKOV LOGIC NETWORKS VERSUS BAYESIAN NETWORKS

### 3.1. Representing Baysian networks with conjunctive normal forms

Darwiche (2002) showed that a BN can be encoded in a Conjunctive Normal Form (CNF). A CNF $C$ is a conjunction of logical clauses $D_{i}: C=D_{1} \wedge \ldots \wedge D_{N}$, where a logical clause $D_{i}$ is a disjunction of either propositional variables or their negations (although a variable and its negation cannot be in the same clause): thus, $V_{i_{1}} \vee \neg V_{i_{2}} \vee \ldots \vee V_{i_{K}}$.

Following Darwiche's notation, we first establish the alphabet of propositional logic corresponding to the objects of a BN. We use two types of propositional symbols here, $\lambda_{v}$ and $\theta_{v \mid \mathbf{u}}$. A propositional symbol $\lambda_{v}$ for

each value $v$ of a random variable $V$ is interpreted as being true iff $V=v$. Note that $V$ can have more than two values. A propositional symbol $\theta_{v \mid \mathbf{u}}$, for each value $v$ of $V$ and for each combination of values $\mathbf{u}$ of a set $\mathbf{U}$ of parent vertices of $V$, is interpreted as being true iff there is an entry in a conditional probability table whose value is $\operatorname{Pr}(V=v \mid \mathbf{U}=\mathbf{u})$. These elements can be used to define precisely the logical structure inherent in BNs.

Consider then a BN $(\mathbf{V}, G, \Theta)$ and construct a CNF encoding this BN. First, for each network variable $V$, whose possible values are $v_{1}, \ldots, v_{K}$, we must include the following clauses (disjunctions): $\lambda_{v_{1}} \vee \ldots \vee \lambda_{v_{K}}$ and $\neg \lambda_{v_{i}} \vee \neg \lambda_{v_{j}}, i \neq j$. These clauses ensure that we use exactly one value for each random variable when evaluating our BN. In addition, for each entry of every conditional probability table of the BN, we must include in the CNF encoding the following clauses: $\lambda_{v} \wedge \lambda_{u_{1}} \wedge \ldots \wedge \lambda_{u_{M}} \Leftrightarrow \theta_{v \mid u_{1}, \ldots, u_{M}}$. These clauses ensure that, while evaluating the BN, the evidence $v, u_{1}, \ldots, u_{M}$ is necessary and sufficient for the BN to include a conditional probability table that contains $\operatorname{Pr}\left(v \mid u_{1}, \ldots, u_{M}\right)$.

Let us now construct a CNF encoding the road traffic BN from Figure 1. Our CNF is a conjunction of the disjunctions (clauses) shown in Table 4. The CNF models (possible truth assignments to the propositional variables) are in one-to-one correspondence with the instantiations of the network variables. Following Darwiche (2002), we can now apply weighted model counting to the CNF by assigning weights to all the letters and their negations: the weight of $\lambda_{v}, \neg \lambda_{v}$, and $\neg \theta_{v \mid \mathbf{u}}$ is 1 , and the weight of $\theta_{v \mid \mathbf{u}}$ is a value $\operatorname{Pr}(V=v \mid \mathbf{U}=\mathbf{u})$ from a corresponding CPT of the BN. Consequently, the probability of an event $e$ can be computed by weighted model counting of the CNF in conjunction with $e$.

For example, one of the $32\left(2^{|\mathbf{V}|}=2^{5}\right)$ possible CNF models correspond to the following instantiation of the random variables of the BN:

$$
C \leftarrow c_{2}, A \leftarrow a_{1}, B \leftarrow b_{1}, T \leftarrow t_{1}, L \leftarrow l_{2}
$$

In this model, the following propositional letters are true:

$$
\lambda_{c_{2}}, \lambda_{a_{1}}, \lambda_{b_{1}}, \lambda_{t_{1}}, \lambda_{l_{2}}, \theta_{c_{2}}, \theta_{a_{1}}, \theta_{b_{1} \mid c_{2}}, \theta_{t_{1} \mid c_{2}, a_{1}}, \theta_{l_{2} \mid a_{1}}
$$

Consequently, the weight of this model is a product of weights of these propositional letters, $0.6 \times 0.5 \times 0.2 \times 0.8 \times 0.01 \approx 0.0005$.

Thus, it is possible to represent and elucidate the logical structure of BNs using the CNF formulation. We can use this in turn to make the connection directly to MLNs.

# 3.2. Representing Bayesian networks with Markov logic networks 

The relationship between these two kinds of networks can best be elucidated by explicitly formulating one in terms of the other. Let us then encode a BN using MLNs by a construction similar to the CNF

Table 4. Set of Propositional Clauses Representing Each Element of Every Conditional Probability Table (CPT) of the BN Given in Figure 1


encoding in the previous section. Consider a set of random variables $\mathbf{V}=\left\{V_{1}, \ldots, V_{N}\right\}$ of a BN, where $V_{i} \in\left\{v_{i}^{1}, \ldots, v_{i}^{K}\right\}$. For each value $v_{i}^{l}$ of every variable $V_{i}$ we define a predicate $I V_{i}(x)$ such that $I V_{i}\left(v_{i}^{l}\right)=\operatorname{True} \Leftrightarrow V_{i}=v_{i}^{l}$. In BNs, each random variable can take on one and only one value, therefore we have to add the following formulas to the corresponding encoding MLN to specify this restriction:

$$
\begin{aligned}
& \exists v_{i}^{k} I V_{i}\left(v_{i}^{k}\right) \\
& \left(v_{i}^{k} \neq v_{i}^{l}\right) \wedge I V_{i}\left(v_{i}^{k}\right) \Rightarrow \neg I V\left(v_{i}^{l}\right)
\end{aligned}
$$

Note that formulas $(5,6)$ are "pure" FOL formulas (they are either true or false, meaning that their probabilistic weight is large without bound.)

Consider a set of parameters $\Theta=\left\{\Theta_{1}, \ldots, \Theta_{N}\right\}$ of the BN we are trying to encode, where each $\Theta_{i}$ is a conditional probability table assigned to a variable $V_{i}$. Assuming variable $V_{i}$ has $K$ parents in the BN, $V_{i_{1}}, \ldots, V_{i_{K}}$, then

$$
\Theta_{i} \equiv\left\{\operatorname{Pr}\left(V_{i}=v_{i} \mid V_{i_{1}}=v_{i_{1}}, \ldots, V_{i_{K}}=v_{i_{K}}\right), \forall v_{i}, v_{i_{1}}, \ldots, v_{i_{K}}\right\}
$$

For every BN parameter $\Theta_{i}$, the corresponding encoding MLN contains the following set of formulas

$$
\begin{aligned}
& \cdots \\
& w_{i} \quad I V_{i}\left(v_{i}\right) \wedge I V_{i_{1}}\left(v_{i_{1}}\right) \wedge \ldots \wedge I V_{i_{K}}\left(v_{i_{K}}\right) \\
& \cdots
\end{aligned}
$$

where the weight $w_{i}=\ln \left(\operatorname{Pr}\left(V_{i}=v_{i} \mid V_{i_{1}}=v_{i_{1}}, \ldots, V_{i_{K}}=v_{i_{K}}\right)\right)$. Note that the set (8) contains $N_{i} \times N_{i_{1}} \times \ldots \times N_{i_{K}}$ formulas, one formula per each element of the conditional probability table $\Theta_{i}$. Here $N_{i}$ and $N_{i_{1}}$ are the number of values variables $V_{i}$ and $V_{i_{k}}$ can take. If $\operatorname{Pr}\left(V_{i}=v_{i} \mid V_{i_{1}}=v_{i_{1}}, \ldots, V_{i_{K}}=v_{i_{K}}\right)=0$, then we use a "hard" encoding formula (whose weight is large without bound):

$$
\neg I V_{i}\left(v_{i}\right) \wedge \neg I V_{i_{1}}\left(v_{i_{1}}\right) \wedge \ldots \wedge \neg I V_{i_{K}}\left(v_{i_{K}}\right)
$$

As indicated in equation (4), an MLN represents the following distribution:

$$
\operatorname{Pr}\left(V_{1}=v_{1}, \ldots, V_{N}=v_{N}\right)=\frac{1}{Z} \exp \left(\sum_{\left\{F_{i}\right\}} w_{i} f_{i}\left(v_{1}, \ldots, v_{N}\right)\right)
$$

where the sum is taken over all formulas of the MLN. For each formula $F_{i}, w_{i}$ is its weight and $f_{i}$ is its characteristic function:

$$
f_{i}\left(v_{1}, \ldots, v_{N}\right)= \begin{cases}1, & F_{i}\left(V_{1} \leftarrow v_{1}, \ldots, V_{N} \leftarrow v_{N}\right)=\text { True } \\ 0, & \text { otherwise }\end{cases}
$$

Because of the way we constructed this MLN to encode a BN, equation (10) is a product of elements of the BN conditional probability tables corresponding to the BN instantiation $v_{1}, \ldots, v_{N}$. Note also that the partition function $Z$ defined as $Z=\sum_{v_{1}, \ldots, v_{N}} \exp \left(\sum_{\left\{F_{i}\right\}} w_{i} f_{i}\left(v_{1}, \ldots, v_{N}\right)\right)$ is 1 in this case, since values of random variables are mutually exclusive and all the formulas exhaust all the possibilities, thus we are essentially adding up the joint probabilities for all possible instantiations of the set of random variables.

Let us now illustrate with an example how a BN can be encoded by an MLN. Consider a toy BN in Figure 2.
![img-1.jpeg](img-1.jpeg)

FIG. 2. Structure of a toy Bayesian network. Here $A$ and $B$ stand for two events.

Let us define predicates $I A(A)$ and $I B(B)$ :

$$
\begin{aligned}
& I A\left(a_{i}\right)=\text { True } \Leftrightarrow A=a_{i} \\
& I B\left(b_{i}\right)=\text { True } \Leftrightarrow B=b_{i}
\end{aligned}
$$

The MLN encoding the toy BN in figure 2 consist of the following formulas

$$
\begin{array}{ll} 
& \exists x \quad I A(x) \\
& (x \neq y) \wedge I A(x) \Rightarrow \neg I A(y) \\
& \exists x \quad I B(x) \\
& (x \neq y) \wedge I B(x) \Rightarrow \neg I B(y) \\
\ln (0.6) & I A\left(a_{1}\right) \\
\ln (0.4) & I A\left(a_{2}\right) \\
\ln (0.9) & I A\left(a_{1}\right) \wedge I B\left(b_{1}\right) \\
\ln (0.1) & I A\left(a_{1}\right) \wedge I B\left(b_{2}\right) \\
\ln (0.2) & I A\left(a_{2}\right) \wedge I B\left(b_{1}\right) \\
\ln (0.8) & I A\left(a_{2}\right) \wedge I B\left(b_{2}\right)
\end{array}
$$

The top four first-order formulas of this MLN ensure that the arguments of $I A$ and $I B$ are mutually exclusive and exhaustive, whereas the remaining formulas represent every element of the corresponding probability tables of the BN. Note that the representational complexity of this MLN and the original BN is the same, since we are essentially mapping every element of the BN to a formula in MLN. Note that the description of the MLN is a bit lengthy, since we want to express exactly the same probability distribution represented by the BN. As a result, most of the formulas of this MLN are propositional (since they were manually instantiated) with explicitly specified weights. The representational power of MLN becomes clearer in this example if we decide to learn the weights from data, in which case the propositional part of the MLN can be replaced with a more concise

$$
\begin{aligned}
& I A(+x) \\
& I A(+x) \wedge I B(+y)
\end{aligned}
$$

Moreover, this structure does not change, if we change the domains of the logical variables $x$ and $y$. This demonstrates both that BNs can be represented as MLNs and that part of this representation consists of restrictions not necessary if we do not impose the BN constraints.

# 3.3. MLN in the landscape of probabilistic logic methods 

Markov logic networks are based on a combination of MRFs with FOL. An MLN can be seen as a template (Richardson and Domingos, 2006) for constructing MRFs according to specific logical patterns. MLNs are more general than MRFs, since we can represent any MRF by an MLN (in the worst case we can simply list all the cliques of the MRF using statements in propositional logic). On the other hand, an MLN can be seen as a relaxation of otherwise strict logical rules specified in FOL, allowing us to define the likelihood of logical models (Richardson and Domingos, 2006). MLNs can thus be seen also as a generalization of FOL: when the weights are equal and infinitely large, MLNs become FOL. Richardson and Domingos showed that, when all weights are equal and tend to infinity, an MLN represents a uniform distribution over all possible worlds satisfying the set of first-order formulas (Richardson and Domingos, 2006). Moreover, using the MLN with infinitely large weights, we can check whether or not a formula can be logically inferred from the set of MLN formulas by computing the probability that the formula is true and checking whether it is true or not.

Figure 3 schematically depicts the relationship between MLNs and other well-known probabilistic methods. Each method is classified here according to three major components: a probabilistic component, a logic component, and a graphical representation. Note that these components are not completely separate from each other, for example the graphical representation is intrinsically connected with the probabilistic dependency specified in the probabilistic component. On the other hand, using these three components allows us to illustrate the overall relationships between MLNs and other probabilistic methods. In particular, we can see how methods derive from others by imposing more constraints.

![img-2.jpeg](img-2.jpeg)

FIG. 3. The relationships between MLN and different probabilistic representations.

In Figure 3, we position MRFs and BNs on the same level, right under MLNs, since both are the most expressive methods among those based on propositional logic. MLNs generalize MRFs and BNs by using FOL. Note that BNs typically imply some (temporal) ordering: a true value of a variable may "cause" another variable to be true. Although MRFs imply no such ordering, MLNs use FOL to make such an implication (see previous section). Two well-known methods, HBNs and DBNs, are the specialized versions of BNs; therefore, we place them right under BNs in Figure 3. HBNs and DBNs are essentially BNs with additional structural constraints: an HBN is a directed hierarchical tree where some "sibling" vertices may be linked, and a DBN is a sequence of BNs, representing a systems snapshot, such as a systems state at a moment of time, interlinked in one direction, representing a series of events, such as a progression of time. MLNs, which can express BNs, are also able to represent HBNs and DBNs, whose structural constraints can be easily expressed in FOL. Another well-known class of probabilistic models, probabilistic boolean networks (PBN), deals with systems dynamics, similarly to DBNs. Moreover, a very close relationship between PBNs and DBNs was shown in Lahdesmaki et al. (2006). Thus, we place PBNs on the same level with DBNs and directly under MLNs, since Boolean logic, which PBNs are based on, is directly generalized by FOL.

# 4. THE APPLICATION OF MLNS TO GENETICS 

We have used MLNs to study the interactions of genetic loci in predicting phenotypes (Sakhanenko and Galas, 2010) and to capture the influence of these interconnected loci on phenotypes. We use a regressiontype MLN: given $N$ predictor variables $X_{i}$ (that could represent alleles of genetic markers), predict a value of an outcome variable $Y$ (that could represent a phenotype, for example). Algorithm 1 summarizes the method that handles a model selection problem of finding a model that captures best the probability distribution over the training data:

```
Algorithm 1: MLN-based predictor selection
foreach predictor variable \(X_{i}\) do
    repeat
        shuffle data;
        train and test \(M L N\left(X_{i}, K n o w n, Y\right)\);
        obtain a cross-validation score \(e\left(X_{i}\right)\);
    until the average score \(e\left(X_{i}\right)\) does not change;
if \(e\left(\bar{X}_{i}\right)\) is a max outlier then
    Known \(=\operatorname{Known} \bigcup\left\{X_{i}\right\}\);
    go to line 1 ;
```

The inner repeat-until loop trains and evaluates the same model on a reordered, or shuffled, data set: since MLN modeling is path-dependent, this loop reduces the effect of path-dependency on a prediction

score. The outer foreach loop traverses the set of all predictor variables (genetic markers) and computes how well each marker, together with a small set of known markers, predicts an outcome variable (a phenotype). Once all the markers in the given set are traversed and assigned a score, the most significantly predictive marker is selected and added to the set of known markers, prompting another iteration of the search procedure. The search stops when there are no markers left with significant predictive power. This heuristic search keeps the structure of MLN and the outcome variable $Y$ the same, but considers different subsets of predictor variables $X_{i}$ in order to find a model that best "explains" the variation of $Y$ (Sakhanenko and Galas, 2010). In the next sections, we present and compare two types of MLNs using Algorithm 1, single-marker models and pair-wise models. We also explain what it means for two markers to predict a phenotype together when using each of these models.

# 5. SINGLE-MARKER MODELS 

We have used MLNs as an underlying model representation in the method that detects genetic loci determining quantitative phenotypes (Sakhanenko and Galas, 2010). This method is an iterative procedure that scans the set of all possible genetic markers during every iteration and selects a marker that, in combination with other known predictors, has a significant predictive power of the phenotype. The selected marker is then added to the set of known predictors and the method continues to the next iteration.

The first iteration of the method is similar to GWAS in the following way. The method scans all the markers and finds those markers whose individual predictive power is high. However, our method is different from the traditional statistical tools of GWAS: during the next iterations, our method searches for subsets of markers whose compound effect on the phenotype is high. Consequently, our method is a model selection procedure, where the relationships between markers (gene interactions) and phenotypes are hypothesized and encoded by a model, and the method then evaluates all possible such models and identifies the most probable one from the available data. Furthermore, the models are represented using MLNs allowing us to bring the power of both logic and probabilistic reasoning into genetic analyses, which will allow direct extension to arbitrarily complex models.

### 5.1. The connection with logistic regression

Following the MLN syntax used in Alchemy (Kok et al., 2007), a single-marker model is expressed by the following program:

$$
\begin{aligned}
& \text { Phenotype }(\text { Strain },+T) \\
& \text { Allele }(\text { Strain },+ \text { Marker },+V) \Rightarrow \text { Phenotype }(\text { Strain },+T)
\end{aligned}
$$

Here, Phenotype and Allele are logical predicates, and Strain, Marker, $V$, and $T$ are variables. Assuming Marker $=m_{1}, V=v_{1}, T=t_{1}$, and Strain $=s_{1}$, predicates Phenotype $\left(s_{1}, t_{1}\right)$ and Allele $\left(s_{1}, m_{1}, v_{1}\right)$ encode two facts (two data points) that $t_{1}$ is a phenotype value of strain $s_{1}$ and that $v_{1}$ is an allele of marker $m_{1}$ for strain $s_{1}$. Furthermore, a logical formula, Allele $\left(\right.$ Strain, $\left.m_{1}, v_{1}\right) \Rightarrow$ Phenotype $\left(\right.$ Strain, $\left.t_{1}\right)$, encodes the following statement:
for all strains, an allele value $v_{1}$ of a marker $m_{1}$
implies a phenotype value $t_{1}$.
If Marker $\in\left\{m_{1}, \ldots, m_{N_{1}}\right\}, V \in\left\{v_{1}, \ldots, v_{N_{2}}\right\}, T \in\left\{t_{1}, \ldots, t_{N_{3}}\right\}$, and Strain $\in\left\{s_{1}, \ldots, s_{N_{4}}\right\}$, then program (13) is actually a set of $N_{3}$ instances of a first-order formula (15) and $N_{1} \times N_{2} \times N_{3}$ instances of a first-order formula (16) with separate weights $w_{i}$ and $w_{j k l}$ correspondingly:

$$
\begin{aligned}
& w_{i}: \text { Phenotype }\left(\text { Strain, } t_{i}\right) \\
& \ldots \\
& w_{j k l}: \text { Allele }\left(\text { Strain, } m_{j}, v_{k}\right) \Rightarrow \text { Phenotype }\left(\text { Strain, } t_{l}\right)
\end{aligned}
$$

Note that all variables of $(15,16)$ are replaced with various combinations of values, except for the variable Strain, which represents the specific, representative organism. Consequently, each formula represents a truth statement for any value of the variable Strain. A weight assigned to a formula indicates the probability of the truth of the encoded statement: the higher the weight, the greater the difference in log probability between the world that satisfies the statement and the one that does not. Note that while a weighted formula (16) models a probability distribution over logic statements (14), a weighted formula (15) models a binomial probability distribution of the phenotype values across all possible strains.

The model represented by the formulas (15) and (16) is equivalent to

$$
\begin{aligned}
& \cdots \\
& w_{i}: \text { Phenotype }\left(\text { Strain, } t_{i}\right) \\
& \cdots \\
& w_{j k l}: \text { Allele }\left(\text { Strain, } m_{j}, v_{k}\right) \wedge \text { Phenotype }\left(\text { Strain, } t_{l}\right) \\
& \quad \cdots
\end{aligned}
$$

if conditioned on Allele(Strain, $m_{i}, v_{j}$ ) for all $i$ and $j$. The equivalency between models $(15,16)$ and $(17,18)$ will be discussed later in this section.

Let us introduce characteristic functions $a_{i j}$ and $p_{k}$ :

$$
a_{i j}= \begin{cases}1, & \text { allele of marker } m_{i} \text { is } v_{j}, \\ 0, & \text { otherwise }\end{cases} \quad p_{k}= \begin{cases}1, & \text { phenotype is } t_{k} \\ 0, & \text { otherwise }\end{cases}
$$

Note that $a_{i j}=1$ and $p_{k}=1$ for a strain $s$ iff the corresponding predicates Allele $\left(s, m_{i}, v_{j}\right)$ and Phenotype $\left(s, t_{k}\right)$ are true. The MLN represented by the formulas $(17,18)$ encodes the joint probability distribution (see equation (4)):

$$
\operatorname{Pr}\left(p_{k}, a_{11}, \ldots, a_{N_{1} N_{2}}\right)=\frac{1}{Z} \exp \left(w_{k} p_{k}+\sum_{i=1}^{N_{1}} \sum_{j=1}^{N_{2}} w_{i j k} a_{i j} p_{k}\right)
$$

This equation yields a logistic regression formula where every characteristic function $a_{i j}$ of each allele is a binary predictor variable of a phenotype function $p_{k}$ (an outcome variable of the logistic regression):

$$
\log \left(\frac{\operatorname{Pr}\left(p_{k}=1 \mid a_{11}, \ldots, a_{N_{1} N_{2}}\right)}{\operatorname{Pr}\left(p_{k}=0 \mid a_{11}, \ldots, a_{N_{1} N_{2}}\right)}\right)=w_{k}+\sum_{i=1}^{N_{1}} \sum_{j=1}^{N_{2}} w_{i j k} a_{i j}
$$

Let us now come back to the equivalency of models $(15,16)$ and $(17,18)$. For simplicity we will compare the following two models:

$$
\begin{aligned}
& w_{1}: \mathbf{B}(x) \\
& w_{2}: \mathbf{A}(x) \wedge \mathbf{B}(x) \\
& w_{1}^{\prime}: \mathbf{B}(x) \\
& w_{2}^{\prime}: \mathbf{A}(x) \Rightarrow \mathbf{B}(x)
\end{aligned}
$$

As in our earlier discussion, we introduce two characteristic functions

$$
a= \begin{cases}1, & \mathbf{A} \text { is true } \\ 0, & \text { otherwise }\end{cases} \quad b= \begin{cases}1, & \mathbf{B} \text { is true } \\ 0, & \text { otherwise }\end{cases}
$$

We also introduce two binary feature functions representing a truth-value of a compound formula

$$
f_{1}= \begin{cases}1, & \mathbf{A} \wedge \mathbf{B} \text { is true } \\ 0, & \text { otherwise }\end{cases} \quad f_{2}= \begin{cases}1, & \mathbf{A} \Rightarrow \mathbf{B} \text { is true } \\ 0, & \text { otherwise }\end{cases}
$$

Table 5. Truth Table for Logical Conjunction and Implication


Table 5 provides the truth table for logical concatenation and implication. This table can be rewritten in terms of the characteristic functions (Table 6) revealing the dependency of $f_{1}$ and $f_{2}$ on $a$ and $b$, which can be written as:

$$
f_{1}=a b \text { and } f_{2}=1-a(1-b)
$$

The expression of $f_{2}$ in terms of $a$ and $b$ is also evident if we recall an equivalent representation of the logical implication through the concatenation and negation: $(\mathbf{A} \Rightarrow \mathbf{B}) \equiv \neg(\mathbf{A} \wedge \neg \mathbf{B})$, sometimes termed a "contrapositive."

In terms similar to (19), we can now express the joint probability distribution encoded by model (21) as

$$
\operatorname{Pr}(b, a)=\frac{1}{Z} \exp \left(w_{1} b+w_{2} f_{1}\right)
$$

Rewriting this as a logistic regression model, we get:

$$
\begin{aligned}
& \frac{\operatorname{Pr}(b=1 \mid a)}{\operatorname{Pr}(b=0 \mid a)}=\frac{\exp \left(w_{1}+w_{2} f_{1} \mid b=1\right)}{\left.\exp \left(w_{2} f_{1}\right|_{b=0}\right)}= \\
& =\frac{\exp \left(w_{1}+w_{2} a\right)}{\exp (0)}=\exp \left(w_{1}+w_{2} a\right)
\end{aligned}
$$

Model (22) encodes the joint probability distribution expressed as:

$$
\operatorname{Pr}(b, a)=\frac{1}{Z} \exp \left(w_{1}^{\prime} b+w_{2}^{\prime} f_{2}\right)
$$

and can therefore be represented as a logistic regression formula:

$$
\begin{aligned}
& \frac{\operatorname{Pr}(b=1 \mid a)}{\operatorname{Pr}(b=0 \mid a)}=\frac{\exp \left(w_{1}^{\prime}+w_{2}^{\prime} f_{2} \mid b=1\right)}{\left.\exp \left(w_{2}^{\prime} f_{2}\right|_{b=0}\right)}= \\
& =\frac{\exp \left(w_{1}^{\prime}+w_{2}^{\prime}\right)}{\exp \left(w_{2}^{\prime}(1-a)\right)}=\exp \left(w_{1}^{\prime}+w_{2}^{\prime} a\right)
\end{aligned}
$$

We can see then that, conditioned on a, the logistic regression models (24) and (25) are equivalent.

# 5.2. Single-markers models in Algorithm 1 

Working with haploid yeast genetics, every marker can have only 2 allele values, $A$ and $B$, so $N_{2}=2$. When applying a single-marker model (13) to one marker only (such as when we perform the first iteration of the marker search in Algorithm 1), $N_{1}=1$ and the simplified model (20) becomes

Table 6. Relationship Between Characteristic Functions $a, b$, Representing Two Propositions, and $f_{1}, f_{2}$, Representing a Conjunction and Implication Based on These Propositions


![img-3.jpeg](img-3.jpeg)

FIG. 4. Structure of a logical model underlying a single-marker MLN based on one marker. A single-marker MLN, defined by (13) and applied to a single marker $m_{1}$, encodes a MRF. For the illustration we assumed there are $s_{N}$ strains, and the phenotype can have two values. $\mathbf{A l}($ ) and $\mathbf{P h}($ ) stand for Allele() and Phenotype().

$$
\log \left(\frac{\operatorname{Pr}\left(p_{k}=1 \mid a_{11}, a_{12}\right)}{\operatorname{Pr}\left(p_{k}=0 \mid a_{11}, a_{12}\right)}\right)=w_{k}+w_{11 k} a_{11}+w_{12 k} a_{12}
$$

where

$$
a_{11}= \begin{cases}1, & \text { allele of } m_{1} \text { is } A \\ 0, & \text { otherwise }\end{cases} \quad a_{12}= \begin{cases}1, & \text { allele of } m_{1} \text { is } B \\ 0, & \text { otherwise }\end{cases}
$$

Figure 4 shows a structure of a MRF imposed by the logical formulas of the single-marker MLN (13) applied to one marker. Each node of the structure graph corresponds to a predicate (either Allele or Phenotype) whose variables are substituted with every possible combination of values. There is an edge between two nodes of the graph if the corresponding predicates appear in the same formula. In our example, edges show all possible dependencies of Phenotype on Allele: probabilistic dependency of $p_{1}$ and $p_{2}$ on $a_{11}$ and $a_{12}$, and thus every edge is assigned a probabilistic weight. Note that the graphical structure is disjoint, since there are no edges between nodes corresponding to different strains. Note that edges, such as Allele $\left(s_{1}, m_{1}, A\right)$ - Phenotype $\left(s_{1}, 0\right)$, Allele $\left(s_{2}, m_{1}, A\right)$ - Phenotype $\left(s_{2}, 0\right)$, etc, are instances of the same statistical template, Allele $\left(\cdot, m_{1}, A\right)$ - Phenotype $(\cdot, 0)$, and thus are assigned the same weight, learned from the entire network.

At the second iteration of Algorithm 1 using a single-marker model, each model is applied to two markers, one of which is a known marker $\bar{m}_{1}$ selected after the first iteration. Therefore, $N_{1}=2$ and the model (20) becomes

$$
\log \left(\frac{\operatorname{Pr}\left(p_{k}=1 \mid a_{11}, a_{12}, a_{21}, a_{22}\right)}{\operatorname{Pr}\left(p_{k}=0 \mid a_{11}, a_{12}, a_{21}, a_{22}\right)}\right)=w_{k}+w_{11 k} a_{11}+w_{12 k} a_{12}+w_{21 k} a_{21}+w_{22 k} a_{22}
$$

![img-4.jpeg](img-4.jpeg)

FIG. 5. Structure of a logical model underlying a single-marker MLN based on two markers. A single-marker MLN, defined by (13) and applied to a pair of markers $m_{1}$ and $m_{2}$, encodes a MRF. We assume there is a data set with $s_{N}$ strains, and for each strain the phenotype can have one of two possible values. In brown we show the subnetwork, which is the entire network in figure 4, illustrating the increase of complexity of the model when switching to the second iteration of Algorithm 1.

where

$$
\begin{aligned}
& a_{11}= \begin{cases}1, & \text { allele of } \bar{m}_{1} \text { is } A, \\
0, & \text { otherwise }\end{cases} \quad a_{12}= \begin{cases}1, & \text { allele of } \bar{m}_{1} \text { is } B \\
0, & \text { otherwise }\end{cases} \\
& a_{21}= \begin{cases}1, & \text { allele of } m_{2} \text { is } A, \\
0, & \text { otherwise }\end{cases} \quad a_{22}= \begin{cases}1, & \text { allele of } m_{2} \text { is } B . \\
0, & \text { otherwise }\end{cases}
\end{aligned}
$$

Figure 5 shows a graphical representation of a model generated for two markers at the second iteration. Notice that this model is similar to the model generated at the first iteration (Fig. 4). The only difference is in the number of predictor variables.

# 6. PAIR-WISE MODEL 

Like a single-marker model (13), a pair-wise model is expressed by the following program including more than one marker and variant:

$$
\begin{aligned}
& \text { Phenotype }(\text { Strain },+T) \\
& \text { Allele }\left(\text { Strain, }+M_{1},+V_{1}\right) \wedge \text { Allele }\left(\text { Strain, }+M_{2},+V_{2}\right) \Rightarrow \\
& \quad \Rightarrow \text { Phenotype }(\text { Strain },+T)
\end{aligned}
$$

Assuming $M_{1}=m_{1}, V_{1}=v_{1}, M_{2}=m_{2}, V_{2}=v_{2}$, and $T=t_{1}$, this program encodes a statement: for all strains, the allele values $v_{1}$ and $v_{2}$ of markers $m_{1}$ and $m_{2}$ together (as a pair) imply a phenotype value $t_{1}$.

As in the case of a single-marker model, the pair-wise MLN (29) encodes a joint probability distribution:

$$
\operatorname{Pr}\left(p_{m}, a_{11}, \ldots, a_{N_{1} N_{2}}\right)=\frac{1}{Z} \exp \left(w_{m} p_{m}+\sum_{i=1}^{N_{1}} \sum_{k=1}^{N_{2}} \sum_{j=1}^{N_{1}} \sum_{l=1}^{N_{2}} w_{i j m}^{k l} a_{i k} a_{j l} p_{m}\right)
$$

Since a genetic marker cannot have two different allele values at the same time, which means that $a_{i m} a_{i n}=0$ if $m \neq n$, expression (30) can be rewritten as:

$$
\begin{aligned}
& \operatorname{Pr}\left(p_{m}, a_{11}, \ldots, a_{N_{1} N_{2}}, b_{11}^{11}, \ldots, b_{N_{2} N_{2}}^{N_{1} N_{2}}\right)= \\
& =\frac{1}{Z} \exp \left(w_{m} p_{m}+\sum_{i=1}^{N_{1}} \sum_{j=1}^{N_{2}} w_{i j m} a_{i j} p_{m}+\right. \\
& \left.+\sum_{\substack{\left.u, l_{1} N_{2} \times N_{1} \\ \text { or }}} \sum_{\left(k, l\right) \in N_{2} \times N_{2}} w_{i j m}^{k l} b_{i j}^{k l} p_{m}\right)
\end{aligned}
$$

where $a_{i j}$ are the same characteristic functions as in the single-marker model case, and

$$
b_{i j}^{k l}= \begin{cases}1, & \text { allele of marker } m_{i} \text { is } v_{k} \text { and allele of marker } m_{j} \text { is } v_{l} . \\ 0, & \text { otherwise }\end{cases}
$$

Note that $b_{i j}^{k l}=a_{i k} a_{j l}$.
The pair-wise MLN can be seen as a logistic regression model where all characteristic functions $a_{i j}$ and $b_{i j}^{k l}$ are the predictor variables of an outcome variable $p_{m}$ :
$\log \left(\frac{\operatorname{Pr}\left(p_{m}=1 \mid a_{11}, \ldots, a_{N_{1} N_{2}}, b_{11}^{11}, \ldots, b_{N_{2} N_{2}}^{N_{1} N_{1}}\right)}{\operatorname{Pr}\left(p_{m}=0 \mid a_{11}, \ldots, a_{N_{1} N_{2}}, b_{11}^{11}, \ldots, b_{N_{2} N_{2}}^{N_{1}}\right)}\right)=w_{m}+\sum_{i=1}^{N_{1}} \sum_{j=1}^{N_{2}} w_{i j m} a_{i j}+\sum_{\substack{u, l_{1} N_{2} \times N_{1} \\ \text { or }}} \sum_{\left(k, l\right) \in N_{2} \times N_{2}} w_{i j m}^{k l} b_{i j}^{k l}$.
Note that this can also be seen as logistic regression with interaction terms of every pair of predictor variables $a_{i j}$.

![img-5.jpeg](img-5.jpeg)

FIG. 6. Structure of a logical model underlying a pair-wise MLN based on two markers. A pair-wise MLN, defined by (29) and applied to a pair of markers $m_{1}$ and $m_{2}$, encodes a MRF. As before, we assume a data set with $s_{N}$ strains and two phenotypes. In brown we show the sub-network, which is the entire network in figure 5, illustrating the increase of complexity when switching from a single-marker model to a pair-wise model. All the new edges, not present in figure 5, correspond to the pair-wise interactions and are colored in blue.

When applying a pair-wise model (29) to two markers, $N_{1}=2$ and the simplified model (32) becomes

$$
\begin{aligned}
& \log \left(\frac{\operatorname{Pr}\left(p_{m}=1 \mid a_{11}, a_{12}, a_{21}, a_{22}\right)}{\operatorname{Pr}\left(p_{m}=0 \mid a_{11}, a_{12}, a_{21}, a_{22}\right)}\right) \\
& \quad=w_{m}+w_{11 m} a_{11}+w_{12 m} a_{12}+w_{21 m} a_{21}+w_{22 m} a_{22}+ \\
& \quad+w_{12 m}^{11} b_{12}^{11}+w_{12 m}^{12} b_{12}^{12}+w_{12 m}^{21} b_{12}^{21}+w_{12 m}^{22} b_{12}^{22}+ \\
& \quad+w_{21 m}^{11} b_{21}^{11}+w_{21 m}^{12} b_{21}^{12}+w_{21 m}^{21} b_{21}^{21}+w_{21 m}^{22} b_{21}^{22}
\end{aligned}
$$

Recall that $p_{m}$ is a characteristic function equal to 1 when the phenotype has a value $t_{m}$. Note that this long expression of logistic regression with many predictor variables is compactly represented by a pairwise model (29) emphasizing the representational power of MLN.

The second line of equation (33) is similar to equation (28) of the single-marker model. That is why all the informative markers identified by algorithm 1 using a single-marker model can be also identified using a pair-wise model. The third and fourth lines of equation (33) are the interaction terms between alleles of different markers. Consider two markers that have a specific combination of alleles that are predictive of a phenotype, but that have no effect of the phenotype on their own (for example if the markers have a synthetic interaction). Equation (28) would not work on these markers, since each weight representing a predictive power of an individual marker will be zero. Similarly, the second line of equation (33) would disappear as well (the corresponding weights would also be zero). However, some of the weights of the interaction terms of equation (33) would not be zero allowing us to detect the synergy between two markers by using the pair-wise model.

Figure 6 illustrates a graphical representation of a pair-wise model generated for two markers. Notice that this model is somewhat similar to the single-marker model generated at the second iteration (Fig. 5). However, the major difference is that in a pair-wise model predictor variables are interconnected, forming cliques with phenotype variables (see blue edges in Fig. 6). Moreover, the probabilistic dependency is modeled between two predictor variables (alleles) and an outcome variable (a phenotype value); thus, the weights are assigned to every triangle (clique) connecting two marker alleles and a phenotype value.

Table 7 summarizes the three models described above: a single-marker MLN based on one and two markers and a pair-wise MLN based on two markers, and their corresponding representation as logistic regressions. The complexity of the regression formula for the pair-wise case points to the significant advantage of the first order logic expression, even when as here they can be effectively expressed as logistic regressions. The compactness of the expression of the model is striking. Many more complex models cannot, of course, be expressed at all as logistic regressions, even extremely large ones. The power of the compactness of expression of models in MLNs is illustrated by the rapid expansion of the equivalent logistic regressions shown above, relative to the modest expansion of the model complexity. Since we are

Table 7. Summary of Single-Marker MLNs Based on One and Two Markers as Well as a Pair-Wise MLN Based on Two Markers


The left column shows the formulas expressed in FOL defining the structure of the models, and the right column shows their corresponding representation as logistic regressions.
only scratching the surface of the underlying complexity of models that will be useful in future, the lesson here is evident.

# 7. OTHER APPLICATIONS IN BIOLOGY AND MEDICINE 

In its most abstract form, genetic analysis is directed to the detection of causative patterns in heritable genomes that predict well the phenotypes of interest. In a similar vein, the detection of patterns in data that predict experimental outcomes is at the heart of almost any modern biological or medical problem. Framed this way we can quickly conclude that MLNs and other probabilistic logic methods are well suited to the solution of these kinds of problems. Problems in this class include predicting sub-networks of the functioning complex networks that are central to cellular function (we do not presume to infer the entire networks of any system quite yet). This includes inferring networks from mRNA expression data like array data and RNA Seq data. An important characteristic of biological problems of this kind is that we sometimes know something about the system, or have specific hypotheses about the system, that need to be incorporated into the models during inference. MLNs are perfectly well suited to this kind of problem.

Classes of data like mRNA expression data-which include microRNA data, alternative splicing data (exon usage and alternative UTR use), protein expression level data, metabolite level data, transcription factor binding site occupation levels, histone modification and methylation patterns, and a variety of other kinds of molecular and non-molecular data-present the same kinds of problems. The challenge is to use these different data sets together to extract more information about the reality of the complex models that predict function than can be inferred from the individual sets by themselves. Since we also know something about how one kind of data is related to the others (e.g., proteins are made from mRNA at a rate determined by their sequences, translation factors and the levels of modulators like miRNAs) we need to represent this knowledge as constraints on the models when using the data together. This concept is a central aspect of true data integration and, as the knowledge of biology and medicine grows, is a major potential application for the methods we describe here.

## 8. CONCLUSION

Probabilistic logic methods, particularly those that use graphical model representations as a central part of the structure, are powerful tools in the analysis of data. They are particularly potent in dealing with biological data, as the field is currently in a state where the detailed data generation volume is enormous and the knowledge of the underlying complex systems is substantial, but very partial and often uncertain, with non-negligible quantitative error levels. Taking all of this into account-huge diverse data sets, partial knowledge of various types-is all but impossible without the systematic structures provided by methods and models that combine the rigors of representing and tracking multiple logical relationships with the

scoring of likelihoods reflecting reality in a balanced and integrated fashion. Neither strictly logical nor completely statistical and probabilistic methods can properly manage the complexity that is presented by the current state and dynamics of modern biological and medical research. Together they hold a great deal of promise.

We have summarized a wide range of both simple and complex mathematical and computational advances by focusing on a very general method, the MLN method, and attempting to put it into the context of some methods more familiar to most experimental and computational biologists. In the computational analysis of biological problems, analyzing data, inferring networks and complex models, and estimating model parameters, it has been common to use a range of methods based on various probabilistic logic models, sometimes collectively called "machine learning" methods. Inference methods based on the widely used BNs fall into this class, as do those based on HBNs, PBNs, and MLNs. We have tried to illustrate this landscape of methods, particularly contrasting MLNs with BNs, and describe some of the strengths and limitations. The pivotal concepts for the sketching of this landscape and comparisons of methods has been probabilistic graphical models, the structures of the graphs, and the scope of the logical language repertoire (from FOL to Boolean logic).

While these methods are powerful, the computational intensity is substantial for the most general, and therefore most potent of them. This certainly includes the application of MLN, for which the pair-wise genetic model has proven to be extremely computationally intensive. This limitation is, of course, temporary for several reasons, but two of them are evident. First, the available computing power to be brought to these problems is increasing rapidly and the costs are dropping. In addition, the engineering of software, and specialized hardware, for efficiency and speed in executing these algorithms, particularly using parallelization methods and hardware embodiment of algorithms, is substantial and growing. It is clear that the complexity of our understanding of biological problems, and the application of probabilistic logic methods are both at the very beginnings of their growth curves, and the future is very rich with possibilities.

# ACKNOWLEDGMENTS 

We are grateful to a number of colleagues for comments and suggestions on the manuscript: Aimee Dudley, Alex Skupin, and Hong Li. This work has been supported by the National Science Foundation FIBR Program and the Luxembourg-ISB Program.

## DISCLOSURE STATEMENT

No competing financial interests exist.
