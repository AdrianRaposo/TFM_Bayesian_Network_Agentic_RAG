![img-0.jpeg](img-0.jpeg)

This item is the archived peer-reviewed author-version of:

Developing an advanced dynamic risk analysis method for fire-related domino effects

Reference:

Zeng Tao, Chen Guohua, Yang Yunfeng, Chen Peizhu, Reniers Genserik. - Developing an advanced dynamic risk analysis method for fire-related domino effects Process safety and environmental protection / Institution of Chemical Engineers [London] - ISSN 0957-5820 - 134(2020), p. 149-160

Full text (Publisher's DOI): https://doi.org/10.1016/J.PSEP.2019.11.029

To cite this reference: https://hdl.handle.net/10067/1660960151162165141

# Developing an advanced dynamic risk analysis method for fire- 

related domino effects

Tao Zeng ${ }^{\mathrm{a}, \mathrm{b}}$, Guohua Chen ${ }^{\mathrm{a}, \mathrm{b}, *}$, Yunfeng Yang ${ }^{\mathrm{a}, \mathrm{b}, \mathrm{e}}$, Peizhu Chen ${ }^{\mathrm{a}, \mathrm{b}}$, Genserik Reniers ${ }^{\mathrm{c}, \mathrm{d}, \mathrm{e}}$ a Institute of Safety Science \& Engineering, South China University of Technology, Guangzhou, 510640, China
b Guangdong Provincial Science and Technology Collaborative Innovation Center for Work Safety, Guangzhou, 510640, China
c Faculty of Technology, Policy and Management, Safety and Security Science Group (S3G), TU Delft, 2628 BX, Delft, The Netherlands
d Faculty of Applied Economics, Antwerp Research Group on Safety and Security (ARGoSS), University Antwerp, Antwerp, 2000, Belgium
e CEDON, KULeuven, Campus Brussels, Brussels, 1000, Belgium
*Corresponding author.
E-mail address: mmghchen@scut.edu.cn

## ABSTRACT

Domino effects are typically high impact low probability (HILP) accidents, whereby escalation effects triggered by fires are most frequent. The evolution of fire-related domino effects depends on synergistic effects and the performance of safety barriers, but those factors usually are time-dependent. In the present study, a methodology is developed to provide more accurate probabilities related to domino effects, by considering the temporal evolution of escalation vectors caused by time-dependent factors. The Dynamic Bayesian Network (DBN) approach is applied both to model the spatialtemporal propagation pattern of domino effects and to estimate the dynamic probabilities of domino chains. The methodology is illustrated with a case study to determine the dynamic aspect of the probabilities of domino effects considering the impact of add-on (active and passive) safety barriers and taking into account synergistic effects. The critical units for facilitating domino propagation have been identified by the analysis of posterior probabilities, and further validated using graph theory. The methodology will be helpful for risk management and emergency decision-making of any chemical industrial area.

Keywords: domino effect; Dynamic Bayesian Network; synergistic effect; temporal evolution; safety

barrier

# 1. Introduction 

The clustering of chemical plants into industrial parks is a development trend within the petrochemical industry. Any large-scale chemical cluster is congested with complex pipeline infrastructure, high-pressure equipment and other hazardous process units of which malfunctions and mishaps may lead to fires or explosions (He et al., 2018; Wang et al, 2018; Swuste et al., 2019). A domino effect denotes an accident in a unit propagating into the neighboring unit and triggering the escalation of the accident (De Rademaeker et al., 2014; He et al.,2018). Since 1947, domino accidents have been recorded, and most of them resulted in serious economic loss and fatalities. On 19 November 1984, an explosion at the Mexican National Oil Company Pemex caused 650 fatalities, and also 48 tanks were damaged and there were a further 22.5 million dollars losses (Smolders et al., 2014). On 13 November 2005, a refining column exploded in the Petrochemical Biphenyl Plant, Jilin, China, killing 8 people and injuring more than 60 (Fu et al., 2008). Due to their low probability yet catastrophic consequences, the European Seveso III Directive (2012/18/EU) requires that domino scenarios should be considered in the safety management of chemical plants. In order to dynamically predict the probability of accident chains and to take action to prevent the escalation, it is important to broaden the domino effects model by considering the actual accident scenario and real-time risk analysis.

In the field of domino effects, many methods such as the relative risk model (Ni et al., 2016), the matrix-based model (Zhou and Reniers, 2018a), graph theory (Khakzad and Reniers, 2015; Chen et al., 2018; Chen et al., 2019a), Petri-nets (Zhou and Reniers, 2017; Zhou and Reniers, 2018b; Kamil et al., 2019), event trees (Alileche et al., 2017), Bayesian Networks (BN) (Yuan et al., 2016; Khakzad et al., 2013; Khakzad et al., 2014; Khakzad et al., 2016b; Yang et al., 2018), and Dynamic Bayesian Networks (DBN) (Khakzad, 2015; Khakzad et al., 2016a; Khakzad, 2018) have been proposed for modeling domino effects and estimating the vulnerabilities or escalation probabilities of process units. Among those existing methods, BN is widely used in the risk assessment of domino effects due to its flexible structure and the ability for reasoning the uncertainty (Yuan et al., 2016; Khakzad et al., 2013; Khakzad et al., 2014). DBN extends the BN method, which can be used for explicitly modeling the continuity of accident propagation in the time dimension (Khakzad, 2015; Khakzad et al., 2016a;

Khakzad, 2018). More importantly, the posterior probability analysis can show the most likely propagation pattern of domino effects in the next time step, which is beneficial for risk management.

Modeling the likely evolution pattern of actual accident scenarios is a crucial part of domino risk assessment. Many technical standards and safety regulations require the adoption of safety barriers in process units which can effectively impede the propagation of an accident, or even avoid the escalation of domino effects. Chief among them are the engineering active and passive safety barriers which are called the add-on safety barriers (Khakzad et al., 2017). However, only a few previous studies have addressed the role of safety barriers in the propagation of domino effects. Landucci et al. (2015) improved the probability model for domino escalation considering the role of active and passive safety barriers. Khakzad et al. (2017) proposed a methodology to study the cost-effectiveness of safety barriers based on graph theory. Khakzad (2018) investigated emergency response actions for fire-related domino effects while considering safety barriers based on a risk-informed methodology. But those studies usually neglected the burnout state of the unit, let alone the temporal change of the escalation vector due to the combined action of fuel burnout and the effect of safety barriers in place, which resulted in an inaccurate prediction of domino risks.

The present work is aimed at exploring the temporal evolution of the synergistic effects and the role of add-on safety barriers on the domino propagation pattern. A methodology based on DBN is proposed, which can both model the spatial-temporal evolution of domino effects and calculate the probabilities of domino chains. Due to the inventories of an accident unit may burn out in the domino propagation, the burnout state is introduced to the unit nodes in the DBN. The methodology is applied to an industrial case study to discuss the influence of synergistic effects and different configurations of safety barriers on the domino propagation. Besides, through multi-dimensional posterior probabilities' analysis, the most probable domino chains and the most critical nodes are identified, which can be used for the prevention of domino effects and emergency decision-making in the chemical industrial area.

Section 2 explains what are fire-related domino effects and describes the calculation method for determining escalation probabilities considering add-on safety barriers. The basic procedure of the developed method and the corresponding explanations are illustrated in Section 3. Next, the developed method is illustrated by a case study and validated using graph theory in Section 4. In

Section 5, a discussion related to the case study and the engineering significance of the method are expounded. Finally, conclusions are provided in Section 6.

# 2. Characteristics of Domino Effects Considering Safety barriers 

### 2.1 Overview of fire-related domino effects

In the framework of domino risk analysis, the primary event including fires and explosions, and the threshold criteria is developed to determine whether the escalation occurs or not (Reniers and Cozzani, 2013). Compared to the domino effects triggered by explosions, fire-related domino effects usually continue over an extended period and generate the changing escalation vectors with the evolution of accidents. Therefore, this paper mainly focuses on the spatial-temporal evolution of firerelated domino effects. The features of fire-related domino effects are summarized in Table 1 (Cozzani et al., 2006).

Table 1 - The features of fire-related domino effects (Cozzani et al., 2006).


For fire-related domino effects, several former researches were devoted to solve the uncertainty problem (Cozzani et al., 2006; Khakzad et al., 2013; Landucci et al., 2015; Khakzad and Reniers, 2015; Khakzad et al., 2016b; Khakzad, 2018; Zhou and Reniers, 2018a). The overview of those studies (Table 2) shows the performance of safety barriers and the complex evolution of synergistic effects are gradually recognized in the domino analysis. In recent years, the dynamic analysis has become a growing trend for domino research, and visual topological structure is beneficial to the detailed description of domino propagation. DBN can model the synergistic effects and parallel effects of fire-related domino scenarios considering the time dimension of accident propagation (Khakzad, 2015; Khakzad et al., 2016a; Khakzad, 2018). This approach can thus effectively guide the development of the domino effects prevention and control strategy. However, most of the previous dynamic risk research on domino effects disregarded the mutation problem of escalation vectors. Introducing the temporal evolution of escalation vectors into the risk analysis of domino effects leads

to more accurate probability calculation results. Besides, too many nodes can not only cause technical problems in DBN modeling, but it is also introducing more uncertainty to the analysis. Another crucial issue of dynamic risk analysis using DBN is how to simplify network structure, it is beneficial to model the complex propagation pattern with multi-units.

Table 2 - Overview of relevant studies for the fire-related domino effects (ttf: the time to failure of target unit).


# 2.2 Safety barriers related to domino effects

There are four types of safety barriers to prevent the escalation of accidents: inherently safer design, active protection systems, passive protection systems and emergency procedures (Center of Chemical Process Safety, 2001). Each type of safety barriers has different action mechanisms and functions, and their quantitative implementation is reflected in the Layer of Protection Analysis (LOPA) approach (Yan and Xu, 2018). However, inherently safer design is limited to the design phase, and cannot be improved in the operation phase. Its function can be embodied in the failure rate

and does not directly affect the escalation vector in the domino propagation. Emergency procedures depend on the daily training of emergency teams and the allocation of emergency means which can make a notable difference in different chemical clusters or plants. Therefore, the focus of the study is on the active protection system and the passive protection system, also known as add-on safety barriers. Their impacts on the propagation of domino effects are analyzed, which are summarized in Table 3.

Table 3 - Add-on safety barriers in a chemical cluster (Center of Chemical Process Safety, 2001).


The add-on safety barriers are designed to delay or prevent the escalation of domino effects (Salvi and Debray, 2006). Therefore, the role of add-on safety barriers is usually considered to directly or indirectly increase the time to failure ( $t t f$ ) of the equipment (Landucci et al., 2015). An active protection system can be used to reduce the strength of the escalation vector, while a passive protection system can be used to reduce the level of heat radiation exposure of target equipment. Both of them can significantly increase the $t t f$ of the equipment compared to the situation without add-on safety barriers.

# 2.3 Probit model considering add-on safety barriers 

The probit model is developed to calculate the escalation probability, which involves the characteristics of escalation vector (e.g. duration and intensity) and target units (e.g. resistance to damage) (Reniers and Cozzani, 2013). The equation for the probit model (Reniers and Cozzani, 2013) under heat radiation is as follows:

$$
\left\{\begin{array}{l}
P=\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{Y-5} \exp \left(-u^{2} / 2\right) \mathrm{d} u \\
Y=12.54-1.847 \ln (t t f)
\end{array}\right.
$$

where $P$ is the escalation probability; $Y$ is the probit value.

The equation (1) shows the $t t f$ of target unit is the only input parameter of the probit model for fire-related domino effects. As mentioned before, the performance of safety barriers will affect the values of $t t f$. Therefore, the relevant quantitative analysis of those influential factors to $t t f$ will improve the accuracy of escalation probability estimation.

Since the active protection system requires external activation to perform the protection action, its reliability $\alpha$ should be considered. For fire accidents, the role of active protection systems can be classified into two categories for preventing domino effects: reducing the heat radiation emitted from the external accident or reducing the heat radiation received by the target equipment (Landucci et al., 2015). When an active protection system is successfully activated, the heat radiation can be calculated as follows (Landucci et al., 2015):

$$
Q^{\prime}=(1-\eta) Q
$$

where $Q$ is the original heat radiation $\left(\mathrm{kW} / \mathrm{m}^{2}\right) ; \eta$ is the reduction rate of the active protection system and $Q^{\prime}$ is the heat radiation $\left(\mathrm{kW} / \mathrm{m}^{2}\right)$ after the mitigation.

The role of passive protection systems can be considered as directly increasing the $t t f$ of the equipment. Considering a passive protection system, the $t t f(\min )$ of the equipment under the external fire can be calculated by the following formula (Landucci et al., 2015):

$$
t t f=0.0167 \times \exp \left(c V^{d}+e \ln \left(Q_{H L}\right)+f\right)
$$

in which $Q_{H L}$ is the heat radiation $\left(\mathrm{kW} / \mathrm{m}^{2}\right)$ received by the target equipment; $V$ is the target equipment volume $\left(\mathrm{m}^{3}\right) ; c, d, e, f$ are coefficients, and their values are listed in Table 4.

Table 4 - Summary of the coefficients values for Eq. (3) (Landucci et al., 2015).


Therefore, when considering the add-on safety barriers, the $t t f$ of target equipment under a heat load is as follows:

$$
\left\{\begin{array}{l}
t t f_{1}=0.0167 \times \exp \left(c V^{d}+e \ln (Q^{\prime})+f\right), P=\alpha \\
t t f_{2}=0.0167 \times \exp \left(c V^{d}+e \ln (Q)+f\right), P=1-\alpha
\end{array}\right.
$$

where $t t f_{l}$ is the time to failure of the equipment when the active protection system is effectively activated on demand; $t t f_{2}$ is the time to failure of the equipment in the case that the active protection system is not enabled.

Based on equation (4), it can be concluded that if the active protection system is enabled, the $t t f$ of the equipment is extended by $\lambda$ times, as shown in the following equation:

$$
\lambda=\frac{t t f_{2}}{t t f_{1}}=\exp [e \ln (1-\eta)]
$$

Substituting equation (4) into equation (1), the probit model of domino effects considering the add-on safety barriers can be obtained.

# 3 Dynamic Bayesian Network Modeling Method 

### 3.1 Basic procedure

The methodology analyzes the spatial-temporal evolution of fire-related domino effects under the influence of add-on safety barriers. The procedure of the approach is given in Fig. 1, and is comprised of the following steps:

Step 1: According to the risk assessment report of the chemical industrial area, the layout and characterization of the dangerous units and add-on safety barriers can be collected. Those units, atmospheric or pressurized, are vulnerable to a fire accident outside from the unit and may trigger an escalation of an accident. Add-on safety barriers are assigned to those dangerous units for mitigation or prevention of domino effects. The units and safety barriers are assigned to nodes in DBN to discuss the propagation pattern of domino effects.

Step 2: After determining the primary accident, the time to burnout ( $t t b$ ) of the primary unit $\left(\mathrm{U}_{\mathrm{p}}\right)$ can be calculated (e.g., see the guidance for quantitative risk assessment in the petrochemical plant or API 581-2016). There are three states (safety, fire, burnout) for each unit to describe the evolution of fire accidents, and the state of each unit can only transfer to the next state until the 'burnout' state. Once a unit catches fire in a certain time, the probability of the 'burnout' state after an interval (the $t t b$ ) is 1 . Besides, if the unit is burned out at time $t$, the probability of state 'burnout' equals 1 at the next time step. Considering the update process of the unit state, a temporal arc is drawn from the primary unit to itself, the CPT is as shown in Table 5. The heat radiation released by the primary unit will trigger the add-on safety barriers to perform the protection action. Therefore, the escalation vector is time-dependent due to the enablement or degradation of those safety barriers. The origin heat radiation can be calculated by consequence analysis software (e.g., Phast), but it should be corrected

according to the add-on safety barriers status using equation (2), namely the actual escalation vector received by target units. The potential secondary unit can be identified by using the comparison result between the threshold in Table 1 and the escalation vector, and the $t t f$ of a potential secondary unit can be calculated using equation (4).
Table 5 - Conditional probability table for $\mathbf{U}_{\mathrm{p}}$ (the initial condition is $\boldsymbol{P}_{\text {Up is fired }}=\mathbf{1}$ at $\boldsymbol{t}=\mathbf{0} ; \boldsymbol{\tau}$ is the time interval spanned by temporal arc).


Step 3: 'Temporal judgment' model is developed to determine the occurrence condition of escalation and synergistic effects in view of a timeline. For the sake of simplicity, domino propagation is likely to occur when the $t t b$ of the external fire is larger than the $t t f$ of the target unit. Suppose the equipment $i$ is the already engaged unit, and the equipment $j$ is the newly engaged unit, the temporal judgment model then decides as follows:
(1) If $t t b_{i}<t t f_{j}$, the domino chain does not propagate at equipment $j$. Let $t=t t b_{i}$, then the accident propagation probability at $t-\Delta t, t, t+\Delta t$ is 0 ;
(2) If $t t b_{i}=t t f_{j}$, the accident $i$ has the probability of causing an accident in equipment $j$, but $i$ and $j$ have no synergistic effect to affect other equipment. Let $t=t t b_{i}=t t f_{j}$, the accident of equipment $j$ does not occur at $t-\Delta t$; accident $j$ has the probability to occur at $t$; the fire of equipment $i$ extinguishes, no synergistic effect at $t+\Delta t$;
(3) If $t t b_{i}>t t f_{j}$, accident $i$ and accident $j$ is in synergy, the heat radiation received by other equipment is strengthened, and the domino escalation probability increases. Let $t=t t f_{j}$, accident $j$ does not occur at $t-\Delta t$, accident $j$ has the probability to occur at $t$; the heat radiation emitted from accident $i$ continues, and if equipment $j$ is ignited, the heat radiation is superposed at $t+\Delta t$. The synergistic effect will be changed if one of the fire units is burned out.

Step 4: The state transition of the secondary unit $\left(\mathrm{U}_{\mathrm{s}}\right)$ depends on not only its prior state, but also the primary accident. Therefore, the two causes are separated to avoid the temporal logic confusion, e.g., the two-state (safety and fire) node $\mathrm{U}_{\mathrm{s}}$ is used to explore the domino evolution, and an auxiliary node $\mathrm{U}_{\mathrm{s}}{ }^{\prime}$ is set to show the whole process of state transition like the $\mathrm{U}_{\mathrm{p}}$ node. For the $\mathrm{U}_{\mathrm{s}}$ node, the state is assumed to 'safety' when it doesn't receive the heat radiation. Then, a 'HEAT' node is added, which represents the heat radiation received by $\mathrm{U}_{\mathrm{s}}$ under the influence of safety barriers. The 'no radiation'

state of the 'HEAT' node is used to show the 'burnout' state of the primary unit or the heat insulation effect of the fireproof material. Considering the heat radiation is mitigated or not, the escalation probability ( $P_{\mathrm{m}}$ and $P_{\mathrm{n}}$ ) of $\mathrm{U}_{\mathrm{s}}$ can be calculated using the probit model. A temporal arc (spanned the time interval of $t t f$ ) is drawn from the HEAT node to the $\mathrm{U}_{\mathrm{s}}$ node to depict the propagation pattern and to indicate delayed effects of escalation, the CPT of $\mathrm{U}_{\mathrm{s}}$ is shown in Table 6. If there is no other unit, the domino propagation is terminated. Otherwise, the analysis is continued and get into the next step.
Table 6 - Conditional probability table for $\mathbf{U}_{\mathrm{s}}$ (the initial condition is $\boldsymbol{P}_{\mathrm{U} \mathrm{s} \text { is safety }}=1$ at $\boldsymbol{t}=0$ ).


Step 5: Given the secondary unit is on fire, and assume that the accident scenario of the secondary unit is specified. Then steps 2-4 are repeated to identify the potential tertiary units when the secondary units are used to substitute the primary unit. Notably, target units damaged by synergistic effects need to be considered when the $t t b$ of the former accident unit is higher than the time-sum of the $t t f$ of the target units in the same domino chain. For instance, the heat radiation released by accident $i$ and accident $j$ are employed together to damage unit $k$ only if $t t b_{i}>t t f_{j}+t t f_{k}$ and $t t b_{j}>t t f_{k}$. Then the quaternary units, fifth units and so forth are identified by repeating those steps until propagation termination.

If the domino effect is $l$-order, and the $n$ th-order domino effect involves a total of $m$ target equipment, the DBN computing time domain $t d$ can be calculated by:

$$
t d=\sum_{n=1}^{l} \max \left(t t f_{1}^{(n)}, t t f_{2}^{(n)}, \cdots, t t f_{m}^{(n)}\right)
$$

The DBN can be unrolled to the equivalent BN in different time slices (also referred to as time frame) (Reynolds et al., 2008), which corresponds to a vertical section at a certain time point of domino propagation. To avoid the scenario mutation of domino propagation not being possible to be captured, the time slicing is needed to ensure approximation of the critical moment ( $t t f$ of target unit and $t t b$ of accident unit). The initial time slice $(t=0)$ is placed at the time of the primary accident, and the computing time domain is reasonably dividing some slices according to the actual scenario.

![img-1.jpeg](img-1.jpeg)

Fig. 1. Procedure for dynamic analysis of domino effects.

# 3.2 Model simplification of DBN 

Fig. 2 depicts the conventional DBNs of a domino chain consisting of 3 tanks whether to consider add-on safety barriers.
![img-2.jpeg](img-2.jpeg)
(a) DBN model of domino effect without safety barriers
![img-3.jpeg](img-3.jpeg)
(b) DBN model of domino effect with safety barriers

Fig. 2. Dynamic Bayesian Network of domino effects without or with safety barriers
(T) means tank i; APS; means active protection system for tank i; PPS; means passive protection system for tank i).

It can be seen from Fig. 2 that the passive protection system is considered as a static node and does not change with time if its degradation is not considered. The activation of the active protection system depends on its reliability, and its state is affected by the state in the previous time slice. In addition to the domino propagation direction, the temporal arc between nodes represents the time delay effect in the DBN.

But, with such a large number of nodes, the network structure and parameter setting of DBN is too complex, especially for the multi-unit scenario. Therefore, a simplified method is advanced to quickly model the propagation pattern in some situation. If the former accident units can't be burned out in the time domain, the role of passive protection system can be simplified to the arc between the equipment nodes. Considering the overall active protection system in the study area, it can be divided into two scenarios: active protection system 'enabled' and 'non-enabled'. Therefore, the role of active protection system can also be simplified into the conditional probability table of equipment nodes to improve the DBN structure, as shown as the case study in Section 4. A comparison of the $t t f$ of equipment with and without add-on safety barriers is illustrated in Fig. 3.
![img-4.jpeg](img-4.jpeg)

Fig. 3. $t t f$ of equipment with and without add-on safety barriers ( $\Delta t$ is the effective protection time of passive protection systems).

# 3.3 Implementation of DBN reasoning 

BN is a probabilistic causal network for probabilistic inference and information fusion, which is widely used to analyze domino effects (Khakzad et al., 2013; Khakzad et al., 2014; Yuan et al., 2016;

Yang et al., 2018). In BN, the link node pointed to by the arc is called 'child node', and the node in the opposite end is called 'parent node'. BN is a directed acyclic structure which means no arc can come back from the child node to its parent node. Using the chain rule and d-separation criteria, the joint probability distribution (JPD) of BN can be obtained (Khakzad et al., 2013; Khakzad et al., 2014; Yang et al., 2018):

$$
P(U)=P\left(X_{1}, X_{2}, \cdots, X_{n}\right)=\prod_{i=1}^{n} P\left(X_{i} \mid P a\left(X_{i}\right)\right)
$$

Where $U$ is the set of those nodes $\left(X_{1}, X_{2}, \cdots, X_{n}\right), P a\left(X_{i}\right)$ is the parent node set of $X_{i}$.
Bayes' theorem is the governing equation for probability updating of BN , the updated JPD under the given evidence $E$ can be expressed as (Khakzad et al., 2013; Khakzad et al., 2014):

$$
P(U \mid E)=\frac{P(U) \times P(E \mid U)}{\sum_{U / E} P(U) \times P(E \mid U)}
$$

DBN is the derivative of BN to depict the temporal relationship of those nodes in a discretized timeline (Khakzad et al., 2016a; Khakzad, 2018). In DBN, the node in time slice $t$ (denotes $X_{i}^{t}$ ) is conditionally dependent not only with the parent nodes in the same time slice but also with the parent nodes and itself in the previous time slice. The JPD is calculated as (Khakzad et al., 2016a; Khakzad, 2018):

$$
P\left(U^{t}\right)=P\left(X_{1}^{t}, X_{2}^{t}, \cdots, X_{n}^{t}\right)=\prod_{i=t}^{n} P\left(X_{i}^{t} \mid X_{i}^{t-1}, P a\left(X_{i}^{t-1}\right), P a\left(X_{i}^{t}\right)\right)
$$

DBN can estimate the future state and probability of nodes, which is convenient for a dynamic analysis. The structure and calculation amount of DBN is larger compared to BN because the timeline is divided into many intervals. The Bayesian Network software GeNIe (BayesFusion, 2015) can effectively solve this problem and updates the probability using the belief updating algorithm.

After selecting the calculation time step, the arc between the nodes reflects the propagation direction of the domino chains, the heat radiation reduction of the add-on safety barriers and the hysteresis of the delayed ignition. The temporal change of the coupling escalation vector generated by the synergistic effect and the impact of add-on safety barriers can be accurately mapped into the DBN and the dynamic update of the escalation probability can be corrected accordingly.

# 4 Case Study and Verification 

### 4.1 Case study

Multiple dangerous equipment is present and a lot of dangerous substances are stored in a tank farm which is usually located at a core area of a chemical plant (Yang et al., 2020). According to the statistics of Darbra et al. (2010), storage areas represent the highest proportion of accident scenarios in 225 domino accidents.

For illustrative purposes, the application of the methodology is demonstrated via a tank farm located in south China. The layout of the tank farm is shown in Fig. 4. Those tanks are all internal floating roof tanks, and other parameters are summarized in Table 7. For the sake of brevity, only the sprinklers were investigated when considering the active protection system in the tank farm, and only one accident scenario (pool fire) for the units. The heat radiation received by the target equipment after cooling consists of $60 \%$ of the initial heat radiation, i.e. $\eta=0.4$, and the reliability of the sprinkler system is 0.99 (Khakzad, 2018). In the framework of escalation prevention, the application of fireproof materials is an important and effective safety barrier (Landucci et al., 2015). Some fireproof materials (e.g., intumescent coatings) can insulate the equipment from the heat for about 2 hours, which may play an important role to impede the domino propagation (Khakzad et al., 2017; Chen et al., 2019b).

T2 has a larger inventory of hazardous substances, and it is assumed that T2 is the primary unit. Considering the typical combination of active-passive safety barriers, several demonstrative cases are analyzed:

Case 1: The active protection system was not activated $(P=0.01)$, and those tanks only have the conventional passive protection system;

Case 2: The active protection system was activated on demand $(P=0.99)$, and those tanks only have the conventional passive protection system;

Case 3: The active protection system was not activated $(P=0.01)$, the conventional passive protection system and the new fireproof materials are used in those tanks;

Case 4: The active protection system was activated on demand $(P=0.99)$, the conventional passive protection system and the new fireproof material are used in those tanks.

![img-5.jpeg](img-5.jpeg)
(a) Satellite map of the tank farm
![img-6.jpeg](img-6.jpeg)
(b) Layout of the tank farm

Fig. 4. Satellite map and layout of the tank farm.
Table 7 - Tank parameters.


According to the main meteorological conditions of the tank farm, the wind comes from the northwest at $2.7 \mathrm{~m} / \mathrm{s}$, the stability is grade B , the ambient temperature is $22.5^{\circ} \mathrm{C}$ with 0.67 relative humidity, and the leakage aperture is set to 100 mm . The heat radiation is calculated by the multifunctional quantitative risk analysis and risk assessment software Phast 8.1 (DNV GL, 2019), and the calculation results are listed in Table 8.

Table 8 - Heat radiation ( $\mathrm{kW} / \mathrm{m}^{2}$ ) received by the different tank (Ti fire).


The guidance for quantitative risk assessment in the petrochemical plant from China Petrochemical Co., Ltd (2007) offered the formulas of pool fire burning rate, and the $t t b$ of each tank can be calculated by dividing the inventory of hazardous material by the burning rate. Based on Table 8 and equation (4), the $t t f$ of each tank can be calculated. The above results are shown in Table 9.

Table 9 - Time to burnout and time to failure of each tank.


# (1) Case 1 calculation discussion 

The DBN model of domino effects in case 1 is shown in Fig. 5. For the domino accident, the propagation of the domino events relies on the escalation vectors emitted from the previous-order accidents, and the escalation vectors of lower-order units are not enough to cause the escalation. Therefore, the conventional arcs, e.g. dash line in Fig. 5, are used to connect equipment nodes that differ by two orders of domino effects, and the arcs entering the same target equipment account for the possible synergistic effect between low-order accidents.
![img-7.jpeg](img-7.jpeg)

Fig. 5. Dynamic Bayesian Network of domino effects in the case 1.
The computational time domain is 9 min , in steps of 1 min , and the analysis results of DBN are shown in Fig. 6. It can be seen from Fig. 6(a) that after T2 is on fire for 6 minutes, there is a creditable probability that T1/T4 catch fire; after 7 minutes, T3 may also catch fire, and the fire probability of T1/T3/T4 increases linearly with time; the fire probability of tertiary equipment T5/T6 is in the order of $10^{-5}$. Fig. 6(b) shows that when the order 1 domino accident is assumed, the T1/T4 fire probability is $43 \%$, which is slightly higher than T3; after T2 catches fire for 9 minutes, T6 has a higher fire probability than T5 because of the order 1 domino accident. As can be seen in Fig. 6(c), when the order 2 domino accident is assumed, the T1/T3/T4 fire probability increases first and then stabilizes

with time, and $\mathrm{P}_{\mathrm{T} 4}>\mathrm{P}_{\mathrm{T} 3}>\mathrm{P}_{\mathrm{T} 1}$, the T 4 fire probability reaches $63 \%$, T 3 has a probability of $31 \%$; T 6 its fire probability is $75 \%$, T5 its fire probability is $25 \%$. We may conclude that T6 is the high-risk unit in the order 2 domino accident.
![img-8.jpeg](img-8.jpeg)

Fig. 6. Dynamic Bayesian Network analysis results of case 1.
(2) Case 2 calculation discussion

For the sake of clarity, when the active protection system is enabled $(\mathrm{P}=0.99)$, the heat radiation received by the tank in the same catch basins with the accident tank is not affected by the active protection system, but the incoming heat flux of other vessels is mitigated. Due to the reduction of heat radiation, the domino chains changed, and the new DBN model developed in Fig. 7 can be used to simulate the evolution pattern under this situation.

![img-9.jpeg](img-9.jpeg)

Fig. 7. Dynamic Bayesian Network of domino effects in the case 2.
The calculation time domain is 14 min , in steps of 1 min , and the DBN analysis results are shown in Fig. 8. Compared with case 1, both the calculation time domain and the order of domino effects increased due to the reduction effect of the active protection system on the emitted heat flux from the accident source. Considering the prior probability, the fire probability of the quaternary equipment T5/T6 is $10^{-9}$ in order of magnitude. Since the probability is too low, the probability curve is not drawn in Fig. 8(a). It can be seen from Fig. 8(a) that after 6 minutes of T2 being on fire, T1 has a creditable probability of catching fire and increasing linearly with time; and due to the possible fire in T1, T3/T4 have a fire probability if T2 would be on fire for at least 11 minutes, also increasing linearly with time, the T3/T4 fire probability is in the $10^{-5}$ order of magnitude and $\mathrm{P}_{\mathrm{T} 4}>\mathrm{P}_{\mathrm{T} 3}$. As Fig. 8(b) shows, if the order 1 domino accident occurs, the probability of T1 catching fire increases gradually after 6 minutes of T 2 being on fire, and reaches $100 \%$ in the final time step; the comparison result of the probability of tertiary equipment being on fire is the same as the prior probability analysis but it increased by two orders of magnitude according to the numerical results. It can be seen from Fig. 8(c) that when the order 2 domino accident is assumed, T1 will certainly catch fire (probability of $100 \%$ ) after T 2 is on fire for 9 minutes. T4 has a probability of $59 \%$ of catching fire in the final time, which thus is the most vulnerable equipment related to the order 2 domino accident; the T5/T6 fire probability is increased to $10^{-4}$ or more, which is 5 orders of magnitude higher than the prior probability. Fig. 8(d) shows that when it is assumed that the order 3 domino accident occurs, T1 will certainly catch fire ( $100 \%$ probable) when T2 is on fire for 6 minutes; the T3/T4 fire probability tends to be stable after 11 minutes of T2 on fire, the fire probability of T3 reaches $57 \%$; the fire probability of T6 is $58 \%$ when T2 is on fire for 14 minutes, which thus is the high-risk unit related to the order 3

domino accident.
![img-10.jpeg](img-10.jpeg)

Fig. 8. Dynamic Bayesian Network analysis results of case 2.
(3) Case 3 calculation discussion

It is assumed that fireproof materials are used on the tanks. According to the article from Khakzad et al. (2017), when the thermal radiation exceeds the threshold, the tanks are considered to be in a state of heat insulation for 2 hours, and the protective layer will degrade after 2 hours. As the inventory in the accident tank may burn out, the escalation vector will change over time.

T2/T1 may burn out in the calculation time domain, the burnout state is added to the T2/T1 node, and the DBN model of domino effects is shown in Fig. 9. Since the heat radiation of T2 on fire can only cause the failure of the secondary equipment's protection layer, setting an FM (T1, T3, T4) node in DBN represents the fireproof material of secondary equipment. The time-delay effect of the heat radiation received by the target equipment is reflected in the HEAT node. The T3/T4 burnout time is much longer than the calculation time domain and does not need to be set the same as T2, the fireproof material of T5/T6 can be simplified into the temporal arc, and no fireproof material and heat radiation nodes need to be set. The auxiliary node $\mathrm{T1}^{\prime}$ is set as the three-state node of T 1 , and the burnout

probability of T 1 can be acquired at $\mathrm{T1}^{\prime}$.
![img-11.jpeg](img-11.jpeg)

Fig. 9. Dynamic Bayesian Network of domino effects in the case 3.
The calculation time domain is 5 h , in steps of 30 min , and Fig. 10 shows the results of the DBN analysis. It can be seen from Fig. 10(a) that T2 will burn out within 3.5 h , and no heat radiation is emitted thereafter; in $0-2 \mathrm{~h}$, due to the heat insulation effect of the fireproof material, the heat radiation received by the secondary equipment $\mathrm{T} 1 / \mathrm{T} 3 / \mathrm{T} 4$ is 0 ; within $2 \mathrm{~h}-3.5 \mathrm{~h}$, the heat flux emitted from the T2 fire will act on the target equipment, which may cause possible domino effects. Fig. 10(b) shows that the fire probability of $\mathrm{T} 1 / \mathrm{T} 4$ is higher than that of T 3 , and both reach a peak value at 3.5 h . If the target equipment has not been ignited, it will not cause domino effects because T 2 is burned out; after 4.5 h of T 2 on fire, T 1 has the probability to burnout, and the burnout probability curve has the same slope as the probability curve of T 1 on fire; the fire probability of the tertiary equipment $\mathrm{T} 5 / \mathrm{T} 6$ is in the order of $10^{-7}$, and $\mathrm{P}_{\mathrm{T} 6}>\mathrm{P}_{\mathrm{T} 5}$. It can be seen from Fig. 10(c) that when the order 1 domino accident would occur within 2.5 h , the fire probability of $\mathrm{T} 1 / \mathrm{T} 3 / \mathrm{T} 4$ increases first and then stabilizes, and the fire probability of $\mathrm{T} 1 / \mathrm{T} 4$ reaches $41 \%$; after 4.5 h of T 2 on fire, the T 1 burnout probability also reaches $41 \%$; the tertiary equipment fire probability is increased by 3 orders of magnitude. It can be seen from Fig. 10(d) that when the order 2 domino accident occurs in 5 h, T4 becomes the high-risk unit in the order 1 domino accident with a fire probability of $62 \%$ and the fire probability of T 3 is $38 \%$. Even if T 1 on fire, it has no effect on the order 2 domino accident because the fire will extinguish before the degradation of the tertiary equipment's fireproof material. Therefore, the fire probability of T 1 in

the posterior probability analysis is only $1.95 \times 10^{-3}$.
![img-12.jpeg](img-12.jpeg)

Fig.10. Dynamic Bayesian Network analysis results of case 3.
(4) Case 4 calculation discussion

When the active protection system is enabled, the heat radiation of T 2 can only affect T 1 and is not sufficient to disable the fireproof material of other tanks. Even if the order 1 domino accident occurs, considering the burnout time of T 2 and T 1 , the fire time is shorter than the degradation time of the fireproof material, which will not lead to domino propagation. Therefore, there is no need for DBN analysis.

# 4.2 Methodology verification 

The graph theory method is widely used in the equipment or plants vulnerability analysis of domino effects (Khakzad and Reniers, 2015; Khakzad et al., 2017; Yang et al., 2018; Chen et al., 2019a). In a connected graph, the closeness of a node is a measurement of centrality in the graph structure by calculating the sum of the shortest paths' length between the node and all other nodes in the graph. Therefore, the higher the closeness of a node, the closer it is to other nodes. The closeness can be calculated by the following formula (Yang et al., 2018; Chen et al., 2019c):

$$
C(x)=\frac{1}{\sum_{y} d(y, x)}
$$

where $d(y, x)$ is the distance between nodes $x, y$.
Khakzad et al. (2017) demonstrated that if the node has a higher closeness, the vulnerability in the domino effects scenario will be higher, and the dynamic graph theory method can be used to analyze the unit temporal vulnerabilities considering the add-on safety barriers. For case 1 and case 2 , although there are some safety barriers, none of the tanks has burned out during the whole process of the analysis. Therefore, the result of the static graph theory can indicate the vulnerability of those tanks. For case 3, the dynamic graph theory method is used to divide the time into four time slices, $[0,2 \mathrm{~h}],[2 \mathrm{~h}, 3 \mathrm{~h}]$, [3h, 4h], [4h, 5h]. Since [0, 2h] is in the heat insulation state for all target equipment due to the fireproof materials, there is no domino propagation, and in [3h, 4h], T2, T1 (if on fire) will burn out, the structure of the graph will change. To ensure the consistency of the vertices, the closeness of [2h, 3h] (i.e., T1, T3, T4 fireproof materials failure, T5, T6 fireproof materials effective) is calculated. Due to the add-on safety barriers of case 4 , no domino propagation of order 2 or higherorder occurs, the graph of case 4 is not analyzed. The closeness calculation is programmed using the igraph software package of R language (Adhikari and Dabbs, 2018), and the results are shown in Table 10.

Table 10 - Closeness result for graph theory.


T3 and T4 have higher closeness, indicating that the vulnerability of the unit is higher than others with respect to domino effects. Correspondingly, the posterior probability should also be a higher numerical value. This is consistent with the results of Figures 6(c), 8(d), and 10(d), supporting the accurateness of the developed methodology.

# 5 Discussion 

Actual accident scenarios are more complicated relative to the case study. In the actual domino propagation, the synergistic effects are combined logically to be a coupling system rather than the superposition of heat radiation. Besides, the service time and the corrosion degree of chemical units

or equipment have some influence on its $t t f$, and a more accurate estimation method is needed. Although the methodology has some ideal assumptions, the laws of probability are very clear and strict.

Comparing the analysis results of case 1 and case 2, the synergistic effect of different orders always persists in the domino propagation, and the fire probability of the target unit increases with time. The activation of the active protection system led to the pattern changes in the domino effects, and the fire probability of T5/T6 was even reduced by three orders of magnitude. Assuming that the highest-order domino accident occurred, the posterior probability analysis of case 1 showed that T1 was the secondary equipment with the lowest probability of catching fire, only $7 \%$. But the posterior probability analysis of case 2 showed that the fire probability of T 1 was $100 \%$. It proved that the activation of active protection systems may result in a vulnerability difference of the same equipment in terms of domino effects.

For the initial condition of case 1 and case 3, obviously, the calculation time domain is greatly increased when the fireproof material is added. Since some accident tanks may burn out in the calculation time domain, the heat radiation will be abruptly changed between sequent time slices. The fire probability of the tertiary equipment $\mathrm{T} 5 / \mathrm{T} 6$ has been reduced by at least an order of magnitude due to the heat insulation effect of the fireproof material. The probability comparison results of case 1 and case 3 is the same which is $\mathrm{P}_{\mathrm{T} 4}>\mathrm{P}_{\mathrm{T} 3}>\mathrm{P}_{\mathrm{T} 1}$ when the order 2 domino accident is assumed. This result is due to the small amount of heat radiation emitted from T1 to the tertiary equipment. T1 may burn out, and the influence of T1 on the order 2 domino accident is smaller or even negligible when considering the effective time of the fireproof material.

Case 4 shows that a higher-order domino accident is avoided when the fireproof material interacts with the active protection system. This combination type of safety barriers cuts off the accident chain in the case based on the theory of chain mitigation and disaster reduction, which can avoid the propagation of higher-order domino effects and offer effective protection for the tank farm.

In summary, the using of add-on safety barriers can significantly reduce accident probability and provides extra time for emergency response. Though the application of fireproof material requires extra costs, it is particularly prominent in delaying or impeding domino effect propagation. Efficient add-on safety barriers may be expensive, whereas they are meaningful for the safety operation of the

chemical industrial area, especially considering follow-up effects (e.g., casualties, construction delay and environmental impact) caused by the domino accidents. Under a limited budget, add-on safety barriers should be used for critical units which are identified by a posterior probability analysis as a priority, which can effectively mitigate partial domino effects.

# 6. Conclusions 

This study proposes a dynamic probability prediction methodology based on DBN which considers the temporal evolution of multi-source heat radiation and the performance of add-on safety barriers in case of fire-related escalating accidents. The burnout state of units is introduced into the DBN to study the dynamic change of escalation vectors under the temporal impact of add-on safety barriers, and a quantitative analysis of the dynamic update process of the domino risk is carried out.

The application of the methodology to the case study shows that add-on safety barriers have a great impact on the domino propagation probability. Those add-on safety barriers, existing or not, will lead to several orders of magnitude difference in the probability level, and may even change the domino chain. Fireproof materials have an important significance for chain mitigation in fire-related domino accidents. Therefore, the probability results are more accurate when considering the timeevolving state-transition of the add-on safety barriers and the synergistic effect in the domino effects.

More importantly, through the posterior probability analysis, the critical unit that causes the domino effect can be efficiently searched from different dimensions, which can support the decisionmaking for the allocation of add-on safety barriers and the optimal decision of emergency resource scheduling.

## Acknowledgements

This study was supported by the National Natural Science Foundation of China (21878102), the National Key R\&D Program of China (2016YFC0801500), and the National Natural Science Foundation of China (21576102).
