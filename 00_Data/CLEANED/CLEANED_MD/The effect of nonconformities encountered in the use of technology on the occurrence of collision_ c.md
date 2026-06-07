# LJMU Research Online 

Kaptan, M, Ugurlu, O and Wang, J
The effect of nonconformities encountered in the use of technology on the occurrence of collision, contact and grounding accidents
http://researchonline.ljmu.ac.uk/id/eprint/15965/

## Article

Citation (please note it is advisable to refer to the publisher's version if you intend to cite from this work)

Kaptan, M, Ugurlu, O and Wang, J (2021) The effect of nonconformities encountered in the use of technology on the occurrence of collision, contact and grounding accidents. Reliability Engineering and System Safetv. 215. ISSN 0951-8320

LJMU has developed LJMU Research Online for users to access the research output of the University more effectively. Copyright © and Moral Rights for the papers on this site are retained by the individual authors and/or other copyright owners. Users may download and/or print one copy of any article(s) in LJMU Research Online to facilitate their private study or for non-commercial research. You may not engage in further distribution of the material or use it for any profit-making activities or any commercial gain.

The version presented here may differ from the published version or from the version of the record. Please see the repository URL above for details on accessing the published version and note that access may require a subscription.

For more information please contact researchonline@ljmu.ac.uk

# The effect of nonconformities encountered in the use of technology on the occurrence of collision, contact and grounding accidents 

Mehmet Kaptan ${ }^{\mathrm{a}}$ (corresponding author), Özkan Uğurlu ${ }^{\mathrm{b}}$, Jin Wang ${ }^{\mathrm{c}}$<br>${ }^{a}$ Faculty of Maritime, Recep Tayyip Erdoğan University Rize-Turkey mehmet.kaptan@erdogan.edu.tr, https://orcid.org/0000-0003-3304-4061<br>${ }^{\text {b }}$ Faculty of Marine Science, Ordu University, Ordu, Turkey, ougurlu@odu.edu.tr, ozkanugurlu24@hotmail.com, 00905058179839, https://orcid.org/0000-0002-3788-1759<br>${ }^{c}$ Liverpool Logistics, Offshore and Marine (LOOM) Research Institute, Faculty of Engineering and Technology, Liverpool John Moores University, Liverpool, UK, j.wang@ljmu.ac.uk, https://orcid.org/0000-0003-4646-9106


#### Abstract

Technology and its innovative applications make life easier and reduce the workload on seafarers. Today's ship bridges have much more modern and integrated navigation systems than before, and the ship's handling and management have become much easier. However, nonconformities encountered in the use of technological devices may cause accidents. In this study, the effect of human factor related errors associated with the use of the bridge's electronic navigational devices on grounding and collision-contact accidents was investigated. Nonconformities obtained from 175 collision-contact and 115 grounding accident reports were qualitatively analysed by means of human factor analysis and a classification system. Afterwards, relationships between nonconformities and their probabilities were evaluated quantitatively via a Bayesian network method. As a result of the study, the accident network was revealed. This accident network summarizes how operating errors in the use of technological equipment cause accidents. Recommendations on the prevention of accidents caused by operating errors associated with the use of new technologies are finally given.


Key words: Accident analysis; Bayesian network; HFACS-PV; Marine accident; Human factor

# 1. Introduction 

To ensure sustainable trade, a safe environment must be created for vessels at sea (UNCTAD, 2017). The International Maritime Organization (IMO) was established in 1958 to maintain maritime safety. Although this organization introduces new regulations, training forms, and the use of new ship equipment, accidents continue to occur (Tarelko, 2012). Today, marine accidents remain a major concern, both environmentally and economically (Youssef and Paik, 2018). Spatial constraints, heavy weather and sea conditions, malfunctions and human error are the dominant factors in the occurrence of accidents (Grabowski and Sanborn, 2003, Eliopoulou and Papanikolaou, 2007, Ung, 2018). Human error accounts for 75-96\% of losses in marine operations (Islam et al., 2018). Although human error does not always result in a disaster, it can cause significant economic losses due to delayed operations (Sotiralis et al., 2016).

Undoubtedly, advances in navigation aid systems from past to present have played an essential role in reducing human error. However, technological advances have posed new risks and potential accident scenarios (Hetherington et al., 2006, Psarros, 2018, Endrina et al., 2019). It is obvious that considerations related to human judgment will remain at the forefront of this industry until the management of maritime transport transitions to autonomous systems and software (Martins and Maturana, 2010, Montewka et al., 2017). In the past, the interactions between operators and technology have caused major disasters (Dhami and Grabowski, 2011). To prevent such disasters in the maritime industry, it is important to understand the perception, abilities, decisions, and effects of watchkeeping officers on developing automation systems and their effects on the likelihood of accidents (Praetorius et al., 2015). Recent studies show that new accident-related factors are coming to the forefront: Errors in the use of electronic navigation devices, overconfidence in data presented by automation control systems, lack of understanding of the natural weaknesses of electronic navigation devices, ergonomic design

failure, and human-computer interfaces are some of them (Chauvin et al., 2013, John et al., 2013, Perera and Soares, 2015). Moreover, the complex structure of automation systems and the incomplete or erroneous steps taken by officers who have not mastered this structure can cause devastating accidents (Lutzhoft and Dekker, 2017). When these factors are taken into consideration, it becomes obvious that human-based errors in relation to electronic navigation systems should be identified and evaluated to prevent future accidents.
"Collision-contact" and "Grounding" are among the most common accident categories (Mullai and Paulsson, 2011). According to Swedish Club (2011) the average cost of these accidents per ship is greater than 800,000 USD. Collision-contact and grounding also account for approximately half of the boat and machine damage costs incurred due to accidents on ships. Therefore, preventing collision-contact and grounding accidents will provide significant savings for all sides of the transport industry.

Accident analysis studies are carried out to determine the factors that trigger accidents and their severity. Thus, accident prevention strategies are identified and implemented. Then, the effects of these strategies on accidents are observed (Stoop, 2003). Achieving effective results from accident analysis depends on identifying the causes of the accident and the correct definition of the relationship between them. Accident analysis models make it possible to determine the effects of accident causes (Katsakiori et al., 2009). Therefore, today there are nearly 100 accident analysis models whose applicability is proven by at least one case study (Johnson, 2003, Kristiansen, 2013, Underwood, and Waterson, 2013). Accident investigators have to choose the most appropriate method. It would be appropriate to select the method according to the complexity of the accident and the elements to be analysed (Underwood, and Waterson, 2013). With the Human Factors Analysis and Classification System (HFACS) based on Reason's Swiss Cheese model, it is possible to systematically examine the effects of human factors on accidents and classify the causes of accidents (Shappell and Wiegmann, 2000).

However, HFACS does not explain the relationship between causes. At this stage, a Bayesian network method is used. Bayesian network is a method based on conditional probability that makes it possible to interpret the relationship between causes by means of nodes and edges. Thus, users can estimate the risk of accident due to varying conditions (Chen et al., 2019, Ni and Zhang, 2019, Seyedhassani et al., 2019).

In this study, the effects of operational errors associated with the use of new technologies in maritime transport on collision-contact and grounding accidents were examined via a hybrid method of a HFACS and a Bayesian network. The HFACS method was used to categorize the causes of accidents according to a hierarchical structure. The Bayesian network method was implemented to show the relationships between accident causes. Using the network structure presented in this study, it is possible to detect the nonconformities that play a role in the occurrence of accidents and analyse the impact of an accident. The risk of accident occurrence under variable conditions can be estimated using the network structure. Thus, it is possible to predict the effect of measures that can be taken to prevent accidents on ships.

# 2. Background 

### 2.1. The HFACS

The HFACS is a human factor analysis system that categorizes the impact of human errors on accident formation according to a hierarchical structure. Using this method, it is possible to systematically examine the effects of human-related factors on accidents and elaborate on the relevant causes and sub-causes. The most important feature that distinguishes the HFACS from other accident analysis methods is the ability to demonstrate the role of administrative and organizational factors in complex systems (Wiegmann and Shappell, 1997). The HFACS method does not require expert opinions on the classification of accident causes or causal

factors. For this reason, researchers who have mastered the main structure and sub-structure can show the occurrence of accidents gradually (Ugurlu et al., 2018).

Over time, as the recognition and application area of this method expanded, the HFACS was transformed by many researchers from various sectors (Dambier and Hinkelbein, 2006, Daramola, 2014). It has a wide range of applications in air transport (Wiegmann and Shappell, 2001, Shappell and Wiegmann, 2004, Dambier and Hinkelbein, 2006), maritime transport (Chen et al., 2013), railway transport (Baysari et al., 2008), the mining industry (Patterson and Shappell, 2010, Lenné et al., 2012), the oil and gas industry (Theophilus et al., 2017), and many other sectors. The last change in the HFACS structure concerning maritime transport was made by Uğurlu et al. (2018), who proved the validity of the HFACS-PV (Human Factor Analysis and Classification System for Passenger Vessel) structure through three case studies (Sarıalioğlu et al. 2020, Uğurlu et al. 2020a, Yıldız et al. 2021). They added a level of operational conditions (environmental factors) to the main structure and made minor changes to the other levels, making them compatible with the maritime sector. The HFACS-PV structure consists of 5 levels, unlike the original HFACS structure. Figure 1 shows the HFACS-PV's main structure and sub-structures. In this study, accident analyses were performed using the HFACS-PV framework.

Figure 1. The human factor analysis and classification system (HFACS-PV)

# 2.2. Bayesian Network 

A Bayesian network is a network cycle in which variables are represented by nodes' and inter-nodes' relations with each other (probabilistic dependency), which are shown using edges (Kjærulff and Madsen, 2013, Loughney and Wang, 2018). In this type of network structure, nodes (inputs) are factors that contribute to the main problem (output) (Rausand, 2011). There

are no restrictions on the number of children or parents that nodes can have (Gross et al., 2019). In contrast to regression and similar methods, the Bayesian network method does not depend on a single output variable and can be deduced for all variables in the network. These features make it an effective tool for decision-making and analysis (Zhang et al., 2013). Therefore, the Bayesian network method has been used as a method in medical diagnosis (Chen et al., 2019), marketing (Seyedhassani et al., 2019), earthquake risk assessment (Ni and Zhang, 2019) and accident analysis (Zhang et al., 2018; Zhao et al., 2020).

In this type of network structure, probability values and conditional probability tables are created depending on the inputs. There are two main approaches to calculating the probability values of nodes in a Bayesian network structure. One of them involves statistical data, and the other involves expert judgement. If sufficient statistical data is not available for the examined events, conditional probability tables are formed based on expert opinions (Matellini et al., 2013, Pristrom et al., 2016). Conditional probability tables explain the effects of nodes on each other independently or dependently (Jones et al., 2010, John et al., 2016). A Bayesian network includes two types of approaches: qualitative and quantitative. In the qualitative approach, the variables of the network and the relationships between them are transferred graphically. In the quantitative approach, the probabilistic relationships between the variables (conditional probability tables) are established. A Bayesian network based on data was formulated in this study, and conditional probability tables were constructed.

Nodes that do not have a dependency or have no parents, have marginalised probabilities (Jones et al., 2010, John et al., 2016). Marginalised probability is the unconditional probability of an event. The marginalised probability of an event A , denoted by $\mathrm{P}(\mathrm{A})$, is the probability that event A will occur. Event A has $\mathrm{P}(\mathrm{A})$ between 0 and 1.0 , and it cannot have a negative probability. Therefore, it can be expressed as follows (Fenton and Neil, 2013):

$$
0 \leq P(A) \leq 1
$$

The complement of $\mathrm{P}(\mathrm{A})$ is the probability that $P(\hat{\mathrm{~A}})$ that event A does not occur. All possible results are in the "S" sample space. $S \supseteq A=>$ the sum of the probabilities of A and its complement $\hat{A}$ must be equal to 1.0 :

$$
P(S)=P(A)+P(\hat{\mathrm{~A}})=1
$$

The probability of an expected event is formulated as follows:

$$
\text { Probability }=\frac{\text { Expected number of events }}{\text { Number of all possible events }}
$$

Bayes' theorem's conditional probability calculations are formulated as follows (Matellini et al., 2013):

$$
\begin{aligned}
& P(A / B)=\frac{P(A \cap B)}{P(B)}, P(B)>0 \\
& P(B / A)=\frac{P(A \cap B)}{P(A)}, P(A)>0
\end{aligned}
$$

Equation (4) in any sample space indicates the probability of the occurrence of event A when event B is known (when event B occurs); Equation (5) shows the probability that event B occurs when event A is known. When Equations (4) and (5) are rearranged, the following equation can be obtained:

$$
P(A \cap B)=P(B) P(A / B)=P(A) P(B / A)
$$

Considering the occurrence of a sample space, the probability of occurrence of any event state $A_{1}$ is shown as Equation (7).

$$
P\left(A_{i} / B\right)=\frac{P\left(A_{i}\right) P\left(B / A_{i}\right)}{P(B)}
$$

# 3. Methodology 

In this study, grounding and collision-contact accidents involving human errors related to the use of electronic navigation devices were investigated with the aim of identifying the errors associated with their use and revealing the effects of these errors on the likelihood of accidents occurring. Accident data was obtained from accident databases, such as the MAIB (Marine Accident Investigation Branch), ATSB (Australian Transport Safety Bureau), EMSA

(European Maritime Safety Agency), and NTSB (National Transportation Safety Board), which form the basis of the data set of many accident analysis studies (Table 1) (Chen et al., 2013, Chauvin et al., 2013, Underwood and Waterson, 2014, Zhang et al., 2018). The accident reports include accidents occurring on ships over 500 GRT (subject to the SOLAS criteria) and the reasons related to bridge-navigation equipment as the cause of the accident. In accordance with these criteria, 115 grounding and 175 collision-contact accident reports from 2000 to 2017 were examined.

Table1. Distribution of accident data according to database

The research consisted of four stages. In the first stage, a Microsoft Excel-based database was created using accident reports. This new database contained several pieces of information, such as ship name, accident date, accident size, type of navigation, and type of ship. The aim of producing this new database was to enable a systematic analysis of accident data. At this stage, the causes of each accident were also determined; the preliminary preparations for the next stage and the HFACS classification were completed. Determination of the causes of each accident and their classification under the HFACS structure was carried out in the presence of a group of 3 domain experts. The expert group in this study has an adequate academic background in marine accident analysis, human factor and HFACS. The experts in the study classified the active failures, latent factors and operational conditions leading to the accidents according to the main structure of HFACS-PV. During the classification, in addition to the definitions in the framework of HFACS-PV, similar studies in the literature were utilized (Wiegmann and Shappell, 2001, Uğurlu et al., 2018, Zarei et al., 2019, Zhang et al., 2019, Uğurlu et al., 2020a, Yıldız et al., 2021). Experts adopted a consensus approach in making final decisions in the classification process. Therefore, results are expected to be obtained with an

acceptable consistency. After classification, the causes of accidents associated with the use of electronic navigational devices and their frequencies were placed in a hierarchical structure. In the third stage, a Bayesian network based on the HFACS was established. This network structure made it possible to qualitatively and quantitatively analyse how electronic navigation devices and their improper use caused accidents. Therefore, the study's Bayesian network structure could be considered an "Accident Network". In previous studies, the conditional probability tables of a Bayesian network were created based on data sets or expert opinions. This is a method that is used when the data set of expert opinions is limited. In this study, conditional probability tables were created based on accident data, as in the studies of Kelangath et al. (2012), Arsham et al. (2013), Hänninen et al. (2013), and Hänninen and Kujala (2014). The details of these tables are presented in Appendix 1. In the accident network, the relationships between the causes of accidents (each node in the Bayesian network) are established by considering the hierarchical structure of the HFACS, accident reports, and the occurrence of accidents. In the study, the steps described above were followed for each accident, and an accident network was created, as given in the "Test Case" section. At the end of the study, all network structures were integrated with each other and the final accident network of the study was constructed. GeNIe software was used to analyse the accident data (Bayes Fusion, 2017). Axiom tests were performed to test the accuracy of the Bayesian network. After verifying the accuracy of the network with Axiom tests, entropy reduction and node sensitivity analysis were performed at the last stage. The entropy reduction method was used to determine the nodes to be focused on at each level of the accident network. The effects of these nodes on the accidents were analysed using the sensitivity analysis method. The results demonstrated the effect of the errors made when using bridge-navigation devices on the likelihood of accidents occurring and can be used to determine recommendations to prevent their recurrence. The stages of the study are presented in Figure 2.

Figure 2. Flow chart of the study

# 4. Test Case 

In this step, a sample accident event and the formation of the Bayesian network, sample nodes, and calculations of marginalised and posterior probability values are explained. In this study, test case applications were made in the light of the studies in the previous literature (Matellini et al., 2013, Pristrom et al., 2016) and they are presented below.

As a test case, M/T Ovit tanker grounding was chosen. The chemical tanker vessel, which departed from the port of Rotterdam in the Netherlands and carried vegetable oil to the Italian Port of Brindisi, was ashore at the exit of the southern band of Dover Strait on the $18^{\text {th }}$ Sept. 2013. The grounding occurred on the night watch. A total of 18 factors played a role in the formation of the grounding. Latent factors, active failures and operational conditions interrelated to lead to the accident are summarized below.
i- Organizational Influence: Unqualified crew assignment (master, $3^{\text {rd }}$ officer and Vessel Traffic Service (VTS) operator), lack of training and familiarization (Electronic Chart Display and Information System (ECDIS)), inappropriate equipment (ECDIS).
ii- Unsafe Supervision: Inappropriate voyage plan, insufficient VTS assistance, insufficient supervision of voyage plan, lack of testing and control (ECDIS).
iii- Pre-condition for Unsafe Act: Lack of situational awareness (bridge team member), lack of situational awareness (VTS operator), malfunctions in the electronic navigations aid/ECDIS (audible alarm unit), guidance error (VTS), lack of coordination, loose team management.

iv- Unsafe Act: Skill-based error/ECDIS (route tracking), perceptual error/failure to detect the presence of the risk of grounding, violations of procedure/using a single position method in coastal waters.
$v$ - Operational Conditions: Night, narrow channel and heavy traffic.
The classification of the accident's causes under the main structure of HFACS for the test case is presented in Figure 3.

Figure 3. HFACS structure for the test case

In the next step, an accident network was set up based on the HFACS structure. The relationship between the nodes in the Bayesian network relies on the HFACS structure, accident reports and accident occurrences. Therefore, the Bayesian network structure is thought to be reliable and realistic (Figure 4).

Figure 4. Bayesian Network structure for the test case

# 4.1. Example of Conditional Probability Calculations 

For the sample calculation of conditional probability tables, child node "Oversight and Control" (Adequate/Inadequate) was selected. This node has 3 parent nodes: "Training and Familiarization" (Insufficient/Sufficient), "Legislations and Regulations" (Appropriate/Inappropriate) and "Crew Assignment" (Qualified/Unqualified). The "Oversight and Control" node is dependent on these three nodes (Figure 5).

Figure 5. Bayesian network structure for the "Oversight and Control" node

The "Crew Assignment" and "Legislations and Regulations" nodes are root nodes within these three nodes. The marginalised (unconditional) probability values of these two root nodes based on accident reports are shown below. It was seen that the unqualified crew assignment took place in 63 out of 290 accidents. Therefore, the marginalised probability value for the "Unqualified" status of the "Crew Assignment" node is calculated as $63 / 290=22 \%$ (Equation (3)). The probability value for "Qualified" status is $100 \%-22 \%=78 \%$. The marginalised probability value of the "Legislations and Regulations" root node for the "Inappropriate" status is $26 \%(76 / 290)$ and $74 \%(100 \%-26 \%)$ (Table 2) for the "Appropriate" status.

Table 2. Table for the marginalised probability values of the "Crew Assignment" and "Legislations and Regulations " root nodes

The "Training and Familiarization" node is chosen for the example of creating conditional probability tables. "Training and Familiarization " node is the child node of the "Crew Assignment" (Figure 5). Depending on the "Crew Assignment" node of the "Training and Familiarization " node, the conditional probability values are calculated as follows (Table 3):

Table 3. Calculation of conditional probability values for the "Training and Familiarization" node

In 63 out of 290 accidents examined, non-conformities due to unqualified crew assignment was observed. Training and familiarization was found to be insufficient in 43 of these 63 accidents. Therefore, the probability of "Training and Familiarization" to be "Insufficient" for the "Unqualified Crew" state of the "Crew Assignment" node is calculated

as $43 / 63=0.68$. The probability of "Training and Familiarization" to be "Sufficient" for the "Unqualified Crew" status of the "Crew Assignment" node is $1-0.68=0.32$.

Non-conformities related to crew assignment was not found in 227 of the analysed 290 accidents (Table 3). It was observed that in 59 of these 227 accidents, training and familiarization was insufficient. Therefore, for the "Qualified Crew" status of the "Crew Assignment " node, the probability of "Training and Familiarization" to be "Insufficient" is calculated as $59 / 227=0.26$. The probability of "Training and Familiarization" to be '’Sufficient" for the '’Qualified Crew’’ status of the "Crew Assignment" node is 1 - 0.26: 0.74. The conditional probability values of the "Training and Familiarization" node based on the "Crew Assignment" node are presented in Table 4.

Table 4. Conditional probability tables for the "Training and Familiarization" node

The posterior probability value of the "Training and Familiarization" node is $65 \%$ for the "Sufficient" status and 35\% for the "Insufficient" status (Figure 5).

$$
P\left(a_{1}\right)=\sum_{j=1}^{2} P\left(a_{1} \mid b_{j}\right) P\left(b_{j}\right)=P\left(a_{1} \mid b_{1}\right) P\left(b_{1}\right)+P\left(a_{1} \mid b_{2}\right) P\left(b_{2}\right)
$$

where $a_{1}=$ Training and Familiarization (Sufficient), $b_{1}=$ Crew Assignment (Qualified crew), $a_{2}=$ Training and Familiarization (Insufficient) and $b_{2}=$ Crew Assignment (Unqualified crew). $\mathrm{P}(\mathrm{TAF}=$ Sufficient $)=(0.74 \times 0.78)+(0.32 \times 0.22=0.65(65 \%)$

The probability of being insufficient of training and familiarization is:

$$
=1-0.65=0.35(35 \%)
$$

According to the Bayesian network founded in the study, there are 8 conditions in which "Oversight and Control" is adequate or inadequate (Table 5). Considering these conditions, the posterior probability values for the "Oversight and Control" node are $62.25 \%$ for the "Adequate" status and $37.75 \%$ for the "Inadequate" status (Figure 5).

Table 5. Conditional probabilities tables for the "Oversight and Control" node

According to Equations (6) and (7), the probability of the "Oversight and Control" node being "Adequate" is calculated as follows:

$$
\begin{aligned}
& P\left(A_{i} \mid B\right)=\frac{P\left(A_{i}\right) P\left(B \mid A_{i}\right)}{P(B)}, i=1,2,3,4 \ldots, k \\
& P(B)=P\left(A_{1}\right) P\left(B \mid A_{1}\right)+P\left(A_{2}\right) P\left(B \mid A_{2}\right)+\cdots+P\left(A_{k}\right) P\left(B \mid A_{k}\right) \\
& =\sum_{j=1}^{k} P\left(A_{j}\right) P\left(B \mid A_{j}\right) \\
& \mathrm{P}(\mathrm{OAC}=\text { Adequate })=[\mathrm{P}(\mathrm{OAC}=\text { Adequate }[\mathrm{TAF}=\text { Sufficient, } \mathrm{CA}=\text { Qualified Crew, } \mathrm{LR}=\text { Appropriate }) \\
& \times \mathrm{P}(\mathrm{TAF}=\text { Sufficient }) \times \mathrm{P}(\mathrm{CA}=\text { Qualified Crew }) \times(\mathrm{LR}=\text { Appropriate })]+ \\
& \text { [P }(\mathrm{OAC}=\text { Adequate }[\mathrm{TAF}=\text { Sufficient, } \mathrm{CA}=\text { Unqualified Crew, } \mathrm{LR}=\text { Appropriate }) \\
& \times \mathrm{P}(\mathrm{TAF}=\text { Sufficient }) \times \mathrm{P}(\mathrm{CA}=\text { Unqualified Crew }) \times(\mathrm{LR}=\text { Appropriate })]+ \\
& \text { [P }(\mathrm{OAC}=\text { Adequate }[\mathrm{TAF}=\text { Sufficient, } \mathrm{CA}=\text { Qualified Crew, } \mathrm{LR}=\text { Inappropriate }) \\
& \times \mathrm{P}(\mathrm{TAF}=\text { Sufficient }) \times \mathrm{P}(\mathrm{CA}=\text { Qualified Crew }) \times(\mathrm{LR}=\text { Inappropriate })]+ \\
& \text { [P }(\mathrm{OAC}=\text { Adequate }[\mathrm{TAF}=\text { Sufficient, } \mathrm{CA}=\text { Unqualified Crew, } \mathrm{LR}=\text { Inappropriate }) \\
& \times \mathrm{P}(\mathrm{TAF}=\text { Sufficient }) \times \mathrm{P}(\mathrm{CA}=\text { Unqualified Crew }) \times(\mathrm{LR}=\text { Inappropriate })]+ \\
& \text { [P }(\mathrm{OAC}=\text { Adequate }[\mathrm{TAF}=\text { Insufficient, } \mathrm{CA}=\text { Qualified Crew, } \mathrm{LR}=\text { Inappropriate }) \\
& \times \mathrm{P}(\mathrm{TAF}=\text { Insufficient }) \times \mathrm{P}(\mathrm{CA}=\text { Qualified Crew }) \times(\mathrm{LR}=\text { Inappropriate })]+ \\
& \text { [P }(\mathrm{OAC}=\text { Adequate }[\mathrm{TAF}=\text { Insufficient, } \mathrm{CA}=\text { Qualified Crew, } \mathrm{LR}=\text { Inappropriate }) \\
& \times \mathrm{P}(\mathrm{TAF}=\text { Insufficient }) \times \mathrm{P}(\mathrm{CA}=\text { Qualified Crew }) \times(\mathrm{LR}=\text { Inappropriate })]+ \\
& \text { [P }(\mathrm{OAC}=\text { Adequate }[\mathrm{TAF}=\text { Insufficient, } \mathrm{CA}=\text { Unqualified Crew, } \mathrm{LR}=\text { Appropriate }) \\
& \times \mathrm{P}(\mathrm{TAF}=\text { Insufficient }) \times \mathrm{P}(\mathrm{CA}=\text { Unqualified Crew }) \times(\mathrm{LR}=\text { Inappropriate })] \\
& \mathrm{P}(\mathrm{OAC}=\text { Adequate })=[1 \times 0.65 \times 0.78 \times 0.74]+[0.715 \times 0.65 \times 0.22 \times 0.74]+[0.64 \times 0.35 \times 0.78 \times 0.74]+ \\
& {[0.404 \times 0.35 \times 0.22 \times 0.74]+[0.10 \times 0.65 \times 0.78 \times 0.26]+[0.07 \times 0.65 \times 0.22 \times 0.26]+} \\
& {[0.05 \times 0.35 \times 0.78 \times 0.26]+[0 \times 0.35 \times 0.22 \times 0.26]} \\
& =0.3752+0.0757+0.1293+0.0230+0.0132+0.0026+0.0035+0 \\
& =0.6225(62.25 \%)
\end{aligned}
$$

The "Oversight and Control" node being "Inadequate" is calculated as follows:
$\mathrm{P}(\mathrm{OAC}=$ Inadequate $)=1-0.6225=0.3775(37.75 \%)$ (Figure 5).

# 5. Classification of Causal Factors in the HFACS Structure 

In this study, the coding process was performed regarding the HFACS-PV structure. Coding makes it possible to analyse the causes of accidents systematically. The coding process involved the classification of each cause of the accident according to the HFACS subcategories. During this process, each cause of accident was assigned a code, or an abbreviation, or explanation in the HFACS structure (Li and Harris, 2006, Chauvin et al., 2008). During the

coding process, the causes and frequencies of accidents were handled independently for each accident category. The operating errors used in the coding and all nonconformities (latent factors, active failures, and operational conditions) leading to their occurrence are detailed in Tables 6-10 for each level of the HFACS. Thus, all nonconformities in the HFACS structure were made comprehensible and clear.

Table 6. Nonconformities at the "Organizational Influence" level and their frequencies
Table 7. Nonconformities at the "Unsafe Supervision" level and their frequencies
Table 8. Nonconformities at the "Pre-Conditions for Unsafe Acts" level and their frequencies

Table 9. Nonconformities at the "Unsafe Acts" level and their frequencies
Table 10. Nonconformities at the "Operational Conditions" level and their frequencies

# 6. Establishment of a Bayesian Network Structure Based on the HFACS Structure 

After coding the causes of accidents according to the HFACS main structure, a Bayesian network connected to the main structure was formulated. A Bayesian network is used to demonstrate the relationships between causes in accident analysis studies with the help of nodes. Also, the conditional probability tables in the network mathematically explain how the nodes (causes of accidents) affect each other (Rausand, 2011, Hassall et al., 2019, Yu et al., 2019). The study's expert group has helped establish a Bayesian network for each of 290 accidents by considering HFACS-PV levels, similar studies in the literature, and the occurrence of the accident. Then, by combining the obtained 290 Bayesian networks, the final network of the study was obtained. The expert group has directed an arrow between nodes with a relationship of $5 \%$ or more in the 290 Bayesian networks in shaping the final Bayesian network. For example, between the "Training and Familiarization" and "Voyage Planning" nodes, there

were relations between 32 of 290 Bayesian networks. Therefore, the arrow was directed between these two nodes in the final Bayesian network. The Bayesian network in this study consists of 32 nodes and 5 levels (Figure 6). Table 11 contains descriptive information about HOFs (Human and Organizational Factors) in the HFACS-PV to which the nodes in the Bayesian network (Figure 6) correspond.

Table 11. Nodes in the Bayesian network and their nonconformities
Figure 6. Accident network (Bayesian network) structure for collision-contact and grounding accidents

# 6.1. Validation of the Bayesian Model 

Axiom tests were performed to prove the accuracy of the Bayesian network established in the study (Pristrom et al., 2016). As a result of the Axiom tests (Axioms 1-3) the validity of the Bayesian network established in the study was proven (Appendix 2).

### 6.2. Entropy Reduction and Sensitivity Analysis

After proving the accuracy of the study with axiom tests, entropy reduction and node sensitivity analysis were performed. Sensitivity analysis helps predict the damage to the system if the adverse event is maximum (Uğurlu et al., 2020a). In Bayesian network studies, sensitivity analysis reveals the effect of the change in the root nodes, main nodes or sub-nodes of the network on the result nodes. In other words, it allows predicting how changes made in system inputs will affect output (Dinis et al., 2020, Uğurlu et al., 2020a). The outputs of this study are collision-contact and grounding, and the inputs are the causes of the accident and operational conditions.

Performing a sensitivity analysis for each node is a time-consuming and challenging task. Instead, it would be more appropriate to identify the nodes that should be focused on at each level. In this study, an entropy reduction method is used to determine the nodes to which sensitivity analysis will be applied. The entropy reduction method in Bayesian network studies is applied to the probability of result nodes, and changes in the respective sub-nodes and main nodes are observed (Yang et al., 2009, Cai et al., 2013). In this study, entropy reduction is applied for result nodes "Collision-Contact" and "Grounding". In the entropy reduction method, the probability values of the result nodes were made first $0 \%$ and then $100 \%$, and the change in other nodes hosted by the network was observed (Table 12). The purpose of entropy reduction in this study is to identify the three most sensitive nodes to be subjected to sensitivity analysis for each HFACS level. The higher the change in probability value of the node due to entropy reduction in a Bayesian network, the more sensitive the node (Fan et al., 2020). To explain with an example, when entropy reduction is applied to the "Collision-Contact" node (when the probability value is first $0 \%$ then $100 \%$ ), the most affected nodes by this change is the "Oversight and Control" (12\%), "Crew Assignment" (11\%) and "Training and Familiarization" (9\%) for the first level of HFACS (Organizational Influence) (Table 12). Therefore, the nodes subjected to sensitivity analysis for the first level of HFACS will be these.

In the sensitivity analysis applications, the probability values of the nodes most affected by entropy reduction were first made $0 \%$ and then $100 \%$, and the change in the probability of the result nodes was revealed (Figure 7 and Figure 8). The aim of sensitivity analysis applications in accident analysis studies is to quantitatively analyse the impact of accident causes and operational conditions on accident formation. Sensitivity analysis results for the "Collision-Contact" and "Grounding" nodes are presented in Figures 7 and 8.

Table 12. Entropy reduction method results for collision-contact and grounding nodes

Figure 7. Sensitivity analysis results for collision-contact nodes
Figure 8. Sensitivity analysis results for grounding node

The final step in the sensitivity analysis is identifying the accident combinations and observing the effect of these combinations on the probability of an accident occurring. The accident network in Figure 6 was created based on the HFACS-PV framework. It would be appropriate to follow Figure 6 to ensure a clear understanding of this section. The network makes it possible to estimate the risk of accident occurrence based on variable conditions. In accordance with the HFACS-PV approach, unsafe acts and operational conditions at the last level of the Bayesian network must coexist for the accident to occur (Uğurlu et al., 2018, Sarialioglu et al., 2020, Uğurlu et al., 2020, Yıldız et al., 2021). In other words, marine accidents occur due to unsafe acts and a combination of environmental factors. Each accident contains at least two environmental factors, categorized as positive or negative: 1- Type of navigation and 2- Condition preventing visibility (Observed/Unobserved) or condition preventing vessel motion (Observed/Unobserved). The combinations that caused the accident in this study were created by taking into account the above explanations. Figures 9 and 10 show the sensitivity analysis results of the most possible combinations for each accident category.

Figure 9. Sensitivity analysis results of accident occurrence combinations for CollisionContact

Figure 10. Sensitivity analysis results of accident occurrence combinations for Grounding

# 7. Results and Discussion 

It is inappropriate to connect marine accidents to a single cause or to focus on only a few reasons for their occurrence. To prevent future accidents, their occurrence should be considered

holistically. This is possible by fully defining the root causes (unsafe acts), environmental factors and causal factors (latent failures) that are associated with accidents. If the correct relationship can be established between these factors in an accident cycle, it can be understood exactly how the accident occurred. Thus, it becomes possible to offer constructive solutions to prevent accident occurrence. In the Bayesian network based on the HFACS structure, a perfect accident network cycle will emerge if the causes of accidents are correctly linked to each other. In this study, a network structure was created to reveal the effect of nonconformities encountered in the use of new technologies on marine accidents. In this study, it was observed that 1,778 of the factors related to the operating errors that caused the accidents were categorized as collision-contact, and 1,332 were categorized as grounding accidents (Tables 610). Accidents are concentrated in coastal waters (grounding: 38\%, collision-contact: 29\%) and narrow channels (grounding: 50\%, collision-contact: 37\%) (Table 10). These results are like those of previous studies conducted within the scope of accident analysis (Arslan and Turan, 2009, Uğurlu et al., 2015a,). The prevention of accidents in restricted waterways is possible when training is adequate to ensure the familiarity of the captains with the region and their ships. In this way, captains who pass through restricted waterways can perceive the existing risks before the transition and prevent an accident by making the most appropriate decision for any emergency. $60 \%$ of collision-contact accidents and $61 \%$ of grounding accidents occurred on the night watch. It was observed that, in $25 \%$ of the accidents, there was not a lookout on the bridge. The fact that the accidents studied were concentrated during the night watch and that the absence of a lookout on the bridge was a factor in a quarter of the accidents revealed that there might be a relationship between the likelihood of ship accidents and fatigue. As stated in the studies of Uğurlu (2016), Uğurlu et al. (2020b) and Lützhöft et al. (2010), working at night negatively affects the energy level of sailors, and fatigue can cause otherwise avoidable errors when there is no lookout on the bridge.

The results of this study related to the accident network are evaluated under the headings below for each level of the HFACS.

# 7.1. Organizational Influence 

According to the Bayesian network sensitivity analysis results, the lack of training and familiarization, and the presence of an unqualified crew were found to be the most critical nonconformities for both accident categories on the organizational influence level (Figures 7 and 8). Lack of training and unfamiliarity with bridges' navigational devices were observed in 61 accidents. A bridge equipped with modern electronic navigation devices can be considered helpful for the officer of the watch (OOW). However, the results of this study and those of Nilsson et al. (2009), Khan et al. (2020), and Arif et al. (2020) showed that officers' lack of education or familiarity with these devices may turn this advantage into a disadvantage. It would be quite risky for OOW/bridge team to use or steer the integrated bridge-navigation devices if they were not familiar with them. In addition, bridge-navigation devices that differ between ships make it difficult to gain familiarity with both a ship and its navigational aids beforehand. Therefore, familiarity must be achieved before boarding the ship so that the issues with a lack of familiarity that may occur during the use of such devices can be eliminated. Bridge-navigation devices, which are continuously becoming more modernized and integrated, require qualified officers and seafarers. According to the BIMCO-ICS (2015) human resources report, it is expected that the amount of technologically advanced equipment used on ships will continue to increase until 2025; therefore, new cognitive demands will come to the forefront for future officers. This situation, which will be encountered soon, requires ships to be equipped with qualified seafarers with sufficient training infrastructure. In this study, unqualified crewrelated non-compliance was observed as the cause of the accident in 63 incidents (Table 6). As in other studies (Lobrigo and Pawlik, 2015, Horck, 2004, Kartal et al., 2019), this study proves that this phenomenon remains a problem for the maritime community. It is impossible to discuss

sustainable navigation safety if bridge team members are unqualified. For this reason, shipowners should be more selective than before when appointing crew to their ships. Deficiencies in the oversight and control mechanism can include risk assessment (collisioncontact: 29 accidents, grounding: 11 accidents). The nonconformities contained in this node can lead to nonconformities in voyage planning, planned maintenance, and tests and controls (Figure 6).

# 7.2. Unsafe Supervision 

In many previous studies, it was emphasized that the lack of a voyage plan played an important role in collision-contact and grounding accidents (Uğurlu et al., 2015a, MujeebAhmed et al., 2018). With the developing technology in the maritime industry, voyage plans that used to be complex and time-consuming to prepare can now be prepared in a short period. In addition, thanks to integrated bridge-navigation devices such as the Electronic Chart Display and Information System (ECDIS), Automatic Identification System (AIS), Global Navigation Satellite System (GNSS), and radar, which are hosted by modern bridges, voyage plans are easy to implement and follow. The Bayesian network sensitivity analysis results show the prominence of the voyage plan node for the level of "Unsafe Supervision" (Figures 7 and 8). The study found that there were nonconformities in the voyage plan in 15 collision-contact and 37 grounding accidents (Table 7). The most important reason for this finding is that, when a non-conformity that is overlooked when preparing a voyage plan is combined with other nonconformities, accidents may be unavoidable. The M/T Ovit accident is a good example of this phenomenon (MAIB, 2013). The fact that there was a lack of familiarity with the ECDIS device among officers, the officer in charge of preparing the voyage plan on the M/T Ovit drew the route on the shallows, and the alarm of the ECDIS device did not work were factors that accelerated the occurrence of this accident.

# 7.3. Pre-Conditions for Unsafe Act 

Nodes that stand out at the level of pre-conditions for unsafe acts in the Bayesian network are situational awareness, external and internal communication, and management activities. A lack of situational awareness is encountered when the bridge team's management is unaware of the current situation or conditions. Chauvin et al. (2008), in their study of a bridge simulator, found that $55 \%$ of young officers had a lack of situational awareness. In this study, situational awareness-related deficiencies were observed in 97 of the collision-contact accidents and 55 of the grounding accidents. According to the network created in this study, engagement with other activities during a watch negatively affected situational awareness weakened internal communication and led to inappropriate management activities (Figure 6). The most common types of engagements with other activities during a watch involved mobile phone conversations and laptop use (19 accidents). The most effective way to prevent this situation is to develop an audit-control mechanism and apply corrective sanctions for nonconformities. In this study, as in many previous studies in the literature, it is emphasized that lack of communication is the most significant factor affecting marine accidents (Uğurlu et al., 2015b, Sotiralis et al., 2016, Kartal et al., 2019). This study's results revealed that a lack of external and internal communication was seen in 99 of the 175 collision-contact accidents and 25 of the 115 grounding accidents. The "Management Activities" node is another important one within this structure. Inappropriate management activities were seen in 72 of the collision-contact accidents and 80 of the grounding accidents (Table 8). Inappropriate management activities included nonconformities such as loose team management, master's lack of authority, and failure in the management of emergency situations (Table 11). As seen in the Bayesian network, the "Management Activities" node is instrumental in the development of nonconformities pertaining to decision-based errors, skill-based errors, and violations (Figure 6).

# 7.4. Unsafe Act 

The focus of this study is the set of inappropriate actions related to bridge-navigation equipment. The first node assessed under this level pertains to skill-based errors. There were 104 nonconformities in collision-contact accidents and 71 nonconformities in grounding accidents. The most common skill-based errors in collision-contact accidents were associated with radar, and for grounding accidents, the most common skill-based errors were associated with the ECDIS and GNSS. The most common skill-based errors regarding radar devices involved the guard zone ( 24 accidents), the distance and time of the closest point of approach (19 accidents), radar range settings (14 accidents), trial manoeuvres ( 7 accidents), and parallel index technique (5 accidents) applications. The most common skill-based errors made by OOWs of the ECDIS were cross-tracking errors (6 accidents); regarding the GNSS, crosstracking ( 9 accidents) and anchor-watch ( 13 accidents) errors were the most common ones. One of the most important conclusions drawn from the Bayesian network in this study is that skillbased errors (made during device use) caused perceptual errors. Skill-based errors made during the use of bridge navigation devices could result in the development of perceived nonconformities, such as an inability to detect the presence of the target ship, detect the behaviour of the target ship, solve the problem in the system (Table 6). Unless devices are carefully and correctly managed, the workload of the officer doing the watchkeeping will increase under these circumstances, and it will become difficult to detect potential hazards. In this case, it is inevitable that ships' officers will make misguided decisions under the appropriate operational conditions, decisions will be delayed, or no action will be taken against dangerous situations, and accidents will become inevitable. The only way to avoid such accidents is to design hardware, software, and warning systems that prevent skill-based errors that occur through human-device interaction and make them available to ships' officers.

Another node at this level is the perceptual error. There were 159 perception-based nonconformities in collision-contact accidents and 107 in grounding accidents. The studies in the literature emphasize that situational awareness and a crew's unsafe acts (skill-based errors) have an indirect effect on subjective risk assessments (perceptual errors) (Cordon et al., 2017, Röttger et al., 2016, O’Connor and Long, 2011, Espevik et al., 2017). This study reveals that technology and interface failures may affect perceptual- and indirect decision-based errors in addition to these two elements.

Decision-based errors include late, faulty, and unstable manoeuvring by navigation officers. This type of error involves adopting the incorrect course of action in the face of a negative situation or failing to adopt the correct course of action in time. Nonconformities related to this node were identified 141 times in collision-contact accidents and 105 times in grounding accidents. Today's electronic navigation aids and their associated systems are based on advanced monitoring and control systems that ensure the safe navigation of ships. However, the fact that the existing systems are incapable of being completely independent (autonomous) decision-makers or implementers requires a human watch officer to be included in the decision mechanism. Decision-based errors are much more complex than perceptual and skill-based ones. As can be seen from the Bayesian network, there are many components that can cause issues to emerge. Currently, the lack of fully autonomous ships results from the failure to understand exactly how to solve decision-based errors.

Violations are divided into three sub-categories: regulations, procedures, and abuse of authority. Nonconformities related to this node were identified 246 times in collision-contact accidents and 159 times in grounding accidents. This node is the most instrumental one in the formation of collision-contact and grounding accidents. Violations arose because of inappropriate management activities and the inability to provide management and guidance, and are the final conditions necessary for an accident to occur (Figure 6). COLREG

(Convention on the International Regulations for Preventing Collisions at Sea) violations were the most instrumental ones in collision-contact accidents (Table 9). COLREG Rule 5 (improper lookout), COLREG Rule 6 (unsafe speed), COLREG Rule 2 (responsibility in case of risk of collision), and COLREG Rule 34 (failure to provide sound and light warnings in case of risk of collision), are the most violated COLREG rules concerning collision-contact accidents. The findings are consistent with the COLREG violations reported in previous studies (Martins and Maturana 2013, Uğurlu et al., 2015a). For grounding accidents, procedural violations, rather than regulatory ones, play a large role in accident occurrence (Table 9). 49 of these violations were related to the use of electronic navigation aids. It has been observed that, in grounding accidents, especially those associated with the use of the Bridge Navigational Watch Alarm System (BNWAS), rudder control systems and echo sounder devices caused them. The most common procedural violations involved the closure of these devices in coastal areas, especially in ports, narrow channels, and anchorage areas. It is unacceptable to leave these devices disabled during navigation, especially during the night watch.

# 7.5. Operational Conditions 

Another category that is instrumental in the occurrence of accidents consists of operational conditions. There is an interaction between operational conditions (fog, currents, wind, tides, etc.) and unsafe actions rather than a cause-and-effect (Ugurlu et al., 2018). As a result of this interaction, ship accidents occur. Spatial constraints (narrow channels, coastal waters) and visibility restrictions (fog, environmental lights) were found to be complementary factors in the occurrence of accidents (Figure 6). The Bayesian network's sensitivity analysis results show that narrow channels were a factor in collision-contact accidents, and rain and fog were included in the conditions affecting visibility. In this study, although the night was not considered a visibility restriction, it was involved in 104 collision accidents and 70 grounding accidents. This reveals the effect of the night on the likelihood of accidents occurring. The

operational conditions that stand out in grounding accidents are narrow channels and conditions that prevent a ship's movement. The results obtained during this study are like those shown in other studies (Xi, et al., 2009, Chen and Chou, 2012, Zhang, et al., 2018). However, the existing risks can be eliminated by choosing personnel who are familiar with the region and ship.

# 7.6. General Considerations 

According to the Bayesian network's sensitivity analysis results, for collision-contact accidents (Figure 7), the most likely accident scenario occurred when a violation (COLREG, STCW, etc.) was made in combination with restricted visibility in a narrow channel. It was shown that, in such a situation, the probability of a collision increased by $57 \%$. When the same situation occurred in coastal waters instead of narrow channels, the probability of collision increased by $44 \%$. In addition, it was seen that decision-based errors affected collision-contact accidents. It was observed that the probability of an accident increased by $44 \%$ when decisionbased errors were made in a narrow channel with restricted visibility (Figure 9).

Grounding accidents were most likely when there was a combination of a violation in a narrow channel (58\%) and conditions that could prevent vessel motion. When the same situation occurred in an anchorage, the probability of an accident increased by $51 \%$ (Figure 10). Navigation type is significant in accident occurrences, and narrow channels are the marine area where both types of accidents are most likely to occur, which is consistent with the studies in the existing literature. Similar results were obtained in the studies in which Uğurlu et al., (2015a) dealt with ship accidents occurring involving oil tankers. The possibility of both grounding and collision-contact accidents being concentrated in narrow channels reveals the need to focus on preventive measures in this area.

## 8. Conclusion

With the presence of much more modern and integrated navigation systems in bridges than ever before, shipping and the handling of ships has become much easier. It is possible to

use the new applications of such technology in the most effective way by familiarising officers with them. However, incompatibilities encountered in the operation of technological devices can cause accidents. This study was conducted to reveal the place and importance of technology in ship accidents. In the study, a network structure that summarises the occurrence of ship accidents based on the HFACS framework is presented. The critical results and recommendations found in the study are explained below:

- The network structure presented in this study allows analysing the impact of nonconformities encountered in the operation of technological devices on accident occurrence. With the help of conditional probability tables, it has become possible to analyse the root causes, causal factors, and operational conditions that cause accidents, and observe how these factors affect accidents. Marine accident investigators can understand the occurrence of the accident, which they will examine, by considering each node in the accident network presented in this study and the relationship between the nodes.
- Unqualified crew assignment and lack of training and familiarization were found to be the most critical factors at the organizational influence level. The most common nonconformities under the title of training and familiarization are the lack of familiarity with ship equipment or the voyage area. It is impossible to maintain sustainable navigation safety with its unqualified bridge crew unfamiliar with these devices. Adoption of training programs that will ensure seafarers' familiarity with the bridge and the navigational aids before embarking on the ship can be effective in preventing accidents.
- The results of this study revealed that accidents occurred due to the inactivation of the BNWAS device, especially during night watches. Therefore, it is necessary to prevent the BNWAS device from being deactivated by the ship's personnel during navigation. For example, the automatic activation of the device by the operation of the main engine and not being taken into a passive position as long as the main machine is running can be considered a

solution. Also, adding software to the BNWAS device to show working hours and controlling the device's working hours records during port or flag state control inspections may effectively prevent accidents caused by fatigue and lack of situational awareness.

- The accident network has shown that skill-based errors made in bridge-navigation devices did not cause the accident directly. All nonconformities under skill-based errors affect perception negatively (Table 9). Also, perceptual errors were found to be one of the important factors that caused decision-based errors. Decision-based errors, combined with appropriate environmental conditions, directly cause an accident. It does not cause the formation of any other non-conformities such as skill-based errors or perceptual errors. Therefore, the consequences are severe, and it is essential to identify the underlying non-conformities in order not to make these errors again in the future.
- Violations of regulations are the most frequently observed unsafe acts, especially in collision-contact and have the most significant impact on accidents. The most common violation under this framework is the COLREG violation. It would be helpful to define the COLREG rules to the devices through the interface software to be added to the bridge electronic navigation devices and to provide the OOW with recommendations to prevent the occurrence of accidents by these devices. Thus, the officer will be able to make the safest manoeuvre by considering the offers of the device in case of accident risk. The allocation of intelligent systems to detect danger in the bridge may be considered an accident prevention solution. The automatic adjustment of the user settings in the appropriate devices (RADAR, ECDIS, echo sounders, etc.) by considering the risk factors such as traffic density, visibility and regional restriction by the intelligent systems may be effective in preventing OOW-induced errors (skill-based errors). In such an environment, OOWs' role in the bridge will be the decision-making mechanism. The officer is obliged to perform safe action taking into account all processed data associated with the technology. Thus, it would be ensured that the OOW reacts quickly and on time to events.

- It was found that both grounding and collision-contact accidents were concentrated in narrow channels. The prevention of accidents in these restricted waters can be achieved by ensuring that the masters are familiar with the operational area. In this context, creating new training modules at the IMO and conducting these training in the presence of local marine pilots can be considered as a measure to prevent accidents in restricted waters. Thus, masters passing through these restricted waters will perceive the existing risks before the passage, avoid possible accidents by making the most appropriate manoeuvre in an emergency that may occur, or minimize the consequences that may arise if the accident occurs.

In this study, the most common user mistakes made by officers in bridge-navigation devices were determined. In future studies, researchers' work on decision support systems and software that will minimize these errors may help prevent skill-based error. It has been observed that the insufficiency of the existing fault warning systems on the bridge-navigation devices may also cause accidents. Therefore, it will be useful to develop integrated software that will detect interface malfunctions. If incorrect information given by one device is detected by another with warnings given to the OOW, it will increase the officer's situational awareness on the bridge.

# Acknowledgments 

This research is produced from the PhD thesis entitled "The Analysis of Role and Importance of Technology in the Occurrence of Marine Accidents" at the Graduate Institute of Natural and Applied Sciences, Karadeniz Technical University. The authors would like to thank anonymous reviewers for their constructive suggestions.

# Appendix 1 


# Appendix 2 Bayesian Network Model (Accident Network) Verification 

Axiom 1. Axiom 1's requirements were tested for the validity of the established accident network. A slight increase or decrease in the probability of each parent node should definitely result in the effect of a relative increase or decrease in the probability of the child node. Table A6 shows the changes of the posterior probabilities of the consequences given changes in the prior probabilities of the respective parent nodes. For example, if the triggering factor for grounding occurs (observed 100\%), the probability of grounding increases from $10 \%$ to $28 \%$ and, if it is not observed the probability of grounding is reduced to $0 \%$. Similarly, if the operational conditions for grounding are observed, the probability of grounding increases from 10 to $37 \%$, and if the operational conditions for grounding are unobserved, the probability of grounding decreases to $0 \%$. The same procedure was applied to all child nodes and their parent nodes in the Bayesian network. All the obtained results show that the Bayesian network fulfils the requirements of Axiom 1 (Table A6).

Table A6. Axiom 1 test results for grounding


Axiom 2. Given the variation of subjective probability distributions of each parent node, its influence magnitude to the child node should be kept consistent. Figure A1 shows the change in the probability of the "Decision-based Error" node with "Perceptual Error", "Coordination and Guidance" and "Management Activities". The general trend of the results indicates a proportional increase of the posterior probabilities given the increase in the individual prior probabilities. In other words, there is a consistent increase of probabilities for "Decision-based Error = Yes" due to the increase of probabilities of "Perceptual Error = Observed", "Coordination and Guidance = Insufficient" and "Management Activities = Inappropriate". A similar observation can be made when analysing the other nodes in the Bayesian network. A gradual change in the probability distributions of the parental nodes has a consistent effect on the child nodes. The Bayesian network satisfies Axiom 2 (Figure A1).

![img-10.jpeg](img-10.jpeg)

Figure A1. Probability changes of the "Decision-based Error" node

Axiom 3. Axiom 3 requires that the individual effect of each of the parent nodes on the child node should not have more effect than the collective effect (Jones, et al., 2010, Li, et al., 2014). The child node "Management Activities" was selected as the test sample for Axiom 3. "Management Activities" (child node) has four parents: "Coordination and Guidance", "External and Internal Communication", "Voyage Planning" and "Management and Supervising".
"Coordination and Guidance = Insufficient", " External and Internal Communication = Inadequate", "Voyage Planning = Unsafe" and "Management and Supervising = Unsuccessful" are entered individually. The occurrence probability of "Management Activities = Inappropriate" is estimated as $44 \%, 81 \%, 53 \%$ and $51 \%$, respectively. When "Coordination and Guidance = Insufficient", "External and Internal Communication = Inadequate", "Voyage Planning = Unsafe" and "Management and Supervising = Unsuccessful" are entered together, the occurrence probability of "Management Activities = Inappropriate" is estimated as 100\%. These results are consistent with Axiom 3. Further tests were also conducted for all accident nodes together with their corresponding sub-evidence.