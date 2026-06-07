# Article 

## A New Dynamic Fault Tree Analysis Method of Electromagnetic Brakes Based on Bayesian Network Accompanying Wiener Process

Jihong Pang ${ }^{1}$, Jinkun Dai ${ }^{2}$, Chaohui Zhang ${ }^{2}$, Hongyong Zhou ${ }^{1}$ and Yong Li ${ }^{2, * *}$


#### Abstract

check for updates Citation: Pang, J.; Dai, J.; Zhang, C.; Zhou, H.; Li, Y. A New Dynamic Fault Tree Analysis Method of Electromagnetic Brakes Based on Bayesian Network Accompanying Wiener Process. Symmetry 2022, 14, 968. https://doi.org/10.3390/ sym14050968

Academic Editors: Piao Chen and Ancha Xu


Received: 9 April 2022
Accepted: 4 May 2022
Published: 9 May 2022
Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## (0)

Copyright: (c) 2022 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 College of Business, Shaoxing University, Shaoxing 312000, China; pjh@usx.edu.cn (J.P.); zhouhy@usx.edu.cn (H.Z.)
2 College of Mechanical and Electrical Engineering, Wenzhou University, Wenzhou 325035, China; 194611471207@stu.wzu.edu.cn (J.D.); 20461439068@stu.wzu.edu.cn (C.Z.)

* Correspondence: lyre@wzu.edu.cn; Tel.: +86-577-8668-9138


#### Abstract

Product fault diagnosis has always been the focus of quality and reliability research. However, a failure-rate curve of some products is a symmetrical function, the fault analysis result is not true because the failure period of the products cannot be judged accurately. In order to solve the problem of fault diagnosis, this paper proposes a new Takagi-Sugeno (T-S) dynamic fault tree analysis method based on a Bayesian network accompanying the Wiener process. Firstly, the top event, middle event, and bottom event of the product failure mode are determined, and the T-S dynamic fault tree is constructed. Secondly, in order to form the Bayesian network diagram of the T-S dynamic fault tree, the events in the fault tree are transformed into nodes, and the T-S dynamic gate is also transformed into directed edges. Then, the Wiener process is used to model the performance degradation process of the stationary independent increment of the symmetric function distribution, and the maximum likelihood estimation method is applied to estimate the unknown parameters of the degradation model. Next, the product residual life prediction model is established based on the concept of first arrival time, and a symmetric function of failure-rate curve is obtained by using the product failure probability density function. According to the fault density function derived from the Wiener process, the reverse reasoning algorithm of the Bayesian network is established. Combined with the prior probability of the bottom event, the posterior probability of the root node is calculated and sorted as well. Finally, taking the insufficient braking force of electromagnetic brakes as an example, the practicability and objectivity of the new method are proved.


Keywords: Bayesian network; Wiener process; symmetric function; T-S dynamic fault tree; electromagnetic brakes

MSC: 62 P30

## 1. Introduction

The importance of diagnosis accuracy for equipment faults is a well-known fact. The need for rapid delivery and ever-changing requirements increases the importance of fault diagnosis and analysis processes during product design and manufacture. Moreover, the combination of the traditional data analysis method and the mathematics statistics method improves the veracity and reliability of fault diagnosis [1,2]. According to the viewpoints of the probability and mathematical statistics, the influence of subjective factors on the final diagnosis result could be eliminated. In addition, the methods of intelligence fault diagnosis have developed a new way to ensure the reliability of complex industrial systems [3,4]. On the other hand, the internal structure of the electromagnetic brakes is relatively complex, the coordination accuracy between mechanical structures is relatively high, and the overall failure-curve of the electromagnetic brakes is normally distributed. In addition, the failure

period of some components is not clear once the electromagnetic brakes fail. Therefore, an excellent method of product fault diagnosis, and one worth advocating, can not only deal with complex product structures, but also accurately judge the failure period of parts when the failure-curve is symmetrically distributed. In this paper, based on comprehensive fault diagnosis, the results are synthesized to realize the analysis of the dynamic fault tree, and the reliability of electromagnetic brakes is well evaluated based on the Bayesian network accompanying the Wiener process.

The fault diagnosis of products has always been a key point of research. Scholars also make their own efforts to standardizethe judgment process as much as possible by combining more scientific methods. Ziyun Wang et al. [5] proposed a hierarchical fault diagnosis algorithm based on in-situ filtering for complex systems with multiple fault types. Its advantage is that, for faults that are not in the fault database, they will actively cluster the missing faults and then carry out system analysis. Lei Kou et al. [6] proposed an open circuit fault diagnosis method of insulated gate bipolar transistors (IGBTs) based on knowledge driven and data driven technology, and used Concorde transform (knowledge driven) and random forests (RFs) technology (data driven) to improve the robustness of fault diagnosis classifier. Xiaoyue Yang et al. [7] proposed an optimal fractional transient fault (TF) diagnosis method to overcome the noise problem in weak fault feature extraction. This method can suppress the background noise, amplify the fault part of the signal, and locate the fault component by using kurtosis and fault duration. Liangjun Feng et al. [8] proposed a data-driven fault analysis method when there is no target fault sample for model training. This method learns to use the human-defined fault description instead of the collected fault samples to determine the fault category and can diagnose the target fault according to the defined fault description without any additional data-based training. In addition, some scholars have also used constructive methods, such as the combination of fault tree analysis and Monte Carlo simulation [9], and the combination of fault tree analysis and the Bayesian network [10]. The above methods can greatly ensure the objectivity of judgment.

Fault tree analysis (FTA) is a deductive failure analysis method from top to bottom. It uses Boolean logic to combine low-order events and analyze the unwanted states in the system. It is characterized by intuitive thinking and strong logic. It can perform qualitative analysis or quantitative analysis. At present, as a classic method, FTA is applied in many fields. Bekir Sahin et al. [11] extended the fuzzy fault tree analysis by embedding the fault tree structure based on ontology. The ontology-based method allows advanced analysis based on rich domain knowledge. Traditional and rule-based methods are used to calculate the fault probability and analyze the fault tree. Xue Lei et al. [12] applied FTA to supply chain risk analysis, not only in natural sciences, but also in humanities. However, with the development of history, itslimitations appear. The relationship between events based on the fuzzy tree cannot be expressed by the traditional fuzzy tree, so the relationship between events based on the fuzzy tree was proposed by Hu Gen in 2008. Since then, the T-S fault tree has been pursued and improved by many scholars, making it gradually perfect in the field of fault judgment. Zhen Li et al. [13] proposed an automatic system modeling and fault analysis method based on AltaRica, and the automatic fault analysis is correct and efficient in the detailed example. Zhuqing Bi et al. [14] proposed a new method combining the T-S fuzzy gate fault tree with the Bayesian network and verified the feasibility of this method through the fault diagnosis model of pumping unit rotor. Yingkui Gu et al. [15] have applied a probabilistic model test and discrete-time Markov chain to fault tree analysis, and the logic gate in the fault tree is transformed into a discrete-time Markov chain. The Markov decision process is used to simulate the uncertain behavior of the system in the unknown environment. Chen Wu et al. [16] proposed an evaluation method for the possibility of tunnel collapse in drilling and blasting construction based on the T-S fuzzy fault tree and used the T-S fuzzy gate instead of a traditional logic gate to describe the relationship between events. In addition, some scholars have developed a dynamic fault tree for fault judgment based on the idea of the control rules of the T-S fault tree. These methods can be applied to some products with multiple states and the application area is

more targeted [17,18]. No matter what kind of fault tree analysis methods, they are judged based on the failure density function of parts. Therefore, it is necessary to fit or deduce the failure density function before fault tree analysis.

On the one hand, the Bayesian network is an extension of the Bayes method, also known as a belief network. It is one of the most effective theoretical models in the field of uncertain knowledge expression and reasoning. Important information regarding various parts can be obtained through the reverse reasoning algorithm of the Bayesian network. Hongqing Liao et al. [19] have applied the Bayesian network reasoning technology combined with the pan function theory to establish grey Bayesian network reasoning and predict the development trend of the system through flight time. Zhengxing Xiao et al. [20] used the Bayesian network theory to establish an independent intelligent decision-making model of traffic lights based on the Dynamic Bayesian network. It can be seen from the above literature that the Bayesian network is widely used in the field of reasoning and can also objectively reflect the situation of each node. The electromagnet plays an important part in automatic control. In the long-term operation process, due to the influence of the complex mechanical structure and other uncertain factors of the electromagnet, its performance will inevitably deteriorate. Therefore, when a fault occurs, the electromagnet will cause huge casualties and property losses. At present, due to the randomness of the residual life and degradation process of products, the reliability evaluation model based on performance degradation data is mostly used for this kind of product [21,22]. These common performance degradation models include the gamma process model [23], the inverse Gaussian process model [24], and the Wiener process model [25].

On the other hand, a large number of the most used degradation models are found in statistical mechanics, such as the Wiener process, gamma process, inverse Gaussian process, compound Poisson process, and so on [26,27]. Compared with other stochastic processes, the Wiener process has been widely used in the field of reliability degradation modeling because of its good analytical properties. The Wiener process has the advantage of being able to describe many types of product degradation processes. Pingping Wang et al. [28] proposed a variable-point Wiener process with measurement error to fit the two-phase degradation path of organic light-emitting diodes (OLED) and derived the failure time distribution. Xiaolin Wang et al. [29] proposed a degenerate model that covers a variety of models based on the Wiener process as their limit cases, and then proposed a two-stage method for estimating the unknown parameters. Xiaosheng Si et al. [30] proposed a degenerate model and recursive filtering algorithm based on the Wiener process, used recursive filters to update the drift coefficients in the Wiener process, and used the expectation-maximization (EM) algorithm to update all unknown parameters. Shengjin Tang et al. [31] proposed a prediction method for lithium-ion batteries based on a Wiener process with measurement error and presented a truncated normal distribution (TND) modeling approach to estimate the degradation state. Baoping Cai et al. [32] used the Wiener process to describe the degradation process of the system, and combined $n$ sets of performance degradation monitoring data and historical prediction data to establish the dynamic Bayesian networks' (DBNs) model of system performance degradation. Han Wang et al. [33] applied the improved Wiener model to thrust ball bearings, where the drift and diffusion parameters of the model were adaptive with the update of monitoring data. Ancha Xu et al. [34] proposed a new bivariate degradation model based on the Wiener process, which can describe the common factor affecting the degradation of the two performance characteristics and unit-to-unit variation, simultaneously. Zeyi Huang et al. [35] proposed an adaptive oblique Wiener model that was more flexible than traditional stochastic process models to model the degradation drift of industrial equipment.

In order to carry out failure diagnosis on electromagnetic brakes, a new dynamic fault tree analysis method based on the Bayesian network and accompanying the Wiener process is presented. The rest of this paper is organized as follows: The methodology and the objectives of this study are proposed in Section 2. Firstly, the fault diagnosis process based on the Bayesian network and the T-S dynamic fault tree analysis is presented. Secondly, the inference model based on the Bayesian network is discussed and the algorithm based

on the model is also approved. Then, a derivation process of fault probability density function of electromagnetic brakes based on the Wiener process is introduced. Next, the T-S dynamic fault tree analysis method is used to solve the actual existence problem of electromagnetic brakes. Furthermore, the input and output analysis of algorithm of the T-S dynamic gate is presented. Section 3 takes the insufficient braking force of electromagnetic brakes as an example and the approved method is used to judge the fault. Finally, some useful conclusions are summarized in Section 4.

# 2. Methodology 

The main contributions of this paper are proposing the new dynamic fault tree analysis method of electromagnetic brakes based on the Bayesian network and accompanying the Wiener process. Firstly, the dynamic fault tree method can describe the dynamic products' performance. Further, the processes of modeling are easy, and the structure of model is clear and available. Based on the dynamic analysis, the results of the products' quality and reliability are synthesized to realize the analysis of a modular fault tree. Moreover, compared with the traditional fault tree, the T-S dynamic fault tree can describe the fault modes with multiple time sequences and multiple logical relationships, which is more in line with the needs of modern mechanical structure fault diagnosis. However, it is more suitable for structures with fewer parts than traditional products. If there are many products parts, the T-S dynamic fault tree analysis method contains a large amount of calculation and is not suitable for ordinary engineers to operate.

On the other hand, a class of optimal stochastic control problems relating to the Wiener process is presented, and the stochastic process models are established in this study. The characteristic of the Wiener process is that the trend after any point on the curve is only related to the point value, but independent of the previous value. Therefore, the Wiener process has time translation in variance, which is very helpful to determine the failure period of a normal distribution failure-curve. Based on the advantages of the above two aspects requests, this paper combines the advantage of the two methods of the T-S dynamic fault tree analysis and the Wiener process. Firstly, the T-S dynamic fault tree analysis method is used to decompose a large subsystem or mechanism until it is decomposed into a small part. Secondly, the interaction relationship of parts of the whole product system, the top event, middle event, bottom event, and the T-S dynamic door of failure mode is determined in turn. Then, the factors mentioned above are connected to form a T-S dynamic fault diagram. Next, the bottom event, intermediate event, top event, and T-S dynamic gate are separately transformed into root node, root node, leaf node, and directed edge. After the above steps are completed, the Bayesian network diagram of T-S dynamic fault tree can be drawn. The detailed process is shown in Figure 1.

According to the figure above, the performance degradation data of electromagnets are obtained experimentally, and the reliability of the performance degradation process with smooth independent increments satisfying the symmetric function distribution is modeled using the Wiener process. The maximum likelihood estimation method is used to estimate the unknown parameters of the degradation model, the diagnostic model of the remaining product life is determined, and the product failure probability density function with the failure-rate curve as a symmetric function can be obtained. Thus, the posterior probability of the root node can be calculated and ranked according to the inverse inference algorithm of Bayesian networks combined with the failure probability density function. After completing the fault determination, the faulty system is repaired in a targeted manner. The derivation process of failure probability density function for each basic event is shown in Figure 2.

![img-0.jpeg](img-0.jpeg)

Figure 1. Fault diagnosis based on the Bayesian network and the T-S dynamic fault tree analysis.

# 2.1. Bayesian Network 

A Bayesian network is one of the most efficient methods in uncertainty environment. Further, Bayesian network is a model combining probability statistics and graph theory [36,37]. The nodes of the Bayesian network represent the random variables related to the problem, and the directed arc between nodes represents the dependence between variables. Each node is attached with the probability distribution table of its random variables. Moreover, the root node is attached with its edge distribution, and the non-root node is attached with the conditional probability distribution table. Therefore, it can be well used the reasoning principle of the Bayesian network and the characteristics of displaying dependency of nodes to reflect the relationship between influencing factors and failure modes. In addition, the quantitative relationship between parent nodes and their offspring nodes can be expressed by conditional probability, and the importance of each influence factor can also be calculated.

![img-1.jpeg](img-1.jpeg)

Figure 2. Derivation of fault probability density function based on the Wiener process.
Furthermore, the establishment of the Bayesian network topology is established based on the selection of node random variables and the logical relationship of nodes, as shown in Figure 3. Considering that $n$ influencing factors are represented by root node of $X_{n}$, intermediate events or top events are represented by $Y_{n}$, and the connecting line represents the input and output algorithm of the Bayesian network [38]. Through the Bayesian network, we can not only calculate the failure rate of top events, but also reverse the importance of each basic event through top event failure. This article introduces a way to take advantage of the Bayesian network approach which better than other simulation optimization methods.
![img-2.jpeg](img-2.jpeg)

Figure 3. Schematic diagram of the Bayesian network structure.

# 2.2. Failure Probability Density Function with Wiener Process 

A class of optimal stochastic analysis problems relating to a Wiener process is presented in this paper. Further, the primary probability function, the failure probability, failure probability density, reliability, and failure rate have been first discussed. During the operation of electromagnet, the electromagnetic force shows a downward trend as a whole. Due to the influence of uncertain factors such as coil aging, uneven wear of movable iron core, ambient temperature change, and electromagnetic force shows a characteristic of non-monotonic decline. As well, these influence factors are in line with the characteristics of non-monotonic performance degradation as described by the Wiener process. Moreover, a finite element model of the change with clearance of an energized coil or filament barrier was established to analyze the non-monotonous attenuation of electromagnetic force [39]. Therefore, the Wiener process is also used to describe the performance degradation process of the electromagnet's electromagnetic force.

In addition, the Wiener process is a widely used stochastic process model which can be used to model the performance degradation process of a stationary independent Gaussian increment. If a continuous random time process obeys the Wiener process, then $X(t)$ will satisfy the following conditions:
(1) If $X(0)=0, X(0)$ is continuous at $t=0$;
(2) For any time between $t$ and $t+\Delta t$, the performance degradation increment $\Delta X(t)=X(t+\Delta t)-X(t)$ obeys the normal distribution;
(3) For any different time, interval of $\left[t_{1}, t_{2}\right],\left[t_{3}, t_{4}\right], t_{1}<t_{2} \leq t_{3}<t_{4}$. Increment $X\left(t_{4}\right)-X\left(t_{3}\right)$ and $X\left(t_{2}\right)-X\left(t_{1}\right)$ are independent of each other.
According to the above properties, the performance degradation model of the electromagnet based on the Wiener process is established. Assuming that $X(t)$ is the performance degradation amount of the permanent magnet brake at time $t$, the degradation process of electromagnet's electromagnetic force can be expressed as [40]:

$$
X(t)=x_{0}+\mu t+\sigma_{B} B(t)
$$

where, $x_{0}$ is the initial value of electromagnetic force degradation; $\mu$ is the drift parameter, which represents the degradation rate of the electromagnetic force; $\sigma_{B}$ is the diffusion parameter, which indicates the influence of the internal structure of the electromagnet and external factors on the performance during the degradation process; $B(t)$ is the standard Brownian motion, and $B(t) \sim N(0, t)$, which represents the randomness of the degradation process of the electromagnet.

If the degradation process of the electromagnetic force's performance of the electromagnet meets Equation (1) and the failure threshold of the electromagnetic force of the electromagnet is $V$, the service life $T$ of the electromagnet is the time when the degradation amount of the electromagnetic force's performance reaches failure for the first time [41]:

$$
T=\inf \{t \mid Y(t) \geq V, t>0\}
$$

According to the electromagnet lifetime defined in Equation (2), and with the inverse Gaussian distribution of the first reach time $T$ of the unitary Wiener process, combining Equations (1) and (2), the residual life probability density function of the electromagnet at moment $\tau$ can be derived as [42]:

$$
f_{T_{1}}(t)=\frac{V-x_{\tau}}{\sqrt{2 \pi \sigma^{2} t^{2}}} \exp \left[-\frac{\left(V-x_{r}-\mu t\right)^{2}}{2 \sigma^{2} t}\right]
$$

where, $x_{\tau}$ by $\tau$ degradation amount of electromagnet's electromagnetic force performance at time; $V$ is the electromagnetic force failure threshold of the electromagnet.

Assuming that the initial value of the electromagnet's electromagnetic force $X\left(t_{0}\right)=0$, the quantity sequence is carried out to time $\left(t_{0}, t_{1}, t_{2}, \cdots, t_{n}\right)$ from $\left(X\left(t_{0}\right), X\left(t_{1}\right), X\left(t_{2}\right), \cdots, X\left(t_{n}\right)\right)$

based on the electromagnet's electromagnetic force degradation experiment, and $\Delta X_{i}=X\left(t_{i}\right)-X\left(t_{i-1}\right)$ is the electromagnetic force at time $t_{i-1} \rightarrow t_{i}$. The degradation amount of the electromagnetic force between $I$ can be known from the nature of the Wiener process:

$$
\Delta X_{i} \sim N\left(\mu \Delta t_{i}, \sigma^{2} \Delta t_{i}\right)
$$

where, $\Delta t_{i}=t_{i}-t_{i-1}, i=1,2, \cdots, n$.
Next, the parameters of the degradation model are estimated from the electromagnetic force data samples of electromagnets $\mu$ and $\sigma^{2}$. The likelihood function of torque degradation can be obtained as follows:

$$
L\left(\mu, \sigma^{2}\right)=\prod_{i=1}^{n} \frac{1}{\sqrt{2 \pi \sigma^{2} \Delta t_{i}}} \exp \left[-\frac{\left(\Delta x-\mu \Delta t_{i}\right)^{2}}{2 \sigma^{2} \Delta t_{i}}\right]
$$

Then, the Pair likelihood function $L\left(\mu, \sigma^{2}\right)$ takes $L n$ from both sides to obtain:

$$
\ln L=\sum_{i=1}^{n}\left[-\frac{\ln \Delta t_{i}}{2}-\ln \sigma-\frac{\left(\Delta X_{i}-\mu \Delta t_{i}\right)^{2}}{2 \sigma^{2} \Delta t_{i}}\right]
$$

Moreover, $\hat{\mu}$ partial derivation is obtained:

$$
\hat{\mu}=\frac{1}{n} \sum_{i=1}^{n} \frac{\Delta X_{i}}{\Delta t_{i}}
$$

In addition, $\hat{\sigma}$ partial derivation is also obtained:

$$
\hat{\sigma}=\left[\frac{1}{n} \sum_{i=1}^{n} \frac{\left(\Delta X_{i}-\hat{\mu} \Delta t_{i}\right)^{2}}{\Delta t_{i}}\right]^{\frac{1}{2}}
$$

# 2.3. T-S Dynamic Fault Tree Analysis Method 

The T-S fault tree analysis is one of the most effective means for the safety and reliability analysis of a dynamic system. Compared with a traditional fault tree analysis, the T-S fault tree analysis can describe the dynamic failure relationship of the system and describe the actual failure form through a logic diagram, which makes it clearly visualized, specific, convenient and simple. A T-S fault tree contains basic events, intermediate events, top events, and T-S dynamic gates. The events describe the components of the system and the T-S dynamic gates of the logical relationships among these components. For example, in Figure 4, $Y$ is the top event, $Y 1-Y 3$ is the intermediate event, $X 1-X 4$ is the basic event, and G1-G4 is the T-S dynamic gate [43].

Suppose that the working time $T$ of the system is divided into $N$ parts, and the time of each interval is $I=\frac{T}{m}$, which is, respectively, denoted as $[(0, I),(I, 2 I), \cdots,((N-1) I, N I),(N I, \cdots)]$. Basic event $X i$ in time period $j_{i}$ fault state is $S_{i}^{\left(a_{i}\right)}$, where $i=1,2, \cdots n ; j_{i}=1,2, \cdots$, $N, N+1 ; a_{i}=1,2, \cdots, k_{i} ;$ and $0 \leq S_{i}^{(1)}<S_{i}^{(2)}<\cdots<S_{i}^{\left(k_{i}\right)} \leq 1$; the top event $Y i$ in time period $j_{i}$ fault state is $S_{i}^{\left(b_{i}\right)}$, where $i=1,2, \cdots n ; j_{i}=1,2, \cdots, N, N+1 ; b_{i}=1,2, \cdots, k_{i}$; and $0 \leq S_{i}^{(1)}<S_{i}^{(2)}<\cdots<S_{i}^{\left(k_{y}\right)} \leq 1$. Moreover, the T-S dynamic gate has two kinds of logic rules, one is defined according to the time of the event, and the other is defined according to the sequence of the event. Taking two operating states and three time periods of two basic events as an example, the T-S dynamic gate is shown in Table 1 based on the time of event occurrence.

![img-3.jpeg](img-3.jpeg)

Figure 4. T-S fault tree.
Table 1. Logical rules of occurrence time.


At the same time, the fault status of superior event $Y$ in time periods 1,2 and 3 is $P_{1}^{Y^{1}}, P_{1}^{Y^{2}}, P_{1}^{Y^{3}}$. Similarly, these rules are shown in Table 2 if the sequence of events is used.

Table 2. Logical rules of event occurrence.


# 2.4. Algorithm of T-S Dynamic Gate 

1. Input analysis algorithm of T-S dynamic gate

Since there are two kinds of logic rules for the T-S dynamic gate, the input algorithms under the two kinds of logic rules are given. Firstly, assume that the failure density function of $X i$ is $f_{i}(t)$. Then, the probability of fault state of $X i$ in time period $j_{i}$ in input rule $l$ is [44]:

$$
P_{(l)}\left(x_{i}^{j_{i}}\right)=\int_{(j_{i}-1) l}^{j, l} f_{i}(t) d t
$$

where $j_{i}$ is time period, and $i=1,2, \cdots, n$.

Then, the occurrence probability of rule $l$ in time state is as follows:

$$
P_{(l)}^{\prime}=\prod_{j_{i}=1}^{N+1} \prod_{i=1}^{n} P_{(l)}\left(x_{i}^{j_{i}}\right)
$$

where $P_{(l)}\left(x_{i}^{j_{i}}\right)$ is the same as Equation (9).
Next, the occurrence probability of rule $l$ in event state is as follows:

$$
P_{(l)}^{\prime}=\prod_{i=1}^{n} P_{(l)}\left(x_{i}^{j_{i}}\right)
$$

The same meaning fits in Equations (10) and (11).
2. Output analysis algorithm of T-S dynamic gate

The top event occurs in time period $j_{i}$ of fault state $y_{i}^{\left(j_{i}\right)}$ is $S_{i}^{\left(k_{j}\right)}$ of probability, which can be shown in the following [45]:

$$
\left\{\begin{array}{c}
P\left(y^{\left(j_{p}\right)}=S_{y}^{1}\right)=\sum_{l=1}^{r} P_{(l)}^{\prime} P_{(l)}\left(y^{\left(j_{p}\right)}=S_{y}^{1}\right) \\
P\left(y^{\left(j_{p}\right)}=S_{y}^{2}\right)=\sum_{l=1}^{r} P_{(l)}^{\prime} P_{(l)}\left(y^{\left(j_{p}\right)}=S_{y}^{2}\right) \\
\vdots \\
P\left(y^{\left(j_{p}\right)}=S_{y}^{k_{p}}\right)=\sum_{l=1}^{r} P_{(l)}^{\prime} P_{(l)}\left(y^{\left(j_{p}\right)}=S_{y}^{k_{p}}\right)
\end{array}\right.
$$

where $P_{(l)}\left(y^{\left(j_{p}\right)}=S_{y}^{k_{p}}\right.$. is the time period $j_{i}$ of $y$. with rule $l$, the fault state $y_{i}^{\left(j_{i}\right)}$. of rule $l$. is the probability of $S_{i}^{\left(k_{i}\right)} \cdot P\left(y^{\left(j_{p}\right)}=S_{y}^{k_{p}}\right)$. is the time period $j_{i}$. of $y$, and the fault state $y_{i}^{\left(j_{i}\right)}$. is the probability of $S_{i}^{\left(k_{p}\right)}$.
3. Reverse inference algorithm of Bayesian networks

A Bayesian network has the property of bidirectional inference, namely forward inference and reverse inference. Forward inference can calculate the system reliability that may be presented according to the specified design and assembly, and reverse inference refers to the importance of factors causing the failure, which can be calculated backwards in the failure system.

In this paper, we suppose that the posterior probability $P\left(y_{N}^{j_{N}}=1 / x^{j_{p}}=1\right)$ of the root node $y_{i}$ in the multi-time and two-state state is [46]:

$$
P\left(y_{N}^{j_{N}}=1 \mid x^{j_{p}}=1\right)=\frac{P\left(y_{N}^{j_{N}}=1, x^{j_{p}}=1\right)}{P\left(x^{j_{p}}=1\right)}
$$

where $P\left(x^{j_{p}}=1\right)$ represents the failure probability of $x$ in the $j_{x}$ period, $x$ is the base event of root node $y_{i}$.

# 3. A Case Study 

Electromagnetic brakes are a kind of electromagnetic force generated by the energized coil to drive the upper and lower brake pads, in order to clamp the brake disc installed on the moving device to realize braking. Their biggest advantage over other mechanical structures is that they can control the execution and strength of the action without manual operation. In this study, a kind of disc electromagnetic brake developed by a company in China's Zhejiang province is illustrated as an example. Electromagnetic brakes are mainly used for the arm of the robot. So, the auxiliary computer control system breaks the robot. The structure diagram of electromagnetic brakes is shown in Figure 5, and the physical

drawing is shown in Figure 6. According to the analysis of the working principle and the structure of the electromagnetic brake, the reason for the long braking time may be the improper use of brake pad materials, excessive roughness of the brake pad surface, excessive roughness of brake discs, and braking time. Thus, the new approved method is used to accurately find out the fundamental factors which affecting the braking time and corresponding parts.
![img-4.jpeg](img-4.jpeg)

1-strut, 2-spring, 3-screw, 4-upper brake pad, 5-brake disc, 6-lower brake pad, 7-coil, 8-stator

Figure 5. Structural diagram of disc electromagnetic brakes.
![img-5.jpeg](img-5.jpeg)

Figure 6. Physical drawing and parts drawing of electromagnetic brake.
Firstly, the engineers conducted an electromagnetic force attenuation test on the electromagnetic brakes. The schematic diagram of the test platform is shown in Figure 7, and the physical diagram is shown in Figure 8.

![img-6.jpeg](img-6.jpeg)

Figure 7. Test platform diagram.
![img-7.jpeg](img-7.jpeg)

Figure 8. Physical drawing of test platform.
In Figures 7 and 8, we placed the electromagnetic brake on the test platform and ran it with the power on. Then, the torque sensor uploaded the collected data to the computer. Next, we calculated the electromagnetic force through the formula of $W=F * L, W$ is the torque, the unit is $\mathrm{N} \cdot \mathrm{mm}, F$ is the electromagnetic force, the unit is $\mathrm{N}, L$ is the radius of the brake pad, and the unit is mm . The calculated electromagnetic force is shown in Table 3. The instrument models used in the test platform were the JN388 series torque sensor, ECMA series servo motor, PLC control board, PLC data acquisition card, electromagnetic brake and brake working counterweight produced by the company. In Table 3, BT represents the breaking times and EF represents the electromagnetic force.

Table 3. Degradation data of the electromagnet's electromagnetic force.


According to the nature of the Wiener process, the degradation amount of electromagnetic force of the electromagnet must meet the normal distribution. Figure 9 shows the degradation amount of the electromagnet during every other cycle in the degradation process of electromagnetic force.

![img-8.jpeg](img-8.jpeg)

Figure 9. Degradation of electromagnetic force of electromagnetic brakes.
Before modeling the degradation of electromagnetic force performance of the electromagnet, it was necessary to check whether it met normal distribution. The attenuation data of the electromagnetic force was fed into the SPSS software from Table 3, and the descriptive statistical analysis function of the software was used to obtain the $P$ - $P$ test results of electromagnetic force attenuation, as shown in Figure 10. Through the $P$ - $P$ test, it can be seen that the relative incremental cumulative probability of electromagnetic force is basically arranged in a straight line, in line with the characteristics of normal distribution.
![img-9.jpeg](img-9.jpeg)

Figure 10. $P$ - $P$ test of electromagnetic force degradation of electromagnet.
In the next step, we modeled the electromagnetic force performance degradation of the electromagnetic brakes. The electromagnetic force degradation was also analyzed by the K-S analysis method to judge whether it met the normal distribution. Thus, the data test results are shown in Table 4. From the test results, the data distribution conforms to the normal distribution. Therefore, the Wiener process can be used to describe the degradation process of the electromagnetic force of electromagnetic brakes.

Table 4. K-S test for degradation force performance of electromagnetic brakes.


According to the performance degradation data, the performance degradation model of the electromagnet's electromagnetic force is established. The drift coefficient can be obtained from Equation (7) combined with the data in Table 3, $\hat{\mu}$ Estimated value is shown in the following equation:

$$
\hat{\mu}=\frac{1}{n} \sum_{i=1}^{n} \frac{\Delta X_{i}}{\Delta t_{i}}=0.03370
$$

Then, the diffusion coefficient can be obtained from Equation (8), and $\hat{\sigma}$ Estimated value can be obtained using the following equation:

$$
\hat{\sigma}=\left[\frac{1}{n} \sum_{i=1}^{n} \frac{\left(\Delta X_{i}-\hat{\mu} \Delta t_{i}\right)^{2}}{\Delta t_{i}}\right]^{\frac{1}{2}}=0.01841
$$

According to the technical specifications of the electromagnet, the failure threshold of the electromagnetic force of the electromagnet is 7 N . Therefore, the probability density function of the remaining life at the initial time of the electromagnet can be obtained in combination with Equation (3):

$$
\begin{aligned}
f_{T_{1}}(t)=\frac{V-x_{s}}{\sqrt{2 \pi \rho^{2} t^{3}}} \exp \left[-\frac{\left(V-x_{s}-\mu t\right)^{2}}{2 \sigma^{2} t}\right]=\frac{8.68-7-0}{2 * \pi *(0.01841)^{2} * \sqrt{t^{3}}} \exp \left[-\frac{(8.68-7-0.03370 t)^{2}}{2 *(0.01841)^{2} t}\right] \\
=\frac{1.68}{0.00211 \sqrt{t^{3}}} \exp \left[-\frac{(1.68-0.03370 t)^{2}}{0.00067 t}\right]
\end{aligned}
$$

According to the diagnostic steps of the approved method, the T-S dynamic fault tree can be constructed step by step. The top event of this example can be determined with braking time, and the boundary of analysis for the designed product is divided. Thus, the fault information of the system can be collected to consult historical data and find each intermediate event and basic event, which is shown in Table 5.

Table 5. Fault tree model event table for long braking time.


We can acquire the following information from Table 5.
Top Event Y: Long braking time means low braking force.

Intermediate Event Y1: The properties of the brake pad itself have a certain influence on the brake durability, temperature resistance, heat fading and the friction and wear requirements of the brake.

Intermediate event Y2: The brake disc is a part that completes a braking action with upper and lower brake pads. Its effect is to reduce heat dissipation and increase vibration during the braking process.

Basic Event X1: The improper material use of the brake pads affects the maximum speed they are subjected to, as well as increasing the residual magnetic force of the electromagnetic force, which results in the mechanism remaining braked when the power is cut off.

Basic Event X2: Excessive roughness of the brake pad surface increases friction loss with the brake disc, resulting in many hidden costs.

Basic event X3; The surface treatment of the brake disc is uneven, which firstly increases friction loss with brake pads, and secondly affects the performance of the temperature-resistant and heat-dissipating circulation of the whole brake.

Basic Event X4: An overly long braking time of repeated braking tests may lead to results in a thinning of the discs and a downward shift in the axiality of the discs.

Finally, the T-S dynamic gate is used to connect these event symbols, and the fault diagram is confirmed upon re-examination from Figure 2.

In the next stage, the bottom event is transformed into the root node, the intermediate event is transformed into the intermediate node, the top event is transformed into the leaf node, and the T-S dynamic gate is transformed into the directed edge. In addition, the prior probability of collecting the bottom event is shown in Table 6.

Table 6. Event failure rate.


Then, the Bayesian network diagram of the T-S dynamic fault tree is drawn as shown in Figure 11. According to the achievement in research of the above analysis, the posterior probability of the root node can be calculated.
![img-10.jpeg](img-10.jpeg)

Figure 11. Bayesian network diagram.
In this case study, we assumed that the total braking time was $T=1000(\mathrm{~min})$ which was divided into four sections. There were also five value ranges which are represented by $1-5$ numbers in the following:

$$
\{(0,250)(250,500)(500,750)(750,1000)(1000, \cdots)\}
$$

According to Equation (9), the failure probability density function can be calculated in the following:

$$
f_{T_{1}}\left(\lambda_{i}\right)=\frac{1.68}{0.00211 \sqrt{\lambda_{i}{ }^{2}}} \exp \left[-\frac{\left(1.68-0.03370 \lambda_{i}\right)^{2}}{0.00067 t}\right]
$$

Next, the failure probability value of the basic event in each value range can be obtained in Table 7.

Table 7. Failure probability of each basic event in different event segments.


In the next step, we specified the influence law of the basic event and the top event according to the event occurrence rule. The relationship between the basic event $X 1$ and $X 2$ is that once the basic event $X 1$ fails and $X 2$ also fails, the top event fails, and the basic event $X 1$ should directly affect the occurrence of the top event. By the above calculation rules, the conditional probability table between $X 1, X 2$ and $Y 1$ is shown in Table 8.

Table 8. Conditional probability table of $Y 1$.


So similarly, the conditional probability table of $Y 2(Y)$ is shown in Table 9.
Table 9. Conditional probability table of $Y 2(Y)$.


According to Equation (11), Tables 7 and 8, the failure probability of all time periods of intermediate events and top events can be calculated, which is shown in Table 10.

Table 10. Failure probability of intermediate events and top events.


Next, we can calculate the posterior probability of the basic event according to Equation (13). Once $Y$ fails in the fourth time period, the posterior probability of $X 1$ in the first time period can be achieved using the following equation:

$$
\begin{aligned}
& P\left(x_{1}^{1}=1 \mid y^{1}=1\right) \\
& =\frac{P\left(x_{1}^{1}\right) P\left(x_{2}^{4}\right) P\left(x_{3}^{4}\right) P\left(x_{4}^{4}\right)+P\left(x_{1}^{1}\right) P\left(x_{3}^{4}\right) P\left(x_{2}^{4}\right) P\left(x_{4}^{3}\right)+P\left(x_{1}^{1}\right) P\left(x_{2}^{4}\right) P\left(x_{3}^{3}\right) P\left(x_{4}^{3}\right)+P\left(x_{1}^{1}\right) P\left(x_{2}^{3}\right) P\left(x_{3}^{4}\right) P\left(x_{4}^{4}\right)}{P\left(y^{1}=1\right)} \\
& +\frac{P\left(x_{1}^{1}\right) P\left(x_{2}^{5}\right) P\left(x_{3}^{4}\right) P\left(x_{4}^{5}\right)+P\left(x_{1}^{1}\right) P\left(x_{2}^{5}\right) P\left(x_{3}^{5}\right) P\left(x_{4}^{5}\right)}{P\left(y^{1}=1\right)}=0.001356
\end{aligned}
$$

Similarly, the posterior probabilities of other basic events are obtained, as shown in Table 11.
Table 11. Posterior probability of root node in different time periods.


From the posterior probability of each basic event in Table 11, we concluded that the fault should be investigated in the order of $X 4, X 3, X 1$, and $X 2$, which is also the factor with the greatest impact on the top event. In this study, the dynamic fault tree method of electromagnetic brakes based on the Bayesian network accompanying Wiener process is presented to provide decision support for quality engineers and business management staff. Furthermore, this paper will be helpful in that it has a significant capacity to enhance the manager's awareness of quality management and technical analysis capabilities.

# 4. Result Discussion 

A new fault diagnosis method based on the Bayesian network and the Wiener process is proposed in this study, which can better solve the dilemma of fault diagnosis in the working process of electromagnetic brakes. Moreover, the case shows that the approved method is reasonable, scientific, and obtains better effects. In addition, the value of this paper is to build a test platform and use the Wiener process to fit the life-curve of electromagnetic brakes. The example also shows that the new method possesses the advantages of feasibility, effectiveness, and easy control of operation, and it holds important value for engineering application.

On the other hand, according to theoretical and experimental results, we have discovered that the new method is superior to common fault diagnosis methods. If we choose not to apply dynamic fault analysis in the case study, based on the fault rate of each bottom event in the time period in Table 7, it is found that $X 3$ has the highest failure rate of the bottom event, followed by $X 4, X 1$ and $X 2$. The calculation results are different from the analysis of $X 3$ and $X 4$ bottom events. Therefore, the machine test of $X 3$ and $X 4$ bottom events is carried out separately. So, two kinds of brake discs with an uneven surface of roughness Ra 1.6 and Ra 3.2 are selected. Then, we set the braking time to start from 450,000 and increase by 50,000 in turn to obtain the electromagnetic force under various conditions, as shown in Table 12.

Table 12. Test data of brake pads with different roughness.


From the data presented in Table 12, we can see that the unit of electromagnetic force is $N$. For example, 0.02534 is the electromagnetic force when the braking time is $450,000 \mathrm{~s}$ and Ra 1.6. It can be calculated from Table 12 that when the braking time is the same and the roughness is different, the maximum difference of electromagnetic force is recorded as D1, which is $0.00069,0.00172,0.00003$ and 0.00102 in turn, and 0.00069 is the difference of the electromagnetic force of two brake pads with different roughness when the braking time is 450,000 . Similarly, when the roughness is the same and the braking time is different, the maximum difference of the electromagnetic force can also be calculated. It is recorded as D2, which is $0.00638,0.00671$ and 0.00678 in turn. Among them, 0.00638 is the difference of the electromagnetic force between 450,000 and 650,000 braking time when Ra is 1.6. Furthermore, it was easy to acquire calculations through the computer test. Compared with the surface roughness of the brake discs, the braking time had a greater impact on the electromagnetic force. The result shows that the new dynamic fault tree analysis method based on the Bayesian network accompanying Wiener process can be well used in the fault diagnosis of electromagnetic brakes.

# 5. Conclusions 

Failure analysis is an important and challenging problem for product quality and reliability research, not only on the theoretical but also on the practical significance. With the increasing complexity of products, fault tree analysis is becoming an indispensable part of the design process of product development. Through analyzing the faults of electromagnetic brakes by using the Bayesian network and accompanying the Wiener process, effective solutions are proposed in this paper, and the hidden troubles of product design and the production process are also resolved. Compared with the traditional T-S fault tree, the approved method can dynamically divide the faults of the whole production system, which can reduce the probability of each fault segment. Moreover, the T-S dynamic fault tree analysis method can vividly express the logical relationship and dynamic state of the fault system. The results showed that the new method is practicable in electromagnetic brakes fault diagnosis, and it also has reference value on other complicated machines' fault diagnosis and decision making.

Furthermore, compared with the traditional quantitative analysis, the Bayesian network is more convenient in calculating the importance of the dynamic fault tree. It can also obtain the posterior probability of influencing factors by reverse reasoning, according to the directed network. Considering the problem that it is difficult to predict the residual life of an electromagnet, the thesis introduces the Bayesian network and the Wiener process in a random process theory to model the practical operation. Further, the parameters of the degradation model can be estimated by a maximum likelihood estimation method, and the probability density function of the residual life of an electromagnet can be also obtained according to the concept of first arrival time. The simulation and application results on the actual electromagnetic brakes indicate that the new method can improve product fault diagnosis performance significantly. These computations also provide important decisionmaking information for the maintenance and replacement of electromagnets. The new approved method is limited in its scope but rathereffective, and it definitely has a potential engineering application value for use in the future.

Author Contributions: Conceptualization, J.P.; Data curation, J.D.; Formal analysis, J.D. and Y.L.; Funding acquisition, J.P. and Y.L.; Methodology, C.Z.; Project administration, Y.L.; Supervision, J.P. and Y.L.; Validation, H.Z.; Visualization, H.Z. All authors have read and agreed to the published version of the manuscript.
Funding: This work was supported by the National Natural Science Foundation of China (No. 72071149, 71671130), Provincial Natural Science Foundation, Zhejiang, China (No. LY20G010014).

Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Not applicable.
Conflicts of Interest: The authors declare no conflict of interest.
