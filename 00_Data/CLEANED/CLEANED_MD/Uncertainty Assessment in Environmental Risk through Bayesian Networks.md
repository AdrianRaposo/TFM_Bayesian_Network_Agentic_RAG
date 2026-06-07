# Uncertainty Assessment in Environmental Risk through Bayesian Networks 

A. Ahmadi ${ }^{1, *}$, A. Moridi ${ }^{2}$, and D. Han ${ }^{3}$<br>${ }^{1}$ Department of Civil Engineering, Isfahan University of Technology, Isfahan 84156, Iran<br>${ }^{2}$ Department of Water and Environmental Engineering, Abbaspour College of Technology, Shahid Beheshti University, Tehran 16765-1719, Iran<br>${ }^{3}$ Water and Environmental Management Research Centre, Department of Civil Engineering, University of Bristol BS8 1TR, UK

Received 20 January 2013; revised 4 May 2014; accepted 1 August 2014; published online 12 March 2015


#### Abstract

Assessing environmental risks on large dams is a challenging task. This paper describes a study on a novel and comprehensive application of Bayesian Networks (BNs) on the Abolabbas dam in Iran. Bayesian networks are based on probability theory and provide a powerful tool for structuring conceptualizations of the interactions between variables with uncertainties. Firstly, the interaction-based structure of variables is developed using the graphical model. Then, the Bayesian Network input variables, which affect the risk in two categories ("hazards index" and "consequences index"), are determined and the relations between different variables are modeled. The probability values for the risk levels are derived from a novel fuzzy set analysis. The results show that the environmental risk of the Abolabbas dam is considered at a high level with 12.8 percent probability. Also, the sensitivity analysis is used to find out the most effective variables on the environmental risk of the dam site. Finally certain important action plans are suggested to reduce and control the risk which represents a novel way for the risk reduction.


Keywords: risk assessment, environmental risk, Bayesian network, Entropy theory

## 1. Introduction

One of the primary goals of sustainable development is to achieve economic growth in the form of coordinated programs with environmental criteria and standards and to prevent degradation of renewable and non-renewable resources. To cope with population increase and living standard improvements, dams are widely built to deliver hydropower energy, to supply water for domestic, industrial and agricultural uses, and to help recreation activities. Dams have made important contributions to recent urban development, and their benefits have been considerable. However, critics of dams argue that the reduction of dams' environmental impacts is a challenging problem (World Commission on Dams, 2000) and the natural environment has paid a heavy price for man-made dams in addition to population relocation and other social impacts (Bohlen and Lewis, 2008).

There have been numerous studies on dams' environmental impacts. It has been found that dams may damage upstream riparian habitats (Ohmart et al., 1988), change the river flow regimes (Maingi and Marsh, 2002), degrade ecological systems (Baxter, 1977; Jansson et al., 2000), alter river sediment load and riverbed morphology (Yang et al., 2005), increase invasive species (Mumba and Thompson, 2005), dama-

[^0]ge the health and viability of aquatic biota (Kingsford, 2000), and increase water quality and disease burden in human populations (Lerer and Scudder, 1999; Tullos et al., 2009). All these changes have increased the public's concern over the adverse ecological, social, and economic consequences of dam building (Pejchar and Warner, 2001).

Since many interconnected parameters play complex roles in the dam-environment interaction, it is a challenging problem to find a linkage between different elements of the environment and dams. Lack of long-term observation data also hampers the relevant research activities. As a result, the environmental impacts of dams and their associated risks are still poorly predicted.

Currently, there are two categories of environmental risk assessment methods on dams: 1) classical models (i.e., probabilistic analysis); and 2) conceptual models (i.e., Multi-Criteria Decision-Making (MCDM), fuzzy set analysis) (Kangary and Riggs, 1989; Li et al., 2007; Jozi et al., 2012; Ahmadi et al., 2013). The classical approach is based on the quantitative information and data available to estimate frequency of effects and exposure. Hazard frequencies are estimated using the past observed data. In practice, this approach has a major limitation due to a shortage of detailed quantitative/historical data, which is even more difficult in the phase of project development.

Such a problem could be overcome with the conceptual approach. MCDM and fuzzy set analysis can all be carried out without long observation records. Recently, Bayesian Networks (BNs) are increasingly used as a risk assessment tool


[^0]:    * Corresponding author. Tel.: +98 3113913845; fax: +98 3113912700. E-mail address: aahmadi@cc.iut.ac.ir (A. Ahmadi).

aided by graphical models to represent the complex interactions between relevant causal influences on variables (e.g., Bacon et al., 2002; Borsuk et al., 2004; Bromley et al., 2005; Henriksen et al., 2007; Pollino et al., 2007; Ainslie et al., 2009; Chan et al., 2011; Patil and Deng, 2011; Wang et al., 2011). Increasingly, Bayesian Networks and object-oriented Bayesian Networks have been used to model diverse problems of high complexity for water management applications (Borsuk et al., 2004; Sadoddin et al., 2005, Dorner et al., 2007; Henriksen and Barlebo, 2008; Farmani et al., 2009; Carmona et al., 2011; Molina et al., 2011; Nikoo et al., 2011; Peng and Zhang, 2012a, b). BNs are useful for integrating different components from different sources into a unified framework (Pearl, 1988). Learning a Bayesian network includes learning the graph structure and the related parameters. Some methods such as back-propagation and evolutionary algorithms are used to learn the BNs in the literature (Buntine and Weigend, 1991; Larrañaga et al., 2013).

However, despite those published studies, there is a lack of systematic application of BNs on environmental risk assessment of dam projects. In this study, Environmental Risk Assessment (ERA) is carried out to identify the environmental hazards and their consequences associated with a dam project. The goals of the research are: identifying the most effective hazards and environmental consequences of a dam, developing the environmental risk assessment framework, applying Bayesian Networks in quantifying the potential risk, assessing the most effective variables on the environmental risk of the Abolabbas dam system as a case study, and investigating how changing the variables would influence the environmental risk.

## 2. Conceptual Development

Dam construction activities could impose severe environmental impacts that should be qualified and quantified for assessing the potential risks and reducing the negative impacts on the environment. Environmental risk assessment plays an important role in the environment management to mitigate project risks and achieve sustainable development. A combination of techniques may be used to quantitatively investigate the risk by including certain levels of uncertainties for each variable. Further, risk-reduction strategies and action plans should be developed from understanding the posed risks by specific hazards and their impacts and consequences with uncertainties. Therefore, developing a graphical cause-effect model can draw the paths of assessing the risk.

In this paper, in order to assess the environmental risk of a dam, a combination of probabilistic and fuzzy set analysis for risk assessment is used as shown in Figure 1. Different features and functions of the environmental risk of dams are identified in two main categories and their interactions are presented using a schematic cause-effect model. Then a Bayesian network is developed based on the cause-effect diagrams.

The conditional probabilities (CPTs) are utilized to express the relationships between parents and child nodes. One of the novelties of this paper is transforming the scores of the
model's variables to the probability values in different linguistic ranges based on the fuzzy set analysis. The sensitivity analysis on the identification of most effective variables on the risk is performed and the best management practices are suggested to reduce and control the environmental risk. Here, brief discussions of the used methods are given.
![img-0.jpeg](img-0.jpeg)

Figure 1. Flowchart of the research methodology.

### 2.1. Bayesian Network as a Risk Assessment Tool

Bayesian networks are a modeling technique based on Bayes' theorem that enables: (a) the explicit handling of the uncertainties associated with the application domain; and, (b) a graphical representation of the causal influences, which aid the explanation of the causes/effects described in the model.

The network characterizes variable relationships through interlinked nodes and arcs. The nodes represent variables and the arcs relate causes to effects. Bayesian Networks are used to identify those key variable relationships within a system. Information between nodes is produced based on the Bayes theorem. Bayes' theorem describes how the prior probability of A is updated by the observed evidence B . The theorem relates the conditional and marginal probabilities of A and B as follows:

$$
P(A \mid B)=\frac{P(B \mid A) P(A)}{P(B)}
$$

where $P(A)$ is the prior probability of the hypothesis (the probability that A will be in a particular state, prior to consideration of any evidence); $P(B \mid A)$ is the conditional probability (the likelihood of the evidence, given the hypothesis to be tested); and $P(A \mid B)$ is the posterior probability of the hypothesis (Bromley et al., 2005).
![img-1.jpeg](img-1.jpeg)

Figure 2. An example of Bayesian networks.
A simple Bayesian network is shown in Figure 2 to illustrate the application of BNs. The network has three nodes: two basic nodes [hazards index ( $h$ ) and consequences index $(c)]$, and one end node [risk $(r)$ ]. The nodes are connected by two arcs/links: $h-r$ and $c-r$. The prior probability of risk is expressed as follows:

$$
P\left(r=r_{1}\right)=\sum_{i=1}^{3} \sum_{j=1}^{3} P\left(r=r_{1}, h=h_{i}, c=c_{j}\right)
$$

where $P$ is probability, $r_{1}=$ low risk, $h_{1}=$ low, $h_{2}=$ medium, $h_{3}=$ high hazards index, $c_{1}=$ low, $c_{2}=$ medium, $c_{3}=$ high consequences index. According to the joint probability theorem Equation 1 can be written as:

$$
\begin{aligned}
& P\left(r=r_{1}, h=h_{1}, c=c_{j}\right) \\
& =p\left(h=h_{1}\right) \times p\left(c=c_{j}\right) \times P\left(r=r_{1} \mid h=h_{1}, c=c_{j}\right)
\end{aligned}
$$

where the conditional probabilities is considered on the right hand side of the equation.

Now, consider a case with a medium hazard index ( $h$ $\left.=h_{2}\right)$ and a medium consequences index $\left(c=c_{2}\right)$, the posterior probability of low risk, $P\left(r=r_{1} \mid h=h_{2}, c=c_{2}\right)$ can be calculated based on the definition of conditional probability as:

$$
\begin{aligned}
& P\left(r=r_{1} \mid h=h_{2}, c=c_{2}\right)=\frac{P\left(r=r_{1}, h=h_{2}, c=c_{2}\right)}{P\left(h=h_{2}, c=c_{2}\right)} \\
& =\frac{P\left(r=r_{1}, h=h_{2}, c=c_{2}\right)}{\sum_{k=1}^{2} P\left(r=r_{k}, h_{r}=h_{2}, c_{r}=c_{2}\right)}
\end{aligned}
$$

A number of commercial software packages are available for developing BN based models. The most popular ones are Analytica (Lumina, 2004); Netica (Norsys, 2005), Hugin (Hugin Expert A/S, 2004), GeNie (DSL, 2005) and Agenarisk (Fenton and Neil, 2004). The readers are referred to Uusitalo
(2007) for more details about the BNs software. In the field of environmental modeling, Netica and Hugin are most frequenttly used (Aguilera et al., 2011).

The Netica software tool can build, learn, modify, and store nets (Norsys, 2005). One advantage of Netica is the comprehensive, flexible and user friendly graphical user interface included in the package. Netica offers single-finding sensitivity analysis, which determines how much our perception of values in other variables will change given different values of a certain variable (Uusitalo, 2007).

### 2.2. Entropy Theory for Sensitivity Analysis

Sensitivity of the target node(s) in the BN model to variations in the other (evidence) nodes entered into the network can be assessed by sensitivity analysis (Pollino et al., 2007). Evidence nodes can be ranked based on evaluating the degree of variation in the BN's posterior distribution resulting from changes in the evidence. The nodes ranking can assist the expert in targeting future data collection.

Sensitivity analysis can be carried out using Shannon's entropy, $H(X)$, which is the measure of information transferred by the random variable, $X$. The formula for Shannon's entropy is defined as (Pearl, 1991):

$$
H(X)=-\sum P(x) \log P(x)
$$

where $x$ is a state of the random variable. The entropy value, $H(X)$ is used to assess the further information required in addition to the current information to specify an alternative.

Measuring the effect of one variable on another is referred to as mutual information, $I(X, Y)$. It is employed to assess the effect of collecting information about one variable $Y$ to reduce the uncertainty about variable $X$, as follows: (Pearl, 1991):

$$
I(X, Y)=H(X)-H(X \mid Y)
$$

The mutual entropy expresses the expected degree to which the joint probability of $X$ and $Y$ diverges from what it would be if $X$ is independent of $Y$ (Korb and Nicholson, 2004). If $I(X, Y)$ is equal to zero, $X$ and $Y$ are mutually independent (Pearl, 1991).

The entropy reduction associated with a node $X$ means that the uncertainty in variable $Y$ would be reduced by the increased observation about $X$. In this study for risk values, the Sensitivity to Findings function in Netica is used to identify the most effective network variables on the risk. These variables are referred to as 'findings nodes' in the literatures.

### 2.3. The Conceptual Model Development

One of the traditional ways to assess the environmental risk is to evaluate the release of hazards or threats into the receiving environment using the recorded data and frequency analysis. Further, risk-reduction strategies and action plans

![img-2.jpeg](img-2.jpeg)

Figure 3. Factors and their links in the hazards index.
![img-3.jpeg](img-3.jpeg)

Figure 4. Factors and links in the consequences index.
should be developed from improved understanding of both the risks posed by specific stressors and their impacts considering the uncertainties. In this paper, a Bayesian Network with two main sub-networks including hazards index and consequences index is developed for assessing the environmental risk. Therefore, we use a combination of techniques to quantitatively investigate the risk by including certain levels of uncertainties for each variable.

Figures 3 and 4 illustrate the factors influencing hazards index and consequences index and their sub-indices, respectively. In developing hazard index, the most probable hazards in occurrence of an event (crisis) for a dam are determined based on the literatures review (Scott et al., 1997; Toner and Keddy, 1997; World Commission on Dams, 2000; Maingi and Marsh, 2002) and experts' judgments through a series of meetings. The variables are classified in three major fields including 1) dam failure hazard, 2) hazard caused by a lack of co-
ordination, and 3) water quality and quantity hazard. Hazards index includes all the factors which are effective for a dam.

Dam failure potential is considered as a function of dam construction condition and geotechnical consideration such as landslide, liquefaction and seismicity. Dam failure potential is a key parameter for hazard index analysis.

Dam-break emergency action plans are aimed at minimizing the possible dam-break consequences. The success of action plan implementation depends on public awareness, cooperation between sectors and operators' education. Lack of the aforementioned factors during a severe flood makes serious flood damages. Hydraulic parameters including reservoir volume, inflow to the reservoir and water storage directly influence the dam safety conditions which cause dam overtopping (Peng and Zhang, 2013). Water quality hazard is considered by water salinity, thermal stratification and oil pollution in a reservoir.

Table 1. Description of the Input Variables of Hazards Index (Criteria) and Their States


The variables of consequences index are defined based on Environmental Impacts Assessment (EAI) guidelines. In these typical guidelines, the impacts (consequences) of the project development are assessed on natural, physiochemical and socioeconomic environments. For example, ICOLD (International Commission on Large Dams) has prepared a large and comprehensive matrix for use in EIAs for dams with these three major environments (ICOLD, 1980). Therefore, consequences index results from three sub-indices as 1) natural environment including fauna, flora and protected area, 2) physiochemical environment including environmental pollution, river and reservoir water quality, and 3) socioeconomic environment including ancient and historical structures, equality, and economic improvement. These variables are integrated within a single framework by defining the cause-effect diagrams in this study.

In the first step for assessing the environmental risk, the variables in hazards index and consequences index are identified. The second step is to define the cause-effect relationships between the system variables as shown in Figures 3 and 4. Tables 1 and 2 describe the input variables and their states in hazards and consequences indices, respectively. The structure of a developed BN is based on the defined variables and the cause-effect relationships.

## 3. Bayesian Network for the ERA of Abolabbas Dam

### 3.1. Study Area

In this study, the environmental risk assessment is conducted for a dam project, called Abolabbas, in Southwest Iran
on the Abolabbas river as shown in Figure 5. The Abolabbas dam is located at $50^{\circ} 11^{\prime \prime} \mathrm{N}$ longitude and $31^{\circ} 41^{\prime \prime}$ E latitude near the Baghmalek city. The goal of this project is to supply domestic water to the Baghmalek city and its neighboring villages as well as to produce hydropower energy and supply agricultural water demands. The catchment area upstream of the dam is about $284 \mathrm{~km}^{2}$. The reservoir volume at its normal water level is about 113 MCM with a height of 154 m from the riverbed.

The flood release is through an oogee spillway with 8 m in length. The only village upstream of the dam is Malagha. Of the 50 villages located downstream of the Abolabbas dam (see Figure 5), $30 \%$ are riparian. The population growth rate in rural regions of Baghmalek during the last decade is $-0.65 \%$ due to migration changes from rural to urban regions. The migration to urban areas is because of the low level of income and high unemployment of some farmers and also the lack of public health services. The rural population is about 39,730 in 2012. About $40 \%$ of the total rural domestic water consumption is supplied through a water distribution system and the rest is supplied from springs, wells or rivers. The major irrigation method in the study area is rain-fed. The area of agricultural lands is about 28,453 ha with $51 \%$ in rural regions. The dominant crops in the area are wheat, rice and barley. The reservoir water quality studies show that the stratification state of the Abolabbas is Oligotrophic.

In the ecosystems of the region, 78 and 12 plant species are identified, respectively. The dominant plant species are Compositae, Labiatae, Umbelliferae, Polygonaceae, and Convolvulaceae. The specific plant species with national and in-

Table 2. Description of the Input Variables of Consequences Index (Criteria) and Their States


ternational values include Pistachio, Quercus, Rhamnus, Scrophularia and Astragalus. The dominant mammal species are Canidae and Hystricidae, Leporidae and Muridae, and Canidae. 7 bird species are identified and the dominant ones are Alcedinidae, Ciconia ciconia, and Accipiteridae. The five fish species identified include Cyprinidae, Balitoridae, Nemacheilus, Barbus barbulus and Copoeta aculeate. The accessibility
to the river and four fish species for fishing activities increase the recreation attractions in the study area.

### 3.2. Development of Bayesian Network Structure

In this study, the existing qualitative and quantitative data are gathered to model the cause-effect relationships for envi-

![img-4.jpeg](img-4.jpeg)

Figure 5. Location of the Abolabbas Dam in southwestern Iran.

The non-constant risk assessment is developed based on the hazards index, the consequences index, and their sub-indices, defined in Figures 3 to 4 and listed in Tables 1 and 2. The graphical structure of the developed Bayesian network based on the system variables and their interactions is presented in Figure 6. The BN consists of two sub-models: hazards index and the consequences index.

Index | Consequences
Index | Risk |  |   |

Table 3. Conditional Probability Table for the Environmental Risk

The developed Bayesian network has three major typical elements including nodes, links, and Conditional Probability Tables (CPTs).

1. Nodes are displayed as boxes representing system variables. A node consists of a set of states that the node variables may take. In Figure 6 for example, the consequences index has three states (low, medium, and high).

Probabilities describe the chances that the variable takes on a particular state. For example, in Figure 6 there is a 67.5% chance that the consequences index is low, 25.5% chance medium, and 7% chance high.

1. Links represent causal relationships between nodes and are displayed as arrows between boxes. In Figure 6, for example, consequences index and hazards index are parent nodes, representing causes, of the child node of risk.
2. Conditional probability tables (CPTs) representing the relationship between the parent and child nodes are behind the Bayesian network. The quantitative relationships between a child node and its parent nodes are defined in each table (Wang et al., 2011).

# 4. Results and Discussion

## 4.1. Variables and Relationships

The first stage in the model development is to work out the relationships between model variables in the graphical and probability structure. The next stage is to estimate parameters, which involves specifying the CPTs for each node. For each variable, the number of states should be kept to a minimum (preferably three) as a compromise between resolutions of the variable ranges and model complexity.

For example, Table 3 shows the CPTs for risk variables based on hazards and consequences indices. The CPTs in this table can be interpreted as the probability that risk will be in its high, medium, and low states, given the states of hazards.

![img-5.jpeg](img-5.jpeg)

Figure 6. The developed Bayesian network to assess the environmental risk.
and consequences indices. The highlighted row of the table illustrates that if the consequences index is low and hazards index is high, there is a $25 \%$ chance that the risk will be low, a $50 \%$ chance that the risk will be medium, and a $25 \%$ chance that it will be high. The table structure for a node is generated by considering all possible combinations of parent node states.

The CPTs are generated based on the logic explicit documentation using deterministic equations or manually. For example, the framework of Table 3 is created based on the risk matrix approach presented in the documented literature. As can be seen in this table, if the hazards and consequences indices are at high levels, the probability of high risk will be $100 \%$. On the other hand, if the hazards and consequences indices are at low levels, the probability of low risk will be $100 \%$.

The probability estimates are elicited from two sources of information: experiential knowledge of experts, and documented scientific knowledge in the form of reports and scientific literature. In this study, the conditional relationships are specified utilizing the expert and analyst judgments because of data scarcity.

### 4.2. Synthesis of Knowledge into a Bayesian Network

The next stage is to assign node values to the parent states. In this study, the node values are assigned based on the experiential knowledge of experts, and documented scientific knowledge. The experts are selected to elicit a range of knowledge as broad as possible in the fields of hydraulics, ecology, hydrology, forestry, environmental management and other disciplines relevant in different aspects of Environmental Im-

Table 4. The Scores Assigned to the Variables in the Developed BN


pact Assessment (EIA) process. The EIA report is provided by MahabGhods Consulting Engineering Company (2010) and approved by Khouzestan Water and Power Organization (KWPO). There are 32 experts selected in this project.

The main points discussed at these meetings are about variable selection and network architecture. The experts suggest the variables should be defined based on Environmental Impacts Assessment (EAI) guidelines. In these typical guidelines, the impacts (consequences) of project development are assessed on natural, physiochemical and socioeconomic environments. Also the input nodes in each environment are selected based on the recommendation of the EAI guidelines and conformation by experts. For developing hazard index, the most probable hazards of a dam are proposed and classified in three major fields.

In this study, we designed a questionnaire to be filled in by the experts about the effectiveness of input variables on the environmental risk of the Abolabbas dam. A sample of the questionnaire used in the study is presented in Table 4. As shown in this table, the items to be asked from the experts are the input nodes of the BN model. The score to each item is obtained from the experts in a range from 0 to 10 and their averages are presented in Table 4.

The assigned scores to different variables on the environmental risk should be considered as the input values. A node value consists of the set of probabilities considering our current knowledge including uncertainty for describing the chances that the node outcome takes on a particular state. In order to transform the scoring values to probability values of
different states, the Fuzzy set analysis is used. These states are linguistic functions such as low, medium, and high considering the number of variable states in BN. Figure 7 shows the fuzzy transformation functions with three (low, medium and high) states. Unlike conventional fuzzy set analysis, fuzziness here represents ignorance or uncertainty on the variable which corresponds well to the belief in the Bayesian probability concept. Transformation of the scores to the probability values for different states using Fuzzy set analysis is an innovative part of this research.
![img-6.jpeg](img-6.jpeg)

Figure 7. The fuzzy transformation to change scores into probabilities.

The probability values of the fuzzy transformation considering the number of variable states in BN are presented in Table 4. For example, the score of 6 is represented by probability values of $80 \%$ in the medium state and $20 \%$ in the high state. So the score of 6 is transformed to the probabilities

Table 5. The Ranked Effective Variables on the Environmental Risk


in low, medium and high states. Utilizing the information and data from a wide range of sources (as presented in Tables 2 to 4), a Bayesian network is constructed to capture the current understanding on the potential effects of dam construction on environmental risk.

### 4.3. Environmental Risk Evaluation

One way to validate a developed model is to compare the model output with the outputs of other risk assessment methods or the observed data. The other methods such as MultiCriteria Decision-Making based on scoring and weighting achieve a single value without any levels of uncertainty. Because of this difference between the result types, the comparison of the results is challenging (Borsuk et al., 2004; Wang et al, 2011).

Also in the existing case, the Abolabbas dam is under
construction and there is no recorded data on the level of risks or other variables such as damage records, and water releases from the reservoir. Instead the model and each sub-model have been validated using the existing data for the current conditions through a review by local experts through discussion meetings held with the experts from MCEC and KWPO.

Firstly, the cause-effect diagram and the interpretation of each of the variables are presented. A discussion is then followed to ensure that the developed diagram did not differ significantly from the experts' understanding of the function of the system. Subsequently, the CPTs are generated to associate with the problematic nodes by considering all possible combinations of the parent node states. The probabilities assigned to different uncertainty levels (e.g. Low, Medium and High in Table 3) of child nodes are checked by experts' knowledge. Then the quantitative elements of the model are gathered. For this purpose, a questionnaire about the effect-

![img-7.jpeg](img-7.jpeg)

Figure 8. The sensitivity analysis results at the high level of the environmental risk.
tiveness of input variables on the environmental risk of the Abolabbas dam is filled in by scoring the input variables.

Validation of the developed BN is achieved through the use of the tool by experts to check that the model is behaving as expected. The model validation process is completed during the discussion meetings. The experts are asked to examine the model outputs to see if they are consistent with their belief. If the results do not agree with experts' expectations, the procedure to examine the structure and CPTs of the network and the scores to the input variables is carried out.

Some minor changes in the Bayesian diagram have been carried out especially in the consequences index sub-model. The final results show that the environmental risk is at a low level of risk with $51.7 \%$ probability, at a medium level with $35.5 \%$ probability, and at a high level with $12.8 \%$ probability. Overall, the environmental risk is in the low and medium levels with $87.2 \%$ probability.

### 4.4. Sensitivity Analysis

Table 5 shows the mutual information, the level of contribution in percent and variance of beliefs for different variables. Variances of beliefs provide an indication of the uncertainty surrounding the estimates.

The mutual information is used for ranking the variables according to the capacity for further evidence at these variables to change the posterior probability of the environmental risk. In other words the mutual information describes the expected reduction in mutual information of a query variable, $x$, due to a finding, $y$ as presented in Table 5. For example, the mutual information between the hazards index and the risk is 0.258 whereas it is 0.139 between the consequences index and the risk. It shows that the uncertainty in the risk variable would be reduced more by increasing the observations about the hazards index rather than increasing the information about consequences index.

According to the results, for the consequences index, the natural environment, physiochemical environment and then physical environment including changes in flora, fauna, reservoir water quality and especially bird community respectively have dominant influences on the risk. For the hazards
index, the most influential variables are dam failure hazard, water quality and quantity hazard, dam structure, geotechnical considerations and hazard caused by a lack of coordination, respectively. In the fifth column of Table 5, the input variables are marked. These input variables as the independent variables could be controlled by managers for risk reduction. The sensitivity analysis highlights the dominant influence of certain input variables including threatened flora, factor of safety, dam's life-span, ancient and historical structures, birds, liquefaction, and protected area. The rest of the input variables are less important and should demand less effort in quantifying them since they contribute little to improve the predictive accuracy of the model in the risk estimation. These variables are in the last rows of Table 5.

BNs allow assessing the relative changes in the output's probability in a certain state associated with changes in input nodes. This is the second type of sensitivity analyses used in evaluating the BN. In this way, the current probability of environmental risk at the high level, as well as the minimum and maximum of the risk probability at the high level due to the input variable changes are identified. Figure 8 presents the minimum, maximum and current probabilities of environmental risk at a high level due to changes of each variable. The probability of each input node can be altered over the probability space, and changes in the risk node.

Figure 8 shows the model sensitivity for all the variables to the environmental risk of the Abolabbas dam. In general, dam failure potential and impacts on natural environment have the greatest influences on the environmental risk. In this figure, the red line shows the current probability of the high level risk and the low and top bounds of the red line present the potential probability of the high risk that could be varied by changing each variable. The variables with wide top bound in Figure 8 shows that the variables could be considered as threats and should be controlled to avoid the risk increment. Also, the variable with wide left bound in Figure 8 shows that the variables could be considered as an opportunity for risk reduction.

For example, the current probability at the high level of the risk is about $12.8 \%$. In the worst circumstance for the "threatened flora" variable (when there is no conservation for

![img-8.jpeg](img-8.jpeg)

Figure 9. The sensitivity analysis results at the high level of the risk for variables in hazards index category.
![img-9.jpeg](img-9.jpeg)

Figure 10. The sensitivity analysis results at the high level of the risk for variables in consequences index category.
the threatened flora), the probability at the high level of the risk could be changed to $17.2 \%$. In the best circumstance for the "threatened flora" variable (with the conservation action plans), the probability could be reduced to $11.7 \%$. Therefore, the "threatened flora" variable has the wide bound between the current and the maximum probabilities of the risk with the significant influence on the increment of the probability at the high level of the risk. This variable is identified as a threat and should be controlled to avoid the risk increment.

This study is the first application of sensitivity analysis to support the decisions for proposing the action plans in risk reduction/control. The minimum and maximum values of the risk corresponding to variable changes in the hazards and the consequences are shown in Figures 9 and 10, respectively. The results show that the variables of the dam failure potential, soil properties, water quality hazard, dam's life-span in the hazards index category and natural environment, flora, fauna and threatened flora in the consequences index category should be considered in developing the risk mitigation strategies to reduce the probability of the risk at the high level. As shown in Figures 9 and 10, these variables have the wide top range with the potential to increase the risk identified as threats and
weakness of the system.
Importantly, it has been found that if we could control some variables such as dam failure hazard, water quality and quantity hazards, dam structure, water storage, lack of coordination from the hazards index category and natural environment, physicochemical environment, physical environment, reservoir water quality and flora in the consequences index category, significant reduction of the risk could be achieved. Some variables including the dam failure potential, natural environment, and flora have significant influence on both risk reduction and risk control identified as critical variables.

### 4.5. Action Plans for Risk Reduction

In order to reduce the risk at the high level, certain action plans are suggested to control the dam failure hazard, water quality and quantity hazard, and reduce the natural environmental changes. Actions include preparing the guidelines for crises management, performing the training exercise, improving the operator's knowledge and skills, and public awareness. To control the water quality and quantity hazards, certain practices to mitigate some significant risks include satisfying environmental water requirements especially in summer from the lower intakes, organizing and collecting industrial wastewater before its discharge to the reservoir, and monitoring and maintaining oil transfer pipelines. For mitigating the harmful impacts of dam construction on the natural environment, attention should be paid on the protection of narrow woodlands on the river banks such as Salix, Populus and Vitex plant species, as well as to build a fish ladder to reduce the effects of habitat fragmentation.

## 5. Conclusions

This paper describes a study to use Bayesian Networks for environmental risk assessment of dams. The Bayesian network is developed to model the relationships between the variables using the CPTs. The scheme is examined for the Abolabbas dam utilizing the scores transformed from the probabilities using Fuzzy set analysis. To explore and learn about the risks management, sensitivity analysis has been performed. Firstly, the most influential inputs are identified by measuring the sensitivity of changes in probabilities of the risk while inputs variables are perturbed. The changes on the environmental risk at the high level are evaluated. Based on the distance between the current risk and its minimum and maximum values, the control risk reduction strategies are recommended. The results show that the variables of the dam failure potential, natural environment and flora are critical and should be controlled through the risk reduction action plans. To reduce the high level risk, certain action plans are suggested.

It should be noticed that the risk assessment approach using the Bayesian Network has several advantages over the MCDM techniques. The main advantage of the BN technique is that the model outputs consist of a probability values rather

than a single and relative value. Secondly, BNs allow determining the probabilities of different risk levels. They provide an approach to decision making incorporating the uncertainty related to human behaviors. The ability of a Bayesian network model to handle qualitative data is one of the distinctive advantages of the approach.

Various simplifications are considered in BNs development. For example, in order to reduce the overall size of the CPTs, the number of discrete states is reduced. Limitation on the number of discrete states is one of the problems associated with the use of BN. The ability of Bayesian modeling techniques to deal with continuous data is limited (Jensen, 2001) and such data generally needs to be discretized. Discretization can only capture rough characteristics of the original distribution (Uusitalo, 2007). The problem has been partially solved in the Agenarisk tool which allows the user to create continuous nodes, although there are restrictions on the number of links (parents) that a node can have.

Due to the problems associated with the use of BN, more work could be done to improve the BN capabilities.

1. More accurate data of different disciplines of environmental risks should be collected. Then, the BN is updated based on the collected data.
2. The ability of Bayesian modeling techniques to deal with more parent nodes should be improved.
3. The model results should be validated based in the recorded data of different dams.
4. Since a BN only uses discrete variables, automatic data discretization techniques could be useful.
5. BNs should be improved for utilizing continuous-state variables. The shortcoming of not considering continuousstate variables may be incorporated using different distribution functions.

Acknowledgments. The authors gratefully acknowledge the contributions of the experts from MahabGhods Consulting Engineering Company (MCEC) and Khuzestan Water and Power Organization (KWPO) who have collaborated in this research.
