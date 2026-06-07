# GRAPHICAL MODELS FOR ASSOCIATIONS BETWEEN VARIABLES, SOME OF WHICH ARE QUALITATIVE AND SOME QUANTITATIVE 

By S. L. Lauritzen and N. Wermuth<br>Aalborg University and University of Mainz


#### Abstract

We define and investigate classes of statistical models for the analysis of associations between variables, some of which are qualitative and some quantitative. In the cases where only one kind of variables is present, the models are well-known models for either contingency tables or covariance structures. We characterize the subclass of decomposable models where the statistical theory is especially simple. All models can be represented by a graph with one vertex for each variable. The vertices are possibly connected with arrows or lines corresponding to directional or symmetric associations being present. Pairs of vertices that are not connected are conditionally independent given some of the remaining variables according to specific rules.


1. Introduction. The purpose of the present article is to develop statistical models, with discrete and continuous random variables, that can be used to describe and investigate associations among properties of observational units, some of which are qualitative and some of which are quantitative.

The applications we have in mind are primarily in the social sciences and we believe that it is indispensable that the models can take into account that variables can be explanatory, responses and both, in the sense that they are responses to some variables but then explanatory for others. The associations between other variables might appropriately be interpreted without this distinction because the variables appear on a symmetric footing.

As an illustration, consider the following example, taken from a thesis of Schumann (1986), referring to cognitive developments in young children.

We shall not go into details, but in the experiment each of 55 children aged from four to seven was confronted with 19 similar tasks, two of which were extremely easy and only included to keep the child motivated.

In each task the child had to compare one picture, called the standard, to six others arranged in a row 12 cm apart from the standard. Five of the alternatives differed from the standard in one to at most five characteristics. The total number of correct matches in the 17 tasks was taken as a measure of the performance ( P ), the total number of times the child looked from the standard to the alternatives or back (divided by 17) as a measure for the information gathering behaviour (IGB). Furthermore, the capacity of the working memory (CWM) was operationalized by the 'digit span backwards,' that is, by the number of digits the child could repeat in reverse order, while the pure storage

[^0]
[^0]:    Received May 1987; revised June 1988.
    AMS 1980 subject classifications. Primary 62H99; secondary 62J99.
    Key words and phrases. Analysis of variance, conditional independence, contingency tables, covariance selection, exponential families, logistic regression, log-linear models, Markov random fields, multivariate analysis, path analysis, regression, recursive models, triangulated graphs.

capacity (SC) was captured by the 'digit span forwards,' that is, by the number of digits the child could repeat in unchanged order. The levels of SC are called low for less than four digits and high otherwise, while the levels of CWM are low $(<2)$, medium $(=2)$ and high $(>2)$. Since the first two variables are viewed as being quantitative, the other as qualitative, the variables P and IGB are analysed as continuous and CWM and SC as discrete. The hypotheses considered by Schumann are summarized in the following graph:
![img-0.jpeg](img-0.jpeg)

The storage capacity (SC) and the capacity of the working memory (CWM) are explanatory variables on equal footing, the information gathering behaviour (IGB) is conceived as a response to these and the performance as a response to all of them. The (vague) meaning of the picture is that CWM has no influence on IGB, other than what is explainable through SC and that the performance P depends directly only upon CWM and IGB.

One aim of the present article is to enable the researcher to give a precise meaning to such pictures by developing corresponding statistical models. The models are appropriate for what Holland (1986) terms 'associational inference.' They are extensions to models known as path analysis [Wright (1921, 1923, 1934)] and provide an alternative to other similar developments in social sciences; see, for example, Wold (1954), Simon (1957), Blalock (1971), Jöreskog (1977), Goodman (1973) and Goldberger and Duncan (1978). See Kiiveri and Speed (1982) and Wermuth (1985) for further discussion and references.

The most general models discussed here are the graphical chain models (Section 8). These have previously been discussed in the discrete case by Goodman (1973), Asmussen and Edwards (1983) and in the continuous case by Porteous (1985b).

Special cases of these are the recursive models (Sections 5 and 6) investigated in the discrete case by Wermuth and Lauritzen (1983), the continuous case by Wermuth (1980) and Kiiveri (1983) and some aspects of the general case by Kiiveri (1983) and Kiiveri, Speed and Carlin (1984). The latter reference also deals with aspects of the graphical chain models in the general case. Other special cases are the class of graphical Markov models (Sections 3 and 4) that in the discrete case specialize to those of Darroch, Lauritzen and Speed (1980) and in the continuous case to the covariance selection models of Dempster (1972). These models, where all associations are symmetric, are the basic building blocks for the other models. Consequently, most of the article (Sections 3 and 4) is devoted to a study of these and the corresponding distributions. The multivariate distributions upon which our developments are based, are characterized by the joint conditional distribution of the continuous variables, given the discrete as being Gaussian and therefore called CG-distributions. It is crucial to get a good understanding of these and their interplay with properties of conditional

independence (Sections 2 and 3). For the latter notion as well as our notation on this point, the reader is referred to Dawid (1979, 1980).

The class of models where the statistical theory and interpretation is especially simple has been identified as the decomposable models (Section 7). Some technical matters such as our graphtheoretic terminology and a proof of an important result are deferred to the appendices. We suggest that these are omitted at first reading.

Our emphasis here is on the formal development of the models and their properties. For examples of their application and a discussion of some implications of the results for practical statistical work, see Edwards (1987, 1988, 1989) and Wermuth and Lauritzen (1989).
2. CG-distributions and CG-regressions. The present section is devoted to the study of the class of multivariate distributions upon which the models are based. We consider a finite set $V$ of variables partitioned into discrete and continuous as $V=\Delta \cup \Gamma$. Let $|V|=p+q,|\Delta|=p$ and $|\Gamma|=q$. Thus our random variables take values in the product space

$$
\mathscr{X}=\mathscr{I} \times \mathscr{G}=\underset{\alpha \in V}{ } \mathscr{X}_{\alpha}
$$

with $\mathscr{I}=\times_{\delta \in \mathcal{S}} \mathscr{I}_{\delta}, \mathscr{G}=\mathbb{R}^{\mathrm{T}}$, where $\mathscr{I}_{\delta}, \delta \in \Delta$, are finite sets of possible levels of the discrete variables.

The corresponding random variables shall be denoted $X_{\alpha}, \alpha \in \Delta \cup \Gamma$. Thus the variables $X_{\delta}, \delta \in \Delta$, are discrete valued (ranging in $\mathscr{I}_{\delta}$ ), whereas $X_{\gamma}, \gamma \in \Gamma$, are real-valued.

Typical points of $\mathscr{X}$ are denoted by $x$ or as $x=(i, y)$. Similarly, $i_{a}, y_{b}, x_{d}$, etc., are used to denote the projections of a point $x=(i, y)$ onto the spaces

$$
\mathscr{I}_{a}=\underset{\delta \in a}{\times} \mathscr{I}_{\delta}, \quad \mathscr{G}_{b}=\mathbb{R}^{b}, \quad \mathscr{X}_{d}=\underset{\alpha \in d}{\times} \mathscr{X}_{\alpha}, \quad \text { respectively. }
$$

Analogously, we use the notation $X_{a}$ for the collection of variables $\left(X_{\alpha}, \alpha \in a\right)$, and the short notation $a \Perp b \mid c$ to indicate that the random variables $X_{\alpha}$ and $X_{b}$ are conditionally independent given $X_{c}$.

Our investigations shall be directed toward a special class of probability distributions that all have strictly positive density $f$ (w.r.t. product of counting measure on $\mathscr{I}$ and Lebesgue measure on $\mathscr{G}$ ) of the form

$$
\begin{aligned}
f(x) & =f(i, y) \\
& =\exp \left\{g\left(x_{\Delta}\right)+h\left(x_{\Delta}\right)^{\mathrm{T}} x_{\Gamma}-\frac{1}{2} x_{\Gamma}^{\mathrm{T}} K\left(x_{\Delta}\right) x_{\Gamma}\right\} \\
& =\exp \left\{g(i)+h(i)^{\mathrm{T}} y-\frac{1}{2} y^{\mathrm{T}} K(i) y\right\}
\end{aligned}
$$

where $g$ is a real-valued function of $i, h$ is a $q$-vector-valued function of $i$ taking values in $\mathbb{R}^{\Gamma}, K$ is a $q \times q$ matrix-valued function of $i$ taking values in the set of positive definite symmetric matrices and $v^{\mathrm{T}}$ denotes the transpose of the vector $v$.

A probability distribution with density of the form (2.1) has conditional Gaussian distributions in the sense that $X_{\Gamma}$ for given $X_{\Delta}=i$ is $q$-variate Gaussian with covariance $K(i)^{-1}$ and expectation $K(i)^{-1} h(i)$, that is,

$$
\mathscr{L}\left(X_{\Gamma} \mid X_{\Delta}=i\right)=\mathscr{N}_{q}\left(K(i)^{-1} h(i), K(i)^{-1}\right)
$$

The marginal distribution of the discrete variables $X_{\Delta}$ has probabilities equal to

$$
p(i)=(2 \pi)^{-q / 2} \operatorname{det}(K(i))^{-1 / 2} \exp \left\{g(i)+\frac{1}{2} h(i)^{\mathrm{T}} K(i)^{-1} h(i)\right\}
$$

To derive these facts, we first rewrite (2.1) as

$$
f(x)=\exp \left\{g^{*}(i)-\frac{1}{2}(y-\xi(i))^{\mathrm{T}} K(i)(y-\xi(i))\right\}
$$

where we have let

$$
\xi(i)=K(i)^{-1} h(i), \quad g^{*}(i)=g(i)+\frac{1}{2} h(i)^{\mathrm{T}} K(i)^{-1} h(i)
$$

We then integrate over $y$ and obtain (2.3) and (2.2).
On the other hand, it is clear that any probability distribution on $\mathscr{I} \times \mathscr{G}$ with strictly positive marginal probability on $\mathscr{I}$ and with conditional distributions of the continuous variables being multivariate regular Gaussian, with expectation $\xi(i)$ and covariance matrix $\Sigma(i)$, will have an expansion as (2.1), where

$$
\begin{gathered}
K(i)=\Sigma(i)^{-1}, \quad h(i)=K(i) \xi(i) \\
g(i)=\log p(i)-\frac{q}{2} \log (2 \pi)+\frac{1}{2} \log \operatorname{det} K(i)-\frac{1}{2} h(i)^{\mathrm{T}} K(i)^{-1} h(i)
\end{gathered}
$$

Distributions of this type shall be called CG-distributions and are the basic distributions entering in the present article. It is of interest also to consider the special case when the covariance matrix of the conditional distribution of the continuous variables given the discrete ones does not depend on $i$, that is $K(i) \equiv K$, in which case we shall say that the probability distribution is homogeneous and call it an HCG-distribution.

The latter class of distributions (HCG) was considered by Tate (1954) and Olkin and Tate (1961) in a context of defining correlation among a binary and a continuous variable, and by Dempster (1973) in studying aspects of a so-called multinomial logit model. Later, the distributions have been used by Krzanowski (1983) and Little and Schluchter (1985) in a context different from the present. Since we shall be interested in HCG-distributions as well as CG-distributions we shall adopt the convention that unless otherwise stated, all theorems, statements, etc., about CG-distributions, remain true if CG everywhere is replaced by HCG. In cases where this is not obvious, we shall comment on that explicitly.

A CG-distribution can be specified either by the triple $(g, h, K)$ or $(p, \xi, \Sigma)$, whichever might be convenient in the context considered. We shall term the first triple as the canonical and the second as the moment characteristics of the CG-distributions.

An important key to understanding the development in the following sections is the behaviour of these distributions under conditioning and marginalization.

Let $V=A \cup B$ be a partitioning of the set of variables. We then have the following proposition.

Proposition 2.1. If $B \subseteq \Gamma$ and $X$ has a CG-distribution, the marginal distribution of $X_{A}$ is $C G$.

Proof. The result follows immediately by integrating (2.1) over $x_{B}\left(=y_{B}\right)$.

In general this is not true for $B \subseteq \Delta$. However,
Proposition 2.2. If $X$ has a CG-distribution and $B \subseteq \Delta$ satisfies

$$
B \Perp \Gamma \mid \Delta \backslash B
$$

then the marginal distribution of $X_{A}$ is $C G$.
Proof. By standard properties of conditional independence, the condition ensures that

$$
\mathscr{L}\left(X_{\Gamma} \mid X_{\Delta \backslash B}\right)=\mathscr{L}\left(X_{\Gamma} \mid X_{\Delta}\right)
$$

and the latter is Gaussian by assumption.
For conditional distributions we have the following proposition.
Proposition 2.3. If $X$ has a CG-distribution, the conditional distribution of $X_{A}$ given $X_{B}=x_{B}$ is $C G$.

Proof. The result follows from the identity

$$
\mathscr{L}\left(X_{A \cap \Gamma} \mid X_{A \cap \Delta}=i_{A \cap \Delta}, X_{B}=x_{B}\right)=\mathscr{L}\left(X_{A \cap \Gamma} \mid X_{\Delta}=i_{\Delta}, X_{B \cap \Gamma}=x_{B \cap \Gamma}\right)
$$

and the latter is Gaussian since it is obtained by conditioning upon $x_{B \cap \Gamma}$ in the (conditional) Gaussian distribution of $X_{\Gamma}$, given $X_{\Delta}=i_{\Delta}$.

For later use, we need to expand upon Proposition 2.3 and consider how this conditional distribution depends upon $x_{B}$. We thus introduce the class of CG-regressions as systems of maps that to any element $(j, z)$ of a product set

$$
\mathscr{J} \times \mathscr{Z}=\left(\underset{\delta \in \Delta^{*}}{\times} \mathscr{J}_{\delta}\right) \times \mathbb{R}^{\Gamma^{*}}
$$

of possible state spaces for discrete and continuous variables, specify a CG-distribution on $\mathscr{I} \times \mathscr{Y}$ with moment characteristics $(p, \xi, \Sigma)$ depending on $(j, z)$ in a particular way:

$$
\begin{aligned}
\log p(i \mid j, z) & =u(i \mid j)+v(i \mid j)^{\mathrm{T}} z+z^{\mathrm{T}} W(i \mid j) z-\log \kappa(j, z) \\
\xi(i \mid j, z) & =a(i \mid j)+B(i \mid j) z \\
\Sigma(i \mid j, z) & =C(i \mid j)
\end{aligned}
$$

The CG-regression is specified by the sixtuple $(u, v, W, a, B, C)$. The term $\kappa(j, z)$ is a normalizing constant,

$$
\kappa(j, z)=\sum_{i} \exp \left\{u(i \mid j)+v(i \mid j)^{\mathrm{T}} z+z^{\mathrm{T}} W(i \mid j) z\right\}
$$

depending on $(u, v, W)$. If we change any of $(u, v, W)$ by adding terms depending on $j$ only, they will eventually cancel out in the final expression (2.4), giving rise to the same $p(i \mid j, z)$.

A CG-regression specifies a quadratic dependence of $\log p$ on $z$, a linear dependence on $z$ of the conditional expectation and a nondependence on $z$ of the conditional covariance matrix. The coefficients of the dependencies as well as the conditional covariance matrix are allowed to depend on $j$.

We shall say that a CG-regression is homogeneous or an HCG-regression if $W(i \mid j) \equiv 0, B(i \mid j) \equiv B, C(i \mid j) \equiv C$, in words if $\log p$ depends linearly on $z$, the linear dependencies of conditional expectations are parallel and the covariance matrix is constant. We then have the following proposition.

Proposition 2.4. A sixtuple $(u, v, W, a, B, C)$ specifies a CG-regression if and only if there is a joint CG-distribution on $(\mathscr{I} \times \mathscr{J}) \times(\mathscr{G} \times \mathscr{Z})$ such that (2.4) specifies the conditional distribution of $(I, Y)$ given $(J, Z)=(j, z)$.

Proof. Suppose that we have a joint CG-distribution with characteristics $(p, \xi, \Sigma)$ and let us partition $\xi, K$ and $\Sigma$ as

$$
\xi=\binom{\xi_{Y}}{\xi_{Z}}, \quad K=\left(\begin{array}{ll}
K_{Y Y} & K_{Y Z} \\
K_{Z Y} & K_{Z Z}
\end{array}\right), \quad \Sigma=\left(\begin{array}{ll}
\Sigma_{Y Y} & \Sigma_{Y Z} \\
\Sigma_{Z Y} & \Sigma_{Z Z}
\end{array}\right)
$$

Straightforward calculations yield that the conditional distributions have characteristics (2.4) given as

$$
\begin{aligned}
C(i \mid j)= & K_{Y Y}^{-1}(i, j) \\
B(i \mid j)= & -C(i \mid j) K_{Y Z}(i, j) \\
a(i \mid j)= & \xi_{Y}(i, j)-B(i \mid j) \xi_{Z}(i, j) \\
W(i \mid j)= & \frac{1}{2} \Sigma_{Z Z}^{-1}(i, j) \\
v(i \mid j)= & \Sigma_{Z Z}^{-1}(i, j) \xi_{Z}(i, j) \\
u(i \mid j)= & \log p(i, j)-\frac{1}{2} \log \operatorname{det} \Sigma_{Z Z}(i, j) \\
& -\frac{1}{2} \xi_{Z}(i, j)^{\mathrm{T}} \Sigma_{Z Z}^{-1}(i, j) \xi_{Z}(i, j)
\end{aligned}
$$

This direction was the obvious one. To show the converse, we have to fill the apparent gap that $W$ does not have to be positive definite whereas $\Sigma$ must be, implying that (2.5) cannot be used directly. So suppose conversely that we have given a CG-regression by a sixtuple ( $u, v, W, a, B, C$ ), and we want to construct a CG-distribution with corresponding conditional distributions. We then first let

$$
D(i, j)=\theta E-2 W(i \mid j)
$$

where $E$ is the identity matrix, and choose $\theta>2\left|\lambda_{\max }\right|$, where $\lambda_{\max }$ is the largest in absolute value of the eigenvalues of all the matrices $W(i \mid j)$, thereby obtaining that $D(i, j)$ is positive definite for all $(i, j)$. We then let

$$
\begin{aligned}
& K_{Z Z}(i, j)=D(i, j)+B(i \mid j)^{\mathrm{T}} C(i \mid j)^{-1} B(i \mid j) \\
& K_{Y Z}(i, j)=-C(i \mid j)^{-1} B(i \mid j)=K_{Z Y}^{\mathrm{T}}(i, j), \quad K_{Y Y}(i, j)=C(i \mid j)^{-1}
\end{aligned}
$$

The matrix $K(i, j)$ so defined is then positive definite since for arbitrary $e^{\mathrm{T}}=\left(y^{\mathrm{T}}, z^{\mathrm{T}}\right) \neq 0$ we have, suppressing the dependence on $(i, j)$,

$$
\begin{aligned}
e^{\mathrm{T}} K e & =y^{\mathrm{T}} C^{-1} y-2 y^{\mathrm{T}} C^{-1} B z+z^{\mathrm{T}} D z+z^{\mathrm{T}} B C^{-1} B z \\
& =(y-B z)^{\mathrm{T}} C^{-1}(y-B z)+z^{T} D z>0
\end{aligned}
$$

We can now determine $\xi$ from $a$ and $v$ by the equations (2.5). Finally, $p(i, j)$ can be calculated. Doing the calculations in reverse order, remembering that $W$ is only determined up to an additive term, we get that our CG-distribution so constructed has the right conditional distributions.

If the joint distribution is homogeneous we get $B(i \mid j) \equiv B, C(i \mid j) \equiv C$ and $W(i \mid j) \equiv W$. Recalling that $W$ is only determined up to an additive term, possibly depending on $j$, we might as well take $W \equiv 0$, giving a homogeneous regression. On the other hand, had the CG-regression been homogeneous, $K$, as defined, would not depend on $(i, j)$ and the resulting CG-distribution would therefore be homogeneous.

In the special case where the set of 'response' variables $(I, Y)$ has only one element, $V=\Delta=\{\delta\}$ or $V=\Gamma=\{\gamma\}$, we use the term univariate $C G$-regressions.

As an illustration of some of the previous developments consider the following two examples, to be used throughout the remainder of the article:

1. involving one discrete and two continuous variables ( $I, Y_{1}, Y_{2}$ ) and
2. involving two discrete and one continuous variable ( $I_{1}, I_{2}, Y$ ).

In the first case, the general log density becomes

$$
\begin{aligned}
\log f\left(i, y_{1}, y_{2}\right)= & g(i)+h^{(1)}(i) y_{1}+h^{(2)}(i) y_{2} \\
& -\frac{1}{2}\left[k^{(11)}(i) y_{1}^{2}+2 k^{(12)}(i) y_{1} y_{2}+k^{(22)}(i) y_{2}^{2}\right]
\end{aligned}
$$

If the distribution is homogeneous, $k^{(11)}, k^{(12)}$ and $k^{(22)}$ do not depend on $i$. The marginal distribution of ( $I, Y_{1}$ ) is conditional Gaussian, but this is typically not the case for the marginal distribution of $\left(Y_{1}, Y_{2}\right)$. In the homogeneous case, the conditional distribution of $I$, given $\left(Y_{1}, Y_{2}\right)=\left(y_{1}, y_{2}\right)$ has the form

$$
\log p\left(i \mid y_{1}, y_{2}\right)=g(i)+h^{(1)}(i) y_{1}+h^{(2)}(i) y_{2}-\log \kappa\left(y_{1}, y_{2}\right)
$$

In example 2 the general log density is

$$
\log f\left(i_{1}, i_{2}, y\right)=g\left(i_{1}, i_{2}\right)+h\left(i_{1}, i_{2}\right) y-\frac{1}{2} k\left(i_{1}, i_{2}\right) y^{2}
$$

the marginal distributions of $\left(I_{1}, Y\right)$ or $\left(I_{2}, Y\right)$ are not CG in general, whereas the

conditional distribution of $Y$, given $\left(I_{1}, I_{2}\right)=\left(i_{1}, i_{2}\right)$, is Gaussian with expectation $h\left(i_{1}, i_{2}\right) / k\left(i_{1}, i_{2}\right)$ and variance $k\left(i_{1}, i_{2}\right)^{-1}$, the latter being independent of $\left(i_{1}, i_{2}\right)$ in the homogeneous case.
3. The Markov property for CG-distributions and CG-interactions. Consider the setup in the previous section and let a marked graph $\mathscr{G}=(\Delta \cup \Gamma, E)$ be given. In the present section $\mathscr{G}$ is always assumed to be undirected, that is, each connection between vertices is a line.

A distribution on

$$
\mathscr{X}=\mathscr{I} \times \mathscr{G}=\left(\underset{\delta \in \Delta}{\times} \mathscr{I}_{\delta}\right) \times \mathbb{R}^{\Gamma}
$$

with strictly positive density $f$ is said to be Markovian w.r.t. $G$ or $G$-Markovian if it satisfies

$$
\mathbf{M}: \quad \alpha \notin \operatorname{adj}(\beta) \Rightarrow\{\alpha\} \Perp\{\beta\} \mid V \backslash\{\alpha, \beta\} \quad \text { for all } \alpha, \beta \in V
$$

that is, if pairs of variables corresponding to nonadjacent vertices are conditionally independent given the remaining variables.

To introduce the notion of interaction, let us reconsider the general expression for a CG-distribution,

$$
\log f(i, y)=g(i)+h(i)^{\mathrm{T}} y-\frac{1}{2} y^{\mathrm{T}} K(i) y
$$

Let us also adopt the convention that functions denoted by $f_{a}, \psi_{a}, \lambda_{a}$, etc., depend on $x=(i, y)$ only through its coordinates in $a,\left(x_{a}, \alpha \in a\right)=x_{a}$, in other words $x_{a}=z_{a} \Rightarrow f_{a}(x)=f_{a}(z)$, etc. Thus functions $f_{\varnothing}, \psi_{\varnothing}$, etc., with the empty set as subscript are constant. We can now make expansions as follows:

$$
g(i)=\sum_{d \subset \Delta} \lambda_{d}(i), \quad h(i)=\sum_{d \subset \Delta} \eta_{d}(i), \quad K(i)=\sum_{d \subset \Delta} \Psi_{d}(i)
$$

In general such expansions can be made in many ways, see, for example, Darroch and Speed (1983) for a comprehensive discussion of this and similar problems. Whenever such an expansion has been made, we shall denote the $\lambda, \eta$ and $\Psi$ terms as interactions and give them special names:
$\lambda_{\varnothing}$ is the log normalizing constant.
$\lambda_{d}, d \neq \varnothing$, are pure discrete interactions among variables in $d$. If $|d|=1$ we also call these main effects of the discrete variables.
$\eta_{\varnothing}$ 's coordinates are the main effects of the continuous variables.
$\eta_{d}, d \neq \varnothing$, are mixed linear interactions and its coordinates are the mixed linear interaction between a continuous variable and variables in $d$.
$\Psi_{d}, d \subseteq \Delta$, are quadratic interaction matrices; the elements of $\Psi_{\varnothing}(i)$ do not depend on $i$ and are called pure quadratic interactions. The elements of $\Psi_{d}(i)$, $d \neq \varnothing$, are mixed quadratic interactions between variables in $d$ and pairs of continuous variables.

Note that a CG-distribution is homogeneous (HCG) if and only if it has an interaction representation with no mixed quadratic interactions.

Inserting the interaction terms into (3.1) we get the following representation of the logarithm of the density:

$$
\log f(i, y)=\sum_{d \subset \Delta} \lambda_{d}(i)+\sum_{d \subset \Delta} \sum_{\gamma \in \Gamma} \eta_{d}(i)_{\gamma} y_{\gamma}-\frac{1}{2} \sum_{d \subset \Delta} \sum_{\gamma, \mu \in \Gamma} \psi_{d}(i)_{\gamma \mu} y_{\gamma} y_{\mu}
$$

A CG-distribution is now said to be a nearest-neighbour Gibbs distribution w.r.t. $G$ or $G$-Gibbsian, if it has an interaction representation with interaction terms satisfying

$$
\begin{aligned}
\lambda_{d}(i) & \equiv 0 \quad \text { unless } d \text { is complete in } G \\
\eta_{d}(i)_{\gamma} & \equiv 0 \quad \text { unless } d \cup\{\gamma\} \text { is complete in } G \\
\Psi_{d}(i)_{\gamma \mu} & \equiv 0 \quad \text { unless } d \cup\{\gamma, \mu\} \text { is complete in } G
\end{aligned}
$$

Thus a Gibbsian probability has an expansion with interaction terms only involving variables that are neighbours.

A key result in this section is the following version of the "Gibbs = Markov theorem," see, for example, Speed (1979) for a survey.

Proposition 3.1. A CG-distribution is $\mathscr{G}$-Markovian if and only if it is $\mathscr{G}$-Gibbsian.

The general theorem implies that a distribution with positive density is Markov if and only if the density factorizes into a product of functions that only depend on variables that are mutual neighbours. We have to show that the factorization so obtained splits up into separate factorizations of the constant, linear and quadratic terms. This is done in Appendix B.

The corollary below, however, follows as in the standard case and its proof is therefore omitted.

Corollary 3.2. The following statements are equivalent for a CG-distribution:
(i) The distribution is $\mathscr{G}$-Markovian.
(ii) $a \Perp b \mid c$ whenever $a, b, c$ are disjoint and $c$ separates a from $b$.
(iii) $\forall \alpha \in V:\{\alpha\} \Perp V \backslash(\operatorname{cl}(\alpha)) \mid \operatorname{adj}(\alpha)$.

As a continuation of the examples from the previous section, consider the following graphs:
![img-1.jpeg](img-1.jpeg)

The conditional independence restriction in the graph (1) is $Y_{1} \Perp Y_{2} \mid I$ and this is by Proposition 3.1 equivalent to the condition $k^{(12)}(i) \equiv 0$ in (2.6) because there is no edge between $\left(Y_{1}\right)$ and $\left(Y_{2}\right)$. In the second example, the restriction $I_{1} \Perp I_{2} \mid Y$

is by Proposition 3.1 equivalent to the existence of the expansion

$$
\begin{aligned}
\log f\left(i_{1}, i_{2}, y\right)= & \lambda^{(1)}\left(i_{1}\right)+\lambda^{(2)}\left(i_{2}\right)+\left(\eta^{(1)}\left(i_{1}\right)+\eta^{(2)}\left(i_{2}\right)\right) y \\
& -\frac{1}{2}\left(\psi^{(1)}\left(i_{1}\right)+\psi^{(2)}\left(i_{2}\right)\right) y^{2}
\end{aligned}
$$

In the homogeneous case, that is, $\psi^{(1)}\left(i_{1}\right)+\psi^{(2)}\left(i_{2}\right) \equiv \psi$ the conditional distribution of $Y$ given $\left(I_{1}, I_{2}\right)$ will have expectation $\alpha\left(i_{1}\right)+\beta\left(i_{2}\right)$, where $\eta\left(i_{1}\right)=$ $\lambda^{(1)}\left(i_{1}\right) / \psi, \beta\left(i_{2}\right)=\eta^{(2)}\left(i_{2}\right) / \psi$ and variance $\sigma^{2}=\psi^{-1}$, that is, leading to the additive model for a two-way classification.

An important fact about CG-distributions that are Markovian is related to their behaviour under marginalization and conditioning. In fact we have the following proposition.

Proposition 3.3. If a CG-distribution is $\mathscr{G}$-Markovian, then for all $A \subset V$ the conditional distribution of $X_{A}$ given $X_{B}=x_{B}^{*}$, where $B=V \backslash A$ is $C G$ and $G_{A}$-Markovian.

Proof. That the CG-property is preserved is Proposition 2.3. That the Markov property is preserved is immediate from the definition of this property.

In general, the Markov property is not preserved under marginalization. Consider the example 2 above, where the marginal distribution of $\left(I_{1}, I_{2}\right)$ has point probabilities

$$
\begin{aligned}
p\left(i_{1}, i_{2}\right) & =\sqrt{2 \pi \sigma^{2}} \exp \left\{\lambda^{(1)}\left(i_{1}\right)+\lambda^{(2)}\left(i_{2}\right)+\psi\left(\alpha\left(i_{1}\right)+\beta\left(i_{2}\right)\right) / 2\right\} \\
& =\exp \left\{a\left(i_{1}\right)+b\left(i_{2}\right)+\psi \alpha\left(i_{1}\right) \beta\left(i_{2}\right)\right\}
\end{aligned}
$$

As we see, $I_{1}$ and $I_{2}$ are not independent, but $p$ contains a multiplicative interaction term $\psi \alpha\left(i_{1}\right) \beta\left(i_{2}\right)$ in its logarithmic expansion. It is of interest to notice that this is exactly the model considered by Goodman $(1979,1981)$ and others for contingency tables with ordered categories. We see here that the 'ordering' of the categories naturally occurs from increasing values of the 'row effects' $\alpha\left(i_{1}\right)$ and 'column effects' $\beta\left(i_{2}\right)$.

A comprehensive discussion of the marginalization problem for CG-distributions has been given by Frydenberg (1988). We shall here only give the most basic result based on the notion of a strongly simplicial subset; see Appendix A.

Proposition 3.4. If $X$ has a CG-distribution which is $\mathscr{G}$-Markovian and $B=V \backslash A$ is strongly simplicial, then $X_{A}$ has a CG-distribution and is $\mathscr{G}_{A^{-}}$ Markovian.

Proof. Let us first look at the Markov property. Suppose $\alpha, \beta \in A$ are nonadjacent. Since $B$ is simplicial, $\operatorname{bd}(B)$ is complete and at least one of them, say $\alpha$, must be in $A \backslash \operatorname{cl}(B)$. Therefore all paths in $G$ away from $\alpha$ must intersect $A$. Hence $A \backslash\{\alpha, \beta\}$ separates $\{\alpha\}$ from $\{\beta\}$ in $\mathscr{G}$ and $\{\alpha\} \Perp\{\beta\} \mid A \backslash$ $\{\alpha, \beta\}$, whereby the Markov property follows from (ii) of Corollary 3.2.

To check the distributional property, consider first the case $B \subseteq \Gamma$ in which case Proposition 2.1 applies. If $B \subseteq \Delta$ its strong simpliciality ensures $\operatorname{bd}(B) \subseteq \Delta$,

whereby $B \Perp \Gamma \mid \Delta \backslash B$ and Proposition 2.2 applies. Finally, if $B$ contains both discrete and continuous vertices, form the graph $\mathscr{G}^{*}=\left(V, E^{*}\right)$, where

$$
(\alpha, \beta) \in E^{*} \quad \Leftrightarrow \quad[(\alpha, \beta) \in E \text { or }\{\alpha, \beta\} \subseteq \operatorname{cl}(B)]
$$

Then $B \cap \Gamma$ is strongly simplicial in $\mathscr{G}^{*}$ such that we can use the results above, first on $B \cap \Gamma$ and then on $B \cap \Delta$.

In our example 1, the only nonsimplicial vertex is $(I)$, corresponding to the distribution of $\left(Y_{1}, Y_{2}\right)$ being neither Gaussian nor Markovian, since the boundary $\operatorname{bd}(\{(I)\})$ is equal to $\left\{\left(Y_{1}\right),\left(Y_{2}\right)\right\}$ and this is not discrete, nor complete. In the example 2, no nontrivial strongly simplicial subsets exist. The vertex $\left(I_{1}\right)$ has boundary $\{(Y)\}$ and since this is complete, $\left(I_{1}\right)$ is simplicial, but it does not satisfy the second requirement-that it be discrete because $\left(I_{1}\right)$ is-and similarly with $\left(I_{2}\right)$. The vertex $(Y)$ is not even simplicial.
4. Graphical models of Markov type. In the present section we shall discuss statistical models for discrete and continuous variables based on the distributions considered in Section 3.

Suppose that we have $N$ observations of vector-random variables $X^{(1)}, \ldots, X^{(N)}$, each of these having a set of qualitative (discrete) and a set of real-valued (continuous) components, that is,

$$
X^{(\nu)}=\left(I^{(\nu)}, Y^{(\nu)}\right)=\left(I_{\delta}^{(\nu)}, \delta \in \Delta, Y_{\gamma}^{(\nu)}, \gamma \in \Gamma\right)
$$

where $I_{\delta}^{(\nu)}$ take values in $\mathscr{I}_{\delta}$ and $Y_{\gamma}^{(\nu)}$ take values in the set of real numbers.
For each undirected marked graph $\mathscr{G}=(\Delta \cup \Gamma, E)$ the graphical model corresponding to $\mathscr{G}$ is defined by assuming that $X^{(1)}, \ldots, X^{(N)}$ are independent and identically distributed according to a distribution $P$, which is unknown apart from the fact that it is a $\mathscr{G}$-Markovian CG-distribution (or a $\mathscr{G}$-Markovian HCG-distribution).

Corollary 3.2 ensures that the models can be interpreted in terms of a distributional assumption and conditional independence statements, where the latter can be read directly off the graph. The likelihood function becomes

$$
\begin{aligned}
\log L & =\sum_{\nu=1}^{N} g\left(i^{(\nu)}\right)+\sum_{\nu=1}^{N} h\left(i^{(\nu)}\right)^{\mathrm{T}} y^{(\nu)}-\frac{1}{2} \operatorname{tr}\left[\sum_{\nu=1}^{N} K\left(i^{(\nu)}\right) y^{(\nu)} y^{(\nu) \mathrm{T}}\right] \\
& =\sum_{i \in \mathscr{I}}\left[g(i) n(i)+h(i)^{\mathrm{T}} S(i)-\frac{1}{2} \operatorname{tr}(K(i) S P(i))\right]
\end{aligned}
$$

where we have let

$$
\begin{aligned}
& n(i)=\sum_{\nu: i^{(\nu)}=i} 1=\text { the number of observations with } I^{(\nu)} \text { equal to } i \\
& S(i)=\sum_{\nu: i^{(\nu)}=i} y^{(\nu)}=\text { the sum of the corresponding } y \text {-vectors, } \\
& S P(i)=\sum_{\nu: i^{(\nu)}=i} y^{(\nu)} y^{(\nu)^{T}}=\begin{array}{l}
\text { the matrix of sums of squares and } \\
\text { products of corresponding } y \text {-vectors. }
\end{array}
\end{aligned}
$$

For HCG-distributions, $K$ does not depend on $i$ so that the matrices of sums of squares and products can be pooled over $i$ to give $S P=\sum_{i \in \mathscr{I}} S P(i)$.

From expression (4.1) we see that the set $(n(i), S(i), S P(i), i \in \mathscr{I})$ is a sufficient statistic and that we are in an exponential family; cf. BarndorffNielsen (1978). By standard results and by writing the joint density of $X$ as the product of the marginal density of $I$ and the conditional density of $Y$ for given $I$, we obtain explicit estimates for $g, h$ and $K$ in the unrestricted case, that is, when $\mathscr{G}$ is the complete graph.

In the restricted case we define

$$
\begin{aligned}
\mathscr{C}_{\Delta}= & \text { the set of cliques in }\left(\Delta, E_{\Delta}\right) \\
\mathscr{C}_{\Delta}(\gamma)= & \text { the set of subsets } c \text { of } \Delta \text { such that } c \cup\{\gamma\} \text { is } \\
& \text { a clique in }\left(\Delta \cup\{\gamma\}, E_{\Delta \cup\{\gamma\}}\right) \\
\mathscr{C}_{\Delta}(\gamma, \mu)= & \text { the set of subsets } c \text { of } \Delta \text { such that } c \cup\{\gamma\} \cup\{\mu\} \\
& \text { is a clique in }\left(\Delta \cup\{\gamma\} \cup\{\mu\}, E_{\Delta \cup\{\gamma\} \cup\{\mu\}}\right)
\end{aligned}
$$

and note that $\mathscr{C}_{\Delta}(\gamma)=\mathscr{C}_{\Delta}(\gamma, \gamma)$.
Standard arguments imply that also in the restricted case we have an exponential family with canonical sufficient statistics for $i_{c} \in I_{c}$, where we have let $g\left(i_{c}\right)=\sum_{j: j_{c}=i_{c}} g(i)$ for any arbitrary function $g$ :

$$
\begin{aligned}
& n\left(i_{c}\right), \quad c \in \mathscr{C}_{\Delta} \\
& S\left(i_{c}\right)_{\gamma}, S P\left(i_{c}\right)_{\gamma \gamma}, \quad \gamma \in \Gamma, c \in \mathscr{C}_{\Delta}(\gamma) \\
& S P\left(i_{c}\right)_{\gamma \mu}, \quad\{\gamma, \mu\} \in E_{\Gamma}, c \in \mathscr{C}_{\Delta}(\gamma, \mu)
\end{aligned}
$$

These statistics can be arranged in a hierarchy as follows:

1. A set of marginal tables of counts $\left(n\left(i_{c}\right), i_{c} \in \mathscr{I}_{c}\right)$ corresponding to the cliques of $\left(\Delta, E_{\Delta}\right)$.
2. For each continuous variable $\gamma \in \Gamma$, a set of marginal tables of sums and sums of squares $\left(S\left(i_{c}\right)_{\gamma}, S P\left(i_{c}\right)_{\gamma \gamma}\right)$ corresponding to the cliques of $(\Delta \cup\{\gamma\}$, $\left.E_{\Delta \cup\{\gamma\}}\right)$ of form $c \cup\{\gamma\}$.
3. For each pair of variables $\{\gamma, \mu\} \in E_{\Gamma}$ a set of marginal tables of sums of products $S P\left(i_{c}\right)_{\gamma \mu}$ corresponding to the cliques of $\left(\Delta \cup\{\gamma, \mu\}, E_{\Delta \cup\{\gamma, \mu\}}\right)$ of form $c \cup\{\gamma, \mu\}$.

In the HCG-case there is only one table of sums of squares and products, some of the products not being needed, that is, for $\left(\{\gamma, \mu\} \notin E_{\Gamma}\right)$.

Illustrating this by the homogeneous case of example 2 in the previous section, we have

$$
\mathscr{C}_{\Delta}=\left\{\left\{\left(i_{1}\right)\right\},\left\{\left(i_{2}\right)\right\}\right\}, \quad \mathscr{C}_{\Delta}((y))=\mathscr{C}_{\Delta}
$$

and the sufficient statistics are

$$
\left\{n\left(i_{1}\right), n\left(i_{2}\right), S\left(i_{1}\right), S\left(i_{2}\right), S S\right\}
$$

that is, the row and column marginal counts and sums as well as the total sum of squares.

By standard exponential family theory the maximum likelihood estimates are uniquely given by equating the value of the sufficient statistics to their expectations.

Frydenberg and Edwards (1988) have developed an algorithm for solving these equations by a modification of methods of iterative proportional scaling; cf., for example, Darroch and Ratcliff (1972) and Speed and Kiiveri (1986). The algorithm is implemented in the program MIM, documented in Edwards (1987). The program is developed to analyse the models described here as well as their generalizations to so-called hierarchical mixed interaction models, Edwards (1989).
5. The order Markov property, CG-distributions and CG-regressions. Contrasted with Section 3 we shall here study Markov-type properties relative to an oriented graph $\mathscr{G}$, where the orientation is induced by a complete ordering $<$, that is, where $\mathscr{G}=\mathscr{G}^{\times}$.

A distribution on $\mathscr{X}=\mathscr{I} \times \mathscr{G}$ with strictly positive density is said to be order Markovian w.r.t. $\mathscr{G}$ or $\mathscr{G}$-order Markovian if it satisfies

$$
\text { OM: } \quad\{\alpha\} \Perp \Pi(\alpha) \backslash \operatorname{adj}(\alpha) \mid \operatorname{adj}(\alpha)
$$

where $\Pi(\alpha)=\{\mu \in V \mid \mu<\alpha\}$. A slight modification of $\mathbf{O M}$ is the local causal Markov property, so-called by Kiiveri, Speed and Carlin (1984). The above is certainly equivalent, which follows from the main theorem in this reference. A distribution on $\mathscr{X}=\mathscr{I} \times \mathscr{G}$ satisfies the order Markov property if and only if $\alpha \in V$,

$$
\mathscr{L}\left(X_{\alpha} \mid X_{\Pi(\alpha)}=x_{\Pi(\alpha)}\right)=\mathscr{L}\left(X_{\alpha} \mid X_{\operatorname{adj}(\alpha)}=x_{\operatorname{adj}(\alpha)}\right)
$$

In terms of interpretation one can think of $X_{\alpha}$ as a response, of $\Pi(\alpha)$ as the possible influencing variables for $X_{\alpha}$ and of $\operatorname{adj}(\alpha)$ as the variables directly influencing $X_{\alpha}$.

A recursive univariate $C G$-regression is a distribution on $\mathscr{X}$ such that the conditional distributions (5.1) are univariate CG-regressions as described in Section 2. If these are all homogeneous we use the term recursive univariate HCG-regression.

In general such distributions are not CG. We have, however, the following proposition.

Proposition 5.1. If the ordering is strongly reducible any $\mathscr{G}$-order Markovian univariate recursive CG-regression is a $\mathscr{G}$-Markovian CG-distribution and vice versa.

Proof. That the Markov properties coincide is the corollary to the main theorem of Kiiveri, Speed and Carlin (1984). That the classes of distributions also coincide can be seen by an induction argument using Propositions 2.4, 3.1

and 3.4. But the result, as well as its converse if $\left|\mathscr{I}_{\delta}\right| \geq 2$ is a special case of Proposition 8.2 below, see also Frydenberg (1988).

Remark 5.2. If we do not pay attention to the Markovian properties, it is not difficult to show that an order Markovian recursive CG-regression is a $C G$-distribution if and only if $\operatorname{adj}(\delta) \subseteq \Delta$ for all $\delta \in \Delta$.

Remark 5.3. Proposition 5.1 (together with its converse) contains as special cases results of Wermuth (1980) in the case $\Delta=\varnothing$ and Wermuth and Lauritzen (1983) in the case $\Gamma=\varnothing$. So do the results of Kiiveri, Speed and Carlin (1984) whereas they do not consider distributional properties outside the Gaussian case.

Remark 5.4. Strongly reducible orderings exist by definition exactly for decomposable graphs so all Markovian CG-distributions on such graphs can be represented as order Markovian recursive CG-regressions after having chosen a suitable ordering.

Continuing the examples, consider first the oriented graph
![img-2.jpeg](img-2.jpeg)

It displays a strongly reducible ordering and the corresponding order Markovian recursive regressions are the same as the Markovian CG-distributions for the corresponding undirected graph
![img-3.jpeg](img-3.jpeg)
and this graph is thus decomposable. On the other hand, the graph
![img-4.jpeg](img-4.jpeg)
does not admit a strongly reducible ordering and the distributions specified for the oriented version of example 2
![img-5.jpeg](img-5.jpeg)
are different from those specified in Section 3. In fact, in the homogeneous case, the directed version has log density which looks like

$$
\begin{aligned}
\log f\left(i_{1}, i_{2}, y\right)= & \log f\left(i_{2} \mid y\right)+\log f\left(i_{1} \mid y\right)+\log f(y) \\
= & \text { const. }+u^{(2)}\left(i_{2}\right)+v^{(2)}\left(i_{2}\right) y+u^{(1)}\left(i_{1}\right)+v^{(1)}\left(i_{1}\right) y \\
& -\log \kappa^{(1)}(y)-\log \kappa^{(2)}(y)-\frac{1}{2} \psi y^{2}
\end{aligned}
$$

which is different from that in (3.4), even if $\psi^{(1)}\left(i_{1}\right)+\psi^{(2)}\left(i_{2}\right) \equiv \psi$. The normalizing constants $\kappa^{(1)}$ and $\kappa^{(2)}$ are the 'troublemakers.'

6. Recursive graphical models. The models discussed in this section are based on the CG-regressions discussed in Section 2. We consider the same observational scheme as in Section 4, that is, $N$ observations of vector random variables, each having a set of qualitative and a set of quantitative components. But now models are given by an oriented graph induced by a complete ordering $<$, that is, $\mathscr{G}^{\times}$such that the recursive graphical model corresponding to $\mathscr{G}$ is defined by assuming that the observations are realizations of $X^{(1)}, \ldots, X^{(N)}$, where $X^{(i)}$ are independent and identically distributed according to a distribution which is unknown, apart from the fact that it is a $\mathscr{G}$-order Markovian univariate recursive CG-regression (or HCG-regression).

Note that the recursive graphical models in the pure cases considered by Wermuth and Lauritzen (1983) and Wermuth (1980) are slightly more general than those defined here. The graphical chain models discussed in Section 8, however, are general enough to cover these as well.

The likelihood function factorizes into a product of conditional likelihood functions obtained by considering the conditional distribution of a variable $X_{\alpha}$ given its possible influences $X_{\{1(\alpha\}}$. Since by construction the parameters in each of these conditional distributions vary freely and independently of those in other conditional distributions, the likelihood function can be maximized by maximizing each factor separately. Let us derive an expression for such a conditional likelihood function in the case of a discrete variable $\alpha=\delta$ using expressions given in Section 2:

$$
\begin{aligned}
\log L= & \sum_{\nu=1}^{N} \log P\left\{X_{\delta}^{(\nu)}=i_{\delta}^{(\nu)} \mid X_{\operatorname{adj}(\delta)}^{(\nu)}=\left(i_{\Delta \operatorname{bd}(\delta)}^{(\nu)}, y_{\Gamma \operatorname{bd}(\delta)}^{(\nu)}\right)\right\} \\
= & \sum_{i_{d} \in \mathscr{I}_{\delta \cup \Delta \operatorname{bd}(\delta)}}\left[u^{\delta}\left(i_{\delta} \mid j\right) n\left(i_{d}\right)+v^{\delta}\left(i_{\delta} \mid j\right) S_{\delta}\left(i_{d}\right)+\operatorname{tr}\left(W^{\delta}\left(i_{\delta} \mid j\right) S P_{\delta}\left(i_{d}\right)\right)\right] \\
& -\sum_{\nu=1}^{N} \log \kappa^{\delta}\left(i_{\Delta \operatorname{bd}(\delta)}^{(\nu)}, y_{\Gamma \operatorname{bd}(\delta)}^{(\nu)}\right)
\end{aligned}
$$

where we have used the notation $\left(i_{\delta}, j\right)=i_{d}$ and
$n\left(i_{d}\right)=$ the number of observations with $i_{\delta \cup \Delta \operatorname{bd}(\delta)}^{(\nu)}=i_{d}$,
$S_{\delta}\left(i_{d}\right)=$ the sum of the values of $y_{\gamma}^{(\nu)}, \gamma \in \Gamma \operatorname{bd}(\delta)$, for those $\nu$, where $i_{\delta \cup \Delta \operatorname{bd}(\delta)}^{(\nu)}=i_{d}$,
$S P_{\delta}\left(i_{d}\right)=$ the matrix of sums of squares of products of the same $y_{\gamma}^{(\nu)}$-values.
As seen from the above expression (which is also well known) we have an exponential family likelihood with (conditionally) sufficient statistics

$$
\left[n\left(i_{d}\right), S_{\delta}\left(i_{d}\right), S P_{\delta}\left(i_{d}\right), i_{d} \in \mathscr{I}_{\delta \cup \Delta \operatorname{bd}(\delta)}\right]
$$

In the general case [ $\Gamma \operatorname{bd}(\delta) \neq \varnothing$ ] there is no reduction in the term involving the normalizing constant $\kappa^{\delta}$ and we have no explicit formula for the maximum likelihood estimates. Also there is in general no jointly sufficient reduction, because the terms involving $\kappa^{\delta}$ will not have the status of normalization

constants in the joint likelihood. Then the full data set might be needed to calculate maximum likelihood estimates.

In the case $\Gamma \mathrm{bd}(\delta=\varnothing)$, however, the likelihood function reduces to

$$
\log L=\sum_{i_{d} \in \mathscr{F}_{\delta \cup \Delta \operatorname{bd}(\delta)}} u^{\delta}\left(i_{\delta} \mid j\right) n\left(i_{d}\right)-\sum_{j \in \mathscr{F}_{\delta \operatorname{bd}(\delta)}} \log \kappa^{\delta}(j) n(j)
$$

and this is maximized by letting

$$
\hat{u}^{\delta}\left(i_{\delta} \mid j\right)=\log \frac{n\left(i_{d}\right)}{n(j)} \quad \text { and } \quad \hat{\kappa}^{\delta}(j)=1
$$

In the homogeneous case, we get essentially the same phenomena as above, just that now the $S P_{\delta}\left(i_{d}\right)$-terms are not needed in the set of sufficient statistics.

The regression problems for $\gamma \in \Gamma$ are univariate linear model problems with well-known explicit solutions.

To summarize, the joint likelihood function obtained by multiplying conditional likelihood functions together, has in general no nice properties of sufficiency and exponential family type. But each of the conditional likelihood functions has and a unique maximum likelihood estimate can be obtained by maximizing each factor. The maximization problems have an explicit solution in the continuous cases but we know only explicit solutions to the discrete cases when $\Gamma \operatorname{bd}(\delta)=\varnothing$. As a consequence, the pure cases $(\Gamma=\varnothing$ or $\Delta=\varnothing)$ always have an explicit solution.

Note especially that when the ordering is strongly reducible, $\Gamma \operatorname{bd}(\delta)=\varnothing$ for all $\delta \in \Delta$ and therefore the maximum likelihood estimates of the parameters can be found explicitly, see the next section.
7. Decomposable graphical models. Consider a graphical model of Markov type given by a decomposable undirected marked graph $\mathscr{G}=(\Delta \cup \Gamma, E)$. Since it is of the type considered in Section 4, we have an exponential family structure for the joint likelihood and sufficient reductions to marginal tables of counts, sums and sums of squares and products as described in that section.

By definition, a graph is decomposable if and only if a strongly reducible ordering < exists. By Proposition 5.1, any distribution in the family considered is also an order Markovian CG-regression and vice versa, whereby we conclude that the model is equivalent to the recursive graphical model given by the oriented graph $\mathscr{G}^{<}$. Since the ordering is strongly reducible, $\Gamma \mathrm{bd}(\delta)=\varnothing$ for all $\delta \in \Delta$, and we can obtain explicit estimates of the parameters in the recursive graphical model. Using the equivalence between the models once more, we can obtain explicit estimates of the parameters in the graphical model given by $\mathscr{G}$. It thus follows that such models have nice properties in terms of sufficient reductions as well as explicit solutions to the estimation problem. In general, a decomposable graph will admit several strongly reducible orderings and it thus follows that although their interpretations are different, all the corresponding recursive graphical models are identical and equal to the graphical model given by the undirected graph $\mathscr{G}$.

Each strongly reducible ordering of a decomposable graph represents a recursive dependence structure, thus characterizing decomposable graphical models as the subclass of graphical Markovian models for which an interpretation with recursively ordered responses applies.

We mention that it has been shown, Lauritzen (1985) that the likelihood ratio for testing one decomposable model versus another can be partitioned as a product of likelihood ratios for well-known linear models and/or conditional independence tests in contingency tables. This has been used by Williams (1976) in the discrete case and by Porteous (1985a) in the continuous case to obtain Bartlett corrections.
8. Graphical chain models. The notion of a Markovian graphical model and a recursive graphical model can be unified in the notion of a graphical chain model to be briefly described below. While a Markovian graphical model contains no arrows (undirected graph) and a recursive graphical model contains solely arrows (oriented graph) in its picture, the picture of a graphical chain model will in general contain both.

We consider a chain graph $\mathscr{G}=\mathscr{G}^{<}$with chain $V(1), \ldots, V(T)$ that we here shall refer to as a dependence chain.

We now let $D(\alpha)=\{\beta \mid \beta<\alpha$ and $\beta \neq \alpha\}$ and consider the chain Markov property

$$
\mathbf{C M}: \quad \alpha \Perp D(\alpha) \backslash \operatorname{adj}(\alpha) \mid \operatorname{adj}(\alpha)
$$

This specializes to the usual Markov property (M) if $T=1(\mathscr{G}=\overline{\mathscr{G}})$ and the order Markov property $\mathbf{O M}$ if $|V(t)| \equiv 1$.

A corresponding class of distributions is the class of recursive multivariate CG-regressions or HCG-regressions, that is, where the conditional distribution of $X_{V(t)}$ given $X_{W(t)}$, where

$$
W(t)=\bigcup_{l<t} V(l)
$$

is of the type considered in Section 3.
The graphical chain model given by $\mathscr{G}$ and the dependence chain $V(1), \ldots, V(T)$ is now obtained by assuming the observations to be realizations of independent identically distributed random variables, with a distribution being unknown, apart from the fact that it is a recursive multivariate CG-regression (or HCG-regression) satisfying the chain Markov property CM. Frydenberg (1986) has shown that two chain models with the same graph but different dependence chains are identical so that the model in fact is determined by the graph $\mathscr{G}$ alone and reference to the dependence chain can be omitted. As in the previous section, the likelihood function is most conveniently analysed by considering each of the conditional likelihood functions obtained from the conditional distributions of $x_{V(t)}$ given $X_{W(t)}$. We shall abstain from giving the details.

We have seen (Proposition 5.1) that under certain circumstances the models for symmetric associations and the directional models coincide. That is of independent interest and leads, for example, to the identification of the class of

decomposable models as in the previous section. But results on such equivalences can also be useful for a variety of other purposes, ranging from computational shortcuts in the fitting of models to aspects of resolving controversies about the interpretation of data, see, for example, Wermuth and Lauritzen $(1983,1989)$ for a discussion. A nonstandard example of an application is the recent work of Lauritzen and Spiegelhalter (1988) where ideas along these lines have been used to develop methods for efficient calculations with probabilities in expert systems. Here we just briefly state and illustrate the main results.

Proposition 8.1. If $\left|\mathscr{I}_{\delta}\right| \geq 2$ for all $\delta$, the graphical chain model given by $\mathscr{G}$ is equivalent to the Markovian graphical model given by $\overline{\mathscr{G}}$, if and only if the dependence chain is strongly reducible.

The results, in this generality, is due to Frydenberg (1988) and stated and proved there as Proposition 5.6. We therefore omit the proof. As an illustration of the use of the result, the models below are equivalent:
![img-6.jpeg](img-6.jpeg)
(the dependence chain is illustrated by boxes) implying, for example, that estimation in the model to the left can be performed in the model to the right, that is, ignoring the response structure, whereas this is not the case for the models
![img-7.jpeg](img-7.jpeg)

The model to the left specifies, for example, marginal independence of the variables in the left box, whereas the model to the right specifies conditional independence of the two, given the remaining variables. See Wermuth and Lauritzen (1989) for a wide range of similar examples.

The corresponding conditions for coincidence between recursive models and graphical chain models are briefly stated below, in the case where the orderings involved in the recursive model $(\prec)$ and in the chain model $(<)$ are assumed compatible, that is, no arrows in one graph are reversed in the other.

Proposition 8.2. If a complete ordering $\curlyvee$ is locally strongly reducible and compatible, the graphical chain model given by $\mathscr{G}$ and the recursive graphical model given by $\mathscr{G}^{\curlyvee}$ are equivalent.

Proposition 8.3. If a complete ordering $\curlyvee$ is strongly reducible and compatible, the graphical chain model given by $\mathscr{G}$, the Markovian graphical model given by $\mathscr{G}$ and the recursive graphical model given by $\mathscr{G}^{\curlyvee}$ are all equivalent.

Proof. Propositions 8.2 and 8.3 are proved by induction on $T$ and repeated use of Proposition 5.1.

We believe the conditions above to be necessary as well although no formal proof has been established.

A short illustration of this: The two models below are equivalent
![img-8.jpeg](img-8.jpeg)
by Proposition 8.2 and the three models below are by Proposition 8.3,
![img-9.jpeg](img-9.jpeg)
implying that the graph to the far right is decomposable.

# APPENDIX A 

Graph theory. Graph-theoretic aspects of the models considered in the present article were first discussed by Lauritzen and Wermuth (1984). Since then, a thorough study of this has been performed by Leimer (1985, 1989). This had led to considerable improvements of the terminology and of the general understanding of such graphs. We here just give a minimal treatment and refer the reader to the above for details.

Our graphs are simple, that is, there are no loops or multiple edges. The vertices are marked, reflecting the necessity to keep track of two kinds of variables.

A marked graph consists of a finite set $V$ of vertices, partitioned into two disjoint subsets $V=\Delta \cup \Gamma$, and a collection $E$ of edges being a subset of the set of ordered pairs of distinct elements of $V$. We write $\mathscr{G}=(V, E)$ or $\mathscr{G}=$ $(\Delta \cup \Gamma, E)$.

It is important that the properties of our graphs, which refer specifically to the two types of vertices are not symmetric in $\Delta$ and $\Gamma$. Vertices in $\Delta$ are supposed to represent discrete variables and $\Gamma$ continuous variables, and they do play different roles. We shall use discrete and continuous for the vertices $\Delta$ and $\Gamma$, respectively. If either $\Delta$ or $\Gamma$ is empty, the graph is pure.

We represent the graph by a picture with discrete vertices as dots and continuous vertices as circles.

An edge $(\alpha, \beta) \in E$ is represented by an arrow from $\alpha$ to $\beta$ if $(\beta, \alpha) \notin E$, and by a line between $\alpha$ and $\beta$ if both $(\alpha, \beta) \in E$ and $(\beta, \alpha) \in E$. Examples are in the main body of the article.

A graph is called undirected if there are no arrows in the picture, otherwise we call it a directed graph.

A graph is called oriented if the picture has solely arrows and no lines.
The symmetrization of $\mathscr{G}$ of a graph $\mathscr{G}$ is obtained from $\mathscr{G}$ by substituting lines for arrows all over.

A special type of directed graph occurs when the vertex set is partitioned into an ordered sequence of subsets $V(1), \ldots, V(T)$ to be called a chain.

The chain induces a partial order $<$ on the vertices as

$$
\alpha<\beta \quad \Leftrightarrow \exists s, t, \quad \alpha \in V(s), \quad \beta \in V(t), \quad s \leq t
$$

We then define for $\mathscr{G}=(V, E)$ the induced chain graph $\mathscr{G}^{<}=\left(V, E^{<}\right)$as

$$
(\alpha, \beta) \in E^{<} \quad \Leftrightarrow \quad(\alpha, \beta) \in E \quad \wedge \quad \alpha<\beta
$$

The chain graph has lines between vertices in the same chain element and arrows between vertices in different elements, all arrows pointing from low to high.

If $|V(t)| \equiv 1$, we have a complete ordering of the vertices and $\mathscr{G}^{<}$will be an oriented graph. If only $V(1)$ has more than one element, $\mathscr{G}^{<}$will be what Kiiveri, Speed and Carlin (1984) call a recursive causal graph.

The subgraph induced by a subset $A \subseteq V$ of the vertex set given as $\mathscr{G}_{A}=$ $\left(A, E_{A}\right)$ where $E_{A}=E \cap(A \times A)$.

A graph is complete if all pairs of distinct vertices are connected with an arrow or a line.

A subset is complete if it induces a complete subgraph. A maximal (w.r.t. inclusion) complete subset is called a clique.

To a graph $\mathscr{G}$ corresponds its adjacency function, given as

$$
\alpha \in \operatorname{adj}(\beta) \quad \Leftrightarrow \quad(\alpha, \beta) \in E
$$

that is, the vertices $\alpha$ adjacent to $\beta$ are those being the starting point of arrows pointing toward $\beta$ or lines between $\alpha$ and $\beta$. Note that this is reversed compared to Golumbic (1980).

If $\mathscr{G}$ is undirected we have

$$
\alpha \in \operatorname{adj}(\beta) \quad \Leftrightarrow \quad \beta \in \operatorname{adj}(\alpha)
$$

and $\alpha$ and $\beta$ are called adjacent or neighbours.
For $A \subseteq V$ we define its boundary and closure as

$$
\operatorname{bd}(A)=\bigcup_{\alpha \in A} \operatorname{adj}(\alpha) \cap(V \backslash A), \quad \operatorname{cl}(A)=A \cup \operatorname{bd}(A)
$$

the boundary of $A$ thus being all vertices adjacent to some vertex $\alpha \in A$.
With special reference to marked graphs we also define the discrete and continuous boundaries as

$$
\Delta \operatorname{bd}(A)=\operatorname{bd}(A) \cap \Delta, \quad \Gamma \operatorname{bd}(A)=\operatorname{bd}(A) \cap \Gamma
$$

A path of length $n$ from $\alpha$ to $\beta$ is a sequence of vertices $\alpha=\alpha_{0}, \alpha_{1}, \ldots, \alpha_{n}=\beta$, such that $\left(\alpha_{i-1}, \alpha_{i}\right) \in E$ for all $i=1, \ldots, n$, and all vertices except possibly $\alpha$ and $\beta$ are distinct. If $\alpha=\beta$ the path is a cycle.

A cycle is chordless if only consecutive elements are joined with edges.
Two disjoint subsets $A$ and $B$ are said to be separated by a subset $C$ (disjoint from $A$ and $B$ ) if all paths from $A$ to $B$ contain vertices from $C$.

A vertex $\alpha$ is called simplicial if its adjacency set is complete and with special reference to marked graphs, a vertex $\alpha$ is strongly simplicial if it is simplicial and $\alpha \in \Gamma$ or $\operatorname{adj}(\alpha) \subseteq \Delta$. In words, a discrete simplicial vertex is supposed to have only discrete vertices in its adjacency set. Note the asymmetry in this definition, and that, if $\mathscr{G}$ is pure, any simplicial vertex is strongly simplicial. The vertices underlined are simplicial in the graphs below and those double underlined are strongly simplicial:
![img-10.jpeg](img-10.jpeg)

We generalize this notion to subsets $A$ by saying that $A$ is simplicial if its boundary $\operatorname{bd}(A)$ is complete and strongly simplicial if further $A \subseteq \Gamma$ or $\operatorname{bd}(A) \subseteq \Delta$.

Following Frydenberg $(1986,1988) A$ is called a (strongly) simplicial collection if all connected components $A_{1}, \ldots, A_{p}$ of the subgraph $\mathscr{G}_{A}$ are (strongly) simplicial in $\mathscr{G}$.

An ordering induced by a chain $V(1), \ldots, V(T)$ is called (strongly) reducible if all chain elements are (strongly) simplicial collections in the induced chain graph $\mathscr{G}^{\times}$. This extends the notion of a reducible numbering as used by Wermuth (1980) and Wermuth and Lauritzen (1983).

A complete ordering $\nless$ of the vertices in a chain graph is said to be compatible if

$$
\alpha \nless \beta \quad \Rightarrow \quad \alpha<\beta
$$

where the right inequality sign refers to the ordering given by the chain graph.
A compatible ordering is locally reducible if $\rho \in V(t)$ and $\alpha, \beta \in \operatorname{adj}^{\kappa}(\rho)$ implies

$$
\alpha \in \operatorname{adj}^{\kappa}(\beta) \quad \text { or } \quad \beta \in \operatorname{adj}^{\kappa}(\alpha) \quad \text { or } \quad \alpha, \beta \notin V(t)
$$

It is locally strongly reducible if also

$$
\rho \in \Gamma \quad \text { or } \quad \operatorname{adj}^{\kappa}(\rho) \cap V(t)=\varnothing
$$

Of special interest to us is the class of triangulated graphs, these being undirected graphs with no chordless cycles of length $\geq 4$. These have been extensively studied by Dirac (1961) and many authors, occasionally under other names. For further information on this issue see Berge (1973), Golumbic (1980), Lauritzen, Speed and Vijayan (1984) and Darroch, Lauritzen and Speed (1980) together with references therein. The following results can be found in Golumbic (1980).

Proposition A.1. An undirected graph is triangulated if and only if there exists a reducible ordering of the vertices.

Proposition A.2. Any triangulated graph has at least one simplicial vertex.
Proposition A.3. If $\mathscr{G}$ is triangulated and $A$ is a subset of $V$, then $\mathscr{G}_{A}=\left(A, E_{A}\right)$ is triangulated.

These results automatically give an algorithm for recognizing triangulated graphs. First, look for a simplicial vertex. If such a vertex does not exist, the graph is not triangulated. Otherwise, remove the simplicial vertex $\alpha$ by forming the graph $\mathscr{G}_{V \backslash\{\alpha\}}$. Repeat the procedure on the subgraph of $\mathscr{G}$. Either we get at some stage a graph without a simplicial vertex and the graph is not triangulated, or we end up with the empty graph. Introduce now the ordering of $V$,

$$
\alpha<\beta \quad \Leftrightarrow \quad \beta \quad \text { was removed before } \alpha
$$

This ordering will necessarily be reducible since the adjacency set of any vertex in $\mathscr{G}^{<}$exactly will be its adjacency set in the subgraph that is left over just before it has been removed. This algorithm is inefficient in terms of computing time but a fast algorithm exists; see Tarjan and Yannakakis (1984). Motivated by these algorithms, we state

Definition A.4. An undirected marked graph $\mathscr{G}=(\Delta \cup \Gamma, E)$ is called decomposable if there exists a strongly reducible ordering of $\Delta \cup \Gamma$.

The definition fits well with an algorithm of the type just described but also the fast algorithms can be generalized; see Leimer (1989).

In the pure cases an undirected graph is decomposable if and only if it is triangulated; cf. Proposition A.1.

# APPENDIX B 

CG-Markov = CG-nearest-neighbour Gibbs. The proof of Proposition 3.1 is basically a modification of the standard proof of the result in the discrete case. We first need a lemma.

Lemma B. 1 (Möbius inversion). Let $H$ and $K$ be functions defined on the subsets of a finite set $A$ and taking values in an Abelian group. Then the following are equivalent:

$$
\begin{array}{ll}
\forall a \subseteq A: & H(a)=\sum_{b \subseteq a} J(b) \\
\forall a \subseteq A: & J(a)=\sum_{b \subseteq a}(-1)^{|a \backslash b|} H(b)
\end{array}
$$

For a proof, see, for example, Aigner (1979).
Let $f$ be the density of a CG-distribution and let its logarithm be expressed as in (3.2) with interaction terms satisfying (3.3), that is, with only interactions among neighbours. Let $\alpha \notin \operatorname{adj}(\beta)$. We have to show

$$
\alpha \Perp \beta \mid V \backslash\{\alpha, \beta\}
$$

But this follows from (3.2) and from conditional independence, since no interaction terms involving both $x_{\alpha}$ and $x_{\beta}$ will be present in (3.2) thus giving a factorization of the density $f$ into a function not depending on $x_{\alpha}$ and one not depending on $x_{\beta}$.

The reverse implication demands a somewhat more complicated argument, since we have to construct a representation (3.2) and afterwards show that it satisfies (3.3). This is where the Möbius inversion lemma shall prove useful.

First we define elements of $\mathscr{I}$ depending on $d \subseteq \Delta$ as follows: Choose a fixed but arbitrary $i^{*} \in \mathscr{I}$. For $i \in \mathscr{I}$, let $i(d) \in \mathscr{I}$ be given as the "substituted" element

$$
i(d)_{\delta}= \begin{cases}i_{\delta} & \text { if } \delta \in d \\ i_{\delta}^{*} & \text { if } \delta \notin d\end{cases}
$$

Thus, for example, we have $i(\Delta)=i, i(\varnothing)=i^{*}$.
Let a density $f$ of a CG-distribution be given by the expression (3.1) and define the functions

$$
\rho_{d}(i)=g(i(d)), \quad \xi_{d}(i)=h(i(d)), \quad \Phi_{d}(i)=K(i(d))
$$

and further for $a \subseteq \Delta$,

$$
\begin{aligned}
& \lambda_{a}(i)=\sum_{d \subset a}(-1)^{|a \backslash d|} \rho_{d}(i) \\
& \eta_{a}(i)=\sum_{d \subset a}(-1)^{|a \backslash d|} \xi_{d}(i) \\
& \Psi_{a}(i)=\sum_{d \subset a}(-1)^{|a \backslash d|} \Phi_{d}(i)
\end{aligned}
$$

For fixed $i \in I$, the functions entering into (B.2) can be considered as functions on the subsets of $\Delta$ into the groups $(\mathbb{R},+),\left(\mathbb{R}^{k},+\right),\left(\mathbb{R}^{k \times k},+\right)$, and Lemma B. 1 applies. In the special case where $d=\Delta, i(\Delta)=i$, we get from (B.1)

$$
\begin{aligned}
& \rho_{\Delta}(i)=g(i)=\sum_{d \subset \Delta} \lambda_{d}(i) \\
& \xi_{\Delta}(i)=h(i)=\sum_{d \subset \Delta} \eta_{d}(i) \\
& \Phi_{\Delta}(i)=K(i)=\sum_{d \subset \Delta} \Psi_{d}(i)
\end{aligned}
$$

and we have constructed a representation of the form (3.2) for the density $f$. What remains to be shown is that also (3.3) is satisfied. The necessary trick is to identify terms in the expansions with particular values of the density and then to use (B.2) and the Markov property to see that zeros occur.

We first define the vector $e(\alpha) \in \mathbb{R}^{T}$ as that with one in position $\alpha$ and zero elsewhere.

We then have the following expressions for the terms in (B.1):

$$
\begin{aligned}
\rho_{d}(i)= & \log f(i(d), 0) \\
\xi_{d}(i)_{\alpha}= & 2 \log f(i(d), e(\alpha))-\frac{1}{2} \log f(i(d), 2 e(\alpha)) \\
& -\frac{3}{2} \log f(i(d), 0)
\end{aligned}
$$

and, if $\alpha \neq \beta$,

$$
\begin{aligned}
\Phi_{d}(i)_{\alpha \beta}= & \log f(i(d), e(\alpha)) .-\log f(i(d), e(\alpha)+e(\beta)) \\
& +\log f(i(d), e(\beta))-\log f(i(d), 0)
\end{aligned}
$$

whereas

$$
\begin{aligned}
\Phi_{d}(i)_{\alpha \alpha}= & 2 \log f(i(d), e(\alpha))-\log f(i(d), 2 e(\alpha)) \\
& -\log f(i(d), 0)
\end{aligned}
$$

Suppose now that $d$ is not complete. Then there exist $\delta, \varepsilon \in d$ nonadjacent, which by the Markov property implies that $\{\delta\} \underline{z}\{\varepsilon\} \mid V \backslash\{\delta, \varepsilon\}$. Using now

(B.2) and (B.3), we get

$$
\begin{aligned}
\lambda_{d}(i) & =\sum_{a \in d}(-1)^{|d \backslash a|} \rho_{a}(i) \\
& =\sum_{a \in d \backslash\{\delta, \epsilon\}}(-1)^{|d \backslash a|}\left[\rho_{a \cup\{\delta, \epsilon\}}(i)-\rho_{a \cup\{\epsilon\}}(i)-\rho_{a \cup\{\delta\}}(i)+\rho_{a}(i)\right] \\
& =\sum_{a \in d \backslash\{\delta, \epsilon\}}(-1)^{|d \backslash a|} \log \frac{f(i(a \cup\{\delta, \epsilon\}), 0) f(i(a), 0)}{f(i(a \cup\{\delta\}), 0) f(i(a \cup\{\epsilon\}), 0)}
\end{aligned}
$$

In each of the terms in the above ratios, we have $X_{a}=i_{a}, X_{b}=i_{b}^{*}, X_{\Gamma}=0$, where $b=\Delta \backslash(a \cup\{\delta, \epsilon\})$. Conditioning on this, we obtain that the ratios are equal to

$$
\begin{aligned}
& \left(P\left\{X_{\{\delta, \epsilon\}}=\left(i_{\delta}, i_{\epsilon}\right) \mid X_{a}=i_{a}, X_{b}=i_{b}^{*}, X_{\Gamma}=0\right\}\right. \\
& \left.\times P\left\{X_{\{\delta, \epsilon\}}=\left(i_{\delta}^{*}, i_{\epsilon}^{*}\right) \mid X_{a}=i_{a}, X_{b}=i_{b}^{*}, X_{\Gamma}=0\right\}\right) \\
& \quad \div\left(P\left\{X_{\{\delta, \epsilon\}}=\left(i_{\delta}, i_{\epsilon}^{*}\right) \mid X_{a}=i_{a}, X_{b}=i_{b}^{*}, X_{\Gamma}=0\right\}\right. \\
& \left.\quad \times P\left\{X_{\{\delta, \epsilon\}}=\left(i_{\delta}^{*}, i_{\epsilon}\right) \mid X_{a}=i_{a}, X_{b}=i_{b}^{*}, X_{\Gamma}=0\right\}\right)
\end{aligned}
$$

This ratio is equal to one by conditional independence, and thus $\lambda_{d}(i) \equiv 0$.
Using the same kind of argument for $\eta_{d}$ and $\Psi_{d}$ gives $\eta_{d} \equiv \Psi_{d} \equiv 0$ just that the corresponding term inside square brackets has to be split into three or four terms depending on whether (B.4), (B.5) or (B.6) is used.

If $d$ is complete but $d \cup\{\gamma\}$ is not, there must be a $\delta \in d$ with $\delta \notin \operatorname{adj}(\gamma)$. Then

$$
\eta_{d}(i)_{\gamma}=\sum_{a \in d \backslash\{\delta\}}(-1)^{|d \backslash a|}\left(\xi_{a}(i)_{\gamma}-\xi_{a \cup\{\delta\}}(i)_{\gamma}\right)
$$

Using now (B.4) and conditional independence, we obtain $\eta_{d}(i)_{\gamma} \equiv 0$, and similarly for $\psi_{d}$.

Finally, if $d \cup\{\gamma\}$ is complete and also $d \cup\{\mu\}$ but not $d \cup\{\gamma, \mu\}$, we must have $\gamma \notin \operatorname{adj}(\mu)$ and thus $\{\gamma\} \pm\{\mu\} \mid V \backslash\{\gamma, \mu\}$. From (B.5) we get $\Phi_{d}(i)_{\gamma \mu} \equiv 0$ and by (B.2)

$$
\Psi_{d}(i)_{\gamma \mu}=\sum_{a \in d}(-1)^{|d \backslash a|} \Phi_{a}(i)_{\gamma \mu} \equiv 0
$$

Proposition 3.1 has been proved.

Acknowledgments. We are indebted to Morten Frydenberg, Finn Søholm Larsen, Hanns-Georg Leimer, Klaus Rostgaard and several referees for critical readings of earlier versions of this article leading to the correction of errors and other improvements.
