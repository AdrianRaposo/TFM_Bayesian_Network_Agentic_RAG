# Safety Analysis of plugging and abandonment of oil and gas wells in uncertain conditions with limited data 

Ahmed O. Babaleye ${ }^{\mathrm{a}}$, Rafet Kurt ${ }^{\mathrm{a}}$, Faisal Khan ${ }^{\mathrm{b}, *}$<br>${ }^{\text {a }}$ Department of Naval Architecture, Ocean and Marine Engineering, University of Strathclyde, Glasgow, United Kingdom<br>${ }^{\text {b }}$ Centre for Risk, Integrity and Safety Engineering (C-RISE), Faculty of Engineering and Applied Science, Memorial University of Newfoundland, St. John's, NL, Canada A1B 3X5<br>*Correspondence author: fikhan@mun.ca


#### Abstract

Well plugging and abandonment are necessitated to ensure safe closure of a non-producing offshore asset. Little or no condition monitoring is done after the abandonment operation, and data are often unavailable to analyze the risks of potential leakage. It is therefore essential to capture all inherent and evolving hazards associated with this activity before its implementation. The current probabilistic risk analysis approaches such as fault tree, event tree and bowtie though able to model potential leak scenarios; these approaches have limited capabilities to handle evolving well conditions and data unavailability. Many of the barriers of an abandoned well deteriorates over time and are dependent on external conditions, making it necessary to consider advanced approaches to model potential leakage risk. This paper presents a Bayesian network-based model for well plugging and abandonment. The proposed model able to handle evolving conditions of the barriers, their failure dependence and, also uncertainty in the data. The model uses advanced logic conditions such as Noisy-OR and leaky Noisy-OR to define the condition and data dependency. The proposed model is explained and tested on a case study from the Elgin platform's well plugging and abandonment failure.


Keywords: Bayesian network; Decommissioning; Plugging and abandonment; Well barrier failure

# 1. Introduction 

The ultimate goal of a plugged and abandoned well is to provide permanent containment of the formation fluids migrating from the reservoir to the seabed. Many of these hydrocarbon-containing reservoirs have unknown characteristics during the end-of-life phase. The geological forces within the wellbores can vary from layer-to-layer with devastating consequence. These uncertainties make leakage route of the oil and/or gas wells complex and unpredictable. The leakage of hydrocarbon can be initiated through a compromised well barrier either by degradation overtime or natural seepage, or both. Also, little or no condition monitoring of the abandoned wells can lead to eventual failure of the well. The failure of one barrier can lead to subsequent failure of surrounding barriers, leading to cascading of failures until the formation fluids reach the mudline.

Many accidents emanating from plugging and abandonment operations have been recorded, some of which resulted in the release of oil or gas in enormous quantities. For example, on 15 October 2016, the plugging and abonnement (P\&A) operation in the G-4 well of the Troll Field on the Norwegian Continental Shelf (NCS) operated by Statoil, failed and was classified by highest degree of severity. As reported by Statoil (2017), noncompliance with procedures was the primary cause of the leakage of oil, gas and flammable liquids. Primary barriers capable of being displaced by internal fluids pressure were installed instead of deep-set plugs. On 25 March 2012, the Elgin well plugging, and abandonment operation failed to lead to an uncontrollable gas release to the seabed. The well was successfully killed after seven weeks of the leak with remediation cost of over $\$ 2.09 \mathrm{~m}$ and accumulated loss of around $\$ 109 \mathrm{~m}$ (Total, 2013). The failure was attributed to a unique corrosion event in the casings within the wellbore. One common challenge in both cases is that the complete knowledge of the uncertainties associated with decommissioning, especially, plugging and abandonment of wells, is lacking. Also, the sequence of occurrence of these hazards leading to well failure is not entirely known, making the application of Boolean logic gates such as AND/OR insufficient in estimating the exact risk value. Therefore, a safety methodology capable of addressing these concerns is essential to enable the prediction of leakage probability with consequent reduction of risk.

The analysis of accident scenarios is characterized by risk (Khan, 2001) and all probabilistic risk assessment (PRA) tools such as fault tree analysis (FTA), event tree analysis (ETA), Layer of Protection Analysis (LOPA) and bowtie (BT) aim at analyzing the safety and reliability of systems. However, these methods are limited in their ability to assess and accommodate dynamic variations in complex engineering systems such as a reservoir. Forms of probabilistic risk assessment have been developed to assess accidents scenarios and events sequence modelling. For example, Sklet (2006) investigated hydrocarbon release accidents on offshore platforms using barrier block diagrams. Nivolianitou et al. (2004) compared fault trees, event trees and Petri nets for investigating accidents in an ammonia storage plant. The work examined the sequence of events leading to failure, event dependencies, and appropriate modelling considerations. Gowland (2006) used the layer of protection analysis process in the ARAMIS project to assess the sequence of operation of safety barriers. Delvosalle et al. (2005) developed a bowtie to identify significant and interacting accident scenarios in process plants application. Paltrinieri et al. (2013) introduced a dynamic approach to atypical scenarios identification (DyPASI) to identify and assess early signals of risk related to past events as the development of bow-tie identification technique.

Although, few types of research have been conducted to assess the safety risks of well P\&A (Kaiser, 2017; Ouyang and Allen, 2017). However, most of these previous works have focused on data mining or on pilot experiments to describe the well characteristics whereas no consideration was given to data uncertainty and events dependencies. Also, most of the probabilistic risk analysis (FTA, ETA, and BT) techniques applied to the previous studies cannot flexibly adapt to new information, or handle uncertain data including the dependencies of events (Pasman and Rogers, 2013; Pasman et al., 2009). FTA as a risk analysis tool, albeit its drawbacks, has been widely applied in diverse fields to estimate the safety risks and reliability of mooring systems (Mentes and Helvacioglu, 2011), complex process systems (Ferdous et al., 2009, 2007; Khan et. al. 2001), and fault diagnoses of industrial processes (Bartlett et. al. 2009; Kavcic and Juricic, 2001; Khoo et. al. 2001). Where interacting basic events are few, FTA can be solved with ease. Whereas, FTA cannot cope with complex and overly dependent systems, redundant failures or common cause failures by itself unless additional information is incorporated with the model. Furthermore, each basic event in a fault tree (FT) model is often assumed to be statistically independent, but in practice, events are interactively dependent (Khakzad et al. 2011; Simon et al. 2007; Bobbio et al. 2001). Many researchers have developed different forms of FTA to cope with these drawbacks. For example, Markowski et al. (2009) applied fuzzy and evidence theory to account for data uncertainty from expert judgements and similar accidents. Shalev and Tiran (2007) developed a methodology for dynamic FTA by coupling FTA with condition monitoring. A complete framework to conduct qualitative and quantitative risk analysis within temporal FTA were developed by Kabir et al. (2015) and Walker and Papadopoulos (2009). This temporal FTA was applied to capture temporal dependence among faults and events by Palshikar (2002). Lefebvre et al. (2007) extended the temporal FTA model to include time dependency among failures for avionics applications. Although, these methods aim at updating static FTAs to cope with dynamic safety analysis; however, none of the proposed methods is capable of independent analysis without adding additional gate(s) to the existing FTA.

To improve these limitations, Bayesian network (BN) have been adopted by researchers in recent times due to its flexible nature and capability to assess risks under uncertainty. BN has been demonstrated to thrive in fault diagnosis (Huang et. al. 2008; Przytula and Thompson, 2000), reliability assessment (Wilson and Huzurbazar, 2007; Langseth and Portinale, 2007; Mahadevan et. al., 2001) and probability updating (Boudali and Dugan, 2005; Giribone and Valette, 2004). FTAs have been mapped into BNs in different forms with the primary goal of relaxing its limitations. For instance, static FTAs have been mapped into BNs (Marsh and Bearfield, 2007; Simon et. al., 2007; Graves et. al. 2007; Bobbio et.al. 2001), and dynamic FTAs into DBNs, accordingly (Boudali and Dugan, 2005; Montani et. al. 2008). BNs also offer superior multivariable handling ability. However, a significant amount of computation is required to represent dependencies among the interacting events. This drawback can only be addressed with the help of advanced logics such as Noisy-OR (N-OR) and leaky Noisy-OR (LN-OR), which have not been applied in the risk analysis of well P\&A until now.

The present work focuses on the application of advanced modelling logics (N-OR and LN-OR) for estimating the leakage probability of formation fluids during P\&A operation. This is achieved through the mapping of P\&A FTA into BN and incorporating the N-OR and LN-OR logics in the

model to obtain significant improvement in the level of uncertainty. Following this introduction, Section 2 presents a brief description of FT, BN, mapping of FT into BN and the N-OR/LN-OR logics. An application of the methodology is presented as a case study in Section 3. Model description emanating from the case study is offered and analyzed in Section 4 while Section 5 is dedicated to the conclusions drawn from the study.

# 2. Proposed Safety methodology 

### 2.1 Dynamic safety model

### 2.1.1 Fault tree (FT)

The FT is a deterministic, deductive and graphical technique capable of estimating the probable cause or combination of causes of an undesired top event (TE) and their criticalities. Typically, the top event is the major accident that can initiate hazards especially, when the safety barriers implemented are insufficient or deteriorate over time. To develop the FT, the top event must be recognized and identified. The common events (IEs) leading to the top event are then systematically categorized in a top-down approach until the causal events (CEs) are identified. It is worth mentioning that, the complete knowledge of the process operation and the failure rate (or frequency/probability) of the CEs must be known. The CEs are the minimum faults that can initiate a potential fault or harm to the subsystems of a component. The IEs are sets of faults in the subsystem capable of causing a potential accident. The analysis of an FT can be performed both qualitatively and quantitatively. For qualitative analysis, algebraic equation containing the combinations of CEs as independent variables is developed regarding TE, based on Boolean logic. In the quantitative analysis, the occurrence probabilities or the minimum cut-sets (MCs) of the CEs are used to obtain the occurrence probability of the TE.

The static nature of FT is based on its application domain where every component of a system is believed to be either reliable or non-reliable over time. The FT model formulation does not take into consideration the possibility of a reliable system degradation when subject to operation. Also, FT can only handle binary logic operations without the possibility of accommodating intermediate states (Khakzad et al. 2011; Rausand and Høyland, 2004). For these reasons, this paper relies only on the logical representation of the accident model within FT and all computation are performed within BN. Furthermore, uncertain conditions coupled with limited data can be problematic for FT analysis. Some modifications have been developed to address these concerns such as fuzzy set and evidence theory (Lavasani et al. 2015; Yuhua and Datao, 2005).

### 2.1.2 Bayesian network

BN is a probabilistic tool capable of handling multi-variable systems and their dependencies under uncertainty. BN consists of a directed acyclic graph (DAG) used to represent events. The nodes within the DAG represent variables, and the arcs denote the causal relationships amongst the connected nodes. The relationships between these variables are specified within conditional probability tables (CPT) to indicate the strength of influence among the interacting nodes. Consider Fig. 1 with a set of variables $Y_{i} Y_{1}$ and $Y_{2}$ are root nodes; $Y_{3}$ and $Y_{4}$ are the intermediate nodes, and $Y_{5}$ is the leaf node. The root nodes corresponding to CEs in an FT are assigned marginal prior probabilities. The intermediate and leaf nodes are given CPTs based on the level of influence

of their parent nodes. The theory and practice of BN is not the focus of this present paper but its applicability to the task under consideration. Comprehensive information regarding BN can be found in the literature (Bobbio et al., 2001; Jensen and Nielsen, 2007).

Binary outcomes $y_{i}$ and $\bar{y}_{i}$ represent each state $Y_{i}$. The BN, joint probability distribution, follows the chain rule as given in Eq. 1.

$$
P\left(y_{i}\right)=\prod_{i=1}^{5} P\left(y_{i} \mid y_{j e(i)}\right)
$$

Where $P\left(y_{i}\right)$ is the joint probability distribution of the state variables $y_{i} \cdot \mu(i)$ is the parent of variable node $i$. Eq. 1 can be expanded according to the chain rule as:

$$
P\left(y_{i}\right)=P\left(y_{5} \mid y_{4}, y_{3}\right) \cdot P\left(y_{4} \mid y_{2}, y_{1}\right) \cdot P\left(y_{3} \mid y_{1}\right) \cdot P\left(y_{2}\right) \cdot P\left(y_{1}\right)
$$

Eq. 2 can be extended to accommodate the large but finite number of variables with a combination of states, making BBN well suited to handle complex and nonlinear systems. Given the availability of new evidence, $E$ the posterior (updated) probabilities of Fig. 2 can be obtained by:

$$
P\left(y_{i} \mid E\right)=\frac{P\left(E, y_{i}\right)}{P(E)}
$$

![img-0.jpeg](img-0.jpeg)

Figure 1. Generic BN model.

# 2.1.3 FT to BN Mapping algorithm 

The causal, intermediate and top events of the FT are transformed to the BN structure to represent its root, intermediate and leaf (or pivot) nodes, respectively. The logic relationship among the interacting events in the FT is assigned similarly to the interacting nodes within the BN (Fig. 2). The failure prior probabilities of the causal events become the marginal prior probabilities of the root nodes. The probabilities assigned to the intermediate and leaf nodes are based on the logic gates relationship of the FT and are specified within the CPTs of the BN depending on the degree of belief or knowledge of the new observations.

![img-1.jpeg](img-1.jpeg)

Figure 2. FT to BN mapping technique.

# 2.2 Modelling interactions with advanced logic 

In the decommissioning operation, cost reduction is one of the major concerns. For this reason, it is necessary to model the accident scenarios accurately such that the cost of implementing safety measures is not over- or under-estimated. The logic gates of AND and OR utilized by FT are sometimes not enough to predict the actual scenarios, leading to a conservative analysis of risk. To overcome this notion, Noisy-OR and leaky Noisy-OR gates are explored.

### 2.2.1 Noisy-OR Formalism

N -OR gate is a canonical model used to describe the interactions between the causes of accidents and their corresponding common effect. The underlying principle of this type of gate assumes that any causal element is independently capable of influencing the common effect even if other causes are absent. In other words, the typical consequence can only be initiated given that at least one of the causal elements is accurate and unhindered. Noisy-OR model offers the advantage of reducing the number of conditional probabilities required to represent dependencies among interacting variables since only the actual causes alone are specified. Consider Fig. 1, the probability of node 5 with state $y_{5}$ given the occurrence of any of the causes $y_{3}$ and $y_{4}$ will yield a $n$ ( $n=2$ parameters in this case, with each state of the parameters either true " $y_{i}$ " or false " $\bar{y}_{i}$ ") conditional probabilities. This can be expressed mathematically as:

$$
\begin{gathered}
P\left(y_{5} \mid y_{4}, y_{3}\right)=P_{4} \cdot P_{3} \\
P\left(y_{5} \mid y_{4}, \bar{y}_{3}\right)=P_{4} \\
P\left(y_{5} \mid \bar{y}_{4}, y_{3}\right)=P_{3} \\
P\left(y_{5} \mid \bar{y}_{4}, \bar{y}_{3}\right)=0
\end{gathered}
$$

Typically, if all causes and their common effect are false, then the outcome probability is unity. In general, the probability of $y$ given subset $k$ when $y_{i}$ is instantiated is expressed as:

$$
P(y \mid k)=1-\prod_{i: y_{i} \in k}\left(1-P_{i}\right)
$$

The advantage offered by the Noisy-OR model is observed from the considerable decrease in the number of conditional probabilities required to represent the cause-consequence relationship within the CPT completely.

# 2.2.2 Leaky Noisy-OR Formalism 

The LN-OR gate is an extension of the N-OR model. It is used to address scenarios where a consequence still exists even in the absence of any cause. This model is especially applicable to accident models where all potential causes are not identified. In practice, most risk identification model falls short to capture hazards specific to a scenario, in its entirety, making the Noisy-OR with leak model an essential precision risk analysis tool. The principal argument is that there exists a leak (common cause) probability $l$, which describes the overall consequence of all causes not captured in the event of an accident (Onisko et al., 2001; Jensen and Nielsen, 2007; Bobbio et al., 2001). Fig. 1 can demonstrate the applicability of the common cause probability, $l$ where $0 \leq l<1$ , such that $P\left(y_{5} \mid \bar{y}_{4}, \bar{y}_{3}, L\right)=l$. Here, $L$ is the uncaptured cause of the occurrence of $y_{5}$, and Eq. 6 can be rewritten to accommodate this extra term, thus,

$$
P(y \mid k)=1-\left[(1-l) \prod_{i: y_{i} \in k}\left(1-P_{i}\right)\right]
$$

Eq. 6 demonstrates that even if all the components of an accident model are actively operational, the consequence can still occur due to a common cause or leak.

## 3. Application of methodology

### 3.1 Case study - Failure sequence description

The failure of the well P\&A, characterized by the leakage of hydrocarbon to mudline, is described based on physical inspection of the wellbore schematics as contained in the Minerals Management Service (MMS) report (2000). A permanently abandoned well schematics representing the migrating fluid and leakage route is shown in Fig. 3. To maintain the integrity of a permanently abandoned well, two critical barriers (the zone isolation plug, $\mathrm{B}_{1}$ and the lower casing plug, $\mathrm{B}_{2}$ ) must not be compromised. The performance of the surface casing $\left(\mathrm{B}_{4}\right)$ depends on the proper functioning of plugs $B_{1}$ and $B_{2} . B_{1}$ can be initiated or exacerbated by the effect of fluids pressure buildup $\left(B_{1.1}\right)$ or injection from nearby producing wells $\left(B_{1.2}\right)$. Following the failure of $B_{4}$, the migrating fluid can flow unhindered through the hanger or seal assembly $\left(\mathrm{B}_{5}\right)$ or the conductor casing $\left(\mathrm{B}_{6}\right)$. The leaked fluids or gas may flow within the annulus of the conductor and surface casings through the hanger assembly $\left(\mathrm{B}_{7}\right)$. Compromised $\mathrm{B}_{4}$ may also allow the passage of fluids past the surface plug $\left(\mathrm{B}_{3}\right)$ to the mudline as shown in Fig. 3.

![img-2.jpeg](img-2.jpeg)

Figure 3. Permanently abandoned well: (a) Schematics (b) Leak route (MMS, 2000).

# 3.2 Fault tree analysis 

Based on the failure sequence description, the TE is defined as the leak through the permanently abandoned well to the mudline. The causal events and corresponding intermediate events are used to construct the FT as shown in Fig. 4. The occurrence probability of the CEs obtained as failure rate from OREDA (2015) and Woodyard (1982), although not entirely sure, are presented in Table 2. The uncertainty analysis and measures to improve the safety of the well through advanced logic is the focus of this study and will be demonstrated in subsequent sections.

### 3.2.1 Estimating the leakage probability

The occurrence probability of the TE can be estimated based on the Boolean logic governing the FT and the CEs probabilities in Table 2. Following this, the safety critical CEs and the minimal cut-sets $\left(\mathrm{MC}_{\mathrm{S}}\right)$ capable of causing the occurrence of the TE can be determined. The occurrence probability of each MC is first calculated in the form;

Table 1. Failure probabilities of leak causal events (OREDA, 2015; Woodyard, 1982).



$$
P\left(M C_{j}\right)=\bigcap_{i \in M C_{j}} P\left(y_{i}\right)
$$

Where $P\left(M C_{j}\right)$ is the occurrence probability of $j$ th minimal cut-set; $P\left(y_{i}\right)$ represents the causal event occurrence probability in the $j$ th minimal cut-set. The MCs represent the contribution of all causal events to the occurrence of the top event failure, given that they occur independently. The occurrence probability of the TE can then be expressed regarding the MCs as;

$$
\begin{gathered}
P(T E)=P\left(M C_{1} \cup M C_{2} \cup M C_{3} \cup \ldots \cup M C_{n}\right) \\
T E=M C_{1}+M C_{2}+M C_{3}+\ldots+M C_{n}=\cup_{j=1}^{n} M C_{j}
\end{gathered}
$$

Where $P(T E)$ represent the occurrence probability of the top event; $P\left(M C_{j}\right)$ is the occurrence probability of the $j$ th MCs, and $n$ is the number of MCs of the FT. Based on the MCs values presented in Table 3 obtained from Eq. (7), the occurrence probability of the top event, using Eq. (8) yields 2.39E-05 for non-sour well (and 1.80E-04 for sour well).

# 3.2.2 Safety-critical event analysis 

To ascertain the strength of influence of each CE , it is important to rank the MCs according to the number of combinations of the causal events. As seen in Table 3, the minimum order is three while the maximum is 5 . It follows that the critical (weakest or shortest) path leading to the leakage of hydrocarbon through the mudline is 3 . Also, the measure of importance $\left(I M^{V F}\right)$ of the calculated MCs can provide valuable decision support for the safety of the abandoned well. The $I M^{V F}$ adopted in this study is based on the Vesely-Fussell approach given by;

$$
I M^{V F}=\frac{P\left(M C_{j}\right)}{P(T E)}
$$

From Eq. 9, the most probable cause of the top event occurrence is calculated and ranked as shown in Table 3. The most critical of these MCs are $M C_{1}=B_{1.1} B_{2} B_{3}$ with $I M_{j}^{V F}=0.8996$. This value indicates that Pressure buildup within the wellbore, leak through the lower plug and eventual leak through the upper plug are the most probable causes for the release of hydrocarbon through the mudline. The constituent events of $M C_{1}$ require the largest resources to control. Generally, the order of resource allocation is $M C_{1}>M C_{2}>M C_{3}>M C_{4}>M C_{5}>M C_{6}$. It is worth observing that the occurrence probability of each causal event is the initial (or prior) values, hence, Eqs. (7), (8) and (9) yield prior occurrence of minimal cut-sets, prior occurrence TE probability and prior importance measures, respectively. Also, the data used to analyze the case study is limited and uncertain. Therefore, this work adopts BN to validate the data while N-OR and LN-OR relaxation formalisms are used to model the deviations from uncaptured causes of well P\&A failure.
![img-3.jpeg](img-3.jpeg)

Figure 4. FT model for permanently abandoned well.

Table 2. Failure probabilities of MCs for non-sour well.



# 3.3 Bayesian network analysis 

### 3.3.1 Model validation with BN

Through the mapping technique discussed in section 2.1.3, the developed FT is transformed into its corresponding BN (Fig. 5) to cope with uncertain conditions and limited data. The BN is modelled and analyzed with HUGIN 8.6 (2018). It is important to note that a similitude mapping of the FT, where all the causal events are assumed independent, yields similar occurrence probability as those obtained in the FTA. The BN analysis is performed by defining the CPTs of the intermediate and leaf nodes as binary (i.e. leak/no leak), and the TE prior occurrence probability is $2.39 \mathrm{E}-05$, the same value as obtained in the FTA.
![img-4.jpeg](img-4.jpeg)

Figure 5. BN model for permanently abandoned well failure.
However, BN can help validate the degree of belief in the obtained results through prognostic or diagnostic propagations. In the prognostic analysis, BN can yield varying but promising results depend on the conditional dependencies that exist among causal events. Here, one or more of the CEs occurrence probabilities can be instantiated to obtain new and up-to-date information about the occurrence of the TE. In the diagnostic analysis, the TE occurrence probability can be set as evidence to provide updated information about the CEs, accordingly. Also, the availability of

accident precursor data during the well $\mathrm{P} \& \mathrm{~A}$ operation can be directly fed into the BN to perform probability updating and sequential updating (adaptation). This information can help to update the knowledge of the inherent risks and evolving ones in real-time. Although, the aim of probability updating within BN is to reduce data uncertainty, primarily, because the updated probabilities are believed to be a better reflection of the well $\mathrm{P} \& \mathrm{~A}$ failure when compared to the prior probabilities. However, two important issues relating to BN modelling is that the size of the CPTs and model parameters. The size of CPTs, typically, increases exponentially as the number of finite parent variables rises. Also, the model parameters are associated with own uncertainties as expert judgements can be quite subjective. This study, therefore, adopts N-OR and LN-OR within the BN to address these concerns.

# 3.3.2 $\underline{\text { Noisy-OR analysis }}$ 

The N-OR approach is used to relax the model parameters based on the explanation in Section 2.2.1. Since the occurrence of the TE relies on the leak through the isolation plug, lower plug and upper plug-production casing failures. The number of parameters needed to model the TE is shown in Table 3. $P_{f}$ and $\left(1-P_{f}\right)$ are the noisy occurrence (and non-occurrence) probability of the TE. The introduction of the N-OR formalism within the BN yields a prior occurrence probability of TE as $2.19 \mathrm{E}-3$ for non-sour well.

Table 3. CPT for the leak through mudline failure with the N-OR approach.


### 3.3.3 Leaky Noisy-OR analysis

For the sake of simplicity, an uncaptured hazard in the case of LN-OR is introduced with a leak probability, $l=0.01$. The prior occurrence probabilities of the root nodes are unchanged, except that the next nodes leading to the top event are linked with an LN-OR condition and their interactions reflected in the TE's CPT. The model parameters are assigned as explained in section

2.2.2 and are presented in Table 4. The introduction of the LN-OR formalism within the BN yields a prior occurrence probability of TE as $8.55 \mathrm{E}-3$ for non-sour well.

Table 4. CPT for the leak through mudline failure with the LN-OR approach.


# 3.4 Dynamic safety analysis 

### 3.4.1 Prognostic analysis

In prognostic (forward propagation) analysis within BN, some knowledge of the causal events is gathered and feed into the BN to investigate their influence on the top event. This modelling can provide up-to-date information about the current state of the leakage potentials. For example, instantiating the occurrence probabilities of causal events $P\left(B_{1.1}\right)=P\left(B_{3}\right)=P\left(B_{5}\right)=1$. The BN can then be reassessed using $P\left(B_{1.1}=\{T\}, B_{1.2}=\{F\}, B_{2}=\{F\}, B_{3}=\{T\}, B_{4}=\{F\}, B_{5}=\{T\right), B_{6}$ $=\{F \mid\{T E\}$. The posterior occurrence probability of the leak through mudline (TE) is seen to be higher than the priors in both the similitude mapping of FTA, N-OR and LN-OR cases (Table 5).

Table 5. The posterior probability of TE for non-sour well based on forwarding propagation.


### 3.4.2 Diagnostic analysis

In diagnostic (backward propagation) analysis within BN, the desired information meaningful to decision-makers offshore are the updated (posterior) probabilities, reflecting the specific features of the accident under investigation and, the most probable causes (MPCs) of well P\&A failure. To determine the posterior probabilities of the CEs, a new observation of the overall leak through

mudline is necessary. For instance, given that it becomes certain that the well P\&A fails, the occurrence probability of the TE is instantiated to unity, i.e. $P($ leak thru mudline $)=1$. The updated failure probabilities of the CEs are then reassessed using $P\left(C E_{i} \mid T E=\{T\}\right)$. The results obtained from the FTA, N-OR and LN-OR logics modelled through BN are presented in Table 6, show that events $\mathrm{B}_{1.1}, \mathrm{~B}_{1.2}, \mathrm{~B}_{2}$ and $\mathrm{B}_{3}$ have the largest posterior occurrence probabilities in all cases. To estimate the MPCs, the weakest routes among interacting events are assessed where all the identified largest causal events are assumed to be true while other events are false i.e. $P\left(B_{1.1}\right.$ $=\{T\}, B_{1.2}=\{T\}, B_{2}=\{F\}, B_{3}=\{T\}, B_{4}=\{F\}, B_{5}=\{F\}, B_{6}=\{F\} \mid T E=\{T\})$. The values of the MPC computation when ran through different relaxation approaches yield up-to-date top event probabilities of $1.00 \mathrm{E}+00,2.37 \mathrm{E}-05$ and $2.40 \mathrm{E}-05$, respectively.

Table 6. Failure probabilities comparison of CEs based on backward propagation.


# 3.4.3 Sensitivity analysis 

To examine in more detail how small changes in the causal events influence the overall leak probability of the hydrocarbon to mudline (TE), sensitivity analysis, $\eta_{s}$ is conducted for both cases involving sour- and non-sour fluids within the wellbore. First, the data shown in Table 6, are used to compare the prior and posterior probabilities under all the relaxation conditions (Fig. 6). Then, Eq. 10 is used to compute the contribution of each CE to provide an informed decision on the sensitivity of each event to the well ultimate failure (Fig.7). Furthermore, the sensitivity analysis is validated by repetitive substitution of the posterior occurrence probabilities within BN to provide up-to-date information on the uncertainty, as shown in Fig. 8. For each increment, the updated TE occurrence probability of the TE is recorded.

$$
\eta_{s}\left(B_{i}\right)=\frac{\vartheta\left(B_{i}\right)-\theta\left(B_{i}\right)}{\theta\left(B_{i}\right)}
$$

Where $\vartheta\left(B_{i}\right)$ and $\theta\left(B_{i}\right)$ are the posterior and prior probabilities for nodes $B_{i}$. The trends obtained from the sensitivity analysis are depicted in Fig. 6.

![img-5.jpeg](img-5.jpeg)

Figure 6. Comparison between prior and posterior probabilities (non-sour).
Fig. 7 indicates that it is important to focus on the criticality of events based on sensitivity analysis, rather than simply comparing the magnitudes of posterior against prior probabilities.
![img-6.jpeg](img-6.jpeg)

Figure 7. Sensitivity analysis of causal events (non-sour).
A closer examination of Fig. 8 revealed that events $B_{2}$ (leak through the lower casing plug) and $B_{3}$ (leak through surface plug), albeit their progressive increment with the top event, overlap. This indicates that updating their probabilities repetitively produce similar outcomes. The effect of an injection into nearby wells $\left(\mathrm{B}_{1.2}\right)$ tend to increase steadily as the leak through mudline becomes imminent. To a lesser degree, the leak through seal assembly $\left(\mathrm{B}_{5}\right)$ and that between the annulus of the conductor and surface casing $\left(\mathrm{B}_{7}\right)$ rise with the top event. Leak through the surface casing $\left(\mathrm{B}_{4}\right)$ and leak through the conductor casing $\left(\mathrm{B}_{6}\right)$ are not sensitive to the occurrence of the top event, as evident by Fig. 6.

![img-7.jpeg](img-7.jpeg)

Figure 8. Sensitivity analysis of CEs to TE update probability (non-sour).

# 4. Results and Discussion 

From the fault tree analysis of the causal events, it can be inferred that the critical leakage route to the well $\mathrm{P} \& \mathrm{~A}$ failure is $\mathrm{B}_{1.1} \mathrm{~B}_{2} \mathrm{~B}_{3}$ with a combined failure probability of $2.15 \mathrm{E}-3$ leading to an overall top event failure probability of $2.39 \mathrm{E}-5$, in the case of non-sour oil or gas well. The sequence of occurrence of this route is not as important as the significance of damage their combination would contribute to the accident. It is worth observing that $\mathrm{B}_{1.2} \mathrm{~B}_{2} \mathrm{~B}_{3}$ leakage route also has a higher potential to lead to the accident and must, therefore, be equally controlled. Although the minimal cut-sets provide valuable knowledge about the critical leakage route, it, however, does not explicitly imply that an uncaptured causal event is capable of causing the leak of hydrocarbon to the mudline. This, therefore, justifies the adoption of BN and more importantly, the N-OR and LN-OR relaxation techniques. Furthermore, by comparing the top event failure for both sour and non-sour reservoirs, it is observed that wells with sour fluids yield a higher probability of failure. This is mainly due to their higher corrosion rates within the wellbore and tendencies to present severe safety risks.

In line with the introduction of N-OR and LN-OR, the occurrence probability of the leak of hydrocarbon through the mudline is seen to increase progressively. For instance, running the BN modelled through N-OR logic yield a leak through mudline occurrence probability of 2.19E-3 resulting from a pressure buildup of the migrating fluid failure probability of $1.65 \mathrm{E}-1$, leak through lower plug failure probability of $1.30 \mathrm{E}-2$, and leak through the upper plug and production casing failure probability of $1.01 \mathrm{E}-2$. The N -OR appeared to produce occurrence probabilities relatively lesser than those obtained from a logical OR-gate and more substantial than the logical AND-gate, hence, provides a middle-bound value. A comparison between the FTA and the BN models yield a $90.45 \%$ increased failure probability for the N-OR and $99.72 \%$ for the case of LN-OR. The LN-

OR, therefore, yields an upper-bound value when compared with either FTA or N-OR. It can be concluded that both advanced logics (N-OR and LN-OR) help to significantly reduce the level of uncertainty associated with limited data in modelling the probability of leakage through the mudline and its potential accident scenarios. However, these advanced logics also do not consider the uncertainties in their modelling parameters. For instance, the modelling assumption is such that an event can only be binary (i.e. true/false), but in practice, the unknown parameter should take into account the possibility of an event being true and/or false (i.e. true or false) at the same time, a concept termed ignorance level.

As noted from Fig. 6, leak through the surface plug $\left(B_{3}\right)$ is the most sensitive event to the occurrence of the plugging and abandonment failure. To a lesser extent is the leak through the lower casing plug $\left(B_{2}\right)$, migrating fluids' pressure buildup $\left(B_{1.1}\right)$ and possible injection into a nearby well $\left(B_{1.2}\right)$. It is worth observing that the failure of either $B_{1.1}$ or $B_{1.2}$ is enough to trigger the leak through the isolation plug $\left(B_{1}\right)$. This result is in agreement with those obtained from the MCs in the FTA analysis, particularly because each event is modelled and assumed to be independent within the BN. Another trend established by the presented results is that the prior and posterior probabilities cannot by themselves give an accurate risk value, hence, the need for sensitivity analysis.

# 5. Conclusion 

This study developed an FT to represent the failure of a permanently abandoned oil and gas well. The FT was mapped into its corresponding BN to address the issues associated with static features of an FT to cope with complex time-dependent operations within the offshore decommissioning environment. Advanced relaxation strategies such as Noisy-OR and leaky Noisy-OR logics are considered to obtain realistic failure probability of hydrocarbon leak through the mudline and handle the elicitation of complex interactions within the conditional probability tables. The proposed BN model focused on the uncertainty associated with unknown reservoir characteristics and limited data dictated by expert judgements and uncaptured hazards during the plugging and abandonment planning stage. Fault tree analysis has continued to be a preferred quantitative risk analysis method in offshore structures reliability and risk estimation, due to its ability to provide a detailed overview of the complex systems. However, it is unable to handle time-dependent events and those operations requiring nonlinear interactions and dependencies among causal events. To this end, BN is proposed due to its flexible makeup, and its capabilities to update the occurrence probabilities of both causal events and the top event. BN yielded similar results as the FT in cases where events are assumed to be independent. Performing prognostics and diagnosis analyses, the leak through the surface plug is observed as the most probable cause of well P\&A failure.

It is observed that wells with sour fluids yield a higher probability of failure compared to non-sour fluid wells. This is mainly due to higher corrosion rates within the wellbore. It presents severe safety risks. Based on the preceding, the results support the argument about the need to focus on the criticality of events based on sensitivity analysis, rather than how large or small the posteriors are than the prior probabilities. This study has provided insight into the dynamic safety analysis of plugging and abandonment operations in the event of uncertain reservoir conditions and limited data. Future studies may include the dependencies among interacting events; cascading of failure

due to compromised integrity of the well; adoption of imprecise relaxation strategies to address the uncertainties associated with existing relaxation parameters.

# Acknowledgement 

The authors acknowledge the funding provided by the John Blackburn Main fellowship through IMarEST, United Kingdom; Engineering the Future fellowship and Department of Naval, Ocean and Marine Engineering at the University of Strathclyde. Author Faisal Khan thankfully acknowledges the financial support provided by the Natural Science and Engineering Council of Canada and the Canada Research Chair (CRC) Tier I Program.
