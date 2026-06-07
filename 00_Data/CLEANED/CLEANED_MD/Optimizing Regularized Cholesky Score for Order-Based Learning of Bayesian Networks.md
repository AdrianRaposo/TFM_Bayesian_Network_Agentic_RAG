# Optimizing Regularized Cholesky Score for Order-Based Learning of Bayesian Networks 

Qiaoling Ye, Arash A. Amini, and Qing Zhou


#### Abstract

Bayesian networks are a class of popular graphical models that encode causal and conditional independence relations among variables by directed acyclic graphs (DAGs). We propose a novel structure learning method, annealing on regularized Cholesky score (ARCS), to search over topological sorts, or permutations of nodes, for a high-scoring Bayesian network. Our scoring function is derived from regularizing Gaussian DAG likelihood, and its optimization gives an alternative formulation of the sparse Cholesky factorization problem from a statistical viewpoint, which is of independent interest. We combine global simulated annealing over permutations with a fast proximal gradient algorithm, operating on triangular matrices of edge coefficients, to compute the score of any permutation. Combined, the two approaches allow us to quickly and effectively search over the space of DAGs without the need to verify the acyclicity constraint or to enumerate possible parent sets given a candidate topological sort. The annealing aspect of the optimization is able to consistently improve the accuracy of DAGs learned by local search algorithms. In addition, we develop several techniques to facilitate the structure learning, including pre-annealing data-driven tuning parameter selection and post-annealing constraint-based structure refinement. Through extensive numerical comparisons, we show that ARCS achieves substantial improvements over existing methods, demonstrating its great potential to learn Bayesian networks from both observational and experimental data.


Index Terms-Bayesian networks, proximal gradient, sparse Cholesky factorization, regularized likelihood, simulated annealing, structure learning, topological sorts.

## 1 INTRODUCTION

Bayesian networks (BNs) are a class of graphical models, whose structure is represented by a directed acyclic graph (DAG). They are commonly used to model causal networks and conditional independence relations among random variables. The past decades have seen many successful applications of Bayesian networks in computational biology, medical science, document classification, image processing, etc. As the relationships among variables in a BN are encoded in the underlying graph, various approaches have been put forward to estimate DAG structures from data. Constraint-based approaches, such as the PC algorithm [1], perform a set of conditional independence tests to detect the existence of edges. In score-based approaches, a network structure is identified by optimizing a score function [2, 3]. There are also hybrid approaches, such as the max-min hill-climbing algorithm [4], which use a constraint-based method to prune the search space, followed by a search for a high-scoring network structure.

The score-based search has been applied to three different search spaces: the DAG space [2, 5], the equivalence classes $[2,6]$ and the ordering space (or the space of topological sorts) [7, 8]. In this paper, we focus on the order-based search, which has two major advantages. First, the existence of an ordering among nodes guarantees a graph structure that satisfies the acyclicity constraint. Second, the space of orderings is significantly smaller than the space of DAGs or of the equivalence classes. Consequently, several lines of research have developed efficient order-based methods for DAG learning. Some methods adopt a greedy search in con-

[^0]junction with various operators that propose moves in the ordering space $[8,9,10,11]$. A greedy search, however, may easily be trapped in a local minimum, and thus different techniques were proposed to perform a more global search $[7,12,13,14]$. In particular, stochastic optimization, such as the genetic algorithm [7, 11, 15] and Markov chain Monte Carlo $[16,17]$, has been advocated as a promising way to perform global search over the ordering space.

In spite of these methodological and algorithmic advances, there are a few difficulties in score-based learning of topological sorts for DAGs. First, the score of an ordering is usually defined by the score of the optimal DAG compatible with the ordering. The computational complexity of finding the optimal DAG given an ordering, typically by enumerating all possible parent sets for each node [18], can be as high as $O\left(p^{k+1}\right)$ for $p$ nodes and a prespecified maximum indegree of $k$. Such computation is needed for every ordering evaluated by a search algorithm, which becomes prohibitive when $k$ is large. Second, although the ordering space is smaller than the graph space, optimization over orderings is still a hard combinatorial problem due to the NP-hard nature of structure learning of BNs [19]. It is not surprising that the performance of the above global optimization algorithms degrades severely for large graphs.

Motivated by these challenges, we develop a new orderbased method for learning Gaussian DAGs by optimizing a regularized likelihood score. Representing an ordering by the corresponding permutation matrix $P$, the weighted adjacency matrix of a Gaussian DAG can be coded into a lower triangular matrix $L$. We add a concave penalty function to the likelihood to encourage sparsity in $L$, and thus achieve the goal of structure learning. Instead of a prespecified maximum indegree, which is ad hoc in nature,


[^0]:    Department of Statistics, University of California, Los Angeles. This work was supported by NSF grant IIS-1546098. Email: yeqiaoling@g.ucla.edu, aaamini@stat.ucla.edu, zhou@stat.ucla.edu.

we provide a principled data-driven way to determine the tuning parameters for the penalty function. Finding the optimal DAG given $P$ is then reduced to $p$ decoupled penalized regression problems, which are solved by proximal gradient, an efficient first-order method, without enumerating possible parent sets for any node. Searching over $P$ is done by simulated annealing (SA). Other than using SA solely as a global optimization algorithm, we may also incorporate informative initial orderings, learned from an existing local algorithm, by setting a low starting temperature. Our numerical results demonstrate that this strategy substantially improves the accuracy of an estimated DAG. We note an interesting connection between our formulation and the sparse Cholesky factorization problem, and thus name our scoring function the regularized Cholesky score of orderings or permutations.

Regularizing likelihood with a continuous penalty function has been shown to be effective in learning Gaussian DAGs [20, 21]. These methods optimize a regularized likelihood score over the DAG space by blockwise coordinate descent, which is a local search algorithm in nature and thus likely to be trapped in a suboptimal structure. Using DAGs learned by these methods to generate initial orderings, our method can significantly improve the accuracy in structure learning. This highlights the advantages of combining local and global searches over the ordering space under an annealing framework. More recently, Champion et al. [15] developed a genetic algorithm that optimizes an $\ell_{1}$-penalized likelihood over a triangular coefficient matrix and a permutation to learn Gaussian BNs. However, the $\ell_{1}$ penalty tends to introduce more bias in estimation than a concave penalty, thus producing less accurate DAGs. The authors did not provide a principled method to select the tuning parameter for the $\ell_{1}$ penalty. Given a permutation, they optimize the network structure by an adaption of the least angle regression [22], which is closely related to the Lasso. In contrast, we use a more general and effective firstorder method, the proximal gradient algorithm, which is applicable to many regularizers, including the $\ell_{1}$ and concave penalties. As shown by our numerical experiments, our method substantially outperforms their genetic algorithm.

The paper is organized as follows. Section 2 covers some background on Gaussian BNs and the role of permutations in identifying the underlying DAGs. We introduce the regularized Cholesky loss and set up the global optimization problem for BN learning in Section 3. In Section 4, we develop the annealing on regularized Cholesky score (ARCS) algorithm which combines global annealing to search over the permutation space and a proximal gradient algorithm to optimize the network structure given an ordering. We also propose a constraint-based approach to prune the estimated network structure after annealing process and a data-driven model selection technique to choose tuning parameters for the penalty function. Section 5 consists of exhaustive numerical experiments, where we compare our method to existing ones using both observational and experimental data. We conclude with a discussion in Section 6. All proofs are relegated to the Appendix.

## 2 BACKGROUND

We start with some background on Bayesian networks. A Bayesian network for a set of variables $\left\{X_{1}, \ldots, X_{p}\right\}$ consists of 1) a directed acyclic graph $\mathcal{G}$ that encodes a set of conditional independence assertions among the variables, and 2) a set of local probability distributions associated with each variable. It can be considered as a recipe for factorizing a joint distribution of $\left\{X_{1}, \ldots, X_{p}\right\}$ with probability density

$$
p\left(x_{1}, \ldots, x_{p}\right)=\prod_{j=1}^{p} p\left(x_{j} \mid \Pi_{j}^{\mathcal{G}}=p a_{j}\right)
$$

where $\Pi_{j}^{\mathcal{G}} \subseteq\left\{X_{1}, \ldots, X_{p}\right\} \backslash\left\{X_{j}\right\}$ is the parent set of variable $X_{j}$ in $\mathcal{G}$ and $p a_{j}$ its value. The DAG $\mathcal{G}$ is denoted by $\mathcal{G}=(V, E)$, where $V=\{1, \ldots, p\}$ is the vertex set corresponding to the set of random variables and $E=\left\{(i, j): i \in \Pi_{j}^{\mathcal{G}}\right\} \subseteq V \times V$ is the edge set. We use variable $X_{j}$ and node $j$ exchangeably throughout the paper. DAGs contain no directed cycles, making the joint distribution in (1) well-defined.

### 2.1 Gaussian Bayesian networks

In this paper, we focus on Gaussian BNs that can be equivalently represented by a set of linear structural equation models (SEMs):

$$
X_{j}=\sum_{i \in \Pi_{j}^{\mathcal{G}}} \beta_{i j}^{0} X_{i}+\varepsilon_{j}, \quad j=1, \ldots, p
$$

where $\varepsilon_{j} \sim \mathcal{N}\left(0,\left(\omega_{j}^{0}\right)^{2}\right)$ are mutually independent and independent of $\left\{X_{i}: i \in \Pi_{j}^{\mathcal{G}}\right\}$. Defining $B_{0}:=\left(\beta_{i j}^{0}\right) \in \mathbb{R}^{p \times p}$, $\varepsilon:=\left(\varepsilon_{1}, \ldots, \varepsilon_{p}\right)^{\top} \in \mathbb{R}^{p}$, and $X:=\left(X_{1}, \ldots, X_{p}\right)^{\top} \in \mathbb{R}^{p}$, we rewrite (2) as

$$
X=B_{0}^{\top} X+\varepsilon
$$

The model has two parameters: 1) $B_{0}$ as a coefficient matrix, sometimes called the weighted adjacency matrix, where $\beta_{i j}^{0}$ specifies a weight associated with the edge $i \rightarrow j$ and $\beta_{i j}^{0}=$ 0 for $i \notin \Pi_{j}^{\mathcal{G}}$, and 2) $\Omega_{0}:=\operatorname{diag}\left(\left(\omega_{j}^{0}\right)^{2}\right)$ as a noise variance matrix. The SEMs in (2) define a joint Gaussian distribution, $X \sim \mathcal{N}\left(0, \Sigma_{0}\right)$, where $\Sigma_{0}$ is positive definite and given by

$$
\Sigma_{0}^{-1}=\left(I-B_{0}\right) \Omega_{0}^{-1}\left(I-B_{0}\right)^{\top}
$$

### 2.2 Acyclicity and permutations

The support of $B_{0}$ in (3) defines the structure of $\mathcal{G}$, and thus it must satisfy the acyclicity constraint so that $\mathcal{G}$ is indeed a DAG. To facilitate the development of our likelihood score for orderings, we express the acyclicity constraint on $B_{0}$ via permutation matrices. Let $\left\{e_{1}, \ldots, e_{p}\right\}$ be the canonical basis of $\mathbb{R}^{p}$. To each permutation $\pi$ on the set $[p]:=\{1, \ldots, p\}$, we associate a permutation matrix $P_{\pi}$ whose $i^{\text {th }}$ row is $e_{\pi(i)}^{\top}$. For a vector $v=\left(v_{1}, \ldots, v_{p}\right)^{\top}$, we have

$$
P_{\pi} v=v_{\pi}=\left(v_{\pi(1)}, \ldots, v_{\pi(p)}\right)^{\top}
$$

that is, $P_{\pi}$ permutes the entries of $v$ according to $\pi$. Since $P_{\pi}^{\top} P_{\pi}=I_{p}$, we can rewrite (3) as

$$
P_{\pi} X=B_{\pi}^{\top} P_{\pi} X+P_{\pi} \varepsilon
$$

![img-0.jpeg](img-0.jpeg)

Fig. 1: An example DAG G, its coefficient matrix $B_{0}$, and a permutation $\pi$. $B_{\pi}$ permutes columns and rows of $B_{0}$ and is strictly lower triangular.

where $B_{\pi}:=P_{\pi} B_{0} P_{\pi}^{\top}$ is obtained by permuting the rows and columns of $B_{0}$ simultaneously according to $\pi$. Then, $B_{\pi}$ will be a strictly lower triangular matrix if and only if $\pi$ is the reversal of a topological sort of $\mathcal{G}$, i.e., $i \prec j$ in $\pi$ for $j \in \Pi_{i}^{\mathcal{G}}$. See Figure 1 for an illustration. Under this reparameterization, we translate the acyclicity constraint on $B_{0}$ into the constraint that $B_{\pi}$ must be strictly lower triangular for some permutation $\pi$. Define $\Omega_{\pi}:=P_{\pi} \Omega_{0} P_{\pi}^{\top}$. Equivalently, one may think of the node $\pi(i)$ relabeled as $i$ in $B_{\pi}$ and $\Omega_{\pi}$.

For simplicity, we drop the subscript $\pi$ from $P_{\pi}, B_{\pi}$ and $\Omega_{\pi}$ if no confusion arises. Therefore, throughout the paper, $P$ defines a permutation $\pi$, $B$ and $\Omega$ label nodes according to $\pi$ and we write the permuted SEM as

$$
P X=B^{\top} P X+P \varepsilon
$$

Denote by $\operatorname{cov}(X)$ the covariance matrix of $X$. Then we have $\Sigma:=\operatorname{cov}(P X)=P \Sigma_{0} P^{\top}$, obtained by permuting the rows and columns of $\Sigma_{0}$ (4) according to $P$.

## 3 REGULARIZED LIKELIHOOD SCORE

In this section, we formulate the objective function to estimate BN structure given data from the Gaussian SEM (2).

### 3.1 Cholesky loss

Let $\mathbf{X}:=\left[\mathbf{X}_{1}, \ldots, \mathbf{X}_{p}\right] \in \mathbb{R}^{n \times p}$ be a data matrix where each row is an i.i.d. observation from (2). According to (6), we obtain a similar SEM on the data matrix:

$$
\mathbf{X} P^{\top}=\mathbf{X} P^{\top} B+\mathbf{E} P^{\top}
$$

where each row of $\mathbf{E} \in \mathbb{R}^{n \times p}$ is an i.i.d. error vector from $\mathcal{N}\left(0, \Omega_{0}\right)$. In (7), $\mathbf{X} P^{\top}$ and $\mathbf{E} P^{\top}$ are $\mathbf{X}$ and $\mathbf{E}$ with columns permuted according to $P=P_{\pi}$. It then follows that each row of $\mathbf{X} P^{\top}$ is an i.i.d. observation from $\mathcal{N}(0, \Sigma)$ with $\Sigma^{-1}=(I-B) \Omega^{-1}(I-B)^{\top}$, and thus the negative loglikelihood of (7) is

$$
\begin{aligned}
& \ell(B, \Omega, P \mid \mathbf{X}) \\
& =\frac{1}{2} \operatorname{tr}\left[P \mathbf{X}^{\top} \mathbf{X} P^{\top}(I-B) \Omega^{-1}(I-B)^{\top}\right]+\frac{n}{2} \log |\Omega|
\end{aligned}
$$

Recall that $B$ and $\Omega=\operatorname{diag}\left(\left(\omega_{j}\right)^{2}\right)$ are defined by permuting the rows and columns of $B_{0}$ and $\Omega_{0}$ by the permutation matrix $P$. In particular, $B$ is strictly lower triangular and we write its columns as $\beta_{j} \in \mathbb{R}^{p}$.

Denote by $L:=(I-B) \Omega^{-\frac{1}{2}}$ a weighted coefficient matrix, where each column $L_{j}=\left(e_{j}-\beta_{j}\right) / \omega_{j}$ is a weighted coefficient vector for node $\pi(j)$. We define what we call the Choleskly loss function

$$
\mathscr{L}_{\text {chol }}(L ; A):=\frac{1}{2} \operatorname{tr}\left(A L L^{\top}\right)-\log |L|
$$

where $|L|$ denotes the determinant of $L$. Noting that $|L|=$ $\left|(I-B) \Omega^{-\frac{1}{2}}\right|=|\Omega|^{-\frac{1}{2}}$ and denoting by $\widehat{\Sigma}:=\frac{1}{n} \mathbf{X}^{\top} \mathbf{X}$ the sample covariance matrix, one can re-parametrize the negative log-likelihood (8) with $L$ and $P$ and connect it to the Cholesky loss:

Lemma 1. The negative log-likelihood (8) for observational data can be re-parametrized as

$$
\begin{aligned}
\ell(L, P) & =n \cdot \mathscr{L}_{\text {chol }}\left(L ; P \widehat{\Sigma} P^{\top}\right) \\
& =\frac{n}{2} \operatorname{tr}\left(P \widehat{\Sigma} P^{\top} L L^{\top}\right)-n \log |L|
\end{aligned}
$$

where $L=(I-B) \Omega^{-\frac{1}{2}}$ is a lower triangular matrix and $P$ is a permutation matrix.

The reason for naming (9) the Cholesky loss is that it provides an interesting variational characterization of the Cholesky factor of the inverse of a matrix as the following proposition shows. Let $\mathcal{L}_{p}$ be the set of $p \times p$ lower triangular matrices with positive diagonal entries, and for any positive definite matrix $M$, let $\mathcal{C}(M)$ be its unique Cholesky factor, i.e., the unique lower triangular matrix $L$ with positive diagonal entries such that $M=L L^{\top}$.

Proposition 1. For any positive definite matrix $A \in \mathbb{R}^{p \times p}$, we have

$$
\arg \min _{L \in \mathcal{L}_{p}} \mathscr{L}_{\text {chol }}(L ; A)=\left\{\mathcal{C}\left(A^{-1}\right)\right\}
$$

with optimal value

$$
\mathscr{L}_{\text {chol }}^{*}(A):=\mathscr{L}_{\text {chol }}\left(\mathcal{C}\left(A^{-1}\right) ; A\right)=\frac{1}{2}(p+\log |A|)
$$

Consequently, $\mathscr{L}_{\text {chol }}^{*}(A)=\mathscr{L}_{\text {chol }}^{\star}\left(P A P^{\top}\right)$ for any permutation matrix $P$.

The proof is given in Appendix A.1. Proposition 1 states that $\mathcal{C}\left(A^{-1}\right)$ is the unique minimizer of $\mathscr{L}_{\text {chol }}(\cdot ; A)$. Now consider finding the maximum likelihood DAG for a fixed permutation $P$, which corresponds to minimizing $L \mapsto \ell(L ; P)$ given by (10). Let $\ell^{*}(P)$ be the optimal value of this problem, i.e.,

$$
\ell^{*}(P):=\min _{L \in \mathcal{L}_{p}} \ell(L ; P)
$$

Then, Proposition 1 implies

$$
\ell^{*}(P)=n \cdot \mathscr{L}_{\text {chol }}^{*}\left(P \widehat{\Sigma} P^{T}\right)=n \cdot \mathscr{L}_{\text {chol }}^{*}(\widehat{\Sigma})
$$

showing that $\ell^{*}$ is invariant to permutations, hence maximum likelihood estimation does not favor any particular ordering. In other words, all the maximum likelihood DAGs corresponding to different permutations give the same Gaussian likelihood.

### 3.2 Sparse regularization

To break the permutation equivalence of the maximum likelihood (11), we add a regularizer to the Cholesky loss to

favor sparse DAGs. Under faithfulness [23], the true DAG $\mathcal{G}$ in (2) and its equivalence class are the sparsest among all DAGs that can parameterize the joint distribution $\mathcal{N}\left(0, \Sigma_{0}\right)$. To start, let us point out some connections to the wellknown "sparse Cholesky factorization" problem from linear algebra.

According to Proposition 1, the minimizer of $\ell(L ; P)$ over $L$ is the Cholesky factor of $\left(P \widehat{\Sigma} P^{\top}\right)^{-1}=P \widehat{\Sigma}^{-1} P^{\top}$. For a sparse $\widehat{\Sigma}^{-1}$, it is well-known that the choice of $P$ greatly affects the sparsity of the resulting Cholesky factor. Heuristic approaches have been developed in numerical linear algebra to find a permutation that leads to a sparse factorization by trying to minimize the so-called "fill-in". An example is the maximum cardinality algorithm [24].

From a statistical perspective, however, $\widehat{\Sigma}^{-1}$ is, in general, not sparse (due to noise) even if the inverse of population covariance matrix $\Sigma=\mathbb{E}[\widehat{\Sigma}]$ is so. In such cases, one can first estimate a sparse precision matrix and then use the sparse estimate as the input to the sparse Cholesky factorization problem. We take a more direct alternative approach by adding a sparsity-measuring penalty to the Cholesky loss.

Let $\rho_{\theta}: \mathbb{R} \mapsto[0, \infty)$ be a nonnegative and nondecreasing regularizer with some tuning parameter(s) $\theta$. We consider the following penalized loss function:

$$
f_{\theta}(L ; P):=n \cdot \mathscr{L}_{\text {chol }}\left(L ; P \widehat{\Sigma} P^{\top}\right)+\sum_{i>j} \rho_{\theta}\left(L_{i j}\right)
$$

where the penalty is only applied to the off-diagonal entries of a lower triangular matrix $L$. The loss depends on the regularization parameter $\theta$, and for simplicity we write $f_{\theta}(L ; P)$ as $f(L ; P)$. In this paper, we focus on the class of regularizers called the minimax concave penalty (MCP) [25] which includes $\ell_{1}$ and $\ell_{0}$ as extreme cases; see (15) below. MCP is a sparsity-favoring penalty and adding it breaks the symmetry of the Cholesky loss w.r.t. permutations as in (11). As a result, the permutations leading to sparser lowertriangular factors $L$ will have smaller loss values $f(L ; P)$.

Let $\mathcal{P}_{p}$ be the set of $p \times p$ permutation matrices. Given $P \in \mathcal{P}_{p}$, the minimizer of $f(L ; P)$ over $L$ is a sparse DAG $\mathcal{G}(P)$ with a score $f(P)$ defined as

$$
f(P):=\min _{L \in \mathcal{L}_{p}} f(L ; P)
$$

We can minimize permutation score $f(P)$ over $\mathcal{P}_{p}$ to obtain an estimated ordering. The overall sparse BN learning problem is then

$$
\begin{aligned}
\min _{P \in \mathcal{P}_{p}} f(P)=\min _{P \in \mathcal{P}_{p}} \min _{L \in \mathcal{L}_{p}} & \left\{\frac{n}{2} \operatorname{tr}\left(P \widehat{\Sigma} P^{\top} L L^{\top}\right)\right. \\
& \left.-n \log |L|+\sum_{i>j} \rho_{\theta}\left(L_{i j}\right)\right\}
\end{aligned}
$$

In Section 4, we discuss our approach to solve this problem by optimizing over $(P, L)$. It is worth noting that problem (14) can be considered both as 1) a penalized maximum likelihood BN estimator in the Gaussian case, and 2) a variational formulation of the sparse Cholesky factorization problem when the input matrix $\widehat{\Sigma}$ is noisy (hence its inverse usually not sparse). According to the second interpretation, we call $f(L ; P)$ in (12) the regularized Cholesky loss function
![img-1.jpeg](img-1.jpeg)

Fig. 2: A comparison between the MCP (solid line) and the $\ell_{1}$ penalty (dashed line).
and $f(P)$ in (13) the regularized Cholesky (RC) score of a permutation $P$.

Throughout, let $\rho(\cdot):=\rho_{\theta}(\cdot)$ be the MCP with two parameters $\theta=(\gamma, \lambda)$ [25]:

$$
\rho(x ; \gamma, \lambda)= \begin{cases}\lambda|x|-\frac{x^{2}}{2 \gamma}, & |x|<\gamma \lambda \\ \frac{1}{2} \gamma \lambda^{2}, & |x| \geq \gamma \lambda\end{cases}
$$

where $\lambda \geq 0$ and $\gamma>1$. Parameter $\lambda$ measures the penalty level, while $\gamma$ controls the concavity of the function. For a fixed value of $\lambda$, the MCP approaches the $\ell_{1}$ penalty as $\gamma \rightarrow \infty$, and the $\ell_{0}$ penalty as $\gamma \rightarrow 0^{+}$.

Figure 2 compares the MCP with $(\gamma, \lambda)=(2,1)$ and the $\ell_{1}$ penalty. The right derivative of MCP at zero is $\lambda$, which is the same as the derivative of the $\ell_{1}$ penalty. The MCP function flats out when $|x| \geq \gamma \lambda$.

Remark 1. Aragam and Zhou [21] use an MCP regularized likelihood to estimate Gaussian DAGs as well. However, rather than searching over permutations, which automatically satisfies the acyclicity constraint, they perform a greedy coordinate descent to minimize the regularized loss over DAGs. Thus, at each update in their algorithm the acyclicity constraint must be carefully checked.

### 3.3 Likelihood for experimental data

It is well-known that DAGs in the same Markov equivalence class are observationally equivalent, and thus we cannot distinguish such DAGs from observational data alone. However, experimental interventions can help distinguish equivalent DAGs and construct causal networks. Following [26], intervention on a node $X_{j}$ in a DAG is to impose a fixed external distribution on this node, denoted by $p\left(x_{j} \mid \bullet\right)$, independent of all $X_{-j}$, while keeping the structural equations (2) of the other nodes unchanged.

Suppose that our data $\mathbf{X} \in \mathbb{R}^{n \times p}$ consists of $M$ blocks, where each block $\mathbf{X}^{m} \in \mathbb{R}^{n_{m} \times p}$ and $n=\sum_{m=1}^{M} n_{m}$. Denote by $X_{2}^{m} \subseteq\left\{X_{1}, \ldots, X_{p}\right\}$ the set of variables under experimental interventions in block $m$. Then, the data for $X_{j} \in X_{2}^{m}$ in this block are generated independently from the distribution $p\left(x_{j} \mid \bullet\right)$, while for $X_{i} \notin X_{2}^{m}$ from the conditional distribution $\left[X_{i} \mid \Pi_{i}^{p}\right]$. Note that multiple nodes could be intervened for a block of data, in which case $\left|X_{2}^{m}\right| \geq 2$.

Let $\mathcal{I}_{j} \subseteq\{1,2, \ldots, n\}$ be the set of observations for which $X_{j}$ is under experimental intervention, and let $\mathcal{O}_{j}=$ $\{1,2, \ldots, n\} \backslash \mathcal{I}_{j}$ be its complement. By the truncated factorization formula [23, 26, 27], the joint density of experimental data is

$$
p(\mathbf{X})=\prod_{j=1}^{p} \prod_{h \in \mathcal{O}_{j}} p\left(x_{h j} \mid p a_{h j}\right) \prod_{k \in \mathcal{I}_{j}} p\left(x_{k j} \mid \bullet\right)
$$

where $x_{h j}$ is the value of the $j^{\text {th }}$ variable in the $h^{\text {th }}$ observation and $p a_{h j}$ is the value for its parents. Let $\mathbf{X}_{\mathcal{O}_{\pi(j)}}$ be the submatrix of $\mathbf{X}$ with rows in $\mathcal{O}_{\pi(j)}$ and

$$
\widehat{\Sigma}^{j}:=\frac{1}{\left|\mathcal{O}_{\pi(j)}\right|} \mathbf{X}_{\mathcal{O}_{\pi(j)}}^{\top} \mathbf{X}_{\mathcal{O}_{\pi(j)}}
$$

be the sample covariance matrix computed from data in these rows. Then the log-likelihood of experimental data can be re-parametrized into the Cholesky loss functions as well:
Lemma 2. The negative log-likelihood for experimental data (16) can be written as

$$
\ell_{\mathcal{O}}(L, P)=\sum_{j=1}^{p}\left|\mathcal{O}_{\pi(j)}\right| \mathscr{L}_{\text {chol }}\left(L_{j} ; P \widehat{\Sigma}^{j} P^{\top}\right)
$$

where $L_{j}=\left(e_{j}-\beta_{j}\right) / \omega_{j} \in \mathbb{R}^{p}, L=\left(L_{j}\right) \in \mathcal{L}_{p}$, and $\left|L_{j}\right|:=$ $L_{j j}$ in $\mathscr{L}_{\text {chol }}(\cdot)(9)$.

See Appendix A. 2 for the proof. Though experimental data likelihood $\ell_{\mathcal{O}}(L, P)$ in (17) is not identical to the observational $\ell(L, P)$ in (10), searching strategies described in the next section can be applied on both observational and experimental data.

## 4 OPTIMIZATION

We now describe how we solve the optimization problem (14). The main steps are outlined in Algorithm 1, where we use simulated annealing to search over the permutation space for an ordering that minimizes the RC score defined in (13). To obtain the RC score for a given permutation, we need to solve a continuous optimization problem (line 2 and 6) for which we propose a proximal gradient algorithm (Algorithm 2).

### 4.1 Searching over permutations

The ARCS algorithm is detailed in Algorithm 1. At each iteration, we propose a permutation $P^{*}$ and decide whether to stay at the current permutation or move to the proposed one with probability $\alpha$ given in line 7 . The probability is determined by the difference between the proposed and current scores $f\left(P^{*}\right)-f(\widehat{P})$ normalized by a temperature parameter $T$. For $T \rightarrow \infty$, the jumps are completely random and for $T \rightarrow 0^{+}$completely determined by the RC score $f(\cdot)$. The algorithm follows a temperature schedule which is often taken to be a decreasing sequence $T^{(0)} \geq T^{(1)} \geq \ldots \geq T^{(N)}$ allowing the algorithm to explore more early on and zoom in on a solution as time progresses.

The proposed permutation matrix $P^{*}$ is constructed as follows. Let $\widehat{\pi}$ and $\pi^{*}$ be the permutations associated with $\widehat{P}$ and $P^{*}$ as in (5). We propose $\pi^{*}$ by flipping (i.e., reversing the order of) a random interval of length $m$ in the current

Algorithm 1 Annealing on regularized Cholesky score (ARCS).

Input: Dataset $\mathbf{X}$, initial permutation matrix $P_{0}$, a temperature schedule $\left\{T^{(i)}, i=0, \ldots, N\right\}$, constant $m$.
Output: Adjacency matrix $\widehat{B}$.
1: Select tuning parameters $(\gamma, \lambda)$ for $f(L ; P)$ according to Algorithm 4 (Section 4.4).
2: $\widehat{P} \leftarrow P_{0}, \widehat{L} \leftarrow \arg \min _{L \in \mathcal{L}_{p}} f(L ; \widehat{P})$ by Algorithm 2, $f(\widehat{P}) \leftarrow f(\widehat{L} ; \widehat{P})$.
3: for $i=0, \ldots, N$ do
4: $\quad T \leftarrow T^{(i)}$.
5: $\quad$ Propose $P^{*}$ by flipping a random length- $m$ interval in the permutation defined by $\widehat{P}$.
6: $\quad L^{*} \leftarrow \arg \min _{L \in \mathcal{L}_{p}} f\left(L ; P^{*}\right)$ using Algorithm 2, $f\left(P^{*}\right) \leftarrow f\left(L^{*} ; P^{*}\right)$.
7: $\quad \alpha \leftarrow \min \left\{1, \exp \left(-\frac{1}{T}\left[f\left(P^{*}\right)-f(\widehat{P})\right]\right)\right\}$.
8: $\quad$ Set $(\widehat{P}, \widehat{L}, f(\widehat{P})) \leftarrow\left(P^{*}, L^{*}, f\left(P^{*}\right)\right)$ with prob. $\alpha$.
9: end for
10: Refine adjacency matrix $\widehat{B}$ given $(\widehat{P}, \widehat{L})$ by Algorithm 3 (Section 4.3).
permutation $\widehat{\pi}$. For example, with $m=3$ we may flip $\widehat{\pi}=$ $(1,2,3,4, \ldots, p)$ to $\pi^{*}=(1,4,3,2, \ldots, p)$ in the proposal. Equivalently, we flip a contiguous block of $m$ rows of $\widehat{P}$ to generate $P^{*}$.

As a byproduct of evaluating the RC score for the proposed permutation $P^{*}$, we also obtain the corresponding lower triangular matrix $L^{*}$, representing the associated DAG. We keep track of these DAGs as well as the permutations throughout the algorithm (line 6).

### 4.2 Computing RC score

We propose a proximal gradient algorithm to evaluate the RC score $f(P)$ at each permutation matrix $P$ (line 2 and 6, Algorithm 1). This algorithm belongs to a class of first-order methods that are quite effective at optimizing functions composed of a smooth loss and a nonsmooth penalty [28].

The RC score is obtained by minimizing the RC loss $f(L ; P)$ over $L$ as shown in (13). Recall that $\mathcal{L}_{p}$ is the set of $p \times p$ lower triangular matrices, and let

$$
\rho(u):=\sum_{i>j} \rho\left(u_{i j}\right), \quad \text { for } \quad u=\left(u_{i j}\right) \in \mathcal{L}_{p}
$$

Note that we are leaving out the diagonal elements of $u$ in defining $\rho(u)$. Then, the RC loss is $f(u ; P)=\ell(u, P)+\rho(u)$, where $\ell(u, P)(10)$ is differentiable and $\rho(u)$ is nonsmooth. The idea of the proximal gradient algorithm is to replace $\ell(u, P)$ with a local quadratic function at the current estimate $L$ and optimize the resulting approximation to $f(u ; P)$ to get a new estimate $L^{+}$:

$$
\begin{aligned}
L^{+} & =\arg \min _{u \in \mathcal{L}_{p}} \ell(L)+\nabla \ell(L)^{\top}(u-L)+\frac{1}{2 t}\|u-L\|^{2}+\rho(u) \\
& =\arg \min _{u \in \mathcal{L}_{p}} \frac{1}{2 t}\|L-t \nabla \ell(L)-u\|^{2}+\rho(u)
\end{aligned}
$$

Algorithm 2 Compute the RC score by proximal gradient.
Input: $P, L^{(0)} \in \mathcal{L}_{p}, t^{(0)}>0, \kappa \in(0,1)$, max-iter, tol.
Output: $L$.
$k \leftarrow 0, \operatorname{err} \leftarrow \infty, L \leftarrow L^{(0)}$.
while $k<$ max-iter and err $>$ tol do
Compute $\nabla \ell(L)$ using either Lemma 3 or 4.
$t \leftarrow t^{(0)} /\|\nabla \ell(L)\|_{F}$.
repeat
$\tilde{L} \leftarrow L-t \nabla \ell(L)$.
$L_{i j}^{+} \leftarrow \operatorname{prox}_{t \rho}\left(\tilde{L}_{i j}\right)$ for $i>j$ (using Lemma 5).
$L_{i i}^{+} \leftarrow \tilde{L}_{i i}$.
break if $\ell\left(L^{+}, P\right) \leq \ell(L, P)+\left\langle\nabla \ell(L), L^{+}-L\right\rangle$ $+\frac{1}{2 t}\left\|L^{+}-L\right\|_{F}^{2}$
$t \leftarrow \kappa t$.
$\operatorname{err} \leftarrow \max _{j} \delta\left(L_{j}^{+}, L_{j}\right)$ where $\delta(x, y):=\frac{\|x-y\|}{\max \{\mathbb{1},\|y\|\}}$.
$L \leftarrow L^{+}$and $k \leftarrow k+1$.
end while
where $\ell(L)=\ell(L, P), \nabla \ell(L):=\nabla_{L} \ell(L, P)$ is the gradient of $\ell(L, P)$ w.r.t. $L$, and $t>0$ is a step size. Consider the proximal operator $\operatorname{prox}_{\rho}: \mathcal{L}_{p} \rightarrow \mathcal{L}_{p}$ associated with $\rho$ defined by

$$
\operatorname{prox}_{\rho}(x):=\underset{u \in \mathcal{L}_{p}}{\arg \min }\left(\rho(u)+\frac{1}{2}\|x-u\|^{2}\right)
$$

where $x \in \mathcal{L}_{p}$ and $\|\cdot\|$ is the usual Euclidean norm. Then, (19) is equivalent to

$$
L^{+}=\operatorname{prox}_{t \rho}(L-t \nabla \ell(L))
$$

where $\operatorname{prox}_{t \rho}(\cdot)$ is the proximal operator applied to the scaled function $t \rho(\cdot)$. Since $\rho(u)$ is separable across the coordinates $\left\{u_{i j}, i \geq j\right\}$, we have for $x \in \mathcal{L}_{p}$,

$$
\left(\operatorname{prox}_{\rho}(x)\right)_{i j}= \begin{cases}\operatorname{prox}_{\rho}\left(x_{i j}\right), & i>j \\ \operatorname{prox}_{0}\left(x_{i i}\right)=x_{i i}, & i=j\end{cases}
$$

The proximal operators on the RHS are univariate, and the distinction between the two cases is because we do not penalize the diagonal entries, i.e., $\rho\left(u_{i i}\right)=0$.

The overall procedure is summarized in Algorithm 2. To choose the step size $t$ normalized by $\|\nabla \ell(L)\|_{F}$ (line 4), we have used a line search strategy [28], where we repeatedly reduce the step size by a factor $\kappa \in(0,1)$ until a quadratic upper bound is satisfied by the new update (line 9). To implement Algorithm 2, we need two more ingredients, $\nabla \ell(L)$ and the univariate $\operatorname{prox}_{\rho}(\cdot)$, both of which have nice closed-form expressions:

Lemma 3. The gradient of $\ell(L, P)$ in (10) w.r.t. $L$ is

$$
\nabla \ell(L)=n\left(\Pi_{\mathcal{L}}\left(P \widehat{\Sigma} P^{\top} L\right)-\operatorname{diag}\left(\left\{1 / L_{i i}\right\}_{i=1}^{p}\right)\right)
$$

where $\Pi_{\mathcal{L}}: A \mapsto\left(A_{i j} \mathbb{1}\{i \geq j\}\right)_{p \times p}$ maps a matrix to its lower triangular projection.

Lemma 4. The gradient of $\ell_{\mathcal{O}}(L, P)$ in (17) w.r.t. $L_{j}$ is

$$
\nabla_{L_{j}} \ell_{\mathcal{O}}(L, P)=\left|\mathcal{O}_{\pi(j)}\right|\left(\Pi_{j}\left(P \widehat{\Sigma}^{j} P^{\top} L_{j}\right)-\frac{e_{j}}{L_{j j}}\right)
$$

where $\Pi_{j}: v \mapsto\left(v_{i} \mathbb{1}\{i \geq j\}\right)_{p \times 1}$ and $\left\{e_{j}\right\}$ is the canonical basis of $\mathbb{R}^{p}$.

Lemma 5. Let $\rho$ be the scalar MCP with parameter $(\gamma, \lambda)$ defined in (15), and let $\rho_{1}$ be the same penalty for $\lambda=\gamma=1$. Then, for any $t>0$,

$$
\operatorname{prox}_{t \rho}(x)=\lambda \gamma \operatorname{prox}_{(t / \gamma) \rho_{1}}\left(\frac{x}{\lambda \gamma}\right)
$$

and for any $\alpha>0$,

$$
\operatorname{prox}_{\alpha \rho_{1}}(x)= \begin{cases}0, & 0 \leq x<\min \{\alpha, 1\} \text { or } \\ \frac{x-\alpha}{1-\alpha}, & \alpha<x \leq 1 \\ x, & x>\max _{1} \{\alpha, 1\} \text { or } \\ & 1<\sqrt{\alpha}<x \leq \alpha\end{cases}
$$

Moreover, $\operatorname{prox}_{\alpha \rho_{1}}(-x)=-\operatorname{prox}_{\alpha \rho_{1}}(x)$ for all $x \in \mathbb{R}$.
We have excluded two special cases in (22) in which the minimizer is not unique: 1) If $x=\alpha=1, \operatorname{prox}_{\alpha \rho_{1}}(x)=$ $[0,1] ; 2$ ) If $x=\sqrt{\alpha}>1, \operatorname{prox}_{\alpha \rho_{1}}(x)=\{0, \sqrt{\alpha}\}$. We set $\operatorname{prox}_{\alpha \rho_{1}}(x)=0$ in our implementation if these special cases occur. The MCP has parameter $\gamma>1$, and usually the step size $t<1$. Thus, the cases with $\alpha<1$ are the most common scenario in our numerical study. These lemmas are proved in Appendix A.3, A.4, and A.5.

### 4.3 Structure refinement after annealing

At the end of the annealing loop (line 9, Algorithm 1), a pair $(\widehat{P}, \widehat{L})$ is found which minimizes the RC score (14). Accordingly, an estimated reversal of a topological sort is $\widehat{\pi}=\widehat{P}(1, \ldots, p)^{\top}$. Define $\widehat{L}=\widehat{P}^{\top} \widehat{L} \widehat{P}$, and $\widehat{B}$ by $\widehat{B}_{i j}=-\widehat{L}_{i j} / \widehat{L}_{j j}$ for $i \neq j$ and $\widehat{B}_{i i}=0$. Then, $\widehat{B}$ is the estimated weighted adjacency matrix for a DAG, i.e., an estimate for $B_{0}$. The support of $\widehat{B}$ gives the estimated parent sets $\widehat{p a}_{j}=\left\{i: \widehat{B}_{i j} \neq 0\right\}$ for $j=1, \ldots, p$. The use of a continuous regularizer, i.e. MCP, eases our optimization problem; however, this may lead to more false positive edges compared to $\ell_{0}$ regularization. To improve structure learning accuracy, we add a refinement step to remove some predicted edges by conditional independence tests, which borrows the strength from a constraint-based approach.

The refinement step outlined in Algorithm 3 is based on the following fact. If $k \prec j$ in a topological sort and there is no edge $k \rightarrow j$, then $X_{k} \perp X_{j} \mid \Pi_{j}$, where $\Pi_{j}$ is the parent set of $X_{j}$. For each $k \in \widehat{p a}_{j}$, we test the null hypothesis that $X_{k}$ and $X_{j}$ are conditionally independent given $\widehat{p a}_{j} \backslash$ $\{k\}$ using the Fisher Z-score. We remove the edge $k \rightarrow j$ if the null hypothesis is not rejected at a given significance level. The conditional independence tests are performed in a sequential manner for the nodes in $\widehat{p a}_{j}$ according to the estimated topological sort: For $k_{1}, k_{2} \in \widehat{p a}_{j}$, if $k_{1} \prec k_{2}$ in the sort, we carry out the test for $k_{2}$ prior to that for $k_{1}$.

### 4.4 Selection of the tuning parameters

Before starting the iterations in Algorithm 1, we select and fix the tuning parameters $\theta=(\gamma, \lambda)$ of MCP (line 1), hence fixing a particular scoring function $f(L, P)=f_{\theta}(L, P)$ throughout the algorithm.

Algorithm 3 Constraint-based structure refinement.
Input: Dataset $\mathbf{X}$, permutation $\widehat{\pi}$, adjacency matrix $\widehat{B}$, significance level $\alpha$.
Output: Adjacency matrix $\widehat{B}$.
$Z_{\alpha} \leftarrow \Phi^{-1}\left(1-\frac{\alpha}{2}\right)$, where $\Phi(x)$ is the CDF of $\mathcal{N}(0,1)$.
for $j=1, \ldots, p$ do
$\widehat{p a}_{j} \leftarrow\left\{i: \widehat{B}_{i j} \neq 0\right\}$.
for $k \in \widehat{p a}_{j}$ do
$\mathbf{s} \leftarrow \widehat{p a}_{j} \backslash\{k\}$.
$\mathbf{X}^{j} \leftarrow$ observations for which $j$ is not intervened
$n \leftarrow$ number of rows in $\mathbf{X}^{j}$.
$r_{j, k \mid \mathbf{s}} \leftarrow$ sample partial correlation between $X_{j}$ and $X_{k}$ given $X_{\mathbf{s}}$ based on $\mathbf{X}^{j}$.
$z \leftarrow \frac{1}{2} \sqrt{n-|\mathbf{s}|-3} \log \left(\frac{1+r_{j, k \mid \mathbf{s}}}{1-r_{j, k \mid \mathbf{s}}}\right)$.
Remove $k$ from $\widehat{p a}_{j}$, if $|z|<\widehat{Z_{\alpha}}$.
end for
$\widehat{B}_{i j} \leftarrow 1$ if $i \in \widehat{p a}_{j}$ and $\widehat{B}_{i j} \leftarrow 0$ otherwise.
end for

Algorithm 4 Tuning parameter selection by BIC.
Input: Initial permutation $P_{0}$ and a grid of values
$\left\{\theta^{(i)}\right\}=\left\{\left(\gamma^{(i)}, \lambda^{(i)}\right)\right\}$.
Output: Optimal index $i^{*}$ in the grid.
1: Define $\widehat{L}(\theta):=\arg \min _{L \in \mathcal{L}_{p}} f_{\theta}\left(L ; P_{0}\right)$ computed by Algorithm 2.
2: Let $\operatorname{BIC}(\theta):=2 \ell\left(\widehat{L}(\theta) ; P_{0}\right)+\|\widehat{L}(\theta)\|_{0} \log (\max \{n, p\})$.
3: Output $i^{*}=\arg \min _{i} \operatorname{BIC}\left(\theta^{(i)}\right)$.

We use the Bayesian information criterion (BIC) [29] to select the tuning parameters, given an initial permutation $P_{0}$. The details are summarized in Algorithm 4. For every pair $\left(\gamma^{(i)}, \lambda^{(i)}\right)$ over a grid of values, we evaluate the BIC score given in line 2, where $\|\widehat{L}(\cdot)\|_{0}$ is the number of nonzero entries in $\widehat{L}(\cdot)$, and then we output the one with the lowest BIC score. The regularization parameter in $\operatorname{BIC}(\theta)$ is adapted to $\log (\max \{n, p\})$, which works well for both low and highdimensional data. To construct the grid, possible choices for the concavity parameter $\gamma$ are $\{2,10,50,100\}$ based on our tests. Note that $\gamma>1$ is required in the definition of MCP (15), while the behavior of MCP for $\gamma \geq 100$ is essentially the same as the $\ell_{1}$ penalty. For the regularization parameter $\lambda$, we select 20 equi-spaced points from the interval $[0.1 \sqrt{n}, \sqrt{n}]$. The choice of $\sqrt{n}$ often leads to an empty graph when the data are standardized, hence a natural end point.

## 5 ReSults

### 5.1 Methods and data

Recall that $p$ is the number of variables and $n$ is the number of observations. For a thorough evaluation of the algorithm, we simulated data for both $n>p$ and $n<p$ cases.

We used real and synthetic networks to simulate data. Real networks were downloaded from the Bayesian networks online repository [30]. We duplicated some of them to further increase the network size. Synthetic DAG structures were constructed using the sparsebn package [31]. Given
a DAG structure, we sampled the edge coefficients $\beta_{i j}$ uniformly from $[-0.8,-0.5] \cup[0.5,0.8]$ and set the noise variance to one. We then calculated the covariance matrix according to (4) and normalized its diagonal elements to one. Consequently, the variances of $\left\{X_{1}, \ldots, X_{p}\right\}$ were identical. We used the following networks to generate observational data, denoted by the network name and $\left(p, s_{0}\right)$, where $s_{0}$ is the number of edges after duplication: 4 copies of Hailfinder (224, 264), 1 copy of Andes (223, 338), 2 copies of Hepar2 (280, 492), 4 copies of Win95pts (304, 448), 1 copy of Pigs (441, 592), and random DAGs, rDAG1 $(300,300)$ and rDAG2 $(300,600)$.

In the observational data setting, we compared our algorithm with the following BN learning algorithms: the coordinate descent (CD) algorithm [21], the standard greedy hill climbing (HC) algorithm [5], the greedy equivalence search (GES) [6], the Peter-Clark (PC) algorithm [1], the maxmin hill-climbing (MMHC) algorithm [4], and the genetic algorithm (GA) [15].

The CD algorithm optimizes a regularized log-likelihood function by a blockwise update on $\left(\beta_{i j}, \beta_{j i}\right)$ while checking the acyclicity constraint before each update. The HC algorithm performs a greedy search over the DAG space by starting from a certain initial state, performing a finite number of local changes and selecting the DAG with the best improvement in each local change. The GES algorithm searches over the equivalence classes and utilizes greedy search operators on the current state to find the next one, of which the output is an equivalence class of DAGs. The PC algorithm performs conditional independence tests to identify edges and orients edge directions afterwards. The MMHC algorithm constructs the skeleton of a Bayesian network via conditional independence tests and then performs a greedy hill climbing search to orient the edges via optimizing a Bayesian score. The GA decomposes graph estimation into two optimization sub-problems: node ordering search with mutation and crossover operators, and structure optimization by an adaption of the least angle regression [22].

Among these methods, PC is a constraint-based method, and MMHC is a hybrid method. Other methods, CD, HC, GES and GA, are all score-based, where CD and HC search over the DAG space, GES searches over the equivalence classes, and GA searches over the permutation space. Our method is a score-based search over the permutation space, similar to GA.

Our ARCS algorithm (Algorithm 1) may take an initial permutation $P_{0}$ provided by a local search method. In this study, we use the CD and GES algorithms to provide an initial permutation, and call the corresponding implementation ARCS(CD) and ARCS(GES). To partially preserve properties of the input initial permutation, we start with a low temperature $T^{(0)}=1$. The output of the CD algorithm is a DAG for which we find a topological sort to define $P_{0}$. The GES algorithm outputs a completed partially directed acyclic graph (CPDAG). We then generate a DAG in the equivalence class of the estimated CPDAG, and initialize ARCS with a topological sort of this DAG.

We implemented the ARCS algorithm in MATLAB, and used the following R packages for other methods: sparsebn [31] for the CD algorithm, rcausal [32] for

the GES, GIES (for experimental data) and PC algorithms, bnlearn [33] for the MMHC and HC algorithms, and GADAG [15] for the GA.

### 5.2 Accuracy metrics

Among all methods applied on observational data, ARCS, CD, HC and MMHC output DAGs, while the GES and PC algorithms output CPDAGs. Given these estimates, we need to evaluate the performance of each method. Define P, TP, FP, M, R as the numbers of estimated edges, true positive edges, false positive edges, missing edges and reverse edges, respectively. To standardize the performance metrics in observational data setting, we consider both directed and undirected edges in the definitions of these metrics as follows.

P is the number of edges in the estimated graph. FP is the number of edges in the estimated graph skeleton but not in the true skeleton. M counts the number of edges in the true skeleton but not in the skeleton of the estimated graph. We define an estimated directed edge to be true positive (TP) if it meets either of the two criteria: 1) This edge is in the true DAG with the same orientation; 2) This edge coincides after converting the estimated graph and true DAG to CPDAGs. An estimated undirected edge is considered TP if it satisfies the second condition. Note that our criterion takes into account reversible edges in an equivalence class for observational data. Lastly, the number of reversed edges $\mathrm{R}=\mathrm{P}-\mathrm{TP}-\mathrm{FP}$.

Denote by $s_{0}$ the number of edges in the true DAG. The overall accuracy of a method is measured by the structural Hamming distance (SHD) and Jaccard index (JI), where $\mathrm{SHD}=\mathrm{R}+\mathrm{FP}+\mathrm{M}$ and $\mathrm{JI}=\mathrm{TP} /\left(s_{0}+\mathrm{P}-\mathrm{TP}\right)$. A method has better performance if it achieves a lower SHD and/or a higher JI.

### 5.3 Comparison on observational data

We used large networks, where $p \in(200,450)$ and $s_{0} \in$ $(250,600]$, to simulate observational data with $n<p$ and $n>p$. For each setting $\left(p, s_{0}, n\right)$, we generated 20 datasets, and ran CD, ARCS(CD), GES, ARCS(GES) and other methods (PC, HC, MMHC and GA) with a maximum time allowance of 10 minutes per dataset. The HC and MMHC algorithms had an upper-bound of the in-degree number as 2 . We tried a higher maximum in-degree, but it resulted in a large FP. MMHC and PC were run with a significance level of 0.01 in conditional independence tests. We ran the CD algorithm with an MCP regularized likelihood, in which $\gamma=2$ and $\lambda$ was chosen by a default model selection mechanism. GA was run for a maximum of $10^{4}$ iterations, using the default population size and the default rates of mutation and crossover. We tried a larger population size for GA, but it was too time-consuming.

Our methods, ARCS(CD) and ARCS(GES), initialized with permutations from CD and GES estimates, were run for a maximum of $10^{4}$ iterations, with initial temperature $T^{(0)}=1$ and reversal length $m=4$ (Algorithm 1). A $p$-value cutoff of $10^{-5}$ was used in the refinement step (Algorithm 3). For the networks we considered, on average, 500 tests were performed in the refinement step, and the cutoff was chosen by Bonferroni correction to control the

TABLE 1: Comparison between ARCS and initial estimates on observational data $(n<p)$.


In this and all subsequent tables, reported results are rounded averages over 20 datasets; the best SHD and JI for each network are highlighted in boldface. familywise error rate at level 0.005 . In fact, our results were almost identical for any $p$-value cutoff between $10^{-3}$ and $10^{-5}$. ARCS versus CD and GES. Table 1 reports the average performance metrics across 20 datasets for 7 networks ( 5 real and 2 random networks) in the high-dimensional setting $n<p$ using CD, ARCS(CD), GES and ARCS(GES). We were interested in the potential improvement of ARCS upon its initial permutations. It is indeed confirmed by the results in the table that ARCS(CD) and ARCS(GES) outperformed CD and GES, respectively, for every network, achieving lower SHDs and higher JIs. The reduction in SHD was very substantial, close to or above $40 \%$, for many networks, such as Win95pts, Pigs, rDAG1 and rDAG2.

The same comparison was done for low-dimensional settings with $n>p$, reported in Table 2. We observe similar improvements of ARCS(CD) and ARCS(GES) over CD and GES, consistent with the results for high-dimensional data. It is seen from both tables that ARCS always increased TP, while maintaining or slightly reducing FP. The annealing process often identified more TP edges, while the refinement

1. Results for Pigs are averaged over 17 datasets because CD estimates were too dense using the default model selection criterion for the other three datasets.

TABLE 2: Comparison between ARCS and initial estimates on observational data $(n>p)$.


![img-2.jpeg](img-2.jpeg)

Fig. 3: Boxplots of SHDs for CD, ARCS(CD), GES and ARCS(GES) on observational data from two networks. step (Algorithm 3) cut down the FP edges given the ordering and parent sets learned through simulated annealing.

Figure 3 shows the clear improvement of the ARCS algorithm over CD and GES for the Andes and Win95pts networks with more choices of the sample size $n$. Each boxplot summarizes the SHDs over 20 datasets (excluding outliers). For all $n$, ARCS(GES) had a lower SHD than GES, and ARCS(CD) had a lower SHD than CD. The SHD distributions were well-separated, supporting the conclusion that ARCS significantly improves the accuracy of its initial estimates. ARCS(GES) versus HC, PC, MMHC and GA. We also compared ARCS(GES) with other existing methods, including

TABLE 3: ARCS against others on observational data $(n<p)$.

|  network
$\left(p, s_{0}, n\right)$ | method | P | TP | R | FP | SHD | JI  |

If a method is absent for a network, that means, it took more than 10 minutes to run on a singe dataset, and thus is excluded from the comparison.

HC, PC, MMHC and GA. Table 3 summarizes the average performance on high-dimensional observational data. Among all the methods, ARCS(GES) achieved the lowest SHD and the highest JI for all networks. The HC algorithm tended to output a denser DAG than the truth, leading to a large FP. The PC algorithm had a relatively large number of reverse edges, causing a high SHD. The MMHC algorithm had a lower SHD than some other algorithms, but the SHD difference between ARCS(GES) and MMHC was still large. The PC and MMHC algorithms were slow for some networks, and thus are absent in the results for these networks. The GA was formulated in a similar way as ARCS(GES), but the TPs of GA estimates were much lower, resulting in large SHDs for the tested networks.

Table 4 summarizes the results for the low-dimensional setup, $n>p$. It confirms that ARCS(GES) outperforms competing algorithms by a great margin. In general, HC had a larger P and GA had a smaller P than the true DAG, which indicates that their estimates were either too dense or too sparse. That the GA estimates were too sparse is more pronounced in this setting compared to the high-dimensional case. This might be related to its tuning parameter choice.

TABLE 4: ARCS against others on observational data $(n>p)$.


It is worth mentioning that ARCS(GES) outperformed other methods substantially for larger networks such as Pigs with $p=441$ and $s_{0}=592$. MMHC and PC failed to complete a single run on the Pigs network within 10 minutes, while HC and GA had very low accuracies. We suspect that the Pigs network has a certain structure that is particularly difficult to estimate, a hypothesis that merits more investigation.

We also tested another order-based algorithm, linear structural equation model learning (LISTEN) [34], which estimates Gaussian DAG structure by a sequential detection of ordering. A key assumption of LISTEN is that the noise variables have equal variances. Moreover, the algorithm requires a prespecified regularization parameter for the score metric. To compare with this algorithm, we adapted our data generation process to satisfy the equal-variance assumption. ARCS(GES) achieved a much higher accuracy, with SHD as small as $14 \%$ to $18 \%$ of the SHD achieved by LISTEN. Full results are reported in the supplementary material.

### 5.4 Comparison on experimental data

To generate experimental datasets, we generated $p$ blocks of observations, in each of which a single variable was under intervention. For each block, we generated 5 observations, and thus $n=5 p$. Networks in this experiment were smaller, with $p \leq 50$ and $s_{0} \leq 100$, including real DAGs $\left(p, s_{0}\right)$ : Asia $(8,8)$, Sachs $(11,17)$, Ins. $(27,52)$, Alarm $(37,46)$, and Barley $(48,84)$, and random DAGs: rDAG3 $(20,20)$, rDAG4 $(20,40)$, rDAG5 $(50,50)$ and rDAG6 $(50,100)$. Using these networks, we also simulated observational data of the same sample size, $n=5 p$, to study the effect of experimental interventions. Since networks in the experimental setting were smaller, we used a $p$-value cutoff of $10^{-3}$ in the refinement step of the ARCS algorithm (Algorithm 3).

To assess the accuracy on experimental data, we compare an estimated DAG with the true one to calculate the numbers of false positives (FP), missing edges (M), reverse edges $(\mathrm{R})$ and true positives (TP). FP and M follow the same calculations as in the observational settings. R counts the number of edges whose orientations are opposite between the two DAGs, and $\mathrm{TP}=\mathrm{P}-\mathrm{R}-\mathrm{FP}$. Note that the definition of R is different from that for observational data, because under the intervention setting used in this comparison, the true causal DAG is identifiable [20]. The structural Hamming distance (SHD) and the Jaccard index (JI) are then calculated as in the observational case.

In this setting, we compared ARCS with the CD algorithm [20] and the greedy interventional equivalence search (GIES) algorithm [35], both of which can handle experimental interventions. We initialize ARCS with CD and GIES estimates and call them ARCS(CD) and ARCS(GIES), respectively.

Table 5 compares the CD, ARCS(CD), GIES and ARCS(GIES) algorithms, averaging over 20 datasets for each type of networks. It is seen that both ARCS(GIES) and ARCS(CD) achieved dramatic improvements upon GIES and CD algorithms for every single network. This observation is consistent with the findings from the observational data and further confirms that the ARCS algorithm is a powerful tool for improving local estimates. Different from the observational data results (Table 1 and 2), ARCS(CD) usually had better performance than ARCS(GIES) on experimental data.
Experimental versus observational. We also compared the performance of our method ARCS(CD) on experimental and observational data with the same sample size $n=5 p$. Figure 4 plots the SHDs of ARCS(CD) on 20 datasets, with a side-by-side comparison between observational and experimental data. For some networks, such as rDAG6 and Ins., the estimated DAGs using experimental data had much lower SHDs than using the observational data. For some small networks, such as Asia, ARCS(CD) achieved a low SHD on observational data and the improvement when using experimental data was not substantial.

Because estimated DAGs did not have the same number of predicted edges, we further compared the reversed edge proportion (R/P). The DAGs estimated by ARCS(CD) had a lower R/P on the experimental than the observational data for all networks. The decrease in R/P with experimental interventions was remarkable, as Figure 4 shows. This finding supports the idea that experimental interventions help correct the reversed edges and distinguish equivalent DAGs. Note that for the 20 observational datasets generated from Asia $(p=8, s_{0}=8)$, ARCS(CD) output 16 estimated DAGs with $\mathrm{P}=8$ and $\mathrm{R}=1$, resulting in a very thin

TABLE 5: Performance comparison on experimental data.


interquantile range in the boxplots of Asia in Figure 4.

### 5.5 Effectiveness of BIC selection

Given an initial permutation, we use the BIC to choose tuning parameters $(\gamma, \lambda)$ before applying the ARCS algorithm (Section 4.4). In Tables 3 and 4, the number of predicted edges by ARCS(GES) is closer to $s_{0}$ than any other competing method in every network. This observation signifies the effectiveness of our parameter selection method by BIC. To further study its effect, we compared DAGs estimated with all values on a grid of $(\gamma, \lambda)$ by ARCS(CD) and ARCS(GES).

Figure 5 shows the histograms of the SHDs for all values of $(\gamma, \lambda)$ on Andes datasets with $\left(p, s_{0}\right)=(223,338)$ and $n \in\{200,400\}$. The grey area in a histogram corresponds to values of $(\gamma, \lambda)$ that led to a lower SHD than the $\left(\gamma^{*}, \lambda^{*}\right)$ chosen by the BIC, i.e., it indicates the percentile of the SHD of the BIC selection among all choices of the tuning parameters. The smaller this percentile, the better the BIC selection performance.

Each histogram has a high spike of large SHD, corresponding to large values of $\lambda$ that generate almost empty
![img-3.jpeg](img-3.jpeg)

Fig. 4: Comparison of SHD and reversed edge proportion between experimental and observational data with ARCS(CD).
graphs. The SHDs of ARCS(CD) with BIC selection corresponded to the $14^{\text {th }}$ and $16^{\text {th }}$ percentiles in low and high dimensions, respectively, and for ARCS(GES) the $16^{\text {th }}$ and $3^{\text {nd }}$ percentiles. These low percentiles confirm that the BIC selection works well for choosing the tuning parameters. Moreover, in our tests, the BIC usually selected $\gamma^{*}=2$, the smallest provided value for $\gamma$. Since for small $\gamma$, the MCP is closer to the $\ell_{0}$ penalty and far from the $\ell_{1}$ norm, this choice of $\gamma$ indicates the preference of concave penalties over $\ell_{1}$ in estimating sparse DAGs. Some of CD's and GA's inferior performances, such as CD on the Pigs network (Table 1) and the overall performance of GA (Tables 3 and 4), were potentially caused by a bad choice of their tuning parameters. This demonstrates the importance of our data-driven selection scheme for a regularized likelihood method.

### 5.6 Random initialization with a high temperature

Recall that we started ARCS(CD) and ARCS(GIES) with $T^{(0)}=1$. To test its global search ability over the permutation space, we may initialize the annealing process with a random permutation and a high temperature, which we denote by ARCS(RND). For a random initial permutation, we do not need to preserve its properties, so we use a high initial temperature $T^{(0)}=100$ to help the algorithm traverse the search space.

We compared ARCS(RND) and ARCS(CD) on experimental data for nine networks. We chose ARCS(CD) due to its superior performance on these networks in the experimental setting (Table 5). As shown in Figure 6, ARCS(RND) and ARCS(CD) had comparable performances on all net-

![img-4.jpeg](img-4.jpeg)

Fig. 5: Performance of the BIC selection among a grid of (γ, λ) given an initial permutation. Tuning parameters that lead to lower SHDs than the BIC selection are shown in gray.

![img-5.jpeg](img-5.jpeg)

Fig. 6: A comparison between ARCS(RND) with a high initial temperature and ARCS(CD) on experimental data.

works. Both of them learned DAGs with small SHDs. ARCS(RND) was slightly better on rDAG4 and Ins., and slightly worse on Alarm and rDAG6. For the other networks, the two methods were quite comparable, demonstrating the effectiveness of ARCS(RND).

The networks in this experiment had p ≤ 50. For p = 50, there are 50! ≈ 3 × 10⁶⁴ possible permutations. ARCS(RND) managed to learn a network structure within 10⁴ iterations, which is much smaller than p!. However, the performance of ARCS(RND) was not competitive on large networks. The reason is that for large p, it takes much more time for the annealing to thoroughly search the huge permutation space. Therefore, for large networks, it is better to initialize the ARCS algorithm with estimates from other local methods and choose a low temperature. Given a good initial estimate, ARCS searches over the permutation space and improves the accuracy of the initial estimate as demonstrated in Tables 1, 2 and 5. This study suggests that, by combining effective local and global searches under a regularized likelihood framework, our ARCS algorithm is a promising approach to the challenging problem of DAG structure learning.

## 6 DISCUSSION

In this paper, we developed a method to learn Gaussian BN structures by minimizing the MCP regularized Cholesky score over topological sorts, through a joint iterative update on a permutation matrix and a lower triangular matrix. We search over the permutation space and optimize the network structure encoded by a lower triangular matrix given a topological sort. This approach relates BN learning problem to sparse Cholesky factorization, and provides an alternative formulation for the order-based search. Our method can serve as an improvement of a local search or a stand-alone method with a best-guess initial permutation. Although we formulated this order-based search for Gaussian BNs, it can potentially be extended to discrete BNs and other scoring functions. A main difference in the extension to discrete data is the proximal gradient step, where we can borrow the regularized multi-logit model in [36] or develop a continuous regularizer for multinomial likelihood.

For the simulated annealing step, there are several interesting aspects to investigate. For instance, various operators of moving from one permutation to another have been proposed for greedy order-based search, which could better guide the annealing process in traversing the search space. This paper focuses on numerical results, and shows the advantage and potential application of local search and global annealing in learning BNs. Left as future work are theoretical properties of our method, such as the consistency of the regularized Cholesky score and the convergence of ARCS with a good initial permutation.

## APPENDIX A

### A.1 Proof of Proposition 1

Since A is positive definite, A⁻¹ is positive definite as well. Let us apply the Cholesky decomposition on A⁻¹, i.e., A⁻¹ = CCᵀ where C = C(A⁻¹). Therefore, A = C⁻ᵀC⁻¹. Recall that Lₚ is the set of lower triangular matrices with positive diagonals. The goal is to show that the minimizer of L⁰^{chol}(L; A) over Lₚ, denoted by L*, equals to C.

Letting R = C⁻¹L, we have log|R| = − log|C| + log|L|, where log|C| is a constant. Since C ∈ Lₚ and L ∈ Lₚ, we have R ∈ Lₚ as well. Also,

$$
\text{tr}(ALLᵀ) = \text{tr}(C^{-ᵀ}C^{-1} LLᵀ) = \text{tr}(RRᵀ) = \|R\|_{F}^2.
$$

Then,

$$
\begin{aligned}
& \min_{L \in L_p} \mathcal{L}_{\text{chol}}(L; A) = \min_{L \in L_p} \left[ \frac{1}{2} \text{tr}(ALLᵀ) - \log|L| \right] \\
& = \min_{R \in L_p} \frac{1}{2} \left[ \|R\|_{F}^2 - 2 \log|R|\right] - \log|C| \\
& = \min_{R \in L_p} \frac{1}{2} \left[ \sum_{(i,j):i>j} R_{ij}^2 + \sum_{i=1}^{p} (R_{ii}^2 - 2 \log R_{ii}) \right] - \log|C|.
\end{aligned}
$$

The problem is separable over entries. Minimizing over off-diagonal entries, the unique minimizer is $R_{i j}^{*}=0$ for all $i>j$ (and clearly $i<j$ ). Optimizing over $R_{i i}$, we are minimizing $x \mapsto x^{2}-2 \log x$ over $x>0$. The unique minimizer is attained at $x=1$, i.e. $R_{i i}^{*}=1$ for all $i$. Therefore the unique minimizer is $R^{*}=I_{p}$, i.e. $C^{-1} L^{*}=I_{p}$. In terms of the original variable, the minimizer is $L^{*}=C=\mathcal{C}\left(A^{-1}\right)$.

Substituting $L^{*}=\mathcal{C}\left(A^{-1}\right)$ into $\mathscr{L}_{\text {chol }}(L ; A)$, we obtain the minimum value:

$$
\begin{aligned}
\mathscr{L}_{\mathrm{chol}}^{*}(A) & :=\mathscr{L}_{\mathrm{chol}}\left(L^{*} ; A\right)=\frac{1}{2} \operatorname{tr}\left(A A^{-1}\right)-\log \left|A^{-\frac{1}{2}}\right| \\
& =\frac{1}{2}(p+\log |A|)
\end{aligned}
$$

The assertion $\mathscr{L}_{\text {chol }}^{*}(A)=\mathscr{L}_{\text {chol }}^{*}\left(P A P^{\top}\right)$ follows by noting that $\left|P \widehat{\Sigma} P^{T}\right|=|P||\widehat{\Sigma}|\left|P^{\top}\right|=|\widehat{\Sigma}|$.

## A. 2 Proof of Lemma 2

Recall $B=\left(\beta_{j}\right) \in \mathbb{R}^{p \times p}, \Omega=\operatorname{diag}\left(\omega_{j}^{2}\right) \in \mathbb{R}^{p \times p}$, we have the following experimental data log-likelihood:

$$
\begin{aligned}
& \ell_{\mathcal{O}}\left(B, \Omega, P_{\pi} \mid \mathbf{X}\right) \\
= & \sum_{j=1}^{p} \frac{1}{2 \omega_{j}^{2}}\left\|\mathbf{X}_{\mathcal{O}_{\pi(j)}: \pi(j)}-\mathbf{X}_{\mathcal{O}_{\pi(j)}} P_{\pi}^{\top} \beta_{j}\right\|^{2}+\frac{1}{2}\left|\mathcal{O}_{\pi(j)}\right| \log \omega_{j}^{2} \\
= & \frac{1}{2} \sum_{j=1}^{p}\left[\frac{1}{\omega_{j}^{2}}\left\|\mathbf{X}_{\mathcal{O}_{\pi(j)}} P_{\pi}^{\top}\left(e_{j}-\beta_{j}\right)\right\|^{2}+\left|\mathcal{O}_{\pi(j)}\right| \log \omega_{j}^{2}\right] \\
= & \frac{1}{2} \sum_{j=1}^{p}\left[\frac{1}{\omega_{j}^{2}} \operatorname{tr}\left(P_{\pi} \mathbf{X}_{\mathcal{O}_{\pi(j)}}^{\top} \mathbf{X}_{\mathcal{O}_{\pi(j)}} P_{\pi}^{\top}\left(e_{j}-\beta_{j}\right)\left(e_{j}-\beta_{j}\right)^{\top}\right)\right. \\
& \left.+\left|\mathcal{O}_{\pi(j)}\right| \log \omega_{j}^{2}\right]
\end{aligned}
$$

Recall $L_{j}=\left(e_{j}-\beta_{j}\right) / \omega_{j} \in \mathbb{R}^{p}$ and $L=\left(L_{j}\right) \in \mathbb{R}^{p \times p}$. Define $\left|L_{j}\right|:=L_{j j}$. Recall $\widehat{\Sigma}^{j}:=\frac{1}{\left|\mathcal{O}_{\pi(j)}\right|} \mathbf{X}_{\mathcal{O}_{\pi(j)}}^{\top} \mathbf{X}_{\mathcal{O}_{\pi(j)}}$ and simplify $P_{\pi}$ as $P$. We have

$$
\begin{aligned}
\ell_{\mathcal{O}}(L, P) & =\frac{1}{2} \sum_{j=1}^{p}\left|\mathcal{O}_{\pi(j)}\right| \cdot\left[\operatorname{tr}\left(P \widehat{\Sigma}^{j} P^{\top} L_{j} L_{j}^{\top}\right)-\log L_{j j}^{2}\right] \\
& =\sum_{j=1}^{p}\left|\mathcal{O}_{\pi(j)}\right|\left[\frac{1}{2} \operatorname{tr}\left(P \widehat{\Sigma}^{j} P^{\top} L_{j} L_{j}^{\top}\right)-\log \left|L_{j}\right|\right] \\
& =\sum_{j=1}^{p}\left|\mathcal{O}_{\pi(j)}\right| \mathscr{L}_{\mathrm{chol}}\left(L_{j} ; P \widehat{\Sigma}^{j} P^{\top}\right)
\end{aligned}
$$

where $\mathscr{L}_{\text {chol }}(L ; A)$ is the Cholesky loss defined in (9).

## A. 3 Proof of Lemma 3

Fix $P$ and let $Z=\frac{1}{\sqrt{n}} \mathbf{X} P^{\top}$ so that $Z^{\top} Z=\frac{1}{n} P \mathbf{X}^{\top} \mathbf{X} P^{\top}=$ $P \widehat{\Sigma} P^{\top}$. We can rewrite (10) as

$$
\ell(L):=\ell(L, P)=\frac{n}{2}\|Z L\|_{F}^{2}-n \log |L|
$$

Let $\ell^{1}(L):=\frac{n}{2}\|Z L\|_{F}^{2}$ and $\ell^{2}(L):=-n \log |L|$. To compute the gradient of $\ell^{1}$ w.r.t. $L$, we perturb $L$ to $L+t \delta$ where
$\delta \in \mathcal{L}_{p}$ and $t \in \mathbb{R}$. We have

$$
\begin{aligned}
\lim _{t \rightarrow 0} \frac{\ell^{1}(L+t \delta)-\ell^{1}(L)}{t} & =\lim _{t \rightarrow 0}\left[n\langle Z L, Z \delta\rangle+\frac{t n}{2}\|Z \delta\|_{F}^{2}\right] \\
& =n\langle Z L, Z \delta\rangle=n\left\langle Z^{\top} Z L, \delta\right\rangle
\end{aligned}
$$

where $\langle A, B\rangle=\operatorname{tr}\left(A^{\top} B\right)$ for two matrices $A$ and $B$. Be definition, $\Pi_{\mathcal{L}}$ maps a $p \times p$ matrix to its lower triangular projection. Since $\delta \in \mathcal{L}_{p_{f}}\left\langle Z^{\top} Z L, \delta\right\rangle=\left\langle\Pi_{\mathcal{L}}\left(Z^{\top} Z L\right), \delta\right\rangle$, and thus $\nabla \ell^{1}(L)=n \Pi_{\mathcal{L}}\left(Z^{\top} Z L\right)$.

For the second term, $\ell^{2}=-n \sum_{i=1}^{p} \log L_{i i}$, and thus $\nabla \ell^{2}(L)=-n \operatorname{diag}\left(\left\{1 / L_{i i}\right\}_{i=1}^{p}\right)$ where $L \in \mathcal{L}_{p}$. Putting the pieces together gives the desired result.

## A. 4 Proof of Lemma 4

From (17), we have $\ell_{\mathcal{O}}=\ell_{\mathcal{O}}^{1}+\ell_{\mathcal{O}}^{2}$, where

$$
\begin{aligned}
\ell_{\mathcal{O}}^{1} & :=\frac{1}{2} \sum_{j=1}^{p}\left|\mathcal{O}_{\pi(j)}\right| L_{j}^{\top} P \widehat{\Sigma}^{j} P^{\top} L_{j} \\
\ell_{\mathcal{O}}^{2} & :=-\sum_{j=1}^{p}\left|\mathcal{O}_{\pi(j)}\right| \log L_{j j}
\end{aligned}
$$

Note that each term in $\ell_{\mathcal{O}}^{1}$ is a quadratic form in $L_{j}$. The gradient of $\ell_{\mathcal{O}}^{1}$ w.r.t. to $L_{j}$ is $\left|\mathcal{O}_{\pi(j)}\right| \Pi_{j}\left(P \widehat{\Sigma}^{j} P^{\top} L_{j}\right)$, since $L_{i j}=0$ for $i<j$. It is also easy to see that $\nabla_{L_{j}} \ell_{\mathcal{O}}^{2}=$ $-\left|\mathcal{O}_{\pi(j)}\right| \frac{e_{j}}{L_{j j}}$. Putting the pieces together, the gradient of $\ell_{\mathcal{O}}$ w.r.t. $L_{j}$ is $\left|\mathcal{O}_{\pi(j)}\right|\left(\Pi_{j}\left(P \widehat{\Sigma}^{j} P^{\top} L_{j}\right)-\frac{e_{j}}{L_{j j}}\right)$.

## A. 5 Proof of Lemma 5

Recall the MCP function is defined as

$$
\rho(x)= \begin{cases}\lambda|x|-\frac{x^{2}}{2 \gamma}, & |x|<\gamma \lambda \\ \frac{1}{2} \gamma \lambda^{2}, & |x| \geq \gamma \lambda\end{cases}
$$

It is not hard to see that $\rho(\lambda \gamma x)=\gamma \lambda^{2} \rho_{1}(x)$. It follows that

$$
\begin{aligned}
& \operatorname{prox}_{t \rho}(\lambda \gamma x) \\
= & \underset{u}{\arg \min }\left[\rho(u)+\frac{1}{2 t}(u-\lambda \gamma x)^{2}\right] \\
= & \lambda \gamma \cdot \underset{v}{\arg \min }\left[\rho(\lambda \gamma v)+\frac{1}{2 t}(\lambda \gamma v-\lambda \gamma x)^{2}\right] \\
= & \lambda \gamma \cdot \underset{v}{\arg \min }\left[\gamma \lambda^{2} \rho_{1}(v)+\frac{\gamma^{2} \lambda^{2}}{2 t}(v-x)^{2}\right] \\
= & \lambda \gamma \cdot \underset{v}{\arg \min }\left[\rho_{1}(v)+\frac{\gamma}{2 t}(v-x)^{2}\right] \\
= & \lambda \gamma \operatorname{prox}_{(t / \gamma) \rho_{1}}(x)
\end{aligned}
$$

where the second equality uses the change of variable $u=$ $\lambda \gamma v$ and the fourth uses the fact that $\arg \min$ is invariant to rescaling the objective. This establishes (21).

Due to the symmetry of $\rho_{1}$, we have $\operatorname{prox}_{\alpha \rho_{1}}(-x)=$ $-\operatorname{prox}_{\alpha \rho_{1}}(x)$, which is easy to see by a change of variable $u=-v$ in the defining optimization. Thus, it is enough to consider $x \geq 0$ which we assume in the following.

The function $h(u)=\rho_{1}(u)+\frac{1}{2 \alpha}(u-x)^{2}$ is continuous and decreasing on $(-\infty, 0]$, hence it achieves its minimum of $\frac{x^{2}}{2 \alpha}$ over this interval at $u=0$. Over $(0, \infty)$, the function is differentiable with derivative $h^{\prime}(u)=(1-u)_{+}+\frac{1}{\alpha}(u-x)$ which is piecewise linear (or affine) with a break at $u=1$. The first segment of $h^{\prime}$ is a line connecting $(0,1-x / \alpha)$ to

![img-6.jpeg](img-6.jpeg)

Fig. 7: (a) The derivative $h^{\prime}(u)$ for $u \in(0, \infty)$ in a typical case. Note that $h^{\prime}$ is discontinuous at 0 . (b) and (c) Plots of $h(u)$ for two values of $(\alpha, x)$ that lead to case 4.
$(1,(1-x) / \alpha)$. The next segment is an always-increasing section starting at $(1,(1-x) / \alpha)$ and increasing with slope $1 / \alpha$. See Figure 7(a). The behavior of $h^{\prime}$ for $u \in(0,1)$ determines the minimizer. We have four cases:

1) When both $1-x / \alpha>0$ and $(1-x) / \alpha>0$, that is $x<\min \{\alpha, 1\}, h^{\prime}$ is increasing in $[0,1]$. Hence, $h^{\prime}>0$ over $[0, \infty)$ and the overall minimum of $h$ occurs at $u_{1}=0$.
2) When $1-x / \alpha \leq 0<(1-x) / \alpha$, that is, $\alpha \leq x<1$, then $h$ has a single critical point at $u_{2}=(x-\alpha) /(1-\alpha)$ before which it decreases and after which it increases. Hence, this is its unique minimizer.
3) When both $1-x / \alpha<0$ and $(1-x) / \alpha<0$, that is, $x>\max \{\alpha, 1\}$, then, the only critical point occurs in the second linear segment and is $u_{3}=x$ which is the unique minimizer.
4) When $(1-x) / \alpha<0 \leq 1-x / \alpha$, that is, $1<x \leq \alpha$, then both of the points $u_{2}$ and $u_{3}$ in cases 2 and 3 are critical points. The function drops in $\left(-\infty, u_{1}\right)$ where $u_{1}=0$, increases in $\left(u_{1}, u_{2}\right)$, drops in $\left(u_{2}, u_{3}\right)$ and increases in $\left(u_{3}, \infty\right)$. Thus, both $u_{1}$ and $u_{3}$ are local minima (while $u_{2}$ is a local maximum). The global minimum is determined by comparing $h\left(u_{1}\right)=x^{2} /(2 \alpha)$ and $h\left(u_{3}\right)=1 / 2$. That is, if $x<\sqrt{\alpha}$, the global minimum is $u_{1}=0$ (Figure 7b); if $x>\sqrt{\alpha}$, the global minimum is $u_{3}=x$ (Figure 7c); if $x=\sqrt{\alpha}$, minimum is $\left\{u_{1}, u_{3}\right\}=\{0, x\}$, which is not unique.
What left is the special case when both $1-x / \alpha=0$ and $(1-x) / \alpha=0$, i.e. $\alpha=x=1$, indicating the first segment of $h^{\prime}(u), u \geq 0$, is flat as zero. Hence, minimizer of $h$ is any value in the interval $[0,1]$. We merge case 4 into cases 1 and 3 by revising the domains of $x$, and thus complete the derivation of (22).
