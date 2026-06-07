# Article 

## Decision Support System for Adaptive Regional-Scale Forest Management by Multiple Decision-Makers

Yusuke Yamada ${ }^{1, *}$ and Yuichi Yamaura ${ }^{2,3}$ (D)<br>1 Department of Forest Management, Forestry and Forest Products Research Institute, 1 Matsunosato, Tsukuba, Ibaraki 305-8687, Japan<br>2 Department of Forest Vegetation, Forestry and Forest Products Research Institute, 1 Matsunosato, Tsukuba, Ibaraki 305-8687, Japan; yamaura@ffpri.affrc.go.jp<br>3 Fenner School of Environment and Society, Australian National University, Canberra 2601, Australia<br>* Correspondence: yamayu@ffpri.affrc.go.jp; Tel.: +81-29-829-8313

Received: 27 October 2017; Accepted: 15 November 2017; Published: 17 November 2017


#### Abstract

Various kinds of decision support approaches (DSAs) are used in adaptive management of forests. Existing DSAs are aimed at coping with uncertainties in ecosystems but not controllability of outcomes, which is important for regional management. We designed a DSA for forest zoning to simulate the changes in indicators of forest functions while reducing uncertainties in both controllability and ecosystems. The DSA uses a Bayesian network model based on iterative learning of observed behavior (decision-making) by foresters, which simulates when and where zoned forestry activities are implemented. The DSA was applied to a study area to evaluate wood production, protection against soil erosion, preservation of biodiversity, and carbon retention under three zoning alternatives: current zoning, zoning to enhance biodiversity, and zoning to enhance wood production. The DSA predicted that alternative zoning could enhance wood production by $3-11 \%$ and increase preservation of biodiversity by $0.4 \%$, but decrease carbon stock by $1.2 \%$. This DSA would enable to draw up regional forest plans while considering trade-offs and build consensus more efficiently.


Keywords: forest zoning; uncertainty; observed behavior; bayesian network model

## 1. Introduction

Adaptive management (AM) has been advocated for achieving sustainable forest management [1-3]. AM supports management of natural resources while reducing uncertainties through iterative learning and improving management by incorporating environmental and social changes [4,5]. Various cases or methods have been proposed to facilitate AM while reducing uncertainties. Some of these decision support approaches (DSAs) are powerful tools for implementing AM [6-8].

Williams [9] identified four forms of uncertainties concerned with natural resource management: environmental variation, partial observability, partial controllability, and structural or process uncertainty. Environmental variation is caused by such factors as climate variability and strongly affects natural resources. Partial observability arises from a lack of ability and finances to investigate a whole ecosystem, and it results in sampling variation. Partial controllability expresses the differences between the intent of a management plan and actual actions. Structural or process uncertainty refers to incomplete knowledge of the structure and processes of ecosystems, which can change during investigations. These uncertainties can be grouped as ecosystem uncertainties (such as environmental variations or structural uncertainties) and social uncertainties (such as partial controllability or economic changes). The integration of these uncertainties is reflected in the differences in the consequences between a DSA simulation and actual management.

The importance of uncertainties in controllability is acknowledged in natural resource management [10]. In particular, where multiple decision-makers or stakeholders are involved,

it is necessary to consider the influence of broad-scale management (e.g., zoning; see [11]) on local-scale decision-making [12,13]. Discordances between scales of management can be understood only by examining differences between the intentions and observed behaviors of decision-makers [14]. Although some DSAs designed to deal with social uncertainties related to economic change have been established (e.g., [15,16]), no DSAs designed to apply AM to regional forestry while reducing uncertainties of controllability have been offered.

We established a DSA for sustainable AM to support regional forest zoning plans by simulating changes of forest functions relevant to controllability and ecosystem uncertainties. The target scale of the DSA is the municipality, which is the minimum unit of governance and plays a central role in regional forest management in Japan. Most forest owners in Japan have only tiny forest areas, so each municipality usually includes many decision-makers for each forestry activity. We then applied the DSA to a study area to validate its efficacy.

To consider decision-making by individual foresters, the DSA (1) simulates the allocation of future forest resources by predicting when and where forestry activities will be implemented on the basis of observed behavior; and (2) estimates indicators of forest ecological services in simulated forest scenarios. To improve the controllability and effectiveness of regional forest management, the DSA uses a Bayesian network (BN) model to reduce uncertainties through iterative learning.

The case study estimated changes in three indicators of forest functions (wood production, protection against soil erosion, and preservation of biodiversity) under three alternative zoning plans (current zoning, zoning to enhance protection against soil erosion, and zoning to enhance biodiversity). Differences from current zoning indicate the effectiveness of each alternative. Such results will enable municipal governments to implement AM for local forest more efficiently.

Ecological services simulated by DSAs include uncertainties in controllability and ecosystem function. In the case study, we did not interpret the consequences of individual uncertainties, which are often not important for forest managers, who want to know the influences of their plans and management on the resultant ecosystem services.

# 2. Materials and Methods 

To construct a DSA for sustainable regional forest management, we integrated a long-term simulation of spatial allocation of forest resources and methods for evaluation of multiple forest functions based on a BN model, which improves accuracy by iterative learning and is suitable for AM [17,18]. BN is a directed acylic graph with a set of variables and a set of directed edges between variables, which can factor the joint probability distribution for the variables [19,20,21]. For classification problems such as a classification of whether a forest activity is implemented or not, BN have many successful applications reported in literature as Bayesian networks classifier (see [22]).

### 2.1. Simulation Model

To construct a model for a DSA that can reduce uncertainties of decision-making for each forestry activity, simulations must be based on observed behavior of forest owners (e.g., harvesting, planting), because even forest owners themselves do not often know how they arrive at decisions [23]. We based our model on an earlier model [24] constructed to calculate the probability of an operation in a forest stand by a BN model based on observed behavior in forestry activities in the region by Maximum-Likelihood with BNLearn R package [25]. Probabilities, which are based on the forest type, geology, and social factors relevant to target forest stands were inferred with gRain R package [26]. The estimated probability indicates whether or not a particular forestry activity, including clear-cutting, occurs in each stand. Generally speaking, clear-cutting is not the most environmentally-friendly method for having great impacts on soil erosion, wildlife (biodiversity) and other public functions, whereas selective cutting is more environmentally benign. Even so, we only focused on clear-cutting because methods such as selective cutting is not a common way to harvest in Japan. We included zoning as a key factor to reveal its influence on future forest functions. As decision-making in forestry

should be affected by subsidies and guidelines designed for individual zones, we also incorporated biological, geographical, and social factors to estimate probabilities (Table 1).

Table 1. Variables and states used for the model to reveal the influence of regional forest management on individual forestry activities.


The calculated probabilities are then used to simulate the assignment of forestry activities in space and over time. The model compares the probability with a random number ( $0-1$ ); if the probability is larger than the random number, the activity is applied to the stand. The model uses random numbers in the simulation, so the Simulations over 100 years were carried out 100 times, and means $\pm$ variances were compared.

# 2.2. Methods for Evaluation of Multiple Forest Functions 

We evaluated timber production, protection against soil erosion, preservation of biodiversity, and carbon retention. Timber production was evaluated from the simulated amount of harvested timber. The timber volume of each harvest was estimated from a yield table. Indicators for other functions were determined as follows.

### 2.2.1. Protection Against Soil Erosion

Soil supplies ecological services such as water, clean air, and biodiversity [27], so the protection of soil against erosion is crucial [28,29]. In forest, soil erosion is caused mainly by rain and by surface streams [30], and pillar, rill, and gully erosion are typical [31,32,33]. The occurrence of erosion depends on the terrain and on objects on the forest floor [34,35].

We evaluated the risk of soil erosion with a BN model to reveal the relationships with terrain factors and forest floor cover percentage (FCP). In general, steep slopes and poor FCP often contribute to erosion [36,37]. The BN model was trained with data from the National Forest Inventory of Japan (NFI). The NFI is based on a forest resource monitoring survey implemented every 5 years in permanent sampling plots on a $4-\mathrm{km}$ grid [38]. Tree variables such as species and size, FCP, and degree of soil erosion are measured, as well as site conditions such as slope and surface features. The existence of pillar, rill, and gully erosion in every plot is recorded as a binary variable. FCP is measured by eye in increments of $10 \%$. Vegetation cover and large stones are assessed from FCP (Figure 1). FCP is low in crowded forests because the understory vegetation is sparse [35,39].
![img-0.jpeg](img-0.jpeg)

Figure 1. Criteria assessed in inspection of forest floor cover in National Forest Inventory of Japan, adapted from the NFI manual (unpublished).

The structure of the BN model is shown in Figure 2. Slope and surface topography are used as terrain factors. Forest growth stage and dominant species, which determine the forest density, influence FCP. FCP tends to be lower in young forest than in very young and older forest on account of crowding. Forest stage is determined by eye in the NFI. Elements for surface are integrated in two categories to reduce complexity, gentle and steep. We determined the structure of the BN model considering a mechanism of soil erosion, which occur by raindrops and surface stream, and is protected by FCP. The BN model learned NFI of third term (2009-2013), which contains 12,497 plots data for estimating parameters by Maximum-Likelihood with BNLearn R package. States of variables are shown in Table 2.

![img-1.jpeg](img-1.jpeg)

Figure 2. Structure of the Bayesian network model used to estimate the possibility of soil erosion.
Table 2. Variables and states used for the model to reveal the influence of regional forest management on individual forestry activities.


The area where the DSA is applied is divided into 10-m square cells, each of which is evaluated to determine probabilities. Then the probability of soil erosion is inferred for each cell by the forest conditions with gRain R package. The forest conditions for each cell are determined based on Fundamental Geospatial Data [40] and forest inventory data provided by a local government. Slope degree, terrain surface, forest growth stage, and dominated species were used for inference as factors. FCP was inferred from those data because there is no direct information available about it. Cells with $p>15 \%$ (the proportion of plots with soil erosion in the NFI) are regarded as high-risk cells. The total high-risk area is treated as an indicator of the function of protection against soil erosion. If regional management has a good influence on the function, this indicator should be low.

# 2.2.2. Preserving Biodiversity 

The preservation of biodiversity is crucial owing to its relationships with other forest functions, as well as its own economic, ecological, spiritual, and aesthetic values [41]. Old-growth or primary forests have high biodiversity values because they provide habitat to many species (e.g., [42,43]). Studies suggest that the value of biodiversity can be maintained by certain management methods such as establishing unharvested nature reserves [44] and retaining trees during the harvest [45].

Because studies of the retention of old-growth components during harvest (retention forestry) are lacking in Japan and the available information is easily managed, we evaluated the preservation of biodiversity using the areas of natural old-growth forests as indicators. We defined old-growth forest as forest over 80 years old. Ohsawa and Shimokawa [46] also treated forest over 80 years as old-growth forest and found high conservation values.

# 2.2.3. Carbon Retention 

The importance of forest as a carbon sink is likely incontrovertible in this era of climate change [47]. There is increased need to evaluate the effect of forest management on carbon stocks to contribute to the global warming prevention [48]. Regional forest management can prevent decrease of carbon retention by suppressing excessive logging.

We evaluated the function for carbon retention by estimating living woody biomass with an equation provided by Greenhouse Gas Inventory Office of Japan [49]. The carbon stocks are calculated by multiplying the stand volume of each tree species by wood density, the biomass expansion factor, the root-to-shoot ratio and the carbon fraction of dry matter:

$$
C=\Sigma_{j}\left\{\left[V_{j} \times D_{j} \times B E F_{j}\right] \times\left(1+R_{j}\right) \times C F\right\}
$$

where $C$ is carbon stock in living biomass $[t-C], \mathrm{V}$ is stem volume $\left[\mathrm{m}^{3}\right], \mathrm{D}$ is wood density $\left[t-d . m . / \mathrm{m}^{3}\right]$, BEF is biomass expansion factor for conversion of stem volume, R is root-to-shoot ratio, CF is carbon fraction of dry matter $[t-C / t-d . m$.$] . The parameters for each tree species (j) are shown in Table 3.$

Table 3. Parameters used for calculating carbon stock.


### 2.3. Case Study

We applied the DSA that we established to a study area. Using data collected in the study area, the model simulated the changes in indicators of forest functions among the three zoning alternatives. We did not investigate individual uncertainties, only integrated uncertainties, which is what planners need to know. The ability to reduce uncertainties was not verified, because not enough data for iterative learning were available.

### 2.3.1. Study Area

We modeled alternative plans for forest zoning in Ugo municipality, Akita prefecture (Figure 3). Here, $90 \%$ of forest is privately owned (most by small-scale owners), of which half is plantation forest. The dominant species in most plantation forests is sugi (Japanese cedar, Cryptomeria japonica), which is the major forestry species in Japan. Forestry is one of the main pillars of the economy in the region; however, low timber prices have caused economic stagnation in forestry for several decades. This situation gives the age distribution of forests a peaked shape (Figure 4). Timber production must be enhanced to activate the regional economy.

![img-2.jpeg](img-2.jpeg)

Figure 3. Location of the study area, Ugo, Akita prefecture in the Tohoku district of Japan.
![img-3.jpeg](img-3.jpeg)

Figure 4. Current distribution of forest age classes in the study area: forest age was separated by every five years in each class.

The municipality designates $23 \%$ of privately owned forest as an "enhancing wood production" (EWP) zone, which is intended to promote timber production by preferential treatments such as subsidies. The percentage and assignation of EWP zone were initially determined according to the distribution of mature plantation forest when the first municipality plan was established in 1999, and have not been varied since. The designation may not be efficient in terms of forestry promotion.

Forest functions are significant in the region. Rice, which requires plentiful clean water, is extensively cropped, and thus relies on forest to provide clean water and to conserve soil.

Figure 5 shows a structure and variables of the BN model used to simulate the allocation of forestry activities in the case study. The structure of BN was estimated by the authors, and the parameters were estimated by Maximum-Likelihood with BNLearn R package. The model was trained on data on forest resources and forestry activities from 2013 to 2015 (forest inventory and tree felling records supplied by the prefectural government), which contains 12,011 forest stands data for each year. Clear-cutting occurred in both plantations and natural forest. Probabilities of forestry activities were inferred with

gRain R package. The probabilities of stands with conditions, which did not appear in training data, were inferred with evidences of species and age, although such stands were very few. Forest older than 150 years excluded from the list of clear-cutting because a sawmill in the region refuses to accept logs beyond a certain diameter.
![img-4.jpeg](img-4.jpeg)

Figure 5. Structure of the Bayesian network model to estimate the probability of forestry activities.

# 2.3.2. Forest Zoning Alternatives 

Sustainable forest management depends on the application of scientific zoning methods. We considered three forms of zoning: current zoning, zoning to enhance biodiversity (BD zoning), and zoning to enhance wood production (WP zoning) (Figure 6). In BD zoning, compartments with the lowest proportion of natural forest were assigned an EWP zone. In WP zoning, slope degree, stand index, and area of plantation Japanese cedar, which is the major forestry species in Japan were considered. Each district was given a score for the ratio of area of less than $30^{\circ}$ slope to the total area, the average stand index, and the ratio of ceder plantation area to the total area, with each parameter assigned a score of 1 to 5 for each conditions. As a final score for each district, individual parameter scores were summed. Then districts were converted from their current condition to EWP, starting with the stands that received the highest score. The total area of the EWP zone was adjusted to be about the same in each plan. Forest compartments were determined by the local government according to natural landscape features. The mean area is 66.4 ha.
![img-5.jpeg](img-5.jpeg)

Figure 6. Three zoning alternatives compared in the case study.

# 3. Results 

We examined changes in the indicators to investigate the influence of zoning.

### 3.1. Wood Production

In the 100-year simulation of wood production, volumes increased for the first 50 years and then decreased (Figure 7). This trend seems to be due to the distribution of current forest age (Figure 4): the proportion of forest old enough for clear-cutting first increased and then decreased. Because the area of clear-cutting was relatively high in WP zoning, a large amount of harvestable forest was felled. The mean volume of wood production in WP zoning was 3000 to $10,000 \mathrm{~m}^{3}$ larger than in current zoning, or $3 \%$ to $11 \%$ of the total volume of clear-cutting. These differences could be interpreted in terms of efficacy of zoning and be explained by the EWP zone within WP zoning, which tended to cover area where it is convenient for forestry activities. Such areas have appeal for decision-makers to harvest, and can be increased with EWP zoning. Hence, WP zoning was likely to improve the efficacy of the EWP zone. On the other hand, wood production in BD zoning was also slightly higher than in current zoning. The EWP zone of BD zoning covered plantation forest, which is designed for forestry, efficiency was improved, however it was less compared to WP zoning. This result indicates that for wood production, it is more efficient to assign an EWP zone based on terrain features than forest type.
![img-6.jpeg](img-6.jpeg)

Figure 7. Change of wood production over 100 years simulated with the DSS. Boxes show median values, maximum and minimum values, and quartiles of each trial.

### 3.2. Protection against Soil Erosion

Overall, the proportion of the area at high risk of erosion declined for the first 30 years, then increased slightly until around 70 years to a stable level (Figure 8). The initial decline was due also to the distribution of forest age: the area of young forest, where the risk of soil erosion is higher, dropped over time. Part of the bulge in the age distribution (Figure 4) overlaps the range of the trees in the young forest. In addition, very young forest was scarce, because the area of recently clear-cut forest is small.

There were only little differences among the three zoning types. Although WP zoning had more clear-cut area than the other zoning types, it had almost the same area at risk of erosion. Thus, timber production may be compatible with protection against soil erosion.
![img-7.jpeg](img-7.jpeg)

Figure 8. Change in area at $>15 \%$ risk of soil erosion over 100 years simulated with the DSS. Boxes show median values, maximum and minimum values, and quartiles of each trial.

# 3.3. Conserving Biodiversity 

In general, the total area of natural old-growth forest increased for the first 40 years owing to the current age distribution then decreased slightly until around 90 years. Thereafter, there were only slight differences as clear-cutting balanced the growth of forest across the whole region (Figure 9). BD zoning maximized the total area; at 100 years, the area was 16 ha or $0.4 \%$ more than in current zoning and 33 ha or $0.8 \%$ more than in WP zoning. The smaller area in WP zoning could be explained by its greater clear-cut volume. These results indicate the possibility of enhancing biodiversity by zoning and trade-offs between wood production and biodiversity.

The area of old-growth forest was relatively high in BD zoning, although wood production and protection against soil erosion were almost the same as in current zoning. Flexible assignment of the EWP zone can let forest owners avoid clear-cutting in natural and nearby plantation old-growth forest. We designated BD zoning only by considering current factors, such as forest type, rather than static factors such as terrain, even though zoning may affect some forest functions. The results indicate that zoning considered in relation to current factors could enhance certain forest functions as well as terrain factors do.

![img-8.jpeg](img-8.jpeg)

Figure 9. Change of old-growth forest area simulated with the DSS. Boxes show median values, maximum and minimum values, and quartiles of each trial.

# 3.4. Carbon Retention 

Carbon stocks of living woody biomass increased during the simulation (Figure 10). The rate of increase was gradually decreasing. The differential of attractions for forestry activities of forest stands can be assumed as a reason of this trend. Forest stands with factors such as gentle slope or EWP zone, which make them more attractive to forest owners can be clear-cut repeatedly, on the other hand, stands with less attractiveness tend to be avoided for clear-cutting. Less attractive stands got old in an early stage while favorable stands for forest owners stay relatively young to the end due to clear-cutting and reforestation.
![img-9.jpeg](img-9.jpeg)

Figure 10. Change of carbon stock simulated with the DSA. Boxes show median values, maximum and minimum values, and quartiles of each trial.

Current zoning maximized the total area; at 100 years, the area was 8000 ton or $0.4 \%$ more than in BD zoning and 23,000 or $1.2 \%$ more than in WP zoning. The carbon stock of living biomass was relatively high in current zoning. The relative low wood production in current zoning can cause this trend. These results indicate the possibility of trade-offs between wood production and carbon retention.

# 4. Discussion 

The results indicate the efficacy of DSAs in adaptive regional forest management. Scientifically designed zoning can ensure long-term ecosystem services. It is possible to enhance forest functions of both wood production and protection against soil erosion by assigning an EWP zone to cover areas of gentle terrain. However, such zoning might place biodiversity at risk. In this study, biodiversity was evaluated only by the area of old-forest, although landscape patterns can enhance or deteriorate it [50]. Further research might achieve to integrate landscape evaluations for biodiversity with the DSAs to conserve biodiversity while maintaining wood production and reducing soil erosion.

The results show the effects of zoning on ecosystem functions. Zoning is typically assigned without consideration of the effects on forest resources; two main approaches are used: comparing alternatives or functions with contemporary factors (e.g., [51,52]), and comparing scenarios to impose fixed forestry activities (e.g., [53,54]). The former cannot assess sustainability, and the latter can easily be idealistic. In contrast, a DSA designed for uncertainties in both controllability and ecosystem functions enables spatial planning such as zoning to be integrated with temporal planning. In addition, such a DSA adapts to observed behaviors to make the predicted results more realistic. This type of DSA accommodates trade-offs among forest functions during planning.

Although we created the DSA to decrease uncertainties, the case study did not test this outcome, as continuous data collection and inspections are required to verify it: it has not been a long period since the municipal government began to collect data about forestry activities in the study area, so there is not enough data yet to allow iterative learning. In addition, FCP and the occurrence of soil erosion have been recorded only since 2009 and have been measured only once or twice in each plot. Neither was it possible to update the BN model to estimate the risk of soil erosion due to a lack of iterative survey data. However, the ability of the DSA model to reduce uncertainties of controllability was verified by simulation in Yamada [24]. The scientific and adaptive management of local forest will need information gathered continuously and the use of such DSAs.

In spite of these problems, however, our results show how the DSA can benefit regional forest management by providing useful information for zoning to acquire sustainable ecosystem services while including partial controllability.

Participatory planning is one method used for managing regional forests where multiple decision-makers are involved [55,56]. It promotes collaboration and consensus-building among various stakeholders in establishing plans, and has high affinity with AM [57,58]. Its goal is to establish plans to fulfill forest functions by satisfying all needs through trade-offs. Plans based on common sense should have a degree of controllability [59]. Although decision-makers are involved in broad-scale planning in adaptive participatory planning, it is unlikely that every activity is totally suited to a plan [60], and they seldom know how far they can follow the plan in deciding activities. It is important to understand the degree of controllability by management to achieve sustainability. The DSA established in this study can provide a basis for decision-making in participatory planning considering uncertainties of controllability. The DSA improves the feasibility of a plan by simulating consequences of regional management at the local scale. Integrating both participatory planning and a DSA can efficiently reduce uncertainty about controllability. This kind of DSA will support adaptive participatory management of regional forests while reducing uncertainties.

## 5. Conclusions

Prior works have developed various DSAs for adaptive forest management, which aim to achieve sustainability while improving management and reducing uncertainties. Those DSAs tend to pay

attention on uncertainties about ecosystems rather than controllability of management, which is important in regional scale management. This research established a DSA for zoning to manage regional forest coping with uncertainties of both controllability and ecosystem. A BN model based on observable behavior was constructed to estimate influences, or controllability of zoning on the allocation of forestry activities. Adding to that, models including BN were established to evaluate ecosystem services such as protecting soil erosion, preserving biodiversity, or carbon retention. The DSA in this research integrated these models to simulate future trends of forest functions.

The DSA was applied to the study area as a case study to assess efficiency. We compared three zoning alternatives that aimed to enhance different forest functions. The results of the simulation indicated the possibility of the DSA to establishing an efficient zoning by considering the effects of zoning on the target functions in the long-term perspectives. However, the differences of forest functions simulated by the DSA among the alternatives were only slight. Future works should focus on the factors to establish zoning that can enhance target functions more efficiently by arranging attractiveness of forest for forest activities with the DSA of this research.

Acknowledgments: The authors would like to thank T. Nakajima for his valuable comments and S. Miura for lending his expertise on soil erosion. We are also grateful to Akita prefectural government and Ugo municipal government for providing dataset. This study was conducted with the data of the National Forest Inventory of Japan (third term, ver.1.0). All data used in this study is unpublished. Yuichi Yamaura was supported by JSPS KAKENHI Grant Number JP16H03004.
Author Contributions: Yusuke Yamada conceived and designed the experiments; Yuichi Yamaura designed some experiments concerned with forest functions for biodiversity; Yusuke Yamada wrote the paper; Yuichi Yamaura helped write the paper.
Conflicts of Interest: The authors declare no conflict of interest. The founding sponsors had no role in the design of the study; in the collection, analyses, or interpretation of data; in the writing of the manuscript; or in the decision to publish the results.

# Abbreviations 

The following abbreviations are used in this manuscript:
AM Adaptive management
DSS Decision support system
BN Bayesian network model
FCP Floor cover percentage
NFI National Forest Inventory
EWP Enhancing wood production
SE Soil erosion
BD Biodiversity
