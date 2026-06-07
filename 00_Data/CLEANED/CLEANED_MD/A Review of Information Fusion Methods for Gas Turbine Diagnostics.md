# Review <br> A Review of Information Fusion Methods for Gas Turbine Diagnostics 

Valentina Zaccaria *, Moksadur Rahman ${ }^{\ominus}$, Ioanna Aslanidou and Konstantinos Kyprianidis ${ }^{\ominus}$<br>School of Business, Society and Engineering, Mälardalen University, 72123 Vasteras, Sweden; moksadur.rahman@mdh.se (M.R.); ioanna.aslanidou@mdh.se (I.A.); konstantinos.kyprianidis@mdh.se (K.K.)<br>* Correspondence: valentina.zaccaria@mdh.se

Received: 27 September 2019; Accepted: 4 November 2019; Published: 6 November 2019 check for updates


#### Abstract

The correct and early detection of incipient faults or severe degradation phenomena in gas turbine systems is essential for safe and cost-effective operations. A multitude of monitoring and diagnostic systems were developed and tested in the last few decades. The current computational capability of modern digital systems was exploited for both accurate physics-based methods and artificial intelligence or machine learning methods. However, progress is rather limited and none of the methods explored so far seem to be superior to others. One solution to enhance diagnostic systems exploiting the advantages of various techniques is to fuse the information coming from different tools, for example, through statistical methods. Information fusion techniques such as Bayesian networks, fuzzy logic, or probabilistic neural networks can be used to implement a decision support system. This paper presents a comprehensive review of information and decision fusion methods applied to gas turbine diagnostics and the use of probabilistic reasoning to enhance diagnostic accuracy. The different solutions presented in the literature are compared, and major challenges for practical implementation on an industrial gas turbine are discussed. Detecting and isolating faults in a system is a complex problem with many uncertainties, including the integrity of available information. The capability of different information fusion techniques to deal with uncertainty are also compared and discussed. Based on the lessons learned, new perspectives for diagnostics and a decision support system are proposed.


Keywords: data fusion; diagnostics; gas turbine

## 1. Introduction

The growing penetration of renewable energy sources into the grid at a centralized and decentralized level represents a promising step toward a low-carbon society, but brings with it several challenges related to reliability, resiliency, and sustainability [1]. Gas turbines still have an important role in this scenario and are actually considered a key technology to favor a smooth transition; for example, the use of hydrogen or biogas in gas turbine plants is raising much attention [2-4]. Gas turbine-based hybrid systems (e.g., solar hybrid [5] and fuel cell hybrid [6]) are also considered promising solutions for increasing efficiency, flexibility, and availability of renewable power generation. An interesting role for gas turbine technology, given the substantial energy consumption from buildings, is in distributed applications for residential sector and micro grids [7]. In fact, the role of buildings is expected to expand from energy savings to becoming active elements in future energy systems, allowing their occupants to use, supply, and store energy in a more flexible and smarter way [8]. Small cogeneration systems based on gas turbine technology can provide a more efficient utilization of fossil fuels, as well as a better integration with renewables in residential applications [1].

In this view, it is evident that effective diagnostic and prognostic systems are essential for the sustainable management of gas turbine plants, especially in a future energy market where these machines will experience frequent starts and stops or fast load, following the accommodation of renewable energy fluctuations, which will directly affect component lifetime. In addition, the need for reducing maintenance and operating costs to guarantee accessible energy for everyone is strong. Progress has to be made in condition-based maintenance to ensure that the future role of gas turbines will be sustainable.

Automated systems for degradation monitoring and fault diagnostics are commonly used currently in gas turbine power plants. Over the decades, a myriad of methods and techniques were proposed and developed to address the challenge of early detection of incipient faults or failures, and effective maintenance planning. The simplest tools are those performing anomaly detection; when a measurement or a monitored parameter exceeds a predefined threshold or its trend differs from what is expected, an anomalous condition is flagged. These systems do not give any indication of the problem source, but merely point out that something is not working as expected. They can be as simple as a threshold exceedance or they can employ artificial intelligence for pattern recognition [9-11].

Once an anomaly is detected, the wish of the service engineer (or the operator) is to isolate the anomalous component, identify the severity of the problem, and ultimately answer the following question: "Can the machine still operate in a safe condition, or which corrective action needs to be performed?" Numerous model-based solutions were investigated until now, which include filters for states estimation [12], performance models coupled to various optimization algorithms [13-15], and machine learning models such as neural networks, support vector machine, etc. [16,17]. The common purpose of these techniques is to estimate non-measurable quantities, i.e., some performance deviation indices, from available measured data. Extensive reviews of currently used methods can be found in the literature, for example, References [18,19].

Parameters such as deviation in efficiency or flow capacity are often considered as health indicators; however, they are affected not only by thermodynamic "anomalies" (e.g., fouling, erosion, corrosion) but also by other malfunctions or mechanical integrity (e.g., wrong variable guide vane (VGV) position, wrong valve position, foreign object damage (FOD), etc.). Diagnostic systems based on performance models and optimization tools usually detect thermodynamic deviations without relating them to the occurred event. Classification of fault or malfunctions is often provided through statistical methods or machine learning techniques. However, classification algorithms suffer one major drawback, i.e., the necessity of a large amount of historical data. Depending on the available data, certain faults may not be recognized or, on the contrary, perfectly healthy operations can be classified as faulty conditions if lying outside the training space. All methods also have various degrees of sensitivity to noise and model uncertainties $[20,21]$.

Data pre-processing and correction is fundamental for any type of diagnostic system [22-24]. Because gas turbine performance is extremely sensitive to ambient conditions, measured data need to be corrected to isolate the effect from that induced by a fault. Measurements can be manipulated to extract useful features (or information) that can work as input of the diagnostic tool. Multiple methods were proposed for data correction and feature extraction, such as in References [15,23,25].

In order to combine the benefits from different methods for data processing, anomaly detection, and fault identification, the approach of information fusion was proposed. Various pieces of information coming from different sensors, models, or algorithms can be fused together to achieve the right answer to the question previously formulated. The concept of integrating and fusing multiple information aims at emulating human reasoning, which is extremely effective in drawing conclusions even in the presence of uncertainty. An illustration of what is required in industry was provided by Zhang et al. [26], who presented an effort to integrate human experience, expert reasoning systems, and signal processing. The key is not to exclude the human but to leverage digital tools to include human experience and, at the same time, supervise the automated system, which learns from the experts.

In this paper, a review is given concerning the information fusion approach applied to diagnostics and prognostics in gas turbine systems. Information fusion is often mentioned as a promising solution for enhanced diagnostic and decision support systems (DDSS) in numerous review articles [18,27]; however, the lack of a focused review and a discussion of different methods and applications is what this paper aims to address.

# 2. Background 

The concept of data and information fusion for gas turbine diagnostics and decision support was already discussed in the 1990s, especially given the increasing use of belief networks combined with thermodynamic models for diagnostics [28]. Bayesian belief networks (or BBNs) started being used to fuse the information coming from gas path analysis with other observations, including maintenance history, and to capture the experience of the service engineer [29].

A first concept of data fusion for enhanced prognostics was proposed by Hansen et al. [30]; in their framework, sensor data were fused with models of fault evolution to predict the remaining life of the component. In the following years, Hall et al. suggested including negative information in the fusion system to rule out possible causes if one or more expected evidences did not occur [31]. This is actually possible through both probabilistic and fuzzy inference. The promising opportunities opened by information fusion led Impact Technologies LLC to present a proof of concept for an integrated diagnostics and prognostics framework [32]. In their article, Roemer and Kacprzynski theoretically discussed the implementation of such a framework based on the concepts of sensor data fusion and information fusion for failure prognostics. A Bayesian inference algorithm was recommended for fusing the diagnosis information from two techniques, namely, a collaborative probabilistic fault identification and neural-network pattern recognition, and from vibration analysis; finally, information from the diagnostics module and remaining lifetime models was combined. The concept of multiple-source information fusion with a Bayesian network is illustrated in Figure 1 and is explained more in detail in the next section.
![img-0.jpeg](img-0.jpeg)

Figure 1. Outline of a multi-source information fusion tool based on a Bayesian network.

## 3. Common Tools and Methods

Over the years, multiple methods for information fusion were explored; the most common are summarized below. Due to the uncertain nature of the data and event observation, stochastic methods are preferred for the task of information fusion. The most common techniques include Bayesian belief networks (BBNs), Dempster-Schafer (DS) theory, fuzzy logic inference, and probabilistic neural networks (PNNs). These are briefly introduced in this section, with more space given to Bayesian networks. An overview of the methods and applications can be found in Reference [33].

# 3.1. Kalman Filters 

One of the most used methods for information fusion, especially for sensor data, is the Kalman filter and its variants. As a fundamental principle, the Kalman filter estimates states in the system from the available measurements; this procedure includes two steps, prediction, as shown in Equations (1) and (2), and correction, as shown in Equations (3)-(5).

$$
\begin{gathered}
\hat{x}_{k}=F x_{k-1}+B u_{k-1} \\
P_{k}=F \cdot P_{k-1} \cdot F^{T}+Q \\
\varepsilon_{k}=y_{k}-H \hat{x}_{k} \\
K=P_{k} \cdot H^{T}\left(R+H \cdot P_{k} \cdot H^{T}\right)^{-1} \\
x_{k}=\hat{x}_{k}+K \varepsilon_{k}
\end{gathered}
$$

In the above equations, $x$ is the estimated state multiplied by a state-transition matrix $F, B$ is the observation model applied to the control vector $u, P$ is the covariance matrix, $Q$ and $R$ are the covariance matrices of process and observation noise, respectively, and $y$ is the measurement.

Multiple solutions to modify the original algorithm for data fusion were proposed, such as in Reference [34]. For example, states estimated from multiple sensors can be fused by weighting matrices as a function of the covariance between measurements. In other problems, one sensor can provide the a priori information for the prediction algorithm.

### 3.2. Bayesian Networks

Bayesian networks represent a culmination of the Bayesian theory of probability, which can be summarized as shown in Equation (6). The equation represents a casual statement of the kind $X \rightarrow Y$, where $X$ causes $Y$ and $Y$ takes the role of an observable effect of $X . P(Y)$ is called the prior probability, while $P(Y \mid X)$ is called the posterior probability. The factor that relates the two, $P(X \mid Y) / P(X)$, is called the likelihood ratio.

$$
P(Y \mid X)=\frac{P(X \mid Y)}{P(X)} P(X)
$$

A BBN is a probabilistic graphical model that represents the factorization of joint probability distribution [35]. It provides a comprehensive way to handle uncertainty in mathematical computation, and it is consequently widely used for representing uncertain knowledge. Bayesian probability differs from classical probability by the fact that classical probability does not put any weightage to the evidence, while Bayesian probability always comprises a certain degree of belief in the evidence [36]. The most beneficial aspect of a BBN is that it can be constructed with a limited dataset or even in the absence of data only by integrating expert knowledge [37,38]. A BBN model can also produce partial results with missing data, which can be beneficial in an industrial set-up. As soon as new evidence become available, the BBN can be inferred to update belief in a specific outcome.

A BBN has two major parts, as shown in Figure 1: a qualitative or structural part, consisting of a directed acyclic graph (DAG), and a quantitative part, which is a set of conditional probability distributions. Typically, a DAG consists of a finite number of nodes and edges, where each edge corresponds to a conditional dependency, and each node corresponds to a unique random variable. As the directed edges represent a static causal probabilistic dependence, cycles are not allowed in the graph. As a result, they are called acyclic graphs. The edges are irreversible. It is important to note here that a node in a BBN is only dependent on its "parent" nodes. Therefore, BBNs have a local Markov property.

Constructing a BBN involves building the structural part of the BBN or DAG and specifying the conditional probabilities also known as parameters. A BBN can be constructed completely manually from expert knowledge, completely automatically from data, or through a combination of a manual

and automatic technique, where partial knowledge about the structure or the parameters is learnt from the data [35]. Over the years, many learning algorithms such as the search-and-score approach, constraint-based approach, bootstrap approach, K2 algorithm, three-phase dependency algorithm, etc. were explored for structural learning of a BBN from historical data [39,40,41]. On the other hand, manual construction of a BBN structure is also possible, but can be very labor-intensive, requiring a great deal of skills, as well as in-depth knowledge on the problem domain. Similar to DAG, parameters can also be estimated from historical data and expert knowledge. The most popular techniques for identifying parameters from data are maximum-likelihood estimation and Bayesian estimation [42].

An example BBN structure for multi-source information fusion is depicted in Figure 2. Here, the $X_{i j}$ node denotes the input information collected from information source " $i$ " about the fault type " $j$ ", and the $Y_{j}$ node denotes the fused information about the fault type " $j$ ".
![img-1.jpeg](img-1.jpeg)

Figure 2. The Bayesian network structure for multi-source information fusion.
Bayesian networks were extensively used in the gas turbine field for fault diagnosis purposes, and multiple examples can be found in the literature of BBN application to modeling of gas turbine components, anomaly detection, fault identification, and information fusion [43,44,45]. These articles illustrate some of the principles to construct a BBN for fault detection, isolation, and classification in gas turbines. Figure 3 depicts three general BBN structures for different applications. In Figure 3a, the common structure for fault classification is shown, where evidence coming from sensors is fused together to establish a probability for a certain component to be faulty through reverse reasoning. Another application, presented in Figure 3b, is for sensor validation purposes, as shown in Reference [46]. It was pointed out by the author of Reference [46] that a multilayer approach is beneficial when the first layer is given by the structure in Figure 3b for anomaly detection, and a second layer is used for fault isolation. If, for example, Measurement 1 is related to Measurements 2 and 3, the probability of reading a certain value for Measurement 1 is computed from the values of Measurements 2 and 3, and, if it lies below a defined threshold, a sensor failure is detected. The final schematic, in Figure 3c, is an example of a BBN used for information fusion, where faulty conditions estimated by various diagnosis methods are used as evidences to increase the belief that a specific fault occurred [47].
![img-2.jpeg](img-2.jpeg)

Figure 3. Cont.

![img-3.jpeg](img-3.jpeg)

Figure 3. General Bayesian network structure for fault classification (a), sensor validation (b), and information fusion for diagnostics (c).

# 3.3. Dempster-Schafer Theory 

As a generalization of Bayes theory, the Dempster-Schafer (DS) theory assigns different degrees of belief, called masses, to each subset of propositions that form a system (e.g., set $A$, set $B$, both, neither). Unlike Bayes theory, the probability of an event is bounded between a belief level and a plausibility level. Belief from different sources can be combined through the DS rule, which calculates the resulting mass from Equation (7) and ignores conflicting evidences through a normalization factor, as shown in Equation (8).

$$
\begin{gathered}
\left(m_{1} \otimes m_{2}\right)(C)=\frac{1}{1-K} \sum_{A \cap B=C \neq \varnothing} m_{1}(A) m_{2}(B) \\
K=\sum_{A \cap B=\varnothing} m_{1}(A) m_{2}(B)
\end{gathered}
$$

In this case, Equation (7) calculates the cumulative belief for set $C$ given the sources of information $A$ and $B$. If $A$ and $B$ do not have any element in common (i.e., in the presence of conflicting evidence), the term $K$ is equal to 1 , and the problem has no solution.

### 3.4. Fuzzy Inference

In the presence of incomplete or imprecise information, fuzzy logic can be used to perform so-called approximate reasoning, via combining membership functions through a set of rules (IF ... AND ... OR ... THEN). A membership function represents the possibility of an element $x$ to be a member of a certain set (for example, the set denoting "faulty compressor"). The difference from probability distributions is the fuzziness of the membership function, which considers that $x$ may belong to both sets "faulty compressor" and "healthy compressor" with different degrees, whereas the probability theory tells us that the compressor is either faulty or not, and we have different

levels of confidence in each proposition. An example of membership functions is shown in Figure 4. Logic IF/THEN rules can be used to determine the output function from the membership degree of $x$ to the various membership functions that are built based on expert knowledge [48,49].
![img-4.jpeg](img-4.jpeg)

Figure 4. Example of fuzzy membership functions.

# 3.5. Probabilistic Neural Networks 

A neural network is a mathematical model that emulates the structure and working principle of the neurons in the brain. A PNN is a particular type of neural networks based on the Bayes pattern classification strategy that performs statistical classification [19]. The architecture of a typical PNN is illustrated in Figure 5; the input layer represents the available information (e.g., measurements), the hidden layer is the pattern layer, and the output or summation layer represents the desired classification groups (e.g., type or location of faults).
![img-5.jpeg](img-5.jpeg)

Figure 5. Probabilistic neural network architecture.
The hidden layer is formed by all training patterns, where each neuron corresponds to a specific pattern in the training dataset. The output of these neurons indicates how close a generic input pattern is to the training pattern, giving statistical (probabilistic) information. The outputs of the pattern layer are all summed in the summation layer, where the neuron with a higher sum is considered the most likely class. A considerable advantage of PNNs is their simplicity in building and training them [50]. In gas turbine diagnostics, PNNs were used for fault classification and compared with other pattern classification algorithms, where they were proven to have similar accuracy [50,51,52]. The method was also applied to sensor fault diagnostics [53], and in conditions of a deteriorated engine [54].

## 4. Fusion Architectures

Common information fusion systems can be classified as follows, depending on the level on which data or other pieces of information are combined and fused together:

- Sensor-level fusion;
- Feature-level fusion;
- Decision-level fusion.

The first strategy is used to combine data from various correlated sensors to enhance the quality of the information for diagnostics purposes. The second method combines features extracted from different measurements or obtained through different data analysis methods to provide more information to the diagnostic tool(s). At the decision level, performance changes or event detection resulting from multiple analysis methods are combined, often including an assessment of the confidence level of the diagnosis. Results from a single fault detection system or from the fusion of multiple methods can also be combined with other information such as maintenance history, operator observations, experience from similar units, etc. The complexity increases generally from the sensor level to the decision level. The three levels are depicted in Figure 6.
![img-6.jpeg](img-6.jpeg)

Figure 6. Three levels of information fusion for diagnostic and decision support systems.

# 4.1. Sensor-Level Fusion 

Sensor-level data fusion is used to combine measurements from different sensors with the purpose of validating the measurement values and/or detecting sensor malfunctions, and providing more reliable data to the diagnostic system. As for other levels of information fusion, the techniques for sensor data fusion range from a simple weighted average to Kalman filters, probabilistic methods (e.g., Bayesian or Dempster-Schafer theory), and fuzzy logic.

An approach for sensor fusion through fuzzy inference in a gas turbine power plant was proposed by Goebel and Agogino [55]. Values of important variables such as compressor outlet pressure, $p 2$, were computed from different combinations of other measurements and compared with the measured value (e.g., measured $p 2$ ). A confidence level was calculated for each measurement, and the values were fused accordingly to provide a unique value with high confidence level. The proposed algorithm was proven to be robust toward sensor faults.

Fusion of vibration and gas path measurements through principal component analysis allowed extracting common features from various sensors and performing anomaly detection on a heavy-duty gas turbine [56]. The fusion of information from hardware sensors and soft sensors for increased diagnostics effectiveness was also tested and discussed [57]. An extended Kalman filter was employed in Reference [58] to cope with time delay uncertainty in various sensors and fuse their information.

An interesting piece of work was presented by Liu et al. [59-61]. Sensor data were fused to obtain one health index (HI) that was used as an indication of system degradation and as the main parameter to calculate remaining lifetime in an aero-engine. Weight coefficients for the fusion function were calculated via quadratic programming to guarantee two properties of the HI: a monotonic trend of degradation signal and minimal variance in degradation threshold. The progress from the early study

to the most recent one includes assessment at various operating conditions, by modeling the weights for combining sensor data as a function of the engine operating condition [61]. Similarly, Chen et al. selected a health indicator through a genetic algorithm optimization to fuse measurement data into a parameter that would give optimal results in anomaly detection and remaining life estimation [62].

# 4.2. Feature-Level Fusion 

An important step in data processing is the extraction of features, which is a common term to indicate processed measurement data that contain useful information for the diagnostics, prognostics, and decision-making levels. Common feature extraction methods include data normalization against nominal or expected values to create a series of measurement deviations (as shown for example in Reference [63]). When dealing with acoustic or vibration measurements, statistical analysis is widely used to extract information such as the mean, standard deviation, skewness, etc.; spectrum analysis, often by means of Fourier transform, is commonly employed to extract features in the frequency domain [56].

Feature-level fusion is, thus, very common for vibration monitoring. The comparison and aggregation of correlated measurements through statistical features extraction was proven successful for sensor fault detection [64]. Data fusion for vibration sensors in rotating machines was performed through a method called poly-coherent composite spectrum, which combines the information of amplitude and phase from all vibration measurements [65]. Kyriazis et al. combined features extracted from vibration sensors and from non-linear gas path analysis (GPA) through a certainty factor fusion approach to select the health parameters for a subsequent GPA [66].

Similarly, a data fusion system for the detection of foreign object damage (FOD) in a turbofan engine was developed based on a fuzzy inference system to combine features extracted from GPA and vibration sensors and successive Dempster-Schafer theory for fusing the fuzzy diagnosis [67]. The evidence of FOD resulting from Kalman filter estimations and vibration analysis was converted into probability functions through a fuzzy inference engine; these were consequently aggregated using the Demspter-Schafer technique to determine the probability of FOD occurrence. It was pointed out by Turso and Litt that the use of BBNs for diagnostics and data fusion requires precise knowledge of the conditional probabilities, either from test data or from well-understood distributions presented in the literature, which poses challenges [67].

Another example of multi-sensor information fusion in an aircraft engine was presented by Sarkar et al., by using symbolic dynamic filtering to extract and combine features from various sensors and provide them to the diagnostic system [68].

Some of the data fusion methods for sensor and feature levels are summarized in Table 1, where the improvement with respect to using a single sensor is highlighted.

Table 1. Summary of data fusion methods. PCA—principal component analysis; HI—health index; DS—Demspter-Schafer technique; PDF—probability density function.


# 4.3. Decision-Level Fusion 

At the decision level, results from multiple independent diagnostic and prognostic methods can be fused together to provide a more accurate and confident estimation, due to the fact that different techniques can be more suitable for identifying different problems. Estimations from one or multiple methods can also be combined with other types of information: vibration analysis, maintenance history, behavior of similar units, observations during inspections, negative information, etc. These two approaches can be considered as happening at two levels, where the first one is the automated decision level and the second one is the supervised decision level. While the first level was the object of extensive research, not many examples of the latter can be found in the literature; one interesting work on the integration of the two layers of decision level fusion was presented in Reference [69].

The simplest approach for information fusion is voting. Each diagnostic method results in a classified fault, which counts as one vote. The fault that has the largest number of occurrences is selected as the most likely. The main disadvantage with this approach is that, in the case of an even number of events and equal number of occurrences, a final decision cannot be taken; furthermore, if wrong classifications occur at the first level, the same wrong conclusion may be drawn after the voting.

In a combined effort among NASA, Pratt \& Whitney, and several technical companies, a framework for information fusion at feature level for aero-engine diagnostics was proposed in 2004 [69]. Two levels of information fusion constituted the health management framework; the first level combined the information coming from GPA, an anomaly detection block based on NN, and vibration and structural measurements. Health assessment of engine components and sensors could be performed at this level, which was in turn fed to the second tier, where the information was combined with maintenance history data, and pilot observations to provide a suggestion on maintenance action. A fuzzy belief network (FBN) was selected for the first information fusion layer, given its fast computability, while a BBN constituted the second level.

In Reference [70], an information fusion technique based on the integration of a Kalman filter and a BBN was presented. The Kalman filter was used for fault diagnostics, and the BBN provided a priori knowledge to the Kalman filter, fusing information coming, for example, from historical or statistical data. This first attempt was successful in improving the final diagnostic results. The challenge of different probability distributions required by the Kalman filter and provided by the BBN was overcome by converting the BBN results into a Gaussian distribution with the same mean and variance.

Extensive work on this topic was performed by the research group at the National Technical University of Athens throughout the 2000s. Kyriazis et al. [71] proposed, for the first time, an information fusion system based on probabilistic data, and compared for this purpose a probabilistic neural network (PNN) and a dynamic Bayesian belief network (BBN). They used different diagnostic methods for first-level diagnostics, including different pattern classification techniques and the use of PNN for fault classification. The results of the different diagnostic tools were combined in a $K \times W$-dimensional vector, where $K$ is the number of first level diagnostic techniques used and $W$ is the number of faults. A set of vectors for various possible faults were used to train both a PNN and a BBN. The output of the probabilistic information fusion system was a vector with $W$ elements, where each element corresponded to the probability of that particular fault occurring. Both information fusion techniques improved the final diagnostic result, but none seemed superior in the cases presented. The authors did not make any comparison of the accuracy, computational time, time needed for training, etc.

The same authors proposed later on the application of Dempster-Schafer technique for information fusion [72]. Results from two independent probabilistic diagnostic approaches (a PNN and a BBN) were combined through the DS technique to establish the most likely event. The probabilistic nature of the fault classification results from PNN and BBN made these methods perfect for the information fusion technique proposed. A comparison with the previous method was, however, not provided. The same DS technique was later extended to successfully detect the gradual deterioration of engine components by fusing the results from a model-based tracking system and a statistical approach [73].

Successively, the same group of authors proposed the use of a linear opinion pool for probability aggregation as an information fusion technique [74,75]. In the first study, the results of two PNNs were aggregated through the linear opinion pool, which is a weighted average of the probability functions for each health parameter, and a consensus vector was generated. Subsequently, two fuzzy logic approaches were used to establish the most likely fault based on the consensus vector. Both approaches gave the same results, reducing the number of misclassifications. The same fusion technique was later applied in a second study, where non-linear GPA was used to identify health parameters in multiple sub-systems of the engine [47]. The probabilistic results for all the sub-systems were aggregated to select the fault parameters, and the non-linear GPA was performed a second time on the selected parameters to isolate the one that gave the maximum diagnostic index (ratio between mean value and standard deviation). In a further attempt to improve the fault classification system, the group of authors proposed a new weighting procedure for the results from different diagnostics methods feeding the BBN fusion system [47]. A summary of their results on the investigation of different fusion techniques is given in Table 2, where the number of misclassifications over the number of tested cases (radial or axial compressor cases) is presented. Since the investigated cases were approximately the same in all studies, a comparison of these results is effective for a preliminary assessment of the benefits of fusion techniques.

Table 2. Summary of fusion methods results for similar case studies applied to axial and radial compressors. BBN—Bayesian belief network; PNN—probabilistic neural network.


In the field of prognostics for aircraft engines, a fusion approach was applied to estimate the remaining useful life [76]. Three models for engine life estimation, based on Dempster-Schafer theory, support vector machine (SVM), and recurrent NN were combined through the comentropy fusion technique. The comentropy index was calculated as a function of the prediction error of each method; this approach requires the availability of historical data to train the prognostic algorithms and estimate the prediction errors and consequent weights for the fusion method.

More recently, data fusion was used to estimate faults or engine degradation during transients [77]. The method was based on particle filters applied to different engine partitions, whose results were weighted with their covariance and then fused by a master filter. The global estimates from the master filter were fed back to the local filters for the next time step. In a further work, the research group developed a diagnostic system based on the fusion at feature level between a machine learning algorithm and particle filter/fuzzy inference method [78]. Information fusion was accomplished by means of DS theory with evidence reliability coefficients, and the results showed sufficient accuracy even in the presence of modeling uncertainty. Lu et al. successively demonstrated the use of a non-linear Kalman filter with a distributed architecture for information fusion [79].

A generalized architecture for a health management fusion system was proposed in Reference [80], where a BBN constituted the deeper decision level of information fusion, and its conditional probabilities were based on the maintenance history and the reliability of the diagnostic methods. In another study, a two-layer fusion approach for decision support was presented [81]. Firstly, the outputs of several

classifiers were decomposed into binary classifications, and a dynamic fusion algorithm correlated the outcomes at different time epochs within a sliding window.

# 5. Discussion 

The choice of the best information fusion technique for diagnostics is highly dependent on the type of data that need to be combined. When the data are homogeneous, e.g., multiple sensor measurements of the same variable or performance deviations calculated by various algorithms, purely mathematical or statistical fusion techniques can be applied. Learning techniques such as PNN and BBN do not appear to always perform better, despite the more complex algorithms that aim to emulate human reasoning. When heterogeneous information needs to be fused together, e.g., vibration and gas path measurements, BBN appears to be the preferred choice to handle information coming from very disparate sources. The work analyzed here is grouped in Table 3.

In gas turbine engines, useful information is limited by sensor availability and normally affected by noise and bias. In the presence of such uncertainties, stochastic reasoning is preferred for decision-making, which explains the wide popularity of the BBN and DS methods. However, expert systems and decision support systems ought to function in uncertain environments where information is often incomplete or lacking. Conditional probabilities of each event are usually impossible to know when setting up the information fusion system, and sufficient data to train the stochastic model may not be available. This represents a drawback of employing BBNs. Furthermore, as the nets become quite complex for the purpose of information fusion at the decision level, with several nodes and connections, the conditional probability table grows exponentially and can easily become intractable. However, BBNs are among the most used technique for information fusion at the decision level, where probabilistic reasoning is preferred.

The use of PNNs brings the advantage of less required training and no required a priori knowledge of conditional probabilities, since only a limited number of patterns are sufficient for setting up the network. The capability of PNNs for sensor and engine diagnostics was proven to be comparable with other neural networks; however, for information fusion, it does not appear to be a popular choice given the simplicity of reasoning.

Dempster-Schafer theory is frequently selected for information fusion at all levels thanks to its probabilistic structure and the major flexibility compared to BBNs, since detailed a priori probabilities are not required. Implementation of the DS technique and estimation of the masses are simpler tasks than constructing a conditional probability table for a large BBN. Among the drawbacks, there is, however, a similar limitation in performance in the presence of fuzzy or incomplete information. Furthermore, DS theory may not perform well in the presence of conflicting evidence, even if multiple modifications of the theory were suggested to overcome this drawback.

Table 3. Summary of data fusion methods.


Fuzzy inference, hence, appears to be an interesting choice for information fusion, especially at the decision level, since it presents the following advantages:

- It can deal with incomplete and fuzzy information, including conflicting evidence;
- It does not require a priori knowledge of condition probabilities;

- It is robust toward measurement uncertainty;
- It provides a confidence level associated with the results.

On the other hand, high expert knowledge or a large amount of training data are required to derive the fuzzy rules, on which the diagnostic accuracy depends. Fuzzy membership functions can be used for feature fusion and combined with other probabilistic fusion methods, as shown in Reference [69], or in a structured net to form an FBN, as presented in Reference [71]. However, despite the remarkable advantages and the extensive use of fuzzy logic for diagnostics in gas turbine systems, this technique remains to be fully studied for information fusion purposes at the decision level.

# Weights 

One major concern is that the results from the fusion algorithm could be less accurate than those from a single diagnostic system, since they may be affected by the poorly performing methods in certain situations. To limit this risk, a common practice is to weight the inputs to the fusion algorithm. The weights should be related to the accuracy or importance of each feature or result and, hence, come often from a priori knowledge. Kyriazis and Mathioudakis proposed a weighting system based on the efficiency of the utilized diagnostic techniques (i.e., a higher weight was attributed to the technique with a higher success rate) [47]. In Reference [78], the weights of the inputs to the DS fusion scheme were used as a function of the evidence reliability for each fault detection method, as extracted from a confusion matrix. It was pointed out in Reference [61] that different sensors can be more sensitive to variations in different operating conditions; therefore, a model to calculate fusion weights as a function of operating conditions was proposed.

Satisfactory a priori knowledge of the weights is not always possible. If sufficient information is not available, the weights could be estimated and consequently updated based on probabilistic distributions of results. For transient operations or degradation monitoring, the weights are often a function of data scatter or covariance [73,77].

## 6. Future Perspectives and Recommendations

Among the different methods presented, Bayesian networks attracted the most interest, although the use of fuzzy logic may be more promising and should be further investigated and tested. Some comparisons between fusion techniques at the decision level could be determined from the results obtained by the authors in References [47,71,72,74,75]. It appears that a similar success rate can be achieved with different fusion techniques, leading to the consideration that the accuracy of the underlying diagnostic systems may be more important than the choice of fusion method. However, a more systematic comparison of qualitative and quantitative aspects (e.g., computational time, difficulty of integration into an existing system, etc.) is still lacking. Future research should cover these elements to achieve better conclusions on the use of information fusion systems.

## Micro Gas Turbine Diagnostics and Decision Support

An attractive application for advanced decision support systems is the world of micro gas turbines for distributed generation in buildings. Micro gas turbines in the size of $1-100 \mathrm{~kW}$ were the focus of recent development to obtain combined heat and power (CHP) systems with efficiency levels close to those of larger generation plants. When going to the small and micro scale, the efficiency levels in micro gas turbines are inevitably limited by small-scale effects due to their size, and relatively high auxiliary system losses due to the low power output level [7]. Improvements on these aspects are not compatible with the need for reduced costs. However, the development of small turbochargers from the automotive industry achieved isentropic efficiencies in the levels of $75 \%$ for compressors and $70 \%$ for turbines [7,82], which currently allows the use of off-the-shelf turbocharger parts for the realization of small gas turbine units with practical efficiency levels at low cost. In this way, a competitive market

for these small CHP units is to replace conventional boilers in domestic applications, as discussed in Section 1.

Since the share of renewable energy is continually increasing, especially from intermittent sources such as sun or wind, small CHP units find an opportunity for compensating production fluctuations by flexible energy generation. With buildings currently accounting for roughly $40 \%$ of Europe's energy consumption [83], the role of micro CHP based on flexible gas turbine technology is expected to be very beneficial for a smarter energy management, increasing the penetration of renewables, and reducing power transportation losses thanks to decentralized energy conversion.

However, the shift from a large, centralized plant to a fleet of distributed micro CHP engines raises a number of challenges in terms of system monitoring and diagnostics. The operators would no longer be trained for the job, but rather be consumers with no engineering experience or knowledge on engine performance; therefore, a completely automated system for diagnostics and decision-making is essential. With the increase in market penetration and, thus, in the number of engines, monitoring and corrective actions mostly need to occur at a decentralized level and leave only a supervisory role to the service engineer. Furthermore, the aim for low engine costs limits the number of sensors used, reducing the capability of traditional diagnosis approaches, which is also limited by the lack of data due to a relatively new market. In addition, manufacturing tolerances in small turbomachines are high, which calls for robust and adaptable methods. Advancements in information fusion techniques, hence, seem very promising to enable diffusion of micro gas turbines for domestic applications.

As micro CHP fleets become more important, information fusion for decision support opens possibilities not only for maintenance planning but also for grid optimization in the presence of fluctuating renewable energy resources. Reasoning systems that combine, e.g., information coming from the grid with user's preference and various measurements, bring the opportunity of having automated remote control of such units and switching from heat to power generation depending on the electricity spot price. The challenge of dealing with such a massive amount of data, including data protection, has to be addressed.

As part of the EU Horizon 2020 project "FUDIPO" (Future Directions of Production planning and Optimized energy) [84,85], the present authors are developing an integrated framework for monitoring, diagnostics, and decision-making for a fleet of micro gas turbines. The proposed framework is depicted in Figure 7, and it includes a multi-level diagnostics and decision support system. Firstly, the measurements from plant sensors are collected, and, after data assurance, a set of physics-based and data-driven models and diagnostic algorithms are used to perform fault detection, isolation, and identification. Trend analysis on sensors data is also performed, and trends are compared within the fleet to detect anomalies and to train machine learning systems for the prediction of future trends. Finally, outputs from all the diagnostic tools are fed to a BBN-based decision support system that provides a ranking of the most probable anomalies and suggests appropriate corrective actions. The non-homogeneous and probabilistic nature of input data makes BNN a suitable choice in this application. These activities are meant to run in parallel for a fleet of micro gas turbines that are distributed over a large geographical area.

Successful application of a fault detection and identification system on a micro gas turbine was achieved by integrating an adaptive model for GPA and data correction with a statistical algorithm [86]. Similarly, the diagnostic system was tested on a large unit from Siemens Industrial Turbomachinery, demonstrating the adaptability of the proposed method [87].

![img-7.jpeg](img-7.jpeg)

Figure 7. Schematic diagram of the proposed framework for micro gas turbine diagnostics and decision support.

# 7. Conclusions 

Data fusion techniques are widely used in gas turbine applications at the sensor and feature level, especially in the aeronautical field. At the decision level, the implementation of information fusion systems for diagnostics and prognostics is, however, limited. Due to the uncertain nature of sensor measurements and numerical models, probabilistic techniques such as Bayesian network and Dempster-Schafer were mostly selected so far. However, fuzzy inference appears to be promising to deal with incomplete and fuzzy information and should, hence, be further investigated for this purpose. From a comparison of different methods and techniques, it seems that the accuracy of the underlying diagnostic methods plays the greatest role. Since each diagnostic method may perform differently depending on the operating conditions or the type of fault, the selection of weights for the fusion system is a complex task, not always possible with a priori knowledge. Although complex decision support structures integrating historical information were theorized in the 1990s, real-world implementations of such multi-layer fusion systems are not numerous.

The challenges relate to contradictory event classifications, incomplete information, and heterogeneous data. Future work has to be devoted to a quantitative and qualitative comparison of various existing methods, addressing the challenges, and demonstrating real-world application. Small and micro-scale gas turbines represent one application in particular that could benefit significantly from the enhancement in automated diagnostics and decision-making brought by information fusion approaches. Research in that direction is needed to address the challenges related to large fleets of small, reduced-cost units and to increase the use of micro gas turbines for decentralized, domestic applications.

Author Contributions: Conceptualization, V.Z.; formal analysis and investigation, V.Z. and M.R.; resources, V.Z., M.R., and I.A.; data curation, V.Z. and M.R.; writing-original draft preparation, V.Z., I.A., and M.R.; writing-review and editing, K.K.; supervision, K.K.
Funding: This research was partially funded by the European Commission under the Horizon 2020 project FUDIPO and partially by the Swedish Knowledge Foundation under the project DIAGNOSIS.
Acknowledgments: The authors kindly acknowledge Esin Iplik and Amare Fentaye for their advice during manuscript preparation.
Conflicts of Interest: The authors declare no conflicts of interest.


# Nomenclature 

