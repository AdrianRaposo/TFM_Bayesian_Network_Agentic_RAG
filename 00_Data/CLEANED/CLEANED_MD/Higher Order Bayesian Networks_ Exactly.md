# Higher Order Bayesian Networks, Exactly 

CLAUDIA FAGGIAN, IRIF, CNRS, Université Paris Cité, France DANIELE PAUTASSO, University of Turin, Italy GABRIELE VANONI, IRIF, CNRS, Université Paris Cité, France

Bayesian networks are graphical first-order probabilistic models that allow for a compact representation of large probability distributions, and for efficient inference, both exact and approximate. We introduce a higher-order programming language-in the idealized form of a $\lambda$-calculus-which we prove sound and complete w.r.t. Bayesian networks: each Bayesian network can be encoded as a term, and conversely each (possibly higher-order and recursive) program of ground type compiles into a Bayesian network.

The language allows for the specification of recursive probability models and hierarchical structures. Moreover, we provide a compositional and cost-aware semantics which is based on factors, the standard mathematical tool used in Bayesian inference. Our results rely on advanced techniques rooted into linear logic, intersection types, rewriting theory, and Girard's geometry of interaction, which are here combined in a novel way.
CCS Concepts: $\cdot$ Theory of computation $\rightarrow$ Lambda calculus; Probabilistic computation; Linear logic; Type theory; Denotational semantics.
Additional Key Words and Phrases: lambda calculus, intersection types, Bayesian networks, probabilistic programming, denotational semantics

## ACM Reference Format:

Claudia Faggian, Daniele Pautasso, and Gabriele Vanoni. 2024. Higher Order Bayesian Networks, Exactly. Proc. ACM Program. Lang. 8, POPL, Article 84 (January 2024), 33 pages. https://doi.org/10.1145/3632926

## 1 INTRODUCTION

This paper is a foundational study, taking a cost-aware approach to the semantics of higher-order probabilistic programming languages. Probabilistic models play a crucial role in several fields such as machine learning, cognitive science, and applied statistics, with applications spanning from finance to biology. A prominent example of such models are Bayesian networks (BNs) [Pearl 1988], a (first-order, static) graphical formalism able to represent complex systems in a compact way and enabling efficient inference algorithms. BNs decompose large joint distributions into smaller factors. These are used in inference algorithms, both exact (such as message passing and variable elimination) and approximate (sampling-based). Despite their significant strengths, the task of modeling using Bayesian networks is comparable to the task of programming using logical circuits.

Probabilistic Programming Languages. A different approach is taken by probabilistic programming languages (PPLs), where statistical models are specified as programs. The fundamental idea behind PPLs is to separate the model description-the program-from the computation of the probability distribution specified by the program-the inference task. This separation aims at making stochastic modeling as accessible as possible, hiding the underlying inference engines, which typically encompass various sampling methods such as importance sampling, Markov Chain Monte Carlo, and

[^0]
[^0]:    Authors' addresses: Claudia Faggian, IRIF, CNRS, Université Paris Cité, France, faggian@irif.fr; Daniele Pautasso, University of Turin, Italy, daniele.pautasso@unito.it; Gabriele Vanoni, IRIF, CNRS, Université Paris Cité, France, gabriele.vanoni@irif.fr.

Gibbs sampling. In this paper, we specifically focus on functional PPLs, which allow for first-class higher-order functions and compositional semantics (e.g. Church [Goodman et al. 2008], Anglican [Wood et al. 2014] and Venture [Mansinghka et al. 2014]).

Bayesian Networks and PPLs. Bayesian networks and PPLs are closely interconnected. On the one hand, Bayesian networks can be easily represented as simple, first-order, probabilistic programs [Gilks et al. 1994; Koller et al. 1997]. On the other hand, several first-order PPLs (such as BUGS, a widely used declarative language, and Infer.NET) compile programs into a graphical model, specifically a Bayesian network, which is then utilized for performing inference tasks. For a detailed tutorial and an analysis of the involved subtleties, we refer to [van de Meent et al. 2018] (Ch.3).

Towards a Foundational Understanding. The research community is devoting considerable effort to establish a solid foundational understanding of functional PPLs. A central concept is compositionality, which is the key to reason in a modular (and scalable) way about programs. Such an understanding is crucial for the development of robust formal methods to facilitate the analysis of probabilistic programs, the construction of Bayesian models, and the verification of inference correctness. Pioneering works by Jacobs and Zanasi [2016, 2020] have paved the way for a logical and semantical comprehension of Bayesian networks and inference from a categorical perspective. The majority of foundational papers, e.g. [Dahlqvist et al. 2018; Heunen et al. 2017; Scibior et al. 2018; Stein and Staton 2021; Vákár et al. 2019], have adopted an approach based on category theory, which has yielded remarkable insights, enabling denotational proofs of correctness and compositionality principles. This line of research however does not take into account the raison d'être of Bayesian networks, namely the space and time efficiency of inference. In the literature, compositional semantics and efficiency are typically explored as separate entities. This dichotomy stands in stark contrast to Bayesian networks, where the representation, its semantics (the defined joint distribution), and the inference algorithms are deeply intertwined.

This paper. Our foundational investigation adopts a cost-aware perspective. We introduce a semantical framework that integrates the efficiency of Bayesian networks with the expressiveness of higher-order functional programming, and the compositional nature of type systems. We adopt an idealized functional PPL, namely an untyped $\lambda$-calculus enriched with probabilistic primitives. Our language faithfully encompasses conventional Bayesian networks (expressed here by first-order terms in normal form), and comes equipped with a semantics and formal methods which are resources-sensitive. The core of our approach lies in semantical techniques, including rewriting theory and type systems. These form the groundwork for a compilation scheme that translates higher-order terms into Bayesian networks, which serve as a low-level language. We list below our main contributions:

- A higher-order language for BNs. We introduce a probabilistic call-by-push-value $\lambda$-calculus that we prove sound and complete for BNs: not only any Bayesian network can be encoded as a term (which is standard), but also-conversely-any higher-order (possibly recursive) program of ground type will eventually reduce to a first-order normal form, corresponding to a Bayesian network (Thm. 4.6 and Thm. 7.1). Our language also supports the encoding of advanced stochastic models, including template Bayesian networks, and the specification of recursive probability models. Notably, the operational semantics we define corresponds to the process of unrolling the template into an actual BN, in line with the intended semantics of the templates.
- A factor-based semantics. We endow each term of ground type with a factor-based semantics. Factors, indeed, are the mathematical structure which give semantics to BNs. Technically, computing this factor-based semantics requires tracking the generation and sharing of random variables-this task is achieved using non-idempotent intersection types. This technique allows

![img-0.jpeg](img-0.jpeg)

Fig. 1. An example of Bayesian network (from [Darwiche 2009]).
us to extract a Bayesian network $\mathcal{B}_{t}$ from the type derivation of a ground term $t$, and to prove that the semantics (in the sense of Bayesian networks theory) of $\mathcal{B}_{t}$ coincides with the semantics of $t$.

- The factor semantics is compositional. The main technical achievement of the paper is to establish the compositionality of the factor semantics for typed terms (Sect. 6 and Sect. 7.2). This is particularly noteworthy since operations on factors do not exhibit this property, in general. The design of the type system plays a crucial role in ensuring compositionality, thereby enabling the modular reasoning that one expects in a high-level programming language.
- The factor semantics is resource-sensitive. Our semantics takes resource consumption into account-its computational complexity (both in terms of space and time) is similar to that for Bayesian networks. Additionally, the type system offers a precise estimate of the cost associated with computing the semantics of a term (i.e., the cost of calculating the exact distribution defined by the term).
- Proof techniques. The proof of our results incorporates sophisticated techniques that have their foundation in linear logic, leveraging significant advancements made over the past 15 years. Specifically, we employ intersection types, rewriting theory, linear logic, and concepts inspired by Girard's geometry of interaction in a novel and synergistic manner.

Proofs and more examples are available in the Technical Report [Faggian et al. 2023].

# 2 ABOUT BAYESIAN NETWORKS, SHARING, AND THE $\lambda$-CALCULUS, INFORMALLY 

Bayesian Reasoning. In the Bayesian interpretation, probabilities describe degrees of belief in events, and inference allows for reasoning under uncertainty. One challenge in Bayesian reasoning is how to represent joint probability distributions. Indeed, these can quickly become very large: in general, a probability distribution over $n$ boolean variables requires storing $2^{n}$ values. Bayesian networks are able to express a joint probability distribution over several variables in a compact way (factorized representation), allowing for efficient inference, without ever needing to reconstruct the full joint distribution.

An Example of Bayesian Network. Let us start with an informal example. We want to model the fact that the lawn being Wet in the morning may depend on either Rain or the Sprinkler being on. In turn, both Rain and the regulation of the Sprinkler depend on being or not in the Dry Season. The dependencies between these four variables (shortened to $D, S, R, W$ ) are represented as arrows in Fig. 1, while (for each variable) the strength of the dependencies is quantified by a conditional probability table (CPT). Assume we wonder: did it rain last night? Given that we are in DrySeason,




$\operatorname{Pr}(r, w)=\sum_{d, s \in\{1, f\}} \operatorname{Pr}(d, s, r, w)$
summing out $D, S$
Fig. 2. Joint distribution corresponding to the Bayesian network in Fig. 1, and marginalization.
our prior belief is that Rain happens with probability 0.2 . However, if we observe that the lawn is Wet, our confidence increases. The updated belief is called posterior. The model in Fig. 1 allows us to infer the posterior probability of Rain, given the evidence that the lawn is Wet, i.e. $\operatorname{Pr}(R=t \mid W=t)$. Posteriors are typical queries which can be answered by Bayesian inference, which has at its core Bayes conditioning, often condensed in the following informal formula:

$$
\text { Posterior }=\text { Prior } \times \text { Likelihood } \div \text { Evidence }
$$

Concretely, in our example:

$$
\operatorname{Pr}(\text { Rain }=\mathrm{t} \mid \text { Wet }=\mathrm{t})=\frac{\operatorname{Pr}(\text { Wet }=\mathrm{t} \mid \text { Rain }=\mathrm{t}) \operatorname{Pr}(\text { Rain }=\mathrm{t})}{\operatorname{Pr}(\text { Wet }=\mathrm{t})}=\frac{\operatorname{Pr}(\text { Rain }=\mathrm{t}, \text { Wet }=\mathrm{t})}{\operatorname{Pr}(\text { Wet }=\mathrm{t})}
$$

So, to compute the posterior $\operatorname{Pr}($ Rain $=\mathrm{t} \mid$ Wet $=\mathrm{t})$, we have to compute the marginal $\operatorname{Pr}($ Rain $=$ $t$, Wet $=t$ ), which can be obtained by summing out the other variables from the joint probability. Marginalization is illustrated in Fig. 2 (all rows which agree on the value of Rain and Wet are merged into a single row, summing up the probabilities). We remark that the joint distribution over D, S, R, W has $2^{4}$ entries, although here we only display a subset of them.

The marginal probability $\operatorname{Pr}($ Wet $=\mathrm{t})$ of the evidence is computed in a similar way (yielding 0.69). Then, we obtain the posterior by normalizing: $\operatorname{Pr}($ Rain $=\mathrm{t} \mid$ Wet $=\mathrm{t})=0.33 / 0.69=0.48$. Further evidence (for example, the Sprinkler is broken) would once again update our belief. In practice, the numerator of Bayes theorem (the unnormalized marginal) often suffices, since the actual posterior is proportional to it:

$$
\text { Posterior } \propto \text { Prior } \times \text { Likehood }
$$

Summing up, the key step in exact inference is the computation of marginals.
Bayesian Networks as Terms. In probabilistic programming, it is standard to describe a Bayesian network with a term (see e.g. [Gordon et al. 2014] for a brief tutorial). We can encode our initial example into a rather standard probabilistic call-by-value $\lambda$-calculus, as follows:

```
let dry = bernoulli
let rain = case 〈dry〉 of {t=bernoulli
let sprinkler = case 〈dry〉 of {t=bernoulli
let wet
```

in wet
The idea is that any CPT can be encoded with a case construct, together with a probabilistic primitive sample $_{d}$, which returns a value sampled from a (countably supported) probability distribution

![img-1.jpeg](img-1.jpeg)

Fig. 3. Modeling $m$ coin tosses.
![img-2.jpeg](img-2.jpeg)

Fig. 4. Discrete Time Dynamic Bayesian network.
d. In this example we sample from a Bernoulli distribution. This way, all Bayesian networks can be encoded in a very basic fragment of the simply typed call-by-value $\lambda$-calculus (this will be discussed in the next sections). What if we allow for a richer, non linear, $\lambda$-calculus?

Beyond Ground Bayesian Networks. Standard Bayesian networks describe probabilistic models in an intuitive and compact way, but have some inherent limitations. They are a first-order model, lacking modularity and compositionality. A well-established way to increase the expressive power of Bayesian networks are templates ${ }^{1}$, which allow for the description of hierarchical models and for taking into account temporality. Dynamic Bayesian networks [Dean and Kanazawa 1989] (in Fig. 4) are an instance extensively used in real-world applications-e.g. mobile robotics. A more structured approach is indeed essential when models become large and complex. While standard Bayesian networks have a precise mathematical definition, rooted in graph theory and statistics, templates are a more informal notion. We show that techniques from functional programming language theory can provide a neat and mathematically sound framework, founded on the theory of lambda calculus, exactly matching the intended semantics of templates.

Repeated Coin Tosses. Let us consider the following experiment, where repetition is involved.

1. Sample a bias $r_{i}$ from a discrete distribution (for simplicity, let us assume there are only two possible choices: $r_{1}$ or $r_{2}$ ).
2. Toss $m$ times a coin of bias $r_{i}$.
3. Return the results of the $m$ (biased) coin tosses.

It is standard to graphically describe such an experiment by means of the plate notation [Buntine 1994; Gilks et al. 1994] (see Fig. 3), a graphical meta-formalism for representing models with repeated structures and shared parameters. A rectangular plate grouping random variables indicates multiple copies of the sub-graph. A number $(m)$ is drawn to represent the number of repetitions. Unrolling the plate $m$ times defines a ground Bayesian network. Please notice that the intended Bayesian network is the unrolled one. In Fig. 3, we show the template which models our experiment (a), and the ground Bayesian network resulting from its unrolling (b).

Repetitions, Sharing, and PPL. How can we describe this experiment as a $\lambda$-term? Let us assume $m=2$. It is tempting to encode the template in the following way:

```
let bias = sample \(_{d}\) in
let coin = case 〈bias〉 of \(\left\{r_{1}=\right.\) bernoulli \(_{r_{1}} ; r_{2}=\) bernoulli \(_{r_{2}}\)
in 〈coin, coin〉
```

Unfortunately, the call-by-value policy makes sure that all the instances of coin have the same shared value, so the possible outcomes are only $\langle\mathrm{t}, \mathrm{t}\rangle$ and $\langle\mathrm{f}, \mathrm{f}\rangle$. Indeed, since only values can be

[^0]
[^0]:    ${ }^{1}$ We refer to [Koller and Friedman 2009], Ch. 6, for a detailed presentation and pointers to the vast literature.


Fig. 5. The $\lambda$-term correctly modeling two coin tosses, and its reduction to normal form. $\mathbf{c}$ 〈bias〉 stands for the conditional expression case 〈bias〉 of $\left\{r_{1}=\right.$ bernoulli $\left._{r_{1}} ; r_{2}=\right.$ bernoulli $\left._{r_{2}}\right\}$. The result stored in bias is correctly shared, while coin is copied before performing the toss, thus giving two independent and identically distributed values to $y_{1}$ and $y_{2}$.
substituted for variables, all expressions, even the probabilistic ones, have to be evaluated before being substituted. Switching the evaluation order to call-by-name does not solve the problem: now all the probabilistic primitives are copied before being evaluated. This means that all coin tosses are independent, this way not belonging necessarily to the same coin: some could have bias $r_{1}$ and some others $r_{2}$. We need a finer evaluation mechanism that allows the programmer to say when values have to be shared, and when instead we want to actually duplicate unevaluated expressions.

Call-by-Push-Value. More than 20 years ago Levy [1999] introduced call-by-push-value as a subsuming paradigm and functional/imperative synthesis, refining the computational $\lambda$-calculus by Moggi [1989]. The slogan was: "a value is, a computation does", as this language tries to unify call-by-name and call-by-value, providing two new primitives. The former thunks a computation inside a value, and the latter forces the evaluation of a value as a computation. Similar ideas have been independently developed in the linear logic community, using Girard's translations. There, linear $\lambda$-calculi use the ! to thunk, and der(eliction) to force [Benton and Wadler 1996; Egger et al. 2014; Ehrhard 2016; Melliès and Tabareau 2010; Simpson 2005]. Having all of this in mind, we encode our experiment as the leftmost term of Fig. 5.

Operational Semantics. The simplest operational semantics for probabilistic programs is in terms of sampled values. A standard approach in probabilistic $\lambda$-calculi (including [Ehrhard and Tasson 2019]) is to give the operational semantics via Markov chains: sequential evaluation produces distributions over execution paths. Here, we follow a different route, because we want to model the unrolling of a higher-order term into a ground Bayesian Network, as shown in Fig. 5. By firing all the redexes but the probabilistic choices, the term $t$ reduces to a normal form that represents a standard, ground Bayesian network, exactly matching the unrolling of the template in Fig. 3.

# 3 PRELIMINARIES ON CALCULUS AND TYPES 

This section presents the probabilistic programming language we are going to use throughout this paper. The language includes constructs for describing sampling and conditioning. We have already argued why we opted for a language that is able to thunk computations and force values.

### 3.1 Syntax

Our language, dubbed $\lambda_{!}$-calculus, is a fragment of [Ehrhard and Tasson 2019] probabilistic call-by-push-value. For ease of presentation, in this paper we limit ground types to booleans. This way, all random variables are assumed binary, and as a consequence, we only sample from Bernoulli distributions. Generalizing the language to discrete r.v.s is straightforward.

Terms. Let $\mathcal{V}$ be a countable set of variables. $\lambda_{i}$-terms are defined by the following grammar:


Following [Ehrhard 2016; Ehrhard and Tasson 2019], we use Linear Logic inspired notations: ! $t$ corresponds to thunk $(t)$ and der $t$ to force $(t)$. The probabilistic primitive sample $_{d}$ samples a boolean value from a (Bernoulli) distribution $d$. The case construct is just a generalized if/then/else-please notice that the case expression is restricted, because we reserve it to the encoding of CPT's, as we have informally described in Sect. 2. Observed data (the evidence) are specified syntactically using an observe construct, written obs-for example obs(wet $=\mathrm{t}$ ); we will give several examples of its use in Sect. 8 .

Free and bound variables are defined as usual: $\lambda x . t$ binds $x$ in $t$, and the same for let and letp. A term is closed when there are no free occurrences of variables in it. Terms are considered modulo $\alpha$-equivalence, and capture-avoiding (meta-level) substitution of all the free occurrences of $x$ for $u$ in $t$ is noted $t\{x \leftarrow u\}$.

Syntactic Sugar. The grammar of the calculus is rather restricted, reminiscent of A-normal forms (and similarly to [Levy 1999]). It is standard to recover general constructs as follows:

$$
\begin{aligned}
t u & \triangleq \text { let } z=u \text { in } t z \\
\left\langle u_{1}, u_{2}\right\rangle & \triangleq \text { let } z_{1}=u_{1} \text { in let } z_{2}=u_{2} \text { in }\left\langle z_{1}, z_{2}\right\rangle \\
\operatorname{der} u & \triangleq \text { let } z=u \text { in der } z \\
\operatorname{letp}\left\langle y_{1}, y_{2}\right\rangle=u \text { in } t & \triangleq \text { let } z=u \text { in letp }\left\langle y_{1}, y_{2}\right\rangle=z \text { in } t \\
\text { case } u \text { of }\left\{v_{i} \equiv t_{i}\right\} & \triangleq \text { let } z=u \text { in case } z \text { of }\left\{v_{i} \equiv t_{i}\right\} \\
\operatorname{obs}(u=b) & \triangleq \text { let } z=u \text { in obs }(z=b)
\end{aligned}
$$

Notation 3.1. We often write $\left\langle v_{1}, \ldots, v_{n}\right\rangle$ for a $n$-tuple, ignoring the tree order. In particular, we write $\widehat{\mathrm{b}}$ for tuples of booleans $\left\langle\mathrm{b}_{1}, \ldots, \mathrm{~b}_{n}\right\rangle$.
(Call-by-Push-Value) Simple Types. In the actual technical development of this paper, we will use intersection types. However, we prefer to first give the intuitions about typing in the more familiar setting of simple types. The ground types are (tensors of) booleans. Following Levy [1999] and Ehrhard and Tasson [2019], we then define by mutual induction two kinds of types: positive types and general types. Only positive types can be assigned to variables in the type environment and can appear in the left hand side of an arrow.


The typing rules are in Fig. 6, where a context $\mathcal{P}$ is a sequence of assignments of positive types $P$ to variables $x$. As usual, a judgment $\mathcal{P} \vdash t: A$ indicates that $t$ has type $A$ given typing context $\mathcal{P}$. We write $\pi \triangleright \mathcal{P} \vdash t: A$ to indicate that $\pi$ is a type derivation of the given judgment. All the rules in Fig. 6 are standard but s-COND. Notice that in rule s-COND by $\left\{\widehat{\mathrm{b}} \equiv \operatorname{sample}_{d_{\widehat{\mathrm{c}}}}\right\}_{\widehat{\mathrm{b}} \in\{\mathrm{t}, \mathrm{f}\}^{n}}$ we mean that for each possible $n$-tuple of booleans $\widehat{\mathrm{b}} \in\{\mathrm{t}, \mathrm{f}\}^{n}$ there is a corresponding sample clause. For the sake of brevity, from now on we will often shorten a case expression depending on $n$ variables $x_{1}, \ldots, x_{n}$ as follows:

$$
\mathbf{c}_{\left\langle x_{1}, \ldots, x_{n}\right\rangle} \triangleq \text { case }\left\langle x_{1}, \ldots, x_{n}\right\rangle \text { of }\left\{\widehat{\mathrm{b}} \equiv \text { sample }_{d_{\widehat{\mathrm{c}}}}\right\}_{\widehat{\mathrm{b}} \in\{\mathrm{t}, \mathrm{f}\}^{n}}
$$

![img-3.jpeg](img-3.jpeg)

Fig. 6. The simply typed $\lambda_{1}$-calculus.

Remark 3.2 (Additive Contexts). The reader familiar with Linear Logic and calculi based on it (such as [Benton et al. 1993]) may be surprised by the fact that here (as in [Ehrhard 2016; Levy 1999]) the context is managed additively. This is because the only types which are allowed in a context are positive, hence either of the form $!A$, or booleans, coded by additives. ${ }^{2}$ Notice that proper linear types, such as $A \rightarrow B$, are not allowed in the context (if allowed, their management would be multiplicative).

The Higher-Order and the Low-Level Language. It is standard to encode a ground Bayesian network with a simple let-term of ground type. The reader can easily realize that every ground Bayesian network can be described in a simple, first-order fragment of the $\lambda_{1}$-calculus, as we have done in the examples in Sect. 2. In particular, there is no need for the modalities ! and der, which are instead the key to implement higher-order behaviors. Abstraction and application are not necessary, as well. We refer to such a fragment as $\lambda_{\text {low }}$-calculus. Formally, the grammar for $\lambda_{\text {low }}$-terms is:

$$
\begin{aligned}
& \text { Low-level Terms } t, u \quad::=\left.v \mid \text { sample }_{d} \mid \text { case } v \text { of }\left\{\overline{\mathrm{b}} \equiv \text { sample }_{d_{\bar{u}}}\right\} \mid \text { obs }(x=\mathrm{b})\right| \\
& \text { let } x=u \text { in } t \mid \text { letp }\langle x, y\rangle=v \text { in } t \\
& \text { Low-level Values } v, w \quad::=\left.x \in \mathcal{V} \mid\langle v, w\rangle \mid t \mid f\right.
\end{aligned}
$$

It is easy to check that a $\lambda_{\text {low }}$-term is typable with a ground context if and only if it has ground type and is typable with first-order rules (those highlighted in Fig. 6), only. Going back to our introductory intuitions, we see the $\lambda_{1}$-calculus as the target high-level language in which the statistical model is designed by the programmer, and the $\lambda_{\text {low }}$-calculus as the low-level language, closer to ground Bayesian networks. Compiling $\lambda_{1}$-terms into $\lambda_{\text {low }}$-terms is taken care of by semantical tools. The first of such tools is the reduction relation, which we introduce next.

[^0]
[^0]:    ${ }^{2}$ Positive types can be contracted and weakened. This is clear for types of the form $!A$, but holds also for ground types. Indeed a boolean type corresponds to the additive formulas $1 \oplus 1$. Notice that $\perp \& \perp=(1 \oplus 1)^{\perp}$ can be weakened and contracted.

# 3.2 Operational Semantics 

In Sect. 2 we have anticipated that the operational semantics of our calculus formalizes the unrolling of a template into a ground Bayesian network, which is its intended meaning. Formally, every $\lambda_{!}$-term of ground type compiles (i.e., rewrites) into a $\lambda_{\text {low }}$-term.

Root Rules. Since the goal is to produce a term describing a Bayesian network, here reduction does not fire probabilistic redexes, i.e. we do not actually sample from distributions. As a consequence, a term of shape sample $_{d}$ never reduces to a value. This feature of our language forces us to opt for a notion of reduction, dubbed reduction at a distance [Accattoli and Kesner 2010; Milner 2006], which is a bit more sophisticated than usual, and reminiscent of reduction on graphs, such as proof-nets and bigraphs. Precisely, our reduction is similar to that in [Arrial et al. 2023; Bucciarelli et al. 2020]. Reduction is called at a distance because in some of the rules the interacting parts of a redex can be separated by an arbitrarily long (possibly empty) list of let constructs-i.e. they are distant. Formally, we need the notion of substitution list, i.e. a sequence of nested let constructors:

Substitution Lists $\quad \mathrm{S} \quad::=\{\cdot\} \mid$ let $x=u$ in $\mathrm{S} \mid \operatorname{letp}\langle x, y\rangle=v$ in S
We are now able to define the rewriting rules which are the base of our reduction relation. We call the term on the left-hand side a redex.


$\{t\} \mathrm{S}$ stands for the term obtained from S by replacing the hole $\{\cdot\}$ with $t$ (possibly capturing the free variables of $t$ ). The rule $\mapsto_{\mathrm{db}}$ fires a (possibly distant) beta-redex. The rule $\mapsto_{\text {dsub }}$ fires a (possibly distant) let, provided that its argument is a value. The rule $\mapsto_{\text {der! }}$ defrosts a frozen term. The rule $\mapsto_{\mathrm{pm}}$ performs pattern matching with pairs. We set $\mapsto \triangleq \mapsto_{\mathrm{db}} \cup \mapsto_{\mathrm{dsub}} \cup \mapsto_{\mathrm{der}!} \cup \mapsto_{\mathrm{pm}}$.

Reduction. A reduction step $\rightarrow$ is the closure of $\mapsto$ under evaluation context. Reduction $\rightarrow_{r}$ (for $r \in\{d b$, dsub, der!, pm\}) is defined similarly. Evaluation contexts, which are terms containing exactly one occurrence of a special symbol-the hole $\langle\vdash\rangle$ - are defined as follows:

$$
\text { Evaluation Contexts } \mathrm{E} \quad::=\langle\vdash\rangle \mid \mathrm{E} v \mid \text { let } x=\mathrm{E} \text { in } t \mid \text { let } x=u \text { in } \mathrm{E}
$$

$\mathrm{E}\langle t\rangle$ stands for the term obtained from E by replacing the hole $\langle\vdash\rangle$ with $t$ (possibly capturing the free variables of $t$ ). As it is standard with programming languages, we adopt a weak notion of reduction, which here means that we do not reduce inside the scope of a ! (a thunk), nor in the scope of a $\lambda$. Please notice that given a term of shape let $x=u$ in $t$, reduction can be performed inside either $u$ or $t$. This is essential to make possible a reduction such as the one in Fig. 5. As a consequence, reduction is not deterministic. However, the choice of redex is irrelevant, in the following sense.

## Proposition 3.3 (Confluence).

1. The reduction $\rightarrow$ is confluent.
2. Every normalizing term is strongly normalizing.
3. All maximal reduction sequences from a term $t$ have the same length.

Proof. Consequences of a diamond-like property, essentially as in [Bucciarelli et al. 2020].
Progress and BN Normal Forms. We say that a term $t$ is in normal form if no reduction applies $(t \nrightarrow)$. It is well-known that simply typed $\lambda$-calculi are strongly normalizing. Here we prove that every $\lambda_{!}$-term of ground type reduces to a normal form which is a low-level term, that we dub $B N$ normal form. The idea-which we will make formal in Sect. 7.1-is that normal forms of ground type directly correspond to ground Bayesian networks, hence the name.

Proposition 3.4 (Progress). Let $t$ be a $\lambda_{1}$-term in normal form and $\pi \triangleright \mathcal{L} \vdash t: L$ a type derivation, where all types in the context $\mathcal{L}$ are ground. Then $t$ is a $\lambda_{\text {low }}$-term, and $\pi$ contains first order rules, only.

Proof. By induction on the structure of the derivation $\pi$.
The proposition above allows us to describe the grammar of BN normal forms. These are the normal forms of $\lambda_{1}$-terms of ground type. If we restrict to closed terms, the BN normal forms are the subset of closed low-level terms generated by the following set of productions:

$$
n::=\text { let } x=s \text { in } n|v| s \quad s::=\text { let } x=s \text { in } s\left|\operatorname{sample}_{d}\right| \mathbf{c}_{\left\langle x_{1}, \ldots, x_{n}\right\rangle} \mid \operatorname{obs}(x=\mathrm{b})
$$

Please notice that BN normal forms are not values, in general. This is because we do not reduce probabilistic primitives.

# 4 THE INTERSECTION TYPE SYSTEM 

Simple type systems guarantee termination, but are poor in expressiveness. In this work we want to specify rich behaviors, such as recursion, and this is why we switch to the untyped $\lambda$-calculus. However, this is not enough to obtain the results we want, and we still do need a form of typing. Since we are interested in giving a Bayesian network semantics to terms, we need to keep track of the random variables defined by a term, and to handle the fact that recursive programs generate a finite but unbounded number of random variables. Random variables are associated to the sampling and conditional primitives, so we need to take into account how many times these primitives are duplicated during the reduction. A quite natural option (especially when using a calculus inspired by linear logic, as we do) is to consider a type system that explicitly takes into account how many times a sub-term is copied during the evaluation. Non-idempotent intersection types for the untyped $\lambda$-calculus do precisely that. This approach has several advantages:

- Tracking random variables: ground types now correspond precisely to random variables, as we discuss in Sect. 4.1 below.
- Distinguishing copies: non-idempotent intersection types intrinsically take into account how many times a (sub-)term is copied. This is of fundamental importance for us, since we want to keep track of all the random variables generated by our typed program. Think for example of a single (thunked) sample $_{d}$ instruction that is duplicated several times during execution. Non-idempotent intersection type derivation duplicate in advance each use of a sub-term, and give each a (possibly different) type.
- Enforcing termination: Bayesian networks are representations for finite probabilistic models. Therefore we are interested in terminating programs, only. Intersection types provide such a guarantee, still allowing for complex behaviors such as general recursion.
- Ruling out ill-formed terms: as a by-product, intersection types act as a traditional type system discarding terms which "go wrong".
We highlight that we could have proceeded differently. We could have considered a typed PCF-like language, as in [Ehrhard and Tasson 2019]. Still-for the reasons described above-we would have needed to add, on top of its type system, an intersection type system, like in [Dal Lago and Gaboardi 2011; Ehrhard 2016]. However, dealing with two layers of types is heavy, and we preferred keeping the syntax as simple as possible. This way, from now on we will consider just the intersection type system for the (untyped) $\lambda_{1}$-calculus which we have presented in Sect. 3.1. In Sect. 10 we sketch how the (two-layered) type system for the call-by-push-value PCF would look like.

Remark 4.1 (Intersection Types and Turing Completeness). Type systems ensure safety and desirable properties such as termination, or deadlock-freeness. Intersection types for the untyped $\lambda$-calculus [Coppo and Dezani-Ciancaglini 1978; Coppo et al. 1981] bring this idea to its extreme

consequence. Intersection types not only guarantee termination, but also characterize it, providing a compositional presentation of all and only the terminating programs. They can indeed be seen as $a$ semantical tool for higher-order languages. Being the untyped $\lambda$-calculus Turing-complete, the price to pay is that intersection type systems are inherently undecidable. This is not typically considered an issue because such systems have a semantic nature: they are used to give denotational models. However, please notice that the first-order fragment of our system is decidable.

# 4.1 Towards Bayesian Networks: Named Types 

Before presenting the intersection type system, we need to introduce one more ingredient, namely named booleans, which we use to track random variables. In this subsection we give some simple examples to convey the intuitions, which we then formalize in Sect. 4.2.

Describing a Bayesian network (or a marginal distribution) by means of a term of type $\otimes^{n} B$ is a standard, easy task. However, retrieving a Bayesian network from a term of type $\otimes^{n} B$ is less immediate, even with low-level terms. Does a low-level term of ground type define a marginal distribution? If yes, over how many random variables? And what is the underlying Bayesian network, if any?

Example 4.2. Let us consider the term $t$, where $\mathbf{c}\langle y\rangle \triangleq$ case $y$ of $\left\{b \Rightarrow\right.$ sample $\left._{d_{b}}\right\}$.

$$
t \triangleq \text { let } x=\text { bernoulli }_{0.2} \text { in let } y=x \text { in let } z=\mathbf{c}\langle y\rangle \text { in }\langle x, y\rangle: B \otimes B
$$

We know that the term $t$ defines two r.v.s (say $X$ and $Y$ ), because there are two probabilistic constructs. We also know that the output is a probability distribution over tuples in $B \otimes B$. It is however not obvious which variables are involved in the final marginal distribution. We can track which random variables are involved in the term by naming the booleans and assigning a distinct name to the subject of each probabilistic axiom (we will formalize this in Sect. 4.2).

$$
\begin{aligned}
& x: B_{X} \vdash x: B_{X} \quad y: B_{X} \vdash y: B_{X} \\
& \begin{array}{c}
x: B_{X} \vdash x: B_{X} \quad y: B_{X} \vdash y: B_{X} \\
\vdash \text { sample }_{d}: B_{X} \quad x: B_{X} \vdash \text { let } y=x \text { in let } z=\mathbf{c}\langle y\rangle \text { in }\langle x, y\rangle: B_{X} \otimes B_{X}
\end{array} \\
& \vdash \text { let } x=\text { sample }_{d} \text { in let } y=x \text { in let } z=\mathbf{c}\langle y\rangle \text { in }\langle x, y\rangle: B_{X} \otimes B_{X}
\end{aligned}
$$

We now realize that the marginal distribution defined by the term $t$ is in fact $\operatorname{Pr}(X=b, X=b)$, for $b \in\{t, f\}$. This is a redundant version of $\operatorname{Pr}(X=b)$, the distribution over the single variable $X$. The probabilities associated to the tuple of values in $B_{X} \otimes B_{X}$ are indeed $\langle t, t\rangle \mapsto 0.2,\langle f, f\rangle \mapsto 0.8$. Necessarily, the tuples $\langle t, f\rangle$ and $\langle f, t\rangle$ have probability 0 . Please contrast the term $t$ above with the term let $x=$ bernoulli $_{0.2}$ in let $y=\mathbf{c}\langle x\rangle$ in $\langle x, y\rangle: B_{X} \times B_{Y}$, which instead defines a distribution over two variables.

In the following we formalize these ideas, exploiting named types to associate a Bayesian network to a ground term. We write only the names $X, Y$, but please think of them as named booleans $B_{X}, B_{Y}$.

### 4.2 The Type System

In this section, we introduce the type system, which will be the base for the factor semantics in Sect. 6. In order to focus on the main ideas, we postpone the treatment of the evidence, namely of the construct obs $(x=b)$ to Sect. 8. This is because while being conceptually easy, it requires some fine tuning of the type system, that would make its description harder to understand.

The Type System. The grammar of intersection types is derived from the one for simple types, and for this reason we keep the same meta-variables. Indeed, we shall not use simple types anymore in the rest of the paper, so no confusion can occur. We assume a countable set Names $=\{X, Y, Z \ldots\}$ of

symbols, called names, which play the role of atomic types. The grammar of types includes ground types, multisets of types (the proper intersection types), and functional types.


Here [...] denotes the multiset constructor. Please notice that the empty multiset [] is a positive type, as well. Two changes are present w.r.t. the definition of simple types:

1. Named Booleans : the type B of booleans has been substituted by a countable set of names. This means that each use of a boolean variable has now a distinct type (name). Morally, different names correspond to different random variables.
2. Multisets for Thunks : types of shape !A have been replaced by multisets of types. As usual in non-idempotent intersection types, the idea is that every type inside a multiset corresponds to a single use of the typed term (see Sect. 4.4 for an example).
The typing rules are in Fig. 7; typing contexts, which we separate in ground contexts (denoted by $\Lambda$ ) and multiset contexts (denoted by $\Gamma$ or $\Delta$ ), are defined in the next paragraph. Given a type $A$, we denote by $\mathrm{Nm}(A)$ the set of names which appear in $A$. The definition extends to typing contexts (e.g. $\mathrm{Nm}(\Lambda)$ ) and type derivations $(\mathrm{Nm}(\pi))$.

Contexts. A typing context $\Sigma$ is a (total) map from variables to positive types such that only finitely many variables are not mapped to the empty multiset []. The domain of $\Sigma$ is the set $\operatorname{dom}(\Sigma) \doteq\{x \mid \Sigma(x) \neq[]\}$. A context $\Sigma$ is empty if $\operatorname{dom}(\Sigma)=\emptyset$. A typing context $\Sigma$ is denoted by $x_{1}: P_{1}, \ldots, x_{n}: P_{n}$ if $\operatorname{dom}(\Sigma) \subseteq\left\{x_{1}, \ldots, x_{n}\right\}$ and $\Sigma\left(x_{i}\right)=P_{i}$ for all $1 \leq i \leq n$. Given two typing contexts $\Sigma_{1}$ and $\Sigma_{2}$ such that $\operatorname{dom}\left(\Sigma_{1}\right) \cap \operatorname{dom}\left(\Sigma_{2}\right)=\emptyset$, the typing context $\Sigma_{1}, \Sigma_{2}$ is defined as $\left(\Sigma_{1}, \Sigma_{2}\right)(x) \doteq \Sigma_{1}(x)$ if $x \in \operatorname{dom}\left(\Sigma_{1}\right),\left(\Sigma_{1}, \Sigma_{2}\right)(x) \doteq \Sigma_{2}(x)$ if $x \in \operatorname{dom}\left(\Sigma_{2}\right)$, and $\left(\Sigma_{1}, \Sigma_{2}\right)(x) \doteq[]$ otherwise. Observe that $\Sigma, x:[]$ is equal to $\Sigma$. Given a context $\Sigma$, it is convenient to partition it into a ground and a multiset context. We call ground context (denoted by $\Lambda$ ) the restriction of $\Sigma$ to the variables which are mapped to ground types, and we call multiset context (denoted by $\Gamma$ or $\Delta$ ) its complement, i.e. the restriction of $\Sigma$ to the variables which are mapped to multisets. Multiset union $\uplus$ is extended to multiset contexts point-wise, i.e. $(\Gamma \uplus \Delta)(x) \doteq \Gamma(x) \uplus \Delta(x)$, for each variable $x$.

Remark 4.3. Please notice that in Fig. 7 we have operated a few simplifications in the presentation of the type system. In particular, we do not type boolean constants anymore-this simplifies the I-COND rule, that now is an axiom. Moreover, notice that tuples always have the multiset context empty.As we aforementioned, we postpone the treatment of $\operatorname{obs}(x=\mathrm{b})$ to Sect. 8.

Type Derivations. We write $\pi \triangleright \Lambda, \Gamma \vdash t: A$ to indicate that $\pi$ is a type derivation (using the full type system in Fig. 7), proving that $t$ has type $A$ given typing context $\Lambda$ (ground) and $\Gamma$ (multiset). We write $\pi \triangleright_{\text {low }} \Lambda \vdash t: L$ for a derivation $\pi$ which uses first order rules, restricted to ground contexts, only.

Naming Condition. We call main names those which type the subject of an I-COND or I-SAMPLE rule. Given a type derivation $\pi$, we assume that all the main names are pairwise distinct. So, each I-COND or I-SAMPLE rule is uniquely identified by a name X. This requirement is easy to implement. Indeed, it is a sort of Barendregt convention, but for types. One could consider the name introduced by a probabilistic axiom as the address of the axiom in the type derivation.

The First-Order Fragment. Notice that the first-order fragment in Fig. 7 is the same as the firstorder fragment of simple types (Fig. 6), the only difference being that now the booleans are named. Clearly this fragment is decidable, since any first-order simply typed derivation of $\mathcal{L} \vdash t: \otimes^{n} \mathrm{~B}$

# Higher-Order Calculus 

First-Order Rules
![img-4.jpeg](img-4.jpeg)

Fig. 7. The intersection type system iTypes.
(where every type in the context $\mathcal{L}$ is ground) can easily be named, by assigning a distinct name to the subject of every probabilistic axioms, and to every occurrence of boolean type in $\mathcal{L}$.

### 4.3 Properties of the Type System

The intersection type system satisfies all the properties one would expect-proofs are in the Tech. Report. First, types are stable under reduction and expansion (this latter property not holding for simple types).

Proposition 4.4 (Subject Reduction/Expansion). Let $t$ be a $\lambda_{1}$-term such that $t \rightarrow u$. Then $\Sigma \vdash t: A$ if and only if $\Sigma \vdash u: A$.

Subject reduction can be strengthened, showing that there is a measure that decreases along each reduction sequence. This gives a combinatorial proof that typable terms are strongly normalizing.

Theorem 4.5. Let $t$ be a $\lambda_{1}$-term. If $t$ is typable, then $t$ is strongly normalizing.
Crucially, the progress lemma, stated for simple types, still holds for intersection types. This means that every (higher-order, possibly recursive) $\lambda_{1}$-term which is typable with ground type in a ground context, eventually reduces to a BN normal form.

Theorem 4.6 (Compiling into the low-level). Let $t$ be a $\lambda_{1}$-term such that $\pi \triangleright \Lambda \vdash t: L$. Then $t \rightarrow^{*} u$, where $u$ is a $\lambda_{\text {low }}$-term in normal form (i.e. a BN normal form).

Notice that the BN normal form $u$ has necessarily a type derivation $\pi^{\prime} \triangleright_{\text {low }} \Lambda \vdash u: L$ (using first-order rules only). Finally, we highlight that the type system is syntax driven. As a consequence:

Proposition 4.7 (Unique Derivation). Let $t$ be a $\lambda_{1}$-term, and $\Lambda$ a ground context. Then there exists at most one type derivation $\pi$ such that $\pi \triangleright \Lambda \vdash t: L$.

This means that for each $\lambda_{1}$-term $t$ and ground context $\Lambda$, there exists at most one ground type $L$ such that $\pi \triangleright \Lambda \vdash t: L$. In particular, the type derivation for a term in BN normal form is uniquely determined. Since all BN normal forms are typable, using subject expansion we have:

Theorem 4.8. Let $t$ be a $\lambda_{1}$-term $t$. If $t$ reduces to $B N$ normal form, then a type derivation $\pi \triangleright \vdash t: L$ exists and is unique.

# 4.4 Putting the Calculus and the Type System at Work 

We illustrate with some examples the expressiveness of the calculus, and the use of the type system.
Expressiveness. Since we have access to the full expressiveness of the untyped $\lambda$-calculus (Remark 4.1), we can use a standard encoding (in its call-by-push-value flavor) of integers, arithmetic, if/then/else, and fixed point combinators.

Example 4.9 (Encoding Recursive Behavior). We are now able to encode Dynamic Bayesian networks, such us the one depicted in Fig. 4 (from [Koller and Friedman 2009], Ch.6). The idea behind this model is that a system evolves with time in a stochastic way. At each time step, one random variable $S_{i+1}$, which depends only on the previous state $S_{i}$, represents the new state, while the observation $\mathrm{O}_{i+1}$ depends only on the current state $\mathrm{S}_{i+1}$. A typical query in these kinds of models is

$$
\operatorname{Pr}\left(S_{n}=s \mid O_{1}=o_{1}, \ldots, O_{n}=o_{n}\right)
$$

which intuitively means: after $n$ time steps, what is the probability of being in a certain state, knowing all the observations? We can write the template of Fig. 4 as follows:

```
t \delta \lambda n . \text { let } s_{0}=\text { bernoulli }_{p} \text { in u } n s_{0}
u \delta \text { fix ! }(\lambda x . \lambda n . \lambda s . \text { if isZero }(n) \text { then } s
    else let \(s^{\prime}=c^{S_{i, s}}\rangle\) in
    let \(o^{\prime}=c^{O_{i, s^{\prime}}}\rangle\) in
    let \(m=\operatorname{pred}(n)\) in
    let \(r=(\operatorname{der} x) m s^{\prime}\)
    in \(\left\langle o^{\prime}, r\right\rangle\) )
```

Then $t \underline{n}$-where $\underline{n}$ is an encoding of the integer $n$-represents the template that is to be unrolled $n$ times. Operationally, we have exactly that the fixed point operator is unfolded $n$ times generating the unrolled Bayesian network. From the point of view of the type system, we have that the type of $t \underline{n}$ depends on the integer $n$ :

$$
\vdash t \underline{n}: \mathrm{O}_{1} \otimes \cdots \otimes \mathrm{O}_{n} \otimes \mathrm{~S}_{n}
$$

The Intersection Types, in use. The term which encodes the BN of Fig. 1 is easily typed in the firstorder fragment-the reader can find the derivation in Example 7.2. Here we give an example of type derivation where multiple copies are involved, so that we need to use the multiset type. First, observe that a type of shape $\left[A_{1}, \ldots, A_{n}\right]$ can be thought of as an informative refinement of the thunk type !A. Sub-terms are typed several times, once for each copy that will be produced during the reduction. This feature is crucial to handle random variables. We stress that the inability to deal with an unbounded number of random variables is the key issue which limits to first-order the compilation of programs into BNs, or data flow analysis (see e.g. [Gorinova et al. 2022; van de Meent et al. 2018]).

Example 4.10 (Multiple Coin Tosses). Consider a term $u$ similar to that in Fig. 5, modeling two tosses of the same (biased) coin: $u \stackrel{\text { a }}{=} \operatorname{let} x=\operatorname{sample}_{d}$ in let $y=!(\boldsymbol{c}(x))$ in $\langle x$, der $y$, der $y\rangle$. For readability, here we use some syntactic sugar. The (unique) type derivation for $u$ is

![img-5.jpeg](img-5.jpeg)

# 5 THE SEMANTICS OF BAYESIAN NETWORKS 

In this section we formally define the semantics of Bayesian networks. First, let us briefly revise the language of Bayesian modeling. For more details, we refer to [Darwiche 2008] for a concise presentation, and to standard texts for an exhaustive treatment [Darwiche 2009; Neapolitan 2003; Pearl 1988].

### 5.1 Random Variables

Bayesian methods provide a formalism for reasoning about partial beliefs under conditions of uncertainty. Since we cannot determine for certain the state of some features of interest, we settle for determining how likely it is that a particular feature is in a particular state. Random variables represent features of the system being modeled. For the purpose of modeling, a random variable can be seen as a name for an atomic proposition (e.g. "Wet") which assumes values from a set of states (e.g. $\{\mathrm{t}, \mathrm{f}\}$ ). The system is modeled as a joint probability distribution on all possible values of the variables of interest - an element in the sample space represents a possible state of the system.

Example 5.1. The canonical sample space sketched in Fig. 2 consists of $2^{4}$ tuples (only some entries are displayed); to each tuple $\bar{x}$ is associated a probability. The event $(R=t)$ contains $2^{3}$ tuples, the event $(R=t, W=t)$ contains $2^{2}$ tuples, and has probability 0.33 .

Remark 5.2. Notice that in Bayesian modeling, random variables are identified first, and only implicitly become functions on a sample space. We refer to the excellent textbook by Neapolitan [Neapolitan 2003] (Ch. 1) for a formal treatment relating the notion of random variable as used in Bayesian inference, with the classical definition of function on a sample space.

Given a countable set Names, we associate to each name $X \in$ Names a set of values, denoted by $\operatorname{Val}(X)$ (typically $\operatorname{Val}(X)=\{t, f\}$ ). From now on, we silently identify a name $X$ with the pair $(X, \operatorname{Val}(X))$, which effectively defines a random variable (r.v.). A finite set of names $\mathbb{X}=\left\{\mathrm{X}_{1}, \ldots, \mathrm{X}_{n}\right\}$ defines a "compound" r.v. whose value set $\operatorname{Val}(\mathbb{X})$ is the Cartesian product $\operatorname{Val}\left(\mathrm{X}_{1}\right) \times \cdots \times \operatorname{Val}\left(\mathrm{X}_{n}\right)$.

Notation 5.3. The metavariables $\mathbb{X}, \mathbb{Y}, \mathbb{Z}$ range over finite sets of names (r.v.s). As standard, a lowercase letter $x$ denotes a generic value $x \in \operatorname{Val}(X)$, and $\bar{x}$ denotes a tuple in the cartesian product $\operatorname{Val}(\mathbb{X}) \triangleq \operatorname{Val}\left(\mathrm{X}_{1}\right) \times \cdots \times \operatorname{Val}\left(\mathrm{X}_{n}\right)$. Moreover, we use juxtaposition as a tuple constructor, e.g. if $x \in \operatorname{Val}(X)$ and $\bar{y} \in \operatorname{Val}\left(Y_{1}\right) \times \cdots \times \operatorname{Val}\left(Y_{n}\right)$, then $x \bar{y} \in \operatorname{Val}(X) \times \operatorname{Val}\left(Y_{1}\right) \times \cdots \times \operatorname{Val}\left(Y_{n}\right)$. Given a subset $\mathbb{Y} \subseteq \mathbb{X}$, we denote by $\left.\bar{x}\right|_{\mathbb{Y}}$ the restriction of $\bar{x}$ to $\mathbb{Y}\left(\right.$ so, $\left.\bar{x}\right|_{\mathbb{Y}} \in \operatorname{Val}(\mathbb{Y})$ ). Given two sets of names $\mathbb{X}$ and $\mathbb{Y}$, we say that $\bar{x} \in \operatorname{Val}(\mathbb{X})$ and $\bar{y} \in \operatorname{Val}(\mathbb{Y})$ agree on the common names $(\bar{x} \sim \bar{y}$ for short) whenever $\left.\bar{x}\right|_{\mathbb{X} \cap \mathbb{Y}}=\left.\bar{y}\right|_{\mathbb{X} \cap \mathbb{Y}}$.

### 5.2 Factors, Sum and Product Operations

Inference algorithms rely on basic operations on a class of functions known as factors, which generalize the notions of probability distribution and of conditional distribution. Factors will be the key ingredients also in our semantics.

Definition 5.4 (Factor). A factor $\underset{\sim}{\mathbb{X}}$ over a set of names (r.v.s) $\mathbb{X}$ is a function $\underset{\sim}{\mathbb{X}}: \operatorname{Val}(\mathbb{X}) \rightarrow \mathbb{R}_{\geq 0}$ mapping each tuple $\bar{x} \in \mathbb{X}$ to a non-negative real.

When $\mathbb{X}$ is clear from the context, we simply write $\phi$ (omitting the superscript $\mathbb{X}$ ); then $\operatorname{Nm}(\phi)$ denotes $\mathbb{X}$. Letters $\phi, \psi$ range over factors. Please notice that in the literature about BNs, $\phi(\bar{x})$ is often written $\phi_{\bar{y}}$. We adopt this convenient notation when making explicit calculations.

Example 5.5. Factors generalize familiar concepts from probability theory.

- A joint probability distribution over the set $\mathbb{X}$ is a factor $\phi$ which maps each tuple $\bar{x} \in \operatorname{Val}(\mathbb{X})$ to a probability $\phi(\bar{x})$ such that $\sum_{\bar{x} \in \operatorname{Val}(\mathbb{X})} \phi(\bar{x})=1$.

- A conditional probability table (CPT) for $X$ given $\mathbb{Y}$ is a factor $\frac{\{X\} \cup \mathbb{Y}}{\phi}$ which maps each tuple $x \bar{y} \in \operatorname{Val}(\{X\} \cup \mathbb{Y})$ to a probability $\phi(x \bar{y})$ such that for each $\bar{y} \in \mathbb{Y}, \sum_{x \in \operatorname{Val}(X)} \phi(x \bar{y})=1 .{ }^{3}$

Factors come with two important operations: sum (out) and product. Summing out a name (r.v.) Z from a factor means that we are removing Z, thus obtaining a smaller factor. As depicted in Fig. 2, intuitively we do so by merging all tuples which agree on all the other variables but Z.

Definition 5.6 (Sum Out). The sum out of $\mathbb{Z} \subseteq \mathbb{X}$ from $\stackrel{\mathbb{X}}{\phi}$ is a factor $\sum_{\mathbb{Z}} \phi$ over $\mathbb{Y} \triangleq \mathbb{X}-\mathbb{Z}$, defined as:

$$
\left(\sum_{\mathbb{Z}} \phi\right)(\bar{y}) \triangleq \sum_{\bar{x} \in \operatorname{Val}(\mathbb{Z})} \phi(\bar{x} \bar{y})
$$

Multiplication of factors is defined in such a way that only "coherent" pairs are multiplied.
Definition 5.7 (Product). The product of $\stackrel{\mathbb{X}}{\phi_{1}}$ and $\stackrel{\mathbb{Y}}{\phi_{2}}$ is a factor $\phi_{1} \odot \phi_{2}$ over $\mathbb{Z} \triangleq \mathbb{X} \cup \mathbb{Y}$, defined as:

$$
\left(\phi_{1} \odot \phi_{2}\right)(\bar{x}) \triangleq \phi_{1}(\bar{x}) \phi_{2}(\bar{y}) \quad \text { where } \bar{x}=\left.\bar{x}\right|_{\mathbb{X}} \text { and } \bar{y}=\left.\bar{x}\right|_{\mathbb{Y}}
$$

We denote $n$-ary products by $\bigcirc_{n} \phi_{n}$. We denote by $\mathbf{1}_{\mathbb{Y}} \triangleq \stackrel{\mathbb{Y}}{\mathbf{1}}$ the factor over the set of names $\mathbb{Y}$, sending every tuple of $\operatorname{Val}(\mathbb{Y})$ to 1 . Observe that $\stackrel{\mathbb{X}}{\phi} \odot \stackrel{\mathbb{Y}}{\mathbf{1}}=\stackrel{\mathbb{X}}{\phi}$ if $\mathbb{Y} \subseteq \mathbb{X}$. Factors over an empty set of variables are allowed, and called trivial. In particular, we write $\mathbf{1}_{\emptyset} \triangleq \stackrel{\emptyset}{\mathbf{1}}$ for the trivial factor assigning 1 to the empty tuple. Product and summation are both commutative, product is associative, and-crucially-they distribute under suitable conditions:

$$
\text { If } \mathbb{Z} \cap \operatorname{Nm}\left(\phi_{1}\right)=\emptyset \text { then } \sum_{\mathbb{Z}}\left(\phi_{1} \odot \phi_{2}\right)=\phi_{1} \odot\left(\sum_{\mathbb{Z}} \phi_{2}\right)
$$

This distributivity is the key property on which exact inference algorithms rely. CPT's being factors, they admit sum and product operations. Please notice that the result of such operations is not necessarily a CPT, but, of course, it is a factor.

Remark 5.8 (Cost of Operations on Factors). Summing out any number of variables from a factor $\phi$ demands $O(\exp (w))$ time and space, where $w$ is the number of variables over which $\phi$ is defined. Multiplying $k$ factors demands $O(k \cdot \exp (w))$ time and space, where $w$ is the number of variables in the resulting factor.

# 5.3 The Semantics of Bayesian Networks 

Bayesian networks are graph-theoretic objects able to represent large probability distributions compactly, via a factorized representation. Inference algorithms then implement factorized computations.

Definition 5.9. A Bayesian network $\mathcal{B}$ over the set of r.v.s $\mathbb{X}$ is a pair $(\mathcal{G}, \mathcal{T})$ where:

- $\mathcal{G}$ is a directed acyclic graph (DAG) over the set of nodes $\mathbb{X}$.
- $\mathcal{T}$ assigns, to each variable $X \in \mathbb{X}$ a conditional probability table (a CPT), which is a factor $\phi^{X}$ over variables $\{X\} \cup \operatorname{Pa}(X)$, where $\operatorname{Pa}(X)$ denotes the set of parents of $X$ in $\mathcal{G}$.

The graph structure and independence assumptions on it yield the correctness of the semantics.

[^0]
[^0]:    ${ }^{3}$ Please notice that here, and in the following definition of sum out, we slightly abuse the notation. In fact, as standard, we consider the tuples as sequences indexed by the set of random variables. Every time, we present the tuples ordered in the most convenient way for a compact definition.

Theorem 5.10 (Pearl [1986]). A Bayesian network $\mathcal{B}$ over the set of r.v.s $\mathbb{X}$ defines a unique probability distribution over $\mathbb{X}$ (its semantics):

$$
\llbracket \mathcal{B} \rrbracket \triangleq \bigodot_{\mathrm{X} \in \mathbb{X}} \phi^{\mathrm{X}}
$$

Please notice also that, given a Bayesian network $\mathcal{B}$ defining a probability distribution over $\mathbb{X}$, the marginal distribution of $\llbracket \mathcal{B} \rrbracket$ over a subset $\mathbb{Y} \subseteq \mathbb{X}$ is defined by $\sum_{\mathbb{X}-\mathbb{Y}} \llbracket \mathcal{B} \rrbracket$.

# 6 THE SEMANTICS OF TYPED TERMS 

This section contains the main result of this paper, namely the fact that we can endow terms of ground type with a factor-based semantics that reflects the probabilistic behavior of the term. Moreover, we prove that the semantics is compositional, in the sense that it can be computed following the structure of intersection type derivations.

Semantics of the Probabilistic Axioms. The intuition guiding the definition of our semantics is the very definition of the semantics of a BN, as we have just seen in Sect. 5.3. In general, this depends only on the CPT's which are assigned to each random variable. We apply the same principle in the realm of (intersection) typed $\lambda$-terms. The idea is that we can associate a CPT to each probabilistic axiom in a type derivation, and then we define the semantics of the typed term as their product (as factors), summing out the names not occurring in the final type judgment to obtain the marginal which is specified by the term. We start by formally defining the factor which is associated to a probabilistic axiom. We give an example of how the following definitions work in Fig. 8.

Definition 6.1 (Probabilistic Axioms). Recall that we identify each name $X$ with the pair $(X, \operatorname{Val}(X))$, effectively defining a r.v. (see Sect. 5.1).

- I-SAMPLE. We associate to the axiom $\Lambda \vdash$ sample $_{d}: X$ the factor $\phi$ over the r.v. $\{X\}$ such that $\phi(\mathrm{x}) \triangleq d(\mathrm{x})$ for each $\mathrm{x} \in \operatorname{Val}(\mathrm{X})$.
- I-COND. Let us consider the following instance of the I-COND axiom.

$$
\frac{X \notin\left\{\mathrm{Y}_{1}, \ldots, \mathrm{Y}_{n}\right\} \text { and } X \notin \operatorname{Nm}(\Lambda)}{\Lambda, y_{1}: \mathrm{Y}_{1}, \ldots y_{n}: \mathrm{Y}_{n} \vdash \text { case }\left\langle y_{1}, \ldots, y_{n}\right\rangle \text { of }\left\{\overline{\mathrm{b}} \Rightarrow \operatorname{sample}_{d_{\overline{\mathrm{b}}}}\right\}_{\overline{\mathrm{b}} \in\{\mathrm{t}, \mathrm{f}\} \in}: \mathrm{X}} \text { I-COND }
$$

We associate to this axiom the factor $\phi$ over the set of r.v.s $\left\{\mathrm{Y}_{1}, \ldots, \mathrm{Y}_{n}, \mathrm{X}\right\}$, such that $\phi(\overline{\mathrm{b}} \mathrm{x}) \triangleq$ $d_{\overline{\mathrm{b}}}(\mathrm{x})$, for each $\overline{\mathrm{b}} \mathrm{x} \in \operatorname{Val}\left(\mathrm{Y}_{1}\right) \times \cdots \times \operatorname{Val}\left(\mathrm{Y}_{n}\right) \times \operatorname{Val}(\mathrm{X})^{1}$.

[^0]$\Lambda \vdash$ bernoulli $0.2: R$
I-SAMPLE

$$
\phi_{1} \triangleq \begin{array}{l|l}
R & \operatorname{Pr}(R) \\
t & 0.2 \\
f & 0.8
\end{array}
$$

$$
\Lambda, r: R \vdash \text { case } r \text { of }\left\{\mathrm{t}=\text { bernoulli }_{0.7} ; \mathrm{f}=\text { bernoulli }_{0.01}\right\}: \mathrm{W}
$$


Fig. 8. The factor associated to this I-SAMPLE axiom is $\phi_{1}$. The factor associated to this I-COND axiom is $\phi_{2}$. For example, $\phi_{2}(\mathrm{tf}) \triangleq$ bernoulli $_{0.7}(\mathrm{f})$.


[^0]:    ${ }^{4}$ Please notice that we are a bit informal here, because we assume that $\mathrm{Y}_{1}, \ldots, \mathrm{Y}_{n}$ are pairwise distinct. This is not an obligation, so the actual definition is more involved. This is, however, just a technical point that does not affect the meaning of the definition. For the sake of completeness, we provide the technically precise definition in the Tech. Report.

Semantics of a Type Derivation. Once given the interpretation of the probabilistic axioms, it is straightforward to extend the interpretation to any type derivation of ground type. We multiply all the factors associated to the axioms, and then sum out all the names not appearing in the conclusion.

Definition 6.2 (Semantics of a Type Derivation). Let $\pi \triangleright J$ be a type derivation, $\operatorname{Cpts}(\pi)$ the set of factors associated to its probabilistic axioms, and $\mathbb{X}=\bigcup_{\phi \in \operatorname{Cpts}(\pi)} \operatorname{Nm}(\phi)$. Then the semantics of $\pi$ is:

$$
\llbracket \pi \rrbracket \triangleq \sum_{\mathbb{X}-\operatorname{Nm}(J)}\left(\bigodot_{\phi \in \operatorname{Cpts}(\pi)} \phi\right)
$$

Remark 6.3. If $\pi$ is a type derivation such that $\operatorname{Cpts}(\pi)=\emptyset$, then $\llbracket \pi \rrbracket=\mathbf{1}_{\emptyset}$. Notice, in particular, that this is the case for each I-VAR axiom.

On Compositionality. One immediately notices that the above definition of semantics does not look compositional. Indeed, the semantics of a type derivation $\pi$ is computed looking globally at $\pi$, in particular at its probabilistic axioms. We ask ourselves, and we answer in the positive, if it is possible to give a more local, modular way, of computing the very same semantics. Informally, given a type derivation $\pi$ obtained from the composition of $\pi_{1}, \ldots, \pi_{n}$, such as

$$
\pi \quad \triangleq \quad \frac{\pi_{1} \quad \ldots \quad \pi_{n}}{J}
$$

we would like to obtain $\llbracket \pi \rrbracket$ from $\llbracket \pi_{1} \rrbracket, \ldots, \llbracket \pi_{n} \rrbracket$. In particular, following the pattern of Definition 6.2, we could write:

$$
\llbracket \pi \rrbracket=\sum_{\mathbb{Z}}\left(\bigodot_{i} \llbracket \pi_{i} \rrbracket\right) \quad \text { where } \mathbb{Z}=\bigcup_{i} \operatorname{Nm}\left(\llbracket \pi_{i} \rrbracket\right)-\operatorname{Nm}(J)
$$

In words, composition is obtained by first performing the product $\bigodot_{i} \llbracket \pi_{i} \rrbracket$-which yields a factor over the names $\bigcup_{i} \operatorname{Nm}\left(\llbracket \pi_{i} \rrbracket\right)$ - and then marginalizing, by summing out the names which do not appear in the conclusion $J$. Such a notion of composition is yet a variant of the pervasive paradigm composition = parallel composition + hiding.
The problem now is that the equation 3 is not a priori true. This is because sum out and product do not distribute in general, but only under suitable conditions. The type system design is crucial to guarantee that the factors semantics is indeed compositional. We illustrate this fact with an example.

Example 6.4 (Types and Compositionality.). Consider the following derivation, which is non well-typed because the names introduced by the first and third probabilistic axiom are not distinct. Below, $\mathbf{c}^{1}, \mathbf{c}^{3}$ are sample terms, and $\mathbf{c}^{2}\left(z_{i}\right), \mathbf{c}^{4}\left(z^{\prime}\right)$ are case expressions. The terms $t, u$ are those typed by $\pi_{1}, \rho_{1}$, respectively. The premise $\rho_{2}$ is the obvious derivation of $x: X, y: Y \vdash\langle x, y\rangle: X \otimes Y$.

$$
\begin{aligned}
& \frac{\vdash \mathbf{c}^{1}: \mathrm{Z} \diamond \phi^{\mathrm{2}}}{\pi_{1} \triangleright \operatorname{let} z=\mathbf{c}^{1} \text { in } \mathbf{c}^{2}(z): \mathrm{X}} \stackrel{\{Z, X\}}{\phi^{\mathrm{Z}}} \quad \frac{x: \mathrm{X} \vdash \mathbf{c}^{3}: \mathrm{Z} \diamond \phi^{\mathrm{2}}}{\rho_{1} \triangleright x: \mathrm{X} \vdash \operatorname{let} z^{\prime}=\mathbf{c}^{3} \text { in } \mathbf{c}^{4}\left(z^{\prime}\right): \mathrm{Y}} \stackrel{\{Z, Y\}}{\phi^{3}} \\
& \frac{\pi_{2} \triangleright x: X \vdash \operatorname{let} y=u \text { in }\langle x, y\rangle: X \otimes Y}{\pi \triangleright \vdash t \operatorname{in} \operatorname{let} y=u \text { in }\langle x, y\rangle: X \otimes Y}
\end{aligned}
$$

We annotate each of the four probabilistic axioms with the corresponding CPT. It is easy to check that compositionality (Eq. (3)) does not hold, because $\llbracket \pi \rrbracket=\sum_{Z}\left(\phi^{1} \odot \phi^{2} \odot \phi^{3} \odot \phi^{4}\right) \neq\left(\sum_{Z} \phi^{1} \odot\right.$ $\left.\phi^{2}\right) \odot\left(\sum_{Z} \phi^{3} \odot \phi^{4}\right)=\llbracket \pi_{1} \rrbracket \odot \llbracket \pi_{2} \rrbracket$. Observe that $\llbracket \pi \rrbracket$ is a factor over $\{\mathrm{X}, \mathrm{Y}\}, \llbracket \pi_{1} \rrbracket$ over $\{\mathrm{X}\}$, and $\llbracket \pi_{1} \rrbracket$ over $\{\mathrm{Y}\}$. So for example we have:
$\llbracket \pi \rrbracket_{\mathrm{tt}}=\phi_{\mathrm{t}}^{1} \cdot \phi_{\mathrm{tt}}^{2} \cdot \phi_{\mathrm{t}}^{3} \cdot \phi_{\mathrm{tt}}^{4}+\phi_{\mathrm{f}}^{1} \cdot \phi_{\mathrm{ft}}^{2} \cdot \phi_{\mathrm{f}}^{3} \cdot \phi_{\mathrm{ft}}^{4} \quad \llbracket \pi_{1} \rrbracket_{\mathrm{t}}=\phi_{\mathrm{t}}^{1} \cdot \phi_{\mathrm{tt}}^{2}+\phi_{\mathrm{f}}^{1} \cdot \phi_{\mathrm{ft}}^{2} \quad \llbracket \pi_{2} \rrbracket_{\mathrm{t}}=\phi_{\mathrm{t}}^{3} \cdot \phi_{\mathrm{tt}}^{4}+\phi_{\mathrm{f}}^{3} \cdot \phi_{\mathrm{ft}}^{4}$
Therefore $\llbracket \pi \rrbracket_{\mathrm{tt}} \neq\left(\phi_{\mathrm{t}}^{1} \cdot \phi_{\mathrm{tt}}^{2}+\phi_{\mathrm{f}}^{1} \cdot \phi_{\mathrm{ft}}^{2}\right) \cdot\left(\phi_{\mathrm{t}}^{3} \cdot \phi_{\mathrm{tt}}^{4}+\phi_{\mathrm{f}}^{3} \cdot \phi_{\mathrm{ft}}^{4}\right)=\llbracket \pi_{1} \rrbracket_{\mathrm{t}} \cdot \llbracket \pi_{2} \rrbracket_{\mathrm{t}}=\left(\llbracket \pi_{1} \rrbracket \odot \llbracket \pi_{2} \rrbracket\right)_{\mathrm{tt}}$.
Proc. ACM Program. Lang., Vol. 8, No. POPL, Article 84. Publication date: January 2024.

Proving Compositionality. We are ready to prove that $\llbracket \pi \rrbracket$ can be compositionally defined for every typed derivation $\pi \triangleright \Lambda \vdash t: L$. The crucial property-guaranteed by the type system-is that $\pi$ is well-formed, in the technical sense given below. Such a property is the key ingredient in the proof of compositionality, because it ensures the distributivity of the sum over the product.

Definition 6.5 (Well-Formedness).

1. The type derivations $\pi_{1} \triangleright J_{1}, \ldots, \pi_{n} \triangleright J_{n}$ are compatible if

$$
\text { exists } j \text { s.t. } \mathrm{Z} \in \operatorname{Nm}\left(\pi_{j}\right) \text { and } \mathrm{Z} \notin \operatorname{Nm}\left(J_{j}\right) \quad \Rightarrow \quad \mathrm{Z} \notin \operatorname{Nm}\left(\pi_{i}\right) \text { for any } i \neq j
$$

2. A type derivation $\pi$ is well-formed if for every rule in $\pi$, its premises are compatible.

Lemma 6.6 (Well-Formed Derivations). Every type derivation $\pi \triangleright \Lambda \vdash t: L$ is well-formed.
We postpone to Sect. 7 the discussion of the proof, which relies on a fine analysis of the flow of the computation. Using this result, we are able to prove that the semantics-that we have defined in a global way-can indeed be computed compositionally, validating Eq. (3).

Proposition 6.7 (Compositionality). Let $\pi \triangleright J$ be the following type derivation:

$$
\frac{\pi_{1} \triangleright J_{1} \quad \ldots \quad \pi_{n} \triangleright J_{n}}{\pi \triangleright J}
$$

If $\pi_{1}, \ldots, \pi_{n}$ are compatible, then:

$$
\llbracket \pi \rrbracket=\sum_{\mathbb{Z}}\left(\bigodot_{i} \llbracket \pi_{i} \rrbracket\right) \quad \text { where } \mathbb{Z} \triangleq \bigcup_{i} \operatorname{Nm}\left(\llbracket \pi_{i} \rrbracket\right)-\operatorname{Nm}(J)
$$

Proof. Wlog, consider $n=2$. Let us set $\Phi_{\pi} \triangleq \bigodot_{\psi \in \operatorname{Cpts}(\pi)} \psi$ for each derivation $\pi$. By Def. 6.2, we can write $\llbracket \pi_{i} \rrbracket=\sum_{\mathbb{W}_{1}} \Phi_{\pi_{i}}$, where $\mathbb{W}_{i}=\operatorname{Nm}\left(\Phi_{\pi_{i}}\right)-\operatorname{Nm}\left(J_{i}\right)(i \in\{1,2\})$. Crucially, since $\pi_{1}$ and $\pi_{2}$ are compatible, $\mathbb{W}_{1} \cap \operatorname{Nm}\left(\pi_{2}\right)=\emptyset$ and $\mathbb{W}_{2} \cap \operatorname{Nm}\left(\pi_{1}\right)=\emptyset$. Hence, by Eq. (2), sum and product distribute, and we have:

$$
\llbracket \pi_{1} \rrbracket \odot \llbracket \pi_{2} \rrbracket=\sum_{\mathbb{W}_{1}} \Phi_{\pi_{1}} \odot \sum_{\mathbb{W}_{2}} \Phi_{\pi_{2}}=\sum_{\mathbb{W}_{1}} \sum_{\mathbb{W}_{2}}\left(\Phi_{\pi_{1}} \odot \Phi_{\pi_{2}}\right)=\sum_{\mathbb{W}_{1}} \sum_{\mathbb{W}_{2}} \Phi_{\pi}
$$

where we used the fact that $\operatorname{Cpts}(\pi)=\operatorname{Cpts}\left(\pi_{1}\right) \cup \operatorname{Cpts}\left(\pi_{2}\right)$. Now let $\mathbb{Y}_{i} \triangleq \operatorname{Nm}\left(\llbracket \pi_{i} \rrbracket\right)$; since $\operatorname{Nm}\left(\Phi_{\pi_{i}}\right)=\mathbb{Y}_{i} \uplus \mathbb{W}_{i}$ and, by the compatibility of $\pi_{1}$ and $\pi_{2}, \mathbb{W}_{i} \cap \operatorname{Nm}\left(\Phi_{\pi_{j}}\right)=\emptyset$ for $i \neq j$, we have

$$
\operatorname{Nm}\left(\Phi_{\pi}\right)=\left(\mathbb{Y}_{1} \cup \mathbb{Y}_{2}\right) \uplus\left(\mathbb{W}_{1} \uplus \mathbb{W}_{2}\right)
$$

Let $\mathbb{Z} \triangleq\left(\mathbb{Y}_{1} \cup \mathbb{Y}_{2}\right)-\operatorname{Nm}(J)$; by Eq. (5) and compatibility, $\operatorname{Nm}\left(\Phi_{\pi}\right)-\operatorname{Nm}(J)=\mathbb{Z} \uplus \mathbb{W}_{1} \uplus \mathbb{W}_{2}$. Therefore

$$
\sum_{\mathbb{Z}}\left(\llbracket \pi_{1} \rrbracket \odot \llbracket \pi_{2} \rrbracket\right)=\sum_{\mathbb{Z}} \sum_{\mathbb{W}_{1}} \sum_{\mathbb{W}_{2}} \Phi_{\pi}=\sum_{\operatorname{Nm}\left(\Phi_{\pi}\right)-\operatorname{Nm}(J)} \Phi_{\pi} \triangleq \llbracket \pi \rrbracket
$$

where we sum out $\mathbb{Z}$ from both sides of Eq. (4).
Inductive Interpretation of Type Derivations. Now that we have proved that our semantics is compositional, we are able to compute it inductively, starting from the axioms, and then following the structure of the type derivation. Probabilistic axioms are assigned a CPT as indicated in Def. 6.1. The I-VAR axioms are assigned the trivial factor $\mathbf{1}_{\emptyset}$ (see Remark 6.3). Then the semantics of each sub-derivation is inductively obtained following Prop. 6.7. In Fig. 9 we decorate the intersection type system with factors, according to this process. A decorated type judgment is written $\Sigma \vdash t: A \circ \psi$, where $\psi$ is the inductively computed factor.

Lemma 6.8. Let $\pi \triangleright J \circ \psi$ be a well-formed type derivation. Then $\llbracket \pi \rrbracket=\psi$.

![img-6.jpeg](img-6.jpeg)

Fig. 9. Inductive Interpretation of typed terms (judgments are annotated-in blue-with their interpretation).

Proof. By induction on the derivation. The property trivially holds for all axioms. Assume that $\pi \triangleright J \diamond \psi_{i}$ is obtained from derivations $\pi_{i}(1 \leq i \leq n)$. Since $\pi$ is well-formed, by definition of well-formedness also the derivations $\pi_{i}$ are well-formed. Then by i.h., $\psi_{i}=\llbracket \pi_{i} \rrbracket$. Thus, by letting $\mathbb{Z} \triangleq \bigcup_{i} \operatorname{Nm}\left(\psi_{i}\right)-\operatorname{Nm}(J)$, we have

$$
\psi:=\sum_{\mathbb{Z}}\left(\bigodot_{i} \psi_{i}\right)=\sum_{\mathbb{Z}}\left(\bigodot_{i} \llbracket \pi_{i} \rrbracket\right)=\llbracket \pi \rrbracket
$$

where the last equality follows from Prop. 6.7.
Since derivations of ground type are always well-formed (Lemma 6.6), we have proved that:
Theorem 6.9. Let $\pi \triangleright \Lambda \vdash t: L \diamond \psi$ be a derivation of ground type. Then $\llbracket \pi \rrbracket=\psi$.
This theorem states that the semantics $\llbracket \pi \rrbracket$ (as in Def. 6.2) of a type derivation $\pi$ can be inductively computed, as described in Fig. 9.

Invariance of the Semantics. The semantics is invariant under reduction and expansion. This is due to the fact that probabilistic axioms are stable w.r.t. reduction and expansion.

Theorem 6.10 (Invariance). Let $t$ be a $\lambda_{1}$-term and $t \rightarrow u$. Then: $\Lambda \vdash t: L \diamond \psi \Leftrightarrow \Lambda \vdash u: L \diamond \psi$.
Semantics Completion. We conclude with a remark. The reader may expect that the interpretation of a type derivation $\pi \triangleright J$ were a factor over $\operatorname{Nm}(J)$. For example, one could expect the interpretation of an identity axiom to be $y: \mathrm{Y} \vdash y: \mathrm{Y} \diamond \stackrel{(\mathrm{Y})}{1}$ instead of $y: \mathrm{Y} \vdash y: \mathrm{Y} \diamond \stackrel{\emptyset}{1}$. The fact is that our semantics focuses only on the probabilistic content of the derivation $\pi \triangleright J$. Please notice

that the non-probabilistic information is already fully contained in the type judgment $J$, because intersection types carry such information. Indeed, an interpretation of $\pi \triangleright J$ as a factor over $\operatorname{Nm}(J)$ is easily obtained by a form of completion. We give more details in the Tech. Report. We mention also that the completed interpretation is a needed step to bridge the gap between our semantics and weighted relational models/probabilistic coherence spaces such as [Ehrhard et al. 2014; Ehrhard and Tasson 2019; Laird et al. 2013].

# 7 BAYESIAN NETWORKS GO WITH THE FLOW 

In this section we prove two results which we have already anticipated:

- we show that every (closed) term $t$ of ground type corresponds to a Bayesian network $\mathcal{B}_{t}$, and that the two have the same semantics. ${ }^{5}$
- we prove the central result making the semantics of terms compositional, namely that every type derivation $\pi \triangleright \Lambda \vdash t: L$ is well-formed (Lemma 6.6).
The key ingredient underlying both results is the same: we associate to each type derivation $\pi$ a directed graph-flow $(\pi)$-which essentially describes the flow of the computation in $\pi$. The crucial fact is proving that flow $(\pi)$ is acyclic. Our argument exploits sophisticated techniques borrowed from the theory of Linear Logic, and in particular from Girard's Geometry of Interaction [Accattoli et al. 2020a, 2021a,b; Dal Lago et al. 2017; Girard 1989]. In order to convey more clearly the basic ideas, here we give the definitions only for the low-level fragment. Recall that this fragment suffices to type every BN normal form. The development for the full higher-order calculus is in the Tech. Report.

The Flow Graph of a Type Derivation is a DAG. Intuitively, the graph we are going to build tracks the occurrences of atomic types (i.e. the random variables) throughout the type derivation. We indicate a specific occurrence of an atom inside a ground type $L$ by means of a (type) context, i.e. a type with a hole, as follows:

Ground Type Ctxs $\underline{K}, \underline{L} \quad::=\quad(\cdot)|\underline{K} \otimes L| K \otimes \underline{L}$
So $\underline{L}$ denotes an occurrence of atom (here X ) inside the type $L \triangleq \underline{L}(\mathrm{X})$. Notice for example that the type $(X \otimes X) \otimes Y$ contains three occurrences of atoms. Given a type derivation $\pi$, we assume given a distinct label to each occurrence of atom appearing in each judgment of $\pi$. We call such a label a position. We can now build a graph that has all the positions of $\pi$ as vertices, and that tracks the flow of each name $X$.

Definition 7.1 (Flow Graph). Let $\pi \triangleright \Lambda \vdash t: L$. The flow graph flow $(\pi)$ of $\pi$ is the directed graph which has as vertices all the positions occurring in $\pi$, and edges as indicated in Fig. 10.

Example 7.2. We show the type derivation for the term (1) encoding our initial example, annotated with the flow graph. The reader can already notice that the flow exactly matches the DAG corresponding to the Bayesian network in Fig. 1.
![img-7.jpeg](img-7.jpeg)

We will exploit the fact that the flow graph of a type derivation of ground type is acyclic.

[^0]
[^0]:    ${ }^{5}$ Precisely, the joint distribution underlying $t$ and $\mathcal{B}_{t}$ is exactly the same. We then have to take into account that, in general, the term $t$ encodes also a query, defining a marginal of the full joint distribution (Thm. 7.1).

![img-8.jpeg](img-8.jpeg)

Ground Contexts:
$\frac{\Lambda \vdash u: \underline{K}\{\mathrm{X}\} \quad \Lambda, x: \underline{K}\{\mathrm{X}\} \vdash t: \underline{L}\{\mathrm{Y}\}}{\Lambda \vdash \text { let } x=u \text { in } t: \underline{L}\{\mathrm{Y}\}}$ I-LET $\quad \Lambda, x: \underline{L}\{\mathrm{X}\} \vdash \ldots \quad \Lambda, x: \underline{L}\{\mathrm{X}\} \vdash \ldots$

Fig. 10. Flow graph on the low-level fragment. The flow graph for the full calculus is defined in the Tech. Report.

Proposition 7.3 (The Flow is Acyclic). Let $\pi \triangleright \Lambda \vdash t: L$. Then flow $(\pi)$ is a $D A G$.
Proof Sketch. If $t$ is in normal form, it is immediate to verify (by induction on the derivation $\pi)$ that flow $(\pi)$ is acyclic. If $t$ is not in normal form, by Thm. 4.6 we know that there exists a term $u$ in normal form such that $t \rightarrow^{*} u$. It is then enough to prove that cycles are preserved along a reduction sequence, which we do by strengthening the subject reduction statement.

# 7.1 Terms and Bayesian Networks: Soundness and Completeness 

We can encode any Bayesian network $\mathcal{B}$ with a low-level term $t_{\mathcal{B}}$, in the standard way; it is immediate to check that $\mathcal{B}$ and $t_{\mathcal{B}}$ have the same semantics. Conversely, the flow graph gives us a way to extract a Bayesian network $\mathcal{B}_{t}$ from every term $t$ of ground type. Indeed, each probabilistic axiom corresponds to a random variable, and the dependencies between probabilistic axioms in the flow graph correspond to the edges in the Bayesian network. We have already illustrated this process in Example 7.2. More formally, we extract a Bayesian network as follows. For clarity, we focus on closed terms. If the term is not closed, what we would extract is a conditional Bayesian network.

Definition 7.4 (BN Extraction). Let $t$ be a closed $\lambda_{1}$-term of ground type. The derivation $\pi \triangleright \vdash t: L$ defines a Bayesian network $\mathcal{B}_{t}=(\mathcal{G}, \mathcal{T})$ over $\mathrm{Nm}(\pi)$ where:

- $\mathcal{T}$ maps each name $\mathrm{X} \in \operatorname{Nm}(\pi)$ to the factor which is associated to the axiom introducing X .
- $\mathcal{G}$ is obtained from flow $(\pi)$ by collapsing all the vertices labeled by the same name.

This extraction process is correct, in the following sense (the proof is straightforward).
Theorem 7.1 (From Ground Type Terms to BNs). Let $\pi \triangleright \vdash t: L$ be a derivation of ground type, and $\mathcal{B}_{t}$ the Bayesian network associated to it, as in Def. 7.4. Then

$$
\llbracket \pi \rrbracket=\sum_{\mathrm{Nm}(\pi)-\mathrm{Nm}(L)} \llbracket \mathcal{B}_{t} \rrbracket
$$

### 7.2 From DAGs to Compositionality

We use the technology of the flow graph also to prove the fundamental result which we used to determine compositionality, namely that all derivations of ground type are well-formed (Lemma 6.6). The crucial property is the following, which is remarkably reminiscent of the characterizing property of jointrees, the data structure underlying the message passing algorithm for exact inference on BNs. The proof relies on the fact that the flow graph is a DAG.

Lemma 7.5 (Named Paths). Let $\pi \triangleright \Lambda \vdash t: L$, and let X be the main name of a probabilistic axiom $\alpha^{\mathrm{X}}$. Then in flow $(\pi)$, each position with name X is connected to the occurrence of X in $\alpha^{\mathrm{X}}$ by a path where all positions have name X .

Then, we are finally able to give the proof of Lemma 6.6.

Proof of Lemma 6.6. We prove that each rule in $\pi \triangleright \Lambda \vdash t: L$ has compatible premises. Let $\pi_{1} \triangleright J_{1}, \ldots, \pi_{n} \triangleright J_{n}$ be the premises of a rule in $\pi$. Assume there exists a $\pi_{j}$ such that $X \in \operatorname{Nm}\left(\pi_{j}\right)$ and $X \notin \operatorname{Nm}\left(J_{j}\right)$. It is easy to see that $X$ is necessarily the main name of a probabilistic axiom $\alpha^{X}$ in $\pi_{j}$. By Lemma 7.5, each position with name $X$ in flow $(\pi)$ is connected to the occurrence of $X$ in $\alpha^{X}$ by a path where all positions have name $X$. Since $X \notin \operatorname{Nm}\left(J_{j}\right)$, it is impossible that $X \in \operatorname{Nm}\left(\pi_{i}\right)$ for $i \neq j$.

# 8 DEALING WITH EVIDENCE, AKA COMPUTING THE POSTERIOR 

Quoting [Gordon et al. 2014], inference is the task of "computing an explicit representation of the probability distribution implicitly specified by a probabilistic program". So far, we have focused on the computation of marginals, without explicitly dealing with evidence. Admittedly, the most interesting inference problem is to compute a posterior distribution, such as $\operatorname{Pr}($ Rain $|\mathrm{We} t=t)$. We know that this is the same as $\operatorname{Pr}($ Rain, Wet $=\mathrm{t}) / \operatorname{Pr}(\mathrm{Wet}=\mathrm{t})$ (as recalled in Sect. 2). In standard practice, to compute a posterior means to compute the unnormalized posterior

$$
\operatorname{Pr}(\text { Rain, Wet }=\mathrm{t})
$$

We can then normalize (6) by dividing for $\operatorname{Pr}($ Wet $=\mathrm{t})$, which is also available-for free-from (6), just by adding up all the probabilities appearing in it. Indeed, $\operatorname{Pr}(\mathrm{We} t=t)=\sum_{\text {Rain }} \operatorname{Pr}($ Rain, Wet $=\mathrm{t})$.

Technically, in the setting of BNs (and in our setting), there is no essential difference between computing a marginal like $\operatorname{Pr}($ Rain, Wet $=\mathrm{t})$ or a marginal like $\operatorname{Pr}($ Rain, Wet $)$. The key to deal with evidence (such as Wet $=\mathrm{t}$ ) is to update each CPT in the model, by zeroing out those rows that are inconsistent with the observed data. The resulting factors are no longer normalized, but are still valid factors, and their product gives the unnormalized posterior distribution. We illustrate this with an example, referring to [Darwiche 2009] (Ch. 6.7) or [Koller and Friedman 2009] (Ch. 9.3.2) for the details.

Example 8.1 (Basic). Consider a simple BN of graph Rain $\rightarrow$ Wet. The factors associated to Rain and Wet are respectively $\phi_{1}$ and $\phi_{2}$, as given in Fig. 8. We know (Sect. 5.3) that $\operatorname{Pr}($ Rain, Wet $)=\phi_{1} \odot \phi_{2}$. Assume we have evidence $\mathrm{e} \doteq(\mathrm{We} t=t)$. The (unnormalized) posterior distribution $\operatorname{Pr}($ Rain, Wet $=$ $t)$ is again the product of the factors associated to the nodes of the BN (as in Thm. 5.10) but this time starting from the updated factors $\phi_{1}^{\mathrm{e}}$ and $\phi_{2}^{\mathrm{e}}$. In our case, $\phi_{1}^{\mathrm{e}}=\phi_{1}$, while $\phi_{2}^{\mathrm{e}}$ is modified as in Fig. 11. So $\operatorname{Pr}($ Rain, Wet $=\mathrm{t})=\phi_{2}^{\mathrm{e}} \odot \phi_{1}^{\mathrm{e}}$ (the result is in Fig. 11). Hence, we immediately have:
![img-9.jpeg](img-9.jpeg)

Fig. 11. Dealing with evidence

- $\operatorname{Pr}(\mathrm{We} t=t)=0.148$, which is obtained by adding up all the entries in $\operatorname{Pr}($ Rain, Wet $=\mathrm{t})$;
- $\operatorname{Pr}($ Rain $|\mathrm{We} t=t)$, which is obtained by normalizing $\operatorname{Pr}($ Rain, Wet $=\mathrm{t})$, as depicted in Fig. 11. So, for example, we have the posterior $\operatorname{Pr}(\operatorname{Rain}=\mathrm{t} \mid \mathrm{We} t=t)=0.14 / 0.148=0.946$, a huge increase from our prior belief $\operatorname{Pr}(\operatorname{Rain}=\mathrm{t}) \doteq \phi_{1}(\mathrm{t})=0.2$.


### 8.1 The Semantics of Terms, with Evidence

The main ingredients being the same, our approach is easily adapted to deal with evidence, syntactically encoded by the construct obs $(x=b)$. To express evidence, we enrich the definition of intersection types with two more sets of atomic types, namely $\left\{X^{t} \mid X \in\right.$ Names $\}$ and $\left\{X^{f} \mid X \in\right.$ Names $\}$.
![img-10.jpeg](img-10.jpeg)

Technically, we require the atomic types appearing in a type derivation to be pairwise consistent, meaning that if two atomic types $\mathcal{X}_{1}, \mathcal{X}_{2}$ have the same name $X$, then they are both either $X$ or $X^{t}$ or $X^{f}$. It is easy to check that for this property to hold for a type derivation $\pi \triangleright J$, it just suffices to require that it holds for the atomic types in the conclusion $J$.

Given a derivation $\pi$ and a name $X$, we define $\operatorname{Val}(X)=\{t\}$ if $X$ occurs in $\pi$ as $X^{t}, \operatorname{Val}(X)=\{f\}$ if $X$ occurs in $\pi$ as $X^{f}$, and $\operatorname{Val}(X)=\{t, f\}$ otherwise. Essentially, we treat an observed r.v. as unary, akin to factor reduction in [Koller and Friedman 2009].

Types and Semantics. We can now complete Fig. 7 (and Fig. 9) with the typing rule for obs $(x=b)$ :

$$
\widehat{\Lambda, x: X^{b} \vdash \operatorname{obs}(x=b): X^{b} \diamond \stackrel{\ominus}{1}}^{I-\text { OBS }}
$$

where we annotated the rule with the semantics indicated by Def. 6.2 (a remark similar to 6.3 applies). The typing rules for I-SAMPLE and I-COND in Fig. 7 (and Fig. 9) are updated as follows:

$$
\frac{X \notin \operatorname{Nm}(\Lambda)}{\Lambda \vdash \operatorname{sample}_{d}: \mathcal{X} \diamond \stackrel{(\mathrm{X})}{\phi}} \stackrel{\text { I-SAMPLE }}{\text { I-SAMPLE }} \frac{X \notin\left\{\mathrm{Y}_{1}, \ldots, \mathrm{Y}_{n}\right\} \text { and } X \notin \operatorname{Nm}(\Lambda)}{\Lambda, y_{1}: \mathcal{Y}_{1}, \ldots, y_{n}: \mathcal{Y}_{n} \vdash \mathbf{c}_{\left(y_{1}, \ldots, y_{n}\right)}: \mathcal{X} \diamond \stackrel{\left\{\mathrm{Y}_{1}, \ldots, \mathrm{Y}_{n}, \mathrm{X}\right\}}{\phi}} \text { I-COND }
$$

where we annotate the rules with the factor $\phi$ indicated by Def. 6.1, taking into account the definition of $\operatorname{Val}(X)$ given above (see Example 8.2). Everything else stays the same: all definitions and results in Sections 6 and 7 remain valid. An example will clarify what happens, and how the evidence is reflected into the semantics, via the type derivation.

Example 8.2 (Basic). Consider a term modeling the BN of Example 8.1, i.e. Rain $\rightarrow$ Wet:

$$
\text { let rain }=\text { bernoulli }_{0.2} \text { in let wet }=\mathbf{c}_{\text {(rain) }} \text { in }\langle\text { rain, wet }\rangle: \mathrm{R} \otimes \mathrm{~W}
$$

where $\mathbf{c}_{\text {(rain) }} \hat{=}$ case rain of $\left\{t \equiv\right.$ bernoulli $\left._{0.7} ; f \equiv\right.$ bernoulli $\left._{0.01}\right\}$. To express the evidence $W=t$, we use the construct obs (wet $=\mathrm{t}$ ), yielding the (sugared) term

$$
\text { let rain }=\text { bernoulli }_{0.3} \text { in let wet }=\mathbf{c}_{\text {(rain) }} \text { in }\langle\text { rain, obs }(\text { wet }=\mathrm{t})\rangle: \mathrm{R} \otimes \mathrm{~W}^{\mathrm{t}}
$$

Let us see how the evidence is reflected into the semantics, thanks to the type derivation $\pi$.
![img-11.jpeg](img-11.jpeg)
$\pi \triangleright \vdash$ let $r=$ bern $_{0.2}$ in let $w=\mathbf{c}_{\langle r\rangle}$ in $\langle r$, obs $(w=t) \rangle: R \otimes W^{t} \diamond \phi_{1} \odot \psi$
The I-OBS axiom forces the type $\mathrm{W}^{\mathrm{t}}$. In turn, $\mathrm{W}^{\mathrm{t}}$ is propagated to the I-COND axiom, via the I-LET rule. What is the semantics of the I-COND axiom? Spelling out Def. 6.1, and recalling that here $\operatorname{Val}(W)=\{t\}$, we have that the factor $\psi$ associates a scalar to each of the two tuples in $\operatorname{Val}(R) \times \operatorname{Val}(W)$ :

$$
\psi(\mathrm{tt}) \hat{=} \text { bernoulli }_{0.7}(\mathrm{t}) \text { and } \psi(\mathrm{ft}) \hat{=} \text { bernoulli }_{0.01}(\mathrm{t})
$$

That is, $\psi$ is exactly the factor $\phi_{2}^{\mathrm{e}}$ in Fig. 11. Please observe that the difference in the interpretation is entirely due to the type $\mathrm{W}^{\mathrm{t}}$. With the same definitions as in Sect. 6 , we have $\llbracket \pi \rrbracket=\phi_{1} \odot \psi$, which is exactly $\phi_{1}^{\mathrm{e}} \odot \phi_{2}^{\mathrm{e}}=\operatorname{Pr}($ Rain, Wet $=\mathrm{t})$.

A very similar reasoning would apply to express $\operatorname{Pr}($ Rain $\mid$ Wet $=\mathrm{t})$ in a model with several variables, like the one in Fig. 1; marginalization is taken care by the semantics exactly as before. It is more interesting to revisit Example 4.10, to illustrate how we deal with evidence together with copies.

Example 8.3 (Coin Tosses). Consider again the term $u$ of Example 4.10, modeling two tosses of the same (biased) coin. Assume we want to infer (learn) the bias of the coin from the result of the tosses. For example, if we observe that both the coin tosses yield $t$, this would increase our confidence

that the coin is biased toward $t$. Indeed the semantics of the updated term changes in this sense, as we show here. The following term ${ }^{6} u^{\prime}$ expresses the evidence, given the model encoded by $u$. Notice the modularity in the encoding.

$$
u^{\prime} \triangleq \operatorname{letp}\left\langle x, y_{1}, y_{2}\right\rangle=u \text { in }\left\langle x, \operatorname{obs}\left(y_{1}=\mathrm{t}\right), \operatorname{obs}\left(y_{2}=\mathrm{t}\right)\right\rangle
$$

Once again, each observation obs $\left(y_{i}=\mathrm{t}\right)$ forces the type $\mathrm{Y}_{i}^{\mathrm{t}}$, so recording the evidence t for each $\mathrm{Y}_{i}$; the type derivation takes care of propagating the evidence, as shown below:

$$
\begin{aligned}
& y_{1}: \mathrm{Y}_{1}^{\mathrm{t}} \vdash \operatorname{obs}\left(y_{1}=\mathrm{t}\right): \mathrm{Y}_{1}^{\mathrm{t}} \quad y_{2}: \mathrm{Y}_{2}^{\mathrm{t}} \vdash \operatorname{obs}\left(y_{2}=\mathrm{t}\right): \mathrm{Y}_{2}^{\mathrm{t}} \\
& x: X \vdash x: X \quad y_{1}: \mathrm{Y}_{1}^{\mathrm{t}}, y_{2}: \mathrm{Y}_{2}^{\mathrm{t}} \vdash\left\langle\operatorname{obs}\left(y_{1}=\mathrm{t}\right), \operatorname{obs}\left(y_{2}=\mathrm{t}\right)\right\rangle: \mathrm{Y}_{1}^{\mathrm{t}} \otimes \mathrm{Y}_{2}^{\mathrm{t}} \\
& x: X, y_{1}: \mathrm{Y}_{1}^{\mathrm{t}}, y_{2}: \mathrm{Y}_{2}^{\mathrm{t}} \vdash\left\langle x, \operatorname{obs}\left(y_{1}=\mathrm{t}\right), \operatorname{obs}\left(y_{2}=\mathrm{t}\right)\right\rangle: \mathrm{X} \otimes \mathrm{Y}_{1}^{\mathrm{t}} \otimes \mathrm{Y}_{2}^{\mathrm{t}}
\end{aligned}
$$

The derivation $\pi^{\prime} \triangleright u$ (highlighted in red) is the same as the derivation $\pi \triangleright u$ of Example 4.10, but with each type $\mathrm{Y}_{i}$ replaced by $\mathrm{Y}_{i}^{\mathrm{t}}$ (as forced by the I-LETP typing rule). The semantics changes as expected, reflecting that the evidence increases our confidence that the coin is biased toward t. The reader can find the computation of the semantics developed in full in the Tech. Report.

# 9 A COST-AWARE SEMANTICS 

In this section we examine the cost of computing the semantics of a term $t$ of ground type, that is the cost of inferring the marginal distribution defined by $t$. We assume $\pi$ to be an arbitrary derivation of a judgment $J$ of shape $\Lambda \vdash t: L$. Looking at Def. 6.2 one easily realizes the following:

Proposition 9.1 (Cost Upper Bound). The cost of computing $\|\pi\|$ according to Def. 6.2 is $O\left(m_{\pi} \cdot 2^{n}\right)$, where $n=|\operatorname{Nm}(\operatorname{Cpts}(\pi))|$ is the number of names which appear in $\operatorname{Cpts}(\pi)$, and $m_{\pi} \leq n$ is the number of probabilistic axioms in $\pi$.

This is the upper bound to the cost of computing the semantics of $\pi$. But there is more to the story. Non-idempotent type systems are known to provide quantitative information about the typed term, such as bounds on the execution time. There is a rich literature on systems which capture (possibly tight) complexity bounds in different styles of computation [Accattoli et al. 2022, 2020b; de Carvalho 2018], including the expected runtime of probabilistic computations [Dal Lago et al. 2021]. However, in the setting of Bayesian modeling and exact inference, the runtime, and even the expected runtime, has little relevance, because the dominating cost (in time and space) is due to the computation of the probability distribution. Such a cost is what interests us-our type system is able to provide accurate bounds.

On the Cost of Inductively Computing $\|\pi\|$. Let us point out the differences, computationally, between the definition of $\|\pi \triangleright J\|$ according to Def. 6.2-which only considers the probabilistic axioms and the names occurring in the conclusion $J$-and the inductive definition illustrated in Fig. 9. The latter, which computes the semantics following the structure of the type derivation, allows for a more efficient computation, in general. This is because summing out step-by-step yields intermediate factors of smaller size. This indeed is exactly the way algorithms for exact inference work.

Example 9.2. Consider a Bayesian network whose DAG is a chain $\mathrm{X}_{1} \rightarrow \mathrm{X}_{2} \rightarrow \cdots \rightarrow \mathrm{X}_{n}$. The following term defines the marginal over the single variable $\mathrm{X}_{n}$.

$$
\pi \triangleright \operatorname{let} x_{1}=\operatorname{sample}_{d} \text { in let } x_{2}=\mathbf{c}^{2}\left(x_{1}\right) \text { in } \ldots \text { let } x_{n}=\mathbf{c}^{n}\left(x_{n-1}\right) \text { in } x_{n}: \mathrm{X}_{n}
$$

[^0]
[^0]:    ${ }^{6}$ As usual, we use some syntactic sugar.

- Computing $\llbracket \pi \rrbracket$ according to Def. 6.2 has cost $O\left(n \cdot 2^{n}\right)$. Indeed, we first compute the product of $n$ factors-that is the full joint distribution over $\mathrm{X}_{1}, \ldots, \mathrm{X}_{n}$-and then sum out all the variables but $\mathrm{X}_{n}$.
- Regardless of the number of variables in the chain, the cost of computing the semantics following the structure of the derivation is $O\left(n \cdot 2^{3}\right)$, as one can easily verify by trying to write down the derivation: we do not actually need to explicitly build a distribution over $n$ random variables. Clearly, there is no guarantee that the cost of inductively computing the semantics of $\pi$ is always strictly less than computing $\llbracket \pi \rrbracket$ directly.

If we examine the cost of computing the semantics of $\pi$ inductively, we obtain a better upper bound than in Prop. 9.1-please observe that the latter essentially corresponds to computing the full joint distribution underlying the model.

Proposition 9.3 (Inductive Cost). Let $\pi$ be a type derivation, $m_{\pi}$ the number of probabilistic axioms in $\pi$, and $n=|\mathrm{Nm}(\operatorname{Cpts}(\pi))|$ the number of names which appear in $\operatorname{Cpts}(\pi)$ (as in Prop. 9.1). The cost of inductively computing the semantics of $\pi$ following the structure of the derivation is

$$
O\left(m_{\pi} \cdot 2^{W}\right)
$$

where $W \leq n$ is the maximal cardinality of any set of names $\mathbb{Y}$ appearing in the derivation, when decorated as in Fig. 9.

Remark 9.4. The reader familiar with inference algorithms will realize that inductively computing the semantics following the structure of the derivation implements inference by a form of the Variable Elimination algorithm, and indeed such an observation can be made formal. The needed technical details, however, are beyond the scope of this paper.

Remark 9.5 (Observed Variables). Both bounds-in Prop. 9.1 and Prop. 9.3- can be made tighter by restricting $n$ to the set $\widehat{\mathbb{Y}}$ of non observed names. The set $\mathbb{E}$ of observed variables does not actually contribute to the number of entries in a factor, since each one has a single possible value. So $\operatorname{Val}(\widehat{\mathbb{Y}}) \times \operatorname{Val}(\mathbb{E})$ is isomorphic to $\operatorname{Val}(\widehat{\mathbb{Y}})$.

Exact Bounds. Given that the type system is resource-sensitive by design, it is not difficult to refine type derivations by decorating $\pi$ with the number of elementary steps needed to compute its semantics. We stress that this information can be retrieved without performing calculations on factors-it is enough to keep track of the relevant names occurring in each judgment. It is straightforward to fine-tune the complexity measure and provide bounds with different granularity.

In Fig. 12 we give a minimalist example, limited to the decidable first-order system, where the weight on the turnstile counts the number of multiplications performed during the computation (the cost of sums being negligible w.r.t. the cost of products). Here, given a judgment $J \diamond \mathbb{X}$, we write $\widehat{\mathbb{X}}$ for the restriction of $\mathbb{X}$ to the names that are not observed in $J$ : this is to take into account that observed names do not actually contribute to the factor size, hence to the overall cost, as remarked above.

Same Model, Different Cost. Since the cost of computing the semantics (i.e. the cost of exact inference) depends on the structure of the term itself, different terms describing the very same marginal distribution may have different costs. Indeed, a term encodes not only a Bayesian network and a marginal, but also a way to compute it, in agreement with the ideas which underlay exact inference on terms, as proposed by Koller and Pfeffer [1997]. Our type system detects such a difference. The following example illustrates this point.

Example 9.6 (Same BN, Different Cost). Consider the following two terms, both in normal form, and both corresponding to the same Bayesian network whose graph is the chain $X \rightarrow Y \rightarrow Z$.

1. $t_{1} \triangleq \operatorname{let} x=\operatorname{sample}_{d}$ in let $y=\mathbf{c}^{t}(x)$ in let $z=\mathbf{c}^{z}(y)$ in $z: Z$

![img-12.jpeg](img-12.jpeg)

Fig. 12. First-order type system annotated with the cost of computing the factor.
2. $t_{2} \triangleq \operatorname{let} z=\left(\right.$ let $y=\left(\right.$ let $x=\operatorname{sample}_{d}$ in $\left.\mathbf{c}^{\mathrm{Y}}\langle x\rangle\right)$ in $\mathbf{c}^{\mathrm{Z}}\langle y\rangle$ ) in $z: \mathrm{Z}$

Both terms define the same marginal distribution over Z. However, inductively computing such a distribution has a different cost $^{7}: 12$ multiplications for $t_{1}$, and 8 for $t_{2}$.

Cost and Reduction. The upper bound in Prop. 9.1 is invariant by reduction, because the number of probabilistic axioms in a type derivation is invariant. On the other hand, the cost of inductively computing the semantics of a type derivation $\pi$ (Prop. 9.3) is not stable by reduction, because the structure of the derivation changes, and so the size $W$ of the largest factor to be inductively computed may grow or shrink. This is indeed the rationale behind the program transformations which correspond to the Variable Elimination algorithm performed on terms [Ehrhard et al. 2023b]. Starting from a normal form, the efficiency may be improved via expansion (the reverse of reduction).

Cost of Factors Product vs. Matrices Product. We stress how much the product of factors differs from the product of matrices. In this difference lies the efficiency of a factors-based semantics w.r.t. to a categorical [Jacobs and Zanasi 2020] or relational [Ehrhard et al. 2014; Ehrhard and Tasson 2019] one, where a central role is played by a product $\otimes$ which behaves as the tensor product of matrices.

Example 9.7. Let $t_{1}, t_{2}$ be case expressions, respectively encoding two CPTs $\phi^{\mathrm{X}_{1}}=\operatorname{Pr}\left(\mathrm{X}_{1} \mid \mathrm{Y}_{1}, \mathrm{Y}_{2}, \mathrm{Y}_{3}\right)$ and $\phi^{\mathrm{X}_{2}}=\operatorname{Pr}\left(\mathrm{X}_{2} \mid \mathrm{Y}_{1}, \mathrm{Y}_{2}, \mathrm{Y}_{3}\right)$, where two distinct r.v.s ( $\mathrm{X}_{1}$ and $\mathrm{X}_{2}$, respectively) are conditioned to the same set of r.v.s $\mathrm{Y}_{1}, \mathrm{Y}_{2}, \mathrm{Y}_{3}$. We can see each $\phi^{\mathrm{X}_{i}}$ interpreting $t_{i}$ as a stochastic matrix (of size $2^{4}$ ). One easily realizes that computing the tensor product $\phi^{\mathrm{X}_{1}} \otimes \phi^{\mathrm{X}_{2}}$ of the two matrices, requires to compute and store $2^{4} \cdot 2^{4}=2^{8}$ entries. In contrast, the factor product $\phi^{\mathrm{X}_{1}} \odot \phi^{\mathrm{X}_{2}}$ computes $2^{5}$ entries. Indeed, in a categorical or relational model, to compute the semantics of the term $\left\langle t_{1}, t_{2}\right\rangle$ will (in general) pass via $\phi^{\mathrm{X}_{1}} \otimes \phi^{\mathrm{X}_{2}}$. On this basis, it is easy to build a term which encodes a BN over the 5 variables $\mathrm{X}_{1}, \mathrm{X}_{2}, \mathrm{Y}_{1}, \mathrm{Y}_{2}, \mathrm{Y}_{3}$, and whose inductive interpretation (in a categorical or relational model) requires to compute and store $2^{8}$ values-one such a term is given in the Tech. Report. This is somehow weirdfrom the point of view of BNs-given that the full joint distribution over 5 variables has size $2^{5}$.

# 10 LIFTING THE TYPE SYSTEM TO CALL-BY-PUSH-VALUE PCF 

To streamline the presentation, we carried out our analysis in the setting of the untyped $\lambda$-calculus, on top of which we have defined an intersection type system. As mentioned in Sect. 4.2, all our methods can be lifted to a more user friendly PCF-like sintax, similar to that in [Ehrhard and Tasson 2019].

[^0]
[^0]:    ${ }^{7}$ The reader can find the explicit computations in the Tech. Report.

![img-13.jpeg](img-13.jpeg)

Fig. 13. The type system for call-by-push-value PCF (selected rules).
Terms of a call-by-push-value PCF are those of the $\lambda$-calculus in Sect. 3 plus some operations needed to handle natural numbers (including a constant $\underline{n}$ for each number $n$ ) and a fixed point combinator:

$$
\begin{array}{cc}
\text { Terms } t, u & ::= \\
\text { Values } v, \mathrm{w} & ::= \\
\hline
\end{array} \quad \begin{aligned}
& \text { ... } \mid \text { succ } v \mid \text { pred } v \mid \text { ifZerov } t u \mid \text { fix } x . t \\
& \text { n } \underline{n} \text {. }
$$

The reduction rules are as expected. As standard, PCF types (represented in red) are the simple types of Sect. 3 extended with the ground type of natural numbers:

$$
\text { Ground Types } L, K \quad::=\ldots \mid \mathrm{N}
$$

The fact that PCF is a typed calculus does not mean that we can get rid of intersection types (here represented in blue) to give semantics to the terms. Indeed, we still need to keep track of the names which are generated during the computation. As usual with PCF, ground intersection types need to be extended with a type constant $\bar{n}$ for each natural number $n$ :

$$
\text { Ground Intersection Types } L, K \quad::=\ldots \mid \bar{n}
$$

At this point we need to type PCF terms. A PCF term will come with two types: a standard type, and an intersection type, as in [Dal Lago and Gaboardi 2011; Ehrhard 2016; Ehrhard et al. 2014]. For example, the term sample $_{d}$ is typed as $\vdash$ sample $_{d}: \mathrm{B}: \mathrm{X}$. The idea is that in a judgment $\vdash t: A: C$, the intersection type $C$ refines the standard PCF type $A$. In the example, X refines B , being X the name of a boolean variable. In Figure 13, we report a selection of the typing rules for this language. One can notice that the rules P-SAMPLE, P-COND, and P-LET are obtained by overlapping the ones for simple types with the ones for intersection types. The typing rules which are specific to PCF constructs are standard, and have been adapted from [Ehrhard 2016].

# 11 RELATED WORK 

Theoretical research on functional PPLs, pioneered by [Saheb-Djahromi 1978] is a very active area. Early investigation [Friedman et al. 1998; Koller et al. 1997; Park 2003; Park et al. 2005; Pless and Luger 2001; Ramsey and Pfeffer 2002] has evolved in a large body of work, to support the growing development of software. Landmark foundational work aiming at providing sound and compositional methods for higher-order Bayesian inference includes [Borgström et al. 2015] and [Ścibior et al. 2018]. The former is based on operational techniques, while the latter on a modular denotational semantics. Our work is inspired by both. The importance of capturing the data flow of higher-order probabilistic programs, is stressed in [Castellan and Paquet 2019; Paquet 2021], which rely on event structures. Relevantly, Bayesian networks are at the core of Paquet [2021] game semantics proposal, motivated by the fact that-in practice-most modern inference engines do not manipulate directly

the program syntax but rather some graph representation of it. We share this view, and the goal of providing reasoning tools for such implementations. We also mention [Gorinova et al. 2022], which introduces an information flow type system, in a first-order, imperative setting. As already recalled in the introduction, the theory of Bayesian networks has been investigated extensively from a categorical viewpoint by Jacobs and Zanasi [Jacobs 2023; Jacobs et al. 2019; Jacobs and Zanasi 2016, 2020].

The foundational studies based on Bayesian networks which we have cited above focus on expressiveness and compositionality. However, they do not take into account space and time consumption of probabilistic reasoning, which is the very motivation for the introduction [Pearl 1986] and development of BNs. As a matter of fact, the cost of actually computing the semantics explodes when taking a categorical [Jacobs and Zanasi 2020] or relational [Ehrhard et al. 2014; Ehrhard and Tasson 2019] approach, because of the product $\otimes$, which behaves as the tensor product of matrices (see Example 9.7); inductively computing the semantics of $n$ binary r.v.s easily leads to intermediate computations whose size is much larger than $2^{n}$ (the size of the full joint distribution). This fact has already been pointed out in a recent paper by Ehrhard et al. [2023a], which advocates the need for a new approach to quantitative semantics, more attentive to the resource consumption. That paper imports factors techniques into the setting of multiplicative linear logic, essentially a linear $\lambda$-calculus with tuples (roughly, our first-order fragment)-the authors leave as an open challenge the treatment of linear logic exponentials (roughly, the calculus of Fig. 6). Our framework, indeed, is able to deal with a fully-fledged $\lambda$-calculus, thanks to the intersection type system and the flow-graph techniques built on top of it. Actually, our factor-based semantics can be seen as an optimized version of semantics based on the weighted relational model, such as [Laird et al. 2013] and Probabilistic Coherence Space [Danos and Ehrhard 2011; Danos and Harmer 2002; Ehrhard et al. 2014; Ehrhard and Tasson 2019]. Finally, we mention that Chiang et al. [2023] also use techniques inspired from linear logic to provide a denotational semantics and exact inference procedures to recursive probabilistic programs.

The idea that programming languages provide a way to overcome the limitations of standard Bayesian networks has been actively propounded by Koller and Pfeffer [1997]; Pfeffer and Koller [2000], which introduced a modeling framework based on Object-Oriented programming. This approach has eventually led to the object-oriented language Figaro [Pfeffer 2016].

# 12 CONCLUSIONS 

We have presented a higher-order probabilistic programming language which allows for the specification of recursive probability models and hierarchical structures. Higher-order programs are compiled into standard Bayesian networks operationally, via rewriting, and denotationally, via an intersection type system. The novelty of our contribution is that (1) the compositional semantics is based on factors, the very mathematical notion which is used to give semantics to Bayesian networks, and which is the basis of exact inference algorithms, and (2) our semantics and type system are resource-sensitive. The notion of resource appears here in two forms: (1) we precisely track generation and sharing of random variables, and (2) we account for the actual cost of inference-the cost of computing the semantics of a typed term. We obtain these quantitative results relying on advanced semantic techniques rooted into linear logic, intersection types, rewriting theory, and Girard's geometry of interaction, which are here combined in a novel way.

The fact that our semantics is factor-based implies that standard algorithms for exact inference (which are acting on factors) can be applied. A further natural direction is to investigate inference techniques based on term transformations, in the spirit of [Ehrhard et al. 2023b; Koller et al. 1997].

## ACKNOWLEDGMENTS

The authors are in debt with Thomas Ehrhard and Michele Pagani for many insightful discussions. We thank Ugo Dal Lago, Beniamino Accattoli, Delia Kesner for their useful remarks. We are also

grateful to the anonymous referees, whose valuable comments have improved the presentation of this work. This research was supported by the ANR project PPS: ANR-19-CE48-0014. The third author is also supported by the European Union's Horizon 2020 research and innovation programme under the Marie Sklodowska-Curie grant agreement No 101034255.

# DATA AVAILABILITY STATEMENT 

Missing proofs and more examples are available in the Technical Report [Faggian et al. 2023]. Please notice that while in the paper we postpone to Sect. 8 the treatment of types and semantics for the observe construct, the proofs in the Tech. Report directly integrate it.
