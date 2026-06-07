# Accident Precursor Probabilistic Method (APPM) for Modeling and Assessing Risk of Offshore Drilling Blowouts - A Theoretical Micro-scale Application 

Pedro Perez ${ }^{1,2}$, Henry Tan ${ }^{1}$<br>${ }^{1}$ Lloyd's Register Foundation (LRF) Centre for Safety and Reliability Engineering, School of Engineering, University of Aberdeen, Aberdeen AB24 3UE, UK<br>${ }^{2}$ Witt O'Brien's Brasil, Brazil


#### Abstract

This paper proposes and explains the application of an accident precursor probabilistic method (APPM) that aims to overcome the usual limitations of existing quantitative risk analyses (QRA), with a focus on offshore drilling blowouts. This limitation is implicit in generic QRAs that do not appropriately reflect the specificities of the rig and its environment, without considering systems arrangements, risk influencing factors (RIF) or current operational conditions.


The proposed method is divided into three pillars: (i) a guideline for modeling the blowout probability considering specific conditions or well, rig, safety barriers and risk influencing factors (RIF) objectives; (ii) a proposed axiom combined with a scoring system to quantify the RIF into the QRA; and (iii) a risk based plan framework, to allow risk update and sequential learning during the operational phase.
The APPM is based on a Bayesian Network (BN) mathematical framework. It allows the pre-defined axiom to be entered into a conditional probability table (CPT). This approach, combined with the assessment of the company's safety management system, allows the incorporation of RIF into the QRA.
The developed APPM is applied to a theoretical micro-scale calculation. The result demonstrates its suitability for addressing common aspects inherent to the blowout phenomenon, including uncertainty, dependability between variables (common cause factors and redundant failures), and dynamism due to planned or unplanned operational changes in systems, drilling parameters and current conditions of RIF. Limitations of the APPM are also identified, and suggestions are made for future work on this topic.

# List of Definitions and Abbreviations 

BN - Bayesian Network
BOP - Blowout Preventer
BT - Bow Tie
CPT - Conditional Probability Table
DAG - Direct Acyclic Graph
ET - Event Tree
FT - Fault Tree
G\&G - Geological and geophysical parameters
HOF - Human and Organizational Factors
KPI - Key Performance Indicator
MoC - Management of Change
MTTF - Mean Time to Failure
QRA - Quantitative Risk Analysis
RIF - Risk Influencing Factors
SMS - Safety Management System

## List of symbols


# 1. INTRODUCTION 

Offshore drilling is an activity inherent to the oil and gas industry, as it is essential in confirming the economic feasibility of hydrocarbon reservoirs. However, risks related to uncertainties, i.e: lack of knowledge about risk influence factors (RIF), and risks inherent to typical major accident hazards are associated with this activity. Blowouts are assumed to be one of the major contributors to risk in offshore drilling (Rosenberg \& Nielsen, 1997).

The risks inherent to drilling projects are assessed prior to and during operations. Risk assessment studies are part of the regulatory framework in several countries and are critical documents for the permit process for drilling activities. For instance, the UK Health and Safety Executive (UK) (Health and Safety Executive, 2006) states that the primary objectives of risk assessment in this context are to identify and rank risks so that they can be adequately managed, and to examine associated risk reduction measures to determine those which are most suitable for implementation.

On new frontiers, most exploratory blocks and potential reservoirs are generally located in deep waters and unknown geological and geophysical (G\&G) environments. This requires design and construction of wells under complex, hazard conditions (high pressures and temperatures) and with higher degrees of uncertainty, leading to the conclusion that the blowout risk also increases. According to the National Commission (Skelet et al., 2006b) on the BP Deepwater Horizon Oil Spill and Offshore Drilling, the Macondo blowout requires a reassessment of the risks associated with the activity of offshore drilling.

Nevertheless, the current practice in the oil \& gas industry has been to assess the risks of complex drilling projects based on the same traditional QRA methods that are applied to common drilling projects, with a lesser degree of complexity and uncertainty, i.e: where wells have standard designs and are located in environments where geological and geophysical (G\&G) information is readily available. In cases when wells are designed under uncertainty and risk, deterministic safety factors are seldom applied to estimate the risk and, in some cases, may even discontinue the project (Dahlin et al., 1998).

Traditional QRA methods are characterized by relying on traditional statistical techniques and, as consequence, are limited in addressing dependability, uncertainty and changes in the risk picture overtime (risk update) (Aven \& Bjerga, 2009). These methods may be suitable for assessing regular drilling projects, but when applied to complex, risky and dynamic drilling projects, it generates generic risk assessments that are not reliable in reflecting specifics that could significantly change the risk profile of the activity.

This research paper proposes an accident precursor probabilistic method (APPM) that was designed for overcoming the limitations of traditional QRA, with a focus on addressing specificities related to blowout risk in deep-water offshore drilling. Therefore, the following specifications for the APPM were established: address specificities of well and top-side safety barrier systems and elements, easily reflect changes in drilling operational conditions and properly reflect the effect of risk influencing factors (RIF) on the performance of safety barriers.

This research paper is divided into the following sections:

- Review of traditional and contemporary QRA methods, focusing on the oil and gas industry;
- Presentation of the APPM, including expected advantages and limitations;
- Demonstration and discussion of its application in a micro-scale theoretical example;
- Discussion about the APPM's limitations and suggestions for future research work; and
- Conclusions;

# 2. REVIEW OF OFFSHORE QRA METHODS 

The IADC HSE Case Guidelines (International Association of Drilling Contractors, 2015) are the present benchmark for offshore drilling risk assessment. The Guidelines provide a framework for developing an integrated health, safety and environmental management system for use in reducing the risks associated with drilling activities. The guidelines are divided into the following major parts:

- Drilling contractor management system;
- RIG/ MODU description and support information;
- Risk management;
- Emergency response; and
- Performance monitoring.

The HSE Case Guidelines demonstrate that risks associated with major and other workplace hazards have been adequately assessed and that risk-reducing controls within the drilling contractor's management system have been applied (International Association of Drilling Contractors, 2015). IADC HSE Guidelines are the outcome of good practices for drilling contractors. Even though they are not compulsory, they are a standardized aspect of HSE that operators, drilling contractors, authorities, and oil and gas producers (industry stakeholders) should consider as part of their Health, Safety and Environmental (HSE) Management Systems.
They are also a methodology for drilling contractors to acknowledge the application and requirements of operations aligned with other offshore international standards, such as International Safety Management Code requirements (ISM) of the International Maritime Organization (IMO). They are a risk management tools which helps to demonstrate the compliance of agreed HSE-applicable regulations with stakeholders' expectations. This is especially useful when drilling contractors operate in different global regulatory jurisdictions (Holand, 1997).

The challenge when modeling a blowout hazard is to conduct an analysis which reflects the actual equipment and procedures that are being used. Commonly utilized models are unable to distinguish between different platforms, systems and operators(Vinnem, 2007). In addition, the models used for quantification are not suitable for dealing with significant levels of operational uncertainty and changes, which are also inherent to most drilling projects. This combination leads to generic and static risk analyses.
A review of several studies (Skogdalen \& Vinnem, 2012), reinforced by the author's own professional experience, has identified the following limitations of blowout QRAs:

- Blowout risk assessments are generic. They do not reflect the specific risk influence factors (RIF) of the project, mainly those related to human and organizational factors (HOF) (Skogdalen \& Vinnem, 2011);
- They are strongly dependent upon historical accident data banks that don't address the uncertainty or specificities of the project. However, in some cases the frequencies can be adjusted based on the types of operations(International Association of Oil and Gas Producers, 2010);
- They are modeled using a set of event trees (ET) and fault trees (FT), without considering dependability effects on the calculations, as demonstrated by (Khakzad et al., 2013);
- Risk assessments are static, as the risk is not updated in light of operational changes and new information that becomes available (Khan et al., 2016);
The risk models also do not address the specificities inherent to the basic causes of a kick, which is the major blowout accident precursor. In addition, quantification is limited to a review of accident frequency data banks that, in most cases, are not adjusted for the specificities of the system and operations. As a consequence, specific risk influencing factors (RIF) of geology, equipment, systems, and human and organizational factors (HOF) are not considered in the risk model, as already discussed by Skogdalen \& Vinnem $(2011,2012)$ and Vinnem $(2007)$. These findings are also in line with the limitations of QRA

applied to chemical process industries, as presented by Villa et al. (2016), who highlight that conventional risk analysis methodologies suffer the disadvantage of being intrinsically static, which may preclude possible updates and integrations with overall average risk. For this reason, during the past decade, great effort has been devoted to the development of dynamic assessment and management approaches that consider the evolution of conditions affecting risk.

These contemporary approaches are mostly designed for chemical process industries, but some of them are derived from the nuclear industry. Villa et al. (2016) presents an overview on how risk analysis methodologies and applications have rapidly evolved in a dynamic direction (Dynamic Risk Analysis), to address risk issues in a continuously evolving environment and to overcome the limitations of traditional techniques.

Khan et al. (2016), investigated the main contributions in the areas of Dynamic Risk Assessment (DRA) and proposes an overall framework for dynamic risk management for process facilities. The update mechanism, advantages, and disadvantages of the following methods were addressed: Bayesian network, dynamic bow-ties, principal component analysis (PCA), loss functions, and risk barometer. The authors highlight the existence of improvement opportunities in technical aspects of the DRA field, especially for overcoming the inherent structural limitations of the Bayesian Network (BN) which is broadly used, as it does not allow consideration of multivariate systems with different marginal distributions and complex non-linear dependencies.
Paltrinieri et al. (2016) reviewed, analyzed, and classified different risk assessment approaches, then presented their limitations for application to the process industry. The work highlights the application of a novel method based on indicators, the Risk Barometer, that demonstrated valuable features in its first applications, as it is capable of continuously monitoring risk-picture changes and supporting decision makers on a daily basis. However, the method requires the availability of a large amount of real-time data, the collection of which is made easier by the extensive use of information and communication technologies in process systems.

In addition, Paltrinieri et al. (2016) suggests that the incorporation of Bayesian Network (BN) into risk assessment may be another interesting focus for both research and industry purposes, mostly because it allows a systematic approach that considers human error and management influences. Ale et al. (2014) also highlights the BN capability of providing a useful tool for dealing with uncertainty and with information from different sources, such as expert judgment, observable information or experience, and common causes and influences of human factors (Paltrinieri et al., 2016).

Drilling projects may differ in many aspects when compared to chemical process systems, mostly in terms of the degree of automation and process stability. Chemical processes have well-defined design and operational envelopes, combined with relatively automated instrumentation systems. However, in drilling, operational parameters are mostly related to operational performance and Geological and Geophysical (G\&G) conditions. In addition, instrumentation is less automated and consequently the drilling system's reliability is more dependent upon human and organizational factors (HOF). This combination of uncertainty, planned and unplanned changes in the well operations, and a significant degree of dependency on human and organizational factors (HOF) when compared to other high reliability industries, makes drilling and consequently blowout risk assessment and management, a quite singular subject.
Extensive reviews and studies (Reason, 1997) have already estimated that 70\% of offshore accidents happen due to human failures and the remaining $30 \%$ is attributed to technical failures (Cai et al., 2013). Specifically, in the Macondo well blowout, there were a series of technical mistakes, bad engineering judgements, improper maintenance and communication, lack of leadership, structure, and component failures that all contributed to the tragedy (Pranesh et al., 2017).

Specific approaches for the oil \& gas sector have also been a focus of the scientific field, dedicated to improving current QRA methods. A brief review of some of these modern methods, capable of updating risk and/ or incorporating RIF into the QRA with a focus on the oil and gas sector, is provided as follows:

- Khakzad et al. (2013) present a risk analysis of drilling operations using both bow-tie and Bayesian network approaches. Bayesian network is shown to take priority over bow-tie since: (i) it considers both common cause failures and conditional dependencies among the primary events of the well control system; (ii) it allows probability updates and sequential learning by considering accident precursors, and (iii) it also helps to identify the most probable sequence of events leading to a blowout.
- Khakzad et al. (2014) present a Bow-tie analysis and real-time barrier failure probability assessment of offshore drilling operations involving subsurface Blowout Preventers. The Bow-tie model is used to represent the potential accident scenarios, their causes, and the associated consequences. Real time predictive models are developed for the failure probabilities of key blowout barriers using a physical reliability model of constant strength and random stress to allow risk updates using realtime observed data.
- Abimbola et al. (2014) illustrate the application of a precursor-based hierarchical Bayesian analysis for updating the risk of major accidents, examining two types of likelihood functions (binomial and multinomial distributions). The method was applied in a case study, updating the failure probability of traditional offshore blowouts' safety barriers.
- (Ahmad, Pontiggia, \& Demichela, 2014) propose a Bayesian methodology (MEDIA) to incorporate human and organizational factors into the risk assessment of technical systems. In MEDIA, a Bayesian Network combines a set of organizational factors classified into two states (good or bad) with a set of human factor taxonomies. The model can be used in two possible ways: (i) if an industry provides states of organizational factors to calculate HOF risks, or (ii) if they evaluate different organizational characteristics to compare HOF risks associated with specific organizational structures, to recommend the most suitable solution for an industry.
- Landucci \& Paltrinieri (2016a, 2016b) propose the TEC20 method (frequency modification methodology based on Technical Operational and Organizational Factors), which is based on an aggregated set of indicators, and their contribution to the expected leak frequency is systematically evaluated though a specific procedure. The method is suitable for implementation in dynamic risk assessments to provide an update mechanism that allows revision of accident frequency during the lifecycle of an installation. This work also compares TEC20 with other relevant methods for frequency tailoring, such as: CCPS Method (Center of Chemical Process Safety, 2000) based on arbitrary expert judgment evaluation; API 581 Method (American Petroleum Institute, 2000), which is based on the determination of equipment and management modification factors obtained from design data and site inspection; MANAGER (Pitblado, Williams, \& Slater, 1990) which is based on the determination of a management modification factor obtained from site inspection, implicitly covering technical aspects; and DNV (Pitblado, Bain, Falck, Litland, \& Spitzenberger, 2011) which is based on scoring safety barriers, obtaining frequency reduction factors, and implicitly covering managerial aspects.
Regarding human factors specifically, for about a decade the oil and gas industry have been looking for alternatives to incorporating HOF into QRA, as verified by the 2010 OGP report (International Association of Oil and Gas Producers, 2010). More recently, successful projects have been implemented in this specific area, such as Risk OMT program (Vinnem et al., 2012) that represent a further development of Barrier and Operational Risk Analysis (BORA) (Aven et al., 2006; Skelet et al., 2006a, 2006b).
BORA (Skelet et al., 2006a, 2006b) analyses the effect of safety barriers introduced to prevent hydrocarbon releases, and how platforms' specific conditions of technical, human, operational, and organizational risk influencing factors influence barrier performance. This work was based on the general framework and definition of safety barrier systems and elements suggested by (Sklet, 2006), which is also adopted in the

context of the present research paper. (Sklet, 2006) defines safety barriers as physical and/or non-physical measures planned to prevent, control or mitigate undesired events or accidents. The measures may range from human actions or a single technical unit, to a complex socio-technical system. 'Planned' implies that at least one of the purposes of the measures is to reduce risk. In line with (ISO 13702, 2015), 'prevent' means to reduce the likelihood of a hazardous event, 'control' means to limit the extent and/or duration of a hazardous event to prevent escalation, and 'mitigate' means to reduce the effects of a hazardous event.
A 'barrier element' is a component or subsystem of a barrier system that itself is not sufficient to perform the designed safety function, and 'risk influencing factor' (RIF) is any factor, whether technical or human and organizational (HOF), capable of affecting the performance of a barrier function by affecting an element or system (Sklet, 2006).
The Risk OTM method (Vinnem et al., 2012) departs from the safety barrier framework introduced by BORA (Skelet et al., 2006a, 2006b), taking advantage of a Bayesian approach combined with a scoring system for modelling human influences on both an operational and organizational level on offshore process leaks, focusing on maintenance work. The evaluation of the method's application in this context was demonstrated by (Gran et al., 2012).
More recently, (Strand \& Lundteingen, 2016) applied the principles of Risk OMT to offshore drilling operations, with a focus on quantifying human reliability. The authors concluded that the method is still novel for well drilling human reliability analysis (HRA) and QRA, but may need further empirical validation to demonstrate it has the necessary reliability to be a practical tool for risk management in global offshore drilling operations. The same authors (Strand \& Lundteingen, 2016) suggest that there are improvement opportunities in regard to limiting the number of assumptions, and the use of expert judgments to substitute observations such as field data, human resource data, and simulator training data.
The proposed accident precursor Bayesian Network (BN) method for modeling the risk of deep-drilling blowouts suggested by this research paper also takes advantage of these works, especially Risk OMT (Vinnem et al., 2012), since it employs a Bayesian approach to allow risk updates based on the effect of RIF in the performance of safety barriers.
The major differences between Risk OMT and the APPM are the following: (i) the procedure for quantifying the effect of the RIF and integrating it into the QRA (scoring system and axiom); (ii) the proposed modeling approach divided into three levels; and the proposed risk update mechanism (risk-based plan).

# 3. APPM FOR MODELING AND ASSESSING THE RISK OF OFFSHORE DRILLING BLOWOUTS 

The APPM for modeling and assessing the risk of drilling blowouts relies on the pillars illustrated in Figure 1.

![img-0.jpeg](img-0.jpeg)

Figure 1: Pillars of the proposed risk-assessment method.

The Bayesian Network method (BN) is the mathematical framework that integrates all pillars presented by Figure 1, allowing them to: decode the proposed axiom into a simple mathematical rule; address dependability between random variables, including common cause RIF affecting the performance of a safety barrier; and implement sequential learning and risk updates based upon new evidence collected by the routine implementation of SMS. Each one of these pillars was defined in accordance with the previously mentioned specifications of the design method:

- Three-level modeling (Section 3.1) consists of simple guidelines to facilitate modelling, in accordance with the specifications of the proposed method. It assures that specificities inherent to drilling projects, including safety critical barrier elements and RIF, are properly identified;
- The axiom and scoring system (Section 3.2) were designed to allow the incorporation of RIF into QRA, in a simpler and more transparent way when compared with similar Bayesian methods;
- The design and implementation of a customized risk-based plan (Section 3.3), aligning the company's Safety Management Systems (SMS) with the axiom and scoring system allows risk updating and sequential learning based on operational changes and the observation of new evidence.


# 3.1 Three-Level Modeling Guidelines 

The three-level modeling guidelines were organized in accordance with three distinct modeling objectives. The three-level modeling guidelines are presented in Table 1.

Table 1: Three-level modeling guidelines.


# 3.2 Axiom and Scoring System 

Bayesian statistics were adopted to solve several variations of problems, mostly involving dynamism and uncertainty, as demonstrated by (Pourret, Naim, \& Marcot, 2008). Directed acyclic graphs (DAG) are used to map the cause-and-effect relationships between barrier elements and systems with the groups of risk influencing factors (RIF) that may affect their performance.

A basic DAG mapped cause-and-effect relationship between two events (A and B) is based on the simplest form of the Bayes' theorem (Equation 1):

$$
\mathbf{P}(\mathbf{A} \mid \mathbf{B})=\frac{\mathbf{P}(\mathbf{B} \mid \mathbf{A}) \mathbf{P}(\mathbf{A})}{\mathbf{P}(\mathbf{B})}
$$

- $\mathrm{P}(\mathrm{A})$ and $\mathrm{P}(\mathrm{B})$ are the probabilities of A and B independent of each other;
- $\mathrm{P}(\mathrm{A} \mid \mathrm{B})$, is known as posterior probability, it is the probability of A given that B is true; and
- $\mathrm{P}(\mathrm{B} \mid \mathrm{A})$, is the conditional probability of event B given that event A is true.

A simple change to the mathematical framework is proposed, changing the focus of the analysis to the term $\mathrm{P}(\mathrm{B} \mid \mathrm{A})$ instead of the traditional posterior probability term $\mathrm{P}(\mathrm{A} \mid \mathrm{B})$, from the most simple form of the Bayes' theorem.

Thus, the updated failure probability of a barrier element or system, in accordance with the conditions of a group of ' $n$ ' risk influencing factors (RIF), is represented by the direct acyclic graph DAG shown in Figure 2.
![img-1.jpeg](img-1.jpeg)

Figure 2: DAG representation of failure probability of barrier element or system.
Equation 2 is a Bayesian inference obtained from the traditional Bayes theorem (Equation 1), with the purpose of calculating the posterior failure probability of a barrier element or system given the specific conditions of ' $n$ ' RIF:

$$
P\left(\hat{E} \mid C_{1}, C_{2}, \ldots, C_{n}\right)=P(\hat{E}) \times \prod_{i=1}^{n} \frac{P\left(C_{i} \mid \hat{E}\right)}{P\left(C_{i}\right)}
$$

Bayesian inference derives the posterior probability as a consequence of two antecedents, a prior probability and a probability distribution which, in this case, is derived from observable data:

- $\mathrm{P}\left(\hat{\mathrm{E}} \mid \mathrm{C}_{1}, \mathrm{C}_{2}, \ldots, \mathrm{C}_{\mathrm{n}}\right)$ is the posterior probability (Failure if TRUE and Operational if FALSE) of the barrier element or system given the influence of a specific group of risk factors $\left(\mathrm{C}_{1}, \mathrm{C}_{2}, \ldots, \mathrm{C}_{\mathrm{n}}\right)$;
- $\mathrm{P}(\hat{\mathrm{E}})$ is the prior failure probability of a barrier element or system.

- $\mathrm{P}(\mathrm{Ci})$ is a probability distribution that represents the different possible observable conditions (states) of a risk influencing factor ( Cn ) in accordance with the proposed scoring system and axiom; and
- $\mathrm{P}(\mathrm{Ci} \mid \hat{\mathrm{E}})$ is the probability of a specific RIF given Failure (TRUE) or functionality (FALSE) of the barrier element, which can be expressed by the conditional probability table (CPT) which complies with the APPM axiom.

This slight adjustment to the mathematical framework is necessary for applying the main axiom of the method, the main objectives of which are to simplify the risk-update mechanism and to minimize subjectivity. The APPM axiom relies on the following assumptions:

- Most oil companies prioritize their investments and management efforts seeking to comply with industry standards. Also, compliance of RIF in contrast with well-known industry standards is easy to measure using traditional elements available in every Oil Company's Safety Management System (SMS). The metric, being simpler, facilitates implementation and reduces the subjectivity inherent to Bayesian Network methods, that in most cases relies on the implementation of probability elicitation procedures; and
- Catastrophic engineering system failures still occur. This leads to the conclusion that the average failure probability of an operating engineering system incorporates the socio-technical management practices that are designed and implemented to comply with regulations. In other words, accidents and failure data banks reflect the failure probabilities of socio-technical systems that, on average, have their performance managed to comply with industry standards. However, failure probabilities need to be industry specific whenever possible. This is because, as discussed by R., (Pitblado et al., 2011; Spouge, 2005), generic leak frequencies can change significantly in accordance with the industry, including onshore and offshore facilities. Therefore, offshore leak frequencies provide more reliable data as they reflect the application of specific industry requirements.

Based on these two assumptions, a main axiom for the method was established, which is:
If a RIF (including HOF) complies with industry standards, the failure probability of the barrier element affected by the RIF is expected to be approximately equal to the failure probability available from historical data banks. Or, in mathematical terms:

$$
\mathrm{P}(\text { Êi } \mid \text { RIF }=\text { IS }) \sim \mathrm{P}(\text { Êi })
$$

where, Êi is defined as the failure of a random event Ei and IS stands for "compliance to Industry Standards".

Consequently, one can derive the following hypothesis from the proposed axiom:

- When the scores of the RIFs inherent to a safety barrier lean towards best industry standards, the performance of the safety barrier function affected by these RIFs will lean towards high reliability performance;
- When the scores of the RIFs inherent to a safety barrier lean towards complete non-compliance to the standard, the performance of the safety barrier function affected by these RIFs will lean towards low reliability performance;

To implement the aforementioned axiom and hypothesis, the RIFs were quantified by combining a fourscale scoring system (Table 2) and a conditional probability table (CPT), presented in Table 3. This CPT was engineered with the single purpose of making the system comply with the proposed axiom and sustaining its subsequent hypothesis.

Table 2: Description of RIF scoring classification.


Table 3: CPT engineered for modeling the effect of a RIF in the performance of the safety barrier in accordance with the axiom of the method.


The CPT was tested using a basic DAG cause-and-effect model. The test consisted of confirming that the effect will change in accordance with the axiom and subsequent hypothesis. A prior failure probability of $5 \%$ was represented as the effect $\mathrm{P}(\hat{\mathrm{E}})$. Figure 3 presents the results obtained from this analysis and demonstrates the compliance of this basic model with the axiom of the method. Figure 4 presents the same results in a two-dimensional graph.

![img-2.jpeg](img-2.jpeg)

Figure 3: Basic net for a barrier element with a failure probability of $5 \%$, influenced by a RIF with four states.

![img-3.jpeg](img-3.jpeg)

Figure 4: Updated failure probability of barrier element, given RIF variation.
Figure 4 presents the four possible updated failure probabilities given the variation of the scoring system applied to one specific RIF that affect the performance of a barrier element. The graph shows that the axiom and the derived hypothesis meet and can be mathematically described as a linear trend with a determination coefficient of $\mathrm{R}^{2}=97,6 \%$ :

- Main Axiom: $\mathrm{P}\left(\hat{\mathrm{E}} \mid \mathrm{C}_{2}\right)=\mathrm{P}(\hat{\mathrm{E}})$; and
- Derived Hypothesis: $\mathrm{P}\left(\hat{\mathrm{E}} \mid \mathrm{C}_{1}\right)<\mathrm{P}\left(\hat{\mathrm{E}} \mid \mathrm{C}_{2}\right)<\mathrm{P}\left(\hat{\mathrm{E}} \mid \mathrm{C}_{3}\right)<\mathrm{P}\left(\hat{\mathrm{E}} \mid \mathrm{C}_{4}\right)$;

This update procedure, once implemented in all elements of a barrier system, will reflect the conditions of the system at a specific operational moment, functioning with the compliance of a group of RIF that affect performance. This is demonstrated in Section 4 through the application of the same test on a microscale theoretical blowout probability model.

# 3.3 Design and Implementation of Risk-Based Plan 

Khan et al. (2016) highlight that a Dynamic Risk Analysis (DRA) can actually improve the risk management process. They suggest a dynamic risk management framework to ensure the continuous improvement of the risk-management process, based on real-time process performance that is revised using process and failure history. The application of a dynamic risk management framework enhances the risk informed decision-making process by constantly monitoring, evaluating and improving process performance.

The use of safety or risk indicators may allow risk assessment to assume both dynamic and proactive features. Appropriate sets of indicators collected and evaluated on a regular basis can provide information on overall risk level variation. Indicators on technical equipment can often be automatically retrieved from online systems, such as maintenance management systems and condition monitoring systems. Indicators for human and organizational factors are generally more difficult to obtain, and rely on manual input and assessment (Paltrinieri et al., 2016).

This sub-section suggests a specific framework for updating DRA, considering the specificities of both this method and a drilling project's life cycle. Figure 5 summarizes this framework.
![img-4.jpeg](img-4.jpeg)

Figure 5: Risk-based plan framework.

The life cycle of the drilling project starts with the approval of the well design for a specific site. At this stage, risks related to the complexity of the well design and geological \& geophysical (G\&G) conditions are known. Consequently, the risk customized for the general characteristics of the drilling project can be estimated in accordance with the modeling guidelines of Level 1 of the proposed method.

After rig selection, the characteristics of the rig's drilling systems and Safety Management System (SMS) are known, allowing the QRA to be customized by implementing the Level 2 and Level 3 guidelines. At this stage, the blowout safety critical systems and RIF are correlated with: applicable key performance indicators (KPI), audit and inspection programs encompassing both hardware (equipment/ systems), and software (HOF) elements. The assumption that the Company's SMS is sufficient to monitor and manage critical processes against industry standards, the blowout QRA can be customized. This is done by reviewing the adequacy of the critical processes and updating the QRA by adjusting it to reflect specific system configurations and the scores of the RIF in accordance with the proposed axiom.
This integration allows for specific conditions of RIF to be accounted for, without the necessity of timeconsuming effort, such as performing sections of probability elicitation involving different types of experts.
Also, by the time the rig is selected, a risk-based plan reflecting the Plan, Do, Check and Adjust (PDCA) philosophy must have been designed. Since the safety critical systems and RIF will have been identified, the following additional guidelines must be defined to allow the implementation of the plan during the operational phase:

- PLAN the frequency and strategy for performing periodic reviews aligned with the method's axiom and scoring system. The following processes shall be considered: drilling reports/ operational parameters, SMS and Maintenance KPI, Management of Change (MoC) records, test/ inspections results and audit programs related to the Company's SMS and Maintenance Plan;
- DO / Implement and record the results of periodic reviews and update the model with new evidence based on direct observations and reviews;
- CHECK and communicate the updated risk to strategic and operational decision makers;
- ADJUST the process based on the updated risk picture and implement corrective actions whenever applicable;


# 3.4 Expected Advantages and Limitations of the Method 

Table 4 summarizes the most relevant characteristics of the model for different aspects that can be applied to assess dynamic risk analysis (DRA).

Table 4: Advantages/ Disadvantages of the Accident Precursor BN Method for Modeling Blowout Risks


# 4. MICRO-SCALE APPLICATION OF THE METHOD 

This section demonstrates the application of the method and tests it against the pre-defined axiom in a micro-scale blowout risk model. The model adopted in this example reflects the following: blowout while drilling into the reservoir (Level 1), Kick detection barrier system (Level 2) and the main risk influencing factors that affect the performance of the human element, responsible for detecting and reacting in the event of a kick (Level 3).

### 4.1 Level 1: Modelling and quantification of a blowout scenario

The suggested Level 1 blowout (step (i)) was developed using the bow-tie technique in Figure 6. This model represents the risk of a blowout when drilling into the reservoir.
The top event of the bow-tie (in $100 \%$ of cases) is the kick (the blowout accident precursor), i.e. the influx of hydrocarbon to the wellbore from the reservoir. It depends upon two geological and geophysical (G\&G) conditions, porosity and permeability. The loss of the primary barrier occurs when the hydrostatic pressure $\left(\mathrm{p}_{\mathrm{h}}\right)$ from the mud inside the well is lower than the formation pressure $\left(\mathrm{p}_{\mathrm{f}}\right)$. The event tree (ET) represents the escalation from the kick to the blowout and describes the secondary barrier system (well control system).
![img-5.jpeg](img-5.jpeg)

Figure 6: General blowout bow-tie model.
Table 5 presents the failure probabilities of the basic events available at Ref (Khan et al., 2016) that were calculated based on the failure rates (per $10^{6}$ hours) available in the (Offshore Reliability Data Handbook, 2002) data bank.

Table 5: Historical data used in the micro-scale analysis for Level 1(Bercha, 1978; Khan et al., 2016; Offshore Reliability Data Handbook, 2002).


(*) The basic "kick detection" event is calculated separately by modeling the barrier systems' into barrier elements with a specific configuration aiming to demonstrate the application of the method (Section 5.2 - Level 2 Demonstration).
(**) Calculation procedure based on data bank review, presented as follows.

The BOP failure probability can be calculated based upon BOP reliability data. In 2008, several industry groups created a task force to define the work scope for a joint industry project to study the BOP reliability of wells drilled in the US Gulf of Mexico from 2004 to 2006. The high-level result of the study indicated that even though improvements were noted over time, subsea systems actually had better failure rates than surface systems (Sattler \& Gallander, 2010). In accordance with the same study, the MTTF of a Class VIII BOP (the most complex deepwater system) is 121 days.
Therefore, the BOP failure probability equals $\mathrm{P}(\mathrm{BOP}$ Fails $)=1-\mathrm{R}(\mathrm{t})=8.23 \times 10^{-3}$ assuming that failure rates are exponentially distributed with failure rate $\lambda$, which is constant and independent of time.
The solution of the micro-scale blowout bow-tie model is obtained by separately calculating the probability of kick formation, its escalation to the blowout, and solving the event tree. The kick formation (hydrocarbon influx from the reservoir into the wellbore) will occur when adequate geological and geophysical (G\&G) conditions are available (hydrocarbon under pressure, porosity and permeability) and the hydrostatic pressure $\left(\mathrm{P}_{\mathrm{h}}\right)$ of the mud column is lower than the formation pressure $\left(\mathrm{P}_{\mathrm{f}}\right)$ (see Equation 4).

$$
\begin{gathered}
(\text { Kick Formation })=\mathrm{E}_{10} \cap\left(p_{h}-p_{f}<0\right) \\
\mathrm{P}(\text { Kick Formation })=5.02 \times 10^{-3}
\end{gathered}
$$

# 4.2 Level 2: Modeling and quantification of failure rate of barriers' systems 

The main goal of Level 2 is to model the specifics of the barrier systems and calculate the failure probability of blowout barrier systems. Figure 7 presents an example of the performance assessment of the kick

detection's safety barrier system using a fault tree (FT). The safety function of this critical safety barrier is to detect the well flow before it reaches the blowout preventer (BOP). To perform the planned safety function, at least one operator must recognize specific changes in operational parameters monitored by proper instrumentation systems, interpret this information and properly respond to control the kick by shutting in the BOP.

This theoretical example assumed that the driller is responsible for monitoring two independent hardware systems: pit instrumentation and drilling instrumentation. This specific aspect of the operational condition generates a redundant failure element in the model $\left(\mathrm{E}_{2}\right)$ in the fault tree presented in Figure 7. The failure probability of the basic events of the model are available in Table 6.

![img-6.jpeg](img-6.jpeg)

Figure 7: Fault tree for failure of the kick detection system.

Table 6: Historical data used in the micro-scale analysis for Level 2 (Bercha, 1978; Khan et al., 2016; Offshore Reliability Data Handbook, 2002).


The fault tree (FT) for failure probability of the Kick Detection Barrier System, presented in Figure 7, was mapped into a Bayesian Network (BN). The purpose of mapping the fault tree into a Bayesian network is to adjust for the incorporation of RIF affecting the performance of selected barriers of the system that will be addressed in Level 3. The nodes of the BN are composed of basic events and sub-systems, connected by arcs that define their cause-and-effect relationship.

Boolean nodes are suitable for modeling the Level 2 barrier systems in a BN as, on a micro scale, it can be assumed that the barrier systems are composed of independent variables with two operational conditions (Operational state $=$ Yes) and (Not-Operational state $=$ No).

Table 7 presents the Boolean CPT correlating the three barrier systems that, if all of them failed, would cause the kick detection function to fail.

Table 7: CPT for kick detection Bayesian Network.


However, the specific configuration of this system presents a redundant failure element $\left(\mathrm{E}_{2}\right)$. This specific condition of the system leads to the adoption of the BN method to facilitate modeling and calculation of the failure probability that reflects the redundant failure element. Figure 8 in the sequence presents a BN for kick detection failure, modeled and calculated by GENIE Software 2.0 (GENIE SOFTWARE 2.0 COPYRIGHT 1998-2015, 2015).

![img-7.jpeg](img-7.jpeg)

Figure 8: BN for failure of kick detection safety barrier system.
The failure probability of the kick detection system $\mathrm{P}(\hat{\mathrm{E}})=0.05$, in Figure 8 above, represented by the TRUE state of the central node which shows an approximated value of $1 \%$. The FALSE state stands for the probability that the system operates effectively, $\mathrm{P}(\mathrm{E})=0.995$.

# 4.3 Level 3: Modeling and quantification of RIF 

After modelling the barrier system into a BN (Level 2), it is necessary to identify the risk-influencing factors (RIF), including human and organizational factors (HOF) that affect the performance of the barriers. This process is what allows the model to be customized for the current operational reality of each rig, by incorporating human and organizational factor specifics into the model.
Table 8 presented below provides examples of RIF that are applicable to the barrier element assessed in this example, which is the drilling operator's performance.

Table 8: Examples of risk-influencing factors that can affect the performance of the human operator part of a kick detection system.


It should be noted that failure of the human operators (driller and geologist) was chosen to demonstrate the mapping for Level 3, as human failure is a critical failure mode for kick detection. Based on the work of Reason (Reason, 1990), human failures can be divided into three main categories: human error, violations and sabotage. 'Human errors' may be defined as "occasions in which a planned sequence of mental or physical activities fails to achieve its intended outcome, and when these failures cannot be attributed to the intervention of some change agency" (Reason, 1990). 'Violations' have been defined as "deliberate - but not necessarily reprehensible - deviation from those practices deemed necessary (by designers, managers and regulatory agencies) to maintain the safe operation of a potentially hazardous system". 'Sabotage' may be defined as deliberate actions with a prior intention to damage the system (Reason, 1990).
A Bayesian network (BN) micro scale blowout risk model was designed for testing the axiom. The Level 1 bow-tie (BT) and the Level 2 fault tree (FT) were integrated and mapped into a BN. Then, the set of nodes representing the human and organizational factors (HOF) presented in Table 8 were connected to the applicable barrier elements (human element), in accordance with the mathematical framework represented by Equation 2. Figure 9 presents the micro-scale blowout BN risk model.

![img-8.jpeg](img-8.jpeg)

Figure 9: Microscale theoretical blowout BN risk model.

The theoretical micro-scale blowout BN risk model (Figure 9) was tested by the following procedures:

- randomly changing the states of risk influencing factors (RIF) that affect the reliability of the human operators responsible for detecting the kick;
- updating the states of all RIF and barrier elements of the model in accordance with the major findings of the Macondo Blowout reviewed from (Deepwater Horizon Study Group, 2010; Hopkins, 2012) and
- performing a sensitivity analysis.

The major nodes of the test procedure, in their original state, are highlighted in Figure 9 to facilitate visualization and listed as follows:

- the blowout, which is the major failure being analyzed $: \Leftrightarrow \mathrm{P}(\overline{\mathrm{E}})=6.62 \times 10^{-5}$ (TRUE);
- the blowout accident precursor, which has a kick formation probability of $: \Leftrightarrow \mathrm{P}(\overline{\mathrm{E}})=5.00 \times 10^{-3}$ (TRUE);
- the critical systems related to primary and secondary blowout barriers:
- Failure of kick detection system $: \Leftrightarrow \mathrm{P}(\overline{\mathrm{E}})=5.02 \times 10^{-3}$ (TRUE); and
- BOP system failure $: \Leftrightarrow \mathrm{P}(\overline{\mathrm{E}})=8.23 \times 10^{-3}$ (TRUE);
- the nodes from Level 1 and 2, updated in accordance with the major findings of the Macondo Blowout:
- Level1_E10 stands for proper G\&G conditions for kick $: \Leftrightarrow \mathrm{P}(\overline{\mathrm{E}})=1.25 \times 10^{-1}$ (TRUE);
- Failure of the Pit System $: \Leftrightarrow \mathrm{P}(\overline{\mathrm{E}})=1.00 \times 10^{-1}$ (TRUE);,
- The risk influencing factors (RIF) presented in Table 8 were modeled in accordance with Equation 2 and the CPT, which was designed to meet the axiom of the method (See Table 3). The discrete probability distribution $\mathrm{P}\left(\mathrm{C}_{\mathrm{i}}\right)$ which is generated by this process is shown on the nodes of Level 3 (RIF) in Figure 9.
Figure 10 presents the posterior failure probabilities of the kick detection system given the variation of the scoring system applied to the RIF presented in the micro-scale example in Figure 9. The same figure presents two non-linear trend lines derived from this procedure, one describing the failure probability of the kick detection system and the other of the major failure (blowout), as the variation of the former directly affects the latter. The derived non-linear curves, represented by the equations also presented in Figure 10, have determination coefficients of $\mathrm{R}^{2}=97,8 \%$ and $\mathrm{R}^{2}=98,6 \%$ respectively.
The non-linear behavior of the failure probability of the kick detection system and, consequently, of the blowout probability, is explained by the common risk influencing factors affecting the performance of the barrier elements. This system's arrangement creates a dependence that significantly influences its reliability, partly by changing the order of the failure probability equations, as demonstrated by (Xiaowei, 2010).

![img-9.jpeg](img-9.jpeg)

Figure 10: Kick Detection Failure and Blowout Probability Update Given the Variation of Scores of RIF for Human Operators.
The model behaved in accordance with the axiom and its subsequent hypothesis. When "industry standard" was set as the evidence for all RIF, the failure probability of kick detection and blowout probability were both equal to the prior probability from failure rate data banks:

- $\mathbf{P}(\hat{E}=$ Failure of Kick Detection $\left|\mathbf{C}_{\mathbf{i}}=\mathbf{I S}\right\rangle=\mathbf{P}(\hat{E})=\mathbf{5 . 0 0} \mathbf{x 1 0}^{-\mathbf{3}}$; and
- $\mathbf{P}\left(\hat{\mathbf{E}}=\right.$ Blowout $\left|\mathbf{C}_{\mathbf{i}}=\mathbf{I S}\right\rangle=\mathbf{P}(\hat{\mathbf{E}})=\mathbf{6 . 6 2} \mathbf{x 1 0}^{-\mathbf{5}}$

The derived hypothesis is also confirmed, as the variations applied to the scoring of RIF changed the failure probability of the safety barrier system from a low reliability standard $\left(\sim 10^{-1}\right)$ to a high reliability standard $\left(\sim 10^{-6}\right)$. As a result, the major failure of the system (blowout probability) was automatically updated.
It was also noted that the CPT is more sensitive when best industry practices (BP) are set, since this prevalence more rapidly leads the system to a high reliability state when compared to the states where the RIF are classified as below industry standards. However, this configuration of having all RIF above what is expected by industry standards can be considered infrequent, since industry standards are becoming stricter and, for this reason, most companies consider their goals against these standards.

The same model was updated with evidence from the Macondo blowout for testing its capability for performing probability updates and sequential learning. For the sake of simplicity, the risk update for the Macondo blowout considered the following sequence of selected general evidence gathered from available bibliography (Deepwater Horizon Study Group, 2010; Hopkins, 2012):

- The rig crew knew that there were proper G\&G conditions for a blowout, as the well was being completed for production;
- The rig crew bypassed the pit system (one of the redundancies of the kick detection system) to send mud from the well to the supply vessel;

- It was inferred that organizational factors affecting blowout risk were not adequate at that moment, as well as human and organizational factors, as demonstrated in (Hopkins, 2012).

This simplified evidence from the Macondo Blowout was cumulatively added to the Bayesian network, from $\mathrm{C}_{1}$ to $\mathrm{C}_{4}$. Consequently, the blowout risk was updated, as presented in the bar chart at Figure 11. Table 9 in the sequence presents the exact values of posterior probability obtained from this test, for blowout posterior probability and also for the failure of the kick detection system.
![img-10.jpeg](img-10.jpeg)

Figure 11: Updated blowout probability, given general evidence collected from the Macondo blowout.

Table 9: Updated kick detection failure and blowout probability, given general evidence collected from the Macondo blowout.


The model also behaved as expected, as the evidence that was updated lead the kick detection system (which failed in the Macondo event) into a low reliability state, which lead the blowout probability to increase drastically.

The last test of the micro-scale model consisted of performing a sensitivity analysis for the probability of a blowout occurring (Figure 12) and for the failure probability of the kick detection system (Figure 13).

![img-11.jpeg](img-11.jpeg)

Figure 12: Sensitivity analysis for the probability of a blowout occurring.
![img-12.jpeg](img-12.jpeg)

Figure 13: Sensitivity analysis for the failure probability of the kick detection system.
It is important to stress that a basic condition applicable to risk modeling was not fulfilled, which is "The precision and sensitivity of the model depends on all relevant RIF and conditional dependencies between variables of the model being identified and their relationship with risk being known and mapped". However, this limitation is inherent to the nature of a microscale example, not representing the entire system, and therefore not directly affecting the sensitivity of the model.

The micro-scale model only encompasses a very specific part of the entire blowout risk system, as the guidelines for modeling Level 2 objectives were exclusively applied to the kick detection system, and the objectives defined for Level 3 considered exclusively the HOF affecting the human elements. This effect can be perceived by the significance of human operators, represented by the codes Level 2_E3 and Level_2_E4 in both graphs, in the behavior of the model, mostly when assessing its impact on the failure of the kick detection system alone.

The other variables that significantly contribute to the sensitivity of the model, i.e. for the blowout risk, are: the BOP, the root causes of lower mud weight, and the availability of adequate G\&G conditions for a blowout. Therefore, in accordance with the analysis, loss of mud volume appears to be a less relevant contributing factor to a blowout while drilling, when compared with lower mud weight. This result is inline with the findings of a review of major blowout causes applied to workover (which is similar to drilling into the reservoir modeled in this paper) performed by Holand (1997) who presents an overview of the causes of the blowouts from the SINTEF database.

# 5. DISCUSSION OF APPM LIMITATIONS AND FUTURE WORK 

The following remarks discuss the major APPM characteristics with a focus on the limitations that were identified by this research paper, and support the suggestions for future work presented afterwards.

- The method still has structural disadvantages and limitations when compared to other modern DRA methods, mostly those that were designed for application in process industries. However, some of these characteristics are exactly what makes the proposed method superior for oil drilling, and also:
- The method is not free of subjectivity. However, its subjectivity is anchored to one Conditional Probability Table (CPT), which is testable and transparent in relation to its objectives, since it is directly correlated with a clear and easily observable axiom. This move from a traditional elucidation process to a axiomatic approach makes the method more transparent, less subjective and less time-consuming to apply in real-life projects;
- Risk updates are dependent on the implementation of a risk-based plan (risk updates are not automated). This characteristic can be considered a mathematical disadvantage, but this same disadvantage makes it possible to cover all the elements and RIF applicable to a drilling blowout, which are highly dependent on G\&G factors and HOF (both quite uncertain, but measurable using observation techniques). This is also precisely what enables the continuous improvement of the Safety Management System (SMS), improve situational awareness of operational managers and, consequently, the safety culture related to this singular major accident hazard. These combination leads to improved decisionmaking processes which are, as demonstrated by Kongsvik et al. (2015), a central component of the management of safety-critical operations;
- The test process was not sufficient to assess the model's precision and sensitivity due to limitations inherent to the micro-scale model, as discussed in the last section.

From the discussion, the following future work is suggested:

- To develop a comprehensive blowout risk model in accordance with the APPM. The model must integrate all relevant blowout safety barrier systems and RIF, mapping potential conditional dependencies between the system's variables. The comprehensive Bayesian Network blowout risk model can be derived from existing models, such as the ones developed by (Abimbola et al., 2014; Khakzad et al., 2013). It is expected that a comprehensive model will be more precise, since its sensitivity requires all relevant RIF and conditional dependencies between variables to be identified, and their relationship with risk to be known and mapped in the BN. This was not accomplished in this current research;
- To detail the three-level modeling guidelines and the framework for implementing a risk-based plan aligned with the APPM specifications. Both improvements will facilitate the design and implementation of a testing process similar to the one presented by this research paper, but on a more realistic scale. This standardization will facilitate other researchers and scientists to apply and test the method, and consequently strengthen its scientific basis.

# 6. CONCLUSION 

The APPM for modeling and assessing the risk of deep drilling blowouts was designed to overcome the limitations of currently employed QRA methods in the oil and gas industry. The technique has the capabilities of: incorporating RIF into QRA, addressing dependability between variables, and allowing risk updates using new evidence, considering the specificities inherent to a drilling operation.
The advantages and disadvantages of the technique, when compared to other similar methods discussed in this research work were identified. Most of its characteristics, discussed in the last section, have both positive and negative aspects. From this comparison, it was concluded that the APPM is appropriate for application to modeling and assessing the risk of blowouts in offshore hydrocarbon drilling projects.
It shall be highlighted that the axiom of the method, supported by a Bayesian approach, allows the incorporation of RIF and risk-updates without the necessity of performing probability elucidation sessions. Also, its metrics based on regulatory compliance are transparent, readily available and measurable and, for this reason, minimize subjectivity. Its integration with a 'life' safety management system SMS using a riskbased plan should improve risk-based decisions and, consequently, enhance operational decision making.
The implementation of the method was tested by a theoretical micro-scale blowout risk model, which focused on the performance assessment of the 'kick detection' barrier function and on the 'human operator detecting kick' barrier element. The test was considered satisfactory, as it was sufficient to validate the behavior of the method and identify opportunities for future work in this scientific field.

## 7. ACKNOWLEDGMENTS

We appreciate and acknowledge the research's financial support provided by Witt O'Brien's Brazil. Adriano Ranieri and Flavio Andrade for their professional support and reference. Oliver Peters for English proof reading and revision, Rafael Perez for proof reading the article as many times as requested, and for both anonymous peer reviewers for all their valuable comments.
