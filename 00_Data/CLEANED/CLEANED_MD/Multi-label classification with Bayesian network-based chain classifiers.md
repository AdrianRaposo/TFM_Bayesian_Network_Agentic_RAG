# Multi-label classification with Bayesian network-based chain classifiers 

L. Enrique Sucar, Concha Bielza, Eduardo F. Morales, Pablo Hernandez-Leal, Julio H. Zaragoza, Pedro Larrañaga

In multi-label classification the goal is to assign an instance to a set of different classes. This task is normally addressed either by defining a compound class variable with all the possible combinations of labels (label power-set methods) or by building independent classifiers for each class (binary relevance methods). The first approach suffers from high computationally complexity, while the second approach ignores possible dependencies among classes. Chain classifiers have been recently proposed to address these problems, where each classifier in the chain learns and predicts the label of one class given the attributes and all the predictions of the previous classifiers in the chain. In this paper we introduce a method for chaining Bayesian classifiers that combines the strengths of classifier chains and Bayesian networks for multi-label classification. A Bayesian network is induced from data to: (i) represent the probabilistic dependency relationships between classes, (ii) constrain the number of class variables used in the chain classifier by considering conditional independence conditions, and (iii) reduce the number of possible chain orders. The effects in the Bayesian chain classifier performance of considering different chain orders, training strategies, number of class variables added in the base classifiers, and different base classifiers, are experimentally assessed. In particular, it is shown that a random chain order considering the constraints imposed by a Bayesian network with a simple tree-based structure can have very competitive results in terms of predictive performance and time complexity against related state-of-the-art approaches.

## 1. Introduction

In contrast with traditional (one-dimensional) classifiers, multilabel classifiers assign each instance to a set of $d$ classes. Multilabel classification has received increasing attention in recent years as several important problems need to predict a set of multiple labels (Zhang et al., 2013; Vens et al., 2008; Zhang and Zhou, 2007), such as text classification (assigning a document to several topics), HIV drug selection (determining the optimal set of drugs), and scene classification, among others.

Two main types of approaches have been proposed for multilabel classification: binary relevance and label power-set. In the binary relevance approach (Zhang and Zhou, 2007), the multi-label
classification problem is transformed into $d$ binary classification problems, one for each class variable, $C_{1}, \ldots, C_{d}$. A classifier is independently learned for each class and the results are combined to determine the predicted class vector. The main advantages of this approach are its low computational complexity and that existing classification techniques can be directly applied. However, it is unable to capture the interactions between classes and, in general, the most likely class of each classifier will not match the most likely set of classes due to possible interactions among them.

In the label power-set approach (Tsoumakas and Katakis, 2007), the multi-label classification problem is transformed into a singleclass scenario by defining a new compound class variable whose possible values are all the possible combinations of values of the original classes. In this case, the interactions between classes are implicitly considered and can be an effective approach for domains with a few class variables. Its main drawback, however, is its computational complexity, as the size of the compound class variable increases exponentially with the number of classes.

To overcome the limitations of previous methods, two main strategies have been proposed within the field of probabilistic

graphical models: (i) to incorporate class interactions in binary relevance methods, in what are known as chain classifiers (Dembczynski et al., 2010; Read et al., 2009), and (ii) to explicitly represent the dependence structure between the classes, avoiding the combinatorial explosion of the label power-set approach, via multi-dimensional Bayesian network classifiers (Bielza et al., 2011; van der Gaag and de Waal, 2006; Zaragoza et al., 2011a).

Chain classifiers (Dembczynski et al., 2010, 2012; Read et al., 2009, 2011) consist of $d$ base classifiers which are linked in a chain, such that each classifier incorporates the classes predicted by the previous classifiers as additional attributes. In this way the class interactions are incorporated while maintaining an efficiency close to the binary relevance method. The order of the classes considered in the chain can affect the final results and usually an ensemble of random orders is used, which is computationally expensive. Another potential drawback of this technique is that the number of attributes increases with the number of classes, and it can become problematic for certain domains.

A multi-dimensional Bayesian network classifier (Bielza et al., 2011; de Waal and van der Gaag, 2007; van der Gaag and de Waal, 2006; Zaragoza et al., 2011a) is a Bayesian network (BN) of restricted topology designed to solve multi-dimensional (and also multi-label) classification problems. It consists of three subgraphs, one for the class variables, one for the feature variables, and a bridge structure that interconnects the class and feature subgraphs allowing only arcs from classes to features. Although several alternatives have been proposed to learn these substructures (Bielza et al., 2011; Rodríguez and Lozano, 2008), it suffers from the high computational cost of determining the optimal network structure, and computing the most probable explanation for any instance with unknown values for the classes.

Bayesian Chain Classifiers (BCC) (Zaragoza et al., 2011b) combine the previous strategies, taking advantage of their strengths and at the same time avoiding their main limitations. The method for learning these classifiers consists of two main phases: (i) obtain a dependency structure for the class variables, and (ii) based on the dependency structure, build a chain classifier. In the first phase, a BN that represents the probabilistic dependency relations between the class variables is learned from data. This class structure serves as a guide for the second phase, as it constrains the possible variable orderings in the chain and reduces the number of classes considered in the chain classifier, by considering the independence conditions of the Bayesian network. Finally, as for chain classifiers, the predicted class vector is obtained by concatenating the outputs of all the classifiers in the chain.

In Zaragoza et al. (2011b) it was shown that a simple BCC with a tree structure in the first phase, and a random class order consistent with the tree, using naïve Bayes as base classifier in the chain, was able to outperform several state-of-the-art multi-dimensional Bayesian network classifiers on several testbed problems with a lower time complexity. This paper extends the approach in Zaragoza et al. (2011b) presenting a deeper analysis to get insights into the BCC behavior. We perform an extensive empirical evaluation on alternative strategies for building BCCs varying several aspects:

1. Different training schemes.
2. Several heuristics to define the order of the chain.
3. Different number of classes incorporated in each classifier in the chain.
4. Alternative base classifiers.
5. Single chain vs. ensembles.

We also compare experimentally BCCs with binary relevance and standard chain classifiers (Read et al., 2009; Read et al., 2011). All the experiments are carried out over 9 benchmark multi-label data sets using four different performance metrics.

The main contribution of this paper is the proposal and analysis of several extensions to the basic BCC classifier introduced in Zaragoza et al. (2011b). This work opens a new research avenue for multi-label classification research as considering dependencies among classes is clearly beneficial.

The paper is organized as follows. Section 2 describes the multilabel classification problem. Section 3 reviews related work. Bayesian chain classifiers are introduced in Section 4. In Section 5, we analyze alternative configurations for Bayesian chain classifiers. Section 6 describes the experiments and discusses the results. Section 7 summarizes the main ideas of the paper and provides future research directions.

## 2. Multi-label classifiers

The multi-dimensional classification problem corresponds to searching for a function $h$ that assigns to each instance represented by a vector of $m$ features, $\mathbf{x}=\left(x_{1}, \ldots, x_{m}\right)$, a vector of $d$ class values $\mathbf{c}=\left(c_{1}, \ldots, c_{d}\right)$ of the $d$ dimensional class variable $\left(C_{1}, \ldots, C_{d}\right)$ :
$h: \Omega_{X_{1}} \times \cdots \times \Omega_{X_{m}} \rightarrow \Omega_{C_{1}} \times \cdots \times \Omega_{C_{d}}$
$\left(x_{1}, \ldots, x_{m}\right) \mapsto\left(c_{1}, \ldots, c_{d}\right)$
We assume that $C_{i}$ and $X_{j}$ for all $i=1, \ldots, d$ and all $j=1, \ldots, m$ are discrete, and that $\Omega_{C_{i}}$ and $\Omega_{X_{j}}$ respectively, represent their sample spaces.

Under a 0-1 loss function, the $h$ function should assign to each instance $\mathbf{x}$ the most likely combination of classes, that is:
$\arg \max _{c_{1}, \ldots, c_{d}} P\left(C_{1}=c_{1}, \ldots, C_{d}=c_{d} \mid \mathbf{x}\right)$
This assignment amounts to solving a total abduction inference problem and corresponds to the search for the most probable explanation (MPE), a problem that has been proved to be an NPhard problem for Bayesian networks (Shimony, 1994).

In this work, we consider the multi-label classification problem, which can be seen as a particular case of a multi-dimensional classification, where all class variables are binary, that is $\left|\Omega_{C_{i}}\right|=2$ for $i=1, \ldots, d$.

## 3. Related work

In this section we briefly review the main approaches that have been proposed for multi-label classification. The review is organized into three subsections, discussing research in multi-label classification, multi-dimensional Bayesian network classifiers, and chain classifiers, respectively.

### 3.1. Multi-label classification

As mentioned before, there are two basic approaches for multi-label classification: binary relevance and label power-set (Tsoumakas and Katakis, 2007). Binary relevance approaches transform the mul-ti-label classification problem into $d$ independent binary classification problems, one for each class variable, $C_{1}, \ldots, C_{d}$. A classifier is independently learned for each class and the results are concatenated to determine the predicted class vector; the dependencies between classes are not considered. The label power-set approach transforms the multi-label classification problem into a single-class scenario by defining a new compound class variable whose possible values are all the possible combinations of values of the original classes. In this case the interactions between classes are implicitly considered and can be an effective approach for domains with a few class variables; however for many classes this approach is impractical.

An overview of multi-label classification is presented in Tsoumakas and Katakis (2007), where two main methods are

distinguished: (a) problem-transformation methods, and (b) algorithm-adaptation methods. Methods in (a) transform the multilabel classification problem into either one or more single-label classification problems. Methods in (b) extend specific learning algorithms to handle multi-label data directly.

### 3.2. Multi-dimensional Bayesian network classifiers

A multi-dimensional Bayesian network classifier (MBC) over a set $$V = \{Z_1, \ldots, Z_n\}, n \geq 1$$, of discrete random variables is a Bayesian network $$B = (G, \Theta)$$, where $$G$$ is an acyclic directed graph with vertexes $$Z_i$$, and $$\Theta$$ is a set of parameters $$\theta_{Z(\mathbf{pa};Z_i)} = P(Z|\mathbf{pa}|Z))$$, where $$\mathbf{pa}(Z)$$ is a value for the set $$\mathbf{Pa}(Z)$$ of parents variables of $$Z$$ in $$G$$. $$B$$ defines a joint probability distribution $$P_B$$ over $$V$$ given by:

$$P_B(Z_1, \ldots, Z_n) = \prod_{i=1}^{n} P_B(Z_i|\mathbf{pa}(Z_i)) \tag{2}$$

The set $$V$$ of vertexes is partitioned into two sets $$V_C = \{C_1, \ldots, C_d\}, d \geq 1$$, of class variables and $$V_X = \{X_1, \ldots, X_m\}, m \geq 1$$, of feature variables $$(d + m = n)$$. The set $$A$$ of arcs is also partitioned into three sets, $$A_C$$, $$A_X$$, $$A_{CX}$$, such that $$A_C \subseteq V_C \times V_C$$ is composed of the arcs between the class variables, $$A_X \subseteq V_X \times V_X$$ is composed of the arcs between the feature variables and finally, $$A_{CX} \subseteq V_C \times V_X$$ is composed of the arcs from the class variables to the feature variables. The corresponding induced subgraphs are $$G_C = (V_C, A_C), G_X = (V_X, A_X)$$ and $$G_{CX} = (V, A_{CX})$$, called respectively class, feature and bridge subgraphs (see Fig. 1).

Different graphical structures for the class and feature subgraphs may lead to different families of MBCs. van der Gaag and de Waal (2006) learn trees for both subgraphs. In de Waal and van der Gaag (2007) they analyze the conditions for the optimal recovery of poly-tree structures in both subgraphs.

Rodríguez and Lozano (2008) extend poly-trees to k-DB structures for class and features subgraphs.

Bielza et al. (2011) describe a general model in which any Bayesian network structure is allowed in the three subgraphs. Learning from data algorithms cover many possibilities: wrapper, filter and hybrid scores with different search strategies. Direct algorithms for learning these simpler MBCs, both from a wrapper point of view (Borchani et al., 2010) and from a filter Markov blanket-based perspective (Borchani et al., 2012) have been recently proposed. In Zaragoza et al. (2011a), the authors introduce a two-step method for learning multi-dimensional Bayesian network classifiers based on mutual information or dependency between the classes and the features variables.

### 3.3. Chain classifiers

Read et al. (2009) introduce chain classifiers as an alternative method for multi-label classification that incorporates class dependencies, while keeping the computational efficiency of the binary relevance approach. A chain classifier consists of d base binary

![img-0.jpeg](img-0.jpeg)

**Fig. 1.** A multi-dimensional Bayesian network classifier structure, showing the three subgraphs: classes, features and bridge.

classifiers which are linked in a chain, such that each classifier incorporates the classes predicted by the previous classifiers as additional attributes. Thus, the feature vector for each binary classifier is extended with the class values (labels) of all previous classifiers in the chain. Each classifier in the chain is trained to learn the association of label $$C_i$$ given the features augmented with all previous class labels in the chain, $$c_i, c_1, \ldots, c_{i-1}$$. At classification time, the process starts at $$C_1$$, and propagates the predicted classes along the chain such that for $$c_i$$ it computes $$\arg \max_{c_i} P(c_i|\mathbf{x}, c_1, c_2, \ldots, c_{i-1})$$. As in the binary relevance approach, the class vector is determined by concatenating the outputs of all the binary classifiers in the chain.

In Read et al. (2009), the authors use several chain classifiers by changing the order for the labels, building an ensemble of chain classifiers. Thus, m chain classifiers are trained, by varying the training data and the order of the classes in the chain (both are set randomly). The final label vector is obtained using a voting scheme: each label $$c_i$$ receives a number of votes from the m chain classifiers, and a threshold on this number is used to determine the final predicted multi-label set. They used support vector machines as base binary classifier, and evaluate experimentally their method with 12 multi-label data sets, comparing it with binary relevance and other ensemble algorithms. The classifier chains outperformed binary relevance in terms of accuracy for most data sets, with some increase in training time. However the results were not always the best in terms of accuracy of their ensemble against other ensemble methods, with some advantage in training and classifications times, as expected.

Recently, Read et al. (2011) have presented several extensions of their previous work. In particular, they propose some improvements to make the ensemble learning process more efficient, such as taking random subsets of attributes and instances. The experimental results show a significant reduction on running time with almost the same accuracy. They also present additional experiments and compare chain classifiers and ensembles of chain classifiers with alternative techniques.

Dembczynski et al. (2010) introduce probabilistic chain classifiers (PCCs), by basically putting chain classifiers under a probabilistic framework. Using the chain rule of probability theory, the probability of the vector of d class values $$\mathbf{c} = (c_1, \ldots, c_d)$$ given the feature vector $$\mathbf{x}$$ can be written as:

$$P(\mathbf{c}|\mathbf{x}) = P(c_1|\mathbf{x}) \prod_{i=2}^{d} P(c_i|c_1, \ldots, c_{i-1}, \mathbf{x}) \tag{3}$$

A PCC estimates the joint probability of the classes, providing better estimates than the chain classifiers, but with a much higher computational complexity. In fact, the experiments reported by Dembczynski et al. (2010) are limited to 10 class variables.

They analyze different scoring functions, and argue that for certain loss functions considering class dependencies can be important, and not for others, as confirmed by their experiments with artificial data. For independent classes, the results in terms of certain loss functions are almost the same for binary relevance, chain and probabilistic chain classifiers; while for dependent classes, binary relevance has competitive performance for certain loss functions, and it is clearly outperformed for certain loss functions by the other methods (that consider label dependencies). Their experiments with artificial and benchmark data sets show that PCC and its corresponding ensemble, EPCC, have a better performance than the chain classifier and the ensemble of chain classifiers, for some loss scoring functions.

In Zhang and Zhang (2010), $$P(\mathbf{c}|\mathbf{x})$$ is decomposed according to a Bayesian network: $$P(\mathbf{c}|\mathbf{x}) = \prod_{i=1}^{d} P(c_i|\mathbf{pa}(c_i), \mathbf{x})$$. Finding $$\mathbf{pa}(c_i)$$ is complex under the setting of (many) continuous features, whose effect on the labels may be nonlinear. Thus, this is simplified as follows. First, d classifiers are built for all labels independently,

from a nonlinear regression model of **x** over **c<sup>i</sup>**, whose output is thresholded to yield the predicted labels. Second, from the corresponding errors for each label, a Bayesian network structure is learnt. The links found here are incorporated as **pa**(**c<sup>i</sup>**) in the sought Bayesian network. Finally, a PCC is implemented according to an order implied by the network.

As shown in Dembczynski et al. (2010), a method that considers class dependencies under a probabilistic framework can have a significant impact on the performance of multi-label classifiers. However, both MBCs and PCCs have a high computational complexity, which limits their applicability to high dimensional problems. In the following section we describe an alternative probabilistic method which also incorporates class dependencies while being very efficient at the same time. Unlike Zhang and Zhang (2010), we directly work on the original class variables (and not over the regression errors), where we find a simple tree structure. The feature variables are assumed to be discrete. We allow to have ensembles of classifiers.

## **4. Bayesian chain classifiers**

In this section we consider the multi-dimensional classification problem under a Bayesian network framework; and in particular we analyze the assumptions implied by a Bayesian chain classifier approximation.

If we apply the chain rule of probability theory, we can rewrite Eq. (1) as:

$$
\arg\max\_{c\_i} P(c\_1|c\_2, \dots, c\_d, \mathbf{x})P(c\_2|c\_3, \dots, c\_d, \mathbf{x}) \dots P(c\_d|\mathbf{x})
$$

If we assume we can represent the joint probability distribution of the class variables given the features as a Bayesian network, then we can simplify Eq. (1) by considering the independencies implied by the Bayesian network; so that only the *parents* of each class variable are included in the chain, and all other *previous* classes according to the chain order are eliminated. So we can write Eq. (4) as:

$$
\arg\max\_{c\_1, \dots, c\_d} \prod\_{i=1}^{d} P(c\_i|\mathbf{pa}(C\_i), \mathbf{x})
$$

where **Pa**(**C<sup>i</sup>**) are the parents of class **i** in the Bayesian network.

Next we make a further simplification by assuming that the most probable joint combination of classes can be approximated by just concatenating the individual most probable classes from the base classifier. That is, we solve the following set of equations as an approximation of Eq. (1):

$$
\arg\max\_{c\_1} P(c\_1|\mathbf{pa}(C\_1), \mathbf{x})
$$

$$
\arg\max\_{c\_2} P(c\_2|\mathbf{pa}(C\_2), \mathbf{x})
$$

$$
\arg\max\_{c\_d} P(c\_d|\mathbf{pa}(C\_d), \mathbf{x})
$$

This last approximation corresponds to a Bayesian chain classifier. Thus, a BCC makes two basic assumptions:

1. The class dependency structure given the features can be represented by a Bayesian network.
2. The most probable joint combination of class assignment (total abduction) is approximated by the concatenation of the most probable individual classes.

The first assumption is reasonable if we have enough data to obtain a good approximation of the class dependency structure, and assuming that this is obtained conditioned on the features. With respect to the second assumption, it is well known that the total abduction or most probable explanation is not always equivalent to the maximization of the individual classes. However, this assumption, also considered by chain classifiers and PCCs, is less strong than that assumed by the binary relevance approach.

In this setting, a chain classifier can be constructed by inducing first the class that does not depend on any other class and then proceed with its children. We can:

- Create an (partial) order of classes in the chain based on the dependencies between classes given the features. Assuming that these dependencies can be represented as a BN, the chain structure complies with the structure of the BN, such that we can then start building base classifiers for the classes without parents, and continue with their children classes, and so on. We can further simplify the problem by considering the marginal dependencies between classes as a first approximation (without conditioning on the features) to obtain an order for the chain classifier, and then induce base classifiers considering such an order.
- Consider conditional independencies between classes to create simpler base classifiers. In this case, construct *d* classifiers considering only the parent classes of each class. For a large number of classes this can be a huge reduction as normally we can expect to have a limited number of parents per class.

The general idea for building a BCC is illustrated in Fig. 2.

We first introduce the simplest option to build a BCC, and then present several possible extensions.

### *4.1. Tree naïve Bayesian chain classifier*

The simplest Bayesian chain classifier considers only one parent per class in a chain. This can be solved by obtaining the skeleton of a tree-structured BN for the classes using Chow and Liu's algorithm (1968), that is, a *maximum weight spanning tree* (*MWST*). This algorithm builds the structure that maximizes the likelihood of the data over all possible trees. The weights are computed as the mutual information between pairs of variables.

Chow and Liu's algorithm does not give us the directions of the links, however, we can build a directed tree by taking any class (node) as root of a tree and assigning directions to the arcs starting from this root node to build a directed tree. The chaining order of the base classifiers is given by traversing the tree following an ancestral ordering.

For *d* classes we can build *d* trees. Then we can choose an ancestral ordering from each tree and build a chain classifier. Finally, we

![img-1.jpeg](img-1.jpeg)

**Fig. 2.** An example of a BCC: (a) a BN that represents the class dependency structure; (b) set of naïve Bayes classifiers, one for each class. Each base classifier defined for **C<sup>i</sup>** includes the set of attributes, **X<sub>1</sub>**, ..., **X<sub>n</sub>**, plus its parents in the BN as additional attributes.

can combine the chain classifiers in an ensemble (if $d$ is very large we can limit the number of chains by selecting a random subset of trees).

Once the dependencies between classes have been taken into account to generate a chain classifier, we only need to define the base classifier. Our baseline approach is to use a naïve Bayes classifier, see Fig. 3. We call this approach a tree naïve Bayesian chain classifier (TNBCC). Each naïve Bayes classifier for $C_{i}$ has as attributes all the features and also $\mathbf{P a}\left(C_{i}\right)$ according to the BN structure. Therefore for each base classifier we solve $\arg \max _{c_{i}} P\left(c_{i} \mid \mathbf{p a}\left(C_{i}\right), \mathbf{x}\right)$, which shapes the chain classifier (as in Eq. (5)).

We can summarize the algorithm to build the TNBCC as follows. Given a multi-label classification problem with $d$ classes:

1. Build an undirected tree to approximate the dependency structure among class variables.
2. Create an order for the chain classifier by randomly selecting one class as the root of the tree and assigning the rest of the links in order.
3. For each class variable (node) in the chain, build a naïve Bayes classifier for class $C_{i}$ which has as attributes its parent $\mathbf{P a}\left(C_{i}\right)$ and all the features $\mathbf{x}$, taking advantage of the conditional independence properties.
4. To classify a new instance concatenate the outputs of the chain.

This is a very fast and easy way to build chain classifiers, which represents the simplest alternative for a BCC. Other, more complex alternatives, are explored in the following section.

## 5. Alternative Bayesian chain classifiers

The basic, tree naïve Bayesian chain classifier can be extended in different ways. We consider five dimensions:

1. The training scheme.
2. The order in which the classes are considered in the chain.
3. The number of classes in each base classifier (chain complexity).
4. The base classifier.
5. Whether to use one chain or an ensemble of chains.

In the following sections we analyze each one in detail.

### 5.1. Training scheme

There are at least two options for training chain classifiers:

- The first approach considers the predicted output of the previous classifiers as training input for the next classifier in the chain. The rationale is to build a new classifier considering what will be the "actual" output of the first classifiers during the
![img-2.jpeg](img-2.jpeg)

Fig. 3. An example of a Tree Naïve Bayesian Chain Classifier where each node ( $C_{0}$, for instance) in the chain yields a naïve Bayesian classifier which has as attributes its parent class $\left(C_{1}\right)$ and all the features $\left(X_{1}, \ldots, X_{n}\right)$.
testing phase. The disadvantage of this approach is that a poor classifier will tend to produce erratic predictions and consequently affect the subsequent classifiers.

- The second approach constructs classifiers in the chain considering the actual class values given in the original training set. The rationale is that using the "real" value (as opposed to the predicted value by the previous classifiers) will tend to produce more accurate classifiers.

Section 6.4 describes the performance results for both approaches.

### 5.2. Order of classes in the chain

For a tree naïve BCC, where we have a tree-based structure for the classes, there are different ways of deciding which node to be selected as the root of the tree, from which the chain order can be directly obtained. Here we propose several alternatives:

- Random choice. A class node is randomly selected as the root of the tree. For example, in Fig. 3, $C_{3}$ is selected to produce the tree to the left.
- Select the node with the largest number of incident edges. In Fig. 3 it could be $C_{3}$ or $C_{6}$, both of which have three associated links.
- Construct a base classifier for each class independently and select the class with the best classification accuracy as the root of the tree.
- Construct a base classifier for each class independently, sort the classes according to their classification accuracy and use that order for the chain regardless of the Bayesian network.

In Section 6.4 we describe the results of tests with different options for the chain order.

### 5.3. Complexity of the chain

The main idea of constructing a (class) Bayesian network representing the dependencies among classes is to restrict the number of classes to consider in the base classifiers to only those related to each class and to help to choose a suitable chain order. The number of classes considered for each classifier depends on the structure of the class Bayesian network.

- The simplest approach is to consider a single parent in a treebased structure (restricting the class Bayesian network structure to a tree), which is the approach taken by the tree naïve BCC.
- By still working with a tree structure, an alternative approach is to consider all the class ancestors in the tree as input for the next classifier, providing additional information from indirectly related classes.
- Other approach is to decide on a traversing order of the class Bayesian network or choosing a random order of classes as suggested in Read et al. (2009), and using all the previous classes in the classifier chain.
- Alternatively more complex class structures could be built, such as polytrees or multi-connected networks. In both cases, each base classifier could have several parents which would be incorporated as additional attributes in the base classifiers. An example is shown in Fig. 2.

For multi-label classification problems where there can be a large number of classes, it is important to see if considering a small subset of related classes can produce competitive results against a more expensive strategy that uses all the previous classes in the chain. We test these alternatives in Section 6.3.3.

### 5.4. Base classifier

There are many different choices for constructing each classifier of the chain. So far, the same classifier has been used for all the classifiers of the chain, but nothing prevents us from using different classifiers along the chain. Among the possible choices, TNBCC uses a naïve Bayes classifier, which has the advantage of being simple and easy to implement. In this paper we also use support vector machines to assess the effect on the predictive performance of a generally stronger, although computationally more expensive, classifier. A comparison of these base classifiers is described in Section 6.3.4.

### 5.5. One chain vs. an ensemble of chains

Lastly, there is the choice of whether to use a single chain or an ensemble of chain classifiers. Ensembles have proved to be an effective mechanism to improve the performance metrics of simple classifiers at the expense of using more computational resources. Due to the nature of several multi-label problems (large number of data, attributes and classes), it is relevant to determine whether finding a good chain order could produce equivalent performance results to an ensemble of random chain orders, with significant savings in computational resources. This is analyzed in Section 6.4.

## 6. Empirical evaluation

In this section we empirically evaluate different choices for building BCCs and compare them against other state-of-the-art multi-label classifiers.

### 6.1. Data sets

Different Bayesian chain classifiers were tested on 9 benchmark multi-label data sets ${ }^{1}$; each of them with different dimensions ranging from 6 to 983 labels, and from about 600 examples to more than 43,000 . All class variables of the data sets are binary, however, in some of the data sets the feature variables are numeric. In these cases we used a static, global, supervised and top-down discretization algorithm (Cheng-Jung et al., 2008). The details of the data sets are summarized in Table 1.

### 6.2. Evaluation metrics

Several metrics have been recently proposed to evaluate the performance of multi-label classifiers. They basically range from considering the performance of the multi-label classifier over each class independently of the rest, to considering the performance of all the classes at the same time. For the purpose of comparison we used four different multi-label evaluation measures (Bielza et al., 2011; Read et al., 2009):

1. Mean accuracy over the $d$ class variables (accuracy per label):

$$ M-\operatorname{Acc}=\frac{1}{d} \sum_{j=1}^{d} A c c_{j}=\frac{1}{d} \sum_{j=1}^{d} \frac{1}{N} \sum_{i=1}^{N} \delta\left(c_{i j}^{\prime}, c_{i j}\right) $$

where $\delta\left(c_{i j}^{\prime}, c_{i j}\right)=1$ if $c_{i j}^{\prime}=c_{i j}$ and 0 otherwise, and $c_{i j}^{\prime}$ denotes the $C_{j}$ class value outputted by the model for instance $i$ and $c_{i j}$ is its true value. 2. Global accuracy over the $d$-dimensional class variable (accuracy per example, also called subset zero-one loss):

[^0]Table 1 Multi-label data sets used in the experiments and associated statistics. $N$ is the size of the data set, $d$ is the number of binary classes or labels, $m$ is the number of features. + indicates that there are numeric attributes.


$$ G-\operatorname{Acc}=\frac{1}{N} \sum_{i=1}^{N} \delta\left(\mathbf{c}_{i}^{\prime}, \mathbf{c}_{i}\right) $$

where $\delta\left(\mathbf{c}_{i}^{\prime}, \mathbf{c}_{i}\right)=1$ if $\mathbf{c}_{i}^{\prime}=\mathbf{c}_{i}$ and 0 otherwise. Therefore, we call for a total coincidence on all the components of the vector of predicted classes $\mathbf{c}_{i}^{\prime}$ and the vector of real classes $\mathbf{c}_{i}$. 3. Multi-label accuracy, also called Jaccard measure, as defined in Tsoumakas and Katakis (2007):

$$ M L-\operatorname{Acc}=\frac{1}{N} \sum_{i=1}^{N} \frac{\left|\mathbf{c}_{i} \wedge \mathbf{c}_{i}^{\prime}\right|}{\left|\mathbf{c}_{i} \vee \mathbf{c}_{i}^{\prime}\right|} $$

where in the numerator we count the number of coincidences of the two vectors (real and predicted), and in the denominator we count the number of labels covered by some of both vectors. 4. F-measure is the harmonic mean between precision and recall:

$$ F-\text { measure }=\frac{1}{d} \sum_{j=1}^{d} \frac{2 p_{j} r_{j}}{\left(p_{j}+r_{j}\right)} $$

where $p_{j}$ and $r_{j}$ are the precision and recall for $C_{j}$. Here, the F-measure is calculated per label and then averaged.

### 6.3. Experiments and results

In Zaragoza et al. (2011b) it was shown that the simplest BCC, a TNBCC, was able to outperform nine state-of-the-art multidimensional Bayesian network classifiers (including: tree-tree, polytree-polytree, pure-wrapper, pure-filter and hybrid, among others) on several testbed problems with a significantly lower time complexity. In this paper, we perform several experiments to evaluate different variants of BCCs, and compared them against other multi-label classifiers, such as binary relevance and chain classifiers:

1. TNBCC against the binary relevance method (Section 6.3.1).
2. Different chain orders (Section 6.3.2) and chain complexities (Section 6.3.3).
3. One vs. all previous classes in the tree incorporated in each base classifier (Section 6.3.3).
4. Different base classifiers (Section 6.3.4).
5. Different heuristics for selecting the root node (Section 6.4).
6. Different training techniques for chain classifiers (Section 6.4).
7. A single chain versus an ensemble of chains (Section 6.4).

We used 10-fold cross-validation for the five smaller data sets and 3-fold cross-validation for the larger data sets. We repeated this process 10 times for the smaller data sets and 5 times for the larger ones and reported the average results. We performed statistical significance tests using a $t$-test for the five smaller data sets. For the larger data sets, however, we used Wilcoxon rank sum test, since we performed only a small number of runs. In both cases

[^0]: ${ }^{1}$ The data sets can be found at http://mulan.sourceforge.net/datasets.html, http:// mlkdzssd.auth.gr/multilabel.html and http://www.cs.waikato.ac.nz/ml/weka/ index.html.

we used $\alpha=0.05$. If the differences in the results are statistically significant an " $\alpha$ " symbol is shown in the tables. In Tables 2-6 the best results for each database and for each evaluation metric are shown in bold.

We used the naïve Bayes and SVM implementations of Weka (Hall et al., 2009).

### 6.3.1. TNBCC against binary relevance

We start by comparing the TNBCC approach with a baseline algorithm that constructs independent classifiers for each class binary relevance method (BRM). The results are presented in Table 2 for the four evaluation metrics.

From the table, it can be seen that in average, the TNBCC approach obtained better results than the baseline algorithm. Moreover, for most of the data sets the results are statistically significant. However, for the Medical and TMC2007 data sets the independent approach obtained better results than TNBCC for some metrics. We believe that in these data sets the classes are fairly independent between each other. To corroborate this hypothesis, we constructed a (Pearson) correlation matrix between classes for all the data sets. From this analysis, we found that for the data sets Scene, Medical and TMC2007 there is almost no correlation between classes.

### 6.3.2. TNBCC against a random tree and a random chain

The next experiment compares the performance of a TNBCC against a random tree that is built without considering the dependencies between classes, and also a random chain of classifiers as in Read et al. (2009). Table 3 shows that for the four different measures.

The results with the TNBCC strategy are, as expected, better than the ones using a random tree. When compared to a random chain as in Read et al. (2009) we can see that TNBCC achieves better performance results in most measures and data sets: (a) in $M$-Acc, TNBCC significatively outperforms a random chain in two data sets and is significatively beaten by a random chain in two other data sets (i.e. two wins and two losses); (b) in G-Acc, there are three wins vs. one loss; (c) in ML-Acc, we obtain three wins and two losses, and (d) in F-measure, four wins and no losses are found. On average, TNBCC is superior to a random tree and a random chain for three of the four measures.

Table 2
Tree naïve Bayesian chain classifiers (TNBCC) against binary relevance (BRM).


The results show that using information about the dependencies of the classes, even by considering a single parent, clearly benefits the performance of the classifier.

### 6.3.3. Number of parents for each base classifier

The next experiment compares TNBCC against a more elaborated strategy. Given that TNBCC only uses the parent node as a new attribute for the chain, in this experiment we incorporate all previous classes in the path towards the root of the tree as additional attributes. The idea is to incorporate more contextual information to each classifier, considering not only the directly relevant class but also all the indirectly related classes. We call this scheme a path-BCC. Table 4 presents the results of comparing the TNBCC approach and the path-BCC version.

The results show that using all the precedent classes as attributes contributes to statistically significant better results (two wins in $M$-Acc, one win in $G$-Acc, four wins in ML-Acc and five wins in F-measure), although in some data sets the best significant results are obtained when using a single parent (one win in $M$-Acc, $G$-Acc and $F$-measure, and two wins in $G$-Acc). The pathBCC is still computationally more efficient than considering all the previous classes as in a random chain classifier.

### 6.3.4. Different base classifiers

So far, we have used in all the experiments naïve Bayes as base classifier. In this experiment we want to evaluate the relevance of the base classifier, so we compare the results obtained by tree naïve BCC with a tree BCC that uses kernel support vector machines (TSVMBCC). We also present a comparison with a chain classifiers, including a chain with NB as base classifier (NB-CC) and a chain with SVMs (SVM-CC) as in Read et al. (2009). The results are presented in Tables 5 and 6.

From these results we can notice that using a more elaborate classifier yields better performance on average; however, as it happens with other classification problems, a simpler classifier sometimes obtains the best results. This applies to both, the tree BCCs and the chain classifiers. It should be noticed that TSVMBCC and SVM-CC tend to produce better results on the larger data sets.

An important result is that TSVMBCC is in most cases superior for all measures and data sets to the SVM-CC approach, which is basically the same as the chain classifier in Read et al. (2009) and Read et al. (2011).

### 6.4. Other tests

We performed other experiments, but due to space limitations, we only describe here our main results. In particular, during the training phase of a chain classifier, the learning method can use the predicted values of the previous classes in the chain or the original values as previously discussed in Section 5.1. In our experiments, in most cases training with the original data produces better results, although for the F-measure the results are very similar.

In all the previous experiments, once a tree-based structure was built with Chow and Liu's algorithm, the root node was randomly selected. We tested different strategies for selecting the root node and found that using an ordered derived from the dependencies of the classes is relevant; however, once the tree-structure is obtained, there is no significant difference between which node to select as root.

We also compared the results of tree naïve BCC and an ensemble of ten TNBCCs, denominated ETNBCC, with different roots in the tree selected randomly and found that ETNBCCs performs better than the single TNBCC specially in the larger data sets. The difference, however, is not very large considering that it is, in this case, ten times slower.

Table 3 Experimental comparison between TNBCC, a random tree (Random Tree), and a random chain (Random Chain). " $\star$ " means significant difference between TNBCC and Random Tree and " $\dagger$ " means significant difference between TNBCC and Random Chain. (Results are not reported for Delicious because the Random Chain did not finish after one week.)


Table 4
Experimental comparison of TNBCC and path-BCC.


### 6.5. Discussion

From the experiments we can draw the following conclusions:

- Finding dependencies among classes guides the chaining process and achieves better evaluation performance, even with a simple tree-based structure.
- The basic TNBCC is competitive with state of the art chain classifiers and at the same time very efficient.
- Once the dependency structure among classes is defined, choosing a particular root node is apparently not relevant.
- Incorporating information of indirectly relevant classes does make a difference. Although it requires more computational resources it is still less expensive than a chain classifier that considers all the previous classes in the chain.

Table 5
Mean accuracy and global accuracy of TNBCC, TSVMBCC (BCC with support vector machine as base classifier), NB-CC and SVM-CC (chain classifier as in Read et al. (2009) with naive Bayes and support vector machine as base classifiers). " $\star$ " means significant difference between TNBCC and SVM-CC, " $\dagger$ " means significant difference between TSVMBCC and SVM-CC, " $\S$ " means significant difference between TNBCC and NB-CC and " $\ddagger$ " means significant difference between TSVMBCC and NB-CC. (Results are not reported for Mediamill and Delicious because the SVMs did not finish after one week.)


- It is not always necessary to build a complete chain classifier as for some domains the classes are independent between each other.
- Stronger base classifiers produce stronger BCCs.
- A tree BCC with SVMs as base classifiers has in average superior performance than the standard chain classifier that includes all previous classes in the chain as in Read et al. (2009).
- Ensembles of tree naïve BCCs (ETNBCCs) appear to perform better than single TNBCCs.

Table 6
Multilabel accuracy and F-measure of TNBCC, TSVMBCC (BCC with support vector machine as base classifier), NB-CC and SVM-CC (chain classifier as in Read et al. (2009) with naive Bayes and support vector machine as base classifiers). " + " means significant difference between TNBCC and SVM-CC, " $\dagger$ " means significant difference between TSVMBCC and SVM-CC, " $\|$ " means significant difference between TNBCC and NB-CC and " $\|$ " means significant difference between TSVMBCC and NB-CC. (Results are not reported for Nodianill and Delicious because the SVMs did not finish after one week.)


## 7. Conclusions and future work

In this paper we have introduced Bayesian chain classifiers for multi-label classification problems. We experimented with the simplest model for a BCC, considering a tree structure for the class dependencies and a simple naïve Bayes classifier as base classifier. The proposed approach is simple and easy to implement, and yet is highly competitive against multidimensional Bayesian network classifiers (as shown in Zaragoza et al. (2011b)) and also against chain classifiers. In this paper, we extend our previous work with a more thorough analysis of BCCs and considering several alternative strategies for building them.

It is shown that inducing an undirected tree and randomly picking a class as root of this tree is enough to produce competitive results, both in terms of accuracy and time complexity, against other state-of-the-art algorithms. We proposed and analyzed experimentally several alternatives to the basic BCC, showing that some extensions do make a difference in performance with a small increment in complexity; while other do not have a significant impact.

BCC opens a new research avenue for multi-label classification research as considering dependencies among classes is clearly beneficial, as shown in this paper.

As future work we will explore alternative models considering more complex dependency structures, identifying independent classes to simplify the chaining process, and more alternatives on how to incorporate other related classes to improve the performance results.

## Acknowledgments

The authors wish to acknowledge FONCICYT for the support provided through Project No. 95185 (DyNaMo).

Also, this research has been partially supported by the Spanish Ministry of Economy and Competitiveness, projects TIN201020900-C04-04, Consolider Ingenio 2010-CSD2007-00018 and Cajal Blue Brain.
