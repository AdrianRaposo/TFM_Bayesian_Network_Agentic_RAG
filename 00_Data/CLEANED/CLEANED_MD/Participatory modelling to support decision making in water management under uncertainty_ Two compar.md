# Participatory modelling to support decision making in water management under uncertainty: Two comparative case studies in the Guadiana river basin, Spain 

Gema Carmona , Consuelo Varela-Ortega , John Bromley

## A B S T R A C T

A participatory modelling process has been conducted in two areas of the Guadiana river (the upper and the middle sub-basins), in Spain, with the aim of providing support for decision making in the water management field. The area has a semi-arid climate where irrigated agriculture plays a key role in the economic development of the region and accounts for around $90 \%$ of water use. Following the guidelines of the European Water Framework Directive, we promote stakeholder involvement in water management with the aim to achieve an improved understanding of the water system and to encourage the exchange of knowledge and views between stakeholders in order to help building a shared vision of the system. At the same time, the resulting models, which integrate the different sectors and views, provide some insight of the impacts that different management options and possible future scenarios could have. The methodology is based on a Bayesian network combined with an economic model and, in the middle Guadiana sub-basin, with a crop model. The resulting integrated modelling framework is used to simulate possible water policy, market and climate scenarios to find out the impacts of those scenarios on farm income and on the environment. At the end of the modelling process, an evaluation questionnaire was filled by participants in both sub-basins. Results show that this type of processes are found very helpful by stakeholders to improve the system understanding, to understand each other's views and to reduce conflict when it exists. In addition, they found the model an extremely useful tool to support management. The graphical interface, the quantitative output and the explicit representation of uncertainty helped stakeholders to better understand the implications of the scenario tested. Finally, the combination of different types of models was also found very useful, as it allowed exploring in detail specific aspects of the water management problems.

## 1. Introduction

For management problems, especially in the field of natural resources, the current trend is to develop integrated policies that are sustainable in the long term and take into account all the factors related to resource use. To support this approach the European Union has developed the Water Framework Directive (WFD), which establishes general guidelines for water management in EU countries. This framework represents a new perspective on water
management, as it includes a shift from supply to demand management, an obligation to consider the cost-effectiveness of measures and the requirement to include stakeholders in the design of river-basin management plans. The WFD is based on the concept of Integrated Water Resources Management (IWRM), which was developed during the 1990s and was defined by the Global Water Partnership as "a process which promotes the co-ordinated development and management of water, land and related resources, in order to maximise the resultant economic and social welfare in an equitable manner without compromising the sustainability of vital ecosystems" (Global Water Partnership, 2000). There are other definitions of the concept, but all of them involve the need to consider the complexity of water systems, involving multiple factors and actors in multiple spatial and time scales, and the need to involve stakeholders in the resource management (Biswas, 2004; Pahl-Wostl, 2007; Rault and Jeffrey, 2008).

The WFD stresses the importance of stakeholder participation in decision making, being one of the main principles and a compulsory feature of water management in the European legal framework (De Stefano, 2010; European Commission, 2000; European Commission, 2003). Participation is understood as the involvement of members of the general public in policy-forming activities, by means of several mechanisms intentionally created for that purpose (Beierle and Cayford, 2002; Rowe and Frewer, 2004). Three major justifications for stakeholder involvement proposed in the literature (Johnson, 2009; Smith Korfmacher, 2001; Webler and Tuler, 2001) are:

- **Democratic rationale**: the public should be involved in decisions that affect them.
- **Substantive rationale**: citizens can provide scientists with their specialized knowledge, for better understanding of facts and values.
- **Pragmatic rationale**: an involved and educated public is more likely to support implementation of resulting policies.

These motivations form the basis of the WFD participatory requirements. First, stakeholder participation enables information to be shared by those holding different points of view and, as a result, helps build a common understanding of the system. In addition, stakeholder involvement in decision making improves public acceptance of water-management plans, which become more likely to be successful when stakeholders have participated in the design of those plans.

The design of the participatory process has to be carefully planned if the desired results are to be obtained. The process should ideally be iterative, taking into account perception of uncertainty and including a stage of group validation and verification (Johnson, 2009; Smith Korfmacher, 2001; Webler and Tuler, 2001).

This article describes the implementation of a participatory process developed as a tool to support decision making in water management. The process aims to achieve an improved understanding of the water system and to encourage the exchange of knowledge and views between stakeholders in order to help build a shared vision of the system. The process also identifies the impacts of different solutions to water-system problems in order to provide information regarding which solution a final decision should be based on. This research has been applied in the Guadiana river basin, which is located in the centre of the Iberian Peninsula and covers an area of 67,000 km². The area has a semi-arid climate, with high variable precipitation leading to irregular water recharge throughout the year. The Spanish part of the Guadiana basin (83% of the total) is divided into 3 sub-basins: the upper Guadiana (UG), the middle Guadiana (MG) and the lower Guadiana in Huelva Province. Our study focuses on the upper and middle sub-basins (see Fig. 1).

These two sub-basins sustain an economically important agricultural sector, which consumes large quantities of water. However, the two catchments draw most of their water supplies from different sources. In the UG groundwater provides the bulk of the supply, while in the MG surface water is the main source. The development of irrigation in the upper part of the basin has been accomplished through private initiatives, which produced highly efficient irrigation systems. However, over-exploitation of groundwater for irrigation in the upper part of the basin led to the depletion of aquifers, together with serious environmental deterioration and conflicts between water users (Llamas and Martínez-Santos, 2005). Management and control measures, such as water transfers from the Tagus river, the EU funded Agri-Environmental plan or the enforcement of legal restrictions in pumping volume and wells' drilling, have been costly but ineffective (Llamas et al., 2010). In contrast, the middle part of the basin has benefited from public plans for the development of irrigation; however, irrigation efficiency is low and large volumes of water are used. The modernization of irrigation systems and water governance is a major challenge for the area.

To define the various complexities and uncertainties in the area and provide the opportunity to involve stakeholders in the decision making process, a decision-support system based on Bayesian

![img-0.jpeg](img-0.jpeg)

Fig. 1. Location of the Guadiana Basin in Spain. Source: Adapted from CHG, 2010 CHG (Confederación Hidrográfica del Guadiana), 2010. URL: http://www.chguadiana.es/consultas/sigchgweb/SIGCHGWEB_pub.jsp. Last viewed: March 2011

networks (BNs) was selected. A particular strength of this approach is that it provides quantitative results to facilitate comparison of different alternatives.

## 2. Literature review

Stakeholder participation is especially important in the complex field of water-resources management, where physical and biological systems are combined with the multiple perspectives, needs, values and concerns associated with human use (Welp, 2001; Antunes et al., 2009). This entails the need for the development of participatory tools capable of overcoming complexity and uncertainty (Pahl-Wostl, 2007). In addition, successful participation of stakeholders in natural-resources management requires decisionmaking tools that are transparent and flexible (Henriksen and Barlebo, 2008). These tools should be designed to elicit knowledge from different stakeholder groups and operate as a platform to carry out the debate. At the same time, the selected methodology needs to support planning and decision making. These two objectives, namely social learning and support for decision making, are identified in the literature, and should be considered together, as the first aids the second (Lynam et al., 2010; Martínez-Santos et al., 2010; Simon and Etienne, 2010; Voinov and Bousquet, 2010).

Although the WFO highlights the need for public participation in the development of water-management plans, there is a lack of guidelines regarding support systems for making environmental decisions (Henriksen et al., 2007). In the literature we find participatory methods designed to achieve two objectives (Rowe and Frewer, 2000): to elicit input in the form of opinions (public opinion surveys, focus groups), and to elicit judgements and decisions that can be used to inform policy (consensus conferences, citizens' juries). When conflict resolution is a major issue, selected instruments will need to include (Wittmer et al., 2006) the capability to manage complexity and uncertainty, to produce decisions according to the rules in the specific context, include all relevant interests in the process, assure transparency, respect relationships, allow changes in behaviour and learning, and facilitate convergence, as well as the cost effectiveness of the process.

Decision-support systems are computer-based tools that can create and assess management alternatives, as well as facilitate knowledge communication between stakeholders. Some DSTs used for river-basin management in recent years include (Welp, 2001): scenario-simulation and modelling systems, expert systems which combine expert and local knowledge with a set of reasoning tools, GIS applications and databases, visualisation methods, role plays and gaming. DSTs can be used to: help reach a consensus about the main problems and possible strategies; elicit knowledge and including it in models; and to serve as a vehicle for communication, training and forecasting. At the same time, addressing watermanagement issues following the IWRM principles requires the use of integrated tools capable of taking into consideration the different aspects of water use. An interesting approach is the use of "formal methods" (mainly mathematical models) combined with stakeholder based approaches (Giordano et al., 2007). These are not mutually exclusive but complementary, and their application can help to obtain a better quality of decision than traditional approaches thanks to the integration of different perspectives and stakeholder expertise in those traditional formal methods.

That combination of formal methods with stakeholder based approaches can be done through participatory modelling, which is understood as a "process in which the formulation of a conceptual model and its formalisation is carried out by disciplinary experts with the direct involvement of stakeholders" (Jonsson, 2005; Sgobbi and Giupponi, 2007; Sheppard, 2005). In any event, but especially when dealing with computer models, participation from
the early stages helps understanding of the modelled system (Rowe and Frewer, 2000).

Voinov and Bousquet (2010) provide an overview of participatory modelling techniques, in which they describe the emergence of two parallel phenomena: the development of system-dynamics modelling and the trend to include participation requirements under different laws. Under the umbrella of participatory modelling methods, there are a number of different approaches:

1) Participatory Modelling (PM), as a generic term, referring to the inclusion of participation in traditional formal modelling, such as hydrologic or economic models (Langsdale et al., 2009; Martínez-Santos et al., 2008; Videira et al., 2010)
2) Group Model Building (Andersen et al., 1997, 2007; Richardson et al., 1997; Vennix, 1999), mainly based on the use of causal loop diagrams, where stakeholders collectively participate in building the dynamic model;
3) Mediated Modelling (Antunes et al., 2006; Van den Belt, 2004), also based on system dynamics but more focused on environmental applications; Companion Modelling (Becu et al., 2008; Bousquet et al., 2005; Campo et al., 2010; Simon and Etienne, 2010), which involves a combination of agent-based models and role-playing games and is based on the principles of transparency and adaptivity;
4) Participatory Simulation, also based on role-playing games and agent-based modelling, but where stakeholders only participate in simulations, not model building; Shared Vision Planning, which is mainly used in applied studies carried on by the US Army Corps of Engineers in relation to water management; Collaborative Learning, where stakeholders work together and learn from each other through information exchanges.

In practice, these approaches are implemented using different types of tools. The Annex shows a summary of the tools most commonly used in participatory modelling in the field of water and natural resources management, specifying some of the advantages and disadvantages of each tool. The most appropriate tool will depend on the specific context and objectives of the particular case in question.

Apart from the selection of the most suitable tool, the participatory process itself has to be carefully designed. A successful participatory modelling process should be kept flexible, so that it can build a common understanding, be open in temporal and spatial terms and represent changing environmental systems. Four principles should guide the approach: (a) a transparent modelling process; (b) a continuous and appropriately representative involvement; (c) a strong influence on modelling decisions; and (d) a clear role for modelling in watershed management (Johnson, 2009; Smith Korfmacher, 2001). These principles have guided the process held in the Guadiana river basin, where we have selected a participatory modelling approach using BNs.

## 3. Materials and methods

This paper describes the construction of two BNs for the Guadiana river basin: one for the upper and one for the middle subbasin. In our case we are facing complexity and uncertainties related to data that come from different sources. Special attention has been given to the representation of the agricultural sector: in particular, different types of farm were identified in order to illustrate the impact of management measures on each of the various types in the area.

The models have been built with the active involvement of the key stakeholders in both areas, following a feedback-based iterative process. The BNs worked as decision support tools, developed to

![img-1.jpeg](img-1.jpeg)

**Fig. 2.** Steps followed in the development of the BNs and similarities with the general framework for the construction of environmental models. Ten steps recommended by Jakeman et al. (2006) in the development and evaluation of environmental models: Steps in the development of a BN, according to Bromley (2005).

help select the best management options given the existing environmental and socio-economic constraints.

BNs are acyclic, directed graphs that represent a system through the main variables (nodes), the possible values they can adopt, and the relationships between variables in terms of conditional probabilities (Bromley, 2005; Cain, 2001). The mathematical basis of this type of model is Bayes' theorem, which is expressed as follows:

$$P(A_i/B) = \frac{P(B/A_i)P(A_i)}{\sum_{k=1}^{n} P(B/A_i)P(A_i)}$$

Based on this theorem, probability distributions of all variables are calculated given certain initial conditions. When new evidence is introduced, probabilities are updated in light of the new evidence.

The graphical design and calculations have been made using the Hugin commercial software (Hugin Expert A/S, 2008).

Although several types of model were built and provided input for the BNs, in this paper we focus solely on the BNs and on the participatory process required for the development of these BNs in both the upper and middle Guadiana sub-basins. BNs can deal with different types of variables and different types of data, which make them particularly appropriate in the Guadiana water management context (Batchelor and Cain, 1999; Bromley et al., 2005; Cain et al., 1999; Jensen and Nielsen, 2007). When complete, the model is able to simulate a wide range of different scenarios, which allows for quantitative assessment of the outcomes. But perhaps the main advantage of this tool is the explicit consideration of uncertainties through probabilities. When used as part of a participatory process, the need to discuss the representation of the system both in qualitative and quantitative terms can facilitate debate and promote openness and transparency (Zorrilla et al., 2009).

The processes held in the UG and in the MG began with a selection of relevant stakeholders, a series of stakeholder meetings and post-meeting work. For the definition of the steps in the process, we built on previous studies that focused on social-environmental system analysis (e.g. Kelkar et al., 2008; Walker et al., 2004), and in studies that had a more specific focus on environmental modelling (e.g. Refsgaard et al., 2007; Liu et al., 2008; Jakeman et al., 2006). In our case, the process was structured following the guidelines laid out by Bromley (2005), which consist of seven steps divided into a qualitative and a quantitative phase and can be considered as a specific example of Jakeman's approach (see Fig. 2).

As in Jakeman's design, and despite the linear nature of the process, the development of the BN has been implemented in an iterative way, returning to previous steps when stakeholders or researchers pointed out the need to review the previously defined structure or data.

Due to differences between the two sub-basins, a separate procedure was employed for each area. While in the upper part of the basin the main problems to be addressed were conflicts between stakeholder groups and uncertainties in the data, the MG was affected more by a lack of governance.

### 3.1. Model development in the UG sub-basin

In the UG basin, the participatory modelling process began in May 2007 and ended in November 2008. A series of earlier meetings had taken place between 2005 and 2007 in the context of the NeWater project,<sup>3</sup> where key stakeholders in the UG basin discussed the main aspects of water management in the region in a forum, the objective being to reduce conflict between stakeholder groups (Correa, 2007; Martínez-Santos et al., 2007).

These previous workshops helped to improve the relationships between stakeholders, whose initial approach at the NeWater project meetings was very hostile. Stakeholder selection for the BN participatory process was based on these previous meetings: the group included the planning group of the Guadiana RBA, the agriculture department of the Castilla la Mancha regional government, representatives of the main irrigation communities of the sub-basin, environmental conservation groups, researchers and academics.

Table 1 provides details of the number, dates, format and content of meetings.

The first step before the development of the model was the definition of a typology of farms. Based on that typology, an

<sup>3</sup> NeWater ("New Approaches to Adaptive Water Management under Uncertainty"), FP6-2003-GLOBAL-2-SUSTDEV-6.3.2-511179-2.

Table 1 Meetings held within the upper Guadiana participatory process.

b) Obtain missing data, and
c) Check if the states defined by the data collected were close to reality | 12 | Validation of the network and the states of variables. New data and sources of data | Modifying the BN structure according to interviews, collecting additional data and adding missing variable values, including results of the economic model. Starting CPTs.  |
b)Define the probabilities of the states of each variable | 11 | Validation of network structure. Expert inputs to set probability tables (CPT) | Modifying variable values according to results, completing CPTs using various sources, including economic model. Specific BN for each farm type. First round of simulations.  |

Source: Updated from Carmona et al. (2011), Zorrilla et al., (2009). individual BN was developed for each farm type. These individual BNs were similar, although they differed in some of the probability tables, and were aggregated afterwards using an object-oriented network approach, which allows for the representation of particular characteristics of the different farm types (Carmona et al., 2011; Dawid et al., 2007; Koller and Pfeffer, 1997; Molina et al., 2010). This is important for decision making, as we can simultaneously test the effects of the different water management strategies on the different farm types and on the common environment.

In order to capture the relationship between water use, yields and economic results for the farmers and agricultural activity, an economic non-linear mathematical model was used to represent the farmers' behaviour, capturing their response in terms of water use and selection of cropping patterns in response to different water-policy and climate scenarios (Carmona and Varela-Ortega, 2007; Carmona et al., 2009; Varela-Ortega et al., 2006).

Once the model was complete, a set of scenario simulations were carried out. In the UG sub-basin, some of the measures included in the new Special Plan for Regional Water Management (C.H.G., 2007) were tested, specifically: (1) the purchase of water rights from farmers by the Guadiana RBA (River Basin Authority), simulating different offer price levels; (2) several climate change scenarios; and (3) the increase of the enforcement capacity of the RBA to make farmers comply with water volume restrictions, taking into consideration various levels of compliance. Those measures were evaluated against economic and environmental variables (essentially, farm income and aquifer recovery).

### 3.2. Model development in the MG sub-basin

In the MG basin, the modelling process took place between May 2008 and February 2011, within the framework of the SCENES project. ${ }^{4}$ Selected stakeholders were contacted by phone

[^0]and e-mail. Although some of the invitees were also involved in the upper-Guadiana process, mainly those from the RBA, most of the participants were new to the forum. The group included the planning group of the Guadiana RBA, the agriculture department of the Extremadura regional government, representatives of the main irrigation communities of the sub-basin, environmental conservation groups, researchers and academics.

The number and organization of meetings was similar to those of the UG sub-basin, but in this case, previous to the development of the Bayesian network itself, two preliminary meetings were organised with the aim of eliciting the problem to be addressed and exploring the existing views of the MG system held by the different stakeholder groups.

Table 2 shows the details of the number, dates, format and content of meetings.

Like in the UG process, the same group of stakeholders were involved during the whole participatory process, but the list of attendees varied slightly for the different meetings. In this case, the end of the process coincided with an active period in the development of the river basin management plan. This drastically reduced stakeholders' attendance.

The methodology developed in the MG was similar to the framework described above for the UG, except that for the MG we added a new element: the crop model Aquacrop (Raes et al., 2009; Steduto et al., 2009), which was used to derive yield response to water functions and to climate change scenarios. The combination of the BN with the economic and crop models allowed us to carry out simulations with those models, capturing the detailed consequences of the different management options for the different farm types. Fig. 3 shows how the information has been linked between the different models.

Within the simulation scenarios chosen in the MG basin, we considered: (1) the change in environmental flow restrictions; (2) several climate change scenarios; and (3) the increase of the enforcement capacity of the RBA to make farmers comply with water volume restrictions, taking into consideration various levels of compliance. The indicators selected in the comparison of

[^0]: ${ }^{4}$ SCENES ("Water Scenarios for Europe and for the Neighbouring States"), FP6-2005-GLOBAL-4 (OJ 2005 C 177/15).


**Table 2**

Meetings held within the middle Guadiana participatory process.

scenario-simulation results were mainly farm income, employment, the environmental impact of hydraulic works and the good state of water bodies.

In both cases, the researchers conducted extensive studies between the two meetings, concentrating on two aspects: data collection and re-arrangement of the BN structure. The data collected was used to identify the states for each variable and to establish the conditional probability tables. A variety of sources was used, including statistical records, scientific reports, legal reports, field surveys and results from simulations with economic and crop models. In some cases, stakeholders were contacted by phone or by e-mail to exchange information regarding the data.

### 4. Results

Results are divided into two groups: first, we present the models obtained, and then we focus on the results of the participatory process.

#### 4.1. Modelling results

After the participatory modelling processes were carried out, a model was produced for each sub-basin representing the water system and very much focused on the agricultural water use. We present next a summary of the models built in the upper and in the middle Guadiana sub-basins.

#### 4.1.1. Upper Guadiana

Fig. 4 shows a summary of the BN representing the UG sub-basin.

We can see that the BN of the sub-basin accounts for 32 nodes. These are very much focused on the agricultural sector, with a significant group of policy-related variables. Stakeholders wanted to test the effects of a range of management actions represented as independent policy variables in the network (enforcement capacity, water quotas, price of water rights, closure of illegal wells, forestation and agrarian measures) against two variables selected as indicators: farm income and aquifer recovery. These variables represent the trade-off between the economy of the region and the state of the environment.

#### 4.1.2. Middle Guadiana

The BN built for the MG sub-basin is summarised in Fig. 5.

Compared to the UG model, that of the MG is more complex, with 47 nodes providing more detail on the different aspects of the water system. In this case, the agricultural system is thoroughly described and the policy elements are an important part of the model, while the environmental issues are more detailed than in the UG. In addition, other water uses, social elements and transboundary agreements are also represented here.

The differences in the BN of the two sub-basins can be explained in two ways:

- The water system in the UG is actually simpler, as it is reduced to a main aquifer with well-defined interactions. In contrast, the MG is based on surface water and has a more complex regulatory system and a higher number of interrelated elements.
- The problem in the UG is more clearly defined. In essence it consists of a depletion of the main aquifer and the conflict arising between the different stakeholder groups over this issue. In contrast, the MG presents a scenario of imperfect governance, where symptoms, causes and relationships are less clear.

![img-2.jpeg](img-2.jpeg)

**Fig. 3.** Methodological scheme of the research; linkage between models developed. BNs developed at farm scale.

![img-3.jpeg](img-3.jpeg)

Fig. 4. Summary of the BN representing the upper Guadiana system.

Some other differences identified in the two sub-basins, related to the conditions of each site, are highlighted in Table 3.

Most of the differences identified in the BNs are derived from the different water sources, which determine in turn the water management system. In the UG stakeholders provide fewer details about the out-farm variables, focussing to a great extent on water management inside the farm. The role of the water authority in this area is limited to the establishment of legal water allotments and to control the compliance of farmers with those limits, and the environmental problems are focused on the aquifer depletion. In contrast, the MG BN defines a more complex system, where out-farm variables acquire a higher weight. In this case, the water authority does not only control that farmers keep their water consumption below their legal allotments, but they are also responsible for water delivery among the different uses and irrigation communities. The environmental elements are also more developed here, where different problems threaten the compliance with the WFD, but there is not such a focused problem as in the UG sub-basin. In addition, water pricing is also expressed differently in the two sub-basins. In the MG, farmers pay higher tariffs for water, while in the UG water costs were restricted to the cost of pumping. That is the reason why water cost reveals an important variable in the system in the MG BN, while it did not appear in the UG BN.

Something common to both BNs is the perception of risks. Stakeholders identify two main sources of uncertainty: the market and the climate, which are present in both BNs affecting the economic results of farms.

Details of the results of the different scenario simulations are not provided in this paper. Rather, main objective is to report on the

![img-4.jpeg](img-4.jpeg)

Fig. 5. Summary of the BN representing the middle Guadiana system.

- Irrigation development through a private initiative
- High ecological value and protected natural sites
- High levels of competition between agriculture and environment
- Lack of transparency in data
- Significant conflicts between users
- Low compliance with water restrictions, high rate of illegal water use | - Irrigation from surface water
- More complex organisation of irrigation scheme
- Major role of irrigation communities in water distribution
- Big dams, high water-storage capacity
- Higher water allotments
- Perceived problem of ill-defined governance  |
- Lower consciousness of interactions between users, uses, areas, etc.
- Greater importance of farms as decision-making units in the water system
- Emphasis on the conflict-solving objective within the participatory process
- Inconsistency of data coming from different sources | - Higher interest in the macro level (basin/sub-basin)
- Higher consciousness of interactions between users, uses, areas, etc.
- Greater importance of the Water Authority as decision-making unit in the water system
- Emphasis on the decision-making-aid abilities of the modelling tool  |

**Table 3** Main differences found in the participatory process of the upper- and middle-Guadiana sub-basins.

usefulness of this approach in terms of stakeholder participation. An evaluation of the process is provided in the next sub-section.

### 4.2. Participatory process results

The participatory process was evaluated by using evaluation questionnaires completed by stakeholders and informal interviews with stakeholders.

The evaluation questionnaires were distributed at the final meeting in both sub-basins. The questionnaires, completed anonymously, covered a series of topics based on aspects considered to be important in the literature and related to the objectives set in our specific participatory processes. These objectives included: to contribute towards conflict-resolution, improve understanding of the system, enhance social learning, include stakeholder views in management and support decision making and other specific capabilities of the tool selected (Beierle, 1998; Beierle and Konisky, 2000; Lynam et al., 2007; Rowe and Frewer, 2000, 2004; Von Korff, 2006; Webler et al., 1995; Webler and Tuler, 2001).

The evaluation questionnaires were distributed in both sub-basins at the end of the participatory process. In the UG, they were answered by 15 stakeholders representing all key interest groups. For the MG, 7 stakeholders attended the final workshop; it was a much more focused meeting than the one for the UG and featured more technical discussion. Only the stakeholders involved throughout the process were invited to this final meeting. Fig. 6 shows the distribution of responses in terms of stakeholder groups for both the UG (Fig. 6a) and the MG (Fig. 6b).

Results of the evaluation for each of the two case studies are presented in the following sub-sections.

#### 4.2.1. Evaluation of the process in the UG sub-basin

In the UG sub-basin, questionnaires were distributed during a general meeting in which the results of the Bayesian networks were presented, together with other results from the NeWater project. More detailed results of this process can be found in Zorrilla et al. (2009); here we have taken a selection of those results, focusing on common elements with the MG process. Among other things, stakeholders were asked whether they perceived conflicts of interest at the beginning of the process, a question to which 90% of stakeholders answered "important conflicts", while 10% perceived "some conflicts".

Although the questionnaires for the evaluation of the BN participatory process included some open questions, for the most part it took the form of positive assertions about desired outcomes, with which stakeholders had to express their agreement or disagreement. The assertions included in the questionnaires referred to two aspects: the process itself and the performance of the BN as a participatory tool:

A. Regarding the process:

1. My interests/views have been included in the BN
2. The BN building process has been useful for me
3. The process has helped us understand one another's concerns
4. The process has helped improve my understanding of the basin's problems
5. The process has helped improve my understanding of the interrelationships between water-management factors
6. The process has helped to improve data transparency

B. Regarding the tool:

1. BNs are a good method for planning and management, as they include all interests
2. BNs have helped to focus discussions
3. BNs have been built to reproduce reality
4. Visual representation helps understand how the system functions

Fig. 7 provides the responses to the questionnaire in the UG sub-basin, showing the number of 'I agree', 'I disagree' responses and also the number of unanswered questions.

As we can see from this figure, stakeholders seem quite satisfied with the process. Among the outcomes of the participatory process the improvement of data transparency was the most appreciated (100% responded 'I agree' to the statement number 6), followed by

### a. EVALUATION OF BN IN UPPER GUADIANA: Participants by stakeholder group

![img-5.jpeg](img-5.jpeg)

![img-6.jpeg](img-6.jpeg)

**Fig. 6.** Distribution of responses to the evaluation questionnaires by stakeholder group, for the upper Guadiana (6a) and for the middle Guadiana (6b).

the inclusion of stakeholder views in the model (93%), then the usefulness of the process (87%) and improved understanding of the system (87%). In last place we have improved understanding of one another's concerns, with 73% positive responses to this outcome.

Regarding usefulness of BNs as a participatory tool, the lowest score is given to the credibility of the model outputs, as only half of the respondents believed that the model obtained reproduced reality. In contrast, 100% of respondents agreed on the benefits of BNs in supporting management and planning. The graphical interface was also very much appreciated by stakeholders (80% agreement and 13% disagreement with statement number 10), followed by the capacity of the tool to focus discussions (67% agreement and 13% disagreement with statement number 8).

Apart from the main set of questions analysed above, there were some open questions designed to find out stakeholders' motivations for participating in the modelling process and the extent to which their expectations had been met (e.g.: Which was your motivation to participate in the development of Bayesian networks in the upper Guadiana?; What outcomes did you expect from the process?; To what extent have your expectations be met?) Few participants answered these open questions, but it is interesting to note that most of the responses indicated considerable interest in the capabilities of the BNs to support decision making. Some of these expectations were based on the capacity of the model to provide quantitative output. In addition, the possible use of the model to investigate root causes of problems in the basin and possible solutions for local development were also mentioned.

An analysis of the type of responses by stakeholder group (Fig. 8) reveals that participants from the public administration were the most positive in their evaluations (higher number of 'I agree' answers), followed by water users in the number of 'I agree' responses, while the members of environmental conservation groups appeared to be the most critical with regard to the participatory modelling process.

This is true for both sub-basins, and it is probably due to the low weight that the environmental concerns have traditionally had in the past water management practices that, in the case of the UG sub-basin, has led to a fall in the water table that is compromising the sustainability of the water system. Although environmental objectives have now become a key element in the context of the WFD, environmentalists feel that tradition is making the shift in water management too slow and that farmers still are the most influential group in water negotiations. Their lower satisfaction with the process is maybe due to higher expectations about its direct contribution to practical management. Farmers, in contrast, feel very much identified with the models, which represent in detail the agricultural activity.

### 4.2.2. Evaluation of the process in the MG sub-basin

As for the UG, evaluation questionnaires were distributed during the final meeting of the participatory process and they were completed anonymously by stakeholders. Since we were trying to evaluate the process against the same criteria, the questions included in the questionnaires were the same for both sub-basins, thereby facilitating comparison.

The first question was related to the degree of conflict in the sub-basin, to which 70% answered that there was no conflict and 30% said there were few conflicts. This is one of the major differences in comparison with the UG case and one which has conditioned the outcomes for the whole process.

As in the UG questionnaires, most of the questions took the form of positive assertions to which stakeholders had to express their degree of agreement. Results are shown in Fig. 9 compared to the previous results, the degree of stakeholder satisfaction was higher for the MG.

Although the results of the evaluation of the process in the UG sub-basin were quite positive, we can conclude from results displayed in Fig. 9 that those results were even more positive in the MG (94% 'agree' and 2% 'disagree' responses, compared to 79% 'agree' and 13% 'disagree' responses in the UG). In this case, and as for the UG process, the lowest percentages were achieved by the capacity of the model to represent reality (57% 'agree' and 14% 'disagree' answers).

In the open questions, some of the stakeholders expressed their concerns about the accuracy of data introduced in the model. However, they found the process and the model extremely useful for exploring scenarios and management alternatives and for supporting decision making. Some of the open questions referred to the expectations of the stakeholders in the participatory process, and the answers showed a high degree of satisfaction with the outcomes. One of the aspects they seemed to be especially satisfied with concerned the ability to actively participate in the development of the model. At the end of the meeting, many of the participants showed interest in learning how to use the software and

![img-7.jpeg](img-7.jpeg)

**Fig. 7.** Results of the evaluation questionnaires in the upper Guadiana Basin.

![img-8.jpeg](img-8.jpeg)

![img-9.jpeg](img-9.jpeg)

**Fig. 8.** Types of responses per stakeholder group, in the upper Guadiana (8a) and in the middle Guadiana (8b).

inquired about the possibility of implementing the process in other Spanish river basins within the framework of the current process of developing new river basin management plans.

Finally, the high number of variables, probability tables and the resultant high number of calculations required to run the model meant that a certain amount of time was needed to make those calculations when a change in the values of probability tables was required. Although some attendees felt especially satisfied with the high number of variables included in the model, others felt frustrated by the difficulties of running certain types of simulations onsite.

Some other general comments came up during the meetings in the UG and in the MG processes that can be relevant in the evaluation of the participatory modelling process:

- Some stakeholders found the BN too complicated to be used and felt that additional training would be needed if they intended to go on using the tool.
- The graphical interface and the ability of the software to solve calculations in scenario testing were mentioned several times as remarkable characteristics of the BN methodology.
- Participants from the RBA showed a great interest in the possibility of updating the BNs obtained so as to be able to use them in the future, especially in the MG sub-basin, where the management problem seems to be less clearly defined and where many variables are interacting. They also showed interest in the extension of the study to other river basins.
- The combination of BNs with economic and crop models and the construction of an object-orientated BN structure capturing the differences between farm types was also of particular interest to stakeholders.

### 5. Discussion

The current trend in natural resources management, and specifically in water management, calls for an integrated approach in which all sectors are considered, social and environmental sustainability are safeguarded and stakeholders are able to actively participate in the management process. To that end, considerable effort has been made in recent years to develop integrated participative tools to support decision making. Among the possible approaches, participative modelling can help implement IWRM requirements, given its proven capacity to integrate different types of knowledge and disciplines.

Our research was based on the development of two participatory models using Bayesian networks to support decision making in the field of water management in the UG and MG sub-basins in Spain. Despite being in the same river basin, the two sites display very different characteristics, both in terms of the physical environment and participation needs. The same methodology was

![img-10.jpeg](img-10.jpeg)

**Fig. 9.** Results of the evaluation questionnaires in the middle Guadiana Basin.

applied to these two different contexts, where participation was expected to yield different outcomes.

As other authors have confirmed (Lynam et al., 2002; Sgobbi and Giupponi, 2007), we showed that in a participatory modelling exercise the process is more important than the specific modelling outputs. According to the evaluation results, discussions improved the participants' understanding of the system and their ability to understand one another's views, which constitutes a remarkable outcome especially when conflict resolution is among the objectives of the process (Cain et al., 2003; Henriksen and Barlebo, 2008). Besides, the discussions have had other benefits: the debate over the data accuracy contributed to transparency, which stakeholders considered to be even more useful than the figures provided as a result of the simulations. This was seen more clearly in the UG subbasin, where information from different sources did not match and there was an evident lack of transparency in the data. Accuracy of data made the discussions longer, but brought an additional benefit of the process compared to the MG process.

When designing our modelling exercise we tried to keep the criteria for representativeness and early involvement, which are considered by many authors to be important requirements for the success of a participatory process (Reed, 2008; Rowe and Frewer, 2000; Webler et al., 1995). These two characteristics allowed for the inclusion of stakeholder values in decision making, which is considered to be a desirable feature of the participatory process when it is also aimed at helping management decision making (Bacon et al., 2002; Lynam et al., 2007). In our case, this characteristic was evaluated positively by stakeholders, and its inclusion was made possible thanks to the involvement of stakeholders other than policy makers.

Comparing the upper and the middle Guadiana cases, the process achieved different outcomes in terms of participation. While in the UG sub-basin conflict resolution and the uncertainty of information were the main issues, in the MG an improved understanding of the interrelations between variables in the water system and the possible effects of future market and climate scenarios were more important issues. The results of the participatory process were related to these main problems, confirming other authors' findings about the flexibility of BNs (Cain, 2001).

The graphical interface was shown to be useful by many studies (Cain et al., 2003; Henriksen and Barlebo, 2008; Kragt et al., 2011) and confirmed in our case, according to the stakeholder evaluations. The numerical output was highly appreciated as well, as it facilitated comparison of different scenarios. Moreover, the numerical data made uncertainties evident during discussions and triggered efforts to achieve information transparency, which is another positive outcome reflected in the evaluation results.

One drawback of BNs relates to the construction of the conditional probability tables, which is sometimes difficult, tedious and occasionally complicated by an inability to find appropriate data relating to all linked variables. But one positive feature is the possibility of investigating qualitative relationships with stakeholders and then allowing researchers to translate them into probabilities.

In areas similar to our case studies, where irrigated agriculture is the main economic activity, the ability to combine the BNs with other models that can account for details on agricultural variables is remarkable. Moreover, if the model is designed using an objectorientated approach, it allows for the representation of a typology of farms and makes it possible to capture the results of scenario simulations simultaneously on the different farm types. This possibility of differentiating results by farm type is an important feature when decision making intends to include social criteria and when those farm types are behaving very differently and exerting diverse influences on the whole system.

Some practical lessons we can draw about the implementation of the participatory process include the importance of selecting a representative group of stakeholders and building a good relationship with them. Despite their interest in the process and in the models being developed, it is sometimes difficult to keep the number of participants along time, especially when dealing with busy policy makers. Special attention should be given to selecting the right calendar and timing, which should include enough time for debate and for stakeholders to understand and participate in the model development, but not too much to avoid their involvement.

## 6. Conclusions

Based on the results obtained, we can conclude that, when a participatory modelling process is held with the aim of finding problems, identifying possible solutions and supporting planning and management, the process that leads to the creation of the model is more useful than the model itself. However, when the model selected is capable of providing numerical output it is valued positively by stakeholders, as it can help to directly compare alternative management actions and decision outcomes.

Regarding the models obtained in the participatory modelling exercise, their complexity depends not only on the complexity of the system itself, but also on the clarity of the problem we are dealing with. The existence of a well-defined, specific problem allows for the simplification of reality, which can be reduced to the key factors involved in the problem. In contrast, when the problems are not well defined it is difficult to discard irrelevant variables, which leads to a more complex representation of the system.

We found that the development of BNs helps highlight uncertainties, which are made evident during the construction of the conditional probability tables associated with the system's variables. This characteristic makes BNs more appropriate than other participatory modelling tools when uncertainties are an issue in the participatory process. We could also confirm the flexibility of BNs: once the main issues are defined (conflict solving, uncertainty analysis, etc.), the modelling process can be adapted to those particular issues, and this characteristic makes it appropriate for any kind of context.

Although integrated models are claimed to be the most appropriate type in the IWRM approach, when a specific sector prevails over other water uses the combination of such integrated models with other classical models can provide a deeper insight into the effects of water-management actions on that specific sector. This combination of models was very useful in our case studies, where an economic model and a crop model provided details on the agricultural sector.

Finally, within the BN models, the object-orientated approach proved to be useful when a group of elements of the same type were interacting within the same system. In our case, different farm types were represented, which made it possible to compare the effects of management actions on every farm type: an interesting ability when social criteria are influencing decisions.

## Acknowledgements

The authors would like to acknowledge the European Commission, which funded this research through the NeWater project ("New Approaches to Adaptive Water Management under Uncertainty"), FP6-2003-GLOBAL-2-SUSTDEV-6.3.2-511179-2, DG Research. European Commission and the SCENES project ("Water Scenarios for Europe and for the Neighbouring States"), FP6-2005-GLOBAL-4(OJ 2005 C 177/15). Special acknowledgement is also due to the Universidad Politécnica de Madrid for co-funding this research.

Annex: Review of participatory modelling tools used in the field of water and natural resources management.

