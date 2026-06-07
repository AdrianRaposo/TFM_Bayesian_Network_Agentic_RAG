# DIAGNOSIS STRATEGY FOR COMPLEX SYSTEMS BASED ON RELIABILITY ANALYSIS AND MADM UNDER EPISTEMIC UNCERTAINTY 

## STRATEGIA DIAGNOSTYKI DLA SYSTEMÓW ZŁOŻONYCH OPARTA NA ANALIZIE NIEZAWODNOŚCI ORAZ METODACH WIELOATRYBUTOWEGO PODEJMOWANIA DECYZJI MADM W WARUNKACH NIEPEWNOŚCI EPISTEMOLOGICZNEJ


#### Abstract

Fault tolerant technology has greatly improved the reliability of train-ground wireless communication system (TWCS). However, its high reliability caused the lack of sufficient fault data and epistemic uncertainty, which increased significantly challenges in system diagnosis. A novel diagnosis method for TWCS is proposed to deal with these challenges in this paper, which makes the best of reliability analysis, fuzzy sets theory and MADM. Specifically, it adopts dynamic fault tree to model their dynamic fault modes and evaluates the failure rates of the basic events using fuzzy sets theory and expert elicitation to hand epistemic uncertainty. Furthermore, it calculates some quantitative parameters information provided by reliability analysis using algebraic technique and Bayesian network to overcome some disadvantages of the traditional methods. Diagnostic importance factor, sensitivity index and heuristic information values are considered comprehensively to obtain the optimal diagnostic ranking order of TWCS using an improved TOPSIS. The proposed method takes full advantages of the dynamic fault tree for modelling, fuzzy sets theory for handling uncertainty and MADM for the best fault search scheme, which is especially suitable for fault diagnosis of the complex systems.


Keywords: Train-ground wireless communication system, Reliability analysis, MADM, Epistemic uncertainty, TOPSIS.

Technologia odporna na błędy przyczyniła się do dużej poprawy niezawodności systemów łączności bezprzewodowej pociagziemia (TWCS). Jednakże wysoka niezawodność tych systemów pociaga za sobą brak wystarczajacych danych o uszkodzeniach oraz niepewność epistemologiczna, której zwiększenie stworzyło liczne wyzwania w zakresie diagnostyki systemów. W niniejszej pracy zaproponowano nowatorska metodę diagnozowania TWCS, która odpowiada na owe wyzwania wykorzystujac analizę niezawodności, teorię zbiorów rozmytych oraz metody wieloatrybutowego podejmowania decyzji MADM. W szczególności, zaproponowana metoda wykorzystuje dynamiczne drzewa błędów do modelowania dynamicznych stanów niezdatności oraz pozwala na oszacowanie częstości występowania uszkodzeń dla zdarzeń podstawowych z wykorzystaniem teorii zbiorów rozmytych oraz oceny eksperckiej, rozwiazując w ten sposób problem niepewności epistemologicznej. Ponadto, metoda ta umożliwia obliczenie niektórych parametrów ilościowych na podstawie informacji pochodzacych z analizy niezawodności, z zastosowaniem techniki algebraicznej oraz sieci bayesowskich, co pozwala na obejście ograniczeń tradycyjnie stosowanych metod. W artykule przeprowadzono szczegółowa analizę czynnika ważności diagnostycznej, wskaźnika czulości oraz wartości informacji heurystycznej w celu określenia optymalnej kolejności działań diagnostycznych dla TWCS z zastosowaniem poprawionej wersji TOPSIS Proponowana metoda w pełni wykorzystuje zalety metody drzewa błędów do modelowania, teorii zbiorów rozmytych - do rozwiazzywania problemu niepewności oraz MADM - do wyznaczania najlepszej metody wyszukiwania niezdatności, co jest szczególnie przydatne w przypadku diagnozowania niezdatności systemów złożonych.

Słowa kluczowe: system łaczności bezprzewodowej pociag-ziemia, analiza niezawodności, MADM, niepewność epistemologiczna, TOPSIS.

## 1. Introduction

Train-ground wireless communication system (TWCS) is a safe-ty-critical subsystem of urban rail transit and its reliability has a direct effect on the stability and safety of the train operation system. For fast technology innovation, the performance of TWCS has been greatly improved with the wide application of high dependability safeguard techniques on one hand, but on the other hand, its complexity of technology and structure increasing significantly raise challenges in system maintenance and diagnosis. These challenges are shown as follows. (1) Lack of sufficient fault samples. Fault samples integrity has a significant influence on the system diagnostic performance.

However, it is extremely difficult to obtain mass fault samples which need many case studies in practice due to some reasons. One reason is imprecise knowledge in an early stage of the new product design. The other factor is the changes of the environmental conditions which may cause that the historical fault data cannot represent the future failure behaviours. (2) Failure dependency of components. TWCS adopts many redundancy units and fault tolerance techniques to improve its reliability. So the behaviours of components in the system and their interactions, such as failure priority, sequentially dependent failures, functional dependent failures, and dynamic redundancy management, should be taken into account. (3) Uncertainty of diagnostic test cost for components. Usually, different components have different diagnostic

test cost and it is very difficult to estimate a precise diagnostic test cost due to the lack of sufficient data, especially for the new components. Aiming at these challenges, many efficient diagnostic methods have been proposed. Assaf et al. proposed a reliability-based approach to determine the diagnosis order of components using diagnostic importance factor (DIF), which uses the dynamic fault tree to model the failure dependency of components and can, to some extent alleviate fault data acquisition bottleneck [1, 19]. However, the solution for dynamic fault tree was based on Markov Chains (MC) modelwhich is ineffective in handing larger dynamic fault tree and modelling power capabilities. For this purpose, Duan et al. proposed a hybrid diagnosis method using dynamic fault tree and discrete-time Bayesian network (DTBN) [17]. Dynamic logic gates were converted to DTBN and the reliability results were calculated by a standard Bayesian Network (BN) inference algorithm. However, it is an approximate solution for dynamic fault tree and requires huge memory resources to obtain the query variables probability accurately. Furthermore, these diagnostic methods, which are usually assumed that the failure rates of the components are considered as crisp values describing their reliability characteristics, have been found to be inadequate to deal with the challenge (1) mentioned above. Therefore, fuzzy sets theory has been introduced as a useful tool to handle challenges (1) and (3). The fuzzy fault tree analysis model employs fuzzy sets and possibility theory, and deals with ambiguous, qualitatively incomplete and inaccurate information [8, 12-13]. However, these approaches use the static fault tree to model the system fault behaviours and cannot cope with the challenge (2). So fuzzy dynamic fault tree (FDFT) analysis has been introduced [7, 22], which takes into account not only the combination of failure events but also the order in which they occur. Nonetheless, the solution for FDFT is still MC based approach, which has the infamous state space explosion problem. To overcome these difficulties and limitations, Duan et al. proposed a new diagnosis method using fuzzy sets and dynamic fault tree, which use fuzzy sets to evaluate the failure rates of the basic events and uses a dynamic fault tree model to capture the dynamic failure mechanisms [18]. But the solution for the dynamic fault tree is still based on DTBN and cannot avoid the aforementioned problems. Assaf et al. firstly introduced the cost diagnostic importance factor (CDIF) to incorporate the diagnostic test cost into the diagnosis process in order to optimize the fault diagnosis [2]. They assumed the test cost of the components was crisp value, which was highly impracticable and almost impossible to apply. So it cannot deal with the challenge (3). In addition, all the diagnosis algorithms are based on minimal cut sets and DIF or CDIF, which are in essence single attribute decision making, and usually cause minimal cut sets with a smaller DIF to be diagnosed first, thereby influencing the diagnosis result.

Motivated by the problems mentioned above, this paper presents a novel diagnosis strategy for TWCS based on fuzzy sets, dynamic fault tree and MADM shown in Figure 1. It pays particular attention to meeting above three challenges. We adopt expert elicitation and fuzzy sets theory to deal with insufficient fault data and handle the uncertainty problem by treating diagnostic test cost as fuzzy numbers. Furthermore, we use a dynamic fault tree model to capture the dynamic behaviours of the TWCS failure mechanisms and calculate some quantitative parameters information provided by reliability analysis using BN and algebraic technique in order to avoid the aforementioned problems. In addition, components' DIF, sensitivity index (SI) and heuristic information values (HIV) are considered comprehensively to design a novel diagnosis strategy which can locate the fault with the objective of fast and low-cost diagnosis.

The aim of this project is to present the scientific decision for the fault diagnosis of TWCS and offer a new idea for fault diagnosis in complex systems. The rest sections of this paper are organized as
follows: Section 2 provides a brief introduction on TWCS and its dynamic fault tree model. Estimation of failure rates for the basic events is described in Section 3. Section 4 presents a novel dynamic fault tree solution which uses BN and algebraic technique. Section 5 presents a new diagnosis algorithm which makes use of the components' DIF, SI and HIV using MADM solution. The outcomes of the research and future research recommendations are presented in the final section.
![img-0.jpeg](img-0.jpeg)

Fig. 1. Diagnosis framework for TWCS

## 2. Dynamic fault tree of TWCS

Credible wireless communication technology is one of the development directions of communication based train control because it can meet the demands of real-time large amount of information transmission of train-ground. TWCS based on orthogonal frequency division multiplexing adopts some redundancy techniques to ensure higher reliability and is widely applied in the train control system, which transmits real-time data between train and ground. TWCS mainly includes train-ground communication access devices and train-ground communication transmission system. Train-ground communication access devices are responsible for information acquisition, information composition, information decomposition, information encoding, information decoding, and information transmission security mechanism. This can guarantee a safe, reliable and real-time information transmission. Specifically, train-ground communication access devices include decentralized radio control unit (DRCU) and mobile radio control unit (MRCU). DRCU, situated in the decentralized control center, offers the interfaces between the decentralized control system and the traction power supply system and controls the information transmission of the decentralized train-ground communication devices. In addition, it also performs the most challenging tasks such as information acquisition, composition, decomposition, encoding and decoding among the decentralized control system, the vehicle control system, localization system and the traction power supply system. MRCU, located on the opposite ends of the train, not only offers the interfaces between the vehicle control system and the localization system, but also implements information processing among the vehicle control system, the localization system, the decentralized control system and the traction power supply system. Train-ground communication transmission system includes ground radio transceiver equipment, mobile radio transceiver equipment and wireless communication channel. It is its responsibility for the reliable, transparent data transmission between train and ground devices.

TWCS is a typically complex system and adopts redundancy techniques to ensure higher reliability. For example, the hardware redundancy technique is employed in the design of DRCU and MRCU. High coupling degree together with complicated logic relationships exists between these modules. So the dynamic behaviours of components in these modules and their interactions, such as failure priority, sequentially dependent failures, functional dependent failures, and dynamic redundancy management, should be taken into consideration. Obviously, traditional static fault tree is unsuitable to model these dynamic fault behaviours. Therefore, we use the dynamic fault tree model to capture the dynamic behaviours of system failure mechanisms such as

![img-1.jpeg](img-1.jpeg)

Fig. 2. Dynamic fault tree of TWCS
sequence-dependent events, spares and dynamic redundancy management, and priorities of failure events. Taken reception failure of the operation control location signals as the top event, the dynamic fault tree of TWCS is shown in Figure 2.

## 3. Estimation of failure rates for TWCS

In order to calculate some reliability parameters for diagnosis, failure rates of the basic events must be known. However, fault tolerant technology has greatly improved the system reliability and its high reliability caused the lack of sufficient fault data and epistemic uncertainty. For this reason, it is very difficult to estimate precisely the failure rates of the basic events, especially for the new equipment.
![img-2.jpeg](img-2.jpeg)

Fig. 3. Structure of the estimation of failure rates for TWCS

In this study, the expert elicitation through several interviews and questionnaires and fuzzy sets theory are used to estimate the failure rates of the basic events through qualitative data processing. An overall architecture of the estimation of failure rates for TWCS is shown in Figure 3.

### 3.1. Experts evaluation

Experts are people who are familiar with the system and understand the system working environment and the system operation. Therefore, experts can be selected from different fields, such as the design, installation, maintenance, operation and management of the system, to judge the failure rates of the basic events. They are more comfortable justifying event failure likelihood using qualitative natural languages based on their experiences and knowledge about the system, which capture uncertainties rather than by expressing judgments in a quantitative manner. The granularity of the set of linguistic values commonly used in engineering system safety is from four to seven terms. In this paper, the component failure rate is defined by seven linguistic values, i.e. very high, high, reasonably high, moderate, reasonably low, low and very low.

### 3.2. Fuzzification module

Experts evaluation expressed in terms of qualitative natural languages should be converted into the operational format of fuzzy numbers, for example, trapezoidal fuzzy numbers. This function can be implemented by fuzzification module. The objective of fuzzification module is to quantify the basic event qualitative data into their corresponding quantitative data in the form of membership

function of fuzzy numbers. In addition, each predefined linguistic value has a corresponding mathematical representation and the shapes of the membership functions to mathematically represent linguistic variables in engineering systems are illustrated in Figure 4. To eliminate bias coming from an expert, six experts are asked to justify how likely a basic event will fail in the system under investigation. Therefore, it is necessary to combine or aggregate these opinions into a single one. There are many approaches to aggregate fuzzy numbers. An appealing approach is the linear opinion pool [6]:

$$
M_{i}=\sum_{j=1}^{n} \omega_{j} A_{i j}, \quad i=1,2,3, \ldots, m
$$

where $m$ is the number of basic events; $A_{i j}$ is the linguistic expression of a basic event $i$ given by expert $j ; n$ is the number of the experts; $\omega_{i j}$ is a weighting factor of the expert $j$ and $M_{i}$ represents combined fuzzy number of the basic event $i$.
![img-3.jpeg](img-3.jpeg)

Fig. 4. Fuzzy numbers used for representing linguistic value
Usually, an $\alpha$-cut addition followed by the arithmetic averaging operation is used for aggregating more membership functions of fuzzy numbers of different types. The membership function of the total fuzzy numbers from $n$ experts' opinion can be computed as follows:

$$
f(z)=\max _{z=x_{1}+x_{2}+\ldots \ldots+x_{n}}\left[\omega_{1} f_{1}(x) \wedge \omega_{2} f_{2}(x) \wedge \ldots \wedge \omega_{n} f_{n}(x)\right]
$$

where $f_{n}(x)$ is the membership function of a fuzzy number from expert $n$ and $f(z)$ is the membership function of the total fuzzy numbers.

### 3.3. Calculating fuzzy fault rates of the basic events

Apparently, the final quantitative data taken from the fuzzification module are still in the form of fuzzy numbers and cannot be used for fault tree analysis because they are not crisp values. So, fuzzy number must be converted to a crisp score, named as fuzzy possibility score (FPS) which represents the most possibility that an expert believes occurring of a basic event. This step is usually called defuzzification. There are several defuzzification techniques. It is very important to choose a suitable defuzzification technique for a specific application. We use an area defuzzification technique to realize this algorithm, which has lowest relative errors and the closest match with the real data [16]. If ( $\mathrm{a}, \mathrm{b}, \mathrm{c}, \mathrm{d} ; 1$ ) is a trapezoidal fuzzy number, then its area defuzzification technique is as follows:

$$
F P S=\frac{(a+2 b-2 c-d)\left((2 a+2 b)^{2}+(c+d)(-3 a+2 c-d)-2 c(3 b+d)-4 a b\right)}{18(a+b-c-d)^{2}}
$$

The event fuzzy possibility score is then converted into the corresponding fuzzy failure rate, which is similar to the failure rate. Based on the logarithmic function proposed by Onisawa [14], which utilizes the concept of error possibility and likely fault rate, the fuzzy failure rate can be obtained by the following equation (4). Table 1 shows the fuzzy failure rates of the basic events for TWCS.

$$
F F R=\left\{\begin{array}{cc}
1 & F P S \neq 0 \\
10^{\left[\frac{1-F P S}{F P S}\right]^{2}+2.301} \\
0, & F P S=0
\end{array}\right.
$$

Table 1. Basic events' FPS and FFR


## 4. Calculating reliability parameters using BN and algebraic technique

After the dynamic fault tree is constructed and all basic events have their corresponding failure rates with the exponential distribution function, reliability results of TWCS can be calculated by solving the dynamic fault tree. Traditional solution for dynamic fault tree is based on MC model [11], which has the infamous state space explosion problem and cannot solve a larger dynamic fault tree. Therefore, DTBN was proposed to solve the dynamic fault tree in [3-4]. Dynamic logic gates are converted to DTBN and the reliability results are calculated using a standard BN inference algorithm. However, this is an approximate solution and requires huge memory resources to obtain the probability distribution accurately. In addition, as the number of intervals increases, the accuracy and execution time increases greatly. An innovative algorithm has been introduced to reduce the dimension of conditional probability tables by an order of magnitude [9]. However, this method cannot perform posterior probability updating. In the following section, we present an improved method to calculate the reliability parameters using BN and algebraic technique to overcome the disadvantages mentioned above.

### 4.1. Mapping static fault tree into BN

There is a clear correspondence between static fault tree and BN. The fault tree can be seen as a particular deterministic case of the BN. Conceptually it is straightforward to map a fault tree into a BN: one only needs to "re-draw" the nodes and connect them while correctly enumerating reliabilities. Figure 5 shows the conversion of an OR and an AND gate into equivalent nodes in a BN. Parent nodes A and B

![img-4.jpeg](img-4.jpeg)

Fault tree: AND gate

![img-5.jpeg](img-5.jpeg)

![img-6.jpeg](img-6.jpeg)

Fault tree: OR gate

![img-7.jpeg](img-7.jpeg)

Fig. 5 The Equivalent BN of OR and AND Gate

are assigned prior probabilities, which coincide with the probability values assigned to the corresponding basic nodes in the fault tree, and child node C is assigned its conditional probability table (CPT). Since the OR and AND gates represent deterministic causal relationships, all the entries of the corresponding CPT are either 0 or 1. The detailed algorithm of converting a fault tree into a BN was proposed in [3, 15].

### 4.2. Fault Probability of a Module with Sequence Dependence

Let us consider an event sequence composed of *n* events, *e*₁, *e*₂, ..., *e*ₙ including several spare events. An event in the sequence is denoted by *e*′*j*, which means that the event that failed in the *j*-th order of the sequence is designated a spare of an event that failed in the *i*-th order. *e*′*j* denotes an event that was originally in active mode. *e*′*j* (*i* > 0, *i* < *j*) has a dormancy factor 0 ≤ α*j* ≤ 1. The sequence probability of <*e*₁¹, *e*₂², ..., *e*ₙᵐ > can be calculated using the *n*-tuple integration as:

$$
\begin{aligned}
Pr(< e_1^{1}, e_2^{12}, \dots, e_n^{in} >)(t) &= \int_0^t \int_0^{x_0} \dots \int_0^{x_2} \prod_{e_j^1 \in S_{\alpha}} f_j(x_j) \prod_{e_j' \in S_{\omega}} f_{j\alpha}(x_j) \\
&\times \prod_{e_j' \in S_{\omega}} \bar{F}_{j\alpha}(x_i) f_j(x_j - x_i) dx_i dx_2 \dots dx_n
\end{aligned}
\tag{5}
$$

where *x*ₙ indicates the occurrence time of *e*′*j*, *f*ₙ *x* is the probability distribution function of *e*′*j* and *F*jα(*x*) is the survival function of *e*′*j* in standby mode. *S*ₙ is a set of events that were originally in active mode and *S*ₙ (*S*ₙ) is a set of spare events that fail in active (standby) mode [20].

When the failure time of *e*′*j* in active mode follows an exponential distribution with λ*j*, the sequence probability is:

$$
Pr(< e_1^{1}, e_2^{12}, \dots, e_n^{in} >)(t) &= \prod_{e_j' \in S_{\alpha}} \alpha_j L^{-1} \left[ \frac{1}{x} \prod_{i=1}^{n} \left( \frac{\lambda_i}{x + a_i} \right) \right] \tag{6}
$$

where *a*ₙ = ∑_k=1^n λ_k - ∑_k=1^n (1 - α_k) λ_k - ∑_k=1^n (1 - α_j) λ_j, for *a*ₙ > 0 *e*′*k* ∈ *S*ₙ *e*′*k* ∈ *S*ₙ and *L*<sup>−1</sup> is the inverse Laplace transform operator.

If every *a*ₙ in the above equation is distinct from the other, the sequence probability is:

$$
Pr(< e_1^{1}, e_2^{12}, \dots, e_n^{in} >)(t) = \prod_{e_j' \in S_{\alpha}} \alpha_j \prod_{i=1}^{n} \lambda_i \sum_{k=0}^{n} \frac{e^{-a_k t}}{\prod_{j=0, j \neq k}^{n} (a_j - a_k)} \tag{7}
$$

where *a*₀ = 0.

### 4.3. Mapping dynamic fault tree into BN

Dynamic fault tree extends traditional fault tree by defining special gates to capture the components' sequential and functional dependencies. Currently there are six types of dynamic gates defined: the functional dependency gate (FDEP), the cold, hot, and warm spare gates (CSP, HSP, WSP), the priority AND gate (PAND), the sequence enforcing gate (SEQ). Here, we briefly discuss the FDEP and the WSP gates as they will be later used in our examples.

#### (1) WSP Gate

The WSP gate has one primary input and one or more alternate inputs. The primary input is initially powered on and the alternate inputs are in standby mode. When the primary fails, it is replaced by an alternate input, and in turn, when this alternate input fails, it is replaced by the next available alternate input, and so on and so forth. In standby mode, the component failure rate is reduced by a factor α called the dormancy factor. α is a number between 0 and 1. A cold spare has a dormancy factor α=0; and a hot spare has a dormancy factor α=1. The WSP gate output is true when the primary and all the alternate inputs fail. Figure 6 shows the WSP gate and its equivalent BN. Table 2 shows the CPT of the node A. Supposing that A and S follow the same exponential distribution with λ; Here, *p*₁(*t*) and *p*₂(*t*) in this table can be derived as:

$$
p_1(t) = P(A = 1 | S = 0) = \frac{P(S = 0, A = 1)}{P(S = 0)} = 1 - e^{-\lambda_1 t} \tag{8}
$$

$$
p_2(t) = P(A = 1 | S = 1) = \frac{P(S = 1, A = 1)}{P(S = 1)} = \frac{P(< P, A^S >)(t) + P(< A, S >)(t)}{F_S(t)} = P(< P, A^S >)(t) \quad \text{and} \quad P(< A, S >)(t) \quad \text{are sequence probabilities calculated by equation (10)}.
$$

$$
P(< P, A^S >)(t) + P(< A, S >)(t) = 1 - e^{-\lambda t} + \frac{e^{-(\lambda + \lambda t t)t} - e^{-\lambda t}}{\alpha} \tag{10}
$$

The output of node WSP is an AND gate whose CPT is shown in Figure 5.

Table 2. The CPT of the node $A$


![img-8.jpeg](img-8.jpeg)

Fig. 6. WSP and its equivalent $B N$

## (2) FDEP Gate

FDEP is used to model situations where one component's correct operation is dependent upon the correct operation of some other component. It has a single trigger input, which could be another basic event or the output of another gate, a non-dependent output reflecting the status of the trigger, and one or more dependent basic events. Figure 7 shows FDEP gate and its equivalent BN. Table 3 shows the CPT of the node A. Here, $p_{3}(t)$ in this table can be derived as:

$$
p_{3}(t)=P(A=1 \mid T=0)=1-e^{-\lambda_{i} t}
$$

The CPT of output node FDEP is shown in Table 4.
![img-9.jpeg](img-9.jpeg)

Fig. 7. FDEP and its equivalent $B N$

Table 3. The CPT of the node $A$


Table 4. The CPT of the node FDEP


### 4.4. Calculating reliability parameters

According to the dynamic fault tree shown in Figure 2 and the basic failure data shown in Table 1, we can map the dynamic fault tree into an equivalent BN using the proposed method. Its equivalent BN is given in Figure 8. Once the structure of a BN is known and all the probability tables are filled, it is straight forward to calculate the reliability parameters of TWCS using the inference algorithm. These reliability parameters mainly include system reliability, DIF and SI.

## (1) System reliability

Assume the mission time of TWCS is 1000 hours. We can calculate the system unreliability using the following equation:

$$
P(S)=P(S=\text { state } 1)=0.1036
$$

## (2) DIF

DIF is defined conceptually as the probability that an event has occurred given the top event has also occurred. DIF is the corner stone of reliability based diagnosis methodology. This quantitative measure allows us to discriminate between components by their importance from a diagnostic point of view. Components with larger DIF are checked first. This assures a reduced number of system checks while fixing the system:

$$
D I F_{i}=P(i \mid S)
$$

where $i$ is a component in system $S$.
Suppose the system has failed at the mission time 1000 hours, we enter the evidence that TWCS has failed i.e. $P(S=$ state $1)=1$ and calculate DIF using the jointree algorithm.

## (3) SI

Sensitivity analysis allows the designer to quantify the importance of each of the system's components and the impact the improvement of component reliability will have on the overall system reliability. Here we show how one can perform sensitivity through the usage of SI [10]. SI of the $i^{\text {th }}$ basic event is defined as:

$$
\begin{aligned}
& \alpha_{S I, i}=\frac{\gamma_{i}}{\gamma_{\max }} \quad i=1,2, \cdots, m \\
& \gamma_{i}=1-\frac{P(S \mid \bar{i})}{P(S)} \\
& \left.\gamma_{\max }=\max \left\{\gamma_{1}, \gamma_{2}, \cdots \gamma_{m}\right\}\right.
\end{aligned}
$$

where $P(S)$ is the probability of the top event failure; $P(S \mid \bar{i})$ is the probability that the top event has occurred given the basic event $i$ has not occurred.

## 5. Diagnosis strategy based on MADM

MADM models try to answer the question of 'what is the best alternative?' given a set of selection attributes and a set of alternatives. Generally there are three independent steps in MADM models to obtain the ranking of alternatives [23]: (1) Determine the relevant attribute and alternatives. (2) Attach numerical measures to the relative importance of the attribute and to the impacts of the alternatives on these attribute. (3) Calculation procedures to determine a ranking score of each alternative. Technique for Order Preference by Similarity to Ideal Solution (TOPSIS) is one of the known classical methods to solve MADM problem, developed by Hwang and Yoon [5]. It bases on the concept that the chosen alternative should have the shortest

![img-10.jpeg](img-10.jpeg)

Fig. 8. The equivalent $B N$ of $T W C S$
distance from the positive ideal solution (PIS) and the farthest from the negative ideal solution (NIS). In the process of TOPSIS, the performance ratings and the weights of the attributes are usually given as crisp values. Under many conditions, crisp data are not sufficient to model real-life situations. Since human opinions are often vague and cannot estimate his performance with an exact numerical value. A more realistic approach may be to use linguistic assessments instead of numerical values, that is, to suppose that the ratings of the attributes are assessed by means of linguistic variables. In this paper, we treat the optimal diagnostic sequence problem as a MADM problem and propose an improved TOPSIS to solve the MADM problem.

### 5.1. Constructing diagnostic decision table for TWCS

DIF enables us to discriminate between components by their importance from a diagnostic point of view. SI allows the designer to quantify the importance of each of the system's components and the impact the improvement of component reliability will have on the overall system reliability. So we treat DIF and SI as attribute $v 1$ and $v 2$ respectively. Owing to the different complexity of components their test costs are different. A balance should be taken into account between the DIF and test costs. Therefore, we introduce a new measure of importance called HIV, which allows us to optimize the cost of diagnosis. This measure is simply the DIF per unit cost. HIV appears in the following equation (15):

$$
H I V_{i}=D I F_{i} / T_{i}
$$

where $D I F_{i}$ is the DIF of the component $i ; T_{i}$ is the test cost of the component $i$.

Test costs of the components are usually very difficult to express as crisp values because of uncertainty. So we introduce fuzzy linguistic expression to assess the test costs of components. Table 5 and 6 show the evaluation standards of the test costs and components' test costs for TWCS, respectively. HIV has an important effect on the diagnostic sequence and is treated as attribute $v 3$. Table 7 shows the diagnostic decision table for TWCS.

Table 5. Evaluation standards of the test costs


### 5.2. Normalizing diagnostic decision table

Different attributes usually have different values and dimensions, which are not always directly comparable, so we should normalize the diagnostic decision table [21]. For the quantitative data, we normalize them with the following equation:

$$
b_{i j}=\frac{a_{i j}}{\sqrt{\sum_{i=1}^{n} a_{i j}^{2}}}, 1 \leq i \leq 15,1 \leq j \leq 3
$$

where $a_{i j}$ is the $j^{\text {th }}$ attribute value of the $i^{\text {th }}$ component.

For the fuzzy numbers, we normalize them with the following equation:

$$
b_{i j}^{\prime}=\frac{a_{i j}^{\prime}}{\sqrt{\sum_{i=1}^{n}\left\|a_{i j}\right\|^{2}}}, b_{i j}^{m}=\frac{a_{i j}^{m}}{\sqrt{\sum_{i=1}^{n}\left\|a_{i j}\right\|^{2}}}, b_{i j}^{\prime}=\frac{a_{i j}^{\prime}}{\sqrt{\sum_{i=1}^{n}\left\|a_{i j}\right\|^{2}}}
$$

Table 6. Components' test costs for TWCS


Table 7. The diagnostic decision table for TWCS


where $\tilde{a}_{i j}=\left\{a_{i j}^{j}, a_{i j}^{m}, a_{i j}^{r}\right\}, \tilde{b}_{i j}=\left\{b_{i j}^{j}, b_{i j}^{m}, b_{i j}^{r}\right\} ; \left\|\tilde{a}_{i j}\right\|$ is the module of the triangular fuzzy number $\tilde{a}_{i j}$ :

$$
\left\|\tilde{a}_{i j}\right\|=\sqrt{\frac{1}{3}\left[\left(a_{i j}^{j}\right)^{2}+\left(a_{i j}^{m}\right)^{2}+\left(a_{i j}^{r}\right)^{2}\right]}
$$

We can obtain the normalized diagnostic decision table shown in Table 8 for TWCS using equation $(16) \sim(18)$. Considering the same importance of each attribute, we can construct the weighted normalized diagnostic decision table shown in Table 9.

### 5.3. Determining the optimal diagnosis sequence

Attributes can be divided into two groups: beneficial attributes where higher values are preferable and non-beneficial attributes where lower value is preferable. There are three attributes in diagnostic decision table and they belong to the beneficial attributes. When the at-

Table 8. The normalized diagnostic decision table


Table 9. The weighted normalized diagnostic decision table


tributer $a_{i j}$ is a beneficial attribute, the positive and negative ideal solutions are calculated as:

$$
\begin{aligned}
& \tilde{X}_{j}^{+}=\left\{\tilde{r}_{1}^{+}, \tilde{r}_{2}^{+}, \cdots, \tilde{r}_{k}^{+}\right\}=\left\{\max _{i} r_{i j}^{j}, \max _{i} r_{i j}^{m}, \max _{i} r_{i j}^{r}\right\} \\
& \tilde{X}_{j}^{-}=\left\{\tilde{r}_{1}^{-}, \tilde{r}_{2}^{-}, \cdots, \tilde{r}_{k}^{-}\right\}=\left\{\min _{i} r_{i j}^{j}, \min _{i} r_{i j}^{m}, \min _{i} r_{i j}^{r}\right\}
\end{aligned}
$$

where $\tilde{r}_{j}^{+}$is the maximal value of the $j^{\text {th }}$ attribute and $\tilde{r}_{j}^{-}$is the minimal value of the $j^{\text {th }}$ attribute

When the attributer $a_{i j}$ is a non-beneficial attribute, the positive and negative ideal solutions are calculated as:

$$
\begin{aligned}
& \tilde{X}_{j}^{+}=\left\{\min _{i} r_{i j}^{j}, \min _{i} r_{i j}^{m}, \min _{i} r_{i j}^{r}\right\} \\
& \tilde{X}_{j}^{-}=\left\{\max _{i} r_{i j}^{j}, \max _{i} r_{i j}^{m}, \max _{i} r_{i j}^{r}\right\}
\end{aligned}
$$

The distance of each alternative from $\tilde{X}_{j}^{+}$and $\tilde{X}_{j}^{-}$can be currently calculated as:

$$
\begin{aligned}
& D_{i}^{+}=\sqrt{\sum_{j=1}^{k}\left[\tilde{r}_{i j}-\tilde{r}_{j}^{+}\right]^{2}} \\
& D_{i}^{-}=\sqrt{\sum_{j=1}^{k}\left[\tilde{r}_{i j}-\tilde{r}_{j}^{-}\right]^{2}}
\end{aligned}
$$

A closeness coefficient is defined to determine the ranking order of all alternatives once the $D_{i}^{+}$and $D_{i}^{+}$of each alternative has been calculated. The closeness coefficient of each alternative is calculated as:

$$
C_{i}=D_{i}^{-} /\left(D_{i}^{+}+D_{i}^{-}\right)
$$

Table 10 shows the distance of each alternative from the positive and negative ideal solutions together with the corresponding closeness coefficient. Obviously, an alternative comes closer to the PIS and farther from NIS as $C_{i}$ approaches to 1 . Therefore, we can determine the ranking order of all alternatives and choose the best one from among a set of feasible alternatives. According to Table 10, we can obtain the optimal diagnostic ranking order of TWCS: X3, X6(X7), X8(X9), X12(X13), X14(X15), X4(X5), X10(X11), X2, X1, which considers the DIF, SI and HIV comprehensively.

## 6. Conclusion

In this paper, we have discussed the use of dynamic fault tree, fuzzy sets theory and MADM to diagnose the complex systems fault. Specifically, it has emphasized three important issues that arise in engineering diagnostic applications, namely the challenges of insufficient fault data, uncertainty and failure dependency of components. In terms of the challenge of insufficient fault data and uncertainty, we

Table 10. The corresponding closeness coefficient of components


adopt expert elicitation and fuzzy sets theory to evaluate the failure rates of the basic events for TWCS; In terms of the challenge of failure dependency, we use a dynamic fault tree to model the dynamic behaviours of system failure mechanisms. Furthermore, we calculate
some reliability parameters used for fault diagnosis using BN and algebraic technique in order to avoid the aforementioned disadvantages. In addition, we treat the optimal diagnostic sequence problem as a MADM problem, propose an improved TOPSIS to solve the MADM problem and obtain the optimal diagnostic ranking order of TWCS. The proposed method makes full use of the dynamic fault tree for modelling, fuzzy sets theory for handling uncertainty and MADM for the best fault search scheme, which is especially suitable for fault diagnosis of the complex systems.

In the future work, we will focus on how to determine the attributes weights and take full advantage of the previous fault diagnosis results to dynamically update the diagnostic decision table, thereby optimizing the diagnosis efficiency.

## Acknowledgement

This work was supported by the National Natural Science Foundation of China (71461021), the Natural Science Foundation of Jiangxi Province (20142BAB207022), the Science and Technology Foundation of Department of Education in Jiangxi Province (GJJ14166) and the Postdoctoral Science Foundation of Jiangxi Province
(2014KY36).
s

# Rongxing DUAN Huilin ZHOU Jinghui FAN <br> School of Information Engineering <br> Nanchang University <br> Xuefu Rd., 999 Jiangxi, China <br> E-mail: duanrongxing@ncu.edu.cn, zhouhuilin@ncu.edu.cn, Jinghuifan@ncu.edu.cn