# Risk Assessment for Transporting Ammonium Nitrate-Based Fertilizers with Bulk Carriers 

- Mehmet Kaptan

Recep Tayyip Erdoğan University, Department of Maritime Transportation and Management Engineering, Rize, Turkey


#### Abstract

Population growth has enhanced the need for agricultural products. Ammonium nitrate (AN)-based fertilizers are well known to increase product yield. Unfortunately, this type of fertilizer presents serious risks on account of its volatile nature. Accidents continue to occur despite international regulations and practices to eliminate or reduce risks arising from maritime transport to acceptable levels. In the present study, risks related to the transport of AN-based fertilizers were identified through root cause analysis of the M/V Cheshire accident. The relationships between the detected risks and probabilities were quantitatively evaluated using the Bayesian network method, and suggestions to prevent accidents caused by mistakes made during the transport of AN-based fertilizers were provided.


## Keywords

Ammonium nitrate, Dangerous good, Hazardous materials transportation, Bayesian network, Risk assessment

## 1. Introduction

Maritime transport generally features safety and pollution risks due to poor weather and sea conditions, local restrictions, human factors, and variable conditions. Reducing the risks of this type of transport to tolerable levels depends on the introduction and implementation of risk reduction measures. Comprehensive risk assessment is essential for every operation that takes place on board a ship. In this context, the risks of cargo should be evaluated prior to its transport [1-3]. In this study, the risks associated with the transport of ammonium nitrate (AN)-based fertilizers, which greatly impact food production, via bulk carrier were analyzed.
AN-based fertilizers are white crystalline salts produced at low cost from ammonium and nitric acid. These fertilizers are readily soluble in water and used as nitrogen fertilizers in agriculture because they provide a nourishing effect on plant growth [4]. The action time of this type of fertilizer is longer than that of other types of nitrogenous fertilizers [5]. According to a Food and Agriculture Organization of the United Nations report, approximately 153 million of the 243 million tons of fertilizer produced in 2015 is

AN-based fertilizer [6]. This type of fertilizer constitutes $2 \%$ of all cargo carried by bulk carriers [7]. However, this fertilizer also has high risk of fire, decomposition, and explosion when stocked in large amounts [8]. Details of the physical, chemical, and reactive properties, toxicity, and firefighting and first-aid measures of AN-based fertilizers are available in the literature [9-12]. However AN-based fertilizer accidents continue to occur. Over 70 accidents related to AN fertilizers have occurred in the last century [4]. Indeed, a recent explosion in Beirut linked to AN fertilizers resulted in the death of over 200. Among the fertilizerrelated accidents recorded recently, nine occurred during transport on a bulk carrier.
Risk analyses of tankers carrying dangerous liquid cargo [1], passenger ships [13,14], packaged dangerous cargo [15], electrical systems [16], main engines [17,18], and similar fire and explosion accidents are widely available in the literature. Babrauskas [4] examined the incidence of accidents due to AN-based fertilizers and found uncontrollable fires in all reported accidents. Thus, the author stated that the most effective approach to prevent such accidents is the elimination of factors

[^0]To cite this article: M. Kaptan, "Risk Assessment for Transporting Ammonium Nitrate-Based Fertilizers with Bulk Carriers." Journal of ETA Maritime Science, vol. 9(2), pp. 130-137, 2021.
${ }^{\text {C }}$ Copyright 2021 by the Journal of ETA Maritime Science published by UCTEA Chamber of Marine Engineers


[^0]:    Address for Correspondence: Mehmet Kaptan, Recep Tayyip Erdoğan University, Maritime Transportation and Management Engineering Department, Rize, Turkey
    E-mail: cptmehmetkaptan@hotmail.com
    ORCID ID: orcid.org/0000-0003-3304-4061

causing uncontrolled fires. The author also proposed two suggestions: formulate fertilizers by considering uncontrolled fire risks and build security measures that can address uncontrolled fires. Hadden et al. [19] investigated the fertilizer-related M/V Ostedijk accident, determined the circumstances contributing to the occurrence of fire, assessed the fire response errors, and made appropriate recommendations according to the accident investigation report. Watrobski et al. [20] investigated the problem of sustainable AN transport and found that the current international regulations created to ensure sustainable dangerous cargo transportation are insufficient. The authors used the characteristic object method to select the best scenario for sustainable transport and provided the most ideal transport options considering the factors of safety and transportation costs. Ettouney and El-Rifai [21] analyzed two AN solutions in terms of solubility data, flash point, and boiling point and listed the conditions that could increase the explosion probability of AN fertilizers; these conditions included high solution acidity, accumulation of stainless steel corrosion products, increased temperature, and lack of gas flowing [21].
In the present study, the Bayesian network method is used to analyze fire and explosion accidents caused by the transport of AN fertilizer on a bulk carrier. The rest of this article is organized as follows. Section 2 introduces the Bayesian method used in this study, section 3 describes the methodology, and section 4 provides a comprehensive qualitative and quantitative risk analysis to demonstrate the applicability of the proposed method. Finally, section 5 concludes this study and provides recommendations for future research.

## 2. Background

### 2.1. Bayesian Network

Bayesian networks are non-looped graphs used to model the relationships of set elements with an uncertain probability relationship among them [22]. Bayesian networks are probabilistic networks built on the Bayes theorem and enable researchers to make inferences on future incidents by analyzing previous events. Simply put, a Bayesian network is a model that explains the variables of a cluster and the qualitative relationships between these variables in a graphical manner and quantitatively calculates the probabilistic relationships between the same variables $[23,24]$.
Bayesian networks are composed of a graphical component, where the probabilistic relationships between variables are represented by means of nodes and arrows, and the conditional probability tables of the variables. The graphical component forms the structure of the Bayesian network
[25]. When two nodes are connected with an arrow, the node at the beginning of the arrow is called the parent node and the node at the end of the arrow is called the child node [26]. Figure 1 shows a Bayesian network consisting of variables A, B, C, D, and E. In this network, nodes A and B are the parent nodes of node C and root nodes. Node C is the parent of node E , and variable D is the child variable of variable B. The conditional probability distributions of the variables $P(A), P(B), P[C \mid A, B], P[D \mid B]$, and $P(E \mid C)$ are indicated in Figure 1. The absence of arrows between a variable in the network and another variable indicates that the variable does not have a probabilistic relationship with other variables in the network; thus, it takes place in the network with a marginal probability (unconditional probability) distribution.
![img-0.jpeg](img-0.jpeg)

Figure 1. Example of a Bayesian network structure

Variables in a Bayesian network are not restricted in terms of the number of children or parents they can have [27] and the use of sub-optimal strategies is essential in domains involving many variables. One approach is the generation of multiple approximate structures and then reduce the ensemble to a representative structure. This can be performed by using the occurrence frequency (on the structures ensemble. If the theory is extended to multiple events, the situations in which a B event can occur together with one of the discrete D events $\left(D_{1}, D_{2}, D_{3}, \ldots, D_{n}\right)$ are expressed as in equations 1-2 [26,28,29].

$$
\begin{aligned}
& \mathrm{P}\left(D_{i} \mid \mathrm{B}\right) \frac{P\left(A_{i}\right) P\left(B_{i} A_{i}\right)}{P(B)}, \mathrm{i}=1,2,3,4, \ldots, \mathrm{k} \\
& P_{i}\left(B_{j}=P\left(D_{1}\right) P\left(B_{i} D_{1}\right)+P\left(D_{2}\right) P\left(B_{i} D_{2}\right)+\ldots+P_{i} D_{k}\right) P\left(B_{i} D_{k}\right)=\sum_{i=1}^{k} P\left(D_{i j}\right) \cdot P\left(B \mid D_{i}\right)
\end{aligned}
$$

## 3. Methodology

This section introduces the Bayesian network constructed to analyze fire and explosion accidents caused by AN-based

fertilizers transported in bulk carriers. Figure 2 shows the flowchart of the proposed methodology. The main steps of the methodology are briefly described below.
![img-1.jpeg](img-1.jpeg)

Figure 2. Flowchart of the study

### 3.1. Definition of the Problem

The purpose of this section is to determine the causes of accidents and their occurrence conditions. The necessary data are first collected to reveal the variables causing accidents. Data can be obtained by different methods, as stated in previous studies [30-32]. For example, accident reports or databases may be studied. Surveys or indepth interviews with subject matter experts may also be conducted. Applying one or a combination of these methods may reveal all factors (variables) causing an accident and the relationships between these factors.

### 3.2. Bayesian Network Construction

Two methods, namely, expert opinion and data set learning, are used to create the graphical structure of the Bayesian network. Analysis of the graphical structure of the Bayesian network on the basis of expert opinion is not only probabilistic but also causal and explanatory. Moreover, analysis of the network on the basis of data set learning can ensure an objective network structure because the relationships between variables are established via numerical and statistical methods [33]. A graphical network structure showing the relationships between variables is created by one of these data sets. The nodes created in the network structure are also introduced in this stage.

### 3.3. Conditional Probabilities from Expert Judgment

The conditional probabilities of the nodes can be obtained from expert opinion and data set learning, as stated in the previous sections. If a data set that allows the calculation of
node conditional probabilities is not found in the study, it is a practical solution to obtain because of expert evaluation. Experts provide their opinion of each probability in the conditional probability tables of the nodes. Because the opinion of each expert participating in the study does not have the same weight, a weighted score is assigned to these experts. Suppose expert $i$ 's decision is represented by $x_{i}$. The following equation 3 is used to find the combined measure of expert judgments, $x[34]$.
$x=\omega_{1} \times x_{1}+\omega_{2} \times x_{2}+\omega_{3} \times x_{3}+\omega_{4} \times x_{4}+\omega_{5} \times x_{5}$

$$
=\sum_{i=1}^{5} w_{i} x_{i}
$$

Each $\omega_{n} \mathrm{i}(\mathrm{i}=1,2, \ldots, 5)$ normalized expert's weight is expressed as $\sum_{i=1}^{5} \omega_{i}=1$.
The background and assigned weights of the five experts who participated in this study are briefly explained below.
Expert 1; worked as a captain on bulk carriers for approximately 7 years. Today, he is an academician who completed his Ph.D. on shipping risks. The weight value assigned to this expert is 3 (range, 1-5).
Expert 2; is an oceangoing masteral student with a total of 25 years of service on bulk carriers. Because this expert has loading experience on AN-based fertilizers, the weight value assigned to this expert is 4.
Expert 3; works as a chemistry professor at a university and has published several SCi articles on inorganic chemistry. Therefore, the weight value assigned to this expert is 5.
Expert 4; has worked as a chemist for 10 years in the laboratory of a factory that produces AN-based fertilizers. The weight value assigned to expert is 1.
Expert 5; is an oceangoing master with a total of 25 years of service on bulk carriers. Thus, the weight assigned to this expert is 2 .

### 3.4. Verification of the Bayes Network

Axioms tests are used to confirm that the Bayesian network is built correctly and working as designed [34]. Requests for axiom tests must be met by the Bayesian network for the latter to be considered valid. Tests of the following axioms were applied to the Bayes network established in this study. Axiom 1: The change in probability of each parent node would cause a relative change in the probability of the child node. Axiom 2: Considering the probability distributions of each parent node, their impact on the child node values should be consistent. Axiom 3: The combined effects of a child node with more than one parent node on the probability values of the parent nodes are always greater than the individual effects [35].

### 3.5. Sensitivity Analysis

Sensitivity analysis determines whether any variable (node) in the network is sensitive to the difference in the status of any other variable in the network [36,37]. Sensitivity analysis results are usually represented as deviation values. Deviation values are defined as an expected decrease/ increase in the selected output variable depending on the value of the input variable [38]. The input variable, which is determined to have the highest variance reduction value due to the analysis made on this variable, is expected to shift the probabilities for the conditions of the target variable toward the maximum value. In other words, how changes in the inputs (i.e., root node, parent node) of the Bayesian network will affect the output (i.e., child node) is calculated in the network. In this study, the outputs of the network are the probability of explosion accidents caused by ANbased fertilizers. The inputs are defects that play a role in the occurrence of the accident. The GeNIe software package was used for the axiom tests and sensitivity analysis [39].

## 4. Application

The proposed methodology was applied to an actual maritime accident; specifically, the M/V Cheshire accident was selected to conduct a comprehensive risk analysis. The M/V Cheshire bulk carrier sailed from its loading port in Norway on 6 August 2017 to Thailand with a load of ANbased fertilizers. A bad odor and dust, pressure, and water accumulation were observed when the hatch cover drains were opened 3 days into the voyage. The ensuing accident resulted in the complete loss of the ship because these signs and the accompanying increase in hatch temperature were not interpreted correctly by the ship's personnel; thus, intervention was delayed [40].

### 4.1. Establishing the Bayesian Network Structure

The causes of the accident and the relationships between these causes were determined on the basis of the M/V Cheshire accident. Thus, a tentative network structure was formed. The final form of the network structure was decided by considering the experts' opinions on the network structure. The Bayesian network in this study consists of 11 nodes in total (Figure 3). Information about these nodes is given below.

## Cargo Declaration

According to SOLAS Chapter VI rules 1 and 2, the shipper is obliged to inform the captain about the cargo before loading, as specified in International Maritime Solid Bulk Cargoes (IMSBC) code rule 4. The cargo must be packed properly and transported safely. This node considers causes of inappropriate reports.

## Heat Source

A heat source is necessary to initiate the decomposition of AN-based fertilizers. Thus, operations involving welding, burning, or cutting and equipment that could generate fire, open flames, or sparks should not be performed near the cargo hold containing this cargo, except for emergencies. This node considers improper practices performed by the ship's crew.
![img-2.jpeg](img-2.jpeg)

Figure 3. Bayesian network structure for Ammonium nitrate (AN)-based fertilizer-induced explosion

## Previous Cargo

Cargo holds in which AN-based fertilizers are to be loaded should be washed with salt and fresh water and free of previous load residues. This node considers improper practices of seafarers.

## Adequate Separation

The compatibility of AN-based fertilizers with other cargo loaded in the same cargo hold should be considered prior to loading. Bulk carriers must be arranged, equipped, or approved to transport AN-based fertilizers in their hold. This node considers non-conformities to established practices and requirements

## Monitoring (True action)

AN-based fertilizer decomposition shows observable and measurable signs, including a decrease in the atmospheric oxygen content of the cargo hold, water accumulation in the hatch cover channels, effluvium, temperature increases, and fume formation. This node considers the crew's misunderstanding of the signs observed and improper actions.

## Decomposition

AN-based fertilizers can be chemically decomposed upon exposure to heat. This node considers the probability of decomposition occurring.

## Combustible Material

AN does not burn, but it is an oxidizing agent and, therefore, can support combustion [8]. The presence of flammable materials is necessary to produce a fire involving AN. This node considers the inconveniences caused by the combination of AN-based fertilizer and flammable materials.

## No Damage (Only dusk)

This node considers the level of damage sustained by the ship following appropriate action by the ship's personnel when the separation of AN-based fertilizers begins.

## Fire/Hot Spot

This node reflects the possibility of fire caused by a fertilizer based on AN.

## Fire Extinguishing

A suitable extinguishing medium for AN-based fires is water. The use of other extinguishing materials (e.g., foam, carbon dioxide) is useless in firefighting this type of fire and even encourages decomposition. This node considers the operational errors made within the ship.

## Explosion

AN-based fertilizers can explode under certain conditions that require a strong start-up source. This node considers the possibility of explosion.

### 4.2. Axiom Test

The axiom 1 test was implemented over the entire Bayesian network constructed in this study, and a sample application was carried out using the Fire/Hot spot node. Parent nodes affecting the formation of this node include the monitoring (true action), decomposition, and combustible material nodes. When the individual negative statements of the parent nodes of the Fire/Hot spot node are 100\%, the probabilities of Fire/Hot spot formation are $3 \%, 22 \%$, and $5 \%$, respectively (Table 1). This result confirms that an increase in the probability of each parent node causes an increase in the probability of the child node; conversely, a decrease in the probability of each parent node causes a decrease in the probability of the child node. All of the results obtained show that the Bayesian network fulfills the test requirements of axiom 1. Thus, the Bayesian network created is compatible with the axiom 1 test.

Table 1. Results of the Fire/Hot spot node-based axiom 1 test


The axiom 2 test was conducted on the Fire/Hot spot node; here, a gradual increase in the parent nodes independently for example, $10 \%, 20 \%, 30 \% \ldots .100 \%$ ) caused the probability of the child node to increase gradually. This finding indicates that a gradual change in the probability distribution of the parent nodes exerts a consistent effect on the child node. Thus, the Bayesian network complies with axiom 2 requirements.
According to the axiom 3 test, when $100 \%$ independent negative probabilities of the parental nodes of the Fire/Hot spot node are selected, the probability values for the "observed" state of the Fire/Hot spot node are 3\%, 22\%, and $5 \%$, respectively. When these three parent nodes are given $100 \%$ negative probabilities, the probability value (observed) of the Fire/Hot spot node is $100 \%$. The results obtained are consistent with the axiom 3 test. The axiom 3 test was also applied to all intermediate nodes, and results

consistently indicated that the Bayesian network fulfills axiom 3 requirements.

### 4.3. Sensitivity Analysis

In the sensitivity analysis, the probability of the Explosion node was changed to $0 \%$ and then $100 \%$ by using the GeNIe program. No change was made to the probabilities of other nodes in the network. The change in the probability values of the nodes was then examined, and the effects of the causes (nodes) of explosion accidents due to AN fertilizer on the occurrence of these accidents were quantitatively calculated using the Bayesian network created in this study. Table 2 shows the sensitivity analysis results.

## 5. Results and Discussion

The Bayesian networks created in this study demonstrate the factors causing the explosion of AN fertilizers and the relationships among these factors. Users of the network can understand the occurrence of AN fertilizer explosion and predict the risk of explosion when several factors are present in the environment. Nodes that stand out according to the results of the explosion sensitivity analysis include heat source ( $93 \%$ ), combustible material ( $32 \%$ ), Fire extinguishing ( $25 \%$ ), and monitoring (true action) (17\%) (Table 2).

The root cause of explosion accidents was determined to be heat source. Decomposition of AN-based fertilizers may occur via two ways: Thermal decomposition and self-sustaining decomposition (SSD). In the case of thermal decomposition, removing the heat source from the environment may be sufficient to prohibit further decomposition. However, even if the heat source causing thermal decomposition is removed, sufficient heat may remain in the material because of chemical reactions, which give rise to SSD [10]. In this case, the size of the heat source to which the cargo is exposed, the exposure time of the cargo, and the tendency of the cargo to under SSD must be assessed [41]. The decomposition tendency of the load is determined by the trough test specified in the IMSBC code. The risk of cargo degradation is significant at temperatures exceeding $170^{\circ} \mathrm{C}$ [8]. Thus, internal heat sources (welding, naked flame, electrical equipment etc.) must be kept away from the cargo. The temperature inside the hold may also increase due to the heat of the area in which the ship is located. The importance of heat sources has been emphasized in previous studies [2,21].
Besides keeping heat sources away from the cargo, strict observation of the condition of the cargo may be an effective approach to avoid explosion accidents. Accident investigation reports often reveal a lack of understanding of the signs of decomposition during the transport of cargo,

Table 2. Sensitivity analysis results of AN-based fertilizerinduced explosions


as well as incorrect action due to the lack of information. When accidents in vessels such as the M/V Purple Beach and M/V Cheshire were examined, strain due to pressure, effluvium, and water accumulation were observed when the hatch cover drains were opened within the first days of sailing. However, these signs were ignored by the ship's crew. Subsequent interventions were thus insufficient, and the ensuing accidents resulted in the complete loss of the ships [40,42]. Given these reports, all crew members must have detailed information on the need for hold cleanliness, cargo hazards, stowage and segregation, loading, weather, carriage precautions, and discharge on ships carrying ANbased fertilizers.
Another important factor in the formation of AN-based fires and explosions is material combustion. AN-based fertilizers are not combustible but are self-oxidizing [43], which could promote combustion. Fertilizers are very sensitive to the residues of flammable materials, such as coal, grain, sawdust, and petroleum [44].Therefore, personnel should remove cargo residues and prepare appropriate stowage plans. Structural equipment, such as hatch covers and bulkheads, should meets the standard requirements of the ship. Baalisampang et al. [45] indicated that detailed risk assessment should be performed to minimize human and organizational errors.

The last node within the scope of this study is the fire extinguishing node. Fire extinguishers suitable for the burning cargo must be available to address fires. The appropriate firefighting methods are listed in the sources as follows. If the deterioration area is small and easily accessible, it can be removed from the main body by using a digging shovel; local extinguishing with water can then be performed. However, if the deterioration area cannot be removed, the area should be sprayed with water by using a high-pressure jet as quickly as possible. Other firefighting methods, such as spraying with foam and carbon dioxide or covering the area with non-combustible materials, are useless and may even encourage decomposition. The amount of water used to stop decomposition should not disturb the stability of the ship $[46,47]$.

## 6. Conclusion

The development of agriculture and increasing demands for mineral fertilizers have caused the transport of ANbased fertilizers to intensify. Sea transport is prominent in the shipping of this type of fertilizer because this mode of transport is inexpensive. Several factors should be considered when transporting AN-based fertilizers because of their inherent and ship-related risks. The network obtained in this study contributes to the literature by providing a means to predict the probability of fire and explosion accidents caused by AN-based fertilizers. Some recommendations to prevent such accidents are as follows.

- Risk assessment procedures should be developed to identify and eliminate heat sources that may cause decomposition.
- A standard operating procedure that allows communication between the captain and fertilizer specialist during the ship's voyage should be established.
- A monitoring logbook that could track the signs of decomposition, such as odor, dust, and water accumulation, should be prepared.
- SSD may be inhibited by delivering water to the reaction zone. Thus, the availability of three different fog lances on ships carrying AN-based fertilizers as cargo, depending on the height of the ships' holds, should be made mandatory.
Future researchers may focus on the effects of human error on fertilizer-related accidents. Further studies estimating the probability of human error are recommended to provide decision-making support to operational stakeholders.

