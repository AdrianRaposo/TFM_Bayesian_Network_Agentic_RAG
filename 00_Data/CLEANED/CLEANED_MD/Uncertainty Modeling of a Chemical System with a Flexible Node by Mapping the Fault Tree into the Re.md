# TUDelft 

Delft University of Technology

## Uncertainty Modeling of a Chemical System with a Flexible Node by Mapping the Fault Tree into the Response Surface Method

Modi, Siddharth; Srinivasa Rao, Meka; Gupta, T.C.S.M.; Yang, M.

## DOI

10.1021/acs.iecr.2c03329

## Publication date

2023

## Document Version

Final published version

## Published in

Industrial and Engineering Chemistry Research

## Citation (APA)

Modi, S., Srinivasa Rao, M., Gupta, T. C. S. M., \& Yang, M. (2023). Uncertainty Modeling of a Chemical System with a Flexible Node by Mapping the Fault Tree into the Response Surface Method. Industrial and Engineering Chemistry Research, 62(7), 3206-3220. https://doi.org/10.1021/acs.iecr.2c03329

## Important note

To cite this publication, please use the final published version (if applicable).
Please check the document version above.

## Copyright

Other than for strictly personal use, it is not permitted to download, forward or distribute the text or part of it, without the consent of the author(s) and/or copyright holder(s), unless the work is under an open content license such as Creative Commons.

## Takedown policy

Please contact us and provide details if you believe this document breaches copyrights.
We will remove access to the work immediately and investigate your claim.

# Green Open Access added to TU Delft Institutional Repository 

'You share, we take care!' - Taverne project
https://www.openaccess.nl/en/you-share-we-take-care

Otherwise as indicated in the copyright section: the publisher is the copyright holder of this work and the author uses the Dutch legislation to make this work public.

# Uncertainty Modeling of a Chemical System with a Flexible Node by Mapping the Fault Tree into the Response Surface Method 

Siddharth Modi, Meka Srinivasa Rao, ${ }^{\circledR}$ T. C. S. M. Gupta, and Ming Yang ${ }^{\circledR}$<br>Cite This: Ind. Eng. Chem. Res. 2023, 62, 3206-3220<br>Read Online

ACCESS
@ Metrics \& More
@ Article Recommendations
Supporting Information


#### Abstract

This paper elaborates three novel contributions in the field of chemical process safety. The first contribution is the identification and classification of chemical system variabilities into seven broad categories, namely, media, equipment, component, operator, procedural, management, and external (MECOPME). The identified variabilities lead to epistemic and aleatory types of uncertainties in the probabilistic safety analysis. To deal with the uncertainties caused due to the variabilities, a concept of the flexible node is proposed, which demands a failure probability in the flexible range of a lower level to a higher level instead of a fixed static probability. Since the existing techniques are not robust enough to handle the probability range, the classical fault tree is

![img-0.jpeg](img-0.jpeg)
mapped into a statistically more reliable approach of the response surface method (RSM). The unique idea of using RSM in the failure analysis is demonstrated over the fault tree of an overtemperature scenario in a semipilot scale setup for the hydrogenation process and successfully evaluated over an industrial accident of the release prevention barrier scenario. The contour and surface plots of RSM reveal more information than the traditional approach of minimal cut sets. The statistical markers of RSM are a better substitute for the improvement index for sensitivity analysis. The proposed approach deals with chemical system variabilities and the lack of knowledge of exact occurrence probabilities more effectively.


## 1. INTRODUCTION

Chemical process industries (CPI) deal with severe conditions like extreme temperature, pressure, corrosive media, toxic chemicals, flammable materials, and rigorous situations like huge column sizes, complex piping networks, and operations at elevated places and inside confined areas. The safety analysis and modeling of such process facilities are absolutely necessary as any malfunctioning and mishap may lead to a fatal accident scenario. ${ }^{1}$

The fault tree analysis (FTA) is one of the popular techniques for probabilistic safety analysis (PSA), which is static in nature and demands sufficiently reliable failure probabilities for basic events (BEs), which is sometimes not available or difficult to obtain. Because of this, FTA is continuously upgraded by converting it into a dynamic system and mapping into more efficient methods. ${ }^{2}$

The dynamic characteristic of FTA was explained by Čepin and Mavko ${ }^{3}$ and later by Durga Rao et al. ${ }^{4}$ using Monte Carlo simulations. The mapping of FTA into Bayesian network analysis (BNA) for dependable systems was proposed by Bobbio et al., ${ }^{5}$ and the capability of BNA over FTA was compared by Khakzad et al. ${ }^{1}$ Recently, the mapping of FTA into artificial neural networks (ANN) was conceptualized by Sarbayev et al. ${ }^{6}$ to relax the primary assumption of FTA and BNA. Both the
techniques assume that the states of each node are independent, which is partly correct for the intermediate events (IEs) (nodes).

The dynamic FTA and mapping of FTA into BNA are efficient techniques for analyzing time-dependent failures and updating the failure probabilities based on available prior beliefs. However, these techniques are not robust enough while handling unavoidable uncertainty inherently present with failure probabilities. The uncertainties being epistemic (lack of knowledge) and aleatory (intrinsic randomness) in nature require some special attention. ${ }^{7,8}$

To counter the uncertainties, researchers have employed various approaches. Vaezi et al. ${ }^{9}$ demonstrated a two-stage stochastic model for HazMat shipments under uncertainties. $\mathrm{Yu}^{10}$ proposed a two-stage predisaster location and storage model to protect against disaster under uncertain conditions. Hasani and Mokhtari ${ }^{11}$ used multiobjective mixed integer linear programming for designing a relief network under uncertainty.

[^0]
[^0]:    Received: September 15, 2022
    Revised: January 28, 2023
    Accepted: January 31, 2023
    Published: February 13, 2023

![img-1.jpeg](img-1.jpeg)

Figure 1. Proposed seven system variabilities related to chemical process industries.
Poortvliet et al. ${ }^{12}$ employed statistical information to deal with uncertainty in flood risk management. Misuri et al. ${ }^{13}$ presented the evidential network and Credal network to deal with uncertainty. Zhang and Thai ${ }^{14}$ highlighted the limitation of traditional BNA while addressing uncertainties in maritime accident modeling and proposed improvement by adopting interval probabilities. Stroeve et al. ${ }^{15}$ illustrated a Monte Carlo simulation-based approach to address the uncertainty in risk assessment of air traffic management. Zubair et al. ${ }^{16}$ utilized a Monte Carlo N-particle transport-based approach to address the operators safety under different glass materials.

Zhou et al. ${ }^{17}$ incorporated the cognitive reliability error analysis method and Monte Carlo simulations into FTA for LNG transportation. Zubair and Zhang ${ }^{18}$ proposed a methodology and program to estimate parameters like temperature and pressure with utmost reliability while updating them. Khalil Ur et al. ${ }^{19}$ mapped the reliability block diagram with general gates into BNA for safety and reliability analysis of instrumentation and control components. Zubair and Ishag ${ }^{20}$ employed a methodology to map a reactor protection system into a digital plant protection system and control element drive mechanism. The abovementioned approaches are case-specific and poorly demonstrated over chemical systems under uncertainties.

The alternative approach adopted by researchers is the use of a fuzzy crisp set to handle the uncertainties by fuzzing the inputs. This was first demonstrated by Noma and Tanaka ${ }^{21}$ using fuzzy failure possibilities instead of failure probabilities. Afterward, the fuzzy approach is popularly used by various researchers to address the uncertainties. ${ }^{22-27}$ The fuzzy set approach being capable enough to handle vague and imprecise information faces criticism for the tedious task of framing fuzzy rules, conversion of the linguistic term to a corresponding fuzzy number, and heavy dependence on the expert's rich experience in assigning
probabilities and selection of membership function. In addition, the fuzzy outputs can be interpreted in many ways, making this analysis less practical for field applications. ${ }^{28}$

Since the above-discussed approaches are domain-specific and fuzzy crisp set-based approaches over-rely on an expert for interpretation, an alternative approach is required to be explored in PSA. We believe that FTA can be mapped into a suitable technique that can be more appropriate for field issues of chemical process industries, simple in use, less laborious in processing, and efficient in interpreting results.

This paper is structured as follows. The background and novel contributions are discussed in Section 2, in which chemical system variabilities are classified into seven broad categories, a concept of the flexible node is proposed, and the possibility of the use of the response surface method (RSM) in PSA is explored. Section 3 discusses the causes of component variability and efficient RSM designs. The mapping of FTA into RSM and uncertainty modeling is presented in Section 4. In Section 5, the capability of RSM over an industrial problem is demonstrated. Finally, Section 6 summarizes major findings, draws conclusions, and shows directions for future work.

## 2. BACKGROUND AND NOVEL CONTRIBUTIONS

Chemical systems have numerous variabilities, which lead to uncertainties in probabilistic safety analysis. These variabilities are caused due to several reasons, and they must be duly identified and addressed at the design stage along with a detailed safety analysis.

While revamping an old semipilot scale setup designed for vapor-phase reactions and later modified to study the technical feasibility and scale-up of the liquid-phase hydrogenation of heavy base oils, several system variabilities were observed and noted down, which were leading to uncertainty in PSA. On the

basis of the experience associated with revamping of an old setup and scaling-up of the hydrogenation of the heavy base oil process from semibatch mode to continuous mode, the system variabilities are proposed and classified into seven broad categories. These variabilities are media, equipment, component, operator, procedural, management, and external, shortly memorized as MECOPME.

The proposed variabilities and their typical characteristics are illustrated in Figure 1. The MECOPME variabilities are further correlated with the Flixborough accident (1974) for comparison, which suggests that these variabilities can well explain the Flixborough accident, as shown in Table 1. We do not claim that

Table 1. Analysis of the Flixborough Accident Based on MECOPME Variabilities


only these seven chemical system variabilities exist in nature. However, these seven MECOPME variabilities are necessary and sufficient to explain major deviations leading to faults and subsequent safety issues in CPI. The background information and some preliminary work on the hydrogenation of heavy base oils can be accessed through our past work. ${ }^{29-31}$

The media variability is caused by replacing the fluid with another having completely different fluid properties like a difference in viscosity, density, dirtiness, volatility, acidity, or alkalinity. The equipment variability is caused due to modifications done in the original design or bypassing the major types of equipment. The component variability is observed due to the use of a vast range of measuring devices (a variety of sensors with different failure probabilities) in the
industry. The operator variability is because of human attitude and the difference in experience and skills. The procedural variability is observed when any major change or modification in the operating procedure or with the work permit system is executed. The management variability is the result of changes in decisions like increasing or decreasing the production, preponing or postponing maintenance, or a sudden priority change leading to the execution of an unplanned activity. The external variability is the outcome of external disturbances, fluctuations, or unpredictables associated with the system.

Since the identified variabilities lead to uncertainties in the probabilistic safety analysis, some relevant mechanism is required to address it. To counter the uncertainty caused due to variabilities, we put forward the concept of a "flexible node" in the PSA. The flexible node is the basic event (node) demanding the range of probability between the lower level and higher level. Thus, the requirement of a fixed static probability value can be avoided. One can assign all possible probabilities in the range of a lower level to higher level sufficiently broad (i.e., in between $\pm 10$ and $\pm 50 \%$ of occurrence probabilities) such that the probabilities of the uncertain event fall within it.

In this work, we focus on the component variability caused due to the provision for more number of replaceable sensors in chemical systems. The system with the flexibility of multiple interchangeable sensors in a particular basic event (node) is primarily conceptualized as the flexible node in this work. The counterpart of the flexible node can be considered as a fixed node that cannot handle uncertainties caused due to any of the chemical system variabilities.

To overcome the limitations of existing techniques to address the uncertainties, as discussed in Section 1, we present the mapping of FTA into RSM. The RSM is a statistical optimization technique used in chemical engineering problems. Since RSM also demands a range for inputs, the FTA with a range of probability can be well expressed using RSM. Further, the RSM has some merits over other competing techniques, i.e., well-designed simulation runs, better graphical representation, clarity in the analysis of results supported by a wide statistical base, and an efficient regression equation for mathematical modeling.

## 3. COMPONENT VARIABILITY, FLEXIBLE NODE, AND RSM DESIGNS

3.1. Component Variability and the Flexible Node. Due to their requirement of uninterrupted continuous operations,

Table 2. Component Variability in Chemical Systems Conceptualized as the Flexible Node


the process industries may experience the use of interchangeable devices and sensors, leading to component variability. It should be noted that the absence of the same component in the inventory and, at the same time, the priority of production over maintenance may lead to interchangeable devices in chemical process industries. Table 2 lists a few of the applications where interchangeable devices are used in the chemical process leading to the component variability. The nodes or events having such variabilities can be hypothesized as the flexible node.

The traditional PSA using the fault tree approach assumes a single static node (fixed node) without any variability for all of the basic events, whereas the flexible node assumes variability (mainly component variability in the present work) for one or more basic events or nodes. Under such circumstances, the traditional FTA requires mapping into a suitable technique that can model the whole fault tree covering all possible failure probabilities. All possible failure probabilities must fall between a range of lower-level (lower bound) and higher-level (upper bound) failure probabilities, and the same concept is used in RSM.
3.2. RSM Designs. The RSM is the statistical technique of the design of experiments (DOE). The RSM has mainly four useful designs, namely, central composite design (CCD), BoxBehnken design (BBD), Doehlert matrix design, and three-level factorial design. The efficacy of the design can be judged by various statistical markers like $p$-value, analysis of variance (ANOVA), Pearson matrix, $R^{2}$ (goodness of fit), $R^{2}$ predicted, and $R^{2}$ adjusted. ${ }^{32-34}$

Among the four RSM designs, the CCD and BBD are widely used techniques and considered in this work. The CCD design consists of corner points of the cube for linear estimation, a center point of the cube, and star points to estimate the curvature. The BBD design consists of midpoints of the edges of the cube and a center point. The BBD design requires a minimum of three factors, whereas the CCD design can be used with a minimum of two factors. The number of runs vs the number of factors for CCD and BBD designs is compared in Table 3.

Table 3. Runs vs Factors for Competent Designs


${ }^{a} 1 / 2$ fraction. ${ }^{b} 1 / 4096$ fraction. ${ }^{c}$ Minimum runs.

The BBD design is an efficient one, as seen in Table 3; however, it cannot estimate beyond its design points. The CCD design is less efficient, but it allows the estimation beyond the design point due to star points embedded in the design. The detailed criteria for the selection of an appropriate design is discussed by Montgomery. ${ }^{35}$

## 4. GRAPHICAL MAPPING AND UNCERTAINTY MODELING

4.1. Mapping of FTA into RSM. A mapping algorithm should consist of graphical, numerical, and analysis tasks, as demonstrated in Figure 2. The basic events (BEs) of the fault tree have equivalence to factors defined in RSM. The top event (TE) of the fault tree has equivalence with the response in RSM. The intermediate events (IEs) of FTA can be mapped by assigning relevant weights. The typical weights range between 0.1 and 10 . The lower weight of 0.1 gives less importance to the response, whereas the upper weight of 10 gives more importance to the response. Our past experience suggests that the default weight of 1 works well when the response is not overweighted or underweighted. ${ }^{36,37}$

The Boolean gates can be mapped through the selection of appropriate regression models and transformations available in RSM. Each basic event has a fixed failure probability in FTA, whereas the same is mapped through the lower level and higher level in RSM. The minimal cut sets (MCS) of FTA can be presented as two-dimensional (2D) contour and three-dimensional (2D) surface plots in RSM. The traditional FTA depends on an improvement index to perform the sensitivity analysis (SA), whereas the RSM relies on the statistical parameters of ANOVA, $p$-value, and Pearson's product moment correlation coefficient (PPMCC).
4.2. Chemical System with Flexible Nodes Due to Component Variability. In the present work, a simplified version of the fault tree for an overtemperature scenario (OTS) from the hydrogenation of heavy base oil is considered for demonstration. The details of the process flow diagram, equipment list, specifications, and safety analysis using HAZOP and the Bayesian network for hydrogenation of heavy base oil can be accessed through the literature. ${ }^{38-41}$ Figure 3 is the fault tree of a chemical system having two flexible nodes due to the presence of component variability. The basic events $\left({ }^{*} X_{5}\right)$ and $\left({ }^{*} X_{8}\right)$ are two flexible nodes as they have the provision for interchangeable temperature sensors leading to multiple failure possibilities. The flexible node-1 has the provision to use any one sensor out of three sensors (expansion type, resistance type, and thermocouple type). The flexible node-2 is compatible to use any one sensor out of the two sensors (resistance type and thermocouple type) at a time. It should be noted that the safety evaluator is not aware of which sensor will be in service (in ${ }^{*} X_{5}$ and at the same time in ${ }^{*} X_{8}$ ) the moment an undesirable top event occurs.

The occurrence probabilities for all basic events are mentioned in Table 4, which were obtained from Crowl and Louvar ${ }^{38}$ and Lees. ${ }^{39}$ The lower level and higher level are considered sufficiently broad by assigning a moderate deviation of $\pm 15 \%$ from the reported occurrence probabilities. Thus, all nodes have some flexibility in terms of assigning probabilities with additional provision for more flexibility to the flexible nodes (nodes ${ }^{*} X_{5}$ and ${ }^{*} X_{8}$ ) as the lower level and higher levels are $\pm 15 \%$ from the least occurrence and the highest occurrence probabilities (Table 4).

The traditional FTA approach to evaluating TE is to assess all possible combinations and each combination will have a different failure probability. The six possible combinations are as follows: (1) resistance type in ${ }^{*} X_{8}$ and expansion type in ${ }^{*} X_{5}$, (2) resistance type in ${ }^{*} X_{8}$ and resistance type in ${ }^{*} X_{5}$, (3) resistance type in ${ }^{*} X_{8}$ and thermocouple in ${ }^{*} X_{5}$, (4) thermocouple in ${ }^{*} X_{8}$ and expansion type in ${ }^{*} X_{5}$, (5)

![img-2.jpeg](img-2.jpeg)

Figure 2. Graphical mapping of FTA into RSM.
![img-3.jpeg](img-3.jpeg)

Figure 3. Fault tree with flexible nodes due to component variability.
thermocouple in $* X_{8}$ and resistance type in $* X_{2}$, and (6) thermocouple in $* X_{8}$ and thermocouple in $* X_{3}$. Thus, the traditional FTA approach is very lengthy, laborious, and tedious.

The practical approach is to evaluate TE twice by considering the best case using the lowest occurrence probabilities in $* X_{3}$ and $* X_{8}$ and by calculating the worst case using the highest occurrence probabilities in $* X_{3}$ and $* X_{8}$. This will reduce the tedious task of repeated calculations but does not provide a
complete idea for various scenarios. To understand this, we evaluated the best case, worst case, and in-between scenarios by calculating all possible combinations. The TE values for the six combinations in the respective order are as follows: (1) 0.1773 (best case), (2) 0.3017 , (3) 0.3295 , (4) 0.1914 , (5) 0.3256 , and (6) 0.3556 (worst case). This suggests that there are six failure possibilities, each top event has a different minimal cut sets in

Table 4. Occurrence Probabilities of Various Basic Events for OTSa


${ }^{a}$ where ${ }^{*} X_{5}$ and ${ }^{*} X_{8}$ are flexible nodes. ${ }^{b}$ Expansion type. ${ }^{c}$ Resistance type. ${ }^{d}$ Thermoelectric type.
terms of the "importance index" and different sensitivities using the "improvement index".

A total of $12 \mathrm{MCS}\left(X_{i} X_{l}, X_{j} X_{l}\right.$ and $X_{k} X_{l}$ where $\left.i=7, j=8, k=9\right\rangle$ and $l=1,2,4,5$ ) can be obtained for each combination having different cut-set importance. For illustration purpose, 6 important cut sets out of 12 with a higher significance for the best case and worst case are compared in Figure 4a. The cut-set $X_{8} X_{1}$ is the shortest path leading to OTS for the best-case scenario. The cut-set $X_{8} X_{5}$ is the shortest path leading to an undesirable top event for a worst-case scenario. Thus, it is clear that two different shortest paths $\left(X_{8} X_{1}\right.$ and $\left.X_{8} X_{5}\right)$ are obtained for the accident causation in the same fault tree having component variability.

The contribution of each BE leading toward TE is evaluated using sensitivity analysis, as seen in Figure 4b. The $\mathrm{BE}_{1}\left(X_{1}\right)$ shows a maximum improvement index for the best-case scenario, whereas a $\mathrm{BE}_{4}\left({ }^{*} X_{5}\right)$ indicates a maximum improvement index for the worst-case scenario. Thus, the fault tree with component variability exhibits the characteristics of the same MCS with a different significance and different BEs responsible for the same top event. This suggests the requirement of uncertainty modeling in probabilistic safety analysis, which
covers all possibilities in BEs using a probable range if a fault tree has any of the variability proposed in Section 2.

### 4.3. Uncertainty Modeling for Fault Tree with Flexible

Nodes. The uncertainties are classified as epistemic and aleatory in nature. The epistemic uncertainty arises due to a lack of knowledge, small sample size, and an incomplete understanding of the system. This kind of uncertainty is reducible in nature by increasing the knowledge domain of the system and is addressed by classical probability theory, fuzzy set theory, and Dempster-Shafer theory. ${ }^{40-43}$ The aleatory type of uncertainty is observed because of the inherent variability of the system and heterogeneity among the components. Such uncertainty is irreducible and tackled only by probability theory. ${ }^{40-42}$ In this Section 4, the epistemic type of uncertainty is handled for the OTS scenario caused due to component variability.
4.3.1. Modeling Epistemic Type of Uncertainty. The categorization of uncertainties as either epistemic or aleatory is purely based on the model builder and depends on the context and its application. ${ }^{40-42}$ The fault tree of OTS, as shown in Figure 3, can be considered as epistemic in nature since it involves parameter uncertainty in which any type of suitable sensor can be used in flexible nodes ${ }^{*} X_{5}$ and ${ }^{*} X_{8}$ during the continuous operation. In addition to this, the risk evaluator is not aware of which type of sensor is in the service the moment failure occurs.

To model this by mapping FTA into RSM, the first step is the selection of design. The BBD design requires 62 runs, whereas the CCD design needs 152 runs to evaluate 7 factors, as reported in Table 3. We have evaluated both BBD and CCD designs by following the mapping process described in Figure 2. The nodes ${ }^{*} X_{5}$ and ${ }^{*} X_{8}$ are considered as flexible nodes by providing a vast probability range in which all probable possibilities are covered. The BBD and CCD design runs were generated and simulated in Design Expert version 12 and the same was validated using Minitab version 19. (The combination of runs for OTS using BBD and CCD can be accessed through Tables S1 and S2, respectively.)

The model fitting summary for BBD and CCD is given in Table 5. A total of four models were checked, namely, linear, 2 factor interaction (2FI), quadratic, and cubic. The BBD design shows a relatively minimal value of the standard deviation (SD) and relatively higher values of $R^{2}, \operatorname{adj} . R^{2}$, and pred. $R^{2}$ compared to the CCD design. The 2 FI model using BBD was selected to generate the regression equation, ANOVA, and contour and surface plots for MCS analysis. The cubic model shows zero SD with an $R^{2}$ value of 1 for both BBD and CCD designs; however, it adds more square and cubic terms in the regression equation leading to more complexities in analysis.
![img-4.jpeg](img-4.jpeg)

Figure 4. (a) Importance index and (b) sensitivity analysis for the fault tree with flexible nodes.

Table 5. Summary of the Model Fit for OTS with Flexible Nodes Using BBD and CCD


Table 6. Significance of Linear and Interaction Terms in the 2FI Model (BBD)

| linear terms
(7) | $p$-value (linear)
(7) | interaction terms
$(1-7)$ | $p$-value (1-7) | Interaction terms
$(8-14)$ | $p$-value (8-14) | Interaction terms
$(15-21)$ | $p$-value
$(15-21)$  |

![img-5.jpeg](img-5.jpeg)

Figure 5. Contour plots equivalent to MCS using BBD (group 1).

$$ \begin{aligned} \mathrm{TE}(\mathrm{OTS})= & -0.0984+0.2661 X_{1}+0.311 X_{2}+0.311 X_{4}+0.27633 X_{5}+0.2329 X_{7}+0.1986 X_{8}+0.2410 X_{9}-0.44 X_{1}^{*} X_{2} \ & -0.444 X_{1}^{*} X_{4}-0.57479 X_{1}^{*} X_{5}+0.3965 X_{1}^{*} X_{7}+0.4756 X_{1}^{*} X_{8}+0.341 X_{1}^{*} X_{9}-0.3 X_{2}^{*} X_{4}-0.425 X_{2}^{*} X_{5} \ & +0.29 X_{2}^{*} X_{7}+0.351 X_{2}^{*} X_{8}+0.25 X_{2}^{*} X_{9}-0.429 X_{4}^{*} X_{5}+0.296 X_{4}^{*} X_{7}+0.355 X_{4}^{*} X_{8}+0.25 X_{8}^{*} X_{9} \ & +0.38330 X_{5}^{*} X_{7}+0.45973 X_{5}^{*} X_{8}+0.3299 X_{5}^{*} X_{9}-0.4052 X_{7}^{*} X_{8}-0.291 X_{7}^{*} X_{9}-0.3488 X_{8}^{*} X_{9} \end{aligned} $$

The uncoded regression equation for BBD using the 2 FI model is reported as eq 1. Various combinations of factors between the lower level and higher level can be given as an input to eq 1 , and the respective top event response can be obtained using this equation.

The traditional FTA analysis for OTS yields a total of 12 MCS out of which $X_{8} X_{1}$ is the shortest path for the best-case scenario, whereas $X_{8} X_{2}$ is the shortest for the worst-case scenario. In contrast to this, the RSM approach using a 2 FI model yields a total of 21 interaction terms equivalent to MCS in the whole

![img-6.jpeg](img-6.jpeg)

**Figure 6.** Contour plots equivalent to MCS using BBD (group 2).

![img-7.jpeg](img-7.jpeg)

**Figure 7.** (a) Surface plot for the maximum interaction for *X*<sub>8</sub>*X*<sub>5</sub>. (b) Predicted vs actual (OTS).

Range of lower level to higher level. The significance of the interaction terms (based on *p*-value <0.005) is presented in Table 6, in which 10 significant (S) terms and 11 nonsignificant (NS) terms are obtained.

A new finding observed using the RSM approach is the existence of significant interactions between *X*<sub>1</sub>*X*<sub>5</sub>, *X*<sub>4</sub>*X*<sub>5</sub>, *X*<sub>7</sub>*X*<sub>8</sub>, and *X*<sub>8</sub>*X*<sub>9</sub>, which is completely missing and not considered in the classical FTA approach. The *p*-values of these four interaction terms are much lesser than the traditional cut-set *X*<sub>1</sub>*X*<sub>9</sub>, indicating that these four cut sets are more significant and important than *X*<sub>1</sub>*X*<sub>9</sub>. The traditional FTA does not acknowledge this, which suggests looking beyond the traditional approach.

The interaction terms can be graphically represented as contour and surface plots. For better representation, the contour plots are grouped into two parts, as depicted in Figure 5 (group 1) and Figure 6 (group 2). The least significant cut sets have a more light green color and the significant cut sets have a more dark green color. The significance of cut-sets *X*<sub>1</sub>*X*<sub>5</sub>, *X*<sub>1</sub>*X*<sub>8</sub>, *X*<sub>2</sub>*X*<sub>5</sub>, *X*<sub>4</sub>*X*<sub>5</sub>, *X*<sub>8</sub>*X*<sub>4</sub>, *X*<sub>8</sub>*X*<sub>5</sub>, and *X*<sub>7</sub>*X*<sub>8</sub> having a more dark green color with a response scale above 0.36 is presented in contour plots shown in Figures 5 and 6.

The maximum interaction and maxima of response are observed for the interaction *X*<sub>8</sub>*X*<sub>5</sub> with a typical interaction range between 0.1583 and 0.4175 as visible in a 3D surface plot in Figure 7a. Further, the parity plot for predicted vs actual using the BBD design is shown in Figure 7b, indicating the perfect fit for the 2FI model.

The physical significance of cut-set *X*<sub>5</sub>*X*<sub>8</sub> is that we are interested in quantifying the overtemperature scenario and the cut-set *X*<sub>5</sub>*X*<sub>8</sub> is the combination of failure for *X*<sub>5</sub> (local temperature transmitter failure) and *X*<sub>8</sub> (remote temperature

![img-8.jpeg](img-8.jpeg)

Figure 8. Response of Y (top event) against the factors X (basic events).

![img-9.jpeg](img-9.jpeg)

Figure 9. (a) PPMCC matrix for OTS. (b) SA using PPMCC for OTS.

![img-10.jpeg](img-10.jpeg)

Figure 10. Fault tree of the RPB scenario.

Transmitter failure). If both the temperature transmitters fail, then auto mode and manual mode fail simultaneously leading to an overtemperature scenario.

The effect of various factors (seven factors for overtemperature scenario) on the top event is shown in Figure 8. This represents the span of the individual factor and its respective effect on TE. This can be further validated using sensitivity analysis. The sensitivity analysis in RSM can be performed using the PPMCC matrix shown in Figure 9a, which can be further plotted as a pie chart, as shown in Figure 9b, to understand the order of sensitivity. The overall order of sensitivity can be further arranged as *X<sub>5</sub>* *X<sub>8</sub>* > *X<sub>1</sub>* > *X<sub>7</sub>* > *X<sub>9</sub>* > *X<sub>4</sub>* > *X<sub>2</sub>*, which represents the whole range between the best-case and the worst-case scenario.

Table 7. Occurrence Probabilities of Various Basic Events for the RPB Scenario


![img-11.jpeg](img-11.jpeg)

Figure 11. (a) 3D surface plot for $\mathrm{BE}_{9} \mathrm{BE}_{12}$. (b) Parity of the improvement index with PPMCC for SA.
* $X_{5}$ is the most sensitive because of two main reasons. The first is because $* X_{5}$ is the local temperature measurement and failure of this has a direct impact on the overtemperature as the operator cannot take any preventive or mitigating actions in case of emergency due to unavailability of temperature readings. The second is the broad range of $P\left({ }^{*} X_{5}\right)=0.0266-0.4055$, which impacts the maximum on the top event. In contrast to this, the node $X_{2}$ is the least significant as the operator inexperience can be tackled by auto mode operation, and the low value of $P\left(X_{2}\right)=$ 0.011 will have a less impact on the top event. The same is reflected in Figures 8 and 9.

## 5. ANALYSIS OF THE BENCHMARKING PROBLEM USING THE RSM APPROACH

### 5.1. Fault Tree of the Release Prevention Barrier (RPB).

This section will evaluate the modeling capability of the RSM approach to the benchmarking problem and summarize critical observations and comments. To assess the capability of the RSM approach, we have selected a fault tree of the release prevention barrier (RPB) having 21 BEs, 10 IEs, and associated TE. The fault tree of RPB was proposed by Adedigba et al., ${ }^{44}$ based on the findings from the Tesoro Anacortes Refinery accident (2010). The heat exchanger (E-6600E) was ruptured due to a hightemperature hydrogen attack igniting hydrogen and naphtha leading to severe explosion causing seven fatalities and damage to the plant. The fault tree of the RPB scenario is reconstructed and shown in Figure 10.

The failure modeling for RPB is performed in two parts. In the first part, the RSM approach is compared with the traditional FTA approach. The second part models the aleatory type of uncertainty in RPB by assuming that all BEs of the RPB scenario have some system variabilities. The failure occurrence probabilities, lower and higher levels ( $\pm 15 \%$ deviation), are reported in Table 7.
5.1.1. Evaluating RPB Using FTA and RSM. To evaluate RPB using the RSM approach and subsequently, its comparison with FTA, the lower level and higher level were considered with $\pm 15 \%$ deviation from occurrence probabilities reported by Adedigba et al. ${ }^{44}$ The combination of 348 runs and respective responses for RPB using BBD was generated (refer to Table S3).

The first part of the analysis suggests that all available models are significant with $R^{2}$ values of 0.999 and more. The ANOVA suggests that $\mathrm{BE}_{4}, \mathrm{BE}_{8}, \mathrm{BE}_{13}, \mathrm{BE}_{14}, \mathrm{BE}_{15}, \mathrm{BE}_{18}, \mathrm{BE}_{19}$, and their interactions are nonsignificant. The interactions between $\mathrm{BE}_{12}$, $\mathrm{BE}_{9}, \mathrm{BE}_{10}$, and $\mathrm{BE}_{7}$ were more significant compared to others. The most significant interaction was obtained between $\mathrm{BE}_{9} \mathrm{BE}_{12}$ and $\mathrm{BE}_{10} \mathrm{BE}_{12}$.

The 3D surface plot of $\mathrm{BE}_{9} \mathrm{BE}_{12}$ is presented in Figure 11a. The spread of TE is in the range of $0.07459-0.09393$ with a TE probability of 0.0842 (based on Adedigba's data) lying somewhere in the middle of the plot. The regression equation generated using the 2 FI model has a total of 232 terms bifurcated as 21 linear terns, 210 interaction terms, and 1 constant term. The sensitivity analysis using an improvement index for the FTA approach and PPMCC for the RSM approach is plotted in Figure 11b, and both the approaches are comparable. This suggests that PPMCC can be adopted for sensitivity analysis while using the RSM approach.
5.1.2. Modeling Aleatory Type of Uncertainty. Out of the seven proposed variabilities, six variabilities (except external variability) are quite possible in the RPB scenario (refer column 2 in Table 7). Since the evaluators are not aware of the probable possibilities for each variability, the RPB scenario is modeled for an aleatory type of uncertainty by assuming all nodes as flexible nodes. To model this, a vast range must be provided for lower and higher levels, in which we have assigned the lower level to 0 and higher level to 1 . This is more of a black-box model approach in which all BEs are on the same level, and the importance of each basic event (factors) purely depends upon its Boolean relation toward the top event (response). The combination of 348 runs using BBD for RPB with an aleatory approach was generated (refer to Table S4).

The spread of TE for RPB with aleatory is obtained in the range of $0.9765-1$ for BBD, indicating skewness in the TE probability distribution. The TE distribution shift toward 1 indicates more occurrence chances for the RPB scenario as all intermediate events are connected with the top event using the OR gate relation.

The model fitting for the aleatory type of uncertainty in RPB is summarized in Table 8. The linear model is very poor and the

Table 8. Summary of the Model Fit for the Aleatory Type of Uncertainty in the RPB Scenario


cubic model is perfect in fitting. The 2 FI and quadratic models are almost similar though the 2 FI model is slightly better than the quadratic model. The cubic model can be selected for more detailed and rigorous analysis; however, a simple and practical 2 FI model was selected to produce regression equation, ANOVA, and contour and surface plots for demonstration purposes.

The interaction of $\mathrm{BE}_{12}$ with $\mathrm{BE}_{11}, \mathrm{BE}_{9}$, and $\mathrm{BE}_{10}$ are significant in the whole tree network. The interaction of $\mathrm{BE}_{11} \mathrm{BE}_{12}$ is demonstrated using a contour plot and surface plot presented in Figure 12a,b. The red color used in the same figure indicates a much higher value of TE shifting toward 1 . The green color indicates a lesser effect on TE, whereas the yellow color indicates a moderate effect on TE.

$$
\begin{aligned}
& \mathrm{TE}(\mathrm{RPB})=0.890274+0.0177 \mathrm{BE}_{1}+0.01563 \mathrm{BE}_{2} \\
& +0.01817 \mathrm{BE}_{3}+0.01518 \mathrm{BE}_{4}+0.01659 \mathrm{BE}_{5} \\
& +0.01675 \mathrm{BE}_{6}+0.02079 \mathrm{BE}_{7}+0.01325 \mathrm{BE}_{8} \\
& +0.05081 \mathrm{BE}_{9}+0.04969 \mathrm{BE}_{10}+0.05814 \mathrm{BE}_{11} \\
& +0.05053 \mathrm{BE}_{12}-0.00936 \mathrm{BE}_{13}-0.00646 \mathrm{BE}_{14} \\
& -0.00208 \mathrm{BE}_{15}+0.00504 \mathrm{BE}_{16}+0.0071 \mathrm{BE}_{17} \\
& +0.01045 \mathrm{BE}_{18}+0.00664 \mathrm{BE}_{19}+0.01431 \mathrm{BE}_{20} \\
& +0.00399 \mathrm{BE}_{21}-0.00515 \mathrm{BE}_{1} \mathrm{BE}_{2}+ \\
& \cdots+0.002953 \mathrm{BE}_{20} \mathrm{BE}_{21}
\end{aligned}
$$

Regression eq 2, is generated using the 2 FI model has a total of 232 terms bifurcated as 21 linear terms, 210 interaction terms, and 1 constant term. Out of the 231 terms (excluding the constant term from 232 terms), 81 terms are highly significant ( $p$-value less than 0.0001 ), 68 terms are significant ( $p$-value in between 0.0001 and 0.05 ), 69 terms are nonsignificant ( $p$-value in the range of $0.05-0.5$ ), and 13 terms are highly insignificant or have almost no effect on the top event as their $p$-values are much higher.

The sensitivity analysis reveals that only $\mathrm{BE}_{13}$ is a nonsignificant basic event due to a very high $p$-value ( 0.2069 ). The basic events $\mathrm{BE}_{14}$ and $\mathrm{BE}_{15}$ are significant, but the $p$-values are much closer to a reference value of 0.05 . It suggests that $\mathrm{BE}_{13}$, $\mathrm{BE}_{14}$, and $\mathrm{BE}_{15}$ have a minimal impact on RPB. This can be explained by the structure of the fault tree in which $\mathrm{BE}_{13}, \mathrm{BE}_{14}$, and $\mathrm{BE}_{15}$ are at the bottom connected with the AND gate and the chances of a simultaneous failure of these three basic events are very less. The same sensitivity trend is reflected in Figure 13.

The sensitivity analysis also identifies basic events $\mathrm{BE}_{11}, \mathrm{BE}_{9}$, $\mathrm{BE}_{12}$, and $\mathrm{BE}_{10}$ as significantly affecting the top event in a given order. The basic events $\mathrm{BE}_{9}$ to $\mathrm{BE}_{12}$ are the most sensitive events because they are much closer to the top event with the OR gate operation. The remaining basic events have intermediate events in between the top events, and hence the sensitivity of these events is quite less.

Thus, the aleatory approach of assigning the lower level as 0 and the higher level as 1 draws an interesting finding that $\mathrm{BE}_{11}$ was relatively very less dominating in the FTA approach (refer Figure 11b) due to the lower occurrence probability assigned in the analysis, but it is the most sensitive event (refer Figure 13) leading to the shortest path in the accident causation if the actual probability is much higher than reported by Adedigba et al. ${ }^{44}$
5.2. Comparison, Observations, and Comments. The RPB scenario, evaluated in the previous Section 5.1, is also

![img-12.jpeg](img-12.jpeg)

Figure 12. (a) 2D Contour plot. (b) 3D Surface plot for RPB with the aleatory uncertainty.

![img-13.jpeg](img-13.jpeg)

Figure 13. SA using PPMCC for RPB with aleatory type uncertainty.

studied by Yazdi and Kabir^{7} using a combination of the fuzzy-BNA approach and by Sarbayev et al.,^{6} using the ANN approach. So it would be interesting to compare the RSM approach with fuzzy and ANN approaches.

Yazdi and Kabir^{7} have relied on three independent experts' knowledge and assigned weighing scores based on decided criteria. The sensitivity analysis in the fuzzy-BNA approach is performed using two different tools, Birnbaum importance measure (BIM) and ratio of variation (RoV) as elaborated by Yazdi and Kabir.^{7} Against this, Sarbayev et al.^{6} have randomly generated 500 runs, trained the network using 450 runs, and validated using the remaining runs. The sensitivity analysis in the ANN approach was done using criticality importance (CRIT), as discussed by Sarbayev et al.^{6}

The following observations and comments can be drawn from Table 9, which also highlight the strength of the RSM approach over other techniques.

- The FTA and RSM (with ±15% deviation in level) yield the same results for SA though it is performed by two different tools, namely, improvement index and PPMCC.
- The BIM and RoV produce similar results for the fuzzy-BNA approach but they are not in agreement with PPMCC for RSM-aleatory and CRIT analysis for ANN.
- The order of sensitivity of the first three BEs (BE_{12}, BE_{9}, and BE_{10} in the mentioned order) are in agreement except for modeling the aleatory type of uncertainty using the RSM.
- BE_{11} is identified as highly sensitive toward TE based on statistical evidence by assigning occurrence probability in the range of 0–1. The other approaches consider its significance but do not give the desired level of importance.
- The common least significant events in most of the approaches are BE_{12}, BE_{14}, and BE_{15} in which ANN fails to identify BE_{13} and BE_{15}.
- The least significant events identified by RSM and fuzzy-BNA are in close agreement because both the approaches can handle uncertainty, whereas the ANN approach heavily depends on its quality and quantity of the training set.
- Fuzzy-BNA by BIM and RoV evaluate the same ranking for more than one event and thus the exact order for SA is difficult to obtain using the fuzzy approach compared to RSM and ANN approaches, as seen in Table 9 (refer to the last two columns).

# 6. CONCLUSIONS AND FURTHER WORK

To address any of the variability, the concept of flexible node is proposed, which demands the probability range between the lower level and higher level. The BEs can be converted into flexible nodes by assigning a probability range sufficiently broad such that all probable possibilities are covered in it. This is demonstrated by mapping FTA into RSM, which is a statistically sound technique with the best graphical representation of results and an efficient mathematical model. The OTS scenario demonstrated in this work had two flexible nodes because of the provision for interchangeable sensors. The traditional FTA requires exploring all possible combinations against which the RSM requires to evaluate once covering a whole range of possibilities. The RSM generates more number of cut sets supported by the p-value, suggesting looking beyond the traditional approaches.

The BBD design is observed to be more efficient than the CCD design, as demonstrated over the OTS scenario. The aleatory type of uncertainty is possible if more number of nodes

Table 9. SA for RPB Using Various Approaches (FTA, ANN, Fuzzy-BNA, and RSM)


are flexible. This can be handled by assigning a sufficiently broad range of probability to almost all nodes. This also helps to identify the most sensitive BE having the highest impact on TE purely based on its Boolean relation toward TE as demonstrated over the RPB scenario.

Further work will be devoted to model more complex industrial fault scenarios having all seven variabilities. Additionally, it would be interesting to evaluate the complex system using the RSM-BNA approach and further mapping the multivariate regression into the supervised algorithm for machine learning.

## ASSOCIATED CONTENT

## Supporting Information

The Supporting Information is available free of charge at https://pubs.acs.org/doi/10.1021/acs.iecr.2c03329.

OTS scenario with epistemic uncertainty using the BBD design ( 62 runs) (Table S1); OTS scenario with epistemic uncertainty using the CCD design (152 runs) (Table S2); RPB scenario without uncertainty using the RSM (BBD design_348 runs) (Table S3); and RPB scenario with aleatory uncertainty using the BBD design (348 runs) (Table S4) (PDF)

## AUTHOR INFORMATION

## Corresponding Authors

Meka Srinivasa Rao - Department of Chemical Engineering, Dharmsinh Desai University, Nadiad 387001, India; -orcid.org/0000-0002-0501-7667; Email: msrao@ ddu.ac.in
Ming Yang - Safety and Security Science Section, Department of Values, Technology, and Innovation, Faculty of Technology, Policy, and Management, Delft University of Technology, 2628 BX Delft, The Netherlands; Centre of Hydrogen Energy, Institute of Future Energy, Universiti Teknologi Malaysia, 81310 UTM Johor Bahru, Johor, Malaysia; National Centre
of Maritime Engineering and Hydrodynamics, Australia Maritime College, University of Tasmania, Launceston, TAS 7248, Australia; -orcid.org/0000-0002-6544-9226; Email: m.yang-1@tudelft.nl

## Authors

Siddharth Modi - Department of Chemical Engineering, Dharmsinh Desai University, Nadiad 387001, India
T. C. S. M. Gupta - Research \& Development Centre, APAR Industries Ltd, Navi Mumbai 400701, India
Complete contact information is available at:
https://pubs.acs.org/10.1021/acs.iecr.2c03329

## Notes

The authors declare no competing financial interest.

## ACKNOWLEDGMENTS

This work is supported by D. D. University, Nadiad, and APAR Industries Limited, Mumbai. The present work is the fourth step (process safety evaluation step) as part of the joint research project on the feasibility of hydrogenation of heavy base oils from semibatch mode to continuous mode.

## ABBREVIATIONS


TE top event
MCS minimal cut sets
SA sensitivity analysis
ANOVA analysis of variance
PPMCC Pearson product moment correlation coefficient
OTS overtemperature scenario
SD standard deviation
(S) significant terms
(NS) nonsignificant terms
RPB release prevention barrier
BIM Birnbaum importance measure
RoV ratio of variation
CRIT criticality importance
