# DP2-Pub: Differentially Private High-Dimensional Data Publication with Invariant Post Randomization 

Honglu Jiang, Member, IEEE, Haotian Yu, Xiuzhen Cheng, Fellow, IEEE, Jian Pei, Fellow, IEEE, Robert Pless, Member, IEEE, and Jiguo Yu, Fellow, IEEE


#### Abstract

A large amount of high-dimensional and heterogeneous data appear in practical applications, which are often published to third parties for data analysis, recommendations, targeted advertising, and reliable predictions. However, publishing these data may disclose personal sensitive information, resulting in an increasing concern on privacy violations. Privacy-preserving data publishing has received considerable attention in recent years. Unfortunately, the differentially private publication of high dimensional data remains a challenging problem. In this paper, we propose a differentially private high-dimensional data publication mechanism (DP2-Pub) that runs in two phases: a Markov-blanket-based attribute clustering phase and an invariant post randomization (PRAM) phase. Specifically, splitting attributes into several low-dimensional clusters with high intra-cluster cohesion and low inter-cluster coupling helps obtain a reasonable allocation of privacy budget, while a double-perturbation mechanism satisfying local differential privacy facilitates an invariant PRAM to ensure no loss of statistical information and thus significantly preserves data utility. We also extend our DP2-Pub mechanism to the scenario with a semi-honest server which satisfies local differential privacy. We conduct extensive experiments on four real-world datasets and the experimental results demonstrate that our mechanism can significantly improve the data utility of the published data while satisfying differential privacy.


Index Terms-High-dimensional data, differential privacy, Bayesian network, Markov-blanket, invariant PRAM.

## 1 INTRODUCTION

THE rapid development of information technology has opened up the era of big data. Collecting and publishing an unprecedented amount of data, as well as mining data correlations and generating insights have become an important component of social statistical research [1]. A large amount of high-dimensional and heterogeneous data appear in various applications, which are often published to third parties for data analysis, recommendations, targeted advertisements, and reliable predictions. Examples include healthcare data, social networking data, Internet of Things data (i.e., IoT device monitoring data, location data, trajectory data), financial market data (i.e., electronics commercial data, credit card data), which can be used to dig out valuable

- H. Jiang is with the Department of Computer Science and Software Engineering, Miami University, Oxford, OH 45056, USA, and the Department of Computer Science, The George Washington University, Washington, DC 20052, USA. E-mail: jiangh34@miamioh.edu.
- H. Yu is with the Department of Data Analytics, The George Washington University, Washington, DC 20052 USA. E-mail: yuxx6789@gwu.edu.
- X. Cheng is with the Department of Computer Science, The George Washington University, Washington, DC 20052 USA, and the School of Computer Science and Technology, Shandong University, Qingdao 266510, China. E-mail: xzcheng@sdu.edu.cn.
- J. Pei is with the Departments of Computer Science, Biostatistics and Bioinformatics, and Electrical and Computer Engineering, Duke University, Durham, NC 27708, USA. E-mail: j.pei@duke.edu.
- R. Pless is with the Department of Computer Science, The George Washington University, Washington, DC 20052 USA. E-mail: pless@gwu.edu.
- J. Yu (Corresponding Author) is with Big Data Institute, Qilu University of Technology, Jinan, 250353, P.R. China, and Shandong Fundamental Research Center for Computer Science, Qilu University of Technology, Jinan, Shandong, 250353, P.R. China. E-mail: jiguoyu@sina.com.
Manuscript received; revised.
information hidden behind the massive data for modern life. However, publishing these data may disclose personal sensitive information, resulting in an increasing concern of privacy violations. Privacy-preserving data publishing (PPDP) has gained significant attentions in recent years as a promising approach for information sharing while preserving data privacy [2].

Generally speaking, commonly used approaches for PPDP can be characterized into three categories: encryption technology [3], $k$-anonymity [4] and its derivative approaches ( $l$-diversity [5], $t$-closeness [6]), and differential privacy [7]. Differential privacy has gradually become the de facto standard privacy definition and provides a strong privacy guarantee. It rests on a sound mathematical foundation with a formal definition and rigorous proof while making the assumption that an attacker has the maximum background knowledge.

However, the differentially private publication of high dimensional data remains a challenging problem - it suffers from the "Curse of High-Dimensionality" [8], that is, when the dimensionality increases, the complexity and cost of multi-dimensional data processing and analysis increases exponentially. Specifically, this curse is manifested in two aspects: first, since the high-dimensional data space is usually sparse, high dimensions and large attribute domains lead to a low "Signal-to-Noise Ratio" and low data utility; second, complex correlations exist between high-dimensional data, therefore the change of a single record may have a great impact on query results, leading to increased sensitivity.

To address these challenges, an effective way is to decompose high-dimensional data into a set of low-

dimensional marginal tables along with inferring the joint distributions of the data, thus generating a synthetic dataset. A representative solution is PrivBayes [9], which constructs a Bayesian network to model the data correlations and conditional probability distributions, allowing one to approximate the distributions of the original data using a set of low-dimensional marginal distributions. However, such an approach suffers from poor data utility and high communication cost, since too much noise is added when there are too many attribute pairs resulting in unreliable conditional probabilities. Moreover, most approaches generally ignore the different roles a dimension may play for a specific query - one dimension may be more important than another for a particular query. Additionally, one dimension may release more information than another if the same amount of noise is added; thus evenly allocating the total privacy budget to each dimension degrades the performance.

In this paper, we provide a two-phase mechanism (DP2Pub) consisting of a Markov-blanket-based learning process and an invariant post randomization (PRAM) process satisfying local differential privacy to overcome the above difficulties. Our contributions can be summarized as follows:

- To capture the dependencies between the attributes in the dataset, we resort to differentially private Bayesian network construction, employing the exponential mechanism to attribute pairs using the mutual information as the score function.
- We propose the procedure of attribute clustering with a Markov blanket learning algorithm based on the constructed Bayesian network. Our most fundamental purpose is to split attributes into several lowdimensional clusters with high intra-cluster cohesion and low inter-cluster coupling, thus obtaining a reasonable allocation of privacy budget determined by the conditional independence among attributes and the importance of each cluster.
- Invariant PRAM is an important perturbation technique for privacy protection, which transforms each record stochastically in a dataset using delicately pre-selected probabilities. It ensures no loss of statistical information, thus can significantly preserve data utility. Motivated by this, we provide a doubleperturbation mechanism to achieve invariant PRAM for two-valued and multivalued attributes and apply it to each attribute cluster. Resorting to the randomized mapping based post-processing property for differential privacy, we prove that the proposed double-perturbation mechanism satisfies differential privacy.
- To tackle the data privacy preservation problem for the scenario where each individual contributes a single data record to a semi-honest server, we extend our DP2-Pub mechanism to handle the highdimensional data publication in a local-differentialprivacy manner, in which each user locally perturbs its data satisfying local differential privacy, then the server conducts all the operations including attribute clustering and post randomization over the privatized data.
- We evaluate the performance of data utility on four
real-world datasets from two aspects, the total variation distance between the original dataset and the perturbed dataset and the classification error rate of SVM classification on the perturbed dataset. Experimental results indicate that our approach can obtain higher data utility of the published data compared with the state-of-the-art.

The rest of this paper is organized as follows. We provide a literature review in Section 2. Section 3 formulates our problem and presents necessary background knowledge on Bayesian network, differential privacy, random response and post randomization. In Section 4, we propose our DP2Pub mechanism by detailing the constructions of differentially private Bayesian network, attribute clustering, and invariant PRAM. Comprehensive experimental studies on four real-world datasets are presented in Section 6. Section 7 concludes the paper with a future research discussion.

## 2 Related Work

Various differentially private mechanisms for highdimensional data publications have been proposed in recent years. In this section, we briefly review the most relevant works from two perspectives: under centralized setting or distributed setting, and discuss how our work differs from the existing ones.

### 2.1 Private Mechanisms Under Centralized setting

A powerful approach of dimensionality reduction is the Bayesian network model proposed in [10], in which Zhang et al. developed a differentially private scheme PrivBayes for publishing high-dimensional data. PrivBayes first constructs a Bayesian network to approximate the distribution of the original dataset, then adds noise into each marginal of the Bayesian network to guarantee differential privacy, next constructs an approximate distribution of the original dataset, and finally samples the tuples from the approximate distribution to construct a synthetic dataset.

Researchers also have developed sampling techniques to support differentially private high-dimensional data publications. In [11], Chen et al. provided a solution to protect the joint distribution of the dimensions in a high-dimensional dataset compared with PrivBayes. They first established a robust sampling-based approach to investigate the dependencies over all attributes for constructing a dependence graph, then applied a junction tree algorithm to provide an inference mechanism for deriving the joint data distribution. In [12], Li et al. proposed a differentially private data synthetization technique called DPCopula using Copula functions to handle multi-dimensional data. In [13], Xu et al. developed a high-dimensional data publishing algorithm under differential privacy to optimize the utility by first projecting a $d$-dimensional vector of user's attributes into a lower $k$-dimensional space using a random projection, then adding Gaussian noise to each resultant vector to obtain a synthetic dataset.

### 2.2 Private Mechanisms Under Distributed setting

The approaches mentioned above mainly consider centralized scenarios. Some efforts have also been devoted to differentially private high-dimensional data publications under distributed setting. Based on PrivBayes, Cheng et al. [14] considered a multi-party setting from multiple data owners and proposed a differentially private sequential update of the Bayesian network (DP-SUBN) approach, allowing the parties to collaboratively identify the Bayesian network that best approximates the joint distribution of the integrated dataset. Wang et al. [15] introduced a framework with a simple and generic aggregation and decoding technique. This framework can analyze, generalize and optimize several local differential privacy protocols [16-18] for frequency estimation. In [8], Ren et al. proposed a solution LoPub to realize high-dimensional data publication with local differential privacy in crowdsourced data publication systems. LoPub can first learn from the distributed data records to build correlations and joint distributions of attributes, then synthesize an approximate dataset achieving a good compromise between local differential privacy and data utility. In [19], Ju et al. also considered the high-dimensional data publication problem under local differential privacy in the crowdsourced-sensing system. They proposed an aggregation and publication mechanism which provides local privacy guarantees for crowd-sensing users, approximates the statistical characteristics of high-dimensional perception data and publishes synthetic data. Wang et al. [20] proposed two mechanisms for collecting and analyzing users' private data under local differential privacy, which can collect multidimensional data with both numerical and categorical attributes. In [21], Domingo-Ferrer developed several random-response-based complementary approaches for multi-dimensional data preservation. In [22], Takagi et al. presented a privacy-preserving phased generative model (P3GM) for high-dimensional data, which employs a twophase learning process for training the model to increase the robustness to the differential privacy constraint.

In light of the above analysis, the following aspects distinguish our work from the existing approaches. First, since the sensitivity of distinct dimensions are different and evenly allocating the total privacy budget to each dimension cannot obtain good performance, we take into account the privacy budget allocation problem to realize attribute clustering with a reasonable allocation of privacy budget. Second, we design an invariant PRAM mechanism instead of generating noisy conditional distributions of the Bayesian network, then apply it to each attribute cluster, which can significantly improve the data utility while satisfying local differential privacy.

## 3 Problem Formulation and Preliminaries

### 3.1 Problem Formulation

In this paper, we consider the following problem: a data server collects data containing a vast amount of individual information and aims to release an approximate dataset to third parties for their uses such as data analysis and recommendations. Let $D$ be the dataset, $n$ be the total number of records, and $\mathcal{A}=\left\{A_{1}, A_{2}, \cdots A_{d}\right\}$ be the set of $d$ unique
attributes. Assume that all attribute values are categorical as one can always discretize all numerical data. The domain of an attribute $A_{i}$ is denoted by $\Omega_{i}$, whose size is $\left|\Omega_{i}\right|$.

### 3.2 Bayesian Network

A Bayesian network is a type of probabilistic graphical model that approximately describes the joint distribution over a set of variables by specifying their conditional independence [23]. More specifically, a Bayesian network is a directed acyclic graph (DAG) whose nodes represent attribute variables and edges model the direct dependence among attributes. Formally speaking, a Bayesian network $\mathcal{N}$ over $\mathcal{A}$ (the set of attributes in $D$ ) is defined as a set of $d$ attributeparent (AP) pairs, $\left(A_{1}, \Pi_{1}\right), \cdots,\left(A_{d}, \Pi_{d}\right)$, where each AP contains a unique attribute and all its parent nodes in $\mathcal{N}$. If the maximum size of any parent set in $\mathcal{N}$ is $k$, we define $\mathcal{N}$ to be a $k$-degree Bayesian network. Let $\operatorname{Pr}[\mathcal{A}]$ denote the joint distribution over all attributes in $D$. A Bayesian network $\mathcal{N}$ defines a way to approximate $\operatorname{Pr}[\mathcal{A}]$ with $d$ conditional distributions $\operatorname{Pr}\left[A_{1} \mid \Pi_{1}\right], \operatorname{Pr}\left[A_{2} \mid \Pi_{2}\right], \cdots, \operatorname{Pr}\left[A_{d} \mid \Pi_{d}\right]$, that is, $\operatorname{Pr}_{\mathcal{N}}[\mathcal{A}]=\prod_{i=1}^{d} \operatorname{Pr}\left[A_{i} \mid \Pi_{i}\right]$. If $\mathcal{N}$ accurately captures the dependencies between the attributes in $\mathcal{A}, \operatorname{Pr}_{\mathcal{N}}[\mathcal{A}]$ can be a good approximation to $\operatorname{Pr}[\mathcal{A}]$. Moreover, the computation of $\operatorname{Pr}_{\mathcal{N}}[\mathcal{A}]$ can be efficient and simple if the degree of $\mathcal{N}$ is small. Figure 1 illustrates the Bayesian network over a set of five attributes, namely, age, gender, exposure to toxins, smoking, and cancer. Table 1 shows the AP pairs in the sample Bayesian network.
![img-0.jpeg](img-0.jpeg)

Fig. 1. A Bayesian network over five attributes.

TABLE 1
The attribute-parent pairs in the Bayesian network shown in Fig. 1


Given a dataset $D$, our goal is to construct a $k$-degree Bayesian network $\mathcal{N}$ which provides an accurate approximation to the full distribution of $D$. That is, $\operatorname{Pr}_{\mathcal{N}}[\mathcal{A}]$ should be close to $\operatorname{Pr}[\mathcal{A}]$. As $K L$-divergence [24] is commonly used as a measure of the similarity between a probability distribution and a candidate (estimated) distribution, in this paper, we adopt the $K L$-divergence of $\operatorname{Pr}_{\mathcal{N}}[\mathcal{A}]$ and $\operatorname{Pr}[\mathcal{A}]$ to measure the difference between these two probability distributions:

$$
K L(\operatorname{Pr}[\mathcal{A}], \operatorname{Pr}_{\mathcal{N}}[\mathcal{A}])=\sum_{i=1}^{d} H\left(A_{i}\right)-\sum_{i=1}^{d} I\left(A_{i}, \Pi_{i}\right)-H(\mathcal{A})
$$

where $H\left(A_{i}\right)$ denotes the entropy of the random variable $A_{i}$,

$$
H\left(A_{i}\right)=-\sum_{\left(x \in \Omega_{i}\right)} \operatorname{Pr}\left[A_{i}=x\right] \log \operatorname{Pr}\left[A_{i}=x\right]
$$

and $I(\cdot, \cdot)$ denotes the mutual information between the two variables:
$I\left(A_{i}, \Pi_{i}\right)$
$=\sum_{x \in \Pi_{i}} \sum_{y \in \operatorname{dom}\left(\Pi_{i}\right)} \operatorname{Pr}\left[A_{i}=x, \Pi_{i}=y\right] \log \frac{\operatorname{Pr}\left[A_{i}=x, \Pi_{i}=y\right]}{\operatorname{Pr}\left[A_{i}=x\right] \operatorname{Pr}\left[\Pi_{i}=y\right]}$
Here, $\operatorname{Pr}\left[A_{i}, \Pi_{i}\right]$ is the joint distribution of $A_{i}$ and $\Pi_{i}$, $\operatorname{Pr}\left[A_{i}\right]$ and $\operatorname{Pr}\left[\Pi_{i}\right]$ are the marginal distributions of $A_{i}$ and $\Pi_{i}$, respectively, and $H(\mathcal{A})$ is the joint entropy of all attribute variables in $\mathcal{A}$, which is defined as:
$H(\mathcal{A})=H\left(A_{1}, A_{2}, \cdots, A_{d}\right)$
$=-\sum_{\left(x_{1} \in \Pi_{1}\right)} \cdots \sum_{\left(x_{d} \in \Pi_{d}\right)} \operatorname{Pr}\left[A_{1}=x_{1}, \cdots, A_{d}=x_{d}\right] \log \operatorname{Pr}\left[A_{1}=x_{1}, \cdots, A_{d}=x_{d}\right]$
Therefore, learning a Bayesian network is to find $\mathcal{N}$ from $D$ with the minimum $K L\left(\operatorname{Pr}[\mathcal{A}], \operatorname{Pr}_{\mathcal{N}}[\mathcal{A}]\right)$. The construction of $\mathcal{N}$ can be modeled as choosing a parent set $\Pi_{i}$ for each attribute $A_{i}$ to maximize $\sum_{i=1}^{d} I\left(A_{i}, \Pi_{i}\right)$ since $\sum_{i=1}^{d} H\left(A_{i}\right)-$ $H(\mathcal{A})$ is fixed once the dataset $D$ is given.

### 3.3 Differential Privacy

Differential privacy (DP) has become the de facto standard of privacy preservation, which ensures that query results of a dataset are insensitive to the change of a single record. Differential privacy is defined based on the neighboring datasets $D$ and $D^{\prime}$, where $D^{\prime}$ differs from $D$ by only one record:
Definition 1 (Differential privacy [25]). A randomized algorithm $M$ is $\epsilon$-differentially private if for any pair of neighboring datasets $D$ and $D^{\prime}$, and for all sets $S$ of possible outputs, we have

$$
\operatorname{Pr}[M(D) \in S] \leq e^{\epsilon} \operatorname{Pr}\left[M\left(D^{\prime}\right) \in S\right]
$$

where $\epsilon$ is often a small positive real number.
The smaller the $\epsilon$, the higher the level of privacy preservation. A smaller $\epsilon$ provides greater privacy preservation at the cost of lower data accuracy with more added noise. Differential privacy can be achieved by two best known mechanisms, namely the Laplace mechanism [25] and the exponential mechanism [26]. We provide the formal definition of the exponential mechanism as follows:
Definition 2 (Exponential Mechanism [26]). Given a random algorithm $M$ with the input dataset $D$ and the output entity object $o \in R$, where $R$ is the output range. Let $q(D, o)$ be the utility function and $\Delta q$ be the global sensitivity of function $q(D, o)$. If algorithm $M$ selects and outputs o from $R$ at a probability proportional to $\exp \left(\frac{\operatorname{cq}(D, o)}{2 \Delta q}\right)$, then $M$ is $\epsilon$-differentially private.

DP techniques implicitly assume a trusted third party to collect data and thus can hardly be applied to the case where a server is not reliable. Therefore local differential privacy (LDP) emerges, in which each user independently and locally conducts data perturbation. The formal definition of LDP can be shown as follows:
Definition 3 (Local Differential Privacy [27]). Consider $n$ records. A privacy algorithm $M$ with domain $\operatorname{Dom}(M)$ and range $\operatorname{Ran}(M)$ satisfies the $\epsilon$-local differential privacy if $M$ obtains the same output result $t^{*}\left(t^{*} \subseteq \operatorname{Ran}(M)\right)$ on any two records $t$ and $t^{\prime}\left(t, t^{\prime} \in \operatorname{Dom}(M)\right)$ with

$$
\operatorname{Pr}\left[M(t)=t^{*}\right] \leq e^{\epsilon} \times \operatorname{Pr}\left[M\left(t^{\prime}\right)=t^{*}\right]
$$

Local differential privacy ensures the similarity between the output results of any two records. Random response (RR) [28] is currently the most widely used technique for achieving local differential privacy.

### 3.4 Random Response and Post Randomization

Random response (RR) is a technique developed in social science to collect statistical data about individuals' sensitive information. Its main idea is to provide data privacy protection by making use of the uncertainty of responses to sensitive questions. Privacy comes from the randomness of the answers while accuracy comes from the noise generation procedure [29].

Post randomization (PRAM) is another important perturbation technique for privacy protection, which stochastically transforms each record in a dataset using pre-selected probabilities. For a random variable $X$ with $s$ categories $c_{1}, c_{2}, \cdots, c_{s}$, let $\pi_{i}=\operatorname{Pr}\left[X=c_{i}\right], i=1, \cdots, s$, and $\tilde{\pi}=$ $\left(\pi_{1}, \cdots, \pi_{s}\right)^{\mathrm{T}}$. The basic idea of PRAM is to select a transition probability matrix $P=\left\langle p_{i j}\right\rangle$ with $\sum_{j} p_{i j}=1$ for $i=$ $1,2, \cdots, s$. Then the original category $c_{i}$ is changed to $c_{j}$ with probability $p_{i j}$. Let $Z$ denote the transformed variable. We have $p_{i j}=\operatorname{Pr}\left(Z=c_{j} \mid X=c_{i}\right), \lambda_{i}=\operatorname{Pr}\left[Z=c_{i}\right], i=1, \cdots, s$, and $\tilde{\lambda}=\left(\lambda_{1}, \cdots, \lambda_{s}\right)^{\mathrm{T}}$.

Mathematically, PRAM is equivalent to RR. Therefore many mathematical results developed for RR such as the local differential privacy guarantee can be applied to PRAM [30]. In this paper, we employ PRAM for the case when a trusted data server is available (Section 4), where all the data can be processed at the server to maintain differential privacy, and RR for the case when the server is semihonest, in which case local differential privacy is adopted for collecting data from each user to the server (Section 5).

## 4 DP2-Pub With a Trusted Server

In this section, we propose a novel differentially private high-dimensional data publication mechanism based on a double-perturbation process, namely DP2-Pub, assuming the availability of a trusted server that can access the original data. We first present an overview on DP2-Pub, then detail its modules in the following subsections.

### 4.1 Overview

Figure 2 illustrates the main procedure of DP2-Pub, which runs in two phases of attribute clustering and data randomization, with both being performed by the trusted server. Since both phases require access to the original dataset, we divide the total privacy budget $\epsilon$ into two portions with $\epsilon_{1}$ being used for the first phase and $\epsilon_{2}$ for the second phase, and demonstrate that the two phases are both differentially private.

1. Bayesian Network and Attribute Clustering. To learn the correlations between different attribute variables, we adopt the approach of constructing a differentially private Bayesian network through the exponential mechanism presented in [9]. Based on the constructed Bayesian network, we propose the procedure of attribute clustering using the

![img-1.jpeg](img-1.jpeg)

Fig. 2. Overview of DP2-Pub.

Markov blanket model to achieve high intra-cluster cohesion and low inter-cluster coupling. Each cluster is composed of a cluster head and its Markov blanket members, thus the attribute set can be divided into a number of disjoint clusters denoted as CL1, ···, CLt. Our most fundamental purpose is to realize attribute clustering, and then to obtain a reasonable allocation of privacy budget for each cluster based on its importance.

**2. Data Randomization.** We propose an invariant post randomization method (PRAM) and apply it to each attribute cluster. Note that PRAM is an important technique for data perturbation, and that a PRAM is invariant if the transition probability matrix P satisfies Pπ̃ = π̃ (except for the identity matrix I). The appealing advantage of an invariant PRAM lies in that there is no loss of statistical information and thus can significantly preserve data utility. The key point to construct an invariant PRAM is to delicately solve P satisfying Pπ̃ = π̃. We design a double-perturbation mechanism to achieve the invariant property of PRAM for two-valued and multivalued attributes.

### 4.2 Differentially Private Bayesian Network Construction

In this section, we adopt the algorithm proposed in [9] to construct our Bayesian network in a differentially private manner, which employs the exponential mechanism to select (A_i, Π_i), using the mutual information I as the score function. For completeness, we present the algorithm in Algorithm 1.

At the beginning of Algorithm 1, we initialize the Bayesian network N to be an empty set. Let V denote the set containing the attributes whose parent sets have been fixed and the initial set of V is empty (Line 1). Then we randomly select an attribute from the d attributes as the initial node and set its parent set empty (Line 2). For each A_i, its AP pair is selected in a differentially private manner by the exponential mechanism (Lines 3-7), of which the mutual information I is taken as the score function, and ∆ is its global sensitivity. Algorithm 1 ensures that each invocation of the exponential mechanism satisfies (e1/(d − 1))-differential privacy, and the exponential mechanism is invoked d − 1 times, so the construction of N is e1-differentially private based on DP's composability property (Lines 3 − 7). We adopt the calculation of the sensitivity ∆ of the mutual information in [9], which is shown as follows:

$$
\Delta = \begin{cases}
\frac{1}{n} \log(n) + \frac{n-1}{n} \log\left(\frac{n}{n-1}\right), & \text{if } A_i \text{ or } Π_i \text{ is binary,} \\
\frac{2}{n} \log\left(\frac{n+1}{2}\right) + \frac{n-1}{n} \log\left(\frac{n+1}{n-1}\right), & \text{otherwise.}
\end{cases}
$$

#### 4.3 Attribute Clustering

Given a Bayesian network, the Markov blanket MB(x) of an attribute variable x can be intuitively represented as the set of parent nodes Pa(x) and child nodes Ch(x) of x as well as the set of parent nodes of x's child nodes, which can be formalized as follows:

$$
MB(x) = Pa(x) \bigcup Ch(x) \bigcup \{Pa(y) \mid y \in Ch(x)\}
$$

We propose a procedure of attribute clustering shown in Algorithm 2. First, we initialize the set S to include all the attributes of N. Then we randomly select an attribute x, add MB(x) and x into a cluster, and delete all these attributes from S. Repeat this procedure until S is empty. Each cluster is composed of a cluster head (an attribute variable x) and its Markov blanket members. Thus, the attribute set can be divided into a number of disjoint clusters, which can be denoted as CL1, ···, CLt.

#### Algorithm 2: Attribute Clustering

**Input:** Bayesian Network N
**Output:** Cluster CL1, CL2···, CLt
1 S = Set of all attributes of N;
2 i = 0;
3 **while** S ≠ ∅ **do**
4 i = i + 1;
5 Randomly select the attribute x in S and let CLt = MB(x) ⊥ {x};
6 S = S − CLt;
7 **return** CL1, CL2···, CLt

The key to overcome the curse of dimensionality is to decompose high-dimensional data into a set of low-dimensional data based on the conditional independences of the data. Bayesian network and Markov blanket are the most widely used graphical models for identifying a minimal set of attributes with strong correlations. Specifically, for any attribute variable A_i in the Bayesian network, its

Markov blanket is the set of attributes which are strongly corelated to $A_{i}$, while the attributes not in $A_{i}$ 's Markov blanket are loosely correlated with $A_{i}$ or even conditionally independent of $A_{i}$. Therefore, our clustering algorithm yields attribute clusters with high intra-cluster correlation (cohesion) and low inter-cluster coupling which can improve the accuracy of the estimated joint distribution of the data. Note that the input of Algorithm 2 is the differentially private Bayesian network constructed from Algorithm 1, which guarantees that the operation of attribute clustering does not break differential privacy.

According to the attribute clustering process, a reasonable allocation of the privacy budget for the next data randomization phase is determined by the conditional independence among the attributes in a cluster and the importance of the cluster based on the probability distributions over the dataset. Thus we define the importance factor (CIF) of each cluster $C L_{i}, 1 \leq i \leq t$, in (2), which measures the importance of each cluster. The higher the CIF, the more important the cluster.

$$
\operatorname{CIF}\left(C L_{i}\right)=\frac{\sum_{A_{j} \in C L_{i}} H\left(A_{j}\right)}{\sum_{k=1}^{d} H\left(A_{k}\right)}
$$

Based on the CIF, one can allocate a privacy budget to each cluster, following the principle stating that the smaller the privacy budget, the higher the level of privacy preservation. Therefore, we define the privacy budget coefficient (PBC) for each cluster $C L_{i}$ as follows:

$$
P B C\left(C L_{i}\right)=\frac{\frac{1}{C I F\left(C L_{i}\right)}}{\sum_{j=1}^{d} \frac{1}{C I F\left(C L_{j}\right)}}
$$

Note that (3) conducts a normalization of PBC so that it falls into the $[0,1]$ interval. As the privacy budget of the data randomization is $\epsilon_{2}$, which will be carried out on each cluster at the server, the privacy budget allocated for cluster $C L_{i}$ is $P B C\left(C L_{i}\right) \cdot \epsilon_{2}$.

### 4.4 Invariant PRAM

The characteristic of an invariant PRAM lies in that the transition probability matrix $P$ satisfying $P \vec{\pi}=\vec{\pi}$. In this section, we propose an invariant PRAM scheme, which is suitable for categorical attributes. The main idea of our approach is to compute $P$ via double-perturbation, as shown in Figure 3. For an attribute variable $X$, let $X_{1}$ denote the perturbed variable after the first perturbation, and $X_{2}$ denote the one after the second perturbation. We first construct a transition probability matrix $Q=\left(q_{i j}\right)$ satisfying differential privacy and conduct the first perturbation on the attribute variable $X$ according $Q$. Then we compute the estimate of $\pi$ based on the perturbed data $X_{1}$, denoted as $\hat{\pi}$, construct the transition probability matrix $\hat{Q}=\left(\hat{q}_{i j}\right)$ for the second perturbation according to a specific rule to achieve $\hat{Q} \cdot Q \cdot \vec{\pi}=\vec{\pi}$, and finally carry out the second perturbation on $X_{1}$ based on $\hat{Q}$ to obtain $X_{2}$. More specifically, the rule of constructing $\hat{Q}$ is to set $\hat{q}_{j i}=P r\left(X=c_{i} \mid X_{1}=c_{j}\right)$, where $\hat{q}_{j i}$ denotes the probability of $X_{1}$ being changed from category $c_{j}$ to
$c_{i}$ in the second perturbation. In other words, $\hat{Q}$ can be considered as the inverse of $Q$ while ensuring that $\hat{Q}$ is also a transition probability matrix. Thus, the doubleperturbation is an invariant PRAM with $P=\hat{Q} \cdot Q$, and it satisfies differential privacy since the first perturbation satisfies differential privacy and the second perturbation is a randomized mapping of the first one.
![img-2.jpeg](img-2.jpeg)

Fig. 3. Process of Double Perturbation.
The attribute variables can be either two-valued or multivalued. For better elaboration, we detail the construction of the transition probability matrix for a two-valued attribute first and then extend the procedure to multivalued attributes. Following that, we apply the construction to compound variables and present the analysis on the privacy guarantee.

### 4.4.1 Two-Valued Attributes

We start from the case of a categorical attribute variable $X$ with only two possible values of $c_{1}$ and $c_{2}$. Let $\pi_{1}=P r[X=$ $\left.c_{1}\right]$ and $\pi_{2}=P r\left[X=c_{2}\right]$; denoted by $\vec{\pi}=\left(\pi_{1}, \pi_{2}\right)^{\mathrm{T}}$. The data randomization process is conducted in a way that $c_{1}$ or $c_{2}$ either remains unchanged with probability $q$, or is changed to the other value with the probability of $1-q$; that is $q_{11}=q_{22}=q$ and $q_{12}=q_{21}=1-q$. Thus, the transition probability matrix $Q$ of the two-valued variable $X$ is a $2 \times 2$ matrix, which can be shown as follows:

$$
Q=\left[\begin{array}{cc}
q & 1-q \\
1-q & q
\end{array}\right]
$$

Let $\lambda_{1}=P r\left[X_{1}=c_{1}\right]$ and $\lambda_{2}=P r\left[X_{1}=c_{2}\right]$; set $\vec{\lambda}=\left(\lambda_{1}, \lambda_{2}\right)^{\mathrm{T}}$. Note that the transition probability matrix satisfies $\vec{\lambda}=Q \vec{\pi}$.

In this setting, let $q=\frac{e^{e}}{1+e^{e}}$. Then the local differential privacy can be satisfied as:

$$
\frac{P r\left(X_{1}=c_{1} \mid X=c_{1}\right)}{P r\left(X_{1}=c_{1} \mid X=c_{2}\right)} \leq \frac{q}{1-q} \leq e^{e}
$$

As mentioned earlier, we propose our invariant post randomization method to preserve the statistical information and data utility to the greatest possible extent, which first adopts transition probability matrix $Q$ on the original attribute variable $X$, estimates the probability distribution of the variable $X$ based on the perturbed data after the first perturbation, and constructs the transition probability matrix $\hat{Q}$ for the second perturbation according to the transition probability matrix $Q$ and the probability distribution of the perturbed data $X_{1}$. The advantage of this doubleperturbation mechanism lies in that there is no need to know

the probability distribution of the original data in advancewe actually do not know the probability distribution of $X$-the transition probability matrix of the original data is thus constructed adaptively. After obtaining the perturbed data $X_{1}$ with $\tilde{\lambda}$, we can obtain the estimate of the original attribute variable distribution:

$$
\tilde{\tilde{\pi}}=Q^{-1} \tilde{\lambda}
$$

Then we compute the transition probability of each variable for the second perturbation as follows:

$$
\begin{gathered}
\tilde{q}_{11}=\operatorname{Pr}\left(X=c_{1} \mid X_{1}=c_{1}\right)=\frac{\tilde{\pi}_{1} \cdot q}{q \cdot \tilde{\pi}_{1}+(1-q) \cdot \tilde{\pi}_{2}} \\
\tilde{q}_{22}=\operatorname{Pr}\left(X=c_{2} \mid X_{1}=c_{2}\right)=\frac{\tilde{\pi}_{2} \cdot q}{q \cdot \tilde{\pi}_{2}+(1-q) \cdot \tilde{\pi}_{1}} \\
\tilde{q}_{12}=\operatorname{Pr}\left(X=c_{2} \mid X_{1}=c_{1}\right)=\frac{\tilde{\pi}_{2} \cdot(1-q)}{q \cdot \tilde{\pi}_{1}+(1-q) \cdot \tilde{\pi}_{2}}=1-\tilde{q}_{11} \\
\tilde{q}_{21}=\operatorname{Pr}\left(X=c_{1} \mid X_{1}=c_{2}\right)=\frac{\tilde{\pi}_{1} \cdot(1-q)}{q \cdot \tilde{\pi}_{2}+(1-q) \cdot \tilde{\pi}_{1}}=1-\tilde{q}_{22}
\end{gathered}
$$

Accordingly, we obtain the transition probability matrix for the second perturbation:

$$
\tilde{Q}=\left[\begin{array}{ll}
\tilde{q}_{11} & \tilde{q}_{12} \\
\tilde{q}_{21} & \tilde{q}_{22}
\end{array}\right]=\left[\begin{array}{ll}
\frac{\tilde{\pi}_{1} \cdot q}{q \cdot \tilde{\pi}_{1}+(1-q) \cdot \tilde{\pi}_{2}} & \frac{(1-q) \cdot \tilde{\pi}_{2}}{q \cdot \tilde{\pi}_{1}+(1-q) \cdot \tilde{\pi}_{2}} \\
\frac{(1-q) \cdot \tilde{\pi}_{1}}{q \cdot \tilde{\pi}_{2}+(1-q) \cdot \tilde{\pi}_{1}} & \frac{\tilde{\pi}_{2} \cdot q}{q \cdot \tilde{\pi}_{2}+(1-q) \cdot \tilde{\pi}_{1}}
\end{array}\right]
$$

Therefore, to obtain the invariant PRAMed data $X_{2}$ of the attribute variable $X$, we apply $\tilde{Q}$ to the perturbed data $X_{1}$ during the second perturbation. These two phases of data perturbation with $Q$ and $\tilde{Q}$ successfully realize an invariant PRAM with $P=Q \cdot \tilde{Q}$, where $\tilde{Q}$ can be considered as the inverse of $Q$ while ensuring that $\tilde{Q}$ is also a transition probability matrix.

### 4.4.2 Multivalued Attributes

The perturbation of the multivalued attributes is similar to that of the two-valued one. We consider a categorical random variable with $s$ possible values $c_{1}, c_{2} \cdots, c_{s}$. Let $\pi_{i}=\operatorname{Pr}\left[X=c_{i}\right], i=1, \cdots, s$ and $\tilde{\pi}=\left(\pi_{1}, \cdots, \pi_{s}\right)^{\mathrm{T}}$. Given that $X$ belongs to category $c_{i}$, it either remains unchanged with probability $q_{i i}$, or is changed uniformly at random with the probability of $\frac{1-q_{i i}}{s-1}$ to one of the other $s-1$ categories. That is, the transition probability matrix is a $s \times s$ one, which can be formalized as follows:

$$
Q=\left[\begin{array}{cccc}
q_{11} & \frac{1-q_{11}}{s-1} & \cdots & \frac{1-q_{11}}{s-1} \\
\frac{1-q_{22}}{s-1} & q_{22} & \cdots & \frac{1-q_{22}}{s-1} \\
\cdots & \cdots & \cdots & \cdots \\
\frac{1-q_{s s}}{s-1} & \frac{1-q_{s s}}{s-1} & \cdots & q_{s s}
\end{array}\right]
$$

To satisfy local differential privacy, we set $q_{11}=q_{22}=$ $\cdots=q_{s s}=\frac{e^{r}}{s-1+e^{r}}$, then $Q$ can be denoted as:

$$
Q=\left[\begin{array}{cccc}
\frac{e^{r}}{s-1+e^{r}} & \frac{1}{s-1+e^{r}} & \cdots & \frac{1}{s-1+e^{r}} \\
\frac{1}{s-1+e^{r}} & \frac{e^{r}}{s-1+e^{r}} & \cdots & \frac{1}{s-1+e^{r}} \\
\cdots & \cdots & \cdots & \cdots \\
\frac{1}{s-1+e^{r}} & \frac{1}{s-1+e^{r}} & \cdots & \frac{e^{r}}{s-1+e^{r}}
\end{array}\right]
$$

The PRAMed variable can be denoted as ${ }_{1}$ after applying $Q$ to $X$. Correspondingly, let $\lambda_{i}=\operatorname{Pr}\left[X_{1}=c_{i}\right], i=1, \cdots, s, \tilde{\lambda}=$ $\left(\lambda_{1}, \cdots, \lambda_{s}\right)^{\mathrm{T}}$. In this setting, the local differential privacy condition can be satisfied as:

$$
\frac{\operatorname{Pr}\left(X_{1}=c_{i} \mid X=c_{i}\right)}{\operatorname{Pr}\left(X_{1}=c_{i} \mid X^{\prime} \neq c_{i}\right)} \leq \frac{q_{i i}}{q_{j i}(j \neq i)} \leq e^{r}
$$

We can compute the estimated $\tilde{\tilde{\pi}}$ of the original attribute variable $X$ as

$$
\tilde{\tilde{\pi}}=Q^{-1} \cdot \tilde{\lambda}
$$

Then the elements of the transition probability matrix $\tilde{Q}$ for the second perturbation can be computed as:

$$
\tilde{q}_{i j}=\operatorname{Pr}\left(X=c_{j} \mid X_{1}=c_{i}\right)=\frac{\tilde{\pi}_{j} \cdot q_{j i}}{\sum_{k=1}^{s} \tilde{\pi}_{k} \cdot q_{k i}}
$$

It can be observed that $\sum_{j=1}^{s} \tilde{q}_{i j}=1$, which satisfies the property of a transition probability matrix. We take $\sum_{j=1}^{s} \tilde{q}_{1 j}$ as an example:

$$
\begin{aligned}
& \sum_{j=1}^{s} \tilde{q}_{1 j}=\tilde{q}_{11}+\tilde{q}_{12}+\cdots+\tilde{q}_{1 s} \\
& =\operatorname{Pr}\left(X=c_{1} \mid X_{1}=c_{1}\right)+\operatorname{Pr}\left(X=c_{2} \mid X_{1}=c_{1}\right)+\cdots+\operatorname{Pr}\left(X=c_{s} \mid X_{1}=c_{1}\right) \\
& =\frac{\tilde{\pi}_{1} \cdot q_{11}}{\sum_{k=1}^{s} \tilde{\pi}_{k} \cdot q_{k 1}}+\frac{\tilde{\pi}_{2} \cdot q_{21}}{\sum_{k=1}^{s} \tilde{\pi}_{k} \cdot q_{k 1}}+\cdots \frac{\tilde{\pi}_{s} \cdot q_{s 1}}{\sum_{k=1}^{s} \tilde{\pi}_{k} \cdot q_{k 1}} \\
& =1
\end{aligned}
$$

After applying $\tilde{Q}$ to the perturbed data $X_{1}$ in the second perturbation, we obtain the invariant PRAM result $X_{2}$ of the attribute variable $X$.

### 4.4.3 Compound Variables

Since an attribute cluster may include more than one twovalued or multivalued attribute variables which are strongly correlated, one can treat all these variables as a compound one. Thus an invariant PRAM for compound variables [30] is needed, which first computes the transition probability matrix for each attribute variable, then computes the transition probability matrix for the compound one. For example, for two categorical variables $X$ with $r$ categories and $Y$ with $s$ categories, we may first compute the invariant PRAM transition probability matrix of $X$ and $Y$, denoted as $E=\left(e_{i j}\right)$ and $F=\left(f_{i j}\right)$, respectively. Then the combination of $X$ and $Y$ can

$$
\begin{aligned}
& Q_{E F}=E \otimes F= \\
& \left[\begin{array}{cccccc}
e_{11} f_{11} & e_{11} f_{12} & \cdots e_{11} f_{1 s} & & e_{1 r} f_{11} & e_{1 r} f_{12} & \cdots e_{1 r} f_{1 s} \\
e_{11} f_{s 1} & e_{11} f_{s 2} & \cdots e_{11} f_{s s} & & e_{1 r} f_{s 1} & e_{1 r} f_{s 2} & \cdots e_{1 r} f_{s s} \\
& \vdots & & \ddots & & \vdots & \\
e_{r 1} f_{11} & e_{r 1} f_{12} & \cdots e_{r 1} f_{1 s} & & e_{r r} f_{11} & e_{r r} f_{12} & \cdots e_{r r} f_{1 s} \\
e_{r 1} f_{s 1} & e_{r 1} f_{s 2} & \cdots e_{r 1} f_{s s} & & e_{r r} f_{s 1} & e_{r r} f_{s 2} & \cdots e_{r r} f_{s s}
\end{array}\right]
\end{aligned}
$$

Similarly, when there exist three categorical variables $X, Y, Z$ with respectively $r, s, t$ categories, we may first

compute the invariant PRAM transition probability matrix of $X, Y$ and $Z$, denoted as $E=\left(e_{i j}\right), F=\left(f_{i j}\right)$ and $G=\left(g_{i j}\right)$. Then the combination of $X, Y$ and $Z$ can be regarded as a compound variable with $r \cdot s \cdot t$ categories, whose transition probability $Q_{E F G}$ is the Kronecker product of $E, F$ and $G$, which is a $(r \cdot s \cdot t) \times(r \cdot s \cdot t)$ matrix.

As mentioned earlier, when applying the proposed invariant PRAM to each cluster, we need to allocate privacy budget $P B C\left(C L_{i}\right) \cdot \epsilon_{2}$ to cluster $C L_{i}$. If a cluster $C L_{i}$ includes more than one attribute variable, we first compute the transition probability matrix for each attribute variable with uniformly allocated privacy budget $\frac{P B C\left(C L_{i}\right) \cdot \epsilon_{2}}{\left|C L_{i}\right|}$, then compute the transition probability matrix for the compound variable.

### 4.5 Privacy Analysis

As discussed in Section 4.2, Algorithm 1 satisfies $\epsilon_{1}$ differential privacy, i.e., the procedure of Bayesian network construction satisfies differential privacy. The procedure of attribute clustering just simply cluster the attributes based on the constructed Bayesian network, which does not disclose more information. Therefore, one can say that the first phase of DP2-Pub, i.e., Bayesian network construction and attribute clustering, satisfies $\epsilon_{1}$-differential privacy.

Now we analyze the second phase, i.e., the phase of data randomization. According to [29], differential privacy is resistant to any randomized mapping of differentially private results. More specifically, with randomized mapping, a data analyst cannot make the output of a differentially private algorithm $M$ less differentially private without any additional knowledge about the private dataset [29]. That is, if an algorithm is differentially private, simply conducting randomized mapping on the output of the algorithm without any additional knowledge does not leak any extra private information, which has been proved by the following PostProcessing Proposition [29]:

Proposition 1. (Post-Processing [29]) Let $M: D \rightarrow R$ be a randomized algorithm that is $\epsilon$-differentially private. Let $f: R \rightarrow$ $R^{t}$ be an arbitrary randomized mapping. Then $f \circ M: D \rightarrow R^{t}$ is $\epsilon$-differentially private.

Theorem 1. The double-perturbation of Invariant PRAM satisfies $\epsilon_{2}$-differential privacy.
Proof. The first perturbation of each attribute variable is a post randomization satisfying local differential privacy for both two-valued and multivalued variables:

$$
\begin{gathered}
\frac{\operatorname{Pr}\left(X_{1}=c_{1} \mid X=c_{1}\right)}{\operatorname{Pr}\left(X_{1}=c_{1} \mid X=c_{2}\right)} \leq \frac{q}{1-q} \\
\frac{\operatorname{Pr}\left(X_{1}=c_{i} \mid X=c_{i}\right)}{\operatorname{Pr}\left(X_{1}=c_{i} \mid X^{t} \neq c_{i}\right)} \leq \frac{q_{i i}}{q_{j i}(j \neq i)}
\end{gathered}
$$

of which $q$ and $q_{i i}$ are determined by the privacy budget allocated for each attribute variable in a cluster. According to Proposition 1, the second random perturbation of our invariant PRAM mechanism can be considered as a randomized mapping of the differentially private algorithm output, that is, a randomized mapping based post-processing of differential privacy.

Since each cluster $C L_{i}$ is $P B C\left(C L_{i}\right) \cdot \epsilon_{2}$-differentially private, the $t$ clusters can be regarded as a $t$-dimensional
dataset achieving $\epsilon_{2}$-differential privacy according to the sequential composition theorem [31].

Accordingly, one can obtain the following theorem.
Theorem 2. The DP2-Pub satisfies $\left(\epsilon_{1}+\epsilon_{2}\right)$-differential privacy according to sequential composition theorem [31].

## 5 DP2-Pub With a Semi-honest Server

In many practical settings the central data server may not be trustworthy - it is generally semi-honest, i.e., honest-butcurious, which faithfully follows the protocol but tries its best to infer as much knowledge as possible. Therefore in this section, we extend our DP2-Pub mechanism to consider a semi-honest server. A number of users generate multidimensional data records, then send them to a server who intends to release an approximate dataset to third-parties for various applications. Formally, each user contributes a data record constituting a dataset $D=\left\{U^{1}, U^{2}, \cdots U^{n}\right\}$, where $U^{i}$ denotes the data record of user $i$ and $n$ is the total number of records/users.

Figure 4 illustrates the main procedure of DP2-Pub with a semi-honest server, which includes three main steps: privacy preservation of local data satisfying local differential privacy, Markov-blanket-based cluster learning based on Bayesian network, and the PRAM perturbation on the private data. Both the attribute clustering and PRAM perturbation are conducted at the data server, while the local differential privacy protection is performed by each user. Although the data server is semi-honest, it can only access the private data processed by each user.
![img-3.jpeg](img-3.jpeg)

Fig. 4. Overview of DP2-Pub with a Semi-honest Server.
We first propose a local randomization using RR on each user's data making it satisfy LDP, then the sanitized data is sent to and aggregated at the central server. Each user $i$ has a $d$-dimensional data record $U^{i}=\left[u_{1}^{i}, u_{2}^{i}, \cdots u_{d}^{i}\right]$, and the perturbation process is conducted on each dimension with the privacy budget $\epsilon^{t}=\epsilon / d$.

If $u_{j}^{i}$ is the value of a two-valued attribute, it is randomly flipped according to the following rule in RR:

$$
u_{j}^{i}= \begin{cases}u_{j}^{i}, & \text { with probability of } q=\frac{\epsilon^{t^{i}}}{\frac{1+\epsilon^{t}}{}}\{1-q^{\epsilon^{t}} \}\end{cases}
$$

If $u_{j}^{i}$ is the value of a multivalued attribute with $s$ possible values $c_{1}, c_{2}, \cdots c_{s}$, it is randomly flipped according to the following rule in RR:

$$
u_{j}^{i}= \begin{cases}u_{j}^{i}, & \text { with probability of } q_{s s}=\frac{e^{s_{i}}}{s-1+e^{e^{s}}} \\ c_{k} \neq u_{j}^{i}, & \text { with probability of } \frac{1}{s-1+e^{e^{s}}}\end{cases}
$$

of which $k=1,2, \cdots, s$.
After receiving the noisy data from each user, the server computes the marginal probability distribution $\widehat{\lambda}$, estimates the original distribution $\widehat{\pi}$, and then calculates $Q$ for each attribute variable according to the methods presented in Sections 4.4.1 and 4.4.2. Then it constructs a Bayesian network and conducts attribute clustering on the aggregated data to learn the correlations between different attribute variables. The processes of Bayesian network construction and attribute clustering are similar to those in Sections 4.2 and 4.3 except for a few minor changes: replace Line 6 of Algorithm 1 with a procedure that selects $\left(A_{i}, \Pi_{i}\right)$ with the largest $I(A, \Pi)$, since the process of the Bayesian network construction does not need to satisfy differential privacy, as the aggregated data at the server is already differentially private (guaranteed by local differential privacy). To further improve accuracy, Line 5 of Algorithm 2 can be replaced by "Select the attribute $x$ with the maximal entropy in $S$ ".
Next the server calculates $\hat{Q}$ for each attribute variable based on $\widehat{\pi}$ and $Q$. Then the server conducts the randomized perturbation by applying $\hat{Q}$ on the aggregated data to achieve invariant PRAM. According to the attribute clustering, each cluster may include more than one attribute variable which are strongly correlated. Thus we compute the transition probability matrix of the compound variable following the procedure presented in Section 4.4.3.
Theorem 3. The DP2-Pub with a semi-honest server satisfies $\epsilon$-local differential privacy.
Proof. Each user perturbs its data record individually with the help of random response to get the privatized data, which provides local differential privacy. The operations of the server are all conducted on the privacy-preserved data, and the PRAM perturbation can be considered as a randomized mapping (post processing) without breaking differential privacy. Therefore, the DP2-Pub mechanism with a semi-honest server is differentially private with privacy budget $\epsilon$.

## 6 EXPERIMENTAL EVALUATIONS

In this section, we conduct extensive experiments to demonstrate the performance of our DP2-Pub mechanism and compare it with two benchmark approaches, PrivBayes [10] and DPPro [13], on four real-world datasets of NLTCS [32], ACS [33], BR2000 [33] and Adult [34]. The data utility is evaluated and analyzed from two aspects, namely the total variation distance between the original dataset and the perturbed dataset, and the classification error rate of the SVM classification on the perturbed datasets.

### 6.1 Experimental Settings

### 6.1.1 Datasets

We make use of four real-world datasets in our experiments: NLTCS [32] consists of records of 21574 individuals partic-
ipated in the National Long Term Care Survey, and each record has 16 attributes; ACS [33] includes 47461 records of personal information from the 2013 and 2014 ACS sample sets in IPUMS-USA, where each record has 23 attributes; BR2000 [33] consists of 38000 census records with 14 attributes collected from Brazil in the year 2000; and Adult [34] contains personal information such as gender, salary, and education level of 45222 records extracted from the 1994 US Census, where each record has 15 attributes. The first two datasets only contain binary attribute values while the last two possess continuous as well as categorical attributes with multiple values. We summarize the statistics of these datasets in Table 2.

TABLE 2
Data Statistics


### 6.1.2 Evaluation Metrics

We consider two tasks to evaluate the performance of DP2-Pub. The first task is to study the accuracy of $\alpha$-way marginals of the perturbed datasets. We evaluate the $\alpha$-way marginals of the four datasets by adopting the total variation distance [24] between the noisy marginal distribution and that of the original datasets, which is shown in Eq. (5).

$$
A V D(X, Z)=\frac{1}{2}\left\|P_{X}-P_{Z}\right\|_{1}=\frac{1}{2} \sum_{w \in \Omega}\left|P_{X}(w)-P_{Z}(w)\right|
$$

where $\Omega$ is the domain of the probability variable $X$ and $Z$; $P_{X}$ and $P_{Z}$ are the probability distributions of the original attribute variable $X$ and the perturbed one $Z$, respectively.

Then we compute the average results of the total variation distance over all $\alpha$-way marginals as the final result - a lower distance implies a better utility. More specifically, in our experiments, we evaluate the 3 -way and 4 way marginals on binary datasets NLTCS and ACS, and 2-way and 3-way marginals on BR2000 and Adult, since the domain size of BR2000 and Adult are prohibitively large leading to very complex joint distributions.

The second task is to evaluate the classification results of SVM classifiers. The purpose of data publication is to conduct data analysis and data mining. We adopt SVM to evaluate the data utility from the perspective of data applications, as SVM is the most popular classification approach among various data mining techniques with powerful discriminative features both in linear and non-linear classifications [35]. Specifically, we train two classifiers on ACS to predict whether an individual: (1) goes to school, (2) lives in a multi-generation family; four classifiers are constructed on NLTCS to predict whether an individual: (1) is unable to go outside, (2) is unable to manage money, (3) is unable to bathe, and (4) is unable to travel; two classifiers are trained on BR2000 to predict whether an individual (1) owns a private dwelling, (2) is a Catholic; and two classifiers are trained on Adult to predict whether an individual (1) is a female, (2) makes over 50 K a year. For each classifier, we

use $80 \%$ of the tuples of the dataset for training and the other $20 \%$ as the testing set. The prediction accuracy of each SVM classifier is measured by the misclassification rate on the testing set.

### 6.1.3 Comparison Approaches

For the two evaluation metrics mentioned above, we compare our mechanism DP2-Pub with two existing approaches: (1) PrivBayes [10], which first constructs a Bayesian network to model the correlations among the attributes in a dataset, then injects noise into each marginal distribution in the Bayesian network to realize differential privacy, and finally constructs an approximation to the data distribution of the original dataset using the Bayesian network and the noisy marginal distributions; (2) DPPro [13], which projects a $d$-dimensional vector representation of a user's attributes into a lower $d$-dimensional space by a random projection, and then adds noise to each resultant vector. Note that we choose PrivBayes and DPPro for our comparison study because the former is a benchmark solution in a way of decomposing high-dimensional data into a set of lowdimensional marginal distributions while the latter is an effective approach of random projection.

### 6.1.4 Parameter Settings

In our experiments, we use DP-Pub ${ }^{1}$ to denote the case with a trusted server and DP-Pub ${ }^{2}$ the one with a semihonest server. The privacy budget $\epsilon$ of DP-Pub ${ }^{1}$ is evenly distributed to the two phases, i.e., $\epsilon_{1}=\epsilon_{2}=\frac{1}{2} \epsilon$. For DPPub $^{2}$, there is no need to partition the privacy budget since the data is first locally differentially privatized, i.e., the privacy budget $\epsilon$ is completely allocated to the local privacy procedure. For the parameter $k$ used in the construction of the Bayesian network, we test $k=1,2,3$. Since the time cost for larger $k$ values is typically higher, we do not try the cases of $k>3$. Based on our experiments, we observe that the influence of $k$ on the experimental results is not obvious. The reason possibly lies in that the structure of the Markov blanket can help to accurately learn the data correlations between different attributes. In the following section, we present the experimental results of $k=2$.

### 6.2 Experimental Results

In this subsection, we carry out 50 independent runs for each of the experiments mentioned above and report the averaged results for statistical confidence.

### 6.2.1 Results on Average Variation Distance

For the task of examining the accuracy of $\alpha$-way marginals, we compute all the $\alpha$-dimensional attribute unions and compare the averaged variation distance of PrivBayes, DPPro, DP-Pub ${ }^{1}$ and DP-Pub ${ }^{2}$, with a varying privacy budget $\epsilon$ from 0.2 to 1.6 .

Figure 5 shows the average results of the variation distance of each approach on the four datasets. From Figure 5, one can see that the average variation distances of these three approaches decrease when $\epsilon$ increases over the four datasets. It is obvious that when $\epsilon$ is larger, smaller noise is required, and the data utility is higher. One can also observe that our approach clearly outperforms PrivBayes and DPPro
![img-4.jpeg](img-4.jpeg)

Fig. 5. Results of $\alpha$-way marginals with different $\epsilon$.
in all cases for ACS and NLTCS, while for BR2000 and Adult, the relative superiority is more pronounced when $\epsilon$ is small. There are several reasons that DP2-Pub outperforms PrivBayes and DPPro. First, PrivBayes constructs a Bayesian network to model the data correlation and generates a set of noisy conditional distributions of the original dataset. That is, for each attribute-parent pair in the Bayesian network, PrivBayes generates differentially private conditional distributions by adding Laplace noise which makes the data utility of the dataset drastically decrease. In our approach, we only utilize the Bayesian network to learn the correlations between different attributes and adopt our proposed invariant post randomization to achieve data perturbation, which ensures that there is almost no loss of statistical information. The probability distribution of each attribute variation is basically unchanged after the double-perturbation. Second, the random projection method DPPro does not consider the data characteristics and only preserves the pairwise $L_{2}$ distance when generating the random projection matrix, thus it may lead to relatively low utility especially when there exist data correlations between different attributes. In our approach DP2-Pub, we learn the data correlations of the original dataset and consider the importance of different attributes when allocating the privacy budget.

DP-Pub ${ }^{2}$ performs better than DP-Pub ${ }^{1}$ according to the results shown in Figure 5. This is counter-intuitive as centralized differential privacy usually performs better than

local differential privacy because centralized differential privacy adds noise based on the sensitivity of a particular query function while in local differential privacy noise is added via post randomization. But in DP-Pub ${ }^{1}$, noise is added for differentially private Bayesian network construction and for post randomization, with none of them considering the sensitivity of a particular query function, which is more general at the cost of lower utility. Moreover, at the same budget level, adding noise at two phases increases the total amount of noise as the added noise amount is not linearly proportional to the privacy budget - it is superlinear, which also contributes to the lower utility of DPPub $^{1}$.

### 6.2.2 Results on SVM classification

![img-5.jpeg](img-5.jpeg)

Fig. 6. Results of SVM with different $\epsilon$
For the second task, we evaluate the performance of PrivBayes, DPPro, DP2-Pub ${ }^{1}$,DP-Pub ${ }^{2}$, and Non-Private (no DP is considered) for SVM classification. Figure 6 shows the misclassification rate of each approach under various
different privacy budgets. One can see that the error of Non-Private remains unchanged for all $\epsilon$ since it does not consider differential privacy. One can also see that both DPPub $^{1}$ and DP-Pub ${ }^{2}$ outperform PrivBayes and DPPro on almost all datasets. The reason for the higher classification accuracy of our approach lies in that it can achieve higher data utility with a better retention of correlations among attribute variables and a higher accuracy of joint distributions. More specifically, both DP-Pub ${ }^{1}$ and DP-Pub ${ }^{2}$ retain the data characteristics while satisfying privacy guarantee, thus can help to obtain good results of SVM classifications. Moreover, the misclassification rate decreases faster when $\epsilon$ increases from 0.2 to 0.6 , and the decrease of the misclassification rate is not obvious when $\epsilon$ is larger than 0.8 . This indicates that a higher privacy level with a small $\epsilon$ leads to a lower data utility.

## 7 CONCLUSIONS AND FUTURE RESEARCH

In this paper, we propose a differentially private data publication mechanism DP2-Pub consisting of two phases, attribute clustering and data randomization. Specifically, in the first phase, we present the procedure of attribute clustering using the Markov blanket model based on the differentially private Bayesian network to achieve attribute clustering and obtain a reasonable allocation of privacy budget. In the second phase, we design an invariant post randomization method by conducting a double-perturbation while satisfying local differential privacy. Our privacy analysis shows that DP2-Pub satisfies differential privacy. We also extend our mechanism making it suitable for the scenario with a semi-honest server in a local-differential privacy manner. Comprehensive experiments on four real-world datasets demonstrate that DP2-Pub outperforms existing methods and improves data utility with strong privacy guarantee.

In our future research, we intend to combine other effective dimensionality reduction techniques[36,37] with differential privacy to investigate their impact on the data utility of published data. Particularly, we intend to combine DP with manifold learning [36], which is a popular approach for non-linear dimensionality reduction that maps a high dimensional data space into a low-dimensional manifold representation of the data while preserving a certain form of geometric relationships between the data points.

## ACKNOWLEDGMENT

This work was partially supported by the US National Science Foundation under grant CNS-1704397.
