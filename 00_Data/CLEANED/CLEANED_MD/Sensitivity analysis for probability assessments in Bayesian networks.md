# Sensitivity Analysis for Probability Assessments in Bayesian Networks 

Kathryn Blackmond Laskey<br>Department of Systems Engineering and C ${ }^{3}$ I Center<br>George Mason University<br>Fairfax, VA 22030<br>klaskey@gmu.edu


#### Abstract

When eliciting probability models from experts, knowledge engineers may compare the results of the model with expert judgment on test scenarios, then adjust model parameters to bring the behavior of the model more in line with the expert's intuition. This paper presents a methodology for analytic computation of sensitivity values to measure the impact of small changes in a network parameter on a target probability value or distribution. These values can be used to guide knowledge elicitation. They can also be used in a gradient descent algorithm to estimate parameter values that maximize a measure of goodness-of-fit to both local and holistic probability assessments.


## 1 INTRODUCTION

The Bayesian network is becoming a standard representation for uncertainty in symbolic reasoning systems. In a Bayesian network, a probability distribution over a set of random variables is represented by a set of local conditional probability distributions. Local representation has well-known advantages for maintainability of the knowledge base, computation of probabilities, and knowledge elicitation.
To specify a Bayesian network, one first decomposes the hypotheses of interest and related hypotheses into a set of random variables, each representing a set of mutually exclusive and exhaustive hypotheses. Next, one defines a directed acyclic graph which encodes conditional dependencies among the variables. (At this point, auxiliary variables are often added to simplify the conditional dependency structure.) Finally, one specifies the local conditional distributions. At each node, one must define a set of conditional distributions for the node's random variable, one for each combination of values of the direct parents of the node.
The network topology and conditional distributions can be learned from data (e.g., Cooper and Herskovits, 1991; Spiegelhalter and Lauritzen, 1990; Buntine, 1991) or, more commonly in expert systems applications, specified by experts. Although local assessments are sufficient to specify the full joint distribution, these assessments may
have non-intuitive consequences for propositions for which beliefs were not assessed directly. Commonly, a Bayesian network model is used to answer queries about the conditional distribution of a target variable given specific values for a subset of variables called evidence variables. (Sometimes the variables designated as target and evidence variables are fixed in advance; at other times they vary from query to query.) It is rarely the case that the first attempt at assessing network structure and local conditional distributions leaves the expert satisfied with the system's responses to test queries. Knowledge elicitation thus involves an iterative process of specifying a Bayesian network, processing a representative set of queries, and adjusting structure and parameters until the expert is satisfied with the system's response to the test queries.
Key to this iterative process is sensitivity analysis, or examination of the impact of changes in base assumptions on model results. One common approach to sensitivity analysis is to define reasonable ranges for each of the model parameters, vary each parameter from its lowest to highest reasonable value while holding the other variables fixed, and examine the resultant changes in the target value. Another approach, the one taken here, is to compute the partial derivative of the target value with respect to each of the model parameters. A disadvantage of the partial derivative approach is that it provides information only about changes in a small neighborhood about the assessed value. It has the advantage that the expert need not assess upper and lower reasonable values for each parameter. Another advantage for the Bayesian network application is that standard belief network propagation algorithms are easily modified to compute sensitivity values. I show below that the partial derivative method requires far fewer iterations through the belief propagation algorithm than does the direct variation method. Partial derivatives and direct variation can be used in conjunction. Partial derivatives may be used to identify variables with potentially high impact. Reasonable ranges may then be assessed for these variables and sensitivity values may be computed by direct variation.

This paper presents a method for computing sensitivity values. I begin with a single scenario, in which the probability distribution is considered for a target variable given values for a set of evidence variables. These sensitivities may be used to provide feedback to guide the expert in deciding which local probability assessments to consider changing when a global probability estimate is unsatisfactory. Sensitivity values can also be used to suggest possible structural changes to the network. The methodology can also be used to aggregate assessments for multiple scenarios into a best-fit model.

## 2 COMPUTING SENSITIVITY VALUES

### 2.1 Definitions and Notation

Consider a Bayesian network model for $\mathbf{X}$, a random vector with $n$ components. ${ }^{1}$ Let $\mathrm{X}_{i}$ denote the $i$ th component of $\mathbf{X}$, and let $\mathbf{X}_{c(i)}$ represent the set of conditioning variables, or direct parents, of $\mathrm{X}_{i}$. The probability distribution for $\mathbf{X}$ depends on a parameter vector $\theta$. The probability that $\mathbf{X}$ takes on a particular value $x$ is given by

$$
\mathrm{P}(x \mid \theta)=\prod_{i} \mathrm{P}\left(x_{i} \mid x_{c(i)}, \theta_{i}\right)
$$

The factors in (1) are the local conditional probabilities that $\mathrm{X}_{i}=x_{i}$ given the values $\mathbf{X}_{c(i)}=x_{c(i)}$ of the conditioning variables.
The local conditional distribution for $\mathrm{X}_{i}$ consists of a probability for each possible value of $\mathrm{X}_{i}$ given each combination of possible values of its parent variables $\mathbf{X}_{c(i)}$. A number of authors have discussed models for the local conditional distributions that depend on fewer parameters. The parameter vector $\theta_{i}$ has been introduced to permit the methodology to handle such models.
The local parameter vector $\theta_{i}$ determines the probability distribution of the $i$ th node given values of its parent nodes. That is, the parameter vector $\theta$ is partitioned as $\theta$ $=\left(\theta_{1}, \ldots \theta_{n}\right)$, where $\theta_{i}$ controls the distribution of $\mathrm{X}_{i}$ given its parents $\mathbf{X}_{c(i)}$. The components of $\theta_{i}$ are denoted by $\theta_{i}(s)$, where $k$ indexes the elements of the parameter vector.
Example 1 below considers the simplest model for the local conditional distributions, one with no restrictions on the local conditional probabilities except that the probabilities in each local conditional distribution sum to 1. Example 1 shows one way to parameterize this model.

Example 1: Unrestricted Local Conditional Distributions, The parameter vector $\theta_{i}$ consists of one component for each combination of values of $\mathrm{X}_{i}$ and its parents. Components of $\theta_{i}$ are denoted $\theta_{i\left[s_{i}, x_{c(i)}\right]}$ and are restricted to be

[^0]nonnegative. The conditional probability distributions are related to the parameters as follows.

$$
\mathrm{P}\left(x_{i} \mid x_{c(i)}, \theta_{i}\right)=\frac{\theta_{i\left(x_{i}, x_{c(i)}\right]}}{\sum_{x_{i}^{\prime} i} \theta_{i\left[x_{i}^{\prime}, x_{c(i)}\right]}}
$$

(For the initial assessed model it is convenient to scale the $\theta$ 's so that the sum in the denominator is equal to 1 . However, it is necessary to write the local distribution as (2) in order to enforce the sum-to-one constraint when a single $\theta_{i[k]}$ is changed).
The noisy-OR model (Pearl, 1988) is a commonly cited example of a model for local conditional distributions that depends on fewer parameters than the total number of local conditional probabilities. A noisy-OR model applies when $\mathrm{X}_{i}$ and its predecessors are all binary variables and each predecessor can be thought of as an independent cause of $\mathrm{X}_{i}$. The model can be determined by assessing from the expert a "base" probability for $\mathrm{X}_{i}$ and a single probability for each immediate predecessor of $\mathrm{X}_{i}$. The base probability is the probability that $\mathrm{X}_{i}$ is true when none of its immediate predecessors is true. The model can be estimated by assessing for predecessor $\mathrm{X}_{j}$ the probability that $\mathrm{X}_{i}$ is true when $\mathrm{X}_{j}$ is true and all other predecessors are false. From these values and the assumptions of the noisy-OR model it one can estimate the full set of local conditional distributions for $\mathrm{X}_{i}$. Example 2 shows how the noisy-OR model can be parameterized.

Example 2: Noisy-OR model. The variable $\mathrm{X}_{i}$ and its parents $\mathrm{X}_{j}(j \in c(i))$ are binary, taking on values $t_{i}\left(t_{j}\right)$ and $f_{i}\left(f_{j}\right)$. The parameter vector $\theta_{i}$ consists of one element for each parent variable. An element of $\theta_{i}$ is denoted by $\theta_{i(j)}$, where the subscript $j$ ranges over the indices $c(j)$ of the conditioning variables. The value $\theta_{i(j)}$ represents the probability that the "inhibitor" corresponding to variable $x_{j}$ is active (see Pearl, 1989). The variable $\mathrm{X}_{i}$ takes on the value $t_{i}$ if at least one inhibitor for a parent variable in state $t_{j}$ is inactive. One may also add a "dummy inhibitor" $\theta_{i[0]}$ which represents a "base probability" that $\mathrm{X}_{i}=t_{i}$ when none of its parents in is the true state.

$$
\begin{aligned}
& \mathrm{P}\left(t_{i} \mid x_{c(i)}, \theta_{i}\right)=1-\theta_{i[0]} \prod_{x_{j}=t_{j}} \theta_{i[j]} \\
& \mathrm{P}\left(f_{i} \mid x_{c(i)}, \theta_{i}\right)=\theta_{i[0]} \prod_{x_{j}=t_{j}} \theta_{i[j]}
\end{aligned}
$$

Other lower dimensional representations of the local conditional distributions are have been discussed in the literature. For example, Srinivas (1992) discusses generalizing the noisy-OR to non-binary variables.


[^0]:    ${ }^{1}$ I use uppercase letters to represent random variables and lowercase letters to represent specific values for the random variables. Boldface letters represent vectors and standard letters represent scalars.

Asymmetric independencies (e.g., Heckerman, 1990)) can be represented as equality constraints on some of the local conditional probabilities.
In what follows, I assume that an initial value of the parameter vector $\theta$ has been specified. This initial specification commonly comes from expert judgment. (Note that the expert need not specify $\theta$ values directly; these values can be inferred from probability judgments with which the expert feels comfortable.) The goal of the methodology presented here is to provide guidance to an expert or analyst who wishes to consider the impact of varying the parameter vector. I assume that $\theta$ can be varied in an open ball around the value $\theta$. This means that $\theta$ does not lie on the boundary of the parameter space and that the $\theta_{i[k]}$ can all be varied independently of each other.

### 2.2 Single Target Probability, Single Scenario

A scenario for sensitivity assessment is defined by a target variable $\mathrm{X}_{t}$ and an assigned set of values $x_{e}$ for a subset $\mathrm{X}_{e}$ of variables called evidence variables. The goal of sensiavity analysis is to analyze the impact of changes in the parameter vector $\theta$ on the probability distribution $\mathrm{P}\left(\mathrm{X}_{t} \mid x_{e}, \theta\right)$. In this section I show how to assess the impach of small changes in a single element $\theta_{s[4]}$ on $\mathrm{P}\left(\mathrm{X}_{t} \mid x_{e}, \theta\right)$. The selected element $\theta_{s[4]}$ is the $k$ th element of the parameter vector for the local conditioal distribution for the selected variable $\mathrm{X}_{s}$. Proposition 1 shows how to compute the sensitivity of the probability $\mathrm{P}\left(x_{i} \mid x_{e}, \theta_{s}\right)$ to changes in the parameter $\theta_{s[k]}$.

Proposition 1. The partial derivative of the probability value $\mathrm{P}\left(x_{i} \mid x_{e}, \theta\right)$ with respect to the parameter value $\theta_{s k}$ is given by

$$
\begin{aligned}
& \frac{\partial \mathrm{P}\left(x_{i} \mid x_{e}, \theta\right)}{\partial \theta_{s[k]}}= \\
& \quad \mathrm{P}\left(x_{i} \mid x_{e}, \theta\right)\left(\mathrm{E}\left[\mathrm{U}_{s[k]} \mid x_{i}, x_{e}\right]-\mathrm{E}\left[\mathrm{U}_{s[k]} \mid x_{e}\right]\right)
\end{aligned}
$$

where

$$
\mathrm{U}_{s[k]}\left(\mathrm{X}_{s}, \mathrm{X}_{c(s)}, \theta_{s}\right)=\frac{\partial}{\partial \theta_{s[k]}} \log \mathrm{P}\left(\mathrm{X}_{s} \mid \mathrm{X}_{c(s)}, \theta_{s}\right)
$$

The proof of Proposition 1 is given in the appendix.
The next two propositions apply this result to the two examples described in Section 2.1. To find sensitivity values for the unrestricted models, one needs to compute the function $U$ when the local conditional distribution is defined by (2). This is found by differentiating (2) with respect to $\theta_{i\left(x_{i}, x_{e(i)}\right]}$ and using the chain rule to compute the derivative of the logarithm.

Proposition 2. The values of $U$ for the unrestricted node distribution model of Example 1 are given by

$$
\begin{aligned}
& \mathrm{U}_{i\left(x_{i}, x_{e(i)}\right]}\left(x_{i}, x_{c(i)}, \theta_{i}\right)= \\
& \quad \frac{1}{\sum_{x_{i}^{\prime}} \theta_{i\left(x_{i}^{\prime}, x_{e(i)}\right]}}\left(\frac{1-\mathrm{P}\left(x_{i} \mid x_{c(i)}, \theta_{i}\right)}{\mathrm{P}\left(x_{i} \mid x_{c(i)}, \theta_{i}\right)}\right) \\
& \mathrm{U}_{i\left(x_{i}, x_{e(i)}\right]}\left(x_{i}^{*}, x_{c(i)}, \theta_{i}\right)=-\frac{1}{\sum_{x_{i}^{\prime}} \theta_{i\left(x_{i}^{\prime}, x_{e(i)}\right]}} \\
& \mathrm{U}_{i\left(x_{i}, x_{e(i)}\right]}\left(x_{i}^{*}, x_{c(i)}^{*}, \theta_{i}\right)=0
\end{aligned}
$$

From Proposition 2 it is clear that increasing $\theta_{i\left(x_{i}, x_{e(i)}\right.}$ increases the probability of $x_{i}$ given $x_{c(i)}$ (this is hardly surprising). Icreasing $\theta_{i\left(x_{i}, x_{e(i)}\right]}$ also decreases the probability of other values of $X_{t}$ because of the sum-to-1 constraint. The distributions of $\mathrm{X}_{t}$ given other combinations of values of the parent variables are unaffected by changes in $\theta_{i\left(x_{i}, x_{e(i)}\right]}$.

Proposition 3: The values of $U$ for the NoisyOR model of Example 2 are given by

$$
\begin{aligned}
& \mathrm{U}_{i[j]}\left(t_{i}, x_{c(i)}, \theta_{i}\right)= \\
& \begin{cases}-\theta_{i[0]} \prod_{x_{j}=t_{j}} \theta_{i[j]} & x_{j}=t_{j} \\
j \neq j & \\
0 & x_{j}=f_{j} \\
-\prod_{x_{j}=t_{j}} \theta_{i[j]} & j=0\end{cases} \\
& \mathrm{U}_{i[j]}\left(f_{i}, x_{c(i)}, \theta_{i}\right)= \\
& \left\{\begin{array} { l } 
{ \theta _ { i } _ { 1 0 } } \\
{ \sum _ { j } = t _ { j } } \\
{ \theta _ { i } _ { i } _ { j } }
\end{array} \left\{\begin{array}{rl}
\mathrm{e}_{i}[j] & x_{j}=t_{j} \\
0 & x_{j}=f_{j} \\
\prod_{x_{j}=t_{j}}
\end{array}\right.\right.
\end{aligned}
$$

$$
\begin{aligned}
& x_{j}=t_{j}
\end{aligned}
$$

Proposition 3 says that changes in the inhibitor probability $\theta_{i[j]}$ change the probability distribution of $\mathrm{X}_{t}$ only when the corresponding parent variable $\mathrm{X}_{j}$ is true. Increases in the inhibitor probability have impact of equal magnitude but opposite sign on the probability of $t_{i}$ and the probability of $f_{i}$ conditional on any given combination of values of the parent variables.

### 2.3 Computing Sensitivity Values

The expectations in (4) can be computed by straightforward modification of standard belief network propagation algorithms. I describe how to compute these expectations using the Lauritzen and Spiegelhalter algorithm and variants of logic sampling. Similar

modifications are possible with other belief propagation algorithms.
In some cases, the structure of the graph implies that (4) is equal to zero. To determine when (4) is equal to zero, one constructs and auxiliary graph by adding a new parent node $\Theta_{i}$ to each node $\mathrm{X}_{i}$. This new parent represents the possible values of the parameter vector $\theta_{i}$. Now, (4) is equal to zero when $\mathrm{X}_{e} d$-separates $\Theta_{s}$ from $\Theta_{t}$. In addition, as evidenced by Equations (2) and (3), specific local models imply additional conditions under which the sensitivities of $\theta_{t[k]}$ are zero.
The Lauritzen and Spiegelhalter algorithm and its variants transform the network into a tree of cliques, where each clique consists of a subset of variables in the network and the cliques satisfy the running intersection property (Neapolitan, 1990). The set consisting of a node $\mathrm{X}_{i}$ and its parents $\mathbf{X}_{c(j)}$ must belong to at least one clique. The belief propagation algorithm computes and stores with each clique a potential for each combination of values of each node in the clique. The clique potential function is proportional to the joint conditional probability distribution over the nodes in the clique given the values of the evidence nodes.
To compute sensitivity values for $\mathrm{X}_{t}=x_{t}$, first declare as evidence $\mathrm{X}_{t}=x_{t}$ and $\mathbf{X}_{e}=x_{e}$ and run the belief propagation algorithm. As noted above, for each $s$, one of the cliques must contain $\mathrm{X}_{s}$ and all its parents $\mathbf{X}_{c(s)}$. Marginalizing the clique potential over all nodes in this clique other than $\left(\mathrm{X}_{s}, \mathbf{X}_{c(s)}\right)$ yields a function which can be normalized to obtain the conditional probability distribution $\mathrm{P}\left(\mathrm{X}_{s}, \mathrm{X}_{c(s)} \mid x_{t}, x_{e}, \theta\right)$. Now, use this joint distribution to compute the second expectation in (4):

$$
\begin{aligned}
& \mathrm{E}\left[\mathrm{U}_{s[k]} \mid x_{t}, x_{e}\right]= \\
& \quad \sum_{\left(x_{s}, x_{s(t)}\right)} \mathrm{U}_{s[k]}\left(x_{s}, x_{c(s)}, \theta_{s}\right) \mathrm{P}\left(x_{s}, x_{c(s)} \mid x_{t}, x_{e}, \theta\right)
\end{aligned}
$$

In this manner, compute $\mathrm{E}\left[\mathrm{U}_{s[k]}\right]$ given each value $x_{t}$ of $\mathrm{X}_{t}$. The algorithm must now be run again without conditioning on $\mathrm{X}_{t}$ (but still conditioning on $\mathrm{X}_{e}=x_{e}$ ). The first expectation in (4) is now computed as follows :

$$
\mathrm{E}\left[\mathrm{U}_{s[k]} \mid x_{e}\right]=\sum_{x_{t}} \mathrm{E}\left[\mathrm{U}_{s[k]} \mid x_{t}, x_{e}\right] \mathrm{P}\left(x_{t} \mid x_{e}, \theta\right)
$$

The values (7) and (8) may be substituted into (4) to yield the sensitivity value.
Approximating (4) using Monte Carlo simulation is also straightforward. For each node $\mathrm{X}_{s}$ for which sensitivities are to be calculated, define arrays $\mathrm{A}_{s[k]}$ and $\mathrm{B}_{s[k]}$, each with one element for each possible value of $\mathrm{X}_{t}$. Initialize the array values to zero. Each iteration of the algorithm yields a realization $x$ of all nodes in the network and a
sampling weight $w .{ }^{2}$ Compute $\mathrm{U}_{s[k]}\left(x_{s}, x_{c(s)}, \theta_{s}\right)$ and increment $\mathrm{A}_{s[k]}\left(x_{t}\right)$ by its value. Increment $\mathrm{B}_{s[k]}\left(x_{t}\right)$ by $w$.
After the simulation is run, compute the estimates

$$
\begin{aligned}
& \hat{\mathrm{E}}\left[\mathrm{U}_{s[k]}\left|x_{t}, x_{e}\right|=\frac{\mathrm{A}_{s[k]}\left(x_{t}\right)}{\mathrm{B}_{s[k]}\left(x_{t}\right)} \quad \text { and } \\
& \hat{\mathrm{E}}\left[\mathrm{U}_{s[k]}\left|x_{e}\right|=\frac{\sum_{x_{t}} \mathrm{~A}_{s[k]}\left(x_{t}\right)}{\sum_{x_{t}} \mathrm{~B}_{s[k]}\left(x_{t}\right)}\right.
\end{aligned}
$$

These estimates can be plugged into (4) to estimate the desired sensitivity values.

## 3. EXAMPLE

The graph of Figure 1 is taken from Neapolitan (1990), from an example originally due to Lauritzen and Spiegelhalter. The local probability distributions for this example are given in Table 1. Sensitivity values for this network were computed as described in Section 2.3 using the Lauritzen and Spiegelhalter algorithm as implemented in IDEAL (Srinivas and Breese, 1992), using the unrestricted node model of Example 1. The evidence nodes were $\mathrm{A}=t_{\mathrm{A}}$ and $\mathrm{H}=q_{\mathrm{H}}$ (dyspnea observed in a patient who had been to Asia). Sensitivities were computed for target value $\mathrm{B}=t_{\mathrm{B}}$ (patient has tuberculosis). Table 2 summarizes the sensitivity information for each node's local probability distribution. The value shown is the largest value of $\left|\mathrm{U}_{s\left(x_{t}, x_{s(t)}\right)}\right|$ for the node. Variable C is not shown. Because C is defined as a deterministic function of the values of its parent variables B and E , so sensitivities for C are not of interest.
The local distribution to which the target probability $\mathrm{P}\left(\mathrm{B}=t_{\mathrm{B}} \mid \mathrm{A}=t_{\mathrm{A}}, \mathrm{H}=q_{\mathrm{H}}\right)$ is most sensitive is the distribution of B given $\mathrm{A}=t_{\mathrm{A}}$. The maximum sensitivity value for the local distribution of B is about 1.6. This value corresponds to the distribution of B when $\mathrm{A}=t_{\mathrm{A}}$ (the sensitivity for $\mathrm{A}=f_{\mathrm{A}}$ is zero because the conditional distribution of B given $f_{\mathrm{A}}$ is irrelevant given the scenario in which $\mathrm{A}=t_{\mathrm{A}}$ ). This large value is not surprising because the evidence variable A is a direct predecessor of B. One certainly expects $\mathrm{P}(\mathrm{B} \mid \mathrm{A}, \mathrm{E})$ to be highly sensitive to $\mathrm{P}(\mathrm{B} \mid \mathrm{A})$.
The largest value for this node is greater by a factor of 18 than maximum value for node H (dyspnea), another local distribution for an evidence node. The local distributions for E (lung cancer) and G (bronchitis), both competing explanations for the finding of dyspnea, have maximum sensitivities about half that for node H . The node F (smoking), which affects the prior probabilities of both E and $G$, has about half the maximum sensitivity value of either of these nodes. Finally, all sensitivities for A and D

[^0]
[^0]:    ${ }^{2}$ The sampling weight adjusts for the effect of efficiency improving modifications such as likelihood weighting and importance sampling. A weight of zero is given to any observation for which $\mathrm{X}_{e}=x_{e}$.

are zero. In the absense of any observations, the local conditional distribution of $D$ has no effect on the posterior probability of $B$. The prior probability of $A$ is irrelevant once the value of $A$ becomes known.
![img-0.jpeg](img-0.jpeg)

Figure 1: Example Network


Table 1: Probabilities for Dyspnea Example


Table 2: Sensitivities for Dyspnea Example
Evidence $\mathrm{A}=\mathrm{I}_{\mathrm{A}}, \mathrm{H}=4 \mathrm{I}$; Target $\mathrm{B}=\mathrm{B}$

## 4. INCORPORATING DIRECT ESTIMATES OF TARGET DISTRIBUTIONS

### 4.1 Adjusting to Fit a Directly Assessed Distribution

Suppose the expert provides not only the local conditional probability distributions $\mathrm{P}\left(x_{t} \mid x_{C(s)}, \theta_{s}\right)$ but also direct assessments of target probability distributions for a set of scenarios. I consider here how to use these direct assessments in estimating model parameters.
Begin with an initial model $P(x \mid \theta)$. Suppose the expert is given a scenario $X_{e}=x_{e}$ and assesses directly the distribution of a target variable $P^{*}\left(x_{t} \mid x_{e}\right)$. In general this will be different from the model distribution $\mathrm{P}\left(x_{t} \mid x_{e}, \theta\right)$. Suppose the expert wishes guidance on how to change the model to bring $\mathrm{P}\left(x_{t} \mid x_{e}, \theta\right)$ closer to $\mathrm{P}^{*}\left(x_{t} \mid x_{e}\right)$.
A way to measure distance between $\mathrm{P}\left(x_{t} \mid x_{e}, \theta\right)$ and $\mathrm{P}^{*}\left(x_{t} \mid x_{e}\right)$ is to use a proper scoring rule. A scoring rule assigns a score $\mathrm{s}\left(x_{t}, \mathrm{P}\right)$ if outcome $x_{t}$ occurs and the probability distribution P was assessed. If $\mathrm{P}^{*}$ is the correct distribution, the expected score is

$$
\begin{aligned}
\mathrm{d}\left(\mathrm{P}, \mathrm{P}^{*}\right) & =\mathrm{E}_{\mathrm{P}^{*}}\left[\mathrm{~s}\left(\mathrm{X}_{t}, \mathrm{P}^{*}\right)-\mathrm{s}\left(\mathrm{X}_{t}, \mathrm{P}\right)\right] \\
& =\sum_{x_{t}}\left(\mathrm{~s}\left(x_{t}, \mathrm{P}^{*}\right)-\mathrm{s}\left(x_{t}, \mathrm{P}\right)\right) \mathrm{P}^{*}\left(x_{t} \mid x_{e}\right)
\end{aligned}
$$

A scoring rule is proper if (10) is always positive (i.e., one maximizes one's expected score by assessing the correct distribution). I make the assumption that (10) can be written as

$$
\begin{aligned}
& \mathrm{d}\left(\mathrm{P}, \mathrm{P}^{*}\right)= \\
& \quad \sum_{x_{t}} h\left(\mathrm{P}\left(x_{t} \mid x_{e}, \theta\right), \mathrm{P}^{*}\left(x_{t} \mid x_{e}\right)\right) \mathrm{P}^{*}\left(x_{t} \mid x_{e}\right)
\end{aligned}
$$

This is the case for two of the most common scoring rules, the quadratic and logarithmic rules as defined in Lindley (1982). For these two rules, $h\left(\mathrm{P}, \mathrm{P}^{*}\right)$ is given by

$$
\begin{aligned}
& h_{\log }\left(\mathrm{P}, \mathrm{P}^{*}\right)=\log (\mathrm{P})-\log \left(\mathrm{P}^{*}\right) \text { and } \\
& h_{\text {quad }}\left(\mathrm{P}, \mathrm{P}^{*}\right)=\mathrm{P}^{*}\left(1-\mathrm{P}^{*}\right)+\left(\mathrm{P}-\mathrm{P}^{*}\right)^{2}
\end{aligned}
$$

respectively.
Using the results of the previous section, the partial derivative of (10) with respect to $\theta_{s[k]}$ can be computed:

$$
\frac{\partial}{\partial \theta_{s[k]}} \mathrm{d}\left(\mathrm{P}, \mathrm{P}^{*}\right)=
$$

$$
\sum_{x_{t}}\left(\frac{\partial}{\partial \mathrm{P}} \hbar\left(\mathrm{P}, \mathrm{P}^{*}\right)\right)\left(\frac{\partial}{\partial \theta_{s[k]}} \mathrm{P}\left(x_{t} \mid x_{e}, \theta\right)\right) \mathrm{P}^{*}\left(x_{t} \mid x_{e}\right)
$$

which is straightforward to compute from (4) and the distributions P and $\mathrm{P}^{*}$.
It is interesting to note that for the logarithmic scoring rule (14) reduces to

$$
\begin{aligned}
& \frac{\partial}{\partial \theta_{s[k]}} \mathrm{d}\left(\mathrm{P}, \mathrm{P}^{*}\right)= \\
& \quad \sum_{x_{t}}\left(\mathrm{E}\left[\mathrm{U}_{s[k]} \mid x_{t}, x_{e}\right]-\mathrm{E}\left[\mathrm{U}_{s[k]} \mid x_{e}\right]\right) \mathrm{P}^{*}\left(x_{t} \mid x_{e}\right) \\
& \quad=E^{*}\left[\mathrm{U}_{s[k]} \mid x_{e}\right]-\mathrm{E}\left[\mathrm{U}_{s[k]} \mid x_{e}\right]
\end{aligned}
$$

The first expression on the right side of (15) denotes the expectation of $\mathrm{U}_{S[k]}$ taken under the distribution $\mathrm{Q}(\mathrm{X})=$ $\mathrm{P}^{*}\left(\mathrm{X}_{t}\right) \mathrm{P}\left(\mathrm{X} \mid \mathrm{X}_{t}\right)=\mathrm{P}(\mathrm{X})\left(\mathrm{P}^{*}\left(\mathrm{X}_{t}\right) / \mathrm{P}\left(\mathrm{X}_{t}\right)\right)$. That is, (15) is the difference in the expectation of $\mathrm{U}_{S[k]}$ under two distributions, one in which the distribution of $x_{t}$ is set equal to the holistically assessed distribution and the other equal to the model distribution.
If holistic assessments are made for a number of scenarios, (15) can be computed and examined separately for each scenario. Alternatively, an aggregate goodness-of-fit measure can be computed by summing values of (10) for different scenarios (the sum can be weighted by importance of the assessment or by a measure of how sure the expert is of the judgment). The appropriate derivative then is the corresponding (perhaps weighted) sum of values of (15).

### 4.2 Automating Best-Fit Assessments

The methods presented here can also be used to compute a best-fit model (under one of the scoring rules presented in Section 3.1) given a set of judgments (holistic and local) from an expert. A simple gradient descent method can be defined as follows.

1. Initialize the network probabilities.
2. Select a scenario. (A scenario is a conditional probability distribution assessed by the expert. A local conditional distribution counts as a scenario. Scenario selection may be random or may cycle through the scenarios in some fixed order.)
3. Compute (15) for all relevant nodes. ( $D$ separation can be used to eliminate some computations. If the scenario is an assessment of a local conditional distributions, only the distribution for that node need be considered.)
4. Change all relevant $\theta_{S[k]}$ by an amount proportional to (15).
5. Cycle through Steps 2 through 4 until a convergence criterion is met.
This gradient descent approach is employed by common neural network learning algorithms (e.g., backpropagation and Boltzmann machine learning; see Laskey, 1990).
This algorithm may stop at a local optimum (the objective function is generally not convex in the parameters). If all local probability assessments are available, they determine a consistent global model which may make a good starting value for $\theta$. It may be desirable to restart the algorithm from different starting values. Cycling through scenarios in random order introduces a random element to the algorithm, which may help prevent its becoming stuck in local optima.
Of course, it is always a good idea to identify and set aside for special examination any outliers, or assessments for which the estimated model fits very poorly.

## 5. DISCUSSION

This paper describes a method for computing the sensitivity of a target probability or a target distribution to changes in network parameters. Sensitivity values can be computed one scenario (instantitation of evidence variables) at a time, or sensitivities of an aggregate goodness-of-fit measure for multiple scenarios can be computed. The method can be adapted for automated fitting of a best-fitting model to a set of holistic and local judgments.
This paper considered the problem of adjusting the parameter values in a model with fixed structure. Another important part of the knowledge elicitation process is changing the structure of a model to better fit the expert's judgments. Sensitivity values can also be used to suggest links to add. The absence of a link in the network can be viewed as the assignment of a zero value to a log-linear interaction term. For each link one wishes to consider adding to the network, one can compute a sensitivity value for this parameter. If the sensitivity value is large, there is a large improvement in model fit by adding the extra link.

## APPENDIX: PROOFS OF RESULTS

The proof of Proposition 1 requires the following lemma.
Lemma 1. The partial derivative of the unconditional probability value $\mathrm{P}(x \mid \theta)$ with respect to the parameter value $\theta_{s[k]}$ is given by:

$$
\frac{\partial}{\partial \theta_{s[k]}} \mathrm{P}(x \mid \theta)=\mathrm{P}(x \mid \theta) \mathrm{U}_{s[k]}\left(x_{s}, x_{c(s)}, \theta_{s}\right)
$$

Proof of Lemma 1:

$$
\begin{aligned}
& \frac{\partial}{\partial \theta_{s[k]}} \mathrm{P}(x \mid \theta)= \\
& \prod_{i \neq s} \mathrm{P}\left(x_{i} \mid x_{c(i)}, \theta_{i}\right)\left(\frac{\partial}{\partial \theta_{s[k]}} \mathrm{P}\left(x_{s} \mid x_{c(s)}, \theta_{s}\right)\right) \\
& =\mathrm{P}(x \mid \theta) \frac{\frac{\partial}{\partial \theta_{s[k]}} \mathrm{P}\left(x_{s} \mid x_{c(s)}, \theta_{s}\right)}{\mathrm{P}\left(x_{s} \mid x_{c(s)}, \theta_{s}\right)} \\
& =\mathrm{P}(x \mid \theta) \frac{\partial}{\partial \theta_{s[k]}} \log \mathrm{P}\left(x_{s} \mid x_{c(s)}, \theta_{s}\right) .
\end{aligned}
$$

Proof of Proposition 1:

$$
\frac{\partial \mathrm{P}\left(x_{t} \mid x_{e}, \theta\right)}{\partial \theta_{s[k]}}=
$$

$$
\begin{aligned}
& \frac{\partial}{\partial \theta_{s[k]}}\left(\frac{\sum_{x_{s}, x_{u}} \mathrm{P}\left(x_{t}, x_{s}, x_{u}, x_{e} \mid \theta\right)}{\sum_{x_{i}^{\prime}, x_{s}, x_{u}} \mathrm{P}\left(x_{t}^{\prime}, x_{s}, x_{u}, x_{e} \mid \theta\right)}\right) \\
& =\frac{\sum_{x_{s}, x_{u}} \mathrm{P}\left(x_{t}, x_{s}, x_{u}, x_{e} \mid \theta\right) \mathrm{U}_{s[k]}\left(x_{s}, x_{c(s)}, \theta_{s}\right)}{\sum_{x_{i}^{\prime}, x_{s}, x_{u}}} \\
& -\left(\sum_{x_{s}, x_{u}} \mathrm{P}\left(x_{t}, x_{s}, x_{u}, x_{e} \mid \theta\right)\right) \times \\
& \left(\frac{\sum_{x_{i}^{\prime}, x_{s}, x_{u}} \mathrm{P}\left(x_{t}^{\prime}, x_{s}, x_{u}, x_{e} \mid \theta\right) \mathrm{U}_{s[k]}\left(x_{s}, x_{c(s)}, \theta_{s}\right)}{\sum_{x_{i}^{\prime}, x_{s}, x_{u}} \mathrm{P}\left(x_{t}^{\prime}, x_{s}, x_{u}, x_{e} \mid \theta\right)}\right)^{2} \\
& =\sum_{x_{s}, x_{u}} \mathrm{P}\left(x_{t}, x_{s}, x_{u} \mid x_{e}, \theta\right) \mathrm{U}_{s[k]}\left(x_{s}, x_{c(s)}, \theta_{s}\right) \\
& -\left(\sum_{x_{s}, x_{u}} \mathrm{P}\left(x_{t}, x_{s}, x_{u} \mid x_{e}, \theta\right)\right) \times \\
& \left(\sum_{x_{i}^{\prime}, x_{s}, x_{u}} \mathrm{P}\left(x_{t}^{\prime}, x_{s}, x_{u} \mid x_{e}, \theta\right) \mathrm{U}_{s[k]}\left(x_{s}, x_{c(s)}, \theta_{s}\right)\right) \\
& =\mathrm{P}\left(x_{t} \mid x_{e}, \theta\right) \times \\
& \sum_{x_{s}, x_{u}} \mathrm{P}\left(x_{s}, x_{u} \mid x_{t}, x_{e}, \theta\right) \mathrm{U}_{s[k]}\left(x_{s}, x_{c(s)}, \theta_{s}\right) \\
& -\mathrm{P}\left(x_{t} \mid x_{e}, \theta\right) \times \\
& \left(\sum_{x_{i}^{\prime}, x_{s}, x_{u}} \mathrm{P}\left(x_{t}^{\prime}, x_{s}, x_{u} \mid x_{e}, \theta\right) \mathrm{U}_{s[k]}\left(x_{s}, x_{c(s)}, \theta_{s}\right)\right) \\
& =\mathrm{P}\left(x_{t} \mid x_{e}, \theta\right)\left(\mathrm{E}\left[\mathrm{U}_{s[k]}\left(x_{s}, x_{c(s)}, \theta_{s}\right) \mid x_{t}, x_{e}\right]\right. \\
& \left.-\mathrm{E}\left[\mathrm{U}_{s[k]}\left(x_{s}, x_{c(s)}, \theta_{s}\right) \mid x_{e}\right]\right) .
\end{aligned}
$$