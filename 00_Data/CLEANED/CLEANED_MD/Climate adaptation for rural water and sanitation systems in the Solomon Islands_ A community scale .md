# (M) GRIFFITH UNIVERSITY 

## Climate adaptation for rural water and sanitation systems in the Solomon Islands: A community scale systems model for decision support

## Author

Chan, T, MacDonald, MC, Kearton, A, Elliott, M, Shields, KF, Powell, B, Bartram, JK, Hadwen, WL

Published
2020

## Journal Title

Science of the Total Environment

## Version

Accepted Manuscript (AM)

## DOI

10.1016/j.scitotenv.2020.136681

## Rights statement

(c) 2020 Elsevier. Licensed under the Creative Commons Attribution-NonCommercialNoDerivatives 4.0 International Licence (http://creativecommons.org/licenses/by-nc-nd/4.0/) which permits unrestricted, non-commercial use, distribution and reproduction in any medium, providing that the work is properly cited.

## Downloaded from

http://hdl.handle.net/10072/391630

Griffith Research Online
https://research-repository.griffith.edu.au

# Journal Pre-proof 

Climate adaptation for rural water and sanitation systems in the Solomon Islands: A community scale systems model for decision support
T. Chan, M.C. MacDonald, A. Kearton, M. Elliott, K.F. Shields,
![img-0.jpeg](img-0.jpeg)
B. Powell, J.K. Bartram, W.L. Hadwen

PII: S0048-9697(20)30191-1
DOI: $\quad$ https://doi.org/10.1016/j.scitotenv.2020.136681
Reference: STOTEN 136681

To appear in: Science of the Total Environment

Received date: $\quad 16$ June 2019
Revised date: $\quad 12$ January 2020
Accepted date: $\quad 12$ January 2020

Please cite this article as: T. Chan, M.C. MacDonald, A. Kearton, et al., Climate adaptation for rural water and sanitation systems in the Solomon Islands: A community scale systems model for decision support, Science of the Total Environment (2020), https://doi.org/ 10.1016/j.scitotenv.2020.136681

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Climate adaptation for rural water and sanitation systems in the Solomon Islands: A community scale systems model for decision support 

T. Chan ${ }^{\text {a,1 }}$, M. C. MacDonald ${ }^{\text {b }}$, A. Kearton ${ }^{\text {c }}$, M. Elliott ${ }^{\text {d }}$, K. F. Shields ${ }^{\text {e,2 }}$, B. Powell ${ }^{\text {c,f }}$, J. K. Bartram ${ }^{\text {e }}$, W. L. Hadwen ${ }^{\text {b.g }}$<br>${ }^{a}$ Corresponding author: Monash Sustainability Institute and the Water Studies Centre, Monash University, Victoria, Australia. terry.chan@delwp.vic.gov.au,<br>${ }^{\mathrm{b}}$ Australian Rivers Institute, Griffith University, Nathan, Queensland 4111, Australia<br>${ }^{\text {c }}$ International WaterCentre, PO Box 10907, Adelaide St, Brisbane, Queensland 4000, Australia<br>${ }^{\text {d }}$ Department of Civil, Construction and Environmental Engineering, University of Alabama, Box 870205, Tuscaloosa, AL 35487, USA<br>${ }^{\text {e }}$ The Water Institute, Department of Environmental Sciences and Engineering, University of North Carolina at Chapel Hill, CB\#7431, Chapel Hill, NC 27599, USA<br>${ }^{f}$ School of Chemical Engineering, The University of Queensland, St Lucia, Brisbane, Queensland 4072, Australia<br>${ }^{g}$ Griffith Climate Change Response Group, Griffith University, Nathan, Queensland 4111, Australia

[^0]
[^0]:    ${ }^{1}$ Present address: Waterway Programs Branch, Department of Environment, Land, Water and Planning, PO Box 500, Melbourne, Victoria 8002, Australia. Email: terry.chan@delwp.vic.gov.au
    ${ }^{2}$ Present address: Department of Geography, 1251 University of Oregon, Eugene OR 97403-1251, USA

#### Abstract

: Delivering water and sanitation services is challenging in data poor rural settings in developing countries. In this paper we develop a Bayesian Belief Network model that supports decision making to increase the availability of safe drinking water in five floodprone rural communities in the Solomon Islands. We collected quantitative household survey data and qualitative cultural and environmental knowledge through community focus group discussions. We combined these data to develop our model, which simulates the state of eight water sources and ten sanitation types and how they are affected by season and extreme events. We identify how climate and current practices can threaten the availability of drinking water for remote communities. Modelling of climate and intervention scenarios indicate that water security could be best enhanced through increased rainwater harvesting (assuming proper installation and maintenance). These findings highlight how a systems model can identify links between and improve understanding of water and sanitation, community behaviour, and the impacts of extreme events. The resultant BBN provides a tool for decision support to enhance opportunities for climate resilient water and sanitation service provision.


Keywords: water resource management, Bayesian belief network, Pacific Islands, small island developing states, climate change, rainwater harvesting

# 1 Introduction 

The delivery of drinking water and sanitation ( WaSH ) services is a major challenge in developing countries (WHO and UNICEF 2017). Among these are the Pacific Island Countries (PICs), of which six of the fifteen nations are categorised as among the Least Developed Countries according to the United Nations (UN 2018). Although WaSH coverage is increasing in many regions globally, overall WaSH conditions remain poor for many PICs (WHO and UNICEF 2017, Anthoj et al. 2019). Their isolated and dispersed geography, small

and predominantly rural populations, limited resources and diverse cultures make provision of WaSH services especially challenging (Moglia et al. 2012, Hadwen et al. 2015, MacDonald et al. 2017). PICs also have costly access to markets and supply chains (affecting investment in WaSH infrastructure and maintenance) and financial, human and technical resource disadvantages not faced by countries in other regions and contexts (Briguglio 1995, Saunders et al. 2016). It is also clear that the WaSH challenges facing communities within the Pacific are intensified by climate change (Meehl 1996, Hay and Mimura 2006). Climate projections for the South Pacific are more variable than for many other parts of the world, but there is a high likelihood of wetter wet seasons, drier dry seasons and more frequent and severe climate events such as floods and droughts (IPCC 2014). The relationships among climate change, water availability (and accessibility), water quality and sanitation practices underpin the need for climate-sensitive WaSH service delivery (Rasmussen et al. 2009, Hadwen et al. 2015).

The Solomon Islands is one of the PICs that failed to meet the Millennium Development Goal (MDG) target for WaSH (Goal 7c, WHO and UNICEF 2017). Rural areas remain drastically underserviced, with only $61 \%$ of the rural population reporting use of improved drinking water sources and just $18 \%$ of the rural population reporting use of improved or shared sanitation services (WHO and UNICEF 2017). On-going scrutiny indicates that even these statistics may overestimate the consistent use of adequate drinking water and sanitation (Onda et al. 2012, Martinez-Santos 2017, Anthoj et al. 2019). Despite substantive investment and activity, these levels of service remained unchanged over the MDG period (WHO and UNICEF 2017), in part because of a 2.6\% population growth rate (UNPD 2014). Both urban and rural populations grew substantially in the Solomon Islands - for rural areas, the population rose from 412,000 in 2000 to 584,000 in 2015 (UNPD 2014).

A wide variety of water sources are used by rural floodplain communities, including rainwater collected by individual households, commonly captured using the household roof, and stored in small volume containers such as pots and pans (Elliott et al. 2017). Households often heavily rely on their own shallow well next to the house, hand dug into permeable sediments (primarily sand and other unconsolidated soils) and accessing brackish coastal groundwater, which is reported as salty to taste and growing saltier with the well's proximity to the coast. External organisations have attempted to supplement these household sources with alternatives for community use, including larger rainwater tanks and deep wells. Communal sources require collection and transport to the household in containers, and are in theory available for anyone in the community to use. However, communal sources are often not shared equitably among all community members, even during periods of water scarcity or water contamination (Elliott et al. 2017). The effectiveness of locally managed communal water sources is not well understood in the Solomon Island communities, and can vary from a "first-come, first-serve" system, to management where village chiefs and leaders dictate the terms of its use. In terms of other sources of available water, some communities access springs, rivers and streams, which are sometimes piped closer to a community for convenience (Elliott et al. 2017). Many such surface water sources are considered high risk by the United Nations and World Health Organization for contamination by both biological and chemical pollutants (Sachs et al. 2019). Water (bottled or bulk) is rarely purchased by rural community members (Elliott et al. 2017).

Multiple sanitation methods are used in rural floodplain communities in the Solomon Islands. Traditionally, open defecation is practised in rivers and streams, in the ocean, or on the beach at low tide; in fields and in the forest and undergrowth (MHMS 2014). Non-traditional types of sanitation (often termed "improved sanitation") have been introduced by external organisations, including bucket-style toilets (the contents of which are then disposed of in the

traditional defecation sites), pit latrines and pour flush and flush toilets (MacDonald et al. 2017). Concerns over the use of pit latrines and unlined septic tanks have been raised about the concurrent use of groundwater and the potential for contamination (Back et al. 2018). Additional research is still needed to determine the effects of contextual variables on groundwater contamination risks from latrines, improved measurement approaches and better criteria for siting pit latrines (Graham and Polizzotto 2013).

In response to low levels of WaSH service delivery, the Solomon Islands Rural Water Sanitation and Hygiene ("RWASH") Policy, endorsed in 2014, emphasised sustainability, the need for sectoral reform and capacity building to enhance coordination at all levels of government, and increased support for community WaSH management (MHMS 2014). The policy also revolves around the changing function of RWASH from implementation to regulation, whereby the task of implementation is intended to be transferred to nongovernmental organisations (NGOs) and other agencies (MHMS 2015).

Decision making around WaSH in PICs is complex, as there are multiple water-related hazards faced by communities, and the impacts of these will likely be exacerbated by anticipated changes to climate, weather and development (Hadwen et al. 2015). Analysis of these impacts, hazards, and determination of strategies for adaptation is urgently needed. The development of quantitative WaSH models, which can handle the challenges of high uncertainty and data-scarcity, can aid in the decision making around WaSH interventions and climate change adaptation options. The research objective was to improve understanding of how WaSH works in understudied flood-prone rural communities, with a specific focus on: (a) accounting for the complex relationships between multiple water sources and sanitation types, where previous research has often focused on the primary version of each; (b) exploring the potential impact of climate change; and (c) showing which factors and decisions stakeholders implementing WasH programs (including government agencies and NGOs) and the

communities themselves should focus effort on increasing resilience of WaSH systems. In this paper, we describe how WaSH understanding was improved through the participatory development and application of a Bayesian Belief Network (BBN) model. A BBN is a type of system model that is particularly suited to using sparse data and handling uncertainty to address the issues of multiple complex hazards, and is increasingly being used in the context of WaSH (e.g. Dondeynaz et al. 2013, Phan et al. 2016, Giné-Garriga et al. 2018, RequejoCastro et al. 2019). An extensive background to Bayesian modelling is provided in Korb and Nicholson (2004). In this instance it is used to support decision making to increase the availability of safe drinking water in rural communities in the Solomon Islands. The model employs data on multiple water sources and sanitation types from five communities that experienced water shortages as a result of overland and/or coastal flooding. Data from communities in two provinces populate the model, expanding its scope of application to assess safe drinking water availability in different Solomon Island contexts. Critically, the BBN offers a systems view such that it can take into consideration complex water and sanitation systems, and their connections to and across atmosphere (e.g. climate and weather), hydrosphere (e.g. water sources), lithosphere (e.g. hydrogeology of permeable coastal sediments) and anthropospheric behaviour and decision-making. Such a tool is intended to provide insights into the anticipated consequences of climate change and the impacts of extreme events like floods and droughts.

# 2 Methods 

Our approach in this study, which underpinned the process of BBN model construction, was based on a general risk assessment process (illustrated in Supplementary Figure 1) as is used in many fields where there are multiple, difficult to manage risks (e.g. see Aven 2016 for a review). This process fits into an adaptive management cycle, where the recommendations

from the participatory process and risk characterisation modelling lead to management actions which are monitored for the updating of analyses and future rounds of risk characterisation.

# 2.1 Participatory problem formulation 

Five communities that had previously been affected by flooding were selected for survey and focus group sessions, and the most accessible of these was chosen for a more involved multistage participatory process. Community selection was based on recommendations from the Solomon Islands RWASH team within the Ministry of Health and Medical Services who were able to provide a list of communities that had been affected by recent flood events and that were in need of further WaSH development. Communities that were selected had struggled to access acceptable drinking water sources during recent floods, either through perceived or real contamination, or loss of access. For practical access, the communities were located in the two central Provinces of the Solomon Islands, Guadalcanal and Malaita.

Of the five communities participating in this study, two were on Guadalcanal (Suaghi and Verahue) and three were on Malaita (California, Radefasu and Aifera). Although all were rural, those on Malaita had less access to the large markets and shopping centres of Honiara, the capital, than those on Guadalcanal. All work conducted with the communities occurred through the use of local intermediaries and interpreters, with responses and discussions recorded, translated verbally on the day and also noted in English by the research team.

Introductory meetings were held with community leaders, who extended open invitations throughout each community to sessions introducing the project and team. At the end of these introductions the gathered community group were prompted to consider amongst themselves who they would like to participate in further focus group discussions about water and sanitation practices in their community. The focus group discussions however were explicitly

open to anyone interested, with the number of people attending varying according to the popularity of the topics and the availability of local people. Typically, groups ranged in size from 5 to 20 people.

In all communities, an initial problem formulation activity was run with participants to ensure relevance and determine the priority value (measurement endpoint) of the project. Male and female participants were consulted separately throughout the process to respect local cultural norms, avoid gender bias and ensure that the views of all community members could be canvassed. The researchers used participatory mapping exercises of the local area to initiate thinking and discussion around where, why and how water was used, which was repeated for where, why and how sanitation occurred. This information then informed community focus group discussions which sought to list and prioritise water values with discussion and consensus building around the key values that participants considered requiring better management. Across all communities, this process led all community groups to identify their priority concern as drinking water, both in terms of quality and quantity. The focus and measurement endpoint for the model was defined as "proportion of (each) community with sufficient drinking water of acceptable quality", as perceived by community members and reported during the household surveys and focus group discussions. With this endpoint defined, community members identified and ranked threats affecting the community selected measurement endpoint and then crystallized their own thinking as well as that of the researchers by creating causal diagrams demonstrating their mental (conceptual) models around what affected water use and sanitation in the local context (see Supplementary Figures 2-4).

# 2.2 Risk analysis: development of community-level models 

To assist in the development of the BBN models, quantitative WaSH data was collected directly from the five communities through household surveys. The survey methods,

implementation and detailed data analyses are described elsewhere (MacDonald et al. 2016, Elliott et al. 2017). 106 household surveys were conducted across the five communities to gather primary data concerning water sources and sanitation systems and their usage, seasonal (wet, dry) changes and extreme weather events (floods, tropical cyclones and droughts). Note also that although droughts are currently rare in all of the communities, we wanted to capture community experience with water scarcity as this is important to consider given increased likelihood of extended dry spells associated with climate change. The survey questions and the participatory elicitation activities facilitated the collection of data on community WaSH behaviour and how it varied according to a) seasons, b) extreme events, c) sanitation systems, d) multiple sources of water, and e) other contamination concerns.

As with most modelling approaches, expert judgement is often part of BBN development; however BBNs make the expert contribution explicit and transparent, and combine expert judgement with significant stakeholder input (Kuhnert et al. 2010, Moglia et al. 2012). In our study we couple quantitative data collected from the household surveys with qualitative social, cultural and environmental knowledge gathered through focus group discussions and participatory processes. Household surveys were conducted by local enumerators, who attended two full days of training followed by field piloting the survey in Nomoliki, a periurban community of Honiara. Further details on the household survey can be found in two previous, open-access publications (MacDonald et al. 2016, Elliott et al. 2017).

# 2.2.1 Conceptual modelling and quantification 

The data collected from each community was the starting point for the construction of BBN models, including: community mapping; ranked lists; conceptual diagrams for community drinking water supply (e.g. different water sources), how threats affected different individual water sources (e.g. the types of contamination affecting wells vs rainwater tanks), the types of sanitation used and what factors influenced sanitation behaviour (e.g. extreme events); and

field notes on the discussion accompanying community development of this data. The research team also brought expertise and understanding of integrated water resource systems from around the world (e.g. Chan et al. 2010, Hoverman et al. 2011, Cumming et al. 2014, Hadwen et al. 2015, Fisher et al. 2016, MacDonald et al. 2016, Phan et al. 2016), as well as analyses of the data from the household surveys (Özdemir et al. 2011, MacDonald et al. 2016, Elliott et al. 2017), allowing refinement and combination of the community conceptual diagrams and causal influences into an overall systems diagram of water and sanitation at the community scale (Figure 1).
![img-1.jpeg](img-1.jpeg)

Figure 1. Solomon Islands drinking water conceptual diagram (with Community and Region).

The drinking water conceptual diagram developed (Figure 1) was used as the structure of the BBN model. The network structure was input into the modelling software Netica (version 5.15, Norsys 1997). The raw household WaSH survey data was used for network learning using the expectation-maximization algorithm, which was the most appropriate learning approach given the heterogeneity of the data set (e.g. the sparseness of some parts of the data

relative to others, such as drought not having been experienced in some communities), and resulted in the working BBN presented here (e.g. as per Lauritzen and Spiegelhalter 1988, Korb and Nicholson 2004, Fisher et al. 2015).

The model includes different water source and sanitation types reported in the floodplain communities surveyed, effects of season and extreme events, and shows differences between regions and communities. The water sources included were: private/household level rainwater collection, public/communal rainwater collection, private/household well, public/communal wells, rivers and streams, springs, "standpipes" which are sourced from surface waters including rivers/streams and springs, and bottled/purchased water. The sanitation types were: flush toilets, pour flush toilets, and pit latrines ("improved" types); as well as open defecation in oceans, rivers and streams, on the beach, in the fields, in the "bush", and in a "bucket", after which faecal waste is disposed of in the open. Drinking water quality determinants, as perceived by the local people, included both the impact of sanitation type (with risk of human faecal contamination) as well as other types of contamination (e.g. salinity linked to saltwater penetration in groundwater). While direct analysis of water quality and quantity would help to explore health risks, this work lay beyond the scope of this study. Instead, the focus here was on community-based concerns around water quality and quantity, across multiple sources and resulting community decisions. Overall, there were 22 variables/nodes (each with between two and ten possible states), and 82 causal links (relationships) between the variables that were based on the community focus group discussions and conceptual modelling. This model structure results in a total of 41,126 conditional probabilities which were trained with the household survey data.

A simple holdout validation was used, partitioning the dataset into a randomly selected $75 \%$ subset of the data that was used to train the network, with the remaining $25 \%$ of cases reserved for testing the model predictions. Note there is no set rule for validation partition but

proportions used commonly range from 90:10 to 70:30 (see Kuhn and Johnson 2013 for further discussion). The results of the validation are described in section 3.1. The finalised models were then used to gain a quantitative understanding of the integrated WaSH system, and in particular, allow exploration of common scenarios relevant to water resource management and the interventions that might most powerfully mitigate the threats to drinking water in these communities.

# 2.3 Characterisation of risks: model analysis 

### 2.3.1 Sensitivity analysis of the model

A sensitivity analysis was performed on the learned network by calculating reductions in Shannon's entropy (also known as the "mutual information") as described by Pearl (1988) and as determined within Netica (Norsys 1997). This analysis determines how much the uncertainty in the endpoint is reduced after gaining information regarding each state of every other variable. The variables in the network with the most influence on the endpoint condition can thus be identified.

### 2.3.2 Applying scenarios to the finalised BBN model

BBNs are excellent models to use for decision support purposes, as they enable scenario testing while explicitly handling uncertainty (Castelletti and Soncini-Sessa 2007, Phan et al. 2016). Given the number of variables (22), states (69), and relationships (82) in this BBN model, there is an unwieldy number of potential scenarios. This was reduced to consider those scenarios likely to pose the greatest risk to acceptable community drinking water, as informed by analysis of the household data collected (Elliot et al. 2017), stakeholder interest (Supplementary Table 1) and suggestions, as well as the sensitivity analysis.

Initial model development, proposed scenarios and results were presented to external (noncommunity) stakeholders (including those implementing WaSH programs in rural

communities) in Honiara in March 2016. While not all invited stakeholders were able to attend this event (see Supplementary Table 2), there was strong engagement and representation across health and climate adaptation stakeholders from Solomon Islands Government, UNDP and NGO bodies. The preliminary results presented included example outputs (e.g. a drought scenario given recent El Nino projections, the impact of a number of adaptation options identified in previous stakeholder meetings, and comparison of the impact of normal/seasonal conditions vs extreme events). Stakeholders were tasked with ensuring the model and output results made sense to them and were useful, and were given opportunities for clarifications and feedback to inform corrections or adjustments needed (flagging of problems, suggestions for improving usefulness, suggestions for preferred visual/other presentation of outputs, and additional scenarios of interest). They were specifically prompted for ways this type of information could support their institutions' decision making for water supply and sanitation improvements.

Feedback from the stakeholders included appreciation of the importance of examining multiple water sources, which they had not seen analysed previously, and the impact of "single technology solutions" such as (communal/public) rainwater tanks vs (communal/public) wells. Communal water sources were often viewed as secondary sources to be used only when household sources had been depleted. In the absence of a piped water source, individual households were responsible for collecting and storing water from various natural sources. Stakeholders requested adjustments to the model such as adding a link between season and the surface water sources (rivers and streams, and springs), and expressed interest in using the model to explore the impact of "software" interventions, such as operations and maintenance training, on proposed interventions.

On the basis of feedback from stakeholders, the selected scenarios and their permutations were simulated using the finalised BBN model to understand the impact on the endpoint

"proportion of (each) community with sufficient drinking water of acceptable quality", as perceived by community members. The following range of water-focused scenarios were evaluated: (1) the cumulative unavailability of water sources under different extreme events, (2) the impact of extreme events on different management options, (3) the impact of sanitation practices on contamination of water sources and (4) the impact of contamination from other sources. This resulted in a final list of 10 sets of scenarios, as presented in Table 1.

# Scenarios 

1. Provision of rainwater tanks, including:
a. Public/communal/shared tanks
b. Private/household tanks
c. Both
2. Provision of wells:
a. Public/communal
b. Private/household
3. Cumulative loss of water source scenario of:
a. Baseline (current conditions)
b. No private rain water tanks
c. No private and no public rain water tanks
d. No rain water tanks and no private wells
e. No rain water tanks and no wells
4. Water treatment, modelled as perceived absence of contamination
a. Contamination (springs)
i. Absence of contaminants
ii. Uniform likelihood of salinity, animal, helminth, other

iii. Helminth only
b. Contamination (private wells)
i. Absence of contaminants
ii. Uniform likelihood of salinity, animal, helminth, other
iii. Individual contaminants
c. Public wells
i. Absence of contaminants
ii. Uniform likelihood of salinity, animal, helminth, other
iii. Individual contaminants
5. Sanitation type
a. improved (all communities baseline): pour flush, pit latrine, flush toilet used (assumes equally likely); other options not used
b. not improved (all communities baseline): not improved options used (assumes options equally likely); pour flush, pit latrine, flush toilet not used
6. Extreme events

Range of each extreme event baseline
a. Baseline
b. No extreme events
c. Flood
d. Cyclone
e. Drought

Testing interventions under a range of conditions/scenarios, i.e. different extreme events
7. Private rain water tanks
a. Baseline
b. No extreme events

c. Flood
d. Cyclone
e. Drought
8. Public rain water tanks
a. Baseline
b. No extreme events
c. Flood
d. Cyclone
e. Drought
9. Both private and public rain water tanks
a. Baseline
b. No extreme events
c. Flood
d. Cyclone
e. Drought
10. As for Scenario 9, but for private and public wells

Table 1. Final list of WaSH scenarios examined to understand impacts on the model endpoint.

# 3 Results 

Figure 2 shows an overall summary of the BBN model trained on the household data. For example, the community variable shows approximately what fraction of total households surveyed were from each community, while the season variable indicates almost half the information elicited from households was conditional on it being during the wet season.

# 3.1 Model testing 

The predictions of the trained model were compared to the data on adequacy of drinking water as reported by households in the $25 \%$ of the household survey dataset reserved from training (shown in a confusion matrix in Supplementary Table 3).

Of the 301 test cases used, there were 274 correct and 27 incorrect predictions, an overall error rate of $9.0 \%$. Although the model was good at predicting when a community judges it has acceptable drinking water ( $2 \%$ error rate), predictions of the conditions under which they judge they have unacceptable drinking water were less accurate. This imbalance is a result of the communities and households experiencing an unacceptable water condition comparatively less often, providing a much smaller dataset with which to train the model for this condition.

### 3.2 Sensitivity analysis

The sensitivity analysis for the model is illustrated in Figure 3, with nodes ranked according to entropy reduction (see Supplementary Table 4, for calculated entropy measures). The most influential variables are nearest the top of the figure, with the length of the bar indicating the variation for the endpoint being in the "unacceptable" state (the longer the bar, the greater the influence on the endpoint of being "unacceptable"). In terms of which factors influence the endpoint condition, differences between community are particularly significant, followed by the influence of sanitation type. Note that community is a latent variable that allows convenient collation of any consistent differences reported in household survey data from those communities.

![img-2.jpeg](img-2.jpeg)

Figure 2. Solomon Islands drinking water populated BBN.

![img-3.jpeg](img-3.jpeg)

Figure 3. Sensitivity analysis showing the potential influence of network variables on the probability (from 0 to 1) that the endpoint "Proportion of (each) community with sufficient drinking water of acceptable quality" was "Unacceptable" (detailed data on mutual information and variance of belief is provided in the supplementary materials, Supplementary Table 4). As for Figure 2, the variables are colour coded according categorisation into water sources (blue), sanitation and related contamination (brown), other contamination (grey), geography (orange) and controlling factors (green).

# 3.3 Model outputs 

### 3.3.1 Impact of extreme events on water sources

Under flood and cyclone conditions, the community participatory activities and household survey data indicate that community members adopt similar behaviours (Figure 4). During these conditions, the focus group discussions with all communities indicates that use of the abundantly available rainwater increases at the same time as surface water sources become inaccessible and/or are perceived to be too contaminated for use as drinking water. Indeed, the BBN model indicates that use of water from rivers and streams decreases from $7.4 \%$ of households under no extreme event, to $1.1 \%$ under flooding, and springs from $41.4 \%$ to

$34.5 \%$, while use of wells, both public/communal and household/private are also reduced from $69.5 \%$ to $50 \%$ for the former, and $55.7 \%$ to $43.1 \%$ for the latter. To offset the loss of surface water sources, rainwater use increases under flood (and cyclone) conditions, with private/household rainwater use increasing by $26 \%$ (from $41.9 \%$ to $67.8 \%$ ), and public/communal rainwater use increasing by $23 \%$ (from $73 \%$ to $96.3 \%$ ). Community focus groups and participatory activities revealed that a certain degree of flooding was often caused by the heavy rains that accompany cyclones. The reported frequency of cyclones in our study communities was comparable to the reported frequency of flooding; however, given the similarity between patterns of water use under flood and cyclone conditions events experienced by all communities, we primarily report on flooding hereafter.
![img-4.jpeg](img-4.jpeg)

Figure 4. Change in use of water sources for drinking under different extreme events.

During droughts the availability and use of rainwater is vastly reduced, with small volume household level collection eliminated rapidly for many households. Larger volume communal and public rainwater collection sources reportedly last a little longer. Additionally, the

likelihood of using unimproved water sources (rivers/streams and springs) increases considerably. Drought data are fewer than for flood and cyclone, as a much smaller proportion of the households surveyed had previously experienced drought, and these were largely from two communities (Suaghi and Verahue).

These model runs highlighted that changes in water source usage (i.e. increase vs decrease) under any particular type of extreme event are very similar for private and public RWT, although there are differences in the magnitude of the change. A similar trend also occurs for public and private wells, in that the direction of change is consistent no matter whether the resource is a private or public water source.

On the basis of the reported behaviours around water source usage, it is possible to examine the impact of increased magnitude of extreme events such as those projected under climate change modelling for the South Pacific (Perkins et al. 2012, IPCC 2014), by modelling scenarios where water sources are completely removed as an informative upper boundary. Under such scenarios, a cumulative total removal of sources following the order of likelihood of each source being used as shown in Figure 4 would result in the proportion of communities with sufficient and acceptable drinking water reducing as shown in Figure 5a for flood and Figure 5b for drought. This pattern of cumulative water source loss is a combination of loss of access and preferences due to values, perceptions of quality and ownership (e.g. private sources are preferred over shared/public sources) rather than only exhaustion of water sources (e.g. smaller RWT sources are exhausted before wells).

![img-5.jpeg](img-5.jpeg)

Figure 5. BBN endpoint (proportion of community with sufficient drinking water of acceptable quality) values if sources cumulatively become "Unused" under (a) a flooding scenario and (b) a drought scenario. Note this scenario assumes bottled water and standpipes are unavailable. The raw data is available in Supplementary Table 5 and Supplementary Table 6.

During floods, the immediate "loss" of "natural" surface water sources, like rivers and streams and springs (due to both inaccessibility and acceptability given contamination concerns), result in a small decline in the availability of drinking water to the community. In contrast, the additional loss of wells, both private and public, results in moderate decline in the proportion of the community with access to acceptable water, despite the fact that public

and private rainwater sources remain. These losses reflect the fact that rainwater collection and storage behaviours in our study communities are not well established to benefit the whole community: for example, public RWTs were often poorly managed, and damaged and without any plans for repair.

During droughts, the rapid depletion of rainwater stores (private and public) as a source of drinking water results in a substantial decline in the proportion of a community with sufficient drinking water of acceptable quality. This is because rainwater is viewed as a superior source of drinking water and rainwater storage volumes (as observed in our study communities) are insufficient to provide drinking water into the dry season or in prolonged drought. Loss of access to drinking water from private and public wells further reduces the proportion of a community with sufficient drinking water of acceptable quality. Interestingly, the loss of private wells has double the impact of the loss of public wells. This difference reflects the community preference for private well water. Private/household wells are usually constructed directly by household members and their immediate connections (neighbours and relatives). Despite this, communities indicated that public/communal wells are usually constructed by external actors (e.g. government or NGOs), and are reported to be deeper and better constructed, providing water for longer under dry conditions. However, community members also report that local hydrogeology is generally unknown and placement of public wells is influenced primarily by other factors (e.g. community politics). As a result, many community members consider the quality of the water from these communal water sources to be poor relative to privately owned and managed wells. While this perception of impaired water quality from public wells may be unfounded, the consistency of this perspective across communities does appear to drive behaviour, and so was an important part of the model.

# 3.3.2 Impact of extreme events on management options 

The SI government's strategy for rural water supply promotes community use of rainwater (MHMS 2014). NGOs have invested and continue to invest in providing rainwater tanks (e.g. ADRA, World Vision). The sensitivity analysis of the model indicates that rainwater is an influential variable affecting the endpoint ("proportion of (each) community with sufficient drinking water of acceptable quality"), with private RWT use being the $4^{\text {th }}$ most influential variable, and public RWT being the $8^{\text {th }}$ most influential variable (Supplementary Table 4, partly illustrated in Figure 3). There is also interest from government and NGOs in assisting rural communities' use of groundwater, typically through deeper and more durable communal wells that are also less vulnerable to surface pollution sources. However, these sources are currently less influential (than rainwater harvesting) on community perceptions of acceptable drinking water supply, with public/communal wells being the $10^{\text {th }}$ most influential variable, and private wells the $14^{\text {th }}$ most influential given the number of wells available at the time of data collection.

To examine the effectiveness of the SI government strategy to increase harvesting and use of rainwater, we investigated the potential impact of RWT interventions through the BBN model during extreme events (Figure 6). In our study communities, public RWT interventions perform better in drought than private RWT, likely because of the larger volumes of public tanks (5000-10,000 L tanks) compared to the small containers used for private rainwater collection. However, despite the larger volumes in the public tanks, there were reports from one community that these did not last very long in times of water shortage due to distribution and hoarding at a household level. These behavioural aspects of water use were incorporated into the design and functioning of the BBN model to reflect community member's realities with respect to the endpoint.

![img-6.jpeg](img-6.jpeg)

Figure 6. Impact of extreme events on proportion of community with sufficient drinking water of acceptable quality and the associated consequences of proposed interventions on the provision of drinking water at the community scale. See supplementary material for raw data, Supplementary Table 7.

# 3.3.3 Impact of sanitation practice 

Sanitation practice was the $2^{\text {nd }}$ most influential variable affecting the BBN model endpoint according to the sensitivity analysis (Figure 3). This highlights the communities' perception and awareness of the degree to which different sanitation practices may impact drinking water sources. The links between practice and expectations are important in considering community outcomes and our examination of the impact of sanitation practices on the drinking water endpoint initially provided a surprising result, with little improvement in the drinking water endpoint when simulating a full "improved" sanitation scenario (i.e. scenario 5a in Table 1, result shown in Figure 7). Further examination under this scenario revealed a

strong provincial difference, with Malaita having a better drinking water condition under unimproved sanitation compared to improved sanitation (scenario 5b in Table 1). Reflection on the study communities highlighted that one Malaitan community (Aifera) has a very high proportion of pit latrines ( $83 \%$ ) while also having a much lower proportion of the community with perceived acceptable drinking water than the other communities. This particular setting appears to be influencing the overall result in the combined BBN model (Figure 7). Notwithstanding this influence on the total model, this result converges with evidence from focus group discussions where communities highlighted their concerns around the design of some sanitation options. For example, some members of the community expressed concern around pit latrines being "bottomless", which would enable sanitation waste to drain into the local groundwater, or contaminate nearby surface waters when overflows occurred during flood events.
![img-7.jpeg](img-7.jpeg)

Figure 7. BBN endpoint values and the impact of sanitation systems, with only Improved sanitation types used (Pour Flush Toilet, Flush Toilet and Pit Latrines used) against Unimproved sanitation types used (open defecation, including "bucket" toilets where disposal is to open defecation areas). See Supplementary Table 9 for raw data.

# 3.3.4 Impact of water source contamination (excluding human faecal contamination) 

Community members also raised concerns around other sources of water source contamination. Communities considered helminths the most pressing contamination concern for springs, while salinity and forms of animal contamination (including animal waste and dead animals), were perceived to be more of a concern than helminths in private wells (Supplementary Figure 5 and Supplementary Table 8). Somewhat counter-intuitively, communities regarded contamination as less of an issue for public wells than for private wells and springs, perhaps due to the fact that public wells are generally not thought of as good enough quality for drinking, and as a result, these aspects of contamination pose less of a threat to health and are rarely contemplated. In addition, some communities are suspicious of the water quality from public wells, and only use this for cooking and non-drinking domestic purposes, despite general acknowledgement that these wells are generally deeper and better constructed. Significantly, when public wells (and rivers and streams) are used for drinking (more so in the dry season) it is for the reason that no other water source is available. In other words, communities set aside their concerns around water quality, when water resources are scarce.

## 4 Discussion

### 4.1 Baseline conditions and water security

Acceptable quantities and qualities of water remain a commonly expressed priority and an ongoing concern for community members in the five Solomon Island communities. Through analysis of the use of multiple water sources (see Elliott et al. 2017), we can use the BBN model presented in this paper to determine the weaknesses in current practice, the possible outcomes of interventions and the likely consequences of climate change on water security. Indeed, our BBN model shows that having multiple household sources of water available

enhances the resilience of rural communities during extreme events and, depending on water quality, can raise the proportion of the community with access to acceptable (i.e. sufficient quantities of perceived safe) drinking water. Few studies have examined the role of multiple sources (but see Özdemir et al. 2011, Paton et al. 2014, Elliott et al. 2017) and our research contributes to the growing evidence base assessing the use of multiple sources in developing countries and a more nuanced understanding of water systems and the resilience of communities to climate change threats (Elliott et al. 2019). Understanding the complexity and patterns of use of multiple water sources represents a new but very important aspect of achieving positive outcomes for remote and rural communities.

It is also important to consider how current practices might affect community health outcomes. Specifically, the reported consumption (without treatment) of surface (river/stream and spring) and groundwater sources during droughts represents a risky practice, whereby community members set aside their concerns around water quality to make up for the shortfall in rainwater availability. Drinking water has the highest likelihood of becoming unacceptable in both quality and quantity during the dry season and especially drought conditions. This is particularly pronounced in remote rural communities where bottled water and standpipes are not available. While it is important to note that information relating to drought represents just $36.7 \%$ of the total household data set and largely comes from just two of the five communities surveyed, the impacts of the growing incidence of dry spells on water sources and the implications for public health warrant more investigation.

In terms of management interventions to develop climate-resilient WaSH systems and services, support for development of better practices around household level rainwater collection, improving both infrastructure and maintenance of tanks, has significant potential given community preference for this source (Elliott et al. 2017). While we can model the anticipated outcomes of interventions, the community response to these interventions requires

further investigation. Although larger volume, communal rainwater collection and storage may provide communities with water for a longer period during dry times, some community members mentioned that during disasters water from the public RWTs was collected by each household and hoarding occurred, with consequences for the equity and sharing of the rainwater resources. The need for behaviour change and a culture of sharing is recognised in the SI government (RWASH) policy (MHMS 2014), which suggests that "rainwater harvesting can provide very good quality water throughout the year provided the system is designed properly and water usage is controlled". Further to this, increasing rainwater collection through infrastructure (rainwater tanks) and behaviour change (e.g. tank maintenance, communal rainwater arrangements) has been the emphasis of many aid endeavours.

# 4.2 Link between sanitation and water systems 

Whilst they are often designed and implemented separately, it is clear from our community participants, our model results and our conceptualisation of WaSH in the Pacific (Hadwen et al. 2015), that water and sanitation systems are intimately linked. Importantly, there is a recognition that some existing sanitation practices can threaten the quality of surface water and groundwater sources in the eyes of community members. Part of the concern here is the style and design of sanitation systems, especially those which are prone to overflows, those located in flood-prone areas, and/or are designed to leak directly into the ground despite limited knowledge about the hydrogeology.

Participant perceptions of "adequate and safe" drinking water and understanding of contaminants are not necessarily aligned with sector understanding of risks, e.g. concern about water discolouration is higher than concern about faecal contamination, reflecting other recent results in PICs (Foster and Willetts 2018). While actual contamination is currently unknown, major factors determining whether pit latrines contaminate water sources are (1)

soil characteristics that enable rapid infiltration with inadequate treatment (e.g. coarse sands, gravels), (2) high local water tables and (3) use of shallow wells (Massoud et al. 2009, Graham and Polizzotto 2013). For the communities in this study, most households reported that they were aware of these contamination risks and their decision making around drinking water sources is strongly influenced by this awareness and perception of risk. These social and behavioural dimensions of water source usage, as built into our BBN model, are vitally important components of the system that ultimately determine the degree to which interventions are successful (Macleod et al. 2007, Clarke et al. 2014, Thomson et al. 2019). To further strengthen both community knowledge and our capacity to evaluate the adequacy of drinking water sources it will be necessary to couple environmental health sampling with community education and awareness campaigns.

Additionally, scepticism toward water quality in public wells was consistent across our communities. There are numerous technical advantages of protected deep wells for sustainable provision of safe drinking water, but the concerns of communities about use of public wells must be addressed if deep well installations are to be accepted and used. Comprehensive water sampling programs focusing on the key indicators of faecal contamination, coupled with community outreach, are essential to both address scepticism about water quality from public wells and provide insight into the relationship between water quality as perceived by the community and the safety of each source.

# 4.3 Future scenarios and the impacts of management interventions 

Beyond immediate WaSH interventions, our BBN model also has utility in analysing future climate scenarios. The risk of saline intrusion and contamination of well water has been reported as a concern in many coastal communities (Ranjan et al. 2006, Talukder et al. 2015) with brackish water present in wells of many of the coastal communities surveyed in this study (unpublished data), and community members report increases in well water salinity

when king tides occur. Aside from the physical changes in water sources, much more work is needed to understand the decision making processes of local people as they respond to losses in the accessibility and/or acceptability of water sources. This is particularly important with respect to droughts in the Solomon Islands, as many communities have very limited experience with extended dry spells and the risks of consuming unacceptable water may have substantial health impacts.

The current emphasis on rainwater harvesting in the Solomon Islands (and elsewhere in the Pacific) marks a change in policy, as previous interventions sought to increase access to groundwater through the establishment of more public and private wells. While properly designed, constructed and maintained sealed wells can be flood resilient and may improve access and perceptions of well water quality (Musche et al. 2018), our communities showed a clear preference for consuming rainwater. Indeed, the development of well resources does not result in significantly increased proportion of the community having access to acceptable drinking water, mostly due to the perceived contamination risks associated with groundwater in the studied communities. It is clear that more work to measure and assess water quality and communicating these findings with local people is an important aspect that may influence decision making and public health outcomes with respect to the patterns well water use (Foster and Willetts 2018, Thomson et al. 2019).

While rainwater collection does appear to be a sensible approach to increasing climate resilience of communities, it is clear from our focus group discussions that there are many problems associated with the management and use of public RWTs. With that in mind, we advocate for the implementation of large household RWTs, with complementary education and training to ensure that the quality of the water remains good and the risks of unintended consequences (like mosquito breeding) are mitigated.

The ultimate outcomes of interventions which increase the use of rainwater through the provision of rainwater tanks combine provision of infrastructure and "software" interventions such as education and training around operation and maintenance, and awareness and processes for on-going funds for sustainable use (e.g. to replace parts which wear out or are damaged). Several researchers have identified the lack of software support as a cause of intervention failure in many parts of the Pacific, including the Solomon Islands (Wohlfahrt and Kukyuwa 1982, Mourits and Kumar 1995, Clarke et al. 2014). While the BBN model developed here is not designed to specifically test the difference in system interventions with or without software support, the effects of failed maintenance or acceptance of infrastructure can be modelled by modifying water source nodes and the levels of use within the community. Further research would be required to estimate the relative losses associated with infrastructure implementation without software support but, as noted by our partners in RWASH, there is growing awareness of the need for engagement and support to sustain the uptake and maintenance of development actions. We note the reality of delivering software is far from simple given low capacity and resources in the Solomon Islands, however there is a growing body of research on community managed systems and the support they need for ongoing success which provide a useful starting point (Quinn et al. 2007, Schweitzer and Mihelcic 2012, Barrington et al. 2013, Behnke et al. 2017, Kelly et al. 2018, Klug et al. 2017, Aleixo et al. 2019).

# 5 Conclusions 

Our findings show that multiple sources of water provide flexibility to the communities under a range of conditions, such as extreme events. Integrating community perceptions of factors affecting drinking water supply and reported behaviours within each community into the model, we show how community members consider sanitation to have the greatest overall

influence on the proportion of community with drinking water of acceptable quantity and quality. Communities perceive rainwater as the most reliable and safe source for drinking water, including during extreme events like floods and droughts. Improved climate resilience can be achieved through greater use of rainwater harvesting, under the proviso that programs supporting rainwater harvesting include:
a) RWT infrastructure to be installed with a suitable technology transfer process to ensure communities understand practical functioning, maintenance and options for repair when needed due to damage or normal degradation;
b) a more socially focused transfer process to facilitate community development of agreed rainwater sharing protocols, clear assignation of responsibilities such as basic cleaning, for minor and major maintenance, and an agreement for how funding of repairs might be shared;
c) agreed disincentives for breaking agreed protocols, for directly causing damage, or other behaviour which negatively affects water availability for others, including removal of use privileges and paying for repair of damage;
d) post-construction support in the form of an on-going contact point or liaison from Government that communities can contact to provide advice and reminders regarding maintenance or repair lessons, and suggestions regarding where parts can be obtained and how much they should cost.

Although this study focuses on rural floodplains in the Solomon Islands, there are many similar communities across the Pacific, especially in Melanesian countries. Although there will be differences in geography, environment, social structure, and other factors, we believe there are lessons and considerations from our participatory model development process which apply across the region. Of particular relevance throughout the region we demonstrate that participatory model development can demonstrate the locally nuanced connections between

behaviour, water and sanitation systems and help prioritise suitable WaSH solutions. These solutions should be viewed in the context of the broader water cycle, incorporating contamination and climate variability. In a region that benefits from development aid and climate and disaster relief support, the use of the BBN to evaluate scenarios and examine potential interventions to mitigate impacts represents a contribution to understanding the climate change resilience of climate-vulnerable communities, like those studied here.

# 6 Acknowledgements 

Funding: This work was funded by the Australian Government, through the Department of Foreign Affairs and Trade (DFAT) Australian Development Research Awards Scheme (http://dfat.gov.au/aid/topics/developmentissues/research/Pages/australian-development-research-awards-scheme.aspx, DFAT agreement number 66471).

The authors would like to thank all of the study participants without whom this research would not have been possible, as well as the in-country enumerators Hilda Rade, Patricia Kennedy and Trevor Palusi for their exceptional work in the field and keen insights into community life. No conflicts of interest are declared. Data supporting the conclusions can be found in the tables and the supporting information, with data from each household survey housed on the project website: http://www.watercentre.org/portfolio/wash-and-climate-change-adaptation-in-the-pacific.

# Declaration of competing interests 

$\boxtimes$ The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.
$\square$ The authors declare the following financial interests/personal relationships which may be considered as potential competing interests:
$\square$

Author Statement
Terence Chan: Conceptualization, Funding acquisition, Project administration, Methodology, Investigation, Data curation, Software, Formal analysis, Visualization, Validation, Writing - Original draft, Writing - Reviewing and Editing. Morgan MacDonald: Project administration, Methodology, Investigation, Data curation, Software, Formal analysis, Writing - Reviewing and Editing. Annika Kearton: Project administration, Methodology, Investigation, Data curation, Writing - Reviewing and Editing Mark Elliott: Project administration, Methodology, Investigation, Data curation, Software, Formal analysis, Writing - Reviewing and Editing. Katherine Shields: Project administration, Methodology, Investigation, Data curation, Writing - Reviewing and Editing. Bronwyn Powell: Conceptualization, Funding acquisition, Investigation, Methodology, Project administration, Data curation, Writing - Reviewing and Editing. Jamie Bartram: Project administration, Methodology, Investigation, Data curation, Writing - Reviewing and Editing. Wade Hadwen: Conceptualization, Funding acquisition, Investigation, Methodology, Project administration, Data curation, Writing Reviewing and Editing.

Graphical abstract

Highlights

- Solomon Islands rural communities use multiple water sources and sanitation types
- Water supply is threatened by aspects of atmosphere, hydrosphere and lithosphere
- Drinking water choices provide resilience and are part of the anthroposphere
- A model integrating threats and water resource arrangements supports decisions
- Improving rain harvest capacity provides most additional climate change resilience