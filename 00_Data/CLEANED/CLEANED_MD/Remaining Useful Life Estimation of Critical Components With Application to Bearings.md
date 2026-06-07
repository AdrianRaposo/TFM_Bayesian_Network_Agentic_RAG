# HIAL open science 

## Remaining useful life estimation of critical components with application to bearings.

Kamal Medjaher, Diego Tobon-Mejia, Noureddine Zerhouni

## To cite this version:

Kamal Medjaher, Diego Tobon-Mejia, Noureddine Zerhouni. Remaining useful life estimation of critical components with application to bearings.. IEEE Transactions on Reliability, 2012, 61 (2), pp.292-302. 10.1109/TR.2012.2194175 . hal-00737596

## HAL Id: hal-00737596 <br> https://hal.science/hal-00737596v1

Submitted on 2 Oct 2012

HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers.

L'archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d'enseignement et de recherche français ou étrangers, des laboratoires publics ou privés.

# Remaining useful life estimation of critical components with application to bearings 

K. Medjaher, D.A. Tobon-Mejia, N. Zerhouni


#### Abstract

Prognostics activity deals with the estimation of the Remaining Useful Life (RUL) of physical systems based on their current health state and their future operating conditions. RUL estimation can be done by using two main approaches, namely model-based and data-driven approaches. The first approach is based on the utilization of physics of failure models of the degradation, while the second approach is based on the transformation of the data provided by the sensors into models that represent the behavior of the degradation. This paper deals with a data-driven prognostics method, where the RUL of the physical system is assessed depending on its critical component. Once the critical component is identified, and the appropriate sensors installed, the data provided by these sensors are exploited to model the degradation's behavior. For this purpose, Mixture of Gaussians Hidden Markov Models (MoG-HMMs), represented by Dynamic Bayesian Networks (DBNs), are used as a modeling tool. MoG-HMMs allow us to represent the evolution of the component's health condition by hidden states by using temporal or frequency features extracted from the raw signals provided by the sensors. The prognostics process is then done in two phases: a learning phase to generate the behavior model, and an exploitation phase to estimate the current health state and calculate the RUL. Furthermore, the performance of the proposed method is verified by implementing prognostics performance metrics, such as accuracy, precision, and prediction horizon. Finally, the proposed method is applied to real data corresponding to the accelerated life of bearings, and experimental results are discussed.


## Index Terms

Condition monitoring, prognostics, remaining useful life, performance metrics, mixture of Gaussians hidden Markov models, condition-based maintenance, dynamic Bayesian networks.

## ACRONYMS



# NOTATION 

## I. INTRODUCTION

Maintaining equipment in operational condition is an industrial, economical, and societal requirement. This requirement can be satisfied by implementing appropriate maintenance strategies, which can be curative or preventive. In the first case, the maintenance interventions are done only after a fault has been observed. This action may lead to non desired situations, especially for critical industrial systems (one can cite the petrochemical explosion in 2010 in the Gulf of Mexico). To avoid such situations, a systematic maintenance can be used. However, this type of maintenance can be a source of unnecessary spending due to unnecessary interventions or replacement of components. Thus, for more efficiency, one can implement condition Based Maintenance (CBM) [1]. Indeed, contrary to a systematic maintenance, a CBM is done according to the real equipment's health condition, estimated or measured, potentially through the sensors present on the industrial equipment. In addition, by using appropriate mathematical or modeling tools, the estimated or measured equipment's state can be projected to predict its future health condition, and thus support appropriate decisions.
In the framework of CBM, failure prognostics is considered to be one of the main processes, which permits one to estimate the Remaining Useful Life (RUL) before the failure of a given industrial system [2]. Numerous methods and tools can be used to predict the RUL's value. These methods can be classified into two principal approaches: model-based prognostics (also called physics of failure prognostics), and data-driven prognostics. Model-based prognostics [3] deals with the prediction of the RUL of critical physical components by using mathematical or physical models of the degradation phenomenon (crack by fatigue, wear, corrosion, etc.). The data-driven prognostics [3] aims at transforming the data provided by the sensors into relevant models (which can be parametric or non-parametric) of the degradation's behavior.
This paper deals with a data-driven prognostics method for the estimation of the RUL of critical physical components. The proposed method belongs then to the category of data-driven approaches, and uses mainly Mixture of Gaussians Hidden Markov Models (MoG-HMMs), represented by Dynamic Bayesian Networks (DBNs), to model the degradation, and to estimate the value of the RUL before a potential failure. MoG-HMMs are chosen for their capability to transform the features extracted from the raw signals to relevant behavioral models representing the physical component's degradation.
The proposed failure prognostics method is done in two phases: a learning phase, and an exploitation phase. During the first phase, the raw signals coming from the sensors are processed to extract appropriate, useful features. These features are then used to learn the parameters of the MoG-HMMs. In the second phase, the learned models are exploited in order to assess the current condition of the component, and to predict its future one, leading to an estimation of the component's RUL. In addition to RUL, a confidence value can be calculated. Note that the RUL and the confidence are important information that may be used in the decision process. For example, they can be used to delay the maintenance interventions, or stop a machine before its future maintenance due to early fault.
To assess the performance of the predictions provided by the proposed method, performance prognostics metrics are implemented. Finally, the method is applied on real experimental data related to the accelerated life tests of bearings.
The paper is organized as follows. Section 2 presents the steps of the proposed method, Section 3 is dedicated to its application on real degradation data related to bearings, and Section 4 concludes the paper.

## II. DATA-DRIVEN PROGNOSTICS METHOD BASED ON MoG-HMMs

Compared to fault diagnostics, which consist of detecting and isolating the probable cause of the fault [2], failure prognostics aims at anticipating the time of the failure [4]. Thus, the diagnostic is realized after the occurrence of the fault, whereas the prognostics is done before the occurrence of the failure.
Several definitions related to prognostics have been reported in the literature [1], [5], [6]. The International Standard Organization [7] defines failure prognostics as "the estimation of the Time To Failure (ETTF) and the risk of existence or later appearance of one or more failure modes." Note that most of the definitions reported in the literature use the terminology Remaining Useful Life (RUL) instead of ETTF. An illustration of a RUL is given in Fig. 1.

![img-0.jpeg](img-0.jpeg)

Fig. 1: Illustration of a RUL.

In addition to the absolute value of the RUL, a confidence interval can be associated, which may be useful during the decision process.

Numerous methods and tools regarding failure prognostics have been proposed and reported in the literature [1]–[3], [8]. The reported tools and methods have been subject to several classifications. The first classification (in a pyramidal) form has been proposed in [1] where three main approaches are distinguished: model-based prognostics, data-driven prognostics, and experience-based prognostics. This classification was created according to four criteria: complexity, cost, precision, and applicability. The experience-based approach (also called reliability-based approach, which takes its origins from the reliability domain) uses data gathered from the experience feedback to estimate the parameters of reliability laws. So, it can be put within the data-driven approach. Consequently, the following updated approaches can be considered: model-based (physics of failure), data-driven, and hybrid approaches (Fig. 2). In the model-based (or physics of failure) approach, the physical component and its degradation phenomenon are represented by a set of mathematical laws, which are then used to estimate the RUL [9], [10]. The data-driven approach consists of transforming the monitoring data provided by the sensors installed on the system into reliable behavioral models of the degradations [3], [11]. The modeling tools used in this approach are mainly those used by the artificial intelligence community: temporal prediction series, trend analysis techniques, neuronal networks, neuro-fuzzy systems, hidden Markov models, and dynamic Bayesian networks.

Compared to model-based methods, the data-driven methods offer a trade-off in terms of complexity, cost, precision, and applicability. They are suitable for systems where it is easy to obtain monitoring data and transform them into behavior models of the degradation phenomena. In practice, this condition is the case in several applications, such as bearings, which are the subject in this paper. Indeed, prediction models, such as the $L_{10}$ for bearings or physics of failure laws (Paris-Erdogan) [9] for wear by fatigue, can be used to calculate the remaining useful life; but these laws are valid only for specific components in specific conditions that are difficult to verify in real applications.

In the rest of the paper, MoG-HMMs (represented by DBNs) are used to model the component's degradation, and to estimate its RUL. MoG-HMMs have proved to be a suitable tool in failure diagnostic and prognostics domains [11]. They allow one to model the physical component's degradation by using continuous observations provided by the monitoring sensors. They also permit one to estimate the stay durations in each health state, leading to the prediction of the RUL value. Furthermore, contrary to regression models or neural networks where the structure is not interpretable [12], the states in the MoG-HMM can be interpreted as the health conditions of the component.

A MoG-HMM is primarily an HMM. This latter is defined as a statistical model used to represent stochastic processes, where the states are not directly observed [13]. An HMM is completely defined by the parameters $N$, $V$, $A$, $B$, and $\pi$ (more details can be found in [13], and [14]).

For simplicity and clarity of presentation, a compact notation $(\lambda=\pi, A, B)$ is used for each HMM. In practice, HMMs are

used to solve the following problems (see [13] for more details).

- Problem 1 (detection): given a model $\lambda$, and an observation sequence $O=\left(O_{1}, O_{2}, \ldots, O_{T}\right)$, compute the probability $P(O \mid \lambda)$ of the sequence given the model. The solution of this problem is obtained by using the forward-backward algorithm [15].
- Problem 2 (decoding): given an observation sequence $O=\left(O_{1}, O_{2}, \ldots, O_{T}\right)$, find the hidden state sequence $S=$ $\left(X_{1}, X_{2}, \ldots, X_{T}\right)$ that has most likely produced the observation sequence. This problem is solved by using the Viterbi algorithm [16].
- Problem 3 (learning): find the model parameters $(\pi, A, B)$ that better fit the observation sequence $O$, i.e., that maximize the probability $P(O \mid \lambda)$. This problem is solved by using the Baum-Welch algorithm [17].
The problem with discrete HMMs is that they cannot be directly applied to model continuous observations. To overcome this difficulty, one can use MoG-HMMs, where the observation probability densities are represented by a mixture of Gaussians in the form

$$
b_{j}(O)=\sum_{m=1}^{M i x} C_{j m} \xi\left(O, \mu_{j m}, U_{j m}\right), 1 \leq j \leq N
$$

A MoG-HMM is completely defined by the $A$ matrix, the $B$ matrix, and the initial probability $\pi$. The observation matrix $B$ is modeled by a Gaussian density with a mean $\mu$, a covariance matrix $U$, and a mixture matrix $M$.
To speed up the learning and inference calculations, Dynamic Bayesian Networks (DBNs) and related algorithms are used in this paper to represent the MoG-HMMs (more details on how to model Hidden Markov Models and MoG-HMMs by using DBNs can be found in [18]). An example of a compact representation of a MoG-HMM by a DBN is shown in Fig. 3. In this figure, $X_{1}$ is the initial state, $X_{t}$ represents the hidden states at time $t, C_{t}$ are the mixture coefficients, and $O_{t}$ are the observation distributions.
![img-1.jpeg](img-1.jpeg)

Fig. 3: Representation of a MoG-HMM by a DBN: (a) unrolled model for three time slices, and (b) compact representation.

The data-driven method proposed to estimate the RUL of critical physical components is presented next. In this method, it is assumed that the RUL of the machine (or industrial plant) depends on the RUL of its most critical component. It is also considered that an adequate monitoring system, with necessary sensors that capture the evolution of the component's degradation, is available. Thus, the data provided by the sensors can be used to model the component's degradation behavior, and estimate its RUL. The main steps of the proposed prognostics method are given in Fig. 4, and a description of each step is given in the following. The estimation of the RUL is done in two principal phases, as shown in Fig. 5: a learning phase,
![img-2.jpeg](img-2.jpeg)

Fig. 4: Main steps of the proposed prognostics method.
and an exploitation phase.

# A. Identification of the critical component 

The identification of the critical component in an industrial plant or a machine can be done using analysis of the data and information gathered during the exploitation of the machine (experience feedback), and by using Failure Modes, Effects, and Criticality Analysis (FMECA).
The principle of experience feedback consists of improving the knowledge of a system through observation, acquisition, analysis, and information processing related to the real operation of the system in its environment. Then, the knowledge gathered can be used to identify the critical component by providing useful information to formal tools such as the FMECA. For example, in electrical rotating machines, the data gathered during a long time period of exploitation can help with estimating the failure distribution on the main components (stator, rotor, bearings, etc.). Then, the component which presents a high percentage of

![img-3.jpeg](img-3.jpeg)

Fig. 5: RUL estimation steps.
failures can be considered as the one to be selected for further analysis.
An example of how to identify the physical critical component in a machine is given in [20].

# B. Condition monitoring of the component 

Once the critical physical component is identified, and the potential failure known, it is necessary to define a set of appropriate sensors, which will be used to monitor the behavior of the component and its degradation. The type and number of sensors depend mainly on the physical phenomena to monitor. The data provided by the sensors are then processed to extract relevant features and information, which will be used during the modeling step. Depending on the type of the degradation phenomena, and the application domain, several types of features can be extracted. The features can be temporal, frequency, or timefrequency. More details on how to choose the sensors and select the features depending on the application are given in [21].

## C. Modeling of the component's degradation

The behavior model of the critical component including its degradation is obtained through a data-driven method, where the features extracted from the raw signals provided by the sensors are used during the learning phase (see Fig. 5) to estimate the parameters of the MoG-HMMs (represented by DBNs) that represent the degradation. Practically, each monitoring signal belonging to a given historical data $\eta$ (related to a degradation) is transformed into a matrix $D_{\chi}^{\eta}$ by signal processing (S.P). In this matrix, each column of X cells corresponds to a snapshot of the features at the instant $t$ for the historical $\eta$.

$$
\text { Raw historical data } \eta \xrightarrow{S . P} D_{\chi}^{\eta}(t)=\left(\begin{array}{ccc}
D_{1}(t) & \ldots & D_{1}\left(T^{\eta}\right) \\
\vdots & \ddots & \vdots \\
D_{\mathrm{X}}(t) & \ldots & D_{\mathrm{X}}\left(T^{\eta}\right)
\end{array}\right) \begin{array}{r}
1 \leqslant t \leqslant T^{\eta} \\
\forall 1 \leqslant \chi \leqslant \mathrm{X} \\
1 \leqslant \eta \leqslant \mathrm{H}
\end{array}
$$

where

$$
T^{\eta}=\text { total duration of the historical } \eta
$$

These features are then used to estimate the Conditional Probability Distributions (CPDs) ( $\pi, A$ et $B$ ) and the temporal parameters (stay duration in each health state) of the DBNs.
The temporal parameters are estimated using the Viterbi algorithm [16]. This algorithm permits us to estimate the sequence of states visited using historical data $\eta$ during the experiment. The estimation of the sequence is done using the degradation's behavior model (with parameters $\pi, A$, and $B$ ) learned from the observations (features $O_{t}=D_{\chi}^{\eta}(t)$ ). So, by assuming that the stay durations in the states are governed by Gaussian laws, one can estimate the mean stay duration $\mu_{d}\left(x_{i}\right)$ and its standard deviation $\sigma_{d}\left(x_{i}\right)$ by using

$$
\begin{aligned}
& \mu_{d}\left(x_{i}\right)=\frac{1}{\Omega} \sum_{w=1}^{\Omega} \Delta\left(x_{i w}\right) \\
& \sigma_{d}\left(x_{i}\right)=\sqrt{\frac{1}{\Omega} \sum_{w=1}^{\Omega}\left[\Delta\left(x_{i w}\right)-\mu\left(\Delta\left(x_{i}\right)\right)\right]^{2}}
\end{aligned}
$$

$\Delta(\cdot)$ stands for the visit duration, $i$ is the state index, $w$ is the visit index, and $\Omega_{x_{i}}$ corresponds to the total number of visits of the analyzed historical data $\eta$. A compact representation of each learned DBN is then given by

$$
\lambda_{\mathrm{DBN}}=\left(\pi, A, B, \mu_{d}\left(x_{i}\right), \sigma_{d}\left(x_{i}\right), \Omega_{x_{\text {final }}}\right)
$$

Furthermore, the estimated sequence of states is used to identify the final state $x_{\text {final }}$, which corresponds to the failure health state of the component, visited by the historical data.

# D. Estimation of the RUL 

The estimation of the RUL and the associated confidence value is done during the exploitation phase (see Fig. 5), after having derived the model of the degradation. Indeed, the learned models are used on-line to detect the current health state of the component, and to calculate its RUL. For this purpose, the observations (features) related to the current component are continuously injected to the learned models to select the one that best fits the observed data. The selection process is based on the calculation of the likelihood probability $\mathrm{P}\left[\mathrm{O} \mid \lambda_{\mathrm{DBN}}\right]$ of the models given the observations. Then, the model that gets the highest probability is chosen to detect the current health state of the component, and to estimate its RUL. The estimation of the RUL and the confidence is done in five steps, which are explained hereafter.

1) The first step consists in identifying the model $\lambda_{\mathrm{DBN}}$, from the list of learned models, that best represents the sequence of current observations (Fig. 5). The best model corresponds to that which gives the highest likelihood probability $\mathrm{P}\left[\mathrm{O} \mid \lambda_{\mathrm{DBN}}\right]$ calculated by the forward-backward algorithm.
2) The second step is the identification of the component's current health state. The Viterbi algorithm is used on the selected model to define the sequence of states that corresponds to the current observed features. The state which is most repeated at the end of the sequence is then retained as the active state.
3) The third step corresponds to the utilization of the current health state, the final state, and the transition probability matrix $A$ of the selected DBN to find the critical path, which goes from the current state to the final state (failure). For this procedure, all transition probabilities $a_{i j}$ which are different from zero are used to define the shortest path by considering only one visit per state. Similarly, the longest path is defined as the path which goes through the maximum number of states.
4) Finally, in the fourth step, the previously defined paths are used to calculate the RUL. This RUL is obtained by using the stay durations in each state of the selected DBN. In addition, the confidence value is computed by using the standard deviations on the stay durations. The confidence coefficient $n$ (for a confidence interval $\alpha$ ) is calculated according to

$$
\Phi(n)=\frac{\alpha+100}{200}
$$

where $\Phi$ is the distribution function of the centered normal law, and $\alpha \in[0,100]$. Consequently, three values of RUL are estimated: upper RUL $(\mu+n \cdot \sigma)$, mean RUL, and lower RUL $(\mu-n \cdot \sigma)$.

$$
\begin{gathered}
\mathrm{RUL}_{u p p e r}(t)=\sum_{i=\text { current state }}^{N}\left[v_{i} \cdot \mu_{d}\left(x_{i}\right)+n \cdot \sigma_{d}\left(x_{i}\right)\right]-\hat{t}_{a c} \\
\mathrm{RUL}_{\text {mean }}(t)=\sum_{i=\text { current state }}^{N} v_{i} \cdot \mu_{d}\left(x_{i}\right)-\hat{t}_{a c} \\
\mathrm{RUL}_{\text {lower }}(t)=\sum_{i=\text { current state }}^{N}\left[v_{i} \cdot \mu_{d}\left(x_{i}\right)-n \cdot \sigma_{d}\left(x_{i}\right)\right]-\hat{t}_{a c} \\
\forall i \in \text { state in the active path } \wedge v_{i} \in\left[0, \Omega_{x_{i}}\right]
\end{gathered}
$$

In the previous expressions, $\tilde{t}_{\mathrm{ac}}$ represents the time spent by the component in the active state. This time is estimated through the equation

$$
\tilde{t}_{\mathrm{ac}}= \begin{cases}0, & x_{t} \neq x_{t-1} \\ \tilde{t}_{\mathrm{ac}}(t-1)+\Delta t, & x_{t}=x_{t-1}\end{cases}
$$

The variable $\nu_{i}$ represents the number of possible remaining visits to the state $x_{i}$. This variable is initialized to the number of visits to the state $x_{i}$, i.e. $\nu_{i}=\Omega_{x_{i}}$. Once the process of current state detection has found a change in state $\left(x_{t} \neq x_{t-1} \wedge \lambda_{\mathrm{DBN}}(t-1)=\lambda_{\mathrm{DBN}}(t)\right)$ or model $\left(\lambda_{\mathrm{DBN}}(t) \neq \lambda_{\mathrm{DBN}}(t-1)\right)$, the variable $\nu_{i}$ is reduced by one unit.

# E. Prognostics performance metrics 

The performance of the proposed prognostics method is assessed through the implementation of prognostics metrics proposed in [8], and [22]. A brief description of the implemented metrics is given hereafter.

1) Accuracy [8]: An accuracy value near to zero means that the predictions are not good, while an accuracy near one corresponds to good predictions.

$$
\text { Accuracy }=\frac{1}{T} \sum_{t=1}^{T} e^{-\frac{\left[R U L_{\text {real }}(t)-R U L(t)\right]^{n}}{R U L_{\text {real }}(t)}}
$$

In (11) $\alpha \in[1,2], T$ is the final time of the historical test, $R U L_{\text {real }}(t)$ is the real value of the RUL at time $t$, and $R U L(t)$ is the estimated value of the RUL at time $t$.
2) Precision [22]: this measure quantifies the dispersion of the prediction error around its mean.

$$
\text { Precision }=\sqrt{\frac{\sum_{t=1}^{T}(\mathcal{E}(t)-\overline{\mathcal{E}})^{2}}{T}}
$$

where

$$
\begin{aligned}
\mathcal{E}(t) & =\operatorname{RUL}_{\text {real }}(t)-\operatorname{RUL}(t) \\
\overline{\mathcal{E}} & =\frac{1}{T} \sum_{t=1}^{T} \mathcal{E}
\end{aligned}
$$

3) Mean Absolute Percentage Error (MAPER): this measure quantifies the mean error in percentage.

$$
\operatorname{MAPER}=\frac{1}{T} \sum_{t=1}^{T}\left|\frac{100 \cdot \mathcal{E}(t)}{\operatorname{RUL}_{\text {real }}(t)}\right|
$$

4) Prognostics Horizon (HP) [22]: this measure estimates the time at which the prognostics algorithm gives its first prediction within the confidence interval defined by $\alpha_{c} \in[0,1]$.

$$
\mathrm{HP}=T-t \quad \forall \mathrm{RUL}(t) \in\left[\mathrm{RUL}_{\text {real }}(t) \cdot(1-\alpha), \mathrm{RUL}_{\text {real }}(t) \cdot(1+\alpha)\right]
$$

5) Performance measure ( $P_{\alpha_{c}-\lambda_{c}}$ ) [22]: it permits one to test if at one or more temporal instants $t=\lambda_{c} \cdot T \quad \forall \lambda_{c} \in[0,1]$ the predicted RUL is within the confidence interval defined by the coefficient $\alpha_{c}$.

$$
P_{\alpha_{c}-\lambda_{c}}=\left\{\begin{array}{l}
\text { No if other } \\
\text { Yes if } \operatorname{RUL}(t) \in\left[\operatorname{RUL}_{\text {real }}(t) \cdot\left(1-\alpha_{c}\right), \operatorname{RUL}_{\text {real }}(t) \cdot\left(1+\alpha_{c}\right)\right]
\end{array}\right.
$$

6) Relative accuracy measure (RA) [22]: it permits one to assess the accuracy of the estimation of the RUL at different times $t=\lambda_{c} \cdot T \quad \forall \lambda_{c} \in[0,1]$.

$$
R A=1-\frac{\left|R U L_{\text {real }}(t)-R U L(t)\right|}{R U L_{\text {real }}(t)}
$$

## III. APPLICATION AND EXPERIMENTAL RESULTS

The method proposed in the previous section is applied hereafter on real experimental data taken from accelerated life tests performed on bearings. First, the choice of bearing as a critical component is motivated, then experimental data and RUL estimation results are given and discussed.

## A. Bearing as critical component

During the last decade, several works have been conducted in the field of failure diagnostics and prognostics of critical physical components such as bearings, gears, batteries, etc. Interested readers can find more details in [12], [23]-[25].
The analysis of the experience feedback performed on electrical machines by the Electric Power Research Institute (ERPI), and researchers in the reliability of electrical machines, has shown that the bearings and the stator are the components which present the most failures (table I). In the following application, bearings are considered as the critical components on which the prognostics method is tested.

TABLE I: Failure distribution in asynchronous motors.


![img-4.jpeg](img-4.jpeg)

Fig. 6: Experimental platform Pronostia: (a) global overview and (b) type of the tested bearing.

# B. Experimental platform: Pronostia

Pronostia is an experimental platform dedicated to test, verify, and validate methods related to bearing health assessment, diagnostics, and prognostics. A general overview of the main parts of the platform and the type of the bearing used for tests are shown in Fig. 6. The main objective of Pronostia is to provide real data related to the degradation of bearings during their useful life. Particularly, in this application, we use the NSK 6804DD bearing, which can operate at a maximum speed of 13000 rpm , and a load limit of 4000 N . Pronostia is composed of two main parts: a first part related to the speed variation, and a second part dedicated to load profile generation. The speed variation part is composed of a synchronous motor, a shaft, a set of bearings, and a speed controller. The synchronous motor develops a power equal to 1.2 kW , and its operational speed varies between 0 and 6000 rpm . The load profiles part is composed of a hydraulic jack connected to a lever arm used to create different loads to degrade the bearing mounted on the platform. The radial load can be varied between 0 and $10,000 \mathrm{~N}$, and the operating speed of the bearing can be controlled within the interval $0-2000 \mathrm{rpm}$. The force delivered by the pneumatic jack is indirectly applied on the external ring of the bearing through a clamping ring (Fig. 7-(b)). The effort is transmitted by a lever arm in rotation, which applies the load on the clamping ring. Two high frequency accelerometers (DYTRAN 3035B) are mounted, one horizontally and one vertically, on the housing of

![img-5.jpeg](img-5.jpeg)

Fig. 7: Multiplication system and load transmission: (a) top view and (b) elements of the transmission chain. the tested roller bearing to pick up the horizontal and the vertical accelerations. In addition, the monitoring system includes one temperature probe (of type PT100) to record the temperature of the tested bearing. A speed sensor and a torque sensor are also available on the Pronostia platform. The sensors are connected to a data acquisition card (NI DAQCard-9174) to provide the user with monitoring data. The sampling frequency is set to 25600 Hz , and the vibration data provided by the two

accelerometers are collected every 1 second.

# C. Experimental data 

A total of 12 accelerated life tests (separated in two groups of 6 tests) under two constant operating conditions are realized on the Pronostia platform. In this paper, only the first six tests (first group) are used. The six experiments are realized under specific operating conditions: the constant speed of the shaft is controlled at 1800 rpm , and the radial load at 4000 N (Table II).

For the estimation of the RUL and the associated confidence, the historical data related to tests $1,3,4,5$, and 6 are used in the learning phase to estimate the parameters of the DBNs, representing the degradation, while the historical data related to test 2 is used in the exploitation phase to calculate the RUL, and the confidence.
Examples of bearingsí $\xi_{\mathrm{i}}$ failure at the end of experiments are shown in Fig. 8. Two types of features are extracted from

TABLE II: Summary of the accelerated life tests on Pronostia.


$\mathrm{ER}=$ Extern ring, $\mathrm{IR}=$ Inner ring
![img-6.jpeg](img-6.jpeg)

Fig. 8: Failure of the bearings of Pronostia: (a) extern ring failure, and (b) inner ring failure.
the raw signal provided by the two accelerometers: temporal features [30] (Root Mean square: RMS, mean value, pick value, crest factor, skewness, etc.), and time-frequency features (energy levels of the signals extracted by using a Wavelet Packet Decomposition: WPD). An example of two temporal features extracted from the horizontal accelerometer is shown in Fig. 9. The drawback of temporal features is that the frequency part is not considered. To overcome this situation, one can use wavelet
![img-7.jpeg](img-7.jpeg)

Fig. 9: Features extracted from the radial accelerometer: (a) RMS, and (b) kurtosis.
transforms, such as WPD, which permits one to adjust the size of the temporal window according to the analyzed frequencies. A WPD has two parameters: a scale parameter $a$ for the frequency, and a translation parameter $b$ for the time [31]. The original

signal can then be decomposed into several levels. The decomposition level can be defined using (17).

$$
J_{f} \leqslant \log _{2} \frac{F_{s}}{3 F_{d}}-1
$$

where $J_{f}$ is the decomposition level, $F_{s}$ is the sampling frequency, and $F_{d}$ is the maximum frequency among the bearing's frequencies.
Fig. 10 shows two results about the percentage of energy extracted from the last levels of decomposition on the frequency band $1-800 \mathrm{~Hz}$.
![img-8.jpeg](img-8.jpeg)

Fig. 10: Percentage of energy of the vertical and horizontal accelerometers after decomposition in wavelet packets for the band $1-800 \mathrm{~Hz}$.

# D. Degradation modeling 

During the learning of the MoG-HMMS models (represented by DBNs) related to the degradations, two parameters are needed: the number of states $N$, and the number of mixtures of Gaussians $M$. In this application, the number of states is set to $3(N=3)$. This choice of number of states is motivated by the fact the degradation of the bearings can be represented by three levels: the nominal health condition, the initiation and propagation of the defect, and the failure level.
For the definition of the number of mixtures, a prior analysis is done. The results of this analysis are shown in Fig. 11. The number of mixtures has been varied during the model learning related to each experiment. Then, for a given number of mixtures, a likelihood $\mathrm{P}[\mathrm{O}] \lambda_{\mathrm{DBN}}$ ] is calculated. Finally, the number of mixtures is taken as small as possible (to avoid model complexity) when the likelihood starts to converge. In the following application, the number of mixtures is set to $M=4$.
The parameters $\pi, A$, and $B$ of the DBNs representing the degradations of the bearings are learned using the Viterbi algorithm,
![img-9.jpeg](img-9.jpeg)

Fig. 11: Sensibility analysis to define the number of mixtures $M$.
and the extracted features (temporal and time-frequency). An example of a generated Viterbi state sequence is shown in Fig. 12. The obtained parameters of the DBN related to each experiment are given in Tables III, and IV.

![img-10.jpeg](img-10.jpeg)

Fig. 12: State sequences obtained by using Viterbi algorithm for experiment 1.

TABLE III: Temporal parameters of the learned model by using temporal features.


# E. RUL estimation, and prognostics performance metrics 

The models $\lambda_{\text {DBN }}$ obtained during the learning phase are used to estimate the RUL, and to assess the performance of the method through prognostics metrics. In this application, the forgotten coefficient $l$ is set to 10 , which means that the recurrent state in the last 10 minutes is chosen as the most probable active state. For the estimation of the confidence limits, (RUL ${ }_{\text {upper }}$, and $\mathrm{RUL}_{\text {lower }}$ ), an interval of $95 \%$ is defined $(\alpha=95)$.
Concerning the prognostics performance metrics, $\alpha_{c}$ is set to 0.3 . This value permits us to tolerate a deviation of $30 \%$ from the real RUL.

For the calculation of $P_{\alpha_{c}-\lambda_{c}}, \lambda_{c}$ is set to 0.5 to verify if at the middle of the historical data length $(T / 2)$ the predictions are within the confidence interval $\alpha_{c}$. Concerning the relative accuracy, it is assessed for three values $\lambda_{c}=[0.75,0.5,0.25]$ corresponding to three time intervals: the beginning, the middle, and the end of the historical data. The results obtained from the implementation of the prognostics performance metrics on temporal and time-frequency features are given in Table V. The prognostics results obtained for the experiments realized on the Pronostia platform are shown in Fig. 13. The results shown in Fig. 13-(a) are obtained from the temporal features, while those obtained from wavelet features are given in Fig. 13-(b). By observing the results shown in Fig. 13-(a), one can note that there is no change in the confidence limits. In addition, the estimated RUL is a line which is parallel to the real RUL. This result can be explained by the fact that, during the estimation of the RUL, the best model was always that which corresponds to Experiment 4. According to the learning results given in Table III, the historical data of Experiment 4 is represented by the left-right model (only transitions from left states to right states are allowed in the MoG-HMM), which produces null standard deviations $\sigma_{d}$. However, it can be seen that the estimated

TABLE IV: Temporal parameters of the learned model by using time-frequency features.


RUL is relatively precise, as confirmed by the performance measures given in Table V (accuracy equal to 0.7874). Moreover, the precision is good with a dispersion of 4.91 min . Also, the value of the HP measure is equal to 409 min , which means that 1 min after the launch of the prognostics method, the predictions entered the confidence interval.

The prognostics results obtained by using the wavelet features are shown in Fig. 13-(b). Contrary to the results obtained from
![img-11.jpeg](img-11.jpeg)

Fig. 13: Estimation of the RUL for experiment 2: (a) temporal features, and (b) time-frequency features.

TABLE V: Prognostics performance metrics.


the temporal features, one can observe a variation in the confidence limits. From Fig. 13-(b), one can see that the real RUL is within the confidence interval during the whole experiment. This result can be explained by the fact that the time-frequency features are more sensitive to the degradation, allowing us to update the models $\lambda_{\mathrm{DBN}}$, and to calculate the RUL value. This behavior, sensitive to the degradation, has allowed us to create good estimations of the $\mathrm{RUL}_{\text {mean }}$. In addition, this estimation is confirmed by a prognostics horizon equal to 405 min , a good value of the measure $P_{\alpha_{c}-\lambda_{c}}$, and relative accuracies near 1.

# IV. CONCLUSION 

A data-driven prognostics method based on the utilization of data provided by monitoring sensors is presented in this paper. The aim of the method is to estimate the remaining useful life of an industrial plant by focusing on its most critical component. The degradation of this component is then modeled using Mixture of Gaussians Hidden Markov Models (represented by DBNs), which permit us to represent the evolution of the degradation using hidden states. The estimation of the remaining useful life is done in two main phase: a learning phase to derive the degradation's behavior model, and an exploitation phase to estimate the RUL and its associated confidence.
The proposed method is applied to real data related to accelerated life tests on bearings, and the results of the RUL are given and discussed. Two types of features are tested: temporal, and frequency. Furthermore, prognostics metrics are implemented to assess the performance of the prognostics results obtained by the method.
The proposed prognostics method has been applied to the degradation of bearings operating at constant conditions (constant load, and speed). This method can be easily applied to other types of physical components. It can be also extended to variable operating conditions. However, this latter point requires one to adapt the model learning and selection process, and also the computation of the RUL.
