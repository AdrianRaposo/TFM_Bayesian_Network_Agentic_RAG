# Federated Bayesian Network Ensembles 

Florian van Daalen, Graduate Student Member, IEEE, Lianne Ippel, Andre Dekker, and Inigo Bermejo


#### Abstract

Federated learning allows us to run machine learning algorithms on decentralized data when data sharing is not permitted due to privacy concerns. Ensemble-based learning works by training multiple (weak) classifiers whose output is aggregated. Federated ensembles are ensembles applied to a federated setting, where each classifier in the ensemble is trained on one data location. In this article, we explore the use of federated ensembles of Bayesian networks (FBNE) in a range of experiments and compare their performance with locally trained models and models trained with VertiBayes, a federated learning algorithm to train Bayesian networks from decentralized data. Our results show that FBNE outperforms local models and provides a significant increase in training speed compared with VertiBayes while maintaining a similar performance in most settings, among other advantages. We show that FBNE is a potentially useful tool within the federated learning toolbox, especially when local populations are heavily biased, or there is a strong imbalance in population size across parties. We discuss the advantages and disadvantages of this approach in terms of time complexity, model accuracy, privacy protection, and model interpretability.


Index Terms-Federated Learning, Bayesian network, privacy preserving, Federated Ensembles, Ensemble Learning

## 1 INTRODUCTION

Federated learning allows machine learning algorithms to be applied to decentralized data when data sharing is not an option due to privacy concerns [1]. Traditionally federated learning approaches train a model iteratively on local data [2]. The local results are then averaged back into a single global model. Privacy is preserved using epsilondifferential privacy [3], homomorphic encryption [4], and multiparty computation (MPC) [5] during this process. The specific techniques used, depend on the way the data is split across the various parties. If the data is split horizontally, i.e, each party has data belonging to a different population but the attributes are the same, simpler techniques can be used. While this approach yields good results in many cases, it suffers from several limitations.

A major downside is that it does not explicitly consider heterogeneity across different data sites. That is, it assumes that the data is independent and identically distributed (IID) over the various parties. However, in practice, federated environments will often be subject to local biases. For example, a common scenario where federated learning is implemented is when multiple hospitals combine their data to build a joint model [6]. These hospitals may have very different population sizes, which may cause the final model to overfit on the biggest hospital. Additionally, the hospitals might have biases in their populations: e.g., an urban and a rural hospital will have different patient populations. Furthermore, the hospitals may even be on opposite sides

- F. van Daalen, I. Bermejo, and A. Dekker are with the Department of Radiation Oncology (MAASTRO) GROW School for Oncology and Reproduction Maastricht University Medical Centre+ Maastricht the Netherlands
- L. Ippel is with Statistics Netherlands Heerlen the Netherlands.

The views expressed in this paper are those of the authors and do not necessarily reflect the policy of Statistics Netherlands.

This research received funding from the Netherlands Organization for Scientific Research (NWO): Coronary ARtery disease: Risk estimations and Interventions for prevention and EaRly detection (CARRIER): project nr. 628.011.212.
of the globe, adding further biases into the distribution due to cultural, socio-economic, and many other factors. Simply averaging over these diverse populations may result in models that fit neither population, or it may result in the model overfitting on one particular population, while ignoring others.

If the data is split vertically, , i.e. when different parties have different variables about the same population, it may be possible that there are dependencies between the parties. For example, if one party is a general practitioner (GP) and the other party is the specialist clinician, the GP might have referred the patient to the specialist and there will be a dependency between the two datasets. The GP might, for example, have started treatment based on the data he has, which will influence the data the specialist receives.

These diverse types of bias may create problems when using the traditional federated learning approach. An alternative is the use of federated ensembles, ensembles of classifiers, each of which has been trained on the local data of each party in a federated setting [7]. Ensemble based learning works by combining multiple (weak) classifiers which work together to jointly produce classifications using various voting schemes [8]. It relies on a diverse set of classifiers, under the assumption that if one classifier makes a mistake the other classifiers will correct it. This allows ensembles to achieve a high performance, even when the individual classifiers are weak. A major advantage of ensemble learning is that it can deal with non-IID data [9]. It can even take advantage of the dependencies by using (dynamically) weighted voting schemes. For example, an ensemble of experts can weigh the votes of classifiers trained on a similar population, or trained on specific sub-tasks, more strongly [10], [11].

Current research into federated ensembles is limited [7]. There is only a small body of current work specifically looking into federated ensembles. There are still several general open questions, mainly:

1) How to share class labels in a privacy preserving

manner in a vertically distributed setting.
2) How to detect and exploit the subtle biases and dependencies that exist across parties.
3) How to determine correlations between the various attributes split across parties.

In addition to these general questions, there is also room for exploring different types of ensembles, using different base-classifiers. In this article, we will explore the use of federated ensembles consisting of Bayesian networks (BN). We will compare these ensembles with VertiBayes [12], a federated implementation of BNs, as well as with a BN that was centrally trained. We will compare the various options in terms of technical complexity, training time required, privacy protection, and model performance.

## 2 MEthods

### 2.1 Bayesian networks

Bayesian networks (BN) are widely used probabilistic graphical models consisting of a directed acyclic graph (the structure) where each node represents a variables and arcs represent conditional dependencies and a set of conditional probability distributions (the parameters), one per node [13]. Their ability to combine existing expert knowledge with data has given them great utility and popularity. In addition, their graphical representation and probabilistic reasoning makes them relatively intuitive to understand models for non-technical personnel. This makes them especially useful in scenarios where non-technical personnel need to be able to understand the models, for example when models are used to inform clinical decisions.

### 2.2 VertiBayes

VertiBayes [12] is an implementation of BN learning algorithms in a federated environment. It works both in vertical and horizontally distributed scenarios, as well as in a hybrid scenario. In addition to this, it can deal with missing data [14], [15]. Furthermore, it includes a federated implementation of the K2 algorithm [16], allowing it to learn a network structure on the fly. Lastly, VertiBayes includes several validation methods, of various computational complexity, that can be used to validate the model in a privacy preserving manner. This makes it an appropriate tool in a federated setting where data quality across parties may not be guaranteed.

It has a similar performance compared to a centrally trained model. In addition, it provides the same privacy guarantees as the n-party scalar product protocol [17] used. However, it is considerably more time consuming to train a model using VertiBayes than it is to train a model centrally. The time complexity mostly depends on the number of probabilities that need to be calculated during parameter learning.

### 2.3 Federated Bayesian Network Ensembles

Federated Bayesian Network Ensembles (FBNE) are an ensemble learning approach where the base classifier consists of Bayesian networks. Each data owner within the federated setting makes their own Bayesian network based on locally
available data. This local data is only enriched with the class label (should this not be available locally) in a privacy preserving manner using VertiBayes. The local classifiers can then be used in an ensemble to classify a new individual.

It is possible to use FBNE in a horizontally split, vertically split and hybrid settings. In the case of a hybrid split, one may decide to build the models purely based on local data, or to allow the hybrid variables to also utilize the data available at other data parties. For example, if party 1 contains attribute A \& B, and party 2 contains attributes B \& C, we can choose to either build a model using only the data available locally at party 1 , or to build a model which also includes the data party 2 has regarding attribute B. In addition, it is possible with the use of predefined structures to mix and match variables from various parties to create the optimal ensemble.

### 2.3.1 Privacy risks

The privacy risks posed by FBNE are the same as those posed by VertiBayes. That is to say, there are no major risks during training. However, the BNs themselves do still contain information. The structure and CPDs included in the BNs will be revealed if they are published. The published networks can be used to predict missing values in a dataset by a third party. This is inherent to how BNs work and as such is unavoidable. An ensemble of BNs poses a similar risk.

### 2.3.2 Runtime advantages

FBNE are significantly faster than VertiBayes as the majority of the calculations can be done locally. This minimizes the use of complex MPC needed to preserve privacy.

### 2.3.3 Performance advantages and disadvantages

FBNE may outperform a single model. The ensembles may catch local biases that are lost when only a single model is built. Furthermore, by using weighted voting it becomes possible to create a mixture of experts. This is especially advantageous if it is known that the various data parties have biases in their data. For example, in a scenario where hospitals work together to build an ensemble it may be useful to weigh the votes if one hospital specializes in a certain type of patient.

### 2.3.4 Interpretability

Ensembles are generally less interpretable than a single classifier. However, Bayesian networks are highly interpretable. While it is not possible to directly detect interactions across the various individual classifiers within the ensemble it is possible to use the individual classifiers to guide research into variable interactions in a smart manner. For example, by comparing the sparsity of the local networks to determine if certain variables are actually of interest to the outcome variable. In addition to this, it can be possible to use expert knowledge to deduce possible interactions. For example take the following toy examples shown in figure 1.

In addition to these two models, expert knowledge indicates that poverty increases the likelihood of smoking. Based on this expert knowledge and the local models that were created it can be deduced that the global structure might be similar to the network shown in figure 2

![img-0.jpeg](img-0.jpeg)

Fig. 1: Two local networks based on locally available data
![img-1.jpeg](img-1.jpeg)

Fig. 2: Global network created by combining the two local models from figure 1 while utilizing expert knowledge.

Furthermore, it should be noted that it is possible to apply feature selection across ensembles using wrapper-based approaches. By utilizing this type of feature selection, it may be possible to detect mediating effects between attributes.

## 3 EXPERIMENTS

We ran a range of experiments to assess the performance of $\mathrm{FBNE}^{1}$. We used the following datasets: Iris [18], Autism [19], Asia [20], Diabetes [21], Alarm [22] and Mushroom [23].

The Iris dataset contains 5 attributes and contains 150 individuals. It contains no missing values. The Autism dataset has 20 attributes and contains 704 individuals. The Asia dataset contains 10.000 individuals and 8 attributes. The Alarm dataset also contains 10.000 individuals and 37 attributes. The Diabetes dataset contains 768 individuals and 9 attributes. The mushroom dataset has 23 attributes and contains 8124 individuals.

Each dataset was tested with varying levels of missing values (no missing values, $5 \%, 10 \%, 30 \%$ missing at random ) We tested the following federated split scenarios:

- Vertical split with the attributes split randomly between parties. Each party has at least 2 local at-

1. An implementation of FBNE can be found in the following git repository: https://github.com/MaastrichtU-CDS/bayesianEnsemble
![img-2.jpeg](img-2.jpeg)

Fig. 3: Horizontally split data
![img-3.jpeg](img-3.jpeg)

Fig. 4: Vertically split data
tributes. This was done for a setting with 2 and a setting with 3 parties.

- Horizontal split with the samples split randomly between parties. Each party has at least 50 records. Again this was done for a setting with 2 and a setting with 3 parties.
- Additionally the horizontal splits were tested at varying levels of bias. To induce this bias we would make it more likely for individuals of a certain label to be put in a specific data station, e.g. individuals with the class label "true" are more likely to be put in party 1 , individuals with class label "false" are more likely to be put in party 2. In the case of non-binary labels, such as for the Iris dataset, the bias would be created by piting label 1 against the rest. The following levels of bias were introduced: no bias, $75 \%, 85 \%$, and $95 \%$ bias.
- Hybrid split. The attributes are randomly split in two, the samples in one of these splits is then randomly split in two again. This results in 3 parties in total, each with at least 2 local attributes and 50 local records.

An illustration of the various data splits can be found in section 4 and fig. 4.

![img-4.jpeg](img-4.jpeg)

Fig. 5: Hybrid split data

Each of these scenarios was run 10 times for each dataset. It should be noted that not every dataset could be used in every scenario. For example, the Iris dataset only contains 5 attributes and thus cannot be used in a 3-party vertically split scenario.

In addition to these random splits, an experiment was also run where data was manually split in a "realistic" manner in a vertical setting based on expert knowledge. These experiments attempt to represent a realistic split where different parties collected different types of data. For example, the Autism data set contains attributes representing answers to a questionnaire, and some general personal attributes such as age, sex, and country of residence. This data was split in such a way that one party had the questionnaire answers, and the other party had the remaining attributes. As mentioned above, horizontal bias is addressed separately in the horizontal experiments.

We compared the performance of FBNE with VertiBayes as well as a centrally trained Bayesian network. In addition, the performance of the local models on their local data is used as a baseline, after all if the local model already creates a sufficiently strong classifier there is no need for a federated model. The performance was measured by calculating the AUC using a 10-fold cross validation.

In all cases both structure and parameters were learnt. Continuous variables were discretized into intervals that contained at least 10% of the total population.

## 4 Results

A selection of the results can be seen in tables tables 1 and 2 and section 4. The selected results illustrate the general trends seen across all experiments. The remaining experimental results can be found in the appendix.

In all tables the highest AUC is indicated in green, the second highest in yellow.

### 4.1 Runtime

The training process for FBNE is consistently faster than VertiBayes in every experimental setting and for every dataset used. However, it should be noted that the differences vary widely and depend on the dataset. These differences are mainly driven by the different network structures. FBNE has the advantage that most calculations can be done locally. During our experiments FBNE was faster than VertiBayes by a factor that ranged from twice as fast to fifty times as fast. It should be noted that it is difficult to predict per scenario how large the processing speed gains will be as it is difficult to predict the resulting network structure.

### 4.2 Performance

FBNE largely shows the same performance as VertiBayes, scoring similar AUC's. However, it should be noted that for specific datasets, and for specific data-splits, the ensembles can perform significantly better. With the largest difference being nearly a 0.1 difference in AUC.

In addition to outperforming VertiBayes by a relevant margin in specific scenarios, the following general trends were visible in our experiments. First, FBNE performs very well in scenarios with no missing data. FBNE achieved the highest AUC in 80% of the scenarios with no missing data. However, VertiBayes performs better in scenarios with missing values. VertiBayes achieved the highest AUC in roughly 70% of the scenarios.

Another interesting trend that is visible in our experiments is that in horizontally split scenarios the local models can perform well if the local data quality is high, occasionally performing similarly to the federated and centralized models. However, it should be noted that this is rare.

It is important to note that neither approach was optimized, and better models can potentially be created. For example, a network structure generated using expert knowledge, as opposed to using an automatic approach like the K2 algorithm, may result in better Bayesian networks. Both VertiBayes and FBNE could benefit from such expert knowledge. In addition, weighted voting, and especially dynamically weighted voting, can improve the performance of FBNE.

## 5 DISCUSSION

Our experiments show that FBNE can be a suitable solution in certain scenarios. In this section we will take a deeper dive into the differences between FBNE and VertiBayes.

### 5.1 Runtime

The reduced training time that was observed during the experiments is a strong advantage in favor of the federated ensembles, especially in time critical applications or in cases when MPC solutions such as VertiBayes are too time consuming. FBNE has this advantage due to the fact that the vast majority of calculations can be done locally and thus requires far fewer computationally difficult operations than VertiBayes does.

In addition to the improved runtime already observed here, it should be noted that our implementation of the ensembles has not been fully optimized. There is room for further improvements, especially with respect to parallelization, which will further increase the gap in terms of runtime. However, since the goal of this study was to simply explore the potential of FBNE, not to provide an optimized implementation, this will not a part of this study.

TABLE 1: Experimental results vertically split 2-party scenarios where attributes were randomly split across parties. ${ }^{\prime * *}$ Indicates the best performing model, ' $\dagger$ ' indicates the second best performing model.


TABLE 2: Experimental results vertically split 2-party scenarios where attributes were manually split across parties to simulate a realistic biased split. ${ }^{\prime * *}$ Indicates the best performing model, ' $\dagger$ ' indicates the second best performing model.


### 5.2 Performance

FBNE largely showed the same performance as VertiBayes, however, in specific scenarios it significantly outperformed VertiBayes. With the largest difference being nearly a 0.1 difference in AUC. This does indicate that FBNE are potentially very useful in the right situation. However, it is very difficult to determine when this is the case without simply training the FBNE.

Two trends were visible with respect to the performance differences. First, FBNE performs very well in scenarios with no missing data. However, VertiBayes performs better in scenarios with missing values. There are two plausible reasons that explain why VertiBayes performs better in these scenarios. The first explanation is that FBNE did not have a large, or diverse, enough ensemble in the experimental scenarios to work properly. Ensemble learning relies on a diverse set of classifiers which can correct each other's mistakes, with only 2 or 3 models in our scenarios the ensembles may not be able to do this consistently. The second possible explanation is that the synthetic data generation step within VertiBayes allows it to bootstrap itself for an improved performance.

Another interesting trend that is visible in our experiments is that in horizontally split scenarios the local models occasionally perform well when local data is of a high quality, especially when the local population is not biased in any way. This reminds us that it is always important to ask if a federated model is truly necessary. Building a federated model is only worthwhile if the data added from other parties adds extra information. But if your local data is already sufficiently large, and representative of the true population, then a federated model may not be needed. However, if the local data is small, or biased in some way, then a federated approach is needed.

It is important to note that neither approach was optimized, and better models can potentially be created. For example, both VertiBayes and FBNE can benefit from improvements, such as using expert knowledge to build the optimal structures. In addition to improvements that could be applied to both approaches, weighted voting, and especially dynamically weighted voting, can improve the performance of FBNE.

### 5.3 Privacy concerns \& disclosure control

Our implementation of FBNE uses VertiBayes at its core. As such, the privacy guarantees are largely the same. However, there are two aspects in which they potentially differ from VertiBayes:

1) The classification of individuals, and evaluation of the model.

TABLE 3: Experimental results hybrid split 3-party scenarios where only locally available data was used in the local model. '*' Indicates the best performing model, ' $\dagger$ ' indicates the second best performing model.


TABLE 4: Experimental results horizontally split 2-party scenarios where records are randomly split across parties. '*' Indicates the best performing model, ' $\dagger$ ' indicates the second best performing model.


2) The consequences of having multiple networks.

With FBNE, the individual classifiers can create their classifications fully locally at the party they belong to given that required attributes for each local model should be available locally. These individual classifications can be combined using homomorphic encryption, resulting in a final classification which can be shared. For example, estimated probabilities can be weighted according to the voting power of a particular classifier, then encrypted using an additive homomorphic encryption scheme, and all encrypted weighted probabilities are summed. The sum is then decrypted and divided by the total weight to get the weighted average probabilities, which determine the final classification. Combining the votes in this way prevents any local data from being shared and allows FBNE to be evaluated without the need of the homomorphic encryption and a privacy preserving n-scalar product protocol [17] or other more complex evaluation methods that VertiBayes needs [?]. This is a strong advantage when new samples need to be classified or predicted in a federated manner.

The other aspect in which FBNE differs from VertiBayes is that the end-result consists of multiple networks instead of one. Ensembles might provide a minor advantage with respect to privacy in this case. In both cases it is possible to learn dependencies between attributes and certain statistics about the training set, based on the CPDs and network structures. Similarly, based on local, incomplete data, the network can be used to predict missing values. These are unavoidable consequences of using Bayesian networks. However, because FBNE has the information split up over multiple networks, it will be difficult to do this for every attribute. It is very difficult to determine any relation between two attributes when those two attributes are split over two Bayesian networks, as discussed in section 2.3.4. This provides some additional privacy protection compared to a single network.

### 5.4 When should FBNE be preferred over VertiBayes

Due to the significant advantage in terms of runtime it may be beneficial to use FBNE as an exploratory first step before deciding if using VertiBayes is worth it. This naïve approach will already provide reasonable results.

The general advantages of each approach can be found in table 5.

TABLE 5: Comparison of main features of FBNE and VertiBayes


In addition to these advantages which hold in general, one of the two may perform better depending on how the data happened to be split. However, there is currently no good way to predict which approach will achieve the highest accuracy.

## 6 CONCLUSION

In this article, we have proposed the use of Federated Bayesian Network Ensembles (FBNE) and assessed their usefulness in a battery of experiments. We have shown the approach performs well in a range of situations and datasets, often achieving similar results when compared to VertiBayes, an alternative federated method. FBNE are significantly faster than VertiBayes, provide slightly better privacy guarantees, and are easier to use in a scenario where future classifications will also be done in a federated setting. On the other hand, VertiBayes results in more interpretable models and makes it easier to determine the dependencies between variables split over multiple sites.

The notable advantage in terms of runtime does mean that it is easily possible to use FBNE as an initial exploratory option. Since it is currently not possible to preemptively determine which approach will result in the highest accuracy, using this naive approach and simply training both models might be the best course of action for now. Additionally, this means it can be very useful when exploring new federated datasets.

### 6.1 Future work

We would like to explore ways to determine which approach is more effective as it would be highly beneficial to be able to know beforehand if an ensemble-based approach will outperform a single model. Additionally, we would like to run experiments to discover if (dynamically) weighted voting could be used to significantly improve the performance of the ensembles. Lastly, it would be extremely valuable if these experiments could be run on real use cases. This would allow the experiments to work with realistic biases and remove the need to artificially create these biases in our experimental setup. Resulting in much more realistic experimental scenarios.

## APPENDIX

The remaining experimental results are contained in the following pages of this appendix.

TABLE 6: Experimental results vertically split 3-party scenarios where attributes were randomly split across parties. ${ }^{\prime * *}$ Indicates the best performing model, ' $\dagger$ ' indicates the second best performing model.


TABLE 7: Experimental results vertically split 3-party scenarios where attributes were manually split across parties. ${ }^{\prime * *}$ Indicates the best performing model, ' $\dagger$ ' indicates the second best performing model.


TABLE 8: Experimental results hybrid split 3-party scenarios where hybrid split attributes can fully incorperated into the local models. ${ }^{\prime * *}$ Indicates the best performing model, ' $\dagger$ ' indicates the second best performing model.


TABLE 9: Experimental results horizontally split 3-party scenarios where records are randomly split across parties. '*' Indicates the best performing model, ' $\dagger$ ' indicates the second best performing model.


TABLE 10: Experimental results horizontally split 2-party scenarios where records are randomly split across parties. Varies levels of bias were introduced in this experiment where the level of bias corresponds to the probability of an individual with first class label to be assigned to party 1. '*' Indicates the best performing model, ' $\dagger$ ' indicates the second best performing model.


TABLE 11: Experimental results horizontally split 3-party scenarios where records are randomly split across parties. Varies levels of bias were introduced in this experiment where the level of biass corresponds to the probability of an individual with first class label to be assigned to party 1. ${ }^{\text {* }}$ * Indicates the best performing model, ' $\dagger$ ' indicates the second best performing model.
