# New Approach for Analyzing Marine Ecosystem Structure Using Bayesian Networks 

Denis Krivoguz ${ }^{\star, 1}$, Sergey Chernyi ${ }^{2,3}$, and Artur Manukov ${ }^{2}$<br>${ }^{1}$ Russian Federal Research Institute of Fisheries and Oceanography ("VNIRO"), Azov-Black Sea Branch of the "VNIRO" ("AzNIIRKH"), 344002, Rostov-on-Don, Russia<br>${ }^{2}$ Kerch State Maritime Technological University, 298309, Kerch, Russia<br>${ }^{3}$ Admiral Makarov State University of Maritime and Inland Shipping, 198035, Saint-Petersburg, Russia

Received 8 June 2021; accepted 27 October 2021; published 20 November 2021.


#### Abstract

Aquatic ecosystems of the Black Sea are complex multiparametric systems with a hierarchical structure. Thus, the main goal of our research was to investigate possibilities of using Bayesian networks to study the structure fo the natural systems in the Black Sea. We used CMEMS Black Sea environmental dataset, which consists of 7 different variables, that, in our opinion, can describe structural relations in the Black Sea ecosystem - sea surface temperature and salinity, concentrations of nitrates and phosphates, amount of chlorophyll-a and net primary production and also dissolved oxygen concentration. We think, that these variables can generally define interactions in water environment of the Black Sea, organisms, that live there and human activity. As a modelling result, we receive a structure of environmental variables interactions. At the top of this structure is a dissolved oxygen, as a final result of the ecosystem functioning. Further, we think it's more appropriate to use Dynamic Bayesian networks for investigation of spatio-temporal changes to distinguish main drivers of changes and provide more balanced management of natural territories.


Keywords: machine learning, Black Sea, Bayesian networks, ecosystem analysis
Citation: Denis Krivoguz, Sergey Chernyi, and Artur Manukov, (2021), New Approach for Analyzing Marine Ecosystem Structure Using Bayesian Networks, Russ. J. Earth. Sci., Vol. 21, ES6001, 10.2205/2021ES000782.

## 1 Introduction

Ecosystem analysis - is one of the most important scientific methods of receiving information about characteristics of any area [Bourlière and Hadley, 1973]. Main goal of the ecosystem analysis is studying and assignment of natural ecological systems, defining their functional potential, georeferencing, ecological and social position [Krivoguz and Borovskaya, 2020; Milns et al., 2010]. Also, it can give an informational basis for more objective evaluation of environmental and resource state for future optimization, predicting of their state, qualitative and quantitative environmental monitoring, etc. Due to the hierarchical structure, ecosystems are a good choice for modern modelling and analytical approaches using machine learning algorithms. Modelling is a key method of ecosystem analysis, which helps to investigate ecosystems in time and space. Aquatic ecosystems are a complex multiparameter systems, described by non-stationary and non-linear processes. Large amount of direct and opposite connections from all of the ecosystem elements, make its behavior unpredictable for researchers. That's why prediction accuracy of some

[^0]ecosystem elements wittingly too low [Lehikoinen et al., 2019]. In this case, ecosystem analysis using machine learning algorithms is a key for increasing predicting performance on modelling.

Objective-oriented approach, used in our paper is that analyzed ecosystem of the Black Sea consists from some variety of objects with some certain properties, which are interact with each other. For example, it can be some physical-chemical properties of water environment (salinity or temperature) which interact with biota or, in our case, phytoplankton, that defined by such factors, as chlorophyll-a concentration and net primary production values.

One of the most widespread use of Bayesian networks is in area of ecosystem services. For example, Landuyt D. [Landuyt et al., 2013] used data about different characteristics of trees and population density combining with Bayesian network to understand amount of wood production and extraction in future. Great example of understanding structure of ecosystem presented in [Milns et al., 2010], where they're investigate inter-habitat networks for different spatial scales of Peak District National Park, United Kingdom. Some interesting implementations of Bayesian networks and aquatic


[^0]:    *Corresponding author: krivoguz_d_o@azniirkh.ru

![img-0.jpeg](img-0.jpeg)

Figure 1: Seasonal zoning of the Black Sea. A – Winter; B – Spring; C – Summer; D – Autumn. [Krivoguz, 2020]

environment presented in [Havron et al., 2017], where using different environmental factors, such as amount of silt and sand, salinity, temperature, total organic carbon, nitrogen and other variables they're mapped marine habitat suitability and uncertainty.

Thus, we think, that using a Bayesian networks can become an important part of more complex spatio-temporal prediction system in future. In this case, Bayesian network helps us to understand not only the structure of the system, but also connections of element's interactions between each other. Further, with analysis of temporal patterns, this approach will help us to investigate the structure of natural systems on different stages of its spatio-temporal evolution. This will help us more accurately identify different factors, having the greatest impact and leading to her transforming.

Some research about investigation of ecosystem structure for fisheries were made by N. Trifonova [Trifonova et al., 2015, 2017]. In their study, they use a dynamic Bayesian network model with a hidden variable and spatial autocorrelation to explore the future of different fish and zooplankton species, given alternate scenarios, and across spatial scales within the North Sea.

Thus, the goal of our research is to investigate possibilities of using Bayesian networks, as a tool for studying the structure of the natural systems on the example of the Black Sea.

## 2 Materials and Methods

### 2.1 Research area

**Geographical conditions.** Black sea is situated between 46°38' and 40°54'N and 27°21' and 41°47'E. It isn't isolated from the World Ocean [Tamaychuk, 2017]. Through the Bosporus Strait it's connected with the Sea of Marmara, that is connected with Aegean Sea through the Dardanelle Strait. The averaged area of the Black Sea is 420,000 km² and volume about 555,000 km³ [Barratt, 1993].

**Geological and tectonic conditions.** Black sea is situated in the depression between Anatolian peninsula and South-Eastern Europe. This depression was formed in Miocene with an active mountain building processes, that divided Tethys ocean into several separate waterbodies [Ozsoy and Unluata, 1997].

Rocks of the Black Sea consist from coarse-grained deposits, like pebbles, gravel and sand [Ivanov and Belokopytov, 2011]. Offshore sediments presented by fine-grained sands and silts, while in the North-Western part of the sea, by shell rocks.

**Climate.** Climate of the Black Sea can be characterized as continental. Shores of Caucasus and Southern Crimea is covered with mountain ranges

from cold northern winds. Atlantic Ocean has a critical impact on the climate of the Black Sea [Ivanov and Belokopytov, 2011]. Averaged air temperature in January in the North part of the Black Sea is about $-1^{\circ} \mathrm{C}$ to $-5^{\circ} \mathrm{C}$, but rarely it can go lower to $-10^{\circ} \mathrm{C}$. Areas in the southern part of the Black Sea is quite warmer, with mild winters, when temperature don't get lower then $5^{\circ} \mathrm{C}$ [Ivanov and Belokopytov, 2011].

In June averaged air temperature in the Northern part of the Black Sea is $22-25^{\circ} \mathrm{C}$, but sometimes it can reach $35^{\circ} \mathrm{C}$ [Ozsoy and Unluata, 1997]. The maximum amount of precipitation drops near Caucasus shore of the Black Sea (about 1500 mm annually), while the minimum - on North-Western part (about 300 mm annually). Averaged sea surface temperature doesn't fall lower then $7^{\circ} \mathrm{C}$ [Ivanov and Belokopytov, 2011].

Natural zones. Studying water objects important to know the seasonal differentiation of zones, due to their very high rate of changing in time. Comparing with land areas, water objects doesn't be stable in the large period of time and the spatial distribution of the different factors can change from season to season (Figure 1).

In winter season distribution of zones spread from East to West. The most important role plays the interaction with the Sea of Marmara, river flows in the Norther part of the Black Sea, Caucasus and areas near the Southern Crimean and Kerch peninsula shores.

In spring, zonation of the Black Sea comes from North to South. Main role here plays large amount of river flows from such rivers as Dnieper, Danube and Dniester in North-Western part of the Black Sea and inflow water from the Sea of Marmara. Due to the interactions of these two water masses, radically different by their properties, they form transitional zone between them from Kerch strait to Danube estuary.

### 2.2 Data

In this research we used monthly averaged data from Copernicus Marine Environmental Monitoring Service (CMEMS) - Black Sea Reanalysis, which contains 7 spatial variables of different environmental factors, describing the Black Sea ecosystem [Lima et al., 2020].

For building the Black Sea ecosystem structure using Bayesian network we used 7 environmental variables: sea surface temperature (SST), sea surface salinity (SSS), nitrates and phosphates, chlorophylla, net primary production (PPN) and dissolved oxygen.

Distribution of environmental variables of the Black Sea presented in Table 1. Concentration of nitrates ranges from 0 to $140.19 \mathrm{mmol} / \mathrm{m}^{-3}$, but usually it values varies around $3-4 \mathrm{mmol} / \mathrm{m}^{-3}$. Higher
values (about $140 \mathrm{mmol} / \mathrm{m}^{-3}$ ) can be explained by flows from the farmlands or other human activity. Concentration of phosphates in the Black Sea waters varies from 0.88 to $5.48 \mathrm{mmol} / \mathrm{m}^{-3}$. Statistical analysis showed that usually phosphates concentrations lays near its maximum, an reaches its minimum only sometimes. Amount of dissolved oxygen varies from $240.37 \mathrm{mmol} / \mathrm{m}^{-3}$ to $287.66 \mathrm{mmol} / \mathrm{m}^{-3}$ and its fluctuations mainly caused by seasonal dynamics. Amount of net primary production in the Black Sea varies from $0.40 \mathrm{~mol} / \mathrm{m}^{-3} \mathrm{day}^{-1}$ to $27.76 \mathrm{mmol} / \mathrm{m}^{-3} \mathrm{day}^{-1}$, that with the concentration of the chlorophyll-a, which is in range from $0.01 \mathrm{mg} / \mathrm{m}^{3}$ to $15.07 \mathrm{mg} / \mathrm{m}^{3}$ explained by seasonal growth of phytoplankton in some areas of the Black Sea mostly in spring and summer. Variations of sea surface temperature and salinity are from $12.97^{\circ} \mathrm{C}$ to $16.94^{\circ} \mathrm{C}$ and from $11.87 \%$ to $18.50 \%$ correspondingly with the lowest values in the NorthWestern part of the Black Sea, due to the high amount of water flows from big rivers, and maximum in the South-Eastern part of the sea.

### 2.3 Algorithm description

Bayesian networks often use in ecology, where they have two main directions of application. First, when we need to understand basic principles of ecosystems functions. In this case, the research bases on edges of Bayesian network to investigate functional relations in ecosystem or on rules, used for constructing conditional probabilities for node to investigate principles of factor's interactions [Scutari, 2010]. The second way is to evaluate values of model and giving us an empirical information, that is useful and related to the key ecological predictors [Chen and Pollino, 2012].

Bayesian networks is a good tool for describing the complex systems and events with uncertainty. The main idea of using Bayesian networks is a decomposition of complex system into several simple elements [Bendtsen, 2017]. Bayesian network is a directed acyclic graph that represents the structure of nodes and edges, where nodes are responsible for some variables and edges represents relations between them [Margaritis, 2003]. Commonly, Bayesian network also called as "Deep network" due to its complicated structure [Cooper and Herskovits, 1992; Singh and Valtorta, 1995]. Presence of the edge between two nodes indicates, that there's a statistical dependency between two variables [Koski and Noble, 2012]. In some cases, the direction of the edge interpreted as a presence of casual relationship between variables[Friedman et al., 1997]. Generally, Bayesian network represents as:

The node $X_{i}$ is a parent of the node $X_{j}$, if they're connected by edge from $X_{i}$ to $X_{j}$. Respectively, the node $X_{j}$ is a child to the node $X_{i}$. If the node $X_{i}$ is

Table 1: Annual distribution of environmental variables in the Black Sea


not connected to the node $X_{j}$ - they're independent of each other or as (1) [Marcot, 2012].

$$
P\left(X_{1}, \cdots, X_{n}\right)=\prod_{i=1}^{n} p\left(X_{i} \mid P a\left(X_{i}\right)\right)
$$

where probability $X_{i}$ depends from probability of corresponding parent node and can be represented by a random value.

The concept of Bayesian network mainly based on two things - conditional probability and joint probability. Conditional probability of event $X$ - is a numeric value of probability, that event $X$ will occur on a condition, that event $Y$ had occurred. The probability for one event can be calculated as (2) [Marcot, 2012].

$$
P(X)=\frac{n(x)}{N}
$$

where $n$ - investigated events, $N$ - all possible events.

For two events, if and is a dependent events, probability calculates by (3) [Marcot, 2012].

$$
P(X \mid Y)=\frac{P(X \in Y)}{P(Y)}
$$

If $X$ and $Y$ are independent events, probability calculates by (4) [Marcot, 2012].

$$
P(X \mid Y)=P(X)
$$

i.e. investigated event occuring is equally same to each other.

Joint probability is a definition of statistical measure for two or more events, that are occurring at the same point of time, i.e. if events $X, Y$ and $Z$ occurs together, their joint probability can be defined by (5) [Marcot, 2012].

$$
P(X \in Y \in Z)
$$

The structure of a simple Bayesian network can be described by three junction patterns: chain, fork and collider (Figure 2) [Margaritis, 2003].

Chain pattern means that event $X$ depends of event $Y$, which depends of event $Z$ or $X \rightarrow Y \rightarrow Z$.
![img-1.jpeg](img-1.jpeg)

Figure 2: Simple representation of a Bayesian network with events $X, Y$ and $Z$.

Fork patter is similar to chain but in this case, dependence is reverse - that $X \leftarrow Y \rightarrow Z$. Collider pattern is differed for others. In this case, the event $Y$ is depend both from event $X$ and from event $Z$ or $X \rightarrow Y \leftarrow Z$ [Marcot and Penman, 2019; Zhou et al., 2020].

## 3 ReSults and DISCUSSION

Through the constructed Bayesian Network (Figure 3), we can see patterns, that shows dependency between main components of the Black Sea ecosystem. Sea surface salinity and sea surface temperature is a basis of the network. Each of these factors are independent from other in ecosystem and all of the patterns starts from them.

We divided this system into 4 levels, according to location of analyzed factors in our network. Each of this level $L_{n}$ has "in-factors" (some factors from level $L_{n-1}$, which are connected with any of the factor in the level $L_{n}$ ) and "out-factors" (some factors from level $L_{n}$, which are connected with any of the factor in the level $L_{n+1}$ ). Each of these factors describes some event or state of this factors according to other in same state of the time.

For building and learning the structure of this network we used R-package "bnlearn" on Black Sea environmental dataset [Nagarajan et al., 2013]. To create Bayesian network we loaded dataset with environmental variables and created undirected and unweighted structure using "hc" command. Next, we set directions of undirected edges of the network using "iamd". This means that direction of the edges will be chosen automaticaly, based on the input data, instead of the setting them manually.

![img-2.jpeg](img-2.jpeg)

Figure 3: Systematic connectivity of environmental factors in the Black Sea modeled by Bayes network.

After this step we fitted our model using unweighted structure and directions of the edges to create visualization of the ecosystem structure using "bn.fit" command.

Sea surface temperature is one of the most important factors of the environment, defining not only a spatial distribution of the ecosystems, but also their biodiversity. For example, water temperature can impact on metabolism speed level of marine organisms and speed of photosynthetic reactions for algae and flora. The main factor influencing the level of sea surface temperature is solar radiation.

Sea surface salinity is also an important factor of any marine ecosystem. Lifecycle of many marine organisms highly depends on the salinity level. This is due to the peculiarities of osmosis – the ability to penetrate into a living cell of the body and vice versa, depending on the concentration of substances dissolved in water, until equilibrium is reached. Main driver of the salinity level changing is an amount of precipitation and the level of evaporation from the sea surface.

Nitrates and phosphates situated higher than salinity and temperature due to their dependency from temperature and salinity and also to the sources. The main driver, defining the level of nitrates and phosphates in aquatic environments of the Black Sea is a human activity, through river flows.

Higher from phosphates and nitrates are situated chlorophyll-a and net primary production. Generally, these two different factors describing the amount of phytoplankton in the Black Sea waters. Also, these factors are dependent from temperature, salinity, nitrates and phosphates.

At the top of the Bayesian network is dissolved oxygen. It's a key factor, that is a result of interactions between other factors.

![img-3.jpeg](img-3.jpeg)

Figure 4: Out-factors layer of level-1.

Schemes of the first-level factors temperature and salinity are quite similar (Figure 4). The only

difference between them is an interaction with chlorophyll-a. The main cause of it is a strong impact of sea temperature on distribution of phytoplankton. This means that if there are any changes in sea surface temperature it will lead to changes in level of the chlorophyll-a amount. On the other hand, sea surface salinity doesn't have any impact on chlorophyll-a amount directly, but mainly though more complex pattern by interactions with another factors.

![img-4.jpeg](img-4.jpeg)

**Figure 5:** In-factors layer of the level-2.

In-factors graph (Figure 5) shows some similarities between level-2 factors nitrates and phosphates. The main difference between them is some impact of the nitrates level and amount of phosphates. Due to the fact, that the source of these factors mainly is an anthropogenic activity, the nature of this dependence can be outside of the Black Sea ecosystem. This means that if the main source of the phosphates and nitrates here is a flow from the rivers of the Black Sea basin, this dependence forms on the stage, when phosphates and nitrates fall into them, not with the functioning of the ecosystem.

![img-5.jpeg](img-5.jpeg)

**Figure 6:** Out-factors layer of the level-2.

Out-factors graphs are quite different for nitrates and phosphates (Figure 6). While changing in phosphates level impact only on phytoplankton, nitrates has more wide interactions with ecosystem of the Black Sea. If we discard interaction between phosphates and nitrates, the only difference between them will be an interaction with the dissolved oxygen, as a top-level factor of our Bayesian network. The main cause of this is a participation of nitrates in different chemical reactions in aquatic environment with using oxygen, that contains in water.

In-factor graph of level-3 factors (Figure 7) chlorophyll-a and net primary production differs mainly by impact of sea surface salinity. Generally, salinity has a direct impact into net primary pro-

![img-6.jpeg](img-6.jpeg)

**Figure 7:** In-factors layer of the level-3.

duction. When its level decreases, then the amount of fixated carbon decreasing too, but it makes no effect into chlorophyll-a amount in aquatic environments. Phosphates and nitrates are well-known factors of phytoplankton growth, while temperature mainly impacts on their spatial distribution. Net primary production is a derivative of an amount of chlorophyll-a and correspondingly phytoplankton biomass.

![img-7.jpeg](img-7.jpeg)

**Figure 8:** Out-factors layer of the level-3

Out-factor graph of this ecosystem (Figure 8) level quite similar, cause mainly these 3 factors describes phytoplankton activity and extraction of by-product of their lifecycle – oxygen. This connection has a direct impact, so when biomass of phytoplankton decreases, then the amount of dissolved in water oxygen will decrease too.

![img-8.jpeg](img-8.jpeg)

**Figure 9:** In-factors layer of the level-4

In-factor graph of the last 4th level (Figure 9) shows pattern of the dissolved oxygen dependency with different factors of the Black Sea ecosystem. These relations can be described with all of the analyzed factors except phosphates, which, as we think, has just an indirect impact. Mostly, these factors make part in different physio-chemical processes, that involves consumption or extraction of oxygen,

so any changes in levels of these factors will lead to increasing or decreasing in the amount of dissolved oxygen, contained in the Black Sea ecosystem.

## 4 Conclusion

In this paper we suggest using of Bayesian networks for investigation and analysis of natural systems structure. We used CMEMS Black Sea environmental dataset, which consists of 7 different variables, that, in our opinion, can describe structural relations in the Black Sea ecosystem - sea surface temperature and salinity, concentrations of nitrates and phosphates, amount of chlorophyll-a and net primary production and also dissolved oxygen concentration. We think, that these variables can generally define interactions in water environment of the Black Sea, organisms, that live there and human activity.

As a modelling result, we receive a structure of environmental variables interactions. At the top of this structure is a dissolved oxygen, as a final result of the ecosystem functioning.

Further, we think it's more appropriate to use Dynamic Bayesian networks for investigation of spatiotemporal changes to distinguish main drivers of changes and provide more balanced management of natural territories.
