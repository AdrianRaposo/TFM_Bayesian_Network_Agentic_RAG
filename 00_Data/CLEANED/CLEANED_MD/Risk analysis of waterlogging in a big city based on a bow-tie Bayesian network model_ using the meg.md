## OPEN ACCESS

EDITED BY
Yilmaz Bayar,
Bandirma Onyedi Eylül University, Türkiye
REVIEWED BY
Rubayet Bin Mostafiz,
Louisiana State University Agricultural
Center, United States
Özlem Yorulmaz,
Istanbul University, Türkiye
*COMPRESPONDENCE
Chun Cai,
ci cai.c@whut.edu.cn
RECEIVED 14 July 2023
ACCEPTED 25 August 2023
PUBLISHED 17 October 2023

## CITATION

Li J, Liu J, Wu T, Peng Q and Cai C (2023), Risk analysis of waterlogging in a big city based on a bow-tie Bayesian network model, using the megacity of Wuhan as an example.
Front. Environ. Sci. 11:1258544.
doi: 10.3389/fenvs.2023.1258544

## COPYRIGHT

(c) 2023 Li, Liu, Wu, Peng and Cai. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

## Risk analysis of waterlogging in a big city based on a bow-tie Bayesian network model, using the megacity of Wuhan as an example

Jiao Li ${ }^{1}$, Juan Liu ${ }^{2}$, Tiancheng Wu ${ }^{2}$, Qianxi Peng ${ }^{2}$ and Chun Cai ${ }^{3 *}$<br>${ }^{1}$ The School of Arts, Hubei University of Education, Wuhan, China, ${ }^{2}$ School of Safety Science and Emergency Management, Wuhan University of Technology, Wuhan, China, ${ }^{3}$ School of Automotive Engineering, Wuhan University of Technology, Wuhan, China

At present, the global urbanization process is accelerating, with the climate changing constantly and extreme weather increasing. In this background, urban flood disasters caused by rainstorms frequently occur in China. Therefore, a disaster risk analysis model based on a bow-tie Bayesian network was established to analyze the risk of waterlogging disasters. First, the waterlogging accident was analyzed, the intermediate and basic events that caused the accident were identified, and the accident tree was drawn. According to the intuitive nature of the fault tree, it was transformed into a Bayesian network, and in the meantime, a posteriori probability analysis of nodes was performed to further obtain the critical importance of basic events. By analyzing the importance of the basic events of waterlogging disasters, the key basic events that lead to disasters were proposed. Finally, the bow-tie model was used to analyze the importance of the hazards, and a strategy for the prevention and control of accidents was proposed. The results show that the major accident node of urban waterlogging accidents is the unsafe state of the urban environment, and the management and control of the urban environment should be strengthened to improve the prevention and control of urban waterlogging, e.g., pre-disaster prevention.

## KEYWORDS

urban waterlogging, importance analysis, bow-tie model, Bayesian network, accident tree analysis

## 1 Introduction

In recent years, the intensification of climate change and rapid urban expansion have led to an increasing trend in the frequency and intensity of regional rainfall, resulting in increasingly frequent urban flooding, which has caused serious social hazards. An area of 2.23 million $\mathrm{km}^{2}$ of land was flooded globally from 2000 to 2018, and the lives of more than 255 million people were disrupted. In China, the national average annual direct economic loss caused by flooding is approximately 150 billion RMB, and the social impacts of the "7.21"rainstorm in Beijing in 2012 and the "7.20"rainstorm in Zhengzhou in 2021 are still remembered (Zhao et al., 2023). In recent years, the risk of flooding caused by the superposition of extreme rainstorm flooding and basin flooding in megacities has been increasing, causing significant casualties and property losses, and joint prevention and

control studies of basin flooding and urban waterlogging disaster chains are urgently needed (Liu et al., 2023). In 2021, 30 provinces (autonomous regions and municipalities directly under the central government) were flooded to varying degrees, with a total of 59,010,100 people affected by flooding, 590 people dead and missing, 150,200,000 houses collapsed, 476,043,000 km² of crops affected, including 872,350,000 km² of crop failure, and direct economic losses of 245,892 million yuan (Compilation group of China Flood and Drought Disaster Prevention Bulletin, 2022).

Cities are vulnerable to extreme weather events, particularly when considering flash flood risk as a result of even more short-duration intensive rainfall. In the context of climate change, compound flooding due to simultaneous storm surges and increased runoff may further exacerbate the risk in coastal cities, and it is expected to be frequent and severe across several North American urban areas. Toronto is Ontario's capital and Canada's foremost economic hub. Toronto spreads over 633.5 km², and its population is 2.73 million (in 2016), 50% of which are visible minorities, which makes it the most populous city in Canada and one of the most multicultural cities in the world. The city's location within the Lake Ontario Watershed and its exposure to moist air masses and high precipitation rates have caused several historical flooding events that resulted in the loss of lives and damage to property and infrastructure in 1878, 1954 (after Hurricane Hazel), 1976, 2005, and 2013. Luna Khirfan et al. developed a multicriteria model that draws on distributive justice's interconnections with the risk drivers of social vulnerabilities, flood hazard exposures, and the adaptive capacity of urban form (through land use and town plans). They tested the model in Toronto, where there are indications of increased rainfall events and disparities in social vulnerabilities. Using ArcGIS, they then mapped and overlayed the values of the risk drivers in all the neighborhoods across the city based on the assigned weights provided by experts (Mohtat and Khirfan, 2022). In a context of global warming characterized by a mean sea level rise and extreme meteorological events, the study of the causes of coastal flooding is essential to protect communities and ecosystems. Densely urbanized and rather unprotected cities in developing countries, such as the historic Saint Louis city in Senegal, are particularly vulnerable to coastal flooding and sea hazards. The results show that over the period 1994–2015, potential flood risk increased by nearly 1 day per year, primarily due to sea level rise, sounding a warning signal to take countermeasures to protect communities and infrastructure (Cisse et al., 2022).

![img-0.jpeg](img-0.jpeg)

**FIGURE 2** Urban waterlogging disaster accident tree.

Table 1 Accident tree symbols and their meanings.


At present, the more commonly used methods for urban storm waterlogging risk assessment mainly include the historical disaster assessment method (Wang et al., 2022), remote sensing image assessment method (Barbara, 2019), index system assessment method (Collins et al., 2020) and scenario simulation assessment method (Wang et al., 2018). Zhang et al. (2018) analyzed the existing urban waterlogging monitoring and early warning system and its problems from the perspective of multi-source data integration, taking Wuhan city, which is seriously affected by waterlogging, as an example. Combining the real situation of each place, we make full use of the new generation of IOT technology and GPRS technology to collect and process the real-time data of urban flooding and propose an optimization scheme to improve the monitoring and early warning system of flooding in Wuhan. It is of great practical significance to enhance the emergency response capacity of China's cities and reduce the casualties and property damage caused by flooding. used the flooding process in a district of Zhengzhou City under the "7-20"heavy rainstorm in 2021 as an example to demonstrate the limited reduction of subsurface water accumulation by flooding in underground space. The generalized reservoir method is simple and easy to implement, and the hydraulic linkage method restores the subsurface flooding process in detail. The results show that accumulated rainfall and periods of heavy precipitation have important effects on subsurface space flooding (Guo et al., 2023). Yu et al. (2023) took the main urban area of Kaifeng City, Henan Province, a typical flood-prone area, as an example, and used the hour-by-hour ponding depth of urban waterlogging monitoring points and simultaneous weather station rainfall data to construct a flooding assessment model based on precipitation factors and historical ponding + precipitation factors.

Zhang et al. (2023) proposed a method of urban storm flooding risk assessment integrating social information to address the problem that the existing urban storm flooding risk assessment did not fully consider social information, obtained natural information of flooding disasters based on urban rainfall and flooding models, captured social information using web crawler technology, established an urban storm flooding risk assessment index system coupling natural and social information, and comprehensively assessed the risk through an index model. Xu et al. (2021) constructed a flooding model based on an InfoWorks ICM model for Beijing City and analyzed the drainage capacity of the urban pipe network and waterlogging characteristics. Using an ArcGIS network analysis module to evaluate the reach and response time of three types of emergency services (public security, medical, and fire) under single and combined scenarios, the city's emergency response capability was determined.

The risks to lives, livelihoods, and property from climate change-related hazards, including floods from extreme rainfall events, are not equal, ensuing from the triad of spatially differentiated patterns of social- and climate-related vulnerabilities, exposure to hazards, and adaptive capacity, in which adaptive capacity refers to the ability to cope (Thomas and Warner, 2019). Empirical evidence shows that the urban form of socially and climatically vulnerable neighborhoods with high exposure to flooding often maintains low adaptive capacity that renders marginalized groups unable to cope with flood hazards (Michael et al., 2019). For instance, there is evidence that lowincome neighborhoods contain a higher percentage of impervious surfaces than affluent neighborhoods due to a lack of green spaces (García-Lamarca et al., 2021), leading to their inadequate adaptive capacity.Khakzad and Van Gelder (2017) used Bayesian networks to assess the vulnerability of factories to flooding. Beuzen et al. (2018) used Bayesian networks of integrated non-linear systems,


TABLE 2 Probability of the occurrence of an elementary event.

![img-1.jpeg](img-1.jpeg)

FIGURE 3 Bayesian network diagram of an urban waterlogging disaster fault tree.

transparent probabilistic frameworks, and low computational costs to study and predict coastal storm risk.

The bow-tie model is highly visual and easy to operate within the enterprise risk assessment method, which has been widely used in recent years for its intuitive and concise characteristics. Most applications of the bow-tie model by current scholars are focused on the accident risk analysis of railroads, highways, oil pipelines, etc. For example, Taleb Berrouane Mohammed and others take the bow-tie model as the basis and establish a fuzzy Bayesian network risk assessment framework based on the bow-tie model with reference to the risk analysis methods in industrial sectors to realize the transformation from static hierarchical analysis to dynamic network reasoning, from risk assessment to risk prediction deepening, and from risk pre-occurrence assessment to risk post-occurrence analysis (Taleb Berrouane et al., 2021). Wang et al. (2021) established a bow-tie model of an ammunition road transport explosion accident, used an accident tree method to analyze the causes of explosion accidents, and proposed preventive measures in terms of drivers, travel speed, safety management, and packaging technology; they used an event tree method to analyze the impact after the explosion, and proposed control measures to reduce the accident loss. Huang addressed the railroad product quality sampling stage, sampling stage, and inspection stage to establish the bow-tie model, used a fault tree to analyze the causes of typical accidents, and used an event tree to analyze the accident emergency plan to analyze the failure risk of railroad product quality sampling. Chen et al. proposed the introduction of the bow-tie model into risk evaluation based on

![img-2.jpeg](img-2.jpeg)

FIGURE 4
Posterior probability of each elementary event in the Bayesian network diagram.

The oil pipeline leakage and explosion accidents in towns and cities that have occurred continuously in recent years and combined it with the improved hierarchical analysis method to derive the weights of the influencing factors and rank them to evaluate the risk of pipelines, which facilitates the proposal of reasonable safety management plans to reduce the occurrence of accidents.

Bayesian networks (BN), proposed by Judea Pearl in 1988, are graphical networks based on probabilistic inference and are currently one of the most effective theoretical models in the field of uncertain knowledge representation and inference. Hart and Pollino (2008) argued that using Bayesian network models for the quantitative risk assessment of systems can effectively analyze the complex relationships between multiple variables and overcome the limitations of existing risk. Lu et al. constructed Bayesian network risk models for the quantitative assessment of oil spill recovery effectiveness under representative winter conditions and evaluated the strength of evidence of the above models according to the study's corresponding risk perspective (Lu et al., 2019). Zhang et al. proposed a method of applying dynamic Bayesian networks to analyze a controlled pressure drilling safety accident scenario and assess dynamic quantitative risk. The effects of uncertainty risk factors in the study were modeled by introducing probabilistic parameters, and quantitative risk analysis and dynamic risk evolution were performed using dynamic Bayesian network inference. The root causes of vulnerability are identified by sensitivity analysis for accident prevention and mitigation measures (Zhang et al., 2018). Minuri et al. (2019) used a finite memory influence diagram (LIMID) approach based on BN extensions to efficiently model complex systems, consider the interdependencies and interactions of system components, and protect critical infrastructure through the efficient assignment of security measures.

Combining the bow-tie model with Bayesian network analysis can clearly express the basic event that caused the accident, analyze its basic event importance, and propose measures to prevent the occurrence of that accident and emergency protection measures to prevent injuries caused by the accident. Borgheipour et al. (2021) used the hydrogen leakage accident of a chlorination plant as a research use case and determined the relationship between the type of catastrophic accident and the actual cause using the bow-tie technique and Bayesian network analysis, suggesting that the use of Bayesian networks can update the probabilities to reduce the uncertainty of the parameters. Bilal et al. (2017) used the fault tree method, bow-tie, and Bayesian networks to quantitatively analyze the causes and consequences of accidents, estimate the probability of occurrence of undesirable events, and use fuzzy logic to evaluate the occurrence of each basic event in the fault tree to develop a complete and effective assessment model for pipeline fire and explosion risk accidents. Xu and Xu (2018) developed a bow-tie Bayesian network model for disaster risk analysis, constructing a disaster-causing model using an accident tree and predicting the posterior probability of disasters using a Bayesian network model. Through the node posterior probability, the importance of basic disaster events was analyzed, the key basic events causing disasters were extracted, and countermeasures and suggestions were put forward for subway flood disasters from three

TABLE 3 Posterior probability and importance analysis of an elementary event.


TABLE 4 The code meanings of various preventive measures in the bow-tie model.


dimensions: pre-disaster prevention, disaster resistance, and postdisaster recovery. Carlotta et al. (2021) investigated an urban flood risk mitigation model using Integrated Valuation of Ecosystem Services and Tradeoffs (InVEST), an open-source tool developed by the Natural Capital Project, and integrating it into a GIS environment. The model was applied to three urban coastal areas in the Italian region of Liguria, estimating the runoff volume of each watershed during two extreme rainfall events. A resilient solution was used by reducing runoff at specific locations. Finally, localized sensitivity analyses were also conducted to understand the impact of rainfall changes on model input parameters. Heavy rainfall disasters can lead to serious economic losses and social problems, posing a great threat to the safety of people's lives and properties and social stability.

The main innovations are: 1) The extraction of three main reasons and disaster factors that cause urban waterlogging disasters; 2) the importance analysis of the accident tree structure is used to excavate the factors' importance ranking for urban waterlogging disasters; 3) the Bayesian network of urban waterlogging disasters is constructed to explore the general urban waterlogging prevention problem, and key importance factor groups are revealed; 4) the bow-tie model of urban waterlogging disaster for scenario response analysis is applied. Four causes and three types of accidents of urban waterlogging disasters are excavated, and preventive and control measures are proposed according to the resulting accidents.

The main contribution is analyzing the evolution process of multiple urban disasters using the probability tree method. This Introduction has described how a megacity is used as the key case analysis to establish an accident tree for qualitative analysis of an urban waterlogging disaster. The "Bow-Tie Bayesian Network Model" section describes how a bow-tie model is established by constructing a Bayesian network for quantitative analysis of the relevant important basic events that cause accidents. The "Accident Tree Analysis of Urban Waterlogging Disaster" puts forward measures to avoid the proposed risks with the bow-tie model combined with the Bayesian network.

## 2 Bow-tie Bayesian network model

The bow-tie model was first proposed by the University of Queensland, Australia, and contains four major elements: hazards, risk events, potential outcomes, and safety barriers, of which safety barriers include pre-accident preventive measures and post-accident control measures; pre-accident preventive measures are set up beforehand to reduce the possibility of accidents; post-accident control measures are adopted after an accident through relevant remedial methods to reduce the degree of impact of the accident.

The risk management action model analyzes how the hazard is released and further evolves into consequences and identifies current release prevention measures versus post-release mitigation measures and the key management or maintenance activities to keep these measures effective. This approach graphically presents the association between the hazard source, hazardous factors, preventive control measures, overhead events, mitigating measures, and consequences in the shape of a bow tie.

As shown in Figure 1, the left side is constructed based on the principle of fault tree analysis, listing the hazards and hazardous factors that may develop or lead to a specific top event; at the same time, the control measures that should be taken for the corresponding hazardous factors for each hazard source are considered. The right side is constructed based on the principle

![img-3.jpeg](img-3.jpeg)

**TABLE 5** Bayesian network diagram of the urban waterlogging disaster fault tree.


of event tree analysis while listing mitigation measures and the further development of hazardous events leading to consequences.

# 3 Accident tree analysis of an urban waterlogging disaster

This section may be divided by subheadings. It should provide a concise and precise description of the experimental results, their interpretation, as well as the experimental conclusions that can be drawn.

## 3.1 Urban waterlogging accident tree

As a method of deductive reasoning, the accident tree analysis method can use a tree diagram to represent the logical relationship between the possible accidents in each system and the various factors of the accident, and then apply mathematical and physical methods to find the events and causes (including direct and indirect causes) leading to the accident, layer by layer, starting from this possible accident. At the same time, the logical relationship between the causes of each accident should be analyzed to find the most important cause of the accident (Khakzad et al., 2013). The accident tree constructed in this study mainly involves two logical gate relationships, "AND" gate and "OR" gate. The "AND" gate indicates that the output event occurs only when all input events occur. The "OR" gate indicates that the output event occurs when at least one input event occurs.

According to the relevant information, in China, the hazard loss of life and property caused by flooding is second only to earthquakes. In this study, taking urban waterlogging disaster as the top event, we summarize and conclude that there are three main causes (Du et al., 2019; Feng and Tong Wen, 2022) of urban waterlogging disaster, including unsafe human behavior (A1), unsafe state of the urban environment (A2), and defects of management (A3). In this study, unsafe human behavior is composed of urban residents (B1) and rescuers (B2), whose logical relationship is represented by the "AND" gate; the unsafe state of the urban environment is composed of planning and construction (B3), drainage system (B4), and local climate change (B5), the logical relationship of which is represented by the "AND" gate; and the defects of management are composed of construction management chaos (X15), emergency response behavior (B6), and inadequate drainage measures (X18), the logical relationship of which is represented by the "OR" gate, and the other logical

![img-4.jpeg](img-4.jpeg)

FIGURE 6
Sensitivity analysis of the urban waterlogging disaster fault tree.

Relationships are followed in this way. Finally, the accident tree of urban inundation disaster is drawn (Figure 2).

The symbolic meanings of each event in Figure 2 are indicated in Table 1.

### 3.2 Structural importance analysis of the urban waterlogging accident tree

Probabilistic importance analysis indicates the extent to which a change in the probability of the occurrence of the *ith* fundamental event causes a change in the probability of the occurrence of the top event. If the probability of occurrence of all basic events is equal to 1/2, then the probability importance coefficient of the basic event is equal to its structural importance coefficient (Eq. 1):

$$I_{\beta}(i)_{\{\xi= \}} = I_{\Phi}(I) \quad (i = 1, 2, \dots, n) \tag{1}$$

In the above equation, *q<sub>i</sub>* represents the probability of the occurrence of the basic event, *I<sub>β</sub>(i)* is the probability importance coefficient of the basic event, and *I<sub>Φ</sub>(I)* refers to the structural importance coefficient of the basic event.

The probabilistic importance coefficient is used to find the structural importance coefficient. First, the minimum cut set of the accident tree is found. The Boolean algebraic method is used to find the minimum cut set, which results in Eq. 2:

$$T = A_1 + A_2 + A_3 = B_1B_2 + B_3B_4B_5 + X_{15} + B_6 + X_{18} \tag{2}$$

The minimum cut set is found to be 14 sets:

$$[X_1, X_3, X_4, X_5], [X_1, X_3, X_4, X_6], [X_2, X_3, X_4, X_5], [X_2, X_3, X_4, X_6], [X_7, X_8, X_{11}, X_{12}, X_{13}], [X_7, X_8, X_{11}, X_{12}, X_{14}], [X_7, X_9, X_{11}, X_{12}, X_{13}], [X_7, X_9, X_{11}, X_{12}, X_{14}], [X_7, X_{10}, X_{11}, X_{12}, X_{13}], [X_7, X_{10}, X_{11}, X_{12}, X_{14}], [X_{15}], [X_{16}], [X_{17}], [X_{18}]$$

According to the minimum cut set, its structural importance ranking is obtained by using the probabilistic importance formula to solve:

$$X_{15} = X_{16} = X_{17} = X_{18} > X_3 = X_4 > X_7 = X_{11} = X_{12} > X_1 = X_2 = X_5 = X_6 > X_{13} = X_{14} > X_8 = X_9 = X_{10}$$

By analyzing the structural importance, it is known that the importance of events affecting urban waterlogging hazards in descending order are: inadequate drainage measures (*X<sub>18</sub>*), emergency response behavior (*B<sub>6</sub>*), construction management (*X<sub>15</sub>*), high population density (*X<sub>3</sub>*), panic psychology (*X<sub>4</sub>*), drainage system (*B<sub>4</sub>*), degree of groundwater exploitation (*X<sub>7</sub>*), uncivilized behavior (*C<sub>1</sub>*), rescuers (*B<sub>2</sub>*), localized climate change (*B<sub>5</sub>*), and road planning (*C<sub>2</sub>*).

$$f(x) = a_0 + \sum_{n=1}^{\infty} \left( a_n \cos \frac{n\pi x}{L} + b_n \sin \frac{n\pi x}{L} \right)$$

### 3.3 Probability of tree-top events in an urban waterlogging disaster

The statistical analysis of the causes of accidents in the past years led to the probability distribution of their underlying events, as shown in Table 2.

![img-5.jpeg](img-5.jpeg)

FIGURE 7
Tornado diagram of an urban waterlogging disaster.

Let an incident tree consist of K minimal cut sets: E<sub>1</sub>, E<sub>2</sub>, ..., E<sub>r</sub>...E<sub>k</sub>. The top event occurrence probability is obtained according to the minimum cut set, and the formula is Eq. 3:

$$P(T) = \sum_{r=1}^{k} \prod_{X_{i} \in E_r} q_i - \sum_{1 \le r \le s \le k} \prod_{X_{i} \in E_r \cup E_r} q_i + \dots + (-1)^{k-1} \sum_{r=1}^{k} \prod_{X_{i} \in E_r \cup E_r} q_i \tag{3}$$

In the Formula (3): *r*, *s*, *k* represents the serial number of the minimum cut set *r* < *s* < *k*;

*i* is the serial number of the basic event; 1 ≤ *r* ≤ *s* ≤ *k* represents the combinatorial order of the two cut sets *r*, *s* in the *k* smallest cut sets; *X<sub>i</sub>* ∈ *E<sub>r</sub>* is the ith fundamental event of the *i*th or *s*th minimum cut set; and *q<sub>i</sub>* is the probability of the occurrence of the event.

# 4 Bayesian network model analysis of urban waterlogging disaster

## 4.1 Bayesian network diagram of urban waterlogging hazards

Bayesian networks are mathematical models based on probabilistic inference [30]. The probabilistic information of the unknown variables is calculated by using the information of some known variables. Its mathematical theory is based on the Bayesian formula (Eq. 4):

$$P(X_1, X_2, \dots, T) = P(X_1)P(X_2)P(C_1 | X_1, X_2) \dots P(T | A_1, A_2, A_3) \tag{4}$$

GeNle software was used to draw the corresponding Bayesian network diagram based on the urban waterlogging disaster accident tree (Figure 3). Where the basic events in the accident tree correspond to the root nodes in the Bayesian network, the intermediate events correspond to the non-root nodes, and the probabilities of the basic events are input by connecting the root nodes to the non-root nodes with arrows.

## 4.2 Bayesian network backward diagnosis analysis of an urban waterlogging disaster

The structural importance analysis is a qualitative analysis of the accident tree, which does not reflect the importance of the basic events to the top events or the importance of the intermediate events and has certain limitations. Therefore, based on the accident tree, we further introduce Bayesian and use its posterior distribution to conduct quantitative analysis to more accurately derive the importance of the basic events leading to the top event, and conduct a more in-depth analysis of the intermediate events, which is more comprehensive.

Using Bayesian networks, the posterior probability of each fundamental event can be inferred backwards by assuming that the top event has occurred (Figure 4), and thus the importance of each fundamental event can be inferred backwards. Additionally, the influence of the occurrence or non-occurrence of each fundamental event on the occurrence of the top event is examined. Based on the magnitude of the posterior probability of the basic event and its degree of influence on the top event, we can comprehensively derive the basic event importance. We use the critical importance [24] to express as Formula (5):

$$\Gamma_{x_i} = \left[P(T | X_i) - P(T | X_i \setminus \left. \left. \left. \left. \right)^{P(X_i)} \right)^{P(T)} \right.\right. \tag{5}$$

*P*(*T* | *X<sub>i</sub>*) denotes the probability of the occurrence of the top event under the condition the occurrence of this basic event, and *P*(*T* | *X<sub>i</sub>*<sup>−</sup>) denotes the probability of occurrence of the top event under the condition of non-occurrence of this basic event. The critical importance is a comprehensive consideration of the *a priori*

probability and posterior probability of the basic event leading to the occurrence of the top event, eliminating the influence of one-sided analysis of the causative factors, which is highly comprehensive.

The results of the importance of each basic event are shown in Table 3. The basic events that cause the top event are divided into four categories according to their critical importance. The first category is {*X*6, *X*7, *X*8, *X*10}, the second category is {*X*11, *X*16}, the third category is {*X*8, *X*13}, and the fourth category is {*other basic events*}. These focus on the causes of the first, second, and third categories of basic events and their impact degrees. It can be seen that the key importance of the basic events to the risk hazard of flooding in urban areas is higher than the insufficient rescue force (*X*6), overexploitation of groundwater (*X*7), blind expansion of roads (*X*8), decline of lake water area (*X*9), decline in greenery coverage (*X*10), substandard drainage network (*X*11), air pollution (*X*13), and inadequate flood control materials (*X*16).

## 5 Bow-tie model analysis of an urban waterlogging disaster

The key importance analysis results show that the intermediate events such as “planning and Construction”, “drainage system” and “local climate” hold high impact on “unsafe state of the urban environment”. Therefore, the bow-tie analysis method is used here to analyze the intermediate event of the unsafe state of the urban environment and analyze its causes that possibly lead to flooding accidents, so that we can precisely propose corresponding prevention and control measures to reduce its risk. Through the analysis of the causes of the unsafe state of the urban environment, 18 recommendations were made, and the meanings of the symbols are shown in Tables 4, 5, and the bow-tie analysis is shown in Figure 5.

The bow-tie model is constructed as follows: the hazardous source is released after breaking all the preventive measures under the action of harmful factors, where the release is called the top event; the top event further develops and breaks all the mitigation measures, causing serious consequences. The construction of the model reveals that preventive measures and mitigation measures as a barrier are effective ways of reducing the probability of accidents and abating accident hazards.

Through bow-tie analysis, four causes of unsafe conditions in the urban environment and three types of accidents that may result can be clearly identified, and 12 preventive measures are proposed for causes such as overexploitation of groundwater, road planning, drainage systems, and local climate change, and six control measures are proposed according to the accidents generated.

There used to be a large area of arable land, water surface, and woodland around the city, and rainwater could infiltrate into the ground in many ways, and the waterlogging situation was relatively light. However, with the increasing urbanization rate, urban construction sites cover the aforementioned water storage areas, making it difficult for rainwater to flow into surface runoff or infiltrate into the ground, resulting in urban flooding.

Sensitivity analysis is considered to be the most efficient way of identifying important nodes and highly sensitive risk factors in Bayesian network analysis (Chen et al., 2016). Urban waterlogging disasters is set as a target node and GeNIe software efficiently calculates a complete set of derivatives of the posterior probability distributions over the target node over each node. The results of the sensitivity analysis are shown in Figures 6, 7.

The alteration of unsafe human behavior and the unsafe state of the urban environment could change urban waterlogging disasters to a large extent. As shown in Figure 7, the derivative of the state in which unsafe human behavior is a YES state, deficiencies in management are a NO state, and the unsafe state of the urban environment is a NO state is highly ranked. Otherwise, urban residents as NO and rescuers as YES may change the unsafe human behavior node to a large extent.

In terms of preventive measures, we should 1) improve the drainage system, repair the drainage network, improve the drainage standard, and improve urban drainage capacity; 2) strengthen urban greening, weaken the “rain island effect”, consider green space as an important content of urban planning, carry out reasonable road planning, and promote three-dimensional urban greening; and 3) establish a common concept, coordinate drainage and water storage projects, build efficient water supply and drainage projects, and carry out in-depth development and utilization of stormwater resources.

The control measures after waterlogging disasters mainly include 1) disaster prevention and a mitigation emergency management system based on big data technology, strengthening the control of disaster sites, timely evacuation of personnel, and rescue and disaster relief; 2) the use of digital and specialized rescue equipment, the establishment of disaster databases, the use of intelligent equipment to participate in rescue, and improve rescue capabilities and efficiency; and 3) improve the horizontal linkage, disaster prevention, and reduction mechanism, smooth the channels for the public to participate in rescue, expand the rescue force, and improve the emergency response capacity to deal with disasters.

## 6 Conclusion

The bow-tie Bayesian network model is constructed to solve problems such as the results in the accident tree model not being able to be inferred backward, while avoiding the one-sidedness of a single model, and more comprehensively describes the causes of an accident and its prevention and control measures. By analyzing the key importance of the 18 basic events of an urban waterlogging disaster to the top event, the key basic events leading to the top event are extracted, so that the accident prevention and control measures can be targeted to reduce the probability of disaster occurrence and minimize disaster losses.

Bow-tie analysis of the unsafe state of the urban environment proposes 12 measures to prevent an accident and six control measures to reduce the probability of the occurrence of a disaster and disaster losses.

From the analysis, it is concluded that the four basic events, insufficient rescue force, overexploitation of groundwater, decreasing lake water area, and decreasing greenery coverage, have a higher degree of influence on the top event hazard, and the prevention of these four basic events should be strengthened in the process of preventing and controlling internal flooding disasters. The following specific measures should be taken: 1) Expand social rescue participation, realize the efficient linkage between official rescue and civil organizations, open up the information publication channels, and realize the timely update and publication of flooding disaster information; 2) establish the ecological red line, reasonably plan the groundwater mining project, and promote the legislative process related to groundwater mining; 3)

provide remedial treatment to land reclamation and increase the protection of lakes; 4) for urban rivers, lakes, wetlands, and other land that can have the function of rainwater storage, no-construction and restricted construction zones should be set up to strictly limit development intensity and ensure the ecological efficacy of the land; 5) when developing green buildings such as parks, their ecological functions should be truly brought into play by adopting measures corresponding to the concept of green development; and 6) construct depressed green areas to appropriately relieve the pressure of drainage networks so that rainwater can be stored and allowed to infiltrate in a timely manner.

There are still some limitations in this study. The derivative disasters of waterlogging disasters are very complex and closely related to the ground and underground environment and facilities, and the risk management of waterlogging disasters is a kind of detection for urban stable operation and facility construction, which in reality can only be explored by using scenario simulation methods. The urban waterlogging accident tree is a typical risk expression framework, reflecting a type of waterlogging disaster scenario. More scenarios can be investigated in future studies, e.g., blocking the drainage pipe network, blocking the river channel, unreasonable flood control material arrangement, and other factors in the modern intelligent construction of a city, which can be quickly monitored and improved through the Internet of Things. Blind expansion of roads and a decline in green plant coverage will gradually improve in future urban planning and construction, which in turn has a certain impact on the correlation relationship between various factors in the urban waterlogging accident tree. Therefore, this study simplifies complex disaster system research, but rapid dynamic change will lead to a certain distortion of the bow-tie model used here, which requires continuous updates of the simulation.

## Data availability statement

The original contributions presented in the study are included in the article/Supplementary Materials, further inquiries can be directed to the corresponding author.

## Author contributions

JiL: Writing--original draft. CC: Methodology, Writing--review and editing. JuL: Methodology, Writing--review and editing. TW: Writing--review and editing. QP: Supervision, Writing--review and editing.

## Funding

The authors declare financial support was received for the research, authorship, and/or publication of this article. This study was supported by the National Natural Science Foundation of China (71603197).

## Acknowledgments

Throughout the writing of this paper, I have received a great deal of support and assistance. We would like to thank my supervisor Xingxing Liu, whose expertise was invaluable in formulating the research questions and methodology.

## Conflict of interest

The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.

## Publisher's note

All claims expressed in this article are solely those of the authors and do not necessarily represent those of their affiliated organizations, or those of the publisher, the editors and the reviewers. Any product that may be evaluated in this article, or claim that may be made by its manufacturer, is not guaranteed or endorsed by the publisher.

Saint Louis historic city, Senegal (West Africa). Front. Mar. Sci. 9. doi:10.3389/FMARS. 2022.993644

Collins, S. L., Vasileios, C., Jackson, C. R., Mansour, M. M., Macdonald, D. M. J., and Barkwith, K. A. P. (2020). Towards integrated flood inundation modelling in groundwater-dominated catchments. J. Hydrologytprepublish) 591, 125755. doi:10. 1016/j.jhydrol.2020.125755

Compilation group of China Flood and Drought Disaster Prevention Bulletin (2022). Summary of China flood and Drought disaster prevention Bulletin 2021. China Flood Drought Manag. 32 (9), 38-45.

Du, H., Cao, J., Shen, Y., and Li, L. (2019). "The simulation evaluation system fuzzy reliability based on fuzzy fault tree," in Proceedings of 2019 International Conference on Modeling, Simulation, Optimization and Numerical Techniques(SMONT 2019), Shenzhen, China, Feb 27, 2019 - Feb 28, 2019, 15-17.

Feng, Y., and Tong Wen, L. (2022). Spatiotemporal differentiation and influencing factors of urban land green use efficiency in Jiangsu Province from perspective of highquality development. Bull. Soil Water Conservation (06), 351-360. doi:10.13961/j.cnki. stbctb.2022.06.042

Garcia-Lamarca, M., Anguelovski, I., Cole, H., Connolly, J. J., Argielles, L., Baro, F., et al. (2021). Urban green boosterism and city affordability: For whom is the 'branded'green city? Urban Stud. 58, 90-112. doi:10.1177/0042098019885330

Guo, Y., Wang, L., and Chen, N. (2023). Simulation of the flood process in urban surface-underground space under extreme rainfall. Adv. water Sci. (02), 209-217. doi:10. 14042/j.cnki.32.1309.2023.02.005

Hart, B. T., and Pollino, C. A. (2008). Increased use of bayesian network models will improve ecological risk assessments. Int. J. 14 (5), 851-853. doi:10.1080/10807030802235037

Khakzad, N., Khan, F., and Paul, A. (2013). Dynamic safety analysis of process systems by mapping bow-tie into Bayesian network. Process Saf. Environ. Prot. 91 (1-2), 46-53. doi:10.1016/j.psep.2012.01.005

Khakzad, N., and Van Gelder, P. (2017). Vulnerability of industrial plants to floodinduced natechs: A bayesian network approach. Reliab. Eng. Syst. Saf. 169, 403-411. doi:10.1016/j.ress.2017.09.016

Liu, J. H., Mei, C., and Shao, W. W. (2023). T Key scientific and technological issues of joint prevention and control of river flood and urban waterlogging disaster chain in megacities. Adv. water Sci. (02), 172-181. doi:10.14042/j.cnki.32.1309.2023.02.002

Lu, L., Goerlandt, F., OsirisValdez, A. B., Arneborg, L., and Höglund, A. (2019). A Bayesian Network risk model for assessing of spill recovery effectiveness in the ice-covered Northern Baltic Sea. Mar. Pollut. Bull. 139, 440-458. doi:10.1016/j.marpolbul.2018.12.018

Michael, K., Deshpande, T., and Ziervogel, G. (2019). Examining vulnerability in a dynamic urban setting: The case of Bangalore's interstate migrant waste pickers. Clim. Dev. 11, 467-678. doi:10.1080/17565529.2018.1531745

Misuri, A., Khakzad, N., Reniers, G., and Cozzani, V. (2019). A Bayesian network methodology for optimal security management of critical infrastructures. Reliab. Eng. Syst. Saf. 191, 106112. doi:10.1016/j.rese.2018.03.028

Mohtat, N., and Khirfan, L. (2022). Distributive justice and urban form adaptation to flooding risks: Spatial analysis to identify toronto's priority neighborhoods. Front. Sustain. Cities 4, 919724. doi:10.3389/fesc.2022.919724

Taleb Berrouane, M., Khan, F., and Kelly, H. (2021). Corrosion risk assessment using adaptive bow-tie (ABT) analysis. Reliab. Eng. Syst. Saf. 214, 107731. doi:10.1016/J.RESS. 2021.107731

Thomas, K. A., and Warner, B. P. (2019). Weaponizing vulnerability to climate change. Glob. Environ. Change 57, 101928. doi:10.1016/j.gloenvcha.2019.101928

Wang, H., Mei, C., Liu, J., and Shao, W. (2018). A new strategy for integrated urban water management in China: Sponge city. Sci. China Technol. Sci. 61 (3), 317-329. doi:10.1007/s11431-017-9170-5

Wang, W., An, Z., and Yao, K. (2021). The application of bow-tie model in the risk analysis of ammunition highway transportation. Traffic Eng. Technol. Natl. (04), $7-10+30$. doi:10.13219/j.gigyat.2021.04.003

Wang, Y., Li, H., Shi, Y., and Yao, Q. (2022). A study on spatial accessibility of the urban stadium emergency response under the flood disaster scenario. Sustainability 24, 17041. doi:10.3390/SU142417041

Xu, M., Yao, Y., Liu, S., Sun, Y., and Yan, Y. (2021). Multi-mode surface generalization supports a detailed urban flooding simulation model. Front. Earth Sci. 9. doi:10.3389/ FEART.2021.340473

Xu, Q., and Xu, K. (2018). Risk assessment of rail haulage accidents in inclined tunnels with bayesian network and bow-tie model. Curr. Sci. 12, 2530. doi:10.18520/cs/v114/ i12/2530-2538

Yu, Q., Huo, J., and Tong, Y. (2023). Research on waterlogging evaluation model of Kaifeng based on support vector machine. J. Catastrophology 38 (3), 342-353. doi:10. 3969/j.issn.1000-811X.2023.03.014

Zhang, L., Wu, S., Zheng, W., and Fan, J. (2018). A dynamic and quantitative risk assessment method with uncertainties for offshore managed pressure drilling phases. Saf. Sci. 104, 39-54. doi:10.1016/j.ssci.2017.12.033

Zhang, Z., Wang, Z., and Fang Dan, H. (2018). Optimal design of urban water logging monitoring and warning system in Wuhan based on Internet of things and GPRS technology. Saf. Environ. Engineering (02), 37-43. doi:10.13578/j.cnki.issn.1671-1556. 2018.02.006

Zhang, Z., Zeng, Y., Huang, Z., Liu, J., and Yang, L. (2023). Multi-source data fusion and hydrodynamics for urban waterlogging risk identification. Int. J. Environ. Res. Public Health 3, 2528. doi:10.3390/IJERPH20032528

Zhao, C., and WanZhang, J. Y. (2023). Review of the characteristics, causes and governance of urban flood in China. J. Catastrophology 38 (1), 220-228. (in Chinese). doi:10.3969/j.issn.1000-811X.2023.03.033