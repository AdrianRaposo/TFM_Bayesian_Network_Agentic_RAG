# TUDelft 

## Delft University of Technology

## Calculation of dam risk probability of cascade reservoirs considering risk transmission and superposition

Wang, Te; Li, Zongkun; Ge, Wei; Zhang, Yadong; Jiao, Yutie; Sun, Heqiang; Zhang, Hua

## DOI

10.1016/j.jhydrol.2022.127768

## Publication date

2022

## Document Version

Final published version

## Published in

Journal of Hydrology

## Citation (APA)

Wang, T., Li, Z., Ge, W., Zhang, Y., Jiao, Y., Sun, H., \& Zhang, H. (2022). Calculation of dam risk probability of cascade reservoirs considering risk transmission and superposition. Journal of Hydrology, 609, Article 127768. https://doi.org/10.1016/j.jhydrol.2022.127768

## Important note

To cite this publication, please use the final published version (if applicable).
Please check the document version above.

## Copyright

Other than for strictly personal use, it is not permitted to download, forward or distribute the text or part of it, without the consent of the author(s) and/or copyright holder(s), unless the work is under an open content license such as Creative Commons.

## Takedown policy

Please contact us and provide details if you believe this document breaches copyrights.
We will remove access to the work immediately and investigate your claim.

# Green Open Access added to TU Delft Institutional Repository 

'You share, we take care!' - Taverne project
https://www.openaccess.nl/en/you-share-we-take-care

Otherwise as indicated in the copyright section: the publisher is the copyright holder of this work and the author uses the Dutch legislation to make this work public.

# Calculation of dam risk probability of cascade reservoirs considering risk transmission and superposition 

Te Wang ${ }^{\mathrm{a}}$, Zongkun $\mathrm{Li}^{\mathrm{a}}$, Wei $\mathrm{Ge}^{\mathrm{a}, \mathrm{b}, *}$, Yadong Zhang ${ }^{\mathrm{a}}$, Yutie Jiao ${ }^{\mathrm{a}}$, Heqiang Sun ${ }^{\mathrm{a}}$, Hua Zhang ${ }^{\mathrm{a}}$<br>${ }^{a}$ School of Water Conservancy Engineering, Zhengzhou University, Zhengzhou 450001, PR China<br>${ }^{\mathrm{b}}$ Safety and Security Science Group (S3G), Faculty of Technology, Policy and Management, Delft University of Technology, Delft 2826 CD, The Netherlands

## A R T I C L E I N F O

Keywords:
Cascade reservoirs
Risk transmission
Risk superposition
Dam break
Probability

## A B S T R A C T

Because of the risk transmission and superposition among dams in cascade reservoirs, the analysis and probability calculation of dam risk become more complex compared with a single reservoir. By analyzing the main risk sources and actionmechanisms, the disaster-causing factors, disaster-transmitting body and disaster-bearing body in the cascade reservoirs system were determined. By defining the influence coefficient $(I C)$ to express the transmission and superposition degree of dam risk among cascade reservoirs, dam risk was divided into two parts: own risk (OR) and additional risk (AR). On this basis, the relevant concepts and equations for the calculation of the dam risk probability of cascade reservoirs were proposed. The numerical simulation was carried out to quantify the $I C$, and a Bayesian network analysis model was constructed to calculate the $O R$. Finally, taking five cascade reservoir dams in the Dadu River basin as examples, the value of their ORs, ARs and risk probabilities were calculated, and thereafter the weakest cascade, controlling cascade and general cascade in the system were divided. The proposed methodology realizes an effective connection with the dam risk calculation method of a single reservoir, which can provide a reference for the risk assessment and management of cascade reservoirs in the basin.

## 1. Introduction

The cascade reservoir group refers to a complex system comprising multiple reservoirs in the same basin, which has obvious advantages, such as full utilization of water flow, rolling project development and coordinated power dispatching (Ardeshirtanha and Sharafati, 2020; Latrubesse et al., 2017). It has become a major livelihood project with strategic and overall impact on social and economic development (Zhou et al., 2018). At present, cascade reservoirs account for $48 \%$ of China's built reservoir projects and $50 \%$ of the reservoir projects under construction (Hu et al., 2020). In the next 20 years, the main rivers in China, such as Jinsha River, Yalong River, Dadu River and Lancang River, will continue to carry out cascade development and construction of river basins, forming more than 100 cascade reservoirs (including tributaries), that are successive. In recent years, aging dams and levees, in combination with an increasing frequency of climate extremes pose an unprecedented risk to communities around the world. (Larruari and Lall 2020). Compared with ordinary reservoirs, the dam risk in cascade reservoirs has transmission and superposition effects. One of the cascade dam breaks can easily lead to successive dam breaks in downstream
reservoirs, resulting in serious losses. In August 2014, the Ludian earthquake in China formed a barrier lake, which flooded Hongshiyan Hydropower Station in the main stream of the Niulan River and posed a serious threat to the safety of two downstream cascade hydropower stations (Zhou et al., 2015d). In May 2020, heavy rainfall in Michigan led to the collapse of two cascade dams, the Edenville Dam and Sanford Dam, resulting in the emergency evacuation of more than 10,000 residents and the destruction of infrastructure downstream (Mehta et al., 2020). With the rolling development of cascade reservoirs and the enhancement of public self-protection awareness, the risk problem of cascade reservoirs has become a public safety problem. It is critical to carry out the risk analysis to improve the safety of the basin.

With the transformation of dam management mode from traditional safety management to risk management, the risk analysis theory and technology of a single reservoir dam are becoming increasingly mature (Ge et al., 2020a; Ge et al., 2020b; Ge et al., 2021; Li et al., 2018b). Kravits et al. (2021) presented a machine learning dam hazard potential classification model that demonstrated the utility of this approach for dams in Massachusetts, United States. Larruari and Lall (2020) proposed a framework to assess the probability and financial consequences of dam

[^0]
[^0]:    * Corresponding author.

    E-mail address: gewei@zzu.edu.cn (W. Ge).
    https://doi.org/10.1016/j.jhydrol.2022.127768
    Received 11 November 2021; Received in revised form 13 March 2022; Accepted 24 March 2022
    Available online 29 March 2022
    0022-1694/© 2022 Elsevier B.V. All rights reserved.

failures, which provided an effective solution for risk analysis under the action of dam aging and climate trends. Assaad and El-Adaway (2020) developed a computational data-driven asset management system to evaluate and predict the deterioration conditions of a bridge deck. Feinberg et al. (2016) provided an overview of Reclamation's Consequences Estimation Methodology (RCEM) for estimating life loss due to dam failure. Luo et al. (2009) adopted the improved Graham method to estimate the life loss of dam failure.

By comparison, it is rare to comprehensively analyze and evaluate the dam risk of cascade reservoirs as a whole. Professor David Bowles put forward the concept of reservoir group risk analysis for the first time (David et al., 1999). In recent years, some scholars have also carried out active exploration in this field and have achieved some valuable results. Zhou et al. (2015a) explored the reasons for failure, mechanism and chain failure mode of cascade dams, and the results showed that overtopping was the main failure mechanism. Dewals et al. (2008) combined the one-dimensional and two-dimensional calculation methods of break flood into a series of models for dam break calculation of reservoir groups, which effectively improved the accuracy of successive break flood prediction. Takayama et al. (2021) studied the chain failure of landslide dams through channel experiments, and the results were significant in predicting the flood flow caused by successive dam failures. Riha et al. (2020) carried out dam break simulation for three cascade reservoirs and analyzed the attenuation effect of dam break peak discharge. Combining the hydraulic characteristics of reservoirs with flood routing simulation, Hu et al. (2020) carried out numerical simulations and risk analysis of dam failure of cascade reservoirs. Zhang et al. (2016) considered the role of upstream dam break flood in reservoir overtopping risk analysis, and proposed a reservoir overtopping risk analysis model based on a a right-angle trapezoidal fuzzy number. Chen et al. (2017) calculated the failure probability of earth rock dam slope considering the joint action of earthquakes and upstream cascade dam break floods. Lin and Chen (2018) and Li et al. (2018a); Li and Liang (2016) analyzed the key risk factors of reservoir overtopping and established a Bayesian network $(B N)$ risk analysis model of overtopping of cascade reservoirs.

Despite the fact that the above efforts have been made for risk calculation and assessment, there is still a lack of quantitative analysis on the risk transmission and superposition mechanism among the dams of cascade reservoirs. Moreover, most of them are limited to the risk analysis and calculation of unilateral factors (such as floods), which fail to consider the failure mode and actual risk status of cascade dams under the coupling action of multiple factors (Zhang et al., 2016; Zhou et al., 2018). Risk probability is usually used to describe the probability of accidents or risk events (Liu et al., 2020; Schwabe et al., 2015; Su et al., 2009). Considering that the risks faced by a single reservoir dam are also applicable to cascade reservoirs and its risk calculation method has been widely used, the calculation method of risk probability of cascade reservoir dams should be connected with the calculation method for a single reservoir dam to form a unified system.

Therefore, this paper divided the total risk of a cascade dam into two parts: $O R$ and $A R$. Based on the risk theory and uncertainty analysis method, an influence coefficient $(I C)$ was defined and quantified to reflect the risk transmission and superposition degree among cascade dams, and a Bayesian network analysis model was constructed to calculate the $O R$. Ultimately, the formulas and methods for calculating the dam risk probability of cascaded reservoirs were proposed, which realizes the transition of dam risk probability method from single reservoir to cascade reservoirs. Through a case study of five cascade reservoirs, the feasibility and effectiveness of the proposed models and methods were verified. The research is not only a supplement and improvement of reservoir risk management theory, but also the support for risk assessment and control technology of cascade reservoirs in the basin.

## 2. Background

### 2.1. Risk identification and uncertainty analysis of cascade reservoirs

Geographically, cascade reservoirs are mainly concentrated in high mountains and valleys, with engineering characteristics such as high altitude, high seismic intensity, high slope and extremely complex geological conditions (Zhou et al., 2018). In terms of dam type, earth rock dams and rockfill dams can adapt to various topographic, geological and climatic conditions owing to their convenient materials. Arch dams have a strong overload capacity and are suitable for construction in high mountains and valleys. These characteristics make the above dam types more common in cascade reservoir groups. According to the statistics of dam failures in China, earth rock dams account for more than $95 \%$ of the total number of dam failures, becoming the main dam failure type (Li et al., 2019; Zhou et al., 2018). Therefore, the risk analysis of cascade reservoirs in this study considers earth rock dams as the main object of study. Considering the complexity of the service environment of the cascade reservoir group dams and the characteristics of the earth rock dam breaking in case of overtopping (Li et al., 2018a; Li and Liang, 2016; Lin and Chen, 2018), the flood, strong earthquake and landslide are regarded as the main sources of natural risks tothe cascade reservoir group dams, and the overtopping and dam slope instability are regarded as the main failure forms.

Flood. According to statistics, overtopping caused by floods is the main failure mode of reservoir dams, accounting for more than $50 \%$ (Li et al., 2018a; Li and Liang, 2016; Lin and Chen, 2018). Floods in cascade reservoirs can be divided into natural flood and upstream dam-break flood: natural floods were generated by natural rainfall and interval confluence; upstream dam-break flood refers to the dam-break flood transmitted from the upstream cascade, which often directly evolves to the downstream reservoir through the river canyon, resulting in the surge of the downstream reservoir water level or even overtopping. Therefore, dam-break flood is also the main carrier of risk transmission among cascade reservoirs. The uncertainty of natural flood risk analysis is mainly the hydrological factors, including the possibility of different scale floods (flood frequency) and the uncertainty of reservoir operating water level, while the uncertainty of the upstream dam-break flood risk analysis is mainly related to the dam height, operating water level, river channel parameters and other factors of cascade reservoirs (Hu et al., 2020; Zhang et al., 2016).

Earthquake. Earthquakes are the main factors inducing landslides. The strong action of earthquakes and the repeated vibration of aftershocks, destroy the internal structure of the slope earth rock, resulting in the overall landslide and instability. In cascade reservoirs, when a strong earthquake occurs, the damage of landslide and collapse induced by the earthquake is greater than the loss directly caused by the earthquake. Therefore, it is essential to analyze the seismic risk of reservoir dams, in particular, high dams. The uncertainty of seismic risk analysis is mainly due to the uncertainty of the occurrence possibility and intensity of earthquakes (Chen et al., 2017; Li and Liang, 2016).

Landslide. The most basic topographic and geomorphological features of the area where the terrace reservoir group is located are numerous mountains, steep mountains, loose soil structure, and the extensive existence of basic conditions for landslides to occur. The fluctuation of the reservoir water level caused by the joint operation of cascade reservoirs has a significant impact on the hydrogeological conditions and internal balance relationship in rock and soil mass, which can reduce the anti-sliding coefficient on the sliding surface and lead to instability (Chen et al., 2017). In terms of the location of the reservoir landslide, it can be divided into bank and dam landslides: bank landslide refers to the sliding instability of the reservoir bank, which can block the river channel to form a weir plug or produce surge, resulting in an overtopping accident; the dam landslide refers to the instability of the dam slope. According to the statistics of engineering practice, the ratio of upstream landslide dam break to downstream landslide dam break is

approximately 1:9 (Luo et al., 2014). The uncertainty of reservoir landslide risk analysis is due to the uncertainty of the reservoir water level and parameters of the soil material.

In addition to the above factors, dam leakage, improper dispatching and some other factors, are added uncertain risks, that may occur in engineering practice (Li et al., 2019).

### 2.2. Analysis of risk action mechanism and division of cascade reservoirs system

From the analysis above, it can be seen that there is a correlation among various risk sources, which induce dam break and act on the reservoir together. According to the disaster theory (Li et al., 2018b), natural floods, earthquakes and landslides are the main disaster-causing factors in cascade reservoir systems. Dam-break flood, as the carrier of risk transmission and superposition among the cascade units in the system, is not only the disaster-causing factor of the downstream cascade, but also the disaster-transmitting body in the cascade system. Each cascade reservoir dam is the direct risk bearing body, that is, the object directly affected by the risk accidents, which is defined as the disaster-bearing body in the system.

The break of the upstream cascade will have varying degrees of impact on the downstream cascades, with some probability of causing successive breaks (Chen et al., 2018; Zhang et al., 2016). Therefore, the risk analysis of cascade reservoirs can be based on the risk assessment of a single reservoir dam, but the risk transmission and superposition effect among cascades should be considered.

To reduce the complexity of risk analysis and probability calculation of cascade reservoirs, according to the source of risk, the total risk of a cascade dam in cascade reservoirs is divided into its own risk (*OR*) and the additional risk (*AR*). *OR* refers to the failure probability of a cascade dam under its own risk factors without considering the impact of upstream cascade, which corresponds to each disaster-causing factor in the cascade system; *AR* is transmitted from the upstream cascade through the dam-break flood, which depends on the degree of risk transmission and superposition and corresponds to the disaster transmission body in the cascade system. This proposed risk classification method can effectively connect the risk assessment method of cascade reservoir dams with that of a single reservoir dam. On the one hand, the risk of cascade reservoir dams can be calculated according to the traditional risk probability calculation method of a single reservoir dam (Ge et al., 2020a; Ge et al., 2020b; Ge et al., 2021; Li et al., 2019), its risk analysis is no longer limited to the unilateral risk source of flood, but can more comprehensively consider the impact of various risk factors. On the other hand, the source of dam risk of each cascade reservoir becomes clear and intuitive, which lays a foundation for the quantification of risk

![img-0.jpeg](img-0.jpeg)

![img-1.jpeg](img-1.jpeg)

(b) Risk division of cascade reservoir dams.

**Fig. 1.** Risk analysis of cascade reservoir dams.

correlation. The risk identification results for the cascade reservoirs are shown in Fig. 1.

As shown in Fig. 1, the AR of M includes the conditional probability of N failing and the conditional probability of K failing given that M fails, while the AR of N is the conditional probability of K failing given that N fails.

## 3. Methods

### 3.1. Quantitative model of risk transmission and superposition effect

### 3.1.1. Expression of dam risk relevance of cascade reservoir groups

The break of each dam in cascade reservoirs will have varying degrees of impact on the entire basin. Thus, the cascade reservoirs can be regarded as a series system comprising several single reservoirs. Most of the existing studies reflect the possibility of risk transmission of adjacent cascades from a qualitative point of view (Zhang et al., 2016), without considering the uncertainty of water level in front of dams, which has certain limitations in practical application. In particular, when the difference between the flood regulation storage capacity of the downstream cascade and the upstream adjacent cascade storage capacity is not obvious, it is difficult to determine the possibility of their successive break.

The dam risk correlation in the cascade reservoir system is mainly the risk transmission and superposition effect among the cascade dams, which is manifested in the change in the dam break probability of the downstream cascade reservoirs caused by the upstream cascade reservoirs (Li and Liang, 2016; Lin and Chen, 2018). To more clearly reflect the degree of risk transmission and superposition, the IC is defined here to represent the dam break probability of the targeted cascade under the condition that the upstream cascade dam breaks, that is, the conditional probability of successive dam break of the adjacent upstream and downstream cascades. The value range of IC is [0,1].

As the disaster transmission body in the cascade reservoir group system, a break-flood is the carrier of risk transmission and superposition among different cascade reservoirs. Regardless of the upstream dam-break scenario, the dam failure flood must act on the downstream dams. Therefore, the risk transmission and superposition effect can be quantified by analyzing the impact of upstream dam-break floods on downstream cascade dams. Most reservoir dams, in particular, earth rock dams, are generally considered to break in the case of overtopping (Du et al., 2015; Zhou et al., 2015b; Zhou et al., 2015c). Therefore, the downstream cascade dam overtopping under the action of an upstream dam-break flood can be directly used as the basis for its break. The calculation of the IC in this study is also based on the assumption that the cascade dam will break if overtopping occurs under the action of an upstream dam break flood. In practical engineering, the water level in front of the cascade dam, formed by the upstream dam-break flood, is affected by multiple factors with great uncertainty. Therefore, IC is determined by sampling different initial storage levels combinations and taking the frequency of uncertain events as the probability, which is based on the dam break simulation and mathematical statistics, as shown in Fig. 2.

### 3.1.2. Dam break simulation and flood routing models

A dam-break simulation, which includes calculation models and empirical formulas, is carried out to obtain the maximum discharge and the dam break flood hydrograph (Mahdizadeh et al., 2012). Dam-break calculation models, such as the MIKE, HEC-RAS, DSS-WISE, and DBIWHR models are widely used (Aggarwal et al., 2016; Larruari and Lall 2020; Pilotti et al., 2020; Wang et al., 2016). In these models, the initial size, final size and development process of the breach must be set to ensure accurate results. The dam-break flood hydrograph is generalized by a quartic parabola (Li and Liang, 2016; Lin and Chen, 2018), which is related to the maximum discharge QM, water storage capacity w of the upstream reservoir, inflow discharge Q0 during dam break and emptying time t of dam break storage capacity.

The dam break simulation of cascade reservoirs mainly focuses on the maximum discharge and flood flow processes under each successive break condition. Therefore, the simplified equations can be used for relevant calculations, which are simple, fast, and can meet a certain accuracy. The Xierenzhi Formula has wide application conditions with high calculation accuracy (Li et al., 2018a; Li and Liang, 2016; Lin and Chen, 2018), as shown in Eq. (1).

$$
Q m=\lambda B 0 g^{0.5} H 0^{1.5}
$$

where Qm is the maximum discharge, λ is the discharge coefficient; B0 is the width of the valley at the dam site; g is the gravitational acceleration, which can be taken as 9.8 m/s2; H0 is the upstream water depth before dam break.

In the cascade reservoir system, the dam-break flood enters the river channel and flows to the downstream reservoir after the upstream dam breaks. The flood routing model aims to deduce and describe the change process of hydraulic factors in the river channel over time, such as the discharge and water level of the flood, in order to obtain the inflow flood characteristics of the downstream reservoir (Perumal et al., 2007). According to the hydraulic theory, the natural river channel is often regarded as one-dimensional flow and the description of river flow is mainly based on the Saint Venant equations (Goutal and Sainte-Marie, 2011; Liu et al., 2015). As shown in Eqs. (2) and (3).

$$
\frac{\partial A}{\partial t}+\frac{\partial Q}{\partial x}=0
$$

$$
\frac{\partial}{\partial t}\left(\frac{Q}{A}\right)+\frac{\partial}{\partial x}\left(\frac{\beta Q^{2}}{2A^{2}}\right)+\dot{x} \frac{\partial h}{\partial x}+g(Sf - S0)=0
$$

where A is the cross-sectional area of water discharge, t is the time step, Q is the flow, x is the spatial coordinate, H is the water depth, S0 is the river bottom gradient, Sf is the resistance gradient (gradient of head loss along the way), K is the flow modulus.

![img-2.jpeg](img-2.jpeg)

Fig. 2. Calculation flow of IC.

#### *3.1.3. Determination of the IC*

The water level of the reservoir has great uncertainty during the operation period, which leads to the uncertainty of the water level in front of the downstream cascade dam formed by the upstream dam-break flood. In order to reasonably quantify the value of *IC*, the Monte Carlo (MC) method widely used for uncertainty analysis is selected in this study for random sampling, which has the advantages of high precision, and is more effective for nonlinear, different distributions and related systems (Sharafati and Azamathulla, 2018).

The following process is proposed to calculate the value of *IC*: (1) according to the measured data during the operation period, the water level distribution characteristics of the upstream cascade reservoirs are counted; (2) according to the water level distribution characteristics in front of the upstream cascade dam, *N* times of random sampling are carried out through the MC method and the corresponding dam break flow hydrograph is obtained by dam break simulation, so as to generate *N* types of inflow floods to the downstream cascade reservoir; (3) the water levels in front of the downstream cascade dam are obtained by storage routing. Accordingly, the value of *n* is determined, indicating the number of times that the water level exceeds the dam height. Finally, the conditional probability that successive breaks of upstream and downstream cascades are determined as *IC* = *n*/N, as shown in Fig. 2.

The proposed method considers the uncertainty of reservoir water level and dam break flood during reservoir operation, and the analysis results can effectively reflect and quantify the degree of risk transmission and superposition among cascade dams. Owing to the complexity of discharge analysis of cascade reservoirs, which is affected by operation rules and other factors, the discharge of water release facilities was not considered in this study.

#### *3.2. Calculation of AR and the dam risk probability of cascade reservoirs based on influence coefficient*

The *AR* of the cascade reservoir dam is transmitted from the upstream cascade and its value depends on two factors: the dam break probability of the upstream cascade and the conditional probability that the upstream dam break causes successive break, that is, the *IC*.

Dam *K*, at the most downstream location in Fig. 1, was taken as the object of study. In addition to the *OR*, this cascade dam bears *AR* from dams *M* and *N*. Therefore, the risk probability calculation method for dam *K* is as follows:

$$PK = OR + AR = OR + PNK + PMNK \tag{4}$$

where *PNK* represents the probability that dam *N* break leads to the successive break of dam *K*, and *PMNK* is the probability that dam *M* break leads to the successive failure of dams *N* and *K*.

Because the *IC* represents the conditional probability of the targeted dam break caused by its upstream dam break, *PNK* and *PMNK* can be further deduced, as shown in Eq. (5).

$$\begin{cases} PNK = PN \times INK \\ PMNK = PM \times IMN \times IMNK \end{cases} \tag{5}$$

where *PN* and *PM* are the total risk probabilities of dam *N* and dam *M* in the cascade reservoir system, respectively; their calculation idea of them is the same as *PK*, which can be obtained by iterative operation using Eqs. (4) and (5); *INK*, *IMN* and *IMNK* are the *ICs*, which, respectively, represent the conditional probability of *N-K* successive break caused by dam *N*, the conditional probability of *M-N* successive break caused by dam *M* and the conditional probability of *M-N-K* successive failure caused by *M-N* successive break.

By substituting Eq. (5) into Eq. (4), the total risk probability of dam *K* in the cascade reservoir system is obtained, as shown in Eq. (6).

$$PK = OR + AR = OR + PNINK + PMIMNINK \tag{6}$$

Moreover, if there is a concrete dam or arch dam in the upstream cascade, in addition to the successive break scenario, there may be a case where the concrete dam or arch dam in the middle cascade does not break but the downstream earth rock dam breaks. Assuming that dam *N* in Fig. 1 is an arch dam, when calculating the risk probability of downstream dam *K*, it is only necessary to replace *IMN*/IMNK in Eq. (6) with the influence coefficient *IMK*, which represents the conditional probability of dam *K* break in this case.

In addition to their *ORs*, dams *M* and *N* in Fig. 1 create *ARs* to their downstream dams. According to the characteristics of the series system, the calculation method above is applied to the entire cascade reservoir system to calculate the total risk probability Σ*P*, as shown in Eq. (7).

$$\begin{aligned}
\sum P &= PM + PN + PK = \sum OR + \sum AR \\
&= ORM + ORN + ORK + PMIMN + PMIMNIMNK + PNINK
\end{aligned} \tag{7}$$

where *PM*, *PN*, and *PK* are the risk probabilities of dams *M*, *N* and *K* in the cascade reservoir system, respectively, and *ORM*, *ORN*, and *ORK* are the *ORs* of the dams, respectively.

#### *3.3. Calculation of OR based on Bayesian network*

According to the division of the cascade reservoir system above, the *OR* of cascade dam refers to the risk probability without considering the effect of upstream dam-break flood, which can be calculated based on the traditional dam risk calculation methods. In fact, the *OR* is the basis for calculating *AR*, which should be estimated first. Mathematical models commonly used for dam risk probability calculation include event trees, fault trees, and *BNs*. (Li et al., 2019; Peng and Zhang, 2012; Wu et al., 2020) In view of the great uncertainty of the risk of cascade reservoir group dams, the selected risk probability calculation model needs to solve two basic problems: one is to meet the needs of uncertainty analysis of the occurrence possibility and combination mode of disaster-causing factors; the other is to reflect the correlation between disaster-causing factors and risk events, as well as their impact on dam break. Therefore, an *OR* calculation model based on *BN* is constructed for reference.

#### *3.3.1. Bayesian network*

A *BN*, also known as a belief network, is a directed acyclic graph that expresses and calculates the probability relationship between random variables (Li et al., 2019), as shown in Fig. 3.

The Bayesian formula and total probability formula are the theoretical bases of the *BN*, as shown in Eqs. (8) and (9):

$$P(B|A) = \frac{P(A|B)P(B)}{P(A)}$$

$$P(A) = \sum_i P(A|Bi)P(Bi) \tag{9}$$

where *P(B)* is the a priori probability of event *B*, without considering any other factors (Li et al., 2019; Peng and Zhang, 2012); *P(B|A)* is the probability of event *B* under the condition that event *A* has occurred, also known as a posteriori probability; *P(A|B)* is the likelihood ratio and *i* is the number of events.

The operation result of a *BN* is the joint probability distribution of all variables in the studied problem, which is the probability value under

![img-3.jpeg](img-3.jpeg)

**Fig. 3.** Simple Bayesian network.

the influence of all factors. For example, the joint probability distribution of the simple Bayesian network in Fig. 3 is as follows:

$$P(A, B, C) = P(C|A, B)P(A, B) = P(C|A, B)P(A)P(B) \tag{10}$$

According to the risk identification results and the action relationship of risk factors of the cascade reservoir system in Section 2.1, the *BN* model for *OR* calculation of cascade reservoir dam is constructed, as shown in Fig. 4. The probability calculation formula of node "Dam break" is shown in Eq. (11).

$$P(O, L, D) = P(D|O, L)P(O, L) = P(D|O, L)P(O)P(L) \tag{11}$$

where *O, L*, and *D* represent the nodes "Overtopping", "Landslide of dam slope", and "Dam break", respectively; *P(O, L, D)* and *P(O, L)* are joint probabilities; *P(D|O, L)* are the conditional probabilities.

### 3.3.2. Determination of node probability value

The a priori probability of "Natural flood" is generally determined by hydrological statistics based on the measured data (Cai et al., 2019; Larruari and Lall 2020; Lin and Chen, 2018). According to the flood scale, this node in Fig. 4 is divided into several state intervals as "below design flood", "between design flood and check flood", and "beyond check flood", to facilitate the setting of node states in *BN* for subsequent analysis and calculation. Each state corresponds to an a priori probability. Similarly, the node state of "Strong earthquake" is set as "occurred" and "not occurred". According to the earthquake intensity data, the probability of exceeding this earthquake intensity in a reference period is taken as the a priori probability (Li and Liang, 2016).

In addition to the nodes mentioned above, other nodes were all determined the corresponding conditional probability. The numerical simulation was also based on the MC method.

The landslide risk events in Fig. 4 include "Landslide of reservoir bank" and "Landslide of dam slope", of which the parent nodes are "Natural flood" and "Strong earthquake". Natural floods of different scales will form different reservoir levels, the slope safety factors under various conditions are calculated respectively. Considering the variation characteristics of materials, the pseudo static method (Li and Liang, 2016) is used to simulate the impact of seismic load on reservoir bank landslide and dam slope instability, thereafter the critical slip surface corresponding to the minimum safety factor is searched based on the simplified Bishop method and the optimization method (Mahdi and Merabtene, 2010), in order to obtain different safety factor *K*, which combines the action of reservoir water level, earthquake and material parameters. When the dam body forms stable seepage at a certain water level, the circular arc sliding slice and calculation formula for calculating *K* by simplified Bishop method are shown in Fig. 5 and Eq. (12).

$$K = \frac{\sum \left\{ \left[ (W \pm V) \text{sec}\alpha - \text{abse}\alpha \right] \text{tan}\varphi + \text{cbse}\alpha \right\}_{1 \le \frac{1}{1 \le \frac{1}{2 \text{sec}}\text{sec}}}\sum \left[ (W \pm V) \text{sin}\alpha + \frac{M_C}{g} \right] \tag{12}$$

where *W* is the weight of the soil strip (KN), *V* is the vertical seismic inertia force (KN), *µ* is the pore pressure acting on the ground of the soil strip (KN/M), *c* and *φ* are the cohesion (kPa) and internal friction angle (°) of the bottom surface of the soil strip, respectively; and *M<sub>C</sub>* is the moment of horizontal seismic inertia force to the center of the circle (KN·m).

Previous studies have shown that the cohesion *φ* and friction coefficient tan *φ* usually follow an extreme value type I distribution and lognormal distribution (Chen et al., 2012; Li and Liang, 2016). By substituting the parameter distribution of each variable into Eq. (12), the random distribution of the safety factor *K* is calculated, and thereafter the conditional probability of "Landslide of reservoir bank" and "Landslide of dam slope" are obtained by counting the times that *K* is less than the allowable value.

The reservoir bank landslide near the upstream of the dam will easily lead to surge in front of the dam, resulting in overtopping. Therefore, the occurrence of overtopping under the combination of "Natural flood" and "Reservoir bank landslide" is closely related to the surge height and the original reservoir water level. The calculation of the water inflow velocity of a landslide mass is the basis for estimating its surge height, which is effectively solved by the formula recommended by the American Society of Civil Engineers (Cao et al., 2011):

$$V = \sqrt{2gh} \times \sqrt{1 - \text{cot}\alpha \times \text{tan}\varphi - \frac{cL}{\text{Mg}\text{sin}\alpha}} \tag{13}$$

The equations proposed by Pan Jiazheng were used for the surge propagation attenuation analysis and climbing calculation of landslide mass (Li and Liang, 2016), as shown in Eqs. (14) and (15), respectively:

$$\frac{\eta_0}{h} = (1.17 - 0.00189\beta) \frac{V}{\sqrt{gh}} \tag{14}$$

$$\eta_x = \frac{\eta_0}{\pi} \sum_{n=3/2,3...} (1 + k\text{cost}\theta n) k^{(n-1)}$$

$$\times \ln\left[\frac{\sqrt{1 + \left(\frac{nB}{s0} \right) - L}\right)^2 - 1}{\left(\frac{s0}{s0} \right) - L} \right] \sqrt{1 + \left(\frac{nB}{s0} \right) - L} - 1 \tag{15}$$

where *η<sub>0</sub>* is the initial surge height formed after the landslide mass enters the water (m), *h* is the distance from the center of gravity of the landslide mass to the water surface (m), *β* is the water inflow angle (°), *η<sub>x</sub>* is the surge height formed by the landslide on the reservoir bank in front of the dam (m), *K* is the wave reflection coefficient (*K≈1*), *L* is the length of the landslide along the river bank (m), and *B* is the average width of the reservoir water surface (m), *x<sub>0</sub>* is the distance from the calculation point to the landslide (m), and *θ* is the inclination angle (°), tanθn = *x<sub>00</sub>*·

According to the parameter distribution of the variables in the equations above, a random distribution of *η<sub>x</sub>* is obtained by the MC simulation method. By superposing *η<sub>x</sub>* with the reservoir water level formed by natural flood, the random distribution of surge elevation in front of the dam is obtained, and then the frequency at which it exceeds the dam crest elevation is taken as the value of conditional probability of overtopping.

It is undeniable that the age of the dam and climate change will also affect the probability of dam risk. The former is reflected in the change in material parameters and properties (Li et al., 2019), and the latter is reflected in the changes of external factors, such as flood event recurrence (Larruari and Lall 2020). According to the division concept of this study, these factors mainly cause changes in their *OR*. Therefore, the

![img-4.jpeg](img-4.jpeg)

**Fig. 5.** Schematic diagram of circular arc sliding strip.

Basic concept and model proposed in this study are still suitable for analyzing the risk calculation under age and climate change, although the specific calculation is more complex. Likewise, the risk events that impact a dam that weaken its structure but do not cause a full dam break will increase its *OR*, which indirectly leads to an increase in the total risk probability.

In summary, the flow of the calculation of dam risk probability of cascade reservoirs is shown in Fig. 6.

# **4. Results**

## *4.1. Project overview*

Dadu River is one of the important tributaries in the upper reaches of the Yangtze River. A total of 24 cascade reservoirs are planned to be built in the main stream, with a total storage capacity of more than 16.5 billion m³, a drop of 2750 m and an installed capacity of 25000 MW (Cai et al., 2019; Zhou et al., 2018). Xiaerga, Shuangjiangkou, and Pubugou are the leading reservoirs of the planned river reach and the controlling reservoirs in the upper and middle reaches respectively. Geological disasters are mainly landslides and debris flows. Historically, several geological disasters have blocked this river (Chen et al., 2018).

Five cascade reservoirs connected to Xiaerxia, Bala, Dawei, Busigou, and Shuangjiangkou in the upper reaches of the basin were selected as the objects of study for the dam risk probability calculation. Their geographical locations and the parameter datas of the cascade reservoirs are shown in Fig. 7 and Table 1, respectively.

## *4.2. Calculation of OR*

Taking the concrete face rockfill dam of Shuangjiangkou Reservoir as an example, its *OR* of a single reservoir is calculated. According to the Hydrological data (Li and Liang, 2016), the "natural flood" node in Fig. 4 is divided into three states: "below design flood (A)", "between design flood and check flood (B)" and "beyond check flood (C)", and the corresponding a priori probabilities are 0.999, 0.0009, and 0.0001, respectively. The basic earthquake intensity in the dam site area is VII and the peak acceleration of bedrock with an exceedance probability of 2% in 100 years of the design reference period is a = 0.2 g, that is, the prior probability of strong earthquakes above this intensity is 0.02. A landslide mass was set on the reservoir bank 3 km upstream from the dam site, and the soil parameters were determined, in a previous study (Li and Liang, 2016). The statistics of the material index parameters are listed in Table 2.

According to the method for determining the node probability value in Section 3.3.2 above, the most dangerous slip arc surface of rock and soil mass under the corresponding reservoir water level is determined (using SLOPE software). Thereafter, 10,000 MC random simulations were programmed using MATLAB to calculate the conditional probability value of the corresponding node. After input into the *BN* in Fig. 4, the probability value of each cascade reservoir risk event and its *OR* were deduced, as shown in Tables 3 and 4. The calculation process was realized by GeNie, a software specially used for *BN* modeling and calculation (Li et al., 2019).

## *4.3. Determination of IC*

According to the comparison of the storage capacity of the five cascade reservoirs in Table 1, it can be inferred that if the Xiaerga Reservoir dam breaks, the dam-break flood will cause overtopping in the four downstream reservoirs, so the corresponding *IC*s can be directly taken as 1. For other cascade dams, the *IC*s are calculated one by one according to the method described in Section 3.1. Two dam break scenarios were selected as examples, in which the reservoir water level conditions were set to the normal pool levels.

![img-5.jpeg](img-5.jpeg)

**Fig. 6.** Calculation of dam risk probability of cascade reservoirs.

![img-6.jpeg](img-6.jpeg)

**Fig. 7.** Geographical location of the cascade reservoirs.

**Table 1** Engineering parameters of the cascade reservoirs.


Scenario I was set as, the dam of Dawei Reservoir breaks alone. After dam break simulation and flood regulation routing, it is concluded that the maximum water level in front of the Busigou dam is approximately 2614 m, indicating that this dam-break scenario will lead to overtopping in Busigou Reservoir; similarly, Scenario II was set to reflect the successive break of Busigou caused by the Dawei dam break under the normal pool level, thereafter the successive flood is simulated and the water level in front of the dam formed in Shuangjiangkou Reservoir is about 2504.2 m, indicating that the successive failure flood under this scenario will not lead to overtopping in the Shuangjiangkou Reservoir. The corresponding hydrograph of the dam-break flood is shown in Fig. 8.

The previous research shows that the water level in front of the dam during the operation period of the reservoir generally follows the normal distribution and is mostly below the normal pool level (Li and Liang, 2016). If the detailed distribution of the water level can be obtained by measurement, the result will be more reliable. It was set that the water levels in front of the dam during the operation period of the Dawei, Pusigou and Shuangjiangkou reservoirs follow the normal distribution of (2685, 0.8), (2599, 1.1) and (2498, 1.8), respectively. The former in brackets referred to the mean, and the latter was the standard deviation, respectively. 10,000 groups of reservoir water level combinations were sampled in MATLAB, and all possible dam-break floods for each of the five reservoirs were considered. Dam-break flood simulation and flood regulation routing were carried out to obtain the random distribution of water level in front of the downstream cascade dam after superimposing the upstream dam break flood, as shown in Fig. 9.

By repeating the above process, the overtopping times under

Table 3 Condition probability values of risk events of Shuangjiangkou Reservoir dam.


where N refers to Not Occur, O refers to Occur.

Different dam-break scenarios can be obtained, and the corresponding ICs can be determined. Because the difference in storage capacity of the middle three cascades in this project case is not obvious, there are many dam-break scenarios with ICs of 0 or 1. The sampling simulation and calculation results of the ICs are shown in Table 5.

### 4.4. Calculation of dam risk probability of cascade reservoirs

Combined with the calculation results of OR and I of the cascade reservoir dams under each dam break scenario, the AR and the risk probabilities of the cascade reservoir dams under the risk transmission and superposition effect are calculated according to Eq. (6). Accordingly, the total risk the cascade reservoirs can be calculated using Eq. (7). The results are presented in Table 6 and Fig. 10.

## 5. Discussion

It can be seen from Table 6 that the ORs of Xiaerga Reservoir and Shuangjiangkou Reservoir are less than those of the other three reservoirs. This is because they have a larger storage capacity and the space for flood storage and detention is relatively sufficient. In addition, according to the current reservoir classification standards of China (Ge et al., 2020a), both belong to the large (1) type, with higher corresponding fortification standards and stronger ability to resist extraordinary floods and earthquakes. In this paper, it is assumed that the dam will break in the case of overtopping or landslides, which may cause the risk calculation results to be slightly higher than the actual value. It does not affect the analysis and comparison of the final results because the same mathematical model and method were used in the calculation. In engineering practice, the management department often resolves the risk in time through operation scheduling and emergency management measures, so as to avoid the occurrence of dam breaks.

It can be seen from Table 6 and Fig. 10 that the OR of the Dawei Reservoir dam is the highest among the five cascade reservoirs, so the Dawei Reservoir is the weakest cascade that may trigger the failure of the cascade reservoir system, which requires special attention. The OR of the Xiaerga Reservoir dam is relatively lower, but it will directly lead to the successive break of four cascade reservoirs downstream once it breaks, and Shuangjiangkou Reservoir can effectively intercept and weaken the upstream dam-break flood to a certain extent, and its AR is significantly reduced compared with the upstream cascade, which

![img-7.jpeg](img-7.jpeg)

Fig. 8. Dam break flood hydrograph.

indicates that the risk is blocked and prevented further amplification in this cascade. Therefore, both reservoirs belong to the controlling cascades, which determine the risk level of the entire system (Zhou et al., 2018). Although risks to the Dawei Reservoir and Busigou Reservoir are not the largest, they will break under the action of upstream dam-break flood, further amplifying the risk and transmitting it downstream, which belong to the general cascades of the system.

According to the concept proposed in this study, the AR is the product of the dam risk of the upstream cascade and its ICs. Therefore, there are two ways to reduce the AR of cascade reservoir dams: one is to reduce the upstream controlling cascade risk by means of risk elimination and reinforcement, and the other is to reduce the IC by increasing the emergency storage capacity of the targeted cascade. In the construction and management of engineering practice, the system risk should be reasonably designed based on the risk analysis and calculation results. For an incomplete project, the interaction among the cascades in the basin needs to be fully considered, and the position of the controlling cascade should be reasonably arranged with the reserved risk emergency storage capacity. What needs to be addressed is not only the full utilization of water resources, but also the reasonable control of system

Table 4 Calculation results of OR of cascade reservoir group dams (10⁻⁵).


where OT refers to Overtopping, LS refers to Landslide of reservoir bank.

![img-8.jpeg](img-8.jpeg)

### (a) Water level distribution in front of Shuangjiangkou reservoir dam (successive break of Dawei-Bosigou)

![img-9.jpeg](img-9.jpeg)

### (b) Water level distribution in front of Shuangjiangkou reservoir dam (successive break of BaLa-Dawei-Bosigou)

**Fig. 9.** Simulation results after superimposed dam-break flood regulation.

risk. For the built projects, the *OR* of each cascade dam and the *AR* transmitted from the upstream cascade should be scientifically evaluated, and the dam safety (in particular, the weakest cascade dam) should be ensured by reinforcement measures and strengthening monitoring.

The risk analysis and calculation model proposed in this study considers the combination of various working conditions during the long-term operation of the reservoir dam, which makes the risk calculation and evaluation results more reasonable and reliable. *OR* and *AR* are used to divide the risk probability of cascade reservoir dam and the degree of risk transmission and superposition between adjacent cascades is expressed by the value of influence coefficient *IC*, which makes the risk analysis and calculation process clearer and more intuitive. More importantly, this treatment realizes an effective connection with the traditional risk probability calculation method for a single reservoir. In addition, the landslide dam formed by the landslide blocking the river can be regarded as natural earth rock dam (Cao et al., 2011), and thus the risk probability calculation model in this study is also suitable for analyzing and evaluating the risk of landslide dams in downstream reservoirs.

### 6. Conclusions

Owing to the transmission and superposition effect of dam risk, the traditional dam risk calculation methods for a single reservoir cannot meet the needs of risk management in cascade reservoirs. In this study, the risk of cascade dam was divided based on the risk analysis. The

#### Table 5


where A-B indicates the successive break of A and B.

#### Table 6


![img-10.jpeg](img-10.jpeg)

**Fig. 10.** Comparison of dam risks of the cascade reservoirs.

degree of risk transfer and superposition effect was defined as the *IC*, which was quantified in combination with uncertainty analysis, dam break simulation and flood routing. Considering the uncertainty of natural floods, earthquake intensity, soil parameters and reservoir water level, a *BN* model for calculating the *OR* of cascade reservoir dams was constructed. Thereafter, a method for calculating the *AR* and the the dam risk probability of cascade reservoirs was proposed. In the case analysis, all possible water level combinations and successive break scenarios were considered, of which two dam break scenarios under a normal pool level were discussed as examples in detail. This study aims to provide a new idea for the risk analysis and calculation of cascade reservoirs. Limited by the simulation model and the hydrology, earthquake, and soil parameter data in this study, it will be further improved upon and demonstrated in future studies and practice.

### CRediT authorship contribution statement

**Te Wang:** Conceptualization, Methodology, Formal analysis, Investigation, Writing – original draft, Writing – review & editing. **Zongkun Li:** Conceptualization, Validation, Supervision, Funding acquisition. **Wei Ge:** Methodology, Validation, Formal analysis, Writing – review & editing, Funding acquisition. **Yadong Zhang:** Investigation. **Yutie Jiao:**

Methodology. Heqiang Sun: Supervision. Hua Zhang: Formal analysis.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgements

This research was funded by the National Natural Science Foundation of China (Grant No. 52179144, 52079127, U2040224, 51679222, 51709239), the Fund of National Dam Safety Research Center (Grant No. CX2021B01), the Young Talent Support Project of Henan Province (Grant No. 2021HYTP024), Program for Science \& Technology Innovation Talents in Universities of Henan Province (HASTIT) (Grant No. 22HASTIT011).
