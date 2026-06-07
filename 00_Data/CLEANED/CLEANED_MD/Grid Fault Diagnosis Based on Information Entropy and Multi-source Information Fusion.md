# Grid Fault Diagnosis Based on Information Entropy and Multi-source Information Fusion 

Xin Zeng, Xingzhong Xiong and Zhongqiang Luo


#### Abstract

In order to solve the problem of misjudgment caused by the traditional power grid fault diagnosis methods, a new fusion diagnosis method is proposed based on the theory of multisource information fusion. In this method, the fault degree of the power element is deduced by using the Bayesian network. Then, the time-domain singular spectrum entropy, frequencydomain power spectrum entropy and wavelet packet energy spectrum entropy of the electrical signals of each circuit after the failure are extracted, and these three characteristic quantities are taken as the fault support degree of the power components. Finally, the four fault degrees are normalized and classified as four evidence bodies in the D-S evidence theory for multifeature fusion, which reduces the uncertainty brought by a single feature body. Simulation results show that the proposed method can obtain more reliable diagnosis results compared with the traditional methods.


Keywords-Information entropy, Bayesian network, Multisource information fusion, D-S evidence theory, Fault diagnosis

## I. INTRODUCTION

WITH the continuous expansion of the scale of the power system, the complexity of the interconnection of the power grid has gradually increased, and the power security has encountered an unprecedented threat. At the same time, the economics and convenience of power also have the risk of being restricted. Power failure may cause huge property loss, even personal injury, so more and more attention has been paid to the diagnosis of power failure [1]. The corresponding research methods mainly include artificial neural networks

This work was supported in part by the Natural Science Foundation of China under Grant 61801319, in part by the grant No. 2018JY0512 "Research on Fast Fatigue Testing Technology of Rotating Structure" financed from Major Frontier Project of Sichuan Science and Technology Plan, in part by Sichuan Outstanding Youth Fund Project under Grant 2020JDJQ0061, in part by the Education Agency Project of Sichuan Province under Grant 18ZB0419, in part by Sichuan Provincial Department of Science and Technology Cooperation Project under Grant 2020YFSY0027, 2021YFG0099 and 2020RC33, in part by Graduate Innovation Fund of Sichuan University of Science and Engineering under Grant y2020018, in part by Undergraduate Student Innovation Fund of Sichuan University of Science and Engineering under Grant cx2020161.

Xin Zeng is with School of Automation and Information Engineering and Artificial Intelligence Key Laboratory of Sichuan Province, Sichuan University of Science and Engineering, Yibin, China (e-mail: zincedu@qq.com).

Xingzhong Xiong is with School of Automation and Information Engineering and Artificial Intelligence Key Laboratory of Sichuan Province, Sichuan University of Science and Engineering, Yibin, China (e-mail: xzxiong@suse.edu.cn).

Zhongqiang Luo is with School of Automation and Information Engineering and Artificial Intelligence Key Laboratory of Sichuan Province, Sichuan University of Science and Engineering, Yibin, China (e-mail: zhongqiangluo@gmail.com).
[2], expert system [3], fuzzy Petri nets [4], Bayesian network [5] and fuzzy set theory [6], etc. However, these methods are usually based on a single information as a basis to diagnose the fault of electric power systems, so the information characterization of the single diagnosis results have greater uncertainty.

Power grid fault diagnosis is faced with the problem of fault tolerance, the Bayesian network can solve this problem. Miao [7] put forward a new method based on dynamic Bayesian network, it checking the circuit fault diagnosis method of the robot, but due to the uncertain fault probability of circuit elements, this may make the Bayesian network can't get an accurate diagnosis in the complex in the grid. Information entropy can effectively describe the degree of uncertainty of the system [8]. Literature [9] proposed an improved Whale Optimization Algorithm based on information entropy to improve the global convergence rate of the algorithm. The information entropy can be used to extract the characteristics of the electrical information expression caused by the inborn uncertainty of the grid components, and then obtain the fault location. Compared with the Bayesian network, the information entropy is more accurate, but there is also the possibility of missing detection.

Literature [10] described the singular spectrum entropy of time domain, power spectrum entropy of frequency domain and wavelet packet energy spectrum entropy can be extracted by information entropy related theory from fault signal.In order to solve the problems that brought by the methods above, the artical combined the information entropy and Bayesian network. Firstly, according to the given initial condition probability table, the Bayesian fault degree can be obtained by Bayesian network reasoning. Next, extract the three kinds of entropy, those are the singular spectrum entropy, power spectrum entropy and wavelet packet energy spectrum entropy. Then, let the three kinds of entropy and Bayesian fault degree as four evidences, and the all evidences should be normalized, because it is a requirment of the D-S evidence theory that the sum of all evidences is 1 . Lastly, fuse four evidences by D-S evidence theory. The proposed method ensures the fault diagnosis of breadth, and also ensure the accuracy of fault diagnosis with information entropy. In addition, the effectiveness of the method is verified by the simulation test.

## II. BAYESIAN NETWORK

Bayesian theorem is a theorem about conditional (or marginal) probabilities of random events A and B [11].

$P(A \mid B)$ is the probability of the occurrence of A in the case of B, and its formula is expressed as Equation (1).

$$
P\left(B_{i} \mid A\right)=\frac{P\left(B_{i}\right) P\left(A \mid B_{i}\right)}{\sum_{j=1}^{n} P\left(B_{j} P\left(A \mid B_{j}\right)\right.}
$$

Bayesian network, also known as reliability network, is a mathematical model based on probabilistic reasoning formed by the combination of Bayesian method and graph theory in probability theory. Bayesian network is composed of a directed acyclic graph and a set of conditional probability distributions. The combination of probability distributions can quantitatively express the degree of correlation among variables, and the model diagram can intuitively express the dependent or independent relationship between variables.It is intuitive and easy to understand, quantified and comparable, powerful, flexible and universal [11].

As shown in Fig. 1(a), six nodes represent six events, and the wires between nodes represent the two connected events that are related. The arrows refer to the former "cause" and the latter "effect". According to the conditional probability table given by each node, the inference results of each event can be obtained quantitatively, which constitutes a complete Bayesian network. When the conditional probability table is given, it can be concluded that the inference result of node F is 'False', which means that event F is not valid, and the probability of the occurrence is $66 \%$, as shown in Fig. 1(b).
![img-0.jpeg](img-0.jpeg)

Fig. 1. Bayesian network: (a) represents the original image; (b) Represents the inference results of a given conditional probability table

## III. INFORMATION ENTROPY

Entropy is an important concept in information theory and permeates other fields, which is a measure that represents the uncertainty of the system in a certain state. For discrete signals, information entropy can measure the unknown degree of the system and represent the uncertainty of the system. The higher the entropy is, the greater the uncertainty is. The entropy of information is expressed as Equation (2).

$$
H(X)=-\sum_{j=1}^{S} p_{j} \lg p_{j}
$$

where $\mathrm{p}_{j}$ is the probability that takes $\mathrm{x}_{j}$ as the value of $X$, which is the random variable of state characteristic, namely $p_{j}=P\left(x=x_{j}\right) ; S$ is the number of events that $X$ contain; The entropy value is calculated using a common logarithm with a base of 10 .

Information entropy can make a quantitative evaluation of the uncertainty of the system. According to the information
entropy theory, the faulty system can be regarded as a source of information, extracting the effective characteristics of the abnormal output signal, and then measuring the singularity and complexity of the system through the information entropy degree. Therefore, in power grid fault diagnosis, the use of information entropy theory can effectively achieve the quantitative analysis of system uncertainty.

## A. Singular spectrum entropy

Singular spectrum entropy is a division of the analytical signal in the time domain. Due to a large amount of discrete data, a matrix $A$ representing the state of the signal is generated by reducing the dimension of the data group with the step length as $n$ and dividing it into $I$ segment data. Then, the singular value spectrum of the state matrix $A$, that is $\left\{\lambda_{i}\right\}$ can be obtained according to the singular value decomposition principle of the signal and $\lambda_{1} \geq \lambda_{2} \geq \ldots \geq \lambda_{i}$. According to the literature [10], we can calculate $p_{j}=\lambda_{j} / \sum_{j=1}^{I} \lambda_{j}$, and then the singular spectrum entropy of each signal can be obtained as $H_{q}=-\sum_{j=1}^{I} p_{j} \lg p_{j}$.

## B. Power spectrum entropy

In addition to time domain analysis, signals can also be analyzed from the frequency domain. Spectrum analysis is an important means of signal research. The power spectrum entropy is a kind of frequency domain division after the signal is transferred from the time domain to the frequency domain, which can accomplish the characteristic description of signal energy distribution in the frequency domain. Firstly, the discrete Fourier transform of the discrete time-domain signal was performed, and the form changes into $F(\omega)$. Then, the power spectrum $S=\left\{s_{1}, s_{2}, \ldots, s_{n}\right\}$ was calculated according to the signal power spectrum estimation formula $S(\omega)=$ $\frac{1}{2 \pi n}|F(\omega)|^{2}$, and the power spectrum entropy was finally obtained as $H_{s}=-\sum_{j=1}^{n} p_{j} \lg p_{j}$, where $p_{j}=s_{j} / \sum_{j=1}^{I} s_{j}$, $n$ represents the number of discrete signals.

## C. Wavalet package energy spectrum entropy

Wavelet analysis has a good time-frequency localization capability, which can characterize part of the characteristics of electrical volume and time-frequency energy distribution. Wavelet packet decomposition is one of the feature extraction methods in the field of fault diagnosis. It can divide electrical signals in the full frequency band to obtain different levels of features, and has strong signal analysis capabilities. Combine wavelet packet decomposition and information entropy can fully complement the deficiencies of the two. In the wavelet analysis, the wavelet packet energy spectrum entropy is constructed to quantitatively analyze the time-frequency domain uncertainty of the signal, so as to better reflect the signal energy complexity.

Firstly, $d \mathcal{S} \Delta$ wavelet function is used to decompose the output signals of each circuit into three layers and then reconstructed by wavelet to obtain eight wavelet packet reconstructed signals. The sequences of wavelet packet energy spectrum $E=\left\{E_{1}, E_{2}, \ldots, E_{8}\right\}$ can be calculated by the program,

according to the db3 wavelet function, the energy spectrum sequence number n is 8 , finally according to the information entropy theory to calculate the wavelet packet energy spectrum entropy $H_{n}=-\sum_{j=1}^{8} p_{j} \lg p_{j}$, where $p_{j}=E_{j} / \sum_{j=1}^{8} E_{j}$.

## IV. FAULT INFORMATION FUSION DIAGNOSIS

## A. D-S eveidence theory

D-S evidence theory, also known as belief function theory, it is an extension of the classic probability theory, and transforms the uncertain problem of proposition into the uncertain problem of set by establishing the one-to-one correspondence between proposition and set [12]. In evidence theory, a sample space is referred to as an identification framework, represented by $\Theta=\left\{\theta_{1}, \theta_{2}, \ldots, \theta_{n}\right\}$. A statement can be expressed as a subset $A$ of $\Theta$, that is $A \subseteq \Theta$, or $A \subseteq 2^{\Theta}$. For each subset of $\Theta$, a probability can be assigned, called the basic probability assignment, represented by $m$, and it is not difficult to get

$$
\left\{\begin{array}{c}
m(\varphi)=0 \\
\sum_{A \subseteq \Theta} m(A)=1
\end{array}\right.
$$

This means that the identification framework must be completely closed and the sum of all probabilities is 1 . The uncertainty description of proposition $A$ by D-S evidence theory can be shown in Fig. 2, where $\operatorname{Bel}(A)$ represents the belief function of $A$ and $\operatorname{Pl}(A)$ represents the plausibility function of $A$.
![img-1.jpeg](img-1.jpeg)

Fig. 2. The uncertainty representation of proposition $A$
D-S evidence combination rule: D-S evidence combination rule is an operation process of combining all evidence, and its theoretical core calculation formula can be expressed as follows:

$$
\begin{gathered}
k=\sum_{A_{i} \cap B_{j}=\emptyset} m_{1}\left(A_{i}\right) m_{2}\left(B_{j}\right)<1 \\
m(C)=\left\{\begin{array}{ll}
0 & i f A_{i} \cap B_{j}=\emptyset \\
\frac{\sum_{A_{i} \cap B_{j}=C} m_{1}\left(A_{i}\right) m_{2}\left(B_{j}\right)}{1-k} & i f A_{i} \cap B_{j} \neq \emptyset
\end{array}\right.
\end{gathered}
$$

Where $m_{1}$ and $m_{2}$ are respectively basic probability assignment functions on $\Theta, A$ and $B$ represent two mutually independent evidence. $K$ is the inconsistency factor, also known as the conflict factor. The above calculation formula is the D S combination operation $m_{1} \oplus m_{2}$. If there are three or more evidence bodies, the result $m_{1} \oplus m_{2}$ can be combined with the third assignment function, and so on. The expression form is orthogonal sum of multiple basic probability assignment functions, namely $m_{1} \oplus m_{2} \oplus \ldots \oplus m_{n}$.

## B. Fault diagnosis decision

To sum up, the grid fault diagnosis framework in this paper is shown in Fig. 3.

The decision steps are as follows:

1) Calculate Bayesian fault degree: According to the distribution diagram of power components in the fault power system, establish the corresponding Bayesian network model, set the corresponding conditional probability table and update the state of power components in the Bayesian network model according to the actual trip situation of the fault circuit, and then back deduce the Bayesian fault degree of each line component.
2) Calculate each entropy: Combining the theory of information entropy theory, the matrix decomposition theory, the energy distribution of spectrum and wavelet theory for feature extraction of fault output signals, and singular spectral entropy, power spectral entropy, and wavelet packet energy spectrum entropy are obtained in the time domain, frequency domain, and time-frequency domain, respectively.
3) Fuse all evidences: The four feature information should be normalized to meet the necessary conditions of the evidence theory. The multi-source information fusion technology based on D-S evidence theory is used to make fusion decisions on four fault information including Bayesian inference fault degree, singular spectral entropy, power spectral entropy and wavelet packet energy spectral entropy, then obtain the location of the fault components, and finally obtain the fault diagnosis results.

## V. Simulation TESTING

## A. Grid analysis

According to the fusion diagnosis method proposed in this paper, the local power grid system as shown in Fig. 4 is used for the simulation test.

The known fault point occurred in the L1 line, and the fault type was a two-phase ground short circuit, which caused the circuit breaker to break. Due to the complexity of the circuit interconnection, the degree of uncertainty has soared. The purpose of the simulation test is to find the fault occurrence line according to the method proposed in this article. The output signal of the L1 line is shown in Fig. 4.

The fault of the L1 line causes the main protection of the sending end and the receiving end of L1 to operate, and the circuit breaker CB1 to trip. No tripping occurs on the B2 side of L1, which makes the zero sequence segment on the B7 side of L2, namely CB7 tripping. No tripping action occurred in L6; Both sides of the L4 were tripped by wrong actions, and both CB3 and CB4 were protected by tripping. The B6 side of L5 also made an error action, causing CB12 tripping.

## B. Simulating calculation

1) Bayesian inference fault degree: According to the above local power grid system diagram, use the GeNle software to establish the Bayesian network model of each line component in the power grid. Literature [13] listed the prior probability of failure of each power component through consulting a large

![img-2.jpeg](img-2.jpeg)

Fig. 3. Fault diagnosis framework
![img-3.jpeg](img-3.jpeg)

Fig. 4. Local grid system
amount of data. Based on these probabilities, established the initial condition probability table, and deduced the fault degree of each line in Table I according to the fault process.

TABLE I
FAULT DEGREE OF BAYESIAN INFERENCE.


If the fault diagnosis is carried out separately from the data in Table 1, it will be judged that L4 is the fault line, which is inconsistent with the actual situation
2) Information entropy measurement: Matlab was used to extract and analyze the output signal of the fault circuit, and three original information entropy values were calculated according to the method in section III, as shown in Table II.

TABLE II
INFORMATION ENTROPY VALUES OF DIFFERENT LINES.


3) $D-S$ evidence fusion: According to the D-S evidence theory in section III, consider the four failure support degrees in the table above as the evidence bodies and combine them, and the combination rules refer to the description in section III. Due to the synthesis of D-S evidence needs to meet $\sum_{A \subset \Theta} m(A)=1$, the data in Table I and Table II must be normalized. At the same time, since each piece of evidence is uncertain, so the normalization of data needs to be processed with the uncertainty $u$.

Assuming that the fault identification framework contains $t$ pieces of evidence and the number of recognition states is $n$, then $m_{j}\left(\Theta_{i}\right)=\left(1-u_{j}\right) x_{i j} / x_{j}$, where $i=1,2, \ldots, n, j=$ $1,2, \ldots, t, x_{i j}$ represents the fault support degree of the type $j$ body of evidence corresponding to the $i t h$ state, $x_{j}$ represents the sum of fault support degree of each state of class $j$ evidence body, and $u_{j}$ represents the uncertainty of the evidence in section $j$. In the grid fault diagnosis framework in this paper, there are 4 pieces of evidence and 6 lines (states), and assume the uncertainty $u$ of all 4 pieces of evidence is 0.1 .

![img-4.jpeg](img-4.jpeg)

Fig. 5. Output signal of fault line: Three-Phase V Measurement:1 represents the voltage of $A$ phase; Three-Phase V Measurement:2 represents the voltage of $B$ phase; Three-Phase V Measurement:3 represents the voltage of $C$ phase

To sum up, calculate the fusion results from Eq.(3) and Eq.(4), as shown in Table III.

TABLE III
NORMALIZATION AND FUSION RESULTS.


The fusion result value of L1 in the above table is the largest, indicating that the most likely fault location is L1 line, which is consistent with the actual situation, indicating that the application of multi-source information fusion technology in power grid fault diagnosis is very reasonable. Due to the complexity of circuit interconnection, the fault of line L1 will lead to abnormal signals in other lines, accompanied by the misoperation and rejection of each circuit breaker, which has disadvantages for the single-variable diagnosis method. If only based on the results of Bayesian network inference, we will misjudge that L4 is the fault point. In fact, this is because the circuit breakers on both sides of L4 occur misoperation, which shows that multi-feature information fusion strengthens the reliability of fault diagnosis. In addition, the original uncertainty $u$ also decreases after the fusion process, which indicates that D-S evidence fusion reduces the uncertainty of the system and enhances the power grid fault diagnosis capability.

According to the data in Table III, the figure can be descripted as below, which comparing diagnose efficiency of the Bayesian network reasoning and the proposed method.
![img-5.jpeg](img-5.jpeg)

Fig. 6. The compare of results of Bayesian network reasoning and Fusion method

As Fig. 6 shown, the Max value of Fusion method appears at L1, and the Max value of Bayesian reasoning appear at L4. This result indicating that Bayesian reasoning will misjudge the diagnosis results, that is the actual fault line is L1 not L4. In addition, the fault degree of other lines calculated by Fusion method are less than Bayesian reasoning longly. The proposed fusion method not only increased the fault degree of the fault line, but also reduced the fault degree of the normal lines, which is easier to understand and inspect. By Bayesian network, the diagnosis result is obtained that the L4 is the fault line. But by the proposed method, the fault degree of L4 just 0.198 that less than 0.231 that from Bayesian network reasoning.

## VI. CONCLUSION

Power system components are numerous, the circuit is complex, and each power component has its own prior failure rate, switch and circuit breaker may also occur misoperation and rejection. If there is a fault, it is not realistic to locate the fault position through manual inspection. So to find a practical and effective method is the expectation of many workers. Bayesian network reasoning has the advantages of intuitive understanding and clear reasoning, it can be used to quantify grid elements' own failure probability according to the connected components' states. Information entropy represents the uncertainty of the system. Through the analysis of output signal in 3 different transformation spaces which include time domain, frequency domain and time-frequency domain, the intrinsic characteristics of the signal can be described. The prior data required by D-S evidence theory is easier to obtain than those required by probabilistic reasoning. Its synthesis formula can integrate the effective characteristics of different data sources for the overall description, thereby increase the accuracy. Based on this, the article combined Bayesian network reasoning, information entropy and D-S evidence theory together for the local power grid fault diagnosis. Finally, through theoretical inference and simulation test show that the proposed method is effective. When a single statistical method is unable to diagnose or misjudge, the multi-feature fusion diagnosis method can show superior diagnostic performance and reduce the uncertainty of the diagnosis.

The article utilized the information entropy and Bayesian network reasoning to construct evidence bodies for D-S evidence fusion, and this method outperform single data method in grid fault diagnosis. But, there is an unsolved problem in fusion, that is if some highly conflict elements in Bayesian network reasoning, the correctness of result will be influenced. Thus, The next work of this article is to preprocess these highly conflicting data in order to facilitate better fusion.

## ACKNOWLEDGMENT

The authors would like to thank the reviewers for taking the time to read the manuscript.
