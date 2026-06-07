# Article 

## Integrating Dynamic Bayesian Networks and Analytic Hierarchy Process for Time-Dependent Multi-Criteria Decision-Making

Chin-Yi Chen ${ }^{1}$ and Jih-Jeng Huang ${ }^{2, * *}$


#### Abstract

check for updates Citation: Chen, C.-Y.; Huang, J.-J. Integrating Dynamic Bayesian Networks and Analytic Hierarchy Process for Time-Dependent Multi-Criteria Decision-Making. Mathematics 2023, 11, 2362. https:// doi.org/10.3390/math11102362

Academic Editor: Óscar Valero Sierra


Received: 22 March 2023
Revised: 10 May 2023
Accepted: 15 May 2023
Published: 19 May 2023

## (0)

Copyright: (c) 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 Department of Business Administration, Chung Yuan Christian University, No. 200, Zhongbei Rd, Zhongli District, Taoyuan City 320, Taiwan
2 Department of Computer Science \& Information Management, Soochow University, No. 56, Section 1, Kueiyang Street, Chungcheng District, Taipei City 100, Taiwan

* Correspondence: jjhuang@scu.edu.tw


#### Abstract

The analytic hierarchy process (AHP) has been a widely used method for handling multicriteria decision-making (MCDM) problems since the 1980s. However, it postulates that criteria are independent and static, which may not always hold true in realistic situations. Although several methods have been proposed to relax the assumption of independence between criteria in the AHP, such as the analytic network process (ANP), these methods do not account for time-dependent criteria in the AHP. Consequently, this paper presents an innovative method that integrates dynamic Bayesian networks (DBNs) with the AHP to model dynamic interdependencies between criteria in MCDM problems. We illustrate the proposed method through a comprehensive numerical example and compare the result with the conventional AHP. The findings suggest that the proposed method extends the AHP to accommodate time-dependent issues and, when ignoring specific information, reduces to the conventional AHP, thereby demonstrating that our approach serves as a more general AHP model.


Keywords: analytic hierarchy process (AHP); dynamic Bayesian networks (DBNs); multi-criteria decision-making (MCDM); time-dependent criteria

MSC: 90B50

## 1. Introduction

Decision-making can be complex, often involving the assessment of multiple factors and their interconnections. Numerous methods in academic literature address multicriteria decision-making (MCDM) problems, one of which is the analytic hierarchy process (AHP) [1]. AHP has gained popularity across various fields due to its straightforward nature and ability to decompose intricate decision problems into hierarchical structures [2]. However, AHP assumes that criteria are independent, which may not hold true in many real-world situations.

To tackle the independence assumption in AHP, researchers have developed several techniques to incorporate dependencies between criteria, such as employing the analytic network process (ANP) [3] or combining AHP with methods such as fuzzy cognitive maps (FCMs) [4] and Bayesian networks (BNs) [5]. While these approaches provide valuable insights, they frequently neglect the evolving nature of dependencies between criteria over time. Dynamic Bayesian networks (DBNs) extend BNs by modeling dependencies between variables across time [6]. DBNs have been effectively applied in various domains, including finance [7] and environmental modeling [8]. To our knowledge, no studies have explored the integration of DBNs and AHP to model time dependencies between criteria in MCDM problems and, hence, are considered here to account for the time-dependent criteria in the AHP.

This paper introduces an innovative method that combines DBNs and AHP to model dynamic dependencies between criteria in multi-criteria decision-making problems. First, we use AHP to derive independent weights for criteria. Then, we establish the dependencies between criteria and derive the DBN parameters. Next, considering time dependency, we combine the initial weights and DBN parameters to update the criteria weights. Finally, we use the revised weights to rank alternatives and make decisions. Our contributions are as follows. The major novelty of the proposed method is to provide extra information for the AHP and adjust the weights derived from the AHP to account for this information. Compared to the data of the AHP or ANP, which are quantified from expert opinions, the time-dependent relationship between criteria can be derived either from expert opinion or historical data. In addition, the concept presented here can be naturally extended to the ANP for handling interdependent and time-varying criteria since the information considered here is distinct from PCMs used in the AHP/ANP. The fact that past papers have not addressed this issue also contributes to the novelty of the paper. We use the AHP as our base model here because it is a well-established and extensively utilized technique for MCDM. In addition, our method can easily be applied in others, besides the AHP/ANP, since the information considered here is distinct from conventional MCDM methods. Its application spans a multitude of domains, and both academics and practitioners have embraced it. This broad acceptance and popularity serve as a solid basis for our suggested method.

The paper's organization is as follows: Section 2 delves into the literature on AHP and DBNs; Section 3 elaborates on our proposed method for amalgamating DBNs and AHP; Section 4 showcases a numerical example illustrating the implementation of our approach; Section 5 juxtaposes our method with established approaches; and lastly, Section 6 concludes the paper and explores potential avenues for future research.

# 2. Literature Review 

This section gives the literature review about the AHP and DBN as follows.

### 2.1. AHP

AHP has been a popular MCDM method since its introduction by [1]. It effectively addresses complex decision problems by organizing them hierarchically, considering criteria and alternatives at separate levels. AHP has found widespread applications in various fields, such as project management [9], resource allocation [10], and environmental management [11]. The fundamental aspect of AHP is pairwise comparison, which enables decision-makers to express their preferences for criteria and alternatives by evaluating them in pairs [12]. Pairwise comparison matrices (PCMs) are constructed to assess the relative importance of criteria and the performance of alternatives concerning each criterion. The judgments provided by the decision-makers are typically represented using a numerical scale, such as Saaty's [1] 9-point scale, to indicate from equal importance to extreme importance. These matrices are then used to derive local weights, which are subsequently synthesized to obtain global weights for the alternatives [13]. The alternative with the highest global weight is considered the best option.

The mathematical process of the AHP can be considered as solving the eigenvalue problem as [1]:

$$
\boldsymbol{A} \boldsymbol{w}=\lambda_{\max } \boldsymbol{w}
$$

where $\boldsymbol{A}=\left[a_{i j}\right]_{a \times n}$ is the pairwise comparison matrix (PCM), $\lambda_{\max }$ is the largest eigenvalue, and $\boldsymbol{w}$ denotes the weight vector. Then, we can use the consistency index (CI) and the consistency ratio (CR) to check if the consistency condition is satisfied.

AHP has been praised for its simplicity and ability to capture qualitative and quantitative criteria in decision-making [2]. It provides a structured approach for breaking down complex decision problems into smaller, manageable components. Moreover, AHP allows for incorporating expert opinions and handling incomplete or imprecise information by using fuzzy numbers [14] or interval judgments [15].

Despite its numerous advantages, AHP assumes that the criteria are independent, which may not always hold in real-world situations. In many cases, criteria are interdependent, which means that changes in one criterion can influence the others. Ignoring these dependencies can lead to inaccurate or suboptimal decisions. Several methods have been developed to address this issue, such as the ANP [3], which extends AHP to model complex relationships between criteria and alternatives in a network structure.

Another approach to addressing the independence assumption in AHP is to integrate it with other techniques that can capture dependencies between criteria, such as FCMs [4] and BNs [5]. FCMs are a knowledge representation tool that can model causal relationships between concepts, while BNs are probabilistic graphical models that represent the joint probability distribution of a set of random variables. In addition, Grey relational analysis (GRA) has been integrated with AHP to model dependencies between criteria in MCDM problems [16].

However, these approaches often do not account for the dynamic nature of dependencies between criteria over time. Real-world decision problems often involve changing relationships between criteria due to external factors or the evolving nature of the problem itself. For example, in environmental management, the relationships between different ecological criteria may change over time due to climate change, human interventions, or other factors. As proposed in this paper, the integration of DBNs with AHP seeks to address this limitation by capturing time-dependent relationships between criteria and allowing for more accurate and informed decision-making in complex, dynamic environments.

# 2.2. DBNs 

DBNs serve as an expansion of BNs by modeling variable dependencies over time [6]. As graphical models, BNs illustrate probabilistic connections among a set of variables, enabling reasoning in uncertain situations [8]. Applications of DBNs span various domains, such as finance [7], environmental modeling [17], and robotics [18]. DBNs can be perceived as an amalgamation of multiple BNs, each encapsulating a momentary snapshot of the system at a distinct time step [19]. The DBN structure consists of two layers: the initial layer represents the variables' starting state, while the second layer portrays the variables at the subsequent time step. Directed edges linking the two layers signify dependencies between variables across different time steps, and edges within each layer exhibit dependencies among variables at identical time steps [6].

The DBN's mathematical model can be expressed as follows. A DBN represents a stochastic process, where each random variable is indexed by a discrete time step $t=1,2$, $\ldots, T$. Let $X(t)=\left\{x_{1 t}, x_{2 t}, \ldots, x_{n t},\right\}$ be a set of $n$ random variables at time step $t$. A DBN is a directed acyclic graph (DAG) $G=(V, E)$, where $V$ is a set of nodes representing the random variables, and $E$ is a set of directed edges representing the conditional dependencies between the random variables.

A DBN can be characterized by a set of conditional probability distributions (CPDs) $P\left(X_{t}^{i} \mid P a\left(X_{t}^{i}\right)\right)$, where $P a\left(X_{t}^{i}\right)$ denotes the parents of $X_{t}^{i}$ in the graph. The joint probability distribution over all random variables in a DBN can be factorized as:

$$
P\left(X_{1: T}\right)=\prod_{t=1}^{T} \prod_{i=1}^{n} P\left(X_{t}^{i} \mid P a\left(X_{t}^{i}\right)\right)
$$

where $X_{1: T}$ represents the set of random variables from time step 1 to $T$.
DBNs often assume a first-order Markov property, which means that the value of a random variable at a given time step depends only on the values of the random variables in the previous time step:

$$
P\left(X_{t}^{i} \mid X_{1: t-1}\right)=P\left(X_{t}^{i} \mid X_{t-1}\right)
$$

This property allows for a compact representation of the DBN using a two-slice temporal Bayesian network (2TBN). A 2TBN consists of two consecutive time slices, $t$ and $t+1$, representing the dependencies between the random variables at these time slices. The 2TBN

can be used to represent the transition model of the DBN, which describes how the random variables evolve over time:

$$
P\left(X_{t+1} \mid X_{t}\right)=\prod_{i=1}^{n} P\left(X_{t+1}^{i} \mid P a\left(X_{t+1}^{i}\right) \cap X_{t}\right)
$$

where $P a\left(X_{t+1}^{i}\right) \cap X_{t}$ denotes the parents of $X_{t+1}^{i}$ that are in the previous time slice $t$.
Inference in DBNs typically involves computing the posterior distribution of a set of random variables at a specific time step, given the observed evidence $P\left(X_{t} \mid E_{1: T}\right)$, where $E_{1: T}$ represents the observed evidence from time step 1 to $T$. Numerous algorithms exist for performing inference in dynamic Bayesian networks (DBNs), including the forwardbackward algorithm (also known as the Baum-Welch algorithm [20]) for Hidden Markov models (HMMs) [21], the Kalman filter for linear Gaussian models, and the more general particle-filtering algorithm for non-linear, non-Gaussian models. DBNs encode transition probabilities between states by considering conditional probability distributions for each variable, based on their parent variables within the network. These probabilities can be derived from data, expert knowledge, or a mix of both. DBNs have been effectively applied across diverse fields, such as time-series-data modeling and prediction [19], portfolio management [20], and climate modeling [21].

Though DBNs haven't been extensively utilized in the MADM arena, they hold promise in addressing certain limitations of existing techniques, such as the static nature of dependencies between criteria in AHP. For instance, DBNs can be employed to model time-dependent dependencies among various criteria in supply chain management, such as demand, lead times, and supplier reliability. Likewise, DBNs can be leveraged to model the dynamic relationships among different criteria in project management, such as cost, time, and quality, facilitating improved decision-making under uncertainty.

# 3. Integrating DBNs and AHP: Proposed Method 

In this section, we outline our suggested approach for combining DBNs and AHP. The integration seeks to overcome the independence assumption constraint in AHP by including time-dependent dependencies between criteria through the use of DBNs. By fusing DBNs, which are capable of modeling criteria dependencies over time, with AHP, which concentrates on deriving weights for hierarchical decision-making, we enable the computation of timedependent weights that consider the interdependencies among criteria.

The proposed method comprises the following steps:
Step 1. Problem structuring: define the decision problem and identify the relevant criteria and alternatives. Decision problems are considered hierarchical structures, with the goal at the top, followed by criteria and sub-criteria (if applicable), and alternatives at the bottom.

Step 2. Pairwise comparison and initial weight calculation: conduct pairwise comparisons of criteria using the AHP scale (1-9) based on expert opinion. Construct pairwise comparison matrices for each criterion at the same hierarchical level and calculate the initial weights of the criteria using the eigenvector method, i.e., Equation (1).

Step 3. Designing the DBN: identify criteria with time dependencies and define the time steps for the DBN based on the decision problem's temporal characteristics. For example, create a two-layered DBN structure, i.e., two time steps, with the first layer representing the initial state of the criteria and the second layer representing the criteria at the next time step. Represent dependencies between criteria with directed edges within and between layers, as shown in Figure 1.

![img-0.jpeg](img-0.jpeg)

Figure 1. Time dependencies between criteria.
Based on Figure 1, we need to acquire information of each transition matrix, e.g., $P\left(C_{t+1}^{1} \mid C_{t}^{1}\right), P\left(C_{t+1}^{n} \mid C_{t}^{1}\right)$, etc.

Step 4. Learning DBN parameters: here, we assume the transition probabilities between statuses are given by experts, but we will consider historical data to derive the transition probabilities between statuses in our numerical example. Take $P\left(C_{t+1}^{1} \mid C_{t}^{2}\right)$, for example; we need experts to give the option to fill up the below transition matrix:


Indeed, we can use linguistic variables to help experts to give their opinion above. For example, we can give the scores for linguistic probability: high, medium, and low as 3, 2, and 1, respectively. Then, we normalize the linguistic score matrix to a probability matrix.

Step 5. Inference in DBN: perform inference in the DBN to obtain the probability distribution of each criterion, taking into account the dependencies between criteria and their evolution over time. The marginal steady-state distribution of each criterion can be derived using the Markov chain theory. However, the joint steady-state distribution for a criterion can be determined by the marginal steady-state distribution as follows. The Markov chain theory derives from the marginal distributions of two criteria with two statuses, namely, $C 1=\left[p_{11}, p_{12}\right]$ and $C 2=\left[p_{21}, p_{22}\right]$. Then, we can calculate the joint probability of $C 1$ and $C 2, P(C 1, C 2)$, as:


Assume $C 3$ also has two statuses, and $C 3(t+1)$ is affected by $C 1(t)$ and $C 2(t)$, then the marginal probability of $C 3$ for the $i$ th status can be calculated by the joint probability of $C 1$ and $C 2$ as:

$$
P(C 3=\operatorname{status}(i))=\sum P(C 1, C 2) \times P(C 3=\operatorname{status}(i) \mid C 1, C 2), \forall i
$$

Step 6. Synthesis of time-dependent weights: combine the initial weights obtained from the AHP (Step 2) with the time-dependent weights from the DBN (Step 5) to calculate adjusted weights for each criterion. Synthesize the modified weights to rank alternatives, considering the time dependencies between criteria.

Let the marginal distributions of criteria, e.g., C1-C3 here, be presented as shown in Table 1.

Table 1. Marginal distributions for criteria and the relative advantages.


The relative advantage (RA) of different statuses indicates the relative importance of criteria under the same status. Next, we can derive the total relative advantage scores (RS) of criteria as the base to adjust the initial weights of criteria. Here, we use the weighted average method to calculate the total relative advantage scores of criteria for simplicity.

Finally, the modified weights of the criteria can be calculated as follows:

$$
w_{m}^{i}=\frac{w_{j} \times R S_{j}}{\sum_{i} w_{i} \times R S_{i}}, \forall j
$$

By incorporating time dependencies between criteria, the proposed method for integrating DBNs and AHP offers a comprehensive framework to address the limitations of the independence assumption in AHP. This approach enables more accurate and informed decision-making in complex, dynamic environments where criteria dependencies change over time.

# 4. Numerical Example 

In this section, we present a numerical example to demonstrate the application of the proposed method for integrating DBNs and the AHP. The decision problem involves selecting the best location for a new warehouse among five alternatives (A1, A2, A3, A4, and A5) based on eight criteria (C1 to C8). The criteria are as follows. C1: proximity to customers; C2: proximity to suppliers; C3: infrastructure quality; C4: labor availability; C5: real-estate costs; C6: regulatory environment; C7: environmental impact; and C8: local economic conditions. We will now apply the proposed method to this decision problem, explaining each step in detail.

Step 1: Problem structuring
The decision problem is structured hierarchically using AHP, with the goal at the top (selecting the best warehouse location), followed by the eight criteria (C1 to C8), and the five alternatives (A1 to A5) at the bottom, as shown in Figure 2.
![img-1.jpeg](img-1.jpeg)

Figure 2. The hierarchical structure of the problem.
The problem above indicates criteria and alternatives are independent. Here, we focus on handling the time dependence between criteria.

Step 2: Pairwise comparison and local weight calculation

Let an expert perform pairwise comparisons of the criteria using the AHP scale (1-9) using the following PCM information:


Note that $\lambda=8.050 ; \mathrm{CI}=0.007 ; \mathrm{CR}=0.005$.
We can use the eigenvector method to calculate the local weights of the criteria from the AHP. Then, the initial weights will be adjusted and updated based on the information on the time dependence between criteria.

Step 3: Designing the DBN
Next, we need to identify the relationship between criteria with time-dependent dependencies based on expert opinion. In this example, we assume that $C 1, C 2$, and $C 8$ exhibit time-dependent dependencies for simplicity. Hence, the weights of $C 3-C 7$ are static and will not be changed further. We then define the time steps for the DBN (e.g., monthly) and create a two-layered DBN structure. The structure represents two consecutive time steps, with the initial state of the criteria in the first layer and their state at the next time step in the second layer. The dependencies between criteria are represented by directed edges within and between layers, as shown in Figure 3:
![img-2.jpeg](img-2.jpeg)

Figure 3. Dependencies between criteria.
In this structure, expert opinion indicates that $C 1$ and $C 2$ at time $t$ influence themselves at time $t+1$, and $C 1$ and $C 2$ at time $t$ also influence $C 8$ at the $t+1$ time step.

Step 4: Learning DBN parameters
Assume we use expert opinion to estimate each criterion's transition probabilities between states. The experts provide the following conditional probability tables for $C 1, C 2$, and $C 8$. Note that in the given context below, low (L), medium (M), and high (H) refer to each criterion's different states or levels. These levels represent the degree to which the criterion is satisfied or its intensity in the decision-making process. For instance, for C1 (proximity to customers), a low level would imply that the warehouse location is relatively far from the customers.

In this example, we used expert opinion to estimate the transition probabilities for the time-dependent criteria in the DBN. These probabilities describe the dynamics of the criteria over time and their influence on other criteria in the network. Assume we have the following historical series for C1: (L, L, L, M, L, L, L, M, M, L, H, M, M, H, H, H, H, H, M, H, H, M, M, M, L, M, L, L, M, L, L, L, L, L, M, M, M, H, M, H, H, H, H, M, H, H, H, M, L, L, L, L, L, L, M, H, H, H, M, H, M), we can calculate the transition probabilities for C 1 as:

$$
P\left(C_{t+1}^{1} \mid C_{t}^{1}\right):
$$


For example, $P\left(C_{t+1}^{1}=\operatorname{Low} \mid C_{t}^{1}=\operatorname{Low}\right)=19 / 28 \approx 0.7$. We can use the historical data to complete the transition matrix above.

Let us assume we calculate the historical data to obtain the following transition matrices:

$$
P\left(C_{t+1}^{2} \mid C_{t}^{2}\right):
$$


$P\left(C_{t+1}^{8} \mid C_{t}^{1}, C_{t}^{2}\right):$


Step 5: Updating the criteria weights using the DBN
Using the learned DBN parameters, we compute the updated weights for criteria $C 1, C 2$, and $C 8$, considering their dependencies. For simplicity, let us assume the state probabilities for $C 1, C 2$, and $C 8$ provided by an expert as shown in Table 2:

Table 2. The state probabilities for criteria.


Then, we can use the steady-state distributions of $C 1$ and $C 2$ to calculate the joint probability of $C 1$ and $C 2$ as:


The joint probability matrix, $P(C 1, C 2)$, can then be used to derive the marginal probability distribution of $C 8$ as:

$$
\begin{aligned}
P(C 8=\text { Low }) & =\sum P(C 1, C 2) \times P(C 8=\text { Low } \mid C 1, C 2) \\
& =P(C 1=L, C 2=L) \times P(C 8=L \mid C 1=L, C 2=L)+ \\
P(C 1=L, & C 2=M) \times P(C 8=L \mid C 1=L, C 2=M)+\ldots+ \\
P(C 1=H, & C 2=H) \times P(C 8=\text { Low } \mid C 1=H, C 2=H) \\
& =0.2 \times 0.7+0.12 \times 0.4+\ldots+0.04 \times 0.6=0.568 \\
P(C 8=\text { Medium }) & =\sum P(C 1, C 2) \times P(C 8=\text { Medium } \mid C 1, C 2)=0.296 \\
P(C 8=\text { High }) & =\sum P(C 1, C 2) \times P(C 8=\text { High } \mid C 1, C 2)=0.136
\end{aligned}
$$

After calculating the steady-state distribution of $C 8$, we can derive the marginal probabilities for criteria, as shown in Table 3.

Table 3. The steady-state distributions for the criteria.


Next, we can calculate the RA and RS of the criteria, as shown in Table 4.
Table 4. The relative advantages for different status.


Finally, we can derive the modified weights of the criteria as follows:

$$
\begin{aligned}
w_{m}^{1} & =\frac{(0.25 \times 0.366)}{0.172} \times(0.25+0.15+0.10)=0.266 \\
w_{m}^{2} & =\frac{(0.15 \times 0.344)}{0.172} \times(0.25+0.15+0.10)=0.150 \\
w_{m}^{3} & =\frac{(0.10 \times 0.290)}{0.172} \times(0.25+0.15+0.10)=0.084
\end{aligned}
$$

Note that we adjust the second term of the modified weights formula to ensure that the sum weights of $C 1, C 2$, and $C 8$ after DBN should be the same as the original sum weights of $C 1, C 2$, and $C 8$.

Step 6: Ranking the alternatives
We now have the updated weights for all criteria, including the time-dependent criteria. The following performance matrix for the alternatives with respect to the criteria and the weighted sum for each alternative using the updated criteria weights can also be given as shown in Table 5:

Table 5. The performance matrix and the total scores of the alternatives.


Rank of the proposed method: (A3, A4, A1, A5, A2)
Rank of the AHP method: (A1-A3-A4, A5, A2)

The proposed method's final rank shows the scores of A1, A3, and A4. Compared with the conventional AHP, the proposed method can account for extra information on time dependencies between criteria and modify the initial weight based on the information. The proposed method also reduces to the conventional AHP by ignoring the time-dependency information between criteria.

# 5. Discussions 

Interdependency between criteria has been an important issue in MCDM. For example, ref. [22] presented a hybrid modified TOPSIS integrated with preemptive goal programming to address interdependencies in the supplier selection process, a multiple-criteria decision-making issue. By comparing the proposed methodology to the analytical hierarchy process (AHP), the results show improved total value of purchasing while maintaining the equal total cost of purchasing, emphasizing the importance of considering interdependencies in supplier selection. Ref. [23] proposed a non-orthogonal coordinate system-based multi-criteria decision-making method to address interdependent criteria in sustainability assessments. The method was applied to an electricity production case study, comparing results with traditional methods and conducting sensitivity analysis. Ref. [24] presented a non-orthogonal coordinate system-based multi-criteria decision-making method that accounts for the interactions and interdependencies among the criteria in sustainability assessments. This approach offers a more comprehensive framework for prioritizing industrial systems, as it incorporates the complex relationships between evaluation criteria and sustainability-oriented decision-makers.

In this numerical example, we have showcased the practical application of our proposed method for combining DBNs and the AHP. This comprehensive framework addresses the limitations of the independence assumption in the AHP by integrating time dependencies between criteria using DBNs. It enables more accurate and informed decisionmaking in complex, dynamic environments where criteria dependencies evolve over timesomething that previous AHP-related papers have not been able to address.

In this section, we compare our proposed method with existing approaches in the literature, focusing on the differences and advantages our method brings to the decisionmaking process. Conventional AHP and Fuzzy AHP [1], ref. [25] are widely used techniques for multi-criteria decision-making. However, both methods assume criteria independence, which may not always hold true in real-life scenarios. Some studies, such as [26], have combined AHP with BNs to model dependencies among criteria. In addition, ref. [27] presented a method for quantitative risk assessment of gas explosions in underground coal mines using BNs and FAHP. The proposed approach combines subjective and objective expert information for fuzzification, calculates real-time probabilities of potential risk events and risk factors, and determines the most critical risk factors through sensitivity analysis. Although this approach can capture static dependencies, it lacks the ability to model time-varying relationships.

In conclusion, our proposed method for integrating DBNs and AHP addresses some limitations found in existing approaches, particularly in modeling time-varying dependencies among criteria. By incorporating DBNs, our approach can capture complex and evolving relationships in multi-criteria decision-making problems, offering a more accurate and robust tool for decision-makers across various domains. Note that in this paper, we only consider two-layer DBNs, and the concept can be extended to consider more layers to handle more complicated time-dependent criteria in practice. In addition, the availability of transition matrices is still the major limitation of the proposed method.

## 6. Conclusions

This paper proposes a novel method for integrating DBNs and the AHP to address time-varying dependencies among criteria in multi-criteria decision-making problems. Our approach combines the strengths of AHP in deriving criteria weights and DBNs in modeling complex and evolving relationships among criteria. We provided a detailed numerical example to illustrate the application of our method in a practical decision-making scenario, demonstrating its usefulness in the presence of changes in criteria weights. The finding of the numerical example indicates the initial weights have been modified by accounting for time dependencies between criteria to result in different rankings compared to the conventional AHP.

Our approach addresses some limitations found in existing methods, such as assuming criteria independence or only capturing static dependencies. By incorporating DBNs, our method can model both direct and indirect relationships and temporal dynamics, providing a more accurate and flexible tool for decision-makers across various domains. For further research, our proposed method could be extended to integrate DBNs with other multicriteria decision-making methods, such as the ANP, to further enhance the ability to capture time dependencies among interdependent criteria in various decision-making problems.

The limitation of the proposed paper can be described as follows. The information of the state probabilities between criteria plays the critical role in this paper and historical data may not be available to calculate the information. However, experts may not have the ability to quantify the information. In addition, the DBN structure and transition probabilities are fixed over time in our current method. However, in some real-world problems, the relationships among criteria may change dynamically. Future research could investigate the development of adaptive DBNs that can learn and update their structure and probabilities as new data or expert opinions become available.

Author Contributions: Conceptualization, C.-Y.C. and J.-J.H.; methodology, J.-J.H.; writing—original draft preparation, C.-Y.C.; writing—review and editing, J.-J.H. All authors have read and agreed to the published version of the manuscript.
Funding: This research received no external funding.
Data Availability Statement: All used data are presented in the paper.
Conflicts of Interest: The authors declare no conflict of interest.
