# Dynamic Reliability Assessment of Flare Systems by Combining Fault Tree Analysis and Bayesian Networks 

Sohag Kabir ${ }^{\mathrm{a}, \mathrm{b}}$, Mohammed Taleb-Berrouane ${ }^{\mathrm{c}}$, and Yiannis Papadopoulos ${ }^{\mathrm{a}}$<br>${ }^{a}$ Department of Computer Science and Technology, University of Hull, Hull, HU6 7RX, UK<br>${ }^{\mathrm{b}}$ Department of Computer Science, University of Bradford, BD7 1DP, Bradford, UK<br>${ }^{\text {c }}$ Faculty of Engineering and Applied Science, Memorial University of Newfoundland, St. Johns, NL A1B 3X5, Canada


#### Abstract

Flaring is a combustion process commonly used in the oil and gas industry to dispose flammable waste gases. Flare flameout occurs when these gases escape unburnt from the flare tip causing the discharge of flammable and/or toxic vapor clouds. The toxic gases released during this process have the potential to initiate safety hazards and cause serious harm to the ecosystem and human health. Flare flameout could be caused by environmental conditions, equipment failure and human error. However, to better understand the causes of flare flameout, a rigorous analysis of the behaviour of flare systems under failure conditions is required. In this article, we used fault tree analysis (FTA) and the dynamic Bayesian network (DBN) to assess the reliability of flare systems. In this study, we analysed 40 different combinations of basic events that can cause flare flameout to determine the event with the highest impact on system failure. In the quantitative analysis, we use both constant and time-dependent failure rates of system components. The results show that combining these two approaches allows for robust probabilistic reasoning on flare system reliability, which can help improving the safety and asset integrity of process facilities. The proposed DBN model constitutes a significant step to improve the safety and reliability of flare systems in the oil and gas industry.


Keywords: Reliability, Fault tree analysis, ecological risk, Bayesian network, Flare system.

## 1 Introduction

Technological systems are widely used in many areas. These systems make our lives more comfortable; however, energy is needed to operate these systems. Assurance of an uninterrupted supply of energy is a priority for society in order to efficiently utilize the available energy sources and develop new sources for future use. Of many energy sources, crude oil contributes significantly to the total world energy consumption. For example, in 2014, crude oil was estimated to provide $52.5 \%$ of the worlds energy, out of which oil and natural gas accounted for $31.3 \%$ and $21.2 \%$, respectively (IEA, 2016). According to BP (2017), there were 1706.7 billion barrels of oil and 186.6 trillion cubic metres of gas reserves available worldwide at the end of 2016. The distribution of the world gas and oil reserves is shown in Fig.1. Fig. 2 shows the global natural gas and oil production for the last eleven years and it shows that production has increased in recent years.

The increased production rate of oil and gas in every year shows how heavily we rely on these as energy sources. Our high dependence on gas and oil as an energy source has its own attendant impact

![img-0.jpeg](img-0.jpeg)

Figure 1: Distribution of (a) world gas reserves and (b) world oil reserves (BP, 2017)

![img-1.jpeg](img-1.jpeg)

Figure 2: Global natural gas and oil production until 2016

on the environment. During the crude oil production process, different associated natural gases (mainly hydrocarbons) are produced. A typical natural gas sample contains *CH₄*, *C₂H₆*, *C₃H₈*, *n-C₄H₁₀*, *i-C₄H₁₀*, *n-C₅H₁₂*, *i-C₅H₁₂*, *C₆H₁₄*, *C₇H₁₆*, *H₂S*, *CO₂*, and *N₂*, where *‘n’* stands for *‘normal’*, i.e., straight chain, and *‘i’* stands for *‘iso’* or branched-chain alkanes (Fawole et al., 2016; McEwen and Johnson, 2012; Ismail and Umukoro, 2016; Sonibare and Akeredolu, 2004). These associate gases become a waste stream and are either vented or flared due to the unavailability or inadequacy of technology, infrastructure, and market structure. These actions have a harmful impact on the environment (Fawole et al., 2016; Sonibare et al., 2010; Osuji and Adesiyan, 2005).

In addition to venting and reinjecting, flaring is a common method used to dispose the natural gases associated with extracted crude oil in upstream operations, downstream refining, and chemical processing industries. Flaring is commonly used to dispose of hydrocarbon gases by the oil companies due to their cost-effectiveness and ability to burn efficiently (Anejionu et al., 2015). The primary function of a flare is to oxidize associated gases through combustion to produce less harmful emissions to the atmosphere rather than simply venting the gases, hence allowing safe, reliable, and efficient removal of waste gases. Flare systems are increasingly susceptible to weather conditions, such as wind, which can severely affect the combustion efficiency of the system. Reduced combustion efficiency would lead to the emission of unburned gases such as soot, carbon monoxide, and hydrogen sulphide to the atmosphere. The inefficient combustion of methane will result in an increase in greenhouse gas emissions. Inefficiency in sour gas flares will result in the emission of toxic gases such as hydrogen sulphide, which may have hazardous impacts on the environment as a continuous exposure to which is hazardous to the health of people and animals (Hassan and Kouhy, 2013; Zadakbar et al., 2011; Ismail and Umukoro, 2012; Sinaki et al., 2011). Zadakbar et al. (2011) have studied the risks associated with the flare flame-out condition.

As flaring is a very common activity in process industries, and failures of flare systems have the potential to cause significant harm to humans and the environment, it is expected that flare systems have high

level of reliability. A safety and reliability analysis will assist to recognize the potential causes of flare system failures, thereby providing potential solutions to improve safety by preventing failures. There are many reliability analyses approaches available to evaluate the reliability of the systems. One of the popular approaches for reliability assessment is the FTA (Vesely et al., 2002). FTA is a deductive analysis method, in which investigation begins with a hazardous event. It then works backwards to find the root causes of the hazardous event. The causes of system failure are represented as logical relationships among different system components' failure (i.e., basic events (BEs) in a fault tree) and Boolean gates such as 'AND' and 'OR' gates are used to represent these relationships. Even though fault tree analysis has some limitations, it has been widely applied for systems reliability and risk assessment (Bhangu et al., 2015; Renjith et al., 2010; Ramesh and Saravannan, 2011; Ferdous et al., 2009; Khan et al., 2002; Khan and Abbasi, 2000). Classical fault trees are not suitable for capturing time-dependent behaviour and it is not suitable for analysing systems if there are mutually exclusive basic events or common cause failures. Moreover, events in classical FTs are considered statistically independent, however, in practice this is not always a valid assumption (Bobbio et al., 2001). In situations where events are statistically dependent, this assumption may produce misleading results about system reliability.

In recent years, the Bayesian network (BN) has been increasingly used in system safety and reliability analysis applications. As a graphical inference methodology, BN expresses causal relationships among events. BN can either be used for the prediction of the probability of unknown variables or for updating the probability of known variables given some evidence. Weber et al. (2012) and Kabir and Papadopoulos (2019) have provided a comprehensive review of the application of BNs in dependability analysis and risk assessment. Applications of BNs in systems engineering include but are not limited to: reliability and risk analysis (Khakzad et al., 2013; Hänninen et al., 2014; Yazdi and Kabir, 2018; Yuan et al., 2015), system safety improvement (García-Herrero et al., 2013; Trucco et al., 2008), mapping of fault trees into Bayesian networks (Bobbio et al., 2001; Barua et al., 2016; Zarei et al., 2017; Kabir et al., 2014b; Yeo et al., 2016), and diagnostic analysis (Wu et al., 2015; Musharraf et al., 2016).

Considering the fact that the flare flame-out has high potential to cause adverse environmental effects, this paper aims at performing reliability analysis of a flare system. In the past, Berrouane and Lounis (2016) evaluated the reliability of flare system using FTA. That analysis was not rigorous and has a number of limitations:

- Due to the use of classical FTA, during the reliability assessment, the study was not able to consider the dynamic characteristics of the system and was not able to model the statistical dependencies between the events. This may have produced inaccurate results.
- The analysis was done based on the constant failure probability of events, however, in practical system many components have time-dependent failure rates due to exposure to fatigue and ageing, which was not considered.
- The criticality of the events with respect to their contribution to the occurrence of flare flame-out was not studied.

In this paper, we overcome the above mentioned limitations of the previous study by using both FTA and DBN for the reliability assessment of the flare system. We retained the FT used in the previous study to determine the root-causes of the flare flameout. In this current study, we proposed to map a FT into DBN, and the occurrence probability of the hazardous event (flare flameout) is estimated by mapping the FT into a DBN, which addresses the issue of dependency between events. Moreover, in the analysis, both constant and time-dependent failure rates of the events are considered at the same time. We compare the results obtained by FTA and DBN, and it shows that the reliability of the system obtained by the FTA is not accurate. Finally, we determine the criticality of the components using the DBN model, which will

be particularly important for the decision maker to understand where to put more effort to enhance the reliability of the system.

# 2 Methodologies Used 

### 2.1 Fault Tree Analysis

A fault tree (FT) is a deductive, top-down graphical method that is used to identify the potential causes of undesired events, often referred to as a top event (TE). The graphical representation of the FT is based on Boolean logic, which shows logical relationships between different faults and their causes. The top event usually represents a system failure which may lead to safety hazards or economic loss. As a deductive method, the derivation of fault tree starts by considering the TE as the root of the tree and subsequently, constructing the tree downwards until the basic events (BEs) causing the top event are known. In a FT, a BE is symbolised by a circle and it represents a lower level fault which does not require any further decomposition. An intermediate event, graphically represented by a rectangle, is an event that is caused by other lower-level events occurring further down the tree. In an FT, the 'AND' and the 'OR' gates are most widely used. An example FT is shown in Fig. 3.
![img-2.jpeg](img-2.jpeg)

Figure 3: An example fault tree
After construction, both qualitative and quantitative analysis could be performed on a FT. Qualitative analysis of a FT usually yields a set of minimal cut sets (MCSs). A MCS is the smallest combination BEs that can cause the top events of the FT. The FT in Fig. 3 can be qualitatively analysed to obtain four MCSs: 1. A.C, 2. A.D, 3. B.C, and 4. B.D. Note that the event $A$ is shared between MCSs 1 and 2, the event $B$ is shared between MCSs 3 and 4, the event $C$ is shared between MCSs 1 and 3, and the event $D$ is shared between MCSs 2 and 4. The quantitative data about system components such as failure rates or failure probabilities are used in the quantitative analysis of FT to evaluate quantitative system properties such as reliability, availability, criticality of components, etc. The quantitative analysis of FT is usually performed under the assumption that the events in the FT are statistically independent. Nevertheless, in practice, basic/intermediate events can be statistically dependent (Talebberrouane et al., 2016; Kamil et al., 2019). Hence, statistical independence assumption could result into an inaccurate evaluation of system reliability and other related indices.

There are many methods available to perform quantitative FTA such as the analytical method, binary decision diagram, and Monte Carlo simulation (Vesely et al., 2002; Kabir, 2017). In analytical method, also known as rare event approximation, mathematical formulas are used to approximate the probability of FTs' top events. If the exponentially distributed failure rate $(\lambda)$ of $B E_{i}$ and the operating time $t$ is provided, then the $B E_{i}$ 's occurrence probability is computed as:

$$
\operatorname{Pr}\left\{B E_{i}\right\}(t)=1-e^{-\lambda t}
$$

Note that the BEs usually represent mechanical components, which are exposed to fatigue or ageing can have time-dependent failure rate distributions defined for them. The Weibull distribution is one of the regularly used life distributions used to define failure behaviour of mechanical components. The probability density function (PDF) of the Weibull distribution is given by:

$$
f(t)=\frac{\beta}{\eta}\left(\frac{t}{\eta}\right)^{\beta-1} e^{-\left(\frac{t}{\eta}\right)^{\beta}}
$$

Where $\beta$ and $\eta$ are the shape and scale parameter, respectively. The occurrence probability of a BE with Weibull distribution can be calculated as:

$$
\operatorname{Pr}\left\{B E_{i}\right\}(t)=\int_{0}^{t} f(t) d t=1-e^{-\left(\frac{t}{\eta}\right)^{\beta}}
$$

As the MCSs are presented as the intersection of the statistically independent BEs, the occurrence probability of a MCS is calculated as (Henley and Kumamoto, 1981):

$$
\operatorname{Pr}\left\{M_{i}\right\}(t)=\prod_{i=1}^{m} \operatorname{Pr}\left\{B E_{i}\right\}(t)
$$

where $m$ is the number of basic events in the MCS, $\operatorname{Pr}\left\{M_{i}\right\}(t)$ is the occurrence probability of the MCS $i$ at time $t$.

Finally, as the TE is the union of the MCSs, the TE probability is approximated as (Esary and Proschan, 1963):

$$
\operatorname{Pr}\{T E\}(t)=1-\prod_{k=1}^{m}\left(1-\operatorname{Pr}\left\{M_{k}\right\}(t)\right)
$$

where $P(T E)$ is the TE's occurrence probability. To address the uncertainty associated with the failure data and system behaviour, fuzzy set theory has been used by several researchers such as (Halloul et al., 2019; Shi et al., 2014; Tanaka et al., 1983; Kabir et al., 2016; Yuhua and Datao, 2005; Markowski et al., 2009; Kabir et al., 2014a).

It is worthwhile noting that, FT software often use "rare event approximation" i.e. simple sum of MCSs probabilities as standard method for quantifying FTs due to efficiency of computation. The calculation is precise only if MCSs do not share events and therefore are statistically independent, otherwise it leads to approximation. The FT handbook suggests that this is typically an accurate approximation and the calculated top event probability value is within about $10 \%$ of the true value if the basic event probabilities are less than 0.1 (Vesely et al., 2002). Even if some the basic event probabilities are greater than 0.1 , the approximation could still be accurate if most of the basic event probabilities are less than 0.1 . For critical applications, the FT handbook suggests application of more accurate approximation approaches.

# 2.2 Bayesian Networks 

Over the years, Bayesian Networks (BN) have gained popularity in system safety and reliability modelling and risk management. BN have the capability to aggregate diverse sources of information in a single model to offer a comprehensive reliability assessment of systems. Like FTs, Bayesian networks contain a qualitative and a quantitative part. The qualitative part of a BN is a directed acyclic graph representing the causal relationship between a set of variables (Pearl, 1988). The quantitative part of a BN includes a set of prior probability distributions for a set of variables and a set of conditional probability distributions defining

the cause-effect relations among the nodes in terms of numerical values. In a BN, if an arc starts at node $X$ and ends in node $Y$, then node $X$ is the parent of node $Y$. A node without a parent is considered as a root node and a node without any child node is considered as a leaf node.
![img-3.jpeg](img-3.jpeg)

Figure 4: Example of a Bayesian Network
BNs utilise the chain rule and $d$-separation rules (Pearl, 1988) while performing inference on the model. According to the d-separation rules, "the root nodes are conditionally independent and all other nodes are conditionally dependent on their direct parents"(Khakzad et al., 2011). In a BN model, chain rule can be used to calculate the joint probability distribution of a set of random variables $\left\{V_{1}, V_{2}, V_{3},, V_{n-1}, V_{n}\right\}$ as:

$$
\operatorname{Pr}\left\{V_{1}, V_{2}, V_{3}, \ldots, V_{n-1}, V_{n}\right\}=\prod_{i=1}^{n} \operatorname{Pr}\left\{V_{i} \mid \operatorname{Parents}\left(V_{i}\right)\right\}
$$

BNs in their classical form cannot model the changes in variables over time, i.e., they perform analysis for a fixed time. DBNs (Neapolitan, 2004) are extensions of classical BNs, which provides a flexible structure and distinctive modelling mechanism for explicit modelling of the temporal progression of a set of variables over time. In a DBN, the overall timeline is divided into several discrete time slices. This permits a node at the $i^{\text {th }}$ time interval to be conditionally dependent on both its parents in the same interval and its own and its parents' states in the previous interval (Khakzad, 2015). Fig. 5 shows a DBN model of the BN of Fig. 4 over a discretized timeline $t \in[0, T]$. The black arcs within the same time interval are the intra-interval arcs, whereas the red dashed arcs connecting the nodes in the consecutive time intervals are the inter-interval arcs. According to Fig. 5, the conditional probability of the copy of node $A$ at time slice $t+\Delta t$ would be $P\left(A^{t+\Delta t} \mid A^{t}\right)$.

As reported in (Abbassi et al., 2016; Baksh et al., 2015; Sigurdsson et al., 2001; Neil et al., 2008; Doguc and Ramirez-Marquez, 2009), both classical and dynamic BNs have been widely used in the risk and reliability assessment of varieties of fields such as chemical process, maritime, aerospace, offshore system, etc. For instance, Torres-Toledan and Sucar (Torres-Toledan and Sucar, 1998) used BNs for relaibility analysis of complex systems and Bayesian reliability of gas network was studied in (Iesmantas and Alzbutas, 2016). DBN was used for risk assessment of a technological system in (Ashrafi and Zadeh, 2017). A widespread use of BNs in safety and reliability assessment is by translating other reliability models such as FTs into

![img-4.jpeg](img-4.jpeg)

Figure 5: A DBN model of the BN of Fig. 4 over a discretized timeline $t \in[0, T]$ (Khakzad, 2015)

Bayesian networks. In the pioneering work, Bobbio et al. (2001) have illustrated how fault trees can be mapped into BNs for reliability evaluation of systems. As shown in Fig. 6, the translation was done in two phases: graphical mapping and numerical mapping. The BEs and intermediate events (logic gates) of the fault trees are mapped to the root nodes and intermediate nodes of BNs, respectively in the graphical mapping phase. Contrarily, the TE is mapped to the leaf node of the BNs. In the numerical mapping phase, BEs' failure probabilities are used to define the prior probabilities of the root nodes and Boolean logic is used to define the conditional probability tables for the other nodes. Bayesian networks have also been used for the quantitative analysis of dynamic and temporal FTs, e.g. in (Boudali and Dugan, 2005, 2006; Montani et al., 2008; Kabir et al., 2018). BN-based approaches have been used for hazard analysis in process industries such as in (Khakzad et al., 2011; Yazdi and Kabir, 2017; Deyab et al., 2018; Taleb-Berrouane et al., 2018).

Once an FT is mapped into a BN model, the predictive analysis could be done on the model to obtain system reliability. Simultaneously, an observation about the status of the BEs could be put on the root nodes. According to these observations, the criticality of BEs could be determined, i.e., the relative contribution of the BEs to the TE occurrence probability could be measured. Utilising the ability to observe the status of a node, diagnostic analysis can also be performed. In this case, the users can provide evidence about the occurrence of the TE, and thereby users knowledge about the components failure probability is updated according to the provided evidence.

# 3 Reliability Analysis of Flare Systems 

### 3.1 Overview of Flare Systems

Gas flare systems (Baukal Jr, 2012) are structures used to collect and burn the disposable gases from different stages of the process plant. The combustion of these disposable gases is performed in a safe manner far from the plant. A typical flare system is shown in Fig. 7. The flare stack collects the flare gases that

![img-5.jpeg](img-5.jpeg)

Figure 6: Fault tree to Bayesian network mapping procedure (Khakzad et al., 2011)
are to be flared. To improve combustion efficiency, the flare tip is designed to allow the entrance of air into the flare. To prevent the flashback of the flare, seals are installed in the stack. The knock-out drum resides at the base of the stack, which operates at a relatively low pressure (Zadakbar et al., 2015). The knock-out drum should be able to prevent liquid carryover into the flare while the flare operates with large gas and liquid loads (Akeredolu and Sonibare, 2004).

Flare systems are safety barriers or layer of protection from overpressure. They allow pressure relief and the safe disposal of toxic and/or flammable gases. During both normal operations and abnormal conditions, such as plant upsets or emergency shutdowns, the flare system should be able to handle quick changes in gas flow and maintain the flame. However, these flare systems can turn to a source of hazards if their operation is not properly controlled. One of the hazardous operating conditions is when the gases are released from the flare stack without being burned. This is known as "flame-out". This incident can present human and environmental toxicity and the release can lead to vapour cloud explosions (V.C.E). The scenarios leading to this incident are studied and analysed in this paper. The analyses are based on probabilistic approaches to calculate the occurrence probability of the flame-out and to identify the most critical events leading to the flame-out incident.

# 3.2 Reliability Analysis using FTA 

Fault tree analysis was performed to determine the primary causes of failure of the flare system. In this study, we considered "flare-flameout" as the hazardous event (TE of the FT) and the fault tree of Fig. 8 shows the logical causes of the occurrence of this event. The failure data of the BEs of this FT is presented in Table 1. Many of these BEs have fixed failure probabilities, whereas some of the BEs have their lifetime defined using Weibull distribution. After performing qualitative analysis on the FT of Fig. 8, we obtained

![img-6.jpeg](img-6.jpeg)

Figure 7: A classical flare system (Akeredolu and Sonibare, 2004)

40 minimal cut sets (MCSs) as seen in Table 2. Each of these MCSs can independently cause the flare flame-out.

The probability of the occurrence of the MCSs were calculated using Equation (4) and data from Table 1. Without loss of generality, and for the purposes of comparison, the calculation was performed for 10 years operating time with 1 year interval period. Table 3 presents the occurrence probability of the flare flameout condition for different mission time.

It is worth noting that, the TE probability is obtained using rare event approximation by considering that the MCSs are statistically independent. However, from Table 2, it is evident that MCSs share basic events and they are therefore statistically dependent. Moreover, for the above mentioned mission time, the probability of most of the BEs is greater than 0.1. That means, as suggested in Section 2.1, more accurate approximation of top event probability is needed. Bayesian network is used in the following section for this purpose.

# 3.3 Reliability Analysis using Bayesian Network 

To perform the reliability analysis of the flare system using the DBN-based approach, we first translated the FT of the failure behavior of the flare system into a discrete-time BN. In order to model the time dependent

![img-7.jpeg](img-7.jpeg)

Figure 8: FT of flare flameout condition of the flare system (Berrouane and Lounis, 2016)

Table 1: ID, Name, and failure rates of the BEs of the fault tree in Fig. 8


Behaviour of BEs 1, 2, 7, 8, 9, and 10, the DBN shown in Fig. 9 is formed. The prior probability tables of the root nodes associated with the BEs with constant failure probability are populated using the data from table 1. On the other hand, the prior and the conditional probabilities, at different time slices, of the nodes associated with the BEs with time-dependent failure behavior are populated based on the Weibull distribution defined for them. The CPT of each of the intermediate nodes of the BN is generated according

Table 2: List of MCSs to Cause the Flare System Failure


Table 3: Flare flameout occurrence probability based on FTA


to the behaviour of the logic gate it signifies.
The next step is to run a query on the DBN model, which would give us the occurrence probability of the flare flameout at different point in time. According to the DBN based technique, the probability of the occurrence of the flare flameout after 10 years is $1.01 \times 10^{-3}$. If we compare this value with the value estimated by the rare event approximation of FT, then we can notice that this value is $34.42 \%$ smaller. This is because the DBN approach considers dependency among events and provides a global reliability assessment, whereas the rare event approximation approach does not consider dependency among events, which is not valid in this case. Fig. 10 shows the comparison between the occurrence probabilities of the flare flameout at different operating time estimated by rare event approximation and DBN.

Until now, we used the failure probabilities of the BEs and used predictive analysis on the BN to evaluate the unreliability of the system. By providing evidence on the Bayesian network model, diagnostic analysis

![img-8.jpeg](img-8.jpeg)

Figure 9: DBN of the FT in Fig. 8
is also performed. For example, if there exists any evidence about the failure of flare system, then based on this knowledge we can update our belief about the basic events failure probabilities. This will allow calculating the posterior probability of the BEs given that the system has failed. For the flare system, we obtained the posterior probability distribution of the BEs and the comparison between the prior and posterior probabilities is shown in Fig. 11. Note that this chart uses logarithmic scale for Y-axis. Based on these updated probabilities of the BEs, a new set of analyses could be performed.

# 3.3.1 Criticality analysis 

In FTA, criticality analysis plays a vital role by identifying the critical events causing the TE of a FT. Criticality is measured in terms of the relative contributions of the events to the occurrence probability of the top event. Different approaches like the risk reduction worth (RRW) and Birnbaum importance measure (BIM) are widely used (Vesely et al., 2002).

![img-9.jpeg](img-9.jpeg)

Figure 10: Comparison of flare flameout probability estimated by rare event approximation of FT and BN methods

![img-10.jpeg](img-10.jpeg)

Figure 11: Comparison between prior and posterior probabilities of BEs (logarithmic scale used for Y-axis)

Note that in this paper BIM is used to measure the criticality of BEs as an illustrative purpose, however, different other approaches can be used.BIM of a basic event, $I_{B E_{i}}^{B I M}$, is evaluated as follows by taking the difference between TE probabilities by considering the basic event's probability as 1 and 0 , respectively.

$$
I_{B E_{i}}^{B I M}=P\left(T E \mid P\left(B E_{i}\right)=1\right)-P\left(T E \mid P\left(B E_{i}\right)=0\right)
$$

where $P\left(T E \mid P\left(B E_{i}\right)=1\right)$ and $P\left(T E \mid P\left(B E_{i}\right)=0\right)$ are the TE probabilities while the probability of the $B E_{i}$ is considered as 1 and 0 , respectively.

Using the BN model, BIM of an event can be calculated as:

$$
I_{B E_{i}}^{B I M}=P\left(T E \mid B E_{i}=\text { True }\right)-P\left(T E \mid B E_{i}=\text { False }\right)
$$

Where $P\left(T E \mid B E_{i}=\right.$ True $)$ is the TE probability while observing the state of $B E_{i}$ as true and $P\left(T E \mid B E_{i}=\right.$ False) is the TE probability while observing the state of $B E_{i}$ as false. Once the BIM of all basic events are determined, they are ranked according to their criticality. The higher the value of the $I_{B E_{i}}^{B I M}$ the greater the importance of the event and vice versa.

Table 4: Criticality of the BEs based on the BN method


As the BN approach can consider statistical dependency among the events and the probability of most of the BEs is greater than 0.1 , for more accurate estimation, we use BN based approach as described above to calculate the importance of the BEs. The result is shown in Table 4. As seen from the table, BE11 and BE15 are recognized as the most critical events. These events correspond to Relief PCVs closed and Pumping phenomenon. This information is particularly important in aiding the stakeholders to identify the weakest part of the flare system, thus helping them to channelling their efforts to the identified part of the system to improve the reliability of the flare system.

The primary goal of this article was to evaluate the reliability of flare systems. A previous study based on FTA was found in the literature; and we have identified a number of limitations of that study. To overcome these limitations, we translated a FT into a DBN, and thereby evaluated the occurrence probability of the flare flameout condition and provided a solution for criticality analysis on a DBN model. Note that the superiority of BN over FTA was highlighted in the comparative study performed in (Khakzad et al., 2011; Taleb-Berrouane et al., 2019). In this study, we utilised the superiority of BN over FTA when it comes to the modelling capacity, capability of integrating evidence and updating probabilities based on observations.

Table 5: Comparison between past and present study based on modelling aspects considered


All these features of BN help to alleviate the limitations of the prior study based on FTA. Regarding the aspects covered by the two studies, Table 5 presented a comparison between the past and the present study. It can be seen that to perform more realistic analysis and to produce more reliable results, the present study considers many aspects which were absent in the past study. Note that none of the study has performed uncertainty analysis for the results. In the future, we have the plan to perform uncertainty analysis of the results by considering different aspects that have the potential to affect the results.

# 4 Conclusion 

Under flare flameout condition, toxic gases such as $\mathrm{H}_{2} \mathrm{~S}$ can be emitted, which can have very adverse effects on the ecosystem and human health. Considering the importance of maintaining efficient flaring throughout the combustion process, in this paper we have analysed the reliability of a flare system using both FTA and Bayesian network approaches. In the FT, we had 15 basic events, and from qualitative FTA, we determined 40 different combinations of basic events that can cause flare flameout. We also obtained the probability of experiencing a flare flameout using both rare event approximation of FT and DBN approaches given the failure data of the BEs. The rare event approximation of the FT approach obtained results by considering the MCSs as statistically independent; on the other hand, the DBN approach produced results by taking into account the dependencies among the events. During analysis, we found that many events in the current study were statistically dependent. For this reason, we have noticed a significant difference between the occurrence probabilities estimated by the approaches. Using DBN, we identified and reported the critical basic events that contributed to the flare flameout condition.
