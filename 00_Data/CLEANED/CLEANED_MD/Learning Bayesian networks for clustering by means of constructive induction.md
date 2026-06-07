# Learning Bayesian networks for clustering by means of constructive induction 

J.M. Peña, J.A. Lozano, P. Larrañaga

Intelligent Systems Group, Department of Computer Science and Artificial Intelligence, University of the Basque Country, P.O. Box 649, E-20080 Donostia-San Sebastián, Spain

The purpose of this paper is to present and evaluate a heuristic algorithm for learning Bayesian networks for clustering. Our approach is based upon improving the Naive-Bayes model by means of constructive induction. A key idea in this approach is to treat expected data as real data. This allows us to complete the database and to take advantage of factorable closed forms for the marginal likelihood. In order to get such an advantage, we search for parameter values using the EM algorithm or another alternative approach that we have developed: a hybridization of the Bound and Collapse method and the EM algorithm, which results in a method that exhibits a faster convergence rate and a more effective behaviour than the EM algorithm. Also, we consider the possibility of interleaving runnings of these two methods after each structural change. We evaluate our approach on synthetic and real-world databases.

## 1. Introduction

From the point of view adopted in this paper, data clustering (Duda and Hart, 1973; Hartigan, 1975; Kaufman and Rousseeuw, 1990) may be defined as the inference of a probability distribution for a database. We assume that, in addition to the observed variables, there is a hidden variable. This last unobserved variable would reflect the cluster membership for every case in the database. Thus, the clustering problem is also referred to as an example of learning from incomplete data due
to the existence of such a hidden variable. In this paper, we focus on learning Bayesian networks for clustering.

In the last few years, several methods for learning Bayesian networks have arisen (Cooper and Herskovits, 1992; Heckerman et al., 1995; Pazzani, 1996b), some of them even for learning from incomplete data (Cheeseman and Stutz, 1995; Friedman, 1998; Meilä and Heckerman, 1998; Thiesson et al., 1998). A key step in the Bayesian approach to learning graphical models in general and Bayesian networks in particular is the computation of the marginal likelihood of a database given a model structure. This quantity is the ordinary likelihood of the database averaged over the parameters with respect to their prior distribution. When dealing with incomplete data, the

exact calculation of the marginal likelihood is typically intractable (Cooper and Herskovits, 1992), thus, we have to approximate such a computation (Chickering and Heckerman, 1997). The existing methods are rather inefficient for our purpose of eliciting a Bayesian network from an incomplete database as they do not factor into separate marginal likelihoods for each family (a node and its parents).

To avoid this problem, we develop an algorithm for learning Bayesian networks for clustering based upon an adaptation of the work done in (Thiesson et al., 1998). We search for parameter values for the initial structure by means of the EM algorithm (Dempster et al., 1977; McLachlan and Krishnan, 1997). This fact allows us to treat expected data as real data which results in the possibility of completing the database. Therefore, a score criterion that is both in closed and factorable form can be used. In addition, we propose an alternative approach to fulfill the task of the EM algorithm which reveals a faster and more effective method: an alternation of the Bound and Collapse method (Ramoni and Sebastiani, 1997, 1998) and the EM algorithm. We also consider the possibility of interleaving one of these two methods (the EM algorithm or the alternative approach) after each structural change to improve the set of parameter values for the new structure.

The remaining part of this paper is structured as follows. In Section 2, we describe Bayesian networks. Section 3 is dedicated to explaining our heuristic algorithm in detail. In Section 4, we present some experimental results. Finally, in Section 5 we draw conclusions.

## 2. Bayesian networks

We follow the usual convention of denoting variables with upper-case letters and their states by the same letters in lower-case. We use a letter or letters in bold-face upper-case to designate a set of variables and the same bold-face lower-case letter or letters to denote an assignment of state to each variable in a given set. We use $p(\boldsymbol{x} \mid \boldsymbol{y})$ to denote the probability that $\boldsymbol{X}=\boldsymbol{x}$ given $\boldsymbol{Y}=\boldsymbol{y}$. We also use $p(\boldsymbol{x} \mid \boldsymbol{y})$ to denote the probability distribution
(mass function as we restrict our discussion to the case where all the variables are discrete) for $\boldsymbol{X}$ given $\boldsymbol{Y}=\boldsymbol{y}$. Whether $p(\boldsymbol{x} \mid \boldsymbol{y})$ refers to a probability or a probability distribution should be clear from the context.

Given an $n$-dimensional variable $\boldsymbol{X}=\left(X_{1}, \ldots\right.$, $X_{n}$ ), a Bayesian network (BN) for $\boldsymbol{X}$ is a graphical factorization of the joint probability distribution of $\boldsymbol{X}$. A BN is defined by a directed acyclic graph $\boldsymbol{b}$ (model structure) determining the conditional independencies among the variables of $\boldsymbol{X}$ and a set of local probability distributions. When there is in $\boldsymbol{b}$ a directed arc from a variable $X_{j}$ to another variable, $X_{i}, X_{j}$ is referred to as a parent of $X_{i}$. We denote the set of all the parents that the variable $X_{i}$ has in $\boldsymbol{b}$ as $\boldsymbol{P a}(\boldsymbol{b})_{i}$. The model structure yields to a factorization of the joint probability distribution for $\boldsymbol{X}$,
$p(\boldsymbol{x})=\prod_{i=1}^{n} p\left(x_{i} \mid \boldsymbol{p a}(\boldsymbol{b})_{i}\right)$,
where $\boldsymbol{p a}(\boldsymbol{b})_{i}$ denotes the configuration of the parents of $X_{i}, \boldsymbol{P a}(\boldsymbol{b})_{i}$, consistent with $\boldsymbol{x}$. The local probability distributions of the BN are those in Eq. (1). We assume that the local probability distributions depend on a finite set of parameters $\boldsymbol{\theta}_{\boldsymbol{b}} \in \boldsymbol{\Theta}_{\boldsymbol{b}}$. Therefore, Eq. (1) can be rewritten as follows:
$p\left(\boldsymbol{x} \mid \boldsymbol{\theta}_{\boldsymbol{b}}\right)=\prod_{i=1}^{n} p\left(x_{i} \mid \boldsymbol{p a}(\boldsymbol{b})_{i}, \boldsymbol{\theta}_{\boldsymbol{b}}\right)$.
If $\boldsymbol{b}^{b}$ denotes the hypothesis that the conditional independence assertions implied by $\boldsymbol{b}$ hold in the true joint distribution of $\boldsymbol{X}$, then we obtain from Eq. (2):
$p\left(\boldsymbol{x} \mid \boldsymbol{\theta}_{\boldsymbol{b}}, \boldsymbol{b}^{b}\right)=\prod_{i=1}^{n} p\left(x_{i} \mid \boldsymbol{p a}(\boldsymbol{b})_{i}, \boldsymbol{\theta}_{i}, \boldsymbol{b}^{b}\right)$.
In this paper, we limit our discussion to the case in which the BN is defined by multinomial distributions. That is, all the variables are finite discrete variables and the local distributions of each variable in the BN consist of a set of multinomial distributions, one for each configuration of the parents.

## 3. Learning BNs for clustering through constructive induction

### 3.1. The $B N$ structure that we aim to learn

Due to the difficulty involved in learning densely connected BNs and the painfully slow probabilistic inference when working with them, there has been a great interest in developing methods for learning the simplest models of BNs, e.g., Naive-Bayes (NB) models (Duda and Hart, 1973; Peot, 1996) and Tree Augmented Naive Bayes models (Friedman et al., 1997; Keogh and Pazzani, 1999). Despite the fact that these models are a weaker representation of some domains than more general BNs, the expressive power of these models is still recognized. Thus, these models are examples of a balance between efficiency and effectiveness, i.e., a balance between the cost of the learning process and the quality of the learnt model.

Keeping this idea in mind, we describe in this paper, a heuristic algorithm for learning BNs with a structure that can be considered as having an intermediate place in-between the NB model and the model with all the predictive variables fully correlated. By doing that we aim to keep the main features of both extremes: simplicity of the NB model and a better performance of the fully correlated model.

This class of models that we aim to learn was proposed by Pazzani (1996a,b) as a Bayesian classifier (supervised learning). In this paper, we extend these works by applying this class of models to perform data clustering. These models are very similar to the NB models, as all the attributes are independent given the class. In our approach, the only difference with the NB models is that the number of nodes in the structures of these models can be smaller than the original number of attributes in the database, as some attributes can be grouped together under the same node as fully correlated attributes (we refer to such nodes as supernodes). Therefore, this class of models ensures a better performance than the NB models while it keeps their simplicity. Hence, for the class of models that we learn, it follows that the probability of a case belonging to class
$c_{i}$, given the values of the attributes as $\boldsymbol{x}=$ $2\left(x_{1}, \ldots, x_{n}\right)$, is

$$
\begin{aligned}
& p\left(c_{i} \mid \boldsymbol{x}, \boldsymbol{\theta}_{\boldsymbol{k}}, \boldsymbol{b}^{h}\right) \\
& \quad \propto p\left(c_{i} \mid \boldsymbol{\theta}_{c}, \boldsymbol{b}^{h}\right) \prod_{j=1}^{r} p\left(\boldsymbol{x}^{j} \mid c_{i}, \boldsymbol{\theta}_{j}, \boldsymbol{b}^{h}\right)
\end{aligned}
$$

where $\left\{\boldsymbol{x}^{1}, \ldots, \boldsymbol{x}^{r}\right\}$ is a partition of $\boldsymbol{x}, r$ being the number of nodes (including the special nodes referred to as supernodes). Each $\boldsymbol{x}^{j}$ is, if the node $j$ is a supernode, the set of values in $\boldsymbol{x}$ for the original attributes grouped together under the supernode $j$, else it is the value in $\boldsymbol{x}$ for the attribute $j$.

### 3.2. A heuristic algorithm for learning BNs for clustering

In the remaining part of this paper we adopt the common Bayesian approach to learning BNs. We introduce the log relative posterior probability of model structure as the score criterion to evaluate each model structure with respect to the data. Then, we search for the best model structure from among all possible models, according to this score criterion (model selection),

$$
\begin{aligned}
\log p\left(\boldsymbol{b}^{h} \mid \boldsymbol{d}\right) & \propto \log p\left(\boldsymbol{d}, \boldsymbol{b}^{h}\right) \\
& =\log p\left(\boldsymbol{b}^{h}\right)+\log p\left(\boldsymbol{d} \mid \boldsymbol{b}^{h}\right)
\end{aligned}
$$

Assuming uniform model structure priors, this criterion is reduced to the log marginal likelihood, $\log p\left(\boldsymbol{d} \mid \boldsymbol{b}^{h}\right)$ (Eq. (5)).

Under the assumptions that (i) the variables in the database are discrete, (ii) cases occur independently, (iii) the database is complete and (iv) the prior distribution of the parameters given a structure is uniform, the marginal likelihood has a closed form for BNs, which allows us to compute it efficiently. In particular, assuming uniform model structure priors, we have
$p\left(\boldsymbol{d} \mid \boldsymbol{b}^{h}\right) \propto \prod_{i=1}^{n} \prod_{j=1}^{q_{i}} \frac{\left(r_{i}-1\right)!}{\left(N_{i j}+r_{i}-1\right)!} \prod_{k=1}^{r_{i}} N_{i j k}!$
where $n$ is the number of variables, $r_{i}$ the number of states that the variable $X_{i}$ can have, $q_{i}$ the number of states that the parent set of $X_{i}$ can have, $N_{i j k}$ the number of cases in the database where $X_{i}$

has its $k$ th value and the parent set of $X_{i}$ has its $j$ th value and $N_{i j}=\sum_{k=1}^{r_{i}} N_{i j k}$ (see (Cooper and Herskovits, 1992) for a derivation).

An important feature of the log marginal likelihood is that it factors into scores for families (under the assumptions described above). When a criterion is factorable, search is more efficient because we need not reevaluate the criterion for the whole structure from anew when only the factors of some families have changed.

When the variable that we want to classify is hidden, the assumption that the data is complete does not hold. When data is incomplete, the exact calculation of the log marginal likelihood is typically intractable (Cooper and Herskovits, 1992), thus, we have to approximate such a computation (Chickering and Heckerman, 1997). However, the existing methods for doing that are rather inefficient for our purpose of eliciting the BN structure from an incomplete database as they do not factor into scores for families.

To avoid this problem, we introduce our heuristic algorithm. A schematic of this algorithm for learning BNs for clustering is shown in Fig. 1. First, the algorithm chooses initial structure and parameter values. Then, it performs a parameter search step to improve the set of parameters for the current structure. These parameter values are used to complete the database. Doing so, we treat expected data as real data. Hence, the log marginal likelihood can be calculated using Eq. (6) in closed form. Furthermore, the factorability of Eq. (6) allows to perform an efficient structure search step.

After this step, the algorithm reestimates the parameters for the new structure that it finds to be the maximum likelihood parameters given the complete database. Finally, the probabilistic inference process to complete the database and the structure search step are iterated until no change in the structure occurs. We consider the possibility of interleaving the parameter search step after each structural change.

Notice should be taken of the importance of the built-in penalty term for complexity that the log marginal likelihood has. This term makes our algorithm able to avoid very complex models such as the fully correlated model. In (Meilä and Heckerman, 1998), we find a similar use of this built-in penalty term.

### 3.2.1. Parameter search

To fulfill the parameter search step, we consider two procedures: the EM algorithm and a new method that we present below.

The well-known EM algorithm (Dempster et al., 1977; McLachlan and Krishnan, 1997) is an iterative method to compute maximum a posteriori and maximum likelihood parameters from incomplete data. The EM algorithm finds a local maximum for the parameters. As the convergence rate of the EM algorithm is painfully slow, we present an alternative approach to carry out the task of the EM algorithm. In the remaining part of this paper we refer to this method as $\mathrm{BC}+\mathrm{EM}$ as it alternates between the Bound and Collapse (BC) method and the EM algorithm.

1. choose initial structure and initial set of parameter values for the initial structure
2. parameter search step
3. probabilistic inference to complete the database
4. calculate sufficient statistics for computing the $\log p\left(\mathbf{d} \mid \mathbf{b}^{h}\right)$
5. structure search step
6. reestimate parameter values for the new structure
7. if no change in the structure has been done
then stop
else if interleaving parameter search step
then go to 2
else go to 3 .

Fig. 1. A schematic of the algorithm for learning BNs for clustering.

The BC method (Ramoni and Sebastiani, 1997, 1998) is a deterministic method to estimate conditional probabilities from incomplete databases. It bounds the set of possible estimates consistent with the available information by computing the minimum and the maximum estimate that would be obtained from all possible completions of the database. These bounds that determine a probability interval are then collapsed into a unique value via a convex combination of the extreme points with weights depending on the assumed pattern of missing data (see (Ramoni and Sebastiani, 1998) for further details). This method presents all the advantages of a deterministic method and a dramatic gain in efficiency when compared with the EM algorithm.

The BC is described to be used in the presence of missing data, but it is not useful when there is a hidden variable, as in the clustering problem. The reason for this limitation is that the probability intervals returned by the BC method would be too wide and poorly informative, as all the missing entries are concentrated in a single variable. The $\mathrm{BC}+\mathrm{EM}$ method overcomes this problem by performing a partial completion of the database at each step (see Fig. 2).

For every case $\boldsymbol{x}$ in the database, the $\mathrm{BC}+\mathrm{EM}$ uses the current parameter values to evaluate the posterior distribution of the class variable given $\boldsymbol{x}$. Then, it assigns the case $\boldsymbol{x}$ to the class with the highest posterior probability only if this posterior probability is greater than a threshold (which is
called fixing probability threshold) that the user must determine. The case remains incomplete if there is no class with posterior probability larger than the threshold. As some of the entries of the hidden variable have been completed during this process, we hope to have more informative probability intervals when running the BC. Then, the EM algorithm is executed to improve the parameter values that the BC have returned. The process is repeated until convergence.

### 3.2.2. Structure search

The heuristic that we have presented in Fig. 1 is based upon the work done by Pazzani (1996a,b). Our heuristic algorithm learns BNs for clustering as a result of improving the NB model by searching for dependencies among attributes. In order to find the dependencies, the algorithm performs constructive induction (Arciszewski et al., 1995), which is the process of changing the representation of the cases in the database by creating new attributes (supernodes) from existing attributes. As a result, some violation of conditional independence assumptions made by the NB model are detected and dependencies among attributes are included in the model. Therefore, we reach a better performance while the model that we obtain after the constructive induction process keeps the simplicity of the NB model. We use the term joining to refer to the process of creating a new attribute whose values are the Cartesian product of two other attributes.

1. for every case $\mathbf{x}$ in the database do
a. calculate the posterior probability distribution $p\left(c \mid \mathbf{x}, \boldsymbol{\theta}_{\mathbf{b}}, \mathbf{b}^{h}\right)$
b. let $p_{\max }$ be the maximum of $p\left(c \mid \mathbf{x}, \boldsymbol{\theta}_{\mathbf{b}}, \mathbf{b}^{h}\right)$ which is reached for $C=c_{\max }$
c. if $p_{\max }>$ fixing_probability_threshold then assign the case $\mathbf{x}$ to the class $c_{\max }$
2. run the BC method
a. bound
b. collapse
3. set the parameter values for the current structure to be the BC's output parameter values
4. run the EM algorithm until convergence
5. if $\mathrm{BC}+\mathrm{EM}$ convergence
then stop
else go to 1 .

Fig. 2. The BC + EM method.

1. consider joining each pair of attributes
2. if there is an improvement in the $\log p\left(\mathbf{d} \mid \mathbf{b}^{h}\right)$ then make the joint that improves the $\log p\left(\mathbf{d} \mid \mathbf{b}^{h}\right)$ the most else return the current case representation.

Fig. 3. A template for the forward structure search step.

The algorithm for learning BNs for clustering of Fig. 1 starts from one of two possible initial structures: from the NB model or from the model with all the variables fully correlated. When considering the NB model as the initial structure, the heuristic algorithm performs a forward structure search step (see Fig. 3). When starting from the fully correlated model, the heuristic algorithm performs a backward structure search step (see Fig. 4).

In addition to the hill-climbing search proposed by Pazzani, we also introduce a global search algorithm as Simulated Annealing (SA) (Kirkpatrick et al., 1983) in our evaluation due to the obvious limitations of a local search algorithm as hillclimbing.

In our case, a solution of SA is a model structure and the neighbourhood of solutions for the current one consists of all the solutions that can be obtained from the current one either by joining any pair of attributes or by splitting any attribute at any possible point. We use a slow cooling schedule with initial temperature $\left(T_{0}\right)$ equal to 25 . For each temperature $T_{k}$, we assume that the equilibrium is achieved after visiting 50 solutions, then we apply the temperature reduction function $T_{k+1}=0.95 \cdot T_{k}$. The stopping criterion is satisfied when 100 consecutive iterations without changing the current solution are performed. Obviously, the score that we use to guide the search is the log marginal likelihood of the model structure. We do
not consider the interleaving of parameter search steps after each structural change in order not to enlarge the long runtime of SA. So, it is senseless to compare the results obtained by SA when the EM algorithm is used and when the $\mathrm{BC}+\mathrm{EM}$ method is used as they are only used to improve the parameter values of the initial solution and SA does not depend on the initial solution (assuming a proper cooling schedule).

## 4. Experimental results

Table 1 summarizes the criteria that we use to compare the learnt models. As we have discussed, the log marginal likelihood criterion is used to select a good model structure. We use this score in our comparisons as well. In addition to this, we consider the runtime as valuable information. For the synthetic databases (where the original models are available), we give special importance to the fraction of the nodes in the final BN which were correctly guessed, as it reflects the reliability of our algorithm for learning BNs for clustering.

For both the EM algorithm and the $\mathrm{BC}+\mathrm{EM}$ method, the convergence criterion is satisfied when either the relative difference between successive values for the log marginal likelihood for the model structure is less than $10^{-6}$ or 150 iterations are reached.

1. consider splitting each attribute at each possible point
2. if there is an improvement in the $\log p\left(\mathbf{d} \mid \mathbf{b}^{h}\right)$ then make the split that improves the $\log p\left(\mathbf{d} \mid \mathbf{b}^{h}\right)$ the most else return the current case representation.

Fig. 4. A template for the backward structure search step.

Table 1
Performance criteria


All the experiments are run on a Pentium 233 MHz computer.

Notice should be taken that in all experiments, we assume that the number of classes is known, thus, we do not perform a search to identify the number of classes in the database.

### 4.1. Synthetic data

In this section, we describe our experimental results on synthetic data. We constructed 4 synthetic databases as follows. There were 20 predictive binary attributes involved and one 4 valued hidden class variable. In order to get the 4 databases, we simulated 4 BNs that had the same structure as the output models of the algorithm that we introduced in Section 3.2 (we refer to them as the original models). We constructed the structure of these 4 BNs as follows. First, we began with the NB model structure where all the 20 predictive variables were independent given the class. Then, we fixed the number of predictive attributes that we wanted to have in each of the 4 output models to be $20,14,10$ and 5 , respectively. Therefore, in the last 3 models, some of the 20 original predictive variables had to be grouped together under supernodes (constructive induction) as the Cartesian product of the original variables. We joined attributes at random until the final number of nodes that we wanted to have was reached. The local probability distributions for
the 4 original models were randomly generated. From each of these 4 networks, we sampled 8000 cases by means of the h_domain_simulate function provided by the software HUGIN API. ${ }^{1}$ Obviously, we discarded all the entries corresponding to the class variable. Finally, every entry corresponding to a supernode was replaced with as many entries as there were original attributes under this supernode. That is, we "decoded" the Cartesian product of original attributes for every entry in the database corresponding to a supernode.

The purpose of evaluating our heuristic algorithms on synthetic databases is to show (i) the reliability of the presented heuristic for learning BNs for clustering, (ii) the improvement in the log marginal likelihood when we learn BNs by means of our algorithm and (iii) the improvement in the performance when using the $\mathrm{BC}+\mathrm{EM}$ method instead of the EM algorithm.

As Table 2 shows, our algorithm, when performing forward structure search steps, most of the times, is able to reconstruct the original structure with high fidelity and reliability. Also, we can clearly see the improvement of the initial log marginal likelihood. Moreover, Table 2 compares

[^0]
[^0]:    ${ }^{1}$ We used HUGIN API in the implementation of our algorithm. The HUGIN API (Application Program Interface) is a library that allows a program to create and manipulate BNs.

Table 2 Performance of the algorithm for learning BNs for clustering on the 4 synthetic databases (averaged over 5 runs) when forward structure search steps are performed


Table 3
Performance of the algorithm for learning BNs for clustering on the 4 synthetic databases (averaged over 5 runs) when SA is used


the performance of the algorithm for learning BNs for clustering when using the EM algorithm as parameter search step and when using the $\mathrm{BC}+\mathrm{EM}$ method. As we can see in the 4 databases, the use of the $\mathrm{BC}+\mathrm{EM}$ method outperforms the use of the EM algorithm in terms of final log marginal likelihood, percentage of right guessed nodes and runtime when no interleaving is done.

It seems obvious to assume that better results will be reached by interleaving parameter search steps after each structural change than without. However, most of the times, the EM algorithm needs to be interleaved to approach the performance level that our algorithm exhibits when the $\mathrm{BC}+\mathrm{EM}$ method without interleaving after each structural change is used. Thus, the saving of runtime (between $50 \%$ and $78 \%$ ) and the gain in effectiveness that we reach when the $\mathrm{BC}+\mathrm{EM}$ method is used is clearly apparent.

Moreover, in Table 3 we present the results achieved by our heuristic algorithm when SA is used to perform the search. Comparing the results summarized in Table 2 with those presented in Table 3, we conclude that our approach performs surprisingly well. Despite being a global search algorithm, SA reveals a poor level of performance and appears to be unable to find better solutions than those achieved by the algorithm with forward structure search steps.

For the sake of brevity and due to the poor reliability and long runtime of our algorithm when using backward structure search steps, we do not present results. Thus, in the remaining part of this
paper only forward structure search steps are considered when using the hill-climbing search.

### 4.2. Real data

Another source of data for our evaluation consists of two well-known real-world databases from the Machine Learning Repository (Merz et al., 1997): the tic-tac-toe database ${ }^{2}$ and the nursery database. ${ }^{3}$ The past usage of both databases classifies them as paradigmatic domains for testing constructive induction methods. Obviously, for both databases we delete all the class entries.

Table 4 reveals the effectiveness of our algorithm when forward structure search steps are done, as can be derived from the improvement of the initial log marginal likelihood. These results also show the superiority of using the $\mathrm{BC}+\mathrm{EM}$ method over using the EM algorithm. For the tic-tac-toe database, better results are achieved with the $\mathrm{BC}+\mathrm{EM}$ method than with the EM algorithm and in a shorter runtime. For large databases as the nursery database, when the $\mathrm{BC}+\mathrm{EM}$ method shows all its advantages over the EM algorithm, making our algorithm able to reach better results with up to 11 times less runtime than when using the EM algorithm.

[^0]
[^0]:    ${ }^{2}$ This database contains 958 cases, each of them has 93 valued predictive attributes. There are 2 classes.
    ${ }^{3}$ This database consists of 12960 cases, each of them has 8 predictive attributes which have between 2 and 5 possible values. There are 5 classes.

Table 4
Performance of the algorithm for learning BNs for clustering on the 2 real-world databases (averaged over 5 runs) when forward structure search steps are performed


Table 5
Performance of the algorithm for learning BNs for clustering on the 2 real-world databases (averaged over 5 runs) when SA is used


The results that we present in Table 5 reinforce the good behaviour of our algorithm. Once again, SA is outperformed by the greedy algorithm with forward structure search steps which, moreover, requires less computational expense.

## 5. Conclusions

We proposed a new approach to perform data clustering. Our heuristic algorithm relied on treating expected data as real data and on constructive induction to improve the NB structure searching for dependencies among the attributes. In order to do that the EM algorithm played a very important role. Primarily, due to the slow convergence rate of the EM algorithm, we developed the $\mathrm{BC}+\mathrm{EM}$ method to fulfill the task of the EM algorithm.

Our experimental results suggested that the greedy algorithm for learning BNs for clustering with forward structure search steps performed really well, it even reached a better performance than when SA was used. Furthermore, these experimental results showed the substantial gain in
effectiveness and in efficiency that our algorithm reached when the $\mathrm{BC}+\mathrm{EM}$ method was used instead of the EM algorithm.

## Discussion

Hancock: How does your work compare with the structural EM algorithm that Friedman developed a few years ago? (Note of the editors: see (Friedman, 1998) in this paper.)

Peña: In some way this work can be seen as a structural EM algorithm, but there are a few differences. Our algorithm is limited to learn this class of models because it seems to be a balance between efficiency and effectiveness. Also, I think the structural EM takes account of all the possible ways in which the databases can be completed. We just complete them with the most probable values; we do not take account of all possible completions. And we give the choice of interleaving or not interleaving the parameter search step. I think, in the structural EM you do not have such a choice: interleaving is always

done. Moreover, we found that if we use the $\mathrm{BC}+\mathrm{EM}$ method, we can reach a very good performance without interleaving the parameter search step. In almost all the cases for which we evaluated our algorithm, we reached the best performance with the $\mathrm{BC}+\mathrm{EM}$ algorithm without interleaving, whereas in the EM algorithm interleaving must be performed to reach as good results as our algorithm without interleaving.

Hancock: My second question is about the experimental results. Can you give me some idea of how much structure you can reconstruct and for what fraction of the database you can do this?

Peña: We tested our algorithm on four synthetic databases generated with $20,14,10$ and 5 nodes. If there are fewer than 20 nodes, this means that there are some supernodes, because all the domains have 20 original attributes. In the case of 20 nodes, almost all the methods are able to recover the original structure. In the most difficult case we reach a performance of $75 \%$.

Hancock: Have you looked at what happens when you have extraneous structure or noise in the data?

Peña: Yes. That is why we tested the algorithm on the real world databases. The only problem is that we have to fix the probability threshold. We are now investigating if we can characterise in some way the behaviour of our algorithm.

## Acknowledgements

Jose Manuel Peña wishes to thank Dr. Dag Wedelin for his interest in this work. He made it possible to visit the Department of Computer Science of Chalmers University of Technology at Gothenburg, Sweden. This work was supported by the Spanish Ministerio de Educacion y Cultura under AP97 44673053 grant.
