# Article 

## Bayesian Feature Fusion Using Factor Graph in Reduced Normal Form

Amedeo Buonanno ${ }^{1, * *}$, Antonio Nogarotto ${ }^{2}$, Giuseppe Cacace ${ }^{2}$, Giovanni Di Gennaro ${ }^{2 * *}$, Francesco A. N. Palmieri ${ }^{2,3}$, Maria Valenti ${ }^{1}$ and Giorgio Graditi ${ }^{4}$

## check for updates

Citation: Buonanno, A.; Nogarotto, A.; Cacace, G.; Di Gennaro, G.; Palmieri, F.A.N.; Valenti, M.; Graditi, G. Bayesian Feature Fusion using Factor Graph in Reduced Normal Form. Appl. Sci. 2021, 11, 1934. https://doi.org/10.3390/app11041934

Academic Editor: Alessandra Biancolillo
Received: 8 December 2020
Accepted: 17 February 2021
Published: 22 February 2021
Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## (0)

Copyright: (C) 2021 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 Department of Energy Technologies and Renewable Energy Sources, Research Centre of Portici, ENEA, 80055 Portici, Italy; maria.valenti@enea.it
2 Dipartimento di Ingegneria, Università degli Studi della Campania "Luigi Vanvitelli", Via Roma, 81031 Aversa, Italy; antonio.nogarotto2@studenti.unicampania.it (A.N.); giuseppe.cacace2@studenti.unicampania.it (G.C.); giovanni.digennaro@unicampania.it (G.D.G.); francesco.palmieri@unicampania.it (F.A.N.P.)
3 CNIT-Consorzio Nazionale Interuniversitario per le Telecomunicazioni, Complesso Universitario di Monte S. Angelo, Edificio Centri Comuni, Via Cintia, 80126 Naples, Italy
4 Department of Energy Technologies and Renewable Energy Sources, Research Centre of Casaccia, ENEA, Via Anguillarese, S. Maria di Galeria, 00123 Rome, Italy; giorgio.graditi@enea.it

* Correspondence: amedeo.buonanno@enea.it


#### Abstract

In this work, we investigate an Information Fusion architecture based on a Factor Graph in Reduced Normal Form. This paradigm permits to describe the fusion in a completely probabilistic framework and the information related to the different features are represented as messages that flow in a probabilistic network. In this way we build a sort of context for observed features conferring to the solution a great flexibility for managing different type of features with wrong and missing values as required by many real applications. Moreover, modifying opportunely the messages that flow into the network, we obtain an effective way to condition the inference based on the different reliability of each information source or in presence of single unreliable signal. The proposed architecture has been used to fuse different detectors for an identity document classification task but its flexibility, extendibility and robustness make it suitable to many real scenarios where the signal can be wrongly received or completely missing.


Keywords: Data Fusion; bayesian networks; belief propagation; factor graph

## 1. Introduction

Data Fusion techniques are becoming increasingly important in many application contexts, such as defence, energy, biomedicine, manufacturing, etc. Fusion methods lead to better understanding of a phenomenon and of the decisions to be taken, especially in terms of robustness and accuracy with respect to what we would obtain using separate sources of information [1].

We can identify three increasing abstraction levels of Data Fusion models: Data Level, Feature Level and Decision Level. Dasarathy [2] has proposed five fusion modes : Data In-Data Out (Dal-DaO) Fusion, Data In-Feature Out (Dal-FeO) Fusion, Feature In-Feature Out (FeI-FeO) Fusion, Feature In-Decision Out (FeI-DeO) Fusion, Decision In-Decision Out (DeI-DeO) Fusion.

In this work, we investigate the application of a Bayesian approach to the FeI-DeO Fusion, which can be considered one of the most common fusion paradigms. The input features, coming from different sensors, are merged to produce a more informed decision. The data, retrieved from each sensor, can have missing, or wrong values, and the proposed Bayesian approach permits to manage them in a robust and flexible way.

In the following, we apply the Bayesian Data Fusion methodology to the Classification of Documents in a Maritime Port scenario, limiting our attention to documents such as Passports, Identity Cards and Fiscal Codes from different countries.

The general architecture of such system is similar to Automated Border Control (ABC) [3], which is a self-service barrier that permits the identification of the passengers through the comparison between biometrics information stored in the passport's chip and the face, fingerprint, or iris (or a combination of them). These automatic systems have improved the efficiency, rapidity and security of the identification process. A simplified scheme of an ABC is presented in Figure 1.

In our applications, each document is scanned in its front and back, and three specialized detectors extract face, text, and barcode, possibly present in it. The related content is also stored for a Document Verification, or for other steps of the overall Border Control as: Authenticity Check, Identity Verification, etc.
![img-0.jpeg](img-0.jpeg)

Figure 1. Automatic Border Control (ABC) Schematic Representation.
The document classification has been emerging as an important task for its application in several real scenarios where a huge number of documents has to be managed. In this context, many different solutions have been proposed that use the layout, the contained text, the visual contents or a combination of them as the more recent solutions [4,5]. In the recent years some approaches based on the Graph Convolutional Networks have demonstrated to be very promising [6,7] given their capability to describe the relations among different part of the document.

The identity document classification can be considered a particular type of more generic document classification task but the layout is not discriminant enough because the identity documents have similar layouts, the textual information is not so easy to extract and the available datasets are small and with critical privacy and legal issues. In the years the identity document classification task has been tackled using different approaches. Some solutions have used the visual features extracted from the document image itself in order to train a classifier [8,9]; other works have used the template matching approach comparing the observed document with some reference models [10]; finally different deep learning approaches have been investigated as $[8,11,12]$.

In our work, instead of focusing on the strength and weakness of the particular classifiers and/or features, we describe a general architecture where information from different detectors (in general feature extractors or different classifiers), are fused together in order to infer the type of the presented document. The technique is based on the Naive Bayes model represented as Factor Graph in Reduced Normal Form (FGrn) [13]. Even though there is a vast literature on the application of Naive Bayes to the classification task and for the decision fusion [14,15], the usage of FGrn paradigm, confers to the proposed architecture more flexibility, extendibility and robustness in an unified probabilistic framework.

This work has been inspired by works on probabilistic context analysis [16,17]. In one of our previous works [18], we demonstrated that the context is a very valuable information to help complete or correct some available evidence. In this work we demonstrate that the presented model builds a sort of context for the measures, which reduces the uncertainty and improves the robustness of the overall system.

# 2. Materials and Methods 

### 2.1. Model Architecture

For each document, we have at maximum one image for each side: front and back. Each image is presented to three detectors: Face Detector, Text Detector and Barcode Detector. Each detector returns, if it exists, the bounding box containing the object of interest: face, text and barcode.

We focus on simple features, i.e., the ratio between Area in Detected Bounding Box and the Area of the complete image. More complex features as CNN Features, SIFT or feature based on words extracted from the documents, could be used, but here we are focusing on the general fusion model and not so much on the best single features.

Moreover, the proposed approach permits to treat some situations that can occur in a real scenario, when some detections can be missing or wrongly transmitted and when some detectors, or detections, are more reliable than others.

### 2.1.1. Face Detector

The face detection has been implemented using YOLOv3 model [19], i.e., a deep neural network of 106 layers where the first 53 layers, called Darknet-53 and derived by Darknet-19 introduced in [20], are used as feature extractor. The major novelty of the YOLOv3, respect to the previous versions, is the capability of making detection on three different scales following the idea behind the feature pyramid paradigm [21]. YOLOv3 predicts 3 bounding boxes for each cell into which the image is divided. Each bounding box is described by $5+Y_{C}$ parameters: two center coordinates, two dimensions, the objectness score (that express how confident is the model that that box contains an object) and a classification vector that describes the classification confidence for each of $Y_{C}$ considered class.

For our face detection problem, we used weights of a pretrained architecture on WIDER FACE Dataset [22] available at [23], where the only class of interest is "face".

### 2.1.2. Text Detector

Text detection has been implemented using the East model [24] with the pretrained weights available at [25]. East's peculiarity is its ability to perform accurate detection on images that are not perfectly centered and rotated. The model is composed by three parts: the feature extractor, the feature merger and the predictor. The detected geometry is represented as a rotated box (R-BOX), consisting of four distances from the top, right, bottom, left boundaries of the rectangle and a rotation angle. The final step is the NonMaximum Suppression algorithm, which avoids multi-detections of the same object.

### 2.1.3. Barcode Detector

Barcode detection was implemented using the Computer Vision algorithm adapted from [26]. The detector does not work with all existing barcodes, but it works well with those with a striped spectrum as ones present on identity cards and maritime documents. The input image is converted in grayscale and filtered using Scharr operator (with a $3 \times 3$ kernel) to detect the second derivative in the horizontal and vertical direction. The gradient image is filtered with a $9 \times 9$ blurring filter and a binary thresholding algorithm is applied in order to create a black and white image, where the white region contains the barcode. Morphological operations are also applied to make the candidate region more regular. Finally, if a detection exists, the boundaries of the barcode region are determined and the detector returns the coordinates of the bounding box.

### 2.2. Feature Fusion Model

The proposed feature fusion architecture is based on the Naive Bayes model where $N$ observed categorical variables $\left\{X_{1}, X_{2}, \ldots, X_{N}\right\}$ are connected to a single class variable $C$.

Each observed variable represents the output of a sensor, detector or, more in general, an information source that need to be fused together with the other ones. It assumes values in a discrete alphabet: $\mathcal{X}_{i}=\left\{\xi_{1}^{i}, \xi_{2}^{i}, \ldots, \xi_{L_{i}}^{i}\right\}$; where the dimension $L_{i}$ is the number of values

that each variable can assume, if discrete, or the number of levels we use to quantize it (and which is therefore generally different for each variable). For the continuous variables several quantization schemes may be used, but here we propose a simple approach: the values assumed by each $X_{i}$ are clipped in $\left[m_{X_{i}}, M_{X_{i}}\right]$, where $m_{X_{i}}$ and $M_{X_{i}}$ are, respectively, the minimum and maximum permitted value for variable $X_{i}$. The range is then divided uniformly using $L_{i}$ levels, so that the generic continuous value $v$ is associated with level $l$ if $(l-1)<v \leq l$.

It should be noted that in an Internet of Things (IoT) context, the number of levels used to quantize the sensor measure may be an important design parameter. In fact, generally, the trade-off between accuracy and available hardware resources need to be evaluated, for every specific application, also in terms of overall system energy consumption [15].

Finally, in the training phase, each variable $X_{i}$ is represented through a discrete distribution obtained using a smooth one-hot encoding. More specifically, for representing the $k$-th value of $X_{i}\left(\xi_{k}^{i}\right)$, instead of use a sharp distribution $\boldsymbol{\delta}_{k}^{i}$ (an $L_{i}$ size vector representing the Kronecker delta, i.e., with all zero and only a one at the $k$-th position), we use a smoother distribution:

$$
\boldsymbol{\delta}_{k}^{i}=\overbrace{\left(\frac{\epsilon}{\left(L_{i}-1\right)}, \ldots, 1-\epsilon, \ldots, \frac{\epsilon}{\left(L_{i}-1\right)}\right.}^{L_{i}}
$$

where $\epsilon$ is a small positive number.
Since the values assumed by the detections are always positive, we set the minimum value $m_{X_{i}}=\frac{M_{X_{i}}}{L_{i}}$ in order to "use" all $L_{i}$ levels. Differently, with $m_{X_{i}}=0$, the first quantization level will be underused since there are no negative values.

Furthermore, we assume that all observed variables are connected to one class variable $C$ that assumes values in the discrete alphabet $\mathcal{C}=\left\{\gamma_{1}, \gamma_{2}, \ldots, \gamma_{L_{c}}\right\}$.

The relationship between each observed and class variable, is formalized by a Conditional Probability Table (CPT): $P\left(X_{i} \mid C\right)=\left[\operatorname{Pr}\left\{X_{i}=x_{i} \mid C=c\right\}\right]_{c \in \mathcal{C}}^{x_{i} \in \mathcal{X}_{i}}$. This model is the classical Naive Bayes, shown in Figure 2 together with its FGrn representation, which represents the joint probability distribution:

$$
p_{X_{1}, X_{2}, \ldots, X_{N}, C}\left(x_{1}, x_{2}, \ldots, x_{N}, c\right)=\pi_{C}(c) \prod_{i=1}^{N} p_{X_{i} \mid C}\left(x_{i} \mid c\right)
$$

where $\pi_{C}$ is the prior on $C$.
![img-1.jpeg](img-1.jpeg)

Figure 2. The Naive Bayes model as a Bayesian graph (a) and as a Factor Graph in Reduced Normal Form (b).

Please note that in the FGrn formulation the CPTs in Figure 2b are represented as Single Input-Single Output (SISO) blocks, making the model more flexible [13,27,28] with respect to other factor graph representation [29]. Learning each CPT is performed locally through backward and forward messages using the optimized Maximum Likelihood algorithm as

described in [30]. The usage of FGrn provides us with a formal probabilistic framework for learning and allows easy handling of classification, error correction, missing values, etc.

In every single inference phase, when all observed variables are instantiated, the backward messages $\mathbf{b}_{X_{i}}=\boldsymbol{\delta}_{k_{i}}^{i}$ are injected into the network, where $k_{i}$ is the index position of the instantiated value $\bar{x}_{i}:=\xi_{k_{i}}^{i}$ for the variable $X_{i}$. In functional notation the backward message would be $\left.b_{X_{i}}\left(x_{i}\right)=\delta\left(x_{i}-\bar{x}_{i}\right)\right|_{\bar{x}_{i} \in X_{i}}$, with $i=1, \ldots, N$. The class label is not observed and its forward message, $\mathbf{f}_{\mathcal{C}}$, is set to a uniform distribution over class alphabet $\mathcal{C}$.

After message propagation, the product of the backward and the forward messages at the class label $\left(b_{C}(c) f_{C}(c)\right)$ is proportional to the posterior probability of the class given all the other instantiated observed variables, i.e.: $b_{C}(c) f_{C}(c)=p_{X_{1}, \ldots, X_{N}, C}\left(\bar{x}_{1}, \ldots, \bar{x}_{N}, c\right) \propto$ $p_{C \mid X_{1}, \ldots, X_{N}}\left(c \mid \bar{x}_{1}, \ldots, \bar{x}_{N}\right)$.

Suppose that all observed variables except one (e.g., $X_{1}$ ) are instantiated and that the class variable is unknown. Once we injected the messages in the network properly, after the message propagation we obtain:

$$
\begin{aligned}
f_{X_{1}}\left(x_{1}\right) & =\sum_{c} p_{X_{1} \mid C}\left(x_{1} \mid c\right) p_{X_{2} \mid C}\left(\bar{x}_{2} \mid c\right) \ldots p_{X_{N} \mid C}\left(\bar{x}_{N} \mid c\right) \pi_{C}(c) \\
& \propto p_{X_{1} \mid X_{2}, \ldots, X_{N}}\left(x_{1} \mid \bar{x}_{2}, \ldots, \bar{x}_{N}\right)
\end{aligned}
$$

in other words, the forward distribution of the non-instantiated variable is proportional to its posterior probability given all the other instantiated observed variables.

If also the class label is instantiated, the forward distribution of the non-instantiated variable (e.g., $X_{1}$ ), is proportional to its posterior probability given the class variable, i.e.: $f_{X_{1}}\left(x_{1}\right) \propto p_{X_{1} \mid C}\left(x_{1} \mid \bar{c}\right)$. This is coherent with the Naive Bayes model where each observed variable is conditionally independent from other variables given the class label.

The forward messages that we can collect at the observed variables represent the most probable configuration given the evidence and the learned model. Injected messages consistent with the forward values are considered plausible, while when this accordance is low an error, or a strange behavior, may have occurred.

We can also try to condition the behavior of the system based on the reliability (estimated or assumed) of each detector. If we have low confidence on a particular observed variable, $X_{i}$, we can try to reduce its contribution raising the message $\mathbf{b}_{C^{(i)}}$ to an exponent $0<v<1$ and normalizing the resulting message. The effect of this operation is to make $\left(\mathbf{b}_{C^{(i)}}\right)^{v}$ more and more uniform with $v \rightarrow 0$, a sort of smoothing for the message. A uniform message does not make any contribution in the element-by-element product performed in the replicator block and successive normalization of the resulting message.

All the other messages $\mathbf{b}_{C^{(i)}}$, with $i \in\{1, \ldots, N\} \backslash\{e\}$, can remain raised to 1 (no effect), or can be slightly augmented (raising to an exponent $v>1$ ) to weight more their contribution since the distribution thickens around the most probable value, a sort of sharpening for the message.

# 2.3. Model Evaluation 

After the training phase, we can obtain classification results together with other inference over observed variable. Usually, in the classification problems, a confusion matrix that summarizes the classification performance of the trained model is computed. To take better into account the uncertainty in the answer, we present also the Jensen-Shannon divergence and Conditional Entropy on the class variable.

### 2.3.1. Likelihood

The likelihood for each example (observed variables) is available anywhere in the network. For example, the Likelihood for the $n$-th example of the $X_{1}$ variable is:

$$
\begin{aligned}
L_{X_{1}}[n] & =\sum_{c} p_{X_{1}, X_{2}, \ldots, X_{N}, C}\left(\bar{x}_{1}, \bar{x}_{2}, \ldots, \bar{x}_{N}, c\right) \\
& =p_{X_{1}, X_{2}, \ldots, X_{N}}\left(x_{1}, \bar{x}_{2}, \ldots, \bar{x}_{N}\right) \delta\left(x_{1}-\bar{x}_{1}\right) \\
& \propto f_{X_{1}}\left(x_{1}\right) b_{X_{1}}\left(\bar{x}_{1}\right)
\end{aligned}
$$

The previous equation is true for each observed variable and it is always identical in every point of the network. The Likelihood computation can be performed for all examples of Training set and Test set.

# 2.3.2. Conditional Entropy 

The capability of the system to provide sharp responses on class variable, given all observed variables, can be obtained considering the conditional entropy of $C$ given all the others [31], which quantifies the uncertainty we have on $C$ given the evidence:

$$
\begin{aligned}
\mathcal{H}\left(C \mid X_{1},\right. & \left.\ldots, X_{N}\right) \\
& =-\sum_{x_{1}, \ldots, x_{N}, c} p_{X_{1}, \ldots, X_{N}, C}\left(x_{1}, \ldots, x_{N}, c\right) \log p_{C \mid X_{1}, \ldots, X_{N}}\left(c \mid x_{1}, \ldots, x_{N}\right) \\
& :=-\sum_{\boldsymbol{x}, c} p_{\boldsymbol{X}, C}(\boldsymbol{x}, c) \log p_{C \mid \boldsymbol{X}}(c \mid \boldsymbol{x})
\end{aligned}
$$

Considering the $n$-th example, we can therefore compute the conditional entropy of $C$ using messages as follows:

$$
\begin{aligned}
\mathcal{H}\left(C \mid X_{1}\right. & \left.=\bar{x}_{1}, \ldots, X_{N}=\bar{x}_{N}\right) \\
& =-\sum_{c} p_{X_{1}, \ldots, X_{N}, C}\left(\bar{x}_{1}, \ldots, \bar{x}_{N}, c\right) \log p_{C \mid X_{1}, \ldots, X_{N}}\left(c \mid \bar{x}_{1}, \ldots, \bar{x}_{N}\right) \\
& :=-\sum_{c} p_{\boldsymbol{X}, C}(\overline{\boldsymbol{x}}, c) \log p_{C \mid \boldsymbol{X}}(c \mid \overline{\boldsymbol{x}}) \\
& =-\sum_{c} p_{\boldsymbol{X}, C}(\overline{\boldsymbol{x}}, c) \log \frac{p_{\boldsymbol{X}, C}(\overline{\boldsymbol{x}}, c)}{p_{\boldsymbol{X}}(\overline{\boldsymbol{x}})} \\
& =-\sum_{c} p_{\boldsymbol{X}, C}(\overline{\boldsymbol{x}}, c) \log p_{\boldsymbol{X}, C}(\overline{\boldsymbol{x}}, c)+\sum_{c} p_{\boldsymbol{X}, C}(\overline{\boldsymbol{x}}, c) \log p_{\boldsymbol{X}}(\overline{\boldsymbol{x}}) \\
& =-\sum_{c} b_{C}(c) f_{C}(c) \log b_{C}(c) f_{C}(c)+\log p_{\boldsymbol{X}}(\overline{\boldsymbol{x}}) \sum_{c} b_{C}(c) f_{C}(c) \\
& \text { if } f_{C}(c) \text { is uniform } \\
& =-\frac{1}{|C|} \sum_{c} b_{C}(c) \log b_{C}(c)+\frac{1}{|C|}\left(\log p_{\boldsymbol{X}}(\overline{\boldsymbol{x}})+\log |C|\right) \sum_{c} b_{C}(c) \\
& \text { since } b_{C}(c) \text { is normalized } \\
& =-\frac{1}{|C|} \sum_{c} b_{C}(c) \log b_{C}(c)+\frac{1}{|C|} \log p_{\boldsymbol{X}}(\overline{\boldsymbol{x}})+\frac{1}{|C|} \log |C| \\
& \propto-\sum_{c} b_{C}(c) \log b_{C}(c)+\log p_{\boldsymbol{X}}(\overline{\boldsymbol{x}})+\log |C|
\end{aligned}
$$

Since $\log p_{\boldsymbol{X}}(\overline{\boldsymbol{x}})$ and $\log |C|$ are constant respect to $c$, we focus only on the first term. As Likelihood, we can average Conditional Entropy over the Training and the Test Set.

### 2.3.3. Jensen-Shannon Divergence

Since the confusion matrix is based on the MAP (Maximum a Posteriori) rule, some interesting behaviors (how wrong are the results, what are the situations where the output is completely uniform, etc.) may be invisible. For this reason, we evaluated the Jensen-Shannon (JS) divergence between $b_{C}(c)$ and $f_{C}(c)$. The JS divergence is based on Kullback Laibler (KL) divergence but has the advantage to be symmetric. Suppose we have two distribution $P$ and $Q$ over the same set $\mathcal{X}$, then the JS divergence is defined as $J S(P, Q)=\frac{1}{2} K L(P, M)+\frac{1}{2} K L(Q, M)$; where $M=\frac{1}{2}(P+Q)$, and $K L(P, M)$ and $K L(Q, M)$ are respectively the KL divergence between $P$ and $M$ and $Q$ and $M$.

## 3. Results

In this work, we test the Fusion Model for the identity documents classification task. We selected simple features that model the predominance of a particular object (Face, Text, Barcode) in a document. Each feature is the ratio between area of the detection and total area of the document. The six categorical random variables are: Face Front $\left(X_{F F}\right)$, Face Back $\left(X_{F B}\right)$, Text Front $\left(X_{T F}\right)$, Text Back $\left(X_{T B}\right)$, Barcode Front $\left(X_{B F}\right)$, Barcode Back $\left(X_{B B}\right)$. Each variable represents and takes values in its discrete alphabets: $\mathcal{X}_{F F}, \mathcal{X}_{F B}, \mathcal{X}_{T F}, \mathcal{X}_{T B}$, $\mathcal{X}_{B F}, \mathcal{X}_{B B}$ of dimension, respectively, $L_{F F}, L_{F B}, L_{T F}, L_{T B}, L_{B F}, L_{B B}$. The dimension of each dictionary is the number of levels we use to quantize the ratios of interest and, generally, is not the same for all variables.

The continuous and positive values obtained from each detector has to be properly quantized in order to be treated from our model where each observed variable $X \in$ $\left\{X_{F F}, X_{F B}, X_{T F}, X_{T B}, X_{B F}, X_{B B}\right\}$ is categorical.

# 3.1. Dataset Preparation 

Since privacy and legal issues, it is extremely difficult to access to a public dataset of identity documents. For this reason, we collected several identity documents from Internet adding 50 documents recorded in [32] and 36 private documents of some volunteers. The "other" documents are collected from Internet considering documents that could be related to the context of our interest and from RVL-CDIP Dataset [33], in particular from "invoice" and "form" categories.

In this way, we built a private dataset composed of 412 images representing personal documents: Fiscal Codes, Identity Documents, Driving License, Passports, and Other Images that can occur in the maritime application domain. The Driving License are then fused in the more general Identity Documents category.
![img-2.jpeg](img-2.jpeg)

Figure 3. Some examples extracted from the Dataset. For privacy motivations, personal data has been obfuscated.

For many documents (298) only the front pages are available and all the "back" variables $\left(X_{B B}, X_{F B}, X_{T B}\right)$ are missing. These examples have been excluded from the training process. The resulting 114 documents are distributed as follows: $29.8 \%$ are Fiscal Codes (fc), $9.6 \%$ are Identity Documents (id), $32.5 \%$ are Passports (pa) and $28.1 \%$ are Other documents (other). Since the document distribution is not related to the probability that a document is shown to the desk, the prior probability $\pi_{C}$ has not been learned and set to uniform over the 4 possible values. Table 1 contains the main characteristics of the considered dataset and the Figure 3 shows some examples.

Table 1. Characteristics of the dataset.


Following what is described in Section 2.2, we set $M_{X_{i}}$ to 95 th percentile of the values present in the Training Set, $L_{X_{i}}=10$ and $m_{X_{i}}=M_{X_{i}} / 10$ for each observed variable $X_{i}$, except for the variable $X_{B B}$ which it is set to 75 th percentile of the values present in the Training Set. The $\epsilon$ value is set to $10^{-5}$.

After the quantization process a 5-fold Stratified Cross Validation procedure has been performed to assess the Classification Accuracy of the learned model. To have a fair evaluation of the model's performance, at each split (after the quantization process based on the parameters defined from Training Set as described above), all duplicated records and records also present in the Training Set are removed from the Test Set. At this point we have backward messages for the observed variables and the same number of forward messages for the class variables. At each epoch the flow of messages in the network is used to learn the SISO blocks, with $N_{s}=3$ cycles and following the rules described in [13,28]. The learning process is stopped when all CPTs are unchanged and for a maximum of $N_{e}=50$ epochs. In Table 2 the confusion matrix for the dataset is shown together with per class precision, recall and F1-Score [34]. The overall classification accuracy is $82.7 \%$ and the macro-average F1-Score (harmonic mean of the average precision and recall) is 0.8073 .

Table 2. Confusion Matrix, per class precision, recall and F1-Score without missing values.


# 3.2. Inference 

In the following paragraphs we present the results of some inference tasks based on a model trained on 80 records and tested on 22 . The inference is performed injecting into the network the backward messages for the observed variables and collecting the backward messages at the class variable, comparing the resulting $\mathbf{b}_{C}$ with the ground truth for the current example. Moreover the model responds with forward messages on the observed variables that is proportional, for each variable, to the posterior probability of the considered observed variable given all the other instantiated variables (Equation (2)). This is a sort of probability induced from the measure's context represented by all evidences injected in the network.

Figure 4 shows the model's answer when we inject the evidence related to an example: when the injected value is correct (upper row), when there is an error on $X_{T F}$ variable (middle row) and when the $X_{T F}$ variable is completely missing (lower row). It should be noted that both in missing and wrong cases, the model responds with the correct class, providing also with $\mathbf{f}_{X_{T F}}$, that tries to correct, or complete the injected value since the suggested values are more consistent with the measure's context.

### 3.2.1. Measure's Context

Figure 5 shows the model's answer when we inject the evidence on the class variable $\left(\mathbf{f}_{C}\right)$ and collect the forward messages on the observed variables $\left(\mathbf{f}_{X_{i}}\right)$ that represent the $p_{X_{i} \mid C}\left(x_{i} \mid \vec{v}\right)$. The distributions shown could be considered to be a context that can help the system in situation of high uncertainty, permitting, for example, to detect strange disagreement between the injected evidence and the system knowledge.

![img-3.jpeg](img-3.jpeg)

Figure 4. Upper Row: Injected Variable and model's answer. Middle Row: Injected Variable with Error on Variable $X_{T F}$ and related answer. Lower Row: Injected Variable with the completely missing variable $X_{T F}$ and related answer.
![img-4.jpeg](img-4.jpeg)

Figure 5. Induced distribution on the observed variable from the Class.

# 3.2.2. Missing Values' Management 

One of the most important characteristics of the Bayesian approach is its capability to treat missing values. In Figure 6 the effect of the absence of some detections on the classification performance is shown. All detections are correctly injected in the network except for $k$ of them that are completely missing, and for which uniform distributions are injected in the network.

For increasing number of missing variables, we compute all the possible missing variables' combinations and average the obtained metrics: classification accuracy, JensenShannon Divergence and Conditional Entropy.

In Figure 6d we show also the number of completely uncertain classification that is always zero except for high number of missing variables. With all variable missing, we have a completely uncertain classification for all presented examples.

![img-5.jpeg](img-5.jpeg)

Figure 6. (a) Classification accuracy, (b) Jensen-Shannon divergence on Class Variable, (c) Conditional Entropy of Class Variable and (d) the number of completely uncertain classifications varying the number of missing variables.

The graph demonstrates that, in the average, also with three completely missing detections (e.g., $X_{F F}, X_{F B}, X_{T B}$ or $X_{F F}, X_{T B}$ and $X_{B B}$, etc.) the classification accuracy decreases less than $10 \%$ and also other metrics confirm the robustness of this model to the missing values. Please note that the Conditional Entropy describes an increasing in the uncertainty, in other words the classification becomes less sharp.

To emphasize the capability of the model to treat missing values, following the same procedure described in Section 3.1, we performed a 5-fold Stratified Cross Validation but, now, including the records with missing values in the Training Set and in the Test Set at each split (also in this case all duplicated records and records also present in the Training Set are removed from the Test Set). In Table 3 the confusion matrix is shown together with per class precision, recall and F1-Score. The overall classification accuracy is $76.2 \%$ and the macro-average F1-Score is 0.7474 .

In the same configuration, if we do not take in account missing values in Training Set, we obtain a decrease in the accuracy classification ( $62.6 \%$ ) and of the macro-average F1-Score ( 0.6506 ). This could suggest of including missing values also in the Training Set to increase the accuracy in presence of the missing values. Unfortunately, we can't conclude this because the dimension of the effective Test Set for two simulations are different since, in the first case, several records in the Training Set are present also in the Test Set and hence are removed from it.

Moreover, we trained the model using all 114 records without missing values and performed a classification task only on the unique 80 records that contain missing values for the "back" variables $\left(X_{B B}, X_{F B}, X_{T B}\right)$. The classification accuracy for these records is $58.8 \%$ and the macro-average F1-Score is 0.6274 . These simulations confirm the high flexibility and robustness of the model to manage missing values.

Table 3. Confusion Matrix, per class precision, recall and F1-Score including missing values.


# 3.2.3. Errors Management 

In Figure 7 the effect of the wrong detections on the classification performance is shown. In this simulation all detections are injected in the network but $k$ of them are assumed to be completely wrong. For increasing number of wrong variables, we compute all the possible variables' combinations and, for each combination, we insert 5 random detections for each variable using the smooth deltas. We let the messages flow in the network and average the obtained metrics: classification accuracy, Jensen-Shannon Divergence and Conditional Entropy. In Figure 7d we show also the number of completely uncertain classification. The graph shows how the system performance does not decrease too much for one wrong detection, but it decreases dramatically when more errors are inserted.
![img-6.jpeg](img-6.jpeg)

Figure 7. (a) Classification accuracy, (b) Jensen-Shannon divergence on Class Variable, (c) Conditional Entropy of Class Variable and (d) the number of completely uncertain classifications varying the number of wrong values.

# 3.2.4. Reliability Test 

As described in Section 2.2, the information coming from different devices has a reliability dependent on the confidence of the related detector. This reliability value can be assigned globally to a particular detector, or to a particular example, if we have evidence that the current one is not so accurate. In Figure 8 the effect of raising the messages $\mathbf{b}_{C^{(r)}}$ related to detectors containing errors, with an exponent $v_{e}$ is shown. The exponent of messages related to other observed variables, i.e., not affected by errors, are indicated as $v_{\sim e}$ and are set to 1 (no effect) or "normalized", in a way that the sum of all exponents is 6 with a sharpening effect on these variables:

$$
v_{\sim e}:=\left.v_{i}\right|_{i \neq e}=\frac{N-v_{e}}{N-1}=\frac{6-v_{e}}{5}
$$

As expected, with values of $v_{e}$ extremely low $(1 e-7)$ the trends are the same that in Figure 6, because the effect of such a small value for $v_{e}$ is to delete completely the information related to a particular detector. The intermediate values of $v_{e}$ instead, reduce the effect of the error improving the performance of system in terms of Classification Accuracy and Jensen-Shannon divergence.
![img-7.jpeg](img-7.jpeg)

Figure 8. (a) Classification accuracy, (b) Jensen-Shannon divergence on Class Variable, (c) Conditional Entropy of Class Variable varying the number of wrong values and setting different combination of $v$.

## 4. Conclusions

In this work, we described an Information Fusion architecture using the Factor Graph in Reduced Normal Form paradigm.

The proposed approach permits learning a sort of measure's context that, in presence of high uncertainty, helps to detect disagreement between the injected evidence and the system knowledge, giving to overall system great flexibility and robustness in the handling missing and wrong values. The proposed architecture, in fact, also in presence of missing values and errors, continues to have a good classification performance.

We also demonstrated how it is possible to condition the system in the presence of information sources with different reliability or in presence of single unreliable detection. This is another demonstration of the flexibility of the paradigm that can manage several information sources taking into account their peculiarities.

Even though the approach is completely general and applicable to several contexts where it is required to fuse information from several sources, the framework has been applied to a classification problem of identity documents, where different detectors are fused into a unique classifier.

Author Contributions: Conceptualization, A.B., G.D.G., F.A.N.P.; methodology, A.B., G.D.G., F.A.N.P.; software, A.B., A.N., G.C.; validation, A.B., G.D.G., F.A.N.P.; investigation, A.B., G.D.G., F.A.N.P.; data curation, A.N.; writing-original draft preparation, A.B.; writing-review and editing, A.B., A.N., G.C., G.D.G., F.A.N.P., M.V., G.G.; visualization, A.B., A.N.; supervision, A.B., F.A.N.P., M.V., G.G.; funding acquisition, F.A.N.P. All authors have read and agreed to the published version of the manuscript.

Funding: Work partially supported by POR CAMPANIA FESR 2014/2020, ITS for Logistics, awarded to CNIT (Consorzio Nazionale Interuniversitario per le Telecomunicazioni)

Data Availability Statement: The data are not publicly available due to privacy. The dataset of extracted features used in this study is available on request from the corresponding author.

Conflicts of Interest: The authors declare no conflict of interest. The funders had no role in the design of the study; in the collection, analyses, or interpretation of data; in the writing of the manuscript, or in the decision to publish the results.
