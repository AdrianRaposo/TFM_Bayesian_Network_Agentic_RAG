# Bayesian Class-Matched Multinet Classifier 

Yaniv Gurwicz and Boaz Lerner<br>Pattern Analysis and Machine Learning Lab<br>Department of Electrical \& Computer Engineering<br>Ben-Gurion University, Beer-Sheva 84105, Israel<br>\{yanivg, boaz\}@ee.bgu.ac.il


#### Abstract

A Bayesian multinet classifier allows a different set of independence assertions among variables in each of a set of local Bayesian networks composing the multinet. The structure of the local network is usually learned using a joint-probability-based score that is less specific to classification, i.e., classifiers based on structures providing high scores are not necessarily accurate. Moreover, this score is less discriminative for learning multinet classifiers because generally it is computed using only the class patterns and avoiding patterns of the other classes. We propose the Bayesian class-matched multinet $\left(\mathrm{BCM}^{2}\right)$ classifier to tackle both issues. The $\mathrm{BCM}^{2}$ learns each local network using a detection-rejection measure, i.e., the accuracy in simultaneously detecting class patterns while rejecting patterns of the other classes. This classifier demonstrates superior accuracy to other state-of-the-art Bayesian network and multinet classifiers on 32 real-world databases.


## 1 Introduction

Bayesian networks (BNs) excel in knowledge representation and reasoning under uncertainty [1]. Classification using a BN is accomplished by computing the posterior probability of the class variable conditioned on the non-class variables. One approach is using Bayesian multinets. Representation by a multinet explicitly encodes asymmetric independence assertions that cannot be represented in the topology of a single BN using a several local networks that each represents a set of assertions for a different state of the class variable [2]. Utilizing these different independence assertions, the multinet simplifies graphical representation and alleviates probabilistic inference in comparison to the BN [2]-[4]. However, although found accurate at least as other BNs [3], [4], the Bayesian multinet has two flaws when applied to classification. The first flaw is the usual construction of a local network using a joint-probability-based score [4], [5] which is less specific to classification, i.e., classifiers based on structures providing high scores are not necessarily accurate in classification [4], [6]. The second flaw is that learning a local network is based on patterns of only the corresponding class. Although this may approximate the class data well, information discriminating between the class and other classes may be discarded, thus undermining the selection of the structure that is most appropriate for classification.

We propose the Bayesian class-matched multinet $\left(\mathrm{BCM}^{2}\right)$ classifier that tackles both flaws of the Bayesian multinet classifier (BMC) by learning each local network

using a detection-rejection score, which is the accuracy in simultaneously detecting and rejecting patterns of the corresponding class and other classes, respectively. We also introduce the $t \mathrm{BCM}^{2}$ which learns a structure based on a tree-augmented naïve Bayes (TAN) [4] using the SuperParent algorithm [7]. The contribution of the paper is three fold. First is the suggested discrimination-driven score for learning BMC local networks. Second is the use of the entire data, rather than only the class patterns for training each of the local networks. Third is the incorporation of these two notions into an efficient and accurate BMC (i.e., the $t \mathrm{BCM}^{2}$ ) that is found superior to other state-of-the-art Bayesian network classifiers (BNCs) and BMCs on 32 real-world databases.

Section 2 of the paper describes BNs and BMCs. Section 3 presents the detectionrejection score and $\mathrm{BCM}^{2}$ classifier, while Section 4 details experiments to compare the $\mathrm{BCM}^{2}$ to other BNCs and BMCs and their results. Section 5 concludes the work.

# 2 Bayesian Networks and Multinet Classifiers 

A BN model $B$ for a set of $n$ variables $\boldsymbol{X}=\left\{X_{1}, \ldots, X_{n}\right\}$, having each a finite set of mutually exclusive states, consists of two main components, $B=(G, \Theta)$. The first component $G$ is the model structure that is a directed acyclic graph (DAG) since it contains no directed cycles. The second component is a set of parameters $\Theta$ that specify all of the conditional probability distributions (or densities) that quantify graph edges. The probability distribution of each $X_{i} \in \boldsymbol{X}$ conditioned on its parents in the graph $\boldsymbol{P a}_{i} \subseteq \boldsymbol{X}$ is $P\left(X_{i}=x_{i} \mid \boldsymbol{P a}_{i}\right) \in \Theta$ when we use $X_{i}$ and $\boldsymbol{P a}_{i}$ to denote the $i$ th variable and its parents, respectively, as well as the corresponding nodes.

The joint probability distribution over $\boldsymbol{X}$ given a structure $G$ that is assumed to encode this probability distribution is given by [1]

$$
P(\boldsymbol{X}=\boldsymbol{x} \mid G)=\prod_{i=1}^{n} P\left(X_{i}=x_{i} \mid \boldsymbol{P a}_{i}, G\right)
$$

where $\boldsymbol{x}$ is the assignment of states (values) to the variables in $\boldsymbol{X}, x_{i}$ is the value taken by $X_{i}$, and the terms in the product compose the required set of local conditional probability distributions $\Theta$ quantifying the dependence relations. The computation of the joint probability distribution (as well as related probabilities such as the posterior) is conditioned on the graph. A common approach is to learn a structure from the data and then estimate its parameters based on the data frequency count. In this study, we are interested in structure learning for the local networks of a BMC.

A BN entails that the relations among the domain variables be the same for all values of the class variable. In contrast, a Bayesian multinet allows different relations, i.e., (in)dependences for one value of the class variable are not necessarily those for other values. A BMC [2]-[5], [8], [9] is composed of a set of local BNs, $\left\{B_{1}, \ldots, B_{N 7}\right\}$, each corresponds to a value of the $|C|$ values of the class node $C$. The BMC can be viewed as generalization of any type of BNC when all local networks of the BMC have the same structure of the BNC [4]. Although a local network must be searched for each class, the BMC is generally less complex and more accurate than a BNC. This is because usually each local network has a lower number of nodes than the

BNC, as it is required to model a simpler problem. The computational complexity of the BMC is usually smaller and its accuracy higher than those of the BNC since both the complexity of structure learning and number of probabilities to estimate increase exponentially with the number of nodes in the structure [2].

A BMC is learned by partitioning the training set into sub-sets according to the values of the class variable and constructing a local network $B_{k}$ for $\boldsymbol{X}$ for each class value $C=C_{k}$ using the $k$ th sub-set. This network models the $k$ th local joint probability distribution $P_{B_{k}}(\boldsymbol{X})$. A multinet is the set of local BNs $\left\{B_{1}, \ldots, B_{|C|}\right\}$ that together with the prior $P(C)$ on $C$ classify a pattern $\boldsymbol{x}=\left\{x_{1}, \ldots, x_{n}\right\}$ by choosing the class $C_{K} \forall K \in[1,|C|]$ maximizing the posterior probability

$$
C_{K}=\underset{k \in[1,|C|]}{\arg \max }\left\{P\left(C=C_{k} \mid \boldsymbol{X}=\boldsymbol{x}\right)\right\}
$$

where

$$
P\left(C=C_{k} \mid \boldsymbol{X}=\boldsymbol{x}\right)=\frac{P\left(C=C_{k}, \boldsymbol{X}=\boldsymbol{x}\right)}{P(\boldsymbol{X}=\boldsymbol{x})}=\frac{P\left(C=C_{k}\right) P_{B_{k}}(\boldsymbol{X}=\boldsymbol{x})}{\sum_{i=1}^{|C|} P\left(C=C_{i}\right) P_{B_{i}}(\boldsymbol{X}=\boldsymbol{x})}
$$

In the Chow-Liu multinet (CL multinet) [4], the local network $B_{k}$ is learned using the $k$ th sub-set and based on the Chow-Liu (CL) tree [10]. This maximizes the loglikelihood [4], which is identical to minimizing the KL divergence between the estimated joint probability distribution based on the network $P_{B_{k}}$ and the empirical probability distribution for the sub-set $\hat{P}_{k}[5]$,

$$
\mathrm{KL}\left(\hat{P}_{k}, P_{B_{k}}\right)=\sum_{\boldsymbol{x}} \hat{P}_{k}(\boldsymbol{X}=\boldsymbol{x}) \cdot \log \left[\frac{\hat{P}_{k}(\boldsymbol{X}=\boldsymbol{x})}{P_{B_{k}}(\boldsymbol{X}=\boldsymbol{x})}\right]
$$

Thus, the CL multinet induces a CL tree to model each local joint probability distribution and employs (2) to perform classification. Further elaborations to the construction of the CL tree may be found in [3]. Also we note that the CL multinet was found superior in accuracy to the naïve Bayes classifier (NBC) and comparable to the TAN [4]. Other common BMCs are the mixture of trees model [9], the recursive Bayesian multinet (RBMN) [8] and the discriminative CL tree (DCLT) BMC [5].

# 3 The Bayesian Class-Matched Multinet Classifier 

We suggest the Bayesian class-matched multinet $\left(\mathrm{BCM}^{2}\right)$ that learns each local network using the search-and-score approach. The method searches for the structure maximizing a discrimination-driven score that is computed using training patterns of all classes. Learning a local network in a turn rather than both networks simultaneously has computational benefit regarding the number of structures that need to be considered. First we present the discrimination-driven score and then the $t \mathrm{BCM}^{2}$ that is a classifier based on the TAN [4] and searched using the SuperParent algorithm [7].

The $\mathbf{B C M}^{\mathbf{2}}$ Score. We first make two definitions: (a) a pattern $\boldsymbol{x}$ is native to class $C_{k}$ if $\boldsymbol{x} \in C_{k}$ and (b) a pattern $\boldsymbol{x}$ is foreign to class $C_{k}$ if $\boldsymbol{x} \in C_{j}$ where $j \in[1,|C|]$ and $j \neq k$. We partition the dataset $D$ into test $\left(D_{t s}\right)$ and training $\left(D_{t r}\right)$ sets, the latter is further divided into internal training set $T$ used to learn candidate structures and a validation set $V$ used to evaluate these structures. Each training pattern in $D_{t r}$ is labeled for each local network $B_{k}$ as either native or foreign to class $C_{k}$ depending on whether it belongs to $C_{k}$ or not, respectively. In each iteration of the search for the most accurate structure, the parameters of each candidate structure are learned using $T$ in order to construct a classifier that can be evaluated using a discrimination-driven score on the validation set. After selecting a structure, we update its parameters using the entire training set $\left(D_{t r}\right)$ and repeat the procedure for all other local networks. The derived $\mathrm{BCM}^{2}$ can be then tested using (2).

The suggested score evaluates a structure using the ability of a classifier based on this structure in detecting native patterns and rejecting foreign patterns. The score $S_{x}$ for a pattern $\boldsymbol{x}$ is determined based on the maximum a posteriori probability, i.e.,

$$
S_{x}=\left\{\begin{array}{l}
\left\{\text { if }\left\{P\left(C=C_{k} \mid \boldsymbol{X}=\boldsymbol{x}_{n}^{k}\right) \geq P\left(C \neq C_{k} \mid \boldsymbol{X}=\boldsymbol{x}_{n}^{k}\right)\right\} \text { or }\left\{P\left(C \neq C_{k} \mid \boldsymbol{X}=\boldsymbol{x}_{f}^{k}\right)>P\left(C=C_{k} \mid \boldsymbol{X}=\boldsymbol{x}_{f}^{k}\right)\right\} \\
\left\{\text { if }\left\{P\left(C=C_{k} \mid \boldsymbol{X}=\boldsymbol{x}_{n}^{k}\right)<P\left(C \neq C_{k} \mid \boldsymbol{X}=\boldsymbol{x}_{n}^{k}\right)\right\} \text { or }\left\{P\left(C \neq C_{k} \mid \boldsymbol{X}=\boldsymbol{x}_{f}^{k}\right) \leq P\left(C=C_{k} \mid \boldsymbol{X}=\boldsymbol{x}_{f}^{k}\right)\right\}
\end{array}\right.
$$

where $\boldsymbol{x}_{n}^{k}$ and $\boldsymbol{x}_{f}^{k}$ are native and foreign patterns to $C_{k}$, respectively. The first line in (5) represents correct detection (classification of a native pattern to $C_{k}$ ) or correct rejection (classification of a foreign pattern to a class other than $C_{k}$ ), whereas the second line represents incorrect detection of a native pattern or incorrect rejection of a foreign pattern. By identifying $T P$ (true positive) as the number of correct detections and $T N$ (true negative) as the number of correct rejections made by a classifier on all the $|V|$ validation patterns in $V$, we define the detection-rejection measure (DRM)

$$
D R M=\frac{\sum_{x \in V} S_{x}}{|V|}=\frac{(T P+T N)}{|V|}, \quad D R M \in[0,1]
$$

That is, for each local network and each search iteration, we select the structure that the trained classifier based on this structure simultaneously detects native patterns and rejects foreign patterns most accurately. Both correct detection and correct rejection contribute equally to the score although any other alternative is possible.

TAN-Based BCM ${ }^{2}$. We propose a TAN-based $\mathrm{BCM}^{2}\left(t \mathrm{BCM}^{2}\right)$ that utilizes the $D R M$ and SuperParent algorithm searching the TAN space. The SuperParent (SP) algorithm has reduced computational cost compared to hill-climbing search (HCS) and it expedites the search [7]. In each iteration, we determine the best edge to add to a structure by finding a good parent and then the best child for this parent.

Following [7] we define: (a) an Orphan is a node without a parent other than the class node, (b) a SuperParent (SP) is a node extending edges to all orphans simultaneously (as long as no cycles are formed) and (c) a FavoriteChild (FC) of an SP is the orphan amongst all orphans that when connected to the SP provides a

structure having the highest value of the $D R M$. We initialize the search for each local network using the NBC structure and employ the value of $D R M$ it provides as the current $D R M$ value. Each iteration of the search comprises of two parts. First, we make each node an SP in turn and choose the SP that if added to the structure would provide the highest value of the $D R M$. Second, we find the FC for this SP and add the edge between them to the structure if this edge increases the current value of the $D R M$. We update the current value of the $D R M$ and continue the search as long as the $D R M$ value increases and more than one orphan remains unconnected to an SP. Since in each iteration we connect one variable at the most, the maximum number of iterations and edges that can be added to the initial structure is $n-1$ (yielding the TAN structure). We repeat this procedure for all $|C|$ local networks terminating with the $t \mathrm{BCM}^{2}$, as is exemplified in the following pseudo code:

```
1. For \(k=1:|C| \quad / /\) index of the local network \(B_{k}\)
1.1 Start with the NBC structure as the current structure of the \(k\) th local network. In
    all stages, use \(T\) to learn the structure and \(V\) to calculate the structure \(D R M\).
1.2 For \(g=1: n-1 \quad / /\) index of iteration
1.2.1 Find the SP yielding the structure having the highest \(D R M\).
1.2.2 Find the FC for this SP.
1.2.3 If the edge \(\mathrm{SP} \rightarrow \mathrm{FC}\) improves the \(D R M\) value of the current structure, update
        the structure with this edge and employ the structure as the current structure.
        Else: Return the current structure as the \(k\) th local network and go to 1 .
1.3 Return the current structure as the \(k\) th local network and go to 1 .
2. Calculate the parameters of each local network using \(D_{t r}\) and return the \(t \mathrm{BCM}^{2}\).
```

Although both the CL multinet and $t \mathrm{BCM}^{2}$ learn a multinet based on the TAN, the two algorithms differ in a several main issues. First, the CL multinet is learned using a constraint-based approach [11] based on the CL tree algorithm [10] or an extended version of this algorithm [3], while the $t \mathrm{BCM}^{2}$ is learned by employing the search-and-score approach [11]. Second, the former algorithm establishes for each class a CL tree that maximizes a joint-probability-based measure, whereas the latter algorithm employs a discrimination-driven score for structure learning. Third, the CL multinet utilizes only the class patterns for learning each local network, whereas the $t \mathrm{BCM}^{2}$ utilizes all patterns. Fourth, the CL multinet always adds $n-1$ edges even when some variables are completely independent, while the $t \mathrm{BCM}^{2}$ stops adding edges when there is no improvement in the score of a local network.

Finally we note that the worst case computational complexity of the $t \mathrm{BCM}^{2}$ (excluding the cost of parameter learning) is $O\left(3 \cdot|C| \cdot|V| \cdot n^{3} / 2\right)$, which incurs if the algorithm does not end before finding the maximum possible number of SPs [12]. As an example, Figure 1 demonstrates the four local networks learned by the $t \mathrm{BCM}^{2}$ for the UCI repository Car database [13] along with the corresponding $D R M$ values.

# 4 Experimental Results 

Between the $D R M$ and Classification Accuracy. Since the $D R M$ is measured for each local network separately and using the validation set and the classification accuracy is measured for the $t \mathrm{BCM}^{2}$ and the test set, we studied the relation between the two scores. We started the search for each local network with the NBC structure and identified an iteration by the addition of an edge between an SP and its FC. Whenever all the local networks had completed an iteration, we computed the values of $D R M$ they achieve, the average $D R M$ value and the test accuracy of the $t \mathrm{BCM}^{2}$ that used these networks. We repeated this procedure until all local networks completed learning (i.e., all final structures were found). Networks that completed learning before their counterpart networks, contributed their final $D R M$ values to the calculation of the average $D R M$ in each following iteration. Figure 2a presents the relation between the average $D R M$ value of the local networks and the classification accuracy of the $t \mathrm{BCM}^{2}$ for increasing numbers of iterations of the SP algorithm and the UCI repository Nursery database [13]. This database is large (i.e., providing reliable results) and has relatively many variables that introduce numerous possible edge additions in each search iteration, thereby the database enables testing structure
![img-0.jpeg](img-0.jpeg)

Fig. 1. The four local networks and associated $D R M$ values of the $t \mathrm{BCM}^{2}$ for the Car database
![img-1.jpeg](img-1.jpeg)

Fig. 2. (a) The relation between the average $D R M$ and the $t \mathrm{BCM}^{2}$ classification accuracy for increasing numbers of iterations of the SP algorithm and the UCI Nursery database. (b) Learning curves for the $t \mathrm{BCM}^{2}, \mathrm{CL}$ multinet, TAN and NBC for the Waveform-21 database.

learning extensively. The figure shows that the classification accuracy increases monotonically with the average $D R M$ value.
Learning Curves. Figure 2b presents learning curves for the $t \mathrm{BCM}^{2}$, CL multinet, TAN and NBC for the large UCI repository Waveform-21 database [13]. Each of ten random replications of the database was partitioned into ten sets. One set was reserved for the test, and the other nine sets were added incrementally to the training set. Each classifier was trained using the increased-size training set and tested on the same test set following each increase. The accuracy was repeatedly measured for all data replications and averaged. Figure 2b demonstrates that the NBC and CL multinet have, respectively, the smallest and largest sensitivity to the sample size. The former classifier has lesser sensitivity since it needs to estimate only few parameters so even a small sample size provides the classifier its asymptotic accuracy. The $t \mathrm{BCM}^{2}$ is less sensitive than the CL multinet for two reasons. First, the $t \mathrm{BCM}^{2}$ may have fewer edges for each of its local networks than the CL multinet (Section 3) and therefore it needs to estimate less parameters. Second, the $t \mathrm{BCM}^{2}$ utilizes all the data whereas the CL multinet employs only the class data. In addition we note that except for a very small sample size, the $t \mathrm{BCM}^{2}$ is superior to all other classifiers for this database. Similar conclusions are drawn for most of the other databases.

Classification Accuracy. Table 1 demonstrates the superior classification accuracy of the $t \mathrm{BCM}^{2}$ in comparison to the NBC, TAN, CL multinet and RBMN for 32 databases of the UCI repository. Out of the databases, the $t \mathrm{BCM}^{2}$ accomplishes higher accuracy than the CL multinet on 24 databases, identical accuracy on 3 databases and inferior accuracy on 5 databases. It achieves higher accuracy than the TAN on 28 databases and inferior accuracy on 4 databases. The $t \mathrm{BCM}^{2}$ also outperforms the NBC on $90 \%$ of the databases. Twenty-two databases are tested using CV10 and the remaining (large) databases using holdout. On the former databases, the $t \mathrm{BCM}^{2}$ reaches higher accuracy than the CL multinet classifier on 16 of the databases with statistical significance of $95 \%$ (t-test with $\alpha=0.05$ ) on 12 of the databases and the CL multinet classifier achieves higher accuracy than the $t \mathrm{BCM}^{2}$ on 4 of the databases without statistical significance for none of them. Also for these 22 databases, the $t \mathrm{BCM}^{2}$ accomplishes higher accuracy than the TAN on 18 of the databases with statistical significance of $95 \%(\alpha=0.05)$ for 13 of them and the TAN achieves higher accuracy than the $t \mathrm{BCM}^{2}$ on 4 of the databases with statistical significance of $95 \%$ $(\alpha=0.05)$ for 1 of the databases.

In addition, Table 1 exemplifies the $t \mathrm{BCM}^{2}$ superiority to the RBMN [8] for those databases for which results are provided. Also, we compare the $t \mathrm{BCM}^{2}$ to the DCLT algorithm [5] for the only two databases for which results are given in [5]. We find for the Hepatitis database accuracies of $89.25 \%$ and $90.4 \%$ and for the Voting database accuracies of $92.18 \%$ and $93.97 \%$ for the DCLT and $t \mathrm{BCM}^{2}$ classifiers, respectively. Finally, Table 1 presents also the average classification accuracies of the inspected methods over all 32 databases. The table shows that the $t \mathrm{BCM}^{2}(89.64 \%)$ is superior on average to the NBC $(85.74 \%)$, TAN $(87.41 \%)$ and CL multinet $(87.45 \%)$.

Table 1. Classification accuracies of the $t \mathrm{BCM}^{2}$ and other classifiers on 32 databases from [13]. Bold font represents the highest accuracy for a database.


# 5 Summary and Concluding Remarks 

We propose the $t \mathrm{BCM}^{2}$ which is a multinet classifier that learns each local network based on a detection-rejection measure, i.e., the accuracy in simultaneously detecting and rejecting, respectively, the corresponding class and other class patterns. The $t \mathrm{BCM}^{2}$ uses the SuperParent algorithm to learn for each local network a TAN having only augmented edges that increase the classifier accuracy. Evaluated on 32 realworld databases, the $t \mathrm{BCM}^{2}$ demonstrates on average superiority to the NBC, TAN, CL multinet and RBMN classifiers. The advantage of the $t \mathrm{BCM}^{2}$ to the TAN is related to the facts that the former classifier is a multinet that is learned using a discrimination-driven score, and the advantage of the $t \mathrm{BCM}^{2}$ to the CL multinet is attributed to the score of the former and the facts that it usually learns a smaller number of parameters and use the whole data for training.

In further work, we will make parameter learning discriminative rather than generative and apply the $\mathrm{BCM}^{2}$ to less restricted structure spaces, such as augmented naïve and general Bayesian networks.

Acknowledgment. This works was supported in part by the Paul Ivanier Center for Robotics and Production Management, Ben-Gurion University, Beer-Sheva, Israel.
