# Data-Driven Bayesian Network Learning: A Bi-Objective Approach to Address the Bias-Variance Decomposition 

Vicente-Josué Aguilera-Rueda * ${ }^{\circledR}$, Nicandro Cruz-Ramírez ${ }^{\circledR}$ and Efrén Mezura-Montes ${ }^{\circledR}$<br>Centro de Investigación en Inteligencia Artificial (CIIA), Universidad Veracruzana, Sebastián Camacho No. 5, Centro, Xalapa, Veracruz 91000, Mexico; ncruz@uv.mx (N.C.-R.); emezura@uv.mx (E.M.-M.)<br>* Correspondence: vaguilera@uv.mx

Received: 30 May 2020; Accepted: 19 June 2020; Published: 20 June 2020


#### Abstract

We present a novel bi-objective approach to address the data-driven learning problem of Bayesian networks. Both the log-likelihood and the complexity of each candidate Bayesian network are considered as objectives to be optimized by our proposed algorithm named Nondominated Sorting Genetic Algorithm for learning Bayesian networks (NS2BN) which is based on the well-known NSGA-II algorithm. The core idea is to reduce the implicit selection bias-variance decomposition while identifying a set of competitive models using both objectives. Numerical results suggest that, in stark contrast to the single-objective approach, our bi-objective approach is useful to find competitive Bayesian networks especially in the complexity. Furthermore, our approach presents the end user with a set of solutions by showing different Bayesian network and their respective MDL and classification accuracy results.


Keywords: Bayesian networks; Bias-Variance; NSGA-II

## 1. Introduction

Bayesian Network (BN) [1] is a preferred formalism to represent knowledge under uncertainty using efficient reasoning. BN stands as a popular tool for prediction, diagnosis, decision-making, control, and to attain a better understanding of phenomena amenable to modeling. Nevertheless, building a BN comes with inherent difficulties, such as deciding on the specific graph structure, and corresponding parameter values. Two traditional ways to build a BN structure are through (i) domain expertise and (ii) a data-driven inductive approach. The induction of a BN from data is subsequently classified into two types (i) methods searching for conditional-dependencies, also known as constraint-based methods and (ii) search and scoring based methods [2-5]. This study is based on the latter case, where the learning task is framed as a combinatorial optimization problem with two main components: (1) a metric to assess the quality of each BN candidate, and (2) a search procedure to move intelligently through the space of candidate networks.

In data-driven BN learning, it is common to implement metrics in the form of a penalized log-likelihood (LL) function. LL is the log probability of the data given a network structure. While adding an edge to a BN never decreases the likelihood -and hence irrelevant edges may be addedadding extra edges leads to two main problems: the overfitting problem [6], where good performance in the training data comes with poor performance on the testing data and the construction of a densely connected network, which involves an increase in the running time and a poor description of the phenomenon being modelled when the network is being used for data analysis [7]. In order to deal with these problems, a penalty term is used to avoid complex networks. Such, complex networks may have a low LL score value but overfit the model while a high penalty term may incur in models

that, on the other hand, underfit. The balance between the goodness of fit (measured as LL) and the complexity of a model is known as the bias-variance dilemma, decomposition or trade-off [8,9,10,11].

There are several decomposable penalized LL (DPLL) scoring functions for learning BN and are represented by the Akaike's information criteria (AIC) [12], the Bayesian Dirichlet with score equivalence and uniforms priors (BDeu) [13], the factorized normalized maximum likelihood (fNML) [14], the Bayesian information criterion (BIC), and the minimum description length (MDL) [15]. These metrics differ mainly in their penalty function. Additionally, for the latest two cases, the MDL objective is to determine the model that provides the shortest description of the data set and, although the principles of BIC are different in the practice, some authors assure that MDL is simply the additive inverse of the BIC [5,16].

This work is based on crude MDL as the scoring metric, which is a popular metric used to learn BN structures [17,18,19,20,21]. Grünwald [15] defines the crude MDL as the two-part version of MDL, where "crude" means that the complexity of a model is calculated considering its parameters but not its functional form. Some researches consider that crude MDL is able to recover a network with a good bias-variance tradeoff; however, other works consider that this version of MDL is not complete and it will not work as expected [4,10,15,22]. Some researchers point out that to the trade-off between accuracy, measured in terms of the LL, and complexity should be featured as a multi-objective problem [23,24,25,26,27]; however, in the context of BN, the study of this approach has not been extensively studied. Motivated by this, our work addresses the comparison of a single-objective versus a multi-objective approach for learning BN from data. The single-objective Genetic algorithm (GA) uses crude MDL whereas NS2BN is used to find an appropriate selection of networks with a trade-off between accuracy and complexity.

The remainder of this paper is structured as follows: Section 2 describes related work and motivates the work conducted in this paper. In Section 3, the background is described. Section 4 describes our approach in detail. Section 5 presents the experiments setup. Section 6 discusses the results. The concluding section summarizes the findings and gives an account for future work.

# 2. Related Work 

There exist two main approaches to the use of crude MDL to learn BN: (i) crude MDL to find the true model (that has given rise to the data), in our context it is the gold-standard network, and (ii) crude MDL to find a model with a good trade-off between the accuracy and complexity. Regarding the first approach, some of the most representative works are [4,28,29,30,31]. Regarding the second approach, some researchers assure that crude MDL is capable of finding a BN with a trade-off between the LL and the complexity, but not the gold-standard network [10,15,22,32,33]. As recent work in this approach, Cruz-Ramírez et al. [34], performed an exhaustive experiment with four-node networks. Therefore, even though these results show how crude MDL produces well-balanced models in terms of complexity and log-likelihood, those experiments have a limited scope and they left for future work to explore the search procedure, which is an important factor that affects the final selection of the model.

Previous studies have tackled the BN model selection problem using evolutionary algorithms. In [35] a Genetic Algorithm (GA) with genotype representation was proposed. The algorithm uses MDL as the fitness function and the results were based on evaluating several new recombination operators that helped to evolve BNs in a Directed Acyclic Graph (DAG) search space. In [36], the performance of GAs with two univariate Exploratory Data Analysis (EDA) based algorithms were compared. Three different scoring functions were used and the results showed that EDAs are able to recuperate structure similar to the gold-standard network. Wong's works [37,38] are based on evolutionary programming to induce BN in a two-phase constraint-based method that yields models that predict more accurately in comparison with the previous work of Wong based on MDL as the fitness function. In [39], a novel algorithm based on immune binary particle swarm optimization and MDL as the fitness function was proposed. The experiments show advantages in the quality of the fitness function in a comparison between a Particle Swarm Optimization algorithm (PSO) and a GA. In [40], a hybrid algorithm between the maximal information coefficient and binary PSO was proposed. The experimental results show that

without a given node ordering, this algorithm has better performance than the other five of the state of the art algorithms.

Lastly, the work of Ross and Zuviria [41] uses a multi-objective genetic approach to learn dynamic Bayesian networks from data with a trade-off between likelihood and complexity. This work is focused on the modeling of biological phenomena that typically require low-connectivity networks. However, to the best of our knowledge, this work is the only one with multi-objective criteria learning. Although, it is in the context of dynamic BN.

In summary, crude MDL uses a weighted sum to combine the log-likelihood and the structural complexity, thus, the learning problem of BN using MDL as a metric has been dealt mainly as a singleobjective problem. However, we proved that one objective tends to dominate the search procedure and also add bias to the kind of result obtained [26].

# 3. Background 

This section presents the main concepts that supports this investigation: the BN mathematical representation, the minimum description length principle, and the multi-objective problem.

### 3.1. Bayesian Networks

A BN is a graphical model that represents a joint probability distribution over a set of random variables $\left\{X_{1}, \ldots, X_{n}\right\}$. BNs are represented as a pair $(G, \Theta)$, where the directed acyclic graph (DAG) is represented by $G=\left(U, E_{G}\right) ; U$ is the set of nodes or random variables, and $E_{G}$ is the set of arcs that represent the probabilistic relationship among these variables. The parents of $X_{i}$ are denoted $P A_{i} ; X_{i}$ is independent of its non-descendant variables given its parents. Thus, $\Theta$ is a set of parameters which quantifies the network. The joint probability distribution can be recovered from local conditional probability distributions as is shown in Equation (1).

$$
P\left(X_{1}, \ldots, X_{n}\right)=\prod_{i=1}^{n} P\left(X_{i} \mid P A_{i}\right)
$$

Bayesian network structure learning is the problem of learning a network structure from dataset $(D)$, where the data set is a particular instantiation of all the variables $\left\{X_{1}, \ldots, X_{n}\right\}$. MDL is a well-known score used to measure the goodness of a BN candidate [15]. The model learned under the MDL principle is expected to exhibit a trade-off between model accuracy and complexity, thus avoiding data overfitting. In this work, the Bayesian learning problem is treated as a multi-objective optimization problem that consists of searching for potential solutions exhibiting a balanced trade-off between accuracy and the complexity (defined formally in the next subsection).

### 3.2. Minimum Description Length

The crude definition of MDL [15] is of the form:

$$
\begin{gathered}
M D L=-\log P(D \mid \Theta)+\frac{k}{2} \log n \\
k=\sum_{i=1}^{m} q_{i}\left(r_{i}-1\right)
\end{gathered}
$$

where $D$ is the dataset, $\Theta$ represents the parameters of the model, $k$ is the dimension of the model, and $n$ is the sample size. The parameter $\Theta$ is the corresponding local probability distribution for each node in the network. The dimension of the model $(k)$ is given by Equation (3).

For the case of Equation (3), $m$ is the number of variables, $q_{i}$ is the number of possible configurations of $P A_{i}$ and $r_{i}$ is the number of values of the variable.

The first term of Equation (2) measures the accuracy of the model using $-\log P(D \mid \Theta)$ (represented as $f_{1}$ in the next section) and the second term measures the complexity using $\frac{1}{2} \log n$ (represented as $f_{2}$ in the next section). The complexity of a BN is proportional to the number of arcs, as shown in Equation (3).

Hence, metrics that incorporate these two terms are dealing with a multi-objective problem which may represent that while the accuracy is better the complexity increases.

# 3.3. Multi-Objective Optimization Problem 

According to Deb [42], a multi-objective optimization problem (MOOP) can be seen as a search problem that aims to minimize or maximize two (or more) objectives that are usually in conflict. Without loss of generality, a MOOP can be defined as: $\vec{f}(\vec{x})=\left[f_{1}(\vec{x}), f_{2}(\vec{x}), \ldots, f_{l}(\vec{x})\right]$ where $\vec{x}=$ $\left[x_{1}, \ldots, x_{n}\right] \in R$ is an $n$-variable decision vector, $\vec{f}$ is the set of objective functions to be minimized or maximized, and $l$ is the number of objectives (in our case, we have two objectives: the LL $f_{1}$ and the complexity $f_{2}$ ).

According to this idea, the following definitions are provided: a solution $x_{1}$ dominates a solution $x_{2}$ (denoted by $x_{1} \preceq x_{2}$ ) if the solution $x_{1}$ is not worse than $x_{2}$ in all objectives and it is better than $x_{2}$ in at least one objective. In MOOPs there is not a single optimal solution; conversely, we can find a set of solutions that have no other solution which dominates them when all objectives are currently considered. Hence, the set of non-dominated solutions is called Pareto optimal set, and the evaluations of each non-dominated solution in each objective function are known as the Pareto front.

Figure 1 shows a particular case of the Pareto front in the presence of two-objective functions.
![img-0.jpeg](img-0.jpeg)

Figure 1. The Pareto front of a set of solutions in a two-objective space.
Several techniques have been proposed to solve MOOP [43]. This work is based on an evolutionary algorithm, which has shown advantages over classical techniques.

## 4. Nondominated Sorting Genetic Algorithm for Learning Bayesian Networks (NS2BN)

NSGA-II is a fast elitist multi-objective evolutionary algorithm proposed by Deb et al. [42]. In NSGA-II the individuals are ordered into non-dominated sets called fronts. In the first front are those individuals that are not dominated by the solutions in the current population. Such solutions are removed from the population and the process is repeated so as to select the set of non-dominated solutions to get the second front, and so on. A rank based on the number of the front is assigned to each individual. Additionally, the crowding distance is computed for each individual. The crowding distance is used to know how close an individual is to its neighbors in the objective function space. The selection of parents is performed by using binary tournament based on the rank and the crowding distance. The selected parents generate offsprings through crossover and mutation operators.

This work presents a multi-objective approach by using NSGA-II. The aim is to deal with the BN learning structure problem as a multi-objective optimization problem. The likelihood and the complexity of the model are considered as the objectives to be optimized. The pseudocode of the proposed approach NS2BN is presented in the Algorithm 1.

```
Algorithm 1 NS2BN
    \(\mathrm{G}=0\) \{Generation\}
    Generate a population \(P\) of random solutions \(\vec{x}_{i}, \forall i, i=1, \ldots, P O P_{-} S I Z E\)
    Repair cycles of each \(\vec{x}_{i} \forall i, i=1, \ldots, P O P_{-} S I Z E\)
    Evaluate the fitness functions using the first and the second term of the Equation (2) of each
    \(\vec{p}_{i} \forall i, i=1, \ldots, P O P_{-} S I Z E\)
    while \(G \leq G_{\max }\) do
        Create an offspring population \(Q\) using: binary tournament selection, one-point crossover and
        bit inversion mutation.
        Repair cycles
        Evaluate the fitness functions using the first and the second term of the Equation (2) of each
        \(\vec{x}_{i} \forall i, i=1, \ldots, P O P_{-} S I Z E\)
        Combine parents and offspring populations \(R=P \cup Q\)
        Sort using non-dominated criterio
        Replacement
        \(G=G+1\)
    end while
```

For the implementation of NS2BN, the following features are highlighted, (i) due to the nature of the problem, the representation of individuals (BNs) is an adjacency matrix as can be seen in Figure 2, (ii) due to this representation, a repair operator to avoid cycles inspired on [44] is used (see Figure 3). This repair operator identifies cycles in three kinds of processes: self-cycles, by-cycles, and regular cycles. In the first one, the repair strategy is to replace the value along the diagonal, when the value is 1 by 0 . The second repair strategy fixes the bi-directional cycles that occurs when two nodes are seen to influence each other then the repair operator removes one of the arcs at random to resolve it; finally the regular cycles need to identify a path between nodes, the strategy is the same as the path-cyclic graphs, where one of the offending arcs is removed randomly. And, (iii) the fitness functions are defined by each term of Equation (2) and both are minimizations.

Regarding the total computational cost per iteration; to the cost of the base algorithm we add the cost of the repair operator, therefore our NS2BN algorithm is $\mathcal{O}\left(M N^{2}\right)+\mathcal{O}(N D)$, where; $M$ is the number objectives, $N$ is the population size and $D$ is the dimensionality of the individuals [42].
![img-1.jpeg](img-1.jpeg)

Figure 2. Example of an adjacency matrix and its corresponding BN.
![img-2.jpeg](img-2.jpeg)

Figure 3. The self-cycle (left), the path-cycle (center) and the regular-cycle (right).

# 5. Experimental Setup 

This section presents the experimental setup used to compare the resultant BN models in terms of the trade-off between LL and complexity. A set of twelve databases was used: (i) four synthetic databases with 6-nodes, in which all the random variables are binary; do not produce any qualitative impact on the results in comparison to non-binary variables [45]. Two of these databases were generated using a random probability distribution and the next two were generated with distribution $p=0.1$ that according to [45] changing the parameters to be high or low tends to produce low-entropy distributions which have more potential for data compression. Tetrad IV software [46] was used to generate synthetic databases with a specific distribution. (ii) Three databases of a well-known benchmark [47] and (iii) five databases from the UCI repository [48]. Table 1 shows a detailed description of each database.

Table 1. Databases used in the experiments.


A single objective Genetic Algorithm [49] (GABN) was adopted for comparison purposes. The individual representation consists of the same adjacency matrix above discussed; the fitness function is the crude MDL, as described in the previous Section 3.2. In this algorithm, binary tournament parent selection, one-point crossover and bit inversion mutation are employed.

Ten independent runs were made by each algorithm per database, with 20,000 evaluations each. The GABN finds a single network for each execution, the network with the best MDL is chosen as the "genetic solution", meanwhile, in NS2BN the result of a run is a set of solutions with a variety of accuracy and structural complexity measurements. Based on the fact that all solutions in the Pareto front are optima, a decision making process based on expert knowledge in the modeling field is required to choose the most suitable solution.

To carry out a comparison between the multi-objective approach and the single-objective approach the linear programming technique for multidimensional analysis of preference (LINMAP) was used [50]. In the LINMAP decision approach criterion, from the accumulated Pareto front of ten executions, the solution nearest to a reference point which is $(0,0)$ is chosen. To find this solution all the solutions were normalized and the Euclidean distances were computed between the reference point and each Pareto solution as is shown in Figure 4. The solution with the shortest Euclidean distance is referred to as the chosen solution in this work.

The experimentation is presented in three parts: (1) the chosen solution obtained by NS2BN and the single solution from the Genetic algorithm are compared in terms of their complexity, likelihood, MDL and the classification accuracy using 10-fold-cross-validation (See Equation (5), where CV is test error on $k$ th fold), (2) for the case of the databases in Table 1 from 1 to 6 , we measure how the probability distribution of the gold-standard network is different from the genetic solution; for this

computation the formulation of the Kullback Leibler distance (KLD) was used, see Equation (4). Finally, (3) the analysis of the plots of the accumulated Pareto fronts are discussed.

$$
D_{K L}(p \| q)=\sum_{i=0}^{N}\left(x_{i}\right) \log _{2}\left(\frac{p\left(x_{i}\right)}{q\left(x_{i}\right)}\right)
$$

where $q(x)$ is the approximation and $p(x)$ is the gold-standard network distribution that we are interested in matching $q(x)$. If the obtained value is equal to 0 means that the distributions perfectly match, otherwise, it can take values between 0 and $\infty$.

$$
C V=\frac{1}{K} \sum_{k=1}^{K} C V_{k}
$$

The parameter setting employed by NS2BN and the GA were tuning empirically. The parameters are as follows: $P O P_{-} S I Z E=100, G_{\max }=200, C=0.9$ and $M=0.3$.
![img-3.jpeg](img-3.jpeg)

Figure 4. Points in the Pareto front represent the trade-off between both objectives. The Euclidean distance was computed between each Pareto solution and the reference point $(0,0)$. The solution with the shortest distance was considered as the chosen one to be compared with the GABN solution.

# 6. Results 

Table 2 shows the results in terms of LL, complexity, and MDL for the chosen solution and the genetic solution. Additionally, the results in terms of the 10 -fold-cross-validation rate are presented in the column named "CV". A parametric t-test with $95 \%$-confidence was applied between the chosen solution and the genetic solution in terms of classification accuracy. Numbers in bold-face letters indicate that the difference between accuracies is significant and this accuracy is the best.

According to such a test, in five databases there were significant differences in favor of the NS2BN chosen solution. The rest of the results did not show significant differences, which means that genetic solutions do not have advantages or disadvantages in terms of classification. Since the genetic algorithm is searching the minimum value of MDL, the genetic solutions show a minor MDL in sixteen databases. However, one of the objectives is clearly affected in those results.

Figure 5d-f show how the genetic solution tends to choose solutions with a smaller log-likelihood but more complex, and a similar situation occurs in Figure 5g-i where the GABN chooses solutions less complex but with a worse log-likelihood value.

It is important to notice the prominence of the search procedure and all the elements associated with this. It may be necessary, in the case where the genetic algorithm tends to choose solutions with a smaller LL but more complex, to find the balance in the configuration parameters to have a balance

between exploration and exploitation. Other components that could be explored include genetic diversity, reinitialization, or self-adaptation, which we will leave for future work.

Regarding the sample size, Grünwald [15] points that crude MDL does not work well when the sample size is small or moderate and Hastie et al. [16] point out that a metric like crude MDL, in a finite sample, tends to select less complex models. Our results agree with Grünwald and in contrast to Hastie's et al, our work shows a bias when the sample size is greater in the Genetic Solution, which is used a weighted sum, since this solution tends to select a more complex model (see Figure 5b,c,e,f, Figure 6 f and Figure $7 \mathrm{~b}, \mathrm{c}$ ).

The experiments generated by a low-entropy distribution show, as was pointed by Cruz-Ramírez et al. [34] that the presence of noise rate affects the behavior of MLD, which tends to prefer the less complex models, even a network with no arcs. However, the results of the experiments with low entropy distribution show, regardless the sample size, solutions with better values in both terms in comparison with the solution provided by NS2BN (see Figure 5g-l).

Finally, Table 3 shows the results of the KLD computation. According to such a test, there were significant differences in ten databases in favor of the solution obtained by NS2BN, which means that the chosen solution is closest to the gold-standard network concerning the underlying distribution.

Table 2. Comparison between the NS2BN and the GABN solutions. Values in parentheses represent the standard deviation, for the case of -Log-Likelihood, complexity, and MDL the minimum value is in boldface. For the case of the CV, we carry out the t-test and values in boldface mean the significant best value found.


Table 2. Cont.


![img-4.jpeg](img-4.jpeg)

Figure 5. Accumulated Pareto front of the twelve first databases with 6-nodes, random probability distribution (RPD) and low-entropy probability distribution (LED). Gray stars-the accumulated front obtained by ten runs of NS2BN. Blue triangle-the golden-standard network. Pink square-the GABN solution and then green circle-the chosen solution from the NS2BN Pareto front.

![img-5.jpeg](img-5.jpeg)

Figure 6. Accumulated Pareto front of the well-known benchmark databases with the different number of cases. Gray stars-the accumulated front obtained by ten runs of NS2BN. Blue triangle-the goldenstandard network. Pink square-the GABN solution and the green circle-the chosen solution from the NS2BN Pareto front.
![img-6.jpeg](img-6.jpeg)

Figure 7. Accumulated Pareto front of the UCI repository databases. Gray stars-the accumulated front obtained by ten runs of NS2BN. Pink square-the GABN solution and green circle-the chosen solution from the NS2BN Pareto front.

Table 3. Kullback-Leibler divergence computed between the gold-standard network with the GABN solution and the gold-standard network with the chosen solution of the NS2BN Pareto front. Values in boldface mean the best value found.


# 7. Conclusions and Future Work 

In this paper, a novel evolutionary bi-objective optimization approach for model selection of BN was presented. The accuracy and the complexity, which are related to bias and variance respectively, were adopted as the objectives to be optimized so as to obtain models with an acceptable generalization performance. A set of trade-off solutions was obtained per database. A solution nearest to the origin was chosen as a competitive solution with a suitable trade-off between the objectives. This chosen solution was compared with a single-objective solution. The chosen solution achieved competitive results, especially in complexity. It is important to note, that one of the main advantages of this approach is the set of trade-off solutions and that the selection of a model can be a high-level decision and must be performed by a domain expert of the modeling phenomenon. Additional advantages are that the proposed method can be applied to a databases from different domains and can be extended to other models such as artificial neural networks. As future work, different methods can be used to control (adapt or self-adapt) the algorithms parameters. Also, alternatives to reduce the computational cost of the algorithm can be included.

Author Contributions: Conceptualization, V.-J.A.-R. and N.C.-R.; investigation, V.-J.A.-R.; methodology, V.-J.A.-R., N.C.-R., and E.M.-M.; supervision, N.C.-R., and E.M.-M.; writing-draft V.-J.A.-R. All authors have agreed to the published version of the manuscript.
Funding: This research received no external funding.
Acknowledgments: The first author acknowledges support from the Mexican Council for Science and Technology (CONACyT) through a scholarship to pursue graduate studies at the University of Veracruz.
Conflicts of Interest: The authors declare no conflict of interest.
