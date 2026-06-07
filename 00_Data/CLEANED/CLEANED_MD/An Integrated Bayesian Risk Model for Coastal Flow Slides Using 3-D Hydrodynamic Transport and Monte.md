# Article 

## An Integrated Bayesian Risk Model for Coastal Flow Slides Using 3-D Hydrodynamic Transport and Monte Carlo Simulation

Ahmet Durap ${ }^{1,2, \star}$, Can Elmar Balas ${ }^{3}$ (D), Şevket Çokgör ${ }^{2}$ and Egemen Ander Balas ${ }^{4}$


#### Abstract

check for updates Citation: Durap, A.; Balas, C.E.; Çokgör, Ş.; Balas, E.A. An Integrated Bayesian Risk Model for Coastal Flow Slides Using 3-D Hydrodynamic Transport and Monte Carlo Simulation. J. Mar. Sci. Eng. 2023, 11, 943. https://doi.org/ 10.3390/jmse11050943

Academic Editors: Zili Dai, Chongqiang Zhu and Wei Chen

Received: 22 March 2023
Revised: 22 April 2023
Accepted: 26 April 2023
Published: 28 April 2023


## (0) (1)

Copyright: (c) 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /)$.


#### Abstract

1 Division of Civil Engineering, The University of Queensland, Brisbane, QLD 4072, Australia 2 Division of Coastal Sciences and Engineering, Civil Engineering Department, Civil Engineering Faculty, Istanbul Technical University, 34467 Istanbul, Turkey 3 Sea and Aquatic Sciences Application and Research Center, Gazi University, 06570 Ankara, Turkey 4 Department of Civil Engineering, Faculty of Engineering, Başkent University, 06790 Ankara, Turkey * Correspondence: a.durap@uq.edu.au


#### Abstract

The literature suggests two forms of flow slides: breaching and liquefaction. Both forms of failure have comparable ultimate circumstances, but the progression and sand movement mechanisms of breaching failure diverge from those of liquefaction. The first type, breaching, occurs in densely packed sand and is characterized by slow sand grain discharge throughout the dilation of the failing soil particles and negative excess pore pressures. The latter form, known as liquefaction, is the process by which a mass of soil abruptly begins to behave like a flowing liquid, and as a result, it can flow out across overly mild slopes. The process begins in compacted sand and is linked to positive surplus pore water pressures that are caused by the compaction of the sand. Despite the available literature on flow slide failures, our understanding of the mechanisms involved remains limited. Since flow slides often begin below the water surface, they can go undetected until the collapse reaches the bank above ground. The complexity of flow slides requires the use of cutting-edge technological instruments, diving equipment, advanced risk assessment, and a variety of noteworthy probabilistic and sensitivity analyses. Hence, we developed a new sensitivity index to identify the risk of breach failure and vulnerable coastal areas to this risk. In addition, we developed a sophisticated hybrid model that allows for all possibilities of flow slides in sync with random variables used in this new sensitivity index. In this new hybrid model, three distinctive models exist. The 3D Hydrodynamic Model addresses waves, wind, current, climate change, and sediment transport. The Monte Carlo Simulation is responsible for sensitivity analysis, and the Bayesian Network focuses on joint probabilities of coastal flow slide parameters of this new index that incorporates all environmental parameters, including climate change. With the assistance of these three models, researchers aim to: (a) expand the application scope by presenting a method on coastal flow slides; (b) consider different particle diameters corresponding to critical angle slope failure; (c) analyze variables that can play a pivotal role in the flow slides; and (d) present a methodology for coupling coastal flow slide projections with reliable outcomes. The hybrid model incorporates random variables of retrogressive breach failures, and the new risk index considers their ranges to control the simulation. The use of such a hybrid model and risk index offers a robust and computationally efficient approach to evaluating coastal flow slides.


Keywords: coastal flow slides; retrogressive breach failure; liquefaction flow slide; Monte Carlo simulation; risk assessment

## 1. Introduction

Coastal flow slides, also known as retrogressive breaching or liquefaction flow slides, are geomorphological processes that involve the downslope movement and redeposition of a significant amount of material from an underwater slope of a specific steepness [1-3].

However, their brief lifespan, unpredictable timing, and unseen initiation locations make them difficult to observe in nature and complicated to determine their causes and consequences [4]. Coastal flow slides are classified into two categories: breaching failure and liquefaction failure [5]. Breaching failure occurs when the slope of the beach is steep, while liquefaction failure occurs when the natural slope of the beach is mild [6]. In coastal engineering, the term "mild slope" refers to a topographic feature of the seafloor where the slope of the bottom terrain is relatively gentle or gradual over a large distance. In other words, the slope of the bottom terrain changes slowly and smoothly over a long distance compared to a steep slope. Mild slopes are commonly found in coastal environments such as estuaries, bays, and lagoons where there is a shallow water depth, and the seabed gradually transitions from the shore to deeper water. Coastal structures such as breakwaters, jetties, and seawalls are often designed to function effectively in the presence of mild slopes. Since the liquefaction flow slides occurs in mild slope regions, the area of concern needs to be examined thoroughly highlighted the need for increased awareness and research into this phenomenon to ensure the safety and effectiveness of coastal structures in mild slope regions. However, the danger of coastal liquefaction flow slides is significant, but it is not recognized as a prominent failure mechanism worldwide [7].

Various regions across the world have experienced coastal flow slides, and their occurrences, details are summarized in Table 1 [3]. An example of Inskip Point and Walsoorden coastal flow slides are shown in Figures 1 and 2 respectively. Coastal flow slides and other coastal hazards are quantified by the "retrogression length" metric, which measures the amount of land lost or relocated. The natural balance of the coastline may be disturbed by several variables, including sea-level rise, wave action, and coastal engineering initiatives. A comprehensive understanding of coastal processes is crucial in coastal engineering projects to maintain this natural balance.

Table 1. The global summary of events, including attributes, dates, and links [3].


![img-0.jpeg](img-0.jpeg)

Figure 1. Inskip Point coastal flow slides: when coastal flow slides occur below the waterline, the coastline loses its support, and a portion of it slips seaward, creating a hole, the edges of which regress toward the coast. ((a): The Sunshine Coast Daily, 2015, (b): SBS news, 2015).

![img-1.jpeg](img-1.jpeg)

Figure 2. Field investigation is being conducted in Walsoorden to study the cause of the coastal flow slide that occurred in the area [3].

Coastal protection structures, such as breakwaters and spurs, are being built in coastal areas, but if the environmental conditions of the specific region are not considered, these structures can severely disrupt the delicate balance of the coastal morphology. Wave and current energy play a critical role in coastal sediment transfer, but the impact of gravitational potential energy on slope failure has not been studied, despite its critical role in the migration of vast amounts of coastal sediments. In addition, wave energy devices are being constructed in the vicinity of the shoreline as wave energy is a renewable source, but if the equilibrium of the slope is disrupted, these structures may become ineffective or even disappear [8].

Slope failure due to coastal flow slides can have several potential impacts on the environment, such as the deterioration of water quality by increasing nitrogen and phosphorus concentrations at the surface. The reproductive habitats at the bottom of the sea could also be disrupted due to slope failures caused by coastal flow slides. The tourism and leisure

industries are equally vulnerable to the indirect effects of coastal flow slides on the coastal region and tourism industry, such as rendering coastal protections ineffective and reducing the width of the beach. The global climate crisis has led to higher sea levels and more frequent storms, both of which have hastened the erosion of beaches close to urban areas.

Past studies on coastal flow slides have been limited and conducted under deterministic conditions. This study utilizes a Monte Carlo Simulation (MCS) that employs random variables modeling the effects of hydrodynamic forces on slopes and assesses the critical regions. Understanding the causes underlying flow slides and creating effective measures to limit their consequences is crucial in light of their growing frequency and severity as a result of climate change. The critical angle slope design should be commonly employed methodology for assessing the safety of coastal slopes and identifying potential failure zones. This approach is utilized to determine the maximum angle at which a slope can remain stable under specific geological and environmental conditions. By employing critical angle slope design techniques, engineers and geologists can identify areas of potential instability and take appropriate measures to prevent slope failure, protecting both human lives and infrastructure. Nevertheless, there are certain limitations to this method, and the accuracy may be enhanced by including hydrodynamic forces.

One can model the effects of hydrodynamic forces on coastal slopes with the use of the Hydrodynamic Transport and Turbulence Module (HYDROTAM-3D) [9]. The vulnerability of a specific zone design's precision is greatly enhanced by including this module. This is a significant step forward in our knowledge of coastal flow slides since it is the first application of risk design to this topic.

A more thorough and accurate analysis of the hazards associated with coastal slope collapse is provided by the study's use of Monte Carlo Simulation (MCS) and Bayesian Networks (BN) for the stability evaluation. By using the BN-based Monte Carlo Simulation Model, researchers may learn more about the probability, amplitude, and effect of flow slides. Important implications for coastal management and engineering may be drawn from this line of study on coastal slope failure.

A liquefaction flow slide is a particular type of coastal flow slide, which occurs when the soil or sediment loses its strength and stiffness due to the build-up of pore water pressure. This can lead to the collapse of dikes and the displacement of water and sand, resulting in significant damage to coastal ecosystems and infrastructure.

The incorporation of the Hydrodynamic Transport and Turbulence Module of HYDROTAM-3D, Bayesian Network, and Monte Carlo simulation in the critical angle slope design has led to substantial advancements in the understanding of coastal flow slides. The implementation of these sophisticated modeling techniques has allowed for a more thorough and accurate assessment of the risk of slope failure in coastal regions. The Hydrodynamic Transport and Turbulence Module of HYDROTAM-3D enables us to simulate the complex interplay of CRBF, LFS and packing type, e.g., densely packed, loosely packed sand in coastal environments, while Bayesian Network and Monte Carlo simulation facilitate probabilistic risk analysis and perform probabilistic risk analysis to quantify uncertainty. By utilizing these advanced tools, researchers and practitioners can gain a deeper understanding of the factors contributing to coastal flow slides and make more informed decisions regarding slope management and mitigation [10]. This study has significant implications for coastal management and engineering since it increases design precision and provides a more in-depth examination of hazards connected with coastal slope collapse. We obtain a deeper comprehension of the probable outcomes of flow slides and insights into the most efficient methods for reducing their effects via the use of MCS and BN in the stability evaluation. As a whole, the findings of this study stress the significance of future studies in this field and the need for continuous efforts to overcome the difficulties presented by coastal slope failure.

## 2. The Breaching Failure

Coastal breach failure can occur in the nearshore zone when slope stability is locally broken (e.g., due to dredging or incision by currents). It is essential to note when evaluating safety that breaching may cause a "destabilizing" effect if the height of the breach face increases, leading to an uncontrolled retrogressive failure of the slope. A typical figure of the breaching mechanism is shown in Figure 3. The gravity flow of sand exiting from the retrogressing front starts and fuels sediment transfer, and the transported sand accumulates in the zone of a moderate slope as shown in Figure 3.

![img-2.jpeg](img-2.jpeg)

**Figure 3.** Coastal Breaching Mechanism: Processes and Factors Involved in the Formation and Propagation of Breaching Flow Slides and Associated Turbidity Currents.

Understanding the mechanisms and causes of coastal flow slides, including liquefaction flow slides, is crucial for developing effective approaches to mitigating their impact and preserving coastal areas. As highlighted by previous research, it is important to differentiate between different types of coastal failures to develop appropriate responses and management strategies.

To enhance our understanding of these processes, this research introduces a hybrid probabilistic model that can simulate the processes of coastal flow slides, including liquefaction flow slides. The model combines probabilistic approaches with numerical models to provide a more accurate representation of the underlying processes.

Figure 4 shows the occurrence of a coastal flow slide on the Amity Point beach. Photo (a) displays the beach before the flow slide event, while photo (b) shows the beach during the flow slide event. In this panel, you can see the failure of the coastal slope, which results in the movement of sand toward the sea. Photo (c) displays the aftermath of the flow slide event, where the beach has undergone significant changes due to the movement of sand and debris. The occurrence of coastal flow slides, as demonstrated in this figure, can have severe impacts on the coastal environment and can result in the loss of important habitats for marine life. Understanding the mechanisms and potential triggers of flow slides is crucial to effectively manage and mitigate their impacts, as discussed in the preceding sections.

![img-3.jpeg](img-3.jpeg)

Figure 4. Flow slide occurrence on the Amity Point beach.

# 3. Liquefaction Flow Slides 

When the soil in coastal areas becomes unstable and loses its strength owing to the presence of water, liquefaction flow slides may occur. Because of this, coastal towns and infrastructure are at risk of massive landslides and flow flows.

When soil is saturated with water and then shaken or exposed to additional forces, such as wave action or storm surge, liquefaction may occur. This may lead to a decrease in the soil's bearing capacity, as the soil particles lose contact with one another and become more fluid-like.

Liquefaction may be caused by earthquakes, storm surges, and intense rainfall in coastal locations. Liquefaction may cause a mass of saturated silt to flow downslope, often with additional debris. This poses a serious threat to human life and may have devastating effects on coastal infrastructure including buildings, roads, and bridges. The occurrence of coastal liquefaction flow slides is difficult to foretell because of the complexity of the event. Nevertheless, a variety of variables, such as the soil's type and composition, the availability of water in the soil, and the severity and length of the triggering event, might enhance the probability of such occurrences. The same applies to coastal breaching failure, which is also influenced by various factors that need to be carefully analyzed and accounted for in risk management strategies. Coastal engineers and Marine Spatial Planners may take many steps to reduce the likelihood of liquefaction flow slides occurring along the coast. Some of these measures include the use of deep foundations or reinforced concrete in the building of coastal structures to resist the effects of liquefaction. Coastal areas may also lessen the likelihood of soil liquefaction by taking measures such as enhancing drainage and decreasing soil moisture. Overall, coastal liquefaction flow slides pose a serious threat to coastal populations and infrastructure, necessitating cautious preparation and mitigating measures to lessen the likelihood of destruction and casualties.

## 4. The New Hybrid Bayesian Risk Model

This research introduces a novel Hybrid Bayesian Risk Model for evaluating vulnerability and threat from coastal flow slides. The Bayesian Risk Model, the 3-Dimensional Hydrodynamic Transport Model, and the MCS Model all come together for the first time in literature in this Hybrid Bayesian Risk Model (HBRM).

The Bayesian Risk Model is a statistical framework for evaluating potential dangers by integrating historical information with contemporary findings. It's a potent instrument that may aid in the quantification of risks, the identification of key variables, and the assessment of model-related uncertainties. The researchers can calculate the likelihood of coastal flow slides and assess the dangers involved by including this new Hybrid Model.

The BN Model is combined with 3-D Hydrodynamic Transport and MCS to form the Hybrid Bayesian Risk Model. Three-dimensional hydrodynamic transport applies to sediment and water flow modelling. This method provides a more precise depiction of the intricate relationships between water and sediment along coasts. In contrast, Monte Carlo simulations are a statistical method for investigating model uncertainty and diversity. To determine the range of potential outcomes and the probability associated with them, we can perform many simulations with varied inputs.

Using these three methods in the Hybrid Bayesian Risk Model, we have produced a robust instrument for evaluating vulnerability to and potential harm from Coastal Flow Slides (CFS). The model may aid policymakers in pinpointing vulnerable locations, assessing risks, and creating efficient plans to prevent coastal flow slips. Overall, the new Hybrid Bayesian Risk Model (HBRM) is a major step forward in coastal risk assessment and may help make coastal towns more resilient.

The HBRM incorporates various modules to consider critical environmental conditions of the limit state functions in terms of stability risk, such as wind, wave, current, and sediment transport, which are modeled by using HYDROTAM-3D, a simulation of the hydrodynamic transport and water quality in three dimensions. Previous research conducted by [11,12,13] has shown that HYDROTAM-3D has proved successful for a wide range of applications in real-life scenarios around the coast of Turkey.

The HYDROTAM-3D is supported by Geographic Information Systems (GIS) and cloud computing, which facilitates processes such as data entry and output and remote access to all functions through a graphical user interface that is controlled by a menu structure. The model has a relational database for Turkish coastal waters that includes bathymetries of all Turkish coasts, hourly wind data since the establishment of Turkish Meteorological Stations (MS) and measured physicochemical data at the sites.

The HBRM includes six sub-modules: Wind, wave, and current climates, sediment transport, Monte Carlo, and Bayesian network modules. The flow chart of the model procedure is demonstrated in Figure 5. The term "flow slide parameters" refers to a set range of values that will be adjusted to conduct a flow slide risk assessment. Table 2 lists the values used to characterize the CFS.
![img-4.jpeg](img-4.jpeg)

Figure 5. The flow chart of the new Hybrid Bayesian Risk Model for CFS.

Table 2. The CFS failure parameters of DSI.


The 3-D numerical model HYDROTAM-3D was also used for the simulation of transport processes in the Bay of Fethiye, Turkey [17]. They applied HYDROTAM-3D to simulate the transport processes in the Bay of Fethiye under different meteorological and oceanographic conditions and discussed the circulation patterns and their impacts on the water quality in the region. HYDROTAM-3D was applied as the sediment transport model to Akyaka Beach to study the sediment dynamics in the region. They applied HYDROTAM3 D to simulate the sediment transport in the region and discussed the impact of wave and current conditions on sediment dynamics. In this paper, to account for the impact of environmental factors, a comprehensive Three-Dimensional Numerical Hydrodynamic Transport Model HYDROTAM-3D is interrelated with the Monte Carlo Simulation (MCS) and Bayesian risk models.

The validity of HYDROTAM-3D has been tested through a series of case studies along the Turkish coastline for more than 20 years in more than 50 projects [11,13,18,19], by providing empirical evidence for its successful implementation. In this paper, HYDROTAM3D as the hydrodynamic sub-model was integrated with the Bayesian Risk Model of Coastal Flow Slides.
a. The wind climate module conducts long-term and extreme analyses of the wind data for the specified station. Moreover, this module analyses the data using ECMWF at each 0.1-degree horizontal grid spacing by 6 hourly time frames encompassing all Turkish coastal waterways between the years 2000 and 2022. It is possible to collect annual, seasonal, and monthly wind roses, all of which give information on the directional variation of wind speeds. The highest wind speeds and the directions in which they blow are examined, and then the prevailing wind direction for the area is analyzed and calculated. The statistical analysis of the yearly maximum wind speeds is performed using the Gumbel Probability distribution, and the most appropriate line is then fitted to the wind speeds presented in this study. Extrapolation to a greater value is thus feasible.
b. The wave climate module gives long-term significant wave statistics, annual and seasonal wave roses, and links among wave heights and periods [20]. In addition to this, it estimates the amplitude and duration of significant waves. The issue of coupled refraction and diffraction in the wave module is addressed by subjecting equations similar to the one provided by Ebersole (1985) to numerical analysis [21]. Three equations describing the wave phase function, wave amplitude, and wave approach angle make up the mild slope equation that computes the wave field resulting from the transformation of an incident, linear wave as they propagate over irregular bottom contours. The numerical model is quite effective when it comes to modeling wave propagation across wide coastal regions that are exposed to different wave conditions from a computational standpoint. It has been selected to make use of the sophisticated velocity potential $\Phi$ :

$$
\Phi=a e^{i s}
$$

in which, $a$ is wave amplitude, and $s$ is the function of the wave's scalar phase. To obtain the following equation, substitute Equation (1) into the equation that explains the twodimensional propagation of harmonic linear waves.

$$
\begin{gathered}
\frac{1}{a}\left[\frac{\partial^{2} a}{\partial x^{2}}+\frac{\partial^{2} a}{\partial y^{2}}+\frac{1}{C C g}(\nabla a \cdot \nabla(C C g))\right]+k^{2}-|\nabla s|^{2}=0 \\
\nabla \cdot\left(a^{2} C C_{g} \nabla s\right)=0
\end{gathered}
$$

in which $\nabla$ is horizontal gradient operator; $C$ is wave celerity; $C_{g}$ is group velocity; $k$ is wave number, respectively. They are determined by the dispersion regards. The combined

equations are determined for three wave parameters, wave height $H$, local wave angle $\theta$ and $|\nabla \mathrm{s}|$ :

$$
\begin{gathered}
\frac{\partial}{\partial x}\left(H^{2} C C g|\nabla s| \cos \theta\right)+\frac{\partial}{\partial y}\left(H^{2} C C g|\nabla s| \sin \theta\right)
\end{gathered}
$$

c. The current climate module includes three-dimensional modeling of wind, tide, or density stratification-induced currents, changes in water surface elevations, and storm surges. The Hydrodynamic Turbulence Module includes a three-dimensional k-c turbulence model for transport processes. In a Cartesian coordinate system with three dimensions, the equations that are used to regulate the system are as follows:

The continuity equation:

$$
\frac{\partial u}{\partial x}+\frac{\partial v}{\partial y}+\frac{\partial w}{\partial z}=0
$$

The momentum equations for the orthogonal horizontal directions x and y ;

$$
\begin{aligned}
& \frac{\partial u}{\partial t}+u \frac{\partial u}{\partial x}+v \frac{\partial u}{\partial y}+w \frac{\partial u}{\partial z}=f v-\frac{1}{\rho_{0}} \frac{\partial p}{\partial x}+2 \frac{\partial}{\partial x}\left(v_{X} \frac{\partial u}{\partial x}\right)+\frac{\partial}{\partial y}\left(v_{y}\left(\frac{\partial u}{\partial y}+\frac{\partial v}{\partial x}\right)\right)+\frac{\partial}{\partial z}\left(v_{y}\left(\frac{\partial u}{\partial z}+\frac{\partial w}{\partial x}\right)\right) \\
& \frac{\partial v}{\partial t}+u \frac{\partial v}{\partial x}+v \frac{\partial v}{\partial y}+w \frac{\partial v}{\partial z}=-f u-\frac{1}{\rho_{0}} \frac{\partial p}{\partial y}+\frac{\partial}{\partial x}\left(v_{X}\left(\frac{\partial v}{\partial x}+\frac{\partial u}{\partial y}\right)\right)+2 \frac{\partial}{\partial y}\left(v_{y} \frac{\partial v}{\partial y}\right)+\frac{\partial}{\partial z}\left(v_{z}\left(\frac{\partial v}{\partial z}+\frac{\partial w}{\partial y}\right)\right)
\end{aligned}
$$

and in the vertical direction $z$;

$$
\frac{\partial w}{\partial t}+u \frac{\partial w}{\partial x}+v \frac{\partial w}{\partial y}+w \frac{\partial w}{\partial z}=-\frac{1}{\rho_{0}} \frac{\partial p}{\partial z}+g z+\frac{\partial}{\partial x}\left(v_{x}\left(\frac{\partial w}{\partial x}+\frac{\partial u}{\partial z}\right)\right)+\frac{\partial}{\partial y}\left(v_{y} \frac{\partial w}{\partial y}+\frac{\partial v}{\partial z}\right)+2 \frac{\partial}{\partial z}\left(v_{z} \frac{\partial w}{\partial z}\right)
$$

where x and y represent the horizontal coordinates, z represents the vertical coordinate, $\mathrm{u}, \mathrm{v}$, and w are components of velocity in the $\mathrm{x}, \mathrm{y}$, and z directions at any grid place in space, and $t$ stands for time. The viscosity coefficients in the $\mathrm{x}, \mathrm{y}$, and z directions are denoted by $\nu_{x}, \nu_{y}$, and $\nu_{z}$, respectively. f : the coefficient of the Coriolis effect, $(x, y, z, t)$ : the water density at the current location, $\rho_{0}$ : the density used as a reference, g : gravitational acceleration, $\mathrm{p}=$ pressure.

Seawater density is influenced by its salinity, temperature, and, to a lesser extent, pressure. Salinity and temperature dispersion affect its dispersal. $\left(\sigma_{\mathrm{T}}\right)$ is a terminology used in oceanography to measure the density of seawater $\left(\sigma_{\mathrm{T}}\right)$ at a given temperature.
$\sigma_{\mathrm{T}}$ is defined in terms of sea water density $\left[\rho(\mathrm{S}, \mathrm{T})-1000 \mathrm{~g} / \mathrm{cm}^{3}\right]$, where $\rho(\mathrm{S}, \mathrm{T})$ is the density of seawater at a certain temperature T and salinity S at standard atmospheric pressure. For example, a water sample with a density of $1.027 \mathrm{~g} / \mathrm{cm}^{3}$ has a $\sigma_{\mathrm{T}}$ value of 27 . The relation between the two is:

$$
\sigma_{t}=(\rho-1) \times 10^{3}
$$

where $\rho$ : density in $\mathrm{g} / \mathrm{cm}^{3}$. The density increases noticeably with depth due to the increased hydrostatic pressure. This compression does not affect buoyancy or stability because all water masses moved up and down are similarly compressed. Therefore, the convention has been adopted to reduce all densities to $\sigma_{t}$ (at 1 atm pressure) and to neglect compressibility in the equations of motion. The following formulae are used to calculate density $\rho$ as a function of salinity ( S ) and temperature ( T ):

$$
C=999.83+5.053 d-0.048 d^{2}
$$

$$
\begin{gathered}
\beta=0.808-0.0085 d \\
\alpha=0.0708(1+0.351 d+0.68(1-0.0683 d) T) \\
\gamma=0.003(1-0.059 d-0.012(1-0.064 d) T) \\
\rho=C(d)+\beta(d) S-\alpha(T, d) T-\gamma(T, d)(35-S) T
\end{gathered}
$$

where S: salinity (\%), d: dynamic depth (km), T: temperature $\left({ }^{\circ} \mathrm{C}\right)$.
The model includes thermohaline forcing that occurs in enclosed water bodies. Solving the three-dimensional convection-diffusion equations allows for the calculation of the fluctuations in temperature as well as salinity. Equations of three-dimensional convective diffusion are utilized to figure out the temperature, and the equations for calculating salinity, by using Equation (16):

$$
\frac{\partial Q}{\partial t}+u \frac{\partial Q}{\partial x}+v \frac{\partial Q}{\partial y}+w \frac{\partial Q}{\partial z}=\frac{\partial}{\partial x}\left(D_{x} \frac{\partial Q}{\partial x}\right)+\frac{\partial}{\partial x}\left(D_{y} \frac{\partial Q}{\partial y}\right)+\frac{\partial}{\partial z}\left(D_{z} \frac{\partial Q}{\partial z}\right)
$$

The turbulent diffusion coefficient is denoted by the letters Dx, Dy, and Dz, which stand, in that order, for the directions x, y, and z. Q: temperature (T), or salinity (S).

# Verification of Hydrodynamic Sub-Model 

One of the verifications of the hydrodynamic sub-model HYDROTAM-3D was through a physical (hydraulic) model study performed in the Coastal Engineering Laboratory of the Middle East Technical University in Turkey. The velocities in the physical model were measured at the grid points neighboring the intake and then used as the boundary conditions in the mathematical HYDROTAM-3D model. The length scale of the hydraulic model was 1:50, where the length and width of the rectangular model marina basin were 5.80 and 2.8 m , respectively, and the average water depth was 0.2 m . Using the length scale of 1:50, these dimensions correspond to a prototype marina of $290 \mathrm{~m} \times 140 \mathrm{~m}$, with a water depth of 10 m . Surface water was withdrawn from the marina by installing a morning-glory spillway structure as forced flushing, which consists of a vertically placed conical shaft connected to a horizontal discharge pipe placed on the seabed. Velocity measurements were taken using a 'Minilab SD-12 microscale 3-axis ultrasonic current meter. The morning-glory-shaped intake structure was placed at various locations in the basin, and the grid system used had a square mesh size of $10 \mathrm{~m} \times 10 \mathrm{~m}$. In HYDROTAM-3D, the vertical eddy viscosity was calculated by the $\mathrm{k}-\varepsilon$ model, and horizontal eddy viscosities were predicted by the sub-grid scale turbulence model. The water depth was divided into ten layers of equal thickness, and the density of water was taken as $1025 \mathrm{~kg} / \mathrm{m}^{3}$. At $t=0$, the pump was started, so that the water began to flow in the intake, whereas the remaining part of the water body was assumed to be at rest, and the water surface was horizontal. Steady-state conditions were reached approximately 1.5 h after the start of pumping in the hydraulic model.

The paths followed by the floats in the physical model were compared with the results obtained from the mathematical model HYDROTAM-3D in Figure 7. The average velocities along the paths followed by the floats in both physical and HYDROTAM-3D models were compared. The results show that the numerical model performs well in predicting the path of float number 2, released at location ( $100 \mathrm{~m} \times 0 \mathrm{~m}$ ), with an average velocity relative error of $0.55 \%$. This study demonstrated that the mathematical model accurately predicted the behavior of the physical model for forced flushing, one of the validations of the hydrodynamic sub-model HYDROTAM-3D in literature is given in Figure 7.

![img-5.jpeg](img-5.jpeg)

Figure 7. The comparison of float paths and velocity distributions at the surface layer as obtained from the mathematical model of HYDROTAM-3D with the physical (hydraulic) model when the morning glory is placed on the right-end corner of the marina.
d. The sediment transport module is interrelated with the hydrodynamic transport and turbulence modules. The Boussinesq approximation, a commonly used method that assumes that the density change is minimal in comparison to the velocity, is employed to calculate the Navier-Stokes equations in the hydrodynamic model component. To find the solution, finite elements, and finite differences are employed, combining the strengths of both techniques. The vertical plane is modeled using finite element shape functions and the horizontal plane using finite difference approximations. In a Cartesian coordinate system, the equations that regulate the system are solved implicitly.

The long-term wave environment of the region was analyzed using wind readings from meteorological stations and the European Centre for Medium-Range Weather Forecast (ECMWF) wind predictions for 30 years. Wind statistics by the hour as well as fetch lengths were used to calculate wave heights, wave durations, and wave directions. These calculations formed the basis for the wave transformation model, which is built upon the nonlinear shallow water formulas that have vertical averaged and constant density streams.

The use of the Boussinesq approximation and the finite elements and finite differences approaches in HYDROTAM-3D offers a robust and efficient solution to the Navier-Stokes equations. The combination of wind readings and ECMWF wind predictions provides a comprehensive view of the long-term wave environment of the region. The use of the vertically averaged nonlinear shallow water equations as the foundation for the wave transformation model ensures that the model accurately captures the physics of wave hydrodynamics.

This study also demonstrates the use of advanced numerical modeling techniques and comprehensive data collection to analyze the long-term hydrodynamics of the region. The results of this study contribute to the larger body of knowledge on the modeling of fluid dynamics and wave propagation and can be used to inform decision-making in maritime and coastal engineering.

$$
\frac{\partial u}{\partial t}+u \frac{\partial u}{\partial x}+v \frac{\partial u}{\partial y}=-g \frac{\partial \eta}{\partial x}+\left(\frac{\partial^{2} u}{\partial x^{2}}+\frac{\partial^{2} u}{\partial y^{2}}\right)-\frac{g u|u|}{C^{2} H}+\frac{F_{x}}{g H}
$$

$$
\begin{gathered}
\frac{\partial v}{\partial t}+u \frac{\partial v}{\partial x}+v \frac{\partial v}{\partial y}=-g \frac{\partial \eta}{\partial y}+\left(\frac{\partial^{2} v}{\partial x^{2}}+\frac{\partial^{2} v}{\partial y^{2}}\right)-\frac{g v|\mathrm{v}|}{C^{2} H}+\frac{F_{y}}{g H} \\
\frac{\partial \eta}{\partial t}+u \frac{\partial(H u)}{\partial x}+v \frac{\partial(H v)}{\partial y}
\end{gathered}
$$

where $u$ and $v$ are the $x$ - and $y$-directional depth-averaged current velocity components, respectively; $\mathrm{H}=\mathrm{h}+\eta$ total water depth; h : still water depth; g : gravity acceleration; C : Chezy friction coefficient; $v$ : turbulent eddy viscosity coefficient; $\eta$ : water surface elevation; wave-induced forces in the directions of $x$ and $y$, respectively, are denoted by the letters Fx and Fy. It can also be written Fx and Fy as:

$$
F_{x}=-\left(\frac{\partial S_{x x}}{\partial x}+\frac{\partial S_{x y}}{\partial y}\right), F_{y}=-\left(\frac{\partial S_{y x}}{\partial x}+\frac{\partial S_{y y}}{\partial y}\right)
$$

where $S_{x x}$ and $S_{y y}$ are the components of the normal radiation stress that are acting, respectively, on the plane that is perpendicular to the $x$ and $y$ axes. The following are the sources from which radiation stress calculations are derived:

$$
\begin{gathered}
S_{x x}=E\left[\left(2 n-\frac{1}{2}\right)-n \sin ^{2} \theta\right] \\
S_{y y}=E\left[\left(2 n-\frac{1}{2}\right)-n \sin ^{2} \theta\right] \\
S_{x y}=\operatorname{En} \sin \theta \cos \theta
\end{gathered}
$$

where $\mathrm{n}=\mathrm{C}_{\mathrm{g}} / \mathrm{C}, \mathrm{E}=\rho \mathrm{gH}^{2} / 8$ wave energy, $\rho=$ water density, $\emptyset=$ incident wave angle, $\mathrm{C}_{\mathrm{g}}=$ group velocity of waves, $\mathrm{C}=$ wave celerity and $\mathrm{H}=$ wave height.

The partial differential equations of the wave-induced current model are solved using a sequence of finite difference equations on a stepped spatial grid. Nonlinear terms may be approximated using upwind-downwind approximations. In areas with strong spatial gradients, the combined model's finer resolutions may be a benefit. The Runge-Kutta Fehlberg Method, which involves six function evaluations per step and offers an automated error estimate, is used to solve the nonlinear equation system. The numerical model of wave-induced currents uses a staggered spatial grid and a no-flow boundary condition at the coastline. At the lateral borders, a uniform flux-type boundary condition is applied, with the flux at the adjacent interior grid equal to that at the lateral boundary grid. The longshore sediment model is based on long-term wave statistics. The occurrence probability for each direction is considered in the model. Net and gross longshore sediment transport rates are calculated with the CERC method [22].
e. The climate change module uses the Sea Level Rise Projections for the climate change scenario of RCP8.5 for the determination of extreme design water levels of the project area. CMIP6 (Coupled Model Intercomparison Project Phase 6) is the sixth phase of the standard experimental framework for studying the output of combined atmosphereocean general cycle models.
f. The MCS module presents the development of a statistical model for conducting failure analysis of Coastal Flow slides. The module simulates the stability failure function, to provide a comprehensive understanding of the various factors that could contribute to coastal flow slides system failure. The results of the simulation deliver statistical distributions of failure probabilities, which can be used to estimate the risk associated with CRB failures under various conditions.
g. The Bayesian network module: The traditional method for forecasting the probability of events involved representing the "joint distribution," which stored one probability value for each possible combination of states. However, this approach could result in a large number of calculations, as the total number of states for each node was multiplied by

the total number of states in the joint distribution. Bayesian networks offer a more efficient solution. They only connect nodes that are probabilistically related by dependent relationships, thus reducing the number of possible combinations that need to be considered. The flexibility of Bayesian networks has contributed to their widespread use and success. They can be applied to complex systems involving interrelated variables, such as active wall velocity, which plays a critical role in understanding sediment erosion in coastal flow slides. The Bayesian network can evaluate various parameters to calculate the active wall velocity, which reflects the rate at which a vertical underwater slope propagates horizontally due to coastal flow slides. This calculation allows for an estimation of the rate at which the underwater slope is propagating. It was described as the active wall velocity by underlying its physical principles [23].

This research enhances the understanding of the intricacies of the erosion process by the probabilistic simulation model and improves the ability to estimate sediment erosion rates by combining with the HYDROTAM-3D sediment transport module:

$$
v_{w}=\frac{\sin (\varphi-\alpha)}{\sin \varphi} \frac{\rho_{s-} \rho_{w}}{\rho_{w}} \frac{\left(1-n_{0}\right) k_{l}}{\Delta n}
$$

where $\mathrm{n}_{0}$ represents the porosity of the sand measured in situ, $\rho_{\mathrm{s}}$ represents the particle density, $\rho_{w}$ represents the water density, $k_{l}$ represents the permeability in the loose state, $\varphi$ represents the angle of the internal friction, $\alpha$ represents the angle of the beach slope, and $\Delta n$ represents the relative change in porosity.

$$
\Delta n=\frac{n_{f}-n_{o}}{n_{f}}
$$

in which $n_{f}$ is the largest value of porosity. The sediment particle velocity is obtained from the sediment transport model and is controlled in MCS by using Equation (10):

$$
v_{\text {sed }}=\frac{S-E}{\rho_{s}\left(1-n_{0}-\overline{c_{b}^{\prime}}\right)}
$$

where s: settling flux, $\mathrm{E}=$ pick-up flux.
Van Rhee, 2015 proposed the critical angle slope is given in Equation (27).

$$
i_{c r}=0.0049\left[30 \rho_{s}\left(1-n_{0}\right) H k_{0}\right]^{-0.39} D_{50}^{0.92}
$$

Using N various particle sizes, it can be defined the vertical velocity $\mathrm{v}_{\mathrm{z}, \mathrm{j}}$ of a particle of size $D_{j}$.

$$
v_{z, y}=w+\sum_{k=1}^{N} c_{k} v_{s, k}-v_{s, j}
$$

where w is the vertical flow velocity obtained from the hydrodynamic model. For a uniformsized mixture, the settling velocity $\mathrm{w}_{\mathrm{s}}$ of a given size corresponds to the slip velocity $v_{s, j}$, which depends on the sediment concentration. The Shields parameter gives the relationship between grain size diameter and the dimensionless parameter to calculate the initiation of motion as given by Equation (29):

$$
\tau_{*}=\theta=\frac{\tau}{\left(\rho_{s}-\rho_{w}\right) D_{50}}
$$

where $\tau$ is dimensional shear stress, $\rho_{s}$ is the density of the sediment, $\rho_{w}$ is the density of water, and $\mathrm{D}_{50}$ is the median particle size.

Considering the surface area dS and the control volume $\mathrm{d} \Omega$, the applied horizontal and vertical momentum equations are given by:

$$
\frac{\partial}{\partial t} \int \Omega \rho u \mathrm{~d} \Omega+\int_{S} \rho u \vec{v} \cdot \vec{n} \mathrm{~d} S=\int_{S} \tau_{s j} i_{j} \vec{n} \mathrm{~d} S-\int_{S} p i_{s} \cdot \vec{n} \mathrm{~d} S
$$

$$
\frac{\partial}{\partial t} \int_{\Omega} \rho w \mathrm{~d} \Omega+\int_{S} \rho w \vec{v} \cdot \vec{n} \mathrm{~d} S=\int_{S} \tau_{z j} i_{j} \vec{n} \mathrm{~d} S-\int_{\Omega} \rho g \mathrm{~d} \Omega
$$

The continuity equation for incompressible fluids is written as:

$$
\int_{S} \vec{v} \cdot \vec{n} \mathrm{~d} S=0
$$

where p represents the pressure, u and w represent the horizontal and vertical flow velocities, v represents the velocity vector, and $\rho$ is the sediment-water mixture density, $\vec{i}_{i, j, z}$ are unity vectors as obtained from the hydrodynamical model. The transport equation is given in Equation (33) and the sediment concentrations were estimated by the sediment transport module of HYDROTAM-3D.

$$
\frac{\partial}{\partial t} \int_{\Omega} c_{j} \mathrm{~d} \Omega+\int_{S} c_{j} \vec{v}_{z, j} \cdot \vec{n} \mathrm{~d} S=\int_{S}\left(\Gamma c_{j}\right) \cdot \vec{n} \mathrm{~d} S
$$

where $v_{z, j}$ denotes the particle size of the sediment, c is the sediment concentration, and $\Gamma$ is the diffusion coefficient. The Hydrodynamic and Sediment Transport sub-models are interrelated with the Monte Carlo Simulation and Bayesian Networks.

The Monte Carlo Simulation Risk Assessment Model was developed for the design of natural gas pipelines in İzmit Bay [13]. In this paper, we suggest the coupling of the HYDROTAM-3D model with Monte Carlo Simulation to quantify the uncertainties associated with the coastal flow slides mechanism.

# 5. The Durap Sensitivity Index (DSI) of CFS Failure 

G. Van den Ham et al. 2014 proposed a criteria-based evaluation of coastal flow slides [8]. Nevertheless, this approach is limited because it does not account for several important factors. These factors include dredging rate, number of coastal buildings, coastal slope, packing type, driving forces, and so on. In addition, the suggested method does not have anything that sets it apart, therefore it implies an equal likelihood of flow slide breaching and liquefaction. Assumptions underpin the methodology as well, which may not be reflective of the complexities of coastal flow slides. In addition, the suggested technique does not ensure that liquefaction, rather than breaching, would occur, which may have major ramifications for risk evaluation and mitigation plans.

Sassa and Takagawa, 2019 presented a stochastic evaluation of static liquefaction in a predominantly dilative sand fill [24]. The study used statistical methods to analyze the variability of soil properties and their impact on the liquefaction potential. The authors found that the critical state friction angle was the most significant factor affecting the probability of liquefaction. They also compared the results of the stochastic analysis with deterministic methods and found that the stochastic approach provided a more realistic and reliable assessment of the liquefaction potential. Overall, the study provided insights into the behavior of predominantly dilative sand fills under static loading conditions and highlighted the importance of considering uncertainty in soil properties in the assessment of liquefaction potential. The method for assessing landslides in marine environments has proven to be a useful tool for predicting and managing potential landslides. However, like any method, there are limitations to its application. One of the primary drawbacks of this approach is that it does not account for coastal flow slides. Coastal flow slides are a specific type of landslide that occurs on slopes near the coastline and is characterized by the movement of material in a fluid-like manner.

Additionally, there are several critical factors that this method does not take into consideration. For example, factors such as dredging rate, the number of buildings located along the coast, coastal slope, packing type, and driving forces, all have a significant impact on the likelihood and severity of landslides in marine environments. Neglecting these

critical factors can lead to underestimating the potential risk and impact of landslides in the area.

Furthermore, while the method for liquefaction was useful for identifying potential areas of liquefaction, it did not consider all coastal flow parameters. The coastal flow slide parameters are critical parameters that can significantly impact the severity and extent of liquefaction. Neglecting these parameters can lead to a misinterpretation of the risk of liquefaction in the area.

Lastly, the method did not label the parameters in terms of posing a danger for liquefaction. Without labeling the parameters in terms of posing a danger for liquefaction, it can be challenging to determine the level of risk associated with each parameter. Overall, while the method for assessing landslides in marine environments was useful, it is essential to recognize its limitations and take into account additional critical factors to accurately predict and manage potential landslides in the area.

Stoutjesdijk et al., 1998 discussed a method for predicting flow-slides on slopes based on slope geometry [25]. The study examined the relationship between the geometry of the slope and the likelihood of flow-slides. The paper provided a detailed explanation of the flow-slide prediction method, including the critical geometry that affects flow-slide initiation and the corresponding mathematical equations.

The study involved examining data from several flow-slide events that occurred on different slopes to determine the critical slope geometry parameters that influence flowslide initiation. The researchers analyzed the data using statistical methods to identify the critical slope geometry parameters and developed mathematical equations for predicting flow-slides based on these parameters.

The paper concluded that the flow-slide prediction method based on slope geometry was a useful tool for predicting flow-slides and could provide valuable information for managing potential flow-slide hazards. The paper focused solely on the influence of slope geometry on flow-slide prediction, and it did not consider other factors that could influence flow-slides, such as dredging rate, number of coastal buildings, coastal slope, packing type, and driving forces. Therefore, the weakness of the paper was that it provided a limited understanding of flow-slide prediction, as it only focused on one aspect of the problem, which was geometry, and neglected other critical factors that could significantly impact flow-slide initiation and propagation.

Thus, further studies are required to provide more thorough and precise methodologies for evaluating and forecasting coastal flow slides. Therefore, to properly detect the danger of Coastal Flow Slide (CFS) failure and designate the most susceptible coastal locations at risk of suffering such failure, we developed the Durap Sensitivity Index (DSI). We devised a complex hybrid model to accomplish this goal, one that accounts for all the potential outcomes of flow slides while also accounting for the unpredictability of the variables utilized in the new sensitivity index of DSI.

The Durap Sensitivity Index (DSI) is an innovative tool developed to detect the risk of Coastal Flow Slide (CFS) failure and pinpoint the most vulnerable coastal locations. The DSI utilizes a complex hybrid model that integrates three independent models to achieve high accuracy in predicting the likelihood of CFS failure. Our goal is to provide a computationally efficient and reliable method for calculating the critical zone of CFS using this novel hybrid model and risk index. Predicting, preventing, and mitigating the negative consequences of CFS failure on coastal regions is projected to be much enhanced by the DSI and by integrating the hybrid model. Calculation of the DSI is determined by using the parameters listed in Table 2, where DSI is the coastal flow slides sensitivity index of Durap. This index is calculated by using the following parameters of $k_{B F}$ and $k_{L}$, where $k_{B F}$ is the coefficient of breaching and $k_{L}$ is the liquefaction coefficient. The breaching coefficient $k_{B F}$ consists of the following variables: dredging rate, slope, packing type, and type of driving force. The liquefaction coefficient $\left(k_{L}\right)$ depends only on the dredging rate, slope, densely packed slope, and mass flow as driving forces.

The calculation of CFS coefficients is given in Equation (34):

$$
k_{i}=\sqrt[n]{p_{1} \times p_{2} \ldots \ldots \ldots \times p_{n}}
$$

Each of the variables represents a different facet of the sediment transport process, and they are labeled as P1 through P7. The dredging rate, denoted by P1, is the quantity of silt being dredged from a certain region. P2 is the total number of manmade coastal features that may guide sediment flow or generate eddies. Slope P3, categorizes distinct sorts of slopes that might affect sediment flow. Packaging type, P4 is a loosely packed slope, and P5 is a densely packed slope.

Turbidity, or the quantity of sediment in suspension, is denoted by the symbol P6 and denotes the prevailing current. This factor is crucial because it affects the likelihood of liquefaction and breaching; and may change the total flow of sediment. The entire quantity of silt being moved is shown by the seventh symbol, P7, which stands for mass flow.

A collection of constant variables relevant to both the liquefaction and breaching processes is represented by the letter i in Equation (34). The qualities of the silt being carried, the durability of the coastal constructions, and similar elements may all be considered further constants.

Predicting the likelihood of liquefaction and breaching in coastal locations requires an understanding and quantification of these factors. Researchers may create models to better forecast and manage the possible harm caused by coastal sand flow by analyzing the many components that contribute to these hazards.

Equation (35) is used to generate the DSI for either breaching-prone or liquefactionsensitive zones. If the packing type is densely packed and the driving force is mass flow, then these two parameters encompass in the calculation of $\mathrm{k}_{\mathrm{L}}$, since they are the main reasons for the liquefaction type of failure of the slope, as given in Equation (35).

$$
k_{L}=\sqrt[3]{p_{1} \times p_{2} \times p_{3} \times p_{4} \times p_{7}}
$$

The Sensitivity Index of CFS to DSI Parameters in long term is given in Table 3. DSI is a numerical ranking system used to assess the sensitivity of breaching failure and liquefaction flow slides. It ranges from 1 (very low sensitivity) to 5 (very high sensitivity). The DSI parameters are based on several factors, such as dredging rate, number of coastal structures, slope angle, and packing type (for both loosely and densely packed sediment). Other parameters such as driving force (specifically turbidity current) and mass flow are also considered. Each DSI parameter has a qualitative term and corresponding quantitative range that helps determine the DSI ranking. In the short run, the dredging range is given in Table 4.

Table 3 presents the qualitative terms for different parameters and their associated values for dredging rate, number of coastal structures, slope, packing types, driving force, and mass flow. The qualitative terms range from very low to very high, and they provide a general description of the CFS conditions. The values associated with each qualitative term are specific and include the range of dredging rate in cubic meters per year, the number of coastal structures, slope angle in degrees, packing types, and driving force. While (P6), turbidity current, is associated with CRBF, the last parameter (P7), mass flow, describes the regime changes for LFS. The table provides a useful reference for assessing the potential impacts of dredging activities on coastal environments, and it can be used to develop appropriate management strategies for coastal areas.

Table 3. Sensitivity Index of CFS to DSI Parameters (Long term).

Type-Loosely
Packed (P4) | Packing
Type-Densely
Packed (P5) | Driving
Force-Turbidity
Current (P6) | Mass Flow (P7) |

Table 4. Dredging intensity levels and their approximate volumes $\left(\mathrm{m}^{3} / \mathrm{h}\right)$.


Table 4 provides the dredging intensity levels and approximate volume in cubic meters per hour $\left(\mathrm{m}^{3} / \mathrm{h}\right)$ and is intended for short-term risk assessment purposes. The dredging intensity levels range from no dredging to very high or heavy dredging, and each level corresponds to a specific approximate volume of material that is being dredged per hour. This table can be used as a reference for assessing the risk associated with different dredging intensity levels, especially in the short-term period.

Table 5 provides a summary of the different slope categories (Flat, Gentle, Moderate, Steep, and Very Steep) based on their angle range and the corresponding description. It highlights the suitability of each slope category for different types of coastal structures based on their required stability and control of Coastal Flow Slides (CFS). Table 5 also provides recommendations on the required level of CFS control and additional stabilization measures for each slope category.

Table 5. Slope Classification and recommendation for CFS.


Equations (34) and (35) are used to generate the DSI for either breaching-prone or liquefaction-sensitive zones. Following that, the main risk levels are described by using the following percentages ranging from Level I: $(0-25) \%$, Level II: $(25-50) \%$, Level III: $(50-75) \%$, Level IV: $(75-100) \%$, respectively. To put it another way, a sensitivity score of Level I indicates the least amount of risk, while a sensitivity score of Level IV indicates the greatest amount of risk. Finally, the Durap Sensitivity Index (DSI) can be written in terms of coastal flow slides and liquefaction flow slides as given in Equation (36):

$$
D S I=k_{L} \cdot P\left(V_{\text {liquefaction }}\right)+k_{B F} \cdot P\left(V_{\text {breach }}\right)
$$

If the first part of the DSI equation, $k_{L} \cdot P\left(V_{\text {liquefaction }}\right)$, is greater than the second part, then the flow slide is dominated by breaching or vice versa, as given in Equations (37) and (38).

$$
0.5<\frac{k_{B F} \cdot P\left(V_{\text {breach }}\right)}{k_{L} \cdot P\left(V_{\text {liquefaction }}\right)}<1 \text { breaching dominated failure }
$$

$$
0.5<\frac{k_{L} \cdot P\left(V_{\text {liquefaction }}\right)}{k_{B F} \cdot P\left(V_{\text {breach }}\right)}<1 \text { liquefaction dominated failure }
$$

The probabilities of liquefaction $P\left(V_{\text {liquefaction }}\right)$ and breaching $P\left(V_{\text {breach }}\right)$ are determined from the MCS module.

# 6. Application of the Hybrid Risk Model to the Osman Gazi Bridge 

The case study focuses on the slopes in the eastern Marmara Sea of Izmit Bay near the Osman Gazi Bridge (Figure 8), which is an earthquake area sensitive to slope failures. In the case study, the analyzed slope is illustrated in Figure 8.
![img-6.jpeg](img-6.jpeg)

Figure 8. The case study area of the Osman Gazi Bridge Footing (The concern point for this study is point 1).

By employing the earthquake risk assessment component in the event of a tsunami, the hybrid model may manage the link between earthquake risk and coastal flow slide vulnerability. This has the potential to lessen the likelihood of coastal erosion and other tsunami-related dangers.

The hybrid model may then be used to create early warning systems that can inform coastal populations of impending danger from earthquakes and related hazards such as coastal flow slides. These systems may help coastal towns become more resilient and lessen risks from natural disasters by delivering early and accurate information.

In the seismic section, we employed geological information to locate and characterize fault lines under the sea bottom. Based on these findings, a model can be included to estimate the ground movements that would arise from an earthquake along the fault lines.

Soil type, ground water levels, earthquakes, and changes in water pressure all have a role in the likelihood of liquefaction flow slides occurring on coastlines. The situation at Osman Gazi Bridge Footing is a good illustration of this.

In a flat coastal plain with abundant amounts of soft clay, the footing for the Osman Gazi Bridge was laid. The high-water content of these deposits made the footing vulnerable to liquefaction during earthquakes. Moreover, the closeness to the sea increased the groundwater pressure there.

During the building of the bridge, the footing's weight compressed the earth underneath it, raising groundwater pressure and increasing the soil's liquefaction risk. One of the bridge footings encountered liquefaction risk when a 5.2 magnitude earthquake hit the area in 2011.

Coastal building projects should not be started without first learning about the site's geological and geotechnical characteristics, as shown by this occurrence. Because of the information, it provides about the seafloor's composition and the closeness to faults and other geological features that may impact the stability of the shoreline, geomorphology data may be used to assist estimate the danger of coastal liquefaction flow slides. Accurate risk assessments and coastal infrastructure design and development are both aided by these data. The drilling sites and bathymetric/geotechnical surveys in front of the slope are demonstrated in Figure 9.
![img-7.jpeg](img-7.jpeg)

Figure 9. Drilling sites, bathymetric and geotechnical surveys along the analyzed slope in Section 5. A: silt and clay, B: clay, C: medium sand (Adopted from [26]).

# 6.1. Application of Wind Climate Sub-Model 

Izmit Bay is in the Marmara Sea, a body of water that connects the Black Sea to the Aegean Sea. The bay is approximately 48 km in length and ranges in width from 1.8 to 9 km . It is part of a two-layered current system, which means that there are different layers of water with different characteristics flowing through the bay.

To determine the wind climate of the project area, wind predictions of ECMWF Operational Archive (OA) at the closest oversea coordinates of $40^{\circ} 42^{\prime} \mathrm{N}-29^{\circ} 18^{\prime} \mathrm{E}$ have been analyzed. When the annual wind climate is examined, it has been determined that the winds blowing from NE and ENE directions are dominant with mean speeds of $4.2 \mathrm{~m} / \mathrm{s}$ and $3.7 \mathrm{~m} / \mathrm{s}$, respectively. In winter, prevailing winds blowing from SSE and NE directions were observed, in other seasons, it was determined that winds blowing from NNE and ENE directions were dominant. The wind data of ECMWF-OA are compared with the data obtained from İzmit Meteorological Station in Figure 10. The comparison studies show that the ECMWF OR wind forecasts are 2.1 times higher than the meteorological station on land and can be safely used to determine the wind climate of the study area.

![img-8.jpeg](img-8.jpeg)

Figure 10. Comparison of wind sources of ECMWF-OA with İzmit Meteorological Station (The red line is the linear regression of the data).

# 6.2. Application of Wave Climate Sub-Model 

İzmit Bay wave climate studies have been carried out by using the wave predictions obtained from the ECMWF Operational Archive (OA) coordinates of $40^{\circ} 42^{\prime} \mathrm{N}-29^{\circ} 18^{\prime}$ E. Studies on long-term wave statistics have been carried out using wave data predicted from a wave model for the years 2000 to 2022.

The ECMWF wave predictions with the WAM model were utilized for the case study. The WAM model, a third-generation wave model, is one of the most extensively used models globally by the Wave Model Development and Implementation Group [27]. The dominant wave directions originate from the WSW-NW sector, signifying that waves are formed in the Marmara Sea and subsequently travel towards İzmit Bay. During summer and spring, waves originating from the inner bay are also observed from the NE sector in the prevailing wind directions, where fetch distances are comparatively shorter.

A wave rose typically consists of a circle with spokes radiating outwards, where each spoke represents a specific direction from which waves may come, and the length of the spoke represents the proportion of waves that come from that direction.

The current pattern of concerning area is shown in Figure 11. The annual wave rose provides information on the prevailing wave heights and directions in Izmit Bay, which is important for understanding the local wave climate and the associated risks to coastal communities and infrastructure. Additionally, it was discovered that waves traveling from the north-northeast directions were the most common wave directions having a monthly average significant wave height of $\mathrm{H}_{\mathrm{a}}=1.5 \mathrm{~m}$ during the past 20 years.

![img-9.jpeg](img-9.jpeg)

Figure 11. The HYDROTAM-3D model was used to produce current pattern.

# 6.3. Application of Climate Change Sub-Model 

The increase in the Mean Sea Level (MSL) of Izmit Bay was determined by the data of the Climate Change module. According to the RCP8.5 scenario, it is predicted that average temperatures will tend to increase in the Izmit Bay area at $+1.5^{\circ} \mathrm{C}$ in the first period. It is expected that the temperature will rise to $2^{\circ} \mathrm{C}$ in the 2041-2070 period and above $3.5^{\circ} \mathrm{C}$ in the 2071-2099 period (DC, 2023). By considering this trend, the MSL increase in the future is predicted by MCS considering global warming. The MWL increase is coupled with HYDROTAM-3D model, and the wind set-up, tidal effect, and wave set-up that may occur in the bay were cumulatively determined.

The MSL increase was predicted as 0.43 m in the next 50 years by determining the effects of the storm from the wave and wind climate modules. These modules were interrelated with MCS to estimate the water level variation of Izmit Bay.

### 6.4. Application of Current Climate Sub-Model

Considering the MWL change, the variations of wind and wave-generated currents are predicted by the HYDROTAM-3D model. The bathymetry of İzmit Bay was obtained in Mercator ED $502911 / 50000\left(41^{\circ}\right)$ scale from the Department of Navigation and Hydrography of Turkey. The area between the coordinates of $40^{\circ} 48.733^{\prime} \mathrm{N}-29^{\circ} 15.240^{\prime} \mathrm{E}$ and $40^{\circ} 39.6426^{\prime} \mathrm{N}-29^{\circ} 56.7679^{\prime} \mathrm{E}\left(58,398.11 \mathrm{~m} \times 16,824.64 \mathrm{~m}\right)$ was modeled with a grid system of $120 \times 36$ cells having dimensions of $65 \mathrm{~m} \times 467.35 \mathrm{~m}$ covering the entire bay (Figure 12).
![img-10.jpeg](img-10.jpeg)

Figure 12. The grid system of the hydrodynamic model.

The model calibration data were taken from the Cooling Water Deep Sea Outfall and Aksa Container Port Projects, Hydrographic and Oceanographic Survey Report (P.NO: 190812-A) in the İzmit Bay.

Current measurements made at two measurement points $\left(40.700152^{\circ} \mathrm{N} 29.413878^{\circ} \mathrm{E}\right.$ and $40.700329^{\circ} \mathrm{N} 29.418689^{\circ} \mathrm{E}$ ) on 22-23-24-25 and 26 March 2018 and 22 and on 23 March 2018, regarding salinity, temperature, and water density measurements, were carried out at six points, and their annual variation is illustrated in Figure 13.
![img-11.jpeg](img-11.jpeg)

Figure 13. The variation of seawater salinity and temperature in İzmit Bay.
Figure 14 displays the average upper layer currents under prevailing wind conditions blowing from NE, showing that the waters in the Gulf of İzmit move in the WSW direction with the upper currents. The circulation patterns in İzmit Bay are known to be turbulent and irregular. To account for this complexity, the model incorporates eddy viscosities and diffusivities to link the turbulent and mean motions in both horizontal and vertical directions. The isotropic $\mathrm{k}-\varepsilon$ model is used to calculate the eddy viscosity values in the vertical direction. The water temperature and salinity of the bay are considered monthly changing variables taken from the database of the HYDROTAM-3D Model.
![img-12.jpeg](img-12.jpeg)

Figure 14. The average currents (V) of İzmit Bay (a) surface (b) sea bottom as obtained from wind prevailing from SE direction.

The dominant surface currents are in the WNW and WSW directions, with average velocities of $11.86 \mathrm{~cm} / \mathrm{s}$ and $12.40 \mathrm{~cm} / \mathrm{s}$, and maximum velocities of $14.72 \mathrm{~cm} / \mathrm{s}$ and $14.94 \mathrm{~cm} / \mathrm{s}$, respectively. It has been determined that the prevailing current in the winter season is in the N and NNE directions with average current velocities of $11.68 \mathrm{~cm} / \mathrm{s}$ and $11.35 \mathrm{~cm} / \mathrm{s}$, respectively.

In other seasons, the directions of the dominant current change, in spring they are in SSW and W directions. In summer, they are WSW and WNW, and in autumn, they are in the WNW and W directions. Average current velocities vary between $11.35 \mathrm{~cm} / \mathrm{s}$ and $12.71 \mathrm{~cm} / \mathrm{s}$. The maximum velocities of the prevailing currents fluctuate between $14.50 \mathrm{~cm} / \mathrm{s}$ and $20.00 \mathrm{~cm} / \mathrm{s}$.

The wind and wave generated current pattern on the sea surface at the steady state after ten hours of prototype simulation in which the wind was blowing uniformly at $10 \mathrm{~m} / \mathrm{s}$ from the NNW direction is given in Figure 15.
![img-13.jpeg](img-13.jpeg)

Figure 15. The pattern of the currents on the surface of the water at steady state with winds coming from the north-northwest at 10 m per second.

# 6.5. Application of the Sediment Transport Module 

The longshore sediment model is based on long-term wave statistics. The occurrence probability for each direction is considered in the model. Net and gross longshore sediment transport rates are calculated with the CERC method. The gross transport is computed in Figure 16 by summing the probabilities of occurrences of effective directions obtained from the long-term probability distributions of ECMWF-OR.
![img-14.jpeg](img-14.jpeg)

Figure 16. The sediment transport rates $\left(\mathrm{m}^{3} /\right.$ year) of the study area were obtained from the 3D hydrodynamic model.

### 6.6. Application of the MCS Module

The values of active wall height were found in a range of 0.1 to 1 m , which is critical. These thresholds are crucial to prevent the environmental deterioration that may be caused by the coastal flow slides. Hence, considering the hydrodynamic modeling, the variations of

main design parameters and probability distributions are determined and now modeled in the MCS as given in Table 6. The characteristic fluid parameters in Table 6 are obtained from the oceanographic measurements taken nearby the site. The soil characteristics in Table 6 were determined by analyzing the geophysical surveys onshore that involve 100 CPTU tests and 33 geotechnical boreholes given in the site investigation reports at the site [26,28]

Table 6. Probability distributions describe the fluctuations of key design parameters in the simulations.


Consequently, using a variety of model components or a robust model is essential for providing an accurate risk assessment of coastal flow slides. Many elements, such as sediment characteristics, water velocity, and soil stability, come into play during coastal flow slides. Researchers may better replicate the underlying physical processes and increase the models' prediction potential by combining various model components or a robust model.

One practical way for estimating the outcomes of such complicated systems is Monte Carlo Simulation (MCS), a methodology that makes use of random sampling techniques. In the study, the MCS technique is being applied to estimate the susceptibility of seawalls and breakwaters to wave loads on coastal flow slides. Researchers may obtain a more trustworthy and precise assessment of probable outcomes by integrating the robust model with the MCS technique, enabling better decision-making and planning for coastal flow slides in the face of changing climatic circumstances.

To achieve a comprehensive understanding of the risks and vulnerabilities associated with coastal flow slides, it is necessary to employ several model components or a robust model in conjunction with the MCS approach. This approach allows for the consideration of a wide range of potential scenarios and uncertainties, including varying rainfall intensity, wave heights, and coastal slope conditions. By utilizing multiple model components or a robust model, it is possible to incorporate more accurate and detailed information into the analysis and provide a more reliable estimate of the potential hazards and risks associated with coastal flow slides.

Because of its inherent unpredictability, the MCS may generate a wide range of outcomes, each of which has its likelihood of occurrence, as described by the probability distributions used to represent the random variables involved. Our sensitivity analysis using the MCS technique revealed that sediment and fluid properties, as well as the interaction between waves and currents from the model, have a significant impact on the stability of coastal slopes. Specifically, we found that the Shields parameter, which is a key parameter for evaluating coastal stability, is adversely affected by sediment density and diameter. Our analysis also showed a high likelihood of breaches occurring under certain conditions.

The effects of fluid density, depth, and slope on shear stress sensitivity analysis are roughly equivalent. Furthermore, the active wall height (=breach height), water density, and permeability all have negative effects on the critical slope angle, as does the average particle size.

By combining the MCS method with other model components as a robust model, we may better assess the risks and weaknesses in coastal infrastructure. The safety and

resilience of coastal communities may be ensured by using this information to better understand the potential implications of coastal hazards and to influence choices concerning the design, construction, and maintenance of the infrastructure.

In terms of coastal flow slides, the active wall height, refer to the height of the slope where the slope angle is steeper than the angle of repose, indicating a greater likelihood of flow slides occurring, is crucial because it controls the amount of pressure and force applied to the soil and rock slopes behind the wall. The greater the pressure and force, which might cause instability and collapse of the slope, the higher the active wall height.

Random variables, such as the active wall height, may be modeled using probability distributions. Researchers can simulate a variety of situations and evaluate the degree of risk and uncertainty in each by using probability distributions of MCS. The stability of the slopes behind an active wall has a direct impact on coastal flow slides, and probability distributions help model the intrinsic variability of random variables and estimate the risk and uncertainty associated with them.

Figure 17 is a graphical representation of a sensitivity analysis conducted on the various parameters that influence the formation of coastal flow slides, using data from Table 6. The parameters depicted in Figure 17 include sediment density, in situ porosity, in situ permeability, median particle size, active wall height, water density, and slope. These parameters are all known to play a role in the development of coastal flow slides and understanding their impact is critical in predicting the occurrence of these events and implementing measures to mitigate their effects.
![img-15.jpeg](img-15.jpeg)

Figure 17. Sensitivity analysis by MCS contribution to variance technique.
Through an analysis of Figure 17, we can gain insight into how changes in each of these parameters can affect the formation of coastal flow slides. For example, a decrease in median particle size would result in a more stable slope, which would be less likely to experience a flow slide. On the other hand, the active wall velocity can vary with respect to permeability. This means that if the permeability of the active wall is increased, the velocity of the wall can be adjusted to minimize the risk of a flow slide.

Understanding the relationship between each of these parameters and the formation of coastal flow slides is crucial in predicting the occurrence of these events and minimizing their impact. By utilizing the sensitivity analysis provided in Figure 17, we can identify the most influential parameters and generate more precise predictions about the occurrence and behavior of coastal flow slides under different conditions. This information can be used to develop strategies to minimize the occurrence of coastal flow slides in vulnerable

areas. Ultimately, the information provided by Figure 17 is a valuable tool for engineers, scientists, and policymakers who are seeking to mitigate the impact of these potentially devastating events.

In data analysis, correlations are used to understand the relationship between variables. While strong correlations are preferred as they provide more conclusive evidence of a relationship between variables, weak correlations should not be ignored. Weak correlations, even though not statistically significant, can still provide important insights into potential relationships between variables. When dealing with large datasets, even a weak correlation can have a significant impact on the data, potentially revealing new patterns and trends.

One example of a weak correlation in coastal flow slides that plays a significant role could be the correlation between permeability and the likelihood of a flow slide occurring. While the correlation between these two variables may be weak, it still suggests that permeability may play a role in determining the likelihood of a flow slide. Further investigation and analysis may reveal that other factors, such as particle density and water density, also play a role in the occurrence of flow slides. While the correlations between these variables may also be weak, the combined effect of these factors may be significant and cannot be overlooked. Therefore, it is important to consider all factors, even those with weak correlations, when studying the mechanisms of coastal flow slides.

When it comes to safety analyses, random variables should be interrelated with a 3-D hydrodynamic and sediment transport model to correctly encounter the variations at the limit state. It showed the importance of the Hybrid Hydrodynamic and Sediment Transport Coupled Monte Carlo Simulation Model developed in this paper. To determine the critical angle slope by using the hybrid model, 10,000 random values are generated for each variable in the MCS. Variations of modeled parameters obtained from the Hybrid Model are given in Figure 18 where charts display both the occurrence probability and frequency of design parameters.
![img-16.jpeg](img-16.jpeg)

Figure 18. Variations of modeled parameters obtained from the Hybrid Model.
The following units were used for the random variables in Figures 17-21:

![img-17.jpeg](img-17.jpeg)

Figure 19. Correlations between the critical slope angle and soil/fluid parameters obtained from the Hybrid Model.

![img-18.jpeg](img-18.jpeg)

Figure 20. Correlations of wall velocity and soil/fluid parameters given by the Hybrid Model.

![img-19.jpeg](img-19.jpeg)

Figure 21. Correlations of the Shields and soil/fluid parameters obtained from the Hybrid Model.
Mean particle size: typically measured in millimeters (mm) or micrometers ( $\mu \mathrm{m}$ ).
Active wall height: measured in meters (m) or feet (ft) depending on the system of units being used. In situ porosity: expressed as a percentage (\%), or as a decimal between 0 and 1. Permeability: M, asured in units of length per time, such as meters per second ( $\mathrm{m} / \mathrm{s}$ ) or feet per day ( $\mathrm{ft} /$ day).

Water density: measured in units of mass per volume, such as kilograms per cubic meter $\left(\mathrm{kg} / \mathrm{m}^{3}\right)$ or pounds per gallon $(\mathrm{lb} / \mathrm{gal})$.

Particle density: measured in units of mass per volume, such as kilograms per cubic meter $\left(\mathrm{kg} / \mathrm{m}^{3}\right)$ or pounds per cubic foot $\left(\mathrm{lb} / \mathrm{ft}^{3}\right)$.

Internal friction angle: measured in degrees $\left({ }^{\circ}\right)$.
Pick-up flux: measured in units of mass per area per time, such as kilograms per square meter per second $\left(\mathrm{kg} / \mathrm{m}^{2} / \mathrm{s}\right)$ or pounds per square foot per minute $\left(\mathrm{lb} / \mathrm{ft}^{2} / \mathrm{min}\right)$.

To better simulate the failure events, it is crucial to understand the relationships between the critical slope angle and soil/fluid characteristics. By elucidating these connections, scientists will be able to foretell the frequency and magnitude of coastal flow slides more accurately under a variety of conditions. For instance, a lower critical slope angle indicates a larger failure risk if the soil has a low shear strength. On the other side, a higher critical slope angle indicates a decreased failure risk when the soil density is high.

Understanding these associations requires knowledge of probability distributions as well. The random variables' intrinsic fluctuations are captured through probability distributions in the Hybrid Model. Probability distributions allow the model to deliver more accurate and realistic findings by considering uncertainty in the soil/fluid parameters. Soil composition, moisture levels, and loading conditions are only a few of the variables that might affect the soil's shear strength. The model can simulate a wider variety of possibilities and provide more accurate predictions of failure events by treating the shear strength as a random variable with a probability distribution.

Shear stress, sediment particle velocity, and the critical slope angle were all found to correspond to a normal distribution, but the Shields parameter, owing to the asymmetry

in the particle size distribution, followed a log-normal distribution. To further examine the effect of the random design factors on the population, scatter diagrams were created. The degree of relationship between design variables may be determined with the use of these diagrams, which depict the dependencies and interactions between forecast and design factors. Parameters of soil and fluids, such as permeability, porosity, particle density, friction angle, and water density, are shown to have relationships with active wall velocity as illustrated in Figure 19.

When discussing coastal flow slides, the active wall height is crucial since it establishes the slope's stability. The scatter plot demonstrates a positive relationship between active wall velocity, particle velocity, and permeability, such that an increase in any one of these parameters results in a corresponding increase in active wall velocity. On the other hand, in situ porosity, internal friction angle, water density, and erosion pick-up flux are all negatively correlated with active wall velocity. It follows that raising these variables reduces the active wall velocity and, by extension, the stability of the system. Hence, the hybrid model verified the velocity-permeability relations with hydraulic gradient as discussed [29].

The Shields parameter, which plays a crucial role in sediment transport, has been found to exhibit complex relationships with several geomorphological and hydrodynamic factors as shown in Figure 20. In particular, the Shields parameter has a positive correlation with the density of the fluid, the gravitational acceleration, the slope, and the depth of the water as given in Figure 21. However, this relationship is found to be negatively correlated with the density of the sediment and the diameter of the sediment particles, suggesting that increased sediment density and diameter are associated with a reduction in the Shields parameter. The study has also revealed a positive correlation between fluid density and temperature.

In this study, since the material was fine, fine sand and clay, the critical angle slope was calculated in conjunction with the particle size. The critical angle of coastal flow slide is the steepest angle of decline or dipping concerning the horizontal plane whereby a granular material may be deposited without falling over. It is an important factor in determining the stability of slopes and can vary depending on the particle size and other factors. Sensitivity analysis is a crucial step toward obtaining trustworthy results in the field of RBF studies. Given the vast number of model input parameters and the inherent uncertainty of their underlying values, sensitivity analysis allows researchers to run numerous simulations at a relatively low cost. In this study, the sensitivity analysis was performed using the MCS together with the Hydrodynamic Transport and Turbulence module, yielding computationally efficient results.

# 6.7. Application of the BN Module 

The hybrid model and the sensitivity index developed were validated by the Bayesian Network (BN) by which the relations of CFS depth, sediment density, fluid density, and porosity on vital parameters such as Shields parameters, shear stress, critical angle slope, and active wall velocity were confirmed by the MCS module. The simulation of coastal flow slides by the BN module is illustrated in Figure 22. The validation of DSI was assessed by using the literature and applying the hybrid model according to the flowchart given in Figure 23.

![img-20.jpeg](img-20.jpeg)

Figure 22. Simulation of retrogressive breach failure by BN (critical angles vary $(\mathbf{a})=20,(\mathbf{b})=15$, $(\mathbf{c})=13,(\mathbf{d})=10,(\mathbf{e})=9$, and $(\mathbf{f})=8$, respectively. The blue lines show the critical angle slope).
![img-21.jpeg](img-21.jpeg)

Figure 23. Flowchart for the validation of the hybrid model.
The model incorporates various factors including breaching failure (CRBF), liquefaction (LFS), and ranking DSI parameters to estimate the probability of CRBF and LFS occurring in coastal areas. The validation process involves using literature and other sources to confirm that the model's predictions are accurate and reliable. The flowchart provides a step-by-step guide for ensuring that the hybrid model is valid and can be used to effectively predict the likelihood of breaching failure and liquefaction in coastal areas.

The DSI investigated the sensitivity of specific parameters (P1 through P7) in relation to their influence on the breach and liquefaction of a given structure. Table 7 contains

four different cases, each represented by a different model (CRBF or LFS), and displays the DSI values for each parameter, indicating their relative importance in determining the likelihood of breach or liquefaction. The major equation for each model is also included, representing the relationship between the parameters and the probability of breach or liquefaction. The results of the BN model are shown in Figure 22 and are tabulated in Table 7. The hybrid model results presented in Table 7, show the predicted probability of breach or liquefaction based on the analyzed parameters by BN.

Table 7. Model results compared with the literature (DSIP: DSI Parameters).


The combined procedure that was followed in this paper is named as the Hybrid Model, and it was used consistently throughout the process. This was conducted by constructing the BN in the simplest and most effort-effective manner for feasible computations.

As can be seen from the BN in Figure 22, the stability of CFS is strongly contingent on dredging rate, beach slope, packing type (densely packed sand, loosely packed sand), mass flow, and turbidity current. If the turbidity current on the set of CFS is substantial enough, then it is referred to as Retrogressive Breach Failure. On the other hand, the LF will take place by the situation unless the turbidity current is commanding.

If the slope condition has a predilection towards CRBF, then the angle has to be somewhat steep, as was indicated in Table 7. Figure 24 illustrates that the angle of the beach is generally a mild slope because of this reason. This indicates that the slope is not steep enough to generate CRBF; nevertheless, the liquefaction flow sliding rate as a percentage is rather high at 41.5 .
![img-22.jpeg](img-22.jpeg)

Figure 24. Established BN in the Hybrid Model.
For this case study of Osman Gazi Bridge abutments, the sensitivity indexes of all variables are $\mathrm{P} 1=1, \mathrm{P} 2=3, \mathrm{P} 3=4$, and $\mathrm{P} 6=5$, respectively. Therefore, the liquefaction coefficient is found as 3.87 (Level IV) which is considered under high risk of liquefaction flow slide according to the level of sensitivity analysis given in Table 7.

Additionally, a BN was used to explore the effects of DSI parameters on the coefficient of breaching and liquefaction, which are measures of the likelihood and magnitude of coastal breaching and liquefaction as illustrated in Figures 25 and 26.
![img-23.jpeg](img-23.jpeg)

Figure 25. Effects of parameters (dredging rate, beach slope, loosely sand packed, mass flow) on coefficient breaching.

![img-24.jpeg](img-24.jpeg)

Figure 26. Effects of parameters (dredging rate, beach slope, loosely sand packed, mass flow) on liquefaction coefficient and their percentage.

Figure 25 is intended to provide a qualitative representation of the range of breaching coefficients, showing them as low, moderate, and high. Figure 26, on the other hand, presents data quantitatively in terms of the liquefaction coefficient, showing the percentage of values falling into each category. For example, if the percentage of low values is greater than the percentage of moderate and high values, then the overall coefficient value is considered low (Figure 26).

As a result, the case study area was estimated as an unsafe zone by running the Hybrid Model developed in this paper, and since the Hersek abutment of the Osman Gazi Bridge was going to be constructed here, the soil was fortified by sheet piles of 16.00 . In addition, a dry dock with an area of $22,820 \mathrm{~m}^{2}$ and depth of -7.50 m was built and $70 \%$ of the construction works of the bridge caissons were carried out in this dry dock.

# 7. Discussion of Results 

When compared to past years, the beaches of the globe have undergone an extraordinary transformation because of climate change and human interference, and this change puts them in jeopardy. Considering coastal flow slides have the potential to devastate the surrounding region, a designer must analyze these areas to prevent construction in inappropriate spots and incurring additional costs. Therefore, a feasibility study is required in marine spatial planning (MSP) for beach conservation, where both the aesthetics and safety of the beaches will be maintained. It is anticipated that beaches will become focal points of interest, which in turn will lead to an expansion of the tourism industry. Coastal flow slides (CFS), which encompass both retrogressive breach failures (RBF) and liquefaction flow slides (LFS), are a type of slope instability that poses a significant risk to the management practices of MSP. Despite the frequency of these failures, there exists a limited understanding of their underlying mechanisms and causes. This lack of understanding often leads to misdiagnosis, with CFS being misinterpreted as shear failures, liquefaction failures, or even simple erosion processes.

The complex nature of CFS stems from its dependence on two primary factors: the characteristics of geomechanically saturated sand and the behavior of accompanying turbulent density currents. These currents can rapidly transport large volumes of suspended sand downslope, contributing to the retrogression of the breach, as modeled by the sediment transport module. Given the potentially destructive impact of flow slides, marine spatial planners and coastal engineers must possess a thorough understanding of the mechanisms driving RBF, the environmental conditions in which they may occur, the hazards posed

by these failures, and the countermeasures that have been implemented successfully in different environmental conditions. This article aims to understand RBF through a case study of a bridge in the Marmara Sea. The study focuses on the evaluation of the critical slope angle, a crucial factor in several environmental challenges such as beach stability, erosion, and wave energy converters.

Through sensitivity analysis, we treat various factors as random variables with probability distributions to evaluate the critical slope angle. The results of the case study support the proposed new model for assessing the threat of slope instability.

# 8. Conclusions 

Complex in nature, coastal flow slides (CFS) may have serious consequences for shoreline integrity, hydraulic fill structures, and dredging efforts. Due to the complexity of the processes involved and the breadth of characteristics that must be taken into account, a study in this field has been restricted. Yet, the inherent uncertainties in the CFS process may have been missed in previous research since they relied on deterministic approaches. To solve this problem, a new robust model was created that uses Monte Carlo Simulation (MCS), Bayesian Networks, and the hydrodynamic sediment transport model HYDROTAM3D. This model offers a considerable advance over earlier research since it incorporates a mix of various model components and leverages the MCS approach to predict the outcomes of a complex system.

By treating input parameters as random variables, the MCS approach generates many sets of input parameters that characterize various possible outcomes for the system's behavior, making it especially applicable in this setting. This compensates for the volatility of input factors, such as water density, wave height, and ambient conditions, which may fluctuate to some amount. These random variables are characterized by probability distributions, and the MCS generates a set of outcomes, each of which has its likelihood of occurrence.

The new model's accuracy is further improved by using the hydrodynamic sediment transport model HYDROTAM-3D. Sediment transport and wave-current interactions are accounted for in this model. Bayesian Networks (BN) are then used to merge the output of the MCS and HYDROTAM-3D models. BN is a probabilistic graphical model that concludes the underlying system using probabilistic linkages. Overall, this new robust model allows a more full and accurate analysis of the probable hazards and vulnerabilities of coastal infrastructure, such as seawalls, breakwaters, and coastal flow slides. This approach may help maintain coastal communities safe and resilient by guiding choices regarding the design, construction, and maintenance of coastal infrastructure considering the possible implications of coastal hazards.

The DSI ranking of parameters affecting coastal liquefaction for Osman Gazi bridge are dredging rate, coastal structures, packing type, and driving force as tabulated in Table 8. In Table 8, the Sensitivity Index Ranking column explains the ranking of each parameter's sensitivity index. The rankings are as follows:

- very low: the parameter has little to no effect on the DSI;
- low: the parameter has a small effect on the DSI;
- moderate: the parameter has a moderate effect on the DSI;
- high: the parameter has a significant effect on the DSI;
- very high: The parameter has a very significant effect on the DSI.

Overall, the cumulative effect of these parameters created to contribute to LFS.
As a result, there are so many variables at play, predicting coastal flow slides (CFS) has always been challenging. Yet, by creating a new probabilistic simulation model of CFS that accounts for all the complicated mechanisms involved, our work has achieved a tremendous leap in our knowledge of CFS. Our capacity to foretell sediment erosion rates in coastal regions has been substantially improved by using this model to cooperate with the HYDROTAM-3D sediment transport model.

Table 8. DSI ranking of parameters affecting coastal liquefaction for Osman Gazi Bridge: dredging rate, coastal structures, packing type, and driving force.


To calculate how susceptible seawalls, breakwaters, and hydraulic fill structures are to CFS, the new model combines a Monte Carlo Simulation (MCS) with Bayesian Networks (BN). Based on the probability distributions for the random variables, the MCS method creates many sets of input parameters, each of which reflects a unique scenario of the system's behavior. This method considers the probabilities of a variety of outcomes in light of the process' inherent uncertainty.

Sediment movement and erosion are fundamental aspects of CFS, and they may be simulated with the help of the HYDROTAM-3D sediment transport model. We improved our ability to estimate sediment erosion rates using the HYDROTAM-3D model in conjunction with the new probabilistic simulation model, which is crucial for comprehending and minimizing the effects of CFS on coastal infrastructure.

Designers have learned a lot more about CFS and its potential effects on coastal areas as a result of this research. The new probabilistic simulation model has the potential to considerably enhance our capacity to forecast and mitigate the consequences of CFS on coastal infrastructure by considering the uncertainties inherent in the process. The critical zone for RBF in coastal flow slides is assessed using a combination of hydrodynamics, sediment transport models, probabilistic risk analysis, and stochastic simulation. To further investigate what factors, influence the slope of the critical angle, a sensitivity analysis of the RBF and its input parameters has been conducted.

The model's usage of a Bayesian network also allows for the incorporation of probabilistic inputs and uncertain parameters, resulting in a more accurate portrayal of the system's behavior. By taking this viewpoint, we may learn more about the impact of CFS and better understand the key aspect of RBF. The stability of coastal slopes is affected by sediment/fluid characteristics and wave/current interaction, as shown by the Monte Carlo sensitivity analysis. Limit-state transitions may be reliably determined by correlating such research with a three-dimensional hydrodynamic sediment transport model.

The study's use of simulation models has improved the understanding of the challenges involved with coastal slope collapse and gives important insights by creating a hybrid model. Since it incorporates many modeling techniques, the hybrid model provides more room for certain chapters to make meaningful contributions to the overall discussion. The method and results presented in the study can be extended to other environments and coastal evolutions.

Author Contributions: Conceptualization, Methodology, Software, Validation, Formal analysis, Investigation, Resources, Data Curation, Writing-Original Draft, Writing-Review \& Editing, Visualization: A.D.; Writing-Review \& Editing, Supervision, Visualization: C.E.B.; Supervision, Ş.Ç.; Visualization, E.A.B. All authors have read and agreed to the published version of the manuscript.
Funding: This research was funded by THE SCIENTIFIC AND TECHNOLOGICAL RESEARCH COUNCIL OF TÜRKİYE, grant number: 1059B142200092.

Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Data will be made available on request.

Acknowledgments: The authors would like to express their sincere gratitude to Peter Nielsen, the supervisor of the first author, for his invaluable guidance and support throughout the research process. Peter Nielsen's expertise and insights were instrumental in shaping the direction of the study and in ensuring the research adhered to the highest academic standards. The authors would also like to thank the four anonymous reviewers for their constructive feedback, which significantly improved the quality and impact of the paper. The authors are grateful for the time and effort the reviewers put into providing thorough and thoughtful comments, which helped to strengthen the arguments and findings of the research. Finally, the first author wishes to acknowledge THE SCIENTIFIC AND TECHNOLOGICAL RESEARCH COUNCIL OF TÜRKİYE for their support through the International Research Fellowship Program for PhD Students. This funding has enabled the first author to pursue his research interests and make significant contributions to the field of study. The author recognizes the importance of such funding programs in promoting scientific research and academic excellence and is grateful for the opportunities provided by the fellowship program.

Conflicts of Interest: The authors declare no conflict of interest.
