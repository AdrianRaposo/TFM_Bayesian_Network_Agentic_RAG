# Article 

## Resilient Factor Graph-Based GNSS/IMU/Vision/Odo Integrated Navigation Scheme Enhanced by Noise Approximate Gaussian Estimation in Challenging Environments

Ziyue Li ${ }^{1}$, Qian Meng ${ }^{2,3, *}$, Zuliang Shen ${ }^{2,3}$, Lihui Wang ${ }^{2,3}$, Lin Li ${ }^{4}$ and Haonan Jia ${ }^{5}$ (D)<br>check for updates

Citation: Li, Z.; Meng, Q.; Shen, Z.; Wang, L.; Li, L.; Jia, H. Resilient Factor Graph-Based GNSS/IMU/Vision/ Odo Integrated Navigation Scheme Enhanced by Noise Approximate Gaussian Estimation in Challenging Environments. Remote Sens. 2024, 16, 2176. https://doi.org/10.3390/ rs16122176

Academic Editor: Michael
E. Gorbunov

Received: 30 April 2024
Revised: 9 June 2024
Accepted: 14 June 2024
Published: 15 June 2024

## (0)

Copyright: (c) 2024 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 Beijing Kunpeng Borui Technology Co., Ltd., Beijing 100096, China; Izy_work@126.com
2 School of Instrument Science and Engineering, Southeast University, Nanjing 210096, China; zuliangshen@seu.edu.cn (Z.S.); wlhseu@seu.edu.cn (L.W.)
3 Key Laboratory of Micro-Inertial Instruments and Advanced Navigation Technology, Ministry of Education, Southeast University, Nanjing 210096, China
4 China Astronaut Research and Training Center, Beijing 100094, China; linli_507@163.com
5 State Key Laboratory of Satellite Navigation System and Equipment Technology, The 54th Research Institute of China Electronics Technology Group Corporation, Shijiazhuang 050002, China; 230219409@seu.edu.cn

* Correspondence: qianmeng@seu.edu.cn


#### Abstract

The signal blockage and multipath effects of the Global Navigation Satellite System (GNSS) caused by urban canyon scenarios have brought great technical challenges to the positioning and navigation of autonomous vehicles. In this paper, an improved factor graph optimization algorithm enhanced by a resilient noise model is proposed. The measurement noise is resilient and adjusted based on an approximate Gaussian distribution-based estimation. In estimating and adjusting the noise parameters of the measurement model, the error covariance matrix of the multi-sensor fusion positioning system is dynamically optimized to improve the system accuracy. Firstly, according to the approximate Gaussian statistical property of the GNSS/odometer velocity residual sequence, the measured data are divided into an approximate Gaussian fitting region and an approximate Gaussian convergence region. Secondly, the interval is divided according to the measured data, and the corresponding variational Bayesian network and Gaussian mixture model are used to estimate the innovation online. Further, the noise covariance matrix of the adaptive factor graph-based model is dynamically optimized using the estimated noise parameters. Finally, based on low-cost inertial navigation equipment, GNSS, odometer, and vision, the algorithm is implemented and verified using a simulation platform and real-vehicle road test. The experimental results show that in a complex urban road environment, compared with the traditional factor graph fusion localization algorithm, the maximum improvement in accuracy of the proposed algorithm can reach $65.63 \%, 39.52 \%$, and $42.95 \%$ for heading, position, and velocity, respectively.


Keywords: resilient navigation; autonomous vehicles; multi-sensor fusion; approximate Gaussian estimation

## 1. Introduction

Accurate, reliable, and continuous navigation and localization are the important foundation and prerequisite for the safe operation of autonomous vehicles [1]. Localization can be further divided into absolute localization, relative localization, and simultaneous localization and mapping (SLAM) [2,3]. The Real-Time Kinematic-based Global Navigation Satellite System (RTK-GNSS) is the most widely applied localization technology for autonomous driving, but it is susceptible to interference in urban road environments [4,5]. The fusion of multi-sensor data can achieve complementary advantages and collaborative superiority to a certain extent, which is the core technology solution used to improve the perception capability of autonomous vehicles [6]. The inertial navigation system (INS)/GNSS/odometer fusion localization is the most commonly used navigation and

localization technology for autonomous vehicles in urban road environments [7]. The INSs installed on autonomous vehicles are mostly based on lost-cost inertial measurement units (IMU). However, in GNSS-denied or challenging environments, the IMU/odometer standalone navigation system struggles to maintain long-term accuracy due to error accumulation [8,9]. Owing to the good autonomy of visual navigation, the visual/map attitude matrix measurement information can decouple the IMU/odometer measurement information, improving the system observability [10]. Additionally, visual feature matching is also an effective method used to improve the accuracy of IMU/odometer localization [11]. Based on the complementary characteristics between inertial navigation, odometry, satellite navigation, and vision, the multi-sensor data fusion module estimates and compensates navigation errors online through model state estimation, which can effectively improve the performance of the navigation system.

The complex urban road environment often has a significant impact on satellite navigation, for example, when differential data are unavailable due to communication abnormalities, the working state will be downgraded from RTK to single-point positioning (SPP); the signal obstruction and multipath effects caused by challenging environments (CEs) such as dense tree canopies, tall buildings, and overpasses will further increase or even interrupt the error. The frequent switching of satellite navigation working states caused by the dynamic changes in the urban environment will bring significant measurement model noise parameter errors, thereby significantly reducing the system accuracy. The nonlinear motion of carriers in congested environments poses a severe challenge to the performances of inertial devices. Laser radar and vision systems are also highly susceptible to the influence of the physical characteristics of the urban environment, typically manifested as model mismatches characterized by faults and biases. The mutual propagation and coupling of multi-sensor errors have exacerbated the complexity of the problem, making it difficult to meet the requirements of future autonomous vehicles for positioning accuracy, integrity, and continuity [12]. To address the challenges faced by the multi-sensor fusion localization systems of autonomous vehicles, scholars from various countries have made substantial research progress in recent years, which can be mainly divided into two directions [13,14]: (1) innovative distributed multi-source heterogeneous sensor fusion architectures, such as the fusion of GNSS, INS, odometry, and vision, to improve the performance of the integrated navigation system; and (2) research on optimized data fusion algorithms, such as improved Kalman filter series and factor graph (FG) optimization, to continuously enhance the performance of the fusion localization system.

In multi-sensor fusion localization systems of autonomous vehicles, the GNSS not only provides the only absolute positioning observation, but the high-precision RTK positioning data also plays a crucial role. However, in complex urban road environments, issues such as increased GNSS errors and signal interruptions inevitably degrade the accuracy of the fusion localization system. In improving the performance of the multi-sensor fusion localization system, the adaptive optimization of the GNSS measurement noise model has always been an important research direction. On road sections where multiple satellite navigation working modes alternate, the noise parameters based on empirical values will introduce non-negligible errors to the measurement model. The measurement data noise model error is one of the main factors limiting the improvement of the multi-sensor fusion localization accuracy.

Based on the resilient Positioning, Navigation and Timing (PNT) theory, it is necessary to perform the online accurate estimation and resilient adjustment of the noise model [15]. In order to overcome the problem of the decreased accuracy of integrated navigation systems caused by noise model parameter errors in complex urban road environments, this paper proposes an adaptive factor graph (AFG) data fusion optimization model enhanced by a resilient noise model. The noise is resilient and adjusted based on the approximate Gaussian estimation algorithm to effectively improve the accuracy of the IMU/GNSS/vision/odometer fusion localization system. First, the distribution characteristics of the GNSS measurement noise model were analyzed. Then, an algorithm

for estimating the noise parameters based on the GNSS/odometer ground speed residual sequence was studied. Finally, an adaptive factor graph model enhanced by the resilient noise model was utilized to implement and test the system. The main contributions can be summarized as follows:
(1) In using the velocity data output from the odometer as the reference, the approximate Gaussian distribution characteristics of the GNSS/Odometer ground speed residual sequence are analyzed.
(2) Based on the variational Bayesian network and Gaussian mixture model (GMM), an approximate Gaussian estimation algorithm for the measurement data noise model is studied, and a resilient noise model is proposed.
(3) Based on the resilient noise model, the factor graph-based IMU/GNSS/odometer/vision fusion navigation system is implemented, and the superiority of the algorithm is verified through theoretical analyses and road tests.
The rest of this paper is organized as follows. In Section 2, related research work is introduced. In Section 3, the proposed resilient noise model based on approximate Gaussian estimation is presented in detail. In Section 4, the factor graph-based IMU/GNSS/odometer/vision integrated navigation method enhanced by the resilient noise model is studied and presented. As discussed in Section 5, the superiority of the proposed algorithm was verified through simulation platform and road tests. Finally, the contributions of this study are discussed and summarized in the Conclusion.

# 2. Related Work and Problem Statement 

Accurate and assured positioning results are crucial for safety-critical applications such as autonomous driving. However, in complex urban road environments, a single sensor struggles to achieve accurate and reliable environmental perception, and multi-source data fusion is an important research direction in the field of autonomous driving [16]. Meanwhile, the multiple localization sensors integrated in autonomous vehicles have distributed installation, asynchronous, and delayed characteristics, and the factor graph data fusion algorithm has obvious advantages. The related work is introduced in the following subsections from the aspects of factor graph data fusion algorithms and noise model optimization.

### 2.1. Multi-Source Fusion Localization Based on Factor Graph

The continuous improvement and optimization of the Kalman filter have improved the filter's performance in terms of nonlinearity, adaptability, robustness, and fault tolerance [17,18]. However, the inherent defects limit the further improvement of their performance. The factor graph optimization algorithm based on the sum-product algorithm proposed by Kschischang [19] has many advantages, such as plug-and-play and global optimization, which can effectively solve the shortcomings of the Kalman filtering algorithm. Different from the Kalman-based filters, the factor graph optimization algorithm is based on the current data and historical data, and it achieves global optimization through the construction of a batch optimization cost function.

Zeng [20] studied an improved multi-sensor data fusion algorithm based on the factor graph, which fully utilizes the sensor data with different update rates, including inertial navigation, Global Positioning System (GPS), geomagnetic, vision, and sonar data, to achieve a globally optimal estimation. The effectiveness of this algorithm was verified through a comparison with that of the extended Kalman filter (EKF), and it was also tested on a small unmanned aerial vehicle platform. Furthermore, Wen [21] researched the tightly coupled GNSS/SINS integration based on the factor graph and fisheye camera and conducted a detailed comparison of the filtering effects of the EKF and factor graph in both loosely coupled and tightly coupled cases. The impact of the sliding window size on the factor graph filtering performance was also analyzed [22]. In the field of autonomous driving, Zhao [23] designed a sliding window smoothing estimator based on the factor graph architecture and applied it to the tightly coupled Differential GPS (DGPS)/inertial

measurement unit (IMU) system on the Google self-driving car platform. Road tests in urban environments showed that this algorithm has significant advantages over the EKF, due to its global optimization, re-linearization, and multiple iterations. Gao [24] utilized the factor graph model to design a multi-source fusion localization algorithm, which effectively reduced the errors caused by the asynchrony and time delay of the sensors in the vehiclemounted INS/GNSS/odometer system. Li [25] analyzed the advantages of the graph optimization algorithm over the EKF and proposed a robust graph optimization scheme for inertial/satellite tight integration, using the GNSS reliability state variable to optimize the GNSS pseudorange residual weight, thereby improving the system accuracy in urban road environments.

# 2.2. Adaptive Optimization of Measurement Noise Model 

In complex urban road environments, autonomous vehicles face dynamic changes in navigation and positioning environments. Fixed noise parameters based on empirical values in multi-sensor fusion positioning systems inevitably introduce model errors. Conducting research on dynamic noise parameter estimation for multi-sensor data fusion models is an effective method for improving the positioning accuracy. Sarkka [26] first proposed the application of the variational Bayesian method to optimize measurement noise model parameters. In using fixed-point iterations, the noise variance distribution is statistically analyzed, improving the accuracy of the adaptive Kalman filtering. Li [27] achieved the adaptive optimization of the unscented Kalman filter (UKF) by performing a variational Bayesian approximate estimation of the model noise, improving the system's robustness. To enhance the robustness of the Strap-down Inertial Navigation System (SINS)/GPS combined navigation system in complex environments, Hu [28] used the T-distribution to simulate the noise matrix, suppressing the heavy-tailed characteristics of noise caused by outliers. The variational Bayesian network was then used to iteratively estimate the state variables.

Optimally estimating measurement noise parameters based on innovation is an effective way to improve the performance of multi-sensor fusion localization systems. To enhance the positioning accuracy of autonomous driving systems in urban roads, Liu [29] proposed an online estimation method for measurement noise parameters using estimated values and measurements. The noise covariance matrix is updated and adaptively optimized through a decay factor, which more accurately reflects the noise characteristics and achieves the effect of suppressing white noise, effectively improving the accuracy of the INS/GPS fusion localization system. Addressing the issue of the reduced filter accuracy caused by uncertain statistical characteristics of the measurement noise, Yue [30] proposed a weighted adaptive square root cubature Kalman filter (CKF). The moving window theory is used to perform a maximum likelihood estimation (MLE) on the covariance matrix of innovation, based on which the measurement noise matrix is dynamically adjusted. This effectively improves the adaptive ability and navigation performance of the GPS/INS combined navigation system in environments with uncertain measurement noise statistics. Xu [31] performed a maximum a posteriori estimation of the covariance matrix of the factor graph data fusion model based on the estimated state values and observations and iteratively updated it through dynamic weighting, effectively improving the robustness of the multi-sensor fusion localization algorithm. By analyzing the raw observations of a GNSS and accelerometers, Jing [32] constructed an adaptive measurement noise model using the a posteriori coordinate covariance of an RTK-GNSS and optimized and improved the GNSS/odometer data fusion model. The batch covariance estimation (BCE) framework iteratively updates the measurement error uncertainty model by fitting the Gaussian mixture model to the measurement residuals, thereby achieving a robust state estimation of the robot platform. Watson [33] proposed the BCE-AD method by expanding the data space to achieve a more accurate description of measurement uncertainty models.

In summary, the aforementioned research on multi-sensor fusion localization has extensively explored optimization techniques for factor graph fusion algorithms from the

perspectives of sensor schemes, data fusion architectures, and robustness. However, there are relatively few studies on the online adaptive optimization of covariance matrices. On the other hand, certain algorithms, such as variational Bayesian and maximum a posteriori algorithms, have been used to estimate system measurement information online, achieving the adaptive optimization of noise models. However, due to the lack of high-precision data with strong autonomy, the decoupling of noise model errors and measurement errors is difficult, and the accuracy needs to be further improved. Based on the advantages of odometry in terms of ground speed autonomy and accuracy, this paper proposes a noise parameter approximate Gaussian estimation method using the GNSS/odometer ground speed residual sequence as measurement information. After analyzing the distribution characteristics, the proposed method realizes an online resilient adjustment of the factor graph covariance matrix.

# 3. Approximate Gaussian Estimation of Measurement Noise Parameters Based on Innovation 

To address the issue of system accuracy degradation caused by measurement noise model errors, a resilient noise model based on approximate Gaussian estimation is proposed in this section.

### 3.1. Approximate Gaussian Distribution Analysis of GNSS/Odometry Velocity Residual Sequences

As mentioned above, the GNSS is the most widely used positioning sensor for autonomous vehicles. However, it is also the most susceptible to interference in urban road environments, which can negatively impact the performances of combined navigation systems. Therefore, measurement noise model optimization primarily focuses on the online estimation of the impact of road environment changes on GNSS data. Odometry is an important autonomous sensor for relatively good accuracy in its output ground speed data. In using the ground speed output of the odometer as a reference, the estimation of the GNSS/odometer ground speed residual sequence can further improve the estimation accuracy of the measurement noise model. The expression for the velocity measurement output by the odometer in the vehicle coordinate system is shown in Equation (1):

$$
\tilde{v}_{O D}^{m}=C_{m}^{b}(1+\delta K) v_{O D}+n_{O D}
$$

where $\tilde{v}_{O D}^{m}$ represents the measured value of odometer; $C_{m}^{b}$ represents the rotation matrix from the odometer body coordinate system to the vehicle body coordinate system; $\delta K$ represents the scale factor error; $v_{O D}$ represents the theoretical output value of the odometer; and $n_{O D}$ represents the Gaussian noise. In Equation (1), $C_{m}^{b}$ can be neglected due to mechanical mounting and high-precision offline calibration; $\delta K$ can also be ignored after estimation and correction using RTK-GNSS road sections. Therefore, $\tilde{v}_{O D}^{m}$ can be approximated as the sum of $v_{O D}$ and $n_{O D}$. The mean and variance of the noise $n_{O D}$ are primarily affected by road factors such as bumps and slipping.

In considering that the odometer is typically mounted centrally on the non-steering wheel axle and that the GNSS antenna is centrally mounted on the roof, the lever arm effect between the two can be neglected. In using the odometer velocity as the GNSS velocity measurement estimate, the GNSS/odometry velocity residual sequence can be expressed as shown in Equation (2):

$$
\begin{aligned}
\widetilde{Z}_{k / k-1} & =\widetilde{Z}-\widehat{Z}_{k / k-1}=\delta \widetilde{V}_{G N S S} \\
& =\sqrt{\left(v_{E}+\delta v_{E}\right)^{2}+\left(v_{N}+\delta v_{N}\right)^{2}}-\sqrt{\left(v_{E}\right)^{2}+\left(v_{N}\right)^{2}}-n_{O D} \\
& =\frac{2 v_{E} \delta v_{E}+2 v_{N} \delta v_{N}+\left(\delta v_{E}\right)^{2}+\left(\delta v_{N}\right)^{2}}{\sqrt{\left(v_{E}+\delta v_{E}\right)^{2}+\left(v_{N}+\delta v_{N}\right)^{2}}+\sqrt{\left(v_{E}\right)^{2}+\left(v_{N}\right)^{2}}}-n_{O D}
\end{aligned}
$$

where $\delta \widetilde{V}_{G N S S}$ represents the GNSS velocity residual sequence; $v_{E}$ represents the east velocity of the GNSS; and $v_{N}$ represents the north velocity of the GNSS. From Equation (2), it can be seen that the measurement noise of the velocity residual sequence does not follow

a Gaussian distribution. When the vehicle is stationary, the true velocity value is 0 , and the measurement noise becomes $\sqrt{\left(\delta v_{E}\right)^{2}+\left(\delta v_{N}\right)^{2}}-n_{O D}$, which follows the difference between the Rayleigh distribution $\left(\sqrt{\left(\delta v_{E}\right)^{2}+\left(\delta v_{N}\right)^{2}}\right)$ and the Gaussian distribution $\left(n_{O D}\right)$. When $v \gg \delta v$, Equation (2) can be approximated as the sum of three Gaussian distributions. These two cases are shown in Equation (3):

$$
\left\{\begin{array}{c}
\delta \widetilde{V}_{G N S S}=\sqrt{\left(\delta v_{E}\right)^{2}+\left(\delta v_{N}\right)^{2}}-n_{O D} ; v=0 \\
\delta \widetilde{V}_{G N S S} \approx \frac{v_{E} \delta v_{E}}{\sqrt{\left(v_{E}\right)^{2}+\left(v_{N}\right)^{2}}}+\frac{v_{N} \delta v_{N}}{\sqrt{\left(v_{E}\right)^{2}+\left(v_{N}\right)^{2}}}-n_{O D} ; v \gg \delta v
\end{array}\right.
$$

When the vehicle speed is between these two cases, Equation (2) can be represented as a mixed distribution, as shown in Equation (4):

$$
\delta \widetilde{V}_{G N S S} \approx \frac{v_{E} \delta v_{E}}{\sqrt{\left(v_{E}\right)^{2}+\left(v_{N}\right)^{2}}}+\frac{v_{N} \delta v_{N}}{\sqrt{\left(v_{E}\right)^{2}+\left(v_{N}\right)^{2}}}+\frac{\left(\delta v_{E}\right)^{2}+\left(\delta v_{N}\right)^{2}}{2 \sqrt{\left(v_{E}\right)^{2}+\left(v_{N}\right)^{2}}}-n_{O D}
$$

Figure 1 provides a concise illustration of the evolution process of the aforementioned residual sequence distribution characteristics. In Figure $1, \delta$ represents the root mean square error (RMSE) of the east and north velocity measurements. As the velocity gradually increases from 0 , the probability density function (PDF) of the measurement noise evolves from the Rayleigh distribution shown in PDF1 to the approximate Gaussian distribution shown in PDF5. In the three sets of data, PDF1, PDF2, and PDF3, the RMSE was set to $0.3 \mathrm{~m} / \mathrm{s}$, and the distribution characteristics gradually evolved toward the Gaussian distribution as the velocity increased. At the same time, in the two sets of data, PDF3 and PDF4, the velocity value was $3.754 \mathrm{~m} / \mathrm{s}$, and when the RMSE was reduced from $0.3 \mathrm{~m} / \mathrm{s}$ to $0.03 \mathrm{~m} / \mathrm{s}$, the distribution characteristics became closer to the Gaussian distribution. This shows that as the error-to-true value ratio decreases, the measurement noise error model will gradually evolve from a Rayleigh distribution to an approximate Gaussian distribution.
![img-0.jpeg](img-0.jpeg)

Figure 1. The residual sequence distribution characteristics.
In our previous research [34], using a simulation platform, we conducted a detailed analysis of the changes in the velocity and variance function relationship curves during the uniform acceleration of a vehicle from $[0 \mathrm{~m} / \mathrm{s}, 0 \mathrm{~m} / \mathrm{s}]$ to $[6 \mathrm{~m} / \mathrm{s}, 3 \mathrm{~m} / \mathrm{s}]$ for nine sets of GNSS velocity RMSE values. The results are shown in Figure 2.

![img-1.jpeg](img-1.jpeg)

Figure 2. The noise variance curve and the segmentation of the approximate Gaussian fitting region (AGFR) and approximate Gaussian convergence region (AGCR).

Based on the vehicle speed and innovation data distribution characteristics in Figure 2, a convergence function $y=f_{I}(x)$ is fitted, and the data regions satisfying the relationship, $y \geq f_{I}(x)$ and $y<f_{I}(x)$, are divided into the AGFR and the AGCR, respectively. In the AGFR, the nonlinearity of the speed and variance relationship function is relatively strong, and a neural network is suitable for fitting and solving. In the AGCR, the information sequence has converged, and it can be estimated according to the Gaussian distribution. In conventional autonomous driving scenarios, the data sequence distribution characteristics are basically consistent, and the mean and variance parameters can be estimated using the MLE method based on the given sufficient measurement dataset. However, in complex urban road positioning environments, RTK, GNSS single-point positioning, and GNSS challenging environment navigation states appear alternately, and the sample set formed by the information sequence within the time window may contain multiple Gaussian mixture distributions. In challenging environments, GNSS measurement data can bring significant errors to the state estimation model. Using a GMM to solve multiple sub-distributions of data within the window and eliminate outliers can further optimize the adaptive factor graph model. Based on the above analysis, the main calculation process of the multi-sensor fusion positioning system based on the approximate Gaussian noise model estimation is shown in Figure 3.
![img-2.jpeg](img-2.jpeg)

Figure 3. Multi-sensor fusion localization algorithm based on GMM noise parameter estimation.

# 3.2. The Design of Resilient Noise Model Based on the Approximate Gaussian Estimation Algorithm 

The distribution characteristics of the innovation sequence dynamically change between the Rayleigh distribution and approximate Gaussian distribution according to the driving speed and road environment changes of autonomous vehicles. The functional relationships between speed, innovation, and GNSS measurement noise parameters are divided into the AGFR and AGCR, and they are solved using a variational Bayesian network and GMM, respectively. The two algorithms are described in detail as follows.

### 3.2.1. Variational Bayesian Network Estimation of Noise Parameters Based on Innovation

Each nonlinear function curve in the AGFR corresponds to a specific speed measurement root mean square error, which essentially reflects the relationship between the change in ground speed variance with the increase in speed under different speed measurement root mean square error conditions. Therefore, the output result corresponding to each data group is not only related to the current value but also has a relationship with the previous and subsequent data. Based on the obvious advantages of the Gate Recurrent Unit (GRU) framework-deep neural network in sequence data processing, this network was selected for the measurement noise parameter estimation.

The variational Bayesian GRU (VBGRU) network combines the characteristics of variational Bayesian Inference (VBI) and the GRU network, introducing uncertainty weights into the model training process, representing model parameters with random variables of normal distribution, which greatly improves the adaptability and generalization ability of the model. Different from the traditional GRU network, the VBGRU uses random variables of a specific probability density distribution to fit nonlinear functions. At the same time, it can calculate its uncertainty while outputting the predicted value, which is a maximum a posteriori estimation method.

As the multi-sensor fusion positioning system is carried out on the autonomous driving edge computing platform, the real-time calculation performance of the algorithm is particularly important. Therefore, the VBGRU network adopts a lightweight three-layer Long Short-Term Memory (LSTM) architecture design, with the number of neurons being 48, 48, and 24, respectively; the decoder adopts a two-layer LSTM architecture, with the number of neurons being 24 and 24, respectively. Reference [33] conducted an experimental verification of the network through a simulation platform, and its accuracy could meet the measurement noise estimation requirements of urban roads.

### 3.2.2. Noise Parameter Estimation Based on Innovation and Gaussian Mixture Model

The essence of the GMM is to decompose a probability density function that conforms to the characteristics of a Gaussian distribution into multiple Gaussian functions. Its random variables can be either one-dimensional or multi-dimensional, which can be specifically expressed as shown in Equation (5):

$$
f(x)=\sum_{k=1}^{M} \lambda_{k} G_{k}\left(x \mid u_{k}, \Sigma_{k}\right)
$$

In the equation, $\lambda_{k} G_{k}\left(x \mid u_{k}, \Sigma_{k}\right)$ represents the multi-dimensional Gaussian function, $\lambda_{k}$ is the normalization coefficient, and it represents the weight of the Gaussian function. According to the GNSS/odometer innovation sequence probability density function, the Gaussian mixture maximum likelihood function can be obtained, and the logarithm is taken on both sides to obtain Equation (6):

$$
\operatorname{Log}(\theta \mid x)=\sum_{j=1}^{N} \log \sum_{l=1}^{M} \lambda_{i} p_{i}\left(x \mid \theta_{i}\right)
$$

In the above equation, $p_{i}\left(x \mid \theta_{i}\right)$ is the probability density function of the Gaussian distribution. In using the expectation-maximization (EM) algorithm, the Gaussian distribu-

tion combination containing multiple hidden variables is iteratively solved. Firstly, based on the Jensen inequality, the expectation of the hidden variable is calculated as shown in Equation (7), and the lower bound $B(\theta)$ of the likelihood function is further obtained, as shown in Equation (8).

$$
\begin{gathered}
\operatorname{Log}(\theta \mid x)=\sum_{j=1}^{N} \log \sum_{i=1}^{M} \lambda_{i} p_{i}\left(x_{j} \mid \theta_{i}\right)=\sum_{j=1}^{N} \log \left(\sum_{i=1}^{M} q_{i}(x) \frac{\lambda_{i} p_{i}\left(x_{j} \mid \theta_{i}\right)}{q_{i}(x)}\right) \\
\geq \sum_{j=1}^{N} \sum_{i=1}^{M} q_{i}(x) \log \frac{\lambda_{i} p_{i}\left(x_{j} \mid \theta_{i}\right)}{q_{i}(x)} \\
B(\theta)=\sum_{j=1}^{N} \sum_{i=1}^{M} q_{i}\left(x_{j}\right)\left[\log \left(\lambda_{i} p_{i}\left(x_{j} \mid \theta_{i}\right)\right)-\log \left(q_{i}\left(x_{j}\right)\right)\right]
\end{gathered}
$$

Then, in adjusting the model parameters $\theta_{i}$ to maximize the lower bound of the likelihood function as shown in Equation (8), Equation (9) can be obtained. In taking the partial derivative of $\theta$ and setting it to 0 , the updated parameters $\theta_{i+1}$ can be obtained.

$$
\hat{\theta}=\operatorname{argmax} \sum_{j=1}^{N} \sum_{i=1}^{M} q_{i}\left(x_{j}\right)\left[\log \left(\lambda_{i} p_{i}\left(x_{j} \mid \theta_{i}\right)\right)-\log \left(q_{i}\left(x_{j}\right)\right)\right]
$$

Determine whether the convergence condition $\left\|\theta_{i+1}-\theta_{i}\right\| \leq \varepsilon$ is satisfied. If not, repeat the above expectation and maximization calculation processes until the convergence condition is satisfied and the Gaussian distribution statistics corresponding to different innovation sequences can be obtained. The key steps of the above method are briefly outlined in Algorithm 1.

```
Algorithm 1: GNSS measurement noise parameter estimation algorithm based on GMM
Input (Velocity residual sequence \(X\), number of Gaussian distributions \(k\), convergence threshold \(\varepsilon\) )
Output (Parameters for each Gaussian distribution: mean \(\mu_{k}\), covariance \(c_{k}\), and weight
    coefficient \(\lambda_{k}\) )
Initialize:
Initialize the parameters for each Gaussian distribution: \(\theta_{i}(\) mean \(\mu_{k}\), covariance \(c_{k}\), and weight
    coefficient \(\lambda_{k}\) ).
Iterative Update Steps:
while not reached the maximum number of iterations or not converged:
    E-step (Expectation step):
        For each data point \(x_{i}\) :
            Calculate the responsibility of each Gaussian distribution \(q_{i}(x)\)
                \(q_{i}(x)=\lambda_{i} p_{i}\left(x \mid \theta_{i}\right) / \sum_{i=1}^{k} \lambda_{i} p_{i}\left(x \mid \theta_{i}\right)\)
    M-step (Maximization step):
        For each Gaussian distribution \(k\) :
            Update the mean \(\bar{\mu}_{i}\) :
                \(\mu_{i}=\sum_{j=1}^{N} q_{i}\left(x_{j}\right) x_{j} / \sum_{i=1}^{N} q_{i}\left(x_{j}\right)\)
            Update the weight coefficient \(\lambda_{i}\) :
                \(\lambda_{i}=\frac{1}{N} \sum_{j=1}^{N} q_{i}\left(x_{j}\right)\)
            Update the covariance \(c_{i}^{2}\) :
                \(c_{i}^{2}=\sum_{j=1}^{N} q_{i}\left(x_{j}\right)\left(x_{j}-\mu_{i}\right)^{T}\left(x_{j}-\mu_{i}\right) / \sum_{j=1}^{N} q_{i}\left(x_{j}\right)\)
    Check for convergence:
        If the change in parameters is less than the threshold \(\varepsilon\), stop iterating.
```

# 4. IMU/GNSS/Odometer/Vision Fusion Positioning Scheme Based on the Adaptive Factor Graph Optimization Model 

As the resilient noise model based on the approximate Gaussian estimation was described in the above section, the factor graph-based IMU/GNSS/odometer/vision integration navigation method enhanced by the proposed resilient noise model is introduced in this section.

### 4.1. Adaptive Factor Graph Data Fusion Architecture Design

In the multi-sensor data fusion model, the observation is the output data of the subsystem, and the error model of each sensor is defined as the factor node function. The optimal estimation equation of the factor graph can be expressed as in Equation (10):

$$
\hat{X}=\operatorname{argmax} \prod_{i=1}^{k} f_{i}\left(X_{i}\right)
$$

where $f_{i}\left(X_{i}\right)$ is the cost function composed of the errors of each sensor subsystem; $X_{i}$ is the state variable; $i$ is the number of the factor node; $k$ is the total number of factor nodes within the time window; and $\hat{X}$ is the maximum posterior estimation of the state variable. The optimal estimation method of the factor graph obtains the global optimal estimation of the state variable $X$ by solving the minimum value of the total cost function. The factor nodes of the sensor subsystems all correspond to independent probability functions, which can be expressed as the proportional relationship shown in Equation (11):

$$
p\left(X_{k} \mid Z_{k}\right) \propto \prod_{i=1}^{k} p\left(Z_{i} \mid X_{i}\right) p\left(X_{i} \mid X_{i-1}\right) \propto \prod_{i=1}^{k} f_{i}\left(X_{i}\right)
$$

In Equation (11), $p\left(X_{k} \mid Z_{k}\right)$ is the maximum posterior probability density of the state variable $X_{k}$ given the observation $Z_{k}$. Assuming that the noise model $R$ of the sensor subsystem follows the Gaussian distribution, the corresponding error function can be obtained by substituting the multidimensional Gaussian probability density function, as shown in Equation (12):

$$
p\left(Z_{m} \mid X_{i}^{m}\right) \propto f_{i}\left(X_{i}^{m}\right)=\exp \left(-\frac{1}{2}\left\|h\left(X_{i}^{m}\right)-z_{m}\right\|_{R}^{2}\right)
$$

In Equation (12), $m$ is the time of the model update. The cost function can be rewritten as Equation (13):

$$
l(\operatorname{err})=\exp \left(-\frac{1}{2}\|\operatorname{err}\|_{\Sigma}^{2}\right)
$$

In Equation (13), $\Sigma$ is the covariance matrix for measuring noise, and err is the residual function between the predicted and measured values of the model. The optimal estimation method of the factor graph can be expressed as in Equation (14):

$$
\hat{X}=\operatorname{argmax} \prod_{i=1}^{k} f_{i}\left(X_{i}\right)=\operatorname{argmax}\left(\sum l(\operatorname{err})\right)=\operatorname{argmin}\left(\sum\left\|\operatorname{err}_{i}\right\|_{\Sigma_{i}}^{2}\right)
$$

Based on the above theoretical derivation, the multi-sensor fusion positioning system architecture based on adaptive factor graph is shown in Figure 4.

As shown in Figure 4, the INS factor connects the state variable nodes of the previous and next adjacent moments, while the GNSS, vision/map, and odometry factors only relate to the state variable at the current moment. The specific factor node functions of each sensor subsystem are as follows.

![img-3.jpeg](img-3.jpeg)

Figure 4. Architecture diagram of multi-sensor fusion positioning system based on adaptive factor graph.

# 4.2. INS Factor 

The INS is a core subsystem in the autonomous navigation system, connecting the state variable factors of the previous and next moments. Its output frequency is higher than those of other sensors, which can be used for state update estimation and state propagation asunnd prediction through the sum algorithm. By pre-integrating the inertial device measurement data $\left\{\tilde{f}^{b}, \tilde{\omega}^{b}\right\}$ within the time interval $\left[t_{k}, t_{k+1}\right]$, the real-time performance of the algorithm can be effectively improved. The cost function of the INS factor is shown in Equation (15):

$$
f^{I M U}\left(x_{k}\right)=l\left(\tilde{x}_{k+1}-h\left(x_{k}, z_{k}^{I M U}\right)\right)=\exp \left(-\frac{1}{2}\left\|\tilde{x}_{k+1}-h\left(x_{k}, z_{k}^{I M U}\right)\right\|_{Q}^{2}\right)
$$

In Equation (15), the cost function $l(*)$ represents the INS factor, which is proportional to the random distribution function of the difference between the observed value and the estimated value of the state variable.

### 4.3. GNSS Factor

The GNSS factor is mainly related to the state variable at the current moment. The cost function can be obtained through the current observation value and the estimated value, as shown in Equation (16):

$$
f^{G N S S}\left(x_{k}\right)=l\left(z_{k}^{G N S S}-h^{G N S S}\left(x_{k}\right)\right)=\exp \left(-\frac{1}{2}\left\|z_{k}^{G N S S}-h^{G N S S}\left(x_{k}\right)\right\|_{R_{-} \bar{G}}^{2}\right)
$$

In the GNSS factor shown in Equation (16), $h^{G N S S}\left(x_{k}\right)$ represents the GNSS estimated value in the cost function, which can be either the position and velocity estimated value or the pseudorange and pseudorange rate estimated value. In order to improve the algorithm efficiency and system stability, a loosely coupled model is adopted, and the position and velocity parameters of satellite navigation are used as observation measurements.

### 4.4. Odometry Factor

The scale factor error is the main error in the output measurement value of the odometer. When the GNSS operates in RTK mode, after accurately estimating and compensating this error with high-precision measurement values, the error can be modeled as a constant error. In assuming that the odometer measurement error satisfies the Gaussian distribution, the factor can be expressed as shown in Equation (17):

$$
f^{O D}\left(x_{k}\right)=l\left(z_{k}^{O D}-h^{O D}\left(x_{k}\right)\right)=\exp \left(-\frac{1}{2}\left\|z_{k}^{O D}-h^{O D}\left(x_{k}\right)\right\|_{R_{-} O}^{2}\right)
$$

In Equation (17), $z_{k}^{O D}$ of the cost function is the odometer measurement output value, and $h^{O D}(\cdot)$ represents the odometer output value estimated based on the current vehicle motion state value, which mainly includes attitude misalignment error, installation error, and scale factor error.

# 4.5. Vision/Map Factor 

In the previous research results [10], a vision/map attitude matrix construction algorithm was proposed, of which the main error sources are positioning error, map data error, and lane line recognition error. The measurement equation is shown in Equation (20):

$$
z_{k}^{V / m a p}=h^{V / m a p}\left(x_{k}\right)+n^{V / m a p}
$$

In Equation (18), $h^{V / m a p}$ is the relationship expression between the attitude angle, heading angle, and road attitude matrix in the state vector, and $n^{V / m a p}$ is the measurement noise. The expression of the vision/map factor is shown in Equation (19):

$$
f^{V / m a p}\left(x_{k}\right)=l\left(z_{k}^{V / m a p}-h^{V / m a p}\left(x_{k}\right)\right)=\exp \left(-\frac{1}{2}\left\|z_{k}^{V / m a p}-h^{V / m a p}\left(x_{k}\right)\right\|_{R_{-} V}^{2}\right)
$$

In summary, the IMU/GNSS/odometer/vision factor graph data fusion model can be expressed as shown in Equation (20):

$$
\begin{aligned}
\hat{X} & =\operatorname{argmin}\left\{\sum\left\|\tilde{x}_{k+1}-h\left(x_{k}, z_{k}^{I M U}\right)\right\|_{Q_{-} I}^{2}+\sum\left\|z_{k}^{O D}-h^{O D}\left(x_{k}\right)\right\|_{R_{-} O}^{2}\right. \\
& \left.+\sum\left\|z_{k}^{G N S S}-h^{G N S S}\left(x_{k}\right)\right\|_{R_{-} G}^{2}+\sum\left\|z_{k}^{V / m a p}-h^{V / m a p}\left(x_{k}\right)\right\|_{R_{-} V}^{2}\right\}
\end{aligned}
$$

The optimal estimation problem of the factor graph is essentially to find the minimum Mahalanobis distance $\|x-u\|_{\Sigma}^{2}$ between the observed value and the predicted value.

## 5. Experimental Verifications

The performance of the proposed navigation method was verified in this study. Firstly, based on the simulation platform, the accuracy of the approximate Gaussian estimation method was verified. Furthermore, through real-vehicle road tests, the superiority of the adaptive factor graph fusion positioning system based on resilient noise model was verified in typical scenarios.

### 5.1. Simulation Verification of Resilient Noise Model Based on Approximate Gaussian Estimation

In a complex urban road environment, the measurement information collected by the factor graph model within the sliding window may contain multiple GNSS working states. The GMM method is a probability model that can be used to represent multiple sub-distributions of the population distribution and is suitable for the estimation of the noise parameters mentioned above. Since it is difficult to obtain the true values of actual road acquisition data, the accuracies of the above two algorithms can be compared more clearly through the data simulation. Based on the simulation platform, a GNSS/odometer information sequence with a total length of 3000 was generated, and the expectations, root mean square errors (RMSE), and weights of two types of positioning status data were set to simulate the information sequence of mixed road sections in three positioning states: RTK + SSP, RTK + CE, and SSP + CE. The details are shown in the following table.

The GNSS velocity error can generally be considered a zero-mean Gaussian distribution. At the same time, after the RTK state GNSS/odometer fusion correction, the odometer scale factor error can be ignored. Therefore, the expected values of the above three residual sequences were set to $0 \mathrm{~m} / \mathrm{s}$. According to the empirical value, the initial parameters of the GMM were set, and the above three sets of binary Gaussian distribution data were estimated, respectively. Then, each set of data estimated two sets of corresponding expectations, RMSEs, and their weights, as shown in Figures 5-7.

![img-4.jpeg](img-4.jpeg)

Figure 5. Estimation results of the GMM algorithm for the residual sequence in the RTK/SPP mixed scenario. (a) The weight estimation error of the measurement noise sequence; (b) the probability density function for measuring noise sequences.
![img-5.jpeg](img-5.jpeg)

Figure 6. Estimation results of the GMM algorithm for the residual sequence in the RTK/CE mixed scenario. (a) The weight estimation error of the measurement noise sequence; (b) the probability density function for measuring noise sequences.

Figures 5-7 show the performance of the GMM algorithm in estimating the GNSS measurement noise in the three typical urban complex road environments, as indicated in Table 1. Figure 5a shows the estimation effect of the GMM on the weights of the RTK and SPP measurement data, which gradually converge after 180 iterations. Figure 5b uses curves of three colors to, respectively, display the PDFs of the RTK, SPP, and the hybrid data. The measurement errors of both the RTK and SPP conform to a zero-mean Gaussian distribution. When mixed according to their respective weights, their statistical properties remain as a zero-mean distribution. Figures 6 and 7, respectively, display the estimation of the statistical properties of the two types of hybrid GNSS state measurement data, RTK + CE and SPP + CE, using the GMM algorithm. In using the MLE method, the above three groups of data were estimated, respectively, and each group of data could obtain a set of corresponding expectation and root mean square error parameters. Table 2 shows the MLE algorithm estimation values, GMM algorithm estimation values, and error comparison analysis results of the above three groups of parameters.

![img-6.jpeg](img-6.jpeg)

Figure 7. Estimation results of the GMM algorithm for the residual sequence in the SPP/CE mixed scenario. (a) The weight estimation error of the measurement noise sequence; (b) the probability density function for measuring noise sequences.

Table 1. Simulation parameter table for innovation sequence.


Table 2. Estimation and comparison of MLE and GMM algorithms.


As shown in the table, the MLE algorithm estimates the new information sequences of the RTK + SPP, RTK + CE, and SPP + CE mixed navigation modes as a whole, respectively. Therefore, each group of data only corresponds to a set of expectations and RMSEs. Under the "estimation error/true value ratio", one group of MLE data is represented as "-". The expectations of the mixed new information sequences were all $0 \mathrm{~m} / \mathrm{s}$, so both the MLE and GMM algorithms can achieve accurate expectation estimations. The RMSE parameters of the residual sequences are quite different, and the estimation accuracy of the GMM is significantly higher than that of the MLE, with a maximum improvement of $26.2 \%$. This is mainly because of the MLE estimating two different sequences as the same probability distribution will introduce significant errors that cannot be ignored. Compared to RTK + SPP ( $21.65 \%$ ) and SPP + CE ( $15.09 \%$ ), in RTK + CE mode, the difference in system accuracy between the two GNSS operating states is the greatest. Therefore, the improvement in the estimation accuracy of the GMM is also more significant.

# 5.2. Real-World Road Test

The test was conducted in Xiqing District, Tianjin, China. The test equipment is shown in Table 3.

Table 3. Test equipment and parameter list.


The reference device (TJYJ/15-S1) in Table 3 is a high-precision fiber-optic inertial/satellite system, which provided high-precision reference information for the test. In order to obtain accurate reference information and environmental errors and to compare the algorithm improvement effect more clearly, the test simulated a GNSS single-point positioning and satellite navigation challenging environment (Gaussian noise simulating positioning errors) through software in a specific road section. The specific test method was as follows:
(1) In the whole test section, the reference device collects the fusion positioning data in RTK working mode, which is used as the theoretical reference value;
(2) In the RTK positioning section, the traditional factor graph model and the proposed model are used to solve the data of each sensor subsystem synchronously;
(3) In the GNSS single-point positioning section, GNSS data are collected in nondifferential mode, and the data are fused with other sensor subsystems using two model algorithms;
(4) In the GNSS challenging environment section, Gaussian noise is added to the collected GNSS data to simulate the satellite data of a complex urban road environment with multiple interference factors superimposed.

The test route and urban road environment simulation are shown in Figure 8, starting and ending at 27 Xingguang Road, Xiqing District ( $\star$ in the figure).

As shown in Figure 8a, the test vehicle traveled southward to Fujin Road, passing Wanhuai Road, Outer Ring West Road, Zhongbei Avenue, Chunhua Road, Fujin Road, and Xingguang Road along the way. The total route length was 12.508 km , and the driving time was 28 min and 57 s . Figure 8 b illustrates the driving directions of the test vehicle, the RTK road section, the single-point positioning road section, and the CE road section setting scheme. The test route and test vehicle are shown in Figure 9. The reference equipment and test equipment were fixed using hexahedral tooling and aluminum tooling, respectively, and rigidly connected to each other.

The vehicle's speed profile during the test is shown in Figure 10. The maximum vehicle speed was $18.5422 \mathrm{~m} / \mathrm{s}$ (corresponding to $66.75 \mathrm{~km} / \mathrm{h}$ ) at 699 s , with the maximum eastward speed reaching $18.5417 \mathrm{~m} / \mathrm{s}$. At 1426 s , the maximum northward speed reached $18.1506 \mathrm{~m} / \mathrm{s}$ (corresponding to $65.35 \mathrm{~km} / \mathrm{h}$ ). The test vehicle performed various maneuvers during the test, including acceleration, deceleration, stopping, high/low-speed driving, left turns, right turns, and U-turns. The average driving speed was $25.94 \mathrm{~km} / \mathrm{h}$.

![img-7.jpeg](img-7.jpeg)

Figure 8. Adaptive factor graph fusion localization algorithm for vehicle test route planning based on approximate Gaussian estimation. (a) On-road vehicle test route planning; (b) urban road environment simulation scheme.
![img-8.jpeg](img-8.jpeg)

Figure 9. Adaptive factor graph fusion localization algorithm for vehicle test route planning based on approximate Gaussian estimation: on-road vehicle test with real-world data.
![img-9.jpeg](img-9.jpeg)

Figure 10. Urban road test, vehicle speed profile.
To validate the performance of the proposed adaptive factor graph with a resilient noise model algorithm, we conducted a comparative analysis with a traditional factor graph approach. Figure 11 presents the speed errors obtained for all test sections.

![img-10.jpeg](img-10.jpeg)

Figure 11. Real-world driving test, speed error comparison plot.
Figure 11 shows the speed errors obtained for both the AFG and FG algorithms. It can be observed that both algorithms exhibit comparable accuracies under RTK conditions. However, when transitioning to single-point positioning, the AFG algorithm demonstrates the ability to improve in accuracy to a limited extent through the online estimation and correction of the noise model. In challenging satellite navigation environments, the traditional FG algorithm fails to effectively identify external interference, resulting in significant fluctuations in speed error. In contrast, the AFG algorithm not only recognizes the impact of external factors on the system but also accurately estimates them. In adjusting the noise covariance matrix parameters, the influence of environmental factors can be substantially reduced.

Furthermore, the errors in position, attitude angles, and heading angle obtained by both algorithms exhibit consistency with the speed errors, as shown in Figures 12-14.
![img-11.jpeg](img-11.jpeg)

Figure 12. Real-world driving test, position error comparison plot.

![img-12.jpeg](img-12.jpeg)

Figure 13. Real-world driving test, attitude angle error comparison plot.
![img-13.jpeg](img-13.jpeg)

Figure 14. Real-world driving test, heading angle error comparison plot.
As shown in Figure 12, the trends of the east and north positioning errors are essentially the same as the velocity error shown in Figure 11. The AGF algorithm has significantly improved the system accuracy through performing an approximate Gaussian estimation of the GNSS measurement noise parameters for the three CE road segments. Figures 13 and 14, respectively, present the attitude and heading errors, from which it can be observed that the improvement in heading error is more significant. This is mainly because autonomous vehicles driving on urban roads have relatively small changes in attitude angles, and the errors are not fully stimulated. To facilitate a more comprehensive analysis of the AFG algorithm's improvement, the RMSEs from Figures 11-14 are statistically summarized in Table 4. Additionally, Table 5 presents the calculated accuracy improvement achieved by the AFG algorithm.

As evidenced in Tables 4 and 5, the AFG algorithm significantly enhances the accuracy of multi-source integration positioning systems in urban complex road environments compared to the traditional FG algorithm. Notably, in challenging road sections, the heading error is improved by up to $65.63 \%$. This improvement primarily stems from the ability of the AFG algorithm to effectively suppress error divergence through model optimization. In contrast, the FG algorithm's heading error estimation accuracy is significantly reduced during the low-speed phase of Zhongbei Avenue (CE-1) due to the rapid increase in speed error. Furthermore, in the CE discussed in Section 3, the AGE-FG algorithm achieves accuracy improvements of $27.80 \%, 32.34 \%, 39.52 \%$, and $42.95 \%$ for speed and position errors. This is mainly attributed to the larger errors introduced in this section,

which amplifies the effectiveness of the AFG algorithm's error estimation improvement. Additionally, the higher speed in the CE discussed in Section 3 reduces the proportion of the speed error in the true value, enhancing the accuracy of the track angle. Consequently, the AFG algorithm's improvement in heading error estimation accuracy is less pronounced.

Table 4. Comparison of navigation accuracy between FG and proposed AFG algorithm.


Table 5. Statistical summary of accuracy improvement achieved by AFG algorithm compared to FG.


# 6. Conclusions 

To address the issues of insufficient continuity and poor accuracy in multi-sensor fusion positioning caused by the GNSS's vulnerability in urban canyon environments, this paper proposes a resilient factor graph-based fusion positioning algorithm enhanced by the approximate Gaussian estimation of noise models. Firstly, leveraging the autonomy and accuracy advantages of odometry data, GNSS/odometry ground speed residual sequences are used as measurement values for noise parameter estimation, and their approximate Gaussian distribution characteristics are analyzed. Furthermore, based on variational Bayesian networks and Gaussian mixture models, the resilient noise model based on approximate Gaussian estimation is proposed. Finally, the resilient factor graph-based IMU/GNSS/vision/odometer integrated navigation system was tested and verified through simulation platforms and real-vehicle road tests. The results demonstrate the effectiveness and superiority of the algorithm, with heading, speed, and position accuracy improvements of up to $65.63 \%$, $32.34 \%$, and $42.95 \%$, respectively, in GNSS-challenging environments.

Although the above research achieved good results, there are still some limitations that can be improved upon in the future work. From the perspective of optimizing the factor graph multi-sensor data fusion model, dynamically optimizing the sliding window, the online adjustment of feedback correction coefficients, and autonomous sensor fusion are all promising research directions. Firstly, by predicting the positioning state of urban roads based on prior maps and real-time positioning data, the factor graph sliding window size can be resilient and adjusted to improve the system's positioning accuracy; secondly, the online calculation of the system observability and dynamic optimization of feedback correction coefficients for state estimation values based on this calculation can enhance the system's fault tolerance and robustness; additionally, combining multi-sensor fusion global positioning with LiDAR local positioning can significantly improve the integrity and safety of autonomous vehicle driving. The use of artificial intelligence technology for

the auxiliary optimization of multi-sensor autonomous fusion navigation systems is also an important research direction. Firstly, in using a visual foundation model to intelligently recognize the road environment, GNSS measurement noise estimations can be obtained, and then the online adaptive optimization of the data fusion model can be achieved; secondly, based on deep learning neural networks and prior maps, the optimal estimation of the observability of the data fusion model can greatly improve the robustness and fault tolerance of the system.

Author Contributions: Conceptualization and methodology, Z.L. and Q.M.; software, writing—original draft preparation, and validation, Z.L.; investigation and data curation, Z.S. and H.J.; visualization, L.W. and L.L.; writing-review and editing, supervision, project administration, and funding acquisition, Q.M. All authors have read and agreed to the published version of the manuscript.
Funding: This work was funded by the National Natural Science Foundation of China (No. 62388101 and No. 62203111), Aeronautical Science Foundation of China (20220008069003), Natural Science Foundation of Jiangsu Province (No. BK20231434), and Jiangsu Provincial Department of Science and Technology (No. BM2023013).

Data Availability Statement: The datasets used and/or analyzed during the current study are available from the corresponding author upon reasonable request.

Conflicts of Interest: Author Ziyue Li was employed by the company Beijing Kunpeng Borui Technology. The remaining authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.
