# FAULT DIAGNOSIS FOR COMPLEX SYSTEMS BASED ON RELIABILITY ANALYSIS AND SENSORS DATA CONSIDERING EPISTEMIC UNCERTAINTY 

## DIAGNOZOWANIE BŁĘDÓW W SYSTEMACH ZŁOŻONYCH NA PODSTAWIE ANALIZY NIEZAWODNOŚCI ORAZ DANYCH Z CZUJNIKÓW Z UWZGLĘDNIENIEM NIEPEWNOŚCI EPISTEMICZNEJ


#### Abstract

This paper presents an information fusion method to diagnose system fault based on dynamic fault tree (DFT) analysis and dynamic evidential network (DEN). In the proposed method, firstly, it uses a DFT to describe the dynamic fault characteristics and evaluates the failure rate of components using interval numbers to deal with the epistemic uncertainty. Secondly, qualitative analysis of a DFT is to generate the characteristic function via a traditional zero-suppressed binary decision diagram, while quantitative analysis is to calculate some importance measures by mapping a DFT into a DEN. Thirdly, these reliability results are updated according to sensors data and used to design a novel diagnostic algorithm to optimize system diagnosis. Furthermore, a diagnostic decision tree (DDT) is obtained to guide the maintenance workers to recover the system. Finally, the performance of the proposed method is evaluated by applying it to a train-ground wireless communication system. The results of simulation analysis show the feasibility and effectiveness of this methodology.


Keywords: dynamic fault tree, dynamic evidential network, interval numbers, sensors data, diagnostic importance factor.


#### Abstract

W artykule przedstawiono metodę fuzi informaciónużąco do diagnozowania błędów systemu w oparciu o analizę dynamicznego drzewa błędów (DFT) oraz dynamiczną sieć dowodową (DEN). W proponowanej metodzie, pierwszym krokiem jest wykorzystanie DFT do opisania dynamicznych charakterystyk błędów oraz ocena intensywności uszkodzeń komponentów przy użyciu liczb przedziałowych, która rozwiązuje problem niepewności epistemicznej. Krok drugi stanowi jakościowa analiza DFT, która polega na wygenerowaniu funkcji charakterystycznej za pomocą tradycyjnego binarnego diagramu decyzyjnego typu "zero-suppressed" (w którym zostały wyeliminowane wszystkie węzly, których krawędź „1" prowadzi do liścia „0"), oraz analiza ilościowa polegajaca na obliczeniu pewnych miar ważności poprzez odwzorowanie DFT w DEN. W kroku trzecim, otrzymane wyniki niezawodnościowe aktualizuje się zgodnie z danymi z czujników a następnie wykorzystuje do stworzenia nowego algorytmu diagnostycznego do optymalizacji diagnostyki systemu. Powstaje diagnostyczne drzewo decyzyjne (DDT), które stanowi dla pracowników utrzymania ruchu wytyczną w procesie odzyskiwania systemu. Działanie proponowanej metody oceniano poprzez zastosowanie jej do diagnostyki systemu łączności radiowej pociąg-ziemia. Wyniki analizy symulacyjnej wskazują na możliwość praktycznego wykorzystania i skuteczność omawianej metodologii.


Slowa kluczowe: dynamiczne drzewo błędów, dynamiczna sieć dowodowa, liczby przedziałowe, dane z czujników, czynnik ważności diagnostycznej.

## 1. Introduction

With the rapid development of science and technology, application of high dependability safeguard techniques have improved the performance of modern systems greatly on the one hand, but increased the complexity of these systems on the other hand, which significantly raises some challenges in fault diagnosis. These challenges are failure dependency of components and epistemic uncertainty. Usually, some methods of fault tolerance are used to improve the system reliability. The behaviours of components in this system, such as failure priority, functional dependent failures, and sequentially dependent failures should be taken into account. In addition, high reliability makes it extremely difficult to obtain complete fault data because these systems may still be in the early life cycle, which results in the epistemic uncertainty. Thus, the work of fault diagnosis has attracted more attention than before. The aim of a fault diagnosis system is to quickly detect and identify the root causes of these failures based on some in-
formation such as sensors data and operator experience by using some models and algorithms. Several efficient fault diagnosis approaches have been proposed for a variety of systems over the last few decades. Doguc et al. proposed a new fault diagnosis method based on the realtime reliability analysis [7]. Bayesian network (BN) was used to calculate the system reliability, and the real-time system reliability was monitored and compared with the previous values. If the deviations exceeded the set threshold, a heuristic efficient algorithm was used to locate the failed component which had the greatest changes between the prior probability and posterior probability. In the literature [3], a real-time fault diagnosis method for complex systems using objectoriented BN was proposed. It included an off-line BN construction phase and an on-line fault diagnosis phase. However, the construction of BN model requires a large amount of fault data. In [5], a fault diagnosis approach based on the fuzzy neural network and fault tree was proposed. Fuzzy neural network was used to train the relation-

ship between faults and symptoms. Fault tree was used to describe the logical relationship between faults and symptoms. In [13], a new method was proposed to diagnose the bearing fault using evidence network and support vector machine. The fault model construction was established using a data-driven method, and the evidence theory was used to solve the conflicting results from different layer models to increase the diagnosis accuracy. However, the above methods are based on the data-driven fault method which needed lots of fault data and cannot deal with the epistemic uncertainty. A fault diagnosis method for safety instrumentation system based on the fault tree and BN was proposed [6]. It used the static fault tree to construct the fault model of safety instrument system and mapped the fault tree into BN to calculate the importance measure which was used to design the diagnosis algorithm. Nevertheless, this method is unable to describe the dynamic fault characteristics and fails to deal with the epistemic uncertainty. In work of [1], DFT was introduced to model the dynamic fault behaviours and diagnostic importance factor (DIF) was calculated to determine the diagnostic sequence. However, this method determined the diagnosis sequence only by components' DIF, and usually caused minimal cut sets ((MCS)) with a smaller DIF to be checked first, thereby influencing the diagnosis result. Tao et al. presented an improved fault diagnosis method which took components' DIF and MCS's DIF into account to avoid that case [23]. In order to improve the diagnosis efficiency, Assaf et al. proposed a method to incorporate the evidence information from sensors into the diagnostic process based on the DFT [2]. However, the solution for DFT is based on Markov chains, which is ineffective in handing large DFT and modelling power capabilities. Furthermore, it cannot update the reliability results according to the evidence data from sensors, which affects the diagnostic efficiency. Therefore, Duan et al. presented an efficient diagnostic algorithm which used DFT to establish a system failure model and calculated reliability parameters using a discrete time Bayesian network (DTBN) [8]. This approach not only can avoid the state space explosion, but also can incorporate sensor information to update reliability results. Nevertheless, DTBN is an approximate method to solve DFT and there is a contradiction between the accuracy and computational complexity. Furthermore, these diagnosis methods are usually assumed that the failure rates of the components are expressed in crisp values describing their reliability characteristics and cannot cope with the epistemic uncertainty. So, a fuzzy DFT analysis was introduced, which can deal with the uncertainty and model the dynamic fault characteristics [12, 17]. Nevertheless, the solution for the fuzzy DFT was still based on the Markov chains. To overcome these shortcomings, a new fault diagnosis algorithm based on fuzzy set and DFT analysis was proposed [10]. The fuzzy information obtained by fuzzy set theory and domain expert was transformed into quantitative information to obtain the fuzzy failure rates of components. DTBN was used for quantitative analysis. Nevertheless, it is usually difficult to determine the corresponding membership function of each language value. To this end, Duan et al. proposed a new fault diagnosis for complex systems based on dynamic evidential network and multi-attribute decision making [11]. It used interval numbers to express the failure rates of the basic events and obtained the optimal diagnosis sequences based multi-attribute decision making with interval numbers. However, this method failed to incorporate the sensors data to optimize the diagnosis process.

In summary, fault diagnosis methods based on reliability analysis have some following limitations:
(1) Traditional fault diagnosis methods based on reliability analysis generally use a static fault tree or DFT to construct fault model and assume that the failure rates of all events are crisp values, which cannot deal with epistemic uncertainty. Although some researchers put forward the possibility theory [21, 25], fuzzy set theory [4, 15], imprecise probability [18], interval analysis [27] and evidence theory [28], these theories were only used for
the reliability analysis and risk assessment and were not further applied to the fault diagnosis. Furthermore, Markov chains and DTBN are usually used to solve DFT. Markov chains have a bad state space explosion problem and the inability to update the posterior probability of the component based on sensors data. The DTBN based solution for DFT has the contradiction between computational accuracy and computational complexity. That is, its computational accuracy is related to the size of time granularity $n$. As $n$ increases, the conditional probability table has an exponential growth [26]. Although the solution proposed in [16] can solve the problem of calculation accuracy to a certain extent, it cannot fuse the sensors information for backward reasoning.
(2) From the aspect of sensors information fusion, Traditional method appends a sensor layer for capturing evidence onto the DFT without impacting the reliability analysis, and the sensor layer uses static gates to represent evidence information. However, evidence information is only used to update qualitative information to reduce the number of suspected MCS and fails to update the quantitative information, thus unable to reflect the contribution of components to the system failure.
(3) In the view of the diagnosis algorithm, the algorithms based on reliability analysis generally only take the importance measures or posterior probability of components into account [1, 9]. Furthermore, the importance measures are usually crisp values and cannot be used to make decisions under uncertainty.

Motivated by the problems motioned above, this paper proposes an information fusion method to diagnose system fault based on DFT and DEN. DFT is used to establish the system fault model to describe the dynamic fault characteristics. Interval numbers are used to describe the failure rate of components to deal with epistemic uncertainty. Furthermore, an efficient zero-suppressed binary decisions diagrams is used to obtain all MCSs, and a DFT is mapped into a DEN to calculate the reliability parameters. In addition, evidence information from sensors is incorporated to update the qualitative information and quantitative parameters, which are used to design the fault diagnosis algorithm. Finally, a train-ground wireless communication system is given to demonstrate the efficiency of this proposed method.

The remainder of this article is organized as follows. Section 2 presents the model construction and qualitative analysis of DFT. Section 3 introduces the dynamic evidence network and provides a quantitative analysis method by mapping a DFT to a DEN. A novel approach is proposed to incorporate the evidence information to update the reliability results, and an efficient diagnosis algorithm is given in Section 4. Section 5 is devoted to a simple illustration example of the proposed approach. Some conclusions and future research recommendations are given in the final section.

## 2. DFT

### 2.1. Model Construction of DFT

Fault tree is a deductive method to decide the potential causes that may cause the occurrence of a predefined undesired event, generally denoted as the top event. DFT extends a static fault tree to describe the dynamic failure behaviours such as priorities of failure events, spares, and sequence-dependent events. Dynamic gates in DFT include the priority AND gate (PAND), the functional dependency gate (FDEP), the sequence enforcing gate (SEQ), the cold, hot, and warm spare gates (CSP, HSP, WSP). The model construction of the fault tree usually requires an in depth knowledge of the system and its components. It includes the construction of a network topology and the failure rates estimation of components. The former can resort to fault mode and effect analysis and the latter needs to obtain lots of fault data, which

is almost impossible to estimate precisely the failure rates of the basic events in the practical engineering application. In this paper, interval numbers are used to describe the failure rates of the basic events based on the expert elicitation and some data sheet at the design stage.

### 2.2. Qualitative analysis of a DFT

The qualitative analysis of a fault tree can be used to obtain the MCS. Algebraic simplification is the most effective method to solve MCS, but it is not suitable for solving DFT. Zero-suppressed binary decisions diagrams, introduced by Tang, separate timing constraints and logic constraints and convert a DFT into a static fault tree [24]. This algorithm generates the MCS of the corresponding static fault tree using several set operations and then it can be expanded into minimal cut sequences if we consider the timing constraints.

Let $S_{1}, S_{2}$ be the input of MCS for AND gate and MCS for OR gate respectively, several set operations are as follows:

$$
\begin{aligned}
& S_{c}=S_{1} \cap S_{2}, D_{1}=S_{1}-S_{c}, D_{2}=S_{2}-S_{c} \\
& U=D_{1} \cup D_{2}, P=D_{1}+D_{2}, D_{3}=U-P \\
& M C S_{O R}=S_{c} \cup D_{3}, M C S_{A N D}=S_{c} \cup P
\end{aligned}
$$

where $D, S_{c}, U$, and $P$ respectively represent set difference, set intersection, set union, and set product. MCSOR and MCSAND are the output of MCS- OR and MCS- AND respectively.

The MCS generation algorithm is implemented recursively during the depth-first left-most traversal of a fault tree. Firstly, it generates the MCS of the inputs of a connection gate, and then executes some operations to combine the MCS of the inputs into the MCS of the output of the connection gate. Finally, all the minimal cut sequences from the MCS can be obtained by considering the timing constraints [24].

### 2.3. Quantitative analysis of a DFT

Quantitative analysis of a DFT is mainly to calculate the system reliability and some importance measures. DIF is the most frequently used importance measure and is also the cornerstone of diagnosis method based on reliability. From a diagnostic point of view, it allows us to discriminate between components by their importance. It is well known to us all that components with a larger DIF value should be diagnosed first. It can assure a minimal number of system checks while bringing back the system. Reliability parameters are calculated by converting a DFT into a DEN which is introduced in Section 3.

## 3. DEN

### 3.1. EN

D-S evidence theory has a unique ability in the expression of epistemic uncertainties. The evidence theory can be well compatible with the theory of probability. EN consists of BN and D-S evidence theory and includes both advantages [14]. It is a popular analysis tool for representing and managing epistemic uncertainties. An EN is a directed acyclic graph (DAG) used to represent system's uncertain knowledge and system logic in artificial intelligence. An EN is defined as $E N=<G, P>$, where $G=<N, A>$ represents a network graph and $N=\left\{N_{1}, N_{2}, \cdots, N_{k}\right\}$ represents a set of nodes. A node can be a basic variable or an abstraction of a system or component, such as system reliability, component status. A is a set of arcs, which indicate direct conditional relations between the connected nodes. P represents some network parameters in EN. Each network parameter represents the belief distributions that are distributed to a node, and each node $X_{i} \in N$ has a corresponding conditional belief table. The parent node
of node $X_{i}$ is set to $P a\left(X_{i}\right)$ and their relationship is expressed in the formula $P\left(X_{i} \mid P a\left(X_{i}\right)\right)$.

### 3.2. DEN

A DEN extends an EN with adding a temporal dimension. This new dimension is managed by defining different nodes to model variables with respect to different time slices. A DEN includes an initial network and some temporal transition networks. Each time slice corresponds to a static EN, and the time slices are made up of a directed acyclic graph $G_{T}=<V_{T}, E_{T}>$ and the corresponding conditional probabilities. The $V_{T}$ and $E_{T}$ are respectively nodes of time $T$ and directed arcs. A directed arc links two variables belonging to different time slices and $E_{T}^{\text {imp }}$ is used to denote the temporal transition network of time slices. Then $E_{T}^{\text {imp }}$ can be determined by:

$$
E_{T}^{\text {imp }}=\left\{(a, b) \mid a \in V_{T-1}, b \in V_{T}\right\}, T_{0} \leq T \leq T_{0}+N \Delta T
$$

where $T_{0}$ is an initial network.
In the DEN model, $G_{T}$ depends solely upon the present state and the previous state. Thus, the following equation is obtained:

$$
P\left(G_{T} \mid G_{T-\Delta T}, \ldots, G_{T_{0}}\right)=P\left(G_{T} \mid G_{T-\Delta T}\right)
$$

In addition, we define these impacts as transition-belief masses between the focal elements of the variable at time step $k$ and those at time step $k+1$ and the CBT relative to inter-time slices is calculated by Equation 4:

$$
m\left(X_{k+1} \mid X_{k}\right)=\left[\begin{array}{cccc}
m\left(G_{1}^{X_{k+1}} \mid G_{1}^{X_{k}}\right) & \cdots & m\left(G_{Q}^{X_{k+1}} \mid G_{1}^{X_{k}}\right) \\
\vdots & \ddots & \vdots \\
m\left(G_{1}^{X_{k+1}} \mid G_{Q}^{X_{k}}\right) & \cdots & m\left(G_{Q}^{X_{k+1}} \mid G_{Q}^{X_{k}}\right)
\end{array}\right]
$$

### 3.3. System reliability model of DEN

In evidence theory, $\Theta=\left\{W_{i}, F_{i}\right\}$ is the knowledge framework of the component $i$ and the focal elements are defined by:

$$
2^{\Theta}=\left\{\{\varnothing\},\left\{W_{i}\right\},\left\{F_{i}\right\},\left\{W_{i}, F_{i}\right\}\right\}
$$

where $\left\{W_{i}\right\}$ and $\left\{F_{i}\right\}$ denote the working state and failure state respectively. The state of $\left\{W_{i}, F_{i}\right\}$ corresponds to the epistemic uncertainty.

Belief measure (Bel) defines the lower bound of the probabilities that the focal element exists, and plausibility measure (Pl) defines the upper bound of the probabilities that the focal element exists. The basic belief assignment on the system state expresses an epistemic uncertainty, where Bel and Pl measures are not equal and bound the system reliability. Therefore, the basic probability assignment (BPA) of component $i$ can be computed as:

$$
\left\{\begin{array}{l}
m\left(\left\{W_{i}\right\}\right)=\operatorname{Bel}\left(\left\{W_{i}\right\}\right) \\
m\left(\left\{F_{i}\right\}\right)=\mathrm{I}-\operatorname{Pl}\left(\left\{W_{i}\right\}\right) \\
m\left(\left\{W_{i}, F_{i}\right\}\right)=\operatorname{Pl}\left(\left\{W_{i}\right\}\right)-\operatorname{Bel}\left(\left\{F_{i}\right\}\right)
\end{array}\right.
$$

Presumably, the upper and lower bounds of the component's failure probability is equivalent to the BPA in the DEN:

$$
\left\{\begin{array}{l}
m\left(\left\{W_{i}\right\}\right)=1-\overline{P(x)} \\
m\left(\left\{F_{i}\right\}\right)=\underline{P(x)} \\
m\left(\left\{W_{i}, F_{i}\right\}\right)=\overline{P(x)}-P(x)
\end{array}\right.
$$

where $\operatorname{Bel}\left(\left\{F_{i}\right\}\right)=\underline{P(x)}$ and $\operatorname{Pl}\left(\left\{F_{i}\right\}\right)=\overline{P(x)}$.

### 3.4. DFT analysis based on DEN

### 3.4.1. Converting a static logic gate into a DEN

Static logic gates mainly include three gates, AND gate, OR gate and voting gate. This section takes an OR gate for example and provides the schemes to map an OR gate into a DEN. When any of the input components $X_{i}(i=1, \ldots, n)$ of an OR gate fails, the output of the gate fails too. Fig. 1 shows an OR gate and the equivalent DEN. Table 1 gives the conditional probabilities of node $A(T+\Delta T)$ in the DEN. Equation 8 gives the conditional probabilities of output node $E(T+\Delta T)$. A more detailed description of this work can be found in [20].

Table 1. The conditional probabilities of node $A(T+\Delta T)$.


![img-0.jpeg](img-0.jpeg)

Fig. 1. An OR gate and the equivalent DEN

$$
\begin{aligned}
& \left\{P(E=1 \mid A(T+\Delta T)=0, B(T+\Delta T)=1\right)=1 \\
& P(E=1 \mid A(T+\Delta T)=1, B(T+\Delta T)=0)=1 \\
& P(E=1 \mid A(T+\Delta T)=1, B(T+\Delta T)=1)=1 \\
& P(E=1 \mid A(T+\Delta T)=1, B(T+\Delta T)=\{0,1\})=1 \\
& P(E=1 \mid A(T+\Delta T)=\{0,1\}, B(T+\Delta T)=1)=1 \\
& P(E=\{0,1\} \mid A(T+\Delta T)=0, B(T+\Delta T)=\{0,1\})=1 \\
& P(E=\{0,1\} \mid A(T+\Delta T)=\{0,1\}, B(T+\Delta T)=0)=1 \\
& P(E=\{0,1\} \mid A(T+\Delta T)=\{0,1\}, B(T+\Delta T)=\{0,1\})=1 \\
& P(E=1 \mid A(T+\Delta T)=0, B(T+\Delta T)=0)=0
\end{aligned}
$$

### 3.4.2. Converting a dynamic logic gate into a DEN

Some dynamic logic gates are introduced to model the functional and sequential in the DFT. These logic gates include PAND, SEQ, FDEP and spare gates. An FDEP gate will be used to describe how the dynamic logic gates are mapped into DEN. An FDEP gate includes a trigger event and some dependent basic events. The trigger event can be a basic event or an output of another gate in the DFT. The occurrence of a trigger event will force all basic events to occur, which
means all basic events functionally depend upon the trigger event. Fig. 2 shows an FDEP gate and the equivalent DEN. Table 2 and Table 3 show the conditional probabilities of the node $A(T+\Delta T)$ and $E(T+\Delta T)$ respectively.
![img-1.jpeg](img-1.jpeg)

Fig. 2. An FDEP gate and the equivalent DEN
Table 2. The conditional probabilities of the node $A(T+\Delta T)$


Table 3. The conditional probabilities of the node $E(T+\Delta T)$.


### 3.4.3. Calculating reliability results

After DFT model of a system is built, it can be mapped into the equivalent DEN using the approach mentioned above. Reliability results of system can be obtained by resorting to the DEN inference algorithm. Reliability parameters mainly include system unreliability and DIF, which can be used to develop a diagnosis algorithm.

The unreliability of a system is calculated by the following equation:

$$
P_{S}=\left[P_{S}, \overline{P_{S}}\right]=\left[\operatorname{Bel}\left(\left\{F_{S}\right\}\right) \quad P l\left(\left\{F_{S}\right\}\right)\right]
$$

where $\left[\operatorname{Bel}\left(\left\{F_{S}\right\}\right), P l\left(\left\{F_{S}\right\}\right)\right]$ represents the failure probability of a system.

DIF is usually defined as the probability that a basic event has occurred given that the top event has also occurred. The DIF of a component $i$ is given by:

$$
D I F_{i}=P(i \mid S)=\left[\operatorname{Bel}\left(\left\{F_{i \mid S}\right\}\right), P l\left(\left\{F_{i \mid S}\right\}\right)\right]
$$

where $i$ is a component in the system $S ; P(i \mid S)$ is the probability that the basic event $i$ has occurred given the top event has occurred.

Similarly, the DIF of a MCS $n$ is defined by:

$$
D I F_{M C S_{n}}=P\left(M C S_{n} \mid S\right)-\frac{P\left(M C S_{n}\right)}{P(S)}
$$

where $P(S)$ is the unreliability of the system $S ; P\left(M C S_{n} \mid S\right)$ is the failure probability that the MCS $n$ has occurred given the top event has occurred.

For convenience, we calculate the value $P\left(M C S_{n}\right)$ instead of $D I F_{M C S_{n}}$ and use it to design the diagnosis algorithm in the following section.

### 3.5. Importance sorting using possibility-based NSG ranking approach

Based on above analysis, we can obtain the interval value of DIF which can be used to develop an efficient diagnosis algorithm in order to reduce the diagnosis cost. As is known to all, components with a larger DIF are more important from a diagnostic point of view. Thus, the importance ranking of components will be very important for determining a diagnosis sequence. Nevertheless, these interval values are not sufficient to rank components and should be converted into a probability measure. In this paper, a possibility-based NSG ranking method, developed by Nakahara et al. is used to rank DIF of components expressed by interval numbers [19, 22]. This method can be used to compare the DIF of components to provide a guidance for system diagnosis.

For interval numbers $a=\left[a^{-}, a^{+}\right]$and $b=\left[b^{-}, b^{+}\right], \mathrm{l}(\mathrm{a})$ and $l(b)$ respectively denote the lengths of the intervals $a=\left[a^{-}, a^{+}\right]$and $b=\left[b^{-}, b^{+}\right]$, it calculated as follows:

$$
l(a)=a^{+}-a^{-}, l(b)=b^{+}-b^{-}
$$

Then the possibility of $[a] \geq[b]$ can be defined as:

$$
\begin{aligned}
p([a] \geq[b]) & =\min \left\{0,1-\max \left\{\frac{a^{+}-b^{-}}{l(a)+l(b)}, 0\right)\right\} \\
& =\left\{\begin{array}{lc}
1 & a^{-} \geq b^{+} \\
\frac{a^{+}-b^{-}}{l(a)+l(b)} & a^{+}>b^{-} \text {and } a^{-}<b^{+} \\
0 & a^{+} \leq b^{-}
\end{array}\right.
\end{aligned}
$$

A possibility-based NSG ranking method includes the following steps.

Step 1: For a set of interval numbers $a_{i}=\left[a_{i}{ }^{-}, a_{i}{ }^{+}\right] \quad i=1,2, \cdots, n$, compare them with each other, and then the corresponding possibility $p_{i j}=p(a>b)$ can be obtained. So we can establish the probability matrix $P=\left(p_{i j}\right)_{n \times n}$, which is given by:

$$
P=\left(\begin{array}{cccc}
P_{11} & P_{12} & \cdots & P_{1 n} \\
P_{21} & P_{22} & \cdots & P_{2 n} \\
\vdots & \vdots & \ddots & \vdots \\
P_{n 1} & P_{n 2} & \cdots & P_{n n}
\end{array}\right)
$$

Step 2: Denote $\lambda_{i}=\sum_{j=1}^{n} p_{i j}$ as the row sum of the possibility matrix P and $\lambda=\left(\lambda_{1} \quad \lambda_{2} \quad \cdots \quad \lambda_{n}\right)^{T}$ as the corresponding row sum vector.

Step 3: Calculate the ranking vector $\omega=\left(\omega_{i}\right)$ is given by:

$$
\omega_{i}=\frac{1}{n(n-1)}\left(\lambda_{i}+\frac{n}{2}-1\right) \quad i=1,2 \cdots n
$$

According to the ranking vector of the possibility matrix $P$, the interval numbers $a_{i}=\left[a_{i}{ }^{-}, a_{i}{ }^{+}\right] \quad i=1,2, \cdots, n$ can be sorted based on the value of $\omega_{i}$.

## 4. Fault Diagnosis Method based on Reliability Analysis and Sensors data

### 4.1. Model construction of diagnostic sensors

When a system fails, usually several evidence information from sensors can be observed too, and this may be utilized to improve the efficiency of the diagnosis algorithm. In general, the more the number of sensors used to monitor the system, the higher the diagnostic efficiency of the system. However, too many sensors will increase system costs on the one hand, but on the other hand, it will reduce the reliability of the diagnostic system. So a tradeoff between the good points against the bad should be taken into account. Besides, sensors might fail and false information can misguide the diagnosis process. For simplicity, we assume that sensors never fail in the paper. To optimize the diagnosis process, a diagnostic sensors model is constructed to update the qualitative and quantitative information. As we all know, the DEN created from DFT has no evidence nodes representing the evidence information, thus, we need to add them in the DEN. Evidence nodes in the DEN provide links connecting it with the component in the DEN, which are monitored by sensors. The links are directed from the component to the evidence nodes. Evidence nodes in the DEN create a conditional probability table using the probability of producing the observation results. This diagnostic sensors model does not affect the system reliability analysis and can update the qualitative information and quantitative parameters according to sensors data.

### 4.2. Incorporating sensors data

### 4.2.1. Updating the system characteristic function

If sensors detect some failed components, we can use this evidence information to minimize the number of the diagnosed MCS. Since, examining a cut set that caused the system to fail then fixing the failed components in that cut set should recover the system, we can increase the efficiency of fault diagnosis by reducing the number of cut sets examined. The cut sets under evidence (CUE) is the set of all essential MCS obtained after evidence information removes some unsuspected cut sets. We can use evidence information from sensors to simplify the characteristic function of the system in order to obtain the CUE function using the algorithm in [2].

### 4.2.2. Updating DIF

In addition, we can use the evidence information from sensors to update DIF, which reflects objectively the contribution to the system failure. The DIF of the components under the evidence information conditions can be calculated using the Equation (16). Calculating DIF is very simple. We just input the corresponding evidence information

to the DEN and obtain the DIF of components and CUE using the inference algorithm:

$$
D I F_{i}^{\prime}=P(i \mid S, E)=\frac{P(i, E, S)}{P(S) D I F_{E}}
$$

where $i, S$ and $E$ represent a component, system and evidence information, respectively.

### 4.3. Fault diagnosis algorithm

The aim of fault diagnosis is to obtain the optimal check sequence to locate the fault as fast as possible using an efficient diagnosis algorithm. As it is known to all, the direct cause of the system failure is the failure of a CUE. So, we should check CUE one by one to locate the failed component in the system. Only when we finish checking a CUE can we do next. The sequence by which CUE is diagnosed depends on the corresponding DIF, while the sequence of components in the same CUE is determined by their DIF. The CUE with a larger DIF is checked first. Accordingly, the component with a larger DIF in a CUE is checked first. It can assure a minimal number of system checks while bringing the system back. The fault diagnosis algorithm, which incorporates sensors data, is as follows:

Step 1. List all CUEs and rank them according to their DIF.
Step 2. Select the CUE with a highest DIF value and diagnose the component $X$ with a highest DIF in the same CUE.

Step 3. Split all CUEs into those with $X$ and those without.
a) If $X$ has failed test, we take all CUEs that include $X$
$>$ Diagnose all CUEs and the CUE with a higher DIF is checked first.
$>$ The component with a larger DIF in the same CUE is checked first.
b) If $X$ has not failed test, we take the other CUEs
$>$ Select the CUE untested with a highest DIF value.
$>$ And recursively repeat Step2 Step3.

### 4.4. Evaluation of diagnosis algorithm

The diagnosis algorithm can easily be described in the graphical DDT, which can help us recognize the failed components with a map. It is a directed acyclic graph composed of circular nodes and arcs linking parent nodes to child nodes. A node represents a component being tested. Arcs point to the next component to be tested; right arcs point to components within the same cutest as the parent node, and left arcs point to components which are not in the same cutest as the parent node. Moreover, when diagnostician reaches a node and tests the component at the node, the test either fails or passes. If the test fails, then the right arc is traversed indicating the need to repair the tested component in the parent node. If a test passes, then the left arc is traversed indicating that the cut sets which include the tested component in the parent node have not failed.

There are many indicators to evaluate the fault diagnosis algorithm. In this paper, we can evaluate the diagnostic efficiency with the help of the DDT. Traditional evaluation measures only take the test cost or the failure probability
of components into account, and neglect the qualitative information and the importance factors. Thus, we use expected diagnostic cost (EDC) which incorporates the structure information, DIF and test cost into one measure for predicting diagnosis cost. This evaluation index takes the diagnosis accuracy as well as the diagnosis cost into account and also considers the relationship between component failure and system failure. Generally, the diagnostic cost is lower, the diagnostic approach is more efficient. EDC can be computed by:

$$
E D C=\sum_{i=1}^{n} D I F_{C U E_{i}} c p_{i}, c p_{i}=\sum_{j=1}^{m_{i}} t_{c_{j}}
$$

where $D I F_{C U E_{i}}$ is the DIF of the $i^{\text {th }} \mathrm{CUE} ; c p_{i}$ is the sum of all test cost from the top node to the $i^{\text {th }} \mathrm{CUE}$ 's leaf node; $t_{c_{j}}$ is the test cost of the node $c_{j}$.

## 5. A numerical example

Train-ground wireless communication system is a key subsystem of urban rail transit, and its reliability has been improved by the application of high technologies to ensure safe operation. Once breaking down, less causes the operation performance drop, more leads to a disaster. Therefore, an efficient diagnosis strategy should be taken to restore normal operation as soon as possible. A DFT model of a train-ground wireless communication system is shown in Fig.3. It is assumed that all components have the exponential distribution and interval failure rates of components expressed in interval values are shown in Table 4.
![img-2.jpeg](img-2.jpeg)

Fig. 3. DFT model of train-ground wireless communication system

Table 4. Failure rates of components are expressed in interval numbers


Through the qualitative analysis of DFT mentioned above, the system characteristic function (the sum of all MCS) of train-ground wireless communication system is obtained:

$$
\begin{gathered}
F=X 1+X 2+X 3+X 4 X 5+X 4 X 7+X 4 X 9+X 6 X 5+X 6 X 7+X 6 X 9+ \\
X 8 X 5+X 8 X 7+X 8 X 9+X 10 X 11+X 10 X 13+X 10 X 15+X 12 X 11+ \\
X 12 X 13+X 12 X 15+X 14 X 11+X 14 X 13+X 14 X 15
\end{gathered}
$$

The DFT is mapped into a corresponding DEN for quantitative analysis. Assuming the task time $T=1000 \mathrm{~h}$, the probability of system failure can be obtained using the inference algorithm and it is [0.08293, 0.10714]. In addition, the DIF of all components and MCSs can be calculated shown in Table 5 and Table 6 respectively.

Table 5. DIFs of all components


Table 6. DIFs of all MCSs


We assume that a sensor monitors $X 6$ and detects that it is in a work state. We can use this evidence information to simplify the characteristic function and obtain an updated system characteristic function:

$$
\begin{gathered}
F_{C U E}=X 1+X 2+X 3+X 4 X 5+X 4 X 7+X 4 X 9+X 8 X 5+X 8 X 7+ \\
X 8 X 9+X 10 X 11+X 10 X 13+X 10 X 15+X 12 X 11+ \\
X 12 X 13+X 12 X 15+X 14 X 11+X 14 X 13+X 14 X 15
\end{gathered}
$$

In addition, this evidence information can be input into the DEN and the corresponding evidence is as follows:

$$
P(X 6=\{W\})=1, P(X 6=\{W, F\})=P(X 6=\{F\})=0
$$

Using the DEN reasoning algorithm, the updating DIFs of components and CUEs are shown in Table 7 and Table 8 respectively.

Using the sorting method, we can get the order of components:

$$
X 3>X 12(X 13)>X 14(X 15)>X 7>X 2>X 10(X 11)>X 1>X 9>X 5>X 8>X 4
$$

Based on the proposed diagnosis algorithm, we can get the DDT of train-ground wireless communication system without sensors information, shown in Fig. 4 and the corresponding DDT which incorporates sensors information into diagnosis process shown in Fig. 5.

Since the failure probability of CUE is expressed as an interval number, it cannot be directly used to calculate EDC. For convenience, assuming that all components have a unit test cost and test cost of components is independent, we calculate EDC using the median of the interval number in Equation (17). Table 9 shows the EDC of different diagnostic algorithms and indicates the proposed method is more efficient than others.

## 4. Conclusion

In this paper, a novel fault diagnosis approach for complex systems is presented based on DFT analysis and DEN, which aims to deal with two important issues that arise in engineering applications, such as failure dependency and epistemic uncertainty. For the challenge of failure dependency, a DFT is used to describe the dynamic fault behaviours. For the challenge of the epistemic uncertainty, the failure rates of components in complex systems are

A possibility-based NSG sorting method is used to rank the DIF of components and the ranking vectors $\omega_{i}$ of matrices $P$ can be computed as:
$\omega_{i}=(0.0333,0.0402,0.1,0.0544,0.0544,0.0873,0.0873,0.0643$, $0.0643,0.0446,0.0446,0.0889,0.0889,0.0738,0.0738)$

So, the order of the components' DIF is obtained:

$$
X 3>X 12(X 13)>X 6(X 7)>X 14(X 15)>X 8(X 9)>X 4(X 5)>X 10(X 11)>X 2>X 1
$$

Similarly, the ranking of all MCSs can also be obtained:

$$
\begin{aligned}
& X 3>X 6 . X 7>X 12 . X 13>X 12 . X 15(X 13 . X 14)>X 14 . X 15>X 2>X 6 . X 9(X 8 . X 7) \\
& >X 1>X 4 . X 7(X 6 . X 5)>X 10 . X 13(X 12 . X 11)>X 10 . X 15(X 14 . X 11)>X 8 . X 9 \\
& >X 8 . X 5(X 4 . X 9)>X 4 . X 5>X 10 . X 11
\end{aligned}
$$

![img-3.jpeg](img-3.jpeg)

Fig. 4. A DDT of train-ground wireless communication system without sensors information.

Table 7. The updating DIFs of components


Table 8. The updating DIFs of CUEs


Table 9. EDC of Different diagnostic algorithms


expressed in interval numbers. Furthermore, qualitative analysis of a DFT is to generate the characteristic function via a zero-suppressed binary decision diagram, while quantitative analysis is to calculate some importance measures by converting a DFT into a DEN. In addition, these reliability results are updated according to the evidence information from sensors and used to design a novel algorithm to improve the diagnosis efficiency. Finally, a real example is given to demonstrate the feasibility and efficiency of the proposed method. This method takes full advantages of both DFT for modelling and DEN for the uncertainty inference, which is especially suitable to diagnose complex systems.

In the future work, we will focus on how the reliability of sensors influences the diagnosis efficiency.

# Acknowledgement 

This research was funded by China Postdoctoral Science Foundation [2015M580568], National Natural Science Foundation of China [71461021] and Graduate Innovation Foundation of Nanchang University [CX2017185].

# Rongxing DUAN <br> Yanni LIN <br> Yining ZENG 

School of Information Engineering
Nanchang University, 999 Xuefu Rd., Honggutan new district
Nanchang, Jiangxi, China
E-mail: duanrongxing@ncu.edu.cn, Nikkilin@yeah.net, 1244942196@qq.com