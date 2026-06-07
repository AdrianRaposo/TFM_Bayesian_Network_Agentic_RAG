# UPCommons 

## Portal del coneixement obert de la UPC

http://upcommons.upc.edu/e-prints

Aquesta és una còpia de la versió author's final draft d'un article publicat a la revista Journal of Cleaner Production.
http://hdl.handle.net/2117/167918

## Article publicat / Published paper:

Bortolini, R., Forcada, N. A probabilistic-based approach to support the comfort performance assessment of existing buildings. Journal of Cleaner Production, Novembre 2019, vol. 237, 117720. DOI: $<10.1016 /$ j.jclepro. 2019.117720 $>$.
(C) <2019>. Aquesta versió està disponible sota la llicència CC-BY- NCND 4.0 http://creativecommons.org/licenses/by-nc-nd/4.0/

Bortolini, R., and Forcada, N. A probabilistic-based approach to support the comfort performance assessment of existing buildings, Journal of Cleaner Production < doi: 10.1016/j.jclepro.2019.117720>.

Final version available at: <https://www.sciencedirect.com/journal/journal-of-cleanerproduction/vol/237/suppl/C>.

# A probabilistic-based approach to support the comfort performance assessment of existing buildings, 

Rafaela Bortolini ${ }^{1}$ and Núria Forcada ${ }^{2}$<br>${ }^{1}$ PhD Researcher, Department of Project and Construction Engineering (DPCE), Group of Construction Research and Innovation (GRIC), Universitat Politècnica de Catalunya (UPC), Colom, 11, Ed. TR5, 08222 Terrassa, Barcelona, Spain. E-mail: rafaela.bortolini@upc.edu (corresponding author)<br>${ }^{2}$ Associate Professor, Department of Project and Construction Engineering (DPCE), Group of Construction Research and Innovation (GRIC), Universitat Politècnica de Catalunya (UPC), Colom, 11, Ed. TR5, 08222 Terrassa, Barcelona, Spain. E-mail: nuria.forcada@upc.edu


#### Abstract

Building performance is focused on maintaining and increasing sustainability while enhancing occupants' comfort levels. Occupants' comfort depends on uncertain, interrelated personal, social and building factors. However, the relationships between these factors are not covered by performance assessment tools based on linear analysis approaches. This study proposes a probabilistic model based on Bayesian networks (BNs) to assess the comfort performance of a building. An extensive review and evaluation of the causal factors of building performance, supported by the results of a satisfaction survey, are the basis for the BN model. Sensitivity analysis is used to verify the BN model, and the proposed approach is tested on an existing building. Findings from this research can guide decision-makers in the facility management industry to assess and understand causal factors of occupants' comfort to properly establish sustainable and cleaner production strategies.


## Author keywords:

Environmental quality, performance assessment, probabilistic modeling, Bayesian networks

# 1. INTRODUCTION 

The incorporation of sustainable attributes into buildings has been accepted widely as a positive measure from economic, environmental and social perspectives (Reed et al., 2005). There is evidence that buildings' indoor conditions have far-reaching implications for occupants' comfort, health and productivity (Frontczak and Wargocki, 2011; Sharmin et al., 2014; Li et al., 2018) and energy efficiency (Keyvanfar et al., 2014), which are the main goals of building sustainability (Reed et al., 2005; Wilkinson, 2009).

To encourage the uptake of sustainability in buildings, sustainability must be maintained and increased while comfort levels are sustained and enhanced (Ruparathna, Hewage and Sadiq 2016). For example, there has been a focus on adopting natural ventilation over air conditioning systems and natural light over artificial (Alibaba, 2016; Ruparathna, Hewage and Sadiq, 2016) among other factors. The assessment of building performance based on occupants' comfort can help building sustainability and the implementation of cleaner production programs through preventive and corrective maintenance processes (including retrofitting and space adaptation) (Menassa and Baer, 2014).

Numerous studies have developed methods and tools to assess the performance of a building, taking into account the indoor environment and which conditions are considered comfortable (Frontczak and Wargocki, 2011). Post-occupancy evaluation (POE) is a common technique used to measure building performance from the user's perspective (Preiser and Vischer, 2005). POE surveys are focused on assessing occupants' comfort and productivity, and the more sophisticated ones can also conduct physical measurements of Indoor Environmental Quality (IEQ) (Li et al., 2018). Standards based on IEQ factors have been developed to define the acceptable ranges of comfort (e.g., ASHRAE 2013). Indicators such as ventilation rate or CO2 concentration, temperature and lighting intensity, are the most frequently used in guidelines and standards (Bluyssen, 2010).

These assessments methods are based on deterministic models (Agha-Hossein et al., 2013; Catalina and Iordache, 2012; Wagner et al., 2007) and do not consider the effect of variability in factors that influence indoor environmental condition, such as the building microclimate, building properties and usage patterns (Chen et al., 2017; Van Gelder et al., 2014). Comfort is much more than the average of perceived indoor air quality, noise, lighting and thermal comfort responses (Bluyssen et al., 2011).

Occupants' control of the indoor climate and moreover the perceived effect of their intervention (i.e., control action) strongly influence occupant satisfaction with thermal indoor conditions (Wagner et al., 2007). Occupants' comfort is also influenced by several variables, such as the building envelope (e.g., insulation and infiltration), building systems (e.g., HVAC and lighting), and occupants' behavior (Abisuga et al., 2016; Catalina and Iordache, 2012). Improper operation or failure of the HVAC system may lead to poor ventilation, which in turn can cause a range of health problems and a condition called sick-building syndrome (Au-Yong et al., 2014; Rostron, 2008).

Problems in the walls, such as dampness, were also found to be relevant in an analysis of occupants' comfort (Abisuga et al., 2016).

The relationships between these personal, social and building factors are complex and their uncertainty needs to be accounted for to effectively assess building comfort (Bluyssen et al., 2011; Chen et al., 2017). To close this gap, a probabilistic approach for assessing building comfort can be used. Unlike traditional models, Bayesian networks (BNs) can model building comfort as a probabilistic process, to give the most probable performance level of a building using probability distributions.

Some researchers have used BN to analyze occupant's satisfaction with specific services (Salini and Kenett 2009, Chakraborty et al. 2016) or to predict thermal preferences (Langevin et al. 2013 Auffenberg, Stein and Rogers 2015; Lee et al. 2017). However, the use of BN to model occupants' comfort in terms of personal, social and building factors has not been investigated to date.

This study presents the development of a BN model to assess the comfort performance of buildings. The model includes multiple interacting factors and supports decisionmaking on maintenance and retrofitting actions to enhance the comfort and sustainability of buildings. A literature review, domain experts and the results of a satisfaction questionnaire administered to 1,001 users in 37 buildings were used to create the model, which was then validated in existing buildings and verified using sensitivity analysis.

# 2. METHODS 

Notwithstanding the difficulty in representing human behavior in buildings, this study proposes the use of BN: a probabilistic graphical model that provides a formalism for reasoning about partial beliefs under conditions of uncertainty (Pearl, 2000, 1991). A BN model consists of a directed acyclic graph (DAG) and an associated set of conditional probability tables (CPTs) (Pearl, 1997). A DAG is comprised of nodes that represent random variables with a finite set of states, and the edges correspond to probabilistic causal dependence among the variables (Pearl, 1991). CPTs specify the degree of belief (expressed as probabilities) that the node will be in a particular state given the states of the parent nodes (the nodes that directly affect that node) (Pearl, 1991). BNs also handle uncertainty though the established probability theory. The notion of causation is related to finding a satisfactory explanation for a given set of observations and determining the meaning of the explanation (Pearl and Verma, 1994). Furthermore, BNs are apt for utilizing data and knowledge from different sources and handling missing data (Pearl and Verma, 1994).

The research process adopted in this study is illustrated in Figure 1. The construction of the BN model is based on existing methods (Chen and Pollino, 2012; Fenton and Neil, 2012) and consist of four main steps: key variables identification, model structure definition, CPTs definition and model evaluation.

![img-0.jpeg](img-0.jpeg)

Figure 1. Research process
The most common BN modeling tools used by the scientific community were explored to construct the BN model. AgenaRisk was selected for its power, versatile capabilities and user-friendly interface (Perez-Minana, 2016). The model focuses on existing nonresidential buildings, in which facility managers are typically in charge of the building performance management.

# 2.1. KEY VARIABLES IDENTIFICATION 

The most influential variables in a building's comfort performance were initially identified by literature review. Variables consist of factors that affect building performance and indicators to quantify the performance. In the BN model, each variable is represented as a node. All nodes in the model must affect (or be affected by) the final output. If this is not the case, the node can be removed (Chen and Pollino, 2012).
Second, a questionnaire survey was developed to understand the main causes of comfort dissatisfaction. The questionnaire was administered in two university campuses of the Universitat Politècnica de Catalunya (UPC), including 37 buildings. The structure of the questionnaire included:

- Section 1. Respondents' details, including gender and age.
- Section 2. For regular users: workplace location (building group and building name) and workplace characteristics, including years of working in the same workplace and availability of personal control adjustments (curtain, windows, ventilation, thermostat and others). For sporadic users: building group and most frequently used building (campus and building name) and years of working in the same building.
- Section 3. The survey asks regular users to rate their satisfaction in relation to some aspects of their workplaces, including: thermal sensation in winter and summer, air quality in winter and summer, light quality, cleanliness, space adequacy and acoustic quality. The survey uses a 5-point scale to rate occupants' satisfaction ranging from "very satisfied" (5) to "very dissatisfied" (1), with a neutral midpoint (3). The survey also asks the reasons for dissatisfaction given the predefined options, and contains a text entry box for the respondents to add other reasons.
- Section 4. The survey asks regular and sporadic users to rate their satisfaction in relation to some aspects of the common spaces of the building that they use most (e.g., classrooms, corridors, conference rooms, restrooms and dining rooms), including: thermal sensation in winter and summer, air quality in winter and summer, light quality, cleanliness, space adequacy and acoustic quality.
- Section 5. The survey asks regular and sporadic users to rate their satisfaction in relation to the building's accessibility, and their general satisfaction with the building. Regarding the building condition, possible reasons for dissatisfaction

are predefined, and a text entry box is provided to add other reasons. An openended question is also included, allowing respondents to comment on what they personally found relevant.

# 2.2. MODEL STRUCTURE DEFINITION 

The BN model structure was defined in two steps. First, a literature review was conducted to analyze the relationships (cause-effect) of key variables that affect a building's comfort performance. Second, satisfaction survey results were statistically analyzed. To check and improve the model structure, an adaptation of the Delphi method (Wright and Rowe, 1999) was conducted. Nine experts in building performance and facility management (FM) were interviewed. All interviewees had over 10 years of experience in FM consulting and maintenance activities, while three of them were also specialists in energy management. The interviews lasted between an hour and an hour and a half and the experts were asked to review the model by adding, changing, erasing and weighting the existing causal factors and relationships, if necessary.

The Delphi method consists of a procedure to obtain the most reliable consensus of opinion in a group of experts (Wright and Rowe, 1999). As in many cases where the Delphi method is used to elicit expert opinion, some intermediate nodes were added and missing relationships were established in the final version of the network to increase the model's content validity. Participants were encouraged to review the anonymous opinion of the other experts and consider revising their previous response. The goal during this process was to decrease the variability of the responses and achieve consensus. The model was then refined after rounds of questions with feedback until consensus was reached between the experts.

### 2.3. CPTS DEFINITION

The CPTs of each node of the model were defined in two main steps. First, a literature review and reports on the European building stock (e.g., BPIE, 2011) were consulted to define the pattern (i.e. probability distribution) of some nodes. Second, for the nodes that had no available data, information was elicited from domain experts. Experts were asked to provide the most-likely values for some variables under consideration. They had to identify the impact of the relationships between nodes and their uncertainty on the CPTs. This information was used to define statistical distribution expressions.

A node can be discrete (labeled, Boolean, discrete real and ranked) or continuous (Fenton and Neil, 2012). The states of the nodes depend on the type. Some nodes are defined as Boolean and have binary states such as "Yes" and "No". Others are defined as ranked nodes. Due to the underlying numerical scale of the ranked nodes, numerical statistical distribution expressions can be defined. The truncated Normal distribution (TNormal) is especially useful for defining numerical statistical distributions as expressions (Fenton and Neil, 2012). Unlike the regular Normal distribution, TNormal has finite end points that go from 0 to 1 in equal intervals. Like the Normal distribution, TNormal is characterized by two parameters: mean and variance. The variance parameter reflects the influence of parent nodes' uncertainties. As the variance rises, the distributions gets closer to uniform. This enables a variety of distribution shapes to be

modelled. In the simplest case, the parameter mean is determined as a weighted mean of the parent nodes with the following expression:

$$
W M E A N=\frac{21=1 \ldots n w i X i}{n}
$$

where $\mathrm{wi} \geq 0$ are weights, and n is number of parent nodes. In AgenaRisk, the syntax of the function is:

$$
\text { wmean (w1, parent1, w2, parent2,..., wN, parentN) }
$$

Indeed, this distribution is sufficiently flexible that it has been proven to generate satisfactory CPTs for almost all BN fragments involving a ranked node with ranked parents (Fenton and Neil, 2012).

# 2.4. MODEL EVALUATION 

The objective of a model evaluation is to ensure that the model's interactions and outcomes are feasible (Chen and Pollino, 2012). Generally, there are two methods for evaluating a model: verification and validation (Sargent, 2013). Validation assures that a product, service or system meets the needs of the customer and other identified stakeholders (Engel, 2010). Verification demonstrates that a problem formulation has been transformed into a model specification with sufficient accuracy (Balci, 1997).

First, two existing buildings were selected to analyze scenarios. Forward and backward propagation were then used to refine the strength of the relationships between the nodes and make the model more accurate. Forward propagation implies the propagation of an observed variable and measures its impact on the target variable (Pearl, 1991). If there is enough evidence that an observation occurs, then the observation can be entered into the model, and the probabilities of all unobserved variables can be updated. Backward propagation is another useful feature of BN. In backward propagation, an observation is made for a specific variable, and then the BN calculates the marginal probabilities of unobserved variables by propagating the impact of the observed variable through the network in a backward fashion (Pearl, 1991).

Second, a sensitivity analysis was undertaken to understand the most significant factors in the model and to verify whether the model response conforms to expectations. Sensitivity analysis is a useful way to check the validity of a BN model, and reveals diagrammatically which nodes have the greatest impact on any selected (target) node (Fenton and Neil, 2012).

Finally, a case study was used to verify the model. The model verification was conducted by assessing the behavior of parts of the model under different scenarios: to make predictions, determine causal factors of known variables and conduct what-if scenarios to make decisions.

# 3. BN MODEL FOR BUILDING COMFORT PERFORMANCE 

### 3.1. KEY VARIABLES AFFECTING BUILDING COMFORT

Occupant's comfort in non-residential buildings is influenced by physical and nonphysical factors (Geng et al., 2019). Physical factors include the four aspects of IEQ: thermal, visual, acoustic environment and air quality (Frontczak et al., 2012; Frontczak and Wargocki, 2011). Non-physical factors generally refer to those space qualities that are difficult to measure with instruments, such as space layout, privacy, furnishing and cleanliness (Frontczak et al., 2012; Geng et al., 2019).

For thermal quality, studies revealed that factors other than indoor air temperature play an essential role, including the climate, the characteristics of the building and its services (Hua et al., 2014). It was found that people indoors felt warmer in winter than in summer, even though the indoor temperature was lower in the winter (Oseland, 1994). The type of HVAC system also plays a role in thermal comfort. For instance, radiant systems can provide higher comfort levels for indoor temperature (Karmann et al., 2017). Furthermore, occupants with thermal adaptive opportunities present high levels of comfort (Kim and De Dear, 2012). Al-atrash, Hellwig and Wagner (2018) identified that the most desired control options are operable windows and thermostats. Thermal characteristics such as envelope insulation is particularly relevant for buildings that rely on thermal passive strategies (Catalina and Iordache, 2012). In this sense, an envelope with a low thermal transmittance (U-value) can help extend the periods of thermal comfort without reliance on mechanical air-conditioning (Al-Homoud, 2005). The condition of the envelope is also identified as a contributing factor to the performance of the building envelope. The main defects in the façade, roof and doors/windows are obtained from Bortolini and Forcada (2018a).

Good indoor air quality is related to the ventilation rate (Bluyssen, 2010). In this context, criteria/threshold values for ventilation rate are recommended by regulations. For instance, the Spanish regulation Royal Decree 1027/2007 (RITE, 2007) provides the minimum fresh (outdoor) air rates based on occupancy and type of use. For high indoor air quality, a minimum of $12.5 \mathrm{l} /$ person should be adopted for ventilating office and academic buildings. Moreover, the type of ventilation system adopted in a building can influence the occupants' comfort perception. Generally, naturally ventilated buildings have higher rates of comfort than air-conditioned buildings (Rostron, 2008). The occupants can open windows and so they can vary the indoor environment to some extent. However, natural ventilation is dependent on weather conditions (e.g., temperature, humidity and wind speed) (Chilton et al., 2012), and might not be adequate in environments with extreme temperature (e.g., extreme cold or extreme heat). Therefore, the most comfortable type of ventilation should be conditioned to the exterior environmental characteristics. For buildings with mechanical ventilation, the condition of the HVAC system is an important factor, as its improper operation may lead to poor ventilation causing health problems and discomfort (Au-Yong et al., 2014; Rostron, 2008).

For light quality, the impact of daylighting can be considered quantitatively through the window-wall-ratio (WWR). There is a strong preference for daylight in workplaces,

which is closely associated with the belief that daylight is better for health (Galasiu and Veitch, 2006). However, occupants of buildings with a high WWR (e.g., a glazed façade) may have lower perceived control (Hellwig, 2015). Pino et al. (2012) demonstrated that lower WWRs with solar protection can achieve better daylight performance than larger WWRs, due to prevention of glare. Window shading is a key element in controlling glare and overheating, both of which affect the occupants' wellbeing (Galasiu and Veitch, 2006).

For acoustic quality, physical parameters are linked with the quality of the sound environment, which includes exterior and interior sound insulation of walls. Jensen, Arens, and Zagreus (2005) demonstrated that the main reasons for dissatisfaction are almost the same in all types of offices, and that people are mostly dissatisfied with hearing other people talking on telephones, private conversations being overheard and the sound of people talking in surrounding offices. Equipment noise is another source of acoustic discomfort reported in some studies (Leaman and Bordass, 2001). Acoustic attenuators used in mechanical ventilation systems can reduce noise from air systems. Buildings with natural ventilation might lead to discomfort due to outside noises.
Regarding space adequacy, occupant satisfaction is influenced by space characteristics including size, aesthetic appearance, furniture and cleanliness (Bortolini and Forcada, 2018b; Frontczak et al., 2012). Ergonomic furniture and enclosed rooms for meetings and collaborative work are examples of factors that help ensure users' functional comfort at work (Vischer, 2008).

Design errors might be factors that cause occupants' discomfort with air, thermal and light quality (Aghemo et al., 2014; Roulet et al., 2006). Error can be defined as 'the failure of planned actions to achieve their desired goal, where this occurs without some unforeseeable or chance intervention" (Reason and Hobbs, 2003). The wrong dimensioning of room conditioning systems or failure to design appropriate daylight controls are some design errors that affect building comfort performance.

# 3.2. RELATIONSHIPS BETWEEN VARIABLES - SATISFACTION SURVEY RESULTS 

### 3.2.1. Database description

Building occupants are the best source of information on needs and comfort requirements (Frontczak et al., 2012). Therefore, to understand and check the relationships stated in the literature, a satisfaction survey was conducted in two UPC campuses with 37 buildings.

Occupants were contacted by email in October 2017. A total of 1,001 valid responses were received. A total of $71.12 \%$ of the respondents were men and $28.88 \%$ were women. The average age of respondents was 28.87 years, with a standard deviation of 13.63. Most of the occupants ( $72.06 \%$ ) had worked in the same building for over 5 years.

# 3.2.2. Analysis of comfort factors 

Users were asked to report reasons for their dissatisfaction, and 698 out of the 1,001 participants gave at least one cause of dissatisfaction. "Frequently hot" was noted as the greatest source of occupant dissatisfaction in the summer. Two reasons were given for this problem in the summer season, when the cooling system is on. The first is that in some cases, thermostats were shared by the next-door office, and therefore the indoor environment of one individual's workspace was controlled by the next-door occupant's thermal perception and attitude. This situation caused a perceived lack of personal control. The other cause was related to design errors. The low thermal insulation of the buildings together with high temperatures in summer, requires a cooling system to acclimatize the rooms. Even though these buildings require a cooling system, some have only been designed with a heating system. Therefore, occupants experience greater discomfort in summer. In the winter season, many occupants stated that they were "frequently cold", which is associated with the fact that they could not control the temperature.
"Stuffy air" was the most frequent reason given for air quality discomfort. Most of the buildings only have natural ventilation. This suggests that passive ventilation strategies (e.g., cross ventilation) might not be enough to renovate the spaces in these buildings. Indeed, most of these buildings were constructed before the introduction of legislation that make the adoption of forced or mixed ventilation for non-residential buildings compulsory in Spain (RITE, 2007).

In the Pareto diagram (Figure 2), the causes of dissatisfaction with thermal and air quality accounting for more than $80 \%$ of the responses were identified as the most significant.
![img-1.jpeg](img-1.jpeg)

Figure 2. Causes of dissatisfaction frequency: (a) thermal quality and (b) air quality

The survey results revealed that issues related to glazing and shading, such as "sun glare", "lack of daylight" and "impossibility of controlling light", were cited as reasons for light quality discomfort. "Noise from HVAC equipment", "noise from exterior equipment" and "noise from people talking in the corridor" were the top three reported causes of acoustic quality discomfort. These problems were mainly associated with the low interior and exterior acoustic insulation of the walls. The causes of dissatisfaction with light and acoustic quality accounting for more than $80 \%$ of responses were identified as the most significant in the Pareto diagram (Figure 3).
![img-2.jpeg](img-2.jpeg)

Figure 3. Causes of dissatisfaction frequency: (a) light quality and (b) acoustic quality
Regarding space adequacy, "furniture ergonomics", "lack of flexibility" and "inadequate space distribution" were the three most frequent reasons for dissatisfaction selected by the respondents. The causes of dissatisfaction with space adequacy accounting for more than $80 \%$ of responses were identified as the most significant in the Pareto diagram (Figure 4).
![img-3.jpeg](img-3.jpeg)

Figure 4. Causes of dissatisfaction frequency: space adequacy

# 3.2.3. Delphi method results 

To check and refine the relationships, interviews were undertaken with domain experts using an adaptation of the Delphi method. Nine experts were interviewed between June and July 2018. Experts were asked to analyze the model and validate, add, change or erase the existing causal factors and relationships, if necessary. In general, experts agreed with the proposed relationships and helped define the classification of HVAC systems in relation to occupants' comfort. Experts also suggested the incorporation of accessibility as a contributing factor in the category of space adequacy.

### 3.3. GENERIC BN MODEL

The relationships identified in the literature within the statistical results for the causes of discomfort and reinforced by the domain experts were used to define the model structure. The generic model to manage a building's comfort performance is illustrated in Figure 5.
![img-4.jpeg](img-4.jpeg)

Figure 5. Generic BN model for assessing a building's comfort performance

# 3.4. CPTS FOR COMFORT NODES 

Survey results, the literature review and experts' opinions were used to define the CPTs of each node of the BN model. The CPTs were defined as generically as possible for the model to be applied in the European context. However, probability distributions for some variables can be adapted to a specific context (region/country).

The different levels of uncertainty involved in the variables for assessing building comfort performance lead to the definition of discrete, uniform, triangular, or normal probability distributions, depending on the input parameters (Calleja Rodríguez et al., 2013). For instance, if there are large uncertainties about a specific input parameter, this is modelled using the uniform distribution function. The opposite case would be to define input parameter uncertainty by the normal distribution.

In this study, TNormal is used to define probability distribution in most cases. As previously described, TNormal is an appropriate distribution, since it provides flexibility to generate a variety of distribution shapes when the mean ( $\mu$ ) and variance $\left(\sigma^{2}\right)$ are defined (Fenton and Neil, 2012).

For envelope insulation nodes, the European Building Stock Observatory database (2018) was consulted to obtain the most common thermal transmittance (U-value) values for façade, roof and window. The average U-value for non-residential buildings is $1.1 \mathrm{~W} / \mathrm{m}^{2} . \mathrm{K}, 0.83 \mathrm{~W} / \mathrm{m}^{2} . \mathrm{K}$ and $3.17 \mathrm{~W} / \mathrm{m}^{2} . \mathrm{K}$ for façade, roof and windows, respectively (EU Building Stock Observatory, 2018). Moreover, there is a degree of uncertainty in U-values, as defined by Bordbari, Seifi and Rastegar (2018), who defined probability distribution functions for uncertain parameters. These values were adapted to a TNormal distribution, as illustrated in Table 1.

Table 1. CPTs for comfort nodes




The building geometry (proportions of windows, wall and roof) influences the thermal resistance of the building envelope (Parasonis et al., 2012). Therefore, the envelope insulation node is conditioned to the building geometry and the WWR. The WWR is defined as the ratio of the glazed area with respect to the total area of the envelope (Pino et al., 2012). Based on work conducted by Alibaba (2016) and Pino et al. (2012), some ranges for WWR were defined, as shown in Table 1. The envelope performance node depends on the infiltration rate, which is influenced by age, construction quality, building use and weather conditions (Macdonald, 2002). The envelope condition node refers in this case to defects that can cause infiltration such as cracks, leaks and openings problems (Sadineni et al., 2011). The CPTs for the envelope condition are defined in Bortolini and Forcada (2018c).

The possibility of controlling each IEQ factor is extremely valuable for the occupants' comfort. Kim et al. (2017) conducted an extensive literature review and classified occupant personal controls into thermostat control, shade control, ventilation control (fan control and window opening) and light control. Each personal control is defined as a Boolean node.

For exterior conditions in winter and summer, the nodes were defined as ranked type. Uncertainty in the exterior condition has been handled by a normal distribution to quantify uncertainty in both ambient temperature and relative humidity (Huang et al., 2015).

For thermal comfort, the heating type and cooling type were defined as labelled nodes with the following states: radiant, all-air, others and not applicable. For ventilation type, three states were defined: natural, forced and mixed.

Regarding the importance of the parent nodes for each IEQ factor and space adequacy, several studies were consulted in the literature (Dogrusoy and Tureyen, 2007; Frontczak et al., 2012; Karmann et al., 2017; Kim and De Dear, 2012). Domain experts were also asked to refine the importance of the variables. In general, thermal comfort is considered the most important parameter influencing overall satisfaction (Frontczak and Wargocki, 2011; Kim and De Dear, 2012). Furthermore, occupants with ample adaptive opportunities also express high levels of satisfaction with IEQ (Kim and De Dear, 2012).

# 3.5. BN COMFORT MODEL EVALUATION 

### 3.5.1. Data validation

The proposed BN model was validated with two academic buildings on the Campus Nord of the UPC. Table 2 shows their main characteristics, which were obtained from the technical inspection described in Bortolini and Forcada (2018a). The main use of building CN -A4 is for lectures, while building CN-B2 mainly contains offices. Aggregated data (regular and sporadic users) were presented for the satisfaction survey results. However, differences were found for different users.

Table 2. Buildings CN-A4 and CN-B2 characteristics



First, a forward propagation analysis was conducted to obtain the probabilities of each comfort factor when the evidence was established for their parent nodes. The results of the forward propagation were then validated with the results of the satisfaction survey of the selected buildings.

When the acoustic quality was analyzed, evidence on the characteristics of buildings CN-A4 and CN-B2 was entered in the parent nodes (Figure 6). The probability of having a high level of acoustic quality was higher in building CN-B2, which is in agreement with the satisfaction survey results. The most probable cause is the type of ventilation system. Building CN-B2 has mixed ventilation, while Building CN-A4 only has natural ventilation. Therefore, in CN-B2, windows can be closed to prevent excessive traffic noise from outside, if necessary. Another cause could be the high occupancy density of building A4 ( $1.74 \mathrm{~m} 2 /$ person), which is mainly devoted to classes. In contrast, the spaces in building CN-B2 are designated as office buildings, with a low occupancy density ( $5.38 \mathrm{~m} 2 /$ person).

![img-5.jpeg](img-5.jpeg)

Figure 6. Acoustic quality for building CN-A4 (blue bars) and CN-B2 (green bars)
The light quality for the buildings is illustrated in Figure 7. In both buildings, the end user can control the artificial light, but occupants can only control the sun glare through shades in the building CN-A4 (Figure 8). Building CN-A4 has a higher probability of obtaining good light quality than building CN-B2. In the survey results, respondents complained about the low daylight and high artificial light levels in building CN-B2. The low WWR is the most probable cause of the dissatisfaction of users of building CN-B2. The satisfaction survey results indicated the same average level for light quality in both buildings.
![img-6.jpeg](img-6.jpeg)

Figure 7. Light quality for buildings CN-A4 (blue bars) and CN-B2 (green bars)

![img-7.jpeg](img-7.jpeg)

Figure 8. Shade control: (a) building CN-A4 and (b) building CN-B2Buildings
CN-A4 and CN-B2 have different thermal quality characteristics. Building CN-A4 only has a heating system and building CN-B2 has a heating and cooling system. Even with a cooling system, building CN-B2 has a probability of $66.7 \%$ of medium thermal quality. This is because the condition of the HVAC system has a probability of $43.3 \%$ of being low, and the envelope condition has a probability of $24.3 \%$. The results of the BN model were compared with the survey results, which showed that end users are not satisfied with the thermal quality in the summer in building CN-B2. The results suggested that it is not enough to have a cooling system in a building to produce high thermal comfort; the maintenance and smooth running of this equipment also influences end users' perceptions of thermal quality. The forgiveness factor could also influence the satisfaction of end users. End users of building CN-B2 would expect higher thermal quality, since there is a cooling system to acclimatize the building in summer. In contrast, end users of building CN-A4 would not expect higher thermal quality in summer, since the building does not have a cooling system. Some studies support this evidence that forgiveness is greater when the most desirable features are present in a building (Hellwig, 2015). People working in air-conditioned spaces are isolated from the outdoor environment, therefore they expect their buildings to provide consistent thermal environmental conditions regardless of outdoor weather conditions (Kim and De Dear, 2012).

Considering air quality, the satisfaction survey results revealed that the air quality in summer was similar in both buildings. However, building CN-A4 had a higher probability of comfortable air quality than building CN-B2. Forgiveness is greater for buildings with natural ventilation. End users may be more likely to tolerate otherwise excessively uncomfortable conditions in buildings with natural ventilation (Leaman and Bordass, 2007). In passively ventilated buildings, more adaptive mechanisms (e.g., operable windows) are typically available to the occupant for comfort and consequently support greater individual awareness of the available adaptive opportunities.

# 3.5.2 Model verification: sensitivity analysis 

A sensitivity analysis was carried out to verify the BN model. From a practical point of view, sensitivity analysis in a probabilistic network consists of the computation of the probability outcomes of the target nodes given the evidence. In particular, a sensitivity analysis indicates diagrammatically which nodes have the greatest impact (length of the bars) on any selected target node, and in which states. A sensitivity analysis is available for each node and each node state, but only a few examples are included here, to show the most interesting results.

Figure 9 shows the probability of building comfort performance being Very High given that the results of the parent nodes rise from $0.1 \%$ (when thermal quality is Very Low) to $9.5 \%$ (when thermal quality is Very High). It can be concluded that the probability of a building having very high comfort levels is more sensitive to changes in the states of thermal quality, acoustic quality and air quality, and least sensitive to changes in space quality and light quality. The results are in agreement with previous studies claiming that building users consider thermal comfort to be the most important parameter influencing overall satisfaction, followed by acoustic comfort and satisfaction with air quality that were considered of similar importance, and visual comfort as the least important factor (Frontczak and Wargocki, 2011).
![img-8.jpeg](img-8.jpeg)

Figure 9. Tornado graph to analyze the sensitivity of building comfort performance (Very High $=2.0 \%)$

A sensitivity analysis was also conducted for thermal quality, air quality and light quality. Similar thermal quality results were obtained for winter and summer. Figure 10 illustrates the impact of six variables when the thermal quality in summer is Very High (4.7\%). Clearly, cooling type, design errors and exterior condition in summer have the greatest impact. Design errors could be related to selection of the wrong type of equipment, or incorrect design of system capacity.

![img-9.jpeg](img-9.jpeg)

Figure 10. Tornado graph to analyze the sensitivity of thermal quality in summer (Very High = $4.7 \%)$

Figure 11 shows the impact of seven variables when the air quality in winter is Very High (7.7\%). The ventilation type and exterior condition in winter have the greatest impact. Design errors and occupancy density also have a considerable impact. The denser the occupancy of a space, the stuffier the air could be if the ventilation system is not designed correctly.
![img-10.jpeg](img-10.jpeg)

Figure 11. Tornado graph to analyze the sensitivity of air quality in winter (Very High = 7.7\%)

The sensitivity analysis for light quality is shown in Figure 12. The formal interpretation is that the probability of light quality being Very High given the results of the parent nodes rises from $1.6 \%$ (when design errors are High) to $36.9 \%$ (when design errors are Low). The window-wall-ratio has the greatest impact on light quality, indicating that a medium ratio (between 10 to $40 \%$ ) is the most comfortable solution. The light control possibility and the shade control possibility have similar impacts on light quality.
![img-11.jpeg](img-11.jpeg)

Figure 12. Tornado graph to analyze the sensitivity of light quality (Very High $=15.6 \%$ )

# 3.6. CASE STUDY - BUILDING PERFORMANCE SCENARIOS 

To evaluate the applicability of the proposed model, building CN-C2 from Campus Nord was used as a case study. The selected building was constructed in 1989 and has 2,124 square meters. The main characteristics of this building are shown in Table 3. Table 3 also includes the results of the technical inspection conducted on the building envelope and the problems with the HVAC system.

Table 3. Building CN-C2 characteristics



# 3.6.1. Assessment of a building's performance and identification of causal factors 

The characteristics of the building were entered in the model as evidence to assess its comfort performance. The results are shown in Table 4. Building CN-C2 has a probability of $2.87 \%$ of being very high and $35.56 \%$ of being high comfort performance.

Table 4. Comfort performance results for the case study


The results demonstrated that the most probable level of acoustic quality in the CN-C2 building is low/medium ( $47.53 \%$ ). CN-C2 had a high probability of space adequacy being high ( $67.89 \%$ ). The air quality had a probability of $58.44 \%$ of being high, while the thermal quality presented a probability of $62.32 \%$ of being medium. Regarding the thermal quality in summer, the results revealed a probability of $72.63 \%$ of being medium. This result could be attributed to the low condition of the HVAC system.

The light quality is the IEQ factor with the most probability of being low. The most likely reason for this result is the low WWR, which limits the daylight (Figure 13). However, preferred illuminance levels in offices with daylight vary widely from one person to another, as reported by Galasiu and Veitch (2006). In addition, desired quantities of additional electric light vary with the type of task and the distance from the window (Galasiu and Veitch, 2006). To increase the light quality of this building, further investigation is required to ensure that the level of artificial light is adequate for all workspaces and/or to provide additional control options to occupants such as the possibility of choosing the electric lighting level. Control systems are more acceptable to both occupants and facility managers when they are simple and easy to use (Galasiu and Veitch, 2006).
![img-12.jpeg](img-12.jpeg)

Figure 13. Building CN-C2

# 3.6.2. Prediction of performance through renovation and retrofit scenarios 

Based on the results presented in Table 4 and the cause analyses, some interventions were made to improve the comfort performance of the building. A what-if scenario to improve the thermal quality was defined to conduct a backward propagation analysis. An observation was made setting the HVAC condition as "very high" state (i.e., HVAC system operating without problems) and changing the preventive maintenance of the HVAC system to "Yes". This scenario led to a reduction in the probability of defects in the HVAC system and consequently, improved thermal quality. Before the renovation, the thermal quality was most likely to be medium ( $62.32 \%$ ). The result of the proposed scenario predicted that the thermal quality would be improved, with $55.01 \%$ probability of being high (very high $=3.27 \%$, high $=55.01 \%$, medium $=40.94 \%$, low $=0.78 \%$, very low $=0.0 \%$ ). These results corroborate that poor maintenance and problems in the HVAC systems can cause discomfort to users.

Another what-if scenario is to analyze the implications of using a mixed mode ventilation system. Although natural ventilation is considered an energy efficient alternative to reduce energy use, the results revealed a low level of comfort regarding the indoor air quality. The natural ventilation adopted by $\mathrm{CN}-\mathrm{C} 2$ may not be enough to

freshen the air of rooms with high occupation. Moreover, the use of natural ventilation is compromised during winter due to weather conditions, i.e., low probability of opening windows in cold days. The prediction results of using a mixed mode ventilation system revealed that the air quality would be improved (very high $=3.37 \%$, high $=$ $58.85 \%$, medium $=37.10 \%$, low $=0.0 \%$, very low $=0.0 \%$ ).

# 3.6.3. Prioritization of maintenance actions 

Another potential application of the proposed model consists of prioritizing maintenance actions to promote sustainability, taking into account occupants' comfort. For example, envelope performance, HVAC condition, temperature control possibilities and heating type impact the thermal performance and can be improved potentially. Based on the impact of these causal factors on the thermal performance and sustainability, owners can prioritize whether to insulate the façade, implement temperature control possibilities and change or upgrade the heating equipment, among other factors.

The model can be used to benchmark and prioritize retrofitting and or investments in buildings. This is especially valuable for institutions with a tight budget for managing many buildings, such as university campuses. Hence, the buildings on the two UPC campuses could be analyzed to assess comfort performance results. This could help the Facility Campus department to make decisions to improve the building stock and support better management of the resources.

Scenarios to evaluate the comfort of different groups of users (regular and sporadic) could also be performed. For instance, differences were obtained when specific common spaces of the buildings were evaluated in the satisfaction survey conducted on the university campuses. Sporadic users (i.e., students) were more dissatisfied with the thermal and air quality than regular users (i.e., professors and administrative staff). Therefore, the proposed model may help analyze and compare the level of satisfaction of different groups of occupants in relation to retrofits and/or maintenance actions.

### 3.7. CONCLUSIONS

The assessment of building comfort performance involves the analysis of multiple variables under uncertainty. It is difficult to use traditional methods to quantify and assess building comfort from such uncertain variables. Therefore, this paper presents the development of a novel BN model to manage the comfort performance of existing buildings. Unlike deterministic models, the proposed BN can model building comfort as a probabilistic process, providing levels of comfort performance using probability distributions. The main advantage of BN is that it can deal with uncertainty and is flexible enough to include data sources including empirical data, observation and expert evidence.

This model includes a comprehensive, structured, robust model for causal factors that affect building comfort. The capability of the proposed model is demonstrated by applying it to real buildings. The IEQ factor and space adequacy are key issues for the health and comfort of occupants in non-residential buildings. The results showed that

the BN model can estimate the building comfort level when the characteristics of the building and the environmental conditions are known. However, when evidence about the IEQ and space (gathered through the questionnaire survey) are included, the model also provides the most probable causes for dissatisfaction. Therefore, the proposed model helps facility managers to make informed decisions to enhance the comfort of buildings and consequently occupant satisfaction.

Knowledge about people's comfort priorities may be used as guidelines in the construction and renovation of buildings so that building occupants' satisfaction can be maximized. The high impact factors in the BN model were illustrated using a sensitivity analysis. Moreover, scenario analyses provided the capacity for deeper understanding of potential responses of the model, helping facility managers to optimize building operation strategies to increase building comfort performance. Besides using the model as a performance assessment tool, facility managers can create hypothetical scenarios and simulate outcomes before finalizing a renovation or retrofitting plan. This will provide the manager with quantitative and visual comparisons between options.

The results of this model can be complemented with assessments of the economic dimension. The proposed model can also be replicated in any geographic context and it can be easily adapted to other non-residential buildings. The model can also be used to conduct more rational management and maintenance of building stock. Buildings can be compared to prioritize those with the worst performance. Moreover, the use of the model can optimize government incentives for high quality and sustainable buildings. Performance levels could be used by the administration to propose mandatory performance evaluations of existing buildings and create incentives for highperformance buildings.

# Nomenclature 

BN - Bayesian network
CPTs - Conditional Probability Tables
D\&C - Design and Construction
DAG - Directed Acyclic Graph
FM - Facility Management
HVAC - Heating, Ventilation and Air Conditioning
IEQ - Indoor Environmental Quality
POE - Post-occupancy evaluation
TNormal - Truncated Normal distribution
WMEAN - Weighted mean function
WWR - Window-wall-ratio
