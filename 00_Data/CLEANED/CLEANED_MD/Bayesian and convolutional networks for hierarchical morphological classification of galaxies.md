# Bayesian and Convolutional Networks for Hierarchical Morphological Classification of Galaxies 

Jonathan Serrano-Pérez ${ }^{1^{*}}$, Raquel Díaz Hernández ${ }^{2}$ and L. Enrique Sucar ${ }^{1}$<br>${ }^{1^{*}}$ Computer Science Dept., Instituto Nacional de Astrofísica, Óptica y Electrónica, Luis Enrique Erro No. 1, San Andrés Cholula, 72840, Puebla, Mexico.<br>${ }^{2}$ Optics Department, Instituto Nacional de Astrofísica, Óptica y<br>Electrónica, Luis Enrique Erro No. 1, San Andrés Cholula, 72840, Puebla, Mexico.<br>*Corresponding author(s). E-mail(s): js.perez@inaoep.com;<br>Contributing authors: raqueld@inaoep.mx; esucar@inaoep.mx;

## Abstract

This work is focused on the morphological classification of galaxies following the Hubble sequence in which the different classes are arranged in a hierarchy. The proposed method, BCNN, is composed of two main modules. First, a convolutional neural network (CNN) is trained with images of the different classes of galaxies (image augmentation is carried out to balance some classes); the CNN outputs the probability for each class of the hierarchy, and its outputs/predictions feed the second module. The second module consists of a Bayesian network that represents the hierarchy and helps to improve the prediction accuracy by combining the predictions of the first phase while maintaining the hierarchical constraint (in a hierarchy, an instance associated with a node must be associated to all its ancestors), through probabilistic inference over the Bayesian network so that a consistent prediction is obtained. Different images from the Hubble telescope have been collected and labeled by experts, which are used to perform the experiments. The results show that BCNN performed better than several CNNs in multiple evaluation measures, reaching the next scores: $67 \%$ in exact match, $78 \%$ in accuracy, and $83 \%$ in hierarchical F-measure.

Keywords: Morphological galaxy classification, hierarchical classification, Bayesian networks, convolutional neural networks

# 1 Introduction 

Galaxy morphological classification is essential for understanding galaxies evolution and studying stellar populations and their physical properties. For the classification, large-scale data sets are needed. Galaxy classification continues to face several difficulties and challenges despite recent advances. Some current issues and challenges include subjectivity that can lead to inconsistencies and variations in classification results, mainly due to subjective decisions made by experts based on visual inspection. The ambiguity in the diverse and complex morphology that some galaxies may present makes it difficult to define clear boundaries between the classes, allowing overlap between them, which hinders accurate classification. On the other hand, data set biases can affect the generalization and performance of models used for classification. Well-selected and balanced data sets for training and evaluation of the models are crucial for accurate classification.

In our experience, image quality is one of the challenges we face in classifying galaxy morphology. As the galaxy's images are taken using telescopes, the image quality depends on observation techniques, sky section selection, and exposition time. When galaxies are presented face-on and are well-centered, classification is more straightforward. However, it is more difficult to analyze their structure when they are edge-on, tilted, or in other positions. Therefore, it is necessary to develop identification and classification techniques that are invariant concerning the position and size of the galaxies. Also, galaxy classification models trained on specific data sets may have difficulty generalizing well to new and unknown data sets.

The challenge is to build and train computational models that can effectively capture the inherent characteristics of galaxies across different surveys, instruments, or observing conditions. As data sets grow in size and complexity, accuracy and computational efficiency become significant challenges.

An example of a large dataset to classify is Cheng et al (2022), where a comparison of two comprehensive galactic morphology catalogs created with Convolutional Neural Networks (CNNs) using Dark Energy Survey (DES) data is performed. Despite methodological differences, the two catalogs agree well up to certain magnitudes, demonstrating the reliability of CNN predictions for faint samples. The combined use of both catalogs allows the identification of unusual galaxies, providing valuable insights into galactic morphology and evolution. In a prior publication by the same author, the challenges in galaxy morphological classification are discussed, emphasizing the impact of decreasing apparent brightness and size on the accurate assessment of morphological details. The study also addresses the necessary bias corrections to address these challenges. A comparison is made between classifications obtained through CNNs and visual assessments, revealing discrepancies and underscoring the need for corrections in the galaxy sample (Cheng et al, 2021).

On the other hand, using deep learning algorithms, namely CNNs, another study utilized two classification schemes: T-type, related to the Hubble sequence, and the Galaxy Zoo 2 (GZ2) classification. The research generated the most extensive and precise morphological catalog to date by integrating precise visual classifications (Domínguez Sánchez et al, 2018). The performance of these models outperformed previous models trained with support vector machines. T-type classifications showed lower deviation and dispersion than earlier models used for this purpose.

Advances in the field involve the development of hybrid models that leverage data-driven approaches and physical modeling to improve classification accuracy. Furthermore, endeavors to assemble inclusive and comprehensive datasets, mitigate biases, and enhance deep learning models, can be crucial in solving the existing challenges in galaxy classification (Huertas-Company and Lanusse, 2023; Goan and Fookes, 2020).

A particular case of solution proposes to use CNNs and Bayesian Neural Networks (BNNs) (Goan and Fookes, 2020). Thus, using these techniques in morphological galaxy classification, the networks will estimate the properties of the galaxies, which, in turn, will allow for a better morphological classification.

The great utility of deep learning in astronomy is straightforward, specifically for galaxy classification. However, previous work does not take advantage of the hierarchy, which could help to improve accuracy. We propose Bayesian and Convolutional Neural Networks (BCNN) for morphological galaxy classification in the present work. This method combines a CNN trained with different classes of galaxies and a Bayesian network that represents the hierarchy of each type analyzed by the CNN.

The Bayesian network helps to improve the prediction accuracy by combining the predictions of the CNN while maintaining the hierarchical constraint (in a hierarchy, an instance associated with a node must be associated with all its ancestors) through probabilistic inference over the Bayesian network so that a consistent prediction is obtained. Also, we solve the class imbalance problem using data augmentation through geometric transformations.

# 1.1 Related Work 

In hierarchical classification there is a hierarchy where the labels (nodes) are arranged, an example of hierarchy is shown in Fig. 1. Hence, hierarchical classification considers the hierarchy (and the relations among the labels) in its training and predictions phases. On the other hand, flat classification focuses its training and predictions phases only on the most specific labels (the leaves of the hierarchy) while ignoring the rest of the hierarchy, as shown in Fig. 1.

Few works address the problem of hierarchical classification of galaxies since most of them are focused on flat classification, that is, they do not use a hierarchy, or there is no hierarchy to perform hierarchical classification.

Bazell (2000) carried out an analysis of feature selection for galaxy classification. Seven classes of galaxies are considered in the paper; some are also grouped to reduce the classifier's output; 22 features were selected, and an artificial neural network was trained with back-propagation as the classifier. Later, Bazell and Aha (2001) extended the previous work by including different classifiers, such as naive Bayes, decision trees, and artificial neural networks. Additionally, experiments with bagged

![img-0.jpeg](img-0.jpeg)

Fig. 1 Hierarchical classification considers, in training and prediction phases, all nodes and their relations in the hierarchy $\left\{y_{1}, \ldots, y_{8}\right\}$. Flat classification focus its training and prediction phases only on the leaves nodes (shaded in gray) $\left\{y_{3}, y_{4}, y_{6}, y_{7}, y_{8}\right\}$ while ignoring the rest of the nodes.
ensembles were carried out, showing that an ensemble may help improve a single classifier's performance; the best performance was obtained with neural networks along bagged ensembles, where the classification error was $\sim 12 \%$ when only two classes are considered.

Selim et al (2017) proposed a scheme based on the Nonnegative Matrix Factorization algorithm to perform morphological classification of galaxies. Four types of galaxies were considered: elliptical, lenticular, spiral, and irregular. Their method was applied to two datasets, small and large, where they report scores of $\sim 93 \%$ and $\sim 92 \%$ on accuracy, respectively.

Diaz-Hernandez et al (2016) addressed the problem of galaxy classification using the sparse representation technique and dictionary learning with $K$-SVD (Aharon et al, 2006). They extracted 20 features from each galaxy related to the galaxies' shape, intensity, and area. They consider eight types of galaxies which are clustered from two to seven classes, where they find that the most challenging group to qualify is the one of spiral galaxies. The highest accuracy was obtained when two classes were considered, $\sim 82 \%$ on accuracy, nevertheless, when considered the seven classes the performance was decreased to $\sim 44 \%$.

Khalifa et al (2018) proposed Deep Galaxy V2. The method consists of a convolutional neural network formed by eight layers; four are used to perform feature extraction, while the rest are focused on classification. Results in the paper reach up to $\sim 97 \%$ in exact match; nevertheless, they only consider three classes of galaxies: elliptical, spiral, and irregular.

Marin et al (2013) carried out a study of the classification of galaxies using a hierarchy. They used the same features as Bazell (2000) plus some geometric moments. Their classification scheme follows two steps; in the first step, they try to identify stars and galaxies. In the second step, they can classify the previously identified galaxies into a specific class of galaxies. They also show that their hierarchical approach got better results than a flat approach, that is, $\sim 53 \%$ and $\sim 39 \%$, respectively, in exact match.

This paper proposes a novel approach, Bayesian and convolutional neural networks, consisting of a Bayesian network fed by a CNN. Unlike most related works, there is no

feature extraction process to train a classifier later; instead, a pre-trained CNN is used to extract image features automatically. In general, the features learned automatically by a CNN tend to give better results than manually selected features; additionally, it gives us the advantage that the training can only be focused on the last layer of the CNN. Furthermore, the hierarchy is modeled as a Bayesian network, a novel way to represent the hierarchy and enforce the hierarchical constraint that related methods do not consider. On the other hand, results of the related work can not be compared directly against our results due to several reasons: the datasets are not the same, most works make use of different variants of the datasets, and they do not usually share them; the labels/classes are not the same, some works focus their research on the most general labels (spiral, irregular, elliptical, lenticular) while in this work there are 10 different labels (arranged in a hierarchy).

The rest of the document is organized as follows. Section 2 summarizes the fundamentals of hierarchical classification, the standard evaluation measures, CNNs, and Bayesian networks; and presents the proposed classifier. Section 3 introduces the galaxies dataset and shows the experiments and results. Finally, in section 4, conclusions and some ideas for future work are given.

# 2 Methodology 

### 2.1 Fundamentals

In hierarchical classification, there are several labels to which an instance can be associated. However, the labels are arranged in a predefined structure, a hierarchy, which commonly is a tree but, in its general form, is a directed acyclic graph. The hierarchy, $H$, can be denoted with graph notation: $H=(L, E)$, where $L$ is the set of labels or nodes and $E$ is the set of edges that links the nodes. Furthermore, the labels associated with an instance must comply with the hierarchical constraint, which states if an instance is related to a node, the instance must be associated with all the ancestors of that node given by the hierarchy. Therefore, a set of labels that do comply with the hierarchical constraint is called consistent path or consistent prediction.

Even though there are several hierarchical problems (Silla and Freitas, 2011), in this work, the problem of interest is described as a hierarchy of tree type, where the instances are associated with a single path of labels (SPL) that always reach a leaf node, that is, full depth (FD); <Tree, SPL, FD> following Silla and Freitas (2011) notation.

Therefore, the problem of hierarchical classification consists in assigning to a particular object described by $d$ attributes, a subset of labels that comply with the hierarchical constraint: $f_{H C}=\mathbb{R}^{d} \rightarrow\{0,1\}^{|L|}$.

One key element in this work is the use of Bayesian networks to represent the hierarchy. Bayesian networks are directed graphical models representing the joint distributions of a set of random variables (Sucar, 2021). In a Bayesian network, nodes represent the random variables, while arcs represent direct dependencies among the nodes. In other words, the graph structure encodes a set of independent relations among variables.

Let the Bayesian network $G$ be a directed acyclic graph composed by the random variables $X_{1}, \ldots, X_{n}$, let $P a\left(X_{i}\right)$ be the set of parents of $X_{i}$ in $G$. Then it is said that a distribution $P$ factorizes according to $G$ if $P$ can be expressed as a product:

$$
P\left(X_{1}, \ldots, X_{n}\right)=\prod_{i=1}^{n} P\left(X_{i} \mid P a\left(X_{i}\right)\right)
$$

Equation 1 is derived from the chain rule and the conditional independence relations represented in the Bayesian network. The individual factors, $P\left(X_{i} \mid P a\left(X_{i}\right)\right)$, are called conditional probabilities distributions, which are commonly estimated from data.

In a Bayesian network, specific evidence may be available; the values for a subset of variables are known, then the posterior probability of the other (unknown) variables can be inferred. This is achieved by propagating the available evidence; several algorithms have been proposed for this purpose, such as probability propagation, variable elimination, junction tree, etc. The interested reader will find the description of those algorithms in Sucar (2021) Chapter 7.

On the other hand, CNNs are a type of feed forward neural network that can extract features from data with convolutional structures (Li et al, 2022). CNNs comprise three main types of layers, so a CNN architecture is formed when these layers are stacked. The layers are briefly described next (Li et al, 2022; Haridas and JyothiR, 2019; Khan et al, 2020): convolutional layers which are composed by convolutional kernels that work by diving the image into small slices, which helps to extract features' motifs; pooling layers which have the purpose of decreasing the complexity of the CNNs, neurons in these layers do not have weights or biases that will be learned in the training process, instead, they perform some fixed function; and fully connected layers, they are commonly used at the end of the network, which are used for classification or regression.

An example of a CNN model is AlexNet (Krizhevsky et al, 2012) which was proposed to predict 1000 different classes from the ImageNet LSVRC-2010 contest. AlexNet is composed of five convolutional layers, some of them are followed by pooling layers, and three fully connected layers; AlexNet's architecture is depicted in Fig. 2.

In this work, pre-trained CNN models are used because they have several advantages over training one from scratch: (i) pre-trained CNNs have already been trained on large data sets, meaning they have learned feature-rich representations for a wide range of images; (ii) less training data required, this is especially useful when few training data is available for the new task, that is, learning is usually faster and easier than starting from scratch with randomly initialized weights; (iii) less computational resources, because training a network from scratch can be computationally expensive and time consuming, especially if powerful hardware is not available.

# 2.2 Evaluation measures 

In this work, three evaluation measures are considered. First, exact match (RamírezCorona et al, 2016; Serrano-Pérez and Sucar, 2019) is the most strict evaluation

![img-1.jpeg](img-1.jpeg)

Fig. 2 AlexNet architecture(Krizhevsky et al, 2012), which is composed of multiple layers (convolutional, pooling and fully connected).
measure because the prediction must equal the real label set. However, in hierarchical classification, the predictions may be partially correct; in this way, accuracy and hierarchical F-measure (Silla and Freitas, 2011) give a score (greater than zero) if the prediction is partially correct. Let $N$ be the number of instances in the test set, $Y$ be the real subset of classes an instance is associated with, and let $\hat{Y}$ be the subset of predicted classes. The evaluation measures are described next:

- Exact Match (EM): Percentage of instances classified correctly.

$$
E M=\frac{1}{N} \sum_{i=1}^{N} 1_{Y=\hat{Y}}
$$

- Hierarchical Accuracy (H. Accuracy): Ratio of classes predicted correctly to the union of the real and predicted classes for each instance.

$$
\text { H.Accuracy }=\frac{1}{N} \sum_{i=1}^{N} \frac{\left|Y_{i} \cap \hat{Y}_{i}\right|}{\left|Y_{i} \cup \hat{Y}_{i}\right|}
$$

- Hierarchical F-measure (hF): F-measure for hierarchical classification.

$$
\begin{gathered}
h F=\frac{2 * h P * h R}{h P+h R} \\
h P=\frac{\sum_{i=1}^{N}\left|Y_{i} \cap \widehat{Y}_{i}\right|}{\sum_{i=1}^{N}\left|\widehat{Y}_{i}\right|} \\
h R=\frac{\sum_{i=1}^{N}\left|Y_{i} \cap \widehat{Y}_{i}\right|}{\sum_{i=1}^{N}\left|Y_{i}\right|}
\end{gathered}
$$

Where $h P$ and $h R$ are the hierarchical precision and recall, respectively.

# 2.3 Bayesian and Convolutional Neural Networks 

![img-2.jpeg](img-2.jpeg)

Fig. 3 A hierarchy (left) is transformed into a Bayesian network (right).

First of all, the hierarchy is transformed into a Bayesian network (Serrano-Pérez and Sucar, 2019), see Fig. 3. The Bayesian network comprises two types of random nodes, $y$ and $q$. First, $y$ nodes represent the data distribution and maintain the hierarchical constraint in the Bayesian network; hence, for each node of the hierarchy, there is a $y_{i}$ node in the Bayesian network. The parameters for each node $y_{i}, P\left(y_{i} \mid p a\left(y_{i}\right)\right)$, can be estimated by maximum likelihood from the training set as shown in Table 1, where $p a\left(y_{i}\right)$ is the parent of $y_{i}$ given by the hierarchy. As it can be seen, if an instance is not associated with $p a\left(y_{i}\right)$, then it will be no associated to $y_{i}$ with probability one, $P\left(y_{i}=0 \mid p a\left(y_{i}\right)=0\right)=1$, this is what maintains the hierarchical constraint in the Bayesian network.

Second, each $y_{i}$ node has a child node, $q_{i}$, in the Bayesian network, except the root node. $q$ nodes represent the base classifier output distribution to be expected on instances that were not used as training; that is, $q$ nodes model the behavior of the base classifier for predicting correctly and incorrectly instances. Furthermore, $q$ nodes will receive the predictions of the base classifier, which will be propagated in the Bayesian network.

Taking into account that the base classifier predicts the probability of being associated with the $i$-th node, the distribution for each node $q_{i}, P\left(q_{i} \mid y_{i}\right)$, can be modeled parametrically with Gaussian distributions (Barutçuoglu et al, 2008). That is,

Table 1 Conditional probability table of $P\left(y_{i} \mid p a\left(y_{i}\right)\right) . a$ is the number of instances associated to both $y_{i}$ and its parent, $p a\left(y_{i}\right) ; b$ is the number of instances no associated to $y_{i}$ but associated to its parent, $p a\left(y_{i}\right)$. Laplace smoothing is applied.


$P\left(q_{i} \in \mathbb{R} \mid y_{i}=0\right) \simeq N\left(\mu_{0}, \sigma_{0}^{2}\right)$ where $\mu_{0}$ is the mean and $\sigma_{0}^{2}$ is the variance of the predictions of the base classifier in the instances no associated to $y_{i}$ in the validation set; and the same for $P\left(q_{i} \in \mathbb{R} \mid y_{i}=1\right) \simeq N\left(\mu_{1}, \sigma_{1}^{2}\right)$ but considering the instances associated to $y_{i}$ in the validation set.

In this work, the base classifier is a pretrained convolutional neural network. CNNs have the advantage that can be trained with raw images because they can automate the feature extraction process from the images (Li et al, 2022; Altenberger and Lenz, 2018). The CNN in the proposed model is joined with a dense layer (with sigmoid activation function), which has one output for each node of the hierarchy (except the root node) and serves as a classifier. In this way, the training can be carried out only in this last layer; however, the whole CNN can be retrained, too. Later, the predictions of the CNN are used to feed the Bayesian network through the $q$ nodes, as shown in Fig. 4.

Finally, the prediction for new instances is obtained from the $y$ nodes and the posterior probabilities. Finally, the top-down (TD) procedure is used to get only one path of labels. TD starts at the root node and advances toward the child node with
![img-3.jpeg](img-3.jpeg)

Fig. 4 Model of the proposed classifier. It comprises two main modules: a CNN that feeds a Bayesian network. The CNN classifier is fed directly with the images, which outputs the probability for each class (in this example, four classes, $q_{1 . .4}$ ). These probabilities are sent to the Bayesian network that optimizes the classification via probabilistic inference. In this simple example, the hierarchy consists of 4 classes, where $y_{1}$ and $y_{2}$ are sub-classes of the root, $R$; and $y_{3}$ and $y_{4}$ are sub-classes of $y_{1}$.

the most significant probability, and so on until a leaf node is reached; so this path is returned as the prediction of the model.

To sum up the proposed classifier:

- Training phase: The CNN is trained with the labeled images. Then, the parameters of the Bayesian network are estimated. $P\left(y_{i} \mid p a\left(y_{i}\right)\right)$ can be calculated from the training set, while $P\left(q_{i} \mid y_{i}\right)$ can be estimated from the predictions of the CNN in a validation set.
- Prediction phase: The images are fed to the CNN, the CNN's predictions are sent to the Bayesian network, and the evidence is propagated. Finally, the TD procedure is applied to the posterior probabilities of the $y$ nodes to get the image's final prediction (set of labels).


# 3 Experiments and Results 

The experiments evaluate the impact of several improvements over the basic CNN classifier, including (i) the incorporation of the hierarchical constraint with a Bayesian network, (ii) selection of the path of labels, (iii) data augmentation and (iv) fine-tuning of the CNN.

In the following experiments, gradient descent is used to train the CNN as the optimizer with a learning rate $=0.005$ and momentum $=0.9$. All the experiments were executed on a computer with CPU Threadripper 3970X, GPU RTX3090, and RAM 128 GB .

### 3.1 Datasets and Preprocessing

![img-4.jpeg](img-4.jpeg)

Fig. 5 Galaxy hierarchy considered in the experiments.

We employed a collection of galaxies ${ }^{1}$ sourced from the Principal Galaxies Catalog (PGC) and the APM Equatorial Catalogue of Galaxies. Both compilations provide

[^0]
[^0]:    ${ }^{1}$ The dataset is available at https://www.kaggle.com/datasets/jonsperez/ galaxies-dataset-for-hierarchical-classification

details regarding the morphological and numerical characteristics of each galaxy. Furthermore, we cross-verified the details of each galaxy against the most recent citations available for each of them. All the images were standardized to size $300 \times 300$ pixels and monochrome. The classes of galaxies are arranged in the hierarchy shown in Fig. 5. As it can be seen, the different classes and the hierarchy are based on the Hubble sequence (Hubble, 1926, 1927), that is, galaxies of classes $S a, S b, S c$ and $S d$ are grouped as Spiral galaxies; Elliptical, Lenticular and Spiral classes are grouped as Regular galaxies; and galaxies of classes Regular, Irregular and Others are grouped in the root node. Even though the Hubble sequence does not include the class Others, in this dataset the class Others contains astronomical objects such as nebulae and star clusters, which are objects that can be found in the dataset. Each image is associated with a single full path of labels (classes); the path starts in the root node and finishes in a leaf node. Table 2 presents the number of galaxies per class.

Table 2 Classes of galaxies and the number of images in training, test, and validation sets. *: Images associated with multiple classes are counted only once.


# 3.2 Base classifier 

As stated in the section 2.3, the base classifier is a pre-trained CNN; there are several CNNs freely available; some of the most popular are shown in Table 3. The accuracy in the ImageNet ${ }^{2}$ task is shown for all of them; as it can be seen, the best is EfficientNet V2. At the same time, the well-known Inception v3 is 10 points lower than the first. EfficientNet v2 is selected as the base classifier for the following experiments.

First, the CNN classifier was trained for 40 epochs over the galaxies training set (Table 2); the evolution of the losses, for training and validation sets, tend to decrease as expected. Nevertheless, the loss for validation set is reduced up to 0.35 on the first 20 epochs, then it is barely reduced. Therefore, to avoid overfitting of the classifier on the training data, the number of epochs was set to 30 in all the next experiments.

[^0]
[^0]:    ${ }^{2}$ ImageNet is an image database organized according to the WordNet hierarchy - https://www.image-net.org/

Table 3 Some popular convolutional neural networks. The top 1 accuracy (percentage) in the ImageNet task and the number of parameters of each one are shown.


# 3.3 Incorporation of the Bayesian network 

In this section, the experiment shows whether the inclusion of the Bayesian network helps to improve the classifier's performance. That is, the CNN will be trained without the Bayesian network while, on the other side, the CNN will be trained with the Bayesian network (BCNN); in order to obtain consistent paths, the TD procedure is applied to the output of both classifiers. Table 4 shows the results of this experiment; as it can be seen, making use of the Bayesian network helps to improve the performance of the CNN from $57 \%$ to $64 \%$ in exact match and $77 \%$ to $81 \%$ in hF.

Table 4 Results (percentage) of the classifier with and without the Bayesian network, BCNN and CNN, respectively.


### 3.4 Selection of the path of labels

As described in section 2.3, the TD procedure is used to obtain the classifier's predictions, that is, the path of labels (classes) to which an instance is associated. However, there are other ways to obtain paths of labels from the probabilities of the nodes, such as sum of probabilities (SP) (Hernandez et al, 2013) that consists of averaging the probabilities of the nodes that form a path (the path starts on the root node and finishes on a leaf node) and returns the path with the highest score; and score gainloose balance (scoreGLB) (Ramírez-Corona et al, 2016) which follows a similar idea than SP but gives weight to each node with respect to its level in the hierarchy, so that higher nodes in the hierarchy have greater weight than lower ones.

Hence, the experiment in this section shows which procedure is the best to obtain the path of labels in the proposed classifier. Table 5 shows the results of the BCNN classifier with different procedures to obtain the predictions of the instances; as seen, the TD procedure got the best performance in all the evaluation measures. We attribute this situation to the fact that SP and scoreGLB are based on the idea that nodes may have a higher probability than their parents/ancestors, which would be beneficial when scoring the paths; however, this case does not occur in the BCNN classifier, because the Bayesian network always keeps the probabilities of the nodes with lower

Table 5 Results (percentage) of the BCNN classifier with different procedures to obtain the path of labels (in bold the best).


probabilities than their parents. Thus, the TD procedure is the best choice in the proposed classifier.

# 3.5 Image augmentation 

The galaxy dataset is unbalanced; that is, some classes have more images associated than others; for instance, classes $S d$ and others have 40 and 32 images associated, respectively, while the elliptical class has associated 301 images. This makes a difference up to $\sim 10$ times, considering only the training set and the leaf nodes.

Hence, the following experiment generates artificial images for the classes with few images associated to improve the classifier's general performance. Details of how images are generated are shown in Appendix A. Table 6 shows the results of the BCNN classifier trained with and without image augmentation; as it can be seen, the classifier does not improve its performance when using artificial images as extra data. However, when we combine fine-tuning with image augmentation, all evaluation measures improve, as shown in section 3.6 .

Table 6 Results (percentage) of BCNN classifier with and without image augmentation.


### 3.6 Fine-Tuning

Up to this point, the training of the CNN consisted only of training its last layer, a dense layer with one output for each node of the hierarchy. Therefore, the rest of CNN's layers were only used as feature extractors from the images; but if all its layers are retrained (fine-tuned) with the available images, will the classifier's performance improve?

In this experiment, all the layers of the CNN are retrained. Table 7 shows the results of the BCNN classifier allowing or not retraining all the layers of the CNN. As can be seen, retraining the whole CNN helps to improve the classifier's performance in all the evaluation measures. Additionally, an experiment with both retraining all the CNN's layers and with image augmentation is carried out; the results are shown in the last row (Yes+ImgA); as can be seen, the combination of both gives the best results.

Table 7 Results (percentage) of BCNN classifier retraining or not all the CNN's layers. ImgA: plus image augmentation. (In bold the best.)


# 3.7 Comparison of BCNN against CNN models 

This section compares the proposed classifier against Deep Galaxy 2 (Khalifa et al, 2018) and different CNN models. In the same way as BCNN, all of them were joined with a dense layer with one output per class and sigmoid activation functions; also, the models were optimized with the Gradient descent (with momentum) optimizer and binary cross-entropy as the loss. Additionally, in order to obtain consistent predictions from all CNN models, the TD procedure is applied to their predictions.

Table 8 shows the results of the proposed classifier, BCNN, and the different models. BCNN outperforms the rest of the classifiers in all the evaluation measures. Furthermore, when BCNN is trained with image augmentation and fine-tuning the performance increased from $64 \%$ to $67 \%$ in exact match and $81 \%$ to $83 \%$ in hF.

Table 8 Results (percentage) of the BCNN classifier compared with several CNN models. ImgA: plus image augmentation; FN: plus fine-tuning. (In bold the best.)


### 3.8 Discussion

From the experiments, we can conclude that all the elements - Bayesian network hierarchical classifier, data augmentation, and fine-tuning- contribute to improve the performance of the basic CNN classifier in all measures. There is an approx. 10 point improvement on exact match and 7 points for the hierarchical F-measure over the baseline. Of the different elements, the Bayesian network provides the most significant impact on performance, $\sim 7$ points (from $57 \%$ to $64 \%$ ) in exact match and $\sim 3$ points $(77 \%$ to $81 \%$ ) in hF.

# 4 Conclusions and Future Work 

Morphological galaxy classification is still a challenging problem. In this work, we proposed a novel approach, Bayesian and Convolutional Neural Networks, for morphological galaxy classification. This method combines a convolutional neural network trained with different classes of galaxies and a Bayesian network that represents the hierarchy of each type analyzed by CNN. The BN helps to improve the performance by enforcing the hierarchical constraint via probabilistic inference. Further improvements are obtained by image augmentation and fine-tuning the CNN.

The proposed approach was evaluated on images collected from different repositories considering ten classes of galaxies. The experiments show that all the BCNN components help the model improve its performance. Furthermore, BCNN got the best performance when compared to other CNN models.

In future work, a semi-supervised approach could be carried out to incorporate unlabeled images of galaxies.

Supplementary information. Not applicable.
Acknowledgments. J. Serrano-Pérez acknowledges the support from CONAHCYT scholarship number (CVU) 84075 .

## Declarations

- Funding: J. Serrano-Pérez was supported by CONAHCYT scholarship number (CVU) 84075 .
- Conflict of interest/Competing interests: The authors declare that they have no known competing financial interest, conflict of interest, or otherwise.
- Ethics approval: Not applicable.
- Consent to participate: Not applicable.
- Consent for publication: Not applicable.
- Availability of data and materials: The dataset is made available to the scientific community: https://www.kaggle.com/datasets/jonsperez/ galaxies-dataset-for-hierarchical-classification
- Code availability: The code is available at: https://github.com/jona2510/BCNN
- Authors' contributions (CRediT): Jonathan Serrano-Pérez: Conceptualization, Software, Validation, Formal analysis, Writing-Original Draft, Writing-Review \& Editing. Raquel Díaz Hernández: Conceptualization, Formal analysis, WritingOriginal Draft, Writing-Review \& Editing. L. Enrique Sucar: Conceptualization, Formal analysis, Resources, Writing-Original Draft, Writing-Review \& Editing, Supervision.


## Appendix A Image augmentation

Data augmentation is carried out to balance the leaf nodes. It consists of applying some operations to the available images, such as flip, scale, rotation, etc., to obtain different images. The detailed procedure is described next.

First, let $L M A X$ be the number of associated instances to the leaf node with the most significant number of related instances. Then, for each $l$ leaf node with $m_{l}$ instances associated: generate $n$ images so that $n+m_{l}=L M A X * 0.95$; the $n$ generated images will be associated to $l$ and all its ancestors given by the hierarchy. Image generation follows the next pipeline (iterating over the images associated with the $l$ node):

1. Flip (either horizontal or vertical) with a probability of 0.5 .
2. Shift both x and y axis in the range $[-10,10]$ (percent) with probability one.
3. Scale in the range $[-30,30]$ (percent) with probability one.
4. Rotate in the range $[0,360]$ (degrees) with probability one.
5. To fill the voids that may appear in the images due to the different transformation, the strategy border reflect ${ }^{3}$ is used to fill those pixels.
6. Resize to 300x300 pixels.

An example is shown in Fig. A1. Two images are generated from the image on the left.
![img-5.jpeg](img-5.jpeg)

Fig. A1 example of generation of artificial images. The image on the left is the available one; the two on the left are generated images after applying some operations to the image on the left.
