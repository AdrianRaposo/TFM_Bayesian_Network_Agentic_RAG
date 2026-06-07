# UNIVERSITÀ DEGLI STUDI FIRENZE 

## FLORE <br> Repository istituzionale dell'Università degli Studi di Firenze

## Developing a risk-based maintenance model for a Natural Gas Regulating and Metering Station using Bayesian Network

Questa è la Versione finale referata (Post print/Accepted manuscript) della seguente pubblicazione:

## Original Citation:

Developing a risk-based maintenance model for a Natural Gas Regulating and Metering Station using Bayesian Network / Leoni, Leonardo; Bahoo, Ahmad; De Carlo, Filippo; Paltrinieri, Nicola. - In: JOURNAL OF LOSS PREVENTION IN THE PROCESS INDUSTRIES. - ISSN 0950-4230. - STAMPA. - (2019), pp. 1-10. [10.1016/j.jlp.2018.11.003]

## Availability:

The webpage https://hdl.handle.net/2158/1138919 of the repository was last updated on 2024-0627T10:21:32Z

Published version:
DOI: 10.1016/j.jlp.2018.11.003

Terms of use:
Open Access
La pubblicazione è resa disponibile sotto le norme e i termini della licenza di deposito, secondo quanto stabilito dalla Policy per l'accesso aperto dell'Università degli Studi di Firenze
(https://www.sba.unifi.it/upload/policy-oa-2016-1.pdf)

Publisher copyright claim:

La data sopra indicata si riferisce all'ultimo aggiornamento della scheda del Repository FloRe - The abovementioned date refers to the last update of the record in the Institutional Repository FloRe

# Developing a risk-based maintenance model for a Natural Gas 

## Regulating and Metering Station using Bayesian Network

Leonardo Leoni ${ }^{\mathrm{a}}$, Ahmad BahooToroody ${ }^{\mathrm{a}, \mathrm{b}}$, Filippo De Carlo ${ }^{\mathrm{a}, \mathrm{b}^{*}}$, Nicola Paltrinieri ${ }^{\mathrm{c}}$


#### Abstract

a. Department of Industrial Engineering (DIEF), University of Florence, 50125, Florence, Italy b. IBISLAB, University of Florence, 50125, Florence, Italy c. Department of Mechanical and Industrial Engineering, Norwegian University of Science and Technology NTNU, S.P. Andersens Veg 5, 7031, Trondheim, Norway

During the last decades, the vital role of maintenance activities in industries including natural gas distribution system has cleared up progressively. High costs may induce to reduced maintenance and, in turn, lead to a lower availability and high risk of undesired events. Therefore, a probabilistic model, based on an acceptable level of risk, is required to avoid under and over estimation of maintenance time interval. This paper presents an advanced Risk-based Maintenance (RBM) methodology to optimize maintenance time schedule. Bayesian Network (BN) is applied to model the risk and the associated uncertainty. Based on the proposed methodology, the exact maintenance time for each component would be achieved dependent of risk level. To demonstrate and discuss the applicability of the methodology, a case study of Natural Gas Reduction and Measuring Station in Italy is considered. Results prove that the most critical components are the pilots and the water pipe which have to be serviced every 297 and 298 days respectively, while the most reliable one is the odorization tank with a maintenance interval of 444 days. On the other side the components that require less time in order to have a huge increase of the risks associated to their failures are the pressure and temperature gauge (PTG), the meter and the remote control system (RCS).

Keywords: Risk-based maintenance, Bayesian Network, Natural Gas Reduction and Measuring Station

# 1. Introduction 

Natural gas is one of the most pivotal sources among fossil energy all over the world, particularly for industry and for electric energy production. It covers 20\% of energy consumption in the European Union (Montiel et al., 1996) and its export value to the industrialized countries is progressively increasing (Vianello \& Maschio, 2014). Accidents related to gas distribution and consumption may bring huge damages to environment and humans. In recent years, a striking portion of catastrophic events were related to the gas distribution networks industry. In 2004 the explosion of a natural gas factory in Belgium was lead to considerable number of fatalities and injuries. During the same year, in Paraguay, a conflagration caused by gas leakage led to more than 250 deaths. In 2009, another

explosion caused by gas leakage induced the greatest conflagration in Moscow ever since the Second World War (Han \& Weng, 2011). There could also be some external causes leading to accidents, like the hurricanes that in 2005 and 2008 struck the Gulf of Mexico and damaged gas pipelines (Girgin \& Krausmann, 2016). Considering these accidents, it is inevitably necessary to reduce the risk associated with possible breakdowns in natural gas distribution systems.

To provide a reliable service, maintenance must be implemented. The literature on definition of maintenance in different applications is vast (Bhandari et al., 2015; Garg \& Deshmukh, 2006; Khan \& Haddara, 2003; Okoh \& Haugen, 2013; Sharma et al., 2011). Dhillon (2002) defines maintenance as all the appropriate actions for retaining or restoring to a given condition an item or a part or an equipment. There are four kinds of maintenance: corrective, preventive, proactive and predictive (Iqbal et al., 2017). Corrective maintenance is done after a failure, leading to more risks. On the contrary, preventive maintenance is done before a failure, involving more costs. Another kind of maintenance is Condition-Based Maintenance (CBM), referred as proactive maintenance. In this category, the parameter of interest in the system is monitored and, in case of exceeding the safe operational limits, maintenance is required. Jardine et al. (1999) adopted CBM to study shear pump bearings in a food processing plant, in which vibrations are controlled. A more recent type of maintenance is Risk-Based Maintenance (RBM) (Arunraj \& Maiti, 2007), which integrates reliability with safety and environmental issues and minimizes the probability of system failure and its consequences related to safety, economic, and environment (Khan \& Haddara, 2003). RBM can be adopted to be assured about the level of risk and its associated cost. The base principle of this category is to prioritize the maintenance of the components based on the level of risk (Ambühl \& Sørensen, 2017).

There is a great deal of research on RBM and optimization of maintenance plans (Abbassi et al., 2016; Barua et al., 2016; Dawotola et al., 2012; Khan \& Haddara, 2004; Krishnasamy et al., 2005). Dawotola et al. (2012) proposed a maintenance plan in which both economic and risk aspects are considered. They chose an oil pipeline system as a case study. The optimization process has six steps:

probability of failure estimation, determination of consequences of failure, estimation of risk of failure, calculation of risk reduction, calculation of total cost function and determination of costoptimal inspection frequency of the pipeline in a preventive maintenance policy. The maintenance interval is estimated by minimizing the expected total cost that considers both preventive and corrective maintenance. In another research, a risk-based maintenance strategy is adopted by Krishnasamy et al. (2005) to a power generation plant. The authors have divided the methodology into four stages: scope identification, risk assessment, risk evaluation, and maintenance planning. A Fault Tree Analysis (FTA) is used to estimate the probabilities of failure. This model identifies the critical components and allows reducing the cost related to maintenance.

Meanwhile, Bayesian inference, as a parametric and non-parametric probabilistic method, have attracted a significant attention from researches for increasing both effectiveness and efficiency of RBM applications (Abaei et al., 2017; Arzaghi et al., 2017; Cullum et al., 2018; Nielsen \& Sørensen, 2018; Toroody et al., 2016). Bayesian Network (BN) is generally used for causal representation of the phenomena involved in a complex system or process, where data sources are limited and uncertain (Trucco et al., 2008). As most of the traditional risk analysis techniques (such as FTA and Event Tree Analysis (ETA)) are static and non-updatable conventional model, they regularly fail to fully capture the variation of risks during operation (Paltrinieri and Khan, 2016; Khakzad et al., 2011). Besides, conventional techniques use only binary variables and do not represent conditional dependencies (Martins et al., 2014). Accordingly, based on BN, Abbassi et al. (2016) presented a RBM methodology, applied to an offshore process facility. In this method, risk level is calculated via BN considering the failure probabilities and the possible consequences and the maintenance plan is determined after setting the evidence that the system operates at the lowest possible risk. One year later Pui et al. (2017) proposed a similar methodology applied to an offshore manage pressure drilling, focusing on two critical systems: rotating control device and blowout preventer.

Probability of failures estimation is of prominent importance and is widely established in gas pipelines (Wu et al., 2017; Yuhua \& Datao, 2005). Yuhua and Datao (2005) presented a method to

evaluate the probability of failure for a gas pipeline. Their study is divided in two parts: the first part is a qualitative analysis used to achieve the minimal cut set of a FT in which the pipeline failure is given as top event, while the second part is devoted to a quantitative analysis including the estimation of the failure probability of the top event. To evaluate the probabilities of failure, the authors applied the Delphi method and represented natural linguistic expressions through the fuzzy set theory. In the other more recent research, Wu et al. (2017) developed a probabilistic study about gas pipelines using BN and Dempster-Shafer evidence theory, to deal with expert judgments. Other researchers assessed the reliability of gas pipelines containing corrosion defects (Caleyo et al., 2002; Teixeira et al., 2008). Caleyo et al. (2002) used different methods to estimate the probability of failure: the first-order second-moment iterative reliability method, the crude Monte Carlo integration technique, and the first order Taylor series expansion of the limit state function. On the other side, Teixeira et al. (2008) adopted the first-order reliability method and used Monte Carlo simulation to deal with uncertainty.

Despite the fact that ongoing efforts are made on either gas distribution systems or other operational systems, these fields still lack of RBM application for estimating maintenance time (Zarei et al., 2017). As a result, a risk-based methodology for maintenance scheduling is developed in this work and demonstrated through an application of case study. The objective of this approach is to provide the optimum maintenance time by implementing a BN analysis. The advance of the proposed model has been verified on actual examples of stochastic process of a Natural Gas Regulating and Metering Stations (NGRMS) near Florence, Italy.

# 1.1. Bayesian network 

A wide summary of BN is provided by Barber (2012) and Neapolitan (2004). A BN is a Directed Acyclic (DAG) used for reasoning under uncertainty, in which each node represents a variable and each arc represents a conditional dependency among the variables. It calculates the joint probability distribution of a set of random variables using Eq. (1):
$P(U)=\prod_{i=1}^{n} P\left(X_{i} \mid p a\left(X_{i}\right)\right)$

where $P(U)$ is the joint probability distribution and $p a\left(X_{i}\right)$ is the parent set of variable.
As an example, the joint probability distribution of the variables $X_{1}-X_{4}$ illustrated in Fig. 1 is given by $P\left(X_{1}, X_{2}, X_{3}, X_{4}\right)=P\left(X_{1}\right) P\left(X_{2}\right) P\left(X_{3} \mid X_{1}, X_{2}\right) P\left(X_{4} \mid X_{3}\right)$. When new information about the state/value of any of the node in the network is acquired, BN estimates the updated joint probability distribution based on Bayes' Theorem. Given the evidence that $X_{3}$ is in a state/value $e$ the joint probability distribution is updated using Eq. (2):
$P\left(X_{1}, X_{2}, X_{4} \mid e\right)=\frac{P\left(X_{1}, X_{2}, X_{4}, e\right)}{\sum_{X_{1}, X_{2}, X_{4}} P\left(X_{1}, X_{2}, X_{4}, e\right)}$
![img-0.jpeg](img-0.jpeg)

Fig. 1. Example of a Bayesian Network.

# 2. Developed methodology 

The sequence of the proposed methodology for risk-based maintenance in this study is illustrated in Fig. 2.

![img-1.jpeg](img-1.jpeg)

Fig. 2. Proposed dynamic RBM methodology for NGRMS applying Bayesian Network.
In the first stage, (1.) the system is defined and divided into its components. The relationship among the components is also determined in this phase. Next, (2.) the associated FT is built. The top event (system failure) is broken down into sub events until all the primary events (events that could not be expanded further) are found. Then, (3.) the FT it is transformed into a BN and later would be (4.), where the hazard analysis identifies failure consequences based on historical data. Consequence analysis is executed to model the risk assessment and subsequently RBM. The possible consequences should be mapped into the BN as a children of the top event. These steps are accounted for qualitative risk assessment.

In the next step, (5.) Mean Times To Failure (MTTF) of each component are found using available data. Subsequently, (6.) the annual probability of failure is worked out then. The probability table of root nodes in the BN can be filled with their respective failure probabilities. Next, (7.) is to specify the consequences of system failure (top event) and risk of the operation. The level of risk can be defined in different approaches. Herein, it is proposed to be divided into three different categories:

1) minor risk that is a low level of risk and it is considered acceptable in order to operate safely;
2) major risk that is a higher level of risk that comprehends consequences that may bring damages to environment or to human beings;
3) catastrophic risk that is the highest level of risk and it has to be avoided.

Based on present RBM the optimum maintenance time of components is revised through probability updating. (8.) Setting the evidence that minor risk has occurred at $100 \%$ probability, a backward analysis is conducted on the BN to point out the updated probabilities of the roots (e.g. the probabilities of failure of the components when the system operates at the lowest risk possible). Finally, (9.), based on the updated probabilities the maintenance interval is calculated.

# 3. Application of the methodology to NGRMS 

In order to demonstrate the applicability of the developed RBM methodology, it is applied to NGRMS as a case study. The main functions of a NGRMS are measuring the flow of the gas and reducing the gas pressure to adapt it to the subsequent utilities. a NGRMS has four critical groups of different components, that can lead to a failure of the system as shown in Table 1.

Table 1
Groups and components of NGRMS.



Pressure regulator keeps the downstream function at a pre-determined value and at the same time it has to guarantee the required flow. The gas flow is regulated by increasing or decreasing the crosssectional flow area. Pilot is needed to have more precision and a faster change of the gas flow. Filter has to block the impurities, both solid and liquid which are always present in the gas. The filters must be set before the pressure regulator. The measuring group measures both the flow and its characteristics parameters. The gas flow is measured in cubic meters for every hour. Remote control system allows to measure the data from distance. Preheating group is placed after filter and before pressure regulator. As the temperature decreases along with reduction of pressure, also to prevent the formation of ice, the gas is heated by an exchanger in which there is a flow of water. A very precise quantity of odorizer, which is usually tetrahydrothiophene (THT), must be added to warn of any gas leaks. Resulted FT and its corresponding BN are shown in Fig. 3. and Fig. 4., respectively. As it can be seen in Fig. 5., the possible consequences are categorized into efficiency, loss and leakage that are later expanded further into increase of noise, damage third part, environmental impact and explosion.

![img-2.jpeg](img-2.jpeg)

Fig. 3. Developed FT for failure scenario of a NGRMS

Data provided by industry (ESTRA, 2016) refer to 59 different NGRMSs. The data presents maintenance activity, component of interest, time of maintenance and costs of maintenance including trip costs, manpower costs and materials costs. It is worth noting that the MTTF of each component are also provided by industry based on literature and the calculation of their experts. These values and corresponding failure rate are shown in Table 2.

Table 2
MTTF and Failure rate of critical components of NGRMS'.



![img-3.jpeg](img-3.jpeg)

Fig.4. Developed BN for risk analysis of a NGRMS
Based on reported MTTF and failure rate the probability of failure in a year is calculated. According to Krishnasamy et al. (2005) and in order to consider the randomness of failures events, exponential distribution is adopted for the estimation of maintenance intervals. So the annual probabilities of failure would be achieved by Eq. (3):
$P(t)=1-e^{-\lambda t}$
where $P(t)$ is the annual probability of failure when $t$ is set equal to 8760 hours (a year) and $\lambda$ is the failure rate expressed in failure per hour given by Eq. (4):
$\lambda=\frac{1}{M T T F}$

The developed BN for a NRGMS incorporating the failure of critical components is illustrated in Fig. 5.
![img-4.jpeg](img-4.jpeg)

Fig.5. Developed BN to estimate maintenance interval of critical components

The primary events are linked to four major intermediate events (i.e. reduction group failure, measuring group failure, preheating failure and gas odorization failure) which consequently may lead to system failure. The annual failure probabilities of critical components calculated by Eq. 3 were assigned to root nodes as prior probability. The CPTs of intermediate and leaf nodes represent the contribution factors of root nodes in the intermediate nodes. Based on the succeeding intermediate events, NGRMS is estimated to exhibit a reliability of $97 \%$. The Conditional Probability Table (CPT) of NGRMS risks is then filled using a risk matrix illustrated in Table 3:

# Table 3 

Adopted risk matrix for developing RBM.


(L,M,H,E): Low, Medium, High, Extreme

The risk of operation consisting of three aforementioned levels is integrated into the network. After mapping the possible consequences into the BN, the system results to operate in minor risk with probability of $84 \%$, in major risk with probability of $14 \%$ and in catastrophic risk with probability of $4 \%$.

To generate the posterior probability of the components, the risk level of $100 \%$ safe level (minor risk) was targeted. In the light of new evidence and based on posterior probability, the maintenance interval is calculated using Eq. (5):
$T=-\frac{\ln (1-F(t))}{\lambda}$
where $F(t)$ is the updated probability of failure and $\lambda$ is the previous failure rate estimated by Eq. (4). The posterior probabilities and the maintenance times of each component are reported in following section.

## 4. Results and discussions

Table 4 lists the maintenance intervals of NGRMS' components in the three different scenarios of minor, major and catastrophic risk.

# 4.1. Minor risk level 

The calculations depicted that the most critical components is determined as the pilots with the shortest maintenance interval of 297 days. On the contrary, the most reliable components are the THT tank and the remote control system which have the longest maintenance interval of 444 and 387 days, respectively. The less critical component of reduction group is filter, for which maintenance is required to be performed every 379 days. Maintenance schedule of meter will be optimized with a repair interval of 328 days, around once every 11 months. The THT pipelines must be maintained every 302 days as the third most critical component while the boiler are to be serviced every 340 days. Following these criteria, the most critical group that has to be controlled in a more accurate way is preheating group including pump, boiler and water pipe (second most critical component) with maintenance interval of 346,340 and 298 respectively.

### 4.2. Major risk level

In case that the policies of the system accept and tolerate more risks (major level), the maintenance time can be extended to wider time interval. The repair action is needed for THT tank before 575 days in order to avoid it from major risk. This time interval (575 days) is the longest time for overpassing from minor to major risk, the second and third longest are pressure regulator and THT pipelines, estimated as 480 and 433 days. 17 days delay, in the process of maintenance activities throughout the measuring group (the calculator) can lead to an unexpected change in the risk level of the system from minor risk to major level.

## Table 4

Failure probabilities $\left(\mathrm{P}_{\mathrm{f}}\right)$ and maintenance time $\left(\mathrm{T}_{\text {main }}\right)$ of NGRMS' critical components.



# 4.3. Catastrophic risk level 

The free maintenance time approaching the system into catastrophic risk level can be predicted based on proposed RBM approach (See table 4). As it can be seen form the results, there are some components needing less time in order to overpass from minor to catastrophic risk level. The measuring group with Pressure and temperature gauge (22 days), Meter and the remote controls (44 days) and calculator ( 65 days) are the most critical components in this regards. The longest time to suffer from catastrophic risk level, throughout the system, are related to pressure regulator and THT tank with 966 and 959 days, respectively.

Finally, a clustered column chart is applied to compare assigned maintenance interval across the three risk levels. (see Fig. 6.)
![img-5.jpeg](img-5.jpeg)

Fig. 6. assigned maintenance time interval for all components across the different risk level
Aggregated framework allows engineers and designers to plan an effective maintenance schedule. The proposed maintenance plan has to be followed to minimize failure consequences. Longer

maintenance time may produce major or catastrophic consequences. On the other side adopting shorter maintenance time will increase maintenance efforts and lead to more costs and loss of productivity. Risk profile and maintenance plan has to be updated as soon as new information is known. The methodology could be applied to systems in which high safety is required.

# 5. Conclusions 

This paper presents a novel methodology to optimize the maintenance of gas regulating operation to model the associated risks. By modeling the failure risks, the cost of maintenance and nonproductive time of operation is minimized significantly. The developed RBM methodology estimates the optimum maintenance interval for each component using a Bayesian Network. NGRMS was chosen as a case study to illustrate the methodology and its advantages. This study divides the possible risks in three different categories. By these categories the maintenance time is determined given that a component is overpassing the minor, major or catastrophic level of risk. The most critical components were determined based on their respective times of maintenance. In most of the cases data about MTTF are not directly available or are limited. To provide these data methods such as Maximum Likelihood Estimation (MLE) or Linear Square Estimate (LSE) can be implemented, while to deal with uncertainty and limitation Monte Carlo Simulations could be applied. Further work can also be carried out to study the redundant and stand-by components based on Non-Homogeneous Poisson Process (NHPP) considering correlation modelling between data.

## Acknowledgement

Authors gratefully acknowledge the financial support provided by Estra S.p.A. and the University of Florence.

# 21