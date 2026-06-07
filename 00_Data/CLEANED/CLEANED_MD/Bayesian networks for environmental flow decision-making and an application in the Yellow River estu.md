# Bayesian networks for environmental flow decision-making and an application in the Yellow River estuary, China 

A. P. Pang and T. Sun<br>State Key Laboratory of Water Environment Simulation, School of Environment, Beijing Normal University, Beijing, 100875, China

Correspondence to: T. Sun (suntao@bnu.edu.cn)
Received: 22 October 2013 - Published in Hydrol. Earth Syst. Sci. Discuss.: 5 December 2013
Revised: - Accepted: 16 March 2014 - Published: 8 May 2014


#### Abstract

We proposed an approach for environmental flow decision-making based on Bayesian networks considering seasonal water use conflicts between agriculture and ecosystems. Three steps were included in the approach: water shortage assessment after environmental flow allocation using a production-loss model considering temporal variations of river flows; trade-off analysis of water use outcomes by Bayesian networks; and environmental flow decisionmaking based on a risk assessment under different management strategies. An agricultural water shortage model and a production-loss model were integrated after satisfying environmental flows with temporal variability. The case study in the Yellow River estuary indicated that the average difference of acceptable economic loss for winter wheat irrigation stakeholders was $10 \%$ between water saving measures and water diversion projects. The combination of water diversion projects and water-saving measures would allow $4.1 \%$ more river inflow to be allocated to ecological needs in normal years without further economic losses in agriculture.


## 1 Introduction

One of the greatest challenges to realizing sustainable water resource management is the assessment of the amount of water that can be withdrawn from an ecosystem before its ability to meet social, ecological, and economic needs declines (Richter et al., 1997; Acreman and Dunbar, 2004; McCartney et al., 2009). To define water requirements for an ecosystem, various methods for environmental flow assessments have been developed worldwide (Arthington et al., 2006; Poff et al., 2009; Vogel et al., 2007; Yang et al., 2009). Those
methods can generally be divided into four groups based on the types of ecological objectives: hydrological, hydraulic, habitat, and holistic (Tharme, 2003; Alcázar et al., 2008). However, difficulties in identifying reasonable objectives and uncertainties in establishing nonlinear eco-hydrological relationships have hampered the broad application of these approaches to environmental flow assessments (Adams et al., 2002; Richter, 2010; Cai et al., 2011). Up to now, it remains difficult to determine ideal water requirements for ecosystems because it is still difficult for us to define the best objectives for ecosystem protection. Furthermore, it is also difficult to identify whether a natural ecosystem is more reasonable than a managed ecosystem. To overcome these difficulties, adaptive management techniques and long-term field studies were suggested to support environmental management (Richter et al., 2006; Poff et al., 2003; Schreiber et al., 2004; Gregory et al., 2006; King et al., 2010), and more powerful mathematical models were also emerged to offer convenient tools for optimal water resource management (Cai et al., 2007, 2009).

Moreover, with limited water resources and seemingly limitless water requirements for humans and ecosystems, it is difficult to balance the water requirements for different stakeholders. Water requirements recommended for ecosystem protections may not be easily accepted by water utilization stakeholders due to the possible economic losses caused by environmental flow allocations. Achieving a socioeconomic and political consensus on different scenarios of human activities and ecosystem requirements has been identified as having great importance for successful implementation of environmental flow and decision-making in water resources management (William et al., 2008; O'Keeffe, 2009;

![img-0.jpeg](img-0.jpeg)

Fig. 1. Steps for environmental flow (EF) decision-making.

Renöfält et al., 2009). Barbier et al. (2008) highlighted the complexities involved and compromises necessary to obtain results that are not only ecologically desirable, but also enable management practices that are acceptable to a diverse set of stakeholders.

Water-use conflicts between human activities and ecosystems are influenced by the uncertainties about variations in river discharge, water management strategies, objectives of ecosystem protection, and agricultural development. In recent years, many different methods have been employed to integrate environmental changes and economic values. McCartney et al. (2009) stressed the necessity of integrating ecological economics into a social-ecological systems associated with different social, ecological, and management conditions. It is crucial to understand the effects of various flow scenarios on environmental flow allocation and to understand the operational rules necessary for implementing environmental flows (Shafroth et al., 2010).

Instead of proposing a method to determine the optimized environmental flows for ecosystems or human activities, we developed an approach for environmental flow decision-making considering trade-offs between socioeconomic and ecological water demands based on Bayesian networks (BNs). By identifying the point of inflection in probability for the acceptable outcomes of water use, we provided a way to quantify environmental flow decision-making under different water utilization scenarios. The proposed approach is flexible and will allow the incorporation of additional environmental, economic, and social factors into assessments, as well as considerations on socioeconomic and ecological needs for sustainable development.

## 2 Methods

The approach for environmental flow decision-making was comprised by three steps (Fig. 1): analyze the water use conflicts between agriculture and ecosystem, and also the water volume maybe lost in agricultural sector due to the maintenance of environmental flows; evaluate the trade-offs between different water use options using the BNs, the outcomes of which were the probability of economic losses under different water allocations scenarios; calculate the
environmental flows based on risk assessment using the inflection point analysis method.

### 2.1 Water shortage assessment for environmental flow allocation

In recent years, the natural flow regime for maintaining ecosystems has been significantly altered worldwide. In most river basins, large amounts of water are diverted for agricultural irrigation and other human activities (Malano and Davidson, 2009). According to Calzadilla et al. (2010), approximately $70 \%$ of freshwater, withdrawals from rivers and groundwater, is annually diverted from global river systems to supply agricultural irrigation. Consequently, we proposed a water shortage model for agriculture based on a higher priority for environmental flow allocation in water resources management. And water allocation outcomes can be evaluated based on crop yield variations affected by water utilization. Equation (1) shows the D-K model proposed by Doorenbos and Kassam (1979), which is typically used to evaluate crop yield losses with respect to the relative evapotranspiration deficit in different growth stages, that is,

$$
\frac{q_{\mathrm{m}}-q_{\mathrm{a}}}{q_{\mathrm{m}}}=k_{\mathrm{y}} \frac{\mathrm{ET}_{\mathrm{m}}-\mathrm{ET}_{\mathrm{a}}}{\mathrm{ET}_{\mathrm{m}}}
$$

where $q_{\mathrm{m}}$ is the maximum potential crop yield $\left(\mathrm{kg} \mathrm{ha}^{-1}\right)$, $q_{\mathrm{a}}$ is the actual crop yield $\left(\mathrm{kg} \mathrm{ha}^{-1}\right), k_{\mathrm{y}}$ is the crop yield response factor (dimensionless), and $\mathrm{ET}_{\mathrm{a}}$ and $\mathrm{ET}_{\mathrm{m}}$ are the actual and maximum potential evapotranspiration (mm), respectively.

We set $q_{\mathrm{s}}$ to represent the corresponding yield losses $\left(q_{\mathrm{m}}-q_{\mathrm{a}}\right)$ and set the ratio of agricultural water shortage to planting area $\left(W_{\mathrm{S}} / A\right)$ to indicate the agricultural water deficiency $\left(\mathrm{ET}_{\mathrm{m}}-\mathrm{ET}_{\mathrm{a}}\right)$ after satisfying environmental flows. Hence, the production-loss model can be written as follows (Pang et al., 2013):
$q_{\mathrm{s}}^{\mathrm{i}}=q_{\mathrm{m}} k_{\mathrm{y}}^{\mathrm{i}} \frac{W_{\mathrm{S}}^{\mathrm{i}}}{\mathrm{ET}_{\mathrm{m}}^{\mathrm{i}} A}$,
where $A$ is the planting area, and $W_{\mathrm{S}}^{\mathrm{i}}$ is the regional agriculture water shortage $\left(\mathrm{m}^{3}\right)$ during the growth period, in month $i$. Potential crop evapotranspiration $\mathrm{ET}_{\mathrm{m}}^{\mathrm{i}}$ is estimated

by a reference crop evapotranspiration $\left(\mathrm{ET}_{0}\right)$ and a crop coefficient $\left(k_{\mathrm{c}}\right)$.

Based on a high priority of environmental flows allocation, agricultural water shortage $W_{\mathrm{a}}^{i}$ can be calculated as the difference in water volume between agricultural demands and actual supply after maintaining environmental flows for ecosystems:
$W_{\mathrm{s}}^{i}= \begin{cases}(1-\mu) W_{\mathrm{a}}^{i}-W_{0}^{i}(1-\mu) W_{\mathrm{a}}^{i}>W_{0}^{i} \\ 0 & (1-\mu) W_{\mathrm{a}}^{i} \leq W_{0}^{i}\end{cases}$
where $W_{\mathrm{s}}^{i}$ is the agricultural water shortage, $W_{\mathrm{a}}^{i}$ is the agricultural water demand in the irrigation district, and $W_{0}^{i}$ is the agricultural water usage after deducting downstream commitments for environmental flows, all in month $i$, and $\mu$ is a dimensionless water-saving coefficient.

The agricultural water demand $W_{\mathrm{a}}^{i}$ can be determined according to water consumption in evapotranspiration in the irrigated area:
$W_{\mathrm{a}}^{i}=k_{\mathrm{c}}^{i} \mathrm{ET}_{0}^{i} S$,
where $k_{\mathrm{c}}^{i}$ is a dimensionless crop coefficient, $\mathrm{ET}_{0}^{i}$ is the evapotranspiration of the reference crop, and $S$ is the planting area.

Agricultural water usage $\left(W_{0}^{i}\right)$ can be calculated using the water balance principle. The water sources (river discharge, groundwater, precipitation, water transfer projects) and water utilization (domestic and industrial water use, agricultural water demand, and environmental flow requirements) include various factors required for the assessment model:
$W_{0}^{i}=W_{\mathrm{a}}^{i}+W_{\mathrm{p}}^{i}+W_{\mathrm{g}}^{i}-W_{\mathrm{d}}^{i}-W_{\mathrm{f}}^{i}-W_{\mathrm{e}}^{i} \pm W_{\mathrm{i}}^{i}$,
where $W_{\mathrm{a}}^{i}$ is river discharge, $W_{\mathrm{p}}^{i}$ is precipitation, $W_{\mathrm{g}}^{i}$ is the water supply depleted from groundwater, $W \mathrm{~d}^{i}$ is the amount of domestic water used, $W_{\mathrm{f}}^{i}$ is the amount of water used for industrial purposes, $W_{\mathrm{e}}^{i}$ is the initial environmental flow that satisfies ecological objectives, all in month $i$, and $W_{\mathrm{i}}^{i}$ is the amount of water transferred into or out of the watershed.

The initial environmental flow $W_{\mathrm{e}}^{i}$ can be determined based on different ecological objectives for ecosystem protections. Sun et al. (2008) develop a method for quantifying the environmental flows integrating multiple ecological objectives in estuaries.
$W_{\mathrm{e}}=\sum_{i=1}^{n} W_{i}+\operatorname{MAX}\left(W_{j 1}, W_{j 2}, \ldots, W_{j m}\right)$,
where $W_{\mathrm{e}}$ are environmental flows in the estuary $\left(\mathrm{m}^{3}\right)$, $\operatorname{MAX}(a, b)$ denotes the maximum of variables $a, b, W_{i}$ is the consumptive water volumes $\left(\mathrm{m}^{3}\right), W_{j}$ is the nonconsumptive water volumes $\left(\mathrm{m}^{3}\right), n$ and $m$ indicate the number of the objectives of consumptive and non-consumptive water volumes, respectively. The rule of summation is generally used for calculating consumptive water requirements,
![img-1.jpeg](img-1.jpeg)

Fig. 2. A simple framework illustrating the structure and CPTs of the BNs.
while the rule of compatibility (i.e., maximum principle) is adopted for estimating non-consumptive ones. In the environmental flows assessments of the Yellow River estuary, the water needed to ensure replacement of evaporative loss and maintenance of appropriate surface area and depth for wetland habitat stability is considered consumptive. Water needed to maintain the salinity balance and provided adequate transport of sediment and nutrients is identified as nonconsumptive, constituting runoff to the ocean.

Prioritizing environmental flow may cause economic losses in agriculture due to reduction in the use of water for irrigation. The economic losses resulting from agricultural water shortage were estimated by the crop price and production losses associated with the provision of the environmental flow.
$V^{i}=q_{\mathrm{s}}^{i} P$,
where $V^{i}$ represents the economic losses during the growth period, $q_{\mathrm{s}}^{i}$ is the corresponding production loss calculated from Eq. (2), and $P$ is the crop price $\left(\mathrm{USD} \mathrm{kg}^{-1}\right)$.

### 2.2 Trade-off analysis Bayesian networks (TOBNs)

We employed the BNs to obtain probability distributions under multiple choices and different scenarios. In general, Bayesian networks were developed as an effective analysis tool to estimate the probabilities of multiple states of response variables (Barton et al., 2008; Chan et al., 2010; Shenton et al., 2011). Previous research has already described the use of BNs for integrated water resources management, water sustainability, and probabilistic hydrologic forecasting (Martín de Santa Olalla et al., 2007; Castelletti and Soncini-Sessa, 2007; Zhang et al., 2011; Kragt et al., 2011). The BN consisted of a series of nodes, representing variables that interact with each other. Figure 2 shows a simple BN in which the node at the tail of the arrow, referred to as the parent node, directly affects the node at the head of the arrow, referred to as the child node. The cause-effect relationship between the parent node and the child node is often represented by an arrow, which are referred to as links. The links are expressed as probabilistic dependencies, which

are quantified through a set of conditional probability tables (CPTs). A CPT simply quantifies the probability of a node being in any particular state, given the states of the nodes linked to it. The information in CPTs may come from empirical data or an expert opinion, or it may be predicted from related model outputs.

The BN was then used in a "what if" analysis. In addition, no data were included for situations that could occur in the future but that had never occurred in the past (Jakeman et al., 2006; Aguilera et al., 2011), or those that could not be systematically verified or validated. Variables in the BNs are divided into five groups according to their function in the network.

1. parent nodes: not affected by changes in the states of other nodes;
2. intervention actions: actions that follow from the strategies selected through the parent nodes;
3. intermediate variables: represent simulation of the intermediate processes that take place between action and objective;
4. partial objectives: intermediate objectives that contribute toward final objectives;
5. final objectives: represent the variables that are of key importance to the system; the states of these variables are of great concern to stakeholders.

The TOBNs, defined as the use of BNs to evaluate the tradeoffs of water utilization between agriculture and ecosystem, were established based on the water shortage assessment for environmental flow allocation in Sect. 2.1. The Netica BNs software (Norsys Software Corporation, 1998) was used to build the TOBNs. This software utilizes Bayes' theorem for calculating the conditional probability of a variable that is dependent on the previous variable by the propagation of the probability.

### 2.3 Recommended environmental flow under different water management strategies

Economic losses caused by the prioritization of environmental flow may be unacceptable to irrigation stakeholders, but the recommended environmental flow cannot only be determined by the principles of maximum acceptability of economic losses. In this study, the environmental flow was recommended based on the inflection point in the probability distribution of "acceptable" economic loss (Fig. 3).

## 3 Study area

The Yellow River is the second longest river in China and the sixth longest river in world. In recent years, with rapid economic development in China, the volume of water diverted
![img-2.jpeg](img-2.jpeg)

Fig. 3. Illustration of the determination of recommended environmental flow.
for human activities has increased significantly, particularly for agricultural processes in the middle section of the Yellow River basin (Xu, 2007). Approximately $90 \%$ of the total water resources have been used for agricultural development in the Yellow River basin, resulting in a steady decrease in freshwater inflows to the Yellow River estuary over the past several decades (Li et al., 2004; Sun and Feng, 2013). Figure 4 shows the position of the Shandong irrigation district in the downstream section of the Yellow River, which is located between the Gaocun hydrological station and the Yellow River estuary. The Shandong irrigation district is an important zone for economic development and grain crop production in China. The water utilized for agriculture in this district is mainly supplied by the Yellow River, and since the 1960s, diversion of water for irrigation has increased significantly in the district. By the 1990s, the gross irrigation area had stabilized at 1.7 million ha.

In this area, up to $90 \%$ of water demands for agriculture are supplied by the Yellow River; the remaining $10 \%$ is supplied by groundwater (Yellow River Conservancy Commission of MWR, 1998-2011). According to monitoring data provided by the Shandong Hydrology and Water Resources Reconnaissance Office, the average fluctuation in groundwater level was between -0.5 and 0.5 m in $70 \%$ of the Shandong irrigation district. At the watershed scale, little groundwater recharge or return flow occurs due to the aboveground nature (the riverbed higher than the surrounding land) of the downstream section of the Yellow River and frequent drainage of water for irrigation (Zhi, 2006).

The main crops are winter wheat and summer corn, which are planted in a rotation system (October-May and JuneSeptember, respectively) and account for almost $90 \%$ of agricultural products in the district (Government Office of Shandong Province, 1956-2005). According to the Government Office of Shandong Province (1956-2005), the maximum potential crop yields of winter wheat and summer corn are $5.08 \times 10^{3}$ and $5.79 \times 10^{3} \mathrm{~kg} \mathrm{ha}^{-1}$, respectively, and the crop yield response factors for winter wheat and summer corn are 1.0 and 1.25 , respectively (Doorenbos and Kassam, 1979). Figure 5 shows temporal variations in reference crop evapotranspiration $\mathrm{ET}_{0}$ and crop coefficient $k_{\mathrm{c}}$ (Chen, 1995).

![img-3.jpeg](img-3.jpeg)

Fig. 4. Location of the Yellow River estuary and the Shandong irrigation district in China.

![img-4.jpeg](img-4.jpeg)

Fig. 5. Reference crop evapotranspiration and crop coefficients, derived from Chen (1995).

Increased water utilization has resulted in variations in the natural flow regime and even no-flow events in the downstream portions of the Yellow River. In the early 1990s, the river dried out annually, and contained no water for an average of 100 days per year in the lower reaches. Considerable effort has been made in determining environmental flow requirements of the Yellow River estuary (Sun et al., 2008, 2013). Sun et al. (2008) assessed the environmental flow in the Yellow River estuary considering different functions served by the ecosystem. The minimum and maximum levels of environmental flow were estimated to be 13.4 × 10<sup>9</sup> and 27.5 × 10<sup>9</sup> m<sup>3</sup>, accounting for 42.6 and 87.2% of the average annual runoff, respectively. To maintain a natural flow regime, temporal variation in natural river discharge was chosen as an indicator of the temporal variation objectives of the environmental flow. The minimum ratio is 2.5% in January and the maximum ratio is 15.9% in August.

### 4 Results

Figure 6 shows the structure of the TOBNs for environmental flow decision-making in the Yellow River estuary. The CPTs for the variables (nodes) were derived from the outcomes of water allocation analysis presented in Sect. 3.1 and the literature cited therein.

Nodes and output states in the TOBNs are listed in Table 1. The relationship between initial environmental flow, water inflow (wet, normal, and dry years), and agricultural water shortage was established based on the water shortage assessment for environmental flow allocation. The wet, normal, and dry states represent 25, 50, and 75% water supply assurance, respectively. We used river flow rates recorded at the Gaocun hydrological monitoring station and precipitation data collected at the Jinan weather station (Fig. 4) in Shandong Province from 1956 to 2005. Domestic and industrial water use and crop prices were determined using statistics from yearbooks produced by the Government Office of Shandong Province (1956–2005). Groundwater was set at 10% of agricultural water demand (Yellow River Conservancy Commission of MWR, 1998–2011). Economic outcomes of water shortage in agriculture were determined by the crop price and production losses associated with the environmental flow provision. In recent years, the planting areas of winter wheat and summer corn were 3.52 × 10<sup>6</sup> ha and 2.75 × 10<sup>6</sup> ha, respectively, (together accounting for about 90% of the total area of the irrigation district), and the prices were around USD 0.15 kg<sup>−1</sup> and USD 0.13 kg<sup>−1</sup>, respectively (Government Office of Shandong Province, 1956–2005). Before 2006, total agricultural taxes accounted for 15% of the yield for irrigation stakeholders (i.e., about USD 100 ha<sup>−1</sup> per year). Therefore, we set the final objective under USD 100 ha<sup>−1</sup>, to represent the acceptable economic loss for irrigation stakeholders.

To illustrate the influence of different levels of environmental flow allocations to the irrigation process, different

![img-5.jpeg](img-5.jpeg)

**Fig. 6.** The structure of trade-off analysis Bayesian networks (TOBNs).

![img-6.jpeg](img-6.jpeg)

**Fig. 7.** Comparison of the outcomes in the wet, normal, and dry years, (**A**) for winter wheat irrigation stakeholders, and (**B**) for summer corn irrigation stakeholders.

Levels of water requirements between the high and low initial estimated environmental flows were used in the calculation. Figure 7 shows the calculated probability distribution of economic losses after maintaining environmental flows with different water supply assurances. These were based on the acceptable limit of the water utilization outcomes considering economic losses of USD 100 ha<sup>−1</sup>. The balance between water utilization for ecosystems and agricultural processes varied with river discharge and crop type.

Based on the inflection point in the probability distribution of acceptable economic loss, appropriate environmental flow can be recommended considering the requirements of both ecosystems and agriculture. The average probability of acceptable economic loss was 50.9% for summer corn irrigation stakeholders, which was only 1% greater than that of the winter wheat irrigation stakeholders. During the summer corn growth stages (June–September), the probabilities of acceptable economic losses were relatively stable when environmental flows were allocated at less than 66.8% of natural flows in wet and normal years, the probability of acceptable economic losses decreased from 54.6 to 49.6% with an increase in environmental flow allocation of 66.8 to 70.8%. This suggested that 66.8% could be defined as environmental flows that may not cause more unacceptable economic loss for agriculture under present water resource strategies in wet and normal years. In dry years, the inflection point for the acceptable economic loss was 57.4%, the corresponding environmental flow was 50.7% of the natural flow. Consequently, the recommended environmental flows accounted for 66.8, 66.8 and 50.7% of natural flows during

Table 1. Nodes and outputs in the TOBNs.


* Included in both parent and water management interventions nodes.
wet, normal, and dry years for summer corn stakeholders, respectively. During the winter wheat growth stages (OctoberMay in the next year), the recommended environmental flows were $70.8,62.7$ and $54.7 \%$ of natural flows in wet, normal, and dry years, respectively. We combined the results in the two growth stages to calculate the annual environmental flows. In dry years, for the periods of June to September and October to May, the recommended environmental flows were 50.7 and $54.7 \%$ of natural flows, respectively, the annual recommended environmental flows accounted for $52.6 \%$ of the natural river flows. Similarly, the annual environmental flows were 64.8 and $68.7 \%$ of the natural river flow in normal and wet years (Fig. 8).

## 5 Discussion

In the TOBNs, water system engineering and water-saving measures were not only parent nodes but also water management intervention nodes. The water management strategy nodes referred to as "water system engineering" and "water-saving measures" in the TOBNs can be set to "yes" or "no," leading to four possible combinations of management strategies.

1. Water management strategy I reflected the present patterns of water utilization. The average river discharge during 1998-2005 was $18.8 \times 10^{9} \mathrm{~m}^{3}$, and water utilization for agricultural processes fluctuated between $19.8 \times 10^{9}$ and $20.2 \times 10^{9} \mathrm{~m}^{3}$. Under strategy I, annual discharges of 70.8 and $62.7 \%$ were taken as the recommended environmental flows that could meet the
![img-7.jpeg](img-7.jpeg)

Fig. 8. The recommended environmental flow in dry, normal, and wet years.
requirements of both the initial environmental flow and the lower economic loss during the winter wheat growth stage in wet and normal years, respectively; and $66.8 \%$ was recommended during the summer corn growth stage in wet and normal years (Fig. 7).
2. Water management strategy II included expected water utilization after the implementation of water diversion projects. To mitigate conflicts over water use in northern China, an eastern route for the south-to-north water diversion project was designed. The project aimed to transfer $0.72 \times 10^{9} \mathrm{~m}^{3}$ of water to Shandong Province, with $90 \%$ of these resources being used for agricultural development in the Shandong irrigation district. Water quantity of $0.65 \times 10^{9} \mathrm{~m}^{3}$ is supposed to be

![img-8.jpeg](img-8.jpeg)

Fig. 9. Comparisons of the probability distributions of acceptable economic loss among different water management strategies for the irrigation stakeholders of (A) winter wheat, and (B) summer corn.

transferred from outside of the watershed to Shandong irrigation district yearly.

3. Under water management strategy III, water utilization patterns incorporated the predicted impacts of water-saving measures. In the Shandong irrigation district, furrow and drip irrigation were the main water-saving measures and were part of the water-saving program. Moreover, new planting technologies, such as low-pressure irrigation, furrow irrigation, plastic mulch, and drip irrigation under plastic and terracing, could help to reduce agricultural water demands by 30%, based on suggestions from the FAO (Food and Agriculture Organization of the United Nations, 2011). As a result, about 6.0 × 10<sup>9</sup> m<sup>3</sup> of water could be saved from irrigation each year in the Shandong irrigation district.

4. Water management strategy IV represented the incorporation of the water diversion project and the water-saving measures.

The probability distributions of acceptable economic loss were compared among the different strategies under environmental flow allocations in normal years (Fig. 9).

For the winter wheat irrigation stakeholders, the average difference in the probability of acceptable economic loss between water management strategies II and III is 10%. Further, when 82.9% of the natural flow was allocated to the environmental flow, the implementation of water-saving measures had a particularly higher chance (17.9%) of an acceptable outcome than the water diversion project. The difference of an acceptable outcome when applying water-saving measures and water diversion projects was not much obvious when the environmental flow allocation was under the lowest state (42.6% of the natural flow), which were only 5.3% and 3.5% for the winter wheat and summer corn stakeholders.

Under the strategy of a combination of water-saving measures and water diversion projects, greater than 66.8% of natural flows could be allocated to environmental flows before the probability of an acceptable outcome for the winter wheat irrigation stakeholders decreased significantly. The inflection point in the probability distribution of acceptable economic loss was 62.7% under the current patterns of water utilization (strategy I).

Figure 10 shows the recommended environmental flow under the four water management strategies, after integrating the water requirements of the different irrigation stakeholders. Temporal variations of the recommended environmental flow exhibited the same trends and patterns as the natural flow variations in the Yellow River estuary, which used as an indicator of healthy environmental flows. The annual recommended environmental flow under strategy IV accounted for 64.8%, 68.9%, and 87.3% of the natural river flow in the dry, normal, and wet years, respectively. This suggested that 4.1% of river discharge could be allocated to ecosystems without increasing agricultural economic loss when the combined strategy was employed in normal years.

It should be pointed out that even if different water management strategies are employed, it remains difficult to satisfy the water requirements for both agricultural and ecological use, especially in dry years. In this situation, economic compensation could be an effective way to alleviate water-use conflicts (Sisto, 2009; Pang et al., 2013). A growing number of studies have suggested that the water trade may be an effective tool as a means of buying water from agriculture to establish a supply that meets environmental needs (Wheeler et al., 2010). In recent years, governments have pressured the agricultural irrigation sector to improve local environmental conditions. For example, the Australian government has been relying increasingly on water markets to buy water from willing irrigators to supply environmental flow (Australian Government, 2009; Wheeler et al., 2010). Based on the economic losses we calculated, compensation for agricultural stakeholders could alleviate water-use conflicts. In addition, stakeholder compensation for implementing water-saving measures could encourage others to take these steps, further reducing water-use conflicts.

![img-9.jpeg](img-9.jpeg)

Fig. 10. The recommended environmental flow under different water management strategies.
suggestion has been to establish a special fund to provide compensation for irrigators. This fund could then be used to upgrade irrigation systems and encourage the use of advanced irrigation techniques to reduce water loss.

Instead of proposing a method to determine the optimized environmental flows for ecosystems or human activities, we proposed a framework with more flexibility, which allowed us to incorporate additional factors into the assessments based on a consensus on socioeconomic and ecological needs for sustainable development. The water inflow, initial environmental flow requirements, water-saving measures and water diversion projects involved in this process were divided into different levels (states). In this way, variability in the objectives of environmental flows and irrigation processes, and diverse water resource management strategies could be utilized in the assessment. Additional influences such as climate change and human activity could also be included in the trade-off analysis. The probability distribution of economic losses provided the basis for the determination of recommended environmental flow for sustainable water use in ecosystem protection and irrigation processes. The approach developed here also allowed for an improved understanding of how to incorporate the traditional management framework by displaying the probabilities of multiple choices to analyze economic acceptability under different water management strategies. This is an important step in formulating an acceptable recommendation for stakeholders that is both hydrologically and economically practical.

## 6 Conclusions

We developed an approach for environmental flow decisionmaking considering the allocation of water for both agricultural and ecosystem processes. The approach was based on the conceptualization of water use conflicts and the utilization of BNs for quantifying uncertainties. Uncertainty in water utilization in agriculture and ecosystems was determined by BNs under different water management strategies. The inflection point in the probability distribution of acceptable economic loss for different stakeholders was identified as the threshold of recommended environmental flows.

We applied the approach in the downstream region of the Yellow River. Agricultural economic losses were calculated in the Shandong irrigation district after maintaining different levels of environmental flow in the Yellow River estuary. In a normal year, $68.9 \%$ of the natural flow could be allocated to environmental flow after implementing the water-saving measures (strategy III) or the combined water management strategy (strategy IV), contrast to $64.8 \%$ under strategy I, an additional $4.1 \%$ of the natural river inflow could be allocated to environmental flow without increasing agricultural economic losses.

Environmental flows identified from an ecosystem protection standpoint should be taken as preliminary results rather than conclusive flow requirements in a changing world. At this point, it is possible for us to provide a practical recommendation that is at least acceptable to a majority of stakeholders. Although we have only focused on a specific case

study in a limited area, the approach could be used to help settle water-use conflicts on a larger, regional scale.

Acknowledgements. This work was supported by the National Science Foundation for Innovative Research Group (no. 51121003), the National Basic Research Program of China (973) (no. 2013CB430402), the National Natural Science Foundation of China (no. 51079005), and the International Science \& Technology Cooperation Program of China (no. 2011DFA72420).

Edited by: Y. Cai
