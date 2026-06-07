# Article 

## Research on a Safety Assessment Method for Leakage in a Heavy Oil Gathering Pipeline

Peng Zhang ${ }^{1}$, Xiangsu Chen ${ }^{2, *}$ and Chaohai Fan ${ }^{2}$<br>1 School of Civil Engineering and Mapping, Southwest Petroleum University, Chengdu 610500, China; zp_swpi@sina.com<br>2 Petroleum Engineering School, Southwest Petroleum University, Chengdu 610500, China; 201822000459@stu.swpu.edu.cn<br>* Correspondence: 201721000508@stu.swpu.edu.cn

Received: 4 December 2019; Accepted: 10 February 2020; Published: 13 March 2020


#### Abstract

At present, the number of oil and gas gathering and transportation pipelines is numerous, and leakage accidents occur frequently. Each year, due to pipeline failure, there are immeasurable consequences for people and the environment around the affected pipelines. In order to reduce the risk of leakage accidents in heavy oil gathering pipelines and prevent the occurrence of major spills, it is of great significance to carry out safety assessments of them. However, failure data of these pipelines is seriously deficient and statistical methods used to evaluate pipeline safety are incompatible. Therefore, this paper proposes a risk assessment system for heavy oil gathering pipelines in the absence of failure data. Firstly, a Bayesian network (BN) for the leak safety evaluation of heavy oil gathering pipelines is established via mapping from a bow-tie (BT) model. Then, information diffusion theory is combined with fuzzy set theory to obtain the failure probability of each factor affecting the pipeline failure, and then the failure probability of the pipeline is obtained by the full probability formula. In addition, in order to assess the extent of consequences due to accidents, variable fuzzy set theory is used to comprehensively consider the consequences of the leakage of heavy oil gathering pipelines. Finally, the above two parts are combined to form a safety assessment system to realize risk management and control for pipelines, which is necessary to ensure the safety of heavy oil gathering pipelines.


Keywords: heavy oil gathering pipelines; safety evaluation; absence of failure data; information diffusion theory; variable fuzzy set theory

## 1. Introduction

With the sharp demand for oil and gas consumption, the construction speed of oil and gas gathering and transportation networks is increasing. For oil and gas fields, gathering pipeline networks are usually large and complex [1]. Once a leakage accident occurs, it is very likely to cause casualties, economic losses, and ecological environment damage around the pipeline. It has been proven that the total reserve of heavy oil in the world is about $4 \times 10^{9}$ billion barrels, which is three times the known amount of conventional crude oil resources, thus, more and more attention will be paid to heavy oil exploitation and transportation in the future. However, heavy oil pipes leak more frequently and have higher risk than normal ones because of heated or high temperature transportation. Therefore, carrying out safety assessment for them and reducing the probability of accidents is one of the most important issues in the operation and management of oil and gas fields [2,3].

Safety assessment is a systematic and scientific approach to analyzing risk in industrial systems. In 1992, the Gulf Press of the United States first published the monograph "Pipeline Risk Management Handbook" by W. Kent Muhlbauer, which is the world's first monograph on the risk assessment of oil and gas pipelines. It completely described a risk scoring method and pipeline risk assessment

model [4]. Recently, more and more experts and scholars have begun to realize the need for safety in heavy oil gathering pipelines. A number of methods have been proposed for initial safety assessment, including an analytical hierarchy process (AHP), fuzzy logic [5,6,7] (FL), fault tree analysis [8,9] (FTA), event tree analysis [3] (ETA), and a bow-tie model [10,11,12,13,14,15], and so on.

However, the above methods are slightly insufficient for the safety assessment of heavy oil gathering pipelines, mainly because the results of the assessment are more subjective, or require complete and reliable failure data [16,17,18], where the development status does not match the current safety assessment of heavy oil gathering pipelines. Moreover, research on the consequences of failure have concentrated on certain specific consequences [19,20,21,22,23,24]. However, the types of consequences of pipeline leakage are diverse, and research on a single type of leakage consequence clearly cannot meet the requirements of severity assessment. Therefore, this paper proposes a safety assessment system which consists of two parts, one is the failure possibility research, and the other is a comprehensive evaluation of the leakage consequences.

The following work is carried out in this paper. Information diffusion theory is combined with fuzzy set theory to obtain the failure probability of each factor affecting pipeline fault. Then, the fault probability of the pipeline can be obtained by the full probability formula, and the Bayesian network (BN) is used as the carrier to update the probabilities of nodes. Furthermore, variable fuzzy set theory is used to comprehensively evaluate the consequences of leakage and determine the severity of the consequences. Finally, the above two parts form a safety evaluation system to realize risk management and control of pipelines.

# 2. Methodology for Uncertainty in Risk Analysis 

### 2.1. Bayesian Network

### 2.1.1. Theoretical Basis

The BN has been described as a belief network or probability network [25]. It is a directed acyclic graph structure based on graph theory and probability theory. Here, we let $B=(G, P)=(X, E, P)$, which is used to represent a BN, where $G$ represents a directed acyclic graph of the variable domain, $P$ represents a set of conditional probabilities, and a directed acyclic figure, such as $G=(X, E)$, where $X$ represents a set of random variables and $E$ represents a set of directed edges. For each node $x_{1} \in X$ in the directed acyclic graph $G$, a conditional probability table is assigned. Each edge $e_{1} \in E$ corresponds to an interdependent relationship (Figure 1).
![img-0.jpeg](img-0.jpeg)

Figure 1. A typical 6-node Bayesian network (BN).
where $X=\left\{X_{1}, X_{2}, X_{3}, \cdots, X_{n}\right\}$ is used to represent the set of random variables, $x=\left\{x_{1}, x_{2}, x_{3}, \cdots, x_{n}\right\}$ represents the value of the random variable, and the variable in $X$ corresponds to the nodes in the BN. Here, $E_{1}, E_{2}, E_{3}, E_{4}$, and $E_{5}$ are directed edges. For example, $E_{1}$ is a directed line segment of the $X_{2}$ node pointing to the $X_{1}$ node, indicating the dependency of the $X_{1}$ and $X_{2}$ nodes. Moreover, $X_{2}$ is the parent node of $X_{1}$ and $X_{1}$ is a child node of $X_{2}$. Here, $X_{4}, X_{5}$, and $X_{6}$, having no parent node, are

also called root nodes. Each root node has prior probability, and a non-root node has a conditional probability table for the corresponding parent nodes. The prior probability means that the node has an independent probability of occurrence (Table 1). There are only two possible states, namely, $Y$ (occurs) or $N$ (does not occur), and the probability value in the table indicates the probability that the node is in a different state. The sum of all probability values in each prior probability is 1 . The conditional probability represents the causal relationship between the parent node and the child node. Table 2 shows the probability of the child node variable $X_{1}=f\left(X_{2}, X_{3}\right)$, given the parent node variables $X_{2}$ and $X_{3}$, that is, the conditional probability of the variable $X_{1}$ when its parent nodes $X_{2}$ and $X_{3}$ take each possible value.

Table 1. Marginal probability table.


Table 2. Conditional probability table of node $X_{1}$.


In addition, the BN can describe multiple states of random events. Taking the $X_{1}$ node as an example, the traditional method represented by the failed fault tree can only describe the two states of the event $X_{1}$ node, namely, "occurrence" and "does not happen". However, in engineering practice, the $X_{1}$ node tends to present a variety of states, and a BN can effectively resolve this contradiction, where $X_{1}$ events would be described as "does not happen", "may happen", "certainly occur", and so on. It can be seen from the analysis that the BN has obvious advantages in dealing with the uncertainty problem and can be applied to the problem of constant probability change in the security risk analysis of leakage failure in heavy oil gathering pipelines.

# 2.1.2. Establishment of Bayesian Network 

There are usually two methods for establishing a BN. One is based on expert knowledge and experience, which is efficient, intuitive, and concise. However, a complex BN will result in a situation where the logic is not strict and not considered well. The other method is to convert the corresponding BN through a mapping structure based on logically strong fault tree analysis or event tree analysis. The heavy oil gathering pipeline system, having numerous failure causes, is complicated. Therefore, this research adopts the second method, that is, to establish a logically strong bow-tie (BT) model and then to map it into a BN structure [26].

The transformation of the BT model and BN mainly includes two aspects, namely, graphics conversion and numerical conversion (Figure 2). In the BT model, basic events, the intermediate events, and the top event are respectively represented as the root nodes, along with the child nodes and the leaf node in the equivalent BN, and the security barriers correspond to the security nodes, but the logical relationships between the security nodes, consequence nodes, and leaf node need to be considered. The probability of the basic events is assigned as the prior probability to the corresponding root nodes in the BN, and the conditional probability table is assigned to the intermediate nodes and the leaf node.

![img-1.jpeg](img-1.jpeg)

Figure 2. Bow-tie (BT) model mapped to a BN.

# 2.2. The Idea of Calculating Failure Probability 

The average failure probability of pipeline leakage is often expressed as the number of failures per unit time/total length, which is usually inaccurate. In order to gain more accurate results, a complete failure statistics database is required. China's failure data of heavy oil gathering pipelines are incomplete at present. In order to more accurately express the actual leakage failure probability. This paper proposes a new node-based probability solution. Take Figure 1 as an example. First, we make full use of intermediate node failure data, which are more specific. Then, information diffusion theory is used to improve the accuracy of the average failure probability of the intermediate nodes $\left(X_{2}, X_{3}\right)$. Then, the failure probability of leaf node $\left(X_{1}\right)$ can be determined by BN software. Finally, through the comparison of the failure possibility of the intermediate nodes, caused by the failure of the parent nodes $\left(X_{4}, X_{5}, X_{6}\right)$, fuzzy set theory is used to transform the expert experience into the subjective possibility. Then, the failure probability of the parent nodes can be obtained by the failure probability of the intermediate nodes. The calculation process is shown in Figure 3.
![img-2.jpeg](img-2.jpeg)

Figure 3. Calculation of the node failure probability.

### 2.2.1. The Failure Probability of Intermediate Nodes

Information diffusion theory is used to improve overall distribution accuracy by optimizing the use of small sample information, that is, to transform single-valued samples into set-valued samples and perform set-valued fuzzy processing on these samples.

Here, we assume that the average failure probability values of pipeline corrosion indicators in the past $m$ years are $x_{1}, x_{2}, \ldots, x_{t}$, respectively, and the set of samples recorded as the average failure probability are denoted by $X=\left\{x_{1}, x_{2}, \ldots, x_{j}, \ldots, x_{t}\right\}$, where $m$ is the total number of samples. Here, $U_{i}=\left\{u_{1}, u_{2}, \ldots, u_{i}, \ldots, u_{r}\right\}$ is a subset of information diffusion and each $x_{j}$ within the $X$ set, where $i=$ $1,2, \ldots, r$. The $u_{i}$ value is a discrete real value obtained by discrete spacing at a fixed interval. Any

sample point of $x_{j}$ spreads the entropy information it represents to all points in the average failure probability set $\mathcal{U}_{i}$, and the corresponding diffusion estimation expression is shown in Equation (1):

$$
f_{i}\left(u_{j}\right)=\frac{1}{h \sqrt{2 \pi}} \exp \left[-\frac{\left(x_{i}-u_{j}\right)^{2}}{2 h^{2}}\right]
$$

where $h$ is the information diffusion coefficient, which is determined by the minimum average failure probability $a$, the maximum average failure probability $b$, and the number of leakage average failure probability sample $t$. Its formula is as follows:

$$
h= \begin{cases}0.8146(b-a) & t=5 \\ 0.5690(b-a) & t=6 \\ 0.4560(b-a) & t=7 \\ 0.3860(b-a) & t=8 \\ 0.3362(b-a) & t=9 \\ 0.2986(b-a) & t=10 \\ 2.6851(b-a) /(t-1) & t>11\end{cases}
$$

Remember that $C_{i}=\sum_{j=1}^{r} f_{i}\left(u_{j}\right), i=1,2, \cdots t$, where $C_{i}$ is the total amount of information that the sample $x_{i}$ normally diffuses into the domain, which is and normalized to the following:

$$
\mu_{x_{i}}\left(u_{j}\right)=\frac{f_{i}\left(u_{j}\right)}{C_{i}}, i=1,2, \cdots t ; j=1,2, \cdots r
$$

where $\mu_{x_{i}}\left(u_{j}\right)$ is the normalized information distribution of the average failure probability of the sample $\left(x_{i}\right)$. Here, we let $Q=\sum_{i=1}^{t} \sum_{j=1}^{r} \mu_{x_{i}}\left(u_{j}\right)$, where $Q$ is the sum of the average number of failure probability samples $\left(x_{i}\right)$. Under ideal conditions, $Q=t$, however, because there is a rounding error in the calculation, $Q \approx t$, which is easy to know.

$$
P\left(u_{j}\right)=\frac{\sum_{i=1}^{t} \mu_{x_{i}}\left(u_{j}\right)}{Q}
$$

where $P\left(u_{j}\right)$ is the frequency at which the average failure probability sample falls at $u_{j}$, which can be used as the failure probability value at $u_{j}$, and $P\left(u \geq u_{j}\right)$ is the value of the probability of surpassing $u_{j}$ in the sample.

$$
P\left(u \geq u_{j}\right)=\sum_{k=j}^{r} P\left(u_{k}\right), j=1,2, \cdots, r
$$

Due to the complexity of the gathering pipeline system, it is almost impossible to ensure the absolute safety of the system. In addition, an abnormally high level of safety means that the cost of input is immeasurable. Elucidating how to measure the relationship between the degree of safety and spending is worthy of consideration. To make the calculation result more operable and the evaluation more straightforward, this paper introduces failure probability, $P_{0}$, which represents a certain expected value, indicating the ratio of the allowable over-period probability $P_{a}$ to the maximum over-probability $P_{m}$, and the expression of this is $P_{0}=\beta \times P_{a} / P_{m}$, where $\beta$ is the adjustment factor, $\beta=1$ represents safety assessment of the leakage accident for the first time, and each calculation can be appropriately raised or lowered by the manager according to the last safety assessment. Here, $P_{0}$ can be divided into

five levels. The higher the $P_{0}$ value, the higher the acceptable degree of overtaking probability and that the middle and lower values are acceptable (Figure 4).


Figure 4. Classification standard of intermediate node failure possibility.

# 2.2.2. Fuzzy set theory 

Failure data of the existing sub-nodes and root nodes are obviously insufficient, where neither the information diffusion method nor the statistical method cannot be used to calculate the failure probability. Therefore, it is necessary to combine the experience of experts and field operators to determine the probability of occurrence for child nodes and root nodes. However, when the evaluator expresses an opinion on the evaluation subject, the evaluation results are subjective, and the process of semantic value conversion occurs. It is difficult to ensure that different evaluators express the same inner feelings for the same semantic expression. Thus, fuzzy set theory is introduced to transform the linguistic variables of experts and field operators into certain numerical variables [27,28].

Suppose the fuzzy number on the domain $R$ is $M$. Considering the membership function $\mu_{\bar{M}}$, where $R \in[0,1]$ of $M$, the triangular fuzzy number can be expressed as $M=(l, m, u)$, and its membership function expression is given as follows:

$$
\mu_{\bar{M}}(x)= \begin{cases}0 & y \leq l \\ (y-l) /(m-l) & l \leq y \leq m \\ (u-y) /(u-m) & m \leq y \leq u \\ 0 & y \geq u\end{cases}
$$

In Equation (6), $l, m$, and $u$ represent the lower bound of the triangular fuzzy number, the most likely value and the upper bound, respectively, where $\alpha=m-l, \beta=u-m$. Here, $\alpha, \beta$ are the degree of ambiguity. If $\alpha, \beta<0.5$, the ambiguity is too small. If $\alpha, \beta>1$ the ambiguity is too ambiguous. Usually, $\alpha, \beta \in[0.5,1]$ is more suitable.

- Decision Matrix

Taking the intermediate $X_{2}$ node as an example to solve the prior failure probability of the parent nodes, the failure probability of the parent nodes (root nodes) is represented by $P_{s}$ and $s=1,2$, and 3, represent nodes $X_{3}, X_{4}$, and $X_{5}$, respectively. Three industry experts were selected to evaluate the probability of failure probability. According to the experience and failure data, a fuzzy number $\left(\left(l_{1}, m_{1}, u_{1}\right),\left(l_{2}, m_{2}, u_{2}\right)\right.$, and $\left.\left(l_{3}, m_{3}, u_{3}\right)\right)$ was obtained for the influence of the activity of the child nodes, respectively. The initial triangular fuzzy evaluation table is shown in Table 3.

Table 3. Trigonometric fuzzy evaluation of third-party damage.


The operation method of two triangular fuzzy numbers $M_{1}$ and $M_{2}$ is described in [29], where the three fuzzy numbers of $C_{q s}$ are combined into a fuzzy number according to the rule of $\frac{l_{1}+l_{2}+l_{3}}{3}, \frac{m_{1}+m_{2}+m_{3}}{3}, \frac{u_{1}+u_{2}+u_{3}}{3}$.

- Determine initial likelihood

Through the calculation of Equation (7), the initial probabilities of $C_{1}, C_{2}$, and $C_{3}$ are $D_{c 1}=$ $(0.26,0.45,0.83), D_{c 2}=(0.18,0.33,0.56)$, and $D_{c 3}=(0.14,0.22,0.37)$, respectively.

$$
D_{c q}=\sum_{q=1}^{3} a_{q s} \div \sum_{q=1}^{3} \sum_{s=1}^{3} a_{q s}
$$

- Defuzzification

$$
F\left(D_{c 1} \geq D_{c 2}\right)= \begin{cases}1 & m_{1} \geq m_{2} \\ \frac{l_{2}-u_{1}}{\left(m_{1}-u_{1}\right)-\left(m_{2}-l_{2}\right)} & m_{1} \leq m_{2}, u_{1}>l_{2} \\ 0 & \text { other }\end{cases}
$$

The initial failure probability was defuzzified and then normalized to obtain the operational misoperation, maintenance misoperation, and construction misoperation, which were $0.54,0.35$, and 0.11 , respectively. Then, the failure probability value of all root nodes can be solved step by step.

# 2.2.3. The updating of nodes failure probability in Bayesian Network 

The failure probability of the root nodes, child nodes, intermediate nodes and leaf node of the entire BN can be obtained by the above method. When the data are accumulated to a certain amount, the prior failure probability of nodes can be updated, thereby obtaining posterior probability. The failure probability of the resulting nodes will be closer to the actual situation by updating the failure data, where the updating process is shown in Figure 5.
![img-3.jpeg](img-3.jpeg)

Figure 5. Flow chart of updating the probability of nodes.

Compared with long-distance pipelines, heavy oil gathering pipelines have the characteristics of having long lines, a wide area, many stations, dense pipelines, crossover with each other, and imperfect data records. Li Yarong [30] combined a fuzzy comprehensive evaluation method with the Kent pipeline evaluation method to construct a fuzzy comprehensive evaluation system for risk in natural gas gathering and transportation pipelines, which could evaluate the risk of natural gas gathering pipelines objectively and semi-quantitatively. Qin Chuan [31] used the theory of pre-hazard analysis to establish a pre-hazard analysis table to determine the probability of accidents and the level of accidents in a gathering pipeline. Zeng Xuanwei [32] calculated the failure probability of a gathering pipeline by weighting the failure possibility factors and evaluating the consequence level of pipeline accidents. The above method is slightly insufficient in terms of the safety evaluation of heavy oil gathering and transportation pipelines. There are two main disadvantages, however. On the one hand, the evaluation results are more subjective, while, on the other hand, the data requirements are too high. After analysis, heavy oil gathering pipeline leakage usually has four consequences, namely, casualties, direct economic losses, environmental pollution, and negative social impacts, while an industry norm in China "Production Safety Accident Reporting and Investigation Regulations" only gives the scope of casualties and direct economic losses. If only the casualties and direct economic losses are taken into account, the evaluation of the consequences is one-sided. Environmental pollution and negative social impacts caused by pipeline leakage are also receiving more and more attention. In addition, the consequences of environmental pollution and negative social impacts are ambiguous and cannot be accurately quantified. Secondly, the leakage of previous gathering pipelines indicates different leakage consequences resulting in different impacts for oilfields. At present, the production concept in China is centered on the safety of production, and the benefits and environmental and social impacts are three-fold. Therefore, based on the consideration of personal injury and direct economic loss, this research conforms to the current development theme, increasing the indicators of environmental damage and social influence factors, and applying variable fuzzy set theory to evaluate the consequences of leakage failure of heavy oil gathering pipelines comprehensively.

# 2.3. Assessment of Leakage Consequence Rating 

### 2.3.1. Variable Fuzzy Set Principle

One of the most basic concepts in fuzzy set theory is ambiguity. The degree of membership can express the difference between objective things [33,34], while variable fuzzy set theory describes things by relative membership. The intermediate transition state of the difference is a dynamic description of ambiguity in a precise mathematical language [35].

Suppose that the fuzzy concept A on the domain $Z$ assigns a value of 0 and 1 to the left and right endpoints of the A-dimensional difference intermediate transition segment. Therefore, a continuum with an interval of 0 to 1 is formed on the number axis from 0 to 1 [36]. This is relative to a reference frame for a time-space condition. For any element $z(z \in Z)$ in $Z$, the relative memberships of the object $z$, representing the concept of attraction and repulsion, are denoted by $\mu_{A}(z)$ and $\mu_{A^{c}}(z)$, where $\mu_{A}(z)+\mu_{A^{c}}(z)=1$ and $0 \leq \mu_{A}(z) \leq 1,0 \leq \mu_{A^{c}}(z) \leq 1$.

### 2.3.2. Relative Difference Function Model

Taking environmental damage as an example, we let the interval [a, b] be the fuzzy variable set attraction domain of the leakage effect of the domain Z environment destruction, where $a$ denotes that the environmental damage is light, $b$ denotes that the environmental damage is heavy, and interval [c, d] is the range field containing the upper and lower bounds of [a, b]. It can be seen from the fuzzy set complement algorithm that the intervals [c, a] and [b, d] are the exclusion domains of the fuzzy variable set and that $M$ represents the qualitative change points from $a$ to $b$. We let the relative difference function be $D_{A}(z)=\mu_{A}(z)-\mu_{A^{c}}(z)$, and $z$ is the specific quantitative value of the environmental damage caused by the leakage of the collecting pipeline in a certain year. If $D_{A}(z)>0$, this means that

$z$ falls on the interval $[a, b]$, and, at this point, $z$ is attractive if $D_{A}(z)<0$, which means that $z$ falls on the interval $[\mathrm{c}, \mathrm{a}]$ and $[\mathrm{b}, \mathrm{d}]$, and, at this point, $z$ is repulsive. When things change from attractive to repulsive, they must pass the point of gradual change. The relationship of $z$ between each interval and the mass change point $M$ is shown in Figure 6 below.

![img-4.jpeg](img-4.jpeg)

Figure 6. Positional relationship between points $x, M$, and intervals.
In Figure 6, the endpoints $c$ and $a$ of the interval divide the variable domain of environmental destruction into different sub-intervals. When $x$ falls in different intervals, there will be a corresponding difference in the function model at this time. From the set of complement operations and the definition of relative difference function, we can obtain the following formula:

$$
\mu_{A}(z)=\left[D_{A}(z)+1\right] / 2
$$

When $z$ falls to the left of point $M$, the corresponding relative difference function model is as follows:

$$
\left\{\begin{array}{c}
\mu_{A}(z)=\left[\left(\frac{z-a}{M-a}\right)^{\gamma}+1\right] / 2 ; z \in[a, M] \\
\mu_{A}(z)=\left[1-\left(\frac{z-a}{z-a}\right)^{\gamma}\right] / 2 ; z \in[c, a]
\end{array}\right.
$$

When $z$ falls to the right of point $M$, the corresponding relative difference function model is as follows:

$$
\left\{\begin{array}{c}
\mu_{A}(z)=\left[\left(\frac{z-b}{M-b}\right)^{\gamma}+1\right] / 2 ; z \in[M, b] \\
\mu_{A}(z)=\left[1-\left(\frac{z-b}{d-b}\right)^{\gamma}\right] / 2 ; z \in[b, d]
\end{array}\right.
$$

where $\gamma$ is a non-negative exponent, usually taken as 1 , and satisfies the following conditions: (1) When $z=a$ or $b, \mu_{A}(z)=0.5$; (2) when $z=M, \mu_{A}(z)=1$; (3) when $z=c$ or $d$ when $\mu_{A}(z)=0$; (4) when $\mu_{A}(z)=\mu_{A^{\prime}}(z), D=0.5$.

# 2.3.3. Comprehensive relative membership 

After determining the relative difference function model of the object to be evaluated, the variable fuzzy set comprehensive evaluation model proposed by Chen, S. [37,38] can calculate the comprehensive relative membership degree of the leakage consequence of the $q$-th year to the consequence level $g$ via the following equation:

$$
u_{q g}=\left\{1+\left[\frac{\sum_{q=1}^{w}\left[\omega_{q}\left(1-\mu_{A}\left(z_{s}\right)_{g}\right)\right]^{w}}{\sum_{q=1}^{w}\left[\omega_{i} \mu_{A}\left(z_{s}\right)_{g}\right]^{w}}\right]^{\frac{q}{w}}\right\}^{-1}
$$

where $q$ is the year of the consequence safety assessment, $g$ the consequence level division; $\eta$ is the variable optimization standard parameter; $w$ is the distance parameter; $\omega$ is the weight of failure consequence type; $\eta$ and $w$ have four combinations: (1) $\eta=1, w=1$; (2) $\eta=1, w=2$; (3) $\eta=2, w=1$; (4) $\eta=2, w=2$.

### 2.3.4. Level eigenvalues and comprehensive evaluation

The formula for calculating the level eigenvalue of the $q$-th year to be evaluated is as follows:

$$
H_{q}=(1,2, \cdots, c) \cdot U_{q g}^{T}
$$

where $c$ is the consequence level. The consequence level of this paper is divided into four levels, so $c=$ 4 and $T$ is the transposed matrix. The final comprehensive evaluation result of the $q$-year consequences is calculated according to Equation (14):

$$
\overline{H_{q}}(u)=\sum_{q=1}^{4} H_{q} / 4
$$

When $\overline{H_{q}}(u)$ is greater than the midpoint of the two-level interval, the consequence evaluation takes a larger level, otherwise a smaller consequence level is taken (Table 4).

Table 4. Judgment criteria for the consequences level.


# 3. Case study 

Safety assessment is an important part of integrity management and is the basis for conducting pipeline integrity testing and evaluation. At present, there are more than 9500 kilometers of metal gathering and transportation pipelines in A oilfield, which is located in the northwestern area of China. The gathering and transportation pipelines account for about $80 \%$ of the total length of the pipelines. These pipelines pass through the Gobi Desert, along with passage over railways, highways, national roads, woods, scenic areas, etc., which have complex terrain and present frequent leakage in pipelines.

Up to now, there is no standard for the risk analysis of heavy oil gathering and transportation pipelines in the Chinese A oilfield. According to the national requirements for pipeline integrity, all pipeline safety assessments must be completed within three years. Therefore, it is urgent to combine the regional characteristics of the A oilfield and formulate corresponding safety evaluation methods to guide on-site risk safety evaluation work.

### 3.1. Establishment of BT Model

### 3.1.1. Risk Identification

Risk identification is the most important basic work of safety evaluation. The completeness and accuracy of risk identification is directly related to the consistency between the established evaluation model and the evaluation object and the reliability of the evaluation results. After on-the-spot investigation, the risk sources of the A oilfield gathering pipelines can be divided into the following four aspects:

- Third-party damage The heavy oil gathering pipelines in the A oilfield are staggered vertically and horizontally, and there are more pipelines for parallel or crossing roads. Ground protection devices or protective measures are not in place. Here, the marking piles of pipelines are fewer in number and seriously damaged, where only the text can be distinguished. Moreover, it is generally considered that the linear direction between the wellhead and the metering station is the pipeline direction, which often results in serious construction damage. At last, due to the special geographical environment of the A oilfield, which is sparsely populated, locomotives often ignore the road and randomly shuttle, usually causing pipeline stress or fatigue damage.
- Corrosion Corrosion mainly includes internal corrosion and external corrosion. The medium transported by heavy oil gathering pipelines is generally a multi-phase flow with oil, gas, water, hydrocarbon and solid coexistence. The transport medium has a high degree of mineralization and can easily generate ions. There are also corrosive media such as dissolved oxygen, carbon dioxide, sulfides, and a large number of sulfate-reducing bacteria, along with mud sand, resulting

in fouling, corrosion, and the abrasion of pipelines. On-site investigation of the corrosion causes of heavy oil gathering and transportation pipelines in the A oilfield mainly includes the following aspects: Some working areas have reservoirs, resulting in a high groundwater level, and water content in produced oil is $\sim 85-92 \%$, where some samples have high soil salinity. The transport medium contains more impurities, such as saprophytic bacteria, iron bacteria and sulfate reducing bacteria, etc. Some insulation layers are severely destroyed, and some are directly exposed to the outside, where the maintenance condition of which is not ideal. Moreover, the sulfur content in the produced oil is $0.34 \%$, the acid value is $2.11 \mathrm{mg} \mathrm{KOH} / \mathrm{g}$, and the salt content is 15.93 mg of $\mathrm{NaCl} / \mathrm{L}$.

- Misoperation There are many accessories and auxiliary facilities for heavy oil gathering pipelines, and the operators will make mistakes if they pay little attention to them. In the past accident records, accidental operation has caused pipelines to overpressurize and explode, to date resulting in the death of one staff member and many injuries. In addition, the frequency of regular safety training and job training is also one of the main sources of misoperation.
- Material/Welding/Accessories The construction time of heavy oil gathering pipelines in the A oilfield is relatively long. Due to the welding technology level and the limited welding process at the time of pipeline construction, there is a large number of weld crack defects in the pipelines. With the long-term operation of the pipelines, the defects in initial small weld seams continue to expand and become larger, which brings about great hidden dangers to the safe operation of the pipeline. The quality of welding and maintenance will also directly affect the operating life of the pipelines. In the welding construction process, defects such as wear and dents often occur. If the defects are not discovered in time or are not fixed, they will become weak points of destruction during operation, especially in the later stages of service, where it is easy to induce damage. After on-site investigation, although the pipeline construction has been carried out by units with more than three years of construction experience, it has also been found that some construction misoperation still exists and that inspections are not in place. For example, anti-corrosion layers of different pipelines in the same operation area are very different. After running for many years, some are still intact, while some have already begun to fall off and even be destroyed. Leakage failure caused by weld defects occurs more frequently, which is inferred to be due to the quality of pipe welding construction. In addition, the maintenance situation is also uneven, and some pipeline accessories are exposed to the atmosphere and obviously fall off, but nobody cares.


# 3.1.2. Establishment of BT Model 

The analysis of 3.1.1 examined accidents and the characteristics of heavy oil gathering and transportation pipelines in the A oilfield, such as frequent ground activities and the violation of regulations, etc. According to the characteristics of the types of consequences of leakage failure and the evaluation of the consequences of pipeline leakage in today's society, direct economic losses (pool fires), environmental damage (water pollution and soil pollution), social impacts, and personal injuries (explosions, fires casualties) are considered here. The BT model of the heavy oil gathering pipeline was established as shown in Figure 7.

![img-5.jpeg](img-5.jpeg)

Figure 7. BT model diagram of heavy oil gathering pipeline.
The specific event descriptions in the BT model are shown in Table 5.
Table 5. Descriptions of root nodes in the BT model.


# 3.1.3. Conversion of BT model and BN 

From the conversion method of BN introduced in Section 2.1.2, the BN for the safety evaluation of heavy oil gathering pipelines can be obtained from the BT model (Figure 8).

![img-6.jpeg](img-6.jpeg)

Figure 8. The BN of safety evaluation of heavy oil gathering pipelines.

# 3.2. Failure Probability Calculation of Intermediate Nodes 

The leakage data of the gathering pipelines in the A oilfield of Northwest China from 2011-2016 is given in Table 6.

Table 6. Time-dependent variation of leakage times of gathering pipelines due to different reasons.


The outcome of intermediate nodes, such as corrosion, third-party damage, misoperation, and material/weld/pipe accessories was given by the formula of average failure probability and the results are shown in Table 7.

Table 7. Failure probability of intermediate nodes.


Taking third-party damage as an example to calculate the failure probability by using information diffusion theory, the minimum average probability of failure in the observed sample is 0.0269 , and the maximum value is 0.0560 . Therefore, the domain can be set to $[0.024,0.0600]$ and the dispersion is

$\{0.0240,0.0280,0.0320,0.0360,0.0400,0.0440,0.0480,0.0520,0.0560,0.0600\}$, with an interval of 0.004 . The information of the above formula ( $\sim 1-5$ ) can be used to obtain the probability of surpassing, that is, the probability of leakage failure under certain expected values. In the same way, the probability of leakage failure of the misoperation, corrosion and material/welding/pipe accessories at a certain expected value is $0.0400,0.0004,0.0005,0.0125$, respectively.

# 3.3. Solution of the Leaf Node and Root Nodes' Probability 

According to the failure data, the objective failure probability of the intermediate nodes can be obtained by information diffusion theory. Then, to obtain the subjective failure probability, fuzzy set theory is used for the failure data. Finally, the subjective failure probability and the objective failure probability can be used comprehensively to derive the root nodes' failure probabilities. The probability of a priori failure of all root nodes and the failure probability rankings are shown in Table 8.

Table 8. Prior failure probability of root nodes.


As can be seen from Section 2.1.1, a BN inference requires solving the a priori failure probability of the parent node by setting the conditional probability of the child node firstly, and then realizing the

probability estimation of the leaf node in the BN. The prior failure probabilities of corrosion, third-party damage, misoperation, and material/welding/pipeline accessory are $0.0400,0.0004,0.0005$, and 0.0125 , respectively, and the leaf node leakage probability is 0.065 times/(km$\cdot$year). At present, there are several more comprehensive failure databases in the world, including the European EGIG (European Natural Gas Pipeline Incident Data Organization) database, the US PHMSA (Pipeline and Hazardous Materials Safety Administration) database, and the Canadian EUB (Albert Energy and Utilities Commission) database. The probability of leakage failures derived from their failure data is approximately $1.4 \times 10^{-3}$, $4.19 \times 10^{-3}$, and $1.1 \times 10^{-2}$ times / (km$\cdot$year), respectively [39]. Because most of the transport media in the gathering pipelines is untreated or coarsely treated, the failure probability of them is higher than that of long-distance pipelines. Obviously, we can still see the gap between China and developed countries in terms of pipeline safety. There is still a long way to go in terms of mitigating leakage risk, and continuous measures need to be taken to reduce the probability of pipeline leakage.

# 3.4. Analysis of Failure Consequences of Heavy Oil Gathering Pipeline 

Establishing a scientific and complete consequence index system is the premise and basis for the safety assessment of the gathering pipeline. According to the characteristics of the types of consequences of the leakage failure and the current development theme, this paper uses the "Production Safety Accident Reporting and Investigation Regulations". In addition to personal injury and direct economic loss, environmental damage and social impact are also considered. The above four types of consequences are classified in Table 9.

Table 9. Standard for the value of leakage consequences of heavy oil gathering pipelines.


Note: The boundary in the table contains the lower bound value and does not contain the upper bound value.

Personal injury and death in Table 2 includes both injuries and deaths. Combined with the operation of the heavy oil gathering pipeline in the A oilfield for many years, the number of deaths caused by leakage is less. In order to get closer to the consequences of personal injury and death caused by leakage, a more stringent classification was set based on the "Production Safety Accident Reporting and Investigation Regulations". In addition, in order to better clarify the meaning of the number of injuries and deaths, the value of the injury was limited to from $0-1$, which is a comprehensive quantitative value of the number of people and the degree of injury, that is, as long as someone is injured, the value is limited to the interval of [0,1], according to the severity of the injury and the number of people. The value of death is greater than 1 . At present, there are no relevant recovery standards for environmental damage caused by oil and gas pipeline leakage, so this paper gives a grade standard according to experience by environmental recovery personnel. The social impact coefficient is manifested by social impacts such as panic caused by leakage and explosion, bad maintenance, and repairs for frequent pipeline leakage, and even social panic. Based on the annual frequency of leakage, we set the received maximum number of leakages to 1 , so the value of the social impact coefficient is $0-1$. The higher the frequency of pipeline leakage every year, the higher the social impact coefficient, which denotes a more serious impact on society.

# 3.4.1. Standard Interval of the Indicator Level 

According to the interval division result of the security level of the consequences in Table 9, the ranking evaluation matrix and the variable interval matrix are $I_{a b}$ and $I_{c d}$, respectively.

$$
I_{a b}=\left(\begin{array}{cccc}
{[0,0.5]} & {[0.5,1]} & {[1,3]} & {[3,10]} \\
{[0,0.1]} & {[0.1,0.5]} & {[0.5,1]} & {[1,3]} \\
{[0,10]} & {[10,50]} & {[50,100]} & {[100,500]} \\
{[0,0.2]} & {[0.2,0.5]} & {[0.5,0.7]} & {[0.7,1]}
\end{array}\right) I_{c d}=\left(\begin{array}{cccc}
{[0,1]} & {[0,3]} & {[0.5,10]} & {[1,10]} \\
{[0,0.5]} & {[0,1]} & {[0.1,3]} & {[0.5,3]} \\
{[0,50]} & {[0,100]} & {[10,500]} & {[50,500]} \\
{[0,0.5]} & {[0,0.7]} & {[0.2,1]} & {[0.5,1]}
\end{array}\right)
$$

Firstly, we determined the point equaling to 1 membership degree in each level interval, and then obtained the matrix $M$ by combining the characteristics of the consequence level interval with the physical meaning of the parameter $M[40]$.

$$
M=\left(\begin{array}{cccc}
0 & 0.75 & 2 & 10 \\
0 & 0.3 & 0.75 & 3 \\
0 & 30 & 75 & 500 \\
0 & 0.35 & 0.6 & 1
\end{array}\right)
$$

The data on the consequences of the 2011-2016 heavy oil gathering pipeline leakage are shown in Table 10.

Table 10. Data on the types of leakage consequences of heavy oil gathering pipelines in the A oilfield.


### 3.4.2. Determination of Comprehensive Membership

From Equations (2) to (3), taking the 2011 data as an example for calculation, the matrix of relative membership degree can be calculated by the combination of the four kinds of consequence type weights $\omega_{i}=(0.39,0.23,0.21,0.17)$, and then brought into Equation (4), where the relative membership matrix $U_{2011 h}$ of each consequence level is as follows:

$$
U_{2011}=\left(\begin{array}{cccc}
0.80 & 0.20 & 0 & 0 \\
0.17 & 0.66 & 0.17 & 0 \\
0.33 & 0.33 & 0.14 & 0.19 \\
0.38 & 0.16 & 0.33 & 0.13
\end{array}\right) U_{2011 h}=\left(\begin{array}{cccc}
0.22 & 0.42 & 0.07 & 0.29 \\
0.30 & 0.45 & 0.08 & 0.17 \\
0.31 & 0.44 & 0.09 & 0.16 \\
0.29 & 0.44 & 0.08 & 0.18
\end{array}\right)
$$

Combined with the Equations (5) to (6), the four combined eigenvalues of the failure consequence level of the heavy oil gathering pipeline in 2011 are $2.786,1.780,1.811$ and 2.096, respectively. Similarly, the combined eigenvalues of 2012-2016 can be calculated (Table 11), and the trend with time here is shown in Figure 9.

Table 11. Level characteristic values of comprehensive evaluation of consequences in 2011-2016.


![img-7.jpeg](img-7.jpeg)

Figure 9. Trend graph of mean of level eigenvalues over time.
The mean level eigenvalues in Table 10 shows that although the consequence levels in 2011-2016 are at level 2 to level 3, it can be clearly seen that the eigenvalue levels show a significant upward trend (Figure 3). The solid line in the figure is the contour line of the annual eigenvalue level connected in chronological order, the dashed line is the trend line of the trend fitting, which is fitted with the equation $y=0.0252 x-48.541$ and the correlation coefficient is 0.9438 . It can be seen from the figure that if the relevant measures are not taken, a major accident phase will be entered, suggesting a major accident in 2025, thus, corresponding measures must to be taken to avoid further consequences.

# 4. Conclusions 

In this paper, the safety evaluation of heavy oil gathering pipeline leakage is carried out, and a corresponding safety evaluation system is proposed. The following conclusions can be drawn: With more complete failure data, as a breakthrough, improved information diffusion theory has been used to correct the failure probability of the previously used statistical methods. Moreover, risk factors lacking failure data have been calculated by fuzzy set theory, then the failure probability of each risk factor has been obtained. In addition, this has been carried out via the comprehensive consideration of the consequences of leakage, adopting variable fuzzy set theory to calculate the consequences for various levels of leakage. In the operation and maintenance of pipelines, corresponding mitigation measures should be taken in combination with the probability of pipeline leakage failure and the severity of the consequences in order to reduce or control risks and avoid greater leakage consequences. While, at present, this article presents no separation between accidents on land and under water because of the lack of accurate data, and, as we know, such accidents can be different in their environmental and economic scale, so it is worth considering this distinction in further research and risk management in the future.

Author Contributions: Conceptualization, X.C. and P.Z.; methodology, P.Z.; software, X.C.; writing—original draft preparation, X.C. and C.F.; scene researching X.C.; writing-review and editing, X.C.; supervision, P.Z. All authors have read and agreed to the published version of the manuscript.
Funding: This research was funded by the National Natural Science Foundation of China, grant number 50974105, and the Research Fund for the Doctoral Program of Higher Education of China, grant number 20105121110003.
Acknowledgments: The authors are grateful to the National Natural Science Foundation of China for their support. The authors also acknowledge the provision of the heavy oil gathering pipeline leakage data and consequence data of the northwestern A oilfield.
Conflicts of Interest: The authors declare no conflict of interest.
