# Article 

## Intelligent Condition Diagnosis Method Based on Adaptive Statistic Test Filter and Diagnostic Bayesian Network

Ke Li ${ }^{1}$, Qiuju Zhang ${ }^{1, *}$, Kun Wang ${ }^{1}$, Peng Chen ${ }^{2}$ and Huaqing Wang ${ }^{3}$<br>Received: 6 November 2015; Accepted: 30 December 2015; Published: 8 January 2016<br>Academic Editor: Vittorio M.N. Passaro<br>1 Jiangsu Key Laboratory of Advanced Food Manufacturing Equipment and Technology, Jiangnan University, 1800 Li Hu Avenue, Wuxi 214122, China; like@jiangnan.edu.cn (K.L.); wangkun0808@163.com (K.W.)<br>2 Graduate School of Bioresources, Mie University / 1577 Kurimamachiya-cho, Tsu, Mie 514-8507, Japan; chen@bio.mie-u.ac.jp<br>3 School of Mechanical \& Electrical Engineering, Beijing University of Chemical Technology, Chao Yang District, Beijing 100029, China; wanghq_buct@hotmail.com<br>* Correspondence: qjzhang@jiangnan.edu.cn; Tel.: +86-151-0618-6878; Fax: +86-510-8591-0526


#### Abstract

A new fault diagnosis method for rotating machinery based on adaptive statistic test filter (ASTF) and Diagnostic Bayesian Network (DBN) is presented in this paper. ASTF is proposed to obtain weak fault features under background noise, ASTF is based on statistic hypothesis testing in the frequency domain to evaluate similarity between reference signal (noise signal) and original signal, and remove the component of high similarity. The optimal level of significance $\alpha$ is obtained using particle swarm optimization (PSO). To evaluate the performance of the ASTF, evaluation factor $I_{p q}$ is also defined. In addition, a simulation experiment is designed to verify the effectiveness and robustness of ASTF. A sensitive evaluation method using principal component analysis (PCA) is proposed to evaluate the sensitiveness of symptom parameters (SPs) for condition diagnosis. By this way, the good SPs that have high sensitiveness for condition diagnosis can be selected. A three-layer DBN is developed to identify condition of rotation machinery based on the Bayesian Belief Network (BBN) theory. Condition diagnosis experiment for rolling element bearings demonstrates the effectiveness of the proposed method.


Keywords: feature extraction; adaptive statistic test filter; Diagnostic Bayesian Network; evaluation factor; condition diagnosis

## 1. Introduction

In the field of condition monitoring for rotating machinery, the vibration information, such as vibration accelerometer signal, vibration velocity signal, and vibration displacement signal, is often used for detecting faults and distinguishing fault types. Feature extraction of vibration signals is important for condition diagnosis [1,2]. However, feature extraction for condition diagnosis is difficult because the vibration signals measured for condition diagnosis contain strong noise component. Useful information is buried under stronger noise. In such case, the feature of machine condition could not be obtained and even the wrong conclusion will be induced. Thus, it is important that the feature of the signal can be sensitively extracted at the state change of a machine [3].

Many studies based on vibration signal processing technology have been carried out with the goal of machinery condition diagnosis [4-7]. Fourier analysis has been the dominating signal processing tool for condition diagnosis. In [8], Fourier analysis was used to identify the gear faults in planet cage. In [9], Fourier transform has been applied to detect rolling bearing faults. Unfortunately, there

are some limitations of the Fourier transform, such as the fact that the signal to be analyzed must be strictly periodic or stationary. However, in practice, machinery operate under unsteady condition, such as varied rotating speed and operating load. In such case, even though the machinery is in the normal state, the spectrum feature and the frequency components of vibration signal are always changing with time. Thus the Fourier transform has no application to analyze non-stationary signal and can not reveal the inherent information of non-stationary signals [10,11]. Time frequency analysis methods, such as Wavelet Transforms (WT), Short Time Fourier Transform (STFT), etc., are effective tools for analyzing the non-stationary signals. These technologies can simultaneously provide the joint distribution information of signals in time domain and frequency domain, and describe the energy density or intensity of the signal at different times and frequencies. In [12], STFT and Hilbert-Huang transform (HHT) analysis were integrated to detect faults of ball bearings for wind turbine. However, the result of the STFT method depends on the choice of the windows size. Moreover, computational cost the STFT is high. WT has got huge success in fault diagnostics of rotating machinery for its ability to focus on localized structures in time frequency domain. WT can decompose the signal into many basis functions and extract signal features through change of the scales and time shifts of the basis function. In [13], WT method was employed to extract fault features of external load changing and the asymmetry of three-phase in induction motor. In [14], the broken-bar fault of induction motor was detected based on discrete WT. However, the feature extraction results of WT rest with the choice of wavelet basis function. Only selecting the appropriate basis function, the features of signal can work well to detect faults. In addition, due to the limited length of the wavelet base function, energy loss is inevitable [15]. Empirical mode decomposition (EMD) technique was proposed by Huang et al., for non-linear and non-stationary signal processing. EMD is a self adaptive signal processing technology that could decompose a non-linear and non-stationary signal into a set of intrinsic mode functions (IMFs). However, undesired frequency components in results and undesired low amplitude IMFs at the low-frequency region remain unsolved in EMD [16,17,18,19]. In addition, there are many noise cancelling methods that have also been applied, such as band pass filter [20], Kalman filter [21], Wiener filter [22], and so on. However, due to their flaws and shortcomings, these methods cannot always be applied to failure feature extraction. For example, band pass filter cannot cancel the wide band noise; when using Wiener filter and Kalman filter to process signal, the signal must follow the normal distribution.

The number of the artificial intelligence techniques, such as artificial neural networks (ANN), ant colony optimization (ACO), Bayesian belief network (BBN) etc., have been widely applied to fault diagnosis of plant machinery. In [23], three architecture NN, single-layer, multilayer perceptron network and counter propagation network, were introduced to detect 10 faults of a heat exchanger. In [2], an improved NN called partially-linearized neural network (PLNN) was presented to distinguishing the three types defect occurred in a rolling bearing. However, NN is not suitable for dealing with ambiguous diagnosis problems, and will never converge if SPs calculated by signals measured in different states have the same value. ACO algorithm imitates the behavior to solve optimization problems. In [24], ACO and DWT were integrated to detect faults of a rolling bearing used in the centrifugal fan system. However, ACO method is easy to trap into local optimum. In many cases, the optimization solution cannot be found. BBN is a powerful tool to represent and reason about complex systems with uncertain, incomplete and conflicting information [25,26]. A BBN enables us to model and reason about uncertainty, ideally suited for diagnosing real world problems where uncertain incomplete data exist. Therefore, it is a suitable solution for troubleshooting complex rotation machinery systems. In the last decades, BBN has been widely applied in condition diagnosis of plant machinery. References [27,28,29] are successful cases of BBN being used to detect fault of complex systems, such as nuclear power systems [27], aircraft engines [28], semiconductor manufacturing systems [29], etc.

To extract the fault feature of signals more effectively and discriminate conditions of rotation machinery more correctly, a novel method based on adaptive statistic test filter and Diagnostic Bayesian Network algorithm (DBN) for condition diagnosis of rotating machinery is presented. Structure of this

paper is as follows: Section 2 instructs feature extraction method based on ASTF and evaluation factor $I_{p q}$. The optimal level of significance $\alpha$ is obtained by using PSO. In Section 3, the ten SPs for condition diagnosis are defined and PCA is employed to obtain high sensitive SPs for condition diagnosis. In Section 4, a three-layer DBN is built to identify condition of rotation machinery based on BBN theory. Section 5 shows a practical example of fault diagnosis for verifying the effectiveness of the proposed method. Summary and conclusions are given in Section 6.

# 2. Feature Extraction by ASTF 

In this study, a new weak fault feature extraction method called adaptive statistic test filter (ASTF) is proposed. Principle of ASTF is based on statistic hypothesis testing in the frequency domain to evaluate similarity between reference signal (noise signal) and original signal, and remove the component of high similarity. Otherwise, the optimal level of significance $\alpha$ is obtained using PSO. The procedure for applying STF for the condition diagnosis is proposed, as shown in Figure 1.
![img-0.jpeg](img-0.jpeg)

Figure 1. Procedure for applying the ASTF for the condition diagnosis.

The reference signal $n(t)$ is measured in a normal state in advance. The original signal $g(t)$ is measured in the state to be detected and polluted by noise. $\mu_{n}(f)$ and $\mu_{g}(f)$ indicate the average value of $n(t)$ and $g(t)$ in the frequency domain, respectively; and $\sigma_{n}^{2}(f)$ and $\sigma_{g}^{2}(f)$ indicate the variance value of $n(t)$ and $g(t)$ in the frequency domain, respectively. The two null hypotheses are as follows:

$$
\begin{aligned}
H_{1}: \sigma^{2}{ }_{g}(f) & =\sigma^{2}{ }_{n}(f) \\
H_{0}: \mu_{g}(f) & =\mu_{n}(f)
\end{aligned}
$$

Firstly, $\sigma^{2}{ }_{g}(f)=\sigma^{2}{ }_{n}(f)$ is verified by $F$ test with $m-1$ degree of freedom, and $F \equiv S_{n}{ }^{2} / S_{g}{ }^{2}$.

$$
\begin{aligned}
& S_{g}^{2}(f)=\sum_{j=1}^{m} g(f)^{2} /(m-1)-\bar{g}(f)^{2} \\
& S_{n}^{2}(f)=\sum_{j=1}^{m} n(f)^{2} /(m-1)-\bar{n}(f)^{2}
\end{aligned}
$$

If $\sigma^{2}{ }_{g}(f)=\sigma^{2}{ }_{n}(f), \mu_{g}(f)=\mu_{n}(f)$ is verified by $t$ test with $2 m-2$ degree of freedom, and $t=\{\bar{g}(f)-\bar{n}(f)\} / S \sqrt{2 / m}$.
here,

$$
S^{2}=\left\{(m-1) S_{g}^{2}+(m-1) S_{n}^{2}\right\} /(2 m-2)
$$

If $\sigma^{2}{ }_{g}(f) \neq \sigma^{2}{ }_{n}(f), t=\{\bar{g}(f)-\bar{n}(f)\} / \sqrt{S_{g}{ }^{2}(f) / m+S_{n}{ }^{2}(f) / m}$.

$$
m^{*}=\left(S_{g}^{2} / m+S_{n}^{2} / m\right)^{2} /\left[\left\{S_{g}^{4} / m^{2}(m-1)\right\}+\left\{S_{n}^{4} / m^{2}(m-1)\right\}\right]
$$

If both null hypotheses would prove to be received, the spectrum component of the original signal $g(t)$ at the frequency $f$ is similar to that of the reference signal $n(t)$. The component at the frequency $f$ does not contain fault information and will be removed. If alternative hypothesis is denied, it means that the spectrum component of the original signal $g(t)$ at the frequency $f$ is not similar to that of the reference signal $n(t)$. The component at the frequency $f$ contains fault information.

After STF, the original signal $g(t)$ is decomposed into estimated fault signal $g^{\prime}(t)$ and estimated noise signal $n^{\prime}(t)$. In order to appraise the performance of STF, evaluation factor $I_{p q}$ is defined. $q_{i}$ and $q_{i}{ }^{\prime}$ are the number that $n(t)$ and $n^{\prime}(t)$ cross over some level $i$ of the vertical coordinate of the power spectrum $F_{n}{ }^{2}\left(f_{k}\right)$ with a positive slope in unit time and can be calculated as follows:

$$
\begin{gathered}
q_{i}=\frac{\sigma_{v}}{2 \pi \sigma_{x}} e^{-n_{i}{ }^{2} / 2 \sigma_{x}{ }^{2}} \\
p_{i}=\frac{\sqrt{2 \pi}}{\sigma_{v}} q_{i} \\
\sigma_{x}^{2}=\int_{0}^{\infty} F_{n}^{2}\left(f_{k}\right) d f_{k} \\
\sigma_{v}^{2}=\int_{0}^{\infty}\left(2 \pi f_{k}\right)^{2} F_{n}^{2}\left(f_{k}\right) d f_{k}
\end{gathered}
$$

where $i=1 \sim K, n_{i}=\min \{n(t)\} \sim \max \{n(t)\}$.
$I_{p q}$ is defined as follows:

$$
I_{p q}=\sum_{i=1}^{K}\left|\log \left(\frac{q_{i}}{q_{i}^{*}}\right)\right| / K+\sum_{i=1}^{K}\left|\log \left(\frac{p_{i}}{p_{i}^{*}}\right)\right| / K
$$

It is obvious that the smaller the value of the $I_{p q}$, the more similar $n(t)$ and $n^{\prime}(t)$ will be, and therefore, the better the STF will be. Thus, $I_{p q}$ is able to express the similarity degree between $n(t)$ and $n^{\prime}(t)$; that is to say, $I_{p q}$ can be used to evaluate the performance of STF.

To obtain optimal level of significance $\alpha$, an adaptive PSO algorithm is proposed in this paper. PSO algorithm is based on groups, and solves an unconstrained D-dimensional optimization problem by minimization of the objective or the fitness function [30-32]. In this study, the fitness function is the evaluation factor $I_{p q}$ (Equation (11)). In PSO algorithm, each particle keeps track of its own position denoted by $P(i)$.location $=\left[X_{i 1}, X_{i 2} \cdots X_{i D}\right]$ and velocity denoted by $P(i)$.velocity $=\left[V_{i 1}, V_{i 2} \cdots V_{i R}\right]$ in

the problem space, according to its own and neighboring particle experience [22-24]. The best previous position of particle is marked by the lowest fitness value and indicated by $P(i)$. best $=\left[P_{i 1}, P_{i 2} \cdots P_{i R}\right]$. The best position among all particles experienced discovered by the swarm, so far, is defined as $g(i)$.best $=\left[g_{i 1}, g_{i 2} \cdots g_{i R}\right]$. Then, the new positions and velocities of the particles are updated by the following equations:

$$
\begin{gathered}
P(i) \cdot \operatorname{velocity}(t+1)=\omega P(i) \cdot \operatorname{velocity}(t)+\eta_{1} r_{1}[P(i) \cdot \operatorname{best}(t)-P(i) \cdot \operatorname{location}(t)] \\
+\eta_{2} r_{2}[g(i) \operatorname{best}(t)-P(i) \cdot \operatorname{location}(t)] \\
P(i) \cdot \operatorname{location}(t+1)=P(i) \cdot \operatorname{location}(t)+P(i) \cdot \operatorname{velocity}(t+1)
\end{gathered}
$$

where $r_{1}$ and $r_{2}$ indicate random numbers between $0-1 . \eta_{1}$ is the cognitive parameter (acceleration coefficient). $\eta_{2}$ is the social parameter (acceleration coefficient). The inertia weight $\omega$ controls the previous velocity of particle, and $\omega$ adaptively adjust as follows:

$$
\omega= \begin{cases}k_{1}+0.5 q & R>0.05 \\ k_{2}+0.5 q & R \leqslant 0.05\end{cases}
$$

where $q$ is a random number with a uniform probability between $0-1 ; k_{1}$ and $k_{2}$ are parameters, and $k_{1}>k_{2}$, the choice of $k_{1}$ and $k_{2}$ is determined experimentally, here $k_{1}=0.5$ and $k_{2}=0.2$. R indicates change rate, which defined as Equation (15); if $R$ is greater than 0.05 , PSO is in the exploration stage, a large $\omega$ is beneficial to the algorithm's convergence; if $R$ is less than 0.05 , PSO is in the development stage, a small $\omega$ is beneficial to searching optimum point.

$$
R=\frac{\left|I_{p q}(t+5)-I_{p q}(t)\right|}{\left|I_{p q}(t)\right|}
$$

where $I_{p q}(t)$ is minimization evaluation factor value of the $t$-th iteration. $I_{p q}(t+5)$ is minimization evaluation factor value of the $(t+5)$-th iteration.

In order to test and verify capability of ASTF, a simulation experiment is designed. Ten set signals that consist of the impulsive signal with the period of 0.015 s and random white Gaussian noise are produced using Matlab software to simulate a bearing fault. These noisy signals are processed by ASTF and a high pass filter with 5000 Hz cut off frequency, respectively. The performances of denoising are estimated based on SNR. Mathematical expression of the impulsive signal is shown in Equation (16).

$$
x(t)=x_{0} e^{-\xi \omega_{n} t} \sin \omega_{n} \sqrt{1-\xi^{2} t}
$$

where $\xi$ indicates coefficient of damping and $\xi=0.2 ; \omega_{n}$ expresses natural frequency and $\omega_{n}=3 \mathrm{kHz}$; and $x_{0}$ denotes displacement constant and $x_{0}=2$.

Figure 2 shows the SNR of denoised signals processed by ASTF and high pass filter. As shown in Figure 2, all of the SNR values of denoised signals after ASTF are much greater than high pass filter. Then, ASTF method is effective and has high robustness for signal denoising.

![img-1.jpeg](img-1.jpeg)

Figure 2. Signal-to-Noise Ratio (SNR) of denoised signals processed by each method.

# 3. Symptom Parameters for Fault Diagnosis and Sensitivity Evaluation 

### 3.1. Symptom Parameters for Fault Diagnosis

The number of SPs reflect plant machinery condition have been defined in the pattern recognition field [33]. In this study, ten SPs in the time domain are considered.

$$
\begin{gathered}
P_{1}=\frac{\sigma}{\bar{x}} \\
P_{2}=\frac{\sum_{i=1}^{N} x_{i}^{2}}{\sigma^{2}} \\
P_{3}=\frac{\left|\sum_{i=1}^{N}\left(x_{i}-\bar{x}\right)^{3}\right|}{N \sigma^{3}} \\
P_{4}=\frac{\sum_{i=1}^{N}\left(x_{i}-\bar{x}\right)^{4}}{N \sigma^{4}}
\end{gathered}
$$

where, $x_{i}$ is digital data of vibration signal. $\bar{x}$ is the mean value of $x_{i}, \bar{x}=\frac{\sum_{i=1}^{N} x_{i}}{N}$. $\sigma$ is standard deviation of $x_{i}, \sigma=\sqrt{\frac{\sum_{i=1}^{N}\left(x_{i}-\bar{x}\right)^{2}}{N-1}}$.

$$
\begin{gathered}
P_{5}=\frac{\overline{x_{p}}}{\bar{x}} \\
P_{6}=\frac{\overline{x_{p}}}{\sigma} \\
P_{7}=\frac{\left|\sum_{i=1}^{N_{p}}\left(x_{p i}-\overline{x_{p}}\right)^{3}\right|}{N_{p} \sigma_{p}{ }^{3}} \\
P_{8}=\frac{\left|\sum_{i=1}^{N_{p}}\left(x_{p i}-\overline{x_{p}}\right)^{4}\right|}{N_{p} \sigma_{p}{ }^{4}}
\end{gathered}
$$

where, $x_{p i}$ is the peak value of $x_{i} . \bar{x}_{p}$ and $\sigma_{p}$ are the mean value and standard deviation of $x_{p i}$, respectively.

$$
\begin{aligned}
& P_{9}=\frac{\left|\sum_{i=1}^{N_{0}}\left(x_{v i}-\overline{x_{v}}\right)^{3}\right|}{N_{0} \sigma_{v}^{3}} \\
& P_{10}=\frac{\left|\sum_{i=1}^{N_{0}}\left(x_{v i}-\overline{x_{v}}\right)^{4}\right|}{N_{0} \sigma_{v}^{4}}
\end{aligned}
$$

where, $x_{v i}$ is the valley value of $x_{i} . \bar{x}_{v}$ and $\sigma_{v}$ are the mean value and standard deviation of $x_{v i}$, respectively.

# 3.2. High Sensitivity Symptom Parameters Obtained by PCA 

PCA is a statistical analytical tool used to explore, sort and group data. PCA takes a large number of correlated variables and transform these data into a smaller number of uncorrelated variables known as principal components. The first few principal components contain most of the information and the discriminatory features [34].

Define a data matrix with size $m \times n$, where $m$ is the number of identifying states and $n$ is the number of SPs, whose covariance matrix has eigenvalue $\lambda_{i}$ and eigenvector $a_{i}$ ( $a$ is loading of the principal component and can express the importance of the SPs for each principal component) and $I=1-n$ with $\lambda_{1} \geqslant \lambda_{2} \geqslant \ldots \geqslant \lambda_{n}$. Principal components $Z_{i}$ and the cumulative contribution rate of the principal components $\eta_{i}$ can be calculated as follows:

$$
\begin{gathered}
\left\{\begin{array}{c}
Z_{1} \\
\vdots \\
Z_{n}
\end{array}\right\}=\left[\begin{array}{ccc}
a_{11} & \cdots & a_{1 n} \\
\vdots & \ddots & \vdots \\
a_{m 1} & \cdots & a_{m n}
\end{array}\right]=A P \\
\eta_{i}=\sum_{j=1}^{i} \lambda_{j} / \sum_{k=1}^{n} \lambda_{k}
\end{gathered}
$$

where $P_{i}$ indicates a symptom parameter, $I=1-n$.

## 4. Bayesian Belief Network

BBN is a probability network based on graphical network model for describing causal uncertainties between variables. It is built for uncertainty modeling and reasoning, and has a great advantage in diagnosing fault caused by uncertainty and correlation of the complex systems.

### 4.1. Bayesian Inference

Supposing $A$ is a random event and $B$ is the event that is root causes generating $A$, conditional probabilities $P(A \mid B)$ between $A$ and $B$ can be calculated as follows:

$$
P(A \mid B)=\frac{P(A B)}{P(B)}=\frac{P(A) P(B \mid A)}{P(B)}
$$

where $P(A B)$ is the joint probability, $P(A B)=P(B) \cdot P(A \mid B)=P(A) \cdot P(B \mid A)$.
Supposing $B_{i}(i=1,2, \ldots, n)$ are mutually exclusive and complete set of root causes generating $A$, the marginal probability of $A$ is

$$
P(A)=\sum_{i=1}^{n} P\left(B_{i}\right) P\left(A \mid B_{i}\right)
$$

The conditional and marginal probabilities of $A$ and $B_{i}$ is

$$
P\left(B_{i} \mid A\right)=\frac{P\left(A B_{i}\right)}{P(A)}=\frac{P\left(B_{i}\right) P\left(A \mid B_{i}\right)}{\sum_{i=1}^{n} P\left(B_{i}\right) P\left(A \mid B_{i}\right)}
$$

In Equation (31), $P\left(B_{i}\right)$ and $P\left(A / B_{i}\right)$ express prior probabilities and prior conditional probabilities, respectively. $P\left(B_{i} / A\right)$ indicates posterior probability. When using the Bayesian inference for fault diagnosis, $B_{i}$ represents an equipment condition and $A$ represents a SP. The prior probability of the $\operatorname{SP} B_{i}\left(P\left(B_{i}\right)\right)$ and the conditional probability of equipment condition $A$ given $B_{i} P\left(A / B_{i}\right)$ can be obtained from expert experience or statistical data. Then, the posterior probability $P\left(B_{i} / A\right)$ can be obtained by Equation (31). If this posterior probability is high, the condition $B_{i}$ can be confirmed at the given $A$, and the equipment condition is judged $B_{i}$.

# 4.2. Topology of Bayesian Belief Network 

A BBN consists of a number of nodes, directed links, and probability tables. For a diagnostic BBN model, nodes represent variables that can be SP, equipment condition or observations. Directed links indicate casual relationships between the variables. In this paper, the purpose of building a diagnostic BBN is to reason the most likely mechanical condition based on the values of SP, given one or more SP values to calculate posterior probabilities of the cause. The calculus of posterior probability involves calculating the joint probability for the model (probabilities of all combined states for all nodes within the model). The network contains five nodes, $X 1, X 2, X 3, X 4$, and $X 5$, with a structure of three layers (see in Figure 3). In terms of the definition of the three types of conditional independence, $X 1$ is independent of $X 2 ; X 1$ is parent of $X 3$ and $X 4$. Given $X 1, X 3$ and $X 4$ are conditionally independent of each other, $X 5$ is independent of $X 1, X 2$, and $X 3$. The following derivation indicates how to calculate the posterior conditional probability $P(X 4=$ true $\mid X 5=$ true $)$.

$$
P\left(X_{4}=\text { true } \mid X_{5}=\text { true }\right)=\frac{P\left(X_{4}=\text { true } \mid X_{5}=\text { true }\right)}{P\left(X_{5}=\text { true }\right)}=\frac{\sum_{x_{1} x_{2} x_{3}} P\left(X_{1}, X_{2}, X_{3}, X_{4}=\text { true }, X_{5}=\text { true }\right)}{\sum_{x_{1} x_{2} x_{3} x_{4}} P\left(X_{1}, X_{2}, X_{3}, X_{4}, X_{5}=\text { true }\right)}
$$

where $P(X 1, X 2, X 3, X 4=$ true $\mid X 5=$ true $)$ and $P(X 1, X 2, X 3, X 4, X 5=$ true $)$ involve calculating the joint probability of the model. The joint probability of this model $P(X 1, X 2, X 3, X 4, X 5)$ can be calculated as follows:

$$
\begin{aligned}
P\left(X_{1}, X_{2}, X_{3}, X_{4}, X_{5}\right) & =\prod_{i=1}^{5} P\left(X_{i} \mid X_{1}, \cdots, X_{i-1}\right) \\
& =P\left(X_{1}\right) P\left(X_{2} \mid X_{1}\right) P\left(X_{3} \mid X_{1} X_{2}\right) P\left(X_{4} \mid X_{1} X_{2} X_{3}\right) P\left(X_{5} \mid X_{1} X_{2} X_{3} X_{4}\right)
\end{aligned}
$$

Applying the independence assumption, the joint probability distribution can be simplified as follows:

$$
\begin{aligned}
P\left(X_{1}, X_{2}, X_{3}, X_{4}, X_{5}\right) & =\prod_{i=1}^{5} P\left(X_{i} \mid P_{a i}\right) \\
& =P\left(X_{1}\right) P\left(X_{2}\right) P\left(X_{3} \mid X_{1}\right) P\left(X_{4} \mid X_{1} X_{2}\right) P\left(X_{5} \mid X_{4}\right)
\end{aligned}
$$

![img-2.jpeg](img-2.jpeg)

Figure 3. General model of Bayesian Belief Network.

# 4.3. Framework of Diagnostic Bayesian Network 

In this study, Diagnostic Bayesian Network (DBN) is constructed for intelligent condition diagnosis. As shown in Figure 4, the proposed DBN consists of three layers. The first layer is normal and abnormal states. The second layer is fault states, and the last layer is SPs calculated from the signals processed by ASTF.

In the proposed DBN, prior probabilities of root nodes are needed and conditional probabilities are also needed to represent direct probabilistic dependences among nodes in the three layers. Here, all machine states are regarded as parent nodes, and the prior probabilities of state $i\left(S_{i}\right)$ can be obtained as follows:

$$
P\left(S_{i}\right)=\frac{N_{S_{i}}}{N}
$$

where $N_{S i}$ represents the sample size of state $i$, and $N$ indicates the total number of samples.
The conditional probabilities of each node are obtained as follows

$$
\begin{gathered}
P\left(S P=x_{i} \mid S_{i}\right)=\frac{N_{S_{i}}^{x_{i}}}{N_{S_{i}}} \quad N_{S_{i}}^{x_{i}} \neq 0 \\
P\left(S P=x_{i} \mid S_{i}\right)=\frac{1 / N}{N_{S_{i}}+N_{x_{i}} / N} \quad \text { if } \quad N_{S_{i}}^{x_{i}}=0
\end{gathered}
$$

where $S P$ represents the values of symptom parameters, and $N_{S_{i}}^{x_{i}}$ indicates the sample size of state $i$, when $S P=x_{i}$.
![img-3.jpeg](img-3.jpeg)

Figure 4. Structure of Diagnostic Bayesian Network.

# 5. Diagnosis and Application 

### 5.1. Condition Diagnosis by Proposed Method

In this section, an experimental setup is designed to evaluate the effectiveness of the method proposed in this paper. The flowchart of the condition diagnostic procedure is shown in Figure 5.

Figure 6 shows the experimental bench for condition diagnosis test, which includes a servo motor, rotor system and loading equipment. The NSK 205 ball bearing is used for bearing condition diagnosis. As shown in Figure 7, three types fault: the outer defect, the inner defect, and the roller element defect were artificially made by using electro discharge machining with fault width was 0.3 mm , and fault depth was 0.025 mm .

In the present work, the original vibration signals in each state were measured by the accelerometer (PCB MA352A60, PCB Piezotronics Inc., New York, NY, USA) with $50,000 \mathrm{~Hz}$ sampling frequency. The accelerometer was fixed on vertical direction of the bearing. While the vibration signals were being obtained, the speed of servo motor was 800 rpm , and a 150 kg load was also transported on the rotating shaft by the loading equipment (RCS2-RA13R, IAI Co. Ltd., Shizuoka, Japan). All the data were recorded and transformed by a collection system includes a sensor signal conditioner (PCB ICP Model 480C02, PCB Piezotronics Inc., New York, NY, USA) and a signal recorder (Scope Coder DL750, YOKOGAWA Co. Ltd. Tokyo, Japan). Obtained data was divided to two sets, one set includes 80 samples and was used to train diagnosis system; the other set includes 20 samples and was used for condition identification test. Figure 8 shows the original vibration signal in each state, and Figure 9 shows the vibration signal after ASTF.
![img-4.jpeg](img-4.jpeg)

Figure 5. Flowchart for the condition diagnostic procedure.
![img-5.jpeg](img-5.jpeg)

Figure 6. Experimental system for bearing fault diagnosis.

![img-6.jpeg](img-6.jpeg)

Figure 7. Bearing defects: (a) outer-race defect; (b) inner-race defect; and (c) roller defect.
![img-7.jpeg](img-7.jpeg)

Figure 8. Original vibration signal: (a) normal state; (b) outer-race defect; (c) inner-race defect; and (d) roller defect.
![img-8.jpeg](img-8.jpeg)

Figure 9. Vibration signal after ASTF: (a) normal state; (b) outer-race defect; (c) inner-race defect; and (d) roller defect.

In this study, the SPs that contain the most information and have high sensitivity for each state are selected by PCA. As an example, parts of the selection results are shown in Tables 1 and 2; $\mathrm{P}_{1}, \mathrm{P}_{2}$, $P_{6}, P_{8}$ and $P_{9}$ have high sensitivity for distinguishing normal state and abnormal state. Because the weight coefficients for $P_{1}, P_{2}, P_{6}, P_{8}$ and $P_{9}$, the first principal component, are larger than those of the other, the contribution rate of the first principal component is larger than 0.86 , which contains enough information and discriminatory features to identify the normal state and abnormal state. Similarly, the SPs for other states can also be selected.

In this paper, the DBN for distinguishing conditions of a rolling bearing was built as shown in Figure 10. The proposed DBN consists of three layers. The first layer is normal and abnormal states. The second layer is main failures such as outer-race defect, inner-race defect, and roller element defect, which often occurred in a rolling bearing. The last layer is SPs shown in Table 2. The prior probabilities

and the conditional probabilities were obtained by Equations (35) and (36). All of the SPs were divided into five levels, $1,2,3,4$ and 5 , which indicate very small, small, middle, big and very big levels, respectively. As an example, parts of the training sample data are shown in Table 3.
![img-9.jpeg](img-9.jpeg)

Figure 10. DBN for distinguishing conditions of a rolling bearing.
Table 1. First principal component of SPs.


Table 2. Selection result of the SPs for distinguishing each state.


Table 3. Training sample data.


To verify the diagnostic capability of the diagnosis methods proposed in this paper, we used the data measured in each state had not been used to train the DBN system. They can correctly and quickly diagnose those faults with the possibility grades of the corresponding states. In the test of normal state, the successful diagnosis ratio is $100 \%$. In the test of each faults, the successful diagnosis ratio of outer-race defect, inner-race defect and roller element defect states are $100 \%, 94 \%$ and $86 \%$, respectively. Some diagnosis results are shown in Tables 4-7.

Table 4. Diagnosis results of normal state.


Table 5. Diagnosis results of outer-race defect state.


Table 6. Diagnosis results of inner-race defect state.


Table 7. Diagnosis results of roller element defect state.


# 5.2. Condition Diagnosis by NN 

In this study, a back propagation NN shown in Figure 11 is also constructed for condition diagnosis of the roller bearing. The NN consists of three layers, the SPs calculated by vibration signals are entered into input layer, hidden layer includes 80 units, output layer is the possibility grades of each condition of roller bearing. Table 8 shows the parts of diagnosis results of NN. N, O, I and R indicate the normal, outer race defect, inner race defect and roller element defect states, respectively. The symbol $\times$ expresses the case that NN is incapable of identifying the fault type. As shown in Table 8, the normal and outer race defect states of roller bearing were correctly identified by NN. However, NN is incapable of identifying inner race defect and roller element defect states of roller bearing. The

main reasons are that the vibration signals measured for condition diagnosis contain strong noise, there exist ambiguous relationships between the SPs and the fault types, and NN cannot deal with incomplete and conflicting information.
![img-10.jpeg](img-10.jpeg)

Figure 11. The back propagation NN for condition diagnosis.

Table 8. Diagnosis results of NN.


# 6. Conclusions 

In order to detect the condition of rotating machinery at an early stage, a novel fault diagnosis method based on ASTF and DBN was presented. The main conclusions of this paper are summarized as follows:

1. The method of ASTF for extracting weak fault features under background noise was presented. The optimal level of significance $\alpha$ was obtained using PSO. To evaluate the performance of ASTF, evaluation factor $I_{p q}$ was also defined. In addition, a simulation experiment was designed to verify the effectiveness and robustness of ASTF.
2. PCA based on statistical analysis theory was also presented to evaluate the sensitivities of SPs calculated via vibration signals measured in each state for condition identification.
3. A three-layer DBN was developed to identify condition of rotation machinery based on the BBN theory. It is effective and efficient in condition diagnosis based on uncertain, incomplete and conflicting information.
4. Study examples of diagnosis for a bearing were shown to demonstrate the effectiveness of the methods proposed in this paper. The verification results show that the bearing faults that often occur in roller bearings, such as the Outer race, the Inner race and the roller element defects, have been effectively identified by the proposed method in this paper. However, these bearing faults are difficult to detect using NN technology, because the vibration signals measured for condition diagnosis contain strong noise, there exist ambiguous relationships between the SPs and the fault types, and NN cannot deal with incomplete and conflicting information.

In summary, this paper verifies the capability of condition diagnosis method based on ASTF and DBN. In addition, soft sensor technique establish inference model of symptom parameters based

on state-space model, and solves inference model of symptom parameters by parameter estimation method, such as Kalman filter and Bayesian filter. The condition diagnosis system includes two parts: feature extraction and condition identification. Soft sensor technique can be used of feature extraction and fusion, and condition identification can adopt artificial intelligence techniques, such as DBN, NN, etc. In the future, we will consider using soft sensor technique to extract features of signals.

Acknowledgments: The authors would like to acknowledge the financial support of the National Natural Science Foundation of China (51575236), Fundamental Research Funds for the Central Universities (Grant No. JUSRP51511). This work was also supported by the open project of Jiangsu key laboratory of advanced food manufacturing equipment \& technology (Grant No.FM-2015-01).
Author Contributions: Ke Li, Peng Chen and Huaqing Wang conceived and designed the experiments; Ke Li and Peng Chen performed the experiments; Ke Li, Qiuju Zhang and Kun Wang analyzed the data; Ke Li wrote the paper.
Conflicts of Interest: The authors declare no conflict of interest.
