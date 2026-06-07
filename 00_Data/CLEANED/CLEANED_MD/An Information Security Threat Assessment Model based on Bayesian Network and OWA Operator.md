# An Information Security Threat Assessment Model based on Bayesian Network and OWA Operator 

Kehe Wu ${ }^{1, *}$ and Shichao $\mathrm{Ye}^{2, *}$<br>${ }^{1}$ Beijing Engineering Research Center of Electric Information Technology, North China Electric Power University, Changping 102206, Beijing, China<br>${ }^{2}$ Department of Control and Computer Engineering School, North China Electric Power University, Changping 102206, Beijing, China

Received: 17 Apr. 2013, Revised: 18 Aug. 2013, Accepted: 20 Aug. 2013
Published online: 1 Mar. 2014


#### Abstract

Information security threat assessment involves two aspects, namely, technology and management. A great amount of uncertainties exist in the assessment, which cannot be strictly quantized. Thus, the completely objective information security risk assessment is hard to realize. To this end, this research proposed an information security threat assessment model based on Bayesian Network (BN) and OWA operator. Firstly, with the integration of expert knowledge, the conditional probability matrix of reasoning rules in BN was clarified, as a basis of the establishment of information security threat assessment model. Then, with the group-decision method of OWA operator, the subjective judging information of experts on the threat level of target information system was integrated, which was taken as the prior information of the threat level of target information system. Meanwhile, with the observation nodes of objective assessment information, subjective and objective security threat level was integrated, which realized the continuity and accumulation of the security assessment. Finally, the rationality and effectiveness of this model were verified through the simulation example.


Keywords: Information security, Bayesian Network, OWA operator, quantitative assessment

## 1 INTRODUCTION

With the development of computer technology and the Internet, new attacks with pitfalls of system security have been extensively used by illegal intruders and hackers. Moreover, security risks and threats faced by the security of information system have been gradually severed. The security of information system has been a focus among people.

The information security risk assessment is one of the effective methods of addressing the security issues of information system, including fault tree analysis, analytic hierarchy process (AHP) and fuzzy comprehensive evaluation. Such methods have been used by security assessment personnel. Yet, the impact of human factors and administrative management measures on the information system was insufficiently considered so far. Meanwhile, information security threat assessment involves two aspects, namely, technology and management. A great amount of uncertainties exist in the assessment, which cannot be strictly quantized. Thus, the
completely objective information security risk assessment is hard to realize.

In this research, the subjective and objective security assessment information was integrated, and the information security threat assessment model based on Bayesian Network (BN) and OWA operator was established. First of all, the group-decision method based on OWA operator sufficiently uses the experiences and knowledge of each decision makers to assess the target information system. This, to a great extent, makes up the one-sidedness of individual judgment of decision makers; secondly, similar to the neural network, BN can fully depict the reasoning process of human beings. BN-based security assessment can not only quantitatively interpret the process of security assessment, but also reflect the continuity and accumulation of the security assessment. Hence, information security threat assessment model based on BN and OWA operator can sufficiently consider the subjective judging information of each decision-maker but also demonstrate the continuity and

[^0]
[^0]:    * Corresponding author e-mail: epuwkh@126.com, ye_shichao@126.com

accumulation of security assessment. Besides, it improves the confidence level of BN prior information.

## 2 SUBJECTIVE THREAT GROUP DECISION BASED ON OWA OPERATOR

### 2.1 OWA Operator and Its Weight Endowment Method

Definition 1: Given $F: R_{n} \rightarrow R$, there is a n-dimensional weight vector correlated to $F, w_{i} \in[0,1], 1 \leq i \leq n$, and $\sum_{i=1}^{n} w_{i}=1$, to make:

$$
F\left(a_{1}, a_{2}, \ldots, a_{n}\right)=\sum_{i=1}^{n} w_{i} b_{i}
$$

Where $b_{i}$ is the $i$ th maximum factor of the array $\left(a_{1}, a_{2}, \ldots, a_{n}\right)$. Then $F$ is called the n-dimension OWA operator.

OWA operator is a kind of operator lying between the maximum operator and the minimum operator.

When $w=(1,0,0, \ldots, 0)$ :

$$
F\left(a_{1}, a_{2}, \ldots, a_{n}\right)=\max \left(a_{1}, a_{2}, \ldots, a_{n}\right)=b_{1}
$$

OWA operator is equivalent to the "or" operator in fuzzy operation:

When $w=(0,0,0, \ldots, 1)$ :

$$
F\left(a_{1}, a_{2}, \ldots, a_{n}\right)=\min \left(a_{1}, a_{2}, \ldots, a_{n}\right)=b_{n}
$$

OWA operator is equivalent to the "and" operator in fuzzy operator:

When $w=(1 / n, 1 / n, 1 / n, \ldots, 1 / n)$ :

$$
F\left(a_{1}, a_{2}, \ldots, a_{n}\right)=\frac{1}{n} \sum_{i=1}^{n} a_{i}
$$

OWA operator is equivalent to the arithmetic average operator.

The identification of weight vector of OWA operator is directly related to the size of the data set. In order to ensure the fairness and reasonableness of the decision results, this research discretized the Gaussian distribution to clarify the weight vector of position. In this method, the discretion value was ranked in a position with a relatively small weighted value, which efficiently eliminated the adverse effects of emotional factors on the decision-making process.

Set $\mu$ is the mathematical expectation of $(1,2, \ldots, n)$ endowed with the weight vector $w=(1 / n, 1 / n, \ldots, 1 / n)$; $\sigma$ is the standard deviation of $(1,2, \ldots, n)$ in $\mu$ and weight
vector $w$, thus we have:
$\mu_{n}=\frac{1}{n} \frac{n(n+1)}{2}=\frac{n+1}{2}$
$\sigma_{n}=\sqrt{\frac{1}{n} \sum_{i=1}^{n}\left(i-\mu_{n}\right)^{2}}$
$\omega^{\prime}=\frac{1}{\sqrt{2 \pi \sigma_{n}}} e^{-\frac{\left(i-\mu_{n}\right)^{2}}{2 \sigma_{n}^{2}}}$
$\omega=\frac{\omega^{\prime}}{\sum_{i=1}^{n} \omega^{\prime}}$

### 2.2 Group decision making subjective judgments threat based on OWA operator

For the evaluation of n information systems, The set of decision-making groups is $D=\left(d_{1}, d_{2}, \ldots, d_{n}\right)$, where $d_{k}(k=1,2, \ldots, m)$ represents the K-th decision makers, subjective judgment given in the form of decision are: the Utility value is $u^{(k)}=\left(u_{1}^{k}, u_{2}^{k}, \ldots, u_{n}^{k}\right)^{T}$, the fuzzy language evaluation value is $S=\left(s_{0}, s_{1}, \ldots, s_{T}\right)$,the fuzzy complementary judgment matrix is $p_{(k)}=\left(p_{i j}^{(k)}\right)_{n \times n}$, Therefore, the information consistent with these judgments into utility value is:

1) fuzzy complementary judgment matrix into utility values:

$$
u_{i}^{(k)}=\left(\sum_{j=1}^{n} p_{i j}^{(k)}+\frac{n}{2}-1\right) / n(n-1), i=1,2, \ldots, n
$$

2) evaluation value into fuzzy linguistic approach utility value:

We can make the fuzzy language evaluation value $c$ as described in natural language corresponding to a utility value. For example,
$S=\left\{s_{0}=\right.$ level $\left._{1}=0, s_{1}=\right.$ level $\left._{2}=0.1, s_{2}=\right.$ level $\left._{3}=0.3\right.$,
$s_{3}=$ level $_{4}=0.5, s_{4}=$ level $_{5}=0.7, s_{5}=$ level $_{6}=0.9$,
$\left.s_{6}=\right)$ level $_{7}=1\}$
Thus,the utility value is converted to the formula is:

$$
u_{i}^{(k)}=\sum_{i}^{n(k)} / \sum_{i=1}^{n} s_{i}^{(k)}, i=1,2, \ldots, n
$$

Assembled using OWA operator making a threat on the target population levels of subjective judgment of the i-th information is:

$$
u_{i}=O W A_{w}\left(u_{i}(1), u_{i}(2), \ldots, u_{i}^{(n)}\right), i=1,2, \ldots, n
$$

Decision-making groups $u=\left(u_{1}, u_{2}, \ldots, u_{n}\right)^{T}$ which is the subjective judgment of the information is:

$$
u_{i}=\sum_{i}^{u_{i}} / \sum_{i=1}^{n}, i=1,2, \ldots, n
$$

## 3 BN and reasoning algorithm

BN is also known as Belief Network, comprising of a series of combinations expressing causal rules. Most communications reasoning algorithm was proposed by Pearl, as a reasoning algorithm that is appropriate for simply connected space BN. In the algorithm of multi-tree communication method, assume at a node $X$, then there are $m$ child nodes $\left(Y_{1}, Y_{2}, \ldots, Y_{n}\right)$ and $n$ father nodes $\left(Z_{1}, Z_{2}, \ldots, Z_{n}\right)$. Assume Bel as a posterior probability distribution, then $\lambda$ is the information of evidence acquired from child nodes $\pi$ and is the information of evidence acquired from father nodes. $M_{X \mid Z}=P(X=x \mid Z=z)$ shows the probability of Event $x$ in the child node $X$ for a father node $Z$ in a situation $z$. As $X$ has discreteness, $\lambda(x)$ and $\pi(x)$ are actually vectors. Its element is related with each discrete value of :
$\lambda(x)=\left[\lambda(X=x), \lambda\left(X=x_{2}\right), \ldots, \lambda\left(X=x_{l}\right)\right]$
$\pi(x)=\left[\pi(X=x), \pi\left(X=x_{2}\right), \ldots, \pi\left(X=x_{l}\right)\right]$
The reasoning algorithm of BN centers on single node. $\lambda$ can be obtained from child node and $\pi$ from father node. After that, Bel, $\lambda$ and $\pi$ at this node were calculated, triggering the updates of adjacent nodes. The renewal process is as follows:

Step 1: renewal of its own posterior probability: $\operatorname{Bel}(x)=\alpha \lambda(x) \pi(x)$ Where $\alpha$ was the normalizing factor, so we have:

$$
\sum \operatorname{Bel}(x)=1, \lambda(x)=\prod \lambda_{\gamma_{j}}(x), \pi(x)=\prod \pi_{z_{i}} M_{X \mid Z}
$$

Step 2: bottom-up renewal:

$$
\lambda_{s}(z)=\lambda(x) M_{X \mid Z}
$$

Step 3: top-down renewal:

$$
\pi_{y}(x)=\alpha \pi(x) \prod_{k \neq j} \lambda_{\gamma_{j}}(x)
$$

## 4 BN-based information security threat assessment model

### 4.1 Analysis of assessment factors that influence information security threat level

Information security incidents originated from external causes (threats) and internal factors (fragility). Through the assessment of threats and fragility of information, the possibility of incidents can be acquired. Meanwhile, the impact of information security incidents is correlated with capital. Thus, the impact can be acquired through the assessment of capital.

Information security risks can be viewed as an influence on capital. To simplify the model, the following factors will only be considered: influence on capital , frequency of threats on capital as well as the fragility $f$ of
![img-0.jpeg](img-0.jpeg)

Fig. 1: The structure of Bayesian Network
![img-1.jpeg](img-1.jpeg)

Fig. 2: An Information Security Threat Assessment Model based on Bayesian Network
capital. The threat level was TL. On this basis, the BN-based information security threat assessment model was established.

States of variables in the model are gathered as follows:

$$
\begin{aligned}
T L & =\{\text { high }, \text { medium }, \text { low }\} \\
C & =\{\text { big }, \text { middle }, \text { small }\} \\
T & =\{\text { high }, \text { medium }, \text { low }\}
\end{aligned}
$$

### 4.2 Establishment of conditional probability matrix of reasoning rules

Conditional probability matrix reflects experts' opinions on causal relationship among the association node in the network, which form the expert knowledge. For example, if TL is high, the possibility of small, medium and large loss of capital is $10 \%, 30 \%$ and $60 \%$ respectively; if TL is medium, possibility of small, medium and large loss of capital is $40 \%, 40 \%$ and $20 \%$; if TL is low, possibility of small, medium and large loss of capital is $60 \%, 30 \%$ and $10 \%$. The interpretation of $t$ and $f$ is similar with the above descriptions, as shown in the following Table.

It should be noted that conditional probability matrix is an expert knowledge, thus showing certain subjectivity. Thus, repeated testing of sample data can be used to properly adjust the matrix so that the credibility of the assessment results can be improved.

Table 1: Inference rules conditional probability matrix.


# 5 Analysis of examples 

The decision-making group comprised of four experts assessed the TL of a target. Assume the target TL was respectively high, medium and low. Threat judging information given by four decision makers is:
$U_{1}=(0.2,0.6,0.2)$
$U_{2}=(0.3,0.3,0.4)$
$U_{3}=(0.07,0.33,0.6)$
$U_{4}=(0.37,0.3,0.33)$
According to the equation, it can be obtained that the OWA operator weight vector is:

$$
w=(0.155,0.345,0.155,0.345)
$$

Then TL assessment value of the decision-making group was:

$$
U=(0.247,0.367,0.387)
$$

After the BN initialization with prior information and conditional probability, the assessment system was fully prepared and put into the waiting state. When the system obtained new assessment information, leaf node of the network was renewed, and triggered the network reasoning. After the renewal of probability distribution of node state of the entire network, the condition of probability distribution of root node state was obtained, and the TL assessment was completed. Assume the probability of the following influential factors was logged in:

$$
\lambda_{c}=[001] \lambda_{t}=[010] \lambda_{f}=[010]
$$

Example 1: Assume there is no prior subjective assessment information of threat from the decision-making group, we set the prior information of $T L$ in an information system as $\pi(T L)$, which reflected the insufficient possibility assessment from information starvation. Thus, it can be considered that each condition was closer. Thus, the assessment results were as shown in the figure. Bel1 indicates the maximal possibility of low threat.

Example 2 Assume that TL is generated from the group-decision method based on OWA operator, and then BN prior information is $\Pi(\mathrm{TL})$. The assessment results were shown in the figure. Bel2 indicates the increase of probability of medium TL. And the probability of the other two levels was decreased. It can be seen that the subjective TL judging information of the decision-making group obviously influenced the assessment results.
![img-2.jpeg](img-2.jpeg)

Fig. 3: Example 1 assessment results
![img-3.jpeg](img-3.jpeg)

Fig. 4: Example 2 assessment results
![img-4.jpeg](img-4.jpeg)

Fig. 5: Example 3 assessment results

Example 3 After a certain period, this information system was assessed again. In this round of assessment, the results of the previous round were taken as the prior information for calculation. At this time, prior information became $\Pi(\mathrm{TL})$. Assume the probability of each influencing factor remain unchanged. Then the results were shown in the figure. In other words, the probability of medium TL continued to increase while the rest kept decreasing.

To sum up, due to different prior information, the results were differed. Common prior information includes two aspects, namely, the prior information that should be

set in the initiation of the algorithm, and the prior information as the results of the previous period in the operation period of algorithm. Results of the previous simulation examples demonstrated that to take the subjective judgment of threat level of target information system from the decision-level group as BN prior information can more efficiently reflect the real TL of the target.

## 6 Conclusion

The traditional information security threat assessment model does not take into account subjective threat judgment information given by decision-makers based on their professional experiences. For the overall assessment model, it was a kind of information loss. In this research, on the basis of systematic analysis of information security threat elements, subjective TL judging information and objective situation information were combined so as to establish the information security threat assessment model based on BN and OWA operator. This model is verified to be more consistent with the actual process of information security assessment, which can relatively reflect the real TL accurately. The algorithmic examples proved the effectiveness of the method, which could provide a new perspective for the assessment of information security threat.

## Acknowledgements

This work was supported by the National Basic Research Program of China (973 Program). The first author acknowledges the financial support by the National Basic Research Program of China (973 Program) from China's Ministry of Science and Technology.The authors are grateful to the anonymous referee for a careful checking of the details and for helpful comments that improved this paper.
