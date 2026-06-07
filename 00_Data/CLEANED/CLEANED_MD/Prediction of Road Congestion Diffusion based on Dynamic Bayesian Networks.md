PAPER $\cdot$ OPEN ACCESS

## Prediction of Road Congestion Diffusion based on Dynamic Bayesian Networks

To cite this article: Xinyue Fan et al 2019 J. Phys.: Conf. Ser. 1176022046

View the article online for updates and enhancements.

## You may also like

- Simulation-based inference on virtual brain models of disorders
Meysam Hashemi, Abolfazl Ziaeemehr, Marmaduke M Woodman et al.
- KPM-induced modulation instability in silicon-on-insulator nano-waveguides and the impact of nonlinear losses Deepa Chaturvedi, Ajit Kumar and Akhilesh Kumar Mishra
- MZI-based all-optical serial-to-parallel conversion circuit by free-carrier dispersion effect
Ranepura Howage Neranjith, Yuya Shoji and Tetsuya Mizumoto


# Join the Society Led by Scientists, for Scientists Like You! 

![img-0.jpeg](img-0.jpeg)

This content was downloaded from IP address 81.35.110.163 on 01/06/2025 at 18:06

# Prediction of Road Congestion Diffusion based on Dynamic Bayesian Networks 

Xinyue Fan ${ }^{1,2}$, Jiao Zhang ${ }^{2}$ and Qi Shen ${ }^{3, *}$<br>${ }^{1}$ Guizhou Provincial Key Laboratory of Public Big Data, Guizhou University, China<br>${ }^{2}$ School of Mathematics and Statistics, Guizhou University, China<br>${ }^{3}$ Science and Technology Department, Guiyang Public Security Traffic Administration Bureau, China<br>*Corresponding author e-mail: 29722339@qq.com


#### Abstract

Based on the passing data and floating car data (FCD) collected by the traffic police of Shenzhen Public Security Bureau, China. A dynamic Bayesian network (DBN) model is constructed to describe the change and dissipation of road congestion. The prediction model of road congestion diffusion is established by integrating Internet traffic data and FCD data. To provide a theoretical basis for solving urban traffic congestion, the experimental results show that the prediction results coincide with the actual state of the Internet road conditions, which proves the feasibility and practicability of the prediction method.


## 1. Introduction

In recent years, the urban road is becoming complicated, and the urban traffic problems are becoming more serious. With the process of urban modernization, vehicles increase rapidly in the city. Urban traffic congestion is becoming a big traffic problem and social problem. Many factors will cause traffic congestion such as the road physical condition, unexpected vehicular failure, weather conditions, or a road accident, etc. Prediction of road congestion in real-time is a key problem for applications of Intelligent Transportation Systems (ITS), which dedicate to traffic management and pedestrian information[1]. Existing road congestion prediction methods in view of artificial neural network (ANN)[2], hidden Markov model (HMM)[3], plain mathematical model[4]. Pankaj et al. Based on multiple symbol HMM, [5] built an adaptive traffic congestion prediction model which incorporate any number of reflecting factors. Shraddha et al. presented a distributed camera network based on road traffic surveillance and a forecast scheme in paper [6].

For estimating the urban traffic congestion, lots of works concentrated upon the prediction of traffic flow parameters and fixed quantity, such as mean velocity, capacity, flow and density, etc. However, road network capacity, density is not easy to obtain. Only one parameter can not reflect local traffic congestion. For government department managers and drivers, they are more concerned about when the traffic congestion can be dissipated, how to choose the most fast road to their aim. In traffic congestion mitigation and traffic situation forecasting, the most important thing is to describe the diffusion process. In road networks, document lacks precise models for characterizing the process of traffic congestion diffusion, through it can be observed. Zhao [7] discussed congestion diffusion by traffic flow influence from a macro perspective, but it could not be widely used for urban road traffic congestion. In order to alleviate traffic congestion, many experts and scholars have done a lot of simulation experiments and research on predicting traffic flow state. Through the pheromone

mechanism instead of using traffic control center, Ando [8] proposed a method to short-term future predicts traffic congestion. Liu [9] used the Bayesian Network method to accurately predict the probability of urban traffic congestion. Based on the self-organization criticality of collaborative theory, Zhang [10] created synergetic predictive models. Zhao [11] used a Markov decision chain model to study traffic congestion. The trend of traffic flow is calculated based on information entropy, and the heuristic forecasting model is used to predict the traffic congestion. Wang [12] explored traffic congestion correlation from multiple data sources to predict traffic congestion.

In the paper, we present a dynamic Bayesian network model to characterize the traffic diffusion process. It is an extension of dynamic Bayesian network in time series, and it can learn the probability dependence relation between variables and its changing rule with time. The main idea s is that we first construct the dynamic of Bayesian network. The cause of traffic congestion is not just caused by single factors. Dynamic Bayesian network not only inherits the advantages of static Bayesian network, but also considers the influence of time factors on the model. It is a network model which can be used for reasoning and prediction. In this paper, the floating car data provided by traffic police bureau of Shenzhen Public Security Bureau and the data of Internet navigation platform are used to study. Dynamic Bayesian network model is constructed to predict road congestion. At any time after road congestion occurs, road congestion changes are predicted based on the obtained historical monitoring data.

# 2. Average speed algorithm for floating car data (FCD) 

There are two main types of vehicle speed information: interval mean velocity and instantaneous velocity. For the calculation of road speed, if the instantaneous speed is adopted, the average speed of vehicles passing through the road can not be well described because of the sampling interval of FCD and the individual characteristics of vehicle behavior. In general, the mean method is used to calculate the average speed of road sections. Assuming that a single vehicle sample has GPS information at different locations on a section of the road, the instantaneous speed of a single vehicle is the average speed of a floating vehicle on the section. Let $\left\{v_{i}\right\}$ is instantaneous speed, $v^{k}$ is average speed of FCD, then

$$
v^{k}=\frac{1}{n} \sum_{i=1}^{n} v_{i}, k=1,2,3 \ldots
$$

Extract the trajectory data of a certain section of a day for feature analysis. The interval is 5 minutes, plot average velocity frequency diagram (Figure 1).
![img-1.jpeg](img-1.jpeg)

Figure 1 Frequency chart of average velocity of a road section
The average velocity frequency maps extracted by FCD on the road sections show bimodal distribution, and the speed is slower in the congested sections. According to the central limit theorem, the data set of road travel speed $V=\left\{v^{k}\right\}$ passes the K-S test under the condition of collecting a large number of floating vehicle data. The distribution tends to normal distribution $V \sim N\left(v^{k}, \sigma^{2}\right)$, That is, its frequency density curve will show Gauss distribution rule ${ }^{[13]}$. Here, $v^{k}$ is the average instantaneous speed of road sample data reflects the centralization trend of road speed distribution. $\sigma$ is the standard

deviation of road sample velocity which reflects the discrete degree of the overall velocity distribution of road samples. In a time interval of data analysis, if the number of single-car section travel speed samples reaches a certain number, the reliability of traffic flow section travel speed calculation results is higher. At this point, the reliability and the number of samples are obviously proportional. Yang et al. [14] carried out a quantitative study on the sample size of floating vehicles on the road section. Here, in order to accurately describe the degree of road congestion through speed, outliers must be removed from the abnormal data, including noise data caused by parking, passenger stopping and other factors. Using $3 \sigma$ outliers to filter outliers, the standard is

$$
v_{T}=v^{k} \pm 3 \sigma
$$

According to the statistical distribution characteristics of floating vehicle data, the noise data cleaning threshold model can filter the FCD noise data quickly and efficiently by setting the threshold filtering frequency band with the average speed as the center.

For $n$ vehicle speed samples passing through a certain section $\left(v_{T, 1}, l_{1}\right),\left(v_{T, 2}, l_{2}\right), \ldots,\left(v_{T, n}, l_{n}\right)$, where $v_{T, n}$ is the average speed of a single vehicle after excluding outliers, $l_{n}$ is the covered driving distance. The reliable travel speed of the section is

$$
v=\frac{\sum_{i=1}^{n} l_{i}}{\sum_{i=1}^{n} v_{T, i}}
$$

Compared with the average speed calculated by the arithmetic mean value directly (1), the data after denoising and the result calculated by (3) formula alleviate the influence of high-speed and lowefficiency samples on the final results, making the calculation results more accurate.

# 3. Road congestion identification 

With the popularity of mobile internet travel applications in recent years, traffic travel data provides another data perspective for real-time road conditions. In this paper, congestion prediction is based on the road condition monitoring and evaluation data provided by the third-party Internet large data platform. Internet road condition data has a separate evaluation system, which takes a more detailed division of road units for administrative roads, and gives time-series road conditions for each segment of road units. The road state index corresponds to different road grades and traffic speed interval thresholds.
Table 1 Different road grades and speed range thresholds corresponding to road state index values


## 4. Dynamic Bayesian network (DBN)

Bayesian network (BN), also called Belief network, it has been widely used in various environmental modeling and decision support applications, which provides a method for modeling complex systems. The dependencies between attributes are characterized by directed acyclic graph and the joint probability distribution of attributes is described by conditional probability table. The Bayesian network can be divided into static Bayesian network (SBN) and dynamic Bayesian network (DBN). DBN developed on the basis of SBN and hidden Markov model (HMM), which is an extension of BN by introducing temporal dependencies. The conclusions obtained by SBN cannot extrapolate to particular time, nor handled time series. Thus, DBN is more reasonable to be introduced to modelling

traffic congestion diffusion process. Road traffic is a dynamic real-time scene, which changes with time. Time is expressed as discrete time slices that are connected by directed arcs form the node in the slice $t$ to the node in the slice $t+1{ }^{[15]}$. There is an upstream and downstream relationship between roads or sections, that is, the whole road network has a topological structure. Downstream congestion strongly affects the upstream congestion. Traffic flow itself has the characteristics of randomness, and the same factors influence each other at different times. The essence of Bayesian network theory is a reasoning network based on probabilistic uncertainty, which is one of the most importance theoretical models in the field of uncertain knowledge representation and reasoning. The dynamic Bayesian network theory can be used as a powerful theoretical basis for road congestion prediction. The target of this paper is modelling the temporal behavior of traffic congestion diffusion process through DBN and shows its applicability in traffic congestion modelling. It is the first time that topological structure of road network has been included in a DBN for traffic modelling.

Bayesian network can effective represent and compute the joint probability distributions on a set of random variables, which implement a graphic modelling structure known as directed acyclic graphing ${ }^{[16]}$. The conditional probability table describes the degree of interaction between variables by probability. BN $B=\{G, P\}$ are defined by a directed graph $G(G=\langle\mathrm{X}, \mathrm{E}\rangle$ is a circuit in $X$ and $E$ is the set of arcs), a probability space $P=(\Omega, p)$ and a set of random variable $X=\left\{X_{1}, X_{2}, \ldots, X_{n}\right\}$. Here $\Omega$ is the probability of the universe and $p$ symbolizes all the random variables $X$ such as

$$
p\left(X_{1}, X_{2}, \ldots, X_{n}\right)=\prod_{i=1}^{n} p\left(X_{i} \mid P_{a}\left(X_{i}\right)\right)
$$

where $P_{a}\left(X_{i}\right)$ is the set of all ancestor nodes $X_{i}$ in $G$.
DBN includes a series of time slices and each one is composed by a SBN, it satisfies the first order Markov condition and the topology structure does not change over time. Define a pair $\left(B_{0}, B_{-r}\right)$ as the DBN, here $B_{0}$ represents the initial network structure on the states, $B_{-r}$ is the model of DBN transmission network structure. $T_{u}=\left\{\left[t_{0}, t_{1}\right), \cdots,\left[t_{i-1}, t_{i}\right), \cdots,\left[t_{n-1}, t_{n}\right),\left[t_{n}, \infty\right)\right]\right\}$ are time slices. For road traffic flow, we can use GPS information and travel confidence time to divide sections, each section can be divided into upstream and downstream topological relationship. The time $t+1$ state of traffic depends on the estimated downstream traffic status of the section and upon the previous time $t$ traffic states of the section. These two factors are the main factors that affect their traffic flow. Therefore, the following relations can be defined:

$$
P\left(O_{c, t+1} \mid O_{c, t}, O_{c+1, t+1}^{(1)}, O_{c+1, t+1}^{(2)}, \ldots, O_{c+1, t+1}^{(n)}\right)
$$

Here, $O_{c}$ indicates the road status evaluation index provided by road sections according to the third party Internet traffic condition big data platform. The roads are divided into 1 (serious congestion), 2 (congestion), 3 (slow), 4 (smooth) four states as in section 3 (Table 1). $c$ represents this section, $c+1$ represents the downstream section of this section, the subscript $t$ and $t+1$ represent the current time and the next (predict) time, superscript (1), (2)... (n) representing all downstream sections of this section. The local network structure shown in Figure 2 can be formed:
![img-2.jpeg](img-2.jpeg)
(a) $P\left(O_{c, t+1} \mid O_{c+1, t+1}^{(1)}, O_{c+1, t+1}^{(2)}, \ldots, O_{c+1, t+1}^{(n)}\right)$
![img-3.jpeg](img-3.jpeg)
(b) $P\left(O_{c, t+1} \mid O_{c, t}\right)$

Figure 2 Local Bayesian network graph

Combining the above local structures into a static BN structure, extending to different time slices, the following figure is a DBN structure diagram on two time slices (Figure 3)

$$
t+1
$$

![img-4.jpeg](img-4.jpeg)

Figure 3 Dynamic Bayesian network
The algorithm estimates the maximum likelihood of each node in Bayesian network by maximizing likelihood function. Set training data set $O=\left\{O_{1}, O_{2}, \ldots, O_{m}\right\}$, then the likelihood function ${ }^{[17]}$ can be expressed as

$$
L=\sum_{i=1}^{n} \sum_{j=1}^{m} \log P\left(X_{i} \mid P_{a}\left(X_{i}\right), O_{m}\right)
$$

When the conditional probability distribution is discrete, define $\theta_{i, j, k}=P\left(X_{i}=k \mid P_{a}\left(X_{i}\right)=j\right)$, then likelihood function is rewritten as

$$
\begin{aligned}
L= & \sum_{i} \sum_{m} \log \prod_{j, k} \theta_{i, j, k}^{I_{i, j, k, m}}=\sum_{i} \sum_{m} \sum_{j, k} I_{i, j, k, m} \log \theta_{i, j, k} \\
& =\sum_{i, j, k} \sum_{m} I\left(X_{i}=k, P_{a}\left(X_{i}\right)=j \mid O_{m}\right) \log \theta_{i, j, k}
\end{aligned}
$$

Here

$$
I_{i, j, k, m}=\left\{\begin{array}{cc}
1 & \text { in } O_{m}\left(X_{i}=k, P_{a}\left(X_{i}\right)=j\right) \\
0, & \text { others }
\end{array}\right.
$$

$\sum_{m} I\left(X_{i}=k, P_{a}\left(X_{i}\right)=j \mid O_{m}\right)$ records the number of times in historical data. The maximum likelihood estimation of $\theta_{i, j, k}$ can be obtained by using Lagrange multiplier method.

$$
\tilde{\theta}_{i, j, k}=\frac{\sum_{m} I\left(X_{i}=k, P_{a}\left(X_{i}\right)=j \mid O_{m}\right)}{\sum_{m} \sum_{k} I\left(X_{i}=k, P_{a}\left(X_{i}\right)=j \mid O_{m}\right)}
$$

Introduce two variables $\delta$ and $\varphi$, define the maximum probability that all downstream congestion states in the current section are $i$ at time $t+1$, and $j$ at time $t$ at upstream

$$
\delta_{O_{i, t+1}}(i)=\max _{1 \leq i, j \leq 4} p\left(O_{i, t+1}=i \mid O_{i, t}=j, O_{i+1, t+1}^{(1)}, O_{i+1, t+1}^{(2)}, \cdots, O_{i+1, t+1}^{(n)}\right)
$$

The state with the maximum probability of congestion state for all downstream state $i$ at time $t+1$ and current section state $j$ at time $t$ is

$$
\varphi_{O_{c, t+1}}(i)=\arg \delta_{O_{c, t+1}}(i)
$$

Where

$$
\begin{aligned}
p\left(O_{c, t+1} \mid\right. & \left.O_{c, t}, O_{c+1, t+1}^{(1)}, O_{c+1, t+1}^{(2)}, \cdots, O_{c+1, t+1}^{(n)}\right) \\
= & \frac{p\left(O_{c+1, t+1}^{(1)}, O_{c+1, t+1}^{(2)}, \cdots, O_{c+1, t+1}^{(n)}, O_{c, t} \mid O_{c, t+1}\right)}{p\left(O_{c, t}\right) p\left(O_{c+1, t+1}^{(1)}\right) p\left(O_{c+1, t+1}^{(2)}\right) \cdots p\left(O_{c+1, t+1}^{(n)}\right)} \\
= & \frac{\prod_{i=1}^{n} P\left(O_{c+1, t+1}^{(i)} \mid O_{c, t+1}\right) P\left(O_{c, t} \mid O_{c, t+1}\right) P\left(O_{c, t+1}\right)}{P\left(O_{c, t}\right) \prod_{l=1}^{n} P\left(O_{c+1, t+1}^{(l)}\right)}
\end{aligned}
$$

# 5. Experimental Result 

The above DBN model is used for prediction of traffic congestion diffusion, it can predict traffic congestion state using the DBN model. In this section, we will give experimental results. The research area is a road network located in Shenzhen, China. FCD based on a GPS acquisition system was available. The position and velocity feedback of a single vehicle is detected every 2 minutes. For FCD in this paper, we use the average speed algorithm in section 2 to obtain the average speed in 2 minutes to one section. According to the road condition monitoring and evaluation data provided by the thirdparty Internet large data platform, the state of road traffic can be observed. We selected a links Qiao Xiang routes West to East as a test road, as shown in Figure 4. Based on the DBN model in this paper, input variables for prediction traffic congestion diffusion model consist the topological structure of road network and their traffic state.
![img-5.jpeg](img-5.jpeg)

Figure 4 Qiao xiang routes West to East
Integrating Internet traffic data and FCD, Qiao xiang routes West to East, which road level is classified into the third level according to the Internet traffic condition data. The seven-day data from March 25, 2018 to March 31, 2018 can be used to classify road conditions according to road conditions. Data shows that 06:00 and 06:12 began to slow down and severe congestion in March 31, 2018. Therefore, the DBN model is selected as the initial state for road condition prediction. The experimental results are shown in table 2 and 3 .

Table 2 Traffic congestion prediction table (part of data) based on the initial state of 06:00 on March 31 for a certain section


During the period of 06:00-06:08, the section appears slow-moving. The dissipation prediction of the section is carried out by using the DBN model. From table 2, the predicted results are the same as those given by the Internet.
Table 3 Traffic congestion prediction table (part of data) based on the initial state of 06:12 on March 31 for a certain section


As shown in Table 3, during the 06:12-06:22 period, the road was suddenly seriously congested, and it can be assumed that an emergency occurred. We use the DBN model to predict the dissipation of the section. According to the predicted state results, the state of the road becomes unblocked at 06:22, that is, the congestion time lasts for 10 minutes, which is the same as the state given by the Internet road conditions, indicating that the model is feasible. In the course of the experiment, we found that the given FCD data in Shenzhen can be used to predict the vehicle dissipation, the prediction accuracy of the congestion dissipation time is very high, can reach $100 \%$. But the current data can not predict sudden congestion. If the training data is large enough, the prediction accuracy will be more accurate. We will use this model in Guiyang in the future ${ }^{[18]}$.

# 6. Conclusion 

In this work, we proposed the dynamic Bayesian network model into the road congestion state prediction according to the time-varying characteristics of traffic flow, which can roughly predict the traffic congestion state and dissipation time at the next moment, and take timely measures to alleviate congestion, so as to provide a basis for a traffic control. The prediction results show that the DBN model is feasible in predicting vehicle flow state and dissipation time, but it still needs further optimization and improvement. DBN prediction model in this paper can provide drivers with the shortest and less congestion paths and establish an intelligent management recommendation system. It can provide how long the traffic congestion will diffuse in one section. At present, the theoretical knowledge can not meet the needs of urban traffic, so there is no efficient method or model to address the problem of urban traffic congestion at home and abroad. In the face of this problem, the future urban traffic problems also need the corresponding management departments to increase efforts to regulate and control, more detailed study of the formation of the law of traffic flow and targeted guidance strategies.

## Acknowledgments

This work was financially supported by Guizhou university, Guizhou Provincial Key Laboratory of Public Big Data Guizhou Guiyang, China 2017BDKFJJ012 fund.
