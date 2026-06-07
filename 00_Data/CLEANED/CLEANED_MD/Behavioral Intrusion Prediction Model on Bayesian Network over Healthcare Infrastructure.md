# Behavioral Intrusion Prediction Model on Bayesian Network over Healthcare Infrastructure 

Mohammad Hafiz Mohd Yusof ${ }^{1, *}$, Abdullah Mohd Zin ${ }^{2}$ and Nurhizam Safie Mohd Satar ${ }^{2}$<br>${ }^{1}$ Faculty of Computer \& Mathematical Sciences, Universiti Teknologi MARA, 40450, Shah Alam, Selangor, Malaysia<br>${ }^{2}$ Centre for Software Technology and Management (SOFTAM), Universiti Kebangsaan Malaysia, 43600, Bangi, Selangor Malaysia<br>*Corresponding Author: Mohammad Hafiz Mohd Yusof. Email: hafizyusof@uitm.edu.my

Received: 13 September 2021; Accepted: 27 December 2021


#### Abstract

Due to polymorphic nature of malware attack, a signature-based analysis is no longer sufficient to solve polymorphic and stealth nature of malware attacks. On the other hand, state-of-the-art methods like deep learning require labelled dataset as a target to train a supervised model. This is unlikely to be the case in production network as the dataset is unstructured and has no label. Hence an unsupervised learning is recommended. Behavioral study is one of the techniques to elicit traffic pattern. However, studies have shown that existing behavioral intrusion detection model had a few issues which had been parameterized into its common characteristics, namely lack of prior information $(p(\theta))$, and reduced parameters $(\theta)$. Therefore, this study aims to utilize the previously built Feature Selection Model subsequently to design a Predictive Analytics Model based on Bayesian Network used to improve the analysis prediction. Feature Selection Model is used to learn significant label as a target and Bayesian Network is a sophisticated probabilistic approach to predict intrusion. Finally, the results are extended to evaluate detection, accuracy and false alarm rate of the model against the subject matter expert model, Support Vector Machine (SVM), $k$ nearest neighbor ( $k$-NN) using simulated and ground-truth dataset. The ground-truth dataset from the production traffic of one of the largest healthcare provider in Malaysia is used to promote realism on the real use case scenario. Results have shown that the proposed model consistently outperformed other models.


Keywords: Intrusion detection prevention system; behavioral malware analysis; machine learning in cybersecurity; deep learning in intrusion detection system (IDS) and intrusion prevention system (IPS)

## 1 Introduction

Machine learning can be divided into supervised and unsupervised learning. In cybersecurity research, supervised learning has been widely adopted, especially using deep learning [1,2]. This is applied due to the nature of the standard dataset that has been deliberately labelled as normal or

This work is licensed under a Creative Commons Attribution 4.0 International License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.

attack. Arguably, deep learning is the state-of-the-art; however, production network traffic has no label, hence unsupervised learning is recommended [3-5]. Current trend on unsupervised learning over unstructured, especially in bio-technology and statistical computation, is on Bayesian model, specifically the non-parametric Bayesian model [6,7], thus it has motivated this research to explore a solution through Bayesian model.

This unsupervised learning applied in production network is to discover underlying pattern of the network distribution between normal and attack. Behavioral study is one of the techniques to elicit this pattern. Studies have shown that existing network-level behavioral analysis methods suffered a few issues, for instance; lack of distribution modelling refinement processes, limited ground truth testing dataset, non-inferential analysis which leads to the inability to predict zero-day attacks, and produces high-level assumptions [4]. The reduction of millions of instances, disregarded parameters, removed similarities of most of the traffic flows to reduce information noise, insufficient number of optimized features, and ignored instances which do not involve an entity are amongst other problems that have been identified as the main issues contributing to the inability to predict zero-day attacks [8].

Those problems have been parameterized into a few common root-cause characteristics. They lack of priori information $p(\theta)$ and reduced parameters $(\theta)$. Previous methods were proposed to address the problems; however, were still unable to resolve the stated scientific glitches. Due to the shortcomings, the Bayesian Network, in terms of its probabilistic modelling, would be the best method to deal with the stated scientific glitches. The method has been proven in the area of Artificial Intelligence, Clinical Expert Systems, and Pattern Recognition. One of the credible malware analysis studies to have applied the Bayes theorem model was in [9]. However, the model had limited directed conditional probabilities, which could lead to false alarm. Furthermore, in this study, the distribution density model has been fixed, and only one feature, the IP address, has been utilized to build up the model.

Therefore, this study aims to determine the Feature Selection and Distribution Density Model to select the optimal features that will improve the prediction of the behavioral analysis. Subsequently, the Predictive Analytics Model based on Bayesian Network which utilizes the selected optimized features is designed based on the outcome. The final step is to evaluate the model against detection, accuracy, false positive rate and state-of-the-art model. The testing dataset is from production network traffic.

This study has significantly contributed to the construction of; (1) The Feature Selection Model based on distribution density function. Many Intrusion Detection System (IDS) models have used supervised learning from labeled dataset, whilst production traffic is unlabeled and multidimensional. Using maximum likelihood information from the density distribution function, this model will assist the acquisition of the target label during data pre-processing stage. (2) The Predictive Analytics Model based on Bayesian network. This model is arguably the novelty of this research. From the optimized feature, it serves as a prior information for this model. Having this model will allow this prior information to be automatically updated through its posterior probability information. This is the essence of the Machine Learning model whereby the model is able to learn and update itself from data. Detailed discussion is available in the Research Methodology section.

# 2 Literature Review 

Intrusion and malicious software detection in network security has become an important research domain [10]. The emergence of new threats that are stealthy and sophisticated are almost undetectable and not recognized by existing intrusion detection systems, or traditional tools in security layer perimeters (i.e., firewall, antivirus (AV)). These are among the challenges in malware and intrusion

system research. This scenario leads to inefficiency to achieve higher detection rates and reduced false positives in intrusion systems. Signature-based can only detect intrusion based on pattern or signature. Signature-based method primarily focuses on code-structure of the viruses, vs. the dynamic aspects of its behavior [11].

Study in [12] introduced supervision system for the IDS to monitor traffic log. The analysis phase includes data preprocessing, feature selection and finally proactive prediction based on deep learning. The study stated that data perspectives in ML are divided into 1) supervised and 2) unsupervised. Supervised data are a labelled dataset and unsupervised are an unlabeled training or testing dataset. In this study, the pre-processing technique uses time-series multivariate to construct self-supervised data labels.

Research by [13] introduced a model that can learn features from unlabeled dataset and is able to classify simultaneously benign or malicious traffic. It has two stages: 1) to decide normal (benign) or abnormal (malicious) traffic using probability, which will then be used in 2) which is to label certain features as target for the classifier. The first stage is to classify normal or abnormal traffic with probability value by using any distribution or z-score value. Then, in the second stage, the probability value will be used as additional feature or label or target for the transformed dataset for which the multi-classification model can be trained and tested. As a conclusion, the study had introduced feature representation from unlabeled data.

Then study in [14] designed an optimization algorithm for optimizing hidden layers in neural network and then evaluated the algorithm against network intrusion system. Dataset used is NSLKDD, which is for training and testing dataset. This algorithm has been compared against traditional optimization algorithm and subsequently the classification effectiveness was compared with other machine learning model like SVM, Random Forest and Naïve Bayes.

Research by [9] stated that behavioral-based methods are effective in malware detection; hence there is a need for a research toward behavioral-based analysis methods. Behavioral-based analysis is highly related to heuristic approach to speed up the process of finding a satisfactory solution, especially when dealing with real-time traffic [15]. Previous studies have described the issues in this area, namely reduced instances $(\theta)$, and lack of priori $(p(\theta))$. Thus, there is a need for a sophisticated probabilistic interpretation. It can be resolved using Bayesian theorem; a sophisticated probabilistic approach to interpret the uncertainty event that has been proven in Clinical Expert Systems, Artificial Intelligence, Pattern Recognition.

Bayesian Network is known as Belief Network and is the Artificial Intelligence framework for uncertainty supervision, which is a contrast to the deterministic approach to understand phenomena [16]. Although it was published in 1763, the techniques applied in health management and medicine decision-support systems are quite recent; colon biopsy [17] was recently used in the mortality classification of COVID-19 patients [18]. Thus, the gaps discussed previously can be resolved using Bayesian theorem. The latest approach in behavioral malware analysis at network level using Bayes theorem is proposed by [9], which produces high detection rate and low false positive result [19].

However, the current method may lead to inability to detect unknown attacks [20]. The first factor is the distribution density model proposed by [9], which only focused on one feature, which will affect the accuracy of classification results [21]. The second factor is the distribution density model strategy used by [9], which is fixed with Gamma function and it is not flexible [22] and may not follow sample weights [23]. The third factor is the predictive model used by Weaver, which is based on naïve Bayes analysis method to model scanning behavior of Conficker Botnet in large Internet Service Provider (ISP) network. However, studies by [17] stated that the use of the Bayesian Network method may

improve the result of prediction. Thus, this research is to extend the previous works in [8] which has established the Feature Selection Model. The model is utilized to obtain optimized features which are subsequently used in this proposed model. Reference in [3] highlights some of the preliminary studies of this work.

# 3 Research Methodology 

This section introduces the research methodology framework to execute the study. Altogether, there are four stages to complete the research activities; which are (1) ground-truth dataset acquisitions, (2) modelling, (3) testing, and (4) evaluation. Stage 1, which is the ground-truth dataset acquisitions, will include profiling the baseline, spike, decay after disinfections, and decay after spike. Stage 2 is to design feature selection and distribution density model for which to obtain optimized lambda information. Stage 3 is the design of the predictive analytics model based on Bayesian Network method. Finally, Stage 4 is the testing and evaluation, whereby the predictive analytics model is evaluated against the ground-truth traffic. The discussion will be presented in the Results and Discussions section. The following section will discuss each stage in detail.

### 3.1 Stage 1: Ground-truth Dataset Acquisitions

This stage is to acquire the ground-truth dataset from the largest healthcare provider in Malaysia. 
Figure~1 shows the network physical diagram of the provider. 
The dataset is in the form of a packet capture (PCAP) file of live production network traffic. 
It will be used to train the predictive model. 
The first task is to acquire site permission, then to acquire the baseline (normal) dataset from the site over the configured switched port analyzer (SPAN) port. 
Next, Suspicious Objects (SOs) are acquired from the Trend Micro Deep Discovery Inspector (TMDDI) on the specified date: $24^{\text{th}}$ August, 2017. 
Then, attack procedures are simulated using a Virtual Machine, after which the PCAP file of the attacked network traffic is retrieved via Wireshark. 
This is used to baseline the detection threshold of the predictive model. 
The final step is to draw the distribution functions over the raw data and analyze them.

Raw ground-truth dataset is grouped into baseline, spike, decay, and decay after disinfection, and decay after spike attributes. 
Beta, Gamma and Normal distribution models are used to characterize the baseline dataset. 

Equation (1) shows the Gamma distribution model, which is applied throughout the baseline dataset of 
$q_{\text{baseline\_win\_size}}, \; q_{\text{baseline\_frame\_len}}, \; q_{\text{baseline\_delta\_time}}, \; q_{\text{baseline\_dst\_src}}$:

$$
\text{Gamma}\bigl(\lambda_{\text{baseline\_win\_size}} ; \alpha, \beta \bigr) 
= \frac{1}{\Gamma(\alpha)} \, \beta^{\alpha} \, 
\lambda_{\text{baseline\_win\_size}}^{\alpha-1} \,
\exp\bigl(-\beta \, \lambda_{\text{baseline\_win\_size}}\bigr).
\tag{1}
$$

Equation (2) shows the Beta distribution model, which is also applied across the baseline dataset:

$$
\text{Beta}\bigl(\lambda_{\text{baseline\_win\_size}} ; \alpha, \beta \bigr) 
= \frac{1}{B(\alpha,\beta)} \, \lambda_{\text{baseline\_win\_size}}^{\alpha-1} \,
\bigl(1 - \lambda_{\text{baseline\_win\_size}}\bigr)^{\beta-1}, 
\quad 0 < \lambda_{\text{baseline\_win\_size}} < 1.
\tag{2}
$$

Finally, the Normal distribution model applied to the same baseline dataset is given in Equation (3):

$$
\text{Norm}\bigl(\lambda_{\text{baseline\_win\_size}} ; \mu, \sigma^2 \bigr) 
= \frac{1}{\sqrt{2 \pi \sigma^2}} \,
\exp\!\left( -\frac{(\lambda_{\text{baseline\_win\_size}} - \mu)^2}{2\sigma^2} \right).
\tag{3}
$$

![img-0.jpeg](img-0.jpeg)

Figure 1: Physical network diagram of the healthcare provider in Malaysia

Table 1: Ground-truth dataset sampling


# 3.2 Stage 2: Feature Selection and Density Distribution Function Modelling 

Several method specifications were identified as weights of classifier to rank the feature for their removal [24]. Let $w_{j}$ be defined as in Eq. (4).
$w_{j}=\frac{\mu_{j}(+)-\mu_{j}(-)}{\sigma_{j}(+)+\sigma_{j}(-)}$
Eq. (4) can be used as a ranking criteria to sort features. Another weighted score is the true normal score; whereby, in order to create a normal profile, it is necessary to index each attribute's instances as $i=1,2, \ldots, n$. The model was built based on the ratio of the normal number of training data $\left(R_{i}\right)$

against the total number of packets associated with each attribute $\left(N_{i}\right)$. The probability of the normal score, $P_{i}=R_{i} / N_{i}$ is represented by Eq. (5).
$p_{i}=\sum_{i=1}^{n} \frac{R_{i}}{N_{i}}, i=1,2,3, \ldots, n$
Another ranking criteria principle is the correlation coefficient, also known as the Pearson correlation. Correlation coefficient ranking is able to identify linear dependencies between the target and the variables. The Pearson correlation coefficient $(r)$ is defined in Eq. (6).
$r=\frac{1}{n-1} \sum_{i=1}^{n}\left(\frac{x_{i}-\mu_{i}}{\sigma_{x}}\right)\left(\frac{y_{i}-\mu_{y}}{\sigma_{y}}\right)$
The selected features will be normalized through the following Eq. (7).
baseline_ $f_{i}$ _beta $=10^{-x} \sum_{\text {baseline }_{i} f_{i} \text { _beta }=1}^{n}(-)\left(\log _{10}\right.$ baseline_ $f_{i}$ _beta $)$
At this stage, the model will be first trained using KKD Cup 99 dataset, which includes a wide variety of simulated intrusion scenarios in a military network environment specifically simulating typical U.S Air Force, Local Area Network (LAN). To obtain optimized features, the maximum likelihood function as defined in Eq. (8) is utilized. This work has been published in previous work in [8]. Then, it will be used to extract optimized features from the ground truth dataset of the largest healthcare provider in Malaysia.

$$
\begin{aligned}
& \text { Maximumlikelihood, } \mathbb{1}_{f_{i} \text { beta }}=\ln \left[\sum_{f_{j}=1}^{n} \frac{1}{\text { Beta }(\alpha, \beta)} \lambda_{f_{j}}^{\alpha-1} \cdot\left(1-\lambda_{f_{j}}\right)^{\beta-1}\right] \\
& =(\alpha-1) \sum_{f_{j}=1}^{n} \ln \left(f_{i}\right)+(\beta-1) \cdot \sum_{f_{j}=1}^{n} \ln \left(1-f_{i}\right)-N \cdot \ln (\operatorname{Beta}(\alpha, b))
\end{aligned}
$$

Finally, the optimized features of the ground truth from the real use case of Malaysia healthcare provider is shown in Tab. 2.

Table 2: Variable notations


# 3.3 Stage 3: Predictive Analytics Modelling Based on Bayesian Network 

Statistically, a Bayesian Network model has four properties, which are (1) prior probability or priori, (2) the likelihood or the conditional probability, (3) posterior probability or posteriori as shown in Eq. (9), and (4) the relationship of parents' nodes and its inheritance.

$p(\theta \mid y) \propto p(y \mid \theta) \cdot p(\theta)$
Bayesian Network is a directed acyclic probabilistic model, and conditional probability is the nucleus of the model. It is a probabilistic causal network also known as Belief Network. It is used as an Artificial Intelligence framework for uncertainty supervision, which is contrary to the deterministic approach to understand phenomena [16].

For the proposed model, it starts with the following Eq. (10) of the Joint Probability function. $\operatorname{Pr}(b w s)$ refers to the baseline window size, $\operatorname{Pr}(b f l)$ refers to the baseline frame length, and $\operatorname{Pr}(b d t)$ refers to the baseline delta time. $B T$ is the probability of baseline traffic, and comprises of all the baseline traffic intersections, and $M$ is the probability of malicious traffic where all of these at a later stage will be defined as lambda information.
$\operatorname{Pr}(b w s, b f l, b d t, B T, M)=\operatorname{Pr}(b w s) \cdot \operatorname{Pr}(b f l) \cdot \operatorname{Pr}(b d t) \cdot \operatorname{Pr}(B T \dashv \mid b w s, b f l, b d t) B T \cdot \operatorname{Pr}(M \mid B T)$
These notions are the ground-truth dataset which have been trained in Stage 2. The model can be written in its conditional probability as derived in the following forms in Eqs. (11) to (15). This brute force notation is supplied to the classifier engine.
$\operatorname{Pr}(b w s)=\lambda$ baseline_win_size
$\operatorname{Pr}(b f l)=\lambda$ baseline_frame_length
$\operatorname{Pr}(b d t)=\lambda$ baseline_delta_time
$\operatorname{Pr}(B T)=\lambda B T$
$\operatorname{Pr}(M)=\lambda M$
Eqs. (11) to (15) is the prior information of the proposed model. It is taken from the density distribution information which was sourced from Stage 2 research activity. The following are the generated posterior probability or posteriori. The posteriori will be updated when the prior information is updated. Having this feature will allow the model to be automatically updated.
$\operatorname{Pr}(B T$ and $b w s)=\operatorname{Pr}(b w s) * \operatorname{Pr}(\operatorname{Pr}(B T) \mid b w s)$
$\operatorname{Pr}(\operatorname{Pr}(B T) \mid b w s)=\frac{\operatorname{Pr}(B T \text { and } b w s)}{\operatorname{Pr}(b w s)}$
$\operatorname{Pr}(B T$ and $b w s)=(\operatorname{Pr}(B T) * \operatorname{Pr}(b w s)) /(\operatorname{Pr}(B T) * \operatorname{Pr}(b w s))+(\operatorname{Pr}(` B T) * \operatorname{Pr}(b w s))$
$\operatorname{Pr}(\operatorname{Pr}(B T) \mid b w s)=((\operatorname{Pr}(B T) * \operatorname{Pr}(b w s)) /(\operatorname{Pr}(B T) * \operatorname{Pr}(b w s))+(\operatorname{Pr}(` B T) * \operatorname{Pr}(b w s)) / \operatorname{Pr}(b w s)$
$\operatorname{Pr}(B T$ and $b f l)=\operatorname{Pr}(b f l) * \operatorname{Pr}(\operatorname{Pr}(B T) \mid b f l)$
$\operatorname{Pr}(\operatorname{Pr}(B T) \mid b f l)=\frac{\operatorname{Pr}(B T \text { and } b f l)}{\operatorname{Pr}(b f l)}$
$\operatorname{Pr}(B T$ and $b f l)=(\operatorname{Pr}(B T) * \operatorname{Pr}(b f l)) /(\operatorname{Pr}(B T) * \operatorname{Pr}(b f l))+(\operatorname{Pr}(` B T) * \operatorname{Pr}(b f l))$

$$
\operatorname{Pr}(\operatorname{Pr}(B T) \mid b f l)=((\operatorname{Pr}(B T) * \operatorname{Pr}(b f l)) /(\operatorname{Pr}(B T) * \operatorname{Pr}(b f l))+(\operatorname{Pr}(B T) * \operatorname{Pr}(b f l)) / \operatorname{Pr}(b f l)
$$

$\operatorname{Pr}(B T$ and $b d t)=\operatorname{Pr}(b d t) * \operatorname{Pr}(\operatorname{Pr}(B T) \mid b d t)$
$\operatorname{Pr}(\operatorname{Pr}(B T) \mid b d t)=\frac{\operatorname{Pr}(B T \text { and } b d t)}{\operatorname{Pr}(b d t)}$
$\operatorname{Pr}(B T$ and $b d t)=(\operatorname{Pr}(B T) * \operatorname{Pr}(b d t)) /(\operatorname{Pr}(B T) * \operatorname{Pr}(b d t))+(\operatorname{Pr}(B T) * \operatorname{Pr}(b d t))$
$\operatorname{Pr}(\operatorname{Pr}(B T) \mid b d t)=((\operatorname{Pr}(B T) * \operatorname{Pr}(b d t)) /(\operatorname{Pr}(B T) * \operatorname{Pr}(b d t))+(\operatorname{Pr}(B T) * \operatorname{Pr}(b d t)) / \operatorname{Pr}(b d t)$
Eqs. (16) to (18) are the conditional probabilities between $\operatorname{Pr}(b w s)$ - baseline window size, $\operatorname{Pr}(b f l)$ baseline frame length, $\operatorname{Pr}(b d t)$ - baseline delta time, $\operatorname{Pr}(B T)$ - benign baseline, and $\operatorname{Pr}(M)$ - malicious baseline.

It begins with this general expression, for instance; $\operatorname{Pr}(B T$ and $b d t)=\operatorname{Pr}(b d t) * \operatorname{Pr}(\operatorname{Pr}(B T) \mid b d t)$. Then, this equation; $\operatorname{Pr}(\operatorname{Pr}(B T) \mid b d t)$ is unknown. Algebraically, the equation can be reversed into $\operatorname{Pr}(\operatorname{Pr}(B T) \mid b d t)=\frac{\operatorname{Pr}(B T \text { and } b d t)}{\operatorname{Pr}(b d t)}$. Next, the numerator can be expanded into $\operatorname{Pr}(B T$ and $b d t)=$ $(\operatorname{Pr}(B T) * \operatorname{Pr}(b d t)) /(\operatorname{Pr}(B T) * \operatorname{Pr}(b d t))+(\operatorname{Pr}(B T) * \operatorname{Pr}(b d t)$. Substitute this expanded numerator into $\operatorname{Pr}(\operatorname{Pr}(B T) \mid b d t)=\frac{\operatorname{Pr}(B T \text { and } b d t)}{\operatorname{Pr}(b d t)}$ and finally the full expression is shown in Eq. (18). This set of expressions can be optimized into a single equation as shown in Eq. (19). This final representation ensures the translation of expressions into code will be much easier during implementation.

$$
\begin{aligned}
\operatorname{Pr}(B T \text { and } b w s, b f l, b d t)= & \operatorname{Pr}(b w s) * \operatorname{Pr}(\operatorname{Pr}(B T) \mid b w s)+\operatorname{Pr}(b f l) * \operatorname{Pr}(\operatorname{Pr}(B T) \mid b f l) \\
& +\operatorname{Pr}(b d t) * \operatorname{Pr}(\operatorname{Pr}(B T) \mid b d t)
\end{aligned}
$$

$\operatorname{Pr}(\operatorname{Pr}(B T) \mid b w s, b f l, b d t)=\frac{\operatorname{Pr}(B T \text { and } b w s)+\operatorname{Pr}(B T \text { and } b f l)+\operatorname{Pr}(B T \text { and } b d t)}{\operatorname{Pr}(b w s)+\operatorname{Pr}(b f l)+\operatorname{Pr}(b d t)}$
$\operatorname{Pr}(B T$ and $b w s, b f l, b d t)=[(\operatorname{Pr}(B T) * \operatorname{Pr}(b w s)) /(\operatorname{Pr}(B T) * \operatorname{Pr}(b w s))+(\operatorname{Pr}(B T) * \operatorname{Pr}(b w s))]$

$$
\begin{aligned}
& +[(\operatorname{Pr}(B T) * \operatorname{Pr}(b f l)) /(\operatorname{Pr}(B T) * \operatorname{Pr}(b f l))+(\operatorname{Pr}(B T) * \operatorname{Pr}(b f l))] \\
& +[(\operatorname{Pr}(B T) * \operatorname{Pr}(b d t)) /(\operatorname{Pr}(B T) * \operatorname{Pr}(b d t))+(\operatorname{Pr}(B T) * \operatorname{Pr}(b d t))]
\end{aligned}
$$

$\operatorname{Pr}(\operatorname{Pr}(B T) \mid b w s, b f l, b d t)=([(\operatorname{Pr}(B T) * \operatorname{Pr}(b w s)) /(\operatorname{Pr}(B T) * \operatorname{Pr}(b w s))+(\operatorname{Pr}(B T) * \operatorname{Pr}(b w s)]$

$$
\begin{aligned}
& +[(\operatorname{Pr}(B T) * \operatorname{Pr}(b f l)) /(\operatorname{Pr}(B T) * \operatorname{Pr}(b f l))+(\operatorname{Pr}(B T) * \operatorname{Pr}(b f l)] \\
& +[(\operatorname{Pr}(B T) * \operatorname{Pr}(b d t)) /(\operatorname{Pr}(B T) * \operatorname{Pr}(b d t)) \\
& +(\operatorname{Pr}(B T) * \operatorname{Pr}(b d t)]) /(\operatorname{Pr}(b w s)+\operatorname{Pr}(b f l)+\operatorname{Pr}(b d t))
\end{aligned}
$$

The next step is to resolve the set of conditional probability between probability of benign baseline $(\operatorname{Pr}(B T))$ and malicious baseline $(\operatorname{Pr}(M))$; or $\operatorname{Pr}(M$ and $B T)$. Hence, the equation needs to consider prior information of $\operatorname{Pr}(b w s), \operatorname{Pr}(b f l)$ and $\operatorname{Pr}(b d t)$.
$\operatorname{Pr}(M$ and $B T, b w s)=(\operatorname{Pr}(M) * \operatorname{Pr}(B T \mid M))+(\operatorname{Pr}(M) * \operatorname{Pr}(\operatorname{Pr}(b w s) \mid M))$

$$
\begin{aligned}
\operatorname{Pr}(\operatorname{Pr}((B T, b w s) \mid M)) & =\frac{\operatorname{Pr}(M \text { and } B T, b w s)}{\operatorname{Pr}(M)} \\
\operatorname{Pr}(M \text { and } B T, b w s)= & ((\operatorname{Pr}(M) * \operatorname{Pr}(B T, b w s)) /[(\operatorname{Pr}(M) * \operatorname{Pr}(B T, b w s)) \\
& +(\operatorname{Pr}(\operatorname{PrimeM}) * \operatorname{Pr}(B T, b w s))]+[(\operatorname{Pr}(M) * \operatorname{Pr}\left(B T^{\prime}, b w s\right)) \\
& \left.+\left(\operatorname{Pr}(\operatorname{PrimeM}) * \operatorname{Pr}\left(B T^{\prime}, b w s\right)\right)\right] \\
\operatorname{Pr}(\operatorname{Pr}(B T, b w s) \mid M)= & (\operatorname{Pr}(M) * \operatorname{Pr}(B T, b w s)) /[(\operatorname{Pr}(M) * \operatorname{Pr}(B T, b w s)) \\
& +(\operatorname{Pr}(M) * \operatorname{Pr}(B T, b w s))] \\
& +[(\operatorname{Pr}(M) * \operatorname{Pr}\left(B T^{\prime}, b w s\right)) \\
& \left.+\left(\operatorname{Pr}(M) * \operatorname{Pr}\left(B T^{\prime}, b w s\right)\right)\right] / \operatorname{Pr}(M)
\end{aligned}
$$

$\operatorname{Pr}(M$ and $B T, b f l)=(\operatorname{Pr}(M) * \operatorname{Pr}(B T \mid M))+(\operatorname{Pr}(M) * \operatorname{Pr}(\operatorname{Pr}(b f l) \mid M))$
$\operatorname{Pr}(\operatorname{Pr}((B T, b f l) \mid M))=\frac{\operatorname{Pr}(M \text { and } B T, b f l)}{\operatorname{Pr}(M)}$
$\operatorname{Pr}(M$ and $B T, b f l)=((\operatorname{Pr}(M) * \operatorname{Pr}(B T, b f l)) /[(\operatorname{Pr}(M) * \operatorname{Pr}(B T, b f l))$

$$
\begin{aligned}
& +(\operatorname{Pr}(\operatorname{PrimeM}) * \operatorname{Pr}(B T, b f l))]+[\left(\operatorname{Pr}(M) * \operatorname{Pr}\left(B T^{\prime}, b f l\right)\right) \\
& \left.+\left(\operatorname{Pr}(\operatorname{PrimeM}) * \operatorname{Pr}\left(B T^{\prime}, b f l\right)\right)\right] \\
& \operatorname{Pr}(\operatorname{Pr}(B T, b f l) \mid M)=(\operatorname{Pr}(M) * \operatorname{Pr}(B T, b f l)) /[(\operatorname{Pr}(M) * \operatorname{Pr}(B T, b f l)) \\
& \left.+\left(\operatorname{Pr}(\operatorname{PrimeM}) * \operatorname{Pr}(B T, b f l)\right)\right]+\left[(\operatorname{Pr}(M) * \operatorname{Pr}\left(B T^{\prime}, b f l\right)\right) \\
& \left.+\left(\operatorname{Pr}(\operatorname{PrimeM}) * \operatorname{Pr}\left(B T^{\prime}, b f l\right)\right)\right] / \operatorname{Pr}(M)
\end{aligned}
$$

$\operatorname{Pr}(M$ and $B T, b d t)=(\operatorname{Pr}(M) * \operatorname{Pr}(B T \mid M))+(\operatorname{Pr}(M) * \operatorname{Pr}(\operatorname{Pr}(b d t) \mid M))$
$\operatorname{Pr}(\operatorname{Pr}((B T, b d t) \mid M))=\frac{\operatorname{Pr}(M \text { and } B T, b d t)}{\operatorname{Pr}(M)}$
$\operatorname{Pr}(M$ and $B T, b d t)=((\operatorname{Pr}(M) * \operatorname{Pr}(B T, b d t)) /[(\operatorname{Pr}(M) * \operatorname{Pr}(B T, b d t))$

$$
\begin{aligned}
& +\left(\operatorname{Pr}(M) * \operatorname{Pr}(B T, b d t)\right)\right]+\left[\left(\operatorname{Pr}(M) * \operatorname{Pr}\left(B T^{\prime}, b d t\right)\right)\right. \\
& \left.+\left(\operatorname{Pr}(M) * \operatorname{Pr}\left(B T^{\prime}, b d t\right)\right)\right] \\
& \operatorname{Pr}(\operatorname{Pr}(B T, b d t) \mid M)=\left(\operatorname{Pr}(M) * \operatorname{Pr}(B T, b d t)\right) /[(\operatorname{Pr}(M) * \operatorname{Pr}(B T, b d t)) \\
& \left.+\left(\operatorname{Pr}(M) * \operatorname{Pr}(B T, b d t)\right)\right]+\left[\left(\operatorname{Pr}(M) * \operatorname{Pr}\left(B T^{\prime}, b d t\right)\right)\right. \\
& \left.+\left(\operatorname{Pr}(M) * \operatorname{Pr}\left(B T^{\prime}, b d t\right)\right)\right] / \operatorname{Pr}(M)
\end{aligned}
$$

These equations should be optimizable. This is to reduce the number of parameters in the equation(s), which will utilize less memory and will speed up the computational process. For instance, Eq. (16) $\operatorname{Pr}(\operatorname{Pr}(B T) \mid b w s)=((\operatorname{Pr}(B T) * \operatorname{Pr}(b w s)) /(\operatorname{Pr}(B T) * \operatorname{Pr}(b w s))+(\operatorname{Pr}(B T) * \operatorname{Pr}(b w s)) / \operatorname{Pr}(b w s)$ has redundant parameters in the denominator. $\operatorname{Pr}(b w s)$ is mentioned twice. Take it outside the equation and it can be eliminated by the same parameter in the numerator. The final equation is as shown in Eq. (23)
$\operatorname{Pr}(\operatorname{Pr}(B T) \mid b w s)=\operatorname{Pr}(B T) /[\operatorname{Pr}(B T)+\operatorname{Pr}(B T)]) / \operatorname{Pr}(b w s)$

# 3.4 Stage 4: Evaluation Matrix 

The first evaluation stage is by comparing the proposed predictive analytics model that is trained using the ground truth dataset against the Poisson inter-arrival modelling that is used as the testing simulated traffic. Suppose a simulation of $n$ packet of connection is observed as packet $_{1}$, packet $_{2}, \ldots$, packet $_{n}$; this connection's win_size is modelled as Poisson function, as shown Eq. (24).

$$
\begin{aligned}
& \text { Poisson }\left(\text { packet }_{n} ; \lambda_{\text {packet }_{\text {winsize }}}\right) \\
& =e^{-\lambda_{\text {packet } \_ \text {win_size }}} \cdot \frac{\lambda_{\text {packet }_{n}}^{\text {packet }}}{p a c k e t_{n}!}
\end{aligned}
$$

where $\lambda_{\text {packet } \_ \text {win_size }}$ is the mean of the packet's window size, the distribution of the mean is modelled as Gamma and Beta as in Eq. (25) following the raw data analysis.

$$
\begin{aligned}
& \text { Gamma } \sim\left(\lambda_{\text {packet }_{\text {winsize }}} ; \alpha, \beta\right) \\
& =\frac{1}{\text { Gamma }(\alpha)} \cdot \beta^{\alpha} \cdot \lambda_{\text {packet }_{\text {win_size }}}^{a-1} \cdot \exp ^{-\beta \cdot \lambda_{\text {packet } \_ \text {win_size }}}
\end{aligned}
$$

Then, the traffic will be flagged as true positive $(T P)$, true negative $(T N)$, false positive $(F P)$, and false negative $(F N)$. These flags will be used to evaluate accuracy, detection rate and false alarm rate (FAR). Detection rate, on the other hand, is used to measure true positive traffic over the sum of true positive and false traffic (positive traffic wrongly classified as negative, and negative traffic wrongly classified as positive). The formula is the following Eq. (26).
DetectionRate, $D R=\frac{T P}{T P+F N}$
Accuracy is used to measure all true traffic, which consists of the sum of the true positive $(T P)$ and true negative $(T N)$ over the sum of all traffic of a true positive $(T P)$, true negative $(T N)$, false positive $(F P)$ and false negative (FN) nature. The formula is denoted as the following Eq. (27).
Accuracy $=\frac{T P+T N}{T P+T N+F P+F N}$

Finally, the false alarm rate (FAR) is used to measure the false positive $(F P)$ alarm, which signifies true negative $(T N)$; the negative traffic that was wrongly classified as positive. In this research, positive traffic that was wrongly classified as negative also will be considered as a false alarm and the rate will be measured. This is a very serious issue because it may cause an attack vector. The formula is denoted as the following Eq. (27).
False AlarmRate, $F A R=\frac{F P}{F P+T N}$
Prior to that, the baseline traffic will be compared against the threshold, which, according to Weaver in [4], can be done through hard setting, heuristically, or probabilistic relationships. However, in [4], it is mentioned that probabilistic relationships will give more statistically rigorous results. For this research, the threshold will be set both by probabilistic relationships and by hard setting. For simulated traffic, it is set to a quarter $\left(1 / 4\right)$ of the baseline traffic.

Next, the model will be tested against another testing ground truth dataset based on the real use case in Malaysian healthcare provider, as shown in Fig. 2. This figure illustrates a year of observation of the ground-truth dataset uses HGIGA ${ }^{\circledR}$ load balancer from August 2016 until August 2017. The sample was acquired at different occasions. Sample traffic were captured early October 2016, early Jan 2017, early May 2017 and in August 2017. The samples represent different traffic conditions, namely baseline, attack and after-disinfection. Next, it will be tested against other classification models, SVM and $k$-NN.
![img-1.jpeg](img-1.jpeg)

Figure 2: Ground truth testing dataset sampling activity

# 4 Results and Discussion 

Fig. 3 shows correlation heat map matrix of the KDD dataset. 22; 'count', 23; 'srv_count', 24; 'serror_rate', 25; 'srv_serror_rate', 26; 'rerror_rate' and 39; 'dst_host_rerror_rate' are the labelled features. Light (white) plots depict relatively low correlation, and dark (blue) plots depict high correlation. High correlation is the relationship between two variables at upward trending (positive relationship). Here, it is observed that high relationship between source and destination endpoints' transactions, size and counts. The attributes like 'count' and 'srv_count', 'dst_host_same_src_port_rate' and 'srv_count', 'serror_rate' and 'dst_host_serror_rate', and 'rerror_rate' and 'dst_host_rerror_rate' describe the features of source and destination endpoints' transactions, size and counts with $98 \%$ to $99 \%$ correlation.

This is the lead to select and process the ground truth dataset, whereby the final selected features were $q_{\text {baseline_win_size }}, q_{\text {baseline_frame_len, }}$ and $q_{\text {baseline_delta_time. }}$. Detailed discussion on Feature Selection Model is explained in paper [8].
![img-2.jpeg](img-2.jpeg)

Figure 3: Correlation heat map for KDD dataset
The PCAP files were extracted from the baseline Transmission Control Protocol or User Datagram Protocol (TCP/UDP) traffic of the live production network from a Malaysian healthcare provider. This is conducted during Stage 1 of the research activity. Graphs in Fig. 4 below are the

bar plotted for baseline traffic. The graphs show the baseline traffic of window size, frame length, delta time, and source and destination traffic distribution.
![img-3.jpeg](img-3.jpeg)

Figure 4: Descriptive analysis of baseline traffic
If a network administrator observes these graphs over the available state-of-the-art, signaturebased CNMS (Centralized Network Monitoring System), they could conclude some normalcy over its distribution. Further analysis procedure is to be compared with the spike (attacked network distribution). This could lead into different outcomes and conclusions.

# 4.1 Comparison Results of the Proposed Distribution Function Against the One Feature Model 

Fig. 5A shows the dataset from the descriptive analysis is further analyzed using distribution function, as discussed in Stage 2 of the research activity. This figure is on Normal distribution $\sim$ (baseline_win_size $_{x} ; \lambda_{\text {baseline_win_size }}, \sigma^{2}$ ) function where the mean, $\lambda_{\text {baseline_win_size }}$, and the variance, $\sigma^{2}$ ( $\sigma$ is the standard deviation) are fitted by the normal MLE (maximum likelihood) as shown in the Data vs. Density graph above. QQ plot graph (quantile-quantile plot) suggests that the distribution is not normally distributed.

Fig. 5B shows the Beta distribution analysis, which the unknown parameters; shape $1 \alpha$ (alpha) and shape $2 \beta$ (beta), are fitted by the normal MLE (maximum likelihood) as shown in the Data vs. Density graph. Meanwhile, Fig. 5C shows the Gamma distribution analysis, Gamma $\sim\left(\lambda_{\text {baseline_win_size }} ;\right.$ $\alpha_{\text {baseline_win_size_gamma }}, \beta_{\text {baseline_win_size_gamma }}$ ) where the mean, $\lambda_{\text {baseline_win_size }}$, and the unknown parameters; shape $\alpha_{\text {baseline_win_size_gamma }}$ rate, and $\beta_{\text {baseline_win_size_gamma }}$ are also fitted by the normal MLE (maximum likelihood),

as shown in the Data vs. Density graphs. This analysis will then be replicated against the other selected features.
![img-4.jpeg](img-4.jpeg)

Figure 5: Goodness of fit information of baseline traffic
One feature's model previously fitted the distribution function to Gamma. This study processes the selected features against several distribution functions to get optimized results. As a result, proposed model of Normal distribution scored optimum likelihood value (the least score) of 762.3 as compared to Weaver's [9] Gamma distribution chosen model with the score of 874.6. In this case, optimum or maximum likelihood indicates the optimized selection at the very least mean score. For

the remaining baseline features, the proposed model scored certain optimum likelihood values, which are not available in the state-of-the-art model. AIC is the Akaike's Information Criterion to measure error and the same goes to BIC (the Bayesian Information Criterion) [10]. Lowest AIC and BIC scores indicate the least error measured. Proposed model AIC scored value is -1520.5 whereas Weaver in [9] scored -1745.2 . Error measurement shows that the proposed model has +0200.0 slightly higher value than in [9]. However, the idea of having the best mean value has been met with the likelihood function, which estimates the maximum likelihood mean. Tab. 3 summarizes the differences of distribution function modelling between the proposed model and the subject matter expert.

Table 3: Comparison of the proposed distribution model against one feature's model


Table 3: Continued


# 4.2 Classification Results Against Simulated Dataset 

Next, is to use the optimized features from Stage 2 and fit it into the predictive analytics model as discussed in Stage 3 of the research activity. This model is used to test against simulated dataset. The traffic was generated using Poisson function for inter-arrival modelling and will be optimized using Gamma distribution function as discussed in Stage 4 of the research activity. The prior information (lambda information) of the traffic is illustrated in Tab. 4. This lambda information and its initial value has been selected and optimized using the feature selection and density distribution model as discussed in Stage 2 of the research activity.

Table 4: Lambda information of the baseline dataset


This is the followed by two designed scenarios to simulate the traffic. First, the traffic is generated using the Poisson model as mentioned before. The system then sets the threshold of the attacked traffic at an additional of $23 \%$ higher from the baseline. Then, the model is run and evaluated in accordance to the evaluation matrix. The result is shown in Tab. 5.

From Tab. 5, the threshold will flag more true positive traffic or simply true traffic. From here, the additional $23 \%$ traffic will still indicate $100 \%$ accuracy that all traffic is a true positive; with $100 \%$ detection rate and $0 \%$ false alarm rate. In the second and final scenario, this is where the amount of $\operatorname{Pr}(b w s)$ of the simulated traffic (trained traffic) is increased by $50 \%$. The results are as in Tab. 6.

A tuple of lambda $\boldsymbol{P r}(\boldsymbol{b w s})$ which is contained with malicious traffic had exceeded the threshold; a significant outcome. It will trigger the malicious alarm and it will be flagged as true negative traffic or simply true traffic. This will generate a bunch of true negative traffic based on the model. However, there are several tuples, which indicate a true positive traffic and this is true, as their lambda information does not exceed the threshold. This is considered a false alarm. To measure this, false alarm rate equation, which measures the false alarm over the whole traffic, is used. Here, the false

alarm rate is at $27 \%$. However, the detection rate (of detecting true traffic) is still at $73 \%$; a significantly high probability rate.

Table 5: Baseline dataset tested against simulated traffic with $23 \%$ threshold


Table 6: Baseline dataset tested against simulated traffic with $50 \%$ increase in traffic tuple


# 4.3 Predictive Analysis Results Against Ground Truth Dataset 

The next step is to use the optimized features and to fit it into the predictive analytics model as discussed in Stage 4 of the research activity. This model is used to test over the real use case scenario of an attacked dataset from the Malaysian healthcare provider as shown in Fig. 2 of Stage 4 of the research activity. The figure shows the testing dataset sampling extracted from the HGIGA ${ }^{\circledR}$ internet traffic utilization monitoring system dashboard. It also shows the attacked traffic were ranged from early May until early July 2017. Later attacked traffic will be set as a threshold value for the model.

Traffic in August 2017 on the other hand was sampled as a baseline traffic. Traffic in October 2016 and early January 2017 will be studied to model its distribution.

The distribution characteristics of this testing traffic dataset were then recorded. The selected features were extracted during the feature selection phase and three optimized features were selected, namely $\lambda_{\text {frame_len }}$, for frame length lambda, $\lambda_{\text {sim_size }}$ for window size lambda and $\lambda_{\text {delta_time }}$ for delta time lambda. These are the same selected features from the same feature selection model discussed in Stage 2 of the research activity.

The October traffic could be considered as benign traffic as it is way below the spike threshold. Generally, a threshold is used in many behavioral researches. For instance Weaver in [9] suggested that instead of hard setting the threshold heuristically, probabilistic relationship will give a more statistically rigorous outcome. Thus, in this research, the threshold is set by both probabilistic relationships and hard setting threshold. Hence, the quarter ( $1 / 4$ ) baseline rate was chosen to condition the prediction rate of more than $20 \%$ before the attack. In this section, the results have been discussed by applying the predictive model against the ground truth testing datasets. We run the dataset against our model and the result is summarized in Fig. 6. It is apparent that the proposed predictive analytics model has accurately detected a zero day attack a few months prior to the actual attack. For the baseline traffic of the ground truth dataset (October 2016), the model was already able to detect almost $60 \%$ of the traffic that was prepared for the zero day attack with $75 \%$ accuracy. Then the test traffic (January 2017), which was obtained five months prior to the attack, was run across the algorithm. The model has detected that $86 \%$ of the traffic was directed toward the attack and this time with $100 \%$ accuracy.
![img-5.jpeg](img-5.jpeg)

Figure 6: Predictive analytics model detection and accuracy rate

# 4.4 Results Against Other Classification Methods 

Many researchers, for instance Leskovec in [25], considered Support Vector Machine (SVM) as a state-of-the-art classification method for behavioral malware analysis. Thus, the dataset is further trained, classified then later compared to the SVM model as defined in Eq. (29);
$f(x)= \begin{cases}1, \text { if margin, }=|X A . w+Y A . w|+b=w . A+b>0 \\ 0, \text { otherwise }\end{cases}$
where $X A$ and $Y A$ is the coordinate of point A and $w$ is the weight vector. This is the margin between point A and the hyperplane. Each feature has a weight defined in Eq. (30);
$w=A . B=\|A\| \cdot\|B\| \cos \theta$
where $w$ is a distance inner product of some point A or the support vector with some point B along the hyperplane $90^{\circ}$ to point A . In order to separate attack (1) from benign (0) episode is the work to

decide the best separating line (hyperplane). Hence, there is a need to find the hyperplane with the largest margin; the line that separates ones and zeroes the most. The data are trained through total Least Squares residuals equation to obtain optimal hyperplane with optimal slope $(m)$ and intercept (b). The general Least Squares $(L)$ equation is defined in Eq. (31).
$L=\left(\left(m . X_{i}\right)+b-Y_{i}\right)^{2}$
However, since support vector is used, the model is refined by measuring the Euclidean distance $(D)$ of the support vector near the optimal hyperplane obtained from the Least Squares $(L)$ model. Fig. 7 below is the depiction of the dataset separated by the optimal hyperplane.
![img-6.jpeg](img-6.jpeg)

Figure 7: A depiction of optimal hyperplane separating baseline traffic and attack traffic
Linear equation for the classification model mentioned in Eq. (28) will penalize the attacked nodes that fall into a normal region. This will determine the accuracy of the detection using this model. The measured accuracy is $5.83333 \mathrm{e}-1$, which is almost $60 \%$ accuracy.
$k \mathrm{NN}(k$ Nearest Neighbor) is another classification and prediction model based on feature similarity of the nearest neighbors. This model is considered as the favorite model amongst researchers for its simplicity. Euclidean distance works in $k \mathrm{NN}$ algorithm. It determines the distance between the unknown data from all the points in the trained dataset. The closest distance from the nearest class neighbor will determine the class of the unknown dataset or test dataset. The binary classification and prediction model is derived from the general term of Euclidean Distance and extended into Eq. (32);

$$
\begin{gathered}
1-(1(\text { normal }), 0(\text { attack })) \\
\text { if distance, } D= \\
\sqrt{\sum_{i=1}^{n} \sum_{i=1}^{n}\left\|x_{\text {iuew point }}-x_{\text {attack }}\right\|^{2}+\left\|y_{\text {iuev point }}-y_{\text {attack }}\right\|^{2}}< \\
\sqrt{\sum_{i=1}^{n} \sum_{i=1}^{n}\left\|x_{\text {iuev point }}-x_{\text {normal }}\right\|^{2}+\left\|y_{\text {iuev point }}-y_{\text {normal }}\right\|^{2}} \\
0, \text { otherwise }
\end{gathered}
$$

where $x_{\text {iuev }}$ point is the new point of the test dataset projected in the dataset plane. It will be evaluated against attack point first, $x_{\text {attack }}$ and then normal point, $x_{\text {normal }}$. Then the class will be modeled as $y \in Y$, $y$ : Attack (1), Benign (0). Fig. 8 depicts the new point (test dataset) on the trained dataset. Some of the points are overlaid onto its neighbor on each class, which could significantly improve the classification of the new data point based on the $k \mathrm{NN}$ model suggested in Eq. (32). The coefficient values of 1 and 0

are inserted to penalize the wrong decision made by the model. It will assist in measuring the accuracy and false alarm rate.
![img-7.jpeg](img-7.jpeg)

Figure 8: A depiction of test dataset separating baseline traffic and attack traffic using $k \mathrm{NN}$
Tab. 7 summarizes the comparison results of the proposed model to other classification models discussed in this research. Again, detection rate and accuracy rate of the proposed Behavioral-based Malware Analysis model based on the Bayesian Network method scored $100 \%$ and $86 \%$, significantly outperforming other models. False Alarm Rate also scored less, at $14 \%$ as compared to other classification models. This is achieved through the feature selection model and refined distribution model and finally the application of Bayesian Network for the classification model.

Table 7: Comparison results against other classification model


Acknowledgement: The authors wish to thank the Research Management Centre (RMC) of Universiti Teknologi MARA (UiTM), Universiti Kebangsaan Malaysia (UKM) and Centre for Languages and Foundation Studies (CELFOS), Universiti Sultan Azlan Shah (USAS).

Funding Statement: The work is fully sponsored by the research project grant FRGS/1/2021/ICT07/ UITM/02/3.

Conflicts of Interest: The authors declare that there are no conflicts of interest to report regarding the present study.
