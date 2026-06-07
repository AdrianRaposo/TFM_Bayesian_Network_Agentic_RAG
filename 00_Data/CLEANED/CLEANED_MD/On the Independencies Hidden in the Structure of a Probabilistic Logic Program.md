# On the Independencies Hidden in the Structure of a Probabilistic Logic Program 

Kilian Rückschloß<br>Ludwig-Maximilians-Universität München<br>Oettingenstraße 67, 80538 München, Germany<br>kilian.rueckschloss@lmu.de

## Felix Weitkämper

Ludwig-Maximilians-Universität München
Oettingenstraße 67, 80538 München, Germany
felix.weitkaemper@lmu.de

Pearl and Verma developed d-separation as a widely used graphical criterion to reason about the conditional independencies that are implied by the causal structure of a Bayesian network. As acyclic ground probabilistic logic programs correspond to Bayesian networks on their dependency graph, we can compute conditional independencies from d-separation in the latter.

In the present paper, we generalize the reasoning above to the non-ground case. First, we abstract the notion of a probabilistic logic program away from external databases and probabilities to obtain so-called program structures. We then present a correct meta-interpreter that decides whether a certain conditional independence statement is implied by a program structure on a given external database. Finally, we give a fragment of program structures for which we obtain a completeness statement of our conditional independence oracle. We close with an experimental evaluation of our approach revealing that our meta-interpreter performs significantly faster than checking the definition of independence using exact inference in ProbLog 2.

## 1 Introduction

A probabilistic logic program is a logic program, in which each clause holds with a specified probability. The most common semantics for these programs is the distribution semantics [13], which assigns to each ground program a joint probability distribution over the atoms occurring in it. It is the basis for many programming languages such as the Independent Choice Logic [9], PRISM [14], Logic Programs with Annotated Disjunctions [15] and ProbLog [1].

Since conditional independence is a rather fundamental notion in probability theory, it is natural to ask for its counterpart in probabilistic logic programming. Moreover, considering the work of Holtzen et al. [4], such an analysis may contribute to speed up lifted inference. In this paper, we extend the effort of Rückschloß and Weitkämper [11] to establish a calculus deriving the conditional independencies that are determined by the clause structure of a ProbLog program. Let us illustrate this problem in the following example:

Example 1. We consider storages, which consist of rooms, tanks, employees and liquids that are given by the unary predicates room/1, tank/1, employee/1, liquid/1, respectively. For each storage a database table passage $\left(R, R^{\prime}\right)$ tells us, between which rooms $R$ and $R^{\prime}$ we find a passage. Moreover, in each room $R$ we find tanks $T$, denoted by in $(T, R)$ and a tank $T$ may store a liquid $L$, denoted by stores $(T, L)$. Finally, we assume a database table flammable $(L)$, indicating the flammable liquids. In this context, it makes sense to assume that each tank stores at most one liquid which results in the following integrity constraint:

$$
\perp \leftarrow \operatorname{tank}(T), \operatorname{liquid}\left(L_{1}\right), \operatorname{liquid}\left(L_{2}\right), L_{1} \neq L_{2}, \text { stores }\left(T, L_{1}\right), \text { stores }\left(T, L_{2}\right)
$$

[^0]
[^0]:    S. Costantini, E. Pontelli, A. Russo, F. Toni,
    R. Calegari, A. D’Avila Garcez, C. Dodaro, F. Fabiano,
    S. GaggI, A. Mileo, (Eds.): ICLP 2023

    © K. Rückschloß, F. Weitkämper This work is licensed under the Creative Commons Attribution License.

With a certain probability _ we find an employee E opening a tank $T$, denoted by opens $(E, T)$. This leads to the following ProbLog clause:

$$
\lrcorner:: \text { opens }(E, T) \leftarrow \text { employee }(E), \text { tank }(T)
$$

Further, if employee $E$ opens tank $T$, it may be that $E$ does not close the tank $T$ properly, which then causes the tank $T$ to leak, denoted by leaks $(T)$. Again we assume that we don't know the exact probabilities and capture the mechanism in the following clause:

$$
\lrcorner:: \operatorname{leaks}(T) \leftarrow \text { employee }(E), \text { tank }(T), \text { opens }(E, T)
$$

Moreover, an employee $E$ may smoke in a room $R$, denoted by smokes $(E, R)$ :

$$
\lrcorner:: \operatorname{smokes}(E, R) \leftarrow \text { employee }(E), \operatorname{room}(R)
$$

If employee $E$ smokes in a room $R$, which contains a leaking tank storing an flammable liquid, this may cause a fire in room $R$. Further, the smoke immediately spreads to the rooms $R_{1}$, which are connected to the room $R$ by passages, where it may trigger a sensor. In this case, we observe the event fire $\left(R_{1}\right)$. This mechanism is captured in the clauses below:

$$
\begin{aligned}
& \text { connected }(R, R) \leftarrow \operatorname{room}(R) \\
& \text { connected }\left(R, R_{1}\right) \leftarrow \operatorname{room}(R), \operatorname{room}\left(R_{1}\right), \operatorname{room}\left(R_{2}\right), \text { passage }\left(R_{2}, R_{1}\right) \\
& \quad \text { connected }\left(R, R_{2}\right) \\
& \lrcorner:: \operatorname{fire}\left(R_{1}\right) \leftarrow \operatorname{room}\left(R_{1}\right), \operatorname{room}(R), \text { employee }(E), \text { tank }(T), \operatorname{liquid}(L), \operatorname{in}(T, R) \\
& \quad\left(\text { connected }\left(R, R_{1}\right) ; \text { connected }\left(R_{1}, R\right)\right), \text { stores }(T, L), \text { flammable }(L) \\
& \quad \text { smokes }(E, R), \text { leaks }(T)
\end{aligned}
$$

Given (RC1), (RC2), (RC3), (RC4), (Const) and (Int) together with a concrete storage, we aim to answer queries about conditional independencies. For instance, we want to determine whether the event smokes $(e 1, r)$ of employee e1 smoking in room $r$ is independent of the event opens $(e 2, t)$ of employee e2 opening the tank $t$ without knowing the probabilities of the clauses (RC1), (RC2), (RC3) and (RC4). Further, we would also like to predict how things change if we observe fire $\left(r_{1}\right)$ a fire in room $r_{1}$.

We accomplish our goal by grounding ProbLog programs to Bayesian networks, where we can apply the theory of d-separation [16] to derive the desired independence statements. In this way we can efficiently reason about conditional independencies. Further, we highlight that the theory of d-separation lies at the basis of constraint based causal structure discovery, i.e. it enables us to reason about causal relationships on the basis of observational data. Hence, we suppose that the present work also serves as a starting point in the development of causal structure discovery techniques for probabilistic logic programming.

# 2 On the Independencies Hidden in a Propositional Causal Structure 

At the beginning, we discuss how conditional independencies can be inferred from a causal structure in the propositional case. Here, we identify a causal structure on a set of random variables $\mathbf{V}$ with a directed acyclic graph $G$, i.e. a partial order, on $\mathbf{V}$. The intuition is that $X$ is a cause of $Y$ if there is a directed path from $X$ to $Y$ in $G$. In this case, we also say that $Y$ is an effect of $X$. Further, we say that $X$ is a direct cause of $Y$ if the edge $X \rightarrow Y$ exists in $G$, i.e. if and only if the node $X \in \mathrm{~Pa}(Y)$ lies in the set $\mathrm{Pa}(Y)$ of parents of $Y$.

Example 2. Consider a road that passes by a field with a sprinkler in it. The sprinkler is switched on by a weather sensor and the pavement of the road may be wet, denoted by wet, because the sprinkler is on, denoted sprinkler or because it rains, denoted by rain. Further, we know that the events rain and sprinkler are caused by the season, denoted by season, as they both are triggered by the weather. Finally, we note that a wet road is more likely to be slippery, denoted by slippery. The situation above gives rise to the following causal structure on the random variables $\boldsymbol{V}:=\{$ season, rain, sprinkler, wet, slippery $\}$ :
![img-0.jpeg](img-0.jpeg)

In particular, we find that season is a cause of slippery but not a direct cause, whereas wet is a direct cause of slippery. Further, there is no causal relationship between sprinkler and rain.

Next, a given probability distribution $\pi$ on the random variables $\mathbf{V}$ is consistent with a causal structure $G$ if the influence of any cause $X$ on an effect $Y$ is moderated by the direct causes of $Y$. This intuition is formally captured in the following definition:
Definition 1 (Markov Condition). We say that the distribution $\pi$ on the set of random variables $\boldsymbol{V}$ satisfies the Markov condition with respect to a causal structure $G$ on $\boldsymbol{V}$, if every random variable $X \in \boldsymbol{V}$ is independent of its causes in $G$, once we observe its direct causes $\mathrm{Pa}(X)$. In this case, we write $\pi \models G$.
Example 3. In Example 2 the Markov condition states for instance that the influence of season on the event slippery is completely moderated by the event wet. Once we know that the pavement of the road is wet, we expect it to be slippery regardless of the event that caused the road to be wet.

If a distribution $\pi \models G$ satisfies the Markov condition with respect to a given causal structure $G$, it is represented by a Bayesian network on $G$ and vice versa [8, §1.2.3]:
Definition 2 (Bayesian Network). A Bayesian network on a set of random variables $\boldsymbol{V}$ consists of a causal structure $G$ on $\boldsymbol{V}$ and the probability distributions $\pi(X \mid \operatorname{Pa}(X))$ of the random variables $X \in \boldsymbol{V}$ conditioned on their direct causes in G. A Bayesian network gives rise to a joint probability distribution on $\boldsymbol{V}=\left\{X_{1}, \ldots, X_{k}\right\}$ by setting

$$
\pi\left(X_{1}=x_{1}, \ldots, X_{k}=x_{k}\right):=\prod_{i=1}^{k} \pi\left(X_{i}=x_{i} \mid \mathrm{pa}\left(X_{i}\right)\right)
$$

where $\operatorname{pa}\left(X_{i}\right):=\left\{X_{j}=x_{j} \mid X_{j} \in \operatorname{Pa}\left(X_{i}\right)\right\}$.
The Markov condition equips a causal structure with a semantics that is given by conditional independence statements. Further, Verma and Pearl [16] derive d-separation as a criterion to compute all conditional independencies that follow if we apply the Markov condition to a given causal structure.
Definition 3 (d-Separation). Let G be a directed acyclic graph, i.e. it is a causal structure. An undirected path $P$ between two nodes $A$ and $B$ is an alternating sequence of nodes and edges

$$
P=R_{0} \stackrel{E_{1}}{-} R_{1} \stackrel{E_{2}}{-} R_{2} \stackrel{E_{3}}{-} \ldots \stackrel{E_{n-1}}{-} R_{n-1} \stackrel{E_{n}}{-} R_{n}
$$

where $E_{i} \in\left\{R_{i-1} \rightarrow R_{i}, R_{i-1} \leftarrow R_{i}\right\}$ for all $1 \leq i \leq n$. We call a node $R_{i}$ of $P$ a collider if $P$ is of the form $\ldots \rightarrow R_{i} \leftarrow \ldots$, otherwise $R_{i}$ is said to be a non-collider of $P$.

Further, let $\boldsymbol{Z}$ be a set of nodes. We say that a node $N$ is blocked by $\boldsymbol{Z}$ if it lies in $\boldsymbol{Z}$, i.e. if we have that $N \in \boldsymbol{Z}$. Moreover, $N$ is said to be activated by $\boldsymbol{Z}$ if there exists a directed path from $N$ to a node in $\boldsymbol{Z}$. The undirected path $P$ is a d-connecting path with respect to the observations $\boldsymbol{Z}$ if every non-collider $N$ of $P$ is not blocked and if every collider $C$ of $P$ is activated.

We say that $\boldsymbol{Z}$ d-connects two nodes $A$ and $B$ if there exists a d-connecting path between $A$ and $B$ with respect to $\boldsymbol{Z}$. Otherwise, we say that $\boldsymbol{Z}$ d-separates $A$ and $B$. Finally, two sets of nodes $\boldsymbol{A}$ and $\boldsymbol{B}$ are said to be d-separated by $\boldsymbol{Z}$ if $\boldsymbol{Z}$ d-separates $A$ and $B$ for every $A \in \boldsymbol{A}$ and every $B \in \boldsymbol{B}$. Otherwise, the sets $\boldsymbol{A}$ and $\boldsymbol{B}$ are d-connected by $\boldsymbol{Z}$.

Note that the term "d-connected" is a shorthand for "directionally connected" [3].
Example 4. Let us consider the causal structure (1) again and take $\boldsymbol{Z}:=\{$ slippery $\}$ for the observations. We find the following d-connecting path $P:=$ season $\rightarrow$ rain $\rightarrow$ wet $\leftarrow$ sprinkler. The intuition behind this d-connecting path is as follows:

Assume we observe the event $\boldsymbol{Z}$. We know that this increases the probability for wet, which itself is triggered by rain or sprinkler. If we additionally suppose that it is summer, this decreases the probability for rain, which increases the probability of sprinkler as we have an increased probability for wet. To summarize we expect season and sprinkler to be dependent once we observed slippery.

Note that the argument above does not go through anymore, if we observe additionally that it rains or if we observe nothing.

The reasoning of Example 4 is now formalized in the following theorem.
Theorem 1 (Verma and Pearl [16]). Let $G$ be a causal structure on the set $\boldsymbol{V}$, let $\boldsymbol{Z}:=\left\{Z_{1}, \ldots, Z_{n}\right\} \subseteq \boldsymbol{V}$ be a subset of nodes and let $A, B \in \boldsymbol{V}$ be nodes of $G$. If $\boldsymbol{Z}$ d-separates $A$ and $B$, we obtain that $A$ and $B$ are independent conditioned on $\boldsymbol{Z}$ in every distribution $\pi \models G$, which is Markov to $G$. Here, being conditionally independent means that

$$
\begin{aligned}
& \forall_{a \text { value of } A} \forall_{b \text { value of } B} \forall_{z_{1}, \ldots, z_{n} \text { values of } Z_{1}, \ldots, Z_{n}}: \\
& \pi\left(A=a, B=b \mid\left\{Z_{i}=z_{i}\right\}_{i=1}^{n}\right)=\pi\left(A=a \mid\left\{Z_{i}=z_{i}\right\}_{i=1}^{n}\right) \cdot \pi\left(B=b \mid\left\{Z_{i}=z_{i}\right\}_{i=1}^{n}\right) .
\end{aligned}
$$

However, McDermott [5] demonstrates that in general d-separation does not yield a complete independence oracle. This observation motivates the following definition.
Definition 4 (Faithfulness). A distribution $\pi$ is (causally) faithful to a causal structure $G$ on $\boldsymbol{V}$ if it is Markov to $G$ and if every conditional independence of two random variables $A, B \in \boldsymbol{V}$ with respect to a set of observations $\boldsymbol{Z} \subseteq \boldsymbol{V}$ can be derived from d-separation by Theorem 1.

Fortunately, Meek [6] shows that faithfulness holds for almost all Boolean Bayesian networks in the following sense:
Theorem 2. Let $G$ be a causal structure and let $\theta \in[0,1]^{n}$ be the vector, which determines the conditional distributions that turn $G$ into a Boolean Bayesian network representing the distribution $\pi$. In this case we obtain finitely many non-trivial polynomial equations such that $\pi$ is faithful to $G$ unless $\theta$ solves one of these equations.

Note that Theorem 2 states that d-separation enables us to derive all conditional independence statements that are implied by a causal structure under the Markov condition.

Finally, we identify a causal structure $G$ with the database that contains a fact $X$---> Y for every edge $X \rightarrow Y$ in $G$. In this case the predicate dseparates $/ 3$ in following meta-interpreter decides whether two nodes $X$ and $Y$ are d-separated by a list of observations $\mathbf{Z}$.

Program 1 (Deciding d-Separation).
\% Implement hactivates/2 as the transitive closure of (--->)/2 and
\% calculate activated nodes
hactivates $(X, X) . \quad$ hactivates $(Z, X):-(Y--->Z)$, hactivates $(Y, X)$.
activates $([Z / \ldots], X):-hactivates(Z, X) . \quad$ activates $([\ldots / T Z], X):-a c t i v a t e s(T Z, X)$.
\% Implement dconnects/3 by case distinction over the last orientation
dconnects $(X, Y, Z):-\mid+$ member $(X, Z), \quad \mid+$ member $(Y, Z)$, dconnects $(X, Y, Z, \ldots)$.
dconnects $(X, Y, \ldots$ right $):-(X--->Y) . \quad$ dconnects $(X, Y, \ldots$ left $):-(Y--->X)$.
dconnects $(X, Y, Z$, right $):-(Y 1--->Y), \mid+$ member $(Y 1, Z)$, dconnects $(X, Y 1, Z$, right $)$.
dconnects $(X, Y, Z$, right $):-(Y 1--->Y), \mid+$ member $(Y 1, Z)$, dconnects $(X, Y 1, Z$, left $)$.
dconnects $(X, Y, Z$, left $):-(Y--->Y 1), \mid+$ member $(Y 1, Z)$, dconnects $(X, Y 1, Z$, left $)$.
dconnects $(X, Y, Z$, left $):-(Y--->Y 1)$, activates $(Z, Y 1)$, dconnects $(X, Y 1, Z$, right $)$.
\% dseparates/3 is the complement of dconnects/3
dseparates $(X, Y, Z):-\mid+d c o n n e c t s(X, Y, Z)$.

# 3 A Formalism for Lifted Probabilistic Logic Programming 

Recall that events of the trivial probabilities zero and one are independent of every other event. To overcome this obstruction, we introduce a language which separates logical predicates, denoting logical statements with probabilities zero and one, from random predicates, denoting events with a probability lying between zero and one.

Let us fix a query language i.e. a language $\mathfrak{Q} \supseteq \mathfrak{L} \supseteq \mathfrak{E}$ in three parts with an external vocabulary $\mathfrak{E}$ and a logical vocabulary $\mathfrak{L}$. Here, $\mathfrak{Q}$ is a finite relational vocabulary with equality $\doteq$, i.e. it consists of a finite set of relation symbols, a finite set of constants as well as a countably infinite set of variables. Further, $\mathfrak{L}$ is a subvocabulary of $\mathfrak{Q}$ containing all of the variables and constants of $\mathfrak{Q}$ as well as a (possibly empty) subset of the relation symbols of $\mathfrak{Q}$. Moreover, $\mathfrak{E}$ is a subvocabulary of $\mathfrak{L}$, which satisfies the same properties in $\mathfrak{L}$ as $\mathfrak{L}$ does regarding $\mathfrak{Q}$.
Example 5. In Example 1 the vocabulary $\mathfrak{E}$ consists of the predicates room/1, employee/1, tank/1, liquid/1, passage/2, in/2, stores/2 and flammable/1, which we assume to be given by a database. Further, $\mathfrak{L}$ extends $\mathfrak{E}$ by the predicate connected/2, which is deterministically defined in terms of the predicates of $\mathfrak{E}$. Finally, $\mathfrak{Q}$ extends $\mathfrak{L}$ by the predicates opens/2, leaks/1, smokes/2 and fire/1, which we expect to denote non-deterministic random variables.

As usual, an atom is an expression of the form $r\left(t_{1}, \ldots, t_{n}\right)$ or $t_{1} \doteq t_{2}$, where $r$ is a relation symbol and $t_{1}$ to $t_{n}$ are constants or variables, and a literal is an expression of the form $A$ or $\neg A$ for an atom $A$. It is called an external atom or literal if $r$ is in $\mathfrak{E}$, a logical atom or literal if $r$ is in $\mathfrak{L}$, an internal atom or literal if $r$ is in $\mathfrak{L} \backslash \mathfrak{E}$ and a random atom or literal if $r$ is in $\mathfrak{Q} \backslash \mathfrak{L}$. Here, we regard equality $\doteq$ as a relation in $\mathfrak{E}$. A literal of the form $A$ is called positive and a literal of the form $\neg A$ is called negative. A literal $L$ is said to be ground if no variable occurs in it. Finally, we use $\operatorname{var}(E)$ to refer to the variables occurring in a given expression $E$.
Example 6. In Example 5 passage $\left(R, R^{\prime}\right)$ is an external atom, whereas connected $\left(R, R^{\prime}\right)$ is an internal atom and fire $(R)$ is a random atom.

Formulas, as well as existential and universal formulas are defined as usual in first-order logic. The logical vocabulary will be used to formulate constraints and conditions for our probabilistic logic program. The purpose of a probabilistic logic program, however, is to define distributions for the random variables determined by the language $\mathfrak{Q}$. This is done by so-called ProbLog clauses.

Definition 5 (ProbLog Clause). A generalized ProbLog clause $R C$ is an expression of the form

$$
\left(\_:: R \leftarrow R_{1}, \ldots, R_{m}, L_{1}, \ldots, L_{n}.\right)=\left(\_:: \operatorname{effect}(R C) \leftarrow \operatorname{causes}(R C) \cup \operatorname{cond}(R C)\right)
$$

which is given by the following data:
i) a random atom $R:=\operatorname{effect}(R C)$, called the effect of $R C$
ii) a finite and possibly empty set of random literals $\operatorname{causes}(R C):=\left\{R_{1}, \ldots, R_{m}\right\}$, called the causes of $R C$
iii) a finite and possibly empty set of logical literals $\operatorname{cond}(R C):=\left\{L_{1}, \ldots, L_{n}\right\}$, called the condition of $R C$

We call $R C$ positive if the set of causes $\operatorname{causes}(R C)$ contains only positive literals. Further, we obtain a ProbLog clause $R C^{\pi(R C)}:=\left(\pi(R C):: R \leftarrow R_{1}, \ldots, R_{m}, L_{1}, \ldots, L_{n}.\right)$ from the generalized ProbLog clause $R C$ by choosing a probability $\pi(R C) \in[0,1]$.

In i) and ii) of Definition 5 we use the terminology of cause and effect to reflect that under our semantics, a ground program represents a functional causal model [8, §1.4].

Example 7. Note that (RC4) of Example 1 yields a generalized ProbLog clause. Further, if we choose the probability $\pi(R C 4):=0.6$ we obtain the ProbLog clause $R C 4^{0.6}$ below.

$$
\begin{aligned}
& 0.6:: \operatorname{fire}(R 1) \leftarrow \operatorname{room}(R 1), \text { room }(R), \text { employee }(E), \text { tank }(T), \text { liquid }(L), \text { in }(T, R) \\
& (\text { connected }(R, R 1) ; \text { connected }(R 1, R)), \text { stores }(T, L), \text { flammable }(L) \\
& \quad \text { smokes }(E, R), \text { leaks }(T)
\end{aligned}
$$

After having established the necessary syntax we proceed to the semantics. Let us begin with the logical expressions. The semantics of logical expressions is given in a straightforward way.

We highlight the unique names assumption in our definition of a structure:
An $\mathfrak{L}$-structure $\Lambda$ consists of a domain $\Delta$, an element of $\Delta$ for every constant in $\mathfrak{L}$, such that two different constants are mapped to different elements, and an $n$-ary relation on $\Delta$ for every relation symbol of arity $n$ in $\mathfrak{L}$.

Whether a logical formula is satisfied by a given $\mathfrak{L}$-structure (under a given interpretation of its free variables) is determined by the usual rules of first-order logic. Finally, note that the semantics of external expressions is defined analogously.

For the semantics of clauses and programs we choose the FCM-semantics [12] since it directly relates an acyclic ground program to a Bayesian network. We start with the definition of a lifted program:

Definition 6 (Lifted Program and Program Structure). A program structure $\boldsymbol{P}:=(\boldsymbol{R}, \boldsymbol{I}, \boldsymbol{C})$ is a triple, which consists of the following data
i) a finite set of integrity constraints $\boldsymbol{C}(\boldsymbol{P}):=\boldsymbol{C}$ of the form $\left(\perp \leftarrow L_{1}, \ldots, L_{k}.\right)$ for logical literals $L_{i}$ with $1 \leq i \leq k$, which we call the constraints of $\boldsymbol{P}$.
ii) a finite set of normal clauses $\boldsymbol{I}(\boldsymbol{P}):=\boldsymbol{I}$ of the form $\left(H \leftarrow B_{1}, \ldots, B_{m}.\right)$ with logical literals $B_{1}, \ldots, B_{m}$ and an internal atom $H$, which we call the internal part of $\boldsymbol{P}$.
iii) a finite set of generalized ProbLog clauses $\boldsymbol{R}(\boldsymbol{P}):=\boldsymbol{R}$, which we call the random part of $\boldsymbol{P}$.

We say that $\boldsymbol{P}$ is stratified if its internal part $\boldsymbol{I}$ is a stratified set of normal clauses and we say that $\boldsymbol{P}$ is positive if every generalized ProbLog clause of its random part $\boldsymbol{R}(\boldsymbol{P})$ is positive.

A choice of parameters for the program structure $\boldsymbol{P}$ is a function $\pi: \boldsymbol{R}(\boldsymbol{P}) \rightarrow[0,1]$. A program structure $\boldsymbol{P}$ and a choice of parameters $\pi$ yield a (lifted) program $\boldsymbol{P}^{\pi}:=(\boldsymbol{R}(\boldsymbol{P})^{\pi}, \boldsymbol{I}(\boldsymbol{P}), \boldsymbol{C}(\boldsymbol{P}))$, where $\boldsymbol{R}(\boldsymbol{P})^{\pi}$ is the set of ProbLog clauses $\pi(R C):: \operatorname{effect}(R C) \leftarrow \operatorname{causes}(R C) \cup \operatorname{cond}(R C)$ for $R C \in \boldsymbol{R}(\boldsymbol{P})$. In this case, $\boldsymbol{C}(\boldsymbol{P})$ are the constraints, $\boldsymbol{I}(\boldsymbol{P})$ is the internal part and $\boldsymbol{R}(\boldsymbol{P})^{\pi}$ is the random part of the program $\boldsymbol{P}^{\pi}$. Further, $\boldsymbol{P}$ is called the structure of the program $\boldsymbol{P}^{\pi}$. Finally, the program $\boldsymbol{P}^{\pi}$ is stratified or positive if $\boldsymbol{P}$ is.

Example 8. In Example 1 we obtain a stratified program structure $\boldsymbol{P}$ with random part (RC1), (RC2), (RC3), (RC4), internal part (Int) and constraints (Const). Further, we obtain a choice of parameters $\pi$ by assigning $\pi(R C 1):=0.8, \pi(R C 2):=0.1, \pi(R C 3):=0.5$ and $\pi(R C 4):=0.05$. Finally, the choice of parameters $\pi$ gives rise to the following (lifted) program $\boldsymbol{P}^{\pi}$ :
$\%$ Random part
$0.8::$ opens $(E, T):-$ employee $(E)$, tank $(T)$.
$0.1::$ leaks $(T):-$ employee $(E)$, tank $(T)$, opens $(E, T)$.
$0.5::$ smokes $(E, R):-$ employee $(E)$, room $(R)$.
$0.05::$ fire $(R 1):-$ employee $(E)$, room $(R)$, room $(R 1)$, tank $(T)$, liquid $(L)$, flammable(L), in(T,R), stores(T,L), (connected(R,R1); connected(R1,R)), smokes $(E, R)$, Leaks $(T)$.
$\%$ Internal part
connected $(R, R):-r o o m(R)$.
connected $(R, R 1)$ :- room $(R)$, room $(R 1)$, room $(R 2)$, passage $(R 2, R 1)$, connected $(R, R 2)$.
\%Constraints
:- tank(T), liquid(L1), liquid(L2), L1 \= L2, stores(T,L1), stores(T,L2).
Definition 7 (Ground Variable and External Database). Let $\boldsymbol{P}$ be a stratified program structure and let $\mathscr{E}$ be an $\mathfrak{E}$-structure. In our setting, we may assume without loss of generality that $\mathscr{E}$ is a Herbrand model of a language $\mathfrak{E}^{+}$, which extends the external language $\mathfrak{E}$ by constants. Further, denote by $\mathfrak{L}^{+}$and $\mathfrak{Q}^{+}$respectively the extension of the languages $\mathfrak{L}$ and $\mathfrak{Q}$ by the new constants in $\mathfrak{E}^{+}$. We write $\mathscr{E}^{\boldsymbol{I}}:=\mathscr{E}^{\boldsymbol{I}(\boldsymbol{P})}:=\{L$ ground atom of $\mathfrak{L}^{+}: \boldsymbol{I} \cup \mathscr{E} \models L\}$ for the minimal Herbrand model of $\boldsymbol{I} \cup \mathscr{E}$, which is the result of applying the stratified Datalog program $\boldsymbol{I}$ to $\mathscr{E}$.

Further, we call $\mathscr{E}$ an external database of the program structure $\boldsymbol{P}$ if it satisfies the constrains of $\boldsymbol{P}$ after applying the Datalog program $\boldsymbol{I}$ to $\mathscr{E}$, i.e. if

$$
\mathscr{E}^{\boldsymbol{I}} \models \bigwedge_{\substack{\perp \leftarrow L_{1}, \ldots, L_{n} \in \boldsymbol{C}(\boldsymbol{P}) \\ \kappa \text { interpretation on } \operatorname{var}\left(L_{1}, \ldots, L_{n}\right)}} \neg\left(\bigwedge_{i=1}^{n} L_{i}^{\kappa}\right)
$$

A ground variable is a ground atom $G:=r\left(x_{1}, \ldots, x_{n}\right)$ of $\mathfrak{Q}^{+}$with a random predicate $r \in \mathfrak{Q}$. Finally, we write $\mathscr{G}(\mathscr{E})$ for the set of all ground variables.

The term ground variable indicates that we expect $G$ to denote a proper random variable under our semantics. From now on we restrict ourselves to the study of stratified program structures. Hence, let us fix a stratified program structure $\mathbf{P}$ for the rest of this work.

Definition 8 (FCM-Semantics of Lifted Programs). Let $\pi$ be a choice of parameters and let $\mathscr{E}$ be an external database for $\boldsymbol{P}$. The grounding $\boldsymbol{P}^{(\pi, \mathscr{E})}$ of the program structure $\boldsymbol{P}$ with respect to $\pi$ and $\mathscr{E}$ is the system of Boolean equations given by

$$
G:=\underset{\substack{\kappa \text { interpretation on } \operatorname{var}(R C) \\ \operatorname{effect}(R C)^{\pi}=G \\ \left(\mathscr{E}^{\prime}, \kappa\right)=\operatorname{cond}(R C)}}{\bigvee} \quad\left(\bigwedge_{C \in \operatorname{causes}(R C)} C^{\kappa} \wedge u(R C, \kappa)\right)
$$

for every ground variable $G \in \mathscr{G}(\mathscr{E})$. Here, the error term $u(R C, \kappa)$ is a distinct Boolean random variable with the distribution $\pi(u(R C, \kappa))=\pi(R C)$ for every generalized ProbLog clause $R C \in \boldsymbol{R}(\boldsymbol{P})$ and every variable interpretation $\kappa$ on $\operatorname{var}(R C)$. Besides, the error terms $u(R C, \kappa)$ are assumed to be mutually independent. Finally, the grounding of the program $\boldsymbol{Q}:=\boldsymbol{P}^{\pi}$ is given by $\boldsymbol{Q}^{\mathscr{E}}:=\boldsymbol{P}^{(\pi, \mathscr{E})}$.
Example 9. It is easy to observe that the program structure $\boldsymbol{P}$ of Example 8 is indeed a stratified program structure in our sense. Now assume we are given a specific storage, which consists of four rooms $r 1, r 2, r 3$ and $r 4$. These rooms are connected by passages as follows:
passage( $r 1, r 2$ ), passage( $r 2, r 3$ )
Moreover, we have five tanks $t 1, t 2, t 3, t 4$ and $t 5$ with
in $(t 1, r 1)$, in $(t 2, r 2)$, in $(t 3, r 3)$, in $(t 4, r 4)$, in $(t 5, r 4)$.
The tanks contain two types of liquids gasoline and water, which we describe in the following way:
stores(gasoline, t1), stores(gasoline, t2), stores(water, t3),
stores(water, t4), stores(gasoline,t5), flammable(gasoline)
Finally, assume there are two employees Mary and John, which we express simply as mary and john. In this case, one checks that the storage above satisfies the integrity constraint (Const), i.e. we are given an external database $\mathscr{E}$ for the program structure $\boldsymbol{P}$.

Further, let $\pi$ be the choice of parameters in Example 8. For $e \in\{$ john, mary $\}, t \in\left\{t_{1}, t_{2}, t_{3}, t_{4}, t_{5}\right\}$ and $r \in\left\{r_{1}, r_{2}, r_{3}, r_{4}\right\}$ the grounding $\boldsymbol{P}^{(\pi, \mathscr{E})}$ is given by the equations of the form:

- opens $(e, t):=u\left(\left(\_::\right.\right.$opens $(E, T) \leftarrow$ employee $(E), \operatorname{tank}(T) .),\{E \mapsto e, T \mapsto t\})$ such that $u\left(\left(\_::\right.\right.$opens $(E, T) \leftarrow$ employee $(E), \operatorname{tank}(T) .),\{E \mapsto e, T \mapsto t\})$ is true with probability 0.8
- leaks $(t):=\operatorname{opens}(e, t) \wedge u(R C 2,\{E \mapsto e, T \mapsto t\})$ such that $u(R C 2,\{E \mapsto e, T \mapsto t\})$ is true with probability 0.1
- $\operatorname{smokes}(e, r):=u(R C 3,\{E \mapsto e, R \mapsto r\})$ such that $u(R C 3,\{E \mapsto e, R \mapsto r\})$ is true with probability 0.5
- fire $\left(r_{i}\right):=\bigvee_{j=1}^{3} \operatorname{smokes}\left(e, r_{j}\right) \wedge \operatorname{leaks}\left(t_{j}\right) \wedge u\left(R C 4,\left\{R_{1} \mapsto r_{i}, E \mapsto e, R \mapsto r_{j}, T \mapsto t_{j}\right\}\right)$ such that $u\left(R C 4,\left\{R_{1} \mapsto r_{i}, E \mapsto e, R \mapsto r_{j}, T \mapsto t_{j}\right\}\right)$ is true with probability 0.05 for $1 \leq i, j \leq 3$
- fire $\left(r_{4}\right):=\operatorname{smokes}\left(e, r_{4}\right) \wedge \operatorname{leaks}\left(t_{5}\right) \wedge u\left(R C 4,\left\{R_{1} \mapsto r_{4}, E \mapsto e, R \mapsto r_{4}, T \mapsto t_{5}\right\}\right)$ such that $u\left(R C 4,\left\{R_{1} \mapsto r_{4}, E \mapsto e, R \mapsto r_{4}, T \mapsto t_{5}\right\}\right)$ is true with probability 0.05

In the present paper, we reason on a syntactic level about the conditional independencies implied by the program structure $\mathbf{P}$ and an external database $\mathscr{E}$. We proceed as Geiger and Pearl [2] and restrict ourselves to those independence statements following from d-separation in the corresponding propositional causal structures, which we call ground graphs.

Definition 9 (Ground Graph and Acyclicity). Let $\mathscr{E}$ be an external database for $\boldsymbol{P}$. We define the ground graph $\operatorname{Graph}_{\mathscr{E}}(\boldsymbol{P})$ to be the directed graph on the set of ground variables $\mathscr{G}(\mathscr{E})$, which is obtained by drawing an edge $G_{1} \rightarrow G_{2}$ if and only if there exists a generalized ProbLog clause $R C \in \boldsymbol{R}(\boldsymbol{P})$, a cause $C \in \operatorname{causes}(R C)$ and a variable interpretation $\mathfrak{t}$ on $\operatorname{var}(C) \cup \operatorname{var}(\operatorname{effect}(R C))$ such that the following assertions are satisfied:
i) $\left(\mathscr{E}^{\boldsymbol{t}}, \mathfrak{t}\right) \models \exists_{\operatorname{var}(\operatorname{cond}(R C)) \backslash(\operatorname{var}(C) \cup \operatorname{var}(\operatorname{effect}(R C)))} \operatorname{cond}(R C)$
ii) $C^{\mathfrak{t}} \in\left\{G_{1}, \neg G_{1}\right\}$
iii) $\operatorname{effect}(R C)^{\mathfrak{t}}=G_{2}$.

In this case we say that the edge $G_{1} \rightarrow G_{2}$ is induced by $R C$. Moreover, we call $\boldsymbol{P}$ an acyclic program structure if $\operatorname{Graph}_{\mathscr{E}}(\boldsymbol{P})$ is a directed acyclic graph i.e. a causal structure for every external database $\mathscr{E}$.

From now on we assume the program structure $\mathbf{P}$ to be acyclic. In this case it is easy to see that the grounding $\mathrm{P}^{(\pi, \mathscr{E})}$ yields a unique expression for every ground variable $G \in \mathscr{G}(\mathscr{E})$ in terms of the error terms $u(R C, \kappa)$ for every choice of parameters $\pi$ and for every external database $\mathscr{E}$. Hence, it induces a unique probability distribution on $\mathscr{G}(\mathscr{E})$. Rückschloß and Weitkämper [12] further show that this distribution coincides with the distribution semantics of the ProbLog program $\mathbf{P}^{\mathcal{G}} \cup \mathscr{E}$. Overall Definition 6 yields a causal generalization of the standard semantics for acyclic ProbLog programs. Further, we obtain the following result:
Proposition 1 (Rückschloß and Weitkämper [12]). For every external database $\mathscr{E}$ and for every choice of parameters $\pi$ the grounding $\boldsymbol{P}^{(\pi, \mathscr{E})}$ yields a distribution, which is Markov to the ground graph $\operatorname{Graph}_{\mathscr{E}}(\boldsymbol{P})$.

Example 10. The program structure $\boldsymbol{P}$ of Example 8 is indeed acyclic in our sense. Further, in the situation of Example 9 we obtain the following ground graph.
![img-1.jpeg](img-1.jpeg)

As we now defined the necessary refinement of the ProbLog language [1], we can return to reasoning about conditional independence.

# 4 A Symbolic Calculus for Conditional Independencies 

By Proposition 1, for every external database $\mathscr{E}$ the causal information about the conditional independencies implied by our program structure $\mathbf{P}$ lies in the ground graph $\operatorname{Graph}_{\mathscr{E}}(\mathbf{P})$. Hence, applying Theorem 1 we obtain a correct conditional independence oracle if we combine a Prolog representation of the ground graph $\operatorname{Graph}_{\mathscr{E}}(\mathbf{P})$ with the d-separation oracle in Program 1.

Assume we are given a meta-predicate random/2 that indicates all random predicates together with their arities.

Example 11. In Example 8, this means we add the facts
random(opens,2). random(1eaks,1). random(smokes,2). random(fire,1).
to the program structure $\boldsymbol{P}$.

In this case, Program 2 computes the ground graph $\operatorname{Graph}_{\mathscr{E}}(\mathbf{P})$ when applied to the program structure $\mathbf{P}$ and an external database $\mathscr{E}$.
Program 2 (Representation of the Ground Graph).
underlyingAtom(Atom, Atom) :- Atom $\mid=(\mid+_{-})$.
underlyingAtom(Literal,Atom) :- Literal = ( $\mid+$ Literal1), underlyingAtom(Literal1,Atom).
\% Determine the conditions in a body of a random clause
conditions(Body,true) :- Body $\mid=(\_$,$\rangle underlyingAtom(Body, Atom),$ functor(Atom, R,Arity), random(R,Arity).
conditions(Body, Body) :- Body $\mid=(\_$,$\rangle underlyingAtom(Body, Atom),$ functor(Atom, R,Arity), \mid+random(R,Arity).
conditions((C1, Body), Cond) :- underlyingAtom(C1,Atom), functor(Atom, R,Arity), random(R,Arity), conditions(Body, Cond).
conditions((C1, Body),(C1, Cond)) :- underlyingAtom(C1, Atom), functor(Atom, R,Arity), \+random(R,Arity), conditions(Body, Cond).
\% Calculate the potential parents
potentialParents(Body, [Atom]) :- Body $\mid=(\_$,$\rangle underlyingAtom(Body, Atom),$ functor(Atom, R,Arity), random(R,Arity).
potentialParents(Body, []) :- Body $\mid=(\_$,$\rangle underlyingAtom(Body, Atom),$ functor(Atom, R,Arity), \mid+random(R,Arity).
potentialParents((C1, Body), [Atom|Parents]) :- underlyingAtom(C1,Atom), functor(Atom, R,Arity), random(R,Arity), potentialParents(Body, Parents).
potentialParents((C1, Body), Parents) :- underlyingAtom(C1, Atom), functor(Atom, R,Arity), \+random(R,Arity), potentialParents(Body, Parents).
\%Check whether edge exists
(X ---> Y) :- random(R,Arity), functor(Y,R,Arity), clause((_::Y), Body), potentialParents(Body, Parents), member(X, Parents), conditions(Body, Conds), Conds.
Together, Program 1 and 2 yield a meta-interpreter that computes valid conditional independence statements implied by an acyclic, stratified program structure and an external database. In the appendix we prove the following result that establishes the completeness of this conditional independence oracle for a fragment of program structures.
Theorem 3 (Completeness). Let $\boldsymbol{P}$ be a positive program structure and let $\mathscr{E}$ be an external database such that the ground graph $\operatorname{Graph}_{\mathscr{E}}(\boldsymbol{P})$ is singly connected. Further, let $\pi$ be a choice of parameters for $\boldsymbol{P}$ with values in $(0,1)$ that yields proper unconditional probabilities for all ground variables. In this case, the grounding $\boldsymbol{P}^{(\pi, \mathscr{E})}$ yields a distribution that is faithful to the ground graph $\operatorname{Graph}_{\mathscr{E}}(\boldsymbol{P})$.

In particular, if the ground graph $\operatorname{Graph}_{\mathscr{E}}(\boldsymbol{P})$ is singly connected for every external database $\mathscr{E}$ and has a generalized ProbLog clause grounding to a probabilistic fact for every source in $\operatorname{Graph}_{\mathscr{E}}(\boldsymbol{P})$, our meta-interpreter is correct and complete for every choice of parameters $\pi$ of $\boldsymbol{P}$ with values in $(0,1)$.

As singly connected ground graphs imply mutual independence of body atoms, the fragment of Theorem 3 reminds us of the (Ind,Ind) assumption [10], under which marginal probabilities can be computed in a much simpler way.
Example 12. As the program structure $\boldsymbol{P}$ of the introduction lies in the fragment of Theorem 3, Program 1 and 2 yield a correct and complete conditional independence oracle whenever we choose probabilities in $(0,1)$ for every generalized ProbLog clause in $\boldsymbol{P}$.

# 5 Experimental Evaluation 

To evaluate our conditional independence oracle in Program 1 and 2, we investigate the lifted program $\mathbf{P}$ that defines the random predicate random $(p, 1)$ with the random part below.

$$
\operatorname{random}(p, 1) . \quad 0.5:: p(X) \leftarrow n(X) . \quad 0.5:: p(Y) \leftarrow p(X), n(Y), n(Y), e(X, Y)
$$

Further, the program $\mathbf{P}$ expects a directed acyclic graph $G$ as external database, represented by storing its nodes $n / 1$ and its edges $e / 2$. Here, $p / 1$ is a random property that holds with a base probability of 0.5 for every node of $G$. If we observe $p(n)$ for a node $n$ of $G$, this enhances the probability of $p(c)$ for every child $c$ of $n$ by a factor of 0.5 .

Further, we generate directed acyclic graphs $G$ with $S:=5 i$ nodes for $1 \leq i \leq 20$ by sampling five times from the following ProbLog program.

$$
n(1) . \quad n(Y) \leftarrow n(X), Y=X+1, X<S+1 . \quad \frac{1}{\sqrt{S}}:: e(X, Y) \leftarrow n(X), n(Y), X<Y
$$

In this way we obtain five directed acyclic graphs on the nodes $\{1, \ldots, S\}$ that have an edge $i \rightarrow j$ with probability $\sqrt{S}^{-1}$ for every $1 \leq i<j \leq S$. Next, we choose for every graph size $S$ ten tuples $(a, b)$ of even numbers between one and $S$. We then process the queries
$\operatorname{dseparates}(p(a), p(b),[])$ and $\operatorname{dseparates}(p(a), p(b),[p(i): i$ odd number between 1 and S$])$
on $\mathbf{P}$ for every graph of size $S$ using the meta-interpreter of Program 1 and 2 with a timeout of 10 seconds.
Finally, we aim to compare our approach with checking the definition of independence, i.e. with checking whether $\pi(p(a) \wedge p(b))=\pi(p(a)) \cdot \pi(p(b))$. To this aim we additionally calculate the probabilities of $p(a), p(b)$ and $p(a) \wedge p(b)$ with the evidence $\{p(i): i$ odd number between 1 and S$\}$ and without evidence using ProbLog 2 with a timeout of 10 seconds. The median and maximal run times of the queries described above are visualized in Figure 1, clearly demonstrating that our approach performs significantly faster than checking (conditional) independencies with exact inference in ProbLog 2.
![img-2.jpeg](img-2.jpeg)

Figure 1:

## 6 Conclusion

First, we establish a framework for lifted probabilistic logic programming, i.e. we abstract the notion of a ProbLog program away from a concrete database and away from the concrete probabilities mentioned in

the clauses. In this way we obtain so-called program structures. As our main result we then use the theory of d-separation from Bayesian networks to reason about conditional independence on the basis of these program structures. We also implement the corresponding independence oracle as a meta-interpreter in Prolog. Finally, we prove the completeness of our conditional independence oracle for a fragment of programs structures in Theorem 3. The paper then closes with an experimental evaluation of our results revealing that our approach processes significantly faster than checking the definition of independence with exact inference in ProbLog 2.

As the theory of d-separation is the basis of causal structure discovery in Bayesian networks, one direction for future work is to develop the analogue of this theory in probabilistic logic programming. In this context, we note that causal faithfulness is needed to extract possible causal structures from an observed distribution. Furthermore, Theorem 2 suggests that our independence oracle is complete for most program structures and choices of parameters. Hence, in our opinion determining completeness results for more general fragments of program structures is a promising direction for future work.

# Appendix 

Lemma 1 (Weak Transitivity, [7, p.137, Exercise 3.10]). Let $\boldsymbol{A}$ and $\boldsymbol{C}$ be sets of random variables. Further, let $B$ be a Boolean random variable and let $\pi$ be a distribution on $\boldsymbol{A} \cup \boldsymbol{C} \cup\{B\}$. Choose possible values $\boldsymbol{a}$ and $\boldsymbol{c}$ for the random variables in $\boldsymbol{A}$ and $\boldsymbol{C}$ respectively. Further, choose a possible value $b$ for $B$. If $b$ is both dependent on $\boldsymbol{a}$ and on $\boldsymbol{c}$, we find that $\boldsymbol{a}$ and $\boldsymbol{c}$ are marginally dependent or they become dependent once we condition on $b$.
Lemma 2. Let $\pi$ be a distribution on the set $\Omega$ of all valuations on the variables $X, X_{1}, \ldots, X_{n}$ such that $\{X\} \cup\left\{X_{i}\right\}_{i=1, \ldots, n}$ encodes a mutually independent set of events and let $\varphi$ be a propositional formula (in minimal DNF) in which $X$ occurs, and only occurs positively.

Then $\varphi$ and $X$ are positively correlated as events on $\Omega$.
Proof. We must show that $\pi(\varphi \mid X)>\pi(\varphi)$. Let $\psi$ be the formula obtained by substituting $\top$ for $X$ in $\varphi$. Then we have the following:

$$
\pi(\varphi \mid X)=\pi(\psi \mid X)=\pi(\psi)
$$

The first equality holds because $\varphi$ and $\psi$ are equivalent on valuations satisfying $X$, and the second equality holds because $\pi$ is an independent distribution. As $\psi$ is staisfied by all valuations satisfying $\varphi$, but also on at least one valuation not satisfying $\varphi$ (since $X$ occurs in the minimal DNF formula $\varphi$ ), this implies the statement.

Proof of Theorem 3. Let $G:=\operatorname{Graph}_{\mathscr{E}}(\mathbf{P})$ be the ground graph of the program structure $\mathbf{P}$ with respect to the external database $\mathscr{E}$. Let $P$ be a d-connecting path from $A$ to $B$ over a subset of nodes $\mathbf{Z}$ in $G$. We show that for all truly probabilistic choices of parameters, $A$ and $B$ are dependent over $\mathbf{Z}$. Let $\pi$ be the probability distribution on the random variables corresponding to such a choice of parameters. We proceed by induction on the length of $P$.

As we use this in the argument for colliders below, we first show that for directed paths, one obtains the stronger statement that $A$ and $B$ are positively correlated over $\mathbf{Z}$.

We begin with paths of length two. If the length of $P$ is two, there is an edge between $A$ and $B$. Assume without loss of generality that the edge goes from $A$ to $B$. Consider the definition $\varphi$ of $B$ in the Clark completion of the logic program associated with $\mathbf{P}$. This is a propositional formula in the parents of $B$ and the error terms of ground clauses with head $B$; Since $A$ is a parent of $B$, there is a clause $\mathscr{C}$

whose body includes $A$, and thus since $B$ is true if and only if $A$ is true when the error terms associated with all other clauses are set to false and all other facts in the body of $\mathscr{C}$ are true, $A$ occurs in a minimal disjunctive normal form representation of $\varphi$. As $G$ is singly connected, the only path between any two parents of $B$ is via $B \notin \mathbf{Z}$, and thus the distribution induced by $\pi \mid Z$ on the parents of $B$ is independent by the correctness of d-separation. Therefore $A$ and $B$ are positively correlated by Lemma 2.

So assume it to be true for directed paths of length $n$ and let $A_{1} \ldots A_{n} A_{n+1}$ be a directed path of length $n+1$. Then $\pi\left(A_{n+1} \mid A_{1}, Z\right)$ is equal to

$$
\pi\left(A_{n+1} \mid A_{n}, A_{1}, Z\right) \pi\left(A_{n} \mid A_{1}, Z\right)+\pi\left(A_{n+1} \mid \neg A_{n}, A_{1}, Z\right) \pi\left(\neg A_{n} \mid A_{1}, Z\right)
$$

and $\pi\left(A_{n+1} \mid Z\right)$ is equal to

$$
\pi\left(A_{n+1} \mid A_{n}, Z\right) \pi\left(A_{n} \mid Z\right)+\pi\left(A_{n+1} \mid \neg A_{n}, Z\right) \pi\left(\neg A_{n} \mid Z\right)
$$

Since $P$ is the only path between $A_{1}$ and $A_{n+1}, A_{1}$ and $A_{n+1}$ are d-separated by $A_{n}$. Thus, we find $\pi\left(A_{n+1} \mid A_{n}, A_{1}, Z\right)=\pi\left(A_{n+1} \mid A_{n}, Z\right)$ and $\pi\left(A_{n+1} \mid \neg A_{n}, A_{1}, Z\right)=\pi\left(A_{n+1} \mid \neg A_{n}, Z\right)$. Furthermore, by the induction hypothesis, $\pi\left(A_{n+1} \mid A_{n}, Z\right)>\pi\left(A_{n+1} \mid \neg A_{n}, Z\right)$ and $\pi\left(A_{n} \mid A_{1}, Z\right)>\pi\left(A_{n} \mid Z\right)$. Overall, this implies that $\pi\left(A_{n+1} \mid A_{1}, Z\right)>\pi\left(A_{n+1} \mid Z\right)$ as required.

We now return to the case of a general d-connecting path. As paths of length 2 are necessarily directed, the base step of the induction follows from the directed case above. So assume that dependence holds for all paths of length $n$ and let $P$ be a path of length $n+1>2$.

We proceed by appeal to weak transitivity.
Let $A^{\prime}, C$ and $B$ be the final three nodes in $P$. We first cover the case where $C$ is not a collider.
Then by the induction hypothesis, $A$ and $C$ are dependent over $\mathbf{Z}$, and by the length two case above, $C$ and $B$ are dependent over $\mathbf{Z}$. Thus, either $A$ and $B$ are dependent over $\mathbf{Z}$, or they are dependent over $\{C\} \cup \mathbf{Z}$. However, since $G$ is singly connected, $P$ is the only path from $A$ to $B$ and thus $A$ and $B$ are d-separated by $\{C\} \cup \mathbf{Z}$. Together with the correctness of d-separation we can conclude that $A$ and $B$ are dependent over $\mathbf{Z}$.

Now consider the case of a collider where $C$ has a descendant in $\mathbf{Z}$. Note that since conditioning on a descendant $C_{i}$ of $C$ blocks the (only) path between $A$ and $B$ and any descendant $C^{\prime}$ of $C_{i}$, we can assume by correctness of d-separation without loss of generality that all descendants $C_{i}$ of $C$ in $\mathbf{Z}$ are nondescendants of each other. Let $\left\{C_{i}\right\}_{i=1, \ldots, n}$ be the descendants of $C$ in $\mathbf{Z}$, and let $\mathbf{Z}^{\prime}:=\mathbf{Z} \backslash\left\{C_{i}\right\}_{i=1, \ldots, n}$.

We show by induction on $n$ that $\pi\left(X \mid C_{1}, \ldots, C_{n}, \mathbf{Z}^{\prime}\right)>\pi\left(X, \mathbf{Z}^{\prime}\right)$ for $X \in\left\{A^{\prime}, B\right\}$. The base case of the induction is given by the special case of a directed path above. So assume $\pi\left(X \mid C_{1}, \ldots, C_{n}, \mathbf{Z}^{\prime}\right)>\pi\left(X \mid \mathbf{Z}^{\prime}\right)$. We want to show that $\pi\left(X \mid C_{1}, \ldots, C_{n}, C_{n+1}, \mathbf{Z}^{\prime}\right)>\pi\left(X \mid \mathbf{Z}^{\prime}\right)$. However, we know that

$$
\pi\left(X \mid C_{1}, \ldots, C_{n}, C_{n+1}, \mathbf{Z}^{\prime}\right)>\pi\left(X \mid C_{1}, \ldots, C_{n}, \mathbf{Z}^{\prime}\right)
$$

by the special case of directed paths above, from which the claim follows.
To apply weak transitivity, we alter the graph by introducing a new node $\wedge C$ with arrows from every $C_{i}$ into $\wedge C$. We extend the probability distribution to $\wedge C$ by setting $\wedge C$ to be true of and only if all $C_{i}$ are true. By the argument above, $A^{\prime}$ and $B$ are both positively correlated with $\wedge C$ over $\mathbf{Z}^{\prime}$. Thus, by weak transitivity, either $A^{\prime}$ and $B$ are dependent over $\mathbf{Z}^{\prime}$ or they are dependent over $\{\wedge C\} \cup \mathbf{Z}^{\prime}$. The former is excluded by the correctness of d-separation and the fact that the collider $C$ blocks the only path from $A^{\prime}$ to $B$ (since the original graph was singly connected). Therefore $A^{\prime}$ and $B$ are dependent over $\{\wedge C\} \cup \mathbf{Z}^{\prime}$, which implies $A^{\prime}$ and $B$ being dependent over $\mathbf{Z}=C_{1}, \ldots, C_{n}, \mathbf{Z}^{\prime}$ in the original graph.

We can now conclude the proof by using weak transitivity and singly-connectedness a final time to deduce that $A$ and $B$ are dependent over $Z$ from the fact that $A$ and $A^{\prime}$ are dependent over $Z$ (the induction hypothesis) and the fact that $A^{\prime}$ and $B$ are dependent over $Z$.