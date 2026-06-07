# Corresponding Author: 

Wenpei Zheng
Email: zhengwenpei@cup.edu.cn
College of Mechanical and Transportation Engineering
China University of Petroleum (Beijing)
Changping Fuxue Road 18 Beijing, China

## Authors information

Shengnan $\mathrm{Wu}^{\mathrm{a}, \mathrm{b}}$ Laibin Zhang ${ }^{\mathrm{a}}$ Wenpei Zheng ${ }^{\mathrm{a}}$ Yiliu Liu $^{\mathrm{b}}$ Mary Ann Lundteigen ${ }^{\text {b }}$
${ }^{\mathrm{a}}$ College of Mechanical and Transportation Engineering, China University of Petroleum (Beijing), Beijing, China
${ }^{\text {b }}$ Department of Production and Quality Engineering, Norwegian University of Science and Technology, Trondheim, Norway

Shengnan Wu shengnanwu19@sina.com
Laibin Zhang zhanglb@cup.edu.cn
Wenpei Zheng zhengwenpei@cup.edu.cn
Yiliu Liu yiliu.liu@ntnu.no
Mary Ann Lundteigen mary.a.lundteigen@ntnu.no

# A DBN-based risk assessment model for prediction and diagnosis of offshore drilling incidents 

Shengnan Wu ${ }^{\mathrm{a}, \mathrm{b}}$ Laibin Zhang ${ }^{\mathrm{a}}$ Wenpei Zheng* ${ }^{\mathrm{a}}$ Yiliu Liu ${ }^{\mathrm{b}}$ Mary Ann Lundteigen ${ }^{\mathrm{b}}$<br>${ }^{a}$ College of Mechanical and Transportation Engineering, China University of Petroleum (Beijing), Beijing, China<br>${ }^{\mathrm{b}}$ Department of Production and Quality Engineering, Norwegian University of Science and Technology, Trondheim, Norway


#### Abstract

: Drilling operations of offshore oil and gas fields are characterized by high technical complexity, high risks, and high costs, since they are always in harsh environments with complicated geological factors. Lost circulation or well "kick" is a typically hazardous event that may occur while drilling wells and it also may develop into a blowout accident without being well handled. It is necessary to identify and analyze the root causes of these events and their consequences, in order to prevent serious accidents from happening. In a drilling operation, the risk of blowout may change with time, depending on the operation stage, and such kind of dynamics should be captured in risk assessment. This paper presents an approach for determining the conditional probabilities of hazardous events and their consequences. The approach includes models that take into account the influence of degradation and (if applicable) new real-time information which represents the changing model parameters (such as state change of mud density). Such an approach is based on the Dynamic Bayesian network (DBN) theory and then incorporates additional nodes to address the model uncertainties and parameter uncertainties. In addition, the effect of degradation, which had been ignored in the existing researches, also is taken into account. Given that a hazardous event has occurred, this presented model can be used to predict the risk evolution, as well to reason its root causes during offshore drilling operation. A bowtie model is established to link the potential incident scenarios with the pressure regimes and formation load capacity, and then the model is translated into a DBN. DBN inference is adapted to perform prediction and diagnosis for dynamic risk assessment, and then a sensitivity analysis is carried out to find the relative importance of each root cause. A case study with focusing on lost circulation during three drilling scenarios is adapted to illustrate the feasibility of the proposed approach.


Key words: Dynamic Bayesian network (DBN); drilling incidents; dynamic risk assessment; prediction of risk evolution; root cause reasoning

[^0]
[^0]:    *Corresponding Author.
    E-mail address: zhengwenpei@cup.edu.cn (W. Zheng)

# 1 Introduction 

Drilling into offshore oil and gas fields with high pressure, temperature, $\mathrm{H}_{2} \mathrm{~S}$-gases, and weak formations often meets many challenges, such as narrow drilling fluid density window, multiple pressure systems in vertical direction, and high pressure zones. Drilling operations at such fields are more prone to serious problems (here referred to as drilling incidents), such as lost circulation and uncontrolled influx to well ("kick"), and blowouts (to environment) compared to (less demanding) oil and gas fields. These drilling incidents can result in unplanned downtime (which are costly) or may develop into large accidents, with the potential to cause fatalities, environmental damages, and full or partial loss of drilling facility and well (Crichton et al., 2005; Holland, 1997; Skogdalen et al., 2011). For example, the well-known Macondo blowout that occurred during the last stage of a drilling operation resulted in 11 fatalities and the largest oil spill in the history of offshore oil and gas industry. It is necessary to predict early kick or lost circulation, and then take necessary precautions, so as to avoid such kind of disastrous accidents (Khan and Abbasi, 1999; Skogdalen and Vinnem, 2012).

Kick is the first warning towards a blowout and it is therefore important to detect a kick as early as possible and to implement efficient measures in due time. Mud weight and circulation are the primary barriers to prevent kicks, and lost circulation is an early indication of a kick under development. It is therefore important to direct the attention to avoid and manage this situation. A loss of circulation occurs when the bottom hole pressure in the wellbore is higher than the formation pressure, allowing (or forcing) the drilling fluid to flow into the formation. Several researchers have focused on the effects of lost circulation (Shen, 2015; Yan et al., 2015), and proposed measures to reduce such effects (Sheremetov et al., 2008). In terms of the causes, lost circulation is usually accompanied by wellbore stability problems, damage of reservoir near well bottom and stuck pipe, and these are the main reasons why kick and even blowout can occur as a consequence. Managed pressure drilling (MPD) technology has been developed and widely used to avoid flow of drilling fluid into the formation (Hannegan, 2006; Hannegan \& Fisher, 2005), and the effects of MPD should be included in risk assessments associated with loss of circulation.

Bayesian networks (BNs) is a flexible approach to analyze the effects of risk influencing factors like well conditions and physical measurements. Abimbola et al. (2015) have, for example, proposed a BN-based risk model that considers potential scenarios for different pressure regimes. BNs may be derived from other frequently used models, such as bow-ties (BTs), fault trees (FTs) and event trees (ETs), for example with basis in the BTs, FTs and ETs developed by Khakzad et al. (2013). Bhandari et al. (2015) have applied BN method to investigate different risk factors associated with MPD and underbalanced drilling deep water drilling technologies with respect to blowout accidents. Other approaches for modeling risk also exist: Xue et al. (2013) have proposed a safety barrier-based accident model for blowouts which considers the effects of three-level well control. Ataallahi and Shadizadeh (2015) have introduced Delphi and fuzzy approach into a risk analysis model, and used this model to find the main risk influencing factors in different type of wells.

The main weakness of the mentioned risk assessment approaches is their inability to capture dynamic effects of a drilling operation, such as change of well conditions, occurrence of a new event, and the release of new estimation or measurement for technical state of equipment. FT, ET and BT models which constitute the main elements of most methods presented are not very effective to evaluate the correlations and dependencies between risk influence factors, and the

models cannot be easily updated under changing conditions and handle the uncertainty issues (Khakzad et al., 2011). Models based on BNs have been developed to overcome these modeling deficiencies (Cai et al., 2012), but cannot explicitly treat temporary relationships between model parameters, i.e. account for the fact that relationships of parameters may change from one drilling phase to the next. These limitations have already been resolved by introducing dynamic BNs (DBN) (Cai et al., 2015; Hu et al., 2015). DBNs are built on the basis of BNs, but have additional features that allow the incorporation of events, conditions, and interrelationships that may change over time. Cai et al. (2013) have explored the use of DBN in performance evaluation of subsea blowout preventer (BOP) considering imperfect repair. DBNs have also been used for the same purpose in other industry sectors, such as for monitoring the risk of tunnel-induced road surface damage (Wu et al., 2015) and for studying the risk of life extension of fire water pump (Ramírez and Utne, 2015).

However, what seems to be missing in these mentioned DBN models is the possibility to incorporate the effects of uncertainties on both of model and parameters. Parameter uncertainty may exist due to parameters of conditional probability that are always assumed to be time-invariant (Hu et al., 2011) based on prior knowledge being from existing literature, while model uncertainty may relate to uncertainty about the logical relationship between model parameters. Both of these are relevant in situations where experience is limited and the causal relationship is not well understood. In addition, current DBN based models assume that failure rates are constant (Cai et al., 2013), but in practices mechanical equipment may be subjected to degradation of time as in an ocean environment and most of their failures follow other probability distribution, e.g. Weibull. The main motivation for this paper is therefore to present a new approach to handle the above-mentioned issues by allowing uncertain logical relationships among root causes, integrating parameter uncertainty of prior knowledge, and introducing failure probability distributions with DBN theory. This approach can systematically perform incidents evolution prediction and root cause reasoning for risk assessment using the predictive, diagnostic and sensitivity analysis technology.

The rest of this paper is organized as follows. Section 2 presents three drilling scenarios with the MPD technology. In section 3, the fundamental theory of BN and DBN will be briefly introduced. In section 4, a DBN-based risk assessment model is developed by incorporating some additional nodes to handle the uncertainty issues involving the model uncertainty and relevant parameters' uncertainty and the effect of degradation is also considered for the drilling incidents. The proposed method is applied for incident prediction evolution as well as root cause reasoning regarding lost circulation in the case study of section 5 . Section 6 provides the conclusion and research perspectives of this study.

# 2. Manage pressure drilling (MPD) technology 

MPD is a powerful drilling hazard mitigation technique for offshore drilling and is defined by International Association of Drilling Contractors (IADC) Underbalanced Operations Committee as "an adaptive drilling process used to precisely control the annual pressure profile throughout the wellbore". The aim of MPD is to ascertain the down hole pressure environment limits and to manage the annular hydraulic pressure profile accordingly (Stamnes et al., 2008). An MPD system consists of the following main systems: a rotating control device (RCD), an automated dynamic

annular pressure control (DAPC) system, a backpressure pump, a DAPC choke manifold, a flowmeter (Elliott et al., 2011). RCD is also regarded as first barrier to seal the annulus from drill-string by creating a closed circulation system different from normally open circulation system, and therefore the flow of mud out from the annulus can be controlled by an automated choke. DAPC system is used to maintain the constant bottom hole pressure (BHP) through providing the backpressure on the annulus by continuously adjusting the DAPC chocks and backpressure pump. A flowmeter provides the flow-out data and kick detection is predicted by monitoring flow-in data (Vajargah and van Oort, 2015). MPD drilling techniques include constant bottom hole pressure (CBHP), pressurized mud-cap drilling, and dual gradient drilling (Rehm et al., 2013). The case study selected for this paper focuses on the use of CBHP as a measure to prevent or mitigate drilling hazards, such as differential sticking, lost circulation and kicks, on a development well in a pressurized, fractured basement with narrow downhole environmental limitation. A MPD system can also optimize the rate of penetration, reduce non-productive time and the number of casing strings relative to conventional drilling techniques, and deepen casing set points. The typical offshore MPD system is illustrated in Fig.1.
![img-0.jpeg](img-0.jpeg)

Fig. 1 MPD system (Elliott et al., 2011)

During a drilling operation, it is required to always maintain two functioning well barriers: The primary barrier, which is the active balancing of drilling fluid (i.e. mud) to avoid hydrocarbons escaping from the well, and the secondary barrier, BOP. The BOP mainly consists of BOP control system and BOP stack, used to seal, control and monitor oil and gas wells to prevent blowout, the uncontrolled release of crude oil and/or natural gas from well. The MPD system can be regarded as being part of the primary barrier, as the system applies backpressure control to maintain control with BHP (Patel et al., 2013). The hydrostatic pressure of the drilling fluid column must take into account the correct balance between BHP and formation fracture pressure (FFP).

The formula for determining the BHP (Rehm et al., 2013) varies for different types of drilling operations. Three types of drilling operations have been considered in this paper: not circulating, tripping in, and circulating. When the rig pump is not circulating the drilling fluid, the static BHP is defined as:

$$
\mathrm{BHP}_{\text {static }}=P_{d f c}=\rho_{d} g h+
$$

where $P_{d f c}$ is the hydrostatic pressure of the drilling fluid column, $\rho_{d}$ is the density of drilling fluid and, $g$ stands for gravitational acceleration, $h$ is drilling fluid height, and $P_{b}$ is the backpressure of wellhead.

When the drillstring is tripping in the wellbole, the dynamic BHP is defined as:

$$
\begin{aligned}
& \mathrm{BHP}_{\text {dynamic }}=P_{d f c}+P_{s g} \\
& =\rho_{d} g h+P_{s g} \\
& +P_{b}
\end{aligned}
$$

where $P_{s g}$ is the surging pressure caused by drillstring tripping in the wellbore.
When the rig pump is on and circulating the drilling fluid, the dynamic BHP is defined as:

$$
\begin{aligned}
& \mathrm{BHP}_{\text {dynamic }}=P_{d f c}+P_{f c} \\
& =\rho_{d} g h+P_{f c} \\
& +P_{b}
\end{aligned}
$$

where $P_{f c}$ is the frictional pressure due to pumping the drilling fluid through the drillstring, and $P_{f c}$ is the backpressure of wellhead.

In this paper, the main focus is the control of CBHP to avoid drilling fluid loss. If the MPD system fails to perform this function, the result may be serious, such as differential sticking and lost circulation. Lost circulation does not simply means the loss of a few dollars of drilling mud, but it can be disastrous as a blowout. Drilling crew therefore pays close attention to monitoring of tanks, pits, and flow from the well, to quickly assess and control the lost circulation. This paper studies the causes and effects of lost circulation for the three mentioned, considering the performance of the MPD system and other influencing factors.

# 3 Theoretical basis for Dynamic Bayesian Networks 

This section highlights some selected points about the theories of BNs as well as DBNs.

### 3.1 Bayesian Networks

A Dynamic Bayesian Networks (DBNs) is an extension of a Bayesian Network (BN). A BN combines graph model and probability theory, consisting of a directed acyclic graph (DAG) and an associated joint probability distribution (JPD) (Nielsen and Jensen, 2009). In a DAG, nodes including parent nodes and child nodes represent random variables, and links determine probabilistic dependences between variables. A conditional probability table (CPT) for discrete variables is defined for the relationship among parent nodes to demonstrate marginal probability. Assuming $P a\left(X_{i}\right)$ is the parent node of $X_{i}$, the CPT of $X_{i}$ is denoted by $P\left(X_{i} \mid P a\left(X_{i}\right)\right)$. Therefore, the $\mathrm{JPD}, \mathrm{P}\left(X_{1}, \ldots, X_{N}\right)$, can be rewritten as Eq. (4).

$$
\mathrm{P}\left(X_{1}, \ldots, X_{N}\right)=\prod P\left(X_{i} \mid P a\left(X_{i}\right)\right)
$$

The quantification of probabilities in BNs includes two steps: assigning prior probabilities to the parent nodes, and defining CPT of child nodes by combining priori knowledge. Such knowledge can be from expert judgment, or observations.

### 3.2 Dynamic Bayesian Networks

A DBN extends a BN by introducing relevant temporal dependencies, so as to model the dynamic behavior of random variables (Hu et al., 2011). A DBN consists of a sequence of time slices and temporal links. Each slice represents a static BN to describe variables in the

corresponding time step, and temporal links between variables in different time slices represent a temporal probabilistic dependence. A DBN is able to model probability distribution over semi-infinite collection of random variables. The CPT of each variable in DBN can be calculated independently, facilitating the interpretation of DBN.

In general, there are two assumptions for a DBN construction interconnected time slices of static BNs. Firstly, the system is assumed as the first-order Markovian (i.e., $\mathrm{P}\left(X_{t} \mid X_{1}, \ldots, X_{t-1}\right)=$ $\mathrm{P}\left(X_{t} \mid X_{t-1}\right)$, and secondly the transition probability $\mathrm{P}\left(X_{t} \mid X_{t-1}\right)$ is the same for all the t . Therefore, a DBN can be defined by a pair of $\mathrm{BNs}\left(\mathrm{B}_{1}, \mathrm{~B} \rightarrow\right)$ : where $B_{l}$ is a BN which defines the prior $P\left(X_{l}\right)$, and $B \rightarrow$ is a two-slice temporal Bayesian net (2TBN) that defines the transition and observation models as a product of the CPTs in the 2TBN (Murphy, 2002), as seen in Eq. (5).

$$
\mathrm{P}\left(X_{t} \mid X_{t-1}\right)=\prod_{i=1}^{N} P\left(X_{t}^{i} \mid P a\left(X_{t}^{i}\right)\right)
$$

where

- $X_{t}^{i}$ is the $i^{\text {th }}$ node in time-slice $t$,
- $P a\left(X_{t}^{i}\right)$ denotes the parent of $X_{t}^{i}$, which may be in the same time-slice $t$ or previous time-slice $t-1$, and
- $N$ indicates the number of random variables in $X_{t}^{i}$.

The nodes in the first time-slice of a 2 TBN have unconditional initial state distribution, $\mathrm{P}\left(X_{1}^{1: N}\right)$, while each node in the second time-slice has an associated CPT. Then, for a DBN with $T$ slices, the joint distribution can be obtained by "unrolling" the network as expressed in Eq. (6).

$$
\mathrm{P}\left(X_{1: T}^{1: N}\right)=\prod_{i=1}^{N} P_{B 1}\left(X_{1}^{i} \mid P a\left(X_{1}^{i}\right)\right) \times \prod_{t=2}^{T} \prod_{i=1}^{N} P_{B \rightarrow}\left(X_{t}^{i} \mid P a\left(X_{t}^{i}\right)\right)
$$

Several inference algorithms (Murphy, 2002; Neapolitan, 2004) have been proposed for DBN modeling. In this paper, the forwards-backwards inference and mutual information are used for Bayesian inference. The main benefit of introducing DBN for risk assessment may be summarized as follows:

- All relevant qualitative and quantitative analyses can be carried out in a full probabilistic model, including a broad variety of modeling schemes and a large collection of inference techniques from the BN applied to dynamical process.
- A DBN is more acceptable for predicting values of variables and capable of revealing the system state at any time. At a time slice new information about model parameters may be incorporated into the model, the value of a variable can be calculated based on probabilistic inference. This information may be in the format of:

1) Updated probabilities, updating only on the basis of the associated probability distribution and the elapsed time.
2) Updated probabilities, considering new real-time information, such as a change in a state of a model parameter.
3) A combination of the two above, using Bayesian update.

# 4 Development of a DBN-based risk assessment model 

DBNs and BTs are combined in this paper as the basis to set up a risk assessment model consisting of factors that may lead to drilling incidents, the causal relationship between them, and the effects of measures available to prevent the escalation. The model is used to perform the prediction for occurrence probability of drilling incidents over time and compare risk among the different drilling processes. The overall workflow needed to derive the model and apply it for risk assessment is shown in Fig. 2. As seen in the figure, there are three main steps: Hazard identification, DBN development, and DBN-based risk assessment.
![img-1.jpeg](img-1.jpeg)

Fig. 2. DBN-based risk assessment model for drilling incidents

The particulars of the presenting model are specified as:

- Step 1: A BT model is integrated, so that the cause-consequence chain or causal relationships can be mostly easily identified and foreseen.
- Step 2: Uncertainties on model and parameters related to DBN construction are taken into account. The parameters of CPTs from the previous time to the current time used in the proposed model are assumed both time-variant and time-homogeneous.
- Step 3: Estimation does not only focus on forward analysis, but also dynamics given any events occurring drilling process. In addition, the occurrence probability of a hazardous event or the development trend of its underlying consequence as functions of time will be predicted. The root cause reasoning is discussed given the occurrence of an hazardous event in diagnosis analysis.


### 4.1 Step 1: Hazard identification

A BT model can provide visual explanation of a complete accident scenario evolution and is widely applied in hazard identification and risk analyses (De Dianous and Fiévez, 2006). A simplified BT is shown in Fig. 3 (a), with three main parts: The left side, the middle, and the right side. On the left side is a FT, identifying the causes of an unwanted event (which is placed in the middle), and on the right side there is an ET, identifying the possible outcomes given the effects of mitigating measures.

The following notations will be used in the rest:

- Root causes (RC), the basic events of the FT,
- Intermediate event (IE), which can be substructures of the FT,
- Top event (TE), the unwanted event that is placed in the middle of the BT,

- Safety barriers (SB), mitigation measures to reduce the severity of potential consequences (C).

Once hazards have been identified, the bow-tie model can be applied to further build the causal relationships. This process for hazards identification is considered a difficult task for complex offshore wells, especially the drilling with high temperature and pressure information.
![img-2.jpeg](img-2.jpeg)

Fig. 3. Translating from BT to BN (a) simplified BT model (b) simplified BN model

The detailed steps for hazard identification are explicitly illustrated as follows.
(1) Develop drilling incidents scenarios based on the drilling operations and pressure regime in section 2 .
(2) Collect available safety-based information about influence factors including ocean environment factors, geological factors, drilling technology, and human factors ect., incidents (kick, lost circulation ect.) or underlying consequences (blowout ect.) associated with the drilling operation in question, using the relative standards, literature, accident reports and experts input.
(3) Develop BT based on the FT and ET theory for drilling incidents, and the BT should be reviewed by relevant personnel from operations, maintenance, safety and management, etc.
(4) Describe the explicit causal relationships among the root causes, target incidents and consequences and define the state of each root cause and the corresponding failure data.

But the application of BT in the risk analysis suffers the limitation of updating probability and cannot take uncertainties into consideration (Khakzad et al., 2011). More importantly, because of being composed of static structures such as FT and ET, BT has not widely been recognized in the context of dynamic analysis. To consider dynamic behavior over time, the BT model needs to be transformed into DBN for dynamic risk assessment. The dynamic behavior over time consists of three aspects as follows:

- The evolution tendency of the TE can be predicted over time after the actual evidences

of root causes are collected in different time-slices.

- The occurrence probability of having TE and experiencing corresponding consequences can be predicted given the current status of root causes detected at any time.
- The failure probabilities of any root cause at previous time can be calculated when the status of this cause at current time is detected.


# 4.2 Step 2: DBN development 

### 4.2.1 Mapping BT to BN

The translating algorithm from BT to BN consists of FT mapping and ET mapping (Khakzad et al., 2013). First, the mapping from FT into BN includes a graphical and probability translation based on the previous work (Bobbio et al., 2001). Fig. 3 (b) illustrates the simplified procedure of mapping FT and ET into BN. In this phase, each root cause, intermediate event and top event of FT is translated into a corresponding root node, intermediate event node and top event node of BN, respectively. The nodes of BN are linked in the same way as the corresponding events in the FT. The failure probabilities of the root causes are assigned to the corresponding parents nodes as prior probabilities. The connections between events such as "AND gate" and "OR gate" are translated into corresponding conditional probability tables (CPTs) in BN.

Bearfield and Marsh (2005) present a mapping algorithm from ET into DBN, which includes safety barriers and consequence translation. Each safety barrier of ET is translated into a corresponding barrier node with two states (success and failure) and the consequences of ET are translated into a corresponding consequence node with multiple states as the number of the event tree consequences. The failure probabilities of safety barriers are assigned to the prior probabilities of corresponding barrier nodes. It is noted that the CPTs of the corresponding consequence node are assigned based on the expert judgment.

### 4.2.2 Simplified DBN model development

As the state of the node or the probability of the node e.g. failure is changing over time, a simplified DBN is established by extending the BN formalism within three time-slices from at time $t=0, t=t_{1}$ to at time $t=t_{2}$, as presented in Fig. 4 (a). The time interval is the same between 0 and $t_{1}$ or $t_{1}$ and $t_{2}$. As indicated in Fig. 4 (a), the root nodes RC1, RC2, RC3 and RC4, and barrier nodes SB1 and SB2 are extended from $0^{\text {th }}$ to $t_{1}$ or from $t_{1}$ to $t_{2}$ with inter-slice arcs, respectively. It is noted that the inter relationship over time is not discussed in this paper, and so there are no inter-slice arcs assigned for other nodes except for root nodes and barrier nodes. Each root nodes of DBN can have two states, YES and NO. The state YES denotes that an event or a failure occurs, while NO means that it doesn't occur. IE/TE can take states True or False. The state True and False refers to the IE/TE occur and do not occur, respectively. Each barrier nodes of DBN also involve two states, namely, Success and Failure. The state Success and Failure refers whether or not the barrier is able to carry out its safety function.

![img-3.jpeg](img-3.jpeg)

Fig. 4. Simplified DBN modeling (a) without model uncertainty and (b) with model uncertainty for three time-slices
This proposed model can handle the uncertainty issues involving the model uncertainty and parameters uncertainty.
(1) Modeling uncertainty is necessary due to the lack of the accurate determination of a causal relationship between the nodes and their parents, e.g. the relationship between the nodes RC1 and RC2 cannot completely follow the OR-gate. To handle the model uncertainty, the nodes denoted as MU as shown in Fig. 5 (b) is introduced by modifying its CPT and constant with different time-slices. MU can take the states OR and AND, which refers to the IE follow the OR-gate or the AND-gate. The CPT of IE1 can be assigned as seen Table 1, e.g. $\mathrm{P}(\mathrm{IE} 1=\operatorname{True} \mid \mathrm{RC} 1=\mathrm{YES}, \mathrm{RC} 2=\mathrm{YES}, \mathrm{MU}=\mathrm{OR})=1$.

Table 1 CPT for IE1 node


(2) Parameters uncertainty can be split into the space-based and the time-based ones.

- The space-based parameters uncertainty occurs when linking the root nodes $\left(R_{i}\right)$ to IE nodes $\left(\mathrm{IE}_{\mathrm{i}}\right)$, which is based on the uncertainty of the root causes itself, e.g. the node RC3 and RC4 which represent the formation fracture pressure and formation porosity are influenced by uncertainty effect of geology information for offshore drilling operation. We can handle this uncertainty by using Noisy AND-gate or Noisy OR-gate algorithm (Neapolitan 2004). If we assume that $\mathrm{P}(\mathrm{IE} 2=$ True $\mid \mathrm{RC} 3=\mathrm{YES}, \mathrm{RC} 4=\mathrm{NO})=0.04$ and $\mathrm{P}(\mathrm{IE} 2=$ True $\mid \mathrm{RC} 3=\mathrm{NO}, \mathrm{RC} 4=\mathrm{YES})=$ 0.05 , we can get $\mathrm{P}(\mathrm{IE} 2=\operatorname{True} \mid \mathrm{RC} 3=\mathrm{YES}, \mathrm{RC} 4=\mathrm{YES})=0.088$. The CPT can be got as seen Table 2.

Table 2 CPT for IE2 node


- The time-based parameters uncertainty occurs when linking the root nodes $\left(R_{i j-1}^{i}\right)$ at the previous time $t_{j-1}$ to the root nodes $\left(R_{i j}^{i}\right)$ at the current time $t_{j}$. The CPTs are assumed time-invariant if prior knowledge is usually obtained in accordance with accident statistic and literature reviews, e.g. the occurrence probability of for a specific change in density is $\mathrm{P}\left(R_{t j}^{i}\right)$ which is prior probability and assumed to be constant over time. We assume when the root cause occurs at time $\mathrm{t}-1$, the root cause will not occur at time $t$. It means that the root cause can be adjusted in a perfect state in the current time interval. The CPTs is therefore obtained as shown in Table 3, when $\mathrm{P}\left(R_{t j}^{i}=\right.$ YES $\left|R_{t j-1}^{i}=\right.$ YES $)=0$ and $\mathrm{P}\left(R_{t j}^{i}=\mathrm{NO}\right| R_{t j-1}^{i}=$ $\mathrm{YES})=\mathrm{P}\left(R_{t j}^{i}\right)$.

Table 3 CPT for two time slices


The CPTs are regarded as the time-variant if failures for root causes such as equipment failure and safety barrier failure follow the Weibull distribution. The degradation influence is considered to estimate the parameters of CPTs. If $\mathrm{P}\left(R_{t j}^{i}=\right.$ YES $\left|R_{t j-1}^{i}=\right.$ YES $)=1-\mathrm{e}^{-\left(\lambda t_{j-1}\right)^{\alpha}}$ and $\mathrm{P}\left(R_{t j}^{i}=\right.$ YES $\left|R_{t j-1}^{i}=\mathrm{NO}\right)=1-\mathrm{e}^{-\left(\lambda t_{j}\right)^{\alpha}}$, we have CPTs as listed in Table 4, where $\lambda$ and $\alpha$ denote the scale parameter and shape parameter, respectively.

Table 4 CPT for two time slices with degradation


# 4.3 Step 3:DBN-based risk assessment 

In this step it is proposed to utilize DBN for the three mentioned decision-support scenarios:

- Predictive analysis, meaning to estimate the risk evolution of drilling operation over time and forecast development in the risk of a drilling operation given the current state of knowledge.
- Diagnostic analysis, meaning to detect and investigate the most likely causes of a drilling incident using backward analysis when the top event occurs.
- Sensitivity analysis, meaning to check to what extent the results of the predictive or diagnostic analysis is influenced by specific parameters which are regarded as uncertain.


### 4.3.1 Predictive analysis

Predictive analysis aims to predict the future risk evolution tendency of drilling operation over time and forecast development in the risk of a drilling operation given the current state of knowledge, using the forward inference technical in DBN. The occurrence probability distribution of a top event at time $t$ under the combination of root causes $\left(R_{t}^{1}, \cdots R_{t}^{i}\right)$ and the occurrence probability distribution of the corresponding consequence (C) under the combination TE and safety barriers $\left(B_{t}^{1}, \cdots B_{t}^{i}\right)$. The state of each root cause or safety barrier is treated as input by CPTs into DBN model. Probability distribution of $\mathrm{TE} / \mathrm{C}$, represented by $P\left(T E_{t}=t e\right) / P\left(C_{t}=c\right)$, is calculated by Eq. (7) and Eq. (8).

$$
\begin{gathered}
P\left(T E_{t}=t e\right)=P\left(T E_{t}=t e \mid I E_{t}^{1}=i e_{1}, \cdots, I E_{t}^{i}=i e_{j}\right) \\
\times P\left(I E_{t}^{1}=i e_{1}, \cdots, I E_{t}^{i}=i e_{j}, R_{t}^{1}=r_{1}, \cdots, R_{t}^{i}=r_{j}\right)
\end{gathered}
$$

where, te stands for the state of a top event $T E_{t} ; i e_{j}$ stands for the state of intermediate event $\mathrm{IE}_{t}$ and $r_{j}$ stands for the state of root nodes $R_{t}^{i} ; P\left(T E_{t}=t e \mid I E_{t}^{1}=i e_{1}, \cdots, I E_{t}^{i}=i e_{j}\right)$ refers to the conditional probability distribution of $T E_{t}$; and $P\left(I E_{t}^{1}=i e_{1}, \cdots, I E_{t}^{i}=i e_{j}, R_{t}^{1}=r_{1}, \cdots, R_{t}^{i}=r_{j}\right)$ refers to the joint probability distribution of $I E$ nodes and root nodes.

$$
\begin{gathered}
P\left(C_{t}=c\right)=P\left(C_{t}=c \mid T E_{t}=t e, B_{t}^{1}=b_{1}, \cdots, B_{t}^{i}=b_{j}\right) \times \\
P\left(T E_{t}=t e\right) \times P\left(B_{t}^{1}=b_{1}, \cdots, B_{t}^{i}=b_{j}\right)
\end{gathered}
$$

where, $c$ stands for the state of consequence $C_{t} ; b i$ stands for the state of root nodes $B_{t}$; $P\left(C_{t}=c \mid T E_{t}=t e, B_{t}^{1}=b_{1}, \cdots, B_{t}^{i}=b_{j}\right)$ refers to the conditional probability distribution of $C_{t}$; and $P\left(B_{t}^{1}=b_{1}, \cdots, B_{t}^{i}=b_{j}\right)$ refers to the joint probability distribution of barrier nodes.

The risk of a drilling operation given the occurrence of root causes $\left(R_{t}^{m}=r_{m}\right)$, represented by $P\left(T E_{t}=t e \mid R_{t}^{1}=r_{1}, \cdots, R_{t}^{m}=r_{m}, \cdots, R_{t}^{i}=r_{j}\right)$, can also be calculated by Eq.(9)

$$
\begin{gathered}
P\left(T E_{t}=t e \mid R_{t}^{m}=r_{m}\right)=P\left(T E_{t}=t e \mid I E_{t}^{1}=i e_{1}, \cdots, I E_{t}^{i}=i e_{j}\right) \\
\times P\left(I E_{t}^{1}=i e_{1}, \cdots, I E_{t}^{i}=i e_{j}, R_{t}^{1}=r_{1}, \cdots, R_{t}^{m}=r_{m}, \cdots, R_{t}^{i}=r_{j}\right)
\end{gathered}
$$

where, $P\left(T E_{t}=t e \mid I E_{t}^{1}=i e_{1}, \cdots, I E_{t}^{i}=i e_{j}\right)$ refers to the conditional probability distribution of $T E$; and $P\left(I E_{t}^{1}=i e_{1}, \cdots, I E_{t}^{i}=i e_{j} R_{t}^{1}=r_{1}, \cdots, R_{t}^{m}=r_{m}, \cdots, R_{t}^{i}=r_{j}\right)$ refers to the joint probability distribution of IE nodes and root causes given the occurrence of root causes $\left(R_{t}^{m}=\right.$

$r_{m}$ ).
Generally, $P\left(T E_{t}=t e\right), P\left(C_{t}=c\right)$ or $P\left(T E_{t}=t e \mid R_{t}^{m}=r_{m}\right)$ can serve as an indicator to evaluate the risk, providing the basis for decision makers to take proper measures.

# 4.3.2 Diagnostic analysis 

Diagnostic analysis aims to obtain the posterior probability distribution of each root causes when a TE occurs at certain time, which is performed through backward analysis of DBN. The underlying causes with the largest occurrence probability or the occurrence probability above the acceptable safety level can then be detected by means of posterior probability distribution, reminding engineers to pay more attention for these causes. Posterior probability distribution of root nodes $R_{t}^{i}$, represented by $P\left(R_{t}^{i}=r_{i} \mid T E_{t}=t e\right)$, can be calculated by Eq. (10).

$$
P\left(R_{t}^{i}=r_{i} \mid T E_{t}=t e\right)=\frac{P\left(T E_{t}=t e \mid R_{t}^{i}=r_{i}\right) \times P\left(R_{t}^{i}=r_{i}\right)}{P\left(T E_{t}=t e\right)}
$$

Normally, $R_{t}^{i}$ is more likely to become the key root cause at time $t$ leading to the occurrence of a TE when $P\left(R_{t}^{i}=r_{i} \mid T E_{t}=t e\right)$ is close to 1 .

### 4.3.3 Sensitivity analysis

Sensitivity analysis, meaning to check to what extent the results of the predictive or diagnostic analysis are sensitive to specific parameters regarded as uncertain. The important degree of root cause to the top event can be analyzed by applying Shannon's mutual information (entropy reduction), which is one of the most commonly used measurement for ranking information sources (Kjærulff and Madsen, 2006). The mutual information is the total uncertainty-reducing potential of R, given the original uncertainty in $R_{i}$ prior to consulting $R_{j}$. Intuitively, mutual information can measure how much knowing one of these variables reduces our uncertainty about the other. The mutual information of $R_{i}$ and $R_{j}$ is given by:

$$
I\left(R_{i}, R_{j}\right)=-\sum_{i} \sum_{j} P\left(R_{i}, R_{j}\right) \log \frac{P\left(R_{i}, R_{j}\right)}{P\left(R_{i}\right) P\left(R_{j}\right)}
$$

where $P\left(R_{i}, R_{j}\right)$ is the joint probability distribution function of root cause $R_{i}$ and $R_{j}$, and $P\left(R_{i}\right)$ and $P\left(R_{i}\right)$ is the probability distribution of root cause $R_{i}$ and $R_{j}$, respectively.

### 4.4 Validation of the model

Validation for a newly-develop model is a significant process of checking whether it will provide a reasonable amount of confidence to meet its specification and produce the required results in a sound, defensible and well-grounded way. It seems to become an impractical exercise to gather the all monitored data to perform a fully comprehensive validation for a newly-develop model because it ideally requires to cover the complete range of possibilities. The validation in this paper is carried out from the following aspects:

- Validation of model development process means to verify the model to be constructed in a reasonably, defensibly and realistically way.
- Validation of model usability means to check sensitivities of results by modeling the change of inputs data by three-axiom-based validation method by Jones et al. (2010).
- Validation of model results means to evaluate the results generated from a

developed model involving model parameters inputs, and make the result more reasonable by a comparison with that of another approach such as fault tree and static Bayesian network using existing data.

1) The proposed model is developed based on a Bowtie model illustrated in Fig. 3 that is also used for translating to meet the requirement for dynamic risk assessment. Examination of development process, illustrated in Fig. 4, consists of checking both effect of uncertainty and degradation. As an example, it is not clear whether the relationship between RC1 and RC2 follows rule of OR-gate or AND-gate and what kind of effect it will bring. The effect of uncertainty on model and parameters is therefore to be checked by comparing results from the model without MU nodes and results from the model with MU nodes by taking probabilities range of OR-gate $[0,1]$. The comparison results, seen as in Fig. 5, reveal that the occurrence probability of the top event will be revised from $1.9 \times 10^{-3}$ to $3.61 \times 10^{-2}$ given every root cause taking the initial probabilities 0.1 in YES state under not considering effect of parameter uncertainty, while that will be changed from $9 \times 10^{-5}$ to $1.7 \times 10^{-3}$ under considering that. The validation for degradation effect given MU nodes probabilities $(0.3,0.7)$ is carried out by comparing the occurrence probability not taking degradation effect into account (time-invariant CPT) with excluding the degradation effect (time-variant CPT) as listed as in Table 3 and Table 4. The results (seen as in Table 5) also indicate that the occurrence probability of the top event will change slightly former and increase later. The change of occurrence probability can be explained reasonably due to the consideration of the causal relationship and parameters uncertainty and degradation effect.
![img-4.jpeg](img-4.jpeg)

Fig. 5 Comparison of occurrence probability for MU nodes with OR-gate probabilities
Table 5 Comparison of occurrence probability for degradation


2) Validation of model usability as illustrated in Fig. 4, is to check whether sensitivities of results by modeling parameters inputs is expected. At the initial time, the prior probabilities for all root causes are set to 0.1 , and probability of MU nodes is taken by $(0.3,0.7)$. When the probabilities of root causes including $\mathrm{RC} 1, \mathrm{RC} 2, \mathrm{RC} 3$, and RC 4 are set to 1 in sequence and keep the probability of MU nodes constant, the occurrence probability of the top event will gradually increase from $5.7 \times 10^{-4}$ to $3.3 \times 10^{-3}, 9 \times 10^{-3}$, $4.48 \times 10^{-2}$ and $8.8 \times 10^{-2}$, respectively. The exercise of increasing the failure probability of each root cause one after another will meet the axiom specification and produce the required results, thus giving a partial verification to the newly-developed model.
3) The results have been validated by the special case with "lost circulation" in not circulating scenario using the existing partial data seen as Fig. 6 (a). The results from the fault tree (FT), BN with average probability failure on demand (PFDavg) (Rausand, 2014) and DBN with probability failure on demand (PFD(t)) and PFDavg (Rausand, 2014) are compared for a period with 4 time slices, which is seen as in Table 6. The basic event with these of the occurrence probability is listed as Table 7 and Table 8. The results has indicated that the magnitude of occurrence probabilities almost keep the same. The difference of results between FT and BN is caused by the uncertainty issues, while that between BN and DBN can be explained by the effect of degradation. This part can make the final results from the newly-developed model more reasonable.


# 5 Case study 

A case study for an offshore well related to lost circulation is carried out in this section. An offshore drilling well in BD oil and gas field in Madura is considered as the equipment under protection. The highest wind events (thunderstorms) will result in maximum wave heights that are relatively small according the statistics. The sea condition is therefore relatively safe in this selected area. The interface of the target oil and gas reservoir pressure is approximately 8090 psi , which is equivalent to the pressure coefficient 1.68 , and formation temperature is about $151.7^{\circ} \mathrm{C}$, belonging to the high-temperature and high-pressure system. Lost circulation or kick is more likely caused by these special geological conditions such as the very light gray and low-density limestone reservoir with narrow drilling fluid density window. Therefore, the MPD technology is adapted in this application.

### 5.1 Risk identification for lost circulation

A BT model is firstly developed for risk identification of lost circulation in the three drilling scenarios. Fig. 6 shows the fault tree and event tree of lost circulation in BT model. Considering well lost circulation as an undesired event among such drilling incidents, the potential causes and

consequences have to be determined. As indicated in Fig. 6 (a), (b) and (c), three fault trees are established for modeling different drilling operations involving not circulating, tripping in and circulating process. The root causes of lost circulation are collected and investigated. According to the section 2, the overbalanced drilling condition is likely to result in the loss of mud. As drilling encountering limestone and fissures formation, the likelihood of lost circulation will be increased. So, two main reasons could be identified including the larger BHP than FFP and the leakage path. The increasing BHP and the MPD system failing to maintain a constant BHP will make the larger BHP than FFP possible. The others leading to lost circulation may include excessive drilling fluid density in not circulating process, the surging effect caused by tripping activities and high pump pressure in circulating process. The formation condition and well structure design can also be taken into consideration in terms of the contribution to the lost circulation. Therefore, totally 21 potential root causes in fault tree was found based on the work of Fuh et al. (1992), Skogdalen and Vinnem (2012) and Abimbola et al. (2015).

Safe operation, collapse stuck, kick and blowout as potential consequences are emphasized for a weak formation as depicted in Fig. 6 (d). To forestall the occurrence of these consequences, three safety barriers are installed: plugging barrier, kick detection system and BOP system. Plugging barriers should be used when massive volume of drilling mud into the formation is losing. The successful plugging plays a critical role in reducing the downtime loss and preventing the wellbore collapse and pipe sticking through the utilizing of plugging materials, tools and a series shut or kill operations. Kick detection system has the function to detect the occurrence of kick if the plugging fails to control the loss of mud. The BOP system can prevent the formation fluid into external environment and it will be highlighted when kick cannot be detected and controlled.

![img-5.jpeg](img-5.jpeg)
(b)

![img-6.jpeg](img-6.jpeg)
(d)

Fig. 6. BT model for (a) fault tree of Not circulating, (b) fault tree of Tripping in and (c) fault tree of Circulating (d) event tree

# 5.2 DBN modeling for the case 

The DBNs for drilling lost circulation in this study are established using Netica (2015) software that is regard as a general platform to realize risk assessment in a fast way. According to the mapping algorithm described in Section 4.2.1, BTs of "lost circulation" combining the root causes and consequences for three drilling operations are translated into corresponding DBNs with three time-slices as presented in Fig. 7, which is extended from time at $t=0^{\text {th }}, t=720^{\text {th }}$ to $t=1440^{\text {th }}$ hour for modeling.

![img-7.jpeg](img-7.jpeg)
(a)

![img-8.jpeg](img-8.jpeg)
(b)

![img-9.jpeg](img-9.jpeg)
(c)

Fig. 7 DBN modeling with three time-slices for different drilling scenarios (a) Not circulating (b) Tripping in and (c) Circulating

It is noted that model uncertainty issues can be handled by adding the MU node with two states "OR" and "AND" in the proposed DBN-based model. The states of root/IE nodes, TE nodes and barriers nodes are assigned "YES/NO", "True/False" and "Success/Failure" respectively, as indicated in Fig.7. Similarly, consequence states are achieved from "safe operation to blowout" according to the availability and reliability performance of safety barriers. The CPTs of nodes considering the parameters uncertainty should be assigned to model the DBNs. In the initial time at $t=0$, the value of the prior probability needs to be assigned to each state of root nodes. If the prior knowledge of root causes such as UDDFD and IDFH is obtained by taking advantage of the available literature (Abimbola et al., 2014; Holland, 1997; Participants, 2002) and also the expert inputs if necessary, the prior probabilities of these root causes are assigned as listed in column 4 of Table 7. If the probabilities of failure on demand for the equipment and safety barriers such as

RCDFS and BOPS are assumed to follow the Weibull distribution, the initial states of these root causes are considered in their perfect functioning state, and the value of failure probability is assigned to 0 . The values of scale parameter $\lambda$ and shape parameter $\alpha$ in Weibull distribution are provided in Table 8, and such values are determined by the expert's inputs.

Table 7 Prior and posterior probability for root causes


Table 8 Parameters of Weibull distribution


The parameters of CPTs should also be assigned to model DBNs. The approach of CPTs calculation considering the parameters uncertainty is following the discussion in section 4.2.2. There are two examples to illustrate the space-based parameters of CTPs and two examples to explain the time-based parameters of CPTs, respectively. Taking the "DAPC fail to control" as example, the occurrence of this event is caused by the DAPC system failure, back pressure pump failure and DAPC choke failure. With the use of Boolean logic relationships, the CPTs can be calculated as listed in Table 9. Taking the "NLPF" as example, the CPT is calculated from the nodes "NMF" and "PFLC" to the node "NLPF" based on experts knowledge and Noisy-OR filling-up algorithm in this study, as presented in Table 10. The presence of NLPF is caused by NMF and PFLC in the YES state at respective probability of 0.02 and 0.05 , but not 1 due to the effect of uncertainty. The time-based CPTs, namely the CPTs for two time-slices of root causes follow the rules as depicted in Table 3 and Table 4. Taking the "UDDFD" as example, the prior probability of UDDFD is 0.05 , and the CPT is assigned as listed in Table 11. Taking the "BPPF" as example, the failure probability of BPPF is 0.07 and 0.014 at $\mathrm{t}=720^{\text {th }}$ and $\mathrm{t}=1440^{\text {th }}$ hour respectively, and the CPT is assigned as listed in Table 12.

Table 9 CPT for DAPCFC


Table 10 CPT for NLPF


Table 11 CPT of UDDFD for two time slices


Table 12 CPT of BPPF for two time slices


# 5.3 Results and discussion 

### 5.3.1 Risk evolution prediction

Fig. 7 shows DBNs modeling results for the three drilling scenarios contributing to lost circulation within three time-slices. The predictive results indicate that the occurrence probability of lost circulation at time $\mathrm{t}=720^{\text {th }}$ hour and at time $\mathrm{t}=1440^{\text {th }}$ hour for not circulating, tripping in and circulating scenario is $7.0 \mathrm{E}-05,7 \mathrm{E}-05$ and $8 \mathrm{E}-05$, and $2.2 \mathrm{E}-04,2.4 \mathrm{E}-04$ and $3.3 \mathrm{E}-04$, respectively. Fig. 8 (a) shows the risk comparison for three drilling scenarios and tendency of the risk evolution within 9 time-slices. We assume that the time slice interval is the same as 360 hours. It is clear that the occurrence probability of lost circulation is highest and is growing fastest in the scenario of circulating process, which means that lost circulation is much more likely to occur in circulating process when the rig pump is on. Compared to the static operation, dynamic operations is more vulnerable due to the effect of the surging pressure and the annual friction pressure. In addition, the reliability of wellhead back pressure control is decreasing over time and it has a great effect on the occurrence probability of lost circulation. Dynamic operation and the reliability of wellhead back pressure control therefore needs to be paid more attention when drilling.

![img-10.jpeg](img-10.jpeg)

Fig. 8 Risk comparison for (a) three drilling scenarios and (b) different time-slices given mud density change

When drilling encounters the formation with the narrow mud density window, the small change of mud density will have a great impact on the occurrence of lost circulation. Fig. 8 (b) shows the occurrence probability of lost circulation at the different time (at $3^{\text {rd }}$ time-slice, $4^{\text {th }}$ time-slice and $7^{\text {th }}$ time-slice) given the mud density in abnormal state in circulating scenarios. It is clear that the occurrence probability of lost circulation increases fast given the unreasonable change of mud density at $3^{\text {rd }}$ time-slice, $4^{\text {th }}$ time-slice and $7^{\text {th }}$ time-slice and will decrease at their next time-slice. The occurrence probability of lost circulation increases from $1.8 \times 10^{-4}$ to $2.6 \times 10^{-3}$ when the mud density changed at $3^{\text {rd }}$ time-slice. According the assumption in Section 4.2.2, when $\mathrm{P}\left(U D D F D_{\mathrm{f}}=\right.$ YES $\left|U D D F D_{\mathrm{f}-1}=\right.$ YES $)=0$, the occurrence probability of lost circulation decreases from $3.3 \times 10^{-4}$ to $1.4 \times 10^{-4}$ at $4^{\text {th }}$ time-slice given the mud density changed at $3^{\text {rd }}$ time-slice. The ratio is largest at $7^{\text {th }}$ time-slice compared that of $3^{\text {rd }}$ time-slice and $4^{\text {th }}$ time-slice. As a matter of fact, the drilling well goes exactly through more narrow density window as the depth is

growing over time, and the $7^{\text {th }}$ time-slice is mostly considered as dangerous period during the drilling progress. The likelihood of lost circulation can be estimated with the unreasonable change of mud density.

The blowout may happen at the same time when drilling is encountering the weak formation with gas-layers. The occurrence probability is mostly close to 0 in Fig. 7 due to the lower probability of the lost circulation and failure of safety barriers. Based on the failure of safety barriers following the Weibull rules, the reliability of barriers is decreasing along with time. Taking the circulating scenarios as example, their consequence probabilities when lost circulation occurs are calculated starting from collapse stuck to blowout as shown in Fig.9. Hence, collapse stuck has the higher likelihood than other consequences. Plugging barrier should be therefore given more concern to meet high level reliability. It is also worth noting that there is a small change for kick and blowout in occurrence probability because of the higher reliability of kick detection barrier and BOP barrier in the whole drilling.
![img-11.jpeg](img-11.jpeg)

Fig. 9 Risk comparison of its consequences for different time-slices given lost circulation occurrence

# 5.3.2 Root cause reasoning 

Assuming the occurrence of lost circulation for three drilling scenarios by $1440^{\text {th }}$ hours by setting the state of lost circulation node to True, a diagnostic analysis is conducted. The prior and posterior probabilities of these root causes for not circulating, tripping in and circulating scenarios are listed in column 4 and column 5 of Table 7, which indicate updated failure probability available given the occurrence of lost circulation from backward propagation. The comparison of prior probabilities and posterior probabilities by using the ratio as presented in Fig. 10 shows that the posterior probabilities are more than 10 times as much as their prior probabilities. In the above diagnostic analysis using DBN probability inference algorithm, the critical roles of drilling fluid density should be highlighted because the ratio of UDDFD (1) is the largest. It is worth noting that the root causes such as UDDFD (1) and RDCD (15) which would have been totally dominating as other factors in causing lost circulation in three scenarios. The other main contributing factors identified are LRPO (20) and HPP (22) in circulating process. Therefore the practical diagnosis and checking should then focus on the availability of these root causes until the high risk is controlled in real time.

![img-12.jpeg](img-12.jpeg)

Fig. 10. Ratio of Posterior probability ( P (posterior)) and prior probability ( P (prior)) in (a) Not circulating
(b) Tripping in and (c) Circulating

The occurrence probability of lost circulation at current time can be calculated by the proposed model when the loss of circulation occurred at previous time. Taking the circulating scenario as example, the occurrence probability of lost circulation (LC) at time $\mathrm{t}=1440^{\text {th }}$ given the LC occurred at time $t=720^{\text {th }}$ is calculated, namely $P\left(L C_{t=1440 t h}=\right.$ Ture $\left|L C_{t=720 t h}=\right.$ True $)=$ 0.00009 , which become lower than that $(0.00033)$ of LC at time $\mathrm{t}=720^{\text {th }}$. There is a change for root cause (RC) state between at time $\mathrm{t}=720^{\text {th }}$ and $\mathrm{t}=1440^{\text {th }}$, the $P\left(R C_{t=720 t h}=\right.$ YES $\left|L C_{t=720 t h}=\right.$ True $)$ becomes larger and $P\left(R C_{t=1440 t h}=\right.$ YES $\left|R C_{t=720 t h}=\right.$ YES $)$ become smaller based on the Eq. (10) and Eq. (6), as shown in Fig. 11 (a) and Fig. 11 (b). As a result, the posterior probabilities can provide new evidential information for diagnosis analysis, and the values of root causes can be updated in a dynamic manner.
![img-13.jpeg](img-13.jpeg)
(a)

![img-14.jpeg](img-14.jpeg)

Fig. 11 Prior probability ( P (prior)) and posterior probability ( P (posterior)) of root causes at time (a) $\mathrm{t}=720^{\text {th }}$ and (b) $\mathrm{t}=1440^{\text {th }}$

# 5.3.3 Sensitivity analysis 

Importance factors degree sequence of root causes for lost circulation is also calculated by using mutual information, which can measure the information that two variables share and how much uncertainty about one variable is reduced by knowing the other. The individual contribution of each root cause towards lost circulation at time slice $\mathrm{T}=4$ is calculated by comparing three drilling scenarios as shown in Fig. 12(a). It is seen that, for three types of operations, UDDFD (1) contributes much to the lost circulation, which is regard as the most fatal weakness. In Fig. 12(a), UDDFD (1) in not circulating scenario has a higher contribution for lost circulation comparing with other scenarios, whereas RCDFS (4), BPPF (6), NMF (9), and RDCR (15) in circulating scenario also have higher contributions than those of other scenarios.

The individual contribution of each root cause to lost circulation in circulating scenarios is calculated under the different time slices $\mathrm{T}=1, \mathrm{~T}=4$ and $\mathrm{T}=9$, as shown in Fig. 12(b). It is found that, UDDFD (1) and RCDFS (4) at time slice $\mathrm{T}=1$, UDDFD (1) at time slice $\mathrm{T}=4$ and RCDFS (4) at time slice $\mathrm{T}=9$ make the highest contribution to the lost circulation, which indicates that these root causes are sensitive to the lost circulation and should be given more attention. In Fig. 12(b), the value of mutual information at time slice $\mathrm{t}=9$ has a higher contribution for lost circulation comparing with other time slices, such as UDDFD (1), BPPF (6), NMF (9), and RDCR (15). Therefore, the different root causes should be highlighted at different time of drilling.

![img-15.jpeg](img-15.jpeg)

Fig. 12. Sensitivity analysis of root causes for (a) different scenarios and (b) different time-slices

# 6 Conclusions and research perspectives 

This paper focuses on the safety of drilling operations given the special geological conditions, where the MPD technology which is adopted to avoid the drilling incidents. According to the close relationship between hazard factors and the dynamic variance of bottom hole pressure during drilling, a risk assessment model based on DBN for predict analysis, diagnostic analysis and sensitivity analysis is proposed.

The application of the proposed model has been presented with a case study on the offshore lost circulation during drilling. In order to provide graphical symbols for the logical causal relationship between factors and effect of lost circulation, a BT model is establish to map different drilling operation scenarios. All potential root causes contributing to lost circulation and the corresponding possible outcomes identified given the occurrence of this incident are analyzed carefully. Then the DBN is established from the BT. Finally by the inference mechanism of DBN,

the risk evolution tendency of drilling operations can be predicted comparing the not circulating, tripping in and circulating scenarios over time and given the current state of root causes. The root cause reasoning and the development trend of underlying consequence are discussed given the occurrence of lost circulation in diagnostic analysis. The most important root causes have been identified with sensitivity analysis on the basis of mutual information for different drilling scenarios and different time. The occurrence probability is highest in the scenario of circulating, which indicates that lost circulation is much more likely to occur in this process. Drilling fluid density and availability of rotating control device have made the highest contribution to the lost circulation for this scenario, and they may for this reason be regarded as the most important weaknesses to give attention.

The direction of our subsequent work is to extend our model to improve the robustness of probability distribution of root causes from the prior knowledge by logging data and apply the method to other oil and gas operations such as production and overwork.

# Acknowledgment 

This research is partly carried out with the Reliability, Availability, Maintainability and Safety (RAMS) group at Norwegian University of Science and Technology (NTNU), and it is supported by the Project (YXKY-2015-ZY-12) of Drilling and completion technology research from China National Offshore Oil Corporation Research Center. The authors are grateful for the reviewers' helpful comments.
