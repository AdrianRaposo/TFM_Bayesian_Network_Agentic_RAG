# Article 

## Uncertainty in Building Inspection and Diagnosis: A Probabilistic Model Quantification

Clara Pereira * ${ }^{\text {® }}$, Ana Silva ${ }^{\text {® }}$, Cláudia Ferreira ${ }^{\text {® }}$, Jorge de Brito ${ }^{\text {® }}$, Inês Flores-Colen ${ }^{\text {® }}$ and José D. Silvestre (D)<br>check for updates

Citation: Pereira, C.; Silva, A.; Ferreira, C.; de Brito, J.; Flores-Colen, I.; Silvestre, J.D. Uncertainty in Building Inspection and Diagnosis: A Probabilistic Model Quantification. Infrastructures 2021, 6, 124. https:// doi.org/10.3390/infrastructures6090124

Academic Editor: David Lattanzi

Received: 9 July 2021
Accepted: 31 August 2021
Published: 1 September 2021

Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## (0) 0

Copyright: (c) 2021 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

CERIS, Instituto Superior Técnico, Universidade de Lisboa, Av. Rovisco Pais, 1, 1049-001 Lisboa, Portugal; ana.ferreira.silva@tecnico.ulisboa.pt (A.S.); claudiaarferreira@tecnico.ulisboa.pt (C.F.); jb@civil.ist.utl.pt (J.d.B.); ines.flores.colen@tecnico.ulisboa.pt (I.F.-C.); jose.silvestre@tecnico.ulisboa.pt (J.D.S.)

* Correspondence: clareira@sapo.pt; Tel.: +351-21-841-9709

Abstract: In the field of building inspection and diagnosis, uncertainty is common and surveyors are aware of it, although it is not easily measured. This research proposes a model to quantify uncertainty based on the inspection of rendered façades. A Bayesian network is developed, considering three levels of variables: characteristics of the building, façade and exposure conditions; causes of defects; and defects. To compute conditional probabilities, the results of an inspection campaign from the literature are used. Then, the proposed model is validated and verified using inspection results from another sample, the combination of a strength-of-influence diagram and sensitivity analysis and the application of the model to a case study. Results show that the probabilities computed by the model are a reasonable representation of the hesitancy in decision making during the diagnosis process based only on visual observation. For instance, design and execution errors show lower probabilities due to not being verifiable a posteriori without detailed documentation. The proposed model may be extended and replicated for other building materials in the future, as it may be a useful tool to improve the perception of uncertainty in a key stage of building maintenance or rehabilitation.

Keywords: Bayesian networks; building inspection and diagnosis; façade renders; uncertainty

## 1. Introduction

### 1.1. Background, Problem and Purpose

Physical degradation is one of the processes that may result in the obsolescence of buildings, as some performance requirements stop being fulfilled and, eventually, the building or its elements reach the end of their service life. Physical, chemical and mechanical degradation agents gradually affect building elements and, together with natural ageing, lead to deterioration [1]. This general issue requires action to extend the buildings' service life, such as carrying out maintenance activities to hinder the degradation mechanisms.

In the context of maintenance planning, which combines different maintenance strategies (reactive or proactive, whether preventive or condition based [2]), building inspections provide valuable data on the degradation condition of the building elements, informing stakeholders and helping them to make better decisions.

Nevertheless, uncertainty is associated with the inspection and diagnosis activities performed to assess the degradation state of buildings and their elements. Even though this uncertainty is rarely quantified, surveyors, designers, engineers and prescribers are aware of some level of subjectivity inherent to all diagnoses, as well as of the vulnerability and unpredictability of outcomes stemming from recommendations and decisions. Additionally, the levels of uncertainty vary according to several contextual factors.

During inspection and diagnosis operations, uncertainty may arise at different stages, namely [3]:

1. During the observation, understanding and analysis of degradation phenomena, depending on:

a. The knowledge and experience of the surveyor
b. The circumstances of observation (for instance, means of access or weather conditions)
c. The availability and effective use of expeditious means of observation (more relevant when the signs of failure are invisible to the naked eye)
d. The preliminary planning of the on-site inspection (for instance, consulting available documents about the building)
2. During the process of clearly identifying the defect, its causes and the best course of action to reinstate performance levels that fulfil the building element's functional requirements, while making decisions involving:
a. The determination of the need of additional in situ diagnosis methods or laboratory tests
b. The choice of in situ diagnosis methods or laboratory tests, if needed, considering their contribution for a more accurate diagnosis (usefulness, intrusiveness, ease of execution, precision, type of results, cost, time needed to obtain results)
c. The decision about whether eventual results of in situ diagnosis methods or laboratory tests are conclusive and enough [4]
d. The identification of the defect and its causes based on all available data (information about the building, visual inspection and any additional diagnosis method)
e. The development of recommendations according to the diagnosis.
3. During the communication of recommendations in a non-ambiguous and detailed way, allowing stakeholders to weigh several parameters that may affect decision making
Uncertainty is associated with risk, and the former needs to be acknowledged so that any danger is not completely unexpected. Risks may be associated with, among others [3], (i) an incorrect diagnosis, causing resources to be allocated towards activities that end up not extending durability; (ii) an inadequate application of repair techniques, although resulting from a correct diagnosis; (iii) a decontextualised evaluation of the built object, eventually disregarding occasional historical value; and (iv) an incorrect safety assessment of the building, leading to human and material losses.

To overcome the blurred perception of uncertainty by surveyors during the process of diagnosis of the degradation, it is necessary to find a way to clarify that perception. Quantification measures are expected to be more effective in promoting that clarification process.

This research intends to propose a model of quantification of uncertainty in building inspection and diagnosis. With that purpose in mind, the scope of building inspection and diagnosis was limited to a type of façade cladding (façade renders) so that the problem could be outlined in a simpler manner. Additionally, the diagnosis of a detected defect was analysed to define the factors that influence it (e.g., causes). Furthermore, those factors had to be adapted to a quantification model. It is expected that the findings of this research will help surveyors in enhancing their understanding of the underlying uncertainty associated with the diagnosis process, thus improving it.

In this paper, after a brief description of the issue at hand, Bayes' theorem and Bayesian networks are outlined. Then, the materials and methods used in this study are described, including not only those needed to create the proposed model but also those to assess it. Next, the results are presented in terms of the development of the model and respective validation and verification. Results are then discussed, and the main conclusions are drawn.

# 1.2. Formulations of Uncertainty 

There is a large range of disciplines that refer to uncertainty, whether applying concepts of decision theory, statistics or other quantification fields. In this section, the methods of Bayes' theorem and Bayesian networks to deal with uncertainty are highlighted.

# 1.2.1. Bayes' Theorem 

The diagnosis process in the context of building inspection involves making decisions that can be compared to those in the medical (clinical) context, with the necessary adaptations. In differential diagnosis, uncertainty can be faced complementing the competinghypotheses heuristic with Bayesian probability [5]. In that context, uncertainty may be associated with [5] (i) clinical information, (ii) interpretation of laboratory data, (iii) the connection between clinical findings and diseases and (iv) the effects of different therapies. These items can be matched with parameters involved in building diagnosis, namely (i) information about the building and its components, (ii) interpretation of data from in situ or laboratory tests, (iii) the connection between defects and their causes and (iv) the effects of different repair techniques.

The same way the mathematical form of Bayes' theorem can be used in a clinical context when estimates of the likelihood of a disease for relevant groups are available [5], it can also be applied in building diagnosis when estimates of the likelihood of causes of defects are employable for relevant groups of building elements or materials. Nevertheless, even without calculations, the formulation of Bayes' theorem can help clinicians and surveyors to address decisions about the possible relevance of additional information [5].

Although Bayes' theorem may have limitations, its logic may be useful to improve systematic problem solving during a diagnosis process. Bayes' theorem's simplest form is presented in Equation (1):

$$
P(\text { cause } \mid \text { defects })=[P(\text { defects } \mid \text { cause }) \times P(\text { cause })] / P(\text { defects })
$$

representing the probability $P$ of a building element or material being subjected to a cause of defect, given the observation of a set of defects. In Equation (1), the numerator refers to the product between (i) the probability of having that set of defects, given the presence of the considered cause, and (ii) the probability of having the cause in the population of building elements and materials. That population may refer to specific characteristics, such as elements only in the building envelope or only cementitious materials. The numerator is divided by the probability of occurrence of the set of defects [3].

The limitations of using Bayes' theorem are associated with [5] requiring large datasets, the shifting availability of probability estimates (variations of available data according to symptoms and diseases), the complexity of stating hypotheses based on anomalous manifestations and the difficulty of computing probabilities from memory. Moreover, Bayes' theorem does not conciliate the hypothesis of multiple diseases occurring in the same case (or multiple causes in the same element), nor the non-independence of symptoms associated with a single disease (or defects and a single cause).

### 1.2.2. Bayesian Networks

To deconstruct the analysis of elaborate problems, their components can be reduced to a finite number of states. An option is to formulate binary hypotheses, modelling numerous scenarios, which may still be incomplete, as the systems' components often require the assumption of multi-states. In these cases, Boolean or classic logic may be insufficient [6]. Such probabilistic events can be framed within Bayesian networks, which provide a theoretical context to represent events using discrete random variables [7]. The relationship between those events is then represented by conditional probabilities [6].

Considering these premises, the degradation mechanisms of a building can be represented as a system and analysed, breaking down its components. Thus, a Bayesian network (BN) can be developed, where uncertainty would be represented by the conditional probability tables (CPTs) associated with each variable. In the present research, the system was delimited to rendered façades, as part of a more complex system. In this way, a lower number of variables may be considered to explore the applicability of the methodology.

In a BN, variables are represented by nodes and the relationship between nodes is represented by arcs. Those arcs are unidirectional, denoting the influence of one node (at the tail of the arc) in another node (at the head of the arc). That graphical structure

is complemented by the numerical properties of each node, which are encoded in CPTs, prepared according to the influence of prior nodes [8].

In the field of building performance, a BN has already been developed to predict the condition of buildings in order to assist maintenance planning [9,10,11]. Other authors [12,13] proposed the use of dynamic Bayesian networks to model the deterioration process of structural systems as a method suitable to plan and optimise monitoring activities, as well as inspection and other maintenance actions of such systems. Bayesian belief networks were also used, for instance, to assess the probability of collapse of structures associated with the corrosion of reinforcement in concrete structures of buildings, for repair optimisation [14] and to monitor the condition state of a bridge [15]. Additionally, maintenance scenarios were also explored using Bayesian networks to support decision making at the design stage of a building, accommodating a design-for-maintainability approach [16,17]. Most of the mentioned research in the literature input conditional probabilities in the BN based on the judgement of experts, while the model proposed in this research is based on an existing dataset from on-site inspections, providing conditional probabilities from real scenarios. Additionally, the proposed model deals with a specific problem that has not been focused on previous research about uncertainty-the inspection and diagnosis of non-structural materials of the building envelope. Thus, the present research adds novelty to the literature.

# 2. Materials and Methods 

This study adopted an observational research methodology to create a model to quantify uncertainty in building inspection and diagnosis. Developing such a model required a set of analysis, execution and verification steps. Research procedures included (Figure 1) understanding uncertainty and risk in the studied context, selecting a model to perform uncertainty analysis, defining CPTs and assessing the BN model. Within these procedures, several research steps were performed, including selecting a dataset (from the literature) and analysing quantitative information.
![img-0.jpeg](img-0.jpeg)

Figure 1. Framework of the methodology.
At an initial stage, a search for common and accessible BN modelling tools was performed, considering the capabilities of each software and the objectives of the research. GeNIe Modeler [18] was chosen due to the reliability of data analysis, its user-friendly interface and its availability for academic users.

Based on the sample of Sá et al. [19], the model refers to existing rendered façades in urban buildings (with residential, office and commercial uses). The sample includes 99 different façades from the inspection of 52 buildings, all located in the metropolitan area of Lisbon, Portugal. The inspections occurred in 2010 [19]. The buildings were totally or partially occupied and were associated with different types of actors, such as owners and tenants. Inspections were solely based on visual observation and small interviews with owners or tenants.

### 2.1. Development of the Model and Defining CPTs

The sample points correspond to defects visually detected on each inspected façade. Each observation included information about (i) the building (age, exposure to aggressive

agents—rain-wind action, humidity, pollution); (ii) the façade (orientation, type of render, execution method and finish, type of washes and washing frequency) it was detected on; and (iii) information about the probable causes inferred during the diagnosis. Data about the number of floors of the building, type of façade (front, since, rear), area of the rendered surface, proximity to heat sources, inclusion of a reinforcement mesh, contact with people and animals, and recommended diagnosis methods and repair techniques were also available but were excluded from the analysis. Only the most influential characteristics of the building and façades for their degradation were considered, according to whether they seemed likely to affect defect occurrence [20], while diagnosis methods and repair techniques were not considered a part of the cause-effect relationship represented in the proposed model.

Thus, the relevant variables for the analysis of the degradation of rendered façades had already been identified by Sá et al. [19], being subjected to a refinement process aiming at constraining the complexity of the BN.

Upon further analysis of the sample, two outlier observations were excluded from the sample, as an unlikely number of probable causes was being pointed out ( 14 different types of causes), revealing great doubt on the diagnosis of those two occurrences. The remaining observations considered between one and seven probable causes (direct or indirect [21]) for the occurrence of each defect.

Nodes in the BN model represent variables that are associated with the final output; otherwise, they can be deemed insignificant and removed [6]. In such a model, an effort should be made to include only significant variables so that the complexity of the network is not needlessly increased, thus optimising time and effort according to the added value (i.e., parsimony principle).

After the identification of variables, the type and states of the nodes were determined. Nodes can be discrete or continuous [7]. Discrete random variables represented by chance nodes were included in the proposed BN model. The node state is defined according to the type of node. Some were defined as Boolean, having binary states, such as true or false (nodes of causes of defects and defects). Others were defined as multi-state, such as, in the case of façade orientation, eight states/orientations, according to the points of a compass.

Three levels of nodes were designed in the structure of the model [9]: level 1, referring to physical characteristics; level 2, referring to probable causes of defects; and level 3, referring to observable defects. Level 1 nodes are root nodes, whose child nodes are level 2 nodes. Level 3 nodes are leaf nodes, whose parent nodes are level 2 nodes [6]. Level 1 nodes are general chance nodes. Levels 2 and 3 nodes are chance nodes using the Noisy-Max assumption [20]. The Noisy-Max assumption is part of a technique to ease the process of structuring large networks. It is applied when a binary effect variable $y$ may have different possible causes, $x_{i}, i=1,2, \ldots n$. Each cause has a probability $p_{i}$ of being sufficient to produce the effect in the absence of all other causes, and the probability of each cause being sufficient is independent of the presence of other causes [20]. A base rate probability $p_{0}$ should also be assessed, representing "all other causes", as it is assumed that a BN is never complete. Noisy-Max chance nodes allow simplifying the computation of CPTs, as it is much easier to answer the question "What is the probability of $X$ when only cause $U$ is present?" than to entail a complex casuistry [22]. Using this type of nodes saved an essential amount of processing time.

Evidence about the key variables was collected from Sá et al.'s [19] sample with 368 defects attributed to 807 causes. Inspected buildings were, on average, 27 years old, with 6 storeys. On average, each rendered surface was $380 \mathrm{~m}^{2}$. The collection of data was carried out according to the methodology of inspection systematised by Sá et al. [23]. Correlation tests (Pearson's and Spearman's tests) were performed to reduce data, leading to the pairing of highly correlated variables. These tests were carried out using STATISTICA $8.0[24]$

# 2.2. Assessment of the BN Model 

The objective of assessing the BN model is to test its behaviour considering façade renders' degradation mechanisms, highlighting any inconsistencies [25]. The assessment process is threefold, including verification and validation stages. Verification is to demonstrate that the model has an acceptable accuracy level, and validation is to ensure that the model meets the predetermined objectives [26].

The first step in the assessment process consists of comparing the results of applying the BN model to other inspection results, from other samples available in the literature [27]. This process may benefit from the consistency of inspection methodologies, collecting similar types of information from objects. So, the sample of Pereira et al. [27] was considered, assessing the degradation of those rendered surfaces using the proposed method. The results were then compared and discussed to evaluate the model's validity.

Secondly, a strength-of-influence diagram was drawn and combined with carrying out a sensitivity analysis to discover the relative importance of different indicators in the model to reach the quantification of the probability of occurrence of defects [20]. That perception allows comparing the model with the expectations and empirical knowledge of the defect's diagnosis process. Sensitivity analysis is performed according to predetermined target nodes, identifying the most critical parameters.

The third, and final, stage of the assessment process consists of using a case study to verify the model [10], assuming a building with four façades as four different scenarios. The case study is a single-family residential building 37 years old with a floor area of $176 \mathrm{~m}^{2}$, located in the municipality of Leiria, Portugal. The main characteristics of the building and their façades were collected and entered as evidence in the model. Then, the predictions of probable causes and defects were studied and cross-checked with observations of the built object to verify the model applicability.

## 3. Results

### 3.1. Development of the Degradation Analysis Model

The variables associated with the degradation of rendered façades in the sample of Sá et al. [19] can be grouped into (i) characteristics of the building and its exposure, (ii) characteristics of the façade and its maintenance, (iii) probable causes of defects, (iv) defects, (v) recommended diagnosis methods and (vi) preconised repair techniques. Within the whole set of variables, to optimise the BN structure and processing time, only some characteristics of the building and of the façade were considered. Moreover, as the network focused on the diagnosis of symptoms and diseases [5], the possibility of carrying out diagnosis methods and the recommendation of repair techniques were excluded from the model. Additionally, selecting variables to frame the problem considered whether they seemed likely to affect the occurrence of defects. The set of variables is presented in Table 1.

Using the Spearman rank-order correlations, non-parametric correlations between the building and façade characteristics were computed. This statistic helped to reduce data, namely joining three different variables (the type of render (e.g., one-coat), type of execution (e.g., mechanical) and type of finish (e.g., bush-hammered)), as they presented high correlation coefficients between them. The type of render and the type of execution had a Spearman rank-order correlation of 1.00 , while the type of render and the type of finish had 0.71 . The type of execution and the type of finish also had a 0.71 Spearman rank-order correlation. So, in the sample, traditional renders were all executed manually and had two types of finish: textured or smooth. On the other hand, all one-coat renders were executed mechanically and corresponded to two types of finish: mineral or bush hammered.

Table 1. Variables in the BN model and respective states (based on [19]).


Table 1. Cont.


Pearson product-moment correlations were computed for the probable causes of defects, also aiming at data reduction. High correlations were detected between C-C6 and C-U3 (0.73), C-A7 and C-C5 (0.81) and C-E14 and C-E7 (0.66), which led to pairing those variables. C-C6 refers to the faulty specification of the applied products, while C-U3 refers to poorly executed maintenance works or minor repairs. Although C-U3 refers to the maintenance and operation stage of the building's life cycle, it is related to C-C6, as poor maintenance and repair works often are due to a poor choice of materials.

As for C-A7, it is a mechanical action cause indicating stress concentration (for instance, next to the corners of windows). That stress can be minimised using reinforcement embedded in the render, and that is what cause C-C5 refers to, thus making sense to join both variables.

Finally, C-E14 is an execution error occurring when there is a lack of monitoring of the rendering during the curing process. On the other hand, C-E7 refers to execution errors while formulating the render, namely with an excessive amount of water or when mortar or substrate walls have excessive moisture. Therefore, knowing that moisture content affects the curing process of the render, C-E14 and C-E7 were paired in a single variable.

High Pearson $r$ correlations were also detected between C-E11 and C-E1, C-E11 and CE7, C-E11 and C-E14, C-E1 and C-E7, and C-E1 and C-E14. Nevertheless, "C-E11 Rendering applied under adverse weather conditions" and "C-E1 Use of inexperienced/unqualified workmanship" were not observed in the sample of Sá et al. [19], being excluded from the BN structure.

The states of each variable were determined according to the data collected on-site [19]. Buildings were between 2 and 51 years old. Thus, Sturges' [28] suggestion of sizing intervals was used, as presented in Equation (2):

$$
k=1+3.3 \log n
$$

where $n$ is the number of data values and $k$ is the number of intervals, while logarithms to the base 10 are employed [29]. Six intervals were determined, leading to the presented possible states of the variable "age".

Rain-wind action, exposure to humidity and exposure to pollution were defined according to the work of Silva et al. [1]. The states of the variable referring to the orientation of the façade were defined according to the cardinal and ordinal directions (eight possible states). The type of render, execution and finish were defined according to the properties of each surface inspected. The type of washes referred to gentle or average aggressiveness in cleaning the façades, while the periodicity of that operation determined three levels of washing frequency.

Tables 2 and 3 refer to correlations, respectively, between causes of defects and characteristics of the building and the façade, and between causes of defects and defects.

Table 2. Spearman rank-order correlations between causes and characteristics of buildings and façades.


Underlined correlations are significant at $p<0.05$. Highlighted correlations: in pink $>0.15$; in yellow $<-0.15$. Missing data pairwise deleted.
Although correlation does not imply causality, some affinity is noticed between some parameters in Table 2, as several significant correlations were determined.

In Table 3, the highest correlation coefficients show some empirical relationships, such as the association between graffiti and vandalism; dirt/particles deposits and the existence of airborne dirt particles in the environment; corrosion stains and the corrosion of metal elements, whether embedded or fixed to the surface render; efflorescence/cryptoflorescence and the presence of water-soluble salts; mapped cracking and shrinkage of the render; and scratches/grooves and the occurrence of impacts/bumping with the façade.

Table 3. Linear correlation between causes and defects.


Underlined correlations are significant at $p<0.05$. Highlighted correlations: $>0.70 . n=370$ (casewise deletion of missing data).
The graphical structure of the model reflects the relationships identified in the literature review, namely the characteristics of the building, façade and their exposure influence the rise of diseases (causes of defects), while the causes affect the occurrence of defects. Hence, three levels were designed. The colour of the nodes is also associated with their nature; i.e., first-level nodes are blue, second-level nodes are pink and third-level nodes are yellow. Different shades of pink were used to categorise the nodes of the causes of defects according to the groups of causes [23]: design errors, execution errors, environmental actions, mechanical actions, and wear and maintenance faults. Likewise, different shades of yellow categorised the nodes of defects [23] as aesthetical defects, defects associated with moisture and mechanical action-related defects. The arcs drawn between nodes determined that, to design and execution errors, only the characteristics of the building and façades were relevant, excluding exposure characteristics. The arcs between the causes and the defects were drawn according to the different scenarios of causality determined during the inspection process [19]. Figure 2 represents the graphical structure of the model.

![img-1.jpeg](img-1.jpeg)

**Figure 2.** BN model to quantify uncertainty in building diagnosis.

For instance, for node "C-C2 Faulty design or lack of detailing", the characteristics age, type of render, execution and finish, type of washes and washing frequency were considered to have some influence. Although the maintenance of the façade does not correspond to the design and construction stage of the building's life cycle, design errors may be highlighted or disguised by the maintenance conditions. As for a node from the group of environmental actions' causes, "C-M4 Presence of water/water vapour" is considered to be influenced by all first-level nodes. So, it is assumed that the response to aggressive agents is not independent of the building and façade characteristics.

The scenarios of defect occurrence represent the inferences and effect-cause relationships determined by the surveyor during the on-site diagnosis. The example of "A-H1 Infiltrations/dampness stains" can be mentioned. It referred to 20 different combinations of causes, including 12 different types of probable causes (design errors, environmental actions, and wear and maintenance faults). Still, the Noisy-Max assumption [20] determines that each cause must be considered as being able to produce the effect (defect) separately. Thus, it is assumed that the surveyor determines more than one cause for an occurrence as a reflection of the uncertainty of the diagnosis.

The CPTs of the nodes mirror the specificity of the sample of Sá et al. [19], i.e., construction features are associated with the Portuguese construction sector methodologies and practices, while environmental specifications are typical of a metropolitan area with a Mediterranean climate. Relative frequencies were used as the probability measure. Figure 3 shows an excerpt of the BN model, where nodes are represented by boxes showing bar charts of the probability of each node. It is noted that "C-M1 Airborne dirt particles" (88\%) is the most probable cause in the group of environmental actions. Additionally, in the first-level nodes, the prevalence of gentle washes ( $85 \%$ ) on the sample of façades is evident.

# 3.2. Model Evaluation 

### 3.2.1. Verification of the Model Results

To verify the estimation of uncertainty in the diagnosis process, inspection results from a different sample [27] were used. In the BN model, the characteristics of the building were input, as well as the detected defects, one at a time. The unequivocal presence or absence of causes was also entered, namely the absence of vandalism. One building was chosen, and a surface per inspected façade was analysed. The results and the quantification of uncertainty provided by the BN are presented in Table 4.

The building selected was eight years old at the moment of inspection and was subjected to moderate wind-rain action. It had low exposure to humidity and high exposure to polluting agents. The façades were rendered with a traditional mortar scheme, applied manually with a smooth finish. No information was available referring to the type of washes nor its frequency. As the building was in a fenced plot, "C-U6 Vandalism" was considered to be false.

The uncertainty of the causes of defects shown in Table 4 express that:

- Design and execution errors' causes have consistently lower probabilities of being true.
- Every set of causes selected for a defect has at least one cause with a probability of being true higher than $50 \%$.
- The highest probability obtained from the verification cases was $87 \%$, corresponding to cause "presence of water/water vapour" (C-M4) of defects "efflorescence/ cryptoflorescence" (A-H4) and "infiltration/damp stains" (A-H1); this cause is a wellknown part of the degradation mechanism of efflorescence and façade staining [30].
- The lowest probability obtained from the verification cases was $11 \%$, corresponding to causes "faulty design or lack of heat insulation in walls" (C-C4) and "lack of conformity to design and/or building and construction specifications" (C-E2), attributed to the occurrence of "infiltration/damp stains" (A-H1). When thermophoresis occurs (i.e., the condensation of water vapour in the cooler areas/materials of a façade [31]), the design of a poorly insulated wall or not executing the designed wall (well insulated) may result in moisture stains highlighted by the accumulation of dirt; however,

Table 4. Quantification of uncertainty based on the BN model using cases of a sample from the literature [27].


![img-2.jpeg](img-2.jpeg)

**Figure 3.** Partial view of the BN model with charts showing the probability of occurrence of environmental and construction characteristics and of environmental action causes of defects (C-M).

# 3.2.2. Sensitivity Analysis 

Before proceeding to perform a sensitivity analysis, a strength-of-influence diagram was drawn (Figure 4), where arcs have different thicknesses, depending on the amount of impact that nodes exert on other nodes. It expresses the distance between various conditional probability distributions over the child node conditional on the states of the parent node [32]. To obtain this diagram, the Euclidean measure of distance between distributions was used [8], and the average distances were displayed.

From the strength-of-influence diagram, these are the most influential relationships:

- The influence of C-E8 on A-E3 is the strongest, associating the corrosion of metal elements with the appearance of corrosion stains [33,34].
- Then, vandalism (cause) is highly related to the observation of graffiti (effect) [35,36].
- The occurrence of mapped cracking (defect A-M4) is significantly influenced by the shrinkage of the render (cause C-A5) [37,38].
- The lack of follow-up activities when the render is curing or the existence of excessive construction moisture (C-E14/C-E7) reflects on the occurrence of cohesion loss/crumbling (A-M2) [39,40].
It is coherent that the most relevant influences are supported by the literature [33-41] since the inspection system of Sá et al. [23] is based on a review of the knowledge on the degradation of rendered walls and on the experience of experts.

The sensitivity analysis also contributed to the verification of the BN model. This type of analysis provides a visual perspective and helps to locate the most sensitive parameters, depending on the context (target nodes set). Six nodes were identified as targets, referring to the six most frequent defects in the samples of Sá et al. [19]: "A-E1 Graffiti", "A-E2 Dirt/particle deposits", "A-E4 Colour change/discolouration", "A-H1 Infiltration/damp stains", "A-H2 Biological colonisation" and "A-M3 Linear cracking". The colour scale of the diagram identified A-E1 (average sensitivity $=0.063$, maximum $=0.205$ ) and A-E4 (average sensitivity $=0.002$, maximum $=0.125$ ) as the most sensitive nodes. Still, in the set of first-level nodes, the age of the building was also identified as a significant sensitive node; i.e., it is important for the calculation of probability distributions in the nodes marked as targets.

Tornado diagrams were drawn for both "A-E1 Graffiti" and "A-E4 Colour change/ discolouration" (Figures 5 and 6, respectively). Such diagrams present the most sensitive parameters for a predetermined state of the target node. The length of each bar refers to the range of changes that a parameter can produce in the state of the target node. The red colour represents negative change, while green represents positive change.

In Figure 5, the tornado diagram representing the sensitivity of node A-E1 shows the impact of the combination of vandalism (C-U6) being true, a building being 28-35 years old, orientation towards the west, harsh rain-wind action exposure and low exposure to humidity. In fact, the only important condition in this set of characteristics is the occurrence of vandalism. However, as the combination of characteristics is always identified, they are all highlighted in this analysis. Vandalism (C-U6) being true is also present in two more parameters of Figure 5. The tornado diagram ranges from 0.576293 to 0.576963 , thus still referring to low levels of sensitivity.

The tornado diagram for colour changes/discolouration (A-E4), in Figure 6, shows in turn the relevant impact of the occurrence of natural wear and tear (C-M8), the building being 28-35 years old, orientation towards SW, harsh exposure to rain-wind action and low exposure to humidity. Still, the range of the diagram is only 0.00001 .

![img-3.jpeg](img-3.jpeg)

**Figure 4.** Strength of influence between the nodes of the BN. Both the use of dirty tools (C-E3) and the presence of water-soluble salts in water or construction materials (C-E4) have a significant influence on the occurrence of efflorescence/cryptoflorescence (A-H4) [37,41]; shocks/bumping (C-A2) has a strong influence on the occurrence of scratches or grooves (A-M5).

![img-4.jpeg](img-4.jpeg)

Figure 5. Tornado diagram analysing the sensitivity of "A-E1 Graffiti" (true $=58 \%$; red bars: negative change; green bars: positive change).


Figure 6. Tornado diagram analysing the sensitivity of "A-E4 Colour change/discolouration" (true $=81 \%$; red bars: negative change; green bars: positive change).

# 3.2.3. Case Study 

A residential building in Portugal was randomly selected to validate the proposed model. It was built in 1984 and has two floors and a floor area of $176 \mathrm{~m}^{2}$. The building's rendered façades were already subjected to maintenance actions (repainting), not including minor repairs in the render layer. The building has a reinforced concrete structure with ceramic brick masonry walls and a two-slope pitched roof with eaves. The windowsills are protruding elements on the façades, and they include a drip detail on their lower surface. The main façade (northeast) is only one floor high, as the lower floor is essentially a basement, with exterior walls northwest, southwest and southeast. Table 5 identifies the state of the evidence nodes for the case study building.

Table 5. Evidence for nodes related to the characteristics of the building, the façade and their exposure conditions, as well as cause C-U6.


Note: Selected nodes refer to known facts about the case study.
A technical inspection based only on visual observation was performed on the building with the mere purpose of identifying the occurrence of defects. The observed defects were:

- A-E2 Dirt/particle deposits
- A-H1 Infiltration/damp stains
- A-H2 Biological colonisation
- A-M1 Adhesion loss/detachment
- A-M3 Linear cracking
- A-M4 Mapped cracking
- A-M5 Scratches/grooves.

This set of defects should be compared with the prediction of the model, presented in Table 6.

Table 6. Defect occurrence results.


Considering the defects with a probability of occurrence higher than $50 \%$ (Table 6), only corrosion stains were not identified in the case study building. On the other hand, both mapped cracking and scratches/grooves were present in one or more surfaces of the case study, although the model only predicted a $34-37 \%$ and $28-33 \%$ chance of occurrence, respectively. Mapped cracking occurs on the northwest façade and was not repaired before repainting. The detected scratches/grooves are due to vehicle bumping next to the garage entrance.

Additionally, the causes of defects with a probability of occurrence higher than $50 \%$ in the BN model are (Figure 7):

- C-M1 Airborne dirt particles
- C-M2 Solar radiation/temperature action
- C-M3 Wind and/or rainwater action

- C-M4 Presence of water/water vapour
- C-M5 High relative humidity (RH $>70 \%$ )
- C-M8 Natural wear and tear
- C-U1 Irregular cleaning/washing
- C-U2 Irregular repainting

All these causes correspond to reasonably inferred causes of the detected defects. Nevertheless, some causes may be missing from the presented list, such as "C-A2 Shocks/bumping" ( $16 \%$ probability), "C-A5 Rendering shrinkage (17\%), "C-A6 Structural motions (settlement and deformation)" (6\%), "C-A7 Stress concentration/C-C5 Faulty design or lack of reinforcement systems for protection against mechanical action" (43\%) and "C-U4 Accidental actions related to user occupation, traffic and wear" ( $10 \%$ ). These causes mainly refer to mechanical action, requiring further tests for confirmation (e.g., tell-tale crack gauge); thus the high level of uncertainty may not be completely out of step with reality. Even so, the experience of surveyors could compensate for such high levels of uncertainty. Furthermore, some information observed on-site that is not included in the variables may also explain the high levels of uncertainty. C-U4 corresponds to an accidental cause that can only be confirmed by witnesses or a complete set of maintenance records. Hence, the sample of Sá et al. [19] and their inspection conditions may be limiting the BN model.
![img-5.jpeg](img-5.jpeg)

Figure 7. Defects detected on the façades of the case study: (a) moisture stains (highlighted in blue), biological colonisation (pink) and mapped cracking (orange); (b) moisture stains (blue) and loss of adhesion (green); (c) sirt deposits and loss of adhesion of the finishing coat; (d) linear cracking and biological colonisation; and (e) scratches/grooves.

# 4. Discussion 

Although uncertainty is inherent to the diagnosis of building degradation, depending on the amount and quality of available data, on the inspection methodology and on the experience and knowledge of the surveyor, the quantification of such uncertainty is not immediate. The methods used in this research allowed the authors to propose a model to measure uncertainty while assessing the degradation of rendered façades. The model was developed on the grounds of an existing building inspection system [19,23] based on expert knowledge and experience. The provided systematisation of deterioration mechanisms and

inspection data, following the best practices in the field [42], was a solid basis for the current study. Additionally, Sá et al. [19] provided thorough information on the characteristics of the inspected buildings and supplied a representative sample size. The variables selected as important attributes of the analysed built objects have also been considered by other authors that studied building pathology [43,44,45,46,47,48,49,50,51,52].

Nevertheless, as the sample [19] used to determine the CPTs was the same that had been used to validate the building inspection system [23], any minor incorrection not detected by those authors may have been transposed to the BN model. Additionally, that same sample does not have universal representativeness. Although it is representative of the Portuguese population of rendered façades, its applicability to other construction and environmental contexts may require further analysis, namely in terms of substrate materials (in the sample, masonry and concrete), the materials' content of mortars (cement, lime, water and admixtures), exposure to weather agents according to climatic features and current maintenance activities (in the sample, only the type of washes and its frequency were considered).

The proposed model supplies a graphical representation of quantitative and qualitative data that is easy to interpret, focusing on the cause-defect relationship. BN models have also been used by other authors with similar purposes, for instance, evaluation of maintenance scenarios [16], making predictive maintenance decisions [9,10], inspection planning in ships [53], damage assessment [54] and design-for-maintainability assessment of building systems [17]. Yet, to the best of the authors' knowledge, no other research has centred on the use of BN models to analyse the diagnosis process of building defects on rendered façades.

Nevertheless, the developed BN should not be viewed as a diagnosis guide, considering the probabilities as the basis for assuming the presence of defects or their causes. Instead, the proposed model should complement the in situ diagnosis process as an additional source of information or quantification tool. It should not be downplayed that an event with a $1 \%$ chance of occurrence may still be observed three times when the sample has 300 cases. So, if there is only a $1 \%$ chance of a rendered façade not presenting "A-E2 Dirt/particle deposits", surveyors should not assume that such defect is observed in all the façades they inspect.

The verification of the uncertainty estimates using data from a different inspection sample shows that the proposed model is valid, providing uncertainty levels consistent with the surveyor's diagnosis process. Additionally, a strength-of-influence diagram was drawn to identify the most influential relationships between nodes. Those relationships correspond to associations recognised in the literature as part of degradation mechanisms. Furthermore, to check which variables had the highest impact on selected target nodes [20], a sensitivity analysis was performed. It confirmed that the probability of occurrence of graffiti (A-E1) is more sensitive to changes in the state of variable vandalism (C-U6), while the probability of occurrence of colour changes/discolouration (A-E4) is more sensitive to changes in the states of natural wear and tear (C-M8), age of the building, the orientation of the façade, exposure to rain-wind action and exposure to humidity. These results are in line with studies on façade pathology [1,33,34,35,36,37,40,41,43,44,45,46,47,52].

The analysis of the case study highlighted that the detected defects had been predicted by the proposed BN model with reasonable levels of uncertainty, as only two of the detected defects had a probability of occurrence lower than $50 \%$. On the other hand, the most probable causes predicted by the model were likely to cause the detected defects, but some causes that could be identified during the diagnosis process had lower probabilities (between $6 \%$ and $43 \%$ ). Nevertheless, those high levels of uncertainty are justified by the need of further testing or additional information to confirm the occurrence of the selected causes.

Given the development of other inspection systems [42], and their validation in representative samples, the proposed model can be replicated for other building materials or elements, provided that the necessary adaptations are taken into account. Still, the

time/effort required to compute the BN model may limit the expected technological advance. The complexity of buildings in terms of variety of materials, elements and systems may also limit a wider scope of BN models in terms of degradation mechanisms, since it may be difficult to collect and use significant samples of information on all types of materials, elements or systems. Even so, Bayes' belief networks could still be built, considering the assessment of experts, estimating the probability of events [10,20].

Additionally, the proposed model could be extended with the inclusion of more variables and levels of analysis. For instance, the height of the building could be included as one of the properties of the rendered surface, and recommended in situ diagnosis methods and repair techniques could be included in a new (fourth) level of variables. That was not the case in the current research, because the proposed approach required an initial validation step, which is presented in this paper. The future inclusion of new variables in the network may expand its scope of interest.

With the possibilities provided by computer applications for building inspection [42,55-57], in the future, this network may be used to integrate data and provide more tools for surveyors during the inspection procedures. Furthermore, the integration of several BN models referring to the degradation of different materials may become a powerful instrument to relate degradation in adjacent elements or systems.

# 5. Conclusions 

Building inspection and diagnosis involves uncertainty while simultaneously analysing numerous variables. Although surveyors are normally conscious of that uncertainty, it is difficult to quantify it. Therefore, this paper proposes the development of a new BN model to quantify uncertainty in the diagnosis of defects and their causes during technical inspections. Rendered façades were used to develop the prototype model. Bayesian networks are a well-supported framework for uncertainty reasoning that allow constructing coherent probabilistic representations. Those conditional probabilities can be based on available databases with a large number of cases or on assessments of probability obtained from experts [20,22]. In this paper, a database was used.

The proposed model includes a well-structured and comprehensive representation of cause-effect relationships affecting building pathology in façade renders, offering a new approach/analysis to previously published data [19]. The model is limited to the main characteristics of the building, façade and their exposure; the causes of defects; and the defects that may be observed in rendered façades. Additionally, it represents a balance between complexity and computation time.

The probability distributions of variables were defined according to a dataset from the literature [19], thus representing a specific population (building characteristics and exposure conditions). Nevertheless, degradation patterns should be similar to those in other contexts.

The validation of results confirmed the model, as the estimates of uncertainty are a good depiction of the surveyor's reservations during the diagnosis process, as demonstrated by using cases from another sample and a new case study. In this way, the causes in the groups of design and execution errors were associated with higher levels of uncertainty, since information about the design and execution processes (often missing) may be required to establish causal relationships of defects to events at those initial stages. Additionally, some causes in the group of mechanical actions were also associated with high levels of uncertainty, since their identification may lack confirmation through the use of in situ tests.

Furthermore, the relative importance of different indicants, as revealed by a strength-of-influence diagram and sensitivity analysis, was supported by the literature about degradation mechanisms on rendered façades. In the model, expected relationships were clearly identified through the mentioned analyses, such as the influence of corrosion of metal elements on the appearance of corrosion stains, the influence of vandalism on the occurrence of graffiti and the influence of render shrinkage on the occurrence of mapped cracking.

The proposed model may help surveyors to provide better information to decision makers, thus promoting better repair and maintenance choices.

Future studies could include the replication of the proposed methodology for other building materials or elements, the extension of the model with more variables and levels of analysis and the integration of the model in building inspection computer applications.

Author Contributions: Conceptualisation, C.P., A.S. and C.F.; methodology, C.P.; validation, C.P.; formal analysis, C.P.; investigation, C.P.; resources, J.d.B.; data curation, C.P.; writing-original draft preparation, C.P.; writing-review and editing, A.S., C.F., J.d.B., I.F.-C. and J.D.S.; visualisation, C.P.; supervision, J.d.B., I.F.-C. and J.D.S.; project administration, A.S., J.d.B. and J.D.S.; funding acquisition, A.S. and J.d.B. All authors have read and agreed to the published version of the manuscript.

Funding: This research was funded by the Fundação para a Ciência e a Tecnologia (FCT; grant number PTDC/ECI-CON/29286/2017) and also by the FCT grant SFRH/BD/131113/2017.
Data Availability Statement: Restrictions apply to the availability of these data. Data was obtained from Sá et al. [19] and are available from the authors with the permission of Sá et al. [19].
Acknowledgments: The authors gratefully acknowledge the support of CERIS, from Instituto Superior Técnico, University of Lisbon.

Conflicts of Interest: The authors declare no conflict of interest. The funders had no role in the design of the study; in the collection, analyses or interpretation of data; in the writing of the manuscript; or in the decision to publish the results.
