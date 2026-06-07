# Causal Discovery Using Weight-Based Conditional Independence Test 

ZHAOLONG LING, BO LI, YIWEN ZHANG, and PENG ZHOU, Anhui University, Hefei, China<br>XINGYU WU, The Hong Kong Polytechnic University, Hong Kong SAR, China<br>YUEE HUANG, Wannan Medical College, Wuhu, China<br>KUI YU and XINDONG WU, Hefei University of Technology, Hefei, China

Conditional Independence (CI) tests play an essential role in causal discovery from observational data, enabling the measurement of independence between two nodes. However, traditional CI tests ignore the imbalanced occurrence probabilities of node values, which may affect the accuracy of determining independence between nodes. To address this problem, we first introduce a new concept of the Node-imbalance phenomenon to describe the imbalance of node values in the Bayesian network data and analyze the influence of the Node-imbalance phenomenon on the traditional CI tests, then we propose a Weight-Based Conditional Independence (WCI) test to improve the accuracy of CI tests in the presence of Node-imbalance. In the experiments, we verify that WCI effectively measures the dependency between nodes in the Node-imbalance phenomenon compared with the traditional independence tests, and the state-of-the-art causal discovery algorithms reduce the number of false causal orientations through WCI.

CCS Concepts: $\cdot$ Computing methodologies $\rightarrow$ Causal reasoning and diagnostics;
Additional Key Words and Phrases: Causal discovery, Conditional independence test, Bayesian network
Associate Editor: Danai Koutra

## ACM Reference format:

Zhaolong Ling, Bo Li, Yiwen Zhang, Peng Zhou, Xingyu Wu, Yuee Huang, Kui Yu, and Xindong Wu. 2024. Causal Discovery Using Weight-Based Conditional Independence Test. ACM Trans. Knowl. Discov. Data. 19, 1, Article 9 (November 2024), 24 pages.
https://doi.org/10.1145/3687467

[^0]
[^0]:    This work was supported by the National Key Research and Development Program of China (under Grant 2020AAA0106100), the National Natural Science Foundation of China (under Grant 62306002, 62176001, 62376087, and 62120106008), and the Natural Science Project of Anhui Provincial Education Department (under Grant 2023AH030004).
    Authors' Contact Information: Zhaolong Ling, Anhui University, Hefei, China; e-mail: zlling@ahu.edu.cn; Bo Li, Anhui University, Hefei, China; e-mail: ahulibo@163.com; Yiwen Zhang (corresponding author), Anhui University, Hefei, China; e-mail: zhangyiwen@ahu.edu.cn; Peng Zhou, Anhui University, Hefei, China; e-mail: doodzhou@ahu.edu.cn; Xingyu Wu, Department of Computing, The Hong Kong Polytechnic University, Hong Kong SAR, China; e-mail: xingy.wu@polyu.edu.hk; Yuee Huang, School of Public Health, Wannan Medical College, Wuhu, China; e-mail: huangyeWindow@163.com; Kui Yu, Key Laboratory of Knowledge Engineering with Big Data (the Ministry of Education of China), the School of Computer Science and Information Technology, Hefei University of Technology, Hefei, China; e-mail: yukui@hfut.edu.cn; Xindong Wu, Key Laboratory of Knowledge Engineering with Big Data (the Ministry of Education of China), the School of Computer Science and Information Technology, Hefei University of Technology, Hefei, China; e-mail: xwu@hfut.edu.cn.
    Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org.
    (c) 2024 Copyright held by the owner/author(s). Publication rights licensed to ACM.

    ACM 1556-472X/2024/11-ART9
    https://doi.org/10.1145/3687467

# 1 Introduction 

Conditional Independence (CI) testing is an important tool in causal discovery based on graphical models [23, 38]. For two random nodes $X, Y$, and a set $\mathbf{Z}$, CI between $X$ and $Y$ given the set $\mathbf{Z}$ (i.e., $X \Perp Y \mid \mathbf{Z}$ ) means that given values of $\mathbf{Z}$, and values of $X$ (or $Y$ ) do not provide any additional information about $Y$ (or $X$ ) [14, 39]. Thus, if the true probability distribution of the observed data is faithful to the underlying causal graph, the CI test recovers the causal network by determining a set of Markov equivalence classes through the d-separation theorem [2, 6, 20, 27].

Traditional CI tests utilize the $G^{2}$ test and mutual information test to determine the Markov equivalence classes with discrete data for causal discovery [10, 34]. The $G^{2}$ test employs the loglikelihood ratio method to calculate the test statistic. $G^{2}$ test statistics are additive, which means they can be used for more elaborate statistical designs [21]. The mutual information test calculates the mutual information between variables based on their conditional probability distribution [16]. If the mutual information between two variables exceeds a certain threshold, it indicates that the variables are considered dependent, otherwise independent [35]. Goebel et al. have shown that the empirical mutual information follows a gamma distribution, which allows them to define a threshold based on the domain size of variables and the sample size of data [11].

However, these CI tests ignore the phenomenon of significant differences in sample numbers between different state values due to the imbalanced probability distribution of node state values, which may significantly weaken the test statistics corresponding to small data samples, and then affect the accuracy of independence tests. That is, initially independent nodes may appear to be dependent, leading to existing causal discovery algorithms based on independence tests to obtain false causal skeleton and false causal orientations (see Section 4 for details). Furthermore, imbalanced probability distributions of node state values are ubiquitous in real-world scenarios due to various factors. For example, as shown in the Lung Cancer ${ }^{1}$ [17] Bayesian Network (BN) dataset in Figure 1, the number of people without disease is much higher (over nine times) than the number of people with the disease, regardless of whether the disease is tuberculosis or lung cancer.

The amount of information measures the predictive information that can be provided in a prediction task for another variable [9]. As the probability of an event occurring decreases, the information quantity associated with it increases, and vice versa [9]. Since the amount of information is related to the likelihood of event occurrence, for nodes in BN with imbalanced probability distribution like lung cancer, small samples of data suffering from lung cancer have more information quantity. In other words, the amount of information on samples suffering from lung cancer is inversely proportional to the number of its samples. This property of the amount of information exactly satisfies the requirement that the sample size of node values should be inversely proportional to their weights [36]. Consequently, the influence of the Node-imbalance phenomenon can be mitigated using the amount of information contained in the nodes.

In this article, we focus on the influence on traditional CI tests when the occurrence probability of node values in a BN is imbalanced, and use the difference in the amount of information of nodes to deal with the influence. The main contributions of this article are summarized as follows:

- We propose a new concept, called the Node-imbalance phenomenon, to describe the imbalance of values taken by nodes in BN data, and then analyze the influence of the Node-imbalance phenomenon on traditional CI tests.
- We propose the Weight-Based Conditional Independence (WCI) test through theoretical analysis. WCI adjusts the weight of its test statistic according to the amount of information on nodes to mitigate the influence of the Node-imbalance phenomenon.

[^0]
[^0]:    ${ }^{1}$ The dataset is publicly available at https://www.bnlearn.com/bnrepository/discrete-small.html\#asia

![img-0.jpeg](img-0.jpeg)

Fig. 1. Lung Cancer BN and conditional probability assessed by the expert for some of its nodes. BN, Bayesian network.
-We compare WCI with two CI tests to verify that the WCI has higher accuracy and efficiency in handling imbalanced data, and enables eight state-of-the-art causal discovery algorithms to construct more accurate causal network structures.

The remainder of the article is structured as follows. Section 2 provides a review of related work. Section 3 introduces basic definitions and notation. In Section 4, the article analyzes the influence of the Node-imbalance phenomenon on traditional CI tests and proposes a solution. The WCI algorithm is described in detail in Section 5. Section 6 presents the experimental results and analysis. Finally, Section 7 concludes the article and discusses potential directions for future research.

# 2 Related Work 

Causal discovery algorithms based on independence tests can generally be categorized into three main types [30]: global causal structure learning [7], local causal structure learning [33], and Partial Causal Structure Learning (PSL) [18]. These algorithms utilize CI tests to eliminate and orientate causal directions [40].

For global causal discovery, constraint-based methods employ independence tests to construct causal networks, while hybrid methods utilize independence tests to construct causal skeletons, thereby reducing the search space [10, 15]. One of the most classical constraint-like algorithms is the Parents and Children (PC) algorithm [27] proposed by Spirtes et al. It starts with a complete undirected graph and iteratively removes edges based on CI tests. The PC algorithm employs the CI tests and Meek-rule [22] to orientate edge directions in directed acyclic graphs. When the DAG is sparse, the PC algorithm can reduce the required computation and use the $G^{2}$ test or mutual information test without specific CI tests [5]. Colombo and Maathuis [3] address the issue of erroneous CI tests due to limited sample sizes, particularly in relation to the order of CI tests execution. They demonstrate that the output of all three phases in the original PC algorithm is sensitive to the order of CI tests. Thus, PC-stable avoids the order dependence problem by preserving the conditioning set in the CI tests. The accuracy of learning high-dimensional graph structures is improved. Yehezkel and Lerner [32] focus on reducing the number of CI tests, specifically higherorder tests that are costly and unreliable. Their Recursive Autonomy Identification (RAI) algorithm assumes discrete variables and variable faithfulness. Similar to the PC algorithm, RAI employs incremental order CI tests. However, edge orientation is performed after each round

of edge removal at different conditioning set sizes, enabling RAI to identify autonomous subgraphs. RAI achieves higher accuracy and efficiency compared to the PC algorithm. The Max-Min Hill-Climbing (MMHC) [29] algorithm proposed by Tsamardinos et al. is a hybrid structure learning method. In the constraint phase, MMHC uses CI tests to determine the PC set of each node, constraining the search space and establishing a causal skeleton. In the score-based search phase, MMHC uses a hill-climbing algorithm to find the network with the highest score. More recently, Guo et al. [13] address the symmetry constraint problem caused by independence tests and propose the Adaptive DAG Learning (ADL) algorithm. ADL differs from the MMHC algorithm in that it adaptively uses AND-rule and OR-rule to construct an exact global causal skeleton structure, providing a more reliable network space for the search scoring phase. In addition, many CI-based global causal discovery algorithms have been proposed to bring the causal discovery problem closer to real-world scenarios [12, 37]. For example, the Cyclic Causal Discovery algorithm relaxes the assumption of acyclicity [26], and the Fast Causal Inference algorithm relaxes both the assumption of no latent confounding and no selection bias [4].

Local causal structure learning algorithms and PSL algorithms are mainly constraint-based approaches [1]. The existing local causal structure learning algorithms recursively identify collider nodes and edge orientations by obtaining Markov blankets of variables through $G^{2}$ test or mutual information as CI tests [34]. The Causal Markov Blanket (CMB) [8] algorithm proposed by Gao et al. first learns the MB of the target variable and orientates the edges by tracking the CI changes in the MB of the target variable until the PCs of the target variable are identified, or they cannot be further identified by continuing the process [33]. The Efficient Local Causal Structure (ELCS) [31] algorithm aims to identify the N-structure of the target node by using independence tests to reduce the construction of the local skeleton and improve efficiency. Additionally, the PSL [18] algorithm is proposed, which uses CI tests to recursively identify all V-structures in Markov blankets and learn local causal structures of any depth.

In summary, independence tests are crucial tools in causal learning. Minimizing the cascading impact of independence tests is a key consideration in the design of constraint- and hybrid-based algorithms [15]. Thus, we aim to improve the accuracy of CI tests and, consequently, enhance the accuracy of causal discovery.

# 3 Notations and Definitions 

In the following, the relevant definitions and theorems are introduced. Table 1 provides a summary of the notations used in this article.

Definition 1 (V-Structure) [25]. The triplet of variables $T, X, Y$ forms a V-structure (i.e., $T \rightarrow$ $X \leftarrow Y$ ) if node $X$ has two incoming edges from $T$ and $Y$, respectively, and $T$ is not adjacent to $Y$.

There are four cases of the path $T-X-Y$ : (a) $T \rightarrow X \leftarrow Y$, (b) $T \rightarrow X \rightarrow Y$, (c) $T \leftarrow X \rightarrow Y$, (d) $T \leftarrow X \leftarrow Y$. In the V-structure of case (a), $X$ is a collider because $X$ has two incoming edges from $T$ and $Y$ in this path, while in the other three cases, $X$ is a non-collider.

Definition 2 (D-Separation) [25]. Given $\mathbf{Z} \subseteq \mathbf{U} \backslash\{X \cup Y\}$, the path $\pi$ between $X$ and $Y$ is open if and only if either colliders or their descendants on $\pi$ are included in $\mathbf{Z}$, and every non-collider on $\pi$ is not included in $\mathbf{Z}$, otherwise, the path $\pi$ is blocked. If each path from $X$ to $Y$ is blocked by $\mathbf{Z}$, then $\mathbf{Z}$ is called d-separating $X$ and $Y$, denoting as $d-\operatorname{sep}(X, Y \mid \mathbf{Z})$.

Definition 3 (Faithfulness) [27]. Given a BN $<\mathbf{U}, \mathbf{G}, \mathbf{P}>, \mathbf{P}$ is faithful to $\mathbf{G}$ when for any $X, Y \in \mathbf{U}$ and $\mathbf{Z} \in \mathbf{U} \backslash\{X, Y\}, X \Perp Y \mid \mathbf{Z}$ in $\mathbf{P}$ if $d-\operatorname{sep}(X, Y \mid \mathbf{Z})$ in $\mathbf{G}$.

Definition 2 shows that CI and d-separation are equivalent if the dataset and its underlying BN are faithful to each other.

Table 1. Summary of Notations


Theorem 1 [27]. In a $B N<\mathbf{U}, \mathbf{G}, \mathbf{P}>$, for $X, Y \in \mathbf{U}$, there is an edge between $X$ and $Y$ if $X \Perp Y \mid \mathbf{Z}$ for $\forall \mathbf{Z} \in \mathbf{U} \backslash\{X, Y\}$.

Theorem 1 illustrates that if $X$ is the causal node of $Y, X$ and $Y$ are conditionally dependent for $\forall \mathbf{Z} \in \mathbf{U} \backslash\{X, Y\}$. Thus, we can recover the causal network structure by performing CI tests.

Theorem 2 [27]. In a faithful BN, for three variables $X, Y, T \in \mathbf{U}$ and variable set $\mathbf{Z} \in \mathbf{U} d$-separates variable $X$ and $Y$. If $X \Perp Y \mid \mathbf{Z} \cup T$, then there is a $V$-structure $X \rightarrow T \leftarrow Y$.

Theorem 2 shows that the chain $A \rightarrow T \leftarrow B$ is different from $A \rightarrow T \rightarrow B$ and $A \leftarrow T \rightarrow B$ with respect to the requirement of whether $T$ is in the set $\mathbf{Z}$. Thus, we can identify the $V$-structure to discover the causal orientations through independence tests.

The $G^{2}$ test is an extension of $\mathcal{X}^{2}$ test [24]. Given nodes $X, Y$ and conditioning set $\mathbf{Z}$, the formula for $G^{2}$ test is as follows:

$$
G^{2}(X ; Y \mid \mathbf{Z})=2 \sum_{x y z} s_{X Y Z}^{x y z} \ln \left(\frac{s_{X Y Z}^{x y z} s_{X}^{x}}{S_{X Z}^{x z} s_{Y Z}^{y z}}\right)
$$

Theorem 3 [24]. The Chi-square statistic $\mathcal{X}^{2}$ test is an approximation of the log-likelihood statistic $G^{2}$ test.

Theorem 3 shows that the $G^{2}$ test statistic is approximated by the $\mathcal{X}^{2}$ test statistic, when the expected value is close to the observed value. However, the more significant the difference between the expected and observed values, the higher the value of the $G^{2}$ test statistic is above the $\mathcal{X}^{2}$ test statistic. In addition, $G^{2}$ test is a sub-class of likelihood ratio tests, and its statistics are additive, which means they can be used for more elaborate statistical designs [21].

Mutual information is another form of the $G^{2}$ test; its essence is the same [35]. The mutual information calculation formula of $X$ and $Y$ under the conditioning set $\mathbf{Z}$ is as follows:

$$
M I(X ; Y \mid \mathbf{Z})=\sum_{x y z} p(x, y \mid \mathbf{z}) \ln \left(\frac{p(x, y \mid \mathbf{z})}{p(x \mid \mathbf{z}) p(y \mid \mathbf{z})}\right)
$$

Theorem 4 [35]. The $G^{2}$ test statistic is the expansion of the ratio of mutual information, and the size of this ratio is the sample size $M$.

![img-1.jpeg](img-1.jpeg)
(a) Barley Bayesian network and its sub-network


(b) Data for node exptgens with $\mathbf{1 0 0 0}$ samples


(c) Data for nodes "exptgens" and "nedbarea" with 1000 samples

Fig. 2. Barley BN and experimental data for some of its nodes. (a) Barley BN and its sub-network. (b) Statistical results of the experimental data for "exptgens" (black node in (a)). (c) Statistical results of the experimental data for "exptgens" (black node in (a)) and "nedbarea" (blue node in (a)).

Theorem 4 establishes that the $G^{2}$ test is essentially a representation of the mutual information between variables, i.e., $G^{2}(X ; Y \mid \mathbf{Z})=2 M \cdot M I(X ; Y \mid \mathbf{Z})$, where $M$ represents the data sample size. Thus, in the following, when illustrating that the Node-imbalance phenomenon results in false dependencies between variables, this article employs the $G^{2}$ test as an illustrative and verification example.

# 4 Problem Analysis and Resolution 

In this section, we first describe the Node-imbalance phenomenon, then analyze the impact of the Node-imbalance phenomenon on independence testing and causal discovery, and finally propose a method based on the amount of information weight to mitigate the effect of the Node-imbalance phenomenon.

### 4.1 Node-Imbalance Phenomenon

By running the CI test, $G^{2}$ test, on benchmark BN datasets, we find that it cannot correctly measure the dependency between two nodes in some cases, and then we find that data samples that do not get correct results are imbalanced. To demonstrate this phenomenon, we analyze the composition of node values using the Barley ${ }^{2}$ BN dataset with 1,000 samples as an example. The experimental data obtained from the statistics in Figure 2(b) show that the number of node "exptgens" with the value of "x40_50" is almost 25 times higher than that of "x60_70," which leads to a significant weakening of the data corresponding to "x60_70" in the calculation. We also find the similar phenomenon with other benchmark BN datasets. Thus, if this problem is ignored, it may reduce the accuracy of traditional CI tests and further affect the accuracy of the causal discovery algorithms using CI tests.

To demonstrate the impact of the imbalanced probability distribution of node state values on $G^{2}$ test, we use "exptgens" = "x40_50" (520 samples) and "exptgens" = "x60_70" (25 samples) with significant sample size differences for analyzing. We first give the following symbol definitions

[^0]
[^0]:    ${ }^{2}$ The dataset is publicly available at https://www.bnlearn.com/bnrepository/discrete-medium.html\#barley

to show the formula more concisely: " $E$ " denotes the node "exptgens," " $N$ " represents the node "nedbarea." " $e_{3}$," " $e_{4}$," " $e_{5}$," " $e_{6}$," and " $e_{7}$ " denote that node "exptgens" takes values "x_30," "x30_40," "x40_50," "x50_60," and "x60_70," respectively. " $n_{1}$," " $n_{2}$," and " $n_{3}$ " represent that node "nedbarea" takes values "x1," "x2," and "x3," respectively.

The $\mathcal{X}^{2}$ test statistics for nodes "exptgens" and "nedbarea" in the data with Figure 2(b) and (c) are calculated as follows:

$$
\mathcal{X}^{2}(\text { exptgens; nedbarea })=\sum_{i=3}^{7} \sum_{j=1}^{3} \frac{\left(S_{E N}^{e_{i} n_{j}}-E\left(S_{E}^{e_{i}}, S_{N}^{n_{j}}\right)\right)^{2}}{E\left(S_{E}^{e_{i}}, S_{N}^{n_{j}}\right)}=18.51
$$

The $G^{2}$ test statistics for nodes "exptgens" and "nedbarea" in the data with Figure 2(b) and (c) are calculated as follows:

$$
G^{2}(\text { exptgens; nedbarea })=2 \sum_{i=3}^{7} \sum_{j=1}^{3} S_{E N}^{e_{i} n_{j}} \cdot \ln \frac{S_{E N}^{e_{i} n_{j}}}{E\left(S_{E}^{e_{i}}, S_{N}^{n_{j}}\right)}=21.73
$$

The degrees of freedom for both test statistics are $d f=\left(c_{E}-1\right)\left(c_{N}-1\right)=8$. The p-value of the $\mathcal{X}^{2}$ test with reference to the $\mathcal{X}^{2}$ distribution table is 0.0177 , while the p -value of the $G^{2}$ test with reference to the $\mathcal{X}^{2}$ distribution table is 0.0054 . By comparing the p -value and significance level of 0.01 , the $G^{2}$ test finally rejected this null hypothesis and the $\mathcal{X}^{2}$ test accepted it. Since nodes "exptgens" and "nedbarea" are independent in the null set, the $\mathcal{X}^{2}$ test yields the correct test result for independence, while the $G^{2}$ test rejects the correct hypothesis and yields the incorrect result that indicates dependence. This discrepancy is caused by inconsistent size relationships between the $G^{2}$ test sub-items and the $\mathcal{X}^{2}$ test sub-items. Specifically, nodes "exptgens" and "nedbarea" are taken as " $N$ " = " $n_{1}$ " and " $E$ " = " $e_{5}$," " $N$ " = " $n_{1}$ " and " $E$ " = " $e_{7}$," the $\mathcal{X}^{2}$ test statistics for the two subsections are calculated as follows:

$$
\begin{aligned}
& \mathcal{X}^{2}\left(E=e_{7} ; N=n_{1}\right)=\frac{\left(S_{E N}^{e_{i} n_{1}}-\left(S_{E}^{e_{7}} \cdot S_{N}^{n_{1}} / M\right)\right)^{2}}{\left(S_{E}^{e_{7}} \cdot S_{N}^{n_{1}} / M\right)}=\frac{(10-8.425)^{2}}{8.425}=0.294 \\
& \mathcal{X}^{2}\left(E=e_{5} ; N=n_{1}\right)=\frac{\left(S_{E N}^{e_{i} n_{1}}-\left(S_{E}^{e_{5}} \cdot S_{N}^{n_{1}} / M\right)\right)^{2}}{\left(S_{E}^{e_{5}} \cdot S_{N}^{n_{1}} / M\right)}=\frac{(178-175.24)^{2}}{175.24}=0.043
\end{aligned}
$$

However, the $G^{2}$ test statistics for the nodes " $N$ " = " $n_{1}$ " and " $E$ " = " $e_{5}$," " $N$ " = " $n_{1}$ " and " $E$ " = " $e_{7}$ " sub-items are as follows:

$$
\begin{aligned}
& G^{2}\left(E=e_{7} ; N=n_{1}\right)=S_{E N}^{e_{i} n_{1}} \ln \frac{M \cdot S_{E N}^{e_{i} n_{1}}}{S_{E}^{e_{7}} \cdot S_{N}^{n_{1}}}=10 \cdot \ln \frac{1000 \cdot 10}{25 \cdot 337}=1.714 \\
& G^{2}\left(E=e_{5} ; N=n_{1}\right)=S_{E N}^{e_{i} n_{1}} \ln \frac{M \cdot S_{E N}^{e_{i} n_{1}}}{S_{E}^{e_{5}} \cdot S_{N}^{n_{1}}}=178 \cdot \ln \frac{1000 \cdot 178}{520 \cdot 337}=2.781
\end{aligned}
$$

Thus, the sub-item of $G^{2}$ test result, $G^{2}\left(E=e_{7} ; N=n_{1}\right)<G^{2}\left(E=e_{5} ; N=n_{1}\right)$, is the opposite of the result of $\mathcal{X}^{2}\left(E=e_{7} ; N=n_{1}\right)>\mathcal{X}^{2}\left(E=e_{5} ; N=n_{1}\right)$. Furthermore, if $\frac{S_{i}}{E_{i}}>\frac{S_{j}}{E_{j}}$ holds, the following conclusion to hold $\frac{S_{i}-E_{i}}{E_{i}}>\frac{S_{j}-E_{j}}{E_{j}}$. For $\mathcal{X}^{2}=\sum_{1}^{n} \frac{(S-E)^{2}}{E}$, the positive and negative of the numerator of this inequality only indicates the positive and negative correlation, not the magnitude of the correlation. So, squaring the numerator, the above inequality still holds. For the $G^{2}$ test, the logarithmic term in the formula for calculating its statistical value is $\ln \frac{S}{E}$, when $\frac{S_{i}}{E_{i}}>\frac{S_{j}}{E_{j}}$, the inequality $\ln \frac{S_{i}}{E_{i}}>\ln \frac{S_{j}}{E_{j}}$ holds, which is consistent with the size relationship among the sub-terms of the $\mathcal{X}^{2}$ test. In this example, the logarithmic terms of the two sub-items of the $G^{2}$ test are

$\ln \frac{S_{E N}^{e_{1} n_{1}}}{E_{E N}^{e_{2} n_{1}}}=0.171$ and $\ln \frac{S_{E N}^{e_{2} n_{1}}}{E_{E N}^{e_{3} n_{1}}}=0.016$, which are consistent with the size relationship between the sub-items of the $\mathcal{X}^{2}$ test. Thus, to ensure that the sub-item of the $G^{2}$ test result corresponds with the theoretical result, the following inequality needs to be satisfied:

$$
\frac{S_{E N}^{e_{1} n_{1}}}{S_{E N}^{e_{2} n_{1}}}<\frac{\ln \frac{M \cdot S_{E N}^{e_{2} n_{1}}}{S_{E}^{e_{2}} \cdot S_{N}^{e_{1}}}}{\ln \frac{M \cdot S_{E N}^{e_{2} n_{1}}}{S_{E}^{e_{2}} \cdot S_{N}^{e_{1}}}}=\frac{\ln \left(\frac{M}{S_{N}^{e_{1}}} \cdot p\left(n_{1} \mid e_{7}\right)\right)}{\ln \left(\frac{M}{S_{N}^{e_{1}}} \cdot p\left(n_{1} \mid e_{5}\right)\right)}=10.967
$$

However, due to the node "exptgens" existing in the imbalanced probability distribution of state values, $\left(p\left(e_{5}\right)=0.52>p\left(e_{7}\right)=0.025\right)$, resulting in $\frac{S_{E N}^{e_{5} n_{1}}}{S_{E N}^{e_{2} n_{1}}}=17.8>10.976$, not satisfying the above inequality in the observed data, which further leads to a significant difference in the numbers multiplied by each item when using $G^{2}$ test sub-items, and the results obtained by $G^{2}$ test sub-items differ from the results in $\mathcal{X}^{2}$ test. To illustrate this phenomenon more intuitively, we formulate it as: for a node $X$ in BN, $i \in 1,2, \ldots, n, s_{X}^{x_{i}}$ denotes the number of node $X$ taking value $x_{i}$, and $s_{X}^{x_{1}}<s_{X}^{x_{2}}<\ldots<s_{X}^{x_{n}}$. If $s_{X}^{x_{n}}>>s_{X}^{x_{1}}$, then there is the Node-imbalance phenomenon.

Since the $G^{2}$ test uses the $G^{2}$ test statistic and the degrees of freedom $d f$ to calculate the final p-value value concerning the $\mathcal{X}^{2}$ distribution table, if there is the Node-imbalance phenomenon, the huge difference in sample size between the sub-items leads to a significant difference in the size relationship between the $G^{2}$ test sub-items and the size relationship between the $\mathcal{X}^{2}$ test sub-items, which affects the overall $G^{2}$ test statistic obtained from the final sub-items accumulation, making the results of the $G^{2}$ test different from the results of the $\mathcal{X}^{2}$ test, which may result in an error in this CI test. Note that the $G^{2}$ test is a sub-class of likelihood ratio tests, a general category of tests that have many uses for testing the fit of data to mathematical models [21]. Moreover, most state-of-the-art causal discovery algorithms use the $G^{2}$ test as a statistical test for CI testing of discrete data, because the $G^{2}$ test statistics are additive, which means they can be used for more elaborate statistical designs [24]. Therefore, we hope to design a novel CI test based on the $G^{2}$ test to reduce the impact of the Node-imbalance phenomenon.

Owing to Definition 2, under the assumption of faithfulness, the empty set $\mathbf{Z}$ cannot d-separate nodes "exptgens" and "nedbarea." However, based on Definition 1, the paths $\pi$ between nodes "exptgens" and "nedbarea" are blocked by $\mathbf{Z}$, satisfying $d-\operatorname{sep}($ exptgens, nedbarea $\mid \mathbf{Z})$. Therefore, the Node-imbalance phenomenon leads to independent test results contradicting the actual d-separation results. There are two cases in which the d-separation and CI test results of two nodes contradict each other: (1) The CI results of two nodes are dependent, but the actual d-separation cases are separated. (2) The CI results of the two nodes are independent, but the actual d-separation cases are not separated.

According to Theorem 1, the first case results in nodes without a causal relationship entering the candidate PC set during the causal skeleton orientation stage. This, in turn, increases the size of the conditional set space during the removal of false-positive nodes, leading to a surplus of CI tests. This surplus may lead to an increase in false-positive nodes, resulting in a redundant causal skeleton. Consequently, the final causal network may contain numerous redundant and incorrect causal orientations. The second case directly leads to the omission of correct causal nodes, a critical issue resulting in a deficient causal skeleton. This, in turn, diminishes the number of correct causal orientations in the final causal network. According to Theorem 2, the first case prompts the identification of false V-structures during the skeleton orientation phase. This can lead to reversing causal direction when using Meek-rule oriented edges. Redundant false-positive nodes in the skeleton construction phase may lead to the identification of redundant V-structures, further contributing to the reversal of causal orientations. The second case results in the absence of correct

V-structures, directly impacting the recognition of causal orientations. The lack of causal nodes in the skeleton construction phase reduces the number of correctly recognized V-structures, resulting in an increased number of unrecognized causal orientations. For hybrid class algorithms, both the first and second cases introduce redundancy and absence in the subsequent network search space, influencing the final causal network structure determined by the search algorithm.

# 4.2 Analysis and Solution 

With the above analysis, the Node-imbalance phenomenon significantly affects the accuracy of traditional CI tests in measuring the dependence between two nodes, resulting in an increased number of false-positive nodes and false causal orientations in causal discovery. In the following, we propose Theorem 5 to deal with this problem.

Theorem 5. For a node $X$, assuming that the number of value $x_{n}$ in $X$ is much higher than $x_{1}$ (the Node-imbalance phenomenon exists), then the weight of $x_{1}$ needs to be set much higher than $x_{n}$.

Proof. $p\left(x_{1}\right)$ and $p\left(x_{n}\right)$ denote probabilities of $x_{1}$ and $x_{n}$ in the node $X$, respectively, and $w_{X}^{x_{1}}$ and $w_{X}^{x_{n}}$ denote weights that should be added to $x_{1}$ and $x_{n}$ in node $X$, respectively. Assuming that the number of value $x_{n}$ in the node $X$ is $k$ times that of $x_{1}$, i.e.,

$$
p\left(x_{n}\right)=k * p\left(x_{1}\right)
$$

The value of $k$ will be much higher than 1 due to the Node-imbalance phenomenon.
To avoid the influence of the Node-imbalance phenomenon, occurrence probabilities of $x_{1}$ and $x_{n}$ need to be almost the same:

$$
w_{X}^{x_{n}} * p\left(x_{n}\right)=w_{X}^{x_{1}} * p\left(x_{1}\right)
$$

Bringing Equation (4) into Equation (5), we can get

$$
w_{X}^{x_{1}}=k * w_{X}^{x_{n}}
$$

Thus, the $x_{1}$ weight needs to be higher than that of $x_{n}$ because $k$ is a large value.

Theorem 5 demonstrates that in a BN, when nodes $X$ and $Y$ exist the Node-imbalance phenomenon under the conditioning set $\mathbf{Z}$, it is necessary to increase the weight of low-frequency state values and decrease the weight of high-frequency state values to mitigate the effect of the imbalance phenomenon. The amount of information is inherently linked to an event's probability. More precisely, the amount of information associated with an event is inversely proportional to the likelihood of its occurrence. This characteristic of information quantity exactly fulfills the requirement mentioned above.

In a BN, let the nodes $X$ take $x_{i}, Y$ take $y_{j}$, and the conditioning set $\mathbf{Z}$ take $\mathbf{z}$, then the amount of information for this state value is calculated as follows:

$$
\begin{aligned}
H\left(X=x_{i} ; Y=y_{j} \mid \mathbf{Z}=\mathbf{z}\right) & =\ln \frac{1}{p\left(X=x_{i}, Y=y_{j} \mid \mathbf{Z}=\mathbf{z}\right)} \\
& =-\ln \frac{s_{X Y Z}^{x_{i} y_{j} \mathbf{z}}}{S_{\mathbf{Z}}^{\mathbf{z}}}
\end{aligned}
$$

Further, the amount of information for each state value and the mean value of the amount of information for all state values can be found, and finally, the adjustment factor $w_{i j}$ of $S_{X Y Z}^{x_{i} y_{j} \mathbf{z}}$ is

obtained as follows:

$$
\begin{aligned}
w_{i j}= & \frac{-\ln p\left(x_{i}, y_{j} \mid \mathbf{z}\right)-E\left(\sum_{i j}^{n}-\ln p\left(x_{i}, y_{j} \mid \mathbf{z}\right)\right)}{E\left(\sum_{i j}^{n}-\ln p\left(x_{i}, y_{j} \mid \mathbf{z}\right)\right)} \\
= & \frac{-\ln \frac{S_{X Y Z}^{x_{i} y_{j} z}}{S_{Z}^{z}}-E\left(\sum_{i j}^{n}-\ln \left(\frac{S_{X Y Z}^{x_{i} y_{j} z}}{S_{Z}^{z}}\right)\right)}{E\left(\sum_{i j}^{n}-\ln \left(\frac{S_{X Y Z}^{x_{i} y_{j} z}}{S_{Z}^{z}}\right)\right)}
\end{aligned}
$$

where $E\left(\sum_{i j}^{n}-\ln \left(\frac{S_{X Y Z}^{x_{i} y_{j} z}}{S_{Z}^{z}}\right)\right)$ denotes the mean value of the amount of information for all state values of $X$ and $Y$ under the conditioning set $\mathbf{Z}$. The $n$ is the state values of $X$ and $Y$ under the conditioning set $\mathbf{Z}$, for which the sample size is not 0 . Similarly, when the conditioning set $\mathbf{Z}$ is empty, $X$ takes $x_{i}$, and $Y$ takes $y_{j}$, the corresponding adjustment factor as follows:

$$
\begin{aligned}
w_{i j}= & \frac{-\ln p\left(x_{i}, y_{j}\right)-E\left(\sum_{i j}^{n}-\ln p\left(x_{i}, y_{j}\right)\right)}{E\left(\sum_{i j}^{n}-\ln p\left(x_{i}, y_{j}\right)\right)} \\
= & \frac{-\ln \frac{S_{X Y}^{x_{i} y_{j}}}{M}-E\left(\sum_{i j}^{n}-\ln \left(\frac{S_{X Y}^{x_{i} y_{j}}}{M}\right)\right)}{E\left(\sum_{i j}^{n}-\ln \left(\frac{S_{X Y}^{x_{i} y_{j}}}{M}\right)\right)}
\end{aligned}
$$

To provide a more intuitive illustration of Theorem 5, we will continue using the example depicted in Figure 2. Applying Equation (9), each $S_{X Y}^{x_{i} y_{j}}$ item increases or decreases in weight as $0.402,0.614$, $0.402,-0.153,-0.105,-0.121,-0.474,-0.479,-0.443,-0.226,-0.238,-0.330,0.470,0.682,0.000$. After weighting based on the amount of information, there is $G_{w}^{2}\left(E=e_{7} ; N=n_{1}\right)>G_{w}^{2}\left(E=e_{5} ; N=n_{1}\right)$, which is consistent with the $\mathcal{X}^{2}\left(E=e_{7} ; N=n_{1}\right)>\mathcal{X}^{2}\left(E=e_{5} ; N=n_{1}\right)$. Recalculating the test statistics for the nodes "exptgens" and "nedbarea" is

$$
\begin{aligned}
& G_{w}^{2}(\text { exptgens; nedbarea }) \\
& =2 \sum_{i=3}^{7} \sum_{j=1}^{3} w_{i j} \cdot S_{E N}^{e_{i} n_{j}} \cdot \ln \frac{M \cdot S_{E N}^{e_{i} n_{j}}}{S_{E}^{e_{i}} \cdot S_{N}^{n_{j}}}=18.767
\end{aligned}
$$

With $G_{w}^{2}($ exptgens; nedbarea $)=18.767, d f=8$, and referencing the $\mathcal{X}^{2}$ distribution table, the calculated p-value is determined to be 0.0162 . Therefore, when the significance level was set at 0.01 , the results of the CI test for "exptgens" and "nedbarea" were consistent with the results of the d-separation theory. Therefore, through Theorem 5, existing causal discovery algorithms based on constraint methods can improve the accuracy of causal skeletons, reduce the number of redundant edges in causal networks, and reduce the number of unnecessary CI tests. In the skeleton orientation phase, more correct V-structures can be recognized, and the number of reversed edges in the causal network can be reduced. The causal discovery algorithm based on hybrid methods can then obtain a more accurate causal skeleton space through Theorem 5, and the subsequent search algorithm can converge to a more accurate causal network structure through a more accurate network space.

# Algorithm 1: WCI Test Algorithm 

Input: $X, Y$ : node; $\mathbf{Z}$ : conditioning set; $\operatorname{Cat}(X)$ : the number of categories in $X$
Output: $\rho$-value: significance level
if isempty(Z) then
Initialize the $S_{X}^{x_{i}}, S_{Y}^{y_{j}}, S_{X Y}^{x_{i} y_{j}}$;
$E\left(S_{X}^{x_{i}}, S_{Y}^{y_{j}}\right)=\frac{S_{X}^{x_{i}} S_{Y}^{y_{j}}}{M}$;
$G_{i j-}^{2}$ terms $=2 \cdot S_{X Y}^{x_{i} y_{j}} \ln \left(\frac{S_{X Y}^{x_{i} y_{j}}}{E\left(S_{X}^{x_{i}}, S_{Y}^{y_{j}}\right)}\right)$;
Reducing small sample noise using the Yates continuity correction values;
$W C I(X ; Y)=\sum_{i j}^{n} \frac{-\ln \frac{S_{X Y}^{x_{i} y_{j}}}{S_{Y}^{y_{j}}}}{E\left(\sum_{i j}^{n}-\ln \left(\frac{S_{X Y}^{x_{i} y_{j}}}{M}\right)\right)} \cdot G_{i j_{-}}$terms;
$d f=(\operatorname{Cat}(X)-1)(\operatorname{Cat}(Y)-1)$
else if $X$ and $Y$ conditioning on $\mathbf{Z}$ then
Initialize the $S_{\mathbf{Z}}^{x}, S_{X \mathbf{Z}}^{x_{i} \mathbf{z}}, S_{Y \mathbf{Z}}^{y_{j} \mathbf{z}}, S_{X Y \mathbf{Z}}^{x_{i} y_{j} \mathbf{z}}$;
$E\left(S_{X \mathbf{Z}}^{x_{i} \mathbf{z}}, S_{Y \mathbf{Z}}^{y_{j} \mathbf{z}}\right)=\frac{S_{X \mathbf{Z}}^{x_{i} \mathbf{z}} S_{Y \mathbf{Z}}^{y_{j} \mathbf{z}}}{S_{\mathbf{Z}}^{x}}$;
$G_{i j-}^{2}$ terms $=2 \cdot S_{X Y \mathbf{Z}}^{x_{i} y_{j} \mathbf{z}} \ln \left(\frac{S_{X Y \mathbf{Z}}^{x_{i} y_{j} \mathbf{z}}}{E\left(S_{X \mathbf{Z}}^{x_{i} \mathbf{z}}, S_{Y \mathbf{Z}}^{y_{j} \mathbf{z}}\right)}\right)$;
Reducing small sample noise using the Yates continuity correction values;
$W C I(X ; Y \mid \mathbf{Z})=\sum_{i j}^{n} \frac{-\ln \frac{S_{X Y \mathbf{Z}}^{x_{i} y_{j}}}{S_{\mathbf{Z}}^{x}}}{E\left(\sum_{i j}^{n}-\ln \left(\frac{S_{X Y \mathbf{Z}}^{x_{i} y_{j}}}{S_{\mathbf{Z}}^{x}}\right)\right)} \cdot G_{i j_{-}}$terms;
$d f=(\operatorname{Cat}(X)-1)(\operatorname{Cat}(Y)-1) \prod_{Z \in \mathbf{Z}} \operatorname{Cat}(Z)$;
end if
$\rho$-value $\leftarrow \operatorname{chi} 2 \operatorname{cdf}(W C I, d f)$;
return $\rho$-value;

## 5 WCI Test

Based on the analysis conducted in the previous section, we have observed that adjusting the weight of test statistics between nodes, considering the amount of information, can mitigate the impact of the Node-imbalance phenomenon. Motivated by this insight, we introduce a weighting strategy to the $G^{2}$ test, proposing a novel approach called WCI test. The algorithm encompasses both unconditional independence testing and CI testing, as depicted in Algorithm 1. In the following, we will provide a step-by-step explanation of the WCI algorithm, accompanied by theoretical analysis to support its effectiveness.

Unconditional Independence Testing (Lines 2-7). We first describe the unconditional independence test. When the condition set is empty, the adjustment factor $w$ of the amount of information between two nodes is Equation (9), then the WCI between $X$ and $Y$ is as follows:

$$
\begin{aligned}
W C I(X ; Y) & =2 \sum_{i j}^{n}\left(1+w_{i j}\right) S_{X Y}^{x_{i} y_{j}} \ln \left(\frac{S_{X Y}^{x_{i} y_{j}}}{E\left(S_{X}^{x_{i}}, S_{Y}^{y_{j}}\right)}\right) \\
& =2 \sum_{i j}^{n} \frac{-\ln \frac{S_{X Y}^{x_{i} y_{j}}}{M}}{E\left(\sum_{i j}^{n}-\ln \left(\frac{S_{X Y}^{x_{i} y_{j}}}{M}\right)\right)} S_{X Y}^{x_{i} y_{j}} \ln \left(\frac{M \cdot S_{X Y}^{x_{i} y_{j}}}{S_{X}^{x_{i}} \cdot S_{Y}^{y_{j}}}\right)
\end{aligned}
$$

In the case where the conditioning set $\mathbf{Z}$ is empty, the WCI algorithm first counts the number of samples for each combination of state values for $X, Y, X$ and $Y$ (denoted as $S_{X Y}^{x_{i} y_{j}}$ for convenience). Then, for each $S_{X Y}^{x_{i} y_{j}}$, the algorithm calculates the expected value and the $G^{2}$ test statistic (Lines $2-4)$. Subsequently, the WCI computes the weighted independence test statistics for $X$ and $Y$ using Equation (10) and determines the final p-value based on the $d f$ and the specific distribution function associated with this independence test (Lines 6-7, 16-17).

CI Testing (Lines 9-14). When the conditioning set $\mathbf{Z}$ is not empty, the adjustment factor $w$ of increase or decrease of two nodes is Equation (8), then the WCI between $X$ and $Y$ conditioning on the set $\mathbf{Z}$ is as follows:

$$
\begin{aligned}
W C I(X ; Y \mid \mathbf{Z}) & =2 \sum_{i j}^{n}\left(1+w_{i j}\right) S_{X Y Z}^{x_{i} y_{j} \mathbf{z}} \ln \left(\frac{S_{X Y Z}^{x_{i} y_{j} \mathbf{z}}}{E\left(S_{X Z}^{x_{i} \mathbf{z}} ; S_{Y Z}^{y_{j} \mathbf{z}}\right)}\right) \\
& =2 \sum_{i j}^{n} \frac{-\ln \frac{S_{X Y Z}^{x_{i} y_{j} \mathbf{z}}}{S_{Z}^{x}}}{E\left(\sum_{i j}^{n}-\ln \left(\frac{S_{X Y Z}^{x_{i} y_{j} \mathbf{z}}}{S_{Z}^{x}}\right)\right)} S_{X Y Z}^{x_{i} y_{j} \mathbf{z}} \ln \left(\frac{S_{X Y Z}^{x_{i} y_{j} \mathbf{z}} S_{Z}^{x}}{S_{X Z}^{x_{i} \mathbf{z}} S_{Y Z}^{y_{j} \mathbf{z}}}\right)
\end{aligned}
$$

If the conditioning set $\mathbf{Z}$ is not empty, the WCI counts the number of samples for each state value of $X, Y, X$ and $Y$ under the conditioning set $\mathbf{Z}$, and the conditioning set $\mathbf{Z}$ itself, respectively. Based on the sample statistics, the expected value and $G^{2}$ statistics corresponding to each $S_{X Y Z}^{x_{i} y_{j} \mathbf{z}}$ are calculated (Lines 9-11). After that, WCI computes the weight-based independence test statistics and degrees of freedom $d f$ for $X$ and $Y$ under the conditional set $\mathbf{Z}$ using Equation (11) to obtain the final p-value values (Lines 13-14, 16-17).

Note that the adjustment factor $w_{i j}$ in Equations (10) and (11) denotes the difference in the amount of information on node values compared to the average amount of information for these nodes across all state values. Thus, to mitigate the influence of the Node-imbalance phenomenon, we adjust the weight of the test statistic according to the amount of information on nodes using $\left(1+w_{i j}\right)$.

Theorem 6. In a BN, let nodes $X$ and $Y$ exist in Node-imbalance phenomenon under the conditioning set $\mathbf{Z}$, then the WCI can dynamically adjust the adjustment factor $w$ of node based on the amount of information contained in $S_{X Y Z}^{x_{i} y_{j} \mathbf{z}}$ to mitigate the effect of Node-imbalance phenomenon.

Proof. If there is Node-imbalance phenomenon on node $X$, then $S_{X Y Z}^{x_{k} y_{j} \mathbf{z}}>>S_{X Y Z}^{x_{i} y_{j} \mathbf{z}}$. Further, according to Equation (11), the following inequalities hold for the weights of test statistics on $S_{X Y Z}^{x_{k} y_{j} \mathbf{z}}$ and $S_{X Y Z}^{x_{i} y_{j} \mathbf{z}}$ :

$$
\frac{w_{i}+1}{w_{k}+1}=\frac{-\ln \frac{S_{X Y Z}^{x_{i} y_{j} \mathbf{z}}}{S_{Z}^{x}} / E\left(\frac{n}{i j}-\ln \left(\frac{S_{X Y Z}^{x_{i} y_{j} \mathbf{z}}}{S_{Z}^{x}}\right)\right)}{-\ln \frac{S_{X Y Z}^{x_{k} y_{j} \mathbf{z}}}{S_{Z}^{x}} / E\left(\sum_{i j}^{n}-\ln \left(\frac{S_{X Y Z}^{x_{i} y_{j} \mathbf{z}}}{S_{Z}^{x}}\right)\right)}>1
$$

According to the inequality equation above, Equation (11) can ensure that the test statistic weight of $S_{X Y Z}^{x_{i} y_{j} \mathbf{z}}$ is greater than that of $S_{X Y Z}^{x_{k} y_{j} \mathbf{z}}$, when $S_{X Y Z}^{x_{k} y_{j} \mathbf{z}}>S_{X Y Z}^{x_{i} y_{j} \mathbf{z}}$. Therefore, according to Theorem 5, WCI can effectively mitigate the impact of the Node-imbalance phenomenon. The same conclusion holds when the conditioning set is empty.

Furthermore, it is important to realize that small sample sizes may introduce noise, which may not be as significant in larger samples. As a result, it is necessary to appropriately reduce the noise in small samples to prevent its amplification during the weighting operation. The Yates'

continuity correction formula reduces the difference between the absolute values of expected value and observed value in the Chi-square test by 0.5 , reducing noise for small samples without affecting the test statistic for large samples [28]. The formula is given by $\chi_{\text {yetes }}^{2}=\frac{\left(\left|S_{X Y Z}^{x y z}-E\left(S_{X Z}^{x z}-S_{Y Z}^{y z}\right)\right|-0.5\right)^{2}}{E\left(S_{X Z}^{x z}-S_{Y Z}^{y z}\right)}$. According to Theorem 3, the Chi-square statistic $\mathcal{X}^{2}$ test approximates the log-likelihood statistic $G^{2}$ test. This implies that WCI can utilize the Yates' continuity correction to reduce the noise in the $G^{2}$ test statistic for small samples, thereby mitigating noise amplification while weighting $G^{2}$ test sub-items (Lines 5, 12). Specifically, WCI computes the Yates' correction $c$ corresponding to each $S_{X Y Z}^{x y z}$. If $c \geq 0$, it indicates the need to increase the test statistics between variables. Conversely, if $c<0$, it signifies the requirement to reduce the test statistics between variables. Thus, for the $G^{2}$ test, if the $G^{2}$ test statistic for $S_{X Y Z}^{x y z}$ is greater than or equal to 0 , WCI adds $c$ to increase the $G^{2}$ test statistic if $c \geq 0$, and likewise, it adds $c$ to decrease the $G^{2}$ test statistic if $c<0$, aiming to reduce the noise in small samples (i.e., Equation (13)). When the $G^{2}$ test statistic for $S_{X Y Z}^{x y z}$ is less than 0 , WCI achieves the requirements above by subtracting $c$ (i.e., Equation (14)):

$$
\begin{aligned}
& G^{2}(x ; y \mid \mathbf{z})=G^{2}(x ; y \mid \mathbf{z})+\left(\chi_{\text {yetes }}^{2}(x ; y \mid \mathbf{z})-\chi^{2}(x ; y \mid \mathbf{z})\right) \\
& G^{2}(x ; y \mid \mathbf{z})=G^{2}(x ; y \mid \mathbf{z})-\left(\chi_{\text {yetes }}^{2}(x ; y \mid \mathbf{z})-\chi^{2}(x ; y \mid \mathbf{z})\right)
\end{aligned}
$$

Case 1: Suppose the nodes $X, Y$, and the conditioning set $\mathbf{Z}$ satisfy the condition $X \Perp Y \mid \mathbf{Z}$, and $S_{X Y Z}^{x y z}$ represents a small sample. In that case, we can establish that $S_{X Y Z}^{x y z}=E\left(S_{X Z}^{x z}, S_{Y Z}^{y z}\right)$. By applying Theorem 3, we obtain $G^{2}(X ; Y \mid \mathbf{Z})=\mathcal{X}^{2}(X ; Y \mid \mathbf{Z})$. According to Equations (13) and (14), the WCI employs the Yates' correction statistic to adjust the test statistic for each $S_{X Y Z}^{x y z}$, resulting in $G^{2}(X ; Y \mid \mathbf{Z})=\mathcal{X}_{y \text { retes }}^{2}(X ; Y \mid \mathbf{Z})$, which reduces noise in small samples without affecting large samples.

Case 2: Suppose $X \Perp Y \mid \mathbf{Z}$, and $S_{X Y Z}^{x y z}$ represents a small sample. The impact of noise on small samples can be classified into two cases. (1) Noise that causes an increase in $S_{X Y Z}^{x y z}$ : Since $X \Perp Y \mid \mathbf{Z}$, this noise should be supported. According to Theorem 3, the more significant the difference between observed and expected values, the larger the difference between the $G^{2}$ test statistic and the $\mathcal{X}^{2}$ test statistic. Therefore, Equations (13) and (14) do not completely eliminate the positive effect of this noise. (2) Noise that causes a decrease in $S_{X Y Z}^{x y z}$ : Since $X \Perp Y \mid \mathbf{Z}$, this noise should be attenuated. Moreover, $S_{X Y Z}^{x y z}$ represents a small sample, and according to Theorem 3, the closer the observed value is to the expected value, the smaller the difference between the $G^{2}$ test statistic and the $\mathcal{X}^{2}$ test statistic. And hence, Equations (13) and (14) slightly reduce the negative impact of this noise.

In summary, WCI employs the Yates' continuity correction to reduce noise in small samples, thereby mitigating weighting operations that could amplify noise and impact the accuracy of independence tests.

# 6 Experiments 

In this section, we present the evaluation of the proposed WCI. Section 6.1 describes the benchmark BN used, the evaluation metrics for the independence test, and the experimental steps. We compare WCI with other CI test methods. Section 6.2 discusses the causal discovery algorithms used and the evaluation metrics for the algorithms. We apply WCI to eight state-of-the-art causal discovery algorithms to further assess its performance. The significance level for the CI tests is set at 0.01 . All the code implementations are done in Matlab, and the experiments are conducted on a computer with an Intel Core $17-127002.10 \mathrm{GHz}$ CPU and 8 GB of memory.

Table 2. Summary of Benchmark BN Datasets


# 6.1 CI Test 

To evaluate the performance of WCI, we conducted comparisons with other methods: $X^{2}$ test and $G^{2}$ test $[15,34]$. We used four benchmark $\mathrm{BNs}^{3}$ as our experimental datasets, with each network generating five datasets containing either 1,000, 2,000, or 5,000 samples. Table 2 shows the details of the four BNs. The average ratio means the average imbalance ratio of all nodes in a BN dataset, where the imbalance ratio of each node is the most occurring value in the node divided by the least occurring value. Under the faithfulness assumption, we compared the d-separation results obtained from the independence tests with the true d-separation results. This comparison allows us to assess the probability of incorrectly rejecting the null hypothesis and mistakenly accepting the null hypothesis, and thus obtains the final overall performance.

Causal discovery algorithms are based on d-separation results to determine the causal relationship between nodes. The target node and its causal node as well as the non-causal node have different d-separation results. However, judging whether two nodes are d-separated from each other is required to know the causal network structure in advance. Therefore, under the faithfulness assumption, we use CI tests to equate d-separation and thus determine the causal relationship between nodes. The CI test results and d-separation results between the same nodes vary with the condition set $\mathbf{Z}$. Therefore, to ensure fairness and standardization, we uniformly employed the Max-Min Parents and Children (MMPC) algorithm to perform CI tests between each node and all other nodes in a BN. MMPC is a heuristic search algorithm that uses the target node's candidate PCs as the conditioning set for the independence test. It iteratively adds or removes candidate PCs based on the results of independence tests to obtain the final PCs for the target node. According to Theorem 1, in a BN, there is a separating set that makes the target node independent of its non-PC. Correspondingly, there is no separating set that makes the target node independent of its PC, because the target node is always dependent on its PC. Since we know the true BN structure, if there is a non-PC node (false positive) included in the PCs (true positive) of the test node, it indicates that the d-separation result obtained from this independence test is contrary to the true d-separation result.

CI tests usually have two types of errors, Type I and Type II errors. Based on the above analysis, under the faithfulness assumption, the erroneous dependency relationship (Type I error) causes a redundant causal network structure and the number of CI tests. Erroneous independent relationship (Type II error) will cause the absence of causal network structure. Therefore, if there is a falsepositive node in the PC set of a node, then it means that a Type I error has occurred in some CI test of this node, and if the causal node is missing in the PC set, it means that Type II error has occurred in some CI test of this node. Thus, a higher recall of the causal discovery algorithm means a lower probability of Type II error for the CI test, and the higher the accuracy, the lower the probability of Type I error for the CI test with the same recall. In addition, other things being equal, when the

[^0]
[^0]:    ${ }^{3}$ These datasets are publicly available at https://www.bnlearn.com/bnrepository/

Table 3. Detailed Experimental Results of the WCI Test and Other Independence Tests for Identifying d-Separation in Four Unbalanced BNs


$\downarrow$ means the smaller the better, $\uparrow$ means the bigger the better.
probability of Type I error decreases, the likelihood of Type II error increases. Thus, F1 serves as a comprehensive assessment considering both errors. CITs and Time metrics, on the other hand, are a consideration of the effect of CI tests on the efficiency of causal discovery. In summary, the evaluation metrics used in our study are as follows:
$-F 1$ : The harmonic average of precision and recall is used to calculate the $F 1$ score ( $F 1=$ $2 \cdot$ Precision $\cdot$ Recall $/($ Precision + Recall)).
$-$ Precision: The number of true positive in the output divided by the sum of the number of true positives and false positives in the output of the MMPC algorithm.
$-$ Recall: The number of true positives in the output divided by the number of true positives in the BN.
-CITs: The number of CI tests for the MMPC algorithm.
-Time: The running time of the MMPC algorithm is used to evaluate the impact of the CI tests on the efficiency of the algorithm.

Table 3 presents a comprehensive summary of the detailed metrics, including F1, Precision, Recall, CITs, and Time for each CI test. The values are presented in the format $A \pm B$, where $A$ represents the mean and $B$ represents the variance. The best results are highlighted in bold within the table. Furthermore, to provide an integrated evaluation of the performance and efficiency of each CI test, we have normalized the results. Table 4 reports the normalized $F 1$ and CITs for each independence test. The normalized values are calculated by dividing the $F 1$ or CITs of each CI test for a specific sample size and network by the corresponding values of WCI for the same sample size and network. For visualization, in Figure 3, normalized CITs larger than 1 indicate that the CI test is slower than WCI, while normalized $F 1$ less than 1 suggests that the CI test is worse than WCI.

From the experimental results in Table 3, we have the following analysis: In terms of precision metrics, compared with the best results achieved by the other two CI tests, WCI reaches an average increase in precision of $7 \%$ and $6 \%$ in Barley network, $7 \%$ and $3 \%$ in Pathfinder network, $5 \%$ and $3 \%$ in Hailfinder network, and $6 \%$ and $0 \%$ in Pigs network, respectively. But, on the recall metric,

![img-2.jpeg](img-2.jpeg)

Fig. 3. Normalized SHD vs. normalized CITs with 1,000 (left), 2,000 (center), and 5,000 (right) data samples. SHD, Structural hamming distance.
there was a slight decrease in the WCI compared to the best experimental results. Thus, under the faithfulness assumption, WCI can significantly reduce the number of false-positive nodes while ensuring that the number of correct true-positive nodes is found to be slightly decreased, allowing the causal discovery algorithm to reduce additional false causal orientations (to be verified in Section 6.2). Since WCI considers the impact of the Node-imbalance phenomenon, it accurately measures the dependency relationships between nodes. The recall of WCI on the Pathfinder network is improved by about $4 \%$ compared with the recall of the $G^{2}$ test, which also verifies to some extent that WCI also has good performance in measuring the independent relationship of nodes. In addition, according to the formula for calculating the amount of information $H(X)=-\ln p(x)$, when $\mathrm{p}(\mathrm{x})$ takes values ranging between $0 \sim 1$, the growth rate of the amount of information decreases as $S_{X Y Z}^{x y z}$ increases. Therefore, according to Equations (7) and (8), the number of $S_{X Y Z}^{x y z}$ that increases the weight will be less than or equal to the number of $S_{X Y Z}^{x y z}$ that decreases. Since not all node imbalances lead to independent test errors, it is possible that some imbalanced nodes with correct independence tests may cause a decrease in test statistics based on information weighting, resulting in a slight decrease in recall for WCI compared to the other CI tests with the best results.

According to Table 4 and Figure 3, our observations are summarized as follows: In terms of overall performance $F 1$, WCI achieves the highest $F 1$ scores in all the datasets, and the normalized $F 1$ values of the other CI tests ranged from 0.84 to 0.97 . In terms of CITs, WCI improved the efficiency of the causal discovery algorithm by reducing the number of CI tests in eight datasets. After normalization, most of the CITs values normalized for the other CI tests fell between 1.01 and 2.67. Specifically, WCI can have higher precision and slightly lower recall compared to the other CI tests. This indicates that WCI reduces the number of false-positive nodes, allowing causal discovery algorithms to reduce additional incorrect causal directions and the number of CI tests through WCI. Further analyzed, MMPC is divided into two steps: discovering candidate PC nodes and removing false-positive nodes from candidate PC nodes. Therefore, the number of CI tests in the algorithm is affected by precision and recall. The higher the recall, the more correct true-positive nodes are found by MMPC, which increases the number of CI tests in the algorithm. With the same recall, higher precision means a lower probability of error in the CI tests in the first and second steps of the algorithm. Thus, fewer false-positive nodes enter the candidate PC set in the first stage of the algorithm, and the more false-positive nodes are removed in the second stage, which improves the precision of the algorithm and reduces the number of CI tests in which the algorithm removes false-positive nodes. This explains why on the Barley, Hailfinder, and Pigs datasets, the WCI guarantees a higher $F 1$ and a lower number of CI tests compared to the other CI tests. On the Pathfinder dataset, the WCI has a higher recall than the $G^{2}$ test, so the number of CI tests is higher than the $G^{2}$ test.

In summary, the results on these four BN datasets demonstrate that WCI can more accurately determine the dependency relationship between nodes in the presence of the Node-imbalance phenomenon. As the Node-imbalance ratio increases, the effect of WCI enhancement becomes more obvious. WCI considers the impact of the Node-imbalance phenomenon and adjusts the weight of its test statistic according to the amount of information on nodes to mitigate this influence. This means that existing causal discovery algorithms can reduce the number of unnecessary false causal orientations and the number of independence tests while maintaining the number of correct causal orientations found by using WCI, which will be further verified in Section 6.2.

# 6.2 Performance in Causal Discovery 

To evaluate the enhanced causal discovery effect achieved by the WCI, we follow the data generation process described in the previous subsection, and apply the WCI to eight different causal discovery algorithms [19], ${ }^{4}$ including four global causal structure learning algorithms, three local causal structure learning algorithms, and one PSL algorithm. The details of the algorithms used are as follows:

- Global causal structure learning: PC [27], PC-stable [3], MMHC [29], ADL [13].
- Local causal structure learning: PCD-by-PCD [33], CMB [8], ELCS [31].
- PSL [18].

It is important to highlight that the PSL algorithm exhibits high flexibility. Our experiments classify PSL as a local causal structure learning algorithm when the learning depth is set to 1 , referred to as PSL-local. Conversely, when the learning depth is set to the maximum, we classify PSL as a global causal structure learning algorithm called PSL-global. Additionally, the original causal discovery algorithm utilizes $G^{2}$ test for CI test. Based on the previous analysis and Theorems 1 and 2, incorrect CI test results lead to incorrect causal skeleton structures and causal orientations, and affect the efficiency of the algorithm. Therefore, we use the following metrics to evaluate the impact of WCI on the performance of the causal discovery algorithms described above:
-SHD: The sum of values of Miss, Extra, and Reverse.
-CITs: The number of CI tests for the algorithm.
Figures 4 to 6 summarize the specific values of SHD and CITs for the WCI test and $G^{2}$ test applied to the global causal structure learning algorithms. Figure 7 shows the percentages of SHD and CITs improvement or reduction for the global structure learning algorithms and the local structure learning algorithms, respectively, after using the WCI test. That is, the SHD (CITs) of the original algorithm minus the SHD (CITs) of the algorithm after using WCI divided by the SHD (CITs) of the original algorithm. Furthermore, Figures 8 to 10 summarize the specific values of SHD and CITs for the WCI test and $G^{2}$ test applied to the local causal structure learning algorithms. Figure 11 shows the percentages of SHD and CITs improvement or reduction for the local structure learning algorithms and the local structure learning algorithms, respectively, after using the WCI test.

Global Causal Structure Learning: The existing global structure learning process can be divided into two steps: global skeleton learning and global skeleton orientation. Constraint-based global structure learning algorithms use CI tests to determine the causal skeleton and orient the causal orientations, and hybrid global structure learning algorithms utilize CI tests to establish the causal skeleton. Based on the observations in Figures 4 to 6, we can conclude that applying the WCI test to the five global learning algorithms resulted in improvements in the SHD metrics regardless of the datasets. This improvement can be attributed to the higher accuracy of WCI, which enables the

[^0]
[^0]:    ${ }^{4}$ The code for WCI and applied causal discovery algorithms are available at http://bigdata.ahu.edu.cn/causal-learner

![img-3.jpeg](img-3.jpeg)

Fig. 4. The results of the experiments for the accuracy (the fewer SHD, the better) and efficiency (the fewer CITs, the better) of applying WCI test and $G^{2}$ test to global causal structure learning algorithms on four benchmark BN datasets with 1,000 samples (the labels of the $x$-axis from 1 to 4 denote the BNs. 1: Barley. 2: Pathfinder. 3: Hailfinder. 4: Pigs).
![img-4.jpeg](img-4.jpeg)

Fig. 5. The results of the experiments for the accuracy (the fewer SHD, the better) and efficiency (the fewer CITs, the better) of applying WCI test and $G^{2}$ test to global causal structure learning algorithms on four benchmark BN datasets with 2,000 samples (the labels of the $x$-axis from 1 to 4 are the same as those in Figure 3).
algorithm to reduce the number of false-positive nodes during skeleton construction, resulting in a more accurate causal skeleton structure. Since the constraint-based algorithm uses the CI test to identify V-structures in the skeleton orientation phase for causal orientations, more accurate V-structure identification results in a reduction in the number of reversed edges. Furthermore, as the MMHC and ADL are hybrid algorithms, a more accurate causal skeleton enables them to reduce the number of SHD by avoiding false causal directions during search scoring.

Combining the impact of WCI on the performance of global structure learning algorithms, we can have the following experimental conclusion from Figure 7; after applying the WCI test, the five global structure learning algorithms obtained fewer numbers of SHD, and learned more accurate global causal network structures. In most datasets, the five global structure learning algorithms reduced the number of CI tests and possessed higher efficiency. Specifically, compared to PC and PC-stable, PC-w and PC-stable-w have reduced SHD by more than $5 \%$ in all datasets and more

![img-5.jpeg](img-5.jpeg)

Fig. 6. The results of the experiments for the accuracy (the fewer SHD, the better) and efficiency (the fewer CITs, the better) of applying WCI test and $G^{2}$ test to global causal structure learning algorithms on four benchmark BN datasets with 5,000 samples (the labels of the $x$-axis from 1 to 4 are the same as those in Figure 3).
![img-6.jpeg](img-6.jpeg)

Fig. 7. The percentage improvement or decrease in SHD and CITs of WCI test applied to global structural learning algorithms on four BN datasets with different samples (the labels of the $x$-axis from 1 to 4 denote the BNs. 1: Barley. 2: Pathfinder. 3: Hailfinder. 4: Pigs).
than $11 \%$ in 10 datasets. In terms of efficiency, PC-w reduces the number of CI tests by more than $6 \%$ in eight datasets, while PC-stable-w reduces it by more than $7 \%$ in eight datasets. Compared to MMHC, MMHC-w reduces SHD value by more than $4 \%$ in nine datasets. On the CITs metric, MMHC-w had fewer CI tests in 11 datasets and reduced the number of CI tests by more than $8 \%$ in 9 datasets. PSL-global-w reduced the SHD by more than $8 \%$ in 8 out of the 12 datasets using the WCI and reduced the number of CI tests in 9 datasets by more than $6 \%$. Similarly, with WCI, ADL reduced SHD by more than $4 \%$ in 9 of the 12 datasets. Regarding efficiency, ADL decreased the number of CI tests by more than $5 \%$ in 8 of the 12 datasets. In summary, all the algorithms can have a better global causal structure learning performance when using the WCI test, and improved algorithmic efficiency on most datasets, regardless of the sample size of 1,000, 2,000, or 5,000. Additionally, the algorithms show improved efficiency on the Barley, Hailfinder, and Pigs datasets, then these improvements can be attributed to the inadequacy of the $G^{2}$ test in accurately measuring dependencies between nodes when dealing with unbalanced data. This leads to more non-PC nodes being included in the PCs, resulting in incorrect causality and causal orientations.

![img-7.jpeg](img-7.jpeg)

Fig. 8. The results of the experiments for the accuracy (the fewer SHD, the better) and efficiency (the fewer CITs, the better) of applying WCI test and $G^{2}$ test to local causal structure learning algorithms on four benchmark BN datasets with 1,000 samples (the labels of the $x$-axis from 1 to 4 are the same as those in Figure 3).
![img-8.jpeg](img-8.jpeg)

Fig. 9. The results of the experiments for the accuracy (the fewer SHD, the better) and efficiency (the fewer CITs, the better) of applying WCI test and $G^{2}$ test to local causal structure learning algorithms on four benchmark BN datasets with 2,000 samples (the labels of the x-axis from 1 to 4 are the same as those in Figure 3).

Consequently, more CI tests are required, which negatively impacts the accuracy and efficiency of global causal structure learning algorithms.

Local Causal Structure Learning: The existing local structure learning algorithms are also divided into two steps: local skeleton learning and local skeleton orientation, both of which utilize CI tests to construct and orient the causal structure. Based on the experimental data in Figures 8 to 10, the following observations can be made: On the Barley, Pathfinder, Hailfinder, and Pigs datasets, the four local causal structure learning algorithms exhibit lower SHD and fewer CI tests. This indicates that applying WCI to local structure learning algorithms can reduce redundant causal skeleton structures in the local skeleton learning stage and reduce the occurrence of unnecessary causal orientations. Thus, WCI enhances the identification of the correct causal skeleton structure and reduces the number of missing causal orientations.

![img-9.jpeg](img-9.jpeg)

Fig. 10. The results of the experiments for the accuracy (the fewer SHD, the better) and efficiency (the fewer CITs, the better) of applying WCI test and $G^{2}$ test to local causal structure learning algorithms on four benchmark BN datasets with 5,000 samples (the labels of the $x$-axis from 1 to 4 are the same as those in Figure 3).
![img-10.jpeg](img-10.jpeg)

Fig. 11. The percentage improvement or decrease in SHD and CITs of WCI test applied to local structural learning algorithms on four BN datasets different samples (the labels of the $x$-axis from 1 to 4 denote the BNs. 1: Barley. 2: Pathfinder. 3: Hailfinder. 4: Pigs).

To comprehensively measure the impact of WCI on the performance of four local structure learning algorithms, we can draw the following experimental conclusions from Figure 11: After using WCI, the four local structure learning algorithms outperform the original algorithms in terms of their structure learning capabilities across most datasets. Specifically, PCD-by-PCD reduces the SHD value by more than $10 \%$ in 10 out of 12 datasets and reduces the number of CI tests by more than $5 \%$ in 10 datasets. CMB-w improves the structure learning accuracy by more than $7 \%$ in all datasets and improves the structure learning efficiency by more than $7 \%$ in eight datasets. For ELCS, the application of WCI reduced the number of learning error edges by more than $11 \%$ for nine datasets, and more than $17 \%$ for eight datasets. In addition, ELCS-w reduced the number of CI tests by more than $8 \%$ for the nine datasets, improving efficiency. When using WCI tests, PSL-local reduced SHD by over $4 \%$ on all datasets. Regarding efficiency, PSL-local-w reduces the number of CI tests on 11 datasets by more than $7 \%$. In summary, the four local causal structure learning algorithms obtain more accurate local causal structures and improved algorithmic efficiency on most datasets by using WCI tests, regardless of whether the data sample size is $1,000,2,000$, or

5,000. In summary, all algorithms achieve more accurate local causal structures after using the WCI test. Additionally, all algorithms demonstrate a reduction in the number of CI tests on the Barley, Hailfinder, and Pigs datasets. Applying WCI helps mitigate the impact of the Node-imbalance phenomenon, leading to more accurate CI test results and avoiding erroneous causality and causal orientations. It also reduces the number of redundant CI tests. Consequently, integrating WCI into local causal structure algorithms enhances accuracy and efficiency.

# 7 Conclusion 

In this article, a new concept, the Node-imbalance phenomenon, is proposed in BN to describe the problem of significant differences in the number of observed samples between different state values due to the unbalanced distribution of node values. We analyze the impact of the Node-imbalance phenomenon on traditional independence tests and propose a WCI test to tackle the issue of node imbalance. WCI aims to decrease the likelihood of falsely rejecting true hypotheses and incorrectly accepting false hypotheses in independence tests conducted on imbalanced data, and achieves comparable recall and higher precision, enabling causal discovery algorithms to reduce redundant causal skeleton structures and incorrect causal orientations.

We conduct experiments to compare WCI with other independence tests using four unbalanced benchmark BN datasets, and apply WCI to eight state-of-the-art causal discovery algorithms. The experimental results demonstrate that WCI exhibits superior performance in handling unbalanced data.

In addition, it should be noted that WCI is currently unable to fully resolve the imbalance phenomenon. Since we have yet to determine how much statistics should be adjusted for subitems with different size relationships to eliminate the effect of imbalance. We use the amount of information of the nodes to adaptively mitigate the disparity of statistics between sub-items with inconsistent size relationships, and thus mitigate the effect of imbalance on the $G^{2}$ test. In the future, we will explore new methods to completely resolve the effect of the imbalance phenomenon on $G^{2}$ tests. At the same time, we will try to solve the problem of redundancy or missing information in causal feature selection due to the imbalance phenomenon and improve the accuracy of Markov blanket discovery for class variables.
