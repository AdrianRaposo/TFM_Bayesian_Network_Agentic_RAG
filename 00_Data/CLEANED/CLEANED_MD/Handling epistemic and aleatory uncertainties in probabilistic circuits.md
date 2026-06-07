# Handling epistemic and aleatory uncertainties in probabilistic circuits 

Federico Cerutti ${ }^{1,2}$ (D) $\cdot$ Lance M. Kaplan ${ }^{3} \cdot$ Angelika Kimmig ${ }^{4,5} \cdot$ Murat Şensoy ${ }^{6,7}$<br>Received: 15 May 2020 / Revised: 27 March 2021 / Accepted: 27 September 2021 /<br>Published online: 10 January 2022<br>(c) The Author(s), under exclusive licence to Springer Science+Business Media LLC, part of Springer Nature 2021


#### Abstract

When collaborating with an AI system, we need to assess when to trust its recommendations. If we mistakenly trust it in regions where it is likely to err, catastrophic failures may occur, hence the need for Bayesian approaches for probabilistic reasoning in order to determine the confidence (or epistemic uncertainty) in the probabilities in light of the training data. We propose an approach to Bayesian inference of posterior distributions that overcomes the independence assumption behind most of the approaches dealing with a large class of probabilistic reasoning that includes Bayesian networks as well as several instances of probabilistic logic. We provide an algorithm for Bayesian inference of posterior distributions from sparse, albeit complete, observations, and for deriving inferences and their confidences keeping track of the dependencies between variables when they are manipulated within the unifying computational formalism provided by probabilistic circuits. Each leaf of such circuits is labelled with a beta-distributed random variable that provides us with an elegant framework for representing uncertain probabilities. We achieve better estimation of epistemic uncertainty than state-of-the-art approaches, including highly engineered ones, while being able to handle general circuits and with just a modest increase in the computational effort compared to using point probabilities.


Keywords Bayesian learning $\cdot$ Probabilistic circuit $\cdot$ Imprecise probabilities

## 1 Introduction

Even in simple collaboration scenarios-like those in which an artificial intelligence (AI) system assists a human operator with predictions-the success of the team hinges on the human correctly deciding when to follow the recommendations of the AI system and when to override them (Bansal et al., 2019b). When that happens, the human has developed insights (i.e., a mental model) of when to trust the AI system with its recommendations

[^0]
[^0]:    Editors: Nikos Katzouris, Alexander Artikis, Luc De Raedt, Artur d’Avila Garcez, Sebastijan Dumančić, Ute Schmid, Jay Pujara.

    F Federico Cerutti
    federico.cerutti@unibs.it
    Extended author information available on the last page of the article

(Bansal et al., 2019b). If the human mistakenly trusts the AI system in regions where it is likely to err, catastrophic failures may occur. This is a strong argument in favour of Bayesian approaches to probabilistic reasoning: research in the intersection of AI and HCI has found that interaction improves when setting expectations right about what the system can do and how well it performs (Kocielnik et al., 2019; Bansal et al., 2019a). Guidelines have been produced (Amershi et al., 2019), and they recommend to Make clear what the system can do (G1), and Make clear how well the system can do what it can do (G2).

To identify such regions where the AI system is likely to err, we need to distinguish between (at least) two different sources of uncertainty: aleatory (or aleatoric), and epistemic uncertainty (Hora, 1996; Hüllermeier and Waegeman, 2019). Aleatory uncertainty refers to the variability in the outcome of an experiment which is due to inherently random effects (e.g. flipping a fair coin): no additional source of information but Laplace's daemon $^{1}$ can reduce such a variability. Epistemic uncertainty refers to the epistemic state of the agent using the model, hence its lack of knowledge that-in principle-can be reduced on the basis of additional data samples. Particularly when considering sparse data, the epistemic uncertainty around the learnt model can significantly affect decision making (Antonucci et al., 2014; Anderson et al., 2016), for instance when used for computing an expected utility (Von Neumann and Morgenstern, 2007).

In this paper, we propose an approach to probabilistic reasoning that manipulates joint distributions of probabilities without assuming independence between the single random variables (i.e. their covariances may not be zero), and without resorting to sampling. We operate within the unifying computational formalism provided by arithmetic circuits (von zur Gathen, 1988), sometimes named probabilistic circuits when manipulating probabilities, or simply circuits. This is clearly a novel contribution as the few approaches (Rashwan et al., 2016; Jaini et al., 2016; Cerutti et al., 2019) resorting to distribution estimation via moment matching, the very same technique we also use in this work, still assume independence between the random variables when computing their joint distribution using a probabilistic circuit. Instead, we provide an algorithm for Bayesian learning from sparsealbeit complete-observations, and for probabilistic inferences that keep track of the dependencies between variables when they are manipulated within the circuit. In particular, we focus on the large class of approaches to probabilistic reasoning that rely upon algebraic model counting (AMC) (Kimmig et al., 2017) (Sect. 2.1), which has been proven to encompass probabilistic inferences under Sato (1995)'s semantics, thus covering not only Bayesian networks (Sang et al. 2005), but also probabilistic logic programming approaches such as ProbLog (Fierens et al., 2015), and others as discussed by Cerutti and Thimm (2019). We can exploit the results of Darwiche and Marquis (2002) (Sect. 2.2) who studied the succinctness relations between various types of circuits and thus their applicability to model counting. Their work, indeed, directly refers to set of models of a propositional logic theory exactly as AMC does. To stress the applicability of this setting, circuit compilation techniques (Darwiche, 2004; Choi and Darwiche, 2013; Oztok and Darwiche, 2015) are behind state-of-the-art algorithms for (1) exact and approximate inference in discrete probabilistic graphical models (Chavira and Darwiche, 2008; Kisa et al., 2014; Friedman and den Broeck, 2018); and (2) probabilistic programs (Bellodi and Riguzzi, 2013; Fierens et al., 2015). Also, learning tractable circuits is the current method of choice for discrete density estimation (Gens and Domingos, 2013; Rooshenas and Lowd, 2014;

[^0]
[^0]:    1 "An intelligence that, at a given instant, could comprehend all the forces by which nature is animated and the respective situation of the beings that make it up" (Laplace, 1825, p.2).

2015; Vergari et al., 2019; Liang et al., 2017). Finally, Xu et al. (2018) also used circuits to enforce logical constraints on deep neural networks.

In this paper, we label each leaf of the circuit with a beta-distributed random variable (Sect. 3). The beta distribution is a well-defined theoretical framework that specifies a distribution of probabilities representing all the possible values of a probability when the exact value is unknown. In this way, the expected value of a beta-distributed random variable relates to the aleatory uncertainty of the phenomenon, and the variance to the epistemic uncertainty: the higher the variance, the less certain the machine is, thus targeting directly (Amershi et al., 2019, G1 and G2). In previous work (Cerutti et al., 2019) we provided operators for manipulating beta-distributed random variables under strong independence assumptions (Sect. 4). This paper significantly extends and improves our previous approach by eliminating the independence assumption in manipulating beta-distributed random variables within a circuit.

Indeed, our main contribution (Sect. 5) is an algorithm for reasoning over a circuit whose leaves are labelled with beta-distributed random variables, with the additional piece of information describing which of those are actually independent (Sect. 5.1). This is the input to an algorithm that shadows the circuit by superimposing a second circuit for computing the probability of a query conditioned on pieces of evidence (Sect. 5.2) in a single feed forward. While this at first might seems unnecessary, it is actually essential when inspecting the main algorithm that evaluates such a shadowed circuit (Sect. 5.3), where a covariance matrix plays an essential role by keeping track of the dependencies between random variables while they are manipulated within the circuit. We also include discussions on memory management of the covariance matrix in Sect. 5.4.

We evaluate our approach against a set of competing approaches in an extensive set of experiments detailed in Sect. 6, comparing against leading approaches to dealing with uncertain probabilities, notably: (1) Monte Carlo sampling; (2) our previous proposal (Cerutti et al., 2019) taken as representative of the class of approaches using moment matching with strong independence assumptions; (3) Subjective Logic (Jøsang, 2016), that provides an alternative representation of beta distributions as well as a calculus for manipulating them applied already in a variety of domains, e.g. (Jøsang et al., 2006; Moglia et al., 2012; Sensoy et al., 2018); (4) Subjective Bayesian Network (SBN) on circuits derived from singly-connected Bayesian networks (Ivanovska et al., 2015; Kaplan \& Ivanovska, 2016; Kaplan \& Ivanovska, 2018), that already showed higher performance against other traditional approaches dealing with uncertain probabilities, such as (5) Dempster-Shafer Theory of Evidence (Dempster, 1968; Smets, 1993), and (6) replacing single probability values with closed intervals representing the possible range of probability values (Zaffalon and Fagiuoli, 1998). We achieve better estimation of epistemic uncertainty than state-of-the-art approaches, including highly engineered ones for a narrow domain such as SBN, while being able to handle general circuits with just a modest increase in the computational effort compared to using point probabilities.

# 2 Background 

### 2.1 Algebraic model counting

Kimmig et al. (2017) introduce the task of algebraic model counting (AMC). AMC generalises weighted model counting (WMC) to the semiring setting and supports various types

of labels, including numerical ones as used in WMC, but also sets, polynomials, Boolean formulae, and many more. The underlying mathematical structure is that of a commutative semiring.

A semiring is a structure $\left(\mathcal{A}, \oplus, \otimes, e^{\oplus}, e^{\otimes}\right)$, where addition $\oplus$ and multiplication $\otimes$ are associative binary operations over the set $\mathcal{A}, \oplus$ is commutative, $\otimes$ distributes over $\oplus, e^{\oplus} \in \mathcal{A}$ is the neutral element of $\oplus, e^{\otimes} \in \mathcal{A}$ that of $\otimes$, and for all $a \in \mathcal{A}$, $e^{\oplus} \otimes a=a \otimes e^{\oplus}=e^{\oplus}$. In a commutative semiring, $\otimes$ is commutative as well.

Algebraic model counting is now defined as follows. Given:

- a propositional logic theory $T$ over a set of variables $\mathcal{V}$,
- a commutative semiring $\left(\mathcal{A}, \oplus, \otimes, e^{\oplus}, e^{\otimes}\right)$, and
- a labelling function $\rho: \mathcal{L} \rightarrow \mathcal{A}$, mapping literals $\mathcal{L}$ of the variables in $\mathcal{V}$ to elements of the semiring set $\mathcal{A}$,
compute

$$
\mathbf{A}(T)=\bigoplus_{l \in \mathcal{M}(T)} \bigotimes_{l \in I} \rho(l)
$$

where $\mathcal{M}(T)$ denotes the set of models of $T$.
Among others, AMC generalises the task of probabilistic inference according to Sato (1995)'s semantics (PROB), (Kimmig et al., 2017, Thm. 1), (Goodman, 1999; Eisner, 2002; Bacchus et al., 2009; Baras and Theodorakopoulos, 2010; Kimmig et al., 2011).

A query $q$ is a finite set of algebraic literals $q \subseteq \mathcal{L}$. We denote the set of interpretations where the query is true by $\mathcal{I}(q)$,

$$
\mathcal{I}(q)=\{I \mid I \in \mathcal{M}(T) \wedge q \subseteq I\}
$$

The label of query $q$ is defined ${ }^{2}$ as the label of $\mathcal{I}(q)$,

$$
\mathbf{A}(q)=\mathbf{A}(\mathcal{I}(q))=\bigoplus_{l \in \mathcal{I}(q)} \bigotimes_{l \in I} \rho(l)
$$

As both operators are commutative and associative, the label is independent of the order of both literals and interpretations.

In the context of this paper, we extend AMC for handling PROB of queries with evidence by introducing an additional division operator $\varnothing$ that defines the conditional label of a query as follows:

$$
\mathbf{A}(q \mid \boldsymbol{E}=\boldsymbol{e})=\mathbf{A}(\mathcal{I}(q \wedge \boldsymbol{E}=\boldsymbol{e})) \varnothing \mathbf{A}(\mathcal{I}(\boldsymbol{E}=\boldsymbol{e}))
$$

where $\mathbf{A}(\mathcal{I}(q \wedge \boldsymbol{E}=\boldsymbol{e})) \varnothing \mathbf{A}(\mathcal{I}(\boldsymbol{E}=\boldsymbol{e}))$ returns the label of $q \wedge \boldsymbol{E}=\boldsymbol{e}$ given the label of a set of pieces of evidence $\boldsymbol{E}=\boldsymbol{e}$.

In the case of probabilities as labels, i.e. $\rho(\cdot) \in[0,1]$, (5) presents the AMC-conditioning parametrisation $\mathcal{S}_{\rho}$ for handling PROB of (conditioned) queries:

[^0]
[^0]:    ${ }^{2}$ Albeit $\mathbf{A}$ has been introduced to operate over propositional logic theories, with a small abuse of notation we use it also for a finite set of algebraic literals, i.e. query, and a set of interpretations.

$$
\begin{aligned}
& \mathcal{A}=\mathbb{R}_{\geq 0} \\
& a \oplus b=a+b \\
& a \otimes b=a \cdot b \\
& e^{\oplus}=0 \\
& e^{\otimes}=1 \\
& \rho(f) \in[0,1] \\
& \rho(\neg f)=1-\rho(f) \\
& a \oslash b=\frac{a}{b}
\end{aligned}
$$

A naïve implementation of (4) is clearly exponential: Darwiche (2004) introduced the first method for deriving tractable circuits (d-DNNFs) that allow polytime algorithms for clausal entailment, model counting and enumeration. Also, while for a generic AMC it is true that $\mathbf{A}(q)$ might not be an un-normalised probability distribution, we will see in the following section that the decomposability and determinism restrictions to the circuits solve the problem.

# 2.2 Probabilistic circuits 

After defining what AMC is, we turn our attention to how we can compute it. From (1) we can see that it requires two operations $\oplus$ and $\otimes$ whose operands are elements of the commutative semiring $\mathcal{A}$ that are associated to literals in a propositional logic theory $T$. Not only, but we explicitly need to consider the set of models $\mathcal{M}(T)$ of such a propositional logic theory $T$ to compute the result of AMC.

AMC is thus computed by, informally speaking, multiplying and adding ${ }^{3}$ labels of propositions that belong to one of the models $\mathcal{M}(T)$ of a propositional theory $T$ : this is a hard problem. Therefore, the difficulty of AMC does not rely in the addition or multiplication, rather in computing the models of a theory. To illustrate this, the truth table for just variables of the form like $p \wedge q \vee r \wedge \neg s$ leads to $2^{4}$ rows.

To better manage the hard problem of computing the models $\mathcal{M}(T)$ of a propositional theory $T$, we can exploit the succinctness results of the knowledge compilation map by Darwiche and Marquis (2002). The restriction to two-valued variables allows us to directly compile AMC tasks to circuits without adding constraints on legal variable assignments to the theory.

In their knowledge compilation map, Darwiche and Marquis (2002) provide an overview of succinctness relationships between various types of circuits. Instead of focusing on classical, flat target compilation languages based on conjunctive or disjunctive normal forms, Darwiche and Marquis (2002) consider a richer, nested class based on representing propositional sentences using directed acyclic graphs: NNFs. A sentence in negation normal form (NNF) over a set of propositional variables $\mathcal{V}$ is a rooted, directed acyclic graph where each leaf node is labeled with true ( $T$ ), false ( $\perp$ ), or a literal of a variable in $\mathcal{V}$, and each internal node with disjunction $(\vee)$ or conjunction $(\wedge)$.

An NNF is decomposable if for each conjunction node $\bigwedge_{i=1}^{n} \phi_{i}$, no two children $\phi_{i}$ and $\phi_{j}$ share any variable.

[^0]
[^0]:    ${ }^{3}$ Formally speaking, AMC is computed by the using $\otimes$, the usual multiplication operation in PROB, and $\oplus$, the usual addition operation in PROB.

An NNF is deterministic if for each disjunction node $\bigvee_{i=1}^{n} \phi_{i}$, each pair of different children $\phi_{i}$ and $\phi_{j}$ is logically contradictory, that is $\phi_{i} \wedge \phi_{j} \vDash \perp$ for $i \neq j$. In other terms, only one child can be true at any time. ${ }^{4}$

The function eval specified in Algorithm 1 evaluates an NNF circuit for a commutative semiring $\left(\mathcal{A}, \oplus, \otimes, e^{\oplus}, e^{\otimes}\right)$ and labelling function $\rho$. Evaluating an NNF representation $N_{T}$ of a propositional theory $T$ for a semiring $\left(\mathcal{A}, \oplus, \otimes, e^{\oplus}, e^{\otimes}\right)$ and labelling function $\rho$ is a sound $A M C$ computation iff $\operatorname{EVAL}\left(N_{T}, \oplus, \otimes, e^{\oplus}, e^{\otimes}, \rho\right)=\mathbf{A}(T)$.

```
Algorithm 1 Evaluating an NNF circuit \(N\) for a commutative semiring
\(\left(\mathcal{A}, \oplus, \otimes, e^{\oplus}, e^{\otimes}\right)\) and labelling function \(\rho\).
    procedure \(\operatorname{Eval}\left(N, \oplus, \otimes, e^{\oplus}, e^{\otimes}, \rho\right)\)
        if \(N\) is a true node \(T\) then return \(e^{\otimes}\)
        if \(N\) is a false node \(\perp\) then return \(e^{\oplus}\)
        if \(N\) is a literal node \(l\) then return \(\rho(l)\)
        if \(N\) is a disjunction \(\bigvee_{i=1}^{m} N_{i}\) then
            \(\operatorname{return} \oplus_{i=1}^{m} \operatorname{EVAL}\left(N_{i}, \oplus, \otimes, e^{\oplus}, e^{\otimes}, \rho\right)\)
        end if
        if \(N\) is a conjunction \(\wedge_{i=1}^{m} N_{i}\) then
            \(\operatorname{return} \otimes_{i=1}^{m} \operatorname{EVAL}\left(N_{i}, \oplus, \otimes, e^{\oplus}, e^{\otimes}, \rho\right)\)
        end if
    end procedure
```

In particular, (Kimmig et al., 2017, Theorem 4) shows that evaluating a d-DNNF representation of the propositional theory $T$ for a semiring and labelling function with neutral $(\oplus, \rho)$ is a sound AMC computation. A semiring addition and labelling function pair $(\oplus, \rho)$ is neutral iff $\forall v \in \mathcal{V}: \rho(v) \oplus \rho(\neg v)=e^{\otimes}$.

Unless specified otherwise, in the following we will refer to d-DNNF circuits labelled with probabilities or distributions of probability simply as circuits, and any addition and labelling function pair $(\oplus, \rho)$ are neutral. Also, we extend the definition of the labelling function such that it also operates on $\{\perp, \top\}$, i.e. $\rho(\perp)=e^{\oplus}$ and $\rho(\top)=e^{\otimes}$.

Let us now introduce a graphical notation for circuits in this paper: Fig. 1 illustrates a d-DNNF circuit where each node has a unique integer (positive or negative) identifier. Moreover, circled nodes are labelled either with $\oplus$ for disjunction (a.k.a. $\oplus$-gates) or with $\otimes$ for conjunction (a.k.a. $\otimes$-gates). Leaves nodes are marked with a squared box and they are labelled with the literal, $T$ or $\perp$, as well as its label via the labelling function $\rho$.

Unless specified otherwise, in the following we will slightly abuse the notation by defining an $\bar{\cdot}$ operator both for variables and $T, \perp$, i.e. for $x \in \mathcal{V} \cup\{\perp, T\}$,

$$
\bar{x}=\left\{\begin{array}{ll}
\neg x & \text { if } x \in \mathcal{V} \\
\perp & \text { if } x=T \\
T & \text { if } x=\perp
\end{array}\right.
$$

and for elements of the set $\mathcal{A}$ of labels, s.t. $\overline{\rho(x)}=\rho(\bar{x})$.

[^0]
[^0]:    ${ }^{4}$ In the case $\phi_{i}$ and $\phi_{j}$ are seen as events in a sample space, the determinism can be equivalently rewritten as $\phi_{i} \cap \phi_{j}=\emptyset$ and hence $P\left(\phi_{i} \cap \phi_{j}\right)=0$.

![img-0.jpeg](img-0.jpeg)

Fig. 1 Circuit computing $p\left(\right.$ calls(john) ) for the Burglary example (Listing 1). Solid box for query, double box for evidence

Finally, each leaf node $i$ presents an additional parameter $\lambda_{i}$-i.e. the indicator variable cf. (Fierens et al. 2015)—that assumes values 0 or 1 , which allows one to reuse the same circuit for different purposes.

In the following, we will make use of a running example based upon the burglary example as presented in (Fierens et al., 2015, Example 6). In this way, we hope to better convey to the reader the value of our approach as the circuit derived from it using (Darwiche, 2004) will have a clear, intuitive meaning behind. However, our approach is independent from the system that employs circuit compilation for its reasoning process, as long as it can make use of d-DNNFs circuits. The d-DNNF circuit for our running example is depicted in Fig. 1 and has been derived by compiling the ProbLog (Fierens et al., 2015) code listed in Listing 1 (Fierens et al., 2015, Example 6) into a d-DNNF using the methods introduced in (Darwiche, 2004). For compactness, in the graph each literal of the program

is represented only by its initials, i.e. burglary becomes b, hears_alarm(john) becomes $h(j)$. ProbLog is an approach to augment ${ }^{5}$ Prolog programs (Kowalski, 1988; Bratko, 2001) annotating facts ${ }^{6}$ with probabilities: see Appendix A for an introduction. As discussed in (Fierens et al., 2015), the Prolog language admits a propositional representation of its semantics. For the example the propositional representation of Listing 1 is:

$$
\begin{aligned}
\text { alarm } & \leftrightarrow \text { burglary } \vee \text { earthquake } \\
\text { calls(john) } & \leftrightarrow \text { alarm } \wedge \text { hears_alarm(john) } \\
& \text { calls(john) }
\end{aligned}
$$

Figure 1 thus shows the result of the compilation of (7) in a circuit, annotated with a unique id that is either a number $x$ or $\bar{x}$ to indicate the node that represents the negation of the variable represented by node $x$; and with weights (probabilities) as per Listing 1.

The fact that calls (john) is true (see line 7 of Listing 1) translates in having $\lambda_{2}=1$ for the double boxed node with index 2 in Fig. 1-that indeed is labelled with the shorthand for calls (john), i.e. $c(j)$ —and $\lambda_{2}=0$ for the double boxed node with index $\overline{2}$ that is instead labelled with the shorthand for calls(john), i.e. $\overline{c(j)}$.

```
0.1::burglary.
0.2::earthquake.
0.7::hears_alarm(john).
alarm :- burglary.
alarm :- earthquake.
calls(john) :- alarm, hears_alarm(john).
evidence(calls(john)).
query(burglary).
```

Listing 1: Problog code for the Burglary example, originally Example 6 in (Fierens et al., 2015).

The $\lambda_{i}$ indicators modify the execution of the function eval (Alg. 1) in the way illustrated by Algorithm 2: note that Algorithm 2 is analogous to Algorithm 1 when all $\lambda_{i}=1$. Hence, in the following, when considering the function eval, we will be referring to the one defined in Algorithm 2.

[^0]
[^0]:    ${ }^{5}$ We refer readers interested in probabilistic augmentation of logical theories in general to (Cerutti and Thimm, 2019).
    ${ }^{6}$ Albeit ProbLog allows for rules to be annotated with probabilities: rules of the form p::h :- b are translated into $h$ :- b, t with $t$ a new fact of the form p::t.

Algorithm 2 Evaluating an NNF circuit $N$ for a commutative semiring $\left(\mathcal{A}, \oplus, \otimes, e^{\oplus}, e^{\otimes}\right)$ and labelling function $\rho$, considering indicators $\lambda_{i}$.

```
procedure \(\operatorname{Eval}\left(N, \oplus, \otimes, e^{\oplus}, e^{\otimes}, \rho\right)\)
    if \(N\) is a true node \(T\) then
        if \(\lambda_{N}=1\) then return \(e^{\otimes}\)
        else return \(e^{\oplus}\)
    end if
    if \(N\) is a false node \(\perp\) then return \(e^{\oplus}\)
    if \(N\) is a literal node \(l\) then
        if \(\lambda_{N}=1\) then return \(\rho(l)\)
        else return \(e^{\oplus}\)
    end if
    if \(N\) is a disjunction \(\bigvee_{i=1}^{m} N_{i}\) then
        return \(\oplus_{i=1}^{m} \operatorname{EVAL}\left(N_{i}, \oplus, \otimes, e^{\oplus}, e^{\otimes}, \rho\right)\)
    end if
    if \(N\) is a conjunction \(\bigwedge_{i=1}^{m} N_{i}\) then
        return \(\otimes_{i=1}^{m} \operatorname{EVAL}\left(N_{i}, \oplus, \otimes, e^{\oplus}, e^{\otimes}, \rho\right)\)
    end if
end procedure
```

Finally, the ProbLog program in Listing 1 queries the value of burglary, hence we need to compute the probability of burglary given calls (john),

$$
p(\text { burglary } \mid \text { calls(john }))=\frac{p(\text { burglary } \wedge \text { calls(john }))}{p(\text { calls(john }))}
$$

While the denominator of (8) is given by eval of the circuit in Fig. 1, we obtain the numerator $p$ (burglary $\wedge$ calls(john)) by evaluating the same circuit with $\lambda_{7}=0$ that is the parameter for the node labelled with burglary (see Fig. 2). eval on the circuit in Fig. 2 will thus return the value of the denominator in (8).

It is worth highlighting that computing $p$ (query $\mid$ evidences) for an arbirtrary query and arbirtrary set of evidences requires eval to be executed at least twice on slightly modified circuits.

In this paper, similarly to (Kisa et al., 2014), we are interested in learning the parameters of our circuit, i.e. the $\rho$ function for each of the leaves nodes, or $\rho$ in the following, thus representing it as a vector. We will learn $\rho$ from a set of examples, where each example is an instantiation of all propositional variables: for $n$ propositional variables, there are $2^{n}$ of such instantiations. In the case the circuit is derived from a logic program, an example is a complete interpretation of all the ground atoms. A complete dataset $\mathcal{D}$ is then a sequence (allowing for repetitions) of examples, each of those is a vector of instantiations of independent Bernoulli distributions with true but unknown parameter $\boldsymbol{\theta}$. Indeed, in this case, the dataset is assumed to have been sampled from the joint Bernoulli distribution represented by a circuit whose parameters are unknown. This, for complete training datasets, translates into observing independent Bernoulli distributions, one for each (pair) of leaves. Covariances will be not null only between one leaf and its negation (see Appendix C).

From this, the likelihood is thus:

$$
p(\mathcal{D} \mid \boldsymbol{\theta})=\prod_{i=1}^{|\mathcal{D}|} p\left(\boldsymbol{x}_{i} \mid \boldsymbol{\theta}\right)
$$

![img-1.jpeg](img-1.jpeg)

Fig. 2 Circuit computing $p($ burglary $\wedge$ calls( $j$ ohn $)$ ) for the Burglary example (Listing 1). Solid box for query, double box for evidence. White over black for the numeric value that has changed from Fig. 1. In particular, in this case, $\lambda_{\bar{Y}}$ for the node labelled with burglary is set to 0
where $\boldsymbol{x}_{i}$ represents the $i$-th example in the dataset $\mathcal{D}$. Differently, however, from (Kisa et al., 2014), we do not search for a maximum likelihood solution of this problem, rather we provide a Bayesian analysis of it in Sect. 3.

The following analysis provides the distribution of the probabilities (second-order probabilities) for each propositional variable. For complete datasets, their joint distributions is factorised into probabilities on individual variables, meaning that the second-order probabilities for the propositional variables are statistically independent (see Appendix C). Nevertheless, it is shown that second-order probabilities of a variable and its negation are correlated because the first-order probabilities (i.e. the expected values of the distributions) sum up to one. For complete datasets, the covariances at the leaves are only non-zero between a variable and its negation.

In this paper, we propose an inference process that does not assume independent second order probabilities. Indeed, when training using incomplete data-i.e. with not all variable values visible during training-the random variables associated to the leaves of the circuits are no longer independent, hence they can have non-null covariance. The derivations of these correlations during the learning process with partial observations is left for future work. Nevertheless, the proposed inference method can accommodate such correlations without any modifications.

This seamless integration of covariance information is one of our main contributions, that separates our approach from the literature on Bayesian approach to learning parameters in circuits (Jaini et al., 2016; Rashwan et al., 2016; Zhao et al.,2016a; Zhao et al., 2016b; Trapp et al., 2019; Vergari et al., 2019). In addition, similarly to (Rashwan et al., 2016; Jaini et al., 2016) we also apply the idea of moment matching instead of using sampling.

# 3 A Bayesian account of uncertain probabilities 

Let us now expand further (9): for simplicity, let us consider here only the case of a single propositional variable, i.e. a single binary random variable $x \in\{0,1\}$, e.g. flipping coin, not necessary fair, whose probability is thus conditioned by a parameter $0 \leq \theta \leq 1$ :

$$
p(x=1 \mid \theta)=\theta
$$

The probability distribution over $x$ is known as the Bernoulli distribution:

$$
\operatorname{Bern}(x \mid \theta)=\theta^{x}(1-\theta)^{1-x}
$$

Given a data set $\mathcal{D}$ of i.i.d. observations $\left(x_{1}, \ldots, x_{N}\right)^{\mathrm{T}}$ drawn from the Bernoulli with parameter $\theta$, which is assumed unknown, the likelihood of data given $\theta$ is:

$$
p(\mathcal{D} \mid \theta)=\prod_{n=1}^{N} p\left(x_{n} \mid \theta\right)=\prod_{n=1}^{N} \theta^{x_{n}}(1-\theta)^{1-x_{n}}
$$

To develop a Bayesian analysis of the phenomenon, we can choose as prior the beta distribution, with parameters $\boldsymbol{\alpha}=\left\langle\alpha_{x}, \alpha_{\bar{x}}\right\rangle, \alpha_{x} \geq 1>0$ and $\alpha_{\bar{x}} \geq 1>0$, that is conjugate to the Bernoulli:

$$
\operatorname{Beta}(\theta \mid \boldsymbol{\alpha})=\frac{\Gamma\left(\alpha_{x}+\alpha_{\bar{x}}\right)}{\Gamma\left(\alpha_{x}\right) \Gamma\left(\alpha_{\bar{x}}\right)} \theta^{\alpha_{x}-1}(1-\theta)^{\alpha_{\bar{x}}-1}
$$

where

$$
\Gamma(t) \equiv \int_{0}^{\infty} u^{t-1} e^{-u} \mathrm{~d} u
$$

is the gamma function.
Given a beta-distributed random variable $X$,

$$
s_{X}=\alpha_{x}+\alpha_{\bar{x}}
$$

is its Dirichlet strength and

$$
\mathbb{E}[X]=\frac{\alpha_{x}}{s_{X}}
$$

is its expected value. From (15) and (16) the beta parameters can equivalently be written as:

$$
\boldsymbol{\alpha}_{X}=\left\langle\mathbb{E}[X] s_{X},(1-\mathbb{E}[X]) s_{X}\right\rangle
$$

The variance of a beta-distributed random variable $X$ is

$$
\operatorname{var}[X]=\operatorname{var}[1-X]=\frac{\mathbb{E}[X](1-\mathbb{E}[X])}{s_{X}+1}
$$

and because $X+(1-X)=1$, it is easy to see that

$$
\operatorname{cov}[X, 1-X]=-\operatorname{var}[X]
$$

From (18) we can rewrite $s_{X}(15)$ as

$$
s_{X}=\frac{\mathbb{E}[X](1-\mathbb{E}[X])}{\operatorname{var}[X]}-1
$$

Considering a beta distribution prior and the binomial likelihood function, and given $N$ observations of $x$ such that for $r$ observations $x=1$ and for $s=N-r$ observations $x=0$

$$
p\left(\theta \mid \mathcal{D}, \boldsymbol{\alpha}^{0}\right)=\frac{p(\mathcal{D} \mid \theta) p\left(\theta \mid \boldsymbol{\alpha}^{0}\right)}{p(\mathcal{D})} \propto \theta^{r+\alpha_{x}^{0}-1}(1-\theta)^{s+\alpha_{x}^{0}-1}
$$

Hence $p\left(\theta \mid r, s, \boldsymbol{\alpha}^{0}\right)$ is another beta distribution such that after normalization via $p(\mathcal{D})$,

$$
p\left(\theta \mid r, s, \boldsymbol{\alpha}^{0}\right)=\frac{\Gamma\left(r+\alpha_{x}^{0}+s+\alpha_{x}^{0}\right)}{\Gamma\left(r+\alpha_{x}^{0}\right) \Gamma\left(s+\alpha_{x}^{0}\right)} \theta^{r+\alpha_{x}^{0}-1}(1-\theta)^{s+\alpha_{x}^{0}-1}
$$

We can specify the parameters for the prior we are using for deriving our beta distributed random variable $X$ as $\boldsymbol{\alpha}^{0}=\left\langle a_{X} W,\left(1-a_{X}\right) W\right\rangle$ where $a_{X}$ is the prior assumption, i.e. $p(x=1)$ in the absence of observations; and $W>0$ is a prior weight indicating the strength of the prior assumption. Unless specified otherwise, in the following we will assume $\forall X, a_{X}=0.5$ and $W=2$, so to have an uninformative, uniformly distributed, prior.

The complete dataset $\mathcal{D}$ is modelled as samples from independent Bernoulli distributions. As such, the posterior factors as a product of beta distributions representing the posterior distribution for each fact or rule as in (22) for a single fact (see Appendix C for further details). This posterior distribution enables the computation of the means and covariances for the leaves of the circuit, and because it factors, the different variables are statistically independent leading to zero covariances. Only the leaves associated to a variable and its complement exhibit nonzero covariance via (19). Now, the means and covariances of the leaves can be propagated through the circuit to determine the distribution of the queried conditional probability as described in Sect. 5.

Given an inference, like the conditioned query of our running example (8), we approximate its distribution by a beta distribution by finding the corresponding Dirichlet strength to match the computed variance. Given a random variable $Z$ with known mean $\mathbb{E}[Z]$ and variance $\operatorname{var}[Z]$, we can use the method of moments and (20) to determine the $\boldsymbol{\alpha}$ parameters of a beta-distributed variable approximation $Z^{\prime}$ with mean $\mathbb{E}\left[Z^{\prime}\right]=\mathbb{E}[Z]$. To ensure that the

approximated variable can be seen as a posterior beta distribution and thus that its parameters can be interpreted as observations pro and against a phenomenon further to a Bayesian update starting with a prior $\boldsymbol{\alpha}^{0},{ }^{7}$ we need to impose a restriction on such a Dirichlet strength to ensure that, for the approximated random variable $Z^{\prime}, \boldsymbol{\alpha}_{Z^{\prime}} \geq \boldsymbol{\alpha}^{0}$ :

$$
s_{Z^{\prime}}=\max \left\{\frac{\mathbb{E}[Z](1-\mathbb{E}[Z])}{\operatorname{var}[Z]}-1, \frac{W a_{Z}}{\mathbb{E}[Z]}, \frac{W\left(1-a_{Z}\right)}{(1-\mathbb{E}[Z])}\right\}
$$

To summarise, each time we use the method of moments to approximate a random variable $Z$ with a beta-distributed random variable $Z^{\prime}$ such that $\mathbb{E}\left[Z^{\prime}\right]=\mathbb{E}[Z]$ and $\operatorname{var}\left[Z^{\prime}\right] \cong \operatorname{var}[Z]$. The approximation of the variance is computed using (18), that bounds together variance and the Dirichlet strength, and the constraint on the Dirichlet strength added by (23).

# 3.1 Subjective logic 

Subjective logic (Jøsang, 2016) provides (1) an alternative, more intuitive, way of representing the parameters of beta-distributed random variables, and (2) a set of operators for manipulating them that we use to compare against our proposal in an empirical evaluation in Sect. 6. Our proposal, in fact, is inspired by subjective logic, which approximates Bayesian reasoning via a least commitment principle, i.e., matching the expected values, but then maximising the variance. Contrarily, in our approach not only we match the expected values but also the variances.

A subjective opinion about a proposition $X$ is a tuple $\omega_{X}=\left\langle b_{X}, d_{X}, u_{X}, a_{X}\right\rangle$, representing the belief, disbelief and uncertainty that $X$ is true at a given instance, and, as above, $a_{X}$ is the prior probability that $X$ is true in the absence of observations. These values are nonnegative and $b_{X}+d_{X}+u_{X}=1$. The projected probability $p(x)=b_{X}+u_{X} \cdot a_{X}$, provides an estimate of the ground truth probability $\theta$.

The mapping from a beta-distributed random variable $X$ with parameters $\boldsymbol{\alpha}_{X}=\left\langle\alpha_{x}, \alpha_{\bar{x}}\right\rangle$ to a subjective opinion is:

$$
\omega_{X}=\left\langle\frac{\alpha_{x}-W a_{X}}{s_{X}}, \frac{\alpha_{\bar{x}}-W\left(1-a_{X}\right)}{s_{X}}, \frac{W}{s_{X}}, a_{X}\right\rangle
$$

With this transformation, the mean of $X$ is equivalent to the projected probability $p(x)$, and the Dirichlet strength is inversely proportional to the uncertainty of the opinion:

$$
\mathbb{E}[X]=p(x)=b_{X}+u_{X} a_{X}, \quad s_{X}=\frac{W}{u_{X}}
$$

Conversely, a subjective opinion $\omega_{X}$ translates directly into a beta-distributed random variable with:

$$
\boldsymbol{\alpha}_{X}=\left\langle\frac{W}{u_{X}} b_{X}+W a_{X}, \frac{W}{u_{X}} d_{X}+W\left(1-a_{X}\right)\right\rangle
$$

[^0]
[^0]:    ${ }^{7}$ This is also needed by Subjective Logic (SL) (Jøsang, 2016) discussed in Sect. B, from which this work was inspired.

Subjective logic is a framework that includes various operators to indirectly determine opinions from various logical operations. In particular, we will make use of $\boxplus_{S L}, \boxtimes_{S L}$, and $\boxtimes_{S L}$, resp. summing, multiplying, and dividing two subjective opinions as they are defined in (Jøsang, 2016) (Appendix B). Those operators aim at faithfully matching the projected probabilities: for instance the multiplication of two subjective opinions $\omega_{X} \boxtimes_{S L} \omega_{Y}$ results in an opinion $\omega_{Z}$ such that $p(z)=p(x) \cdot p(z)$.

# 4 AMC-conditioning parametrisation with strong independence assumptions 

Building upon our previous work (Cerutti et al., 2019), we allow manipulation of imprecise probabilities as labels in our circuits. Figure 3 shows an example of the circuits we will be manipulating, where probabilities from the circuit depicted in Fig. 1 have been replaced by uncertain probabilities represented as beta-distributed random variables and formalised as SL opinions, in a shorthand format listing only belief and uncertainty values.

### 4.1 SL AMC-conditioning parametrisation with strong independence assumptions

The straightforward approach, we first introduced in (Cerutti et al., 2019), to derive an AMC-conditioning parametrisation under complete independence assumptions at each step of the evaluation of the probabilistic circuit using subjective logic, is to use the operators $\boxplus, \boxtimes$, and $\boxtimes$. This gives rise to the SL AMC-conditioning parametrisation $\mathcal{S}_{\mathrm{SL}}$, defined as follows:

$$
\begin{aligned}
& \mathcal{A}_{\mathrm{SL}}=\mathbb{R}_{\geqslant 0}^{4} \\
& a \oplus_{\mathrm{SL}} b=\left\{\begin{array}{ll}
a & \text { if } b=e^{\oplus_{\mathrm{SL}}} \\
b & \text { if } a=e^{\oplus_{\mathrm{SL}}} \\
a \boxplus_{\mathrm{SL}} b & \text { otherwise }
\end{array}\right. \\
& a \otimes_{\mathrm{SL}} b=\left\{\begin{array}{ll}
a & \text { if } b=e^{\otimes \mathrm{SL}} \\
b & \text { if } a=e^{\otimes_{\mathrm{SL}}} \\
a \boxtimes_{\mathrm{SL}} b & \text { otherwise }
\end{array}\right. \\
& e^{\oplus_{\mathrm{SL}}}=\langle 0,1,0,0\rangle \\
& e^{\otimes_{\mathrm{SL}}}=\langle 1,0,0,1\rangle \\
& \rho_{\mathrm{SL}}\left(f_{i}\right)=\left\langle b_{f_{i}}, d_{f_{i}}, u_{f_{i}}, a_{f_{i}}\right\rangle \\
& \rho_{\mathrm{SL}}\left(\neg f_{i}\right)=\left\langle d_{f_{i}}, b_{f_{i}}, u_{f_{i}}, 1-a_{f_{i}}\right\rangle \\
& a \oslash_{\mathrm{SL}} b=\left\{\begin{array}{ll}
a & \text { if } b=e^{\otimes_{\mathrm{SL}}} \\
a \boxtimes_{\mathrm{SL}} b & \text { if defined } \\
\langle 0,0,1,0.5\rangle & \text { otherwise }
\end{array}\right.
\end{aligned}
$$

Note that $\left\langle\mathcal{A}_{\mathrm{SL}}, \oplus_{\mathrm{SL}}, \otimes_{\mathrm{SL}}, e^{\oplus_{\mathrm{SL}}}, e^{\otimes_{\mathrm{SL}}}\right\rangle$ does not form a commutative semiring in general. If we consider only the projected probabilities-i.e. the means of the associated beta

![img-2.jpeg](img-2.jpeg)

Fig. 3 Variation on the circuit represented in Fig. 1 with leaves labelled with imprecise probabilities represented as Subjective Logic opinions, listing only $b_{X}$ and $u_{X}: d_{X}=1-b_{X}-u_{X}$, and $a_{X}=0.5$. Solid box for query, double box for evidence
distributions-then $\boxplus$ and $\boxtimes$ are indeed commutative, associative, and $\boxtimes$ distributes over $\boxplus$. However, the uncertainty of the resulting opinion depends on the order of operands.

# 4.2 Moment Matching AMC-conditioning parametrisation with strong independence assumptions 

In (Cerutti et al., 2019) we derived another set of operators operating with moment matching: they aim at maintaining a stronger connection to beta distribution as the result of the manipulation. Indeed, while SL operators try to faithfully characterise the projected probabilities, they employ an uncertainty maximisation principle to limit the belief commitments, hence they have a looser connection to the beta distribution. Instead, in (Cerutti et al., 2019) we first represented beta distributions (and thus also SL opinions) not parametric in $\boldsymbol{\alpha}$, but rather parametric on mean and variance. Hence we proposed operators that manipulate means and variances, and then we transformed them back into beta distributions by moment matching.

In (Cerutti et al., 2019) we chose to represent all labels-not only of leaves-as beta distributions. Since the sum (and in the following the product as well) of two beta random variables is not necessarily a beta random variable, we follow (Kaplan and Ivanovska, 2018) and approximate the result as a beta distribution via moment matching on mean and variance.

Given $X$ and $Y$ independent beta-distributed random variables represented by the subjective opinion $\omega_{X}$ and $\omega_{Y}$, the sum of $X$ and $Y\left(\omega_{X} \square^{\beta} \omega_{Y}\right)$ is defined as the beta-distributed random variable $Z$ such that:

$$
\mathbb{E}[Z]=\mathbb{E}[X+Y]=\mathbb{E}[X]+\mathbb{E}[Y]
$$

and

$$
\sigma_{Z}^{2}=\sigma_{X+Y}^{2}=\sigma_{X}^{2}+\sigma_{Y}^{2}
$$

$\omega_{Z}=\omega_{X} \square^{\beta} \omega_{Y}$ can then be obtained as discussed in Sect. 3, taking (23) into consideration. The same applies for the following operators as well.

The product operator between two independent beta-distributed random variables $X$ and $Y$ is then defined as the beta-distributed random variable $Z$ such that $\mathbb{E}[Z]=\mathbb{E}[X Y]$ and $\sigma_{Z}^{2}=\sigma_{X Y}^{2}$. Given $X$ and $Y$ independent beta-distributed random variables represented by the subjective opinion $\omega_{X}$ and $\omega_{Y}$, the product of $X$ and $Y\left(\omega_{X} \square^{\beta} \omega_{Y}\right)$ is defined as the betadistributed random variable $Z$ such that:

$$
\mathbb{E}[Z]=\mathbb{E}[X Y]=\mathbb{E}[X] \mathbb{E}[Y]
$$

and

$$
\sigma_{Z}^{2}=\sigma_{X Y}^{2}=\sigma_{X}^{2}(\mathbb{E}[Y])^{2}+\sigma_{Y}^{2}(\mathbb{E}[X])^{2}+\sigma_{X}^{2} \sigma_{Y}^{2}
$$

Finally, the conditioning-division operator between two independent beta-distributed random variables $X$ and $Y$, represented by subjective opinions $\omega_{X}$ and $\omega_{Y}$, is the beta-distributed random variable $Z$ such that $\mathbb{E}[Z]=\mathbb{E}\left[\frac{X}{Y}\right]$ and $\sigma_{Z}^{2}=\sigma_{Z}^{2}$. Given $\omega_{X}=\left\langle b_{X}, d_{X}, u_{X}, a_{X}\right\rangle$ and $\omega_{Y}=\left\langle b_{Y}, d_{Y}, u_{Y}, a_{Y}\right\rangle$ subjective opinions such that X and Y are beta-distributed random variables, the conditioning-division of $X$ by $Y^{\prime}\left(\omega_{X} \square^{\beta} \omega_{Y}\right)$ is defined as the betadistributed random variable $Z$ such that:

$$
\mathbb{E}[Z]=\mathbb{E}\left[\frac{X}{Y}\right]=\mathbb{E}[X] \mathbb{E}\left[\frac{1}{Y}\right] \simeq \frac{\mathbb{E}[X]}{\mathbb{E}[Y]}
$$

and $^{8}$

$$
\sigma_{Z}^{2} \simeq(\mathbb{E}[Z])^{2}(1-\mathbb{E}[Z])^{2}\left(\frac{\sigma_{X}^{2}}{(\mathbb{E}[X])^{2}}+\frac{\sigma_{Y}^{2}+\sigma_{X}^{2}}{(\mathbb{E}[Y]-\mathbb{E}[X])^{2}}+\frac{2 \sigma_{X}^{2}}{\mathbb{E}[X](\mathbb{E}[Y]-\mathbb{E}[X])}\right)
$$

Similarly to (27), the moment matching AMC-conditioning parametrisation $\mathcal{S}^{\beta}$ is defined as follows:

[^0]
[^0]:    ${ }^{8}$ Please note that (33) corrects a typo that is present in its version in (Cerutti et al., 2019).

$$
\begin{aligned}
& \mathcal{A}^{\beta}=\mathbb{R}_{\geqslant 0}^{4} \\
& a \oplus^{\beta} b=a \boxplus^{\beta} b \\
& a \otimes^{\beta} b=a \boxtimes^{\beta} b \\
& e^{\oplus^{\beta}}=\langle 1,0,0,0.5\rangle \\
& e^{\otimes^{\beta}}=\langle 0,1,0,0.5\rangle \\
& \rho^{\beta}\left(f_{i}\right)=\left\langle b_{f_{i}}, d_{f_{i}}, u_{f_{i}}, a_{f_{i}}\right\rangle \in[0,1]^{4} \\
& \rho^{\beta}\left(\neg f_{i}\right)=\left\langle d_{f_{i}}, b_{f_{i}}, u_{f_{i}}, 1-a_{f_{i}}\right\rangle \\
& a \oslash^{\beta} b=a \boxtimes^{\beta} b
\end{aligned}
$$

As per (27), also $\left\langle\mathcal{A}^{\beta}, \oplus^{\beta}, \otimes^{\beta}, e^{\oplus^{\beta}}, e^{\otimes^{\beta}}\right\rangle$ is not in general a commutative semiring. Means are correctly matched to projected probabilities, therefore for them $\mathcal{S}^{\beta}$ actually operates as a semiring. However, for what concerns variance, by using (31) and (29)—thus under independence assumption-the product is not distributive over addition: $\operatorname{var}[X(Y+Z)]=$ $\operatorname{var}[X](\mathbb{E}[Y]+\mathbb{E}[Z])^{2}+(\operatorname{var}[Y]+\operatorname{var}[Z]) \mathbb{E}[X]^{2}+\operatorname{var}[X](\operatorname{var}[Y]+\operatorname{var}[Z]) \neq \operatorname{var}[X](\mathbb{E}[Y]^{2}$ $+\mathbb{E}[Z]^{2})+(\operatorname{var}[Y]+\operatorname{var}[Z]) \mathbb{E}[X]^{2}+\operatorname{var}[X](\operatorname{var}[Y]+\operatorname{var}[Z])=\operatorname{var}[(X Y)+(X Z)]$.

To illustrate the discrepancy, let's consider node 6 in Fig. 3: the disjunction operator there is summing up probabilities that are not statistically independent, despite the independence assumption used in developing the operator. Due to the dependencies between nodes in the circuit, the error grows during propagation, and then the numerator and denominator in the conditioning operator exhibit strong correlation due to redundant operators. Therefore, (33) introduces further error leading to an overall inadequate characterisation of variance. The next section reformulates the operations to account for the existing correlations.

# 5 CPB: covariance-aware probabilistic inference with beta-distributed random variables 

We now propose an entirely novel approach to the AMC-conditioning problem that considers the covariances between the various distributions we are manipulating. Indeed, our approach for computing Covariance-aware Probabilistic entailment with beta-distributed random variables $\operatorname{CPB}$ is designed to satisfy the total probability theorem, and in particular to enforce that for any $X$ and $Y$ beta-disributed random variables,

$$
\operatorname{var}[(Y \otimes X) \oplus(Y \otimes \bar{X})]=\operatorname{var}[Y]
$$

Algorithm 3 provides an overview of $\overline{\mathrm{CPB}}$, that comprises three stages: (1) pre-processing; (2) circuit shadowing; and (3) evaluation. In particular, we associate each node in the circuit with a beta distribution that gives us a distribution of values between 0 and 1 that can be interpreted as a measure of imprecise probabilities, i.e., a second-order probability. The determination of the distributions is through moment matching via the first and second moments through (18) and (20). Effectively, the collection of nodes are treated as

Table 1 Associative table for the aProbLog code in Listing 2


multivariate Gaussian characterised by a mean vector and covariance matrix that it computed via the propagation process described below. When analysing the distribution for particular node (via marginalisation of the Gaussian), it is approximated via the best-fitting beta distribution through moment-matching.

# 5.1 Pre-processing 

We assume that the circuit we are receiving has the leaves labelled with unique identifiers of beta-distributed random variables. We also allow for the specification of the covariance matrix between the beta-distributed random variables, bearing in mind that $\operatorname{cov}[X, 1-X]=-\operatorname{var}[X]$, cf. (18) and (19). In our running example, we assume the ProbLog code from Listing 1 has been transformed into the aProbLog ${ }^{9}$ code in Listing 2.

We also expect there is a table associating the identifier with the actual value of the betadistributed random variable. In the following, we assume that $\omega_{1}$ is a reserved indicator for the $\operatorname{Beta}(\infty, 1.00)$ (in Subjective Logic term $\langle 1.0,0.0,0.0,0.5\rangle$ ). For instance, Table 1 provides the associations for code in Listing 2, and Table 2 the covariance matrix for those beta-distributed random variables that we assume being learnt from complete observations of independent random variables, and hence the posterior beta-distributed random variables are also independent (cf. Appendix C).

Algorithm 3 Solving the PROB problem on a circuit $N_{A}$ labelled with identifier of beta-distributed random variables and the associative table $A$, and covariance matrix $C_{A}$.

```
procedure CovProbBeta \(\left(N_{A}, C_{A}\right)\)
    \(\overline{N_{A}}:=\operatorname{ShadowCircuit}\left(N_{A}\right)\)
    return EvalCovProbBeta \(\left(\widehat{N_{A}}, C_{A}\right)\)
end procedure
```

[^0]
[^0]:    ${ }^{9}$ aProbLog (Kimmig et al., 2011) is the algebraic version of ProbLog that allows for arbitrary labels to be used.

Table 2 Covariance matrix for the associative table (Table 1) under the assumption that all the beta-distributed random variables are independent each other. We use a short-hand notation for clarity: $\sigma_{i}^{2}=\operatorname{cov}\left[\omega_{i}\right]$. Zeros are omitted


1
$\omega_{2}$ : :burglary.
2
$\omega_{3}:$ :earthquake.
3
$\omega_{4}:$ :hears_alarm(john).
4 alarm :- burglary.
5 alarm :- earthquake.
6 calls(john) :- alarm, hears_alarm(john).
7 evidence(calls(john)).
8 query(burglary).
Listing 2: Problog code for the Burglary example with unique identifier for the random variables associated to the database, originally Example 6 in (Fierens et al., 2015)

# 5.2 Circuit shadowing 

We then augment the circuit adding shadow nodes to superimpose a second circuit to enable the possibility to assess, in a single forward pass, both $p($ query $\wedge$ evidence $)$ and $p$ (evidence). This can provide a benefit time-wise at the expense of memory, but more importantly it simplifies the bookkeeping of indexes in the covariance matrix as we will see below. The pseudocode is provided in Appendix D, Algorithm 5.

Figure 4 depicts the result of such an algorithm applied to our running example. The algorithm begins by focusing on the node that identifies the negation of the query we want to evaluate with this circuit, that we mark with $\overline{\mathrm{QNODE}\left(N_{A}\right)}$ ) ${ }^{10}$ indeed, to evaluate $p($ query $\wedge$ evidence $)$, the $\lambda_{\overline{\mathrm{QNODE}\left(N_{A}\right)}}$ parameter for such a node must be set to 0 . In Fig. 4, $\overline{\mathrm{QNODE}\left(N_{A}\right)}=\overline{7}$. The algorithm then superimposes a new circuit by creating shadow nodes, e.g. $\tilde{c}$, that will represent random variables affected by the change in the $\lambda_{\overline{\mathrm{QNODE}\left(N_{A}\right)}}$ parameter. Figure 4 depicts the $\overline{7}$ node right next to its shadow $\overline{\overline{7}}$. The algorithm then allocates new nodes for each and every node that would be affected by this change in $\lambda_{\overline{\mathrm{QNODE}\left(N_{A}\right)}}$ : in Fig. 4, nodes $9,12,13,14,16$, and 17.

[^0]
[^0]:    ${ }^{10}$ In this paper we focus on a query composed by a single literal.

![img-3.jpeg](img-3.jpeg)

Fig. 4 Shadowing of the circuit represented in Fig. 1 according to Algorithm 5. Solid box for query, double box for evidence, in grey the shadow nodes added to the circuit. If a node has a shadow, they are grouped together with a dashed box. Dashed arrows connect shadow nodes to their children

# 5.3 Evaluating the shadowed circuit 

Each of the nodes in the shadowed circuit (e.g. Fig. 4) has associated a (beta-distributed) random variable. In the following, and in Algorithm 4, given a node $n$, its associated random variable is identified as $X_{n}$. For the nodes for which exists a $\rho$ label, its associated random variable is the beta-distributed random variable labelled via the $\rho$ function, cf. Fig. 4.

Algorithm 4 takes a shadowed circuit and a covariance matrix, to then output means and variance of a beta-distributed random variable that approximates the probabilistic evaluation of a given query, see (44) and (45) below.

```
Algorithm 4 Evaluating the shadowed circuit \(\widehat{N_{A}}\) taking into consideration
the given \(C_{A}\) covariance matrix.
    procedure EVALCOVProbBeta \(\left(\widehat{N_{A}}, C_{A}\right)\)
        means \(:=\) ZEROS \(\left(\left|\widehat{N_{A}}\right|, 1\right)\)
        \(\operatorname{cov}:=\operatorname{ZEROS}\left(\left|\widehat{N_{A}}\right|,\left|\widehat{N_{A}}\right|\right)\)
        nvisited \(:=\left\{\overline{\operatorname{QNODE}\left(N_{A}\right)}\right\}\)
        for \(n \in \operatorname{LEAVES}\left(\widehat{N_{A}}\right) \backslash \overline{\operatorname{QNODE}\left(N_{A}\right)}\) do
            nvisited \(:=\) nvisited \(\cup\{n\}\)
            tvar \(:=0\)
            if \(\lambda_{n}=1\) then
                means \([n]:=\mathbb{E}\left[X_{n}\right]\)
                tvar \(:=\) var \(\left[X_{n}\right]\)
                else means \([n]:=0\)
            end if
            for \(n^{\prime} \in \operatorname{LEAVES}\left(\widehat{N_{A}}\right) \backslash \overline{\operatorname{QNODE}\left(N_{A}\right)}\) do
                \(\operatorname{cov}\left[n, n^{\prime}\right]:=C_{A}\left[X_{n}, X_{n^{\prime}}\right]\)
            end for
        end for
        nqueue \(:=\widehat{N_{A}} \backslash n\) visited
        while nqueue \(\neq \varnothing\) do
            \(n:=n \in n q u e u e\) s.t. \(\operatorname{CHILDREN}\left(\widehat{N_{A}}, n\right) \subseteq n\) visited
            nqueue \(:=\) nqueue \(\backslash\{n\}\)
            nvisited \(:=n\) visited \(\cup\{n\}\)
            if \(n\) is a (shadowed) disjunction over \(C:=\operatorname{CHILDREN}\left(\widehat{N_{A}}, n\right)\) then
                means \([n]:=\sum_{c \in C}\) means \(\left[X_{c}\right]\)
                \(\operatorname{cov}[n, n]:=\sum_{c \in C} \sum_{c^{\prime} \in C} \operatorname{cov}\left[c, c^{\prime}\right]\)
                \(\operatorname{cov}[z, n]:=\operatorname{cov}[n, z]:=\sum_{c \in C} \operatorname{cov}[c, z] \forall z \in \widehat{N_{A}} \backslash\{n\}\)
            else if \(n\) is a (shadowed) conjunction over \(C:=\operatorname{CHILDREN}\left(\widehat{N_{A}}, n\right)\) then
                means \([n]:=\prod_{c \in C}\) means \(\left[X_{c}\right]\)
                \(\operatorname{cov}[n, n]:=\sum_{c \in C} \sum_{c^{\prime} \in C} \frac{\operatorname{means}\left[X_{n}\right]^{2}}{\operatorname{means}\left[X_{c}\right] \operatorname{means}\left[X_{c^{\prime}}\right]} \operatorname{cov}\left[c, c^{\prime}\right]\)
                \(\operatorname{cov}[z, n]:=\operatorname{cov}[n, z]:=\sum_{c \in C} \frac{\operatorname{means}\left[X_{n}\right]}{\operatorname{means}\left[X_{c}\right]} \operatorname{cov}[c, z] \forall z \in \widehat{N_{A}} \backslash\{n\}\)
            end if
        end while
        \(r:=\operatorname{ROOT}\left(\widehat{N_{A}}\right)\)
        return \(\left\langle\frac{\operatorname{means}[\tilde{c}]}{\operatorname{means}[r]}, \frac{1}{\operatorname{means}[r]^{2}} \operatorname{cov}[\tilde{r}, \tilde{r}]+\frac{\operatorname{means}[\tilde{c}]^{2}}{\operatorname{means}[r]^{4}} \operatorname{cov}[r, r]-2 \frac{\operatorname{means}[\tilde{c}]}{\operatorname{means}[r]^{3}} \operatorname{cov}[\tilde{r}, r]\right\rangle\)
    end procedure
```

Algorithm 4 begins with building a vector of means (means), and a matrix of covariances (cov) of the random variables associated to the leaves of the circuit (lines 2-16) derived from the $C_{A}$ covariance matrix provided as input. At lines 2 and 3 we make use of

a support function $\operatorname{ZEROS}(X, Y)$ that returns a matrix of $X$ rows and $Y$ columns filled with zeroes: when $Y=1$, this is equivalently a vector of $X$ values. The algorithm can also be modified to handle the case where $C_{A}$ is in this case, assuming independence among the variables, it is straightforward to obtain a matrix such as Table 2.

Then, Algorithm 4 proceeds to compute the means and covariances for all the remaining nodes in the circuit (lines 17-31). Here two cases arise.

Let $n$ be a $\bigoplus$-gate over $C$ nodes, its children: hence (lines 22-35)

$$
\begin{gathered}
\mathbb{E}\left[X_{n}\right]=\sum_{c \in C} \mathbb{E}\left[X_{c}\right] \\
\operatorname{cov}\left[X_{n}\right]=\sum_{c \in C} \sum_{c^{\prime} \in C} \operatorname{cov}\left[X_{c}, X_{c^{\prime}}\right] \\
\operatorname{cov}\left[X_{n}, X_{z}\right]=\sum_{c \in C} \operatorname{cov}\left[X_{c}, X_{z}\right] \text { for } z \in \widehat{N_{A}} \backslash\{n\}
\end{gathered}
$$

with

$$
\operatorname{cov}[X, Y]=\mathbb{E}[X Y]-\mathbb{E}[X] \mathbb{E}[Y]
$$

and $\operatorname{cov}[X] \equiv \operatorname{cov}[X, X]=\operatorname{var}[X]$.
Let $n$ be a $\otimes$-gate over $C$ nodes, its children (lines 26-30). Following (Benaroya et al., 2005, §4.3.2) we perform a Taylor approximation: let's assume $X_{n}=\Pi\left(\boldsymbol{X}_{\boldsymbol{C}}\right)=\prod_{c \in C} X_{c}$, with $\boldsymbol{X}_{\boldsymbol{C}}=\left(X_{c_{1}}, \ldots, X_{c_{k}}\right)^{\mathrm{T}}$ and $k=|C|$.

Expanding the first two terms of the Taylor series about $\mathbb{E}\left[\boldsymbol{X}_{\boldsymbol{C}}\right]$ yields:

$$
\begin{aligned}
X_{n} & \left.\simeq \Pi\left(\mathbb{E}\left[\boldsymbol{X}_{\boldsymbol{C}}\right]\right)+\left.\left(\boldsymbol{X}_{\boldsymbol{C}}-\mathbb{E}\left[\boldsymbol{X}_{\boldsymbol{C}}\right]\right)^{\mathrm{T}} \nabla \Pi\left(\boldsymbol{X}_{\boldsymbol{C}}\right)\right|_{\boldsymbol{X}_{\boldsymbol{C}}=\mathbb{E}\left[\boldsymbol{X}_{\boldsymbol{C}}\right]} \\
= & \simeq \mathbb{E}\left[X_{n}\right]+\left(X_{\rfloor_{1}}-\mathbb{E}\left[X_{c_{1}}\right]\right) \prod_{\rfloor \in C \backslash\left\{c_{1}\right\}} \mathbb{E}\left[X_{c}\right]+\ldots+\left(X_{\rfloor_{k}}-\mathbb{E}\left[X_{c_{k}}\right]\right) \prod_{\rfloor \in C \backslash\left\{c_{k}\right\}} \mathbb{E}\left[X_{c}\right] \\
& =\mathbb{E}\left[X_{n}\right]+\sum_{c \in C} \frac{\prod_{c^{\prime} \in C} \mathbb{E}\left[X_{c^{\prime}}\right]}{\mathbb{E}\left[X_{c}\right]}\left(X_{c}-\mathbb{E}\left[X_{c}\right]\right) \\
& =\mathbb{E}\left[X_{n}\right]+\sum_{c \in C} \frac{\mathbb{E}\left[X_{n}\right]}{\mathbb{E}\left[X_{c}\right]}\left(X_{c}-\mathbb{E}\left[X_{c}\right]\right)
\end{aligned}
$$

Taking the expectation of both leads to approximating $\mathbb{E}\left[X_{n}\right]$ ] as $\Pi\left(\mathbb{E}\left[\boldsymbol{X}_{\boldsymbol{C}}\right]\right)$.
Using this approximation, then (lines 34-42 of Algorithm 4)

$$
\begin{gathered}
\operatorname{cov}\left[X_{n}\right] \simeq \sum_{c \in C} \sum_{c^{\prime} \in C} \frac{\mathbb{E}\left[X_{n}\right]^{2}}{\mathbb{E}\left[X_{c}\right] \mathbb{E}\left[X_{c^{\prime}}\right]} \operatorname{cov}\left[X_{c}, X_{c^{\prime}}\right] \\
\operatorname{cov}\left[X_{n}, X_{z}\right] \simeq \sum_{c \in C} \frac{\mathbb{E}\left[X_{n}\right]}{\mathbb{E}\left[X_{c}\right]} \operatorname{cov}\left[X_{c}, X_{z}\right] \text { for } z \in \widehat{N_{A}} \backslash\{n\}
\end{gathered}
$$

Finally, Algorithm 4 computes a conditioning between $X_{r}$ and $X_{\mathbb{P}}$, with $r$ being the root of the circuit $\left(r:=\operatorname{ROOT}\left(\widehat{N_{A}}\right)\right.$ at line 46). This shows how critical is to keep track of the nonzero covariances where they exist. The Taylor series approximation of $X_{r}$ and $\frac{1}{X_{\mathbb{P}}}$ about $\mathbb{E}\left[X_{\mathbb{P}}\right]$ and $\frac{1}{\mathbb{E}\left[X_{r}\right]}$ leads to

$$
\frac{X_{\bar{y}}}{X_{r}} \simeq \frac{\mathbb{E}\left[X_{\bar{y}}\right]}{\mathbb{E}\left[X_{r}\right]}+\frac{1}{X_{\bar{y}}}\left(X_{\bar{y}}-\mathbb{E}\left[X_{\bar{y}}\right]\right)-\frac{\mathbb{E}\left[X_{\bar{y}}\right]}{\mathbb{E}\left[X_{r}\right]^{2}}\left(X_{r}-\mathbb{E}\left[X_{r}\right]\right)
$$

which implies

$$
\begin{gathered}
\mathbb{E}\left[\frac{X_{\bar{y}}}{X_{r}}\right] \simeq \frac{\mathbb{E}\left[X_{\bar{y}}\right]}{\mathbb{E}\left[X_{r}\right]} \\
\operatorname{cov}\left[\frac{X_{\bar{y}}}{X_{r}}\right] \simeq \frac{1}{\mathbb{E}\left[X_{r}\right]^{2}} \operatorname{cov}\left[X_{\bar{y}}\right]+\frac{\mathbb{E}\left[X_{\bar{y}}\right]^{2}}{\mathbb{E}\left[X_{r}\right]^{4}} \operatorname{cov}\left[X_{r}\right]-2 \frac{\mathbb{E}\left[X_{\bar{y}}\right]}{\mathbb{E}\left[X_{r}\right]^{3}} \operatorname{cov}\left[X_{\bar{y}}, X_{r}\right]
\end{gathered}
$$

Tables 3 and 4 depict respectively the non-zero values of the means vector and cov matrix for our running example. Overall, the mean and variance for $p$ (burglary|calls(john)) are 0.3571 and 0.0528 , respectively. Figure 5 depicts the resulting beta-distributed random variable (solid line) against a Monte Carlo simulation.

# 5.4 Scalability and memory performance 

Algorithm 3 returns the mean and variance of the probability for the query conditioned on the evidence. Algorithm 5 adds shadow nodes to the initial circuit formed by the evidence to avoid redundant computations in the second pass. For the sake of clarity, Algorithm 4 is presented in its most simple form. As formulated, it requires a $\left|\overline{N_{A}}\right| \times\left|\overline{N_{A}}\right|$ array to store the covariance values between the nodes. For large circuits, this memory requirement can significantly slow down the processing (e.g., disk swaps) or simply become prohibitive. The covariances of a particular node are only required after it is computed via lines 24-25 or 34-35 in Algorithm 4. Furthermore, these covariances are no longer needed once all the parent node values have been computed. Thus, it is straightforward to dynamically allo-cate/de-allocate portions of the covariance array as needed. In fact, the selection of node $n$ to compute in line 19, which is currently arbitrary, can be designed to minimise processing time in light of the resident memory requirements for the covariance array. Such an optimisation depends on the computing architecture and complicates the presentation. Thus, further details are beyond the scope of this paper.

## 6 Experimental results

### 6.1 The benefits of considering covariances

To illustrate the benefits of Algorithm 3 (Sect. 5), we run an experimental analysis involving several circuits with unspecified labelling function. For each circuit, first labels are derived for the case of parametrisation $\mathcal{S}_{p}$ (5) by selecting the ground truth probabilities from a uniform random distribution. Then, for each label, we derive a set of subjective opinions by observing $N_{\text {ins }}$ instantiations of a random variable derived from the chosen probability, so to simulate data sparsity (Kaplan and Ivanovska 2018).

We then proceed analysing the inference on specific query nodes $\boldsymbol{q}$ in the presence of a set of evidence $\boldsymbol{E}=\boldsymbol{e}$ using:

Table 3 Means as computed by Algorithm 4 on our running example. In grey the shadow nodes. Values very close or equal to zero are omitted. Also, values for nodes labelled with negated variables are omitted. $\overline{7}$, i.e. the shadow of $\operatorname{QNODE}\left(N_{4}\right)$, is included for illustration purposes


Table 4 Covariances $\left(\times 10^{-2}\right)$ as computed by Algorithm 4 on our running example. In grey the shadow nodes. Values very close or equal to zero are omitted. Also, values for nodes labelled with negated variables are omitted. $\overline{7}$, i.e. the shadow of $\operatorname{QNODE}\left(N_{4}\right)$, is included for illustration purposes


- $\underline{\mathrm{CPB}}$ as articulated in Sect. 5; ${ }^{11}$
- $\underline{S^{g}}$, cf. (34);
$-\underline{S_{\mathrm{SL}}}$, cf. (27);
- $\overline{\mathrm{MC}}$, a Monte Carlo analysis with 100 samples from the derived random variables to obtain probabilities, and then computing the probability of queries in presence of evidence using the parametrisation $\mathcal{S}_{p}$.

[^0]
[^0]:    ${ }^{11}$ Source code is available at https://github.com/federicocerutti/CPB.

![img-4.jpeg](img-4.jpeg)

Fig. 5 Resulting distribution of probabilities for our running example using Algorithm 3 (solid line), and a Monte Carlo simulation with 100,000 samples grouped in 25 bins and then interpolated with a cubic polynomial (dashed line)

We then compare the RMSE to the actual ground truth. This process of inference to determine the marginal beta distributions is repeated 1000 times by considering 100 random choices for each label of the circuit, i.e. the ground truth, and for each ground truth 10 repetitions of sampling the interpretations used to derive the subjective opinion labels observing $N_{\text {ins }}$ instantiations of all the variables.

We judge the quality of the beta distributions of the queries on how well its expression of uncertainty captures the spread between its projected probability and the actual ground truth probability, as also Kaplan and Ivanovska (2018) did. In simulations where the ground truths are known, such as ours, confidence bounds can be formed around the projected probabilities at a significance level of $\gamma$ and determine the fraction of cases when the ground truth falls within the bounds. If the uncertainty is well determined by the beta distributions, then this fraction should correspond to the strength $\gamma$ of the confidence interval (Kaplan \& Ivanovska, 2018, Appendix C).

```
\(\omega_{1}::\) stress(X) :- person(X).
\(\omega_{1}:\) :influences(X,Y) :- person(X), person(Y).
smokes(X) :- stress(X).
smokes(X) :- friend(X,Y), influences(Y,X), smokes(Y).
\(\omega_{3}:\) asthma(X) :- smokes(X).
person(1).
person(2).
person(3).
person(4).
friend(1,2).
friend(2,1).
friend(2,4).
friend(3,2).
friend(4,2).
evidence(smokes(2), true).
evidence(influences(4,2), false).
query(smokes(1)).
query(smokes(3)).
query(smokes(4)).
query(asthma(1)).
query(asthma(2)).
query(asthma(3)).
query(asthma(4)).
```

Listing 3: Smoker and Friends aProbLog code
Following (Cerutti et al. 2019), we consider the famous Friends \& Smokers problem, cf. Listing $3,{ }^{12}$ with fixed queries and set of evidence. Table 5 provides the root mean square error (RMSE) between the projected probabilities and the ground truth probabilities for all the inferred query variables for $N_{\text {ins }}=10,50,100$. The table also includes the predicted RMSE by taking the square root of the average-over the number of runs-variances from the inferred marginal beta distributions, cf. (18). Figure 6 plots the desired and actual significance levels for the confidence intervals (best closest to the diagonal), i.e. the fractions of times the ground truth falls within confidence bounds set to capture x\% Finally, Fig. 8 depicts the correlation of Dirichlet strengths between the Monte Carlo approach MC running with variable number of samples and the golden standard (i.e. a Monte Carlo run with 10,000 samples), as well as between the golden standard and CPB , which is clearly independent of the number of samples used in MC. We, however, rephrased the sentence to clarify it. of the number of samples used in the Monte Carlo approach MC. Given $\boldsymbol{X}_{\boldsymbol{q}}^{g}$ (resp. $\boldsymbol{X}_{\boldsymbol{q}}$ ) the random variable associated to the queries $\boldsymbol{q}$ computed using the golden standard (resp. computed using either MC or CPB ), the Pearson's correlation coefficient displayed in Fig. 8 is given by:

$$
r=\frac{\operatorname{cov}\left[s_{X_{q}^{g}}, s_{X_{q}}\right]}{\operatorname{cov}\left[s_{X_{q}^{g}}\right] \operatorname{cov}\left[s_{X_{q}}\right]}
$$

[^0]
[^0]:    ${ }^{12}$ https://dtai.cs.kuleuven.be/problog/tutorial/basic/05_smokers.html (on 29th April 2020).

Table 5 RMSE for the queried variables in the Friends \& Smokers program: A stands for Actual, P for Predicted. Best results—also considering hidden decimals—for the actual RMSE boxed . MC has been run over 100 samples


![img-5.jpeg](img-5.jpeg)
(a)
![img-6.jpeg](img-6.jpeg)
(b)
![img-7.jpeg](img-7.jpeg)
(c)

Fig. 6 Actual versus desired significance of bounds derived from the uncertainty for Smokers \& Friends with: (a) $N_{\text {ins }}=10$; (b) $N_{\text {ins }}=50$; and (c) $N_{\text {ins }}=100$. Best closest to the diagonal. $\overline{\mathrm{MC}}$ has been run over 100 samples

This is a measure of the quality of the epistemic uncertainty associated with the evaluation of the circuit using $\overline{\mathrm{MC}}$ with varying number of samples, and $\overline{\mathrm{CPB}}$ : the closer the Dirichlet strengths are to those of the golden standard, the better the computed epistemic uncertainty represents the actual uncertainty, ${ }^{13}$ hence the closer the correlations are to 1 in Fig. 8 the better.

From Table 5, $\overline{\mathrm{CPB}}$ exhibits the lowest RMSE and the best prediction of its own RMSE. As already noticed in (Cerutti et al., 2019), $S^{\beta}$ is a little conservative in estimating its own RMSE, while $\bar{S}_{\mathrm{SL}}$ is overconfident. This is reflected in Fig. 6, with the results of $S^{\beta}$ being over the diagonal, and those of $S_{\mathrm{SL}}$ being below it, while $\overline{\mathrm{CPB}}$ sits exactly on the diagonal, like also $\overline{\mathrm{MC}}$. However, $\overline{\mathrm{MC}}$ with 100 samples does not exhibit the lowest RMSE according to Table 5, although the difference with the best one is much lower compared with $\bar{S}_{\mathrm{SL}}$.

Considering the execution time, Fig. 7, we can see that there is a substantial difference between $\overline{\mathrm{CPB}}$ and $\overline{\mathrm{MC}}$ with 100 samples.

[^0]
[^0]:    ${ }^{13}$ The Dirichlet strengths are inversely proportional to the epistemic uncertainty.

![img-8.jpeg](img-8.jpeg)

Fig. 7 Distribution of execution time for running the different algorithms for Smokers \& Friends with: (a) $N_{\text {ins }}=10$; (b) $N_{\text {ins }}=50$; and (c) $N_{\text {ins }}=100$. Best lowest. MC has been run over 100 samples
![img-9.jpeg](img-9.jpeg)

Fig. 8 Correlation of Dirichlet strengths between runs of $\overline{\mathrm{MC}}$ varying the number of samples and golden standard (i.e. a Monte Carlo run with 10,000 samples) as well as between $\overline{\mathrm{CPB}}$ and golden standard with cubic interpolation-that is independent of the number of samples used in $\overline{\mathrm{MC}}$-for Smokers \& Friends with: (a) $N_{\text {ins }}=10$; (b) $N_{\text {ins }}=50$; and (c) $N_{\text {ins }}=100$

Finally, Fig. 8 depicts the correlation of the Dirichlet strength between the golden standard, i.e. a Monte Carlo simulation with 10,000 samples, and both $\overline{\mathrm{CPB}}$ and $\overline{\mathrm{MC}}$, this last one varying the number of samples used. It is straightforward to see that $\overline{\mathrm{MC}}$ improves the accuracy of the computed epistemic uncertainty when increasing the number of samples considered, approaching the same level of $\overline{\mathrm{CPB}}$ when considering more than 200 samples.

# 6.2 Comparison with other approaches for dealing with uncertain probabilities 

```
\(\omega_{2}:: \mathrm{n} 1\).
\(\omega_{3}:: \mathrm{n} 2:-\backslash+\mathrm{n} 1\).
\(\omega_{4}:: \mathrm{n} 2:-\mathrm{n} 1\).
\(\omega_{5}:: \mathrm{n} 3:-\backslash+\mathrm{n} 2\).
\(\omega_{6}:: \mathrm{n} 3:-\mathrm{n} 2\).
\(\omega_{7}:: \mathrm{n} 4:-\backslash+\mathrm{n} 2\).
\(\omega_{8}:: \mathrm{n} 4:-\mathrm{n} 2\).
\(\omega_{9}:: \mathrm{n} 5:-\backslash+\mathrm{n} 3\).
\(\omega_{10}:: \mathrm{n} 5:-\mathrm{n} 3\).
\(\omega_{11}:: \mathrm{n} 6:-\backslash+\mathrm{n} 3\).
\(\omega_{12}:: \mathrm{n} 6:-\mathrm{n} 3\).
\(\omega_{13}:: \mathrm{n} 7:-\backslash+\mathrm{n} 6\).
\(\omega_{14}:: \mathrm{n} 7:-\mathrm{n} 6\).
\(\omega_{15}:: \mathrm{n} 8:-\backslash+\mathrm{n} 5\).
\(\omega_{16}:: \mathrm{n} 8:-\mathrm{n} 5\).
\(\omega_{17}:: \mathrm{n} 9:-\backslash+\mathrm{n} 5\).
\(\omega_{18}:: \mathrm{n} 9:-\mathrm{n} 5\).
evidence \(\left(\mathrm{n} 1, e_{1}\right)\).
evidence \(\left(\mathrm{n} 4, e_{2}\right)\).
evidence \(\left(\mathrm{n} 7, e_{3}\right)\).
evidence \(\left(\mathrm{n} 8, e_{4}\right)\).
evidence \(\left(\mathrm{n} 9, e_{5}\right)\).
query (n2).
query (n3).
query (n5).
query (n6).
```

Listing 4: An example of aProblog code that can be seen also as a Bayesian network, cf. Fig. 12a in Appendix E. $e_{i}$ are randomly assigned as either True or False.

To compare our approach against the state-of-the-art approaches for reasoning with uncertain probabilities, following (Cerutti et al., 2019) we restrict ourselves to the case of circuits representing inferences over a Bayesian network. For instance, Listing 4 shows an aProblog code that can also be interpreted as a Bayesian network. We considered three circuits and their Bayesian network representation: Net1 (Listing 4); Net2; and Net3. Figure 12 in Appendix E depicts the Bayesian networks that can be derived from such circuits. In the following, we will refer to NetX as both the circuit and the Bayesian network without distinction. We then compared CPB against three approaches specifically designed for dealing with uncertain probabilities in Bayesian networks: Subjective Bayesian Networks; Belief Networks; and Credal Networks.

Subjective Bayesian Network SBN (Ivanovska et al., 2015; Kaplan \& Ivanovska, 2016; Kaplan \& Ivanovska, 2018), was first proposed in (Ivanovska et al., 2015), and it is an uncertain Bayesian network where the conditionals are subjective opinions instead of dogmatic probabilities. In other words, the conditional probabilities are known within a beta distribution. SBN uses subjective belief propagation (SBP), which was introduced for trees in (Kaplan \& Ivanovska 2016) and extended for singly-connected networks in (Kaplan \& Ivanovska, 2018), that extends the Belief Propagation (BP) inference method of Pearl (1986). In BP, $\pi$ - and $\lambda$-messages are passed from parents and children, respectively, to a node, i.e., variable. The node uses these messages to formulate the inferred marginal probability of the corresponding variable. The node also uses these messages to determine

the $\pi$ - and $\lambda$-messages to send to its children and parents, respectively. In SBP, the $\pi$ - and $\lambda$-messages are subjective opinions characterised by a projected probability and Dirichlet strength. The SBP formulation approximates output messages as beta-distributed random variables using the methods of moments and a first-order Taylor series approximation to determine the mean and variance of the output messages in light of the beta-distributed input messages. The details of the derivations are provided in (Kaplan \& Ivanovska, 2016; Kaplan \& Ivanovska, 2018).

Belief Networks $\underline{\text { GBT }}$ Smets (1993) introduced a computationally efficient method to reason over networks via Dempster-Shafer theory (Dempster, 1968). It is an approximation of a valuation-based system. Namely, a (conditional) subjective opinion $\omega_{X}=\left[b_{x}, b_{\bar{x}}, u_{X}\right]$ from our circuit obtained from data is converted to the following belief mass assignment: $m(x)=b_{x}, m(\bar{x})=b_{\bar{x}}$ and $m(x \cup \bar{x})=u_{X}$. Note that in the binary case, the belief function overlaps with the belief mass assignment. The method exploits the disjunctive rule of combination to compose beliefs conditioned on the Cartesian product space of the binary power sets. This enables both forward propagation and backward propagation after inverting the belief conditionals via the generalized Bayes' theorem (GBT). By operating in the Cartesian product space of the binary power sets, the computational complexity grows exponentially with respect to the number of parents.

Credal Networks $\underline{\text { Credal }}$ (Zaffalon \& Fagiuoli, 1998). A credal network over binary random variables extends a Bayesian network by replacing single probability values with closed intervals representing the possible range of probability values. The extension of Pearl's message-passing algorithm by the 2 U algorithm for credal networks is described in (Zaffalon \& Fagiuoli, 1998). This algorithm works by determining the maximum and minimum value (an interval) for each of the target probabilities based on the given input intervals. It turns out that these extreme values lie at the vertices of the polytope dictated by the extreme values of the input intervals. As a result, the computational complexity grows exponentially with respect to the number of parents nodes. For the sake of comparison, we assume that the random variables we label our circuits with and elicited from the given data corresponds to a credal network in the following way: if $\omega_{x}=\left[b_{x}, b_{\bar{x}}, u_{X}\right]$ is a subjective opinion on the probability $\theta$, then we have $\left[b_{x}, b_{x}+u_{X}\right]$ as an interval corresponding to this probability in the credal network. It should be noted that this mapping from the beta-distributed random variables to an interval is consistent with past studies of credal networks (Karlsson et al., 2008).

As before, Table 6 provides the root mean square error (RMSE) between the projected probabilities and the ground truth probabilities for all the inferred query variables for $N_{\text {ins }}$ $=10,50,100$, together with the RMSE predicted by taking the square root of the average variances from the inferred marginal beta distributions. Figure 9 plots the desired and actual significance levels for the confidence intervals (best closest to the diagonal). Figure 10 depicts the distribution of execution time for running the various algorithms, and Fig. 11 the correlation of the Dirichlet strength between the golden standard, i.e. a Monte Carlo simulation with 10,000 samples, and both CPB and MC varying the number of samples.

Table 6 shows that CPB shares the best performance with the state-of-the-art SBN and $S^{\beta}$ almost constantly. This is clearly a significant achievement considering that SBN is the state-of-the-art approach when dealing only with single connected Bayesian Networks with uncertain probabilities, while we can also handle much more complex problems. Consistently with Table 5, and also with (Cerutti et al., 2019), $S^{\beta}$ has lower RMSE

Table 6 RMSE for the queried variables in the various networks: A stands for Actual, P for Predicted. Best results—also considering hidden decimals—for the Actual RMSE boxed. MC has been run over 100 samples


than $S_{\mathrm{SL}}$ and it seems that $S^{\beta}$ overestimates the predicted RMSE and $S_{\mathrm{SL}}$ underestimates it as $S_{\mathrm{SL}}$ predicts smaller error than is realised and vice versa for $S^{\beta}$.

From visual inspection of Fig. 9, it is evident that $\underline{\text { CPB }}, \underline{\text { SBN }}$, and $\underline{\text { MC }}$ all are very close to the diagonal, thus correctly assessing their own epistemic uncertainty. $S^{\beta}$ performance is heavily affected by the fact that it computes the conditional distributions at the very end of the process and it relies, in (33), on the assumption of independence. CPB , keeping track of the covariance between the various nodes in the circuits, does not suffer from this problem. This positive result has been achieved without substantial deterioration of the performance in terms of execution time, as displayed in Fig. 10, for which the same commentary of Fig. 7 applies.

Finally, Fig. 11 depicts the correlation of the Dirichlet strength between the golden standard, i.e. a Monte Carlo simulation with 10,000 samples, and both CPB and MC , this last one varying the number of samples used. Like for Fig. 8, it is straightforward to see that $\underline{\text { MC }}$ improves the accuracy of its computed epistemic uncertainty when increasing the number of samples considered, approaching the same level of CPB when considering more than 200 samples, while $\underline{\text { CPB }}$ performs very closely to the optimal value of 1 .

![img-10.jpeg](img-10.jpeg)

Fig. 9 Actual versus desired significance of bounds derived from the uncertainty for: (a) Net1 with $N_{\text {ins }}=10$; (b) Net1 with $N_{\text {ins }}=50$; (c) Net1 with $N_{\text {ins }}=100$; (d) Net2 with $N_{\text {ins }}=10$; (e) Net2 with $N_{\text {ins }}=50$; (f) Net2 with $N_{\text {ins }}=100$; (g) Net3 with $N_{\text {ins }}=10$; (h) Net3 with $N_{\text {ins }}=50$; (i) Net3 with $N_{\text {ins }}=100$. Best closest to the diagonal. MC has been run over 100 samples

# 7 Conclusion 

In this paper, we introduce (Sect. 5) an algorithm for reasoning over a probabilistic circuit whose leaves are labelled with beta-distributed random variables, with the additional piece of information describing which of those are actually independent (Sect. 5.1). This provides the input to an algorithm that shadows the circuit derived for computing the probability of the pieces of evidence by superimposing a second circuit modified for computing the probability of a given query and the pieces of evidence, thus having all the necessary components for computing the probability of a query conditioned on the pieces of evidence (Sect. 5.2). This is essential when evaluating such a shadowed circuit (Sect. 5.3), with the covariance matrix playing an essential role by keeping track of the dependencies between random variables while they are manipulated within the circuit. We also include discussions on memory management in Sect. 5.4.

In our extensive experimental analysis (Sect. 6) we compare against leading approaches to compute uncertain probabilities, notably: (1) Monte Carlo sampling; (2) our previous proposal (Cerutti et al., 2019) as representative of the family of approaches using a moment matching approach with strong independence assumptions; (3) Subjective Logic

![img-11.jpeg](img-11.jpeg)

Fig. 10 Distribution of computational time for running the different algorithms for: (a) Net1 with $N_{\text {ins }}=10$; (b) Net1 with $N_{\text {ins }}=50$; (c) Net1 with $N_{\text {ins }}=100$; (d) Net2 with $N_{\text {ins }}=10$; (e) Net2 with $N_{\text {ins }}=50$; (f) Net2 with $N_{\text {ins }}=100$; (g) Net3 with $N_{\text {ins }}=10$; (h) Net3 with $N_{\text {ins }}=50$; (i) Net3 with $N_{\text {ins }}=100 .[\mathrm{MC}]$ has been run over 100 samples
(Jøsang, 2016); (4) Subjective Bayesian Network (SBN) (Ivanovska et al., 2015; Kaplan \& Ivanovska, 2016; Kaplan \& Ivanovska, 2018); (5) Dempster-Shafer Theory of Evidence (Dempster, 1968; Smets, 1993); and (6) credal networks (Zaffalon and Fagiuoli 1998).

We achieve the same or better results of state-of-the-art approaches for dealing with epistemic uncertainty, including highly engineered ones for a narrow domain such as SBN, while being able to handle general probabilistic circuits and with just a modest increase in the computational effort. In fact, this work has inspired us to leverage probabilistic circuits to expand second-order inference for SBN for arbitrary directed acyclic graphs whose variables are multinomials. As part of future work, we will expand our experimental investigation to consider larger models, also leveraging recent advancements in engineering

![img-12.jpeg](img-12.jpeg)

Fig. 11 Correlation of Dirichlet strengths between runs of MC varying the number of samples and golden standard (i.e. a Monte Carlo run with 10,000 samples) as well as between CPR and golden standard with cubic interpolation-that is independent of the number of samples used in MC-for: (a) Net1 with $N_{\text {ins }}=10$; (b) Net1 with $N_{\text {ins }}=50$; (c) Net1 with $N_{\text {ins }}=100$; (d) Net2 with $N_{\text {ins }}=10$; (e) Net2 with $N_{\text {ins }}=50$; (f) Net2 with $N_{\text {ins }}=100$; (g) Net3 with $N_{\text {ins }}=10$; (h) Net3 with $N_{\text {ins }}=50$; (i) Net3 with $N_{\text {ins }}=100$
highly-efficient procedures over probablistic circuits, e.g. (Peharz et al., 2020). However, as also highlighted in Figs. 7 and 10 our research-grade prototype is substantially faster than using Monte Carlo sampling for estimating variances. Indeed, we can estimate it from just one pass over the circuit (see Algorithm 4), while a Monte Carlo approach would need to go through the circuit once for each sample.

We focused our attention on probabilistic circuits derived from d-DNNFs: work by Darwiche (2011), and then also by Kisa et al. (2014) has introduced Sentential Decision Diagrams (SDDs) as a new canonical formalism respectively for propositional and for probabilistic circuits. However, as we can read in (Darwiche, 2011, p. 819) SDDs is a strict subset of d-DNNF, which is thus the least constrained type of propositional circuit we can safely rely on according to (Kimmig et al., 2017, Theorem 4). However, in future work we will enable our approach to efficiently make use of SDDs.

In addition, we will also work in the direction of enabling learning with partial obser-vations-incomplete data where the instantiations of each of the propositional variables are not always visible over all training instantiations-on top of its ability of tracking the covariance values between the various random variables for a better estimation of epistemic uncertainty.

# A. aProbLog 

In the last years, several probabilistic variants of Prolog have been developed, such as ICL (Poole, 2000), Dyna (Eisner et al., 2005), PRISM (Sato and Kameya, 2001) and ProbLog (De Raedt et al. 2007), with its aProbLog extension (Kimmig et al., 2011) to handle arbitrary labels from a semiring. They all are based on definite clause logic (pure Prolog) extended with facts labelled with probability values. Their meaning is typically derived from Sato's distribution semantics (Sato, 1995), which assigns a probability to every literal. The probability of a Herbrand interpretation, or possible world, is the product of the probabilities of the literals occurring in this world. The success probability is the probability that a query succeeds in a randomly selected world.

For a set $J$ of ground facts, we define the set of literals $\mathrm{L}(J)$ and the set of interpretations $\mathcal{I}(J)$ as follows:

$$
\begin{gathered}
\mathrm{L}(J)=J \cup\{\neg f \mid f \in J\} \\
\mathcal{I}(J)=\{S \mid S \subseteq \mathrm{~L}(J) \wedge \forall l \in J: l \in S \leftrightarrow \neg l \notin S\}
\end{gathered}
$$

An algebraic Prolog (aProbLog) program (Kimmig et al., 2011) consists of:

- a commutative semiring $\left\langle\mathcal{A}, \oplus, \otimes, e^{\oplus}, e^{\otimes}\right\rangle$
- a finite set of ground algebraic facts $\mathrm{F}=\left\{f_{1}, \ldots, f_{n}\right\}$
- a finite set BK of background knowledge clauses
- a labeling function $\rho: \mathrm{L}(\mathrm{F}) \rightarrow \mathcal{A}$

Background knowledge clauses are definite clauses, but their bodies may contain negative literals for algebraic facts. Their heads may not unify with any algebraic fact.

For instance, in the following aProbLog program

```
alarm :- burglary.
0.05 :: burglary.
```

burglary is an algebraic fact with label 0.05 , and alarm :- burglary represents a background knowledge clause, whose intuitive meaning is: in case of burglary, the alarm should go off.

The idea of splitting a logic program in a set of facts and a set of clauses goes back to Sato's distribution semantics (Sato, 1995), where it is used to define a probability distribution over interpretations of the entire program in terms of a distribution over the facts. This is possible because a truth value assignment to the facts in F uniquely determines the truth values of all other atoms defined in the background knowledge. In the simplest case, as realised in ProbLog (De Raedt et al., 2007; Fierens et al., 2015), this basic distribution considers facts to be independent random variables and thus multiplies their individual probabilities. aProbLog uses the same basic idea, but generalises from the semiring of probabilities to general commutative semirings. While the distribution semantics is defined for countably infinite sets of facts, the set of ground algebraic facts in aProbLog must be finite.

In aProbLog, the label of a complete interpretation $I \in \mathcal{I}(\mathrm{~F})$ is defined as the product of the labels of its literals

$$
\mathbf{A}(I)=\bigotimes_{l \in I} \rho(l)
$$

and the label of a set of interpretations $S \subseteq \mathcal{I}(\mathrm{~F})$ as the sum of the interpretation labels

$$
\mathbf{A}(S)=\bigoplus_{I \in S} \bigotimes_{l \in I} \rho(l)
$$

A query $q$ is a finite set of algebraic literals and atoms from the Herbrand base, ${ }^{14}$ $q \subseteq \mathrm{~L}(\mathrm{~F}) \cup H B(\mathrm{~F} \cup \mathrm{BK})$. We denote the set of interpretations where the query is true by $\mathcal{I}(q)$,

$$
\mathcal{I}(q)=\{I \mid I \in \mathcal{I}(\mathrm{~F}) \wedge I \cup \mathrm{BK} \vDash q\}
$$

The label of query $q$ is defined as the label of $\mathcal{I}(q)$,

$$
\mathbf{A}(q)=\mathbf{A}(\mathcal{I}(q))=\bigoplus_{I \in \mathcal{I}(q)} \bigotimes_{l \in I} \rho(l)
$$

As both operators are commutative and associative, the label is independent of the order of both literals and interpretations.

ProbLog (Fierens et al., 2015) is an instance of aProbLog with

$$
\begin{aligned}
& \mathcal{A}=\mathbb{R}_{\geq 0} \\
& a \oplus b=a+b \\
& a \otimes b=a \cdot b \\
& e^{\oplus}=0 \\
& e^{\otimes}=1 \\
& \delta(f) \in[0,1] \\
& \delta(\neg f)=1-\delta(f)
\end{aligned}
$$

# B. Subjective logic operators of sum, multiplication, and division 

Let us recall the following operators as defined in (Jøsang, 2016). In the following, let $\omega_{X}=\left\langle b_{X}, d_{X}, u_{X}, a_{X}\right\rangle$ and $\omega_{Y}=\left\langle b_{Y}, d_{Y}, u_{Y}, a_{Y}\right\rangle$ be two subjective logic opinions.

## Sum

The opinion about $X \cup Y$ (sum, $\omega_{X} \boxplus_{\mathrm{SL}} \omega_{Y}$ ) is defined as $\omega_{X \cup Y}=\left\langle b_{X \cup Y}, d_{X \cup Y}, u_{X \cup Y}, a_{X \cup Y}\right\rangle$, where:

- $b_{X \cup Y}=b_{X}+b_{Y}$
- $d_{X \cup Y}=\frac{a_{X}\left(d_{X}-b_{Y}\right)+a_{Y}\left(d_{Y}-b_{X}\right)}{a_{X}+a_{Y}}$
- $u_{X \cup Y}=\frac{a_{X} a_{X}+a_{Y} u_{Y}}{a_{X}+a_{Y}} ;$ and
- $a_{X \cup Y}=a_{X}+a_{Y}$.

[^0]
[^0]:    ${ }^{14}$ I.e., the set of ground atoms that can be constructed from the predicate, functor and constant symbols of the program.

# Product 

The opinion about $X \wedge Y$ (product, $\omega_{X} \boxtimes_{\mathrm{SL}} \omega_{Y}$ ) is defined-under assumption of independence-as $\omega_{X \wedge Y}=\left\langle b_{X \wedge Y}, d_{X \wedge Y}, u_{X \wedge Y}, a_{X \wedge Y}\right\rangle$, where:

- $b_{X \wedge Y}=b_{X} b_{Y}+\frac{\left(1-a_{X}\right) a_{Y} b_{X} u_{Y}+a_{X}\left(1-a_{Y}\right) a_{X} b_{Y}}{1-a_{X} a_{Y}}$
- $d_{X \wedge Y}=d_{X}+d_{Y}-d_{X} d_{Y}$
- $u_{X \wedge Y}=u_{X} u_{Y}+\frac{\left(1-a_{Y}\right) b_{X} u_{Y}+\left(1-a_{X}\right) u_{X} b_{Y}}{1-a_{X} a_{Y}}$; and
- $a_{X \wedge Y}=a_{X} a_{Y}$.


## Division

The opinion about the division of $X$ by $Y, X \bar{\wedge} Y$ (division, $\omega_{X} \boxtimes_{\mathrm{SL}} \omega_{Y}$ ) is defined as $\omega_{X \bar{\wedge} Y}=\left\langle b_{X \bar{\wedge} Y}, d_{X \bar{\wedge} Y}, u_{X \bar{\wedge} Y}, a_{X \bar{\wedge} Y}\right\rangle$ where

- $b_{X \bar{\wedge} Y}=\frac{a_{Y}\left(b_{Y}+a_{X} u_{X}\right)}{\left(a_{Y}-a_{X}\right)\left(b_{Y}+a_{Y} u_{Y}\right)}-\frac{a_{X}\left(1-d_{X}\right)}{\left(a_{Y}-a_{X}\right)\left(1-d_{Y}\right)}$;
- $d_{X \bar{\wedge} Y}=\frac{d_{X}-d_{Y}}{1-d_{Y}}$
- $u_{X \bar{\wedge} Y}=\frac{a_{Y}\left(1-d_{X}\right)}{\left(a_{Y}-a_{X}\right)\left(1-d_{Y}\right)}-\frac{a_{Y}\left(b_{Y}+a_{X} u_{X}\right)}{\left(a_{Y}-a_{X}\right)\left(b_{Y}+a_{Y} u_{Y}\right)}$; and
- $a_{X \bar{\wedge} Y}=\frac{a_{X}}{a_{Y}}$
subject to:
$-a_{X}<a_{Y} ; d_{X} \geq d_{Y}$
$-b_{X} \geq \frac{a_{X}\left(1-a_{Y}\right)\left(1-d_{X}\right) b_{Y}}{\left(1-a_{X}\right) a_{Y}\left(1-d_{Y}\right)}$; and
$-u_{X} \geq \frac{\left(1-a_{Y}\right)\left(1-d_{X}\right) a_{Y}}{\left(1-a_{X}\right)\left(1-d_{Y}\right)}$.

## C. Independence of posterior distributions when learning from complete observations

Let us instantiate AMC using probabilities as labels (cf. (5)) and let us consider a propositional logic theory over $M$ variables. We can thus re-write (1) as:

$$
p(T)=\sum_{I \in \mathcal{M}(T)} \prod_{m=1}^{M} p\left(l_{m}\right)
$$

Hence, the probability of a theory is function of the probabilities of interpretations $p(I \in \mathcal{M}(T))$, where

$$
p(I \in \mathcal{M}(T))=\prod_{m=1}^{M} p\left(l_{m}\right)
$$

Let's assume that we want to learn such probabilities from a dataset $\mathcal{D}=\left(\boldsymbol{x}_{1}, \ldots, \boldsymbol{x}_{N}\right)^{\mathrm{T}}$, then by (55) the variables for which we are learning probabilities are independent, hence

$$
p\left(l_{1}, \ldots, l_{M}\right)=\prod_{m=1}^{M} p\left(l_{m}\right)
$$

We can thus re-write the likelihood (9) as:

$$
\begin{aligned}
p\left(\mathcal{D} \mid \boldsymbol{p}_{\boldsymbol{x}}\right) & =\prod_{i=1}^{|\mathcal{D}|} p\left(\boldsymbol{x}_{i} \mid \boldsymbol{p}_{x_{i}}\right) \\
& =\prod_{i=1}^{|\mathcal{D}|} \prod_{m=1}^{M} p_{x_{m}}^{x_{i, m}}\left(1-p_{x_{m}}\right)^{1-x_{i, m}}
\end{aligned}
$$

Assuming a uniform prior, and letting $r_{m}$ be the number of observations for $x_{m}=1$ and $s_{m}$ the number of observations for $x_{m}=0$, we can thus compute the posterior as:

$$
\begin{aligned}
p\left(\boldsymbol{p}_{\boldsymbol{x}} \mid \mathcal{D}, \boldsymbol{\alpha}^{0}\right) & \propto p\left(\mathcal{D} \mid \boldsymbol{p}_{\boldsymbol{x}}\right) \cdot p\left(\boldsymbol{p}_{\boldsymbol{x}} \mid \boldsymbol{\alpha}^{0}\right) \\
& \propto \prod_{m=1}^{M} p_{x_{m}}^{r_{m}+\alpha_{s_{m}}^{0}-1}\left(1-p_{x_{m}}\right)^{s_{m}+\alpha_{s_{m}}^{0}-1}
\end{aligned}
$$

which, in turns, show that the independence is maintained also considering the posterior beta distributions.

# D. Algorithm for shadowing a given circuit 

In Algorithm 5 we make use of a stack data structure with associated pop and push functions (cf. lines $3,5,8,16$ ): that is for ease of presentation as the algorithm does not require a stack.

Algorithm 5 Shadowing the circuit $N_{A}$.
procedure ShADOWCircuit $\left(N_{A}\right)$
$\overline{N_{A}}:=N_{A}$
links $:=\operatorname{STACK}()$
for $p \in \operatorname{PARENTS}\left(N_{A}, \overline{\operatorname{QNODE}\left(N_{A}\right)}\right)$ do
$\operatorname{PUSH}\left(\right.$ links, $\left.\left\langle\overline{\operatorname{QNODE}\left(N_{A}\right)}, p\right\rangle\right)$
end for
while -empty (links) do
$\langle c, p\rangle:=\operatorname{POP}($ links $)$
$\overline{N_{A}}:=\overline{N_{A}} \cup\{\tilde{c}\}$
if $\tilde{p} \notin \overline{N_{A}}$ then
$\overline{N_{A}}:=\overline{N_{A}} \cup\{\tilde{p}\}$
$\operatorname{CHILDREN}\left(\overline{N_{A}}, \tilde{p}\right):=\operatorname{CHILDREN}\left(\overline{N_{A}}, p\right)$
end if
$\operatorname{CHILDREN}\left(\overline{N_{A}}, \tilde{p}\right):=\left(\operatorname{CHILDREN}\left(\overline{N_{A}}, \tilde{p}\right) \backslash\{c\}\right) \cup\{\tilde{c}\}$
for $p^{\prime} \in \operatorname{PARENTS}\left(N_{A}, p\right)$ do
$\operatorname{PUSH}\left(\right.$ links, $\left.\left\langle p, p^{\prime}\right\rangle\right)$
end for
end while
return $\overline{N_{A}}$
end procedure

# E. Bayesian networks derived from aProbLog programs 

Figure 12 depicts the Bayesian networks that can be derived from the three circuits considered in the experiments described in Sect. 6.2.
![img-13.jpeg](img-13.jpeg)

Fig. 12 Network structures tested where the exterior gray variables are directly observed and the remaining are queried: (a) Net1, a tree; (b) Net2, singly connected network with one node having two parents; (c) Net3, singly connected network with one node having three parents

Acknowledgements We thank the anonymous reviews whose comments improve the first draft submitted for consideration to this journal. This research was sponsored by the U.S. Army Research Laboratory and the U.K. Ministry of Defence under Agreement Number W911NF-16-3-0001. The views and conclusions contained in this document are those of the authors and should not be interpreted as representing the official policies, either expressed or implied, of the U.S. Army Research Laboratory, the U.S. Government, the U.K. Ministry of Defence or the U.K. Government. The U.S. and U.K. Governments are authorized to reproduce and distribute reprints for Government purposes notwithstanding any copyright notation hereon. This work was performed using the computational facilities of the Advanced Research Computing at Cardiff (ARCCA) Division, Cardiff University.

# Authors and Affiliations 

## Federico Cerutti ${ }^{1,2} \odot$ Lance M. Kaplan ${ }^{3} \cdot$ Angelika Kimmig ${ }^{4,5} \cdot$ Murat Şensoy ${ }^{6,7}$

Lance M. Kaplan
lance.m.kaplan.civ@army.mil
Angelika Kimmig
angelika.kimmig@cs.kuleuven.be
Murat Şensoy
murat.sensoy@ozyegin.edu.tr
1 Department of Information Engineering, University of Brescia, Brescia, Italy
2 Crime and Security Research Institute, Cardiff University, Cardiff, UK
3 US DEVCOM Army Research Laboratory, Adelphi, MD, USA
4 Department of Computer Science, KU Leuven, Leuven, Belgium
5 Leuven.AI - KU Leuven Institute for AI, Leuven, Belgium
6 Blue Prism AI Labs, London, UK
7 Department of Computer Science, Ozyegin University, Istanbul, Turkey