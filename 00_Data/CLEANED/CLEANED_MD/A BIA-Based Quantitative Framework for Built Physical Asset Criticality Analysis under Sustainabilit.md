# Article 

## A BIA-Based Quantitative Framework for Built Physical Asset Criticality Analysis under Sustainability and Resilience

Mohsen Aghabegloo ${ }^{1}$ (D), Kamran Rezaie ${ }^{1}$, S. Ali Torabi ${ }^{1}$ and Seyed Mohammad Khalili ${ }^{2, *}$ (D)<br>check for updates

Citation: Aghabegloo, M.; Rezaie, K.; Torabi, S.A.; Khalili, S.M. A BIA-Based Quantitative Framework for Built Physical Asset Criticality Analysis under Sustainability and Resilience. Buildings 2023, 13, 264. https://doi.org/10.3390/ buildings13010264

Academic Editor: Lei Hou
Received: 21 December 2022
Revised: 11 January 2023
Accepted: 13 January 2023
Published: 16 January 2023

## (0)

Copyright: (c) 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 School of Industrial Engineering, College of Engineering, University of Tehran, Tehran 1439957131, Iran
2 Department of Industrial Engineering, Faculty of Engineering, Khayyam University, Mashhad 9189747178, Iran

* Correspondence: m.khalili@khayyam.ac.ir

Abstract: Asset-intensive industries, such as the construction industry, have experienced major catastrophes that have led to significant operational disruptions. Physical asset failure has been the primary cause of these disruptions. Therefore, implementing proper asset management plans, including continuity plans, is crucial for the business continuity of companies active in these industries. However, companies often face severe resource limitations when implementing these plans for all of their physical assets. Therefore, those critical physical assets that are vital for providing their key products should be identified. Moreover, sustainability and resilience are inseparable parts of organizations' strategies, including strategic asset management plans. Therefore, any proposed ranking methodology for physical asset prioritization should encompass sustainability and resilience measures to ensure its practicality. This paper proposes a novel framework for physical asset criticality analysis based on the so-called business impact analysis to ensure the continuity of providing products/services through the continuity of physical assets. A hybrid fuzzy BWM-TOPSIS method is first applied to identify the key products. Then, a hybrid fuzzy DEMATEL-Bayesian network is applied based on proper sustainability and resilience factors to determine the critical physical assets, while interdependencies among these factors are well captured. The normalized expected asset criticality index is defined to guide managers in taking appropriate directions while developing asset management plans. A case study of a gas company is provided to show the applicability of the proposed decision model. The data needed for each step of the framework is gathered through experts' judgments, historical data available on the sites, or quantitative risk assessment scenarios.

Keywords: buildings; physical asset management; criticality analysis; critical infrastructure; sustainability; business continuity management; business impact analysis; Bayesian network; multi-attribute decision making; operation research

## 1. Introduction

Asset-intensive industries, such as the construction industry, have been subjected to accidents resulting in significant catastrophes that have negatively affected their goals [1,2]. These accidents may threaten the companies' continuity due to the disruption of their physical assets, a key resource for their operations. Failure in physical assets may lead to serious safety and environmental consequences as well as financial loss [3]. Thus, ensuring the continuity of physical assets can enhance the competitive advantage of asset-intensive companies. For this reason, implementing well-established continuity and contingency plans can strengthen companies' resilience against disruptions [4].

Organizations typically face limited resources for implementing contingency plans for all of their physical assets. Thus, prioritizing the physical assets for determining critical ones is inevitable. Physical assets can be critical in terms of safety, environment, quality, production, operation, or maintenance [5]. Therefore, sustainability, which covers environmental, social, and economic issues and helps organizations meet their demands without

negative effects on future generations' needs, should be highlighted while physical assets are prioritized. According to ISO 55000, critical physical assets have a significant impact on organizational goals and are vital for service providers to serve essential customers [6]. Accordingly, identifying the impacts of disruptions on the physical assets' operations and the provision of key products/services is crucial in identifying the critical physical assets.

Business impact analysis (BIA) is an efficient tool to determine critical business processes and the impacts of disruptions on them and companies' goals [7]. BIA provides a list of key products and critical functions [8]. In asset-intensive organizations, such as construction companies, the continuity of key services depends on their critical physical assets [9,10,11]. Therefore, the identification of critical functions via the BIA process can be replaced by identifying critical physical assets. In this way, conducting a BIA can assist organizations in identifying their critical physical assets and prioritizing their business continuity plans (BCPs) to ensure the continuity of their critical functions. Moreover, the resilience of physical assets that contribute to key products/services is of great importance since they are prone to a wide range of disruptive events that can hinder the provision of key products/services. Resilience is the ability of a system to withstand a major disruption and recover to normal operations considering time, cost, and risks [9]. Accordingly, resilience factors should be considered when the criticality of the physical asset is studied. Furthermore, resilience and sustainability are interdependent and sometimes contradictory concepts [12,13]. To comprehend this inter-relationship, a sound strategy is necessary to capture such relations and make the tradeoff between these two concepts.

Considering the above-discussed points, the main research questions are as follows:

- How to consider business continuity aspects when determining asset criticality?
- How can asset criticality analysis reflect tradeoffs between resilience and sustainability metrics?

Accordingly, a quantitative and structured BIA-based framework is proposed in this paper for physical asset criticality analysis to assist asset-intensive companies in efficiently allocating their limited resources to physical assets' continuity plans. The framework is based upon the BIA process, in which several sustainability and resilience factors that are suitable for the physical asset criticality analysis are assessed through a mixed multiattribute decision-making (MADM) approach. For this, the DEMATEL method is first applied to determine the interdependencies among sustainability and resilience factors. Then, a Bayesian Network (BN) is constructed to determine the criticality degree of each asset. Finally, the asset criticality index is calculated using the weighted sum operator, for which the weights of factors are estimated through the fuzzy best-worst method (FBWM).

The rest of this paper is organized as follows: Section two reviews the related literature. Section three elaborates on our proposed framework for physical asset criticality analysis in detail. In the fourth section, our framework is implemented on an actual case study of a gas plant, including its infrastructure and buildings. Section five provides several managerial insights derived from the case study. Finally, the concluding remarks and directions for further research are presented in Section six.

# 2. Literature Review 

The continuity of asset-intensive organizations largely depends on the continuity of their physical assets [10,11]. Therefore, deploying appropriate plans for physical assets and incorporating continuity and contingency plans are inevitable in these industries. The literature review shows that there is just one research study in the area of physical asset risk management. Ref. [14] presented is a quantitative framework for physical asset risk management by which an optimum portfolio of risk mitigation plans and business continuity plans are used for critical physical assets based on the associated risk network structure that is derived from the physical asset life cycle. However, they did not specify how critical physical assets would be determined. As a complementary piece to that paper, this paper provides a quantitative framework for identifying those critical physical assets for which business continuity and risk mitigation plans should be implemented. For this,

the hierarchy of physical assets should be determined based on the degree of impact on business continuity. Such prioritization should consider sustainability and resilience factors to increase the quality of the workplace regarding environmental, social, and economic considerations while improving responses to extreme events [15]. The foundation of the proposed framework involves two different streams, including "physical asset criticality analysis" and "business impact analysis", whose essential contributions are summarized below. In addition, this section discusses the sustainability and resilience assessment as well as the application of the Bayesian network in it.

# 2.1. Physical Asset Criticality Analysis 

Physical asset prioritization is mainly addressed in the literature as criticality analysis. Considering the lifecycle of physical assets, one can carry out criticality analysis in two different phases, namely the design phase and the operations and maintenance phase. Failure modes are identified and prioritized in the design phase to identify the critical areas that may negatively affect the asset availability target [16]. However, in the operations and maintenance phase, which is addressed in this paper, the criticality analysis aims to prioritize the physical assets in order to properly allocate the limited available resources for business continuity plans (BCPs). There are various qualitative and quantitative asset prioritization methods in the literature [17]. In most cases, quantitative methods involve risk assessment techniques to evaluate physical assets' failure modes while considering some influential factors. Ref. [18] presented a risk assessment method in which the likelihood of failure is estimated based on the mean time between failures and lost event criteria. They categorized failure's impacts into production, safety, and maintenance cost impacts. They also applied the multi-attribute decision-making (MADM) method to rank physical assets. To analyze asset criticality, [19], classified failure occurrences into four categories: unacceptable, repetitive, acceptable, and possible. The severity of the functional loss is then predicted based on safety-related parameters, environmental care, service quality, availability, and maintenance cost. They utilized AHP to estimate the relative importance of each criterion and built a criticality matrix. Ref. [20] performed a failure mode, effect, and criticality analysis (FMECA) on an offshore and onshore platform and then used machine learning approaches to establish failure cause-and-effect relationships. In order to determine the criticality of assets in a gas refinery, ref. [21] suggested a fuzzy inference method. The proposed criticality method considers elements, such as production capacity and quality, employee safety, availability, and maintenance costs. Ref. [22] also applied fuzzy set theory to analyze asset criticality for the cyber-physical system. Ref. [23] determined the criticality score of sewer pipeline assets by considering the consequences of failures in the assets. They highlighted deterioration pace as a major influential factor for criticality analysis. Ref. [24] applied a graph theory approach to determine critical assets in natural gas and electricity infrastructure using a vulnerability index. Criticality analysis has been a matter of concern in the food industry as well. Ref. [25] considered quality, availability, safety, environment, cost, and technology complexity as essential factors for asset criticality analysis in the food industry.

Some scholars have addressed the continuity of service provision as the most influential factor for asset criticality analysis. Ref. [26] applied a function-based scoring system at the asset level that took into account the specific impact of each asset on the primary function of the entire system. The method also suggests health and safety measures as essential factors for asset criticality.

### 2.2. Business Impact Aanalysis

The BIA process is the primary step in implementing the business continuity management system (BCMS), since the BCM strategies are determined and implemented based on the BIA results [27]. Accordingly, various procedural steps or frameworks for conducting a suitable BIA have been proposed in the literature [8,28], presenting a four-step BIA that includes identifying key functions, determining business recovery and time recovery

requirements, exploring external and internal dependencies of critical functions, and determining the impact of disruption. Ref. [29] elaborated on different sources of data required for BIA and did data analysis for identifying critical processes and required resources of recovery strategies. They finally explained the structure of the BIA report. Ref. [30] reviewed different BIA implementation approaches, including fast-tracked and standard approaches, and presented the challenges and pitfalls of BIA projects.

Although different qualitative BIA frameworks are introduced in the literature, most of them follow quite similar methods [8]. In general, the BIA process can be summarized in four main steps: (1) identifying the required activities for products/service provision, (2) assuming the impacts of possible disruptions on these activities, (3) setting recovery requirements (i.e., business continuity measures), such as the available timeframe for resumption, and (4) resources dependency identification [6]. There are few quantitative BIA frameworks in the literature. Ref. [8]'s proposed framework includes three main steps. First, using a hybrid fuzzy DEMATEL-ANP method, the key products are identified. Then, the critical functions are determined through a functional breakdown structure mechanism along with a criticality analysis based on suitable criteria (factors and subfactors). Finally, continuity parameters are determined for critical functions in line with the organization's risk appetite.

# 2.3. Sustainability and Resilience Assessment 

Sustainability and resilience are inter-related and contradictory, necessitating tradeoffs during the decision-making process [13]. For example, a lean approach to developing processes that reduce consumption and minimize environmental impacts is used under the sustainability viewpoint, whereas redundancy and flexibility measures are employed under the resilience concept to boost the capacity to cope with risks and threats [12]. On a broader scope, the necessity of such integration has resulted in the new integrated managerial paradigm called LARG (including lean, agile, resilience, and green dimensions) in the supply chain management area [31]. Reference [32] presented a literature review of different frameworks considering sustainability and resilience simultaneously. They suggested that these frameworks either consider the hierarchal relation between resilience and sustainability or take them as separate concepts with complementing or competing objectives.

In the structure and infrastructure domain, resilience and sustainability have been widely studied jointly. Reference [33] considered quality of life, macroeconomics, human development, construction, and well-being factors to analyze sustainable construction industries in the UK and Norway. They applied complex proportional assessment and degree of project utility and investment value assessment (INVAR) to determine to what extent the country has fulfilled the sustainable construction requirements. Considering the sustainability assessment of projects in the structure and infrastructure domain. Reference [34] applied the SAW method to assess the sustainability of residential projects in Baltic states, considering different indicators for sustainability dimensions. Reference [35] applied hybrid multi-criteria decision attribute methods, including DEMATE, Delphi techniques, and ANP, to identify and rank barriers for green construction projects. Considering infrastructure projects, reference [36] proposed a sustainable decision support system to predict and optimize residual cyanide to increase the resilience of the water treatment plant in the design phase. For this, they applied mathematical computations to find the best regression model and implemented a genetic algorithm to optimize the model. Reference [37] compared resilience and sustainability in terms of definition, target, quantification, and primary calculation methods. They stated that sustainability is quantified based on different quantitative and qualitative indicators, while resilience is quantified based on the resilience index, which is a function of time and the area underneath the recovery path. The paper suggests a risk theory paradigm (combination of probabilities and consequences) to analyze the sustainability and resilience of infrastructures. Reference [13] applied the DEMATEL approach to determine interdependencies among sustainability and resilience

factors to structure a framework for the evaluation of buildings with regard to environmental impacts and persistence to environmental shocks and disturbances. Reference [38] conducted a literature review to gather various sustainability and resilience factors in the building energy domain. They also discerned indicators that are suitable for optimization problems. Reference [39] also discovered the sustainability and resilience of infrastructures.

Similar to the structure/infrastructure sector, scholars have widely recognized sustainable-resilient supply chains. For example, ref. [40] proposed a multi-objective mixed integer linear programming model for sustainable supply chain network design, considering energy consumption and the number of created job opportunities as objectives of such a design. They have studied three choices, including remanufacturing, recycling, and disposing of the returned items. Reference [41] presented a single optimization model to analyze the dynamic sustainability of a supply chain, which can help make a tradeoff between sustainability and resilience. Reference [42] studied tradeoffs between sustainability and resilience in a supply chain. The author considered different contradictory objectives at the strategic level and assessed stakeholders' choices regarding sustainability and resilience with the gray theory. Reference [43] proposed a mixed-integer linear programming problem to minimize food supply chain cost considering resilience and sustainability strategies. Reference [44] conducted a literature survey on different strategies for supply chain disruption, with a special focus on the COVID-19 pandemic. They revealed that developing methods to meet sustainability and resilience objectives simultaneously could be a sound but challenging strategy to cope with supply chain disruptions.

The literature review indicates that applying the Bayesian network to analyze sustainability and resilience factors jointly is scarce, while addressing either of the concepts through the Bayesian network has been widely studied in the literature. Reference [45] applied the Bayesian network model to evaluate resilience in urban transportation systems. They established their models based on three hierarchical layers: function, quality, and factor. Reference [46] proposed a resilience assessment process that included identifying threats, designing resilience capacity, quantifying and assessing resilience, analyzing results, and making recommendations for resilience improvement. They have introduced different contributing factors for each resilience capacity and implemented a Bayesian network to assess the resilience of a deep-water information system. Reference [47] quantified the resilience capacity within the context of supplier selection using the Bayesian network. They structured the model with variables, including Boolean, NoisyOR, continuous, and discrete variables. Refs. [48,49] have also studied the application of the Bayesian network for resilience quantification and assessment in infrastructure, power supply and control systems, transportation systems, and offshore power facilities, respectively.

Similar to resilience assessment, the Bayesian network has been applied to analyze sustainability in different sectors. Reference [50] introduced several measures for four sustainability dimensions, namely, social, environmental, economic, and institutional dimensions for a port system. Then, a Bayesian network was constructed to analyze the relationships between measures. Reference [51] proposed a methodology for the social sustainability of infrastructure projects in which a decision-making model consisting of variables and their relations is first developed. The Bayesian reasoning model then assesses alternatives based on social sustainability variables, and the optimal alternatives are determined for an infrastructure project. Another study [52] applied a Bayesian network to assess environmental and socioeconomic factors in catchment modeling. They analyzed different scenarios to determine cost-effective management actions to improve river water quality. Reference [53] studied the criteria and subcriteria of sustainable supply chains. They introduced an aggregate supply chain performance indicator whose probability is calculated based on the sustainability criteria using the Bayesian network.

# 2.4. Literature Gap and Our Contributions 

In order to have a structured gap analysis and to identify a number of future research paths in the area of physical asset criticality analysis, Table 1 provides a special focus on a number of relevant articles from the literature.

Table 1. A summary of the reviewed articles and their focus.


(1) complete focus (1): Partially Covered $\bigcirc$ : Not Covered.

According to the discussion above, physical asset criticality analysis in asset-intensive companies has been mainly addressed through risk assessment methods while considering safety, environmental, or financial impacts. However, the business impact of physical assets' disruption, particularly resilience factors, has not been systematically studied in the literature, despite the high dependency of these companies' operations on their physical assets. The primary tool for identifying the business impacts of disruptions is BIA, which is one of the main steps for implementing business continuity management systems. However, the lack of a structured but customized quantitative BIA for physical asset management is apparent in the literature. Moreover, criticality analysis has been mainly conducted through risk-based maintenance or risk-based inspection [54], applying failure modes and effect analysis tools [55], which cannot systematically capture the interdependencies among different criteria, while there are extensive relationships among sustainability and resilience factors.

Accordingly, the main contributions of this study are as follows:

- Proposing a new BIA-based physical asset criticality analysis framework that considers sustainability and resilience factors for asset-intensive companies will provide top managers with valuable information for deciding on their physical assets' contingency and continuity plans.
- The relationship between business continuity management and asset management is addressed.
- Proposing a probabilistic graphical model by combining fuzzy DEMATEL and the Bayesian network approaches to assess physical asset criticality.
- Introducing an aggregate asset criticality index by applying the best-worst method and considering environmental, social, economic, and resilience factors will help managers prioritize assets.
- Providing a case study in a gas plant to show the applicability of the proposed framework.


# 3. Proposed BIA-Based Mixed Sustainability-Resilience Framework for Physical Asset Criticality Analysis 

Ensuring the continuity of physical assets in asset-intensive organizations, such as gas companies, is crucial for their consistent and sustainable operations. For this reason, these companies usually implement various physical asset plans that include continuity and contingency plans. However, often there are not enough resources to make use of strict plans for all the physical assets. Accordingly, criticality analysis should be carried out to provide reliable information for asset managers to prioritize physical assets and efficiently allocate their limited available resources such that the sustainability and resilience of the company are ensured.

This paper focuses on the physical asset criticality analysis under a quantitative BIA framework, considering sustainability and resilience factors. The framework includes three main stages: (1) determining the key products, (2) identifying the critical physical assets, and (3) analysis of the results to find useful clues for the improvement of physical assets' conditions. To our knowledge, this is the first framework that integrates BIA with the physical asset management discipline to identify the critical physical assets, considering the continuity of key products' provision. Furthermore, the framework benefits from a mixture of MADM techniques to propose an asset criticality index considering sustainability and resilience factors and their relationships, which is a current gap in the literature. Figure 1 depicts the proposed framework for the physical assets' criticality analysis, whose stages are elaborated hereafter in this section.

![img-0.jpeg](img-0.jpeg)

Figure 1. Proposed framework for the BIA-based physical asset criticality analysis.

# 3.1. Determination of Key Products 

Due to the severe limitations in available resources in the post-disruption situation, organizations cannot recover all the disrupted processes and their related physical assets. Hence, it is vital to identify the key products and their associated physical assets to prioritize recovery activities at the post-disruption stage. In this manner, different products of the company should be prioritized according to suitable criteria. These criteria can be derived from those presented in [8] and modified by the experts in the company.

This study applies a hybrid multi-criteria decision analysis (MCDA) tool to prioritize an organization's products. Several MCDA techniques have been presented in the literature, most of which are time-consuming and require numerous pairwise comparisons [56]. To overcome this problem, the best-worst method (BWM) was developed by [57]. Moreover, BWM has shown more consistency compared to other pairwise comparison-based methods, such as AHP [57]. However, the original BWM has some shortcomings as it does not consider the uncertainty associated with human judgment about pairwise comparisons [58]. In this regard, a fuzzy BWM was applied to determine the importance of the identified criteria. For this reason, the fuzzy reference comparisons for the best (most important) and the worst (least important) criteria are made using appropriate linguistic terms. Then, the obtained fuzzy preferences are transformed into triangular fuzzy numbers (TFNs) for further analysis. Finally, the optimum fuzzy weights of the criteria are calculated through a linear programming model [59]. Fuzzy BWM has been applied in different contexts (see, for instance, [58,59]). We incorporate the calculated weights into a fuzzy TOPSIS methodology to rank the company's products. Such a combination of fuzzy BWM and fuzzy TOPSIS has already been used by [60]. Due to limited space, more details about the hybrid fuzzy BWM-TOPSIS methodology are provided in the online Supplementary Materials.

### 3.2. Identification of Critical Physical Assets

When the key products are determined, the critical physical assets required to produce the key products should be identified. In this regard, there are suitable tools in the literature. For instance, Reference [8] applied a relational work breakdown structure to identify various functions related to key products' provision. This tool can also be applied to identify all the physical assets related to provisions of key products. In the process industry, experts can refer to the associated block diagrams as well as piping and instrumentation diagrams ( P and IDs) to ensure that all the physical assets for delivering each key product are considered.

The company may not have enough resources to recover all the disrupted physical assets at the post-disruption stage. Therefore, physical assets should be prioritized to identify the critical ones. For this, different factors influencing physical asset criticality should be first determined, and then an appropriate method should be applied to prioritize physical assets regarding influential factors. In this study, a hybrid fuzzy DEMATELBayesian network is proposed to assess each physical asset. Physical assets are then prioritized based on their criticality index. For this, fuzzy DEMATEL is first applied to map the interdependencies among sustainability and resilience factors. The Bayesian network is then structured to assess the criticality of each physical asset regarding the factors. Finally, the best-worst method is applied to determine the weights of each factor, and then the asset criticality index is calculated. In the following, we elaborate on this step.

### 3.2.1. Sustainability and Resilience Factors

As mentioned earlier, sustainability and resilience are two critical concepts for physical asset criticality analysis. For this reason, it is crucial to determine the appropriate criteria for each concept.

- Sustainability:

The World Commission, [61], describes sustainability in environment and development as "development that meets current demands without compromising future genera-

tions' ability to meet their own needs". As a result, the triple-bottom-line (TBL) dimensions, which include environmental, social, and economic concerns, could be used to achieve sustainability [62]. Environmental and societal concerns are mainly addressed in industrial asset operations as health, safety, and environmental matters. In order to evaluate the level of assets' sustainability, relevant indicators should be discerned based on the literature review and customized according to expertise judgments. Relevant indicators derived from the literature are shown in Table 2. The list is not exhaustive, but it provides practical and widely used measures of physical asset sustainability.

Table 2. Sustainability indicators for physical asset criticality analysis.


# - Resilience: 

ISO 22300 (2021) defines resilience as the "ability to absorb and adapt in a changing environment". Reference [72] has also defined resilience as the "ability of a system to withstand a major disruption within acceptable degradation parameters and recover in a reasonable amount of time and reasonable costs and risks". Resilience capacity in the literature has been categorized into three types: absorptive capacity, adaptive capacity, and restoration capacity [73].

Absorptive capacity refers to the ability of the physical asset to absorb the disruptive event. In other words, absorptive capacity contributes to Physical Asset Functionality Loss (PAFL), the percentage loss to the normal service level of the physical asset immediately following a disruptive event.

Adaptive capacity represents the ability of physical assets to avoid discontinuity after a disruption. It specifies the period following a disruptive event during which the physical asset's service level is restored to a predefined physical asset recovery point (PARP), which is referred to as the physical asset recovery time (PART). Post-disaster plans should be developed to improve the adaptive capacity of physical assets.

Restorative capacity refers to the capability of a physical asset to be repaired or restored to its pre-degraded state. Restorative and absorptive capacities determine the total time required to recover the physical asset to normal operation (TTR).

Figure 2 represents the total loss of a physical asset (s) due to the occurrence of a particular disruptive event $\left(T L_{s P A P}\right)$. Considering normal operating levels (NOL), $T L_{s P A P}$ can be calculated as follows:

$$
T L_{s P A P}=(P A F L \times P A R T)+(1-P A R P)\left(\frac{T T R-P A R T}{2}\right)
$$

![img-1.jpeg](img-1.jpeg)

Figure 2. Graphical view of physical assets' resilience. PARP is the physical asset recovery point, and PART is the physical asset recovery time.

Therefore, physical asset resilience (PAR) over a suitably long-time interval $T^{\prime}$ can be calculated as follows:

$$
P A R=1-\frac{T L_{s P A P}}{T^{\prime}}
$$

Equations (1) and (2) have been inspired by [74], which proposed a function for predicted resilience.

To evaluate the level of resilience of assets, relevant indicators that affect three types of resilience capacity should be determined based on the experts' opinions. Then, the resilience level of the physical asset is calculated according to Equation (2). These resilience metrics can be expressed and quantified using various resilience indicators. It is crucial to employ indicators that reflect both operational and infrastructure resilience [75]. Existing safety and risk management, emergency preparedness, and business continuity practices can be used as the foundation for the development of resilience indicators. The majority of these initiatives can be found in the existing standards, guidelines, and reports [76]. Various scholars have studied the quantification of resilience capacities [77,78]. Reference [78] defined a resilience equation compromising failure and recovery as functions of time to quantify infrastructure resilience in multi-hazard situations. Reference [79] proposed different internal and external resilience policies as resilience indicators to form a holistic framework for building critical infrastructure resilience. Reference [77] discussed relevant metrics for resilience capacities in the transport infrastructure domain to assess the robustness and rapidity of recovery. These indicators are identified based on the knowledge gathered from various experts in the related field.

# 3.2.2. Identifying Interdependencies, among Sustainability and Resilience Factors 

Either directly or indirectly, sustainability and resilience factors are interdependent. For instance, adaptive capacity in the resilience curve would encourage decision-makers to establish more ready-to-use physical assets to increase redundancy, whereas the environmental dimension of the sustainability paradigm (such as energy efficiency or air pollution reduction) would bolster the lean approach. Consequently, it is essential to capture these relationships between indicators of sustainability and resilience.

Various multi-criteria decision-making (MCDM) models have been applied to select and rank assessment criteria in different domains, including built and infrastructure environments. Reference [80], for example, applied AHP to select and prioritize the selected indicators for urban disaster resilience assessment and used TOPSIS to rank urban districts. The complex proportional assessment method was developed by [81] and applied to green building assessment. Reference [82] also developed the Degree of Project Utility and Investment Value Assessments to define the investment value of projects and optimize selected criteria. In this paper, the interdependencies between sustainability and resilience criteria are emphasized. Therefore, the combination of DEMATEL and the Bayesian network is applied.

DEMATEL is an identified, workable solution through which the network of interdependencies can be structured [83]. The method is based on graph theory, which allows us to visually plan and solve problems by categorizing relevant factors into cause-and-effect groups to confirm variable interdependence and facilitate the development of a directed graph to reflect variable interrelationships [84]. Accordingly, it would be an appropriate method whose results could be a reliable input for Bayesian network analysis. Reference [85] applied DEMATEL to determine interdependencies among supplier selection criteria and structured their casual graph as a Bayesian network. However, experts' opinions about the relationships between risks are mostly uncertain and cannot be expressed by crisp values. Thus, in this paper, the fuzzy DEMATEL (FDEMATEL) approach is applied to structure interdependencies among sustainability and resilience factors while accounting for the subjective judgments of experts [86]. Notably, FDEMATEL has already been applied in different contexts (e.g., [84,87,88]). More details about the FDEMATEL method applied in this paper have been provided in the online Supplemental Materials.

### 3.2.3. Bayesian Network Structure for Physical Asset Criticality Analysis

The Bayesian Network (BN) helps design stochastic relationships among a group of variables and performs probability updating and sequential learning [89]. BNs take uncertainty and variability into account when predicting decisions in a complex system [90]. BNs also aid in analyzing conditional probabilities by updating prior information or events. This is critical in the asset management context, as the metrics are highly dependent on one another and on external events. For instance, the criticality of a physical asset may change in response to planned maintenance activities or changes in the asset's environmental condition or manufacturing process. Accordingly, a network of causes and effects is structured by showing the variables as nodes and the casual relationships among them as edges that are associated with conditional probabilities. BN has been an effective tool for decision-making in different fields, such as risk analysis and reliability engineering in social, economic, or biological disciplines [48,91,92].

BN is based on Bayes' theorem for calculating conditional probabilities, and its algorithm follows Equations (3) to (5) [93].

$$
\begin{gathered}
P(X)=P\left(X_{1}, X_{2}, \ldots, X_{n}\right)=\prod_{X_{n} \in X} P\left(X_{n} \mid X_{p a(n)}\right) \\
P\left(X_{n}\right)=\sum_{\text {except } X_{n}} P(X) \\
P(X \mid e v)=\frac{P(X, e v)}{P(e v)}=\frac{P(e v \mid X) P(X)}{P(e v)}
\end{gathered}
$$

where Equation (3) is the joint probability, where $X_{p a(n)}$ is the set of parents of the node $X_{n}$. Equation (4) calculates the marginal probability of $X_{n}$ and Equation (5) is the probabilities of the occurrence of some nodes given evidence where $e v$ is the evidence found and $P(X \mid e v)$ is the posterior probability and $P(e v)$ is the prior probability [94]. To quantify the dependencies among variables, a node probability table (NPT) is usually given. In NPTs, information on the probability of a variable is provided according to the values of other variables. In this study, $e v$ determines whether or not the sustainability and resilience factors and sub-factors are realized/true.

By applying FDEMATEL, an initial structure for physical asset criticality analysis is determined. For further analysis, we need to restructure the initial network into a BN, since it must be a directed acyclic graph [95], while there might be some cycles in the structure derived from the FDEMATEL method. Therefore, possible cycles in the initial network should be eliminated. For doing so, we apply those guides provided by [85]. In this regard, we consider the following reasons for eliminating some cycles:

- The initial threshold for determining the causal relations may be defined imprecisely by experts. Therefore, the threshold can be modified to identify strong relationships between sustainability and resilience factors.
- In conducting the FDEMATEL survey, experts may indicate the correlation among the factors rather than causal relationships. Therefore, experts should review the graph to identify such correlations and eliminate them.
- The proposed general BN structure for physical asset criticality analysis is illustrated in Figure 3. The target variable is physical asset criticality analysis, which is conditioned on economic, social, environmental, and resilience factors. According to Equations (1) and (2), the resilience factor is calculated based on physical asset functionality loss, physical asset recovery point, physical asset recovery time, and total time to recover, which are conditioned on absorptive, adaptive, and restorative capacities. In addition, interdependencies may exist among sub-factors of different main factors, which are shown by the dotted line. The BN model may have different variable types:
- Equation type or continuous variables: these variables capture uncertainty via a probability distribution. These variables may be functions of other related variables.
- State Variables: uncertainty is captured based on a discrete probability distribution.
- Deterministic or fixed variables: these variables have either constant values or values that are determined based on the states of other related variables (parent variables).

![img-2.jpeg](img-2.jpeg)

Figure 3. General BN structure for physical asset criticality analysis.
Note that the parameters of the variables and their values would change regarding each physical asset.

# 3.2.4. Asset Criticality Index 

Physical assets should be prioritized based on the physical asset criticality analysis conducted in the previous step. For this, an asset criticality index is proposed in this paper. As shown in the general BN structure, the criticality of the physical asset is conditioned on sustainability and resilience factors. Therefore, the asset criticality index is a probabilistic statement about whether a physical asset is critical, conditioned on economic, social, environmental, and resilience factors. Moreover, according to companies' strategies, each factor may have a different importance level. To calculate the relative importance of factors, fuzzy BWM is applied. Finally, asset criticality analysis is calculated by the following equation:

$$
A C I_{i}=\sum_{j} w_{j} \cdot \operatorname{Prob}\left(\text { Factor }_{j}=\text { True }\right)_{i}
$$

where $A C I_{i}$ denotes the asset criticality index for physical asset $i, w_{j}$ is the defuzzified relative importance of factor $j$, which is derived from fuzzy BWM, and $\operatorname{Prob}\left(\right.$ Factor $\left._{j}=\right.$ True $)$ states the probability that the physical asset $i$ is Factor $_{j}-$ critical (for example economiccritical), where $j$ covers all the economic, social, environmental, and resilience factors. This probability is derived from the BN structure.

### 3.3. Analysis of the Results

When choosing asset management plans, it is crucial to trigger factors that significantly influence the criticality of assets. In this way, the condition of physical assets could be improved with limited available resources. For this, the expected asset criticality index (EACI) for each variable should be calculated. $\left(E A C I_{j}\right)$ is defined as the asset criticality index if variable $j$ is in critical condition. For instance, consider physical assets as critical if maintenance cost is higher than 16,000 USD. In this case, the maintenance cost is set to more than 16,000 USD, and the asset criticality index is calculated by running the BN network. The result is equal to $E A C I_{\text {maintenance cost }}$. The normalized expected asset criticality index is

proposed as Equation (7) to prioritize variables. Factors with higher $E A C I_{j}$ should have priority over other factors in developing asset management plans.

$$
N E A C I_{j}=\frac{E A C I_{j}}{\sum_{j} E A C I_{j}} \forall j \in \text { those criteria contributing to criticality }
$$

# 4. Case Study 

In this section, the proposed BIA-based mixed sustainability and resilience framework for physical asset criticality analysis is applied to a gas plant of a gas company (hereafter called the GP). The plant produces different products, including propane, butane, elemental sulfur, and condensate. There are different equipment in the plant, such as slug catchers, tanks and pumps, exchangers, furnaces, drums, etc. GP has planned to improve its physical asset management system by implementing proper physical asset continuity plans to ensure the continuity of the entire system. Sustainability and resilience factors are considered according to the physical asset management strategy and business strategies. Accordingly, our proposed framework would provide the top managers with valuable information about critical physical assets. Notably, the data needed for each step of the framework is gathered through experts' judgments based on historical data available on the sites or quantitative risk assessment scenarios.

### 4.1. Key Product Determination in GP

As stated before, GP produces four products, including propane, butane, elemental sulfur, and condensate. Five criteria, including the loss of revenue (Ca), the degree of damage to the company's reputation $(\mathrm{Cb})$, the importance of the product for the country according to the country's policies (Cc), the defection of customers (Cd), and the loss of interested party's supports (Ce) are first chosen from [8] considering industry requirements. Then, four top managers (i.e., the GP manager, sales manager, marketing manager, and financial manager) were asked to fill out the BWM questionnaire, indicating the most and least important criteria and comparing other criteria with them. The fuzzy weights of product prioritization criteria are calculated by solving the corresponding optimization model introduced in the fuzzy BWM [59]. The derived fuzzy weights are then incorporated into the fuzzy TOPSIS method to identify the products' ranking vectors. The condensate with a closeness coefficient of 0.987 is the most important product of GP, which was selected as the key product for further analysis. The details of the calculations are provided in the online Supplementary Materials.

### 4.2. Critical Physical Assets in GP

The first step in this stage is to identify all the required equipment for condensate production. For this, the block diagrams and P and IDs related to condensate production are checked with experts from the process engineering, operations, and asset management departments of GP. As a result, eight pieces of equipment were identified.

### 4.2.1. Sustainability and Resilience Factors for GP's Physical Assets

For the sake of criticality analysis, the relevant sustainability and resilience factors should be selected. For this, we held some group meetings with experts from GP and its parent company. Plant managers, asset managers, and health, safety, and environmental engineers from the GP and the parent company participated in these meetings. It is noted that factors derived from the literature (Table 2) and the company's strategies are considered to determine suitable sustainability and resilience factors. Table 3 represents the sustainability and resilience factors for GP's physical asset criticality analysis.

Table 3. Sustainability and resilience factors for GP's physical asset criticality analysis.


# 4.2.2. Bayesian Network Structure for Physical Asset Criticality Analysis 

In this step, interdependencies among identified sustainability and resilience factors are determined based on the process explained in Section 3.2.2. To this end, the members of the asset management committee were asked to indicate to what extent they believe a criterion affects others. The initial relationship network among the identified factors was obtained based on their subjective judgments. The threshold value was set at 0.5 to determine the initial interdependency graph. Based on the initial graph, a cycle existed between "Skilled Personal or Contractor to Repair" and "Maintenance Cost". According to the calculated total relation matrix, the value of the dependency of skilled personnel or contractors on repair and maintenance cost is 0.5102 , which is close to 0.5 . Hence, the threshold value is modified to 0.52 . Therefore, the cycle was eliminated. The final interdependency graph is a directed acyclic graph which is modelled as a Bayesian network. The Bayesian network structure is depicted in Figure 4, which is modeled by GeNIe [96].

![img-3.jpeg](img-3.jpeg)

Figure 4. Bayesian network structure for GP's physical asset criticality analysis.
4.2.3. Modeling Sustainability and Resilience Criteria in Physical Asset Criticality Analysis Bayesian Network

The next step is to model each criterion and factor determined in the Bayesian network. BN encompasses different types of variables, including equation type/continuous, state, and deterministic/fixed variables, which help quantify sustainability and resilience factors for asset criticality analysis. At this step, these variables and their parameters are elaborated for one of the critical physical assets derived from P and IDs and block diagrams (which is called PA1 hereafter). Note that variables for all physical assets are the same, while parameters are different.

- Modeling sustainability factors:

Sustainability consists of triple-bottom-line dimensions, including economic, social, and environmental factors. As depicted in Figure 4, the economic factor is conditioned on the maintenance cost, equipment cost, and production loss. Maintenance cost is defined with a truncated normal distribution (TNORM) whose parameters are determined based on the availability of skilled personnel or contractors to repair. Similarly, equipment cost is modeled with TNORM, whose parameters are defined according to the availability of spare parts. Failure in a physical asset may cause production loss in the key product, which is a major attribute for the economic factor in the criticality analysis. Maintenance and equipment costs are other influential criteria in the economic criticality of physical assets. These variables are explained in Table 4.

Table 4. NPT of the variables describing the economic factor and economic criticality.


The social factor has five criteria, including failure in emergency response, leakage possibility, types of fluid, pressure, and temperature. Based on the hazard diamond introduced in [97], the level of hazard for fluids can be calculated. Four measures, including flammability, instability, health, and specific hazard, were defined to assess the level of hazard for fluids. To calculate the level of hazard for fluids, the corresponding numbers for each measure are summed. Noteworthy, the degree of hazard of each measure is determined by an arithmetic number between 0 (no hazard) and 4 (maximum hazard). Therefore, the fluids' level of hazard would be a number between 0 (no hazard) and 16 (maximum hazard).

Pressure and temperature contributors are also categorized based on their quantity. Note that, the higher the temperature and the pressure are, the higher level of safety risks will exist. Categories for pressure and temperature are described in Table 5. These numbers are determined based on the experts' judgments. NPTs for failure in emergency response equipment, leakage possibility, and social criticality are presented in Table 6.

Table 5. Pressure and temperature categorization.


Table 6. NPT of the variables describing safety factors and social criticality.


To model environmental factors, air, water, and soil pollution are considered. Flaring is one of the significant contributors to air pollution in GP. Therefore, the amount of added flaring from storage tanks, units, and the whole plant due to failure in the physical assets should be calculated to model air pollution. For this, a random triangular distribution is considered. Table 7 represents NPTs for the criteria contributing to the environmental factor and environmental criticality.

Table 7. NPT of the variables describing environment criticality.


- Modeling resilience factors:

To model the resilience factor, physical asset functionality loss, physical asset recovery point, physical asset recovery time, and total time to recovery are calculated based on the absorptive, adaptive, and restorative resilience capacities. For this, the probabilities of relative criteria are determined based on historical data available in GP. Then, NPTs for absorptive, adaptive, and restorative capacities are described in Table 8, and NPTs for physical asset functionality loss, physical asset recovery point, physical asset recovery time, and total time to recovery are determined in Table 9.

Table 8. NPT of the variables describing resilience capacities.


Table 9. NPT of the variables describing resilience.


The aggregate resilience variable is then calculated according to Equations (1) and (2) to determine resilience factors. For values lower than 0.98 , the related physical asset is attributed as the resilient-critical one.

# 4.2.4. Calculating the Asset Criticality Index 

Based on the variables and parameters defined in the previous section, the Bayesian network is run, and the probability of it being economically, socially, environmentally, or resiliently critical is calculated. The results are shown in Figure 5. To calculate the asset criticality index, the weights of resilience, economic, social, and environmental criticality are first determined. Thus, we convened some group meetings with the plant manager, mother company manager, and asset manager to determine the most and least important factors. The experts were questioned about their fuzzy preferences for the most important factors over all other factors (Table 10) and their fuzzy preferences for all factors over the least important factors (Table 11). Then, the weights of the factors were calculated using the fuzzy BWM [59]. The results are shown in Table 12.

![img-4.jpeg](img-4.jpeg)

Figure 5. Results for economic, social, environmental, and resilient criticality of PA1 in GP.

Table 10. The linguistic terms describing the fuzzy preferences of the most important factor over all the factors.


Table 11. The linguistic terms describing the fuzzy preferences of factors over the least important factor.


Table 12. Fuzzy weights of factors.


The asset criticality index for PA1 is calculated by applying Equation (6). The results for all ten key physical assets for GP are shown in Figure 6. As the figure shows, PA4 and PA2 are the most critical physical assets in GP. Note that the higher the critical asset index is, the more its corresponding physical asset will need proper asset management plans. Therefore, PA2 and PA4 should be given priority when asset management plans are developed or implemented.

![img-5.jpeg](img-5.jpeg)

Figure 6. Asset criticality index for key physical assets in GP. PA stands for physical assets.

# 4.3. Model Validity and Analysis of the Results 

To validate our proposed framework, we applied face validity, which is one of the most prevalent tests for expert-elicited BNs [98]. For this, we gathered experts from various departments of the Gas Company's gas plants as well as scientists from the process engineering, mechanical engineering, and industrial engineering departments of three Iranian universities. We posed questions regarding the suitability of the proposed BN structure and parameterization. According to [98], we asked the following questions:

- Are the model's node and arc structures consistent with expert predictions?
- Does the model's structure resemble that of other networks in the resilience domain?
- Are the parameters of each node consistent with what experts would expect?

The results of the questionnaire were satisfactory, and the structure and parameters were validated. Another useful method to investigate the validity of an expert-built model is to perform sensitivity analysis [91].

In this section, a sensitivity analysis is conducted to determine the impact of variables on the asset criticality index. For this, $E A C I_{j}$ and $N E A C I_{j}$ for all criteria are calculated. The criteria are ranked based on their $N E A C I_{j}$ value. The results are presented in Table 13.

Based on the results shown in Table 13, equipment cost is the most influential variable on the criticality of the physical asset, while the availability of backup assets is the least influential variable. As backup contractors are likely to be available in disastrous situations, the availability of backup assets has little influence on the criticality of assets. Noteworthy, the priority of variables guides the company in prioritizing their asset management plans regarding their influence on asset criticality.

Table 13. Variables priorities based on expected asset criticality index.


# 5. Contributions 

### 5.1. Contributions to Practice and Managerial Insights

To conduct the physical asset criticality analysis, the following managerial tips should be considered:

- Continuity of key products/services provided in every situation, including disastrous ones, helps organizations foster their reputation. There is a strong relationship between the continuity of physical assets and the continuity of products in asset-intensive organizations. Therefore, the relationship between the continuity of key products' provision and the continuity of physical assets should be addressed in criticality analysis. Accordingly, our framework proposes a business impact analysis approach through which required physical assets for the continuity of product/service provision are identified.
- Sustainability and resilience are crucial factors for organizations' sustained success. For this reason, our framework for criticality analysis not only considers these two main factors and their corresponding criteria, but it also captures the interdependencies that exist between them. Accordingly, the framework provides sufficient tools for asset managers to be consistent with organizations' strategies while prioritizing physical assets.
- Organizations usually struggle with limited resources for their asset management plans. Therefore, the normalized expected asset criticality index is proposed in this paper to prioritize the contributing criteria of criticality analysis. This index will guide managers in taking appropriate directions while developing asset management plans. The priority of variables guides the company in prioritizing their asset management plans.


### 5.2. Contributions to Knowledge and Theoretical Insights

The theoretical contributions of the proposed framework are as follows:

- To our knowledge, this is the first study that applies business impact analysis to determine key physical assets as a prerequisite to criticality analysis. Therefore, our proposed framework acts as a bridge between physical asset management and business continuity management.
- In the literature, a majority of studies on criticality analysis conduct failure mode and affect analysis (FMEA) or similar risk management tools in which interdependencies among contributing factors to criticality are not incorporated. It should be noted that the presented BIA-based criticality analysis framework proposes a combined fuzzy DEMATEL-Bayesian network model to capture interdependencies among sustainability and resilience contributing factors to the asset criticality analysis.

- Unlike other relevant studies to the physical asset criticality analysis, we consider the sustainability and resilience factors as the contributing factors in the criticality analysis. Moreover, a fuzzy BWM is applied to determine the relative importance of each factor in the asset criticality index, which makes the physical asset ranking procedure more realistic.


# 6. Conclusions 

This paper develops a comprehensive framework for physical asset criticality analysis. The framework is developed based on the BIA framework and helps asset managers take into account those assets that are crucial for the continuity of key products' provision. In this way, a hybrid fuzzy BWM-TOPSIS methodology is proposed to rank the organization's products based on relevant criteria. Then, the physical assets required for producing the key products are determined through proper tools based on the industry type (e.g., block diagrams and P and IDs for the process industry). To prioritize the required physical asset, sustainability and resilience factors are determined as the contributing factors to the criticality analysis. Then, the physical asset criticality index is calculated through a hybrid fuzzy DEMATEL-Bayesian network approach, in which interdependencies among sustainability and resilience factors are captured. Accordingly, the availability of "spare parts" and "skilled personnel or contractors to repair," which are indicators of the restorative capacity of resilience, is inter-related with "maintenance costs," which is an indicator of the economic dimension of sustainability. Furthermore, the availability of a "safety relieve valve", which is an indicator of the absorptive capacity of the resilience paradigm, is associated with safety, an indicator of the social factor of sustainability. In the meantime, in the case study, we have provided a comprehensive guide to constructing the Bayesian network for physical asset criticality analysis in a gas plant. In this regard, we presented NPTs for each variable contributing to the asset criticality index for one of the required physical assets for the continuity of the key products' provision. The NPTs are constructed based on the historical data available for the gas plant or quantitative risk assessment scenarios conducted for the plant.

Future research may focus on the applicability of the proposed framework in different industries, including the service sector. Moreover, the application of the INVAR method and its combination with the Bayesian networks for sustainability and resilience criteria may be studied.

Supplementary Materials: The following supporting information can be downloaded at: https: //www.mdpi.com/article/10.3390/buildings13010264/s1.

Author Contributions: Conceptualization, M.A. and K.R.; methodology, M.A. and K.R.; software, M.A., S.M.K.; validation, M.A., K.R. and S.A.T.; investigation, M.A., S.A.T. and K.R.; writing—original draft preparation, M.A.; writing-review and editing, M.A., S.A.T., S.M.K. and K.R.; visualization, M.A.; project administration, M.A. and K.R. All authors have read and agreed to the published version of the manuscript.
Funding: This research received no external funding.
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: The data used in the study is available with the authors and can be shared upon reasonable request.

Conflicts of Interest: The authors declare no conflict of interest.

# Acronyms 

