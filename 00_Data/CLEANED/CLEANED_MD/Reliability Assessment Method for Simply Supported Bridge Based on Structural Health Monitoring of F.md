# Article 

## Reliability Assessment Method for Simply Supported Bridge Based on Structural Health Monitoring of Frequency with Temperature and Humidity Effect Eliminated

Xin He ${ }^{1,2}$ (D), Guojin Tan ${ }^{1, *}$ (D), Wenchao Chu ${ }^{3}$, Sufeng Zhang ${ }^{4}$ and Xueliang Wei ${ }^{5}$

## check for updates

Citation: He, X.; Tan, G.; Chu, W.; Zhang, S.; Wei, X. Reliability Assessment Method for Simply Supported Bridge Based on Structural Health Monitoring of Frequency with Temperature and Humidity Effect Eliminated. Sustainability 2022, 14, 9600. https:// doi.org/10.3390/su14159600

Academic Editors: Yang Liu, Hongye Gou and Wanshui Han

Received: 18 July 2022
Accepted: 2 August 2022
Published: 4 August 2022
Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## 0

Copyright: (c) 2022 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 College of Transportation, Jilin University, Changchun 130025, China
2 College of Construction Engineering, Jilin University, Changchun 130025, China
3 China State Construction Railway Investment \& Engineering Group Co., Ltd., Beijing 100053, China
4 Heilongjiang Highway Construction Center, Harbin 150081, China
5 No. 3 Engineering Company Ltd. of CCCC First Harbor Engineering Company, Dalian 116083, China

* Correspondence: tgj@jlu.edu.cn

Abstract: Structural health monitoring (SHM) has been widely used for the performance assessment of bridges, especially the methods based on dynamic characteristics. Meanwhile, bridge modal frequency is influenced significantly by environmental factors, such as temperature and humidity. Combined with SHM, a reliability assessment of bridges with the temperature and humidity effects eliminated is proposed. Firstly, the bridge deflection verification coefficient is adopted as the evaluation indicator for bridge condition, which is the ratio of deflection-measured value to deflection-calculated value. It is obtained from the relationship between verification coefficient and modal frequency through theoretical derivation. Secondly, a back propagation (BP) neural network is improved by using an artificial bee colony algorithm and employed as a surrogate model to eliminate the effect of temperature and humidity on frequency. Thirdly, a dynamic Bayesian network is applied to establish the reliability analysis model combined with the monitoring results, so that the probability distribution of bridge parameters is updated to improve the accuracy of the reliability analysis. Finally, a simply supported bridge is used as the case study, based on the proposed method in this work. The results indicate that the proposed method can eliminate the temperature and humidity effect on frequency precisely and effectively. With the effect of temperature and humidity on frequency eliminated, the bridge condition assessment can be evaluated accurately through the reliability analysis based on SHM and the dynamic Bayesian network.

Keywords: structural health monitoring; bridge reliability assessment; modal frequency; verification coefficient; temperature and humidity effect elimination; dynamic Bayesian network

## 1. Introduction

As a key component of the transportation network, bridges make essential contribution to social and economic development. However, with service time increasing, bridges become deteriorated under the action of vehicle load and adverse environmental factors [1]. According to the report from the Ministry of Transport of China, 76,483 highway bridges in China had structurally deficient ratings [2]. Moreover, in California, USA, structurally deficient bridges increased from $6.2 \%$ to $7 \%$ of total bridges [3]. Therefore, structural health monitoring (SHM) has been a hotspot in the research of bridge condition assessment in recent years. The accurate evaluation of a bridge's condition for the reliability and sustainability of bridge service performance, which can be carried out by SHM, is of great significance $[4,5]$.

Having benefitted from the development of sensor and communication technology, the SHM of bridges has developed rapidly, and is formed based on acoustic characteristics [6],

graphic information [7], and static response [8] as monitoring indexes. Meanwhile, the vehicle load action and external environmental factors can be obtained accurately [9,10]. The SHM based on structural modal parameters becomes the main monitoring technology due to the advantages of mature technology, higher accuracy, and continuous monitoring [11]. There are two categories of the vibration-based SHM, namely a direct type and an indirect type. The direct method is based on the accelerometer arranged on bridges to extract the dynamic parameter [12], and the indirect method is carried out through vehicle-assisted techniques [13]. The damage identification and performance evaluation of bridges are studied using SHM of modal frequency and mode shape. Lee et al. used time domain decomposition techniques from vibration-based SHM to extract mode shape [14]. Liu et al. established a baseline finite element model including material properties, spring bearing elements, and the replacement of Mindlin plate elements, which is used for real-time damage identification and SHM [15]. Li et al. proposed a new method to extract the time-dependent characteristics of the bridge with vehicles moving, and it was validated through laboratory and field tests that the proposed method evaluated the bridge condition accurately [16]. However, the above SHM technologies and methods based on dynamic performance are only effective for the identification of local damage and dynamic characteristic assessment, and they are prone to the interference of monitoring noise and external environment factors.

Among them, the influence of ambient temperature on the modal frequency is particularly significant, which affects the material and structural properties of bridges directly. Even worse, it masks the changes caused by bridge damage, and leads to the distortion of bridge performance analysis [17]. Therefore, it is very important to eliminate the effect of temperature on bridge condition assessment. Based on research about the long-term monitoring data of bridge frequency and ambient temperature, it was demonstrated that temperature had a negative correlation with frequency [18]. The influence of temperature on geometrical dimensions, boundary conditions, and the elastic modulus of a bridge was analyzed through experimental analysis, numerical simulation, and a neural network. The numerical relationship between structural elastic modulus and ambient temperature was clarified, and the effect mechanism of temperature on bridge modal parameters was further obtained [19-21]. On this basis, a neural network and regression analysis model were employed to establish a method to eliminate the temperature effect on modal parameters. It was obtained that a bridge frequency, with the ambient temperature effect eliminated, made an accurate assessment of the bridge condition [22-24]. Nevertheless, the methods mentioned above are mainly based on numerical model and monitoring data, of which the elimination precision is easily affected by the model error and the humidity effect is not taken into consideration. There is a certain difference between the bridge internal temperature and the ambient temperature. If the internal temperature influence is considered, the elimination precision will be improved.

As one of the main methods for bridge condition assessment, reliability theory has been widely used to evaluate the safety and serviceability of bridges [25-28]. When combined with the SHM data of deflection, strain, stress, and so on, it can predict the time-dependent reliability and residual life of a bridge [29-36]. As the most widely used parameter in SHM, modal frequency is usually adopted to reflect the dynamic characteristics and to identify structural damage. If the relationship between frequency and bridge safety is obtained, bridge frequency can be employed as a structural safety indicator to estimate bridge reliability. However, there is little research literature in this field. Some researchers take advantage of modal theory to establish the safety reliability assessment method with frequency monitoring data. Liu et al. proposed the bridge deflection calculation through modal flexibility theory, which was combined with the mode shape and modal frequency monitoring data. For the monitored bridge, the time-dependent reliability was evaluated and analyzed by the proposed method [37]. Kaloop et al. implemented frequency domain decomposition to estimate the bridge mode shapes and damping ratios and examined the bridge performance reliability through Markov Chain Monte Carlo [38]. Jamali et al. addressed the safety issues on an aging bridge by proposing a multi-tier assessment

procedure, which was established through SHM techniques and probabilistic approaches. The first four frequencies of a box-girder bridge were obtained by modal test, and the bridge reliability was analyzed in part through a destructive experiment [39]. Meanwhile, the Bayesian network can be adopted to propose the relationship among multiple SHM parameters. In some references, it was combined with SHM and reliability theory to make an accurate and comprehensive assessment for bridges [36,39,40]. However, the above studies do not take into account the influence of temperature and humidity on reliability analysis based on SHM. If the influence of temperature and humidity is eliminated, the condition estimation for bridge service will be more effective and accurate.

As an important transportation infrastructure, medium- and small-span bridges account for the largest proportion out of all kinds of bridges. They are widely used across the world, notably under the adverse influence of vehicular and environmental factors. Moreover, the condition assessment for a bridge is restricted by the influence of temperature on bridge frequency SHM. To overcome this drawback, a bridge reliability assessment method based on bridge frequency SHM with the temperature and humidity effect eliminated is proposed in this paper that. The verification coefficient of bridge deflection, namely the ratio of deflection-measured value to deflection-calculated value, is employed as the reliability evaluation indicator for reliability analysis. The verification coefficient calculation method based on frequency SHM is established through the theoretical derivation of bridge deflection and modal frequency. Combined with the frequency, temperature, and humidity SHM data, the BP neural network is used as a surrogate model to predict the bridge frequency. The hidden layer neurons number, network weight, and threshold of BP neural network is optimized through an artificial bee colony algorithm. A temperature and humidity effect on frequency elimination method is proposed based on the frequency measured, predicted, and expected values. The relationship between the verification coefficient and the SHM data is analyzed through the dynamic Bayesian network, and the posterior probability distribution of the monitoring data is also obtained. Finally, the bridge reliability is calculated and analyzed using a Monte Carlo method. A simply supported bridge was built and monitored to verify the correctness and effectiveness of the proposed method.

# 2. Basic Theory of Verification Coefficient 

### 2.1. Verification Coefficient of Deflection

The mid-span deflection of the simply supported beam bridge can be obtained through Equation (1).

$$
f=\frac{F l^{3}}{48 E 1}
$$

According to the Chinese specification [41], the verification coefficient of deflection is defined as Equation (2), and the verification coefficient is dimensionless.

$$
\eta_{f}=\frac{f_{\text {test }}}{f_{0}}
$$

where $f_{0}$ and $f_{\text {test }}$ are the theoretical and measured deflection values (m) of simply supported bridges, respectively, and the theoretical deflection is computed based on Equation (1).

$$
f_{0}=\frac{F l_{0}^{3}}{48 E_{0} I_{0}}
$$

where $I_{0}$ is the design calculation span (m) of bridge, $E_{0}$ is the theoretical value of elastic modulus (Pa), $I_{0}$ is the theoretical value of the bending moment of inertia $\left(\mathrm{m}^{4}\right)$.

Based on the field test, the measured value $f_{\text {test }}$ can be expressed as Equation (4).

$$
f_{\text {test }}=\frac{F l_{1}^{3}}{48 E_{1} I_{1}}
$$

where $l_{1}, E_{1}$, and $I_{1}$ are the measured values of calculation span (m), elastic modulus (Pa), and the bending moment of inertia $\left(\mathrm{m}^{4}\right)$, respectively.

Substituting Equations (3) and (4) into Equation (2), the relationship between the deflection verification coefficient, span, and flexural stiffness is expressed as Equation (5).

$$
\eta_{f}=\frac{l_{1}^{3} E_{0} I_{0}}{l_{0}^{3} E_{1} I_{1}}
$$

It is worth noting that the bridge deflection is proportional to the external force and obeys the superposition principle within the range of elastic deformation [36]. In this study, the simply supported bridge with a single load located at the mid-span section is taken as an example. According to the superposition principle, the deflection verification coefficient calculation method is still applicable for the condition of arbitrary loads imposed on any position of the bridge. In other words, it is suitable for actual bridge engineering.

# 2.2. Verification Coefficient of Frequency 

The frequency calculation equation of a simply supported bridge is defined in Equation (6).

$$
F r e_{n}=\frac{n^{2} \pi}{2 l^{2}} \cdot \sqrt{\frac{E I}{m}}
$$

where $F r e_{n}$ is $n$th modal frequency $(\mathrm{Hz}), \mathrm{m}$ is the mass per unit length $(\mathrm{kg} / \mathrm{m})$ of the simply supported beam bridge.

The frequency verification coefficient of the simply supported bridge is expressed as Equation (7).

$$
\eta_{F r e}=\frac{F r e_{t e s t}}{F r e_{0}}=\frac{F r e_{t e s t}}{\frac{n^{2} \pi}{2 l_{0}^{2}} \cdot \sqrt{\frac{E_{0} I_{0}}{m_{0}}}}
$$

where $\eta_{F r e}$ is the frequency verification coefficient, which is dimensionless; $F r e_{0}$ and $F r e_{\text {test }}$ are the calculated and measured frequencies $(\mathrm{Hz})$ of simply supported bridges, respectively; $m_{0}$ is the theoretical value of mass per unit length $(\mathrm{kg} / \mathrm{m})$.

With the calculation span, mass, and flexural stiffness obtained through field test, the measured frequency of the bridge can be calculated according to Equation (8).

$$
\text { Fre }_{\text {test }}=\frac{n^{2} \pi}{2 l_{1}^{2}} \cdot \sqrt{\frac{E_{1} I_{1}}{m_{1}}}
$$

The frequency verification coefficient can be given by Equation (9).

$$
\eta_{F r e}=\frac{F r e_{t e s t}}{F r e_{0}}=\frac{l_{0}^{2}}{l_{1}^{2}} \sqrt{\frac{m_{0} E_{1} I_{1}}{m_{1} E_{0} I_{0}}}
$$

### 2.3. Deflection Verification Coefficient Based on Frequency

The relationship between the deflection verification coefficient and frequency verification coefficient can be obtained according to Equations (5) and (9). Therefore, the deflection verification coefficient based on frequency is expressed as Equation (10).

$$
\eta_{f}=\frac{l_{1}^{3} E_{0} I_{0}}{l_{0}^{3} E_{1} I_{1}}=\frac{m_{1} m_{0} l_{0} l_{1}^{4} E_{0} I_{0}}{m_{1} m_{0} l_{1} l_{0}^{4} E_{1} I_{1}}=\frac{m_{0} l_{0}}{m_{1} l_{1}} \cdot \frac{l_{1}^{4} m_{1} E_{0} I_{0}}{l_{0}^{4} m_{0} E_{1} I_{1}}=\frac{m_{0} l_{0}}{m_{1} l_{1}} \eta_{F r e}^{-2}=\frac{m_{0} l_{0}}{m_{1} l_{1}} \cdot\left(\frac{F r e_{t e s t}}{F r e_{0}}\right)^{-2}
$$

where $m_{0} l_{0}$ and $m_{1} l_{1}$ represent the theoretical value and the measured value of the overall mass ( kg ) of bridge structure. It is assumed that the mass change of bridge structure is little and can thus be ignored. As a result, Equation (10) is rewritten as $\eta_{f}=\eta_{F r e}^{-2}$.

# 3. Temperature and Humidity Effect Elimination 

### 3.1. BP Neural Network

The BP neural network [42] is a multilayer feedforward network, as shown in Figure 1. The learning process consists of data forward propagation and error back propagation. The measured data is imported through the input layer, processed by the hidden layer, and exported by the output layer in the forward propagation process. If the error between the output result and the expected result do not meet the requirements, the error back propagation is carried out. At the same time, the error propagates from the output layer to the input layer and modifies the weights and thresholds of each neuron. The process of data forward propagation and error back propagation continuously alternates. When the error is less than the allowable value, or if it reaches the termination condition, it stops the neural network training process. The trained network can be used for prediction based on the measured data.
![img-0.jpeg](img-0.jpeg)

Figure 1. Structure diagram of BP neural network.

### 3.2. Artificial Bee Colony Algorithm

The artificial bee colony algorithm (ABC) is an optimization algorithm that simulates the process of bee foraging to find the optimal solution, which consists of four stages: initialization stage, employed bees phase, onlooker bees phase, and scout bees phase. Compared with genetic algorithm (GA), particle swarm optimization algorithm (PSO), and other swarm intelligence optimization algorithms, the ABC algorithm has the advantages of simple structure, a strong ability to search for global optimal solutions, and is easy to implement [43,44]. The main steps of the ABC algorithm are summarized as follows:
(1) Initialization phase

Firstly, the initial food source is generated according to Equation (11), and then the adaptive value is calculated through Equation (12) to evaluate the quality of the food source.

$$
\theta_{i j}=l b_{j}+\left(u b_{j}-l b_{j}\right) \cdot \operatorname{rand}(0,1)
$$

where $\theta_{i j}$ is the $j$ th parameter of the $i$ th solution; $l b_{j}$ and $u b_{j}$ are the lower and upper bounds of the $j$ th parameter, respectively; $\operatorname{rand}(0,1)$ represents a randomly generated real number between 0 and 1 .

$$
f i t_{i}=\left\{\begin{array}{cc}
\frac{1}{1+f\left(\theta_{i}\right)} & \text { if } f\left(\theta_{i}\right) \geq 0 \\
1+a b s\left(f\left(\theta_{i}\right)\right) & \text { otherwise }
\end{array},\right.
$$

where $f i t_{i}$ is the fitness of the $i$ th solution; $f\left(\theta_{i}\right)$ is the target function value of the food source $\theta_{i}$.
(2) Employed bees phase

The employed bee will search for nearby food sources, and the forger bee corresponding to the $i$ th food source selects a new food source according to Equation (13) and retains a better solution according to the greedy selection mechanism.

$$
v_{i j}=\theta_{i j}+\psi_{i j} \cdot\left(\theta_{i j}-\theta_{k j}\right)
$$

where $v_{i j}$ is the $j$ th parameter corresponding to the $i$ th new solution; $\theta_{i j}$ is a randomly selected food source, $k \neq i ; \psi_{i j}$ is random number on interval $[-1,1]$.
(3) Onlooker bees phase

The employed bees share the information of the food source with the onlooker bees after returning to the nest, and the onlooker bees select the food source according to the probability obtained by Equation (14). The best food source will be further exploited and utilized by the onlooker bees.

$$
p_{i}=\frac{f i t_{i}}{\sum_{j=1}^{C N} f i t_{j}}
$$

(4) Scout bees phase

If the exploitation number of a food source is more than the control parameter, it indicates that the food source is exhausted. The employed bees will be converted to scout bees and start to search for food sources randomly. The scout bee will turn back to the employed bee when it discovers a new food source, and the counter is reset to 0 . The algorithm repeats from Step 2 to Step 4 until the termination condition is satisfied.

# 3.3. BP Neural Network Optimized by ABC Algorithm 

The fitting accuracy of the BP neural network is mainly influenced by the number of hidden layer neurons, network weight, threshold, and other parameters. The BP neural network model in this paper is constructed with the bridge internal temperature, environmental temperature, and humidity as the input parameters and the modal frequency as the output parameter. The fitting function of the ABC algorithm is the Euclidean distance between the frequency predicted by the BP neural network and the frequency SHM data. The frequency SHM data cover the first three order frequencies. Therefore, three BP neural networks for the first three frequencies in this work are established. The parameters of the BP neural network are regarded as the food source in the ABC algorithm. The quality of the food source is determined by the fitting function. Through the employed bees phase, onlooker bees phase, and scout bees phase, the best combination of the parameter of the BP neural network can be obtained. Considering the efficiency and accuracy of the optimization process, the population size, iteration times, and exploitation limit of the ABC algorithm, and the upper and lower bounds of the parameters, are determined according to reference [36]. When the parameters' combination of neurons number, network weight, and threshold are optimized by the ABC algorithm, the BP neural network model with the best accuracy can be obtained. The calculation flow of the BP neural network optimized by the ABC algorithm is shown in Figure 2.

![img-1.jpeg](img-1.jpeg)

Figure 2. Flow chart of BP neural network model optimized by ABC algorithm.

# 3.4. Temperature and Humidity Effect Elimination of Bridge Modal Frequency 

The optimized BP neural network model is used to analyze the temperature and humidity effect on bridge frequency. The difference between the predicted frequency and the measured frequency at the reference temperature is taken as the temperature and humidity effect, which is eliminated from the measured frequency to obtain the modal frequency without the effect of temperature and humidity. It is defined as Equation (15) [45].

$$
f_{q}=f_{m}-\left[f_{p}-f_{e}\right]
$$

where $f_{q}$ is modal frequency $(\mathrm{Hz})$ with temperature effect eliminated; $f_{m}$ is the measured frequency value $(\mathrm{Hz}) ; f_{p}$ is the frequency value $(\mathrm{Hz})$ predicted by the optimized BP neural network model; $f_{e}$ is the expected value $(\mathrm{Hz})$ of bridge modal frequency.

In addition, the prediction capacity of the BP neural network is related to the amount of frequency SHM data. As for the SHM of the actual bridge, it can provide a sufficient measured data, which can improve the prediction accuracy of the BP neural network optimized by the ABC algorithm. Therefore, the effect of temperature and humidity on frequency can be eliminated effectively for actual bridge engineering.

## 4. Dynamic Bayesian Network Model

Based on the dynamic Bayesian network, the posterior distribution of bridge frequency with the temperature and humidity effect eliminated is shown as Equation (16).

$$
f\left(\operatorname{Fre}_{U N} \mid \mathbf{X}\right)=\frac{L\left(\mathbf{X} \mid \operatorname{Fre}_{U N}\right) \pi\left(\operatorname{Fre}_{U N}\right)}{\int_{\Omega} L\left(\mathbf{X} \mid \operatorname{Fre}_{U N}\right) d \operatorname{Fre}_{U N}}
$$

where $\mathbf{X}=\left[X_{F r e}, X_{T e m}, X_{H u m}, X_{P C 1}, X_{P C 2}, X_{P C 3}\right]^{T}$ represents the SHM data of the frequency, environmental temperature, humidity, and the internal temperature principal components; $L\left(\mathbf{X} \mid \operatorname{Fre}_{U N}\right)$ is likelihood function; $\pi\left(\operatorname{Fre}_{U N}\right)$ is the prior distribution of modal frequency with the effect of factors eliminated; $\Omega$ is the parameter space of $F r e_{U N}$.

Equation (16) can be expressed by a statistical model, which is composed of response variables, explanatory variables, and likelihood relations. Thus, it is shown as Equation (17).

$$
\operatorname{Fre}_{U N} \mid \mathbf{X} \sim N\left(\mu_{F r e_{U N}}, \nu_{F r e_{U N}}\right)
$$

where $F r e_{U N}$ is the response variable; $\mathbf{X}$ is the explanatory variable as the non-statistical part. This paper assumes that the response variable $F r e_{U N}$ obeys a normal distribution of expected value $\mu_{F r e_{U N}}$ and standard deviation $\nu_{F r e_{U N}}$ [36].

Generally, likelihood relation can be defined as a generalized linear model and nonlinear model [36,46], while the generalized linear model has a simple structure and high applicability. Therefore, the linear model is adopted in this paper to establish the linear regression model, with response variables and explanatory variables given. The mean value of this model is equal to the expected value of the posterior distribution, therefore it can be obtained as Equation (18).

$$
E\left(\operatorname{Fre}_{U N} \mid \mathbf{X}\right)=\mu_{F r e_{U N}}=\beta_{0}+\boldsymbol{\beta} \mathbf{X}
$$

where $\beta_{0}$ is the constant coefficient of the regression model; $\boldsymbol{\beta}=\left[\beta_{\text {Fre }}, \beta_{\text {Tem }}, \beta_{\text {Hum }}, \beta_{\text {PC1 }}, \beta_{\text {PC2 }}, \beta_{\text {PC3 }}\right]$ represents regression parameters corresponding to each explanatory variable.

In addition to the relationship between the various SHM parameters of the bridge, the SHM parameters also possess time property. The linear model mentioned above is no longer applicable. However, the dynamic Bayesian network model can effectively solve such problems, which is a directed acyclic graph (DAG). The nodes of the DAG represent variables, and arrows represent the relationships between variables. The static simplified model among variables in this paper is shown in Figure 3, where circular nodes and rectangular nodes represent random variables and SHM data, respectively.
![img-2.jpeg](img-2.jpeg)

Figure 3. The Bayesian network model for bridge frequency analysis with temperature and humidity eliminated.

In order to analyze the dynamic Bayesian network model, the relationship between variables and time-dependent characteristics should first be simplified. This kind of model satisfies the characteristics of the Markov chain. Therefore, it can be assumed that the probability distribution of any time slice $t$ is only related to the adjacent previous time slice $t-1$. The conditional probabilities of adjacent moments are homogeneous, and the transition probability $P\left(\mathbf{S}_{t+1} \mid \mathbf{S}_{t}\right)$ does not depend on time $t$. In addition, the dynamic

Bayesian network can be divided into prior network $N_{0}$ and transfer network $N_{\rightarrow}$. As a result, the joint probability of all time slices can be expressed as Equation (19).

$$
P\left(S_{0}, S_{1}, \cdots, S_{T}\right)=P_{N_{0}}\left(S_{0}\right) \prod_{t=0}^{T} P_{N \rightarrow}\left(S_{t+1} \mid S_{t}\right)
$$

where $S_{t}=\left[V_{1, t}, V_{2, t}, \cdots V_{n, t}\right]$ is the set of variables in time slice $t$.
Then, the joint probability of any node in the dynamic Bayesian network model is shown as Equation (20).

$$
P\left(X_{1: n, 0: T}\right)=\prod_{t=1}^{n} P_{N_{0}}\left(V_{i, 0} \mid P a\left(V_{i, 0}\right)\right) \prod_{t=1}^{T} \prod_{i=1}^{n} P_{N \rightarrow}\left(V_{i, t} \mid P a\left(V_{i, t}\right)\right)
$$

where $P a\left(V_{i, t}\right)$ represents the father node of the $i$ th variable at time $t$.
The node VerCo is calculated by Equation (10) according to the result of node $\operatorname{Fre}_{1,1 N}$. Therefore, the dynamic Bayesian network model of the bridge verification coefficient based on SHM is shown in Figure 4. WinBUGS software is employed in this paper to calculate and analyze the dynamic Bayesian network model.
![img-3.jpeg](img-3.jpeg)

Figure 4. The dynamic Bayesian network for bridge verification coefficient based on SHM data.

# 5. Experimental Test 

### 5.1. Simply Supported Bridge

In this paper, a simply supported bridge was established in the laboratory as the research object (as shown in Figure 5). The bridge is 4 m long, the calculated span is 3.7 m long, and the cross-section is a rectangle with a width of 0.6 m and a height of 0.15 m . Portland cement of grade 42.5, river sand with fineness modulus of 2.7, and aggregate with maximum nominal size of 31.5 mm were used for bridge construction. The mix proportions are illustrated in Table 1. There are $6 \times \Phi 12$ steel reinforcements longitudinally arranged in the beam, and the concrete cover thickness is 4 mm . The beam is simply supported on concrete piers by plate rubber supports. The deflection verification coefficient of the simply supported bridge was obtained through the static load test. The load level of the static load test was divided into four grades, namely if the load $P$ equals $0.5 \mathrm{kN}, 1.0 \mathrm{kN}, 1.5 \mathrm{kN}$, and 2.0 kN , respectively. The deflection at the midspan of four load conditions was measured by the dial gage.
![img-4.jpeg](img-4.jpeg)

Figure 5. The simply supported bridge.
Table 1. Mix proportions of the bridge.


### 5.2. Structural Health Monitoring System

### 5.2.1. Modal Frequency Monitoring System

In this paper, a DH5922 dynamic signal test and analysis system (as shown in Figure 6) manufactured by Donghua Testing Technology Co., Ltd. was used to monitor the modal frequency of the bridge. The test system includes a signal analysis system, DH131E acceleration sensor, and an impulse hammer with a piezoelectric force sensor. The acceleration sensor has the advantages of small size ( $\Phi 10 \times 16 \mathrm{~mm}$ ), light weight ( 5.5 g ), and large test range ( $1 \mathrm{~Hz}-8000 \mathrm{~Hz}$ ). The force hammer pressure test range is $0 \mathrm{kN} \sim 60 \mathrm{kN}$. The sensor and force hammer can withstand an operating temperature of $-40^{\circ} \mathrm{C}$ to $80^{\circ} \mathrm{C}$ and meet the field experimental environmental conditions. The dynamic test system includes two modal analysis test modes, which are force measurement method and no-force measurement method. Because the force-measured method possesses better performance and accuracy,

it was used to collect and analyze the modal frequency to validate the effectiveness and accuracy of the verification coefficient method proposed in this study. Through the Modal Analysis Module in the DH5922 dynamic signal test and analysis system, it can measure the frequency more accurately, of which the frequency resolution was 0.001 Hz .
![img-5.jpeg](img-5.jpeg)
(c)

Figure 6. Bridge dynamic characteristic monitoring system: (a) accelerometer; (b) hammer; (c) DH5922 type dynamic test system.

Due to the complex testing process of the force-measured method, it is not suitable for the SHM of bridge frequency. The spectral analysis was employed for the frequency SHM, which was excited by rubber hammer. The accelerometer was used to monitor vibration. The sampling frequency was set as 5120 Hz . The rectangular window was used, and the frequency resolution was 0.156 Hz . The bridge frequencies were calculated and extracted by frequency spectral analysis using fast Fourier transform. The monitoring test was carried out from October 2015 to September 2016, and the modal test was performed to measure the bridge frequencies every two hours from 8:00 a.m. to 10:00 p.m. on every day of monitoring.

# 5.2.2. Temperature and Humidity Monitoring System 

The temperature and humidity monitoring system manufactured by Shenzhen TOPRIE Electronics Co., Ltd. (Shenzhen, China) Was used to monitor the ambient temperature and humidity of the bridge and the bridge's internal temperature. The system is composed of a TP-2307 digital temperature and humidity sensor and a TP700 multi-channel data recorder

with a temperature and humidity input module, as shown in Figure 7a,b. The temperature measurement ranges of the temperature and humidity sensor are $-40^{\circ} \mathrm{C} \sim 125^{\circ} \mathrm{C}$ and $0 \%$ to $99 \%$, respectively. The temperature resolution is $0.3^{\circ} \mathrm{C}$, and the humidity resolution is $0.3 \%$.
![img-6.jpeg](img-6.jpeg)

Figure 7. Temperature and humidity monitoring system: (a) temperature and humidity recorder; (b) temperature and humidity sensor; (c) layout of temperature-monitoring sensors inside the bridge.

Omega T-type thermocouple was used to test the internal temperature of the bridge. The two poles of the Omega T-type thermocouple are composed of copper-constantan. According to the Seebeck effect, the temperature of the measuring point was measured through the thermoelectric electromotive generated in the circuit. The temperature measurement range omega T-type thermocouple is $-250^{\circ} \mathrm{C}$ to $260^{\circ} \mathrm{C}$. Next, 38 measuring points were arranged at the midspan cross-section of the bridge, and one thermocouple was buried at each measuring point. The layout is shown in Figure 7b.

# 6. Results and Discussion 

### 6.1. Validation of Bridge Verification Coefficient Based on Modal Frequency

The deflection values of the mid-span section of the simply supported bridge and the first three modal frequencies were obtained through static and dynamic load tests. The temperature and humidity of the field test condition were $13.3^{\circ} \mathrm{C}$ and $33.7 \%$. The results were used to verify the effectiveness and accuracy of the method proposed in this paper, which is used for calculating the bridge verification coefficient based on modal frequency, and the bridge deflections and frequencies were measured for four times to reduce the influence of a test error. Then, the corresponding theoretical values were obtained through

a finite element model established by ANSYS software. The theoretical values and actual test results are shown in Tables 2 and 3.

Table 2. The theoretical values and measured values of deflections.


Table 3. The theoretical values and measured values of the first three order frequencies.


The mean values and theoretical values of the measured data were substituted into Equation (2) to calculate the deflection verification coefficients of the simply supported bridge, and the deflection verification coefficients based on modal frequencies were calculated according to Equation (10). The calculation results are shown in Figure 8.
![img-7.jpeg](img-7.jpeg)

Figure 8. The deflection verification coefficients of the simply supported bridge.
It can be seen from Table 2 that the COVs of the measured deflections of the bridge are between 0.03 and 0.1 , which indicates that the static load test can provide accurate deflection values. The measured data in Table 3 were extracted and obtained through the Modal Analysis Module in the DH5922 system. The frequency resolution of this method is 0.001 Hz , and it can measure the bridge frequencies more accurately. However, the test process is influenced by the electrical interference and human factor, which leads to frequency variation between tests, and the modal test was controlled strictly in this study to reduce the error caused by the adverse factors. The COVs of the measured frequencies in Table 3 do not exceed 0.01, which demonstrates that the dynamic test has higher accuracy and reliability. In Figure 8, the results of the deflection verification coefficient calculated by the two methods are between 0.838 and 0.87 , and the maximum

relative error is $3.82 \%$. This verifies the effectiveness and accuracy of the bridge deflection verification coefficient calculation method based on modal frequency. It proves that the first three modal frequencies can be used to calculate the bridge deflection verification coefficient. With an increase in static load, the deflection verification coefficients increase slightly. With an increase in modal frequency orders, the deflection verification coefficients calculated by the method proposed in this paper decrease from 0.87 to 0.859 .

# 6.2. Bridge Frequency with the Effect of Temperature and Humidity Eliminated 

The temperature data of 38 measuring points inside the bridge were obtained from the structural health monitoring system established in this paper. Due to the high correlations between the internal temperature data, there will be unstable fitting parameter estimations in the temperature effect elimination and dynamic Bayesian network analysis. The principal component analysis method was used to process the temperature-monitoring data inside the bridge. The principal analysis is an approach for linear data visualization and reduction. The principal components obtained by the principal component analysis method are numerical and contain most of the information of the original data and describe the maximum and minimum variability in the data set [47]. Moreover, the obtained temperature principal components can improve the generalization performance of the fitting model, avoiding the over-fitting phenomenon caused by information overlap. The principal component analysis was mainly calculated and analyzed according to Equations (21) and (22):

$$
\boldsymbol{Y}=\boldsymbol{\Psi}^{T} \boldsymbol{X}=\left[y_{1}, y_{2}, \cdots, y_{n}\right]^{T}
$$

where $\boldsymbol{Y}$ is principal component vector; $\boldsymbol{X}$ is the original data vector; $\boldsymbol{\Psi}^{T}$ is orthogonal transformation matrix, namely $\boldsymbol{\Psi}^{T}=\boldsymbol{\Psi}^{-1}$. Through the singular value decomposition of the covariance matrix of $\boldsymbol{X}$, it can be expressed as Equation (22).

$$
\Lambda=\operatorname{diag}\left(\lambda_{1}, \lambda_{2}, \cdots, \lambda_{n}\right)
$$

where $\boldsymbol{\Lambda}$ is a diagonal matrix composed of $n$ eigenvalues; the eigenvalues satisfy $\lambda_{1} \geq \lambda_{2} \geq \cdots \geq \lambda_{n} \geq 0 ; \lambda_{i}$ is the contribution rate of the $i$ th principal component. The selected principal component must meet the condition that the cumulative contribution rate is more than $85 \%$.

The cumulative contribution rates of the principal components of the bridge's internal temperature are shown in Figure 9. The contribution rate of the first principal component is $97.12 \%$, which indicates that the temperature data obtained from the test have a significant correlation. Moreover, the cumulative contribution rate of the first three principal components is $99.8 \%$, therefore it can fully characterize the information of the original internal temperature-monitoring data. The essence of the first three components is the reconstruction of the original temperature-monitoring data, which cover the monitoring data information with a smaller data size. Therefore, the first three principal components were used for analysis in the BP neural network and the dynamic Bayesian network model.

The environment temperature, humidity, and the first three principal components of bridge internal temperature were taken as the input parameters of the BP neural network model. The first three order frequencies of the SHM data of the simply supported bridge were taken as the output parameters. A total of 521 groups of monitoring data were collected by the SHM system, in which the first 417 groups of data were used as training samples and the last 104 groups of data were used as test samples. The monitoring process lasted from October 2015 to September 2016, and the modal frequency, temperature, and humidity monitoring test was preformed every two hours from 8:00 a.m. to 10:00 p.m. for every day of monitoring. The duration of a single monitoring process was 15 min . According to the temperature-monitoring data, the change of the internal temperature lags behind that of the environment temperature. Before 2:00 p.m., the environment temperature is greater than the internal temperature by about $1^{\circ} \mathrm{C}$ to $4^{\circ} \mathrm{C}$. After 2:00 p.m., the environment temperature is less than the internal temperature by about $1^{\circ} \mathrm{C}$ to $6^{\circ} \mathrm{C}$.

The BP neural network model used in this paper has a three-layer structure, including an input layer, hidden layer, and output layer. According to the process shown in Figure 1, the bridge frequencies under the influence of temperature and humidity were fitted and predicted. The population size, iteration times, and exploitation limit of the ABC algorithm were set to 30,300 , and 150 , respectively. Finally, the parameters' combination of the hidden layer neurons number, inter layer weights, thresholds, and other parameters in the BP neural network were optimized by the ABC algorithm. The fitting error results of the optimized BP neural network are shown in Figure 10.
![img-8.jpeg](img-8.jpeg)

Figure 9. Cumulative contribution rate of principal components of bridge internal temperaturemonitoring data.
![img-9.jpeg](img-9.jpeg)

Figure 10. The relationships between the fitting error and the number of hidden layer neurons.
It can be seen from Figure 10 that the fitting errors of the first three frequencies of the bridge decrease gradually with an increase in the hidden layer neurons number. When the number of neurons is 7 , the fitting error of the first order frequency reaches the minimum value. Then, the fitting error fluctuates slightly with an increase in the neurons number, and the minimum values of the fitting errors of the second and third order frequencies occur when the number of neurons in the hidden layer is 6 . Therefore, the number of hidden layer neurons in the BP neural network models, for the first three order frequencies in the monitoring data, were set to 7,6 , and 6 , and the optimized BP neural network model was established according to the optimal combination of layer weights, thresholds, and other parameters determined by the ABC algorithm. The predicted value, expected value, and monitored value of the SHM data were substituted into Equation (15) to calculate the first three frequencies of the simply supported slab bridge, eliminating the influence of temperature and humidity, as shown in Figure 11.

![img-10.jpeg](img-10.jpeg)

Figure 11. Bridge frequencies excluding the influence of temperature and humidity: (a) first order frequency; (b) second order frequency; (c) third order frequency; (d) monitoring data of ambient temperature; (e) monitoring data of ambient humidity.

As shown in Figure 11, the monitoring temperature minimum and maximum values are in time slice 4 and time slice 10, respectively. At the same time, the corresponding frequency monitoring values are maximum and minimum, respectively. The overall change trend shows that the bridge frequency monitoring data has a negative correlation with the temperature. However, the monitoring humidity has little impact on the frequency change trend. The predicted value of the bridge frequencies is consistent with the monitored values, which shows that the BP neural network optimized by the ABC algorithm can accurately predict the bridge frequency. The frequencies with the effect of temperature and humidity eliminated will no longer vary with the change of temperature, which is closer to the expected value. Due to the influence of the test errors, human factors, and other

interference factors, the frequencies with the effect of temperature and humidity eliminated fluctuate slightly around the expected value.

# 6.3. Dynamic Bayesian Network Analysis 

Using the dynamic Bayesian network established above, the uncertainty of SHM data and bridge frequency with the effect of temperature and humidity eliminated were analyzed. The relationship between the monitoring variables was established through Equation (18). In this study, the SHM of the bridge was carried out from October 2015 to September 2016. The SHM data in a month were analyzed and used for a time slice of dynamic Bayesian network, and the time slice 1 to the time slice 12 corresponded to October 2015 to September 2016, respectively. According to the characteristics of the monitoring data parameters [48], this paper assumed that the regression coefficient $\beta$ and the mean value of the bridge frequency with the effect of temperature and humidity eliminated obey the normal distribution and that the standard deviation variable $v$ obeys the gamma distribution. For time slice 1, it was regarded as non-prior information, and the prior distribution mean and standard deviation of each variable are 0 and $10^{4}$, so as to reduce the influence of prior information. The WinBUGS software was adopted to calculate the posterior distribution of the first three frequencies eliminating the effect of temperature and humidity. A part of the posterior information results is shown in Table 4.

Table 4. Posterior distribution information of the dynamic Bayesian network.


The Markov chain error of each variable in the dynamic Bayesian network is less than $1 / 20$ of the posterior standard deviation, which indicates that the dynamic Bayesian network model is convergent and has a high accuracy [36]. Through the K-S hypothesis test, it demonstrated that the posterior distribution of each variable was the same as the prior distribution. It can be seen from Table 4 that, except for the constant term coefficient $\beta_{0}$ and the second principal component coefficient of internal temperature $\beta_{P C 2}$, other regression coefficients have small standard deviations. Thus, the relationships between the first three order modal frequencies with the effect of temperature and humidity eliminated and the SHM parameters are expressed from Equation (23) to Equation (25).

$$
\begin{aligned}
\operatorname{FreUN}_{1,1} & =34.51-0.825 X_{\text {Fre }}-0.0093 X_{\text {Tem }}+0.0021 X_{\text {Hum }} \\
& -0.0995 X_{P C 1}+2.785 X_{P C 2}-0.2917 X_{P C 3} \\
\operatorname{FreUN}_{2,1} & =146.4-0.8431 X_{\text {Fre }}-0.0526 X_{\text {Tem }}+0.0229 X_{\text {Hum }} \\
& -0.9589 X_{P C 1}-52.58 X_{P C 2}-0.9816 X_{P C 3} \\
\operatorname{FreUN}_{3,1} & =240.5-0.3431 X_{\text {Fre }}-0.1116 X_{\text {Tem }}-0.0138 X_{\text {Hum }} \\
& +0.1528 X_{P C 1}+22.83 X_{P C 2}-5.738 X_{P C 3}
\end{aligned}
$$

The fitting coefficients in each time slice have similar posterior distribution parameters, and this indicates that the change trend of environmental conditions and bridge dynamic characteristics are stable during the monitoring period. Equation (23) to Equation (25) show that the internal temperature of the bridge has the highest correlation with the frequency with the effect of temperature and humidity eliminated. The second principal component of the bridge's internal temperature has the greatest influence, and the internal temperature of the bridge will directly cause the change of the bridge frequency. The ambient temperature and humidity will also affect the bridge frequency. The influence of ambient temperature and bridge internal temperature are much greater than that of ambient humidity, which demonstrates that the change of bridge frequency is mainly affected by temperature. Therefore, a change in bridge frequency is not only related to structural performance, but also affected by environmental factors. The accuracy of bridge service condition assessment based on modal frequency will be reduced without the effect of temperature and humidity first being eliminated. According to the analysis of the dynamic Bayesian network, the probability densities of frequencies with the effects of temperature and humidity eliminated are shown in Figure 12.
![img-11.jpeg](img-11.jpeg)

Figure 12. Cont.

![img-12.jpeg](img-12.jpeg)

Figure 12. Bridge frequency probability densities eliminating the effect of temperature and humidity: (a) first order; (b) second order; (c) third order.

It can be seen from Figure 12 that the minimum mean value and maximum standard deviation of the first three frequencies are all in time slice 1. With the monitoring time increasing, the bridge frequencies eliminating the effect of temperature and humidity gradually tend to the same posterior mean value, and their standard deviations also decrease. This indicates that the uncertainty of the bridge frequency with the effect of temperature and humidity eliminated is reduced after the dynamic Bayesian network analysis of monitoring data, which is closer to the real probability distribution parameters.

# 6.4. Bridge Reliability Analysis Based on Verification Coefficient 

According to the Chinese specification [41], the deflection verification coefficient cannot be greater than 1 , otherwise the bearing capacity of the bridge will be identified a as failure. Through the calculation method of bridge deflection verification coefficient based on modal frequency in this paper, the performance function for bridge-bearing capacity evaluation can be defined as Equation (26). The reliability is calculated and analyzed by the Monte Carlo method. According to the analysis results of the dynamic Bayesian network, this paper assumes that the mean value and the standard deviation of the bridge frequency with the effect of temperature and humidity eliminated obey the normal distribution and the gamma distribution, respectively.

$$
Z=1-\eta_{F r e}^{-2}
$$

Then, the failure probability and reliability index [26] are defined as:

$$
\begin{gathered}
F P=\operatorname{Pr}(Z<0) \\
R I=-\Phi^{-1}[\operatorname{Pr}(Z<0)]
\end{gathered}
$$

According to the posterior distribution information of bridge frequency after eliminating the effect of temperature and humidity, the Monte Carlo sampling method was used to calculate Equation (28). Based on the posterior distribution of the first three order frequencies, the reliability index and failure probability of the bridge-bearing capacities before and after eliminating the effect of temperature and humidity were computed and are shown in Figure 13.

![img-13.jpeg](img-13.jpeg)

Figure 13. Reliability analysis of bridge deflection verification coefficient: (a) reliability index before eliminating the temperature and humidity effect; (b) reliability index after eliminating the temperature and humidity effect; (c) failure probability before eliminating the temperature and humidity effect; (d) failure probability after eliminating the temperature and humidity effect.

According to the results shown in Figure 13, the temperature and humidity have a significant influence on the reliability evaluation of the bridge deflection verification coefficient. There is a significant difference between the reliability index before and after eliminating the effect of temperature and humidity. In Figure 13a, the reliability index without the effect of temperature and humidity eliminated is opposite to the variation trend of temperature. From the time slice 4 to 10, the reliability index values decrease from 5.99 to -4.18 . The reliability index calculated by the first three order frequencies' SHM data possess the same variation trend. The calculation results based on the first order and the third order are basically consistent, while the reliability index based on the second order is slightly higher. In Figure 13b, the variation trends of reliabilities based on the first three frequencies are consistent after the effects of temperature and humidity are eliminated. The minimum of the reliability index appears in time slice 1. As time increases, the reliability index is gradually stable at 5.1 and fluctuates slightly. As seen from Figure 13c,d, the variation trend of the failure probability differs from the change in the reliability index. Due to the influence of non-prior information in the dynamic Bayesian network, the error of the probability distribution parameters in time slice 1 is large. Therefore, the reliability index in time slice 1 is much less than those of other time slices. With the continuous updating of monitoring data, the frequency probability distribution information after eliminating the influence is closer to the real value. The bridge-bearing capacity evaluation based on reliability theory can reflect the real condition of the structure. In this paper, the monitoring data were collected in a whole year, which was from October 2015 to September 2016. Both the reliability index and failure probability were gradually stable in time slice 9 to time slice 12, and the change of the reliability results from time slice 1 to time slice 3 was influenced by the accuracy provided after temperature and humidity effect elimination. The temperature

and humidity effect elimination method is related to the amount of monitoring data. If more monitoring data are obtained, the reliability results will converge to a point, which is the real reliability index and failure probability of the bridge. Taking the reliability index of time slice 10 as an example, the evaluation result indicates a failing grade when the temperature and humidity effects are not eliminated. If the effects are eliminated, the reliability result reveals that the bridge is safe and reliable. This verifies the effectiveness and accuracy of the method established in this paper.

# 7. Conclusions 

A verification coefficient calculation method of bridge deflection was proposed based on modal frequency. As a safety indicator, it was used to evaluate bridge condition in combination with SHM techniques and reliability theory. Considering the effect of temperature and humidity on frequency monitoring data, the temperature and humidity elimination method was established based on the BP neural network, which was improved by the ABC algorithm. The dynamic Bayesian network was adopted to analyze the probabilistic distribution information of the SHM data and the frequency with the effect of temperature and humidity eliminated. This improved the reliability assessment accuracy of the bridge's condition. The main conclusions are drawn as follows:
(1) The relationship between modal frequency and verification coefficient was obtained through theoretical derivation. Through the comparation between static test and dynamic test, it verified the verification coefficient calculation method based on modal frequency. The results demonstrated that the verification coefficient computed by the proposed method coincided with that obtained through the static test. The first three modal of frequencies can be used for deflection verification coefficient calculation;
(2) The BP neural network optimized by an artificial bee colony algorithm has high fitting precision, which is adopted for the influence of temperature and humidity on the monitoring frequency elimination method. The bridge frequency does not change with temperature and humidity; rather, it only fluctuates slightly near the expected frequency and gradually approaches the expected value;
(3) According to the results analyzed using the dynamic Bayesian network, bridge internal temperature possesses the greatest influence on the bridge frequency, and ambient temperature and humidity also clearly affect the bridge frequency. However, the change of bridge frequency is mainly influenced by temperature. With more monitoring data, the posterior information of bridge frequency demonstrated that the proposed method reduced the uncertainty of bridge frequency with the temperature and humidity effect eliminated, and showed that it is closer to the real probability distribution parameter;
(4) The bridge reliability calculation results reveal that the reliability indices have a great difference before and after the temperature and humidity effects are eliminated. When the temperature and humidity effects are eliminated, the variations of bridge reliability are independent of temperature and humidity. The bridge performance cannot be accurately estimated without the temperature and humidity effects being eliminated. The proposed method in this paper provides a new theoretical basis and technical support for bridge SHM.

Author Contributions: Conceptualization, X.H. and G.T.; Data curation, W.C. and S.Z.; Formal analysis, X.H. and X.W.; Funding acquisition, G.T. and S.Z.; Investigation, X.H., W.C. and X.W.; Methodology, X.H. and G.T.; Resources, W.C. and X.W.; Software, X.H.; Validation, G.T. and S.Z.; Writing—original draft, X.H.; Writing—review and editing, G.T. and X.W. All authors have read and agreed to the published version of the manuscript.
Funding: This research was funded by the National Natural Science Foundation of China, Grant Number: 51978309; the Key Project of Department of Transportation of Heilongjiang Province, Grant Number: 2022-1; the Transportation Innovation Development Support Project of the Department of Transportation of Jilin Province, Grant Numbers: 2021ZDGC-5 and 2020-1-3.

Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: The data presented in this study are available on request from the corresponding author.

Acknowledgments: The authors would like to thank the anonymous reviewers for their constructive suggestions and comments to improve the quality of this paper.
Conflicts of Interest: The authors declare no conflict of interest.
