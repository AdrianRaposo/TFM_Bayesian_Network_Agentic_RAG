# Article 

## Research on the Reliability Allocation Method of Smart Meters Based on DEA and DBN

Juan Zhou ${ }^{1, * *}$, Zonghuan $\mathrm{Wu}^{1 *}$ and Zhonghua Yu ${ }^{2}$

## check for updates

Citation: Zhou, J.; Wu, Z.; Yu, Z. Research on the Reliability Allocation Method of Smart Meters Based on DEA and DBN. Appl. Sci. 2021, 11, 6901. https://doi.org/10.3390/ app11156901

Academic Editor: Jan Awrejcewicz

Received: 12 June 2021
Accepted: 20 July 2021
Published: 27 July 2021

Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## 0

Copyright: (c) 2021 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 College of Quality and Safety Engineering, China Jiliang University, Hangzhou 310018, China; s20060837009@cjlu.edu.cn
2 School of Mechanical Engineering, Zhejiang University, Hangzhou 310018, China; YZH@zju.edu.cn

* Correspondence: zhoujuan@cjlu.edu.cn; Tel.: +86-571-8691-4553

Abstract: Reliability allocation can reasonably determine the reliability index of each unit in the system to ensure product quality in design, manufacturing, testing and acceptance. In the design process of the smart meter, the preliminary reliability allocation results may be unreasonable, so in the middle and later stages of the design stage, the reliability needs to be reallocated. The traditional allocation method has some limitations, such as strong subjectivity, large amount of calculation and too much reliance on expert judgment. In order to solve these problems, this paper presents a multi-method fusion method of reliability allocation. First, this paper uses the goal-oriented methodology (GO methodology) to integrate dynamic Bayesian networks (DBNs) to predict the reliability of smart meters. Second, a data envelopment analysis (DEA) reliability allocation model is established, the posterior probability obtained by DBN reasoning together with the failure rate and structural complexity of each unit are used as the output indicators of this model. Finally, the reliability allocation weight is calculated by using the efficiency value obtained from the DEA reliability allocation model. The validity and accuracy of this method is verified by an accelerated life test. This provides a new idea for reliability reallocation of smart meters.

Keywords: reliability allocation; smart meter; data envelopment analysis; dynamic Bayesian networks; GO methodology

## 1. Introduction

With the rapid development of the smart grid, the modern power grid with advanced sensor measurement technology, communication technology, information technology and control technology has taken shape. As the core part of the smart grid, the AMI advanced measurement system plays an important role in it, and the smart meter is an important part of the advanced measurement system. Smart meters not only have the basic functions of traditional meters, but also have intelligent functions such as two-way multi-rate metering functions, user-side control functions, two-way data communication functions and antitheft functions. The diversification and complexity of their functions have also led to endless quality problems. According to the statistics of the State Grid, the average failure rate of a newly installed smart meter in the first year of operation reached $0.09 \%$, and was even as high as $0.6 \%$ in some provinces. Research on the reliability of smart meters has become particularly important. Therefore, many scholars have carried out a series of studies on the reliability of smart meters, including reliability predictions, failure mechanism analyses, reliability design analyses, reliability testing, etc. [1-4]. However, there are few studies on the reliability allocation of smart meters.

Reliability allocation is a method of reasonably subdividing the designed system reliability into every unit of the system. Reliability allocation can reasonably determine the reliability index of each unit in the system to ensure the quality of products in design, manufacture, testing and acceptance. It can also help the designer to understand the reliability relationship between the unit and system and to balance the relationship between


In order to solve the above shortcomings of the reliability allocation algorithm, an innovative reliability allocation method based on multi-method fusion of data envelopment analysis (DEA) and dynamic Bayesian networks (DBNs) are proposed. DEA has many advantages, such as no need to consider the relationship between variables, the evaluation result being independent of the data dimension, a simple algorithm, small calculation errors, and not dependence on subjective evaluation. The DEA method is often used to evaluate the efficiency [12,13,14,15], but there are few papers on the application of the DEA method to the reliability allocation of smart meters. Based on this, a new method of reliability allocation is proposed in this paper. This is a smart meter reliability allocation method of multi-method fusion. Firstly, the reliability analysis model of smart meter is established by using the strong semantic advantage of goal-oriented (GO) methodology. DBN is used to solve the complex modeling and low accuracy of GO methodology. On this basis, combined with DEA method, the reliability allocation model of smart meter is established. The posterior probability derived from backward reasoning of DBN, together with the failure rate and structural complexity of each unit, are taken as the output indicators of DEA reliability allocation model to make the output of reliability allocation model more scientific. It is more objective and practical to allocate the reliability index based on the actual fault information of smart meter. This paper does not need expert scoring, decision matrix, screening minimum cut set and so on but is based on the actual system fault data statistics, so the result is more objective, the algorithm is simple and easy to solve.

The organization of the paper is as follows: Section 2 introduces the working principle and system architecture of smart meters. Section 3 introduces the principles of the GO methodology, DBN and DEA, and the detailed steps of the reliability allocation method. Section 4 carries out the reliability allocation of smart meters. Section 5 uses accelerated life tests to verify the validity and accuracy of the proposed reliability allocation method. Conclusions are drawn in Section 6.

# 2. Brief Introduction of Smart Meters 

Compared with traditional meters, smart meters have features such as power memory, meter reading time freezing and remote information transmission. After a smart meter is installed and used, power users can directly query the power, meter number, current time, power consumption and other information through the LCD display on the meter. Smart meters have the advantages of supporting multiple electricity prices, two-way communication, two-way metering and intelligent power consumption control.

### 2.1. Introduction of the Working Principle

The smart meter is mainly composed of electronic components, and its working principle is to process the sampled voltage and current signals by real-time sampling of the voltage and current supplied by the user. Then, the special integrated circuit of the smart meter is used to convert these into electrical energy proportional to the pulse output. Finally, the pulse is displayed as power consumption and output by single chip microcomputer, as shown in Figure 1.
![img-0.jpeg](img-0.jpeg)

Figure 1. Working principle diagram of a smart meter.

# 2.2. System Block Diagram and Unit Division 

In this paper, a single-phase smart meter (the latter are called smart meter) is used as an example, the model is DDZM285-Z, as show in Figure 2, which is the system block diagram of the smart meter, showing the smart meter contains which components, the operational relationship between the components and the working process of the meter.
![img-1.jpeg](img-1.jpeg)

Figure 2. Block diagram of a smart meter system.
According to the functional properties of each component, the smart meter is divided into six units: power supply unit, metering core unit, management core unit, storage unit, communication unit and display unit. The specific components contained in each unit are shown in Table 2 in Section 4. The following is a brief description of the functions of each unit:

- Power supply unit: The power supply of single-phase smart meter includes AC power supply and low power consumption power supply. AC power supply is the input of the meter, 220 V AC. The power circuit converts 220 V AC into DC at different amplitudes, which is used to power other modules as well as input to the metering module; the low power supply is a lithium battery, which is used as a backup power supply, used to maintain the meter in the event of a power failure.
- Metering core unit: The metering core provides the data of power, clock and so on, and keeps the historical data of forward and backward active power total energy every minute, forward and backward active fundamental energy every 15 min , and forward and backward active power harmonic total energy for electric quantity tracing. The charge and clock of the management core are based on the metering core and synchronized in real time. Metering core can record management core plug, power off, meter reset, calibration, management core upgrade and other event records.
- Management core unit: Management Core is responsible for the whole smart meter management tasks, including fee control, display, communication, event records, data freezing, load control, etc.
- Storage unit: Store all kinds of data generated by the smart meter. When the state of the system changes, all the changed parameters can be written to the memory.

- Communication unit: The communication unit includes uplink communication module, downlink communication module, extended function module and blue tooth communication module to realize the communication function and to read meters and send instructions, etc.
- Display unit: The main display mode of the smart meter is the light emitting diode and liquid crystal. The light emitting diode is mainly the role of the indicator light; the liquid crystal circuit is used to display various types of parameters of the smart meter.


# 3. Reliability Allocation Method Base on DEA and DBN 

Before reliability allocation, this paper first uses the GO methodology and DBN method to predict the reliability of smart meters. The Go diagram directly represents the interaction and correlation between the system and its components. The simulation of the GO diagram is more compact than fault tree analysis (FTA) simulation and is easier to examine, change and modify by technicians. The GO methodology not only describes the state of the system and its components at a particular time but also describes the states and state changes of systems and components at various time points, which can be used for probabilistic analysis of systems with time series [16]. The characteristics of the GO methodology also make it difficult to use. There are many types of operators and usage is complicated, which makes it difficult to popularize the GO methodology in engineering applications. Therefore, the combination of GO methodology and DBN is considered, this can effectively solve the problems of complex reliability modeling and low accuracy of reliability model prediction. DBN has ability to describe event polymorphisms and nondeterministic logical relations and can guarantee high precision, so they are often used to analyze dynamic complex systems with time series [17-20]. According to the mapping method from the GO diagram to the DBN diagram, it is easy to deduce the reliability of smart meter by Bayes software. Second, A DEA reliability allocation model is established to obtain the efficiency value of each unit relative to the whole smart meter system, the posteriori probability derived from DBN backward reasoning, together with the failure rate and structural complexity of each unit, are taken as the output indicators of the reliability allocation model. Finally, the reliability allocation results are calculated according to the efficiency value. The whole process of the method is shown in Figure 3.
![img-2.jpeg](img-2.jpeg)

Figure 3. Reliability allocation process.

### 3.1. Brief Introduction of Methods

### 3.1.1. Brief Introduction of the GO Methodology Principle

The GO methodology is a success-oriented system probability analysis technique that is more suitable for multistate systems with time sequences, especially for the reliability analysis of actual logistics processes. The components or subsystems in the system are referred to as units, the operator represents the unit function and the logical relationship between the unit input and output signals in the GO methodology. The attributes of the operator have type, data, and arithmetic rules. The type of operator reflects the unit

functions and features. As show in Figure 4, GO methodology has defined 17 standard operators, divided into logical operators and functional operators. Logical operators have no state of their own and represent only one kind of operation logic, including class 2, 9, $10,11,13,14$ and 15 operators. Functional operators have functional states of their own and contain operation logic, including class $1,3,4,5,6,7,8,12,16$ and 17 operators.
![img-3.jpeg](img-3.jpeg)

Figure 4. Standard operator types of GO methodology.
In Figure 4, S represents the input signal, R represents the output signal. The GO diagram is the direct simulation of the system, and the operators in the GO diagram correspond to the components of the system. The signal flow represents the input and output signals of the system units and the relationships between the units. The signal flow connects the GO operator to generate the GO diagram. In reference [16,21-23], the definition of standard operator type, corresponding data and operation rules are explained in detail, and the algorithm of the operator is illustrated.

# 3.1.2. Brief Introduction of the DBN Principle 

DBN is graphic structures based on static Bayesian networks and Markov models. Dynamic Bayesian networks are composed of initial networks and transfer networks, and the whole network has limited time slices [24,25]. Each time slice has a corresponding conditional probability table (CPT). The dynamic Bayesian network of a simplified pattern is shown in Figure 5. $\mathrm{A}(\mathrm{t})$ and $\mathrm{B}(\mathrm{t})$ are the initial network, $\mathrm{A}(\mathrm{t}+\Delta \mathrm{t})$ and $\mathrm{B}(\mathrm{t}+\Delta \mathrm{t})$ are the transfer network, and $R(t+\Delta t)$ is the output of the transfer network.
![img-4.jpeg](img-4.jpeg)

Figure 5. DBN diagram.
Dynamic Bayes can learn the probability dependence between variables and their changing rules over time. DBN is defined as $\left(B_{1}, 2 T B N\right)$, where $B_{1}$ is a Bayesian network, it defines a prior distribution $P\left(X_{1}\right)$, and 2TBN is a BN with two time slices [26].

$$
P\left(X_{t} \mid X_{t-1}\right)=\prod_{i=1}^{n} P\left(X_{t}^{i} \mid P a\left(X_{t}^{i}\right)\right)
$$

$X_{t}^{i}$ represents the node on time slice $t$ and $P a\left(X_{t}^{i}\right)$ represents the parent node set on time slice $t$. The joint distribution occurs when the time slices of 2TBN are expanded to $T$ time slices:

$$
P\left(X_{1: T}\right)=\prod_{t=1}^{T} \prod_{t=1}^{n} P\left(X_{t}^{i} \mid P a\left(X_{t}^{i}\right)\right)
$$

For system components, the probability that they are in a normal working state and fault state varies with time, where 1 indicates a failure state and 2 indicates a normal working state. Under the condition of unrepairable (the value of the smart meter itself is not high, and the strategy of rotation is generally adopted instead of repair after longterm operation, so a smart meter is defined as a nonrepairable product), the conditional probability of being in state 1 at time $T+\Delta T$ is:

$$
\begin{gathered}
P(B(T+\Delta T)=1 \mid B(T)=2)=\int_{T}^{T+\Delta T} f(t) d t \\
P(B(T+\Delta T)=1 \mid B(T)=1)=1
\end{gathered}
$$

where $B(T)=1$ means that component $B$ is in state 1 at time $T$, and $f(t)$ represents the failure probability density function of component B.

# 3.1.3. Brief Introduction to the Principle of Data Envelopment Analysis 

Based on the relative efficiency concept, the American famous scholars Charnes and Cooper have built a CCR model, and the data envelopment analysis (DEA) was first proposed. Based on the basic concept of Pareto, this method developed the traditional single-input, single-yield project revenue concept, enabling it to evaluate the effectiveness of multi-input, multi-output decision making units (DMU). Input refers to the amount consumed by the DMUs in a certain activity, and output refers to the amount of information generated by the DMUs after a certain input to show the effectiveness of the activity. This method has the advantages of simple algorithm, small calculation error and does not rely on subjective evaluation [27,28].

In this paper, using $\theta_{k}$ as the efficiency value of $D M U_{k}, \theta_{k}$ is defined as the ratio of the weighted sum of the output to the weighted sum of the input. Suppose there are n decision-making units $D M U_{j}(1 \leq j \leq n)$, whose input indicators are $x_{i j}(i=1,2, \ldots, m)$ and output indicators are $y_{j r}(r=1,2, \ldots, s)$, the input and output vectors are:

$$
\begin{aligned}
& x_{j}=\left(x_{j 1}, x_{j 2}, \ldots, x_{j m}\right) \\
& y_{j}=\left(y_{j 1}, y_{j 2}, \ldots, y_{j s}\right)
\end{aligned}
$$

Based on the technical efficiency of input, in a certain output, the pursuit of input reduction, on this basis, chooses an input-type DEA model, that is, finding the minimum value of $\theta$. By applying the Charnes-Cooper transformation to the original CCR-DEA model and adding the relaxation variables, we obtain the following linear programming model:

$$
\left\{\begin{array}{c}
\min \theta \\
\text { s.t. }\left\{\begin{array}{c}
\sum_{j=1}^{n} x_{j} \lambda_{j}+s^{-}=\theta x_{j 0} \\
\sum_{j=1}^{n} y_{j} \lambda_{j}-s^{+}=y_{j 0} \\
\lambda_{j} \geq 0, j=1,2, \ldots, n \\
s^{+}, s^{-} \geq 0
\end{array},\right.
\end{array}\right.
$$

In the Formula (6), $\theta$ is the efficiency value of each DMU, $\theta=1$ is the effective DMU, $\theta<1$ is the noneffective DMU and the model assumes that the constraint to evaluate the effectiveness is that the maximum effective value of all DMUs is 1 , which is based on the principle that the maximum energy conversion efficiency is 1 in the natural process [29]. $\lambda_{j}(j=1,2, \ldots, n)$ is the weight variable, $s^{+}$and $s^{-}$are the output input relaxation variables, $x_{j 0}$ and $y_{j 0}$ are the input output vectors of the decision-making unit to be evaluated and $x_{j}$ and $y_{j}$ are the input and output vectors for $D M U_{j}$.

3.2. Mapping Rule from the GO Methodology to Dynamic Bayesian Network

The mapping of the GO methodology to the dynamic Bayesian network can be found in reference [30]. The operators used in the GO methodology in this paper are in classes 1, 5, 6 and 10, as shown in Figures 6-9. These are the corresponding dynamic Bayesian networks for operators 1, 5, 6 and 10. In the figure, (a) is the operator, (b) is the corresponding initial network and transition network, and (c) is the conditional probability table of each node, the data in the table represents the probability values of the nodes of the dynamic Bayesian network in different state combinations. Nodes have two states, where 1 represents a failure state and 2 represents a normal working state.
![img-5.jpeg](img-5.jpeg)

Figure 6. The dynamic Bayesian network corresponding to operator 1. (a) is the operator 1, (b) is the corresponding initial network and transition network, and (c) is the conditional probability table of each node.
![img-6.jpeg](img-6.jpeg)
(c)

Figure 7. The dynamic Bayesian network corresponding to operator 5. (a) is the operator 5, (b) is the corresponding initial network and transition network, and (c) is the conditional probability table of each node.

![img-7.jpeg](img-7.jpeg)

Figure 8. The dynamic Bayesian network corresponding to operator 6. (a) is the operator 6, (b) is the corresponding initial network and transition network, and (c) is the conditional probability table of each node.
![img-8.jpeg](img-8.jpeg)

Figure 9. The dynamic Bayesian network corresponding to operator 10. (a) is the operator 10, (b) is the corresponding initial network and transition network, and (c) is the conditional probability table of each node.

- Operators 1 (two-state unit): Simulation of only two states of the unit (success or failure). When the unit is working, the input signal can go through and there will be an output signal; when the unit fails, the input signal cannot go through and there is no output.

The calculation method of unknown probability value $P_{C}$ and $P_{S}$ in the conditional probability table is the same, see the method in Section 3.1.

$$
\left\{\begin{array}{l}
P_{\mathrm{C} 11}=1 \\
P_{\mathrm{C} 12}=0 \\
P_{\mathrm{C} 21}=P_{\mathrm{C} 2} \cdot \int_{T}^{T+\Delta T} f_{c}(t) d t \\
P_{\mathrm{C} 22}=P_{\mathrm{C} 2} \cdot\left(1-\int_{T}^{T+\Delta T} f_{c}(t) d t\right)
\end{array}\right.
$$

Then, the success probability of the output signal is:

$$
P_{R}(2)=\left(P_{\mathrm{C} 12}+P_{\mathrm{C} 22}\right) \cdot\left(P_{S 12}+P_{S 22}\right)
$$

- Operators 5 (signal generator): As an input of the system, analog power supply, water source, generator, etc.
$P_{R}$ in the transfer network is calculated in the same way as $P_{C}$ of operator 1 , and the probability of success of the output signal is:

$$
P_{R}(2)=P_{R 12}+P_{R 22}
$$

- Operator 6 (signal-on component): A component that requires two inputs to have an output signal.
$P_{S A}, P_{S B}$ and $P_{C}$ in the transfer network are calculated in the same way as $P_{C}$ of operator 1 , and the probability of success of the output signal is:

$$
P_{R}(2)=\left(P_{S A 12}+P_{S A 22}\right) \cdot\left(P_{S B 12}+P_{S B 22}\right) \cdot\left(P_{\mathrm{C} 12}+P_{\mathrm{C} 22}\right)
$$

- Operator 10 (and): Multiple input and one output; only if all input signals are successful will there will be an output signal.
$P_{S A}$ and $P_{S B}$ in the transfer network are calculated in the same way as $P_{C}$ of operator 1 , and the probability of success of the output signal is:

$$
P_{R}(2)=\left(P_{S A 12}+P_{S A 22}\right) \cdot\left(P_{S B 12}+P_{S B 22}\right)
$$

The general mapping process from the GO diagram to the dynamic Bayesian network is as follows:

1. The nonlogical operator and its input signal flow are mapped to the initial network root node of the dynamic Bayesian network, and the transition network child nodes of each root node are established at the same time. The arrow points from the parent node in the initial network to the corresponding child node in the transition network.
2. Each output signal flow except the fifth operator is mapped to a node of the transfer network, and the parent-child connection relationship with all nodes in the transfer network in step 1 is established.
3. The prior probability of the root node of the initial network and the conditional probability table (transition probability) of the corresponding child node of the transition network are determined.
4. The conditional probability table of the child nodes of the transfer network corresponding to all the output signal flow is given.

# 3.3. Specific Steps for Reliability Allocation 

In this paper, the results of the backward reasoning of a dynamic Bayesian network are introduced into the data envelopment analysis method for reliability allocation. When the expected value is less than the required target value $R$, the reliability distribution should be carried out as follows:

# 3.3.1. Division of Units 

The whole smart meter system is divided into n units according to function, that is, n DMUs.

### 3.3.2. Backward Reasoning of Dynamic Bayesian Networks

The backward reasoning of dynamic Bayes is to derive the probability value of each cause variable in the possible state after knowing the state of the result variable. By comparing the probability value, the most likely cause of failure can be obtained. In this paper, the whole reasoning process is completed on Genie 2.1 software. In this paper, backward reasoning also refers to Viterbi decoding, in which known observation data may have multiple interpretations and the maximum possible interpretation is calculated. Hidden variable discrete DBN reasoning can refer to the hidden Markov model (HMM), and any discrete DBN can be transformed into several standard HMMs for reasoning [31]. The HMM model is shown in Figure 10.
![img-9.jpeg](img-9.jpeg)

Figure 10. HMM model.
$X_{t}$ and $Y_{t}$, respectively, represent $1: t$ implicit sequence and observation sequence, $X_{t}$ represents a hidden variable that has n states, $Y_{t}$ represents a discrete variable that has m possible values, and $x_{t}$ and $y_{t}$, respectively, represent the value of the hidden variable and the value of the observed variable, where $x_{t} \in\{1,2, \ldots n\}$ and $y_{t} \in\left\{c_{1}, c_{2}, \ldots c_{m}\right\}$. The output parameter of the model is defined as $P\left(y_{t} \mid x_{t}\right)$, and the main parameters of the model are as follows:

Initial hidden state distribution matrix: $\pi=\left(\pi_{i}\right)_{1 \times n}, \pi_{i}=P\left(x_{1}=i\right)$.
Implicit state transition matrix: $A=\left(a_{i j}\right)_{n \times n^{\prime}} a_{i j}=P\left(x_{t}=i \mid x_{t-1}=j\right)$.
Observation matrix: $B=(b)_{1 \times n}, b_{i}(k)=P\left(y_{t}=k \mid x_{t}=i\right)$.
The HMM parameters are reduced to $\gamma=(A, B, \pi)$.
The reverse reasoning of DBN solves the most likely hidden sequence $X_{T}$ when the parameter $\gamma$ and the observation sequence $Y_{T}$ are known. Applying the Viterbi decoding algorithm to find the hidden sequence $X$ satisfies:

$$
\hat{X}=\underset{x}{\operatorname{argmax}} P(X, Y \mid \gamma)=\underset{x}{\operatorname{argmax}} P(X \mid Y, \gamma)
$$

$\tau_{t}(i)=\max _{x(1), \ldots x(t-1)} P\left(x_{1}, \ldots x_{t-1}, x_{t}=i, Y_{T} \mid \gamma\right)$, and $\delta_{t}(i)$ is defined as a hidden sequence state before $t-1$. The decoding algorithm is as follows:

Initialization:

$$
\begin{gathered}
\tau_{1}(i)=\pi_{i} b_{i}\left(y_{1}\right), 1 \leq i \leq n \\
\delta_{1}(i)=0
\end{gathered}
$$

Recursion:

$$
\begin{gathered}
\tau_{1}(j)=\left[\max _{1 \leq i \leq n} \tau_{t-1}(i) a_{i j}\right] b_{j}\left(y_{t}\right), 2 \leq t \leq T, 1 \leq j \leq n \\
\delta_{t}(j)=\arg \max _{1 \leq i \leq n}\left[\tau_{t-1}(i) a_{i j}\right] b_{j}\left(y_{t}\right)
\end{gathered}
$$

Calculation:

$$
P(\hat{X}, Y \mid \gamma)=\max _{1 \leq i \leq n}\left[\tau_{T}(i)\right]
$$

Backtracking:

$$
\begin{gathered}
\hat{X}_{T}=\arg \max _{1 \leq i \leq n}\left[\tau_{T}(i)\right] \\
\hat{X}_{t}=\delta_{t+1}\left(\hat{X}_{t+1}\right), t=T-1, T-2, \ldots 1
\end{gathered}
$$

Finally, the posterior probability distribution of each hidden node can be obtained.

# 3.3.3. Analysis of Factors Affecting System Reliability 

The factors that affect system reliability, that is, the output indicators of the DEA reliability assignment model, are defined. This paper gives the following three factors:

Failure rate $\lambda_{i}$ : The failure rate of a smart meter refers to the cumulative value of the number of nonhuman irreparable faults in a specified time interval. In this paper, the failure rate of a smart meter is obtained by using the previous statistical data [32]. The failure rate unit for a smart meter and its components is Fit, which indicates the number of failures per billion hours (i.e., $1 \mathrm{Fit}=10^{-9} / h$ ).

The failure probability density function is:

$$
f(t)=\lambda(t) \exp \left(-\int_{0}^{t} \lambda(t) d t\right)
$$

The reliability function is:

$$
R(t)=\exp \left(-\int_{0}^{t} \lambda(t) d t\right)
$$

$\lambda(t)$ represents the probability that a product that has not failed at time $t$ will fail in unit time $t \sim t+\Delta t$. A higher failure rate means that the unit is more prone to failure, which means that higher failure rate should be assigned.

Structural complexity $c_{i}$ : It is the proportion of the number of key components in each unit to the number of key components in the entire system.

$$
c_{i}=n_{i} / \sum_{i=1}^{m} n_{i}
$$

There are $m$ units, and $n_{i}$ is the number of parts in unit $i$. The more complex the structure is, the more complex the problem is, and should not be assigned to lower failure rate.

Posterior probability $p_{i}$ : Based on the reverse reasoning of the dynamic Bayesian network, the probability of system failure caused by each unit is obtained. A posteriori probability represents the importance of each unit to the whole system. The higher a posteriori probability is, the more need to control the occurrence of failure is that the unit should be assigned a higher reliability.

### 3.3.4. Establishment of the DEA Reliability Allocation Model

In [33], 1 is taken as the input indicator value of each unit, and the value of the three factors mentioned above is taken as the output indicator value. Taking the smart meter system as DMU to be evaluated, only the system unit evaluation indicators are DEA effective, and the other DMUs are non-DEA effective. For the relatively effective DMU, the solution of the DEA model can reflect the gap between the DMU and the relatively effective DMU. The output and input indicators of each unit constitute an output-input matrix, based on the output-input matrix and Formula (6), a DEA reliability allocation model is established.

# 3.3.5. Calculation of the Reliability Allocation Weight of Each Unit 

Using DEAP software to solve the reliability allocation model, the relative efficiency of each unit is the result of model evaluation. The relative efficiency value of each unit relative to the smart meter system $D_{i}$ is obtained.

$$
D_{i}=\theta_{i} / \theta_{0}
$$

Then, let us allocate the failure rate of the smart meter with the weighted allocation coefficient of reliability $W_{i}$.

$$
W_{i}=D_{i} / \sum_{j=1}^{n} D_{j}
$$

### 3.3.6. Calculation of Reliability after Allocation

If the target reliability of the system is $R_{S}$, the unreliability of the system cannot exceed $F_{S}$, where $F_{S}=1-R_{S}$. Then, the reliability $R_{i}$ of each unit after allocation is:

$$
\begin{aligned}
& F_{i}=W_{i} \cdot F_{S} \\
& R_{i}=1-F_{i}
\end{aligned}
$$

## 4. Reliability Allocation of the Smart Meter

### 4.1. Reliability Prediction

### 4.1.1. Creation of a GO Diagram for the Smart Meter

According to the system block diagram of the smart meter, the GO diagram of the smart meter is established, as shown in Figure 11.
![img-10.jpeg](img-10.jpeg)

Figure 11. Go diagram of the smart meter.
Using the fault database of smart meters, the failure rate of smart meters in long-term practical applications can be obtained. As shown in Table 2, the type of each operator and the parts it represents can be marked.

Table 2. Operator data.


# 4.1.2. Conversion of the GO Diagram to a Dynamic Bayesian Network 

The GO diagram was transformed into a DBN diagram, and GeNIe2.1 software was used to perform an inferential calculation. As shown in Figure 12, a dynamic Bayesian network is created.
![img-11.jpeg](img-11.jpeg)

Figure 12. Dynamic Bayesian network diagram of the smart meter.
In Figure 12, the component itself is represented by a C (except Class 5 operators), and the corresponding signal flow is represented by an S. The nodes of the component itself point to its own arrow representing the operator's own state from the initial network to the transition network; the other nodes represent the operator's input signal. All components are assumed to be successful in their initial state (i.e., when $\mathrm{t}=0$ (year), $P_{R}(1)=0$ and

$P_{R}(2)=1$ ). The conditional probability table for each component node is entered at $\mathrm{t}=1$ (year), as shown in Table 3.

Table 3. Conditional probability table of components in the first year.


# 4.1.3. Prediction Results 

The data in Table 3 were input into the GeNIe2.1 software for calculation and reasoning, and the reliability of the smart meter and each unit were obtained, as shown in Table 4.

Table 4. Dynamic reliability of the smart meter and its units.


A dynamic reliability profile of the smart meter was drawn, as shown in Figure 13, from the data obtained:

![img-12.jpeg](img-12.jpeg)

Figure 13. Dynamic reliability diagram of the smart meter.
It can be seen from Figure 13 that the reliability of the metering core unit is the lowest and decreases the fastest and is the weakest unit of the smart meter; the display unit is the highest and decreases the slowest. The reliability of the smart meter is 0.994907 in the first year and 0.950224 in the tenth year.

# 4.2. Reliability Allocation 

First, we performed backward reasoning of a dynamic Bayesian network, updated the smart meter to the fault state as evidence in an established dynamic Bayesian network, and used GeNIe2.1 software to perform backward reasoning to obtain the result, as shown in Figure 14.
![img-13.jpeg](img-13.jpeg)

Figure 14. Posterior probability permutation chart of each unit.
Figure 14 shows that, when fault diagnosis is carried out, the metering core and power supply unit have a higher fault probability, which is the main cause of smart meter faults.

The technical specification standard for smart meters [34] stipulates that the design of products and the selection of components should ensure that the whole meter service life is greater than or equal to 10 years. The allowable failure rate of the product due to the quality of the smart meter shall be less than or equal to the specified value in Table 5.

Table 5. Allowable annual failure rate over the lifetime.


Comparing the predicted results in Table 4 with the specified values in Table 5, it is found that the predicted reliability values are less than the specified values and need to be reallocated according to Section 3.3. Therefore, the output and input matrix are obtained as shown in Table 6.

Table 6. Input and output matrix table.


The DEA reliability allocation model is built by inputting the data of the output-input matrix into the DEAP software, and the result is shown in Table 7.

Table 7. Efficiency value of each DMU.


According to Table 7, only the efficiency value of the smart meter system is 1, which means that DEA is effective. Therefore, according to Equations (20) and (21), the influence degree $D_{i}$ of each unit on system reliability and the distribution weight $W_{i}$ of unreliability can be obtained. The results are shown in Table 8.

Table 8. Each decision-making unit $D_{i}$ and $W_{i}$.


According to the reliability $R_{S}$ specified in Table 5, the dynamic reliability of each unit after allocation was obtained by Equations (22) and (23), as shown in Table 9.

Table 9. Dynamic reliability of each unit after allocation.


# 5. Verification of Allocation Results 

The essence of reliability allocation is an optimization problem, and it needs definite requirements and restrictive conditions to perform index allocation. In this paper, the input is as little as possible under the condition of satisfying the lower limit of reliability; in addition, the design requirements and the possibility of actual implementation under the existing technology need to be considered.

Each unit of the smart meter is connected in series, and the failure of any one unit will lead to the failure of the smart meter. Therefore, the dynamic reliability of a smart meter can be obtained by multiplying the reliability of each unit in Table 9, as shown in Table 10.

Table 10. Dynamic reliability of the smart meter after distribution.


Compared with the specified value in Table 5, the reliability of the allocated smart meter fully meets the requirements. Moreover, it meets the design requirements after analysis and can be realized under the existing technical conditions.

The accelerated life test is an effective way to assess product reliability, using acceleration life test methods to assess the reliability of the product in a short time and accurately assess the reliability life of the product. This paper used the acceleration life test to verify the effectiveness of reliability allocation results, and test whether the reliability of smart meters meets the requirements. Sixty samples were prepared according to the allocation result of the reliability. The structure of the sample meter was the same as that of the smart meter for reliability allocation in Section 4, referencing the standard in $[35,36]$ to design the test. The failure rate was defined as less than $4.25 \%$ after 10 years and the confidence rate was $50 \%$, under $85^{\circ} \mathrm{C}$ and $95 \%$ relative humidity; the reference voltage Un, 10 A and power factor of 1 were continuously applied to the smart meter. The total energy was read every 24 h and compared with the smart meter outside the environment box; the test lasted for 24 days.

Figure 15 shows the sample meters in the accelerated life test, and Figure 16 shows the abnormal display of the smart meters in the test. The reliability analysis software of the meter company was used to fit the data of the accelerated life test, and the reliability function of the smart meter was obtained, as shown in Figure 17.

Through the analysis of the accelerated life test, the reliability of the smart meter after reliability allocation met the requirements of technical specifications, which proves that the reliability allocation method proposed in this paper is effective.

![img-14.jpeg](img-14.jpeg)

Figure 15. Sample meter for the accelerating life test.
![img-15.jpeg](img-15.jpeg)

Figure 16. Abnormal display of the sample table.
![img-16.jpeg](img-16.jpeg)

Figure 17. Reliability function diagram of the smart meter obtained by the accelerated life test.

# 6. Conclusions 

In this paper, a smart meter reliability allocation method of multi-method fusion is proposed. First, the GO methodology is used to fuse DBN to predict the reliability. DBN can solve the complex modeling and low accuracy of the GO methodology, and the failure

rate is based on the actual fault information of the smart meter, so this prediction method is more practical, and the result is more accurate. Second, we use the DEA method to establish a smart meter reliability allocation model. This model is a linear planning problem, so the algorithm is simple and the calculation error is small. The posterior probability obtained by the DBN backward reasoning, failure rate and structural complexity of each unit are used as the output indicators of the DEA reliability allocation model. When the DEA realizes multi-index evaluation, it does not rely on subjective evaluation, and the results are more objective. Finally, the reliability allocation results are calculated according to the result of the DEA reliability allocation model. From the allocation result presented in Section 4.2, the reliability of the smart meter in the first year is 0.99802 , and the reliability of the tenth year is 0.958219 . The results of the accelerated life test show that the allocation is reasonable. The allocation method is based on fault data, and the process of modeling and allocation is objective, simple and operable. Based on the actual fault information of products, this method is more practical and can improve the redistribution of reliability and the reliability of smart meters.

This paper comprehensively considers the importance and influence of each unit on the reliability of the whole smart meter, which can be realized in technology, and the allocation method is easy to operate, which strictly ensures the overall reliability of the smart meter. This paper also has some limitations: The dynamic Bayesian network based on the GO diagram is a network with a large number of nodes and a complex relationship; in the iterative computation, the problems such as the termination of the path, the speed of computation, and the number of cycles will all become apparent, and it will be necessary to decompose the dynamic Bayesian network. In the future, according to the characteristics of the GO methodology, it is necessary to establish the segmentation criterion of the GO diagram and decompose it into several independent subgraphs.

Author Contributions: Data curation, Z.W.; formal analysis, J.Z.; investigation, Z.W.; methodology, J.Z. and Z.Y.; software, Z.W.; supervision, Z.Y.; writing-original draft, J.Z. All authors have read and agreed to the published version of the manuscript.
Funding: This project is supported by Basic public welfare research project of Zhejiang province (Grant No. LGG18E050008), the National Natural Science Foundation of China (Grant No. 51675481).

Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: The data presented in this study are available on request from corresponding author.
Conflicts of Interest: The authors declare no conflict of interest.
