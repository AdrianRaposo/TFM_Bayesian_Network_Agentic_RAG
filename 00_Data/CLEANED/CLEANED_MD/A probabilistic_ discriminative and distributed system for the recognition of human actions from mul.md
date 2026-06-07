This document is published in:

Neurocomputing, (2012), 75 (1), 78-87.
DOI: http://dx.doi.org/10.1016/j.neucom.2011.03.051
(c) 2011 Elsevier B.V.

# A probabilistic, discriminative and distributed system for the recognition of human actions from multiple views 

Rodrigo Cilla, Miguel A. Patricio, Antonio Berlanga, Jose ${ }^{\text {M }}$ M. Molina<br>Computer Science Department, Universidad Carlos III de Madrid, 28270 Colmenarejo, Madrid, Spain<br>E-mail addresses: rcilla@inf.uc3m.es (R. Cilla), mpatrici@inf.uc3m.es (M.A. Patricio), aberlan@ia.uc3m.es (A. Berlanga), molina@ia.uc3m.es (J.M. Molina).


#### Abstract

This paper presents a distributed system for the recognition of human actions using views of the scene grabbed by different cameras. 2D frame descriptors are extracted for each available view to capture the variability in human motion. These descriptors are projected into a lower dimensional space and fed into a probabilistic classifier to output a posterior distribution of the action performed according to the descriptor computed at each camera. Classifier fusion algorithms are then used to merge the posterior distributions into a single distribution. The generated single posterior distribution is fed into a sequence classifier to make the final decision on the performed activity. The system can instantiate different algorithms for the different tasks, as the interfaces between modules are clearly defined. Results on the classification of the actions in the IXMAS dataset are reported. The accuracy of the proposed system is similar to state-of-the-art 3D methods, even though it uses only well-known 2D pattern recognition techniques and does not need to project the data into a 3D space or require camera calibration parameters.


Keywords: Human action recognition, Bayesian networks, Computer vision, Machine learning

## 1. Introduction

Attaching a semantic meaning to human actions occurring in video streams is useful in different situations. Detecting a crowd running away of a building can be a sign of something having gone wrong inside. An elderly person detected lying on the floor in a room suggests that he may have suffered an accident and needs attention. In both cases, an alarm can be automatically raised to the emergency services to require their presence. Beyond surveillance, human actions can be used to interact with automated systems. Playing video games using realistic body gestures or automatically adjusting the lighting of a room when somebody is detected reading are just a couple of such interactions.

The wide variety of applications of human action recognition has brought the field into the focus of computer vision researchers for the past two decades. Recently published surveys in the area give an idea of the progress made over this time [1-3]. There has been an evolution from the single view systems used in the early days [4-6] to the multiple view setups currently being deployed [7-10]. Multiple view systems have exploited multiple view geometry to overcome the main weaknesses of the single view systems: robustness to occlusions and viewpoint invariance.

Most existing multi-view human action recognition systems have followed a similar scheme. First, some low level image processing is done to the images grabbed at each view to extract 2D
features such as a silhouette [7] or body limb segmentation [11] of the monitored human being. These features are then projected into a common scene model to generate a 3D human representation, such as visual hulls [7] or body limb configurations [11].

While these approaches have shown high accuracy in human action recognition tasks, they suffer from some drawbacks [9,12]:

1. Need for camera calibration: The usual human action recognition procedure is to project the perceived views into a common representation of the scene. Camera calibration parameters are necessary in order to project the recovered 2D features into a 3D scene model [13]. These requirements are an obstacle to system deployment, because calibration parameters have to be recovered every time a new camera is added or its position changes (maybe accidentally), which is taxing.
2. Centralized processing: It is common practice in existing approaches to send the features detected at the camera nodes to a central server, where the action recognition is performed in a common scene model. The server usually accounts for most of the computational requirements of the system, its performance degrades as the number of cameras increases. To make the system scalable, the amount of resources that have to be allocated to the central server when a new camera is added should be minimized or, at least, bounded. The projection and

matching of the 2D features in the 3D scene model is one of the most load-demanding tasks to be performed. A possible way to avoid this is to embed part of the action classification into the cameras, using 2D pattern recognition to make a classification of the action for the view. The different view classifications are then combined using lightweight algorithms to create a single representation of what is going on in the scene.

Another reason for avoiding centralized processing is fault tolerance. In a centralized processing scheme, the action recognition process will not work if the central node breaks. The use of a distributed processing scheme affords fault tolerance, as the different action recognition steps are performed by different nodes.

3. *Bandwidth requirements*: As noted earlier, the camera nodes need to send the computed features to a central server. The amount of information that has to be sent is correlated with how much processing is done at each camera. The bandwidth requirements for sending the acquired raw pixels are greater than for just sending the extracted foreground, which again requires more bandwidth than sending segmented body part locations or just trajectory information. In order to prevent the saturation of communication channels when new cameras are added to the system, it is important to reduce the amount of information exchanged by the nodes, while retaining the utmost informativeness about what is going on. Posterior probabilities may be a compact way of reducing the transmitted information without so much loss.

Hybrid Artificial Intelligence systems [14–16] combine different kinds of techniques to efficiently solve a wide variety of real world problems. In this paper we propose a system for the classification of human actions perceived from multiple viewpoints without performing any explicit 3D reconstruction, exploiting the synergies between probabilistic reasoning and image understanding. 2D features characterizing human motion are extracted for each view of the scene. The features are introduced into a probabilistic classifier to create a posterior distribution on the performed action. A central server gathers the posterior distributions for all the views and combines them into a single posterior for the action. Finally, a dynamic Bayesian network (DBN) is used to model the uncertainty of the temporal evolution of the single frame posteriors. This DBN is used to classify the test action sequences entered into the system. To test the performance of the proposed system, it will be trained using action sequences grabbed from different synchronized views of the scene. Then, new action sequences are presented to the system and the ratio of correctly classified sequences is taken as the quality measure. With the proposed approach, we are able to outdo some of the drawbacks of other distributed multi-camera human action recognition systems [12,17,18], that assume a constant number of cameras in the system or do not handle the uncertainty in the classification in a proper way.

This paper is an extended version of the work presented in [8]. The fusion algorithms presented there are now described in the context of an architecture for the distributed recognition of human actions, and a more extensive validation of them is provided.

### 1.1. Contributions

The main contributions of this paper is a hierarchical discriminative system for the recognition of human actions from multiple cameras. Different feature descriptors, classifiers, classifier fusion algorithms and sequence models can be instantiated for the different system levels, choosing the most appropriate one for the action recognition task to be performed. The proposed system achieves an accuracy similar to state-of-the-art 3D methods when applied to the IXMAS dataset classification, using only standard pattern recognition techniques applied at each of the available views and combining the results of the local classifications.

### 1.2. Paper organization

The paper is organized as follows. Section 2 illustrates the components of the proposed system. In Section 3, the methods used to process the images grabbed from each camera are introduced. In Section 4, the algorithms used to combine the results of the local processing are presented. Section 5 describes the sequence classification algorithm used in the system. In Section 6, the system is tested on the IXMAS dataset, and the results are shown and discussed. In Section 7, the state of the art on view-invariant action recognition is reviewed. Finally, Section 8 presents the conclusions of this research.

## 2. System overview

Fig. 1 illustrates the proposed multi-camera action recognition architecture. *C* different cameras observe a scene from different viewpoints. It is assumed that there is only a single individual in the scene. This way, we can ignore data for tracking association problems. Without loss of generality, it is also assumed that all *C* cameras always have a perception of the individual in the scene, although the number of cameras observing the individual may be different at every instant *t*. This should simplify ongoing formulations. The goal of the system is to select the action *α* performed by the individual from a set of *N* predefined actions *A* = (*a*<sub>1</sub>, . . . , *a*<sub>*N*</sub>) known a priori given a set of image sequences (*I*(*x*, *y*, *t*)<sup>*T*</sup>), 1 ≤ *t* ≤ *T*, 1 ≤ *c* ≤ *C*, of length *T* simultaneously acquired by the *C* cameras observing the scene.

![img-0.jpeg](img-0.jpeg)

**Fig. 1.** Overview of the proposed system.

The first step in order to make this decision is to compute an action descriptor *f*<sup>*T*</sup><sub>*i*</sub> ∈ *X* from the data grabbed from each view *c*. *X* is the inner product space where the descriptor is defined and typically *X* = *X*<sup>*i*</sup><sub>*i*</sub>, although other choices are also possible, for example when using histogram descriptors [19]. *f*<sup>*T*</sup><sub>*i*</sub> must capture

enough variability in the data to be able to differentiate the actions in *A*. Another desirable property is that *X* should be compact in order to overcome the problems caused by the *curse of dimensionality*. Manifold learning techniques can be employed to project the original descriptors into a more compact subspace, if necessary.

Once an action descriptor *f<sup>t</sup>* has been obtained, a probabilistic classifier is used to create a posterior probability distribution on the performed action given the observed descriptor, *p(a<sub>i</sub> | f<sub>i</sub><sup>t</sup>), a<sub>i</sub> ∈ A, ∑<sub>i=1</sub><sup>N</sup> p(a<sub>i</sub> | f<sub>i</sub><sup>t</sup>) = 1. This posterior probability distribution measures the uncertainty of the observed descriptors of being an instance of each one of the categories.

The posterior probability distributions computed for each one of the *C* views of the scene are combined using a classifier fusion algorithm, generating a posterior distribution *p(x<sub>i</sub> | f<sub>i</sub><sup>t</sup>, ..., f<sub>i</sub><sup>C</sup>)* on the action performed given the descriptor computed by the different views.

Finally, the posterior probability distributions created at each instant *t* are entered into a sequence classifier to generate a single posterior distribution on the performed action given the observation sequence *p(x | f<sub>i</sub><sup>t</sup>, ..., f<sub>i</sub><sup>C</sup>)*. This distribution will be finally used to predict the action of the observed individual.

This architecture distributes the decision making process across multiple nodes. Each node processes the image grabbed from each camera, and makes a partial decision on the action using the information contained just in that image. A central node then grabs the decisions taken by each node and combines them to make the final decision on the performed action. One advantage of this approach is that if a camera breaks the action recognition decision can still be made, as the central node would be still collecting the decisions made by the other nodes. Other advantage is that the computational resources needed to process the image sequences are allocated across different nodes, reducing the amount of resources needed at the central node.

A possible alternative way of structuring the system would be to first classify each sequence at each camera and then sending just one posterior distribution to the central node, as in [12]. However, we are interested in performing frame by frame action segmentation at the central node in the future, assuming different actions happen on the input sequences. If the system would be structured in such way it would be more difficult to make this extension.

### 3. Single view processing

#### 3.1. Human action representation

The first step in the proposed architecture is to compute a descriptor to capture the variability of the input images. Two different action descriptors will be tested in our system.

#### 3.1.1. Motion history image

The motion history image (MHI), introduced by Bobick and Davies [20], is an appearance descriptor that has been widely used for the recognition of human actions. It recursively accumulates the silhouettes of the moving person up to the current frame. It is used in the system as it is the best example of a descriptor incorporating temporal information while providing a framewise output. Let *D(x, y, t)* be a binary image representing the silhouette of the observed person at time *t*. A MHI ζ is recursively defined as

$$
\zeta(x, y, t) = \begin{cases}
255, & D(x, y, t) = 1, \\
\max(\zeta(x, y, t-1) - \rho, 0), & D(x, y, t) = 0,
\end{cases}
$$

where ρ is a parameter that adjusts the amount of time the presence of the silhouette in a given pixel is remembered. A higher value of ρ implies a shorter memory. The bounding box of the observed person in the MHI is tracked across frames, and resized to a 35 × 20 box. The resulting pixels are concatenated to generate a descriptor with *D<sub>MHI</sub>* = 700 dimensions. An example MHI image is shown on Fig. 2.

![img-1.jpeg](img-1.jpeg)

**Fig. 2.** Motion history image.

#### 3.1.2. Tran's descriptor

Tran et al. [21] proposed a frame descriptor combining optical flow and appearance. It is used in the system because it has shown a high experimental performance. The bounding box of a human being is normalized to a square box, from which human shape and optical flow are computed. Vertical and horizontal planes of the optical flow are split and blurred. A radial histogram is computed over each of the optical flow planes and the shape. The three histograms are concatenated into 216-d vector. Lastly, a principal component analysis (PCA) reduction of the surrounding past and future vectors is appended to finally generate a descriptor of *D<sub>TRAN</sub>* = 286 dimensions. Readers are referred to [21] for more details.

#### 3.2. Dimensionality reduction

The action descriptors just introduced have a large dimensionality (*D<sub>TRAN</sub>* = 286, *D<sub>MHI</sub>* = 700) and need to be projected into a lower dimensional space in order to prevent the problems derived from "the curse of dimensionality". There is a large corpus of dimensionality reduction techniques suitable for solving this problem (see [22] for a recent survey).

Dimensionality reduction techniques can be divided into two major subgroups: (1) unsupervised dimensionality reduction, whose objective is to project the data to a lower dimension where their variance is maximized and (2) supervised dimensionality reduction, also called discriminant analysis, whose objective is to project the data to a lower dimension where the separation between the different categories of the data is maximized.

As the purpose of this paper is to introduce a general system for the recognition of actions, only the simplest technique of each group will be tested. Principal component analysis (PCA) is the standard unsupervised dimensionality reduction technique and projects the

data points into a lower dimensional subspace where the variance of the training data is maximized. Linear discriminant analysis (LDA) finds projective directions by maximizing the ratio of between-class scatter to within-class scatter. Both methods have been used many times in image processing tasks, the most notable being face classification [23,24]. Readers are referred to any pattern recognition book, such as [25], for more details.

### 3.3. Action classification

The action descriptor $f_{t}^{c}$ computed at each frame will be introduced into a probabilistic classifier in order to generate the posterior probabilities of the performed action given the evidence grabbed at that instant. Examples of suitable classifiers are mixtures of Gaussians [26] or conditional random fields [27]. A support vector machine or a C4.5 tree would be invalid classifiers, as they do not provide a calibrated output suitable for conversion into a posterior probability.

We have chosen a parametric (k-means + naive Bayes) and a non-parametric (nearest neighbor conditional density estimator) density estimator to test our system. The parametric splits the feature space in different regions, estimating the conditional probabilities of each class at each region. The non-parametric estimates the conditional probabilities of each class according to the neighbourhood of a test point. This way the possibility of using a local or a global approach to classification is incorporated to the system.

### 3.3.1. Nearest neighbor conditional density estimator

The nearest neighbor conditional density estimator (kNN) [25] is a well-known non-parametric conditional density estimator. The estimator locally captures the conditional density around a given test point $x$. Let $K$ be a fixed neighborhood size and $K_{i}$, $\sum_{i} K_{i}=K$ the number of neighbors of class $a_{i}$
$p\left(x \mid a_{i}\right)=\frac{K_{i}}{K}$.

### 3.3.2. K-means + naive Bayes

The space of feature descriptors $f_{t}^{c}$ will be quantified using a codebook of size $K$. Each feature vector will be associated with its nearest center to obtain the word $w_{k}$. Codebook centers are computed using the k-means algorithm.
$p\left(w_{k} \mid a_{i}\right)=\frac{p\left(a_{i} \mid w_{k}\right) p\left(w_{k}\right)}{p\left(a_{i}\right)}$.

## 4. Action fusion

After extracting a set of posterior probability distributions $p\left(a_{i}^{c} \mid f_{t}^{c}\right)$ from the frame descriptor $f_{t}^{c}$ computed for each view, they have to be combined to generate a joint posterior probability distribution $p\left(\alpha_{t} \mid f_{t}^{1}, \ldots, f_{t}^{c}\right)$ representing the uncertainty in the classification with respect to the evidence perceived by the different cameras at an instant $t$.

Two different algorithms will be tested for this task. The first is a voting scheme. The second is a Bayesian network modeling the errors in local classifications.

### 4.1. Voting

The first algorithm that we tested for the fusion of single view soft classifications is defined as the product of the posterior probabilities:
$p\left(\alpha_{t} \mid f_{t}^{1}, \ldots, f_{t}^{c}\right) \propto \prod_{c=1}^{c} p\left(a_{c} \mid f_{t}^{c}\right)$.
![img-2.jpeg](img-2.jpeg)

Fig. 3. Plate model of the Bayesian network used to combine the outputs from the classifiers at each camera.

This algorithm is tested as baseline to measure the efficiency of the bayesian network.

### 4.2. Bayesian network

The second algorithm that we tested for the fusion of single view soft classifications is based on the Bayesian network shown in Fig. 3. The network is composed of observation nodes $f_{t}^{c}$, representing the observation at instant $t$ and camera $c$, a node $\alpha_{t}$ representing the activity at time $t$ and a set of latent nodes $a_{t}$ to model the single view classification.

Given a set of frame descriptors $\mathbf{f}_{t}=f_{t}^{1}, \ldots, f_{t}^{c}$, a set of latent variables $\mathbf{a}_{t}=a_{t}^{1}, \ldots, a_{t}^{c}$, and the activity label $\alpha_{t}$, their joint probability is factorized as
$P\left(\alpha_{t}, \mathbf{a}_{t}, \mathbf{f}_{t}\right)=P\left(\alpha_{t} \mid \mathbf{a}_{\mathbf{t}}\right) P\left(\mathbf{a}_{\mathbf{t}} \mid \mathbf{f}_{\mathbf{t}}\right) P\left(\mathbf{f}_{\mathbf{t}}\right)$.
The conditional probability given $\mathbf{f}_{\mathbf{t}}$ is then:
$P\left(\alpha_{t}, \mathbf{a}_{t} \mid \mathbf{f}_{t}\right)=\frac{P\left(\alpha_{t}, \mathbf{a}_{t}, \mathbf{f}_{t}\right)}{P\left(\mathbf{f}_{t}\right)}=P\left(\alpha_{t} \mid \mathbf{a}_{\mathbf{t}}\right) P\left(\mathbf{a}_{\mathbf{t}} \mid \mathbf{f}_{\mathbf{t}}\right)$.
The probability $P\left(\alpha_{t}, \mathbf{a}_{t}, \mathbf{f}_{t}\right)$ is defined as a product of independent factors, assuming hidden variables $a_{t}^{c}$ to be independent:
$P\left(\alpha_{t} \mid \mathbf{a}_{\mathbf{t}}\right) \propto \prod_{c=1}^{c} P\left(\alpha_{t} \mid a_{t}^{c}\right)$.
With this assumption we rule out modeling correlations between local classification errors. In this way, this assumption reduces to two the exponential number of probability distributions that would otherwise need to be estimated. Thus, Eq. (6) can be rewritten as
$P\left(\alpha_{t}, \mathbf{a}_{t} \mid \mathbf{f}_{t}\right)=\prod_{c=1}^{c} p\left(\alpha_{t} \mid a_{t}^{c}\right) p\left(a_{t}^{c} \mid f_{t}^{c}\right)$.
Marginalizing over $a_{t}^{c}$ :
$P\left(\alpha_{t} \mid \mathbf{f}_{t}\right)=\prod_{c=1}^{c} \sum_{a_{t}^{c}} p\left(\alpha_{t} \mid a_{t}^{c}\right) p\left(a_{t}^{c}\right) p\left(f_{t}^{c} \mid a_{t}^{c}\right)$.
Bayesian network parameters are estimated using labeled training samples. $p\left(a_{t}^{c} \mid f_{t}^{c}\right)$ is known, being provided by the single view soft classifiers, so only $p\left(x^{c} \mid a_{t}^{c}\right)$ needs to be estimated. Let $O^{c}=\left(o_{1}^{c}, \ldots, o_{k}^{c}\right)$ be the set of $K$ training frame descriptors computed at camera $c$ with their respective activity labels $Y^{c}=\left(y_{1}^{c}, \ldots, y_{K}^{c}\right), y_{k}^{c} \in A$. Model parameters are estimated as
$p\left(x^{t}=a_{i} \mid a_{i}^{c}=a_{j}\right)=\frac{\sum_{k=1}^{K} \gamma_{k} p\left(a_{i}^{c}=a_{j} \mid o_{k}^{c}\right)}{\sum_{l=1}^{K} \sum_{k=1}^{K} \gamma_{k} p\left(a_{i}^{c}=a_{l} \mid o_{k}^{c}\right)}$,
where $\gamma_{k}=1$ if $y_{k}=a_{j}$ and $\gamma_{k}=0$ otherwise.

## 5. Sequence classification

Human actions are not isolated occurrences, they happen in sequence. By this time, the reader will probably have noted the $t$ subscript in our formulation. The method proposed until now

![img-3.jpeg](img-3.jpeg)

**Fig. 4.** Dynamic Bayesian network for sequence classification.

considers individual frame descriptors, but ignores sequence dynamics. So, given a sequence of frame descriptors computed at each camera *F* = {*f*11*, . . . *f*12*, . . . *f*12*, . . . *f*12*}, we need to associate it with their respective activity *α*, assuming that there is only one activity performed in the sequence. The sequence length *T* is not needed to be the same for all sequences.

In this paper a discriminative Hidden Markov Model (HMM) [28] is employed for this task. The probability of a path of hidden node values *H* = *α*1, . . . , *α*T given an action class *α* and an observed sequence *F* is defined as

$$p(H|F, \alpha) = p(\alpha_1|\alpha)p(\alpha_1|f_1^1\dots f_T^1)\prod_{t=2}^T p(\alpha_t|\alpha_{t-1}, \alpha)p(\alpha_t|f_t^1\dots f_T^t),$$

where *p*(αt|αt-1,α) is a transition model for each action. This factorization of the probability distribution is graphically shown on Fig. 4. The action α* performed given a sequence of observed actions *F* is

$$\alpha^* = \arg\max\_{F} p(\alpha|F), \tag{12}$$

where *p*(α|*F*) is defined as

$$p(\alpha|F) \ge \sum\_{t} p(\alpha\_{t}|F, \alpha)p(\alpha). \tag{13}$$

The above quantity can be recursively estimated using the standard forward-backward procedure [28].

The parameters of the model, *p*(α1|α) and *p*(αt|αt-1,α), can be estimated from labeled training samples in a similar way as for the Bayesian network in Section 4.2. We assume a uniform prior on *p*(α).

### 6. Experiments

#### 6.1. Experimental setup

Experiments with different instantiations of the proposed system will be conducted using IXMAS: INRIA Xmas Motion Acquisition Sequences [7]. IXMAS is composed of 36 clips recorded by five different cameras in which 12 different actors perform 14 different activities at least three times each. Sample frames are shown in Fig. 5. Only the 11 activities tested in [7] will be used. The frame descriptor proposed by Tran et al. [21] has been downloaded from their web page. The MHI has been extracted from the dataset using a parameter of σ = 10. The code of our system is available online.

![img-4.jpeg](img-4.jpeg)

**Fig. 5.** The *kick* action in the IXMAS dataset from the five available views: (a) Camera 1, (b) Camera 2, (c) Camera 3, (d) Camera 4 and (e) Camera 5.

Two different evaluation protocols will be used to evaluate the system: Leave-One-Sequence-Out (LOSO-CV) Cross-Validation and Leave-One-Actor-Out Cross-Validation (LOAO-CV). LOSO-CV trains the system using all the clips in the dataset except one, that is used for validation. The process is repeated until all the clips have been used for validation once. LOAO-CV trains the system using the clips of all the actors except one, that is used for validation, and repeating the process until every actor in the system has been used for validation. LOAO-CV is a harder evaluation protocol than LOSO-CV, aiming to study how the system performance is expected to degrade when it observes an unknown actor.

PCA and LDA are used to project the frame descriptors into a lower dimensional subspace. In the case of PCA, it has been tested for *d* = {10, 15, 20, 25, 30, 35, 40, 45}.

The size of the codebook used in the BN classifier has been experimentally adjusted to *k* = 300 words. The k-NN density estimators will be tested using *k* = 3, *k* = 5 and *k* = 7 neighbors.

A different dimensionality reducer and classifier is trained for each camera in the system, with the images that they grabbed. Classifier fusion and sequence classifiers are then run on the results provided by these classifiers.

In order to compare the different system setups to be tested, we compute the accuracy in the classification as the performance criteria. The accuracy is defined as the ratio between the number of correctly classified samples with respect to the total number of samples presented to the system for validation.

### 6.2. Results

### 6.2.1. Single camera classification

Table 1 shows the accuracy of the single frame classifiers. Irrespective of the frame descriptors used, the results reported for cameras 1-4 are quite similar, whereas the accuracy drops by around $10 \%$ for camera 5 .

Classifiers trained using Tran's descriptor generally provide better results than those trained with the MHI descriptor. Additionally, the accuracy of Tran's descriptors increases with the dimensionality of the PCA projection, whereas it appears to reach saturation point and even decrease in the case of MHI descriptors. In the case of MHI descriptors, the LDA projection always results in worse accuracy than PCA, whereas accuracy is better when combined with the BN classifier in the case of Tran's descriptor.

Regarding the classification algorithms employed, k-NN algorithms are more accurate than the BN algorithm for almost all the choices of descriptor and projection algorithm. As regards the
choice of the number of neighbors to use, 7-NN was found to return better results than 3-NN and 5-NN, but the difference is not substantial.

### 6.2.2. Classifier fusion

Table 2 shows the accuracies achieved after applying the classifier fusion algorithms to the posterior distribution generated from each camera. We find that whereas the voting whereas the algorithm always improves the accuracy of the BN classifiers at least a little, this is not the case for the k-NN classifiers, where the final accuracy is always worse than for the best single view classifier. However, the accuracy provided by the BN algorithm is always better than the best single view classifier by about 10-20\%.

### 6.2.3. Sequence classification

Finally, the results for sequence classification are shown in Table 3. The accuracy improvement is notable when compared with frame-by-frame classification.

Table 1
Results obtained after single camera classification of the DXMAS dataset.


Table 2 Accuracy obtained after applying classifier fusion algorithms to the IXMAS dataset.


Table 3 Accuracy obtained after applying sequence classification algorithm to the IXMAS dataset.


The behavior of the sequence classification algorithm depends on the origin of the instant classification posteriors that it combines. When using the output from the BN classifier fusion algorithm, the result varies slightly with respect to the number of dimensions used in the frame descriptor for any given classifier. In the case of k-NN classifiers some overfitting can be observed, as the final accuracy starts to drop as the dimensionality grows. When using the voting algorithm, the variation of the results is greater. While the behavior is similar to BN's when applied to Tran's descriptor, the result quickly overfits when applied to the MHI descriptor and drops with the dimensionality.

### 6.3. Discussion

The results reported in Section 6.2 show that Tran's descriptor is better than the MHI descriptor at the task of recognizing the actions included in the IXMAS dataset. A possible explanation is that Tran's descriptor includes appearance and local motion cues, whereas MHI is based on appearance only. The use of different cues improves the variability of the descriptor, better capturing the variance of the action. Note that classifiers using MHI descriptor start to overfit earlier than classifiers using Tran's descriptor when the dimensionality increases. This again suggests that the content of the Tran's descriptor is richer than the content of MHI descriptor: the latter can be compressed to a smaller number of dimensions than the former.

Another remarkable result is that the use of label information for dimensionality reduction does not improve the results in most cases, or at least not significantly. This might be due to the fact that LDA assumes that each class is unimodal and can be approximated by a Gaussian distribution, whereas the data actually used probably do not fit that assumption.

Table 4 Comparison of the accuracy of the proposed method to other works evaluated with IXMAS dataset.


The BN classifier fusion algorithm has been proved to outperform the voting algorithm. The reason is that the BN attaches different weights to the posteriors produced by each camera, according to a model of the usual errors in the classification, whereas the voting algorithm does not use any prior information about classification accuracy.

The results for sequence classification, when compared to instant classification, show that actions are not isolated occurrences, but happen in sequence. It is not enough to consider just one instant in order to recognize actions, and, whenever already available, the past and the future frames have to be employed to make the decision about what is happening or happened.

When globally examining the results, there is one discouraging observation: the best algorithm configuration found for one tier of the system does not guarantee that the best accuracy will be achieved on the next tier up. We observed many times that the accuracy given after the classifier fusion by the classifiers with the best single frame performance is smaller than the reported for other classifiers with a worse performance at the single frame level. There are also similar examples of these phenomena involving the classifier fusion and sequence classification results. This implies that action recognition systems cannot be constructed incrementally in order to find the best configuration, as the configuration with the best result at the highest level is not the configuration with the best result at intermediate levels.

Finally, the accuracy of the proposed system is compared to other proposals reporting results on the IXMAS dataset. Table 4 compares the proposed system to other alternatives. All algorithms are deterministic for stored images. To the best of our knowledge, the proposed system achieves an accuracy similar to the best reported to date [29]. Let us stress that while the best result was based on the classifications of the 3D visual hull, this proposal relies on only wellknown simple 2D pattern recognition techniques, without any need of recovering camera calibration parameters.

## 7. Related work

The research considering how to achieve view-invariant action recognition can be divided into two separate groups: (1) methods proposing action representations that are invariant to camera view and (2) methods combining the perceptions from multiple cameras to take a view-independent decision.

### 7.1. View-invariant features

The problem of viewpoint action recognition has been studied from the geometrical perspective. Rao et al. [30] introduce a 2D view- invariant descriptor for 3D point trajectories projected in the affine plane. They search the spatio-temporal trajectory curvature to find instants of change. Parameswaran and Chellappa [31] present 2D and 3D invariants for body pose configurations. Gritai et al. [32] propose a metric to compare the trajectories of body parts under anthropometric, temporal and viewpoint transforms. Sheikh et al. [33] approximate the variability in action data as a linear combination of different action bases in spatiotemporal space. The main drawback of these approaches is that they assume that an accurate 3D tracking of the body parts is available, and this is very difficult to achieve in a real scenario.

Other authors have relied on machine learning techniques to create view- invariant action models using only 2D features. Martinez-Contreras et al. [34] project motion history images (MHI) [20] into a subspace that groups viewpoint and movement in a principal manifold using Kohonen self-organizing feature maps. The winner neuron is used to classify the action being performed using HMM smoothing. Tran et al. [21] proposed another approach to achieve view invariance, where view-invariant models are learned using non-parametric classification from a frame descriptor extracted from multiple views including appearance and local motion information. The main weakness of these approaches is the use of only a single view to predict new actions, as different categories may appear similar if they are not observed from the appropriate viewpoint.

### 7.2. Multi-view systems

Traditionally, multi-view systems have projected the silhouettes obtained from the different views into 3D to create a visual hull [35] of the observed human being. Then, different action descriptors can be extracted from the visual hull. Weinland et al. [7] extended MHI to 3D, introducing motion history volume (MHV). Peng et al. [29] perform a multi-linear analysis of the visual hull to create a descriptor of reduced dimensionality that is introduced in a HMM. These approaches achieve good recognition performance, but visual hull computation requires camera calibration and a lot of centralized processing.

A number of ideas have been proposed to avoid visual hull computation. Srivastava et al. [12] compute a histogram over quantized spatio-temporal salient points [36] for each view. They are then concatenated, and a k-NN classifier is used to decide the performed action. Wu et al. [17] and Määttä et al. [18] propose different ways to combine 2D descriptors computed from different views, but their proposals either assume that there is a constant number of cameras observing the view or use the data coming from the best one only. Our approach improves their proposals as uncertainty is propagated to the upper levels every time that they are classified, taking into account the observations from all the cameras.

## 8. Conclusions

This paper has presented a distributed human action recognition system. 2D descriptors have been extracted for the frames captured at each one of the available views. They have been projected into a lower dimensional space and introduced into a probabilistic classifier to generate a posterior probability of the performed action. The posteriors for the different cameras have been merged using a classifier fusion algorithm, whose results have been fed into a sequence classifier to make the final decision on the performed action. The system has been tested with different algorithms, exploiting the flexibility provided by the well-defined interfaces between levels. As result, the system achieves an accuracy similar to the state-of-the-art of human action recognition algorithms for classifying the IXMAS dataset.

In the future, we intend to explore the possibility of exploiting the well-defined interfaces between the system levels to include other types of sensors, such as time-of-flight cameras [37] or motion capture devices [38], in order to improve the accuracy of the recognition process. Implementing these ideas with a

multi-agent system, such as the one proposed by Castanedo et al., would be another challenging task [39]. Other future line would be to test in the system more advanced methods. Authors are specially interested in exploring the dimensionality reduction literature to find appropriate methods to reduce the high dimensionality of the action descriptors.

## Acknowledgments

Authors acknowledge the valuable feedback given by the anonymous reviewers.

This work was supported in part by Projects CICYT TIN2008-06742-C02-02/TSI, CICYT TEC2008-06732-C02-02/TEC, CAM CONTEXTS (S2009/TIC-1485) and DPS2008-07029-C02-02.
