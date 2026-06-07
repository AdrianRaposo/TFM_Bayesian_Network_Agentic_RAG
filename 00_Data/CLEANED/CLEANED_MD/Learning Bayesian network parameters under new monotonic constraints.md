# Learning Bayesian network parameters under new monotonic constraints 

Ruohai Di, Xiaoguang Gao*, and Zhigao Guo<br>School of Electronic and Information, Northwestern Polytechnical University, Xi'an 710129, China


#### Abstract

When the training data are insufficient, especially when only a small sample size of data is available, domain knowledge will be taken into the process of learning parameters to improve the performance of the Bayesian networks. In this paper, a new monotonic constraint model is proposed to represent a type of common domain knowledge. And then, the monotonic constraint estimation algorithm is proposed to learn the parameters with the monotonic constraint model. In order to demonstrate the superiority of the proposed algorithm, series of experiments are carried out. The experiment results show that the proposed algorithm is able to obtain more accurate parameters compared to some existing algorithms while the complexity is not the highest.


Keywords: Bayesian networks, parameter learning, new monotonic constraint.

DOI: 10.21629/JSEE.2017.06.22

## 1. Introduction

Bayesian networks have become a widely used method in the field of uncertain knowledge modeling [1-3]. A Bayesian network, which consists of a graph structure and some parameters, is a concise representation of a joint probability distribution over a set of stochastic variables [4]. Conceptually speaking, the structure of a Bayesian network describes the conditional independence relationship between a set of variables, and the parameters of a Bayesian network describe the quantitative relationship between a set of variables. A major difficulty in applying Bayesian network to solve the practical problem is to establish relationship between nodes from the training data.

When sufficient data are available, some methods have been proposed to learn the structure and parameters of Bayesian networks and have achieved satisfactory results

[^0][5-7]. Unfortunately, there are some data hard to get or getting the data will cost too much, such as geological hazard data and aerial combat data and so on. Therefore, the data are not sufficient in many cases, which may lead to inaccurate structure and parameters of a Bayesian network. Consequently, such "under-training" Bayesian networks with inaccurate structure and parameters will inevitably give rise to considerable errors when applied in reasoning and decision-making. Therefore, learning the structure and parameters of Bayesian networks when the size of the training samples is small is of fundamental importance both theoretically and practically. In this paper we place our emphasis on the parameter learning of Bayesian networks, whose structure is available, with a small-sized training data.

In order to acquire Bayesian network parameters when the data are not sufficient, some research has been completed. For the research, the crucial part is to incorporate the expert knowledge or domain knowledge into the process of learning parameters. Among these existing researches, different kinds of domain knowledge have been formalized into some types of constraints. Witting [8] used the qualitative influence constraint to construct the penalty function, combine the penalty function with the maximum entropy function to get the objective function, and then apply the adaptive probabilistic networks (APN) algorithm to learn the parameters. Altendorf [9] integrated the monotonic constraint into the objective function, but solve the problem with the gradient-descent algorithm. Feelders [10] transformed the qualitative influence constraint into the order constraint in order to correct the results of the maximum likelihood estimation (MLE). Campos and Niculescu [11-13] regarded the parameters learning as a constrains convex problem. Campos [14] proposed the constrained maximum entropy (CME) algorithm based imprecise Dirichlet model. Chang $[15,16]$ put forward the qualitative maximum a posterior (QMAP) algorithm to learn the parameters, which used the Monte Carlo


[^0]:    Manuscript received August 01, 2016.
    *Corresponding author.

    This work was supported by the National Natural Science Foundation of China (61305133; 61573285) and the Fundamental Research Funds for the Central Universities (3102016CG002).

sampling to get the parameters in accordance with the constraint. And then, the hyperparameters of Dirichlet priors were obtained. Liao [17] proposed the constrained expectation maximum algorithm (CEM) for parameters learning, which combined the constraint and maximum entropy, and applied the gradient-descent algorithm to search the optimal solution. Zhou [18] proposed the multinomial parameters learning with constraints (MPL-C) algorithm, which used the auxiliary hybrid Bayesian network and dynamic discretization junction tree (DDJT) algorithm to learn the parameters. All above are the existing Bayesian network parameters learning methods that employ domain knowledge for learning parameters from small dataset. Besides, there are still a few other methods which need not domain knowledge, such as noisy-or-gates [19,20] and minimum free energies [21]. Based on the careful analysis of existing research, it is found that the description of qualitative influence constraint or monotonic constraint mostly are the sorting of the parameters of Bayesian networks when the status of the child node is the same, but the status of the parent node is different. In order to express the sorting of the parameters of Bayesian networks when the status of the parent node is the same, but the status of the child node is different, a new inequality constraint named new monotonic constraint is proposed. Even though the existing research mentions some methods which could learn the parameters of Bayesian networks under the inequality constraint, such as convex optimization and isotonic regression. The advantages of the two algorithms are their generic for all different inequality constraints. However, these two algorithms have their own shortcomings. The convex optimization has the high complexity and the isotonic regression has the poor learning results. Di [22] gave a method to deal with the new monotonic constraint. However, it brings about higher complexity and lower precision. In order to find a more convenient and effective method to learn the parameters of Bayesian networks under the proposed constraint, a novel algorithm is proposed which is called monotonic constraint estimation (MCE) algorithm.

The reminder of this paper is organized as follows. In Section 2, we briefly review Bayesian networks and give a simple instance to illustrate the problem we are solving in this paper. In Section 3, the new monotonic constraint is presented. In Section 4, the MCE algorithm is introduced in detail. In Section 5, the experiments are executed to evaluate the performance of the algorithm through the comparison with some existing methods. In the final section, a few conclusions are drawn from our work and some interesting directions are pointed out for further research.

## 2. Preliminaries

In this section, some concepts of Bayesian networks will be briefly reviewed to help readers better understand.

### 2.1 Bayesian networks

Bayesian networks are represented as a directed acyclic graph which contains some vertices and edges. Vertices represent random variables, while edges represent probabilistic relationship between random variables. For each variable node $X$, a conditional probability table is specified as $P(X \mid \pi(X))$, which describes the probability over the possible values of $X$ and possible configurations of parent variables $\pi(X)$. In a Bayesian network, the joint probability can be written as follows:

$$
p\left(x_{1}, \ldots, x_{n}\right)=\prod_{i=1}^{n} p\left(x_{i} \mid \pi\left(x_{i}\right)\right)
$$

where $x_{i}$ are the state value of variable $i$ and $\pi\left(x_{i}\right)$ denotes the configuration value of parent variables of variable $X_{i}$.

To illustrate the Bayesian network more clearly, the lawn moist Bayesian network is employed, which is depicted as Fig. 1. The model will be used as the experimental model later. The variables in the network are binary, the value is 0 or 1 , that is, if the variable occurs or is present it has the state 1 . Besides, the conditional probabilities are also given in Fig. 1. Our purpose is to learn the parameters in the following Bayesian network.
![img-0.jpeg](img-0.jpeg)

Fig. 1 Lawn moist model

### 2.2 Parameter learning

There are two algorithms often mentioned for Bayesian network parameters learning. They are Bayesian estimation and MLE. There is a hypothesis that the dataset is complete and has no missing data. The MLE of the pa-

rameters is

$$
\theta_{i j k}=p\left(X_{i}=k \mid \pi\left(X_{i}\right)=j\right)=\frac{N_{i j k}}{\sum_{k^{\prime}=1}^{r_{i}} N_{i j k^{\prime}}}
$$

where $i$ is the index of node $X, j$ is the index of parent nodes' configuration, $k$ and $k^{\prime}$ are $X_{i}$ 's states, $r_{i}$ is the number of the states of $X_{i}$, and $N_{i j k}$ is the number of cases which satisfy $X_{i}=k$ and $\pi\left(X_{i}\right)=j$ in the dataset.

When Bayesian statistic is applied to get the estimation of the discrete random variables, based on Bayesian theorem, a posterior probability density function $\rho(\theta \mid d)$ is expressed as follows: $\rho(\theta \mid d) \propto \rho(\theta) f(d \mid \theta)$, where $d$ represents the data, $\rho(\theta)$ is the prior distribution and $f(d \mid \theta)$ is the likelihood function. For the discrete random variables, the likelihood function of the parameters is the multinomial distribution function. The prior and posterior of the multinomial distribution are the Dirichlet distributions. Therefore, the Bayesian network parameters are obtained as

$$
\begin{aligned}
\theta_{i j k}= & p\left(X_{i}=k \mid \pi\left(X_{i}\right)=j\right)= \\
& \frac{\alpha_{i j k}+N_{i j k}}{\sum_{k^{\prime}=1}^{r_{i}} \alpha_{i j k^{\prime}}+N_{i j k^{\prime}}}
\end{aligned}
$$

As indicated in (3), parameters $\alpha$ prevent Bayesian network parameters from getting over-fit, especially when the dataset is small. However, it is difficult for a domain expert to accurately specify the parameters $\alpha$ of a Dirichlet distribution because they are not intuitive for the expert.

### 2.3 Definition of small data set

When the data are very sufficient, MLE is an ideal algorithm to learn the parameters. Unfortunately, the data set is often small, which makes the MLE get no accurate results. Therefore, there is a problem that how many samples could make the MLE get the expected accurate parameters. With regard to the problem, Dasgupta [23] defined a calculation of the lower limit of the sample number for parameters learning with a given Bayesian network structure. If there is a Bayesian network which has $n$ boolean nodes, and no node has more than $k$ parents, the sample number is calculated with a confidence $(1-\delta)$ as follows:

$$
\begin{aligned}
\text { Number } \geqslant & \frac{288 \times n^{2} \times 2^{k}}{\varepsilon^{2}} \ln ^{2}\left(1+\frac{3 n}{\varepsilon}\right) \\
& \ln \left(\frac{1+3 n / \varepsilon}{\varepsilon \delta}\right)
\end{aligned}
$$

Constant $\varepsilon$ is the error and is often set as $\varepsilon=n \sigma, \sigma$ is the Kullback-Leibler (KL) divergence of a parameter.

In the paper, when the given data set is smaller than the data size in (4), the given data set is defined as a small data set.

## 3. Monotonic constraint model

The monotonic constraint was proposed before, which informally means that higher values of the parent node stochastically result in higher values of the child node. However, the new monotonic constraint in this paper is different from the proposed monotonic constraint. The new monotonic constrain definition is given as follows:

Definition 1 For a Bayesian network $G$ containing a set of variables $\left\{X_{1}, \ldots, X_{n}\right\}$, without loss of generality, the node $X_{i}$ has $r$ states which contain $\{1,2, \ldots, k, \ldots, r\}, 1 \leqslant k \leqslant r$. Its parent node set $\pi\left(X_{i}\right)$ has $q$ states which contain $\{1,2, \ldots, j, \ldots, q\}, 1 \leqslant j \leqslant q$. When $\pi\left(X_{i}\right)$ is equal to $j$, the parameters $\theta_{i j k}=p\left(X_{i}=\right.$ $\left.k \mid \pi\left(X_{i}\right)=j\right)$ satisfy

$$
\theta_{i j 1} \leqslant \theta_{i j 2} \leqslant \cdots \leqslant \theta_{i j r} \text { or } \theta_{i j 1} \geqslant \theta_{i j 2} \geqslant \cdots \geqslant \theta_{i j r}
$$

Then $\theta_{i j k}$ is considered to be consistent with the monotonic constraint, (5) is the model of the monotonic constraint. Suppose the Bayesian network parameters conform to the monotonic constraint. Combining with the criterion of the parameters, every parameter will be transformed into the interval as follows:

$$
\begin{aligned}
& \left\{\begin{array}{c}
\theta_{i j 1}+\theta_{i j 2}+\cdots+\theta_{i j r}=1 \\
\theta_{i j 1} \leqslant \theta_{i j 2} \leqslant \cdots \leqslant \theta_{i j r}
\end{array} \Rightarrow\right. \\
& \left\{\begin{array}{l}
0 \leqslant \theta_{i j 1} \leqslant \frac{1}{r} \\
\theta_{i j 1} \leqslant \theta_{i j 2} \leqslant \frac{1-\theta_{i j 1}}{r-1} \\
\vdots \\
\theta_{i j r-2} \leqslant \theta_{i j r-1} \leqslant \frac{1-\sum_{k=1}^{r-2} \theta_{i j k}}{2} \\
\theta_{i j r}=1-\sum_{k=1}^{r-1} \theta_{i j k}
\end{array}\right.
\end{aligned}
$$

Suppose $p(\theta)$ conforms to Dirichlet distribution $D\left(\alpha_{1}, \alpha_{2}, \ldots, \alpha_{r}\right)$, which is

$$
p(\theta)=\frac{\Gamma(\alpha)}{\prod_{i=1}^{r} T\left(\alpha_{i}\right)} \prod_{i=1}^{r} \theta^{\alpha_{i}-1}
$$

where $\alpha=\sum_{i=1}^{r} \alpha_{i}$. It is obvious that the Dirichlet distribution $D\left(\alpha_{1}, \alpha_{2}\right)$ will convert into Beta distribution

$B\left(\alpha_{1}, \alpha_{2}\right)$ when $r=2$. Then, the Bayesian estimation of $\theta$ can be written as follows:

$$
\theta_{i}^{*}=\int \theta_{i} p\left(\theta_{i} \mid D\right) \mathrm{d} \theta_{i}=\frac{m_{i}+\alpha_{i}}{m+\alpha}
$$

Considering that the joint distribution of the Bayesian network parameters is Dirichlet distribution and the marginal distribution of Dirichlet distribution is Beta distribution, the prior distribution of parameter $\theta$ will be depicted with Beta distribution.

$$
p(\theta)=\frac{\Gamma\left(\alpha_{1}+\alpha_{2}\right)}{\Gamma\left(\alpha_{1}\right) \Gamma\left(\alpha_{2}\right)} \theta^{\alpha_{1}-1}(1-\theta)^{\alpha_{2}-1}
$$

Equation (6) gives the upper and lower bounds of the Bayesian network parameters. If no additional prior information is available, the parameter $\theta$ whose scope is given by (6) can be presumed to conform to the uniform distribution $U\left(\theta_{1}, \theta_{2}\right)$. Then the problem is converted to how to use the Beta distribution to approach the uniform distribution. Therefore, we apply the method given by (10) to approach the uniform distribution using a Beta distribution.

$$
\min _{\alpha_{1} \alpha_{2}} \int_{0}^{1}\left(U\left(\theta_{1}, \theta_{2}\right)-B\left(\alpha_{1}, \alpha_{2}\right)\right)^{2} \mathrm{~d} \theta
$$

where $\alpha_{1}$ and $\alpha_{2}$ are the parameters of Beta distribution. As solving the problem above leads to high computation, the approximate method is used as follows:

$$
\begin{gathered}
\left\{\begin{array}{l}
m_{1}=\int_{0}^{1} U(\theta) \theta \mathrm{d} \theta \\
m_{2}=\int_{0}^{1} U(\theta) \theta^{2} \mathrm{~d} \theta
\end{array}\right. \\
\left\{\begin{array}{l}
M_{1}=\int_{0}^{1} B(\theta) \theta \mathrm{d} \theta=\frac{\alpha_{1}}{\alpha_{1}+\alpha_{2}} \\
M_{2}=\int_{0}^{1} B(\theta) \theta^{2} \mathrm{~d} \theta= \\
\frac{\alpha_{1} \alpha_{2}}{\left(\alpha_{1}+\alpha_{2}\right)^{2}\left(\alpha_{1}+\alpha_{2}+1\right)}+M_{1}^{2}
\end{array}\right. \\
\left\{\begin{array} { l } 
{ M _ { 1 } = m _ { 1 } } \\
{ M _ { 2 } = m _ { 2 } }
\end{array} \Rightarrow \left\{\begin{array}{l}
\alpha_{1}=\frac{m_{1}^{2}-m_{1} m_{2}}{m_{2}-m_{1}^{2}} \\
\alpha_{2}=\frac{m_{1}-m_{2}}{m_{2}-m_{1}^{2}}\left(1-m_{1}\right)
\end{array}\right.\right.
\end{gathered}
$$

Based on (11)-(13), we can figure out the parameters $\alpha_{1}$ and $\alpha_{2}$. Then $\alpha_{1}$ and $\alpha_{2}$ are used to calculate Bayesian network parameters as virtual samples using (8). Fig. 2
illustrates how to use a Beta distribution to approach the objective uniform distribution. The $x$-axis of Fig. 2 represents the random variable which belongs to $[0,1]$. The $y$-axis represents the probability of the random variable.
![img-1.jpeg](img-1.jpeg)

Fig. 2 Uniform and Beta distribution

## 4. MCE algorithm

The new monotonic constraint and how to convert it to a Beta distribution have been given in Section 3. Then this section will explain how to use Beta distribution in the process of Bayesian network parameters learning. If Bayesian network parameters $\theta_{i j^{*}}$ subject to the monotonic constraints, then the parameter learning process is given as follows:

Step 1 Establish the monotonic constraint based on the domain knowledge.

Step 2 Obtain interval constraint using (5) and (6), and the scope of $\theta_{i j 1}$ will be obtained first.

Step 3 Convert uniform distribution into Beta distribution using (10) - (13) and obtain virtual sample information.

Step 4 Merge the virtual sample information into Bayesian estimation and get the estimation of parameters:

$$
\theta_{i j k}=\frac{\alpha_{1}+N_{i j k}}{\alpha_{1}+\alpha_{2}+N_{i j}}
$$

where $N_{i j k}$ is the number of samples when the value of node $i$ is $k$ and the value of its parent is $j$.

Step 5 Take obtained parameters as the lower bound of the next parameter, return to Step 2 and repeat Steps 2-5 until all parameters are obtained.

The process of the MCE algorithm is reported in Fig. 3. The MCE is an iterative algorithm until all the parameters $\theta_{i j^{*}}$ have been obtained.

![img-2.jpeg](img-2.jpeg)

Fig. 3 Process of the MCE

## 5. Experiments

In this paper, the classical lawn moist Bayesian network, which has been shown in Fig. 1, is applied for simulation. Our objective is to learn Bayesian network parameters using the MCE algorithm based on the new monotonic constraints. According to domain knowledge and common sense, we give the monotonic constraints among the parameters of the lawn moist network as follows:

$$
\begin{gathered}
P(R=1 \mid C=1)>P(R=0 \mid C=1) \\
P(S=1 \mid C=1)<P(S=0 \mid C=1) \\
P(R=1 \mid C=0)<P(R=0 \mid C=0) \\
P(S=1 \mid C=0)>P(S=0 \mid C=0) \\
P(W=1 \mid R=1, S=1)>P(W=0 \mid R=1, S=1) \\
P(W=1 \mid R=1, S=0)<P(W=0 \mid R=1, S=0) \\
P(W=1 \mid R=0, S=1)<P(W=0 \mid R=0, S=1) \\
P(W=1 \mid R=0, S=0)<P(W=0 \mid R=0, S=0)
\end{gathered}
$$

It means that the event will occur when the value of the variable is 1 , oppositely, the event will not occur. Accordingly, $P(R=1 \mid C=1)>P(R=0 \mid C=1)$ means the probability of raining is higher when the weather is cloudy.

In order to analyze the performance of the proposed algorithm, MCE is compared with MLE, convex optimization estimation (COE) [10] and isotonic regression estimation (IRE) [11] in the experiment with the same constraints. The training data are generated from the network with manually assigned parameters using Bayesian network toolbox designed by Murphy. Learning results are calculated by averaging KL divergence between the
learned parameters and the true parameters. The KL divergence is defined as follows:

$$
\mathrm{KL}\left(\operatorname{Pr}^{\prime}, \operatorname{Pr}\right)=\sum_{X} \operatorname{Pr}(X) \lg \frac{\operatorname{Pr}(X)}{\operatorname{Pr}^{\prime}(X)}
$$

where $\operatorname{Pr}$ and $\operatorname{Pr}^{\prime}$ represent the true parameters and parameters learned by some samples respectively.

In the simulation experiment, four different algorithms are executed under different sample sizes. All the algorithms are repeated for 50 times and the mean KL divergence is calculated as the performance criteria. The results are depicted in Fig. 4 and Fig. 5. Fig. 5 is the local enlarged drawing of the Fig. 4.
![img-3.jpeg](img-3.jpeg)

Fig. 4 KL divergence of all algorithms
![img-4.jpeg](img-4.jpeg)

Fig. 5 KL divergence of all algorithms
The experimental results show that the KL divergence of the proposed algorithms (MCE) is the minimum of all the algorithms when the sample size is less than 35 . The conclusion is especially obvious when the sample size is

less than 10. In other words, the MCE has the highest accuracy of all. The accuracy of the IRE and COE are worse than MCE. MLE is the worst. The KL divergences of some experiments are given in Table 1. In addition, the sample size these algorithms need to get for the same KL divergence is given in Fig. 6. As you can see in Fig. 6, the MCE algorithm needs the smallest data size to achieve the same KL divergence.

Table 1 KL divergence under different sample sizes


![img-5.jpeg](img-5.jpeg)

Fig. 6 Samples needed by different algorithms to achieve the same KL divergence

Average simulation results are given in the previous paragraph. In order to further demonstrate the superiority of the proposed algorithm. The KL divergence of 10 experiments is given in Fig. 7 when the sample size is 10. Because of the sample randomness, the results are different every time. Fig. 7 clearly shows that the MCE algorithm has the best stability and accuracy of all the algorithms. Meanwhile, the learned parameters are applied for reasoning. In the experiment, $P(C \mid R, S)$ will be computed when the evidence $R$ is 0 and $S$ is 1 . With the increase of the data sample size, $P(C=0 \mid R, S)$ becomes bigger and bigger while $P(C=1 \mid R, S)$ becomes smaller and smaller in Fig. 8. This condition could make the reasoning more clearly. All in all, it is concluded that the MCE algorithm can learn parameters most accurately from small dataset by employing monotonic constraints.
![img-6.jpeg](img-6.jpeg)

Fig. 7 KL of different algorithms with 10 samples
![img-7.jpeg](img-7.jpeg)

Fig. 8 Reasoning result of MCE

In order to analyze the complexity of every algorithm, the runtime is used as a criterion. Similar to the previous KL divergence, the experiment will be repeated for 50 times to get the mean values of the runtime. Fig. 10 is the local enlarged drawing of Fig. 9. From Fig. 9 and Fig. 10, the conclusions can be obtained that MCE algorithm costs less runtime than the COE algorithm and costs more runtime than the MLE algorithm and the IRE algorithm. The MLE algorithm costs the least runtime and COE algorithm costs the most. The runtime of all the algorithms are given in Table 2. The runtime of the MCE algorithm is 0.04 s longer than MLE and IRE. Similar to the KL divergence, the runtime of 10 experiments are given in Fig. 11 and Fig. 12 when the sample size is 10. Fig. 12 is the local enlarged drawing of Fig. 11. The conclusions can be obtained that the COE algorithm costs the most runtime and the MLE algorithm costs the least runtime.

Generally speaking, the proposed algorithm has higher complexity than MLE and IRE and lower complexity than COE.
![img-8.jpeg](img-8.jpeg)

Fig. 9 Runtime of different algorithms
![img-9.jpeg](img-9.jpeg)

Fig. 10 Runtime of different algorithms (local)
![img-10.jpeg](img-10.jpeg)

Fig. 11 Runtime of different algorithms with 10 samples

Table 2 Runtime of different algorithms


![img-11.jpeg](img-11.jpeg)

Fig. 12 Runtime of different algorithms with 10 samples (local)

## 6. Conclusions and future research

In this paper, a new monotonic constraint has been proposed to describe the new domain knowledge of parameter learning. And then, a novel algorithm is proposed to learn the parameters under the new monotonic constraints. The proposed algorithm is also suitable for learning Bayesian network parameters from small-sized training data under interval constraint. The proposed algorithm is compared with some existing methods in the experiments. The results show that the proposed algorithm improves the accuracy of parameter learning, while leads to a little higher complexity. The paper provides a new frame for Bayesian network parameters learning when the training data are not enough.

In addition, we find some interesting directions for further research. First, when the monotonic constraint is partly known, the proposed algorithm cannot deal with it, then how to solve that problem. Second, in order to get more accurate parameters, integrating other types of constraints (such as additive synergy or product synergy constraints) with the monotonic constraint to improve the accuracy could deserve further focus.

## Biographies

![img-12.jpeg](img-12.jpeg)

Ruohai Di was born in 1986. He received his M.S. and Ph.D. degrees in system engineering of Northwest Polytechnical University, in 2011 and 2016, respectively. He currently does postdoctoral research in Northwestern Polytechnical University. His topics of interests include Bayesian networks (structure and parameter learning algorithm), and data mining. E-mail: xfwtdrh@163.com

![img-13.jpeg](img-13.jpeg)

Xiaoguang Gao was born in 1957. She received her M.S. and Ph.D. degrees in systems engineering from Northwest Polytechnical University, in 1986 and 1989, respectively. She is currently a professor in Department of Systems Engineering, School of Electronics and Information, Northwestern Polytechnical University. Her topics of interests include Bayesian networks, deep learning, and advanced control theory and application.
E-mail: cxg2012@nwpu.edu.cn

![img-14.jpeg](img-14.jpeg)

Zhigao Guo was born in 1986. He received his M.S. degree in pattern recognition and intelligent system from Shenyang Aerospace University, in 2010. He is currently a Ph.D. student in system engineering in Department of Systems Engineering, School of Electronics and Information, Northwestern Polytechnical University. His topics of interests include Bayesian networks (parameter learning), and data mining.
E-mail: guozhigao2004@163.com