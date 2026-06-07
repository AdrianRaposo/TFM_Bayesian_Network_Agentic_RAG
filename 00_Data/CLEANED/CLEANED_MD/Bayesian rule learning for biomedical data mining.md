# Bayesian rule learning for biomedical data mining 

Vanathi Gopalakrishnan*, Jonathan L. Lustgarten, Shyam Visweswaran and Gregory F. Cooper<br>Department of Biomedical Informatics, University of Pittsburgh, 200 Meyran Avenue Suite M-183, Pittsburgh, PA 15260, USA<br>Associate Editor: Thomas Lengauer


#### Abstract

Motivation: Disease state prediction from biomarker profiling studies is an important problem because more accurate classification models will potentially lead to the discovery of better, more discriminative markers. Data mining methods are routinely applied to such analyses of biomedical datasets generated from highthroughput 'omic' technologies applied to clinical samples from tissues or bodily fluids. Past work has demonstrated that rule models can be successfully applied to this problem, since they can produce understandable models that facilitate review of discriminative biomarkers by biomedical scientists. While many rule-based methods produce rules that make predictions under uncertainty, they typically do not quantify the uncertainty in the validity of the rule itself. This article describes an approach that uses a Bayesian score to evaluate rule models.


Results: We have combined the expressiveness of rules with the mathematical rigor of Bayesian networks (BNs) to develop and evaluate a Bayesian rule learning (BRL) system. This system utilizes a novel variant of the K2 algorithm for building BNs from the training data to provide probabilistic scores for IF-antecedent-THENconsequent rules using heuristic best-first search. We then apply rule-based inference to evaluate the learned models during 10-fold cross-validation performed two times. The BRL system is evaluated on 24 published 'omic' datasets, and on average it performs on par or better than other readily available rule learning methods. Moreover, BRL produces models that contain on average $70 \%$ fewer variables, which means that the biomarker panels for disease prediction contain fewer markers for further verification and validation by bench scientists.
Contact: vanathi@pitt.edu
Supplementary information: Supplementary data are available at Bioinformatics online.

Received on April 9, 2009; revised on December 11, 2009; accepted on January 5, 2010

## 1 INTRODUCTION

High-throughput 'omic' data that measure biomarkers in bodily fluids or tissues are accumulating at a rapid pace, and such data have the potential for the discovery of biomarkers for early diagnosis, monitoring and treatment of diseases such as cancer. Data mining methods that learn models from high-dimensional data are being increasingly used for the multivariate analyses of such biomedical datasets. Together with statistical univariate analyses, some insights into predictive biomarkers of disease states can be gleaned, though

[^0]the results may not generalize due to the small sizes of available training data, typically less than 200 samples.

Due to the large imbalance between variable dimensionality (several thousand) and the sample size (a few hundred), there is a need for data mining methods that can discover significant and robust biomarkers from high-dimensional data. Rule learning is a useful data mining technique for the discovery of biomarkers from highdimensional biomedical data. We have previously developed and applied rule learning methods to analyze 'omic' data successfully (Gopalakrishnan et al., 2004, 2006; Ranganathan et al., 2005). Rules have several advantages, including that they are easy for humans to interpret, represent knowledge modularly and can be applied using tractable inference procedures.

In this article, we develop and evaluate a novel probabilistic method for learning rules called the Bayesian rule learning (BRL) algorithm. This algorithm learns a particular form of a Bayesian network (BN) from data that optimizes a Bayesian score, and then translates the BN into a set of probabilistic rules. The use of the Bayesian approach allows prior knowledge (as probabilities) to be incorporated into the learning process in a mathematically coherent fashion. The possibility of over-fitting is attenuated by the incorporation of prior probabilities into the rule-discovery process. BRL outputs the predictive rule model with the best Bayesian score, which represents the probability that the model is valid given the data.

The remainder of the article is organized as follows. Section 2 presents the BRL algorithm and briefly reviews other popular rule learning methods. Section 3 describes the datasets and the experimental setup to evaluate BRL. Section 4 presents the results of applying BRL to 24 published 'omic' datasets, and compares its performance with multiple rule-learning algorithms. Section 5 presents our conclusions.

## 2 METHODS

In biomedical data mining, a typical task entails the learning of a mathematical model from gene expression or protein expression data that predicts an individual phenotype, such as disease or health. Such a task is called classification and the model that is learned is termed as a classifier. In data mining, the variable that is predicted is called the target variable (or simply the target), and the features used in the prediction are called the predictor variables (or simply the predictors). Rule learning is a useful technique for knowledge discovery from data that is discrete.

In this article, we present a Bayesian method for learning BNs and translating it into rules as shown in Figure 1. A rule model is a set of rules that together comprise a classifier that can be applied to new data to predict the target. The main contribution of this BRL method is its ability to quantify uncertainty about the validity of a rule model using a Bayesian


[^0]:    *To whom correspondence should be addressed.

![img-0.jpeg](img-0.jpeg)

Fig. 1. A BN structure learned by BRL on the acute lymphoblastic leukemia (ALL) versus acute myeloid leukemia (AML) dataset (Golub et al., 1999) and its equivalent set of rules. @Class refers to the target variable that can take on values of either 0 (ALL) or 2 (AML) in this example. Each rule is associated with statistics from the training data (see note 1 ).
score. This score is used for model selection. We now discuss in detail the BRL method. This algorithm learns BN models from the data and the model is then translated into a set of rules with associated statistics. ${ }^{1}$ These rules are mutually exclusive and exhaustive over the values of the predictor variables, and hence inference using these set of rules becomes trivial. Given a new test case, the rule that matches its values for the predictor variables is used to infer the value of the target variable.

### 2.1 Bayesian networks

A BN is a probabilistic model that consists of two components: a graphical structure and a set of probability parameters. The graphical structure consists of a directed acyclic graph, in which nodes represent variables and variables are related to each other by directed arcs that do not form any directed cycles. Associated with each node (let us call it a child node) is a probability distribution on that node given the state of its parent nodes, and all the probability distributions for all the nodes taken together provide a factored (and often concise) representation of the joint probability distribution over all the variables (Pearl, 1988). Learning a BN is a two-step process corresponding to learning the structure and the parameters of the model,

[^0]and several methods have been developed to automatically learn BNs from data (Neapolitan, 2004). Here, we use the Bayesian method called K2 (both the K2 scoring measure and the K2 forward stepping search heuristic) for learning BNs (Cooper and Herkovits, 1992).

The K2 scoring measure (Cooper and Herskovits, 1992) assumes that the variables are discrete, the cases (training examples) occur independently, there are number of cases that have variables with missing values ${ }^{2}$ and there is a uniform prior probability distribution over the space of all possible network structures. The K2 measure also assumes that every possible probability distribution over the values of a node given a state of its parents is equally likely (uniform). Under these assumptions, a closed form solution for the Bayesian score is given by the following equation (Cooper and Herskovits, 1992):

$$
P(D \mid M)=\prod_{i=1}^{n} \frac{1}{(N_{i j}+r_{i}-1)!} \prod_{k=1}^{r_{i}} N_{i j k}!
$$

where $M$ is the BN structure under consideration, $D$ the data used to learn $M, n$ the number of variables in $M, q_{i}$ the number of parent states of child variable $i, r_{i}$ the cardinality (number of values or states) of variable $i$ and $N_{i j k}$ the number of instances in the training database $D$ for which variable $i$ has the value $k$ and the parents of $i$ have the value state denoted by index $j$. Also, $N_{i j}$ is the sum over $k$ of $N_{i j k}$.

Since it is usually computationally intractable to search over all possible BN structures to locate the one with the highest score, a greedy search in the space of BNs is employed. The greedy search method used by K2 (Cooper and Herskovits, 1992), requires an ordering on the variables and a userspecified parameter for the maximum number of parents any variable in the network can have.

### 2.2 Bayesian rule learning

The BRL algorithm uses the score given by Equation (1) to learn simple BNs. In particular, (i) BRL considers constrained BNs where the BN consists of one child variable, which is the target to be predicted, and other variables are parents of it; (ii) only the target node is evaluated with the Bayesian score; and (iii) models are searched by utilizing a beam (memory of particular size) to store high-scoring BNs. The beam refers to a restricted memory size for storing BN structures and is implemented as a priority queue of fixed width (beam size), where BNs are stored according to their score. This reduces the memory requirement for heuristic, best-first search, by exploring only those BN structures that are high scoring, while at the same time providing the ability to improve upon greedy search with a beam size of 1 .

Using the constrained structure of the algorithm in Figure 2, as illustrated by the model shown in Figure 1, Equation (1) simplifies further to the following equation:

$$
P(D \mid M)=\prod_{j=1}^{q} \frac{(r-1)!}{\left(N_{j}+r-1\right)!} \prod_{k=1}^{r_{i}} N_{j k}!
$$

where $q$ is the number of joint parent states of the target variable, $r$ the cardinality (number of values or states) of the target variable and $N_{j k}$ the number of instances in the training database $D$ for which the target variable has the value $k$ and its parents have the joint value state denoted by index $j$. Also, $N_{j}$ is the sum over $k$ of $N_{j k}$.

Figure 1 depicts an example of BN structure $M$ learned by BRL, where @Class represents a target variable and two genes M23197_at and U46499_at are its parents. The values or expression of these genes influence the target class. Figure 1 depicts $M$ and the set of rules derived from $M$. A rule set is defined as the conditional probability, such as the conditional probability $P($ @ Class $\mid M 23197 \_a t, U 46499 \_a t)$ for all values of $M 23197 \_a t$

[^1]
[^0]:    ${ }^{1} \mathrm{CF}$ refers to certainty factor or degree of belief in the rule (Shortliffe et al., 1975; Heckerman, D., 1985), P, $P$-value from Fisher's exact test; TP, number of true positives (match both sides of the rule); FP, number of false positives (match rule antecedent, but not consequent); Pos, number of positive examples (match rule consequent); and Neg, number of negative examples (do not match rule consequent). Cost measures could be incorporated, but are not used for the experiments in this article.

[^1]:    ${ }^{2}$ Missing values can be accommodated by including an extra state for a missing value of a variable. That extra state can be labeled, for example, as 'missing'. Thus, a variable with two domain values (e.g. true and false) becomes a variable with three possible values (e.g. true, false and missing).

INPUT: Discrete predictor variables $\left(X_{1, n}\right)$ and target variable $(T)$, an upper bound MAX_CONJS on the number of parents that $T$ can have, beam-width $b$, and training data $D$ containing $m$ cases
OUTPUT: A disjunction of conjunctive probabilistic IF-THEN rules DEFINITIONS:
$M=$ Bayesian Network structure;
$P(D \mid M)=$ function that returns the Bayesian score (marginal likelihood) for model $M$ and data $D$;
$B=$ Beam of size $b$ that sorts models by their score in descending order;
$V=$ Set of all variables $X_{i}$;
$F=$ Priority queue containing final structures (that cannot be improved further by adding a single variable) sorted by their scores in descending order;
$A=$ Subset of $V$ containing $X_{i}$ already appearing in final structures; $\operatorname{Parent}(M)=$ function that returns the set of parents $X_{i}$ of $T$ in $M$. ALGORITHM:

1. Create model $M$ containing just target node $T$ and place $M$ on beam $B$.
2. $A=\{\}$
3. WHILE (Beam $B$ is not Empty AND $A \subset V$ ) DO:
4. $M \leftarrow$ Highest scoring model removed from $B$
5. $X=V-\left\{\right.$ parents $\left.(M) \cup A\} \quad{ }^{j *} X_{i} \operatorname{NOT}$ in $M$ or $\left.A^{*} /\right.$
6. Set score_improves $=$ false
7. IF ( $X$ not empty AND
$\left.\quad \mid \operatorname{parents}(M) \mid<\operatorname{MAX} \_C O N J S\right)$ THEN
8. FOR (Each $X_{i}$ in $X$ ) DO:
$M_{\text {new }} \leftarrow$ Add $X_{i}$ as parent of $T$ in $M$
IF (score $\left.M_{\text {new }} D\right)>$ score $(M, D)$ THEN
Place $M_{\text {new }}$ on $B$
Set score_improves $=$ true
ENDIF
ENDFOR
ENDIF
9. IF (score_improves is false) THEN

Place $M$ on $F$
$A=A \cup\{\operatorname{all} X_{i}$ in $M\}$
ENDIF
ENDWHILE
10. $M_{F} \leftarrow$ First model removed from priority queue $F$

FOR each possible joint state $j$ of values for all $X_{i}$ in $M_{F}$ FOR each possible value $k$ of target variable $T$
Calculate $\operatorname{CF}\left(R_{i k}\right)$ ENDFOR
Let $s=$ arsmax $_{i}\left(m a x_{i}\left(C F\left(R_{i k}\right)\right)\right)$
Output $R_{i k} m$ : IF ( $X_{i}$ in state $j$ ) THEN $T=s$ with $C F\left(R_{i k}\right)$ ENDFOR

Fig. 2. The BRL algorithm.
and $U 46499 \_s t$. In the example, each of the two genes can take on two discrete ranges of values. Hence, the total number of possible combinations of the values for the predictor variables is four (Rules 0-3).

The Bayesian score [Equation (2)] represents the joint probability of the model and the data under the assumption of uniform structure priors. Since $P(M \mid D) \propto P(D \mid M)$, given the assumption that all models are equally likely a priori, the Bayesian score can be directly utilized as a measure of model uncertainty and used to prioritize and select models. Breadth-first marker propagation (Aronis and Provost, 1997) is utilized to record the matching statistics (or counts) and greatly speeds up the calculations by requiring just one pass through the training data to record the counts. BRL is thus very efficient and runs in $O\left(n^{2} m\right)$ time given $n+1$ variables and $m$ training examples, using the default constant values for beam size $b$ and the maximum conjunct parameter MAX_CONJS, which are both user-specified.

The BRL algorithm is shown in Figure 2. It takes as input a set of input variables $X$, a target variable $T$, an upper bound on the number of parents that $T$ can have and training data containing vectors of values for $X$ 's and the corresponding value for $T$. The user can also provide a beam width $b$ that restricts the number of BNs that are in the priority queue. The default beam width is 1000 .

In Step 1, a BN containing just the target node with zero parents is created, and it is scored using Equation (2). Step 2 initializes the list of variables $X$ that appear in models that have good scores and cannot have a better score by the addition of any single parent of $T$. The loop condition in Step 3 checks to see whether there are still models on the beam that can be expanded further by the addition of a parent variable such that the score would improve. Steps 4-8
![img-1.jpeg](img-1.jpeg)

Fig. 3. Example of a BN (left) to a set of rules (right), where the CF is expressed as the likelihood ratio of the conditional probability of the target value given the value of its parent variable. As seen in Rule 1, the CF is the likelihood ratio $0.8 / 0.2=4$. The two rules in the middle are automatically pruned by BRL and only the higher CF rule for each unique rule antecedent is retained in the rule model.
perform one-step forward search by adding one more allowed variable as an additional parent of the target $T$ to the structure. Specialization refers to the addition of a parent variable (not already present) to the structure of current model, such that the total number of parent variables in the model does not exceed the upper bound MAX_CONJS. The default value we use for MAX_CONJS is 5 .

In Step 9, a check is made to see whether the score of the model removed from the beam improved after all one-step specializations. If not, that model is placed on a priority queue containing final model structures ordered according to their Bayesian scores. Even though we store many final models on the final priority queue, only the best scoring model is presented to the user in the form of a rule model in Step 10. For each value of target variable $T$, its probability given each state of possible values of its parent variables is calculated from the training data. The certainty factor is calculated as shown in Figure 3.

We perform a simple pruning in Step 10, wherein we output only the rule with the target value that has the highest probability given the particular state of its parent variables (Fig. 3). There are many other methods that could be used to perform pruning of the rules generated in Step 10, such as the number of training examples covered by the rule (Han and Kamber, 2006).

Also, we perform an optimization to increase search efficiency of the BRL algorithm. As can be seen in Step 9, the algorithm keeps track of those sets of variables that cannot be specialized further by addition of single variables as parents of the target such that the Bayesian score improves. The assumption is that if a predictor is in some final rule, then it is unlikely to be a strong predictor in another rule. While empirically, we observe that this assumption works well for most datasets that we have analyzed, it is certainly possible that there are datasets for which the assumption will not work well. Thus, extensions to this basic BRL algorithm can be explored along several directions to overcome some of the assumptions and limitations.

### 2.3 Rule learning methods

For our experiments we used three readily available rule learning methods: Conjunctive Rule Learner, RIPPER and C4.5. Conjunctive Rule Learner is a simple rule learner that learns a set of simple conjunctive rules that optimizes the coverage and predictive accuracy. It uses a technique called Reduced Error Pruning (Furnkranz and Widmer, 1994) to trim an initial set of rules to the smallest and simplest subset of rules that provide highest discrimination. Repeated Incremental Pruning to Produce Error Reduction (RIPPER) was developed by Cohen (1995) and uses the REP technique in Conjunctive Rule Learner, but performs multiple runs (Cohen, 1996). C4.5 is a decision tree learner developed by Quinlan (1994) that extends the basic decision tree learner ID3 (Quinlan, 1986) to improve classification. These improvements include parameterization of the depth of the decision tree,

rule post-pruning, ability to handle continuous-valued attributes, ability to choose the best attribute to use in growing the decision tree and an increase in computational efficiency (Gabrilovich and Markovitch, 2004; Xing et al., 2007).

### 2.4 Discretization

The rule learners described above require variables with discrete values. We used a new discretization method called heuristic efficient Bayesian discretization (EBD; Lustgarten, 2009), which we developed for transforming continuous data to discrete. EBD uses a Bayesian score to discover the appropriate discretization for a continuous-valued variable and runs efficiently on high-dimensional biomedical datasets. Compared with Fayyad and Irani's (FI) discretization method (Fayyad and Irani, 1993), which is an efficient method commonly used for discretization, EBD had statistically significantly better performance in the evaluation report in Lustgarten et al. (2008).

## 3 EXPERIMENTAL SETUP

### 3.1 Biomedical datasets

The performance of BRL and the three comparison rule learning methods were evaluated on 24 biomedical datasets [21 publicly available genomic datasets, two publicly available proteomic datasets from the Surface Enhanced Laser/Desorption Ionization Time of Flight (SELDI-TOF; Wright et al., 1999) mass spectrometry platform and one University of Pittsburgh proteomic dataset, which is a diagnostic dataset from a Amyotrophic Lateral Sclerosis study obtained using the SELDI-TOF platform]. The datasets, along with their type (prognostic/diagnostic), number of instances, number of variables and the majority target-value proportions are given in Table 1.

### 3.2 Data mining techniques and statistical analysis

As mentioned, for comparison, we used three rule learners, namely, Conjunctive Rule Learner, RIPPER and C4.5 as implemented in WEKA version 3.5.6 (Witten and Frank, 2005). We used two versions of BRL, namely, BRL (beam size set to 1 ) and BRL 1000 (beam size set to 1000). We used heuristic EBD for discretization; the discretization cutpoints were learned from the training set and then applied to both the training and test sets. We implemented EBD in Java, so that it can be used in conjunction with WEKA.

We evaluated the rule learning methods using 10 -fold crossvalidation performed two times. The methods were evaluated using two measures: balanced accuracy (BACC), which is the average of sensitivity and specificity over all one-versus-rest comparisons for every target value, and relative classifier information (RCI; Sindhwani et al., 2001). These measures are described below.

The BACC differs from accuracy in that it compensates for skewed distribution of classes in a dataset. BACC is defined as follows:

$$
\begin{aligned}
& \mathrm{BACC}=\frac{\sum_{c} \text { Sensitivity }(c)+\text { Specificity }(c)}{|C|} \\
& \text { Sensitivity }(c)=\frac{\mathrm{TP}_{(c) / 1}}{\mathrm{TP}_{(c) / 1}+\mathrm{FN}_{(c / c) / 1}} \\
& \text { Specificity }(c)=\frac{\mathrm{TN}_{(c / c) / c / 1}}{\mathrm{TN}_{(c / c) / c / 1}+\mathrm{FP}_{(c / c / c)}}
\end{aligned}
$$

where $C$ is the set of the target variable values, and Sensitivity (c) [Specificity(c)] refers to the sensitivity (specificity) of the target value $c$ versus all other values of the target. $\mathrm{TP}_{(c) / 1}$ is the number of

Table 1. Biomedical datasets used for the comparison experiments


In the type (T) column, P signifies prognostic and D signifies diagnostic. \#C represents the number of classes, \#A the number of attributes within the dataset, \#S the number of samples and $M$ is the fraction of the data covered by the most frequent target value. The first 21 datasets contain genomic data, whereas the last three datasets contain proteomic data.
samples predicted to have the value $c$ for the target variable given that the observed value is $c, \mathrm{FN}_{(c / c) / c}$ is the number of samples predicted to have a value other than $c$ for the target variable given that the observed value is $c, \mathrm{TN}_{(c / c) / c}$ is the number of samples predicted to have a value other than $c$ for the target variable given that the observed value is not $c$ and $\mathrm{FP}_{(c) \sim c}$ is the number of samples predicted to have the value $c$ for the target variable given that the observed value is not $c$.

RCI is an entropy-based performance measure that quantifies how much the uncertainty of a decision problem is reduced by a classifier relative to classifying using only the prior probability distribution of the values of the target variable uninformed by any predictor variables (Sindhwani et al., 2001). The minimum value for RCI is $0 \%$, which is achieved by a classifier that always predicts the majority target-value, and the maximum value is $100 \%$, which is achieved by a classifier with perfect discrimination. RCI is sensitive to the distribution of the target values in the dataset, and thus compensates for the observation that it is easier to obtain high accuracies on highly skewed datasets. Like the area under the receiver operating characteristic curve (AUC), RCI measures the discriminative ability of classifiers. We did not use AUC since there are several interpretations and methods to compute the AUC when the target has more than two values.

## 4 RESULTS

The average BACCs obtained from 10 -fold cross-validation performed two times for each of the 24 datasets are shown in Table 2.

Table 2. BACC from 10-fold cross-validation performed two times on the 24 datasets depicted along with the overall averages (AVG) and their SD


Averages over the genomic datasets $1-21$ (GA) and their SDs, as well as averages over the proteomic datasets $22-24$ (PA) and their SDs. Bold numbers indicate highest performance on a dataset.

As can be seen from the average BACCs for the 24 datasets, both $\mathrm{BRL}_{1}$ and $\mathrm{BRL}_{1000}$ clearly perform better than the other rule learning methods. This holds for both the genomic datasets (1-21) and the proteomic datasets (22-24).

We see that $\mathrm{BRL}_{1000}$ has the highest BACC on 15 datasets, while $\mathrm{BRL}_{1}$ has the highest BACC on 4 datasets. On the remaining five datasets, C4.5 has the highest BACC on three, ties with BRL on one and Conjunctive Rule Learner has the highest on one. Only the first dataset is very easy to classify by all rule learners. As seen in Table 3, the performance of both $\mathrm{BRL}_{1}$ and $\mathrm{BRL}_{1000}$ are statistically significantly better than C4.5, its nearest competitor in terms of BACC. When compared with each other, BRL ${ }_{1000}$ outperforms $\mathrm{BRL}_{1}$.

The average RCIs obtained by the various rule learning methods are shown in Table 4. BRL ${ }_{1000}$ has the highest RCI on 19 datasets, whereas $\mathrm{BRL}_{1}$ has the highest RCI on 3 datasets. There was one tie among the two BRL methods and C4.5. In addition, C4.5 has the highest RCI on one dataset. In Table 5, we compare the difference in performance using the RCI measure between C4.5 with BRL 1 and $\mathrm{BRL}_{1000}$ and both BRL methods are statistically significantly better than C4.5; the difference in performance using the RCI measure

Table 3. Statistical comparisons between C4.5 and the two BRL algorithms using BACC


We do not compare Ripper and Conjunctive Rule Learner because C4.5 and the two BRL algorithms completely dominate on both performance measures. BRL 1 stands for BRL with beam size 1 and $\mathrm{BRL}_{1000}$ represents BRL with beam size 1000 . We use both two-sided $t$-test and two-sided Wilcoxon signed rank test. Those $P$-values that are significant $(<0.05)$ are in bold and scores with a positive value favor the first method in the comparison.

Table 4. RCI results on the 24 datasets (from $2 \times 10$-fold)


between $\mathrm{BRL}_{1000}$ and $\mathrm{BRL}_{1}$ is statistically significant in favor of $\mathrm{BRL}_{1000}$.

Table 6 depicts a comparison of the average number of variables (markers) appearing in the rule models for $\mathrm{C} 4.5, \mathrm{BRL}_{1}$ and $\mathrm{BRL}_{1000}$, when run with default parameter settings. The average was calculated over the models generated from 20 folds (obtained

Table 5. The statistical comparisons between C4.5 and the two BRL implementations using RCI


Table 6. Comparison of the average number of variables in the models produced by C4.5 and BRL over all folds


from stratified 10 -fold cross-validation repeated two times) on the 24 datasets. As shown, the BRL models have $\sim 70 \%$ less variables on average in their models than C4.5.

If each predictor variable has only two discretized ranges of values, then BRL with default parameters would generate between $2^{3}$ and $2^{5}$ rules on average. However, discretization could yield a larger number of value ranges for a variable, thereby increasing the number of rules generated by BRL. To reduce the number of rules, we can prune rules with zero coverage, that is, those rules whose left-hand side does not match any of the samples in the training data. We notice that pruning does not harm BRL's performance. However, rule pruning could cause problems during testing, since rules that do not match training data could still match test data. We include an example of pruned rules and also C4.5 rules in the

Supplementary Material. The variables chosen in BRL's predictive models are often different from those chosen by C4.5.

### 4.1 Discussion

There are several advantages that accrue from BRL that are not available in current rule learning algorithms. BRL allows for the evaluation of the entire rule set using a Bayesian score. Using such a score results in a whole model evaluation instead of a per rule (or local) evaluation, which often occurs with Ripper and C4.5. The Bayesian score allows us to capture the uncertainty about the validity of a rule set. BRL currently uses this score only for model selection. However, the score could be utilized in extensions to BRL for performing inference when rule sets can be weighted by this score, which would be a form of Bayesian model averaging.

A Bayesian approach allows incorporation of both structure and parameter priors. When training data are scarce, such as in 'omic' data analysis, it is useful to incorporate prior knowledge to improve the accuracy of learned models. For example, a scientist could define all of the variable relationships using either a knowledge base or restrict the possible variables with which to build the model (Frey et al., 2005; Miriam et al., 2005). In a Bayesian approach, a scientist might provide prior knowledge specifying conditional independencies among variables, constraining or even fully specifying the network structure of the BN. In addition to providing such structure priors, the scientist might also specify knowledge in the form of prior distributions over the parameter values of the model. Structure priors are arguably the most useful, however, because in our experience scientists are often more confident about structural relationships than about parameter values.

We have not explored informative priors in this article. We used uniform parameter and uniform structure priors. Exploring informative structure priors in this domain is a direction for future research.

There are different ways of representing non-informativeness of parameters using the Dirichlet priors. We have explored one approach, it would be useful to explore other approaches as well.

An interesting open problem is to investigate methods for BRL rule ordering and pruning within a set of rules. For example, pruning a set of BRL rules based on using local structure and scores (Chickering et al., 1997; Friedman and Goldszmidt, 1996; Visweswaran and Cooper, 2005) would be worth investigating.

A major advantage of BRL is that it can find models with fewer variables (markers) that have equivalent or greater classification performance than those obtained from several other rule learning methods. Fewer variables mean fewer markers for biological verification and subsequent validation. This is important in biomarker discovery and validation studies that have to be designed carefully and under tight resource constraints.

## 5 CONCLUSIONS

We have shown that using a BN approach to generate rule models not only allows a more parsimonious model (in terms of the number of variables), but also produces results that are statistically significantly superior to common rule learning methods. It also allows the creation of probabilistic rules that are optimized on the rule model level as opposed to the current method of evaluation per rule. Using BN as a

generating model also provides a coherent method for incorporating different types of prior information and updating the rule model.

The basic BRL algorithm presented here can be extended in many ways, which include experimenting with different priors, pruning and rule ordering methods. The use of multiple data mining methods to analyze biomedical 'omic' datasets has become important as these techniques often complement one another in terms of discoveries. In this article, we present and evaluate a novel approach that can complement existing methods for biomedical data mining. We hope that researchers will find this approach useful for efficient knowledge discovery from biomedical datasets and that future extensions will yield additional improvements.

## ACKNOWLEDGEMENTS

We thank the Bowser Lab at the University of Pittsburgh (Department of Pathology) for use of the proteomic dataset from Ranganathan et al. (2005). We thank Philip Ganchev, the University of Pittsburgh (Intelligent Systems Program) for help with additional verification runs of the experiments with BRL.

Funding: National Institute of General Medical Sciences (grant number GM071951); the National Library of Medicine (grant numbers T15-LM007059, R01-LM06696); the National Science Foundation (grant number IIS-0325581).

Conflict of Interest: none declared.
