# Enhancing occupants' comfort through BIM-based probabilistic approach 

H.R. Alavi ${ }^{1}$, Nuria Forcada ${ }^{1}$, Rafaela Bortolini ${ }^{1,2}$, David J. Edwards ${ }^{3}$<br>${ }^{1}$ Department of Project and Construction Engineering (DPCE), Group of Construction Research and Innovation (GRIC), Universitat Politècnica de Catalunya (UPC), Colom, 11, Ed. TR5, 08222, Terrassa, Barcelona, Spain<br>${ }^{2}$ School of Architecture and Urbanism, Universidade Federal de Pelotas, Benjamin Constant Street, 1359, 96010-020, Pelotas, Brazil (Present address) (Corresponding author: bortolinirafaela@gmail.com)<br>${ }^{3}$ School of Engineering and the Built Environment, Birmingham City University, Birmingham, United Kingdom


#### Abstract

Despite the fact that buildings are designed to meet occupants' needs, many do not perform as planned, impacting upon both building performance and occupants' comfort. Analyzing occupants' comfort based on questionnaire surveys requires specific information and appropriate use of visualization techniques to identify possible dissatisfactory problems. However, existing studies do not provide a user-friendly visualization and are not interoperable with Building Information Modeling (BIM) to facilitate the data collection. This paper proposes a novel approach for integrating occupants' feedback and an occupants' comfort probabilistic model into BIM. It also presents innovative techniques to facilitate BIM as a more effective platform for visualization to guide decision-makers in addressing building operational problems centered on occupants' comfort. Findings from this research can assist facility managers and owners in identifying causal factors of occupants' discomfort and properly establishing the necessary measurements to moderate the negative consequences on occupants and thereby improve their comfort.


Keywords: Building Information Modeling; Visualization; Data integration; Occupants' comfort; Bayesian networks; Facility Management

## 1. Introduction

The Architecture, Engineering, Construction, and Operation (AECO) sector is responsible for the creation and management of the built environment for the purpose of facilitating human activities over time (i.e. work, leisure and accommodation). Creating this man-made environment directly impacts upon occupants [1], who require buildings that meet their needs and satisfy their expectations in terms of accessibility, productivity, health and comfort [2]. The role of occupants' comfort within buildings, in terms of environmental, social, and

economic aspects, is essential [3] since people spend approximately $90 \%$ of their time indoors [4-6]. Nevertheless, some buildings exhibit poor performance in meeting occupants' comfort [7].

Indoor air quality is one of the primary disturbances among the occupants. Additionally, daylight penetration in buildings and harmful noise level straightforwardly affect the occupants' psychology. Thus, disturbing physical aspects slow down occupants' job levels and raise the number of mistakes due to interruption [8,9]. The physical condition of the workplace influences 15-20\% of the occupants' productivity. Productivity thus constitutes the economic dimension of comfort conditions by ultimately impacting the business financially $[10,11]$. Standards based on indoor environmental quality (IEQ) factors are used to define the acceptable ranges of comfort [12]. However, due to the variations in individual sensation levels, there is a poor relationship between the comfort conditions defined in the standards and those perceived by the occupants [13]. Therefore, it is essential to collect occupants' feedback and evaluate building performance to increase occupants' comfort and productivity [14].

A post-occupancy evaluation (POE) is a common technique used to evaluate the building systematically after it has been occupied and to assess occupants' comfort [1] through a questionnaire survey on various comfort aspects. These include physical aspects, such as visual comfort, acoustic comfort, thermal comfort, and indoor air quality, and non-physical aspects, such as the workplace, space layout, occupancy density, cleanliness, aesthetics, and furniture [15-18]. However, the current POE tools used by researchers are based on deterministic models [19,20] and do not take into account the effects on occupants' comfort of building information (e.g., building characteristics) and spatial information (e.g., occupancy density) [21,22]. There are several factors of high uncertainty that influence occupants' comfort, such as the building characteristic (e.g., the building envelope), HVAC system (e.g., type of heating and ventilation), exterior condition and others [19,23]. The relationships between these factors are complicated, and their uncertainty needs to be taken into account [22,24,25] to evaluate the causal factors of occupants' discomfort, which would assist decision-makers in the facility management (FM) industry [26,27]. Bortolini et al. [28] developed a probabilistic model based on a Bayesian network (BN) that includes multiple interacting factors for supporting occupants' comfort to address this issue. However, different information is required to evaluate occupants' comfort, but this resides typically in different platforms, which are neither analysed nor linked [1,29].

A BN is a type of probabilistic graphical model that provides a formalism for reasoning about partial beliefs under conditions of uncertainty [30]. It is considered a powerful tool by which to model risks with uncertainty data [31-33]. BN can model building comfort as a probabilistic process, to give the most probable performance level of a building using probability distributions [28]. Moreover, Building Information Modeling (BIM) can provide building and spatial information required by the BN model, reducing the time and effort that the FM team spends on manual input. To the best of our knowledge, no previous study has provided integration of BIM with risk assessment models that facilitate the data collection and enable the visualization of the occupants' feedback and the results of causal factors to assist decision-makers. This research aims to integrate occupants' feedback and an occupants' comfort probabilistic model into BIM and provide an effective platform for data visualization. Such incorporation will help the FM team to optimize building operation strategies. The approach can be used to conduct different scenario comparisons and to optimize decisions based on economic and environmental goals. It also provides the FM team with the opportunity to learn from past mistakes or deficiencies and supports decision-making on FM activities (e.g., maintenance) to enhance the comfort and sustainability of buildings.

# 2. Literature review 

Existing studies have utilized probabilistic models for improving occupants' comfort. Yang et al. [34] developed a probabilistic model based on a comprehensive survey of air handling unit (AHU) fault detection and diagnosis (FDD) methods. Zhe et. al. [35] used Bayesian inference approach to derive new occupant comfort temperature ranges for U.S. office buildings using the ASHRAE Global Thermal Comfort Database. Lee et al. [32] developed a Bayesian approach for probabilistic classification and inference of occupant thermal preferences in office buildings to provide predictions for personalized thermal preference profiles. Frederik et al. [36] created a probabilistic model to learn from a user's feedback, allowing it to adapt to the users' individual preferences over time to assess occupants' comfort. However, these studies are lacking some crucial features such as (1) spatial information concerning the occupants' feedback comfort [37], (2) visualized representation of easily understandable data analysis results way [38]. The greatest obstacle is that the data is not processed and analyzed in a way that the decision-makers need and not visualized in an easily accessible, and refined way $[26,38]$.

Other studies have utilized BIM to address these challenges. Efforts to extend BIM beyond the design and construction phases of the buildings are significant. BIM constitutes an effective platform by which to depict high-quality information and integrate different platforms and sources. BIM utilizes 3D, parametric and objectbased models to create, store, and use coordinated and compatible data throughout the life cycle of a facility [39]. Researchers focus on implementing BIM for different aspects of FM, such as: maintenance of warranty and service information [40,41]; quality control [42]; asset management and monitoring [39,41,43]; energy management [44,45]; sustainability [46-48]; space management [39,43,49]; emergency management [43,50]; and retrofit planning [51]. BIM implementation can be further extended to: preventive maintenance planning [52,53]; building systems analysis [53,54]; commissioning processes [53,55]; and strategy planning [53,56]. A few studies have integrated BIM with a probabilistic model [57-60]; however, they do not take into account indoor environment for occupants' comfort. Di Giuda et. al. [61] demonstrates the benefits of using BIM for increasing occupants' comfort, such as (1) obtaining feedback for the design process, (2) reducing energy consumption, and (3) reduction of operational phase's costs. Göçer et. al. [62,63] have integrated BIM with occupants' feedback by extracting spatial information from the BIM model into a graphic information system (GIS) tool and then link occupants' feedback with ArcGIS so as to visualize the results. However, the visualization of occupants' feedback is worthless without an analysis of the discomfort causal factors. Besides these studies, applications of BIM in operation and maintenance phase are still under development, and the research in this area, while growing, is still at a very early stage [64,65].

# 3. Research approach 

There were three main steps to facilitate the analysis of occupants' comfort causal factors, (1) A satisfaction survey was developed and designed in Google forms, based upon comfort aspects (e.g., thermal comfort, acoustic comfort, indoor air quality, visual comfort, and space adequacy). (2) A probabilistic model was utilized to determine occupants' comfort causal factors based on a BN. One of the most common BN modeling tools, AgenaRisk, was used to create the BN model for occupants' comfort. The BN model was obtained from [28]. In order to take advantage of the BN model, building information (e.g., building characteristics or HVAC system) and spatial information (e.g., occupancy density) were collected for each comfort aspect. Some of this information (e.g., building characteristic) could be obtained from a BIM model, but for that information which

was not, parameters were created in the BIM model to host it. (3) The BIM model was integrated with occupants' feedback from the POE survey and the occupants' comfort probabilistic model to support occupants' comfort, utilizing a visual programming extension for Autodesk Revit, Dynamo, and the Python programming language.

Figure 1 illustrates the automation process of integrating occupants' feedback (using parametric tools) and the occupants' comfort probabilistic model (using scripts of Python programming language) into the BIM model, where building and spatial information exists with respect to the BN model for each comfort aspect. The BIM visualization of occupants' feedback and the results of causal analysis provide a way that the FM team can easily understand the data.

# > Insert Figure 1 

### 3.1. Occupants' comfort survey

Occupants' comfort includes both physical and non-physical aspects [28,66]. Physical IEQ aspects include: thermal comfort, visual comfort, acoustic comfort, and indoor air quality [67,68]. Non-physical aspects generally refer to those space qualities that are difficult to measure with instruments, such as: space layout, privacy, furnishing, and cleanliness [66,68]. For this study, both physical and non-physical comfort aspects were incorporated. A questionnaire survey consisting of three sections was developed to collect occupants' feedback (see Appendix 1):

Section 1. Occupants were asked to select their workplace location, as defined by building, floor and room. Section 2. Occupants were asked to rate their satisfaction in relation to various workplace comfort aspects, including thermal comfort in winter and summer, indoor air quality in winter and summer; visual comfort; acoustic comfort; and space adequacy. The survey used a 5-point Likert rating scale to rate occupant feedback, ranging from 'very satisfied' (5) to 'very dissatisfied' (1), with a neutral midpoint (3). The survey also asked the reasons for discomfort given the predefined options, and included a text entry box for respondents to add other reasons.

Section 3. Occupants were also asked to rate their satisfaction in relation to comfort aspects of the common spaces of the building that they used most (e.g., corridors, conference rooms, restrooms, and dining rooms),

including thermal comfort in winter and summer; indoor air quality in winter and summer; visual comfort; acoustic comfort; and space adequacy.

# 3.2. A probabilistic model for occupants' comfort 

To evaluate the causal factors of occupants' discomfort, the building and spatial information affecting occupants' comfort for each comfort aspect should be identified. To do so, firstly the most influential variables in a building's comfort performance were initially identified by literature review, acting as a basis for the selection. Secondly, the results of a satisfaction survey conducted with 1,013 participants was statistically analyzed to identify the cause-effect of some variables. Thirdly, an adaptation of the Delphi method [69] was conducted to check and improve the model structure, which implicate on adding intermediate nodes or establishing missing relationships. Nine experts with more than 10 years of experience in the field of building performance and FM participated in the Delphi method.

Each variable of building and spatial information was represented as a node in the BN model, and depending on the information type, they were defined as discrete (labeled, Boolean, discrete real, or ranked) or continuous [70]. Some nodes were defined as Boolean, with binary states such as 'Yes' and 'No'. Others were defined as ranked and had multiple states such as 'High', 'Medium' and 'Low'. Due to the underlying numerical scale of the ranked nodes, the truncated Normal distribution (TNormal) was used for defining numerical statistical distributions as expressions [70].This distribution is characterized by two parameters: mean and variance. For instance, uncertainty in the exterior condition was handled by a normal distribution [71]. AgenaRisk was selected to build the BN model for occupants' comfort for its power, versatility and userfriendly interface $[28,72]$.

Conditional probability tables (CPTs) specify the degree of belief (expressed as probabilities) that a node will be in a particular state given the states of the parent nodes (the nodes that directly affect that node) [73]. Backward propagation is an essential function of a BN in which an observation is made for a specific node, and then the BN calculates the marginal probabilities of unobserved nodes by propagating the impact of the observed node through the network in a backward fashion [73]. Finally, a BN model allows a sensitivity analysis to be conducted to understand the most significant factors in the model given observed data.

The CPTs for each node, and the importance of the parent nodes for occupants' comfort in different comfort aspects, was defined by Bortolini et al. [28] in the BN model. Table 1 shows the CPTs for occupants' comfort nodes.

# > Insert Table 1 

For acoustic comfort, the insulation characteristics of all walls, windows, and doors of each room are contributing factors in the BN model. Acoustic attenuators used in mechanical ventilation systems can reduce noise from air systems and are considered as a contributing factor to understanding occupants' acoustic discomfort. Buildings with natural ventilation might lead to discomfort due to outside noise; hence the type of ventilation system is identified as a further factor affecting acoustic comfort. Factors such as building and spatial information are considered as nodes in the BN model (e.g., causal factors). The type of ventilation system is defined as a labeled node with the following states: natural, forced, and mixed. Envelope and interior acoustic insulation are defined as ranked nodes. Finally, an acoustic attenuator is defined as a Boolean node (Yes/No). Regarding the importance of the parent nodes, interior acoustic insulation, envelope acoustic insulation, and acoustic attenuator have the same impact on acoustic comfort (See Table 1).

Indoor air quality depends on the type of ventilation system which can influence occupants' comfort perception. Generally, naturally ventilated buildings have higher rates of comfort than air-conditioned buildings [10]. The occupants can open windows and thus vary the indoor environment to some extent. However, natural ventilation is dependent on weather conditions [74], and might not be adequate in environments with extreme temperatures. Obtaining information on outdoor conditions from an exterior meteorological station is, therefore, a relevant factor for determining the air quality comfort.

On the other hand, for buildings with mechanical ventilation, the condition of the HVAC system is an essential factor, as its improper operation may lead to poor ventilation and cause health problems and discomfort [10,28,75]. The HVAC condition, which refers to the condition of the component, is categorized as high, medium, or low. For instance, high condition would describe an item of equipment in excellent condition, capable of being used to its fully specified utilization for its designated purpose. HVAC design errors (wrong design of the system) might have an impact on occupants' discomfort in indoor air quality and thermal comfort [76,77]. For example, a good HVAC system design depends on the architecture of the building. If there are

single thermal zones, then centralized systems are the best option, whereas, for buildings with different thermal zones, decentralized systems are a better option.

Furthermore, occupancy density ( $\mathrm{m}^{2} /$ person) affects air quality comfort, so it is also considered as a contributing factor in indoor air quality. In the BN model, HVAC design errors, HVAC condition and occupancy density are defined as ranked nodes and ventilation control and filter are considered as Boolean nodes. Exterior condition is defined as a labelled node (e.g. extreme cold, cold and mild for winters and extreme hot, hot and mild for summers). HVAC condition and HVAC design errors are the most important factors that affect indoor air quality, while ventilation filter has the least impact on indoor air quality (See Table 1).

With respect to thermal comfort, thermal sensation is the condition of mind that expresses comfort with the thermal environment. The exterior conditions play an essential role in thermal sensation. The type and characteristics of HVAC systems (e.g., cooling and heating type) and thermal adaptive opportunities are also identified as relevant factors in thermal comfort [37,78]. Radiant systems, for example, can provide higher comfort levels for indoor temperature [79]. The age of HVAC components (such as splits, boiler, chiller, etc.) can affect their performance and thus the thermal comfort. Occupants with thermal adaptive opportunities such as operable windows and thermostats present high levels of comfort [80,81]. The characteristics of a building include envelope material and insulation, comprising both façade, roof, and windows [82]. In this sense, an envelope with a low thermal transmittance (U-value) can help extend the periods of thermal comfort without reliance on mechanical air-conditioning [28,83]. The material and insulation properties of partitions also play an important role when the adjacent rooms do not keep thermal comfort characteristics. In the BN model, the heating and cooling types are defined as labeled nodes with the statement of radiant, all-air, others, and not applicable. Both the possibility of controlling temperature and operable windows are considered as Boolean nodes. Although HVAC conditions, temperature control possibility, and envelope performance are classed as essential factors, thermal comfort is mostly affected by HVAC design errors and exterior conditions (see Table 1).

For visual comfort, the impact of daylighting can be considered quantitatively through the window-wallratio (WWR) [84]. There is a strong preference for daylight in workplaces, which is closely associated with the belief that daylight is better for health [85]. Therefore, dimensions of façade and windows should be modeled

in BIM, and the WWR per space calculated. The availability of interior curtains and/or exterior window shading (louvers) is a critical component in controlling glare and overheating, both of which affect occupants' comfort [85]. Design errors might also have an impact on occupants regarding visual comfort; for example, failure to design appropriate daylight controls can affect visual comfort. The light and shade control possibilities are defined as Boolean nodes in the BN model. The WWR is defined as the ratio of the glazed area to the entire area of the envelope and considered as a ranked node (i.e., low ( $<10 \%$ ), medium ( $10-40 \%$ ), and high ( $>40 \%$ )). Regarding the importance of parent nodes for visual comfort, the 'design error' factor is more effective than light and shade control factors (see Table 1).

Considering space adequacy, occupants' comfort is influenced by space characteristics, including flexibility, cleanliness, and accessibility [68,86]. Ergonomic furniture and enclosed spaces for meetings and collaborative work are other factors that affect occupants' comfort [87]. In the BN model, all information regarding space adequacy is defined as ranked nodes. Ergonomic furniture, cleanliness, and accessibility are the most critical factors affecting space adequacy (see Table 1).

# 4. Integration of occupants' feedback and occupants' comfort probabilistic model into BIM 

Even though BIM provides building and spatial information, it still cannot represent complete information on occupants' comfort in which the FM team can make decisions. Therefore, shared parameter was utilized to allow BIM models to contain such information. Shared parameter is a Revit term that can be added to the Revit family for custom data fields. It can also be accessible for any project due to holding parameters in a separate file.

In this study, spatial information was defined and assigned into rooms in BIM, while building information was assigned into their corresponding family (e.g., mechanical family). Since occupants' feedback was reported by the spaces, the rooms were suitable hosts for the satisfaction survey. Hence, all comfort aspects of the satisfaction survey (e.g., indoor air quality and visual comfort) were created, defined, and linked to the rooms in BIM to host occupants' feedback. The same approach was used to create parameters for hosting building and spatial information with respect to the BN model for each comfort aspect that was not available in BIM (e.g., occupancy density). Building information for each component in a building is different; thus, it was crucial to

assign the shared parameters into their relevant families in BIM. For instance, considering 'Ventilation control' as a shared parameter, it should be assigned to a mechanical family but not a wall family.

After creating parameters, occupants' feedback, and the occupants' comfort probabilistic model were integrated into BIM. First, the occupants' feedback from the satisfaction survey was mapped into the corresponding parameters in BIM concerning each room. Second, bidirectional data transfer was implemented from BIM to a BN tool (AgenaRisk) and vice versa to integrate the occupants' comfort probabilistic model into BIM. Finally, the occupants' feedback from the satisfaction survey and the occupants' comfort probabilistic model was visualized in BIM using different color codes for the spatial distribution and Archi-lab_Mandrill package in Dynamo, respectively.

# 4.1. Occupants' feedback mapping into BIM 

The process of mapping occupants' feedback into BIM consisted of three steps. First, the occupants' feedback was exported into Microsoft Excel as an intermediate format, prior to its mapping within BIM. Then, the occupants' feedback for each comfort aspect was imported and sorted to match relevant rooms in BIM by using Dynamo and scripts of Python respectively. Finally, all occupants' feedback was mapped into the appropriate spaces using dynamo scripts as shown in Figure 2.

## > Insert Figure 2

Occupants' feedback was imported in Dynamo from the .xls file and classified to different comfort aspects using ReadFromFile and GetItemAtIndex nodes respectively. At the same time, the list of all rooms was extracted from the Revit file and sorted to match the room numbers in the occupants' feedback using code blocks developed in Python, a similar approach to Bortoluzzi [88]. A python code block queries the occupants' feedback (the spreadsheet file) to find room numbers that match those from the Revit file. Eventually, the final list was mapped to BIM using the SetParameterByName node to match occupants' feedback to the proper parameter names with corresponding rooms.

### 4.2. Bidirectional data transfer between BIM and a probabilistic tool

To integrate BIM and the occupants' comfort probabilistic model, the building and spatial information concerning each comfort aspect together with occupants' feedback was extracted from the BIM model using

Dynamo, by creating a dataset in a comma-separated value (CSV) format. Figure 3 shows the extraction of the building and spatial information from BIM regarding different comfort aspects.

# > Insert Figure 3 

Next, the dataset containing building and spatial information as well as occupants' feedback, was imported into the BN tool AgenaRisk, which utilized the information as 'evidences' to run the occupants' comfort probabilistic model as backward propagation to find out the probable causes of comfort or discomfort. The results of causal analysis were then extracted from the AgenaRisk tool into a CSV format and imported into BIM using Dynamo to be matched with corresponding rooms.

Further, Python code block was used to assign the results of causal analysis to the corresponding rooms, considering the building and spatial information in that room. For a given room, the relevant results of the causal analysis were identified. This data supported the integration of customized sliders in the visualizations to permit the appraisal of each room. The Dynamo script and Python code blocks supported this functionality and are presented in Figure 4 (for indoor air quality).

## > Insert Figure 4

The results of causal analysis were connected to the Python code block as an input (input\#0), whilst the building and spatial information for each room were also connected as inputs (from input\#1 to input\#6 regarding indoor air quality). Then, a Python code block queried from input\#1 to input\#6 to find building and spatial characteristics in rooms that matched those from the results of causal analysis (input\#0) and filtered these to create a final multi-dimensional list with the required room numbers and their corresponding parameter data.

### 4.3. Data visualization

Two kind of visualization were considered for displaying occupants' feedback and the results of causal factors. The former visualizes the results of the satisfaction survey and the latter visualizes the information coming from the probabilistic model to determine the causal factors of dissatisfaction. (1) The first proposed visualization mapped occupants' feedback with different colors to vary from 'Very satisfied' to 'Very dissatisfied', taking into account comfort aspects. The tabulated data taken from Revit's schedule was visualized in a 3D format in the BIM model. The visualization of the occupants' feedback by rooms for each comfort aspect was implemented by applying view filters. The FM team would be able to filter comfort aspects in order

to view the average level of occupants' comfort by room, and it is also possible to compare occupants' comfort between different rooms. (2) The second proposed visualization was to visualize the relevant results of the causal analysis coming from the probabilistic model, as related to each room (using Python scripts), which was then connected to the NormalizedStackedBarChart.Data node as values in Dynamo in order to visualize the normalized stacked bar chart for each room using the Archi-lab_Mandrill package. For a given selected room, the results of causal analysis (i.e., the importance of causal factors) were then displayed in BIM.

To give an example and illustrate it, the main factors affecting acoustic comfort were analyzed (see Figure 5).

# > Insert Figure 5 

The importance of the causal factors on the acoustic quality can be visualized in Figure 6. The sensitivity analysis shows the importance of the causal factors when acoustic quality is very high. It can be visualized that the probability of a building having a high acoustic comfort level is more sensitive to changes in the states of envelope and interior acoustic insulation, and least sensitive to changes in the type of ventilation.

## > Insert Figure 6

For this example, as-built information was not updated, so not all information was available. The information about the acoustic insulation was unknown, so no evidence would be established for that node in the probabilistic model. In this example, to evaluate acoustic comfort for each room, the nodes (i.e., building and spatial information) that were known in that room (such as type of ventilation, acoustic attenuator, and occupants' acoustic comfort) were obtained from BIM. For those nodes that were unknown (e.g., envelope and interior acoustic insulation), the backward propagation analysis in the BN model was used to obtain the results of causal analysis and link to the corresponding rooms in BIM using Python scripts. When including the results of the satisfaction survey as an evidence for a specific room, the probabilistic model calculates the most probable state of the unknown variables. Then, BIM visualized the average comfort of occupants regarding acoustic comfort in a color scale and the results of causal analysis in normalized stacked bar charts to facilitate future analysis. Figure 7 illustrates an example of occupants' feedback regarding acoustic comfort and the results of causal analysis visualized in BIM.
$>$ Insert Figure 7

In this example, although the classroom has natural ventilation, which might lead to discomfort due to outside noises, occupants were very satisfied regarding acoustic comfort. On the other hand, occupants were not satisfied with the acoustic in the office. The stacked bar charts for the office shows that the cause of acoustic discomfort, apart from the ventilation system and not having attenuators, is the acoustic insulation of interior partitions, having a probability of $49 \%$ of being low.

From the visualization on BIM, the facility manager can provide hypothetic scenarios by modifying the state of the causal factors and check the probable occupants' satisfaction under these conditions. Therefore, results of the causal analysis suggest that although having the same acoustic insulation of interior partitions, insulating the interior partitions of the office can improve occupants' acoustic comfort in that room. However, installing acoustic attenuators in ventilation systems is the most comfortable solution for the office.

# 5. Case study 

To evaluate the applicability of integrating occupants' feedback and occupants' comfort probabilistic model into BIM, Building TR5 from Universitat Politècnica de Catalunya (UPC), Terrassa campus was used as a case study.

The campus is located in a small urban area in the city of Terrassa (Barcelona) with a Mediterranean climate characterized by hot, dry summers and cold, wet winters. It includes 25 buildings involving classrooms, offices, laboratories, dining rooms, restrooms, common areas, and study areas. TR5 was constructed in 1960; it has $11,492 \mathrm{~m}^{2}$ and five floors with a concrete structure, a brick façade, and an inverted roof. The majority of the windows are single glazed, and the interior partitions are plain brick walls. When TR5 was built, only a radiant system was installed, with two boilers and four air handling units (AHU) (one for each floor) located in the underground. A duct network brought the heated air from the underground to the habitable areas. There was no cooling system at all, and the ventilation was only natural, by opening windows. In the 1990s, splits providing both cooling and heating were installed in some offices. Later, the boilers were substituted by condensing boilers with high efficiency. Finally, by 2010 most of the third floor, which includes both offices and classrooms, was reconditioned, and an air-water system was installed to provide both heating, ventilation, and air conditioning. A chiller was installed in the roof while the existing boilers were also connected to the new

HVAC system for the third floor. Then, several fan coils were installed in each room (offices, classrooms, and corridors) of this floor.

The satisfaction survey was conducted in different TR5 building spaces including classrooms, offices, corridors, restrooms, laboratories, conference rooms, study rooms and dining rooms. This information was integrated into the BIM model and imported to the probabilistic model together with the building and spatial information of each room (e.g., occupancy density ( $\mathrm{m}^{2} /$ person), operable windows (yes/no) and ventilation type, among others).

# > Insert Figure 8 

The indoor air quality comfort in one part of the third floor of TR5 is presented as a scenario. Figure 8 shows the occupants' comfort level for indoor air quality in summer. The options of ventilation control, ventilation filter, occupancy density, and exterior conditions were obtained from the BIM model defined as 'evidences' to run the occupants' comfort probabilistic model in the BN model and find out the probable causes of comfort or discomfort. The quality comfort level in each room was also obtained from the satisfaction survey integrated into BIM and defined as "evidence" in the BN model. The BN model for indoor air quality in summer is shown in Figure 9.

## > Insert Figure 9

The building and spatial information for indoor air quality obtained from the BIM model for the third floor of building TR5 is shown in Table 2.

## > Insert Table 2

BIM visualization allows the FM team and owners to obtain the probabilities of causal factors for indoor air quality comfort or discomfort in each room. The probabilities of having design errors in the HVAC or have a high condition for the HVAC system for each room is presented in the BIM model (see Figure 10). The results demonstrate that room 301 has a $56 \%$ probability of the HVAC being in a high condition (i.e., HVAC system operation without problems), which provides proof for the high comfort level for occupants in this room regarding indoor air quality. On the other hand, occupants in rooms 302, 303, and 306 were not satisfied with indoor air quality. The model results indicate that HVAC design errors is the most probable cause for rooms 303 and 306 since they have an $81 \%$ probability of having high design errors in HVAC system. These results

must be contrasted with the HVAC requirements (air renovation requirements, pressure of the fan, etc.) to determine if the ventilation system was correctly designed. The second most probable cause, high occupancy density, was also found to be one of the major causes of air quality dissatisfaction in these rooms. These results are coherent with those obtained for room 305 with the same construction characteristics but medium occupancy where occupants revealed to have a neutral indoor air satisfaction.

# > Insert Figure 10 

For those rooms with a low level of indoor air quality comfort, a sensitivity analysis was carried out to determine which parameters (previous nodes) had more impact in achieving a 'very high indoor air quality comfort'. From a purely visual perspective, the length of a bar represents the measure of the impact of that node on the building condition performance (target node).

## > Insert Figure 11

Figure 11 shows the probability of the indoor air quality comfort performance being 'very high' (4.6\%). It can be concluded that the probability of rooms 303 and 306 having very high comfort levels is more sensitive to occupancy and HVAC design errors and least sensitive to ventilation control possibility. The HVAC system of rooms 303 and 306 was based on general AHU for all classrooms, which might be under dimensioned. However, the occupancy was high in these rooms, and instead of changing the AHU, which is costly, reducing the occupancy might bring higher levels of comfort in terms of indoor air quality.

## > Insert Figure 12

The sensitivity analysis for indoor air quality for room 302 in summer was also carried out. Figure 12 shows the impact of three factors when the indoor air quality in summer is 'very high' (5.7\%). The formal interpretation is that the probability of indoor air quality being very high, given the results of the parent nodes, rises from $3.3 \%$ (when HVAC design errors are 'high') to $24.1 \%$ (when HVAC design errors are 'low'). The HVAC condition and occupancy density did not significantly affect occupants' comfort in this room regarding indoor air quality in summer. Therefore, the most probable cause of discomfort in room 302 is 'HVAC design errors' which has a $91 \%$ probability of being high. Hence, a good design would include different equipment (changing the fan coil) to improve occupants' comfort in room 302 in terms of indoor air quality.

## 6. Discussion

The proposed approach of integrating occupants' feedback and the occupants' comfort probabilistic model into the BIM model classifies comfort aspects into thermal comfort, indoor air quality, visual comfort, acoustic comfort, and space adequacy, referred to each room of a building. The visualization of the probabilistic model results was implemented in Revit. However, the automation process of extracting and mapping information was incorporated in Dynamo allowing customization and interoperability with the majority of existing platforms (e.g., Power BI).

Although some studies developed a platform for integrating BIM and BN, they do not provide a generic method to evaluate the comfort performance of existing buildings, which allows the causes of occupants' discomfort in specific comfort aspects to be properly understood. This approach, therefore, presents a novel integration to facilitate data collection for the probabilistic model. It also enables the FM team to address the challenges of information reliability, interoperability, usability and minimisation of labour time.

Existing studies focus on the visualization of occupants' comfort in different platforms [62,63]. However, they only considered spatial information. The method of visualization in this approach focuses on real problems in discomfort spaces, demonstrating occupants' feedback in a color scale, and the results of causal factors of occupants' discomfort in a stacked bar chart, so that the effort of looking for appropriate information (e.g., building and spatial information) is minimized. The visualization of causal factors makes it possible to detect the causes of occupants' discomfort more intuitively and potentially makes it easier to deal with the problem, which will result in a considerable improvement in occupants' comfort and optimize building operation strategies to increase occupants' comfort.

The case study was used to validate the proposed approach. For the scenario of indoor air quality in summer, it was highlighted that although there were similar rooms with the same HVAC system, occupants presented different perceptions of the indoor air quality. It was identified that occupancy density ( $\mathrm{m}^{2} /$ person) has a considerable impact on indoor air quality perception and that redesigning these spaces, or reducing the occupancy, might improve indoor air quality comfort.

There are some limitations: (1) the results of causal analysis coming from a specific software, AgenaRisk, were mapped into BIM. The approach does not consider another software for allocating the results of causal analysis to the corresponding rooms in BIM. To address this issue, different Python code block in Dynamo is

required. (2) Occupants' reaction to satisfaction depends very much upon their age and level of fitness. Different information requirements should be studied to deal with these aspects, including the refinement of the probabilistic model through the incorporation of other causal factors affecting occupant's comfort.

# 7. Conclusion 

The assessment of building performance involves the analysis of multiple factors together with the occupants' feedback. The current probabilistic models to determine the causal factors of occupants' dissatisfaction do not provide a user-friendly visualization and are not interoperable with BIM to have easily accessible data. This paper presents a novel approach that integrates occupants' feedback and the occupants' comfort probabilistic model into BIM, organised by comfort aspects (thermal comfort, indoor air quality, visual comfort, acoustic comfort, and space adequacy). There are three key benefits of this integration: 1) BIM performs as a data repository, providing building and spatial information; 2) BIM can visualize causal factors of occupants' discomfort using an occupants' comfort probabilistic model and provides a potential solution for improving occupants' comfort; 3) BIM intrinsically supports data management and visualization (e.g., the visualization of occupants' feedback in color). The integration process can be used for other building performance aspects such as building condition, energy efficiency, in which occupants' feedback combined with building technical information might help FM decisions. Unlike existing models, using BIM as an integration tool allows automatic updates of the components' characteristics and data management, and enables visualisation. This visualisation method, based on occupants' feedback and the results of causal analysis, focuses on real problems in discomfort spaces and assists the FM team or owners to establish the necessary measurements for improving occupants' comfort.

The pragmatic findings of this study are two-fold. First, the FM team can make decisions on building operational problems centered on occupants' comfort with minimal effort which overcomes a key barrier to collection of required information within the operation and maintenance phase, enabling the much broader use of BN, BIM and their corresponding advantages (analyzing other building performance aspects, such as energy performance and accessibility). Second, the visualization permits a much broader range of FM data (i.e., building and spatial information) to be mapped to such models, with a minimum of effort. The implication of this is that the proposed approach will become much easier for buildings to pursue, enabling academic work,

and encouraging business adoption to increase. The proposed approach supports FM activities and puts occupants at the centre of maintenance/renovation decisions. Using the proposed approach, FM teams can define different scenarios to simulate outcomes and provide visual comparison between options in advance of retrofitting plan. The proposed approach could also be used to analyze the economic aspects that support the decision-making regarding renovation and retrofit actions. Scenarios to evaluate the comfort of different groups of occupants could also be performed.

The results and a case study showed that the proposed approach could yield a better understanding of the dependent factors of discomfort and the relationship between occupants' comfort, indoor environment and building characteristics. This integration and visualisation process is likely to be valuable to facility managers and owners who will be able to make a more precise analysis of building performance based on occupants' feedback; adopt building operational adaptations, and propose retrofit actions. Designers can also utilize the information to create future buildings that take into account the real needs of occupants. This process will also be of interest to other researchers who are integrating and visualising different operational data into BIM. Buildings of the future will offer a wide array of "smart technologies" - networked technology that controls aspects of air, light and thermal quality - therefore future steps will include integrating wearable technologies (e.g., sensor-based networks) that allow them to plug into the building system automatically and control their comfort. The use of the model can be extended by employing some technologies such as Artificial Intelligence (AI) and Internet of Things (IOT), which would coalesce together to create a fully integrated and automated solution. The model, for example, would be able to use machine learning, a subset of AI that trains a machine on how to learn from data and identify patterns. It could then make independent decisions on how to improve occupants' comfort. People would thus live in a truly smart built environment that automatically caters for the needs of every citizen.

# Acknowledgment 

This work was supported by Agència de Gestió d'Ajuts Universitaris i de Recerca (AGAUR) from Generalitat de Catalunya (2019 FI_B00064).

# Figures 

![img-0.jpeg](img-0.jpeg)

Figure 1. Automation process of integrating occupants' feedback and occupants' comfort probabilistic model into BIM

![img-1.jpeg](img-1.jpeg)

Figure 2. Dynamo script to map occupants' feedback into BIM

![img-2.jpeg](img-2.jpeg)

Figure 3. Dynamo script to extract information from BIM

![img-3.jpeg](img-3.jpeg)

Figure 4. Dynamo script to integrate occupants' comfort probabilistic model into BIM
![img-4.jpeg](img-4.jpeg)

Figure 5. BN model for "acoustic comfort" as an example

![img-5.jpeg](img-5.jpeg)

Figure 6. Tornado graph to analyze the sensitivity of acoustic quality as an example

![img-6.jpeg](img-6.jpeg)

Figure 7. BIM visualization for "acoustic comfort" as an example

![img-7.jpeg](img-7.jpeg)

Figure 8. Occupants' comfort level for indoor air quality in summer

![img-8.jpeg](img-8.jpeg)

Figure 9. BN model for indoor air quality in summer
![img-9.jpeg](img-9.jpeg)

Figure 10. The probabilities of having HVAC design errors or having a high HVAC condition for each room

![img-10.jpeg](img-10.jpeg)

Figure 11. Tornado graph to analyze the sensitivity of indoor air quality for rooms 303 and 306 in summer (Very high $=4.6 \%$ )
![img-11.jpeg](img-11.jpeg)

Figure 12. Tornado graph to analyze the sensitivity of indoor air quality for room 302 in summer (Very high $=5.7 \%)$

# Tables 

Table 1. CPTs for occupants' comfort


Table 2. Room information for indoor air quality obtained from BIM


# Appendix 

Section 1. Workplace details.
Please select the campus where you work/study:
$\square \quad$ Campus Terrassa
$\square \quad$ Campus Nord
Please select the building you work/study:
$\square \quad$ TR1
$\square \quad$ TR2
・...
On which floor of the building is your workspace or classroom located?
$\square \quad$ 1st floor
$\square \quad$ 2nd floor
$\square \quad$ 3rd floor
$\square \quad$ 4th floor
$\square \quad$ 5th floor
$\square \quad$ Other:
Please write the room name where you work or study:
How long have you been working/studying in this building?
$\square \quad$ Less than 1 year
$\square \quad$ Between 1 and 5 years
$\square \quad$ More than 5 years
Which of the following do you personally adjust or control in your workspace/classroom? (Check all that apply)
$\square \quad$ Window blinds or shades
$\square \quad$ Room air-conditioning unit
$\square \quad$ Portable heater
$\square \quad$ Permanent heater
$\square \quad$ Adjustable air vent in wall or ceiling
$\square \quad$ Ceiling fan
$\square \quad$ Portable fan
$\square \quad$ Thermostat
$\square \quad$ Operable window
$\square \quad$ None of these
$\square \quad$ Other:

Section 2. Satisfaction with the workplace.
Please write the room name where you work or study:
Indicate the degree of your satisfaction in relation to the different aspects of your workplace/classroom:


If you are dissatisfied, which of the following contribute to your discomfort

1. Thermal comfort:
$\square$ Always too hot
$\square$ Often too hot
$\square$ Occasionally too hot
$\square$ Occasionally too cold
$\square$ Often too cold
$\square$ Always too cold
2. Indoor air quality:
$\square$ The air is stuffy
$\square$ The air is dry
$\square$ The air is humid
$\square$ There are disturbing odors
$\square$ Other:
3. Visual comfort:
$\square$ Glare of sunlight
$\square$ Lack of daylight
$\square$ Dark
$\square$ Impossibility to control light
$\square$ Low level of artificial light
$\square$ High level of artificial light
$\square$ Other:
4. Space adequacy:
$\square$ Quantity of space $\left(\mathrm{m}^{2}\right)$
$\square$ Circulation space
$\square$ Privacy
$\square$ Ergonomics of chair and table
$\square$ Availability of equipment (furniture, printer, etc.)
$\square$ Lack of flexibility
$\square$ Other:
5. Acoustic comfort:
$\square$ Noise from air conditioner unit
$\square$ Noise from lights
$\square$ Noise from exterior machines

$\square \quad$ People talking loud in the corridor
$\square \quad$ Noise from elevator
$\square \quad$ No insulation between rooms
$\square \quad$ Other:

Section 3. Satisfaction with the common spaces.
For the following questions, in case you do not use some common areas, please select as not applicable.
Indicate the degree of your satisfaction in relation to the different aspects of the lobby, corridors, stairways:


Indicate the degree of your satisfaction in relation to the different aspects of the laboratories:


Indicate the degree of your satisfaction in relation to the different aspects of the conference room:


Indicate the degree of your satisfaction in relation to the different aspects of the restrooms:



Indicate the degree of your satisfaction in relation to the different aspects of the lunchroom:
