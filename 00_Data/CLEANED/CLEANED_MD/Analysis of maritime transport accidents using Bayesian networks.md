# LJMU Research Online 

Fan, S, Yang, Z, Blanco-Davis, E, Zhang, J and Yan, X
Analysis of maritime transport accidents using Bayesian networks
http://researchonline.ljmu.ac.uk/id/eprint/12523/

## Article

Citation (please note it is advisable to refer to the publisher's version if you intend to cite from this work)

Fan, S, Yang, Z, Blanco-Davis, E, Zhang, J and Yan, X (2020) Analysis of maritime transport accidents using Bayesian networks. Proceedings of the Institution of Mechanical Engineers, Part O: Journal of Risk and Reliability. ISSN 1748-006X

LJMU has developed LJMU Research Online for users to access the research output of the University more effectively. Copyright © and Moral Rights for the papers on this site are retained by the individual authors and/or other copyright owners. Users may download and/or print one copy of any article(s) in LJMU Research Online to facilitate their private study or for non-commercial research. You may not engage in further distribution of the material or use it for any profit-making activities or any commercial gain.

The version presented here may differ from the published version or from the version of the record. Please see the repository URL above for details on accessing the published version and note that access may require a subscription.

For more information please contact researchonline@ljmu.ac.uk

# Analysis of maritime transport accidents using Bayesian Networks 

2 Shiqi Fan ${ }^{1,2,4}$, Zaili Yang ${ }^{4}$, Eduardo Blanco-Davis ${ }^{4}$, Jinfen Zhang ${ }^{2,3}$, Xinping Yan ${ }^{1,2,3 *}$<br>${ }^{3}$ School of Energy and Power Engineering, Wuhan University of Technology, China<br>${ }^{4}$ Intelligent Transport Systems Research Centre (ITSC), Wuhan University of Technology, China<br>${ }^{5}$ National Engineering Research Centre for Water Transport Safety (WTSC), MOST, Wuhan, China<br>${ }^{6}$ Liverpool Logistics, Offshore and Marine (LOOM) Research Institute, Liverpool John Moores<br>7 University, Liverpool, UK<br>*Corresponding Author e-mail: xpyan@whut.edu.cn (X. Yan)<br>*Permanent Address: Y125 mailbox, Yujiatou Campus, Wuhan University of Technology, 1178 Heping

10 Avenue, Wuchang District, Wuhan City, P. R. China, 430063

11 Abstract: A Bayesian Network-based risk analysis approach is proposed to analyse the risk factors influencing maritime transport accidents. Comparing with previous studies in the relevant literature, it reveals new features including 1) new primary data directly derived from maritime accident records by two major databanks Marine Accident Investigation Branch (MAIB) and Transportation Safety Board of Canada (TSB) from 2012 to 2017, 2) rational classification of the factors with respect to each of major types of maritime accidents for effective prevention, and 3) quantification of the extent to which different combinations of the factors influence each accident type. The network modelling the interdependency among the risk factors is constructed by using a Naïve Bayesian Network (NBN) and validated by sensitivity analysis. The results reveal that the common risk factors among different types of accidents are ship operation, voyage segment, ship type, gross tonnage, hull type, and information. Scenario analysis is conducted to predict the occurrence likelihood of different types of accidents under various situations. The findings provide transport authorities and ship owners with useful insights for maritime accident prevention.

24 Keyword: Maritime safety, Accident analysis, Risk factors, Bayesian networks

# 1. Introduction 

Waterborne transportation accounts for approximately $90 \%$ of the world trades in volume, representing one of the essential transportation modes in ensuring the prosperity of internatioanl tarde and global economy. Maritime accidents reveals new features in the past years. According to the 'Safety and Shipping' Annual Report of $2017{ }^{1}$, published by Allianz Global Corporate \& Specialty, there is more than a quarter of ship losses in 2016 occurred in the South China, Indochina, Indonesia and Philippines regions. Although the number of maritime casualties has declined over years, there is increasing complexity of navigation risk exposed in the shipping industry (e.g. high demand on human reliability in complicated operations introduced by advanced technologies). A study of the onboard duties and offboard entities involving Greek-flagged ships during 1993-2006 indicated that $57.1 \%$ of all accidents were attributed to human element ${ }^{2}$. Among them, $75.8 \%$ of accidents were detected onboard, and $80.4 \%$ of the onboard human-induced accidents were related to errors and violations of the ships' masters. There are numerous reasons for an individual to make errors, which may include communication failure, ineffective training, memory lapse, inattention, poorly designed equipment, exhaustion or fatigue, situation ignorance, noisy working conditions, and other personal and environmental factors (e.g. Fan, Zhang ${ }^{3}$ ). The questionnaire survey on maritime operations conducted by Safahani ${ }^{4}$ emphasised the nontechnical skills: $75 \%$ stated that a team leader should discuss the work plan with his/her teammates; $90 \%$ thought that monitoring the task provided an essential contribution to effective team performance; almost everyone in the survey believed that communication was a significant factor, and that teams who do not communicate effectively would increase the possibility of making errors. Branch, House ${ }^{5}$ disclosed that watchkeeper manning levels and a master's ability to discharge his duties were significant factors

# 46 influencing collisions and groundings. 

47 Studies on maritime accident analysis rely on the discretional context and experts' knowledge to extract the causal relations among the process of accidents, as well as data-driven methodologies. Specifically, casual relations were connected to one type of accidents through accident analysis methods, specifically for grounding or collision ${ }^{6-8}$. Moreover, some studies focused on the probability or the frequency of maritime accidents. Fabiano, Currò ${ }^{9}$ investigated the occupational accident frequency affected by the organisation, job experience, and productivity. Pristrom, Yang ${ }^{10}$ estimated the likelihood of a ship being hijacked in the Western Indian or Eastern African region by using the Global Integrated Shipping Information System (GISIS) database together with expert judgement. Other studies concentrated on the severity or the consequence of maritime accidents. Zhang, Teixeira ${ }^{11}$ predicted the accident consequences in the Tianjin port by statistical analysis of historical accident data. Wang and Yang ${ }^{12}$ analysed the key risk factors influencing waterway accident severity by using Bayesian Networks (BN). In addition, some studies investigated the combination of the above two (i.e. likelihood and consequence) ${ }^{13,14}$. However, few studies have been carried out to investigate the issues on how risk factors affect maritime accident types, leaving a research gap to fulfil for effective accident prevention. The key factors contributing to collisions are quite different from those resulting in groundings. In addition, understanding differentiation among the key factors contributing to different types of accidents will help generate useful insights for rational risk control measures.

64 This study aims at investigating how different risk factors generate, in an individual or combined manner, an impact on different types of maritime accidents in terms of likelihood. Manual case by base analysis of recorded maritime accidents from Marine Accident Investigation Branch (MAIB) and Transportation

67 Safety Board of Canada (TSB) that occurred from 2012 to 2017 is undertaken to develop a primary database to support this study, as they are among the most representative from the literature ${ }^{15-17}$. A BNbased approach is proposed to analyse accident types in maritime transport. To do so, the rest of the paper is structured as follows. The literature review on risk factors associated with maritime transport and BNbased risk analysis is conducted and presented in Section 2. Section 3 describes the methodology of Risk

Influence Factors (RIFs) identification and BN modelling. Section 4 analyses the results of the most important RIFs with respect to different 'accident types' and highlights the implications through scenario analysis. Finally, conclusions are summarised in Section 5.

# 2. Literature review 

### 2.1 Risk factors in maritime transportation

Ship accidents are caused by various types of failures, e.g. deck officer error ( $26 \%$ ), equipment failure ( $9 \%$ ), structural failure ( $9 \%$ ), crew error ( $17 \%$ ), mechanical failure ( $5 \%$ ), among others. ${ }^{18}$. The factor that influences the risk level of maritime transport is defined as risk influence factor (RIF). To determine the risk factors of maritime transport, the latest related literature and maritime accident reports during 2012-2017 have been reviewed.

To determine the RIFs in maritime transportation, risk factors that were commonly presented or frequently described in accident reports were extracted. Such factors, complemented by the RIFs identified from the related literature, compose the maritime transport RIFs in this study, which are presented in Table 1.

Table 1 RIFs contributing to maritime transport accidents.



87 Previous studies relied mainly on secondary database for risk factor identification in which primary information from accident reports was absence. One of the new features of this study is to incorporate new risk factors derived from accident reports into maritime accident analysis.

# 2.2 Risk analysis of maritime accidents

91 Since the UK Maritime and Coastguard Agency (UK MCA) proposed the formal safety assessment (FSA) framework to International Maritime Organization, maritime accident risk models have been fast developed because of the goal-setting risk regime. It takes into account ship conditions, organisational management, human operation, and hardware ${ }^{18}$. To assess the risks in maritime systems, quantitative risk assessments have been conduted to analyse maritime accidents. Yip, Jin ${ }^{23}$ applied econometrics method to conclude that the number of passenger injuries is positively related to the number of crew injuries in ferry, ocean cruise and river cruise passenger vessel accidents. Talley and $\mathrm{Ng}^{24}$ proposed a logical approach to select quality-of-service measures for port cargo, vessel and vehicle services, which

can be used as port performance indicators for evaluating the service performance of multi-service ports. Ventikos and Psaraftis ${ }^{25}$ presented the relationship between an oil spill-assessing approach, namely the event-decision network (EDN) and the FSA to describe the spill-scenario analysis and to pinpoint its interconnections with the official instrument. Besides that, risk analysis of maritime accidents would benefit the decision making systems onboard. Balmat, Lafont ${ }^{21}$ presented a fuzzy approach to automatically define an individual ship risk factor, which could be used in a decision-making system. Wu, Zong ${ }^{26}$ integrated evidential reasoning and TOPSIS into group decision-making for handling ships that are not under command. A fuzzy logic based approach was proposed by Wu, Yip ${ }^{27}$ for ship-bridge collision alert, considering ship particulars, bridge parameters and natural environment, which can be used for improvement of the ship handling in the bridge waterway area. Moreover, the causation analysis and modelling of maritime risks have been conducted ${ }^{28,29}$. Kum and Sahin ${ }^{17}$ used Root Cause Analysis (RCA) to clarify the causes and applied Fuzzy Fault Tree Analysis (FFTA) for a recommendation to reduce the occurrence probabilities of maritime accidents. Also, Zhang, Yan ${ }^{30}$ estimated the navigational risk of the Yangtze River using BN approach. Montewka, Ehlers ${ }^{31}$ developed the risk framework using BN for the estimation of the risk model parameters.

Analysis of maritime accident database is one of the most effective ways to investigate the causal chains and the correlations among causal factors in risk assessment. Pristrom, Yang ${ }^{10}$ used the Global Integrated Shipping Information System (GISIS) database to estimate the likelihood of a ship being hijacked. Zhang, Teixeira ${ }^{11}$ analysed historical accident data from 2008 to 2013 to predict the accident consequences in Tianjin port. However, the maritime accident database contains limited information compared to maritime accident reports. The investigation reports of maritime accidents provide the navigation

information, process of event occurrence, direct or indirect causes of the accidents, the actions taken

during the accidents, and recommendations. A few studies utilised accident reports to conduct accident analysis due to the time-consuming process of extracting the data from each report. For instance, Wang and Yang ${ }^{12}$ analysed the key risk factors influencing waterway accident severity from all accident investigation reports by China's Maritime Safety Administration (MSA). Chauvin, Lardjane ${ }^{15}$ concerned 39 vessels involved in 27 collisions to show the importance of Bridge Resource Management for situations of navigation in restricted waters. Chen, Wall ${ }^{32}$ utilised the accident reports of the selected cases from MAIB for accidents analysis to provide a complement measure. Akhtar and Utne ${ }^{33}$ conducted a correlation analysis of fatigue-related factors identified from 93 accident investigation reports, and identified the most influential factors related to top management: vessel certifications, manning resources, and quality control.

The data acquisition through the investigation of accident reports brings new insights, which cannot be achieved from the existing databases. Integrating the primary data with the advanced quantitative BN analysis approach facilitates maritime accident analysis and prevention from an innovative perspective. Despite previous attempts of using BN to model objective data from accident reports ${ }^{12}$, the relevant investigation relied on a small scale of database constrained in a pre-defined water/region. It requires more experiments based on a wide range of maritime accident data to be conducted to generalise the finding on BN's feasibility on RIF analysis and more importantly to reveal the most important RIF from a global perspective, particularly with respect to different accident types.

# 2.3 Bayesian networks in maritime risk analysis 

The interest of using BN as a tool in scientific risk analysis is continuously increasing, primarily related

to its advantages in terms of learning and inference. According to the literature review by Weber, Medina-

Oliva ${ }^{34}$, the number of academic papers on BN in risk analysis increased every year. Compared with other classical methods applied to dependability analysis, e.g. Markov Chains (MC) and Fault Trees (FT), BN sustains its advantages. Specifically, FT allows for calculating the probability by binary decision diagrams (BDD), which models the dependencies between events. However, it cannot represent the multiple state variables when multiple failures result in different consequences in a system. On the contrary, BN displays similar capabilities as the FT, but has additional ability to model a multi-state variable and several output variables. Weber, Medina-Oliva ${ }^{34,}$ Khakzad, Khan ${ }^{35}$ presented a comparison of FT and BN approaches, while previous studies also explained how FT could be transformed into BN ${ }^{36-38}$, involving dynamic FT transformation ${ }^{39}$. As far as MC is concerned, it analyses the exact probability of a failure event with the dependencies among variables and integrates the knowledge to represent multistate variables. However, the system modelling tends to be sophisticated with increasing variables ${ }^{34}$. In light of this characteristic, BN has required a relatively low number of parameters and a small-size conditional probability table. BN is widely utilised in maritime risk analysis, e.g. ship navigational risk assessment, port safety assessment, Arctic water transportation, inland waterway transportation, and collision assessment ${ }^{114041426,43}$. It is proved to be powerful to model maritime accidents since it enables quantitative analysis of Human and Organisational Factors (HOFs) ${ }^{33,44,45}$. It explicitly reveals probabilistic dependencies between factors and their causal relationships. Moreover, the feature that BN can take advantage of experts' knowledge makes it suitable for maritime risk modelling, in case of that failure data in the relevant investigations are incomplete. Therefore, experts' knowledge continues to be an essential data source for shipping accident modelling ${ }^{41,46}$, although it is subjectivity associated.

applied in the study. Due to its efficiency with the core idea of classification, the NBN model enables the
simplified BN structures without sacrificing its accuracy.

Compared with the studies on the probability and/or the frequency of maritime accidents, those addressing the relationship between risk factors and accident types are scanty in the literature. The risk factors contributing to collision may be different from the risk factors contributing to sinking. It reveals another new feature that is the analysis of accident types in maritime transportation and a new understanding of differentiation among critical factors contributing to different types of accidents.

# 3. Methodology 

BN is a probabilistic directed acyclic graphical (DAG) model ${ }^{47}$, which is composed of nodes with the links between them, representing variables and influences of one node on the other(s), respectively. The directional arc from node $A$ to node B refers that variable $A$ has a direct causal effect on $B$, representing conditional dependencies. In addition, the nodes that are not directly linked are conditionally independent of each other. A BN model usually consists of the following steps: data acquisition, BN structure learning, BN analysis, and sensitivity analysis and model validation ${ }^{22}$. For applying the model into this study, a methodology is developed by the following steps.

### 3.1 Data acquisition

To begin with, it is necessary to conduct a systematic procedure to search the maritime accident reports and select the reviewed reports, referring to Macrae ${ }^{7 .}$ Uğurlu, Köse ${ }^{8 .}$ Chauvin, Lardjane ${ }^{15 .}$ Wan, Yang
${ }^{48}$. The procedure consists of three stages: (1) online database searching; (2) reports screening and selecting; (3) refining and analysis. In this process, some of the reports involving accidents due to

disobeying rules of passengers or drowning in the swimming pool occurred in cruise ships, and extreme accidents occurred in small fishing vessels, tugs and etcetera were discarded, as their reduced manning requirements will easily lead to a distortion of results about the investigation on the factor impact ${ }^{2}$. Then, the maritime accident data is obtained according to the filtered accident reports.

# 3.2 RIF identification 

With respect to RIFs in maritime accidents, it is necessary to identify the key factors from accident investigation reports. According to the filtered reports (in Section 3.1), we derived the risk factors among them according to their appearance frequency in accident reports to eliminate the factors of trivial effect (i.e. appearing less than twice across the whole searching reports). As a result, 16 RIFs are identified including Ship type, Hull type, Ship age (years), Length (metres), Gross tonnage (GT), Ship operation, Voyage segment, Weather condition, Sea condition, Time of day, Fairway traffic, Ship speed (knots), Vessel condition, Equipment/device, Ergonomic design, Information. The detailed explanation of RIFs in BN is stated in Section 4.2.

### 3.3 BN structure learning

Once RIFs are identified, a BN structure is to be generated by using the RIFs as the nodes. There are mainly two approaches for BN structure learning. One is based on the expert knowledge, which is used to conduct a qualitative analysis based on the subjective causal relationships. The other is the data-driven approach to represent the interactive dependencies between variables. This study is to develop the BN modelling by the later method.

However, the complexity of a data-driven BN structure super-exponentially increases with the growing number of variables in the network ${ }^{40,49}$. To overcome such a disadvantage, NBNs are usually applied instead. It is a commonly used model aiming at improving the classification ${ }^{50}$. To realize this, there is a

strong assumption in most NBN models that it has an independent node as the target node directly connected with all the other nodes which are independent to each other in the structure. Referring to the expert opinion and the previous studies ${ }^{12}$, the interdependency among RIFs are insignificant in this study, which make it applicable for such strong assumption.

In the study, the only child node of BN is 'accident type', i.e. the class variable $(S)$. The parent node set $R=\left\{R_{S T}, R_{H T}, R_{S A}, R_{L}, R_{G T}, R_{S O}, R_{V S}, R_{W C}, R_{S C}, R_{T D}, R_{F T}, R_{S S}, R_{v c}, R_{E}, R_{E D}, R_{I}\right\}$ is the set of risk variables $\left(R_{k}\right)$ including the 16 RIFs of (in a matching order) ship type, hull type, ship age, length, gross tonnage, ship operation, voyage segment, weather condition, sea condition, time of day, fairway traffic, ship speed, vessel condition, equipment, ergonomic design, and information. Then, the structure learning is simplified to demonstrate the relationship between $S$ and $R_{k}$, as presented in

Fig.1.(a).
![img-0.jpeg](img-0.jpeg)

Fig. 1. (a). 'Accident type' as a child node
![img-1.jpeg](img-1.jpeg)

Fig. 1.(b). 'Accident type' as a parent node.

However, the size of the conditional probability table of the target node increases exponentially, resulting in the complex computation in this converging BN. To simplify the structure, a modified diverging NBN structure in which 'Accident type' have no parents but is the only parent of other RIFs is presented, as shown in Fig. 1(b). Compared to the structure in Fig. 1(a), this structure (i.e. Fig. 1(b)) significantly reduces the computation and number of conditional probability distributions. Hence, it is adopted to express the relationship between the RIFs in the NBN structure. Because BN has the ability to conduct

bi-directional risk analysis, the transformation from the converging to diverging connections will be well
reflected by the adapted conditional probability tables (CPT) and hence has no influence to the final BN results on risk analysis (e.g. Wang and Yang ${ }^{12}$ ).

# 3.4 Mutual information and sensitivity analysis 

### 3.4.1 Mutual information

In the probabilistic theory, the mutual information is a measure of the mutual dependence between two variables. It describes the amount of information obtained about one random variable, through the other random variables ${ }^{40}$. Mutual information is also interpreted as entropy reduction, measuring the mutual dependence of different variables. Since the objective of this study is to identify the relationship between RIFs and 'accident type', 'accident type' is determined as the fixed variable in mutual information.

The larger the value of mutual information is, the stronger relationship between individual RIF and 'accident type'. In this way, calculating the mutual information is able to filter out the RIFs that are relatively less important in the model. Then the remaining RIFs are selected as significant variables with regards to a pre-defined accident type.

### 3.4.2 Sensitivity analysis - True Risk Influence (TRI) of risk variables

Based on the significant RIFs screened from mutual information calculation, there is another form of sensitivity analysis, e.g. scenario simulation, to determine the effects of different variables, particularly in a combined way. The classical way is to set a scenario in which all the other nodes (apart from the investigated ones) are locked, and the target node is updated accordingly. It means, for example, $10 \%$ up and down for the node reveals the effects of the variable in the model. It is considerably applicable for variables with two states, but not suitable for variables with more than two states. For example, when the

In this case, the traditional scenario simulation is inappropriate.

In order to overcome the drawback of the traditional way, a new method proposed by Alyami, Yang ${ }^{51}$ is
applied here. This method increases the probability of the state within the highest influencing on a type of accidents (e.g. collision) to $100 \%$ to obtain the High Risk Inference (HRI) of collision. Then it increases the probability of the state generating the lowest influence on the collision to $100 \%$ to obtain the Low Risk Inference (LRI) of collision. In this way, calculating the average value of HRI and LRI concludes the True Risk Influence (TRI) of each variable in the case of a particular accident type. It is described as:

$$
T R I=\frac{H R I+L R I}{2}
$$

where HRI refers to 'High Risk Inference' which is calculated for a variable influencing 'collision', LRI is 'Low Risk Inference' calculated for a variable influencing 'collision', and TRI refers to 'True Risk Influence' for a variable influencing 'collision'. To obtain the variable influence on 'accident type', a similar analysis procedure is applied to other accident types, 'grounding' and 'flooding', etc. Then TRIs for a variable influencing all accident types are obtained. After applying this method for each variable, the TRIs for all variables for all accident types are available. Therefore, the sensitivity analysis illustrates the ranking of variables' influences on accident types according to the value of TRI. In addition, the average TRI values of all accident type priorities the variables' effects on the 'accident type'. The higher a TRI is, the higher its corresponding RIF's effect on 'accident type'.

# 4. Results and discussion 

### 4.1 Raw data

The accident reports are from MAIB in UK and TSB in Canada, as they are among the most representative from the literature ${ }^{15-17}$. The raw data derived from the MAIB and TSB contains general information of the ship and the voyage, accident evolution process, and details related to the management and organizational factors. In the screening process stage, the accident reports were screened with a focus on errors-related accidents to ensure their representativeness and relevance. Some of the reports involving accidents due to disobeying rules of passengers or drowning in the swimming pool occurred in cruise ships, and extreme accidents occurred in small fishing vessels, tugs and etcetera were discarded, as their reduced manning requirements will easily lead to a distortion of results about the investigation on the accident ${ }^{2}$. In the final stage, these reports had been further refined and analysed, especially the 'safety issues' and 'common factors' Section in the accident reports. Some details of information associated with the accident process were involved in the refinery. According to such analysis, there are 109 accident reports extracted from 152 reports in MAIB and 52 accident reports obtained from 61 reports in TSB, as shown in Appendix I.

In total, the 161 maritime accidents involving 208 vessels reported in MAIB and TSB between Jan. 2012 and Dec. 2017 were carefully reviewed and analysed manually. The search was conducted in Jan. 2018 and the general statistical analysis and findings are presented in Fig. 2 and Fig. 3(a) (b), which provide the raw data for our next in-depth analysis using NBN.

![img-2.jpeg](img-2.jpeg)

Fig. 2. Accident distribution by accident types
![img-3.jpeg](img-3.jpeg)

288 (a) Accident distribution by ship operations
![img-4.jpeg](img-4.jpeg)

290
(b) Accident distribution by voyage segments

291
Fig. 3. Accident distribution from MAIB

292
As is indicated in Fig. 2, grounding, collision and contact/crush accounted for larger percentages than

other kinds of accidents while sinking and flooding accounted for lower percentages. Specifically, there were 23 grounding accidents from MAIB and 14 from TSB, while 3 sinking accidents from MAIB and 4 from TSB. And Fig. 3 shows accident distributions by ship operation and voyage segment from MAIB.

The number of accidents happened on passage was much higher than that others, followed by 'fishing' and 'at anchor'. However, the number of accidents happened in mid-water was much higher than others like 'departure' and 'in port'.

These reports had been further refined and analysed. And special attention are paid to the 'safety issues' and 'common factors' in the accident reports. Some details of information associated with the accident process were involved in the refinery. According to such analysis, the common factors contributing to the accidents are generated.

# 4.2 RIF identification 

With respect to the accident type, a maritime accident can be classified into collision (S1), grounding (S2), flooding (S3), fire/explosion (S4), capsize (S5), contact/crush (S6), sinking (S7), overboard (S8), and others (S9), which refers to the combined description and definition in MAIB and TSB. These 9 types of accidents consists of 9 states $(S 1 \sim S 9)$ of the variable 'accident type' in the study.

Furthermore, the accident-related RIFs are retrieved in Table 2. In the quantitative analysis of BN modelling, the accident type is defined as a dependent variable, variables in Table 2 are defined as independent variables, as explained in Section 3.3.

Table 2 The accident-related RIFs



312 RIFs: risk influence factors; BN: Bayesian network; RORO: roll on/roll off; NA: not applicable; BNWAS: bridge navigational watch alarm system; MAIB: Marine Accident Investigation Branch.
*The ship speed is group into normal and fast states based on the description in the MAIB accident reports.
315 A majority of definitions of variables' states are derived from accident reports. To quantify such states,
316 majority of variables are defined and quantified based on the literature in Table 1. However, variables,
317 e.g. accident type, ship type, hull type, ship operation, and voyage segment, are divided into different
318 states according to the classification of MAIB or TSB investigation. The 'vessel condition' is quantified
319 into two states based on whether it is blamed for the faults in accidents, as described in the reports. The grading of 'ship speed' is based on the description in the MAIB accident reports, rather than the grading method by Wang and Yang ${ }^{12}$. The main reason is that accurate speeds of vessels involved in accidents

are not clearly indicated in the source database.

# 4.3 NBN modelling 

Although the assumption that the variables are completely independent is not always true in reality, modified diverging NBN simplifies the structure by reducing the number of conditional probability distributions. Moreover, such an assumption does not significantly affect the posterior probabilities calculated, which does not affect the scenario analysis in the study ${ }^{12}$, given the fact that the statistical analysis of all the accidents did not indicate strong correlation among the RIFs. Therefore, assuming that all the variables, i.e. the child nodes, are independent with each other, the NBN is constructed.

Based on the NBN model, the parameter learning of CPTs from the cases is conducted by the software 'Netica' using the counting-learning algorithm. Once the CPTs are constructed and obtained (Appendix II), the posterior probabilities of each variable can be calculated. The statistical analysis of the probability of variables reveals interesting initial findings in terms of safety caution and accident prevention as follows.

![img-5.jpeg](img-5.jpeg)

Fig. 4. Results of NBN

Fig. 4 presents the results of NBN involving all the retained 16 RIFs. Among the accidents, grounding
and collision are two most frequently occurred types of accidents: accounting for $20.3 \%$ and $21.2 \%$,
respectively. A majority of vessel lengths (i.e., $65 \%$ ) are less than 100 m . Vessels with gross tonnages less
than 300 account for $37.5 \%$ of shipments involved in accidents. In addition, $67.5 \%$ of vessels are made
of steel.

In light of environmental factors, $40 \%$ of vessels in the accidents are involved in the ship operation of
'on passage', $41.3 \%$ are involved in the voyage segment of 'mid-water'. In addition, only $19.1 \%$ of ships
involved in accidents are in poor fairway traffic in the process of accidents, $45.7 \%$ are at night time.
Severe weather condition accounts for $40.2 \%$ of accidents, while tough sea condition accounts for $53.2 \%$.

With regard to ship factors, fishing vessels constitute the largest proportion (i.e. 18.4\%) of shipments in

accidents. Ships older than 20 years is presented in $33.2 \%$ of accidents. In addition, $46 \%$ of vessels
convey insufficient information, $14.2 \%$ have ergonomic design problems, $38.9 \%$ are faced with invalidequipment or devices onboard, and $30.4 \%$ experience the condition of modification or increasing size.

# 4.4 Sensitivity analysis and model verification 

### 4.4.1 Mutual information analysis

Table 3 demonstrates the mutual information shared between "accident type" and RIFs. When "accident type" is the parent node, "ship operation" with the corresponding mutual information value of 0.28294 , has the strongest effect on the accident type. To select important variables, a threshold of the mutual information value is set as 0.09 , which is the average mutual information value. The variables with $I\left(S, R_{k}\right)$ larger than 0.09 , i.e. "ship operation", "voyage segment", "ship type", "gross tonnage", "hull type", and "information", illustrate essential impacts on "accident type". Thus, these variables are to be computed for the factor analysis in the next step. In addition, variables that have less impact on "accident type" mainly include "ship age", "vessel condition", "ergonomic design", "length", "fairway traffic", "sea condition", "equipment or device", "ship speed", "time of day", and "weather condition".

Table 3 Mutual information shared with 'accident type'



362 4.4.2 Sensitivity analysis

363 In terms of sensitivity analysis, Table 4 demonstrates the TRI value of 'ship operation' against collision,

364 where $S 1$ refers collision. Table 5 indicates the values of all RIFs for all accidents, where $S 1 \sim S 9$ are defined in Section 4.2.

Table 4 TRI of a risk variable (ship operation) for collision


367 *S1 - Collison
368 Table 5 TRI of risk variables for all accident types


369 Specifically, in Table 4, the first row denotes the base-case scenario where the value of $S 1$ is ' 20.3 ', and
370 the following rows represent the different scenarios with each state of the variable reaches $100 \%$, for
371 example, the second row increases the probability of the state 1 of ship operation to $100 \%$ to obtain the
372 value of $S 1$ (2.99). The same process is applied to all states of ship operation. According to column 'S1',

373 ' 39.8 ' is the largest, which means the state 7 of ship operation is the state within the highest influencing

374 on $S 1$ (collision), and the difference between ' 39.8 ' and ' 20.3 ' (base-case scenario) is the HRI, i.e. ' 19.5 '.

375 However, ' 2.99 ' is the smallest value, which means the state 1 of ship operation is the state within the

376 lowest influencing on $S 1$ (collision), so the LRI is obtained as ' 17.31 '. Then the TRI is calculated by

377 averaging them. In this way, TRIs of each RIF of each accident type are obtained in Table 5.

378 To obtain the impact levels of such RIFs in accident types, TRIs are compared and ranked. Generally,

379 the most important variables lists for 'accident types' are as follows:

380 Ship operation $>$ Voyage segment $>$ Ship type $>$ Hull type $>$ Gross tonnage $>$ Information

381 In detail, the most important variables lists for different accident types are demonstrated in Table 6.

Table 6 The most important variables


383 4.4.3 Model validation

384 To validate the model, another sensitive analysis is conducted by investigating the results of the model given RIFs. It is also used to test the combined effect of multiple RIFs to the accident types. There are two axioms that have at least to be satisfied for the inference process ${ }^{22,52}$ :

387 Axiom 1: A slight increase/decrease in the prior probabilities of each test node should contribute to the correspondence increase/decrease in the posterior probability of the target node.

389 Axiom 2: The total influence of the combination of the probability variations of $x$ parameters (evidence) should be no smaller than the one from the set of $y(y \in x)$ risk factors.

391 Accounting for different states of the parent nodes, this study calculates the changed value of each state.

392 The 'information' is selected as the first node, the state generating the highest changed value of state 1 in 'accident type' is increased by $10 \%$, while the state generating the lowest changed value of state 1 in 'accident type' is decreased by $10 \%$. This procedure is written as ' $\sim 10 \%$ ' in Table 7. Then, the same approach is applied to the next RIF, and the cumulative changed value is obtained and updated. The updating procedure would continue until all the RIF nodes are involved. Similarly, the same updating procedure is applied into the state $2,3 \ldots 9$ in 'accident type' respectively, until all states of accident type are included, as seen in Table 7.

Table 7 Accident rate of minor change in variables


400 The first column of the data in Table 7 shows the original values of 9 states of accident types in NBN, and the rest columns state the updated changed values of results. However, each state of 'accident type' is calculated separately, i.e. each row is computed through the change of states of RIFs in each accident

type. Specifically, for the first row, ' 20.30 ' is the original value of accident type $S 1$ (grounding). Moreover, ' 20.70 ' is calculated by the way that the state of 'Information' generating the highest changed value of $S 1$ is increased by $10 \%$ while the state generating the lowest changed value of $S 1$ is decreased by $10 \%$.

A further step is conducted based on ' 20.70 ' to obtain ' 21.00 ' in the table, which means the state of 'Hull type' generating the highest changed value of $S 1$ is increased by $10 \%$ while the state generating the lowest changed value of $S 1$ is decreased by $10 \%$. Then 'Gross tonnage', 'Ship type', 'Voyage segment', 'Ship operation' apply this method sequentially. Furthermore, the same updating procedure is applied into the $S 3, S 4, \ldots, S 9$ respectively, until accident types are included. Besides that, the updated values of the target node demonstrate this model is in line with Axiom 1. Moreover, Axiom 2 is examined by comparing the initial target value with the updated one under all states. From Table 7, the updated values of the target node are gradually increasing or decreasing along with the continuous updating of RIFs.

# 4.5 Implications: scenario analysis 

The study enables the understanding of differentiation among critical factors contributing to different types of accidents. BN modelling is applicable to analyse the occurrence likelihood of each accident type in different scenarios involving vessel condition and environmental factors. To do this, two scenarios are proposed for useful research implications and managerial contributes.

### 4.5.1 Scenario 1: environmental factor

In the first scenario, maritime accidents under specific shipping environmental factors are estimated. Shipping environmental factors contain ship operation, voyage segment, weather condition, sea condition, time of day, fairway traffic in this scenario. For different assigned states of these factors, maritime accidents reveal in different types.

424 When the nodes are assigned with the specific states in Fig. 5(a), the effects of the shipping environment
425 are revealed. The probability of collision is the highest among the 'accident type', accounting for $85.1 \%$,
426 followed by grounding only accounting for $4.52 \%$. Such probability indicates the considerable increase
427 in the risk of collision compared to the other types of accidents.
![img-6.jpeg](img-6.jpeg)

Fig. 5. (a). Posterior probability analysis in Scenario 1 - collision

![img-7.jpeg](img-7.jpeg)

Fig. 5. (b). Posterior probability analysis in Scenario 1 - grounding

With regard to the following states in Fig. 5(b), the effects of the environment are revealed. The probability of grounding is the highest among the 'accident type', accounting for $79.9 \%$ of the accident types. Therefore, transport authorities and ship owners should pay more attention to risk-reduction measures for collision or grounding under specific navigational environment, especially the strongrelated variables, i.e. ship operation, voyage segment, fairway traffic, and sea condition.

# 4.5.2 Scenario 2: vessel factor 

In the second scenario, attention has been paid to vessel factors associated with maritime accident types.

The variables include ship age, ship type, information, ergonomic design, equipment/device, vessel condition, and ship speed. For different assigned states of these vessel factors, maritime accident types have shown different likelihoods.

442 Assuming that variables are assigned with the certain states in Fig. 6(a), the effects of vessel factors on

443 accident types are illustrated. The probability of collision is the highest among 'accident type',

444 accounting for $82.1 \%$. This probability indicates the considerable increase in the risk of collision

445 compared to the initial states in Fig. 4 due to the combined effect of the involved RIFs.
![img-8.jpeg](img-8.jpeg)

446

447 Fig. 6. (a). Posterior probability analysis in scenario 2 - collision

![img-9.jpeg](img-9.jpeg)

Fig. 6. (b). Posterior probability analysis in scenario 2 - grounding

Assuming that the variables are assigned with the specific states in Fig. 6(b), the effects of vessel factors
are indicated. The probability of grounding is the highest among 'accident type', accounting for $62.6 \%$,
followed by sinking (i.e., $12.7 \%$ ). This probability indicates the significant increase in the risk of grounding and sinking compared to the initial states in Fig. 4.

According to the above analysis, transport authorities and ship owners can use this findings to put forward the most effective risk control measures for different types of accidents derived from various vessel factors, especially the strong-related variables, i.e. ship type, information, ship age, vessel condition, and ergonomic design.

# 5. Conclusions 

Compared to previous studies focusing on causal factors related to the severity and the probability of

maritime accidents, this study uses a NBN approach to investigate how different risk factors pose an impact on different types of maritime accidents. To identify RIFs, maritime accident reports from MAIB and TSB within a five-year period are extracted and reviewed to develop a primary database on maritime accidents. Then the risk-based NBN model is constructed to analyse RIFs in maritime accidents. At last, the sensitivity analysis is conducted, as well as scenario analysis to implicate research contributes. In general, the results from the NBN model present the distinctions among the key factors contributing to different types of accidents, which helps generate insights for accident prevention.

In summary, the findings of this study can be summarised as follows:
(1) According to the calculations of the mutual information, crucial RIFs are ranked under different accident types. The results reveal that critical RIFs for maritime accident types are 'Ship operation', 'Voyage segment', 'Ship type', 'Gross tonnage', 'Hull type', 'Information'.
(2) There is the highest probability of overboard occurred on fishing vessels. When the ship operation is 'towing', the accident type has high likelihood of being 'capsize'; 'manoeuvring' and 'on passage' operation contribute to the higher probability of grounding; 'pilotage' is closely related to 'contact/crush'.
(3) When ships are in 'mid-water' and 'transit' voyage segments, there is a higher probability of being in collision. Grounding is more easily to happen in 'departure' and 'arrival' segments.
(4) The situation of poor information onboard exposes a higher risk of grounding, whereas the condition of good information associates with the collision.

Among them, the scenario analysis reveals that environmental factors and vessel factors of maritime accidents generate significant impact on accident types.

With respect to the environmental factors, the probability of collision is the highest among the 'accident

type' when a ship is in the below states: 'voyage segment - transit'; 'ship operation - on passage'; 'before 7:00 am or after 19:00 pm'; 'good weather and sea condition'; 'not considering the fairway traffic appropriately'. The probability of grounding is the highest when a ship is in the below states: 'voyage segment - departure'; 'ship operation - pilotage'; 'between 7:00 am and 19:00 pm'; 'severe weather and sea condition'; 'not considering the fairway traffic appropriately'.

With regard to the vessel factors, the probability of collision is the highest among 'accident type' if a ship is in the following states: 'older than 20 years', 'effective and updated information provided', 'ergonomic problem', 'equipment operates correctly', 'good condition of vessel', 'fast ship speed'. The probability of grounding is the highest among 'accident type' if a fishing ship is in the following states: 'older than 20 years', 'lack if updated information', 'ergonomic design friendly', 'equipment not fully utilised', 'modification made to vessels and size', 'normal ship speed'. Therefore, such conclusions can effectively assist maritime authorities in developing countermeasures for accident prevention.

There are also limitations in this study. The small number of flooding data makes the results not significant and robust. Although BN has the ability to conduct bi-directional risk analysis, the transformation from the converging to diverging connections does not intuitively represent the accident development. Further research can be performed by using expert judgement to help model learning to overcome the problems brought by data scarcity. Moreover, more human factors resources, underlining communication, situation awareness, fatigue, and etcetera, will be processed to conduct further research to illustrate the influence of human errors on maritime accidents.

# Acknowledgements 

This research thanks the general help from the EU project RESET (H2020-MSCA-RISE-2016, 730888);

# 503 Declaration of conflicting interests 

504 The authors declare that there is no conflict of interest.

## 505 Funding

506 The research was sponsored by the National Key Technologies Research \& Development Program (grant
507 number 2017YFE0118000); Funds for International Cooperation and Exchange of the National Natural

508 Science Foundation of China (grant number 51920105014); Technical Innovation Project of Hubei
509 province (International Cooperation) (2018AHB003); and China Scholarship Council (grant number
$510 \quad 201706950084)$.

## 511 Appendix I

512 Accident reports from MAIB and TSB




# 513 Appendix II 

514 Conditional probability tables (CPT) for RIFs


515

## Equipment_device




517


518







521



522


523


524







526




527









530

531
