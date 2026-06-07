# Process accident prediction using Bayesian network based on IT2Fs and Z-number: A case study of spherical tanks 

Mostafa Mirzaei Aliabadi ${ }^{1}$, Rouzbeh Abbassi ${ }^{2}$, Omid Kalatpour ${ }^{1}$, Omran Ahmadi ${ }^{3}$, Vahid Ahmadi Moshiran ${ }^{1 *}$<br>1 Center of Excellence for Occupational Health, Occupational Health and Safety Research Center, School of Public Health, Hamadan University of Medical Sciences, Hamadan, Iran, 2 School of Engineering, Faculty of Science and Engineering, Macquarie University, Sydney, NSW, Australia, 3 Department of Occupational Health and Safety, Faculty of Medical Science, Tarbiat Modares University, Tehran, Iran<br>* v.ahmadi@edu.umsha.ac.ir

## 6 OPEN ACCESS

Citation: Aliabadi MM, Abbassi R, Kalatpour O, Ahmadi O, Moshiran VA (2024) Process accident prediction using Bayesian network based on IT2Fs and Z-number: A case study of spherical tanks. PLoS ONE 19(8): e0307883. https://doi.org/ 10.1371/journal.pone. 0307883

Editor: Muhammet Gul, Istanbul University: Istanbul Universitesi, TÜRKIYE

Received: May 31, 2024
Accepted: July 12, 2024
Published: August 29, 2024
Copyright: © 2024 Aliabadi et al. This is an open access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

Data Availability Statement: All required data titled "Analyzing Bayesian Network Data, Beta Distribution, and IT2F-Z" is available through the link and DOI below. URL: https://zenodo.org/ records/12657074 DOI: 10.5281/zenodo. 12657073.

Funding: This research is supported by Hamadan University of Medical Sciences (Grant No: 140107266216). The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.


#### Abstract

This study aimed to propose a novel method for dynamic risk assessment using a Bayesian network (BN) based on fuzzy data to decrease uncertainty compared to traditional methods by integrating Interval Type-2 Fuzzy Sets (IT2FS) and Z-numbers. A bow-tie diagram was constructed by employing the System Hazard Identification, Prediction, and Prevention (SHIPP) approach, the Top Event Fault Tree, and the Barriers Failure Fault Tree. The experts then provided their opinions and confidence levels on the prior probabilities of the basic events, which were then quantified utilizing the IT2FS and combined using the Z-number to reduce the uncertainty of the prior probability. The posterior probability of the critical basic events (CBEs) was obtained using the beta distribution based on recorded data on their requirements and failure rates over five years. This information was then fed into the BN. Updating the BN allowed calculating the posterior probability of barrier failure and consequences. Spherical tanks were used as a case study to demonstrate and confirm the significant benefits of the methodology. The results indicated that the overall posterior probability of Consequences after the failure probability of barriers displayed an upward trend over the 5-year period. This rise in IT2FS-Z calculation outcomes exhibited a shallower slope compared to the IT2FS mode, attributed to the impact of experts' confidence levels in the IT2FS-Z mode. These differences became more evident by considering the $10^{-4}$ variance compared to the $10^{-5}$. This study offers industry managers a more comprehensive and reliable understanding of achieving the most effective accident prevention performance.


## 1. Introduction

Spherical tanks currently have a significant function in the oil and gas industries [1]. They serve as a widely used storage option for various gases and fluids, like LPG (liquefied petroleum gas) and LNG (liquefied natural gas), owing to the advantageous characteristics linked to

## Competing interests: The authors have declared

that no competing interests exist.
their form [2, 3]. However, in recent years, as this type of tank has increased in various sectors, several accidents have been involving them, including fires and explosions, resulting in significant human and financial losses [1, 4]. Here are some accidents related to spherical tanks in the past years. In 1984, a spherical LPG tank explosion in Mexico City devastated 270 houses spread across an area measuring 100,000 square meters. Tragically, the accident claimed 500 lives and caused injuries to an additional 4,000 individuals [5-7]. Similarly, at a Texas refinery in 1978, a BLEVE incident led to the rupture and explosion of three spherical tanks, five horizontal tanks, and four vertical tanks, resulting in the loss of at least seven lives [8]. 1966 the Feyzin refinery accident in France caused 18 fatalities and 81 injuries [8, 9]. Furthermore, in Montreal, Canada 1957, a defective level gauge led to a fatality caused by BLEVE spherical tanks [8]. Lastly, the Visakhapatnam refinery incident in India in 1997 resulted in 56 deaths and approximately $\$ 15$ million in damages [10].

These events indicate that despite the low probability of spherical tank accidents, the potential consequences can be significant. Moreover, the absence of a proportional risk assessment framework may contribute to disastrous accidents [2, 11]. As a result, it is crucial to develop a dynamic risk assessment method that can take into account changes in the process and help prevent accidents related to spherical tanks [2, 12]. Dynamic risk assessment adjusts the initial risk rating based on factors such as the reliability of safety systems, maintenance and inspection procedures, human behavior, and operational processes [11, 13].

The development of studies on dynamic risk assessment in process facilities is ongoing. Zarei et al. (2021) employed a BN using the best-worst method (BWM) and D-number theory in the dynamic risk assessment of hydrogen infrastructures, aiming to minimize uncertainty in determining the prior probability of BEs [14]. Using the temporal evolution of escalation vectors with the Dynamic Bayesian Network (DBN) approach was the method used by Zeng et al. to estimate the exact dynamic probabilities of domino effects in chemical industrial areas [15]. Kamil et al. (2019) presented the Stochastic Petri-net model for studying the probability and propagation pattern of domino events to evaluate the dynamic risk associated with domino effects [16]. Luan et al. (2023) analyzed the factors influencing the dynamic risk assessment for road tanker accidents using a fuzzy Bayesian network (FBN) and binary logistic regression model combined with a bow-tie model [17]. In other research, Bhandari et al. (2016) combined a dynamic risk-based strategy with a maintenance-optimizing technique to develop a maintenance plan [18]. Zhou et al. (2023) conducted a risk assessment study of an oil storage tank using the bowtie model. They used expert judgment and fuzzy sets to obtain prior probabilities of basic incidents. They then used new evidence and posterior probabilities of basic incidents to calculate posterior probabilities of storage tank consequences [19]. As a quantitative risk assessment technique to assess safety at each stage of the accident sequence analysis, Rathnayaka et al. introduced SHIPP (System Hazard Identification, Prediction, and Prevention) [20, 21]. This method presents a structured approach to recognize, evaluate, and model accidents during processes, foresee their probability and implement measures to prevent them [22]. By comprehending accidents within intricate systems, this model transcends the constraints of traditional accident models. It estimates the likelihood of accidents happening based on historical accident data and has the ability to adapt the probability of accidents occurring [2]. To connect cause and effect in this model, the fault and event tree are combined, and Bayesian inference is employed to deal with data uncertainty [22].

The usefulness of this technique for modeling accidents has been supported by numerous studies in the process industries. Pouyakian et al. (2021) used the combination of SHIPP and HAZOP techniques to investigate managerial, organizational, human, and process factors to provide a thorough approach based on FBN for modeling and reducing the uncertainty of parameters as well as an accurate analysis of the risk of release of hazardous substances in

Storage tanks with a floating roof [23]. Sarvestani et al. (2021) conducted a study using the MIMAH and SHIPP methods to model the occurrence process of accidents in LPG storage tanks [2]. In another study, the combination of SHIPP with HFACS, FBWM, and FBN methods was offered as a novel model for overcoming the limitations of other studies in the analysis of human and organizational aspects in the occurrence of accidents related to ethylene storage tanks and their consequences [22]. Due to the accident scenario being displayed from causes to consequences, BT is a popular technique in the risk assessment of process systems. This model can help determine and evaluate the root cause of system failure and its potential consequences. It improves FT and ET's capabilities by combining them into a single approach [24, 25]. However, due to the static nature of FTA and ETA in its structure, it is limited in the dynamic risk assessment. Additionally, BT cannot demonstrate conditional reliance. These limitations are overcome by the BN [26]. Moreover, studies have demonstrated the flexible framework of BN in effectively analyzing various accident scenarios for dynamic safety assessment [26--28]. Khakzad et al. (2013) presented an approach that combines the bowtie technique with the Bayesian network framework. They aimed to create a dynamic tool that effectively addresses uncertainties by leveraging the Bayes theorem [26, 29]. BN analysis is favored due to several critical factors compared to traditional techniques like FT and ET. One primary advantage lies in its capacity to simulate intricate systems while diminishing parametric uncertainty by the assimilation of additional evidence. Moreover, its user-friendly and concise graphical approach is highly valued. Furthermore, BN enables probability updating and sequential learning [18, 30].

Zerouali et al. (2019) used FBN to predict the risk of storage tank fire and explosion. They mapped the Bowtie in BN to quantify the probabilities of events [31]. Sun et al. (2022) addressed the challenge of safety assessment in complex, dynamic process systems. They propose a method that combines Catastrophe Theory for quantifying disruption intensity with a Dynamic Bayesian Network (DBN) to model system performance response. This framework offers a resilience metric for evaluating a system's ability to absorb, adapt, and recover from disruptions [28]. Yazdi and Kabir (2018) proposed a methodology for process systems risk assessment to Highlight the limitations of traditional QRA. Their approach integrated Bayesian Networks, Fuzzy Set Theory, and Evidence Theory to address data uncertainty, expert opinion subjectivity, and model limitations [32].

The data quantity and knowledge limitations result in vague and imprecise information used in the suggested frameworks, irrespective of whether BN is utilized. Employing fuzzy logic can resolve this imprecision effectively [33]. It is challenging to use a comprehensive database to cover all systems since the probability of a basic event occurring in various industries is dependent on local conditions. As a result, the primary data inputs for probability estimation are expert judgments. But these opinions frequently contain ambiguity and imprecision. Thus, Zadeh presented a Type-I fuzzy set theory to solve this problem [19, 34].

Several research used FTA with the Fuzzy type-1 set in various industries [35--39]. However, this quantification approach based on experts' opinions cannot show the uncertainties related to the membership functions [37, 40]. Therefore, a type two fuzzy set (T2FS) is developed for more accurate risk quantification [24, 41].

Different individuals assign distinct interpretations to identical words; hence, Zadeh (1975) introduced T2FSs to capture experts' subjective and imprecise judgment in real-world operations [41]. In other words, each element of T2FSs, unlike a T1FS, which presents the degree of membership as a crisp number in [0,1], is an interval in [0, 1] [42]. Three-dimensional T2FS membership functions provide more degrees of freedom for dealing with uncertainties and direct modeling [43].

Mendel and John (2002) put forward the interval type-2 fuzzy set (IT2FS) as a specific form of T2FSs, which has gained popularity due to its simplicity and widespread application [44]. In

some studies, different methods like IT2FTOPSIS, IT2FAHP, IT2FDEMATEL, IT2FVIKOR, IT2FFMEA, and T2FS with D-S evidence theory were used [45-49]. Z-number is a novel idea a more remarkable ability to express human understanding. It has a simple framework with reliability and restrictions that makes it easy to express and manage the confidence of uncertain information [50].

This study proposes a novel approach to address these limitations. It leverages Interval Type-2 Fuzzy Sets (IT2FS) and Z-numbers within a Bayesian Network framework. With the IT2FS combination and the Z-number, this approach provides reliable quantitative values for input for calculations in the Bayesian network and beta distribution, increasing the reliability of predicting process accidents.

IT2FS and Z-numbers (IT2FS-Z) integration within a BN framework has received limited attention in the existing literature. By incorporating Z-numbers, we move beyond traditional fuzzy logic approaches (Level 2) and exact number calculations (Level 1) to a more nuanced representation of uncertainty that is closer to real-world human decision-making (Level 3) [51, 52]. This allows for a more reliable and realistic risk assessment, particularly in scenarios with limited data and subjective expert opinions.

After reviewing previous research, only two studies were found that used the combination of z-number and IT2FS. In one of these studies, Zamri et al. used Z-number, IT2FS, and TOPSIS to deal with decision uncertainty [49]. In another study, Azman et al. improved IT2FVIKOR with Z-numbers to determine the best strategy for water supply security in Malaysia [53]. These researchers attempted to use the IT2FS and Z number (IT2FS-Z) to reduce decision uncertainty. However, no studies using the beta distribution based on the prior probability obtained using IT2FS-Z to calculate the posterior probability of barrier failure and consequences were identified.

In this regard, the present study aims to provide a method to improve the confidence level in dynamic risk assessment by combining IT2FS-Z and beta distribution in the BN platform to reduce the uncertainty in determining the posterior probability of accident occurrence.

# 2. Theoretical background 

### 2.1. Interval type-2 fuzzy sets

The definitions and arithmetic operations of BN, Z-numbers, power average operators, and IT2FS are introduced in this section. It is worth noting that a trapezoidal membership function (TrMF) was employed throughout the study since it can yield results that are more accurate than those produced by triangular MF [54].

Definition 1 [55]. The following is the expression for a T2FS with the membership function $(\mathrm{MF}), \mu_{\hat{A}}(\mathrm{x}, \mu)$, where $\mathrm{x} \in \mathrm{X}$ :

$$
\hat{A}=\left\{\left((x, u), \mu_{\hat{A}}(x, u)\right) \mid \forall x \in X, \forall_{u} \in J_{u} \subseteq[0,1]\right\}
$$

where $J_{u}$ denotes an interval in $[0,1]$ and $0 \leq \mu_{\hat{A}}(x, u) \leq 1$. Moreover, $\hat{A}$ can also be represented as the
following form:

$$
\hat{A}=\int_{x \in X} \int_{\mu \in J_{u}} \mu_{\hat{A}}(x, u) / \cdot x, u), J_{u} \subseteq[0,1]
$$

where $\iint$ indicates the union of all valid x and u . The primary and secondary variables of $\hat{A}$ are x and u , respectively.

![img-0.jpeg](img-0.jpeg)

Fig 1. The membership functions of the IT2FSs.
https://doi.org/10.1371/journal.pone.0307883.g001

Definition 2. Interval type-2 fuzzy sets (IT2FS), a particular instance of T2FS, are what set $\hat{\tilde{A}}$ is known as when all $\mu_{\tilde{A}}(x, u)=1$. IT2FS $\hat{\tilde{A}}$ can be expressed as follows using Eq (2):

$$
\hat{\tilde{A}}=\int_{x \in X} \int_{u \in I_{x}}{ }^{1} / 2 x, u
$$

Definition 3. An IT2FS has two membership functions, the top and lower of which are type-1 membership functions. A trapezoidal IT2FS $\hat{\tilde{A}}$ as provided in Eq 4 is depicted in Fig 1 [56].

$$
\hat{\tilde{A}}=\left[\tilde{A}^{U}, \tilde{A}^{L}\right]=\left[\left(a_{1}^{U}, a_{2}^{U}, a_{3}^{U}, a_{4}^{U} ; h_{A}^{U}\right),\left(a_{1}^{L}, a_{2}^{L}, a_{3}^{L}, a_{4}^{L} ; h_{A}^{L}\right)\right]
$$

Where $a_{1}^{U}, a_{2}^{U}, a_{3}^{U}, a_{4}^{U}$ and $a_{1}^{L}, a_{2}^{L}, a_{3}^{L}, a_{4}^{L}$ represent the reference points of the IT2FS $\hat{\tilde{A}}$ in which $\tilde{A}^{U}$ and $\tilde{A}^{L}$ are the T1FS, with $a_{1}^{U} \leq a_{2}^{U} \leq a_{3}^{U} \leq a_{4}^{U}, a_{1}^{L} \leq a_{2}^{L} \leq a_{3}^{L} \leq a_{4}^{L}, a_{1}^{U} \leq a_{1}^{L}$ and $a_{4}^{L} \leq a_{4}^{U}$. Where the heights of the lower membership function $\left(h_{A}^{L}\right)$ and the upper membership function $\left(h_{A}^{U}\right)$ of IT2FS, $\hat{\tilde{A}}$, respectively, are shown in Fig 1.

Definition 4. Let there be two IT2FS, $\hat{\tilde{A}}_{1}=\left[\left(a_{11}^{U}, a_{12}^{U}, a_{13}^{U}, a_{14}^{U} ; h_{1 A}^{U}\right),\left(a_{11}^{L}, a_{12}^{L}, a_{13}^{L}, a_{14}^{L} ; h_{1 A}^{L}\right)\right]$ and $\hat{\tilde{A}}_{2}=\left[\left(a_{21}^{U}, a_{22}^{U}, a_{23}^{U}, a_{24}^{U} ; h_{2 A}^{U}\right),\left(a_{21}^{L}, a_{22}^{L}, a_{23}^{L}, a_{24}^{L} ; h_{2 A}^{L}\right)\right]$. Then, the following describes how to perform calculations between trapezoidal IT2FS.

Addition operation:

$$
\tilde{\hat{A}}_{1} \oplus \tilde{\hat{A}}_{2}=\left[\begin{array}{l}
\left(a_{11}^{U}+a_{21}^{U}, a_{12}^{U}+a_{22}^{U}, a_{13}^{U}+a_{23}^{U}, a_{14}^{U}+a_{24}^{U} ; \min \left\{h_{1 A}^{U}, h_{2 A}^{U}\right\}\right) \\
\left(a_{11}^{L}+a_{21}^{L}, a_{12}^{L}+a_{22}^{L}, a_{13}^{L}+a_{23}^{L}, a_{14}^{L}+a_{24}^{L} ; \min \left\{h_{1 A}^{L}, h_{2 A}^{L}\right\}\right)
\end{array}\right]
$$

Subtraction operation:

$$
\tilde{\hat{A}}_{1} \ominus \tilde{\hat{A}}_{2}=\left[\begin{array}{l}
\left(a_{11}^{U}-a_{21}^{U}, a_{12}^{U}-a_{22}^{U}, a_{13}^{U}-a_{23}^{U}, a_{14}^{U}-a_{24}^{U} ; \min \left\{h_{1 A}^{U}, h_{2 A}^{U}\right\}\right) \\
\left(a_{11}^{L}-a_{21}^{L}, a_{12}^{L}-a_{22}^{L}, a_{13}^{L}+a_{23}^{L}, a_{14}^{L}-a_{24}^{L} ; \min \left\{h_{1 A}^{L}, h_{2 A}^{L}\right\}\right)
\end{array}\right]
$$

Multiplication operation:

$$
\tilde{\hat{A}}_{1} \otimes \tilde{\hat{A}}_{2}=\left[\begin{array}{l}
\left(a_{11}^{U} \times a_{21}^{U}, a_{12}^{U} \times a_{22}^{U}, a_{13}^{U} \times a_{23}^{U}, a_{14}^{U} \times a_{24}^{U} ; \min \left\{h_{1 A}^{U}, h_{2 A}^{U}\right\}\right) \\
\left(a_{11}^{L} \times a_{21}^{L}, a_{12}^{L} \times a_{22}^{L}, a_{13}^{L} \times a_{23}^{L}, a_{14}^{L} \times a_{24}^{L} ; \min \left\{h_{1 A}^{L}, h_{2 A}^{L}\right\}\right)
\end{array}\right]
$$

Multiplication with a scalar $\mathrm{k}>0$ :

$$
k \cdot \tilde{\hat{A}}_{1}=\left[\begin{array}{l}
\left(k \times a_{11}^{U}, k \times a_{12}^{U}, k \times a_{13}^{U}, k \times a_{14}^{U} ; h_{1 A}^{U}\right) \\
\left(k \times a_{11}^{L}, k \times a_{12}^{L}, k \times a_{13}^{L}, k \times a_{14}^{L} ; h_{1 A}^{L}\right)
\end{array}\right]
$$

Power operation:

$$
\left(\tilde{\hat{A}}_{1}\right)^{x}=\left[\begin{array}{l}
\left(a_{11}^{U}\right)^{x},\left(a_{12}^{U}\right)^{x},\left(a_{13}^{U}\right)^{x},\left(a_{14}^{U}\right)^{x} ; h_{1 A}^{U} \\
\left(\left(a_{11}^{L}\right)^{x},\left(a_{12}^{L}\right)^{x},\left(a_{13}^{L}\right)^{x},\left(a_{14}^{L}\right)^{x} ; h_{1 A}^{L}\right)
\end{array}\right]
$$

d is distance between $\tilde{\hat{A}}_{1}$ and $\tilde{\hat{A}}_{2}$ as following [57]:

$$
d\left(\tilde{\hat{A}}_{1}, \tilde{\hat{A}}_{2}\right)=\left|R_{d}\left(\tilde{\hat{A}}_{1}, \tilde{\hat{1}}\right)-R_{d}\left(\tilde{\hat{A}}_{2}, \tilde{\hat{1}}\right)\right|
$$

where $\tilde{\hat{1}}=[(1,1,1,1 ; 1),(1,1,1,1 ; 1)]$, and

$$
\begin{aligned}
R_{d}\left(\tilde{\hat{A}}_{1}, \tilde{\hat{1}}\right)= & \frac{1}{2 \cdot h_{1 A}^{U} \cdot h_{1 A}^{L}}\left[h_{1 A}^{U} \cdot\left(a_{14}^{L}-a_{13}^{L}-a_{14}^{U}+a_{13}^{U}\right)\right]-\frac{1}{2 \cdot h_{1 A}^{U} \cdot h_{1 A}^{L}}\left[h_{1 A}^{L} \cdot\left(0.5\left(\left(a_{12}^{U}-a_{11}^{U}-a_{12}^{L}\right.\right.\right.\right. \\
& \left.\left.\left.\left.+a_{11}^{L}\right)-\left(a_{14}^{U}-a_{13}^{U}-a_{12}^{U}+a_{11}^{U}\right)\right)\right]+1-a_{14}^{U}-0.5\left(a_{11}^{U}-a_{11}^{L}+a_{14}^{L}-a_{14}^{U}\right)
\end{aligned}
$$

# 2.2. The power average operator 

The Power Average (PA) operator is widely recognized as an effective method for combining individual preferences to derive group preference values that accurately represent the correlation between risk assessments. It is described as follows.

Definition 6. The PA operator, with a dimension of n , is a mapping (PA) that takes Rn to R. This can be represented by Eq 12 [58].

$$
P A\left(a_{1} a_{2}, \ldots, a_{n}\right)=\frac{\sum_{i=1}^{n}\left(1+T\left(a_{i}\right)\right) a_{i}}{\sum_{i=1}^{n}\left(1+T\left(a_{i}\right)\right)}
$$

Where

$$
T\left(a_{i}\right)=\sum_{j=1, j \neq i}^{n} \sup \left(a_{i}, a_{j}\right), i \in N
$$

The following are the characteristics of the $\sup \left(a_{i}, a_{j}\right)$, which expresses the degree that $a_{j}$ supports the $a_{i}$ :

1. $\sup \left(a_{i}, a_{j}\right) \in[0,1]$
2. $\sup \left(a_{i}, a_{j}\right)=\sup \left(a_{j}, a_{i}\right)$

Table 1. Linguistic terms and their corresponding IT2FSs [51].


https://doi.org/10.1371/journal.pone.0307883.t001
3. $\sup \left(a_{i}, a_{j}\right) \geq \operatorname{Sup} \pi(\mathrm{x}, \mathrm{y})$, if $\mathrm{d}\left(a_{i}, a_{j}\right)<\mathrm{d}(\mathrm{x}, \mathrm{y})$

The closer two values are to one another under condition three above, the more they support one another. According to Son et al. [59], the support measure (Sup) is a similarity measure. Consequently, the equation provided below can be utilized to earn $a_{j}$ 's support for $a_{i}$ :

$$
\sup \left(a_{i}, a_{j}\right)=1-\mathrm{d}\left(a_{i}, a_{j}\right)
$$

# 2.3. Z-number 

Definition 5. Z-number denoted as $\mathrm{Z}=(\hat{\vec{A}}, \hat{\vec{B}})$, comprises two components. A restriction on the values is mentioned for the first component, $\hat{\vec{A}}$. The second component, $\hat{\vec{B}}$, provides a measure of the first component's reliability. Generally, $\hat{\vec{A}}$ and $\hat{\vec{B}}$ are subjective and can be conveyed using natural language $[60,61]$.

For example, if the expert's opinion about an event is "Medium High" and her level of confidence is "Relatively sure," it can be written as a Z-number as follows: $Z=$ (Medium High, relatively sure). According to Table 1, this state will be quantitatively $\mathrm{Z}=[((0.5,0.7,0.7,0.9 ; 1)$, $(0.6,0.7,0.7,0.8 ; 0.9)),((0.1,0.3,0.4,0.6 ; 1),(0.2,0.3,0.4,0.5 ; 0.9))] . \hat{\vec{A}}$ and $\hat{\vec{B}}$ are assumed as trapezoidal fuzzy numbers, as defined in Fig 2. The mathematical definition of $\hat{\vec{A}}$ and $\hat{\vec{B}}$ is similar to Eq 1. $\hat{\vec{B}}$ can be converted into a crisp value by means of Eq 15 as follows [43, 51].

$$
\alpha=\frac{\int_{x \in X} \int_{\mu \in I_{x}} \mu_{\hat{\vec{B}}}(x, u) /(x, u) x d x}{\int_{x \in X} \int_{\mu \in I_{x}} \mu_{\hat{\vec{B}}}(x, u) /(x, u) d x}
$$

Where $\alpha$ stands for the weight of the second portion $\hat{\vec{B}}$ and $\mu_{\hat{\vec{B}}}(x, u)$ for the degree to which $x$ $\in X$ is dependent on $\hat{\vec{B}}$. Then, $\alpha$ can be added to the initial element $\hat{\vec{A}}$ using Eq 16. (51).

$$
\hat{\vec{z}}^{x}=\left\{\left(x, \mu_{\hat{\vec{B}}}, \quad\right) \mid \mu_{\hat{\vec{B}}},(x, u)=\alpha \mu_{\hat{\vec{B}}},(x, u), x \in(0,1)\right\}
$$

![img-1.jpeg](img-1.jpeg)

Fig 2. Interval type 2 trapezoid fuzzy membership functions. (a: related to opinion b: related to confidence).
https://doi.org/10.1371/journal.pone.0307883.g002

where $\mu_{\hat{R}}$, is a representation of the degree to which $x \in X$ is dependent on $\hat{\tilde{B}}$. Consequently, it was possible to acquire the rules for converting Z-number linguistic variables to IT2F by combining the linguistic variables.

In the final step, it is suggested that the asymmetrical IT2F number (based on experts' weighted views) be converted to the symmetrical IT2F number Eq 17 [62].

$$
\hat{\tilde{z}}^{\prime}=\left\{\left(x, \mu_{\hat{\tilde{z}}^{\prime}}\right) \mid \mu_{\hat{\tilde{z}}^{\prime}}(x, u)=\mu_{\hat{\tilde{A}}}\left(\frac{x}{\sqrt{\alpha}}\right), x \in[0,1]\right\}
$$

Where $\mu_{\hat{z}^{\prime}}(x)$ can be defined as fallow:

$$
\mu_{\hat{z}^{\prime}}(x, u)=\mu_{\hat{A}}\left(\frac{x}{\sqrt{\alpha}}\right), \quad x \in \sqrt{\alpha} X
$$

# 2.4. Bayesian network 

Definition 7. Conditional Probability Tables (CPTs) are employed in the BN model to determine the probability of BEs. Using these tables, the probability of an intermediate node can be calculated based on its conditional dependencies with related root nodes.

The common probability distribution of a collection of variables is determined in BN using Eq 18 .

$$
P(U)=\prod_{i=1}^{c} p\left(A_{i} \mid P a\left(A_{i}\right)\right)
$$

Where $\mathrm{Pa}(\mathrm{Ai})$ denotes the parent set of Ai in the BN , and $\mathrm{P}(\mathrm{U})$ refers to the BN's characteristics [63].

When new information ( E evidence) is considered, BN updates the prior probability of occurrences using Bayes' theorem to obtain the posterior probability. This new observation typically becomes accessible throughout the operational lifetime of a process, including the occurrence or nonoccurrence of primary events or accidents:

$$
P(U \mid E)=\frac{P(U, E)}{P(E)}=\frac{P(U, E)}{\sum_{U} P(U, E)}
$$

### 2.5. Beta distribution

Definition 8. The discrete value of the BE failure probabilities (FPs) can be explained by the mean $(\mu)$ of the distribution, where $\alpha$ and $\beta$ are the factors defined as the success and failure of equipment in response to demand in the beta distribution. This means that the discrete value of the FPs can be expressed as a continuous value.

$$
F P=\mu=\frac{\alpha}{\alpha+\beta}
$$

Suppose the only information available regarding the reliability or likelihood of BEs is the discrete value of the FP. In that case, the degree of certainty $(\mathrm{FP}=\mu)$, which measures how spread out the distribution is around it, needs to be determined by the variance (VAR) of the distribution:

$$
\mathrm{VAR}=\frac{\alpha \cdot \beta}{(\alpha+\beta)^{2} \cdot(\alpha+\beta+1)}
$$

When there is a higher variance in the data, it becomes less reliable and more sensitive to changes in the following data.

By obtaining FP values of BEs based on experts' opinions and the amount of variance from previous studies [64], it is possible to calculate the initial value of $\alpha$ and $\beta$ in year zero, represented by $\alpha_{0}$ and $\beta_{0}$.

$$
\begin{gathered}
\beta_{0}=\left(\frac{F P \cdot(1-F P)-V A R}{V A R}\right) \cdot(1-F P) \\
\alpha_{0}=\frac{F P \times \beta_{0}}{(1-F P)}
\end{gathered}
$$

Where VAR was considered $10^{-4}$ and $10^{-5}$ so that scores could be compared. The posterior beta distribution represents the updated FP of each BEs (Eq 25).

$$
\begin{aligned}
F P_{1} & =\frac{\alpha_{1}}{\alpha_{1}+\beta_{1}} \\
\alpha_{1} & =\alpha_{0}+\mathrm{F} \\
\beta_{1} & =\beta_{0}+S
\end{aligned}
$$

Where F and S are the numbers of failures and successes of BEs during the expected lifetime of the system, respectively. The indices for the prior and posterior distributions are given by the numbers 0 and 1 , respectively.

# 3. Proposed methodology for assessing dynamic risks 

In this section, the steps of implementing the research method are explained. Fig 3 illustrates the step-by-step process of the proposed methodology.
![img-2.jpeg](img-2.jpeg)

Fig 3. Work flow diagram of proposed method.
https://doi.org/10.1371/journal.pone.0307883.g003

![img-3.jpeg](img-3.jpeg)

Fig 4. The link between barriers and how they affect the consequences based on the SHIPP theory.
https://doi.org/10.1371/journal.pone.0307883.g004

# 3.1. Hazards identification 

3.1.1. Combining the bow-tie with the SHIPP approach. In stage one, the Bes impacting the top event were identified, and a fault tree was also formed for the obstacles. Then, the bowtie diagram was created using the SHIPP approach. The SHIPP approach follows a specific order and hierarchy of event consequences, which closely resemble the structural development of an event tree. The consequences are Respectively as follows. Near miss, mishap, incident, accident. In reality, the occurrence of an end event can potentially escalate in any sequence. For instance, a near miss could potentially turn into an accident (Fig 4) [65].

Safety barrier has been categorized in the SHIPP approach for accident prevention techniques after release factor; 1. Release Prevention Barrier (RPB), 2. Dispersion Prevention Barrier (DPB), 3. Ignition Prevention Barrier (IPB), 4. Escalation Prevention Barrier (EPB), 5. Human Factor Barrier (HFB), 6. Management and Organizational Barrier (MOB) [20].

The bow-tie diagram, which can be observed conceptually in Fig 4, was drawn based on this approach and considering the series of consequences, including near miss, mishap, incident, and accident. Fig 4 illustrates the improved predictive accuracy of presented model, clearly showing how it outperforms existing models during the simulated accident scenarios.

### 3.2. Aggregating stage

3.2.1. Weight of expert judgment. Twenty experts' opinions and confidence levels on the prior probability of BEs were obtained. Their linguistic terms were then quantified and combined using IT2FS and Z-number. It is important to note that the experts' involvement was solely intended to assist the researchers in gaining a comprehensive understanding of the industrial process under investigation and to estimate the probability of BE occurrences and obstacle failure probabilities. Written informed consent was obtained from all twenty participating industry specialists before their involvement in the study, conducted between January $15^{\text {th }}$ and April $23^{\text {rd }}, 2023$. Ethical approval was obtained from the ethics committee of Hamadan University of Medical Sciences. Details of Ethical approval are available in the Acknowledgments section.

It is remarkable that when integrating the views of many experts, it is important to consider the weight of the experts in order to make the evaluation results more scientific and objective. The Linguistic terms given by them were employed for the probability of BEs occurrence and corresponding confidence level, which fall into ("VL", "L", "ML", "M", "MH", "H", "VH") and

Table 2. Weighting scores of various experts [66].


https://doi.org/10.1371/journal.pone.0307883.t002
("NS", "QS", "S", "VS"), respectively (Table 1). Table 2, presents data on the age(A), education level (EL), job title (JT), and related experience (RE) of each expert.

A score is assigned to each expert based on this information. Using the experts' weight scores and weight factors, Eqs (28) and (29) calculate this score (Table 3).

$$
\begin{aligned}
& \text { The weight score of } j^{\text {th }} \text { Expert } \\
& \quad=\text { Score of } \mathrm{A}_{j}+\text { Score of } \mathrm{JT}_{j}+\text { Score of } \mathrm{EL}_{j}+\text { Score of } \mathrm{RE}_{j}
\end{aligned}
$$

$$
W_{j}=\frac{\text { The weight score of } j^{\text {th }} \text { Expert }}{\sum_{j=1}^{n} \text { The weight score of Experts }}
$$

3.2.2. Expert opinion aggregation using the power average operator. Although widely used data aggregation methods like average, median, and mode, they sometimes fail to convey the complexity via the aggregated statistic. Considering the links between the variables being combined would help to make these integrating mechanisms intelligent [58].

Due to the experts' varying experiences, knowledge, and preferences, the assessment information provided by the experts may vary throughout the entire assessment procedure. As a result, in this research, a group decision matrix was created using an aggregation method to take into consideration of individual assessment data. By applying the power average operator (PA) in the aggregation process in risk assessment, lower weight is given to bigger or smaller evaluation values. Therefore, the opinions of the group's experts become closer and create more reliable results. Therefore, the issue of combining expert views is solved using the PA-IT2FS-Z operator which is based on the PA operator theory [67].

Table 3. Calculation weighting factors for 20 experts.


https://doi.org/10.1371/journal.pone.0307883.t003 The fuzzy aggregate outcome of the expert views is represented by $\mathrm{R}*{\mathrm{i}}(\mathrm{i}=1,2,3, \ldots, \mathrm{n})$ as follows:

$$ \begin{aligned} R_{i} & =P A-I T 2 F S-Z\left(\hat{A}*{1}, \hat{A}*{2}, \ldots, \hat{A}*{m}\right) \ & =\left(\begin{array}{l} \left(\frac{\sum_{j=1}^{m} \omega_{j}\left(1+T\left(\hat{A}*{j}\right)\right) a*{j 1}^{U}}{\sum_{j=1}^{m} \omega_{j}\left(1+T\left(\hat{A}*{j}\right)\right) a*{j 2}^{U}} \cdot \frac{\sum_{j=1}^{m} \omega_{j}\left(1+T\left(\hat{A}*{j}\right)\right) a*{j 3}^{U}}{\sum_{j=1} \omega_{j}\left(1+T\left(\hat{A}*{j}\right)\right) a*{j 1}^{U}} \cdot \frac{\sum_{j=1}^{m} \omega_{j}\left(1+T\left(\hat{A}*{j}\right)\right) a*{j 1}^{U}}{\sum_{j=1} \omega_{j}\left(1+T\left(\hat{A}*{j}\right)\right)} \cdot \sum_{j=1}^{m} \omega_{j}\left(1+T\left(\hat{A}*{j}\right)\right) \cdot \min *{j=1,2, \ldots m} h*{j 4}^{U} \cdot \left(\frac{\sum_{j=1}^{m} \omega_{j}\left(1+T\left(\hat{A}*{j}\right)\right) a*{j 1}^{L}}{\sum_{j=1} \omega_{j}\left(1+T\left(\hat{A}*{j}\right)\right) a*{j 2}^{L}} \cdot \frac{\sum_{j=1}^{m} \omega_{j}\left(1+T\left(\hat{A}*{j}\right)\right) a*{j 3}^{L}}{\sum_{j=1} \omega_{j}\left(1+T\left(\hat{A}*{j}\right)\right)} \cdot \sum_{j=1} \omega*{j}\left(1+T\left(\hat{A}*{j}\right)\right) a*{j 1}^{L} \cdot \sum_{j=1} \omega_{j}\left(1+T\left(\hat{A}*{j}\right)\right) a*{j 2}^{L} \sum_{j=1} \omega*{j}\left(1+T\left(\hat{A}*{j}\right)\right) \cdot \min *{j=1,2, \ldots m} h*{j 4}^{L} \right) \end{aligned} $$

Where $\omega_{j}$ stands for the expert $\mathrm{E}*{j}$ 's weight.

# 3.3. The integration of IT2F and Z-number

The method developed by Kahraman et al. is used in this research for defuzzification since it takes fewer calculations than other methods [56].

Let IT2FS-Z

$$ \mathrm{Z}=(\hat{\vec{A}}, \hat{\vec{B}})=\left[\left(a_{1}^{U}, a_{2}^{U}, a_{3}^{U}, a_{4}^{U} ; h_{A}^{U}\right),\left(a_{1}^{L}, a_{2}^{L}, a_{3}^{L}, a_{4}^{L} ; h_{A}^{L}\right),\left(b_{1}^{U}, b_{2}^{U}, b_{3}^{U}, b_{4}^{U} ; h_{b}^{U}\right),\left(b_{1}^{L}, b_{2}^{L}, b_{3}^{L}, b_{4}^{L} ; h_{b}^{L}\right)\right] $$

then defuzzification can be calculated as:

$$ F P S_{B}=\frac{\left[\left(b_{1}^{U}-b_{1}^{U}\right)+\left(b_{2}^{U}+b_{2}^{U}-b_{1}^{U}\right)+\left(b_{3}^{U}+b_{3}^{U}-b_{1}^{U}\right)\right.}{4}+b_{1}^{U}\right]+\left[\frac{\left(b_{2}^{L}-b_{2}^{L}\right)+\left(b_{3}^{L}+b_{3}^{L}-b_{2}^{L}\right)+\left(b_{3}^{L}+b_{3}^{L}-b_{1}^{L}\right)}{4}+b_{1}^{L}\right]}{2} $$

Then $F P S_{B}$ is multiplied in part A according to Eq 8 and definition 18:

$$
\begin{aligned}
\tilde{\tilde{z}}^{x}= & \left(\tilde{\tilde{A}}, \sqrt{F P S_{b}}\right) \rightarrow \tilde{\tilde{z}}^{\prime}=\left(\sqrt{F P S_{b}} \times \tilde{\tilde{A}}\right) E q . 8 q .8 \quad \tilde{\tilde{z}}^{\prime} \\
= & \left(\left(\sqrt{F P S_{b}} \times a_{1}^{U}, \sqrt{F P S_{b}} \times a_{2}^{U}, \sqrt{F P S_{b}} \times a_{3}^{U}, \sqrt{F P S_{b}} \times a_{4}^{U} ; h_{A}^{U}\right),\left(\sqrt{F P S_{b}} \times a_{1}^{L}, \sqrt{F P S_{b}}\right.\right. \\
& \left.\left.\times a_{2}^{L}, \sqrt{F P S_{b}} \times a_{3}^{L}, \sqrt{F P S_{b}} \times a_{4}^{L} ; h_{A}^{L}\right)\right)
\end{aligned}
$$

Like Eq 31, the first part of the Z-number was also defuzzified and the FPS value for part A $\left(F P S_{A}\right)$ obtained. A simple example is provided considering four experts in S1 Appendix to clarify the above explanations.

# 3.4. Converting FPS into FFP 

The expert-rated fuzzy probability score (FPS) must be converted to calculate the fuzzy failure probability (FFP). The conventional conversion method [68] is:

$$
\begin{gathered}
F F P=\left\{\begin{array}{cc}
\frac{1}{10^{K}} & F P S \neq 0 \\
0 & F P S=0
\end{array}\right. \\
K=\left[\frac{1-F P S}{F P S}\right]^{1 / 3} \times 2.301
\end{gathered}
$$

The Onisawa method only holds in some circumstances. In this study, a more effective calculation method is proposed (Eq 35), along with the conversion of FPS to FFP by DNV standards.

$$
K=\left\{\begin{array}{c}
-0.721 \ln F P S+2.839,0 \leq F P S \leq 0.2 \\
4.523-3.287 F P S, 0.2 \leq F P S \leq 0.8 \\
{[(1-F P S) / F P S]^{0.445} \times 3.705,0.8 \leq F P S \leq 1}
\end{array}\right.
$$

### 3.5. Mapping bow-tie in BN

The probability of the BEs derived using the IT2FS-Z technique were taken into account as the probabilities of root nodes occurrences in order to quantify the model. The bow-tie model was mapped in BN using a technique developed by Khakzad et al. Because BN is used as a dynamic tool for updating the probability of barriers and consequences in the next steps [26]. Each construction step meticulously addresses uncertainty to enhance the robustness and reliability of the Bayesian network. This is achieved through rigorous data validation procedures, ensuring the transparency and traceability of information at every stage. Each network layer demonstrably contributes to its overall predictive accuracy by reducing uncertainty and maintaining transparency. GeNIe 3.0 academic software was used to create and assess the Bayesian model. The BEs, intermediate, and top events in the BT are the BN model's root, middle, and top nodes, respectively.

### 3.6. Sensitivity analysis in BN (CBEs identification)

The primary objective of the sensitivity analysis in this study is to pinpoint the critical basic events (CBEs) within the bow-tie model. CBEs represent the basic events (BEs) that most influence triggering the top event (TE) in the bow-tie model. Identifying CBEs is crucial for

prioritizing risk mitigation strategies by honing in on the most impactful factors. The sensitivity analysis leverages a Bayesian network (BN) framework to evaluate the individual BEs' impact on the TE.

To uncover sensitive nodes (CBEs), the sensitivity analysis employs the best and worst-case scenarios for each node in the BN as input. By applying these scenarios to specific BEs, the evidence (success/failure) for each BE is updated within the BN, considering the established prior probabilities and interrelations with other BEs in the network.

During the sensitivity analysis, all nodes except the BE under scrutiny remain unchanged, enabling a focused assessment of each BE's influence on the TE's probability. By monitoring the TE's probability fluctuations following the evidence updates for each BE, we can identify the BEs causing the most significant changes. These identified BEs are designated as the critical basic events (CBEs). The sensitivity analysis yields valuable insights into the relative importance of BEs in shaping the overall risk profile of the system depicted by the bow-tie model.

# 3.7. Probability adapting 

One of the most significant and beneficial uses of Bayesian networks is sequence learning, which can also be thought of as probability adaptation [69]. Due to this feature, the posterior probability of consequences was calculated taking into account the posterior probability of CBEs and their occurrences over the past five years.

The prior probability of the BEs in the bow-tie diagram, including the fault tree and the event tree, is known. These prior probabilities are assumed to follow the beta distribution and were obtained based on the technical knowledge of experts. Then, five years of data, including incidents, near misses, and accident reports, were analyzed to determine the frequency of success and failure of the primary safety barrier (BEs). According to this information, the posterior probability of CBEs is calculated using Eq 25. This application updates probabilities based on new data received over time.

The updated probability of the CBEs enters the Bayesian network and replaces the prior probability of these events. Following this stage, the probability of failure of barriers (RPB, DPB, IPB, EPB, HFB, M\&OB) and the probability of consequences, including near miss, mishap, incident, and accident, are updated.

This operation was calculated in IT2FS and IT2FS-Z modes and with different variances $\left(10^{-4}\right.$ and $\left.10^{-5}\right)$ to enable comparison of the results.

## 4. A case study of gas release from spherical tank

The method explained in Section 3 is utilized to conduct a dynamic risk evaluation of a spherical tank. This study was conducted in a refinery located in the northwest region of Iran in 2023. The refinery consists of four spherical tanks, each with $2,337 \mathrm{~m}^{3}$ of raw materials for producing LPG, and one spherical tank with $635 \mathrm{~m}^{3}$ of LPG.

### 4.1. Bow-tie

Gas release from the spherical tank is considered a Top Event (TE) to draw the fault tree. Intermediate events (IE)and basic events (BE) that caused the gas release are illustrated as a part of a fault tree in Fig 5. Table 4 contains descriptions of the 70 basic events that were identified.

In the next step, near miss, mishap, incident, and accident were considered consequences of gas release. According to the SHIPP concept (Fig 4), a fault tree was created to assess the failure probability of each barrier. The release prevention barrier (RPB) fault tree comprises 42 BEs (symbolized as R), the extended dispersion prevention barrier (DPB) fault tree comprises 16 BEs (symbolized as D), the ignition prevention barrier (IPB) fault tree encompasses 20 BEs

![img-4.jpeg](img-4.jpeg)

Fig 5. Fault tree of gas release in spherical tank.
https://doi.org/10.1371/journal.pone.0307883.g005
(symbolized as IP), the escalation prevention barrier (EPB) fault tree contains 26 BEs (symbolized as E). Additionally, there are 22 BEs associated with the human factor barrier (HFB) fault tree (symbolized as H), and the fault tree for management and organization barrier (M\&OB) incorporates 13 BEs (symbolized as M), as illustrated in Figs 6 to 10. Detailed descriptions of these basic events are provided in Table 5.

The IT2FS-Z and IT2FS methods were utilized to acquire the prior likelihood of BEs. The FFP, K, and FPS values obtained for the fault tree's BEs associated with the TE are displayed in Tables 6 and 7, respectively. Additionally, Tables 8 and 9 show the prior probability of the BEs linked to the failure of RPB, DPB, IPB, and EPB barriers.

These results are compared in Fig 11. The BEs prior probabilities in Fig 11 shows a significant difference in the results when combining opinion and confidence using the Z-number. The results obtained from IT2FS-Z are notably lower than those from IT2FS, consistent with Kang et al.'s study (2016) and Aghaei et al.'s (2021) [50, 61].

Tables 8 and 9 show the prior probability of the BEs linked to the failure of RPB, DPB, IPB, and EPB barriers. The results of these tables were compared in Fig 12, which, like Fig 11, also shows the impact of using a z-number.

Table 4. The basic events of fault tree and their symbols.


https://doi.org/10.1371/journal.pone.0307883.t004

# 4.2. SHIPP concept 

The SHIPP concept was applied in this study to ensure that obstacles and outcomes were logically connected to one another. Based on this approach, the barriers (RPB, DPB, IPB, EPB) that impact the probability of the consequences were identified on the bow-tie model's event tree. In order to assess the failure probability of these barriers with a high level of confidence, a fault tree was created for each of these barriers (Figs 6-10 were mapped according to Fig 13 in the Bayesian network.) based on the Fuzzy probability of BEs.

One of the subtle and vital points in the SHIPP method is the relationship between HFB and M\&OB with other obstacles and how they affect the results. Especially in BN, deciding whether HFB and M\&OB, as a parent, are linked to other barriers and have an indirect effect

![img-5.jpeg](img-5.jpeg)

Fig 6. Fault tree of release prevention barrier (RPB) failure.
https://doi.org/10.1371/journal.pone.0307883.g006
on consequences or are directly linked to consequences can lead to different final values of the probability of consequences. It is also effective in detecting sensitive events to determine the posterior probability of barrier failure and consequences. So, based on the conceptual of SHIPP in the study by Samith Rathnayaka et al., who first used this method, HFB and M\&OB in SHIPP have less of an effect on the outcomes than technical obstacles (RPB, DPB, IPB, EPB) [20]. Therefore, the impact of HFB and M\&OB on outcomes was considered indirectly. For this purpose, HFB and M\&OB were considered as parents and technical barriers as children in
![img-6.jpeg](img-6.jpeg)

Fig 7. Fault tree of dispersion prevention barrier (DPB) failure.
https://doi.org/10.1371/journal.pone.0307883.g007

![img-7.jpeg](img-7.jpeg)

Fig 8. Fault tree of ignition prevention barrier (IPB) failure.
https://doi.org/10.1371/journal.pone.0307883.g008
the BN. In the following, the technical barriers in the role of the parent were considered for the consequences, which can be observed in and the BN view in Fig 13.

# 4.3. Experts' opinions 

This study employed the opinions of twenty experts from the studied refinery. Experts expressed their opinions and confidence level according to the Linguistic terms in Table 1. These terms were quantified using the IT2FS (Eq 31) and combined using the Z-number (Eq 32) to reduce the uncertainty of the opinions.

### 4.4. Bayesian network

This section illustrates the bow-tie diagram of the spherical tank gas release shown in Fig 13, where part 'a' represents the fault tree and part 'b' is the event tree. In part b, the consequences
![img-8.jpeg](img-8.jpeg)

Fig 9. Fault tree of escalation prevention barrier (EPB) failure.
https://doi.org/10.1371/journal.pone.0307883.g009

![img-9.jpeg](img-9.jpeg)

**Fig 10. Fault tree of human factor barrier (HFB) failure and management & organizational barrier (M&OB) failure.**

<https://doi.org/10.1371/journal.pone.0307883.g010>

and barriers are marked in yellow and blue, respectively. Also, in Fig 13, it is clear that each barrier has its fault tree.

Considering the prior probability of the BEs, the prior probability of barriers' failure and consequences (Table 10) was calculated based on the Bayesian network conditional tables. The comparison of the prior probability of barrier failure in Fig 14 shows that the highest probability of failure is associated with the RPB, with 1.596 × 10<sup>−2</sup> and 5.754 × 10<sup>−2</sup> in IT2FS-Z and IT2FS, respectively. The highest probability for consequences is near miss, with probabilities of 5.764 × 10<sup>−4</sup> in IT2FS-Z method and 5.784 × 10<sup>−3</sup> in IT2FS. This Figure shows a decreasing trend in the probability of barriers' and consequences in the subsequent layer, consistent with the study by Sarvestani et al. [2]. This can be due to the layer effect in the barriers. This means that by passing through each layer, the number of the next layer is reduced, and this lack of obstacles in each layer reduces the probability of their failure.

Fig 14 demonstrates the significant impact of employing Z-number to combine expert opinions with their confidence levels. Fig 14B shows that the trend of the plots obtained by the IT2FS-Z and IT2FS methods are indistinguishable for the other consequences, as the initial consequence (near miss) has a significantly higher prior probability than the subsequent consequences. Table 10 presents a more precise distinction between IT2FS-Z and IT2FS conditions.

### 4.4.1. Sensitivity analysis in BN and identification of CBEs

The explosion node was selected as the target node to determine the most critical BEs affecting the final consequence, and BN was used to do a sensitivity analysis. Then, fifteen events with the highest sensitivity were selected in the BN based on IT2FS-Z and IT2FS, depicted in Fig 15A and 15B, respectively. The probability values computed for the CBEs by the IT2FS-Z are different from those derived by the IT2FS technique, as shown by the Tornado diagram Fig 15A and 15B.

Table 5. The symbols and descriptions of basic event of barriers' failure fault tree.


(Continued)

Table 5. (Continued)


https://doi.org/10.1371/journal.pone.0307883.t005

Therefore, the rank of selected sensitive events using these two methods also differs. Therefore, IP12 (ventilation system works but is ineffective) with a prior probability of $2.286824 \times 10^{-3}$ and D10 (defective emergency shutdown sensor) with a prior probability of $5.264846 \times 10^{-3}$ are the most critical BEs in the tornado diagram derived from IT2FS-Z (Fig 15A) and IT2FS data (Fig 15B), respectively.

Furthermore, the BEs in the two fuzzy approaches have different prior probabilities. Thus, a CBE may be among the first fifteen priorities in one calculation mode, but it may be out of this prioritization in another method. For example, D11 (Insufficient detector coverage) ranks 11 in IT2FS-Z calculation method and 23 in IT2F, and D13 (Sensor operation only at very high gas concentration) ranks 12 in IT2FS-Z and 21 in IT2F. On the other hand, while R06 (malfunctioning pressure gauge) ranked 10th in terms of significance and impact on the top event in the IT2FS-based calculations, it did not make it into the top 15 CBEs in the IT2FS-Z calculations.

These differences highlight the importance of considering the confidence level using the Znumber. This is because using the Z-number changes the ranking of CBEs in terms of importance. By bringing the results closer to the real world, the Z-number will help industry experts plan and allocate resources more effectively, leading to the most significant possible reduction in accident-related costs.

Table 6. FPS and FFP values of the basic events of the top event fault tree based on IT2FS-Z.


https://doi.org/10.1371/journal.pone.0307883.t006 Secondly, given this study's ultimate goal of predicting the posterior probability of event occurrence and barrier failure, using z-numbers to make CBE prior probabilities more accurate and realistic leads to more accurate predictions and better results in beta distribution calculations.

Thirdly, this sensitivity analysis using a Bayesian network is a dynamic method that allows managers and experts to be aware of the essential CBEs at all times, providing them greater flexibility in short-term planning.

# 4.5. Probability adapting

Due to incomplete Accident documentation in the industry studied, several hypothetical demands and failures related to CBEs were considered for the last five years; this stage of the

Table 7. FPS and FFP values of the basic events of the top event fault tree based on IT2FS.


https://doi.org/10.1371/journal.pone.0307883.t007 study was conducted by a brainstorming session with the consultation of experts. These events can be seen in Table 11. 4.5.1. Beta distribution. By determining the incidents related to the CBEs over five years and using the likelihood values obtained from the experts' opinions as the prior probability, it was possible to calculate the posterior probability of the CBEs. Notably, to reduce the uncertainty more in the study and based on previous studies, the value of variances of $10^{-4}$ and $10^{-5}$ was considered for beta distribution calculations.

S2A and S2B Tables in S1 Table show the values of $\alpha$ (the number of failures in demand associated with the CBEs) and $\beta$ (the number of successes) in IT2FS-Z and IT2FS for years zero to five with variances of $10^{-4}$ and $10^{-5}$. The likelihood obtained from the expert opinions is the probability of year zero.

Table 8. FPS and FFP values of the basic events in the barrier failure fault tree based on IT2FS-Z.


(Continued)

Table 8. (Continued)


https://doi.org/10.1371/journal.pone.0307883.t008

Although the comparison between IT2FS-Z and IT2FS shows the difference in the posterior probabilities obtained, considering variances difference also helps reduce the uncertainty in the final results as much as possible. Ultimately, the posterior probabilities will be closer to reality with greater certainty.
4.5.2. Sensitivity analysis of methodology. The sensitivity analysis validates and clarifies the performance of IT2FS and IT2FS-Z according to the information provided in Tables 1214. The amount of variation of the posterior probability compared to the prior probability in different fuzzy states and different variances is comparable, which is explained in detail in sections 4.5.3 and 4.5.4. This can facilitate the determination of the worst case in posterior probability and the decision-making process by considering multiple aspects.
4.5.3. Posterior probability of the basic events. Calculating the posterior probability of CBEs for years zero to five (Table 12) based on the $\beta$ and $\alpha$ values shows that the overall trend in the posterior probability of CBEs over five years is upward (Fig 16). This trend is consistent with the study by Ahmadi et al. [64].

According to Fig 16, The comparison of results reveals that incorporating Z-numbers to integrate the confidence levels in experts' opinions reduces both prior and posterior probabilities (Fig 16B). This reduction aligns the results more closely with real-world scenarios, enhancing the model's predictive accuracy and reliability. Notably, when comparing the fuzzy calculations in IT2FS and IT2FS-Z, utilizing Z-numbers results in lower probabilities for both prior and posterior assessments, indicating a more cautious and conservative approach to risk estimation.

Table 9. FPS and FFP values of the basic events in the barrier failure fault tree based on IT2FS.


(Continued)

Table 9. (Continued)


https://doi.org/10.1371/journal.pone.0307883.t009 Furthermore, the calculations based on the beta distribution for predicting future events, considering variances of $10^{-4}$ and $10^{-5}$, demonstrate that the variance of $10^{-4}$ signifies a higher probability of the event occurring in the future (Fig 16A and 16B). This distinction underscores the significance of selecting appropriate parameters, such as variance values, to improve the precision and robustness of risk assessments in dynamic environments.

Fig 16 visually represents these findings, illustrating the trend in posterior probabilities of CBEs over five years. The comparison between IT2FS and IT2FS-Z with variances of $10^{-4}$ and $10^{-5}$ showcases the impact of variance selection on the probability estimations. Specifically, the

![img-10.jpeg](img-10.jpeg)

Fig 11. Comparison between probability of BEs calculated using IT2FS-Z and IT2FS in FTA. https://doi.org/10.1371/journal.pone.0307883.g011

![img-11.jpeg](img-11.jpeg)

Fig 12. Comparison between probability of BEs calculated using IT2FS-Z and IT2FS in ETA.
https://doi.org/10.1371/journal.pone.0307883.g012
higher posterior probabilities observed with the variance of $10^{-4}$ in the IT2FS (Fig 16A) state highlight the increased confidence level in predicting critical events, while the lower probabilities associated with the variance of $10^{-5}$ in the IT2FS-Z model (Fig 16A) emphasize a more conservative risk assessment approach.

By leveraging these insights and understanding the impact of Z-numbers and variance selection on probability estimations, industry professionals can make more informed decisions, proactively address potential risks, and enhance safety measures to ensure operational resilience and efficiency in real-world applications.
4.5.4. Posterior probability of barriers and consequences. The posterior probability of CBEs for years one to five were entered separately into the BN, and the posterior probability of barriers failure and consequences for each year were calculated by updating the Bayesian network. The results of calculating the posterior probability of barrier failure in different fuzzy states with variances of $10^{-4}$ and $10^{-5}$ are shown in Table 13. The results of this table were compared in Fig 17.

The overall comparison of the results in Fig 17 shows that combining Z-number with IT2F has led to significant changes in the posterior probability of barrier failure. In the IT2FS-Z mode, the posterior probability for both DPB (Fig 17B) and IPB (Fig 17C) has a significant difference in the variance of $10^{-4}$ compared to the variance of $10^{-5}$, while this difference is not as
![img-12.jpeg](img-12.jpeg)

Fig 13. BN mapping from bow-tie ("a" is fault tree side of bowtie. "b" is event tree side with fault trees of barriers failure).
https://doi.org/10.1371/journal.pone.0307883.g013

Table 10. Prior and probability of barriers failure and consequences based on BN.


https://doi.org/10.1371/journal.pone.0307883.t010 great for RPB (Fig 17D) and EPB (Fig 17A). This is due to the high number of CBEs present in the fault tree of DPB (seven CBEs) and IPB (six CBEs), which clarifies the effect of the posterior probability of these basic events in the respective barrier. While in the IT2F method, a significant difference in posterior probability can be seen in RPB, in addition to DPB and IPB, during the five years, which can be due to not considering the level of certainty of experts in their opinions.

This issue shows the importance of reducing the uncertainty in the determination of the CBEs and in the planning for the control and prevention of accidents involving spherical tanks.

The results for the posterior probability of all four outcomes (A: near miss, B: mishap, C: incident, D: accident) are shown in Table 14. The results of this Table were compared in

![img-13.jpeg](img-13.jpeg)

Fig 14. a: Prior probability of barrier failure. b: Prior probability of consequences. https://doi.org/10.1371/journal.pone.0307883.g014

![img-14.jpeg](img-14.jpeg)

Fig 15. a: Tornado graph displaying the top fifteen CBEs in the IT2FS-Z BN. b: Tornado graph displaying the top fifteen CBEs in the IT2FS BN.

Table 11. Five-year cumulative table of CBE-related failures and successes.


*F: Failure S: Success https://doi.org/10.1371/journal.pone.0307883.t011

Fig 18. In the IT2F computation, the results obtained using the $10^{-4}$ variance, in comparison to those obtained using the $10^{-5}$ variance, indicate a worse case or the so-called higher posterior probability for barriers (Fig 18). This difference in the value of posterior probabilities increases towards the final years. This indicates the impact of various factors, such as wear and tear of equipment, on the increase in the probability and severity of accidents over time.

For a better comparison of the results, in addition to Figs 18 and 19 has been drawn without the trend plot for near miss to show the difference between the plots for the other consequences. Accuracy in Fig 19 shows that plot ordering in Fig 19B (mishap) is not comparable to the scheme in Fig 17B (DPB). To explain this problem, it can be said that in addition to the DPB as a direct barrier, other barriers also indirectly affect the probability of the subsequent consequences. The same applies to the 19d (accident) and 17d (EPB) graphs.

In general, combining the experts' confidence levels in their opinions using the Z-number has lowered the probability level in both prior and posterior cases compared to the point where only IT2FS was used. Yazdi et al. obtained results using type 1 fuzzy and Z-number in line with this study [60].

The trends in the posterior probability indicate that the method presented provides more reliable, realistic results over time. Irrespective of the difference between the different modes in the results, as seen in Figs 17-19. With this method's continuous learning principles, the general trend in predicting future years' probabilities is incremental. This dynamic prediction helps industries prioritize the necessary preventive measures by analyzing the results and spending the least to achieve the most significant benefit in reducing spherical tank accidents.

Integrating IT2FS, Z-numbers, and Bayesian networks offers a more sophisticated and comprehensive approach to dynamic risk assessments than traditional methods. The model can better handle uncertainties and provide more accurate risk predictions by incorporating fuzzy logic and expert opinions through Z-numbers. Traditional methods like FTA, ETA, and bowtie are widely used for risk assessment in various industries [25, 26]. While these methods

Table 12. The posterior probability of CBEs over the FIVE years.


https://doi.org/10.1371/journal.pone.0307883.t012 provide a systematic approach to identifying potential failures and consequences, they may not effectively handle uncertainties and dynamic changes, while the introduced method Can overcome this limitation.

Another traditional method for risk assessment involves Monte Carlo simulation, which is useful for probabilistic analysis [70]. However, it may not capture the complexity of uncertainties and dependencies as comprehensively as the integrated IT2FS, Z-numbers, and Bayesian networks approach.

In conclusion, the integration of IT2FS, Z-numbers, and Bayesian networks not only improves the accuracy of dynamic risk assessments but also enhances the model's real-world

Table 13. The posterior probability of barriers failure based on beta distribution and BN.


${ }^{*} \mathrm{p}:$ probability https://doi.org/10.1371/journal.pone.0307883.t013 applicability by addressing uncertainties more effectively and providing valuable insights for decision-making in practical settings.

Despite these advantages, the present method does not separate the types of uncertainties. Future research could explore integrating techniques that account for both aleatory and epistemic uncertainties to enhance the current methodology and enable a more comprehensive risk assessment framework. Aleatory uncertainty is a natural variation, haphazardness, or incongruity of a physical system. uncertainty epistemic is based on ambiguity, vagueness, imperfection, ignorance, and deficiency in system behaviors [71]. This integration would enable a more comprehensive and robust risk assessment framework, capable of handling the complexities of both aleatory and epistemic uncertainties. By incorporating these advancements, researchers can refine risk assessment models, leading to more informed decision-making and improved safety outcomes in industrial settings.

Another limitation of this study is that implementing this model in practice may pose challenges, mainly due to the complexity involved in interpreting and propagating uncertainty through the network's layers. Moreover, although powerful, the fuzzy logic components might require additional effort for some industry practitioners to grasp and utilize effectively. To address this limitation and make this methodology more accessible to industry experts, developing an application or software tool based on the fuzzy logic and Bayesian network approach utilized in this study is suggested. This software application can serve as a user-friendly platform for practitioners to input their data, visualize the risk assessment process, and better understand how uncertainty propagates through the network. Additionally, the software can

Table 14. The posterior probability of consequences based on beta distribution and Bayesian network.


- p: probability https://doi.org/10.1371/journal.pone.0307883.t014 include tutorials and training modules to assist users in learning and applying the methodology effectively within their work environment.

Furthermore, to enhance the usability of this proposed methodology, it is suggested to incorporate a case study, like this study's case about spherical tanks, or practical examples that


Fig 16. The prior and the posterior probability of the CBEs. (a: IT2FS. b: IT2FS-Z). https://doi.org/10.1371/journal.pone.0307883.g016

![img-15.jpeg](img-15.jpeg)

**Fig 17. The posterior probability of barriers failure.** (A: RPB. B: DPB. C: IPB. D: EPB). <https://doi.org/10.1371/journal.pone.0307883.g017>

![img-16.jpeg](img-16.jpeg)

**Fig 18. The posterior probability of consequences.** (A: Near miss. B: Mishap. C: Incident. D: Accident). <https://doi.org/10.1371/journal.pone.0307883.g018>

![img-17.jpeg](img-17.jpeg)

Fig 19. The posterior probability of the consequences in different calculations, except for IT2FS(VAR = 10<sup>-4</sup>) (A: Near miss. B: mishap. C: Incident. D: Accident).

https://doi.org/10.1371/journal.pone.0307883.g019

demonstrate the step-by-step application of the fuzzy logic and Bayesian network approach in real-world scenarios. The aim of these practical illustrations is to bridge the gap between theoretical complexity and practical implementation, making it easier for industry practitioners to grasp and utilize this methodology effectively.

## 5. Conclusions

This study presents a method for dynamic risk assessment of spherical tanks in a refinery industry using a combination of interval type 2 fuzzy and Z-number (IT2FS-Z) along with the beta distribution's mean and the SHIPP concept. The first step was to draw a fault tree as part of a bow-tie diagram to identify the events leading to the top event. Then the possible consequences that the top event could cause were defined.

Based on the SHIPP concept, barriers were defined for each consequence, and the Fault Tree associated with failing each barrier was drawn.

Next, the quantitative probability of the base event in both the top event and barrier fault trees was determined using expert opinion. The IT2FS method was used to reduce the uncertainty of the judgments, and the Z-number was used to increase the confidence in the opinions to make the judgments as close to reality as possible. In addition, the power average operator weighting method was used to reduce the conflict between the experts' opinions.

The bow-tie diagram was mapped into the Bayesian network following the previous steps. The first step was to identify the number of the fifteen most sensitive BEs related to the failure of the barriers in the Bayesian network to determine the posterior probability of consequences and the barrier failure. This part was done using data from IT2FS and IT2FS-Z computations to allow a comparison of the results from both.

Then, the number of demands and failures related to CBEs in the last five years were recorded, and their posterior probability was calculated using the mean of the beta distribution. The posterior probability of the barriers and consequences for five consecutive years was obtained by updating the BN based on the posterior probability of CBEs.

Based on the results obtained, the overall posterior probability of consequences shows an increasing trend over five years. Comparing the results from IT2FS-Z and IT2FS shows differences due to the effect of expert confidence in the IT2FS-Z method. These differences are more evident in the $10^{-4}$ variance than in the $10^{-5}$ variance.

Implementing the integrated IT2FS-Z and Bayesian network model in industrial settings holds significant potential to substantially improve workplace safety and operational efficiency. By utilizing this model for dynamic risk assessment, industry professionals stand to make significant strides in reducing accident rates, thereby fortifying safety protocols and mitigating operational risks. The practical implications of embracing this model encompass more precise risk predictions, early detection of potential hazards, and informed decision-making to prioritize preventive measures effectively. Ultimately, integrating IT2FS-Z and Bayesian networks presents a practical and dependable approach for industry professionals to elevate safety performance and optimize risk management strategies in real-world scenarios.

# Supporting information 

S1 Appendix. Calculate the basic event (IP12) probability by aggregating four experts' opinions.
(DOCX)
S1 Table. Containing the following: S2A Table. $\alpha$ and $\beta$ values were obtained based on IT2FS-Z for the first to fifth years. S2B Table. $\alpha$ and $\beta$ values were obtained based on IT2FS for the first to fifth years.
(DOCX)

## Acknowledgments

This study is part of the Corresponding author's Ph.D. thesis supported by Hamadan University of Medical Sciences with the research ethics certificate: IR.UMSHA.REC.1401.572. The authors would also like to thank Dr. Mohammad Yazdi for his guidance.

## Author Contributions

Conceptualization: Mostafa Mirzaei Aliabadi, Rouzbeh Abbassi, Vahid Ahmadi Moshiran.
Data curation: Vahid Ahmadi Moshiran.
Formal analysis: Mostafa Mirzaei Aliabadi, Omid Kalatpour, Omran Ahmadi, Vahid Ahmadi Moshiran.

Investigation: Vahid Ahmadi Moshiran.
Methodology: Mostafa Mirzaei Aliabadi, Rouzbeh Abbassi, Omid Kalatpour, Omran Ahmadi, Vahid Ahmadi Moshiran.

Project administration: Mostafa Mirzaei Aliabadi.
Software: Vahid Ahmadi Moshiran.
Supervision: Mostafa Mirzaei Aliabadi, Rouzbeh Abbassi.
Writing - original draft: Vahid Ahmadi Moshiran.

Writing - review \& editing: Mostafa Mirzaei Aliabadi, Rouzbeh Abbassi, Omid Kalatpour.
