# Medical images modality classification using discrete Bayesian Networks 

Jacinto Arias ${ }^{\mathrm{a}}$, Jesus Martínez-Gómez ${ }^{\mathrm{a}, \mathrm{b}}$, Jose A. Gámez ${ }^{\mathrm{a}}$, Alba G. Seco de Herrera ${ }^{\mathrm{c}}$, Henning Müller ${ }^{\mathrm{c}}$<br>${ }^{a}$ University of Castilla-La Mancha, Spain<br>${ }^{b}$ University of Alicante, Spain<br>${ }^{c}$ University of Applied Sciences Western Switzerland, Switzerland


#### Abstract

In this paper we propose a complete pipeline for medical image modality classification focused on the application of discrete Bayesian network classifiers. Modality refers to the categorization of biomedical images from the literature according to a previously defined set of image types, such as X-ray, graph or gene sequence. We describe an extensive pipeline starting with feature extraction from images, data combination, pre-processing and a range of different classification techniques and models. We study the expressive power of several image descriptors along with supervised discretization and feature selection to show the performance of discrete Bayesian networks compared to the usual deterministic classifier used in image classification. We perform an exhaustive experimentation by using the ImageCLEFmed 2013 collection. This problem presents a high number of classes so we propose several hierarchical approaches. In a first set of experiments we evaluate a wide range of parameters for our pipeline along with several classification models. Finally, we perform a comparison by setting up the competition environment between our selected approaches and the best ones of the original competition. Results show that the Bayesian Network classifiers obtain very competitive results. Furthermore, the proposed approach is stable and it can be applied to other problems that present inherent hierarchical structures of classes.


Keywords: Medical Image Analysis, Visual Features Extraction, Bayesian Networks, Hierarchical Classification

## 1. Introduction

Medical images are essential for diagnosis and treatment planning. These types of images are produced in ever-increasing quantities and varieties [1]. A

[^0]
[^0]:    Email addresses: Jacinto.Arias@uclm.es (Jacinto Arias), Jesus.Martinez@uclm.es (Jesus Martínez-Gómez), Jose.Gamez@uclm.es (Jose A. Gámez), alba.garcia@hevs.ch (Alba G. Seco de Herrera), henning.mueller@hevs.ch (Henning Müller)

recent European report estimates medical images of all kind occupied $30 \%$ of the global digital storage in 2010 [2].

Clinicians use images of past cases in comparison with current images to determine the diagnosis and potential treatment options of new patients. Images are also used in teaching and research $[3,4]$. Thus, the goal of a clinician is often to solve a new problem by making use of previous similar cases/images together with contextual information, by reusing information and knowledge [5].

Systematic and quantitative evaluation activities using shared tasks on shared resources have been instrumental in contributing to the success of information retrieval as a research field and as an application area in the past few decades. Evaluation campaigns have enabled the reproducible and comparative evaluation of new approaches, algorithms, theories and models through the use of standardized resources and common evaluation methodologies within regular and systematic evaluation cycles. The tasks organized over the years by Image$\mathrm{CLEF}^{1}$ [6] have provided an evaluation forum and framework for evaluating the state of the art in biomedical image retrieval.

In this article, we evaluate a probabilistic approach for medical image classification by using the ImageCLEF 2013 medical image modality classification task [7] as a benchmarking environment. We propose a reproducible methodology based on the use of discrete Bayesian Network Classifiers (BNCs) [8]. Our approach first explores details of the modality classification and medical image processing. This is done by defining a basic pipeline in which the application of BNCs is straightforward. The defined pipeline includes a problem transformation from its usual continuous domain to a discrete one that is more natural for probabilistic approaches. In the classification stage we dive into the problem of modality classification to evaluate several proposals in order to deal with the relatively large number of classes (31) that the task presents; for this we focus on hierarchical classification and multi-class approaches. Fig. 1 shows a scheme with all the stages taking part in the described pipeline for the classifier generation process.

Our proposal is based on an extensive experimental evaluation of the proposed pipeline using a collection of probabilistic instead of deterministic classifiers that are the common approaches to tackle this kind of problem [9, 10]. The BN models selected for the experimental analysis show an advantage in their trade-off between efficiency and quality. They also demonstrate a promising performance in a wide range of domains such as document classification [11], object detection [12] or semantic localization [13].

Moreover, probabilistic graphical models are suitable for the integration of contextual categorical variables in conjunction with descriptors extracted from computer vision techniques. Contextual information, such as human annotations or semantic attributes, are becoming more frequent and they can be obtained automatically by means of external tools like Amazon mechanical turk [14]. This kind of information cannot be directly incorporated in other

[^0]
[^0]:    ${ }^{1}$ http://imageclef.org/

![img-0.jpeg](img-0.jpeg)

Figure 1: Classifier Generation Pipeline.
traditionally used methods while maintaining its descriptive properties; black box designed algorithms such as SVMs or Neural Networks are not suitable to properly represent dependency relation or other qualitative information in the data.

Regarding the evaluation of our proposed technique, we conducted experiments by following a competition scheme using the ImageCLEF 2013 training and test sets of images separately, for model selection and evaluation respectively. The purpose of this decision is twofold: first of all, to compare the proposed approaches with the best systems participating in the competition by using only the training subset of images for model selection, and to evaluate the most promising approaches on the test data; second, we use the original ImageCLEFmed training and test sets from the competition to keep the original challenge difficulty, allowing our model selection to remain unbiased and to avoid overfitting. To this extent, we did not perform any parameter tuning, thus leaving our basic approach using only baseline models and strategies as the goal of this paper is to show the competitiveness of BNC over the standard approaches used for this problem and not to adjust the model to this exact benchmark. The final results show that our approach would have ranked 3rd in the competition (where 7 groups sent their results of a variety of techniques) being a promising result as it is a non-specific approach that leaves room to several improvements as it will be discussed at the end of the paper. The better results also used extended training sets, which was not used int he work described here.

The rest of the article is organized as follows. We first review the related work in the field of medical image classification in Section 2. Sections 3 and 4 describe the background on computing visual features and Bayesian Network classifiers. The pre-processing of the data is then discussed in Section 5 and the different strategies for hierarchical and multi-class classification are introduced in Section 6. Finally, an extensive experimentation is conducted and analyzed in Section 7 and in Section 8 we summarize the obtained results and obtain a

brief perspective of future work and extensions.

# 2. Background and Related work 

The interest of the visual retrieval community in the automatic analysis of medical information was motivated in part thanks to the medical ImageCLEF challenge. The medical task has run at ImageCLEF since 2004, with many changes between different editions [6]. The underlying objective of this challenge is the retrieval of similar images to fulfill a precise information need and image classification. The 2009 edition of the task [15] focused on the retrieval of articles from the biomedical literature that might best suit a provided medical case description (including images). In 2010 [16], the organizers introduced the modality classification task.

The goal of modality classification is to classify the images of the literature into medical modalities and other image types, such as Computer Tomography (CT), X-ray or general graphs. Medical image classification by modality can improve the retrieval step by filtering or re-ranking the results lists [17]. Moreover, it can reduce the search space to a set of relevant categories improving the speed and precision of the retrieval [18]. Some example images used in the modality classification task are shown in Fig. 2.
![img-1.jpeg](img-1.jpeg)

Figure 2: Examples of medical images from various moralities.
The modality classification task was maintained until 2013 [6]. The image collection provided in 2013 was used for the evaluation in this article. This collection includes 2896 annotated training images and 2582 test images to be classified. Each image belong to one of the 31 classes that present an intrinsic hierarchy shown in Fig. 3.

The techniques presented, rely mainly on two key stages: a.- extraction of visual features from the images, and b.- generation of classification models. Regarding the feature extraction, several studies have shown that the modality can be extracted from the visual content using only visual features [19, 20]. The extracted visual features must then be transformed to obtain meaningful descriptors. For instance, Kitanovski et al. [9] use a spatial pyramid in combination with dense sampling using an opponentSIFT descriptor for each image patch.

Support Vector Machines (SVMs), in combination with the $\chi^{2}$ kernel, are the most common classification model used in the competition [21, 9, 10]. However, other deterministic classifiers such as $k$-Nearest Neighbor [22] were also

![img-2.jpeg](img-2.jpeg)

Figure 3: The image class hierarchy provided by ImageCLEFmed for document images occurring in the biomedical open access literature.
used. Despite their lack of descriptive capabilities, these classification models present properties that have encouraged their use in image classification problems. They can work with numeric input data, which is the most common output from feature extraction techniques. They can properly cope with the high dimensionality of the image descriptors.

The hierarchical relationship between the categories in the medical task can also be found in other problems, such as object categorization [23]. In this problem, we can find solutions where SVM classifiers are applied over the combination of different 3D descriptors [24], as well as hierarchical decomposition of the descriptors [25] but the explicit management of the object hierarchy is very seldom adopted.

Though different Bayesian and non-Bayesian probabilistic methods have been applied for medical image analysis (see e.g. [26]), the use of BNCs has been scarce to the best of our knowledge. None of the participants of the ImageCLEFmed modality classification task presented approaches based on BNCs. One of the main reasons could be the continuous domain of the features used in medical image classification, while the developments for BNCs have been mainly devoted to the discrete case. In fact, some BN models are available to deal with numerical variables, but they have two major shortcomings: the Gaussian assumption and structural constraints, e.g. a discrete variable cannot be conditioned on a numerical one. Nevertheless, some approaches to medical image analysis problems have been carried out by using discrete BN [27], al-

though they reduce to the use of Naive Bayes and Tree Augmented Naive Bayes (TAN) algorithms.

# 3. Feature extraction and descriptor generation 

The transformation of an input image into a set of features tht describe it is a key stage for a subsequent classification task. This process is known as feature extraction and can be accomplished in different ways, as it is discussed in [28]. In this paper, we follow the scheme proposed in [29], where a combination of multiple low-level visual features is explored. In this paper, the same combination of visual descriptors is applied. Therefore, the descriptors used are the following:

- Bag of Visual Words (BoVW) using Scale Invariant Feature Transform (SIFT) (BoVW-SIFT) [30] - Each image is represented by an histogram symbolizing a set of local descriptors represented in visual words from a vocabulary previously learned with 238 visual words. This leads to a 238 bin histogram;
- Bag of Colors (BoC) [31] - Each image is represented by a 100 bin histogram symbolizing the colors from a vocabulary previously learned;
- Color and Edge Directivity Descriptor (CEDD) [32] - Color and texture information is produced by a 144 bin histogram. Only little computational power is required for its extraction;
- Fuzzy Color and Texture Histogram (FCTH) [33] - This descriptor contains results from the combination of 3 fuzzy systems including color and texture information in 192 bin histogram;
- Fuzzy Color Histogram (FCH) [34] - The color similarity of each pixel's color associated with a 192 histogram bin through a fuzzy-set membership function is used;

These descriptors are extracted using the ParaDISE (Parallel Distributed Image Search Engine) [35]. The combination of all these features generates descriptors with a dimensionality of 866 .

## 4. Bayesian Network classifiers

Bayesian Networks (BNs) [36] are one of the most frequently used knowledge representation techniques when dealing with uncertainty, mostly owing to their predictive/descriptive capabilities. They are based on sound mathematical principles and, as a probabilistic graphical model, they output a graphical structure that provides an interpretative representation of the relationships between the variables of the problem.

Learning general BNs is known to be a complex problem [37] involving the task of structural learning as well as parameter estimation [38]. As learning general BNs is usually problematic, this has lead to the definition and wide usage of specific models that are explicitly designed to tackle the standard classification problem, these are commonly known as Bayesian Network Classifiers (BNCs) $[39,8]$.

The simplest BNC model is the Naive Bayes classifier (NB) that avoids structural learning by assuming that all attributes are conditionally independent given the value of the class. Although this independence assumption can be considered too strong for some domains, the NB classifier has shown very good results in many real applications such as computing, marketing and medicine [40]. Its results can be improved by slightly alleviating its independence assumption and using a more complex graphical structure. The techniques using this principle are known as semi-naive Bayesian network classifiers, some of them are among the most competitive classification techniques.

We evaluated the performance of different semi-naive BNC models to solve the proposed classification problem, specifically: NB, TAN, K-Dependence Bayesian classifiers (KDB) and Average One Dependence Estimators (AODE).

# 4.1. Naive Bayes 

NB classifier [41] is the simplest BNC, due to its independence assumption which avoids any needs for structural learning. This classifier uses a fixed graphical structure in which all predictive attributes are considered independent given the class, as it is depicted in Fig. 4a. This implies the following factorization: $\forall c \in \Omega_{C} p(\vec{e} \mid c)=\prod_{i=1}^{n} p\left(a_{i} \mid c\right)$. Here, the maximum a posteriori (MAP) hypothesis is used to classify:

$$
c_{M A P}=\operatorname{argmax}_{c \in \Omega_{C}} p(c \mid \vec{e})=\operatorname{argmax}_{c \in \Omega_{C}}\left(p(c) \prod_{i=1}^{n} p\left(a_{i} \mid c\right)\right)
$$

### 4.2. Tree-Augmented Naive Bayes

The TAN classifier [39] can be considered a structural augmentation of the NB classifier in which the conditional independence assumption is relaxed by allowing a restricted number of relationships between the predictive attributes. This strategy implies that a structural learning process must be performed. However, TAN can still obtain competitive learning times with moderate datasets establishing a good trade-off between model complexity and model accuracy. In particular, every predictive attribute is allowed to have an extra parent in the model in addition to the class. In order to learn these dependencies a Maximum Weighted Spanning tree (MWST) is learned by using the Chow-Liu algorithm [42] with the conditional mutual information between each pair of attributes and the class as metric to measure each arc weight:

$$
M I\left(A_{i}, A_{l} \mid C\right)=\sum_{r=1} p\left(c_{r}\right) \sum_{i=1} \sum_{j=1} p\left(a_{i}, a_{j} \mid c_{r}\right) \log \frac{p\left(a_{i}, a_{j} \mid c_{r}\right)}{p\left(a_{i} \mid c_{r}\right) p\left(a_{j} \mid c_{r}\right)}
$$

![img-3.jpeg](img-3.jpeg)

Figure 4: Graphical structure of semi-naive Bayesian Network Classifiers.

This process guarantees that the tree learned from the training data is optimal, i.e. it is the best possible probabilistic representation from the available data as a tree as it maximizes the log likelihood. Once the tree is obtained, an arbitrary node is selected as the root of the tree and the edges are oriented to create a directed acyclic graph in which all attributes are conditioned to the class, creating the final BNC structure of a TAN classifier. An example is shown in Fig. 4b.

# 4.3. K-Dependence Bayesian classifiers 

The basic KDB classifier is based on the notion of a $k$-dependence estimator introduced by Sahami [43] in which the structure of a basic NB classifier can be augmented by allowing an attribute to be conditioned to a maximum of $k$ parent attributes in addition to the class, thus covering the full spectrum from the NB classifier to a general full BN structure by varying the parameter $k$. An example for a given value of $k$ is shown in Fig. 4c.

The KDB classifier itself performs a three-stage learning process:

1. A ranking is established between the predictive attributes by means of their mutual information with the class variable.
2. For each attribute $A_{i}, i$ being its position on the previous ranking, the $k$ attributes taken from $\left\{A_{1}, \ldots, A_{i-1}\right\}$ with the highest conditional mutual information $M I\left(\cdot, A_{i} \mid C\right)$ are set as the parents of $A_{i}$.

3. The class variable $C$ is added as a parent for all the predictive attributes. This classifier presents a more flexible approach to the TAN classifier (in fact, the TAN classifier is a particular case of KBD with $K=1$ ), as it is capable of adjusting the mentioned trade-off between model complexity and model quality.

# 4.4. Averaged One Dependence Estimators 

AODE [44] are an alternative to other semi-naive BNC approaches. They present a fixed structure model that avoids structural learning, improving its efficiency when compared to other BNCs that require the step. Moreover, AODE maintains very competitive model quality.

Therefore, AODE is restricted exclusively to 1-dependence estimators. This classifier can be seen as an ensemble of models, concretely, it considers each model belonging to a specific family of classifiers (known as SPODEs (Superparent One-Dependence Estimators)) in which every attribute is dependent on the class and on another shared attribute, designated as superparent. The structure of a specific SPODE is depicted in Fig. 4d.

For classification, AODE computes the average of the $n$ possible SPODE classifiers:

$$
C_{M A P}=\arg \max _{c \in \Omega_{C}}\left(\sum_{j=1, N\left(a_{j}>q\right)}^{n} p(c) \cdot p\left(a_{j} \mid c\right) \prod_{i=1, i \neq j}^{n} p\left(a_{i} \mid c, a_{j}\right)\right)
$$

## 5. Data pre-processing

Input data can be pre-processed to meet the requirements of the classification models, to reduce their complexity but also to increase their performance. Here, we enumerate three data pre-processing techniques. First, we propose a combination of the different descriptors extracted from the image. Then, we discretize the input data to obtain nominal variables suitable for their use in the classification models. Finally, we select a subset of variables from the whole set.

### 5.1. Descriptor combination

In this article, we opted to use five descriptors generated from visual features extracted from the input images: BoVW-SIFT, CEDD, FCTH, FCH, BoC (see Section 3). Every descriptor consists of numeric variables with dimensionality between 100 and 238, which represents visual feature frequencies (see Sec. 3 for more details on the visual features). They can be concatenated to create a single descriptor, as it is commonly done when working with SVMs. However, we can also follow an aggregation approach to merge descriptors in a recursive way, where we can include pruning strategies. From an initial set of $n$ descriptors, we can generate the following number of combinations,

$$
\sum_{i=1}^{n} \frac{n!}{i!(n-i)!}
$$

which would result in 31 different combinations from an initial set of 5 descriptors $(5+10+10+5+1)$.

# 5.2. Discretization 

Some of the internal variables of the image descriptors contain discriminant information but others can be useless for the problem we are facing. While Bayesian classifiers exist tackling numeric variables [45] (e.g. Gaussian Naive Bayes), we opted for the exclusive use of discrete classification models. The main reason for this decision is that some numeric versions of the classifiers assume that input data can be modeled with uni-modal distributions [46], which is not always true. Here, we propose the use of the Fayyad Irani discretization method [47], which can be considered a standard approach. This discretization method takes into account the class information when selecting the number of bins and breaking points by using mutual information. Moreover, it selects the optimal number of bins separately for each input variable. As seen in the experimentation (see Section 7), this discretization step produces a number of binary partitions. It also discretizes input variables into a single bin, which means that the variable has no discriminant power with respect to the class, thus resulting in useless variables that are removed in subsequent steps.

### 5.3. Feature Subset Selection

The number of input variables, which comes from the descriptors combination, can be successfully reduced by following an appropriate procedure. In addition to data reduction, this step can also increase the accuracy of the classification model by finding redundant or irrelevant input variables. Moreover, using fewer variables also provides non-overfitted and more interpretable classification models, which requires shorter training times. In order to avoid the bias introduced by the classification method while using wrapper approaches, we selected a filter strategy. We opted for the Correlation Feature Selection (CFS [48]), which has shown its value in several scenarios.

## 6. Strategies

In addition to the classical data pre-processing (discretization and feature subset selection, which only affects the predictive attributes), we can also take advantage from strategies that cope with multi-class problems. The first alternative consists of partitioning the original problem into recursive sub-problems using a hierarchy of classes. The second strategy splits the multi-class problem into $n$ binary problems with decisions being merged to select the final decision. This second strategy was discarded in a first round of preliminary experiments where no significant improvements were obtained when using several multi-class approaches, such as One-versus-All (OvA) [49]. The improvements of OvA were limited to the absence of hierarchical approaches due to the large number of classes (31).

# 6.1. Hierarchical classification 

The intrinsic relationships between class values in a multi-class problem provides us with relevant information that is commonly discarded. However, this information can be used to create a multi-layer classification scheme [50] where each level corresponds to a degree in the hierarchy of the classes. This involves the generation of more classification models but the training stage in second (and subsequent) layers is performed from a set with a smaller number of instances.
![img-4.jpeg](img-4.jpeg)

Figure 5: Overall class hierarchy and instance distribution using a 3-level approach

Fig. 5 shows a 3-level hierarchy generated from the inherent relationships between the classes of the ImageCLEF 2013 medical classification task. This figure also includes the number of training instances that affect the generation for each one of the seven classifiers (1-class classifiers are not considered) when applying a three layer hierarchy. As it can be observed, classifiers from levels 2 and 3 are generated from a lower number of instances than those from level 1. In addition to the 3-level hierarchy shown in Fig. 5, we can adopt either a 1-level approach (no hierarchy) or a 2-level one, which generates one single or eight different classifiers respectively.

# 7. Results 

### 7.1. Parameter Selection

The first round of experiments was conducted with two main objectives: validating the proposed methodology, and performing an initial selection from the set of internal parameters. The experiments were carried out using the training set from the ImageCLEF 2013 medical classification task, which includes 2896 images and 31 nominal classes by performing a 5 fold cross-validation.

### 7.1.1. Descriptor Combination

There are 31 descriptor combinations as result of merging the 5 initial sets of descriptors: $\operatorname{SIFT}\left(D_{1}\right), \operatorname{BoC}\left(D_{2}\right), \operatorname{CEDD}\left(D_{3}\right), \operatorname{FCTH}\left(D_{4}\right)$, and $\mathrm{FCH}\left(D_{5}\right)$. Each combination was evaluated using the following options:

- Hierarchical Classification (see Fig. 5)
- 1-level hierarchy (no hierarchy)
- 2-level hierarchy
- 3-level hierarchy
- Discretization
- Fayyad-Irani
- Feature Subset Selection
- Correlation Feature Selection (CFS)
- Classification Model / Algorithm
- Naive Bayes (NB)
- Tree Augmented Naive Bayes (TAN)
- Average One Dependence Estimators (AODE)
- K-Dependence Bayesian Classifier (KDB)

By combining all these options for the described parameters, we generated and tested a total of 465 classifiers. Results are graphically presented in Fig. 6 and detailed in Table A.4. Results show a clear difference in performance between the combinations of descriptors where higher accuracy is obtained from larger descriptor combination. This result implies that integrating descriptors increases the expressive power of the classifier and that the proposed pre-processing pipeline is effective in practice, as the feature subset selection (FSS) process copes properly with an increasing number of input attributes, retaining useful information for each one of the combined descriptors. Fig. 7 shows the evolution of the number of attributes in the final combination when we increase the size of the combined descriptors by adding new ones; the figure

![img-5.jpeg](img-5.jpeg)

Figure 6: Preliminary results for each hierarchical approach, classifier and descriptor combination using a 5 -fold cross validation over the full training set. The results are summarised as the mean accuracy for all the different combination of the same number of descriptors. The error bars correspond to the maximum and minimum values for such an experiment.
exposes how a combination of a larger number of descriptors does not necessarily involves higher dimensionality once FSS in applied, in fact we can observe an asymptotic behavior when the number of descriptors in the combination is increased. Given these results, we decided to continue the experimentation by selecting the entire combination of descriptors $D_{1,2,3,4,5}$ as the candidate.

Regarding the classification models and the proposed hierarchies, results from the Table A. 4 show that the usage of a hierarchy improves upon the results when compared to dealing with the 31 original classes using a single classifier. If we compare the models we can observe a better performance of AODE when performing hierarchical classification, however KDB is superior when dealing with the flat class structure ( 31 classes). To analyze these results we performed a statistical evaluation on the performance of each model for each one of the hierarchy approaches. The Friedman test [51] with a 0.05 confidence level rejects the three hypotheses of all classifier being equivalent when using any of the hierarchy levels. A further post-hoc statistical analysis using the Holm procedure is included in Table 1, in which we compare the performance of all classifiers with the best one for each one of the hierarchies. This confirms how KDB clearly outperforms the other classification models within a 1-level hierarchy. However, AODE stood out when taking advantage of the 2 or 3 levels of the hierarchy. This exposes KDB as the optimal classifier when coping with a large number of

classes, while AODE performs notoriously better in the remaining scenarios.
![img-6.jpeg](img-6.jpeg)

Figure 7: Effect on the FSS procedure for two different hierarchical approaches when using different combinations of descriptors.

Table 1: Classification model ranking. $\mathrm{w} / \mathrm{t} / \mathrm{l}$ denote the number of scenarios the first ranking method wins(w) ties(t) and looses(l) the evaluated method


# 7.2. Final Results 

The last experimental stage was carried out following the procedure proposed in the ImageCLEF 2013 medical classification task. Namely, we learned classification systems using the 2896 training images and evaluated such systems against the 2582 test images. In order to perform a fair evaluation we followed the original rules of the competition. We selected the best 10 classification systems that achieved highest results in previous experiments using only the training data, i.e., we evaluated the selected models over the provided the test set and computing the accuracy of our systems. We used the ten best results because this was the limit in the number of task submissions. The internal

parameters for the systems, as well as the accuracy obtained both against the training set that was used to rank the models (with 5 -folds cross-validation) and test sequences are shown in Table 2 .

Table 2: Final results obtained against the test set with the 10 configurations that ranked first in previous experiments.


If we compare the training and test columns in Table 2, we can observe that we are obtaining higher results over the test set. This trend supports the stability of our methodology, allowing the generation of non-overfitted classification systems. All the evaluated systems share the following internal parameters: AODE as classification model, 2 or 3 levels of hierarchy and large combinations of initial descriptors. As previously pointed out, the multi-class approach did not obtain significant improvements on the accuracy once the hierarchy is applied. An important detail is that the best result for the training set is obtained by using the 2 level hierarchy whereas the best results for the test set corresponds to those approaches using the 3 level hierarchy. This is probably due to the small size of the training set compared to the size of the test set, which supports the generalization capabilities of the proposed framework.

# 7.3. ImageCLEF 2013 medical task results 

Our maximum accuracy obtained over the test set was $69.21 \%$. This result ranked 3rd in the modality classification task of ImageCLEF 2013, as shown in Table 3. We can observe how most of the teams used Support Vector Machines (SVMs) as classifier, while none of them used a probabilistic model. Apart from SVMs, only the K-Nearest Neighbor (K-NN) and the Stochastic gradient descent (SGD) were used. With respect to the image descriptors used by the participants, most were based on histogram representations or bag of words approaches managing continuous information, but other more complex techniques (such as the spatial pyramid [52]) were also used. The best results both used a training set expansion, which can explain part of the gains. On the contrary, our proposal relies on just the training provided by the task organizers, which

is not biased nor optimized to artificially increase the accuracy at the expense of lack of generalization.

Table 3: Highest accuracies (by group) in the ImageCLEF 2013 modality classification task including our best result.


# 7.4. Analysis of the results 

We carried a posterior analysis of the results to identify the points suitable for improvements of our methodology. The first study examined the accuracy of the internal classifiers involved in the hierarchical classification. We evaluated the system that ranked 5th in Table 2 which is best in the test set. It uses a 3-level hierarchy with 7 internal classifiers (see Fig. 5). For each of these seven classifiers, we computed two accuracy measures: $\operatorname{Acc}(\mathrm{a})$.- the overall accuracy, and $\operatorname{Acc}(\mathrm{b})$.- the accuracy obtained only with instances that were correctly classified in upper levels. $\operatorname{Acc}(\mathrm{b})$ reflects the isolated behavior of each classifier, while $\operatorname{Acc}(\mathrm{a})$ is affected by the rest of the system.
![img-7.jpeg](img-7.jpeg)

Figure 8: $\operatorname{Acc}(\mathrm{a})$ and $\operatorname{Acc}(\mathrm{b})$ computed for a classification system including $D_{1,2,3,4,5}$ descriptors, 3-hierarchy levels and AODE as classification model without multi-class approach.

The accuracy from the first level classifier ( $80.33 \%$ Fig. 8) shows how nearly $20 \%$ of the test instances were wrongly classified at this level. The classifier is crucial because it processes the full test sequence and its errors are therefore propagated through the hierarchy structure. Concretely, $62.46 \%$ of the classification error came from the first classifier, while the remaining $37.54 \%$ came from the other 6 classifiers.

# 8. Conclusions 

We propose a pipeline for modality classification of medical images by using probabilistic classifiers, namely BNCs. We have identified an extensive descriptor set, a combination of descriptors, a detailed pre-processing scheme and several approaches for hierarchical and multi-class classification. We evaluated a large number of parameter combinations by using a selected range of the most popular BNCs.

Evaluation was carried out on the ImageCLEFmed 2013 collection. The AODE classifier shows superior results when combined with hierarchical classification and a large number of combined descriptors over the training set. For model selection we replicated the competition conditions by using the test set of images to compare our proposal with the best results in the competition. We obtain results that rank 3rd. From this analysis we can draw useful conclusions:

- Descriptor combinations have proven to be an expressive tool showing also the robustness of discrete supervised preprocessing techniques such as MDL discretization and feature selection. The hierarchical approach proved to be an excellent pairing with these methods, as they can be replicated easily for the hierarchy levels.
- Among all the BNCs evaluated, ensemble methods such as AODE prove to obtain highest discrimination power and thus overall best classification results. The best results are obtained when a deeper hierarchy and a larger number are combined.
- The above points suggests that, AODE, being a low-bias learner can be a suitable candidate to tackle these problems. To contrast this we performed an additional experiment in which we evaluate the models when the training set is increased incrementally. We used the best parameter combination mentioned above and the training/test split modifying the size of the training set by means of $10 \%$ random sample partitions. The results are shown in Fig. A. 9 where one can clearly observe the superior behaviour of AODE as well as a tendency to improve its results at the presence of additional data.

We believe that this is a positive result for probabilistic classifiers, as this methodology is not the most popular to be applied for solving these kind of problems. Furthermore, our selected models were not tuned or adjusted to optimize the results for the competition dataset. This means that usual techniques for

learning can still be applied to improve upon the results for the ImageCLEFmed 2013 collection such as model averaging, ensemble learning or training data expansion.

Finally, we have conducted a brief analysis of the behavior of our approach by using a probabilistic view, trying to detect the main weak points in the discrimination capabilities of the different levels of the hierarchy. The result shows that the classification error is high for many instances, either correctly or wrongly classified. In future work, we will explore the possibilities of the proposed pipeline in other classification problems where classes present an intrinsic hierarchy. We plan to apply our system to indoor scene classification problems as well.

# Acknowledgments 

This work is partially funded by the FEDER funds and the Spanish Government (MICINN) through projects TIN2013-46638-C3-3-P, PPII-2014-015P, and TIN2015-65686-C5-3-R. Jacinto Arias is funded by the MECD grant FPU13/00202. Jesus Martínez-Gómez is funded by the JCCM grant POST2014/8171.

# Appendix A. Detailed Results 

![img-8.jpeg](img-8.jpeg)

Figure A.9: Accuracy obtained when incrementally increasing the training set. Results are averaged by classifier.

Table A.4: Results for the descriptor combination in conjunction with the 3 hierarchies and 4 classification models. Highest accuracy (for each hierarchy) is shown in bold.
