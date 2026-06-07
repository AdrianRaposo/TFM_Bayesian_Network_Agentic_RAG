# 5 <br> Universiteit Antwerpen 

## This item is the archived peer-reviewed author-version of:

Risk-based design of process plants with regard to domino effects and land use planning

## Reference:

Khakzad Nima, Reniers Genserik.- Risk-based design of process plants with regard to domino effects and land use planning Journal of hazardous materials - ISSN 0304-3894 - 299(2015), p. 289-297
Full text (Publisher's DOI): http://dx.doi.org/doi:10.1016/J.JHAZMAT.2015.06.020
To cite this reference: http://hdl.handle.net/10067/1264650151162165141

Elsevier Editorial System(tm) for Journal of Hazardous Materials
Manuscript Draft

Manuscript Number: HAZMAT-D-15-01256
Title: Risk-based design of process plants with regard to domino effects and land use planning
Article Type: Research Paper
Keywords: Bayesian network; Domino effect; Land use planning; Multi-criteria decision analysis; Fuel storage plant.

Corresponding Author: Dr. Nima Khakzad, Ph.D.
Corresponding Author's Institution: Memorial University of Newfoundland
First Author: Nima Khakzad, Ph.D.
Order of Authors: Nima Khakzad, Ph.D.; Genserik Reniers, PhD
Abstract: Land use planning (LUP) as an effective and crucial safety measure has widely been employed by safety experts and decision makers to mitigate off-site risks posed by major accidents. Accordingly, the concept of LUP in chemical plants has traditionally been considered from two perspectives: (i) land developments around existing chemical plants considering potential off-site risks posed by major accidents and (ii) development of existing chemical plants considering nearby land developments and the level of additional off-site risks the land developments would be exposed to. However, the attempts made to design chemical plants with regard to LUP requirements have been few, most of which have neglected the role of domino effects in risk analysis of major accidents. To overcome the limitations of previous work, first, we developed a Bayesian network methodology to calculate both on-site and off-site risks of major accidents while taking domino effects into account. Second, we combined the results of risk analysis with Analytic Hierarchical Process to design an optimal layout for which the levels of on-site and off-site risks would be minimum.

Dear Editor,
The present work is the result of a research concentrating on risk-based design of chemical plants considering land use planning (LUP) and domino effects obligation and requirements in design. We believe the methodology developed in this work can effectively be used for inherently safer design of major hazard installations such as chemical plants. In addition, the manuscript word count is 4967, including the abstract, keywords, text, figure captions, table legends, and appendix, but excluding the title page and the references.

We are pleased to submit the result of our research for possible publication in the Journal of Hazardous Materials.

Sincerely yours
Nima Khakzad (Memorial University of Newfoundland)
Genserik Reniers (TUDelft)

We have developed a methodology to risk-based design of chemical plants. The novelty of the work can be summarized as follow:
(i) An innovative Bayesian network methodology is developed to estimate the total probability of accidents in a chemical plant considering both individual accidents and potential domino effects. The methodology can be extended to account for on-site and off-site risks.
(ii) The results of the risk analysis were used in analytic hierarchical process to find an optimal layout for a chemical plant so that the requirements of land use planning can be met.

# Highlights (for review) 

- A Bayesian network methodology has been developed to estimate the total probability of major accidents in chemical plants.
- Total probability of accidents includes the probability of individual accidents and potential domino effects.
- The methodology has been extended to calculate on-site and off-site risks.
- The results of the risk analysis have been used in a multi-criteria decision analysis technique to risk-based design of chemical plants.

# Risk-based design of process plants with regard to domino effects and land use planning 

Nima Khakzad ${ }^{a}$, Genserik Reniers b,c,d

Nima Khakzad, PhD.
Email: nkhakzad@gmail.com
Phone: +17097692345

Genserik Reniers, PhD. (Professor)
Email: G.L.L.M.E.Reniers@tudelft.nl
Phone: +31 152783749
a. Safety and Risk Engineering Group (SREG), Memorial University of Newfoundland, St. John's, NL, Canada A1B 3X5
b. Safety and Security Science Group (S3G), Faculty of Technology, Policy and Management, TU Delft, 2628 BX Delft, The Netherlands
c. Antwerp Research Group on Safety and Security (ARGoSS), Faculty of Applied Economics, Universiteit Antwerpen, 2000 Antwerp, Belgium
d. Research Group CEDON, Campus Brussels, KULeuven, 1000 Brussels, Belgium

.

# Abstract 

Land use planning (LUP) as an effective and crucial safety measure has widely been employed by safety experts and decision makers to mitigate off-site risks posed by major accidents. Accordingly, the concept of LUP in chemical plants has traditionally been considered from two perspectives: (i) land developments around existing chemical plants considering potential off-site risks posed by major accidents and (ii) development of existing chemical plants considering nearby land developments and the level of additional off-site risks the land developments would be exposed to. However, the attempts made to design chemical plants with regard to LUP requirements have been few, most of which have neglected the role of domino effects in risk analysis of major accidents. To overcome the limitations of previous work, first, we developed a Bayesian network methodology to calculate both on-site and off-site risks of major accidents while taking domino effects into account. Second, we combined the results of risk analysis with Analytic Hierarchical Process to design an optimal layout for which the levels of on-site and offsite risks would be minimum.

Key words: Bayesian network; Domino effect; Land use planning; Multi-criteria decision analysis; Fuel storage plant.

## 1. Introduction

Early applications of LUP to major accidents in Europe dates back to the early 1970s when the Flixborough disaster in 1974 in the UK led to the Act 1974, requiring industries to keep internal risks (on-site risks) as well as external risks (off-site risks) as low as reasonably practicable (HSE 2014). Accordingly, local planning authorities have been obliged to obtain advice from HSE in the case of land developments around major hazard installations (MHIs) (Franks 2004; HSE 1989, 2014).

The majority of relevant work over the past two decades, however, has been inspired by the EU Council Directive 96/82/EC, also known as Seveso Directive II. Articles 8 and 12 of the Seveso II explicitly mandates the EU Member States to consider domino effects and land use planning, respectively, for the prevention of major accidents and the limitation of their consequences to man and the environment. Article 12 is mainly devoted to (i) sitting of new installations, (ii)

modification to existing installations, and (iii) land developments in the vicinity of existing installations, particularly those developments which would increase either the population at risk or the severity of the risk. In other words, it does not apply to an existing installation unless there are any internal modifications to the plant or external land developments in the vicinity of the plant.

Provision of domino effect in Seveso II has been made to ensure adequate internal safety distances among the units of a MHI where it is possible that a major accident in a unit propagates to neighboring units, triggering other secondary accidents. Likewise, requirements of LUP have been included in Seveso II to warrant adequate external safety distances between a MHI and residential areas, areas of public use, or areas of particular natural sensitivity and interest (Christou et al., 2006). From 1 June 2015, the new Seveso Directive III comes into force in Europe, containing the same LUP philosophy as its predecessor Seveso II.

LUP has traditionally been considered from two perspectives: (i) land use development in the vicinity of an existing MHI and (ii) modification/development of an existing MHI considering nearby existing land developments. From the first perspective, off-site individual risk or societal risks are calculated for an MHI considering major accident scenarios (Laheij et al., 2000; Taveau, 2010; Hauptmanns, 2005; Cozzani et al., 2014; Kontic and Kontic, 2009). Accordingly, pieces of land in the vicinity of MHI are designated to particular developments based on their vulnerability and the levels of risks they are exposed to. The role of domino effects (chain of accidents), however, has barely been considered in the calculation of off-site risks (Cozzani et al., 2014).

According to the second perspective, however, LUP requirements have been considered in multicriteria decision analysis (MCDA) in order to develop or modify existing MHIs (Papazoglou et al., 2000; Sebos et al., 2010; Bernechea and Arnaldos, 2014) such that the modifications would decrease or at least not increase the level of off-site risks. In the previous attempts, however, either the effect of domino effects has been neglected (e.g., Papazoglou et al. (2000)) or the total risk comprising on-site and off-site risks has been considered as a single decision criterion (e.g., Bernechea and Arnaldos (2014)). While the ignorance of domino effects could result in underestimation of accident probabilities and thus the value of risk, aggregation of on-site and off-site risks into a single risk value could significantly overshadow the requirements of LUP in

the decision analysis. For example, a plant with a lower aggregate risk is likely to be chosen over another plant with a slightly higher aggregate risk even if the former plant might have violated the LUP obligations.

The present study to some extent belongs to the second perspective in the sense that it considers LUP requirements to design (not develop or improve) an optimal layout for an MHI. To overcome the drawbacks of previous work, the impact of domino effect is explicitly included in the risk analysis of major accidents, and instead of aggregating on-site and off-site risks; a MCDA technique, Analytic Hierarchical Process (AHP), is employed to account for on-site and off-site risks as separate decision criteria. Thus, it would be possible to prioritize plant layout alternatives and choose the one which best meets the constraints of the problem without compromising off-site risk for on-site risk or vice versa. To calculate the on-site and off-site we modify a Bayesian network (BN) methodology introduced by Khakzad et al. (2013). The application of the developed BN in conjunction with AHP to risk-based design of chemical plants is demonstrated via a fuel storage plant.

# 2. Risk-based land use planning 

Several methods have been adapted around the world to implement LUP such as the method of generic distances, consequence-based method and risk-based method. These methods are not necessarily contradictory, and in most cases a combination of them are employed (hybrid methods). Comprehensive reviews and comparisons of conventional LUP methods adapted within European countries have been discussed by Papazoglou et al. (1998), Christou et al. (1999, 2011), Cozzani et al. (2006), Basta et al. (2007), Demichela et al. (2014), Pasman and Reniers (2014).

The risk-based method includes several steps: (i) to identify and estimate the probability of potential accident scenarios, (ii) to identify and estimate the intensity of physical effects ${ }^{1}$ (e.g., heat radiation, overpressure, toxic concentration), (iii) to estimate the adverse effects of the physical effects on exposed population, and (iv) to analyze off-site risks in form of individual risk (IR) contours or societal risk curves (F-N curve) (Christou et al., 2006). Quantitative risk

[^0]
[^0]:    ${ }^{1}$ In the case of off-site risk analysis, the physical effects are also referred to dangerous doses if they result in distress of all population, medical attention of a majority or hospitalization of a minority of people, or fatality of $1 \%$ of population.

analysis methods are usually applied to estimate the probabilities of potential accidents while dose-effect relationships and probit models are used to estimate the adverse effects of the physical effects on off-site targets (usually human).

Figure 1 depicts a buffer distance comprising three zones separated by IR contours, resulting from a risk-based approach adopted in the UK. Circumventing an MHI (Figure 1(a)) or a hazardous pipeline (Figure 1(b)), the boundaries of the inner zone (IZ), the middle zone (MZ), and the outer zone (OZ) are identified by IR contours corresponding to $10^{-5}, 10^{-6}$, and $3 \times$ $10^{-7}$, respectively (HSE 2014; PADHI, 2011). Land developments inside a buffer zone should be limited according to the magnitude of IR and vulnerability and number of population at risk. To this end, for example, the HSE of the UK has defined 4 levels of vulnerability for land developments: level 1 including factories with limited number of employees; level 2 including residential houses with limited number of residents; level 3 including primary schools and old people homes; and level 4 including football stadiums and large hospitals.

Figure 1. Buffer zone around a major hazard installation (a) and a pipeline (b) (PADHI, 2011).

Based on these vulnerability levels and amount of IRs, the following decision matrix (Table 1) can be used to Advise Against (AA) or Not to Advise Against (NAA) land developments (PADHI, 2011).

Table 1. Decision matrix used by HSE for risk-based LUP (PADHI, 2011). AA: Advise Against development; NAA: Not Advise Against development.

# 3. An integrated Bayesian network to risk analysis 

To estimate either on-site or off-site risks posed by an MHI, the probabilities of major accidents within the MHI should be determined. For this purpose, the total probability of accident should be determined for each unit of the MHI. The total probability of a unit consists of the probability

of individual accidents in the unit and also the probabilities of accidents in the unit triggered by domino effects, i.e., domino-induced accidents.

Khakzad et al. (2013) introduced a methodology based on BN to model and calculate the probability of domino effects in chemical plants. In their methodology, a primary unit has to be identified as the starting point to develop the BN and thus to model the domino effect. A BN which is developed this way thus cannot account for all possible domino effects with different starting points within a chemical plant. As a result, the total probability of accident in a unit would be underestimated since not all the possible domino effects impacting the unit can be modeled by the BN.

To relax this drawback, we modified the BN introduced by Khakzad et al. (2013) so that the total probability of accident for each unit can be estimated by considering multiple domino effects using a single BN. Figure 2 presents the modified methodology in six steps.

Step 1: According to safety reports and layout of the chemical plant, critical units are identified. Critical units are those with significant inventories of flammable/explosive substances which have the potential to cause credible on-site or off-site damages. These units are likely to initiate a domino effect or facilitate the propagation of an on-going domino effect. These units can be presented as nodes of the BN.

Step 2: Considering factors such as the chemical characteristics of the contained substance, the physical and operational conditions under which the chemical substance is being processed/stored, type of release, and environmental conditions, a number of accident scenarios can be envisaged for each critical unit.

Step 3: Using historical data, databases, and expert judgment, probabilities of individual accidents (disregarding the impact of domino effects) can be estimated. To this end, accident probabilities for a number of units have been calculated and presented in relevant databases and manuals such as FRED (2012) and Bevi Manual (2009). The calculated probabilities in this step are stored to be later used in populating the conditional probability tables of the BN.

Step 4: Based on the type of accidents determined in Step 2, the type and magnitude of escalation vectors between each pair of units are determined. Escalation vectors are physical

effects such as heat radiation and explosion overpressure generated by accidents. Methods to calculate the intensity of escalation vectors can be found in CCPS (2000) and Yellow Book (1997).

Figure 2. Procedure to calculate the total probability of accidents for a unit.

Step 4.1: For an escalation vector to cause credible damage to a target unit and thus escalate the accident, its magnitude should be greater than some threshold values. In other words, if the magnitude of an escalation vector is less than the respective threshold value, the probability of damage would be deemed negligible. Thus, only escalation vectors which exceed predefined threshold values are kept in the modeling.

Step 4.2: The escalation vectors which were calculated in Step 4.1 will be used as the arcs of the BN. Since BN is a directed acyclic graph (Pearl, 1988), it is not permitted to have mutual arcs between any pair of nodes which otherwise would violate the axiom of acyclicity. To overcome this, when there are reciprocal escalation vectors between a pair of units, the smaller escalation vector is eliminated from the BN. Although this simplification is likely to eliminate the possibility of a domino effect which would have been triggered by the smaller escalation vector, it still holds the possibility of a more probable domino effect between the two units by keeping the larger escalation vector.

It is worth noting that when the maintenance of a larger escalation vector could prevent a cycle between a pair of nodes but result in another larger cycle within the BN, the smaller escalation vector takes precedence over the larger escalation vector and remains in the modeling. Nevertheless, such a situation would be rare due to the prevailing direction of wind in the chemical plant of interest.

Step 4.3: The escalation vectors identified in previous steps will act as the arcs of the BN. Up to this point; the BN has qualitatively been developed.

Step 5: To estimate the probability of domino-induced accidents, the damage probabilities of target units should be calculated. Among methods proposed to calculate damage probabilities, probit functions have widely been used because of their simplicity and flexibility. Using probit functions, first a probit value, $Y$, is calculated as $Y=a+b \ln (E V)$, where $E V$ is the magnitude of the escalation vector or a related parameter, and a and b are constant coefficients. Having Y determined, the damage probability, P , can be calculated as $\mathrm{P}=\varphi(\mathrm{Y}-5)$, where $\varphi($.$) is the$ cumulative density function of standard normal distribution.

Step 6: In order to quantify the BN and calculate the total probability of accident for each unit, conditional probability tables (CPTs) of the BN have to be developed. For this purpose, the probabilities of individual accidents (Step 3) and domino-induced accidents (Step 5) can be combined using a Leaky Noisy OR (Khakzad et al., 2013, 2014)

Using the BN developed in the previous section the total probability of accident for each unit can be calculated. Having total probabilities, it is possible to estimate the risks of damage to the units. Furthermore, the BN can further be extended to account for off-site risks at multiple points of interest. Knowing the total probability of accidents, the magnitudes of dangerous doses at different distances from critical units can be determined using the methods earlier mentioned in Section 3.1.

Depending on the type of the target of interest (e.g., building or human) and the level of damage (minor or major damage in case of buildings, and $2^{\text {nd }}$ degree burns or fatality in case of human) a variety of probit functions or dose-effect relationships can be employed to estimate the damage probabilities (e.g., see Assael and Kakosimos, 2010)

# 4. Application of the methodology 

### 4.1. Case study

Consider a hypothetical fuel storage plant (Figure 3) which is planned to sit near a residential area and a hospital. The plant is required to store $24000 \mathrm{~m}^{3}$ of crude oil in atmospheric storage tanks. Furthermore, the distances from the centre of the plant to the residential area and the hospital are 100 m and 150 m , respectively.

Figure 3. A hypothetical fuel storage plant.

The aim is to find an optimal layout for the storage plant of interest for which required resources, on-site risks and off-site risks would be the lowest. To this end, six alternatives are considered as potential layouts for the storage plant (Figure 4). The specifications of the layouts and the storage tanks are listed in Table 2. Also, the safety distances among the storage tanks in each layout have been determined based on the volume and diameter of storage tanks as suggested by Flammable Liquids Bulk Storage Regulations of Canada (2014).

Figure 4. Alternatives for the layout of the fuel storage plant.

Table 2. Characteristics of plant layouts and storage tanks.

# 4.2. Results 

### 4.2.1. Required resources

In the present study, we assume that only influential resources are the required land to sit the storage tanks and the budget required to supply storage tanks. The land can be estimated for each layout as the area $\left(\mathrm{m}^{2}\right)$ occupied by the storage tanks and the safety distances among them. Approximate cost of storage tanks (USD) can also be calculated from a variety of sources (e.g., www.matche.com). The required land and total cost for each layout have been listed in column 3 and 4 of Table 3.

Table 3. Characteristics of plant layouts regarding required resources, on-site risk, and off-site risks.

### 5.2.2. On-site risks

To calculate on-site risks (i.e., risk of damage to storage tanks and the loss of chemical inventory), plant layouts (Figure 4) are modeled using the BN methodology developed in Section

3. For this purpose, each storage tank is considered as a critical unit and thus identified as a node of BN (Step 1 in Figure 2). Considering the type of storage tanks (atmospheric) and contained chemical (crude oil), the most credible accident scenario for storage tanks is identified as a major release of oil leading to a pool fire given an ignition source. This accident scenario holds for either individual accidents or domino-induced accidents (Step 2 in Figure 2).

To estimate the probability of a pool fire as an individual accident (which can also serve as the probability of the primary accident in a domino effect), the probabilities of a major release from a large storage tank ( $\mathrm{V} \geq 450 \mathrm{~m}^{3}$ ) and ignition are determined $1.0 \mathrm{E}-04$ and $3.0 \mathrm{E}-01$, respectively (FRED, 2012). Accordingly, the probability of a pool fire is calculated as 3.0 E-05 (Step 3 in Figure 2). In order to calculate the magnitude of escalation vectors (heat radiation in this example), the ALOHA software tool is used in the present study (Step 4 in Figure 2).

The following input data has been used in ALOHA to calculate the magnitude of heat radiation at different locations: a wind speed of $10 \mathrm{~m} / \mathrm{s}$ measured at 10 m above the ground and gusting from the north west; air temperature of $15^{\circ} \mathrm{C}$; relative humidity of $25 \%$, a clear sky, and stability class of D. Furthermore, the diameters of release opening for storage tanks have been determined as 0.01 of the respective tank diameter. In addition, the location of release has been decided on the bottom of storage tanks, resulting in the worst release scenario. For example, magnitudes of heat radiation for the plan layout depicted in Figure 4(3) have been listed in Table 4 (columns 25).

Table 4. Heat radiation $\left(\mathrm{kW} / \mathrm{m}^{2}\right)$ at different locations resulting from pool fires in storage tanks of plant layout shown in Figure 4(3).

Considering a threshold value of $\mathrm{Q}_{\mathrm{th}}=15 \mathrm{~kW} / \mathrm{m}^{2}$ (Cozzani et al., 2009) for heat radiation, only those heat radiations whose magnitude is greater than or equal to $15 \mathrm{~kW} / \mathrm{m}^{2}$ are kept in the analysis (e.g., bold numbers in Table 4) (Step 4.1 in Figure 2). Figure 5(1) illustrates the plant layout of Figure 4(3) in which only heat radiations which are greater than or equal to $\mathrm{Q}_{\mathrm{th}}=15$ $\mathrm{kW} / \mathrm{m}^{2}$ have been presented. As pointed out in Step 4.2 in Figure 2, in case of having reciprocal escalation vectors only the larger one is considered in the analysis. Figure 5(2) depicts the same

plant layout as Figure 5(1) where smaller heat radiations (shown in dotted arcs) have been removed. The remained heat radiations are employed as the arcs of the BN.

Figure 5. Figure 5(1) depicts the storage plant of Figure 4(3) along with heat radiations greater than or equal to Qth $=15 \mathrm{~kW} / \mathrm{m} 2$. Figure 5(2) shows the final BN where smaller heat radiations have been eliminated. Figure 5(3) presents the extended BN to calculate off-site individual risks at hospital (H) and residential house (R).

In order to calculate the damage probabilities we employ probit functions suggested by Cozzani et al. (2009) (Step 5 in Figure 2):
$\mathrm{Y}=12.54-1.847(-1.13 \ln (\mathrm{Q})-2.67 \mathrm{E}-05 \mathrm{~V}+9.9)$
where Y is the probit value, $\mathrm{Q}\left(\mathrm{kW} / \mathrm{m}^{2}\right)$ is the magnitude of heat radiation received by an atmospheric storage tank, and $\mathrm{V}\left(\mathrm{m}^{3}\right)$ is the volume of the storage tank. The conditional damage probability can then be calculated using $\mathrm{P}=\varphi(\mathrm{Y}-5)$.

Considering the probabilities of individual pool fires and domino-induced pool fires, the total probability of pool fire in a storage tank can be estimated using a Leaky Noisy-OR gate (Khakzad et al., 2013, 2014) (Step 6 in Figure 2).

Having the total probability of pool fire for each storage tank, the value of risk for a storage tank can be calculated as the product of the total probability and the monetary value of each storage tank, that is, the cost of the tank plus the value of its chemical content. It is assuming that during a pool fire the storage tank and the entire chemical inventory would be lost, considering the price of $1 \mathrm{~m}^{3}$ of crude oil as 315 USD. The values of on-site risk for each layout of Figure 4 are listed in column 5 of Table 3.

# 5.2.3. Off-site risks 

After total probabilities of pool fires for storage tanks are estimated, the off-site risks of plants can readily be calculated. To this end, first the magnitudes of heat radiation at residential area and hospital are determined. Having this, the probability of death for a human agent, IR, is estimated using the dose-effect relationship (Yellow Book, 1997):
$\mathrm{Y}=-36.38+2.56 \ln \left(\mathrm{t}_{\text {eff }} \cdot \mathrm{Q}^{4 / 3}\right)$
where $t_{\text {eff }}(\mathrm{s})$ represents a human's exposure time to heat radiation, and $\mathrm{Q}\left(\mathrm{W} / \mathrm{m}^{2}\right)$ is the magnitude of heat radiation received by human. In the present study, the exposure time has been determined as 60 s . The conditional probability of death given a certain amount of heat radiation can thus be calculated using $\mathrm{P}=\varphi(\mathrm{Y}-5)$. The total probability of death is thus equal to the product of the total probabilities of pool fires and the conditional probabilities of death. For this purpose, the BN can be extended as shown in Figure 5(3) to account for the total IR at the targets R and H. Following the same procedure, total IR for the plants depicted in Figure 5 have been calculated and presented in columns 6 and 7 of Table 3.

### 5.2.4. Application of AHP

Analytic hierarchical process (AHP) (Saaty, 2008) is a multi-criteria decision analysis (MCDA) technique consisting of a set of decision criteria and decision alternatives. Decision criteria are influential decision factors based on which the optimal decision alternative is to be selected. In AHP, decision criteria are compared pairwise and weighted according to their relative importance to the decision to be made. Similarly, the decision alternatives are compared pairwise and weighted against each decision criterion. Weights are assigned based on a fundamental scale table (Saaty, 2008), ranging from 1 to 9 . The results of the pairwise comparisons are populated in respective matrices. The normalized elements of the principal right eigenvector of each matrix represent the local rank of each decision criterion and decision alternative. Final rank of each decision alternative can subsequently be determined using the local ranks of the decision alternative and the local ranks of each decision criterion. Accordingly, the decision alternative with the highest final rank is selected as the optimal decision.

Considering the characteristics of plant layouts listed in Table 3, the most optimal layout is the one for which the required resources as well as the on-site (asset damages) and off-site risks (IR)

are the lowest. However, in the case of having conflicting decision criteria, which is the case in most MCDA applications, an optimal decision is less likely to satisfy all decision criteria. For example, to decrease off-site risks of a fuel storage plant with a predefined inventory of fuel, the fuel content of storage tanks can be reduced. This, however, demands for a larger number of storage tanks which in turn not only requires more resources (such as land) but also increases the possibility of domino effects and thus increases on-site risks.

To find an optimal plant layout, an AHP can be developed (Figure 6) comprising a decision "optimal layout", three decision criteria "resources", "on-site risk", and "off-site risk", and six decision alternatives, i.e., plants depicted in Figure 4. The decision criteria "resources" and "offsite risk" are subsequently decomposed to sub-criteria "land" and "budget", and "residential houses" and "hospital", respectively. Next steps are (i) to rank the decision criteria according to the optimal decision, (ii) to rank sub-criteria considering their contributions to the criteria, and (iii) to rank decision alternatives considering their importance to decision sub-criteria and criteria.

To rank the decision criteria against the decision, it has been assumed that among the criteria, the off-site risk should be given more priority over the on-site risk, and the on-site risk should be emphasized more than required resources. As such, using the fundamental scale table (Saaty, 2008), the weights of the decision criteria have been presented in Table 5 (columns 2-4). The normalized values of the principal eigenvector of the resulting matrix represent be the ranks of the decision criteria according to the decision (column 5 of Table 5).

Figure 6. AHP for layouts shown in Figure 4.

Table 5. Pairwise comparison of decision criteria and their rank according to the decision.

Similarly, the pairwise comparison of sub-criteria "land" and "budget" against the criterion "resources" along with the pairwise comparison of "residential houses" and "hospital" against the criterion "off-site risk" have been listed in Tables 6 and 7 respectively. These weights have

been assigned assuming that the initial budget is a more important decisive factor than available land (perhaps due to the availability of extra land but scarcity of the budget) while IR at the hospital is more critical than that at the residential houses (due to a higher population density and relatively higher vulnerability of a hospital compared to residential houses).

Table 6. Pairwise comparison of land and budget according to resources.

Table 7. Pairwise comparison of residential houses and hospital according to off-site risk.

To rank decision alternatives, i.e., plant layouts, against the above-mentioned criteria and subcriteria, the problem constraints should be taken into account. Without loss of generality, assume that the desired amount of land available for the storage plant is about $7500 \mathrm{~m}^{2} \pm 10 \%$ while the available budget to supply storage tanks is 2,000,000 USD $\pm 15 \%$.

To set a constraint on the on-site risk, it is decided that the risk of on-site damages should be limited to 3.00 E - 05 times the sum of the initial budget (i.e., 2,000,000 USD) and the value of fuel content $\left(24,000 \mathrm{~m}^{3}\right)$. Considering a value of $315 \mathrm{USD} / \mathrm{m}^{3}$ for crude oil, the amount of the on-site risk thus should not exceed $3.00 \mathrm{E}-05 \times(2,000,000+24,000 \times 315)=312$ USD. Moreover, following the risk-based approach of LUP suggested by HSE of UK (PADHI, 2011), the amount of individual risks at residential houses and the hospital should not exceed $1.00 \mathrm{E}-05$ and $3.00 \mathrm{E}-07$, respectively.

In order to explain how the foregoing restrictions can be employed to pairwise comparison and weighting of decision alternatives; consider a case where the plant layouts are to be compared based on the required land. Since the desired land is $7500 \mathrm{~m}^{2} \pm 10 \%$, that is (7500-750, $7500+750$ ), a scale such as the one depicted in Figure 7 can be used to weight plant layouts based on a comparison between their required land and the desired land. For example, comparing layouts 2 and 3 in Figure 4, layout 2 requires $8100 \mathrm{~m}^{2}$ of land which is $600 \mathrm{~m}^{2}$ more than 7500 $\mathrm{m}^{2}$ but still in the desired range. On the other hand, layout 3 requires $6000 \mathrm{~m}^{2}$ of land which is much less than the desired range. Although both layouts do not violate the restriction set by

"desired land", layout 3 is still moderately favored over layout 2 due to $2100 \mathrm{~m}^{2}$ saving in land. As another example, consider layouts 3 and 6 in Figure 4, where layout 6 requires $9000 \mathrm{~m}^{2}$ of land which is $750 \mathrm{~m}^{2}$ more than the desired range. In this case, layout 3 is extremely preferred to layout 6 .

The results of the pairwise comparison of plants according to "land" have been presented in Table 8. Similar tables for comparisons with regard to budget, on-site risk, and off-site risks at residential houses, and the hospital have been presented in Appendix I. Having the local ranks of the plants, the overall rank of each plant can be calculated as shown in Figure 8. As can be seen, the most three preferable plants are identified as layouts 6,5 , and 1 , respectively.

Figure 7. Scale used to pairwise comparison of plants according to land.

Table 8. Pairwise comparison of layouts according to land.

Figure 8. Final rank of plant layouts.

# 6. Conclusion 

In this study we have introduced an innovative methodology based on BN to calculate on-site and off-site risks of chemical plants. The developed methodology is able to estimate the total probability of accidents for units of a chemical plant, taking into account individual accidents and credible domino-induced accidents. We also illustrated that the developed BN can readily be extended to calculate the level of individual risks at arbitrary targets in the vicinity of the plant.

The developed BN can be combined by MCDA techniques such as AHP for risk-based design of chemical plants. The outcome such a MCDA would be a plant layout with specific number of storage tanks, inventory, and arrangement, for which the restrictions set by on-site risks and offsite risks would be satisfied more effectively. The application of the methodology was

demonstrated via a fuel storage plant with pool fire as the dominant accident scenario; however, it can effectively be applied to a wide range of chemical plants with a variety of hazardous units and multiple accidents scenarios.

# Appendix I 

Table AI (1). Pairwise comparisons of layouts according to budget.

Table AI (2). Pairwise comparisons of layouts according to on-site risk.

Table AI (3). Pairwise comparisons of layouts according to off-site risk at residential houses.

Table AI (4). Pairwise comparisons of layouts according to off-site risk at hospital.

Table 1. Decision matrix used by HSE for risk-based LUP (PADHI, 2011). AA: Advise Against development; NAA: Not Advise Against development.


Table 2. Characteristics of plant layouts and storage tanks.


Table 3. Characteristics of plant layouts regarding required resources, on-site risk, and off-site risks.


Table 4. Heat radiation $\left(\mathrm{kW} / \mathrm{m}^{2}\right)$ at different locations resulting from pool fires in storage tanks of plant layout shown in Figure 4(3).


Table 5. Pairwise comparison of decision criteria and their rank according to the decision.


Table 6. Pairwise comparison of land and budget according to resources.


Table 7. Pairwise comparison of residential houses and hospital according to off-site risk.


Table 8. Pairwise comparison of layouts according to land.


Table AI (1). Pairwise comparisons of layouts according to budget.


Table AI (2). Pairwise comparisons of layouts according to on-site risk.


Table AI (3). Pairwise comparisons of layouts according to off-site risk at residential houses.


Table AI (4). Pairwise comparisons of layouts according to off-site risk at hospital.


![img-0.jpeg](img-0.jpeg)

Figure 1. Buffer zone around a major hazard installation (a) and a pipeline (b) (PADHI, 2011).

![img-1.jpeg](img-1.jpeg)

Figure 2. Procedure to calculate the total probability of accidents for a unit.

![img-2.jpeg](img-2.jpeg)

Figure 3. A hypothetical fuel storage plant.

![img-3.jpeg](img-3.jpeg)

Figure 4. Alternatives for the layout of the fuel storage plant.
![img-4.jpeg](img-4.jpeg)

Figure 5. Figure 5(1) depicts the storage plant of Figure 4(3) along with heat radiations greater than or equal to Qth $=15 \mathrm{~kW} / \mathrm{m} 2$. Figure 5(2) shows the final BN where smaller heat radiations have been

eliminated. Figure 5(3) presents the extended BN to calculate off-site individual risks at hospital (H) and residential house (R).
![img-5.jpeg](img-5.jpeg)

Figure 6. AHP for layouts shown in Figure 4.
![img-6.jpeg](img-6.jpeg)

Figure 7. Scale used to pairwise comparison of plants according to land.

![img-7.jpeg](img-7.jpeg)

Figure 8. Final rank of plant layouts.
