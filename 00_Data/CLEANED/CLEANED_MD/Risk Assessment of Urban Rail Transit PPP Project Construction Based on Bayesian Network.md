# Article 

## Risk Assessment of Urban Rail Transit PPP Project Construction Based on Bayesian Network

Zhansheng Liu * ${ }^{\text {O }}$, Yueyue Jiao, Anxiu Li and Ximei Liu

## check for updates

Citation: Liu, Z.; Jiao, Y.; Li, A.; Liu, X. Risk Assessment of Urban Rail Transit PPP Project Construction Based on Bayesian Network. Sustainability 2021, 13, 11507. https://doi.org/10.3390/ su132011507

Academic Editors: Pan Lu and Antonio Comi

Received: 3 August 2021
Accepted: 13 October 2021
Published: 18 October 2021

Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## (0)

Copyright: (c) 2021 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

Key Laboratory of Urban Security and Disaster Engineering of Ministry of Education, Beijing University of Technology, Beijing 100124, China; 13589238936@163.com (Y.J.); lianxiu1997@163.com (A.L.); lxm1881067@163.com (X.L.)

* Correspondence: lzs4216@163.com


#### Abstract

In recent years, the accident rate of urban rail transit PPP (public-private partnerships) project under construction has been relatively high, and the issue of security risks has attracted great attention from all walks of life. Therefore, it is necessary to identify, analyze, and evaluate the issue of security risks of the urban rail transit PPP project. This paper takes the PPP project of urban rail transit as the object. Through offline interviews and surveys and online questionnaires, this paper focuses on identifying and analyzing the risks brought by the introduction of PPP mode to the urban rail transit project and its action mechanism. The risk evaluation method based on Bayesian network model is studied, which is described from three dimensions: risk occurrence probability, risk reasoning, and risk sensitivity. Finally, an example of Xuzhou Metro Line 3 is given to verify the feasibility of the proposed method. This study provides a reference basis for relevant practitioners and promotes the healthy development of the industry.


Keywords: urban rail transit; PPP; Bayesian networks; construction risk; risk evaluation

## 1. Introduction

Urban rail transit has become the first choice for cities in many countries to alleviate traffic congestion due to its advantages of low pollution, large traffic volume, and fast running speed. In China, urban rail transit is developing rapidly. From the completion of Beijing Metro Line 1 in 1969 to the end of 2020, 45 cities have opened and operated urban rail transit lines. The mileage of urban rail transit lines that have been completed and put into operation has reached 7978.18 km . The capital of urban rail transit construction has always been dominated by local government finance in China. The investment in subway construction is huge. At present, the cost of subway construction is up to CNY 1 billion per kilometer, which brings great financial pressure and debt risks to the local government. Therefore, through drawing lessons from foreign PPP mode reform experiences, PPP mode was introduced into the field of urban rail transit. The PPP model is cooperation between the government and private capital. It is a project operation mode in public infrastructure. In this mode, private enterprises and private capital are encouraged to cooperate with the government to participate in the construction of public infrastructure. It provides innovative financing channels for urban rail transit projects and introduces new social forces for project construction [1].

Verified by the actual project, the application of PPP mode in the field of urban rail transit can reduce the burden on the government, facilitate the transformation of government functions, and improve the service level of urban rail transit. Therefore, many cities in China have chosen PPP mode to facilitate the development of urban rail transit projects. Since Beijing Metro Line 4 adopted PPP mode for the first time, 49 urban rail transit PPP projects have been carried out in China. Many state-owned holding enterprises, private enterprises, and joint ventures are attracted to participate in the form of a consortium or

non-consortium. At present, the total mileage of PPP projects has reached 1504.748 km . The total investment amount has reached CNY 893.7212.4 billion.

While promoting the development of urban rail transit projects, the PPP model also brings challenges to the project promotion due to the multiple dimensions of complexity of its practice. The multiple dimensions of complexity of PPP project practice is embodied in (1) The objective is complex. The goals and demands of the government include providing convenient rail transit public services, addressing the funding needs of local governments, and modernizing urban governance capacity. These complex targets often lead to governments rushing to sign contracts and move work forward quickly. This approach will result in insufficient preparation for the preliminary work of the project and failure to start work in time after the signing of the project contract. (2) The income source of social capital is complex. The sources of investment recovery of social capital in urban rail transit construction projects generally include four parts: passenger ticket income, value-added income generated by land primary development, financial investment and subsidies, and secondary development income. The complicated income source causes the high uncertainty of the time and scale of future income and the difficulty of income assessment. It brings difficulties to the decision making of the government and social capital. (3) Project participants are complex. Due to the huge amount of investment in urban rail transit projects, social capital is generally tendered into the project in the form of a consortium. The project participants include construction units, financial units, operation and management units, equipment electromechanical units and administrative units of various government departments. The integration of these complex subjects makes it difficult to communicate and coordinate, which puts forward higher requirements for a good communication mechanism of the project.

The above problems bring great challenges to the construction management of urban rail transit PPP projects. With the development of an urban rail transit PPP project, the problems of construction risk management are gradually exposed due to the complicated influencing factors. Therefore, it is necessary to analyze and evaluate the construction risks of urban rail transit PPP projects. According to the evaluation results, certain risk prevention and control measures can be taken to ensure the smooth development of PPP project construction and reduce the potential loss of the project.

Risk refers to the combination of the possibility of a certain dangerous event (accident or accidental event) and its consequences. However, the types of safety risks in PPP mode generally include quality risk, schedule risk, cost risk, security risk, and contract risk. These are the reasons that affect the risks in PPP mode, thus causing the occurrence of specific dangerous events in this mode, leading to the occurrence of dangerous accidents and affecting rail transit construction.

This paper proposes a construction risk assessment method based on Bayesian network (BN). First, identify and analyze the risks from quality, schedule, cost, safety, and contract. The construction risk of an urban rail transit project brought by the introduction of PPP mode is identified and its mechanism is studied. The differences between this method and other methods in this field are as follows: According to the advantages of BN in risk assessment [2], the construction risk assessment method based on BN is studied. Aiming at the uncertainty problems and complex influencing factors in PPP projects, the BN network structure is constructed and the causal relationship between each node is determined. The parameters needed by each node are obtained by questionnaire survey to calculate the initial condition probability The calculation results are corrected by leaky noisy-OR gate model. Netica software is used to calculate the probability of the final construction risk and the construction risk reasoning and sensitivity, by combining a large number of actual samples with machine learning algorithms. Finally, a practical project is taken as an example to verify the applicability and effectiveness of the above methods, and suggestions on construction risk prevention and control measures are proposed. It provides a basis for practitioners and policy makers of urban rail transit PPP projects.

The organizational structure of this article is as follows. Firstly, this paper introduces the development status of PPP projects in detail, and describes the problems existing in the safety risk management of urban rail transit projects under PPP mode. Then, the construction risks of urban rail transit PPP projects are identified, and the construction risk evaluation method based on BN is expounded. Finally, the proposed method is demonstrated by practical projects, and the application value and limitations of the proposed method are further explained.

# 2. Literature Review 

### 2.1. Research Status of Urban Rail Transit PPP Projects

At present, studies on risk sharing between public and private parties, financing risk, key success factors, and life cycle performance have been carried out in PPP projects. In the study of risk sharing between public and private parties, many scholars have constructed models using a structural equation model [3] and neural network [4] to define the risk allocation framework of public and private parties in urban rail transit PPP projects [5], and have given the risk allocation strategy and trade-off method [6]. At the same time, the actual projects in various places are taken as examples [7] to discuss the structure and factors that are conducive to the joint risk sharing between public and private parties [8]. In terms of financing risk research, from the perspective of identification, evaluation, transfer [9], or reduction [10] of risks, the sustainability and efficiency of financing influenced by land policy [11], income [12], and other factors are discussed. In the study of key success factors, the key factors of successful PPP projects in various countries are identified [13]. The roles of financial market maturity, transparency of regulatory framework, and participation of social capital [14] in PPP infrastructure projects are studied. Some scholars also improve the success rate of PPP projects from the perspective of improving the design of PPP contracts [15]. Meanwhile, life cycle performance research mainly studies the influence of key performance indicators on project success or failure [16].

### 2.2. Current Situation of PPP Project Construction Management

Many scholars have also carried out a series of studies on project construction management under PPP mode. In engineering practice, the organizational form, contract structure, and operation process of the project under the PPP model have changed, resulting in inconsistency between the project and the traditional model in construction management. Therefore, some scholars have studied the current situation and existing problems of PPP model project construction [17] and compared the similarities and differences between PPP mode and traditional mode from the aspects of quality, cost, progress, and safety [18]. In addition, scholars also have discussed the influence of different factors on PPP construction projects, including social capital construction experience, contract maturity [19], government corruption [20], contract change, general contractor, and other factors. In terms of social capital, scholars mainly study the influence of explicit control and implicit control of the government on the behavior of social capital in PPP projects and examine the trust control relationship between public and private parties under the background of PPP contracts [21]. It is concluded that minimizing the risk of social capital by transferring construction risks to users and taxpayers is shortsighted [22].

### 2.3. Status of Construction Risk

Construction risk usually involves many factors, such as construction workers risk behavior [23], 4M1E [24], and management risk [25]. In terms of construction risk identification [26], analysis [27], evaluation [28], and risk control [29], scholars have carried out abundant research and found that construction risk factors have different dimensions, such as the dimension of participants, the dimension of construction control objectives, the dimension of engineering nature, the dimension of total factors, and the dimension of project management. No matter which dimension, it represents the concrete description of the project construction risk. At the same time, construction drawing [30], meta-network [31],

Monte Carlo [32], ontology [33], Bayesian network, and other methods have been applied in construction risk identification. BIM technology [34], queuing method [35], particle swarm optimization [36], combined dynamic weighting method [37], work decomposition structure (WBS)-risk decomposition structure (RBS) risk identification matrix [38], and other methods have been applied in construction risk evaluation. There are also related studies on the safety management of urban rail transit. Bonotti R proposed the space-time analysis of light rail systems [39]. Bertolini proposed the application of railway nodes [40]. These studies have improved the overall safety of rail transit. In addition, new technical means such as digital twins, big data [41], cloud computing, artificial intelligence, and BIM technology [42] are also applied in construction risk control.

# 2.4. Research Gap 

The above studies were summarized, and the following key points were found: (1) With the gradual improvement and development of PPP project systems and legal policies around the world, the research focus has gradually been refined from the macro perspective of risk sharing between the two sides of the company, project risk research, and performance evaluation research into the micro perspective of subject behavior research, land value acquisition research, and case studies. However, there are few studies on the influence of the change of the relationship between the participating subjects caused by the change of the financing mode on the construction of urban rail transit PPP projects. (2) The PPP mode originated in developed countries, where laws, regulations, systems, and mechanisms are sound; therefore, the project is progressing smoothly. However, under China's specific national conditions, policy background, and institutional constraints, the demands of the government and market players, and specific responsibility and rights arrangements have put forward higher requirements and challenges to the project, which have an impact on the project construction. (3) In view of the construction management of engineering projects under PPP mode, scholars have carried out a certain degree of exploration; however, it has not been in urban rail transit. The PPP model has been popularized in China since 2014. In recent years, a large number of urban rail transit PPP projects have been constructed, and the problems in the construction process are gradually being exposed. Therefore, no scholars have summarized the construction risk of urban rail transit PPP projects.

## 3. Risk Identification of PPP Project Construction in Urban Rail Transit

According to the strong guiding laws, regulations, and departmental rules in the field of urban rail transit engineering in China, the key points of the survey were identified. The survey of urban rail transit PPP projects was conducted by combining offline interviews and online questionnaires. Offline research projects included Line 1, Line 4, Line 8, and Line 13 in Qingdao City, Shandong Province, Line 1 Phase I, Line 2 Phase I, and Line 3 Phase I in Xuzhou City, Jiangsu Province, and Line 4 in Kunming City, Yunnan Province. The rest of the PPP lines under construction were the objects of questionnaire survey. Based on the results of offline field survey and online questionnaire survey, the construction risks brought by the introduction of PPP mode to an urban rail transit project can be divided into five dimensions, namely, quality management risk, progress management risk, cost management risk, safety management risk, and contract management risk.

### 3.1. Quality Management Risk

### 3.1.1. Various Quality Management Modes

At present, there are three different quality management modes in urban rail transit PPP projects: (1) Rail (subway) companies perform the management responsibility of construction units. (2) The project companies perform the management responsibility of the construction unit. (3) Rail (subway) company and project company jointly fulfill the management responsibility of the construction unit. These three quality management modes have their own advantages and disadvantages. Different cities may choose quality and safety management modes according to their own construction management capabili-

ties and financial strength. The above-mentioned variable quality management modes may lead to the following problems: (1) the quality management interface between the track (subway) company and the project company is not clear. There is no clear and unified basis for the division of management responsibilities between the two sides, which has certain legal risks. (2) For newly built urban rail transit cities, it is very difficult to choose which quality management mode and how to determine and deal with the quality management interface between rail (subway) companies and project companies, which brings difficulties to project construction management. (3) Under the premise of accustomed to the previous construction procedures of urban rail transit projects, local governments and construction social capital parties gradually explore and adapt to the project construction under the PPP mode. Sometimes they may compromise each other for mutual compromise, which violates the original intention of equal cooperation, mutual benefit, and win-win of the project and also affects the construction quality of the project to a certain extent.

# 3.1.2. Variability of Subject Relations 

The Ministry of Housing and Urban-Rural Development stipulates that general engineering projects are the responsibility of five parties. However, China's urban rail transit PPP projects have varied subject relationships in practice, which can be roughly divided into two categories. One is the subject relationship under the PPP + EPC mode, and the other is the subject relationship under the PPP + construction general contracting mode. PPP + EPC mode means financing by PPP mode and contracting by EPC mode, as shown in Figures 1-3. The difference between the three lies in the different subject relations. The first is that the project company performs the responsibilities of the construction unit, and the social capital party, as the EPC contractor, performs the corresponding responsibilities of survey, design, and construction, and the supervision unit winning the bid and entering the PPP rail transit project performs the corresponding responsibilities of supervision. The second is that the government and the project company jointly fulfill the responsibility of the construction unit. The third is that the government side of the investment representative performs the responsibility of the construction unit. Similarly, PPP + construction general contracting mode is to use PPP mode for financing and construction general contracting mode for engineering contracting, as shown in Figures 4-6. The first is that the project company performs the responsibilities of the construction unit, the social capital party performs the responsibilities of the construction unit, and the survey unit, design unit, and supervision unit winning the bid to enter the PPP rail transit project perform the corresponding survey, design, and supervision responsibilities, respectively. The second is that the government and the project company jointly fulfill the responsibility of the construction unit. The third way is that the government side of the investment representative performs the responsibility of the construction unit. According to relevant laws and regulations, the subjects responsible for the construction of the five parties should bear the corresponding main responsibility in their respective fields and pay attention to the cooperation with all parties to manage the engineering quality of urban rail transit projects. However, in the PPP project of urban rail transit, the subject relationship has changed greatly compared with the traditional five-party construction responsibility subject. In the practice of undertaking quality responsibility, there may be problems such as poor performance of quality responsibility and unclear interface of quality responsibility performance, which have a certain impact on the construction quality of the project.

![img-0.jpeg](img-0.jpeg)

Figure 1. Relationship comparison 1 under PPP + EPC mode.
![img-1.jpeg](img-1.jpeg)

Figure 2. Relationship comparison 2 under PPP + EPC mode.
![img-2.jpeg](img-2.jpeg)

Figure 3. Relationship comparison 3 under PPP + EPC mode.
![img-3.jpeg](img-3.jpeg)

Figure 4. Relationship comparison 1 under PPP + general construction contracting mode.

![img-4.jpeg](img-4.jpeg)

Figure 5. Relationship comparison 2 under PPP + general construction contracting mode.
![img-5.jpeg](img-5.jpeg)

Figure 6. Relationship comparison 3 under PPP + general construction contracting mode.

# 3.2. Risk of Schedule Management 

### 3.2.1. Inadequate Construction Organization

(1) The implementation plan of the PPP project is the top-level design of the project. It is also an important basis and action guide for the work at each stage of the project. There are many deficiencies in the content of the current PPP project implementation plan, and the schedule management of urban rail transit project construction is rarely involved. (2) Some project construction general contracting department failed to adjust the schedule reasonably according to the construction situation, which affected the construction schedule and even delayed the construction period.

### 3.2.2. Inadequate Coordination

In the PPP project of urban rail transit, the construction units of the specific construction tasks of the project are mostly subsidiaries or third-class companies with independent legal status of social capital. When the construction general contracting department performs the contract management, the insufficient coordination and subcontracting ability of the construction general contracting department may affect the construction schedule of the project.

### 3.3. Cost Management Risk

### 3.3.1. Nonstandard Cost Control

The nonstandard cost control of urban rail transit PPP project is reflected in the lack of standardization of the extraction management fee of the construction general contracting department: (1) Some projects do not agree on the limit of the extraction management fee of the construction general contracting department in the contract. (2) Some members of the project construction general contracting department extract management fees as high as $17 \%$, which severely reduces the safety investment and brings hidden dangers to the construction of the project.

# 3.3.2. Difficulty in Cost Control 

There is no significant difference between the specific content of cost management of urban rail transit PPP projects and the traditional construction management mode. Compared with the traditional mode, PPP mode increases the cost management during the operation period from the tender offer of the construction enterprise to the end of the operation period, and the management time span is extended. At the same time, PPP mode should not only consider the cost control in the construction stage of the project, but should also consider the cost management in the whole project cycle from the perspective of the interests of all parties who sign the PPP agreement.

### 3.3.3. Lack of Experience in Cost Management

Project companies generally undertake high financing tasks and complex cost management tasks at the same time. Uncertainty factors in practice, such as cost changes caused by design changes, timely changes in financing dues caused by the external environment, and engineering payment problems caused by nonstandard contract signing, all put forward higher requirements for their comprehensive control ability. However, some cities that are newly constructing urban rail transit PPP projects often do not have mature experience in cost management, which also brings challenges to construction management to a certain extent.

### 3.4. Safety Management Risk

### 3.4.1. Unreasonable Safety Management Process

(1) The transfer of preliminary work was incomplete. In terms of construction procedures, the preliminary work of the project is generally completed by the track (subway) company in the project site before the signing of the PPP project cooperation agreement and the establishment of the project company. After the establishment of the project company, the track (subway) company should transfer the previously completed work to the project company. However, in project practice, most projects often have the problem of incomplete handover of preliminary work.
(2) The management of critical projects is not reasonable. In project practice, the subject of track (subway) company and project company is not clear when they perform the management responsibility of critical projects.
(3) The construction of emergency rescue system is not perfect. The division of labor between the railway (metro) company and the project company is not clear in the emergency plan drill, the establishment of training system, the budget of funds, and the allocation of materials, equipment, and teams. Part of the work cannot be effectively implemented. A reasonable workflow execution is not in place or the main body is not clear, which lays a serious security risk for engineering construction and brings certain construction risks.

### 3.4.2. The Separate Contracting of PPP Projects Leads to Unclear Division of Safety Management Responsibilities

Some urban rail transit PPP projects are divided into separate contracting A (civil engineering) and separate contracting B (post-station project). Therefore, there are two project companies and a number of construction units under its management in a project, resulting in unclear division of safety management responsibilities among different project companies.

The project is divided into pre-station and post-station projects, which brings risks to the ownership management of the site construction units and the cross-operation of the site.

According to the requirements of Quality Construction of Interim Measures for Acceptance Management of Urban Rail Transit Construction Project, the unit project acceptance, project acceptance, and completion acceptance shall be organized and implemented by the construction unit. However, for the PPP projects divided into separate contracting A and $B$, it is difficult for each project company to unify the acceptance organization work due to its own management level, which also increases the difficulty of ownership and

cross-operation management of the construction site. There is no standard basis for the transfer of the project involved in the actual operation. These situations lead to unclear division of safety management responsibilities among different project companies in the same project, which in turn affects the implementation of corresponding safety management responsibilities and brings certain risks to project construction.

# 3.4.3. Difficulty in Carrying Out Supervision Work 

Under China's national conditions, supervision units pay more attention to subordinate relationship than to contract relationship. The supervision unit is mainly assigned by the owner, resulting in the situation that the supervision unit is responsible for the construction social capital in the process of project implementation, which may cause problems such as weak management and affect the safety of project construction.

In the operation of some projects, the construction unit directly communicates and coordinates with the project company across the supervision unit. The role of the supervision unit is ignored. To sum up, the supervision unit has some difficulties in the development of safety management, which will directly or indirectly affect the safety management of the project.

### 3.4.4. The Responsibility and Authority of the Project Company and the Construction General Contractor Are Confused

There is confusion of responsibility and authority between the project company and the general contractor department. Some members of the construction social capital party serve in both the project company and the construction general contractor department. This situation may cause the following problems: (1) The person who initiates the application for the construction general contracting department and the project company person who approves the application for the construction general contracting department have a relationship, which does not conform to the specification. Therefore, there may be problems such as unqualified documents and materials through audit or incorrect implementation of approval procedures, which lays a security risk for project construction. (2) The unclear division of responsibilities between project companies and construction headquarters may lead to unclear responsibility subjects and inaccurate accountability in rail transit project construction.

### 3.5. Contract Management Risks

### 3.5.1. Risk of Merging Two Bids into One

Construction social capital has entered the PPP project construction of urban rail transit through the form of "investment and financing and construction integrated bidding", and most of them do not conduct public construction bidding. The party with construction ability and corresponding qualification in the social capital undertakes the construction general contractor task, and the specific construction task is internally assigned to its subordinate units or subsidiaries. The operation mode of "merging two bids into one bid" and "internal assignment of construction tasks" is still controversial at the legal level. In practice, there is a certain legal risk in choosing the social capital party through nonbidding method and assuming the construction task by itself.

### 3.5.2. Risks from Diverse Contractual Structures

By summarizing the contract structure, the different divisions of labor of track (subway) company and project company in the bidding management and contract signing of each participating unit are obtained. The bidding management of survey, design, and supervision units is mainly dominated by the track (subway) company. The bidding management of third-party monitoring and third-party testing units is mainly dominated by project companies. The contracts of survey and design units are also mainly signed with the track (subway) company, but most of the contracting parties of supervision units are signed with the project company. At the same time, the project company also dominates

the contract signing with third-party monitoring and third-party testing units. In short, the contract structure and organizational relationship of most projects are relatively complex, which cannot be simply summarized. There may be disunity between the bidding management party and the contract signing party. This means that in the implementation of the project, the coordination of construction management is difficult, which puts forward higher requirements for the construction management ability of the participating units. The contract structure of the project investigated is shown in Figures 7-12.
![img-6.jpeg](img-6.jpeg)

Figure 7. Chengdu Line 9.
![img-7.jpeg](img-7.jpeg)

Figure 8. Hohhot Line 1.
![img-8.jpeg](img-8.jpeg)

Figure 9. Shaoxing Line 1.

![img-9.jpeg](img-9.jpeg)

Figure 10. Tianjin Line 7.
![img-10.jpeg](img-10.jpeg)

Figure 11. Xuzhou Line 3.
![img-11.jpeg](img-11.jpeg)

Figure 12. Kunming Line 4.

# 3.5.3. Risk of Diversity of Roles of Contract Subjects 

1. Diversity of Government Roles

The government is both "referee" and "athlete". The identity of "referee" is a kind of public power granted by law to the government in PPP projects. It is a kind of administrative supervision relationship with social investors. The identity of "athlete" means that the investment representative of the government and the social capital persons are the shareholders of the project company together and there is an equal civil subject relationship between the government and the social investors. If the role of the government is not clear, there may be problems such as the scope of government intervention and the size of power in practical operation, which brings certain risks to the construction management of the project.
2. The Role of Social Capital in Construction Is Diverse

The social capital side of construction also plays the dual role of "referee" and "athlete". The identity of "referee" means that the social capital party of construction participates in the project construction management as a member of the project company. The identity of "athlete" refers to the social capital party of construction participating in the concrete construction of the project as the construction unit. The role of construction social capital is not clear. In the actual operation of the project, there may be problems such as insufficient management of the construction general contractor, weak management methods and complex relationships due to relevant interests. It also affects the project construction management to some extent.

## 4. Construction Risk Assessment Method of Urban Rail Transit PPP Project Based on BN

### 4.1. Basic Principles of Bayesian Network Model

Bayesian network (BN), also known as directed acyclic graphical model (DAG), was first proposed by Judea Pearl in 1985. The causal relationship between random variables is represented by a directed graph and quantified by conditional probability. Generally speaking, the Bayesian network satisfies the following four conditions:
(1) There is a variable set $V=\left\{v_{i}\right\}, i=1, \cdots, n$, and the set E with directed edges between corresponding nodes to the variable;
(2) Each variable takes a finite discrete value;
(3) A directed acyclic graph $G=(V, A)$ is constituted by the nodes corresponding to variables and the directed edges between nodes;
(4) For each node $v_{i}$ and its parent node set $\Pi_{i}$, there is a conditional probability table (CPT for short) $p\left(v_{i} \mid \pi_{i}, G\right)$, which is as follows:

$$
p\left(v_{1}, \ldots, v_{n}\right)=\prod_{i=1}^{n} p\left(v_{i} \mid \pi_{i}, G\right)
$$

It is concluded from the above definition that the Bayesian network is composed of Bayesian network structure and conditional probability distribution table. The network structure consists of several nodes and directed arcs. Nodes represent random variables, and the directed arc from the parent node to the child node represents the relationship between nodes. The conditional probability distribution table is that each node in the network corresponds to a CPT to represent the influence of its parent node on the node. When a node in the network has no parent node, the conditional probability of the node is the prior probability of the node. When the Bayesian network is represented by topological structure, nodes with causal or nonconditional independence are connected by arrows, pointing to the result from the cause and generating a conditional probability value. Using the Bayesian model to solve practical problems is called Bayesian network reasoning, which can be divided into causal reasoning and diagnostic reasoning. Causal reasoning is from cause to result, reflecting the expected support of parent node to child node in the network.

Diagnostic reasoning is from result to reason, reflecting the review support of child nodes to parent nodes.

# 4.2. Build Bayesian Network 

### 4.2.1. Determine the Bayesian Network Structure

Firstly, through risk identification and analysis, the specific project construction risk factors are listed as random variables in the Bayesian network. Then, each node and the causal relationship between nodes are determined, and the related nodes are connected with each other by arrows to form a network structure. Specifically, various forms such as head-to-head, tail-to-tail, and head-to-tail can be formed, as shown in Figures 13-15.
![img-12.jpeg](img-12.jpeg)

Figure 13. Head-to-head.
![img-13.jpeg](img-13.jpeg)

Figure 14. Tail-to-tail.
![img-14.jpeg](img-14.jpeg)

Figure 15. Head-to-tail.

### 4.2.2. Construction of Conditional Probability Table

Firstly, the relevant information of each node should be defined, such as whether the construction risk factors are the parent node or child node and their respective values. Then, the conditional probability table is estimated. For nodes without parent nodes, the prior probability is the conditional probability and other nodes need to be calculated by formula. The nodes used in this study are N-type nodes, meaning each node has two states of YES and NO, respectively, indicating that the corresponding construction risk events occur and do not occur.

### 4.2.3. Determination of Bayesian Network Parameters

If the value of the random variable is observable, the conditional probability table can be obtained directly. If the value of random variable cannot be obtained directly, the conditional probability table needs to be solved by chain rule and causality.

### 4.3. Construction Risk Assessment Calculation Based on Bayesian Network

### 4.3.1. Classification Standard of Construction Risk Probability

In order to make a relatively accurate evaluation of construction risk, it is necessary to establish a corresponding relationship between the possibility level and probability of risk occurrence, as shown in Table 1. After obtaining the risk possibility through Bayesian network, the specific risk level can be determined.

Table 1. Risk occurrence probability grade standard.


# 4.3.2. Determination of Network Parameters for Construction Risk Assessment 

By issuing questionnaires to urban rail transit PPP project managers and experts, the node parameters needed in Bayesian network are obtained. The prior probability and conditional probability were obtained, which lays the foundation for subsequent calculation and reasoning using Bayesian network. The form of questionnaire is shown in Tables 2 and 3, taking the head-to-head form as an example.

Table 2. Prior probability of root node.


Table 3. Conditional probability of non-root node.


After obtaining the above parameters, each probability value is assigned to the Bayesian network to calculate the probability of construction risk events. At the same time, the accuracy and rationality of Bayesian network calculation results can be verified according to the experience of experts.

### 4.3.3. Correction of CPT Based on Leaky Noisy-OR Gate Model

The occurrence of child node events may not all be caused by the occurrence of parent node events, but may also be caused by some unpredictable or unknown factors, so not every child node can find out all the parent nodes that affect its occurrence. The possibility is that the probability of the parent node is 0 , but the probability of the child node is not 0 . In this case, the leaky noisy-OR gate model can be used to determine the conditional probability table. In the leaky noisy-OR gate model, node Y is not only affected by parent nodes $X_{1}, X_{2}, \ldots, X_{n}$, but is also affected by some unknown factors. All unknown factors are combined into one factor, which is denoted as $X_{L}$, as shown in Figure 16. Its connection probability is denoted as $P_{L}$.
![img-15.jpeg](img-15.jpeg)

Figure 16. Bayesian model structure.
Suppose that the child node Y has two parent nodes, $X_{L}$ and $X_{\text {all }}$. $X_{\text {all }}$ is the sum of other factors except $X_{L} P_{a l l}$ and $P_{i}$ are their connection probabilities, respectively. Then, the calculation formula of $P_{i}$ is shown in Equation (2).

$$
P_{i}=\frac{P\left(Y \mid X_{L}\right)-P(Y \mid \bar{X})}{1-P(Y \mid \bar{X})}
$$

Let the connection probability of all the parent nodes of node Y be $P_{1}, \ldots, P_{i}, \ldots, P_{n}$, and then combine with the uncertain factor $X_{L}$, and let the connection probability be $P_{L}$, then the conditional probability formula of node Y is as follows:

$$
P_{i}(Y)=1-\left(1-P_{L}\right) \prod_{i: X_{i} \in X_{p}}\left(1-P_{i}\right)
$$

# 4.3.4. Construction Risk Calculation Based on Netica Software 

(1) Construction risk probability calculation. After determining the conditional probability table of each node, the conditional probability values of intermediate nodes and top nodes can be calculated. The topological graph is drawn in Netica software. Then, each node and its conditional probability table obtained by the above steps are input into the software to automatically solve the probability value of the final construction risk.
(2) Construction risk reasoning calculation. Causal reasoning and diagnostic reasoning can be carried out on the basis of construction risk probability calculation. Causal reasoning is to lock the occurrence probability of a root node of Bayesian network in Netica software, so that it shows the occurrence state of $100 \%$. At this point, the probability change of the child node can be automatically obtained. Similarly, diagnostic reasoning is that the probability of locking child nodes in Netica software is $100 \%$, and the probability of each root node can also be automatically solved.
(3) Construction sensitivity calculation. In Netica software, through a series of operations, such as constructing topology graph $\rightarrow$ establishing causality $\rightarrow$ determining conditional probability input $\rightarrow$ selecting query node $\rightarrow$ sensitivity analysis, the mutual information index of nodes related to the node can be obtained.

## 5. Engineering Case Study

### 5.1. Project Overview

Xuzhou Line 3 Phase I Project has a total length of 18.13 km . The whole line has 16 stations, 15 main sections, 1 depot, and 1 access section. The project operates in PPP mode. The total investment of the project is CNY 13.526 billion, of which the capital of CNY 3.6 accounts for about $27 \%$ of the total investment. The part other than the capital of CNY 9.926 billion will be solved through the bank loan led by China Development Bank. In the capital composition, China Construction Federation, Rail Company, China Government Enterprise Fund, and Chang' an Trust invested CNY 1.6 billion, CNY 600 million, CNY 1 billion, and CNY 400 million, respectively. Xuzhou Line 3 Phase I Project is shown in Figure 17.

Xuzhou Line 3 Phase I Project adopts the combination of social capital investment and financing and construction general contracting as the bidding method of one bid, which is introduced into China Construction Federation. China Construction Federation and Rail Corporation jointly funded the establishment of Xuzhou Line 3 Rail Transit Investment Co., Ltd. (Project Company). As the project owner of the design, construction, and postmaintenance module, the project company is responsible for project investment, construction, and maintenance and has signed the general construction contract agreement with China Construction Co., Ltd. In addition, Xuzhou Line 3 Rail Transit Investment Co., Ltd. as the owner entrusted the track company to perform construction management duties and signed the project entrusted management contract with the track company. At the same time, according to the entrustment management contract, other participating construction units such as survey, design, supervision, third-party inspection, and thirdparty monitoring are determined by the track company through public tenders (party A of the contract is still the project company) and managed by the track company.

![img-16.jpeg](img-16.jpeg)

Figure 17. Xuzhou Line 3 Phase I Project.

# 5.2. Probability Analysis of Construction Risk Based on Bayesian Network 

### 5.2.1. Construction of Bayesian Network

The construction risk factors of urban rail transit projects under the PPP mode given in the third chapter are based on the summary of most PPP projects of urban rail transit in China. The construction risk factors summarized do not exist in every project. In the application of specific projects, it should be judged according to the actual situation. Through the communication with the staff of the relevant units of the project, such as the track company, the project company, the construction general contracting department, and the supervision unit, the construction risk factors of the PPP project of Xuzhou Line 3 were obtained, which were then transformed into the evaluation index system and marked, as shown in Table 4. It should be noted that the following risk factors are not all the risk factors in the project implementation process, but the main risk factors.

Table 4. Evaluation index system of PPP project construction risk factors for Xuzhou Line 3.


In addition, the relative independence between various factors has been considered in the division of construction risk factors. Therefore, the Bayesian network topology of

construction risk can be obtained from the evaluation index system table. The state of the event is recorded as 1 , and the state of the non-occurrence is recorded as 0 . According to the permutation and combination rules, each node will produce 2'n conditional probability situations. n is the number of child nodes at the node, and the node will produce $2^{\prime} 5=32$ conditional probability situations at most. In order to facilitate the calculation, two auxiliary nodes, $X_{1}$ and $X_{2}$, were introduced to form a new topology. As shown in Figure 18.
![img-17.jpeg](img-17.jpeg)

Figure 18. Improved construction risk Bayesian network.

# 5.2.2. Obtain Original Data 

With the help of the questionnaire designed in the previous section, the expert scoring data were collected. Through statistical analysis, the probability table of initial conditions was obtained.

### 5.2.3. Modified Conditional Probability Table Based on Leaky Noisy-OR Gate Model

The conditional probability table was modified based on leaky noisy-OR gate model. Firstly, the connection probability of the missing factors of each node was set as $P_{L}=0.05$. The connection probabilities of all parent nodes of child node $R$ were calculated by Formula (1): $P\left(Q_{1}\right)=0.51, P\left(Q_{2}\right)=0.20, P\left(Q_{3}\right)=0.09, P\left(P_{1}\right)=0.37, P\left(P_{2}\right)=0.17$, $P\left(P_{3}\right)=0.15, P\left(C_{1}\right)=0.13, P\left(C_{2}\right)=0.32, P\left(C_{3}\right)=0.44, P\left(S_{1}\right)=0.52, P\left(S_{2}\right)=0.26$, $P\left(S_{3}\right)=0.23, P\left(B_{1}\right)=0.31, P\left(B_{2}\right)=0.25, P\left(B_{3}\right)=0.30, P(Q)=0.49, P(P)=0.17$, $P(C)=0.26, P(S)=0.53, P(B)=0.39, P\left(X_{1}\right)=0.63, P\left(X_{2}\right)=0.74$. In addition, the supposed connection probability of each node due to missing factors was $P(L)=0.05$. Then, the conditional probability table of node $Q$ was calculated by formula (2), as shown in Table 5. Similarly, the values of conditional probability tables of each node were obtained.

Table 5. Value of conditional probability table for node $Q$.


### 5.2.4. Calculation of Construction Risk Probability Based on Netica Software

The Bayesian network topology diagram was built based on Netica software, and each node was assigned according to the above calculation results. The topology diagram is shown in Figure 19. It can be seen that the final construction risk level of this project is $39 \%$ when the risk probability of each underlying node is given.

![img-18.jpeg](img-18.jpeg)

Figure 19. Bayesian network topology.

# 5.3. Construction Risk Reasoning Based on Bayesian Network 

### 5.3.1. Reverse Risk Diagnosis

If the probability level of the construction risk of the project is $100 \%$, different values of the intermediate node and the underlying node can be obtained. The calculation results are shown in Figure 20. The probability levels of quality risk, schedule risk, cost risk, safety risk, and contract risk are $28.8 \%, 28.5 \%, 38.2 \%, 52 \%$, and $38.1 \%$, respectively. $P\left(S_{1}\right)=51 \%$ is the highest risk level, so it is necessary to focus on the construction risks caused by the nonstandard safety management process.
![img-19.jpeg](img-19.jpeg)

Figure 20. Reverse risk diagnosis.

### 5.3.2. Positive Causal Reasoning

If a risk event occurs, such as $P\left(Q_{1}\right)=100 \%$, the probability of quality risk increases from $20.9 \%$ to $56 \%$ and the overall probability of construction risk increases from $39 \%$ to $45.5 \%$, as shown in Figure 21. In addition, the probability of construction risk can be predicted by setting different event combinations. If three quality risk events occur, the probability of quality risk increases from $20.9 \%$ to $66 \%$ and the overall construction risk level also increases from $39 \%$ to $47.4 \%$, as shown in Figure 22.

![img-20.jpeg](img-20.jpeg)

Figure 21. Positive causal reasoning 1.
![img-21.jpeg](img-21.jpeg)

Figure 22. Positive causal reasoning 2.

# 5.4. Sensitivity Analysis of Construction Risk Based on Bayesian Network 

The sensitivity analysis of each node was carried out by Netica software. Taking $R$ node as an example, the ranking of the influence degree of $R$ node by the changes of each node can be obtained as follows: $X_{2}>X_{1}>S>B>Q>S_{1}>C>Q_{1}>P>S_{3}>$ $B_{3}>S_{2}>B_{1}>C_{3}>B_{2}>Q_{2}>C_{2}>P_{1}>Q_{3}>P_{2}>C_{1}>P_{3}$. It can be seen that construction risk is more sensitive to safety management risk, contract management risk, and quality management risk. When detailed to the secondary indicators, construction risk is more sensitive to the nonstandard safety management process, the untimely repair of quality defects, and the weak safety awareness of construction personnel. Therefore, in the process of project construction, the influence of the above project risk factors on construction risks should be focused. Similarly, the order of the influence degree of nodes $Q, P$, and $B$ on the change of each child node is as follows: Node $Q: Q_{1}>Q_{2}>Q_{3}$; Node $P: P_{1}>P_{2}>P_{3}$; Node $C: C_{3}>C_{2}>C_{1}$; Node $S: S_{1}>S_{3}>S_{2}$; Node $B: B_{3}>B_{2}>B_{1}$. Quality risk is sensitive to the risk of not timely repair of quality defects. Schedule risk is sensitive to inadequate construction organization. Cost risk is sensitive to the lack of cost management experience. Safety risk is sensitive to the nonstandardized risk of relevant safety management processes. Contract risk is sensitive to the risk of lack of dynamic adjustment mechanism.

# 5.5. Construction Risk Prevention and Control Measures 

Based on Bayesian network method, the construction risk probability calculation, construction risk reasoning, sensitivity analysis, and risk loss evaluation of PPP project of Xuzhou Line 3 Phase I Project were carried out. The following conclusions are obtained: (1) The overall risk probability level of the project is $39 \%$, which is level III risk. According to this, the construction risk is likely to occur. (2) Through positive reasoning, if a risk factor occurs, the overall risk level of the project will be significantly improved. By reverse diagnosis, if the construction risk of the project must occur, the possibility of safety risk and cost risk is larger. (3) Through sensitivity analysis, the overall construction risk of the project is more sensitive to safety management risk, contract management risk, and quality management risk.

Based on the above calculation and results analysis, the risk factors that should be focused on for prevention and control of this project were found, and the following measures and suggestions are put forward: (1) Each participating unit should do a good job of organization and coordination to ensure that the relevant safety management processes are reasonable. For the temporary absence of certain laws and regulations, the relevant units should take the initiative to strengthen communication and avoid the phenomenon of prevarication of responsibility. (2) It is necessary to focus on strengthening construction management, such as timely repair of quality defects, qualified safety training of construction personnel, repeated demonstration of construction technology, and orderly management of construction site. All possible risk factors should be prevented and controlled. (3) The management experience of urban rail transit PPP projects should be learned, especially the cost management experience. From the perspective of the whole life cycle, it is necessary to manage the cost and strengthen the construction of financing capacity and the accumulation of cost management experience to prevent problems such as insufficient engineering funds from affecting the construction progress.

## 6. Discussion

Previous work has proved that the system of the PPP projects all over the world is gradually improving and development of the legal policy and research focus from the macroscopic angle of risk-sharing research, project risk, and performance evaluation adds to the body of the microcosmic angle behavior research, land value research, case studies, etc. However, few studies have deeply explored the influence of the changes in the relationship between construction subjects brought about by the changes in financing methods on the construction of urban rail transit PPP projects. The PPP model originated in developed countries, with sound laws and regulations and a sound system and mechanism, meaning projects are also proceeding smoothly. However, under the specific national conditions of China, the policy background and institutional constraints, the demands of the government and market subjects, and the specific responsibility and right arrangement all put forward higher requirements and challenges to the project, which have an impact on the project construction. For the construction management of projects under PPP mode, some scholars have carried out a certain degree of research; however, it has not yet involved the field of urban rail transit. The PPP model has been promoted in China since 2014. In recent years, a large number of urban rail transit PPP projects have been constructed, and the problems in the construction process are gradually exposed. Therefore, no scholars have conducted a summary study on construction risks of urban rail transit PPP projects. These limitations are worth noting.

However, the method used in this study is really an innovative exploration of PPP mode in the field of rail transit. Since the introduction of PPP mode into China in 2014, the research and application in the field of China PPP rail transit have been increased. This study studies the safety risks of PPP projects in rail transit from the perspective of innovation in China. A security risk evaluation method based on Bayesian network is proposed to identify and analyze risks in quality, schedule, cost, safety, and contract. The construction risk of an urban rail transit project brought by the introduction of PPP mode

is identified, and its mechanism is studied. Different from other studies using Bayesian networks in other fields, this method is the first study on risk research of Bayesian networks in the PPP rail transit field. It can provide experience for risk management in China's PPP rail transit field.

At the same time, based on the advantages of BN in risk evaluation, the construction risk evaluation method based on BN is studied. In view of the uncertainty and complex influencing factors in PPP projects, the BN network architecture is constructed and the causal relationship between each node is determined.

This study calculates the probability of initial conditions by obtaining the parameters required by each node through questionnaire survey and correcting the leaky noisy-OR gate model. Netica software is used to calculate the final probability of construction risk occurrence and carry out inference calculation and sensitivity calculation of construction risk. Compared with other research methods, the calculation results of the model are updated. This makes the calculation of risk more accurate.

This study combines a large number of practical rail transit projects in China. It has adaptability and particularity. Through this research method, the probability of risk occurrence can be obtained, and the inferential calculation and sensitivity calculation of construction risk can be carried out. It has made important contributions to the risk control and improvement of China's rail transit.

This study also has relevance and harmony with the current risk management field of rail transit in China. Although it is aimed at the research and application under the background of rail transit field, the research method in this paper can also be applied to other project risk studies.

In obtaining the original conditional probability table, this study still relies on expert scoring and lacks analysis and evaluation of the global construction risk. In addition, how to utilize artificial intelligence, digital twin, and other methods and technologies to integrate with construction risk assessment also needs further exploration.

# 7. Conclusions and Prospect 

Taking the PPP project of urban rail transit in China as the object, this paper studies and summarizes the construction risk factors and action mechanism of the PPP project of urban rail transit on the premise of online and offline research. Based on the Bayesian network method, the construction risk assessment method is constructed. Finally, an example of Xuzhou Line 3 PPP project is given to verify the effectiveness and applicability of the above method. Through the above research, the following conclusions are obtained:

Summary of the survey: This research was completed with the support of China Urban Rail Transit Association Safety Special Committee. Cooperation units include Beijing Rail Transit Construction Management Co., Ltd., Shenzhen Metro Group Co., Ltd., China Railway Co., Ltd., and other 15 companies. The online survey was sent out to companies via web links. A total of 3000 effective feedback questionnaires were received. The offline research was conducted by the author visiting many rail transit units in China. The results of the survey amounted to 600 copies. Therefore, the research results are persuasive and authoritative.

The construction risk of urban rail transit project under PPP mode can be divided into five dimensions, and secondary risk factors can be obtained through refinement. The mechanism can be further analyzed from the perspective of project practice and laws and regulations, which can provide reference for urban rail transit PPP projects.

Bayesian networks have great advantages for solving complex risks caused by multiple factors. The connections between nodes in the Bayesian network can also be well used to represent the construction risk factors and the causality between them. In order to express the influence of unknown factors on construction risk, the leaky noisy-OR gate model can be introduced to modify the conditional probability table. Then, construction risk calculation, risk reasoning, and sensitivity analysis can be carried out based on Netica software to form a more comprehensive description of construction risk from three different dimensions.

Taking the first-stage PPP project of Xuzhou Line 3 as an example, 15 possible construction risk factors are listed. The above method was used to calculate the overall risk level of the project, deduce the influence of different risk factors on the overall risk, find out the most significant risk factors affected by the overall risk, and obtain the risk factors with high sensitivity and the risk factors with serious losses to the project. According to the calculation results, the risk prevention and control measures are put forward.

Author Contributions: Data curation: A.L.; Formal analysis, Y.J.; Investigation: Y.J.; Methodology, Z.L. and Y.J.; Resources: Z.L.; Supervision: Z.L. and X.L.; Writing-original draft: Y.J. and A.L.; Writing-review \& editing: Z.L. and X.L. All authors have read and agreed to the published version of the manuscript.

Funding: This research was funded by Beijing Science and Technology Plan Fund under Grant, grant number Z181100009018001.

Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: The data used to support the findings of this study are available from the corresponding author upon request.

Conflicts of Interest: The authors declare that they have no conflict of interest.
