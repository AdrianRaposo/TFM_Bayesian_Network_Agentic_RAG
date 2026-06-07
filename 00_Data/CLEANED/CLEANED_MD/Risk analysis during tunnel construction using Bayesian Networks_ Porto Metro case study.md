# MIT <br> Libraries 

## DSpace@MIT

## MIT Open Access Articles

## Risk analysis during tunnel construction using Bayesian Networks: Porto Metro case study

The MIT Faculty has made this article openly available. Please share how this access benefits you. Your story matters.

Citation: Sousa, Rita L., and Herbert H. Einstein. "Risk Analysis During Tunnel Construction Using Bayesian Networks: Porto Metro Case Study." Tunnelling and Underground Space Technology 27, no. 1 (January 2012): 86-100.

As Published: http://dx.doi.org/10.1016/j.tust.2011.07.003
Publisher: Elsevier
Persistent URL: http://hdl.handle.net/1721.1/101601
Version: Author's final manuscript: final author's manuscript post peer review, without publisher's formatting or copy editing

Terms of use: Creative Commons Attribution-NonCommercial-NoDerivs License

# Risk Analysis during Tunnel Construction Using Bayesian Networks: Porto Metro Case Study 

Rita L Sousa a, Herbert H. Einstein a<br>a Massachusetts Institute of Technology, Cambridge, USA

Corresponding Author: Herbert H. Einstein
Email address: einstein@mit.edu
Phone: +16172533598
Fax: +16172536044
Address: 70 Massachusetts Ave, Room 1-342, Cambridge MA 02139


#### Abstract

This paper presents a methodology to systematically assess and manage the risks associated with tunnel construction. The methodology consists of combining a geologic prediction model that allows one to predict geology ahead of the tunnel construction, with a construction strategy decision model that allows one to choose amongst different construction strategies the one that leads to minimum risk. This model used tunnel boring machine performance data to relate to and predict geology. Both models are based on Bayesian networks because of their ability to combine domain knowledge with data, encode dependencies among variables, and their ability to learn causal relationships. The combined geologic prediction - construction strategy decision model was applied to a case, the Porto Metro, in Portugal. The results of the geologic prediction model were in good agreement with the observed geology, and the results of the construction strategy decision support model were in good agreement with the construction methods used. Very significant is the ability of the model to predict changes in geology and consequently required changes in construction strategy. This risk assessment methodology provides a powerful tool with which planners and engineers can systematically assess and mitigate the inherent risks associated with tunnel construction.


Keywords: Risk, Tunneling, Bayesian Networks

## 1. Introduction

There is an intrinsic risk associated with tunnel construction because of the limited a priori knowledge of the existing subsurface conditions. Although the majority of tunnel construction projects have been completed safely there have been several incidents in various tunneling projects that have resulted in delays, cost overruns, and in a few cases more significant consequences such as injury, and loss of life. It is therefore important to systematically assess and manage the risks associated with tunnel construction. A detailed database of accidents that occurred during tunnel construction was created by Sousa (2010). The database contains 204 cases all around the world with different construction methods and different types of accidents. The accident cases were obtained from the technical literature, newspapers and correspondence with experts in the tunneling domain.

Knowledge representation systems (or knowledge based systems) and decision analysis techniques were both developed to facilitate and improve the decision making process. Knowledge representation systems use various computational techniques of AI (artificial intelligence) for representation of human

knowledge and inference. Decision Analysis uses decision theory principles supplemented by judgment psychology (Henrion, 1991). Both emerged from research done in the 1940's regarding development of techniques for problem solving and decision making. John von Neumann and Oscar Morgensten, who introduced game theory in "Games and Economic Behavior" (1944), had a tremendous impact on research in decision theory.

Although the two fields have common roots, since then they have taken different paths. More recently there has been a resurgence of interest by many AI researchers in the application of probability theory, decision theory and analysis to several problems in AI, resulting in the development of Bayesian Networks and Influence Diagrams, an extension of Bayesian Networks designed to include decision variables and utilities. The 1960s saw the emergence of decision analysis with the use of subjective expected utility and Bayesian statistics. Howard Raiffa, Robert Schlaifer, and John Pratt at Harvard, and Ronald Howard at Stanford emerged as leaders in these areas. For instance Raiffa and Schlaifer's Applied Statistical Decision Theory (1961) provided a detailed mathematical treatment of decision analysis focusing primarily on Bayesian statistical models. Pratt and al. (1964) developed basic decision analysis. while Eskesen (2004) and Hartford and Baecher (2004) provide good summaries on the different techniques (fault trees, decision trees, etc) that can be used to assess and manage risk in tunneling.

Various commercial and research software for risk analysis during tunnel construction have been developed over the years, the most important of which is the DAT (Decision Aids for Tunneling), developed at MIT in collaboration with EPFL (Ecole Polytechnique Fédérale de Lausanne). The DAT are based on an interactive program that uses probabilistic modeling of the construction process to analyze the effects of geotechnical uncertainties and construction uncertainties on construction costs and time. (Dudt et al., 2000; Einstein, 2002) However, the majority of existing risk analysis systems, including the DAT, deal only with the effects of random ("common") geological and construction uncertainties on time and cost of construction. There are other sources of risks, not considered in these systems, which are related to specific geotechnical scenarios that can have substantial consequences on the tunnel process, even if their probability of occurrence is low.

This paper attempts to address the issue of specific geotechnical risk by first developing a methodology that allows one to identify major sources of geotechnical risks, even those with low probability, in the context of a particular project and then performing a quantitative risk analysis to identify the "optimal" construction strategies, where "optimal" refers to minimum risk. For that purpose a decision support system framework for determining the "optimal" (minimum risk) construction method for a given tunnel alignment was developed. The decision support system consists of two models: a geologic prediction model, and a construction strategy decision model. Both models are based on the Bayesian Network technique, and when combined allow one to determine the 'optimal' tunnel construction strategies. The decision model contains an updating component, by including information from the excavated tunnel sections. This system was implemented in a real tunnel project, the Porto Metro in Portugal.

# 2. Background on Bayesian Networks 

Bayesian Networks are graphical representations of knowledge for reasoning under uncertainty. They can be used at any stage of a risk analysis, and may substitute both fault trees and event trees in logical tree analysis. While common cause or more general dependency phenomena pose significant complications in classical fault tree analysis, this is not the case with Bayesian networks. They are in fact designed to facilitate the modeling of such dependencies. Because of what has been stated, Bayesian networks provide a good tool for decision analysis, including prior analysis, posterior analysis and pre-posterior analysis. Furthermore, they can be extended to influence diagrams, including decision and utility nodes in order to explicitly model a decision problem.

A Bayesian Network is a concise graphical representation of the joint probability of the domain that is being represented by the random variables, consisting of (Russel and Norvig, 2003):

- A set of random variables that make up the nodes of the network.
- A set of directed links between nodes. (These links reflect cause-effect relations within the domain.)
- Each variable has a finite set of mutually exclusive states.
- The variables together with the directed links form a directed acyclic graph (DAG).
- Attached to each random variable A with parents B1, . . . , Bn there is a conditional probability table $P\left(A=a \mid B_{1}=b_{1}, \ldots ., B_{n}=b_{n}\right)$, except for the variables in the root nodes. The root nodes have prior probabilities.

Figure 1 is an illustration of a simple Bayesian network. The arrows (directed links) going from one variable to another reflect the relations between variables. In this example the arrow from C to B2 means that C has a direct influence on B 2 .
![img-0.jpeg](img-0.jpeg)

Figure 1 Bayesian Network example
Specifically, a Bayesian Network is a compact and graphical representation of a joint distribution, based on some simplifying assumptions that some variables are conditionally independent of others. As a result the joint probability of a Bayesian network over the variables $\mathrm{U}=\left\{\mathrm{X}_{1}, \ldots, \mathrm{X}_{\mathrm{n}}\right\}$, represented by the chain rule can be simplified from:
$P(U)=\prod_{i}^{n} P\left(X_{i} \mid x_{1}, \ldots \ldots, x_{i-1}\right)$
to
$P(U)=\prod^{n} P\left(X_{i}=x_{i} \mid\right.$ parents $\left.\left(X_{i}\right)\right)$, where "parents $\left(\mathrm{X}_{\mathrm{i}}\right)$ " is the parent set of $\mathrm{X}_{\mathrm{i}}$.
It is this property that makes Bayesian Networks a very powerful tool for representing domains under uncertainty, allowing one to store and compute the joint and marginal distributions more efficiently.

In order to obtain results from Bayesian Networks one does inference. This consists of computing answers to queries made to the Bayesian network. The two most common types of queries are:

- A Priori probability distribution of a variable

$$
P(\boldsymbol{A})=\sum_{X_{1}} \ldots \sum_{X_{k}} P\left(X_{1}, \ldots, X_{k}, \boldsymbol{A}\right)
$$

Where A is the query-variable and $\mathrm{X}_{1}$ to $\mathrm{X}_{\mathrm{k}}$ are the remaining variables of the network. This type of query can be used during the design phase of a tunnel for example to assess the probability of failure under design conditions (geology, hydrology, etc).

- Posterior distribution of variables given evidence (observations)

$$
P(A \mid \boldsymbol{e})=\frac{P(A, \boldsymbol{e})}{\sum_{X_{1}} \cdots \sum_{X_{k}} \sum_{A} P\left(X_{1}, \ldots, X_{k}, \boldsymbol{A}, \boldsymbol{e}\right)}
$$

Where $\mathbf{e}$ is the vector of all the evidence, and A is the query variable and $\mathrm{X}_{1}$ to $\mathrm{X}_{\mathrm{k}}$ are the remaining variables of the network. This type of query is used to update the knowledge of the state of a variable (or variables) when other variables (the evidence variables) are observed. It could be used, for example, to update the probability of failure of a tunnel, after construction has started and new information regarding the geology crossed becomes known.

The most straightforward way to do inference in a Bayesian Network, if efficiency were not an issue, would be to use the equations above to compute the probability of every combination of values and then marginalize out the ones one needed to get a result. This is the simplest but the least efficient way to do inference. There are several algorithms for efficient inference in Bayesian Networks, and they can be grouped as follows: Exact inference methods and approximate inference methods. The most common exact inference method is the Variable Elimination algorithm (Jensen, 2001) that consists of eliminating (by integration or summation) the non-query, non-observed variables one by one by summing over their product. This approach, which was used in this paper, takes into account and exploits the independence relationships between variables of the network.

# 3. Decision Support System 

The emphasis of this work is on the construction phase where the construction strategy decision model is used in combination with the (Bayesian) geological prediction model. The geological prediction model allows one to predict ahead of the tunnel face, and based on this, it is then possible to decide on the optimal construction strategy for the "updated" geologies.

The basic structure of the Geologic Prediction Model is presented in Figure 2. The X variables represent construction related variables that will give some information regarding the ground that the tunnel is crossing. GC is the ground condition at the face of the tunnel. One observes, for example, at section 1 and predicts the geology ahead of the face, for sections 2 to N .
![img-1.jpeg](img-1.jpeg)

Figure 2 Basic structure of the Geologic Prediction Model
(X: construction related variables; GC (Si): ground class at section i)
The construction strategy decision model is based on decision graphs, which are Bayesian networks extended to model different actions or alternatives and associated utilities. The model determines the optimal or "best" alternatives based on maximization of utility (minimization of risk). Since decision analysis is a well established field, a simple decision analysis model was used for methodology illustration purposes; other decision models could be used instead.

The basic structure for the construction strategy decision model (Figure 3) consists of:

- Two chance nodes, namely Geological Condition, which represents the possible ground conditions at the face of the tunnel, and Failure Mode, which represents the probability of different failure modes.
- One decision node, Construction Strategy, which represents the possible construction strategies.
- One utility node, the total cost, which represents the sum of costs associated with the different construction strategies and the utilities associated with failure.
![img-2.jpeg](img-2.jpeg)

Figure 3 Basic structure of the Decision Model

The Combined Geology Prediction Model and Construction Decision Model works as follows: One observes construction in section 1 and predicts the geology ahead of the face based on those observations using the Geology Prediction Model. Then the results of the geology prediction model are used in the construction strategy decision model to determine the optimal or best alternatives based on maximization of utility (minimization of risk). As the tunnel construction progresses these same steps are repeated. This can be seen in Figure 4.

![img-3.jpeg](img-3.jpeg)

Figure 4 Combined Geology Prediction Model and Construction Decision model
*The output of geological prediction model (GC) is an input of the construction strategy model

The decision support system described above was applied in a detailed real case study, the Porto Metro, presented next.

# 4. Porto Metro Case Study 

### 4.1 The project

The first phase of Porto Light Metro Project consisted of 4 lines (Figure 5), with an overall length of about 70 km . The Project has two lines (Line C and Line S) that included tunnels that run beneath the center of the city. The Line C tunnel is 2.3 km long and the Line S tunnel is 3.7 km long. The average overburden thickness ranges from $15-30 \mathrm{~m}$, with a minimum value of $3-4 \mathrm{~m}$ occurring in Line C tunnel. The tunnels were excavated by earth pressure balance shields (EPB-shields), which were capable of both closed and open mode excavation in mixed face conditions. Tunneling started with the Line C, from Campanhã to Trindade, in June 2000. The driving stopped in December 2000 as a consequence of a major incident after about 470 m . Work resumed in September 2001 and the Line C tunnel was completed in October 2002. In June 2002 a second EPB machine began the 2.7 km long Line S tunnel, from Salgueiros to São Bento, which was completed in October 2003. After Line C tunnel completion, the first TBM was

disassembled and reassembled to restart in February 2003 on the remaining 1.0 km of Line S, which was completed in November 2003 (Babendererde et al., 2005).
![img-4.jpeg](img-4.jpeg)

Figure 5 Porto Metro network - First phase (Babendererde et al., 2005)
The main geologic formation crossed by the Porto metro tunnels is the Granitic Formation (Porto Granite). It is a deeply weathered formation, especially in faults and joints, resulting in a very irregular profile. Alteration grades range from residual soil (W6) to fresh granite (W1); As a result of the highly variable weathering grade, there are large variations in density, permeability and other geotechnical parameters. A particular feature associated with the local conditions of the Porto area is the frequent occurrence of wells connected by drainage galleries that, in the past, ensured the population's water supply. These wells are not well charted.

The methodology described previously was applied to line C tunnel (Figure 6 and Figure 7) of the Porto Metro. This tunnel was excavated by an 8.7 m Herrenknecht Earth Pressure Balance Machine. This machine can advance in different modes: i) open: operation of the machine without any active face support; ii) closed: work chamber is completely filled with excavated pressurized material; iii) semiclosed: work chamber is only partially filled with muck and compressed air is used to support the empty part of the chamber to prevent local instability of the face.

![img-5.jpeg](img-5.jpeg)

**Figure 6** Line C Tunnel layout (adapted from Transmetro, 1999)

![img-6.jpeg](img-6.jpeg)

Figure 7 Longitudinal Profile of Line C tunnel (adapted from Transmetro 1999)
The designer considered seven geomechanical groups of homogeneous conditions in terms of weathering. These design geomechanical groups and associated conditions are presented in Table 1. The geomechanical groups g 1 to g 4 are rock like materials g 5 to g 6 are soil like materials, saprolite and residual soil. g7 is manmade material and alluvial soils.

Table 1 Geomechanical groups and associated conditions (Russo et al., 2001)


Notes: ${ }^{(1)}$ based on ISRM (1981), the classes correspond to the following (in cm) discontinuity spacing ranges: f1:>200, f2:60-200, f3:20-60, f4:6-20, f5:6; ${ }^{(2)}$ classes of subsurface conditions for "GSI-Based geomechanical groups "; ${ }^{15} \mathrm{~g} 7$ corresponds to manmade material and alluvial soils.

Three accidents occurred during the excavation of the first 300 m of line C tunnel. The first accident happened on 30 September 2000, when the EPBM had advanced 120 m from the beginning of construction as it intercepted a former well resulting in the discharge of its water. The overburden in this area was 12 m . The ground collapsed below two buildings causing damage to the structures. The settlement at the surface was about 2.5 m , within an area of approximately $40 \mathrm{~m}^{2}$.

The second accident (Figure 8) happened on 22 December 2000 when, after the passage of the TBM cracks were observed in the walls of a building followed by $250 \mathrm{~m}^{3}$ of subsidence of the back gardens (over-excavation during installation of rings 318, station $0+606.51$, and 327, station

$0+619.15$ ). The tunnel depth was about 26 m . This accident is located a couple of meters just before the TBM stopped.

The third and last accident (12 January 2001) occurred under houses 182 and 183 (see Figure 8), under approximately rings number 297 to 301 (station $0+570.99$ to station $0+576.60$ ). A building fell into the $8 \mathrm{mx} 8 \mathrm{mx} 6 \mathrm{~m}$ crater resulting in the death of a person. The overburden was of about 25 m . The TBM had passed under these houses on the 16 to 18th of December 2000, and it was stopped 50 m ahead of the 3rd accident location since 28 December 2000. This stoppage was due excessive settlement at the surface and to fill a cavity of around 15 m 3 due to over-excavation (2nd accident). In the period between 28 December 2000 and 12 January 2001 (when the third accident occurred) consolidation works from the tunnel and the surface were executed. In addition, the ground below Building n. 183 was injected through 5 inclined boreholes from the surface. These injection holes had been decided upon after it was realized that the machine had over-excavated when driving underneath this building (Transmetro/Geodata, 2001). The consolidation works underneath building n. 183 were concluded on 29 December 2000. Figure 8 shows the location of the second and third accidents, while Figure 9 shows a longitudinal crossection and the predicted geology.
![img-7.jpeg](img-7.jpeg)

Figure 8 Location of the $2^{\text {nd }}$ and $3^{\text {rd }}$ accidents of Line C tunnel (adapted from Transmetro/Geodata, 2001)

![img-8.jpeg](img-8.jpeg)

Figure 9 Predicted Geology in the 3rd accident zone: design Phase (adapted from Transmetro/Geodata, 2001)

# 4.2 Reported causes 

The Official accident commission's report (Porto Metro Accident Commission, 2001) determined that the causes of the $3^{\text {rd }}$ accident were:
i) Deficient design, which did not include continuous analysis of the crossed geology and adjustment of the excavation to the encountered conditions; ii) Insufficient geological characterization of the ground due to the lack of boreholes from the surface and the lack of boreholes from the machine's face that were required in the design but where never done; iii) No prompt analysis of the monitoring results; iv) Deficient supervision of the work and communication between the different teams.

## 4. 3 Risk Analysis Methodology

The decision support framework described previously was applied to the Porto Metro case. Recall that the decision support framework consists of two models: a geology prediction model and a construction strategy decision model (Figure 10). During the design phase the geology prediction is a simple model only based on the results of the existing geological survey and geological profiles. During the construction phase the geologic prediction model is a Bayesian network prediction model that allows one to predict the geology ahead of a tunnel machine based on observations of various machine parameters, during construction. Note that this is the geological prediction model as used in the Porto Metro Case presented here. Other types of observations may be used in the model. The construction strategy decision model, common to the design and the construction phases, is a Bayesian network based model that allows one to decide on the

optimal construction strategy for a given the geology. When combined the models allow one to asses risks during tunnel construction.
![img-9.jpeg](img-9.jpeg)

Figure 10 Decision support framework

# 4.4 Geology Prediction Model 

The model makes use of information that becomes available during construction to update the geologic predictions ahead of the machine. The ultimate aim of the model is to act as a decision aid for assessing and mitigating risk. If one knows the geology ahead of the face, then one can prepare for any risks, and chose optimal construction methods as was described previously. Prior to developing the model, it is necessary to chose parameters that are important in distinguishing between geologies. These are the parameters that the model will be based on, and that are observed during construction. Hence, an extensive analysis of the TBM data from the Porto Metro case is performed in order to find which parameters are important in distinguishing between geologies. The inter-relationships between parameters are also analyzed. The important parameters and the important inter-relationships are then retained in the model to develop its structure. Once the structure of the model is chosen, the model is applied to the Porto Metro Case. A portion of the dataset is used to 'learn' the model. The model is then used to predict the geologies ahead of the EPB machine and the results are then compared to the actual geologies encountered.

## 4. 5 Machine Data Analysis

The EPBM used in the line C tunnel, registers automatically every 10 seconds several operation related parameters. The ones considered in this study are presented below:

- Weight of excavated material (ton): The extracted material is weighed by scales located in the conveyor belt.
- Penetration rate (mm/rev): The rate at which the machine penetrates the ground, measured in mm per revolution
- Torque of the cutting wheel (MNm): Twist force applied to the cutting wheel.

- Total Thrust (KN): Corresponds to the total force applied by the thrust cylinders (or jacks) required to push the shield forward. The last segmental lining ring built inside the shield tail serves as abutment for the thrust cylinders.
- Cutting wheel Force (KN): Force that is transmitted onto the cutting wheel.

Based on the project information, mainly on the geological interpretative profiles (Transmetro, 1999), eight possible ground scenarios (Figure 11) along the tunnel were determined. For simplifying purposes only the face conditions will be considered in the definition of ground classes. For this reason the geological conditions of Porto Metro Line C tunnel were simplified to soil (G1), mixed (G2) and rock (G3). Soil (G1) corresponds to ground scenarios 1 and 2, i.e. the face of the tunnel is completely in the soil formation (geomechanical groups g5 and g6 in Table 1). Rock (G3) corresponds to ground scenarios 7 and 8, i.e. the face of the tunnel is completely in the rock formation (geomechanical groups g2, g3 and g4 in Table 1). Mixed (G2) corresponds to ground scenarios 3 to 6 , i.e. the face of the tunnel is in a mixed formation, a combination of Soil (G1) and Rock (G3). The ground scenarios are mainly based on the face conditions since this is the only information that was completely recorded through face mapping.
![img-10.jpeg](img-10.jpeg)

Figure 11 Geological scenarios along Line C tunnel

The machine parameter data corresponding to the section of the tunnel from ring 336, station $0+631$, to ring 1611 , station $2+418$ (i.e. the section beyond the location where the machine was stopped due to the last collapse) were analyzed. This was done to develop the model in a section where the "predicted conditions" could be compared to the encountered conditions.

Emphasis was placed on choosing the machine parameters that best distinguish between geological conditions. For this a single parameter analysis is first done. This consists of determining the mean values, standard deviations and relative frequencies of the parameters. The relative frequencies for different geologies are compared (Figure 12). If there are significant differences then the parameter is considered to be good at distinguishing between geologies. A two-parameter analysis followed in order to determine which inter-relationships between these parameters are important in distinguishing geologies (Figure 13). This consists of finding the relative frequency of two parameters at a time, for different geological conditions. The joint relative frequencies of two parameters for different geologies are compared. Again, if there is a significant difference between joint relative frequencies for different geological conditions then

the relationship between the two parameters is important when distinguishing between geologies; consequently the parameters and inter-relationships of importance were retained in the model.
![img-11.jpeg](img-11.jpeg)

Figure 12 Parameter Selection (distinguishing between ground classes). Single parameter analysis

![img-12.jpeg](img-12.jpeg)

Figure 13 Parameter Selection. Two parameter analysis.
Note: all relationships between variables that are presented in Figure 13 are considered important
The discrimination between "important" and "not important" parameters (and relationships) was based on the analyses of the relative frequencies, mean values and standard deviations and sensitivity analysis. First we looked at the relative frequencies (mean values and standard deviations) and consider that the important parameters were those that allowed one to distinguish between classes, i.e. those for which the relative frequencies had noticeably different distributions among the different ground classes. This analysis included also looking at the mean and standard deviation of each parameter for the different classes. We did not consider threshold values,

however. The decision was mostly based on the direct observation of the graph (i.e. engineering judgment). The parameters considered important were retained in the model, specifically the single parameter analysis in Figure 12 shows that Penetration rate (P) and cutting wheel force (CF) are important parameters when distinguishing between ground conditions, while torque of the cutting wheel (TO) and Total Thrust (TT) are less important. Although torque (TO) by itself is not important to distinguish between ground conditions, the relation between torque, cutting wheel force and penetration is extremely important. This can be seen in Figure 13b) and c). In addition, the ratio between some machine parameters was considered as one variable and found to be important when distinguishing between geologies. This is the case for torque of the cutting wheel over the cutting wheel force (TOC) (Figure 12). This ratio is important in all geologies but it becomes more important as the geological conditions are closer to rock conditions. Another parameter ratio that proved to be important when identifying ground conditions is the cutting wheel force over total thrust (COTT) (Figure 12). The total thrust is the force that is applied by the thrust cylinders (or jacks). Only a portion of this force will reach the cutting wheel, the remainder is needed to overcome the friction of the ground around the shield. In soil COTT is lower than in rock since a larger portion of the total thrust is lost by friction around the shield, due to the fact that soil formations are more deformable than rock.

Some other interesting results follow from this study. Penetration rates are lower in rock than in soil and the data is more scattered in soil-like formations. This is probably related to the fact that the Porto Granite is a highly heterogeneous weathered formation with many boulders. We were also able to observe lower and upper bounds for torque and cutting wheel force. The lower bounds are the minimum torque and cutting force necessary to penetrate through the material. The upper bound in the case of torque is a machine related limit and in the case of the cutting wheel force most likely is a limit related to lining resistance.

In order to determine the most suitable model (i.e. the one that "best" predicts reality) sensitivity analyses were then performed. Thirty one different models were considered and three different data sets were used. All data sets consisted of 720 rings ${ }^{1}$ chosen randomly in the section of the tunnel from rings 336 to 1611 . The training sets used are as follows:

A: Training data set A with Hierarchical discretization of continuous variables
B: Training data set B with Hierarchical discretization of continuous variables
A1: Training data set A with uniform bin width discretization of continuous variables

The data set A consisted of an equal distribution of soil, mixed, and rock data, i.e. $1 / 3$ of soil (G1), to $1 / 3$ of mixed (G2) and $1 / 3$ of rock (G3). Data set B data corresponds to a contribution of $34 \%$ of soil (G1) rings, $22 \%$ of mixed (G2) rings, and $44 \%$ of rock (G3) rings. The "real" geological states along the tunnel, which were used in the learning, are the ones determined by the contractor/designer, based on face surveys. At the face survey locations the geological states are known. Between face surveys the geological states were estimated by the contractor/designer.

Figure 14 presents some of the models used in the sensitivity analysis. The models considered varied from simple structures in which only one parameter is used to estimate the geology to more complex models with three or more parameters. Different inter-relationships between the parameters (shown by the different arrows between variables) were considered.

[^0]
[^0]:    ${ }^{1}$ Corresponds to a ring of lining, which in the case of Porto metro is approximately 1.4 m wide.

Note that other machine parameters, were besides the ones presented in Figures 12 and 13 were considered in the sensitivity analyses performed. These parameters included the earth pressure records from the EPBM. The results showed that these other parameters were not relevant when trying to predicted geology.

One Parameter Models
![img-13.jpeg](img-13.jpeg)

Two Parameter Models
![img-14.jpeg](img-14.jpeg)

Three and More Parameters Models
![img-15.jpeg](img-15.jpeg)

Figure 14 Sensitivity analysis: model structure selection
(GC=ground class; $\mathrm{P}=$ penetration; $\mathrm{TOC}=$ torque/cutting wheel force; $\mathrm{CF}=$ cutting wheel force; $\mathrm{TO}=$ torque; COTT=cutting wheel force/ total thrust)

The chosen model is shown Figure 15.The sensitivity analysis considered different parameters and different relationships between parameters (different models). The results of this analysis shows which models (i.e. parameters and their relationships) are important to consider when predicting geology. In this paper only the "best" model is presented, as shown in Table 2. The "best" model is defined as the one that correctly predicts the highest percentage of all ground conditions. However, because the geological conditions ranged from hard rock to soil, it is also important to evaluate how the models perform in each geological condition. Note also that the model was tested only on rings that were not used to train the models.

Table 2 Accuracy results for the "best" geological prediction model


This model, which performed the best overall (see Table 2), contained the parameters penetration rate (P), cutting wheel force (CF), and torque of cutting wheel (TO), and considered the interrelationship between torque and penetration as well as the inter-relationship between cutting wheel force and penetration, and torque and penetration. Note that despite the fact that TO is not

an important variable on its own when distinguishing geologies, the relationship between TO and P , and therefore TO was considered in the model.
![img-16.jpeg](img-16.jpeg)

Figure 15 "Best" geological prediction model

# 4. 6 Construction Strategy Decision Model 

Based on geological, construction and environmental information on the project, a Bayesian network model (extended influence diagram) was built in order to support the decision process during construction. The construction strategy decision model for the Line C tunnel of the Porto Metro is presented in Figure 16. The concept of the model was to support the decision in selecting the optimal construction strategy for the tunnel. In this specific case, it seems that one of the major issues was what would be the optimal mode for the EPBM to operate in given geological conditions. For this reason two construction strategies (Open Mode and Closed Mode) were considered in the model.
![img-17.jpeg](img-17.jpeg)

Figure 16 Decision Model for Line C tunnel

The model, a Bayesian network extended to a decision graph, contains 6 chance nodes, 1 decision node and two utility nodes.

The decision nodes represent different decisions or actions. The chance nodes identify an event in a Bayesian Network where a degree of uncertainty exists. The utility nodes represent the utilities associated with the different decisions/actions.
The Decision node, Construction Strategy (CS), represents the two possible Construction Strategies:
CS1- Open Mode
CS2- Closed Mode.
The chance node Ground condition at the face (GC) represents the different possible geological states that can be found in the sections at the face:
1- Soil (GC1);
2- Mixed (GC2)
3- Rock (GC3).
The chance node Piezometric Level (PL) represents the possible piezometric levels:
1 - piezometric level $<10 \mathrm{~m}$;
2 - piezometric level $>10 \mathrm{~m}$
The chance node Combined ground class (CGC) represents the combination between face condition and piezometric level.
The possible values are:
1-Soil with low piezometric level;
2- Soil with high piezometric level;
3-Mixed with low piezometric level;
4-Mixed with high piezometric level ;
5- Rock.
The chance node Failure ( $F$ ) represents probability of failure of the face given the combined geological and hydrological conditions, and the construction strategy used. The possible values are:

1- Failure;
2- No Failure.
The chance node Surface Occupation (SO) represents the occupation degree at the surface. The possible values are:
1- Low;
2-Medium;
3- High.
The chance node Damage Level (DL) represents the vulnerability, i.e. the fact that if the failure occurs the consequences are uncertain. The possible values are:
1- No damage;
2- Level 1 damage. This damage level corresponds to the situation of the first and second accident that occurred at the Line C tunnel, i.e. damages at the surface to buildings and other structures due to excessive deformation, including partial collapse of a building.
3- Level 2 damage. This damage level represents a collapse up to the surface causing total collapse of at least a building and damage to buildings and other structures at the surface. This is the situation of the 3rd collapse that occurred in the Line C tunnel. Note that in the model the Damage Level also depends on the surface occupation (Figure 16).

The utility node Total Utility consists of the cost of Construction (UC) and Cost of Failure (UF), which represent the costs associated with the construction and a possible failure, respectively.

The prior probability-and conditional probability tables, as well as utilities, attached to each node of the influence diagram of Figure 16 are presented in Tables 2 to 6 . Note that the probability of the ground class (GC) comes from the geological prediction model.

Table 3 Prior Probability of piezometric level


Table 4 Probability of CGC


Table 5 Probability of Failure given CGC and construction strategy, P (Failure| CGC, CS)


Table 6 Probability of Damage Level given SO and Failure


Table 3 presents the prior probability table for the piezometric level, P (PL). The prior probabilities of the piezometric level were determined subjectively, based on results of the

exploration borings and on what is known regarding the rainfall in winter around the Porto area. Table 4 shows the probability of CGC. This was considered, for simplification reasons, to be a deterministic variable that just combines geological state and hydrological state. The probability of failure depends on the geological and hydrological conditions as well as on the construction strategy employed. Table 5 shows the conditional probability table P (Failure| CGC, CS), for the variable Failure (F). The probability of failure was determined subjectively. Note that the probability of failure could have been determined based on mechanical models for face stability with EPBM, such as the method of Jancsecz and Steiner (1994), the method of Leca \& Dormieux (1990) or the method of Anognostou and Kovari (1996).

The utilities of construction are presented in Table 7. They are based on the cost (expressed in utilities) of construction costs in euro (million) per section (each section is about 160 m ).

Table 7 Construction costs per section


The utilities associated with consequences of failure and respective damage levels, presented in Table 8, were determined based on collapse cases from a database of accidents (Sousa, 2010).

# 4.7 Results 

The decision framework, consisting of a geology prediction model and a decision model described in this paper was applied to the Porto Metro in the following approach:

First, the geology prediction model was applied from ring 336, station $0+631$ (after the accidents) to ring 1611 , station $2+418$, i.e. in a section beyond the one where the accidents occurred. The results of the geologic prediction model showed good agreement with the observed geological conditions, particularly in identifying soil (G1) and rock (G3). In the case of soil, $77.2 \%$ of the rings sections that consisted of soil were correctly identified, $20.4 \%$ were misclassified as mixed and $2.4 \%$ as rock. In the case of rock, $82.4 \%$ of the ring sections that consisted of rock were correctly identified, while $10.9 \%$ were misclassified as mixed and $6.7 \%$ as soil. These results served as an indication of how well the geological model performed.

Second, the geology prediction model was used to predict the geological conditions for about 320 m (between rings 104 and 335) of the Line C of the Porto Metro, where the accidents occurred. Information on the geological conditions was available where the last accident occurred, because a post accident survey was made. The geological prediction model was also combined with the Bayesian decision model to determine optimal construction strategies ahead of the tunneling, in this section.

Figure 17 shows the predicted geology ahead of the face at different locations of the tunnel, from ring 217 to ring 335 (this is the area where the two last accidents occurred). It shows that as the EPBM face advances and gets closer to the $3^{\text {rd }}$ accident zone, the model predicts changes in geology and suggests changes in construction strategy. At ring 282 the predicted geology changes from G3 to G2, and as the excavation progresses one can observe that the probability of softer geological conditions (G1) increases as one approaches the $3^{\text {rd }}$ accident zone. These results indicate that the construction strategy should have been changed from CS1 (open/semi-closed

mode) to CS2 (closed mode) around ring 282 , i.e. about 140 m before the location of the $3^{\text {rd }}$ accident.

Table 8 Failure "costs" (per section)



Figure 18, shows summaries of the results of applying the combined risk assessment model from ring 263 to ring 335 . First they show the prediction of Geology that the tunnel passed through. They also show the optimal construction strategy for one ring ahead of the face. Regarding the geological prediction, the model predicts that the machine goes through mostly rock (G3) and mixed (G2) until the zone of accident 3, where the TBM enters a zone of soil (G1) that lasts until the zone of accident 2 (ring 318). From there until ring 335 , where the machine stopped is an area of higher probability of mixed (G2), but with considerable probability of soil (G1). These results seem to be in good agreement with what the accident report suggests, and with the survey results done in the area of collapse 3, after the work stopped. Regarding the risk assessment and choice of optimal construction strategy ahead of the face, the results show that the optimal construction strategy is CS2 (EPBM in closed mode) in the zone between ring 217 to ring 234 ; ring 244 to ring 253 ; ring 283 to ring 335 (zone of accident 2 and 3 ). This correspond to zones where soil (G1) and mixed (G2) were predicted. The optimal construction strategy is CS1 (EPBM in open mode) in the zones where rock was predicted, from ring 235 to ring 243 ; ring 254 to ring 257 ; ring 259 to ring 260 and form ring 263 to ring 282.

Figure 19 shows the design profiles, the post accident survey results and geology predicted by the model. Once again it is possible to see that there is a good agreement between geology predicted with the model and the results of the post accident borehole results. The design profiles (based on the initial geological survey (Figure 9), predicted that the tunnel would go through mainly rock in this section but the results of the post accident survey show that this area consisted mainly soil and mixed conditions at tunnel level. This is captured by our geology prediction model.

![img-18.jpeg](img-18.jpeg)

**Actual Strategy:** CS1 (Open/ Semi-Closed Mode)
**Model Result:** Optimal Strategy: CS1 (Open/Semi-Closed Mode)
![img-19.jpeg](img-19.jpeg)

**Actual Strategy:** CS1 (Open/ Semi-Closed Mode)
**Model Result:** Optimal Strategy: CS1 (Open/Semi-Closed Mode)
![img-20.jpeg](img-20.jpeg)

**Actual Strategy:** CS1 (Open/ Semi-Closed Mode)
**Model Result:** Optimal Strategy: CS2 (Closed Mode)
![img-21.jpeg](img-21.jpeg)

**Actual Strategy:** CS1 (Open/ Semi-Closed Mode)
**Model Result:** Optimal Strategy: CS2 (Closed Mode)
**b) Ring 282**
**d) Ring 297**

**Figure 17** Predicted geology ahead of the face at different locations of the tunnel (from ring 217 to ring 335)

![img-22.jpeg](img-22.jpeg)

Figure 18 Summary of the combined risk assessment model results (from ring 263 to ring 335)

![img-23.jpeg](img-23.jpeg)

Figure 19 Post accident survey results versus predicted geology by decision framework (adapted from Transmetro/Geodata, 2001)

# 5. Conclusions 

A decision support framework for assessing and avoiding risks in tunnel construction was developed and successfully applied in a case study. The decision support framework consists of the geology prediction model and the construction strategy decision model both of which are based on Bayesian Networks. TBM performance data are used to predict geology, which is then used to help decide on the construction method involving the lowest risk.

The presented risk model contains two models, a geological prediction model and a decision model. The geological model was trained (or calibrated) with the data from a specific project (the Porto Metro). Afterwards, the models were applied, i.e. tested on another section of the Porto Metro. The data that were used to test the model were not those used to the train the model. The results of the predictions of geology on the part of tunnel that was not used to train the model can predict changes in geology.

The application to the Porto Metro tunnel case, in which several accidents occurred, shows that the decision support framework fulfills its objectives. Specifically the results show that the model can predict changes in geology and that it suggests changes in construction strategy. This is most visible in the zone of accidents 2 and 3, where the model accurately predicts the change in geology and occurrence of soil. The "optimal" construction strategy determined by the combined risk assessment model is EPBM in closed mode, i.e. with a fully pressurized face, in the areas where accident 2 and 3 occurred, and not what was actually used during construction, EPBM in open/semi closed mode. This difference is due to the fact

that during the actual construction there was no effective system to predict changes in geology and therefore adapt the construction strategy.

Clearly the question arises how the proposed methodology process would work in other cases. If the geological prediction model were applied elsewhere (in another type of geology) it would need calibration. There is also the issue of not having data to calibrate the model at the beginning of construction. A way to use and calibrate this type of prediction model in cases where initial data do not exist (from a nearby project or similar geology) would be to use at the beginning of the construction subjective probabilities given by the experts (e.g. What is the probability that one is in Geology G1, if the Penetration rate is high (i.e. greater than a certain value), etc), and then update these probabilities as the construction progresses.

# Acknowledgments 

The authors would like to acknowledge The Fundação para a Ciência e Tecnologia (FCT) for the funding it has provided to this project through a doctoral research fellowship and the Porto Metro Authorities for generously allowing us to use data from the construction of the Porto metro, without which this work would not have been possible.
