# Article 

## Parameter Learning of Bayesian Network with Multiplicative Synergistic Constraints

Yu Zhang ${ }^{1}$ (D) and Zhiming $\mathrm{Hu}^{2,3, *}$ (D)

## check for updates

Citation: Zhang, Y.; Hu, Z. Parameter Learning of Bayesian Network with Multiplicative Synergistic Constraints. Symmetry 2022, 14, 1469. https://doi.org/10.3390/ sym14071469

Academic Editor: José Carlos
R. Alcantud

Received: 14 June 2022
Accepted: 14 July 2022
Published: 18 July 2022
Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## 0

Copyright: (c) 2022 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 School of Mathematics and Economics, Bigdata Modeling and Intelligent Computing Research Institute, Hubei University of Education, Wuhan 430205, China; yuzhang@nuaa.edu.cn
2 School of Statistics and Mathematics, Zhejiang Gongshang University, Hangzhou 310018, China
3 School of Zhejiang College, Shanghai University of Finance and Economics, Jinhua 321013, China

* Correspondence: z2011159@shufe-zj.edu.cn

Abstract: Learning the conditional probability table (CPT) parameters of Bayesian networks (BNs) is a key challenge in real-world decision support applications, especially when there are limited data available. The traditional approach to this challenge is introducing domain knowledge/expert judgments that are encoded as qualitative parameter constraints. In this paper, we focus on multiplicative synergistic constraints. The negative multiplicative synergy constraint and positive multiplicative synergy constraint in this paper are symmetric. In order to integrate multiplicative synergistic constraints into the learning process of Bayesian Network parameters, we propose four methods to deal with the multiplicative synergistic constraints based on the idea of classical isotonic regression algorithm. The four methods are simulated by using the lawn moist model and Asia network, and we compared them with the maximum likelihood estimation (MLE) algorithm. Simulation results show that the proposed methods are superior to the MLE algorithm in the accuracy of parameter learning, which can improve the results of the MLE algorithm to obtain more accurate estimators of the parameters. The proposed methods can reduce the dependence of parameter learning on expert experiences. Combining these constraint methods with Bayesian estimation can improve the accuracy of parameter learning under small sample conditions.

Keywords: multiplicative synergistic; Bayesian networks; parameter learning; limited data

## 1. Introduction

Bayesian networks (BNs) can model probabilistic dependent relationships among variables in many real world problems. Therefore, they have become very popular in the artificial intelligence (AI) field over the last two decades. BNs have become a powerful tool with many applications such as medical diagnosis, financial analysis, bioinformatics, medical diagnosis, financial analysis, bioinformatics and industrial applications [1], target tracking [2], robot control [3], gene analysis [4], ecosystem modeling [5], signal processing [6], and educational measurement [7]. A BN model consists of a network structure and a set of conditional probability tables (CPTs). This paper focuses on the parameter learning of discrete BNs when the structure is known.

In practice, when performing parameter learning, we need sufficient samples. If we have sufficient data, BNs can be easily constructed using traditional methods such as the maximum likelihood (ML) method [8]. However, the ML method is difficult to obtain accurate parameters when the data is insufficient, and thus it is difficult to give the right decision [9]. It is very difficult to collect abundant data under certain circumstances, such as, in the cases of earthquake prediction [10], parole assessment [11], and rare disease diagnosis [12]. Thus, the data are not sufficient in many cases, which may lead to inaccurate structure and parameters of a BN. Therefore, many scholars began to pay attention to the parameter learning problems of BNs under the condition of small data sets, and proposed some algorithms to solve these problems.

Altendorf et al. [13] converted the qualitative influence constraints to penalty function and gave the objective optimization function combined with the ML function, and then applied the gradient method to solve it. Feelders and Linda [14] converted qualitative influence constraints to order constraints and applied isotonic regression algorithm to adjust the size of parameters so that the parameters satisfy order constraints. Cassio and Ji [15] converted monotonic constraints to penalty function and applied a convex optimization algorithm to solve the objective optimization function. Ren et al. [16] transformed interval constraints into beta distribution to constrain priori parameters, and combined Bayesian estimation to obtain the parameters. Niculescu [17] studied some equality constraints such as normative constraint and proportional constraint by introducing Lagrange multiplier. Rui [18] used Monte Carlo sampling method to extract virtual data from non-monotonic constraints space, and then used virtual data to construct prior distribution. Finally, Bayesian estimation was used to combine prior distribution with real data to obtain the parameters of BNs. Kobra [19] proposed a multi-experts parameter learning framework to fuse multiple experts' knowledge. In addition to the above methods based on constraints, some scholars proposed the parameter learning methods of BN based on the minimum free energy (see [20]) and Noisy- or -Gates (see [21]). Zhou et al. [22] studied a class of constraints that is naturally encoded in the edges of BNs with monotonic influences. Gao et al. [23] developed "MiniMax Fitness" algorithm to address the problem that imposing prior distributions can reduce the fitness between parameters and data. For more studies on BNs, one can refer to [24-27].

It is found that the main idea of the algorithms is to introduce expert experiences or domain knowledge into the parameter learning process of BNs with some constraints in existing literature. However, the constraints involved in the existing literature are mainly network parameters under the condition of single parent node, and the constraints under the synergistic condition of multiple parent nodes are rarely studied, and the methods involved are relatively complex. There are many constraints under the condition of multiple parents nodes such as additive synergy, multiplicative synergy (see [28]), etc. In this paper, isotonic regression is used to study the parameter learning of BNs under multiplicative synergistic constrains. The proposed methods can reduce the dependence of parameter learning on expert experiences. Combining these constraint methods with Bayesian estimation can improve the accuracy of parameter learning under small sample conditions.

The reminder of this paper is organized as follows. In Section 2, we briefly review some basic theories of BNs and parameter learning. In Section 3, the classical isotonic regression algorithm is introduced. In Section 4, we provide the parameter learning algorithms of this paper under multiplicative synergistic constrains by referring to the idea of pool adjacent violators (PAV) algorithm. In Section 5, the effectiveness and performance of four mentioned algorithms are verified by simulations. In Section 6, some conclusions are given.

# 2. Preliminaries 

In this section, some concepts of Bayesian networks will be briefly reviewed, so that one can understand the paper well.

### 2.1. Bayesian Networks

Bayesian networks are represented as a directed acyclic graph that contains some nodes and edges. Nodes represent random variables, while edges represent the probabilistic relationship between random variables. For each variable node $X_{i}$, a conditional probability table is specified as $P\left(X_{i} \mid \pi\left(X_{i}\right)\right)$, which describes the probability over the possible values of $X_{i}$ and possible configurations of parent variables $\pi\left(X_{i}\right)$. In a BN, the joint probability can be written as follows:

$$
P\left(X_{1}, \cdots, X_{n}\right)=\prod_{i=1}^{n} P\left(X_{i} \mid \pi\left(X_{i}\right)\right)
$$

To illustrate the BNs more clearly, the lawn moist BN is employed, which is depicted as Figure 1, where " 1 " stands for "Cloudy", " 2 " stands for "Rain", " 3 " stands for "Sprinkle", and " 4 " stands for "Wet". The model will be used as the experimental model later. The variables in the network are binary, the value is 0 or 1 , that is, if the event occurs or is present, it has the state 1 . Our purpose is to learn the estimators of parameters in the following BN.
![img-0.jpeg](img-0.jpeg)

Figure 1. Lawn moist model.

# 2.2. Maximum Likelihood Estimation 

Maximum likelihood estimation is an important method for parameters learning of BN. The MLE of the parameters is

$$
\theta_{i j k}^{*}= \begin{cases}\frac{m_{i j l}}{m_{i j k}} & \sum_{k=1}^{r_{i}} m_{i j k}>0 \\ \frac{1}{r_{i}} & \sum_{k=1}^{r_{i}} m_{i j k}=0\end{cases}
$$

where $i$ is the index of node $X_{i}, j$ is the index of parent nodes' configuration, $k$ is $X_{i}^{\prime} s$ states, $r_{i}$ is the number of the states of $X_{i}$, and $m_{i j k}$ is the number of cases that satisfy $X_{i}=k$ and $\pi\left(X_{i}\right)=j$ in the data set (see [1]).

## 3. Isotonic Regression

We know that the variables satisfy order relation, but the order obtained by observation or counting does not satisfy the known order relation, then the data will be adjusted by the weighted average method. This is the problem to be solved by the isotonic regression. Let $u_{1}, u_{2} \ldots, u_{k}$ be a set of variables, $u_{1} \leq u_{2} \leq \ldots \leq u_{k}$, and $u^{\prime}{ }_{1}, u^{\prime}{ }_{2} \ldots, u^{\prime}{ }_{k}$ are estimators. The process of using pool adjacent violators (PAV) algorithm to isotonic regression is as follows:
Step 1: Start with $u^{\prime}{ }_{1}$, and compare $u^{\prime}{ }_{1}, u^{\prime}{ }_{2} \ldots, u^{\prime}{ }_{k}$ in pairs, if $u_{i} \leq u_{i+1}$, there is no adjusment, if $u_{i}<u_{i+1}<\ldots<u_{i+j},(1 \leq j \leq k-i)$, let

$$
u_{i+1}=u_{i+2}=\ldots=u_{i+j}=\frac{1}{j+1} \sum_{m=0}^{i} u_{i+m}^{\prime}
$$

and so on.
Step 2: If $u^{\prime}{ }_{1}, u^{\prime}{ }_{2} \ldots, u^{\prime}{ }_{k}$ do not satisfy the size relationship of variables in step 1, repeat the process in step 1 from $u^{\prime}{ }_{1}$. Thus, the values of $u^{\prime}{ }_{1}, u^{\prime}{ }_{2} \ldots, u^{\prime}{ }_{k}$ adjusted by PAV algorithm can be obtained.

The uniqueness of the solution of isotonic regression has been verified (see [29]) and the solutions obtained by the above process that satisfying the order relation of $u_{1} \leq u_{2} \leq \ldots \leq u_{k}$ are unique.

# 4. Parameter Learning of BNs under Multiplicative Synergistic Constraints 

### 4.1. The Model of Multiplicative Synergistic

Multiplicative synergy constraints describe the synergy size relationship of parameters among three node variables. Let $A, B$ and $C$ be the three variables in the BNs, and all of them are discrete binary variables. Suppose that $A$ and $B$ are the parent nodes of $C$, then the negative multiplicative synergy constraint of $A$ and $B$ to $C$ can be expressed as:

$$
P(c \mid a, b) \cdot P(c \mid \bar{a}, \bar{b}) \leq P(c \mid \bar{a}, b) \cdot P(c \mid a, \bar{b})
$$

Similarly, positive multiplicative synergy constraint can be expressed as:

$$
P(c \mid a, b) \cdot P(c \mid \bar{a}, \bar{b}) \geq P(c \mid \bar{a}, b) \cdot P(c \mid a, \bar{b})
$$

### 4.2. Description of Algorithm

Under the condition of small data sets, if the variables $A, B$ and $C$ in the network conform to the above multiplicative synergy constraint, how to apply this constraint and combine the small data sets to limit the Bayesian network parameter learning and get more accurate results is very important.

The algorithm steps adopted in this paper are as follows:
Step 1: Using the existing small data sets and by the maximum likelihood estimation algorithm to get relevant parameters.
Step 2: For the structural part of multiple parent nodes, judge whether the parameters of this part meet the multiplicative synergy constraint. If they meet, conform to step 5, otherwise conform to step 3.
Step 3: Take the left and right sides of multiplicative synergy constraint as a whole, and use the idea of "averaging" of PAV algorithm to modify them, respectively.
Step 4: Adjust the whole (product of parameters) in step 3, and then modify each parameter. Step 5: Obtain the final parameter learning result.

Steps 3 and 4 are the focus of the algorithm, which are described in detail below. By referring to the idea of PAV algorithm, this paper proposes four different methods to complete the order preserving of parameters and the contents mentioned in steps 3 and 4. Taking the negative multiplicative synergy constraint mentioned in Section 4.1 as an example, the following specific calculation methods are given successively. Parameters order preserving under the condition of positive multiplicative synergy can be obtained in a similar way. The proposed four methods are as follows:

## Method 1

$$
\begin{gathered}
\text { mean }=(P(c \mid a, b) \cdot P(c \mid \bar{a}, \bar{b})+P(c \mid \bar{a}, b) \cdot P(c \mid a, \bar{b})) / 2 \\
d=|\operatorname{mean}-P(c \mid a, b) \cdot P(c \mid \bar{a}, \bar{b})| \\
P(c \mid a, b)^{\prime}=P(c \mid a, b)-d / 2 \\
P(c \mid \bar{a}, \bar{b})^{\prime}=P(c \mid \bar{a}, \bar{b})-d / 2 \\
P(c \mid \bar{a}, b)^{\prime}=P(c \mid \bar{a}, b)+d / 2 \\
P(c \mid a, \bar{b})^{\prime}=P(c \mid a, \bar{b})+d / 2
\end{gathered}
$$

## Method 2

$$
\begin{gathered}
\text { mean }=\frac{\left(\left(N_{1} \cdot N_{4}\right) \cdot(P(c \mid a, b) \cdot P(c \mid \bar{a}, \bar{b}))+\left(N_{2} \cdot N_{3}\right) \cdot(P(c \mid \bar{a}, b) \cdot P(c \mid a, \bar{b})))\right)}{N_{1} \cdot N_{2} \cdot N_{3} \cdot N_{4}} \\
d=|\operatorname{mean}-P(c \mid a, b) \cdot P(c \mid \bar{a}, \bar{b})|
\end{gathered}
$$

$$
\begin{aligned}
P(c \mid a, b)^{\prime} & =P(c \mid a, b)-d \cdot N_{1} /\left(N_{1} \cdot N_{4}\right) \\
P(c \mid \bar{a}, \bar{b})^{\prime} & =P(c \mid \bar{a}, \bar{b})-d \cdot N_{4} /\left(N_{1} \cdot N_{4}\right) \\
P(c \mid \bar{a}, b)^{\prime} & =P(c \mid \bar{a}, b)+d \cdot N_{2} /\left(N_{2} \cdot N_{3}\right) \\
P(c \mid a, \bar{b})^{\prime} & =P(c \mid a, \bar{b})+d \cdot N_{3} /\left(N_{2} \cdot N_{3}\right)
\end{aligned}
$$

# Method 3 

$$
\begin{gathered}
\text { mean }=(P(c \mid a, b) \cdot P(c \mid \bar{a}, \bar{b})+P(c \mid \bar{a}, b) \cdot P(c \mid a, \bar{b})) / 2 \\
d=|\operatorname{mean}-P(c \mid a, b) \cdot P(c \mid \bar{a}, \bar{b})| \\
P(c \mid a, b)^{\prime}=P(c \mid a, b)-d \cdot N_{1} /\left(N_{1} \cdot N_{4}\right) \\
P(c \mid \bar{a}, \bar{b})^{\prime}=P(c \mid \bar{a}, \bar{b})-d \cdot N_{4} /\left(N_{1} \cdot N_{4}\right) \\
P(c \mid \bar{a}, b)^{\prime}=P(c \mid \bar{a}, b)+d \cdot N_{2} /\left(N_{2} \cdot N_{3}\right) \\
P(c \mid a, \bar{b})^{\prime}=P(c \mid a, \bar{b})+d \cdot N_{3} /\left(N_{2} \cdot N_{3}\right)
\end{gathered}
$$

## Method 4

$$
\begin{gathered}
\text { mean }=\frac{\left(\left(N_{1} \cdot N_{4}\right) \cdot(P(c \mid a, b) \cdot P(c \mid \bar{a}, \bar{b}))+\left(N_{2} \cdot N_{3}\right) \cdot(P(c \mid \bar{a}, b) \cdot P(c \mid a, \bar{b})))\right)}{N_{1} \cdot N_{2} \cdot N_{3} \cdot N_{4}} \\
d=|\text { mean }-P(c \mid a, b) \cdot P(c \mid \bar{a}, \bar{b})| \\
P(c \mid a, b)^{\prime}=P(c \mid a, b)-d / 2 \\
P(c \mid \bar{a}, \bar{b})^{\prime}=P(c \mid \bar{a}, \bar{b})-d / 2 \\
P(c \mid \bar{a}, b)^{\prime}=P(c \mid \bar{a}, b)+d / 2 \\
P(c \mid a, \bar{b})^{\prime}=P(c \mid a, \bar{b})+d / 2
\end{gathered}
$$

where $N_{1}$ stands for the sample size when the state of parent nodes is $(a, b), N_{2}$ stands for the sample size when the state of parent nodes is $(\bar{a}, b), N_{3}$ stands for the sample size when the state of parents node is $(a, \bar{b})$, and $N_{4}$ stands for the sample size when the state of parent nodes is $(\bar{a}, \bar{b})$.

The algorithms obtained from Methods 1 to 4 are convergent, and we can obtain the theorem as follows:

Theorem 1. Let $p_{01} \cdot p_{04}>p_{02} \cdot p_{03}$, then there exists $k$ such that.

$$
p_{k 1} \cdot p_{k 4} \leq p_{k 2} \cdot p_{k 3}
$$

after $k$ steps adjustment as Method 1, where $p_{1}=P(c \mid a, b), p_{2}=P(c \mid \bar{a}, b), p_{3}=P(c \mid a, \bar{b})$, $p_{4}=P(c \mid \bar{a}, \bar{b}), p_{k i}$ represents the value of $p_{i}(i=1,2,3,4)$ after the adjustment of $k$ steps, $m_{k}=\left|p_{k 1} \cdot p_{k 4}-p_{k 2} \cdot p_{k 3}\right| / 2$, and $d_{k}=\left|m_{k}-p_{k 1} \cdot p_{k 4}\right|$.

Proof of Theorem 1. Without loss of generality, we only prove the case of Method 1, as the proof of the other three cases is analogous.

Proving $p_{k 1} \cdot p_{k 4} \leq p_{k 2} \cdot p_{k 3}$ is to show that

$$
p_{k 1} \cdot p_{k 4}-p_{k 2} \cdot p_{k 3} \leq 0
$$

$p_{k 1}=p_{k-1,1}-d_{k-1} / 2, p_{k 4}=p_{k-1,4}-d_{k-1} / 2, p_{k 2}=p_{k-1,2}+d_{k-1} / 2, p_{k 3}=p_{k-1,3}+d_{k-1} / 2$, then

$$
\begin{aligned}
& p_{k 1} \cdot p_{k 4}-p_{k 2} \cdot p_{k 3} \\
& =\left(p_{k-1,1}-d_{k-1} / 2\right)\left(p_{k-1,4}-d_{k-1} / 2\right)-\left(p_{k-1,2}+d_{k-1} / 2\right)\left(p_{k-1,3}+d_{k-1} / 2\right) \\
& =p_{k-1,1} \cdot p_{k-1,4}-p_{k-1,2} \cdot p_{k-1,3}-\frac{d_{k-1}}{2}\left(p_{k-1,1}+p_{k-1,4}+p_{k-1,2}+p_{k-1,3}\right) \\
& =\left(p_{k-2,1}-d_{k-2} / 2\right)\left(p_{k-2,4}-d_{k-2} / 2\right)-\left(p_{k-2,2}+d_{k-2} / 2\right)\left(p_{k-2,3}+d_{k-2} / 2\right) \\
& -\frac{d_{k-1}}{2}\left(p_{k-2,1}-\frac{d_{k-2}}{2}+p_{k-2,4}-\frac{d_{k-2}}{2}+p_{k-2,2}+\frac{d_{k-2}}{2}+p_{k-2,3}+\frac{d_{k-2}}{2}\right) \\
& =p_{k-2,1} \cdot p_{k-2,4}-p_{k-2,2} \cdot p_{k-2,3}-\frac{d_{k-2}}{2}\left(p_{k-2,1}+p_{k-2,4}+p_{k-2,2}+p_{k-2,3}\right) \\
& -\frac{d_{k-1}}{2}\left(p_{k-2,1}+p_{k-2,4}+p_{k-2,2}+p_{k-2,3}\right) \\
& =p_{k-2,1} \cdot p_{k-2,4}-p_{k-2,2} \cdot p_{k-2,3}-\frac{d_{k-2}+d_{k-1}}{2}\left(p_{k-2,1}+p_{k-2,4}+p_{k-2,2}+p_{k-2,3}\right) \\
& =p_{k-3,1} \cdot p_{k-3,4}-p_{k-3,2} \cdot p_{k-3,3}-\frac{d_{k-3}+d_{k-2}+d_{k-1}}{2}\left(p_{k-3,1}+p_{k-3,4}+p_{k-3,2}+p_{k-3,3}\right) \\
& =\cdots \cdots \\
& =p_{11} \cdot p_{14}-p_{12} \cdot p_{13}-\frac{d_{1}+d_{2}+\cdots+d_{k-1}}{2}\left(p_{11}+p_{14}+p_{12}+p_{13}\right) \\
& =p_{01} \cdot p_{04}-p_{02} \cdot p_{03}-\frac{d_{0}+d_{1}+\cdots+d_{k-1}}{2}\left(p_{01}+p_{04}+p_{02}+p_{03}\right) \\
& =p_{01} \cdot p_{04}-p_{02} \cdot p_{03}-\frac{d_{0}+d_{1}+\cdots+d_{k-1}}{2} \cdot M
\end{aligned}
$$

where $p_{01}+p_{04}+p_{02}+p_{03} \triangleq M$ ( $M$ is a positive constant).
Therefore, we can find that

$$
\begin{aligned}
& d_{k}=\left|m_{k}-p_{k 1} \cdot p_{k 4}\right| \\
& =\left|\frac{p_{k 1} \cdot p_{k 4}+p_{k 2} \cdot p_{k 3}}{2}-p_{k 1} \cdot p_{k 4}\right| \\
& =\frac{\left|p_{k 1} \cdot p_{k 4}-p_{k 2} \cdot p_{k 3}\right|}{2} \\
& =\frac{\left|\left(p_{k-1,1}-\frac{d_{k-1}}{2}\right)\left(p_{k-1,4}-\frac{d_{k-1}}{2}\right)-\left(p_{k-1,2}-\frac{d_{k-1}}{2}\right)\left(p_{k-1,3}-\frac{d_{k-1}}{2}\right)\right|}{2} \\
& =\frac{\left|p_{k-1,1} \cdot p_{k-1,4}-p_{k-1,2} \cdot p_{k-1,3}-\frac{d_{k-1}}{2} \cdot M\right|}{2}
\end{aligned}
$$

Since $p_{k-1,1} \cdot p_{k-1,4}-p_{k-1,2} \cdot p_{k-1,3}>0$, we have

$$
\begin{aligned}
& d_{k-1}=\frac{\left|p_{k 1} \cdot p_{k 4}-p_{k 2} \cdot p_{k 3}\right|}{2} \\
& =\frac{p_{k 1} \cdot p_{k 4}-p_{k 2} \cdot p_{k 3}}{2}
\end{aligned}
$$

Hence,

$$
p_{k 1} \cdot p_{k 4}-p_{k 2} \cdot p_{k 3}=2 d_{k-1}
$$

Therefore,

$$
\begin{aligned}
& d_{k}=\frac{\left|p_{k-1,1} \cdot p_{k-1,4}-p_{k-1,2} \cdot p_{k-1,3}-\frac{d_{k-1}}{2} \cdot M\right|}{2} \\
& =\frac{\left|2 d_{k-1}-\frac{d_{k-1}}{2} \cdot M\right|}{2}=\frac{\left|2 d_{k-1}\left(1-\frac{M}{4}\right)\right|}{2}
\end{aligned}
$$

By $0<M \leq 4$, we have

$$
d_{k}=d_{k-1}\left|1-\frac{M}{4}\right|=d_{k-1}\left(1-\frac{M}{4}\right)
$$

When $M=4, d_{k}=0(k \geq 1)$, then

$$
\begin{aligned}
& p_{k 1} \cdot p_{k 4}-p_{k 2} \cdot p_{k 3} \\
& \quad=p_{01} \cdot p_{04}-p_{02} \cdot p_{03}-\frac{d_{0}+d_{1}+\cdots+d_{k-1}}{2} \cdot M \\
& \quad=p_{01} \cdot p_{04}-p_{02} \cdot p_{03}-\frac{d_{0}}{2} \cdot 4 \\
& =2 d_{0}-2 d_{0}=0
\end{aligned}
$$

Therefore, Theorem 1 holds in this case.
When $0<M<4$,

$$
d_{k}=d_{k-1}\left(1-\frac{M}{4}\right)=d_{k-2}\left(1-\frac{M}{4}\right)^{2}=\cdots=d_{0}\left(1-\frac{M}{4}\right)^{k}
$$

thus

$$
\begin{aligned}
& p_{k 1} \cdot p_{k 4}-p_{k 2} \cdot p_{k 3} \\
& =p_{01} \cdot p_{04}-p_{02} \cdot p_{03}-\frac{d_{0}+d_{1}+\cdots+d_{k-1}}{2} \cdot M \\
& =2 d_{0}-8 d_{0}\left[1-(1-M / 4)^{k}\right]
\end{aligned}
$$

Let $p_{k 1} \cdot p_{k 4}-p_{k 2} \cdot p_{k 3}=2 d_{0}-8 d_{0}\left[1-(1-M / 4)^{k}\right] \leq 0$, we can find that

$$
(1-M / 4)^{k} \leq \frac{3}{4}
$$

Since $0<M<4$, we have

$$
0<1-M / 4<1
$$

Hence, there exists $k$ such that

$$
(1-M / 4)^{k} \leq \frac{3}{4}
$$

From the above, we known that there exists $k$ such that

$$
p_{k 1} \cdot p_{k 4} \leq p_{k 2} \cdot p_{k 3}
$$

This completes the proof of Theorem 1.

# 5. Experiments 

In this section, we verify the effectiveness and performance of four algorithms mentioned in this paper by two simulations.

### 5.1. Experiment 1

### 5.1.1. Simulation Model

This simulation adopts the lawn moist model, as shown in Figure 1.
In the model, $R, S$ and $W$ meet the multiplicative synergy constraint, which can be expressed as follows:

$$
P(W=1 \mid R=1, S=1) \cdot P(W=1 \mid R=0, S=0) \leq P(W=1 \mid R=1, S=0) \cdot P(W=1 \mid R=0, S=1)
$$

In the above inequality, when the value of the variable is 1 , it means that the event occurs, and 0 means that it does not occur. Table 1 shows the real parameters in the network.

In order to quantitatively analyze the performance of several methods in this paper, KL divergence from real parameters is introduced as an index to measure the accuracy of the algorithm. The expression of KL divergence (see [30]) is as follows:

$$
K L(\hat{\theta}, \theta)=\sum_{X} p_{\hat{\theta}}(X) \ln \frac{p_{\hat{\theta}}(X)}{p_{\theta}(X)}
$$

Table 1. Real parameters of the simulation network.


# 5.1.2. Simulation Analysis 

Take the sample size as 20 , the simulation results obtained by several algorithms are shown from Tables 2-6, and the KL divergences between the learning results and the real parameters are shown in Table 7.

Table 2. Learning parameters of MLE.


Table 3. Learning parameters of Method 1.


Table 4. Learning parameters of Method 2.


Table 5. Learning parameters of Method 3.


Table 6. Learning parameters of Method 4.


Table 7. KL divergences between the learning results and the real parameter.


Tables 2-6 show the network parameters learned by MLE algorithm and the four algorithms proposed in this paper when the sample size is 20. Table 7 shows the KL divergences between the learning results and the real parameters. The experimental results show that the KL divergence between the learning parameters of the four methods proposed in this paper and real parameters is smaller than that between the learning parameters of MLE and the real parameters when the sample size is small. It shows that each method proposed in this paper is superior to the MLE algorithm in the accuracy of parameter learning. In addition, it can be seen from Table 7 that among the four algorithms proposed in this paper, the learning accuracy of Method 2 is the highest, while that of Method 1 is the lowest.

# 5.2. Experiment 2 

### 5.2.1. Simulation Model

This simulation adopts Asia Network, as shown in Figure 2, where ' 1 ' stands for $X_{1}$, ' 2 ' stands for $X_{2}$, ' 3 ' stands for $X_{3}$, ' 4 ' stands for $X_{4}$, ' 5 ' stands for $X_{5}$, ' 6 ' stands for $X_{6}$, ' 7 ' stands for $X_{7}$, and ' 8 ' stands for $X_{8}$.
![img-1.jpeg](img-1.jpeg)

Figure 2. Asia network.
In the model, $X_{7}$ and, $X_{8}$ meet the multiplicative synergy constraint, which can be expressed as follows:

$$
\begin{gathered}
P\left(\mathrm{X}_{8}=1 \mid \mathrm{X}_{5}=1, \mathrm{X}_{7}=1\right) \cdot P\left(\mathrm{X}_{8}=1 \mid \mathrm{X}_{5}=0, \mathrm{X}_{7}=0\right) \\
\leq P\left(\mathrm{X}_{8}=1 \mid \mathrm{X}_{5}=1, \mathrm{X}_{7}=0\right) \cdot P\left(\mathrm{X}_{8}=1 \mid \mathrm{X}_{5}=0, \mathrm{X}_{7}=1\right)
\end{gathered}
$$

In the above inequality, if the value of the variable is 1 , it means that the event occurs, and 0 means that it does not occur. Table 8 shows the real parameters in the network.

Table 8. Real parameters of the simulation network.


The explanations of $X_{i}$ are as follows:
$X_{1}$ —Visit To Asia (2): Visit, No_Visit;

$X_{2}$-Tuberculosis (2): Present, Absent;
$X_{3}$-Smoking (2): Smoker, Nonsmoker;
$X_{4}$-Lung Cancer (2): Present, Absent;
$X_{5}$-Tuberculosis or Lung Cancer (2): True, False;
$X_{6}$-Xray Result (2): Abnormal, Normal;
$X_{7}$-Bronchitis (2): Present, Absent;
$X_{8}$-Dyspnoea (2): Present, Absent.

# 5.2.2. Simulation Analysis 

Take the sample size as 20, the simulation results obtained by several algorithms are shown from Tables 9-13, and the KL divergences between the learning results and the real parameters are shown in Table 14.

Table 9. Learning parameters of MLE.


Table 10. Learning parameters of Method 1.


Table 11. Learning parameters of Method 2.


Table 12. Learning parameters of Method 3.


Table 13. Learning parameters of Method 4.


Table 14. KL divergences between the learning results and the real parameter.


Tables 9-13 show the network parameters learned by MLE algorithm and the four algorithms proposed in this paper when the sample size is 20. Table 14 shows the KL

divergences between the learning results and the real parameters. The experimental results show that the KL divergence between the learning parameters of the four methods proposed in this paper and real parameters is smaller than that between the learning parameters of MLE and the real parameters when the sample size is small. It shows that each method proposed in this paper is superior to the MLE algorithm in the accuracy of parameter learning. In addition, it can be seen from Table 14 that among the four algorithms proposed in this paper, the learning accuracy of Method 1 is the highest, while that of Method 3 is the lowest.

# 6. Conclusions 

By referring to the idea of PAV algorithm, this paper proposes four methods to deal with multiplicative synergy constraints. We analyze and compare the algorithms from the algorithm accuracy. The simulations results show that the four algorithms mentioned in this paper are superior to the MLE algorithm in the accuracy of parameter learning, which can improve the results of the MLE algorithm to obtain more accurate estimators of the parameters.

The methods proposed in this paper can reduce the dependence of parameter learning on expert experiences. Combining these constraint methods with Bayesian estimation can improve the accuracy of parameter learning under small sample conditions. However, the algorithms in this paper also have limitations. When there are many parent nodes, it is difficult to give the parameter size relationship of the network. In the future research, the constraints presented in this paper can be combined with other existing constraints to reduce the dependence of constraints on expert experiences and improve the accuracy of parameter learning.

Author Contributions: Methodology, software, writing-original draft, writing-review and editing, Y.Z.; funding acquisition, supervision project administration, Z.H.; validation, Y.Z. and Z.H. All authors have read and agreed to the published version of the manuscript.
Funding: This work was supported by Bigdata Modeling and Intelligent Computing Research Institute, Hubei University of Education, Scientific Research Project of Education Department of Zhejiang Province (Y202147034), Zhejiang College of Shanghai University of Finance and Economics for Scientific Research Projects at the Provincial and Above Levels, and the National Statistical Science Research Project of China (2021LY100).

Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Not applicable.
Acknowledgments: The authors would like to thank everyone for help.
Conflicts of Interest: The authors declare no conflict of interest.
