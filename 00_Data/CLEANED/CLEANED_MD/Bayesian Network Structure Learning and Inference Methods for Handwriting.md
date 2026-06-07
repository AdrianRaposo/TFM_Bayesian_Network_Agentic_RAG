# Bayesian Network Structure Learning and Inference Methods for Handwriting 

Mukta Puri, Sargur N. Srihari and Yi Tang<br>CEDAR, University at Buffalo, The State University of New York, Buffalo, New York, USA<br>mpuri2@buffalo.edu, srihari@cedar.buffalo.edu, yitang@buffalo.edu


#### Abstract

Forensic analysis of handwriting can benefit from constructing probabilistic models of characteristics specified by Questioned Document (QD) examiners. The task considered is as follows. We are given samples of the word and, together with a set of discrete characteristics. The characteristics are different for cursive writing and for hand-printing. The goal is to construct a model of the probability distribution and to make useful inferences using the model. Since the number of parameters needed for the complete joint distribution is over a million, a Bayesian network (BN) approach is proposed. The goal is to learn the structure of the BN and perform useful inferences. Since the structure learning problem is NP-hard, an approximate method that uses chi-squared tests between pairs of variables is used. Directed edges are included one at a time to minimize log-loss. The learned structure was used to obtain samples using Gibbs sampling and their rarity determined by inferring several probabilities: the joint probability of the formation, the probability of random correspondence (PRC) as a measure of the discriminatory power of the characteristics, conditional PRC associated with a given sample and the probability of finding a similar one within tolerance in a database of given size.


Keywords-Bayesian networks; structure learning; forensics

## I. INTRODUCTION

Forensic handwriting examination, also known as questioned document (QD) examination, is based on the fact that no two persons write the same way while considering the fact that the writing of each person has its own individual characteristics [1], [2]. Based on years of training, QD examiners specify the individualizing characteristics in a given handwritten item. Our goal here is to construct a probabilistic model so that it may be used to quantify the degree of individualization provided by the characteristics.

## II. Characteristics and Problem Complexity

Consider the common English word and. Characteristics for this word given by QD examiners is in Table I for both cursive writing and for hand-printing. The handwritten and has nine characteristics $X=X_{1}, X_{2}, \ldots, X_{9}$ where $X_{i}$ takes up to 5 values for the cursive dataset and 6 values for the handprint dataset. Each sample with a set of characteristics can represent several instances of and. For instance, the three samples of cursive and in the first row in Table II(a) all contain the following feature values: $X_{1}=0 X_{2}=1 X_{3}=$ $1 X_{4}=1 X_{5}=0 X_{6}=2 X_{7}=0 X_{8}=2 X_{9}=2$. The three samples of handprint and in the first row in Table II(d)
all contain the following feature values: $X_{1}=0 X_{2}=0$ $X_{3}=0 X_{4}=0 X_{5}=1 X_{6}=0 X_{7}=0 X_{8}=1 X_{9}=2$.

In the probabilistic formulation each feature is considered to be a random variable. The 9 features each have multinomial distributions with $4,5,3,5,4,4,4,5$ and 3 possible values for cursive data and $5,6,5,5,3,5$, 6,4 , and 3 possible values for handprint data. If we assume that all variables are dependent on every other variable, the number of parameters needed for cursive data is $4 \times 5 \times 3 \times 5 \times 4 \times 4 \times 4 \times 5 \times 3-1=287,999$ and for handprint data is $5 \times 6 \times 5 \times 5 \times 3 \times 5 \times 6 \times 4 \times 3-1=809,999$.

## III. BAYESIAN NETWORKS

The computational complexity and the need for samples can be minimized by exploiting statistical independencies that exist between variables using Probabilistic graphical models [3], [4]. Bayesian Networks (BN) are directed graphical models, where the nodes correspond to variables and edges their dependencies. Lack of edges indicate independencies. BNs are more straight-forward to construct than undirected models known as Markov networks, principally because the latter involve a global partition function while BNs can be factored into local dependencies.

## A. Bayesian Network Structure Leaning (BNSL)

BN structure is learned using Algorithm BNSL which is a variant of one described in [5]. Its performance is compared to the case where all variables are assumed to be independent. The pairwise chi-squared ( $\chi^{2}$ ) test, which yields a measure of independence between two variables, is used to obtain values between all possible pairs of nodes (features) is first calculated using Equation 1 and stored in a set $E_{p}$ in non-increasing order of $\chi^{2}$ statistics.

$$
\chi^{2}(\mathcal{D})=\sum_{i, j} \frac{\left(O\left[x_{i}, y_{j}\right]-E\left[x_{i}, y_{j}\right]\right)^{2}}{E\left[x_{i}, y_{j}\right]}
$$

Starting from a model without any edges but containing all the vertices, $G$, the first pair in $E_{p},\left(v_{i}, v_{j}\right)$ was removed from the set and a new edge $\left(v_{i} \rightarrow v_{j}\right)$ or $\left(v_{j} \rightarrow v_{i}\right)$ was added to $G$ based on which edge increased the log-likelihood value of the model more while creating a directed acyclic graph (DAG). The isDAG function was used to veridy that the newly created graph would not be a DAG. The score for the BN is given by the negative log-likelihood, or the log-loss:

Table I
Characteristics of Handwritten and as Specified by QD Examiners.


(b) Hand-print


Table II
Examples of samples with highest and lowest joint probabilities: (A) Cursive- Highest (B) Cursive- Lowest (C) Handprint- Highest (D) Handprint- Lowest. The samples were obtained by Gibbs sampling of BNs.
![img-0.jpeg](img-0.jpeg)

![img-1.jpeg](img-1.jpeg)

Figure 1. Heuristics of determining Structure in Algorithm BNSL

$$s(\mathcal{D}|G) = -\sum_{i=1}^{N} \sum_{j=1}^{n} \log P(x_{ij}|\text{pa}_{ij}),\tag{2}$$

If either edges do not increase the log-likelihood of the model or do not create a DAG, no edge was added to $G$. This process is repeated until the set $E_p$ became empty.

### Algorithm 1 BNSL

**Input:** set $S = \{v_1, ..., v_n\}$ of $n$ random variables, training data $\mathcal{D}_r$ and validation data $\mathcal{D}_v$

**Output:** Graph $G^* = \{V, E^*\}$

1. Compute pairwise $\chi^2$ statistics, $\chi^2_{(v_i, v_j)}$
2. Construct ordered set $E_p = \{(v_i, v_j) | i \neq j\}$ in descending order of $\chi^2$
3. Set $G^* = \{V, E^*\}$, where $V = S, E^* = \emptyset$
4. Set $k = 1$
5. **Repeat**
6. Pick the first pair $(v_i, v_j)$ from $E_p$
7. Create $G_{c_1} = (V, E_{c_1}), E_{c_1} = E^* + \{v_i \rightarrow v_j\}$
8. Create $G_{c_2} = (V, E_{c_2}), E_{c_2} = E^* + \{v_j \rightarrow v_i\}$
9. Compute $s_{k-1}$, $s_{c_1}$ for $G^*$ and $G_{c_1}$ from $\mathcal{D}_r$
10. If $(s_{c_1} > s_{k-1}) \&\ (\text{isDAG}(G_{c_1}))$
11. Then $G^* = G_{c_1}$
12. Compute $s_{k-1}$, $s_{c_2}$ for $G^*$ and $G_{c_2}$ from $\mathcal{D}_r$
13. If $(s_{c_2} > s_{k-1}) \&\ (\text{isDAG}(G_{c_2}))$
14. Then $G^* = G_{c_2}$
15. Increment $k$ by 1
16. $E_p = E_p - \{(v_i, v_j)\}$
17. **Until** $E_p = \emptyset$
18. **return** $G^*$

Since determining the log-likelihood to determine the addition of each edge takes exponential-time, while constructing the models, only up to two parents per node was considered. As shown in Figure 1(a) and 1(b), if the new node 'b' to be added will become the parent of node 'a', the edge is added to our structure as long as 'a' has no parent or 'a' has only a single parent. As shown in Figure 1(c), if 'a' already has 2 parents 'c' and 'd', the new edge is not added to the graph whether or not it decreases the log loss.

### B. Parameter Estimation

Based on the learnt BN structures the component conditional probability distributions (CPDs) are shown in Figure 2. If we assume all variables are independent, the joint probability is a product of the marginals: $P(X) = \prod_{i=1}^9 X_i$.

The parameters of the models were determined by evaluating the Conditional Probability Tables (CPTs) for only the factors in the joint probability. The CPTs were calculated using maximum likelihood estimates. In order to avoid zero probabilities, or to avoid cases of being divided by zero, additive smoothing was used.

The values of marginal densities calculated are shown in Table III whereas the values of conditional densities calculated are shown in Tables IV and IV.

$$\theta_i = P(X_i) = (n_i X_i) + \alpha / (N + \alpha d),\tag{3}$$

where, $\alpha = 1$ for additive smoothing, and $N$ is the number of independent parameters needed. $N$ is the BN area. The $n_i X_i$ are as follows: $n_i = \frac{1}{N}$ for $X_i$ and $\alpha = 10$ for $\alpha = 1$.

###

Table IV
Conditional Probability Tables of Characteristics FOR CURSIVE WRITING:


(b) $X_{6} \mid X_{2}$


(c) $X_{7} \mid X_{4}$


(d) $X_{3} \mid X_{4}$


(e) $X_{8} \mid X_{6}$


(f) $X_{1} \mid X_{7}$


(g) $X_{5} \mid X_{5}$


Table V
Conditional Probability Tables of Characteristics FOR HANDPRINT WRITING:


(b) $X_{8} \mid X_{6}$


(c) $X_{5} \mid X_{1}$


(d) $X_{4} \mid X_{5}$


Table VI
EVALUATION OF MODELS (LOG LOSS).


solution to structure learning. Also, as the possibility of each node having any number of parents was considered, the complexity of calculating the log-loss while determing the addition of each edge could turn out to be exponential. Also, the log loss of the previous model when compared to that of the independent case was not very low. The new BNSL algorithm that we constructed in this paper tries to overcome these drawbacks.

1) Evaluation of Model Accuracy: The models were evaluated by calculating the log-loss of each model. The logloss is given by negating the log-likelihood given in Equation 2 .

The log-loss values were calculated for both the BN model and the model that assumes all variables are independent as shown in Table VI. For both cases the log loss is higher when all variables are assumed independent indicating that the BN structure is the better model.
2) Evaluation of Model Complexity: In this algorithm, exponential search for each edge is reduced to polynomialtime by exploiting dependency constraints, the chi-squared values, between variables. Also, the exponential complex-

Table III: MARGINAL PROABILITIES OF CHARACTERISTICS:


(b) Handprint


ity of determining log-loss was reduced by considering a maximum of only two parents per node.

## IV. INFERRING RARITY OF SAMPLES FROM MODEL

A number of inference tasks can be done in order to determine the rarity of a given handwriting sample such as the calculation of: joint probability of the sample, PRC or the Probability of Random Correspondence, $n$ PRC, and conditional $n$ PRC [7].

## A. Joint Probability

A higher joint probability of a sample signifies that the sample is more common whereas a lower joint probability signifies that the sample is rare. Hence, the calculation of the joint probability gives a direct relation to the rarity of a sample, or its degree of individualization. The joint probability is estimated using the factorizations in Figure2.

Values of the joint probabilities for several Gibbs samples are in Table II, where samples with the highest and lowest joint probabilities are shown. The rare samples are that have individualizing characteristics.

## B. PRC

PRC is the probability that two independent, identically distributed samples $x$ and $y$ have the same characteristics within a specified tolerance, $\epsilon$. It is given by:

$$
\rho=P(z=1)=\sum_{X} \sum_{Y} P(z=1 \mid X, Y) P(X) P(Y)
$$

Where $P(X)=P(Y)$ is the joint probaility of $X . z$ is an indicator variable such that $P(z=1 \mid X, Y)=1$ if $X=Y \pm \epsilon$ and 0 otherwise. Here, we assume $\epsilon=0$ and evaluate PRC for $X=Y$. However, it is not compulsory for $\epsilon$ to be 0 ; for any value of $\epsilon \neq 0$, the complexity of calculating the PRC becomes exponential and is hence such a case is not considered.
![img-2.jpeg](img-2.jpeg)

Figure 3. $n$ PRC vs $n$ for cursive and handprint datasets. Cursive dataset is more individualistic

Using Equation 4 on the BN model constructed in Section III-A and parameters learned asdescribed in Section III-B, the PRC was evaluated as: (1) Cursive $P R C=7.90 \times 10^{-4}$ (2) Handprint $P R C=6.85 \times 10^{-3}$

This value of PRC can be used to compare the discriminative power of and to those of other letters and combinations.

## C. $n$ PRC

$n$ PRC is the probability that among a set of $n$ samples $y_{1}, y_{2},, y_{n}$ some pair have the same characteristics within a specific tolerance $(\epsilon)$, where $n \geq 2$. The $n$ PRC can be written as:

$$
\rho[n]=1-(1-\rho)^{\frac{n(n-1)}{2}}
$$

The different values of $n$ PRC obtained for different values of $n$ were plotted as shown in Figure 3.

It is observed that the $n$ PRC for both cursive and handprint gradually increases until it reaches 1 . However, the

$n$PRC for the hand-print data seems to increase faster and reach 1 faster than the $n$ PRC for the cursive dataset.

## D. Conditional $n$ PRC

The conditional $n$ PRC finds the probability that in a set of $n$ samples, one sample with a specific value coincides, within tolerance, with another sample. It finds the probability of finding a match in the database. In the case of identical match the conditional nPRC can be shown to be equivalent to the followint equation.

$$
1-\left(1-P\left(X_{s}\right)\right)^{n}
$$

## V. Summary and Discussion

Individualizing characteristics are central to writer identification. We have proposed a method for modeling the probability distribution of a given set of characteristics, so that a small probability of evidence (or high rarity) can be considered as a measure of individualization. It is based on directed graphical models known as Bayesian networks (BNs)- which do not suffer from the severe computational complexity of full joint distributions but work better than the extreme assumption of independent variables. Since BN construction is NP-hard, an approximate algorithm has been proposed and demonstrated with samples of handwritten and.

Samples obtained from the BNs using Gibbs sampling were used to demonstrate several inferences: determining joint probability, PRC, $n$ PRC, and conditional $n$ PRC of the samples. The joint probability gave a direct measure of the rarity; the PRC helped to compare the discriminative power of the given letter combination to those of other letters and combinations; the $n$ PRC gave the probability of finding a pair with the same features in a group of samples; and the conditional $n$ PRC gave the probability of finding a similar sample within tolerance in a database of given size.
