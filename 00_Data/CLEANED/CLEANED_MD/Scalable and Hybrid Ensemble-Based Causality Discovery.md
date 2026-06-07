© 2020 IEEE. Personal use of this material is permitted. Permission from IEEE must be obtained for all other uses, in any current or future media, including reprinting/republishing this material for advertising or promotional purposes, creating new collective works, for resale or redistribution to servers or lists, or reuse of any copyrighted component of this work in other works. Access to this work was provided by the University of Maryland, Baltimore County (UMBC) ScholarWorks@UMBC digital repository on the Maryland Shared Open Access (MDSOAR) platform.

# Please provide feedback 

Please support the ScholarWorks@UMBC repository by emailing scholarworks-group@umbc.edu and telling us what having access to this work means to you and why it's important to you. Thank you.

# Scalable and Hybrid Ensemble-Based Causality Discovery 

Pei Guo*, Achuna Ofonedu ${ }^{\dagger}$, Jianwu Wang*<br>*Department of Information Systems, University of Maryland, Baltimore County, Baltimore, United States<br>\{peiguo1, jianwu\}@umbc.edu<br>${ }^{\dagger}$ Department of Electrical Engineering and Computer Science, Catholic University of America, Washington, D.C., United States ofonedub@cua.edu


#### Abstract

Causality discovery mines cause-effect relationships among different variables of a system and has been widely used in many disciplines including climatology and neuroscience. To discover causal relationships, many data-driven causality discovery methods, e.g., Granger causality, PCMCI and Dynamic Bayesian Network, have been proposed. Many of these causality discovery approaches mine time series data and generate a directed causality graph where each graph edge denotes a causeeffect relationship between the two connected graph nodes. Our benchmarking of different causality discovery approaches with real-world climate data show these approaches often generate quite different causality results with the same input dataset due to their internal learning mechanism differences. Meanwhile, there are ever-increasing available data in virtually every discipline, which makes it more and more difficult to use existing causality discovery algorithms to produce causality results within reasonable time. To address these two challenges, this paper utilizes data partitioning and ensemble techniques, and proposes a twophase hybrid causality ensemble framework. The framework first conducts phase 1 data ensemble for partitioned data and then conducts phase 2 algorithm ensemble from data ensemble results. To achieve scalability, we further parallelize the ensemble approaches via the Spark big data analytics engine. Our experiments show that our proposed approaches achieve good accuracy through ensemble and high scalability through dataparallelization in distributed computing environments.


Index Terms-Causality discovery, Ensemble learning, Data parallelism, Granger causality, Dynamic Bayesian Network

## I. INTRODUCTION

Causality [21] is a fundamental research topic studying cause-effect relationships among different components of a system and causality study can help explain why the system has certain behaviors. Causality learning/discovery has been widely studied and applied in many disciplines including climatology and neuroscience.

Many data-driven causality learning approaches have been proposed, such as Granger causality [12], PCMCI [24], Dynamic Bayesian Network [19], and Convergent Cross Mapping [32]. These approaches often mine time series data of two or more variables in a system and produce their predictions on cause-effect relationship among these variables. For instance, the work at [26] uses Granger causality to study cause-effect relationships among multiple climate variables and shows that sea surface temperature changes at pacific ocean near equator, an indicator of the El Niño-Southern Oscillation
(ENSO) climate phenomenon [13] can cause abnormal surface temperature, pressure and precipitation remotely.

One challenge with the variety of different causal discovery approaches/algorithms is that these approaches often lead to divergent causality conclusions from the same dataset, which makes it difficult to explain and use data-driven causality discovery results. There have been some studies comparing different causality discovery methods [15], [33]. For example, the experiments on comparing three causality discovery algorithms show there are only $83 \%$ overlapping among the results on average [15]. Yet there is still a lack of comprehensive framework to effectively integrate these diverse algorithms.

The other challenge to be tackled by this paper is the ever-increasing volume and dimension of available data for causality discovery. For instance, total worldwide climate data volume is projected to increase from 5 PB in 2010 to 350 PB in 2030 [20]. It is more and more difficult to use existing causality discovery algorithms to handle the increasing dimensionality and resolution of these climate datasets. Meanwhile, data volume is just one factor for time complexity of many causality discovery algorithms. As an example, a popular Granger causality algorithm's execution time grows quadratically with the increase of either of the three factors: data record number, variable number and time lag number [4]. Parallel causality discovery is crucial as a solution to reduce computation time.

To address the above two challenges, this paper applies data partitioning and ensemble techniques to achieve scalable and accurate causality learning. Ensemble learning [23] is a meta machine learning algorithm which combines multiple base or individual learners in order to get better overall learning accuracy. In this paper, we propose a two-phase hybrid causality ensemble learning framework by first partitioning data into smaller sizes and conducting phase 1 data ensemble for each data partition and then conducting phase 2 algorithm ensemble from phase 1 ensemble results. The framework can be easily parallelized through big data engines like Spark [1] and is adaptable to different ensemble approaches. To the best of our knowledge, this study is the first supporting both scalable and ensemble learning for causality discovery. The implementations of our work is open-sourced at [2].

The contributions of this paper are as follows.

- We propose a two-phase hybrid causality ensemble framework by first conducting phase 1 data ensemble for partitioned data and then conducting phase 2 algorithm ensemble from phase 1 data ensemble results. The framework can combine learning results from different data partitions (namely data ensemble), and different algorithms (namely algorithm ensemble).
- Based on the above framework, we propose an approach for parallel causality ensemble learning via Spark [1] and the MapReduce programming model [10].
- We did experiments to evaluate our proposed scalable ensemble framework and approach, which shows that our approach can achieve both perfect accuracy and almost linear speedup.

The rest of the paper is organized as follows. The background is introduced in Section II. The two-phase hybrid causality ensemble learning framework is explained in Section III. Section IV contains the ensemble approach based on the scalable causality ensemble framework. Section V describes the parallelization of our implementation. The experiments and evaluations are in Section VI, with related work discussion in Section VII. Finally, Section VIII concludes our paper.

## II. BACKGROUND

### II-A Ensemble Learning

Ensemble learning [23] is a meta machine learning algorithm which uses multiple learning methods to obtain better predictive performance than learning from any of the constituent methods. Since 1990, ensemble learning methods have become a major learning paradigm because of both empirical good performances in real-world applications and theoretical proof on its advantages [25]. Many state-of-art data mining approaches/packages, e.g. random forest and XGBoost [8], are based on ensemble learning.

Many ensemble learning algorithms have been proposed and they mainly vary in the following three aspects: 1) what are base/individual learners, 2) how each base learner learns from input data, 3) how to combine results of base learners. For base learner selection, if base learners used in an ensemble learning belong to the same type, e.g. decision tree or neural network, the ensemble algorithm is called homogeneous ensemble. Otherwise, it is called heterogeneous ensemble. Regarding how each base learner learns, there are three main approaches and they mostly differ in how input data is fed to base learner. The first approach, called stacking ensemble [31], uses the same input data for all base learners. Bagging ensemble [6], as the second approach, uses different sampling results from the original input data for different base learners. The third approach is boosting ensemble [11] which uses multiple base learners iteratively and, in each iteration, assigns higher weight to data whose learning accuracy was low in previous iterations. On base learner combination, common methods are majority voting and weighted majority voting [23].

### II-B Causality Discovery Methods

Existing causal relationships discovery methods can be categorized into two types depending on the input datasets types: 1) learning from multivariate independent and identically distributed (i.i.d.) data and 2) learning from multivariate time-series data. The learning results from a multivariate causality approach can be denoted as a directed graph where each graph edge represents a cause-effect relationship conditioned on all other variables in the graph. In this subsection, we explain three multivariate causality discovery approaches towards time-series input data, namely multivariate (graphical) Granger causality [4], PCMCI [24] and dynamic Bayesian network [19] and their algorithm details. Because they all belong to the same casualty discovery category and their learning results can be modeled as directed graphs, we could conduct ensemble learning using these algorithms as base learners which will be explained in later sections.

1) Multivariate Granger Causality: Granger causality, as a predictive model in economics, was proposed in 1969 by Nobel Laureate Clive W. Granger. By definition, in Granger causality, one time series $x$ Granger causes another time series $y$, if and only if the regression for $y$ based on past values of both $x$ and $y$ is statistically significant than the regression of $y$ only based on past values of $y$ itself. To demonstrate the definition, let the lagged variable $x$ be $x_{t-i}$ for $i$ from 1 to maximum lag $P$; and similarly, the lagged $y$ is represented by $y_{t-i}$. To test Granger causality, in first step, the following two linear regressions functions are fitted as follows:

$y_{t}=a_{11}\cdot y_{t-1}+a_{12}\cdot y_{t-2}+...+a_{1P}\cdot y_{t-P}+\varepsilon_{1}$ (1)
$y_{t}=a_{21}\cdot y_{t-1}+...+a_{2P} \cdot y_{t-P}+b_{21} \cdot x_{t-1}+...+b_{2P} \cdot x_{t-P}+\varepsilon_{2}$

Next, the accuracy of predicting $y_{t}$ using Equation (1) and Equation (2) are compared to check which regression works better. In most cases, statistical hypothesis test methods such as $F$-test or Chi-squared ( $\chi^{2}$ ) test are utilized to get a $p$-value to determine statistical significance.

The above pairwise Granger causality is proven to work well on discovery between each pair of variables. However, most datasets in research contain more than two variables. When the scientists intend to discover the causality among a subset or the whole set of a multivariate dataset, pairwise Granger causality ignores the causalities with other untested variables, which could generate spurious causal relationships such as confounding variable [22] and indirect causal relationship [18].

To address the limitations of the pairwise Granger causality method, multivariate Granger causality discovery, a.k.a. graphical Granger causality discovery, fits a vector autoregressive model (VAR) to time series data [16], compared to linear regression models in pairwise Granger causality. To demonstrate multivariate Granger causality model, we denote $X_{t=1}^{P}$ as lagged variables of time series variable $x$ from time lag 1 to maximum lag $P$, and similarly $Y_{t=1}^{P}$ from $y$, $Z_{t=1}^{P}$ from

$z$. The joint VAR model for multivariate Granger causality is shown as as follows:

$$
\left\{\begin{array}{l}
y_{t}=A_{1} \cdot Y_{l=1}^{P}+B_{1} \cdot X_{l=1}^{P}+\varepsilon_{1 t} \\
x_{t}=C_{1} \cdot X_{l=1}^{P}+D_{1} \cdot Y_{l=1}^{P}+\varepsilon_{2 t}
\end{array}\right.
$$

with the prediction error covariance matrix being:

$$
\operatorname{CovMatrix}=\left[\begin{array}{cc}
\operatorname{var}\left(\varepsilon_{1 t}\right) & \operatorname{cov}\left(\varepsilon_{1 t}, \varepsilon_{2 t}\right) \\
\operatorname{cov}\left(\varepsilon_{2 t}, \varepsilon_{1 t}\right) & \operatorname{var}\left(\varepsilon_{2 t}\right)
\end{array}\right]
$$

Besides lagged variables $X_{l=1}^{P}$ and $Y_{l=1}^{P}$, when a new variable $z$ is taken into account, the new VAR model is:

$$
\left\{\begin{array}{l}
y_{t}=A_{2} \cdot Y_{l=1}^{P}+B_{2} \cdot Z_{l=1}^{P}+C_{2} \cdot X_{l=1}^{P}+\varepsilon_{3 t} \\
z_{t}=D_{2} \cdot Y_{l=1}^{P}+E_{2} \cdot Z_{l=1}^{P}+F_{2} \cdot X_{l=1}^{P}+\varepsilon_{4 t} \\
x_{t}=G_{2} \cdot Y_{l=1}^{P}+H_{2} \cdot Z_{l=1}^{P}+I_{2} \cdot X_{l=1}^{P}+\varepsilon_{5 t}
\end{array}\right.
$$

Correspondingly, the prediction error covariance matrix of VAR model in (5) is:

$$
\Sigma=\left[\begin{array}{ccc}
\operatorname{var}\left(\varepsilon_{3 t}\right) & \operatorname{cov}\left(\varepsilon_{3 t}, \varepsilon_{4 t}\right) & \operatorname{cov}\left(\varepsilon_{3 t}, \varepsilon_{5 t}\right) \\
\operatorname{cov}\left(\varepsilon_{4 t}, \varepsilon_{3 t}\right) & \operatorname{var}\left(\varepsilon_{4 t}\right) & \operatorname{cov}\left(\varepsilon_{4 t}, \varepsilon_{5 t}\right) \\
\operatorname{cov}\left(\varepsilon_{5 t}, \varepsilon_{3 t}\right) & \operatorname{cov}\left(\varepsilon_{5 t}, \varepsilon_{4 t}\right) & \operatorname{var}\left(\varepsilon_{5 t}\right)
\end{array}\right]
$$

The next step, similar to the pairwise Granger causality testing, is to test whether introducing $z$ can improve the prediction of $y$ and how significant the improvement is. From the VAR model in Equation (3) of variable $y$ and $x$, and the VAR model in Equation (5) of variable $y, z$, and $x$, the conditional Granger causality test from $z$ to $y$ conditioned on $x$, denoted as $(z \rightarrow y \mid x)$, is:

$$
F \text {-test }\left(\operatorname{var}\left(\varepsilon_{1 t}\right), \operatorname{var}\left(\varepsilon_{3 t}\right)\right)
$$

From $F$-test in Equation (7), a $p$-value can be used to compare with a threshold to conclude whether $z$ Granger causes $y$ conditioned on $x$.
2) PCMCI: PCMCI is a causal discovery method described in [24] which identifies relevant variables for conditioning and estimates causality graph from time series data. The method makes use of a "time series graph" made of nodes representing the state variables at different time-lags. If the time lag is denoted by $l$, a causal link is notated $x_{t-l} \rightarrow y_{t}$, and this link exists if $x_{t-l}$ is not conditionally independent of $y_{t}$ given the past of all variables. Assuming the causal structure does not change over time, the same links are present at each time step.

The parents $\mathcal{P}(x)$ of a variable $x$ are defined as the set of all nodes with a link towards $x$. However, estimating these parents directly by testing for conditional independence on the whole past is problematic due to high-dimensionality and because conditioning on irrelevant variables leads to biases.

PCMCI estimates causal links by a two-step procedure [24]:

1. Condition-selection: For every variable $\alpha$, estimate a superset of parents $\hat{\mathcal{P}}\left(\alpha_{t}\right)$ with an iterative Markov discovery algorithm [27] such as $P C_{1}$ algorithm. The condition-selection step reduces the dimensionality and avoids conditioning on irrelevant variables.
2. Momentary conditional independence (MCI): To test whether $x_{t-l} \rightarrow y_{t}$ with MCI, it evaluates:

$$
x_{t-l} \perp y_{t} \mid \hat{\mathcal{P}}\left(y_{t}\right), \hat{\mathcal{P}}\left(x_{t-l}\right)
$$

Equation (8) checks momentary conditional independence conditions between $x_{t-l}$ and $y_{t}$, and checks whether or not $x_{t-l}$ and $y_{t}$ are not conditionally independent given $\hat{\mathcal{P}}\left(y_{t}\right)$ and $\hat{\mathcal{P}}\left(x_{t-l}\right)$.
3) Dynamic Bayesian Network: Bayesian network [5] is one of many probabilistic graphical models which consists of a directed acyclic graph (DAG) and conditional probability distributions (CPDs) associated with each node in the model. A Bayesian network can be used to make predictions and decisions under uncertainty. A dynamic Bayesian network [19] is similar to a Bayesian network but with a temporal extension, making it an appropriate graphical model to use for temporal datasets. The two main steps to creating a probabilistic graphical model are structure learning and parameter learning.

In this paper, we adopt the approach in [33] for dynamic Bayesian network learning. The approach first expands variable set by adding new variables for each original variable through time lagging. For instance, $P$ new variables can be created from original variable $x: x_{t-i}$ for $i$ from 1 to maximum lag $P$. With the expanded variable set, the K2 algorithm [9] is used to search through all possible causality graph structures and identify which structure has the highest possibility to produce the data. In this score-based structure learning approach, Bayesian information criterion (BIC) scoring is used. Next, after causality graph is generated for expanded variable set, the causality graph is simplified by removing lagged variable and combining the causality edges. For instance, two edges $x_{t-2} \rightarrow y_{t-1}$ and $x_{t-3} \rightarrow y_{t}$ are combined to one edge $x \rightarrow y$ in the final graph.

Moreover, for the sake of computational time, the time series data is partitioned into bins. Each bin defines a set of sub ranges, then the data is assigned to each labeled bin. For example, if the lowest value of the dataset is -5 , and the highest value is 5 . With the total bin number 10 , a value of 1.2351 can be placed in a bin labeled 7 , whose range is $[1,2)$. This approach increases the state counts of each variable and allows for faster computation.

## III. A Two-Phase Hybrid Causality Ensemble Framework

To deal with both increasing volume of available input data and increasing variety of available causality discovery algorithms, we propose a two-phase hybrid causality ensemble framework to achieve ensemble of both multiple causality discovery algorithms as base learners and multiple data partitions as base learner's input data. Before diving into the details of this two-phase ensemble framework, we first explain how ensemble could be done with only data ensemble and algorithm ensemble. We note most causality discovery algorithms generate not only cause-effect relationships, but also time lag and probability of each relationship. In this paper, we only focus on structure causality ensemble, namely how multiple directed graphs can be combined into one, and leave the time lag and probability ensemble for future work.

### III-A Algorithm Ensemble for Causality Discovery

Algorithm ensemble approach deals with algorithm variety by applying different causality discovery algorithms as base learners with the same input data and later combining all base learner results. Each causality discovery algorithm mines the same time series dataset and produces its own directed graph where nodes denote time series variables and each directed edge denotes a cause-effect relationship between the two connected variables. Because each base learner works on the same input data, the nodes of result graphs are the same for different base learners. But different base learners could produce different causality edges. Then by applying a certain base learner combination method, such as majority voting, we can derive a new directed graph as ensemble result. The nodes in the ensemble graph are the same with the results in each base learner. For graph edges, we can iterate all possible edges of the graph and decide whether this edge should be in the ensemble graph by combining corresponding edges in base learner graph result. If we use majority voting as combination method, an edge will be in ensemble graph only if the edge appears in more than half of base learner graphs.

By applying algorithm ensemble, the ensemble result is often more accurate than utilizing only one single causality discovery algorithm. However, when the size of input time series dataset gets larger, the execution time of algorithm level ensemble increases dramatically because every base learner will take longer time to finish. Thus, a non-scalable algorithm ensemble approach is not enough to meet the challenge of dealing with the increasing data size.

### III-B Data Ensemble for Causality Discovery

Data ensemble approach deals with data volume challenge by first partitioning data into smaller datasets, then using the same causality discovery algorithm as base learners with data partitions, and later combining all base learner results. Data partitioning is often done horizontally, not vertically, so that each data partition can still have all variables needed for multivariate causality learning. Because input data are often time series, data partitioning can be easily done by splitting the overall time ranges into smaller time ranges. Similar to algorithm ensemble, the nodes of resulting causality graph are the same for different base learners and edges of the graphs might be different. Then we can derive ensemble graph using the same base learner combination method in the previous subsection. The limitation of this approach is that it does not deal with variety of causality learning algorithms.

### III-C Two-Phase Hybrid Data-Algorithm Ensemble for Causality Discovery

To address the challenges of diverse causality discovery results and increasing data size, we further integrate data ensemble and algorithm ensemble into one framework as illustrated in Figure 1, which conducts two-phase hybrid ensemble. We implement this generic framework as dataalgorithm ensemble, which means it conducts data ensemble first in phase 1 and then algorithm ensemble in phase 2.

![img-0.jpeg](img-0.jpeg)

Fig. 1. Two-phase hybrid ensemble framework for causality discovery.

In the causality ensemble framework, the input data is first partitioned into different data slices from 1 to N. Then, phase 1 causality computation is executed to get N phase 1 ensemble result for each causality method. Next, all the phase 1 data ensemble results are combined into one final output through phase 2 algorithm ensemble.

## IV. APPROACH OF TWO-PHASE HYBRID CAUSALITY ENSEMBLE FRAMEWORK

Based on the two-phase hybrid causality ensemble framework explained in previous section, the data-algorithm causality ensemble approach is developed as illustrated in Figure 2. This data-algorithm ensemble approach is designed to effectively learn causal relationships from three data-driven causality learning approaches: multivariate Granger causality (MGC), PCMCI and dynamic Bayesian network (DBN).

![img-1.jpeg](img-1.jpeg)

Fig. 2. Illustration of data-algorithm ensemble learning approach.

The data-algorithm ensemble approach (see Figure 2) denotes that data ensemble happens in phase 1, then algorithm ensemble happens in phase 2. In this approach, the input data is first partitioned into N slices. Then, each of the causality discovery method (MGC, PCMCI and DBN) is executed on all the partitioned data to get one causality output directed graph for each data slices. For example, MGC outputs MGC_Result₁, MGC_Result₂, ... MGC_Result₃.

Different methods are executed in serial in the order of $M G C$, $P C M C I, D B N$. The outputs from all partitioned data slices corresponding to each causality method are collected for phase 1 data ensemble. The phase 1 ensemble results are computed by majority voting. In the following step, phase 1 ensemble results of each causality method (MGC_Ensemble, $P C M C I \_$Ensemble and $D B N \_$Ensemble) are combined using ensemble methods again into get a phase 2 algorithm ensemble causality result graph as final output.

```
Algorithm 1: Data-Algorithm Ensemble (Data-
Algorithm_Ensemble)
    Input: Different causality discovery methods:
        Multivariate Granger causality: \(M G C\), PCMCI:
        \(P C M C I\), Dynamic Bayesian Network: \(D B N\),
    Time series data: \(D\),
    Number of data partitions: \(N\)
    Output: A directed causality graph: \(G=(V, E)\)
    1: Partition data \(D\) into \(N\) partitions as
        \(\{d\}=d_{1}, d_{2}, \ldots, d_{N}\)
    2: Get \(E_{M G C}=\) Data-Algorithm_Phase_1(MGC, \(\{d\})
    3: Get \(E_{P C M C I}=\)
        Data-Algorithm_Phase_1(PCMCI, \(\{d\})
    4: Get \(E_{D B N}=\) Data-Algorithm_Phase_1(DBN, \(\{d\})
    5: \#\# Phase 2 edge ensemble:
    6: for unique edges \(\left\{e_{i}\right\}\) in \(E_{M G C}, E_{P C M C I}\) and \(E_{D B N}\)
        do
        Count \(e_{i}\) appearance in \(E_{M G C}, E_{P C M C I}\) and \(E_{D B N}\)
        as \(n_{i}\)
        if \(n_{i}>=2\) then
            Add \(e_{i}\) to final graph \(G\)
        end if
    end for
    Output \(G=(V, E)\)
```

The data-algorithm ensemble approach includes two algorithms: Algorithm 1 (Data-Algorithm_Ensemble) for the twophase hybrid ensemble approach, which regards to the full process in Figure 2 and Algorithm 2 (Data-Algorithm_Phase_1) for phase 1 data ensemble corresponding to each phase 1 ensemble block in Figure 2.

The input of the Data-Algorithm_Ensemble (Algorithm 1) includes different causality discovery methods, which are multivariate Granger causality (MGC), PCMCI (PCMCI) and Dynamic Bayesian Network ( $D B N$ ), time series input data $D$, and the number of data partitions $N$. The logic of Algorithm 1 for the whole ensemble process is as follows. In line 1, the input dataset $D$ is first partitioned into $N$ slices by its timestamp as $\{d\}=d_{1}, d_{2}, \ldots, d_{N}$ where the time interval of each slice is only $1 / N$ of the original time series. Then it calls Algorithm 2 (Data-Algorithm_Phase_1) to execute each causality discovery method to get phase 1 ensemble causality edge set $E_{M G C}, E_{P C M C I}$ and $E_{D B N}$ from all the data partitions in lines 2-4. Finally, in lines 611, phase 2 ensemble result is computed by majority voting
on edge set of all causality mining methods, $E_{M G C}, E_{P C M C I}$ and $E_{D B N}$, that if two or more causality ensemble edge sets contain the same edge, this edge is added into final output graph $G=(V, E)$ with $V$ denoting nodes and $E$ as edges in line 12 .

```
Algorithm 2: Phase 1 Ensemble for Data-Algorithm
Ensemble (Data-Algorithm_Phase_1)
    Input: Causality discovery method: Causality,
    Data partition set: \(\{d\}\)
    Output: A set of directed edges in Graph
        corresponding to causality discovery method:
        \(E_{\text {causality }}\)
    1: for each data partition \(d_{i}\) in \(\{d\}\) do
        Get causality edge set from causality computation:
            \(E_{i}=\operatorname{Causality}\left(d_{i}\right)\)
    end for
    4: \#\# Phase 1 edge ensemble:
    5: for unique edges \(\left\{e_{j}\right\}\) in all \(E_{i}\) do
        Count \(e_{j}\) appearance in all \(E_{i}\) as \(n_{j}\)
        if \(n_{j}>N / 2\) then
            Add \(e_{j}\) to \(E_{\text {causality }}\)
        end if
    end for
    Output \(E_{\text {causality }}\)
```

The phase 1 data ensemble in the data-algorithm ensemble approach, namely Data-Algorithm_Phase_1 is shown in Algorithm 2. Its inputs include the specific causality discovery method Causality, and the partitioned time-series dataset $\{d\}$. In lines 1-3, the causality discovery method executes for each data partition $d_{i}$ in $\{d\}$ to output a causality edge set $E_{i}$ from Causality $\left(d_{i}\right)$. Since this causality edge set contains edges from each partition, in lines 5-10, phase 1 ensemble method loops to check if the number of a given edge $e_{j}$ appears in more than half of the partition edge set. For instance, if there are 10 partitions, and a causality edge $\left(x_{1}, x_{2}\right)$ appears 6 times in all the partition edge set, it is added to the phase 1 ensemble output $E_{\text {causality }}$ as in line 8 then be output as in line 11.

## V. Parallel Two-Phase Hybrid Causality Ensemble Learning via Spark Big Data Engine

The above two-phase hybrid causality ensemble approach is further implemented in parallel via Spark [1] to achieve scalability to deal with big data in two aspects: 1) automatic data partitioning and 2) parallel function mapping.

Regarding the data partitioning part in our parallel implementation, the data is first load into Spark as resilient distributed dataset (RDD); then it is automatically partitioned by timestamp of each record, as in the phase 2 algorithm ensemble of data-algorithm ensemble, in Algorithm 1 line 1. More specifically, every data partition, as a chunk of the large distributed dataset, is assigned an index $i$ for phase 1 ensemble in next step.

For parallel function mapping, the parallelization of data-algorithm ensemble is implemented in its phase 1 data ensemble, as in Algorithm 2 lines 1-3. With Spark RDD partitioning, now each data partition $d_{i}$ becomes an RDD partition. Next, these RDD partitions are mapped to be transformed by the causality discovery method *Causality* in parallel, then be reduced as the edge set $E_{i}$ for later phase 2 ensemble computation.

## VI. EXPERIMENTS

The experiments were conducted on top of the HPCF2018 cluster at the University of Maryland, Baltimore County [3], where each computing node containing two 18-core CPUs and 384 GB memory. For our experiment environment, one cluster contains one master node and several worker nodes. Moreover, the Spark programs are managed by Slurm workload manager in standalone cluster mode. For software, Python (version 3.6.8), Spark (version 2.4) are used. For Spark configurations, each node contains one executor, each driver/executor’s memory is 200GB, and partition number is set as 48.

For test data, we created four synthetic datasets to evaluate our proposed algorithms’ performance. One important reason for synthetic dataset generation is to know causality ground truth so we could evaluate learning result accuracy. Similar to the synthetic dataset generation approach for Granger causality and DBN evaluation in [33], we generated our synthetic dataset based on linear and nonlinear causal dependency Equation (9) and Equation (10), where $\varepsilon$ s are random noises. The causality graph for the equation can be found at Figure 3 and Figure 4. The linear and nonlinear datasets with different sizes (namely 1 million and 10 million for row numbers) were generated using the same equations correspondingly.

$\left\{\begin{array}{l}x_{1}(t)=0.95\cdot\sqrt{2}\cdot x_{1}(t-1)-0.90\cdot x_{1}(t-2)+\varepsilon_{1} \\x_{2}(t)=0.5\cdot x_{2}(t-1)+\varepsilon_{2} \\x_{3}(t)=-0.5\cdot x_{1}(t-1)+0.25\cdot\sqrt{2}\cdot x_{3}(t-1) \\\quad+0.25\cdot\sqrt{2}\cdot x_{2}(t-1)+\varepsilon_{3} \\x_{4}(t)=-0.95\cdot x_{4}(t-1)-0.25\cdot\sqrt{2}\cdot x_{3}(t-1)+\varepsilon_{4} \\x_{5}(t)=0.5\cdot x_{1}(t-1)+0.95\cdot x_{2}(t-2) \\\quad-0.25\cdot\sqrt{2}\cdot x_{3}(t-1)+0.5\cdot x_{5}(t-1)+\varepsilon_{5}\end{array}\right.$
$\left\{\begin{array}{l}x_{1}(t)=0.125\cdot\sqrt{2}\cdot\exp(-x_{1}(t-1)^{2}/2)+\varepsilon_{1} \\x_{2}(t)=1.2\cdot\exp(-x_{1}(t-1)^{2}/2)+\varepsilon_{2} \\x_{3}(t)=-1.05\cdot\exp(-x_{1}(t-1)^{2}/2) \\\quad+0.2\cdot\sqrt{2}\exp(-x_{2}(t-2)^{2}/2)+\varepsilon_{3} \\x_{4}(t)=-1.15\cdot\exp(-x_{1}(t-2)^{2}/2) \\\quad+0.2\cdot\sqrt{2}\cdot\exp(-x_{4}(t-1)^{2}/2) \\\quad+1.35\cdot\exp(-x_{3}(t-1)^{2}/2)+\varepsilon_{4} \\x_{5}(t)=-1.15\cdot\exp(-x_{2}(t-1)^{2}/2)+\varepsilon_{5}\end{array}\right.$
$\left.\begin{array} { l } 
\end{array}\right.$

## A. Baseline Approaches and Parameter Setting

We employed seven baseline approaches in our experiments. The first three were single causality discovery approaches: Multivariate Granger causality ($MGC$), $PCMCI$ and Dynamic Bayesian Network ($DBN$). The next three were corresponding data ensemble approaches for each of the three single

![img-2.jpeg](img-2.jpeg)

Fig. 3. Linear synthetic data ground truth causal graph.

![img-3.jpeg](img-3.jpeg)

Fig. 4. Nonlinear synthetic data ground truth causal graph.

causality discovery approaches following the way described in Section III-B. The last one was an algorithm ensemble approach by combining all the three single causality discovery approaches following the way described in Section III-A. For experiment parameter settings, we set the maximum time lagging as 3 for synthetic data and the $p$-value threshold as 0.05 for both $MGC$ and $PCMCI$ tests. Besides, the total bin number for $DBN$ was set as 5 to reduce computation time. In $PCMCI$ method, we utilized its different conditional independence tests for linear and nonlinear causality discovery. For nonlinear conditional independence tests, as we had a large dataset, $RCOT$ test was applied.

## B. Accuracy Evaluation

We employ Structural Hamming Distance (SHD) metric [29] to compare accuracy of different approaches. SHD is a common metric to measure the difference between two directed graphs with the same node set. SHD value is defined as the total step count of three types of actions needed to transform from one direct graph to another direct graph: 1) reversing an edge’s direction, 2) removing an extra edge, 3) adding a missing edge. We calculate SHD between ground truth graph and each learned graph. The lower SHD value means the more similarity between the two graphs, so the algorithm that generates the learned graph is more accurate.

We measured the accuracy of single causality discovery method of $MGC$, $PCMCI$ and $DBN$ and the three data ensemble baseline approaches and the algorithm ensemble causality ensemble approach. The results were shown columns 2-8 of Table I. For linear datasets, we could see from the table that both data ensemble and algorithm approach could achieve the same or better accuracy than single causality discovery approaches. For nonlinear datasets, data ensemble approaches still performs better in accuracy; however, algorithm ensemble could perform a little bit worse due to two algorithm making the same wrong prediction on certain edges.

The accuracy of two-phase hybrid causality ensemble approach was shown in column 9 of Table I. Compared to

TABLE I
Structural Hamming Distance (SHD) comparison of different Causality Discovery Approaches


TABLE II
EXECUTION TIME TABLE: SERIAL BASELINE EXPERIMENTS(H:MM:SS.SS)


TABLE III
EXECUTION TIME: PARALLEL EXPERIMENTS ON 1M LINEAR DATA


TABLE IV
EXECUTION TIME: PARALLEL EXPERIMENTS ON 10M LINEAR DATA


TABLE V
EXECUTION TIME: PARALLEL EXPERIMENTS ON 1M NONLINEAR DATA


TABLE VI
EXECUTION TIME: PARALLEL EXPERIMENTS ON 10M NONLINEAR DATA


The Spark based parallel implementations of the three dataensemble baseline approaches use the same techniques in Section V. We measured their execution times as in columns 2-4 of parallel experiments execution time tables. We also recorded the execution times of data-algorithm ensemble showing in column 5 of all execution time tables for parallel experiments.

We note Tables III, IV, V, VI show data-level parallel ensemble PCMCI is slower than our two-phase ensemble. By checking the execution logs, we found it is because at the runtime the Spark session encountered idle time for executors in the cluster, thus the computation time is fairly long. However, we did not see the same behavior in the twophase ensemble experiments. The reason for this unexpected result will be further investigated.
2) Speed Up: By comparing the execution times our parallel hybrid approaches in Tables III, IV, V, VI with the execution times of our serial algorithm ensemble baseline approach in Table II, we evaluated the speed ups of our parallel hybrid ensemble approaches. The algorithm ensemble baseline was executed on a single node. As shown in Figures 5 and 6 , both achieved near linear speed up. Figure 5 shows the speed ups of two-phase ensemble in comparison to algorithm ensemble baseline for 10 M row linear dataset. With 8 worker nodes, the speed up is more than 32 times. Similarly, Figure 6 shows speed up of two-phase ensemble compared to algorithm ensemble baseline for 10 M nonlinear dataset. Its speed up, when running with 8 worker nodes, reaches 17 times compared to the baseline. Our approaches can achieve better than linear speedup because the time complexity of each baseline algorithm is worse than $O(n)$. For instance, Granger causality algorithm's execution time grows quadratically with the increase of the data record number [4]. By splitting data into $N$ partitions, the execution time for each data partition is less than $1 / N$ of the baseline serial approach.

## VII. Related Work

There have been many studies on ensemble learning and scalable/parallel machine learning. But we believe our work is the first study dealing with both algorithm variety and data volume for causality discovery. We also did not find many studies directly on ensemble learning for causality. Because

![img-4.jpeg](img-4.jpeg)

Fig. 5. Speed up of two-phase ensemble compared to algorithm ensemble baseline for 10M row linear dataset.

![img-5.jpeg](img-5.jpeg)

Fig. 6. Speed up of two-phase ensemble compared to algorithm ensemble baseline for 10M row nonlinear dataset.

causality graph can be categorized as a type of probabilistic graphic model, we first discuss and compare with related work on ensemble learning for probabilistic graphic models in the first subsection. We further discuss and compare additional big data parallel ensemble learning work beyond probabilistic graphic models.

To achieve probabilistic graphical model ensemble, using the three categories explained in Section II, existing ensemble learning approaches can also be categorized into 1) algorithm ensemble for work at [17], 2) data ensemble work at [14], [30], and 3) hybrid ensemble for both data and algorithm at [28] and [7]. In algorithm ensemble category, [17] supports parallel ensemble learning of multiple classifiers on the same data. As a data ensemble approach, [14] first splits the training data, then trains Bayesian sub-networks in parallel, finally does boosting as ensemble method on the trained sub-networks to get the learning result. [30] is also a data ensemble approach for Bayesian network learning from big datasets to achieve better scalability and accuracy. As a hybrid ensemble approach, [28] conducts two-phase (algorithm ensemble for each data partition and data ensemble for multiple data partitions) Bayesian network ensemble learning. The main differences of this work and [28] are: 1) this work first conducts data ensemble among all data partitions and then algorithm ensemble for different algorithms where [28] first conducts algorithm ensemble then data ensemble; 2) our algorithm-level ensemble belongs to heterogeneous ensemble because each learning algorithm uses its own causality discovery models, while [28] belongs to homogeneous ensemble with different learning algorithms of the same Bayesian network model; 3) this paper targets causality discovery instead of Bayesian network learning.

Besides the probabilistic graphic model related ensemble studies in the previous subsection, most other big data parallel ensemble learning algorithms are tree based where different trees can be trained in parallel with a data subset, then results from multiple trees are ensembled via majority voting (e.g., [7]) or tree boosting (e.g., XGBoost [8]). There are two main approaches of data partitioning: horizontal data partitioning based on rows and vertical data partitioning based on columns. [7] contains horizontal data partitioning and parallel learning among the data partitions. Input data is first partitioned vertically to divide training data features to independent subsets. Then each task loads the data from one feature subset to train an independent tree and multiple trees can be trained in parallel. For XGBoost [8], parallel training is done via horizontally partitioned data and they differ in how different trees are ensembled. As a comparison, parallelization in our hybrid ensemble approaches is done via horizontal data partitioning because all features are needed for each training and our data has time dependency. Further, multiple learning algorithms are employed in our data-algorithm ensemble while the above related works only employ the same learning algorithm for different data partitions.

## VIII. CONCLUSIONS

Causality discovery is a fundamental research topic in many disciplines and discovered cause-effect relationships can help explain why a system has certain behavior or state. Nowadays, data-driven causality discovery faces two challenges: 1) the large volume of datasets to be learned from and 2) the variety of causality discovery algorithms. To deal with these two challenges, this paper proposes a two-phase hybrid ensemble causality learning framework and an implementation approach for scalable ensemble causality learning. Experiments show our algorithms outperform baseline ones in terms of both accuracy and execution time.

For future work, we will focus on the following aspects. First, we will extend the work to further enable ensemble of time lag and probability of causal edges. Second, we will study how to best select from many available causality learning algorithms, i.e., through diversity measurement, for better ensemble result accuracy. Further, we plan to apply the framework and algorithms to real-world climate applications and evaluate their effectiveness through the applications.

## ACKNOWLEDGMENT

This work is supported by grant CyberTraining: DSE: Cross-Training of Researchers in Computing, Applied Math-

ematics and Atmospheric Sciences using Advanced Cyberinfrastructure Resources (OAC-1730250), and grant CAREER: Big Data Climate Causality Analytics (OAC-1942714) from the National Science Foundation. The execution environment is provided through the High Performance Computing Facility at UMBC.
