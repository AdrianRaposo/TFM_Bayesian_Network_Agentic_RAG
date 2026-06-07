# Towards Integration of Security and Safety Measures for Critical Infrastructures Based on Bayesian Networks and Graph Theory: A Systematic Literature Review 

Sandeep Pirbhulal ${ }^{1,2, *}$, Vasileios Gkioulos ${ }^{1}$ and Sokratis Katsikas ${ }^{1 *}$


#### Abstract

check for updates Citation: Pirbhulal, S.; Gkioulos, V.; Katsikas, S. Towards Integration of Security and Safety Measures for Critical Infrastructures Based on Bayesian Networks and Graph Theory: A Systematic Literature Review. Signals 2021, 2, 771-802. https://doi.org/10.3390/ signals2040045


Academic Editors: Vessela Krasteva and Toshihisa Tanaka

Received: 15 June 2021
Accepted: 28 October 2021
Published: 2 November 2021

Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## (0) 0

Copyright: (c) 2021 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 Department of Information Security and Communication Technology, Norwegian University of Science and Technology, 2815 Gjøvik, Norway; vasileios.gkioulos@ntnu.no (V.G.); sokratis.katsikas@ntnu.no (S.K.)
2 Norwegian Computing Center, P.O. Box 114, Blindern, 0314 Oslo, Norway

* Correspondence: sandeep@nr.no; Tel.: +47-41-393-687


#### Abstract

In recent times, security and safety are, at least, conducted in safety-sensitive or critical sectors. Nevertheless, both processes do not commonly analyze the impact of security risks on safety. Several scholars are focused on integrating safety and security risk assessments, using different methodologies and tools in critical infrastructures (CIs). Bayesian networks (BN) and graph theory (GT) have received much attention from academia and industries to incorporate security and safety features for different CI applications. Hence, this study aims to conduct a systematic literature review (SLR) for co-engineering safety and security using BN or GT. In this SLR, the preferred reporting items for systematic reviews and meta-analyses recommendations (PRISMA) are followed. Initially, 2295 records (acquired between 2011 and 2020) were identified for screening purposes. Later on, 240 articles were processed to check eligibility criteria. Overall, this study includes 64 papers, after examining the pre-defined criteria and guidelines. Further, the included studies were compared, regarding the number of required nodes for system development, applied data sources, research outcomes, threat actors, performance verification mechanisms, implementation scenarios, applicability and functionality, application sectors, advantages, and disadvantages for combining safety, and security measures, based on GT and BN. The findings of this SLR suggest that BN and GT are used widely for risk and failure management in several domains. The highly focused sectors include studies of the maritime industry ( $14 \%$ ), vehicle transportation ( $13 \%$ ), railway ( $13 \%$ ), nuclear ( $6 \%$ ), chemical industry ( $6 \%$ ), gas and pipelines ( $5 \%$ ), smart grid ( $5 \%$ ), network security ( $5 \%$ ), air transportation ( $3 \%$ ), public sector ( $3 \%$ ), and cyber-physical systems ( $3 \%$ ). It is also observed that $80 \%$ of the included studies use BN models to incorporate safety and security concerns, whereas $15 \%$ and $5 \%$ for GT approaches and joint GT and BN methodologies, respectively. Additionally, $31 \%$ of identified studies verified that the developed approaches used real-time implementation, whereas simulation or preliminary analysis were presented for the remaining methods. Finally, the main research limitations, concluding remarks and future research directions, are presented


Keywords: graph theory; Bayesian networks; safety; security; critical infrastructures; literature review

## 1. Introduction

In recent times, the growth of the internet of things (IoT) and information communication technologies (ICT) have revolutionized the modern era and critical infrastructures (CIs), including smart manufacturing, healthcare, energy sector, education, and maritime transportation, among others [1,2]. On the one hand, modern communication and electronic technologies have provided many facilities to individuals and nations in different CIs. On the other hand, safeguarding security and safety are essential requirements to offer authenticated operations against possible cyber threats and crises within the respective CIs [3]. Generally, the security mechanisms focus on recognizing and managing risks interrelated with accessibility, privacy, and integrity of devices in CIs. However, safety

approaches are inclined to predict, classify, and resolve the vulnerabilities linked with the safety of humans, systems, and infrastructures. Therefore, integrating both aspects can help identify potential vulnerabilities and threats and the evaluate probable risks associated with the security and safety of CIs.

The incorporation of security and safety aspects has received massive attention worldwide [4,5]. Recent research shows that safety, especially cybersecurity, share interdependencies in many products, especially cyber-physical systems (CPS) [6]. Besides safety regulations interfering in possible security solutions, a fundamental problem is the rising number of cybersecurity threats that negatively impact the affected functional safety and reliability of systems [7]. In safety-sensitive environments, such as the in railway, aircraft, or automotive industries, the consideration of security is widespread [8]. Decision-makers must determine whether the identified issue is due to an attack or technical failure. A precise diagnosis is crucial for an effective response to identified problems. For example, fixing or exchanging the module responsible for the observed issue could be a reasonable response tactic for a technical failure. Simultaneously, blocking an attack vector, utilizing an identified adversary-caused problem, might be an efficient response monitoring strategy.

If the decision-makers can calculate that the apparent problem is an attack, the efficient response policies to resist each attack vector would be dissimilar. For example, the operative response approach for an information manipulation threat on the device could acquire data integrity checks. In contrast, the active response approach against the physical tampering of the device would augment access control. Remarkably, the decision supporting the regulation of the utmost probable root cause for evident problems is not available. In these conditions, Bayesian networks (BNs) could be helpful to solve this problem, mainly cybersecurity and safety applications [4-7]. In BNs, both qualitative and quantitative components are included, such as the directed acyclic graph (DAG) and conditional probability table (CPT), for each node in the DAG, respectively [8]. Furthermore, the graph theory (GT) and neutral network are also incorporated with the safety aspects of network security [9].

Some systematic literature reviews (SLRs) or literature reviews related to safety and security, based on BNs or GT, are available in the literature. Sharma et al. presented a systematic review of safety and security measures for machine learning-enabled agricultural applications. The focus of this study was BN approaches; however, GT was not addressed [10]. Gupta et al. performed a systematic review on blockchain-oriented security outbreak resilience systems for self-governing automobiles. The main limitations are that vehicle applications and their safety aspects are not considered [11]. Chockalingam et al. conducted SLR on 17 BN-based models for integrating cybersecurity and safety measures in different applications [12]. The main drawback of this SLR includes that it merely emphasized BN models; however, GT was not addressed. Lallie et al. reviewed the threat graphs and visual tree syntax-based GT mechanisms, which describe the cyber-attacks central theory, before elaborating on how vital components of a cyber-attack are characterized in attack graphs and outbreak trees. However, safety concerns are not addressed [13]. The main problem with the studies mentioned above is that the SLR or review, based on either GT or BN , ensures safety and security. Since GT and BN are practical approaches to analyzing safety and security risks, there is still a lack of SLR based on both these approaches.

This SLR aims to present current inclinations and advancements, as well as the limitations of incorporating safety and security using GT and BN. The chief contributions of this study are the following:
(a) To identify records, using search queries from numerous databases, including Scopus, ACM, and the Web of Sciences, focusing on united safety and security using GT and BN models.
(b) To perform a comprehensive comparative interpretation of classified approaches, regarding threat actors, performance verification mechanisms, the number of applied nodes for system development, and implementation scenarios, among others, for combining safety and security aspects using GT or BN methodologies.

(c) To illustrate the research consequences of this SLR, based on pre-defined research questions (RQs).
(d) To elaborate pros and cons, limitations, and future research directions of BN and GT approaches for integrating safety and security.
The organization of this paper is stated as follows: the background, to analyze security and safety risks for CIs using BN and GT approaches, is represented in Section 2. In Section 3, the research design, including research questions (RQs), search query, and pre-defined criteria of records, are demonstrated. In Section 4, the identified studies were compared in different aspects, such as application sectors, implementation criteria, applicability, etc. The discussion of RQs, based on included studies, as well as the limitations, are presented in Section 5. Finally, in Section 6, the concluding remarks and future research directions are represented.

# 2. Background 

Incorporating safety and security has received great attention for different applications; a few unified approaches have been designed to evaluate both measures. Though security analysis is implemented in the overall design procedure, it is generally not combined into the safety analysis development [5,14]. Recently, the introduced approaches comprehended the significance of integrated safety and security analysis and intended to incorporate both into a joint methodological process. Two applicable techniques, which describe the integration of security into safety analysis, recommend a merging of fault tree analysis (FTA) with attack tree analysis (ATA) [14] or boolean driven Markov processes (BDMP) [15]. Other introduced approaches either combine safety and security methods, e.g., ATA and bowtie analysis [16], or integrate both fields. However, there are not any practical mechanisms to deal with safety and security integration in real-time applications. Moreover, BN- and GT-enabled approaches have received much attention worldwide, as a solution offering safety and security in several domains.

### 2.1. Bayesian Networks

The BN (referred to as belief networks) represents a hypothesis of rationalizing from uncertain evidence to uncertain conclusions, since it can perform the factorization of the collective distribution of variables, based on the conditional dependencies. BN is helpful in addressing uncertainty and incompleteness problems; thus, it is extensively applied in several domains. BN graphically depicts the logical associations between variables and recognizes the connections between these variables by conditional probabilities. By interpretation, a BN represents a directed acyclic graph (DAG), which encodes a conditional probability distribution. Nodes and arcs are vital components of BN, the nodes symbolize arbitrary variables and the arcs signify random relations between variables. There is a probability function for each state of the node, and conditional probabilities are used to exhibit the associations between variables.

BNs are probabilistic graphical models; these visual structures characterize the information about an uncertain system [17]. BNs are generally utilized for examining the hazards and vulnerabilities of networks, which are acyclic graphs that provide a quantitative and qualitative assessment of risks. Judea Pearl initially proposed the BN-based approach in 1985 and was usually utilized to distribute random information in AI. Owing to the unique functionality of BN for constructing the structures and algorithms, it is successfully used in e-commerce, transportation, data mining, energy control, etc. It is a DAG-based probability rationalization and appropriate for uncertainty representation of queries. BN must be a DAG and CPT (conditional probability table).

BN has been demonstrated to be a powerful tool for solving several problems with uncertain knowledge illustration and reasoning [18,19,20]. The BN formula is represented in Equation (1):

$$
\mathrm{P}\left(\mathrm{X}_{\mathrm{j}} \mid \mathrm{Y}\right)=\frac{\mathrm{P}\left(\frac{\mathrm{Y}}{\mathrm{X}_{\mathrm{i}}}\right) \mathrm{P}\left(\mathrm{X}_{\mathrm{j}}\right)}{\sum_{\mathrm{j}=1}^{\mathrm{m}} \mathrm{P}\left(\frac{\mathrm{Y}}{\mathrm{X}_{\mathrm{j}}}\right) \mathrm{P}\left(\mathrm{X}_{\mathrm{j}}\right)}
$$

where $\mathrm{P}\left(\mathrm{L}\right.$ ) stands for the conditional probability distribution. Suppose the sample space N of experiment $\mathrm{L}, " \mathrm{Y}$ " is the random event of $\mathrm{L} . \mathrm{X}_{1}, \mathrm{X}_{2}, \ldots, \mathrm{X}_{\mathrm{n}}$ is the incompatible set of possibilities in experiment $L$, and " $X_{j}$ " represents the entire group event from $(j=1,2, \ldots, m)$.

Figure 1 represents the three-variable examples of BN structure. A BN comprehends two types of nodes, i.e., the parent and child nodes. The parent node (cause) is at the start of any directed edge; the child node (fruit) is at the end. The directed edge specifies that the two nodes are interrelated. In Figure 1, X, Y are the two-parent nodes of Z. Z is the child nodes of $X$ and $Y$. Prior probability: $P(X)$ characterizes the probability of event $X ; P(Y)$ is the probability of event $Y ; P(Z \mid X, Y)$ is the probability that the event $Z$ occurs before the condition that occurs at $X$ and $Y$. The posterior probability, $P(X \mid Z), P(Y \mid Z)$, and so on, can be obtained through the known prior probability.
![img-0.jpeg](img-0.jpeg)

Figure 1. Three variable Bayesian network examples.
A node without a parent is known as a root node, and a node without children is termed as a leaf node. In BNs, nodes with links represent system variables demonstrating uncertain dependencies. Specifically, every node in the graph characterizes an arbitrary variable, whereas the ends between the nodes represent the dependencies of respective random variables [21]. Usually, statistical and computational techniques are used to calculate these provisional dependencies in the chart. Hereafter, BNs merges concepts from statistics, GT, and probability theory [22]; also, Bayesian probabilistic (BP) are used by considering probability as a mark of belief. The BP is less severe, concerning evidence, than the typically utilized probability methods. BN represents a combination of likelihood and GT; thus, it computes dependencies between several information or fact uncertainties [23]. FTA and ATA can be easily transferred to BN because it familiarizes the assemblies of various data, knowledge, functional associations, and approaches; also, it allows for conducting the extensively utilized interpretation for additional analysis [24,25,26,27]. In current studies of safety and security co-engineering methods, some factors are not considered, such as parameter optimization and balancing; thus, BN-based techniques can solve these essential issues.

# 2.2. Graph Theory 

CIs are a highly interrelated and interdependent system, comprising several components, services, and nodes containing crucial information. There are numerous threats and

risks that may endanger critical data security and privacy in different CIs. After recognizing the CI risks, the next step for the CI safety and security evaluation is to offer an appropriate model for demonstrating the connection among potential risk sources. The GT model represents the study of mathematical structures applied to prototypical pairwise associations between entities, including nodes and points connected by edges or links. For GT analysis, graphs can be divided into various types, comprising of directed and undirected graphs and connected and disconnected charts, as well as weighted, bipartite, and simple graphs. GT analyzed the connectivity properties for susceptibility, trustworthiness, and risk analysis for several applications, i.e., vehicle networks using different graphs [28,29,30]. Moreover, topological properties enable techniques, flow-based approaches, and hybrid methods to analyze the reliability, hazards, and safety of systems [31].

There are several benefits of using the graphs model in different sectors. The first and foremost strength of GT is to describe the topological association between several nodes, connecting links between locations (Figure 2). It helps review the connectivity and the degree distribution of every location in a topological space. Those notions are essential for examining the networks. In the case of a spatial network, the vector and geometric characteristics are incredibly beneficial. Vectors properties provide a directional links; for transportation modeling, this property is applied to model flows between locations. The usage of geometrics properties is to insert distance into the model, allowing spatializing the system in Euclidian space. Moreover, GT also offers a description of relations through the graph. Based on the path, i.e., a course among components into the graph, and cycle (a path with a similar origin and endpoint), these characteristics allow for the study of the relationships between various parts of the charts [32,33,34].
![img-1.jpeg](img-1.jpeg)

Figure 2. An illustration of graph theory.
In existing studies, GT has been applied in protecting systems [35]. An undirected graph $\mathrm{H}=(\mathrm{U}, \mathrm{F})$ represents a mathematical structure, comprising two sets, U and F , where $\mathrm{U}=\left\{\mathrm{u}_{1}, \mathrm{u}_{2}, \ldots, \mathrm{u}_{\mathrm{m}}\right\}$ defines the set of nodes. The set of edges is presented by $\mathrm{F}=\left\{\mathrm{f}_{1}\right.$, $\left.\mathrm{f}_{2}, \ldots, \mathrm{f}_{\mathrm{n}}\right\}$. The undirected graph may be useful in presenting CIs or any other complex systems. Furthermore, each subsystem, such as oil and gas, power, and networks, can be exhibited by a subgraph. In GT, each component of the system represents a link, and the nodes are the connections between components, as per the topology of the network. Interdependencies among subsystems are modeled as definite links between end terminals of the two relevant components or subsystems. The CI graph model is supposed to have $m$ nodes and n connections [36].

GT has become a critical component in various computing applications, such as CI security and network development. However, it is also among the most challenging areas to comprehend and apply for protecting networks, as well as infrastructures. Chung and Lu discussed GT and its real-time implementation in different threat and vulnerability analyses [37]. Ahmat et al. discussed the optimization problems associated with GT and its security applications, using GT concepts to characterize various networks, assess network protocols for multiple scenarios in networking and security, and tools used to generate graphs for demonstrating real-world systems [38]. Shirinivas et al. demonstrated GT's applicability in heterogeneous fields but primarily focused on technical applications that utilize theoretical graph notions [39].

# 3. Research Design 

This section presents the fundamental stages for designing this SLR. This study follows the recommendations of the preferred reporting items for systematic reviews and metaanalyses (PRISMA) statement [40]. This design is used to select the security and safety literature, based on BN and GT, to compare and analyze the included studies.

### 3.1. Search Querry Process and Research Questions

In this SLR, ScienceDirect, IEEE Xplore, Web of Sciences, Scopus, and ACM databases were included. Later, a query was asked from identified databases for integrating safety and security, based on Bayesian networks or graph theory (also a combination of both). The search query for this SLR is given below:
("security" AND "safety") AND ("bayesian network" OR "graph theory")
The SLR is a series of associated arguments in support of the research questions (RQs). The RQs of this SLR is stated as follows:

1. Why is the integration of security and safety needed?
2. How have BN- and GT-based methodologies been utilized for security and safety studies in CI?
3. What have been the targeted application domains?
4. What solutions have been developed in the identified studies?
5. How is performance validated for developed techniques and algorithmic solutions?
6. What are the advantages and disadvantages of existing studies?

### 3.2. Exclusion and Inclusion Criteria

This study applies the web application Rayyan QCRI to eliminate duplicate records from different databases and estimate the eligibility of recognized records [41]. Moreover, in this SLR, we used the following exclusion criteria (EC):
(a) Studies that are not focused on the integration of safety and security, based on Bayesian networks or graph theory (also a combination of both).
(b) Studies that merely provide background about the integration of both measures.
(c) Studies that do not develop or design a novel method/approach/model/tool.

In this SLR, we followed specific inclusion criteria for considering studies to be included for analysis. The inclusion steps for this SLR are stated as below:
(a) Published in a conference or journal classified in the identified databases.
(b) The records are identified from January 2011 to September 2020.
(c) Developed a tool or technique for integrating safety and security measures using Bayesian Networks or Graph Theory (also a combination of both approaches).

## 4. Results

This section discusses BN and GT approaches for security and safety to recognize the significant patterns and findings in applying different applications. Moreover, this study analyzes the identified studies, based on organization and classification, citation index,

applied data source, number of used nodes, application, application sector, threat actor, functionality, implementation scenarios, and validation methodologies.

# 4.1. Organization and Classification of Included Studies 

In this study, at the initial stage, 2295 records were identified during the search process, including ScienceDirect ( $\mathrm{n}=1610$ ), Scopus ( $\mathrm{n}=213$ ), ACM ( $\mathrm{n}=205$ ), IEEE Xplore ( $\mathrm{n}=193$ ), and Web of Science ( $\mathrm{n}=74$ ). Later, 2093 unique records were recognized, after deleting the duplicate records by applying the screening tool. The title and abstract review recommend that 1853 records be excluded by following the exclusion and inclusion criteria, as elaborated on in Section 3.2. From examining the full-text articles of 240 records, based on the eligibility check process stated in Section 3, 176 were excluded. Merely, 64 papers have discussed the security and safety integration for different CI applications based on BN and GT and can be considered to perform comparative analysis in this SLR [42-105]. Figure 3 presents a flowchart of the multiple record processing stages in this SLR.
![img-2.jpeg](img-2.jpeg)

Figure 3. A flowchart of records processing stages.
The details of the included papers, including study year, number of used references, and category are shown in Table 1. Figure 4 demonstrates that the journal and conference proceedings are $61 \%$ and $39 \%$ of total articles, respectively.

Table 1. Details of included articles.


Table 1. Cont.


![img-3.jpeg](img-3.jpeg)

Figure 4. Analysis of identified articles in this SLR.

# 4.2. Included Studies Based on GT and BN for Safty and Security 

In recent times, security and safety problems are rapidly converging on different applications, leading to conditions where these closely associated measures that need to be integrated, instead of applied discretely or categorized. Several scholars have developed innovative methodologies to solve risk analysis and evaluation from safety, security, and united security risk management. Table 2 includes existing techniques, based on BN and GT, to resolve safety and security concerns and their respective application sectors.

Table 2. Description of included studies.


Table 2. Cont.


Table 2. Cont.


Table 2. Cont.


Table 2. Cont.


# 4.3. Citation Index of Included Studies 

In this SLR, the citation index is adapted to evaluate the research quality of each included technique, i.e., BN or GT or unified BN and GT. The citation index represents the number of citations of the included studies as per Google Scholar, accessed on 20th November 2020, as revealed in Table 3. The most extensive cited studies were 139 citations for Shuliang et al. [103], 76 citations are Jinsoo et al. [82], and 60 citations for Huai et al. [68], which are published in 2012, 2015, and 2017, respectively. Whereas the following studies have not received any citations: Tai-hua et al. [46], Xiaoxue et al. [48], and Xin et al. [49] (published in 2020), Sabarathinam et al. [56], Xiqiang et al. [62], and Jamal et al. [63] (published in 2019), Zhao et al. [76] (published in 2016), Jiali et al. [90], and Zeng Xianfeng [93] (published in 2014), and Mo Ming [102] (published in 2012).

Table 3. Citation index and data sources of included studies.


Table 3. Cont.


Table 3. Cont.


However, the record number of included articles per year is reported in Figure 5, which demonstrates the research trend of applying GT and BN to implement safety and security, based on the included studies. The analysis suggests that scholars have been publishing more articles, addressing united safety and security aspects, in the last two years. From 2019 and 2020, 13 ( 9 BN, 1 GT, 1GT, and BN), and 9 ( 8 BN, 1 BN, and GT) papers are included in this SLR, respectively.

# Included Articles per Year 

![img-4.jpeg](img-4.jpeg)

Figure 5. Research trend of included studies.

### 4.4. Data Sources and Number of Nodes Used to Construct BN/GT

The BN and GT play a significant role in predicting and unintentionally diagnosing failures and targeted risks by using numerous tools and models, based on the information collected from the system expert's knowledge (EK) and/or from empirical data (ED). EK represents the opinions collected by interviewing the system or domain expert, and ED is the historical or experimental data gathered by real-time scenarios or the literature [50-54]. It is revealed in existing studies that a reliable strategy can be attained for the developed model by applying collective EK and ED. Figure 6 demonstrates that 26 out of 64 of the included studies used only ED to developed BN or GT approaches. Whereas 16 out of 64 applied EK and 26 out of 64 of included studies that utilized both ED and EK to develop

GT- or BN-enabled models. It is observed that 3 out of 64 of the included studies were based on integrating GT and BN for addressing united security and safety measures, and these studies employed ED analysis for the system development. Though 10 out of 64 included studies were based on GT, in which 7 uses ED, 2 applies EK, and 1 utilizes both. Besides, BN models are applied in 51 out of 64 studies, which categorize as EK (14), ED (16), and collective EK and ED (21).
![img-5.jpeg](img-5.jpeg)

Figure 6. The used data sources for developing BN and GT models.
Several nodes are linked together to represent BN or GT enabled systems for assessing risks and vulnerabilities in different applications. Moreover, the quantity of nodes can be utilized to represent the model complexity of the system. A large number of nodes may reflect the incapacitated association between input and output nodes by introducing in-between layers between source and destination. Chockalingam et al. [106] stated that it is suggested to have a total number of nodes in BN models less than 40. In this SLR, it is observed that 43 out of 51 BN-based model have used less than 40 nodes. However, the remaining eight have used equal or more than 40, including Xiaoyan et al. [65], Song et al. [104], Zhiqiang et al. [70], Xiqiang et al. [85], Barry et al. [54], Jiali et al. [90], Remya et al. [78], and Jinsoo et al. [82], 40, 45, 47, 47, 51, 58, 60, and 64, respectively. However, all models that utilized GT and BN simultaneously have used less than 40 nodes in the developed system. Moreover, it is also noticed that 2 out of 10 GT-based approaches have utilized more than 40 nodes comprising Huai et al. [68] and Shuliang et al. [103], 53 and 182, respectively. Whereas, remaining 8 included studies of GT employ less than 40 nodes.

# 4.5. Applicability, Threat Actor, and Implementation Criteria 

The characteristic applicability is used to comprehend the type of evaluation that is acquired from the developed methodologies. In this SLR, it is observed that 37 out of 64 studies ensure risk management in the proposed system for identifying, analyzing, evaluating, and treating loss exposures, as well as monitoring risk control and financial resources, to mitigate the adverse effects of loss. There are three main stages: identifying, assessing, and evaluating risk. The procedure for assessing risk is the main element in the risk management process. Generally, there are two sorts of risk assessment approaches, including quantitative and qualitative strategies. The qualitative assessment techniques primarily rely on proficient knowledge and attention for revealing the risks. In contrast, the quantitative assessment methods can compute the risk value of the system and emphasize the system's quantitative performance under the risks.

In general, the quantitative methods are chosen to conduct risk analysis and assessment, owing to the accurate explanations of system risks that can optimize the distribution

of protected resources. Whereas 10 out of 64 perform the task of vulnerability assessment for evaluating whether the network is vulnerable to any identified vulnerabilities, allocates severity levels to those susceptibilities, and recommends remediation or mitigation, if and whenever required. Moreover, 3 out of 64, 2 out of 64 , and 2 out of 64 perform attack analysis, fault analysis, and safety assessment, respectively. Besides, 10 out 64 studies perform distinct functionalities, comprising of Lipeng et al. [43], Niamat et al. [51], Alexandre et al. [55], Sabarathinam et al. [56], Mario C et al. [58], Elvin et al. [64], Subhojeet et al. [67], Huai et al. [68], Sher et al. [91], and TIAN et al. [94], holistic event investigation, resilience quantification, cyber impact assessment, root cause analysis, intrusion detection, trust computation, anomaly detection, reliability assessment, software verification, and water traffic management, respectively.

In this SLR, the threat actor is used to identifying that the included studies help prevent the attack. It is observed that the threat actor is classified into two types, such as external and internal. It is observed from Figure 7 that 7 out of 64 and 2 out of 64 studies have mentioned that the developed methodology is applicable against external and internal threats, respectively. Moreover, 2 out 64 developed approaches help prevent both internal and external threats. However, the remaining 53 included articles have not specified any particular kind of threat but rather concentrated on warnings and alarms, which may be suitable for various possible threats.

# Threat Actor in Included Studies 

![img-6.jpeg](img-6.jpeg)

Figure 7. Threat Actor in Included Studies.
Implementing GT- or BN-based models is vital to measure network performance, transform strategic plans to monitor failures and risks in the system, and apply the necessary actions to achieve integrated safety and security for different applications. During the review process, it is observed that GT- or BN-based development scenarios are an association of nodes, modules, and the implementation subsystems. This SLR suggests that $42 \%, 31 \%$, and $27 \%$ of the included studies performed simulated, real-time, and preliminary analysis, respectively, as shown in Table 4.

Table 4. Threat Actor and Implementation Criteria of Included Studies.


Table 4. Cont.


# 5. Discussion 

This section includes answers based on comparative analysis of included articles to find solutions for given RQs in Section 2.

### 5.1. Why Is the Integration of Security and Safety Needed?

In recent times, computer networks have been widely applied in several applications; any failure in these systems could have critical outcomes. There are various hypotheses about the characteristics such crucial systems must maintain, and the methods employed to protect them. Two such attributes are security and safety. Nevertheless, modern designs are usually needed to meet these two attributes simultaneously. Considering safety and security, common goals are needed to protect peoples or systems; therefore, safety-critical assets are considered.

Martin et al. [81] stated that the marine industry is a critical sector, and it is essential to combine safety and security concerns on the sea. The integration of two aspects concentrates on analyzing the energy supply vulnerabilities and introduces a methodology to evaluate the system's exposure using the spatial composition of maritime regions. This study contributes a GT-based model for offering safety and security in a maritime territory. Indeed, the developed model utilizes links, such as roads and ports, as nodes. Matti et al. [84] demonstrate the significance of public safety and security (PSS) in mobile networks. In this study, a risk evaluation model, using BN, is proposed for the current PSS telecommunication services.

### 5.2. How Have Bayesian Network- and Graph Theory-Based Methodologies Been Utilized for Security and Safety Studies in CI?

This RQ assists in knowing which models are used for safety and security integration, functionalities, and applicability. In this SLR, it is observed that $80 \%, 15 \%$, and $5 \%$ of the included studies use BN and GT, as well as both GT and BN, respectively, as shown in Figure 8.

## Unified Security and Safety based on BN and GT

![img-7.jpeg](img-7.jpeg)

Figure 8. Characterization of BN and GT models in included studies.
From Figure 9, it is observed that the developed models based on BN or GT in included studies were utilized to have two sorts of purposes, including diagnosis and prediction. The term diagnosis represents identifying the nature or cause of the incidents or other risks in the systems. In contrast, the prediction is associated with forecasting potential cyber threats in the respective CIs. This study identifies that $48 \%$ of approaches perform a diagnosis of the risks in different applications. However, $36 \%$ and $16 \%$ of papers ensure performance prediction and both prediction and diagnosis, respectively.

![img-8.jpeg](img-8.jpeg)

Figure 9. Functionality of included studies.
However, the applicability of included studies is demonstrated in Figure 10. The key applicability area for integrating safety and security using GT or BN is risk assessment ( $60 \%$ ) of included studies. It is observed that vulnerability assessment, attack analysis, safety analysis, and fault analysis are $16 \%, 5 \%, 3 \%$, and $3 \%$, respectively. Moreover, the applicability of approximately $1 \%$ of total studies is in holistic event investigation, resilience quantification, cyber impact assessment, root cause analysis, intrusion detection, trust computation, anomaly detection, reliability assessment, software verification, and water traffic management.

# Applicability of Included Studies 

![img-9.jpeg](img-9.jpeg)

Figure 10. Applicability of included studies.

# 5.3. What Have Been the Targeted Application Domains? 

Figure 11 demonstrates the application sectors of BN and GT models for jointly monitoring safety and security events. The key sectors are the maritime ( $14 \%$ ), vehicle transportation ( $13 \%$ ), railway ( $13 \%$ ), nuclear ( $6 \%$ ), chemical ( $6 \%$ ), gas and pipelines ( $5 \%$ ), smart grid ( $5 \%$ ), network security ( $5 \%$ ), air transportation ( $3 \%$ ), public sector ( $3 \%$ ), and CPS (3\%) industries. The other preferred application sectors were software (2\%), water traffic system ( $2 \%$ ), ICS ( $2 \%$ ), education ( $2 \%$ ), UAV ( $2 \%$ ), complex systems ( $2 \%$ ), oil wharf handling ( $2 \%$ ), process plant ( $2 \%$ ), socio-technical systems ( $2 \%$ ), SoS ( $2 \%$ ), navigation environment ( $2 \%$ ), petroleum plants ( $2 \%$ ), mobile networks ( $2 \%$ ), cognitive radio networks (2\%), Asian games ( $2 \%$ ), and medical ( $2 \%$ ).

## Application Sector for BN and GT

![img-10.jpeg](img-10.jpeg)

Figure 11. Application sectors of included studies.

### 5.4. What Solutions Have Been Developed in the Identified Studies?

This RQ aims to provide insight into the existing solutions, based on GT or BN, for integrating security and safety. The research outcomes of the included studies were shown in Table 5. It has been observed that $60 \%$ of the included studies have focused on risk assessment and monitoring. Meizhi et al. [44] presented a statistical evaluation of risks to achieve valuable insights into ports protection and build the fundamental BN approach. A dynamic model was introduced, using expert judgment and historical data to evaluate the emergency risk of sea lanes. André et al. [105] focused on protecting ventricular assist devices (VAD)-related risks that have great significance for patient safety, having customized VAD, regarding patients' intensity of sickness and metabolism. Moreover, safety-oriented guidelines are introduced, which also plays an indispensable role in decreasing risk reduction.

Table 5. Research outcomes of included studies.


Table 5. Cont.


5.5. How Is Performance Validated for Developed Techniques and Algorithmic Solutions?

Validation approaches are essential for BN or GT methods, in order to analyze the performance of developed methodologies. In this SLR, it is observed that 56 out of 64 studies were validated by different mechanisms, and the remaining 8 studies have not reported the validation process, as shown in Figure 12. Sensitivity analyses ( $20 \%$ of included studies) perform a critical function in estimating the robustness of the outcomes on the principal analyses of the developed approaches. It is an important measure to evaluate the influence or impact of key hypotheses or variations on the specific infrastructure, including different analysis methods, protocol variations, outliers, definitions of results, and missing data, among others [48-52]. Another important aspect for validating the proposed technique is comparative analysis ( $20 \%$ of included studies), in which the outcomes of distinct models with different assumptions are compared with the developed approaches [79,80]. The other validation mechanisms recognized in the included studies were expert evaluation, scenarios development, statistical analysis, empirical analysis, reachability graph, diagnostic analysis, checklists, cross-validation, and minimax analysis, $16 \%, 12 \%, 8 \%, 3 \%, 2 \%, 2 \%, 2 \%$, $2 \%$, and $2 \%$, respectively.

# Validation Approach for GT and BN 

![img-11.jpeg](img-11.jpeg)

Figure 12. Validation approaches of included studies.

### 5.6. What Are the Advantages and Disadvantages of Existing Studies?

As elaborated in the included studies, the incorporation of safety and security measures based on GT and BN can benefit different CIs. Although there are certain shortcomings with the developed solutions, the advantages and disadvantages of existing BN or GT methods are discussed in this section, as shown in Table 6.

Table 6. Pros and cons of included studies.


Table 6. Cont.


Table 6. Cont.


Table 6. Cont.


# 5.7. Limitations 

This study has given below limitations:
(1) The inclusion of articles is solely based on the English language, which indicates that notable studies of security and safety integration based on BN or GT in other languages have not been considered.
(2) The results of this SLR are based on a restricted number of databases. These databases are used, due to the widespread usage for querying papers in the field of GT and BN.
(3) Included studies were performed in different applications, so it might be not possible to compare each perspective.

## 6. Conclusions

Modern systems must simultaneously guarantee security and safety to provide continuous and accurate execution of crucial roles and services. Since security and safety depend on each other, they must be collectively applied to acquire the root cause assessment of noticeable issues. Therefore, numerous methods are developed to integrate security and safety; however, BN and GT are considered in this SLR, due to their extensive usage in various applications. This SLR includes 64 studies, and given below are concluding points:
(a) It is observed that from the 64 included studies, 51 used BN models, 10 utilized GT models, and the remaining 3 were based on united BN and GT.
(b) Most development scenarios utilized 40 nodes for performing experiments to observe unintentional failures or risks for GT and BN models.
(c) It has been emphasized that approximately one-third of BN and GT models were evaluated in real-time; however, others were either based on simulation analysis or theoretical concepts.
(d) There were two types of data sources (EK and ED) used for developing BN and GT models for different applications.
(e) The key performance validation mechanisms for the included studies were statistical analysis, expert evaluation, and sensitivity analysis.
The future research directions for safety and security integration were the following:
(a) There is a need to develop a generic tool or method or standard to combine security and safety, which can be helpful for different applications, since the significance of integrating both measures was demonstrated in this SLR, and a generic approach may offer feasibility and flexibility.
(b) It is observed that there are various validation methods for evaluating BN or GT. A more extended investigation is necessary to estimate the accuracy and efficiency of validation mechanisms, in order to find the optimal option.

(c) Moreover, there is a need to research to acquire information about the suitable number of nodes to ensure reliable and accurate performance for ensuring safety and security based on BN or GT models.
(d) Further research could improve Bayesian analysis based on the Metropolis-Hastings algorithm and Gaussian distributions [107].

Author Contributions: S.P., V.G. and S.K. designed the study theme and conducted the literature study. S.P. and V.G. examined the data from different databases and performed initial data screening. S.P. interpreted the results and wrote the paper. V.G. and S.K. analyzed data, verified the results, and revised the paper. S.K. assisted in supervising the activities and study's well-organized procedure. All authors have read and agreed to the published version of the manuscript.
Funding: This research received funding from the Research Council of Norway through (a) the CybWin (Cybersecurity Platform for Assessment and Training for Critical Infrastructures-Legacy to digital twin), project no. 287808; and (b) the SFI Norwegian Centre for Cybersecurity in Critical Sectors (NORCICS), project no. 310105.

Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Not applicable.
Acknowledgments: This work has received funding from the Research Council of Norway through (a) the CybWin (Cybersecurity Platform for Assessment and Training for Critical InfrastructuresLegacy to digital twin), project no. 287808; and (b) the SFI Norwegian Centre for Cybersecurity in Critical Sectors (NORCICS), project no. 310105. Also, authors would like to express great appreciation to IIK Department at NTNU Gjovik Campus, and ICT Research Department at NR.

Conflicts of Interest: The authors declare no conflict of interest.
