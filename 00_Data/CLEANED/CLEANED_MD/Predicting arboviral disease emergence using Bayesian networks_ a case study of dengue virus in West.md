# Predicting arboviral disease emergence using Bayesian networks: a case study of dengue virus in Western Australia 

S. H. $\mathrm{HO}^{1 *}$, P. SPELDEWINDE ${ }^{2}$ and A. COOK $^{1}$<br>${ }^{1}$ School of Population Health (M431), The University of Western Australia, Crawley, Perth, WA, Australia<br>${ }^{2}$ Centre of Excellence in Natural Resource Management, The University of Western Australia, Albany, WA, Australia

Received 9 April 2016; Final revision 24 August 2016; Accepted 24 August 2016;
first published online 13 September 2016

## SUMMARY

A Bayesian Belief Network (BBN) for assessing the potential risk of dengue virus emergence and distribution in Western Australia (WA) is presented and used to identify possible hotspots of dengue outbreaks in summer and winter. The model assesses the probabilities of two kinds of events which must take place before an outbreak can occur: (1) introduction of the virus and mosquito vectors to places where human population densities are high; and (2) vector population growth rates as influenced by climatic factors. The results showed that if either Aedes aegypti or Ae. albopictus were to become established in WA, three centres in the northern part of the State (Kununurra, Fitzroy Crossing, Broome) would be at particular risk of experiencing an outbreak. The model can also be readily extended to predict the risk of introduction of other viruses carried by Aedes mosquitoes, such as yellow fever, chikungunya and Zika viruses.

Key words: Aedes aegypti, Aedes albopictus, Bayesian Belief Network, dengue virus, risk mapping, risk modelling.

## INTRODUCTION

The emergence of arboviral disease epidemics in new locations is often preceded by the spread of their vectors and vertebrate hosts. These processes are increasingly brought about by anthropogenic activities such as travel and trade [1, 2]. For example, an assessment of the possible routes of introduction of West Nile virus to the Galapagos Islands revealed that airplanes carrying infected mosquitoes pose the greatest risk [3]. Attempts to predict the emergence of arboviral diseases in novel sites should therefore take into account the underlying human activities, in addition to the

[^0]environmental suitability of those locations for supporting arthropod vector and host populations.

This paper seeks to present such a model for predicting the emergence of arboviruses carried by Aedes aegypti and Ae. albopictus in Western Australia (WA), with a particular focus on dengue virus (DENV). It therefore provides an advance on previous attempts that predicted dengue risks solely by the habitat niches of the Aedes vectors [e.g. 4, 5]. While both vector species are currently absent from WA, Ae. aegypti is already established in Queensland, and large parts of Australia are climatically suitable for both vector species to survive [4-6]. Since these mosquitoes are frequently intercepted at entry points around the country [7, 8], there is a potential risk of both vectors and the viruses they carry becoming established in WA.


[^0]:    * Author for correspondence: Mr S. H. Ho, School of Population Health (M431), The University of Western Australia, 35 Stirling Highway, Crawley, Perth, WA 6009, Australia.
    (Email: hosoonhoe@gmail.com)

Bayesian Belief Networks (BBNs) are acyclic graphical networks representing conditional probability relationships between the variables/nodes of the network, and have been used in the modelling of disease risk (e.g. [9-11]). The probability distribution of each node is either assigned based on a prior distribution model (for input nodes), or calculated using Bayes' Theorem from prior probabilities ('child' nodes) [12, 13]. BBNs are capable of modelling large complex systems with multiple interacting variables [14]; amenable to incorporating expert opinions; and robust to imperfect knowledge - approximate probabilities often give good results [15, 16]. These factors make BBNs ideal for modelling the uncertain risk of Aedes mosquito establishment and dengue emergence in WA.

From a health perspective, Ae. aegypti and Ae. albopictus are two of the most significant mosquitoes in the world, being transmitters of several important viruses such as DENV, yellow fever virus, chikungunya virus, and the recently headlined Zika virus [17, 18]. Dengue is among the most important arboviral diseases in terms of infection rate and risk to humans [19, 20], with about 2.5 billion people currently living in DENV-endemic areas [20] and around $50-200$ million infections occurring worldwide annually [19].

Given that neither mosquito vector is established in WA, the model was specifically designed to distinguish between: (1) the potential risk of vector(s) and virus becoming established, and (2) the risk of an actual outbreak occurring, in the event that they are established. Maps showing the predicted risks across WA are then presented, which we hope will add to the range of measures already available to counter the introduction of dengue in WA.

## METHODS

The procedure for risk modelling and mapping as outlined below is similar to that discussed in detail in [9].

## Framework and process of BBN risk modelling and mapping

The BBN was developed using Netica ${ }^{\text {TM }}$ (Norsys Software Corp., Canada), and mapping was performed on ArcGIS v. 10.1 (ESRI, USA). A comprehensive review of the literature was conducted to determine the main factors affecting the distribution of Ae. aegypti and Ae. albopictus in Australia and
internationally. An initial BBN was created and GIS-compatible data were sourced from various agencies (Supplementary Table A1). Risk distributions were modelled in 3-month blocks in both summer (December-February) and winter (June-August). All climatic data were averaged throughout these 3-month periods. Subsequent revisions were made to the initial model when necessary; especially the links between nodes and the conditional probability tables (CPTs), which specify the probability relationships of all possible combinations of states between the parent and child nodes [21]. The entire process was iterative and continued until we obtained a satisfactory risk model and risk maps that reflected the literature and expert opinion.

The model is therefore a 'knowledge-driven system', with CPTs populated according to a method recently described in Ho et al. [9]. Briefly, a numerical score/ weight was assigned to every possible combination of parent node states. The probability distribution for any combination of states was then derived from a pre-defined probability distribution table containing the distributions for all possible scores, which had been carefully constructed to be symmetrically balanced around the middle score. This method provided a consistent way of populating opinion-based CPTs.

## Input data processing and classification

All nodes in the BBN were used for modelling and mapping. This section describes how the input data were processed and classified.

## Climatic parameters

Monthly and seasonal temperature, rainfall, and 15:00-hours relative humidity spatial data files were obtained from the Australian Bureau of Meteorology [22].

## Road and railroad density

Every operational 'road' and 'railroad' line feature from 'Global Map Australia 1M 2001' was included [23]. Kernel densities of the lines were calculated with the search radius set to twice the output cell size. Raw density values for every pixel were collated and summary statistics (excluding the value 0 ) obtained. These density values were re-classified as follows: zero, 0 ; low, $0-33 \mathrm{rd}$ percentile; medium, 33rd-67th percentile; high, 67th-100th percentile.

## Seaports and airports

Spatial data for WA seaports were obtained from [24]. Kernel densities of the points were calculated, with the search radius set to twice the output cell size. Density values were re-classified dichotomously as follows: no (for values $=0$, i.e. no seaport within a 20 km radius), and yes (for values $>0$, i.e. a seaport present within a 20 km radius).

Airports servicing flights to and from Queensland (where Ae. aegypti is endemic), and/or international flights, were included, i.e. four airports in Perth, Karratha, Broome and Port Hedland. Their geographical coordinates were obtained and mapped, kernel densities of the points were calculated, with the search radius set to twice the output cell size, and density values were re-classified as per the seaports data.

## Human population density (urban areas and rural settlements)

Data on human population density was obtained from [25], which classifies locations on an urban-rural scale according to population size. 'Major urban' (population $>100000$ ) and 'other urban' (population 100099 999) polygons were combined and overlaid with a rectangular fishnet grid comprising $160 \times 160$ cells (longitude $112^{\circ}$ to $156^{\circ}$; latitude $-9^{\circ}$ to $-40^{\circ}$ ). The dimensions of each cell were $0.275^{\circ} \times 0.19375^{\circ}$ $\left(\sim 600 \mathrm{~km}^{2}\right)$. The percentage of each cell occupied by 'major urban' and 'other urban' polygons was calculated and summary statistics (excluding the value 0 ) obtained. Cells were then re-classified according to the zero/low/medium/high categories as for 'road and railroad density' above.
'Miscellaneous population' point features were obtained from [23], representing locations with aggregations of small dwellings. The kernel densities of such features were calculated with a search radius of twice the output cell size, and summary statistics (excluding the value 0 ) obtained. The densities were re-classified according to the zero/low/medium/high categories above.

## Frequency of DENV introduction

The frequency of reported DENV infection cases in each of the nine health regions of WA [26] was used as a proxy measure of the frequency of DENV 'introduction events' into WA. At present, all these dengue cases are 'imported' from outside the state and no infections were acquired locally. Average reported

DENV infection rate during the years 2007-2012 was calculated for each health region and summary statistics obtained. The frequency of DENV introduction in each health region was subsequently reclassified as follows: below average, $0-33 \mathrm{rd}$ percentile; average, $33 \mathrm{rd}-67$ th percentile; above average, 67 th 100th percentile.

## Ae. aegypti predicted climatic niche

The species distribution modelling software, MaxEnt [27], was used to model the potential distribution of Ae. aegypti in Australia. Past and present locations within Australia where the species was recorded were obtained from [4]. The parameters used in modelling were: altitude (data obtained from [28]), mean annual rainfall, mean annual temperature, mean January maximum temperature, mean January minimum temperature, mean July maximum temperature, mean July minimum temperature, mean January relative humidity at 09:00 hours, mean January relative humidity at 15:00 hours, mean July relative humidity at 09:00 hours, and mean July relative humidity at 15:00 hours (climatic data obtained from [22]). The two most important variables affecting the distribution of Ae. aegypti (annual rainfall and mean January maximum temperature) were not correlated with each other.

Average presence probabilities of Ae. aegypti throughout Australia were obtained after ten replicates. As the climatic niche was classified as a binary variable (i.e. either an area is a suitable niche or not), the mean probabilities were re-classified according to the minimum training presence threshold value (the presence probability of Ae. aegypti at the sample point location which was least suitable). Probability values below this value were taken to indicate 'not climatically suitable' for Ae. aegypti survival and vice versa.

## Ae. albopictus predicted climatic niche

Spatial data for Ae. albopictus's potential climatic niche in Australia was obtained from [5]. (MaxEnt could not accurately predict the full extent of its niche throughout Australia because this species is only found at a few locations in the Torres Strait Islands currently [5].) Any part of the map [5] where the Eco-climatic Index is positive was taken to represent areas that are potential climatic niches for the species.

![img-0.jpeg](img-0.jpeg)

Fig. 1. The infectious disease risk model. It is divided into two parts: (a) models 'endemicity risk', and (b) models 'infection' risk.

## Inclusion of 'endemicity' risk node

A separate 'endemicity' risk node was included, even though it is the 'infection' risk node that actually quantifies the risk of a dengue outbreak. In theory, all locations with equal 'endemicity' risks should have equal probabilities of supporting viable Aedes populations and becoming dengue transmission zones, and as long as a place is located within potential Aedes climatic niches, vector establishment is a possibility. However, evidence indicates that the likelihood of experiencing a dengue outbreak varies at different times of the year according to external climatic factors [4, 29]. Therefore, the initial introduction of Aedes mosquitoes (captured by the 'endemicity' risk node) occurs by anthropogenic factors unaffected by seasonal climatic conditions, but the risk of an actual outbreak - in the event that these vectors are successfully introduced - will be affected by seasonal conditions affecting vector population size and the virus's extrinsic incubation period. This latter process is captured by the 'infection' risk node.

## RESULTS

## Risk model

The BBN risk model is shown in Figure 1. Individual nodes and their prior probability distributions are listed in Table 1, and the CPTs are provided in the Supplementary material. The prior probabilities of parentless nodes are uniformly distributed while those of every other node are calculated from their CPTs.

The rationale behind the BBN's construction, including grounds for node/variable inclusion, is provided in the Supplementary material. Briefly, the model distinguishes between 'endemicity' risk (part A), which quantifies the risk of Aedes vectors and DENV becoming endemic to an area, and the risk of a dengue outbreak occurring in the event that the vector(s) and virus had become established (part B). 'Endemicity' risk factors include the climatic niches of Aedes mosquitoes; density of the transport network (all types of transport were taken into consideration);

Table 1. Types of variables and description of nodes in the network


Table 1 (cont.)


![img-1.jpeg](img-1.jpeg)

Fig. 2. Map showing current 'endemicity' risk throughout Western Australia (dark blue, high; light blue, moderate; light yellow, low risk).
![img-2.jpeg](img-2.jpeg)

Fig. 3. Truncated map showing current 'infection' risk in summer [named locations have moderate risk; low risk for the rest of Western Australia (WA)]. 'Infection' risk is low throughout WA in winter (light blue, moderate; light yellow, low risk).
and density of the human population, which is important because Aedes is highly adapted to human environments [19].

The 'infection' risk node accounts for climatic factors that could affect the risk of an outbreak in the event that both virus and vectors were established. It is thus secondary to 'endemicity' risk but comes into play when analyzing seasonal variations in the risk of dengue outbreak [4, 29]. The effect of temperature on the extrinsic incubation period of DENV in Aedes mosquitoes was also accounted for [30].

## Risk maps

## Current 'endemicity' risk

The distribution of dengue 'endemicity' risk is displayed in Figure 2. Risks are moderate to high around

![img-3.jpeg](img-3.jpeg)

Fig. 4. Map showing 'infection' risk in summer when the seasonal rainfall is above 100 mm at all locations, keeping other nodes unchanged from their current average conditions. Named locations have moderate risk, including the circled area near Jurien Bay. In winter, 'infection' risk is low throughout Western Australia (light blue, moderate; light yellow, low risk).
places with significant human populations that fall within the climatic niches of either Aedes species, including all major populated areas in the southwest as well as centres further north such as Geraldton, Carnarvon, Port Hedland, Broome, and Kununurra. Every other location of WA is predicted to have a low risk of Aedes vector(s) and DENV 'endemicity'.

## 'Infection' risk under current summer and winter climates

Figure 3 is a truncated map of WA that illustrates the 'infection' risk distribution in summer under current average climatic conditions, on the condition that DENV and at least one vector are present. The map was truncated because 'infection' risk is moderate
only in Broome, Fitzroy Crossing and Kununurra, while the rest of the state has low risk. This means that, taking the 'endemicity' risk level and summer climatic conditions into account, those three centres are the most likely places to experience a DENV outbreak.

In winter, the risk of an outbreak is low throughout WA, agreeing with historical observations which showed that DENV epidemics in (eastern) Australia ceased during winters [4, 29].

## Scenario modelling: conditions with maximum rainfall throughout WA

We evaluated a scenario whereby the seasonal rainfall node was at its highest state ( $>100 \mathrm{~mm}$ ). The

![img-4.jpeg](img-4.jpeg)

Fig. 5. Map showing 'endemicity' risk when the human population density is high at all locations (dark blue, high; light blue, moderate; light yellow, low risk).
literature concerning rainfall effects on Aedes population growth rates in Queensland is conflicting, ranging from no relationship [31] to some positive correlation depending on the temporal scale [32]. This may be due to differences and limitations in the experimental methodologies [32]. Because a 3-monthly precipitation of 100 mm was previously associated with large natural populations of Culex mosquitoes in central Australia [33], we selected that value to represent 'high' seasonal precipitation on a statewide scale.

Under this scenario, the risk of a dengue outbreak occurring during summer is shown in Figure 4. Moderate 'infection' risk areas now include more
southerly locations with relatively large populations, as far south as Perth. The northern centres of Kununurra, Fitzroy Crossing and Broome remain at moderate risk. From another perspective, this scenario may also illustrate outbreak risks assuming that water is readily available to the mosquitoes from other sources such as man-made containers. Coincidentally, the southernmost location with moderate risk in Figure 4 coincides with where a historical observation of Ae. aegypti was confirmed, namely Harvey ( $33^{\circ} \mathrm{S}$ ) [6].

During winter, however, the 'infection' risk is unchanged despite the higher rainfall (low throughout WA).

![img-5.jpeg](img-5.jpeg)

Fig. 6. Truncated map showing 'infection' risk in summer when the human population density is high at all locations. In winter, 'infection' risk is low throughout Western Australia (light blue, moderate; light yellow, low risk).

## Scenario modelling: conditions with minimum rainfall across WA

When the seasonal rainfall node was set to its lowest state ( $<50 \mathrm{~mm}$ ), the only location where an outbreak risk was moderate is Broome during summer. The risk is unchanged (low throughout WA) during winter.

## Scenario modelling: conditions with maximum human population density

This scenario assesses the 'endemicity' and 'infection' risk distributions when human population densities across WA are at a maximum, achieved by setting the total urban area and rural settlement density at their highest levels. Both risks are now greatly increased: the 'endemicity' risk is moderate to high throughout much of coastal WA and closely tracks the climatic niches of Ae. aegypti and Ae. albopictus (Fig. 5), leading to an enlarged area at moderate DENV 'infection' risk in summer (Fig. 6), but this increased 'infection' risk does not extend into winter.

## Sensitivity analyses of the risk nodes

The results of sensitivity analyses [21] showing the influence of every other node on the risk nodes are displayed in Tables 2 and 3.

## DISCUSSION

We have presented a trial BBN model for predicting the establishment of Ae. aegypti and Ae. albopictus in Western Australia and the consequent risk of DENV epidemics. Dengue was historically present in WA and cases were notified from 1910 to the 1940s [34]. After the Second World War, dengue was successfully eradicated due to the introduction of reticulated water systems and the reduction of open rainwater tanks, among several other public health initiatives [34]. Currently, diagnoses of dengue infection in WA are only in travellers who had been infected elsewhere [35]. Nonetheless, DENV and its vectors have the potential of returning to WA should conditions allow.

The model assumes that Aedes mosquitoes are introduced solely by human transport, which is valid given that range expansions of many exotic species into non-native areas are mainly brought about by human activities such as trade and travel [36]. This was also true of the historical introduction of $A e$. aegypti into Australia [34].

The probability of species invasion is correlated with 'propagule pressure', a measure of the frequency of introductory events and the number of invading organisms per event [37]. Determining their actual values for Ae. aegypti and Ae. albopictus will require

Table 2. Sensitivity analysis of DENV_Endemic_Risk


Table 3. Sensitivity analysis of DENV_Infection_Risk


extensive data collection at seaports, airports, railway stations, and along all major roads of WA. Since this is an exploratory BBN for assessing dengue risk, these quantities were assumed to be correlated with the
density of the transport network. The model also assumes that all four transportation modes have equal probabilities of introducing the vectors into WA.

Our modelling indicates that the risks of dengue outbreak ('infection' risk) are higher in northern WA but can extend as far south as Perth during summer when the seasonal rainfall is high, provided that at least one vector species is present. When seasonal rainfall is low, the only place predicted to be at risk of experiencing an outbreak is Broome. Altogether, Broome and its surroundings appear to be most at risk of a major outbreak since it is in a tropical location, has the largest resident population in northern WA, and is one of the fastest growing centres in the Kimberley region, being a travel gateway for visitors [38].

In its current form, the dengue risk model is knowledge-driven based on an analysis of the potential risk factors that could affect the emergence of both virus and vectors. As with the Murray Valley encephalitis virus risk model developed by the authors [9], the aim was to demonstrate the feasibility of using BBNs for predicting and mapping mosquitoborne arbovirus risks in a particular context. In addition, such models can be used to guide prevention strategies against the introduction of other exotic Aedes-borne arboviruses into WA, such as chikungunya, yellow fever, and Zika viruses.

## SUPPLEMENTARY MATERIAL

For supplementary material accompanying this paper visit http://dx.doi.org/10.1017/S0950268816002090.

## DECLARATION OF INTEREST

None.
