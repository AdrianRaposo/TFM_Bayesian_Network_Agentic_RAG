# Article 

## Effects of Preparedness on Successful Emergency Response to Ship Accident Pollution Using a Bayesian Network

Yini Zhu ${ }^{1,2,3}$, Wenqing Ma ${ }^{1,2,3}$ (D), Hongxiang Feng ${ }^{1,2,3}$ (D), Guiyun Liu ${ }^{1,2,3}$ and Pengjun Zheng ${ }^{1,2,3, *}$


#### Abstract

check for updates Citation: Zhu, Y.; Ma, W.; Feng, H.; Liu, G.; Zheng, P. Effects of Preparedness on Successful Emergency Response to Ship Accident Pollution Using a Bayesian Network. J. Mar. Sci. Eng. 2022, 10, 179. https://doi.org/10.3390/ jmse10020179

Academic Editor: Alberto Ribotti

Received: 28 December 2021
Accepted: 23 January 2022
Published: 28 January 2022


Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## (0)

Copyright: (c) 2022 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 Faculty of Maritime and Transportation, Ningbo University, Ningbo 315832, China; 1911084009@nbu.edu.cn (Y.Z.); 1911084005@nbu.edu.cn (W.M.); fenghongxiang@nbu.edu.cn (H.F.); liuguiyun@nbu.edu.cn (G.L.)
2 National Traffic Management Engineering \& Technology Research Centre Ningbo, Ningbo University, Ningbo 315832, China
3 Jiangsu Province Collaborative Innovation Center for Modern Urban Traffic Technologies, Southeast University, Nanjing 210096, China

* Correspondence: zhengpengjun@nbu.edu.cn


#### Abstract

With the rapid development of international trade and the fast growth of port freight volumes, the risk of ship pollution in marine areas has significantly increased. Frequent ship pollution accidents seriously endanger marine ecosystems and are extremely unfavorable to economic development and marine environmental protection. In this study, we investigate the results of emergency responses after ship pollution accidents and analyze the factors affecting a successful emergency response. A Bayesian network model of the emergency response results of ship pollution is established, and the emergency response results of ship pollution accidents in the example of Zhoushan Port are analyzed. Based on the analysis, suggestions for strengthening the emergency preparedness of Zhoushan Port are proposed. We believe that the results of this are beneficial for improving ship pollution risk management and decision making, and that they have practical significance for marine environmental protection.


Keywords: ship pollution; emergency response; Bayesian network; Zhoushan Port

## 1. Introduction

Accidental spills or intentional discharge of oily wastes into the sea can lead to marine ship pollution. Ship accidents such as collisions, groundings, and explosions are the main causes of large-scale oil and chemical spills. Over the past decade, the number of pollution incidents caused by ship accidents has gradually decreased as stricter regulations for maritime transport safety have been established [1]. Although large pollution incidents are rare, they account for the majority of the pollutants that have entered the marine environment over the past several years. For example, in January 2018, more than 110,000 tons of condensate oil and nearly 2000 tons of fuel oil leaked into the sea from the Sanchi tanker accident, a serious collision in the East China Sea [2]. The emergency response to the oil spill at sea lasted for eight months and consumed enormous labor, material, and financial resources. Ship pollution not only harms human health but also has an incalculable impact on marine ecosystems and coastal economies, such as tourism and shipping. Thus, proper emergency preparedness must be undertaken to protect the marine environment from serious oil and chemical spill incidents.

In an emergency response to ship accident pollution, the relevant management takes reasonable emergency actions as soon as possible to control the pollution to the greatest extent possible, recover as much of the pollutants as possible, and reduce the harm of ship accident pollution to the marine environment. Successful emergency responses to ship pollution accidents are affected by emergency preparedness and the environment, i.e., time urgency, resource constraints, and environmental constraints. Emergency preparedness is

mainly reflected in related responses and response times. Emergency response capacity refers to whether disaster reserve resources, such as emergency vessels, emergency personnel, and total emergency resources, can meet the critical incident needs. Timeliness and adequacy of the emergency response are particularly important. Therefore, it is essential to identify and analyze the factors influencing emergency responses to ship accident pollution and identify the most important influencing factors to prevent failure in such responses. A model should then be established for evaluating the effect of preparedness on a successful response. The results can engender guidance for improving the emergency response capability.

The remainder of this paper is organized as follows. Section 2 reviews the relevant literature. Section 3 introduces the methods used in this study, analyzes the influencing factors of an emergency response, and establishes a Bayesian network model. In Section 4, we consider the Zhoushan port as an example to evaluate emergency response capability. Finally, in Section 5, conclusions are presented.

# 2. Literature Review 

For many years, ship pollution accidents have prompted the development of a series of international conventions undertaken by coastal countries and the IMO [3]. Considerable research has been conducted to evaluate emergency preparedness [4]. Chen Q [5] used AHP and a fuzzy comprehensive evaluation method to evaluate the emergency capacity of a port in terms of the environment, equipment, ship status, and human factors. Chen X [6] evaluated the emergency capacity of Dalian New Port using four factors: the environment, equipment allocation, personnel quality, and management status. Wang et al. [7] established models for different organizations in emergency responses to ship oil spills using a Bayesian network, analyzed the parameters affecting the reliability of the entire rescue organization system, and provided a reliability formula for the system. Cao [8] proposed an emergency response capacity evaluation index system for shipborne hazardous chemical pollution accidents, established a risk-based emergency energy evaluation model, and combined accident risk and emergency response capacity, thereby providing a basis for quantitative comparison of a wind barrier and the emergency response capacity. Chen [9] evaluated the emergency capacity of ship pollution in the northern part of Hangzhou Bay by using a fuzzy comprehensive evaluation method. The author also proposed improvement countermeasures in four aspects: daily construction work, emergency guarantee, emergency response capacity, and emergency rescue capacity. Zhang [10] constructed an evaluation index system of oil spill emergency capability in Shanghai Seas and used AHP, the entropy method, and game theory to assign weights to the combination of index systems. Su et al. [11] systematically and comprehensively analyzed the factors affecting emergency response ability from the entire process of sudden water pollution accidents. They established an emergency capability evaluation index system model for water pollution accidents. They also discussed the relationships among various factors and the order of each factor's effect.

Many studies have evaluated emergency capacity in ports, predominantly using traditional risk analysis approaches (such as FSA, ET, FT, and AHP [12,13,14,15]) to evaluate the environment, emergency reserve capacity, emergency response capacity, and emergency early warning capacity, and to ultimately obtain the emergency capacity evaluation results. Although it is widely used, the traditional risk analysis approach has some deficiencies, such as an inadequate ability to estimate the probability of emergency response results of ship pollution accidents and a lack of fusing diverse qualitative and quantitative data [16]. Therefore, a Bayesian network-based analytical model is proposed herein to analyze the emergency response based on the identification of influential factors that can assist in actively responding to ship pollution accidents, improving the emergency ability of the port, and protecting the marine environment.

# 3. Methods 

### 3.1. Bayesian Networks

A Bayesian network (also known as a belief or decision network) is a probabilistic graphical model that represents a group of variables and their conditional dependencies via a directed acyclic graph (DAG). Bayesian networks are well suited to handling events that have occurred and predicting the likelihood that one of several known causes is a contributing factor. The expression and reasoning of Bayesian network inference models are based on graph theory and probability theory, constituting a collection of DAGs and conditional probability tables (CPTs).

Let $G=(V, E)$ represent a $B N$, where $V$ represents the set of nodes in the $B N$ and $E$ represents the set of directed edges. Nodes represent random variables in the model and each node represents an event (variable). Directed edges indicate the interrelationship between nodes; that is, the parent node to the child node, the root node without the parent node, the leaf node without the child node, and the intermediate node with both the child node and the parent node. Accordingly, each node is affected by its parent node; that is, the parent node represents the cause, and the child node represents the result. The joint probability assignment is expressed as Equation (1):

$$
P\left(X_{1}, X_{2}, \ldots, X_{n}\right)=\prod_{i=1}^{n} P\left(X_{i} \mid P a\left(X_{i}\right)\right)
$$

where $P a\left(X_{i}\right)$ denotes the parent node of $X_{i}$ and $P\left(X_{i} \mid P a\left(X_{i}\right)\right)$ denotes the conditional probability distribution of $X_{i}$.

BN combines the DAG and probability theory to model uncertain domains. Therefore, Bayesian networks are suitable for the expression, analysis, and diagnosis of the uncertainty of probabilistic events. They are used for multi-attribute decision-making problems where multiple influencing factors are interdependent, and reasoning can be conducted in the case of incomplete and uncertain information. The modeling and analysis of the problem using a Bayesian network are mainly divided into three parts: the selection of nodes, determination of the topology structure, and determination of the CPT between nodes. Node selection is based on the analysis of various influencing factors and value domains. The topology is determined based on an analysis of the logical relationships between the obtained nodes. On this basis, the conditional probability between the child node and parent node can be determined according to historical data, actual research data, and expert knowledge.

Bayesian networks need to determine the a priori and posterior probabilities, which can be obtained by summarizing historical data and expert investigations of the probabilities of the event occurrence. Posterior probabilities can be obtained based on prior probabilities, and the calculation formula is built based on Bayes' formula. The corresponding posterior probabilities can be obtained using the prior and conditional probabilities. The formula is shown as Equation (2).

$$
\mathrm{P}(\mathrm{~A} \mid \mathrm{B})=\frac{p(B \mid A) \mathrm{P}(\mathrm{~A})}{\mathrm{P}(\mathrm{~B})}
$$

where $\mathrm{P}(\mathrm{A} \mid \mathrm{B})$ is the a posterior probability, which is used to describe the probability that event A will occur when event B occurs, and $\mathrm{P}(\mathrm{A})$ refers to the prior probability of event A .

### 3.2. Influencing Factors of Emergency Response

The identification and analysis of factors influencing ship pollution emergency response are the basis for determining the topology of Bayesian networks and obtaining observational data and model parameters. Ship pollution emergency response involves complex system engineering, and the main influencing factors include the port environment, emergency response time, and emergency response capacity [17-22].

The environment refers to marine weather, hydrological conditions, and ecologically sensitive areas in the port. In the case of strong winds, heavy waves, and low visibility, the

emergency response will be more difficult to execute, and the probability of an emergency response failure may increase. The existence and distribution of ecologically sensitive areas in the port will also affect the failure rate of the emergency response.

The emergency response time is the time elapsed between the accident and the start of emergency actions. The factors that affect the emergency response time for ship pollution are emergency resource allocation, emergency communication, accident monitoring, and emergency drills. The coverage of monitoring systems, such as ship, aviation, and shore monitoring, as well as the integrity of the construction of inter-ship and ship-to-shore communication modes, will affect the transmission speed of accident information. The distribution of equipment and materials affects the scope of the material dispatching. In addition, the number of emergency trainings at ordinary times affects the response speed of the emergency personnel. These factors affect the speed of emergency time and have a certain impact on the results of the emergency response.

Emergency response capacity refers to the capabilities and effects that can be achieved by using emergency resources after the occurrence of pollution accidents, including emergency vessels, the total amount of emergency resources, the equipment status, and emergency personnel. The total amount of resources equipped in the port and the number of emergency ships and emergency personnel determine the scope of the sea area in which the port can deal with pollution accidents. The efficiency and performance of facilities and equipment will affect a port's ability to handle sudden ship pollution incidents.

# 3.3. Bayesian Network Model for Ship Pollution Emergency Response 

Once a ship pollution accident occurs, the property loss and pollution in the marine environment are immeasurable. After the accident, pollutants can be recovered as much as possible in the shortest time to minimize damage to the ocean. Emergency response to ship pollution is often affected by many factors. In addition to the factors mentioned earlier, the first-level influencing factors of ship pollution emergency response are divided into three categories, and the second-level influencing factors are divided into 12 categories. A description of these variables is provided in Table 1.

Table 1. Bayesian network node for ship pollution emergency response.


Based on the input variables in Table 1, the Bayesian network topology was constructed, as shown in Figure 1. The network is composed of 16 nodes and several directed line segments. The root nodes are wind, wave, visibility, eco-environmental sensitivity,

emergency resource allocation, emergency drills, accident monitoring, emergency communications, emergency personnel, emergency vessels, and total emergency resources and equipment status. The intermediate nodes are environment, emergency response time, and emergency response capacity. A leaf node is an emergency response to ship pollution.
![img-0.jpeg](img-0.jpeg)

Figure 1. Bayesian network model for ship pollution emergency response.

# 4. Case Study 

Zhoushan Port was the port used in this research as the case study. It is located in the Yangtze River Delta and the eastern coastal hub of China. It is backed by large and medium-sized cities, such as Shanghai, Hangzhou, and Ningbo. This is an important node in the comprehensive transportation network of the Yangtze River Delta. Zhoushan Port is composed of many port areas, with more than 620 production berths, including nearly 170 large-scale berths of more than 10,000 tons and more than 100 large and extra-large deep-water berths above 50,000 tons. This represents the largest number of super-large ships in China. It is considered one of the rarest deep-water ports worldwide. In addition to its excellent geographical location, coastline resources, and terminal depth, Zhoushan Port has a preferential bonded port policy and free trade zone policy, which fosters significant future development potential. Therefore, Zhoushan Port is employed as an example to illustrate how to apply the proposed decision support model to improve its emergency response capability and ensure the marine ecological health and regional economy of the East China Sea.

### 4.1. Estimate of the Probability of Successful Ship Pollution Emergency Response

The Bayesian network model can handle both continuous and discrete variables. Because the nodes of the ship pollution emergency response model have obvious discrete characteristics, discrete variables are used as the model input forms. First, a reasonable approach is required to discretize the collected data. For example, the wind, wave, and visibility states are defined by the number of days of strong winds, waves, and fog that occur at Zhoushan Port each year. These data are obtained from the government's annual work reports. The eco-environmental sensitivity of Zhoushan Port is defined according to the distribution of sensitive areas in the port, which can be obtained through the Zhoushan planning documents. The total emergency resources, equipment status, emergency personnel, emergency vessels, etc., can be defined by investigating the current allocation of emergency preparedness in Zhoushan Port and by combining the actual scenarios of planning and terminals. The status of accident monitoring and emergency communications is determined according to the coverage provided by the various monitoring facilities and communication networks in Zhoushan Port, and data can be obtained from maritime agencies.

The degree of marine pollution caused by ship accidents is closely related to pollutant leakage. Generally, the greater the leakage, the larger the simultaneous diffusion area of pollutants and, under similar sea conditions, the greater the pollution degree. The degree of impact of leakage on the pollution level is generally based on the emergency response ability of the given country and the degree of attention focused on the environment. Therefore, by referencing the Technical Guidelines for Environmental Impact Assessment of Marine Engineering as well as other relevant literature [23,24], we classify ship pollution emergency response results into two states: success and failure. An emergency response action with more than 5 tons of marine pollutant residuals subsequent to the response is regarded as a failure and thus a cause of pollution to the marine environment.

The state description and discretization of each input variable after discretizing the data of each node are presented in Table 2.

Table 2. The description and discretization of the nodes in the Bayesian network model.


The widely used Netica software (NORSYS software Corp., Vancouver, BC, Canada) was employed in this study to produce the Bayesian network. Netica can program a Bayesian network into a node tree for fast probabilistic reasoning with a simple operation and reliable results. The processed dataset was input into Netica and calculated, and the result is shown in Figure 2. In Zhoushan Port, the probability of a successful emergency response after a ship pollution accident is approximately $83.1 \%$.
![img-1.jpeg](img-1.jpeg)

Figure 2. Result of the Bayesian network model.

# 4.2. Sensitivity Analysis 

Sensitivity analysis is a commonly used uncertainty analysis method that is employed to study the effect of model parameter uncertainty and to quantify the uncertainty of key node risk and related variables. Sensitivity analysis can help decision makers understand the relationship between the input and output variables.

The sensitivity analysis of the Bayesian network analyzes the probability change of the query node by changing the probability estimation of the network evidence node, that is, the degree of reduction in the entropy of the query node information. Accordingly, the evidence node with the greatest influence on the query node is judged. In this study, the evidence node refers to an observable root node (such as wind, wave, visibility, etc.), and the query node refers to the leaf node, i.e., the emergency response result. The intermediate node (such as the environment, emergency response time, and emergency response capacity) can be used as both the query node of the root node and the evidence node of the leaf node. All sensitivity analyses were calculated in this study using Netica.

Information entropy is a statistic that describes the degree of dispersion of the random variables. When information entropy increases, the uncertainty of the variable also increases. The calculation formula is:

$$
H(Y)=-\sum_{y \in Y} P(y) \ln P(y)
$$

Mutual information refers to the amount of information shared between two variables. It is a measure of the degree of interdependence of the variables. It is used to indicate the degree to which the entropy of the query node is reduced, given the probability of the evidence nodes. The mutual information of two discrete random variables $X$ and $Y$ can be defined as follows:

$$
H(X ; Y)=\sum_{y \in Y} \sum_{x \in X} P(x, y) \ln \left(\frac{P(x, y)}{p(x) p(y)}\right)
$$

where $P(x, y)$ is the joint probability distribution function of $X$ and $Y$, and $p(x)$ and $p(y)$ are the edge probability distribution functions of $X$ and $Y$, respectively.

Using Netica and Equations (3) and (4), the sensitivity of the Bayesian network model was analyzed, and the relationship between nodes was represented by mutual information. The calculation results are presented in Table 3. As shown in the table, the mutual information between the emergency response capacity and the ship pollution emergency response result is the largest, which means that the emergency response capacity is the most important factor affecting the emergency response results of ship pollution. The second factor is emergency response time. Mutual information between the environment and ship pollution emergency response results is a minor factor, accounting for only $3.90 \%$. Therefore, the emergency response capacity and emergency response time are the two most important factors affecting the results of emergency response to ship pollution, accounting for $96.1 \%$. Therefore, emergency preparedness has the greatest impact on emergency response and the environment has a smaller impact than emergency preparedness.

Table 3. Mutual information between ship pollution emergency response result and parent node.


According to the same principle, the mutual information between the emergency response capacity, emergency response time, environment, and the parent node is calculated. According to the results, the mutual information is normalized to obtain the global weight of all influencing factors of the ship pollution emergency response result and the partial

weight of the sub-nodes. The weighting results are presented in Table 4. The table shows the relative weights of all risk-influencing factors. The result of the weights is the identification result of the influencing factors of the ship pollution emergency response findings. These results can support the improvement of ship pollution emergency responses at Zhoushan Port. From the local weight of the root node, it can be observed that among the mutual information of all the root nodes and the above three intermediate nodes, emergency vessels, emergency resource allocation, and eco-environmental sensitivity are the root nodes with the greatest impact on the emergency response capacity, emergency response time, and environment, accounting for $37.06 \%, 52.04 \%$, and $32.54 \%$, respectively.

Table 4. Relative weights of all influencing factors.


From the overall weight, it is evident that the number of emergency vessels ranked first. Because the number of emergency vessels should match the number of pollutant recovery devices, an insufficient number of emergency vessels affects the efficiency of pollutant recovery. The second method is emergency resource allocation. When a ship pollution accident occurs, emergency preparedness prioritizes the allocation of nearby warehouses. When the preparedness of nearby warehouses is insufficient, the emergency response time will increase. Thus, the emergency drill has an impact. The number and pertinence of emergency drills in ordinary times will affect the proficiency of emergency personnel in an actual emergency response. The low disposal capacity of emergency personnel affects pollutant disposal efficiency. Equipment status and emergency personnel also have a high weight. A lack of attention to the emergency status leads to a lack of regular and effective management and equipment maintenance. As a consequence, inefficient and poorly performing emergency equipment result. In the event of an accident, it is difficult for emergency equipment to be effective if the personnel reserve of a professional team is insufficient. This is because it is difficult to implement emergency actions quickly and effectively after large-scale pollution accidents occur. Although the remaining influencing factors are not highly weighted, they also affect the ship pollution emergency response results. Therefore, this aspect must be considered when studying the emergency response to ship accident pollution.

# 4.3. Suggestions for Strengthening the Emergency Capacity of Zhoushan Port 

According to the analysis results in the previous section, the main factors affecting the emergency response results are the port's emergency equipment and emergency response team, i.e., emergency resource allocation, emergency vessels, emergency drills, equipment status, and emergency personnel. Therefore, the following suggestions are put forward to

strengthen the construction of emergency equipment and the emergency response team of Zhoushan Port.

1. Strengthen the construction of emergency equipment and facilities

According to the current scenario of ships entering and leaving Zhoushan Port, the government, professional organizations, and terminal enterprises should gradually supplement and update emergency vessels and equipment. In addition, they should provide regular maintenance of facilities and equipment to prevent their failure.

Preparedness can be enhanced by strengthening the construction of emergency equipment and optimally allocating emergency resources in Zhoushan Port, and also by managing emergency resources as a whole to form an "integral" emergency system, and through promoting personnel support and resource sharing among various departments and regions to maximize the utilization efficiency of emergency resources.
2. Strengthen the construction of emergency response teams

We should strengthen the construction of expert teams in ship pollution emergency response, establish an expert resource information platform and an expert resource sharing mechanism, and establish a mechanism for mobilizing experts to participate in the emergency response. Moreover, the management system of the ship pollution expert team should be improved, and expert training should be regularly provided.

A focus on the construction of professional emergency response teams can increase the use of marine emergency response talent, and a knowledgeable maritime emergency response team can be formed. While continuously expanding the size of the team, it is also necessary to effectively train emergency personnel. Corresponding training plans should be formulated for commanders, front-line emergency personnel, drivers, and other team members. Moreover, regular skills and knowledge training should be conducted, and emergency drills should be undertaken so that emergency personnel can identify any problems in the response procedures. These measures would improve the emergency response capabilities in all aspects.

# 5. Conclusions 

In this study, we quantitatively analyzed the successful emergency response to ship accident pollution. We concluded that the factors affecting the successful emergency response are primarily the environment, emergency response time, and emergency response capacity. A ship pollution emergency response model based on a Bayesian network was constructed, and the model parameters were estimated according to the actual weather, hydrology, and emergency resources and personnel at Zhoushan Port. It was concluded that the probability of a successful emergency response at Zhoushan Port was $83.1 \%$. Subsequently, a sensitivity analysis of the influencing factors was carried out. The results showed that of the first-level influencing factors, emergency preparedness (emergency response capacity and emergency response time) was the main factor affecting the results of an emergency response to ship accident pollution, while the impact of the environment in the port was relatively small. Among the second-level influencing factors, emergency vessels, emergency resource allocation, emergency drills, equipment status, and emergency personnel had the greatest impact on the results of the emergency response to ship pollution, followed by wind, waves, total emergency resources, visibility, and eco-environmental sensitivity. The impact of emergency communication and accident monitoring on emergency response results was relatively weak.

These analysis results can be applied to quantitatively evaluate a port's emergency response capabilities for ship accident pollution. Accordingly, effective measures to improve the emergency response capacity of the port can be developed to reduce the risk of ship pollution in the marine environment.

Author Contributions: Conceptualization, P.Z. and G.L.; methodology, Y.Z., W.M. and H.F.; software, Y.Z. and W.M.; analysis, Y.Z., W.M. and G.L.; writing—original draft preparation, Y.Z. and H.F.;

writing—reviewing and editing, H.F. and P.Z.; supervision, P.Z. All authors have read and agreed to the published version of the manuscript.

Funding: This research was supported in part by the National Key Research and Development Program of China (2017YFE9134700), the EC H2020 Project (690713), the National Natural Science Foundation of China (no. 61074142), and the Zhejiang Natural Science Foundation (LY15E080013).

Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Not applicable.
Acknowledgments: We would like to thank to the National "111" Center on Safety and Intelligent Operation of Sea Bridge (D21013), Zhejiang 2011 Collaborative Innovation Center for Port Economy, and Ningbo Collaborative Innovation Center for Port and Shipping Services System for the financial support in publishing this paper.
Conflicts of Interest: The authors declare no conflict of interest.
