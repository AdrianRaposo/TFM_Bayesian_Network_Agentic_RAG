# Features Dimensionality Reduction Approaches for Machine Learning Based Network Intrusion Detection 

Razan Abdulhammed ${ }^{1}$ (D), Hassan Musafer ${ }^{1}$ (D), Ali Alessa ${ }^{1}$ (D), Miad Faezipour ${ }^{1,2,+}$ (D) and Abdelshakour Abuzneid ${ }^{1}$ (D)<br>1 Department of Computer Science \& Engineering, University of Bridgeport, Bridgeport, CT 06604, USA; rabdulha@my.bridgeport.edu (R.A.); hmusafer@my.bridgeport.edu (H.M.); aalessa@my.bridgeport.edu (A.A.); abuzneid@bridgeport.edu (A.A.)<br>2 Department of Biomedical Engineering, University of Bridgeport, Bridgeport, CT 06604, USA<br>* Correspondence: mfaezipo@bridgeport.edu; Tel.: +1-203-576-4702

Received: 11 February 2019; Accepted: 11 March 2019; Published: 14 March 2019


#### Abstract

The security of networked systems has become a critical universal issue that influences individuals, enterprises and governments. The rate of attacks against networked systems has increased dramatically, and the tactics used by the attackers are continuing to evolve. Intrusion detection is one of the solutions against these attacks. A common and effective approach for designing Intrusion Detection Systems (IDS) is Machine Learning. The performance of an IDS is significantly improved when the features are more discriminative and representative. This study uses two feature dimensionality reduction approaches: (i) Auto-Encoder (AE): an instance of deep learning, for dimensionality reduction, and (ii) Principle Component Analysis (PCA). The resulting low-dimensional features from both techniques are then used to build various classifiers such as Random Forest (RF), Bayesian Network, Linear Discriminant Analysis (LDA) and Quadratic Discriminant Analysis (QDA) for designing an IDS. The experimental findings with low-dimensional features in binary and multi-class classification show better performance in terms of Detection Rate (DR), F-Measure, False Alarm Rate (FAR), and Accuracy. This research effort is able to reduce the CICIDS2017 dataset's feature dimensions from 81 to 10, while maintaining a high accuracy of $99.6 \%$ in multi-class and binary classification. Furthermore, in this paper, we propose a Multi-Class Combined performance metric Combined $_{\text {Mc }}$ with respect to class distribution to compare various multi-class and binary classification systems through incorporating FAR, DR, Accuracy, and class distribution parameters. In addition, we developed a uniform distribution based balancing approach to handle the imbalanced distribution of the minority class instances in the CICIDS2017 network intrusion dataset.


Keywords: Dimensionality Reduction; Intrusion Detection System (IDS); Sparse Auto Encoder (SAE); Principle Component Analysis (PCA); Uniform Distribution Based Balancing (UDBB)

## 1. Introduction

Network Intrusion Detection System (IDS) is a software-based application or a hardware device that is used to identify malicious behavior in the network [1,2]. Based on the detection technique, intrusion detection is classified into anomaly-based and signature-based. IDS developers employ various techniques for intrusion detection. One of these techniques is based on machine learning. Machine learning (ML) techniques can predict and detect threats before they result in major security incidents [3]. Classifying instances into two classes is called binary classification. On the other hand, multi-class classification refers to classifying instances into three or more classes. In this research, we adopt both classifications. For the multi-class classification, there are 15 classes, where each class

represents either normal network flow traffic or one of 14 types of attacks. For the binary case, the network flow traffic is being classified into either normal or anomaly (attack) traffic.

An Artificial Neural Network (ANN) is a self-adaptive mathematical and computational model that is composed of an interconnected group of artificial neurons. There are multiple types of ANNs such as Deep Convolution Neural Networks (DCNN), Recurrent Neural Networks (RNN) and Auto-Encoder (AE) neural networks, each of which come with their own specific applications and levels of complexity. Deep learning is a promising machine learning-based approach that can address the challenges associated with the design of intrusion detection systems as a result of its outstanding performance in dealing with complex, large-scale data.

This study accustoms Auto-Encoder (AE) and Principle Component Analysis (PCA) for dimensionality reduction. As a proof-of-concept and to verify the feature dimensionality reduction ideas, the paper used the up-to-date CICIDS2017 intrusion detection and prevention dataset [4], which consists of five separated data files. Each file represents the network traffic flow and specific types of attacks for a certain period of time. To be more specific, the dataset was collected based on a total of 5 days, Monday through Friday. The traffic flow on Monday includes the benign network traffic, whereas the implemented attacks in the dataset were executed on Tuesday, Wednesday, Thursday and Friday. In this paper, we combined all CICIDS2017's files together and fed them through the AE and PCA units for a compressed and lower dimensional representation of all the fused data. Figure 1 displays the overall idea of the proposed framework.
![img-0.jpeg](img-0.jpeg)

Figure 1. Proposed Framework.

# 1.1. Problem Statement 

In machine learning problems, the high-dimensional features lead to prolonged classification processes. This is while low-dimensional features can reduce these processes. Moreover, classification of network traffic data with imbalanced class distributions has posed a significant drawback on the performance attainable by most well-known classifiers, which assume relatively balanced class distributions and equal miss-classification costs. The frequent occurrence and issues associated with imbalanced class distributions indicate the need for extra research efforts. Previous studies of intrusion detection systems have not dealt with classification of network traffic data with imbalanced class distributions. Furthermore, with the presence of imbalanced data, the known performance metrics may fail to provide adequate information about the performance of the classifier.

### 1.2. Key Contributions and Paper Organization

The key contributions of this paper include the development of a framework for machine learning-based network intrusion detection. The proposed anomaly-based intrusion detection system uses AE as well as PCA for dimensionality reduction and well-tested classifiers such as Random Forest (RF), Bayesian Network (BN), Linear Discriminant Analysis (LDA) and Quadratic Discriminant Analysis (QDA). In summary, the main contributions of this work are as follows:

1. We achieved effective pattern representation and dimensionality reduction of features in the CICIDS2017 dataset using AE and PCA.

2. We used the CICIDS2017 dataset to compare the efficiency of the dimensionality reduction approaches with different classification algorithms, such as Random Forest, Bayesian Network, LDA and QDA in binary and multi-class classification.
3. We developed a combined metric with respect to class distribution to compare various multi-class classification systems through incorporating the False Alarm Rate (FAR), Detection Rate (DR), Accuracy and class distribution parameters.
4. We developed a Uniform Distribution Based Balancing (UDBB) approach for imbalanced classes.

The overall structure of the remainder of this paper is organized as follows. An overview of the dimensionality reduction approaches selection criteria and related work is provided in Section 2. Next, in Section 3, the paper gives a brief review of the CICIDS2017 dataset, describes the attack types embedded in the dataset, and further explains the preprocessing and unity-based normalization steps. In Section 4, the paper explains in detail, the dimensionality reduction approaches based on AE as well as PCA. Afterwards, the performance evaluation metrics are introduced in Section 5. Section 6 elaborates on the Uniform Distribution Based Balancing (UDBB) approach. Next, in Section 7, the paper summarizes the principal findings of the experiments and discusses the results. The challenges and limitations are discussed in Section 8. Finally, the conclusions and future directions are discussed in Section 9.

# 2. Dimensionality Reduction Approaches Selection Criteria and Related work 

This section aims to review the published related work in the past recent years that used features dimensionality reduction approaches to design an intrusion detection system. The selection process was based on certain criteria such as:

1. Being relevant to the CICIDS2017 dataset
2. Being relevant to dimensionality reduction approaches; precisely, the auto-encoder and the PCA
3. Being relevant to machine learning-based intrusion detection

For decades, researchers used dimensionality reduction approaches [5,6] for different reasons such as to reduce the computational processing overhead, reduce noise in the data, and for better data visualization and interpretation. One common dimensionality reduction approach is the Missing Value Ratio (MVR) approach [7]. The MVR approach is efficient when the number of missing values is high. For the CICIDS2017 dataset, the number of missing values is near zero. Therefore, we excluded the Missing Value Ratio approach. Other common approaches include the Forward Feature Construction (FFC) and Backward Feature Elimination (BFE) approaches [7]. Both FFC and BFE are prohibitively slow on high dimensional datasets, which is the case for CICIDS2017 ( $>2,500,500$ instances). As a result, we did not discuss these approaches. The PCA technique, on the other hand, is relatively computationally cost efficient, can deal with large datasets, and is widely used as a linear dimensionality reduction approach [5,8]. The auto-encoder dimensionality reduction approach is an instance of deep learning, which is also suitable for large datasets with high dimensional features and complex data representations [9].

This paper adopts AE as well as PCA for features dimensionality reduction. One of the most fundamental differences between AE and PCA in terms of dimensionality reduction is that in the auto-encoder approach, there is no assumption of linearity in the data. The auto-encoder optimizer figures out the function through the weights that best encode the data under the specified reconstruction error metric. This is while the PCA assumes linearity in the set of reduced data. Moreover, the computational complexity of a dimensionality reduction approach depends on the number of datapoints $n$ as well as their dimensionality $P$, and $w$ which is the number of weights in the auto-encoder. Table 1 shows the properties of AE and PCA for dimensionality reduction and lists the pros and cons of each.

Table 1. Properties of analyzed approaches for dimensionality reduction [8,9].


# 2.1. CICIDS2017 Related Work 

Sharafaldin et al. [4] used a Random Forest Regressor to determine the best set of features to detect each attack family. The authors examined the performance of these features with different algorithms that included K-Nearest Neighbor (KNN), Adaboost, Multi-Layer Perceptron (MLP), Naïve Bayes, Random Forest (RF), Iterative Dichotomiser 3 (ID3) and Quadratic Discriminant Analysis (QDA). The highest precision value was 0.98 with RF and ID3 [4]. The execution time (time to build the model) was 74.39 s . This is while the execution time for our proposed system using Random Forest is 21.52 s with a comparable processor. Furthermore, our proposed intrusion detection system targets a combined detection process of all the attack families.

In wireless mesh environments, Vijayan et al. [10] proposed an intrusion detection system that used the genetic algorithm (GA) as a feature selection method and multiple Support Vector Machines (SVM) for classification. Their system was based on a linear combination of multiple SVM classifiers, which were ordered based on the severity of the attacks. Each classifier was trained to detect a certain attack category using selected features by the GA. A small portion of the CICIDS2017 dataset instances were used to evaluate their system. Conversely, in this paper, we use all the instances of the CICIDS2017 dataset.

Moreover, authors in [11] compared and contrasted a frequency-based model from five sequence of aggregation rules with sequence-based modeling of the Long Short-Term Memory (LSTM) recurrent neural network. The investigation concluded that the frequency-based model tends to perform similar or better than the LSTM models in detecting the attacks.

Additionally, the researchers in [12] analyzed the CICIDS2017 dataset using digital wavelets. Their method efficiently detected service denial attacks of both Slow Loris and HTTP Denial of Service (DoS).

Furthermore, the authors of [13] applied the Multi-Layer Perceptron (MLP) classifier algorithm and a Convolutional Neural Network (CNN) classifier that used the Packet CAPture (PCAP) file of CICIDS2017. The authors selected specified network packet header features for the purpose of their study. Conversely, in our paper, we used the corresponding profiles and the labeled flows for machine and deep learning purposes. According to [13], the results demonstrated that the payload classification algorithm was judged to be inferior to MLP. However, it showed significant ability to distinguish network intrusion from benign traffic with an average true positive rate of $94.5 \%$ and an average false positive rate of $4.68 \%$.

The authors in [14] proposed a denial of service intrusion detection system that used the Fisher Score algorithm for features selection and Support Vector Machine (SVM), K-Nearest Neighbor (KNN) and Decision Tree (DT) as the classification algorithm. Their IDS achieved $99.7 \%, 57.76 \%$ and $99 \%$ success rates using SVM, KNN and DT, respectively. In contrast, our research proposes an IDS to detect all types of attacks embedded in CICIDS2017, and as shown in the confusion matrix results, achieves $100 \%$ accuracy for DDoS attacks using $(P C A-R F)_{M c-10}$ with UDBB.

The authors in [15] used a distributed Deep Belief Network (DBN) as the the dimensionality reduction approach. The obtained features were then fed to a multi-layer ensemble SVM. The ensemble SVM was accomplished in an iterative reduce paradigm based on Spark (which is a general distributed in-memory computing framework developed at AMP Lab, UC Berkeley), to serve as a Real Time Cluster Computing Framework that can be used in big data analysis [16]. Their proposed approach achieved an F-measure value equal to 0.921 .

The authors in [17] proposed a Data Dimensionality Reduction (DDR) method for network intrusion detection. Their proposed scheme was evaluated by XGBoost (Extreme Gradient Boosting) [18], SVM (Support Vector Machine), CTree (Conditional inference Trees) [19] and Neural network (Nnet) classifiers. The number of selected features was 36 and the highest achieved accuracy was $98.93 \%$ with XGboost. Furthermore, the authors excluded Monday network traffic of the CICIDS2017 dataset, which is only benign traffic in their system. This is while our work was able to achieve accuracy of $99.6 \%$ with 10 features. In addition, we kept all the files of the dataset that represent different classes of the network traffic.

# 2.2. Auto-Encoder Related Work 

Regarding using Auto-Encoder for dimensionality reduction, authors in [20] proposed a framework for IDS using a Stacked Auto Encoder (SAE), which is an unsupervised learning method for attribute selection. Their framework used regression layer, a supervised learning technique, with SoftMax activation function for the classification process.

The authors in [21] developed an intrusion detection system for wireless sensor networks using Deep Auto-Encoder (DAE) as the basic classifier to the detect attack type. The authors used a cross-entropy loss function and back-propagation algorithm in an attempt to prevail over the slow update of the weights in the case of traditional varying cost functions with exponential costs [21].

The authors in [22] used Sparse Auto-Encoder (SAE) for feature learning and dimensionality reduction on the NSL-KDD dataset [23], which is an enhanced version of KDD-CUP99 [24]; an old, outdated synthetic netflow dataset. The authors used Support Vector Machines (SVM) and achieved an accuracy of $84.96 \%$ in binary classification and $99.39 \%$ in multi-class classification of five classes. In our work, we used CICIDS2017, which is an up-to-date dataset that accommodates new attacks and intruder strategies. Moreover, the total instances of the NSL-KDD is 125,923 in training and 22,544 instances in testing. This is while CICIDS2017 has 2,830,108 instances and is generated based on real network traffic.

In the same manner, ref. [25] proposed a system based on the same methodology of [22]. The authors in [25] used SAE with SVM on the NSL-KDD dataset. The framework of [25] achieved $88.39 \%$ accuracy in binary classification and $79.10 \%$ in five class classification.

The authors in [26] proposed SU-IDS; a semi-supervised and unsupervised network intrusion detection system that used an auto-encoder-based framework. The framework augments the usual clustering (or classification) loss with an auxiliary loss of auto-encoder, and thus achieves a better performance. A comparison between the experimental results of the classic NSL-KDD dataset and the modern CICIDS2017 dataset show the superiority of our proposed models.

### 2.3. PCA Related Work

The authors in [27] implemented an IDS that used Principal Component Analysis (PCA) as the feature reduction approach and Grey Neural Networks (GNN) as the classifier on the KDD-99 dataset.

In the same context, ref. [27] used PCA for features reduction and decision tree and Nearest Neighbor as classifiers on KDD-99.

The researchers in [28] defined the reduction rate and studied the efficiency of PCA for intrusion detection. The authors fulfilled their experiments using Random Forest and C4.5 on KDD-CUP [24] and UNB-ISCX [29].

## 3. CICIDS2017 Dataset

The CICIDS2017 dataset consists of realistic background traffic that represents the network events produced by the abstract behavior of a total of 25 users. The users' profiles were determined to include specific protocols such as HTTP, HTTPS, FTP, SSH and email protocols. The developers used statistical metrics such as minimum, maximum, mean and standard deviation to encapsulate the network events into a set of certain features which include:

1. The distribution of the packet size
2. The number of packets per flow
3. The size of the payload
4. The request time distribution of the protocols
5. Certain patterns in the payload

Moreover, CICIDS2017 covers various attack scenarios that represent common attack families. The attacks include Brute Force Attack, HeartBleed Attack, Botnet, DoS Attack, Distributed DoS (DDoS) Attack, Web Attack, and Infiltration Attack.

The dataset is publicly available by the authors in two formats:

1. The full packet payloads in Packet CAPture (PCAP) format
2. The corresponding profiles and labeled flows as CSV files for machine and deep learning purposes

CICIDS2017 was collected based on real traces of benign and malicious activities of the network traffic. The total number of records in the dataset is $2,830,108$. The benign traffic encompasses 2,358,036 records ( $83.3 \%$ of the data), while the malicious records are $471,454(16.7 \%$ of the data). CICIDS2017 is one of the unique datasets that includes up-to-date attacks. Furthermore, the features are exclusive and matchless in comparison with other datasets such as UNSW-NB15 [30,31], AWID [32], GPRS [33], and CIDD-001 [34]. For this reason, CICIDS2017 was selected as the most comprehensive IDS benchmark to test and validate the proposed ideas. Table 2 highlights the characteristics and distribution of the attacks in the CICIDS2017 dataset and provides a brief description of each type of attack. CICIDS2017 is a labeled dataset with a total number of 84 features including the last column corresponding to the traffic status (class label). The features were extracted by CICFlowMeter-V3 [35]. The output of CICFlowMeter-V3 is a CSV file that includes: Flow ID (1), Source IP (2) and Destination IP (4), Time stamp (7) and Label (84). The Flow ID (1) includes the four tuples : Source IP, Source Port, Destination IP, and Destination Port. Time stamp represents the timing. To the best of our knowledge, all previous studies that used CICIDS2017 neglect Flow ID (1), Source IP (2), Destination IP (4), and Time stamp (7). In this paper, we used CICIDS2017 with respect to the listed features except the Flow ID (1) and Time Stamp (7). Thus, in our study, the total number of used features encompasses 82 features including the Label (84). These features are listed in Table 3. The extracted traffic features are explained in [36].

Table 2. CICIDS2017 attack distribution and description.


Table 3. Listed features of network traffic in CICIDS2017.


# 3.1. Preprocessing 

In this study, a preprocessing function is applied to the CICIDS2017 dataset by mapping the IP (Internet Protocol) address to an integer representation. The mapped IP includes the Source IP Address (Src IP) as well as the Destination IP Address (Dst IP). These two are converted to an integer number representation. This study splits the data into training set and testing set with a ratio of 70:30.

### 3.2. Unity-Based Normalization

In this step, we use Equation (1) to re-scale the features in the dataset based on the minimum and maximum values of each feature. Some features in the original dataset vary between [0,1] while other features vary between $[0, \infty)$. Therefore, these features are normalized to restrict the range of the values between 0 and 1 , which are then processed by the auto-encoder for feature reduction.

$$
x_{i}=\frac{x_{i}-x_{\min }}{x_{\max }-x_{\min }}
$$

where $x_{i}$ is the value of a particular feature, $x_{\min }$ is the minimum value, and $x_{\max }$ is the maximum value.

## 4. Features Dimensionality Reduction

### 4.1. Auto-Encoder (AE) Based Dimensionality Reduction

In this section, we present the sparse auto-encoder learning algorithm [37,38], which is one approach to automatically learn feature reduction in unsupervised settings. Figure 2 shows the structure of the auto-encoder. The input vector $x=\left(x_{1}, x_{2}, \ldots, x_{n}\right)$ is first compressed to a lower dimensional hidden representation that consists of one or more hidden layers $a=\left(a_{1}, a_{2}, \ldots, a_{m}\right)$.

The hidden representation $a$ is then mapped to reproduce the output $\hat{x}=\left(\hat{x_{1}}, \hat{x_{2}}, \ldots, \hat{x_{n}}\right)$. Let $j$ be the counter parameter for the neurons in the current layer $l$, and $i$ be the counter parameter for the neurons in the previous hidden layer $l-1$. The output of a neuron in the hidden layer can be represented by the following formula.

$$
a_{j}^{(l)}=f\left(z_{j}^{(l)}\right)=f\left(\sum_{i=1}^{n} W_{j i}^{(l-1)} \cdot a_{i}^{(l-1)}+b_{j}^{(l-1)}\right)
$$

![img-1.jpeg](img-1.jpeg)

Figure 2. The structure of an AE.
The size of the weight matrix of the hidden layer is represented by $W \in R^{m \times n}$ and the bias is $b \in R^{m}$. A sigmoid function is chosen as the activation function, such that $f(z)=\frac{1}{\left(1+\exp ^{-z}\right)}$. Parameters $W$ and $b$ are optimized using back propagation, by minimizing the cost function $J$ for all the training instances [39], as follows:

$$
J(W, b ; \hat{x}, x)=\frac{1}{k} \sum_{i=1}^{k}\left(\frac{1}{2}\|\hat{x}-x\|^{2}\right)+\frac{1}{\lambda} \sum_{l=1}^{l s-1} \sum_{j=1}^{m} \sum_{i=1}^{n}\left(W_{j i}^{(l)}\right)^{2}
$$

Parameter $\lambda$ is chosen to control the regularization term of all the weights in a particular layer, and Is denotes the total number of layers. To impose a sparsity constraint on the hidden units, one strategy is to add an additional term in the loss function during training to penalize the Kullback-Leibler (KL) divergence between a Bernoulli random variable with mean $\rho$ and a desired sparsity mean $\hat{\rho}_{j}$.

$$
\hat{\rho}_{j}=\frac{1}{k} \sum_{i=1}^{k}\left[a_{j}^{(i)}\left(x^{(i)}\right)\right]
$$

where $a_{j}^{(i)}$ denotes the activation of hidden unit $j$ in the auto-encoder and $k$ is the training sample [40].

$$
J_{\text {sparse }}(W, b)=J(W, b ; \hat{x}, x)+\beta \sum_{j=1}^{m} K L\left(\rho \| \hat{\rho}_{j}\right)
$$

This sparsity is guaranteed to have the effect of causing $\hat{\rho}_{j}$ to be close to $\rho$, because it ensures that the sparse activations are achieved on the training data for any given units in the hidden layer. The value of $\beta$ is chosen to control the weight of the sparsity penalty term.

The computational complexity of executing the designed auto-encoder with a single hidden layer depends on the dimensionality of the input vector $n$, and the Reduction ratio $R \in(0,1)$ [41].

$$
O(n .(R \times n)+(R \times n) \cdot n)=O\left(R n^{2}+R n^{2}\right)=O\left(n^{2}\right)
$$

In this paper, a two hidden-layer sparse auto-encoder is used with sigmoid activation functions and tied weights. The input layer has 81 neurons which equals the total number of features in the CICIDS2017 dataset. The first hidden layer of the sparse auto-encoder was able to successfully reduce the dimensions to 70 features with a good error approximation. Further, the features were reduced to 64 in the second hidden layer. Once the weights are trained, the resulting sparse auto-encoder can be used to perform the classification in the final stage. The parameters of the sparse representation are set as follows: the weight decay $\lambda=0.0008$. The weights are multiplied by $\lambda$ to prevent the weights from growing too large. The sparsity parameter $\rho=0.05$, and the sparsity penalty term $\beta=6$. The sparsity parameters and penalty are designed to restrict the activation of the hidden units, which reduces the dependency between the features. The algorithm is summarized in Table 4 and the design principles are presented in Table 5.

Table 4. Pseudo-code for the proposed Auto-Encoder.


Table 5. Design Principles.


# 4.2. Principle Component Analysis (PCA) Based Dimensionality Reduction 

In this section, we present the Principle Component Analysis (PCA) algorithm. The objective of PCA is to perform dimensionality reduction. PCA finds a transformation that reduces the dimensionality of the data while accounting for as much variance as possible. PCA is the oldest technique in multivariate analysis. The fundamental concept of the PCA is the projection-based mechanism. Here, the original dataset $X \in R^{n}$ with $n$ columns (features) is projected into a subspace with $k$ or lower dimensions representation $X \in R^{K}$ (fewer columns), while retaining the essence of the original data. The algorithm works as follows:

To reduce the features dimensionality from $n$-dimensions to $k$-dimensions, two phases are implemented; the preprocessing phase and the dimensionality reduction phase. In the preprocessing phase, (steps 1 through 4 below), the data is preprocessed to normalize its mean and variance using Equations (7) and (8). In the second phase (steps 5 through 8), which represent the reduction phase, the covariance matrix $\operatorname{Cov}_{M}$, Eigen-vectors and Eigen-values are calculated from Equations (9) and (10).

1. Normalize the the original feature values of data by its mean and variance using Equation (7), where $m$ is the number of instances in the dataset and $X_{(i)}$ are the data points.

$$
\mu=\frac{1}{m} \sum_{i=1}^{m} X_{(i)}
$$

2. Replace $X_{(i)}$ with $X_{(i)}-\mu$.
3. Rescale each vector $X_{j(i)}$ to have unit variance using Equation (8).

$$
o_{j}^{2}=\frac{1}{m} \sum_{i}\left(X_{j(i)}\right)^{2}
$$

4. Replace each $X_{j(i)}$ with $\frac{X_{j(i)}}{\mu}$.
5. Compute the Covariance Matrix $\operatorname{Cov}_{M}$ as follows:

$$
\operatorname{Cov}_{M}=\frac{1}{m} \sum\left(X_{(i)}\right)\left(X_{(i)}\right)^{\top}
$$

6. Calculate the Eigen-vectors and corresponding Eigen-values of $\operatorname{Cov}_{M}$.
7. Sort the Eigen-vectors by decreasing the Eigen-values and choose $k$ Eigen-vectors with the largest Eigen-values to form $W$.
8. Use $W$ to transform the samples onto the new subspace using Equation (10).

$$
y=W^{T} \times X
$$

where $X$ is a $d \times 1$ dimensional vector representing one sample, and $y$ is the transformed $k \times 1$ dimensional sample in the new subspace.

The computational complexity of executing the designed PCA depends on the number of features $P$ that represent each data point [42].

$$
O\left(P^{3}\right)
$$

According to [28], the Reduction Ratio (RR) of PCA can be defined as the ratio of the number of target dimensions to the number of original dimensions. The lower the value of $R R$, the higher is the efficiency of PCA. The RR of our proposed framework is equal to 10:81 which outperformed previous related work. Our final RR of 2:81 is also able to represent the data with low error and provide high accuracies.

# 5. Performance Evaluation Metrics 

This study used various performance metrics to evaluate the performance of the proposed system, including False Alarm Rate (FAR), F-Measure [43], Detection Rate (DR), and Accuracy (Acc) as well as the processing time. The definitions of these metrics are provided below. The metrics are a function of True Positives (TP), True Negatives (TN), False Positives (FP) and False Negatives (FN).
(1) False Alarm Rate (FAR) is a common term which encompasses the number of normal instances incorrectly classified by the classifier as an attack, and can be estimated through Equation (12).

$$
F A R=\frac{F P}{T N+F P}
$$

(2) Accuracy (Acc) is defined as the ability measure of the classifier to correctly classify an object as either normal or attack. The Accuracy can be defined using Equation (13).

$$
A c c=\frac{T P+T N}{T P+T N+F P+F N}
$$

(3) Detection Rate (DR) indicates the number of attacks detected divided by the total number of attack instances in the dataset. DR can be estimated by Equation (14).

$$
D R=\frac{T P}{T P+F N}
$$

(4) The F-measure (F-M) is a score of a classifier's accuracy and is defined as the weighted harmonic mean of the Precision and Recall measures of the classifier. F-Measure is calculated using Equation (15).

$$
\text { F-Measure }=2 \times \frac{\text { Precision } \times \text { Recall }}{\text { Precision }+ \text { Recall }}
$$

(5) Precision represents the number of positive predictions divided by the total number of positive class values predicted. It is considered as a measure for the classifier exactness. A low value indicates large number of False Positives. The precision is calculated using Equation (16).

$$
\text { Precision }=\frac{T P}{T P+F P}
$$

(6) Recall is the number of True Positives divided by the number of True Positives and the number of False Negatives. Recall is considered as a measure of a classifier completeness such that a low value of recall realizes many False Negatives [44]. Recall is estimated through Equation (17).

$$
\text { Recall }=\frac{T P}{T P+F N}
$$

# 5.1. Proposed Multi-Class Combined Performance Metric with Respect to Class Distribution 

In general, the overall accuracy is used to measure the effectiveness of a classifier. Unfortunately, in presence of imbalanced data, this metric may fail to provide adequate information about the performance of the classifier. Furthermore, the method is very sensitive to the class distribution and might be misleading in some way. Hamed et al. [45] proposed a combined performance metric to compare various binary classifier systems. However, their solution neglects class distribution and can work only for binary classifications.

In this paper, we propose the multi-class combined performance metric Combined $_{M c}$ with respect to class distribution to compare various multi-class classification systems as well as binary class systems through incorporating four metrics together (FAR Equation (12), Accuracy Equation (13), Detection Rate Equation (14), and class distribution Equation (19). The multi-class Combined performance metric can be estimated using the following equation.

$$
\text { Combined }_{M c}=\sum_{i=1}^{C} \lambda_{i}\left(\frac{A c c_{i}+D R_{i}}{2}-F A R_{i}\right)
$$

where $C$ is number of classes, and $\lambda_{i}$ is the class distribution (dist), which can be estimated using the following formula.

$$
\text { dist }=\lambda_{i}=\frac{\text { Number of instances in class } i}{\text { Number of instances in the dataset }}
$$

The result of this metric will be a real value between -1 and 1 ; that is Combined $_{M c} \in[-1,+1]$; where -1 corresponds to the worst overall system performance and 1 corresponds to the best overall system performance. Table 6 illustrates the pseudo-code for calculating this proposed combined metric.

Table 6. Pseudo-code for the proposed Combined $_{M c}$ metric calculation.


# 6. Uniform Distribution Based Balancing (UDBB) 

The problem of learning from skewed multi-class datasets is an important topic that arises very often in practice in classification problems. In such problems, almost all the instances are labeled as one class (called the majority, or negative class), while far fewer instances are labeled as the other class or classes (often called the minority class(es), or positive class(es)); usually the more important class(es). This section provides a glance at the Uniform Distribution Based Balancing (UDBB) technique. UDBB is based on learning and sampling probability distributions [46]. In this technique, the sampling of instances is performed following a distribution learned for each pair example of feature and class label. More specifically, the user determines the uniform distribution balancing to learn in order to re-sample new instances.

According to [44], the Imbalance Ratio (IR) can be defined as the ratio of the number of instances in the majority class to the number of instances in the minority class, as presented in Equation (20).

$$
\text { Imbalance Ratio }=\frac{\text { Majority Class Instances }}{\text { Minority Class Instances }}
$$

For the CICIDS2017 dataset, IR is 5:1 and the total number of classes is 15 classes. To apply UDBB, a uniform number of instances $\left(I_{\text {Resample }}\right)$ for each class is calculated from Equation (21).

$$
I_{\text {Resample }}=\frac{\text { Number of Instances in the dataset }}{\text { Number of Classes in the dataset }}
$$

The literature indicates that imbalanced class distribution is a major hurdle. If the IR value in the data is high, classifiers will be lower in accuracy and reliability; i.e., they do not truly reflect the classes accurately. Furthermore, imbalanced class distributions is an inevitable problem in real network traffic due to the large size of traffic and low frequency of certain types of anomalies. One of the recent attempts to address this problem appears in [47]. The authors used sampling approaches to combat imbalanced class distributions for network intrusion detection.

Previous developers that used CICIDS2017, used files that were relevant to Tuesday through Friday. In this paper, we use these along with the data of Monday by merging all files together in a single combined file. The motivation behind this step is to acquire a large volume of both data size and number of instances with skewed data towards normal traffic and up-to-date attack patterns. Table 7 presents a pseudo-code for the UDBB technique. In addition, our study compares between the imbalanced case (with original distribution of CICIDS2017) and balanced class distribution (after applying the uniform distribution-based balancing approach).

Table 7. UDBB pseudo-code.

```
Input Training Set: \(D_{\text {Train }}\)
Set Distribution to Uniform
C : Number of Classes
\(F_{T}\) : Total number of features in \(D_{\text {Train }}\) Training Set
\(I_{\text {old }}:\) Total number of Instances in \(D_{\text {Train }}\)
Calculate the required number of Instances in each class: \(I_{\text {Resample }}\)
```

Training Set $D_{\text {Train }_{\text {sovo }}}=\varnothing$
For each class $C_{i}$ Do
While $i \neq I_{\text {Resample }}$
For each feature $F_{1}, \ldots, F_{T}$
Generate new sample using uniform distribution
Assign Class label
Return $D_{\text {Train }_{\text {sovo }}}$

# 7. Results and Discussion 

In this section, we present the principal findings of the proposed framework.Extensive simulations have been performed.

### 7.1. Preliminary Assumptions and Requirements

All the simulations were carried out using an Intel-Core i7 with 3.30 GHz and 32 GB RAM, running Windows 10. Our main hypothesis is that reduced features dimensions representation in machine learning-based IDS will reduce the time and memory complexity compared to the original features dimensions, while still maintaining high performance (not negatively impacting the achieved accuracy). Another hypothesis claim is that the proposed balancing technique improves the data representation of imbalanced classes and thus, improves the classification performance compared to the original class distributions. The results highlight the advantages of feature dimensionality reduction on CICIDS2017 as well as the effectiveness of the balancing approach to prove the hypothesis claims.

From the research efforts in this work, we were able to reduce the dimensionality of the features in CICIDS2017 from 81 features to 10 features while maintaining a high accuracy in multi-class and binary class classification using the Random Forest classifier. The findings are discussed in following subsections.

### 7.2. Binary class Classification

The study evaluates the performance of binary classification in terms of Acc, FAR, DR and F-M. Tables 8 and 9 display the summary of the results obtained. Table 8 highlights the results of the dimensionality reduction of the features in CICIDS2017 from 81 features to 10 features obtained using PCA, whereas Table 9 displays the results of the dimensionality reduction of the features in CICIDS2017 from 81 features to 59 features using AE.

The DR metric revealed that $(P C A-R F)_{B c-10}$ is able to detect $98.8 \%$ of the attacks. In the same manner, $(P C A-R F)_{B c-10}$ achieved an F-Measure of 0.997 . Moreover, $(A E-R F)_{B c-59}$ is able to detect $98.5 \%$ of the attacks.

Figure 3 highlights the achieved detection rates resulted from the dimensionality reduction using PCA, whereas, Figure 4 shows the achieved detection rate using the reduced features set by AE. From Figures 3 and 4, it is apparent that Random forest, QDA and Bayesian Network reported significantly higher detection rates than the LDA for the reduced feature dimensionality of CICIDS2017 using the PCA approach. The results from the classification using different classifiers assures that our reconstructing of new feature representation was good enough to achieve an overall accuracy of $98.5 \%$ with 59 features in binary classification using Random Forest from AE.

![img-2.jpeg](img-2.jpeg)

Figure 3. Binary Class Classification: Detection Rate in terms of number of components using PCA.


Table 9. Performance evaluation of the proposed framework in binary classification using AE.


# 7.3. Multi-Class Classification 

The study used the Acc, F-M, FPR, TPR, Precision, Recall, and the Combined multi-class metrics to evaluate the performance of multi-class classification. Tables 10 and 11 display the summary of the results obtained for the dimensionality reduction of the features for CICIDS2017 from 81 to 10 using PCA, and from 81 to 59 using AE, respectively.

Table 10. Performance evaluation of the proposed framework in multi-class classification using PCA.


Table 11. Performance evaluation of the proposed framework in multi-class classification using AE.


Figure 5 presents the resulting accuracies in terms of the number of principle components. What is striking about the resulting accuracies in Figure 5 is that the Random Forest classifier shows a constantly high accuracy for reduced features from 81 through 10. In contrast, the resulting accuracies of LDA and QDA cases were oscillatory. For QDA, the accuracy is wobbling between $66 \%$ with 10 features and $96.7 \%$ with 60 features. For LDA with 10 and 40 features, the accuracy is fluctuating between $85 \%$ and $96.6 \%$, respectively.

The results of the AE dimensionalty reduction approach are displayed in Figure 6. The observed accuracy for Random Forest is significant compared to LDA, QDA and the Bayesian Network classifiers. Furthermore, what stands out in this Figure 6, is the increase of the resulting accuracy for LDA for the reduced dimensionality from 81 through 59 features. Here, the AE reconstructed a new and reduced feature representation pattern that reflects the original data with minimum error. Unlike features selection techniques where the set of features made by feature selection is a subset of the original set of features that can be identified precisely, AE generated new features pattern with reduced dimensions.

![img-3.jpeg](img-3.jpeg)

Figure 5. Multi Class Classification: Accuracy in terms of number of components using PCA.
![img-4.jpeg](img-4.jpeg)

Figure 6. Multi Class Classification: Accuracy in terms of number of features using AE.
A detailed analysis summary of the proposed framework in terms of False Positive Rate (FPR), True Positive Rate (TPR), Precision and Recall are tabulated in Tables 12 and 13. Table 12 depicts the results with 10 features (before applying UDBB), while Table 13 shows the results using 10 features (after applying UDBB). The weighted average result for all the attacks are presented in bold.

Table 12. Performance evaluation before applying UDBB.


Table 13. Performance evaluation after applying UDBB.


The results confirmed that the proposed framework with the reduced feature dimensionality achieved a maximum precision value of 0.996 and an FPR of 0.010 , confirming the efficiency and effectiveness of the intrusion detection process. However, $(P C A-R F)_{M c-10}$ is unable to detect the HeartBleed attacks (noted as NAN in Table 12). In this Table, the Recall and Precision values for HeartBleed and WebAttack:SQL are $0.00,0.000$ and $0.000,0.000$, respectively. A justification of such outcome could be due to the fact that the number of instances of HeartBleed and WebAttack:SQL originally embedded in CICIDS2017 is equal to 11 and 21, respectively. This is expected, since the total number of HeartBleed instances in the original dataset is 11 instances. Thus, these instances were miss-classified by the classifier. To resolve this issue and to assure that the achieved accuracy is reflected due to the effective reduction approach, this paper applies the uniform distribution-based balancing technique to overcome the imbalanced class distributions of certain attacks in CICIDS2017. Table 14 shows the performance before and after applying the UDBB approach. As observed, $(P C A-R F)_{M c-10}$ achieved $99.6 \%$ and $98.8 \%$ before and after applying UDBB, respectively. In the same manner, $(P C A-$

$\left.Q D A\right)_{M c-10}$ achieved $85.6 \%$ and $98.9 \%$ before and after applying UDBB, respectively. The highest achieved F-M was obtained by $(P C A-Q D A)_{M c-10}$. However, the highest $C M_{(M c)}$ achieved was $98.6 \%$ by $(P C A-R F)_{M c-10}$.

The performance evaluation of $(P C A-X)_{B c-10}$ and $(P C A-X)_{M c-10}$ in terms of the time to build and test the model is presented in Table 15 ( $X$ represents the classifier). The lowest times to test the model were achieved by LDA with 2.96 s for multi-class and 5.56 s for binary class classification.

Here, the Random Forest classifier that has the best detection performance, comes with the highest overhead in terms of the time to build and test the model. The fundamental notion behind Random Forest is that it combines many decision trees into a single model and specifically in this work, the dataset has over 2.5 million instances in total. This is expected since the worst case time complexity of Random Forest is estimated using Equation (22) [48].

$$
O\left(M K N^{2} \log N\right)
$$

where $K$ is the number of trees, $M$ is the number of variables used in each split, and $N$ is the number of training samples.

Table 14. Performance evaluation of $(P C A-X)_{M c-10}$.


Table 15. Time to build and test the models.


Moreover, a visualization of the dataset with two PCA components before and after applying the distribution-based balancing approach is displayed in Figures 7 and 8.

This observation of the CICIDS2017 dataset visually represents how the instances are set apart. As displayed in Figure 8, the same type of instances were positioned (clustered) together in groups. This shows a significant improvement over the PCA visualization before applying UDBB. Here, the normal instances are very clearly clustered in their own group. This is applied for other types of instances as well.

![img-5.jpeg](img-5.jpeg)

Figure 7. 2D Visualization of PCA on CICIDS2017 with original distribution.
![img-6.jpeg](img-6.jpeg)

Figure 8. 2D Visualization of PCA on CICIDS2017 with UDBB.

The confusion matrix for the $P C A-R F_{M c-10}$ is shown in Figure 9. The value for HeartBleed is reported as NAN (Not A Number). These values result from operations which have undefined numerical values. The classifier $P C A-R F_{M c-10}$ fails to classify HeartBleed attacks. In contrast, as a result of applying the UDBB technique, the $P C A-R F_{M c-10}$ is able to detect $100 \%$ of HeartBleed attacks, as indicated from the confusion matrix in Figure 10.

A comparison between the proposed framework and related work is highlighted in Table 16. The authors in [17,49,50] reported the accuracy. Our proposed framework outperforms previous studies in terms of F-Measure and accuracy.

Table 16. A comparison of the proposed framework and previous studies.


![img-7.jpeg](img-7.jpeg)

**Figure 9.** Confusion Matrix for (*PCA* − *RF*)*<sub>Mc</sub>*<sup>−10</sup>* with original class distribution.

![img-8.jpeg](img-8.jpeg)

**Figure 10.** Confusion Matrix for (*PCA* − *RF*)*Mc*−10 with UDBB.

# 8. Challenges and Limitations 

Although this study has successfully demonstrated the significance of the feature dimensionality reduction techniques which led to better results in terms of several performance metrics as well classification speeds for an IDS, it has certain limitations and challenges which are summarized as follows.

### 8.1. Fault Tolerance

Fault tolerance enables a system to continue operating properly in the event of failure or faults within any of its components. Fault tolerance can be achieved through several techniques. One aspect of fault tolerance in our system is the ability of the designed approach to detect a large set of well-known attacks. Our models have been trained to detect the 14 up-to-date and well-known type of attacks. Furthermore, fault tolerance can be achieved by adopting the majority voting technique [52]. The trained models of Random Forest, Bayesian Network, and LDA can be used in a majority voting-based intrusion detection system that can adapt fault tolerance. Moreover, the deployment of distributed intrusion detection systems in the network can enable fault tolerance.

### 8.2. Adaption to Non-Stationary Traffic/Nonlinear Models

The AE has the ability to represent models that are linear and nonlinear. Moreover, once the model is trained, it can be used for non-stationary traffic. We intend to further extend our work in the future with an online anomaly-based intrusion detection system.

### 8.3. Model Resilience

As presented in Tables 12 and 13, the achieved FP rate is 0.010 and 0.001 respectively, which may reflect a built-in attack resiliency. Moreover, our models were trained in an offline manner. This ensures that an adversary cannot inject misclassified instances during the training phase. On the contrary, such case could occur with online-trained models. Therefore, it is essential for the machine learning system employed in intrusion detection to be resilient to adversarial attacks [53]. An approach to quantify the resilience of machine learning classifiers was introduced in [53]. The association of these factors will be investigated in future studies.

### 8.4. Ease of Dataset Acquisition/Model Building

The data used for our IDS model was acquired from the CICIDS2017 dataset which is a publicly available dataset provided by the Canadian Institute for Cybersecurity [35,36]. The dataset is open source and available for download and sharing.

### 8.5. Quality of Experience

According to [54], the Quality of Experience is used to measure and express, preferably as numerical values, the experience and perception of the users with a service or application software. The current research was not specifically designed to evaluate factors related to Quality of Experience. Future directions of this research may include such investigations.

## 9. Conclusion and Future Work

The aim of this research was to examine incorporating auto-encoder and PCA for dimensionality reduction and the use of classifiers towards designing an efficient network intrusion detection system on the CICIDS2017 dataset. The experimental analysis confirmed the significance of the feature dimensionality reduction techniques which led to better results in terms of several performance metrics as well as classification speeds. These findings highlight the potential usefulness of auto-encoder and PCA in dimensionality reduction for IDS. From our experiments, we found that PCA is superior, faster, more interpretable and can reduce the dimensionality of the data to as few as two components.

The long training time and limited computational resources formed a barrier towards reducing the dimensionality beyond 59 features representation for the AE approach. This study suggests that AE can be used when the data necessitates a highly non-linear feature representation.

The large number of decision trees that the Random Forest classifier produced by randomly selecting a subset of training samples and a subset of variables for splitting at each tree node, makes the Random Forest classifier less sensitive to both the quality of training instances as well as the overfitting issue. Moreover, Random Forest is suitable, robust, and stable to classify high dimensional and correlated data. These explanations provide a justification as to why Random Forest yielded better results in comparison with other classifiers [55].

As exemplified by the obtained results, the PCA approach is able to preserve important information in CICIDS2017, while efficiently reducing the features dimensions in the used dataset, as well as presenting a reasonable visualization model of the data. Features such as Subflow Fwd Bytes, Flow Duration, Flow Inter arrival time (IAT), PSH Flag Count, SYN Flag Count, Average Packet Size, Total Len Fwd Pck, Active Mean and Min, ACK Flag Count, and Init_Win_bytes_fwd are observed to be the discriminating features embedded in CICIDS2017 [4]. Regarding this study, PCA was very efficient and produced better results than AE. In comparison with AE, the PCA approach is restricted to a linear mapping, whereas the AE can have a nonlinear encoder/decoder architecture.

As a future direction, this research will also serve as a base for further studies and investigations towards developing efficient IDS's from various intrusion detection datasets. Furthermore, the trained models could be extended to implement an IDS for online anomaly-based detection.

Author Contributions: Supervision, M.F. and A.A. (Abdelshakour Abuzneid); Writing—original draft, R.A.; Writing—review \& editing, M.F., A.A. (Abdelshakour Abuzneid) and R.A.; Data Preprocessing, R.A. and A.A. (Ali Alessa); Software, R.A. and H.M.; Methodology, R.A.; Project Administration A.A. (Abdelshakour Abuzneid) and M.F.
Funding: This research was funded by the University of Bridgeport Seed Money Grant UB-SMG-2018.
Conflicts of Interest: The authors declare no conflict of interest.

# Abbreviations 

The following abbreviations are used in this manuscript:


