# Fish-Net: Probabilistic models for fishway planning, design and monitoring to support environmentally sustainable hydropower 

Wilkes, M, Baumgartner, L, Boys, C, Silva, L, O'Connor, J, Jones, M, Stuart, I, Habit, E, Link, O \& Webb, A<br>Author post-print (accepted) deposited by Coventry University's Repository

Original citation \& hyperlink:
Wilkes, M, Baumgartner, L, Boys, C, Silva, L, O'Connor, J, Jones, M, Stuart, I, Habit, E, Link, O \& Webb, A 2018, 'Fish-Net: Probabilistic models for fishway planning, design and monitoring to support environmentally sustainable hydropower', Fish and Fisheries, vol. 19, no. 4, pp. 677-697.
https://dx.doi.org/10.1111/faf. 12282
DOI 10.1111/faf. 12282
ISSN 1467-2960
ESSN 1467-2979

Publisher: Wiley

This is the peer reviewed version of the following article: Wilkes, M, Baumgartner, L, Boys, C, Silva, L, O'Connor, J, Jones, M, Stuart, I, Habit, E, Link, O \& Webb, A 2018, 'Fish-Net: Probabilistic models for fishway planning, design and monitoring to support environmentally sustainable hydropower' Fish and Fisheries, vol 19:4, pp. 677-697, which has been published in final form at 10.1111/faf.12282. This article may be used for non-commercial purposes in accordance with Wiley Terms and Conditions for Self-Archiving.

Copyright © and Moral Rights are retained by the author(s) and/ or other copyright owners. A copy can be downloaded for personal non-commercial research or study, without prior permission or charge. This item cannot be reproduced or quoted extensively from without first obtaining permission in writing from the copyright holder(s). The content must not be changed in any way or sold commercially in any format or medium without the formal permission of the copyright holders.

This document is the author's post-print version, incorporating any revisions agreed during the peer-review process. Some differences between the published version and this version may remain and you are advised to consult the published version if you wish to cite from it.

1 Fish-Net: Probabilistic models for fishway planning, design and monitoring
2 to support environmentally sustainable hydropower

3

4 Running title: Probabilistic models for fishways

5

6 ${ }^{1}$ Martin Wilkes*; ${ }^{2}$ Lee Baumgartner; ${ }^{2,3}$ Craig Boys; ${ }^{2,4}$ Luiz G. M. Silva; ${ }^{5}$ Justin
7 O'Connor; ${ }^{5}$ Matthew Jones; ${ }^{5}$ Ivor Stuart; ${ }^{6}$ Evelyn Habit; ${ }^{7}$ Oscar Link; ${ }^{8}$ J. Angus
8 Webb

9

10 ${ }^{1}$ Centre for Agroecology, Water \& Resilience, Coventry University, Wolston Lane,
11 Ryton on Dunsmore, Coventry CV8 3LG, United Kingdom. *Corresponding
12 author: martin.wilkes@coventry.ac.uk
13 ${ }^{2}$ Institute for Land, Water and Society, Charles Sturt University, Post Office Box
14 789, Albury, New South Wales, 2640, Australia
15 ${ }^{3}$ New South Wales Department of Primary Industries, Port Stephens Fisheries
16 Institute, Taylors Beach Road, Taylors Beach, NSW 2316, Australia
174 Universidade Federal de São João del-Rei, DTECH, Rod. MG 443, Km 7, Ouro
18 Branco - MG, 36420-000, Brazil
$19{ }^{5}$ Arthur Rylah Institute for Environmental Research, 123 Brown St, Heidelberg
20 VIC 3084, Australia
$21{ }^{6}$ Facultad de Ciencias Ambientales, Universidad de Concepción, Víctor Lamas
22 1290, Casilla 160-C, Chile

23 ${ }^{7}$ Universidad de Concepción, Víctor Lamas 1290, Casilla 160-C, Chile
24 bDepartment of Infrastructure Engineering, The University of Melbourne,
25 Parkville 3010, Victoria, Australia

The construction of fishways for upstream and downstream connectivity is the preferred mitigation measure for hydropower dams and other riverine barriers. Yet empirical evidence for effective design criteria for many species is missing. We therefore assembled a group of international fishway designers and combined their knowledge with available empirical data using a formal expert elicitation protocol and Bayesian networks. The expert elicitation method we use minimises biases typically associated with such approaches. Demonstrating our application with a case study on the temperate Southern Hemisphere, we use the resulting probabilistic models to predict the following, given alternative design parameters: (i) the effectiveness of technical fishways for upstream movement of migratory fish; (ii) habitat quality in nature-like bypasses for resident fish; and (iii) rates of mortality during downstream passage of all fish through turbines and spillways.

The Fish Passage Network (Fish-Net) predicts that fishways for native species could be near $0 \%$ or near $100 \%$ efficient depending on their design, suggesting great scope for adequate mitigation. Sensitivity analyses revealed the most important parameters as: (i) design of attraction and entrance features of technical fishways for upstream migration; (ii) habitat preferences of resident fish in nature-like bypasses; and (iii) susceptibility of fish to barotrauma and blade strike during turbine passage. Numerical modelling predicted that mortality rates of small bodied fish (50-100 mm TL) due to blade-strike may be higher for Kaplan than Francis turbines. Our findings can be used to support

51 environmentally sustainable decisions in the planning, design and monitoring
52 stages of hydropower development.

54 Key words: Barotrauma; blade strike; fishway design; fish passage; hydropower;
55 nature-like bypass.

57 Table of contents
58 Introduction
59 Methods

60 Case study region
61 Bayesian Networks

62 Expert elicitation
63 Data analysis

64 Results

65 Technical fishway design for upstream migration
66 Nature-like bypass design for resident species
67 Mortality rates during downstream passage
68 Discussion

69 Technical fishway design for upstream migration
70 Nature-like bypasses
71 Downstream passage
72 Limitations of the approach
73 Research priorities to improve fishway performance
74 Conclusions: Applying Fish-Net in the real world

78 The world is experiencing a hydropower boom (Zarfl et al., 2015), further
79 fragmenting rivers already impacted by multiple barriers associated with
80 irrigation, water supply, transport and flood and erosion management. Given
81 that all fish need to move for reproduction, feeding, refuge, dispersal and gene
82 flow, this poses a serious threat to aquatic biodiversity and fisheries (Winemiller
83 et al., 2016; Pelicice et al., 2017). Impediments to upstream and downstream
84 movements can cause species replacement and extirpation (Poff \& Schmidt,
85 2016).

86

87 The construction of fishways, which we define as any structures designed to facilitate upstream or downstream connectivity for fish, has traditionally been the preferred mitigation measure (Clay, 1995; Larinier, 2001). The research and management involved has often focused on 'technical' fishways for upstream migrants, 'nature-like' bypasses to provide habitat connectivity for nonmigratory (resident) fish, and screens and bypasses to exclude fish from dangerous routes downstream. However, beyond several commerciallyimportant migratory species native to northern Europe and North America (e.g. salmonids, clupeids), few empirical data are available to guide the design of efficient fishways, especially for downstream movement (Bunt et al., 2016; Pracheil et al., 2016; Williams \& Katopodis, 2016; Wilkes et al., 2018). There are exceptions to this in Australia (e.g. Stuart \& Mallen-Cooper, 1999; Morgan \& Beatty, 2006; Mallen-Cooper \& Brand, 2007; Stuart et al., 2008; Baumgartner et

al., 2010; O'Connor et al., 2015a; Amtstaetter et al., 2017), with some notable successes in the Murray-Darling Basin (Barrett, 2004; Baumgartner et al., 2014).

Effective fishway design for non-salmonid species remains challenging (Noonan et al., 2012; Bunt et al., 2016; Kemp et al., 2016). This is especially true of smallbodied, non-recreational species (e.g. adults <150 mm TL; Link \& Habit, 2015), whose relatively weak swimming abilities are consistent with their diminutive stature (Nikora et al., 2003; Nelson et al., 2003; Leavy \& Bonner, 2009; Bestgen et al., 2010; Ficke et al., 2011; Laborde et al., 2016). Several of these species support culturally and economically important capture fisheries (e.g. whitebait; Galaxias spp., Galaxiidae) and all are important for the maintenance of ecosystem function upon which inland and marine fisheries depend (Holmlund \& Hammer, 1999; Dudgeon et al., 2006). Providing effective passage for non-recreational fish is increasingly seen as a priority in diverse biogeographical settings, including South America (e.g. Link \& Habit, 2015), North America (e.g. Pennock et al., 2017), Europe (e.g. Kucukali \& Hassinger, 2016), Asia (e.g. Muraoka et al., 2017), Australia (e.g. O'Connor et al., 2015b) and New Zealand (e.g. Baker \& Boubee, 2006).

"Rules-of-thumb" abound in fishway design internationally. The influential work by Larinier (2008) recommended that maximum water velocity ( $U_{\max }$ ) in technical fishways for upstream passage should be $<2 \mathrm{~m} \mathrm{~s}^{-1}$ for salmonids, cyprinids and clupeids, whereas the average volumetric energy dissipation rate $(K)$ should be $<200 \mathrm{~W} \mathrm{~m}^{-3}$ for large salmonids and $<150 \mathrm{~W} \mathrm{~m}^{-3}$ for other species. Guidance in New Zealand states that a continuous path of mean water velocity

$<0.3 \mathrm{~m} \mathrm{~s}^{-1}$ should be made available for native species passing culverts (Boubée et al., 2000). The fishway guidelines established by the State Government of Victoria, Australia (O'Connor et al., 2015b), make a number of recommendations, including maintaining a water depth of 0.5 m for technical fishways designed for small-bodied fish (20-100 mm TL).

Fish need to move in both upstream and downstream directions but design criteria to minimise fish mortality during downstream movement through turbines and spillways has received far less attention globally than traditional upstream fishway design (Coutant \& Whitney, 2000; Prachiel et al., 2016; Wilkes et al., 2018). The criteria that have been proposed for downstream passage relate to minimising injury and mortality resulting from rapid decompression (barotrauma), fluid shear and blade strike. In southeast Australia, it is recommended that juveniles and adults are not exposed to pressures less than $70 \%$ of their acclimated pressure (Boys et al. 2016). The potentially high mortality of entrained fish has stimulated development of 'fish-friendlier' turbines (Deng et al., 2016). Of the existing turbine technologies in widespread use, the meta-analysis of Pracheil et al. (2016) suggested that Kaplan turbines caused least mortalities of relatively large-bodied fish (e.g. Salmonidae), followed by crossflow and Francis types.

These "rules-of-thumb" for fishway design are generally based on professional judgement with no methodological framework to mitigate for the bias, overconfidence and lack of transparency that can plague the use of expert knowledge (Burgman, 2005; Martin et al., 2012). Furthermore, because they

provide absolute recommendations, these design criteria do not explicitly communicate two crucial pieces of information to non-expert decision makers: (i) the uncertainty involved in fishway design; and (ii) the relative costs and benefits of different design parameters. The latter is particularly important considering that trade-offs among cost, hydraulic and biological performance and species coverage are common in fishway design.

There is a clear and urgent need for a robust set of fishway design criteria for non-recreational species in order to support environmentally sustainable hydropower development. Methods of deriving such criteria are required that can employ the vast body of knowledge held by fishway experts but which provide greater transparency, assessment of uncertainty, and consideration of cost-benefit trade-offs. Our aim in this study was to address this gap by developing knowledge-based criteria using robust methods that take maximal advantage of expert knowledge while minimizing bias (de Little et al., 2018). We modelled: (i) the effectiveness of technical fishways for upstream migration in diadromous non-recreational fish; (ii) the habitat quality in nature-like bypasses for resident non-recreational fish; and (iii) rates of mortality during downstream movement through turbines and spillways for all non-recreational fish. Using a formal expert elicitation method and Bayesian Networks (BNs), we developed clear guidance on fishway design criteria based on empirical data, numerical modelling and expert knowledge. As a demonstrative case study, we focus on the temperate Southern Hemisphere, including New Zealand and southern parts of Chile, Argentina and Australia, but our approach could be applied to improve fishway design globally.

Case study region - the temperate Southern Hemisphere

From an ichthyological perspective, the temperate Southern Hemisphere (TSH) can be defined by the joint distribution of two species, inanga (Galaxias maculatus, Galaxiidae) and pouched lamprey (Geotria Australis, Geotridae) (McDowall, 2002). Though climatically similar to the temperate Northern Hemisphere, TSH is a biologically and socioeconomically distinct region, with different contemporary pressures on river ecosystems. In central Chile, for instance, the sites of around 1000 potential hydropower dams (Ministerio de Energía, 2015) overlap with a biodiversity hotspot home to a highly endemic and threatened fish fauna (Table 1). The negative effects of river fragmentation on fish have been documented throughout TSH. In New Zealand, for example, 74\% of freshwater and diadromous species are classified as threatened or at risk, in many cases due to connectivity issues (Goodman et al., 2014).

The movement patterns of the majority of species native to TSH fall into two broad categories that are helpful for considering fish passage needs: catadromous/amphidromous and resident (e.g. Table 1). However, as caveats to that generalisation we must acknowledge that: (i) many species considered migratory are not obligate migrators (Pollard, 1971; McDowall, 2003; Lattuca et al., 2008); (ii) Galaxiidae, an important group in TSH, also includes anadromous species in New Zealand; (iii) parts of TSH are also home to anadromous lamprey

and catadromous eel; and (iv) the category of resident fish includes species that may exhibit a wide range of movements, from $10^{1} \mathrm{~km}$ to $10^{3} \mathrm{~km}$ (Reynolds 1983; O'Connor et al. 2003; O'Connor et al. 2005; Buria et al. 2007; Piedra et al. 2012; Otturi et al. 2016).

# 205 Bayesian Networks 

206

207 The selection of a modelling framework was based upon several criteria. The framework needed to be: (i) statistically robust; (ii) transparent; (iii) probabilistic; (iv) easy to communicate to a range of audiences; (v) able to integrate data from different sources (empirical, numerical model outputs, expert knowledge); (vi) amenable to updates in light of new evidence in the future; and (vii) able to generate practical outputs to guide fishway design. We identified BNs as the ideal approach as it satisfied all of our essential criteria (Cain, 2001). Furthermore, there is a well-developed body of literature on applications of BNs to freshwater ecosystems (e.g. Borsuk et al., 2006; Peterson et al., 2008; Anderson et al., 2012; Alves et al., 2013).

218 Development of a BN involves the specification of nodes representing causal and response variables in a directed acyclic graph (Pfister \& Zalewski, 2008). Each node has discrete states defining all possible conditions or outcomes. Nodes are connected by arcs representing probabilistic dependency relations among the variables. These relations are described by conditional probability tables (CPTs) that can be populated using empirical data, model outputs and/or expert

knowledge. Cain (2001) outlines 12 steps in the development of BNs. These can be consolidated into four sets of tasks that we followed closely:

1. Establish the aim of the BN
2. Consult with stakeholders to construct and refine a prototype BN, i.e. the set of nodes, discrete node states and CPTs
3. Populate CPTs using a combination of data, modelling results and expert knowledge, interpolating as necessary
4. Implement CPTs in chosen software to form the BN

The aim of the BNs was to facilitate better planning, design and monitoring of hydropower from a fish passage perspective by providing a set of probabilities for use in statistical analyses and to guide fishway design. Our expert stakeholders included biologists and engineers from academia and industry, specialist fishway designers, staff from fisheries authorities and regulatory bodies. We based our initial sets of nodes and node states on information from the global literature on fishway design (e.g. Coutant \& Whitney, 2000; Larinier \& Marmulla 2004; Katopodis, 2005; Roscoe \& Hinch 2010; Bunt et al. 2012, 2016; Noonan et al., 2012; Brown et al., 2014; Pracheil et al., 2016). These initial node sets were then refined through several meetings with stakeholders, resulting in the three separate prototype BNs ready for CPT population. These prototype BNs formed the basis of the Fish Passage Network (Fish-Net).

The first protoype BN considered fishway design for catadromous and amphidromous species migrating upstream (Table 2, Fig. 1a). The response

variable was a composite fishway effectiveness metric commonly used in fish passage research (Kemp \& O'Hanley, 2010; Cooke \& Hinch, 2013). For this part of Fish-Net we took a representative species approach using G. maculatus, a common and widespread inhabitant of coastal basins throughout TSH (McDowall, 2002). This was because the majority of our stakeholders were familiar with this species, it is a common target for fishway design and it forms a large part of the fish biomass in TSH. Furthermore, with relatively weak swimming ability, this species likely represents a lower limit on passage efficiencies among migratory populations (Mitchell, 1989; Nikora et al., 2003; Plew et al., 2007).

For resident species, which may lack the motivation to swim upstream in determined, directed movements, traditional fishway effectiveness metrics are less appropriate. Instead, for non-migratory species, fishways should be designed to provide contiguous habitat to allow dispersal and gene flow (Link \& Habit, 2015). Thus, our second prototype BN focused on modelling habitat quality for multiple species in nature-like bypasses. For this part of Fish-Net we used existing data from García et al. (2011), who adopted the fuzzy habitat simulation model CASiMiR (Schneider, 2001) to model habitat suitability for 16 species and life-stages found in the River Biobío, Chile. We excluded adults and juveniles of G. maculatus and G. australis as these species are not classified as resident (Table 1), although it should be noted not all G. maculatus populations are catadromous (Górski et al 2015). This left 12 species and life-stages that we considered as representative of the resident non-recreational fish fauna of TSH. In this BN, the response node states were habitat suitability categories (low,

medium, high, very high) for each species and life-stage. The parent (causal) nodes were mean column water velocity, water depth and substrate size, with node states taken from the CASiMiR membership functions of García et al. (2011). CPTs were populated using the fuzzy rules from the original analysis (García et al., 2011).

For the third and final part of Fish-Net we used a combination of data sources to model mortality rates during downstream movement through turbines and spillways (Table 3). We separated our response variables into the three main sources of mortality during downstream passage, namely barotrauma, shear and blade strike (Pracheil et al., 2016). In order to integrate the important sources of delayed mortality associated with downstream passage, this BN focused on the 72-hour mortality rate, including indirect mortality due to increased susceptibility to disease and predation. For barotrauma and shear we used expert elicitation to populate CPTs from the prototype BN (see below). Causal nodes and node states were derived from the literature on pressure- (Brown et al., 2014) and shear- (Boys et al., 2014) related mortality. For blade strike we adopted two well-established blade strike models (BSMs) focusing on Kaplan (Deng et al., 2007) and Francis (Ferguson et al., 2008) turbines respectively. We limited our analyses to these turbines as they are the most common types used worldwide. We modelled blade strike probability at 10\% intervals of turbine discharge from between $30 \%$ and $140 \%$ of design discharge to reflect the range of conditions under which the turbine could potentially operate. Because the orientation of a fish during turbine entrainment can have a large effect on blade strike probability, we represented effective fish length as a uniform distribution

using the stochastic approach of Deng et al. (2007). Blade strike probabilities were converted to a likely 72-hour mortality rate using the empirically-based mutilation ratio (MR) of Turnpenny et al. (2000). Turbine design parameters for BSMs were provided by hydroelectric generators and engineers in Chile (Table S1, Supplementary Material online).

Explicit representation of expert knowledge is increasingly used in applied ecological research, where it can form the basis for urgent management decisions (Krueger et al., 2012) and provide informative priors for Bayesian ecologists (Marcot et al., 2001; Martin et al., 2005; Low Choy et al., 2009; Kuhnert et al., 2010; Webb et al., 2015). However, the robustness of such applications depends on the rigour with which knowledge is elicited from experts (Martin et al., 2012). Biases related to knowledge availability, anchoring and group dynamics can impact on attempts to harness expert knowledge to good effect (Burgman, 2005; Martin et al., 2012). Carefully managed, well-facilitated elicitation protocols, however, can provide a reliable basis for management decisions (Knol et al., 2010). Elicitation approaches range from simple 'roundtable discussions' with no controls over common biases, to systematic protocols underpinned by rigorous cognitive psychological research (SpeirsBridge et al., 2010). For our expert elicitation workshops, we employed the protocol described by de Little et al. (2018) involving the mathematical accumulation of expert opinion in a manner that allows direct incorporation into BNs. We explain the protocol in more detail below.

We assembled a group of experts, based in southeast Australia, who are involved in the design of fishways internationally. The group consisted of six senior scientists and one PhD student with extensive industry experience. Experts were employed in academia and state authorities concerned with fisheries and biodiversity conservation. Together they represented more than 100 years of accumulated experience in fishway research in Australia, Southeast Asia, and North and South America.

After several consultations with experts to define our prototype BNs, we held two separate expert elicitation workshops. The first focused on barotrauma and shear-related mortality, and was attended by the three experts with most experience in downstream passage. The second workshop, on technical fishway design for upstream migration, was attended by our five most senior experts with fishway design experience. Before beginning the elicitation, experts were introduced to the context and objectives of the workshop. They were also made aware of the common biases in expert elicitation, and how to mitigate for them. The facilitators then presented the factors forming each management scenario, i.e. each unique combination of causal node states joining response nodes in the prototype BNs (Fig. 1). This was to ensure that workshop participants had a shared understanding of what each node and node state meant (de Little et al., 2018).

Once this familiarisation phase of the workshop was complete, the formal elicitation process began. Experts were asked four questions for each unique

349 combination of causal node states connected to each response node (Speirs-
350 Bridge et al., 2010). The basic forms of the questions in the 'four-point' elicitation
351 protocol are: (i) what is the minimum you would realistically expect?; (ii) what is
352 the maximum you would realistically expect?; (iii) what is your most likely (best)
353 estimate?; and (iv) how confident are you that this range includes the true
354 number? Experts wrote their responses by hand in a pre-prepared document in
355 which each question was printed on a separate page. They were asked not to
356 refer back to previous answers. After every second question the facilitators
357 quizzed the experts with numerical trivia to distract them from previous
358 answers, mitigating for anchoring bias. In each workshop, experts answered all
359 questions twice. In the first round, experts were not permitted to confer or
360 discuss their answers in any way but could refer to published results. First round
361 answers were then inputted into a spreadsheet, converted to probability
362 distributions (see below), and shown to all experts, revealing any convergence or
363 divergence in opinion. After ample opportunity to discuss any differences in
364 opinion, experts were asked to provide new answers or maintain their initial
365 answers. Final probabilities used in constructing the CPTs were taken as the
366 mean of all first and second round answers. For a description of the logic
367 underpinning these aspects of the elicitation process, see de Little et al. (2018).
368
369 Questions for attraction and entrance efficiency respectively related to the
370 expected percentage of an upstream migrating cohort of the representative
371 species G. maculatus ( $40-50 \mathrm{~mm}$ TL) locating the fishway entrance and then the
372 proportion of those fish entering the structure within a timeframe not expected
373 to impact fitness. Questions for shear-related mortality focused on the expected

72-hour mortality rate for a downstream migrating cohort of G. maculatus (80-

90 mm TL). Representative body lengths for upstream and downstream migrants of G. maculatus were derived from observations from the extant literature (Pollard, 1971; McDowall et al., 1994; Chapman et al., 2006; Barriga et al., 2007). Questions for barotrauma-related mortality related to the 72-hour mortality rate for generic species with combinations of two traits: acclimation depth ( $1 \mathrm{~m}, 10 \mathrm{~m}$ ) and swim bladder morphology (none, physoclistous, physostomous). In both cases the 72-hour mortality rate included indirect mortality due to increased susceptibility to disease and predation.

The complexity of BNs can be limited by the number of questions experts may reasonably be expected to answer in one or more workshops (Cain, 2001). Since the number of questions to be asked is a function of the unique combinations of causal node states connected to each response node, it is sometimes necessary to consolidate causal nodes in order to minimise the workload on experts and avoid 'expert fatigue' (Cain, 2001). Our early prototype BNs for technical (upstream) fishway design contained more than 70 unique combinations of node states, clearly too many for a one-day workshop. It was therefore necessary to model passage efficiency in two separate stages (Fig. 1a). First, experts were asked to estimate the percentage of the cohort able to successfully pass the first pool based on unique combinations of pool dimensions, head loss and slot or gap width categories. Experts were provided with the maximum velocity ( $U_{\max }=$ $\sqrt{2 g \cdot \Delta h}$, where $g$ is acceleration due to gravity and $\Delta h$ is head loss), discharge $\left(Q=C \cdot U_{\max } \cdot A\right.$, where $C$ is a coefficient typically taken as 0.7 and $A$ is crosssectional area) and energy dissipation $(K=(Q \cdot \Delta h \cdot \rho) / V$, where $\rho$ is the weight

density of water and $V$ is pool volume) associated with each combination. After collating responses, experts reached a consensus on the best case scenario for passage through a single pool. Experts were then asked to estimate the percentage of the cohort able to pass the whole fishway within 12 hours given the optimal design of an individual pool, assuming each pool section of the hypothetical fishway had the same design. This allowed us to later model the effect of fishway type and length on passage efficiency independent of other design parameters (see below). We stipulated a 12-hour window for fish passage, pragmatically defined as 06:00 to 18:00 hours, to reflect evidence that G. maculatus will fall back downstream overnight if it fails to ascend a fishway within one daylight period (Baker \& Boubee, 2006; Amtstaetter et al., 2017). Two further simplifying assumptions we made were: (i) to set all water depths at 0.5 m within fishways for all scenarios; and (ii) to assume optimal attraction flow geometry (see O'Connor et al., 2015b, for recommendations).

Data analysis

We fitted beta distributions to probabilities (both initial and final) from the expert elicitation workshops using minimum cross-entropy (MCE; Salomon, 2013). The MCE method transforms the results of four-point elicitation protocols into statistically representable distributions. We used beta distributions as our response variables were all bound between zero and one. For continuous causal variables, we then fitted general linear models to the mean and variance of expert elicited distributions in order to interpolate between the discrete values forming the questions posed to experts. For shear-related mortality it was

necessary to force the model through a zero intercept because a positive mortality rate at a strain rate of $0 \mathrm{~cm} \mathrm{~s}^{-1} \mathrm{~cm}^{-1}$ was not realistic. All models were fitted in R 3.3.2 (R Core Team, 2016) and the beta parameters for interpolated scenarios exported for use in the final BNs, which were implemented with Netica v5.24 (Norsys Software Corporation, 2016).

Because an individual fish moving downstream through a turbine or spillway could be killed by one or more of barotrauma, shear or blade strike, we could not implement the overall mortality rate response node in Netica. Instead we exported beta parameters from Netica, sampled $n=1000$ fish from individual barotrauma, shear and blade strike mortality distributions and fitted binomial models. For each sample, we summed binomial distributions from the three mortality sources, i.e. the resulting value could be between 0 (no mortality) and 3 (mortality due to a combination of all three sources). We defined the overall mortality rate as the proportion of samples with non-zero values. Finally, we performed a sensitivity analysis on each response node using the variance reduction (for quantitative response nodes) or entropy reduction (for categorical response nodes) values in Netica.

# Results 

Technical fishway design for upstream migration

Our expert-informed BN reported that attraction efficiency increases with attraction flow and, to a lesser extent, decreases as the fishway entrance gets

further away from the upstream limit of migration (Fig. 2a-d, Table 4). For head loss at the fishway entrance, which was retained in the final BN as two broad categories (20-100 mm, 150-230 mm), the model showed that a lower head loss would lead to a higher entrance efficiency (Fig. 2e). Of the two fishway types identified by our experts as suitable (vertical slot and rock ramp types), there was no difference in predicted passage efficiency. Hence, only results for vertical slot fishways are shown in Fig. 2f-k. According to our experts, fishway length has a relatively weak effect on passage efficiency for a given design (Fig. 2f-k). Instead, head loss between pools, slot or gap width and pool dimensions were all seen as much more important factors (Table 4). Results of our sensitivity analysis also show that attraction efficiency is most limiting for overall fishway effectiveness (Table 4). The BN resulting from the analysis of expert knowledge for this part of Fish-Net can be seen in Fig. 3 where, in addition to providing probabilistic predictions of fishway effectiveness, key fishway hydraulic parameters $\left(U_{\max }, Q, K\right)$ are reported.

Nature-like bypass design for resident species

Mean water velocity was generally the most important design parameter for nature-like bypasses, although the parameters most limiting to habitat suitability varied between species and life-stages (Table 5). The BN resulting from the implementation of the fuzzy rules predicts categorical habitat suitability for each species given values of the causal variables (Fig. 4). Running various scenarios through the BN suggests that an optimal solution for the whole community, resulting in $\geq 16.7 \%$ of habitat within the bypass classified as high or very high

suitability for all species and life-stages, would be provided by water velocities uniformly distributed between $0-1.25 \mathrm{~m} \mathrm{~s}^{-1}$, water depths uniformly distributed between $0.3-1.25 \mathrm{~m}$, with bed surface roughness (gravel).

Swim bladder morphology was by far the most important factor affecting mortality due to barotrauma, followed by the ratio of pressure change (Table 6, Fig. 5a-f). The acclimation depth was thought to have very little effect on the 72hour mortality rate (Fig. 5f). Experts were more uncertain about the mortality rate for physoclistous species than other swim bladder morphologies (Fig. 5b and e). For shear-related mortality, the probability distributions suggest a gradual increase in the response variable from around $200 \mathrm{~cm} \mathrm{~s}^{-1} \mathrm{~cm}^{-1}$ to the maximum considered (Fig. 5g). For blade strike, our model predicts higher mortality rates in Kaplan turbines than in Francis turbines for a given fish body length, with the exception of high discharges up to $140 \%$ of the turbine design discharge (Fig. 5h-n). The sensitivity analysis shows that the 72-hour mortality due to blade strike is most heavily influenced by the turbine design followed by the fish body length (Table 6). Overall, the relative turbine discharge was less influential, although it is clearly a more important variable for Kaplan turbines than Francis turbines (Fig. 5l-n).

The final BN for the downstream component of Fish-Net is shown in Fig. 6. This BN includes as response variables the three mortality sources comprising the overall 72-hour mortality. After sampling from these three distributions external

to the BN it was possible to estimate the overall mortality rate. Predicted best and worst case scenarios for non-recreational fish moving downstream through turbines indicates that physoclists and physostomes are more severely affected than species lacking a swim bladder (Fig. 7). The influence of swim bladder type suggests barotrauma as an important source of mortality, together with blade strike particularly for larger-bodied fish. Our model predicts that almost the complete range of possible mortality rates $(0-100 \%)$ is plausible, depending on turbine design and the characteristics of target species.

# 507 

## 508 Discussion

510 Fishway effectiveness and mortality rates during downstream passage may take a broad range of values depending on design parameters, suggesting that there is wide scope for optimising fishway and turbine design. Overall, the most important parameters in Fish-Net are: attraction flow for technical fishways; mean column water velocity and depth in nature-like bypasses; and turbine design and pressure profiles for downstream passage. In the first application of its kind, Fish-Net integrates diverse sources of data in a transparent and statistically robust modelling framework to provide fishway design recommendations that are readily communicable to a range of audiences. Because BNs provide probabilistic results, our approach explicitly acknowledges the uncertainty in effectiveness of fishways, and allows users to consider tradeoffs between different design elements. Furthermore, sensitivity analyses allowed us to identify the key design parameters that can limit fishway effectiveness.

526 Technical fishways for upstream passage

527

528 Technical fishways have traditionally been the favoured approach to mitigating for fish passage (Clay, 1995; Larinier, 2001). However, the historical development of technical fishways has focused on the needs of salmonids and, to a lesser extent, cyprinids and clupeids. This has resulted in a debate on fishway effectiveness globally, as the majority of the designs have been exported from the temperate Northern Hemisphere to other parts of the world with different fish faunas (Kemp, 2016). A rare exception to this is in Australia, where variations to Northern Hemisphere designs have been successfully adapted to local species (e.g. O'Connor et al., 2015b).

537

538 Fish-Net shows that commonly used "rules-of-thumb" for salmonids and cyprinids of the Northern Hemisphere would be wholly unsuitable for native species of TSH (Fig. 8). Instead, we support the criteria of O'Connor et al. (2015b) of $U_{\max } \leq 1.4 \mathrm{~m} \mathrm{~s}^{-1}$ and $K \leq 30 \mathrm{~W} \mathrm{~m}^{-3}$ for small-bodied fish, compiled from a series of works developed for Australia (e.g. Stuart \& Mallen-Cooper, 1999; Morgan \& Beatty, 2006; Mallen-Cooper \& Brand, 2007; Stuart et al., 2008; Baumgartner et al., 2010). Despite the contrast between these two sets of recommendations, salmonid-type fishways are still being constructed in TSH (e.g. Servicio de Evaluación Ambiental, 2017), presumably at great expense. In addition to limiting passage of native migrants, this exacerbates already serious problems

548 with invasive salmonids and cyprinids (Morgan et al., 2004; Habit et al., 2010) by favouring their movements through the barrier.

551 We found vertical slot and rock ramp fishways to be the most effective solution for migratory non-recreational fish of TSH. Final elicited passage efficiencies were almost identical for these fishway types. However, head- and tail- water levels are typically dynamic because of variable hydrology and energy production, including hydropeaking. Thus, in most cases vertical slot fishways would be recommended as their deep slot configuration provides a greater capacity to maintain relatively stable hydraulic conditions. They are also less susceptible to erosion in high flow events. Another advantage of vertical slot fishways is that slot designs (shape, number) may be modified to manipulate fishway discharge, pool hydraulics and maximum velocities at different depths within the water column, providing a range of conditions for species with different behaviours and swimming capacities (Tomé et al., 2013; O'Connor et al., 2015b). Where water levels are less dynamic and a more natural appearance is desirable, however, a rock ramp may be the preferred option. Furthermore, rock ramps may be constructed across the entire width of smaller streams, eliminating issues with fish attraction.

568 Fish-Net identifies attraction efficiency as the limiting factor in technical fishway effectiveness, a finding consistent with previous analyses (Larinier \& Marmulla, 2004; Bunt et al., 2012). Even for the best case scenario, our BN for technical fishway design predicts a mean attraction efficiency of only $59 \%$. This is despite considering an ideally located fishway entrance, attraction flows of up to $20 \%$ of

the total discharge and an optimal attraction flow design (O'Connor et al., 2015b; Gisen et al., 2017). Furthermore, under the best case scenario for passage efficiency the fishway discharge is only $0.02 \mathrm{~m}^{3} \mathrm{~s}^{-1}$, suggesting that the delivery of auxiliary flow to the entrance is essential for maximising upstream fishway effectiveness in all but the smallest of rivers.

Nature-like bypasses

It has sometimes been assumed that passage of resident fish can be mitigated using technical fishways to a degree sufficient to maintain connectivity between sub-populations (e.g. Laborde et al., 2016; Link et al., 2017). The empirical evidence for these assumptions is scarce, and metapopulation theory suggests that high dispersal rates may be necessary to avoid local extinctions, support healthy sub-populations and maintain high patch occupancy (Schnell et al., 2013; Villard \& Metzger, 2014). Absent of a biological imperative to migrate to distant spawning locations, resident non-recreational fish may not make the potentially stressful journey upstream through technical fishways. Thus, we follow Link and Habit (2015) in recommending nature-like bypasses to ensure habitat continuity for these species where there is sufficient space for a low gradient structure. Some commentators have suggested that nature-like bypasses are also an appropriate solution for migratory fish, but they often fail in this regard due to poor attraction (Bunt et al., 2012, 2016; Noonan et al., 2012; Kemp, 2016). This may mean that multiple fishways are required where the distributions of resident fish overlap with the routes of migratory species.

598 The BN for nature-like bypass design may be used in two ways: (i) to maximise
599 habitat suitability for a single species and life-stage; or (ii) to find distributions of
600 causal node states that maximise habitat suitability for all, or a subset, of species.
601 We recommend optimising design for all species simultaneously due to the
602 uncertainty arising from several factors. Firstly, Environmental Impact
603 Assessment (EIA) baseline data on the resident fish community may be
604 unavailable, incomplete or unreliable (Lacy et al., 2017). Secondly, the set of
605 resident species considered in Fish-Net is representative of the community that
606 could be encountered at a given site in Chile and the wider TSH. Finally,
607 uncertainty also comes from the description of species preferences in the
608 original CASiMiR model of García et al. (2011), which was specific to a single site
609 in the Biobío River, Chile, and focused on mean column velocity rather than the
610 velocity at the focal point of fish.

611

612 In addition to the habitat quality parameters considered in the BN for nature-like
613 bypass design (water velocity, depth, substrate), non-recreational fish also have
614 species-specific habitat associations with cover and turbulence (Wilkes et al.,
615 2016; Link et al., 2017). Whilst these factors are partially captured by substrate
616 and depth (which constitute two forms of cover as well as scaling parameters for
617 turbulence) the situation is more complex in reality (Lacey et al., 2012; Wilkes et
618 al., 2013). Furthermore, the BN contains no information on the spatial
619 relationships between depth and velocity, which may combine to form a
620 different habitat mosaic depending on whether they are coupled laterally (i.e.
621 thalweg-margin) or longitudinally (i.e. pool-riffle) (Stewardson \& McMahon,
622 2002). To minimise the uncertainty associated with optimal channel geometry,

nature-like bypasses should be designed by mimicking the local, least impacted channel form as closely as possible.

625

626 Downstream passage

627

628 For taxa with a swim bladder, our experts predicted an increase in mortality during downstream movement as the ratio between the acclimation and nadir pressure increased. Physoclistous taxa were predicted to have only a slightly higher mortality rate than physostomous taxa. This points to the rate of pressure change, which is typically very high during turbine entrainment, as an important factor; even with the ability to expel excess gases orally, physostomous taxa may still be susceptible to the rapidity of pressure fluctuations (Brown et al., 2012). However, it should be noted that the empirical data on physostome susceptibility to barotrauma only concerns a single species, Chinook salmon (Oncorhynchus tshawytscha, Salmonidae) (Brown et al., 2012; C. Boys, unpublished data). Our experts were more uncertain about barotrauma-related mortality for physoclists than other taxa, which is in agreement with empirical data showing a large degree of variation in barotrauma susceptibility among physoclistous taxa (Boys et al., 2016). Acclimation depth was less important in Fish-Net than the ratio of pressure change because its effect was already captured by the ratio of pressure change. Overall, results for barotrauma-related mortality were in agreement with the literature for the respective swim bladder types (Colotelo et al., 2012; Beirão et al., 2015; Boys et al., 2016; Fu et al., 2016). Predictions of non-zero mortality rates at a ratio of pressure change of $2(50 \%$ of acclimation pressure) for species with a swim bladder supports the precautionary recommendation of

648 Boys et al. (2016) that post-larval fish are not exposed to pressures less than $70 \%$ of their acclimated pressure.

651 Of the turbine designs considered, Fish-Net predicts a higher blade strike-related mortality for Kaplan than Francis models at all but the highest ratios of design discharge to actual discharge. This is surprising given previous work showing that Francis turbines are more damaging to fish because of their greater number of blades (Fu et al., 2016). This unexpected finding may be explained by several factors. Firstly, blade strike studies have not previously been conducted for fish as small as those considered in this study. Secondly, blade strike-related mortality through Francis and Kaplan turbines cannot be compared directly as they operate under different conditions, but power generation and discharge are not standardised in empirical studies (Fu et al., 2016). Finally, an operating discharge as low as $30 \%$ for Kaplan turbines, as considered in Fish-Net, may not be realistic; we are not aware of any studies assessing blade strike mortality for Kaplan turbines operating at such low discharges.

665 Fish-Net predictions for overall 72-hour mortality during downstream passage through turbines were less sensitive to fluid shear than other mortality sources. Probabilities for shear-related mortality derived from expert elicitation were in good general agreement with the literature (Neitzel et al., 2004; Deng et al., 2005; Boys et al., 2014). The relatively low contribution of fluid shear to overall mortality can be attributed to the fact that we only considered post-larval lifestages. The growing literature on the susceptibility of fish to shear forces points to a far greater impact on eggs and larvae (Čada et al., 1981; Čada, 1990, Killgore

et al., 2001; Boys et al., 2014). This raises serious problems in Neotropical systems in which many migratory fish have important downstream-drifting juvenile stages (Pelicice \& Agostinho, 2008; Godinho \& Kynard, 2009; Pompeu et al., 2012). Among non-recreational species of TSH, this life-history strategy is less common (Habit et al., 2006).

679 Limitations of the approach

681 Although we carefully constructed our expert elicitation protocol within a robust cognitive psychological and mathematical framework (de Little et al., 2018), we cannot rule out residual bias in probabilities derived from expert knowledge. Fish-Net probabilities derived from expert opinion may also be affected by the statistical treatment of the data gathered at the workshops. The MCE calculator optimises beta distributions by spreading residual uncertainty throughout the range 0-1 (Salomon, 2013). If experts report a best estimate not equal to 0.5 , any uncertainty (i.e. 1-confidence) serves to pull the mean of the conditional probability distribution closer to 0.5 .

691 In order to reduce the burden on experts, we fitted linear models to the distributions derived from the workshops. Whilst linear responses are consistent with the knowledge of our experts and the available empirical data on several sport species (e.g. Noonan et al., 2012; Bunt et al., 2012, 2016; Boys et al., 2016), we cannot rule out the possibility of non-symmetrical or complex relationships that are not captured in Fish-Net. This possibility could be reduced by asking experts more questions across the range of values of interest (e.g. for every value

of fishway length). However, time and 'expert fatigue' are likely to limit the number of questions that can reasonably be included in expert elicitation workshops (for guidance see Cain, 2001). Further biases potentially remaining despite the careful expert elicitation protocol used are discussed in detail by de Little et al. (2018).

A further limitation of the approach is common to all research on fishways that relies on the so-called 'fishway effectiveness' framework (Kemp \& O'Hanley, 2010; Cooke \& Hinch, 2013) to define how well a fishway is working. Implicit in the framework, which focuses on the percentage of fish passing the barrier, is the assumption that fishways should pass close to $100 \%$ of the population. However, this target is only valid in special cases where the critical habitats (e.g. for spawning, feeding) that a population needs to access are completely separated by the barrier. In many cases, $100 \%$ 'effectiveness' is not necessary and may even be damaging depending on the distribution of critical habitats (Pompeu et al., 2012). Further research should focus on more robust definitions of fishway effectiveness that are applicable to a wide range of fish populations.

Research priorities to improve fishway performance

Our findings help to identify needs for new and refocused fish passage research efforts. This includes the harmonisation of design parameters used by fishway designers and the variables considered in scientific research, which are currently mismatched. Contrast, for example, the causal nodes specified in Fish-Net with the foci of ecohydraulic research on fish locomotion (Lacey et al., 2012; Wilkes et

al., 2013). The latter tend to focus much more on the proximate hydraulic causes that may determine fishway success or failure (e.g. turbulent kinetic energy, dominant scales) than on the physical structures responsible for generating these conditions (Wilkes et al., 2018).

Our findings repeat calls for further research into the attraction and entrance of migratory fish to vertical slot and rock ramp fishways, long known to limit effectiveness (Katopodis \& Williams, 2012; Williams et al., 2012). They also call for more work on the hydraulic habitat preferences of resident populations expected to inhabit nature-like bypasses, the susceptibility of physoclistous fish to barotrauma and the blade strike-related mortality rates of a range of nonrecreational species. These research priorities are all associated with parts of Fish-Net exhibiting greater sensitivity and/or relatively high levels of uncertainty. This is particularly true of attraction efficiency, reinforcing the importance of recent work on optimal attraction flow design (e.g. Gisen et al., 2017).

Several lines of ecological research are also needed to support the application of Fish-Net findings. Firstly, new work is required to provide information on rates of fish exposure to potentially lethal physical forces found in turbine intakes and spillways. This will involve developing a better understanding of: (i) critical habitat requirements and spatial distributions; (ii) the degree of diadromy or potamodromy exhibited by individual populations; and (iii) the dispersal rates of resident species. Such evidence is critical to ensuring that fishways support, rather than deplete, aquatic biodiversity and sustainable fisheries (Pelicice \&

748 Agostinho, 2008; Godinho \& Kynard, 2009; Pompeu et al., 2012; Pelicice et al., 749 2017). Secondly, better development of the conceptual, methodological and 750 statistical frameworks underpinning fishway design and evaluation are urgently 751 required. The current framework emphasises only the proportion of fish able to 752 traverse the barrier, requiring data on upstream movement of fish individually 753 tracked using biotelemetry (Bunt et al., 2012). This is likely a result of the 754 historical focus of fish passage research on relatively large-bodied, strong 755 swimming, obligate migrators (i.e. diadromous salmonids).

757 For non-recreational fish that exhibit a wide range of movement ecologies, from 758 obligate migrator to almost sedentary (Reynolds 1983; O'Connor et al. 2003; 759 O'Connor et al. 2005; Buria et al. 2007; Piedra et al. 2012; Otturi et al. 2016), the 760 current composite fishway effectiveness metric is less relevant. Furthermore, 761 individual tracking using electronic tags is not an option with the majority of 762 non-recreational species, whose body size and sensitivity to handling would 763 confound the interpretation of biotelemetry data (M. Wilkes, unpublished data). 764 Finally, such priorities as defining critical habitats, exposure rates and 765 meaningful fishway performance metrics must be addressed through research 766 that is explicitly spatial and ecological in nature. Metapopulation theory, which 767 has been used to good effect in explaining the dynamics of fragmented 768 populations in other contexts (e.g. Padgham \& Webb, 2010), holds great 769 potential as the basis for a more robust conceptual and statistical underpinning 770 to fishway evaluations. By focusing on the dispersal rates necessary to support 771 viable populations, a metapopulation perspective can answer currently difficult 772 questions such as, what percentage of fish passing is sufficient? Metapopulation

models may show that expensive fishways are not always required, and may even be damaging to population viability in some situations (Pelicice et al., 2017).

776

777 Conclusions: Applying Fish-Net in the real world

778

779 In addition to hydropower applications, Fish-Net is appropriate for designing fishways in a variety of other contexts (e.g. irrigation weirs, road crossings).

781 Furthermore, our elicitation and modelling approach is suitable for implementation with any set of target species anywhere in the world. A crucial

783 advantage of our approach is that it considers upstream and downstream movement in equal measure, a feature that has been lacking from previous

785 frameworks (e.g. Calles \& Greenberg, 2009; Baumgartner et al., 2010; Kemp \& O'Hanley, 2010; Cooke \& Hinch, 2013). Particularly useful and original is our

787 algorithm for combining three major independent sources of mortality during turbine entrainment. This algorithm is available at http://martinwilkes.co.uk, along with all electronic files corresponding to the Bayesian networks for use in

790 Netica (Norsys Software Corporation, 2016).

791

792 The hydraulic boundary conditions affecting internal hydraulics of fishways
793 fluctuate because of variation in power generation and hydrology. Such dynamic
794 conditions may be reflected in Netica by entering a distribution of states for
795 causal nodes (e.g. head loss between pools, pressure change ratio). For
796 populations exhibiting movements within a defined period, the user should enter
797 findings into the BN that reflect expected conditions during this period. When

fishways are to be retrofitted to existing structures, Fish-Net can provide recommendations on the optimal design of technical fishways for projects with a total head of up to 10 m , or to define targets for exclusion of fish from turbine intakes. For new structures, the tool can be used to consider fishway design (upstream and downstream) as an integral part of the wider project. It can also provide a solid foundation for environmental impact assessment (EIA).

During the EIA process, authorities should consider compulsory submission of data relevant to Fish-Net causal nodes, including head- and tail- water dynamics, pressure and shear profiles through turbines and spillways, and detailed turbine design parameters for input into blade strike models. A more proactive use of Fish-Net would be in planning applications, where its outputs could be included as part of a multi-criteria decision support tool for prioritising locations for hydropower development and dam removal. The model can also support monitoring by providing expected proportions to guide power analysis and the evaluation of required sample sizes, as well as basic scientific research on fish passage by providing informative priors for Bayesian inference (see Low Choy et al., 2009, for example). Finally, while we encourage the research community to update Fish-Net predictions by collecting data on the performance of fishways, the probabilistic models presented here are currently the most robust and transparent basis for fishway design for non-recreational fish of TSH and, indeed, small-bodied fish around the world.

823 This work was funded by the European Commission through the Marie Sklodowska-Curie action, 'Knowledge Exchange for Efficient Passage of Fish in the Southern Hemisphere' (RISE-2015-690857-KEEPFISH). We would like to thank Brett Pflugrath of the University of New South Wales for taking part in the workshop on downstream passage, Daniel Gordon of Colbún and Cristian Rodríguez of the University of Concepción for providing turbine design parameters, Daniel Deng of the Pacific Northwest National Laboratory for advice on implementing blade strike models, support staff at the Department of Infrastructure Engineering, University of Melbourne, for organising the expert elicitation workshops, and Dominique Alò of Pontifical Catholic University of Chile, Santiago, for providing information to support our classification of native fish life-histories.

# Figures 

![img-0.jpeg](img-0.jpeg)

Fig. 1. Prototype Bayesian Networks for parts of Fish-Net populated using expert knowledge: (a) technical fishway design for catadromous and amphidromous species and (b) barotrauma and shear-related mortality rates during downstream passage through turbines and spillways. Combinations of causal node states connected to response nodes formed scenarios for the expert elicitation workshops. 'Distance from upstream limit' refers to the distance of the fishway entrance from the physical barrier or other (e.g. hydraulic) upstream limit of migration. 'Attraction flow' refers to the percentage of total streamflow discharged at the fishway entrance. 'Slot or gap width' refers to the slot width in a vertical slot fishway or the distance between rocks in a rock weir. 'Pool dimensions' are specified as three volume classes (length x width x depth): small ( $1.5 \times 1.1 \times 0.5 \mathrm{~m}$ ); medium ( $2.0 \times 1.5 \times 0.5 \mathrm{~m}$ ); and large ( $3.0 \times 2.0 \times 0.5 \mathrm{~m}$ ). 'Fishway length' is described as the number of pools.

![img-1.jpeg](img-1.jpeg)

Fig. 2. Prior probabilities for technical (upstream) fishway design. Example distributions shown for attraction flow given an entrance distance from upstream migration limit ( $L$ ) of (a) 0 m and (b) 95 m , and entrance distance from upstream migration limit given an attraction flow ( $Q_{\text {att }}$ ) of (c) $5 \%$ and (d) $15 \%$. Beta distributions for entrance efficiency given the head loss at the fishway entrance (e). Results for passage efficiency of two fishway types (f-k). Example distributions shown for fishway length given: (f) a 50 mm slot or gap width $(W)$, small pool volume $(V)$ and $60-90 \mathrm{~mm}$ head loss $(\Delta h)$; (g) a 50 mm slot or gap width, small pool and 130-200 mm head loss; (h) a 50 mm slot or gap width, large pool and $60-90 \mathrm{~mm}$ head loss; (i) a 250 mm slot or gap

width, small pool and 60-90 mm head loss; (j) a 250 mm slot or gap width, small pool and 130-200 mm head loss; (k) a 250 mm slot or gap width, large pool and 60-90 mm head loss. Circles represent mean 'most likely' (best) estimate of experts.

![img-2.jpeg](img-2.jpeg)

Fig. 3. Final Bayesian Network for technical (upstream) fishway design for catadromous and amphidromous species. Values given beneath nodes report the mean $\pm$ standard deviation for the uniform case, i.e. all node states equally probable. The .neta file corresponding to this Bayesian Network for use in Netica (Norsys Software Corporation, 2016) is available at http://martinwilkes.co.uk.

![img-3.jpeg](img-3.jpeg)

Fig. 4. Final Bayesian Network for nature-like bypass design for resident species. Causal nodes (velocity, substrate, depth) are set to optimise design for the whole community, for example by specifying variable depths and velocities reflecting lateral and/or longitudinal hydraulic variation within the bypass. Values given beneath nodes report the mean $\pm$ standard deviation for the uniform case, i.e. all node states equally probable. The .neta file corresponding to this Bayesian Network for use in Netica (Norsys Software Corporation, 2016) is available at http://martinwilkes.co.uk.

![img-4.jpeg](img-4.jpeg)

Fig. 5. Results for mortality rates during downstream passage. Example distributions shown for acclimation depth given a ratio of pressure change of 2 for (a) species with no swim bladder, (b) physoclistous species and (c) physostomous species, and pressure change ratio at an acclimation depth of 10 m for (d) species with no swim bladder, (e) physoclistous species and (f) physostomous species. Results for shear-related mortality (g). Results for blade strike mortality for four Francis turbines: (h) F05, (i) F05, (j) F09

and (k) F12, and three Kaplan turbines: (l) K02, (m) K03 and (n) K04. See Table S1 (Supplementary Material online) for turbine design parameters. Model results shown for three representative fish body lengths (TL). Circles represent mean 'most likely' (best) estimate of experts.

![img-5.jpeg](img-5.jpeg)

Fig. 6. Final Bayesian Network for mortality during downstream passage through turbines and spillways. Values given beneath nodes report the mean $\pm$ standard deviation for the uniform case, i.e. all node states equally probable. The .neta file corresponding to this

Bayesian Network for use in Netica (Norsys Software Corporation, 2016) is available at http://martinwilkes.co.uk.

![img-6.jpeg](img-6.jpeg)

Fig. 7. Worst (closed symbols) and best (open symbols) case scenarios for overall 72hour mortality rate during downstream passage through turbines given fish of three body lengths and three swim bladder types. Symbols show the mean and whiskers the range of model predictions. Jitter added to horizontal axis to assist interpretation. Model parameters for scenarios (best/worst) are: strain rate ( $\mathrm{cm} \mathrm{s}^{-1} \mathrm{~cm}^{-1}$ ) $=25 / 1000$; acclimation depth (m)=0/10; ratio of pressure change=2/10; turbine type (turbine)=Francis(F05)/Kaplan(K04); and relative discharge=1.0/0.3. For full details of the turbine design parameters see Table S1 (Supplementary Material online). The script for calculating the overall 72-hour mortality rate in R (R Core Team, 2015) is available at http://martinwilkes.co.uk.

![img-7.jpeg](img-7.jpeg)

Fig. 8. Mean predicted passage efficiency in Fish-Net as a function of maximum water velocity and energy dissipation. Scenarios shown for the minimum, mode and maximum of each head loss range. Colours of symbols represent head loss ranges, as specified in the legend. Lines represent recommendations from the literature for different groups of species.