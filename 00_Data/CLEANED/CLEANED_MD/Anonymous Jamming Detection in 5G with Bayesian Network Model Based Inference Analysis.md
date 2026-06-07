# Anonymous Jamming Detection in 5G with Bayesian Network Model Based Inference Analysis 

Ying Wang<br>Stevens Institute of Technology<br>Hoboken, NJ, USA<br>Virginia Tech, Blacksburg, VA, USA<br>ywang6@stevens.edu<br>Shashank Jere<br>Bradley Department of ECE Virginia Tech<br>Blacksburg, VA, USA<br>shashankjere@vt.edu<br>Soumya Banerjee<br>Virginia Modeling Analysis and Simulation<br>Center<br>Old Dominion University, Norfolk, VA, USA<br>s1banerj@odu.edu

Lingjia Liu<br>Bradley Department of ECE<br>Virginia Tech<br>Blacksburg, VA, US<br>ljliu@vt.edu

Sachin Shetty
Virginia Modeling Analysis and Simulation Center
Old Dominion University, Norfolk, VA, USA
sshetty@odu.edu

Shehadi Dayekh<br>Cyber 5G Strategic Growth Offering<br>Deloitte \& Touche LLP<br>Dallas, TX, USA<br>sdayekh@deloitte.com

Abstract—Jamming and intrusion detection are some of the most important research domains in 5G that aim to maintain use-case reliability, prevent degradation of user experience, and avoid severe infrastructure failure or denial of service in missioncritical applications. This paper introduces an anonymous jamming detection model for 5G and beyond based on critical signal parameters collected from the radio access and core network's protocol stacks on a 5G testbed. The introduced system leverages both supervised and unsupervised learning to detect jamming with high-accuracy in real time, and allows for robust detection of unknown jamming types. Based on the given types of jamming, supervised instantaneous detection models reach an Area Under the Curve (AUC) within a range of 0.964 to 1 as compared to temporal-based long short-term memory (LSTM) models that reach AUC within a range of 0.923 to 1 . The need for data annotation effort and the required knowledge of a vocabulary of known jamming limits the usage of the introduced supervised learning-based approach. To mitigate this issue, an unsupervised auto-encoder-based anomaly detection is also presented. The introduced unsupervised approach has an AUC of 0.987 with training samples collected without any jamming or interference and shows resistance to adversarial training samples within certain percentage. To retain transparency and allow domain knowledge injection, a Bayesian network model based causation analysis is further introduced.

Index Terms-jamming, intrusion, 5G, cybersecurity, anonymous, causal analysis

## I. INTRODUCTION

5G communications and its application verticals are prone to jamming due to the inherent nature of wireless radio frequency transmission. As federal agencies and businesses rely more on 5G and beyond infrastructure, they are becoming increasingly more vulnerable to sophisticated cyber attacks that may cause communication disruption which can be costly. Such jamming attacks pose severe risks to verticals, including self-driving cars, smart cities, public safety, and healthcare. Accurate and

[^0]fast detection techniques of known and unknown jamming over the radio interface is the first step toward preventing such cyber threats and efficiently protecting critical communication.

The anticipation and prevention types of defense (APD) and anomaly-based intrusion detection systems (IDS) represent the two ends in the spectrum of anti-jamming techniques. APD relies on the prior probability and knowledge of possible attacks and malfunctions of a system. In contrast, IDS focuses on learning the characteristics of the expected system response and detects anomalous cases. Preventive security measures are ineffective against unforeseen or zero-day attacks [1]. Cyber risk system assessments that solely depend on APD heuristics such as sums of vulnerability scores or quantities of missing patches, open ports, etc., and such metrics are widely seen as weak and potentially misleading [1], [2].

In contrast with APD, several in-band IDS based anomaly detection techniques have been researched [3], [4], [5], [6]. Authors in [4] proposed an unsupervised anomaly detection method based on a combination of Long-Short Term Memory (LSTM) and Mixture Density Network (MDN) applied to temporal data by analyzing the In-Phase (I) and Quadrature (Q) components of digital radio transmissions. The analysis of IQ data located at the lower end of the network stack relies on a large cache for data processing. In [6], an adversarial auto-encoder-based spectrum anomaly detector is proposed that uses features including power spectral density, signal bandwidth, and center frequency. While anomaly-based IDS has addressed the limitation of detecting unforeseen attacks in APD, there lacks a synthesized understanding of the crosslayer response of the signal under test (SUT) at various attack and upper layer domain knowledge, which limits its accuracy and efficiency. Meanwhile, evolved APD approaches utilizing the availability of software-defined 5G testbeds, large computational power, and advanced machine learning algorithms provide a rich prior-knowledge and deep understanding of the


[^0]:    This work was funded by Deloitte \& Touche LLP's Cyber 5G Strategic Growth Offering.

SUT and of the radio environment [7], [8], [9], [10].

To address these gaps in both IDS and APD, in this study, an anonymous jamming detection model for 5G NSA (Non-Standalone) is design and implemented. The contributions of this paper are summarized below:

- A general approach of evaluating 5G NSA quality with the presence of WiFi-type interference in Long-Term Evolution (LTE) and New Radio (NR) cells is provided.
- Both supervised learning-based, and unsupervised learning-based algorithms are explored to construct an effective jamming detection model.
- A 5G platform including user equipment, base station, core network and cyber attack generator are developed for data generation and proof of concept.
- A Bayesian Network Model (BNM) is constructed for revealing causation and root, direct, and indirect causing of the jamming effects on the performance, thereby providing transparency to machine learning models.

The remainder of this paper is organized as follows: Sec. II formulates the problem, followed by a system description in Sec. III and Sec. IV. Performance evaluation, conclusion and future work are provided in Sec. V and Sec. VI.

## II. PROBLEM FORMULATION

A jamming detection and cyber monitoring application of a 5G NSA wireless network as shown in Fig. 1 was designed and implemented. The steps throughout the life cycle of jamming generation, communication configuration, data collection, intelligent analysis, and real-time feedback are integrated. With the presence of the jamming signal, communications with legitimate users would be impacted. Statistical information from cross-layer data plane including Physical Layer (PHY), Medium Access Layer (MAC), Radio Link Control (RLC), and Packet Data Convergence Control (PDCP) are collected and analyzed at the jamming detector module. The cross-layer data and side information available from the network and application layers are also input to the BNM for cyber inference analysis. The jamming detector and cyber inference analyzer module can be located at the base station (BS) to monitor the statistical information. It can also be a separate node fetching this information from the base station periodically. The former design, i.e., co-located at the BS, complies with the Open Radio Access Network (O-RAN) [11] architecture. In the latter setting, the jamming detector and analyzer module is located in a separate hardware unit and have minimal impact on the BS performance.

Various types of jamming signals are generated and the corresponding statistical data is collected and stored in the implementation platform for model training and evaluation. The jamming discrimination can be formulated as two hypotheses:

$$
\begin{gathered}
H_{0}: r[n]=s[n]+w[n], n=1, \ldots, N \\
H_{1}: r[n]=s[n]+w[n]+j_{m}[n], n=1, \ldots, N, m \in[0, \ldots, M]
\end{gathered}
$$

where, $N$ is the total number of data samples collected, $M$ is the total number of different jamming signal types
![img-0.jpeg](img-0.jpeg)

Fig. 1: System Overview
(including power level and center frequency changes), $r[n]=$ $\left[r_{u e}[n], r_{b s}[n]\right]$ is the concatenated list of received signals from both the User Equipment (UE) and the BS, $j[n]$ represents the concatenated unexpected signal generated by either interference or malicious jammers on both UE and the BS ends, $s[n]$ is the concatenated desired signal, $w[n]$ is the concatenated additive channel environment noise, $n$ is the index of discrete time slots, $m$ is the index of jamming type, where $m=0$ if the jamming type is unknown. Additionally,

$$
y[n]=f(r[n], r[n-1], \ldots, r[n-k])
$$

where $y[n]$ is the statistical information from the BS and the UE for the communication link between them being observed for the past $k$ times slots.

Our approach of jamming detection is designing a test statistic $\Lambda(y)$ and comparing it with a predefined threshold $\eta$, which can be denoted as: $H_{1}=$ True if $\Lambda(y)>\eta$ and $H_{0}=$ True if $\Lambda(y) \leq \eta$. The test statistic $\Lambda(y)$ and the threshold $\eta$ are determined by the selected machine learning models. Two types of models are proposed and compared: supervised discriminative models and unsupervised anomaly detection models. In the discriminative model, the objective is to maximize $P\left(\Lambda(y)>\eta \mid H_{1}\right)$ and maximize $P\left(\Lambda(y)<\right.$ $\eta \mid H_{0}$ ). In the unsupervised anomaly detection model, the objective is to maximize $P\left(\left(\Lambda(y)>\eta, H_{0}\right) \cap\left(\Lambda(y)<\eta, H_{1}\right)\right)$.

## III. SYSTEM DESCRIPTION

## A. Hardware Platform

The hardware platform used in our implementation of the 5G NSA testbed for experimental data collection is depicted in Fig. 2, and consists of: User Equipment (UE), Base Station (BS), Core Network (CN), Cyber Attack Controller (CAC), Jamming Attack Radio Generator (JARG), and a Jamming Detection and Cyber Inference Model (JDCIM). The CAC generates different types of controlled jamming for training purposes. The JARG module emulates the jamming attacks on the legitimate communication link between UE and BS inside the Radio Frequency (RF) enclosure. The connections between BS and CN, CAC, and JARG are via an ethernet

cable. Detailed information about this setup can be found in [9], [10].
![img-1.jpeg](img-1.jpeg)

Fig. 2: System Hardware Platform Setup
The jamming waveforms are originally generated in MATLAB using the Signal Generation toolbox ${ }^{\mathrm{TM}}$ and converted to Application Resource Bundle (ARB) files compatible with the R\&S SMW2000A Signal Generator, which provides a systematic way to generate PHY signal wave- forms for different wireless technologies. Table I shows the waveforms transmitted at the desired RF center frequency.

TABLE I: Jamming Waveforms Description


The legitimate communication type selected is 5G NSA with NR cell Time Division Duplex (TDD) in band $N 78$ and LTE cell Frequency Division Duplex (FDD) in band $B 1$. The Center Frequency (CF) for the jamming signal is selected at the CF for $N 78(3.49 \mathrm{GHz})$, uplink $B 1(1.95 \mathrm{GHz})$, and downlink $B 1(2.14 \mathrm{GHz})$. Different jamming power levels are chosen to compare their impacts. At these levels, the legitimate communication links are still affected but without a call drop, which is the area of interest for this study.

Three types of machine learning models were constructed and integrated for comprehensive use case coverage. An instantaneous learning-based discriminative model is used for detecting known types of interference with short intervals. A temporal-based neural network model for detecting known types of interference is used to exploit underlying temporal correlations. An unsupervised learning-based anomaly detection model is used for detecting unknown types of jamming. The computational complexity and required number of data samples for training and evaluation of these three types of models increase incrementally. The performance of each type is evaluated using the same dataset generated as described in Table. I, and is detailed in Sec. V.

## B. Supervised Discriminative Model

The designed jamming detection module for known jamming types feeds $y(n)$ in Eq. (1) as the input into a discriminative predictor. A single time-stamp (instantaneous) classification model needs shorter observation time in the on-field application, whereas a temporal-based model reveals underlying
temporal correlations. We have considered the performance for both instantaneous classification and temporal-based learning. Instantaneous classification is built with a single time stamp of data, which has the advantage of fast detection time within one sample period. In our implementation, the duration between consecutive time samples is 180 ms , which can be further reduced by higher performance hardware. Temporalbased learning is based on $k$ consecutive time steps, and thus provides $k$ adjacent data samples as the input for detection. In this work, we employ the LSTM as a temporal-based learning model, which has a chain structure comprising a specific neural network cell structure. The cell consists of three gates: input gate, output gate, and forget gate. The LSTM has a higher computational complexity for training and requires more data samples. In the training stage, the jamming information shown in Table I is automatically recorded and labeled in a local database. The independent variables used as input features to both the instantaneous classification model and the temporal-based model are downlink/uplink bitrate, downlink/uplink packet rate, downlink/uplink retransmission rate, Physical Uplink Shared Channel Signal Quantity and Signal to Interface and Noise Ratio (PUSCH SNR), Channel Quality Indicator (CQI), power headroom, energy per resource element, uplink path loss, downlink/uplink Modulation and Coding Scheme (MCS), and the average turbo decoder rate.

The discriminative models are trained using positive (known target jamming types) and negative cases (no jamming present). However, when the jamming types are unknown, an unsupervised anomaly detection approach is adopted with the model trained only with standard signals (without jamming present). The relationship of the supervised discriminative models and unsupervised anomaly detection model and their usage in our proposed system is shown in Fig. 1.

## C. Unsupervised Model

To identify jamming attacks without prior training on a particular jamming type, a network intrusion detection system is proposed in [12], which is trained only on the normal network traffic and then detects attacks as anomalies. We have utilized the auto-encoder based architecture proposed in [12] to detect previously unseen jamming attacks.

Auto-encoders are trained to recreate the input data. As long as new data follows the same distribution in the feature space as the data it has been previously trained on, the autoencoder can recreate them. Working under the hypothesis that a jamming attack is observed in the feature space, we can expect that the auto-encoder will fail to successfully recreate it and generate a large error that can be detected. The training data comprising only non-interference samples is parsed using the input features described in the previous section. These features are clustered hierarchically and each cluster is passed to an auto-encoder. This gives an ensemble of $d$ auto-encoders, where $d$ is the number of clusters. The root mean squared errors from these auto-encoders are concatenated and passed to another auto-encoder. This secondary auto-encoder amplifies the errors from the ensemble. The overall architecture is

![img-2.jpeg](img-2.jpeg)

Fig. 3: The ensemble of auto-encoders, reproduced from [12].

described in Fig. 3. The output from this auto-encoder, in the range [0, ∞), is bound to the range [0, 1] by passing it through the hyperbolic tangent function to get the output score denoting the probability of jamming presence.

## IV. CAUSALITY ANALYSIS

A BNM is a Directed Acyclic Graph (DAG) that discovers and represents dependencies among random variables from observational data [13]. The objective of the proposed causal inference analysis is to enhance the accuracy of predicting jamming presence and assess its effect on significant quality attributes in various use cases. Due to a partial loss of information in transition from empirical information to conditional probability tables, methods of probabilistic inference from learning data may have shortcomings such as high computational complexity and the cumulative error increasing exponentially as the number of nodes in the DAG increases [14]. To address the computational complexity, in the proposed method, a topology is constructed using both the domain knowledge in wireless networks and reverse engineering of the data in the jamming detection study. Fig. 4 shows indirect, direct, and root cause for the throughput performance through domain knowledge. In DAG-based topology, the relationship and probability from node 'jamming', 'Inaccurate CQI', 'MCS Variance Increase', 'Data Channel Jamming', and the impact to 'Throughput Decrease' are established by domain knowledge and verified by empirical data.

![img-3.jpeg](img-3.jpeg)

Fig. 4: BNM Based Inference for Throughput Degradation

When physical layer jamming is present in the control channel (CCH) dedicated to control information between the UE and the network, the reactions of CQI and MCS are different compared to when the jamming is present in the data channel (DCH) dedicated for data information. As demonstrated in [10], CCH jamming causes the incorrect CQI reported by UE, and further causes the increased variance in the MCS distribution, which does not exist in DCH jamming. Through domain knowledge of the 5G protocol, we know that the MCS value or the range of MCS values are set automatically based on the value of CQI, which establishes the causality relationship between MCS and CQI in Fig. 4. The RF environment and the presence of jamming affect the CQI values reported by UE. The throughput is determined by factors from multiple layers, however, in this study, we prioritize the factors from the physical layer and keep the other factors constant to simplify the structure. Eq. (7) is used to calculate the probability of sentinel event S, given a set of different unobserved (Cn) and observed causes (Ci) to simply the causal relationship. Furthermore, the BNM is used to calculate the probability of observing a cause, in our case, the root cause r, given that an effect (e.g., throughput decrease) has occurred due to the observed causes.

$$P(S|r, C_1, \dots, C_5, C_{u_1}, ..., C_{u_n}) = \sum_{C_n} P(S|r, C_1, \dots, C_5)P(C_{u_1}, \dots, C_{u_n}) = P(S|r, C_1, \dots, C_5)$$

## V. PERFORMANCE EVALUATION

### A. Supervised Jamming Detection Performance

The performance evaluation of the proposed machine learning-based jamming detection models is based on data collected as per Table I. For instantaneous classification, a number of different models are used to compare the performance, namely logistic regression, Gaussian Naive Bayes, K-neighbors classifier, decision tree, and random forest. A train-test split of 75%-25% is used in these evaluations. The accuracy of distinguishing between the cases of jamming present and no jamming present is significantly high with tree-based classification. When detecting the listed jamming types from the no jamming scenarios, the random forest algorithm gives 100% accuracy for all jamming types. The reason behind the superior performance using decision trees is that decision trees or random forest models divide the feature space into smaller and smaller regions, whereas other methods such as logistic regression fit a single line to divide the space exactly into two. The light-weighted tree based classifier enables the possibility of migrating the system to UE or Internet of Things (IoT) devices.

In jamming classification for differentiating types of jamming, tree-based classification shows slightly lower but still significantly high performance. As an overview of the jamming classification methods, the AUC values to detect any specific jamming type against all other scenarios are shown in Fig. 5.

In order to exploit the correlation amongst the adjacent time stamps of data, a temporal-based learning scheme based on the LSTM is also implemented. In our implementation, we use k = 2 consecutive data samples, one belonging to the LTE cell and the other sample from the 5G NR cell. Our LSTM implementation uses a single hidden layer consisting

![img-4.jpeg](img-4.jpeg)

Fig. 5: The Overview of AUC for Each Jamming Type

of 100 LSTM units, followed by a fully-connected layer with 100 nodes, with a final output layer with 2 nodes for binary jamming detection. The precision-recall performance for the temporal-based jamming detector is summarized in Table II.

![img-5.jpeg](img-5.jpeg)

Fig. 6: AUC for each jamming type LSTM-based detection

TABLE II: Temporal-based (LSTM) Detector Performance


We show the performance of the LSTM jamming detector in different jamming scenarios as ROC curves in Fig. 6, with the AUC as a single performance metric to compare with the instantaneous classification models.

For LTE Downlink (DL) band (2140 MHz) jamming at −5 dBm, the performance is lower due to the limited training data sample size. The BNM approach from Sec. IV is used for performance enhancement. When applying the model in Fig. 4 to the LTE DL −5 dBm, the training data shows with presence of control channel (CCH) jamming, the probability of a MCS variance increase detected is 0.845 and inaccurate CQI detected is 0.503. Thus a MCS variance increase being observed, the jamming recall increases to 86.4% and precision to 80.9%.

### *B. Unsupervised Jamming Detection Performance*

To evaluate the performance of the approach described in Sec. III-C, the model was trained on 596 samples of non-interference data. The remaining non-interference data, and samples from several unknown types of jamming, 5G new radio, LTE uplink, with multiple power levels for the LTE interference, were concatenated, totaling to 4125 samples, and used to test the trained model. The proposed model performs remarkably well in detecting the unknown jamming attacks. The per class accuracy are summarized in table III. The approach however fails to detect interference in LTE DL bands. The reason for this becomes apparent by looking at a t-SNE projection of the entire data set. Figs. 7 demonstrates how the LTE uplink and NR interference are separable from the no interference data. But the projection shows that the features for LTE DL and no interference have overlapping distributions and the proposed unsupervised approach lacks the information to distinguish between the two.

![img-6.jpeg](img-6.jpeg)

Fig. 7: The t-SNE projection of the feature space for the interference data

TABLE III: Ensemble auto-encoder Performance


Adversarial training is one of the known vulnerabilities of learning-based approaches. Poisoning the training data with adversarial examples can severely compromise the capability of a learning based model. The effect of poisoning of the training data with jamming samples was evaluated. The first

![img-7.jpeg](img-7.jpeg)

Fig. 8: AUC for unknown jamming with noisy training data

10% phase of the training, during which the feature clustering algorithm runs, is completely resistant to poisoned training data. Beyond that the model can withstand a significant percentage of poisoned training samples with graceful gradual degradation. Fig. 8 demonstrates the results when differing percentage of noise is introduced at the beginning of the training, right after the clustering. In addition, the stage at which the samples are poisoned shows significant impact. The model performance was tested with different fractions of poisoned training data placed at different stages during the training. The AUC performance in this setting is summarized in Fig. 9. As previously stated, the first 10% of the training is immune to poisoning. Beyond that, it is empirically observed that early and late training is significantly more vulnerable compared to the mid-training period. Overall, the proposed model is not only remarkably effective in detecting unknown jamming types, but is also robust against adversarial training.

![img-8.jpeg](img-8.jpeg)

Fig. 9: Temporal effect of the adversarial training

### VI. CONCLUSION

In this work, an anonymous jamming detection and classification scheme is introduced, which is based on monitoring and analysis of cross-layer statistical parameters. In particular, supervised learning based instantaneous classification and temporal-based models are developed along with an unsupervised learning-based anomaly detection approach, which, as separate parts of a combined approach, achieve both high accuracy and robust detection for known and unknown jamming types respectively. A causality analysis approach using BNM is developed to identify the root cause of Key Performance Indicator (KPI) degradation caused by jamming, thus adding transparency to the model. Development of the temporal-based supervised learning jamming detection scheme as well as the extension of the Bayesian inference scheme for a deeper root cause analysis is part of future work.

### ACKNOWLEDGMENT

This work was made possible through the collaboration between Dr. Jeff Reed, the Willis G. Worcester professor in Bradley Department of Electrical and Computer Engineering, and Dr. Laura Freeman, Director of the Hume Center for National Security and Technology's Intelligent Systems Lab in Virginia Tech, funded by Deloitte & Touche LLP's Cyber Strategic Growth Offering led by Deborah Golden.
