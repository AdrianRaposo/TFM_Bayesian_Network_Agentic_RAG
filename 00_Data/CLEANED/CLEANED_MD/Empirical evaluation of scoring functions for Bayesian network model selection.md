# Empirical evaluation of scoring functions for Bayesian network model selection 

Zhifa Liu ${ }^{1,2 \dagger}$, Brandon Malone ${ }^{1,3 \dagger}$, Changhe Yuan ${ }^{1,4 *}$<br>From Proceedings of the Ninth Annual MCBIOS Conference. Dealing with the Omics Data Deluge Oxford, MS, USA. 17-18 February 2012


#### Abstract

In this work, we empirically evaluate the capability of various scoring functions of Bayesian networks for recovering true underlying structures. Similar investigations have been carried out before, but they typically relied on approximate learning algorithms to learn the network structures. The suboptimal structures found by the approximation methods have unknown quality and may affect the reliability of their conclusions. Our study uses an optimal algorithm to learn Bayesian network structures from datasets generated from a set of gold standard Bayesian networks. Because all optimal algorithms always learn equivalent networks, this ensures that only the choice of scoring function affects the learned networks. Another shortcoming of the previous studies stems from their use of random synthetic networks as test cases. There is no guarantee that these networks reflect real-world data. We use real-world data to generate our gold-standard structures, so our experimental design more closely approximates real-world situations. A major finding of our study suggests that, in contrast to results reported by several prior works, the Minimum Description Length (MDL) (or equivalently, Bayesian information criterion (BIC)) consistently outperforms other scoring functions such as Akaike's information criterion (AIC), Bayesian Dirichlet equivalence score (BDeu), and factorized normalized maximum likelihood (fNML) in recovering the underlying Bayesian network structures. We believe this finding is a result of using both datasets generated from real-world applications rather than from random processes used in previous studies and learning algorithms to select highscoring structures rather than selecting random models. Other findings of our study support existing work, e.g., large sample sizes result in learning structures closer to the true underlying structure; the BDeu score is sensitive to the parameter settings; and the fNML performs pretty well on small datasets. We also tested a greedy hill climbing algorithm and observed similar results as the optimal algorithm.


## Introduction

Bayesian networks are compact graphical models for representing uncertain relationships among the random variables in a domain. Often, the relationships are unknown and must be learned from data. A popular approach called score-based learning [1] is to assign a score to each Bayesian network structure according to a scoring function and find the structure that optimizes the score. There are many scoring functions for Bayesian networks, such as minimum description length (MDL) [2] (or

[^0]equivalently, Bayesian information criterion (BIC) [3]), Akaike's information criterion (AIC) [4], Bayesian Dirichlet equivalence score (BDeu) [5,6], factorized normalized maximum likelihood (fNML) [7], and others [8,9].

The score-based approach to learning Bayesian networks has been shown to be NP-hard [10]; both the running time and memory usage of exact learning are exponential in the number of variables in the worst case. Therefore, early research mainly focused on developing approximation methods [1,11-14]. Recently, however, optimal learning algorithms such as dynamic programming [15-17], branch and bound [18], admissible heuristic search [19-21], and mathematical programming $[22,23]$ have been developed to learn optimal Bayesian networks with several dozens of variables.


[^0]:    * Correspondence: changhe.yuan@qc.cuny.edu
    $\dagger$ Contributed equally
    ${ }^{\dagger}$ Department of Computer Science and Engineering, Mississippi State University, Mississippi State, MS 39762, USA
    Full list of author information is available at the end of the article

Because of the different theoretical underpinnings of these scoring functions, they typically result in different "optimal" networks. Once a scoring function has been selected, though, all optimal algorithms learn equivalent networks; they only differ in running time and memory usage. A major mystery surrounding Bayesian network learning is which scoring function to use given that there are so many choices. Several empirical investigations have been carried out on the performance of various scoring functions in learning Bayesian networks, e. g. [24-26]. These studies, however, have drawbacks in their evaluations because they used local search methods such as K-2 [1] and Greedy Thick Thinning algorithm [27] to select network structures, or even used randomly generated network structures [26]. These suboptimal structures may affect the reliability of their conclusions regarding the model selection capability of the scoring functions. Furthermore, these studies often generate random synthetic networks as the test cases; experimental data thus generated may not share similar properties as real-world data.

In this study, we use an optimal dynamic programming algorithm [16] to learn Bayesian network structures; any other optimal algorithm would yield the same results, however, because only the choice of scoring function affects the learned networks. We study the capability of four scoring functions, MDL, AIC, BDeu, and fNML, to recover the underlying Bayesian network structures. We generated artificial datasets from a set of gold standard Bayesian networks created based on real-world data, learned optimal Bayesian networks for them using different scoring functions, and compared the learned models with the gold standard models based on various evaluation measures. For comparison, we also included the results of a greedy hill climbing algorithm.

Our results offer new insights into the scoring functions in addition to confirming some other common beliefs. In contrast to the results of existing work, a major finding of our study suggests that the MDL/BIC score consistently outperforms AIC, BDeu, and fNML in recovering the underlying Bayesian network structures across various sample sizes. Other findings of our study support existing work. Our results confirm that the structural Hamming distance gives a more reliable measure of the distance between Bayesian net-work structures. We also observed that a parameter selection greatly affects the BDeu score. Finally, it is confirmed that fNML has good performance when the sample sizes are relatively small. Our results using the greedy hill climbing algorithm are similar to those of the optimal learning algorithm, although with higher variances, so our conclusions also hold for the greedy algorithm.

The remainder of this paper is structured as follows. We first review several prior empirical studies of scoring
functions. We then provide an overview of Bayesian network and structure learning. After that, we introduce four scoring functions which we will compare. We follow that with a description of the experimental design of this study. Finally, we present the empirical results and discuss our findings.

## Prior work

Several researchers have empirically evaluated the various scoring functions for learning Bayesian networks. In [26], Van Allen and Greiner compared the performance of three different model selection criteria, AIC, BIC, and cross-validation, in finding the right balance between the complexity of the model and the goodness of fit to the training data. First, they randomly generated the gold standard Bayesian network structures as well as the probability parameters. Second, they generated datasets with different sample sizes from the networks. For each dataset, they again randomly constructed a set of hypothesis structures and evaluated their quality based on the scoring functions. They found that AIC and cross-validation perform better in avoiding over-fitting in the model selection. While BIC may still work for large sample sizes, it can perform arbitrarily worse than other functions for small datasets. However, they did not use a learning algorithm to try to find good hypothesis structures; they also randomly generated their gold standard networks. It is unclear whether their results stem from the scoring functions or their random model selection technique, or whether the results can be generalized to real-world datasets.

In Yang and Chang's study [24], they compared the performance of five different scoring functions: uniform prior score metric (UPSM), conditional uniform prior score metrics (CUPSM), Dirichlet prior score metric (DPSM), BDe, and BIC. They restricted their experimental evaluations on random networks with three or five nodes as well as a benchmark network called Alarm. Then they generated random datasets from the networks. They used a K2like search method [1] to learn Bayesian networks. Their greedy structure learning algorithm assumes an ordering over the variables. Then, it greedily adds parents consistent with that ordering to maximize the likelihood of the structure and data set. Because of the ordering assumption and the greedy approach to adding parents, it does not guarantee finding the globally optimal structure. For evaluation, they use the cross-entropy (KL-Divergence) to measure the difference between the learned networks and the true networks. Their results indicated that UPSM, CUPSM, DPSM and BIC are able to correctly identify the true networks. Meanwhile, BDe and DPSM's performance are very sensitive to the $\alpha$ value. They may fail to find the true network if the $\alpha$ value is not set properly. This study shares the shortcoming of Van Allen and Greiner's study: their gold standard networks are randomly generated, so

they may not accurately reflect real-world datasets. Furthermore, their K2-like search method requires an ordering of the variables; in real-world applications, an ordering is often not known a priori. Therefore, it is again unclear how their results generalize to real-world situations.

Another related empirical work by de Jongh and Druzdzel [25] investigates structural evaluation measures for Bayesian networks rather than scoring functions. They generated random datasets with different sizes from four benchmark Bayesian networks. Then for each combination of the network and sample size, they ran a local search algorithm called Greedy Thick Thinning [27] to learn Bayesian network structures and calculated the distances between the learned networks and the gold standard networks based on structural Hamming distance, Hamming distance, and other measures. They concluded that the structural Hamming distance is especially useful when looking for the causal structures.

All of these studies have drawbacks in their empirical evaluations. In particular, the conclusions of Van Allen and Greiner are drawn based on randomly generated network structures. Therefore, it is unclear how reliable their conclusions are regarding the model selection capability of the scoring functions. Additionally, the two studies which evaluate scoring functions rely on randomly generated gold standard networks; these may not accurately reflect real-world datasets. The work of de Jongh and Druzdzel only investigates structural evaluation measures using a single scoring function; other scoring functions may behave differently. The current study is designed to address these concerns.

## Bayesian networks

A Bayesian network encodes a joint probability distribution over a set of random variables $\mathrm{V}=\left\{X_{1}, \ldots, X_{n}\right\}$. We consider only discrete variables in this work. Formally, a Bayesian network $B$ is a pair $\{G, \Theta\}$, where $G$ is a directed acyclic graph (DAG) in which each node corresponds to one of the random variables. The edges or lack of them encode the conditional independence relationships among the variables. The parents of $X_{i}$ are denoted $P A_{i} ; X_{i}$ is independent of its non-descendant variables given its parents. $\Theta$ specifies the conditional probability distributions $P\left\{X_{i} \mid P A_{i}\right\}$ for each $X_{i}$. Thus, the joint probability distribution of all of the variables is given as

$$
P(\mathbf{V})=\prod_{i=1}^{n} P\left(x_{i} \mid P A_{i}\right)
$$

Given a dataset $\mathbf{D}=\left\{D_{1}, \ldots, D_{N}\right\}$, where $D_{i}$ is an instantiation of all the variables in $\mathbf{V}$, Bayesian network structure learning is the problem of learning a network
structure from D. Assuming $D$ is complete and discrete, $\Theta$ is maximized using frequency counts from the data [7]. Consequently, finding the optimal Bayesian network reduces to finding the optimal structure.

Score-based learning is a commonly used technique to identify the optimal structure. In this approach, a scoring function is used to measure the goodness of fit of a structure to the data. The goal of the learning problem is then to find the optimally scoring structure. The score typically approximates the probability of the structure given the data and represents a tradeoff between how well the network fits the data and how complex the network is. In this work, we assume the scoring function is decomposable [6]. That is, the score for a network structure $B$ can be calculated as the sum of scores for the individual variables, where the score for a variable is calculated based solely on the variable and its parents. Therefore,

$$
\operatorname{Score}(B \mid D)=\sum_{i=1}^{n} \operatorname{Score}\left(X_{i} \mid P A_{i}, D\right)
$$

and the learning problem is to find $B^{*}$, where

$$
B^{*}=\underset{B}{\arg \max } \operatorname{Score}(B \mid D)
$$

A Bayesian network structure can represent a set of joint probability distributions. Two network structures are said to belong to the same equivalence class if they represent the same set of probability distributions [28]. A scoring function which assigns the same score to networks in the same equivalence class is score equivalent [6].

Unfortunately, the number of possible structures is super-exponential in the number of variables; learning an optimal Bayesian network from $D$ is shown to be NP-hard [10]. Solving the learning problem exactly becomes impractical if the number of variables is too large. Consequently, much early work focused on approximate algorithms, such as greedy hill climbing approaches [1,11], tabu search with random restarts [13], limiting the number of parents or parameters for each variable [14], searching in the space of equivalence classes of network structures [29], and the optimal reinsertion algorithm (OR) [12]. These algorithms use local search to find "good" networks; however, they offer no guarantee to find the one that optimizes the scoring function. Recently, exact algorithms for learning optimal Bayesian networks have been developed based on dynamic programming [15-17,30,31], branch and bound [18], linear and integer programming (LP) [22,23], and heuristic search [19-21]. These algorithms have enabled us to learn optimal Bayesian networks for datasets with dozens of variables.

Given a scoring function, all optimal learning algorithms learn equivalent networks; hence, the choice of which optimal algorithm is used does not affect the learned network. Consequently, these algorithms make it possible for us to study the behavior of different scoring functions in structure learning without needing to consider the confounding factors resulting from the choice of structure learning algorithms.

## Scoring functions

Many scoring functions are in the form of a penalized log-likelihood (LL) functions. The LL is the log probability of $D$ given $B$. Under the standard i.i.d assumption, the likelihood of the data given a structure can be calculated as

$$
\begin{aligned}
L L(D \mid B) & =\sum_{j}^{N} \log P\left(D_{j} \mid B\right) \\
& =\sum_{i}^{n} \sum_{j}^{N} \log P\left(D_{i j} \mid P A_{i j}\right)
\end{aligned}
$$

where $D_{i j}$ is the instantiation of $X_{i}$ in data point $D_{j}$, and $P A_{i j}$ is the instantiation of $X_{i}$ 's parents in $D_{j}$. Adding an arc to a network never decreases the likelihood of the network. Intuitively, the extra arc is simply ignored if it does not add any more information. The extra arcs pose at least two problems, though. First, they may lead to overfitting of the training data and result in poor performance on testing data. Second, densely connected networks increase the running time when using the networks for downstream analysis, such as inference and prediction.

A penalized LL function aims to address the overfitting problem by adding a penalty term which penalizes complex networks. Therefore, even though the complex networks may have a very good LL score, a high penalty term may reduce the score to be below that of a less complex network. Here, we focus on decomposable penalized LL (DPLL) scores, which are always of the form

$$
\operatorname{DPLL}(B, D)=L L(D \mid B)-\sum_{i=1}^{n} \operatorname{Penalty}\left(X_{i}, B, D\right)
$$

There are several well-known DPLL scoring functions for learning Bayesian networks. In this study, we consider MDL, AIC, BDeu and fNML. These scoring functions only differ in the penalty terms, so we will focus on discussing the penalty terms in the following discussions. In terms of memory and runtime, all of the scoring functions incur similar overhead [32].

## Minimum description length (MDL)

The MDL [3] scoring metric for Bayesian networks was defined in [2,33]. MDL approaches scoring Bayesian
networks as an information theoretic task. The basic idea is to minimally encode $D$ in two parts: the network structure and the unexplained data. The model can be encoded by storing the conditional probability tables of all variables. This requires $\frac{\log N}{2} * p$ bits, where $\frac{\log N}{2}$ is the expected space required to store one probability value and $p$ is the number of individual probability values for all variables. The unexplained part of the data can be explained with $L L(D \mid B)$ bits. Therefore, we can write the MDL penalty term as

$$
\operatorname{PenaltyMDL}\left(X_{i}, B, D\right)=\frac{\log N * p_{i}}{2}
$$

where $p_{i}$ is the number of parameters for $X_{i}$. For MDL, the penalty term reflects that more complex models will require longer encodings. The penalty term for MDL is larger than that of most other scoring functions, so optimal MDL networks tend to be sparser than optimal networks of other scoring functions. As hinted at by its name, an optimal MDL network minimizes rather than maximizes the scoring function. To interpret the penalty as a subtraction, the scores must be multiplied by -1 . The Bayesian information criterion (BIC) [3] is a scoring function whose calculation is equivalent to MDL for Bayesian networks, but it is derived based on the asymptotic behavior of the models, that is, BIC is based on having a sufficiently large amount of data. Also, BIC does not require the -1 multiplication.

## Akaike's information criterion (AIC)

Bozdogan [34] defined the AIC [4] scoring metric for Bayesian networks. It, like BIC, is another scoring function based on the asymptotic behavior of models with sufficiently large datasets. In terms of the equation, the penalty for AIC differs from that of MDL by the $\log N$ term. So the AIC penalty term is

$$
\operatorname{PenaltyAIC}\left(X_{i}, B, D\right)=p_{i}
$$

Because its penalty term is less than that of MDL, AIC tends to favor more complex networks than MDL.

## Bayesian Dirichlet with score equivalence and uniform priors (BDeu)

The Bayesian Dirichlet (BD) scoring function was first proposed by Cooper and Herskovits [1]. It computes the joint probability of a network for a given dataset. However, the BD metric requires a user to specify a parameter for all possible variable-parents combinations. Furthermore, it does not assign the same score to equivalent structures, so it is not score equivalent. To address the problems, a single "hyperparameter" called the equivalent sample size was introduced, referred to as $\alpha$ [6]. All of the needed parameters can be calculated

from $\alpha$ and a prior distribution over network structures. This score, called BDe, is score equivalent. Furthermore, if one assumes all network structures are equally likely, that is, the prior distribution over network structures is uniform, $\alpha$ is the only input necessary for this scoring function. BDe with this additional uniformity assumption is called BDeu [6]. Somewhat independently, the BDeu scoring function was also proposed earlier by Buntine [5]. BDeu is also a decomposable penalized LL scoring function whose penalty term is

$$
\operatorname{PenaltyBDeu}\left(X_{i}, B, D\right)=\sum_{j}^{q_{i}} \sum_{k}^{r_{i}} \log \frac{P\left(D_{i j k} \mid D_{i j}\right)}{P\left(D_{i j k} \mid D_{i j}, \alpha_{i j}\right)}
$$

where $q_{i}$ is the number of possible values of $P A_{i}, r_{i}$ is the number of possible values for $X_{i}, D_{i j k}$ is the number of times $X_{i}=k$ and $P A_{i}=j$ in $D$, and $\alpha_{i j}$ is a parameter calculated based on the user-specified $\alpha$. The original derivations $[5,6]$ include a more detailed description. The density of the optimal network structure learned with BDeu is correlated with $\alpha$; low $\alpha$ values typically result in sparser networks than higher $\alpha$ values. Recent studies [35] have shown the behavior of BDeu is very sensitive to $\alpha$. If the density of the network to be learned is unknown, selecting an appropriate $\alpha$ is difficult.

## Factorized normalized maximum likelihood (fNML)

Silander et al. developed the fNML score function to address the problem of $\alpha$ selection in BDeu based on the normalized maximum likelihood function (NML) [7]. NML is a penalized LL scoring function in which regret is the penalty term. Regret is calculated as

$$
\sum_{D^{\prime}} P\left(D^{\prime} \mid B\right)
$$

where the sum ranges over all possible datasets of size N. Kontkanen and Myllymäki [36] showed how to efficiently calculate regret for a single variable. By calculating regret for each variable in the dataset, the NML becomes decomposable, or factorized. fNML is given by

$$
\operatorname{Penalty} f N M L\left(X_{i}, B, D\right)=\sum_{k}^{q_{i}} \log C_{N_{q}}^{r_{i}}
$$

where $C_{N_{q}}^{r_{i}}$ are the regrets. fNML is not score equivalent.

## Methods

Our empirical evaluation of the scoring functions consisted of four phases. First, we created a set of Bayesian networks from real datasets as the gold standard networks. Next, we generated a variety of datasets from each of those gold standard networks by logic sampling.

After that, we learned optimal Bayesian networks from the sampled datasets using both an optimal algorithm and a greedy hill climbing algorithm. Finally, we calculated a number of evaluation metrics by comparing the learned networks with the gold standard networks.

## Creating gold standard networks

We need a set of gold standard Bayesian networks as the basis for our empirical evaluations. It is possible to use randomly generated Bayesian networks like several existing studies did, but we want to use models that resemble Bayesian networks that are created for realworld applications. There are many benchmark Bayesian networks available, such as Alarm, CPCS, Hepar, etc., but these benchmark models contain too many variables and are intractable for the current optimal learning algorithms. Therefore, we chose to create the gold standard networks by learning optimal Bayesian networks for a set of UCI machine learning datasets [37] with fewer than 25 variables. This section describes our data processing method for the reproducibility of the results.

The raw UCI datasets contain both continuous and discrete data, as well as missing values. Table 1 describes the detailed information for all the datasets used in this study. Continuous values were discretized using the minimum description length (MDL) discretization technique [38]. MDL discretization recursively partitions a dataset $S$ with a single variable $A$ by segmenting it into two distinct sets based on a boundary value $T$. The entropy between the two sets is minimal. The entropy between the two sets is defined as

$$
E=\frac{\left|S_{1}\right|}{\left|S_{2}\right|} \operatorname{Ent}\left(S_{1}\right)+\frac{\left|S_{2}\right|}{\left|S_{1}\right|} \operatorname{Ent}\left(S_{2}\right)
$$

where $S_{1}$ and $S_{2}$ are the segments of $S$ based on partitioning at $T$ and $\operatorname{Ent}(\cdot)$ is the entropy of the single set.

The recursion stops when the information gain of adding another partition does not exceed the cost of encoding the two new separate classes, given as

$$
\begin{aligned}
\text { Gain }>\frac{\log _{2}(|S|-1)}{|S|}+\frac{\Delta(A, T ; S)}{|S|} \\
\Delta(A, T ; S)=\log _{2}\left(3^{k}-2\right)+k \times \operatorname{Ent}(S) \\
\quad-k_{1} \times \operatorname{Ent}\left(S_{1}\right)-k_{2} \times \operatorname{Ent}\left(S_{2}\right)
\end{aligned}
$$

where $k_{i}$ is the number of distinct values of $A$ in $S_{i}$.
Although the MDL discretization technique has the same theoretical basis as the MDL scoring function, it is otherwise unrelated. That is, using the MDL discretization does not favor the MDL scoring function over the others in any way.

We used a $k$ nearest neighbors ( kNN ) algorithm to impute missing values [39]. The kNN algorithm

Table 1 Summary of gold standard networks


This table describes all of the datasets we used in this study. Dataset gives the name of the dataset in the UCI machine learning repository. Domain gives a rough indication of the domain of the dataset. Instances gives the number of instances in the original dataset. Nodes gives the number of variables in the dataset (and the number of nodes in the corresponding Bayesian network). Edges gives the number of edges in the optimal Bayesian network learned from the original dataset. This is the gold standard network used throughout the rest of the evaluation. Average In - degree gives the average number of parents of each variable in the learned Bayesian network. computes a missing value $X_{p}$ for record $D_{i}$ by finding the $k$ closest $D_{i} \mathrm{~s}$ (out of those records which are not missing any values) to $D_{i}$ (using Euclidean distance, for example), excluding $X_{p}$. If $X_{p}$ is a continuous variable, the value of $X_{p}$ is averaged for each of the $D_{i} \mathrm{~s}$, and that value is assigned to $X_{p}$ for $D_{i}$. If categorical, it is replaced by a majority vote among the $k$ closest neighbors for $X_{p}$. We set $k=5$. After processing the datasets, we applied an optimal learning algorithm based on the MDL scoring function [17] to learn optimal Bayesian networks. Again, the use of MDL score here does not affect the conclusions of this study, as other scoring functions yielded similar results. We used the maximum likelihood estimation method to learn the parameters of the networks. We took the learned networks as the gold standard networks and generated datasets from them.

## Generating datasets from gold standard networks

After we created the gold standard networks, we generated datasets for each of these Bayesian networks with different numbers of data points ranging from 200 and 1000 (with increments equal to 200) and from 1,000 and 10,000 (with increments equal to 1,000), for a total of 18 sample sizes for each gold standard network. Each data point in a dataset corresponds to one random sample drawn from the joint probability distribution of a Bayesian network using logic sampling [40]. The basic idea is to sample the value for each variable according to the conditional probability distribution of the variable given its parents. The sampling is performed in a topological order of all the variables in order that all the parents already have sampled values before the child variable is sampled.

## Learning from the sampled datasets

After generating datasets from the gold standard networks, we learned optimal networks for all the datasets by using the aforementioned scoring metrics. MDL, AIC and fNML are parameterless, so we learned one network for each combination of scoring function and dataset. All optimal learning algorithms would learn an equivalent network, so our choice of optimal learning algorithm does not affect the learned network. We tried the following $\alpha$ values, $0.1,0.5,1,5,10,20,50,80,100$, for the hyperparameter $\alpha$ of BDeu and learned a network for each combination of $\alpha$ value and dataset. Thus, in total, we learned 12 "optimal" networks for each dataset and sample size. For comparison, we also tested a greedy hill climbing algorithm with random restarts and a tabu list in the same experiments.

## Evaluating the learned networks

We used several structural evaluation metrics to compare the performance of the different scoring functions. Three of the evaluation metrics operate directly on the gold standard and learned DAG structures: accuracy, sensitivity, and average hamming distance (AHD). The formulas for those metrics are

$$ \begin{aligned} & \text { Accuracy }=\frac{T P+T N}{T P+T N+F P+F N} \ & \text { Sensitivity }=\frac{T P}{T P+F N} \ & A H D=\frac{F P+F N}{n} \end{aligned} $$

where a $T P$ is an edge in the correct direction in the learned network, a $T N$ is an edge in neither the learned

nor the gold standard network, a $F P$ is an edge in the learned network but not in the gold standard network, and a $F N$ is an edge in the gold standard but not in the learned network. Note that an edge in the wrong direction in the learned network counts as both a $F P$ and a FN.

We also used an evaluation metric called structural Hamming distance (SHD). As mentioned earlier, multiple structures with edges in different directions may belong to the same equivalence class. Intuitively, the distance between Bayesian networks in the same equivalence class should be zero. To accommodate this, SHD first identifies the equivalence class to which a Bayesian network belongs using an algorithm given by Chickering [28]. An equivalence class is represented by a partially directed graph (PDAG) in which some edges are directed and some undirected. The undirected edges can be orientated arbitrary as long as no new V structure in which multiple variables share a child is introduced. SHD then counts the number of directed and undirected edge additions, deletions, reversals and changes in direction to transform one PDAG into the other as the distance between two corresponding Bayesian networks. Tsamardinos et al. [41] provide a more formal algorithm for computing the SHD metric.

## Results

In this section, we present the results of our empirical study. We first compared the evaluation metrics in order to select one metric for further analysis. We next looked into the effect of the hyperparameter $\alpha$ on the BDeu score. We then compared the capability of the scoring functions in recovering the Bayesian network structures from the sampled datasets generated from the gold standard Bayesian networks. After that, we compared the effect of sample sizes on the performance of the scoring functions in learning from the datasets when using both an optimal learning algorithm and a greedy hill climbing algorithm.

## Comparison of evaluation metrics

We first compared the robustness of the evaluation measures as the sample size increases in the datasets. Theoretically, as the number of data points increases, the bias introduced by the penalty term in a scoring function has decreasing effect, and the learned model should gradually converge to the equivalence class of the true underlying model [29]. Figures 1 and 2 show the convergence results for the scoring functions on the optimal networks learned for the Statlog (Australian CreditApproval) and Cleveland Heart Disease datasets respectively. We consider an evaluation measure to have converged when adding more data points does not change the value of the metric. Our results show that the SHD metric converges
for most of scoring functions with a small number of data points. In contrast, AHD, accuracy and sensitivity still fluctuate when there is a large number of samples. We only show the results on two datasets, but the results on the other datasets are similar. SHD exhibits better convergence behavior because it operates on the equivalence classes of networks rather than directly on the specific DAGs in question. As a simple example, suppose the gold standard network is $X \rightarrow Y$, but the learned network is $X \leftarrow Y$. The two networks represent the same conditional independencies, and SHD gives a distance of 0 . However AHD, accuracy, and sensitivity all consider the arc incorrect because the arcs are oriented in different directions. We therefore only use SHD for the rest of our analysis.

## BDeu parameterizations

We also investigated the effect of the hyperparameter $\alpha$ on BDeu. We focused on both the convergence behavior and the effect of $\alpha$ on recovering the gold standard networks. The results are shown in Figure 3 and Table 2. While some $\alpha$ values give good recovery results, it is clear that selecting either too low or too high of an $\alpha$ can dramatically impact the quality of the learned networks. BDeu was similarly impacted by $\alpha$ on other datasets as shown in the Additional File 1 S1.xls (sheet = results . optimal). On some of the networks, a poorly chosen $\alpha$ value may prevent convergence of the algorithms even when the sample size is large. As mentioned earlier, low $\alpha$ s tend to result in sparser networks than higher $\alpha$ s. Unfortunately, if the density of the gold standard network is unknown, selecting $\alpha$ is difficult. Consequently, BDeu is only a good scoring function if an expert can appropriately estimate $\alpha$. Otherwise, the learned network is either too sparse (if $\alpha$ is too low) or too dense (if $\alpha$ is too high). This analysis supports previously published results [35].

## Gold standard network recovery

We studied the capability of each scoring function in recovering the gold standard network based on the SHD metric. In the case of BDeu, we show the behavior of the best performing $\alpha$ value. Figure 4 shows that most of the scoring functions can recover the gold standard network on four of the datasets given a large enough sample size and appropriate parameters ( $\alpha$ for BDeu). Other datasets exhibit similar behavior as shown in Table 3 and the Additional file 1 S1.xls (sheet = results . optimal). In particular, we consider the minimum distance of each scoring function and dataset. A minimum distance of 0 means that the gold standard network was recovered for the dataset. Small distances indicate that the scoring function guided the learning algorithm to find close to optimal networks.

![img-0.jpeg](img-0.jpeg)

**Figure 1 Comparing the evaluation measures for the optimal networks learned from the Austra datasets with different sizes.** In this figure, we compare the performance of the four evaluation metrics (SHD, AHD, accuracy, and sensitivity) for the *Australian Credit Approval* dataset. The y-axis label indicates which evaluation metric that graph displays. We display the results for α = 1 for BDeu for all measures because it had the best convergence behavior for this dataset. We used the behavior of each of the curves to evaluate the convergence of the corresponding scoring function. We consider a scoring function to have converged for an evaluation metric when increasing the dataset size does not change the value for that scoring function and evaluation metric. Thus, we look for "flat lines" in the graphs.

In contrast to the results reported by several previous studies, we found that MDL was able to recover the gold standard network more quickly than other scoring functions. We observe these differences both because we use an optimal learning algorithm and because we use gold standard networks representing real-world datasets. Given an appropriate α value, BDeu also converged to the gold standard networks within the sample sizes we tested. In some of the datasets, fNML converged to the gold standard network very quickly, but sometimes it converged to a different network. In contrast, AIC's behavior was much more erratic. It found the gold standard network on 8 of the datasets. But because of its high standard deviation, we infer it never completely converged. Figure 4 supports this conclusion. In light of these results, we conclude that MDL is a good scoring function because it often converges to the gold standard network. BDeu also exhibits good behavior if a suitable α is known before learning.

### Convergence behavior

Next, we studied the convergence behavior of each scoring function. We did not consider whether the scoring function converged to the gold standard network; rather, we only focused on whether the scoring function converged to *any* network. In essence, this part of our study investigates the effect of the size of a dataset on the scoring functions. We again consult Figure 4 and Table 3 but this time look for convergence of the scoring functions; that is, we look to see at what point increasing sampling size does not change SHD anymore. As the figure shows, most of the scoring functions converged. To look for convergence in the table, we consider the mean, minimum, maximum, and standard deviation for the SHD statistics. We expect that if the scoring function converged quickly, its standard deviation will be small. This loose interpretation is robust in that it allows us to conclude that a scoring function converged even if SHD changes slightly from one sample size to the next.

![img-1.jpeg](img-1.jpeg)

**Figure 2 Comparing the evaluation measures for the optimal networks learned from the Cleve datasets with different sizes**. In this figure, we compare the performance of the four evaluation metrics (SHD, AHD, accuracy and sensitivity) for the *Cleve* dataset.

As previously shown [7], fNML converges with fewer samples than the other scoring functions. Because the mean SHD is typically small, we conclude that the network to which it converges is often close to the gold standard network. MDL converged somewhat more slowly, but often converged to the gold standard network. BDeu with an optimal α value tends to converge quickly to a network close to the gold standard networks; however, with a sub-optimal α value, BDeu often neither converges nor comes close to the gold standard networks as shown in Table 2. Because AIC has a very low penalty term, more data encourages it to add more edges. Thus, it tends to overfit the data on large sample sizes and rarely converges. The SHD of AIC does tend to decrease as the sampling size increases, but that trend is somewhat inconsistent. Based on these results, fNML seems to be a good scoring function when data is limited, while MDL is superior when more data is present.

### Comparison to greedy hill climbing

Finally, we compared the network recovery and convergence ability of a greedy hill climbing learning algorithm to those from the optimal algorithm. We performed this analysis because, as mentioned, optimal learning algorithms are limited to datasets with several dozens of variables. While some biological datasets (such as the *Breast Cancer*, *Cleveland Heart Database*, *Diabetes*, *Starlog (Heart)*, *Hepatitis* and *Iris* datasets included in this study) are within this limit, many others, such as gene expression datasets, include hundreds or thousands of variables. Greedy hill climbing algorithms have been shown to scale to datasets of this size [14]. This part of our study verifies that our conclusions on scoring functions apply to this algorithm, as well.

We first evaluated the network recovery ability of the scoring functions on the greedy hill climbing algorithm. Table 4 shows that, much like the optimal learning algorithms, the hill climbing algorithm typically either adds extra edges or misses necessary edges. On the other hand, as the small values in the *Reverse* and *Compelled* columns show, the directionality of the edges is typically correct. The *Total* SHD follows a similar trend among the greedy hill climbing and optimal algorithms. That is, scoring functions that performed well for the optimal

![img-2.jpeg](img-2.jpeg)

**Figure 3** The effect of the hyperparameter α on the BDeu score. This figure plots the SHD between the networks learned by BDeu and the gold standard networks for six values of α for the *Breast*, *Glass*, *Diabetes*, and *Hepatitis* datasets. We used the behavior of each curve to evaluate both the convergence and the recovery ability of each value of α. We evaluate the recovery ability by considering both the smallest SHD for the scoring function, the size of the dataset which gives that SHD, and whether the scoring function converged to the smallest SHD, some other SHD or did not converge.

Algorithm also performed well for the hill climbing algorithm. We observed similar results on the other datasets as shown in the Additional file 1 S1.xls (sheet = results . greedy). These results confirm that the scoring functions have a similar impact on structure recovery regardless of whether an optimal or greedy algorithm is used. In almost all cases, though, the optimal algorithm finds a structure closer to the true gold standard networks, so its *Total* distance is always lower. This highlights the benefit of using optimal algorithms when possible.

We then evaluated the convergence behavior of the scoring function on the greedy hill climbing algorithm. As shown in Figure 5, the picture is not as clear as the convergence behavior of the optimal algorithm in Figure 4. Nevertheless, we still see similar trends. Of the scoring functions, fNML typically converges the quickest, though often to a worse network than MDL. On the *Breast Cancer* and *Car Evaluation* datasets, MDL converges to the gold standard network, except for a few perturbations caused by the uncertainty of the greedy search algorithm. BDeu also converges except for a few spikes, but it typically converges to a worse network than MDL. As with the optimal algorithm, AIC does not converge. These results also mirror those of the behavior we observed in the optimal algorithm, though a bit noisier. They again suggest that the conclusions we drew from the optimal algorithms apply to the greedy algorithm, albeit with some noise. We also see that the optimal algorithm gives more consistent behavior, both in terms of quality and consistent convergence, and should be used when possible.

#### **Conclusion**

In this work, we have empirically investigated the ability of four Bayesian network scoring functions (MDL, AIC, BDeu and fNML) to recover the generating distribution of a dataset; a gold standard Bayesian network represents

Table 2 Summary of the effect of different $\alpha$ values on the performance of BDeu


This table shows SHD statistics about the networks learned using the sampled datasets for the BDeu scoring function for all of the $\alpha$ values that we analyzed. GoldNet gives the name of the network. We have used abbreviated names from Table 1, but the order of the datasets is the same in both tables. Min, Mean, Max and STD give the particular statistic for SHD for all sample sizes for the given network and $\alpha$ value. The $\alpha$ value with the lowest mean for each dataset is shown in bold and marked with "*".

![img-3.jpeg](img-3.jpeg)

Figure 4 Plot of structural Hamming distance of the networks learned by optimal learning algorithm from datasets with different sample sizes. This figure plots the SHD of the networks learned by each of the scoring functions for the Breast, Crx, Car, and Diabetes datasets. We display the results for $\alpha=0.5$ for BDeu for all datasets because it had the best behavior in terms of SHD.

Table 3 A comparison of the performance of four scoring functions in recovering the true underlying Bayesian network structures


This table shows SHD statistics about the networks learned using the sampled datasets for all scoring functions that we analyzed. For BDeu, we used the value of $\alpha$ that gave the lowest mean SHD. GoldNet gives the name of the network. We have used abbreviated names from Table 1, but the order of the datasets is the same in both tables. Min, Mean, Max and STD give the particular statistic for SHD for all sample sizes for the given network and scoring function. The scoring function with the lowest mean for each dataset is shown in bold.

Table 4 A Comparison of Structural Error for the suboptimal learning algorithm and the optimal learning algorithm


This table gives detailed information about the structural differences between the learned and gold standard networks for the Statlog (Australian Credit Approval) and Credit Approval datasets. It shows differences for both the greedy hill climbing and the optimal learning algorithm. GoldNet gives the name of the network. Size gives the sample size. Score gives the scoring function. When only a number is shown, the scoring function is BDeu with that value for $\alpha$. Add gives the number of edges that were added to the learned network that were not in the gold standard network. Delete gives the number of edges that were not in the learned network which were in the gold standard network. Rev gives the number of edges that were oriented in the wrong direction in the equivalence class of the learned network compared to that of the gold standard network; that is, the number of edges that were reversed. Mis gives the number of edges that were either directed in the equivalence class of the learned network and undirected in that of the gold standard network, or vice versa; that is, it gives the number of mis-directed edges.

![img-4.jpeg](img-4.jpeg)

**Figure 5 Plot of structural Hamming distance of the networks learned by the sub-optimal learning algorithm from datasets with different sample sizes**. This figure plots the SHD of the networks learned by each of the scoring functions for the *Breast*, *Crx*, *Car*, and *Diabetes* datasets. We display the results for α = 0.5 for BDeu for all datasets because it had the best behavior in terms of SHD.

This distribution. We used an optimal structure learning algorithm to ensure approximation algorithms did not affect the learned networks. All optimal learning algorithms would learn an equivalent network, so our choice of optimal algorithm did not affect our results or conclusions. Then, we controlled scoring function and sample sizes to test their effect on the quality of the learned networks. We also considered four different evaluation metrics: accuracy, sensitivity, AHD and SHD. In addition, we evaluated a greedy hill climbing algorithm to ensure that our conclusions are valid for algorithms which can learn networks with hundreds or thousands of variables.

As a result of our investigation, we discovered that SHD is more well-behaved than the other evaluation metrics because it considers equivalence classes when comparing structures rather than the specific DAGs. Our most surprising result was that MDL was better able to recover gold standard networks than other scoring functions given sufficient data. As expected, BDeu's performance was highly dependent on the selected α parameter, which can be difficult to estimate *a priori*. We also confirmed that fNML converges even with few samples. Throughout our analysis, we found AIC's behavior erratic and unpredictable. The greedy hill climbing algorithm exhibited similar behavior, so we conclude that our results hold for this algorithm, as well.

We plan to extend this work in several ways. We can use synthetic networks to more carefully control the properties of our gold standard networks. Unlike previous studies, though, we will not rely on random network generation; instead, we will handcraft a variety of networks to reflect a variety of real-world datasets. We will also incorporate other scoring metrics, such as MIT [8], and objectives, such as prediction [9], into our study.

### Additional material

**Additional file 1: Detailed empirical results and free software packages**. The file (S1.xls) contains detailed empirical results from testing the various combinations of the scoring functions, sample sizes, and learning algorithms (sheet = results, optimal, results, greedy). It also contains a list of free software packages used in this study (sheet = Software).

## Acknowledgements

This research was supported by the NSF grants IIS-0953723 and EPS0903787. Some software packages that are used in this study are listed in the Additional File 1 S1.xls (sheet = Software).
This article has been published as part of BMC Bioinformatics Volume 13 Supplement 15, 2012: Proceedings of the Ninth Annual MCBIOS Conference. Dealing with the Omics Data Deluge. The full contents of the supplement are available online at http://www.biomedcentral.com/bmcbioinformatics/ supplements/13/515

## Author details

${ }^{1}$ Department of Computer Science and Engineering, Mississippi State University, Mississippi State, MS 39762, USA. ${ }^{2}$ Department of Epidemiology and Public Health, School of Medicine, Yale University, New Haven, CT 06511, USA. ${ }^{3}$ Department of Computer Science, Helsinki Institute for Information Technology, Fin-00014 University of Helsinki, Finland. ${ }^{4}$ Department of Computer Science, Queens College/City University of New York, Flushing, NY 11367, USA.

## Competing interests

The authors declare that they have no competing interests.

Published: 11 September 2012

## Submit your next manuscript to BioMed Central and take full advantage of:

- Convenient online submission
- Thorough peer review
- No space constraints or color figure charges
- Immediate publication on acceptance
- Inclusion in PubMed, CAS, Scopus and Google Scholar
- Research which is freely available for redistribution

Submit your manuscript at www.biomedcentral.com/submit
(3) BioMed Central