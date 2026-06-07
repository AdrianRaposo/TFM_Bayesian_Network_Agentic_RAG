# Ecosystemic Reaction of Water Bodies Against Water Flow Fluctuations - a Forecasting Approach 

Leila Halajian, Reza Arjmandi*, Jamal Ghoddousi, Amir Hessam Hassani<br>Department of Environmental Management, Faculty of Environment and Energy, Science and Research Branch, Islamic Azad University, Tehran, Iran

Received: 11 May 2020
Accepted: 4 August 2020


#### Abstract

This research is an attempt to study ecosystem reaction of Karkheh River and Hoor al-Azim Wetland against the changes in the flow regime of the river using Bayesian Network modelling approach. In this research, demographic changes of two fish species of Barbus Grypus and Barbus Sharpeyi, as two important ecological indicators in the region, against the stress caused by water flow fluctuations were investigated by the next 10 years. For this purpose, the Bayesian Network was structured by three sub-models of hydrology, ecology, and quality. Future trends of demographic changes were studied in the form of three scenarios, including the natural condition (before the construction of the dam), current situation (after its construction and operation), and the predicted (proposed) situation of Karkheh River discharge in the next 10 years with a focus on the drought and wet periods. According to the natural scenario, this model predicts a $60 \%$ probability that the Barbus Grypus population will increase or survive, which shows a $16 \%$ decrease compared to the current situation. Due to tangible changes in the volume of water flow in the spring and summer, spawning and larval transmission in the current conditions is reduced compared to natural conditions. As a result, the population of Barbus Grypus in the current situation is lower than that in normal conditions. Based on the proposed scenario, there is a $24 \%$ chance of maintaining or increasing the Barbus Grypus population for the next 10 years. No significant changes were observed under any of the scenarios in the population of Barbus Sharpeyi by the next decade.


Keywords: river flow, water resources, Bayesian Network, Karkheh River, Hoor Alazim Lagoon, Iran.

[^0]
[^0]:    *e-mail: rezaarjmandi96@gmail.com

# Introduction 

Human activities have greatly affected the provision of ecosystem services in recent decades [1-2]. One of these activities is dam building. Researchers have found that changes in the flow regimes of rivers resulting from dam operations are among the most significant issues putting the life of marine animals at risk [3-5]. Dam construction activities have caused flow stress in the ecological systems by inhibiting large volumes of water [6-7]. Many experts and scientists believe that maintaining more natural flow regime is the most effective way for restoring an ecosystem to its optimal conditions, which often relies on natural processes. The adaptive water management approach in which expert knowledge is used to make decisions about water allocation or water sharing has been considered an effective method. Optimal values of eFlow can be obtained for a specific river system using various methods to make sure the aquatic system is maintained in suitable conditions.

These methods fall generally into four categories of hydrological models, habitat simulation models, hydraulic models, and holistic methods [8]. Hydrological models include relatively basic calculations that are applicable to users who may not even be experts in the field and are unable to perform simple analyses on hydrological data [8]. They require minimal time to be constructed and thus, do not require ecological refinement, which makes them perfect a low-resolution approach for water management. To be able to apply the results from these models to catchment management, one would have to refine the obtained data using an updated model of higher order. Even though they are still being applied to solve some problems, higherorder models can provide more accurate and reliable results when studying the impacts of flow changes on ecological diversity. Habitat simulation models have a much higher level of complexity and are able to assess the physical habitat of a particular species in terms of sustainability aspects at different flow levels. They take into account habitat changes due to fluctuating flow rates in the calculations and do not rely on approximated hydraulic parameters. In holistic models, it is assumed that the way the target biota interacts with any prey, predator or symbiotic biota has the same level of impact on the aquatic habitat as the river flow. Nevertheless, incorporating so many different components in these models increases their complexity, making them more difficult to use and less time-efficient. This issue can be addressed by employing Bayesian Networks in the structure of the models. Bayesian Networks (BNs) are among the most efficient modelling methods used in a vast array of problems. Although they can incorporate large data sets from many different sources; however, their simple structure allows for managing and processing the data sets with minimal complexity. BNs, also known as BBNs (Bayesian Belief Networks), are most helpful in incorporating expert knowledge in
the assessment of the impacts of different management decisions. Researchers by BBNs would be able to successfully model the changing nature of ecosystems as well as the uncertainty of ecosystem behaviour. BBNs have features that avoid over-fitting of data [9]. They are capable of providing accurate predictions with a small sample size [10] and by integrating with decision support tools, they are widely used in the management of resources [11-12]. BBNs were first created and employed to assess decision-making strategies under uncertain situations; However, they have shown capabilities in various fields and have been used for solving in many problems [13]. Karkheh is one of the most important rivers in Iran, which its water regime, due to the construction of dams and reservoirs, has undergone major fluctuations during the recent years. Such fluctuations in the water regime may have a great effect on the ecosystem of the area, especially on the population and distribution of fish species. Any changes in the hydrologic pattern of the region can have a large impact on the economy of the region and its ecosystem as the livelihood of the local communities highly depends on fisheries and aquaculture. Therefore, it is necessary to identify these patterns to overcome its adverse consequences by appropriate management measures. The problem is that the identification of these oscillatory patterns, due to the complexity of the ecosystems and the multiplicity of effective factors, is often not easy. One of the advantages of BNs is that there is no limit of minimum sample data to perform the analysis. These networks can run with the available input data of any size. Even with relatively small size samples, precise predictions can be made.

The use of BNs in the study of water resources is the subject of growing research that has been the focus of researchers in recent years. Phan et al. [14] conducted a review research on the application of BNs in the management of water resources and found that $52 \%$ of the papers reviewed used BBNs in the context of strategic decision-making of water resource management. Roozbahani et al. [15] used BNs to develop a framework for water management in an aquifer in Ilam Province, Iran and concluded that the prepared framework would be useful in the management of water resources. Sherafatpour et al. [16] used BNs to allocate agricultural water 6 irrigation networks downstream of the Zayandeh Rood Dam in Iran and reported a good accuracy of the developed BNs model.

In this paper, the objective was to develop a BNsbased model linking the main components of flow to an ecological model, which enables users to forecast an approximate time frame for spawning of two important fish species of Barbus Grypus and Barbus Sharpeyi in Karkheh River. Another aim of this study is to show how BNs are used to manage aquatic ecosystems, especially when parts of existing data sources are based on expert opinions. This study also showed how to quantify qualitative data in the form of a decision support tool.

## Material and Methods

Site under Study

Karkheh River Basin is situated between $47^{\circ} 30^{\circ}$ to $50^{\circ} 45^{\circ}$ eastern longitudes and $30^{\circ} 57^{\circ}$ to $34^{\circ} 57^{\circ}$ northern latitudes in the western part of Iran as a semiarid to arid region. The river water mainly supplied from Kashkan and Saymareh Rivers. These headwaters originate from the mid-western and south-western regions of Zagros Mountains (Fig. 1) and join at PoleDokhtar forming Kharkheh River. On its way to the basin, in the Hoor al-Azim Marshes - a large wetland on the border between Iraq and Iran - it flows through the plains with a relatively flat surface. The river is approximately 964 km in length and discharges into Arvand Rud River. As the third largest river in Iran, Karkheh River has a strategic position and is one of the most important rivers of Oman Basin and the Persian Gulf. It serves as the major supplier of water to Hoor alAzim Wetland. This study focuses on the downstream of the river basin.

In order to analyse the ecosystems of Karkheh River and Hoor al-Azim Wetland, the entire study area was divided into three sections (Fig. 1).

1. From Pay-e-Pol Station to Abdolkhan Station.
2. From Abdolkhan Station to Hamidieh Station.
3. From Hamidieh Station to Hoor al-Azim Wetland.

The major issue in this region is the stress imposed on the ecosystem of the river resulting from changes in the water level and quality. It has negatively affected the population of native fish as well as the riparian vegetation cover. In order to study the reaction of the ecosystem of Khakeh River Basin and Hoor al-Azim Wetland based on the model of Bayesian Network and

FLOWS method, the fluctuations of the flow rates were investigated over a period of 35 years from 1981 to 2016.

## Materials

The hydrological and water quality data including river flow, salinity, pH , temperature were obtained from the Ministry of Energy of Iran. Ecological data related to the birds and vegetation cover of Karkheh River Basin and Hoor al-Azim Wetland were prepared from the Department of Environment of Iran. Data on the population of the two indicator fish species, namely Barbus grypus (shirbot fish) and Barbus sharpeyi (binni fish), were also taken from Iran Fisheries Organization

## Methodology

## FLOWS Method

FLOWS method is one of the reliable and comprehensive methods for assessing the flow requirements in freshwater rivers. In this approach, there is sufficient data and expert knowledge available on hydrology, ecology and geomorphology of the region. It consists of a series of procedures required to maintain specific flow-dependent objectives in the environment and flow specifications needed to keep them at a minimal risk.

To this end, national and regional policies and plans, awareness of the current state of the river and ecosystem, and satisfaction of the stakeholders' expectations are considered through a Project Advisory Group. The obtained flow components are employed
![img-0.jpeg](img-0.jpeg)

Fig. 1. Karkheh River Basin location and the research site.

to determine the magnitude, timing, duration and frequency of various elements of the natural flow.

## BNs Models

BNs are a form of graphical models that illustrate the cause-and-effect relationships between the main factors and components of a system and show how they contribute to the final output of the system. They can be applied to a wide array of problems and possess a significantly high versatility. With their simple yet comprehensive structure, BNs can be incorporated in decision-making processes of resource management systems and can effectively assist in predicting the impacts of changes in a particular ecosystem. Uncertainty is a major issue in the impact assessment and can be handled successfully in Bayesian Networks. BNs can explicitly define the causal assumptions associated with the possible uncertainties in the model description [17]. They are also helpful when the relationships cannot be expressed with a simple mathematical notation [18]. The uncertainties in the systems often originate from the inherent variability and insufficient knowledge of complex systems. In addition to these great features, Bayesian Networks have other excellent characteristics that make them perfect for modelling applications. Easy construction, ability to handle missing data, accurate predictions even with relatively small data sets and being easy to understand without the need for the extensive mathematical knowledge are among these favourable characteristics.

## Conceptual Model

The process of building a Bayesian network begins with the creation of conceptual models. These influence diagrams identify process variables, drivers, and primary inputs. In this research, the knowledge and opinions of experts in the relevant literature were used to build the diagrams that illustrate the interactions between each pair of variables and how these interactions affect the water quality and the ecosystem response. The prepared diagrams included the hydrological, ecological, and quality sub-models.

## Hydrological Sub-Model

To create the hydrological sub-model, after obtaining the opinions of relevant experts, three components were introduced to the sub-model based on the FLOW method.

- Summer low flows: this type of flow provides a suitable habitat with sufficient depth for the two fish species of Barbus Sharpeyi and Barbus Grypus and provides a suitable environment for the protection of aquatic and coastal plants/vegetation. By definition, the value of Q95 - a flow that is greater than $95 \%$ of summer data - is taken as the threshold and the flows below which are called summer low flows. Spring fresh flows: this is a sign for the migration of Barbus Grypus to its spawning spots. In the Q50 limit definition, a flow that is larger than $50 \%$ of spring data is taken as threshold and the flows above which are called autumn fresh flows.
- Winter bankful flow: This flow provides suitable environmental conditions for both species to spawn. The Q5 limit defines flows greater than $5 \%$ of winter flows as the threshold and larger flows are called winter bankful flows.


## Modes of the Nodes and Their Numerical Values

In the hydrological sub-model, the required data of the nodes (volume size for each interval in each scenario) were obtained by solving the flow time series using RAP software. In addition, in each data set of flow components, the mean value was calculated and used as an indicator of flow volume.

## Scenarios

By designing and using management scenarios, the right decisions can be made about environmental water rights in all areas and in different situations. The three scenarios used in this research include natural condition scenario (considering the conditions before the construction of Karkheh Dam), current scenario (which applying the dam post-construction

Table 1. Comparison of the magnitude of the three flow components for three sub-models.


conditions), and proposed scenario (which predicts the condition of the river and wetland in the next 10 years, taking into account the increase in the base flow rate during the drought years). After calculating the thresholds using RAP software, the flow volume values related to each of these thresholds were analysed and for each volume, the obtained values were classified into 7 discrete states. This classification was performed for the natural, current, and proposed scenarios using the threshold values obtained from RAP as monthly indicators.

## Ecological Sub-Model

According to the field surveys and periodic monitoring reports of the Karkheh River and Hoor alAzim Wetland and by comparing biological habits such as migration, spawning, and larval breeding, Barbus grypus (shirbot fish) and Barbus sharpeyi (binni fish) were recognized as the most important and precious aquatic species in the study area. This means that any changes in these species would be representative of changes in other species in the river and wetland.

The hypothesis is based on the fact that if the conditions of these two fish species improve, the conditions will also be better for the other species fish species. The ecological sub-model was defined based on the conceptual model of Karkheh River. This conceptual model focuses on life stages of the two Barbus grypus and Barbus sharpeyi, including the pre-spawning, spawning, migration stages as well as their habitat conditions.

## Barbus Grypus

This is most abundant type of Barbus fish in the south of Iran and is known by its local name Shabout. During the reproduction season, it migrates upstream and lays its eggs on a bed of soft, fine sand covered with a layer of hard gravel. This process occurs in spring when the temperature increases to over $18^{\circ} \mathrm{C}$. The stimulating factor of spawning is the high flows in winter.

## Barbus Sharpeyi

This is another type of Barbus fish with an average length of $20-30 \mathrm{~cm}$ among juvenile fish and $30-55 \mathrm{~cm}$ among full-size adult fish. It spawns in calm waters on marine vegetation and its large yellow eggs are approximately 1.6 mm in diameter. The fish, whose spawning season is in March, April, and May, reaches its puberty/reproductive maturity at the age of 2 years. It prefers an environment of relatively alkaline pH that is high in oxygen and a temperature of approximately $25^{\circ} \mathrm{C}$.

## Node Modes and Numerical Values

The modes of nodes for the fish index in the ecological sub-model are given in Table 2. The Conditional Probability Tables (CPT) were filled out based upon expert opinions due to lack of necessary quantitative data on the indices. Accordingly, by studying the biological model of these two fish species and using experts' opinions, the inter-relations of each biological stage were specified with flow components, water quality, modes, and numerical values.

## Quality Sub-Model

In the conceptual model of the decision-making network, temperature, and pH parameters were used for the structure of quality sub-model. Other important parameters such as salinity, DO (Dissolved Oxygen), BOD (Biological Oxygen Demand), and COD (Chemical Oxygen Demand), which characterize the water quality, could also been considered. However, due to the absence of these data, this study ignored the effects of these parameters.

## Effects of Temperature on Fish and Specification of Temperature Threshold Limits

Increasing the temperature to $10^{\circ} \mathrm{C}$ generally causes the chemical and physiological reactions in fish to double or triple. For example, at $30^{\circ} \mathrm{C}$, fish consume 2 to 3 times more oxygen than 20 degrees Celsius,

Table 2. Ecological nodes, their modes and relations.


and the body's biochemical reactions increase in the same way. The most prominent impact of temperature change is on fish spawning and migrations. As mentioned before, Barbus Grypus migrates to begin spawning when the temperature goes beyond $18^{\circ} \mathrm{C}$. Also, Barbus Sharpeyi spawns at $25^{\circ} \mathrm{C}$, thus this range of temperature was used to determine temperature threshold for the spawning of the fish species.

## pH Parameter and Its Impacts on Fish Habitat

One of the most important chemical parameters with a significant effect on the settlement and dispersal of the species is pH . This environmental characteristic influences the metabolism, diet, and behaviour of fish species. High levels of pH cause the release of ammonia, which is toxic for marine animals at low concentrations. Maintaining a suitable level of pH in habitats is crucial to the health and survival of fish populations. Therefore, to create the network, pH range of between 7 and 8 was used as a threshold for the habitat of Barbus Grypus and Barbus Sharpeyi in the process of developing the CPT tables.

## Complete Bayesian Network Model

## Developing the Conditional Probability Tables (CPT)

After defining the conceptual model, elaborating the variables, and classifying the value of each variable, the conditional probability between them and their tables is obtained using Netica software. There are three ways to fill the tables:

1. Filling the tables manually; in the model developed for the two indicator fish, after collecting experts' view, the tables were filled and introduced to the model manually;
2. The relations can be introduced in the form of equations; so, the model inputs should be defined as equations;
3. Case data collection is considered as input to the model, which is part of the community under study.

## Sensitivity Analysis

One of the remarkable features of the BNs is that it provides the possibility to assess the impact of each factor on the increase of each ecological index, and thus
![img-1.jpeg](img-1.jpeg)

Fig. 2. eFlow conceptual model for the Karkheh River showing the linked hydrological, quality, and ecological models.

one can realize which factor has the most significant effect on the promotion of the ecological indices. This feature is actually used to investigate the uncertainty of the model variables and their effect on the model output. It also examines the sensitivity of the output node to changes in network inputs. By sensitivity analysis, nodes are ranked based on their effects on the probability of the target node. This helps minimize the uncertainty, creates reliability in the decision-making process, and reveals the parts that need further research.

## Results and Discussion

The Bayesian network developed to assess the environmental water rights of Karkheh River and Hoor al-Azim Wetland is illustrated in Fig. 2. The figure depicts how the sub-models are interrelated. Range nodes and scenarios are introduced to construct a more efficient network. Range nodes make it possible to select three ranges in the downstream of the dam, and the scenario node allows the user to choose one of the three flow scenarios (natural, current, and suggested).

Fig. 3 shows the model sensitivity analysis for Barbus Grypus. It determines the indicators of more importance for the fish population. According to the figure, the spawning of Barbus Grypus has the highest effect on its population. After that, temperature, migration, habitat conditions, and spring flow frequency are the most important factors, respectively. In the graph for Barbus Sharpeyi, the habitat holds the highest rank of significance. Other variables, including spawning, spring low flows, and temperature rank next in ascending order.

## Network Analysis

After adding all the conditional probability tables to the Bayesian network, the model was run separately under the three pre-defined scenarios and the obtained results were analysed based upon the indicators. According to the results of Bayesian analysis for the natural, current, and proposed scenarios, the status of the river and the wetland were compared. It was also possible to calculate the improvement (in percent) in the ecological status of the river and the wetland after applying the proposed measures. Due to the higher importance of Barbus Grypus in the upstream of the river, this indicator was studied at the stations of Pay-epol and Abdolkhan.

Fig. 5 shows the results for the Barbus Grypus population at the Pay-e-pol Station under the natural scenario. By comparing the frequency of winter flow in natural and current conditions, there is no significant change in spawning due to the lack of tangible changes in the frequency. However, due to tangible changes in the volume of water flow in spring and summer, spawning and larval transmission in the present conditions is reduced compared to natural conditions. As a result, the population of Barbus Grypus in the current situation is lower than natural conditions. As mentioned earlier, the proposed scenario considers that the water right of the river will be increased in drought periods and under this hypothesis, it predicts the river flow rate for the next 10 years. According to this scenario, there is a $24 \%$ chance of maintaining or increasing the fish population for the next 10 years. By studying the population of Barbus Grypus at Abdolkhan Station, a $65 \%$ probability of survival or increase in
![img-2.jpeg](img-2.jpeg)

Fig. 3. Results of the sensitivity analysis for Barbus Grypus a) and Barbus Sharpeyi b).

![img-3.jpeg](img-3.jpeg)

Fig. 4. Bayesian Network Analysis under the natural scenario at Pay-e-Pol Station, Karkheh River.
fish populations was observed. This indicates a decline of $5 \%$ in the fish population compared to the current situation. One of the reasons for this can be tangible changes in the flow rates of the river in spring and summer seasons, and the other would be unfavourable thermal conditions. Under natural conditions, there is a $75 \%$ chance of having favorable thermal conditions, while in the current situation this is likely to decrease by $13 \%$. The result will be a reduction in the likelihood of "stimulation to spawning" as well as "spawning". Under the proposed scenario, a $10 \%$ improvement will be observed in the fish population at this station.

Since Barbus Sharpeyi is more important in the downstream of the river, its population was studied at Hamidieh Station. The results under the natural scenario suggest a $19 \%$ chance of survival or population growth, which in the current situation has a drop of almost $2 \%$. The three nodes of "stimulation of spawning", "spawning", and "habitat conditions" have a direct impact on the "population of Barbus Sharpeyi" node. By examining the stimulation of spawning node, compared to the natural condition, a reduction of $2 \%$ in this node is observed under the current situation. This reduction is almost $3 \%$ in the node of spawning. The results for the node of habitat conditions represent
a reduction of $1 \%$ under the current condition in comparison with the natural scenario. Among the factors influencing these changes can be pointed to the changes in temperature and pH nodes as well as the volume of river flow in the spring and summer, which ultimately causes a change in the population of Barbus Sharpeyi. Under the proposed scenario, no significant change is observed in terms of the improvement of the fish population (Fig. 5).

This study showed how minor changes in water fluctuations affected by dam-induced flow stress could affect the ecological parameters of the study area. Similar conclusion was reported by Morrison and Stone in 2014 [19]. They run a Bayesian network model based on four ecological indicators of "timing of seed availability", "floodplain inundation", "river recession rate", and "groundwater depths" to evaluate the effect of water management decisions on the riparian vegetation of Gila River, New Mexico. They found that even slightest changes to river flow could have large ecological consequences.

Our results also showed that respect for environmental water rights in aquatic areas, particularly during drought periods, could be effective not only in the sustainability of aquatic ecosystems but also in the

![img-4.jpeg](img-4.jpeg)

Fig. 5. Bayesian Network Analysis under the natural scenario at Hamidieh Station, Karkheh River.
conservation and survival of aquatic organisms. With a similar approach, Angel and Loftus in 2017 [20] discussed the political ecological approaches to water justice. Likewise, Nilsalab et al. (2017) [21] introduced environmental water right as an important factor for sustainability of rivers and their ecosystem services. The results of this research showed that changes in the river flow regime and collapse of thermal equilibrium induced by the construction of Karkheh Dam could reduce the population of Barbus Grypus by $16 \%$. The role of dam building on thermal conditions of river water was also emphasized by Kędra and Wiejaczka in 2017 [22]. This is in line with the results reported by He et al. (2020) [23]. They investigated the effects of dam construction on the thermal condition of Yangtze River in China and found that the dams upstream of the river could leave cumulative negative effects on the river thermal conditions at downstream areas. Trifonova and his colleagues in 2017 [24] reported the same findings. They used Bayesian network models to analyse the future population of different fish and zooplankton species in North Sea. They introduced temperature as one of the environmental factors affecting the future trends of zooplankton biomass. The role of this factor is also emphasized in our research. According to the
research findings, BNs is a useful tool in modelling aquatic components and their interactions against ecosystem variables. This is in line with the findings reported by Barton et al. [25]. They confirmed the capability of the model in analyzing the environmental regimes and the alternatives for the restoration of physical habitats. Sensitivity analysis is another strength point of Bayesian Networks, which was emphasized by Katic and Morris in 2016. Temperature, pH , and river flow in spring and summer were three factors affecting fish populations in this study. The factor of thermal conditions was also highlighted by Li et al. in 2017 [26]. According to their findings, annual spawning of whitefish in Huron Lake may start earlier during the warmer years.

## Conclusion

According to the research findings, even minor changes in water fluctuations due to flow tension caused by damming in Karkheh River could have an adverse influence on the aquatic ecosystem of the study area. In the case of observing water rights in drought periods, the regular spawning and larval transmission

patterns of Barbus Grypus and Barbus Sharpeyi would be preserved and consequently, their population will not change significantly. The research findings showed that river flow regime and thermal equilibrium are two important environmental conditions affecting fish populations. It was revealed that changes in the flow regime of Karkheh River and collapse of thermal equilibrium caused by the construction of Karkheh Dam led to a $16 \%$-reduction in the population of Barbus Grypus.

This paper was an attempt to provide a decision support framework so that decision makers and water resource managers can assess easily and quickly the consequences and effects of their decisions on ecosystems and their services. The findings showed how quantitative and quantitative changes in river flow could affect the survival of fish species by affecting the larval transplantation and spawning time. The use of the Bayesian network model facilitated the achievement of the research objectives. The graphical tool of the model enables the graphic representation of the cause and effect relationships and makes it easier to understand the complexities of these relationships. The use of this model is especially recommended when not enough information is available. BNs can provide a powerful tool for reasoning under uncertainty. The model can involve experts' opinion in the calculations as one of the key elements of water and natural resource management. Despite the advantages of this method, its use comes with a series of limitations. As such, the model structure does not allow users to consider feedback loops, while they are considered as one of the most important components of the ecosystem response to inputs fluctuations in environmental systems. In this study, in order to overcome this limitation, nodes were chosen in a way that did not need the feedback loops. Another important constraint of the Bayesian models is the difficulty of processing time functions. More recent versions of Bayesian network-based software are expected to overcome these limits to some extent.

## Conflict of Interest

The authors declare no conflict of interest.
