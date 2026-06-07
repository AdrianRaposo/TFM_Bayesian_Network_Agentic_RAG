# Article 

## A Quantitative Risk Assessment Model for Domino Accidents of Hazardous Chemicals Transportation

Jinhua Cheng, Bing Wang *, Chenxi Cao and Ziqiang Lang

## check for updates

Citation: Cheng, J.; Wang, B.; Cao, C.; Lang, Z. A Quantitative Risk Assessment Model for Domino Accidents of Hazardous Chemicals Transportation. Processes 2023, 11, 1442. https://doi.org/10.3390/ pr11051442

Academic Editors: Wende Tian, Qingjie Guo, Bin Liu and Zhe Cui

Received: 1 March 2023
Revised: 28 March 2023
Accepted: 4 April 2023
Published: 10 May 2023

## (0)

Copyright: (c) 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

Department of Automation, East China University of Science and Technology, Shanghai 200237, China

* Correspondence: wangb07@ecust.edu.cn


#### Abstract

In recent years, hazardous materials transportation accidents have received increasing attention. Previous studies have focused on accidents involving a single vehicle. When vehicles loaded with materials gather on a stretch of road, a potential domino accident might cause terrible incidents. This paper prompts a quantitative risk assessment (QRA) model to estimate the risk of multi-vehicle incidents. The model calculates the possibility of leakage and explosion of hazardous chemicals using a dynamic Bayesian network (DBN). For different types of hazardous chemicals, the model uses event trees to list different scenarios and analyzes the probability of domino accidents caused by each scenario. The FN-curve and potential loss of life (PLL) are used as an index to evaluate social risk. A case involving multiple vehicles in the JinShan District, Shanghai, is analyzed. The result of the case shows that the state of the driver, the type of road, weather factors and the distance between vehicles have vital impacts on the societal risk resulting from hazardous materials transportation accidents.


Keywords: QRA; hazardous materials transportation; domino effect; dynamic Bayesian network; FN curve

## 1. Introduction

In recent decades, hazardous materials transportation accidents have severely threatened public safety, especially in developing countries [1]. More than 400 million tons of hazardous materials are transported annually in China. Hazardous materials transportation accidents have a disastrous influence on human life and properties [2,3]. On 13 June 2020, the Wenling liquefied petroleum gas (LPG) accident caused 20 fatalities and 175 injuries [4]. At 14:00 on 1 March 2014, two semi-trailer trucks transporting methanol collided in the Yanhou tunnel of Jincheng section of Shanxi Jinji Expressway, causing a total of 40 fatalities and 12 injuries. Additionally, 42 vehicles burned down, with direct economic losses of CNY 81.97 million. Chinese authorities have promulgated many laws to prevent similar accidents. The Measures for the Safety specifications for road transportation vehicle of explosive substance and toxic substance (GB 20300-2018) have been formally implemented. Therefore, there is a critical need to assess the risk of domino effect accidents relating to hazardous materials and produce more effective risk countermeasures.

Hazardous chemical domino accidents are characterized as low-frequency and highconsequence incidents, which have a potential influence on nearby objects. As early as 1984, B. J. Wiekema analyzed the influence of a steam cloud explosion on the surrounding area based on the historical accidents of chemical enterprises, and deduced the trend when accidents occurred [5]. Bagster and Pitblado found that the probability of failure of the target equipment decreases with the increase in the distance between the target equipment and the accident center. Based on this, they provided a method with which to estimate the probability of failure of the target equipment [6]. P. Latha and G. Gautam emphasized the influence of time on the cascade effect (domino effect) in hazardous chemical accidents and simulated the time-varying heat exchange between the failed equipment and the target

equipment, the failure of the vessel under thermal and other stresses and the subsequent fracture, crushing and impact phenomenon [7]. Glenn N. Pettitt et al. calculated the frequency of each origin event, such as jet flame impact, pool fire engulfing, the steam cloud explosion effect and the BLEVE effect. Combined with the possibility of equipment failure caused by its consequences, this paper gives a relatively complete idea of assessing the risk of chemical parks [8].

The methods used for risk assessment of hazardous chemical transportation can be divided into qualitative and quantitative approaches [9]. Qualitative risk assessment is primarily focused on identifying the contributing factors of transportation accident, while the quantitative approach digs deeper into the relationship between influencing factors and the outcomes [10]. From a systematic point of view, the quantitative risk assessment (QRA) determines the probabilities of each potential scene and quantifies the consequences [11]. The occurrence of hazardous chemical transportation incidents is influenced by numerous factors, such as weather conditions, driver status and road factors [12]. Based on vehicle data from Shanghai, Weng J and Gan X [13] proposed a method for calculating the initial vehicle accident frequency of hazardous materials transportation, which is related to weather time, wind speed, and the size of the leak aperture. The frequency of accidents increases when weather conditions worsen. Tao D and Zhang [14] concluded that driver status was positively correlated with risky driving behavior. Benekos I [15] calculated the annual average frequency of vehicle accidents first and calculated the accident probability of hazardous chemical transportation accidents according to the proportion of vehicles transporting hazardous materials. However, the result of this method does not consider external factors. Bonvicini S [16] used the membership function to calculate the release frequency and the leakage rate. Reniers GLL divided the route into different segments and used the expert experience to classify the likelihood grade and consequence grade according to its characteristics [17], which is more dependent on the empirical knowledge of the decision makers. MATIASJ et al. considered 31 factors, such as weather and road type, that affect the risk of a particular road segment and used ordinal support vector machines (SVMs) to calculate accident frequency and consequences [18]. MATIASJ's method is convincing, but collecting such a large quantity of data is difficult. In 2001, the researchers introduced the Bayesian network (BN) to analyze risky situations. The BN adequately utilizes the data obtained to evaluate the probability and consequence of accidents. Furthermore, the BN can model uncertainty with dependencies between events. The usage of the BN is developing rapidly due to its ability to represent variable dependencies in complex systems. The term "domino effect" in the chemical industry refers to a series of accidents in which the main event, usually a fire or explosion, triggers further accidents that escalate the consequences of the event across the board [19]. N. Khakzad calculates the propagation probability of domino accidents by treating the state of the storage tank as a node of the Bayesian network [20]. E. Zarei uses fault tree analysis (FTA) to determine the leakage scenario of the host group and develops a dynamic risk analysis model for analyzing domino effects in RTHM based on a Dynamic Bayesian Network [21].

Generally, the consequence of hazardous chemical accidents is measured in terms of the number of casualties, the economic loss and the environmental pollution. Considering only the impact on people, the personal risk is measured by the potential loss of life and the social risk is expressed by the FN curve. The FN curve presents the relation between the number of fatalities and the frequency of accidents, which is very effective in risk analysis [22,23]. Social risk criteria can be divided into intolerable, as low as reasonably possible (ALARP) and negligible. According to the ALARP principle, we can easily understand the level of social risk [24]. The risk of hazardous materials transportation accidents changes with the movement of vehicles. The popularity of vehicle terminals enables real-time acquisition of vehicle status. Ma T and Wang Z developed a real-time risk assessment model to evaluate the risk of hazardous materials vehicles [25]. Based on typical hazardous chemical accident scenarios of different accidents, Huang W and Chen X proposed a dynamic evolution model of the domino effect considering the interaction

of time and space [26]. Nevertheless, these studies focused on accidents involving one vehicle [27,28,29,30,31,32]. There was a lack of studies on accidents involving multiple hazardous material vehicles.

A quantitative risk assessment model of multiple hazardous materials vehicles was presented to fill the above research gaps. This study comprehensively considers the factors of hazardous materials accident consequences and develops a QRA model to assess the risk of domino accidents in hazardous materials transportation by combining the frequency and consequence of accident scenarios. This method provides a reference for the government and enterprises to control the domino risk of hazardous chemicals.

# 2. Materials and Methods 

### 2.1. Dynamic Bayesian Network

The Bayesian network (BN) is a directed acyclic graph (Figure 1) [33]. Its nodes represent random variables, some of which are not observable. BN uses some known state nodes to deduce the state of the rest of the nodes:

$$
P(U)=\prod_{i=1}^{n} P\left(X_{i} \mid P a\left(X_{i}\right)\right)
$$

BN has significant advantages in dealing with uncertainty problems:

- BN describes the relationship between data with the graph method, which has unambiguous semantics and is easy to understand.
- BN allows the learning of causal relationships between variables. It can understand causality in data and learn network structure from the causality.
- BN is good at dealing with missing datasets. The method of BN reflects the probabilistic relationship model between the data in the database and can still establish an accurate model without certain data variables.
![img-0.jpeg](img-0.jpeg)

Figure 1. Bayesian network.
DBN is obtained by expanding BN with the same structure along the time axis. BN and time series combine to form DBN, which is a new stochastic model with the ability to process time series data. It fully considers the influence of the time factor when studying the uncertainty problem. Sample data (observational data) of dynamic Bayesian networks change over time. The conditional probability table (CPT) of a node is updated according to the status of its parent.

### 2.2. Domino Effect

An initial event propagates to a nearby device, triggering one or more secondary events, which in turn trigger higher-order events, resulting in a more serious accident than the initial event. The domino effect is a chain reaction from low energy to high energy, as shown in Figure 2. The domino effect in the transportation of hazardous materials is that one transportation vehicle has an accident resulting in a fire or explosion, thermal radiation and overpressure damage the containers of another transportation vehicle, vehicle after vehicle with irreversible consequences [34].

![img-1.jpeg](img-1.jpeg)

Figure 2. Domino effect of hazardous materials transportation vehicles.

# 2.3. Risk Assessment 

Generally, the risk of transport accidents with hazardous materials involving a single vehicle is the product of fatalities and the probability of the accident.

$$
R=\sum_{i=1}^{n} F \times P_{i} \times C_{i}
$$

The risk of transportation accidents with hazardous materials with multi-vehicles includes the upgrade probability of domino effect, which can be expressed as:

$$
R=\sum_{i=1}^{n} F \times P_{i} \times P o e_{i} \times C_{i}
$$

where $R$ is the risk of the accident, $F$ is the frequency of transportation accidents with hazardous materials, $P_{i}$ is the possibility of a different scene, $P o e_{i}$ is the probability of another hazardous materials vehicle being affected, $C_{i}$ is the casualties of each scenario and $i$ is the total number of scenarios. This study will analyze the model from the following four aspects: the frequency of transportation accidents, the possibilities of each scenario, the domino escalation probability and the casualties of each scenario.

### 2.3.1. Frequency of Road Transportation Accidents

Fabiano et al. pointed out that the vehicle accident rate and the average transportation distance of trucks are the determinants of hazardous materials transportation accidents. The meteorological conditions and traffic characteristics influence the frequency of transportation accidents [11]. To obtain an accurate probability estimation of hazardous materials transportation accidents through historical statistics, due to the relatively small sample of hazardous materials transportation accidents, the following model can estimate the occurrence frequency of hazardous materials transportation accidents.

$$
F=V A R \times L \times H_{1} \times H_{2}
$$

where $F$ is the expected frequency of hazardous materials transportation accidents (per year), $V A R$ is the vehicle accident rate (accidents per kilometer per vehicle), $L$ is the average transportation distance of trucks ( $\mathrm{km} /$ year) and $H_{i}(i=1,2)$ are the adjustment factors related to meteorological conditions and traffic characteristics, of which the suggested values are tabulated in Table 1 [13].

Table 1. Local enhancing/mitigating parameters for frequency of accident.


### 2.3.2. Possibilities of Each Scenario

This paper uses dynamic Bayesian networks to calculate the probability of leakage and uses event trees to list the route of each scenario. Figure 3 shows the bow tie diagram.

Table 2 shows the factors of the Bayesian network that affect the outcome of hazardous chemical accidents.
![img-2.jpeg](img-2.jpeg)

Figure 3. Hazardous materials road transport bow tie diagram.
Table 2. Factors affecting the consequences of transportation of hazardous materials.


The probability of each accident scenario is related to the value of each node in the event tree (Figures 4-6). Table 3 shows the possibility of different pore sizes in a leak [13]. Refer to Table 4 for the value of the ignition state. Table 5 shows the ignition efficiencies of diverse ignition sources during delayed ignition [35].

Table 3. Size of leakage hole.


Table 4. Probability of immediate ignition of hazardous materials leakage.


Table 5. Efficiency of ignition source in 1 min .


![img-3.jpeg](img-3.jpeg)

Figure 4. Event tree of compressed flammable gas.

![img-4.jpeg](img-4.jpeg)

Figure 5. Event tree of flammable liquid.
![img-5.jpeg](img-5.jpeg)

Figure 6. Event tree of toxic gas.

If the hazardous materials are compressed flammable gas, the following equation can be adopted to determine the delayed ignition probability:

$$
P_{t}=1-e^{-n w t}
$$

where $P_{t}$ is the delayed ignition probability, $n$ is the number of ignition sources, $w$ is the ignition efficiency of the ignition source, and $t$ is the duration (min).

# 2.3.3. The Domino Escalation Probability 

N. A. Eisenberg revised the data of damage caused by the explosion shock wave to process equipment under the framework of quantitative risk analysis, quantitatively assessed the domino effect caused by overpressure and derived a specific probit model for several different types of process equipment to calculate the probability of domino escalation in hazardous chemical accidents [36]. Leakage of hazardous materials can lead to fires and explosions. The relationship between the failure probability of the device and the overpressure/thermal radiation value is as shown in Table 6. The escalation of the incident will cause the container of the affected vehicle to rupture.

$$
P o e=\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{Y-5} e^{-\frac{x^{2}}{2}} d x
$$

where $Q$ is the value of thermal radiation, $t t f$ is the time at which the container goes from the normal state to the failure state at this value of thermal radiation is $\left(\mathrm{kw} / \mathrm{m}^{2}\right), P$ the value of the overpressure ( Pa ) and Poe is the probability of container failure.

Table 6. Relationship between escalation vector and failure probability of container.


### 2.3.4. Casualties of Each Scenario

Typical scenarios of hazardous materials incidents include fireball, jet fire, VCE, flash fire, pool fire, and diffusion of toxic gas. The empirical formula model in the reference is used in this study. Because the mathematical model is complex, it is only briefly introduced here.

## - Fireball

A fireball is the result of a rapid outflow and ignition of a pressurized combustible chemicals, which is known as a Boiling Liquid Expanding Vapor Explosion (BLEVE). It can also appear during the ignition of a flammable gas mixture. Fireballs can radiate large amounts of heat that cause material damages, injuries or deaths in an area much larger than the fire radius.

## - Jet fire

Jet fire is a fire of turbulent dispersion resulting from the combustion of flammable materials liberated continuously with considerable momentum in a specific direction. Access to hazardous materials species and storage pressure is required. It is necessary to calculate the leakage of different leakage apertures and calculate the radiation value of the jet fire based on the leakage.

# - VCE 

In a limited space, flammable gas is ignited, causing the VCE, which is divided into immediate ignition VCE and delayed ignition VCE. The former is formed when pressurized gas is ignited after the container breaks, which can be calculated by the TNT method according to the quality of goods. The latter is ignited as the vapor cloud spreads. The combustible gas forms a combustible vapor cloud during the leakage process. In the case of limited space, there is an ignition source in the lower and the upper flammability limits (LFL, UFL) of the vapor cloud explosion concentration. It is necessary to estimate the mass of combustible gases in the vapor cloud with concentrations between UFL and LFL. The TNT (Trinitrotoluene) method is used to calculate the overpressure values at different positions according to the mass. The gaussian plume model is widely used in gas diffusion modeling of continuous leakage from fixed point sources because of its good consistency with experimental results and simple calculation method, and plume from a continuous steady-state source is formulated as follows.

$$
C<x, y, z>=\frac{Q}{2 \pi \sigma_{y} \sigma_{z} u} \exp \left[-\frac{1}{2}\left(\frac{y}{\sigma_{y}}\right)^{2}\right] \times \exp \left\{\left[-\frac{1}{2}\left(\frac{z-H r}{\sigma_{z}}\right)^{2}\right]+\left[-\frac{1}{2}\left(\frac{z+H r}{\sigma_{z}}\right)^{2}\right]\right\}
$$

where $C<x, y, z>$ is the concentration of materials at coordinate point $(x, y, z)\left(\mathrm{kg} / \mathrm{m}^{2}\right)$, $Q$ is the rate of leakage of hazardous materials $(\mathrm{kg} / \mathrm{s}), \sigma_{y} \sigma_{z}$ are the diffusion coefficients for crosswind and vertical wind, $x, y, z$ are the distances of upwind, crosswind and vertical wind $(\mathrm{m})$.

The TNT equivalent model is often used as a simple method for estimating the mass of TNT per mass unit of fuel gas, whose detonation results in the same blast wave at the same distance. According to this model, the power of the vapor cloud explosion equates to an equivalent mass of TNT that would produce the same explosive power.

## - Flash Fire

In an open space, the vapor cloud is ignited to form flash fire. The probability of death between LFL and UFL is 1 , and the rest is 0 .

## - Diffusion of toxic gas

Toxic hazardous materials evaporate to form a vapor cloud. People within the vapor cloud can be injured. The probability of death is related to the exposure time and the concentration of the materials.

## - Pool fire

A pool fire is usually defined as a turbulent diffusion fire that burns over a horizontal pool of vaporizing flammable material. Under conditions in which the flammable material has zero or very low initial momentum, the shape of the flame is considered cylindrical.

The hazardous materials accident consequence is calculated based on empirical formulas. The model divides the area around the transportation vehicle of hazardous materials into grids and calculates the thermal radiation, overpressure and the concentration of toxic gas at each grid using empirical formulas according to different scenarios. The model converts the values in the grid into probability of death:

$$
\begin{gathered}
\operatorname{erf}(x)=\frac{2}{\sqrt{x}} \int e^{-t^{2}} d t \\
\operatorname{Pr}_{q}=-36.8+2.56 \times \ln \left(Q^{\frac{4}{3}} \times t \times 60\right) \\
\operatorname{Pr}_{p}=2.47+1.43 \times \ln (P) \\
\operatorname{Pr}_{t}=a+b \times \ln \left(c^{n} \times t\right)
\end{gathered}
$$

$$
P_{d}=0.5\left[1+\operatorname{erf}\left(\frac{P_{r}-5}{\sqrt{2}}\right)\right]
$$

where $P_{d}$ is the probability of death, $\operatorname{Pr}_{q} \operatorname{Pr}_{p} \operatorname{Pr}_{t}$ is the probability of death values from thermal radiation, overpressure, toxic gas, $Q$ is the thermal radiation $\left(\mathrm{W} / \mathrm{m}^{2}\right), P$ is overpressure (Mpa), $a, b, n$ is the materials toxicity constant, $c$ is the concentration of toxic gas $\left(\mathrm{mg} / \mathrm{m}^{3}\right)$ and $t$ is the exposure time $(\mathrm{min})$.

# 2.3.5. Personal Risk and Social Risk 

Personal risk matrix and potential life loss were used to evaluate personal risk of hazardous material transportation. Table 7 shows the personal risk standards of China and England:

$$
\begin{gathered}
\operatorname{prm}_{n}(x, y)=\sum_{k=1}^{n} f_{k} p_{k}(x, y) \\
\operatorname{prm}(x, y)=\operatorname{Max}\left\{\operatorname{prm}_{1}(x, y), \operatorname{prm}_{2}(x, y) \ldots \operatorname{prm}_{n}(x, y)\right\} \\
P L L=D m(x, y) \times \operatorname{prm}(x, y)
\end{gathered}
$$

where $P L L$ is the potential life loss, $D m(x, y)$ is the matrix of population density, $\operatorname{prm}(x, y)$ is the personal risk matrix for the Domino accident, $\operatorname{prm}_{i}(x, y)$ is the personal risk matrix from each vehicle and $n$ is the number of vehicles. $f_{k}$ is the value of frequency for each scenario, $p_{k}(x, y)$ is the probability matrix of death, $x, y$ is grid coordinates and $k$ is the number of scenarios.

Table 7. Individual acceptable risk standard value.


FN-curve is used to evaluate social risk. The principle expression of the FN-curve is as follows:

$$
P_{n}=1-F(n)=\sum_{n}^{n_{0}} f(n)
$$

where $P_{n}$ is the probability that the casualties are more than $n, n$ is the number of casualties, $F(n)$ is the probability function of the casualties, and $f(n)$ is the probability density function of the number of casualties. According to GB 36894-2018 "Hazardous Chemicals Production Equipment and Storage Facilities risk basis" and HSE, the lower limit of risk (N, F) of China's social risk standard is $\left(10.1 \times 10^{-6}\right)$, the upper limit of risk $(\mathrm{N}, \mathrm{F})$ is $\left(10.1 \times 10^{-4}\right)$,

and the slope is -1 . The British social risk standard is the lower limit $\left(50.1 \times 10^{-6}\right)$, the upper limit $\left(50.1 \times 10^{-4}\right)$, and the slope is -1 . The FN-curve consists of ignorable areas, ALARP areas, and intolerable areas.

# 3. Case Study 

### 3.1. Case Analysis Process

The process of case analysis is shown in Figure 7. Flammable, explosive and toxic dangerous chemicals will cause a major disaster once an accident occurs. Vehicles carrying such chemicals are called major risk installations; the study focuses on monitoring these vehicles. On the basis of calculating the frequency of common vehicle accidents, the probability of leakage and explosion of hazardous chemical vehicles is calculated using a dynamic Bayesian network. Ignition conditions, environmental factors and the type of hazardous chemicals lead to different accident scenarios. The ETA lists each scenario based on the chemical properties of the hazardous chemical. Scenario consequences were calculated using empirical formula. Finally, the model calculates the risk of a domino accident if the impact of a fire or explosion on the target equipment would cause a domino effect; otherwise, the model calculates the risk of a single vehicle.
![img-6.jpeg](img-6.jpeg)

Figure 7. Domino risk assessment flowchart for road transport of hazardous chemicals.

# 3.2. Data 

Jinshan Intelligent Emergency Platform is a hazardous chemical management platform built by Shanghai Jinshan District Government, which integrates online monitoring, risk control, major risk source monitoring and intelligent emergency dispatching. The platform contains information about all vehicles transporting hazardous chemicals in Jinshan District. The information includes license plate numbers, information about the chemicals being transported and the vehicle's location. Flammable and explosive chemicals are major risk sources, and the platform will focus on detecting such vehicles. The platform will send out warning messages when other vehicles transporting hazardous chemicals are close by.

There are hundreds of chemical enterprises in Jinshan District of Shanghai, and many dangerous chemicals transport vehicles appear near these chemical factories every day. These vehicles occasionally travel on the same stretch of road. According to the platform's data, at 13:00 on 23 September 2022, two vehicles transporting hazardous chemicals were driving on the same road. Figure 8 shows the location information of two vehicles during the same period. Table 8 shows the information of vehicles and chemicals.

Table 8. Environment variable, data of orders and meteorological conditions.


![img-7.jpeg](img-7.jpeg)

**Figure 8.** The route of hazardous materials transportation vehicles.

According to Equation (4), the vehicle accident frequency

$$F = 5.27 \times 10^{-8} \times 1 \times 10^5 \times 1 \times 0.8 = 0.0426/\text{year}$$

This study collects 367 accident samples from 2017 to 2021, which include driver status, vehicle factors, timing, weather factors and road factors at the accident (Table 9). Previous studies have shown that these factors influence vehicle accidents involving hazardous chemicals [6,13,15,25].

**Table 9.** Data on hazardous chemical incidents.


The node state information needs are discretized (Table 10) to train the structure and parameter of Bayesian networks.

**Table 10.** Node state discretization.


# 4. Results and Discussion 

### 4.1. Structure and Parameters of Dynamic Bayesian Networks

The discretized data were divided into a training set and a testing set at a ratio of 4:1. The training set was used to train the structure and parameters of the Bayesian network model. The structure of the Bayesian network represents the causal relationship between each node. It can be seen from Figure 9 that driver status, vehicle factors and "Hzamat_type" directly affect accident types. Road type has an indirect effect on accidents. Parameters represent the table of conditional probabilities (TCP) for each node. The testing set data were used to verify the accuracy of the model (Table 11). The test results show that the prediction accuracy of the model reached $73.3 \%$.
![img-8.jpeg](img-8.jpeg)

Figure 9. The structure of Bayesian networks.
Table 11. Prediction accuracy of the Bayesian network.


### 4.2. Risk Analysis of Single Vehicle

When two cars are far apart, an accident involving one car does not cause an escalation of the accident. We take vehicle II as an example to analyze the consequences of an accident involving a single vehicle. The parameters of vehicle II are input into the Bayesian network model to obtain the conditional probability table of accident consequences in Table 12.

Table 12. Conditional probability table of consequence.


The transportation accidents of hazardous materials can cause fire, explosions and toxic gas diffusion. ALOHA and CFD are used to simulate these scenarios. The simulation results are applied to estimate the consequences of the accidents. The models of ALOHA are empirical formula, which is also adopted in this paper to calculate the consequences of the accidents. The leakage rate of hazardous materials can be calculated according to pore size and parameters. It can be seen from Figure 10 that the larger the leakage aperture, the higher the leakage rate, which means that the scope of the accident is also larger. The leakage rate is used to calculate the radiation value of the jet fire and the diffusion of the vapor cloud. In this study, the angle between the direction of the jet fire and the

horizontal line was 30 degrees. The maximum evacuation time is 30 min [37]. Figure 11 is the comparison of the result of jet fire and the result of the Aloha simulation. The heat radiation is greater in the direction of the jet fire and the jet fire has strong thermal radiation at 20 m . Figure 12 shows the diffusion of the vapor cloud; the vapor cloud spreads over a large area.
![img-9.jpeg](img-9.jpeg)

Figure 10. Leakage rate of different leakage holes.
![img-10.jpeg](img-10.jpeg)

Figure 11. Jet fire radiation values due to 1-3 butadiene leakage $(\mathrm{d}=0.0508 \mathrm{~m})$.

![img-11.jpeg](img-11.jpeg)

Figure 12. The concentration distribution of gas diffusion $(3 \mathrm{~min}, \mathrm{~d}=0.0508 \mathrm{~m})$.
The experiment assumes that the leak height is 2 m , and the crowd will be evacuated after 3 min of the accident. The mass of the vapor cloud involved in the explosion is part of the vapor mass between the LFL and UFL. The average number of vehicles present during those three minutes is 24.3 , and the average number of people in the zone between LFL and UFL is 5.36. The probability of delayed ignition is calculated by Equation (4). Figure 13 shows the personal risk contours calculated from Equation (12). Part of the curve is bulging in the figure because the wind is causing the vapor cloud to spread in this direction; the risk is higher in this area.
![img-12.jpeg](img-12.jpeg)

Figure 13. Personal risk contours of vehicle II.
This study calculates the probability of each possible scene and the casualties. The calculated results are plotted as FN curves according to Formula (16). The comparative experiments (Figures 14-17) show that the risk value of road transport of hazardous chemicals is higher than the negligible standard, and the government should strengthen the risk management.

![img-13.jpeg](img-13.jpeg)

Figure 14. FN curves under different weather conditions.
![img-14.jpeg](img-14.jpeg)

Figure 15. FN curves under different driver states.

![img-15.jpeg](img-15.jpeg)

Figure 16. FN curves under different road conditions.
![img-16.jpeg](img-16.jpeg)

Figure 17. FN curves under different population densities.

# 4.3. Analysis of Sensitivity 

Another indicator of social risk is the potential loss of life. In order to analyze which factors have a significant effect on PLL, this model compares the PLL corresponding to different node states, such as weather, the state of driver, the type of road and person density. It can be seen from Figure 18 that the potential loss of life $\left(1 \times 10^{-3} /\right.$ year $)$ is fifty times higher on snow days than on sunny days $\left(2 \times 10^{-4} /\right.$ year $)$. Potential loss of life reaches $7 \times 10^{-4} /$ year when the vehicle is driving on urban roads. These values are increases over

the normal node state; the risk will also increase due to poor weather conditions. When the type of road is rural and the area is a business area, with a high density of people, the risk increases exponentially. The reason for this is that complex roads increase the frequency of traffic accidents. When the driver is exhibiting fatigue driving, speeding or improper operation, the potential loss of life is $2.25 \times 10^{-4} /$ year, $2.5 \times 10^{-4} /$ year, $4 \times 10^{-4} /$ year. Human factors have a great impact on the risk of road transport of dangerous chemicals. Thus, it is necessary for enterprises to train their employees.
![img-17.jpeg](img-17.jpeg)

Figure 18. The influence of different factors on potential loss of life.

# 4.4. Risk Analysis of Multiple Vehicles 

The risk of multiple vehicles is related to the distance between vehicles. China's traffic regulations stipulate that the speed of vehicles on urban roads cannot exceed $40 \mathrm{~km} / \mathrm{h}$ and the safe distance between vehicles is 20 m . Fireball, VCE and Jet fire from primary accidents lead to the failure of target equipment. Table 13 lists the accident scenarios that could lead to a domino effect. VCE and fireballs have a high probability of causing a domino effect. When the leak hole is larger, the possibility of ejecting fire, leading to domino effect, increases [38].

Table 13. The accident scenarios that could lead to a domino effect.


Study on domino accidents shows that when the distance between two vehicles carrying hazardous materials is 20 m , the domino effect leads to more deaths (Figures 19 and 20). Under Chinese standards, the risk of transporting hazardous chemicals exceeds the lower limit of socially acceptable risk by a large margin [39]. The risk of transporting hazardous chemicals is slightly above the lower limit of socially acceptable risk under UK standards. When two vehicles are close together, the platform should alert the driver to drive carefully. Under the same conditions, as the distance between the two cars narrows from 200 m to 5 m , the risk increases from $5.5 \times 10^{-4} /$ year to $6.5 \times 10^{-4} /$ year (Figure 21). This is because when the distance between vehicles is shortened, the target vehicle will be exposed to greater thermal radiation/overpressure and the upgrade probability will increase, causing a secondary accident [40].
![img-18.jpeg](img-18.jpeg)

Figure 19. FN-curve considering the domino scenario (Chinese standard).

![img-19.jpeg](img-19.jpeg)

Figure 20. FN-curve considering the domino scenario (British standard).
![img-20.jpeg](img-20.jpeg)

Figure 21. The effect of distance between vehicles on potential loss of life.

# 5. Conclusions 

In this study, a quantitative risk assessment model for hazardous chemical transportation has been established. This model uses dynamic Bayesian networks to predict the frequency of hazardous chemical accidents. The study collected 367 hazardous chemical accidents from 2017 to 2021, including human factors, external factors, vehicle factors,

environmental factors and road factors. These data are used to train the structure and parameters of Bayesian networks. This network and the vehicle state information uploaded by the vehicle terminal constitute a dynamic Bayesian network, which makes the prediction of accident frequency more convincing. The results show that driver status and weather conditions will increase the frequency of hazardous chemical accidents. Road type has a greater impact on risk because urban roads are more densely populated and have a greater traffic flow. The model also quantitatively assesses the risk of dominoes when multiple hazardous chemical vehicles gather. When vehicles gather, potential domino accidents cause more serious consequences. These results have guiding significance for enterprises and governments to prevent hazardous chemical transportation accidents. Enterprises and governments should strengthen the training of drivers, choose to transport hazardous materials on sunny days and avoid urban roads and business areas. When multiple vehicles carrying hazardous chemicals come too close, the government should warn drivers to drive carefully through on-board terminals.

Author Contributions: J.C., Experimental operation and paper writing; B.W. and C.C., methodology, validation; formal analysis; Z.L., supervision. All authors have read and agreed to the published version of the manuscript.

Funding: This work was supported by National Key Research and Development Program of China (2022YFB3304701), National Natural Science Foundation of China (62173145, 62173144), the Shanghai Committee of Science and Technology, China (Grant No.22DZ1101500).

Data Availability Statement: The data of road transport accidents involving hazardous chemicals used in this study were collected from Chinese accident news reports and on-site photos, as well as the materials in the references, which have been put on github.

Conflicts of Interest: The authors declare no conflict of interest.
