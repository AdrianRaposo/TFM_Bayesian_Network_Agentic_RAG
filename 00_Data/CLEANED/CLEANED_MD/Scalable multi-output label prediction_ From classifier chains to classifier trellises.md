# SCALABLE MULTI-OUTPUT LABEL PREDICTION: FROM CLASSIFIER CHAINS TO CLASSIFIER TRELLISES 

J. Read ${ }^{1}$, L. Martino ${ }^{2}$, P. M. Olmos ${ }^{3}$, David Luengo ${ }^{4}$<br>${ }^{1}$ Dep. of Computer Science, Aalto University and HIIT, Helsinki, Finland (jesse.read@aalto.fi).<br>${ }^{2}$ Dep. of Mathematics and Statistics, University of Helsinki, Helsinki (Finland).<br>${ }^{3}$ Dep. of Signal Theory and Communications, Universidad Carlos III de Madrid (Spain) .<br>${ }^{4}$ Dep. of Circuits and Systems Engineering, Universidad Politécnica de Madrid, (Spain).

## ABSTRACT

Multi-output inference tasks, such as multi-label classification, have become increasingly important in recent years. A popular method for multi-label classification is classifier chains, in which the predictions of individual classifiers are cascaded along a chain, thus taking into account inter-label dependencies and improving the overall performance. Several varieties of classifier chain methods have been introduced, and many of them perform very competitively across a wide range of benchmark datasets. However, scalability limitations become apparent on larger datasets when modeling a fully-cascaded chain. In particular, the methods' strategies for discovering and modeling a good chain structure constitutes a mayor computational bottleneck. In this paper, we present the classifier trellis (CT) method for scalable multi-label classification. We compare CT with several recently proposed classifier chain methods to show that it occupies an important niche: it is highly competitive on standard multi-label problems, yet it can also scale up to thousands or even tens of thousands of labels.

Keywords: classifier chains; multi-label classification; multi-output prediction; structured inference; Bayesian networks

## 1. INTRODUCTION

Multi-output classification (MOC) (also known variously as multi-target, multi-objective, and multidimensional classification) is the supervised learning problem where an instance is associated with a set of qualitative discrete variables (a.k.a. labels), rather than with a single variable ${ }^{1}$. Since these label variables are often strongly correlated, modeling the dependencies between them allows MOC methods to improve their performance at the expense of an increased computational cost. Multi-label classification (MLC) is a special case of MOC where all the labels are binary; it has already attracted a great deal of interest and development in machine learning literature over the last few years. In [27], the authors give a recent review of, and many references to, a number of recent and popular methods for MLC. Figure 1 shows the relationship between different classification paradigms, according to the number of labels ( $L=1$ vs. $L>1$ ) and their type (binary $[K=2]$ or not $[K>2]$ ).

There are a vast range of active applications of MLC, including tagging images, categorizing documents, and labelling video and other media, and learning the relationship among genes and biological functions. Labels (e.g., tags, categories, genres) are either relevant or not. For example, an image may be labelled beach and urban; a news article may be sectioned under europe and economy. Relevance is usually indicated by 1 , and irrelevance by 0 . The general MOC scheme may add other information such as month, age, or gender. Note that month $\in\{1, \ldots, 12\}$ and therefore is not simply irrelevant or not. This MOC task has received relatively less attention than MLC (although there is some work emerging, e.g., [25] and [17]). However, most MLC-transformation methods (e.g., treating each label variable as a separate multi-class problem) are equally applicable to MOC. Indeed, in this paper we deal with a family of methods based on this approach. Note also that, as any integer can be represented in binary form (e.g., $3 \Leftrightarrow[0,0,0,1,1]$ ), any MOC task can 'decode' into a MLC task and vice versa.

In this paper, we focus on scalable MLC methods, able to effectively deal with large datasets at feasible complexity. Many recent MLC methods, particularly those based on classifier chains, tend to be over engineered, investing evermore computational power to model label dependencies, but presenting poor scalability properties. In the first part of the paper, we review some

[^0]
[^0]:    ${ }^{1}$ We henceforth try to avoid the use of the term 'class'; it generates confusion since it is used variously in the literature to refer to both the target variable, and a value that the variable takes. Rather, we refer to label variables, each of which takes a number of values.

state-of-the-art methods from the MLC and MOC literature to show that the more powerful solutions are not well-suited to deal with large-size label sets. For instance, classifier chains [3, 20] consider a full cascade of labels along a chain to model their joint probability distribution and, either they explore all possible label orders in the chain, incurring in exponential complexity with the number of labels, or they compare a small subset of them chosen at random, which is ineffective for large dimensional problems.

The main contribution of the paper is a novel highly-scalable method: the classifier trellis (CT). Rather than imposing a long-range and ultimately computationally complex dependency model, as in classifier chains, CT captures the essential dependencies among labels very efficiently. This is achieved by considering a predefined trellis structure for the underlying graphical model, where dependent nodes (labels) are sequentially placed in the structure according to easily-computable probabilistic measures. Experimental results across a wide set of datasets show that CT is able to scale up to large sets (namely, thousands and tens of thousands of labels) while remaining very competitive on standard MLC problems. In fact, in most of our experiments, CT was very close to the running time of the naive baseline method, which neglects any statistical dependency between labels. Also, an ensemble version of CT, where the method is run multiple times with different random seeds and classification is done through majority voting, does not significantly outperform the single-shot CT. This demonstrates that our method is quite robust against initialization.

The paper is organized as follows. First, in Section 2 we formalize the notation and describe the problem's setting. In Section 3 we review some state-of-the-art methods from the MLC and MOC literature, as well as their various strategies for modeling label dependence. This review is augmented with empirical results. In Section 4 we make use of the studies and theory from earlier sections to present the classifier trellis (CT) method. In Section 5 we carry out two sets of experiments: firstly we compare CT to some state-of-the-art multi-label methods on an MLC task; and secondly, we show that CT can also provide competitive performance on typical structured output prediction task (namely localization via segmentation). Finally, in Section 6 we discuss the results and take conclusions.

Two appendixes have been included to help the readability of the paper and support the presented results. In A, we compare two low-complexity methods to infer the label dependencies from training data. In B we review Monte Carlo methods, which are required in this paper to perform probabilistic approximate inference of the label set associated to a new test input.

# 2. PROBLEM SETUP AND NOTATION 

Following a standard machine learning notation, the $n$-th feature vector can be represented as

$$
\mathbf{x}^{(n)}=\left[x_{1}^{(n)}, \ldots, x_{D}^{(n)}\right]^{\top} \in \boldsymbol{\mathcal { X }}=\mathcal{X}_{1} \times \cdots \times \mathcal{X}_{D} \subseteq \mathbb{R}^{D}
$$

where $D$ is the number of features and $\mathcal{X}_{d}(d=1, \ldots, D)$ indicates the support of each feature. In the traditional multi-class classification task, we have a single target variable which can take one out of $K$ values, i.e.,

$$
y^{(n)} \in \mathcal{Y}=\{1, \ldots, K\}
$$

and for some test instance $\mathbf{x}^{*}$ we wish to predict

$$
\hat{y}=h\left(\mathbf{x}^{*}\right)=\underset{y \in \mathcal{Y}}{\operatorname{argmax}} p\left(y \mid \mathbf{x}^{*}\right)
$$

![img-0.jpeg](img-0.jpeg)

Fig. 1: Different classification paradigms: $L$ is the number of labels and $K$ is the number of values that each label variable can take.

![img-1.jpeg](img-1.jpeg)

Fig. 2: Toy example of multi-label classification (MLC), with $K=2$ possible values for each label and $L=3$ labels (thus $y_{j} \in\{0,1\}$ for $j=1,2,3$ ) and, implicitly, $D=2$ features. Circles, squares and triangles are elements with only one active label (i.e., either $y_{1}=1$ or $y_{2}=1$, but not both). Hexagons show vectors such that $y_{1}=y_{2}=1$.
in such a way that it coincides with the true (unknown) test label with a high probability ${ }^{2}$. Furthermore, the conditional distribution $p(y \mid \mathbf{x})$ is usually unknown and has to be estimated during the classifier construction stage. In the standard setting, classification is a supervised task where we have to infer the model $h$ from a set of $N$ labelled examples (training data) $\mathcal{D}=\left\{\left(\mathbf{x}^{(n)}, y^{(n)}\right)\right\}_{n=1}^{N}$, and then apply it to predict the labels for a set of novel unlabelled examples (test data). This prediction phase is usually straightforward in the single-output case, since only one of $K$ values needs to be selected.

In the multi-output classification (MOC) task, we have $L$ such output labels,

$$
\mathbf{y}^{(n)}=\left[y_{1}^{(n)}, \ldots, y_{L}^{(n)}\right]
$$

where

$$
y_{\ell}^{(n)} \in \mathcal{Y}_{\ell}=\left\{1, \ldots, K_{\ell}\right\}
$$

with $K_{\ell} \in \mathbb{N}_{+}$being the finite number of values associated with the $\ell$-th label. For some test instance $\mathbf{x}^{*}$, and provided that we know the conditional distribution $p(\mathbf{y} \mid \mathbf{x})$, the MOC solution is given by

$$
\hat{\mathbf{y}}=h\left(\mathbf{x}^{*}\right)=\underset{\mathbf{y} \in \mathcal{Y}}{\operatorname{argmax}} p\left(\mathbf{y} \mid \mathbf{x}^{*}\right)
$$

Once more, $p(\mathbf{y} \mid \mathbf{x})$ is usually unknown and has to be estimated from the training data, $\mathcal{D}=\left\{\left(\mathbf{x}^{(n)}, \mathbf{y}^{(n)}\right)\right\}_{n=1}^{N}$, in order to construct the model $h$. Therein precisely lies the main challenge behind MOC, since $h$ must select one out of $|\mathcal{Y}|=K^{L}$ possible values ${ }^{3}$; clearly a much more difficult task than in Eq. (1). Furthermore, finding $\hat{\mathbf{y}}$ for a given $\mathbf{x}^{*}$ and $p(\mathbf{y} \mid \mathbf{x})$ is quite challenging from a computational point of view for large values of $K$ and $L[17,25]$.

In MLC, all labels are binary labels, namely $K_{\ell}=2$ for $\ell=1, \ldots, L$, with the two possible label values typically notated as $y_{\ell} \in\{0,1\}$ or $y_{\ell} \in\{-1,+1\}$. Figure 2 shows one toy example of MLC with three labels (thus $\mathbf{y} \in\{0,1\}^{3}$ ). Because of the strong co-occurrence, we can interpret that the first label $\left(y_{1}=1\right)$ implies the second label $\left(y_{2}=1\right)$ with high probability, but not the other way around. When learning the model $h(\mathbf{x})$ in (2), the goal of MLC (and MOC in general) is capturing this kind of dependence among labels in order to improve classification performance; and to do this efficiently enough to scale up to the size of the data in the application domains of interest. This typically means connecting labels (i.e., learning labels together) in an appropriate structure. Table 1 summarizes the main notation used in the paper.

# 3. BACKGROUND AND RELATED WORK 

In this section, we step through some of the most relevant methods for MLC/MOC recently developed, as well as several works specifically related to the novel method, presented in later sections. All the methods discussed here, and also the CT method presented in Section 4, aim to build a model for $h(\mathbf{x})$ in (2) by first selecting a suitable model for the label joint posterior distribution $p(\mathbf{y} \mid \mathbf{x})$ and then using this model to provide a prediction $\hat{\mathbf{y}}$ to a new test input $\mathbf{x}^{*}$. It is in the first step where state-of-the-art methods present a complexity bottleneck to deal with large sets of labels and where CT offers a significantly better complexity-performance trade-off.

[^0]
[^0]:    ${ }^{2}$ Eq. (1) corresponds to the widely used maximum a posteriori (MAP) estimator of $y^{*}$ given $\mathbf{x}^{*}$, but other approaches are possible.
    ${ }^{3} \mathrm{~A}$ simplification of $K_{1} \times K_{2} \times \cdots \times K_{L}$ (to keep notation cleaner).

Table 1: Summary of the main notation.


![img-2.jpeg](img-2.jpeg)
(a) Independent Classifiers (IC)
![img-3.jpeg](img-3.jpeg)
(c) Bayesian Classifier Chain (BCC)
![img-4.jpeg](img-4.jpeg)
(b) Classifier Chain (CC)
![img-5.jpeg](img-5.jpeg)
(d) Conditional Dependency Network (CDN)

Fig. 3: Several multi-label methods depicted as directed/undirected graphical models.

# 3.1. Independent Classifiers 

A naive solution to multi-output learning is training $L K$-class models as in Eq. (1), i.e., $L$ independent classifiers (IC), ${ }^{4}$ and using them to classify $L$ times a test instance $\mathbf{x}^{*}$, as $\left[\hat{y}_{1}, \ldots, \hat{y}_{L}\right]=\left[h_{1}\left(\mathbf{x}^{*}\right), \ldots, h_{L}\left(\mathbf{x}^{*}\right)\right]$. IC is represented by the directed graphical model shown in Figure 3 (a). Note that this approach implicitly assumes the independence among the target variables, i.e., $p(\mathbf{y} \mid \mathbf{x}) \equiv \prod_{\ell=1}^{L} p\left(y_{\ell} \mid \mathbf{x}\right)$, which is not the case in most (if not all) multi-output datasets.

### 3.2. Classifier Chains

The classifier chains methodology is based on the decomposition of the conditional probability of the label vector $\mathbf{y}$ using the product rule of probability:

$$
\begin{aligned}
p(\mathbf{y} \mid \mathbf{x}) & =p\left(y_{1} \mid \mathbf{x}\right) \prod_{\ell=2}^{L} p\left(y_{\ell} \mid y_{1}, \ldots, y_{\ell-1}, \mathbf{x}\right) \\
& \approx f_{1}(\mathbf{x}) \prod_{\ell=2}^{L} f_{\ell}\left(\mathbf{x}, y_{1}, \ldots, y_{\ell-1}\right)
\end{aligned}
$$

which is approximated with $L$ probabilistic classifiers, $f_{\ell}\left(\mathbf{x}, y_{1}, \ldots, y_{\ell-1}\right)$. As a graphical model, this approach is illustrated by Figure 3 (b).

[^0]
[^0]:    ${ }^{4}$ In the MLC literature, the IC approach is also known as the binary relevance method.

The complexity associated to learn Eq. (4) increases with $L$, but with a fast greedy inference, as in [20], it reduces to

$$
\hat{y}_{\ell}=\underset{y_{\ell}}{\operatorname{argmax}} p\left(y_{\ell} \mid y_{1}, \ldots, y_{\ell-1}, \mathbf{x}\right)
$$

for $\ell=1, \ldots, L$. This is not significant for most datasets, and time complexity is close to that of IC in practice. In fact, it would be identical if not for the extra $y_{1}, \ldots, y_{\ell}-1$ attributes.

With greedy inference comes the concern of error propagation along the chain, since an incorrect estimate $\hat{y}_{\ell}$ will negatively affect all following labels. However, this problem is not always serious, and easily overcome with an ensemble [20, 3]. Therefore, although there exist a number of approaches for avoiding error propagation via exhaustive iteration or various search options $[3,13,17]$, we opt for the ensemble approach.

# 3.3. Bayesian Classifier Chains 

Instead of considering a fully parameterized Markov chain model for $p(\mathbf{y} \mid \mathbf{x})$, we can use a simpler Bayesian network. Hence, (3) becomes

$$
p(\mathbf{y} \mid \mathbf{x})=\prod_{\ell=1}^{L} p\left(y_{\ell} \mid \mathbf{y}_{\mathrm{pa}(\ell)}, \mathbf{x}\right)
$$

where $\mathrm{pa}(\ell)$ are the parents of the $\ell$-th label, as proposed in [25, 26], known as as Bayesian Classifier Chains (BCC), since it may remind us of Bayesian networks. Using a structure makes training the individual classifiers faster, since there are fewer inputs to them, and also speeds up any kind of inference. Figure 3 (c) shows one example of many possible such network structures.

Unfortunately, finding the optimal structure is NP hard due to an impossibly large search space. Consequently, a recent point of interest has been finding a good suboptimal structure, such that Eq. (6) can be used. The literature has focused around the idea of label dependence (see [5] for an excellent discussion). The least complex approach is to measure marginal label dependence, i.e., the relative co-occurrence frequencies of the labels. Such approach has been considered in [25, 8]. In the latter, the authors exploited the frequent sets approach [1], which measures the co-occurrence of several labels, to incorporate edges into the Bayesian network. However, they noted problems with attributes and negative co-occurrence (i.e., mutual exclusiveness; labels whose presence indicate the absence of others). The resulting algorithm (hereafter referred to as the FS algorithm) can deal with moderately large datasets, but the final network construction approach ends up being rather involved.

Finding a graph based on conditional label dependence is inherently more demanding, because the input feature space must be taken into account, i.e., classifiers must be trained. Of course, training time is a strongly limiting factor here. However, a particularly interesting approach to modelling conditional dependence, the so-called LEAD method, was presented in [26]. This scheme tries to remove first the dependency of the labels on the feature set, which is the common parent of all the labels, to facilitate learning the label dependencies. In order to do so, LEAD trains first an independent classifier for each label (i.e., it builds $L$ independent models, as in the IC approach), and then uses the dependency relations in the residual errors of these classifiers to learn a Bayesian network following some standard approach (the errors can in fact be treated exactly as if they were labels and plugged, e.g., into the FS approach). LEAD is thus a fast method for finding conditional label dependencies, and has shown good performance on small-sized datasets.

Neither the FS nor the LEAD methods assume any particular constraint on the underlying graph and are well suited for MOC in the high dimensional regime because of their low complexity. However, if the underlying directed graph is sparse, the PC algorithm and its modifications [12, 24] are the state-of-the-art solution in directed structured learning. The PC-algorithm runs in the worst case in exponential time (as a function of the number of nodes), but if the true underlying graph is sparse, this reduces to a polynomial runtime. However, this is typically not the case in MLC/MOC problems.

For the sake of comparison between the different MLC/MOC approaches, in this paper we only consider the FS and LEAD methods to infer direct dependencies between labels. In order to delve deeper into the issue of structure learning using the FS and LEAD methods, in A we have generated a synthetic dataset, where the underlying structure is known, and compare their solutions and the degree of similarity with respect to the true graphical model. As these experiments illustrate, one of the main problems behind learning the graphical model structure from scratch is that we typically get too dense networks, where we cannot control the complexity associated to training and evaluating each one of the probabilistic classifiers corresponding to the resulting factorization in (6). This issue is solved by the classifier trellis method proposed in Section 4.

# 3.4. Conditional Dependency Networks (CDN) 

Conditional Dependency Networks represent an alternative approach, in which the conditional distribution $p(\mathbf{y} \mid \mathbf{x})$ factorizes according to an undirected graphical model, i.e.,

$$
p(\mathbf{y} \mid \mathbf{x})=\frac{1}{Z} \prod_{q=1}^{Q} \phi_{q}\left(\mathbf{y}_{q} \mid \mathbf{x}\right)
$$

where $Z$ is a normalizing constant, $\phi_{I}(\cdot)$ is a positive function or potential, and $\mathbf{y}_{q}$ is a subset of the labels (a clique in the undirected graph). The notion of directionality is dropped, thus simplifying the task of learning the graph structure. Undirected graphical models are more natural for domains such as spatial or relational data. Therefore, they are well suited for tasks such as image segmentation (e.g., [4], [14]), and regular MLC problems (e.g., [7]).

Unlike classifier chain methods, a CDN does not construct an approximation to $p(\mathbf{y} \mid \mathbf{x})$ based on a product of probabilistic classifiers. In contrast, for each conditional probability of the form

$$
p\left(y_{\ell} \mid y_{1}^{(\ell)}, \ldots, y_{\ell-1}^{(\ell)}, y_{\ell+1}^{(\ell-1)}, \ldots, y_{L}^{(\ell-1)}, \mathbf{x}\right)
$$

a probabilistic classifier is learnt. In an undirected graph, where all the labels that belong to the same clique are connected to each other, it is easy to check that

$$
p\left(y_{\ell} \mid y_{1}^{(\ell)}, \ldots, y_{\ell-1}^{(\ell)}, y_{\ell+1}^{(\ell-1)}, \ldots, y_{L}^{(\ell-1)}, \mathbf{x}\right)=p\left(y_{\ell} \mid \mathbf{y}_{\mathrm{ne}(\ell)}, \mathbf{x}\right)
$$

where $\mathbf{y}_{\mathrm{ne}(\ell)}$ is the set of variables connected to $y_{\ell}$ in the undirected graph ${ }^{5}$. Finally, $p\left(y_{\ell} \mid \mathbf{y}_{\mathrm{ne}(\ell)}, \mathbf{x}\right)$ for $\ell=1, \ldots, L$ is approximated by a probabilistic classifier $f_{\ell}\left(\mathbf{y}_{\mathrm{ne}(\ell)}, \mathbf{x}\right)$.

In order to classify a new test input $\mathbf{x}^{*}$, approximate inference using Gibbs sampling is a viable option. In B, we present the formulation of Monte Carlo approaches (including Gibbs sampling) specially tailored to perform approximate inference in MLC/MOC methods based on Bayesian networks and undirected graphical models.

### 3.5. Other MLC/MOC Approaches

A final note on related work: there are many other 'families' of methods designed for multi-label, multi-output and structured output prediction and classification, including many 'algorithm adapted' methods. A fairly complete and recent overview can be seen in [27] for example. However, most of these methods suffer from similar challenges as the classifier chains family; and similarly attempt to model dependence yet remain tractable by using approximations and some form of randomness [22, 18, 23]. To cite a more recent example, [21] uses 'random graphs' in a way that resembles [9]'s CDN, since it uses undirected graphical models, and [25]'s BCC in the sense of the randomness of the graphs considered.

### 3.6. Comparison of State-of-the-art Methods for Extracting Structure

It is our view that many methods employed for multi-label chain classifiers have not been properly compared in the literature, particularly with regard to their method for finding structure. There is not yet any conclusive evidence that modelling the marginal dependencies (among $Y$ ) is enough, or whether it is advisable to model the conditional dependencies also (for best performance); and how much return one gets on a heavy investment in searching for a 'good' graph structure, over random structures.

We performed two experiments to get an idea; comparing the following methods:


Results are shown in Table 2 of $5 \times$ CV (Cross validation) on two small real-world datasets (Music and Scene); small to ensure a comparison with OCC ( $L!=720$ possible chain orderings).

[^0]
[^0]:    ${ }^{5}$ In other words, $\mathbf{y}_{\mathrm{ne}(\ell)}$ is the so called Markov blanket of $y_{\ell}[2]$.

Table 2: Comparison of the classification accuracy of existing methods with $5 \times$ CV (Cross validation). We chose the two smallest datasets so that the 'optimal' OCC could complete.


Figure 4 shows an example of the structure found by BCC-FS and BCC-LEAD in a real dataset, namely Music (emotions associated with pieces of music). As a base classifier, we use support vector machines (SVMs), fitted with logistic models (as according to [11]) in order to obtain a probabilistic output, with the default hyper-parameters provided in the SMO implementation of the Weka framework [10]. Table 2 confirms that IC's assumption of independence harms its performance, and that the bulk of the MOC literature is justified in trying to overcome this. However, it also suggests that investing factorial and exponential time to find the best-fitting chain order and label combination (respectively) does not guarantee the best results. In fact, by comparing the results of ECC with EBCC-LEAD and EBCC-FS, even the relatively higher investment in conditional label dependence over marginal dependence (EBCC-LEAD vs EBCC-FS) does not necessarily pay off. Finally, ECC's performance is quite close to MCC. Surprisingly, the ECC method tends to provide excellent performance, even though it only learns randomly ordered (albeit fully connected) chains. However, as discussed in Section 3.2, its complexity is prohibitively large in high dimensional MLC problems.
![img-6.jpeg](img-6.jpeg)

Fig. 4: Graphs derived from the Music dataset, with links based on (a) marginal dependence (FS, label-frequency) and (b) conditional dependence (LEAD, error-frequency). Here we have based the links on mutual information, therefore links represent both co-occurrences (e.g., quiet $\rightarrow$ sad) and mutual exclusiveness (e.g., happy $\rightarrow$ sad). Generally, we see that the graph makes intuitive sense; amazed and happy are neither strongly similar nor opposite emotions, and thus there is not much benefit in modelling them together; same with angry and sad.

# 4. A SCALABLE APPROACH: CLASSIFIER TRELLIS (CT) 

The goal for a highly scalable CC-based method brings up the common question: which structure to use. On the one hand, ignoring important dependency relations will harm performance on typical MLC problems. On the other hand, assumptions must be made to scale up to large scale problems. Even though in certain types of MLC problems there is a clear notion of the local structure underlying the labels (e.g., in image segmentation pixels next to each other should exhibit interdependence), this assumption is not valid for general MLC problems, where the 4th and 27th labels might be highly correlated for example. Therefore, we cannot escape the need to discover structure, but we must do it efficiently. Furthermore, the structure used should allow for fast inference.

Our proposed solution is the classifier trellis (CT). To relieve the burden of specification 'from scratch', we maintain a fixed structure, namely, a lattice or trellis (hence the name). This escapes the high complexity of a complete structure learning (as in

![img-7.jpeg](img-7.jpeg)

Fig. 5: Three possible directed trellises for $L=9$. Each trellis is defined by a fixed pattern for the parents of each vertex (varying only near the edges, where parents are not possible). Note that no directed loops can exist.
[20] and [3]), and at the same time avoids the complexity involved in discovering a structure (e.g., [25] and [26]). Instead, we a impose a structure a-priori, and only seek an improvement to the order of labels within that structure.

Figure 5 gives three simple example trellises for $L=9$ (specifically, we use the first one in experiments). Each of the vertices $\ell \in\{1, \ldots, L\}$ of the trellis corresponds to one of the labels of the dataset. Note the relationship to Eq. (6); we simply fix the same pattern to each $\mathrm{pa}(\ell)$. Namely, the parents of each label are the labels laying on the vertices above and to the left in the trellis structure (except, obviously, the vertices at the top and left of the trellis which form the border). A more linked structure will model dependence among more labels.

Hence, instead of trying to solve the NP hard structure discovery problem, we use a simple heuristic (label-frequencybased pairwise mutual information) to place the labels into a fixed structure (the trellis) in a sensible order: one that tries to maximize label dependence between parents and children. This ensures a good structure, which captures some of the main label dependencies, while maintaining scalability to a large number of labels and data. Namely, we employ an efficient hill climbing method to insert nodes into this trellis according to marginal dependence information, in a manner similar to the FS method in [1].

The process followed is outlined in Algorithm 1, to which we pass a pairwise matrix of mutual information, where

$$
I\left(Y_{\ell} ; Y_{k}\right)=\sum_{y_{\ell} \in \mathcal{Y}_{\ell}} \sum_{y_{k} \in \mathcal{Y}_{k}} p\left(y_{\ell}, y_{k}\right) \log \left(\frac{p\left(y_{\ell}, y_{k}\right)}{p\left(y_{\ell}\right) p\left(y_{k}\right)}\right)
$$

Essentially, new nodes are progressively added to the graph based on the mutual information. Since the algorithm starts by placing a random label in the upper left corner vertex, a different trellis will be discovered for different random seeds. Each label $y_{\ell}$ is directly connected to a fixed number of parent labels in the directed graph (e.g., in Figure 5 each node has two parents in the first two graphs, and four in the third one) - except for the border cases where no parents are possible. The computational cost of this algorithm is $O\left(L^{2}\right)$, but due to the simple calculations involved, in practice it is easily able to scale up to tens of thousands of labels. Indeed, we show later in Section 5 that this method is fast and effective. Furthermore, it is possible to limit the complexity by searching for some number $<L$ of labels (e.g., building clusters of labels).

Given a proper user-defined parent pattern $\mathrm{pa}(\ell)$ (see Figure 5), we are ensured that the trellis obtained in Algorithm 1 is a directed acyclic graph. Hence, there is no need to check for cycles during construction, which is a very time consuming stage in many algorithms (e.g., in the PC algorithm, see Section 3.3). We can now employ probabilistic classifiers to construct an approximation to $p(\mathbf{y} \mid \mathbf{x})$ according to the directed graph. This approach is simply referred to as the Classifier Trellis (CT). Afterwards, we can either do inference greedily or via Monte Carlo sampling (see B for a detailed discussion of Monte Carlo methods).

Alternatively, note that we can interpret the trellis structure provided by Algorithm 1 in terms of an undirected graph, following the approach of Classifier Dependency Networks, described in Section 3.4. For example, in Figure 5 (middle), we would get (with directionality removed) $\operatorname{ne}(5)=\{2,4,6,8\}$. This compares ${ }^{6}$ to $\mathrm{pa}(5)=\{1,2,4\}$. We refer to this approach as the Classifier Dependency Trellis (CDT).

Both CT and CDT are outlined in Algorithm 2 and Algorithm 3 respectively. Some may argue that the undirected version is more powerful, since learning an undirected graph is typically easier than learning a directed graph that encodes causal relations. However, CDTconstructs an undirected graphical model where greedy inference cannot be implemented and we have to rely on (slower) Monte Carlo sampling methods in the test stage. This effect can be clearly noticed in Table 8.

[^0]
[^0]:    ${ }^{6}$ We did not add the diagonals in the set $\operatorname{ne}(5)$, since we wish that it be comparable in terms of the number of connections

# Algorithm 1 Constructing a Classifier Trellis 

input : $\boldsymbol{Y}$ (an $L \times N$ matrix of labels), $W$ (width, default: $\sqrt{L}$ ), a parent-node function $\mathrm{pa}(\cdot)$ begin
$\boldsymbol{I} \leftarrow \operatorname{LEARNDEPENDENCYMATRIX}(\boldsymbol{Y})$;
$S=\operatorname{SHUFFLE}(\{1, \ldots, L\})$;
$s_{1}=S_{1}$
for $\ell=2, \ldots, L$; do
$S=S \backslash s_{\ell-1}$
$s_{\ell}=\operatorname{argmax}_{k \in S} \sum_{j \in \operatorname{pa}(\ell)} I\left(y_{j} ; y_{k}\right)$
end
end
output: the trellis structure, $\left[\begin{array}{ccccc}s_{1} & s_{2} & \cdots & s_{W-1} & s_{W} \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ s_{L-W} & s_{L-W+1} & \cdots & s_{L-1} & s_{L}\end{array}\right]$.
We henceforth assume that $y_{\ell}=y_{s_{\ell}}$.

## Algorithm 2 Classifier Trellis (CT)

$\operatorname{TRAIN}(\mathcal{D})$ begin
Find the directed trellis graph using Algorithm 1.
Train classifiers $f_{1}, \ldots, f_{L}$, each taking all parents in the directed graph as additional features, such that

$$
f_{\ell}(\mathbf{x}) \approx p\left(y_{\ell} \mid y_{\mathrm{pa}(\ell)}, \mathbf{x}\right)
$$

end
$\operatorname{TEST}\left(\mathbf{x}^{*}\right)$ begin
for $\ell=\left\{s_{1}, \ldots, s_{L}\right\}$; do
$\hat{y}_{\ell}=\operatorname{argmax}_{y_{\ell}} p\left(y_{\ell} \mid \mathbf{y}_{\mathrm{pa}(\ell)}, \mathbf{x}^{*}\right)$
end
return $\hat{\mathbf{y}}=\left[\hat{y}_{1}, \ldots, \hat{y}_{L}\right]$
end

Finally, we will consider a simple ensemble method for CT, similar to that proposed in [19] or [25] to improve classifier chain methods: $M$ CT classifiers, each built from a different random seed, where the final label decision is made by majority voting. This makes the training time and inference $M$ times larger. We denote this method as ECT. A similar approach could be followed for the CDT (thus building an ECDT), but, given the higher computational cost of CDT during the test stage, we have concerns regarding the scalability of this approach, so we have excluded it from the simulations.

## 5. EXPERIMENTS

Firstly, in Section 5.1, we compare E/CT and CDT with some high-performance MLC methods (namely ECC, BCC, MCC) that were discussed in Section 3. We show that an imposed trellis structure can compete with fully-cascaded chains such as ECC and MCC, and discovered structures like those provided by BCC. Our approach based on trellis structures achieves similar MLC performance (or better in many cases) while presenting improved scalable properties and, consequently, significantly lower running times.

All the methods considered are listed in Table 3. In Table 4 we summarize their complexity. $D N$ represents the input dimensions (the dataset-dependent number of features times number of instances); we use $M=10$ ensemble methods and $T=100$ Gibbs iterations for CDT. While this complexity is just an intuitive measure, the experimental results reported in Section 5.1 confirm that CT running times are indeed very close to IC.

Table 5 summarizes the collection of datasets that we use, of varied type and dimensions; most of them familiar to the MLC/MOC community [22, 3, 20].

The last two sets (Local400 and Local10k) are synthetically generated and they correspond to the localization problem

# Algorithm 3 Classifier Dependency Trellis (CDT) 

$\operatorname{TRain}(\mathcal{D})$ begin
Find the undirected trellis graph using Algorithm 1.
Train classifiers $f_{1}, \ldots, f_{L}$, each taking all neighbouring labels as additional features, such that

$$
f_{\ell}(\mathbf{x}) \approx p\left(y_{\ell} \mid \mathbf{y}_{n \theta}(\ell), \mathbf{x}\right)
$$

end
$\operatorname{TEST}\left(\mathbf{x}^{*}\right)$ begin
for $t=1, \ldots, T_{c}, \ldots, T$; do
for $\ell=\operatorname{SHUFFLE}\{1, \ldots, L\}$; do
$y_{\ell}^{(t)} \sim p\left(y_{\ell} \mid \mathbf{y}_{n \theta}(\ell), \mathbf{x}^{*}\right)$
end
end
return $\hat{\mathbf{y}}=\frac{1}{T-T_{c}}\left[\sum_{T_{c}<t<T} y_{1}^{(t)}, \ldots, \sum_{T_{c}<t<T} y_{L}^{(t)}\right]$
end
where $T_{c}, T$ : settling time (discarded samples) and total iterations.

Table 3: Methods tested in experiments.


Table 4: Complexity per algorithm, roughly sorted by training complexity. $D N$ represents the input dimensions (number of features times number of instances). Train complexity indicates roughly how many values are looked at by a classifier. Test complexity indicates how many (times) individual models are addressed as inference.


Table 5: A collection of datasets and associated statistics, where LC is label cardinality: the average number of labels relevant to each example.


described in Section 5.2.
We use some standard metrics from the multi-label literature (see, e.g., [15]), namely,

$$
\begin{gathered}
\text { HAMMING SCORE }:=\frac{1}{N L} \sum_{n=1}^{N} \sum_{j=1}^{L}\left[y_{j}^{(n)}=\hat{y}_{j}^{(n)}\right] \\
\text { EXACT MATCH }:=\frac{1}{N} \sum_{n=1}^{N}\left[\mathbf{y}^{(n)}=\hat{\mathbf{y}}^{(n)}\right] \\
\text { Accuracy }^{7}:=\frac{1}{N} \sum_{i=1}^{N} \frac{\left|\mathbf{y}^{(n)} \wedge \hat{\mathbf{y}}^{(n)}\right|}{\left|\mathbf{y}^{(n)} \vee \hat{\mathbf{y}}^{(n)}\right|}
\end{gathered}
$$

where $[A]$ is an identity function, returning 1 if condition $A$ is true, whereas $\wedge$ and $\vee$ are the bitwise logical AND and OR operations, respectively.

# 5.1. Comparison of E/CT to other MLC methods 

First of all, to confirm that our proposed hill climbing strategy can actually have a beneficial effect (i.e., an improvement over a random trellis), we do a $10 \times 10$ cross validation (CV) on the smaller datasets. Results are displayed in Table 6. A significant increase in performance can be seen, with a decrease in the standard deviation (especially relevant in the Scene dataset). This confirms that the proposed hill climbing strategy can help in optimizing performance and decreasing the sensitivity of CT wrt the initialization.

[^0]
[^0]:    ${ }^{7}$ Known commonly as Jaccard Index in information retrieval circles.

Table 6: Comparing $C T$ accuracy (on Scene, Music) without (just a random trellis) and with our 'hill-climbing' (HC) method, over $10 \times 10 \mathrm{CV}$.


Then, we compare all the methods listed in Table 3 on all the datasets of Table 5. The results of predictive performance are displayed in Table 7, and running times can be seen in Table 8. On the small datasets $(L<100)$ we use Support Vector Machines as base classifiers, with fitted logistic models (as in [11]) for CDN (which requires probabilistic output for inference). As an alternative, other authors have used Logistic Regression directly (e.g., [3, 9]) due to its probabilistic output. In our experience, we obtain better and faster all-round performance with SVMs. Note that, for best accuracy, it is highly recommended to tune the base classifier. However, we wish to avoid this "dimension" and instead focus on the multi-label methods. On the larger datasets (where $L>100$ ) we instead use Stochastic Gradient Descent (SGD), with a maximum of only 100 epochs, to deal with the scale presented by these large problems. All our methods are implemented and made available within the Meka framework; ${ }^{8}$ an open-source multi-output learning framework based on the Weka machine learning framework [10]. The SMO SVM and SGD implementations pertain to Weka.

Results confirm that both ECT and CT are very competitive in terms of performance and running time. Using the Hamming score as figure of merit and given the running times reported, CT is clearly superior to the rest of methods. Note that Table 8 shows that CT's running times are close to IC, namely the method that neglects all statistical dependency between labels. With respect to exact match and accuracy performance results, which are measures oriented to the recovery of the whole set of labels, ECT and CT achieve very competitive results with respect to ECC and MCC, which are high-complexity methods that model the full-chain of labels. Table 8 reports training and test average times computed for the different MLC methods. We also include explicitly the number $L$ of labels per dataset. Note also that even though ECT considers a set of 10 possible random initializations, it does not significantly improve the performance of CT (a single initialization) for most cases, which suggest that the hill climbing strategy makes the CT algorithm quite robust with respect to initialization. Regarding scalability, note that the computed train/running times for CT scale roughly linearly with the number of labels $L$. For instance, in the MediaMill dataset $L=101$ while in Delicious $L$ is approximately one order of magnitude higher, $L=983$. As we can observe, CT running times are multiplied approximately by a factor of 10 between both datasets. The same conclusions can be drawn also for the largest datasets, compare for instance running times between Local400 and Local10k. Finally, CDT, our scalable modification of CDN, shows worse performance than CT while it requires larger test running times.

In order to illustrate the most significant statistical differences between all methods, in Figure 6 we include the results of the Nemenyi test based on Table 7 and Table 8. However, note that here we excluded the two rows with DNFs. The Nemenyi test [6] rejects the null hypothesis if the average rank difference is greater than the critical distance $q_{p} \sqrt{N_{A}\left(N_{A}+1\right) / 6 N_{D}}$ over $N_{A}$ algorithms and $N_{D}$ datasets, and $q_{p}$ according to the $q$ table for some $p$ value (we use $p=0.90$ ). Any method with a rank greater than another method by at least the critical distance, is considered statistically better. In Figure 6, for each method, we place a bar spanning from the average rank of the method, to this point plus the critical distance. Thus, any pair of bars that do not overlap correspond to methods that are statistically different in terms of performance. Note that, regarding both training and test running times, CT overlaps considerably with IC, whereas other methods such as ECC and MCC need significantly more training time. We can say that ECC and ECT are statistically stronger than IC and CDT, but not so wrt exact match. CT performs particularly well on the Hamming score, indicating that error propagation is limited, compared to other CC methods.

In the following section we present the framework behind the localization datasets Local400 and Local10k in the tables presented above.

[^0]
[^0]:    ${ }^{8}$ http://meka.sourceforge.net

Table 7: Predictive performance and dataset-wise (rank). DNF = Did Not Finish (within 24 hours or 2 GB memory).

Accuracy


Hamming Score


Exact Match


Table 8: Time results (seconds). DNF = Did Not Finish (within 24 hours or 2 GB memory).



# 5.2. A Structured Output Prediction Problem

We investigate the application of CT (and the other MLC methods) to a type of structured output prediction problem: segmentation for localization. In this section we consider a localization application using light sensors, based on the real-world scenario described in [16], where a number of light sensors are arranged around a room for the purpose of detecting the location of a person. We take a 'segmentation' view of this problem, and use synthetic models (which are based on real sensor data) to generate our own observations, thus creating a semi-synthetic dataset, which allows us to easily control the scale and complexity. Figure 7 shows the scenario. It is a top-down view of a room with light sensors arranged around the edges, one light source (a window, drawn as a thin rectangle) on the bottom edge and four targets. Note that targets can only be detected if they come between a light sensor and the light source, so the target in the lower right corner is undetectable.

We divide the scenario into $L=W \times W$ square 'tiles', representing $Y_{1}, \ldots, Y_{L}$. Given an instance $n$,

$$
\mathbf{y}^{(n)}=\left[\begin{array}{cccccc}
y_{1,1}^{(n)} & y_{1,2}^{(n)} & \ldots & \ldots & y_{1, W}^{(n)} \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
y_{W, 1}^{(n)} & y_{W, 2}^{(n)} & \ldots & \ldots & y_{W, W}^{(n)}
\end{array}\right]
$$

where $y_{i, j}^{(n)}=1$ if the $i, j$-th tile (i.e., pixel) is active, and $y_{i, j}^{(n)}=0$ otherwise, with $i, j \in{1, \ldots, W}$. For the $n$-th instance we have binary sensor observations $\mathbf{x}^{(n)}=\left[x_{1}^{(n)}, \ldots, x_{D}^{(n)}\right]$, where $x_{d}=1$ if the $d$-th sensor detects an object inside its 'detection zone' (shown in colors in Figure 7). Otherwise, $x_{d}=0$.

### 5.2.1. Sensor Model

Consider, for simplicity, a specific instance $\mathbf{y}=\left\{y_{i, j}\right\}_{i, j=1}^{W}$ (in order to avoid here the use of the super index $n$ ). Moreover, let us denote as $\mathbf{s}_{d}=\left[s_{1, d}, s_{2, d}\right]$ the position of the $d$-th sensor, and $Z_{d}$ the triangle of vertices $\mathbf{s}_{d}, \mathbf{l}_{1}=[2.5,0]$ and $\mathbf{l}_{2}=[7.5,0]$ (the corners of the light source). This triangle $Z_{d}$ is the "detection zone" of the $d$-th sensor. Now, we define the indicator variable

$$ z_{d, i, j}=1 \quad \text { if }\left(i-\frac{1}{2}, j-\frac{1}{2}\right) \in Z_{d}, \quad z_{d, i, j}=0 \quad \text { if }\left(i-\frac{1}{2}, j-\frac{1}{2}\right) \notin Z_{d} $$

![img-8.jpeg](img-8.jpeg)

Fig. 6: Results of Nemenyi test, based on Table 7 and Table 8, If methods' bars overlap, they can be considered statistically indifferent. The graphs based on time should be interpreted such that higher rank (more to the left) corresponds to slower (i.e., less desirable) times.
where $\left(i-\frac{1}{2}, j-\frac{1}{2}\right)$ is the middle point of the $(i, j)$-th pixel (tile), whose vertices are $(i, j),(i-1, j-1),(i-1, j)$ and $(i, j-1)$ (for $i, j=2, \ldots, W)$. Next, we define the variable

$$
c_{d}=\sum_{i=1}^{W} \sum_{j=1}^{W} y_{i, j} z_{d, i, j}
$$

which corresponds to the number of active tiles/pixels inside the triangle $Z_{d}$ associated to the $d$-th sensor. The likelihood function for the $d$-th sensor is then given by

$$
p\left(x_{d}=1 \mid \mathbf{y}\right)=p\left(x_{d}=1 \mid c_{d}\right)= \begin{cases}\epsilon_{2}, & c_{d}=0 \\ 1-\epsilon_{1}, & c_{d}=1 \\ 1-\epsilon_{1} \exp \left[-0.1\left(c_{d}-1\right)\right], & c_{d}>1\end{cases}
$$

and $p\left(x_{d}=0 \mid \mathbf{y}\right)=1-p\left(x_{d}=1 \mid \mathbf{y}\right)$; where $\epsilon_{1}=p\left(x_{d}=0 \mid c_{d}=1\right)=0.15<0.5$ is the false negative rate and $\epsilon_{2}=p\left(x_{d}=1 \mid c_{d}=0\right)=0.01<0.5$ is the false positive rate.

# 5.2.2. Generation of Artificial Data 

Figure 7 shows a low dimensional scenario $(L=100, W=10)$, for the purpose of a clear illustration, but we consider datasets with much higher levels of segmentation (namely Local400, where $L=400$, and Local10k, where $L=10,000$ - see Table 5)

![img-9.jpeg](img-9.jpeg)

Fig. 7: An $L=10 \times 10=100$ tile localization scenario. $D=12$ light sensors are arranged around the edges of the scenario at coordinates $\mathbf{s}_{1}, \ldots, \mathbf{s}_{D}$, and there is a light source between points $\mathbf{l}_{1}=[2.5,0]$ and $\mathbf{l}_{2}=[7.5,0]$ (shown as a thick black line) on the horizontal axis. In this example, three observations are positive $\left(x_{d}=1\right)$. Note that the object in the bottom-right tile ( $y_{L}=1$ in this case) cannot be detected.
to compare the performance of several MOC techniques on this problem. Given a scenario with $L=W \times W$ tiles, $D$ sensors and $N$ observations, we generate the synthetic data, $\left(\mathbf{x}^{(n)}, \mathbf{y}^{(n)}\right)_{n=1}^{N}$, as follows:

1. Start with an 'empty' $\mathbf{y}$, i.e., $y_{i, j}=0$ for $i, j=1, \ldots, W$.
2. Set $y_{i, j}=1$ for relevant tiles to create a rectangle of width $W / 8$ and height 2 starting from some random point $y_{i, j}$.
3. Create a $2 \times 2$ square in the corner furthest from the rectangle.
4. Generate the observations according to Eq. (11).
5. Add dynamic noise in $\mathbf{y}$ by flipping $L / 100$ pixels uniformly at random.

Any MLC method can be applied to this problem, to infer the binary vector $\mathbf{y}^{*}$, which encodes the presence of blockinglight elements in the room, given the vector $\mathbf{x}^{*}$ of measurements from the light sensors. Finally, we also consider that each sensor provides $M$ observations $\left\{x_{d, k}\right\}_{k=1}^{M} \subset\{0,1\}^{M}$ given the same $\mathbf{y}$.

# 5.2.3. Maximum A Posteriori (MAP) Estimator 

Given the likelihood function of Eq. (11), and considering a uniform prior over each variable $c_{d}$, the posterior w.r.t. the $d$-th triangle is

$$
p\left(c_{d} \mid x_{d}\right) \propto p\left(x_{d} \mid c_{d}\right)=p\left(x_{d} \mid \mathbf{y}\right)
$$

If we also assume independency in the received measurements, the posterior density $p\left(c_{1}, \ldots, c_{D} \mid \mathbf{x}\right)$ can be expressed as follows

$$
p\left(c_{1}, \ldots, c_{D} \mid \mathbf{x}\right)=\prod_{d=1}^{D} p\left(c_{d} \mid \mathbf{x}\right) \propto \prod_{d=1}^{D} p\left(x_{d} \mid c_{d}\right)=\prod_{d=1}^{D} p\left(x_{d} \mid \mathbf{y}\right)
$$

We are interested in studying $p\left(y_{i, j} \mid \mathbf{x}\right)$ for $1 \leq i, j \leq W$, but we can only compute the posterior distribution of the variables $\left\{c_{1}, \ldots c_{D}\right\}$, which depend on $y_{i, j}$ through Eq. (10). Making inference directly on $y_{i, j}$ using the posterior distribution $p\left(c_{1}, \ldots, c_{d} \mid \mathbf{x}\right)$ is not straightforward. Let us address the problem in two steps. First, the measurements received by each sensor, $x_{d}$, can be considered as Bernoulli trials: if $c_{d}=0$, then $x_{d}=1$ with probability $\theta_{d}=\epsilon_{2}$; if $c_{d} \geq 1$, then $x_{d}=1$ with

```
input : \(\left\{x_{d, k}\right\}_{k=1, d=1}^{M, D}\) (measurements), \(\left\{\mathbf{s}_{d}\right\}_{d=1}^{D}\) (sensor positions), \(\mathbf{l}_{1}\) and \(\mathbf{l}_{2}\) (light source location).
begin
    1. Initialize \(\hat{y}_{i, j}=0.5\) for \(i, j=1, \ldots, W\).
    2. for \(d=1, \ldots, D\); do
        (a) Calculate the detection triangle \(Z_{d}\).
        (b) If \(\hat{\theta}_{d}=\frac{1}{M} \sum_{k=1}^{M} x_{d, k} \leq 0.5\), then set \(\hat{c}_{d}=0\).
        (c) Otherwise, if \(\hat{\theta}_{d}=\frac{1}{M} \sum_{k=1}^{M} x_{d, k}>0.5\), then set \(\hat{c}_{d}=1\).
        (d) If \(\hat{c}_{d}=0\), then set \(\hat{y}_{i, j}=0\) for all \(i, j \in Z_{d}\).
        end
    3. For all \(d\) such that \(\hat{c}_{d}=1\) and for all \(i, j \in Z_{d}\), check if the decision is still \(\hat{y}_{i, j}=0.5\). Then, set \(\hat{y}_{i, j}=1\).
    4. The remaining tiles with \(\hat{y}_{i, j}=0.5\) correspond to "shadow" zones, where we leave \(\hat{y}_{i, j}=0.5\).
end
output: \(\hat{y}_{i, j}\) for \(i, j=1, \ldots, W\).
```

Table 9: Results using Algorithm 4 with $D=30$ sensors.


success probability $\theta_{d}=1-\epsilon_{1}$. Now, given $M$ measurements for each sensor $\left\{x_{d, k}\right\}_{k=1}^{M} \subset\{0,1\}^{M}$ and uniform prior density over $\theta_{d}$, the MAP estimator of $\theta_{d}$ is given by

$$
\hat{\theta}_{d}=\frac{1}{M} \sum_{k=1}^{M} x_{d, k}
$$

Then, if $\hat{\theta}_{d} \leq 0.5$ we decide $\hat{c}_{d}=0$. Otherwise, if $\hat{\theta}_{d}>0.5$, we estimate $\hat{c}_{d} \geq 1$. Considering a uniform prior over the pixels $y_{i, j}$, a simple procedure to estimate $\mathbf{y}$ from $\left\{\hat{c}_{1}, \ldots \hat{c}_{D}\right\}$ is the one described in Algorithm 4.

# 5.2.4. Classifier Trellis vs MAP Estimator 

Results for CT are already given in Table 7 (predictive performance) and Table 8 (running time). Results in Table 7 illustrate the robustness of the CT algorithm to address multi-output classification in several scenarios. Beyond the training set, no further knowledge about the underlying model is needed to achieve remarkable classification performance. To emphasize this property of CT, we now compare it to the MAP estimator presented above, which exploits a perfect knowledge of the sensor model.

Table 9 shows the results using Algorithm 4 with $D=30$ sensors and different values of $W$ (i.e., the grid precision). The corresponding results obtained by CT are provided in Table 10. A detailed discussion of these results is provided at the end of the next Section. However, let us remark that increasing the number of tiles (i.e., $W$ ) for a given number of sensors $D$ makes the problem harder, as a finer resolution is sought. This explains the decrease in performance seen in the tables as $W$ increases.

## 6. DISCUSSION

As in most of the multi-label literature, we found that independent classifiers consistently under-perform, thus justifying the development of more complex methods to model label dependence. However, in contrary to what much of the multi-label

Table 10: Results using CT ( $D=30$ sensors).


literature suggests, greater investments in modelling label dependence do not always correspond to greater returns. In fact, it appears that many methods from the literature have been over-engineered. Our small experiment in Table 2 suggests that none of the approaches we investigated were particularly dominant in their ability to uncover structure with respect to predictive performance. Indeed, our results indicate that none of the techniques is significantly better than another. Using ECC is a 'safe bet' in terms of high accuracy, since it models long term dependencies with a fully cascaded chain; also noted previously (e.g,. [20, 3]). In terms of EBCC (for which we elected to represent methods that uncover a structure), there was no clear advantage over the other methods, and surprisingly also no clear difference between searching for a structure based on marginal dependence versus conditional label dependence. This makes it more difficult to justify computationally complex expenditures for modelling dependence on the basis of improved accuracy; particularly so for large datasets, where the scalability is crucial.

We presented a classifier trellis (CT) as an alternative to methods that model a full chain (as MCC or ECC) or methods that unravel the label graphical model structure from scratch, such as BCC. Our approach is systematic, we consider a fixed structure in which we place the labels in an ordered procedure according to easily computable mutual information measures, see Algorithm 1. An ensemble version of CT performs particularly well on exact match but, surprisingly, it does not perform much stronger than CT as we expected in the beginning. It does not perform as strong overall as ECC (although there is no statistically significant difference), but is much more scalable, as indicated in Table 4.

The CT algorithm then emerges as a powerful MLC algorithm, able to excellent performance (specially in terms of average number of successfully classified labels) with near IC running times. Through the Nemenyi test, we have shown the statistical similitude between the classification outputs of (E) CT and MCC/ECC, proving that our approach based on the classifier trellis captures the necessary inter-label dependencies to achieve high performance classification. Moreover, we have not analyzed yet the impact that the trellis structure chosen has in the CT performance. In future work, we intend to experiment with trellis structures with different degrees of connectedness.

# 7. ACKNOWLEDGEMENTS 

This work was supported by the Aalto University AEF research programme; by the Spanish government's (projects projects 'COMONSENS', id. CSD2008-00010, 'ALCIT', id. TEC2012-38800-C03-01, 'DISSECT', id. TEC2012-38058-C03-01); by Comunidad de Madrid in Spain (project 'CASI-CAM-CM', id. S2013/ICE-2845); and by and by the ERC grant 239784 and AoF grant 251170 .

# A. GRAPHICAL MODEL STRUCTURE LEARNING: FS VS. LEAD 

In order to delve deeper into the issue of structure learning, we generated a synthetic dataset, where the underlying structure is known. The synthetic generative model is as follows. For the feature vector, we consider a $D$-dimensional independent Gaussian vector $\mathbf{x} \in \mathbb{R}^{D}$, where $x_{d} \sim \mathcal{N}(0,1)$ for $d=1, \ldots, D$. Let $\mathbf{w}_{\ell}(\ell=1, \ldots, L)$ be a binary $D$-dimensional vector containing exactly $T$ ones (and thus $D-T$ zeros), and let us assume that we have a directed acyclic graph between the labels in which each label has at most one parent. Both the vectors $\mathbf{w}_{\ell}$ and the dependency label graph are generated uniformly at random. Given the value of its parent label, $y_{\mathrm{pa}(\ell)} \in\{-1,1\}$, the following probabilistic model is used to generate the $\ell$-th label $y_{\ell}$ :

$$
y_{\ell}= \begin{cases}+1, & T^{-1 / 2} \mathbf{w}_{\ell}^{+} \mathbf{x}+\epsilon_{\ell} \geq \delta \\ -1, & \text { otherwise }\end{cases}
$$

where $\delta$ is a real constant and $\epsilon_{\ell} \sim \mathcal{N}\left(\alpha y_{\mathrm{pa}(\ell)}, \sigma^{2}\right)$, with $\alpha \in \mathbb{R}$ and $\sigma \in \mathbb{R}^{+}$. Note that, according to the model, $y_{\ell} \mid y_{\mathrm{pa}(\ell)}$ is a Bernoulli random variable that takes value 1 with average probability

$$
P\left(y_{\ell}=+1 \mid y_{\mathrm{pa}(\ell)}=+1\right)=Q\left(\frac{\delta-\alpha y_{\mathrm{pa}(\ell)}}{\sqrt{1+\sigma^{2}}}\right)
$$

where $Q(x)=1-\Phi(x)$ and $\Phi(x)$ is the cumulative distribution function of the normal Gaussian distribution. Consequently, with $\alpha$ and $\sigma^{2}$ we control the likelihood of $y_{\ell}$ being equal to its parent $y_{\mathrm{pa}(\ell)}$, thus modulating the complexity of inferring such dependencies by using the FS and LEAD methods.

In Figure 8 we show three examples of synthetically generated datasets, in terms of their ground truth structure and the structure discovered using the FS and LEAD methods, for three different scenarios: 'easy' ( $\alpha=1, \sigma^{2}=1$ ), 'medium' ( $\alpha=0.5$, $\sigma^{2}=2$ ), and 'hard' ( $\alpha=0.25, \sigma^{2}=5$ ) datasets. Recall that we use a mutual information matrix for both methods, with the difference being that the LEAD matrix is based on the error frequencies rather than the label frequencies. Visually it appears that both FS and LEAD are able to discover the original structure, relative to the difficulty of the dataset. There appears to be a small improvement of FS over LEAD. This is confirmed in a batch analysis using the F-measure of 10 random datasets of random difficulty ranging between 'easy' and 'hard': FS gets 0.278 and LEAD gets 0.263 . A more in depth comparison, taking into account varying numbers of labels and features, is left for future work.

## B. APPROXIMATE INFERENCE VIA MONTE CARLO

A better understanding of the MLC/MOC approaches described in Section 3 and the novel scheme introduced in this work can be achieved by describing the Monte Carlo (MC) procedures used to perform approximate inference over the graphical models constructed to approximate $p(\mathbf{y} \mid \mathbf{x})$.

Given a probabilistic model for the conditional distribution $p(\mathbf{y} \mid \mathbf{x})$ and a new test input $\mathbf{x}^{*}$, the goal of an MC scheme is generating samples from $p\left(\mathbf{y} \mid \mathbf{x}^{*}\right)$ that can be used to estimate its mode (which is the MAP estimator of $\mathbf{y}$ given $\mathbf{x}^{*}$ ), the marginal distribution per label (i.e., $p\left(y_{\ell} \mid \mathbf{x}^{*}\right)$ for $\ell=1 \ldots, L$ ) or any other relevant statistical function of the data.

## B.1. Bayesian networks

In a directed acyclic graphical model, the probabilistic dependencies between variables are ordered. For instance, in the CC scheme $p(\mathbf{y} \mid \mathbf{x})$ factorizes according to Eq. (3). If it is possible to draw samples directly from each conditional density $p\left(y_{\ell} \mid y_{1: \ell-1}, \mathbf{x}\right)$, then exact sampling can be performed in a simple manner. For $i=1, \ldots, N_{s}$ (where $N_{s}$ is the desired number of samples), repeat

$$
\begin{aligned}
y_{1}^{(i)} & \sim p\left(y_{1} \mid \mathbf{x}\right) \\
y_{2}^{(i)} & \sim p\left(y_{2} \mid y_{1}^{(i)}, \mathbf{x}\right) \\
& \vdots \\
y_{L}^{(i)} & \sim p\left(y_{L} \mid y_{1: L-1}^{(i)}, \mathbf{x}\right)
\end{aligned}
$$

For Bayesian networks that are not fully-connected, as in BCC, the procedure is similar. Each sampled vector, $\mathbf{y}^{(i)}=$ $\left[y_{1}^{(i)}, y_{2}^{(i)}, \ldots, y_{L}^{(i)}\right]$ for $i=1, \ldots, N_{s}$, is obtained by drawing each individual component independently as $y_{\ell}^{(i)} \sim p\left(y_{\ell} \mid \mathbf{y}_{\mathrm{pa}(\ell)}^{(i)}\right)$ for $\ell=1, \ldots, L$.

![img-10.jpeg](img-10.jpeg)

Fig. 8: Ground-truth graphs of the synthetic dataset (left) - easy, medium, and hard according to the table - and their reconstruction found by the FS strategy [8] (middle) and LEAD strategy [26] (right).

# B.2. Markov networks 

In an undirected graphical model (like that of a CDN), exact sampling is generally unfeasible. However, a Markov Chain Monte Carlo (MCMC) technique that is able to generate samples from the target density $p(\mathbf{y} \mid \mathbf{x})$ can be implemented. Within this class, Gibbs Sampling is often the most adequate approach. Let us assume that the conditional distribution $p(\mathbf{y} \mid \mathbf{x})$ factorizes according to an undirected graphical model as in Eq. (7). Then, from an initial configuration $\mathbf{y}^{(0)}=\left[y_{1}^{(0)}, \ldots, y_{L}^{(0)}\right]$, repeat for $t=1, \ldots, T$ :

$$
\begin{aligned}
y_{1}^{(t)} & \sim p\left(y_{1} \mid y_{1}^{(t-1)}, y_{2}^{(t-1)}, \ldots, y_{L}^{(t-1)}, \mathbf{x}\right) \\
y_{2}^{(t)} & \sim p\left(y_{2} \mid y_{1}^{(t)}, y_{2}^{(t-1)}, \ldots, y_{L}^{(t-1)}, \mathbf{x}\right) \\
& \vdots \\
y_{L}^{(t)} & \sim p\left(y_{L} \mid y_{1}^{(t)}, y_{2}^{(t)}, \ldots, y_{L}^{(t-1)}, \mathbf{x}\right)
\end{aligned}
$$

where each label can be sampled by conditioning just on the neighbors in the graph, as seen from Eq. (9). Thus,

$$
y_{\ell}^{(t)} \sim p\left(y_{\ell} \mid\left\{y_{u}^{(t)}: y_{u} \in \mathbf{y}_{\mathrm{ne}(\ell)}, u<\ell\right\},\left\{y_{m}^{(t-1)}: y_{m} \in \mathbf{y}_{\mathrm{ne}(\ell)}, m>\ell\right\}, \mathbf{x}\right)
$$

which can be simply denoted as $y_{\ell}^{(t)} \sim p\left(y_{\ell} \mid \mathbf{y}_{\mathrm{ne}(\ell)}^{(t)}\right)$, with $\mathbf{y}_{\mathrm{ne}(\ell)}^{(t)}$ denoting the state of the neighbors of $y_{\ell}$ at time $t$.
Following this approach, the state of the chain $\mathbf{y}^{(t)}=\left[y_{1}^{(t)}, \ldots, y_{L}^{(t)}\right]$ can be considered a sample from $p(\mathbf{y} \mid \mathbf{x})$ after a certain "burn-in" period, i.e., for $t>T_{c}$. Thus, samples for $t<T_{c}$ are discarded, whereas samples for $t>T_{c}$ are used to perform the desired inference task. Two problems associated to MCMC schemes are the difficulty in determining exactly when the chain has converged and the correlation among the generated samples (unlike the schemes in Section B.1, which produce i.i.d. samples).