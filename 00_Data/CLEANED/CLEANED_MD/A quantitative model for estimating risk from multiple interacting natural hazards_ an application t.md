# A quantitative model for estimating risk from multiple interacting natural hazards: an application to northeast Zhejiang, China 

Baoyin Liu ${ }^{1} \cdot$ Yim Ling Siu ${ }^{1} \cdot$ Gordon Mitchell ${ }^{2}$

Published online: 18 April 2016
(c) The Author(s) 2016. This article is published with open access at Springerlink.com


#### Abstract

Multi-hazard risk assessment is a major concern in risk analysis, but most approaches do not consider all hazard interactions when calculating possible losses. We address this problem by developing an improved quantitative model—Model for multi-hazard Risk assessment with a consideration of Hazard Interaction (MmhRisk-HI). This model calculates the possible loss caused by multiple hazards, with an explicit consideration of interaction between those hazards. There are two main components to the model. In the first, based on the hazardforming environment, relationships among hazards are classified into four types for calculation of the exceedance probability of multiple hazards occurrence. In the second, a Bayesian network is used to calculate possible loss caused by multiple hazards with different exceedance probabilities. A multi-hazard risk map can then be drawn addressing the probability of multi-hazard occurrence and corresponding loss. This model was applied in northeast Zhejiang, China and validated by comparison against an observed multi-hazard sequence. The validation results show that the model can more effectively represent the real world, and that the modelled outputs, possible loss caused by multiple hazards, are reliable. The outputs can additionally help to identify areas at greatest risk, and allows a determination of the factors that contribute to that risk, and hence the model can provide useful further information for


[^0]planners and decision-makers concerned with risk mitigation.

Keywords Multi-hazard risk modelling $\cdot$ Hazard interaction $\cdot$ Hazard-forming environment $\cdot$ Bayesian network $\cdot$ Zhejiang

## 1 Introduction

Multi-hazard risk assessment (MHRA) is a major concern in risk analysis and management (Carpignano et al. 2009; Frigerio et al. 2012; Marulanda et al. 2013; Ming et al. 2015). MHRA is a relatively new field, with little MHRA research conducted before 2000, although three recognizable phases in MHRA development can be identified. Initially, research focused on multiple hazards affecting a given area through the development of a synthetic indicator. Examples included the Australian Geological Survey Organisation Cities project (Granger and Trevor 2000), the Natural Hazard Index for Mega-cities (Munich Re 2003), the World Bank's global Natural Disaster Hotspot analysis (Dilley et al. 2005), European Spatial Planning and Observation Network (ESPON's) multi-hazard approach for the enlarged European Union (Schmidt-Thomé 2006), and the Calculation of the Total Place Vulnerability Index for the State of South Carolina, USA (SCEMDOAG 2009). These synthetic indicators are effective in comparing the relative danger experienced by different areas, but give no representation of the real risk situation in those areas-that is, the approach is useful in assessing relative but not absolute losses. To address this problem, research moved from synthetic indicators to assessing integrated losses caused by multiple natural hazards in a given region and time period. This included HAZUS-MH software for Risk


[^0]:    $\boxtimes$ Yim Ling Siu
    Y.L.Siu@leeds.ac.uk

    1 School of Earth and Environment, University of Leeds, Leeds LS2 9JT, UK
    2 School of Geography and Water@leeds, University of Leeds, Leeds LS2 9JT, UK

Assessment in the USA (FEMA 2004), the Regional RiskScape project for New Zealand (Schmidt et al. 2011), and the Central American Probabilistic Risk Assessment Program for Latin America and the Caribbean Region (Linares-Rivas 2012). However, this research still neglected hazard interaction, hence recently, more comprehensive MHRA research was proposed to assess possible loss due to multiple hazards with a consideration of domino effects (Marzocchi et al. 2012, Eshrati et al. 2015). Nevertheless, these studies, which typify a rather small body of MHRA work, are incomplete. The interaction between different natural hazards is complex and dynamic, and only addressing domino effect hazard interaction is not enough to cover all situations. For example, hazards can occur independently without evident common cause, yet in close proximity, spatially, temporally, or both, and thus interact to elevate risk. Thus the incomplete consideration of possible hazard interactions represents a significant gap in MHRA. This paper therefore aims to develop an improved MHRA model, Model for multi-hazard Risk assessment with a consideration of Hazard Interaction (MmhRisk-HI). The model calculates the possible loss caused by multiple hazards, with an explicit consideration of interaction between different hazards.

## 2 Multi-hazard risk assessment

The MHRA process is based on that for single-hazard risk assessment, with its main advance being that it puts different hazard types into a single system for joint evaluation (Armonia 2006; Di Mauro et al. 2006; Marzocchi et al. 2009; Carpignano et al. 2009). MHRA is a relatively new field, with no clear definition, but in principle, it takes into account the characteristics (frequency, magnitude) of each hazardous event, and their mutual interactions and interrelations (e.g. a hazard may occur repeatedly in time; different hazards may occur independently in the same place; different hazards may occur dependently in the same place) (Kappes et al. 2012; Marzocchi et al. 2012). The aim of MHRA is to have a holistic view of the total effects or impacts by assessing and mapping the expected social, economic and/or environmental loss due to the occurrence of all natural hazards in a given area (Dilley et al. 2005; Armonia 2006; Kappes et al. 2012; Komendantova et al. 2014).

A conceptual model for multi-hazard risk assessment is as shown in Fig. 1, based on the disaster formation process (Burton et al. 1993; Shi 1996; Wisner et al. 2004). Natural hazards are natural events that arise from a specific geophysical environment, accompanied by concentrations of energy released to produce major threats to human life or economic assets (McGuire et al. 2002; ISDR 2004). Space,
time, magnitude and frequency are the basic characteristics of natural hazards (Alexander 1993; Smith 2000). The hazard forming environment is the specific geophysical environment that natural hazards arise from, including environmental factors in the atmosphere, hydrosphere, biosphere and lithosphere. These factors are the basic conditions for the occurrence of hazards (Park 1994; Shi 1996; McGuire et al. 2002). Natural hazards are then caused by the substantial departure of one or more environmental factor from their mean values, either in a positive or negative direction. Thus flood can be induced when precipitation is above the normal level, and drought when it is below. Hence, the time, space, magnitude and frequency of hazards are determined by the hazard-forming environment. Some hazards can occur in close proximity, spatially, temporally, or both, in a specific hazard-forming environment. Exposure is defined as the number, type and/or monetary value of elements that are under threat from natural hazards (Alexander 2000; Blanchard 2005; Tong et al. 2009). Vulnerability is broadly defined as the conditions, determined by physical, social, economic, and environmental factors, which determine the potential damage following exposure to hazard (Pelling 2003; Brooks 2003; Ge et al. 2013). The hazards' interaction with vulnerability and exposures can result in losses and impacts of a human, material, economic and/or environmental nature, losses that can be increased if one hazardous event interacts with another (Gill and Malamud 2014). The induced consequence also influences the stability of the hazard-forming environment and the distribution of exposures, whilst the influenced hazard-forming environment has a chance of producing new hazards. This conceptual model provides a theoretical basis for the improved MHRA model (MmhRisk-HI) construction.

## 3 Model construction

### 3.1 Framework

The structure of the MmhRisk-HI model, with its' explicit consideration of interaction between different hazards, is shown in Fig. 2. There are two main components. In the first, the hazard-forming environment is used in hazard identification and hazard interaction analysis to analyse the relationship between hazards and to calculate the exceedance probability of multiple hazards occurrence. The second component focuses on the calculation of the possible loss from multiple hazards with different exceedance probabilities. The methods used for the exposure analysis depends on the scale of the region addressed and the assessment units. A Bayesian network (BN) is used to measure the possible loss ratio (the ratio of total losses to

![img-0.jpeg](img-0.jpeg)

Fig. 1 Conceptual model for multi-hazard risk
![img-1.jpeg](img-1.jpeg)

Fig. 2 Framework of model for multi-hazard Risk assessment with a consideration of Hazard Interaction (MmhRisk-HI)
the total value of the exposure) caused by multiples hazards with different exceedance probabilities, considering the relevant vulnerability indicators in the loss ratio assessment. Finally, a multi-hazard risk map can be drawn addressing the probability of multi-hazard occurrence and corresponding loss.

### 3.2 Calculation of the exceedance probability of multiple hazards

Natural hazards arise from specific hazard-forming environments, with environmental factors in each environment determining the preconditions for hazard occurrence. The hazard-forming environment can therefore be used to identify which natural hazards influence a given area. For example, proximity to a crustal plate boundary is a precondition for an earthquake. Substantial change in one or more environmental factor in a hazard-forming
environment is the main reason that hazards are induced, thus these factors can be taken as triggers for natural hazards and used to analyse hazard interaction. Hazards are thus classified, into four types, according to their trigger factors (Liu et al. 2016), as follows.

### 3.2.1 Independent relationship

The Independent relationship is where there is no evident common cause between two different hazards. This means that changes in trigger factors which induce hazard A are independent of those which induce hazard B. The relationship between these trigger factors and hazards can be expressed by Eqs. (1) and (2), whereby changes in trigger factors $t_{1}, t_{2} \ldots t_{i} \ldots t_{n}$ are independent of changes in trigger factors $t_{n+1}, t_{n+2} \ldots t_{s} \ldots t_{r}$. Therefore, the probability of these two hazards occurring together can be calculated as Eq. (3).

$$
\begin{aligned}
f\left(p_{t_{1}}, p_{t_{2}} \ldots p_{t_{i}} \ldots p_{t_{n}}\right) & =p\left(h_{A}\right) \\
f\left(p_{t_{n+1}}, p_{t_{n+2}} \ldots p_{t_{s}} \ldots p_{t_{i}}\right) & =p\left(h_{B}\right) \\
P(A \cap B) & =p\left(h_{A}\right) \times p\left(h_{B}\right) \\
& =f\left(p_{t_{1}}, p_{t_{2}} \ldots p_{t_{i}} \ldots p_{t_{n}}\right) \times f\left(p_{t_{n+1}}, p_{t_{n+2}} \ldots p_{t_{s}} \ldots p_{t_{i}}\right)
\end{aligned}
$$

where $f$ is the function used to calculate the probability of the change in trigger factors within the brackets occurring together, $t_{i}$ is the trigger factor $i, i=1,2, \ldots n, t_{s}$ is the trigger factor $s, s=n+1, n+2, \ldots t, h_{j}$ is the hazard $j$, $j=A, B, p_{t_{i}}$ is the probability of the change in trigger factor $i, p_{t_{s}}$ is the probability of the change in trigger factor $s$, and $p\left(h_{j}\right)$ is the probability of hazard $j$ occurrence.

### 3.2.2 Mutex relationship

A Mutex relationship is where the changes in trigger factors which induce hazards A and B are mutually exclusive, and so these hazards cannot occur together. The relationship between the trigger factors and hazards can be expressed as:
$f\left(p_{t_{i+}}\right)=p\left(h_{A}\right)$
$f\left(p_{t_{i-}}\right)=p\left(h_{B}\right)$
where $f$ is the function, which is used to calculate the probability of the change in trigger factors within the brackets occurring together, $t_{i}$ is the trigger factor $i, i=1$, $2, \ldots n, t_{i+}$ represents the trigger factor $i$ departure in positive direction from its mean values, $t_{i-}$ represents the trigger factor $i$ departure in the negative direction from its mean values, $h_{j}$ is the hazard $j, j=A, B, p_{t_{i}}$ is the probability of the change in trigger factor $i$, and $p\left(h_{j}\right)$ is the probability of hazard $j$ occurrence.

One trigger factor cannot move in two directions simultaneously, hence, the probability of these two hazards occurring together can be expressed as:
$P(A \cap B)=0$

### 3.2.3 Parallel relationship

Changes in one or more trigger factor may induce more than one hazard $\mathrm{A}_{1}, \mathrm{~A}_{2} \ldots \mathrm{~A}_{m}$ at the same time, that is, the relationship of hazard $\mathrm{A}_{1}, \mathrm{~A}_{2} \ldots \mathrm{~A}_{m}$ is parallel. This relationship between trigger factors and hazards can be expressed by Eq. (7), where hazards $\mathrm{A}_{1}, \mathrm{~A}_{2} \ldots \mathrm{~A}_{m}$ constitute a hazard group, with all hazards induced by the same trigger factor(s). Hence, the frequency and magnitude of this hazard group are determined by changes in the trigger factors, with the probability of the hazard group (hazard $\mathrm{A}_{1}, \mathrm{~A}_{2} \ldots \ldots \mathrm{~A}_{m}$ ) occurring expressed by Eq. (8).

$$
\begin{aligned}
f\left(p_{t_{1}}, p_{t_{2}} \ldots p_{t_{i}} \ldots p_{t_{n}}\right) & =p\left(h_{A_{1}}\right) \\
f\left(p_{t_{1}}, p_{t_{2}} \ldots p_{t_{i}} \ldots p_{t_{n}}\right) & =p\left(h_{A_{1}}\right) \\
\ldots & \\
f\left(p_{t_{1}}, p_{t_{2}} \ldots p_{t_{i}} \ldots p_{t_{n}}\right) & =p\left(h_{A_{m}}\right) \\
P\left(A_{1} \cap A_{2} \cap \ldots \cap A_{m}\right) & =f\left(p_{t_{1}}, p_{t_{2}} \ldots p_{t_{i}} \ldots p_{t_{n}}\right)
\end{aligned}
$$

where $f$ is the function, which is used to calculate the probability of the change in trigger factors within the brackets occurring together, $t_{i}$ is the trigger factor $i, i=1$, $2, \ldots n, h_{j}$ is the hazard $j, j=A_{1}, A_{2}, \ldots A_{m}, p_{t_{i}}$ is the probability of the change in trigger factor $i$, and $p\left(h_{j}\right)$ is the probability of hazard $j$ occurrence.

### 3.2.4 Series relationship

In the series relationship, hazard A induces changes in trigger factors, then the changes in these trigger factors induce hazard B. Hazards A and B are in a series relationship, which can be expressed by Eq. (9). Changes in trigger factors $t_{1}, t_{2} \ldots t_{i} \ldots t_{n}$ induce hazard A , then hazard A changes the trigger factors $t_{n+1}, t_{n+2} \ldots t_{s} \ldots t_{t}$, which then induce hazard B. The probability of hazards A and B occurring together can thus be expressed by Eq. (10).

$$
\begin{aligned}
f\left(p_{t_{1}}, p_{t_{2}} \ldots p_{t_{i}} \ldots p_{t_{n}}\right) & =p\left(h_{A}\right) \rightarrow f\left(p_{t_{n+1}}, p_{t_{n+2}} \ldots p_{t_{s}} \ldots p_{t_{i}}\right) \\
& =p\left(h_{B}\right) \\
P(A \cap B)= & p\left(h_{A}\right) \times p\left(h_{B}\right)=f\left(p_{t_{1}}, p_{t_{2}} \ldots p_{t_{i}} \ldots p_{t_{n}}\right) \\
& \times f\left(p_{t_{n+1}}, p_{t_{n+2}} \ldots p_{t_{s}} \ldots p_{t_{i}} \mid p_{t_{1}}, p_{t_{2}} \ldots p_{t_{i}} \ldots p_{t_{n}}\right)
\end{aligned}
$$

where $f$ is the function, which is used to calculate the probability of the change in trigger factors within the brackets occurring together, $t_{i}$ is the trigger factor $i, i=1$, $2, \ldots n, t_{s}$ is the trigger factor $s, s=n+1, n+2, \ldots t, h_{j}$ is the hazard $j, j=A, B, p_{t_{i}}$ is the probability of the change in trigger factor $i, p_{t_{i}}$ is the probability of the change in trigger factor $s$, and $p\left(h_{j}\right)$ is the probability of hazard $j$ occurrence.

This classification of trigger factors is useful as it helps ensure all possible relationships among hazards are considered. It fills a gap in current multi-hazard methods which to date only consider domino effects, just one type of possible hazard interaction. Based on the four part hazard interaction classification above, the probability of multiple hazards of different magnitudes occurring together can be calculated based on changes in trigger factors, with the degree of change representing the magnitude of hazards, and the probability of change representing the probability of hazards. This can be achieved using a mathematical statistics approach to define a function that determines event magnitude and frequency. For example, Grünthal et al. (2006) calculated exceedance probability-mean wind speed curves for windstorm

![img-2.jpeg](img-2.jpeg)

Fig. 3 Generic Bayesian network framework for loss ratio assessment
magnitude assessment using Schmidt and Gumbel distributions (Gumbel 1958).

### 3.3 Calculation of the possible loss caused by multiple hazards

The second main component of the MmhRisk-HI model focuses on the calculation of possible loss caused by multiple hazards with different exceedance probabilities. This requires exposure analysis, and loss ratio assessment.

### 3.3.1 Exposure analysis

Exposure analysis is used to determine the spatial distribution of elements at risk (e.g. people, infrastructure). This is usually achieved using analysis of data contained in official statistical reports, or that obtained via on-site survey or remote sensing image. These data sources vary considerably in their characteristics: on-site survey data may be very detailed, but generally only exist on a very local scale, as it is time and resource intensive to collect. Conversely remotely sensed images provide wide area coverage, but the raster format means that the information conveyed is more limited in scope. Official statistics data, based on government administrative units, represent a common intermediate point, in terms of functional resolution. The exposure analysis module selects from these sources following a consideration of the study area size, and the data available for that area.

### 3.3.2 Loss ratio assessment

The loss ratio assessment module is used to measure the possible loss ratio for a given exposure, under conditions caused by multiple hazards with different exceedance
probabilities, and then to determine how vulnerability-related indicators (physical, social, economic and/or environmental factors) influence the possible loss ratio. A BN, a probabilistic graphical model that encodes probabilistic interdependencies among a set of random variables (Jensen and Nielsen 2007), is used in this process. A BN is a good method for modelling uncertainties and interactions between related factors (Maldonado et al. 2015), and has previously been applied in risk assessment of earthquake (Bayraktarli et al. 2006), landslide (Straub 2005) and flooding (Li et al. 2010). The two key steps in the BN, discussed further below, are the construction of the BN structure and estimating the conditional probabilities of relationships within the network.

## (1) Bayesian network structure

A BN is a complete model of the system of interest, comprising component variables and the probabilistic relationships between them. In this module, the BN modelling framework is constructed according to domain knowledge (e.g. Alexander 2000; Cutter et al. 2003; Villagran 2006; Schmidt-Thomé 2006). Figure 3 shows that the loss ratio, which is assumed to be a parent node of vulnerability and hazard related indicators, is the root node. Trigger factors are then used to construct the set of hazardrelated indicators which represent the magnitude of multiple hazards. Indicators in economic, social, physical and environmental domains represent the sets of vulnerabilityrelated indicators (Table 1).

Table 1 identifies some possible vulnerability-related indicators, with further details given below:

- GDP/capita: high GDP/capita indicates more economic activity is under threat of hazard events (Blaikie et al. 1994; Schmidt-Thomé 2006).

Table 1: Some possible vulnerability-related indicators


- Income of residents: high income indicates residents have more personal resources to absorb losses and speed up recovery after a disaster (Hewitt 1997; Cutter et al. 2003; SCEMDOAG 2009).
- Population density: high population density indicates more population is under threat of hazard events (Puente 1999; Pelling 2003).
- Gender ratio: females are often more vulnerable than males as they tend to have more limited education, lower income and family care responsibilities (Cutter et al. 2003; SCEMDOAG 2009).
- Age structure: children and the elderly are more vulnerable to hazard than young adults due to their limited physical strength (Cutter et al. 2000; Ngo 2001).
- Telecommunication: high telecommunication capacity supports fast and precise hazard information transmission, thus targeted measures can be adopted quickly (Blaikie et al. 1994; Puente 1999).
- Transport route: good transport infrastructure makes it easier to evacuate people and to distribute emergency rescue and relief materials (Platt 1991; Villagran 2006).
- Medical condition: good medical services ensure wounded people get fast and effective treatment after a disaster, thus the recovery period can be shortened (Morrow 1999; Cutter et al. 2003).
- Social dependency: people who are wholly dependent on social services have very limited personal resources to absorb losses, and require more support in the postdisaster period, thus they are more vulnerable than the employed (Cutter et al. 2003; SCEMDOAG 2009).

Fig. 4 Bayesian network frameworks for loss ratio assessment of multiple hazards with different relationships a Independent relationship, b Parallel relationship, c Series relationship

- Risk perception: this measures an individuals' ability to discern and understand the characteristics and severity of risk from hazard events (Slovic 2000). Understanding risk promotes taking effective measures to cope with disaster, thus people with low risk perception are inherently more vulnerable (Armas 2006; Smith 2013).
- Warning system: a disaster warning system gives early warning to those at risk and promotes preparedness, mitigating against disaster (Zschau and Küppers 2003).
- Institutional preparedness: this comprises regulations or procedures (e.g. emergency response plan) developed to mitigate against potential disasters (Haque 2000; Schmidt-Thomé 2006).
- Educational achievement: higher education levels indicate people can better understand information about hazard events and take more effective measures to cope with disaster (Cutter et al. 2003; SCEMDOAG 2009).
- Technical infrastructure: this indicates presence of facilities needed to respond to hazard events (e.g. fire trucks, steamboats, helicopters). Good technical infrastructure makes it possible to evacuate people and exert more control during a disaster (Schmidt-Thomé 2006).
- Significant natural areas: these areas (e.g. national parks) are considered more vulnerable as they are unique and hard to recover (Schmidt-Thomé 2006).
- Fragmented natural areas: these are vulnerable because nature in larger undisturbed areas recovers faster than that in smaller areas (Schmidt-Thomé 2006).

In this framework, the indicators used to construct vul-nerability-related indicators should be independent. To check for this, factor analysis, a classical statistical method to detect structure in the relationships between variables or indicators, is applied (Russell 2002). Using SPSS statistics software, principal component analysis (PCA) (Jolliffe 2002) is adopted to first make distinct the principal component, and then the varimax rotation strategy (Osborne 2008) is used to calculate the factor loading in each principal component. The factors (vulnerability-related indicators) having the highest loading in each principal component are then selected to construct the BN.

Next, trigger factors are chosen to construct the set of hazard-related indicators which represent the magnitude of multiple hazards. Hazard-related indicators for multiple hazards with different relationships are shown in Fig. 4.

In Fig. 4a, hazards A and B have an independent relationship. The changes in trigger factors $t_{1}, t_{2} \ldots t_{i} \ldots t_{n}$ which induce hazard A are independent of the changes in trigger

![img-3.jpeg](img-3.jpeg)
(3) Springer

![img-4.jpeg](img-4.jpeg)

Fig. 4 continued
factors $t_{n+1}, t_{n+2} \ldots t_{s} \ldots t_{t}$ which induce hazard B. The two trigger factor groups $\left(t_{1}, t_{2} \ldots t_{i} \ldots t_{n}\right)$ and $\left(t_{n}+1\right.$, $\left.t_{n+2} \ldots t_{s} \ldots t_{t}\right)$ can be used to measure the frequency and magnitude of hazard A and B respectively. Hence, the trigger factor group $\left(t_{1}, t_{2} \ldots t_{i} \ldots t_{n}\right)$ is chosen as the hazardrelated indicator to represent the magnitude of hazard A , and the trigger factor group $\left(t_{n}+1, t_{n+2} \ldots t_{s} \ldots t_{t}\right)$ is chosen as the hazard-related indicator to represent the magnitude of hazard B.

In Fig. 4b, hazards $\mathrm{A}_{1}, \mathrm{~A}_{2} \ldots \mathrm{~A}_{m}$ represent a parallel relationship. Hazards $\mathrm{A}_{1}, \mathrm{~A}_{2} \ldots \mathrm{~A}_{m}$ are all induced by the changes in the same trigger factors $t_{1}, t_{2} \ldots t_{i}$. The frequency and magnitude of this hazard group $\left(\mathrm{A}_{1}, \mathrm{~A}_{2} \ldots \mathrm{~A}_{m}\right)$ are determined by the changes in these trigger factors. Hence, the trigger factor group $\left(t_{1}, t_{2} \ldots t_{i} \ldots t_{n}\right)$ is chosen as the hazard-related indicator to represent the magnitude of group $\left(\mathrm{A}_{1}, \mathrm{~A}_{2} \ldots \mathrm{~A}_{m}\right)$.

In Fig. 4c, hazards A and B are in a series relationship. The changes in trigger $t_{1}, t_{2} \ldots t_{i} \ldots t_{n}$ induce the hazard A , then hazard A cause the changes in trigger factors $t_{n+1}$, $t_{n+2} \ldots t_{s} \ldots t_{t}$. The changes in trigger factors $t_{n+1}$, $t_{n+2} \ldots t_{s} \ldots t_{t}$ induce hazard B. Hence, the trigger factor group $\left(t_{1}, t_{2} \ldots t_{i} \ldots t_{n}\right)$ is chosen as the hazard-related
indicator to represent the magnitude of hazard A , and the trigger factor group $\left(t_{n}+1, t_{n+2} \ldots t_{s} \ldots t_{t}\right)$ is chosen as the hazard-related indicator to represent the magnitude of hazard B. The probability and degree of the changes in the trigger factor group $\left(t_{n+1}, t_{n+2} \ldots t_{s} \ldots t_{t}\right)$ are decided by the magnitude of hazard A , that is, the changes in the trigger factor group $\left(t_{1}, t_{2} \ldots t_{i} \ldots t_{n}\right)$.

Hazards in a mutex relationship cannot occur together, so the mutex relationship is not mentioned further.
(2) Determining the conditional probability

A conditional probability measures the probability of an event given that another event has occurred. Once a BN framework is constructed, the conditional probability of a node given their parent nodes should be determined. The conditional probability of a vulnerability-related indicator or hazard-related indicator given a loss ratio is determined in this module as:
$p\left(v_{k j} \mid l_{i}\right)$
where $l_{i}$ represent the $i$ state of loss ratio $l, i=1,2, \ldots m$, and $v_{k j}$ represents the $j$ state of a vulnerability-related indicator or hazard-related indicator $k, k=1,2, \ldots x, j=1,2, \ldots n$.

There are three commonly used methods for estimation of the conditional probability. When applied to a complete observed data set, maximum-likelihood estimation (MLE), a well-known statistics method is used to provide estimates for the model's parameters (the conditional probabilities) (Redner and Walker 1984; Grossman and Domingos 2004; Liu et al. 2015). If the model relies on incomplete observed data, an expectation-maximization (EM) algorithm, an iterative method for finding maximum likelihood estimates of parameters (conditional probabilities) in statistical models, can be used (Lauritzen 1995). When there is no observed data for the model, the model's parameters (conditional probabilities) can be estimated according to domain knowledge (Heckerman et al. 1995; Liao and Ji 2009). Hence, in this module, the methods used for estimation of conditional probabilities are determined according to the availability of observed data.

## (3) Loss ratio calculation

In this step, given the above conditional probability, the joint probability (Eq. 12) is used to estimate the posteriori probability of the target loss ratio:

$$
\begin{aligned}
p\left(l_{i}, v_{1}, v_{2}, \ldots v_{k} \ldots v_{s}\right) & =p\left(l_{i}\right) p\left(v_{1}, v_{2}, \ldots v_{k} \ldots v_{s} \mid l_{i}\right) \\
& =p\left(l_{i}\right) \prod_{k=1}^{s} p\left(v_{k} \mid l_{i}\right)
\end{aligned}
$$

where $l_{i}$ represents the $i$ state of loss ratio $l$, and $v_{k}$ is the vulnerability-related indicator or hazard-related indicator $k$, $k=1,2, \ldots s$.

When the states of all vulnerability-related indicator and hazard-related indicators are given as $j$, the probability of loss ratio $l_{i}$ occurring can be calculated based on the posteriori probability of the target loss ratio:

$$
P\left(l_{i}\right)=\frac{p\left(l_{i}, v_{1 j}, v_{2 j}, \ldots v_{k j} \ldots v_{s j}\right)}{\sum_{i=1}^{m} p\left(l_{i}, v_{1 j}, v_{2 j}, \ldots v_{k j} \ldots v_{s j}\right)}
$$

where $l_{i}$ represent the $i$ state of loss ratio $l, i=1,2, \ldots m$, and $v_{k j}$ represents the $j$ state of vulnerability-related indicator or hazard-related indicator $k, k=1,2, \ldots s, j=1,2, \ldots n$.

The final loss ratio $L$, with given all vulnerability-related indicator and hazard-related indicator states $j$, can then be calculated as:
$L=\sum_{i=1}^{m} l_{i} \times P\left(l_{i}\right)$
where $l_{i}$ is the $i$ state loss ratio with given all vulnerabilityrelated indicator and hazard-related indicator states $j$, $i=1,2, \ldots m$, and $P\left(l_{i}\right)$ is the corresponding probability of the target loss ratio $l_{i}$ occurred.

The loss ratio with other states of vulnerability-related and hazard-related indicator can be calculated in the same way. This module can thus calculate the loss ratio induced
by multi-hazards of different degree (different states in hazard-related indicators), whilst also addressing vulnerability using vulnerability-related indicators from physical, social, economic and environmental domains.

### 3.4 Multi-hazard risk assessment

At this point, and based on the hazard identification and hazard interaction analysis modules, the exceedance probability of multiple hazards can be determined. For any given exceedance probability of multiple hazards, the corresponding loss can be calculated by the value of exposure (identified in the exposure module), and the corresponding loss ratio induced by these hazards (measured in the loss ratio assessment module). With the help of ArcGIS software, the possible loss caused by multi-hazard with different exceedance probabilities in each spatial assessment unit can then be mapped. These maps can be used to identify high risk (large potential loss) areas. Furthermore, this model can help to identify what underlies these large losses. This is significant, as such information supports, guides and targets the development of appropriate loss prevention and risk mitigation measures.

## 4 Model application: a case study in northeast Zhejiang

### 4.1 Study area and data

Northeast Zhejiang (Fig. 5), as part of the Yangtze River Delta, is one of China's main economic regions. This region comprises seven prefecture-level cities in Zhejiang provinces (hereafter "city"), and comprises 55 county level cities and counties (hereafter "county"). With both population density and economic activity growing, this already vulnerable region is increasingly at risk from natural disasters (Liu et al. 2013). Northeast Zhejiang, facing the Pacific to the east, is a typical floodplain with numerous rivers, lakes and canals, and is highly prone to natural hazards. This region is downstream of the Yangtze and Qiantang Rivers and their many tributaries, with channel density $>0.5 \mathrm{~km}$ of river per $\mathrm{km}^{2}$, factors that make it liable to frequent flooding (Li et al. 2013). The region is coastal and an oceanic landform between Eurasia and the Pacific, so is susceptible to typhoons and storm surges. In addition, some hilly areas are likely to be influenced by landslides. Hence, due to its geographical location and topography, multiple hazards, particularly typhoons, floods, landslides and storm surges are evident in Northeast Zhejiang.

In addition, according to historical observations, being struck by two consecutive typhoons (within 60 days) is the most common multi-hazard scenario in Northeast Zhejiang.

![img-5.jpeg](img-5.jpeg)

Fig. 5 Northeast Zhejiang, China

The first and second typhoons have an independent relationship, and these two typhoons could induce floods, landslides and storm surges respectively. Typhoons, floods, landslides and storm surges have a strong relationship with each other in this multi-hazard scenario. Hence, Northeast Zhejiang being struck by typhoons twice consecutively (within 60 days) is a suitable case to show the application of the proposed model.

Three types of data are needed to implement the proposed model: environmental data, disaster data and socioeconomic data. Environmental data mainly comprises meteorological data, downloaded for 15 recording stations
(Fig. 5) in the region, with daily data from 1980 to 2013, a suitably lengthy period for hazard-forming environment analysis. Disaster data for this period, collected from the Meteorological Department and the Civil Administration Department in China, includes the disaster type, time, place, and direct economic loss for each disaster in Northeast Zhejiang. Socioeconomic data, derived from statistics yearbooks (1980-2013) in each city includes GDP, income (of rural and urban residents), population density, gender ratio, age structure, telecommunication infrastructure (number of mobile phone users, fixed line phone users, and internet users), transport route (road

length), medical service provision (number of medical institutions, beds and medical personnel), and social dependency (number of residents covered by subsistence allowances, number of employed) in each county.

### 4.2 Exceedance probability for multiple hazards from two consecutive typhoons in northeast Zhejiang

Typhoons, floods, landslides and storm surges are the main hazards in the region. In contrast to other hazards, typhoons can move thousands of kilometres accompanied by strong winds and heavy rain, and a series of hazards (strong winds, floods, landslides and storm surges) induced by changes in wind and rainfall are the reasons for losses in the typhoon track (Lee et al. 2012; Smith 2013). Thus typhoon is viewed as changes of wind speed and rainfall, with these changes used as trigger factors to measure the magnitude of the series of hazards in the track. Hence, the relationships among multiple hazards of two consecutive typhoons in northeast Zhejiang is shown by Fig. 6.

Both typhoons are viewed as the trigger factors, with changes of wind speed and rainfall, which induce strong winds, floods, landslides and storm surges. During each typhoon, these four hazard types are in a parallel relationship and constitute a hazard group with each hazard induced by common trigger factors (wind speed and rainfall). Hence, the frequency and magnitude of this hazard group are determined by changes in wind speed and rainfall. The exceedance probability of this hazard group (strong winds, floods, landslides and storm surges) occurring with different magnitudes can be expressed as:
$E P\left(H_{w} \cap H_{f} \cap H_{l} \cap H_{s}\right)=E P($ wind speed, rainfall $)$
where $H_{w}$ is strong wind, $H_{f}$ is flood, $H_{l}$ is landslide, $H_{s}$ is storm surge, and $E P$ (wind speed, rainfall) is the exceedance probability of the corresponding maximum daily rainfall and maximum daily wind speed sets during the typhoon, calculated using the mathematical statistics
approach with maximum daily rainfall and maximum wind speed during each historical typhoon.

According to the trigger factors for hazard occurrence, two typhoons are in an independent relationship, so the hazard groups A and B are also in an independent relationship. Hence, the exceedance probability for multiple hazards of two consecutive typhoons can be calculated as:

$$
\begin{aligned}
E P(M H)= & E P_{f}(\text { wind speed }, \text { rainfall }) \\
& \times E P_{s}(\text { wind speed }, \text { rainfall })
\end{aligned}
$$

where $E P(M H)$ is the exceedance probability for multiple hazards of two consecutive typhoons, $E P_{f}$ (wind speed, rainfall) is the exceedance probability of the corresponding maximum daily rainfall and maximum daily wind speed sets during the first typhoon, and $E P_{s}$ (wind speed, rainfall) is the exceedance probability of the corresponding maximum daily rainfall and maximum daily wind speed sets during the second typhoon.

In our analysis, we adopted the two dimension information diffusion method (Huang 1997) to calculate the exceedance probability of the corresponding maximum daily rainfall and maximum daily wind speed sets. Within this method, maximum daily wind speed and maximum daily rainfall are viewed as two associated factors in one set, and the coefficient of correlation between them is considered during the diffusion. The results in 3 meteorological sites are used as cases to be shown in Fig. 7. Then, a spatial interpolation technique is used to estimate the rainfall and wind distribution in the whole region. The results, as distribution of maximum daily rainfall and maximum wind speed with different exceedance probabilities, are shown in Fig. 8.

### 4.3 Possible loss caused by multiple hazards from two consecutive typhoons in northeast Zhejiang

### 4.3.1 Exposure distribution in northeast Zhejiang

With respect to losses, our case study takes economic loss as an example, with GDP selected as the exposure
![img-6.jpeg](img-6.jpeg)

Fig. 6 Relationships among multiple hazards of two consecutive typhoons in northeast Zhejiang

indicator. The assessment unit in northeast Zhejiang is the county level (government administrative division), so the official statistics data analysis method is used. From these statistics, GDP in each county was obtained, and mapped using ArcGIS. Figure 9 shows that countries with higher GDP in 2013 are mainly located in the north eastern part of the region.

### 4.3.2 Loss ratio assessment in northeast Zhejiang

For northeast Zhejiang, the relevant vulnerability-related indicators are selected as shown in Table 2. Among these indicators, GDP per $\mathrm{km}^{2}$, population density and percentage of residents covered by subsistence allowances show the same trend direction with vulnerability, that is, as the value of these indicators increases, the value of vulnerability increases. The other indicators show the opposite directional trend with vulnerability. In order to unify the directional trend of these indicators with vulnerability, the reciprocal of the GDP per $\mathrm{km}^{2}$, population density, and 1-percentage of residents covered by subsistence allowances are used in Factor analysis. PCA is adopted to make distinct the principal component. Table 3 shows eight principal components selected based on the cumulative variance, then a varimax rotation strategy is used to calculate the factor loading in each principal component. Variables with the highest loading in each principal component (bold figures in Table 3), are selected as the vulnerability-related indicators to construct the BN. These were: the number of mobile phone users per 10,000 persons (a proxy for income of residents, and telecommunication condition), doctors per 10,000 persons (a proxy for hospital beds and access to medical services), reciprocal of the population density (a proxy for population density and road length per 10,000 persons), reciprocal of the GDP per $\mathrm{km}^{2}$, number of medical institutions per $\mathrm{km}^{2}$, percentage of population age $>15$ and $<65$, and percentage of male residents and percentage of employed.

Maximum daily rainfall and maximum daily wind speed in each typhoon are selected as trigger factors to construct the set of hazard-related indicators which represent the magnitudes of multiple hazards. The first and second typhoons have an independent relationship, hence based on the hazard interaction analysis (Sect. 4.2), the BN framework in northeast Zhejiang can be constructed as shown in Fig. 10.

In our case study, the loss ratio is divided into six states, the eight vulnerability-related indicators are each divided into five states, and the hazard-related indicators (maximum daily rainfall and maximum daily wind speed sets) are divided into eight states (Table 4). From the 1980-2012 historic disaster records, aggregate loss data from two consecutive typhoons were collected, along with corresponding data for vulnerability-related indicators (from the relevant statistics yearbook) to construct a complete
![img-7.jpeg](img-7.jpeg)

Fig. 7 Exceedance probability distribution of rainfall and wind speed sets a Hangzhou, b Shengshan, c Yuhuan

![img-8.jpeg](img-8.jpeg)

Fig. 8 Distribution of maximum daily rainfall and maximum wind speed with different exceedance probabilities a Maximum daily rainfall distribution with exceedance probability of $5 \%$, b Maximum wind speed distribution with exceedance probability of $5 \%$, observed data set. Then maximum-likelihood estimation (MLE) was then used to provide estimates of the conditional probabilities (Grossman and Domingos 2004). With these conditional probabilities, the loss ratio with different states of vulnerability-related and hazard-related indicator was calculated based on Eqs. 12-14. Taking the maximum daily rainfall distribution and maximum wind speed distribution of the first typhoon with exceedance probability of $10 \%$, and the second with exceedance probability of $5 \%$ as example, the results are shown in Fig. 11.

### 4.4 Multi-hazard risk map in northeast Zhejiang

Taking northeast Zhejiang in 2013, influenced by consecutive typhoons (maximum daily rainfall distribution and
c Maximum daily rainfall distribution with exceedance probability of $10 \%$, d Maximum wind speed distribution with exceedance probability of $10 \%$
maximum wind speed distribution of the first typhoon with exceedance probability of $10 \%$, and the second with exceedance probability of $5 \%$ ) as an example, and according to the hazard identification and interaction analysis described above, the magnitudes of multiple hazards can be expressed by the maximum daily rainfall distribution and maximum wind speed distribution (Fig. 8). With these rainfall and wind speed distributions, the corresponding loss can be calculated by the exposure distribution (Fig. 9) and corresponding loss ratio distribution (Fig. 11). The final risk map is shown in Fig. 12.

This analysis shows that higher loss counties are mainly in the south eastern part of the region, with Linhai, Tiantai, Xianju, Sanmen and Jinzhou counties in the highest risk area. Risk is determined by the magnitudes of multiple

![img-9.jpeg](img-9.jpeg)

Fig. 9 GDP distribution in northeast Zhejiang in 2013
hazards, vulnerability and value of exposure. Jinzhou is in the highest risk area due to its highest exposure value. The high risk at Linai, Tiantai, Xianju and Sanmen is due to the interaction of the highest magnitudes of multiple hazards and the highest vulnerability. Thus the relative importance of factors that underlies observed high risk varies geographically. The model can be used to estimate the loss distribution influenced by typhoon with other exceedance probabilities, and also through other hazard combinations.

## 5 Model validation

Model validation is used to check how well the model represents reality. In our example application, MmhRiskHI is applied to estimate potential loss caused by multiple hazards in northeast Zhejiang. To test the effectiveness of the model, the hazards that occurred in 2013 were simulated, and calculated losses compared to observed losses. In 2013, northeast Zhejiang was influenced by typhoon Trami (21st August) then typhoon Fitow (7th October). According to the hazard identification and hazard interaction analysis,
the magnitudes of multiple hazards induced by typhoons in northeast Zhejiang can be expressed by the maximum daily rainfall and maximum wind speed. Data for these variables was collected from 15 meteorological stations in northeast Zhejiang. With these hazard-related indicators (maximum daily rainfall and maximum wind speed) and vulnerabilityrelated indicators described, using data for 2013, the loss ratio assessment module (based on historical data from 1980 to 2012) was used to estimate the probability of loss ratio in each county induced by these typhoons Trami and Fitow. The modelled and observed loss ratio in 55 counties in northeast Zhejiang are shown in Table 5.

As shown in Table 5, among these 55 counties, the real loss ratio in 42 counties ( $76.36 \%$ ) falls into the loss ratio state $\left(l_{1}\right)$ which has the highest estimated probability (bold figures in Table 5). Taking Shangcheng as an example, the real loss ratio in this county is $0.01 \%$, which falls into the loss ratio state $2(0 \%<l_{2}<0.5 \%)$. In the corresponding estimated results, the estimated probability of $l_{2}$ occurring in Shangcheng is $98 \%$, which is the highest among all six loss ratio states. In addition, the total estimated loss in these 55 counties is 51,893.39 million yuan compared to the

Table 2 Vulnerability-related indicators in northeast Zhejiang


- Represents the data is not available in these indicators. These indicators should be considered if such data are available

Table 3 Factor loadings in each principal component in northeast Zhejiang


Bold values represent the highest loading in each principal component

![img-10.jpeg](img-10.jpeg)

Fig. 10 The basic structure of Bayesian Networks for loss ratio assessment in northeast Zhejiang
actual loss of 50,485.43 million yuan; a deviation of estimated from actual value of less than $2.79 \%$. Hence the MmhRisk-HI model is shown to effectively represent the real system, with estimated results reflecting the real loss situation.

## 6 Conclusion and discussion

MmhRisk-HI fills a key research gap in existing MHRA methods as it goes beyond the simple consideration of multi-hazard interaction as domino effect, to calculate possible loss with an explicit consideration of all possible hazard relationships. In our case study example, whilst the typhoons are independent, the short time period between them means the area is more vulnerable as it has not recovered immediately from the first typhoon. Previous MHRA methods assume there is no change in vulnerability, and so would calculate the loss in each typhoon individually assuming the same vulnerability, then the aggregates the losses. Thus such results cannot reflect the real loss situation. In MmhRisk-HI, the loss ratio assessment module addresses this issue by considering the magnitudes of these two typhoons together in hazard-related indicators. These two typhoons are treated as a multiple hazards group, and the relevant vulnerability-related indicators correspond to this group rather than a single typhoon. Hence, the results obtained in the model are more reliable.

Model validation is a highly desirable step in model development, but a process that has previously proved intractable in MHRA due to the nature of the existing models. MmhRisk-HI can be validated through comparison
of modelled and observed data, with the model used to simulate different multiple natural hazards scenarios and estimate the corresponding loss. In the case study, MmhRisk-HI was used to simulate consecutive events, typhoons Trami and Fitow which struck northeast Zhejiang within a few months in 2013. The simulated results were then compared to the observed data, with good agreement. The validation, although based on a necessarily limited set of actual multi-hazard interaction, does indicate that MmhRisk-HI can represent the real world risk situation with greater confidence.

In conclusion, MmhRisk-HI provides more reliable results (possible loss caused by multiple hazards) with an explicit consideration of interaction between different hazards, and can also be used to explore and better explain what underpins large potential losses (high risk). Hence, the model is a useful tool which can provide better information in risk mitigation planning.

Further improvements to MmhRisk-HI are possible. First, a change in one (or several) trigger factors may induce more than one hazard at the same time. In MmhRisk-HI, these hazards are treated as a multiple hazards group, with all hazards in the group induced by the same trigger factor(s). These trigger factors can be used as hazard-related indicators to represent the intensity of this hazard group in loss ratio assessment. In this way, the results obtained in this model are more reliable. However, these results cannot show how much loss is induced by each single hazard in the hazard group. In reality, it is also hard to distinguish how much loss is induced by each single hazard. For example, during a typhoon, it is hard to distinguish how much loss can be attributed to strong winds and how much to floods. Indeed, in the historical

Table 4 Different states of factors in Bayesian network

2. 2500 phone users/10,000 persons $\leq M_{2}<5000$ phone users/10,000 persons
3. 5000 phone users/10,000 persons $\leq M_{3}<7500$ phone users/10,000 persons
4. 7500 phone users/10,000 persons $\leq M_{4}<10,000$ phone users/10,000 persons
5. $M_{5} \geq 10,000$ phone users/10,000 persons  |
2. 10 doctors/10,000 persons $\leq D_{2}<15$ doctors/10,000 persons
3. 15 doctors/10,000 persons $\leq D_{3}<20$ doctors/10,000 persons
4. 20 doctors/10,000 persons $\leq D_{4}<25$ doctors/10,000 persons
5. $D_{i} \geq 25$ doctors/10,000 persons  |
2. $(1 / 1000) \mathrm{km}^{2} /$ persons $\leq P d_{2}<(1 / 750) \mathrm{km}^{2} /$ persons
3. $(1 / 750) \mathrm{km}^{2} /$ persons $\leq P d_{3}<(1 / 500) \mathrm{km}^{2} /$ persons
4. $(1 / 500) \mathrm{km}^{2} /$ persons $\leq P d_{4}<(1 / 250) \mathrm{km}^{2} /$ persons
5. $P d_{5} \geq(1 / 250) \mathrm{km}^{2} /$ persons  |
2. $(1 / 30) \mathrm{km}^{2} /$ million yuan $\leq G_{2}<(1 / 20) \mathrm{km}^{2} /$ million yuan
3. $(1 / 20) \mathrm{km}^{2} /$ million yuan $\leq G_{3}<(1 / 10) \mathrm{km}^{2} /$ million yuan
4. $(1 / 10) \mathrm{km}^{2} /$ million yuan $\leq G_{4}<(1 / 5) \mathrm{km}^{2} /$ million yuan
5. $G_{5} \geq(1 / 5) \mathrm{km}^{2} /$ million yuan  |
2. 0.02 medical institutions $/ \mathrm{km}^{2} \leq M i_{2}<0.03$ medical institutions $/ \mathrm{km}^{2}$
3. 0.03 medical institutions $/ \mathrm{km}^{2} \leq M i_{3}<0.04$ medical institutions $/ \mathrm{km}^{2}$
4. 0.04 medical institutions $/ \mathrm{km}^{2} \leq M i_{4}<0.05$ medical institutions $/ \mathrm{km}^{2}$
5. $M i_{5} \geq 0.05$ medical institutions $/ \mathrm{km}^{2}$  |
2. $72 \% \leq P a_{2}<73.5 \%$
3. $73.5 \% \leq P a_{3}<75 \%$
4. $75 \% \leq P a_{4}<76.5 \%$
5. $P a_{5} \geq 76.5 \%$  |
2. $50 \% \leq M a_{2}<50.5 \%$
3. $50.5 \% \leq M a_{3}<51 \%$
4. $51 \% \leq M a_{4}<51.5 \%$
5. $M a_{5} \geq 51.5 \%$  |
2. $50 \% \leq E_{2}<60 \%$
3. $60 \% \leq E_{3}<70 \%$
4. $70 \% \leq E_{4}<80 \%$
5. $E_{5} \geq 80 \%$  |
2. $W R f_{2}(W<10 \mathrm{~m} / \mathrm{s}, 50 \mathrm{~mm} \leq R)$
3. $W R f_{3}(10 \mathrm{~m} / \mathrm{s} \leq W<20 \mathrm{~m} / \mathrm{s}, R<50 \mathrm{~mm})$
4. $W R f_{4}(10 \mathrm{~m} / \mathrm{s} \leq W<20 \mathrm{~m} / \mathrm{s}, 50 \mathrm{~mm} \leq R<150 \mathrm{~mm})$
5. $W R f_{5}(10 \mathrm{~m} / \mathrm{s} \leq W<20 \mathrm{~m} / \mathrm{s}, R \geq 150 \mathrm{~mm})$
6. $W R f_{6}(W \geq 20 \mathrm{~m} / \mathrm{s}, R<50 \mathrm{~mm})$
7. $W R f_{7}(W \geq 20 \mathrm{~m} / \mathrm{s}, 50 \mathrm{~mm} \leq R<150 \mathrm{~mm})$
8. $W R f_{8}(W \geq 20 \mathrm{~m} / \mathrm{s}, R \geq 150 \mathrm{~mm})$  |

Table 4 continued


![img-11.jpeg](img-11.jpeg)

Fig. 11 Loss ratio distribution influenced by two typhoons with exceedance probability of $10 \%$ and exceedance probability of $5 \%$

![img-12.jpeg](img-12.jpeg)

Fig. 12 Multi-hazard risk map for two consecutive typhoons with exceedance probability of $10 \%$ and exceedance probability of $5 \%$

Table 5 The estimated results and observed real loss ratio


Table 5 continued


Bold values represent that the real loss ratio falls into the loss ratio state which has the highest estimated probability
disaster record, only records of loss induced by the whole typhoon are made, rather than for the constituent hazards. Understanding the loss induced by each single hazard could help decision-makers take more targeted mitigation measures. Addressing this issue, without historical loss data, will be challenging. Equally challenging will be the inclusion of uncertainty quantifiers in the MmhRisk-HI model. Uncertainty is inherent in natural disaster risk, and
needs to be better addressed for effective risk management, yet uncertainty analysis in MHRA remains rare.

Open Access This article is distributed under the terms of the Creative Commons Attribution 4.0 International License (http://creativecommons. org/licenses/by/4.0/), which permits unrestricted use, distribution, and reproduction in any medium, provided you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made.
