# Inference in Probabilistic Logic Programs with Continuous Random Variables 

Muhammad Asiful Islam, C.R. Ramakrishnan, I.V. Ramakrishnan<br>Dept. of Computer Science<br>Stony Brook University<br>Stony Brook, NY 11794<br>\{maislam, cram, ram\}@cs.sunysb.edu


#### Abstract

Probabilistic Logic Programming (PLP), exemplified by Sato and Kameya's PRISM, Poole's ICL, Raedt et al's ProbLog and Vennekens et al's LPAD, is aimed at combining statistical and logical knowledge representation and inference. However, the inference techniques used in these works rely on enumerating sets of explanations for a query answer. Consequently, these languages permit very limited use of random variables with continuous distributions. In this paper, we present a symbolic inference procedure that uses constraints and represents sets of explanations without enumeration. This permits us to reason over PLPs with Gaussian or Gamma-distributed random variables (in addition to discrete-valued random variables) and linear equality constraints over reals. We develop the inference procedure in the context of PRISM; however the procedure's core ideas can be easily applied to other PLP languages as well. An interesting aspect of our inference procedure is that PRISM's query evaluation process becomes a special case in the absence of any continuous random variables in the program. The symbolic inference procedure enables us to reason over complex probabilistic models such as Kalman filters and a large subclass of Hybrid Bayesian networks that were hitherto not possible in PLP frameworks. (To appear in Theory and Practice of Logic Programming)


## 1 Introduction

Logic Programming (LP) is a well-established language model for knowledge representation based on first-order logic. Probabilistic Logic Programming (PLP) is a class of Statistical Relational Learning (SRL) frameworks (Getoor and Taskar 2007) which are designed for combining statistical and logical knowledge representation.

The semantics of PLP languages is defined based on the semantics of the underlying non-probabilistic logic programs. A large class of PLP languages, including ICL (Poole 2008), PRISM (Sato and Kameya 1997), ProbLog (Raedt et al. 2007) and LPAD (Vennekens et al. 2004), have a declarative distribution semantics, which defines a probability distribution over possible models of the program. Operationally, the combined statistical/logical inference is performed based on the proof structures analogous to those created by purely logical inference. In particular, inference proceeds as in traditional LPs except when a random variable's valuation is used. Use of a random variable creates a branch in the proof structure, one branch for each valuation of the variable. Each proof for an answer is associated with a probability based on the random variables used in the proof and their distribu-

tions; an answer's probability is determined by the probability that at least one proof holds. Since the inference is based on enumerating the proofs/explanations for answers, these languages have limited support for continuous random variables. We address this problem in this paper. A comparison of our work with recent efforts at extending other SRL frameworks to continuous variables appears in Section 2.

We provide an inference procedure to reason over PLPs with Gaussian or Gammadistributed random variables (in addition to discrete-valued ones), and linear equality constraints over values of these continuous random variables. We describe the inference procedure based on extending PRISM with continuous random variables. This choice is based on the following reasons. First of all, the use of explicit random variables in PRISM simplifies the technical development. Secondly, standard statistical models such as Hidden Markov Models (HMMs), Bayesian Networks and Probabilistic Context-Free Grammars (PCFGs) can be naturally encoded in PRISM. Along the same lines, our extension permits natural encodings of Finite Mixture Models (FMMs) and Kalman Filters. Thirdly, PRISM's inference naturally reduces to the Viterbi algorithm (Forney 1973) over HMMs, and the Inside-Outside algorithm (Lari and Young 1990) over PCFGs. The combination of well-defined model theory and efficient inference has enabled the use of PRISM for synthesizing knowledge in sensor networks (Singh et al. 2008).

It should be noted that, while the technical development in this paper is limited to PRISM, the basic technique itself is applicable to other similar PLP languages such as ProbLog and LPAD (see Section 7).

Our Contribution: We extend PRISM at the language level to seamlessly include discrete as well as continuous random variables. We develop a new inference procedure to evaluate queries over such extended PRISM programs.

- We extend the PRISM language for specifying distributions of continuous random variables, and linear equality constraints over such variables.
- We develop a symbolic inference technique to reason with constraints on the random variables. PRISM's inference technique becomes a special case of our technique when restricted to logic programs with discrete random variables.
- These two developments enable the encoding of rich statistical models such as Kalman Filters and a large class of Hybrid Bayesian Networks; and exact inference over such models, which were hitherto not possible in LP and its probabilistic extensions.

Note that the technique of using PRISM for in-network evaluation of queries in a sensor network (Singh et al. 2008) can now be applied directly when sensor data and noise are continuously distributed. Tracking and navigation problems in sensor networks are special cases of the Kalman Filter problem (Chu et al. 2007). There are a number of other network inference problems, such as the indoor localization problem, that have been modeled as FMMs (Goswami et al. 2011). Moreover, our extension permits reasoning over models with finite mixture of Gaussians and discrete distributions (see Section 7). Our extension of PRISM brings us closer to the ideal of finding a declarative basis for programming in the presense of noisy data.

The rest of this paper is organized as follows. We begin with a review of related work in Section 2, and describe the PRISM framework in detail in Section 3. We introduce the extended PRISM language and the symbolic inference technique for the extended language in Section 5. In section 6 we show the use of this technique on an example encoding of the Kalman Filter. We conclude in Section 7 with a discussion on extensions to our inference procedure.

# 2 Related Work 

Over the past decade, a number of Statistical Relational Learning (SRL) frameworks have been developed, which support modeling, inference and/or learning using a combination of logical and statistical methods. These frameworks can be broadly classified as statistical-model-based or logic-based, depending on how their semantics is defined. In the first category are frameworks such as Bayesian Logic Programs (BLPs) (Kersting and Raedt 2000), Probabilistic Relational Models (PRMs) (Friedman et al. 1999), and Markov Logic Networks (MLNs) (Richardson and Domingos 2006), where logical relations are used to specify a model compactly. A BLP consists of a set of Bayesian clauses (constructed from Bayesian network structure), and a set of conditional probabilities (constructed from CPTs of Bayesian network). PRMs encodes discrete Bayesian Networks with Relational Models/Schemas. An MLN is a set of formulas in first order logic associated with weights. The semantics of a model in these frameworks is given in terms of an underlying statistical model obtained by expanding the relations.

Inference in SRL frameworks such as PRISM (Sato and Kameya 1997), Stochastic Logic Programs (SLP) (Muggleton 1996), Independent Choice Logic (ICL) (Poole 2008), and ProbLog (Raedt et al. 2007) is primarily driven by query evaluation over logic programs. In SLP, clauses of a logic program are annotated with probabilities, which are then used to associate probabilities with proofs (derivations in a logic program). ICL (Poole 1993) consists of definite clauses and disjoint declarations of the form disjoint $\left(\left[h_{1}: p_{1}, \ldots, h_{n}: p_{n}\right]\right)$ that specifies a probability distribution over the hypotheses (i.e., $\left\{h_{1}, . ., h_{n}\right\}$ ). Any probabilistic knowledge representable in a discrete Bayesian network can be represented in this framework. While the language model itself is restricted (e.g., ICL permits only acyclic clauses), it had declarative distribution semantics. This semantic foundation was later used in other frameworks such as PRISM and ProbLog. CP-Logic (Vennekens et al. 2009) is a logical language to represent probabilistic causal laws, and its semantics is equivalent to probability distribution over well-founded models of certain logic programs. Specifications in LPAD (Vennekens et al. 2004) resemble those in CP-Logic: probabilistic predicates are specified with disjunctive clauses, i.e. clauses with multiple disjunctive consequents, with a distribution defined over the consequents. LPAD has a distribution semantics, and a proof-based operational semantics similar to that of PRISM. ProbLog specifications annotate facts in a logic program with probabilities. In contrast to SLP, ProbLog has a distribution semantics and a proof-based operational semantics. PRISM (discussed in detail in the next section), LPAD and ProbLog are equally expressive. PRISM uses explicit random variables and a simple inference but restricted procedure. In particular, PRISM demands that the set of

proofs for an answer are pairwise mutually exclusive, and that the set of random variables used in a single proof are pairwise independent. The inference procedures of LPAD and ProbLog lift these restrictions.

SRL frameworks that are based primarily on statistical inference, such as BLP, PRM and MLN, were originally defined over discrete-valued random variables, and have been naturally extended to support a combination of discrete and continuous variables. Continuous BLP (Kersting and Raedt 2001) and Hybrid PRM (Narman et al. 2010) extend their base models by using Hybrid Bayesian Networks (Murphy 1998). Hybrid MLN (Wang and Domingos 2008) allows description of continuous properties and attributes (e.g., the formula $\operatorname{length}(x)=5$ with weight $w)$ deriving MRFs with continuous-valued nodes (e.g., length(a) for a grounding of $x$, with mean 5 and standard deviation $1 / \sqrt{2 w}$ ).

In contrast to BLP, PRM and MLN, SRL frameworks that are primarily based on logical inference offer limited support for continuous variables. In fact, among such frameworks, only ProbLog has been recently extended with continuous variables. Hybrid ProbLog (Gutmann et al. 2010) extends Problog by adding a set of continuous probabilistic facts (e.g., $\left(X_{i}, \phi_{i}\right):: f_{i}$, where $X_{i}$ is a variable appearing in atom $f_{i}$, and $\phi_{i}$ denotes its Gaussian density function). It adds three predicates namely below, above, ininterval to the background knowledge to process values of continuous facts. A ProbLog program may use a continuous random variable, but further processing can be based only on testing whether or not the variable's value lies in a given interval. As a consequence, statistical models such as Finite Mixture Models can be encoded in Hybrid ProbLog, but others such as certain classes of Hybrid Bayesian Networks (with continuous child with continuous parents) and Kalman Filters cannot be encoded. The extension to PRISM described in this paper makes the framework general enough to encode such statistical models.

More recently, (Gutmann et al. 2011) introduced a sampling based approach for (approximate) probabilistic inference in a ProbLog-like language that combines continuous and discrete random variables. The inference algorithm uses forward chaining and rejection sampling. The language permits a large class of models where discrete and continuous variables may be combined without restriction. In contrast, we propose an exact inference algorithm with a more restrictive language, but ensure that inference matches the complexity of specialized inference algorithms for important classes of statistical models (e.g., Kalman filters).

# 3 Background: an overview of PRISM 

PRISM programs have Prolog-like syntax (see Fig. 1). In a PRISM program the msw relation ("multi-valued switch") has a special meaning: $\operatorname{msw}(X, I, V)$ says that V is the outcome of the I-th instance from a family X of random processes ${ }^{1}$. The set of variables $\left\{\mathrm{V}_{i} \mid \operatorname{msw}\left(p, i, \mathrm{~V}_{i}\right)\right\}$ are i.i.d. for a given random process $p$. The distribution parameters of the random variables are specified separately.

The program in Fig. 1 encodes a Hidden Markov Model (HMM) in PRISM.

[^0]
[^0]:    ${ }^{1}$ Following PRISM, we often omit the instance number in an msw when a program uses only one instance from a family of random processes.

The set of observations is encoded as facts of predicate obs, where obs (I, V) means that value V was observed at time I. In the figure, the clause defining hmm says that T is the N -th state if we traverse the HMM starting at an initial state S (itself the outcome of the random process init). In hmm_part(I, N, S, T), S is the I-th state, T is the N-th state. The first clause of hmm_part defines the conditions under which we go from the I-th state S to the I+1-th state NextS. Random processes trans (S) and emit(S) give the distributions of transitions and emissions, respectively, from state S.

The meaning of a PRISM program is given in terms of a distribution semantics (Sato and Kameya 1997; Sato and Kameya 1999). A PRISM program is treated as a non-probabilistic logic program over a set of probabilistic facts, the msw relation. An instance of the msw relation defines one choice of values of all random variables. A PRISM program is associated with a set of least models, one for each msw relation instance. A probability distribution is then defined over the set of models, based on the probability distribution of the msw relation instances. This distribution is the semantics of a PRISM program. Note that the distribution semantics is declarative. For a subclass of programs, PRISM has an efficient procedure for computing this semantics based on OLDT resolution (Tamaki and Sato 1986).

Inference in PRISM proceeds as follows. When the goal selected at a step is of the form $\operatorname{msw}(\mathrm{X}, \mathrm{I}, \mathrm{Y})$, then Y is bound to a possible outcome of a random process X . Thus in PRISM, derivations are constructed by enumerating the possible outcomes of each random variable. The derivation step is associated with the probability of this outcome. If all random processes encountered in a derivation are independent, then the probability of the derivation is the product of probabilities of each step in the derivation. If a set of derivations are pairwise mutually exclusive, the probability of the set is the sum of probabilities of each derivation in the set. PRISM's evaluation procedure is defined only when the independence and exclusiveness assumptions hold. Finally, the probability of an answer is the probability of the set of derivations of that answer.

# 4 Extended PRISM 

Support for continuous variables is added by modifying PRISM's language in two ways. We use the msw relation to sample from discrete as well as continuous distributions. In PRISM, a special relation called values is used to specify the ranges of values of random variables; the probability mass functions are specified using set_sw directives. In our extension, we extend the set_sw directives to specify probability density functions as well. For instance, set_sw(r, norm(Mu,Var)) specifies that outcomes of random processes r have Gaussian distribution with mean Mu and

variance Var ${ }^{2}$. Parameterized families of random processes may be specified, as long as the parameters are discrete-valued. For instance, set_sw(w(M), norm(Mu,Var)) specifies a family of random processes, with one for each value of M. As in PRISM, set_sw directives may be specified programmatically; for instance, in the specification of $w(M)$, the distribution parameters may be computed as functions of $M$.

Additionally, we extend PRISM programs with linear equality constraints over reals. Without loss of generality, we assume that constraints are written as linear equalities of the form $Y=a_{1} * X_{1}+\ldots+a_{n} * X_{n}+b$ where $a_{i}$ and $b$ are all floatingpoint constants. The use of constraints enables us to encode Hybrid Bayesian Networks and Kalman Filters as extended PRISM programs. In the following, we use Constr to denote a set (conjunction) of linear equality constraints. We also denote by $\bar{X}$ a vector of variables and/or values, explicitly specifying the size only when it is not clear from the context. This permits us to write linear equality constraints compactly (e.g., $Y=\bar{a} \cdot \bar{X}+b$ ).

Encoding of Kalman Filter specifications uses linear constraints and closely follows the structure of the HMM specification, and is shown in Section 6.

Distribution Semantics: We extend PRISM's distribution semantics for continuous random variables as follows. The idea is to construct a probability space for the msw definitions (called probabilistic facts in PRISM) and then extend it to a probability space for the entire program using least model semantics. Sample space for the probabilistic facts is constructed from those of discrete and continuous random variables. The sample space of a continuous random variable is the set of real numbers, $\Re$. The sample space of a set of random variables is a Cartesian product of the sample spaces of individual variables. We complete the definition of a probability space for $N$ continuous random variables by considering the Borel $\sigma$-algebra over $\Re^{N}$, and defining a Lebesgue measure on this set as the probability measure. Lifting the probability space to cover the entire program needs one significant step. We use the least model semantics of constraint logic programs (Jaffar et al. 1998) as the basis for defining the semantics of extended PRISM programs. A point in the sample space is an arbitrary interpretation of the program, with its Herbrand universe and $\Re$ as the domain of interpretation. For each sample, we distinguish between the interpretation of user-defined predicates and probabilistic facts. Note that only the probabilistic facts have probabilistic behavior in PRISM; the rest of a model is defined in terms of logical consequence. Hence, we can define a probability measure over a set of sample points by using the measure defined for the probabilistic facts alone. The semantics of an extended PRISM program is thus defined as a distribution over its possible models.

# 5 Inference 

Recall that PRISM's inference explicitly enumerates outcomes of random variables in derivations. The key to inference in the presence of continuous random vari-

[^0]
[^0]:    ${ }^{2}$ The technical development in this paper considers only univariate Gaussian variables; see Discussions section on a discussion on how multivariate Gaussian as well as other continuous distributions are handled.

ables is avoiding enumeration by representing the derivations and their attributes symbolically. A single step in the construction of a symbolic derivation is defined below.

Definition 1 (Symbolic Derivation)
A goal $G$ directly derives goal $G^{\prime}$, denoted $G \rightarrow G^{\prime}$, if:
PCR: $G=q_{1}\left(\overline{X_{1}}\right), G_{1}$, and there exists a clause in the program,
$q_{1}(\bar{Y}):-r_{1}\left(\overline{Y_{1}}\right), r_{2}\left(\overline{Y_{2}}\right), \ldots, r_{m}\left(\overline{Y_{m}}\right)$, such that $\theta=\operatorname{mgu}\left(q_{1}\left(\overline{X_{1}}\right), q_{1}(\bar{Y})\right)$; then, $G^{\prime}=\left(r_{1}\left(\overline{Y_{1}}\right), r_{2}\left(\overline{Y_{2}}\right), \ldots, r_{m}\left(\overline{Y_{m}}\right), G_{1}\right) \theta ;$
MSW: $G=\operatorname{msw}(\operatorname{rv}(\bar{X}), Y), G_{1}$ : then $G^{\prime}=G_{1}$;
CONS: $G=$ Constr, $G_{1}$ and Constr is satisfiable: then $G^{\prime}=G_{1}$.
A symbolic derivation of $G$ is a sequence of goals $G_{0}, G_{1}, \ldots$ such that $G=G_{0}$ and, for all $i \geq 0, G_{i} \rightarrow G_{i+1}$.

We only consider successful derivations, i.e., the last step of a derivation resolves to an empty clause. Note that the traditional notion of derivation in a logic program coincides with that of symbolic derivation when the selected subgoal (literal) is not an msw or a constraint. When the selected subgoal is an msw, PRISM's inference will construct the next step by enumerating the values of the random variable. In contrast, symbolic derivation skips msw's and constraints and continues with the remaining subgoals in a goal. The effect of these constructs is computed by associating (a) variable type information and (b) a success function (defined below) with each goal in the derivation. The symbolic derivation for the goal widget ( X ) over the program in Example 1 is shown in Fig. 2b.

```
widget(X) :- msw(m, M),
    msw(st(M), Z),
    msw(pt, Y),
    X = Y + Z.
    6}\mathrm{ G}
% Ranges of RVs
    G
values(m, [a,b]).
values(pt, real).
% PDFs and PMFs:
:- set_sw(m, [0.3, 0.7]), 
    set_sw(st(a), norm(2.0, 1.0)),
    set_sw(st(b), norm(3.0, 1.0)),
    set_sw(pt, norm(0.5, 0.1)).
```

(a) Mixture model program
(b) Symbolic derivation for goal widget ( X )

Fig. 2: Finite Mixture Model Program and Symbolic Derivation

# Example 1 

Consider a factory with two machines a and b. Each machine produces a widget structure and then the structure is painted with a color. In the program Fig. 2a, $\operatorname{msw}(\mathrm{m}, \mathrm{M})$ chooses either machine a or $\mathrm{b}, \mathrm{msw}(\mathrm{st}(\mathrm{M}), \mathrm{Z})$ gives the cost Z of a

product structure, $\mathrm{msw}(\mathrm{pt}, \mathrm{Y})$ gives the cost Y of painting, and finally $\mathrm{X}=\mathrm{Y}+\mathrm{Z}$ returns the price of a painted widget X .

```
q(Y) :- msw(rv, X),
    p(X, Y).
p(a, Y) :- r(Y).
p(b, Y) :- s(Y).
r(1).
r(2).
s(2).
s(3).
values(rv, [a,b]).
:- set_sw(rv, [0.3, 0.7]).
```

(a) Example program
(b) Symbolic derivation for goal q(Y)

Fig. 3: Symbolic derivation

# Example 2 

This example illustrates how symbolic derivation differs from traditional logic programming derivation. Fig. 3b shows the symbolic derivation for goal $q(Y)$ in Fig. 3a.

Notice that the symbolic derivation still makes branches in the derivation tree for various logic definitions and outcomes. But the main difference with traditional logic derivation is that it skips msw and Constr definitions, and continues with the remaining subgoals in a goal.

Success Functions: Goals in a symbolic derivation may contain variables whose values are determined by msw's appearing subsequently in the derivation. With each goal $G_{i}$ in a symbolic derivation, we associate a set of variables, $V\left(G_{i}\right)$, that is a subset of variables in $G_{i}$. The set $V\left(G_{i}\right)$ is such that the variables in $V\left(G_{i}\right)$ subsequently appear as parameters or outcomes of msw's in some subsequent goal $G_{j}, j \geq i$. We can further partition $V$ into two disjoint sets, $V_{c}$ and $V_{d}$, representing continuous and discrete variables, respectively. The sets $V_{c}$ and $V_{d}$ are called the derivation variables of $G_{i}$, defined below.

## Definition 2 (Derivation Variables)

Let $G \rightarrow G^{\prime}$ such that $G^{\prime}$ is derived from $G$ using:
PCR: Let $\theta$ be the mgu in this step. Then $V_{c}(G)$ and $V_{d}(G)$ are the largest sets of variables in $G$ such that $V_{c}(G) \theta \subseteq V_{c}\left(G^{\prime}\right)$ and $V_{d}(G) \theta \subseteq V_{d}\left(G^{\prime}\right)$.
MSW: Let $G=\operatorname{msw}(\operatorname{rv}(\bar{X}), Y), G^{\prime}$. Then $V_{c}(G)$ and $V_{d}(G)$ are the largest sets of variables in $G$ such that $V_{c}(G) \subseteq V_{c}\left(G^{\prime}\right) \cup\{Y\}$, and $V_{d}(G) \subseteq V_{d}\left(G^{\prime}\right) \cup \bar{X}$ if $Y$ is continuous, otherwise $V_{c}(G) \subseteq V_{c}\left(G^{\prime}\right)$, and $V_{d}(G) \subseteq V_{d}\left(G^{\prime}\right) \cup \bar{X} \cup\{Y\}$.
CONS: Let $G=$ Constr, $G^{\prime}$. Then $V_{c}(G)$ and $V_{d}(G)$ are the largest sets of variables in $G$ such that $V_{c}(G) \subseteq V_{c}\left(G^{\prime}\right) \cup \operatorname{vars}($ Constr), and $V_{d}(G) \subseteq V_{d}\left(G^{\prime}\right)$.

Given a goal $G_{i}$ in a symbolic derivation, we can associate with it a success function, which is a function from the set of all valuations of $V\left(G_{i}\right)$ to $[0,1]$. Intuitively, the success function represents the probability that the symbolic derivation represents a successful derivation for each valuation of $V\left(G_{i}\right)$.

Representation of success functions: Given a set of variables $\mathbf{V}$, let $\mathbf{C}$ denote the set of all linear equality constraints over reals using $\mathbf{V}$. Let $\mathbf{L}$ be the set of all linear functions over $\mathbf{V}$ with real coefficients. Let $\mathcal{N}_{X}\left(\mu, \sigma^{2}\right)$ be the PDF of a univariate Gaussian distribution with mean $\mu$ and variance $\sigma^{2}$, and $\delta_{x}(X)$ be the Dirac delta function which is zero everywhere except at $x$ and integration of the delta function over its entire range is 1 . Expressions of the form $k * \prod_{l} \delta_{v}\left(V_{l}\right) \prod_{i} \mathcal{N}_{f_{i}}$, where $k$ is a non-negative real number and $f_{i} \in \mathbf{L}$, are called product $P D F$ (PPDF) functions over $\mathbf{V}$. We use $\phi$ (possibly subscripted) to denote such functions. A pair $\langle\phi, C\rangle$ where $C \subseteq \mathbf{C}$ is called a constrained PPDF function. A sum of a finite number of constrained PPDF functions is called a success function, represented as $\sum_{i}\left\langle\phi_{i}, C_{i}\right\rangle$.

We use $C_{i}(\psi)$ to denote the constraints (i.e., $C_{i}$ ) in the $i^{t h}$ constrained PPDF function of success function $\psi$; and $D_{i}(\psi)$ to denote the $i^{t h}$ PPDF function of $\psi$.

Success functions of base predicates: The success function of a constraint $C$ is $\langle 1, C\rangle$. The success function of true is $\langle 1$, true $\rangle$. The PPDF component of $\operatorname{msw}(\operatorname{rv}(\bar{X}), Y)$ 's success function is the probability density function of rv's distribution if rv is continuous, and its probability mass function if rv is discrete; its constraint component is true.

# Example 3 

The success function $\psi_{1}$ of $\operatorname{msw}(\mathrm{m}, \mathrm{M})$ for the program in Example 1 is such that $\psi_{1}=$ $0.3 \delta_{a}(M)+0.7 \delta_{b}(M)$. Note that we can represent the success function using tables, where each table row denotes discrete random variable valuations. For example, the above success function can be represented as Fig. 4a. Thus instead of using delta functions, we often omit it in examples and represent success functions using tables.

Fig. 4b represents the success function of $\operatorname{msw}(\operatorname{st}(\mathrm{M}), \mathrm{Z})$ for the program in Example 1. Similarly, the success function $\psi_{3}$ of $\operatorname{msw}(\mathrm{pt}, \mathrm{Y})$ for the program in Example 1 is $\psi_{3}=\mathcal{N}_{Y}(0.5,0.1)$.

Finally, the success function $\psi_{4}$ of $\mathrm{X}=\mathrm{Y}+\mathrm{Z}$ for the program in Example 1 is $\psi_{4}=\langle 1, X=Y+Z\rangle$.

Success functions of user-defined predicates: If $G \rightarrow G^{\prime}$ is a step in a derivation, then the success function of $G$ is computed bottom-up based on the success function of $G^{\prime}$. This computation is done using join and marginalize operations on success functions.




Definition 3 (Join)
Fig. 4: Success Functions
Let $\psi_{1}=\sum_{i}\left\langle D_{i}, C_{i}\right\rangle$ and $\psi_{2}=\sum_{j}\left\langle D_{j}, C_{j}\right\rangle$ be two success functions, then join of $\psi_{1}$ and $\psi_{2}$ represented as $\psi_{1} * \psi_{2}$ is the success function $\sum_{i, j}\left\langle D_{i} D_{j}, C_{i} \wedge C_{j}\right\rangle$.

# Example 4 

Let Fig. 5a and 5b represent the success functions $\psi_{m s w(m, M)}(M)$ and $\psi_{G_{3}}(X, Y, Z, M)$ respectively.




(a)


(c)

Fig. 5: Join of Success Functions
Then Fig. 5c shows the join of $\psi_{m s w(m, M)}(M)$ and $\psi_{G_{3}}(X, Y, Z, M)$.
Note that we perform a simplification of success functions after the join operation. We eliminate any PPDF term in $\psi$ which is inconsistent w.r.t. delta functions. For example, $\delta_{a}(M) \delta_{b}(M)=0$ as $M$ can not be both $a$ and $b$ at the same time.

Given a success function $\psi$ for a goal $G$, the success function for $\exists X . G$ is computed by the marginalization operation. Marginalization w.r.t. a discrete variable is straightforward and omitted. Below we define marginalization w.r.t. continuous variables in two steps: first rewriting the success function in a projected form and then doing the required integration.

The goal of projection is to eliminate any linear constraint on $V$, where $V$ is the continuous variable to marginalize over. The projection operation involves finding a linear constraint (i.e., $V=\bar{a} \cdot \bar{X}+b$ ) on $V$ and replacing all occurrences of $V$ in the success function by $\bar{a} \cdot \bar{X}+b$.

## Definition 4 (Projection)

Projection of a success function $\psi$ w.r.t. a continuous variable $V$, denoted by $\psi \downarrow_{V}$, is a success function $\psi^{\prime}$ such that
$\forall i . D_{i}\left(\psi^{\prime}\right)=D_{i}(\psi)[\bar{a} \cdot \bar{X}+b / V]$; and $C_{i}\left(\psi^{\prime}\right)=\left(C_{i}(\psi)-C_{i p}\right)[\bar{a} \cdot \bar{X}+b / V]$,
where $C_{i p}$ is a linear constraint $(V=\bar{a} \cdot \bar{X}+b)$ on $V$ in $C_{i}(\psi)$ and $t[s / x]$ denotes replacement of all occurrences of $x$ in $t$ by $s$.

Note that the replacement of $V$ by $\bar{a} \cdot \bar{X}+b$ in PDFs and linear constraints does not alter the general form of a success function. Thus projection returns a success function. Notice that if $\psi$ does not contain any linear constraint on $V$, then the projected form remains the same.

## Example 5

Let $\psi_{1}=\left\langle 0.3 \mathcal{N}_{Z}(2.0,1.0), \mathcal{N}_{Y}(0.5,0.1), X=Y+Z\right\rangle$ represent a success function. Then projection of $\psi_{1}$ w.r.t. $Y$ yields

$$
\psi_{1} \downarrow_{Y}=0.3 \mathcal{N}_{Z}(2.0,1.0) \cdot \mathcal{N}_{X-Z}(0.5,0.1)
$$

Notice that $Y$ is replaced by $X-Z$.

# Proposition 1 

Integration of a PPDF function with respect to a variable $V$ is a PPDF function, i.e.,

$$
\alpha \int_{-\infty}^{\infty} \prod_{k=1}^{m} \mathcal{N}_{\left(\overline{a_{k}} \cdot \overline{X_{k}}+b_{k}\right)}\left(\mu_{k}, \sigma_{k}^{2}\right) d V=\alpha^{\prime} \prod_{l=1}^{m^{\prime}} \mathcal{N}_{\left(\overline{a_{l}} \cdot \overline{X_{l}^{\prime}}\right)+b_{l}^{\prime}}\left(\mu_{l}^{\prime}, \sigma_{l}^{\prime 2}\right)
$$

where $V \in \overline{X_{k}}$ and $V \notin \overline{X_{l}^{\prime}}$.
For example,

$$
\begin{aligned}
& \int_{-\infty}^{\infty} \mathcal{N}_{a_{1} V-X_{1}}\left(\mu_{1}, \sigma_{1}^{2}\right) \cdot \mathcal{N}_{a_{2} V-X_{2}}\left(\mu_{2}, \sigma_{2}^{2}\right) d V \\
& =\mathcal{N}_{a_{2} X_{1}-a_{1} X_{2}}\left(a_{1} \mu_{2}-a_{2} \mu_{1}, a_{2}^{2} \sigma_{1}^{2}+a_{1}^{2} \sigma_{2}^{2}\right)
\end{aligned}
$$

Here $X_{1}, X_{2}$ are linear combinations of variables (except $V$ ). A proof of the proposition is presented in Section 8.

## Definition 5 (Integration)

Let $\psi$ be a success function that does not contain any linear constraints on $V$. Then integration of $\psi$ with respect to $V$, denoted by $\oint_{V} \psi$ is a success function $\psi^{\prime}$ such that $\forall i . D_{i}\left(\psi^{\prime}\right)=\int D_{i}(\psi) d V$.

It is easy to see (using Proposition 1) that the integral of success functions are also success functions. Note that if $\psi$ does not contain any PDF on $V$, then the integrated form remains the same.

## Example 6

Let $\psi_{2}=0.3 \mathcal{N}_{Z}(2.0,1.0) \cdot \mathcal{N}_{X-Z}(0.5,0.1)$ represent a success function. Then integration of $\psi_{2}$ w.r.t. $Z$ yields

$$
\begin{aligned}
\oint_{Z} \psi_{2} & =\int 0.3 \mathcal{N}_{Z}(2.0,1.0) \cdot \mathcal{N}_{X-Z}(0.5,0.1) d Z \\
& =0.3 \mathcal{N}_{X}(2.5,1.1) . \text { (using Equation 2) }
\end{aligned}
$$

## Definition 6 (Marginalize)

Marginalization of a success function $\psi$ with respect to a variable $V$, denoted by $\mathbb{M}(\psi, V)$, is a success function $\psi^{\prime}$ such that

$$
\psi^{\prime}=\oint_{V} \psi \downarrow_{V}
$$

We overload $\mathbb{M}$ to denote marginalization over a set of variables, defined such that $\mathbb{M}(\psi,\{V\} \cup \bar{X})=\mathbb{M}(\mathbb{M}(\psi, V), \bar{X})$ and $\mathbb{M}(\psi,\{ \})=\psi$.

## Proposition 2

The set of all success functions is closed under join and marginalize operations.
The success function for a derivation is defined as follows.

Definition 7 (Success function of a goal)
The success function of a goal $G$, denoted by $\psi_{G}$, is computed based on the derivation $G \rightarrow G^{\prime}$ :

$$
\psi_{G}= \begin{cases}\sum_{G^{\prime}} \mathbb{M}\left(\psi_{G^{\prime}}, V\left(G^{\prime}\right)-V(G)\right) & \text { for all program clause resolution } G \rightarrow G^{\prime} \\ \psi_{\text {msw }(r v(\bar{X}), Y)} * \psi_{G^{\prime}} & \text { if } G=\operatorname{msw}(\operatorname{rv}(\bar{X}), Y), G^{\prime} \\ \psi_{\text {Constr }} * \psi_{G^{\prime}} & \text { if } G=\text { Constr, } G^{\prime}\end{cases}
$$

Note that the above definition carries PRISM's assumption that an instance of a random variable occurs at most once in any derivation. In particular, the PCR step marginalizes success functions w.r.t. a set of variables; the valuations of the set of variables must be mutually exclusive for correctness of this step. The MSW step joins success functions; the goals joined must use independent random variables for the join operation to correctly compute success functions in this step.

# Example 7 

Fig. 2b shows the symbolic derivation for the goal widget (X) over the mixture model program in Example 1. The success function of goal $G_{5}$ is $\psi_{G_{5}}(X, Y, Z)=$ $\langle 1, X=Y+Z\rangle$.

$$
\psi_{G_{4}}(X, Y, Z)=\psi_{m s w(p t, Y)}(Y) * \psi_{G_{5}}(X, Y, Z)=\left\langle\mathcal{N}_{Y}(0.5,0.1), X=Y+Z\right\rangle
$$

The success function of goal $G_{3}$ is $\psi_{m s w(s t(M), Z)}(Z) * \psi_{G_{4}}(X, Y, Z)$ (Fig. 5b).
Then join of $\psi_{m s w(m, M)}(M)$ and $\psi_{G_{3}}(X, Y, Z, M)$ yields the success function in Fig. 5c (see Example 4).

Finally, $\psi_{G_{1}}(X)=\mathbb{M}\left(\psi_{G_{2}}(X, Y, Z, M),\{M, Y, Z\}\right)$.
First we marginalize $\psi_{G_{2}}(X, Y, Z, M)$ w.r.t. $M$ :

$$
\begin{aligned}
\psi_{G_{2}}^{\prime} & =\mathbb{M}\left(\psi_{G_{2}}, M\right)=\oint_{M} \psi_{G_{2}} \downarrow_{M} \\
& =\left\langle 0.3 \mathcal{N}_{Z}(2.0,1.0) \cdot \mathcal{N}_{Y}(0.5,0.1), X=Y+Z\right\rangle \\
& +\left\langle 0.7 \mathcal{N}_{Z}(3.0,1.0) \cdot \mathcal{N}_{Y}(0.5,0.1), X=Y+Z\right\rangle
\end{aligned}
$$

Next we marginalize the above success function w.r.t. $Y$ :

$$
\begin{aligned}
\psi_{G_{2}}^{\prime \prime} & =\mathbb{M}\left(\psi_{G_{2}}^{\prime}, Y\right)=\oint_{Y} \psi_{G_{2}}^{\prime} \downarrow_{Y} \\
& =0.3 \mathcal{N}_{Z}(2.0,1.0) \cdot \mathcal{N}_{X-Z}(0.5,0.1)+0.7 \mathcal{N}_{Z}(3.0,1.0) \cdot \mathcal{N}_{X-Z}(0.5,0.1)
\end{aligned}
$$

Finally, we marginalize the above function over variable $Z$ to get $\psi_{G_{1}}(X)$ :

$$
\psi_{G_{1}}(X)=\mathbb{M}\left(\psi_{G_{2}}^{\prime \prime}, Z\right)=\oint_{Z} \psi_{G_{2}}^{\prime \prime} \downarrow_{Z}=0.3 \mathcal{N}_{X}(2.5,1.1)+0.7 \mathcal{N}_{X}(3.5,1.1)
$$

## Example 8

In this example, we compute success function of goal $q(Y)$ in Example 2. Fig. 3b shows the symbolic derivation for goal $q(Y)$. Success function of $r(Y)$ is $\delta_{1}(Y)+$ $\delta_{2}(Y)$, and success function of $s(Y)$ is $\delta_{2}(Y)+\delta_{3}(Y)$. Similarly, success function of $p(X, Y)$ is $\delta_{a}(X)\left(\delta_{1}(Y)+\delta_{2}(Y)\right)+\delta_{b}(X)\left(\delta_{2}(Y)+\delta_{3}(Y)\right)$. Now

$$
\psi_{q(Y)}=\mathbb{M}\left(\psi_{m s w(r v, X)} * \psi_{p(X, Y)}, X\right)
$$

Success function of $m s w(r v, X)$ is $0.3 \delta_{a}(X)+0.7 \delta_{b}(X)$. Join of $\psi_{m s w(r v, X)}$ and $\psi_{p(X, Y)}$ yields $0.3 \delta_{a}(X)\left(\delta_{1}(Y)+\delta_{2}(Y)\right)+0.7 \delta_{b}(X)\left(\delta_{2}(Y)+\delta_{3}(Y)\right)$. Finally, $\psi_{q(Y)}=$ $0.3\left(\delta_{1}(Y)+\delta_{2}(Y)\right)+0.7\left(\delta_{2}(Y)+\delta_{3}(Y)\right)$.

When $Y=1$, only $p(a, 1)$ is true. Thus $\psi_{q(1)}=0.3$. On the other hand, $\psi_{q(2)}=1.0$ as both $p(a, 2)$ and $p(b, 2)$ are true when $\mathrm{Y}=2$. Similarly, $\psi_{q(3)}=0.7$.

Complexity: Let $S_{i}$ denote the number of constrained PPDF terms in $\psi_{i} ; P_{i}$ denote the maximum number of product terms in any PPDF function in $\psi_{i}$; and $Q_{i}$ denote the maximum size of a constraint set $\left(C_{i}\right)$ in $\psi_{i}$. The time complexity of the two basic operations used in constructing a symbolic derivation is as follows.

# Proposition 3 (Time Complexity) 

The worst-case time complexity of $\operatorname{Join}\left(\psi_{i}, \psi_{j}\right)$ is $O\left(S_{i} * S_{j} *\left(P_{i} * P_{j}+Q_{i} * Q_{j}\right)\right)$.
The worst-case time complexity of $\mathbb{M}\left(\psi_{g}, V\right)$ is $O\left(S_{g} * P_{g}\right)$ when $V$ is discrete and $O\left(S_{g} *\left(P_{g}+Q_{g}\right)\right)$ when $V$ is continuous.

Note that when computing the success function of a goal in a derivation, the join operation is limited to joining the success function of a single msv or a single constraint set to the success function of a goal, and hence the parameters $S_{i}, P_{i}$, and $Q_{i}$ are typically small. The complexity of the size of success functions is as follows.

## Proposition 4 (Success Function Size)

For a goal $G$ and its symbolic derivation, the following hold:

1. The maximum number of product terms in any PPDF function in $\psi_{G}$ is linear in $\left|V_{c}(G)\right|$, the number of continuous variables in $G$.
2. The maximum size of a constraint set in a constrained PPDF function in $\psi_{G}$ is linear in $\left|V_{c}(G)\right|$.
3. The maximum number of constrained PPDF functions in any entry of $\psi_{G}$ is potentially exponential in the number of discrete random variables in the symbolic derivation.

The number of product terms and the size of constraint sets are hence independent of the length of the symbolic derivation. Note that for a program with only discrete random variables, there may be exponentially fewer symbolic derivations than concrete derivations. The compactness is only in terms of number of derivations and not the total size of the representations. In fact, for programs with only discrete random variables, there is a one-to-one correspondence between the entries in the tabular representation of success functions and PRISM's answer tables. For such programs, it is easy to show that the time complexity of the inference algorithm presented in this paper is same as that of PRISM.

Correctness of the Inference Algorithm: The technically complex aspect of correctness is the closure of the set of success functions w.r.t. join and marginalize operations. Proposition 1 and 2 state these closure properties. Definition 7 represents the inference algorithm for computing the success function of a goal. The distribution of a goal is formally defined in terms of the distribution semantics of extended PRISM programs and is computed using the inference algorithm.

# Theorem 5 

The success function of a goal computed by the inference algorithm represents the distribution of the answer to that goal.

Proof: Correctness w.r.t. distribution semantics follows from the definition of join and marginalize operations, and PRISM's independence and exclusiveness assumptions. We prove this by induction on derivation length $n$. For $n=1$, the definition of success function for base predicates gives a correct distribution.

Now let's assume that for a derivation of length $n$, our inference algorithm computes valid distribution. Let's assume that $G^{\prime}$ has a derivation of length $n$ and $G \rightarrow G^{\prime}$. Thus $G$ has a derivation of length $n+1$. We show that the success function of $G$ represents a valid distribution.

We compute $\psi_{G}$ using Definition 7 and it carries PRISM's assumption that an instance of a random variable occurs at most once in any derivation. More specifically, the PCR step marginalizes $\psi_{G^{\prime}}$ w.r.t. a set of variables $V\left(G^{\prime}\right)-V(G)$. Since according to PRISM's exclusiveness assumption the valuations of the set of variables are mutually exclusive, the marginalization operation returns a valid distribution. Analogously, the MSW/CONS step joins success functions, and the goals joined use independent random variables (following PRISM's assumption) for the join operation to correctly compute $\psi_{G}$ in this step. Thus $\psi_{G}$ represents a valid distribution.

## 6 Illustrative Example

In this section, we model Kalman filters (Russell and Norvig 2003) using logic programs. The model describes a random walk of a single continuous state variable $S_{t}$ with noisy observation $V_{t}$. The initial state distribution is assumed to be Gaussian with mean $\mu_{0}$, and variance $\sigma_{0}^{2}$. The transition and sensor models are Gaussian noises with zero means and constant variances $\sigma_{s}^{2}, \sigma_{v}^{2}$ respectively.

Fig. 6 shows a logic program for Kalman filter, and Fig. 7 shows the derivation for a query $k f(1, T)$. Note the similarity between this and hmm program (Fig. 1): only trans/emit definitions are different. We label the $i^{\text {th }}$ derivation step by $G_{i}$ which is used in the next subsection to refer to appropriate derivation step. Here, our goal is to compute filtered

```
kf(N, T) :-
    msw(init, S),
    kf_part(0, N, S, T).
kf_part(I, N, S, T) :-
    I < N, NextI is I+1,
    trans(S, I, NextS),
    emit(NextS, NextI, V),
    obs(NextI, V),
    kf_part(NextI, N, NextS, T).
kf_part(I, N, S, T) :-
    I=N, T=S.
trans(S, I, NextS) :-
    msw(trans_err, I, E),
    NextS = S + E.
emit(NextS, I, V) :-
    msw(obs_err, I, X),
    V = NextS + X.
```

step. Here, our goal is to compute filtered

Success Function Computation: Fig. 7 shows the bottom-up success function computation. Note that $\psi_{G_{12}}$ is same as $\psi_{G_{13}}$ except that $o b s(1, V)$ binds $V$ to an

![img-0.jpeg](img-0.jpeg)

Fig. 7: Symbolic derivation and success functions for $\mathrm{kf}(1, \mathrm{~T})$
observation $v_{1}$. Final step involves marginalization w.r.t. $S$,

$$
\begin{aligned}
\psi_{G_{1}} & =\mathbb{M}\left(\psi_{G_{2}}, S\right) \\
& =\mathcal{N}_{v_{1}-T}\left(0, \sigma_{v}^{2}\right) \cdot \mathcal{N}_{T}\left(\mu_{0}, \sigma_{0}^{2}+\sigma_{s}^{2}\right) \cdot(\text { using Equation } 2) \\
& =\mathcal{N}_{T}\left(v_{1}, \sigma_{v}^{2}\right) \cdot \mathcal{N}_{T}\left(\mu_{0}, \sigma_{0}^{2}+\sigma_{s}^{2}\right) \cdot(\text { constant shifting }) \\
& =\mathcal{N}_{T}\left(\frac{\left(\sigma_{0}^{2}+\sigma_{s}^{2}\right) * v_{1}+\sigma_{v}^{2} * \mu_{0}}{\sigma_{0}^{2}+\sigma_{s}^{2}+\sigma_{s}^{2}}, \frac{\left(\sigma_{0}^{2}+\sigma_{s}^{2}\right) * \sigma_{v}^{2}}{\sigma_{0}^{2}+\sigma_{s}^{2}+\sigma_{s}^{2}}\right) \\
& \text { (product of two Gaussian PDFs is another PDF) }
\end{aligned}
$$

which is the filtered distribution of state $T$ after seeing one observation, which is equal to the filtered distribution presented in (Russell and Norvig 2003).

# 7 Discussion and Concluding Remarks 

ProbLog and PITA (Riguzzi and Swift 2010), an implementation of LPAD, lift PRISM's mutual exclusion and independence restrictions by using a BDD-based representation of explanations. The technical development in this paper is based on PRISM and imposes PRISM's restrictions. However, we can remove these restrictions by using the following approach. In the first step, we materialize the set of symbolic derivations. In the second step, we can factor the derivations into a form analogous to BDDs such that random variables each path of the factored representation are independent, and distinct paths in the representation are mutually exclusive. For instance, consider two non-exclusive branches in a symbolic derivation tree, one of which has $\operatorname{msw}(\mathrm{r}, \mathrm{X})$ and the other that has $\operatorname{msw}(\mathrm{s}, \mathrm{Y})$. This will be factored such that one of the two, say $\operatorname{msw}\left(\mathrm{r}, \mathrm{X}^{\prime}\right)$ is done in common, with two branches: $X=X^{\prime}$ and $X \neq X^{\prime}$. The branch containing subgoal $\operatorname{msw}(\mathrm{s}, \mathrm{Y})$ is "anded" with the $X=X^{\prime}$ branch, and replicated as the $X \neq X^{\prime}$ branch, analogous to how BDDs are processed. The factored representation itself can be treated as symbolic derivations augmented with dis-equality constraints (i.e. of the form $X \neq e$ ). Note that the success function of an equality constraint $C$ is $\langle 1, C\rangle$. The success function of a dis-equality constraint $X \neq e$ is $\langle 1$, true $\rangle-\langle 1, X=e\rangle$, which is representable by extending our language of success functions to permit non-negative constants. The definitions of join and marginalize operations work with no change over the extended success functions, and the closure properties (Prop. 2) holds as well. Hence, success functions can be readily computed over the factored representation. A detailed discussion of this extension appears in (Islam 2012).

Note that the success function of a goal represents the likelihood of a successful derivation for each instance of a goal. Hence the probability measure computed by the success function is what PRISM calls inside probability. Analogously, we can define a function that represents the likelihood that a goal $G^{\prime}$ will be encountered in a symbolic derivation starting at goal $G$. This "call" function will represent the outside probability of PRISM. Alternatively, we can use the Magic Sets transformation (Bancilhon et al. 1986) to compute call functions of a program in terms of success functions of a transformed program. The ability to compute inside and outside probabilities can be used to infer smoothed distributions for temporal models.

For simplicity, in this paper we focused only on univariate Gaussians. However, the techniques can be easily extended to support multivariate Gaussian distributions, by extending the integration function (Defn. 5), and set_sw directives. We can also readily extend them to support Gamma distributions. More generally, the PDF functions can be generalized to contain Gaussian or Gamma density functions, such that variables are not shared between Gaussian and Gamma density functions. Again, the only change is to extend the integration function to handle PDFs of Gamma distribution.

The concept of symbolic derivations and success functions can be applied to parameter learning as well. We have developed an EM-based learning algorithm which permits us to learn the distribution parameters of extended PRISM programs with discrete as well as Gaussian random variables (Islam et al. 2012). Similar to

inference, our learning algorithm uses the symbolic derivation procedure to compute Expected Sufficient Statistics (ESS). The E-step of the learning algorithm involves computation of the ESSs of the random variables and the M-step computes the MLE of the distribution parameters given the ESS and success probabilities. Analogous to the inference algorithm presented in this paper, our learning algorithm specializes to PRISM's learning over programs without any continuous variables. For mixture model, the learning algorithm does the same computation as standard EM learning algorithm (Bishop 2006).

The symbolic inference and learning procedures enable us to reason over a large class of statistical models such as hybrid Bayesian networks with discrete childdiscrete parent, continuous child-discrete parent (finite mixture model), and continuous child-continuous parent (Kalman filter), which was hitherto not possible in PLP frameworks. It can also be used for hybrid models, e.g., models that mix discrete and Gaussian distributions. For instance, consider the mixture model example where st(a) is Gaussian but st(b) is a discrete distribution with values 1 and 2 with 0.5 probability each. The density of the mixture distribution can be written as $f(Z)=0.3 \mathcal{N}_{Z}(2.0,1.0)+0.35 \delta_{1.0}(Z)+0.35 \delta_{2.0}(Z)$. Thus the language can be used to model problems that lie outside traditional hybrid Bayesian networks.

We implemented the extended inference algorithm presented in this paper in the XSB logic programming system (Swift et al. 2012). The system is available at http://www.cs.sunysb.edu/ cram/contdist. This proof-of-concept prototype is implemented as a meta-interpreter and currently supports discrete and Gaussian distributions. The meaning of various probabilistic predicates (e.g., msw, values, set_sw) in the system are similar to that of PRISM system. This implementation illustrates how the inference algorithm specializes to the specialized techniques that have been developed for several popular statistical models such as HMM, FMM, Hybrid Bayesian Networks and Kalman Filters. Integration of the inference algorithm in XSB and its performance evaluation are topics of future work.

Acknowledgments. We thank the reviewers for valuable comments. This research was supported in part by NSF Grants CCF-1018459, CCF-0831298, and ONR Grant N00014-07-1-0928.

# 8 Appendix 

This section presents proof of Proposition 1.

## Property 6

Integrated form of a PPDF function with respect to a variable $V$ is a PPDF function, i.e.,

$$
\int_{-\infty}^{\infty} \prod_{k=1}^{m} \mathcal{N}_{\left(\overline{a_{k}}: \overline{X_{k}}+b_{k}\right)}\left(\mu_{k}, \sigma_{k}^{2}\right) d V=\alpha \prod_{l=1}^{m^{\prime}} \mathcal{N}_{\left(\overline{a_{l}}: \overline{X_{l}^{\prime}}\right)+b_{l}^{\prime}}\left(\mu_{l}^{\prime}, \sigma_{l}^{\prime 2}\right)
$$

where $V \in \overline{X_{k}}$ and $V \notin \overline{X_{l}^{\prime}}$.
(Proof)
The above proposition states that integrated form of a product of Gaussian PDF

functions with respect to a variable is a product of Gaussian PDF functions. We first prove it for a simple case involving two standard Gaussian PDF functions, and then generalize it for arbitrary number of Gaussians.

For simplicity, let us first compute the integrated-form of $\mathcal{N}_{V-X_{1}}(0,1) \cdot \mathcal{N}_{V-X_{2}}(0,1)$ w.r.t. variable $V$ where $X_{1}, X_{2}$ are linear combination of variables (except $V$ ). We make the following two assumptions:

1. The coefficient of $V$ is 1 in both PDFs.
2. Both PDFs are standard normal distributions (i.e., $\mu=0$ and $\sigma^{2}=1$ ).

Let $\phi$ denote the integrated form, i.e.,

$$
\begin{aligned}
\phi & =\int_{-\infty}^{\infty} \mathcal{N}_{V-X_{1}}(0,1) \cdot \mathcal{N}_{V-X_{2}}(0,1) d V \\
& =\int_{-\infty}^{\infty} \frac{1}{\sqrt{2 \pi}} \exp ^{-\frac{\left(V-X_{1}\right)^{2}}{2}} \cdot \frac{1}{\sqrt{2 \pi}} \exp ^{-\frac{\left(V-X_{2}\right)^{2}}{2}} d V \\
& =\int_{-\infty}^{\infty} \frac{1}{2 \pi} \exp ^{-\frac{1}{2}\left[\left(V-X_{1}\right)^{2}+\left(V-X_{2}\right)^{2}\right]} d V \\
& =\int_{-\infty}^{\infty} \frac{1}{2 \pi} \exp ^{-\frac{1}{2} \eta} d V
\end{aligned}
$$

Now

$$
\begin{aligned}
\eta & =\left(V-X_{1}\right)^{2}+\left(V-X_{2}\right)^{2} \\
& =2 \cdot V^{2}-2 \cdot V \cdot\left(X_{1}+X_{2}\right)+\left(X_{1}^{2}+X_{2}^{2}\right) \\
& =2\left[\left(V-\frac{X_{1}+X_{2}}{2}\right)^{2}+\left(\frac{X_{1}^{2}+X_{2}^{2}}{2}\right)-\left(\frac{X_{1}+X_{2}}{2}\right)^{2}\right] \\
& =2\left[\left(V-\frac{X_{1}+X_{2}}{2}\right)^{2}+g\right]
\end{aligned}
$$

where

$$
g=\left(\frac{X_{1}^{2}+X_{2}^{2}}{2}\right)-\left(\frac{X_{1}+X_{2}}{2}\right)^{2}=\frac{1}{4}\left(X_{1}-X_{2}\right)^{2}
$$

Thus the integrated form can be expressed as

$$
\begin{aligned}
\phi & =\int_{-\infty}^{\infty} \frac{1}{2 \pi} \exp ^{-\frac{1}{2} \cdot 2\left[\left(V-\frac{X_{1}+X_{2}}{2}\right)^{2}+g\right]} d V \\
& =\int_{-\infty}^{\infty} \frac{1}{2 \pi} \exp ^{-\frac{1}{2} \cdot 2 \cdot\left(V-\frac{X_{1}+X_{2}}{2}\right)^{2}} \cdot \exp ^{-\frac{1}{2} \cdot 2 \cdot g} d V \\
& =\frac{1}{2 \sqrt{\pi}} e \cdot x p^{-g} \int_{-\infty}^{\infty} \frac{1}{\sqrt{2 \cdot \pi \cdot \frac{1}{2}}} \exp ^{-\frac{\left(V-\frac{X_{1}+X_{2}}{2}\right)^{2}}{2 \cdot \frac{1}{2}}} d V \\
& =\frac{1}{2 \sqrt{\pi}} e \cdot x p^{-g} \text { (as integration over the whole area is 1) } \\
& =\frac{1}{\sqrt{2 \pi \cdot 2}} e \cdot x p^{-\frac{1}{4}\left(X_{1}-X_{2}\right)^{2}} \\
& =\mathcal{N}_{X_{1}-X_{2}}(0,2)
\end{aligned}
$$

Thus integrated form of a PPDF function is another PPDF function. Notice that the integrated form is a constant when $X 1=X 2$.

Generalization for arbitrary number of PDFs. Note that for any arbitrary number of PDFs in a PPDF function, $\eta=\sum\left(V-X_{i}\right)^{2}$ can be always written as $k[(V-$ $\beta)^{2}+g_{n}],$ where

$$
g_{n}=\frac{1}{n} \sum_{i=1}^{n} X_{i}^{2}-\frac{1}{n^{2}}\left(\sum_{i=1}^{n} X_{i}\right)^{2}
$$

For any arbitrary number of PDFs, we will prove the property on $g_{n}$. In other words, we will show that $g_{n}$ can be expressed as

$$
g_{n}=\frac{1}{n} \sum_{i=1}^{n} X_{i}^{2}-\frac{1}{n^{2}}\left(\sum_{i=1}^{n} X_{i}\right)^{2}=\frac{1}{n^{2}} \sum_{i \neq j, i<j}\left(X_{i}-X_{j}\right)^{2}
$$

which means integrated form of $n$ PDFs,

$$
\phi_{n}=\int_{-\infty}^{\infty} \prod_{i=1}^{n} \mathcal{N}_{V-X_{i}}(0,1) d V
$$

can be expressed as

$$
\phi_{n}=\alpha \exp ^{-g_{n}}=\alpha \prod_{i \neq j, i<j} \mathcal{N}_{X_{i}-X_{j}}
$$

# Proposition 7 

Let $f_{n}=\sum_{i=1}^{n} X_{i}$. Then, $f_{n}^{2}=\sum_{i=1}^{n} X_{i}^{2}+\sum_{i \neq j} X_{i} X_{j}$.

## Proof

We prove the proposition using induction. Let us assume that the above equation holds for $n$ variables. Now for $(n+1)^{t h}$ variable $X_{n+1}$,

$$
\begin{aligned}
f_{n+1}^{2} & =\left(\sum_{i=1}^{n+1} X_{i}\right)^{2} \\
& =\left(\left(\sum_{i=1}^{n} X_{i}\right)+X_{n+1}\right)^{2} \\
& =\left(\sum_{i=1}^{n} X_{i}\right)^{2}+X_{n+1}^{2}+2\left(X_{1}+\ldots+X_{n}\right) X_{n+1} \\
& =\sum_{i=1}^{n} X_{i}^{2}+\sum_{i \neq j, i=1}^{n} X_{i} X_{j}+X_{n+1}^{2}+2\left(X_{1}+\ldots+X_{n}\right) X_{n+1} \\
& \text { (using induction hypothesis) } \\
& =\sum_{i=1}^{n+1} X_{i}^{2}+\sum_{i \neq j} X_{i} X_{j}
\end{aligned}
$$

Now going back to proving equation 3, we first show that $g_{n}$ can be written in the following form

$$
g_{n}=\frac{1}{n} \sum_{i=1}^{n} X_{i}^{2}-\frac{1}{n^{2}}\left(\sum_{i=1}^{n} X_{i}\right)^{2}=\frac{1}{n^{2}}\left[(n-1) \sum_{i=1}^{n} X_{i}^{2}-\sum_{i \neq j} X_{i} X_{j}\right]
$$

The above equation can be proved by induction. It is easy to see that for $n=2$ the equation holds, as $g_{2}=\frac{1}{2} \sum_{i=1}^{2} X_{i}^{2}-\frac{1}{4}\left(\sum_{i=1}^{2} X_{i}\right)^{2}=\frac{1}{4}\left[X_{1}^{2}+X_{2}^{2}-X_{1} X_{2}-X_{2} X_{1}\right]$. Now

$$
\begin{aligned}
g_{n+1} & =\frac{1}{(n+1)} \sum_{i=1}^{n+1} X_{i}^{2}-\frac{1}{(n+1)^{2}} f_{n+1}^{2} \\
& =\frac{1}{(n+1)^{2}}\left[(n+1) \sum_{i=1}^{n+1} X_{i}^{2}-f_{n+1}^{2}\right] \\
& =\frac{1}{(n+1)^{2}}\left[(n+1) \sum_{i=1}^{n+1} X_{i}^{2}-\sum_{i=1}^{n+1} X_{i}^{2}-\sum_{i \neq j} X_{i} X_{j}\right] \\
& \text { (using Proposition 7) } \\
& =\frac{1}{(n+1)^{2}}\left[n \sum_{i=1}^{n+1} X_{i}^{2}-\sum_{i \neq j} X_{i} X_{j}\right]
\end{aligned}
$$

Thus $g_{n}=\frac{1}{n^{2}}\left[(n-1) \sum_{i=1}^{n} X_{i}^{2}-\sum_{i \neq j} X_{i} X_{j}\right]$.
Finally, we will prove that

$$
g_{n}=\frac{1}{n^{2}}\left[(n-1) \sum_{i=1}^{n} X_{i}^{2}-\sum_{i \neq j} X_{i} X_{j}\right]=\frac{1}{n^{2}} \sum_{i \neq j, i<j}\left(X_{i}-X_{j}\right)^{2}
$$

# Proposition 8 

Let $h_{n}=\sum_{i \neq j, i<j}\left(X_{i}-X_{j}\right)^{2}$. Then $h_{n}=(n-1) \sum_{i=1}^{n} X_{i}^{2}-\sum_{i \neq j} X_{i} X_{j}$.

## Proof

We use induction to prove the above proposition. Let $h_{n}$ holds for $n$ variables. Then for $(n+1)^{t h}$ variable,

$$
\begin{aligned}
h_{n+1} & =\sum_{i \neq j, i<j}\left(X_{i}-X_{j}\right)^{2} \\
& =h_{n}+\sum_{i=1}^{n}\left(X_{i}-X_{n+1}\right)^{2} \\
& =(n-1) \sum_{i=1}^{n} X_{i}^{2}-\sum_{i \neq j, i=1}^{n} X_{i} X_{j}+\sum_{i=1}^{n} X_{i}^{2}+n X_{n+1}^{2}-2 \sum_{i=1}^{n} X_{i} X_{n+1} \\
& =n \sum_{i=1}^{n+1} X_{i}^{2}-\sum_{i \neq j, i=1}^{n+1} X_{i} X_{j}
\end{aligned}
$$

Thus $g_{n}=\frac{1}{n^{2}} h_{n}=\frac{1}{n^{2}} \sum_{i \neq j, i<j}\left(X_{i}-X_{j}\right)^{2}$. Thus $\phi_{n}$ can be expressed as

$$
\phi_{n}=\alpha \exp ^{-g_{n}}=\alpha \prod_{i \neq j, i<j} \mathcal{N}_{X_{i}-X_{j}}
$$

Integrated-form with arbitrary constants: For any arbitrary mean, variance and coefficients of $V$,

$$
\begin{aligned}
\phi_{2} & =\int_{-\infty}^{\infty} \mathcal{N}_{a_{1} V-X_{1}}\left(\mu_{1}, \sigma_{1}^{2}\right) \mathcal{N}_{a_{2} V-X_{2}}\left(\mu_{2}, \sigma_{2}^{2}\right) d V \\
& =\mathcal{N}_{a_{2} X_{1}-a_{1} X_{2}}\left(a_{1} \mu_{2}-a_{2} \mu_{1}, a_{2}^{2} \sigma_{1}^{2}+a_{1}^{2} \sigma_{2}^{2}\right)
\end{aligned}
$$

And

$$
\phi_{n}=\alpha \prod_{i \neq j, i<j} \mathcal{N}_{a_{j} X_{i}-a_{i} X_{j}}\left(a_{i} \mu_{j}-a_{j} \mu_{i}, \sigma_{i j}^{2}\right)
$$

where

$$
\sigma_{i j}^{2}=\frac{\sum_{k=1}^{n} a_{k}^{2} \prod_{l \neq k, l=1}^{n} \sigma_{l}^{2}}{\prod_{k=1, k \neq i, j}^{n} \sigma_{k}^{2}}
$$

Note that the normalization constant is also adjusted appropriately in the integrated form.
