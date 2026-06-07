# Evaluating multiple bioclimatic risks using Bayesian belief network to support urban tree management under climate change 

Kim, Yoonjung; Park, Chan; Koo, Kyung Ah; Lee, Myung Kyoon; Lee, Dong Kun

Published in:
Urban Forestry \& Urban Greening

Link to article, DOI:
10.1016/j.ufug.2019.05.016

Publication date:
2019

Document Version
Peer reviewed version

Link back to DTU Orbit

Citation (APA):
Kim, Y., Park, C., Koo, K. A., Lee, M. K., \& Lee, D. K. (2019). Evaluating multiple bioclimatic risks using Bayesian belief network to support urban tree management under climate change. Urban Forestry \& Urban Greening, 43, Article 126354. https://doi.org/10.1016/j.ufug.2019.05.016

[^0]
[^0]:    General rights
    Copyright and moral rights for the publications made accessible in the public portal are retained by the authors and/or other copyright owners and it is a condition of accessing publications that users recognise and abide by the legal requirements associated with these rights.

    - Users may download and print one copy of any publication from the public portal for the purpose of private study or research.
    - You may not further distribute the material or use it for any profit-making activity or commercial gain
    - You may freely distribute the URL identifying the publication in the public portal

    If you believe that this document breaches copyright please contact us providing details, and we will remove access to the work immediately and investigate your claim.

# Evaluating multiple bioclimatic risks using Bayesian Belief Network to support urban tree management under climate change 

## Abstract

Understanding the vulnerability of trees affected by climate change is a key requirement for identifying management priorities and suggesting suitable urban tree species. To measure such vulnerability under changing climate conditions, indicators of bioclimatic characteristics should be identified and evaluated using past and current geographic growth ranges. However, although climate events often occur simultaneously (e.g., frost and drought), and management issues in this regard need to be clarified, it is challenging to consider multiple risks in a climate change vulnerability assessment. Therefore, we applied a Bayesian belief network (BBN) to interlink the bioclimatic requirements of species and seasonal climate risk of the study site to comprehensively assess the multiple risks. In particular, we integrated expert knowledge and supporting evidences from relevant studies to construct the BBN. The developed BBN revealed vulnerability to frost considering occurrences of cascading and co-occurring climatic risks such as warmer winters and droughts throughout the phenological cycle. As a case study, two tree species, Zelkova serrata and Camellia japonica from Seoul, Republic of Korea, were evaluated. Among the climatic risks considered, the BBN revealed that shortened frost hardening and the occurrence of spring frost right after an extraordinarily warm winter would mainly affect vulnerability to frost of the two species. In particular, C. japonica had high vulnerability due to its high susceptibility to coldness, though growing temperature will be perfectly satisfied under climate change. Generally, this study provides insights to consider multiple bioclimatic risks for guiding urban tree management under climate change.

Keywords: Bayesian belief network; Bayesian Network; climate change vulnerability assessment; seasonal climate impact; multiple bioclimatic risk; urban tree management

# 1. Introduction 

Changing climate has modified the vegetation composition and biodiversity in many regions (Kareiva et al., 1993; Skov and Svenning, 2004; Woodward, 1987). In particular, an increase in extreme weather events, such as severe frost and drought, has negatively affected climate-sensitive plants (IPCC, 2014). However, plant species provide multiple ecosystem services and biodiversity conservation, which are necessary for human well-being (Roloff et al. 2009). Accordingly, understanding the effects of climate change on plants and how plants respond to changing climates is required for the effective management of trees to maintain ecosystem services.

Describing the climatic niche of species has been fundamental in ecology and has received renewed attention to assess the impact of climate change on species distributions (McKenzie et al. 2003). Based on the geographic growth range, the species-specific climate niche (e.g., temperature range for growing season on target species) can be estimated, and has enabled the prediction of vulnerability affected by climate change (Al-Qaddi et al. 2016, Hellmann et al. 2016, Deb et al. 2017, Barbosa 2016). The identified bioclimatic requirements cannot exactly predict future tree mortality, since it is difficult to fully consider the adaptive capacity of target species. However, they can estimate the potential risk that may occur, based on deviation from the past growth range. To evaluate such risks, advanced models such as generalized linear models and random forest have been applied (Koo et al. 2017). Nevertheless, it is still challenging to jointly consider multiple bioclimatic hazards and complex seasonal risks under climate change, which restrict the identification of effective management priorities (Barry and Elith, 2006).

Moreover, trees exhibit a fatal response to changing climate when multiple bioclimatic risks occur simultaneously or sequentially (Anderegg et al., 2012; Breshears et al., 2013; Manion, 1981; McDowell, 2011). Previous research identified that combined climatic events decreased the capacity of trees to adapt to a changing climate. For example, an analysis of long-term species data from 1993 to 2012 in a temperate climate showed that late spring frosts followed by early spring and a warm winter increased tree mortality (Augspurger, 2013). Drought stress in interactions with other extreme climate events also increased tree mortality. Early spring, severe frosts, and droughts synthetically decreased the growth of vegetation, which resulted in a decrease in net primary productivity (Arnold et al., 2014).

That is, consideration of interactions between extreme events and the response of trees along with seasonal change is critical for suitable tree management. Therefore, consideration of simultaneous occurrences regarding multiple impacts is required, to improve the predictive power for future bioclimatic responses and promote suitable urban tree management (Case and Lawler, 2017).

There are limited methodologies that account for cascading and overlapping climatic impacts to systematically reflect the overlapping occurrence of bioclimatic factors. The Bayesian Belief Network (BBN) - so called Bayesian Network- has been known for its advantages in systematically combining all available information by structuring a causal probabilistic network among multiple kinds of evidence and knowledge (Barton et al., 2012). In particular, BBN is known for its usefulness as it (i) reflects the complexity of an ecosystem by flexibly illustrating a network among factors, (ii) applicable for data-rich and data-poor conditions, and (iii) incorporates diverse knowledge by reflecting the opinions of experts and other stakeholder (Mccann et al., 2006). BBN ultimately supports strategic decision making for environmental management and modeling by graphically expressing complex relationships in an ecosystem (Mccann et al., 2006, Barton et al., 2012). Specifically, the BBN associates variables via conditional probability distributions and uses inference algorithms using Bayes' law to calculate posterior probabilities of the outcome states. The BBN, with a structured framework for combining the diverse risks of an ecosystem, could be useful to consider coincidental climatic impacts by linking bioclimatic factors as a network. Therefore, in this study, an analytical framework applying the BBN was developed to reflect the occurrence of multiple bioclimatic risks in a climate change vulnerability assessment for individual tree species. Based on expert knowledge and related known information regarding previous studies, we developed the BBN to reflect multiple risks to assess vulnerability to frost. Identified risks and their chronological sequence in a temperate climate were investigated for Zelkova serrata and Camellia japonica, one of the most widely used street trees in urban areas, as a case study. We expect that the suggested methodology and results will provide insights to consider multiple impacts of climate change for supporting effective tree management.

# 2. Method 

In this study, a BBN was developed to reflect multiple bioclimatic impacts in a

climate change vulnerability assessment. The BBN can be constructed by defining and linking a set of nodes including the parent (i.e., variable set by user with no external influences) and child nodes (i.e., variable that is conditional upon the values of its parent nodes) (Webster and McLaughlin, 2014). Here, to reflect multiple risks, we defined a node as an individual climatic risk (e.g., the occurrence of drought), and the linkage of nodes represented the cascading and simultaneous occurrence sequence of such individual risks (Fig. 1). Conditional probability tables were generated regarding the rate of occurrence of simultaneous impacts. Overall, nodes and linkages were identified based on expert knowledge and documented knowledge regarding relevant studies. To develop the BBN, $Z$. serrata and C. japonica, two widely planted urban tree species in Seoul, were evaluated as a case study.

# [Figure 1] please refer to the back page of this manuscript 

### 2.1. Study site and species for case study

The study site was Seoul, the capital city of the Republic of Korea, which has a temperate climate with four distinct seasons. The yearly mean temperature of Seoul is $12.5^{\circ} \mathrm{C}$. The mean temperature in August (summer) is $25.7^{\circ} \mathrm{C}$, and mean temperature in January (winter) is $-2.4^{\circ} \mathrm{C}$, which shows extreme temperature differences (Korea Meteorological Administration, www.kma.go.kr). The modeled species for case study are Z. serrata -zelkova serrata- and C. japonica -camelia japonica-, which are the major tree species of the Republic of Korea and are widely distributed over the Korean Peninsula. The two species were selected, as those were one of the most frequently used street trees in urban areas having higher economic importance. Two species can be found in study site, but show different distribution range across Republic of Korea.

### 2.2. Data

To consider climatic hazards that could occur based on a business-as-usual state, climate projection from the RCP 8.5 scenario was evaluated. The RCP scenarios predict future climates depending on actions to curb greenhouse gas emissions according to changes in policy and the level of anthropogenic impacts (Symon, 2013). RCP 8.5 reflects high levels of global warming, which hypothesizes high future demand for energy (Deb et al., 2017; Moss et al., 2010). We used climate data projected by the HadGEM3 model, which was developed by the Met Office Hadley Centre. In particular, an official national downscaled

regional climate model, HadGEM3-RA (Korea Meteorological Administration, www.kma.go.kr) with a $1 \times 1 \mathrm{~km}$ spatial resolution, was used to reflect climate variations on the Korean Peninsula. Data for the current and past climate was obtained from the Korea Meteorological Administration, including meteorological observatory data (Korea Meteorological Administration, www.kma.go.kr).

Species occurrence data was acquired from the Third National Ecosystem Survey conducted by the Ministry of Environment of the Republic of Korea (www.me.go.kr) from 2006 to 2012. For the WI, based on expert's interview particularly regarding the heat requirement of a species that was distributed beyond the Korean peninsula, we considered the natural distribution range of the species studied by Yim and Kira (1991) regarding the wide range of the heat requirement of the species studied (S1).

# 2.3. Development of a Bayesian Belief Network (BBN) 

### 2.3.1. Selecting and linking indicators

[Table 1] please refer to the back page of this manuscript
Expert knowledge was integrated for selecting, confirming and linking the nodes. Five experts (local managers and scientists) with a minimum of 20 years' experience on tree management were individually interviewed for the indicator selection on main bioclimatic risks and its confirmation. Furthermore, plant's annual phenological cycle (Burton and Cumming 1995), and the relevant researches clarifying bioclimatic requirements of trees, Yim and Kira (1975), Cannell and Smith (1986), Prentice et al. (1992), Urban et al. (1993), Burton and Cumming (1995), McKenzie et al. (2003), Skov and Svenning (2004), Schwartz et al. (2006), Normand et al. (2007), McDowell et al. (2008), Nitschke and Innes (2008), and Arnold et al. (2014), were considered to identify the nodes (Table 1).

In specific, based on the plant's phenological cycle from Burton and Cumming (1995) and relevant research, we identified general bioclimatic requirements of tree species as an indicator: thermal requirement for the growing season (Warmth Index; WI), chill requirement for adequate frost hardening (Chilling Requirement; CR), and optimum minimum temperature in winter (Minimum Temperature; MinT). Furthermore, based on expert's opinion, not only species bioclimatic requirements (WI, CR, and MinT), but also risks of occurrence on spring drought (SD), extra-ordinary warmer winter (WW), and spring frost (SF) were regarded as a node in BBN.

knowledge and relevant studies demonstrating such linkages. In summary, major risks were identified as frost that occurs in winter and spring. The nodes were linked to discern "vulnerability to winter frost" and "vulnerability to spring frost." Specifically, the following principles were applied:
(i) The most crucial phenological stage was determined to budburst. Trees can be most susceptible in such stage, as the first appearance of spring foliage often has a strong response to temperature change (White et al., 1997; Schwartz et al., 2006). The failure of proper budburst can ultimately impact a species abundance (GRUBB, 1977; Nitschke and Innes, 2008). Therefore, the BBN was structured with a particular focus on the budburst stage, hence the network started with the timing of "after budburst", and the last part of the BBN was concentrated on the timing of "budburst" to measure the risks at bud flushing.
(ii) The major climate risk was investigated as SF, and the related risks that were causally increasing vulnerability were investigated as WW and SD. That is, recent warming in winter often caused earlier bud sprouting, which increased the vulnerability of the following SF. Moreover, not only warmer winter, but also cooccurring drought was observed to increase susceptibility to the occurrence of SF. In line with expert knowledge, Arnold et al., (2014), Augspurger (2013), and Schwartz et al (2006) empirically demonstrated such a mechanism.
(iii) Frost that occurred in winter was also regarded as a major threat prior to SF. It has long been known that if trees are exposed to temperatures below their normal minimum temperature, the distribution of trees may change over time (Sakai and Weiser, 1973; Woodward, 1987; Prentice et al., 1992). Specifically, such a threat can increase when an adequate temperature range in the growing season and appropriate frost hardening period are not satisfied beforehand (Cannell and Smith 1986; Burton and Cumming 1995; Nitschke and Innes 2008). Hence, vulnerability to winter frost was determined regarding multiple impacts related to WI, CR, and MinT.
(iv) This study hypothesized that if the vulnerability to winter frost was high, the subsequent vulnerability to spring frost would increase.

Each indicator was basically classified and ordered based on the chronological order and co-occurring features regarding the above principles (Fig. 2). To constitute the BBN, we used Netica software (www.norsys.com/netica). Though there were several tools for developing the BBN such as Netica, Hugin, xBaies, and JavaBayes, Netica was identified as the most frequently and widely applied tool in ecosystem management (Pérez-Miñana, 2016), because it has the strengths of a user-friendly GUI, computational power, and good performance (Zou and Yue, 2017). Hence, we applied Netica for construction of the BBN.

# Calculating probabilistic suitability of tree species on projected years 

To evaluate species suitability affected by climate change, we quantified satisfaction rate of the species bioclimatic requirement and occurrence rate of extreme climate at the target site. For the climate from current to future (2016-2099), representing climate change, the overall probabilistic suitability value was quantified. This shows the degree of how the projected climate will be suitable for tree growth.

First, species bioclimatic requirements, WI, CR, and MinT, were calculated by comparing species-specific threshold values and the target site's projected climate. Specifically, depending on the geographic range of the target species, threshold values of WI, CR, and MinT were identified as shown in Table 2. Second, satisfaction and dissatisfaction rates of such threshold values of the target site climate were calculated. For instance, when the threshold value of MinT was exceeded in the whole evaluated period from 2016 to 2100, the satisfaction and dissatisfaction rates were quantified as $0 \%$ and $100 \%$, respectively.

## [Table 2] please refer to the back page of this manuscript

The risks on occurrences of warm winter, spring drought, and spring frost were calculated for the parent nodes, WW, SF, and SD. These represent the occurrences of extreme events at the target site for the projected years. As such, the occurrence rate of each event for the evaluated period (a total of 84 years) was quantified. For instance, when spring drought occurred for 2020, 2030, and 2050, the occurrence rate was quantified as $3.6 \%$ ( 84 divided by 3).

### 2.3.2. Generating a conditional probability table to integrate the bioclimatic impact

We generated a Conditional Probability Table (CPT) or link matrix, when multiple nodes were integrated in a causal relationship. We applied two main rationale to integrate the

nodes: 1. conditional probability (\%) for multiple nodes -occurrence rate, satisfaction rate- is quantified; 2. discrete choice -high, middle, low- is made for two discrete nodes, that are vulnerability to winter and vulnerability to spring frost. Expert knowledge was applied to identify the discrete nodes.

# 2.4. Sensitivity analysis 

We applied the entropy reduction (mutual information) function in Netica to evaluate the node with greater influence on the target nodes "vulnerability to winter frost and spring frost" in the case of the two species. The entropy reduction (mutual information) function, which is symmetric between nodes, indicates how much of the variation on the target node is explained by the rest of the nodes in the network (Pearl, 1988; Dlamini, 2010), hence it indicates which part of the network most affects the target node (Norsys Software Corp, 2012). As such, for the model evaluation process, the function was applied to identify the most influential factors.

## 3. Results of the case study

### 3.1. Projected climate change of the study site

Climate projection shows that the study site would experience a constant temperature increase during the growing season, $11 \sim 33^{\circ} \mathrm{C}$ (monthly mean temperature from April to September). Coldness in winter would show high variability, ranging from $-15 \sim 9.5^{\circ} \mathrm{C}$ (minimum temperature from December to January). The risk on extreme climate, including WW, SF, and SD in Seoul, was highest for WW, and $48 \%$ of the projected years showed the mean daily temperature of early spring exceeding its mean daily temperature of the past 30 years (Table 3). The spring frost and spring drought was projected to occur at $24 \%$ and $35 \%$ until 2099, respectively (Table 3).
[Table 3] please refer to the back page of this manuscript

### 3.2. Evaluated management priorities for target species

Risks on bioclimatic factors were identified for the study site and target species (Table 3). By constituting the conditional probability table (CPT) depending on Bayes rule, the rationale to combine the values on individual risks identified in Table 3 was determined

As a result, two BBNs were generated as shown in Fig. 3. In the growing season for Z. serrata, the results showed that the required optimum range for growing temperature will be unsatisfied for $38.1 \%$ until 2099 (Fig. 3). In comparison, since C. japonica had a broader threshold range for growing temperature, especially high temperature (Table 3), it showed $100 \%$ satisfaction until 2099 (Fig. 3). Therefore, by comparing the current growing temperature range with projected climate, it shows that high temperatures in the growing season should be carefully managed for Z. serrata.

We hypothesized that if the vulnerability to winter frost was high, the subsequent vulnerability to spring frost would increase. The evaluated satisfaction rate on CR and MinT indicated that cautious supervision on coldness is necessary, especially for C. japonica. That is, Z. serrata and C. japonica presented similar dissatisfaction rates to the frost hardening requirement, $59.5 \%$ and $60 \%$, respectively (Fig. 3). However, C. japonica showed high vulnerability to extreme coldness; $79.1 \%$ of the measured years exceeded the species-specific threshold of minimum temperature (Table 3). The constituted BBN model indicated that a lack of satisfaction of the heat requirement, chilling requirement, and limiting minimum temperature would impact vulnerability to winter frost. As such, the vulnerability to winter frost was determined based on the satisfaction condition of child nodes, as illustrated in Tables 4 and S2. Consequently, the highest vulnerability values of Z. serrata and C. japonica to winter frost were $3.67 \%$ and $47.5 \%$, respectively (Fig. 3). That is, Z. serrata distinctively demonstrated a low vulnerability to winter frost. However, C. japonica exhibited a high vulnerability to winter frost because the prior lack of satisfaction of the chilling requirement and limiting minimum temperature reduced its adaptability to winter frost.

One of major climate hazards, vulnerability to spring frost, was evaluated based on the previously defined vulnerability to winter frost and occurrence risks of spring drought, warm winter, and spring frost. In the study site, the results showed that warm winter will occur for approximately half of the projected years (Table 3). However, the occurrence of spring frost immediately after the occurrence of warm winter (cascading occurrence) was about 40\% (S3).

Regarding spring drought, it was estimated that the study site would have a spring drought occurrence rate of around $35 \%$ until 2099 (Table 3). Consequently, vulnerability to spring frost was determined by integrating all the prior responses to climatic events before the stage of budburst (Table 5). C. japonica was analyzed to have a higher vulnerability to spring frost than Z. serrata owing to its low adaptability to coldness. C. japonica was in a high and middle vulnerable state for about $22.5 \%$ of the projected years (Fig. 3). Since spring frost decreased in the future, the projected management requirement for spring frost was lower than the vulnerability to winter frost.

# 3.3. Influence of bioclimatic factors on vulnerability to frost 

The entropy reduction analysis on two target nodes, vulnerability to spring and winter frost, indicates the bioclimatic elements with the greatest influence (Fig. 4). The results for both evaluated species showed that the CR satisfaction rate was the main factor influencing vulnerability to winter frost. As for C. japonica, the dissatisfaction rate of MinT was also an important bioclimatic factor. For the target node, vulnerability to spring frost, the rate of occurrence of spring frost after a warmer winter was the major element that influenced the variance of vulnerability. In the case of Z. serrata, vulnerability to winter frost and occurrence of spring drought were also evaluated to have a greater influence.
[Figure 4] please refer to the back page of this manuscript

## 4. Discussion

Climate change increases extreme weather events, which accelerates the mortality of trees (Bonan, 2008; Kurz et al., 2008). Accordingly, it is necessary to assess how tree species will respond to climate change for effective tree management practices. The vulnerability of vegetation regarding climate change has been quantified mostly based on an empirical relationship between the geographical distribution of species and climate variables, which is called a climatic niche (Hutchinson, 1957; Pearson and Dawson, 2003). However, it has been challenging to reflect co-occurring and cumulative climate risks for evaluating a tree's vulnerability (McDowell et al., 2008, Adams et al,. 2013). Therefore, in this study, an analytical framework based on a Bayesian network was developed and applied, which

identified the priorities of management issues by modeling the occurrence of cascading and co-occurring bioclimatic risks under climate change.

# 4.1. Effectiveness and strength of the BBN to reflect multiple bioclimatic risks 

By reviewing existing applications of BBNs on climate change assessment, Sperotto et al. (2017) identified its effectiveness and strength: it can include multiple stressors or elements with great flexibility. Although few studies have applied the BBN approach to evaluate the impact of climate change on natural resources, most of the applications considered multiple risks (Catenacci and Giupponi, 2013; Dyer et al., 2011; Gutierrez et al., 2011; Kelly et al., 2013; Kotta et al., 2009; Sperotto et al., 2017), as it has the capability to integrate diverse factors based on conditional probability. Accordingly, in this study, multiple factors affecting "vulnerability to winter frost" and "vulnerability to spring frost" were included as a network. We could consider how often multiple bioclimatic risks such as warm winter and spring frost would occur simultaneously under climate change by constituting the BBN based on insights from expert knowledge and previous studies. When we only considered climate risk individually, there was a risk of exaggeration in projecting the vulnerability of trees affected by climate change. The lack of reality in the model could increase the uncertainty (IPCC, 2014). For instance, when we only considered vulnerability to MinT, we could conclude that C. japonica may have a vulnerability rate of $79 \%$ under climate change, which indicated that for $79 \%$ of the projected years it would be vulnerable for proper growth (Table 3). However, not only an individual impact, but also the overlapping impact of multiple stressors should be considered to offer more useful and abundant information that supports urban tree management.

In line with that, multi-risk assessment requires the conceptualization of interactions and processes relevant to an objective (Dawson, 2015). The graphical representation ability of the BBN was a powerful function for conceptualizing the possible relations among nodes, and it helped to systematically understand the confused structure (Aguilera et al., 2011). As a result, the graphical function effectively illustrated what cascading and co-occurring bioclimatic risks could occur, and how they are linked.

### 4.2. Guiding tree management

The network identified among selected bioclimatic risks informed how tree managers can perform proactive monitoring and make preparations to reduce vulnerability under

climate change. Overall, the BBN stressed the importance of monitoring throughout the yearround phenological cycle. As for winter frost, continuous monitoring of heat requirements, duration of chilling and excess of species-specific coldness tolerance are required to be fulfilled. In particular, the results clearly emphasized the risk of occurrence of an inadequate frost hardening period for the two species (Fig 4). That is, an insufficient chilling period due to temperature rise should be monitored as a priority; also, precautionary actions on covering trees should be taken depending on the monitored duration of the chilling period. Specifically, in the case of C. japonica, as susceptibility to winter frost is notably high, damages due to extensive coldness in winter would be continuously problematic, although the temperature range throughout the growing season is adequate. On the other hand, Z. serrata may face increasing heat stress (e.g., leaf scorch) during the growing season (Fig 3), as intense heat would occur, emphasizing the importance of careful measures such as proper watering to avoid heat injury (Roloff, 2016). To reduce vulnerability to spring frost, the occurrence of related risks in regard to an extraordinarily warmer winter and co-occurring drought was evaluated. The results showed that about $50 \%$ of projected years were assessed to have warming in winter, and related occurrences of spring frost and drought were quantified as about $24 \%$ and $35 \%$, respectively (Fig 3). That is, even though mean temperature would increase in winter, trees may face sudden freezing due to an increase in temperature variance (IPCC, 2014). Along with the occurrence of spring drought, monitoring of the duration and rate of warming is required to perform precautionary frost management. As even moderate frost can significantly damage vegetation at the timing of budburst (Schwartz et al., 2006), such a precautious approach is highly required for urban tree management.

# 4.3. Limitations and next steps 

An analytical framework that reflected multiple bioclimatic risks and their causal relation to vulnerability to frost can be applied to other regions or species. However, the duration and sequence of bioclimatic impacts could differ, thus detailed climatic conditions and its network could be modified for each region. Specifically, in this study, representative bioclimatic factors that frequently affect urban trees were primarily selected, which reflected major phenological events and the notable climatic risk of Seoul. That is, we identified and applied several important factors integrating expert knowledge. However, as ecological response can be more complex, and other non-ecological factors (e.g., location of a tree) can affect vulnerability, for further research, more nodes can be identified and applied to develop

the BBN. For instance, management practices such as frequency of irrigation or characteristics of the urban environment can affect the degree of vulnerability. Thus, as uncertainty is present in a vulnerability assessment, an adaptive approach is required to improve the BBN (Landis et al., 2013). That is, improved knowledge and observations of reactions of a system are recommended to be continuously reviewed and applied, as BBN is highly flexible (Sperotto et al., 2017).

Specifically, the BBN is fundamentally limited in considering the dynamic response of trees and feedback loop of the sequence of vulnerability. Compared to a system dynamics model, another model based on a systematic approach that supports causal loops reflecting positive and negative feedback (Reynolds and Holwell, 2010), BBN generally do not assist the dynamics and feedback effects in the system (Sperotto et al., 2017). In line with that, in this study, we posed static assessment, rather than dynamic assessment that reflects dynamic responses reflecting each tree's resilience. Dynamics such as a tree's changing resilience regarding age or management options were not considered in the BBN. Though the dynamic resilience of species to multiple risks is hard to be reflected due to limitations in data availability and limited known information, a feedback loop is often important in ecology (Nyberg et al., 2006; Mccann et al., 2006). Hence, a Dynamic Bayesian Network (DBN) can be considered for analyzing a tree's vulnerability based on multiple impacts, as it supports the function to monitor and update the system over time (Murphy and Russell, 2002). Otherwise, a simple solution can be applied to improve the BBN structure by adding nodes that reflect different types of possible responses to multiple risks.

However, though such limitations exist, this study provided insights to consider multiple chronological impacts in a climate change vulnerability assessment regarding a tree's phenological cycle. There are a lot of possibilities with climate risks and their combinations that affect a tree's adequate growth. The evaluation of such sequences is hardly performed due to difficulties in identifying systematic sequences and collecting available empirical data. In this context, a BBN's advantage in systematically integrating knowledge in data-poor condition and its strength in supporting optimum decision making can be further applied to consider multiple hazards in urban tree management.

Assessments of future impacts of climate change on ecosystems are rapidly developing. However, attempts to consider multiple climate hazards in urban tree management are often a challenge. There should be an attempt to develop methodologies to comprehensively consider each climatic event. In this respect, this study suggested that a BBN could be used as an effective tool to consider multiple climate hazards for a climate change vulnerability assessment. The assessment framework suggested a method to conditionally interlink the suitability of each bioclimatic requirement and risk in the occurrence of simultaneous climatic threats regarding the phenological cycle. Heat requirement, frost hardening, coldness, and major climate risks (e.g., warmer climate in winter) were systematically evaluated as a network. The results of this study identified prioritized management issues such as a subsequent reduction of chilling period and simultaneous occurrence of spring frost after a warmer winter to reduce vulnerability to frost for two species, Z. serrata and C. japonica. Furthermore, we suggested the strengths and limitations of BBN to consider multiple stressors and their complex influence. In the end, even though it is a challenge to apply multiple causal risks along with the phenological cycle in predicting vulnerability to climate change, as precautionary and proactive tree management is required, further consideration and implications are necessary.

# S1. Values of Warmth Index (WI) 


WI (warmth index); min (minimum value); max (maximum value)

# S2. Conditional probability table (CPT) on discrete node 'vulnerability to WF' 

The value on discrete node 'vulnerability to winter frost' is determined based on the conditional relationship between CR and MinT.


WF (winter frost); CR (chilling requirement); MinT (minimum temperature)

# S3. Conditional probability table (CPT) on the node 'occurrences of SF'

Conditional value between occurrences of WW and SF from 2016 to 2099 is illustrated.


SF (spring frost); WW (warm winter)