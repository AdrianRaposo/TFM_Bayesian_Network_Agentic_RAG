# THE BELIEF NOISY-OR MODEL APPLIED TO NETWORK RELIABILITY ANALYSIS 

KUANG ZHOU<br>Northwestern Polytechnical University<br>Xi'an, Shaanxi 710072, China<br>DRUID, IRISA, University of Rennes 1<br>Rue E. Branly, 22300 Lannion, France<br>kzhoumath@163.com<br>ARNAUD MARTIN<br>DRUID, IRISA, University of Rennes 1<br>Rue E. Branly, 22300 Lannion, France<br>arnaud.martin@univ-rennes1.fr<br>QUAN PAN<br>Northwestern Polytechnical University<br>Xi'an, Shaanxi 710072, China<br>quanpan@nwpu.edu.cn<br>Received (received date)<br>Revised (revised date)

One difficulty faced in knowledge engineering for Bayesian Network (BN) is the quantification step where the Conditional Probability Tables (CPTs) are determined. The number of parameters included in CPTs increases exponentially with the number of parent variables. The most common solution is the application of the so-called canonical gates. The Noisy-OR (NOR) gate, which takes advantage of the independence of causal interactions, provides a logarithmic reduction of the number of parameters required to specify a CPT. In this paper, an extension of NOR model based on the theory of belief functions, named Belief Noisy-OR (BNOR), is proposed. BNOR is capable of dealing with both aleatory and epistemic uncertainty of the network. Compared with NOR, more rich information which is of great value for making decisions can be got when the available knowledge is uncertain. Specially, when there is no epistemic uncertainty, BNOR degrades into NOR. Additionally, different structures of BNOR are presented in this paper in order to meet various needs of engineers. The application of BNOR model on the reliability evaluation problem of networked systems demonstrates its effectiveness.

Keywords: Evidential network; Belief Noisy-OR; Conditional belief function; Uncertainty; Network reliability

# 1. Introduction 

Bayesian Network (BN) is a probabilistic graphical model that represents a set of random variables and their conditional dependencies via a directed acyclic graph (DAG) ${ }^{1}$. BN can be used to learn causal relationships and gain understanding of a problem domain. It allows probabilistic beliefs to be updated automatically when new information becomes available. BN is also able to represent multi-attribute correlated variables and to perform relevant simulations or diagnoses. Owing these advantages, it has been widely applied on the problem of reliability or safety analysis for both static and dynamic systems ${ }^{2-5}$.

In BN, Conditional Probability Tables (CPTs) should be defined to measure the relationships between variables. However, it has been pointed out that it is usually difficult to quantify the CPTs due to the complexity ${ }^{6}$. One of the most appropriate solutions to this problem is the Noisy-OR (NOR) gate, which can be attributed to Pearl ${ }^{7}$. Traditional NOR can only deal with the binary variables. Srinivas ${ }^{8}$ extended NOR for $n$-ary input and output variables, and arbitrary functions other than Boolean OR function can be used. But it has not taken into account the uncertainty on parameters and the state which often exists in practice. Considering such uncertainty, Fallet et al. ${ }^{9}$ proposed the imprecise extensions of Noisy OR (ImNOR) thereafter. Nevertheless, there are still some problems for ImNOR which will be discussed in detail later.

The theory of belief functions, also called Dempster-Shafer Theory (DST), offers a mathematical framework for modeling uncertainty and imprecise information ${ }^{10}$. Belief functions are widely employed in various fields, such as data classification ${ }^{11-13}$, data clustering ${ }^{14-17}$, social network analysis ${ }^{18-21}$ and statistical estimation ${ }^{22-24}$. The concept of evidential networks, which is a combination of belief function theory and Bayesian network, is proposed to model system reliability with imprecise knowledge ${ }^{25 ; 26}$. Recently, Yaghlane and Mellouli ${ }^{27}$ presented another definition of evidential networks based on Transferable Belief Model (TBM) ${ }^{28}$, Dempster-Shafer rule of combination, and binary joint trees.

The objective of this work is to enrich the existing NOR structures by integrating several types of uncertainty. Under the framework of belief functions, the Belief Noisy-OR (BNOR) model is put forward. The uncertainty of variable states can be expressed by the power set of discernment frame. The uncertainty of parameters is described by probability intervals based on which the basic belief assignments are determined. The model can model causal connections among variables as well as taking random and epistemic uncertainty into account. The proposed BNOR model can be implemented in evidential networks ${ }^{26}$, and belief reasoning is proceeded through evoking junction tree inference algorithms ${ }^{25 ; 26}$.

The remainder of this paper is organized as follows. In Section 2, the basic knowledge about Noisy-OR gate and Dempster-Shafer theory is briefly introduced. The BNOR model is presented in detail in Section 3. In order to show the effectiveness of BNOR in real practice, Section 4 discusses about how to apply BNOR

on the problem of network reliability evaluation. Conclusions are drawn in the final section.

# 2. Background 

In this section some related preliminary knowledge will be presented. The definition of Noisy-OR gate will be described first, then some basis of belief function theory will be recalled.

### 2.1. Noisy-OR model

The Noisy-OR structure was introduced by Pearl ${ }^{7}$ to reduce the elicitation effort in building a Bayesian network. The general properties of the Noisy-OR function and its generalizations were captured by Heckerman and Breese ${ }^{29}$ in their definition of causal independence.
![img-0.jpeg](img-0.jpeg)

Fig. 1. The causal connections network.

Let us consider a binary variable $Y$ with $n$ binary parent variables $X_{i}$ (see Figure 1-a). These variables can be either "True" $(T)$ or "False" $(F)$. Each $X_{i}$ exerts its influence on $Y$ independently. To build a Bayesian network, $X$ must be associated with a probability distribution $p\left(Y \mid X_{1}, \cdots, X_{n}\right)$. The number of independent parameters included in the complete specification of $p\left(Y \mid X_{1}, \cdots, X_{n}\right)$ is $2^{n}$. The Noisy-OR function is an attractive way where we can use fewer parameters to specify $p\left(Y \mid X_{1}, \cdots, X_{n}\right)$. The idea is to start with $n$ probability values $p_{i}$, which is the probability that $\{Y=T\}$ conditional on $\left\{X_{i}=T\right\}$ and $\left\{X_{j}=F\right\}$ for $j \neq i$, i.e.,

$$
p_{i}=p\left\{Y=T \mid X_{i}=T,\left\{X_{j}=F\right\}_{j=1, j \neq i}^{n}\right\}
$$

Probability $p_{i}$ is often called "link probability" and illustrates the fact that the causal dependency between $X_{i}$ and $Y$ can be inhibited. If the state of variable $X_{i}$ is $T$, then there is chance $1-p_{i}$ that it is flipped to $F$; If $X_{i}$ is $F$, then it stays with $F$. Denote the result of flipping (or not) $X_{i}$ by $\xi_{i}, i=1,2, \cdots, n$ (see Figure 1-b), then

$$
p\left(Y=\alpha \mid X_{1}, X_{2}, \cdots, X_{n}\right)=\sum_{\alpha_{1} \vee \cdots \vee \alpha_{n}=\alpha} p\left(\xi_{1}=\alpha_{1} \mid X_{1}\right) \cdots p\left(\xi_{n}=\alpha_{n} \mid X_{n}\right)
$$

where the values of $\alpha, \alpha_{i}$ are either $T$ or $F$. A Noisy-OR function is thus a disjunction of "noisy" versions of $X_{i}{ }^{30}$. Let $\boldsymbol{X}_{T}$ be the set of $X_{i}$ whose state is "True", and $\boldsymbol{X}_{F}$ be the set of $X_{i}$ which are "False". The distribution of $Y$ conditional on $X_{1}, X_{2}, \cdots, X_{n}$ is

$$
p\left(Y=T \mid X_{1}, X_{2}, \cdots, X_{n}\right)=1-\prod_{i: X_{i} \in \boldsymbol{X}_{T}}\left(1-p_{i}\right)
$$

We can see the number of independent parameters required for the conditional probability function is reduced from $2^{n}$ to $2 n^{31}$. The following example shows how to create CPTs by the use of NOR gate.
Example 1. Let us consider the Alarm System (see Figure 2). Both a burglar $(B)$ and an earthquake $(E)$ can set the alarm $(A)$ off but neither always do so. The mechanism of the burglar and earthquake is different, thus they can be regarded as independent causes. Variable $B^{\prime}$ (respectively, $E^{\prime}$ ) describes the result after flipping (or not) of $B$ (respectively, $E$ ). Assume all variables are binary with values $\{T, F\}$, where $T$ represents the corresponding event happens, while $F$ means not.

Apparently, $A$ is $F$ only if both the occurrence of burglar and earthquake do not evoke the alarm due to inhibition. Using the Noisy-OR model, we can get,

$$
p(A=F \mid B, E)=\prod_{i \in \boldsymbol{X}_{T}}\left(1-p_{i}\right)
$$

The conditional probability on $\{A=T\}$ can be obtained easily:

$$
p(A=T \mid B, E)=1-\prod_{i \in X_{T}}\left(1-p_{i}\right)
$$

The following CPT can be got using Eqs. (4) and (5).

# 2.2. Belief function theory 

To apply the theory of belief functions, we consider a set of $q$ mutually exclusive $\&$ exhaustive elements, called the frame of discernment, defined by

$$
\Theta=\left\{\theta_{1}, \theta_{2}, \cdots, \theta_{q}\right\}
$$

Table 1. The conditional probability table.


![img-1.jpeg](img-1.jpeg)

Fig. 2. The alarm network.

Let $X$ be a variable taking values in $\Theta$. The function $m: 2^{\Theta} \rightarrow[0,1]$ is said to be the basic belief assignment (bba) on $2^{\Theta}$, if it satisfies:

$$
\sum_{A \subseteq \Theta} m(A)=1
$$

and

$$
m(\emptyset)=0
$$

The constraint on $\emptyset$ defined by Eq. (8) is not mandatory. It assumes that one and only one element in $\Theta$ is true (closed-world assumption). In the case where $m(\emptyset) \neq 0$, the model accepts that none of the elements could be true (open-world assumption) ${ }^{28}$. The closed-world assumption is accepted hereafter. Every $A \in 2^{\Theta}$ such that $m(A)>0$ is called a focal element. Uncertain and imprecision knowledge about the actual value of $X$ can be represented by a bba distributed on $2^{\Theta}$ :

$$
\boldsymbol{M}_{X}=\left[m\left(A_{1}\right), m\left(A_{2}\right), \cdots, m\left(A_{2^{q}-1}\right)\right]
$$

where $A_{1}, A_{2}, \cdots, A_{2^{q}-1}$ are the elements of $2^{\Theta}$ arranged by natural order.
The credibility and plausibility functions are derived from a bba $m$ as in Eqs. (10) and (11).

$$
\operatorname{Bel}(A)=\sum_{B \subseteq A} m(B), \quad \forall A \subseteq \Theta
$$

$$
\operatorname{Pl}(A)=\sum_{B \cap A \neq \emptyset} m(B), \quad \forall A \subseteq \Theta
$$

$\operatorname{Bel}(A)$ measures the minimal belief on $A$ justified by available information on $B(B \subseteq A)$, while $\operatorname{Pl}(A)$ is the maximal belief on $A$ justified by information on $B$ which are not contradictory with $A(A \cap B \neq \emptyset)$. The bba can be recovered from credibility functions through the fast Möbius transformations ${ }^{32}$ :

$$
m(A)=\sum_{B \subseteq A}(-1)^{|A-B|} \operatorname{Bel}(B), \forall A \subseteq \Theta
$$

The relations between Bel and Pl can be established as follows:

$$
\operatorname{Bel}(A)=1-\operatorname{Pl}(\bar{A}), \quad \operatorname{Pl}(A)=1-\operatorname{Bel}(\bar{A})
$$

where $\bar{A}$ denotes the complementary set of $A$. $\operatorname{Bel}(\bar{A})$ is often called the doubt in $A$. Let $\operatorname{Pr}(A)$ denote the probability of the hypothesis $A$, it is easy to get:

$$
\operatorname{Bel}(A) \leq \operatorname{Pr}(A) \leq \operatorname{Pl}(A)
$$

Probability $\operatorname{Pr}(A)$ belongs to the interval $[\operatorname{Bel}(A), \operatorname{Pl}(A)]$ but its exact value remains unknown. The bounding property (14) has been well defined in the work of Shafer ${ }^{10}$.

Ferson et al. ${ }^{33}$ argued that each Dempster-Shafer structure specifies a unique probability-box (p-box), and that each p-box specifies an equivalent class of Dempster-Shafer structure ${ }^{26}$. P-boxes are sometimes considered as a granular approach of imprecise probabilities ${ }^{34}$, which are arbitrarily sets of probability distributions. Probability interval $[\underline{P}(A), \bar{P}(A)]$, which is the restricted case of p-box ${ }^{26}$, can also be used to describe the imprecision of a probability measure. The relation between a probability interval and a bba can be directly obtained ${ }^{26}$ :

$$
[\underline{P}(A), \bar{P}(A)]=[\operatorname{Bel}(A), \operatorname{Pl}(A)]
$$

Belief functions can be transformed into probability distribution functions by Smets method ${ }^{36}$, where each mass of belief $m(A)$ is equally distributed among the elements of $A$. This leads to the concept of pignistic probability, BetP. For all $\theta_{i} \in \Theta$, we have

$$
\operatorname{Bet} P\left(\theta_{i}\right)=\sum_{A \subseteq \Theta \mid \theta_{i} \in A} \frac{m(A)}{|A|(1-m(\emptyset))}
$$

where $|A|$ is the cardinality of set $A$ (number of elements of $\Theta$ in $A$ ). Pignistic probabilities can help us make a decision.

# 3. Belief Noisy-OR model 

We start with the discussion of the uncertainty problem in NOR model. One of the existing approaches to express the uncertain information in NOR is the ImNOR model proposed by Fallet et al. ${ }^{9}$. We will analyze the drawbacks of ImNOR and present a new NOR gate using the theory of belief functions.

# 3.1. The uncertainty problem in NOR structure 

From an industrial point of view, it is classically accepted that observations made on the system are partially realized ${ }^{35}$. For example, it is difficult to determine whether an earthquake has happened, especially when the magnitude is small and the hypo-center is deep. In such a case, there is some uncertainty on the state of boolean parent variables and it is intuitive for experts to give a positive belief on the ignorant modality $\{T, F\}$. Simon and Weber ${ }^{26}$ have investigated a solution based on evidential network and the theory of belief functions to take into account the uncertainty on the state of binary parent variables in AND/OR gates. Simon et al. ${ }^{25}$ combined belief function theory with Bayesian reasoning to deal with this type of epistemic uncertainty. Based on Simon and Weber's modelling formalization, Fallet et al. ${ }^{9}$ proposed imprecise extensions of the Noisy-OR (ImNOR) structure to deal with the uncertainty on the state of variables and link probabilities.

ImNOR describes the uncertainty on variable state and link probabilities separately by calculating the lower bounds of the conditional probability $P(X \mid \operatorname{Pa}(X))$, where $\operatorname{Pa}(X)$ denotes the parent nodes of $X$. Consider the causal network shown in Figure 1-a. As before, the discernment frame of each variable is $\{T, F\}$, and each $X_{i}$ is interpreted as an independent "cause" of $Y$. We can express our epistemic uncertainty on variables' state by assigning the basic belief to ignorant modality $\{T, F\}$. This modality indicates that the variable is exclusively in $\{T\}$ or $\{F\}$ state without distinguishing exactly in which state it is ${ }^{9}$. Different from Noisy-OR model, in ImNOR, each active $X_{i}$ can evoke $Y$ with unknown probability $p_{i} \in\left[p_{i L}, p_{i U}\right]$, where $p_{i U}-p_{i L}$ measures the degree of uncertainty on our knowledge of inhibition. Fallet provided us the formulas (see Eqs. (17)-(19)) to calculate the conditional belief mass functions ${ }^{1}$ :

$$
\begin{gathered}
m\left(Y=\{T\} \mid X_{1}, X_{2}, \cdots, X_{n}\right)=1-\prod_{\left\{i: X_{i}=\{T\}\right\}}\left(1-p_{i L}\right) \\
m\left(Y=\{F\} \mid X_{1}, X_{2}, \cdots, X_{n}\right)=\prod_{\left\{i: X_{i}=\{T\}\right\}}\left(1-p_{i U}\right) \prod_{\left\{i: X_{i}=\{T, F\}\right\}}\left(1-p_{i U}\right) \\
m\left(Y=\{T, F\} \mid X_{1}, X_{2}, \cdots, X_{n}\right)=\prod_{\left\{i: X_{i}=\{T\}\right\}}\left(1-p_{i L}\right)-\prod_{\left\{i: X_{i}=\{T\}\right\}}\left(1-p_{i U}\right) \prod_{\left\{i: X_{i}=\{T, F\}\right\}}\left(1-p_{i U}\right)
\end{gathered}
$$

From Eq. (17), we can get:

$$
m\left(Y=\{T\} \mid X_{1} \cdots X_{k}=\{T, F\} \cdots X_{n}\right)=1-\prod_{\left\{i: X_{i}=\{T\}, i \in\{1,2, \cdots, k-1, k+1, \cdots, n\}\right\}}\left(1-p_{i L}\right)
$$

[^0]
[^0]:    ${ }^{1}$ As the belief functions are defined on the power set of discernment frame, we use $\{T\}\left(\{F\}\right)$ instead of $T(F)$ to denote variable state here.

and
$m\left(Y=\{T\} \mid X_{1} \cdots X_{k}=\{F\} \cdots X_{n}\right)=1-\prod_{\left\{i: X_{i}=\{T\}, i \in\{1,2, \cdots, k-1, k+1, \cdots, n\}\right\}}\left(1-p_{i L}\right)$.
It can be seen that the belief on the proposition that "variable $Y$ is $\{T\}$ " does not change when some prior precise information about the parent variables becomes available (The state of $X_{k}$ changes from $\{T, F\}$ to $\{T\}$ ):
$m\left(Y=\{T\} \mid X_{1}, \cdots, X_{i}=\{T, F\}, \cdots X_{n}\right)=m\left(Y=\{T\} \mid X_{1}, \cdots, X_{i}=\{F\}, \cdots, X_{n}\right)$.
Besides, there is another defect for the above method when calculating the belief mass on the conditional events where there is no working components $\left(X_{i} \neq T, i=\right.$ $1,2, \cdots, n)$. For example, when we want to know

$$
m\left(Y \mid X_{i}=\{F\}, i=1,2, \cdots, n-1, X_{n}=\{T, F\}\right)
$$

the following conditional belief mass functions can be got by Eq. (18):

$$
\begin{gathered}
m\left(Y=\{F\} \mid X_{i}=\{F\}, i=1,2, \cdots, n-1, X_{n}=\{T, F\}\right)=1-P_{n U} \\
m\left(Y=\{F\} \mid X_{i}=\{\mathrm{T}, \mathrm{~F}\}, i=1,2, \cdots, n-1, X_{n}=\{T, F\}\right)=P_{n U}
\end{gathered}
$$

As can be seen, the lower bound of probability $p_{n}, p_{n L}$, has no effect on the final results. That is to say, the conditional belief mass assignment remains unchanged once the upper bound of $p_{n}$ is fixed no matter how long the uncertain interval is. This is against our common sense. Since the length of the interval measures the degree of uncertainty on the available information, the longer the interval is, more mass value should be given to the ignorant state $\{T, F\}$.

# 3.2. Belief Noisy-OR structure 

We introduce here the Belief Noisy-OR structure to express the epistemic uncertainty on the state of the variables and link probabilities at the same time. Consider the causal network where $X_{i}, i=1,2, \cdots, n$ are the parents of $Y$ (Figure 1-a).

Let us first discuss the uncertainty on link probability $p_{i}$. This parametric uncertainty can be modeled by an interval $\left[p_{i L}, p_{i U}\right]$, with $0 \leq p_{i L} \leq p_{i} \leq p_{i U} \leq 1$. Thus the inhibition probability interval of $X_{i}$ is $\left[1-p_{i U}, 1-p_{i L}\right]$. In order to use evidential reasoning, the probability intervals should be transformed to belief function structures. For convenience, $n$ auxiliary variables, $X_{i}^{\prime}, i=1,2, \cdots, n$ are introduced to represent the result of flipping or not $X_{i}$. From the boundary property of belief functions (Eq. (14)), we can get

$$
\begin{gathered}
\operatorname{Bel}\left(X_{i}^{\prime}=\{T\} \mid X_{i}=\{T\}\right)=p_{i L} \\
\operatorname{Pl}\left(X_{i}^{\prime}=\{T\} \mid X_{i}=\{T\}\right)=p_{i U}
\end{gathered}
$$

The associated belief mass distribution can be easily determined by Eq. (12). The corresponding conditional bba in $2^{\Theta}$ can be defined as:

$$
\begin{gathered}
m\left(X_{i}^{\prime}=\{T\} \mid X_{i}=\{T\}\right)=B e l\left(X_{i}^{\prime}=\{T\} \mid X_{i}=\{T\}\right)=p_{i L} \\
m\left(X_{i}^{\prime}=\{F\} \mid X_{i}=\{T\}\right)=B e l\left(X_{i}^{\prime}=\{F\} \mid X_{i}=\{T\}\right) \\
=1-P l\left(X_{i}^{\prime}=\{T\} \mid X_{i}=\{T\}\right) \\
=1-p_{i U}
\end{gathered}
$$

and

$$
m\left(X_{i}^{\prime}=\{T, F\} \mid X_{i}=\{T\}\right)=p_{i U}-p_{i L}
$$

where Eq. (29) is obtained by the relation between Bel and Pl. Eqs. (27)-(31) express the uncertain knowledge of link probabilities and variable states together in the form of belief mass distributions.

When $X_{i}=\{F\}, Y$ is sure to stay in state $\{F\}$. Thus the bba conditioned $X_{i}=\{F\}$ is easy to determine:

$$
\begin{gathered}
m\left(X_{i}^{\prime}=\{T\} \mid X_{i}=\{F\}\right)=0 \\
m\left(X_{i}^{\prime}=\{F\} \mid X_{i}=\{F\}\right)=1 \\
m\left(X_{i}^{\prime}=\{\mathrm{T}, \mathrm{~F}\} \mid X_{i}=\{F\}\right)=0
\end{gathered}
$$

However, the bba on the condition $X_{i}=\{\mathrm{T}, \mathrm{F}\}$ is more complicated. The following equations with unknown parameters $\alpha, \beta, \gamma(\alpha+\beta+\gamma=1)$ are first given, and then the methods for designing the three parameters will be discussed later.

$$
\begin{gathered}
m\left(X_{i}^{\prime}=\{T\} \mid X_{i}=\{T, F\}\right)=\alpha \\
m\left(X_{i}^{\prime}=\{F\} \mid X_{i}=\{T, F\}\right)=\beta \\
m\left(X_{i}^{\prime}=\{T, F\} \mid X_{i}=\{T, F\}\right)=\gamma
\end{gathered}
$$

Eqs. (35)-(37) show that in BNOR, the belief on the uncertain state $X_{i}=\{T, F\}$ may be flipped into all the possible states by different ratios. Parameters $\alpha, \beta, \gamma$ are adjustable.

Generally, the values of $\alpha, \beta, \gamma$ can be given by the proportions of belief mass on $X_{i}=\{T, F\}$ which may be transferred to $X_{i}=\{T\}$ (noted by $\lambda_{1}, 0 \leq \lambda_{1} \leq 1$ ),

$X_{i}=\{F\}$ (noted by $\lambda_{2}, 0 \leq \lambda_{2} \leq 1$ ) and $X_{i}=\{T, F\}$ (noted by $\lambda_{3}, 0 \leq \lambda_{3} \leq 1$ ) $\left(\lambda_{1}+\lambda_{2}+\lambda_{3}=1\right)$ respectively:

$$
\begin{gathered}
\alpha=\lambda_{1} m\left(X_{i}^{\prime}=\{T\} \mid X_{i}=\{T\}\right)=\lambda_{1} p_{i L} \\
\beta=\lambda_{1} m\left(X_{i}^{\prime}=\{F\} \mid X_{i}=\{T\}\right)+\lambda_{2}=\lambda_{1}\left(1-p_{i U}\right)+\lambda_{2} \\
\gamma=\lambda_{1} m\left(X_{i}^{\prime}=\{T, F\} \mid X_{i}=\{T\}\right)+\lambda_{3}=\lambda_{1}\left(p_{i U}-p_{i L}\right)+\lambda_{3}
\end{gathered}
$$

Parameter $\lambda_{3}$ in Eq. (40) indicates the uncertainty on the state of $X_{i}$, and it should be in direct proportion to $m\left(X_{i}=\{T, F\}\right) \triangleq \eta$. It is easy to know that if $\eta \neq 0$, $\lambda_{3} \neq 0$. For simplicity, let $\lambda_{3}=\eta$ and $\lambda_{1}=\lambda, \lambda_{2}=1-\lambda-\eta$, then,

$$
\begin{gathered}
\alpha=\lambda m\left(X_{i}^{\prime}=\{T\} \mid X_{i}=\{T\}\right)=\lambda p_{i L} \\
\beta=\lambda m\left(X_{i}^{\prime}=\{F\} \mid X_{i}=\{T\}\right)+(1-\lambda-\eta)=\lambda\left(1-p_{i U}\right)+(1-\lambda-\eta) \\
\gamma=\lambda m\left(X_{i}^{\prime}=\{T, F\} \mid X_{i}=\{T\}\right)+\eta=\lambda\left(p_{i U}-p_{i L}\right)+\eta
\end{gathered}
$$

This is similar to the optimistic coefficient method in the decision theory. So we call this general approach Optimistic coefficient-BNOR (OCBNOR), where $\lambda(0 \leq \lambda \leq$ 1) is the optimistic coefficient.

Note that Eqs. (41)-(43) propagate the uncertainty on variable state and link probabilities simultaneously. The ignorant modality $\Theta=\{T, F\}$ represents the uncertainty on the state and the belief mass assignment $m\left(X_{i}^{\prime} \mid X_{i}\right)$ deals with the uncertain information of link probabilities.

Different $\lambda$ values can be set to obtain results under various requirements. For instance, if we want to make an optimistic decision, the belief to $X_{i}=\{T, F\}$ could transferred to $X_{i}^{\prime}=\{T\}$ as most as possible. Let $\lambda=1$, then

$$
\alpha=p_{i L}, \beta=1-p_{i U}-\eta, \gamma=p_{i U}-p_{i L}+\eta
$$

This structure is called Optimistic Belief Noisy-OR (OBNOR). By contrary, when a pessimistic decision is required, all the belief on $X_{i}=\{T, F\}$ could transferred to the child state $X_{i}^{\prime}=\{F\}$, thus

$$
\alpha=0, \beta=1-\eta, \gamma=\eta
$$

we call this model Pessimistic Belief Noisy-OR (PBNOR).
The decision-makers can make a compromise between optimism and pessimism. According to the idea of pignistic probability transformation ${ }^{36}$, the belief on the subsets of the discernment framework should be given to the single elements equally. Then we can get:

$$
\begin{gathered}
\alpha=\frac{1}{2} m\left(X_{i}^{\prime}=\{T\} \mid X_{i}=\{T\}\right)=\frac{1}{2} p_{i L} \\
\beta=\frac{1}{2} m\left(X_{i}^{\prime}=\{F\} \mid X_{i}=\{T\}\right)+\frac{1}{2}-\eta=\frac{1}{2}\left(1-p_{i U}\right)+\frac{1}{2}-\eta \\
\gamma=\frac{1}{2} m\left(X_{i}^{\prime}=\{T, F\} \mid X_{i}=\{T\}\right)+\eta=\frac{1}{2}\left(p_{i U}-p_{i L}\right)+\eta
\end{gathered}
$$

BNOR with the above $\alpha, \beta, \gamma$ is called Temperate Belief Noisy-OR (TBNOR) model. It is easy to see that OBNOR, PBNOR and TBNOR are special cases of OCBNOR.

Least Committed Belief Noisy-OR (LC-BNOR), just as the name implies, suggests us that the least committed belief mass function should be selected holding the view that one should never give more belief than justified. It satisfies a form of skepticism, of noncommitment, of conservatism in the allocation of the beliefs ${ }^{37}$. At this time,

$$
\alpha=0, \beta=0, \gamma=1
$$

# 3.3. From Bayesian Networks to Evidential Networks 

In order to apply BNOR structure, it is important to find a relevant model to encode and to propagate the causal relations included in BNOR. Here the evidential network model proposed by Simon and Weber ${ }^{26}$ is taken as a solution to implement BNOR. Similar to BN, evidential networks allow dealing with a lot of variables and modeling the dependencies between variables. From BNOR, the conditional mass distribution

$$
m\left(Y=\{T\} \mid X_{i}\right), \quad m\left(Y=\{F\} \mid X_{i}\right), \quad m\left(Y=\{T, F\} \mid X_{i}\right)
$$

can be established, which plays a similar role as CPTs in Bayesian networks. If the prior belief mass values of the parent nodes $X_{1}, \cdots, X_{n}$ are given, then the junction tree inference algorithm can be evoked to calculate the marginal mass distribution of the child node $Y$. Once the bba of $Y$ is got, the belief and plausibility functions of $Y$ can be obtained accordingly.

### 3.4. The Pignistic probability and decision making

The transferable belief model (TBM) ${ }^{36}$ is an interpretation of the Dempster-Shafer theory of evidence, where beliefs can be held at two levels - credal level and pignistic level. When an agent has to select an optimal action among an exhaustive set of actions, rationality principles lead to the use of a probability measure. Therefore, when a decision has to be made, the bba obtained by BNOR model must be

transformed into a probability measure ${ }^{38}$. One of the most commonly used transformation approaches is Smets method shown in Eq. (16). In our cases, $\Theta=\{T, F\}$. If the following bba is got,

$$
m(X=\{T\})=m_{1}, m(X=\{F\})=m_{2}, m(X=\{\mathrm{T}, \mathrm{~F}\})=m_{3}
$$

we can get the following pignistic probability:

$$
\operatorname{Bet} P(X=T)=m_{1}+\frac{m_{3}}{2}, \quad \operatorname{Bet} P(X=F)=m_{2}+\frac{m_{3}}{2}
$$

If the conditional belief mass functions is obtained,

$$
m(Y=\{T\} \mid X)=m_{1}^{X}, m(Y=\{F\} \mid X)=m_{2}^{X}, m(Y=\{\mathrm{T}, \mathrm{~F}\} \mid X)=m_{3}^{X}
$$

the conditional pignistic probability can be got as follows:

$$
\operatorname{Bet} P(Y=T \mid X)=m_{1}^{X}+\frac{m_{3}^{X}}{2}, \quad \operatorname{Bet} P(Y=F \mid X)=m_{2}^{X}+\frac{m_{3}^{X}}{2}
$$

Example 2. Here we use the example of Alarm System again to illustrate the behavior of different BNOR models and ImNOR. The intervals of the link probabilities of burglar and earthquake are $p_{1} \in(0.6,0.8)$ and $p_{2} \in(0.7,0.9)$ respectively. The prior distribution of $B$ and $E$ are given:

$$
\begin{gathered}
m(B=\{T\})=0.4, m(B=\{F\})=0.6, m(B=\{T, F\})=0 \\
m(E=\{T\})=0.3, m(E=\{F\})=0.6, m(E=\{T, F\})=0.1
\end{gathered}
$$

The corresponding BNOR model is shown in Figure 3. The conditional mass function $m(A \mid B, E)$ based on different BNOR models and ImOR are displayed in Tables 2-4. Figure 4 illustrates the value of $m(A \mid B=\{T\}, E=\{\mathrm{T}, \mathrm{F}\})$ by different schemes. It can be seen that, ImNOR provides a pessimistic decision for $m(A=\{T\} \mid \cdot)$, but an optimistic one for $m(A=\{F\} \mid \cdot)$. This is counter-intuitive as ImNOR holds opposite attitudes towards one event.
![img-2.jpeg](img-2.jpeg)

Fig. 3. The Belief Noisy-OR structure for Alarm System.

From Table 2 we can see, by the use of ImNOR,

$$
m(A=\{F\}|B=\{T\}, E=\{T\})=m(A=\{F\}|B=\{T\}, E=\{T, F\})
$$

but by BNOR,

$$
m(A=\{F\}|B=\{T\}, E=\{T\})<m(A=\{F\}|B=\{T\}, E=\{T, F\})
$$

Eq. (55) fits with our common sense. As soon as we know the earthquake has happened for sure, the less belief should be holding for the proposition the alarm has not gone.

Let the link probability of earthquake be $p_{2} \in(0.7,0.9)$, while the link probability of burglar is set to be $p_{1} \in(\alpha, 0.8)$. When $\alpha \rightarrow 0.8$, the uncertainty on $p_{1}$ becomes less. Consequently the uncertainty on the state of Alarm should also decrease. However, as shown in Figure 5, the values of $m(A=\{T, F\}|B=\{T, F\}, E=\{F\})$ and $m(A=\{T, F\}|B=\{T, F\}, E=\{T, F\})$ by ImNOR remain unchanged although the information for $p_{1}$ becomes more precise. The corresponding results using BNOR show that the belief mass assigned to the uncertainty state of $A$ decreases with the increasing precision of the information on $p_{1}$. Specially, if there is no epistemic uncertainty on $p_{2}$, and the uncertainty on $p_{1}$ declines to $0(\alpha=0.8)$, the belief mass given to $A=\{T, F\}$ also becomes zero (see Figure 5-a).
![img-3.jpeg](img-3.jpeg)
a. $m(A=\{T(F)\}|B=T, E=\{T, F\})$
![img-4.jpeg](img-4.jpeg)
b. $m(A=\{T, F\}|B=T, E=\{T, F\})$

Fig. 4. The different BNOR structures for $m(A \mid B=T, E=\{\mathrm{T}, \mathrm{F}\})$.

![img-5.jpeg](img-5.jpeg)

Fig. 5. The uncertainty of the state of the alarm.

Table 2. The conditional mass distribution for $P(A \mid B=T, E)$ by ImNOR and different BNORs.


Marginal mass $m(A)$ can be obtained by ImNOR and different BNORs, and the results are shown in Table 5 and Figure 6. It is shown that OBNOR provides optimistic results while PBNOR produces a pessimistic one. In order to make a compromise, we can adjust the optimistic coefficient $(\lambda)$. Also the contradiction attitudes of ImNOR can be found here. Thus the BNOR methods are more reasonable and informative.

Using Eqs. (51) and (53), the (conditional) belief mass functions can be transferred to (conditional) pignistic probabilities. The results of

$$
\operatorname{Bet} P(A \mid B=\{T\}, E=\{\mathrm{T}, \mathrm{~F}\})
$$

and $\operatorname{Bet} P(A)$ are displayed in Figure 7. It can be seen that BNOR can provide us

Table 3. The conditional mass distribution for $P(A \mid B=F, E)$ by ImNOR and different BNORs.


Table 4. The conditional mass distribution for $P(A \mid B=\{T, F\} \triangleq \Theta, E)$ by ImNOR and different BNORs.


abundant information for decisions with different special requirements. By comparison, ImNOR is more temperate. This is due to the fact that ImNOR assigns more mass values to the vague state $\{T, F\}$. However, if we want to hold the principle that more belief should be given to the uncertain state, LC-BNOR is a better choice (see Figures 4-b and 6-b).

![img-6.jpeg](img-6.jpeg)

Fig. 6. The different BNOR structures for $m(A)$.

Table 5. The belief mass distribution of the child node $A$.


![img-7.jpeg](img-7.jpeg)

Fig. 7. The (conditional) pignistic probabilities.

# 4. Network reliability analysis

In this section we will discuss the application of BNOR on the problem of network reliability analysis. The definition of network reliability and the traditional Bayesian solution are first recalled. Then the reliability evaluation strategy using BNOR model will be described in detail.

### 4.1. Network reliability and Bayesian network solution

The network reliability considered here is two-terminal reliability, defined as the probability that there is an operative path between source nodes $n_1$ and sink nodes $n_N$ in the network. Nodes are assumed to be operational at all times, and edge failures are assumed to be statistically independent.

Let graph $G(N, E)$ represent a network, where $N$ denotes the set of nodes and $E$ is the set of links. For the network shown in Figure 8-a, $N = \{n_1, n_2, n_3, n_4\}$, $E = \{e_1, e_2, e_3, e_4\}$. Define $|N|$ new variables, $N_i$, $i = 1, 2, \ldots, |N|$, indicating whether the communication between $n_1$ and $n_i$ is successful. Let $N^+(n_i) = \{n_j | < n_j, n_i > \in E\}$, for every element of which sets, $n_j$, there is a path from $n_j$ to $n_i$. And let $E^+(n_i) = \{e_k = < n_j, n_i > |n_j \in N^+(n_i)\}$ denote the sets of edges directed to node $n_i$.

Zhen et al. [39] presented a method for reliability evaluating of networks based on BN. The nodes and edges of BN can be created according to $G(N, E)$:

1. The root nodes of BN are $N_1$ and the edges in $E$.
2. The non-root nodes of BN are $N_i$, $i \neq 1$. And

$$Pa(N_i) = \{N_j |n_j \in N^+(n_i)\} \cup \{e_k |e_k \in E^+(n_i)\} . \tag{56}$$

Bayesian networks' inference algorithms can be evoked then to calculate the network reliability $P(N_s)$. The BN framework for the network described in Figure 8-a can be seen in Figure 8-b.

![img-8.jpeg](img-8.jpeg)

a. Directed network

![img-9.jpeg](img-9.jpeg)

b. BN solution

Fig. 8. An example of directed network and its BN solution.

### 4.2. Reliability evaluation using BNOR

For the network shown in Figure 9, its reliability can be defined by the probability that there is a working path connected from $n_1$ to $n_5$. The network is operating if

the two terminal nodes $n_{1}$ and $n_{5}$ are connected by operational edges. Let $S$ denote the state of the network. It has binary states with $T$ (working) or $F$ (fail). The values for failure rates of each edge are

$$
\lambda_{e_{1}}=\lambda_{e_{3}}=\lambda_{e_{5}}=1.5 * 10^{-3} \mathrm{~h}^{-1}, \lambda_{e_{2}}=\lambda_{e_{4}}=\lambda_{e_{6}}=1.8 * 10^{-3} \mathrm{~h}^{-1}
$$

![img-10.jpeg](img-10.jpeg)

Fig. 9. The network with 5 nodes.

Consider the mission time $t=200 \mathrm{~h}$. The probability distribution of each edge is given in Table 6 .

Table 6. The probability distribution of each edge of the network


The traditional Bayesian network approach is first adopted to calculate the reliability. Using the method described in Section 4.1, we can create a Bayesian network solution model (see Figure 10). By applying the Junction Tree (JT) inference algorithm, we can obtain the exact value of the network reliability $p(S=T)=0.9148$.

In the next two subsections, different BNOR structures (PBNOR, OBNOR, TBNOR, OCBNOR and LC-BNOR) will be applied to estimate the network reliability. The BNOR model for this network is shown in Figure 11. The fail of edge $e_{i}$ can be regarded as an inhibition. For example, in the network displayed in Figure 9, even if $N_{2}$ is in the working state $T, N_{5}$ may not in state $T$ due to the fail of $e_{2}$. The inhibition can be measured by link probabilities $p_{e_{i}}, i=1,2, \cdots, 5$.

![img-11.jpeg](img-11.jpeg)

Fig. 10. The BN network solution.
![img-12.jpeg](img-12.jpeg)

Fig. 11. The BNOR model for network reliability.

# 4.3. BNOR model, case with no epistemic uncertainty 

If there is no epistemic uncertainty, neither on the variable state or on link probabilities, i.e.,

$$
m\left(N_{1}=\{T, F\}\right)=0
$$

and

$$
p_{i L}=p_{i U}=p\left(e_{i}=T\right), i=1,2, \cdots, 6
$$

the same results can be obtained by the use of all BNORs and ImNOR:

$$
m(S=\{T\})=0.9148, m(S=\{F\})=0.0852, m(S=\{T, F\})=0
$$

It can be seen that, if there is no epistemic uncertainty introduced, the reliability estimation results previously obtained by traditional BN method can be recovered. This fact indicates that BNOR is a general extension of Noisy-OR structure in the

framework of belief functions, and it is entirely compatible with the probabilistic solution. The Bel and Pl measures can be obtained by Eqs. (10) and (11) respectively. The following results can be obtained:

$$
\operatorname{Bel}(S=\{T\})=0.9148, p(S=T)=0.9148, \operatorname{Pl}(S=\{T\})=0.9148
$$

# 4.4. BNOR model, case with an epistemic uncertainty 

In this test, the case with some epistemic uncertainty on link probabilities is considered. The lower and upper probability bounds of link probabilities $p_{e_{1}}$ are listed in Table 7. The results by five BNORs and ImNOR are illustrated in Table 8.

Table 7. The probability intervals of the inhibition parameters


In Figures 12-a and 12-b, the results of the evaluation of the network system varying with the optimism coefficient $\lambda$ are demonstrated. It can be found that when $\lambda$ grows from 0 up to 1 , the mass on "the system is working" (i.e., $m(S=\{T\})$ ) increases. On the contrary, $m(S=\{F\})$ decreases. This meets with our common sense of optimistic and pessimistic decisions. However, ImNOR provides opposite attitudes towards $m(S=\{T\})$ and $m(S=\{F\})$. The performance of ImNOR is similar to PBNOR for calculating $m(S=\{T\})$, while similar to OBNOR for calculating $m(S=\{F\})$.

Figure 12-c illustrates that the mass assigned to the uncertain state $\{T, F\}$ by LC-BNOR is larger than that by the other models. This is due to the principle LC-BNOR upholds is that one should never give more support than justified to any subset of the discernment frame.

Let the interval of link probability $p_{e_{1}}$ be $[0.7525,0.8525]$ and the corresponding interval of $p_{e_{2}}$ be $[0.6977,0.6977]-[\alpha,-\alpha]$. The length of the interval, $2 \alpha$, reflects the degree of uncertainty to some extend. Figure 12-d depicts the mass assigned to the uncertain state $m(S=\{T, F\})$ varying with $\alpha$. It can be seen that the uncertainty on system's state increases with the increasing of $\alpha$. LC-BNOR is the most sensitive to uncertainty variation among the six NOR models.

In this case, the credibility and plausibility measures on $S=\{T\}$ are not the same, and they bound the network reliability. For example, if we use OCBNOR $(\lambda=0.6)$, from Table 8 we can see the belief mass assignment of the network state $S$ :

$$
m(S=\{T\})=0.9082, m(S=\{F\})=0.0741, m(S=\{T, F\})=0.0177
$$

The following results can be obtained:

$$
\operatorname{Bel}(S=\{T\})=0.9082, p(S=T)=0.9148, \operatorname{Pl}(S=\{T\})=0.9259
$$

Further decisions can be made based on these uncertainty knowledge.

Table 8. The belief mass distribution of the network system.


![img-13.jpeg](img-13.jpeg)

Fig. 12. The different BNOR structures for $m(S)$.

The information on credal level can be transformed to the pignistic level by Eq. (51) where the decisions can be made more easily. The probability distributions by different models are listed in Table 9. As it can be observed in Figure 13, with

the increasing of $\lambda$, the pignistic probability for $S=T$ increases, on the other hand decreases for $S=F$. For $S=T$, OBNOR gives a upper bound and PBNOR gives a lower bound. While for $S=F$, OBNOR gives a lower bound and PBNOR gives a upper bound. This is in accordance with the optimistic and pessimistic principles. However, the attitude of ImNOR is ambiguous.

Table 9. The probability distribution of the network system.


![img-14.jpeg](img-14.jpeg)

Fig. 13. The different BNOR structures for $\operatorname{Bet} P(S)$.

# 4.5. Discussion 

From the experimental results, it can be concluded that when there is no epistemic uncertainty in the network, BNOR degrades to the traditional Bayesian method. However, if there indeed exists imperfect knowledge, BNOR model can provide us more information in the form of lower bounds (Bel) and upper bounds (Pl). A pessimistic decision can be made according to the Bel value, which provides us the worst value of the network reliability. On the contrary, $P l$ is the maximum degree of belief that can support the connectivity of the network, from which an optimistic decision can be made. These measures are of great value when we have to make a compromise between risks and costs. Also these knowledge on the credal level can be transformed to the pignistic level through Smets method. Then common principles in decision theory such as the minimal expected cost (risk) criterion can be evoked.

# 5. Conclusion 

In this paper, the BNOR model under the framework of belief functions, as an extension of the traditional NOR model, is developed to express several kinds of uncertainty in the independent causal interactions. It is proved that BNOR can be implemented to propagate uncertain information through employing the Bayesian networks tools. In practice, BNOR is more flexible than existing NOR models because it offers a general Bayesian framework that allows us to adopt the exact inference algorithm in their original form without modification, and then by adjusting necessary parameters to obtain results which satisfy the special requirements of engineers. Finally, the application on the reliability evaluation problem of networked systems demonstrates the effectiveness of BNOR model.

BNOR is applicable to systems with binary variables. An extension of BNOR suitable to multi-value variables should be regarded as a future development. Furthermore, the uncertainty on link probabilities may not be given in the form of intervals in practice. How to take advantage of the independence of causal interactions with different types of uncertain knowledge is another considerable problem to be investigated. This paper mainly focuses on theoretical work. Applications of BNOR on more complex situations will be considered in the future.

## Acknowledgments.

This work was supported by the National Natural Science Foundation of China (Nos.61135001, 61403310). The study of the first author in France was supported by the China Scholarship Council.
