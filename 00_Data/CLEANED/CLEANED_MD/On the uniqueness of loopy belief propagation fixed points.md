# ResearchGate 

See discussions, stats, and author profiles for this publication at: https://www.researchgate.net/publication/8238641

## On the Uniqueness of Loopy Belief Propagation Fixed Points

Article $10^{\circ}$ Neural Computation - November 2004
DOI: $10.1162 / 0899766041941943$ - Source: PubMed

CITATIONS
150

1 author:

Tom Heskes
Radboud University
401 PUBLICATIONS 11,738 CITATIONS
SEE PROFILE

# On the Uniqueness of Loopy Belief Propagation Fixed Points 

Tom Heskes<br>tom@snn.kun.nl<br>SNN, University of Nijmegen, 6525 EZ, Nijmegen, The Netherlands


#### Abstract

We derive sufficient conditions for the uniqueness of loopy belief propagation fixed points. These conditions depend on both the structure of the graph and the strength of the potentials and naturally extend those for convexity of the Bethe free energy. We compare them with (a strengthened version of) conditions derived elsewhere for pairwise potentials. We discuss possible implications for convergent algorithms, as well as for other approximate free energies.


## 1 Introduction

Loopy belief propagation is Pearl's belief propagation (Pearl, 1988) applied to networks containing cycles. It can be used to compute approximate marginals in Bayesian networks and Markov random fields. Whereas belief propagation is exact only in special cases, for example, for tree-structured (singly connected) networks with just gaussian or just discrete nodes, loopy belief propagation empirically often leads to good performance (Murphy, Weiss, \& Jordan, 1999; McEliece, MacKay, \& Cheng, 1998). That is, the approximate marginals computed with loopy belief propagation are in many cases close to the exact marginals. In gaussian graphical models, the means are guaranteed to coincide with the exact means (Weiss \& Freeman, 2001). The notion that fixed points of loopy belief propagation correspond to extrema of the so-called Bethe free energy (Yedidia, Freeman, \& Weiss, 2001) is an important step in the theoretical understanding of this success and paved the road for interesting generalizations.

However, when applied to graphs with cycles, loopy belief propagation does not always converge. So-called double-loop algorithms have been proposed that do guarantee convergence (Yuille, 2002; Teh \& Welling, 2002; Heskes, Albers, \& Kappen, 2003), but are an order of magnitude slower than standard loopy belief propagation. It is generally believed that there is a close connection between (non)convergence of loopy belief propagation and (non)uniqueness of loopy belief propagation fixed points. More specifically, the working hypothesis is that uniqueness of a loopy belief propagation fixed point guarantees convergence of loopy belief propagation to this fixed point. The goal of this study, then, is to derive sufficient

conditions for uniqueness. Such conditions are not only relevant from a theoretical point of view, but can also be used to derive faster algorithms and suggest different free energies, as will be discussed in section 9.

# 2 Outline 

Before getting into the mathematical details, we first sketch the line of reasoning that will be followed in this article. It is inspired by the connection between fixed points of loopy belief propagation and extrema of the Bethe free energy, by studying the Bethe free energy we can learn about properties of loopy belief propagation.

The Bethe free energy is an approximation to the exact variational GibbsHelmholtz free energy. Both are concepts from (statistical) physics. Abstracting from the physical interpretation, the Gibbs-Helmholtz free energy is "just" a functional with a unique minimum, the argument of which corresponds to the exact probability distribution. However, the Gibbs-Helmholtz free energy is as intractable as the exact probability distribution. The idea is then to approximate the Gibbs-Helmholtz free energy in the hope that the minimum of such a tractable approximate free energy relates to the minimum of the exact free energy. Examples of such approximations are the mean-field free energy, the Bethe free energy, and the Kikuchi free energy. The connections between the Gibbs-Helmholtz free energy, Bethe free energy, and loopy belief propagation are reviewed in section 3.

The Bethe free energy is a function of so-called pseudomarginals or beliefs. For the minimum of the Bethe free energy to make sense, these pseudomarginals have to be properly normalized as well as consistent. Our starting point, the upper-left corner in Figure 1, is a constrained minimization problem. In general, it is in fact a nonconvex constrained minimization problem since the Bethe free energy is a nonconvex function of the pseudomarginals (the constraints are linear in these pseudomarginals).

However, using the constraints on the pseudomarginals, it may be possible to rewrite the Bethe free energy in a form that is convex in the pseudomarginals. When this is possible, we call the Bethe free energy "convex over the set of constraints" (Pakzad \& Anantharam, 2002). Now, if the Bethe free energy is convex over the set of constraints, we have, in combination with the linearity of the constraints, a convex constrained minimization problem. Convex constrained minimization problems have a unique solution (see, e.g., (Luenberger, 1984), which explains link d in Figure 1.

Sufficient conditions for convexity over the set of constraints, link b in Figure 1, can be found in Pakzad and Anantharam (2002) and Heskes et al. (2003). They are (re)derived and discussed in section 4. These conditions depend on only the structure of the graph, not on the (strength of the) potentials that make up the probability distribution defined over this graph. A corollary of these conditions, derived in section 4.3, is that the Bethe free energy for a graph with a single loop is "just" convex over the set of

![img-0.jpeg](img-0.jpeg)

Figure 1: Layout of correspondences and implications. See the text for details.
constraints: with two or more connected loops, the conditions fail (see also McEliece \& Yildirim, 2003).

Milder conditions for uniqueness, which do depend on the strength of the interactions, follow from the track on the right-hand side of Figure 1. First, we note that nonconvex constrained minimization of the Bethe free energy is equivalent to an unconstrained nonconvex/concave minimax problem (Heskes, 2002), link a in Figure 1. Convergent double-loop algorithms like CCCP (Yuille, 2002) and faster variants thereof (Heskes et al., 2003) in fact solve such a minimax problem: the concave problem in the maximizing parameters (basically Lagrange multipliers) is solved by a message-passing algorithm very similar to standard loopy belief propagation in the inner loop, where the outer loop changes the minimizing parameters (a remaining set of pseudomarginals) in the proper downward direction. The transformation

from nonconvex constrained minimization problem to an unconstrained nonconvex/concave minimax problem is, in a particular setting relevant to this article, repeated in section 5.1.

Rather than requiring the Bethe free energy to be convex (over the set of constraints), we then in sections 6 and 8 work toward conditions under which this minimax problem is convex/concave. These indeed depend on the strength of the potentials, defined in section 7. These conditions can be considered the main result of this article. Link c follows from the observation, in section 5.2, that the minimax problem corresponding to a Bethe free energy that is convex over the set of constraints has to be convex or concave.

As indicated by link e, convex/concave minimax problems have a unique solution. This then also implies that the Bethe free energy has a unique extremum satisfying the constraints, which, since the Bethe free energy is bounded from below (see section 5.3), has to be a minimum: link f.

The concluding statement by link $g$ in the lower-right corner is, to the best of our knowledge, no more than a conjecture. We discuss it in more detail in section 9 .

# 3 The Bethe Free Energy and Loopy Belief Propagation 

3.1 The Gibbs-Helmholtz Free Energy. The exact probability distribution in Bayesian networks and Markov random fields can be written in the factorized form

$$
P_{\text {exact }}(X)=\frac{1}{Z} \prod_{\alpha} \Psi_{\alpha}\left(X_{\alpha}\right)
$$

Here $\Psi_{\alpha}$ is a potential, some function of the potential subset $X_{\alpha}$, and $Z$ is an unknown normalization constant. Potential subsets typically overlap, and they span the whole domain $X$. The convention that we adhere to in this article is that there are no potential subsets $X_{\alpha}$ and $X_{\alpha^{\prime}}$ such that $X_{\alpha^{\prime}}$ is fully subsumed by $X_{\alpha}$. The standard choice of a potential in a Bayesian network is a child with all its parents. We further restrict ourselves to probabilistic models defined on discrete random variables, each of which runs over a finite number of states. The potentials are positive and finite.

The typical goal in Bayesian networks and Markov random fields is to compute the partition function $Z$ or marginals, for example,

$$
P_{\text {exact }}\left(X_{\alpha}\right)=\sum_{X_{\backslash \alpha}} P_{\text {exact }}(X)
$$

One way to do this is with the junction tree algorithm (Lauitzen \& Spiegelhalter, 1988). However, the junction tree algorithm scales exponentially with the size of the largest clique and may become intractable for complex models. The alternative is then to resort to approximate methods, which can be

roughly divided into two categories: sampling approaches and deterministic approximations.

Most deterministic approximations derive from the so-called GibbsHelmholtz free energy,

$$
F(P)=-\sum_{\alpha} \sum_{X_{\alpha}} P\left(X_{\alpha}\right) \psi_{\alpha}\left(X_{\alpha}\right)+\sum_{X} P(X) \log P(X)
$$

with shorthand $\psi \equiv \log \Psi$. Minimizing this variational free energy over the set $\mathcal{P}$ of all properly normalized probability distributions, we get back the exact probability distribution, equation 3.1, as the argument at the minimum and minus the log of the partition function as the value at the minimum:

$$
P_{\text {exact }}=\underset{P \in \mathcal{P}}{\operatorname{argmin}} F(P) \text { and }-\log Z=\min _{P \in \mathcal{P}} F(P)
$$

Since the Gibbs-Helmholtz free energy is convex in $P$, the equality constraint (proper normalization) is linear, and the inequality constraints (nonnegativity) are convex, this minimum is unique. By itself, we have not gained anything: the entropy may still be intractable to compute.
3.2 The Bethe Free Energy. The Bethe free energy is an approximation of the exact Gibbs-Helmholtz free energy. In particular, we approximate the entropy through

$$
\begin{aligned}
\sum_{X} P(X) \log P(X) \approx & \sum_{\alpha} \sum_{X_{\alpha}} P\left(X_{\alpha}\right) \log P\left(X_{\alpha}\right) \\
& -\sum_{\beta}\left(n_{\beta}-1\right) \sum_{x_{\beta}} P\left(x_{\beta}\right) \log P\left(x_{\beta}\right)
\end{aligned}
$$

with $x_{\beta}$ a (super)node and $n_{\beta}=\sum_{\alpha \supset \beta} 1$ : the number of potentials that contains node $x_{\beta}$. The second term follows from a discounting argument: without it, we would overcount the entropy contributions on the overlap between the potential subsets. The (super)nodes $x_{\beta}$ are themselves subsets of the potential subsets, that is,

$$
x_{\beta} \cap X_{\alpha}=\emptyset \text { or } x_{\beta} \cap X_{\alpha}=x_{\beta} \forall_{\alpha, \beta}
$$

and partition the domain $X$,

$$
x_{\beta} \cap x_{\beta^{\prime}}=\emptyset \quad \forall_{\beta, \beta^{\prime}} \text { and } \bigcup_{\beta} x_{\beta}=X
$$

Typically the $x_{\beta}$ are taken to be single nodes, and in the following we will refer to them as such. For clarity of notation, we will indicate these nodes by $\beta$ and $x_{\beta}$ in lowercase, to contrast them with the potentials $\alpha$ and potential subsets $X_{\alpha}$ in uppercase.

Note that the Bethe free energy depends on only the marginals $P\left(X_{\alpha}\right)$ and $P\left(x_{\beta}\right)$. We replace minimization of the exact Gibbs-Helmholtz free energy over probability distributions by minimization of the Bethe free energy,

$$
\begin{aligned}
F\left(Q_{\alpha}, Q_{\beta}\right)= & -\sum_{\alpha} \sum_{X_{\alpha}} Q_{\alpha}\left(X_{\alpha}\right) \psi_{\alpha}\left(X_{\alpha}\right)+\sum_{\alpha} \sum_{X_{\alpha}} Q_{\alpha}\left(X_{\alpha}\right) \log Q_{\alpha}\left(X_{\alpha}\right) \\
& -\sum_{\beta}\left(n_{\beta}-1\right) \sum_{x_{\beta}} Q_{\beta}\left(x_{\beta}\right) \log Q_{\beta}\left(x_{\beta}\right)
\end{aligned}
$$

over sets of "pseudomarginals" ${ }^{1}$ or beliefs $\left\{Q_{\alpha}, Q_{\beta}\right\}$. For this to make sense, these pseudomarginals have to be properly normalized as well as consistent, that is, ${ }^{2}$

$$
\sum_{X_{\alpha}} Q_{\alpha}\left(X_{\alpha}\right)=1 \text { and } Q_{\alpha}\left(x_{\beta}\right)=\sum_{X_{\alpha \backslash \beta}} Q_{\alpha}\left(X_{\alpha}\right)=Q_{\beta}\left(x_{\beta}\right)
$$

Let $\mathcal{Q}$ denote all subsets of consistent and properly normalized pseudomarginals. Then our goal is to solve

$$
\min _{\left\{Q_{\alpha}, Q_{\beta}\right\} \in \mathcal{Q}} F\left(Q_{\alpha}, Q_{\beta}\right)
$$

The hope is that the pseudomarginals at this minimum are accurate approximations to the exact marginals $P_{\text {exact }}\left(X_{\alpha}\right)$ and $P_{\text {exact }}\left(x_{\beta}\right)$.
3.3 Link with Loopy Belief Propagation. For completeness and later reference, we describe the link between the Bethe free energy and loopy belief propagation, as originally reported on by Yedidia et al. (2001). It starts with the Lagrangian

$$
\begin{aligned}
L\left(Q_{\alpha}, Q_{\beta}, \lambda_{\alpha \beta}, \lambda_{\alpha}, \lambda_{\beta}\right)= & F\left(Q_{\alpha}, Q_{\beta}\right) \\
& +\sum_{\beta} \sum_{\alpha \supset \beta} \sum_{x_{\beta}} \lambda_{\alpha \beta}\left(x_{\beta}\right)\left[Q_{\beta}\left(x_{\beta}\right)-Q_{\alpha}\left(x_{\beta}\right)\right] \\
& +\sum_{\alpha} \lambda_{\alpha}\left[1-\sum_{X_{\alpha}} Q_{\alpha}\left(X_{\alpha}\right)\right] \\
& +\sum_{\beta} \lambda_{\beta}\left[1-\sum_{\beta} Q_{\beta}\left(x_{\beta}\right)\right]
\end{aligned}
$$

[^0]
[^0]:    ${ }^{1}$ Terminology from Wainwright, Jaakkola, and Willsky (2002), used to indicate that there need not be a joint distribution that would yield such marginals.
    ${ }^{2}$ Strictly speaking we also have to take inequality constraints into account, namely, those of the form $Q_{\alpha}\left(X_{\alpha}\right) \geq 0$. However, with the potentials being positive and finite, the logarithmic terms in the free energy make sure that we never really have to worry about those; they never become "active." For convenience, we will not consider them any further.

At an extremum of the Bethe free energy satisfying the constraints, all derivatives of $L$ are zero: the ones with respect to the Lagrange multipliers $\lambda$ give back the constraints; the ones with respect to the pseudomarginals $Q$ give an extremum of the Bethe free energy. Setting the derivatives with respect to $Q_{\alpha}$ and $Q_{\beta}$ to zero, we can solve for $Q_{\alpha}$ and $Q_{\beta}$ in terms of the Lagrange multipliers:

$$
\begin{aligned}
Q_{\alpha}^{*}\left(X_{\alpha}\right) & =\Psi_{\alpha}\left(X_{\alpha}\right) \exp \left[\lambda_{\alpha}-1+\sum_{\beta \subset \alpha} \lambda_{\alpha \beta}\left(x_{\beta}\right)\right] \\
Q_{\beta}^{*}\left(x_{\beta}\right) & =\exp \left[\frac{1}{n_{\beta}-1}\left\{1-\lambda_{\beta}+\sum_{\alpha \supset \beta} \lambda_{\alpha \beta}\left(x_{\beta}\right)\right\}\right]
\end{aligned}
$$

In terms of the"message" $\mu_{\beta \rightarrow \alpha}\left(x_{\beta}\right) \equiv \exp \left[\lambda_{\alpha \beta}\left(x_{\beta}\right)\right]$ from node $\beta$ to potential $\alpha$, the pseudomarginal $Q_{\alpha}^{*}\left(X_{\alpha}\right)$ reads

$$
Q_{\alpha}^{*}\left(X_{\alpha}\right) \propto \Psi_{\alpha}\left(X_{\alpha}\right) \prod_{\beta \subset \alpha} \mu_{\beta \rightarrow \alpha}\left(x_{\beta}\right)
$$

where proper normalization yields the Lagrange multiplier $\lambda_{\alpha}$. With definition

$$
\mu_{\alpha \rightarrow \beta}\left(x_{\beta}\right) \equiv \frac{Q_{\beta}^{*}\left(x_{\beta}\right)}{\mu_{\beta \rightarrow \alpha}\left(x_{\beta}\right)}
$$

the fixed-point equation for $Q_{\beta}^{*}\left(x_{\beta}\right)$ can, after some manipulation, be written in the form

$$
Q_{\beta}^{*}\left(x_{\beta}\right) \propto \prod_{\alpha \supset \beta} \mu_{\alpha \rightarrow \beta}\left(x_{\beta}\right)
$$

where again the Lagrange multiplier $\lambda_{\beta}$ follows from normalization. Finally, the constraint $Q_{\alpha}^{*}\left(x_{\beta}\right)=Q_{\beta}^{*}\left(x_{\beta}\right)$ in combination with equation 3.6 suggests the update

$$
\mu_{\alpha \rightarrow \beta}\left(x_{\beta}\right)=\frac{Q_{\alpha}^{*}\left(x_{\beta}\right)}{\mu_{\beta \rightarrow \alpha}\left(x_{\beta}\right)}
$$

Equations 3.5 through 3.8 constitute the belief propagation equations. They can be summarized as follows. A pseudomarginal is the potential (just 1 for the nodes in the convention where no potentials are assigned to nodes) times its incoming messages; the outgoing message is the pseudomarginal divided by the incoming message. The scheduling of the messages is somewhat arbitrary. Loopy belief propagation can be "damped" by taking smaller

steps. This damping is usually done in terms of the Lagrange multipliers, that is, in the log domain of the messages:

$$
\begin{aligned}
\log \mu_{\alpha \rightarrow \beta}^{\mathrm{new}}\left(x_{\beta}\right)= & \log \mu_{\alpha \rightarrow \beta}\left(x_{\beta}\right) \\
& \left.+\epsilon\left[\left\{\log Q_{\alpha}^{*}\left(x_{\beta}\right)-\log \mu_{\beta \rightarrow \alpha}\left(x_{\beta}\right)\right\}-\log \mu_{\alpha \rightarrow \beta}\left(x_{\beta}\right)\right] .\right.
\end{aligned}
$$

Summarizing, loopy belief propagation is equivalent to fixed-point iteration, where the fixed points are the zero derivatives of the Lagrangian.

# 4 Convexity of the Bethe Free Energy 

4.1 Rewriting the Bethe Free Energy. Minimization of the Bethe free energy, equation 3.2, under the constraints of equation 3.3 is equivalent to solving a minimax problem on the Lagrangian, equation 3.4, namely,

$$
\min _{Q_{\alpha}, Q_{\beta}} \max _{\lambda_{\alpha \beta}, \lambda_{\alpha}, \lambda_{\beta}} L\left(Q_{\alpha}, Q_{\beta}, \lambda_{\alpha \beta}, \lambda_{\alpha}, \lambda_{\beta}\right)
$$

The ordering of the min and max operations is important here: to enforce the constraints, we first have to take the maximum. The min and max operations can be interchanged if we have a convex constrained minimization problem (Luenberger, 1984). That is, the function to be minimized must be convex in its parameters, the equality constraints have to be linear, and the inequality constraints convex. In our case, the equality constraints are indeed linear, and the inequality constraints enforcing nonnegativity of the pseudomarginals indeed are convex. However, the Bethe free energy, equation 3.2, is clearly nonconvex in its parameters $\left\{Q_{\alpha}, Q_{\beta}\right\}$. This is what makes it a difficult optimization problem.

Luckily the description in equation 3.2 is not unique: any other form that can be constructed by substituting the constraints of equation 3.3 is equally valid. Following Pakzad and Anantharam (2002), we call the Bethe free energy "convex over the set of constraints" if, by making use of the constraints of equation 3.3, we can rewrite it in a form that is convex in $\left\{Q_{\alpha}, Q_{\beta}\right\}$.
4.2 Conditions for Convexity. The problem is with the term

$$
S_{\beta}\left(Q_{\beta}\right) \equiv-\sum_{x_{\beta}} Q_{\beta}\left(x_{\beta}\right) \log Q_{\beta}\left(x_{\beta}\right)
$$

which is concave in $Q_{\beta}$. Using the constraint $Q_{\beta}\left(x_{\beta}\right)=Q_{\alpha}\left(x_{\beta}\right)$, we can turn it into a functional that is convex in $Q_{\alpha}$ and $Q_{\beta}$ separately, but not necessarily jointly. That is, with the substitution $Q_{\beta}\left(x_{\beta}\right)=Q_{\alpha}\left(x_{\beta}\right)$ for any $\alpha \supset \beta$, the entropy, and thus the Bethe free energy, is convex in $Q_{\alpha}$ and in $Q_{\beta}$, but not necessarily in $\left\{Q_{\alpha}, Q_{\beta}\right\}$. However, if we add to $S_{\beta}\left(Q_{\beta}\right)$ a convex entropy contribution,

$$
-S_{\alpha}\left(Q_{\alpha}\right) \equiv \sum_{X_{\alpha}} Q_{\alpha}\left(X_{\alpha}\right) \log Q_{\alpha}\left(X_{\alpha}\right)
$$

the combination of $-S_{\alpha}$ and $S_{\beta}$ is convex in $\left\{Q_{\alpha}, Q_{\beta}\right\}$, as the following lemma, needed in the proof of theorem 1 below, shows.

# Lemma 1. 

$$
\Delta_{\alpha \beta}\left(Q_{\alpha}, Q_{\beta}\right) \equiv \sum_{X_{\alpha}} Q_{\alpha}\left(X_{\alpha}\right) \log Q_{\alpha}\left(X_{\alpha}\right)-\sum_{x_{\beta}} Q_{\alpha}\left(x_{\beta}\right) \log Q_{\beta}\left(x_{\beta}\right)
$$

is convex in $\left\{Q_{\alpha}, Q_{\beta}\right\}$.
Proof. The matrix with second derivatives of $\Delta_{\alpha \beta}$ has the components

$$
\begin{aligned}
H\left(X_{\alpha}, X_{\alpha}^{\prime}\right) & \equiv \frac{\partial^{2} \Delta_{\alpha \beta}}{\partial Q_{\alpha}\left(X_{\alpha}\right) \partial Q_{\alpha}\left(X_{\alpha}^{\prime}\right)}=\frac{1}{Q_{\alpha}\left(X_{\alpha}\right)} \delta_{X_{\alpha}, X_{\alpha}^{\prime}} \\
H\left(X_{\alpha}, x_{\beta}^{\prime}\right) & \equiv \frac{\partial^{2} \Delta_{\alpha \beta}}{\partial Q_{\alpha}\left(X_{\alpha}\right) \partial Q_{\beta}\left(x_{\beta}^{\prime}\right)}=-\frac{1}{Q_{\beta}\left(x_{\beta}\right)} \delta_{x_{\beta}, x_{\beta}^{\prime}} \\
H\left(x_{\beta}, x_{\beta}^{\prime}\right) & \equiv \frac{\partial^{2} \Delta_{\alpha \beta}}{\partial Q_{\beta}\left(x_{\beta}\right) \partial Q_{\beta}\left(x_{\beta}^{\prime}\right)}=-\frac{Q_{\alpha}\left(x_{\beta}\right)}{Q_{\beta}^{2}\left(x_{\beta}\right)} \delta_{x_{\beta}, x_{\beta}^{\prime}}
\end{aligned}
$$

where we note that $X_{\alpha}$ and $x_{\beta}$ should be interpreted as indices. Convexity requires that for any "vector" $\left(R_{\alpha}\left(X_{\alpha}\right) \quad R_{\beta}\left(x_{\beta}\right)\right)$,

$$
\begin{aligned}
0 & \leq\left(R_{\alpha}\left(X_{\alpha}\right) \quad R_{\beta}\left(x_{\beta}\right)\right)\left(\begin{array}{cc}
H\left(X_{\alpha}, X_{\alpha}^{\prime}\right) & H\left(X_{\alpha}, x_{\beta}^{\prime}\right) \\
H\left(x_{\beta}, X_{\alpha}^{\prime}\right) & H\left(x_{\beta}^{\prime}, x_{\beta}\right)
\end{array}\right)\binom{R_{\alpha}\left(X_{\alpha}^{\prime}\right)}{R_{\beta}\left(x_{\beta}^{\prime}\right)} \\
& =\sum_{X_{\alpha}} \frac{R_{\alpha}^{2}\left(X_{\alpha}\right)}{Q_{\alpha}\left(X_{\alpha}\right)}-2 \sum_{X_{\alpha}} \frac{R_{\alpha}\left(X_{\alpha}\right) R_{\beta}\left(x_{\beta}\right)}{Q_{\beta}\left(x_{\beta}\right)}+\sum_{x_{\beta}} \frac{Q_{\alpha}\left(x_{\beta}\right) R_{\beta}^{2}\left(x_{\beta}\right)}{Q_{\beta}^{2}\left(x_{\beta}\right)} \\
& =\sum_{X_{\alpha}} Q_{\alpha}\left(X_{\alpha}\right)\left[\frac{R_{\alpha}\left(X_{\alpha}\right)}{Q_{\alpha}\left(X_{\alpha}\right)}-\frac{R_{\beta}\left(x_{\beta}\right)}{Q_{\beta}\left(x_{\beta}\right)}\right]^{2}
\end{aligned}
$$

The idea is that the Bethe free energy is convex over the set of constraints if we have sufficient convex resources $Q_{\alpha} \log Q_{\alpha}$ to compensate for the concave $-Q_{\beta} \log Q_{\beta}$ terms. This can be formalized in the following theorem.

Theorem 1. The Bethe free energy is convex over the set of consistency constraints if there exists an allocation matrix $A_{\alpha \beta}$ between potentials $\alpha$ and nodes $\beta$ satisfying

1. $A_{\alpha \beta} \geq 0 \quad \forall_{\alpha, \beta \subset \alpha} \quad$ (positivity)
2. $\sum_{\beta \subset \alpha} A_{\alpha \beta} \leq 1 \quad \forall_{\alpha} \quad$ (sufficient amount of resources)
3. $\sum_{\alpha \supset \beta} A_{\alpha \beta} \geq n_{\beta}-1 \quad \forall_{\beta} \quad$ (sufficient compensation).

Proof. First, we note that we do not have to worry about the energy terms that are linear in $Q_{\alpha}$. In other words, to prove the theorem, we can restrict ourselves to proving that minus the entropy,

$$
-S(Q)=-\left[\sum_{\alpha} S_{\alpha}\left(Q_{\alpha}\right)-\sum_{\beta}\left(n_{\beta}-1\right) S_{\beta}\left(Q_{\beta}\right)\right]
$$

is convex over the set of consistency constraints. The resulting operation is now a matter of resource allocation. For each concave contribution ( $n_{\beta}-$ 1) $S_{\beta}$, we have to find convex contributions $-S_{\alpha}$ to compensate for it. Let $A_{\alpha \beta}$ denote the "amount of resources" that we take from potential subset $\alpha$ to compensate for node $\beta$. Now, in shorthand notation and with a little bit of rewriting,

$$
\begin{aligned}
-S(Q)= & -\left[\sum_{\alpha} S_{\alpha}-\sum_{\beta}\left(n_{\beta}-1\right) S_{\beta}\right] \\
= & -\sum_{\alpha}\left(1-\sum_{\beta \subset \alpha} A_{\alpha \beta}+\sum_{\beta \subset \alpha} A_{\alpha \beta}\right) S_{\alpha} \\
& -\sum_{\beta}\left\{-\sum_{\alpha \supset \beta} A_{\alpha \beta}+\sum_{\alpha \supset \beta} A_{\alpha \beta}-\left(n_{\beta}-1\right)\right\} S_{\beta} \\
= & -\sum_{\alpha}\left(1-\sum_{\beta \subset \alpha} A_{\alpha \beta}\right) S_{\alpha}-\sum_{\alpha} \sum_{\beta \subset \alpha} A_{\alpha \beta}\left[S_{\alpha}-S_{\beta}\right] \\
& -\sum_{\beta}\left[\sum_{\alpha \supset \beta} A_{\alpha \beta}-\left(n_{\beta}-1\right)\right] S_{\beta}
\end{aligned}
$$

Convexity of the first term is guaranteed if $1-\sum_{\beta} A_{\alpha \beta} \geq 0$ (condition 2), of the second term if $A_{\alpha \beta} \geq 0$ (condition 1 and lemma 1), and of the third term if $\sum_{\alpha} A_{\alpha \beta}-\left(n_{\beta}-1\right) \geq 0$ (condition 3).

This theorem is a special case of the one in Heskes et al. (2003) for the more general Kikuchi free energy. Either one of the inequality signs in condition 2 and 3 of equation 4.1 can be replaced by an equality sign without any consequences.

# 4.3 Some Implications 

Corollary 1. The Bethe free energy for singly connected graphs is convex over the set of constraints.

Proof. The proof is by construction. Choose one of the leaf nodes as the root $\beta^{*}$ and define

$$
\begin{array}{ll}
A_{\alpha \beta}=1 & \text { iff } \beta \subset \alpha \text { and } \beta \text { closer to the root } \beta^{*} \text { than any other } \beta^{\prime} \subset \alpha \\
A_{\alpha \beta^{\prime}}=0 & \text { for all other } \beta^{\prime}
\end{array}
$$

Obviously, this choice of $A$ satisfies conditions 1 and 2 of equation 4.1. Arguing the other way around, for each $\beta \neq \beta^{*}$, there is just a single potential $\alpha \supset \beta$ that is closer to the root $\beta^{*}$ than $\beta$ itself (see the illustration in Figure 2) and thus there are precisely $n_{\beta}-1$ contributions $A_{\alpha \beta}=1$. The root itself gets $n_{\beta^{*}}$ contributions $A_{\alpha \beta^{*}}=1$, which is even better. Hence, condition 3 is also satisfied:

$$
\sum_{\alpha \supset \beta} A_{\alpha \beta}=n_{\beta}-1 \forall_{\beta \neq \beta^{*}} \text { and } \sum_{\alpha \supset \beta^{*}} A_{\alpha \beta^{*}}=n_{\beta^{*}}>n_{\beta^{*}}-1
$$

With the above construction of $A$, we are in a sense "eating up resources toward the root." At the root, we have one piece of resources left, which suggests that we can still enlarge the set of graphs for which convexity can be shown using theorem 1. This leads to the next corollary.

Corollary 2. The Bethe free energy for graphs with a single loop is convex over the set of constraints.

Proof. Again the proof is by construction. Break the loop at one particular place, that is, remove one node $\beta^{*}$ from a potential $\alpha^{*}$ such that a singly connected structure is left. Construct a matrix $A$ as in the proof of corollary 1 , taking the node $\beta^{*}$ as the root. The matrix $A$ constructed in this way also just works for the graph with the closed loop since still,

$$
\sum_{\alpha \supset \beta} A_{\alpha \beta}=n_{\beta}-1 \forall_{\beta \neq \beta^{*}} \text { and now } \sum_{\alpha \supset \beta^{*}} A_{\alpha \beta^{*}}=n_{\beta^{*}}-1
$$

It can be seen that this construction starts to fail as soon as we have two loops that are connected: with two connected loops, we have insufficient positive resources to compensate for the negative entropy contributions.
4.4 Connection with Other Work. The same corollaries can be found in Pakzad and Anantharam (2002) and McEliece and Yildirim (2003). Furthermore, the conditions in theorem 1 are very similar to the ones stated in Pakzad and Anantharam (2002), which for the Bethe free energy boil down to the following.

![img-1.jpeg](img-1.jpeg)
(a) Singly-connected structure.
![img-2.jpeg](img-2.jpeg)
(b) Single-loop structure.

Figure 2: The construction of an allocation matrix satisfying all convexity constraints for singly connected (a) and single-loop structures (b). Neglecting the arrows and dashes, each graph corresponds to a factor graph (Kscischang, Frey, \& Loeliger, 2001), where dark boxes refer to potentials and circles to nodes. The numbers within the circles give the corresponding "overcounting numbers," for the Bethe free energy $1-n_{\beta}$ with $n_{\beta}$ the number of neighboring potentials. The arrows, pointing from potentials $\alpha$ to nodes $\beta$, visualize the allocation matrix $A$ with $A_{\alpha \beta}=1$ if there is an arrow and $A_{\alpha \beta}=0$ otherwise. As can be seen, for each potential there is precisely one outgoing arrow, pointing at the node closest to the root, chosen to be the node in the upper right corner of the graph. In the singly-connected structure (a), all nonroot nodes have precisely $n_{\beta}-1$ incoming arrows, just sufficient to compensate the overcounting number $1-n_{\beta}$. The root node itself has one incoming arrow, which it does not really need. In the structure with the single loop (b), we open the loop by breaking the dashed link and construct the allocation matrix for the corresponding singly connected structure. This allocation matrix works for the single-loop structure as well, because now the incoming arrow at the "root" is just sufficient to compensate for the negative overcounting number resulting from the extra link closing the loop.

Theorem 2. (Adapted from theorem 1 in Pakzad \& Anantharam, 2002). The Bethe free energy is convex for the set of constraints if for any set of nodes $B$ we have

$$
\sum_{\beta \in B}\left(1-n_{\beta}\right)+\sum_{\alpha \in \pi(B)} 1 \geq 0
$$

where $\pi(B) \equiv\{\alpha: \exists \beta \in B ; \beta \subset \alpha\}$ denotes the "parent" set of $B$, that is, those potential subsets that include at least one node in $B$.

Proposition 1. The conditions in theorems 1 and 2 are equivalent.
Proof. Let us first suppose that there does exist an allocation matrix $A_{\alpha \beta}$ satisfying the conditions of equation 4.1. Then for any set $B$,

$$
\sum_{\beta \in B}\left(n_{\beta}-1\right) \leq \sum_{\beta \in B} \sum_{\alpha \supset \beta} A_{\alpha \beta} \leq \sum_{\alpha \in \pi(B)} \sum_{\beta \subset \alpha} A_{\alpha \beta} \leq \sum_{\alpha \in \pi(B)} 1
$$

where the inequalities follow from conditions 3,1 , and 2 in equation 4.1, respectively. In other words, validity of the conditions in theorem 1 implies the validity of those in theorem 2.

Next let us suppose that the conditions in Theorem 1 fail. Above, we have seen that this can happen if and only if the graph contains at least one connected component with two connected loops. But then condition 4.2 is violated as well when we take for $B$ the set of all nodes within such a component.

Since validity implies validity and violation implies violation, the conditions must be equivalent.

Graphical models with a single loop have been studied in detail in Weiss (2000), yielding important theoretical results (e.g., correctness of maximum a posteriori assignments). These results are derived by "unwrapping" the single loop into an infinite tree. This argument also breaks down as soon as there is more than a single loop. It might be interesting to find out whether there is a deeper connection between this unwrapping argument and the convexity of the Bethe free energy.

In summary, we have given conditions for the Bethe free energy to have a unique extremum satisfying the constraints. From the connection between the extrema of the Bethe free energy and fixed points of loopy belief propagation, it then follows that loopy belief propagation has a unique fixed point when these conditions are satisfied. These conditions fail as soon as the structure of the graph contains two connected loops.

The conditions for convexity of the Bethe free energy depend on the structure of the graph; the potentials $\Psi_{\alpha}\left(X_{\alpha}\right)$ do not play any role. These potentials appear only in the energy term that is linear in the pseudomarginals

and thus does not affect the convexity argument. Consequently, adding a "fake link" with potential $\Psi_{\alpha}\left(X_{\alpha}\right)=1$ can change the validity of the conditions, whereas it has no effect on the loopy belief propagation updates. Even if we managed to find more interesting (i.e., milder) conditions for convexity over the set of constraints, ${ }^{3}$ the impact of fake links would never disappear. In the following, we will therefore dig a little deeper to arrive at milder conditions that do take into account (the strength of) the potentials.

# 5 The Dual Formulation 

5.1 From Lagrangian to Dual. As we have seen, fixed points of loopy belief propagation are in a one-to-one correspondence with zero derivatives of the Lagrangian. If we manage to find conditions under which these zero derivatives have a unique solution, then for the same conditions, loopy belief propagation has a unique fixed point. In the following, we will work with a Lagrangian slightly different from equation 3.4. First, we substitute the constraint $Q_{\alpha}\left(x_{\beta}\right)=Q_{\beta}\left(x_{\beta}\right)$ to write the Bethe free energy in the "more convex" form,

$$
\begin{aligned}
F\left(Q_{\alpha}, Q_{\beta}\right)= & -\sum_{\alpha} \sum_{X_{\alpha}} Q_{\alpha}\left(X_{\alpha}\right) \psi_{\alpha}\left(X_{\alpha}\right)+\sum_{\alpha} \sum_{X_{\alpha}} Q_{\alpha}\left(X_{\alpha}\right) \log Q_{\alpha}\left(X_{\alpha}\right) \\
& -\sum_{\beta} \sum_{\alpha \supset \beta} A_{\alpha \beta} \sum_{x_{\beta}} Q_{\alpha}\left(x_{\beta}\right) \log Q_{\beta}\left(x_{\beta}\right)
\end{aligned}
$$

where the allocation matrix $A_{\alpha \beta}$ can be any matrix that satisfies

$$
\sum_{\alpha \supset \beta} A_{\alpha \beta}=n_{\beta}-1
$$

And second, we express the consistency constraints from equation 3.3 in terms of the potential pseudomarginals $Q_{\alpha}$ alone. This then yields

$$
\begin{aligned}
L\left(Q_{\alpha}, Q_{\beta}, \lambda_{\alpha \beta}, \lambda_{\alpha}\right)= & -\sum_{\alpha} \sum_{X_{\alpha}} Q_{\alpha}\left(X_{\alpha}\right) \psi_{\alpha}\left(X_{\alpha}\right) \\
& +\sum_{\alpha} \sum_{X_{\alpha}} Q_{\alpha}\left(X_{\alpha}\right) \log Q_{\alpha}\left(X_{\alpha}\right) \\
& -\sum_{\alpha} \sum_{\beta \subset \alpha} A_{\alpha \beta} \sum_{x_{\beta}} Q_{\alpha}\left(x_{\beta}\right) \log Q_{\beta}\left(x_{\beta}\right)
\end{aligned}
$$

[^0]
[^0]:    ${ }^{3}$ We would like to conjecture that this is not possible-that the conditions in theorem 1 are not only sufficient but also necessary to prove convexity of the Bethe free energy over the set of consistency constraints. Note that this would not imply that we need these conditions to guarantee the uniqueness of fixed points, since for that convexity by itself is sufficient, not necessary.

$$
\begin{aligned}
& +\sum_{\beta} \sum_{\alpha \supset \beta} \sum_{x_{\beta}} \lambda_{\alpha \beta}\left(x_{\beta}\right) \\
& \times\left[\frac{1}{n_{\beta}-1} \sum_{\alpha^{\prime} \supset \beta} A_{\alpha^{\prime} \beta} Q_{\alpha^{\prime}}\left(x_{\beta}\right)-Q_{\alpha}\left(x_{\beta}\right)\right] \\
& +\sum_{\alpha} \lambda_{\alpha}\left[1-\sum_{X_{\alpha}} Q_{\alpha}\left(X_{\alpha}\right)\right] \\
& +\sum_{\beta}\left(n_{\beta}-1\right)\left[\sum_{x_{\beta}} Q_{\beta}\left(x_{\beta}\right)-1\right]
\end{aligned}
$$

Note that the constraint $Q_{\beta}\left(x_{\beta}\right)=Q_{\alpha}\left(x_{\beta}\right)$ as well as its normalization is no longer incorporated with Lagrange multipliers, but follows when we take the minimum with respect to $Q_{\beta}$. It is easy to check that the fixed-point equations of loopy belief propagation still follow by setting the derivatives of the Lagrangian, equation 5.3 to zero.

Although the Bethe free energy and thus the Lagrangian, equation 5.3, may not be convex in $\left\{Q_{\alpha}, Q_{\beta}\right\}$, they are convex in $Q_{\alpha}$ and $Q_{\beta}$ separately. Therefore, we can interchange the minimum over the pseudomarginals $Q_{\alpha}$ and the maximum over the Lagrange multipliers, as long as we leave the minimum over $Q_{\beta}$ as the final operation: ${ }^{4}$

$$
\min _{Q_{\alpha}, Q_{\beta}} \max _{\lambda_{\alpha \beta}, \lambda_{\alpha}} L\left(Q_{\alpha}, Q_{\beta}, \lambda_{\alpha \beta}, \lambda_{\alpha}\right)=\min _{Q_{\beta}} \max _{\lambda_{\alpha \beta}, \lambda_{\alpha}} \min _{Q_{\alpha}} L\left(Q_{\alpha}, Q_{\beta}, \lambda_{\alpha \beta}, \lambda_{\alpha}\right) .
$$

Rewriting

$$
\begin{aligned}
& \sum_{\beta} \sum_{\alpha \supset \beta} \sum_{x_{\beta}} \lambda_{\alpha \beta}\left(x_{\beta}\right)\left[\frac{1}{n_{\beta}-1} \sum_{\alpha^{\prime} \supset \beta} A_{\alpha^{\prime} \beta} Q_{\alpha^{\prime}}\left(x_{\beta}\right)-Q_{\alpha}\left(x_{\beta}\right)\right] \\
& \quad=-\sum_{\alpha} \sum_{\beta \subset \alpha} \sum_{x_{\beta}} \bar{\lambda}_{\alpha \beta}\left(x_{\beta}\right) Q_{\alpha}\left(x_{\beta}\right)
\end{aligned}
$$

with

$$
\bar{\lambda}_{\alpha \beta}\left(x_{\beta}\right) \equiv \lambda_{\alpha \beta}\left(x_{\beta}\right)-\frac{1}{n_{\beta}-1} \sum_{\alpha^{\prime} \supset \beta} A_{\alpha^{\prime} \beta} \lambda_{\alpha^{\prime} \beta}\left(x_{\beta}\right)
$$

we can easily solve for the minimum with respect to $Q_{\alpha}$ :

$$
Q_{\alpha}^{*}\left(X_{\alpha}\right)=\Psi_{\alpha}\left(X_{\alpha}\right) \exp \left[\lambda_{\alpha}-1+\sum_{\beta \subset \alpha}\left\{A_{\alpha \beta} \log Q_{\beta}\left(x_{\beta}\right)+\bar{\lambda}_{\alpha \beta}\left(x_{\beta}\right)\right\}\right]
$$

[^0]
[^0]:    ${ }^{4}$ In principle, we could also first take the minimum over $Q_{\beta}$ and leave the minimum over $Q_{\alpha}$, but this does not seem to lead to any useful results.

Plugging this into the Lagrangian, we obtain the "dual,"

$$
\begin{aligned}
G\left(Q_{\beta}, \lambda_{\alpha \beta}, \lambda_{\alpha}\right) \equiv & L\left(Q_{\alpha}^{*}, Q_{\beta}, \lambda_{\alpha \beta}, \lambda_{\alpha}\right) \\
= & -\sum_{\alpha} \sum_{X_{\alpha}} \Psi_{\alpha}\left(X_{\alpha}\right) \\
& \exp \times\left[\lambda_{\alpha}-1+\sum_{\beta \subset \alpha}\left\{A_{\alpha \beta} \log Q_{\beta}\left(x_{\beta}\right)+\bar{\lambda}_{\alpha \beta}\left(x_{\beta}\right)\right\}\right] \\
& +\sum_{\alpha} \lambda_{\alpha}+\sum_{\beta}\left(n_{\beta}-1\right)\left[\sum_{x_{\beta}} Q_{\beta}\left(x_{\beta}\right)-1\right]
\end{aligned}
$$

Next, we find for the maximum with respect to $\lambda_{\alpha}$,

$$
\begin{aligned}
\exp \left[1-\lambda_{\alpha}^{*}\right] & =\sum_{X_{\alpha}} \Psi_{\alpha}\left(X_{\alpha}\right) \exp \left[\sum_{\beta \subset \alpha}\left\{A_{\alpha \beta} \log Q_{\beta}\left(x_{\beta}\right)+\bar{\lambda}_{\alpha \beta}\left(x_{\beta}\right)\right\}\right] \\
& \equiv Z_{\alpha}^{*}
\end{aligned}
$$

where we have to keep in mind that $Z_{\alpha}^{*}$ by itself, like $Q_{\alpha}^{*}$, is a function of the remaining pseudomarginals $Q_{\beta}$ and Lagrange multipliers $\lambda_{\alpha \beta}$. Substituting this solution into the dual, we arrive at

$$
\begin{aligned}
G\left(Q_{\beta}, \lambda_{\alpha \beta}\right) & \equiv G\left(Q_{\beta}, \lambda_{\alpha \beta}, \lambda_{\alpha}^{*}\right) \\
& =-\sum_{\alpha} \log Z_{\alpha}^{*}+\sum_{\beta}\left(n_{\beta}-1\right)\left[\sum_{x_{\beta}} Q_{\beta}\left(x_{\beta}\right)-1\right]
\end{aligned}
$$

Let us pause here for a moment and reflect on what we have done so far. The Lagrangian, equation 5.3, being convex in $Q_{\alpha}$, has a unique minimum in $Q_{\alpha}$ (given all other parameters fixed), which is also the only extremum. It happens to be relatively straightforward to express the value at this minimum in terms of the remaining parameters and then also to find the optimal (maximal) $\lambda_{\alpha}^{*}$. Plugging these values into the Lagrangian equation 5.3, we have not lost anything. That is, zero derivatives of the Lagrangian are still in one-to-one correspondence with zero derivatives of the dual, equation 5.7, and thus with fixed points of loopy belief propagation.
5.2 Recovering the Convexity Conditions (1). To find a minimum of the Bethe free energy satisfying the constraints in equation 3.3, we first have to take the maximum of the dual, equation 5.7, over the remaining Lagrange multipliers $\lambda_{\alpha \beta}$ and then the minimum over the remaining pseudomarginals $Q_{\beta}$. The duality theorem, a standard result from constrained optimization (see, Luenberger, 1984) tells us that the dual $G$ is concave in the Lagrange multipliers. The remaining question is then whether the dual is convex in

$Q_{\beta}$. If it is, we have a convex-concave minimax problem, which is guaranteed to have a unique solution.

Link c in Figure 1 follows from the following proposition.
Proposition 2. Convexity of the Bethe free energy, equation 5.1, in $\left\{Q_{\alpha}, Q_{\beta}\right\}$ implies convexity of the dual, equation 5.7, in $Q_{\beta}$.

Proof. First, we note that the minimum of a convex function over some of its parameters is convex in its remaining parameters. In obvious onedimensional notation, with $y^{*}(x) \equiv \underset{y}{\operatorname{argmin}} f(x, y)$,

$$
\begin{aligned}
f\left(x+\delta, y^{*}(x+\delta)\right)+f\left(x-\delta, y^{*}(x-\delta)\right) & \geq 2 f\left(x,\left(y^{*}(x+\delta)+y^{*}(x-\delta)\right) / 2\right) \\
& \geq 2 f\left(x, y^{*}(x)\right)
\end{aligned}
$$

where the first inequality follows from the convexity of $f$ in $\{x, y\}$ and the second inequality from $y^{*}(x)$ being the unique minimum of $f(x, y)$. Therefore, the dual, equation 5.5, is convex in $Q_{\beta}$ when the Lagrangian, equation 5.3, and thus the Bethe free energy, equation 5.1, is convex in $\left\{Q_{\alpha}, Q_{\beta}\right\}$. Furthermore, from the duality theorem, the dual, equation 5.5, is concave in the Lagrange multipliers $\left\{\lambda_{\alpha \beta}, \lambda_{\alpha}\right\}$. Next, we note that the maximum of a convex or concave function over its maximizing parameters is again convex: with $y^{*}(x) \equiv \underset{y}{\operatorname{argmax}} f(x, y)$,

$$
\begin{aligned}
f\left(x+\delta, y^{*}(x+\delta)\right)+f\left(x-\delta, y^{*}(x-\delta)\right) & \geq f\left(x+\delta, y^{*}(x)\right)+f\left(x-\delta, y^{*}(x)\right) \\
& \geq 2 f\left(x, y^{*}(x)\right)
\end{aligned}
$$

where the first inequality follows from $y^{*}(x \pm \delta)$ being the unique maximum of $f(x \pm \delta, y)$ and the second inequality from the convexity of $f(x, y)$ in $x$. Hence, the dual, equation 5.7, must still be convex in $Q_{\beta}$.

For now, we did not gain or lose anything in comparison with the conditions for theorem 1. However, the inequalities in the above proof suggest a little space that will lead to milder conditions for the uniqueness of fixed points.
5.3 Boundedness of the Bethe Free Energy. For completeness and to support link f in Figure 1, we will here prove that the Bethe free energy is bounded from below. The following theorem can be considered a special case of the one stated in Minka (2001) on the Bethe free energy for expectation propagation, a generalization of (loopy) belief propagation.

Theorem 3. If all potentials are bounded from above, that is, $\Psi_{\alpha}\left(X_{\alpha}\right) \leq \Psi_{\max }$ for all $\alpha$ and $X_{\alpha}$, the Bethe free energy is bounded from below on the set of constraints.

Proof. It is sufficient to prove that the function $G\left(Q_{\beta}\right) \equiv \max _{\lambda_{\alpha \beta}} G\left(Q_{\beta}, \lambda_{\alpha \beta}\right)$ is bounded from below for a particular choice of $A_{\alpha \beta}$ satisfying equation 5.2. Considering $A_{\alpha \beta}=\frac{n_{\beta}-1}{n_{\beta}}$, we then have

$$
\begin{aligned}
G\left(Q_{\beta}\right) \geq & -\sum_{\alpha} \log \sum_{X_{\alpha}} \Psi_{\alpha}\left(X_{\alpha}\right) \exp \left[\sum_{\beta \subset \alpha} \frac{n_{\beta}-1}{n_{\beta}} \log Q_{\beta}\left(x_{\beta}\right)\right] \\
& +\sum_{\beta}\left(n_{\beta}-1\right)\left[\sum_{x_{\beta}} Q_{\beta}\left(x_{\beta}\right)-1\right] \\
\geq & -\sum_{\alpha} \sum_{\beta \subset \alpha} \frac{n_{\beta}-1}{n_{\beta}} \log \sum_{X_{\alpha}} \Psi_{\alpha}\left(X_{\alpha}\right) Q_{\beta}\left(x_{\beta}\right) \\
& +\sum_{\beta}\left(n_{\beta}-1\right)\left[\sum_{x_{\beta}} Q_{\beta}\left(x_{\beta}\right)-1\right] \\
\geq & -\sum_{\alpha} \sum_{\beta \subset \alpha} \frac{n_{\beta}-1}{n_{\beta}} \log \left[\sum_{X_{\alpha \backslash \beta}} \Psi_{\max }\right] \\
& +\sum_{\beta}\left(n_{\beta}-1\right)\left[-\log \sum_{x_{\beta}} Q_{\beta}\left(x_{\beta}\right)+\sum_{x_{\beta}} Q_{\beta}\left(x_{\beta}\right)-1\right] \\
\geq & -\sum_{\alpha} \sum_{\beta \subset \alpha} \frac{n_{\beta}-1}{n_{\beta}} \log \left[\sum_{X_{\alpha \backslash \beta}} \Psi_{\max }\right]
\end{aligned}
$$

where the first inequality follows by substituting the choice $\lambda_{\alpha \beta}\left(x_{\beta}\right)=0$ for all $\alpha, \beta$, and $x_{\beta}$ in $G\left(Q_{\beta}, \lambda_{\alpha \beta}\right)$, the second from the concavity of the function $y^{\frac{n_{\beta}-1}{n_{\beta}}}$, and the third from the upper bound on the potentials.

# 6 Toward Better Conditions 

6.1 The Hessian. The next step is to compute the Hessian-the second derivative of the dual with respect to the pseudomarginals $Q_{\beta}$. The first derivative yields

$$
\frac{\partial G}{\partial Q_{\beta}\left(x_{\beta}\right)}=-\sum_{\alpha \supset \beta} A_{\alpha \beta} \frac{Q_{\alpha}^{*}\left(x_{\beta}\right)}{Q_{\beta}\left(x_{\beta}\right)}+\left(n_{\beta}-1\right)
$$

which is immediate from the Lagrangian, equation 5.3. To compute the matrix of second derivatives

$$
H_{\beta \beta^{\prime}}\left(x_{\beta}, x_{\beta^{\prime}}^{\prime}\right) \equiv \frac{\partial^{2} G}{\partial Q_{\beta}\left(x_{\beta}\right) \partial Q_{\beta^{\prime}}\left(x_{\beta^{\prime}}^{\prime}\right)}
$$

we make use of

$$
\frac{\partial Q_{\alpha}^{*}\left(x_{\beta}\right)}{\partial Q_{\beta^{\prime}}\left(x_{\beta^{\prime}}^{\prime}\right)}=A_{\alpha \beta^{\prime}} \frac{Q_{\alpha}^{*}\left(x_{\beta}, x_{\beta^{\prime}}^{\prime}\right)-Q_{\alpha}^{*}\left(x_{\beta}\right) Q_{\alpha}^{*}\left(x_{\beta^{\prime}}^{\prime}\right)}{Q_{\beta^{\prime}}\left(x_{\beta^{\prime}}^{\prime}\right)}
$$

where both $\beta$ and $\beta^{\prime}$ should be a subset of $\alpha$ and with convention $Q_{\alpha}^{*}\left(x_{\beta}, x_{\beta}\right)$ $=Q_{\alpha}^{*}\left(x_{\beta}\right)$ and $Q_{\alpha}^{*}\left(x_{\beta}, x_{\beta}^{\prime}\right)=0$ if $x_{\beta} \neq x_{\beta}^{\prime}$. Here, the first term follows from the differentation of equation 5.4 and the second term from the normalization as in equation 5.6. Distinguishing between $\beta=\beta^{\prime}$ and $\beta \neq \beta^{\prime}$, we then have

$$
\begin{aligned}
H_{\beta \beta}\left(x_{\beta}, x_{\beta}^{\prime}\right)= & \sum_{\alpha \supset \beta} A_{\alpha \beta}\left(1-A_{\alpha \beta}\right) \frac{Q_{\alpha}^{*}\left(x_{\beta}\right)}{Q_{\beta}^{2}\left(x_{\beta}\right)} \delta_{x_{\beta}, x_{\beta}^{\prime}} \\
& +\sum_{\alpha \supset \beta} A_{\alpha \beta}^{2} \frac{Q_{\alpha}^{*}\left(x_{\beta}\right) Q_{\alpha}^{*}\left(x_{\beta}^{\prime}\right)}{Q_{\beta}\left(x_{\beta}\right) Q_{\beta}\left(x_{\beta}^{\prime}\right)} \\
H_{\beta \beta^{\prime}}\left(x_{\beta}, x_{\beta^{\prime}}^{\prime}\right)= & -\sum_{\alpha \supset\left\{\beta, \beta^{\prime}\right\}} A_{\alpha \beta} A_{\alpha \beta^{\prime}} \frac{Q_{\alpha}^{*}\left(x_{\beta}, x_{\beta^{\prime}}^{\prime}\right)-Q_{\alpha}^{*}\left(x_{\beta}\right) Q_{\alpha}^{*}\left(x_{\beta^{\prime}}^{\prime}\right)}{Q_{\beta}\left(x_{\beta}\right) Q_{\beta^{\prime}}\left(x_{\beta^{\prime}}^{\prime}\right)} \\
& \text { for } \beta^{\prime} \neq \beta
\end{aligned}
$$

where $\delta_{x_{\beta}, x_{\beta}^{\prime}}=1$ if and only if $x_{\beta}=x_{\beta}^{\prime}$. Here, it should be noted that both $\beta$ and $x_{\beta}$ play the role of indices, that is, $x_{\beta}$ should not be mistaken for a variable or parameter. The parameters are still the (tables with) Lagrange multipliers $\lambda_{\alpha \beta}$ and pseudomarginals $Q_{\beta}$.

The goal is now to find conditions under which this Hessian is positive (semi) definite for any setting of the parameters $\left\{Q_{\beta}, \lambda_{\alpha \beta}\right\}$, that is, conditions that guarantee

$$
K \equiv \sum_{\beta, \beta^{\prime}} \sum_{x_{\beta}, x_{\beta^{\prime}}} S_{\beta}\left(x_{\beta}\right) H_{\beta \beta^{\prime}}\left(x_{\beta}, x_{\beta^{\prime}}\right) S_{\beta^{\prime}}\left(x_{\beta^{\prime}}\right) \geq 0
$$

for any choice of the "vector" $S$ with elements $S_{\beta}\left(x_{\beta}\right)$. Straightforward manipulations yield

$$
\begin{aligned}
\sum_{\beta, \beta^{\prime}} & \sum_{x_{\beta}, x_{\beta^{\prime}}} S_{\beta}\left(x_{\beta}\right) H_{\beta \beta^{\prime}}\left(x_{\beta}, x_{\beta^{\prime}}\right) S_{\beta^{\prime}}\left(x_{\beta^{\prime}}\right) \\
= & \sum_{\alpha} \sum_{\beta \subset \alpha} \sum_{x_{\beta}} A_{\alpha \beta}\left(1-A_{\alpha \beta}\right) Q_{\alpha}^{*}\left(x_{\beta}\right) R_{\beta}^{2}\left(x_{\beta}\right) \\
& +\sum_{\alpha} \sum_{\left\{\beta, \beta^{\prime}\right\} \subset \alpha} \sum_{x_{\beta}, x_{\beta^{\prime}}^{\prime}} A_{\alpha \beta} A_{\alpha \beta^{\prime}} Q_{\alpha}^{*}\left(x_{\beta}\right) Q_{\alpha}^{*}\left(x_{\beta^{\prime}}^{\prime}\right) R_{\beta}\left(x_{\beta}\right) R_{\beta^{\prime}}\left(x_{\beta^{\prime}}^{\prime}\right) \\
& -\sum_{\alpha} \sum_{\substack{\left\{\beta, \beta^{\prime}\right\} \subset \alpha \\ \beta^{\prime} \neq \beta}} \sum_{x_{\beta}, x_{\beta^{\prime}}^{\prime}} A_{\alpha \beta} A_{\alpha \beta^{\prime}} Q_{\alpha}^{*}\left(x_{\beta}, x_{\beta^{\prime}}^{\prime}\right) R_{\beta}\left(x_{\beta}\right) R_{\beta^{\prime}}\left(x_{\beta^{\prime}}^{\prime}\right)
\end{aligned}
$$

where $R_{\beta}\left(x_{\beta}\right) \equiv S_{\beta}\left(x_{\beta}\right) / Q_{\beta}\left(x_{\beta}\right)$.

6.2 Recovering the Convexity Conditions (2). Let us first see how we get back the conditions for convexity of the Bethe free energy, equation 5.1. Since

$$
K_{2}=\sum_{\alpha}\left[\sum_{\beta \subset \alpha} \sum_{x_{\beta}} A_{\alpha \beta} Q_{\alpha}^{*}\left(x_{\beta}\right) R_{\beta}\left(x_{\beta}\right)\right]^{2} \geq 0
$$

and $^{5}$

$$
\begin{aligned}
K_{3}= & \sum_{\alpha} \sum_{\substack{\left.\left|\beta, \beta^{\prime}\right| \subset \alpha \\
\beta^{\prime} \neq \beta} \\
& \sum_{x_{\beta}, x_{\beta^{\prime}}} A_{\alpha \beta} A_{\alpha \beta^{\prime}} Q_{\alpha}^{*}\left(x_{\beta}, x_{\beta^{\prime}}^{\prime}\right) \\
& \times\left\{\frac{1}{2}\left[R_{\beta}\left(x_{\beta}\right)-R_{\beta^{\prime}}\left(x_{\beta^{\prime}}^{\prime}\right)\right]^{2}-\frac{1}{2} R_{\beta}^{2}\left(x_{\beta}\right)-\frac{1}{2} R_{\beta^{\prime}}^{2}\left(x_{\beta^{\prime}}^{\prime}\right)\right\} \\
\geq & \sum_{\alpha} \sum_{\beta \subset \alpha} \sum_{x_{\beta}} A_{\alpha \beta}\left(\sum_{\beta^{\prime} \subset \alpha} A_{\alpha \beta^{\prime}}-A_{\alpha \beta}\right) Q_{\alpha}^{*}\left(x_{\beta}\right) R_{\beta}^{2}\left(x_{\beta}\right)
\end{aligned}
$$

we have

$$
K=K_{1}+K_{2}+K_{3} \geq \sum_{\alpha} \sum_{\beta \subset \alpha} \sum_{x_{\beta}} A_{\alpha \beta}\left(1-\sum_{\beta^{\prime} \subset \alpha} A_{\alpha \beta^{\prime}}\right) Q_{\alpha}^{*}\left(x_{\beta}\right) R_{\beta}^{2}\left(x_{\beta}\right)
$$

That is, sufficient conditions for $K$ to be nonnegative are

$$
A_{\alpha \beta} \geq 0 \quad \forall_{\alpha, \beta \subset \alpha} \text { and } \sum_{\beta \subset \alpha} A_{\alpha \beta} \leq 1 \quad \forall_{\alpha}
$$

precisely the conditions for theorem 1 .
6.3 Fake Interactions. While discussing the conditions for convexity of the Bethe free energy, we noticed that adding a "fake interaction," such as a constant potential, can change the validity of the conditions. We will see that here this is not the case and these fake interactions drop out as we would expect them to.

Suppose that we have a fake interaction $\Psi_{\alpha}\left(X_{\alpha}\right)=1$. From the solution, equation 5.4, it follows that the pseudomarginal $Q_{\alpha}^{*}\left(X_{\alpha}\right)$ factorizes: ${ }^{6}$

$$
Q_{\alpha}^{*}\left(x_{\beta}, x_{\beta^{\prime}}^{\prime}\right)=Q_{\alpha}^{*}\left(x_{\beta}\right) Q_{\alpha}^{*}\left(x_{\beta^{\prime}}^{\prime}\right) \quad \forall_{\left[\beta, \beta^{\prime}\right] \subset \alpha}
$$

[^0]
[^0]:    ${ }^{5}$ This step is in fact equivalent to the Gerschgorin theorem for bounding the eigenvalues of a matrix.
    ${ }^{6}$ The exact marginal $P_{\text {exact }}\left(X_{\alpha}\right)$ need not factorize. This is really a consequence of the locality assumptions behind loopy belief propagation and the Bethe free energy.

Consequently, the terms involving $\alpha$ in $K_{3}$ cancel with those in $K_{2}$, which is most easily seen when we combine $K_{2}$ and $K_{3}$ in a different way:

$$
\begin{aligned}
K_{2}+K_{3}= & \sum_{\alpha} \sum_{\beta \subset \alpha} \sum_{x_{\beta}, x_{\beta^{\prime}}^{\prime}} A_{\alpha \beta}^{2} Q_{\alpha}^{*}\left(x_{\beta}\right) Q_{\alpha}^{*}\left(x_{\beta}^{\prime}\right) R_{\beta}\left(x_{\beta}\right) R_{\beta}\left(x_{\beta}^{\prime}\right) \\
& -\sum_{\alpha} \sum_{\substack{\left.\left(\beta^{\prime}\right)^{\prime}\right) \subset \alpha \\
\beta^{\prime} \neq \beta}} \sum_{x_{\beta}, x_{\beta^{\prime}}^{\prime}} A_{\alpha \beta} A_{\alpha \beta^{\prime}} \\
& \times\left[Q_{\alpha}^{*}\left(x_{\beta}, x_{\beta^{\prime}}^{\prime}\right)-Q_{\alpha}^{*}\left(x_{\beta}\right) Q_{\alpha}^{*}\left(x_{\beta^{\prime}}^{\prime}\right)\right] R_{\beta}\left(x_{\beta}\right) R_{\beta^{\prime}}\left(x_{\beta^{\prime}}^{\prime}\right)
\end{aligned}
$$

This leaves us with the weaker requirement (from $K_{1}$ ) $A_{\alpha \beta}\left(1-A_{\alpha \beta}\right) \geq 0$ for all $\beta \subset \alpha$. The best choice is then to take $A_{\alpha \beta}=1$, which turns condition 3 of equation 4.1 into

$$
\sum_{\substack{\alpha^{\prime} \supset \beta \\ \alpha^{\prime} \neq \alpha}} A_{\alpha^{\prime} \beta}+1 \geq n_{\beta}-1
$$

The net effect is equivalent to ignoring the interaction, reducing the number of neighboring potentials $n_{\beta}$ by 1 for all $\beta$ that are part of the fake interaction $\alpha$.

We have seen how we get milder and thus better conditions when there is effectively no interaction. Motivated by this "success," we will work toward conditions that take into account the strength of the interactions. Our starting point will be the above decomposition in $\tilde{K}_{2}$ and $\tilde{K}_{3}$ where, since $\tilde{K}_{2} \geq 0$, we will concentrate on $\tilde{K}_{3}$.

# 7 The Strength of a Potential 

7.1 Bounding the Correlations. The crucial observation, which will allow us to obtain milder and thus better conditions for the uniqueness of a fixed point, is the following lemma. It bounds the term between brackets in $\tilde{K}_{3}$ such that we can again combine this bound with the (positive) term $K_{1}$. However, before we get to that, we take some time to introduce and derive properties of the "strength" of a potential.

Lemma 2. Two-node correlations of loopy belief marginals obey the bound

$$
Q_{\alpha}^{*}\left(x_{\beta}, x_{\beta^{\prime}}^{\prime}\right)-Q_{\alpha}^{*}\left(x_{\beta}\right) Q_{\alpha}^{*}\left(x_{\beta^{\prime}}^{\prime}\right) \leq \sigma_{\alpha} Q_{\alpha}^{*}\left(x_{\beta}, x_{\beta^{\prime}}^{\prime}\right) \quad \forall_{\substack{\left.\left(\beta, \beta^{\prime}\right) \subset \alpha \\ \beta^{\prime} \neq \beta}} \forall_{x_{\beta}, x_{\beta^{\prime}}^{\prime}}
$$

with the "strength" $\sigma_{\alpha}$ a function of the potential $\psi_{\alpha}\left(X_{\alpha}\right) \equiv \log \Psi_{\alpha}\left(X_{\alpha}\right)$ only:

$$
\begin{aligned}
\sigma_{\alpha} & =1-\exp \left(-\omega_{\alpha}\right) \text { with } \\
\omega_{\alpha} & \equiv \max _{X_{\alpha}, \hat{X}_{\alpha}}\left[\psi_{\alpha}\left(X_{\alpha}\right)+\left(n_{\alpha}-1\right) \psi_{\alpha}\left(\hat{X}_{\alpha}\right)-\sum_{\beta \subset \alpha} \psi_{\alpha}\left(\hat{X}_{\alpha \backslash \beta}, x_{\beta}\right)\right]
\end{aligned}
$$

where $n_{\alpha} \equiv \sum_{\beta \subset \alpha} 1$.

Proof. For convenience and without loss of generality, we omit $\alpha$ from our notation and renumber the nodes that are contained in $\alpha$ from 1 to $n$. We consider the quotient between the loopy belief on the potential subset divided by the product of its single-node marginals:

$$
\begin{aligned}
\frac{Q^{*}(X)}{\prod_{\beta=1}^{n} Q^{*}\left(x_{\beta}\right)} & =\frac{\Psi(X) \prod_{\beta} \mu_{\beta}\left(x_{\beta}\right)\left[\sum_{X^{\prime}} \Psi\left(X^{\prime}\right) \prod_{\beta} \mu_{\beta}\left(x_{\beta}^{\prime}\right)\right]^{n-1}}{\prod_{\beta}\left[\sum_{X_{\backslash \beta}^{\prime}} \Psi\left(X_{\backslash \beta}^{\prime}, x_{\beta}\right) \prod_{\beta^{\prime} \neq \beta} \mu_{\beta^{\prime}}\left(x_{\beta^{\prime}}^{\prime}\right) \mu_{\beta}\left(x_{\beta}\right)\right]} \\
& =\frac{\Psi(X)\left[\sum_{X^{\prime}} \Psi\left(X^{\prime}\right) \prod_{\beta} \mu_{\beta}\left(x_{\beta}^{\prime}\right)\right]^{n-1}}{\prod_{\beta}\left[\sum_{X_{\backslash \beta}^{\prime}} \Psi\left(X_{\backslash \beta}^{\prime}, x_{\beta}\right) \prod_{\beta^{\prime} \neq \beta} \mu_{\beta^{\prime}}\left(x_{\beta^{\prime}}^{\prime}\right)\right]}
\end{aligned}
$$

where we substituted the properly normalized version of equation 3.5: a loopy belief pseudomarginal is proportional to the potential times incoming messages. The goal is now to find the maximum of the above expression over all possible messages and all values of $X$. Especially the maximum over messages $\mu$ seems to be difficult to compute, but the following intermediate lemma helps us out.

Lemma 3. The maximum of the function

$$
\begin{aligned}
V(\mu)= & (n-1) \log \left[\sum_{X} \Psi(X) \prod_{\beta=1}^{n} \mu_{\beta}\left(x_{\beta}\right)\right] \\
& -\sum_{\beta=1}^{n} \log \left[\sum_{X_{\backslash \beta}} \Psi\left(X_{\backslash \beta}, x_{\beta}^{*}\right) \prod_{\beta^{\prime} \neq \beta} \mu_{\beta^{\prime}}\left(x_{\beta^{\prime}}\right)\right]
\end{aligned}
$$

with respect to the messages $\mu$ under constraints $\sum_{x_{\beta}} \mu_{\beta}\left(x_{\beta}\right)=1$ for all $\beta$ and $\mu_{\beta}\left(x_{\beta}\right) \geq 0$ for all $\beta$ and $x_{\beta}$, occurs at an extreme point $\mu_{\beta}\left(x_{\beta}\right)=\delta_{x_{\beta}, \hat{x}_{\beta}}$ for some $\hat{x}_{\beta}$ to be found.

Proof. Let us consider optimizing the message $\mu_{1}\left(x_{1}\right)$ with fixed messages $\mu_{\beta}\left(x_{\beta}\right)$ for $\beta>1$. The first and second derivatives are easily found to obey

$$
\begin{aligned}
\frac{\partial V}{\partial \mu_{1}\left(x_{1}\right)} & =(n-1) Q\left(x_{1}\right)-\sum_{\beta \neq 1} Q\left(x_{1} \mid x_{\beta}^{*}\right) \\
\frac{\partial^{2} V}{\partial \mu_{1}\left(x_{1}\right) \partial \mu_{1}\left(x_{1}^{\prime}\right)} & =(n-1) Q\left(x_{1}\right) Q\left(x_{1}^{\prime}\right)-\sum_{\beta \neq 1} Q\left(x_{1} \mid x_{\beta}^{*}\right) Q\left(x_{1}^{\prime} \mid x_{\beta}^{*}\right)
\end{aligned}
$$

where

$$
Q(X) \equiv \frac{\Psi(X) \prod_{\beta} \mu_{\beta}\left(x_{\beta}\right)}{\sum_{X^{\prime}} \Psi\left(X^{\prime}\right) \prod_{\beta} \mu_{\beta}\left(x_{\beta}^{\prime}\right)}
$$

Now suppose that $V$ has a regular extremum (maximum or minimum) not at an extreme point, that is, $\mu_{1}\left(x_{1}\right)>0$ for two or more values of $x_{1}$. At such an extremum, the first derivative should obey

$$
(n-1) Q\left(x_{1}\right)-\sum_{\beta \neq 1} Q\left(x_{1} \mid x_{\beta}^{*}\right)=\lambda
$$

with $\lambda$ a Lagrange multiplier implementing the constraint $\sum_{x_{1}} \mu_{1}\left(x_{1}\right)=1$. Summing over $x_{1}$, we obtain $\lambda=0$ (in fact, $V$ is indifferent to any multiplicative scaling of $\mu$ ). For the matrix with second derivatives at such an extremum, we then have

$$
\frac{\partial^{2} V}{\partial \mu_{1}\left(x_{1}\right) \partial \mu_{1}\left(x_{1}^{\prime}\right)}=\sum_{\beta \neq 1} \sum_{\substack{\beta^{\prime} \neq 1 \\ \beta^{\prime} \neq \beta}} Q\left(x_{1} \mid x_{\beta}^{*}\right) Q\left(x_{1}^{\prime} \mid x_{\beta}^{*}\right)
$$

which is positive semidefinite: the extremum cannot be a maximum. Consequently, any maximum must be at the boundary of the domain. Since this holds for any choice of $\mu_{\beta}\left(x_{\beta}\right), \beta>1$, it follows by induction that the maximum with respect to all $\mu_{\beta}\left(x_{\beta}\right)$ must be at an extreme point as well.

The function $V(\mu)$ is, up to a term independent of $\mu$, the logarithm of equation 7.3. So the intermediate lemma 3 tells us that we can replace the maximization over messages $\mu$ by maximization over values $\hat{X}$ :

$$
\max _{\mu} \frac{Q^{*}(X)}{\prod_{\beta} Q^{*}\left(x_{\beta}\right)}=\max _{\hat{X}} \frac{\Psi(X)[\Psi(\hat{X})]^{n-1}}{\prod_{\beta} \Psi\left(\hat{X}_{\backslash \beta}, x_{\beta}\right)}
$$

Next, we take the maximum over $X$ as well and define the "strength" $\sigma$ to be used in equation 7.1 through

$$
\frac{1}{1-\sigma} \equiv \max _{X, \mu} \frac{Q^{*}(X)}{\prod_{\beta} Q^{*}\left(x_{\beta}\right)}=\max _{X, \hat{X}} \frac{\Psi(X)[\Psi(\hat{X})]^{n-1}}{\prod_{\beta} \Psi\left(\hat{X}_{\backslash \beta}, x_{\beta}\right)}
$$

The inequality 7.1 then follows by summing out $X_{\backslash\left[\beta, \beta^{\prime}\right]}$ in

$$
Q^{*}(X)-\prod_{\beta} Q^{*}\left(x_{\beta}\right) \leq \sigma Q^{*}(X)
$$

The form of equation 7.2 then follows by rewriting equation 7.4 as

$$
\begin{aligned}
\omega & \equiv-\log (1-\sigma)=\max _{X, \hat{X}} W(X ; \hat{X}) \text { with } \\
W(X ; \hat{X}) & =\left[\psi(X)+(n-1) \psi(\hat{X})-\sum_{\beta} \psi\left(\hat{X}_{\backslash \beta}, x_{\beta}\right)\right]
\end{aligned}
$$

where we recall that $\psi(X) \equiv \log \Psi(X)$.
7.2 Some Properties. In the following we will refer to both $\omega$ and $\sigma$ as the strength of the potential. There are several properties worth noting:

- The strength of a potential is indifferent to multiplication with any term that factorizes over the nodes, that is,

$$
\text { if } \tilde{\Psi}(X)=\Psi(X) \prod_{\beta} \mu_{\beta}\left(x_{\beta}\right) \text { then } \omega(\tilde{\Psi})=\omega(\Psi) \text { for any choice of } \mu
$$

This property relates to the arbitrariness in the definition of equation 3.1: if two potentials overlap, then multiplying one potential with a term that only depends on the overlap and dividing the other by the same term does not change the distribution. Luckily, it also does not change the strength of those potentials.

- To compute the strength, we can enumerate all possible combinations. However, we can neglect all combinations $X$ and $\hat{X}$ that differ in fewer than two nodes. To see this, consider

$$
\begin{aligned}
W\left(x_{1}, x_{2}, x_{\backslash 1 \backslash 2} ; \hat{x}_{1}, \hat{x}_{2}, x_{\backslash 1 \backslash 2}\right)= & \psi\left(x_{1}, x_{2}, x_{\backslash 1 \backslash 2}\right)+\psi\left(\hat{x}_{1}, \hat{x}_{2}, x_{\backslash 1 \backslash 2}\right) \\
& -\psi\left(\hat{x}_{1}, x_{2}, x_{\backslash 1 \backslash 2}\right)-\psi\left(x_{1}, \hat{x}_{2}, x_{\backslash 1 \backslash 2}\right) \\
= & -W\left(x_{1}, \hat{x}_{2}, x_{\backslash 1 \backslash 2} ; \hat{x}_{1}, x_{2}, x_{\backslash 1 \backslash 2}\right)
\end{aligned}
$$

If now also $\hat{x}_{2}=x_{2}$, we get $W\left(x_{1}, x_{\backslash 1} ; \hat{x}_{1}, x_{\backslash 1}\right)=-W\left(x_{1}, x_{\backslash 1} ; \hat{x}_{1}, x_{\backslash 1}\right)=$ 0 . Furthermore, if $W\left(x_{1}, x_{2}, x_{\backslash 1 \backslash 2} ; \hat{x}_{1}, \hat{x}_{2}, x_{\backslash 1 \backslash 2}\right) \leq 0$, then it must be that $W\left(x_{1}, \hat{x}_{2}, x_{\backslash 1 \backslash 2} ; \hat{x}_{1}, x_{2}, x_{\backslash 1 \backslash 2}\right) \geq 0$ and vice versa. So $\omega$, the maximum over all combinations, must be nonnegative, and we can indeed neglect all combinations that by definition yield zero.

- Thus, for finite potentials, $0 \leq \omega<\infty$ and $0 \leq \sigma<1$.

- With pairwise potentials, the above symmetries can be used to reduce the number of evaluations to $\left|x_{1}\right|\left|x_{2}\right|\left(\left|x_{1}\right|-1\right)\left(\left|x_{2}\right|-1\right) / 4$ combinations. And indeed, for binary nodes $x_{1,2} \in\{0,1\}$, we immediately obtain

$$
\omega=|\psi(0,0)+\psi(1,1)-\psi(0,1)-\psi(1,0)|
$$

Any pairwise binary potential can be written as a Boltzmann factor:

$$
\Psi\left(x_{1}, x_{2}\right) \propto \exp \left[w x_{1} x_{2}+\theta_{1} x_{1}+\theta_{2} x_{2}\right]
$$

In this notation, we find the simple and intuitive expression $\omega=|w|$ : the strength is the absolute value of the "weight." It is indeed independent of (the size of) the thresholds. In the case of $\{-1,1\}$, coding the relationship is $\omega=4|w|$.

- In some models, there is the notion of a "temperature" $T$, that is, $\Psi(X) \propto$ $\exp [\tilde{\psi}(X) / T]$ where $\tilde{\psi}(X)$ is considered constant. In obvious notation, we then have $\omega(T)=\omega(1) / T$ and thus $\sigma(T)=1-\exp [-\omega(1) / T]=$ $1-[1 /(1-\sigma(1))]^{1 / T}$.
- Loopy belief revision (max-product) can be interpreted as a zerotemperature limit of loopy belief propagation (sum product). More specifically, we get the belief revision updates if we imagine running loopy belief propagation on potentials that are scaled with temperature $T$ and then take the limit $T$ to zero. Consequently, when analyzing conditions for uniqueness of loopy belief revision fixed points, we can take $\sigma(0)=0$ if $\sigma(1)=0$ (fake interaction), yet $\sigma(0)=1$ whenever $\sigma(1)>0$.


# 8 Conditions for Uniqueness 

### 8.1 Main Result.

Theorem 4. Loopy belief propagation has a unique fixed point if there exists an allocation matrix $A_{\alpha \beta}$ between potentials $\alpha$ and nodes $\beta$ with properties

1. $A_{\alpha \beta} \geq 0 \quad \forall_{\alpha, \beta \subset \alpha}$
(positivity)
2. $\left(1-\sigma_{\alpha}\right) \max _{\beta \subset \alpha} A_{\alpha \beta}+\sigma_{\alpha} \sum_{\beta \subset \alpha} A_{\alpha \beta} \leq 1 \quad \forall_{\alpha} \quad$ (sufficient amount of resources)
3. $\sum_{\alpha \supset \beta} A_{\alpha \beta} \geq n_{\beta}-1 \quad \forall_{\beta}$
(sufficient compensation)
with the strength $\sigma_{\alpha}$ a function of the potential $\Psi_{\alpha}\left(X_{\alpha}\right)$ as defined in equation 7.2.

Proof. For completeness, we first summarize our line of reasoning. Fixed points of loopy belief propagation are in one-to-one correspondence with

extrema of the dual, equation 5.5. This dual has a unique extremum if it is convex/concave. Concavity is guaranteed, so we focus on conditions for convexity, that is, for positive (semi)definiteness of the corresponding Hessian. This then boils down to conditions that ensure $K=K_{1}+\tilde{K}_{2}+\tilde{K}_{3} \geq 0$ for any choice of $R_{\beta}\left(x_{\beta}\right)$.

Substituting the bound, equation 7.1, into the term $\tilde{K}_{3}$, we obtain

$$
\begin{aligned}
\tilde{K}_{3} & \geq-\sum_{\alpha} \sum_{\substack{\left.\beta, \beta^{\prime}\right) \subset \alpha \\
\beta^{\prime} \neq \beta}} \sum_{x_{\beta}, x_{\beta^{\prime}}^{\prime}} A_{\alpha \beta} A_{\alpha \beta^{\prime}} \sigma_{\alpha} \mathrm{Q}_{\alpha}^{*}\left(x_{\beta}, x_{\beta^{\prime}}^{\prime}\right) R_{\beta}\left(x_{\beta}\right) R_{\beta^{\prime}}\left(x_{\beta^{\prime}}^{\prime}\right) \\
& \geq-\sum_{\alpha} \sigma_{\alpha} \sum_{\beta \subset \alpha} \sum_{x_{\beta}} A_{\alpha \beta} \sum_{\substack{\beta^{\prime} \subset \alpha \\
\beta^{\prime} \neq \beta}} A_{\alpha \beta^{\prime}} Q_{\alpha}^{*}\left(x_{\beta}\right) R_{\beta}^{2}\left(x_{\beta}\right)
\end{aligned}
$$

where in the last step, we applied the same trick as in equation 6.1. Since $\tilde{K}_{2} \geq 0$ and combining $K_{1}$ and (the above lower bound on) $\tilde{K}_{3}$, we get

$$
\begin{aligned}
K & =K_{1}+\tilde{K}_{2}+\tilde{K}_{3} \\
& \geq \sum_{\alpha} \sum_{\beta \subset \alpha} \sum_{x_{\beta}} A_{\alpha \beta}\left[1-A_{\alpha \beta}-\sigma_{\alpha} \sum_{\beta^{\prime} \neq \beta} A_{\alpha \beta^{\prime}}\right] Q_{\alpha}^{*}\left(x_{\beta}\right) R_{\beta}^{2}\left(x_{\beta}\right)
\end{aligned}
$$

This implies

$$
\left(1-\sigma_{\alpha}\right) A_{\alpha \beta}+\sigma_{\alpha} \sum_{\beta^{\prime} \subset \alpha} A_{\alpha \beta^{\prime}} \leq 1 \quad \forall_{\alpha, \beta \subset \alpha}
$$

which, in combination with $A_{\alpha \beta} \geq 0$ and $\sigma_{\alpha} \leq 1$, yields condition 2 in equation 8.1. The equality constraint, equation 5.2, that we started with can be relaxed to the inequality condition 3 without any consequences.

We get back the stricter conditions of theorem 1 if $\sigma_{\alpha}=1$ for all potentials $\alpha$. Furthermore, "fake interactions" play no role: with $\sigma_{\alpha}=0$, condition 2 becomes $\max _{\beta \subset \alpha} A_{\alpha \beta} \leq 1$, suggesting the choice $A_{\alpha \beta}=1$ for all $\beta \subset \alpha$, which then effectively reduces the number of neighboring potentials $n_{\beta}$ in condition 3 .
8.2 Comparison with Other Work. To the best of our knowledge, the only conditions for uniqueness of loopy belief propagation fixed points that depend on more than just the structure of the graph are those in Tatikonda and Jordan (2002) for pairwise potentials. The analysis in Tatikonda and Jordan is based on the concept of the computation tree, which represents an unwrapping of the original graph with respect to the loopy belief propagation algorithm. The same concept is used in Weiss (2000) to show that belief revision yields the correct maximum a posteriori assignments in graphs

with a single loop and Weiss and Freeman (2001) to prove that loopy belief propagation in gaussian graphical models yields exact means. Although the current theorems based on the concept of computation trees are derived for pairwise potentials, it should be possible to extend them to more general factor graphs.

The setup in Tatikonda and Jordan (2002) is slightly different; it is based on the factorization

$$
P_{\text {exact }}(X)=\frac{1}{Z} \prod_{\alpha} \hat{\Psi}_{\alpha}\left(X_{\alpha}\right) \prod_{\beta} \hat{\Psi}_{\beta}\left(x_{\beta}\right)
$$

to be compared with our equation 3.1, where there are no self-potentials $\Psi_{\beta}\left(x_{\beta}\right)$. With this in mind, the statement is then as follows.

Theorem 5. (adapted from Tatikonda $\mathcal{E}$ Jordan, 2002, in particular proposition 5.3). Loopy belief propagation on pairwise potentials has a unique fixed point if

$$
\sum_{\alpha \supset \beta}\left(\max _{X_{\alpha}} \hat{\psi}_{\alpha}\left(X_{\alpha}\right)-\min _{X_{\alpha}} \hat{\psi}_{\alpha}\left(X_{\alpha}\right)\right)<2 \forall_{\beta}
$$

To make the connection between theorem 5 and theorem 4, we will first strengthen the former and then weaken the latter. We will focus on the case of binary pairwise potentials. Since the definition of self-potentials is arbitrary and the condition 8.2 is valid for any choice, we can easily improve the condition by optimizing this choice. This then leads to the following corollary.

Corollary 3. This corollary concerns an improvement of theorem 5 for pairwise binary potentials. Loopy belief propagation on pairwise binary potentials has a unique fixed point if

$$
\sum_{\alpha \supset \beta} \omega_{\alpha}<4 \quad \forall_{\beta}
$$

with $\omega_{\alpha}$ defined in equation 7.2 .
Proof. The condition 8.2 applies to any arbitrary definition of self-potentials $\hat{\Psi}_{\beta}\left(x_{\beta}\right)$. In fact, it is valid for any choice

$$
\hat{\psi}_{\alpha}\left(X_{\alpha}\right)=\psi_{\alpha}\left(X_{\alpha}\right)+\sum_{\beta \subset \alpha} \phi_{\alpha \beta}\left(x_{\beta}\right)
$$

where $\psi_{\alpha}\left(X_{\alpha}\right)$ is any choice of potential subsets that fits in our framework of no self-potentials (as argued above, there is some arbitrariness here as

well). We can then optimize this choice to obtain milder, and thus better, conditions. Omitting $\alpha$ and renumbering the nodes from 1 to 2 , we have

$$
\begin{aligned}
& \min _{\phi_{1}, \phi_{2}}\left\{\max _{x_{1}, x_{2}} \hat{\psi}\left(x_{1}, x_{2}\right)-\min _{x_{1}, x_{2}} \hat{\psi}\left(x_{1}, x_{2}\right)\right\} \\
& =\min _{\phi_{1}, \phi_{2}}\left\{\max _{x_{1}, x_{2}}\left[\psi\left(x_{1}, x_{2}\right)+\phi_{1}\left(x_{1}\right)+\phi_{2}\left(x_{2}\right)\right]\right. \\
& \left.\quad-\min _{x_{1}, x_{2}}\left[\psi\left(x_{1}, x_{2}\right)+\phi_{1}\left(x_{1}\right)+\phi_{2}\left(x_{2}\right)\right]\right\}
\end{aligned}
$$

In the case of binary nodes (two-by-two matrices $\psi\left(x_{1}, x_{2}\right)$ ), it is easy to check that the optimal $\phi_{1}$ and $\phi_{2}$ that yield the smallest gap are such that

$$
\begin{aligned}
& \psi\left(x_{1}, x_{2}\right)+\phi_{1}\left(x_{1}\right)+\phi_{2}\left(x_{2}\right)=\psi\left(\hat{x}_{1}, \hat{x}_{2}\right)+\phi_{1}\left(\hat{x}_{1}\right)+\phi_{2}\left(\hat{x}_{2}\right) \\
& \quad \geq \psi\left(x_{1}, \hat{x}_{2}\right)+\phi_{1}\left(x_{1}\right)+\phi_{2}\left(\hat{x}_{2}\right)=\psi\left(\hat{x}_{1}, x_{2}\right)+\phi_{1}\left(\hat{x}_{1}\right)+\phi_{2}\left(x_{2}\right)
\end{aligned}
$$

for some $x_{1}, x_{2}, \hat{x}_{1}$, and $\hat{x}_{2}$ with $x_{1} \neq \hat{x}_{1}$ and $x_{2} \neq \hat{x}_{2}$. Solving for $\phi_{1}$ and $\phi_{2}$, we find

$$
\begin{aligned}
& \phi_{1}\left(x_{1}\right)-\phi_{1}\left(\hat{x}_{1}\right)=\frac{1}{2}\left[\psi\left(\hat{x}_{1}, x_{2}\right)-\psi\left(x_{1}, \hat{x}_{2}\right)+\psi\left(\hat{x}_{1}, \hat{x}_{2}\right)-\psi\left(x_{1}, x_{2}\right)\right] \\
& \phi_{2}\left(x_{2}\right)-\phi_{2}\left(\hat{x}_{2}\right)=\frac{1}{2}\left[\psi\left(x_{1}, \hat{x}_{2}\right)-\psi\left(\hat{x}_{1}, \hat{x}_{2}\right)+\psi\left(\hat{x}_{1}, \hat{x}_{2}\right)-\psi\left(x_{1}, x_{2}\right)\right]
\end{aligned}
$$

Substitution back into equation 8.4 yields

$$
\begin{aligned}
& \psi\left(x_{1}, x_{2}\right)+\phi_{1}\left(x_{1}\right)+\phi_{2}\left(x_{2}\right)-\psi\left(x_{1}, \hat{x}_{2}\right)-\phi_{1}\left(x_{1}\right)-\phi_{2}\left(\hat{x}_{2}\right) \\
& \quad=\frac{1}{2}\left[\psi\left(x_{1}, x_{2}\right)+\psi\left(\hat{x}_{1}, \hat{x}_{2}\right)-\psi\left(\hat{x}_{1}, x_{2}\right)-\psi\left(x_{1}, \hat{x}_{2}\right)\right]
\end{aligned}
$$

which has to be nonnegative. Of all four possible combinations, two of them are valid and yield the same positive gap, and the other two are invalid since they yield the same negative gap. Enumerating these combinations, we find

$$
\begin{aligned}
& \min _{\phi_{1}, \phi_{2}}\left\{\max _{x_{1}, x_{2}} \hat{\psi}\left(x_{1}, x_{2}\right)-\min _{x_{1}, x_{2}} \hat{\psi}\left(x_{1}, x_{2}\right)\right\} \\
& \quad=\frac{1}{2}|\psi(0,0)+\psi(1,1)-\psi(0,1)-\psi(1,0)|=\frac{\omega}{2}
\end{aligned}
$$

from equation 7.5. Substitution into the condition 8.2 then yields equation 8.3.

Next we derive the following weaker corollary of theorem 4:

Corollary 4. This is a weaker version of theorem 4 for pairwise potentials. Loopy belief propagation on pairwise potentials has a unique fixed point if

$$
\sum_{\alpha \supset \beta} \omega_{\alpha} \leq 1 \quad \forall_{\beta}
$$

with $\omega_{\alpha}$ defined in equation 7.2 .

Proof. Consider the allocation matrix with components $A_{\alpha \beta}=1-\sigma_{\alpha}$ for all $\beta \subset \alpha$. With this choice, conditions 1 and 2 of equation 8.1 are fulfilled, since (condition 1) $\sigma_{\alpha} \leq 1$ and (condition 2)

$$
\left(1-\sigma_{\alpha}\right)\left(1-\sigma_{\alpha}\right)+2 \sigma_{\alpha}\left(1-\sigma_{\alpha}\right)=1-2 \sigma_{\alpha}^{2} \leq 1
$$

Substitution into condition 3 yields

$$
\sum_{\alpha \supset \beta}\left(1-\sigma_{\alpha}\right) \geq \sum_{\alpha \supset \beta} 1-1 \text { and thus } \sum_{\alpha \supset \beta} \sigma_{\alpha} \leq 1
$$

Since $\omega_{\alpha}=-\log \left(1-\sigma_{\alpha}\right) \geq \sigma_{\alpha}$, condition 8.5 is weaker than condition 8.6.

Summarizing, the conditions in Tatikonda and Jordan (2002) are, for binary pairwise potentials and when strengthened as above, at most a constant (factor 4) less strict and thus better than the ones derived here. The latter are better when the structure is (close to) a tree. The best set of conditions follows by taking the union of both. Note further that the conditions derived in Tatikonda and Jordan (2002) are, unlike theorem 4, specific to pairwise potentials.
8.3 Illustration. For illustration we consider a $3 \times 3$ Ising grid with toroidal boundary conditions as in Figure 3a and uniform ferromagnetic potentials proportional to

$$
\left(\begin{array}{cc}
\alpha & 1-\alpha \\
1-\alpha & \alpha
\end{array}\right)
$$

The trivial solution, which is the only minimum of the Bethe free energy for small $\alpha$, is the one with all pseudomarginals equal to $(0.5,0.5)$. With simple algebra, for example, following the line of reasoning that leads to the belief optimization algorithm in Welling and Teh (2003), it can be shown that this trivial solution becomes unstable at the critical $\alpha_{\text {critical }}=2 / 3 \approx 0.67$. For $\alpha>2 / 3$, we find two minima: one with "spins up" and the other one with "spins down."

In this symmetric problem, the strength of each potential is given by

$$
\omega=2 \log \left[\frac{\alpha}{1-\alpha}\right] \text { and thus } \sigma=1-\left(\frac{1-\alpha}{\alpha}\right)^{2}
$$

![img-3.jpeg](img-3.jpeg)

Figure 3: Three Ising grids in factor-graph notation: circles denote nodes, boxes interactions. (a) Toroidal boundary conditions. All elements of the allocation matrix equal to $3 / 4$ (not shown). (b) Aperiodic boundary conditions and (c) two loops left. The elements of the allocation matrix along the edges follow directly from optimizing condition 3 in theorem 4 and symmetry considerations. With $B=2-2 A$ in $b$ and $C=1-A$ in $c$, the optimal settings for the single remaining variable $A$ then boil down to $3 / 4$ and $1-\sqrt{1 / 8}$, respectively. See the text for further explanation.

The minimal (uniform) compensation in condition 3 of theorem 4 amounts to $A=3 / 4$ for all combinations of potentials and nodes. Substitution into condition 2 then yields

$$
\sigma \leq \frac{1}{3} \text { and thus } \alpha \leq \frac{1}{1+\sqrt{2 / 3}} \approx 0.55
$$

The critical value that follows from corollary 3 is in this case slightly better:

$$
\omega<1 \text { and thus } \alpha \leq \frac{1}{1+\mathrm{e}^{-1 / 2}} \approx 0.62
$$

Next we consider the same grid with aperiodic boundary conditions as in Figure 3b. Numerically, we find a critical $\alpha_{\text {critical }} \approx 0.79$. The value that follows from corollary 3 is dominated by the center node and hence stays the same: a unique loopy belief propagation fixed point for $\alpha<0.62$. Theorem 4 can be exploited to shift resources a little. In principle, we can solve the nonlinear programming problem, but for this small problem, it can still be done by hand with the following argumentation. Minimal compensation according to condition 3 in theorem 4 combined with symmetry considerations yields the allocation matrix elements along on the edges in Figure 3b. It is then easy to check that there are only two different appearances of condition 2 :

$$
(2-2 A) \sigma+\frac{3}{4} \leq 1 \text { and } \frac{1}{2} \sigma+A \leq 1
$$

The optimal choice for $A$ is the one in which both conditions turn out to be identical. In this way, we obtain $A=3 / 4$, yielding,

$$
\sigma \leq \frac{1}{2} \text { and thus } \alpha \leq \frac{1}{1+\sqrt{1 / 2}} \approx 0.58
$$

still slightly worse than the condition from corollary 3 .
An example in which the condition obtained with theorem 4 is better than the one from corollary 3 is given in Figure 3c. Straightforward analysis following the same recipe as for Figure 3b yields $A=1-\sqrt{1 / 8}$ with

$$
\sigma \leq \sqrt{\frac{1}{2}} \text { and thus } \alpha \leq \frac{1}{1+\sqrt{1-\sqrt{1 / 2}}} \approx 0.65
$$

better than the $\alpha<0.62$ from corollary 3 and to be compared with the critical $\alpha_{\text {critical }} \approx 0.88$

# 9 Discussion 

In this article, we derived sufficient conditions for loopy belief propagation to have just a single fixed point. These conditions remain much too strong to be anywhere near the necessary conditions and in that sense should be seen as no more than a first step. These conditions have the following positive features:

- Generalize the conditions for convexity of the Bethe free energy.
- Incorporate the (local) strength of potentials.
- Scale naturally as a function of the "temperature."
- Are invariant to arbitrary definitions of potentials and self-interactions.

Although the analysis that led to these conditions may seem quite involved, it basically consists of a relatively straightforward combination of two observations. The first observation is that we can exploit the arbitrariness in the definition of the Bethe free energy when we incorporate the constraints. This forms the basis of the resource allocation argument. And the second observation concerns the bound on the correlation of a loopy belief propagation marginal that leads to the introduction of the strength of a potential.

Besides its theoretical usefulness, there are more practical uses. First, algorithms for guaranteed convergence explicitly minimize the Bethe free energy. They can be considered "bound optimization algorithms," similar to expectation maximization and iterative proportional fitting: in the inner loop, they minimize a bound on the Bethe free energy, which is then updated in the outer loop. In practice, it appears that the tighter the bound, the faster the convergence (see, e.g., Heskes et al., 2003). Instead of a bound that is convex (Yuille, 2002) or convex over the set of constraints (Teh \& Welling, 2002; Heskes et al., 2003), we might relax the convexity condition and choose a tighter bound that still has a unique minimum, thereby speeding up the convergence. Second, in Wainwright et al. (2002) a convexified Bethe free energy is proposed. The arguments for this class of free energies are twofold: they yield a bound on the partition function (instead of just an approximation, as the standard Bethe free energy) and have a unique minimum. Focusing on the second argument, the conditions in this article can be used to construct Bethe free energies that may not be convex (over the set of constraints), but do have a unique minimum and, being closer to the standard Bethe free energy, may yield better approximations.

We can think of the following opportunities to make the sufficient conditions derived here stricter and thus closer to necessary conditions:

- The conditions guarantee convexity of the dual $G\left(Q_{\beta}, \lambda_{\alpha \beta}\right)$ with respect to $Q_{\beta}$. But in fact we need only $G\left(Q_{\beta}\right) \equiv \max _{\lambda_{\alpha \beta}} G\left(Q_{\beta}, \lambda_{\alpha \beta}\right)$ to be convex, which is a weaker requirement. The Hessian of $G\left(Q_{\beta}\right)$, however, appears to be more difficult to compute and to analyze in general, but may lead to stronger results in specific cases (e.g., only pairwise interactions or substituting a particular choice of $A_{\alpha \beta}$ ).
- It may be possible to strengthen the bound, equation 7.1, on loopy belief correlations, especially for interactions that involve more than two nodes.

An important question is how the uniqueness of loopy belief propagation fixed points relates to the convergence of loopy belief propagation.

Intuitively, one might expect that if loopy belief propagation has a unique fixed point, it will also converge to it. This also seems to be the argumentation in Tatikonda and Jordan (2002). However, to the best of our knowledge, there is no proof of such correspondence. Furthermore, the following set of simulations does seem to suggest otherwise.

We consider a Boltzmann machine with four binary nodes, weights

$$
w=\omega\left(\begin{array}{cccc}
0 & 1 & -1 & -1 \\
1 & 0 & 1 & -1 \\
-1 & 1 & 0 & -1 \\
-1 & -1 & -1 & 0
\end{array}\right)
$$

zero thresholds, and potentials

$$
\Psi_{i j}\left(x_{i}, x_{j}\right)=\exp \left[w_{i j} / 4\right] \text { if } x_{i}=x_{j} \text { and } \Psi_{i j}\left(x_{i}, x_{j}\right)=\exp \left[-w_{i j} / 4\right] \text { if } x_{i} \neq x_{j}
$$

Running loopy belief propagation, possibly damped as in equation 3.9, we observe "convergent" and "nonconvergent" behavior. For relatively small weights, loopy belief propagation converges to the trivial fixed point with $P_{i}\left(x_{i}\right)=0.5$ for all nodes $i$ and $x_{i}=\{0,1\}$, as in the lower left inset in Figure 4. For relatively large weights, it ends up in a limit cycle, as shown in the upper right inset. The weight strength that forms the transition between this "convergent" and "nonconvergent" behavior strongly depends on the step size. ${ }^{7}$ This by itself makes it hard to defend a one-to-one correspondence between convergence of loopy belief propagation (apparently depending on step size) and uniqueness of fixed points (obviously independent of step size).

For weights larger than roughly 5.8, loopy belief propagation failed to converge to the trivial fixed point even for very small step sizes. However, running a convergent double-loop algorithm from many different initial conditions and many weight strengths considerably larger than 5.8, we always ended up in the trivial fixed point and never in another one. We found similar behavior for a three-node Boltzmann machine (same weight matrix as above, except for the fourth node) for very large weights: loopy belief propagation ends up in a limit cycle, whereas a convergent double-loop algorithm converges to the trivial fixed point, which here, by corollary 2, is guaranteed to be unique. In future work we hope to elaborate on these issues.

[^0]
[^0]:    ${ }^{7}$ Note that the conditions for guaranteed uniqueness imply $\omega=4 / 3$ for corollary 3 and $\omega=\log (2) \approx 0.69$ for theorem 4 , both far below the weight strengths where "nonconvergent" behavior sets in.

![img-4.jpeg](img-4.jpeg)

Figure 4: The transition between "convergent" and "nonconvergent" behavior as a function of the step size used for damping loopy belief propagation and the weight strength. Simulations on a four-node Boltzmann machine. The insets show the marginal $P_{1}\left(x_{1}=1\right)$ as a function of the number of loopy belief iterations for step size 0.2 and strength 4 (lower left) and step size 0.6 and strength 6 (upper right). See the text for further detail.

# Acknowledgments 

This work has been supported in part by the Dutch Technology Foundation STW. I thank the anonymous reviewers for their constructive comments and Joris Mooij for computing the critical $\alpha_{\text {critical}}$ 's in section 8.3.
