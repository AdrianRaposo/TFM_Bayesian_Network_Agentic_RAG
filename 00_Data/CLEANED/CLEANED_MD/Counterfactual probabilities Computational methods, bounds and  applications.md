# Counterfactual Probabilities: Computational Methods, Bounds and Applications 

Alexander Balke<br>Cognitive Systems Laboratory<br>University of California<br>Los Angeles, CA 90024<br>balke@cs.ucla.edu

## Abstract

Evaluation of counterfactual queries (e.g., "If $A$ were true, would $C$ have been true?") is important to fault diagnosis, planning, and determination of liability. In this paper we present methods for computing the probabilities of such queries using the formulation proposed in [Balke and Pearl, 1994], where the antecedent of the query is interpreted as an external action that forces the proposition $A$ to be true. When a prior probability is available on the causal mechanisms governing the domain, counterfactual probabilities can be evaluated precisely. However, when causal knowledge is specified as conditional probabilities on the observables, only bounds can computed. This paper develops techniques for evaluating these bounds, and demonstrates their use in two applications: (1) the determination of treatment efficacy from studies in which subjects may choose their own treatment, and (2) the determination of liability in product-safety litigation.

## 1 INTRODUCTION

A counterfactual sentence has the form
If $A$ were true, then $C$ would have been true
where $A$, the counterfactual antecedent, specifies an event that is contrary to one's real-world observations, and $C$, the counterfactual consequent, specifies a result that is expected to hold in the alternative world where the antecedent is true. A typical instance is "If Oswald were not to have shot Kennedy, then Kennedy would still be alive" which presumes the factual knowledge of Oswald's shooting Kennedy, contrary to the antecedent of the sentence.
Because of the tight connection between counterfactuals and causal influences, any algorithm for computing solutions to counterfactual queries must rely heavily on causal knowledge of the domain. This leads naturally to the use of probabilistic causal networks, since these

## Judea Pearl <br> Cognitive Systems Laboratory <br> University of California <br> Los Angeles, CA 90024 <br> judea@cs.ucla.edu

networks combine causal and probabilistic knowledge and permit reasoning from causes to effects as well as, conversely, from effects to causes.
To emphasize the causal character of counterfactuals, we adopt the interpretation in [Pearl, 1993b], according to which a counterfactual sentence "If it were $A$, then $B$ would have been" states that $B$ would prevail if $A$ were forced to be true by some unspecified action that is exogenous to the other relationships considered in the analysis.
Causal theories specified in functional form (as in [Pearl and Verma, 1991, Druzdzel and Simon, 1993, Poole, 1993]) are sufficient for evaluating counterfactual queries, whereas the causal information embedded in Bayesian networks is not sufficient for the task. Every Bayes network can be represented by several functional specifications, each yielding different evaluations of a counterfactual. The problem is that, deciding what factual information deserves undoing (by the antecedent of the query) requires a model of temporal persistence, and, as noted in [Pearl, 1993c], such a model is not part of static Bayesian networks. Functional specifications, however, implicitly contain the needed temporal persistence information.
Consider an example with two variables $A$ and $B$, representing Ann and Bob's attendance, respectively, at a party ( $A=a_{1}$ when Ann is at the party, $A=a_{0}$ otherwise; $B=b_{1}$ when Bob is at the party, $B=b_{0}$ otherwise), and it is believed that Ann's attendance has a causal influence on Bob's attendance, shown by the arrow $A \rightarrow B$ ). Assume that previous behavior shows $P\left(b_{1} \mid a_{1}\right)=0.9$ and $P\left(b_{0} \mid a_{0}\right)=0.9$. We observe that Bob and Ann are absent from the party and we wonder whether Bob would be there if Ann were there. The answer depends on the mechanism that accounts for the $10 \%$ exception in Bob's behavior. If the reason Bob occasionally misses parties (when Ann goes) is that he is unable to attend (e.g., being sick or having to finish a paper for UAI), then the answer to our query would be $90 \%$. However, if the only reason for Bob's occasional absence (when Ann goes) is that he becomes angry with Ann (in which case he does exactly the opposite of what she does), then the answer to our query is $100 \%$, because Ann and Bob's current absence from the party proves that Bob is not angry.

Thus, we see that the information contained in the conditional probabilities on the observed variables is insufficient for answering counterfactual queries uniquely; some information about the mechanisms responsible for these probabilities is needed as well. Still, when only a probabilistic model is given, informative bounds on the counterfactual probabilities can often be derived, and this paper provides a general framework for evaluating these bounds.

The next section will introduce concise notation for expressing counterfactual queries. Section 3.2 will derive a general expression for counterfactual probabilities in terms of a functional specification. Section 3.3 will present a general procedure for evaluating bounds on counterfactual probabilities when only a probabilistic specification is supplied. Section 4 will apply this procedure for evaluating bounds on treatment effects in partial compliance studies, while Section 5 will demonstrate the use of this procedure in product liability litigation.

## 2 NOTATION

Let the set of variables describing the world be designated by $X=\left\{X_{1}, X_{2}, \ldots, X_{n}\right\}$. As part of the complete specification of a counterfactual query, there are real-world observations that make up the background context. These observed values will be represented in the standard form $x_{1}, x_{2}, \ldots, x_{n}$. In addition, we must represent the value of the variables in the counterfactual world. To distinguish between $x_{i}$ and the value of $X_{i}$ in the counterfactual world, we will denote the latter with an asterisk; thus, the value of $X_{i}$ in the counterfactual world will be represented by $x_{i}^{*}$. We will also need a notation to distinguish between events that might be true in the counterfactual world and those referenced explicitly in the counterfactual antecedent. The latter are interpreted as being forced to the counterfactual value by an external action, which will be denoted by a hat (e.g., $\bar{x}$ ).
Thus, a typical counterfactual query will have the form "What is $P\left(c^{*} \mid \hat{a}^{*}, a, b\right)$ ?" to be read as "Given that we have observed $A=a$ and $B=b$ in the real world, if $A$ were $\hat{a}^{*}$, then what is the probability that $C$ would have been $c^{*}$ ?"

## 3 BOUNDS ON COUNTERFACTUALS

In [Balke and Pearl, 1994], an algorithm was presented for evaluating the unique quantitative solutions to counterfactual queries when a functional model is given. In this section we briefly describe the form of the functional model using response-function variables and how the solution is evaluated uniquely. Then we deal with probabilistic specifications and show how bounds can be obtained by optimizing the solution above over all functional models consistent with the probabilistic specification.

### 3.1 FUNCTIONAL MODELS

For the previously described party example, a functional specification models the influence of Ann's attendance $(A)$ on Bob's attendance $(B)$ by a deterministic function

$$
b=F_{b}\left(a, \epsilon_{b}\right)
$$

where $\epsilon_{b}$ stands for all unknown factors that may influence $B$ and the prior probability distribution $P\left(\epsilon_{b}\right)$ quantifies the likelihood of such factors. For example, whether Bob has been grounded by his parents and whether Bob is angry at Ann could make up two possible components of $\epsilon_{b}$. Given a specific value for $\epsilon_{b}$, $B$ becomes a deterministic function of $A$; hence, each value in $\epsilon_{b}$ 's domain specifies a response function that maps each value of $A$ to some value in $B$ 's domain. In general, the domain for $\epsilon_{b}$ could contain many components, but it can always be replaced by an equivalent variable that is minimal, by partitioning the domain into equivalence regions, each corresponding to a single response function [Pearl, 1993a]. Formally, these equivalence classes can be characterized as a function $r_{b}: \operatorname{dom}\left(\epsilon_{b}\right) \rightarrow \mathbf{N}$, as follows:
$r_{b}\left(\epsilon_{b}\right)=\left\{\begin{array}{ll}0 & \text { if } F_{b}\left(a_{0}, \epsilon_{b}\right)=0 \& F_{b}\left(a_{1}, \epsilon_{b}\right)=0 \\ 1 & \text { if } F_{b}\left(a_{0}, \epsilon_{b}\right)=0 \& F_{b}\left(a_{1}, \epsilon_{b}\right)=1 \\ 2 & \text { if } F_{b}\left(a_{0}, \epsilon_{b}\right)=1 \& F_{b}\left(a_{1}, \epsilon_{b}\right)=0 \\ 3 & \text { if } F_{b}\left(a_{0}, \epsilon_{b}\right)=1 \& F_{b}\left(a_{1}, \epsilon_{b}\right)=1\end{array}\right.$
Obviously, $r_{b}$ can be regarded as a random variable that takes on as many values as there are functions between $A$ and $B$. We will refer to this domainminimal variable as a response-function variable. $r_{b}$ is closely related to the potential response variables in Rubin's model of counterfactuals [Rubin, 1974], which was introduced to facilitate causal inference in statistical analysis [Balke and Pearl, 1993].
For this example, the response-function variable for $B$ has a four-valued domain $r_{b} \in\{0,1,2,3\}$ with the following functional specification:

$$
b=f_{b}\left(a, r_{b}\right)=h_{b, r_{b}}(a)
$$

where the mappings defined by each response function $h_{b, r_{b}}(a)$ are given by

$$
\begin{array}{ll}
h_{b, 0}(a)=b_{0} & , h_{b, 1}(a)= \begin{cases}b_{0} & \text { if } a=a_{0} \\
b_{1} & \text { if } a=a_{1}\end{cases} \\
h_{b, 3}(a)=b_{1} & , \quad h_{b, 2}(a)= \begin{cases}b_{1} & \text { if } a=a_{0} \\
b_{0} & \text { if } a=a_{1}\end{cases}
\end{array}
$$

The response-function variable for $A$ has a two-valued domain $r_{a} \in\{0,1\}$ with the functional specification:

$$
a=f_{a}\left(r_{a}\right)=h_{a, r_{a}}()
$$

where

$$
h_{a, 0}()=a_{0} \quad, \quad h_{a, 1}()=a_{1}
$$

The prior probability on the response functions $P\left(r_{b}\right)$ and $P\left(r_{a}\right)$ in conjunction with $f_{b}\left(a, r_{b}\right)$ and $f_{a}\left(r_{a}\right)$ fully parameterizes the model.

For each observable variable $X_{i}$, there will be a function that maps the value of $X_{i}$ 's observable causal influences $\mathrm{pa}\left(X_{i}\right)$ and $X_{i}$ 's response-function variable $r_{x_{i}}$ to the value of $X_{i}$

$$
x_{i}=f_{x_{i}}\left(\mathrm{pa}\left(x_{i}\right), r_{x_{i}}\right)
$$

If the model is complete (such as the functional model described in [Pearl and Verma, 1991]), all response functions will be mutually independent, and each will be characterized by a prior probability $P\left(r_{x_{i}}\right)$. However, when some variables are left out of the analysis, the response functions of the remaining variables $\left(x_{1}, \ldots, x_{n}\right)$ may be dependent and, in principle, a joint probability $P\left(r_{x_{1}}, \ldots, r_{x_{n}}\right)$ would be required. In practice, only local dependencies will be needed.
If one assumes that two variables $A$ and $B$ are dependent via some exogenous common cause, then we create an edge between $r_{a}$ and $r_{b}$ and specify the joint distribution $P\left(r_{a}, r_{b}\right)$. This treatment of latent variables will be utilized in the applications discussed in Sections 4 and 5 .

### 3.2 FUNCTIONAL EXPRESSION

We now derive an expression for $P\left(c^{*}\left|\hat{a}^{*}, o\right)\right.$ in terms of the underlying functional model.
The connection between the factual and counterfactual worlds is discussed in [Balke and Pearl, 1994] where it is argued that the response-function variables should assume the same values in both worlds. For the party example, this invariance allows the response function variables $r_{a}$ and $r_{b}$ to be shared between the networks corresponding to the two worlds (see Figure 1).
![img-0.jpeg](img-0.jpeg)

Figure 1: Factual $(A, B)$ and counterfactual $\left(A^{*}, B^{*}\right)$ worlds for the functional analysis of the structure $A$ B. The response-function variables $r_{a}$ and $r_{b}$ (summarizing all exogenous influences on $A$ and $B$ ) attain the same value in the real and counterfactual worlds.

Let $\mathbf{r}=\left(r_{x_{1}}, r_{x_{2}}, \ldots, r_{x_{n}}\right)$ represent the set of response-function variables for all the variables in the model. Given the value of $\mathbf{r}$, all variables $X_{i} \in X$ are functionally determined according to the recursive function:

$$
\begin{aligned}
x_{i} & =f_{x_{i}}(\mathbf{r}) \\
& =f_{x_{i}}\left(f_{u_{1}}(\mathbf{r}), f_{u_{2}}(\mathbf{r}), \ldots, f_{u_{k}}(\mathbf{r}), r_{x_{i}}\right)
\end{aligned}
$$

where $\mathrm{pa}\left(X_{i}\right)=\left\{U_{1}, U_{2}, \ldots, U_{k}\right\} \subset X$ are the causal influences of $X_{i}$ in the model.

If a set of variables $A \subset X$ in the model are externally forced to the value $\hat{a}$, then according to the actionbased semantics of [Pearl, 1993a], the recursive function becomes

$$
\begin{aligned}
x_{i} & =f_{x_{i}}^{\hat{a}}(\mathbf{r}) \\
& =\left\{\begin{array}{ll}
\hat{x_{i}} & \text { if } X_{i} \in A \\
f_{x_{i}}\left(r_{x_{i}}\right) & \text { if } X_{i} \notin A \text { and } \mathrm{pa}\left(X_{i}\right)=\emptyset \\
f_{x_{i}}\left(f_{u_{1}}^{\hat{a}}(\mathbf{r}), f_{u_{2}}^{\hat{a}}(\mathbf{r}), \ldots, f_{u_{k}}^{\hat{a}}(\mathbf{r}), r_{x_{i}}\right) & \text { otherwise }
\end{array}\right.
\end{aligned}
$$

The counterfactual probability $P\left(c^{*}\left|\hat{a}^{*}, o\right)\right.$ may be rewritten

$$
P\left(c^{*}\left|\hat{a}^{*}, o\right)=\frac{P\left(c^{*}, o \mid \hat{a}^{*}\right)}{P\left(o \mid \hat{a}^{*}\right)}\right.
$$

Since an action can only affect its descendants in the graph [Pearl, 1994] we have $P(o \mid \hat{a})=P(o)$ which is readily computed from the probabilistic specification.
$P\left(c^{*}, o \mid \hat{a}^{*}\right)$ may be evaluated in terms of the functional model by summing the probabilities of the responsefunction configurations which are consistent with the arguments $\left(c^{*}, \hat{a}^{*}, o\right)$. Formally,

$$
P\left(c^{*}, o \mid \hat{a}^{*}\right)=\sum_{\mathbf{r} \in R} P(\mathbf{r})
$$

where
$R=\left\{\mathbf{r} \mid \forall_{x_{i} \in o}\left[x_{i}=f_{x_{i}}(\mathbf{r})\right]\right.$ and $\left.\forall_{x_{j}^{*} \in c^{*}}\left[x_{j}^{*}=f_{x_{j}}^{\hat{a}}(\mathbf{r})\right]\right\}$
Hence, the counterfactual probability may be written in terms of the structure $\left\{\mathrm{pa}\left(x_{i}\right)\right\}$ and parameters $P(\mathbf{r})$ of the functional model:

$$
P\left(c^{*}\left|\hat{a}^{*}, o\right)=\frac{\sum_{\mathbf{r} \in R} P(\mathbf{r})}{P(o)}\right.
$$

In the next section this expression will be optimized under the constraints imposed by the probabilistic specification.

### 3.3 CONSTRAINTS AND OPTIMIZATION

The probabilistic specification $P\left(x_{i} \mid \mathrm{pa}\left(x_{i}\right)\right)$ for a complete model imposes a set of constraints on $P\left(r_{x_{i}}\right)$ of the form

$$
P\left(x_{i} \mid \mathrm{pa}\left(x_{i}\right)\right)=\sum_{r_{x_{i}}} P\left(r_{x_{i}}\right) t\left(r_{x_{i}} ; x_{i}, \mathrm{pa}\left(x_{i}\right)\right)
$$

where the characteristic function $t$ indicates which values of $r_{x_{i}}$ map the particular value of $X_{i}$ 's causal influences $\left(\mathrm{pa}\left(x_{i}\right)\right)$ to the specific value of $X_{i}\left(x_{i}\right)$, i.e.

$$
t\left(r_{x_{i}} ; x_{i}, \mathrm{pa}\left(x_{i}\right)\right)=\left\{\begin{array}{ll}
1 & \text { if } x_{i}=f_{x_{i}}\left(\mathrm{pa}\left(x_{i}\right), r_{x_{i}}\right) \\
0 & \text { otherwise }
\end{array}\right.
$$

For an incomplete model, if $X_{i}$ and $X_{j}$ are assumed to have an exogenous common cause, then the common constraint for these two variables will be given instead by

$$
\begin{aligned}
& P\left(x_{i}, x_{j} \mid \mathrm{pa}\left(x_{i}\right)-\left\{x_{j}\right\}, \mathrm{pa}\left(x_{j}\right)-\left\{x_{i}\right\}\right)= \\
& \quad \sum_{r_{x_{i}}, r_{x_{j}}} P\left(r_{x_{i}}, r_{x_{j}}\right) t\left(r_{x_{i}} ; x_{i}, \mathrm{pa}\left(x_{i}\right)\right) t\left(r_{x_{j}} ; x_{j}, \mathrm{pa}\left(x_{j}\right)\right)
\end{aligned}
$$

Note that the constraints in Eq. (4) are linear in $P\left(r_{x_{1}}, r_{x_{j}}\right)$.
For example, in the party story (which is complete with two binary variables $A$ and $B$ ) the constraints are given by

$$
\begin{aligned}
P\left(b_{1} \mid a_{0}\right) & =P\left(r_{b}=2\right)+P\left(r_{b}=3\right) \\
P\left(b_{1} \mid a_{1}\right) & =P\left(r_{b}=1\right)+P\left(r_{b}=3\right) \\
P\left(a_{1}\right) & =P\left(r_{a}=1\right)
\end{aligned}
$$

Additional subjective constraints may also be imposed on the underlying functional model. For example, we may subjectively believe that Bob is never spiteful against Ann, which can be simply written $P\left(r_{b}=2\right)=0$ and added to the existing set of constraints.
Given the entire set of linear constraints and the objective function from Eq. (2), the bounds may be evaluated using techniques for optimizing non-linear objective functions under linear constraints [Scales, 1985]. In general, the optimization procedure may converge to a local minima/maxima which would produce false bounds. If the objective is to prove that the counterfactual probability falls within a certain range, care must be taken to ensure that global optima are found.
If the objective function given by Eq. (2) is linear, the minimum/maximum may be determined using linear programming techniques. In this case, when the problem size is small enough, we may also derive symbolic bounds to the counterfactual probability in terms of the probabilistic specification. This is accomplished by tracking the conditions that lead to the various decisions in the Simplex Tableau algorithm. This procedure generates a decision tree where each leaf node contains a symbolic solution [Balke and Pearl, 1993].

## 4 APPLICATION TO CLINICAL TRIALS WITH IMPERFECT COMPLIANCE

Consider an experimental study where random assignment has taken place but compliance is not perfect (i.e., the treatment received differs from that assigned). It is well known that under such conditions a bias may be introduced, in the sense that the true causal effect of the treatment may deviate substantially from the causal effect computed by simply comparing subjects receiving the treatment with those not receiving the treatment. Because the subjects who did not comply with the assignment may be precisely those who would have responded adversely (positively) to the treatment, the actual effect of the treatment, when applied uniformly to the population, might be substantially less (more) effective than the study reveals.
In an attempt to avert this bias, economists have devised correctional formulas based on an "instrumental variables" model ([Bowden and Turkington, 1984]) which, in general, do not hold outside the linear regression model. A recent analysis by [Efron and Feldman, 1991] departs from the linear
regression model, but still makes restrictive commitments to a particular mode of interaction between compliance and response. [Robins, 1989] and [Manski, 1990] derived nonparametric bounds on treatment effects using different techniques; however their bounds are not tight. [Holland, 1988] has given a general formulation of the problem (which he called "encouragement design") in terms of Rubin's model of causal effect and has outlined its relation to path analysis and structural equations models. [Angrist et al., 1993], also invoking Rubin's model, have identified a set of assumptions under which the "Instrumental Variable" formula is valid for certain subpopulations. These subpopulations cannot be identified from empirical observation alone, and the need remains to devise alternative, assumption-free formulas for assessing the effect of treatment over the population as a whole. In this section, we derive bounds on the average treatment effect that rely solely on observed quantities and are universal, that is, valid no matter what model actually governs the interactions between compliance and response.
The canonical partial-compliance setting can be graphically modeled as shown in Figure 2.
![img-1.jpeg](img-1.jpeg)

Figure 2: Graphical representation of causal dependencies in a randomized clinical trial with partial compliance.

We assume that $Z, D$, and $Y$ are observed binary variables where $Z$ represents the (randomized) treatment assignment, $D$ is the treatment actually received, and $Y$ is the observed response. $U$ represents all factors, both observed and unobserved, that may influence the outcome $Y$ and the treatment $D$. To facilitate the notation, we let $z, d$, and $y$ represent, respectively, the values taken by the variables $Z, D$, and $Y$, with the following interpretation: $z \in\left\{z_{0}, z_{1}\right\}, z_{1}$ asserts that treatment has been assigned ( $z_{0}$, its negation); $d \in\left\{d_{0}, d_{1}\right\}, d_{1}$ asserts that treatment has been administered ( $d_{0}$, its negation); and $y \in\left\{y_{0}, y_{1}\right\}, y_{1}$ asserts a positive observed response ( $y_{0}$, its negation). The domain of $U$ remains unspecified and may, in general, combine the spaces of several random variables, both discrete and continuous.
The graphical model reflects two assumptions of independence:

1. The treatment assignment does not influence Y directly, but only through the actual treatment D, that is,

$$
Z \Perp Y \mid\{D, U\}
$$

In practice, any direct effect $\mathcal{Z}$ might have on

$Y$ would be adjusted for through the use of a placebo.
2. $Z$ and $U$ are marginally independent, that is, $Z \| U$. This independence is partly ensured through the randomization of $Z$, which rules out a common cause for both $Z$ and $U$. The absence of a direct path from $Z$ to $U$ represents the assumption that a person's disposition to comply with or deviate from a given assignment is not in itself affected by the assignment; any such effect can be viewed as part of the disposition.

These assumptions impose on the joint distribution ${ }^{1}$ the decomposition

$$
P(y, d, z, u)=P(y \mid d, u) P(d \mid z, u) P(z) P(u)
$$

which, of course, cannot be observed directly because $U$ is a latent variable. However, the marginal distribution $P(y, d, z)$ and, in particular, the conditional distributions $P(y, d \mid z), z \in\left\{z_{0}, z_{1}\right\}$, are observed, and the challenge is to assess the causal effect of $D$ on $Y$ from these distributions. ${ }^{2}$

In addition to the independence assumption above, the causal model of Figure 2 reflects claims about the behavior of the population under external interventions. In particular, it reflects the assumption that $P(y \mid d, u)$ is a stable quantity: the probability that an individual with characteristics $U=u$ given treatment $D=d$ will respond with $Y=y$ remains the same, regardless of how the treatment was selected - be it by choice or by policy. Therefore, if we wish to predict the distribution of $Y$ under a condition where the treatment $D$ is applied uniformly to the population, we should calculate

$$
P\left(y^{*} \mid \hat{d}^{*}\right)=\sum_{u} P(y \mid d, u) P(u)
$$

Likewise, if we are interested in estimating the average change in $Y$ due to treatment, we define the average causal effect, $\operatorname{ACE}(D \rightarrow Y)([\text { Holland, 1988 }])$, as

$$
\operatorname{ACE}(D \rightarrow Y)=P\left(y_{1}^{*} \mid \hat{d}_{1}^{*}\right)-P\left(y_{1}^{*} \mid \hat{d}_{0}^{*}\right)
$$

The task of causal inference is then to estimate or bound the expression in Eq. (8), given the observed probabilities $P\left(y, d \mid z_{0}\right)$ and $P\left(y, d \mid z_{1}\right)$. This may be accomplished by following the procedure detailed in Section 3.3 where the objective function to be optimized is the difference between the two counterfactual probabilities on the right-hand side of Eq. (8).
First, the functional model corresponding to the probabilistic model of Figure 2 must be specified. For each of the observable variables in the model ( $Z, D$,

[^0]and $Y$ ), we define the corresponding response-function variables ( $r_{x}, r_{d}$, and $r_{y}$, respectively).
Figure 3 shows the graphical representation of the resulting functional model. Because $D$ and $Y$ are assumed to be influenced by an unobservable common cause, the response-function variables $r_{d}$ and $r_{y}$ are connected by an edge.
The states of the variables $r_{d}$ and $r_{y}$ have the following interpretations:
![img-2.jpeg](img-2.jpeg)

Figure 3: A structure equivalent to that of Figure 1 but employing response-function variables $r_{x}, r_{d}$ and $r_{y}$.
$D$ is a deterministic function of the variable $Z$ and $r_{d} \in\{0,1,2,3\}$ :

$$
d=f_{d}\left(z, r_{d}\right)=h_{d, r_{d}}(z)
$$

where

$$
\begin{aligned}
& h_{d, 0}(z)=d_{0} \quad, \quad h_{d, 1}(z)= \begin{cases}d_{0} & \text { if } z=z_{0} \\
d_{1} & \text { if } z=z_{1}\end{cases} \\
& h_{d, 2}(z)=d_{1} \quad, \quad h_{d, 2}(z)= \begin{cases}d_{1} & \text { if } z=z_{0} \\
d_{0} & \text { if } z=z_{1}\end{cases}
\end{aligned}
$$

Similarly, $Y$ is a deterministic function of $D$ and $r_{y} \in$ $\{0,1,2,3\}$ :

$$
y=f_{y}\left(d, r_{y}\right)=h_{y, r_{y}}(d)
$$

where

$$
\begin{aligned}
& h_{y, 0}(d)=y_{0} \quad, \quad h_{y, 1}(d)= \begin{cases}y_{0} & \text { if } d=d_{0} \\
y_{1} & \text { if } d=d_{1}\end{cases} \\
& h_{y, 3}(d)=y_{1} \quad, \quad h_{y, 2}(d)= \begin{cases}y_{1} & \text { if } d=d_{0} \\
y_{0} & \text { if } d=d_{1}\end{cases}
\end{aligned}
$$

The correspondence between the states of variables $r_{d}$ and $r_{y}$ and the potential response vectors in the Rubin's model [Rosenbaum and Rubin, 1983] is rather transparent: each state corresponds to a counterfactual statement specifying how a unit in the population (e.g., a person) would have reacted to any given input. For example, $r_{d}=1$ represents units with perfect compliance, while $r_{d}=2$ represents units with perfect defiance. Similarly, $r_{y}=1$ represents units with perfect response to treatment, while $r_{y}=0$ represents units with no response ( $y=y_{0}$ ) regardless of treatment. The counterfactual variables $Y_{1}$ and $Y_{0}$ usually invoked in Rubin's model can be obtained from $r_{y}$ as follows:

$$
Y_{1}=\left\{Y \text { if } D=d_{1}\right\}= \begin{cases}1 & \text { if } r_{y}=1 \text { or } r_{y}=3 \\ 0 & \text { otherwise }\end{cases}
$$


[^0]:    ${ }^{1}$ We take the liberty of denoting the prior distribution of $U$ by $P(u)$, even though $U$ may consist of continuous variables.
    ${ }^{2}$ In practice, of course, only a finite sample of $P(y, d \mid z)$ will be observed, but since our task is one of identification, not estimation, we make the large-sample assumption and consider $P(y, d \mid z)$ as given.

$Y_{0}=\left\{Y\right.$ if $\left.D=d_{0}\right\}= \begin{cases}1 & \text { if } r_{y}=2 \text { or } r_{y}=3 \\ 0 & \text { otherwise }\end{cases}$
In general, treatment response and compliance attitudes may not be independent, hence the arrow $r_{d} \rightarrow$ $r_{y}$ in Figure 3. The joint distribution over $r_{d} \times r_{y}$ requires 15 independent parameters, and these parameters are sufficient for specifying the model of Figure 3, $P\left(y, d, z, r_{d}, r_{y}\right)=P\left(y \mid d, r_{y}\right) P\left(d \mid r_{d}, z\right) P(z) P\left(r_{d}, r_{y}\right)$, because $Y$ and $D$ stand in functional relation to their parents in the graph. The causal effect of the treatment can now be obtained directly from Eqs. (7) and (9) according to Eq. (2), giving

$$
\begin{aligned}
& P\left(y_{1}^{*} \mid \dot{d}_{1}^{*}\right)=P\left(r_{y}=1\right)+P\left(r_{y}=3\right) \\
& P\left(y_{1}^{*} \mid \dot{d}_{0}^{*}\right)=P\left(r_{y}=2\right)+P\left(r_{y}=3\right)
\end{aligned}
$$

and

$$
\operatorname{ACE}(D \rightarrow Y)=P\left(r_{y}=1\right)-P\left(r_{y}=2\right)
$$

### 4.1 LINEAR PROGRAMMING FORMULATION

In this section we will explicate the relationship between the parameters of the observed distribution $P(y, d \mid z)$ and the parameters of the joint distribution $P\left(r_{d}, r_{y}\right)$ of the response functions. This will lead directly to the linear constraints needed for minimizing/maximizing $\operatorname{ACE}(D \rightarrow Y)$ given the observation $P(y, d \mid z)$.
The conditional distribution $P(y, d \mid z)$ over the observable variables is fully specified by eight parameters, which will be notated as follows:

$$
\begin{array}{ll}
p_{00.0}=P\left(y_{0}, d_{0} \mid z_{0}\right) & p_{00.1}=P\left(y_{0}, d_{0} \mid z_{1}\right) \\
p_{01.0}=P\left(y_{0}, d_{1} \mid z_{0}\right) & p_{01.1}=P\left(y_{0}, d_{1} \mid z_{1}\right) \\
p_{10.0}=P\left(y_{1}, d_{0} \mid z_{0}\right) & p_{10.1}=P\left(y_{1}, d_{0} \mid z_{1}\right) \\
p_{11.0}=P\left(y_{1}, d_{1} \mid z_{0}\right) & p_{11.1}=P\left(y_{1}, d_{1} \mid z_{1}\right)
\end{array}
$$

The probabilistic constraints

$$
\sum_{n=00}^{11} p_{n .0}=1 \quad \sum_{n=00}^{11} p_{n .1}=1
$$

further imply that $\vec{p}=\left(p_{00.0}, \ldots, p_{11.1}\right)$ can be specified by a point in six-dimensional space. This space will be referred to as $P$.
The joint probability over $r_{d} \times r_{y}, P\left(r_{d}, r_{y}\right)$, has 16 parameters and completely specifies the population under study. These parameters will be notated as

$$
q_{j k}=P\left(r_{d}=j, r_{y}=k\right)
$$

where $j, k \in\{0,1,2,3\}$. The probabilistic constraint

$$
\sum_{j=0}^{3} \sum_{k=0}^{3} q_{j k}=1
$$

implies that $\vec{q}$ specifies a point in 15 -dimensional space. This space will be referred to as $Q$.

Eq. (12) can now be rewritten as a linear combination of the $Q$ parameters:

$$
\begin{aligned}
& \operatorname{ACE}(D \rightarrow Y)= \\
& \quad q_{01}+q_{11}+q_{21}+q_{31}-q_{02}-q_{12}-q_{22}-q_{32}
\end{aligned}
$$

Applying Eqs. (3) and (4) we can write the constraints which reflect the direct linear transformation from a point $\vec{q}$ in $Q$ space to the corresponding point $\vec{p}$ in the observation space $P$ :

$$
\begin{aligned}
& p_{00.0}=q_{00}+q_{01}+q_{10}+q_{11} \\
& p_{01.0}=q_{20}+q_{22}+q_{30}+q_{32} \\
& p_{10.0}=q_{02}+q_{03}+q_{12}+q_{13} \\
& p_{11.0}=q_{21}+q_{23}+q_{31}+q_{33} \\
& p_{00.1}=q_{00}+q_{01}+q_{20}+q_{31} \\
& p_{01.1}=q_{10}+q_{12}+q_{30}+q_{32} \\
& p_{10.1}=q_{02}+q_{03}+q_{22}+q_{33} \\
& p_{11.1}=q_{11}+q_{13}+q_{31}+q_{33}
\end{aligned}
$$

which will be written in matrix form, $\vec{p}=\vec{P} \vec{q}$.
Given a point $\vec{p}$ in $P$ space, the strict lower bound on $\operatorname{ACE}(D \rightarrow Y)$ can be determined by solving the following linear programming problem:
Minimize: $q_{01}+q_{11}+q_{21}+q_{31}-q_{02}-q_{12}-q_{22}-q_{32}$ Subject to:

$$
\begin{aligned}
\sum_{j=0}^{3} \sum_{k=0}^{3} q_{j k} & =1 \\
\tilde{P} \vec{q} & =\vec{p} \\
q_{j k} & \geq 0 \text { for } j, k \in\{0,1,2,3\}
\end{aligned}
$$

However, for problems of this size, the procedure may be used for deriving symbolic expressions as well, leading to the following lower bound on the treatment effect

$$
\begin{aligned}
& \operatorname{ACE}(D \rightarrow Y) \geq \\
& \max \left\{\begin{array}{c}
p_{11.1}+p_{00.0}-1 \\
p_{11.0}+p_{00.1}-1 \\
p_{11.0}-p_{11.1}-p_{10.1}-p_{01.0}-p_{10.0} \\
p_{11.1}-p_{11.0}-p_{10.0}-p_{01.1}-p_{10.1} \\
-p_{01.1}-p_{10.1} \\
-p_{01.0}-p_{10.0} \\
p_{00.1}-p_{01.1}-p_{10.1}-p_{01.0}-p_{00.0} \\
p_{00.0}-p_{01.0}-p_{10.0}-p_{01.1}-p_{00.1}
\end{array}\right\}
\end{aligned}
$$

Similarly, the upper bound is given by

$$
\begin{aligned}
& \operatorname{ACE}(D \rightarrow Y) \leq \\
& \min \left\{\begin{array}{c}
1-p_{01.1}-p_{10.0} \\
1-p_{01.0}-p_{10.1} \\
-p_{01.0}+p_{01.1}+p_{00.1}+p_{11.0}+p_{00.0} \\
-p_{01.1}+p_{11.1}+p_{00.1}+p_{01.0}+p_{00.0} \\
p_{11.1}+p_{00.1} \\
p_{11.0}+p_{00.0} \\
-p_{10.1}+p_{11.1}+p_{00.1}+p_{11.0}+p_{10.0} \\
-p_{10.0}+p_{11.0}+p_{00.0}+p_{11.1}+p_{10.1}
\end{array}\right\}
\end{aligned}
$$

We may also derive bounds on the treatment responses under the condition where treatment is uniformly applied to the population by optimizing Eqs. (10) and (11) individually (under the same linear constraints). The resulting bounds are:

$$
\begin{aligned}
& \max \left\{\begin{array}{c}
p_{10.0}+p_{11.0}-p_{00.1}-p_{11.1} \\
p_{10.1} \\
p_{10.0} \\
p_{01.0}+p_{10.0}-p_{00.1}-p_{01.1}
\end{array}\right\} \\
& \leq P\left(y_{1}^{*} \mid d_{0}^{*}\right) \leq \\
& \min \left\{\begin{array}{c}
p_{01.0}+p_{10.0}+p_{10.1}+p_{11.1} \\
1-p_{00.1} \\
1-p_{00.0} \\
p_{10.0}+p_{11.0}+p_{01.1}+p_{10.1}
\end{array}\right\}
\end{aligned}
$$

and

$$
\begin{aligned}
& \max \left\{\begin{array}{c}
p_{11.0} \\
p_{11.1} \\
-p_{00.0}-p_{01.0}+p_{00.1}+p_{11.1} \\
-p_{01.0}-p_{10.0}+p_{10.1}+p_{11.1}
\end{array}\right\} \\
& \leq P\left(y_{1}^{*} \mid d_{1}^{*}\right) \leq \\
& \min \left\{\begin{array}{c}
1-p_{01.1} \\
1-p_{01.0} \\
p_{00.0}+p_{11.0}+p_{10.1}+p_{11.1} \\
p_{10.0}+p_{11.0}+p_{00.1}+p_{11.1}
\end{array}\right\}
\end{aligned}
$$

These bounds improve upon the results of [Manski, 1990]. In addition, one can prove that these are the tightest possible assumption-free bounds.
Examples and additional results regarding bounds on treatment effects in partial compliance studies are presented in [Balke and Pearl, 1993].

## 5 APPLICATIONS TO LIABILITY JUDGMENT

Evaluation of counterfactual probabilities could be enlightening in some legal cases in which a plaintiff claims that a defendant's actions were responsible for the plaintiff's misfortune. Improper rulings can easily be issued without an adequate treatment of counterfactuals. Consider the following hypothetical and fictitious case study, especially crafted to accentuate the disparity between different methods of analysis.
The marketer of PeptAid (antacid medication) randomly mailed out product samples to $10 \%$ of the households in the city of Stress, California. In a followup study, researchers determined for each individual whether they received the PeptAid sample, whether they consumed PeptAid, and whether they developed peptic ulcers in the following month.
The causal structure which describes the influences in this scenario is identical to the partial-compliance model given by Figure 2, where $z_{1}$ asserts that PeptAid was received from the marketer; $d_{1}$ asserts that PeptAid was consumed; and $y_{1}$ asserts that peptic ulceration occurred. The data showed the following distribution:

$$
P\left(z_{1}\right)=0.1
$$

$$
\begin{array}{ll}
P\left(y_{0}, d_{0} \mid z_{0}\right)=0.32 & P\left(y_{0}, d_{0} \mid z_{1}\right)=0.02 \\
P\left(y_{0}, d_{1} \mid z_{0}\right)=0.32 & P\left(y_{0}, d_{1} \mid z_{1}\right)=0.17 \\
P\left(y_{1}, d_{0} \mid z_{0}\right)=0.04 & P\left(y_{1}, d_{0} \mid z_{1}\right)=0.67 \\
P\left(y_{1}, d_{1} \mid z_{0}\right)=0.32 & P\left(y_{1}, d_{1} \mid z_{1}\right)=0.14
\end{array}
$$

This data indicates a high-correlation between those individuals who consumed PeptAid and those who developed peptic ulcers in the following month

$$
P\left(y_{1} \mid d_{1}\right)=0.50 \quad P\left(y_{1} \mid d_{0}\right)=0.26
$$

In addition, the intent-to-treat analysis showed that those individuals who received the PeptAid samples had a $45 \%$ greater chance of developing peptic ulcers

$$
P\left(y_{1} \mid z_{1}\right)=0.81 \quad P\left(y_{1} \mid z_{0}\right)=0.36
$$

The plaintiff (Mr. Smith), having heard of the study, litigated against both the marketing firm and the PeptAid producer. The plaintiff's attorney argued against the producer, claiming that the consumption of PeptAid triggered his client's ulcer and resulting medical expenses. Likewise, the plaintiff's attorney argued against the marketer, claiming that his client would not have developed an ulcer, if the marketer had not distributed the product samples.
The defense attorney, representing both the manufacturer and marketer of PeptAid, though, rebutted this argument, stating that the high correlation between PeptAid consumption and ulcers was attributable to a common factor, namely, pre-ulcer discomfort. Individuals with gastrointestinal discomfort would be much more likely to both use PeptAid and develop stomach ulcers. To bolster his clients' claims, the defense attorney introduced expert analysis of the data showing that, on the average, consumption of PeptAid actually decreases an individual's chances of developing ulcers by at least $15 \%$.
Indeed, the application of Eqs. 16 and 17 results in the following bounds on the average causal effect of PeptAid consumption on peptic ulceration

$$
-0.23 \leq \operatorname{ACE}(D \rightarrow Y) \leq-0.15
$$

and proves that PeptAid is beneficial to the population as a whole.
The plaintiff's attorney, though, stressed the distinction between the average treatment effects for the entire population and the sub-population consisting of those individuals who, like his client, received the PeptAid sample, consumed it and then developed ulcers. Analysis of the population data indicated that had PeptAid not been distributed, Mr. Smith would have had at most a $7 \%$ chance of developing ulcers regardless of any confounding factors such as pre-ulcer pain. Likewise, if Mr. Smith had not consumed PeptAid, he would have had at most a $7 \%$ chance of developing ulcers.
The damaging statistics against the marketer are obtained by evaluating the bounds on the probability that the plaintiff would have developed a peptic ulcer

if he had not received the PeptAid sample, given that he in fact received the sample PeptAid, consumed the PeptAid, and developed peptic ulcers. This probability may be written in terms of the functional model parameters:

$$
P\left(y_{1}^{*} \mid \hat{z}_{0}^{*}, y_{1}, d_{1}, z_{1}\right)=\frac{P\left(r_{z}=1\right)\left[q_{13}+q_{31}+q_{33}\right]}{P\left(y_{1}, d_{1}, z_{1}\right)}
$$

But, since $Z$ is a root node in the probabilistic specification, $P\left(r_{z}=1\right)=P\left(z_{1}\right)$; therefore,

$$
\begin{aligned}
P\left(y_{1}^{*} \mid \hat{z}_{0}^{*}, y_{1}, d_{1}, z_{1}\right) & =\frac{q_{13}+q_{31}+q_{33}}{P\left(y_{1}, d_{1} \mid z_{1}\right)} \\
& =\frac{q_{13}+q_{31}+q_{33}}{p_{11.1}}
\end{aligned}
$$

This expression is linear with respect to the $Q$ parameters; therefore, we may use linear optimization to derive symbolic bounds on the counterfactual probability with respect to the probabilistic specification $P(y, d \mid z)$ :

$$
\begin{aligned}
& \frac{1}{p_{11.1}} \max \left\{\begin{array}{c}
0 \\
p_{11.1}-p_{00.0} \\
p_{11.0}-p_{00.1}-p_{10.1} \\
p_{10.0}-p_{01.1}-p_{10.1}
\end{array}\right\} \\
& \leq P\left(y_{1}^{*} \mid \hat{z}_{0}^{*}, z_{1}, d_{1}, y_{1}\right) \leq \\
& \frac{1}{p_{11.1}} \min \left\{\begin{array}{c}
p_{11.1} \\
p_{10.0}+p_{11.0} \\
1-p_{00.0}-p_{10.1}
\end{array}\right\}
\end{aligned}
$$

Similarly, the damaging evidence against PeptAid's producer is obtained by evaluating the bounds on the counterfactual probability $P\left(y_{1}^{*} \mid \hat{d}_{0}^{*}, y_{1}, d_{1}, z_{1}\right)$. In terms of the $Q$ parameters the counterfactual probability is written:

$$
\begin{aligned}
P\left(y_{1}^{*} \mid \hat{d}_{0}^{*}, y_{1}, d_{1}, z_{1}\right) & =\frac{q_{13}+q_{33}}{q_{11}+q_{13}+q_{31}+q_{33}} \\
& =\frac{q_{13}+q_{33}}{p_{11.1}}
\end{aligned}
$$

If we minimize/maximize the numerator given the linear constraints, we arrive at the following bounds:

$$
\begin{aligned}
& \frac{1}{p_{11.1}} \max \left\{\begin{array}{c}
0 \\
p_{11.1}-p_{00.0}-p_{11.0} \\
p_{10.0}-p_{01.1}-p_{10.1}
\end{array}\right\} \\
& \leq P\left(y_{1}^{*} \mid \hat{d}_{0}^{*}, z_{1}, d_{1}, y_{1}\right) \leq \\
& \frac{1}{p_{11.1}} \min \left\{\begin{array}{c}
p_{11.1} \\
p_{10.0}+p_{11.0} \\
1-p_{00.0}-p_{10.1}
\end{array}\right\}
\end{aligned}
$$

Substituting the observed distribution $P(y, d \mid z)$ into these formulas, the following bounds were obtained

$$
\begin{aligned}
& 0.00 \leq P\left(y_{1}^{*} \mid \hat{z}_{0}^{*}, z_{1}, d_{1}, y_{1}\right) \leq 0.07 \\
& 0.00 \leq P\left(y_{1}^{*} \mid \hat{d}_{0}^{*}, z_{1}, d_{1}, y_{1}\right) \leq 0.07
\end{aligned}
$$

We can write the average causal effects for the subpopulation resembling the plaintiff by conditioning the
counterfactual probabilities in Eqs. (10) and (11) on the features of the plaintiff.

$$
\begin{aligned}
& \operatorname{ACE}\left(D \rightarrow Y \mid z_{1}, d_{1}, y_{1}\right)= \\
& \quad P\left(y_{1}^{*} \mid \hat{d}_{1}^{*}, z_{1}, d_{1}, y_{1}\right)-P\left(y_{1}^{*} \mid \hat{d}_{0}^{*}, z_{1}, d_{1}, y_{1}\right)
\end{aligned}
$$

Counterfactual probabilities have the property that if the counterfactual antecedent is implied by the realworld observation, then the probability of the counterfactual consequent is the same as in the real-world given the observations:

$$
P\left(c^{*} \mid \hat{a}^{*}, v\right)=P\left(c=c^{*} \mid 0\right)
$$

Therefore,

$$
\begin{aligned}
& P\left(y_{1}^{*} \mid \hat{z}_{1}^{*}, z_{1}, d_{1}, y_{1}\right)=1.00 \\
& P\left(y_{1}^{*} \mid \hat{d}_{1}^{*}, z_{1}, d_{1}, y_{1}\right)=1.00
\end{aligned}
$$

and

$$
\begin{aligned}
& 0.93 \leq \operatorname{ACE}\left(D \rightarrow Y \mid z_{1}, d_{1}, y_{1}\right) \leq 1.00 \\
& 0.93 \leq \operatorname{ACE}\left(Z \rightarrow Y \mid z_{1}, d_{1}, y_{1}\right) \leq 1.00
\end{aligned}
$$

At least $93 \%$ of the people in the plaintiff's subpopulation would not have developed ulcers had they not been encouraged to take PeptAid ( $z_{0}$ ), or similarly, had they not taken PeptAid ( $d_{0}$ ). This lends very strong support for the plaintiff's claim that he was adversely affected by the marketer and producer's actions and product.
The judge ruled in favor of the plaintiff. PeptAid withdrew the product from the market, and initiated a research effort to identify observable characteristics of those individuals who are adversely effected by PeptAid.

## 6 CONCLUSION

This paper has developed a procedure for evaluating bounds on counterfactual probabilities. At first thought, one may believe that assumption-free bounds would be very weak bounds, but this paper has demonstrated that in certain circumstances, the results of such analysis could provide compelling evidence for legal decisions and development of treatment policies.
The corner-stone of counterfactual analysis is the use of functional models with response-function variables, for which the counterfactual probability may be uniquely written. The task of determining bounds involves the optimization of this expression under the constraints imposed by the known probabilistic specification. In general, the task is reduced to the optimization of a polynomial function subject to linear constraints, which introduces the problem of local minima/maxima.
If the counterfactual probability is linear with respect to the functional specification, then the bounds are easily found via linear programming. In addition, in some cases we may be able to derive symbolic bounds on counterfactual probabilities in terms of the probabilistic specification. Such bounds were derived in

applications involving: (1) the determination of treatment efficacy from studies where subjects do not comply perfectly with treatment assignment, and (2) the determination of liability in product-safety litigation.

## Acknowledgements

The research was partially supported by Air Force grant \#AFOSR 90 0136, NSF grant \#IRI-9200918, Northrop Micro grant \#92-123, and Rockwell Micro grant \#92-122. Alexander Balke was supported by the Fannie and John Hertz Foundation.
