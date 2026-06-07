# ECG arrhythmia classification based on optimum-path forest 

Eduardo José da S. Luz ${ }^{\text {a }}$, Thiago M. Nunes ${ }^{\text {b }}$, Victor Hugo C. de Albuquerque ${ }^{\text {c }}$, João P. Papa ${ }^{\text {d }}$, David Menotti ${ }^{\text {a,* }}$<br>${ }^{a}$ Universidade Federal de Ouro Preto, Computing Department, Ouro Preto, MG, Brazil<br>${ }^{\mathrm{b}}$ Universidade Federal do Ceará, Teleinformatic Engeneering Department, Fortaleza, CE, Brazil<br>${ }^{\text {c }}$ Universidade de Fortaleza, Post-Graduate Program in Applied Informatics, Fortaleza, CE, Brazil<br>${ }^{\mathrm{d}}$ Universidade Estadual Paulista, Computer Science Department, Bauru, SP, Brazil

## A R T I C L E I N F O

Keywords:
ECG classification
Feature extraction
Optimum-path forest
Support vector machine
Bayesian
Multilayer artificial neural network

## A B S T R A C T

An important tool for the heart disease diagnosis is the analysis of electrocardiogram (ECG) signals, since the non-invasive nature and simplicity of the ECG exam. According to the application, ECG data analysis consists of steps such as preprocessing, segmentation, feature extraction and classification aiming to detect cardiac arrhythmias (i.e., cardiac rhythm abnormalities). Aiming to made a fast and accurate cardiac arrhythmia signal classification process, we apply and analyze a recent and robust supervised graphbased pattern recognition technique, the optimum-path forest (OPF) classifier. To the best of our knowledge, it is the first time that OPF classifier is used to the ECG heartbeat signal classification task. We then compare the performance (in terms of training and testing time, accuracy, specificity, and sensitivity) of the OPF classifier to the ones of other three well-known expert system classifiers, i.e., support vector machine (SVM), Bayesian and multilayer artificial neural network (MLP), using features extracted from six main approaches considered in literature for ECG arrhythmia analysis. In our experiments, we use the MIT-BIH Arrhythmia Database and the evaluation protocol recommended by The Association for the Advancement of Medical Instrumentation. A discussion on the obtained results shows that OPF classifier presents a robust performance, i.e., there is no need for parameter setup, as well as a high accuracy at an extremely low computational cost. Moreover, in average, the OPF classifier yielded greater performance than the MLP and SVM classifiers in terms of classification time and accuracy, and to produce quite similar performance to the Bayesian classifier, showing to be a promising technique for ECG signal analysis.
(c) 2012 Elsevier Ltd. All rights reserved.

## 1. Introduction

The electrocardiogram (ECG) is the most widely used non-invasive technique in heart disease diagnoses. Since it reflects the electrical activity within the heart during contraction, the time it occurs as well as it shape provide much information about the state of the heart. (Fig. 1 shows a schematic record of a normal heartbeat, in which we can observe the fiducial points $\mathrm{P}, \mathrm{Q}, \mathrm{R}, \mathrm{T}$ and $U$ ). The ECG is frequently used to detect cardiac rhythm abnormalities, also known as arrhythmias, which can be defined in two ways: (i) as a unique irregular cardiac beat or (ii) as a set of irregular beats. Arrhythmias can be rare and harmless, but may also re-

[^0]sult in serious cardiac issues. Some group of arrhythmias are lifethreatening and require immediate care and often an intervention with defibrillator. Other types of arrhythmias, those that do not require instantaneous attention, may require treatment to prevent further problems, and should be detected as well (University of Maryland Medical Center, 2012).

There are several methods proposed in the literature for the purpose of automatic arrhythmia classification in ECG signals, and a complete system for such an aim can be divided into four subsequent categories (preprocessing, segmentation, feature extraction, and classification) as shown in Fig. 2, in which A, B, C and D illustrate fictitious heartbeat classes to be analyzed.

The preprocessing phase consists mainly in detecting and attenuating frequencies of the ECG signal related to artifacts. Those artifacts can be from a biological source, like muscular activity, or originated from an external source, such as $50 / 60 \mathrm{~Hz}$ electric network frequency. It is also desired, in the preprocessing, to perform a signal normalization and complex QRS (wave) enhancement (the most salient part of a heartbeat), in order to help the segmentation process.


[^0]:    * Corresponding author. Address: Universidade Federal de Ouro Preto, Computing Department, 35.400-000 Ouro Preto, MG, Brazil. Tel.: +55 313559 1692; fax: +55 31 35591660 .

    E-mail addresses: eduluz@gmail.com (Eduardo José da S. Luz), tmnun@hotmail. com (T.M. Nunes), victor120585@yahoo.com.br (Victor Hugo C. de Albuquerque), papa@fc.unesp.br (J.P. Papa), menottid@gmail.com, menotti@iceb.ufop.br (D. Menotti).

![img-0.jpeg](img-0.jpeg)

**Fig. 1.** A normal heartbeat ECG signal.

![img-1.jpeg](img-1.jpeg)

**Fig. 2.** A diagram of a classification system of arrhythmia.

ECG signals segmentation consists in delimitating the part of the signal of more interest, the QRS complex, since it reflects the major part of the electrical activity of the heart (see Fig. 1). Once the segmentation of QRS complex is done one can obtain many physiological information, such as, for example, heart rate signal acquisition, in which will be used techniques to feature selection in order to eliminate redundant features from the primary feature set.

Feature extraction is the key point for the final classification performance. Features can be extracted directly from ECG waveform morphology in time or frequency domain. Many sophisticated computational methods have been considered in order to find features less sensitive to noise, such as the autoregressive model coefficients (Llamedo & Martínez, 2011), higher-order cumulant (higher order statistics) (Mehmet, 2004) and variations of wavelet transform (Addison, 2005; Özbay, 2009; Sayadi & Shamsollahi, 2007).

This work focuses mainly on the last step of cardiac arrhythmia analysis, i.e., ECG signal classification. A large number of approaches have been proposed for this task, and the popular ones are statistical approaches based on Linear Discriminants (Chazal, O'Dwyer, & Reilly, 2004), k-Nearest Neighbors (kNN) (Lanatá, Valenza, Mancuso, & Scilingo, 2011), Bayesian probabilities (Wiggins, Saad, Litt, & Vachtsevanos, 2008), artificial neural networks (ANNs) (Ceylan & Özbay, 2007; Korürek & Dogan, 2010; Özbay, 2009; Yu & Chen, 2007; Yu & Chou, 2008), support vector machines (SVMs) (Lin, Ying, Chen, & Lee, 2008b; Moavenian & Khorrami, 2010; Song, Lee, Cho, Lee, & Yoo, 2005; Ye, Coimbra, & Kumar, 2010; Yu & Choua, 2009), among others. We also find in the literature works based on ECG signal clustering analysis (Ceylan, Özbay, & Karlik, 2009; Korürek & Nizam, 2008; Özbay, Ceylan, & Karlik, 2011; Yeh, Chiou, & Lin, 2012), instead of classification. Once the algorithm is run, the clusters are then manually or automatically classified.

However, according to Chazal et al. (2004), Ince, Kiranyaz, and Gabbouj (2009), Llamedo and Martínez (2011) few researchers have used standard protocols to evaluate their expert system classifiers, establishing learning and testing strategies with bias their results near the optimal ones (i.e., the perfect classification). Other works have considered not publicly available dataset (Özbay et al., 2011; Yeh et al., 2012) which becomes difficult any kind of comparison. The majority of those researchers are favored by a biased training set (i.e., the heartbeats from the same patient are used for both training and testing the classifiers, which makes a fair comparison among methods difficult) to train their classifiers. With such strategy, the classifiers know particularities of the patients' heartbeat which is a nonrealistic situation. Usually the results of these works report effectiveness in average near 100% for heartbeats classification. When the constraint of heartbeat from the same patient in data division for training and testing classifiers is imposed, it is noticeable that their achieved effectiveness drop a lot. These classification issues are intensively discussed on (Luz & Menotti, 2011) showing that there is still too much room for improvement.

In order to standardize comparison and overcome such difficulties, *The Association for the Advancement of Medical Instrumentation* (AAMI) has developed a standard (ANSI/AAMI/ISO EC57, 1998-R2008) for testing and reporting performance results of computational techniques aiming at arrhythmia classification. The AAMI also recommends the use of the MIT-BIH Arrhythmia Database (Mark & Moody, 1990) for performance evaluation of arrhythmia systems. THE MIT-BIH Arrhythmia Database is the most widely used database for evaluation of the accuracy/sensitivity/specificity (from now on performance) of arrhythmia classification systems. This database was the first available for such a purpose and it has gone through several improvements over the years to encompass the broadest possible range of waveforms Moody and Mark (2001). Here, we perform experiments following the AAMI standard and solely use the entire MIT-BIH Arrhythmia Database.

In the context, a recent and powerful expert system classifier, proposed in Papa, Falcão, and Suzuki (2009) and customized in Papa, Falcão, de Albuquerque, and Tavares (2012), named optimum-path forest (OPF) classifier, arises for the automated detection of specific problems and has been shown to be very effective, with excellent results compared to ANN and SVM (Papa et al., 2009). The OPF classifier has been used in some applications as, for example, petroleum well drilling monitoring (Guilherme

et al., 2011), characterization of graphite particles in metallographic images (Papa, Nakamura, de Albuquerque, Falcão, \& Tavares, 2013), classification of remote sensing images (Santos, Gosselin, Philipp-Foliguet, Torres, \& Falcão, 2012), nontechnical losses detection (Ramos, Souza, Papa, \& Falcão, 2011), segmentation and classification of human intestinal parasites from microscopy images Suzuki, Gomes, Falcão, Papa, and Shimizu (2012), among others, achieving promising results due to its advantages on other classifiers regarding efficiency (mainly computational cost), which is an important factor in ECG arrhythmia signal classification. In the hospitals, the equipments used to accomplish the arrhythmia signal classification task, such as bed side monitors and defibrillators, often have limited resources. Despite of that OPF classifier has shown effectiveness compatible, and faster for training than other classifiers (Papa et al., 2012).

The aim of this work is to evaluate the OPF classifier performance focusing mainly on the last step of the cardiac arrhythmia analysis, i.e., ECG signal classification, considering mainly the computational cost, accuracy, sensitivity, and specificity. The performance is compared to the ones of three other well-known classifier algorithms widely used in the pattern recognition and machine learning literature (i.e, SVM with radial basis-function kernel, multi-layer perceptron neural network (MLP) and Bayesian expert system classifiers). Besides following the AAMI recommendation and using the MIT-BIH Arrhythmia Database for producing results reliable to clinic analysis, in order to perform our comparison, on non normalized datasets, we re-implement six approaches (Chazal et al., 2004; Güler \& Übeyli, 2005; Song et al., 2005; Ye et al., 2010; Yu \& Chen, 2007; Yu \& Chou, 2008) we consider quite representative of the ECG signal feature extraction domain. These feature selection processes are reproduced as faithfully as possible to their description using Matlab. Each feature extraction set is then submitted to each considered expert system classifier.

The remainder of this work is organized as follows. The feature extraction approaches used in this work are briefly summarized in Section 2. The OPF classifier and the other three expert system classifiers are described in Section 3. The experimental results are shown in Section 4, and discussed in Section 5. Finally, in Section 6, the conclusions are pointed out.

## 2. Feature extraction

In this section, the six feature extraction approaches used in this work for the comparison of classifiers are described. Observe that each approach comes from a work/paper which was used for arrhythmia classification, obviously using a classifier algorithm which is disregarded here. These approaches are chosen because they bring techniques widely used in literature and yet, the values of accuracy, sensitivity, sensibility reported are high compared to other published methods.

Notice that the six methods described here and used in our experiments and discussion are re-implemented as faithfully as possible to their description using Matlab. ${ }^{1}$

### 2.1. Chazal et al. (2004)

The most common feature found in the literature for ECG signal classification is computed from the cardiac rhythm (heartbeat interval) a.k.a. RR interval. The RR interval is the time between the heartbeat $R$ peak (the most important fiducial point) regarding another R peak, which can be its predecessor or successor. In Fig. 3, it is illustrated the RR interval and others also used in the litera-

[^0]![img-2.jpeg](img-2.jpeg)

Fig. 3. Fiducial points and important interval of a cardiac heartbeats. Extracted from (Clifford et al., 2006, Chapter 3).
ture. Except for patients who use pacemakers, the perceived variations in the RR interval width are correlated with variations in the morphology of the ECG signal curve, usually caused by arrhythmias (Clifford, Azuaje, \& McSharry, 2006). Features from the RR interval reveal great discriminatory capabilities for heartbeat classes and have been used in several works in the literature, specially in Chazal et al. (2004).

From the RR interval, we can extract four features which are used in Chazal et al. (2004): the RR interval between the current and its predecessor heartbeat (RR-predecessor), the RR interval between the current and its successor one (RR-posterior), the average of all RR interval containing in a full record (e.g., 30 min for instance) and also the average of ten RR interval around the current heartbeat.

Other features extracted from the cardiac beat intervals are also used in em (Chazal et al., 2004). These features are composed of distances between fiducial points in a heartbeat, as we can see in Fig. 3. Among them, the QRS interval, or the QRS-complex duration, is quite popular in the literature and also is use in (Chazal et al., 2004). Besides the length of QRS-complex, another time segment is used as feature in that work, i.e., the T wave length. The author also used the information about the presence/absence of P-wave. The algorithm used for fiducial point extraction in Chazal et al. (2004) is proposed in Laguna, Jané, and Caminal (1994) and is also used in this work here.

Nonetheless, the best classification results achieved in the literature have used features extracted from the RR interval and time segments of the heartbeat along with features extracted in the time/frequency domain (Chazal et al., 2004; Llamedo \& Martınez, 2011). The simplest form to extract features in the time domain from the ECG signal curve is using its own sampled points as features (Wen, Lin, Chang, \& Huang, 2009; Özbay \& Tezel, 2010) (see Fig. 4). However, using samples from the ECG curve as features is not a such effective technique, due to both (1) the dimension of the feature vector produced is high (it depends on the amount of samples used to represent the heartbeat), (2) it suffers with several problems regarding scale and displacement related to the central point (the R peak). In order to decrease the feature vector size and avoid the aforementioned problems, in Chazal et al. (2004), the authors used the interpolation of the ECG signal such that the final time representation is composed of 18 and 19 samples obtained from 250 samples (approximately 600 ms of curve/signal


[^0]:    ${ }^{1}$ The source code of implementations are available at http://code.google.com/p/ eswa-arrhythmia-classification/.

![img-3.jpeg](img-3.jpeg)

**Fig. 4.** ECG signal extracted from MIT-BIH AR database, sampled at 360 Hz.

![img-4.jpeg](img-4.jpeg)

**Fig. 5.** Reduction of the number of samples/features using interpolation. Extracted from Chazal et al. (2004).

initially sampled at 360 Hz – see Fig. 5). This process is applied in the two leads available in the dataset used. Then, for that work, a feature vector composed of the 52 best features reported is used.

### 2.2. Song et al. (2005)

In Song et al. (2005), instead of interpolating the ECG signal as done in Chazal et al. (2004), the authors used the wavelet transform to extract 15 features from the heartbeat. It is important to note that the majority of works in the literature use the wavelet transform in the feature extraction process, because it allows the extraction of information in both time and frequency domains. Also, several work supports that this method is the best for feature extraction from ECG signals (Güler & Übeyli, 2005; Lin, Du, & Chen, 2008a; Mehmet, 2004).

In that work (Song et al., 2005), the heartbeat is represented as a 400 ms sampled window of the ECG signal centered at the R peak (144 samples). These samples are decomposed into seven levels using the wavelet transform, however only the detail coefficients/sub-bands are used. Along with these feature, RR interval features (RR-predecessor and RR-posterior) are included in the final feature vector.

### 2.3. Güler and Übeyli (2005)

In Güler and Übeyli (2005), the authors also used the wavelet transform to decompose the ECG signal (approximately 700 ms around the R peak) into 256 coefficients of the four first levels combining 247 from details and 18 from approximation sub-bands. In order to reduce the feature vector dimensionality, the authors used simple statistical measures: the average power, the mean, and the standard deviation of the coefficients in each wavelet sub-band, and also the ratio of the absolute mean values of adjacent sub-bands. The authors highlighted that the choice of the mother wavelet function used in the feature extraction process is critical to the final effectiveness of the classification. As a consequence of this claim, all the feature extraction processes using the wavelet transform studied in the work here were carefully reproduced taking into account the mother wavelet function suggested by the authors of each work.

### 2.4. Yu and Chen (2007)

In the work proposed in Yu and Chen (2007), the authors used statistical techniques directly on heartbeat samples and, also, in three wavelet sub-bands: details of the first level of wavelet transform decomposition and approximation and details of the second level one. It is also used the AC power of the original signal, the AC power of each wavelet sub-band, the AC power of the autocorrelation function of the coefficients of each sub-band, and the ratio between the maximum and minimum values in each sub-band, adding up to 10 features. Besides these 10 statistical features, the authors also used the RR interval (RR-predecessor).

### 2.5. Yu and Chou (2008)

In Yu and Chou (2008), the independent component analysis (ICA) is used to extract 100 coefficients from a heartbeat composed of 200 samples centered at the R peak. The ICA coefficients are computed using the Fast-ICA algorithm, proposed in Hyvärinen (1999), and only the first 33 coefficients are finally used. According to the authors, the ICA is used to decompose the ECG signal in a weighted sum of the basic components which are mutually statistically independent. To these coefficients, the RR interval (RR-predecessor) is added.

### 2.6. Ye et al. (2010)

Ye et al. (2010) combined several feature extraction techniques presented in the literature to generate their feature vector. Their features are extracted from 300 samples surrounding the R peak, being 100 before and 200 after the R peak. The wavelet transform is applied to the sampled ECG signal and 118 coefficients are extracted from detail sub-bands of the third and fourth levels and approximation sub-band of the fourth level of the wavelet decomposition. Along with these features, eighteen coefficients extracted using the ICA (also using the algorithm proposed in Hyvärinen (1999)). This set of feature is named as morphological by the authors.

Four features extracted from the RR interval, named as dynamical by the authors, are also used: RR-predecessor, RR-posterior, the average of all RR intervals of a record of a patient, and the average of the 10 RR intervals surrounding (and centered to) the current heartbeat. In order to reduce the dimension of the obtained morphological feature vector to 26, the authors employed the principal components analysis (PCA) technique. This process is applied to the two ECG leads available on the MIT-BIH heartbeat record dataset, producing a final feature vector in which its dimension is twice that for a single lead.

### 3. Expert system classifiers

In this section, the four learning algorithms used in our comparison are presented. Special attention is given to the OPF classifier since to the best of our knowledge it is the first time that such algorithm is used for arrhythmia classification in ECG signals.

### 3.1. Optimum-path forest classifier

The optimum-path forest (OPF) is a framework to the design of pattern classifiers based on optimal graph partitions Papa et al. (2009, 2012), in which each sample is represented as a node of a complete graph, and the arcs between them are weighted by the distance of their corresponding feature vectors. The idea behind OPF is to rule a competition process between some key samples (prototypes) in order to partition the graph into optimum-path trees (OPTs), which will be rooted at each prototype. We have that samples that belong to the same OPT are more strongly connected to their root (prototype) than to any other one in the optimumpath forest. Prototypes assign their costs (i.e., their lowest weight path or the maximum arc-weight along a path) for each node, and the prototype that offered the optimum path-cost will conquer that node, which will be marked with the same prototype's label.

Let $Z=Z_{1} \cup Z_{2}$ be a dataset labeled with a function $\lambda$, in which $Z_{1}$ and $Z_{2}$ are, respectively, a training and test sets such that $Z_{1}$ is used to train a given classifier and $Z_{2}$ is used to assess its accuracy. Let $S \subseteq Z_{1}$ a set of prototype samples. Essentially, the OPF classifier creates a discrete optimal partition of the feature space such that any sample $s \in Z_{2}$ can be classified according to this partition. This partition is an optimum path forest (OPF) computed in $\Re^{n}$ by the image foresting transform (IFT) algorithm (Falcão, Stolfi, \& Lotufo, 2004).

The OPF algorithm may be used with any smooth path-cost function which can group samples with similar properties (Falcão et al., 2004). Particularly, we used the path-cost function $f_{\max }$, which is computed as follows:
$f_{\max }(\langle s\rangle)=\left\{\begin{array}{ll}0 & \text { if } s \in S, \\ +\infty & \text { otherwise }\end{array}\right.$
$f_{\max }(\pi \cdot\langle s, t\rangle)=\max \left\{f_{\max }(\pi), d(s, t)\right\}$,
in which $d(s, t)$ means the distance between samples $s$ and $t$, and a path $\pi$ is defined as a sequence of adjacent samples. In such a way, we have that $f_{\max }(\pi)$ computes the maximum distance between adjacent samples in $\pi$, when $\pi$ is not a trivial path.

The OPF algorithm assigns one optimum path $P^{\prime}(s)$ from $S$ to every sample $s \in Z_{1}$, forming an optimum path forest $P$ (a function with no cycles which assigns to each $s \in Z_{1} \backslash S$ its predecessor $P(s)$ in $P^{\prime}(s)$ or a marker nil when $s \in S$ ). Let $R(s) \in S$ be the root of $P^{\prime}(s)$ which can be reached from $P(s)$. The OPF algorithm computes for each $s \in Z_{1}$, the cost $C(s)$ of $P^{\prime}(s)$, the label $L(s)=\lambda(R(s))$, and the predecessor $P(s)$.

The OPF classifier is composed of two distinct phases: (i) training and (ii) classification. The former step consists, essentially, in finding the prototypes and computing the optimum-path forest, which is the union of all OPTs rooted at each prototype. Then, we take a sample from the test sample, connect it to all samples of the optimum-path forest generated in the training phase and we evaluate which node offered the optimum path to it. Notice that this test sample is not permanently added to the training set, i.e., it is used only once. The next sections describe in details this procedure.

### 3.1.1. Training

We say that $S^{*}$ is an optimum set of prototypes when the OPF algorithm minimizes the classification errors for every $s \in Z_{1} . S^{*}$ can be found by exploiting the theoretical relation between mini-mum-spanning tree (MST) and optimum-path tree for $f_{\max }$ (Allène, Audibert, Couprie, Cousty, \& Keriven, 2007). The training essentially consists in finding $S^{*}$ and an OPF classifier rooted at $S^{*}$.

By computing a MST in the complete graph $\left(Z_{1}, A\right)$ (Fig. 6a), we obtain a connected acyclic graph whose nodes are all samples of
$Z_{1}$ and the arcs are undirected and weighted by the distances $d$ between adjacent samples (Fig. 6b). The spanning tree is optimum in the sense that the sum of its arc weights is minimum as compared to any other spanning tree in the complete graph.

## Algorithm 1. OPF training algorithm

```
Input: A \(\lambda\)-labeled training set \(Z_{1}\) and the pair \((v, d)\) for feature vector
    and distance computations.
Output: Optimum-path forest \(P_{1}\), cost map \(C_{1}\), label map \(L_{1}\), and ordered
    set \(\left.Z_{1}^{\prime}\right)\).
AUXILIARY: Priority queue \(Q\), set \(S\) of prototypes, and cost variable cst.
```

1. Set $Z_{1}^{\prime} \leftarrow \emptyset$
2. Compute by MST the prototype set $S \subset Z_{1}$.
3. For each $s \in Z_{1} \backslash S$, set $C_{1}(s) \leftarrow+\infty$.
4. For each $s \in S$, do
5. $\quad C_{1}(s) \leftarrow 0, P_{1}(s) \leftarrow n i l$,
6. $\quad L_{1}(s) \leftarrow \lambda(s)$, insert $s$ in $Q$.
7. While $Q$ is not empty, do
8. Remove from $Q$ a sample $s / C_{1}(s)$ is minimum.
9. Insert $s$ in $Z_{1}^{\prime}$.
10. For each $t \in Z_{1}$ such that $C_{1}(t)>C_{1}(s)$, do
11. Compute cst \(\leftarrow \max \left\{C_{1}(s), d(s, t)\right\}\).
12. If cst $<C_{1}(t)$, then
13. If $C_{1}(t) \neq+\infty$, then remove $t$ from $Q$.
14. 

$$
P_{1}(t) \leftarrow s, L_{1}(t) \leftarrow L_{1}(s), C_{1}(t) \leftarrow c s t
$$

15. Insert $t$ in $Q$.
16. Return a classifier $\left[P_{1}, C_{1}, L_{1}, Z_{1}^{\prime}\right]$.

In the MST, every pair of samples is connected by a single path which is optimum according to $f_{\max }$. That is, the minimum-spanning tree contains one optimum-path tree for any selected root node. The optimum prototypes are the closest elements of the MST with different labels in $Z_{1}$ (i.e., elements that fall in the frontier of the classes). Algorithm 1 implements the training procedure for OPF.

The time complexity for training is $\theta\left(\left|Z_{1}\right|^{2}\right)$, due to the main (lines 7-15) and inner loops (lines 10-15) in Algorithm 1, which run $\theta\left(\left|Z_{1}\right|\right)$ times each.

After that, we have a collection of OPTs, each one of them rooted at each prototype, as one can see in Fig. 6c. This geometry of the feature space gives the name to the classifier.

### 3.1.2. Classification

For any sample $t \in Z_{2}$, we consider all arcs connecting $t$ with samples $s \in Z_{1}$, as though $t$ were part of the training graph (Fig. 6d). Considering all possible paths from $S^{*}$ to $t$, we find the optimum path $P^{\prime}(t)$ from $S^{*}$ and label $t$ with the class $\lambda(R(t))$ of its most strongly connected prototype $R(t) \in S^{*}$. This path can be identified incrementally by evaluating the optimum cost $C(t)$ as
$C(t)=\min \{\max \{C(s), d(s, t)\}\}, \quad \forall s \in Z_{1}$.
Let the node $s^{*} \in Z_{1}$ be the one that satisfies Eq. (2) (i.e., the predecessor $P(t)$ in the optimum path $P^{\prime}(t)$ ). Given that $L\left(s^{*}\right)=\lambda(R(t))$, the classification simply assigns $L\left(s^{*}\right)$ as the class of $t$ (Fig. 6e). An error occurs when $L\left(s^{*}\right) \neq \lambda(t)$. Algorithm 2 implements this procedure.

Algorithm 2. OPF classification algorithm


1. For each $t \in Z_{2}$, do
2. $\quad i \leftarrow 1$, mincost $\leftarrow \max \left\{C_{1}\left(k_{i}\right), d\left(k_{i}, t\right)\right\}$.
3. $\quad L_{2}(t) \leftarrow L_{1}\left(k_{i}\right)$ and $P_{2}(t) \leftarrow k_{i}$.
4. While $i<\left|Z_{1}^{\prime}\right|$ and mincost $>C_{1}\left(k_{i+1}\right)$, do
5. Compute tmp $\leftarrow \max \left\{C_{1}\left(k_{i+1}, d\left(k_{i+1}, t\right)\right\}\right.$.
6. If tmp < mincost, then
7. $\quad$ mincost $\leftarrow$ tmp.
8. 

8
9 .
$L_{2}(t) \leftarrow L\left(k_{i+1}\right)$ and $P_{2}(t) \leftarrow k_{i+1}$.
$i \leftarrow i+1$.
10. Return $\left[L_{2}, P_{2}\right]$.

In Algorithm 2, the main loop (lines 1-9) performs the classification of all nodes in $Z_{2}$. The inner loop (lines 4-9) visits each node $k_{i+1} \in Z_{1}^{\prime}, i=1,2, \ldots,\left|Z_{1}^{\prime}\right|-1$ until an optimum path $\pi_{k_{i-1}} \cdot\left(k_{i+1}, t\right)$ is found.

### 3.2. Bayesian classifier

Let $p\left(\omega_{i}-x\right)$ be the probability of a given pattern $x \in \Re^{n}$ to belong to class $\omega_{i}, i=1,2, \ldots, c$, which can be defined by the Bayes Theorem (Jaynes, 2003):
$p\left(\omega_{i} \mid x\right)=\frac{p\left(x \mid \omega_{i}\right) P\left(\omega_{i}\right)}{p(x)}$,
where $p\left(x \mid \omega_{i}\right)$ is the probability density function of the patterns that compose the class $\omega_{i}$, and $P\left(\omega_{i}\right)$ corresponds to the probability of the class $\omega_{i}$ itself.

A Bayesian classifier decides whether a pattern $x$ belongs to the class $\omega_{i}$ when:
$p\left(\omega_{i} \mid x\right)>p\left(\omega_{j} \mid x\right), \quad i, j=1,2, \ldots, c, i \neq j$,
which can be rewritten as follows by using Eq. (3):
$p\left(x \mid \omega_{i}\right) P\left(\omega_{i}\right)>p\left(x \mid \omega_{j}\right) P\left(\omega_{j}\right), \quad i, j=1,2, \ldots, x, i \neq j$.
As one can see, the Bayes classifies decision function $d_{i}(x)=$ $p\left(x \mid \omega_{i}\right) P\left(\omega_{i}\right)$ of a given class $\omega_{i}$ strongly depends on the previous knowledge of $p\left(x \mid \omega_{i}\right)$ and $P\left(\omega_{i}\right), \forall i=1,2, \ldots, c$. The probability values of $P\left(\omega_{i}\right)$ are straightforward and can be obtained by calculating the histogram of the classes. However, the main problem is to find the probability density function $p\left(x \mid \omega_{i}\right)$, given that the only information available is a set of patterns and its corresponding labels. A common practice is to assume that the probability density functions are Gaussian ones, and thus one can estimate their parameters using the dataset samples (Duda, Hart, \& Stork, 2000). In the $n$-dimensional case, a Gaussian density of the patterns from class $\omega_{i}$ can be calculated using:
$p\left(x \mid \omega_{i}\right)=\frac{1}{(2 \pi)^{n / 2}\left|C_{i}\right|^{1 / 2}} \exp \left[-\frac{1}{2}\left(x-\mu_{i}\right)^{T} C_{i}^{-1}\left(x-\mu_{i}\right)\right]$,
in which $\mu_{i}$ and $C_{i}$ correspond to the mean and the covariance matrix of class $\omega_{i}$. These parameters can be obtained by considering each pattern $x$ that belongs to class $\omega_{i}$ using the following equations:
![img-5.jpeg](img-5.jpeg)

Fig. 6. OPF pipeline: (a) complete graph, (b) MST and prototypes bounded, (c) optimum-path forest generated at the final of training step, (d) classification process and (e) the triangle sample is associated to the white circle class. The values above the nodes are their costs after training, and the values above the edges stand for the distance between their corresponding nodes.
$\mu_{i}=\frac{1}{N_{i}} \sum_{x \in \omega_{i}} x$,
and
$C_{i}=\frac{1}{N_{i}} \sum_{x \in \omega_{i}}\left(x x^{2}-\mu_{i} \mu_{i}^{T}\right)$,
in which $N_{i}$ means the number of samples from class $\omega_{i}$.

### 3.3. Support vector machines classifier

One of the fundamental problems of the learning theory can be stated as: given two classes of known objects, assign one of them to a new unknown object. Thus, the objective in a two-class pattern recognition is to infer a function (Schölkopf \& Smola, 2002):
$f: \mathscr{X} \rightarrow\{ \pm 1\}$,
regarding the input-output of the training data.
Based on the principle of structural risk minimization (Vapnik, 1999), the SVM optimization process is aimed at establishing a separating function while accomplishing the trade-off that exists between generalization and over-fitting.

Vapnik (1999) considered the class of hyperplanes in some dot product space $\mathscr{H}$,
$\langle\mathbf{w}, \mathbf{x}\rangle+b=0$,
where $\mathbf{w}, \mathbf{x} \in \mathscr{H}, b \in \mathbb{R}$, corresponding to decision function:
$f(x)=\operatorname{sgn}(\langle\mathbf{w}, \mathbf{x}\rangle+b)$,
and, based on the following two arguments, the author proposed the Generalized Portrait learning algorithm for problems which are separable by hyperplanes:

1. Among all hyperplanes separating the data, there exists a unique optimal hyperplane distinguished by the maximum margin of separation between any training point and the hyperplane.
2. The over-fitting of the separating hyperplanes decreases with increasing margin.

Thus, to construct the optimal hyperplane, it is necessary to solve:
$\underset{\mathbf{w} \in \mathcal{F}, b \in \mathbb{R}}{\operatorname{minimize}} \quad \tau(\mathbf{w})=\frac{1}{2}\|\mathbf{w}\|^{2}$,
subject to:
$y_{i}\left(\left\langle\mathbf{w}, \mathbf{x}_{i}\right\rangle+b\right) \geqslant 1 \quad$ for all $\quad i=1, \ldots, m$,
with the constraint (13) ensuring that $f\left(x_{i}\right)$ will be +1 for $y_{i}=+1$ and -1 for $y_{i}=-1$, and also fixing the scale of $\mathbf{w}$. A detailed discussion of these arguments is provided by Schölkopf and Smola (2002).

The function $\tau$ in (12) is called the objective function, while in (13) the functions are the inequality constraints. Together, they form a so-called constrained optimization problem. The separating function is then a weighted combination of elements of the training set. These elements are called support vectors and characterize the boundary between the two classes.

The replacement referred to as the kernel trick (Schölkopf \& Smola, 2002) is used to extend the concept of hyperplane classifiers to nonlinear support vector machines. However, even with the advantage of "kernelizing" the problem, the separating hyperplane may still not exist.

In order to allow some examples to violate (13), the slack variables $\xi \geqslant 0$ are introduced (Schölkopf \& Smola, 2002), which leads to the constraints:
$y_{i}\left(\left\langle\mathbf{w}, \mathbf{x}_{i}\right\rangle+b\right) \geqslant 1-\xi_{i} \quad$ for all $\quad i=1, \ldots, m$.
A classifier that generalizes efficiently is then found by controlling both the margin (through $\|\mathbf{w}\|$ ) and the sum of the slack variables $\sum_{i} \xi_{i}$. As a result, a possible accomplishment of such a soft margin classifier is obtained by minimizing the objective function:
$\tau(\mathbf{w}, \xi)=\frac{1}{2}\|\mathbf{w}\|^{2}+C \sum_{i=1}^{m} \xi_{i}$,
subject to the constraint in (14), where the constant $C>0$ determines the balance between over-fitting and generalization. Due to the tuning variable $C$, these kinds of SVM based classifiers are normally referred to as C-Support Vector Classifiers (C-SVC) (Cortes \& Vapnik, 1995).

### 3.4. Multi-layer perceptron neural network classifier

In this work we used an multi-layer perceptron neural networks (ANN-MLP) from fast artificial neural network library (FANN), in Nissen (2003), which is a free open source ANN library, which implements ANN-MLP in C and supports both fully and sparsely connected networks. The ANN-MLP is a combination of Perceptron layers aiming to solve multi-class problems Haykin (2007). The neural network architecture is composed of neuron layers, such that each output feeds the input neurons at the follows layer. The first layer, denoted by $A$, has $N_{A}$ neurons, where $N_{A}$ has the same dimensionality of the feature vector, while the last layer, denoted by $Q$, has $N_{Q}$ neurons, which stands for the number of the classes. This neural network assigns a pattern vector $x$ to a class $\omega_{m}$ if the $m$ th output neuron achieves the highest value.

Each input layer corresponds to a weighted sum of the previous layer. Let $J-1$ be the previous layer of $J$, such that each input $I_{j}^{j}$ in $J$ is given by
$I_{j}^{j}=\sum_{k=1}^{N_{K}} w_{j k} O_{k}^{j-1}$
and
$O_{k}^{j-1}=\phi\left(I_{k}^{j-1}\right)$,
where $j=1,2, \ldots, N_{J}$, being $N_{J}$ and $N_{K}$ the amount of neurons at the layer $J$ and $J-1$, respectively, and $w_{j k}$ stands for the weights that modify the $k$ th output of layer $J-1$, i.e., $O_{k}^{j-1}$.

The backpropagation algorithm is usually employed to train MLP (Russell \& Norvig, 2009). This algorithm minimizes the mean squared error between the desired outputs $r_{i j}$ and the obtained outputs $\Phi_{i j}$ of each node of the output layer $Q$. Therefore, the idea is to minimize the equation bellow:
$E_{i j}=\frac{1}{N_{Q}} \sum_{q=1}^{N_{Q}}\left(r_{i j}-\Phi_{i j}\right)^{2}$,
in which $N_{Q}$ is the number of neurons at the output layer $Q$.

## 4. Experiments and results

In this work, we propose the use of a recent and powerful pattern recognition technique, the OPF classifier, for heartbeat ECG signal classification. In Section 2, we surveyed six feature selection approaches widely used in the literature for this purpose, in which all were re-implemented. In Section 3, we described the OPF classifier along with the other three classifiers, i.e., SVM, MLP, and Bayesian, which will be used in our experiments presented in this section. These features extraction approaches and classifier algorithms are combined to yield intelligent systems with high accuracy and low computational cost.

The experiments works as follows. Initially we describe the dataset used, the suggested recommendations by the AAMI standards to analyze and classify cardiac arrhythmia using ECG signals which recommends, and, finally, an explanation on how the MITBIH Arrhythmia Dataset is divided for creating the training (denominated in this work as DS1) and testing (denominated of DS2) sets as suggested in Chazal et al. (2004). After, we present the measures used to evaluate the effectiveness of the expert system classifiers proposed in this work.

### 4.1. Database description and AAMI standards

The MIT-BIH Arrhythmia Database contains 48 half-hour recordings, sampled at 360 Hz , and eighteen types of heartbeats are classified and labeled. To comply with the AAMI recommendations, only 44 recordings from the MIT-BIH Arrhythmia Database should be used for evaluation of cardiac arrhythmia signal classification methods, excluding the four recordings that contain paced beats. The ANSI/AAMI EC57:1998/[R]2008 standard AAMI (2008) recommends to group those heartbeats into five classes: (1) normal beat (N), (2) supraventricular ectopic beat (SVEB, here just S), (3) ventricular ectopic beat (VEB, here just V), (4) fusion (F) of a V and a N, and (5) unknown beat type (Q), as shown in Table 1.

Recently, in Llamedo and Martínez (2011), it is proposed a shorter group of classes. Since the AAMI Q class (unclassified and paced heartbeats) is marginally represented in the database (corresponding to $0.015 \%$ of all database), it is discarded. Also, due to its morphologic similarity to the V AAMI class, the fusion (F) AAMI class, instead of being discarded, are merged together creating a new ventricular class, here represented as $V$. This modification is referred as AAMI2 labeling. It is important to note that this reduction in the group of classes is mainly motivated by the non representative amount of samples of the AAMI Q and the featureless

Table 1
Mapping the MIT-BIH Arrhythmia types to the AAMI classes.


Table 2
MIT-BIH Arrhythmia Dataset division scheme of the heartbeats.


Table 3
The division of records of patients' heartbeats of the MIT-BIH Arrhythmia Dataset for training (DS1) and testing (DS2).


values achieved by the AAMI F class in the works reported in the literature (Chazal et al., 2004; Llamedo \& Martínez, 2011; Mar, Zaunseder, Martínez, Llamedo, \& Poll, 2011) and also in this work. Also observe that the N AAMI class is dominant representing $89.46 \%$ of all heartbeats' dataset. So attention has to be given in the effectiveness analysis of the results related to N AAMI class, since an optimal performance in only in that class means a final accuracy of almost $90 \%$. Sensibility and specificity are measures that can capture the effectiveness performance of each class and are explained further in this section.

The AAMI standards also recommend dividing the recordings into two datasets: one for training and another for testing such that heartbeats from one recording (patient) are not used simultaneously for both training and testing the classifier. As claimed before and shown in Luz and Menotti (2011), when this constraint is not imposed for building the datasets for training and testing the classifiers achieve very high performance. However, such practice is not valid for considering realistic clinical results, since the classifier is not trained with the data heartbeat of a patient to be analyzed. Usually the heartbeats of a new patient does not belong to the training set, requiring the use of expert system classifiers more robust.

Then train (DS1) and test (DS2) sets are created, in order to accomplish AAMI recommendations and approximate to real world situation. As one can see from the values in Table 2 an effort to balance the amount of samples/heartbeat per class in the datasets is also noticed in such division. Note that \#Rec stands for the number of records (patients) and DS1 and DS2 are suggested in Chazal et al. (2004) and not in ANSI/AAMI EC57:1998/(R)2008 standard AAMI
(2008). Moreover, analyzing the experiments performed on the six works we studied here used for collect their feature representation (presented in Section 2), (Chazal et al., 2004) is the one to follows the AAMI standards, while the others use different heartbeats of a same patient to be used in training and testing due to the high effectiveness they report in their works. This claim is show in Luz and Menotti (2011).

The two partitions should be composed of the records of patients' heartbeats shown in Table 3, in which the numbers indicate a code for the recording of 30 min of heartbeat of each patient. Chazal et al. (2004) claims that the record numbered 1\#\# and 2\#\# belongs to two class of patients (Mark \& Moody, 1990), i.e. the first range are intended to serve as a representative sample of routine clinical recordings, while the second one contains complex ventricular, junctional, and supraventricular arrhythmias, so they decided to balance the presence of these records in each set such that the classifier has the larger diversity as possible for both training and testing, making these datasets the less biased as possible.

Observe that in such data division scheme heartbeats of a same patient are not present in both datasets, complying to the AAMI standards. That means that the heartbearts of a same patient are solely used to either (and not both) train or test the systems. The reasons for this constraint is to report the predictive effectiveness of ECG signal classification systems compatible in a real clinical trial.

All composition of feature extraction approaches and classifier algorithms are training in DS1 dataset and tested in DS2 following the scheme proposed in Chazal et al. (2004).

### 4.2. Performance evaluation measures

In order to analyze the expert system classifiers, we present the three measures employed: accuracy, sensitivity, and specificity.

Accuracy (Acc) is defined as the ratio of total beats correctly classified and the number of total beats,
Accuracy $=\frac{\text { beats correctly classified }}{\text { number of total beats }}$.
Sensitivity (Se) can be defined as the ratio of correctly classified beats of one class and the total beats classified as that class, including the missed classification beats,
Sensitivity $=\frac{\text { true positives }}{\text { true positives }+ \text { false negatives }}$
in which true positives and false negatives stand for the number of heartbeats of a given class correctly and incorrectly classified, respectively.

Table 4 Computing the classifiers effectiveness from the confusion matrix. This scheme is extracted from Chazal et al. (2004) and adapted.
![img-6.jpeg](img-6.jpeg)

Abbreviation: Acc: Accuracy, F: F AAMI class, $N$ : N AAMI Class, Q: Q AAMI Class, Se: Sensitivity, Sp: Specificity, S: S AAMI class, V: V AAMI class.

Specificity ( $S p$ ) stands for the ratio of correctly classified beats among all beats of a specific class,
Specificity $=\frac{\text { true negatives }}{\text { true negatives }+ \text { false positives }}$
in which true negatives stands for number of the heartbeats not belonging to a given class classified as not belonging to the considered class, while false positives stands for the number of heartbeats incorrectly classified as belonging to a given class. Observe that these last two measures are based on the data of each class.

Furthermore, we also propose the use of a Harmonic mean (Hm) between sensitivity and specificity, mathematically express by:

$$
\mathrm{HM}=2 \times \frac{S e \times S p}{S e+S p}
$$

These measures can be computed from a confusion matrix which can be obtained by comparing the expected classification (reference data) which the ones predicted by a classifier. Table 4 shows in details how to compute these measures, obtained and firstly discussed by Chazal et al. (2004). In Table 4(a) and (b), in dark gray (vertical highlighted lines), we illustrate how to compute the false positives for V and S AAMI classes, respectively, while in gray (horizontal highlighted lines), we illustrate how to compute the false negative for V and S AAMI classes, respectively. To compute Se's e Sp's for N, F, and Q AAMI class we can proceed in a similar way to the ones of V and S AAMI classes.

Table 5
Training and testing time (in seconds) for MIT-BIH Arrhythmia Dataset following AAMI recommendations (5 classes).


Table 6
Training and testing time (in seconds) for MIT-BIH Arrhythmia Dataset following the labeling suggestion from Llamedo and Martínez (2011) (AAMI2-3 classes).


Although the accuracy is the most important measure for deciding the choice of an expert system classifier, the sensitivity and specificity are measures quite important as well in this context, since the number of heartbeats for each class in the MIT-BIH Arrhythmia Database is very imbalanced and a single class (e.g., the normal beats) could represent most of the total accuracy, while the sensitivity and specificity directly depend on the number of samples for each class.

Besides these measures for evaluating and comparing the effectiveness performance of the expert system classifiers, we also compute the training and testing time, which are also very important measures in ECG arrhythmia signal classification depending on the application.

## 5. Discussion

Our analysis and discussion of the results reported in this work are divided into two parts: efficiency and effectiveness. Note that all experiments reported here used a PC Intel i7 at 2.8 GHz and 4 Gb of RAM on a Linux Ubuntu operational system.

### 5.1. Efficiency

The run times obtained by the ECG signal expert system algorithms for learning the model from the entire training set (DS1) and for classifying the testing set (DS2) using the AAMI protocol (five classes) following the scheme proposed in Chazal et al. (2004) and the AAMI protocol with the shorter groups of classes (three classes) suggested by Llamedo and Martínez (2011) are reported in Tables 5 and 6, respectively.

Regarding the training time, in average, the Bayesian classifiers achieved the best time, followed by the SVM classifier being in average almost four time slower than the Bayesian classifier. The OPF classifier presented the third best time being in average around 10 times greater than the one of the Bayesian classifier. In average, the MLP classifier is the slower one for learning the models, due to convergence criterion setup. However, the SVM classifier achieves the highest time for learning in two situations (both for the features extracted by Song et al. (2005)). It is important to note that the grid search time for the SVM's $\gamma$ and $C$ parameters definitions are not taken into account in the training phase. It can be noticed that for the three classifiers, SVM, OPF and Bayesian, the changes in training time were not significant for 3 or 5 classes, but the MLP classifier obtained a significant training speed gain, reaching a time about $8 \%$ faster for three classes classification.

Analyzing the testing time, due to its nature, as we can observe from these tables, the MLP classifier is the fastest one on the test set. Being four orders of magnitude slower, the SVM appears in second place for run on the testing data. The OPF classifier arises as the third fast one being in average one order of magnitude slower than SVM, and the slower classifier for the testing data in the most of the cases is the Bayesian classifier. It is important to note that only in three experiments (Table 6) the Bayesian classifier performed the testing task faster than the OPF classifier, due to the significant testing time decreasing caused by the reduction of the number of classes of the AAMI2 datasets. This reduction seem to affect most of all the Bayesian classifier speeding up its testing time up to $40 \%$. Also observe that the testing time for the features extracted by Chazal et al. (2004) for all the classifiers is greater than to other features. This can be explained due to the higher vector dimensionality of this feature representation.

Concerning the full run average time taken in our experiments, the SVM classifier is faster, being followed by the Bayesian, OPF and MLP classifiers. However, the time to define the parameters $\operatorname{cost}(C)=5$ and $\operatorname{Gamma}(\gamma)=0.001$ was not considered. These val-

Table 7
Accuracies, sensitivities and specificities (in 0.1\%) for MIT-BIH Arrhythmia Dataset following AAMI recommendations (5 classes).


Table 8 Accuracies, sensitivities and specificities (in 0.1\%) for MIT-BIH Arrhythmia Dataset following the labeling suggestion from Llamedo and Martínez (2011) (AAMI2-3 classes).

Se/Sp/HM | S
Se/Sp/HM | V
Se/Sp/HM | Acc | N
Se/Sp/HM | S
Se/Sp/HM | V
Se/Sp/HM  |

Table 9 Confusion matrix for SVM classifying the Yu and Chen (2007) dataset.


ues were reported in the literature in Bhardwaj, Choudhary, and Dayama (2012), in which is analyzed a graph between accuracy and cost keeping gamma constant, and, further, accuracy v/s gamma keeping $C$ constant. When the parametrization of this values is considered in the train phase, the SVM classifier is much slower than the OPF and Bayesian classifiers, as can be seen in Papa et al. (2009), Guilherme et al. (2011), Papa et al. (2013), Santos et al. (2012), Ramos et al. (2011), for example.

One can note that the Bayesian classifier was slower than OPF for two datasets, containing data of 5 classes extracted by Chazal et al. (2004) and Ye et al. (2010) due its high dimensional feature vector. This statement is not true for three classes feature representations (datasets), where there is a speed gain in the testing time explained before.

### 5.2. Effectiveness

The effectiveness evaluation measures obtained, the Accuracy, Sensitivity, Specificity, and HM, by the ECG signal expert system algorithms trained on the training set (DS1) for classifying the testing set (DS2) containing 5 and 3 classes (similarly to the efficiency analysis) are shown in Tables 7 and 8, respectively. Due to page width limits the floating points of the numbers in these table are omitted, and the figures in the tables represent percentages ranging from $000.0 \%$ to $100.0 \%$.

As claimed before, the accuracy is the main important measure for analyzing the effectiveness of a ECG signal classification algorithm. Observing the accuracies values in Tables 7 and 8, it is noticeable that the SVM classifier obtained the highest accuracy in all feature representations used, regardless the amount of classes in the training set ( 5 or 3 ), followed by MLP classifier, which obtained the second best performance also in all feature representations. OPF and Bayesian classifiers showed very close

Table 10 Confusion matrix for SVM classifying the Song et al. (2005) dataset.


performances, varying less then $0.4 \%$ and presenting together the worst overall accuracies.

Further in this section, it will be shown that most of the good accuracy obtained by SVM and MLP classifiers are due to a good performance only for the N class. This happens because the N class is the most representative class in the set, grouping more than $89 \%$ of the entire set.

As sensitivity and specificity of all classes take into account false negatives and positives, respectively, and $H M$ is a combination of both, this parameter is an important one in our analysis of the capability of the method to differentiate the classes, and most of all the arrhythmic ones ( $\mathrm{S}, \mathrm{V}, \mathrm{V}^{\prime}, \mathrm{Q}$, and F ). Due to this, we consider on our analysis these parameters.

A false negative for the N class means a false alarm, that is, the classifier detect an arrhythmic beat when its true class is normal, while a false positive for the N class means that an arrhythmic beat takes place and the classifier detect it as a normal beat. In some situations, we prefer less false negatives (greater sensitivity than specificity) than false positives, and in other situations the opposite, that is why the $H m$ analysis is important which is defined as the harmonic mean of sensitivity and specificity to perform our analysis of the effectiveness in terms of sensitivity and specificity.

Then, our analysis of the effectiveness for classes is concentrated on the Harmonic mean values (Hm). Observing the values presented in Tables 7 and 8, we can see that, despite of the best accuracy performance obtained by SVM and MLP classifiers, their performance as a differentiation tool between classes lacks efficiency. One can observe from the confusion matrices shown in Tables 9 and 10, from the worst HM feature representation for SVM classifier, in this case Yu and Chen (2007) and Song et al. (2005), respectively that this classifier, SVM, tends to fail on classifying samples for arrhythmic classes, prevailing the most numerous class, in this case the N class. This is a major problem, considering the purpose of the classification, where great part of the arrhyth-

mic samples are classified as normal samples. This indicates that for this kind of classification, even with the best accuracy rates, the SVM classifier represents the worst result. The same analysis can be done for other feature representations and for three classes representations. It is clear also that the SVM classifier completely fails on classifying the $S$ class, decreasing its $H M$ on all datasets tested.

In our analysis, we also observed that the same problem occurs with the MLP classifier, in a smaller degree, specially on classes $S$ and $F$ for most of the feature representations on both, 3 and 5 classes analysis. On the other hand, we can note on the OPF and Bayesian classifiers $H M$ results, a very much better performance, showing to be more robust, despite of their lower accuracy rates. Moreover, the results obtained by both are very similar, allowing us to say they have almost the same performance on classifying arrhythmic classes. This ability to evaluate samples provided by potential diseased patients and differentiate it is the most important in our analysis, due to the goal of the classification system in detecting possible heart diseases.

So, from these analyses we can conclude that the OPF and Bayesian classifiers produce similar results and the best balance among classification of normal and arrhythmic classes when compared to the SVM and MLP classifiers.

Observe that the effectiveness achieved for class Q in Table 7 by the classifiers with all feature representations are negligible. The Q class almost always achieves zero value for sensitivity, leading to an $H M 0$. The performance on classifying $F$ class are also weak performances, than the other classes, due to its nature of being a fusion between two other classes. Due to the non representative amount of beats of class Q (less than $0.015 \%$ of the database) and to the difficult of the majority works in the literature and also those shown here in classifying the F class, the protocol called AAMI2 was proposed, in which the Q class was removed and the classes V and F class were fused into $\mathrm{V}^{\prime}$ class. By observing the Harmonic mean values (Hm) for the V class in Table 7 and $\mathrm{V}^{\prime}$ class in 8 , we can see that the fusion of V and F classes to V class does not impact the results for the $\mathrm{V}^{\prime}$ and $S$ classes when the OPF and Bayesian classifier are used. For SVM and MLP classifiers, there is an slightly impact but without leading to a better classification overall. This is a very important result for classification using Bayesian classifier, which was highly affected by the number of classes, in terms of speed. The problem with the number of classes, does not occur with the OPF classifier, since the training and testing time where not significantly affected, showing a great robustness of this classifier.

## 6. Conclusions

In this work, we investigated the use of the OPF classifier for the task of Arrhythmic ECG signal classification. To the best of our knowledge, it is the first that the OPF classifier is applied to ECG signal classification. Moreover, we studied and implemented six feature representation from works in the literature (Chazal et al., 2004; Güler \& Übeyli, 2005; Song et al., 2005; Yu \& Chen, 2007; Yu \& Chou, 2008; Ye et al., 2010) which in our opinion are quite representative. Besides applying these feature representation approaches to learn model with the OPF classifier, we also employ the use of other three well-know learning algorithms: support vector machines, multi-layer perceptron neural network (MLP), and Bayesian expert system classifiers.

The experiments reported here shown that the MLP classifier is the fastest one for the testing task, while the learning task is best performed by the SVM classifier. Nonetheless, in average, the OPF classifier has shown an efficiency performance not being five times worst than SVM classifiers. On the other hand, the OPF classifier to-
gether with the Bayesian one have shown the best balance for classifying the arrhythmic classes, despite the best accuracy performance yielded by the MLP and SVM classifier which biased the classification towards the normal class failing to classify the arrhythmic classes.

## Acknowledgments

The first and last authors would like to thank FAPEMIG, CAPES, and CNPq for the financial support. The third author thank to CNPq and Cearense Foundation for the Support of Scientific and Technological Development (FUNCAP) for providing financial support through a DCR Grant \#35.0053/2011.1 to Universidade de Fortaleza (UNIFOR). The forth author is grateful to National CNPq Grant \#303182/2011-3, and FAPESP Grant \#2009/16206-1.
