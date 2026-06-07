# Article 

## A Decision Support System for Sustainable Agriculture and Food Loss Reduction under Uncertain Agricultural Policy Frameworks

Martine J. Barons ${ }^{1, *}$, Lael E. Walsh ${ }^{2}$, Edward E. Salakpi ${ }^{3}$ and Linda Nichols ${ }^{1}$

check for updates

Citation: Barons, M.J.; Walsh, L.E.; Salakpi, E.E.; Nichols, L. A Decision Support System for Sustainable Agriculture and Food Loss Reduction under Uncertain Agricultural Policy Frameworks. Agriculture 2024, 14, 458. https://doi.org/10.3390/ agriculture14030458

Academic Editor: Christos Karelakis
Received: 23 November 2023
Revised: 2 February 2024
Accepted: 8 February 2024
Published: 12 March 2024

## 0

Copyright: (c) 2024 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 Department of Statistics, The University of Warwick, Coventry CV4 7AL, UK; l.nichols@warwick.ac.uk
2 Horticulture Development Department, Teagasc Ashtown Food Research Centre, D15 DY05 Dublin, Ireland; lael.walsh@teagasc.ie
3 Biological and Environmental Sciences, University of Stirling, Stirling FK9 4LA, UK; edward.salakpi@stir.ac.uk

* Correspondence: martine.barons@warwick.ac.uk

Abstract: The EU Green Deal requires the reduction in pesticides and fertilisers in food crop production, whilst the sustainable development goals require reductions in food loss and food waste. In a complex and interacting system like the food system, these goals are difficult to coordinate. Here, we show an approach using Bayesian network modelling for decision support. Bayesian networks are important tools for modelling complex systems which may develop emergent behaviour and for providing quantitative comparisons for different candidate policies, approaches or interventions under the Integrating Decision Support System paradigm. Using lettuce as an exemplar crop, we demonstrate that expected food loss changes under different agricultural input reduction and integrated pest management combinations can be quantified to aid decision making for growers.

Keywords: Bayesian networks; integrated pest management; EU Green Deal; sustainable development goals; Integrating Decision Support Systems

## 1. Introduction

As human populations continue to grow, so does the demand for food, increasing pressure on finite land resources. Fertilisers, pesticides and other agricultural inputs have been used successfully to reduce food lost to pests and diseases, and so maximise yield. Such losses present a significant threat to food production [1,2] and are mitigated by crop protection measures. These measures, in the form of conventional pesticides (increasingly replaced by biopesticides in certain systems [3,4]), have been utilised as a key tool to ensure good yield and productivity [5]. Integrated pest management (IPM) may be widely interpreted in different agricultural contexts [6]; however, it tends to be regarded as a decision support system for selecting and implementing pest control tactics [7] in a way that minimises crop loss and negative externalities. In the European Union, IPM has been adopted in response to the intensification of pesticide use and is regulated through the Sustainable Use of Pesticides Directive 2009/128/EC [8,9].

The announcement of the Green Deal by the European Union (EU) in 2019, with a focus on significantly reducing pesticide and fertiliser input by 2030, presents a serious challenge to food production, particularly for fresh vegetable production, where high value is placed on quality [10]. In these systems, insights into management strategies and assessments of crop protection decisions are still lacking [11].

With road maps for input reductions under the EU Green Deal yet to be decided for specific crops, food producers find themselves in a situation of decision making under considerable uncertainty. Modern IPM is regarded as a continuously improving process to innovate, integrate and adapt locally, and it is becoming increasingly integrated into

sustainability efforts at the farm level [6]. The Voluntary Initiative [12] in the UK is an industry-led programme to support IPM standards and implementation by farmers.

A review of available decision support tools in an IPM context [13] does not mention models focused on crop loss due to pesticide reductions, suggesting that this may be a research gap. Here, a proof-of-concept approach using Bayesian network modelling is presented, using lettuce as the exemplar crop. This approach supports smarter decision making using digital tools, in the context of more sustainable crop protection inputs in vegetable production systems. Importantly, it displays how large data sets, pesticide use information and domain expertise can be combined for decision making and applied in a specific case study. Useful baseline Structured Expert Judgement data are generated as a reference point for future IPM and sustainable crop protection programmes, and the impact of IPM implementation on crop loss under different production scenarios is demonstrated.

# 1.1. Food Loss 

Food loss is a decrease in the quantity or quality of food due to decisions and actions in the supply chain prior to reaching retailers or service providers [14]. The sustainable development goals (SDGs) call for halving per capita global food waste at retail and consumer levels by 2030, as well as reducing food losses along the production and supply chains. As the use of agricultural inputs has been critical to delivering the productivity required of available agricultural land, including controlling food loss rates, achieving the goals of food loss and waste reduction with simultaneous agricultural input reduction will be a challenging task. A particular challenge lies in the fact that production systems (including crop breeding, variety selection and current conventional agronomic practices) have proceeded in partnership with agricultural input development. Evolving regulatory pressures and weather uncertainty due to climate change add to the difficult context of grower strategy. This makes food loss reduction, whilst also meeting the EU Green Deal requirements for reduced agrochemical inputs, a critical problem in the context of the rising need for human nutrition.

### 1.2. EU Green Deal

The EU Green Deal is a set of proposals adopted by the European Commission to make the EU's climate, energy, transport and taxation policies fit for reducing net greenhouse gas emissions by at least $55 \%$ by 2030, relative to 1990 levels. The EU Green Deal is important for sustainable food production; it is Europe's strategic response to climate change and environmental degradation and presents a vision for key policy measures to transform the economy and society in a more sustainable way. It focuses on 11 key elements. One of them is 'Farm to Fork': designing a just, healthy and environmentally sustainable food system. Clear targets have been set for agrochemical input reduction by 2030: growers will need to reduce pesticide use by $50 \%$ and fertiliser use by $20 \%$. There is no clear path to achieve these cuts without increasing food loss and waste, in direct opposition to the relevant SDGs, and reducing food availability for the human population. IPM is understood to be a holistic approach to addressing plant pests and diseases using all available methods, whilst limiting the application of synthetic chemical pesticides [15,16]. However, the crop protection equivalence of IPM techniques replacing chemical use is still unclear, as the robustness of strategies which focus on IPM have achieved mixed results [17]. Growers and policy makers will need help to make evidence-informed decisions to balance the interacting pressures they face.

### 1.3. Lettuce Growers

By working with lettuce growers, we designed a decision support system for growers to identify the food loss effects of actions to reduce fertiliser and pesticide input. Lettuce production provides a good case study because it has a short growing season, so many crops are grown and harvested in the same calendar year, under similar conditions. Lettuce has no secondary market; it is too watery for bio-digesters and cannot be frozen, making it

more prone to waste. Engagement with horticulture growers has highlighted that pressure to reduce agrochemical inputs poses a serious risk of increasing food loss, which is likely to impact the economic and environmental sustainability of their enterprises [18]. Operating a successful enterprise in horticulture requires meeting the challenge of delivering sufficient and consistent yields whilst ensuring the marketing of aesthetically appealing products [19]. These production parameters have implications for the continued supply of nutritious food and for achieving food security [19]. Additionally, current systems of production and agronomic decision making (crop varieties, drilling techniques, rotations, integrated pest management approaches) are tailored towards intensive farming practices which operate coherently with agrochemical inputs. Pivoting to a system that encompasses lower inputs will require considerations and decision making across the growing system to evaluate how variables interact and influence each other.

# 1.4. Lettuce Production and Decision Support Systems 

Lettuce (Latuca sativa L.) grows well in fertile well-structured soils. The main types are crisphead, butterhead, looseleaf (e.g., batavia, oak leaf lettuce) and romaine [20], with seeds sown in glasshouses or polythene tunnels ahead of transplanting them into the field. Consistent temperature, irrigation, relative humidity, pH and electrical conductivity together with fertilisation (NPK) are necessary for growth [21]. Several pests and diseases may affect lettuce during production, leading to higher levels of food loss [20]. These include bacterial diseases (e.g., Pseudomona and Xanthomonas species cause leaf spotting), fungal diseases (e.g., downy mildew, moulds and rot, many of which are soil-borne and show seasonal variation) and pests (aphids, moths, leaf miners, slugs and whitefly may cause feeding damage or transmit plant viruses). Decision support rules and models facilitate the use of a combination of techniques (including pesticides) to control pests and diseases [20]. Challenges relating to real-world use include accessing commercial data to validate and improve models [22] and little continued adoption due to the complexity of the models [23]. The limitations of these models include inaccuracy in capturing late-season trends at higher latitudes or inaccuracy due to slower growth rates [22].

### 1.5. Bayesian networks for Agriculture

Bayesian networks (BNs) are particularly suited to agricultural research as they represent explicitly the relationships between factors in a system, incorporate new evidence as it becomes available and demonstrate changes in outcomes when either new circumstances arise or when new interventions are enacted [24]. This allows proposed new interventions and scenarios to be tested to see what effects they are likely to have on outcomes ahead of implementation or occurrence. Another key strength is the ability of BNs to use probability distributions to incorporate, in a robust and defensible manner, the inevitable uncertainties associated with the impact of variable factors on each other. The qualitative structure of the BN, representing the relationships, can be learned from data, where suitable data exist, or elicited from the problem owner with other experts. Elicitation is always an iterative process [25], involving the identification of factors, relationships and probability distributions, and formalised processes have recently appeared [26]. The relationships between the variables can be correlations, causal or beliefs, and the strength of these relationships can be represented [27]. The outcomes can be expressed as multi-attribute utilities [28], reflecting the priorities of decision makers. The mathematical constraint that BNs must be Directed Acyclic Graphs (i.e. have no feedback loops) can be easily overcome where a relevant separation of timescales can be defined, allowing a Dynamic Bayesian network (DBN) to be constructed [29]. There have been a number of instances of BN implementation related to automated monitoring in agriculture, including the monitoring of animal livestock [30], crops [31], natural resources [32] and storage environment control [33]. The decisions supported were treatment regimes for mastitis in cattle, swine fever in pigs [34] and tropical diseases in bovine herds. The ability of BNs to make inferences has been leveraged to predict crop yields, disease evolution, disease transmission, weed infestations, pollution po-

tential, the viability of farming businesses, breeding strategies, crop disease and agricultural policies [24]. In causal BNs, it is possible to trace back the causes of emergent problems, including disease transmission, pollution, antibiotic resistance, weed invasion, pests and parasites, farmer engagement and plant growth [24]. There are implied decisions which will be informed by these BN applications; BNs can be designed to be decision support tools directly. Examples include medical interventions, herd management, energy demand, land management, and pollution and crop management [24]. Section 2 introduces statistical decision support, Bayesian networks and Structured Expert Judgement. We then describe the data and sources, how the model was developed and the data incorporated. Section 3 gives the results of the SEJ exercise and the outputs of the model under a range of scenarios. The conclusion discusses the results in context and elucidates the strengths and limitations of the research. Appendix A contains images of the model outputs.

# 2. Materials and Methods 

A novel paradigm for decision support for large, interconnected systems was introduced by researchers [35,36], in which the authors showed that expert judgements from disparate panels of experts (often themselves informed by huge data sets and large, complex models) can be combined to provide a robust and coherent decision support system capable of scoring candidate policies (typically, combinations of actions). The eventual aim of this research is to provide such a decision support system for horticulture. In this paper, we show how a constituent decision support system can be constructed for a single crop. With such a model for each crop, an Integrating Decision Support System (IDSS) for the sector can be designed as described in [35,36] to deliver an evidence-based decision support system for horticulture or agriculture more widely.

### 2.1. Bayesian Networks

Bayesian networks (BNs) [37] are a statistical model comprising the set of factors of influence in the system (random variables, represented as nodes) and the relationship of influence between them (arrows or directed edges, see Figure 1). BNs and dynamic BNs are particularly suited to the role of decision support as they represent the state of the world as a set of variables and model the probabilistic dependencies between the variables [38,39]. When built on the knowledge of domain experts, as in this case, they also provide a narrative for, or represent an understanding of, the system and can be transparently and coherently revised as the domain changes. BNs are one type of probabilistic graphical model, where the nodes represent discrete or continuous variables and the directed arcs represent direct connections between variables, which may be causal or represent causal beliefs. The direction of the arrow indicates the direction of the effect [39].

A Bayesian network is formally defined as a directed acyclic graph (DAG) together with a set of conditional independence statements having the form A is independent of B given C , written as $A \perp B \mid C$. They are a simple and convenient way of representing the factorisation of a joint probability density function of a vector of random variables $\mathbf{Y}=\left(Y_{1}, Y_{2}, \ldots, Y_{n}\right)$. The joint density of $\mathbf{Y}$ may be written as

$$
f(\mathbf{y})=\prod_{i \in|n|} f_{i}\left(y_{B_{i}} \mid y_{\Pi_{B_{i}}}\right)
$$

where $\Pi_{i}$ represents the indices of parents of $Y_{i}$.
Each node has a conditional probability distribution, which, in the case of discrete variables, will be conditional probability tables (CPTs). see Figure 1) for an example of a CPT. Root nodes have simple CPTs as they only contain the prior or marginal probabilities. The downstream nodes have more complex distributions, with nodes having a large number of parents (direct connections leading into them) with very large CPTs which may be difficult to populate either from data or using Structured Expert Judgement (see Figure 1). If it is desirable to reduce the number of parents (perhaps to speed up computation or reduce expert burden in SEJ elicitation [40]), intermediate latent summary nodes can be used. For

example, rainfall, hours of sunshine and temperature might be combined into categories of weather conditions such as favourable or unfavourable.

BNs can capture linear and non-linear relationships and can pass uncertainty in one variable to another to correctly quantify the uncertainty in the outcome.
![img-0.jpeg](img-0.jpeg)

Figure 1. An illustrative directed acyclic graph (DAG) depicting parent nodes A and B and a child node $C$ with example conditional probability tables (CPTs) for nodes $A$ and $C$. Node $D$ represents the decision node.

# 2.2. Structured Expert Judgement 

Structured Expert Judgement (SEJ) elicitation is a robust and defensible method for producing evidence for policymakers. The use of expert advice and opinion to support policy decision making is commonplace, but generally, the manner in which contributions are synthesised to inform the eventual decision is not transparent. Where informal heuristics and elicitation are employed, experts are subject to a number of well-documented biases: social biases, deferring to the member with the most compelling personality or credentials or who is perceived as the most senior; bias towards the most readily available information; and misunderstandings due to semantic differences [41,42]. The results of such unstructured approaches are often not reproducible and can be unreliable and heavily biased. These difficulties can be significantly reduced by using structured approaches designed to mitigate the most pervasive and debilitating psychological and contextual frailties of expert judgement [43-46].

Structured elicitation of expert opinion in pursuit of decision support is an increasingly important technique and is widely used by the European Food Standards Agency (EFSA) in making risk assessments [47]. Other examples include assessments of health risks [48], household food security [49] and to quantify uncertainty in the risks of herbicide-tolerant crops [50]. Validated protocols for SEJ fall into three broad categories based on how they aggregate the individual contributions of experts into a single estimate: behavioural aggregation (seeking consensus); mathematical aggregation (combining individual estimates using a formula); and mixed aggregation. There are several well-established methodologies for SEJ elicitation protocols, each with its own strengths and limitations [47]. The recently-developed IDEA elicitation protocol [51] combines the strengths and ameliorates some limitations of older methods. The acronym IDEA arises from the combination of

the distinctive features of the protocol: it encourages experts to investigate and estimate individual first-round responses, discuss the anonymised version of those responses, and estimate second-round responses, following which judgements are combined using mathematical aggregation. It is an extension of Cooke's classical method, which does not have the facilitated discussion or second round estimates [52]. In the development of the current decision support system to identify and inform potential intervention decisions across the range of food loss determinants, there were no data to quantify food loss percentages under fertiliser and pesticide reduction as ameliorated by a range of integrated pest management actions. Therefore, a SEJ elicitation using the IDEA protocol was employed to fill this data gap.

# 2.3. The SEJ Workshop 

Since SEJ involves a combination of expert judgement, diversity of experts is more important than large numbers. Greater than fifteen experts does not significantly improve the findings, but fewer than five may reduce the chance of providing adequate diversity in opinions [47]. Eight experts initially agreed to participate in the elicitation process in an online workshop and were sent the participant information as given in our successful ethical approval application, outlining the IDEA protocol and the role played by them as experts. On the day, four experts attended the workshop, where the IDEA protocol was explained again. When we moved into the elicitation session itself, all but two left the online meeting without explanation. We were able to find an additional two experts, who had been presented with the protocol outline during the planning stages. This gave us estimates for four experts altogether. However, they did not have the capacity to attend the facilitated discussion element, so we reverted to Cooke's protocol for SEJ, which does not include this element. The final four participating experts were employed in horticulture training (1), research (1) and advisory services (2) and included two females and two males. Whilst a decision maker may wish to re-run the elicitation with a larger group before using the full model for decision support, we are satisfied that the diversity in the experts' backgrounds, experience and perspectives is rich enough for this proof of concept. The experts were asked for their estimates of the percentage change in expected crop yield under scenarios of varying IPM, fertiliser use and pesticide use. They were asked to give their lowest plausible estimate (interpreted as 5th percentile), highest plausible estimate ( 95 th percentile) and best estimate ( 50 th percentile) of the change in crop yield.

### 2.4. Data

The data for each of the nodes were obtained and transformed as necessary. Details of sources can be found in the Table 1.

Table 1. A table showing the sources of the data used for building the Bayesian network. FERA pesticide usage survey data: https://pusstats.fera.co.uk/home, accessed on 16 March 2021.


The pesticide application rate data for the fungicide, insecticide, herbicide and molluscicide were each discretised into three levels, as shown in Table 2. The application rates in each category were then matched with each of the pesticide use reduction scenarios from the SEJ and their corresponding reduction in fertiliser use and percentage change in yield.

The scenarios of the reduction in pesticide and fertiliser use were set to $10 \%, 25 \%$ and $50 \%$ and $5 \%, 10 \%$ and $20 \%$ respectively.

Table 2. A table showing the pesticide application intervals and categories used for the Bayesian network.


There were no data available for changes in food loss given changes in integrated pest management, fertiliser and pesticide use and application rates; thus, a binary node was used for the IPM node in the BN where 'Unchanged IPM' was set to 'No' and 'Increased IPM' set to 'Yes'.

The change in crop yield from the SEJ (see Table 3) is referred to as yield loss in the BN. The percentage changes in crop yield were also discretised into five categories and labelled as 'Very Low' ( 0.0 to $-8.5 \%$ ), 'Low' ( -8.6 to $-13.5 \%$ ), 'Medium' ( -13.6 to $-17.5 \%$ ), 'High' ( -17.6 to $-22.5 \%$ ) or 'Very High' (greater than $-22.6 \%$ ). Note that these losses are in addition to the average $10 \%$ loss.

# 2.5. Model Development 

The Bayesian network was constructed with the assistance of domain experts and the published literature. Using our contacts in the lettuce growing community, we were able to harness expertise in the domain to describe the lettuce system, its important constituents and the relationships between them, as described in [25]. This was an iterative process of sharing understanding, where BN analysts represented their understanding of the experts' explanations in the qualitative structure of a BN, and then, the domain experts discussed the veracity of the representation. This was validated through repetition until the experts were satisfied that the qualitative BN structure accurately represented the dynamics of the system at appropriate granularity, a process called Soft Elicitation [53]. We also ascertained what growers' goals are and what decision support needs are required in relation to the EU Green Deal.

Having ascertained what the parameters should be from the experts and literature, we sought to quantify the model with relevant probability distributions. As described in detail above, these were derived from data wherever possible, using growers' expertise to identify relevant sources of data. Where suitable data could not be obtained, an SEJ exercise was held with growers, horticultural advisers and other relevant experts to derive the missing probability distributions, as described in detail above. The data from both sources were used to construct conditional probability tables, as shown in Figure 1 and Table 3, where the 50th percentile value was used.

Table 3. Aggregated estimates of change in expected crop yield from three experts.


The prototype BN initially conceptualised for this project can be seen in Figure 2. However, due to the challenge with data availability, some nodes were dropped and a modified BN structure in Figure 3 was used for this proof of concept. The Growing Environment, for instance, was a latent node to be derived from the inherent clusters within a combination of pesticide fertiliser application rate, IPM and weather condition. Indeed there are specific pest case studies indicating that IPM tactics impact the soil environment. Our initial models set out to include soil data. However, the available data were typically at a very high resolution and focused on physical parameters and soil classification. Soil data relating to chemical and biological properties are not yet widely available; therefore, it was decided that the node relating to soil should be removed in an effort to focus on nodes where robust data were available to use, thus allowing us to demonstrate our proof of concept. Also, due to the lack of data on IPM and its interaction with weather conditions, this element was omitted.
![img-1.jpeg](img-1.jpeg)

Figure 2. The BN model derived from interaction with multiple domain experts.

The prototype of the BN used for this work (Figure 3) was developed with GeNIe Modeler by 'BayesFusion' (Available from http://www.bayesfusion.com/ accessed on 11 March 2024).
![img-2.jpeg](img-2.jpeg)

Figure 3. The BN model structure used for this proof of concept.

# 3. Results 

The results from the SEJ are based on contributions by three experts, as one expert did not complete the calibration questions required for assessing experts' accuracy and informativeness in Cooke's method. Each expert's accuracy and informativeness score estimates of the 5th, 50th and 95th percentiles for each question of interest were aggregated using the R expert package [54]. Estimates were aggregated to create a distribution, giving equal weight to each expert. Table 3 shows the aggregated lowest, best and highest estimates of the percentage change in crop yield for different scenarios of IPM, pesticide and fertiliser use. Estimates from the fourth expert, who did not complete the calibration questions and so could not be included in the analysis, were in the main slightly lower than the aggregate estimates.

After the data from the SEJ were entered into the model, some plausible scenarios were tested to see how the food loss rates changed.

Scenario 1 represented minimal reductions in fertiliser and pesticides using the application rates in Q1 (Table 2) and no increase in integrated pest management (IPM). To investigate this, we set the fungicide, herbicide, insecticide and molluscicide nodes to Q1, pesticide to reduce $10 \%$ and fertiliser to reduce $5 \%$. Typical food losses are around $10 \%$, so the losses reported here are additional. The outputs showed that the additional food loss was likely up to $8.5 \%$, which we categorised as very low. The probability of losses being very low was $60 \%$ and losses being in other categories (low (8.6-13.5\%), medium (13.6-17.5\%), high (17.6-22.5\%) or very high (over 22.6\%)) 10\% (see Figure 4). As we had few experts, the data are less smooth than they would be with a larger pool of experts.

Scenario 2 represented moderate reductions in fertiliser and pesticides using the application rates in Q1 (Table 2) and no increase in IPM. To investigate this, we set the fungicide, herbicide, insecticide and molluscicide nodes to Q1, pesticide to reduce $25 \%$ and fertiliser to reduce $10 \%$. The outputs showed that the additional food loss was likely between 13.6 and $17.5 \%$, which we categorised as medium. The probability of losses being medium was $60 \%$ and losses being in other categories (very low ( $0.0-8.5 \%$ ), low ( $8.6-13.5 \%$ ), high (17.6-22.5\%) or very high (over 22.6\%)) 10\% (see Figure 5).

![img-3.jpeg](img-3.jpeg)

Figure 4. Scenario 1: The BN model with fungicide, herbicide, insecticide and molluscicide nodes set to Q1, pesticide to reduce 10% and fertiliser to reduce 5%. Typical food losses are around 10%, so the losses reported here are additional.

![img-4.jpeg](img-4.jpeg)

Figure 5. Scenario 2: The BN model with fungicide, herbicide, insecticide and molluscicide nodes set to Q1, pesticide to reduce 25% and fertiliser to reduce 10%. Typical food losses are around 10%, so the losses reported here are additional.

Scenario 3 represented reductions in fertiliser and pesticide in line with the EU Green Deal based on the application rates in Q1 (Table 2) and no increase in IPM. To investigate this, we set the fungicide, herbicide, insecticide and molluscicide nodes to Q1, pesticide to reduce 50% and fertiliser to reduce 20%. The model outputs showed that the additional food loss was likely over 22.6%, which we categorised as very high. The probability of losses being very high was 60% and losses being in other categories (very low (0.0–8.5%), low (8.6–13.5%), medium (13.6–17.5%), high (17.6–22.5%)) 10% (see Figure 6).

Next, we ran the same scenarios with IPM increased. Scenario 4 represented minimal reductions in fertiliser and pesticides based on the application rates in Q1 (Table 2) with an increase in IPM. To investigate this, we set the fungicide, herbicide, insecticide and molluscicide nodes to Q1, pesticide to reduce 10% and fertiliser to reduce 5%. The model outputs showed that the additional food loss was likely up to 8.5%, which we categorised as very low. The probability of losses being very low was 60% and losses being in other categories (low (8.6–13.5%), medium (13.6–17.5%), high (17.6–22.5%) or very high (over 22.6%)) 10% (see Figure 7).

![img-5.jpeg](img-5.jpeg)

Figure 6. Scenario 3: The BN model with fungicide, herbicide, insecticide and molluscicide nodes set to Q1, pesticide to reduce $50 \%$ and fertiliser to reduce $20 \%$. Typical food losses are around $10 \%$, so the losses reported here are additional.
![img-6.jpeg](img-6.jpeg)

Figure 7. Scenario 4: The BN model with fungicide, herbicide, insecticide and molluscicide nodes set to Q1, pesticide to reduce $50 \%$ and fertiliser to reduce $20 \%$. Typical food losses are around $10 \%$, so the losses reported here are additional.

Scenario 5 represented moderate reductions in fertiliser and pesticides using the application rates in Q1 (Table 2) with an increase in IPM. To investigate this, we set the fungicide, herbicide, insecticide and molluscicide nodes to Q1, pesticide to reduce $25 \%$ and fertiliser to reduce $10 \%$. The model outputs showed that the additional food loss was likely between 13.6 and $17.5 \%$, which we categorised as medium. The probability of losses being medium was $60 \%$ and losses being in other categories (very low ( $0.0-8.5 \%$ ), low ( $8.6-13.5 \%$ ), high ( $17.6-22.5 \%$ ) or very high (over $22.6 \%$ )) $10 \%$ (see Figure 8).

Scenario 6 represented reductions in fertiliser and pesticides in line with the EU Green Deal with the application rates in Q1 (Table 2) with an increase in IPM. To investigate this, we set the fungicide, herbicide, insecticide and molluscicide nodes to Q1, pesticide to reduce $50 \%$ and fertiliser to reduce $20 \%$. The model outputs showed that the additional food loss was likely over $22.6 \%$, which we categorised as very high. The probability of losses being very high was $60 \%$ and losses being in other categories (very low ( $0.0-8.5 \%$ ), low ( $8.6-13.5 \%$ ), medium ( $13.6-17.5 \%$ ), high ( $17.6-22.5 \%$ )) $10 \%$ (see Figure 9).

![img-7.jpeg](img-7.jpeg)

Figure 8. Scenario 5: The BN model with fungicide, herbicide, insecticide and molluscicide nodes set to Q1, pesticide to reduce $25 \%$ and fertiliser to reduce $10 \%$. Typical food losses are around $10 \%$, so the losses reported here are additional.
![img-8.jpeg](img-8.jpeg)

Figure 9. Scenario 6: The BN model with fungicide, herbicide, insecticide and molluscicide nodes set to Q1, pesticide to reduce $50 \%$ and fertiliser to reduce $20 \%$. Typical food losses are around $10 \%$, so the losses reported here are additional.

All the possible combinations are shown in Tables 4-6 below.
The models for the application rates in Q2 are shown in Table 5, and the models for the application rates in Q3 are shown in Table 6. The same pattern as in scenarios 1-6 persists regardless of the beginning levels of application rates. In a full model, further scenarios could be run, with different combinations of fungicide, herbicide, insecticide and molluscicide starting application rates.

Table 4. Probability of food loss: Q1. Typical losses are around $10 \%$. The losses above are additional. Very Low represents additional losses up to $8.5 \%$, Low $8.6-13.5 \%$, Medium $13.6-17.5 \%$, High $17.6-22.5 \%$ and High over $22.6 \%$.


Table 5. Probability of food loss: Q2.


We note that the increase in food loss is lowest when input reduction is lowest, regardless of whether IPM is being used or not. Conversely, when the input reduction is at full EU Green Deal levels, the increase in food loss is at its greatest, independent of IPM use. This research demonstrates that, whilst increasing use of IPM to balance the reduction in fertiliser and pesticide does make some difference (Table 3), it is insufficient, in the view of our experts, to compensate for the reductions in pesticide and fertiliser to a sufficient degree to change the category of likely percentage of food losses.

Table 6. Probability of food loss: Q3.


# 4. Conclusions 

We have demonstrated that a BN approach can guide grower decisions to minimise food loss whilst transitioning to reduced pesticide and fertiliser use, using lettuce as an exemplar crop. BNs can model the relevant complexity and interactions in the growing system to form the basis for an IDSS to quantify expected food loss percentages under a range of agricultural input and IPM combinations. This proof of concept provides a basis for developing this approach for decision support for growers and policy makers.

The contribution of the Structured Expert Judgement of expected losses for lettuce under a range of scenarios, where measured data are not available, is a valuable contribution. However, since the number of experts contributing their estimates was fewer than ideal, it would be wise to re-run the elicitation with more experts for a system to be used in business or policy decision making.

The principles of IPM have been well articulated in articles [6,55]. In line with our objective to model Green Deal objectives to reduce pesticide use, we ultimately focus on addressing Principal 6 [55], which indicates the following: "Reduced pesticide use, in terms of frequency, spot spraying, or dose reduction is a recognised tactic along the IPM continuum that can be combined with other ones". As such, we feel we align well with principal 6. The minimal contribution we find IPM makes to supporting pesticide and fertiliser reductions may be explained by the varied definitions and understandings of IPM [6], as well as the perception among practitioners of a high cost associated with practising IPM and complications in applying it [56].

Modelling relationships of crop loss under different pesticide and fertiliser regimes in the context of IPM adoption, as well as the collective use of different types of data, are strengths of this study. One limitation is the low number and diversity of the experts contributing to the SEJ. Experience suggests that the facilitated discussion would have identified more subtle aspects of the system, and experts' estimates would have been shaped by this. It is possible that the probability distributions would be broader with more academics contributing, although experience shows that where calibration is used, a small number of experts typically contribute the majority to the joint estimate. Although some nodes in the BN, which experts had agreed should be present in this proof of concept, were omitted due to a lack of data, the BN structure derived through Soft Elicitation techniques is reported and is a valuable contribution to developing robust and defensible decision support. Policy-

makers can leverage this proof of concept and, having addressed the limitations, use a full model to ascertain the food loss implications of candidate policy options. This will allow policymakers to select from among the candidate policies those which keep food loss within acceptable levels.

Author Contributions: Conceptualization, M.J.B., L.E.W., E.E.S. and L.N.; methodology M.J.B. and E.E.S.; software, L.N.; validation, L.E.W., E.E.S. and L.N.; formal analysis, E.E.S. and L.N.; investigation, L.E.W. and M.J.B.; data curation, E.E.S. and L.N.; writing—original draft preparation, M.J.B., L.E.W., E.E.S. and L.N.; writing—review and editing, M.J.B., L.E.W., E.E.S. and L.N.; visualization, M.J.B., L.E.W., E.E.S. and L.N.; project administration, M.J.B. and L.E.W.; funding acquisition, M.J.B., L.E.W., E.E.S. and L.N. All authors have read and agreed to the published version of the manuscript.

Funding: This research was funded by the Science and Technology Research Council (STFC) Food Network (Grant No: ST/T002921/1), United Kingdom (https://www.stfcfoodnetwork.org/). Accessed on 1 February 2024.

Institutional Review Board Statement: The study was conducted in accordance with the Declaration of Helsinki, and approved by the Institutional Review Board (or Ethics Committee) of University of Warwick (protocol code BSREC 77/20-21 and date of approval 28 April 2021).

Data Availability Statement: Fungicide, insecticide, herbicide and molluscicide application data was purchased from FERA.

Acknowledgments: The input of growers and advisors in this research is appreciated.
Conflicts of Interest: The funders had no role in the design of the study; in the collection, analyses, or interpretation of data; in the writing of the manuscript; or in the decision to publish the results

# Appendix A 

![img-9.jpeg](img-9.jpeg)

Figure A1. The BN model with fungicide, herbicide, insecticide and molluscicide nodes set to Q1, pesticide to reduce $25 \%$ and fertiliser to reduce $5 \%$. Typical food losses are around $10 \%$, so the losses reported here are additional.

![img-10.jpeg](img-10.jpeg)

Figure A2. The BN model with fungicide, herbicide, insecticide and molluscicide nodes set to Q1, pesticide to reduce $50 \%$ and fertiliser to reduce $5 \%$. Typical food losses are around $10 \%$, so the losses reported here are additional.
![img-11.jpeg](img-11.jpeg)

Figure A3. The BN model with fungicide, herbicide, insecticide and molluscicide nodes set to Q1, pesticide to reduce $10 \%$ and fertiliser to reduce $10 \%$. Typical food losses are around $10 \%$, so the losses reported here are additional.
![img-12.jpeg](img-12.jpeg)

Figure A4. The BN model with IPM set to "No", fungicide, herbicide, insecticide and molluscicide nodes set to Q1, pesticide to reduce $50 \%$ and fertiliser to reduce $10 \%$. Typical food losses are around $10 \%$, so the losses reported here are additional.

![img-13.jpeg](img-13.jpeg)

Figure A5. The BN model with IPM set to "No", fungicide, herbicide, insecticide and molluscicide nodes set to Q1, pesticide to reduce $10 \%$ and fertiliser to reduce $20 \%$. Typical food losses are around $10 \%$, so the losses reported here are additional.
![img-14.jpeg](img-14.jpeg)

Figure A6. The BN model with IPM set to "No", fungicide, herbicide, insecticide and molluscicide nodes set to Q1, pesticide to reduce $25 \%$ and fertiliser to reduce $20 \%$. Typical food losses are around $10 \%$, so the losses reported here are additional.
![img-15.jpeg](img-15.jpeg)

Figure A7. The BN model with IPM set to "Yes", fungicide, herbicide, insecticide and molluscicide nodes set to Q1, pesticide to reduce $25 \%$ and fertiliser to reduce $5 \%$. Typical food losses are around $10 \%$, so the losses reported here are additional.

![img-16.jpeg](img-16.jpeg)

Figure A8. The BN model with IPM set to "Yes", fungicide, herbicide, insecticide and molluscicide nodes set to Q1, pesticide to reduce $50 \%$ and fertiliser to reduce $5 \%$. Typical food losses are around $10 \%$, so the losses reported here are additional.
![img-17.jpeg](img-17.jpeg)

Figure A9. The BN model with IPM set to "Yes", fungicide, herbicide, insecticide and molluscicide nodes set to Q1, pesticide to reduce $10 \%$ and fertiliser to reduce $10 \%$. Typical food losses are around $10 \%$, so the losses reported here are additional.
![img-18.jpeg](img-18.jpeg)

Figure A10. The BN model with IPM set to "Yes", fungicide, herbicide, insecticide and molluscicide nodes set to Q1, pesticide to reduce $50 \%$ and fertiliser to reduce $10 \%$. Typical food losses are around $10 \%$, so the losses reported here are additional.

![img-19.jpeg](img-19.jpeg)

Figure A11. The BN model with IPM set to "Yes", fungicide, herbicide, insecticide and molluscicide nodes set to Q1, pesticide to reduce $10 \%$ and fertiliser to reduce $20 \%$. Typical food losses are around $10 \%$, so the losses reported here are additional.
![img-20.jpeg](img-20.jpeg)

Figure A12. The BN model with fungicide, herbicide, insecticide and molluscicide nodes set to Q1, pesticide to reduce $25 \%$ and fertiliser to reduce $20 \%$. Typical food losses are around $10 \%$, so the losses reported here are additional.
