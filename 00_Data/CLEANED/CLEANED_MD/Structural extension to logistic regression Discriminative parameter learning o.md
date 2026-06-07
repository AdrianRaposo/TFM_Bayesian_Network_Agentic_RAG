# Structural Extension to Logistic Regression: Discriminative Parameter Learning of Belief Net Classifiers* 

RUSSELL GREINER<br>greiner@cs.ualberta.ca ${ }^{\dagger}$<br>Department of Computing Science, University of Alberta, Edmonton, AB T6G 2H1 Canada

XIAOYUAN SU
xsu1@umsis.miami.edu
Electrical \& Computer Engineering, University of Miami, Coral Gables, FL 33124, USA

BIN SHEN
bshen@cs.ualberta.ca
Department of Computing Science, University of Alberta, Edmonton, AB T6G 2H1 Canada

WEI ZHOU
w2zhou@math.uwaterloo.ca
School of Computer Science, University of Waterloo, Waterloo, ON N2L 3G1, Canada

Editors: Pedro Larrañaga, Jose A. Lozano, Jose M. Peña and Iñaki Inza


#### Abstract

Bayesian belief nets (BNs) are often used for classification tasks-typically to return the most likely class label for each specified instance. Many BN-learners, however, attempt to find the BN that maximizes a different objective function-viz., likelihood, rather than classification accuracy-typically by first learning an appropriate graphical structure, then finding the parameters for that structure that maximize the likelihood of the data. As these parameters may not maximize the classification accuracy, "discriminative parameter learners" follow the alternative approach of seeking the parameters that maximize conditional likelihood (CL), over the distribution of instances the BN will have to classify. This paper first formally specifies this task, shows how it extends standard logistic regression, and analyzes its inherent sample and computational complexity. We then present a general algorithm for this task, ELR, that applies to arbitrary BN structures and that works effectively even when given incomplete training data. Unfortunately, ELR is not guaranteed to find the parameters that optimize conditional likelihood; moreover, even the optimal-CL parameters need not have minimal classification error. This paper therefore presents empirical evidence that ELR produces effective classifiers, often superior to the ones produced by the standard "generative" algorithms, especially in common situations where the given BN-structure is incorrect.


Electronic Supplementary Material: Supplementary material to this paper is available in electronic form at http://dx.doi.org/10.1007/s10994-005-0469-0

Keywords: (Bayesian) belief nets, logistic regression, classification, PAC-learning, computational/sample complexity
*This paper extends the earlier results that appear in Greiner and Zhou (2002) and Shen et al. (2003).
${ }^{\dagger}$ This e-mail address is available for all problems and questions.

# 1. Introduction 

Many tasks-including fault diagnosis, pattern recognition and forecasting-can be viewed as classification, as each requires assigning the class ("label") to a given instance, which is specified by a set of attributes. An increasing number of projects are using "(Bayesian) belief nets" $(B N)$ to represent the underlying distribution, and hence the stochastic mapping from evidence to response.

When this distribution is not known a priori, we can try to learn the model. Our goal is an accurate BN-i.e., one that returns the correct answer as often as possible. While a perfect model of the distribution will perform optimally for any possible query, learners with limited training data are unlikely to produce such a model; moreover, optimality may be impossible for learners constrained to a restricted range of possible distributions that excludes the correct one (e.g., when only considering parameterizations of a given $B N$-structure).

Here, it makes sense to find the parameters that do well with respect to the queries posed. This "discriminative learning" task differs from the "generative learning" that is used to learn an overall model of the distribution (Ripley, 1996). Following standard practice, our discriminative learner will seek the parameters that maximize the log conditional likelihood (LCL) over the data, rather than simple likehood-that is, given the data $S=\left\{\left\langle c_{i}, \mathbf{e}_{i}\right\rangle\right\}$ (each class label $C=c_{i}$ associated with evidence $\mathbf{E}=\mathbf{e}_{i}$ ), a discriminative learner will try to find parameters $\Theta$ that maximize

$$
\overline{\mathrm{LCL}}^{(S)}(\Theta)=\frac{1}{|S|} \sum_{\left\langle c_{i}, \mathbf{e}_{i}\right\rangle \in S} \log P_{\Theta}\left(c_{i} \mid \mathbf{e}_{i}\right)
$$

rather than the ones that maximize $\sum_{\left\langle c_{i}, \mathbf{e}_{i}\right\rangle \in S} \log P_{\Theta}\left(c_{i}, \mathbf{e}_{i}\right)$ (Ripley, 1996).
Optimizing the LCL of the root node (given the other attributes) of a naïve-bayes structure can be formulated as a standard logistic regression problem (McCullagh \& Nelder, 1989; Jordan, 1995). General belief nets extend Naïve-bayes-structures by permitting additional dependencies among the attributes. This paper provides a general discriminative learning tool, ELR, that can learn the parameters for an arbitrary structure, completing the analogy

Naïve-bayes : General Belief Net :: Logistic Regression : ELR .
Moreover, while most algorithms for learning logistic regression functions require complete training data, the ELR algorithm can accept incomplete data. We also present empirical evidence, from a large number of datasets, to demonstrate that ELR works effectively.

Section 2 provides the foundations, overviewing belief nets then defining our task: discriminatively learning the parameters for a fixed belief net structure, $G$, that maximize LCL. Section 3 formally analyses this task, providing both sample and computational complexity, and noting how these results compare with corresponding results for generative learning. Seeing that our task is NP-hard in general, Section 4 presents a gradient-descent discriminative parameter learning algorithm for general BNs, ELR. Section 5 reports empirical results that demonstrate that our ELR produces a classifier that is often superior to ones produced by standard learning algorithms (which maximize likelihood), over a variety of situations, involving both complete and incomplete data. Section 6 provides a brief survey of the relevant literature. The Electronic Supplementary Material (ESM) attachment

(http://www.cs.ualberta.ca/ greiner/ELR) contains auxiliary material, including proofs of some of the claims appearing in this text, as well as more information about the experiments shown in Section 5, and descriptions of yet other empirical studies. Below we will let $\operatorname{ESM}(x)$ refer to Appendix $x$ of this auxiliary material.

# 2. Framework 

We assume there is a stationary underlying distribution $P(\cdot)$ over $N$ (discrete) random variables $\mathcal{V}=\left\{V_{1}, \ldots, V_{n}\right\}$. For example, perhaps $V_{1}$ is the "Cancer" random variable, whose value ranges over $\{$ true, false $\} ; V_{2}$ is "Gender" $\in\{$ male, female $\}, V_{3}$ is "Age" $\in\{0, \ldots, 100\}$, etc. We refer to this joint distribution as the "underlying distribution" or the "event distribution".

We can encode this which we encode as a "(Bayesian) belief net" (BN)—a directed acyclic graph $B=\langle\mathcal{V}, A, \Theta\rangle$, whose nodes $\mathcal{V}$ represent variables, and whose arcs $A$ represent dependencies. Each node $D_{i} \in \mathcal{V}$ also includes a conditional-probability-table (CPtable) $\theta_{i} \in \Theta$ that specifies how $D_{i}$ 's values depend (stochastically) on the values of its immediate parents. In particular, given a node $D \in \mathcal{V}$ with immediate parents $\mathbf{F} \subset \mathcal{V}$, the parameter $\theta_{d \mid \mathbf{f}}$ represents the network's term for $P(D=d \mid \mathbf{F}=\mathbf{f})$ (Pearl, 1988).

The user interacts with the belief net by asking queries, each of the form "What is $P(C=$ $c \mid \mathbf{E}=\mathbf{e})$ ?"-e.g., What is $P$ (Cancer $=$ true $\mid$ Gender $=$ male, Smoke $=$ true)? where $C \in \mathcal{V}$ is a single "query variable", $\mathbf{E} \subset \mathcal{V}$ is the subset of "evidence variables", and $c$ (resp., e) is a legal assignment to $C$ (resp., $\mathbf{E}$ ). This paper focuses on the case where all queries involve the same variable; e.g., all queries ask about Cancer. Moreover, we will follow standard practice by assuming the distribution of conditioning events matches the underlying distribution. This means there is a single distribution from which we can draw labeled instances, which each correspond to a "labeled query". ${ }^{1}$ Note this corresponds to the data sample used by standard learning algorithms.

Given any unlabeled instance $\left\{\mathbf{E}_{i}=\mathbf{e}_{i}\right\}$, the belief net ${ }^{2} \Theta$ will produce a distribution over the values of the query variable; perhaps $P_{\Theta}(C=$ true $\mid \mathbf{E}=\mathbf{e})=0.3$ and $P_{\Theta}(C=$ false $\mid \mathbf{E}=\mathbf{e})=0.7$. In general, the associated $H_{\Theta}$ classifier system will then return the value $H_{\Theta}(\mathbf{e})=\operatorname{argmax}_{\mathrm{c}}\left\{\mathrm{P}_{\Theta}(\mathrm{C}=\mathrm{c} \mid \mathbf{E}=\mathbf{e})\right\}$ with the largest posterior probability-here return $H_{\Theta}(\mathbf{E}=\mathbf{e})=$ false as $P_{\Theta}($ Cancer $=$ false $\mid \mathbf{E}=\mathbf{e})>$ $P_{\Theta}($ Cancer $=$ true $\mid \mathbf{E}=\mathbf{e})$.

A good belief net classifier is one that produces the appropriate answers to these unlabeled queries. We will use "classification error" (aka " $0 / 1$ " loss) to evaluate the resulting $\Theta$-based classifier $H_{\Theta}$

$$
\operatorname{err}(\Theta)=\sum_{\langle\mathbf{e}, c\rangle} P(\mathbf{e}, c) \times \mathcal{I}\left(H_{\Theta}(\mathbf{e}) \neq c\right)
$$

where $\mathcal{I}(a \neq b)=1$ if $a \neq b$, and $=0$ otherwise.
Our goal is a belief net $\Theta^{*}$ that minimizes this score, with respect to the true distribution $P(\cdot)$. While we do not know this distribution a priori, we can use a sample drawn from this distribution, to help determine which belief net is optimal. This paper focuses on the task of learning the optimal CPtable $\Theta$ for a given BN-structure $G=\langle\mathcal{V}, A\rangle$.

Conditional likelihood. In earlier work (Zhou, 2002, Sections 3.1.3 and 3.2.2), we compared learners that optimized $\operatorname{err}(\Theta)$ versus ones that optimized the "log conditional likelihood" of a belief net $\Theta$

$$
\operatorname{LCL}_{P}(\Theta)=\sum_{\langle\mathbf{e}, c\rangle} P(\mathbf{e}, c) \times \log \left(P_{\Theta}(c \mid \mathbf{e})\right)
$$

(as approximated by Eq. (1)), and found no significant difference in classification performance; this is consistent with (McCullagh \& Nelder, 1989; Friedman, Geiger, \& Goldszmidt, 1997; Binder et al., 1997). Our work therefore focuses on learners that attempt to maximize $\mathrm{LCL}_{P}(\Theta)$.

While Eq. (1)'s $\widehat{\mathrm{LCL}}^{(S)}(\Theta)$ formula closely resembles the (empirical) "log likelihood" function

$$
\widehat{\mathrm{LL}}^{(S)}(\Theta)=\frac{1}{|S|} \sum_{\langle\mathbf{e}, c\rangle \in S} \log \left(P_{\Theta}(c, \mathbf{e})\right)
$$

used by many BN-learning algorithms, there are some critical differences. Of course,

$$
\widehat{\mathrm{LL}}^{(S)}(\Theta)=\frac{1}{|S|}\left[\sum_{\langle c, \mathbf{e}\rangle \in S} \log \left(P_{\Theta}(c \mid \mathbf{e})\right)+\sum_{\langle c, \mathbf{e}\rangle \in S} \log \left(P_{\Theta}(\mathbf{e})\right)\right]
$$

where the first term resembles our $\widehat{\mathrm{LCL}}(\cdot)$ score, which related to how well our network will answer the relevant queries, while the second term is irrelevant to our task (Friedman, Geiger, \& Goldszmidt, 1997). This means a BN $\Theta_{\alpha}$ that does poorly wrt the first " $\widehat{\mathrm{LCL}}(\cdot)$-like" term may be preferred to a $\Theta_{\beta}$ that does better-i.e., it is possible that $\widehat{\mathrm{LL}}\left(\Theta_{\alpha}\right)>\widehat{\mathrm{LL}}\left(\Theta_{\beta}\right)$, while $\widehat{\mathrm{LCL}}\left(\Theta_{\alpha}\right)<\widehat{\mathrm{LCL}}\left(\Theta_{\beta}\right)$. (Section 5.3 provides other arguments explaining why our $\widehat{\mathrm{LCL}}(\cdot)$ based approach may work better than the $\widehat{\mathrm{LL}}(\cdot)$-based approaches; and Section 6 surveys other relevant literature.)

# 3. Theoretical analysis 

How many "labeled instances" are enough-i.e., given any values $\epsilon, \delta>0$, how many labeled instances are needed to insure that, with probability at least $1-\delta$, an algorithm can produce a classifier that is within $\epsilon$ of optimal? While we believe there are comprehensive general bounds, our specific results require the relatively benign technical restriction that all CPtable entries must be bounded away from 0 . That is, for any $\gamma>0$, let

$$
\mathcal{B N}_{\Theta \geq \gamma} G=\left\{\Theta \in[0,1]^{K} \mid \forall \theta_{d \mid \pi} \in \Theta, \theta_{d \mid \pi} \geq \gamma\right\}
$$

be the subset of parameters (appropriate for the $K$-parameter belief net structure $G$ ) whose CPtable values are all at least $\gamma .^{3}$ We now restrict our attention to these parameters and in

particular, let

$$
\Theta_{G, \Theta \succeq \gamma}^{*}=\operatorname{argmax}\left\{\operatorname{LCL}_{P}(\Theta) \mid \Theta \in \mathcal{B} \mathcal{N}_{\Theta \succeq \gamma}(G)\right\}
$$

be a parameter setting with optimal score among $\mathcal{B} \mathcal{N}_{\Theta \succeq \gamma}(G)$ with respect to the true distribution $P(\cdot)$.

Theorem 1 (Appendix A). Let $G$ be any belief net structure with $K$ CPtable entries $\Theta=\left\{\theta_{d, \mid K}\right\}_{i=1 . . K}$, and let $\hat{\Theta} \in \mathcal{B} \mathcal{N}_{\Theta \succeq \gamma}(G)$ be the $B N$ in $\mathcal{B} \mathcal{N}_{\Theta \succeq \gamma}(G)$ that has maximum empirical log conditional likelihood score (Eq. (1)) with respect to a sample of

$$
18\left(\frac{N \ln \gamma}{\epsilon}\right)^{2}\left[\ln \frac{2}{\delta}+K \ln \frac{6 K}{\gamma \epsilon}\right]=O\left(\frac{N^{2} K}{\epsilon^{2}} \ln \left(\frac{K}{\epsilon \delta}\right) \ln ^{3}\left(\frac{1}{\gamma}\right)\right)
$$

labeled queries drawn from $P(\cdot)$. Then, with probability at least $1-\delta, \hat{\Theta}$ will be no more than $\epsilon$ worse than $\Theta_{G, \Theta \succeq \gamma}^{*}$-i.e.,

$$
P\left(L C L_{P}(\hat{\Theta}) \leq L C L_{P}\left(\Theta_{G, \Theta \succeq \gamma}^{*}\right)-\epsilon\right) \leq \delta
$$

A virtually identical proof shows that this same result holds when dealing with another approximation to the $0 / 1$ error, err $(\Theta)$, viz.,

$$
\operatorname{MSE}(\Theta)=\sum_{(\mathbf{e}, c)} P(\mathbf{e}, c) \times\left[P_{\Theta}(c \mid \mathbf{e})-P(c \mid \mathbf{e})\right]^{2}
$$

rather than $\operatorname{LCL}(\cdot)$.
For comparison, Dasgupta (1997, Section 5) proves that

$$
O\left(\frac{N^{2} K}{\epsilon^{2}} \ln \left(\frac{K}{\epsilon \delta}\right) \ln ^{3}(N) \ln ^{2}\left(\frac{1}{\epsilon}\right)\right)
$$

complete tuples ${ }^{4}$ are sufficient to learn the parameters to a fixed structure that are with $\epsilon$ of the optimal likelihood (Eq. (5)). While comparing upper bounds is only suggestive, it is interesting to note that, ignoring the $\ln ^{\ell}(\cdot)$ terms for $\ell>1$, these bounds are asymptotically identical.

One asymmetry is that only our Eq. (8) bound includes the $\gamma$ term, which corresponds to the smallest CPtable entry allowed. While Dasgupta (1997) (following Abe, Takeuchi, \& Warmuth, 1991) can avoid this term by "tilting" the empirical distribution, this trick does not apply in our discriminative task: Our task inherently involves computing conditional likelihood, which requires dividing by some CPtable values, which is problematic when these values are near 0 . This observation also means our proof is not an immediate application of the standard PAC-learning approaches. Of course, our sample complexity

remains polynomial in the size $(N, K)$ of the belief net even if this $\gamma$ is exponentially small, $\gamma=O\left(1 / 2^{N}\right)$.
Note finally that the parameters that optimize (or nearly optimize) likelihood will not necessarily optimize our objective of conditional likelihood; this means Eq. (10) describes the convergence to parameters that are typically inferior to the ones associated with Eq. (1), especially when the structure is wrong; see Ng and Jordan (2001).
The second question is computational: How hard is it to find these best parameters values, given this sufficiently large sample. Here, the news is mixed.
On the positive side, Roos et al. (2005) show this task corresponds to a convex optimization problem when the data is complete and the structure $G$ satisfies certain specified properties; this implies a polynomial algorithm can find the values of the CPtables of $G$ whose (empirical) conditional likelihood (Eq. (1)) is within $\epsilon$ of optimal (Nesterov \& Nemirovskii, 1994; Boyd \& Vandenberghe, 2004). They show that these properties hold for Naïve-bayes and TAN structures (see Section 5).
Unfortunately...

Theorem 2. It is NP-hard to find the values for the CPtables of a fixed BN-structure that produce the largest (empirical) conditional likelihood (Eq. (1)) for a given incomplete sample. ${ }^{5}$

We do not know the complexity of this task for arbitrary structures, given complete data.

# 4. ELR learning algorithm 

Given the intractability of computing the optimal CPtable entries in general, we defined a simple gradient-ascent algorithm, ELR, that attempts to improve the empirical score $\widehat{\mathrm{LCL}}(\Theta)$ by changing the values of each CPtable entry $\theta_{d \mid \mathbf{f}}$. (Of course, this will only find, at best, a local optimum.) To incorporate the constraints $\theta_{d \mid \mathbf{f}} \geq 0$ and $\sum_{d} \theta_{d \mid \mathbf{f}}=1$, we used the different set of parameters, " $\beta_{d \mid \mathbf{f}}$ ", satisfying

$$
\theta_{d \mid \mathbf{f}}=\frac{e^{\beta_{d \mid \mathbf{f}}}}{\sum_{d^{\prime}} e^{\beta_{d^{\prime} \mid \mathbf{f}}}}
$$

As the $\beta_{1} \mathrm{~s}$ sweep over the reals, the corresponding $\theta_{d_{1} \mid \mathbf{f}}$ 's will satisfy the appropriate constraints. (In the naïve-bayes case, this corresponds to what many logistic regression algorithms would do, albeit with different parameters (Jordan, 1995): Find $\alpha, \chi$ that optimize $P_{\alpha, \chi}(C=c \mid \mathbf{E}=\mathbf{e})=e^{\alpha_{c}+\chi_{\mathbf{e}} \cdot \mathbf{e}} / \sum_{j} e^{\alpha_{j}+\chi_{\mathbf{j}} \cdot \mathbf{e}} .{ }^{6}$ Recall that our goal is a more general algorithm-one that can deal with arbitrary structures; see Eq. (2).

Like all such algorithms, ELR is basically
Initialize $\beta^{(0)}$
For $k=1 . . m$

$$
\beta^{(k+1)}:=\beta^{(k)}+\alpha^{(k)} \times \mathbf{d}^{(k)}
$$

where $\beta^{(k)}$ represents the set of parameters at iteration $k$. In a simple gradient ascent approach, we would set $\mathbf{d}^{(k)}$ to be the total derivative with respect to the given set of labeled queries, $\nabla \widehat{L C L}=\left\langle\frac{\partial \widehat{\mathrm{CL}}^{(k)}(\Theta)}{\partial \beta_{d \mid \mathbf{f}}}\right\rangle_{d, \mathbf{f}}$, where each element of the vector is the sum of the individual derivatives from each labeled training case $\langle\mathbf{e} ; c\rangle$ :

$$
\frac{\partial \widehat{\mathrm{CL}}^{(S)}(\Theta)}{\partial \beta_{d \mid \mathbf{f}}}=\sum_{\langle\mathbf{e}, c\rangle \in S} \frac{\partial \widehat{\mathrm{CL}}^{(|\mathbf{e}, c\rangle)}(\Theta)}{\partial \beta_{d \mid \mathbf{f}}}
$$

Proposition 3 (Greiner, Grove, \& Schuurmans, 1997; Darwiche, 2000; ESM(A)). For any labeled training instance $\langle\mathbf{e}, c\rangle$ and each "softmax" parameter $\beta_{d \mid \mathbf{f}}$,

$$
\frac{\partial \widehat{\mathrm{CL}}^{(|\mathbf{e}, c\rangle)}(\Theta))}{\partial \beta_{d \mid \mathbf{f}}}=\left[P_{\Theta}(d, \mathbf{f} \mid \mathbf{e}, c)-P_{\Theta}(d, \mathbf{f} \mid \mathbf{e})\right]-\theta_{d \mid \mathbf{f}}\left[P_{\Theta}(\mathbf{f} \mid c, \mathbf{e})-P_{\Theta}(\mathbf{f} \mid \mathbf{e})\right]
$$

Notice this expression is well-defined for any set of evidence variables $\mathbf{E}$-which can be all "non-query" variables (corresponding to a complete data tuple), or any subset, including the empty $\mathbf{E}=\{ \}$.

To work effectively, ELR incorporates four instantiations/modifications to the basic gradient ascent idea, dealing with

1. the initial values $\beta^{(0)}$ ("plug-in parameters"),
2. the direction of the modification $\mathbf{d}^{(k)}$ (conjugate gradient),
3. the magnitude of the change $\alpha^{(k)}$ (line search) and
4. the stopping criteria $m$ ("cross tuning").

Minka (2001) has shown that the middle two ideas, conjugate gradient and line-search (Press et al., 2002), are effective for the standard logistic regression task.

Begin with plug-in parameters. We must first initialize the parameters, $\beta^{(0)}$. One common approach is to set $\beta^{(0)}$ to small, randomly selected, values; another is to begin with the values specified by the generative approach-i.e., using frequency estimates (0FE; Eq. (13)) in the complete data case, and a simple variant otherwise (see Section 5.1.3). Our empirical evidence shows that this second approach works better, especially for small samples. These easy-to-compute generative starting values are often used to initialize parameters for discriminative tasks, and called "plug-in parameters" (Ripley, 1996).

Conjugate gradient. Standard gradient ascent algorithms may require a great many iterations, especially for functions that have long, narrow valley structures. The conjugate gradient method addresses this problem by descending along conjugate directions, rather than simply the local gradient. As this means that the directions that have already been

optimized, stay optimized, this method often requires far fewer steps uphill to reach the local optimum (Hagan, Demuth, \& Beale, 1996).

In particular, ELR uses the Polak-Rebiere formula to update its search direction. The initial search direction is given by:

$$
\mathbf{d}^{(0)}:=\nabla \widehat{L C L}_{(0)}
$$

On subsequent iterations,

$$
\mathbf{d}^{(k)}:=\nabla \widehat{L C L}_{(k)}-\frac{\left(\nabla \widehat{L C L}_{(k)}-\nabla \widehat{L C} L_{(k-1)}\right) \cdot \nabla \widehat{L C L}_{(k)}}{\nabla \widehat{L C L}_{(k-1)} \cdot \nabla \widehat{L C L}_{(k-1)}} \mathbf{d}^{(k-1)}
$$

where the "." is the vector dot-product. Hence, the current update direction is formed by "subtracting off" the previous direction from the current derivative.

Line search. ELR will ascend in the $\mathbf{d}^{(k)}$ direction; the next challenge is deciding how far to move-i.e., in computing the $\alpha^{(k)} \in \mathfrak{R}^{+}$within (12).

The good news is, as $\beta=\beta^{(k)}$ and $\mathbf{d}=\mathbf{d}^{(k)}$ are fixed, this is a one-dimensional search: find the $\alpha^{*}$ that maximizes $f(\alpha)=\widehat{\mathrm{LCL}}^{(5)}(\beta+\alpha \times \mathbf{d})$. ELR therefore uses a standard technique, Brent's iterative line search procedure (a hybrid combination of the linear Golden Section search (Hagan, Demuth, \& Beale, 1996) and a quadratic interpolation), which has proven to be very effective at finding the optimal value for $\alpha^{(k)}$ (Bishop, 1998). In essense, this method first finds three $\alpha_{i}$ values, and computes the associated function values $\left.\left\langle\left\langle\alpha_{i}, f\left(\alpha_{i}\right)\right\rangle\right\rangle_{i=1,2,3}$. It then assumes the $f(\cdot)$ function is (locally) quadratic, and so fits this trio of points to a second degree polynomial. It then finds the $\alpha^{*}$ value that minimizes this quadratic, replaces one of the three original $\alpha_{i}$ values with this $\left\langle\alpha^{*}, f\left(\alpha^{*}\right)\right\rangle$ pair, and iterates using the new trio of points. See Bishop (1998) for details.

Cross tuning (stopping time). The final issue is deciding when to stop; i.e., determining the value of $m$ within (12). A naïve algorithm would just compute the training-set error (Eq. (3)) at each iteration, and stop when that error measure appears at a local optimumi.e., when the error appears to be getting larger. The graph in Figure 1 shows both training-set and test-set error on a particular dataset at each iteration. If we used this simple approach, we would stop on the third iteration; the generalization error shows that these parameters are very bad-in fact, they seem almost the worst values!

To avoid this, we use a variant of cross validation, which we call "cross tuning", to estimate the optimal number of iterations. Here, we divide the training data into $\ell=5$ partitions, then for each fold, run the gradient descent for remaining $4 / 5$ of the data, but evaluating the quality of the result (on each iteration) on the fold. (This produces a graph like the "Generalization Error" line in Figure 1.) We then determine, for each fold, when we should have stopped-here, it would be on $k=5$, as that is the global optimum for this fold. We then set $m$ to be the median values over these $\ell$ folds. When using all of the data

![img-0.jpeg](img-0.jpeg)

Figure 1. Comparing Training-Set Error with Test-Set Error, as function of Iteration.
to produce the final $\left\{\beta_{i f} \mid \mathbf{f}\right\}$ values, we iterate exactly $m$ times. $\operatorname{ESM}(\mathrm{B})$ presents empirical evidence that cross-tuning is important, especially for complex models.

# 5. Empirical studies 

The ELR algorithm takes, as arguments, a BN-structure $G=\langle\mathcal{V}, A\rangle$ and a dataset of labeled queries (aka instances) $S=\left\{\left\langle\mathbf{e}_{i}, c_{i}\right\rangle\right\}_{i}$, and returns a value for each CPtable parameter $\theta_{i f} \mid$. To explore its effectiveness, we compared the err( $\cdot$ ) performance of the resulting $\Theta_{\text {ELR }}$ parameters against the results of other algorithms that similarly learn CPtable values for a given structure.

We say a data sample is "complete" if each instance is complete (see Note 4); otherwise it is incomplete. When the data is complete, we compare ELR to the standard "observed frequency estimate" (OFE) approach, which is known to produce the parameters that maximize likelihood (Eq. (5)) for a given structure (Cooper \& Herskovits, 1992). For example, if 75 of the $100 C=1$ instances have $X_{3}=0$, then OFE sets

$$
\theta_{X_{3}=0 \mid C=1}=\frac{\#\left(X_{3}=0, C=1\right)}{\#(C=1)}=\frac{75}{100}
$$

(Some versions use a Laplacian correction to avoid the problems caused by 0 probability events.) When the data is incomplete, we compare ELR to the standard Expectation Maximization algorithm EM (Dempster, Laird, \& Rubin, 1977; Lauritzen, 1995; Heckerman, 1998) and to APN (Binder et al., 1997), which ascends to parameter values whose likelihood is locally optimal. ${ }^{7}$

Traditional wisdom holds that discriminative learning (ELR) is most relevant (i.e., better than generative learning: OFE, APN, EM) when this underlying model $G=\langle\mathcal{V}, A\rangle$ is "wrong", that is, not an I-map of the true distribution $T$-which here means the graph structure does not include some essential arcs (Pearl, 1988). The situation, which we denote " $G<T$ ", is fairly common as many learners consider only structures as simple as naïve-bayes, or the class of TAN structures (defined below), which are typically much simpler than $T .^{8}$

Section 5.1 deals with this situation, considering both the complete and incomplete data cases. Section 5.2 then considers another standard situation: where we employ a structurelearning algorithm to produce a structure that is similar to the truth; i.e., where $G \approx T$. Here, we use the PowerConstructor system (Cheng et al., 2002; Cheng \& Greiner, 1999) for the first step (to learn the structure), then compare the relative effectiveness of algorithms for finding parameters for this structure. Finally, Section 5.3 summarizes all of these empirical results.

Notation. The notation "NB + ELR" will refer to the NB structure, whose parameters are learned using ELR; in general, we will use $x+y$ to refer to the system produced when the $y$ algorithm is used to produce the parameter for the $x$ structure. Below we will compare various pairs of learners, in each case over a common dataset; we will therefore use a onesided paired $t$-test (Mitchell, 1997). When this result is significant at the $\rho<0.05$ level, we will write $\alpha \Leftarrow_{(p<\rho)} \beta$-e.g., we will soon see NB + ELR $\Leftarrow_{(p<0.005)}$ NB + OFE. For values larger than 0.05 , we will use the notation $\alpha \leftarrow_{(p<\rho)} \beta$. (That is, we regard $p<0.05$ as the cut-off for statistical significance.) Note the arrow points to the learner that appears to be better. ${ }^{9}$

While our main emphasis is comparing $x+$ ELR to $x+$ OFE (and to $x+$ APN and $x+$ EM) for various structures $x$, where relevant we will also compare across structure classes; e.g., comparing $x+$ ELR to $z+$ ELR for different structures $x$ and $z$.

# 5.1. Model is simpler than the truth $(G<T)$ 

Section 5.1.1 (resp., Section 5.1.2) compares algorithms for learning the parameters for a naïve-bayes model (resp., a TAN model) given complete data; Section 5.1.3 then considers learning these models given incomplete data. ${ }^{10}$
5.1.1. Naïve-bayes-Complete, real world data. Our first experiments deal with the simplest situation: learning the Naïve-bayes parameters from complete data. Recall that the Naïve-bayes structure requires that the attributes are independent given the class label; see Figure 2(a).

We compared the relative effectiveness of ELR with various other classifiers, over the same 25 datasets that Friedman, Geiger, \& Goldszmidt (1997) used for their comparisons: 23 from UCIrvine repository (Blake \& Merz, 2000), plus "MOFN-3-7-10" and "CORRAL",
![img-1.jpeg](img-1.jpeg)

Figure 2. (a) Naïve-bayes structure. (b) TAN structure (Friedman, Geiger, \& Goldszmidt, 1997, Figure 3). (c) Arbitrary GBN structure. (Note: all figures are numbered (a), (b), ... from left to right.)

which were developed by Kohavi and John (1997) to study feature selection; see ESM(C; Table II) which also specifies how we computed our accuracy values-based on 5-fold cross validation for small datasets, and the holdout method for large datasets (Kohavi, 1995). To deal with continuous variables, we implemented supervised entropy discretization (Fayyad and Irani, 1993). ESM(C; Table III) succinctly summarizes the results.

We use the CHESS dataset ( 36 binary or ternary attributes) to illustrate the basic behaviour of the algorithms. Figure 3(a) shows the performance, on this dataset, of our NB + ELR (a.k.a. "Naïve-bayes structure + ELR instantiation") system, versus the "standard" NB + OFE, which uses OFE to instantiate the parameters. We see that ELR is consistently more accurate than OFE, for any size training sample. We also see how quickly ELR converges to the best performance.

Figure 4(a) provides a more comprehensive comparison, across all 25 datasets. (Each point below the $x=y$ line is a dataset where NB + ELR was better than the other approachhere NB + OFE. The lines also express the 1 standard-deviation error bars in each dimension. ${ }^{11}$ ) As suggested by this plot, NB + ELR is significantly better than NB + OFE at the $p<0.005$ level.
![img-2.jpeg](img-2.jpeg)

Figure 3. CHESS domain: (a) ELR vs OFE, complete data, structure is "incorrect" (naïve-bayes); (b) ELR vs EM, APN, incomplete data, structure is "incorrect" (naïve-bayes); (c) ELR vs OFE, complete data, structure is " $\approx$ correct" (POWERCONSTRUCTOR).
![img-3.jpeg](img-3.jpeg)

Figure 4. Comparing NB+ELR with (a) NB+OFE; (b) TAN+OFE.

![img-4.jpeg](img-4.jpeg)

Figure 5. Complete data: Comparing TAN + ELR vs (a) NB + ELR and (b) TAN + OFE.
5.1.2. TAN—Complete, real world data. We next considered TAN ("tree augmented naïvebayes") structures (Friedman, Geiger, \& Goldszmidt, 1997), which include a link from the classification node down to each attribute and, if we ignore those class-to-attribute links, the remaining links, connecting attributes to each other, form a tree; see Figure 2(b). (Hence this representation allows each attribute to have at most one "attribute parent", and so this class of structures strictly generalize Naïve-bayes.) Friedman, Geiger, and Goldszmidt (1997) provide an efficient algorithm for learning such TAN structures given complete data, based on Chow and Liu (1968): first compute the mutual information between each pair of attributes, conditioned on the class variable, then find the minimum-weighted spanning tree within this complete graph of the attributes. (Each mutual information quantity is based on the empirical sample.) They prove that the resulting structure maximizes the likelihood of the data, over all possible TAN structures-n.b., this is optimizing a generative measure.

Figure 4(b) compares NB + ELR to TAN + OFE. We see that ELR, even when handicapped with the simple NB structure, performs about as well as OFE on TAN structures. Of course, the limitations of the NB structure may explain the poor performance of NB + ELR on some data. For example, in the CORRAL dataset, as the class is a function of four interrelated attributes, one must connect these attributes to predict the class. As Naïve-bayes permits no such connection, Naïve-bayes-based classifiers performed poorly on this data. Of course, as TAN allows more expressive structures, it has a significant advantage here. It is interesting to note that our NB + ELR is still comparable to TAN + OFE, in general.

Would we do yet better by using ELR to instantiate TAN structures? While Figure 5(a) suggests that TAN + ELR is slightly better than NB + ELR, this is not significant. However, Figure 5(b) shows that TAN + ELR does consistently better than TAN + OFE-at a $p<0.025$ level. We found that TAN + ELR did perfectly on the the CORRAL dataset, which NB + ELR found problematic.
5.1.3. NB, TAN—Incomplete, real world data. All of the above studies used complete data. We next explored how well ELR could instantiate the Naïve-bayes structure, using incomplete data.

Here, we used the datasets investigated above, but modified by randomly removing the value of each attribute, within each instance, with probability 0.25 . (Hence, this data is

![img-5.jpeg](img-5.jpeg)

Figure 6. Incomplete data: Comparing NB + ELR vs (a) NB + APN and (b) NB + EM.
"missing completely at random", MCAR (Little \& Rubin, 1987).) We then compared ELR to the standard "missing-data" learning algorithms, APN and EM. In each case-for ELR, APN and EM-we initialize the parameters using the obvious variant of OFE that considers, for $\beta_{d R}$, only the records that include values for the relevant node and all of its parents $\{D\} \cup \mathbf{F}$.

Here, we first learned the parameters for the Naïve-bayes structure; Figure 3(b) shows the learning curve for the CHESS domain, comparing ELR to APN and EM. We see that ELR does better for essentially every sample size. We also compared these algorithms over all of the 25 datasets; see Figures 6(a) and 6(b) for ELR vs APN and ELR vs EM, respectively. As shown, ELR does consistently better-in each case, at the $p<0.025$ level.

We next tried to learn the parameters for a TAN structure. Recall the standard TANlearning algorithm uses the mutual information between each pair of attributes, conditioned on the class variable. This is straightforward to compute when given complete information. Here, given incomplete data, we approximate mutual information between attributes $A_{i}$ and $A_{j}$ by simply ignoring the records that do not have values for both of these attributes. Figures 7(a) and 7(b) compare TAN + ELR to TAN + APN and to TAN + EM. We see that these systems are roughly equivalent: while TAN + ELR appears slightly better than TAN + EM, this is not significant (only at $p<0.25$ ); similarly there is no significant difference between TAN + ELR and TAN + APN. Finally, we compared NB + ELR to TAN + ELR (Figure 7(c)), but found no significant difference here either.
![img-6.jpeg](img-6.jpeg)

Figure 7. Incomplete data: Comparing TAN + ELR with (a) TAN + APN; (b) TAN + EM and (c) NB + ELR.

ESM(C; Table IV) presents all of our empirical results related to missing data. We also compared these parameter learners on 20 other UCInvine datasets that are already missing datapoints. Our results here were consistent: NB + ELR was significantly better than NB + EM and $\mathrm{NB}+\mathrm{APN}-\mathrm{NB}+\mathrm{ELR} \Leftarrow_{(p<0.0056)} \mathrm{NB}+\mathrm{EM}, \mathrm{NB}+\mathrm{ELR} \Leftarrow_{(p<0.026)} \mathrm{NB}+\mathrm{APN}$ —but there was no statistical separation difference between TAN + ELR and either TAN + EM or TAN + APNTAN + ELR $\leftarrow_{(p<0.083)}$ TAN +EM and TAN +ELR $\leftarrow_{(p<0.078)}$ TAN + APN. We provide further details in $\operatorname{ESM}(\mathrm{D})$.

# 5.2. Model approximates the truth $(G \approx T)$ 

The previous section considered learners that were constrained to consider only some limited class of structures, such as NB or TAN. Other learners are allowed to first learn an arbitrary BN structure-seeking one that matches the underlying distribution-before learning the parameters of that structure, using ELR or OFE, etc. There are a number of algorithms for learning these BN structures, each of which will typically produce a structure that is close to correct. This paper considers the POWERCONSTRUCTOR system (Cheng et al., 2002; Cheng \& Greiner, 1999), which uses mutual information tests to construct BNstructures from complete tuples. This algorithm is guaranteed to converge to the correct belief net structure, given enough data (and some other relatively benign assumptions). We will refer to the resulting POWERCONSTRUCTOR-produced structure as a "General Belief Net", or GBN; see Figure 2(c). This section explores the effectiveness of beginning with such learned structures.

For each of the 25 datasets, we first used POWERCONSTRUCTOR to produce a structure for the given dataset, given all available (non-hold-out) data; we then asked ELR (resp., OFE) to find best parameters for this (presumably near optimal) structure using the same non-hold-out data, and observed how well the resulting system performs on the held-out data.

Section 5.2.1 compares GBN +ELR to GBN + OFE; Section 5.2.2 compares GBN + ELR to simpler models instantiated using ELR; and Section 5.2.3 compares the OFE-instantiation of GBN to ELR-instantiations of simpler models. Section 5.2.4 investigates different algorithms for learning parameters (for these GBN structures) from incomplete data.
5.2.1. GBN + ELR vs GBN + OFE. Figure 8(a) shows that GBN + ELR is only insignificantly better than GBN + OFE: GBN + ELR $\leftarrow_{(p<0.2)}$ GBN + OFE. Hence, when considering structures that match the underlying distribution, there appears to be little difference between OFE and ELR.
5.2.2. GBN + ELR vs NB + ELR, TAN + ELR. The main purpose of our studies was to see how $x+$ ELR compares to $x+$ OFE (and to $x+\mathrm{EM} / \mathrm{OFE}$ ), for various classes of commonlyused structures $x$. As a side issue, we also considered some cross-structure comparisons. In particular, given that POWERCONSTRUCTOR had no prior constraints on the structures it can produce, it has the potential of producing classifiers superior to the ones produced by the constrained NB or TAN systems. However, when we compared GBN +ELR

![img-7.jpeg](img-7.jpeg)

Figure 8. Comparing GBN + ELR vs (a) GBN + OFE;(b) NB + ELR and (c) TAN + ELR.
to NB + ELR (Figure 8(b)), and to TAN + ELR (Figure 8(c)), we found that the simpler structures actually produced better classifiers than GBN did-NB + ELR $\Leftarrow_{(p<0.01)}$ GBN + ELR and TAN + ELR $\Leftarrow_{(p<0.008)}$ GBN + ELR.

There are several possible reasons for this. First, the optimization task for GBN (unlike the ones for NB and TAN) is not convex, meaning it could have local, non-global maxima (Roos et al., 2005). The fact that GBN + ELR appears comparable to GBN + OFE suggests that this is not a major issue.

Another possibility is that the GBN structure might not be good for the classification task: POWERCONSTRUCTOR is seeking a good model of the underlying distribution, but might fail. (Recall its guarantee is asymptotic, and we have only a finite sample). Moreover, even if it obtained a good approximation to the underlying distribution, this might not produce a good classifier; see the arguments presented in Section 2. ${ }^{12}$ (Of course, as our goal is to compare $x+$ ELR to $x+$ OFE over commonly used classes $x$, it does not really matter whether POWERCONSTRUCTOR provided a good structure $x$ or not.)
5.2.3. GBN + OFE vs NB + ELR, TAN + ELR. One approach to learning a good belief net (classifier) is to first find a good structure, then instantiate this structure using the trivial OFE algorithm. The first step can be hard-e.g., NP-hard if seeking the structure that maximizes the BIC score (Chickering, Geiger, \& Heckerman, 1994). ${ }^{13}$ Another approach, suggested by our analysis, is to use a simple structure, such as NB or TAN, but then spend resources finding the best parameters, using ELR.

We therefore compared GBN + OFE to NB + ELR (Figure 9) and found NB + ELR to be significantly better: NB + ELR $\Leftarrow_{(p<0.03)}$ GBN + OFE. Moreover, TAN + ELR is yet stronger: TAN $+\mathrm{ELR} \Leftarrow_{(p<0.008)} \mathrm{GBN}+\mathrm{OFE}$.

Table 1 presents a succinct summary of the results on the UCI data, over all 25 datasets. (Note this repeats many of the results from the previous sections.) The rows and columns are ordered based on our expectation that most of the entries would be $\uparrow$ 's or $\uparrow$ 's-i.e., the learners are arranged in the order of (anticipated) decreasing performance. We see some exceptions, but only when we cross structure classes; see above discussion.
5.2.4. GBN $+x$ vs other classifiers, with incomplete data. This section investigates the effectiveness of learning the parameters for GBN structures, from incomplete training data.

Table 1. Comparison of Different Parameter Learners-Complete (UCI) Data; all 25 datasets.


Note: Each $\langle i, j\rangle$ entry consists of both an arrow that points to the superior learner (using a double arrow $\Uparrow$ or $\Leftarrow$ if this is significant, and a single arrow $\uparrow$ or $\leftarrow$ otherwise); and the associated $p$-value in parentheses.
![img-8.jpeg](img-8.jpeg)

Figure 9. Comparing (a) GBN + OFE vs NB + ELR and (b) GBN + OFE vs TAN + ELR

As PowerConstructor is designed for complete data, we actually built each of the structures using complete data. We did this once, using all of the available data. ${ }^{14}$

To produce the data used for learning and evaluating the parameters, we then removed the values of each evidence attribute for each tuple, with probability 0.25 -so again we are dealing with MCAR data (Little \& Rubin, 1987).

The overall results appear in Table 2, where again we expected the majority of the entries to be $\Uparrow$ 's or $\uparrow$ 's. Most importantly, for each class $x$, we see that $x+$ ELR is never significantly worse than either $x+$ APN or $x+$ EM, and sometimes it is significantly better. The fact that both TAN $+y$ and NB + ELR appear uniformly better than GBN $+y$, is consistent with the case for complete data; see Section 5.2.2.

# 5.3. Discussion 

This section has presented a number of empirical results, all in the context of producing a good belief-net based classifiers for a fixed structure. The main take-home messages are...

- The discriminative learner ELR system works effectively in essentially every standard situation: Given complete data, it is at least as good as, and often superior to, OFE (Table 1)

Table 2. Comparison of Parameter Learners-InComplete (UCI) Data; all 25 datasets.


and given incomplete data, it is at least as good as, and often superior to, APN and EM (Table 2). ${ }^{15}$

- While we typically found more expressive models produced better classifiers (i.e., for each parameter-learner $z, \mathrm{GBN}+z$ was better than $\mathrm{TAN}+z$, and $\mathrm{TAN}+z$ was better than $\mathrm{NB}+z$ ), this was not universal; see discussion in Section 5.2.2.

Why ELR works well. We found that ELR worked effectively in many situations, and it was especially advantageous (i.e., typically better than the alternative ways to instantiate parameters) when the BN-structure was incorrect-i.e., when it is not an $I$-map of the underlying distribution by incorrectly claiming that two dependent variables are independent (Pearl, 1988). This is a very common situation, as many BN-learners will produce incorrect structures, either because they are conservative in adding new arcs (to avoid overfitting the data (Heckerman, 1998; Van Allen \& Greiner, 2000)), or because they are considering only a restricted class of structures (e.g., Naïve-bayes (Duda \& Hart, 1973), poly-tree (Chow \& Liu, 1968; Pearl, 1988), TAN (Friedman, Geiger, \& Goldszmidt, 1997), etc.) that is not guaranteed to contain the correct structure.

To understand why a bad structure is problematic for OFE, note that when OFE is seeking the parameter $\theta_{G \mathbf{f}}$, it is constrained to match the local empirical distribution, corresponding to $\#(D=d, \mathbf{F}=\mathbf{f}) / \#(\mathbf{F}=\mathbf{f})$. Hence, if the given structure $G$ is incorrect, the resulting instantiated belief net need not be a good model of the true tuple distribution, and so may return incorrect values for the queries. By contrast, the ELR algorithm is not as constrained by the specific structure, and so may be able to produce parameters that yield fairly accurate answers, even if the structure is sub-optimal. (See the standard comparison between discriminative versus generative training, overviewed in Section 6.)

Other learners. We also compared ELR to various other learning algorithms, including SVMs, over these datasets. We found that ELR appeared comparable with several other standard learning algorithms, and superior to some. See $\operatorname{ESM}(\mathrm{E})$ for details, which also repeats the results from Friedman, Geiger, \& Goldszmidt (1997) and Grossman \& Domingos (2004). That webpage also provides other information about the experiments, including timing information.

# 6. Related results 

There are a number of other results related to learning belief nets. Much of this work focuses on learning the best structure, either for a general belief net, or within the context of some specific class of structures (e.g., TAN-structures, or selective Naïve-bayes); see (Heckerman, 1998; Buntine, 1996) for extensive tutorials. By contrast, this paper suggests a way to learn the parameters for a given structure.

While most of those structure-learning systems also learn the parameters, essentially all use the OFE algorithm (Eq. (13)). This is well motivated in the generative situation, as these parameter values do optimize the likelihood of the data (Cooper \& Herskovits, 1992).

As noted earlier, however, our goal is different: as we are seeking the optimal classi-fier-i.e., discriminative learning. There have been many other systems that also considered discriminative learning of belief nets (Kontkanen et al., 1999; Jaakkola, Meila, \& Jebara, 2000; Friedman, Geiger, \& Goldszmidt, 1997; Cheng \& Greiner, 1999; Grossman \& Domingos, 2004). Those research projects, like their generative counterparts, focused on learning structures; and usually used OFE to instantiate the resulting parameters.

As we saw above, when the model is wrong, the OFE-based parameters can produce inferior classifiers. Many researchers have employed tricks to improve the parameters; e.g., tractable Bayesian model averaging of TAN (Cerquides \& de Mántaras, 2003), and exact model averaging of naïve-bayes (Dash \& Cooper, 2002). Our approach is different, as we explicitly seek the parameters of the BN model that maximize conditional likelihood.

Our results also relate closely to the work on discriminant learning of Hidden Markov Models (HMMs) (Schlüter et al., 1997; Chou, Juang, \& Lee, 1992). In particular, much of that work uses "Generalized Probabilistic Descent", which resembles our ELR system by descending along the derivative of the parameters, to maximize the conditional likelihood of the hypothesis (which typically correspond to specific words) given the observationswhich they call "Maximimum Mutual Information" criterion. We differ by considering arbitrary structures, and evaluating based on classification error.

Edwards and Lauritzen (2001) proposed the TM algorithm for maximizing conditional likelihood function, when the corresponding (unconditional) likelihood function is more easily maximized. They have found the algorithm is a useful tool in complex CG-regression models, which are the building blocks for graphical chain models, as well as in other situations (Sundberg, 2002). Their TM algorithm is similar to the EM algorithm as it also alternates between maximization of a function related to the true likelihood function, but differs by being applied to the complete data case and by augmenting the parameters rather than the data.

This issue relates directly to the large literature on discriminative learning in general; see (Cox \& Snell, 1989; Jordan, 1995; Ripley, 1996). One standard model is Linear Discriminant Analysis (LDA), which typically assumes $P(\mathbf{E} \mid C=c)$ is multivariate normal-i.e., $P(\mathbf{E} \mid C=c) \sim \mathcal{N}\left(\mu_{c}, \Sigma\right)$ where each $\mu_{c}$ mean can depend on the class $C=c$, but the covariance matrix $\Sigma$ is the same for all classes. The LDA system then estimates the relevant $\left\{\mu_{c}, \Sigma, \hat{P}(C=c)\right\}$ parameters from a body of data, seeking the ones that maximize the likelihood of the data relevant to those parameters. Given these parameters, we can then use Bayes Rule to compute the conditional distribution of $P\left(C \mid \mathbf{E}=\mathbf{e}^{\prime}\right)$ given new evidence $\mathbf{E}=\mathbf{e}^{\prime}$.

We can view LDA (like OFE/APN/EH) as being generative (aka "causal" or "class- conditional" (Jordan, 1995), or "sampling" (Dawid, 1976)), as it is attempting to fit parameters for the entire joint distribution, while our ELR is discriminative (aka "diagnostic", "predictive" (Jordan, 1995)), as it focuses only on the conditional probabilities.

Our results echo the common wisdom obtained by the previous analyses of discriminative systems. In particular, (1) accuracy: discriminative training typically produces more accurate classifiers than generative training; (2) robustness: typically discriminative systems are more robust against incorrect models than generative ones; (3) efficiency: generative can be more efficient than discriminative (compare the efficient OFE with the iterative ELR).

The work reported in this paper has significant differences from most of those earlier analyses. First, we are dealing with a different underlying model, based on discrete variables (rather than continuous, say normally distributed, ones), in the context of a specified belief net structure, which corresponds to a given set of independency claims. We also describe the inherent computational complexity of this task, produce algorithms specific to our task, and provide empirical studies to demonstrate that our algorithm works effectively, given either complete or incomplete training data.

Our companion paper (Greiner, Grove, \& Schuurmans, 1997) also considers learning the parameters of a given structure towards optimizing performance on a distribution of queries. Our results here differ, as we are considering a different learning model: That earlier work tries to minimize the squared-error score, a variant of Eq. (9) that is based on two different types of samples - one over tuples, to estimate $P(C \mid \mathbf{E})$, and the other over queries, to estimate the probability of seeing each "What is $P(C \mid \mathbf{E}=\mathbf{e})$ ?" query. By contrast, the current paper tries to minimize classification error (Eq. (3)) by seeking the optimal "conditional likelihood" score (Eq. (4)), wrt a single sample of labeled instances. Moreover, our current paper includes new theoretical results, a different algorithm, and completely new empirical data.

# 7. Conclusions 

Future work. Section 3 notes that, in some situations (a specified class of structures, when given complete data), interior point methods can find the parameters that optimize conditional likelihood, in polynomial time. Of course, it is not clear whether these $\mathrm{LCL}(\cdot)$ optimal parameters will optimize error (Eq. (3)), nor that the algorithm will necessarily be more efficient than ELR. We therefore plan to investigate these methods.

Table 3. Summary of known complexity results.


This paper explores the challenges of finding in the CPtables of a given BN-structure. While this is an important subtask, a general learner should be able to learn that structure as well—perhaps using conditional likelihood as the selection criterion; see Kontkanen et al. (1999) and Jaakkola, Meila, \& Jebara (2000). We plan to investigate ways to synthesize these approaches; see Grossman and Domingos (2004).

There are now several other classes of graphical models, such as Conditional Random Fields (Lafferty, McCallum, \& Pereira, 2001), that may be better adapted to optimizing conditional likelihood. (E.g., as they use undirected arcs, they require only a single normalizing division, rather than one per CPtable row.) While this paper has focused on Belief Nets (as it is typically easier to acquire meaningful structures here, both because they allow users to express their prior knowledge, and because there are a number of algorithms for learning belief net structures), we plan to investigate these other models as well.

Contributions. This paper overviews the task of discriminative learning of belief net parameters for general BN-structures. We first describe this task, and discuss how it extends that standard logistic regression process by applying to arbitrary structures, not just Naïve-bayes-see Eq. (2). Our formal analyses show that, in general, discriminative learners can converge to a classifier optimizing conditional likelihood at essentially the same $O(\cdot)$ sample rate (ignoring polylog terms) as a generative classifier that is optimizing likelihood. ${ }^{16}$ Moreover, it is well-known that discriminative learning can converge to a classifier superior to one learned generatively ( Ng \& Jordan, 2001). We also found that the computational complexities of these two tasks also appear fairly comparable; see Table 3. (This is just the cost of finding good parameters, for a given structure. As this structure is not as critical in our discriminative case, we anticipate further savings in the overall task of learning both structure and parameters.)

We next present an algorithm ELR for our task, and show that ELR works effectively over a variety of situations: when dealing with structures that range from trivial (NB), through lesstrivial (TAN), to complex (ones learned by POWERCONSTRUCTOR). We also show that ELR works well when given incomplete training data. In particular, in essentially every standard situation, we see that ELR is at least as good, and often better, than the other contenders, which seek a good generative methods.

The idea of discriminative learning, especially in the context of belief nets, is only beginning to make in-roads into the general AI community. We hope this paper will help further introduce these ideas to this community, and demonstrate that these algorithms should be used here, as they can work very effectively.

# Appendix A: Proof 

Proof of Theorem 1: As the set $\mathcal{B N}_{\Theta \geq \gamma}(G)$ is uncountably infinite, we cannot simply apply the standard techniques for PAC-learning a finite hypothesis set. We can, however, partition this uncountable space into a finite number $L=L(K, \gamma, \epsilon)$ of sets, such that any two BNs within a partition have similar conditional log-likelihood scores. We can then, in essense, simultaneously estimate the scores of all members of $\mathcal{B N}_{\Theta \geq \gamma}(G)$ if we collect enough instances to estimate the score for one representative of each partition.

Now for the details: Let $\Theta^{(1)}=\left\{\theta_{d, \mid \mathbf{K}}^{(1)}\right\}_{i}$ and $\Theta^{(2)}=\left\{\theta_{d, \mid \mathbf{K}}^{(2)}\right\}_{i}$, be two CPtables in $\mathcal{B N}_{\Theta \geq \gamma}(G)$. We prove below that

$$
\begin{aligned}
& \text { if } \quad \forall i\left|\theta_{d, \mid \mathbf{K}}^{(1)}-\theta_{d, \mid \mathbf{K}}^{(2)}\right| \leq \frac{\gamma \epsilon}{6 K} \\
& \text { then } \quad \forall c, \mathbf{e}\left|\ln \left(P_{\Theta^{(1)}}(c \mid \mathbf{e})\right)-\ln \left(P_{\Theta^{(2)}}(c \mid \mathbf{e})\right)\right| \leq \frac{\epsilon}{6}
\end{aligned}
$$

which implies

$$
\begin{aligned}
\left|\mathrm{LCL}_{P}\left(\Theta^{(1)}\right)-\mathrm{LCL}_{P}\left(\Theta^{(2)}\right)\right| & \leq \frac{\epsilon}{6} \\
\left|\widetilde{\mathrm{LCL}}\left(\Theta^{(1)}\right)-\widetilde{\mathrm{LCL}}\left(\Theta^{(2)}\right)\right| & \leq \frac{\epsilon}{6}
\end{aligned}
$$

Now partition the $\mathcal{B N}_{\Theta \geq \gamma}(G)$ space into $L=\left(\frac{6 K}{\gamma \epsilon}\right)^{K}$ disjoint sets, where any two BNs from any partition will have similar CPtable values, then define the set $R=\left\{\Theta_{i}\right\}_{i}$ to contain one representative from each partition. We prove below that a sample $S$ of size

$$
M\left(\frac{\epsilon}{6}, \frac{\delta}{L}\right)=2\left(\frac{3 N \log \gamma}{\epsilon}\right)^{2} \ln \frac{2 L}{\delta}
$$

is sufficient to estimate each of these single representatives to within $\epsilon / 6$ of correct, with probability of error at most $\delta / L$; i.e., such that, for each $i$,

$$
P\left[\left|\widetilde{\mathrm{LCL}}^{(\delta)}\left(\Theta_{i}\right)-\mathrm{LCL}\left(\Theta_{i}\right)\right|>\frac{\epsilon}{6}\right]<\frac{\delta}{L}
$$

As there are $L$ representatives, the probability that any of the representative's scores are mis-estimated by more than $\epsilon / 6$ is at most $L \frac{\delta}{L}=\delta$.

This allows us to estimate the scores on any $\Theta \in \mathcal{B N}_{\Theta \geq \gamma}(G)$ to within $\epsilon / 2$ : For any $\Theta \in \mathcal{B} \mathcal{N}_{\Theta \geq \gamma}(G)$, let $\Theta^{\prime} \in R$ be the representative in $\Theta$ s partition. Observe

$$
\begin{aligned}
& |\widetilde{\mathrm{LCL}}(\Theta)-\mathrm{LCL}(\Theta)| \\
& \quad \leq\left|\widetilde{\mathrm{LCL}}(\Theta)-\widetilde{\mathrm{LCL}}\left(\Theta^{\prime}\right)\right|+\left|\widetilde{\mathrm{LCL}}\left(\Theta^{\prime}\right)-\mathrm{LCL}\left(\Theta^{\prime}\right)\right|+\left|\mathrm{LCL}\left(\Theta^{\prime}\right)-\mathrm{LCL}(\Theta)\right| \\
& \quad \leq \quad \epsilon / 6 \quad+\quad \epsilon / 6 \quad+\quad \epsilon / 6 \\
& \quad=\quad \epsilon / 2 .
\end{aligned}
$$

which implies that our estimates of the scores of both $\widehat{\Theta}$ and $\Theta^{*}$ are within $\epsilon / 2$, and so

$$
\begin{aligned}
& \mathrm{LCL}(\widehat{\Theta})-\operatorname{LCL}\left(\Theta^{*}\right) \\
& \leq\left|\operatorname{LCL}(\widehat{\Theta})-\widehat{\mathrm{LCL}}(\widehat{\Theta})\right|+\widehat{\mathrm{LCL}}(\widehat{\Theta})-\widehat{\mathrm{LCL}}\left(\Theta^{*}\right)+\left|\widehat{\mathrm{LCL}}\left(\Theta^{*}\right)-\operatorname{LCL}\left(\Theta^{*}\right)\right| \\
& \leq \epsilon / 2+0+\epsilon / 2
\end{aligned}
$$

To complete the proof, we need only prove Eqs. (14) and (15). For Eq. (1): Consider the sequence of $\mathrm{BNs} \Theta_{0}, \Theta_{1}, \ldots, \Theta_{K}$ where the first $i$ of $\Theta_{i}$ 's CPtables come from $\Theta^{(1)}$, and the remaining from $\Theta^{(2)}$ - i.e.,

$$
\Theta+i=\left\{\theta_{d_{1} \mid \mathbf{f}_{1}}^{(1)}, \ldots, \theta_{d_{i} \mid \mathbf{f}_{i}}^{(1)}, \theta_{d_{i+1} \mid \mathbf{f}_{i+1}}^{(2)}, \ldots, \theta_{d_{K} \mid \mathbf{f}_{K}}^{(2)}\right\}
$$

Now observe

$$
\left|\ln \left(P_{\Theta^{(2)}}(c \mid \mathbf{e})\right)-\ln \left(P_{\Theta^{(2)}}(c \mid \mathbf{e})\right)\right| \leq \sum_{i=1}^{K}\left|\ln \left(P_{\Theta_{i}}(c \mid \mathbf{e})\right)-\ln \left(P_{\Theta_{i-1}}(c \mid \mathbf{e})\right)\right|
$$

where each $\left|\ln \left(P_{\Theta_{i}}(c \mid \mathbf{e})\right)-\ln \left(P_{\Theta_{i-1}}(c \mid \mathbf{e})\right)\right|$ is based on changing a single CPtable entry. We therefore need only show $\left|\ln \left(P_{\Theta_{i}}(c \mid \mathbf{e})\right)-\ln \left(P_{\Theta_{i-1}}(c \mid \mathbf{e})\right)\right| \leq \frac{\epsilon}{6 K}$. For any value of $z=\theta_{d_{i} \mid \mathbf{f}_{i}}$, let $f(z)=\ln \left(P_{\Theta[z]}(c \mid \mathbf{e})\right)$, where $\Theta[z]$ be the BN whose first $i-1$ CPtable entries come from $\Theta^{(1)}$, whose final $K-i-1$ entries come from $\Theta^{(2)}$, and whose $i$ th CPtable entries is $z$; hence $f\left(\theta_{d_{i} \mid \mathbf{f}_{i}}^{(1)}\right)=\ln \left(P_{\Theta_{i}}(c \mid \mathbf{e})\right)$, and $f\left(\theta_{d_{i} \mid \mathbf{f}_{i}}^{(2)}\right)=\ln \left(P_{\Theta_{i+1}}(c \mid \mathbf{e})\right)$. As this function is continuous, we know that

$$
f(a)-f(b)=\left.\frac{\partial f(z)}{\partial z}\right|_{z^{\prime}}[b-a]
$$

for some $z^{\prime} \in[a, b]$. As $f(z)=\ln \left(P_{\Theta[z]}(c, \mathbf{e})\right)-\ln \left(P_{\Theta[z]}(\mathbf{e})\right)$, we see that

$$
\begin{aligned}
\frac{\partial f(z)}{\partial z}= & \frac{1}{P_{\Theta[z]}(c, \mathbf{e})} P_{\Theta[z]}\left(c, \mathbf{e} \mid d_{i}, \mathbf{f}_{i}\right) \times P_{\Theta[z]}\left(\mathbf{f}_{i}\right) \\
& -\frac{1}{P_{\Theta[z]}(\mathbf{e})} P_{\Theta[z]}\left(\mathbf{e} \mid d_{i}, \mathbf{f}_{i}\right) \times P_{\Theta[z]}\left(\mathbf{f}_{i}\right) \\
= & \frac{1}{z}\left[P_{\Theta[z]}\left(d_{i}, \mathbf{f}_{i} \mid c, \mathbf{e}\right)-P_{\Theta[z]}\left(d_{i}, \mathbf{f}_{i} \mid \mathbf{e}\right)\right]
\end{aligned}
$$

which means that $\left|\frac{\partial f(z)}{\partial z}\right| \leq 1 / z \leq 1 / \gamma$. (The second inequality follows from the assumption that we are only considering $\Theta \in \mathcal{B} \mathcal{N}_{\Theta \geq \gamma}(G)$.) Hence,

$$
\begin{aligned}
\left|\ln \left(P_{\Theta_{i+1}}(c \mid \mathbf{e})\right)-\ln \left(P_{\Theta_{i}}(c \mid \mathbf{e})\right)\right| & =\left|f\left(\theta_{d_{i} \mid \mathbf{f}_{i}}^{(2)}\right)-f\left(\theta_{d_{i} \mid \mathbf{f}_{i}}^{(1)}\right)\right| \\
& \leq \frac{1}{\gamma} \times\left|\theta_{d_{i} \mid \mathbf{f}_{i}}^{(2)}-\theta_{d_{i} \mid \mathbf{f}_{i}}^{(1)}\right| \leq \frac{1}{\gamma} \times \frac{\gamma \epsilon}{6 K}=\frac{\epsilon}{6 K}
\end{aligned}
$$

To prove Eq. (15): Observe first that the probability of any event must be at least the product of $N$ CPtable entries, and hence $P_{\Theta}(c) \geq \gamma^{N}$ for any $c$ and any $\Theta \in \operatorname{EN}_{\Theta \leq \gamma}(G)$. This means the value of $-\ln \left(P_{\Theta}(c \mid \mathbf{e})\right)$, and hence $\mathrm{LCL}_{\chi}(\Theta)$ for any distribution $\chi$, is between 0 and $-N \ln \gamma$.

As the queries $q=P(c, \mathbf{e})$ are drawn at random from a stationary distribution, we can view the quantity $\ln P_{\Theta}(q)$ as an iid random value, whose range is $[0,-N \ln \gamma]$ and whose expected value is $\mathrm{LCL}(\Theta)$. Hoeffding's Inequality bounds the probability that the empirical average score after $|S|=M$ iid examples (here $\widehat{\mathrm{LCL}}(\Theta)$ ) will be far away from the true mean $\operatorname{LCL}(\Theta)$ :

$$
P\left(|\widehat{\mathrm{CL}}(\Theta)-\operatorname{LCL}(\Theta)|>\frac{\epsilon}{6}\right)<2 \exp \left[-2 M\left(\left(\frac{\epsilon}{6}\right) / N \ln \gamma\right)^{2}\right]
$$

This is under $\delta / L$ using the $M$ from Eq. (15).

# Acknowledgments 

We thank C. Cheng, T. Dietterich, A. Grove, P. Hooper, J. Lafferty, D. Schuurmans, and the anonymous reviewers for their many helpful suggestions. We also thank J. Cheng and T. Joachims for letting us use their PowerConstructor and SVM-Light systems, respectively. RG and WZ were partially funded by NSERC; RG and XS were also funded by the Alberta Ingenuity Centre for Machine Learning; and WZ, by Syncrude.

## Notes

1. See Greiner, Grove, and Schuurmans (1997) for an alternative position, and the challenges this requires solving.
2. As we assume the structure $G=\langle\mathcal{V}, A\rangle$ of the belief net $B=\langle\mathcal{V}, A, \Theta\rangle$ is fixed, we will identify a belief net with its parameters $\Theta$.
3. This $\theta_{\mathcal{E} \boldsymbol{f}} \geq \gamma$ constraint is trivially satisfied by any parameter learner that uses Laplacian correction, or that produces the posterior distribution from uniform Dirichlet priors: These system can use $\gamma=1 /(m+2)$ where $m$ is the number of training instances (Heckerman, 1998).
4. We say a tuple is "complete" if it specifies a value for every attribute; hence " $E_{1}=e_{1}, \ldots, E_{n}=e_{n}$ " is complete (where $\left\{E_{1}, \ldots, E_{n}\right\}$ is the full set of evidence variables) but " $E_{2}=e_{2}, E_{7}=e_{7}$ " is not.
5. Proof sketch: Reduce from 3SAT, using the structure from Cooper (1990), with queries that "specify" each clause, and one that requires that the conjunction of clauses has probability 1 . Then the $\log$ conditional likelihood score is 0 iff there is a satisfying assignment to the 3SAT formula. Details are in ESM(A).
6. While the obvious tabular representation of the CPtables involves more parameters than appear in this logistic regression model, these extra BN-parameters are redundant.
7. While the original $\mathrm{APS}_{0}$ (Binder et al., 1997) climbed in the space of parameters $\Theta=\{\theta_{i}\}$, we instead used a modified $\mathrm{APS}_{\beta}$ system that uses the $\beta=\{\beta_{i}\}$ values (Eq. (11)), as we found it produced better classifiers.
8. The $G<T$ notation does not mean the arcs of $G$ are a subset of $T$ 's, as $G$ may also include arcs that are not in $T$.
9. This analysis makes the standard assumptions that the error are identical and independent, and each normally distributed; see Nadeau and Bengio (2003).
10. ESM(F) uses a simple controlled study, on artificial data, to further investigate how ELR and OFE deal with increasingly more erroneous structures.

11. When using 5 -fold cross-validation, we computed the standard deviation using the 5 computed accuracy values. When dealing with a single split of the data, we used the standard binomial formula, $\sqrt{p \times(1-p) / n}$, where $p$ is the accuracy and $n$ is the size of the test set.
12. As another illustration, imagine the class node $C$ depended on the variables, $\left\{E_{i}\right\}$. PowerCONSTRUCTOR would be happy returning a structure that appeared to match the distribution, even if that structure separated $C$ from many of these relevant $E_{i}$ 's. This cannot happen with either NB or TAB, as these structure connect every variable to $C$.
13. This BIC is a generative measure. We suspect finding the best "discriminative structure" would be as difficult. See also the iterative methods used in Grossman and Domingos (2004) for this task.
14. As our goal was only to compare the effectiveness of the parameter-learners on reasonable structures, the source of these structures is irrelevant, and in particular, it does not matter that the structure was generated from all the data.
15. $\operatorname{ESM}(\mathrm{G})$ discusses another situation, where the model is more complex than the truth. It presents empirical data that the generative models often work better in this uncommon situation, and explains why.
16. This differs from the Ng and Jordan (2001) result, which compared only the simplest form, Naïve-bayes versus logistic regression, and dealt with error itself.
