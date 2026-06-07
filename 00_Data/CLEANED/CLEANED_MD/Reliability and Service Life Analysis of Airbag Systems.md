# Article 

## Reliability and Service Life Analysis of Airbag Systems

Hongyan Dui ${ }^{1}$ (D) Jiaying Song ${ }^{1}$ and Yun-an Zhang ${ }^{2, *}$


#### Abstract

check for updates Citation: Dui, H.; Song, J.; Zhang, Y.-a. Reliability and Service Life Analysis of Airbag Systems. Mathematics 2023, 11, 434. https:// doi.org/10.3390/math11020434

Academic Editor: Roberto Rocchetta

Received: 19 October 2022
Revised: 27 December 2022
Accepted: 12 January 2023
Published: 13 January 2023


## (0)

Copyright: (c) 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 School of Management, Zhengzhou University, Zhengzhou 450001, China
2 Laboratory of Science and Technology on Integrated Logistics Support, College of Intelligence Science and Technology, National University of Defense Technology, Changsha 410073, China

* Correspondence: yazhang@nudt.edu.cn; Tel.: +86-731-87005562


#### Abstract

Airbag systems are important to a car's safety protection system. To further improve the reliability of the system, this paper analyzes the failure mechanism of automotive airbag systems and establishes a dynamic fault tree model. The dynamic fault tree model is transformed into a continuous-time Bayesian network by introducing a unit step function and an impulse function, from which the failure probability of the system is calculated. Finally, the system reliability and average life are calculated and analyzed and compared with the sequential binary decision diagram method. The results show that the method can obtain more accurate system reliability and effectively identify the weak parts of the automotive airbag system, to a certain extent compensating for the lack of computational complexity of dynamic Bayesian networks in solving system reliability problems with continuous failure processes.


Keywords: reliability; life analysis; fault tree analysis; failure analysis; airbag system
MSC: 90B25

## 1. Introduction

An airbag is a protective device used in conjunction with seat belts to aid passenger safety [1]. It is often used as a last resort in collisions and consists mainly of airbag bags, sensors, inflators, and igniters. The sensor receives an impact signal and ignites the gas generator, generating a large quantity of gas, which is filtered and cooled into the airbag, causing it to break through the liner and rapidly deploy in a very short time, creating an elastic air cushion in front of the driver or occupant. Airbags can leak and contract in time to absorb impact energy, thus effectively protecting the human head and chest. They save the driver and passengers from injury or reduce the degree of injury suffered. The quality of car airbags is directly related to the safety of the driver and passengers. However, in actual traffic accidents, airbags sometimes fail to open, causing serious injuries and huge losses to the driver and passengers [2]. Therefore, it becomes a very important project to improve the reliability of the individual devices and systems in the automotive airbag system.

One of the common analysis methods used in reliability analysis is fault tree analysis, which is widely used in fault diagnosis and safety performance studies of components or systems [3]. The fault tree method has been used in the reliability assessment and design of systems due to its clear cause-effect relationships, ease of use, and combination of qualitative and quantitative aspects. However, it should also be noted that the traditional fault tree analysis method also has its limitations. While it can effectively handle systems with static logical characteristics, it is not ideal for systems characterized by dynamic properties such as temporality, redundancy, and correlation [4-6].

Especially in engineering applications, many meta-components or systems are not simply static, but often have characteristics such as uncertainty, dynamics, and continuity [7-9]. Static fault trees cannot model the reliability of dynamic systems. Therefore, dynamic fault tree analysis has been developed. Dugan proposed the concept of dynamic

fault trees in 1990, adding dynamic logic gates such as priority AND gates, cold spare gates, and cascading priority AND gates on top of static logic gates, forming the Dugan dynamic fault tree analysis method [10]. Scholars at home and abroad have focused on the quantitative analysis of Dugan dynamic fault trees [11] and dynamic logic gate expansion [12]. In terms of quantitative analysis of algorithms, the main methods are Markov chain analysis, Bayesian network analysis, Monte Carlo analysis, and sequential binary decision diagrams [13-15]. Among them, Boudali et al. [16] introduced the dynamic fault tree analysis method based on the Markov chain. However, when the system is relatively complex, this method will lead to the exponential increase in the computation amount with the increase in the state, so it also has some shortcomings. Walker and Papadopoulos [17] extended the logical basis of fault trees to enhance the ability of dynamic fault trees to express temporal correlations. Fault tree analysis is also widely used in various fields. Pang et al. [18] analyzed and diagnosed the electromagnet manufacturing process based on fuzzy fault trees and evidence theory. Yang et al. [19] used models such as fault trees to analyze the spread, identification, and causes of capital-raising frauds. Zhang et al. [20] used a fault tree model to analyze the collision risk factors of ship collisions, which can effectively guide rescue efforts.

As can be seen from the above analysis, both static and dynamic fault trees make some assumptions about the fault state of the system. These include the assumption that the event has only two states, "normal" and "fault", without considering the existence of other intermediate states [21]. As a result, there is a problem of inaccurate description of the system state and unclear identification of the system failure mode [22], and any errors can lead to large-scale economic losses [23,24]. In this case, therefore, the failure mechanism of the system and the logical relationships between events are usually described with the help of probabilities, but the probabilistic model cannot be described by relying solely on the logic gates in the fault tree. To make up for the shortcomings of fault trees in this area, the American scientist Judea Pearl introduced the concept of Bayesian networks in 1988. This concept has quickly become a hot topic of research and is widely used in various fields because it combines the well-established theories of probability theory and graph theory [25]. Bayesian networks are probability-based directed acyclic graphs with which complex inference problems can be handled [26], which have important applications in both fault diagnosis and reliability analysis. After analyzing the relationship between fault trees and Bayesian networks, complex uncertainty problems can be well handled with the help of Bayesian networks, which represent the interrelationships between nodes using conditional probability tables. It allows a two-way inference analysis: both forward calculation of the reliability of the system and backward diagnosis of the influence of one or some components on the system [27,28]. Bobbio et al. [25] found a way to transform the traditional static fault tree model into a static Bayesian network. For static Bayesian networks, the nodes do not contain dynamic logical relationships with each other. Therefore, static Bayesian networks cannot analyze the system reliability problems of continuous systems at arbitrary times. In order to fully consider the timing of each event occurring in the system, the dynamic Bayesian network is formed on the basis of the static Bayesian network. Dynamic Bayesian networks take into account the conditional independence of variables, and the number of parameters in the conditional probability table is much lower than the number of states in the Markov model, so the solution complexity of the Bayesian network model is low. These advantages of Bayesian network models have led to their increasing application in system reliability modeling and evaluation [29,30].

The fault tree model is quickly constructed through fault analysis and then converted directly into a Bayesian network model, which reduces the modeling process. The excellent bidirectional inference computational capability of Bayesian networks can be applied for multistate reliability analysis of complex systems, which can complement the shortcomings of fault tree analysis in multistate analysis and complex system applications. Therefore, this paper takes an automotive airbag system as a background and draws on the nature of Bayesian networks. It is discussed how the dynamic fault tree model can be transformed

into a continuous Bayesian network. The reliability of the automotive airbag system at any time is derived where the probability distribution obeyed by the failure process of the system events can be obtained.

The rest of this paper is organized as follows. Section 2 briefly describes the components of an automotive airbag system and presents an example of fault analysis of the system with dynamic fault tree modeling. Section 3 transforms the dynamic fault tree model of the automotive airbag system into a continuous Bayesian network model with the help of the unit step function and impulse function, and analyzes the reliability and expected life of the automotive airbag system. The sequential binary decision diagram method is also used to compare with the method proposed in this paper. Section 4 concludes the paper. The research framework of this paper is shown in Figure 1.
![img-0.jpeg](img-0.jpeg)

Figure 1. Structure of the article.

# 2. Dynamic Fault Tree of Automotive Airbag System 

In this paper, the airbag system failure is identified as the top event of the fault tree $Z$. The automotive airbag system mainly consists of sensors, inflators, and electronic control units. Failure of any one of these three subsystems can lead to airbag system failure. A redundant configuration is used, as the sensors and electronic control unit are key components of the airbag system. The sensor subsystem block has a hot standby sensor and the electronic control unit subsystem has a cold standby power circuit. For the inflator subsystem, there are three parts: the inner filter, the outer filter, and the ignition transfer mechanism. The ignition transfer mechanism consists of a bridge wire, an electric ignition device, and a flame transfer hole. The electric ignition apparatus consists of two parts: the spreading charge and the ignition charge. Therefore, the failure mechanism of the system is analyzed. The dynamic fault tree model of the system is shown in Figure 2.

The structure of the automobile airbag system is shown in Figure 3. The meaning of each symbol in the fault tree model is shown in Table 1. Then, according to the analysis of the failure process of the automotive airbag system, the distribution and failure rate obeyed by each component in the system during the failure process can be obtained as follows.

Based on the above analysis, we can obtain the automotive airbag system's dynamic fault tree model and failure rate distribution. Further derivation of the method for converting the dynamic fault tree of an automotive airbag system into a Bayesian network will be presented in the subsequent sections.
![img-1.jpeg](img-1.jpeg)

Figure 2. Dynamic fault tree of automotive airbag system.
![img-2.jpeg](img-2.jpeg)

Figure 3. System structure of automotive airbag system.

Table 1. Table of symbol meanings and their failure distribution in dynamic fault trees.


# 3. Reliability and Life Analysis 

Based on the dynamic fault tree model of automotive airbags proposed in the previous chapter, the reliability and lifetime will be analyzed in this chapter.

### 3.1. Reliability and Life Analysis Based on Bayesian Network

The dynamic fault tree model for each part of the automotive airbag system is next transformed in parts into an equivalent continuous Bayesian network model. The dynamic fault tree model of the overall automotive airbag system will be further transformed in the following. A Bayesian network topology equivalent to it is obtained, as shown in Figure 4.
![img-3.jpeg](img-3.jpeg)

Figure 4. Equivalent Bayesian network model for automotive airbag systems.

According to the structural characteristics of the airbag system, based on Table 1, the failure processes of all the bottom events obey the exponential distribution. The probability density function of the exponential distribution can be obtained according to the content of the probability theory, as shown in Equation (1); $x$ is the time variable of the component, and the distribution function of the exponential distribution is shown in Equation (2)

$$
\begin{aligned}
& f(x)= \begin{cases}\lambda e^{-\lambda x} & x>0 \\
0 & x \leq 0\end{cases} \\
& F(x)= \begin{cases}1-e^{-\lambda x} & x \geq 0 \\
0 & x<0\end{cases}
\end{aligned}
$$

(1) The failure processes of the dynamic logic AND gate event $\mathrm{X}_{9}$ and event $\mathrm{X}_{10}$ obey exponential distribution, and the failure rates of the events are $\lambda_{9}$, and $\lambda_{10}$, respectively. Based on the above analysis of the transformation of the dynamic logic AND gate and the nature of exponential distribution, it can be obtained that the marginal probability density function of the failure of lower level event $\mathrm{Y}_{5}$ is

$$
f_{Y_{5}}(y)=\frac{d\left[F_{X_{9}}(y) F_{X_{10}}(y)\right]}{d y}=\lambda_{9} e^{-\lambda_{9} y}+\lambda_{10} e^{-\lambda_{10} y}-\left(\lambda_{9}+\lambda_{10}\right) e^{-\left(\lambda_{9}+\lambda_{10}\right) y}
$$

The probability distribution function for the failure of the lower-level event $\mathrm{Y}_{5}$ is

$$
F_{Y_{5}}(t)=F_{X_{9}}(t) F_{X_{10}}(t)=1-e^{-\lambda_{9} t}-e^{-\lambda_{10} t}+e^{-\left(\lambda_{9}+\lambda_{10}\right) t}
$$

(2) The failure processes of the dynamic logic OR gate event $\mathrm{Y}_{5}$, event $\mathrm{X}_{7}$, and event $\mathrm{X}_{8}$ all obey exponential distribution. The probability distribution function of the failure of event $\mathrm{Y}_{5}$ has been found, and the failure rates of event $\mathrm{X}_{7}$ and event $\mathrm{X}_{8}$ are $\lambda_{7}$ and $\lambda 8$, respectively. According to the construction method of the upper-level event as two, the dynamic OR gate structure of this layer is transformed into a two-layer virtual dynamic OR gate structure. That is, event $\mathrm{X}_{7}$ and event $\mathrm{X}_{8}$ constitute event $\mathrm{W}_{1}$.

The marginal probability density function for the failure of the lower-level event W1 is

$$
f_{W_{1}}(y)=f_{X_{7}}(y)+f_{X_{8}}(y)-\frac{d\left[F_{X_{7}}(y) F_{X_{8}}(y)\right]}{d y}
$$

The probability distribution function for the failure of the lower-level event $\mathrm{W}_{1}$ is

$$
F_{W_{1}}(t)=F_{X_{7}}(t)+F_{X_{8}}(t)-F_{X_{7}}(t) F_{X_{8}}(t)=1-e^{-\left(\lambda_{7}+\lambda_{8}\right) t}
$$

The marginal probability density function for the failure of the lower-level event $\mathrm{Y}_{4}$ is

$$
f_{Y_{4}}(z)=f_{Y_{5}}(z)+f_{W_{1}}(z)-\frac{d\left[F_{Y_{5}}(z) F_{W_{1}}(z)\right]}{d z}
$$

The probability distribution function for the failure of the lower-level event $\mathrm{Y}_{4}$ is

$$
F_{Y_{4}}(w)=F_{Y_{5}}(w)+F_{W_{1}}(w)-F_{Y_{5}}(w) F_{W_{1}}(w)
$$

(3) The failure processes of dynamic logic OR gate event $\mathrm{Y}_{4}$, event $\mathrm{X}_{3}$, and event $\mathrm{X}_{4}$ all obey exponential distribution. The probability distribution function of the failure of event $\mathrm{Y}_{4}$ has been found, and the failure rates of event $\mathrm{X}_{3}$ and event $\mathrm{X}_{4}$ are $\lambda_{3}$ and $\lambda_{4}$, respectively. According to the construction method of the upper-level event as two, the dynamic OR gate structure of this layer is transformed into a two-layer virtual dynamic OR gate structure. That is, event $\mathrm{X}_{3}$ and event $\mathrm{X}_{4}$ constitute event $\mathrm{W}_{2}$.

The marginal probability density function for the failure of the lower-level event $\mathrm{W}_{2}$ is

$$
f_{W_{2}}(y)=f_{X_{3}}(y)+f_{X_{4}}(y)-\frac{d\left[F_{X_{3}}(y) F_{X_{4}}(y)\right]}{d y}
$$

The probability distribution function for the failure of the lower-level event $\mathrm{W}_{2}$ is

$$
F_{W_{2}}(t)=F_{X_{3}}(t)+F_{X_{4}}(t)-F_{X_{3}}(t) F_{X_{4}}(t)=1-e^{-\left(\lambda_{3}+\lambda_{4}\right) t}
$$

The marginal probability density function for the failure of the lower-level event $\mathrm{Y}_{2}$ is

$$
f_{Y_{2}}(z)=f_{Y_{4}}(z)+f_{W_{2}}(z)-\frac{d\left[F_{Y_{4}}(z) F_{W_{2}}(z)\right]}{d z}
$$

The probability distribution function for the failure of the lower-level event $\mathrm{Y}_{2}$ is

$$
F_{Y_{2}}(w)=F_{Y_{4}}(w)+F_{W_{2}}(w)-F_{Y_{4}}(w) F_{W_{2}}(w)
$$

(4) The failure processes of dynamic logic hot standby gate events $\mathrm{X}_{1}$ and event $\mathrm{X}_{2}$ obey exponential distribution, and the failure rate of event $\mathrm{X}_{1}$ and event $\mathrm{X}_{2}$ is $\lambda_{1}$ and $\lambda_{2}$, respectively, and $\lambda_{1}=\lambda_{2}$, based on the above analysis of the transformation of the dynamic logic hot standby gate and the nature of the exponential distribution. The marginal probability density function for the failure of the upper-level event $\mathrm{Y}_{1}$ can be obtained as

$$
f_{Y_{1}}(y)=\frac{d\left[F_{X_{1}}(y) F_{X_{2}}(y)\right]}{d y}=2 \lambda_{1} e^{-\lambda_{1} y}-2 \lambda_{1} e^{-2 \lambda_{1} y}
$$

The probability distribution function for the failure of the lower-level event $\mathrm{Y}_{1}$ is

$$
F_{Y_{1}}(t)=F_{X_{1}}(t) F_{X_{2}}(t)=1-2 e^{-\lambda_{1} t}+e^{-2 \lambda_{1} t}
$$

(5) The failure process of the dynamic logic cold-ready gate event $\mathrm{X}_{5}$ obeys an exponential distribution with a failure rate of $\lambda_{5}$. The independent failure process of event $\mathrm{X}_{6}$ also obeys an exponential distribution with a failure rate of $\lambda_{6}$ and $\lambda_{5}=\lambda_{6}$, based on the above analysis of the transformation of the dynamic logic cold-ready gate and the nature of the exponential distribution. The marginal probability density function for the failure of the upper-level event $\mathrm{Y}_{3}$ can be obtained:

$$
\begin{aligned}
f_{Y_{3}}(y) & =\int_{0}^{\infty} \int_{0}^{\infty} v\left(x_{6}-x_{5}\right) \zeta\left(y-x_{6}\right) v\left(x_{6}-x_{5}\right) \lambda_{6} e^{-\lambda_{6}\left(x_{6}-x_{5}\right)} \lambda_{5} e^{-\lambda_{5} x_{5}} d x_{5} d x_{6} \\
& =\lambda_{5} \lambda_{5} \int_{0}^{\infty} \int_{0}^{\infty}\left[v\left(x_{6}-x_{5}\right)\right]^{2} \zeta\left(y-x_{6}\right) e^{-\lambda_{5} x_{6}} d x_{5} d x_{6} \\
& =\lambda_{5} \lambda_{5} \int_{0}^{\infty}\left[v\left(y-x_{5}\right)\right]^{2} e^{-\lambda_{5} y} d x_{5}
\end{aligned}
$$

From the properties of the unit step function, the following equation can be obtained:

$$
\left[v\left(y-x_{5}\right)\right]^{2}= \begin{cases}1 & y>x_{5} \\ \frac{1}{4} & y=x_{5} \\ 0 & y<x_{5}\end{cases}
$$

Because the marginal probability density function for finding the failure of event $\mathrm{Y}_{3}$ is a Riemann integral over its probability density function, it follows from the nature of the Riemann integral that changing the value of a point does not affect the result of the integration. Therefore, when $\mathrm{y}=\mathrm{x}_{5}$, one can make $\left[v\left(\mathrm{y}-\mathrm{x}_{5}\right)\right]^{2}=1$.

Then the value of the above equation is

$$
\begin{aligned}
f_{Y_{3}}(y) & =\lambda_{5} \lambda_{5} \int_{0}^{\infty}\left[v\left(y-x_{5}\right)\right]^{2} e^{-\lambda_{5} y} d x_{5} \\
& =\lambda_{5} \lambda_{5} e^{-\lambda_{5} y} \int_{0}^{y} 1 d x_{5} \\
& =\lambda_{5} \lambda_{5} y e^{-\lambda_{5} y}
\end{aligned}
$$

The probability distribution function for the failure of the upper-level event $\mathrm{Y}_{3}$ is

$$
F_{Y_{3}}(t)=\int_{0}^{t} f_{Y_{3}}(y) d y=\int_{0}^{t} \lambda_{5} \lambda_{5} y e^{-\lambda_{5} y} d y=1-e^{-\lambda_{5} y}-\lambda_{5} t e^{-\lambda_{5} y}
$$

(6) For an OR gate structure consisting of event $\mathrm{Y}_{1}$ and event $\mathrm{Y}_{2}$, from the above analysis of the transformation of dynamic logic OR gates, the probability distribution function for the failure of event W is calculated using Matlab and yields the following result:

$$
F_{W}(t)=F_{Y_{1}}(t)+F_{Y_{3}}(t)-F_{Y_{1}}(t) F_{Y_{3}}(t)
$$

Similarly, the probability distribution function for the failure of event $Z$ is calculated as

$$
F_{Z}(t)=F_{Y_{2}}(t)+F_{W}(t)-F_{Y_{2}}(t) F_{W}(t)
$$

Reliability is the ability of a device to perform a specified function under specified conditions and within a specified time. The probability measure of reliability is called dependability. It represents the probability that a component, product, or system will perform a specified function under specified conditions and within a specified time. For the automotive airbag system described above, assuming that the specified time is $t$ and the life of the system is $Z$, the reliability is expressed as the probability that $Z>t$.

$$
R_{Z}(t)=P(Z>t)
$$

The probability of failure characterizes the probability that a component, product, or system will lose a specified function under specified conditions and within a specified time. For the above automotive airbag system, assuming a specified time of $t$ and a system life of $Z$, the probability of failure of the system is

$$
F_{Z}(t)=P(Z \leq t)=1-R_{Z}(t)
$$

From the above analysis, the reliability and probability of failure of an automotive airbag system can be obtained. Substituting the values of the failure rate for each basic event into the above equation, and making $\mathrm{t}=1000 \mathrm{~h}, \mathrm{t}=5000 \mathrm{~h}, \mathrm{t}=10,000 \mathrm{~h}, \mathrm{t}=15,000 \mathrm{~h}, \mathrm{t}$ $=20,000 \mathrm{~h}$, and $\mathrm{t}=25,000 \mathrm{~h}$, respectively, we obtain Table 2.

Table 2. Probability of failure and reliability of automotive airbag systems.


At 1000 h , the probability that the system can complete the specified function under certain conditions is 0.8946 ; at $10,000 \mathrm{~h}$, the probability that the system can complete the specified function under certain conditions is 0.3132 . From Table 2, we can see that after $10,000 \mathrm{~h}$, the reliability of the system is very low and cannot meet the needs for the safe operation of the system at all.

The reliability and probability of failure of the airbag system of the car with time are shown in Figure 5. When the airbag system operates at $40,000 \mathrm{~h}$, the reliability of the system is close to 0 , and the system must be repaired or replaced at this time.

Once the reliability of an automotive airbag system has been obtained, the average life of the system can be predicted based on the resulting reliability. The average life can be obtained from the integration of the reliability of the system $R_{Z}(t)$ over $(0, \infty)$. The average life of the system is approximately 8410 h . The average life is a guide for the replacement of equipment and the evaluation of the safety performance of the system.

![img-4.jpeg](img-4.jpeg)

Figure 5. Reliability change for automotive airbag systems.
By considering the reliability $R_{Z}(t)$ of the automotive airbag system as a function of $\lambda_{1}, \lambda_{5}, \lambda_{7}$, and $\lambda_{9}$, the trend of the reliability with the parameters at any moment can be found. When $t=2000 \mathrm{~h}$, the system reliability $R_{Z}(t)$ can be obtained as a function of a single parameter, as shown in Figure 6. According to Figure 4, we can know the trend of reliability with parameters at any moment: the reliability of the system is negatively related to each parameter and decreases with the increase in the failure rate of each component, and components with a significant trend of change have a greater impact on system reliability.
![img-5.jpeg](img-5.jpeg)

Figure 6. Service life changes with reliability.

# 3.2. Reliability Analysis Based on Sequential Binary Decision Diagrams 

Sequential binary decision diagrams can also be used to analyze dynamic fault trees containing various logical gates such as priority and standby gates [15]. In order to verify the effectiveness and accuracy of the method in this paper, the method is compared with the sequential binary decision diagram method. In a dynamic fault tree, the failure sequence relationship of logic gate input events has a significant impact on system failure, so the relational notation will be used to describe the timing relationship of the basic events. For example, $\mathrm{A} \rightarrow \mathrm{B}$ means that event A occurs before event B. A $\sim$ B means that events A and B occur simultaneously. The following is a brief description of the spare parts gate timing logic used in dynamic fault trees.
(1). Cold Standby Gates

The cold standby gates are regarded as having no consumption before entering the working state, so the failure rate is 0 , and the reserve events must be selected to fail sequentially according to the sequence, whose algebraic description is $\mathrm{A} \rightarrow \mathrm{B}$.
(2). Hot Standby Gates

The backup events of hot standby gates have the same probability of failure during the reserve and active states. When the coverage of the standby structure is not considered, the hot standby gate is equivalent to a parallel structure.

Convert the dynamic fault tree in Figure 2 to the sequential binary decision diagram in Figure 7.
![img-6.jpeg](img-6.jpeg)

Figure 7. The binary decision diagram of automobile airbag system.
Analyzing the sequential binary decision diagram in Figure 7, 21 failure paths of system disjunction can be obtained, and the specific paths are shown in Table 3.

Table 3. Failure paths of automotive airbag systems.


The life of the components in the cold standby gate are $\mathrm{X}_{5}$ and $\mathrm{X}_{6}$, and they are independent of each other, so the life of the cold standby gate is

$$
X_{\mathrm{X}_{5} \rightarrow \mathrm{X}_{6}}=X_{5}+X_{6}
$$

The failure rate of the cold standby gate $\left(\mathrm{X}_{5} \rightarrow \mathrm{X}_{6}\right)$ is

$$
F_{\mathrm{X}_{5} \rightarrow \mathrm{X}_{6}}(t)=F_{5}(t) * F_{6}(t)
$$

The probability of occurrence of failure of each path is $O_{i}(i=1,2, \ldots, 21)$, where $O_{i}$ denotes the probability of failure of path $i$. Therefore, the reliability function of the system is

$$
R(t)=1-\cdots\left(O_{1}+\cdots+O_{21}\right)
$$

Using Matlab to calculate the system failure probability and reliability in the time range $0-8000$, the obtained variation curves are essentially the same as those transformed into dynamic Bayesian networks using dynamic fault trees.

System failure probability calculation under two methods is shown in Table 4 by selecting different task times.

Table 4. Failure probability of automotive airbag systems under two methods.


The results of the two methods are compared to demonstrate the accuracy of the transformation of dynamic fault trees into dynamic Bayesian network methods. Moreover, compared with the method in this paper, for dynamic fault trees containing spare parts, the sequential decision diagram method is affected by the transformation method and suffers from problems such as node redundancy and excessive size, thus reducing the effectiveness of dynamic fault tree qualitative analysis. In contrast, the dynamic Bayesian network-based method can provide a general fault tree transformation method with high computational efficiency and save computing time, which is more suitable for complex dynamic fault tree analysis with more spare parts.

# 4. Conclusions 

In this paper, a dynamic fault tree model of the automotive airbag system is established. Secondly, the discussion in this paper focuses on constructing continuous Bayesian networks with the help of unit step functions and impulsive functions, and an in-depth analysis of the transformation of dynamic logic with AND/OR gates is carried out. The results prove that the transformation of the dynamic fault tree model into a continuous-time Bayesian network model is feasible and can reduce the problem of the dynamic Bayesian network model being too computationally intensive when dealing with complex systems. Finally, after transforming the dynamic fault tree model of an automotive airbag into a Bayesian network, the reliability parameters of the system are analyzed and calculated. When each component of the system has a continuous failure process, the model construction method proposed in this paper can be used, and the reliability of the system at any moment can be further derived. Comparison with the sequential binary decision method shows that the method proposed in this paper can provide a scientific basis for the reasonable maintenance of airbag systems.

In future research, we will consider a maintenance policy that meets optimal replacement times and minimizes expected replacement costs based on system reliability.

Author Contributions: Conceptualization, H.D. and J.S.; methodology, H.D.; software, J.S.; validation, Y.-a.Z.; formal analysis, J.S.; investigation, H.D.; resources, Y.-a.Z.; data curation, J.S.; writing-original draft preparation, J.S.; writing-review and editing, H.D. and Y.-a.Z.; supervision, Y.-a.Z.; funding acquisition, H.D. All authors have read and agreed to the published version of the manuscript.

Funding: This research was funded by the Key Science and Technology Program of Henan Province (No. 222102520019), the Program for Science \& Technology Innovation Talents in Universities of Henan Province (No. 22HASTIT022), the Program for young backbone teachers in Universities of Henan Province (No. 2021GGJS007).

Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: The authors confirm that the data supporting the findings of this study are available within the article.

Conflicts of Interest: The authors declare no conflict of interest.
