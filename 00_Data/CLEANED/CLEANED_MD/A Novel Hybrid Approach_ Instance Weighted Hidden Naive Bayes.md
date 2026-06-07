# Article 

## A Novel Hybrid Approach: Instance Weighted Hidden Naive Bayes

Liangjun Yu ${ }^{1,2}$ (D), Shengfeng Gan ${ }^{1, *}$, Yu Chen ${ }^{1,2}$ and Dechun Luo ${ }^{3,4}$


#### Abstract

check for updates Citation: Yu, L.; Gan, S.; Chen, Y.; Luo, D. A Novel Hybrid Approach: Instance Weighted Hidden Naive Bayes. Mathematics 2021, 9, 2982. https://doi.org/10.3390/math9222982


Academic Editor: María Purificación Galindo Villardón

Received: 13 October 2021
Accepted: 19 November 2021
Published: 22 November 2021

Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## (0) 0

Copyright: (c) 2021 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 College of Computer, Hubei University of Education, Wuhan 430205, China; yuliangjun@hue.edu.cn (L.Y.); chenyu@hue.edu.cn (Y.C.)
2 Hubei Co-Innovation Center of Basic Education Information Technology Services, Hubei University of Education, Wuhan 430205, China
3 School of Management, Huazhong University of Science and Technology, Wuhan 430071, China; m202077097@hust.edu.cn
4 Wuhan Eight Dimension Space Information Technology Co., Ltd., Wuhan 430071, China

* Correspondence: sf_gan@hue.edu.cn


#### Abstract

Naive Bayes (NB) is easy to construct but surprisingly effective, and it is one of the top ten classification algorithms in data mining. The conditional independence assumption of NB ignores the dependency between attributes, so its probability estimates are often suboptimal. Hidden naive Bayes (HNB) adds a hidden parent to each attribute, which can reflect dependencies from all the other attributes. Compared with other Bayesian network algorithms, it offers significant improvements in classification performance and avoids structure learning. However, the assumption that HNB regards each instance equivalent in terms of probability estimation is not always true in real-world applications. In order to reflect different influences of different instances in HNB, the HNB model is modified into the improved HNB model. The novel hybrid approach called instance weighted hidden naive Bayes (IWHNB) is proposed in this paper. IWHNB combines instance weighting with the improved HNB model into one uniform framework. Instance weights are incorporated into the improved HNB model to calculate probability estimates in IWHNB. Extensive experimental results show that IWHNB obtains significant improvements in classification performance compared with NB, HNB and other state-of-the-art competitors. Meanwhile, IWHNB maintains the low time complexity that characterizes HNB.


Keywords: Bayesian network; hidden naive Bayes; instance weighting

## 1. Introduction

Bayesian network (BN) combines knowledge of network topology and probability. It is a classical method which can be used to predict a test instance [1]. The BN structure is a directed acyclic graph, and each edge in BN reflects the dependency between attributes. Unfortunately, it has been confirmed that finding the optimal BN from arbitrary BNs is an non-deterministic polynomial (NP)-hard problem [2,3]. Naive Bayes (NB) is one of the most classic and efficient models in BNs. It is easy to construct but surprisingly effective [4]. The NB model is shown in the Figure 1a. $A_{1}, A_{2}, \cdots, A_{m}$ denote $m$ attributes. The class variable $C$ is the parent node of each attribute. Each attribute $A_{i}$ is independent from the others.

The classification performance of NB is comparable to well-known classifiers [5,6]. However, the conditional independence assumption of NB ignores the dependencies between attributes in real-world applications, so its probability estimates are often suboptimal $[7,8]$. In order to reduce the primary weakness brought by the conditional independence assumption, a lot of improved approaches of NB have been proposed to alleviate the primary weakness in NB by manipulating attribute independence assertions $[9,10]$. These improved approaches can fall into five main categories: (1) Structure

extension by extending the NB's structure to overcome the attribute independence assertions [11,12,13,14]; (2) Instance weighting by constructing a NB classifier on an instance weighted dataset [15,16,17,18]; (3) Instance selection by constructing a NB classifier on a selected local instance subset [19,20,21]; (4) Attribute weighting by constructing a NB classifier on an attribute weighted dataset [22,23,24,25,26]; (5) Attribute selection by constructing a NB classifier on a selected attribute subset [27,28,29,30].
![img-0.jpeg](img-0.jpeg)
(a) Naïve Bayes
![img-1.jpeg](img-1.jpeg)
(b) Hidden Naïve Bayes
![img-2.jpeg](img-2.jpeg)
(c) Instance Weighted Hidden Naive Bayes

Figure 1. The different structures of related models.
Structure extension adds finite directed edges to reflect the dependencies between attributes [31]. It is efficient to overcome the conditional independence assumption of NB, since probabilistic relationships among attributes can be explicitly denoted by directed arcs [32]. Among various structure extension approaches, the hidden naive Bayes (HNB) is an improved model that essentially combines mixture dependencies of attributes [33]. It can display Bayesian network topology well and reflect the dependencies from all other attributes. However, HNB regards each instance as equally important when computing probability estimates. This assumption is not always true because different instances could have different contributions. In order to improve the classification performance of HNB, it will be interesting to study whether a better classification performance can be achieved by constructing an improved HNB model on the instance weighted dataset. The resulting model which combines instance weighting with the improved HNB model into one uniform framework inherits the effectiveness of HNB, and reflects different influences of different instances.

In this study, we propose the novel hybrid model which combines instance weighting with the improved HNB model into one uniform framework, referred to as instance weighted hidden naive Bayes (IWHNB). With the research of the existing HNB model, we propose an improved HNB model that can reflect different contributions of different instances. In contrast to the existing HNB model, the improved HNB model is built on the instance weighted dataset. Instance weights are incorporated into generating each

hidden parent to reflect mixture dependencies of both attributes and instances. In our IWHNB approach, the improved HNB model is proposed to approximate the groundtruth attribute dependencies. Meanwhile, instance weights are calculated by the attribute value frequency-based instance weighted filter. Each instance weight is incorporated into probability estimates and the classification formula in IWHNB.

We have completed experiments to compare IWHNB with NB, HNB, and other state-of-the-art competitors. Empirical studies show that IWHNB obtains more satisfactory classification performance than its competitors. Meanwhile, IWHNB maintains the low time complexity that characterizes HNB. The main contributions of the work presented in this paper can be briefly summarized as follows:

1. We reviewed the related work about structure extension and found that there is almost no method that focuses on the hybrid paradigm which combines structure extension with instance weighting.
2. We reviewed the related work about the existing instance weighting approaches and found that the Bayesian network in these researches is limited to NB.
3. The IWHNB approach is an improved approach which combines instance weighting with the improved HNB model into one uniform framework. It is a new paradigm to calculate discriminative instance weights for the structure extension model.
4. Although some training time is spent to calculate the weight of each instance, the experimental results show that our proposed IWHNB approach is still simple and efficient. Meanwhile, the classification performance of the IWHNB approach is more satisfactory than its competitors.
The paper is organized as follows. In Section 2, we review the related work with regard to this paper. In Section 3, we propose our IWHNB approach. In Section 4, we describe the experimental setup and results. In Section 5, we give our conclusions and outline suggestions for future research.

# 2. Related Work 

### 2.1. Structure Extension

Structure extension adds finite directed edges to encode probabilistic relationships. The extended NB structure encodes attribute independence statements, where directed arcs can explicitly characterize the joint probability distribution. In the case of given its parents, the attribute is independent of its non descendants. Given a test instance $x$, represented by an attribute vector $\left\langle a_{1}, a_{2}, \cdots, a_{m}\right\rangle$, Equation (1) is formalized to classify instance $x$ in structure extended NB:

$$
c(x)=\arg \max _{c \in C} P(c) \prod_{i=1}^{m} P\left(a_{i} \mid \Pi_{a_{i}}, c\right)
$$

where $m$ is the number of attributes, $\Pi_{a_{i}}$ is the attribute value(s) of $\Pi_{A_{i}}$, and $\Pi_{A_{i}}$ denotes the set of parent nodes of $A_{i}$ except for the class node $C$. The prior probability $P(c)$ is defined by Equation (2) as follows:

$$
P(c)=\frac{1+\sum_{t=1}^{n} \delta\left(c_{t}, c\right)}{q+n}
$$

where $n$ is the number of training instances, $c_{t}$ is the class label of the $t$ th training instance, $q$ is the number of classes, and $\delta(\bullet)$ is a binary function, where the value is 1 when two variables are equal, and the value is 0 when unequal.

A number of structure extension approaches have been proposed to alleviate the primary weakness in NB [31]. The network structure of tree-augmented naive Bayesian (TAN) comprising all the attribute nodes is tree-like [14]. The class is the parent node of each attribute, and each attribute can have only one other attribute parent from other attributes. Aggregating one-dependence estimators (AODE) aggregate the joint probability distribution of all qualified classifiers [12]. This Bayesian model directly makes each

attribute the parent node of all other attributes, and does not need to learn the topological structure between attributes. Weighted average of one-dependence estimators (WAODE) is proposed to assign different weights to different one-dependence estimators [34]. Each attribute is set as the root attribute once.

Among various structure extension approaches, the hidden naive Bayes (HNB) [33] is an improved model that essentially combines mixture dependencies of attributes. In this study, our proposed IWHNB approach is based on the HNB model, so the HNB model is introduced in detail here. The existing HNB model is shown in the Figure 1b. C is the class label. Each hidden parent $A_{h p_{i}}, i=1,2, \cdots, m$ is created for each attribute $A_{i}$. A dashed directed line which is from each hidden parent $A_{h p_{i}}$ to attribute $A_{i}$ distinguishes it from a regular arc. A test instance $x, x=<a_{1}, \cdots, a_{m}>$ classified by HNB is formalized as Equation (3):

$$
c(x)=\arg \max _{c \in C} P(c) \prod_{i=1}^{m} P\left(a_{i} \mid a_{h p_{i}}, c\right)
$$

where the prior probability $P(c)$ is also computed by Equation (2). A hidden parent $A_{h p_{i}}$ is created for each attribute $A_{i}$. The probability $P\left(a_{i} \mid a_{h p_{i}}, c\right)$ is formalized as Equation (4):

$$
P\left(a_{i} \mid a_{h p_{i}}, c\right)=\sum_{j=1, j \neq i}^{m} W_{i j} * P\left(a_{i} \mid a_{j}, c\right)
$$

where $W_{i j}(i, j=1,2, \cdots, m$ and $i \neq j)$ are the weights calculated to reflect influences from other attributes. $W_{i j}$ is calculated as Equation (5):

$$
W_{i j}=\frac{I_{P}\left(A_{i} ; A_{j} \mid C\right)}{\sum_{j=1, j \neq i}^{m} I_{P}\left(A_{i} ; A_{j} \mid C\right)}
$$

where $I_{P}\left(A_{i} ; A_{j} \mid C\right)$ is the conditional mutual information formalized as Equation (6):

$$
I_{P}\left(A_{i} ; A_{j} \mid C\right)=\sum_{a_{i}, a_{j}, c} P\left(a_{i}, a_{j} \mid c\right) \log \frac{P\left(a_{i}, a_{j} \mid c\right)}{P\left(a_{i} \mid c\right) P\left(a_{j} \mid c\right)}
$$

where $P\left(a_{i} \mid c\right), P\left(a_{j} \mid c\right)$ and $P\left(a_{i} \mid a_{j}, c\right)$ are formalized as Equations (7)-(9), respectively:

$$
\begin{gathered}
P\left(a_{i} \mid c\right)=\frac{1+\sum_{t=1}^{n} \delta\left(a_{t i}, a_{i}\right) \delta\left(c_{t}, c\right)}{n_{i}+\sum_{t=1}^{n} \delta\left(c_{t}, c\right)} \\
P\left(a_{j} \mid c\right)=\frac{1+\sum_{t=1}^{n} \delta\left(a_{t i}, a_{j}\right) \delta\left(c_{t}, c\right)}{n_{j}+\sum_{t=1}^{n} \delta\left(c_{t}, c\right)} \\
P\left(a_{i}, a_{j} \mid c\right)=\frac{1+\sum_{t=1}^{n} \delta\left(a_{t i}, a_{i}\right) \delta\left(a_{t j}, a_{j}\right) \delta\left(c_{t}, c\right)}{n_{i}+\sum_{t=1}^{n} \delta\left(a_{t j}, a_{j}\right) \delta\left(c_{t}, c\right)}
\end{gathered}
$$

where $a_{t i}$ is the $i$ th attribute value of the $t$ th training instance, $n_{i}$ is the number of values for the $i$ th attribute.

In the HNB model, we can see that each hidden parent essentially combines mixture dependencies of all other attributes. The HNB model avoids structure learning with intractable computational complexity and reflects the dependencies from all other attributes, but it regards each instance equally important when computing probability estimates.

# 2.2. Instance Weighting 

Naive Bayes (NB) is one of the most classic and efficient models in Bayesian networks. The classification performance of the NB classifier is comparable to state-of-the-art classifiers. The classifier of NB uses Equation (10) to classify a test instance $x$ :

$$
c(x)=\arg \max _{c \in \mathrm{C}} P(c) \prod_{i=1}^{m} P\left(a_{i} \mid c\right)
$$

where the prior probability $P(c)$ is also computed by Equation (2). In the meantime, the conditional probability $P\left(a_{i} \mid c\right)$ is defined by Equation (11):

$$
P\left(a_{i} \mid c\right)=\frac{1+\sum_{t=1}^{n} \delta\left(a_{t i}, a_{i}\right) \delta\left(c_{t}, c\right)}{n_{i}+\sum_{t=1}^{n} \delta\left(c_{t}, c\right)}
$$

where $n_{i}$ is the number of values for the $i$ th attribute.
Instance weighting is a practical way to improve NB by constructing a NB classifier on the instance weighted dataset [35]. It calculates the discriminative weight of each instance according to the distribution of the instance. Instance weighted NB still uses Equation (10) to classify a test instance $x$. The classification formula of instance weighted NB is the same as that for NB. However, different from the NB classifier, instance weighted NB calculates the discriminative weight of each instance, and incorporates discriminative instance weights into the prior probability and the conditional probability estimates. The prior probability $P(c)$ is redefined by Equation (12):

$$
P(c)=\frac{1+\sum_{t=1}^{n} w_{t} \delta\left(c_{t}, c\right)}{q+\sum_{t=1}^{n} w_{t}}
$$

where $w_{t}$ is the weight of the $t$ th training instance. In the meantime, the conditional probability $P\left(a_{i} \mid c\right)$ is redefined by Equation (13):

$$
P\left(a_{i} \mid c\right)=\frac{1+\sum_{t=1}^{n} w_{t} \delta\left(a_{t i}, a_{i}\right) \delta\left(c_{t}, c\right)}{n_{i}+\sum_{t=1}^{n} w_{t} \delta\left(c_{t}, c\right)}
$$

How to calculate the different weight of each instance to build an instanced weighted NB classifier is crucial. Instance weighting approaches can broadly fall into two categories: eager learning and lazy learning. Eager learning uses general characteristics of instances to calculate instance weights during the training phase. Each instance weight is directly computed as a preprocessing step before the classification phase. Rather than calculating instance weights based on general characteristics of instances, lazy learning is more profitable to optimize instance weights at classification phase. Lazy learning first uses search algorithms to search for instance weights, and then optimize instance weights by building the target classifier on the instance weighted NB. Lazy learning spends more computational cost. So, eager learning normally is faster to calculate instance weights compared to lazy learning, but lazy learning has better classification performance than eager learning.

Discriminatively weighted NB uses the estimated conditional probability loss to calculate discriminative instance weights [15]. It is an eager learning approach, it achieves remarkable classification results in both classification accuracy and ranking. Attribute value frequency weighted NB is a simple and efficient eager learning approach [18]. This instance weighting filter focuses on the frequency of each attribute value to learn the weight of each instance. It calculates each instance weight according to its attribute value number and its attribute value frequency. Lazy NB clones each instance in the neighborhood [16]. It is a lazy learning approach. It calculates the similarity between the test instance and each training instance, and clones are then made based on the similarity. The improved algorithm called instance weighted NB finds the mode within training instances, and then calculates each weight according to the similarity between the mode and each instance [17].

Numerous instance weighting studies have revealed that the Bayesian networks in these existing instance weighting approaches are all limited to NB. It will be interesting to study whether a better classification performance can be obtained by exploiting instance weighting on the structure extended NB.

# 3. Instance Weighted Hidden Naive Bayes 

The studies show that both structure extension and instance weighting can improve the classification performance. Structure extension extends the structure to overcome the unrealistic assumption, but regards each instance as equally important. Instance weighting weights each instance discriminatively to overcome the conditional independence assumption. Each instance weight is incorporated to calculate probability estimates, but the Bayesian network of existing instance weighting approaches is limited to NB. Based on the above analysis, we study whether more satisfying classification results can be obtained by exploiting instance weighting on the structure extended NB.

Following the reasons above, this paper focuses the research on the new hybrid paradigm which combines structure extension with instance weighting. The extended structure should be more accurate to reflect the dependency between attributes. Meanwhile, different instance weights can be incorporated into probability estimates and the classification formula to give more accurate results compared to traditional methods. Learned instance weights can reflect different contributions of different instances. Based on these, we propose a new hybrid approach which combines the improved hidden naive Bayes with instance weighting into one hybrid model. This improved hybrid approach is called instance weighted hidden naive Bayes (IWHNB). We modify the HNB model into the instance weighted hidden naive Bayes (IWHNB) model. In the following subsection, we describe the IWHNB model in detail.

### 3.1. The Instance Weighted Hidden Naive Bayes Model

Hidden naive Bayes (HNB) generates a hidden parent to each attribute to reflect dependencies from all other attributes [33]. Figure 1 effectively creates relationships among the models, as if they had evolved directly from one to the other. As Figure 1a shows, naive Bayes (NB) is one of the most classic and efficient models in BNs. As Figure 1b shows, the HNB model essentially adds a hidden parent to each attribute, but it regards each instance as equally important. The HNB model avoids structure learning with intractable computational complexity. It can be interpreted as the weight of each instance is set to 1 by default in HNB. However, in the training dataset, some instances contribute more to classification than others, so they should have more influence than less important instances. Different contributions for different instances can be a very important consideration.

Motivated by the work of HNB [33], we modify the HNB model into the instance weighted hidden naive Bayes model in our IWHNB approach. The instance weighted hidden naive Bayes model is shown in the Figure 1c. C is the class label, and is the parent node of each attribute. A hidden parent $A_{h p_{i}}, i=1,2, \cdots, m$ is also created for each attribute $A_{i} . n$ is the number of training instances. $w_{t}$ is the weight of the $t$ th training instance. In the improved HNB model, each instance weight $w_{t}$ is integrated to generate the hidden parent to each attribute. A dashed directed line which is from each hidden parent $A_{h p_{i}}$ to attribute $A_{i}$ distinguishes it from a regular parent. Different from the existing HNB model, the improved HNB model not only essentially reflects dependencies from all other attributes but also can reflect different contributions of different instances.

In our IWHNB approach, the test instance $x=<a_{1}, \cdots, a_{m}>$ classified by IWHNB is formalized as Equation (14):

$$
c(x)=\arg \max _{c \in C} P(c) \prod_{i=1}^{m} P\left(a_{i} \mid a_{h p_{i}}, c\right)
$$

Although the classification formula of our IWHNB approach is the same as that for HNB, the calculations of the probabilities $P(c)$ and $P\left(a_{i} \mid a_{h p_{i}}, c\right)$ are different. We embed each instance weight $w_{t}$ into the generation of each hidden parent. Instance weights are also incorporated into calculating probabilities. The detailed processes are described as follows. Firstly, we redefine the prior probability $P(c)$ as Equation (15):

$$
P(c)=\frac{1+\sum_{t=1}^{n} w_{t} \delta\left(c_{t}, c\right)}{q+\sum_{t=1}^{n} w_{t}}
$$

Secondly, the probability $P\left(a_{i} \mid a_{h p_{i}}, c\right)$ is formalized as Equation (16).

$$
P\left(a_{i} \mid a_{h p_{i}}, c\right)=\sum_{j=1, j \neq i}^{m} W_{i j} * P\left(a_{i} \mid a_{j}, c\right)
$$

where $P\left(a_{i} \mid a_{j}, c\right)$ and $W_{i j}$ both are redefined in our IWHNB approach. We redefine the probability $P\left(a_{i} \mid a_{j}, c\right)$ as Equation (17):

$$
P\left(a_{i}, a_{j} \mid c\right)=\frac{1+\sum_{t=1}^{n} w_{t} \delta\left(a_{t i}, a_{i}\right) \delta\left(a_{t j}, a_{j}\right) \delta\left(c_{t}, c\right)}{n_{i}+\sum_{t=1}^{n} w_{t} \delta\left(a_{t j}, a_{j}\right) \delta\left(c_{t}, c\right)}
$$

where $w_{t}$ is the weight of the $t$ th training instance.
Thirdly, $W_{i j}$ are weights which are measured by the conditional mutual information $I_{P}\left(A_{i} ; A_{j} \mid C\right)$ to reflect influences from other attributes. $W_{i j}$ is calculated as Equation (18):

$$
W_{i j}=\frac{I_{P}\left(A_{i} ; A_{j} \mid C\right)}{\sum_{j=1, j \neq i}^{m} I_{P}\left(A_{i} ; A_{j} \mid C\right)}
$$

where $I_{P}\left(A_{i} ; A_{j} \mid C\right)$ is defined as follows:

$$
I_{P}\left(A_{i} ; A_{j} \mid C\right)=\sum_{a_{i}, a_{j}, c} P\left(a_{i}, a_{j} \mid c\right) \log \frac{P\left(a_{i}, a_{j} \mid c\right)}{P\left(a_{i} \mid c\right) P\left(a_{j} \mid c\right)}
$$

In the process of computing $I_{P}\left(A_{i} ; A_{j} \mid C\right)$ and $W_{i j}$, we incorporate instance weights to compute probability estimates. We redefine the probabilities $P\left(a_{i}, a_{j} \mid c\right), P\left(a_{i} \mid c\right)$ and $P\left(a_{j} \mid c\right)$. The probability $P\left(a_{i} \mid a_{j}, c\right)$ is redefined as Equation (17). Meanwhile, $P\left(a_{i} \mid c\right)$ and $P\left(a_{j} \mid c\right)$ are respectively redefined as:

$$
\begin{aligned}
& P\left(a_{i} \mid c\right)=\frac{1+\sum_{t=1}^{n} w_{t} \delta\left(a_{t i}, a_{i}\right) \delta\left(c_{t}, c\right)}{n_{i}+\sum_{t=1}^{n} w_{t} \delta\left(c_{t}, c\right)} \\
& P\left(a_{j} \mid c\right)=\frac{1+\sum_{t=1}^{n} w_{t} \delta\left(a_{t j}, a_{j}\right) \delta\left(c_{t}, c\right)}{n_{j}+\sum_{t=1}^{n} w_{t} \delta\left(c_{t}, c\right)}
\end{aligned}
$$

Finally, the probability $P\left(a_{i} \mid a_{h p_{i}}, c\right)$ is computed by Equation (16). The test instance is classified by Equation (14). Instance weights are incorporated into the process of calculating probability estimates and the classification formula.

In our IWHNB approach, the improved HNB model is modified to reflect the influences of both attributes and instances. Different contributions for different instances are considered when generating the improved HNB model. Different influences of different instance weights are embedded to generate a hidden parent of each attribute. Now, the only question is how to quantify different instance weights. To address this question, the next subsection will describe how to quantify the weight of each instance.

# 3.2. The Weight of Each Instance 

In order to maintain the computational simplicity that characterizes HNB, we exploit eager learning, known as the attribute value frequency-based instance weighted filter, to calculate each single instance weight. The frequency of an attribute value means the ratio between the occurrence times of each attribute values and the instances' number. It can contain important information to define instance weights [18]. To quantify the frequency of an attribute value, $f_{t i}$ is used to denote the frequency of attribute value $a_{t i}$ (the $i$ th attribute value of the $t$ th instance). We define Equation (22) to denote the attribute value frequency:

$$
f_{t i}=\frac{\sum_{r=1}^{n} \delta\left(a_{r i}, a_{t i}\right)}{n}
$$

where $a_{r i}$ is the $i$ th attribute value of the $r$ th instance. For the $t$ th training instance, its attribute value frequency vector is denoted as $\left\langle f_{t 1}, f_{t 2}, \cdots, f_{t m}\right\rangle$. The more frequently an attribute value appears, the more influence of an attribute value there is on the instance. The frequency of the occurrence of attribute values can well reflect the importance of the instance.

In our IWHNB approach, not only the attribute value frequency but also the number of values of different attributes is considered. $\left\langle n_{1}, n_{2}, \cdots, n_{m}\right\rangle$ is used to denote values of each attribute's value number. It reflects the diversity of each attribute. Each instance weight has positive correlation with its attribute value frequency vector $\left\langle f_{t 1}, f_{t 2}, \cdots, f_{t m}\right\rangle$ and the attribute value number vector $\left\langle n_{1}, n_{2}, \cdots, n_{m}\right\rangle$.

Finally, we set the weight of each instance to be the dot product of the attribute value frequency vector and attribute value number vector. The weight of the $t$ th instance $w_{t}$ is formalized as the following Equation:

$$
\begin{aligned}
w_{t} & =\left\langle f_{t 1}, f_{t 2}, \cdots, f_{t m}\right\rangle \bullet\left\langle n_{1}, n_{2}, \cdots, n_{m}\right\rangle \\
& =\sum_{i=1}^{m}\left(f_{t i} * n_{i}\right)
\end{aligned}
$$

Based on the simple and efficient attribute value frequency-based instance weighted filter, a proper weight is assigned to each different instance. Discriminative instance weights are embedded to generate a hidden parent of each attribute to reflect the influences of both attributes and instances.

Now, the detailed learning algorithm for our instance weighted hidden naive Bayes (IWHNB for short) can be described as Algorithm 1. From Algorithm 1, the time complexity of computing instance weights is $O(3 n m) . n$ is the number of training instances. $m$ is the number of attributes. IWHNB needs to compute the conditional mutual information for each pair of attributes. The time complexity is $O\left(q m^{2} v^{2}\right), v$ is the average number of values for an attribute, $q$ is the number of class labels. The time complexity for computing each weight $W_{i j}$ is $O\left(m^{2}\right)$. These formulas sum over $n$, thus, the training time complexity of IWHNB is $O\left(3 n m+n m^{2}+n q m^{2} v^{2}\right)$. The training procedure of the algorithm IWHNB is similar to that of HNB, except the additional procedure for calculating each instance weight. At classification time, Equation (14) is used to classify a test instance, and it takes $O\left(q n^{2}\right)$. The total time complexity of the IWHNB algorithm is $O\left(q n^{2}+3 n m+n m^{2}+n q m^{2} v^{2}\right)$, which shows that IWHNB is simple and efficient.

```
Algorithm 1 Instance Weighted Hidden Naive Bayes
Input: \(T D\)-a training dataset; a test instance \(x\)
Output: the predicted class label of \(x\)
    Initialize all instance weights by the attribute value frequency-based instance weighted
    filter
    for each training instance \(t=1\) to \(n\) do
        for each training instance's attribute value, \(i=1\) to \(m\) do
            Set new instance weight of \(t\) th instance to be the dot product of its attribute
            value frequency vector \(<f_{t 1}, f_{t 2}, \cdots, f_{t m}>\) and the attribute value number vector
            \(<n_{1}, n_{2}, \cdots, n_{m}>\)
        end for
    end for
    Discriminative instance weights are incorporated into the process of calculating proba-
    bility estimates.
    for each possible class label \(c\) that \(C\) takes do
        Calculate \(P(c)\) using Equation (15)
        for each attribute \(A_{i}, i=1\) to \(m\) do
            Calculate \(P\left(a_{i} \mid c\right)\) using Equation (20)
        end for
        for each pair of attributes \(A_{i}\) and \(A_{j}(i \neq j)\) do
            Calculate \(P\left(a_{i} \mid a_{j}, c\right)\) as Equation (17)
            Calculate \(I_{P}\left(A_{i} ; A_{j} \mid C\right)\) using Equation (19)
            Calculate \(W_{i j}\) using Equation (18)
        end for
        Calculate \(P\left(a_{i} \mid a_{h p_{i}}, c\right)\) using Equation (16)
    end for
    Predict the class label \(c(x)\) of \(x\) by Equation (14)
```


# 4. Experiments and Results 

In order to verify the performance of our proposed IWHNB, we completed experiments to compare IWHNB with NB, HNB and other state-of-the-art competitors. These state-of-the-art competitors and their abbreviations are listed as follows. HNB, AODE and TAN are state-of-the-art structure extension approaches. AVFWNB is an eager instance weighting approach. AIWNB is a new improved approach which combines instance weighting with attribute weighting.

- NB: Naive Bayes [36].
- HNB: Hidden naive Bayes [33].
- AVFWNB: Attribute value frequency weighted NB [18].
- AIWNB: Attribute and instance weighted NB [35].
- AODE: Aggregating one-dependence estimators [12].
- TAN: Tree-augmented NB [14].

We performed our study on the 36 University of California, Irvine (UCI) datasets [37]. These datasets are published on the WEKA platform [38]. They are from a wide range of fields and also have various data characteristics. In the process of preprocessing, we replace missing attribute values with the modes of the nominal attribute values or the means of the numerical attribute values. We also use the Fayyad \& Irani's minimum description length (MDL) method [39] to discretize numerical attribute values. If the attribute's value number is the same instances' number, the attribute is redundant. So, we delete this type of attribute. There are three redundant attributes deleted: "Hospital Number" in the dataset "colic.ORIG", "instance name" in the dataset "splice", and "animal" in the dataset "zoo".

Table 1 shows the results of a comparison of the classification accuracy of each approach on each dataset after averaging the classification accuracies from ten runs of 10 -fold cross-validation, respectively. Meanwhile, two-tailed $t$-test with the $p=0.05$ significance level $[40,41]$ is used to compare the proposed IWHNB with its competitors. We use the

symbol $\cdot$ to denote our proposed IWHNB is a significant improvement over its competitors, and use the symbol $\circ$ to denote it is a significant degradation over its competitors. The second-to-last line reveals the average accuracy of each algorithm, which can provide a gross indicator of its classification performance across all datasets. At the bottom of the Table 1, W/T/L reflects that our proposed IWHNB wins on $W$ datasets, ties on $T$ datasets and loses on $L$ datasets over its competitors.

Then, the summary test results based on a corrected paired two-tailed $t$-test with the $p=0.05$ significance level are shown in Table 2. For each entry $i(j), i$ is the number of datasets on which the algorithm in the column achieves higher classification accuracy than the algorithm in the corresponding row, and $j$ is the number of datasets on which the algorithm in the column achieves significant wins with the $p=0.05$ significance level with regard to the algorithm in the corresponding row. The ranking results are summarized in Table 3. The first column is the difference between the total number of wins and the total number of losses that the corresponding algorithm achieves compared with all the other algorithms, which is used to generate the ranking. The second column is the total number of winning datasets. The third column is the total number of losing datasets.

Table 1. Comparisons of the classification accuracy for IWHNB versus NB, HNB, AVFWNB, AIWNB, AODE and TAN.


Table 2. Summary test results on classification accuracy.


Table 3. Ranking test results on classification accuracy.


Based on comparison results, the conclusion is evident that our IWHNB approach obtains the best experimental results compared with its competitors. We summarize the conclusions briefly as follows:

1. According to results in Table 1, the averaged classification accuracy of IWHNB across all datasets is $86.37 \%$. It is considerably higher than its competitors, such as NB ( $83.31 \%$ ), HNB ( $85.86 \%$ ), AVFWNB ( $84.21 \%$ ), AIWNB ( $84.94 \%$ ), AODE ( $85.68 \%$ ) and TAN $(84.95 \%)$. This suggests that our proposed IWHNB approach is effective.
2. IWHNB obtains the most satisfactory experimental results in accuracy. IWHNB outperforms NB ( 17 wins, 18 ties and 1 loss), HNB ( 9 wins, 27 ties and 0 losses), AVFWNB ( 13 wins, 21 ties and 2 losses), AIWNB ( 8 wins, 25 ties and 3 losses), AODE ( 6 wins, 30 ties and 0 losses) and TAN ( 9 wins, 25 ties and 2 losses).
3. The summary and ranking test results show that IWHNB is overall the best across all datasets ( 62 wins and 8 losses). The descending sort across all datasets is IWHNB, HNB, AIWNB, AODE, TAN, AVFWNB and NB.
4. Compared with HNB, IWHNB considerably improves the classification accuracy (nine wins and zero losses). This suggests that this improved hybrid approach which combines the improved HNB model with instance weighting improves the classification performance effectively.
Furthermore, we observe the performance of IWHNB in terms of the elapsed training time (in milliseconds). Our experiments were conducted on a Linux machine with 3.2 GHz processor and 8 GB of RAM. The elapsed training time comparison results are shown in Tables 4-6. Note that the meanings of the t-test results in these tables are opposite to those in Tables 1-3. For the elapsed training time, a small number which indicates lower time complexity is better than a large number. Thus, in Table 4, the symbols $\circ$ and $\bullet$ denote statistically significant improvement or degradation over its competitors, respectively. Each W/T /L implies that compared to its competitors, our proposed IWHNB wins on W datasets, ties on T datasets, and loses on L datasets. In Table 5, $i$ of value $i(j)$ denotes the number of datasets that the algorithm corresponding to the column loses compared to the algorithm corresponding to the row. In Table 6, the second and third columns represent the total numbers of losses and wins, respectively. The first column is the difference between the second column of losses and third column of wins. We summarize the main highlights of these comparisons as follows:

1. According to results in Table 4, the averaged elapsed training time of IWHNB is 13.15 milliseconds, which is a little bigger than that of HNB ( 12.56 milliseconds). Therefore, our proposed IWHNB approach maintains the computational simplicity that characterizes HNB. It is a simple, efficient and effective approach.
2. Compared with TAN, IWHNB has the lower time complexity. The averaged elapsed training time of IWHNB is smaller than that of TAN ( 15.84 milliseconds). It reduces the elapsed training time on 8 datasets, and loses on 0 datasets.
3. According to Tables 4-6, IWHNB indeed has higher time complexity than NB, AVFWNB, AIWNB, AODE, HNB, but it still has low computational simplicity. Structure extension and instance weighting are both completed in our IWHNB approach.

Table 4. Comparisons of the elapsed training time for IWHNB versus NB, HNB, AVFWNB, AIWNB, AODE and TAN.


Table 5. Summary test results on elapsed training time.


Table 6. Ranking test results on elapsed training time.


# 5. Conclusions and Future Work 

Hidden naive Bayes (HNB) adds a hidden parent to each attribute to encode attribute dependencies. However, it regards each instance as equally important. In this paper, we propose an improved hybrid approach which combines the improved NB model with instance weighting into one hybrid model, called instance weighted hidden naive Bayes (IWHNB). In our IWHNB approach, different contributions for different instances are considered when generating the improved HNB model. Experiments are conducted to compare IWHNB with NB, HNB and other state-of-the-art competitors in terms of the classification accuracy and the elapsed training time. The classification accuracy comparison results show that our IWHNB approach obtains the best experimental results compared with its competitors. The elapsed training time comparison results show that IWHNB maintains the computational simplicity that characterizes HNB. IWHNB is a simple, efficient and effective approach.

How to calculate optimal instance weights to overcome the unrealistic assumption is crucial. We think that more sophisticated algorithms can be used to learn more optimal instance weights to optimize our current version.

Author Contributions: Conceptualization, L.Y. and S.G.; methodology, L.Y. and S.G.; software, L.Y., Y.C., D.L. and S.G.; validation, L.Y. and S.G.; formal analysis, L.Y., Y.C., D.L. and S.G.; investigation, L.Y., Y.C., D.L. and S.G.; resources, L.Y. and S.G.; data curation, L.Y. and S.G.; writing-original draft preparation, L.Y. and S.G.; writing-review and editing, L.Y. and D.L.; visualization, L.Y. and S.G.; supervision, S.G.; project administration, L.Y. and S.G.; funding acquisition, L.Y. and S.G. All authors have read and agreed to the published version of the manuscript.

Funding: The work was partially supported by Science and Technology Project of Hubei ProvinceUnveiling System (2019AEE020), Open Research Project of The Hubei Key Laboratory of Intelligent Geo-Information Processing (KLIGIP-2018A05), Scientific Research Foundation for Talent introduction (20RC07), Teaching Research Project of Hubei University of Education (X2019009).

Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Not applicable.
Conflicts of Interest: The authors declare no conflict of interest.

## Abbreviations

The following abbreviations are used in this manuscript:


