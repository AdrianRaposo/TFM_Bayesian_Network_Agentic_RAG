# Where To: Crowd-Aided Path Selection by Selective Bayesian Network 

Chen Zhang, Member, IEEE, Haodi Zhang, Weiteng Xie, Nan Liu, Kaishun Wu, Member, IEEE, and Lei Chen Fellow, IEEE


#### Abstract

With the wide usage of geo-positioning services (GPS), GPS-based navigation systems have become more and more of an integral part of people's daily lives. GPS-based navigation systems usually suggest multiple paths for a pair of given source and target. Therefore, users become perplexed when trying to select the best one among them, namely the problem of best path selection. Too many suggested paths may jeopardize the usability of the recommendation data, and decrease user satisfaction. Although the existing studies have already partially relieved this problem through integrating historical traffic logs or updating traffic conditions periodically, their solutions neglect the potential contribution of human experiences. In this paper, we resort to crowdsourcing to ease the pain of best path selection. However, the first step of using the crowd is to ask the right questions. For best path selection problem, the simple questions (e.g. binary voting) on crowdsourcing platforms cannot be directly applied to road networks. Thus, in this paper, we have made the first contribution by designing two right types of questions, namely Routing Query (RQ) to ask the crowd to decide the direction at each road intersection. Secondly, we propose a series of efficient algorithms to dynamically manage the questions in order to reduce the selection hardness within a limited budget. In particular, we show that there are two factors affecting the informativeness of a question: the randomness (entropy) of the question and the structural position of the road intersection. Furthermore, we extend the framework to enable multiple RQs per round. To ease the pain of the sample sensitiveness, we propose a new approach to reduce the selection hardness by reasoning on a so-called Selective Bayesian network. We compare our approach against several baselines, and the effectiveness and efficiency of our proposal are verified by the results in simulations and experiments on real-world datasets. The experimental results show that, even the Selective Bayesian Network provides only partial information of causality, the performance on the reduction of the selection hardness are dramatically improved, especially when the size of samples are relatively small.


Index Terms-Crowdsourcing, Approximation Algorithm, Path Selection

## 1 INTRODUCTION

WITH the rapid development of information technology and data science, the scale of diverse data is getting larger and larger. For instance, the global positioning systems makes the real-time navigation systems commonly used in daily life. With the data collected from mobile devices, a good navigation system gives optimal routes between given locations. In realistic applications, however, the selection of the best path can be very challenging, especially in those large-scaled domains. For a road network with a large amount of paths and crossroads, it might be difficult to maintain precise information of the entire map all the time. To address the problem, quite a few existing studies integrate historical traffic logs or periodically update traffic conditions. However they usually neglect the potential contribution of human experience.

In our previous work [1], a crowd-aided path selection frame-

- C. Zhang is with the Department of Computing, Hong Kong Polytechnic University, Hong Kong, SAR China. E-mail: c4zhang@comp.polyu.edu.hk.
- H. Zhang is with the Shanghai Research Center for Brain Science and Brain-Inspired Intelligence, Shanghai, China, and the College of Computer Science and Software Engineering, Shenzhen University, Shenzhen, China. E-mail: zhanglul.ustc@ gmail.com.
- W. Xie and K. Wu are with the College of Computer Science and Software Engineering, Shenzhen University and Guangdong Laboratory of Artificial Intelligence and Digital Economy, Shenzhen, China. E-mail: [wixie, wu]@sza.edu.cn.
- N. Liu is with the College of Engineering, University of Michigan, US. E-mail: liunan@umich.edu.
- L. Chen is with the Department of Computer Science and Engineering, Hong Kong University of Science and Technology, Hong Kong, SAR China. E-mail: leichen@cse.ust.hk.
work is proposed to resort to crowdsourcing for best route selection. The framework successfully leverages the human expertise for the task. The main idea is to first design questions in suitable form for crowdsourcing workers, and then decide the best path with help of the crowdsourced answers. As the query budget is usually limited, the selection of a proper set of Human Intelligence Tasks (HITs) is very important. A series of efficient algorithms are also proposed in [1] to dynamically manage the questions in order to reduce the selection hardness within a limited budget. The sampling-based approach works for best route selection tasks but is very sensitive to the quality and the quantity of the samples. The main reason is that, without considering the probabilistic causalities embedded in the spacial topology, it is actually difficult to precisely estimate the underlying relations merely by sampling.

Therefore, this paper makes the first contribution by proposing a natural way to build up a so-called Selective Bayesian Network as a reasoning tool. The spacial causalities embedded in the network can remarkably control the influence of the noises and sampling bias. Secondly, we propose an effective and efficient algorithm to select the most valuable set of queries for the crowd, with the help of the Selective Bayesian Network. Finally we compare our proposal with several baselines with varying sample size, query batch size, error rate and budget. The experimental result shows that our method dominates others both on simulations and on real datasets.

### 1.1 Candidate Routes and Measurement

As a motivating example, some PhD student who is new to some city needs to go to the university from her apartment every
© 2021 IEEE. Personal use of this material is permitted. Permission from IEEE must be obtained for all other uses, in any current or future media, including eprinting/republishing this material for advertising or promotional purposes, creating new collective works, for resale or redistribution to servers or lists, or reuse of any copyrighted component of this work in other works.

![img-0.jpeg](img-0.jpeg)

Fig. 1. Candidate Routes

morning. A navigation service usually suggests five different paths to her, namely by taxi, Uber, bus, subway and ferry. Taxi and Uber are convenient and comfortable, but quite expensive; while buses and the subway are fairly affordable, but usually slow and crowded; and the ferry is cheapest but also slowest. If the cost of all paths above can be perfectly evaluated by some value function or model, the best path is simply the shortest one. However, such a value function or model is usually absent, as the cost may be influenced by many dynamic factors that are difficult, sometimes impossible, to be quantitatively modeled. Instead, there are only statistics or observations with noises available for the estimation of the best route. To integrate and analyze the complex, multi-sourced statistics via a completely explicit model is quite challenging. However, for humans, experienced drivers for instance, it might be relatively easy to make a quick yet acceptable assessment in such circumstances. Consequently, many systems consider the paths preferred by humans [2], and produce not just one best path, but rather a set of paths. However, to address the 'Painful Options' problem [3], a most likely best route needs to be further selected. In some existing work [4], the task is formalized as predicting the spatial transition patterns of the trips. Several proposals [5], [6] have revealed that the transition patterns of traffic are usually highly skewed and unbalanced: some paths are more likely to be traveled than others. Thus, we follow the problem formalism in [1], [4] and presume a set of candidate routes with a given distribution as the input. It worth mentioning that the payment for the help from the crowd is very important. If the cost is too high, She should simply take a taxi without worrying about the best path. However, the taxi drivers may also be faced with multiple choices of routes, and also potentially need some help from some crowd, for instance other drivers.

The motivating example above can be specifically demonstrated by the distribution in Table 1, over a road network showed in Figure 1. There are totally 5 candidate routes from s to t, with the probabilities of being the best route 0.1, 0.1, 0.4, 0.1, 0.3, respectively. We first have to give a measurement to quantify the hardness selecting the best one from these candidates. As in many previous research work [1], [7], [8], we consider the best route as a discrete random variable defined over the set of the candidate paths, and use the Shannon entropy to measure the selection hardness. For a given candidate value set S for discrete random variable x, the entropy of x is H = −∑s∈S Pr(x = s) log Pr(x = s). So for a given set of candidate routes R, the selection hardness of the best route BR, denoted by H(BR), is

$$H(BR) = -\sum_{R \in \mathbb{R}} Pr(BR = R) \cdot \log Pr(BR = R) \tag{1}$$

In the rest of the paper, we use Pr(R) as the abbreviation of Pr(BR = R). If the distribution over the candidate paths is relatively skewed, i.e. there is some route with a dominant probability to be the best route, then the hardness of the selection is quite low, as well as the entropy. In particular, if the candidate set is a singleton, the entropy is 1·log1 = 0, i.e. there is no difficulty at all to select the best route. When the distribution over the candidates is quite balanced, the selection is quite difficult, and the entropy value is the highest given a uniform distribution. In the example above in Figure 1, the hardness of selecting the best route is H(BR) = −(3·0.1·log 0.1+0.4·log 0.4+0.3·log 0.3) = 0.616.

It worth mentioning that the distribution of the candidate paths can be obtained in multiple ways. There have been many related research works. A straightforward idea is to use the historical trajectory data. In [2], the distribution is inferred by mining the frequent paths chosen by experienced drivers. It is also reasonable to let the user to initialize the distribution according to personal preference [9]. For a recommendation system integrated with multiple routing algorithms, a possible way is to train and test the algorithms on a large number of queries, and each of the methods is assigned with a probability based on its average performance. For some learning-based method, e.g. deep reinforcement learning [10], the output is already a distribution of candidate choices. For instance in [4], a deep probabilistic model is proposed to predict the most likely traveling route on the road network, which unifies three key explanatory factors. To enable effectively sharing the statistical strength, they also proposed an adjoin generative model to learn representations of k-destination proxies. In this paper, we assume that the distribution of the routes has already been given by some of the above methods.

### 1.2 Crowd-Aided Best Path Selection

To leverage human expertise for the route selection, we need to first determine a HIT (Human Intelligent Task) design. We follow the design of the crowdsourcing task and the queries in our previous work [1]. A Human Intelligence Task (HIT) is in the form of a Routing Query, which is a tuple (vs, C, vsg), where vs is the starting vertex of the query, C is the set of candidate directions, and vsg is the target vertex. Intuitively, such a query Q is asking that, if the current position is at the starting vertex vs, in order to reach the target vertex vsg, which direction in the candidate set C should be chosen. In Table 1, there are three

TABLE 1 Route Distribution and Routing Queries


routing queries: $Q_{1}, Q_{2}$ and $Q_{3}$, each of which contains a starting vertex, a target vertex, and a candidate set of next directions. For instance, $Q_{2}$ is a query about which direction to choose to get to $t$, if one is currently at $v_{1}$. There are two choices available, either to go through $v_{3}$ and then to $t$, or directly go to $t$. The crowdsourcing task is to give an answer, denoted by $A_{Q_{2}}$, which is either $v_{3}$ or $t$.

Please notice that there is a probability mass function (pmf) available in the table, which decides the probabilities of different crowdsourced answers for some given $Q$. The probability mass function needs to submit to the distribution of the candidate routes $R S$. Once the distribution is given, the pmf can be determined. The distribution and the pmf can be regarded as the long-term statistics. For example, without any observation at a specific time, the probability of the best route in Figure 1 to be $R_{1}$ is statistically 0.1 , and the probability of $A\left(Q_{1}\right)=v_{1}$ is statistically 0.2 . However, if a crowdsourcing worker has been placed in a specific environment where the best route is already deterministic, which is $R_{3}$ for instance, i.e. with the observation $B R=R_{2}$, the probability of $A\left(Q_{1}\right)=v_{1}$ then becomes 0 , and $\operatorname{Pr}\left(A\left(Q_{1}\right)=v_{2}\right)$ is 1 , if noises are not concerned. It is commonly accepted that crowdsourcing works best when the human intelligent tasks can be decomposed into very simple pieces [11]. So asking which closely next direction is the best choice, as what we did, is much better than generally asking which route is the best one. Moreover, the knowledge about the traffic condition sometimes comes from real-time observation, which is usually partial - a human driver despite his/her rich experience is only able to observe the traffic condition in a limited scope. With the simple pieces of the tasks, the crowdsourcing workers can make use of their expertise or realtime observation easily.

The crowdsourced answers for the simple tasks are then collected and integrated for updating the distribution of the routes. In [1], the query above can be further decomposed into smaller pieces, namely binary routing queries (BRQ). Each $Q=\left(v_{s t}, C, v_{t g}\right)$ can be broken down into $B Q \mathrm{~s}$, each of which contains a singleton candidate direction set, and the answer is either yes or no. For instance, $Q_{1}$ in Table 1 is decomposed into $B Q_{1}, B Q_{2}$ and $B Q_{3}$, and $Q_{2}$ is decomposed into $B Q_{4}$ and $B Q_{5}$. A binary routing query set is easier for the crowd to answer, yet in expressiveness and efficiency it is equivalent with the corresponding routing query set. The framework of crowdaided route selection [1] is as follows: given a route set $\mathbb{R}$ and a budget limit $B$ of RQ numbers,

1) select $k$ queries (denoted as $S_{k}$ ) to ask the crowd, to reduce the selection hardness as much as possible,
2) update the probabilities of all routes in $\mathbb{R}$ according to the crowdsourced $k$ answers (denoted as $A_{S_{k}}$ ),
3) repeat 1 and 2 until budget of $B$ is used up, and then report the most likely best route.
In [1], the selection of the best set of queries is done by a samplingbased approach, which estimates the mutual information between $B R$ and $A_{S_{k}}$ by sampling. It neglects spacial relationship between $B R$ and $A_{S_{k}}$, resulting that the performance is very sensitive to the quality and size of the sample set. In this paper we propose a method to address the problem.

### 1.3 Challenges and Contributions

We present the challenges in the following aspects.

- Idleness of topological information: a main challenge is how to utilize the spacial information in the map, to
accelerate the hardness reduction of selecting the best route. Generally, the routing queries that are given to the crowd are not independent with each other, which makes it very difficult to precisely evaluate different combinations of queries. It is crucial to find an efficient way to make use of the topological causalities among the queries when we compute the mutual information between the selection hardness and the crowdsourced answers.
- Uncertainty from noises and sampling bias: existing sampling-based algorithm suffers from the possible noises in the crowdsourced answers and sample insufficiency. As the answers from the crowd are not always correct, the bias in the samples might be magnified by the noises, in particular when the sample size is not large enough. Thus, we need to find an effective mechanism to control the uncertainty brought about by the error of the crowd.
- Computational complexity on large maps: suppose that we have already known how to leverage the spacial information for the route selection, the efficiency is another important concern. As the given map might be quite large in reality, the designed algorithm has to be highly efficient for online usage.

To address the problems above, we propose a new approach for crowd-aided route selection. We summarize our new contributions as follows:

- Firstly, we give the exact solution for selecting the optimal $k$ RQs in the framework of crowd-aided route selection. We propose a so-called Selective Bayesian Network for representing and leveraging the knowledge of spacial causalities, and propose a natural method to build the networks, as described in detail in Section 4.2.
- Secondly, we propose an efficient algorithm that selects most valuable routing queries and then suggests best routes, by reasoning on the Selective Bayesian Network, which successfully reduces the uncertainty yielded by the sampling bias and the noises in the crowdsourced answers, as presented in Sections 4.3 and 4.4.
- Thirdly, we modularize the algorithm to enable topological information reuse, thus improve the efficiency of the hardness reduction, as illustrated in Section 4.4.
- Finally, we compare different algorithms both on synthetic data and real-world road networks with varying sample size, query batch size, error rate and budget. It turns out that our approach dominates others, as shown in Section 5.


## 2 Definitions and Problem Statement

In this section, we present the core definitions and related notations, then formally state the problem.

Definition 2.1. Given a source vertex $s$ and a target vertex $t$ over a directed graph $G$, a candidate route is a sequence of edges $R=\left(e_{1}, \ldots, e_{n}\right)$, such that $s$ is the head of $e_{1}, t$ is the tail of $e_{n}$, and the sequence $e_{1}, \ldots, e_{n}$ is a directed path in $G$.

For a given vertex $v$ and a candidate path $R$, if $R$ goes through $v$, we denote it as $R \rightarrow v$, and $R \nrightarrow v$ denotes that $R$ does not go through $v$. For an edge $e=\left(v_{i}, v_{j}\right)$ in $G$ such that $R \rightarrow v_{i}$ and $R \rightarrow v_{j}$, i.e. $R$ goes through edge $e$, we simply denote it as $e \in R$.

Definition 2.2. Given a source vertex $s$ and a target vertex $t, \mathbb{R}$ denotes the set of all candidate routes from $s$ to $t$. The best route, denoted by $B R$, is defined as a discrete random variable with sample space $\mathbb{R}$. Each candidate route $R \in \mathbb{R}$ has a probability $\operatorname{Pr}(R)$ of being the best one, and $\sum_{R \in \mathbb{R}} \operatorname{Pr}(R)=1$.
Definition 2.3. Given a Route Set $R S$ with the source vertex $s$ and the target vertex $t$, a Routing Query $Q$ is defined as a triple $\left(v_{s t}, C, t\right)$, where $v_{s t}$ is the starting vertex of the query, indicating an intersection, and $C=\left\{v_{1}, \ldots, v_{|C|}\right\}$ is the set of all successors of $v_{s t}$ in $\mathbb{R}$, namely, all possible directions of moving from $v_{s t}$ towards $t$. In the rest of the paper, by default $|C| \geq 2$, i.e. only those vertices with at least two successors are worth querying about.

Given a route set $\mathbb{R}$, we use $\mathbb{Q}$ to denote the set of all queries in $\mathbb{R}$. For a set of queries $S_{k} \in \mathbb{R}$ that is selected to ask, suppose that $S_{k}=\left\{Q_{1}, Q_{2}, \ldots, Q_{k}\right\}$ the crowdsourced answer set $A_{S_{k}} \in C_{S_{k}}$, where $C_{S_{k}}=C_{Q_{1}} \times \ldots \times C_{Q_{k}}$. The error rate of the crowdsourcing workers is denoted by $\varepsilon$. Table 2 summarizes the notations. In Figure 1 and Table 1, $\mathbb{R}=\left\{R_{1}, R_{2}, R_{3}\right\}$, and suppose that $B R=R_{4}$. Let $k=2$ and $S_{k}=\left\{Q_{1}, Q_{3}\right\}$. As $v_{1}$ is the starting vertex of $Q_{2}$ and $B R \nrightarrow v_{1}$, the crowdsourcing worker gives random answer according to the probability mass function over $C_{2}$, namely, $v_{3}$ with probability 0.5 , or otherwise $v_{4}$. For the starting vertex $v_{2}$ of $Q_{3}, B R \rightarrow v_{2}$ and $\left(v_{2}, v_{4}\right) \in B R$, a worker with error rate $\varepsilon$ answers $v_{4}$ with probability $(1-\varepsilon)$, or answers $t$ with probability $\varepsilon$.

Similar as in [1], we use the Shannon Entropy, which is a non-parametric measurement that requires no assumption about external factors, to measure the hardness of selecting $B R$ from $\mathbb{R}$.

Definition 2.4. Given a path set $\mathbb{R}=\left\{R_{1}, R_{2}, \ldots, R_{|\mathbb{R}|}\right\}$, the hardness of selecting the best path $B R$, denoted by $H(B R)$, is defined as the Shannon Entropy of $B R$,

$$
H(B R)=-\sum_{R \in \mathbb{R}} \operatorname{Pr}(R) \log (\operatorname{Pr}(R))
$$

We formally state the problem definition as follows.
Definition 2.5. (Problem definition) Given a path set $\mathbb{R}$ and a budget $B$ of the number of queries, without exceeding the budget, we aim to design strategies to crowdsource routing queries in order to maximally reduce the selection hardness $H(B R)$.

## 3 BASIC RQ-BASED Method

In this section, we present a complete solution to select and crowdsource RQs in order to reduce the selection hardness. First, we use the expected reduction of selection hardness as the metric to evaluate RQs, and derive necessary formulas to enable the computation. Second, we study how to efficiently select the best RQ. Third, we present how to utilize conflicting crowdsourced answers. Lastly, we put these together to develop the framework of the RQ-based method, which reduces the selection hardness using a sequence of RQs.

### 3.1 RQ Selection Metric

In order to design an effective strategy for selecting RQs, it is essential to define a metric to estimate the importance of RQs before they are answered. Since the final objective is to reduce

TABLE 2
Summary of Notations


the selection hardness, we use the probabilistic expectation of selection hardness conditioned on individual RQs as the metric.

For an arbitrary routing query $Q:=<v_{s t}, D, t>$, let $A_{Q}$ be the ground truth answer of the $Q$. Probabilistically, $A_{Q}$ is a discrete random variable with sample space $D$. Therefore, the expectation of selection hardness after receiving $A_{Q}$, denoted as $\mathbb{E} H\left(B R \mid A_{Q}\right)$, is that

$$
\begin{aligned}
& \mathbb{E} H\left(B R \mid A_{Q}\right) \\
= & \sum_{v_{i} \in D} \operatorname{Pr}\left(A_{Q}=v_{i}\right) H\left(B R=R \mid A_{Q}=v_{i}\right) \\
= & \sum_{v_{i} \in D} \operatorname{Pr}\left(A_{Q}=v_{i}\right) \sum_{R_{j} \in \mathbb{R}}\left(\operatorname{Pr}\left(B R=R_{j} \mid A_{Q}=v_{i}\right)\right. \\
& \left.\quad \log \operatorname{Pr}\left(B R=R_{j} \mid A_{Q}=v_{i}\right)\right)
\end{aligned}
$$

There are two parameters used in Equation $25: \operatorname{Pr}\left(A_{Q}=\right.$ $\left.v_{i}\right)$ (i.e. the probability that $v_{i}$ is the correct answer of $Q$ ) and $\operatorname{Pr}\left(B R=R_{j} \mid A_{Q}=v_{i}\right)$ (i.e. the probability that $R_{j}$ is the best path, given that $v_{i}$ is the correct answer of $Q$ ). Now we derive formulas to compute these two parameters.

Computation of $\operatorname{Pr}\left(\mathbf{A}_{\mathbf{Q}}=\mathbf{v}_{\mathbf{i}}\right)$ : Recall that RQ is a question asking how to move forward starting from $v_{s t}$. Hence, $A_{Q}=v_{i}$ indicates $e:=\left(v_{s t}, v_{i}\right) \in B R$, given $B R$ goes through $v_{s t}$. Then we have

$$
\begin{aligned}
& \operatorname{Pr}\left(A_{Q}=v_{i}\right)=\operatorname{Pr}(e \in B R \mid B R \rightarrow v_{s t}) \\
& =\frac{\operatorname{Pr}\left(B R \rightarrow v_{s t} \mid e \in B R\right) \operatorname{Pr}(e \in B R)}{\operatorname{Pr}\left(B R \rightarrow v_{s t}\right)}
\end{aligned}
$$

Please note that $v_{s t}$ is the head of edge $e$, so given the condition that $e$ is on the best path (i.e. $e \in B R$ ), the best path must go through $v_{s t}$, that is, $\operatorname{Pr}\left(B R \rightarrow v_{s t} \mid e \in B R\right)=1$. Hence, we have

$$
\operatorname{Pr}\left(A_{Q}=v_{i}\right)=\frac{\operatorname{Pr}(e \in B R)}{\operatorname{Pr}\left(B R \rightarrow v_{s t}\right)}
$$

Following the Law of Total Probability [12], we have $\operatorname{Pr}(e \in$ $B R)=\sum_{R \in \mathbb{R}} \operatorname{Pr}(e \in B R \cap B R=R)=\sum_{R \in \mathbb{R} \wedge e \in R} \operatorname{Pr}(R)$

and $\operatorname{Pr}\left(B R \rightarrow v_{s t}\right)=\sum_{R^{\prime} \in \mathbb{R}} \operatorname{Pr}\left(R^{\prime} \rightarrow v_{s t} \cap B R=R^{\prime}\right)=$ $\sum_{R^{\prime} \in \mathbb{R} \wedge R^{\prime} \rightarrow v_{s t}} \operatorname{Pr}\left(R^{\prime}\right)$. Finally, we have

$$
\operatorname{Pr}\left(A_{Q}=v_{i}\right)=\frac{\sum_{R \in \mathbb{R} \wedge e \in R} \operatorname{Pr}(R)}{\sum_{R^{\prime} \in \mathbb{R} \wedge R^{\prime} \rightarrow v_{s t}} \operatorname{Pr}\left(R^{\prime}\right)}
$$

Equation 3 computes the probability that $A_{Q}$ taking each element of $D$, hereby we have the probability mass function (pmf) [12] of $A_{Q}$.

Computation of $\operatorname{Pr}\left(\mathbf{B R}=\mathbf{R}_{\mathbf{j}} \mid \mathbf{A}_{\mathbf{Q}}=\mathbf{v}_{\mathbf{i}}\right)$ : The main difficulty of deriving $\operatorname{Pr}\left(B R=R_{j} \mid A_{Q}=v_{i}\right)$ is to determine the correlation between ' $B R=R_{j}$ ' and ' $A_{Q}=v_{i}$ '. We observe that this correlation is closely related to ' $B R \rightarrow v_{s t}$ ', i.e. whether the best path goes through the starting point of RQ. Therefore, we expand $\operatorname{Pr}\left(B R=R_{j} \mid A_{Q}=v_{i}\right)$ with the Law of Total Probability as follows:

$$
\begin{aligned}
& \operatorname{Pr}\left(B R=R_{j} \mid A_{Q}=v_{i}\right)= \\
& \operatorname{Pr}\left(B R \rightarrow v_{s t}\right) \operatorname{Pr}\left(B R=R_{j} \mid A_{Q}=v_{i}, B R \rightarrow v_{s t}\right) \\
& +\left(1-\operatorname{Pr}\left(B R \rightarrow v_{s t}\right)\right) \operatorname{Pr}\left(B R=R_{j} \mid A_{Q}=v_{i}, B R \nrightarrow v_{s t}\right)
\end{aligned}
$$

where we have $\operatorname{Pr}\left(B R \rightarrow v_{s t}\right)=\sum_{R \in \mathbb{R} \wedge R \rightarrow v_{s t}} \operatorname{Pr}(R)$.
We derive $\operatorname{Pr}\left(B R=R_{j} \mid A_{Q}=v_{i}, B R \rightarrow v_{s t}\right)$ and $\operatorname{Pr}\left(B R=R_{j} \mid A_{Q}=v_{i}, B R \nrightarrow v_{s t}\right)$ by respectively analyzing two exclusive conditions - $B R \rightarrow v_{s t}$ and $B R \nrightarrow v_{s t}$.

Condition $B R \rightarrow v_{s t}$ : First, we analyze the situation that $v_{s t}$ is on the best path $\overline{B R}$. For each $v_{i} \in D$, if edge $e:=\left(v_{s t}, v_{i}\right)$ is on the best path, then $v_{i}$ must be the best direction going from $v_{s t}$ to $t$, i.e. the ground truth answer $A_{Q}$ should be $v_{i}$. Therefore, we have $e \in B R \Rightarrow A_{Q}=v_{i}$.

Similarly, if $A_{Q}=v_{i}$ and $B R \rightarrow v_{s t}$, we can ensure that $e \in B R$. So $\left(A_{Q}=v_{i} \wedge B R \rightarrow v_{s t}\right) \Rightarrow e \in B R$. Overall, we conclude that $e \in B R$ if and only if $\left(A_{Q}=v_{i} \wedge B R \rightarrow v_{s t}\right)$, i.e.

$$
\left(A_{Q}=v_{i} \wedge B R \rightarrow v_{s t}\right) \Leftrightarrow e:=\left(v_{s t}, v_{i}\right) \in B R
$$

Therefore, we have

$$
\begin{aligned}
& \operatorname{Pr}\left(B R=R_{j} \mid A_{Q}=v_{i}, B R \rightarrow v_{s t}\right) \\
& =\operatorname{Pr}\left(B R=R_{j} \mid e:=\left(v_{s t}, v_{i}\right) \in B R\right) \\
& =\frac{\operatorname{Pr}(e \in B R \mid B R=R_{j}) \operatorname{Pr}\left(R_{j}\right)}{\operatorname{Pr}(e \in B R)} \\
& = \begin{cases}0 & e \notin R_{j} \\
\frac{\operatorname{Pr}\left(R_{j}\right)}{\sum_{R \in \mathbb{R} \wedge e \in R} \operatorname{Pr}(R)} & \text { otherwise }\end{cases}
\end{aligned}
$$

Condition $B R \nrightarrow v_{s t}$ : Second, we consider the condition when the best path does not go through $v_{s t}$. Note each vertex in $D$ indicates a path that is possibly the best direction going from $v_{s t}$ to $t$, and we are interested in the best path from the source vertex $s$ to $t$. Therefore, the answer to RQ gives us useful information only if $v_{s t}$ is known to be on the best path. In other words, if $v_{s t}$ is not on $B R$, how to move from $v_{s t}$ towards the target does not affect the distribution of $B R$, since one will not even go to $v_{s t}$ in the first place. Probabilistically, $B R$ and $A_{Q}$ are independent given that ' $B R$ does not go through $v_{s t}$ '. Formally, we have

$$
A_{Q} \perp B R \mid B R \nrightarrow v_{s t}
$$

where we adopt $\perp$ to denote the operator indicating two random variables are conditionally independent [13].

From Formula 7, we have

$$
\begin{aligned}
& \operatorname{Pr}\left(B R=R_{j} \mid A_{Q}=v_{i}, B R \nrightarrow v_{s t}\right) \\
& = \begin{cases}0 & R_{j} \rightarrow v_{s t} \\
\frac{\operatorname{Pr}\left(R_{j}\right)}{\sum_{R \in \mathbb{R} \wedge R \nrightarrow v_{s t}} \operatorname{Pr}(R)} & \text { otherwise }\end{cases}
\end{aligned}
$$

Then, equipped with Equation 8 and 6, we have completed the derivation of parameters used in Equation 30.

Finally, by substituting Equation 30 and 3 into Equation 25, we can compute the expectation of selection hardness for asking each RQ.

### 3.2 Choosing the best RQ

A naive approach of selecting the best RQ is to traverse all the RQs. However, this is very costly since the computation w.r.t. RQ requires accessing all the paths in $\mathbb{R}$. When the number of candidate paths is large, the computational cost will be higher. Fortunately, we found that the expected reduction of selection hardness for $R Q:=<v_{s t}, D, t>$ is only related to the paths going through $v_{s t}$. We conclude this discovery with the following theorem.

Theorem 3.1. For a given path set $\mathbb{R}$ and a given $R Q:=<$ $v_{s t}, D, t>$, let $\Delta H_{R Q}$ be the expected reduction of selection hardness by asking $R Q$ to the crowd, we have that $\Delta H_{R Q}$ is equivalent to 'the entropy of RQ' multiplying 'the probability of the best path going through $v_{s t}$ ', i.e.

$$
\begin{aligned}
& \Delta H_{R Q}=H(B R)-\mathbb{E} H\left(B R \mid A_{Q}\right) \\
& =-\left(\sum_{R \rightarrow v_{s t}} \operatorname{Pr}(R)\right) \sum_{v_{i} \in D} \operatorname{Pr}\left(A_{Q}=v_{i}\right) \log \operatorname{Pr}\left(A_{Q}=v_{i}\right)
\end{aligned}
$$

Proof. Please see the appendix in [1].
Theorem 3.1 reflects two factors influencing the importance of a RQ - 'the entropy of the RQ' and 'the probability of the best path going through $v_{s t}$ '. Intuitively, the former indicates the amount of information gain by asking this question, so the higher the entropy, the more important the question; the latter indicates the structural position of the question, representing how useful the information gain is for determining the best path. It worth noticing that, the common practice 'asking the most uncertain question' does NOT apply in our problem, as shown in the following example.

### 3.3 Utilization of Conflicting Crowdsourced Answers

The essential objective of crowdsourcing is to use the answers to adjust the probability distribution of the best path. However, crowdsourced answers may be mistaken or subjective. As a result, different workers may return conflicting answers for the same question. To handle this issue, we must allow each crowdsourced answer to be wrong with a probability. This probability can be estimated by the error rate of the worker. For a $R Q:=<v_{s t}, D, t>$, let $v_{C}$ be the result returned by a crowdsourcing worker with error rate $\epsilon$.

Now we present how to use crowdsourced answers to adjust the probability of each candidate path $R_{i}$. That is to derive the formula to compute $\operatorname{Pr}\left(B R=R_{i} \mid v_{C}\right.$ returned by the crowd $)$. To do this, we need to consider three exclusive cases: 1) $R_{i} \nrightarrow v_{s t}$,

i.e. $R_{i}$ does not go through $v_{s t}$, so $R_{i}$ is not affected by the answer of the RQ; 2) $\left(v_{s t}, v_{C}\right) \in R_{i}$, i.e. $R_{i}$ goes through $v_{s t}$ and $v_{C}$, which indicates that the crowdsourced answer is supportive for $R_{i}$; 3) $R_{i} \rightarrow v_{s t} \wedge\left(v_{s t}, v_{C}\right) \notin R_{i}$, i.e. $R_{i}$ goes through $v_{s t}$ but not $v_{C}$, which indicates that the crowdsourced answer is against for $R_{i}$.

We list the details for all three cases as follows.
Case 1) $B R \nrightarrow v_{s t}$ : According to Equation 7, the answer of RQ is independent of $B R$ given $B R \nrightarrow v_{s t}$, so we have $\operatorname{Pr}\left(B R=R_{i} \mid v_{C}\right.$ returned by the crowd $)=\operatorname{Pr}(B R=$ $\left.R_{i}\right)=\operatorname{Pr}\left(R_{i}\right)$;

Case 2) $\left(v_{s t}, v_{C}\right) \in R_{i}$ : According to Bayes' theorem

$$
\begin{aligned}
& \operatorname{Pr}\left(B R=R_{i} \mid v_{C}\right. \text { returned by the crowd) } \\
& =\frac{\operatorname{Pr}\left(R_{i}\right) \operatorname{Pr}\left(v_{C}\right. \text { returned by the crowd }\left|B R=R_{i}\right)}{\operatorname{Pr}\left(v_{C}\right.} \text { returned by the crowd })
\end{aligned}
$$

We have

$$
\begin{aligned}
& \operatorname{Pr}\left(v_{C}\right. \text { returned by the crowd })= \\
& \quad \operatorname{Pr}\left(A_{Q}=v_{C}\right)(1-\epsilon)+\left(1-\operatorname{Pr}\left(A_{Q}=v_{C}\right)\right) \epsilon \\
& \operatorname{Pr}\left(v_{C}\right. \text { returned by the crowd }\left|B R=R_{i}\right)= \\
& \quad \operatorname{Pr}(\text { crowd answers the } R Q \text { correctly })=1-\epsilon
\end{aligned}
$$

So, in case of $\left(v_{s t}, v_{C}\right) \in B R$, we have

$$
\begin{aligned}
& \operatorname{Pr}\left(B R=R_{i} \mid v_{C}\right. \text { returned by the crowd })= \\
& \quad \frac{\operatorname{Pr}\left(R_{i}\right)(1-\epsilon)}{\operatorname{Pr}\left(A_{Q}=v_{C}\right)(1-\epsilon)+\left(1-\operatorname{Pr}\left(A_{Q}=v_{C}\right)\right) \epsilon}
\end{aligned}
$$

where $\operatorname{Pr}\left(A_{Q}=v_{C}\right)$ is derived in Equation 3.
Case 3) $R_{i} \rightarrow v_{s t} \wedge\left(v_{s t}, v_{C}\right) \notin R_{i}$ : Analogous to case 2), since $\left(v_{s t}, v_{C}\right) \notin R_{i}$ and $\left(v_{s t}, v_{C}\right) \notin B R$, we know that $v_{C}$ is an incorrect answer of RQ conditioning on $B R=R_{i}$, i.e. the crowd answers RQ correctly. So,

$$
\begin{aligned}
& \operatorname{Pr}\left(v_{C}\right. \text { returned by the crowd }\left|B R=R_{i}\right)= \\
& \operatorname{Pr}(\text { crowd answers the } R Q \text { incorrectly })=\epsilon
\end{aligned}
$$

Then we have

$$
\begin{aligned}
& \operatorname{Pr}\left(B R=R_{i} \mid v_{C}\right. \text { returned by the crowd })= \\
& \quad \frac{\operatorname{Pr}\left(R_{i}\right) \epsilon}{\operatorname{Pr}\left(A_{Q}=v_{C}\right)(1-\epsilon)+\left(1-\operatorname{Pr}\left(A_{Q}=v_{C}\right)\right) \epsilon}
\end{aligned}
$$

To conclude the above analysis, we achieve the following close-form formula for using crowdsourced answer to adjust the probability distribution of the best path:

$$
\begin{array}{ll}
\operatorname{Pr}\left(B R=R_{i} \mid v_{C}\right. & \text { returned by the crowd })= \\
& \left\{\begin{array}{lr}
\operatorname{Pr}\left(R_{i}\right) & R_{i} \nrightarrow v_{s t} \\
\frac{\operatorname{Pr}\left(R_{i}\right)(1-\epsilon)}{\operatorname{Pr}\left(A_{Q}=v_{C}\right)(1-\epsilon)+\left(1-\operatorname{Pr}\left(A_{Q}=v_{C}\right)\right) \epsilon} & \left(v_{s t}, v_{C}\right) \in R_{i} \\
\frac{\operatorname{Pr}\left(R_{i}\right) \epsilon}{\operatorname{Pr}\left(A_{Q}=v_{C}\right)(1-\epsilon)+\left(1-\operatorname{Pr}\left(A_{Q}=v_{C}\right)\right) \epsilon} & \text { otherwise }
\end{array}\right.
\end{array}
$$

Actually, by considering $R_{i}$ as a binary random variable, $\operatorname{Pr}\left(R_{i} \mid v_{C}\right)$ is the probability of $B R=R_{i}$ conditioning on event " $v_{C}$ is answered by the crowd". Therefore, when more answers are received, the probability of $B R=R_{i}$ would be recursively adjusted by Equation 14, conditioning on each received answer and error rate of the corresponding worker. Please note that different workers may have different error rates. Furthermore, after the probabilities of candidate paths are adjusted by one

Input: A path set $\mathbb{R}, U_{R Q}$, a total budget $B$ while $B \neq 0$ do
for each $R Q_{i} \in U_{R Q}$ do
calculate $\Delta H_{R Q_{i}}$ via Theorem 3.1;
end
$R Q_{\max } \leftarrow \operatorname{argmax}_{R Q_{i} \in U_{R Q}} \Delta H_{R Q_{i}} ;$
Ask $R Q_{\max }$ to crowd and receive the corresponding answer $v_{C}$;
for each $R_{j} \in \mathbb{R}$ do
$\operatorname{Pr}\left(R_{j}\right) \leftarrow \operatorname{Pr}\left(B R=R_{j} \mid v_{C}\right)$ via Formula 14);
end
$B \leftarrow B-1 ;$
end
Algorithm 1: The Framework of RQ-based Method
answer, the probability distribution of each $A_{Q}$ is also updated by recomputing Equation 3. So, when the next answer is received, the adjustment is conducted with the updated probability of each $R_{i}$.

It is easy to perform the algebraic manipulations to show that, for any two answers $v_{C}$ and $v_{C}^{\prime}$, we have

$$
\begin{aligned}
& \operatorname{Pr}\left(B R=R_{i} \mid v_{C}\right. \text { returned by the crowd, } \\
& \text { and then } v_{C}^{\prime} \text { returned by the crowd) } \\
= & \operatorname{Pr}\left(B R=R_{i} \mid v_{C}^{\prime}\right. \text { returned by the crowd, } \\
& \text { and then } v_{C} \text { returned by the crowd) } \\
= & \operatorname{Pr}\left(B R=R_{i} \mid v_{C}\right. \text { and } v_{C}^{\prime} \text { are returned by the crowd) }
\end{aligned}
$$

The above equation resolves three issues of concern. The first is the sequence of answers received from workers. Equation 15 indicates that, given two crowdsourced answers, the final result of $\mathbb{R}$ is independent of the sequence of the answers being utilized. In other words, the final result of $R_{i}$ is the probability of $B R=R_{i}$ conditioning on the event that "both answers are received". The second issue is that, the same RQ may be answered differently by multiple workers. Particularly, in Equation 15, $v_{C}^{\prime}$ and $v_{C}$ may be conflicting answers for the same RQ from two workers. In this case, by recursively executing Equation 14 twice, the effect of $v_{C}$ and $v_{C}^{\prime}$ are gracefully aggregated based on different error rates of workers. Third, after the utilization of crowdsourced answers, the sum of probabilities of all candidate paths should always be one. As follows, we show how to use a crowdsourced answer with a running example.

### 3.4 The Framework of RQ-based Method

In this subsection, we provide the complete framework of our proposed RQ-based method. Algorithm 1 illustrates this framework, which consists of two iterative phases:

- Choosing the best $R Q$ - select the best RQ based on the current probabilities of candidate paths, and post it to the crowd;
- Utilization of Conflicting Crowdsourced Answers - adjust the probabilities of all candidate paths according to the crowdsourced answers.

In Algorithm 1, these two phases are iteratively performed $B$ times due to the given budget. In each iteration, we firstly calculate the expected reduction of selection hardness, $\Delta H_{R Q}$, for each RQ via Theorem 3.1. Then, the one with maximum $\Delta H_{R Q}$ is selected and published to the crowd. Second, we receive the answer $v_{C}$, and adjust the probabilities of all candidate paths through Formula 14, hereby reduce the selection hardness.

![img-1.jpeg](img-1.jpeg)

Fig. 2. Crowd-aided route selection with Selective Bayesian Network

### 3.5 BRQ: A Different Question Type

In the RQ-based method, each RQ is a multiple choice question. For a high-degree vertex, it would be constructed into a multiple choice with too many options to be answered by a crowdsourcing worker. As suggested in [14], [15], crowds are good at tasks broken down into small pieces (often with a YES/NO answer). Motivated by this, we consider an extension that uses an easier type of questions, namely BRQ, as defined by the following Definition 3.1.

Definition 3.1 (Binary Routing Query (BRQ)). For a given $R Q:=<v_{s t}, D=\left\{v_{0}, \ldots, v_{|D|}\right\}, t>$, a Binary Routing Query $B R Q$ is triple $<v_{s t}, v_{d}, t>$, where $v_{d} \in D$.

From the perspective of a crowdsourcing worker, a BRQ is a question of the form "From $v_{s t}$ to $t$, should I go to the direction of $v_{d}$ ?" The bottom part of Table 1 lists all the BRQs for the $\mathbb{R}$. It is obvious that each RQ can be easily decomposed in to $|D|$ distinct BRQs. As a new type of questions, BRQs can easily fit into the Algorithm 1. Analogous to the RQ-based method, we also focus on studying how to select the best BRQ in this extension.

Finding the best BRQ: As shown in Theorem 3.1, the significance of an RQ is determined by its information gain and topological position. For BRQs, we reach similar result, as shown with the following theorem.

Theorem 3.2. For a given path set $\mathbb{R}$ and a given $B Q:=<$ $v_{s t}, v_{d}, t>$, let $\Delta H_{B Q}$ be the expected reduction of selection hardness by asking the $B R Q$ to the crowd, we find that $\Delta H_{B Q}$ is equivalent to 'the entropy of the BRQ' multiplying 'the probability of the best path going through $v_{s t}$ ', that is

$$
\begin{aligned}
& \Delta H_{B R Q}=H(B R)-\mathbb{E} H\left(B R \mid A_{B Q}\right) \\
& =-\left(\sum_{R \rightarrow v_{s t}} \operatorname{Pr}(R)\right)\left[\operatorname{Pr}\left(A_{B Q}=v_{d}\right) \log \operatorname{Pr}\left(A_{B Q}=v_{d}\right)\right. \\
& \left.+\left(1-\operatorname{Pr}\left(A_{B Q}=v_{d}\right)\right) \log \left(1-\operatorname{Pr}\left(A_{B Q}=v_{d}\right)\right)\right]
\end{aligned}
$$

Proof. Please see appendix in [1].

## 4 Select the Best Set of RQs with Selective BAYESIAN NETWORK

In this section, we present the crowd-aided route selection with Selective Bayesian Network. Figure 2 shows the architecture of the system. As a centric part of the framework, the Selective Bayesian Network repeatedly selects the best set $S_{k}$ of $k$ routing queries from the query set $\mathbb{Q}$, according to current probabilities of the routes in $\mathbb{R}$. Each selected $S_{k}$ is given to the crowd, and the $k$
answers with noises are then collected from the crowd to update the probabilities and the network. When the budget runs out, the system returns the most likely best route.

### 4.1 RQ Set Selection Metric

Before we formally introduce our approach, we first give the metric. The final objective is to reduce the selection hardness, so we still use the probabilistic expectation of selection hardness conditioned on given set of routing queries as our metric. If the queries are given to the crowd one by one, for a routing query $Q=\left(v_{s t}, C, t\right)$, suppose that the ground truth answer for $Q$ is $A_{Q}$. The answer $A_{Q}$ is actually a discrete random variable with sample space $C$. The expectation of selection hardness after receiving $A_{Q}$, denoted as $\mathbb{E} H\left(B R \mid A_{Q}\right)$, is that

$$
\begin{aligned}
& \mathbb{E} H\left(B R \mid A_{Q}\right) \\
= & \sum_{v \in D} \operatorname{Pr}\left(A_{Q}=v\right) H\left(B R \mid A_{Q}=v\right) \\
= & \sum_{v \in D} \operatorname{Pr}\left(A_{Q}=v\right) \sum_{R \in \mathbb{R}}\left(\operatorname{Pr}\left(B R=R \mid A_{Q}=v\right)\right. \\
& \left.\log \operatorname{Pr}\left(B R=R \mid A_{Q}=v\right)\right)
\end{aligned}
$$

If the problem is to select the best single query $Q$ from $\mathbb{Q}$, such that the expected selection hardness is maximally reduced, the expected reduction of the selection hardness $\Delta H_{S_{k}}$ is

$$
\begin{aligned}
& \Delta H_{Q}=H(B R)-\mathbb{E} H\left(B R \mid A_{Q}\right) \\
& =-\sum_{R \in \mathbb{R}} \operatorname{Pr}(R) \log (\operatorname{Pr}(R))-\sum_{v \in D} \operatorname{Pr}\left(A_{Q}=v\right) H\left(B R \mid A_{Q}=v\right)
\end{aligned}
$$

and we have the optimization problem $\operatorname{argmax}_{Q \in \mathbb{Q}} \Delta H_{Q}$. As a main conclusion of our work in [1], $\Delta H_{Q}$ can be characterized by two features, namely the entropy of $Q$, and the probability of the best path going through $v_{s t}$, where $v_{s t}$ is the starting vertex of $Q$.

$$
\begin{aligned}
& \Delta H_{Q}=H(B R)-\mathbb{E} H\left(B R \mid A_{Q}\right) \\
& =-\left(\sum_{R \rightarrow v_{s t}} \operatorname{Pr}(R)\right) \sum_{v \in C} \operatorname{Pr}\left(A_{Q}=v\right) \log \operatorname{Pr}\left(A_{Q}=v\right)
\end{aligned}
$$

The former feature above indicates the information gain by asking the query $Q$. The higher entropy the query $Q$ has, the more information the answer $A_{Q}$ gives. The latter feature represents the structural importance of the query, indicating how important the information gain is for determining the best route. The two features well captures the essence of crowd-aided route selection with a single best routing query - to select the query with high uncertainty and high spacial importance. However, in a crowdsourcing environment, we usually need to ask multiple questions each round to reduce latency. If we consider giving $k$ queries per round to the crowd, the problem becomes to select the best combination of $k$ routing queries, $S_{k}$, from $\mathbb{Q}$, such that the expected selection hardness is maximally reduced, i.e. the optimization problem

$$
\underset{S_{k} \leq \mathbb{Q},|S_{k}| \leq k}{\operatorname{argmax}} \Delta H_{S_{k}}
$$

where

$$
\Delta H_{S_{k}}=H(B R)-\mathbb{E} H\left(B R \mid A_{S_{k}}\right)
$$

Now the key problem is how to precisely estimate and efficiently compute the expected reduction of selection hardness

after receiving a set of crowdsourced answers. Generally, selecting $S_{k}$ from $\mathbb{Q}$ that maximizes $\Delta H_{S_{k}}$ is NP-Hard, but we can approximate it. From the perspective of information theory [16], $\Delta H_{S_{k}}$ can be considered as the mutual information between $B R$ and $A_{S_{k}}$. The existing work did not give an explicit solution for $\Delta H_{S_{k}}$ above, and the metric was roughly estimated by sampling and the following formula,
$\Delta H_{S_{k}} \approx \Delta \hat{H}_{S_{k}}=\sum_{B R, A_{S_{k}}} f q\left(B R, A_{S_{k}}\right) \log \frac{f q\left(B R, A_{S_{k}}\right)}{f q(B R) \cdot f q\left(A_{S_{k}}\right)}$
where $f q(B R)=\sum_{A_{S_{k}}} f q\left(B R, A_{S_{k}}\right)$ and $f q\left(A_{S_{k}}\right)=$ $\sum_{B R} f q\left(B R, A_{S_{k}}\right)$. To find a better approximation and finally solve the problem, we introduce the Selective Bayesian Network.

### 4.2 Selective Bayesian Network

The baseline sampling-based method in [1] uses two relaxations, one of which calculates approximate solution by greedy strategy, and the other one uses random sampling to estimate the probabilities. If the sampling rate is high enough, the algorithm will give acceptable result in the sense of precision. However, if the sizes of the route set $\mathbb{R}$ and corresponding query set $\mathbb{Q}$ are relatively large, the performance of the sampling-based algorithm dramatically declines due to sampling insufficiency. In the following, we give an alternative approach based on Selective Bayesian Network.

Given a set of candidate routes $\mathbb{R}$, we can construct a corresponding Selective Bayesian Network for the computation of selection hardness reduction $\Delta H_{S_{k}}$. It is obvious that any route that contains a directed loop is not the best route. For instance, for a route $R=v_{1} v_{2} \ldots v_{t}$ where $v_{i}=v_{j}$ for some $i, j \in[1, t], i \neq j, R$ contains a loop $v_{i} v_{i+1} \ldots v_{j}$. Obviously, $R$ is dominated by another route $R^{\prime}=v_{1} v_{2} \ldots v_{i} v_{j+1} \ldots v_{t}$. For any given route $R \in \mathbb{R}$, checking the existence of a loop is an linear-time task, and it's trivial to improve the paths with loops by simply eliminating all loops from them. In the following, we assume that the graph constructed by $\mathbb{R}$ is a directed acyclic graph (DAG), and call $\mathbb{R}$ a directed acyclic graph for convenience.
Definition 4.1. Given a set of routing queries $\mathbb{R}$ that is acyclic, its Selective Bayesian Network, denoted by $\mathcal{N}(\mathbb{R})$, is a DAG that consists of:

Nodes There is a node $v_{i}$ in $\mathcal{N}(\mathbb{R})$ for each vertex $v_{i}$ in $\mathbb{R}$, annotated with the probability of $\operatorname{Pr}\left(v_{i}\right)=$ $\operatorname{Pr}\left(B R \rightarrow v_{i}\right)$, where $B R$ is the best route. In the rest of the paper, we also use $v_{i}$ as a random variable standing for $B R \rightarrow v_{i}$, and $\neg v_{i}$ for $B R \nrightarrow v_{i}$, with probabilities $\operatorname{Pr}\left(v_{i}\right)$ and $1-\operatorname{Pr}\left(v_{i}\right)$ respectively. Each node $v_{i}$ (except the source node $s$ ) is labeled by a conditional probability table $P T\left(v_{i}\right)$. The computation of the probability table $P T$ will be introduced later.
Edges There is a directed edge $\left(v_{i}, v_{j}\right) \in \mathcal{N}(\mathbb{R})$ for each directed edge $\left(v_{i}, v_{j}\right) \in \mathbb{R}$. In the following, we call $v_{i}$ a parent of $v_{j}$, and $v_{j}$ a child of $v_{i}$. Notice that it is possible for a node to have multiple parents and multiple children.
Definition 4.2. For a route set $\mathbb{R}$, its Selective Bayesian Network $\mathcal{N}(\mathbb{R})$, and a node $v \in \mathcal{N}(\mathbb{R})$, we call a set of literals o a priori observation of $v$ if o is in following form:

$$
o=\left\{l_{i} \mid\left(v_{i}, v\right) \in \mathcal{N}(\mathbb{R}), l_{i} \in\left\{v_{i}, \neg v_{i}\right\}\right\}
$$

and define the positive part of the observation o as $o^{+}=$ $\left\{v_{i} \mid v_{i} \in o\right\}$, and the negative part of the observation o as $o^{-}=\left\{\neg v_{i} \mid \neg v_{i} \in o\right\}$.

We denote the set of all priori observations of $v$ by $O(v)$. In Figure 1, for instance,

- $o_{1}=\left\{\neg v_{1}, v_{3}, \neg v_{4}\right\}$ is a priori observation of vertex $t$, i.e. $o_{1} \in O(t)$, with the positive part $o_{1}^{+}=\left\{v_{3}\right\}$ and the negative part $o_{1}^{-}=\left\{\neg v_{1}, \neg v_{4}\right\}$
- $o_{2}=\left\{s, v_{2}\right\}$ is a priori observation of vertex $v_{3}$, i.e. $o_{2} \in O\left(v_{3}\right)$, with the positive part $o_{2}^{-}=\left\{s, v_{2}\right\}$ and negative part $o_{2}^{-}=\emptyset$.
Definition 4.3. For a node $v$ in $\mathcal{N}(\mathbb{R})$, an observation o of $v$, a set of answers $A_{S_{k}}$ for routing query set $S_{k} \subset \mathbb{Q}$, and a route $R \in \mathbb{R}$, we say $R$ submits to $o$, denoted as $R \models o$, if

$$
\left(\forall v_{x} \in o^{+}, R \rightarrow v_{x}\right) \wedge\left(\forall v_{y} \in o^{-}, R \nrightarrow v_{y}\right)
$$

We say $R$ submits to $A_{S_{k}}$, also denoted as $R \models A_{S_{k}}$, if for each query $Q=\left(v_{s t}, C, t\right)$ in $S_{k}$, suppose $v_{\text {ans }}$ is the answer of $Q$ given by $A_{S_{k}}$, we have $R \rightarrow v_{s t} \supset R \rightarrow v_{\text {ans }}$.
The " $\supset$ " above is the implication in classic logic, indicating if the route $R$ goes through $v_{s t}$, then it has to goes through $v_{\text {ans }}$. Now we give the computation of the probability table, denoted by $P T$, of $\mathcal{N}(\mathbb{R})$.
Lemma 4.1 (Computation of probability table $P T$ ). For each node $v_{i} \in \mathcal{N}(\mathbb{R})$,

1) Initialization: for each observation $o \in O\left(v_{i}\right)$, set

$$
\begin{aligned}
& \operatorname{Pr}\left(v_{i} \mid o\right)=\frac{\sum_{R \in \mathbb{R} \wedge R \rightarrow v_{i} \wedge R \models o} \operatorname{Pr}(R)}{\sum_{R \in \mathbb{R} \wedge R \models o} \operatorname{Pr}(R)} \\
& \operatorname{Pr}\left(\neg v_{i} \mid o\right)=1-\operatorname{Pr}\left(v_{i} \mid o\right)
\end{aligned}
$$

2) Completion: for those observation $o \in O\left(v_{i}\right)$ such that $\nexists R \in \mathbb{R} . R \models o$, set $\operatorname{Pr}\left(v_{i} \mid o\right)=0$ and $\operatorname{Pr}\left(\neg v_{i} \mid o\right)=0$.
Note that after the initialization step in Lemma 4.1, the probability table $P T$ is not complete. For instance, Figure 3 shows the the Selective Bayesian Network for the example in Figure 1 with the routing queries in Table 1 (with negative conditional probabilities omitted). In the figure, for node $v_{3}$, the conditional probability $\operatorname{Pr}\left(v_{3} \mid s v_{1} v_{2}\right)$ is still undefined after initialization, since there is no path that submits to the observation of $v_{3}$ : $o=\left\{s, v_{1}, v_{2}\right\}$. So, in the completion step, we complete the probability table $P T\left(v_{3}\right)$ by simply setting $\operatorname{Pr}\left(v_{3} \mid s, v_{1}, v_{2}\right)=0$ and $\operatorname{Pr}\left(\neg v_{3} \mid s, v_{1}, v_{2}\right)=1$, and other necessary conditional probabilities.

We give some more examples of the supportive probabilities:

- For a node $v_{i}$ in $\mathbb{R}$, there is only one outgoing edge from $v_{i}$. Namely, in the routing query $R Q=<v_{i}, D_{i}, t>$, $D_{i}$ is a singleton, say $D_{i}=\left\{v_{\text {out }}\right\}$, we have $\operatorname{Pr}\left(A_{Q}=\right.$ $\left.v_{\text {out }}\right)=1$, though such a query is usually omitted in $U_{R Q}$.
- For a node $v_{i}$ in $\mathbb{R}$, there is only one incoming edge towards $v_{i}$, say $v_{s t}$. The corresponding supportive probabilities will be,

$$
\begin{aligned}
& \operatorname{Pr}\left(v_{i} \mid\left\{v_{s t}\right\}\right)=\operatorname{Pr}\left(A_{<v_{s t}, D, t>}=v_{i}\right) \\
& \operatorname{Pr}\left(v_{i} \mid\left\{\neg v_{s t}\right\}\right)=0 \\
& \operatorname{Pr}\left(\neg v_{i} \mid\left\{v_{s t}\right\}\right)=1-\operatorname{Pr}\left(A_{<v_{s t}, D, t>}=v_{i}\right) \\
& \operatorname{Pr}\left(\neg v_{i} \mid\left\{\neg v_{s t}\right\}\right)=1
\end{aligned}
$$

![img-2.jpeg](img-2.jpeg)

Fig. 3. Initialization of the Selective Bayesian Network

TABLE 3 Supportive probabilities


- For the example in Table 1, the corresponding conditional probabilities is shown in Table 3.

### 4.3 Select the Best Routing Query Set

A straightforward heuristic solution to select the best query set is to select the top-k questions which have the highest expected reduction of selection hardness in Equation 19. However, such a solution neglects the correlation among the queries in $S_{k}$. The correlation can be estimated by sampling, but the precision depends on the sample qualification and quantity. With the Selective Bayesian Network, we have the spacial casual information about the nodes, so we can make use of the spacial causalities to compute the expected uncertainty reduction.

Let $S_{k}$ be a set of $k$ routing queries, $S_{k}=\left{Q_{1}, \ldots, Q_{k}\right}$, where each query is in the form $Q_{i}=\left(v_{s t}^{i}, C_{i}, t\right)$. Let $A_{S_{k}}$ be the $k$ ground-truth answers of the queries in $S_{k}$, which is actually a discrete random variable with sample space $C_{1} \times \ldots \times C_{k}$. The probability of $A_{S_{k}}$ is is actually the joint probability

$$ \operatorname{Pr}\left(A_{S_{k}}=v_{S_{k}}\right)=\operatorname{Pr}\left(A_{Q_{1}}=v_{S_{k}}^{1}, \ldots, A_{Q_{k}}=v_{S_{k}}^{k}\right) $$

where the vector $v_{S_{k}} \in C_{1} \times \ldots \times C_{k}$ and $v_{S_{k}}^{i}$ is the $i$ th coordinate of $v_{S_{k}}$, which is the ground-truth answer for $Q_{i}$.

Therefore, the expectation of selection hardness after receiving $A_{S_{k}}$ is

$$ \begin{aligned} & \mathbb{E} H\left(B R \mid A_{S_{k}}\right) \ & =\sum_{v_{S_{k}} \in C_{1} \times \ldots \times C_{k}} \operatorname{Pr}\left(A_{S_{k}}=v_{S_{k}}\right) H\left(B R=R \mid A_{S_{k}}=v_{S_{k}}\right) \ & =\sum_{v_{S_{k}} \in C_{1} \times \ldots \times C_{k}} \operatorname{Pr}\left(A_{S_{k}}=v_{S_{k}}\right) \sum_{R \in R S}\left(\operatorname{Pr}\left(B R=R \mid A_{S_{k}}=v_{S_{k}}\right)\right. \ & \left.\log \operatorname{Pr}\left(B R=R \mid A_{S_{k}}=v_{S_{k}}\right)\right) \ & =\sum_{v_{S_{k}} \in C_{1} \times \ldots \times C_{k}} \operatorname{Pr}\left(A_{Q_{1}}=v_{S_{k}}^{1}, \ldots, A_{Q_{k}}=v_{S_{k}}^{k}\right) \ & \sum_{R \in R S}\left(\operatorname{Pr}\left(B R=R \mid A_{Q_{1}}=v_{S_{k}}^{1}, \ldots, A_{Q_{k}}=v_{S_{k}}^{k}\right)\right. \ & \left.\log \operatorname{Pr}\left(B R=R \mid A_{Q_{1}}=v_{S_{k}}^{1}, \ldots, A_{Q_{k}}=v_{S_{k}}^{k}\right)\right) \end{aligned} $$

As stated previously, $\Delta H_{S_{k}}$ can be regarded as the mutual information between $B R$ and $A_{S_{k}}$. Actually, for a set of queries $S_{k}=\left{Q_{1}, Q_{2}, \ldots, Q_{k}\right}$, some of the queries are independent with $B R$, and with other queries, given the ground truth and the spacial information. Suppose that $Q_{i}=\left(v_{s t}^{i}, C^{i}, t\right)$, if exists some $1 \leq i, j \leq k$ such that $B R \rightarrow v_{s t}^{i}$ and $B R \nrightarrow v_{s t}^{j}$, then $\operatorname{Pr}\left(A_{Q_{j}}\right)$ is conditionally independent with $\operatorname{Pr}(B R)$ and $\operatorname{Pr}\left(A_{Q_{i}}\right)$, i.e.

$$ \begin{aligned} & \forall v_{p} \in C^{i}, \forall v_{q} \in C^{j} \ & \operatorname{Pr}\left(A_{Q_{1}}, A_{Q_{j}} \mid B R \rightarrow v_{s t}^{i}, B R \nrightarrow v_{s t}^{j}\right) \ & =\operatorname{Pr}\left(A_{Q_{i}} \mid B R \rightarrow v_{s t}^{i}, B R \nrightarrow v_{s t}^{j}\right) \ & \cdot \operatorname{Pr}\left(A_{Q_{j}} \mid B R \rightarrow v_{s t}^{i}, B R \nrightarrow v_{s t}^{j}\right) \ & =\operatorname{Pr}\left(A_{Q_{i}} \mid B R \rightarrow v_{s t}^{i}, B R \nrightarrow v_{s t}^{j}\right) \cdot \operatorname{Pr}\left(A_{Q_{j}}\right) \end{aligned} $$

Now, for a candidate route set $\mathbb{R}$, we can finally calculate $\Delta\left(H_{S_{k}}\right)$ for a given set $S_{k}$ of queries, by using the Selective Bayesian network $\mathcal{N}(\mathbb{R})$ and the following theorem.

Theorem 4.2. For a candidate route set $\mathbb{R}$, its Selective Bayesian Network $\mathcal{N}(\mathbb{R})$ and a given query set $S_{k}$, the expected reduction of selection hardness $\Delta H_{S_{k}}$ is

$$ \Delta H_{S_{k}}=-\sum_{S_{k}^{+}(R) \neq \emptyset} \operatorname{Pr}(R) \log \operatorname{Pr}\left(v_{R}^{1}, v_{R}^{2}, \ldots, v_{R}^{\left|S_{k}^{+}(R)\right|}\right) $$

where $S_{k}^{+}(R)=\left{Q=\left(v_{s t}, C, t\right) \mid Q \in S_{k}, R \rightarrow\right.$ $\left.v_{s t}\right\}$ and $v_{R}^{i}=R \cap C_{i}$ by supposing that $S_{k}^{+}(R)=$ $\left{Q_{1}, Q_{2}, \ldots, Q_{\left|S_{k}^{+}(R)\right|}\right}$ and $Q_{i}=\left(v_{s t}, C_{i}, t\right)$.

Proof. Please see in appendix in supplemental file.
The joint probability $\operatorname{Pr}\left(v_{R}^{1}, v_{R}^{2}, \ldots, v_{R}^{\left|S_{k}^{+}(R)\right|}\right)$ in Theorem 4.2 can be calculated by reasoning on $\mathcal{N}(\mathbb{R})$ :

$$ \operatorname{Pr}\left(v_{R}^{1}, v_{R}^{2}, \ldots, v_{R}^{\left|S_{k}^{+}(R)\right|}\right)=\prod_{i=1}^{\left|S_{k}^{+}(R)\right|} \operatorname{Pr}\left(v_{R}^{i} \mid \operatorname{parent}\left(v_{R}^{i}\right)\right) $$

where $\operatorname{parent}\left(v_{R}^{i}\right)=\left{v \mid\left(v, v_{R}^{i}\right) \in \mathcal{N}(\mathbb{R})\right}$, namely, the set of all parents of node $v_{R}^{i}$ in the network $\mathcal{N}(\mathbb{R})$.

Thus, instead of estimating $\Delta H_{S_{k}}$ by sampling, the Selective Bayesian Network $\mathcal{N}(\mathbb{R})$ is capable to select the best $S_{k}$ with Equations 27 and 28. In practice, however, exploring all possible $k$ combinations and reasoning on them is quite expensive. So in our

algorithm, we also use two relaxations to improve the efficiency, which will be discussed in Section 4.4.

### 4.4 The Framework of the Algorithm

The best routing query set selected by the Selective Bayesian Network is given to the crowd. The probability of the ground-truth answer of a routing query $Q$ is computed by

$$
\begin{aligned}
& \operatorname{Pr}\left(A_{Q}=v\right)=\operatorname{Pr}\left(\left(v_{s t}, v\right) \in B R \mid B R \rightarrow v_{s t}\right) \\
= & \frac{\operatorname{Pr}\left(B R \rightarrow v_{s t} \mid\left(v_{s t}, v\right) \in B R\right) \operatorname{Pr}\left(\left(v_{s t}, v\right) \in B R\right)}{\operatorname{Pr}\left(B R \rightarrow v_{s t}\right)} \\
= & \frac{\sum_{R \in \mathbb{R} \wedge\left(v_{s t}, v\right) \in R} \operatorname{Pr}(R)}{\sum_{R^{\prime} \in \mathbb{R} \wedge R^{\prime} \rightarrow v_{s t}} \operatorname{Pr}\left(R^{\prime}\right)}
\end{aligned}
$$

The above equation can be used to compute the pmf for a given set of route $\mathbb{R}$. For instance, in Figure 1, for the routing query $Q_{3}$, we have $\operatorname{pmf}\left(Q_{3}, v_{3}\right)=\operatorname{Pr}\left(A_{Q_{3}}=v_{3}\right)=\operatorname{Pr}\left(R_{3}\right) /\left(\operatorname{Pr}\left(R_{3}\right)+\right.$ $\left.\operatorname{Pr}\left(R_{4}\right)\right)=0.4 /(0.4+0.1)=0.8$.

With the answers $A_{S_{k}}$ collected from the crowd, the probabilities of the routes in $\mathbb{R}$ can be updated. According to the conclusion in [1], the final result of the best route distribution is independent of the sequence of the answers being utilized. So the answers in $A_{S_{k}}$ can be used to update the distribution one by one. With each answer $A_{Q}=v$ in $A_{S_{k}}$, suppose that $Q=\left(v_{s t}, C, t\right)$, the probability of $R \in \mathbb{R}$ being the best route is updated by following equation

$$
\begin{aligned}
& \operatorname{Pr}(B R=R \mid A_{Q}=v)= \\
& \operatorname{Pr}\left(B R \rightarrow v_{s t}\right) \operatorname{Pr}\left(B R=R \mid A_{Q}=v, B R \rightarrow v_{s t}\right) \\
& +\left(1-\operatorname{Pr}\left(B R \rightarrow v_{s t}\right)\right) \operatorname{Pr}\left(B R=R \mid A_{Q}=v, B R \nrightarrow v_{s t}\right)
\end{aligned}
$$

where $\operatorname{Pr}\left(B R \rightarrow v_{s t}\right)=\sum_{R \in \mathbb{R} \wedge R \rightarrow v_{s t}} \operatorname{Pr}(R)$. In practice, we reasonably assume that the crowd workers do not always give correct answers, so let $\varepsilon$ be the error rate of the crowd. The utilization needs to be replaced by

$$
\begin{array}{ll}
\operatorname{Pr}(B R=R \mid v \text { returned by the crowd })= & \\
& \begin{array}{ll}
\operatorname{Pr}(R) & R \nrightarrow v_{s t} \\
\frac{\operatorname{Pr}(R)(1-\varepsilon)}{\operatorname{Pr}\left(A_{Q}=v\right)(1-\varepsilon)+\left(1-\operatorname{Pr}\left(A_{Q}=v\right)\right) \varepsilon} & \left(v_{s t}, v\right) \in R \\
\frac{\operatorname{Pr}(R) \varepsilon}{\operatorname{Pr}\left(A_{Q}=v\right)(1-\varepsilon)+\left(1-\operatorname{Pr}\left(A_{Q}=v\right)\right) \varepsilon} & \text { otherwise }
\end{array}
\end{array}
$$

We formally introduce our algorithm. The framework of the algorithm is as follows, given a route set $\mathbb{R}$ and a budget limit $B$,

1) Build the Selective Bayesian Network $\mathcal{N}(\mathbb{R})$.
2) Repeatedly use $\mathcal{N}(\mathbb{R})$ to select query set $S_{k}$ to ask the crowd and receive $k$ answers.
3) Update the probabilities of all routes in $\mathbb{R}$ with the crowdsourced $k$ answers.
4) Repeat 2 and 3 until the budget $B$ is used up, and then report the most likely best route.

Please note that in implementation we modularize the algorithm into offline part and online part. The Selective Bayesian Network is built offline for efficiency. The spacial relations between the routes and the vertices are also computed offline, and then stored in a spacial information table $T_{s i}(\mathbb{R})$, which supports queries of form " $R \rightarrow v$ ?" within linear time. As stated above, precise reasoning on all possible combinations of $S_{k}$ in each round is too expensive, so we use two relaxations. The first one

Input: A path set $\mathbb{R}$ and its query set $\mathbb{Q}$, the number $k$ of queries per round and the total budget $B$
Output: The most likely best route
Build the Selective Bayesian network $\mathcal{N}(\mathbb{R})$ according to Lemma 4.1
while $B \neq 0$ do
Set $S_{k}=\emptyset$
while $\left|S_{k}\right|<k$ do
for each $Q \in \mathbb{Q}$ do
Calculate $\Delta H_{S_{k} \cup Q}$ with $\mathcal{N}(\mathbb{R})$ and Theorem 4.2
end
Set $Q_{\max }=\operatorname{argmax}_{Q \in \mathbb{Q}} \Delta H_{S_{k} \cup Q}$
Add $Q_{\max }$ into $S_{k}$ and remove it from $\mathbb{Q}$
end
Ask queries in $S_{k}$ to crowd and receive the corresponding answers $A_{S_{k}}$
for each answer $v \in A_{S_{k}}$ do
for each $R \in \mathbb{R}$ do
Set $\operatorname{Pr}(R)=\operatorname{Pr}(B R=R \mid v)$ with Formula 31
end
end
Set $B=B-k$
if $B<k$ then
$k=B$
end
end
return the route $R$ with the maximum $\operatorname{Pr}(R)$
Algorithm 2: k-selection with Selective Bayesian Net
is the same with the sampling-based approach in [1], namely, to approximate the best $S_{k}$ by incrementally selecting queries, as in Lines 5 - 9 in Algorithm 2. The second relaxation is use samplingbased reasoning instead of precise reasoning, when calculating $\Delta H_{S_{k}}$ in Line 6. Although the joint probabilities needed in the calculation is also estimated by sampling, the precision is higher with the help of the spacial causalities embedded in $\mathcal{N}(\mathbb{R})$. There are lots of samplers available, including Gibbs [17], Hamiltonian Monte Carlo [18], Metropolis-Hastings [19], etc. In our work, we use the basic Gibbs sampling for the reasoning on $\mathcal{N}(\mathbb{R})$.

## 5 EXPERIMENTAL EVALUATION

In this section, we report the experimental study to validate the effectiveness and efficiency of our proposals. First, we use synthetic data and a simulated crowd to explore wide rages of values for the parameters. Second, we conduct an experiment with real-world datasets to verify our conclusions on the synthetic data.

In the experiments, we compare the performances of the following three categories of algorithms.

1) (ours-k=x) k-selection with Selective Bayesian Network, with $k=1,2,4$, our method proposed in Section 3.
2) (baseline-k=x) sampling-based algorithm proposed in [1], with $k=1,2,4$.
3) (random) a naive algorithm - to select a random set of queries, with $k=1,2,4$, to ask the crowd in each round.

In the rest of the paper, for the random selection, we only plot $k=$ 1 , and omit $k=2,4$, because the three curves almost coincides in all settings - selecting one random query is basically the same with selecting multiple random queries per round.

### 5.1 Simulation on Synthetic Data

We compare the performances of the above algorithms with the error rate of the crowd $\varepsilon=0.1,0.2,0.3$, and the total sample size

![img-3.jpeg](img-3.jpeg)

Fig. 4. Error rate $\varepsilon=0.1,0.2,0.3$ and sample size $\mu=30 k, 60 k, 120 k$
$\mu=30 k, 60 k, 120 k$. The route sets with a best route distributions are randomly generated, and for each of them, the corresponding query set and pmf are then calculated. Then several best routes are sampled according to the distribution, and for each best route, we run the competing algorithms separately and finally plot the results, as shown in Figure 4. We summarize the experimental result in following aspects.

Varying sample size. The sample size for probability estimation, $\mu$, is set to $30 \mathrm{k}, 60 \mathrm{k}$ and 12 k , respectively. The performances are directly effected by the sample size, as during the computation, some required probabilities are estimated with the samples. In the result in Figure 4, it is obvious that our method is much less sensitive about the sample size compared with the baseline. With the decrease of the sample size, the advantage of our proposal becomes more significant.

Varying number of queries per round. The number of routing queries to select each round, $k$, is set to 1,2 and 4 . As shown in Figure 4, smaller $k$ tends to be more effective on reducing the selection hardness, for both our proposal and the baseline. This is partially because the bigger $k$ is, the more complex the correlation among the queries is, thus the less precisely the sample estimates the joint probabilities, if we fix the sample size. Another reason is that each routing query is selected based on the previously crowdsourced answers. The bigger $k$ is, the less frequently the best route distribution is updated by the crowd. Interestingly, for our method, when $k$ is increasing, the performance degradation is relatively small, in terms of the descent rate and the minimum number of queries to bring $H(B R)$ down to 0 . The only exception
is in the roughest setting, $\varepsilon=0.3, \mu=30 k$, yet our approach even with $k=4$ is still better than the baseline with $k=1$.

Varying error rate. The error rate of the crowd, $\varepsilon$, is set to $0.1,0.2$ and 0.3 . For all the algorithms, the lower $\varepsilon$ is, the faster the performance converges. For a crowd with higher accuracy, smaller amount of the queries are necessary to suggest a best route.

Different algorithms. The result in Figure 4 shows that for any combination of $\varepsilon, \mu, k$, our approach dominates the baseline and the random algorithms. In most cases, our approach with $k=$ 4 shows even better performance than the baseline with any $k$.

We can conclude that the k -selection with the Selective Bayesian Network is much less sensitive about the sample size $\mu$, the query batch size $k$ and the error rate of the crowd $\varepsilon$. The spacial causalities provided by the Selective Bayesian Network make the routing query selection much more stable and robust.

### 5.2 Verification on Real Data

We use five real-world road-network datasets, namely, California Road Network (CA), San Francisco Road Network (SF), Road Network of North America (NA), City of San Joaquin County Road Network (TG) and City of Oldenburg Road Network (OL) [20], [21]. The road networks in these datasets are obtained from Digital Chart of the World Server. Although each of the above datasets contains a lot of nodes and paths, the data is actually not dense enough in terms of routing queries. For a given pair of locations, the number of intersections of different routes is usually small, which makes the total number of routing queries small. So in the experiment we use a data augmentation to supplement

![img-4.jpeg](img-4.jpeg)

Fig. 5. Comparison on real datasets: CA, SF, NA, TG and OL

![img-5.jpeg](img-5.jpeg)

Fig. 6. Precision with budget B=10, 20, 30, 60

![img-6.jpeg](img-6.jpeg)

Fig. 7. Average time cost

necessary routing queries to deal with the query sparsity of the data. With the data augmentation, we construct 25 route sets (5 from each dataset), and each route set contains more than 60 routing queries. For each route set, we calculate the distribution of the best route according to the normalized costs of the routes, and then sample the best route according to the distribution for 10 runs of algorithms, with k=1,2 and 4 respectively. We test totally 750 runs on the real-world road networks for each algorithm. As shown in Figure 5, the result is consistent with synthetic data. Our best route selection with the Selective Bayesian Network performs better on all datasets.

### 5.3 Effectiveness and Time Cost

Below we conduct experiments to exhibit the goodness of paths selected by the crowd. It worth mentioning that for these 25 route sets from real-world data, the precision of each algorithm except random is quite high, after asking 60 routing queries. So we vary the budget B=10, 20, 30, 60, to test the performances of the algorithms when the budget is limited. As shown in Figure 6, our method performs better than others in terms of precision. In most cases, the precision of our method is close to 100% even with a budget of only 10 queries.

Moreover, we also test the average time cost of our algorithm with k=1, 2 and 4, on all the datasets. As shown in Figure 7, for all the route sets from the real data, our algorithm successfully selects 60 best routing queries and then suggests a best route with nearly 100% precision within 90 seconds, which is impressive for a crowdsourcing framework.

# 6 Related Works

### 6.1 Crowdsourcing

The recent development of crowdsourcing brings us a brand new opportunity to engage human intelligence in the process of answering queries (see [22] as a survey). Crowdsourcing provides a new problem-solving paradigm [23], [24], which has been blended into several research communities. In particular, crowdsourcing-based data management techniques have recently attracted much attention in the database and data mining communities. From a practical viewpoint, [25] proposed and developed a query processing system using microtask-based crowdsourcing to answer queries. Moreover, in [26], a declarative query model is proposed to cooperate with standard relational database operators. In addition, from the viewpoint of theoretical study, many fundamental queries have been extensively studied, including filtering [27], max [28], sorting [29], join [29], [30], and so on. Besides, crowdsourcing-based solutions of many complex algorithms have also been developed, such as categorization based on graph search [15], clustering [31], entity resolution [32], [33], analysis over social media [34], and tagging in social networks [35], trip planning [36], pattern mining [37] etc.

### 6.2 Path Recommendation with Crowd

Finding the most desirable path has now been receiving tremendous research interest for decades [38], [39], [40]. The most popular topic in this area is shortest path finding, which has been extensively studied for over fifty years. If the weight on each edge represents travel time, shortest path finding becomes fastest path finding. Such as, the authors in [38] introduce a favorite route proposal scheme to provide route recommendations, and the scheme they proposed can generate better recommendations than alternative learning algorithms. Specifically, the work in [41] considers the availability of routes for different users. Two efficient algorithms are proposed in [42], which uses minimum on-road travel cost function. The authors in [39] improve the performance of batch shortest path algorithms they proposed by revisiting the problem of query clustering, and three query decomposition methods are proposed for fast query clustering.

In addition, approaches in [43], [44], [45], [46] predict the future trajectory by introducing deep learning models. To help route decision, the approach in [43] uses RNN to build a trajectory model, assuming that the itinerary of the destination link is a known parameter. In [4], a deep probabilistic model is presented, which unifies three key explanatory factors for most likely route prediction. Moreover, in order to effectively share the statistical strength, an adjoint generative model is proposed to learn representations of k-destination proxies.

To the best of our knowledge, this is the first work studying the path selection problem with the help of crowd. The essential objective is to make it easier for users to select the best path among a number of candidates. The authors in [47] propose a system to leverage crowds' knowledge to improve the quality of recommended routes. This paper distinguishes itself with [47] from the following aspects: first, we ask the crowd to identify the direction at each road intersection; second, we adjust the distribution of recommended paths, rather than identify the very best one.

## 7 CONCLUSION AND FUTURE WORK

A GPS-based navigation system usually suggests multiple paths for a pair of given source and target. Therefore, a struggling problem for users is to select the best one among them, namely the best path selection problem. Too many suggested paths may jeopardize the usability of recommendation data, and decrease user satisfaction. Although existing studies have partially solved this problem through integrating historical traffic logs or updating traffic conditions periodically, their solutions neglect the potential contribution of human experiences. In this paper, we resort to crowdsourcing to ease the pain of best path selection. In particular, we design two types of questions, namely Routing Query (RQ) and Binary Routing Query (BRQ), to ask the crowd to decide the direction at each road intersection. We consider the problem of selecting the best $k$ RQs. Furthermore, we propose a series of efficient algorithms, which dynamically manage the questions in order to reduce the selection hardness with a limited budget of questions. Finally, we verified the effectiveness and efficiency of our proposed approaches through experiments with synthetic and real-world datasets.

There are many further research directions to explore. First, an immediate interesting topic is how to create one HIT with multiple $R Q / B R Q$ questions. To do this, our exact formulation has to be modified since some questions would have been answered by the same worker, so the assumption that each question is independently answered does not hold. In future works, we would be interested in examining the trade-off between this decrease in data quality and the cost savings due to larger HITs. Second, although we proposed in this paper an efficient approach to recommend the best path by $k$-RQ selection, we omitted the take into account manpower scheduling problem in crowdsourcing and the delay to get the answers of the crowd. It will be more practical and interesting to design and conduct some real-world experiments to further verify our framework. Last, in our approach, we did not consider the cases that some workers failed to return their answers. In our current framework, we can simply ignore a crowdsourcing worker if no answer is returned. In other words, the worker fails to provide any useful observation to lower the uncertainty of the best path. But it is more interesting to model the failure rate of
returning answers to see what happens. We leave these interesting topics for future work.

## ACKNOWLEDGMENTS

Haodi Zhang is the corresponding author of this work. Chen Zhang and Haodi Zhang have contributed equally to this work. The authors are grateful to the crowd workers for their efforts to complete the experiment. The work is partially supported by the National Natural Science Foundation of China (Grant No. NSFC-61806132 and No. 61729201), Tencent Rhino-Bird Open Fund, Hong Kong RGC GRF Project 16202218 CRF Projects C6030-18G, C103118G, C5026-18G, AOE Project AoE/E-603/18, Guangdong Basic and Applied Basic Research Foundation 2019B151530001, Hong Kong ITC ITF grants ITS/044/18FX and ITS/470/18FX, Microsoft Research Asia Collaborative Research Grant, Didi-HKUST joint research lab project, and Wechat and Webank Research Grants.

## APPENDIX

## Proof of Theorem 4.2

Proof. Suppose $S_{k}=\left\{\left(v_{s t}^{1}, C_{1}, t\right), \ldots,\left(v_{s t}^{k}, C_{k}, t\right)\right\}$, and $C_{S_{k}}=C_{1} \times C_{2} \times \ldots \times C_{k}$.

$$
\begin{aligned}
& \mathbb{E} H\left(B R \mid A_{S_{k}}\right) \\
= & \sum_{R \in \mathbb{R}} \sum_{v_{S_{k}} \in C_{S_{k}}} \operatorname{Pr}\left(A_{S_{k}}=v_{S_{k}}\right)\left(\operatorname{Pr}\left(B R=R \mid A_{S_{k}}=v_{S_{k}}\right)\right. \\
& \log \operatorname{Pr}\left(B R=R \mid A_{S_{k}}=v_{S_{k}}\right)\right) \\
= & \sum_{R \in \mathbb{R}} \sum_{v_{S_{k}} \in C_{S_{k}}}\left[\operatorname{Pr}\left(A_{S_{k}}=v_{S_{k}}\right)\right. \\
& \frac{\operatorname{Pr}(B R=R) \operatorname{Pr}\left(A_{S_{k}}=v_{S_{k}} \mid B R=R\right)}{\operatorname{Pr}\left(A_{S_{k}}=v_{S_{k}}\right)} \\
& \left.\log \frac{\operatorname{Pr}(R) \operatorname{Pr}\left(A_{S_{k}}=v_{S_{k}} \mid B R=R\right)}{\operatorname{Pr}\left(A_{S_{k}}=v_{S_{k}}\right)}\right]
\end{aligned}
$$

Now, for a given $v_{S_{k}} \in C_{S_{k}}$, we calculate the above equation part by part according to different types of $R$.

- For those paths such that $\forall v_{s t}^{i}, R \nrightarrow v_{s t}^{i}, A_{S_{k}}$ is independent with $B R=R$, and $A_{Q_{i}}=v_{i}$ is also independent with each other for $i=1 . . N$, i.e.

$$
\begin{aligned}
& X_{1}=\sum_{\forall v_{s t}^{i}, R \nrightarrow v_{s t}^{i}} \sum_{v_{S_{k}} \in C_{S_{k}}}\left[\operatorname{Pr}\left(A_{S_{k}}=v_{S_{k}}\right)\right. \\
& \frac{\operatorname{Pr}(B R=R) \operatorname{Pr}\left(A_{S_{k}}=v_{S_{k}} \mid B R=R\right)}{\operatorname{Pr}\left(A_{S_{k}}=v_{S_{k}}\right)} \\
& \left.\log \frac{\operatorname{Pr}(B R=R) \operatorname{Pr}\left(A_{S_{k}}=v_{S_{k}} \mid B R=R\right)}{\operatorname{Pr}\left(A_{S_{k}}=v_{S_{k}}\right)}\right] \\
& =\sum_{\forall v_{s t}^{i}, R \nrightarrow v_{s t}^{i}} \sum_{v_{S_{k}} \in C_{S_{k}}}\left[\operatorname{Pr}\left(A_{S_{k}}=v_{S_{k}}\right)\right. \\
& \frac{\operatorname{Pr}(B R=R) \operatorname{Pr}\left(A_{S_{k}}=v_{S_{k}}\right)}{\operatorname{Pr}\left(A_{S_{k}}=v_{S_{k}}\right)} \\
& \left.\log \frac{\operatorname{Pr}(B R=R) \operatorname{Pr}\left(A_{S_{k}}=v_{S_{k}}\right)}{\operatorname{Pr}\left(A_{S_{k}}=v_{S_{k}}\right)}\right] \\
& =\sum_{\forall v_{s t}^{i}, R \nrightarrow v_{s t}^{i}} \sum_{v_{S_{k}} \in C_{S_{k}}} \operatorname{Pr}\left(A_{S_{k}}=v_{S_{k}}\right) \operatorname{Pr}(R) \log \operatorname{Pr}(R) \\
& =\sum_{\forall v_{s t}^{i}, R \nrightarrow v_{s t}^{i}} \operatorname{Pr}(R) \log \operatorname{Pr}(R)
\end{aligned}
$$

- For those paths such that $\forall v_{s t}^{i} R \rightarrow v_{s t}^{i}$, given that $R$ goes through all starting vertices of the queries in $S_{k}$, the probability of $A_{S_{k}}=v_{S_{k}}$ is actually the joint probability, $\operatorname{Pr}\left(A_{S_{k}}=v_{S_{k}}\right)=\operatorname{Pr}\left(R \rightarrow A_{1}, R \rightarrow A_{2}, \ldots, R \rightarrow\right.$ $\left.A_{k}\right)=\operatorname{Pr}\left(A_{1}, A_{2}, \ldots, A_{k}\right)$. So, $\operatorname{Pr}\left(A_{S_{k}}=v_{S_{k}} \mid B R=\right.$ $R)=\operatorname{Pr}\left(A_{1}, A_{2}, \ldots, A_{k} \mid B R=R\right)$, where $A_{i}$ is the node in $B N(G)$ corresponds the answer of $R Q_{i}$. Thus, we have,

$$
\begin{aligned}
& X_{2}=\sum_{\forall v_{s t}^{i}, R \rightarrow v_{s t}^{i}} \sum_{v_{S_{k}} \in C_{S_{k}}}\left[\operatorname{Pr}\left(A_{S_{k}}=v_{S_{k}}\right)\right. \\
& \frac{\operatorname{Pr}(B R=R) \operatorname{Pr}\left(A_{S_{k}}=v_{S_{k}} \mid B R=R\right)}{\operatorname{Pr}\left(A_{S_{k}}=v_{S_{k}}\right)} \\
& \left.\log \frac{\operatorname{Pr}(B R=R) \operatorname{Pr}\left(A_{S_{k}}=v_{S_{k}} \mid B R=R\right)}{\operatorname{Pr}\left(A_{S_{k}}=v_{S_{k}}\right)}\right] \\
& =\sum_{\forall v_{s t}^{i}, R \rightarrow v_{s t}^{i}} \sum_{v_{S_{k}} \in C_{S_{k}}}
\end{aligned}
$$

$$
\begin{aligned}
& {\left[\operatorname{Pr}(B R=R) \operatorname{Pr}\left(A_{S_{k}}=v_{S_{k}} \mid B R=R\right)\right.} \\
& \left.\log \frac{\operatorname{Pr}(B R=R) \operatorname{Pr}\left(A_{S_{k}}=v_{S_{k}} \mid B R=R\right)}{\operatorname{Pr}\left(A_{S_{k}}=v_{S_{k}}\right)}\right] \\
& =\sum_{\forall v_{s t}^{i}, R \rightarrow v_{s t}^{i}}\left[\operatorname{Pr}(B R=R) \operatorname{Pr}\left(A_{S_{k}}=R \cap C_{S_{k}} \mid B R=R\right)\right. \\
& \left.\log \frac{\operatorname{Pr}(B R=R) \operatorname{Pr}\left(A_{S_{k}}=R \cap C_{S_{k}} \mid B R=R\right)}{\operatorname{Pr}\left(A_{S_{k}}=R \cap C_{S_{k}}\right)}\right] \\
& =\sum_{\forall v_{s t}^{i}, R \rightarrow v_{s t}^{i}} \operatorname{Pr}(B R=R) \log \frac{\operatorname{Pr}(B R=R)}{\operatorname{Pr}\left(A_{S_{k}}=R \cap C_{S_{k}}\right)}
\end{aligned}
$$

where

$$
R \cap C_{S_{k}}=\left\{v_{R}^{i} \mid v_{R}^{i} \in C_{i},\left(v_{s t}^{i}, v_{R}^{i}\right) \in R\right\}
$$

namely, the set of k answers for $S_{k}$ which are consistent with $R$.
Suppose that $R \cap C_{S_{k}}=\left\{v_{R}^{1}, v_{R}^{2}, \ldots, v_{R}^{k}\right\}$, we have,

$$
\begin{aligned}
& X_{2}=\sum_{\forall v_{s t}^{i}, R \rightarrow v_{s t}^{i}} \operatorname{Pr}(B R=R) \log \frac{\operatorname{Pr}(B R=R)}{\operatorname{Pr}\left(A_{S_{k}}=R \cap C_{S_{k}}\right)} \\
& =\sum_{\forall v_{s t}^{i}, R \rightarrow v_{s t}^{i}} \operatorname{Pr}(R) \log \frac{\operatorname{Pr}(R)}{\operatorname{Pr}\left(v_{R}^{1}, v_{R}^{2}, \ldots, v_{R}^{k}\right)}
\end{aligned}
$$

where $\operatorname{Pr}\left(v_{R}^{1}, v_{R}^{2}, \ldots, v_{R}^{k}\right)$ can be calculated by the selection Bayesian network $\mathcal{N}(\mathbb{R})$.

- For those paths $R$ such that $\exists v_{s t}^{i}, R \rightarrow v_{s t}^{i}$ and $\exists v_{s t}^{j}, R \nrightarrow$ $v_{s t}^{j}$, i.e. some of the starting vertices of $S_{k}$ are in the path $R$, while the other are not. We denote the corresponding queries with these two categories of starting vertices by $S_{k}^{+}(R)$ and $S_{k}^{-}(R)$ :

$$
\begin{aligned}
& S_{k}^{+}(R)=\left\{Q=\left(v_{s t}, C, t\right) \mid Q \in S_{k}, R \rightarrow v_{s t}\right\} \\
& S_{k}^{-}(R)=\left\{Q=\left(v_{s t}, C, t\right) \mid Q \in S_{k}, R \nrightarrow v_{s t}\right\}
\end{aligned}
$$

We have,

$$
\begin{aligned}
& X_{3}=\sum_{\substack{\exists v_{s t}^{i}, R \rightarrow v_{s t}^{i} \\
\exists v_{s t}^{j}, R \nrightarrow v_{s t}^{i}}} \sum_{v_{S_{k}} \in C_{S_{k}}}\left[\operatorname{Pr}\left(A_{S_{k}}=v_{S_{k}}\right)\right. \\
& \frac{\operatorname{Pr}(B R=R) \operatorname{Pr}\left(A_{S_{k}}=v_{S_{k}} \mid B R=R\right)}{\operatorname{Pr}\left(A_{S_{k}}=v_{S_{k}}\right)} \\
& \left.\log \frac{\operatorname{Pr}(B R=R) \operatorname{Pr}\left(A_{S_{k}}=v_{S_{k}} \mid B R=R\right)}{\operatorname{Pr}\left(A_{S_{k}}=v_{S_{k}}\right)}\right] \\
& =\sum_{\substack{\exists v_{s t}^{i}, R \rightarrow v_{s t}^{i} \\
\exists v_{s t}^{j}, R \nrightarrow v_{s t}^{i}}} \sum_{v_{S_{k}} \in C_{S_{k}}}\left[\right. \\
& \operatorname{Pr}\left(A_{S_{k}^{+}(R)}=v_{S_{k}^{+}(R)}\right) \prod_{R Q \in S_{k}^{-}(R)} \operatorname{Pr}\left(A_{Q}=v_{S_{k}}^{R Q}\right) \\
& \frac{\operatorname{Pr}(B R=R) \operatorname{Pr}\left(A_{S_{k}^{+}(R)}=v_{S_{k}^{+}(R)} \mid B R=R\right)}{\operatorname{Pr}\left(A_{S_{k}^{+}(R)}=v_{S_{k}^{+}(R)}\right)} \\
& \left.\log \frac{\operatorname{Pr}(B R=R) \operatorname{Pr}\left(A_{S_{k}^{+}(R)}=v_{S_{k}^{+}(R)} \mid B R=R\right)}{\operatorname{Pr}\left(A_{S_{k}^{+}(R)}=v_{S_{k}^{+}(R)}\right)}\right]
\end{aligned}
$$

$$
\begin{aligned}
= & \sum_{\substack{\exists v_{s t}^{i}, R \rightarrow v_{s t}^{i} \\
\exists v_{s t}^{i}, R \neq v_{s t}^{i}}}\left[\sum_{v_{S_{k}^{+}}} \prod_{v \in v_{S_{k}^{+}}} \operatorname{Pr}\left(A_{Q}=v\right)\right] \\
& \sum_{v_{S_{k}^{+}} \in C_{S_{k}^{+}(R)}}\left[\operatorname{Pr}\left(A_{S_{k}^{+}(R)}=v_{S_{k}^{+}(R)}\right)\right. \\
& \frac{\operatorname{Pr}(B R=R) \operatorname{Pr}\left(A_{S_{k}^{+}(R)}=v_{S_{k}^{+}(R)} \mid B R=R\right)}{\operatorname{Pr}\left(A_{S_{k}^{+}(R)}=v_{S_{k}^{+}}\right)} \\
& \left.\log \frac{\operatorname{Pr}(B R=R) \operatorname{Pr}\left(A_{S_{k}^{+}(R)}=v_{S_{k}^{+}(R)} \mid B R=R\right)}{\operatorname{Pr}\left(A_{S_{k}^{+}(R)}=v_{S_{k}^{+}(R)}\right)}\right] \\
= & \sum_{\substack{\exists v_{s t}^{i}, R \rightarrow v_{s t}^{i} \\
\exists v_{s t}^{i}, R \neq v_{s t}^{i}}}\left[\operatorname{Pr}(B R=R)\right. \\
& \operatorname{Pr}\left(A_{S_{k}^{+}(R)}=R \cap C_{S_{k}^{+}(R)} \mid B R=R\right) \\
& \left.\log \frac{\operatorname{Pr}(B R=R) \operatorname{Pr}\left(A_{S_{k}^{+}(R)}=R \cap C_{S_{k}^{+}(R)} \mid B R=R\right)}{\operatorname{Pr}\left(A_{S_{k}^{+}(R)}=R \cap C_{S_{k}^{+}(R)}\right)}\right] \\
= & \sum_{\substack{\exists v_{s t}^{i}, R \rightarrow v_{s t}^{i} \\
\exists v_{s t}^{i}, R \neq v_{s t}^{i}}} \operatorname{Pr}(R) \log \frac{\operatorname{Pr}(R)}{\operatorname{Pr}\left(A_{S_{k}^{+}(R)}=R \cap C_{S_{k}^{+}(R)}\right)}
\end{aligned}
$$

where

$$
\begin{aligned}
& R \cap C_{S_{k}^{+}(R)}=\left\{v_{p} \mid \exists v_{s t} \text { s.t. }\right. \\
& \left.<v_{s t}, D, t>\in S_{k}, v_{p} \in D,\left(v_{s t}, v_{p}\right) \in R\right\}
\end{aligned}
$$

Let $R \cap C_{S_{k}^{+}(R)}=\left\{v_{R}^{1}, v_{R}^{2}, \ldots, v_{R}^{\left|S_{k}^{+}(R)\right|}\right\}$, we have

Finally, the expected reduction of selection hardness is

$$
\begin{aligned}
& \Delta H_{S_{k}} \\
& =H(B R)-\mathbb{E} H\left(B R \mid A S_{k}\right) \\
& =H(B R)+X_{1}+X_{2}+X_{3} \\
& =-\sum_{R \in \mathbb{R}} \operatorname{Pr}(R) \log (\operatorname{Pr}(R))+\sum_{\forall v_{s t}^{i}, R \neq v_{s t}^{i}} \operatorname{Pr}(R) \log \operatorname{Pr}(R) \\
& +\sum_{\forall v_{s t}^{i}, R \rightarrow v_{s t}^{i}} \operatorname{Pr}(R) \log \frac{\operatorname{Pr}(R)}{\operatorname{Pr}\left(v_{R}^{1}, v_{R}^{2}, \ldots, v_{R}^{k}\right)} \\
& +\sum_{\substack{\exists v_{s t}^{i}, R \rightarrow v_{s t}^{i} \\
\exists v_{s t}^{i}, R \neq v_{s t}^{i}}} \operatorname{Pr}(R) \log \frac{\operatorname{Pr}(R)}{\operatorname{Pr}\left(v_{R}^{1}, v_{R}^{2}, \ldots, v_{R}^{\left|S_{k}^{+}(R)\right|}\right)} \\
& =-\sum_{\forall v_{s t}^{i}, R \rightarrow v_{s t}^{i}} \operatorname{Pr}(R) \log \operatorname{Pr}\left(v_{R}^{1}, v_{R}^{2}, \ldots, v_{R}^{k}\right) \\
& -\sum_{\substack{\exists v_{s t}^{i}, R \rightarrow v_{s t}^{i} \\
\exists v_{s t}^{i}, R \neq v_{s t}^{i}}} \operatorname{Pr}(R) \log \operatorname{Pr}\left(v_{R}^{1}, v_{R}^{2}, \ldots, v_{R}^{\left|S_{k}^{+}(R)\right|}\right) \\
& =-\sum_{\exists v_{s t}^{i}, R \rightarrow v_{s t}^{i}} \operatorname{Pr}(R) \log \operatorname{Pr}\left(v_{R}^{1}, v_{R}^{2}, \ldots, v_{R}^{\left|S_{k}^{+}(R)\right|}\right) \\
& =-\sum_{\substack{\exists v_{s t}^{i}, R \rightarrow v_{s t}^{i}}} \operatorname{Pr}(R) \log \operatorname{Pr}\left(v_{R}^{1}, v_{R}^{2}, \ldots, v_{R}^{\left|S_{k}^{+}(R)\right|}\right) \\
& =-\sum_{S_{k}^{+}(R) \neq \emptyset} \operatorname{Pr}(R) \log \operatorname{Pr}\left(v_{R}^{1}, v_{R}^{2}, \ldots, v_{R}^{\left|S_{k}^{+}(R)\right|}\right)
\end{aligned}
$$